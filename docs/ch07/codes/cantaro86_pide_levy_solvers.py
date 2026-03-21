#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_pide_levy_solvers.py
PIDE Solvers for Lévy Process Option Pricing: VG and NIG

Credits
-------
Based on notebooks from cantaro86, "Financial Models Numerical Methods":
    3.1 "Merton jump-diffusion, PIDE method"
    3.2 "Variance Gamma model, PIDE method"
    3.3 "Pricing with the NIG Process"
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 7 -- Extensions & Exotics).

Topics covered
--------------
1. Variance Gamma PIDE solver:
   - VG Lévy measure and cutoff epsilon decomposition.
   - PIDE discretisation: tridiagonal diffusion + convolution for jumps.
   - FFT convolution optimisation.
2. NIG PIDE solver:
   - NIG Lévy measure (Bessel K function, singularity at 0).
   - Verification of mean, variance, and martingale correction via
     numerical integration of the Lévy measure.
   - PIDE discretisation analogous to VG.
3. Merton model limitations:
   - Sensitivity of Merton price to jump-size volatility sigJ.

Note: The Merton PIDE solver is already available in
      cantaro86_merton_pricer.py.  This module focuses on the VG and NIG
      PIDE methods which are not covered in the other pricer files.
"""

import numpy as np
import scipy.stats as ss
import scipy.special as scps
import matplotlib.pyplot as plt
from scipy import sparse, signal
from scipy.sparse.linalg import splu
from scipy.integrate import quad


# ============================================================================
# 1. VARIANCE GAMMA -- LÉVY MEASURE AND PIDE SOLVER
# ============================================================================

def vg_levy_measure(y, theta, sigma, kappa):
    """
    VG Lévy measure:  nu(y) = exp(A*y - B*|y|) / (kappa * |y|)

    where A = theta/sigma^2,  B = sqrt(theta^2 + 2*sigma^2/kappa) / sigma^2.

    The VG process has infinite activity (nu integrates to infinity near 0)
    but finite variation.

    Parameters
    ----------
    y : float or ndarray  Jump size(s).
    theta : float         Drift of the subordinated BM.
    sigma : float         Volatility of the subordinated BM.
    kappa : float         Variance rate of the Gamma subordinator.
    """
    A = theta / (sigma**2)
    B = np.sqrt(theta**2 + 2 * sigma**2 / kappa) / sigma**2
    return np.exp(A * y - B * np.abs(y)) / (kappa * np.abs(y))


def vg_pide(S0, K, T, r, theta, sigma, kappa, payoff="call",
            Nspace=5000, Ntime=5000):
    """
    Price a European option under the Variance Gamma model by solving
    the PIDE in log-variables.

    The VG PIDE (in x = log S):
        dV/dt + (r - w - 0.5*sig_eps^2) dV/dx + 0.5*sig_eps^2 d2V/dx2
        - (r + lam) V + integral[V(x+z) nu(z) dz] = 0

    where w is the martingale correction, sig_eps^2 captures small jumps
    (|z| < eps), and lam + integral captures big jumps (|z| >= eps).

    The key subtlety for infinite-activity processes (VG, NIG) is the
    epsilon cutoff: the Lévy measure is singular at z=0, so we decompose
    the process into:
        - Small jumps (|z| < eps): approximated as a diffusion with
          variance sig_eps^2 = integral_{|z|<eps} z^2 nu(dz).
        - Big jumps (|z| >= eps): treated as a compound Poisson process
          with intensity lam = integral_{|z|>=eps} nu(dz).

    Parameters
    ----------
    S0 : float      Spot price.
    K : float       Strike price.
    T : float       Time to maturity.
    r : float       Risk-free rate.
    theta : float   VG drift parameter.
    sigma : float   VG volatility parameter.
    kappa : float   VG variance rate parameter.
    payoff : str    "call" or "put".
    Nspace : int    Number of spatial grid points.
    Ntime : int     Number of time steps.

    Returns
    -------
    dict with keys:
        price : float     Option price at S0.
        S_grid : ndarray  Stock price grid.
        V_curve : ndarray Option values at t=0.
    """
    X0 = np.log(S0)
    W = -np.log(1 - theta * kappa - kappa / 2 * sigma**2) / kappa
    dev_X = np.sqrt(sigma**2 + theta**2 * kappa)

    S_max = 3 * float(K)
    S_min = float(K) / 3
    x_max = np.log(S_max)
    x_min = np.log(S_min)

    dx = (x_max - x_min) / (Nspace - 1)
    extraP = int(np.floor(3 * dev_X / dx))
    x = np.linspace(x_min - extraP * dx, x_max + extraP * dx,
                     Nspace + 2 * extraP)
    T_vec, dt = np.linspace(0, T, Ntime, retstep=True)

    # Cutoff epsilon
    eps = 1.5 * dx

    levy_m = lambda y: vg_levy_measure(y, theta, sigma, kappa)

    # Approximated intensity (big jumps)
    lam = (quad(levy_m, -(extraP + 1.5) * dx, -eps)[0]
           + quad(levy_m, eps, (extraP + 1.5) * dx)[0])

    # Martingale correction (truncated)
    int_w = lambda y: (np.exp(y) - 1) * levy_m(y)
    w = (quad(int_w, -(extraP + 1.5) * dx, -eps)[0]
         + quad(int_w, eps, (extraP + 1.5) * dx)[0])

    # Small jumps variance (diffusion approximation)
    int_s = lambda y: np.abs(y) * np.exp(
        theta / sigma**2 * y
        - np.sqrt(theta**2 + 2 * sigma**2 / kappa) / sigma**2 * np.abs(y)
    ) / kappa
    sig2 = quad(int_s, -eps, eps)[0]

    # Tridiagonal matrix coefficients
    dxx = dx * dx
    a = (dt / 2) * ((r - w - 0.5 * sig2) / dx - sig2 / dxx)
    b = 1 + dt * (sig2 / dxx + r + lam)
    c = -(dt / 2) * ((r - w - 0.5 * sig2) / dx + sig2 / dxx)
    D = sparse.diags([a, b, c], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()
    DD = splu(D)

    # Lévy measure vector (zero near center due to cutoff)
    nu = np.zeros(2 * extraP + 3)
    x_med = extraP + 1
    x_nu = np.linspace(-(extraP + 1 + 0.5) * dx, (extraP + 1 + 0.5) * dx,
                        2 * (extraP + 2))
    for i in range(len(nu)):
        if i in (x_med - 1, x_med, x_med + 1):
            continue
        nu[i] = quad(levy_m, x_nu[i], x_nu[i + 1])[0]

    # Grid initialisation
    if payoff == "call":
        Payoff = np.maximum(np.exp(x) - K, 0)
    else:
        Payoff = np.maximum(K - np.exp(x), 0)

    V = np.zeros((Nspace + 2 * extraP, Ntime))
    offset = np.zeros(Nspace - 2)
    V[:, -1] = Payoff

    if payoff == "call":
        V[-extraP - 1:, :] = (
            np.exp(x[-extraP - 1:]).reshape(-1, 1)
            * np.ones((extraP + 1, Ntime))
            - K * np.exp(-r * T_vec[::-1]) * np.ones((extraP + 1, Ntime))
        )
        V[:extraP + 1, :] = 0
    else:
        V[-extraP - 1:, :] = 0
        V[:extraP + 1, :] = (
            K * np.exp(-r * T_vec[::-1]) * np.ones((extraP + 1, Ntime))
            - np.exp(x[:extraP + 1]).reshape(-1, 1)
            * np.ones((extraP + 1, Ntime))
        )

    # Backward iteration using FFT convolution
    for i in range(Ntime - 2, -1, -1):
        offset[0] = a * V[extraP, i]
        offset[-1] = c * V[-1 - extraP, i]
        V_jump = (V[extraP + 1:-extraP - 1, i + 1]
                  + dt * signal.fftconvolve(V[:, i + 1], nu[::-1],
                                             mode="valid"))
        V[extraP + 1:-extraP - 1, i] = DD.solve(V_jump - offset)

    price = np.interp(X0, x, V[:, 0])
    S_grid = np.exp(x[extraP:-extraP])
    V_curve = V[extraP:-extraP, 0]

    return {"price": price, "S_grid": S_grid, "V_curve": V_curve}


# ============================================================================
# 2. NORMAL INVERSE GAUSSIAN -- LÉVY MEASURE AND PIDE SOLVER
# ============================================================================

def nig_levy_measure(y, theta, sigma, kappa):
    """
    NIG Lévy measure:
        nu(y) = C / |y| * exp(A*y) * K_1(B*|y|)

    where A = theta/sigma^2,
          B = sqrt(theta^2 + sigma^2/kappa) / sigma^2,
          C = sqrt(theta^2 + sigma^2/kappa) / (pi * sigma * sqrt(kappa)),
    and K_1 is the modified Bessel function of the second kind of order 1.

    The NIG process has infinite activity and infinite variation.

    Parameters
    ----------
    y : float or ndarray  Jump size(s).
    theta : float         Drift of the subordinated BM.
    sigma : float         Volatility of the subordinated BM.
    kappa : float         Variance of the IG subordinator.
    """
    A = theta / (sigma**2)
    B = np.sqrt(theta**2 + sigma**2 / kappa) / sigma**2
    C = np.sqrt(theta**2 + sigma**2 / kappa) / (np.pi * sigma * np.sqrt(kappa))
    return C / np.abs(y) * np.exp(A * y) * scps.kv(1, B * np.abs(y))


def nig_verify_moments(theta, sigma, kappa, verbose=True):
    """
    Verify the NIG process moments by numerical integration of the
    Lévy measure.  Compares with the theoretical values:
        mean = theta
        variance = sigma^2 + theta^2 * kappa
        martingale correction w = (1 - sqrt(1 - 2*theta*kappa - kappa*sigma^2)) / kappa

    Returns
    -------
    dict with keys: mean_int, variance_int, w_int, mean_th, variance_th, w_th.
    """
    levy_m = lambda y: nig_levy_measure(y, theta, sigma, kappa)
    dev_X = np.sqrt(sigma**2 + theta**2 * kappa)

    # Theoretical values
    w_th = (1 - np.sqrt(1 - 2 * theta * kappa - kappa * sigma**2)) / kappa
    var_th = dev_X**2

    # Mean (drift component + tail integral)
    beta = theta / sigma**2
    alpha = np.sqrt(beta**2 + 1 / (kappa * sigma**2))
    delta = sigma / np.sqrt(kappa)
    int_drift = lambda y: (
        2 / np.pi * delta * alpha * np.sinh(beta * y) * scps.kv(1, alpha * np.abs(y))
    )
    drift = quad(int_drift, 0, 1, points=[0], limit=2000)[0]
    int_tail = lambda y: y * levy_m(y)
    mean_tail = (quad(int_tail, -10, -1, limit=2000)[0]
                 + quad(int_tail, 1, 10, limit=2000)[0])
    mean_int = drift + mean_tail

    # Variance
    int_var = lambda y: y**2 * levy_m(y)
    var_int = quad(int_var, -2, 2, points=[0])[0]

    # Martingale correction
    epsilon = 1e-7
    int_w = lambda y: (np.exp(y) - 1) * levy_m(y)
    w_int = (quad(int_w, -10, -epsilon)[0]
             + quad(int_w, epsilon, 10)[0])

    if verbose:
        print(f"  Mean:   theoretical={theta:.6f}, "
              f"integrated={mean_int:.6f}")
        print(f"  Var:    theoretical={var_th:.6f}, "
              f"integrated={var_int:.6f}")
        print(f"  w:      theoretical={w_th:.6f}, "
              f"integrated={w_int:.6f}")

    return {"mean_int": mean_int, "variance_int": var_int, "w_int": w_int,
            "mean_th": theta, "variance_th": var_th, "w_th": w_th}


def nig_pide(S0, K, T, r, theta, sigma, kappa, payoff="call",
             Nspace=5000, Ntime=5000):
    """
    Price a European option under the NIG model by solving the PIDE
    in log-variables.

    Uses the same epsilon cutoff framework as the VG PIDE:
    - Small jumps (|z| < eps) approximated as diffusion.
    - Big jumps (|z| >= eps) treated as compound Poisson.

    Parameters
    ----------
    S0, K, T, r : float       Standard option parameters.
    theta, sigma, kappa : float  NIG process parameters.
    payoff : str               "call" or "put".
    Nspace, Ntime : int        Grid sizes.

    Returns
    -------
    dict with keys: price, S_grid, V_curve.
    """
    X0 = np.log(S0)
    w_mc = (1 - np.sqrt(1 - 2 * theta * kappa - kappa * sigma**2)) / kappa
    dev_X = np.sqrt(sigma**2 + theta**2 * kappa)

    S_max = 3 * float(K)
    S_min = float(K) / 3
    x_max = np.log(S_max)
    x_min = np.log(S_min)

    dx = (x_max - x_min) / (Nspace - 1)
    extraP = int(np.floor(3 * dev_X / dx))
    x = np.linspace(x_min - extraP * dx, x_max + extraP * dx,
                     Nspace + 2 * extraP)
    T_vec, dt = np.linspace(0, T, Ntime, retstep=True)

    eps = 1.5 * dx
    levy_m = lambda y: nig_levy_measure(y, theta, sigma, kappa)

    # Approximated intensity (big jumps)
    lam = (quad(levy_m, -(extraP + 1.5) * dx, -eps)[0]
           + quad(levy_m, eps, (extraP + 1.5) * dx)[0])

    # Martingale correction (truncated)
    int_w = lambda y: (np.exp(y) - 1) * levy_m(y)
    w = (quad(int_w, -(extraP + 1.5) * dx, -eps)[0]
         + quad(int_w, eps, (extraP + 1.5) * dx)[0])

    # Small jumps variance
    int_s = lambda y: y**2 * levy_m(y)
    sig2 = quad(int_s, -eps, eps, points=[0])[0]

    # Tridiagonal matrix
    dxx = dx * dx
    a = (dt / 2) * ((r - w - 0.5 * sig2) / dx - sig2 / dxx)
    b = 1 + dt * (sig2 / dxx + r + lam)
    c = -(dt / 2) * ((r - w - 0.5 * sig2) / dx + sig2 / dxx)
    D = sparse.diags([a, b, c], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()
    DD = splu(D)

    # Lévy measure vector
    nu = np.zeros(2 * extraP + 3)
    x_med = extraP + 1
    x_nu = np.linspace(-(extraP + 1 + 0.5) * dx, (extraP + 1 + 0.5) * dx,
                        2 * (extraP + 2))
    for i in range(len(nu)):
        if i in (x_med - 1, x_med, x_med + 1):
            continue
        nu[i] = quad(levy_m, x_nu[i], x_nu[i + 1])[0]

    # Grid initialisation
    if payoff == "call":
        Payoff = np.maximum(np.exp(x) - K, 0)
    else:
        Payoff = np.maximum(K - np.exp(x), 0)

    V = np.zeros((Nspace + 2 * extraP, Ntime))
    offset = np.zeros(Nspace - 2)
    V[:, -1] = Payoff

    if payoff == "call":
        V[-extraP - 1:, :] = (
            np.exp(x[-extraP - 1:]).reshape(-1, 1)
            * np.ones((extraP + 1, Ntime))
            - K * np.exp(-r * T_vec[::-1]) * np.ones((extraP + 1, Ntime))
        )
        V[:extraP + 1, :] = 0
    else:
        V[-extraP - 1:, :] = 0
        V[:extraP + 1, :] = (
            K * np.exp(-r * T_vec[::-1]) * np.ones((extraP + 1, Ntime))
            - np.exp(x[:extraP + 1]).reshape(-1, 1)
            * np.ones((extraP + 1, Ntime))
        )

    # Backward iteration
    for i in range(Ntime - 2, -1, -1):
        offset[0] = a * V[extraP, i]
        offset[-1] = c * V[-1 - extraP, i]
        V_jump = (V[extraP + 1:-extraP - 1, i + 1]
                  + dt * signal.fftconvolve(V[:, i + 1], nu[::-1],
                                             mode="valid"))
        V[extraP + 1:-extraP - 1, i] = DD.solve(V_jump - offset)

    price = np.interp(X0, x, V[:, 0])
    S_grid = np.exp(x[extraP:-extraP])
    V_curve = V[extraP:-extraP, 0]

    return {"price": price, "S_grid": S_grid, "V_curve": V_curve}


# ============================================================================
# 3. NIG MONTE CARLO (SELF-CONTAINED)
# ============================================================================

def nig_monte_carlo(S0, K, T, r, theta, sigma, kappa, payoff="call",
                    N=10_000_000, seed=42):
    """
    Monte Carlo pricing under the NIG model via Brownian subordination.

    NIG random variable: X = theta*G + sigma*sqrt(G)*Z
    where G ~ InverseGaussian(mu_s, lam) and Z ~ N(0,1).

    Parameters
    ----------
    S0, K, T, r : float        Standard option parameters.
    theta, sigma, kappa : float NIG process parameters.
    payoff : str               "call" or "put".
    N : int                    Number of simulations.
    seed : int                 Random seed.

    Returns
    -------
    dict with price and std_error.
    """
    np.random.seed(seed)
    w = (1 - np.sqrt(1 - 2 * theta * kappa - kappa * sigma**2)) / kappa
    lam = T**2 / kappa
    mu_s = T / lam

    IG = ss.invgauss.rvs(mu=mu_s, scale=lam, size=N)
    Norm = ss.norm.rvs(0, 1, N)
    X = theta * IG + sigma * np.sqrt(IG) * Norm
    S_T = S0 * np.exp((r - w) * T + X)

    if payoff == "call":
        payoffs = np.exp(-r * T) * np.maximum(S_T - K, 0)
    else:
        payoffs = np.exp(-r * T) * np.maximum(K - S_T, 0)

    return {"price": np.mean(payoffs), "std_error": ss.sem(payoffs)}


# ============================================================================
# 4. VG MONTE CARLO (SELF-CONTAINED)
# ============================================================================

def vg_monte_carlo(S0, K, T, r, theta, sigma, kappa, payoff="call",
                   N=10_000_000, seed=42):
    """
    Monte Carlo pricing under the VG model via Gamma subordination.

    VG random variable: X = theta*G + sigma*sqrt(G)*Z
    where G ~ Gamma(T/kappa, kappa) and Z ~ N(0,1).
    """
    np.random.seed(seed)
    w = -np.log(1 - theta * kappa - kappa / 2 * sigma**2) / kappa
    rho = 1 / kappa

    G = ss.gamma.rvs(rho * T, scale=1 / rho, size=N)
    Norm = ss.norm.rvs(0, 1, N)
    VG_RV = theta * G + sigma * np.sqrt(G) * Norm
    S_T = S0 * np.exp((r - w) * T + VG_RV)

    if payoff == "call":
        payoffs = np.exp(-r * T) * np.maximum(S_T - K, 0)
    else:
        payoffs = np.exp(-r * T) * np.maximum(K - S_T, 0)

    return {"price": np.mean(payoffs), "std_error": ss.sem(payoffs)}


# ============================================================================
# 5. MERTON MODEL LIMITATIONS ANALYSIS
# ============================================================================

def merton_closed_formula(S0, K, T, r, sig, lam, muJ, sigJ, payoff="call"):
    """
    Merton jump-diffusion closed-form price (series expansion).

    C = sum_{k=0}^{inf} [e^{-lam'*T} (lam'T)^k / k!] * BS(sigma_k, r_k)
    """
    price = 0
    for k in range(40):
        r_k = r - lam * (np.exp(muJ + 0.5 * sigJ**2) - 1) + k * (muJ + 0.5 * sigJ**2) / T
        sigma_k = np.sqrt(sig**2 + k * sigJ**2 / T)
        lam_prime = lam * np.exp(muJ + 0.5 * sigJ**2)

        d1 = (np.log(S0 / K) + (r_k + 0.5 * sigma_k**2) * T) / (sigma_k * np.sqrt(T))
        d2 = d1 - sigma_k * np.sqrt(T)

        if payoff == "call":
            bs_k = S0 * ss.norm.cdf(d1) - K * np.exp(-r_k * T) * ss.norm.cdf(d2)
        else:
            bs_k = K * np.exp(-r_k * T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)

        weight = np.exp(-lam_prime * T) * (lam_prime * T)**k / np.math.factorial(k)
        price += weight * bs_k

    return price


def merton_sensitivity_sigJ(S0=100, K=100, T=1, r=0.1, sig=0.2, muJ=0):
    """
    Analyse Merton model limitations: plot call price as a function of
    jump-size volatility sigJ for various jump intensities lambda.

    For large sigJ with very small lambda, the Merton model approaches
    the BS price.  For large lambda, jumps dominate and the price rises.
    """
    sigJs = np.linspace(0.01, 7, 500)
    lambdas = [0.0001, 0.001, 0.01, 0.1, 1, 10]

    # BS reference price
    d1 = (np.log(S0 / K) + (r + 0.5 * sig**2) * T) / (sig * np.sqrt(T))
    d2 = d1 - sig * np.sqrt(T)
    bs_price = S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)

    plt.figure(figsize=(12, 6))
    for lam_val in lambdas:
        prices = [merton_closed_formula(S0, K, T, r, sig, lam_val, muJ, sj)
                  for sj in sigJs]
        plt.plot(sigJs, prices, label=f"lam={lam_val}")

    plt.axhline(bs_price, color="black", ls="--", label="BS price")
    plt.xlabel("sigJ (jump-size volatility)")
    plt.ylabel("Merton call price")
    plt.title("Merton Price Sensitivity to Jump-Size Volatility")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_all():
    """Run all PIDE and Lévy process demonstrations."""
    S0, K, T, r = 100.0, 100.0, 1.0, 0.1

    # ---- 1. VG PIDE ----
    print("=" * 60)
    print("1. Variance Gamma PIDE Solver")
    print("=" * 60)

    theta_vg, sigma_vg, kappa_vg = -0.1, 0.2, 0.3

    print(f"  Parameters: theta={theta_vg}, sigma={sigma_vg}, kappa={kappa_vg}")
    print("  Solving VG PIDE (this may take a moment)...")

    vg_res = vg_pide(S0, K, T, r, theta_vg, sigma_vg, kappa_vg,
                      payoff="call", Nspace=5000, Ntime=5000)
    print(f"  VG PIDE call price: {vg_res['price']:.6f}")

    # MC comparison
    vg_mc = vg_monte_carlo(S0, K, T, r, theta_vg, sigma_vg, kappa_vg,
                            payoff="call", N=5_000_000)
    print(f"  VG MC call price:   {vg_mc['price']:.6f} "
          f"(se: {vg_mc['std_error']:.6f})")

    # Plot VG curve
    plt.figure(figsize=(10, 5))
    S = vg_res["S_grid"]
    plt.plot(S, np.maximum(S - K, 0), color="blue", label="Payoff")
    plt.plot(S, vg_res["V_curve"], color="red", label="VG PIDE price")
    plt.xlim(50, 200)
    plt.ylim(0, 100)
    plt.xlabel("S")
    plt.ylabel("Price")
    plt.legend()
    plt.title("VG Call Option: PIDE Price at t=0")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ---- 2. VG put ----
    print("\n  VG Put:")
    vg_put = vg_pide(S0, K, T, r, theta_vg, sigma_vg, kappa_vg,
                      payoff="put", Nspace=5000, Ntime=5000)
    vg_mc_put = vg_monte_carlo(S0, K, T, r, theta_vg, sigma_vg, kappa_vg,
                                payoff="put", N=5_000_000)
    print(f"  VG PIDE put price: {vg_put['price']:.6f}")
    print(f"  VG MC put price:   {vg_mc_put['price']:.6f} "
          f"(se: {vg_mc_put['std_error']:.6f})")

    # ---- 3. NIG Lévy Measure Analysis ----
    print("\n" + "=" * 60)
    print("2. NIG Lévy Measure Verification")
    print("=" * 60)

    theta_nig, sigma_nig, kappa_nig = -0.11, 0.2, 0.3
    print(f"  Parameters: theta={theta_nig}, sigma={sigma_nig}, "
          f"kappa={kappa_nig}")
    nig_verify_moments(theta_nig, sigma_nig, kappa_nig)

    # Plot NIG Lévy measure
    x_plot = np.concatenate((np.linspace(-0.1, -0.001, 200),
                              np.linspace(0.001, 0.1, 200)))
    plt.figure(figsize=(10, 5))
    plt.plot(x_plot, nig_levy_measure(x_plot, theta_nig, sigma_nig, kappa_nig))
    plt.title("NIG Lévy Measure")
    plt.xlabel("z")
    plt.ylabel("nu(z)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ---- 4. NIG PIDE ----
    print("\n" + "=" * 60)
    print("3. NIG PIDE Solver")
    print("=" * 60)

    print("  Solving NIG PIDE (this may take a moment)...")
    nig_res = nig_pide(S0, K, T, r, theta_nig, sigma_nig, kappa_nig,
                        payoff="call", Nspace=5000, Ntime=5000)
    print(f"  NIG PIDE call price: {nig_res['price']:.6f}")

    nig_mc = nig_monte_carlo(S0, K, T, r, theta_nig, sigma_nig, kappa_nig,
                              payoff="call", N=5_000_000)
    print(f"  NIG MC call price:   {nig_mc['price']:.6f} "
          f"(se: {nig_mc['std_error']:.6f})")

    # Plot NIG curve
    plt.figure(figsize=(10, 5))
    S = nig_res["S_grid"]
    plt.plot(S, np.maximum(S - K, 0), color="blue", label="Payoff")
    plt.plot(S, nig_res["V_curve"], color="red", label="NIG PIDE price")
    plt.xlim(50, 200)
    plt.ylim(0, 100)
    plt.xlabel("S")
    plt.ylabel("Price")
    plt.legend()
    plt.title("NIG Call Option: PIDE Price at t=0")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # ---- 5. Merton Sensitivity ----
    print("\n" + "=" * 60)
    print("4. Merton Model Limitations: Price Sensitivity to sigJ")
    print("=" * 60)
    merton_sensitivity_sigJ()

    # ---- 6. VG vs BS Comparison ----
    print("\n" + "=" * 60)
    print("5. VG vs BS Comparison (Same Variance, Different Skewness)")
    print("=" * 60)

    # BS reference (matched variance)
    var_vg = sigma_vg**2 + theta_vg**2 * kappa_vg
    sig_bs = np.sqrt(var_vg)
    d1 = (np.log(S0 / K) + (r + 0.5 * sig_bs**2) * T) / (sig_bs * np.sqrt(T))
    d2 = d1 - sig_bs * np.sqrt(T)
    bs_call = S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)
    print(f"  BS call (sig={sig_bs:.4f}): {bs_call:.6f}")
    print(f"  VG call (theta={theta_vg}):  {vg_res['price']:.6f}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_all()
