#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_volatility_tracking.py
Volatility Tracking: Kalman Filter vs GARCH vs Rolling Variance

Credits
-------
Based on notebook "5.3 Volatility tracking" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 17 -- Calibration).

Topics covered
--------------
1. Heston stochastic volatility path simulation (Euler scheme).
2. GARCH(1,1) model: parameter estimation and variance forecasting.
3. Rolling variance estimation.
4. Kalman filter for log-variance tracking using Taylor's (1986)
   linearisation: log(R^2) ≈ h + log(chi^2_1), where h is the
   latent log-variance.
5. Rauch-Tung-Striebel (RTS) smoother for smoothed volatility.
6. MSE comparison of all methods.

Key insight: The Kalman filter for volatility tracking uses a DIFFERENT
model from the Kalman regression (see cantaro86_kalman_filter.py).
Here the hidden state is log-variance, and observations are log-squared-returns.

References:
    [1] Taylor, S.J. (1986) "Modelling Financial Time Series", Wiley.
    [2] Harvey, Ruiz, Shephard (1994) "Multivariate SV models",
        Review of Economic Studies.
    [3] Bollerslev (1986) "Generalized autoregressive conditional
        heteroskedasticity", J. Econometrics.
"""

import numpy as np
import scipy.stats as ss
from scipy.integrate import quad
from scipy.optimize import minimize
import matplotlib.pyplot as plt


# ============================================================================
# 1. HESTON PROCESS PATH SIMULATION
# ============================================================================

def heston_path(S0, v0, mu, kappa, theta, sigma, rho, N, T):
    """
    Simulate one path of the Heston stochastic volatility model
    using the Euler scheme with full truncation.

        dS_t = mu * S_t * dt + sqrt(v_t) * S_t * dW_1
        dv_t = kappa * (theta - v_t) * dt + sigma * sqrt(v_t) * dW_2
        corr(dW_1, dW_2) = rho

    Parameters
    ----------
    S0 : float     Initial stock price.
    v0 : float     Initial variance.
    mu : float     Drift.
    kappa : float  Mean reversion speed.
    theta : float  Long-run variance.
    sigma : float  Vol-of-vol.
    rho : float    Correlation.
    N : int        Number of time points.
    T : float      Time horizon (years).

    Returns
    -------
    S : ndarray    Stock price path (length N).
    V : ndarray    Variance path (length N).
    dt : float     Time step.
    """
    dt = T / (N - 1)
    S = np.zeros(N)
    V = np.zeros(N)
    S[0] = S0
    V[0] = v0

    for i in range(N - 1):
        Z1 = np.random.randn()
        Z2 = rho * Z1 + np.sqrt(1 - rho**2) * np.random.randn()
        v_pos = max(V[i], 0)
        sqrt_v = np.sqrt(v_pos)

        S[i + 1] = S[i] * np.exp(
            (mu - 0.5 * v_pos) * dt + sqrt_v * np.sqrt(dt) * Z1
        )
        V[i + 1] = abs(
            V[i] + kappa * (theta - v_pos) * dt
            + sigma * sqrt_v * np.sqrt(dt) * Z2
        )

    return S, V, dt


# ============================================================================
# 2. GARCH(1,1) MODEL
# ============================================================================

class GARCH:
    """
    GARCH(1,1) model for variance forecasting.

    The conditional variance follows:
        sigma^2_t = omega + alpha * R^2_{t-1} + beta * sigma^2_{t-1}

    Reparametrised with:
        gamma = 1 - alpha - beta
        omega = gamma * V_L       (V_L = long-run variance)

    So the model becomes:
        sigma^2_t = gamma * V_L + alpha * R^2_{t-1} + beta * sigma^2_{t-1}

    Parameters
    ----------
    VL : float     Long-run variance.
    alpha : float  Weight on lagged squared return.
    beta : float   Weight on lagged variance.
    """

    def __init__(self, VL=None, alpha=None, beta=None):
        self.VL = VL
        self.alpha = alpha
        self.beta = beta
        self.gamma = None
        if alpha is not None and beta is not None:
            self.gamma = 1 - alpha - beta

    def generate_var(self, R, R0=None, var0=None):
        """
        Generate conditional variance series from return data.

        Parameters
        ----------
        R : ndarray    Return series.
        R0 : float     Previous return (for initialisation).
        var0 : float   Initial variance.

        Returns
        -------
        var_series : ndarray  Conditional variance at each step.
        """
        N = len(R)
        var_series = np.zeros(N)

        if var0 is None:
            var0 = self.VL
        if R0 is None:
            R0 = 0.0

        omega = self.gamma * self.VL
        var_series[0] = omega + self.alpha * R0**2 + self.beta * var0

        for t in range(1, N):
            var_series[t] = omega + self.alpha * R[t - 1]**2 + self.beta * var_series[t - 1]

        return var_series

    def log_likelihood(self, R, last_var=False):
        """
        Compute the log-likelihood of the return series under GARCH(1,1).

        Assumes R_t | F_{t-1} ~ N(0, sigma^2_t).

        Parameters
        ----------
        R : ndarray    Return series.
        last_var : bool  If True, also return the last variance.

        Returns
        -------
        ll : float     Log-likelihood value.
        last_v : float (optional)  Last conditional variance.
        """
        N = len(R)
        omega = self.gamma * self.VL

        var_t = R[0]**2  # initialise with squared first return
        ll = -0.5 * (np.log(2 * np.pi) + np.log(var_t) + R[0]**2 / var_t)

        for t in range(1, N):
            var_t = omega + self.alpha * R[t - 1]**2 + self.beta * var_t
            if var_t <= 0:
                var_t = 1e-12
            ll += -0.5 * (np.log(2 * np.pi) + np.log(var_t) + R[t]**2 / var_t)

        if last_var:
            return ll, var_t
        return ll

    def fit_from_data(self, R, disp=False):
        """
        Estimate GARCH(1,1) parameters by MLE.

        Optimises over (VL, alpha, beta) subject to alpha + beta < 1
        and all parameters positive.

        Parameters
        ----------
        R : ndarray   Return series.
        disp : bool   Print parameter estimates.
        """
        def neg_ll(x):
            self.VL = x[0]
            self.alpha = x[1]
            self.beta = x[2]
            self.gamma = 1 - x[1] - x[2]
            if self.gamma <= 0:
                return 1e10
            ll = self.log_likelihood(R)
            return -ll

        sample_var = np.var(R)
        x0 = [sample_var, 0.1, 0.85]
        bounds = [(1e-15, None), (1e-15, 0.999), (1e-15, 0.999)]

        result = minimize(neg_ll, x0=x0, method="L-BFGS-B",
                          bounds=bounds, tol=1e-8)

        self.VL = result.x[0]
        self.alpha = result.x[1]
        self.beta = result.x[2]
        self.gamma = 1 - self.alpha - self.beta

        if disp:
            print(f"  GARCH(1,1) MLE estimates:")
            print(f"    V_L = {self.VL:.8f}")
            print(f"    alpha = {self.alpha:.4f}")
            print(f"    beta = {self.beta:.4f}")
            print(f"    gamma = {self.gamma:.4f}")
            print(f"    alpha + beta = {self.alpha + self.beta:.4f}")


# ============================================================================
# 3. ROLLING VARIANCE
# ============================================================================

def rolling_variance(returns, window, dt=1.0):
    """
    Compute rolling MLE variance estimate.

    Parameters
    ----------
    returns : ndarray  Return series.
    window : int       Rolling window size.
    dt : float         Time step (for annualisation).

    Returns
    -------
    roll_var : ndarray  Rolling variance (NaN for initial window).
    """
    N = len(returns)
    roll_var = np.full(N, np.nan)
    for i in range(window - 1, N):
        chunk = returns[i - window + 1: i + 1]
        roll_var[i] = np.var(chunk, ddof=0) / dt
    return roll_var


# ============================================================================
# 4. KALMAN FILTER FOR LOG-VARIANCE TRACKING
# ============================================================================
#
# Taylor's (1986) model for volatility tracking:
#
# Observation model:
#   R_t = sqrt(v_t) * e_t,   e_t ~ N(0, 1)
#
# Taking logs of squared returns:
#   log(R_t^2) = log(v_t) + log(e_t^2)
#              = h_t + log(chi^2_1)
#
# where h_t = log(v_t) is the latent log-variance.
#
# The log-chi-squared(1) random variable has:
#   E[log(chi^2_1)] ≈ -1.27
#   Var[log(chi^2_1)] ≈ pi^2/2
#
# After centering: Y_t = log(R_t^2) + 1.27 ≈ h_t + N(0, pi^2/2)
#
# State equation (AR(1) for log-variance):
#   h_t = phi * h_{t-1} + eta_t,   eta_t ~ N(0, var_eta)
#
# This is a linear Gaussian state-space model solvable by Kalman filter.

def log_chi2_density(x):
    """
    Probability density of log(chi^2_1).

    If Z ~ chi^2(1), then X = log(Z) has density:
        f(x) = (1/sqrt(2*pi)) * exp(x/2 - exp(x)/2)

    Returns
    -------
    float  Density at x.
    """
    return 1.0 / np.sqrt(2 * np.pi) * np.exp(x / 2 - np.exp(x) / 2)


def kalman_volatility(data, h0, P0, phi, var_eta, scale):
    """
    1-D Kalman filter for log-variance tracking.

    Observation model:
        Y_k = h_k + epsilon_k,   epsilon_k ~ N(0, pi^2/2)
    where Y_k = log(data_k^2) + 1.27 - log(scale^2).

    State model:
        h_k = phi * h_{k-1} + eta_k,   eta_k ~ N(0, var_eta)

    The parameter 'scale' absorbs any scaling mismatch between the
    observed returns and the model variance.

    Parameters
    ----------
    data : ndarray   Return series (demeaned).
    h0 : float       Initial log-variance estimate.
    P0 : float       Initial uncertainty (variance of h0).
    phi : float      AR(1) coefficient for log-variance.
    var_eta : float  Process noise variance.
    scale : float    Scaling parameter for returns.

    Returns
    -------
    hs : ndarray     Filtered log-variance estimates.
    Ps : ndarray     Filtered covariance estimates.
    loglik : float   Log-likelihood of observations.
    """
    Y = np.log(data**2)
    N = len(Y)
    hs = np.zeros(N)
    Ps = np.zeros(N)

    # Redefine Y with centering and scaling
    Y = Y + 1.27 - np.log(scale**2)

    h = h0
    P = P0
    log_2pi = np.log(2 * np.pi)
    var_obs = 0.5 * np.pi**2  # variance of log(chi^2_1)
    loglikelihood = 0.0

    for k in range(N):
        # Prediction step
        h_p = phi * h
        P_p = phi**2 * P + var_eta

        # Innovation
        r = Y[k] - h_p
        S = P_p + var_obs
        KG = P_p / S  # Kalman gain

        # Update step
        h = h_p + KG * r
        P = P_p * (1 - KG)

        # Log-likelihood
        loglikelihood += -0.5 * (log_2pi + np.log(S) + r**2 / S)

        hs[k] = h
        Ps[k] = P

    return hs, Ps, loglikelihood


def calibrate_kalman_volatility(train_data, h0, P0):
    """
    Calibrate (phi, var_eta, scale) by Maximum Likelihood Estimation.

    Parameters
    ----------
    train_data : ndarray  Training return series.
    h0 : float            Initial log-variance.
    P0 : float            Initial uncertainty.

    Returns
    -------
    params : tuple  (phi, var_eta, scale).
    """
    def neg_loglik(c):
        _, _, ll = kalman_volatility(train_data, h0, P0, c[0], c[1], c[2])
        return -ll

    result = minimize(
        neg_loglik, x0=[0.1, 1.0, 1.0],
        method="L-BFGS-B",
        bounds=[(-1, 1), (1e-15, None), (1e-15, None)],
        tol=1e-8,
    )

    return tuple(result.x)


def rts_smoother_1d(hs, Ps, phi, var_eta):
    """
    Rauch-Tung-Striebel smoother for 1-D state (log-variance).

    Parameters
    ----------
    hs : ndarray     Filtered log-variance estimates.
    Ps : ndarray     Filtered covariance estimates.
    phi : float      AR(1) coefficient.
    var_eta : float  Process noise variance.

    Returns
    -------
    hs_smooth : ndarray  Smoothed log-variance estimates.
    Ps_smooth : ndarray  Smoothed covariance estimates.
    """
    N = len(hs)
    hs_smooth = np.zeros(N)
    Ps_smooth = np.zeros(N)
    hs_smooth[-1] = hs[-1]
    Ps_smooth[-1] = Ps[-1]

    for k in range(N - 2, -1, -1):
        P_pred = phi**2 * Ps[k] + var_eta
        C = phi * Ps[k] / P_pred
        hs_smooth[k] = hs[k] + C * (hs_smooth[k + 1] - phi * hs[k])
        Ps_smooth[k] = Ps[k] + C**2 * (Ps_smooth[k + 1] - P_pred)

    return hs_smooth, Ps_smooth


# ============================================================================
# 5. LOG-CHI-SQUARED APPROXIMATION ANALYSIS
# ============================================================================

def log_chi2_analysis():
    """
    Compute mean and variance of log(chi^2_1) and compare with Normal.

    The key approximation: log(chi^2_1) ≈ N(-1.27, pi^2/2).
    This is a reasonable approximation despite the asymmetry of
    the log-chi-squared distribution.

    Returns
    -------
    dict with mean_chi2, var_chi2.
    """
    mean_val = quad(lambda x: x * log_chi2_density(x), -30, 10)[0]
    var_val = quad(lambda x: (x - mean_val)**2 * log_chi2_density(x), -50, 10)[0]

    print(f"  Log-Chi-Squared(1) distribution:")
    print(f"    E[log(chi^2_1)]   = {mean_val:.4f}  (≈ -1.27)")
    print(f"    Var[log(chi^2_1)] = {var_val:.4f}  (≈ pi^2/2 = {0.5 * np.pi**2:.4f})")

    return {"mean_chi2": mean_val, "var_chi2": var_val}


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all volatility tracking demonstrations."""
    np.random.seed(42)

    # ---- Heston model parameters ----
    S0, v0 = 100, 0.04
    mu = 0.1
    rho = -0.1
    kappa = 5
    theta = 0.04
    sigma_v = 0.6
    N = 2500
    T = 10

    # ---- 1. Simulate Heston path ----
    print("=" * 60)
    print("1. Heston Process Simulation")
    print("=" * 60)

    # Feller condition check
    feller = 2 * kappa * theta - sigma_v**2
    print(f"  Feller condition: 2*kappa*theta - sigma^2 = {feller:.4f}"
          f"  {'SATISFIED' if feller > 0 else 'VIOLATED'}")

    S, V, dt = heston_path(S0, v0, mu, kappa, theta, sigma_v, rho, N, T)
    T_vec = np.linspace(0, T, N)

    # Asymptotic standard deviation of CIR process
    std_asy = np.sqrt(theta * sigma_v**2 / (2 * kappa))
    print(f"  Long-run variance theta = {theta}")
    print(f"  Asymptotic std dev = {std_asy:.4f}")

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
    ax1.plot(T_vec, S)
    ax1.set_title("Heston Model: Stock Price")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("S")
    ax1.grid(True, alpha=0.3)

    ax2.plot(T_vec, V, label="Variance process")
    ax2.axhline(theta, color="k", ls="--", label=f"theta = {theta}")
    ax2.axhline(theta + std_asy, color="grey", ls=":", label=f"± 1 asy. std")
    ax2.axhline(theta - std_asy, color="grey", ls=":")
    ax2.set_title("Heston Model: Variance Process")
    ax2.set_xlabel("Time (years)")
    ax2.set_ylabel("v")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ---- 2. Log-return analysis ----
    print("\n" + "=" * 60)
    print("2. Log-Return Analysis")
    print("=" * 60)

    ret_log = np.log(S[1:] / S[:-1])
    mean_log = ret_log.mean()
    std_log = ret_log.std()
    print(f"  Normalised mean = {mean_log / dt:.4f}")
    print(f"  Normalised std  = {std_log / np.sqrt(dt):.4f}")
    print(f"  Ito-corrected mean ≈ {mean_log / dt + 0.5 * theta:.4f}"
          f"  (expected mu = {mu})")

    # Student-t fit
    t_params = ss.t.fit(ret_log)
    print(f"  Student-t fit: df = {t_params[0]:.2f}")

    # ---- 3. Log-chi-squared approximation ----
    print("\n" + "=" * 60)
    print("3. Log-Chi-Squared Approximation")
    print("=" * 60)
    chi2_result = log_chi2_analysis()

    x_plot = np.linspace(-15, 5, 200)
    mean_c = chi2_result["mean_chi2"]
    var_c = chi2_result["var_chi2"]

    plt.figure(figsize=(10, 4))
    plt.plot(x_plot, ss.norm.pdf(x_plot, loc=mean_c, scale=np.sqrt(var_c)),
             "b-", lw=2, label="Normal approximation")
    plt.plot(x_plot, log_chi2_density(x_plot),
             "r-", lw=2, label="Log-Chi-Squared(1)")
    plt.title("Normal Approximation to Log-Chi-Squared(1)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ---- 4. GARCH(1,1) ----
    print("\n" + "=" * 60)
    print("4. GARCH(1,1) Variance Tracking")
    print("=" * 60)

    train_size = 1500
    train = ret_log[:train_size]
    train = train - train.mean()  # detrend
    test = ret_log[train_size:]

    garch = GARCH()
    garch.fit_from_data(train, disp=True)

    ll_val = garch.log_likelihood(train)
    print(f"  Log-likelihood = {ll_val:.2f}")

    # Generate variance forecasts
    var_train = garch.generate_var(R=train[1:], R0=train[0], var0=train[0]**2)
    last_var = garch.generate_var(R=train[1:], R0=train[0], var0=train[0]**2)[-1]
    var_test = garch.generate_var(R=test, R0=train[-1], var0=last_var)

    # ---- 5. Rolling variance ----
    print("\n" + "=" * 60)
    print("5. Rolling Variance")
    print("=" * 60)
    window = 20
    roll_var = rolling_variance(ret_log, window, dt)
    print(f"  Rolling window = {window}")
    print(f"  Mean rolling variance (test) = "
          f"{np.nanmean(roll_var[train_size:]):.6f}")

    # ---- 6. Kalman filter for volatility ----
    print("\n" + "=" * 60)
    print("6. Kalman Filter for Log-Variance Tracking")
    print("=" * 60)

    h0 = np.log(train.var())  # initial log-variance from training data
    P0 = 100  # large initial uncertainty

    # Calibrate parameters
    print("  Calibrating (phi, var_eta, scale) via MLE...")
    phi, var_eta, scale = calibrate_kalman_volatility(train, h0, P0)
    print(f"    phi = {phi:.4f}")
    print(f"    var_eta = {var_eta:.6f}")
    print(f"    scale = {scale:.4f}")

    # Run Kalman filter on training set, then test set
    hs_train, Ps_train, ll_train = kalman_volatility(
        train, h0, P0, phi, var_eta, scale)
    hs_test, Ps_test, ll_test = kalman_volatility(
        test, hs_train[-1], Ps_train[-1], phi, var_eta, scale)

    # Transform back to variance
    V_kalm = np.exp(hs_test) / dt * scale**2
    V_up = np.exp(hs_test + np.sqrt(Ps_test)) / dt * scale**2
    V_down = np.exp(hs_test - np.sqrt(Ps_test)) / dt * scale**2

    # RTS smoother
    hs_smooth, Ps_smooth = rts_smoother_1d(hs_test, Ps_test, phi, var_eta)
    V_smooth = np.exp(hs_smooth) / dt * scale**2

    # ---- 7. Comparison ----
    print("\n" + "=" * 60)
    print("7. MSE Comparison (Out-of-Sample)")
    print("=" * 60)

    V_true_test = V[1 + train_size:]
    min_len = min(len(V_true_test), len(V_kalm), len(var_test))
    V_true_test = V_true_test[:min_len]
    V_kalm_cmp = V_kalm[:min_len]
    V_smooth_cmp = V_smooth[:min_len]
    var_test_cmp = var_test[:min_len] / dt
    roll_test = roll_var[train_size:train_size + min_len]

    mse_kalman = np.mean((V_true_test - V_kalm_cmp)**2)
    mse_smooth = np.mean((V_true_test - V_smooth_cmp)**2)
    mse_garch = np.mean((V_true_test - var_test_cmp)**2)
    valid_roll = ~np.isnan(roll_test)
    mse_rolling = np.mean((V_true_test[valid_roll] - roll_test[valid_roll])**2)

    print(f"  {'Method':<25s}  {'MSE':>12s}")
    print(f"  {'-'*25}  {'-'*12}")
    print(f"  {'Kalman Filter':<25s}  {mse_kalman:>12.6f}")
    print(f"  {'RTS Smoother':<25s}  {mse_smooth:>12.6f}")
    print(f"  {'GARCH(1,1)':<25s}  {mse_garch:>12.6f}")
    print(f"  {'Rolling Variance (w=20)':<25s}  {mse_rolling:>12.6f}")

    # Determine winner
    results = {
        "Kalman": mse_kalman,
        "Smoother": mse_smooth,
        "GARCH": mse_garch,
        "Rolling": mse_rolling,
    }
    winner = min(results, key=results.get)
    print(f"\n  Best method: {winner}")

    # ---- Plots ----
    # Plot 1: Kalman filter with confidence bands
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

    ax1.plot(V_true_test, label="True Heston variance", linewidth=2,
             color="steelblue")
    ax1.plot(V_kalm_cmp, label="Kalman filter", color="darksalmon",
             linewidth=1.5)
    ax1.fill_between(range(min_len), V_up[:min_len], V_down[:min_len],
                     alpha=0.3, color="seagreen",
                     label=r"Kalman $\pm$ 1 std dev")
    ax1.plot(V_smooth_cmp, label="RTS smoother", color="maroon",
             linewidth=1.5, ls="--")
    ax1.set_title("Out-of-Sample: Kalman Filter & RTS Smoother")
    ax1.set_xlabel("Time step")
    ax1.set_ylabel("Variance")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: All methods comparison
    ax2.plot(V_true_test, label="True Heston variance", linewidth=2,
             color="steelblue")
    ax2.plot(V_kalm_cmp, label="Kalman filter", color="limegreen",
             linewidth=1.5)
    ax2.plot(var_test_cmp, label="GARCH(1,1)", color="peru",
             linewidth=1.5, ls="--")
    ax2.plot(roll_test, label=f"Rolling variance (w={window})",
             color="orchid", linewidth=1.5, ls="--", alpha=0.8)
    ax2.set_title("Out-of-Sample: All Methods Comparison")
    ax2.set_xlabel("Time step")
    ax2.set_ylabel("Variance")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # ---- Summary ----
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("  The Kalman filter for log-variance tracking (Taylor 1986):")
    print("  - Uses the observation log(R^2) ≈ h + log(chi^2_1)")
    print("  - Models h_t = phi * h_{t-1} + eta_t as an AR(1) state")
    print("  - The log-chi^2(1) is approximated by N(-1.27, pi^2/2)")
    print("  - Parameters (phi, var_eta, scale) calibrated by MLE")
    print()
    print("  Comparison with other methods:")
    print("  - GARCH: parametric, fast, but can be sensitive to outliers")
    print("  - Rolling: non-parametric but noisy and lagging")
    print("  - Kalman: provides confidence bands and smooth estimates")
    print("  - RTS smoother: best MSE (uses future data, not real-time)")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
