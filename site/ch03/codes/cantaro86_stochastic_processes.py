#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_stochastic_processes.py

Stochastic process classes for quantitative finance: GBM, Merton jump-diffusion,
GARCH(1,1), and Ornstein-Uhlenbeck.

Based on Processes.py from cantaro86's "Financial-Models-Numerical-Methods"
(https://github.com/cantaro86/Financial-Models-Numerical-Methods).
Adapted as a self-contained educational module -- no local imports required.

Classes
-------
Diffusion_process : Geometric Brownian Motion (GBM) terminal random variable.
Merton_process    : Jump-diffusion with Poisson jumps and normal jump sizes.
GARCH             : GARCH(1,1) path generation, MLE fitting, variance generation.
OU_process        : Ornstein-Uhlenbeck exact simulation (mean-reverting).
"""

import numpy as np
import scipy.stats as ss
import pandas as pd
from scipy.optimize import minimize


# ---------------------------------------------------------------------------
# Diffusion (GBM)
# ---------------------------------------------------------------------------

class Diffusion_process:
    """
    Geometric Brownian Motion (GBM) diffusion process.

    Under the risk-neutral measure the log-price satisfies:

        dX = (r - sigma^2/2) dt + sigma dW

    so that S_T = S_0 * exp(X_T).

    Parameters
    ----------
    r : float
        Risk-free rate.
    sig : float
        Constant volatility (must be > 0).
    mu : float
        Physical drift (used only outside risk-neutral pricing).
    """

    def __init__(self, r=0.1, sig=0.2, mu=0.1):
        self.r = r
        self.mu = mu
        if sig <= 0:
            raise ValueError("sig must be positive")
        self.sig = sig

    def exp_RV(self, S0, T, N):
        """
        Generate N terminal GBM random variables S_T.

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
        W = ss.norm.rvs(
            (self.r - 0.5 * self.sig ** 2) * T,
            np.sqrt(T) * self.sig,
            N,
        )
        S_T = S0 * np.exp(W)
        return S_T.reshape((N, 1))

    def path(self, S0, T=1, N=500, paths=1):
        """
        Generate full GBM paths via exact log-normal increments.

        Parameters
        ----------
        S0 : float
            Initial stock price.
        T : float
            Total time horizon (years).
        N : int
            Number of time points (N-1 time steps).
        paths : int
            Number of independent paths.

        Returns
        -------
        ndarray, shape (N, paths)
            Simulated price paths (columns = paths).
        """
        dt = T / (N - 1)
        Z = ss.norm.rvs(size=(N - 1, paths))
        log_increments = (self.r - 0.5 * self.sig ** 2) * dt + self.sig * np.sqrt(dt) * Z
        log_S = np.zeros((N, paths))
        log_S[0, :] = np.log(S0)
        log_S[1:, :] = log_increments
        log_S = np.cumsum(log_S, axis=0)
        return np.exp(log_S)


# ---------------------------------------------------------------------------
# Merton jump-diffusion
# ---------------------------------------------------------------------------

class Merton_process:
    """
    Merton jump-diffusion process.

    The log-price follows a diffusion augmented by compound-Poisson jumps
    whose sizes are normally distributed:

        dX = (r - sigma^2/2 - lambda*m) dt + sigma dW + J dN

    where N is Poisson(lambda) and J ~ N(muJ, sigJ^2).

    Parameters
    ----------
    r : float
        Risk-free rate.
    sig : float
        Diffusion volatility (>= 0).
    lam : float
        Jump intensity (expected number of jumps per year).
    muJ : float
        Mean of the log-jump size.
    sigJ : float
        Standard deviation of the log-jump size (>= 0).
    """

    def __init__(self, r=0.1, sig=0.2, lam=0.8, muJ=0, sigJ=0.5):
        self.r = r
        self.lam = lam
        self.muJ = muJ
        if sig < 0 or sigJ < 0:
            raise ValueError("sig and sigJ must be non-negative")
        self.sig = sig
        self.sigJ = sigJ

        # Analytic moments of the 1-year log-return increment
        self.var = self.sig ** 2 + self.lam * self.sigJ ** 2 + self.lam * self.muJ ** 2
        self.skew = (
            self.lam * (3 * self.sigJ ** 2 * self.muJ + self.muJ ** 3)
            / self.var ** 1.5
        )
        self.kurt = (
            self.lam * (3 * self.sigJ ** 3 + 6 * self.sigJ ** 2 * self.muJ ** 2 + self.muJ ** 4)
            / self.var ** 2
        )

    def exp_RV(self, S0, T, N):
        """
        Generate N terminal Merton jump-diffusion prices S_T.

        The martingale correction m = lambda * (exp(muJ + sigJ^2/2) - 1)
        ensures that E[S_T] = S_0 * exp(r*T).

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
        m = self.lam * (np.exp(self.muJ + self.sigJ ** 2 / 2) - 1)
        W = ss.norm.rvs(0, 1, N)
        P = ss.poisson.rvs(self.lam * T, size=N)
        Jumps = np.array([
            ss.norm.rvs(self.muJ, self.sigJ, n_jumps).sum() if n_jumps > 0 else 0.0
            for n_jumps in P
        ])
        S_T = S0 * np.exp(
            (self.r - 0.5 * self.sig ** 2 - m) * T
            + np.sqrt(T) * self.sig * W
            + Jumps
        )
        return S_T.reshape((N, 1))

    def path(self, S0, T=1, N=500, paths=1):
        """
        Generate full Merton jump-diffusion paths (Euler scheme).

        Parameters
        ----------
        S0 : float
            Initial stock price.
        T : float
            Total time horizon (years).
        N : int
            Number of time points.
        paths : int
            Number of independent paths.

        Returns
        -------
        ndarray, shape (N, paths)
            Simulated price paths.
        """
        dt = T / (N - 1)
        m = self.lam * (np.exp(self.muJ + self.sigJ ** 2 / 2) - 1)
        log_S = np.zeros((N, paths))
        log_S[0, :] = np.log(S0)

        for t in range(N - 1):
            Z = ss.norm.rvs(size=paths)
            P = ss.poisson.rvs(self.lam * dt, size=paths)
            Jumps = np.array([
                ss.norm.rvs(self.muJ, self.sigJ, n_j).sum() if n_j > 0 else 0.0
                for n_j in P
            ])
            log_S[t + 1, :] = (
                log_S[t, :]
                + (self.r - 0.5 * self.sig ** 2 - m) * dt
                + self.sig * np.sqrt(dt) * Z
                + Jumps
            )
        return np.exp(log_S)


# ---------------------------------------------------------------------------
# GARCH(1,1)
# ---------------------------------------------------------------------------

class GARCH:
    """
    GARCH(1,1) variance model.

    The conditional variance evolves as:

        V(t) = omega + alpha * R(t-1)^2 + beta * V(t-1)

    where
        gamma = 1 - alpha - beta,
        omega = gamma * VL,
    and VL is the unconditional (long-run) variance.

    Parameters
    ----------
    VL : float
        Unconditional variance (>= 0).
    alpha : float
        ARCH coefficient (> 0).
    beta : float
        GARCH coefficient (> 0).
    """

    def __init__(self, VL=0.04, alpha=0.08, beta=0.9):
        if VL < 0 or alpha <= 0 or beta <= 0:
            raise ValueError("VL >= 0, alpha > 0 and beta > 0 required")
        self.VL = VL
        self.alpha = alpha
        self.beta = beta
        self.gamma = 1 - self.alpha - self.beta
        self.omega = self.gamma * self.VL

    def path(self, N=1000):
        """
        Generate a GARCH(1,1) return series and corresponding variance series.

        Parameters
        ----------
        N : int
            Number of observations.

        Returns
        -------
        R : ndarray
            Return series.
        var : ndarray
            Conditional variance series.
        """
        eps = ss.norm.rvs(loc=0, scale=1, size=N)
        R = np.zeros(N)
        var = np.zeros(N)
        for i in range(N):
            var[i] = self.omega + self.alpha * R[i - 1] ** 2 + self.beta * var[i - 1]
            R[i] = np.sqrt(var[i]) * eps[i]
        return R, var

    def generate_var(self, R, R0, var0):
        """
        Generate the variance process from an observed return series.

        Parameters
        ----------
        R : ndarray
            Observed return array.
        R0 : float
            Return at time 0 (before R starts).
        var0 : float
            Variance at time 0 (before R starts).

        Returns
        -------
        ndarray
            Conditional variance series.
        """
        N = len(R)
        var = np.zeros(N)
        var[0] = self.omega + self.alpha * (R0 ** 2) + self.beta * var0
        for i in range(1, N):
            var[i] = self.omega + self.alpha * R[i - 1] ** 2 + self.beta * var[i - 1]
        return var

    def log_likelihood(self, R, last_var=True):
        """
        Compute the Gaussian log-likelihood of return series R.

        Parameters
        ----------
        R : ndarray
            Return series.
        last_var : bool
            If True, also return the last conditional variance.

        Returns
        -------
        log_lik : float
            Log-likelihood value.
        var : float, optional
            Last conditional variance (if last_var is True).
        """
        var = R[0] ** 2
        N = len(R)
        log_lik = 0.0
        log_2pi = np.log(2 * np.pi)
        for i in range(1, N):
            var = self.omega + self.alpha * R[i - 1] ** 2 + self.beta * var
            log_lik += 0.5 * (-log_2pi - np.log(var) - R[i] ** 2 / var)
        if last_var:
            return log_lik, var
        return log_lik

    def fit_from_data(self, data, disp=True):
        """
        MLE estimation of GARCH(1,1) parameters from data.

        Automatically rescales data to avoid numerical issues with the
        optimizer and log-likelihood overflows.

        Parameters
        ----------
        data : ndarray
            Observed return series.
        disp : bool
            If True, print estimation summary with standard errors and
            confidence intervals.
        """
        # Auto-rescale to help the optimizer
        n = np.floor(np.log10(np.abs(data.mean()))) if data.mean() != 0 else 0
        R = data / 10 ** n

        # Initial guesses
        a0, b0 = 0.05, 0.9
        g0 = 1 - a0 - b0
        w0 = g0 * np.var(R)

        bounds = ((0, None), (0, 1), (0, 1))

        def sum_small_1(x):
            return 1 - x[1] - x[2]

        cons = {"fun": sum_small_1, "type": "ineq"}

        def neg_log_lik(x):
            var = R[0] ** 2
            ll = 0.0
            for i in range(1, len(R)):
                var = x[0] + x[1] * R[i - 1] ** 2 + x[2] * var
                ll += -np.log(var) - R[i] ** 2 / var
            return -ll

        result = minimize(
            neg_log_lik,
            x0=[w0, a0, b0],
            method="SLSQP",
            bounds=bounds,
            constraints=cons,
            tol=1e-8,
            options={"maxiter": 150},
        )
        print(f"  Optimizer: {result.message}")

        self.omega = result.x[0] * 10 ** (2 * n)
        self.alpha, self.beta = result.x[1], result.x[2]
        self.gamma = 1 - self.alpha - self.beta
        self.VL = self.omega / self.gamma if self.gamma > 0 else np.inf

        if disp:
            from statsmodels.tools.numdiff import approx_hess

            hess = approx_hess(result.x, neg_log_lik)
            try:
                se = np.sqrt(np.diag(np.linalg.inv(hess)))
            except np.linalg.LinAlgError:
                se = np.full(3, np.nan)

            cv = ss.norm.ppf(1.0 - 0.05 / 2.0)
            p_val = ss.norm.sf(np.abs(result.x / se))

            df = pd.DataFrame(index=["omega", "alpha", "beta"])
            df["Params"] = result.x
            df["SE"] = se
            df["P-val"] = p_val
            df["95% CI lower"] = result.x - cv * se
            df["95% CI upper"] = result.x + cv * se
            df.loc["omega", ["Params", "SE", "95% CI lower", "95% CI upper"]] *= 10 ** (2 * n)
            print(df)


# ---------------------------------------------------------------------------
# Ornstein-Uhlenbeck
# ---------------------------------------------------------------------------

class OU_process:
    """
    Ornstein-Uhlenbeck (OU) mean-reverting process.

    The continuous-time dynamics are:

        dX = kappa * (theta - X) dt + sigma dW

    Simulation uses the *exact* discretisation:

        X(t+dt) = theta + exp(-kappa*dt) * (X(t) - theta) + noise

    Parameters
    ----------
    sigma : float
        Diffusion coefficient (>= 0).
    theta : float
        Long-run mean level.
    kappa : float
        Mean-reversion speed (>= 0).
    """

    def __init__(self, sigma=0.2, theta=-0.1, kappa=0.1):
        self.theta = theta
        if sigma < 0 or kappa < 0:
            raise ValueError("sigma and kappa must be non-negative")
        self.sigma = sigma
        self.kappa = kappa

    def path(self, X0=0, T=1, N=10000, paths=1):
        """
        Generate OU process paths via exact simulation.

        Parameters
        ----------
        X0 : float
            Starting value.
        T : float
            Time horizon (years).
        N : int
            Number of time points (N-1 time steps).
        paths : int
            Number of independent paths.

        Returns
        -------
        ndarray, shape (N, paths)
            Simulated OU paths.
        """
        dt = T / (N - 1)
        X = np.zeros((N, paths))
        X[0, :] = X0
        W = ss.norm.rvs(loc=0, scale=1, size=(N - 1, paths))

        # Exact conditional standard deviation for one time step
        std_dt = np.sqrt(
            self.sigma ** 2 / (2 * self.kappa) * (1 - np.exp(-2 * self.kappa * dt))
        )
        exp_factor = np.exp(-self.kappa * dt)

        for t in range(N - 1):
            X[t + 1, :] = (
                self.theta
                + exp_factor * (X[t, :] - self.theta)
                + std_dt * W[t, :]
            )
        return X


# ---------------------------------------------------------------------------
# Main demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    np.random.seed(42)

    # ------------------------------------------------------------------
    # 1. GBM paths
    # ------------------------------------------------------------------
    print("=" * 60)
    print("1. Geometric Brownian Motion (GBM)")
    print("=" * 60)

    gbm = Diffusion_process(r=0.05, sig=0.25, mu=0.05)
    S0, T, N_steps, n_paths = 100, 1, 252, 5
    paths_gbm = gbm.path(S0, T=T, N=N_steps, paths=n_paths)
    t_grid = np.linspace(0, T, N_steps)

    # Terminal distribution
    S_T = gbm.exp_RV(S0, T, 50_000)
    print(f"  Parameters : r={gbm.r}, sigma={gbm.sig}")
    print(f"  E[S_T]     : {S_T.mean():.2f}  (theory: {S0 * np.exp(gbm.r * T):.2f})")
    print(f"  Std[S_T]   : {S_T.std():.2f}")

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    for p in range(n_paths):
        axes[0].plot(t_grid, paths_gbm[:, p], linewidth=0.8)
    axes[0].set_title("GBM Sample Paths")
    axes[0].set_xlabel("Time (years)")
    axes[0].set_ylabel("Stock Price S(t)")
    axes[0].grid(True, alpha=0.3)

    axes[1].hist(S_T.ravel(), bins=100, density=True, color="steelblue", alpha=0.7)
    axes[1].set_title("GBM Terminal Distribution S(T)")
    axes[1].set_xlabel("S(T)")
    axes[1].set_ylabel("Density")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_stochastic_processes_gbm.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_stochastic_processes_gbm.png")
    plt.close()

    # ------------------------------------------------------------------
    # 2. Merton jump-diffusion
    # ------------------------------------------------------------------
    print()
    print("=" * 60)
    print("2. Merton Jump-Diffusion Process")
    print("=" * 60)

    merton = Merton_process(r=0.05, sig=0.15, lam=1.0, muJ=-0.05, sigJ=0.1)
    print(f"  Parameters : r={merton.r}, sig={merton.sig}, "
          f"lam={merton.lam}, muJ={merton.muJ}, sigJ={merton.sigJ}")
    print(f"  Analytic moments of 1-yr log-return:")
    print(f"    Variance : {merton.var:.4f}")
    print(f"    Skewness : {merton.skew:.4f}")
    print(f"    Excess kurtosis : {merton.kurt:.4f}")

    paths_merton = merton.path(S0=100, T=1, N=252, paths=5)
    S_T_merton = merton.exp_RV(100, 1, 50_000)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    for p in range(5):
        axes[0].plot(t_grid, paths_merton[:, p], linewidth=0.8)
    axes[0].set_title("Merton Jump-Diffusion Paths")
    axes[0].set_xlabel("Time (years)")
    axes[0].set_ylabel("Stock Price S(t)")
    axes[0].grid(True, alpha=0.3)

    # Compare Merton terminal vs GBM terminal
    axes[1].hist(np.log(S_T_merton.ravel() / 100), bins=120, density=True,
                 alpha=0.6, color="tomato", label="Merton log-return")
    gbm_compare = Diffusion_process(r=0.05, sig=np.sqrt(merton.var))
    S_T_gbm = gbm_compare.exp_RV(100, 1, 50_000)
    axes[1].hist(np.log(S_T_gbm.ravel() / 100), bins=120, density=True,
                 alpha=0.5, color="steelblue", label="GBM (matched var)")
    axes[1].set_title("Log-Return Distribution: Merton vs GBM")
    axes[1].set_xlabel("log(S_T / S_0)")
    axes[1].set_ylabel("Density")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_stochastic_processes_merton.png", dpi=150)
    print(f"  E[S_T] : {S_T_merton.mean():.2f}  (theory: {100 * np.exp(0.05):.2f})")
    print("  Figure saved: /tmp/cantaro86_stochastic_processes_merton.png")
    plt.close()

    # ------------------------------------------------------------------
    # 3. GARCH(1,1)
    # ------------------------------------------------------------------
    print()
    print("=" * 60)
    print("3. GARCH(1,1) Process")
    print("=" * 60)

    garch = GARCH(VL=0.0004, alpha=0.08, beta=0.90)
    print(f"  Parameters : VL={garch.VL}, alpha={garch.alpha}, "
          f"beta={garch.beta}, omega={garch.omega:.6f}")
    print(f"  Persistence (alpha + beta) = {garch.alpha + garch.beta:.2f}")

    R_garch, var_garch = garch.path(N=2000)
    vol_garch = np.sqrt(var_garch) * np.sqrt(252)  # annualised vol

    fig, axes = plt.subplots(2, 1, figsize=(14, 7), sharex=True)
    axes[0].plot(R_garch, linewidth=0.5, color="steelblue")
    axes[0].set_title("GARCH(1,1) Returns")
    axes[0].set_ylabel("Return R(t)")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(vol_garch, linewidth=0.8, color="tomato", label="Annualised vol")
    axes[1].axhline(np.sqrt(garch.VL) * np.sqrt(252), color="k",
                     linestyle="--", linewidth=1, label=f"Long-run vol = {np.sqrt(garch.VL)*np.sqrt(252):.2%}")
    axes[1].set_title("GARCH(1,1) Conditional Volatility")
    axes[1].set_xlabel("Time step")
    axes[1].set_ylabel("Annualised Volatility")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_stochastic_processes_garch.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_stochastic_processes_garch.png")
    plt.close()

    # Demonstrate MLE fit on the simulated data
    print()
    print("  Fitting GARCH(1,1) via MLE on simulated returns...")
    garch_fit = GARCH(VL=0.01, alpha=0.05, beta=0.85)  # start from different params
    garch_fit.fit_from_data(R_garch, disp=False)
    print(f"  Fitted: omega={garch_fit.omega:.6f}, alpha={garch_fit.alpha:.4f}, "
          f"beta={garch_fit.beta:.4f}")
    print(f"  True  : omega={garch.omega:.6f}, alpha={garch.alpha:.4f}, "
          f"beta={garch.beta:.4f}")

    # ------------------------------------------------------------------
    # 4. Ornstein-Uhlenbeck (OU) process
    # ------------------------------------------------------------------
    print()
    print("=" * 60)
    print("4. Ornstein-Uhlenbeck Process (Mean-Reverting)")
    print("=" * 60)

    ou = OU_process(sigma=0.3, theta=1.0, kappa=3.0)
    print(f"  Parameters : theta={ou.theta}, kappa={ou.kappa}, sigma={ou.sigma}")

    T_ou, N_ou = 5, 2000
    X_ou = ou.path(X0=0.0, T=T_ou, N=N_ou, paths=8)
    t_ou = np.linspace(0, T_ou, N_ou)

    # Analytic stationary distribution
    stat_mean = ou.theta
    stat_std = ou.sigma / np.sqrt(2 * ou.kappa)
    print(f"  Stationary mean     : {stat_mean:.3f}")
    print(f"  Stationary std dev  : {stat_std:.3f}")
    print(f"  Half-life           : {np.log(2) / ou.kappa:.3f} years")

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    for p in range(X_ou.shape[1]):
        axes[0].plot(t_ou, X_ou[:, p], linewidth=0.7, alpha=0.8)
    axes[0].axhline(stat_mean, color="k", linewidth=1.5, linestyle="--",
                     label=f"Long-run mean theta = {stat_mean}")
    axes[0].fill_between(t_ou, stat_mean - 2 * stat_std, stat_mean + 2 * stat_std,
                          alpha=0.1, color="gray", label="+/- 2 sigma band")
    axes[0].set_title("OU Process Paths (Mean Reversion)")
    axes[0].set_xlabel("Time (years)")
    axes[0].set_ylabel("X(t)")
    axes[0].legend(fontsize=8)
    axes[0].grid(True, alpha=0.3)

    # Terminal cross-section histogram vs stationary density
    X_terminal = X_ou[-1, :]
    # Generate many more for a clean histogram
    X_many = ou.path(X0=0.0, T=T_ou, N=N_ou, paths=10_000)
    axes[1].hist(X_many[-1, :], bins=80, density=True, alpha=0.6, color="steelblue",
                 label="Simulated terminal")
    x_grid = np.linspace(stat_mean - 4 * stat_std, stat_mean + 4 * stat_std, 200)
    axes[1].plot(x_grid, ss.norm.pdf(x_grid, stat_mean, stat_std),
                 "r-", linewidth=2, label="Stationary N(theta, sigma^2/(2*kappa))")
    axes[1].set_title("OU Terminal Distribution vs Stationary")
    axes[1].set_xlabel("X(T)")
    axes[1].set_ylabel("Density")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/cantaro86_stochastic_processes_ou.png", dpi=150)
    print("  Figure saved: /tmp/cantaro86_stochastic_processes_ou.png")
    plt.close()

    # ------------------------------------------------------------------
    # Summary of process moments
    # ------------------------------------------------------------------
    print()
    print("=" * 60)
    print("Summary: Process Moments (1-year log-returns)")
    print("=" * 60)

    print(f"  {'Process':<20} {'Variance':>10} {'Skewness':>10} {'Ex. Kurt':>10}")
    print(f"  {'-'*20} {'-'*10} {'-'*10} {'-'*10}")

    # GBM: log-return ~ N, so skew=0, excess kurt=0
    gbm_var = gbm.sig ** 2
    print(f"  {'GBM':<20} {gbm_var:>10.4f} {'0.0000':>10} {'0.0000':>10}")

    # Merton
    print(f"  {'Merton':<20} {merton.var:>10.4f} {merton.skew:>10.4f} {merton.kurt:>10.4f}")

    # GARCH (unconditional)
    garch_uncond_var = garch.VL
    print(f"  {'GARCH (uncond.)':<20} {garch_uncond_var:>10.6f} {'--':>10} {'--':>10}")

    # OU (stationary)
    ou_stat_var = ou.sigma ** 2 / (2 * ou.kappa)
    print(f"  {'OU (stationary)':<20} {ou_stat_var:>10.4f} {'0.0000':>10} {'0.0000':>10}")
    print()
    print("Done.")
