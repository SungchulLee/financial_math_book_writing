#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_levy_process_demo.py
Levy Process Simulation, Density, and Parameter Estimation -- Unified Demo

Credits
-------
Based on notebook "1.5 SDE - Levy processes" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 7 -- Extensions & Exotics).

Topics covered
--------------
1. Merton jump-diffusion process:
   - Simulation, closed-form density, histogram, Q-Q plot.
   - Maximum likelihood estimation (MLE).
2. Variance Gamma (VG) process:
   - Simulation via Gamma subordination, density, histogram, Q-Q plot.
   - Approximate method of moments.
   - Maximum likelihood estimation (MLE).
3. Normal Inverse Gaussian (NIG) process:
   - IG first-passage-time interpretation.
   - Simulation via IG subordination, density, histogram, Q-Q plot.
   - Approximate method of moments.
   - Maximum likelihood estimation (MLE).
"""

import numpy as np
import scipy.stats as ss
import scipy.special as scps
from scipy.optimize import minimize
from scipy.integrate import quad
from functools import partial
from math import factorial
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot


# ============================================================================
# CHARACTERISTIC FUNCTIONS
# ============================================================================

def cf_merton(u, t, mu, sig, lam, muJ, sigJ):
    """Characteristic function of the Merton jump-diffusion at time t."""
    return np.exp(
        t * (1j * u * mu - 0.5 * u**2 * sig**2
             + lam * (np.exp(1j * u * muJ - 0.5 * u**2 * sigJ**2) - 1))
    )


def cf_VG(u, t, mu, theta, sigma, kappa):
    """Characteristic function of the Variance Gamma process at time t."""
    return np.exp(
        t * (1j * mu * u
             - np.log(1 - 1j * theta * kappa * u
                       + 0.5 * kappa * sigma**2 * u**2) / kappa)
    )


def cf_NIG(u, t, mu, theta, sigma, kappa):
    """Characteristic function of the Normal Inverse Gaussian at time t."""
    return np.exp(
        t * (1j * mu * u
             + (1 - np.sqrt(1 - 2j * theta * kappa * u
                            + kappa * sigma**2 * u**2)) / kappa)
    )


# ============================================================================
# GIL-PELAEZ INVERSION
# ============================================================================

def Gil_Pelaez_pdf(x, cf, right_lim):
    """Recover PDF from characteristic function via Gil-Pelaez formula."""
    integrand = lambda u: np.real(np.exp(-u * x * 1j) * cf(u))
    return 1 / np.pi * quad(integrand, 1e-15, right_lim)[0]


# ============================================================================
# 1. MERTON JUMP-DIFFUSION
# ============================================================================

def merton_density(x, T, mu, sig, lam, muJ, sigJ, n_terms=20):
    """
    Closed-form density of the Merton process X_T.

    f(x) = e^{-lam*T} * sum_{k=0}^{n_terms}
            (lam*T)^k / k! * N(x; mu*T + k*muJ, sig^2*T + k*sigJ^2)
    """
    tot = 0.0
    for k in range(n_terms):
        var_k = sig**2 * T + k * sigJ**2
        mean_k = mu * T + k * muJ
        tot += ((lam * T)**k
                * np.exp(-((x - mean_k)**2) / (2 * var_k))
                / (factorial(k) * np.sqrt(2 * np.pi * var_k)))
    return np.exp(-lam * T) * tot


def simulate_merton(T, N, mu, sig, lam, muJ, sigJ, seed=42):
    """
    Simulate terminal values of the Merton jump-diffusion:
        X_T = mu*T + sig*sqrt(T)*Z + sum_{i=1}^{N_T} Y_i
    where N_T ~ Poisson(lam*T) and Y_i ~ N(muJ, sigJ^2).
    """
    np.random.seed(seed)
    W = ss.norm.rvs(0, 1, N)
    P = ss.poisson.rvs(lam * T, size=N)
    Jumps = np.array([ss.norm.rvs(muJ, sigJ, k).sum() if k > 0 else 0
                       for k in P])
    return mu * T + np.sqrt(T) * sig * W + Jumps


def mle_merton(data, T, x0=None):
    """
    Maximum likelihood estimation for Merton process parameters.

    Returns
    -------
    dict  Estimated parameters (mu, sig, lam, muJ, sigJ).
    """
    if x0 is None:
        mean_data = np.mean(data) / T
        x0 = [mean_data / 2, 0.5, 1, mean_data / 2, 1]

    def neg_log_likelihood(params):
        density_vals = merton_density(data, T, *params)
        density_vals = np.maximum(density_vals, 1e-300)
        return -np.sum(np.log(density_vals))

    result = minimize(neg_log_likelihood, x0=x0, method="BFGS")
    names = ["mu", "sig", "lam", "muJ", "sigJ"]
    return {n: v for n, v in zip(names, result.x)}, result


# ============================================================================
# 2. VARIANCE GAMMA PROCESS
# ============================================================================

def VG_density(x, T, c, theta, sigma, kappa):
    """
    Closed-form density of the Variance Gamma process.

    Uses the Bessel function K_v representation.
    """
    exponent = theta * (x - c) / sigma**2
    q = T / kappa - 0.5
    arg_bessel = (np.abs(x - c)
                  * np.sqrt(2 * sigma**2 / kappa + theta**2) / sigma**2)
    return (
        2 * np.exp(exponent)
        / (kappa**(T / kappa) * np.sqrt(2 * np.pi) * sigma
           * scps.gamma(T / kappa))
        * (np.abs(x - c)**2
           / (2 * sigma**2 / kappa + theta**2))**(q / 2)
        * scps.kv(q, arg_bessel)
    )


def simulate_VG(T, N, theta, sigma, kappa, seed=42):
    """
    Simulate the VG process via Gamma subordination:
        X = theta * G + sigma * sqrt(G) * Z
    where G ~ Gamma(T/kappa, scale=kappa).
    """
    np.random.seed(seed)
    G = ss.gamma(T / kappa, scale=kappa).rvs(N)
    Z = ss.norm.rvs(0, 1, N)
    return theta * G + sigma * np.sqrt(G) * Z


def approximate_mom_VG(data, T):
    """
    Approximate method of moments for the VG process.
    Uses first-order expansion in theta (ignores theta^2, theta^3, ...).

    Returns
    -------
    dict  Estimated parameters (c, theta, sigma, kappa).
    """
    sigma_hat = np.std(data) / np.sqrt(T)
    kappa_hat = T * ss.kurtosis(data) / 3
    theta_hat = (np.sqrt(T) * ss.skew(data) * sigma_hat / (3 * kappa_hat))
    c_hat = np.mean(data) / T - theta_hat
    return {"c": c_hat, "theta": theta_hat, "sigma": sigma_hat,
            "kappa": kappa_hat}


def mle_VG(data, T, x0_dict=None):
    """
    Maximum likelihood estimation for VG process parameters.
    Uses approximate MoM as initial guess if not provided.

    Returns
    -------
    dict  Estimated parameters (c, theta, sigma, kappa).
    """
    if x0_dict is None:
        x0_dict = approximate_mom_VG(data, T)
    x0 = [x0_dict["c"], x0_dict["theta"], x0_dict["sigma"],
           x0_dict["kappa"]]

    def neg_ll(params):
        density_vals = VG_density(data, T, *params)
        density_vals = np.maximum(density_vals, 1e-300)
        return -np.sum(np.log(density_vals))

    result = minimize(neg_ll, x0=x0, method="L-BFGS-B", tol=1e-8,
                      bounds=[[-1, 1], [-1, -1e-15],
                              [1e-15, 2], [1e-15, None]])
    names = ["c", "theta", "sigma", "kappa"]
    return {n: v for n, v in zip(names, result.x)}, result


# ============================================================================
# 3. NORMAL INVERSE GAUSSIAN PROCESS
# ============================================================================

def NIG_density(x, T, c, theta, sigma, kappa):
    """
    Closed-form density of the Normal Inverse Gaussian process.

    Uses the Bessel function K_1 representation.
    """
    A = theta / sigma**2
    B = np.sqrt(theta**2 + sigma**2 / kappa) / sigma**2
    C = (T / np.pi * np.exp(T / kappa)
         * np.sqrt(theta**2 / (kappa * sigma**2) + 1 / kappa**2))
    arg = np.sqrt((x - c * T)**2 + T**2 * sigma**2 / kappa)
    return (C * np.exp(A * (x - c * T))
            * scps.kv(1, B * arg) / arg)


def simulate_IG(T_val, N, kappa, seed=42):
    """
    Simulate Inverse Gaussian random variables using scipy.

    IG(mu=T_val, lambda=T_val^2/kappa) -- with E[IG] = T_val.
    """
    np.random.seed(seed)
    lam = T_val**2 / kappa
    mus = T_val / lam  # scaled mu
    return ss.invgauss.rvs(mu=mus, scale=lam, size=N)


def simulate_NIG(T_val, N, theta, sigma, kappa, seed=42):
    """
    Simulate the NIG process via Inverse Gaussian subordination:
        X = theta * IG + sigma * sqrt(IG) * Z
    """
    IG = simulate_IG(T_val, N, kappa, seed)
    Z = ss.norm.rvs(0, 1, N)
    return theta * IG + sigma * np.sqrt(IG) * Z


def mle_NIG(data, T, x0_dict=None):
    """
    Maximum likelihood estimation for NIG process parameters.
    Uses approximate MoM as initial guess if not provided.
    """
    if x0_dict is None:
        x0_dict = approximate_mom_VG(data, T)  # same first-order formulas
    x0 = [x0_dict["c"], x0_dict["theta"], x0_dict["sigma"],
           x0_dict["kappa"]]

    def neg_ll(params):
        density_vals = NIG_density(data, T, *params)
        density_vals = np.maximum(density_vals, 1e-300)
        return -np.sum(np.log(density_vals))

    result = minimize(neg_ll, x0=x0, method="L-BFGS-B", tol=1e-8,
                      bounds=[[-1, 1], [-1, -1e-15],
                              [1e-15, 2], [1e-15, None]])
    names = ["c", "theta", "sigma", "kappa"]
    return {n: v for n, v in zip(names, result.x)}, result


# ============================================================================
# VISUALISATION HELPERS
# ============================================================================

def plot_density_comparison(data, x_range, density_fn, cf_fn, cf_y_range,
                            title="Density Comparison"):
    """
    Plot histogram vs closed-form density vs Fourier inversion.
    """
    plt.figure(figsize=(14, 6))
    x = np.linspace(x_range[0], x_range[1], 500)
    plt.plot(x, density_fn(x), color="r", label="Closed-form density")

    if cf_fn is not None and cf_y_range is not None:
        y = np.linspace(cf_y_range[0], cf_y_range[1], 30)
        plt.plot(y, [Gil_Pelaez_pdf(i, cf_fn, np.inf) for i in y],
                 "p", label="Fourier inversion")

    plt.hist(data, density=True, bins=200, facecolor="LightBlue",
             label="Histogram")
    plt.legend()
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_qq(data, title="Q-Q Plot"):
    """Q-Q plot against normal reference distribution."""
    plt.figure(figsize=(6, 5))
    qqplot(data, line="s", ax=plt.gca())
    plt.title(title)
    plt.tight_layout()
    plt.show()


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_merton():
    """Full Merton jump-diffusion demo."""
    print("=" * 60)
    print("Merton Jump-Diffusion Process")
    print("=" * 60)

    mu, sig, lam, muJ, sigJ = 0.05, 0.2, 1.2, 0.15, 0.5
    T, N = 2, 1_000_000

    # Simulate
    X_T = simulate_merton(T, N, mu, sig, lam, muJ, sigJ)

    # Statistics
    print(f"  Mean:     {np.mean(X_T):.4f}")
    print(f"  Std:      {np.std(X_T):.4f}")
    print(f"  Skewness: {ss.skew(X_T):.4f}")
    print(f"  Kurtosis: {ss.kurtosis(X_T):.4f}")

    # Density comparison
    cf_M = partial(cf_merton, t=T, mu=mu, sig=sig, lam=lam, muJ=muJ,
                   sigJ=sigJ)
    density_fn = lambda x: merton_density(x, T, mu, sig, lam, muJ, sigJ)
    plot_density_comparison(X_T, (X_T.min(), X_T.max()), density_fn, cf_M,
                            (-3, 5), "Merton: Histogram vs Density")
    plot_qq(X_T, "Merton Q-Q Plot")

    # MLE
    print("\n--- MLE Estimation ---")
    print(f"  True: mu={mu}, sig={sig}, lam={lam}, muJ={muJ}, sigJ={sigJ}")
    params, result = mle_merton(X_T, T)
    print(f"  MLE:  {params}")
    print(f"  Optimizer: {result.message}")


def demo_variance_gamma():
    """Full Variance Gamma demo."""
    print("\n" + "=" * 60)
    print("Variance Gamma Process")
    print("=" * 60)

    theta, sigma, kappa = -0.1, 0.2, 0.5
    T, N = 2, 1_000_000

    # Simulate
    X = simulate_VG(T, N, theta, sigma, kappa)

    # Statistics
    print(f"  Mean:     {np.mean(X):.4f}")
    print(f"  Std:      {np.std(X):.4f}")
    print(f"  Skewness: {ss.skew(X):.4f}")
    print(f"  Kurtosis: {ss.kurtosis(X):.4f}")

    # Density comparison
    cf_vg = partial(cf_VG, t=T, mu=0, theta=theta, sigma=sigma, kappa=kappa)
    density_fn = lambda x: VG_density(x, T, 0, theta, sigma, kappa)
    plot_density_comparison(X, (X.min(), X.max()), density_fn, cf_vg,
                            (-2, 1), "VG: Histogram vs Density")
    plot_qq(X, "Variance Gamma Q-Q Plot")

    # Approximate MoM
    print("\n--- Approximate Method of Moments ---")
    mom = approximate_mom_VG(X, T)
    print(f"  True: c=0, theta={theta}, sigma={sigma}, kappa={kappa}")
    print(f"  MoM:  {mom}")

    # MLE
    print("\n--- MLE Estimation ---")
    params, result = mle_VG(X, T, mom)
    print(f"  MLE:  {params}")
    print(f"  Optimizer: {result.message}")


def demo_nig():
    """Full Normal Inverse Gaussian demo."""
    print("\n" + "=" * 60)
    print("Normal Inverse Gaussian Process")
    print("=" * 60)

    theta, sigma, kappa = -0.1, 0.2, 0.5
    T, N = 2, 1_000_000

    # Simulate
    X = simulate_NIG(T, N, theta, sigma, kappa)

    # Statistics
    print(f"  Mean:     {np.mean(X):.4f}")
    print(f"  Std:      {np.std(X):.4f}")
    print(f"  Skewness: {ss.skew(X):.4f}")
    print(f"  Kurtosis: {ss.kurtosis(X):.4f}")

    # Density comparison
    cf_nig = partial(cf_NIG, t=T, mu=0, theta=theta, sigma=sigma,
                     kappa=kappa)
    density_fn = lambda x: NIG_density(x, T, 0, theta, sigma, kappa)
    plot_density_comparison(X, (X.min(), X.max()), density_fn, cf_nig,
                            (-2, 1), "NIG: Histogram vs Density")
    plot_qq(X, "NIG Q-Q Plot")

    # Approximate MoM (same formula as VG at first order in theta)
    print("\n--- Approximate Method of Moments ---")
    mom = approximate_mom_VG(X, T)
    print(f"  True: c=0, theta={theta}, sigma={sigma}, kappa={kappa}")
    print(f"  MoM:  {mom}")

    # MLE
    print("\n--- MLE Estimation ---")
    params, result = mle_NIG(X, T, mom)
    print(f"  MLE:  {params}")
    print(f"  Optimizer: {result.message}")


def demo_ig_first_passage():
    """
    Demonstrate that the Inverse Gaussian distribution is the
    first-passage-time distribution of a drifted Brownian motion.
    """
    print("\n" + "=" * 60)
    print("IG as First-Passage-Time of Drifted BM")
    print("=" * 60)

    np.random.seed(42)
    paths, steps = 40000, 10000
    t = 2
    delta = 3 * t  # barrier
    gamma = 2       # drift
    T_max = 20

    T_vec, dt = np.linspace(0, T_max, steps, retstep=True)
    X0 = np.zeros((paths, 1))
    increments = ss.norm.rvs(loc=gamma * dt, scale=np.sqrt(dt),
                             size=(paths, steps - 1))
    Z = np.concatenate((X0, increments), axis=1).cumsum(1)
    T_fp = np.argmax(Z > delta, axis=1) * dt

    # IG density parameters
    mm = delta / gamma
    lam = delta**2
    mm1 = mm / lam

    x = np.linspace(0.01, 10, 5000)

    plt.figure(figsize=(10, 5))
    plt.plot(x, ss.invgauss.pdf(x, mu=mm1, scale=lam),
             color="red", label="IG density")
    plt.hist(T_fp, density=True, bins=100, facecolor="LightBlue",
             label="Simulated first-passage times")
    plt.title("IG Distribution = First-Passage-Time of Drifted BM")
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"  Theoretical mean: {mm:.4f},  Simulated: {T_fp.mean():.4f}")
    print(f"  Theoretical var:  {delta / gamma**3:.4f},  "
          f"Simulated: {T_fp.var():.4f}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_merton()
    demo_variance_gamma()
    demo_nig()
    demo_ig_first_passage()
