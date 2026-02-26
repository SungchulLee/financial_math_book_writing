#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_heston_simulation_statistics.py
Heston Model Simulation, Log-Return Distribution, and CF Stability

Credits
-------
Based on notebook "1.4 SDE - Heston model" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 14 -- Stochastic Volatility).

Topics covered
--------------
1. Generating correlated Normal random variables (explicit formula
   and Cholesky decomposition).
2. Heston process path simulation using log-variables (Euler-Maruyama).
3. Distribution of Heston log-returns: skewness from rho, non-normality.
4. Characteristic function stability: Heston (1993) vs Schoutens (2004).
5. Option pricing comparison: Monte Carlo vs Fourier inversion.
"""

import numpy as np
import scipy.stats as ss
from scipy.integrate import quad
from scipy.linalg import cholesky
from functools import partial
import matplotlib.pyplot as plt


# ============================================================================
# 1. CORRELATED NORMAL RANDOM VARIABLES
# ============================================================================

def generate_correlated_normals_2d(rho, size=100000, method="explicit"):
    """
    Generate bivariate standard Normal with correlation rho.

    Parameters
    ----------
    rho : float       Correlation coefficient in (-1, 1).
    size : int        Number of samples.
    method : str      "explicit" (analytic 2D formula) or "cholesky".

    Returns
    -------
    Y1, Y2 : ndarray  Correlated normal samples.
    """
    Z1 = np.random.normal(0, 1, size)
    Z2 = np.random.normal(0, 1, size)

    if method == "explicit":
        # Y1 = Z1,  Y2 = rho*Z1 + sqrt(1-rho^2)*Z2
        Y1 = Z1
        Y2 = rho * Z1 + np.sqrt(1 - rho**2) * Z2
    elif method == "cholesky":
        COV = np.array([[1, rho], [rho, 1]])
        C = cholesky(COV, lower=True)
        Z = np.vstack([Z1, Z2])
        Y = C @ Z
        Y1, Y2 = Y[0], Y[1]
    else:
        raise ValueError("method must be 'explicit' or 'cholesky'")

    return Y1, Y2


def demo_correlated_normals():
    """Demonstrate generation and verification of correlated normals."""
    rho = 0.6
    size = 1_000_000

    for method in ["explicit", "cholesky"]:
        Y1, Y2 = generate_correlated_normals_2d(rho, size, method)
        corr = np.corrcoef(Y1, Y2)[0, 1]
        print(f"Method '{method}': estimated rho = {corr:.4f} (true: {rho})")


# ============================================================================
# 2. HESTON PROCESS SIMULATION (LOG-VARIABLES)
# ============================================================================

def heston_paths_log(S0, v0, mu, rho, kappa, theta, sigma, T, N=100000,
                     paths=3, seed=42):
    """
    Simulate Heston model paths using log-variables X = log(S), Y = log(v).

    This avoids negative variance values without ad-hoc fixes, but may
    produce overflows for small N (large time steps).

    SDE in log-variables:
        dX = (mu - 0.5*v) dt + sqrt(v) dW1
        dY = v^{-1}[kappa*(theta - v) - 0.5*sigma^2] dt + sigma*v^{-0.5} dW2
    where v = exp(Y).

    Returns
    -------
    T_vec : ndarray   Time grid.
    S : ndarray       Stock price paths, shape (N, paths).
    V : ndarray       Variance paths, shape (N, paths).
    """
    np.random.seed(seed)
    T_vec, dt = np.linspace(0, T, N, retstep=True)
    dt_sq = np.sqrt(dt)

    X0 = np.log(S0)
    Y0 = np.log(v0)

    # Correlated Brownian increments
    MU = np.array([0, 0])
    COV = np.array([[1, rho], [rho, 1]])
    W = ss.multivariate_normal.rvs(mean=MU, cov=COV, size=(N - 1, paths))
    W_S = W[:, :, 0]
    W_v = W[:, :, 1]

    X = np.zeros((N, paths))
    Y = np.zeros((N, paths))
    X[0, :] = X0
    Y[0, :] = Y0

    for t in range(N - 1):
        v = np.exp(Y[t, :])
        v_sq = np.sqrt(v)

        Y[t + 1, :] = (Y[t, :]
                        + (1 / v) * (kappa * (theta - v) - 0.5 * sigma**2) * dt
                        + sigma * (1 / v_sq) * dt_sq * W_v[t, :])
        X[t + 1, :] = (X[t, :]
                        + (mu - 0.5 * v) * dt
                        + v_sq * dt_sq * W_S[t, :])

    return T_vec, np.exp(X), np.exp(Y)


def heston_paths_reflection(S0, v0, mu, rho, kappa, theta, sigma, T,
                            N=20000, paths=20000, seed=42):
    """
    Simulate Heston model using the reflection (absolute value) method
    for the CIR variance process.

    This is more numerically stable than the log-variable approach.

    Returns
    -------
    S_T : ndarray  Terminal stock prices, shape (paths,).
    V_T : ndarray  Terminal variance values, shape (paths,).
    """
    np.random.seed(seed)
    _, dt = np.linspace(0, T, N, retstep=True)
    dt_sq = np.sqrt(dt)

    MU = np.array([0, 0])
    COV = np.array([[1, rho], [rho, 1]])
    W = ss.multivariate_normal.rvs(mean=MU, cov=COV, size=(N - 1, paths))
    W_S = W[:, :, 0]
    W_v = W[:, :, 1]

    log_S = np.full(paths, np.log(S0))
    v = np.full(paths, v0)

    for t in range(N - 1):
        v_pos = np.abs(v)
        v_sq = np.sqrt(v_pos)

        log_S = log_S + (mu - 0.5 * v_pos) * dt + v_sq * dt_sq * W_S[t, :]
        v = np.abs(v + kappa * (theta - v_pos) * dt
                   + sigma * v_sq * dt_sq * W_v[t, :])

    return np.exp(log_S), v


# ============================================================================
# 3. LOG-RETURN DISTRIBUTION ANALYSIS
# ============================================================================

def analyze_log_returns(S_T, S0, title="Log-Return Distribution"):
    """Analyze and plot the log-return distribution of Heston terminal prices."""
    log_R = np.log(S_T / S0)

    print(f"  Mean:     {log_R.mean():.4f}")
    print(f"  Std:      {log_R.std():.4f}")
    print(f"  Skewness: {ss.skew(log_R):.4f}")
    print(f"  Kurtosis: {ss.kurtosis(log_R):.4f}")

    x = np.linspace(log_R.min(), log_R.max(), 500)

    plt.figure(figsize=(10, 5))
    plt.plot(x, ss.norm.pdf(x, log_R.mean(), log_R.std(ddof=0)),
             color="r", label="Normal density")
    plt.hist(log_R, density=True, bins=100, facecolor="LightBlue",
             label="Simulated log-returns")
    plt.legend()
    plt.title(title)
    plt.xlabel("log(S_T/S0)")
    plt.tight_layout()
    plt.show()

    return log_R


# ============================================================================
# 4. CHARACTERISTIC FUNCTIONS (STABLE vs UNSTABLE)
# ============================================================================

def cf_Heston_original(u, t, v0, mu, kappa, theta, sigma, rho):
    """
    Heston characteristic function -- original (1993) formulation.
    Can exhibit discontinuities for large t due to branch cuts.
    """
    xi = kappa - sigma * rho * u * 1j
    d = np.sqrt(xi**2 + sigma**2 * (u**2 + 1j * u))
    g1 = (xi + d) / (xi - d)
    cf = np.exp(
        1j * u * mu * t
        + (kappa * theta) / sigma**2
        * ((xi + d) * t - 2 * np.log((1 - g1 * np.exp(d * t)) / (1 - g1)))
        + (v0 / sigma**2) * (xi + d)
        * (1 - np.exp(d * t)) / (1 - g1 * np.exp(d * t))
    )
    return cf


def cf_Heston_good(u, t, v0, mu, kappa, theta, sigma, rho):
    """
    Heston characteristic function -- Schoutens (2004) stable formulation.
    Uses g2 = 1/g1 to avoid branch-cut discontinuities for large t.
    """
    xi = kappa - sigma * rho * u * 1j
    d = np.sqrt(xi**2 + sigma**2 * (u**2 + 1j * u))
    g1 = (xi + d) / (xi - d)
    g2 = 1 / g1
    cf = np.exp(
        1j * u * mu * t
        + (kappa * theta) / sigma**2
        * ((xi - d) * t - 2 * np.log((1 - g2 * np.exp(-d * t)) / (1 - g2)))
        + (v0 / sigma**2) * (xi - d)
        * (1 - np.exp(-d * t)) / (1 - g2 * np.exp(-d * t))
    )
    return cf


def plot_cf_comparison(v0, mu, kappa, theta, sigma, rho, T):
    """
    Plot the Heston (1993) and Schoutens (2004) characteristic functions
    to show the stability difference for large T.
    """
    cf_orig = partial(cf_Heston_original, t=T, v0=v0, mu=mu, theta=theta,
                      sigma=sigma, kappa=kappa, rho=rho)
    cf_good = partial(cf_Heston_good, t=T, v0=v0, mu=mu, theta=theta,
                      sigma=sigma, kappa=kappa, rho=rho)

    u = np.linspace(-4, 4, 200)

    plt.figure(figsize=(10, 5))
    plt.plot(u, np.real(cf_orig(u)), label="Heston 1993 CF", alpha=0.7)
    plt.plot(u, np.real(cf_good(u)), "--",
             label="Schoutens 2004 CF (stable)")
    plt.title(f"CF Comparison (T={T}): Stable vs Unstable Formulation")
    plt.xlabel("u")
    plt.ylabel("Re[phi(u)]")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# ============================================================================
# 5. OPTION PRICING: MC vs FOURIER
# ============================================================================

def Q1(k, cf, right_lim):
    """Risk-neutral probability under stock numeraire."""
    integrand = lambda u: np.real(
        (np.exp(-u * k * 1j) / (u * 1j)) * cf(u - 1j) / cf(-1j)
    )
    return 0.5 + 1 / np.pi * quad(integrand, 1e-15, right_lim, limit=1000)[0]


def Q2(k, cf, right_lim):
    """Risk-neutral probability under money-market numeraire."""
    integrand = lambda u: np.real(
        np.exp(-u * k * 1j) / (u * 1j) * cf(u)
    )
    return 0.5 + 1 / np.pi * quad(integrand, 1e-15, right_lim, limit=1000)[0]


def price_heston_fourier(S0, K, r, T, v0, kappa, theta, sigma, rho):
    """European call price via Fourier inversion of Heston CF."""
    cf = partial(cf_Heston_good, t=T, v0=v0, mu=r, theta=theta,
                 sigma=sigma, kappa=kappa, rho=rho)
    k = np.log(K / S0)
    return S0 * Q1(k, cf, 1000) - K * np.exp(-r * T) * Q2(k, cf, 1000)


def price_heston_mc(S0, K, r, T, v0, kappa, theta, sigma, rho,
                    N=20000, paths=20000, seed=42):
    """European call price via Monte Carlo with reflection scheme."""
    S_T, _ = heston_paths_reflection(S0, v0, r, rho, kappa, theta, sigma, T,
                                     N=N, paths=paths, seed=seed)
    payoffs = np.exp(-r * T) * np.maximum(S_T - K, 0)
    return {"price": np.mean(payoffs), "std_error": ss.sem(payoffs)}


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all Heston model demonstrations."""
    # --- Parameters ---
    S0, v0 = 100, 0.04
    mu, r = 0.1, 0.05
    rho = -0.9
    kappa, theta, sigma = 2, 0.04, 0.3
    T = 1
    K = 100

    assert 2 * kappa * theta > sigma**2, "Feller condition violated"

    # 1. Correlated normals
    print("=" * 60)
    print("1. Correlated Normal Generation")
    print("=" * 60)
    demo_correlated_normals()

    # 2. Heston paths (log-variable method, small number for plotting)
    print("\n" + "=" * 60)
    print("2. Heston Path Simulation (log-variables)")
    print("=" * 60)
    T_vec, S, V = heston_paths_log(S0, v0, mu, rho, kappa, theta, sigma,
                                    T, N=500000, paths=3)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    ax1.plot(T_vec, S)
    ax1.set_title("Stock price paths")
    ax1.set_xlabel("Time")

    std_asy = np.sqrt(theta * sigma**2 / (2 * kappa))
    ax2.plot(T_vec, V)
    ax2.axhline(theta, color="gray", ls="--", label="Long-term mean")
    ax2.axhline(theta + std_asy, color="black", ls=":", label="1 asy std")
    ax2.axhline(theta - std_asy, color="black", ls=":")
    ax2.set_title("Variance paths")
    ax2.set_xlabel("Time")
    ax2.legend()
    plt.suptitle("Heston Model Simulation")
    plt.tight_layout()
    plt.show()

    # 3. Log-return distribution and skewness from rho
    print("\n" + "=" * 60)
    print("3. Log-Return Distribution (effect of rho)")
    print("=" * 60)

    for rho_val in [-0.9, 0.9]:
        print(f"\nrho = {rho_val}:")
        S_T, _ = heston_paths_reflection(S0, v0, mu, rho_val, kappa, theta,
                                         sigma, T, N=10000, paths=10000)
        analyze_log_returns(S_T, S0,
                           f"Heston Log-Returns (rho={rho_val})")

    # 4. CF stability comparison
    print("\n" + "=" * 60)
    print("4. Characteristic Function Stability (T=15)")
    print("=" * 60)
    plot_cf_comparison(v0=0.08, mu=r, kappa=3, theta=0.1,
                       sigma=0.25, rho=-0.8, T=15)

    # 5. MC vs Fourier pricing
    print("\n" + "=" * 60)
    print("5. Option Pricing: MC vs Fourier Inversion")
    print("=" * 60)

    price_fourier = price_heston_fourier(S0, K, r, T, v0, kappa, theta,
                                         sigma, rho=-0.8)
    mc_result = price_heston_mc(S0, K, r, T, v0, kappa, theta, sigma,
                                rho=-0.8, N=10000, paths=10000)

    print(f"  Fourier inversion call: {price_fourier:.4f}")
    print(f"  Monte Carlo call:       {mc_result['price']:.4f} "
          f"(std err: {mc_result['std_error']:.4f})")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
