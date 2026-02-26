#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_heston_process.py

Heston stochastic-volatility model and Variance Gamma (VG) process --
two workhorse models from the stochastic-volatility / Levy-process toolkit.

Based on Processes.py from cantaro86's "Financial-Models-Numerical-Methods"
(https://github.com/cantaro86/Financial-Models-Numerical-Methods).
Adapted as a self-contained educational module -- no local imports required.

Classes
-------
Heston_process : Euler discretisation of the Heston SDE with correlated
                 Brownian motions and full-truncation (reflection) scheme.
VG_process     : Variance Gamma process via Brownian subordination (time-
                 changed Brownian motion with gamma subordinator).  Includes
                 terminal-value sampling, path generation, and parameter
                 estimation (Method of Moments + MLE).
"""

import numpy as np
import scipy.stats as ss
from scipy.optimize import minimize
from scipy.special import kv as bessel_kv  # modified Bessel function K_v


# ---------------------------------------------------------------------------
# VG probability density (needed for MLE fitting -- kept self-contained)
# ---------------------------------------------------------------------------

def _vg_pdf(x, T, c, theta, sigma, kappa):
    """
    Probability density of the Variance-Gamma process evaluated at *x*.

    Uses the closed-form expression involving the modified Bessel function
    of the second kind K_v.

    Parameters
    ----------
    x : ndarray
        Evaluation points (log-returns or increments).
    T : float
        Time increment.
    c : float
        Drift/convexity correction.
    theta : float
        Drift of the subordinated Brownian motion.
    sigma : float
        Volatility of the subordinated Brownian motion.
    kappa : float
        Variance rate of the gamma subordinator.

    Returns
    -------
    ndarray
        PDF values at each point in *x*.
    """
    nu = T / kappa
    # Shift to centred variable
    y = x - c * T

    # Parameters for the Bessel representation
    a = theta / (sigma ** 2)
    b = np.sqrt(theta ** 2 + 2 * sigma ** 2 / kappa) / (sigma ** 2)

    # Bessel order
    order = nu - 0.5

    # Avoid numerical issues for very small |y|
    eps = 1e-30
    abs_y = np.maximum(np.abs(y), eps)

    # log-pdf for numerical stability
    log_front = (
        nu * np.log(b)
        + (nu - 0.5) * np.log(abs_y)
        + a * y
        - np.log(sigma)
        - 0.5 * np.log(np.pi)
        - (nu) * np.log(2)
        - np.log(ss.gamma(nu).expect(lambda t: 1))  # log(Gamma(nu)) via loggamma
    )
    # Use scipy loggamma for better numerics
    from scipy.special import gammaln
    log_front = (
        nu * np.log(b)
        + (nu - 0.5) * np.log(abs_y)
        + a * y
        - np.log(sigma)
        - 0.5 * np.log(np.pi)
        - nu * np.log(2)
        - gammaln(nu)
    )

    # Bessel K_order(b * |y|)
    bk = bessel_kv(order, b * abs_y)

    # Combine (use log to avoid overflow, then exponentiate)
    pdf = np.exp(log_front) * bk
    # Clean up any NaN/inf from extreme tails
    pdf = np.where(np.isfinite(pdf), pdf, 0.0)
    return pdf


# ---------------------------------------------------------------------------
# Heston stochastic-volatility process
# ---------------------------------------------------------------------------

class Heston_process:
    """
    Heston stochastic-volatility model.

    Stock price and instantaneous variance follow the coupled SDEs:

        dS/S = mu dt + sqrt(v) dW_1
        dv   = kappa (theta - v) dt + sigma sqrt(v) dW_2

    with  Corr(dW_1, dW_2) = rho.

    The Euler scheme uses *full truncation* (reflection) to keep the
    variance non-negative: v(t+dt) = |...|.

    Parameters
    ----------
    mu : float
        Drift of the stock price.
    rho : float
        Correlation between dW_1 and dW_2 (|rho| <= 1).
    sigma : float
        Volatility-of-volatility (vol-of-vol, >= 0).
    theta : float
        Long-run mean of the variance process (>= 0).
    kappa : float
        Mean-reversion speed of the variance (>= 0).
    """

    def __init__(self, mu=0.05, rho=-0.7, sigma=0.3, theta=0.04, kappa=1.5):
        self.mu = mu
        if np.abs(rho) > 1:
            raise ValueError("|rho| must be <= 1")
        self.rho = rho
        if theta < 0 or sigma < 0 or kappa < 0:
            raise ValueError("sigma, theta, kappa must be non-negative")
        self.theta = theta
        self.sigma = sigma
        self.kappa = kappa

    def path(self, S0, v0, N, T=1):
        """
        Simulate one path of the Heston model via Euler-Maruyama with
        correlated Brownian motions and reflection for the variance.

        Parameters
        ----------
        S0 : float
            Initial stock price.
        v0 : float
            Initial instantaneous variance.
        N : int
            Number of time points (N-1 time steps).
        T : float
            Time horizon in years.

        Returns
        -------
        S : ndarray, shape (N,)
            Simulated stock-price path.
        v : ndarray, shape (N,)
            Simulated variance path.
        """
        # Correlated bivariate normal draws
        MU = np.array([0, 0])
        COV = np.array([[1, self.rho], [self.rho, 1]])
        W = ss.multivariate_normal.rvs(mean=MU, cov=COV, size=N - 1)
        W_S = W[:, 0]  # drives stock price
        W_v = W[:, 1]  # drives variance

        T_vec, dt = np.linspace(0, T, N, retstep=True)
        dt_sq = np.sqrt(dt)

        X = np.zeros(N)      # log-price
        v = np.zeros(N)      # variance
        X[0] = np.log(S0)
        v[0] = v0

        for t in range(N - 1):
            v_sq = np.sqrt(v[t])
            # Variance: Euler + reflection (full truncation)
            v[t + 1] = np.abs(
                v[t]
                + self.kappa * (self.theta - v[t]) * dt
                + self.sigma * v_sq * dt_sq * W_v[t]
            )
            # Log-price
            X[t + 1] = (
                X[t]
                + (self.mu - 0.5 * v[t]) * dt
                + v_sq * dt_sq * W_S[t]
            )

        return np.exp(X), v

    def paths(self, S0, v0, N, T=1, n_paths=1):
        """
        Simulate multiple independent Heston paths.

        Parameters
        ----------
        S0, v0, N, T : see ``path``.
        n_paths : int
            Number of independent paths.

        Returns
        -------
        S_all : ndarray, shape (N, n_paths)
            Stock-price paths.
        v_all : ndarray, shape (N, n_paths)
            Variance paths.
        """
        S_all = np.zeros((N, n_paths))
        v_all = np.zeros((N, n_paths))
        for i in range(n_paths):
            S_all[:, i], v_all[:, i] = self.path(S0, v0, N, T)
        return S_all, v_all


# ---------------------------------------------------------------------------
# Variance Gamma process
# ---------------------------------------------------------------------------

class VG_process:
    """
    Variance Gamma (VG) process via Brownian subordination.

    The VG process is a Brownian motion with drift, time-changed by a
    gamma subordinator:

        X(t) = c*t + theta * G(t) + sigma * W(G(t))

    where G(t) ~ Gamma(t/kappa, kappa) and W is a standard Brownian motion.

    Parameters
    ----------
    r : float
        Risk-free rate (used for the martingale correction in exp_RV).
    sigma : float
        Volatility of the subordinated Brownian motion (> 0).
    theta : float
        Drift of the subordinated Brownian motion.
    kappa : float
        Variance rate of the gamma subordinator (> 0).
    """

    def __init__(self, r=0.05, sigma=0.2, theta=-0.14, kappa=0.2):
        self.r = r
        self.c = self.r  # drift parameter
        self.theta = theta
        self.kappa = kappa
        if sigma < 0:
            raise ValueError("sigma must be non-negative")
        self.sigma = sigma

        # Analytic moments of the 1-year VG increment
        self.mean = self.c + self.theta
        self.var = self.sigma ** 2 + self.theta ** 2 * self.kappa
        self.skew = (
            (2 * self.theta ** 3 * self.kappa ** 2
             + 3 * self.sigma ** 2 * self.theta * self.kappa)
            / self.var ** 1.5
        )
        self.kurt = (
            (3 * self.sigma ** 4 * self.kappa
             + 12 * self.sigma ** 2 * self.theta ** 2 * self.kappa ** 2
             + 6 * self.theta ** 4 * self.kappa ** 3)
            / self.var ** 2
        )

    def exp_RV(self, S0, T, N):
        """
        Generate N terminal exponential-VG prices S_T = S_0 exp((r - w)T + VG_T)
        with martingale correction w.

        Parameters
        ----------
        S0 : float
            Initial stock price.
        T : float
            Time to maturity (years).
        N : int
            Number of samples.

        Returns
        -------
        ndarray, shape (N, 1)
            Terminal stock prices.
        """
        # Martingale correction
        w = -np.log(1 - self.theta * self.kappa - self.kappa / 2 * self.sigma ** 2) / self.kappa

        rho = 1 / self.kappa
        G = ss.gamma(rho * T).rvs(N) / rho  # Gamma RV with mean T
        Norm = ss.norm.rvs(0, 1, N)
        VG = self.theta * G + self.sigma * np.sqrt(G) * Norm
        S_T = S0 * np.exp((self.r - w) * T + VG)
        return S_T.reshape((N, 1))

    def path(self, T=1, N=10000, paths=1):
        """
        Generate VG process paths via gamma subordination.

        At each time step dt the gamma increment G_i ~ Gamma(dt/kappa, kappa)
        and the VG increment is:

            dX = c*dt + theta * G_i + sigma * sqrt(G_i) * Z_i

        Parameters
        ----------
        T : float
            Time horizon (years).
        N : int
            Number of time points (N-1 time steps).
        paths : int
            Number of independent paths.

        Returns
        -------
        X : ndarray, shape (paths, N)
            Simulated VG paths (rows = paths).
        """
        dt = T / (N - 1)
        X0 = np.zeros((paths, 1))
        G = ss.gamma(dt / self.kappa, scale=self.kappa).rvs(size=(paths, N - 1))
        Norm = ss.norm.rvs(loc=0, scale=1, size=(paths, N - 1))
        increments = self.c * dt + self.theta * G + self.sigma * np.sqrt(G) * Norm
        X = np.concatenate((X0, increments), axis=1).cumsum(axis=1)
        return X

    def fit_from_data(self, data, dt=1, method="MM"):
        """
        Estimate VG parameters from observed increments.

        Three methods are available:
        - ``"MM"``         : Method of Moments (closed-form, fast).
        - ``"Nelder-Mead"`` : MLE via Nelder-Mead simplex.
        - ``"L-BFGS-B"``  : MLE via bounded quasi-Newton.

        Parameters
        ----------
        data : ndarray
            Observed increments (e.g. daily log-returns).
        dt : float
            Time increment corresponding to one observation.
        method : str
            ``"MM"``, ``"Nelder-Mead"``, or ``"L-BFGS-B"``.
        """
        X = data

        # ----- Method of Moments initial estimates -----
        sigma_mm = np.std(X) / np.sqrt(dt)
        kappa_mm = dt * ss.kurtosis(X) / 3
        if kappa_mm <= 0:
            kappa_mm = 0.01  # safeguard
        theta_mm = np.sqrt(dt) * ss.skew(X) * sigma_mm / (3 * kappa_mm)
        c_mm = np.mean(X) / dt - theta_mm

        if method == "MM":
            self.c = c_mm
            self.theta = theta_mm
            self.sigma = sigma_mm
            self.kappa = kappa_mm
            self._update_moments()
            return

        # ----- MLE via numerical optimisation -----
        def neg_log_lik(x, data, T):
            pdf_vals = _vg_pdf(data, T, x[0], x[1], x[2], x[3])
            pdf_vals = np.maximum(pdf_vals, 1e-300)
            return -np.sum(np.log(pdf_vals))

        if method == "L-BFGS-B":
            if theta_mm < 0:
                bounds = [(-0.5, 0.5), (-0.6, -1e-15), (1e-15, 1), (1e-15, 2)]
            else:
                bounds = [(-0.5, 0.5), (1e-15, 0.6), (1e-15, 1), (1e-15, 2)]
            result = minimize(
                neg_log_lik,
                x0=[c_mm, theta_mm, sigma_mm, kappa_mm],
                method="L-BFGS-B",
                args=(X, dt),
                tol=1e-8,
                bounds=bounds,
            )
        elif method == "Nelder-Mead":
            result = minimize(
                neg_log_lik,
                x0=[c_mm, theta_mm, sigma_mm, kappa_mm],
                method="Nelder-Mead",
                args=(X, dt),
                options={"disp": False, "maxfev": 3000},
                tol=1e-8,
            )
        else:
            raise ValueError(f"Unknown method: {method}")

        print(f"  Optimiser: {result.message}")
        self.c, self.theta, self.sigma, self.kappa = result.x
        self._update_moments()

    def _update_moments(self):
        """Recompute analytic moments after parameter changes."""
        self.mean = self.c + self.theta
        self.var = self.sigma ** 2 + self.theta ** 2 * self.kappa
        self.skew = (
            (2 * self.theta ** 3 * self.kappa ** 2
             + 3 * self.sigma ** 2 * self.theta * self.kappa)
            / self.var ** 1.5
        )
        self.kurt = (
            (3 * self.sigma ** 4 * self.kappa
             + 12 * self.sigma ** 2 * self.theta ** 2 * self.kappa ** 2
             + 6 * self.theta ** 4 * self.kappa ** 3)
            / self.var ** 2
        )


# ---------------------------------------------------------------------------
# Main demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    np.random.seed(42)

    # ==================================================================
    # 1. Heston stochastic-volatility model
    # ==================================================================
    print("=" * 65)
    print("1. Heston Stochastic-Volatility Model")
    print("=" * 65)

    heston = Heston_process(mu=0.05, rho=-0.7, sigma=0.3, theta=0.04, kappa=1.5)
    print(f"  Parameters:")
    print(f"    mu    = {heston.mu}   (stock drift)")
    print(f"    rho   = {heston.rho}  (correlation)")
    print(f"    sigma = {heston.sigma}  (vol-of-vol)")
    print(f"    theta = {heston.theta}  (long-run variance)")
    print(f"    kappa = {heston.kappa}  (mean-reversion speed)")
    print(f"  Feller condition 2*kappa*theta > sigma^2 : "
          f"{2*heston.kappa*heston.theta:.3f} > {heston.sigma**2:.3f} -> "
          f"{'SATISFIED' if 2*heston.kappa*heston.theta > heston.sigma**2 else 'VIOLATED'}")

    S0, v0, N_heston, T_heston = 100, 0.04, 1000, 2
    n_paths_h = 5
    S_all, v_all = heston.paths(S0, v0, N_heston, T_heston, n_paths=n_paths_h)
    t_heston = np.linspace(0, T_heston, N_heston)

    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

    for p in range(n_paths_h):
        axes[0].plot(t_heston, S_all[:, p], linewidth=0.8)
    axes[0].set_title("Heston Model -- Stock Price Paths")
    axes[0].set_ylabel("S(t)")
    axes[0].grid(True, alpha=0.3)

    for p in range(n_paths_h):
        axes[1].plot(t_heston, v_all[:, p], linewidth=0.8)
    axes[1].axhline(heston.theta, color="k", linewidth=1.5, linestyle="--",
                     label=f"Long-run variance theta = {heston.theta}")
    axes[1].set_title("Heston Model -- Variance Paths (Mean-Reverting)")
    axes[1].set_xlabel("Time (years)")
    axes[1].set_ylabel("v(t)")
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_heston_paths.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_heston_paths.png")
    plt.close()

    # --- Variance mean-reversion demonstration ---
    print()
    print("  Variance mean-reversion demonstration:")
    print("  Starting variance far from long-run level...")

    heston_demo = Heston_process(mu=0.05, rho=-0.7, sigma=0.15, theta=0.04, kappa=3.0)
    v0_high, v0_low = 0.16, 0.005

    fig, ax = plt.subplots(figsize=(12, 5))
    for v0_start, color, label in [(v0_high, "tomato", f"v0={v0_high} (high start)"),
                                    (v0_low, "steelblue", f"v0={v0_low} (low start)")]:
        for _ in range(3):
            _, v_path = heston_demo.path(S0, v0_start, N=800, T=3)
            ax.plot(np.linspace(0, 3, 800), v_path, color=color, alpha=0.5, linewidth=0.7)
        # Legend proxy
        ax.plot([], [], color=color, linewidth=1.5, label=label)

    ax.axhline(heston_demo.theta, color="k", linewidth=2, linestyle="--",
               label=f"theta = {heston_demo.theta}")
    ax.set_title("Heston Variance: Mean-Reversion from Different Starting Points")
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("v(t)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_heston_mean_reversion.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_heston_mean_reversion.png")
    plt.close()

    # --- Heston terminal distribution ---
    print()
    print("  Heston terminal distribution (Monte Carlo, 50 000 paths)...")
    n_mc = 50_000
    S_mc = np.zeros(n_mc)
    for i in range(n_mc):
        S_path, _ = heston.path(S0, v0, N=252, T=1)
        S_mc[i] = S_path[-1]

    log_ret = np.log(S_mc / S0)
    print(f"    E[log(S_T/S_0)]  = {log_ret.mean():.4f}")
    print(f"    Std[log(S_T/S_0)] = {log_ret.std():.4f}")
    print(f"    Skewness          = {ss.skew(log_ret):.4f}")
    print(f"    Excess kurtosis   = {ss.kurtosis(log_ret):.4f}")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(log_ret, bins=150, density=True, alpha=0.6, color="steelblue",
            label="Heston log-return")
    # Overlay normal with matched mean/var
    x_grid = np.linspace(log_ret.min(), log_ret.max(), 300)
    ax.plot(x_grid, ss.norm.pdf(x_grid, log_ret.mean(), log_ret.std()),
            "r-", linewidth=2, label="Normal (matched moments)")
    ax.set_title("Heston Terminal Log-Return vs Normal")
    ax.set_xlabel("log(S_T / S_0)")
    ax.set_ylabel("Density")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_heston_terminal.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_heston_terminal.png")
    plt.close()

    # ==================================================================
    # 2. Variance Gamma (VG) process
    # ==================================================================
    print()
    print("=" * 65)
    print("2. Variance Gamma (VG) Process")
    print("=" * 65)

    vg = VG_process(r=0.05, sigma=0.2, theta=-0.14, kappa=0.2)
    print(f"  Parameters:")
    print(f"    r     = {vg.r}")
    print(f"    sigma = {vg.sigma}")
    print(f"    theta = {vg.theta}")
    print(f"    kappa = {vg.kappa}")
    print(f"  Analytic moments (1-year increment):")
    print(f"    Mean             = {vg.mean:.4f}")
    print(f"    Variance         = {vg.var:.4f}")
    print(f"    Skewness         = {vg.skew:.4f}")
    print(f"    Excess kurtosis  = {vg.kurt:.4f}")

    # --- VG paths via gamma subordination ---
    T_vg, N_vg, n_paths_vg = 1, 1000, 6
    X_vg = vg.path(T=T_vg, N=N_vg, paths=n_paths_vg)
    t_vg = np.linspace(0, T_vg, N_vg)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for p in range(n_paths_vg):
        axes[0].plot(t_vg, X_vg[p, :], linewidth=0.8)
    axes[0].set_title("VG Process Paths (Gamma Subordination)")
    axes[0].set_xlabel("Time (years)")
    axes[0].set_ylabel("X(t)")
    axes[0].grid(True, alpha=0.3)

    # Exponential VG stock-price paths
    S_vg_paths = 100 * np.exp(X_vg)
    for p in range(n_paths_vg):
        axes[1].plot(t_vg, S_vg_paths[p, :], linewidth=0.8)
    axes[1].set_title("Exponential VG Stock-Price Paths")
    axes[1].set_xlabel("Time (years)")
    axes[1].set_ylabel("S(t)")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_vg_paths.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_vg_paths.png")
    plt.close()

    # --- VG terminal distribution vs Normal ---
    print()
    print("  Comparing VG terminal distribution to Normal...")
    S_T_vg = vg.exp_RV(100, 1, 80_000)
    log_ret_vg = np.log(S_T_vg.ravel() / 100)

    # Matched-variance normal
    mu_n = log_ret_vg.mean()
    sig_n = log_ret_vg.std()

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Histogram
    axes[0].hist(log_ret_vg, bins=200, density=True, alpha=0.6,
                 color="steelblue", label="VG log-return")
    x_grid = np.linspace(log_ret_vg.min(), log_ret_vg.max(), 400)
    axes[0].plot(x_grid, ss.norm.pdf(x_grid, mu_n, sig_n),
                 "r-", linewidth=2, label="Normal (matched moments)")
    axes[0].set_title("VG Terminal Log-Return vs Normal")
    axes[0].set_xlabel("log(S_T / S_0)")
    axes[0].set_ylabel("Density")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Log-scale to emphasise tails
    axes[1].hist(log_ret_vg, bins=200, density=True, alpha=0.6,
                 color="steelblue", label="VG log-return")
    axes[1].plot(x_grid, ss.norm.pdf(x_grid, mu_n, sig_n),
                 "r-", linewidth=2, label="Normal (matched moments)")
    axes[1].set_yscale("log")
    axes[1].set_title("Same Comparison -- Log Scale (heavier tails visible)")
    axes[1].set_xlabel("log(S_T / S_0)")
    axes[1].set_ylabel("log Density")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_vg_terminal.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_vg_terminal.png")
    plt.close()

    print()
    print(f"  Empirical vs Normal moments of VG terminal log-return:")
    print(f"    {'Moment':<18} {'VG (empirical)':>16} {'Normal':>16}")
    print(f"    {'-'*18} {'-'*16} {'-'*16}")
    print(f"    {'Mean':<18} {log_ret_vg.mean():>16.4f} {mu_n:>16.4f}")
    print(f"    {'Std Dev':<18} {log_ret_vg.std():>16.4f} {sig_n:>16.4f}")
    print(f"    {'Skewness':<18} {ss.skew(log_ret_vg):>16.4f} {'0.0000':>16}")
    print(f"    {'Excess Kurtosis':<18} {ss.kurtosis(log_ret_vg):>16.4f} {'0.0000':>16}")

    # --- Method-of-Moments fit on simulated VG data ---
    print()
    print("  Fitting VG parameters via Method of Moments on simulated data...")
    X_sim = vg.path(T=1, N=2, paths=20_000)  # 1-step paths = terminal increments
    increments = X_sim[:, 1]  # 1-year increments

    vg_fit = VG_process(r=0.05, sigma=0.1, theta=0.0, kappa=0.1)  # start far
    vg_fit.fit_from_data(increments, dt=1, method="MM")
    print(f"    Fitted : c={vg_fit.c:.4f}, theta={vg_fit.theta:.4f}, "
          f"sigma={vg_fit.sigma:.4f}, kappa={vg_fit.kappa:.4f}")
    print(f"    True   : c={vg.c:.4f}, theta={vg.theta:.4f}, "
          f"sigma={vg.sigma:.4f}, kappa={vg.kappa:.4f}")

    print()
    print("Done.")
