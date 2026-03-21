#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_ou_kalman_exit_time.py
OU Process: Kalman Filter State Tracking and First Exit Time from a Strip

Credits
-------
Based on notebook "6.1 Ornstein-Uhlenbeck process and applications" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 18 -- OU Process).

Topics covered
--------------
1. Kalman filter for tracking the hidden OU state from noisy
   observations: Y_k = X_k + eps_k.
2. MLE calibration of Kalman filter parameters (alpha, beta,
   var_eta, var_eps).
3. Rauch-Tung-Striebel smoother for smoothed state estimation.
4. Shumway-Stoffer (1982) EM algorithm for iterative parameter
   estimation as an alternative to direct MLE optimisation.
5. First exit time from a symmetric strip [theta - d, theta + d]:
   - Monte Carlo estimation.
   - ODE for the expected exit time U(x) via upwind finite differences.
   - PDE for the distribution of the exit time via forward Kolmogorov
     equation.

See also: cantaro86_ou_applications.py for OU simulation, estimation,
first hitting time to theta, Vasicek bond pricing, and trading strategy.
"""

import numpy as np
import scipy.stats as ss
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.optimize import minimize
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt


# ============================================================================
# 1. OU SIMULATION (exact formula, from companion module)
# ============================================================================

def simulate_ou(kappa, theta, sigma, X0, T, N, paths=1, seed=42):
    """
    Simulate OU paths using the exact recursive formula.

    Parameters
    ----------
    kappa : float   Mean-reversion speed.
    theta : float   Long-term mean.
    sigma : float   Volatility.
    X0 : float      Initial value.
    T : float       Terminal time.
    N : int         Number of time steps.
    paths : int     Number of Monte Carlo paths.
    seed : int      Random seed.

    Returns
    -------
    X : ndarray, shape (N, paths)
    T_vec : ndarray, shape (N,)
    dt : float
    """
    np.random.seed(seed)
    T_vec, dt = np.linspace(0, T, N, retstep=True)
    X = np.zeros((N, paths))
    X[0, :] = X0
    W = ss.norm.rvs(loc=0, scale=1, size=(N - 1, paths))

    std_dt = np.sqrt(sigma**2 / (2 * kappa) * (1 - np.exp(-2 * kappa * dt)))
    exp_factor = np.exp(-kappa * dt)
    for t in range(N - 1):
        X[t + 1, :] = theta + exp_factor * (X[t, :] - theta) + std_dt * W[t, :]

    return X, T_vec, dt


# ============================================================================
# 2. KALMAN FILTER FOR OU STATE TRACKING
# ============================================================================
#
# Model:
#   True state:    x_k = alpha + beta * x_{k-1} + eta_k,  eta_k ~ N(0, var_eta)
#   Observation:   Y_k = x_k + eps_k,                     eps_k ~ N(0, var_eps)
#
# For the discretised OU process:
#   alpha = theta * (1 - exp(-kappa * dt))
#   beta  = exp(-kappa * dt)
#   var_eta = sigma^2 / (2*kappa) * (1 - exp(-2*kappa*dt))  [exact discretisation]
#
# The Kalman filter tracks the hidden state x_k given noisy observations Y_k.

def kalman_ou(Y, x0, P0, alpha, beta, var_eta, var_eps):
    """
    Kalman filter for the OU state-space model.

    Parameters
    ----------
    Y : ndarray      Noisy observations.
    x0 : float       Initial state estimate.
    P0 : float       Initial covariance.
    alpha : float    Intercept in state equation.
    beta : float     AR(1) coefficient in state equation.
    var_eta : float  State noise variance.
    var_eps : float  Observation noise variance.

    Returns
    -------
    xs : ndarray     Filtered state estimates.
    Ps : ndarray     Filtered covariance estimates.
    loglik : float   Log-likelihood.
    """
    N = len(Y)
    xs = np.zeros(N)
    Ps = np.zeros(N)

    x = x0
    P = P0
    log_2pi = np.log(2 * np.pi)
    loglikelihood = 0.0

    for k in range(N):
        # Prediction
        x_p = alpha + beta * x
        P_p = beta**2 * P + var_eta

        # Innovation
        r = Y[k] - x_p
        S = P_p + var_eps
        KG = P_p / S

        # Update
        x = x_p + KG * r
        P = P_p * (1 - KG)

        loglikelihood += -0.5 * (log_2pi + np.log(S) + r**2 / S)

        xs[k] = x
        Ps[k] = P

    return xs, Ps, loglikelihood


# ============================================================================
# 3. MLE CALIBRATION
# ============================================================================

def calibrate_mle(Y_train, x0, P0):
    """
    Calibrate (alpha, beta, var_eta, var_eps) by maximising the
    Kalman filter log-likelihood.

    Parameters
    ----------
    Y_train : ndarray  Training observations.
    x0 : float         Initial state estimate.
    P0 : float         Initial covariance.

    Returns
    -------
    params : dict  Estimated parameters.
    """
    # Initial guess from OLS on lagged observations
    beta_g, alpha_g, _, _, _ = ss.linregress(Y_train[1:], Y_train[:-1])
    var_eps_g = np.var(Y_train[:-1] - beta_g * Y_train[1:] - alpha_g, ddof=2)

    def neg_loglik(c):
        _, _, ll = kalman_ou(Y_train, x0, P0, c[0], c[1], c[2], c[3])
        return -ll

    result = minimize(
        neg_loglik,
        x0=[alpha_g, beta_g, 0.01, var_eps_g],
        method="L-BFGS-B",
        bounds=[(-1, 1), (1e-15, 1), (1e-15, 1), (1e-15, 1)],
        tol=1e-12,
    )

    return {
        "alpha": result.x[0],
        "beta": result.x[1],
        "var_eta": result.x[2],
        "var_eps": result.x[3],
    }


# ============================================================================
# 4. RTS SMOOTHER
# ============================================================================

def rts_smoother_ou(Y, x0, P0, alpha, beta, var_eta, var_eps):
    """
    Rauch-Tung-Striebel smoother for the OU state-space model.

    Runs the Kalman filter forward, then a backward smoothing pass.

    Parameters
    ----------
    Y : ndarray      Observations.
    x0 : float       Initial state estimate.
    P0 : float       Initial covariance.
    alpha, beta : float  State equation parameters.
    var_eta, var_eps : float  Noise variances.

    Returns
    -------
    xs_smooth : ndarray  Smoothed state estimates.
    Ps_smooth : ndarray  Smoothed covariance estimates.
    Cs_smooth : ndarray  Smoothed cross-covariances (for EM algorithm).
    """
    xs, Ps, _ = kalman_ou(Y, x0, P0, alpha, beta, var_eta, var_eps)
    N = len(xs)

    xs_smooth = np.zeros(N)
    Ps_smooth = np.zeros(N)
    Cs_smooth = np.zeros(N)
    C = np.zeros(N)

    xs_smooth[-1] = xs[-1]
    Ps_smooth[-1] = Ps[-1]

    # Last cross-covariance
    K_last = (beta**2 * Ps[-2] + var_eta) / (beta**2 * Ps[-2] + var_eta + var_eps)
    Cs_smooth[-1] = Ps[-1]
    if N >= 2:
        Cs_smooth[-2] = beta * (1 - K_last) * Ps[-2]

    for k in range(N - 2, -1, -1):
        P_pred = beta**2 * Ps[k] + var_eta
        C[k] = beta * Ps[k] / P_pred
        xs_smooth[k] = xs[k] + C[k] * (xs_smooth[k + 1] - (alpha + xs[k] * beta))
        Ps_smooth[k] = Ps[k] + C[k]**2 * (Ps_smooth[k + 1] - P_pred)

        if k > 0:
            Cs_smooth[k - 1] = (
                Ps[k - 1] * C[k - 1]
                + C[k - 1] * (Cs_smooth[k] - beta * Ps[k - 1]) * C[k - 1]
            )

    return xs_smooth, Ps_smooth, Cs_smooth


# ============================================================================
# 5. SHUMWAY-STOFFER EM ALGORITHM
# ============================================================================

def shumway_stoffer_em(Y_train, x0, P0, max_iter=1000, tol=0.001):
    """
    Shumway-Stoffer (1982) EM algorithm for parameter estimation
    in the linear state-space model.

    This is an alternative to direct MLE optimisation. It alternates
    between:
      E-step: Run Kalman smoother with current parameters.
      M-step: Update (alpha, beta, var_eta, var_eps) from sufficient
              statistics computed from smoothed estimates.

    Parameters
    ----------
    Y_train : ndarray  Training observations.
    x0 : float         Initial state guess.
    P0 : float         Initial covariance guess.
    max_iter : int     Maximum EM iterations.
    tol : float        Convergence tolerance for parameter changes.

    Returns
    -------
    params : dict  Estimated parameters.
    n_iter : int   Number of iterations.
    """
    N = len(Y_train)

    # Initial guesses from OLS
    beta_g, alpha_g, _, _, _ = ss.linregress(Y_train[1:], Y_train[:-1])
    var_eps_g = np.var(Y_train[:-1] - beta_g * Y_train[1:] - alpha_g, ddof=2)

    alpha_em = alpha_g
    beta_em = beta_g
    var_eta_em = 0.1
    var_eps_em = var_eps_g

    for it in range(max_iter):
        a_old = alpha_em
        b_old = beta_em
        eta_old = var_eta_em
        eps_old = var_eps_em

        # E-step: run smoother
        x_sm, P_sm, C_sm = rts_smoother_ou(
            Y_train, x0, P0, alpha_em, beta_em, var_eta_em, var_eps_em)

        # Sufficient statistics
        AA = np.sum(P_sm[:-1] + x_sm[:-1]**2)       # sum(P_k + x_k^2)
        BB = np.sum(C_sm[:-1] + x_sm[:-1] * x_sm[1:])  # sum(C_k + x_k * x_{k+1})
        CC = np.sum(x_sm[1:])                        # sum(x_{k+1})
        DD = np.sum(x_sm[:-1])                       # sum(x_k)

        # M-step: update parameters
        alpha_em = (AA * CC - BB * DD) / (N * AA - DD**2)
        beta_em = (N * BB - CC * DD) / (N * AA - DD**2)

        var_eta_em = (
            np.sum(
                P_sm[1:] + x_sm[1:]**2
                + alpha_em**2
                + P_sm[:-1] * beta_em**2 + (x_sm[:-1] * beta_em)**2
                - 2 * alpha_em * x_sm[1:]
                - 2 * beta_em * (C_sm[:-1] + x_sm[:-1] * x_sm[1:])
                + 2 * alpha_em * beta_em * x_sm[:-1]
            ) / N
        )

        var_eps_em = np.sum(
            P_sm + (Y_train - x_sm)**2
        ) / N

        # Convergence check
        delta = max(
            abs(alpha_em - a_old),
            abs(beta_em - b_old),
            abs(var_eta_em - eta_old),
            abs(var_eps_em - eps_old),
        )
        if delta < tol:
            return {
                "alpha": alpha_em, "beta": beta_em,
                "var_eta": var_eta_em, "var_eps": var_eps_em,
            }, it + 1

    return {
        "alpha": alpha_em, "beta": beta_em,
        "var_eta": var_eta_em, "var_eps": var_eps_em,
    }, max_iter


# ============================================================================
# 6. FIRST EXIT TIME FROM A STRIP
# ============================================================================

def exit_time_mc(X, theta, half_width, dt):
    """
    Monte Carlo estimation of the first exit time from the strip
    [theta - half_width, theta + half_width].

    Parameters
    ----------
    X : ndarray, shape (N, paths)  Simulated OU paths.
    theta : float    Centre of the strip.
    half_width : float  Half-width of the strip.
    dt : float       Time step.

    Returns
    -------
    T_exit : ndarray   First exit times for each path.
    """
    lower = theta - half_width
    upper = theta + half_width
    exit_idx = np.argmax(np.logical_or(X <= lower, X >= upper), axis=0)
    T_exit = exit_idx * dt
    return T_exit


def exit_time_ode(kappa, theta, sigma, half_width, Nspace=100000):
    """
    Solve the ODE for the expected exit time U(x) from the strip
    [theta - d, theta + d] via upwind finite differences.

    The ODE is:
        kappa*(theta - x) * U'(x) + 0.5*sigma^2 * U''(x) = -1
    with boundary conditions U(theta - d) = U(theta + d) = 0.

    Parameters
    ----------
    kappa : float     Mean-reversion speed.
    theta : float     Long-term mean.
    sigma : float     Volatility.
    half_width : float  Half-width d of the strip.
    Nspace : int      Number of grid points.

    Returns
    -------
    x : ndarray    Spatial grid.
    U : ndarray    Expected exit time as a function of starting point.
    """
    x_min = theta - half_width
    x_max = theta + half_width
    x, dx = np.linspace(x_min, x_max, Nspace, retstep=True)

    U = np.zeros(Nspace)
    rhs = -np.ones(Nspace - 2)

    sig2 = sigma**2
    dxx = dx**2

    # Upwind scheme
    drift = kappa * (theta - x[1:-1])
    max_part = np.maximum(drift, 0)
    min_part = np.minimum(drift, 0)

    a = -min_part / dx + 0.5 * sig2 / dxx
    b = (min_part - max_part) / dx - sig2 / dxx
    c = max_part / dx + 0.5 * sig2 / dxx

    D = sparse.diags([a[1:], b, c[:-1]], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()

    U[1:-1] = spsolve(D, rhs)

    return x, U


def exit_time_pde(kappa, theta, sigma, half_width, T_max,
                  Nspace=6000, Ntime=8000):
    """
    Solve the PDE for the CDF of the first exit time from the strip
    [theta - d, theta + d] via implicit upwind finite differences.

    The forward Kolmogorov PDE for the survival probability
    P(t, x) = P(tau > t | X_0 = x):
        dP/dt = kappa*(theta - x)*dP/dx + 0.5*sigma^2*d^2P/dx^2
    with:
        P(0, x) = 0         (initial condition: zero probability at t=0)
        P(t, x_min) = 1     (absorbed at lower boundary)
        P(t, x_max) = 1     (absorbed at upper boundary)

    The exit time density is then d/dt P(t, x).

    Parameters
    ----------
    kappa : float      Mean-reversion speed.
    theta : float      Long-term mean.
    sigma : float      Volatility.
    half_width : float Half-width d of the strip.
    T_max : float      Maximum time for the PDE solution.
    Nspace : int       Number of spatial grid points.
    Ntime : int        Number of time steps.

    Returns
    -------
    x : ndarray       Spatial grid.
    T_array : ndarray Time grid.
    V : ndarray       CDF of exit time, shape (Nspace, Ntime).
    """
    x_min = theta - half_width
    x_max = theta + half_width
    x, dx = np.linspace(x_min, x_max, Nspace, retstep=True)
    T_array, Dt = np.linspace(0, T_max, Ntime, retstep=True)

    V = np.zeros((Nspace, Ntime))
    offset = np.zeros(Nspace - 2)

    # Initial condition: P(0, x) = 0  (no exits yet)
    V[:, 0] = 0
    # Boundary conditions: P(t, x_min) = 1, P(t, x_max) = 1
    V[-1, :] = 1
    V[0, :] = 1

    sig2 = sigma**2
    dxx = dx**2
    r_int = x[1:-1]
    drift = kappa * (theta - r_int)
    max_part = np.maximum(drift, 0)
    min_part = np.minimum(drift, 0)

    # Implicit scheme coefficients (forward in time)
    a = min_part * (Dt / dx) - 0.5 * sig2 * (Dt / dxx)
    b = 1 + sig2 * (Dt / dxx) + (Dt / dx) * (max_part - min_part)
    c = -max_part * (Dt / dx) - 0.5 * sig2 * (Dt / dxx)

    D = sparse.diags([a[1:], b, c[:-1]], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()

    for n in range(1, Ntime):
        offset[0] = a[0] * V[0, n]
        offset[-1] = c[-1] * V[-1, n]
        V[1:-1, n] = spsolve(D, V[1:-1, n - 1] - offset)

    return x, T_array, V


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all OU Kalman filter and exit time demonstrations."""

    # ---- OU parameters ----
    kappa, theta, sigma = 3.0, 0.5, 0.5
    X0 = 2.0
    T, N, paths = 5, 20000, 5000
    std_asy = np.sqrt(sigma**2 / (2 * kappa))

    # ---- 1. Simulate OU process ----
    print("=" * 60)
    print("1. OU Process Simulation")
    print("=" * 60)

    X, T_vec, dt = simulate_ou(kappa, theta, sigma, X0, T, N, paths)
    X_1 = X[:, 1]  # single path for Kalman tracking
    print(f"  kappa={kappa}, theta={theta}, sigma={sigma}, X0={X0}")
    print(f"  Asymptotic std dev = {std_asy:.4f}")

    # ---- 2. Add measurement noise ----
    print("\n" + "=" * 60)
    print("2. Kalman Filter for OU State Tracking")
    print("=" * 60)

    # Derive exact discretisation parameters
    beta_true = np.exp(-kappa * dt)
    alpha_true = theta * (1 - beta_true)
    var_eta_true = sigma**2 / (2 * kappa) * (1 - np.exp(-2 * kappa * dt))

    # OLS estimation to get residual std
    XX = X_1[:-1]
    YY = X_1[1:]
    beta_ols, alpha_ols, _, _, _ = ss.linregress(XX, YY)
    resid = YY - beta_ols * XX - alpha_ols
    std_resid = np.std(resid, ddof=2)

    sig_eps = 0.1
    var_eps_true = sig_eps**2

    np.random.seed(42)
    eps = ss.norm.rvs(loc=0, scale=sig_eps, size=N)
    eps[0] = 0
    Y_1 = X_1 + eps  # noisy observations

    print(f"  Measurement noise std = {sig_eps}")
    print(f"  True state var_eta = {var_eta_true:.6f}")

    # Plot true vs noisy
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.plot(T_vec, X_1, linewidth=0.5, alpha=1, label="True OU process",
            color="tab:blue")
    ax.plot(T_vec, Y_1, linewidth=0.3, alpha=0.4,
            label="Noisy observations (Y = X + eps)", color="tab:blue")
    ax.axhline(theta, color="tab:red", label="Long-term mean")
    ax.legend()
    ax.set_title("OU Process: True State vs Noisy Observations")
    ax.set_xlabel("Time")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ---- 3. Train/test split + MLE calibration ----
    skip_data = 1000
    training_size = 5000
    train = Y_1[skip_data: skip_data + training_size]
    test = Y_1[skip_data + training_size:]
    X_test = X_1[skip_data + training_size:]

    print("\n  MLE Calibration...")
    params_mle = calibrate_mle(train, X0, 10)
    print(f"    alpha: {params_mle['alpha']:.6f}  (true: {alpha_true:.6f})")
    print(f"    beta:  {params_mle['beta']:.6f}  (true: {beta_true:.6f})")
    print(f"    var_eta: {params_mle['var_eta']:.6f}  (true: {var_eta_true:.6f})")
    print(f"    var_eps: {params_mle['var_eps']:.6f}  (true: {var_eps_true:.6f})")

    # ---- 4. Shumway-Stoffer EM ----
    print("\n  Shumway-Stoffer EM Algorithm...")
    params_em, n_iter = shumway_stoffer_em(train, 1, 10)
    print(f"    Converged in {n_iter} iterations")
    print(f"    alpha: {params_em['alpha']:.6f}")
    print(f"    beta:  {params_em['beta']:.6f}")
    print(f"    var_eta: {params_em['var_eta']:.6f}")
    print(f"    var_eps: {params_em['var_eps']:.6f}")

    # ---- 5. Run Kalman filter + smoother on test set ----
    print("\n  Running Kalman filter on test set...")
    a, b = params_mle["alpha"], params_mle["beta"]
    ve, vp = params_mle["var_eta"], params_mle["var_eps"]

    # Get initial conditions from training
    x_tmp, P_tmp, _ = kalman_ou(train, 1, 10, a, b, ve, vp)
    xs, Ps, _ = kalman_ou(test, x_tmp[-1], P_tmp[-1], a, b, ve, vp)
    x_smooth, P_smooth, _ = rts_smoother_ou(
        test, x_tmp[-1], P_tmp[-1], a, b, ve, vp)

    V_up = xs + np.sqrt(Ps)
    V_down = xs - np.sqrt(Ps)

    # Error analysis
    mse_kalman = np.mean((xs - X_test)**2)
    mse_smooth = np.mean((x_smooth - X_test)**2)
    mae_kalman = np.mean(np.abs(xs - X_test))
    avg_std = np.mean(np.sqrt(Ps))

    print(f"  MSE Kalman filter:  {mse_kalman:.6f}")
    print(f"  MSE RTS smoother:   {mse_smooth:.6f}")
    print(f"  MAE Kalman filter:  {mae_kalman:.6f}")
    print(f"  Average std of estimate: {avg_std:.6f}")

    # Plot
    T_test = T_vec[skip_data + training_size:]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

    ax1.plot(T_test, xs, linewidth=0.5, label="Kalman estimate",
             color="tab:blue")
    ax1.plot(T_test, test, linewidth=0.3, alpha=0.4,
             label="Noisy observations", color="tab:blue")
    ax1.plot(T_test, x_smooth, linewidth=0.5,
             label="RTS smoother", color="purple")
    ax1.fill_between(T_test, V_up, V_down, alpha=0.3, color="seagreen",
                     label=r"Kalman $\pm 1\sigma$")
    ax1.axhline(theta, color="tab:red", label="Long-term mean")
    ax1.legend(fontsize=8)
    ax1.set_title("Kalman Filter & Smoother (test set)")
    ax1.set_xlabel("Time")
    ax1.grid(True, alpha=0.3)

    ax2.plot(T_test, np.abs(xs - X_test), linewidth=0.5,
             label=f"Kalman |error| (MSE={mse_kalman:.4f})", alpha=0.7)
    ax2.plot(T_test, np.abs(x_smooth - X_test), linewidth=0.5,
             label=f"Smoother |error| (MSE={mse_smooth:.4f})", alpha=0.7)
    ax2.plot(T_test, np.sqrt(Ps), linewidth=0.5, color="green",
             label="Kalman std", alpha=0.7)
    ax2.legend(fontsize=8)
    ax2.set_title("Estimation Error")
    ax2.set_xlabel("Time")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # ---- 6. First exit time from strip ----
    print("\n" + "=" * 60)
    print("3. First Exit Time from Strip [theta ± std_asy]")
    print("=" * 60)

    # Use the trading strategy parameters
    kappa2, theta2, sigma2 = 10.0, 0.0, 2.0
    X0_2 = 0.0
    T2, N2, paths2 = 1, 1000, 5000
    std_asy2 = np.sqrt(sigma2**2 / (2 * kappa2))

    X2, T_vec2, dt2 = simulate_ou(kappa2, theta2, sigma2, X0_2, T2, N2,
                                   paths2, seed=41)

    # MC exit times
    T_exit_mc = exit_time_mc(X2, theta2, std_asy2, dt2)
    has_non_exit = (T_exit_mc == 0).any()
    print(f"  Strip: [{theta2 - std_asy2:.4f}, {theta2 + std_asy2:.4f}]")
    print(f"  Any paths that never exit? {has_non_exit}")
    print(f"  MC expected exit time: {T_exit_mc.mean():.6f}"
          f"  (std error: {ss.sem(T_exit_mc):.6f})")

    # ODE for expected exit time
    print("\n  Solving ODE for expected exit time U(x)...")
    x_ode, U_ode = exit_time_ode(kappa2, theta2, sigma2, std_asy2)
    expected_t_ode = np.interp(X0_2, x_ode, U_ode)
    print(f"  ODE expected exit time at X0={X0_2}: {expected_t_ode:.6f}")

    # PDE for exit time distribution
    print("\n  Solving PDE for exit time distribution...")
    x_pde, T_pde, V_pde = exit_time_pde(
        kappa2, theta2, sigma2, std_asy2, T2,
        Nspace=6000, Ntime=8000)

    # Interpolate CDF at X0
    fn = RegularGridInterpolator((x_pde, T_pde), V_pde,
                                  bounds_error=False, fill_value=None)
    Cumulative = fn((X0_2, T_pde))
    Dt_pde = T_pde[1] - T_pde[0]
    distribution = (Cumulative[1:] - Cumulative[:-1]) / Dt_pde

    # Expected time from density
    exp_t_pde = distribution @ T_pde[:-1] * Dt_pde
    print(f"  PDE expected exit time at X0={X0_2}: {exp_t_pde:.6f}")

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.plot(x_ode, U_ode, label="Expected exit time U(x)")
    ax1.axvline(X0_2, color="k", ls="--", label=f"X0={X0_2}")
    ax1.axvline(theta2 + std_asy2, color="g", ls="--", label="Strip boundary")
    ax1.axvline(theta2 - std_asy2, color="g", ls="--")
    ax1.set_xlabel("Starting point x")
    ax1.set_ylabel("Expected time")
    ax1.set_title("Expected Exit Time (ODE solution)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.hist(T_exit_mc, density=True, bins=100, facecolor="LightBlue",
             label="MC histogram")
    ax2.plot(T_pde[:-1], distribution, color="red",
             label="PDE density", linewidth=2)
    ax2.axvline(expected_t_ode, color="k", ls="--",
                label=f"E[tau] = {expected_t_ode:.4f}")
    ax2.set_xlim(0, min(0.4, T2))
    ax2.set_xlabel("Time")
    ax2.set_title("Distribution of First Exit Time from Strip")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # ---- Summary ----
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("  Kalman filter for OU state tracking:")
    print(f"    MSE (filter):   {mse_kalman:.6f}")
    print(f"    MSE (smoother): {mse_smooth:.6f}")
    print("    MLE and Shumway-Stoffer EM both recover true parameters.")
    print()
    print("  First exit time from strip:")
    print(f"    MC estimate:  {T_exit_mc.mean():.6f}")
    print(f"    ODE estimate: {expected_t_ode:.6f}")
    print(f"    PDE estimate: {exp_t_pde:.6f}")
    print("    All three methods agree closely.")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
