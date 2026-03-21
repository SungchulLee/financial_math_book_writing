#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_fourier_inversion_demo.py
Fourier Transform Methods for Option Pricing -- Educational Demo

Credits
-------
Based on notebook "1.3 Fourier transform methods" from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 9 -- Fourier Pricing Methods).

Topics covered
--------------
1. Characteristic functions of Normal, Gamma, and Poisson distributions.
2. Gil-Pelaez Fourier inversion formula for density recovery.
3. Density recovery demos for Normal, Gamma, and Poisson.
4. Option pricing via Fourier inversion (Q1, Q2 decomposition):
   - GBM (Black-Scholes), Merton jump-diffusion, Variance Gamma.
5. Lewis integration method for European call options.
6. FFT-Lewis method for pricing across multiple strikes.
7. Warning about oscillatory integrals and short-maturity issues.
"""

import numpy as np
import scipy.stats as ss
from scipy.integrate import quad
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from functools import partial
import matplotlib.pyplot as plt


# ============================================================================
# 1. CHARACTERISTIC FUNCTIONS
# ============================================================================

def cf_normal(u, mu=1, sig=2):
    """Characteristic function of N(mu, sig^2)."""
    return np.exp(1j * u * mu - 0.5 * u**2 * sig**2)


def cf_gamma(u, a=1, b=2):
    """Characteristic function of Gamma(shape=a, scale=b)."""
    return (1 - b * u * 1j) ** (-a)


def cf_poisson(u, lam=1):
    """Characteristic function of Poisson(lambda)."""
    return np.exp(lam * (np.exp(1j * u) - 1))


def cf_merton(u, t=1, mu=1, sig=2, lam=0.8, muJ=0, sigJ=0.5):
    """
    Characteristic function of the Merton jump-diffusion log-return at time t.

    X_t = mu*t + sig*W_t + sum_{i=1}^{N_t} Y_i
    where N_t ~ Poisson(lam*t) and Y_i ~ N(muJ, sigJ^2).
    """
    return np.exp(
        t * (1j * u * mu - 0.5 * u**2 * sig**2
             + lam * (np.exp(1j * u * muJ - 0.5 * u**2 * sigJ**2) - 1))
    )


def cf_VG(u, t=1, mu=0, theta=-0.1, sigma=0.2, kappa=0.1):
    """
    Characteristic function of the Variance Gamma log-return at time t,
    with an additional drift mu.

    phi(u) = exp(i*mu*u*t) * (1 - i*theta*kappa*u + 0.5*kappa*sigma^2*u^2)^(-t/kappa)
    """
    return np.exp(
        t * (1j * mu * u
             - np.log(1 - 1j * theta * kappa * u
                       + 0.5 * kappa * sigma**2 * u**2) / kappa)
    )


# ============================================================================
# 2. GIL-PELAEZ FOURIER INVERSION
# ============================================================================

def Gil_Pelaez_pdf(x, cf, right_lim):
    """
    Recover the probability density f(x) from a characteristic function
    using the Gil-Pelaez formula:

        f(x) = (1/pi) * integral_0^{right_lim} Re[e^{-iux} phi(u)] du

    Parameters
    ----------
    x : float       Evaluation point.
    cf : callable   Characteristic function phi(u).
    right_lim : float  Right limit of integration (np.inf for exact).
    """
    integrand = lambda u: np.real(np.exp(-u * x * 1j) * cf(u))
    return 1 / np.pi * quad(integrand, 1e-15, right_lim)[0]


# ============================================================================
# 3. DENSITY RECOVERY DEMOS
# ============================================================================

def demo_normal_inversion():
    """Recover the Normal density from its characteristic function."""
    x = np.linspace(-8, 10, 100)
    pdf_exact = ss.norm.pdf(x, loc=1, scale=2)
    pdf_inv = [Gil_Pelaez_pdf(xi, cf_normal, np.inf) for xi in x]

    plt.figure(figsize=(8, 5))
    plt.plot(x, pdf_exact, label="Exact Normal PDF")
    plt.plot(x, pdf_inv, "--", label="Gil-Pelaez inversion")
    plt.title("Normal: PDF vs Gil-Pelaez Inversion")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def demo_gamma_inversion():
    """
    Recover the Gamma density from its characteristic function.
    Shows integration limits matter for oscillatory integrands.
    """
    xx = np.linspace(0.1, 20, 100)

    # Case 1: shape=1, scale=2 (requires finite integration limit)
    cf_ab = partial(cf_gamma, a=1, b=2)
    # Case 2: shape=9, scale=0.5 (well-behaved, can use inf)
    cf_cd = partial(cf_gamma, a=9, b=0.5)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    ax1.plot(xx, ss.gamma.pdf(xx, 1, scale=2), label="Exact Gamma PDF")
    ax1.plot(xx, [Gil_Pelaez_pdf(i, cf_ab, 24) for i in xx],
             "--", label="Gil-Pelaez (limit=24)")
    ax1.set_title("Gamma(shape=1, scale=2)")
    ax1.legend()

    ax2.plot(xx, ss.gamma.pdf(xx, 9, scale=0.5), label="Exact Gamma PDF")
    ax2.plot(xx, [Gil_Pelaez_pdf(i, cf_cd, np.inf) for i in xx],
             "--", label="Gil-Pelaez (limit=inf)")
    ax2.set_title("Gamma(shape=9, scale=0.5)")
    ax2.legend()

    plt.suptitle("Gamma Density Recovery via Fourier Inversion")
    plt.tight_layout()
    plt.show()


def demo_poisson_inversion():
    """
    Recover the Poisson PMF from its characteristic function.
    Note: integration domain is [0, pi] due to periodicity.
    """
    k = np.arange(20)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # lambda = 1
    ax1.plot(k, ss.poisson.pmf(k, 1), "p", label="Exact PMF")
    ax1.plot(k, [Gil_Pelaez_pdf(i, cf_poisson, np.pi) for i in k],
             "*", label="Gil-Pelaez")
    ax1.set_title("Poisson(lambda=1)")
    ax1.set_xlabel("k")
    ax1.legend()

    # lambda = 4
    cf_p4 = partial(cf_poisson, lam=4)
    ax2.plot(k, ss.poisson.pmf(k, 4), "p", label="Exact PMF")
    ax2.plot(k, [Gil_Pelaez_pdf(i, cf_p4, np.pi) for i in k],
             "*", label="Gil-Pelaez")
    ax2.set_title("Poisson(lambda=4)")
    ax2.set_xlabel("k")
    ax2.legend()

    plt.suptitle("Poisson PMF Recovery via Fourier Inversion")
    plt.tight_layout()
    plt.show()


# ============================================================================
# 4. OPTION PRICING VIA FOURIER INVERSION
# ============================================================================

def Q1(k, cf, right_lim):
    """
    Risk-neutral probability under the stock numeraire:
        Q_tilde(S_T > K) = 0.5 + (1/pi) * integral Re[...] du

    Uses the change of measure: phi_tilde(u) = phi(u-i) / phi(-i).

    Parameters
    ----------
    k : float       Log-moneyness: log(K/S0).
    cf : callable   Characteristic function of the log-return.
    right_lim : float  Right integration limit.
    """
    integrand = lambda u: np.real(
        (np.exp(-u * k * 1j) / (u * 1j)) * cf(u - 1j) / cf(-1j)
    )
    return 0.5 + 1 / np.pi * quad(integrand, 1e-15, right_lim, limit=1000)[0]


def Q2(k, cf, right_lim):
    """
    Risk-neutral probability under the money-market numeraire:
        Q(S_T > K) = 0.5 + (1/pi) * integral Re[e^{-iuk} phi(u) / (iu)] du
    """
    integrand = lambda u: np.real(
        np.exp(-u * k * 1j) / (u * 1j) * cf(u)
    )
    return 0.5 + 1 / np.pi * quad(integrand, 1e-15, right_lim, limit=1000)[0]


def call_price_fourier(S0, K, r, T, cf, right_lim=np.inf):
    """
    European call price via Fourier inversion:
        C = S0 * Q1 - K * e^{-rT} * Q2

    Parameters
    ----------
    cf : callable  Characteristic function of the log-return X_T = log(S_T/S0).
    """
    k = np.log(K / S0)
    return S0 * Q1(k, cf, right_lim) - K * np.exp(-r * T) * Q2(k, cf, right_lim)


# ============================================================================
# 5. LEWIS METHOD
# ============================================================================

def Lewis_call(S0, K, r, T, cf):
    """
    European call price via the Lewis (2001) integration formula:

    C = S0 - sqrt(S0*K)*e^{-rT}/pi * integral_0^inf
        Re[e^{iuk} phi(u - i/2)] / (u^2 + 1/4) du

    where k = log(S0/K).
    """
    k = np.log(S0 / K)
    integrand = lambda u: (np.real(np.exp(u * k * 1j) * cf(u - 0.5j))
                           / (u**2 + 0.25))
    int_value = quad(integrand, 0, 2000, limit=1000)[0]
    return S0 - np.sqrt(S0 * K) * np.exp(-r * T) / np.pi * int_value


# ============================================================================
# 6. FFT-LEWIS METHOD
# ============================================================================

def fft_Lewis(K_vec, S0, r, T, cf, interp="cubic"):
    """
    Price European calls across a vector of strikes using the FFT-Lewis
    method with Simpson quadrature.

    Parameters
    ----------
    K_vec : array   Vector of strikes.
    S0 : float      Spot price.
    r : float       Risk-free rate.
    T : float       Maturity.
    cf : callable   Characteristic function of the log-return.
    interp : str    Interpolation method ("cubic" or "linear").

    Returns
    -------
    ndarray  Call prices corresponding to K_vec.
    """
    N = 2**12  # FFT size (power of 2 for efficiency)
    B = 200    # integration limit
    dx = B / N
    x = np.arange(N) * dx

    # Simpson weights
    weight = np.arange(N)
    weight = 3 + (-1) ** (weight + 1)
    weight[0] = 1
    weight[N - 1] = 1

    dk = 2 * np.pi / B
    b = N * dk / 2
    ks = -b + dk * np.arange(N)

    integrand = (np.exp(-1j * b * np.arange(N) * dx)
                 * cf(x - 0.5j) / (x**2 + 0.25)
                 * weight * dx / 3)
    integral_value = np.real(ifft(integrand) * N)

    if interp == "linear":
        spline = interp1d(ks, integral_value, kind="linear")
    else:
        spline = interp1d(ks, integral_value, kind="cubic")

    prices = (S0 - np.sqrt(S0 * K_vec) * np.exp(-r * T) / np.pi
              * spline(np.log(S0 / K_vec)))
    return prices


# ============================================================================
# 7. BS CLOSED FORMULA (for comparison)
# ============================================================================

def bs_call(S0, K, T, r, sigma):
    """Black-Scholes call price (for benchmarking)."""
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)


# ============================================================================
# COMPREHENSIVE DEMO
# ============================================================================

def demo_density_recovery():
    """Run all density recovery demonstrations."""
    print("=" * 60)
    print("Density Recovery via Fourier Inversion")
    print("=" * 60)

    demo_normal_inversion()
    demo_gamma_inversion()
    demo_poisson_inversion()


def demo_option_pricing():
    """
    Compare Fourier inversion, Lewis method, and FFT-Lewis method for
    pricing European calls under GBM, Merton, and VG models.
    """
    print("\n" + "=" * 60)
    print("Option Pricing via Fourier Methods")
    print("=" * 60)

    S0, K, T, r = 100.0, 100.0, 1.0, 0.1
    sig = 0.2

    # --- GBM (Black-Scholes) ---
    print("\n--- GBM (Black-Scholes) ---")
    cf_GBM = partial(cf_normal, mu=(r - 0.5 * sig**2) * T,
                     sig=sig * np.sqrt(T))

    price_fourier = call_price_fourier(S0, K, r, T, cf_GBM)
    price_lewis = Lewis_call(S0, K, r, T, cf_GBM)
    price_bs = bs_call(S0, K, T, r, sig)

    print(f"  Fourier inversion: {price_fourier:.6f}")
    print(f"  Lewis method:      {price_lewis:.6f}")
    print(f"  BS closed formula: {price_bs:.6f}")

    # --- Merton ---
    print("\n--- Merton Jump-Diffusion ---")
    lam, muJ, sigJ = 0.8, 0.0, 0.5
    m = lam * (np.exp(muJ + sigJ**2 / 2) - 1)  # martingale correction
    cf_Mert = partial(cf_merton, t=T, mu=(r - 0.5 * sig**2 - m),
                      sig=sig, lam=lam, muJ=muJ, sigJ=sigJ)

    price_fourier_m = call_price_fourier(S0, K, r, T, cf_Mert)
    price_lewis_m = Lewis_call(S0, K, r, T, cf_Mert)

    print(f"  Fourier inversion: {price_fourier_m:.6f}")
    print(f"  Lewis method:      {price_lewis_m:.6f}")

    # --- Variance Gamma ---
    print("\n--- Variance Gamma ---")
    theta_vg, sigma_vg, kappa_vg = -0.1, 0.2, 0.1
    w = -np.log(1 - theta_vg * kappa_vg
                - kappa_vg / 2 * sigma_vg**2) / kappa_vg
    cf_VG_b = partial(cf_VG, t=T, mu=r - w, theta=theta_vg,
                      sigma=sigma_vg, kappa=kappa_vg)

    price_fourier_vg = call_price_fourier(S0, K, r, T, cf_VG_b)
    price_lewis_vg = Lewis_call(S0, K, r, T, cf_VG_b)

    print(f"  Fourier inversion: {price_fourier_vg:.6f}")
    print(f"  Lewis method:      {price_lewis_vg:.6f}")

    # --- FFT across strikes ---
    print("\n--- FFT-Lewis across strikes ---")
    KK = np.arange(60, 141, 10, dtype=float)
    bs_prices = np.array([bs_call(S0, k, T, r, sig) for k in KK])
    fft_prices = fft_Lewis(KK, S0, r, T, cf_GBM)
    error = np.linalg.norm(fft_prices - bs_prices, 1)
    print(f"  BS model, L1 error (cubic interp): {error:.2e}")

    fft_prices_m = fft_Lewis(KK, S0, r, T, cf_Mert)
    fft_prices_vg = fft_Lewis(KK, S0, r, T, cf_VG_b)

    plt.figure(figsize=(10, 6))
    plt.plot(KK, fft_prices, "o-", label="GBM (BS)")
    plt.plot(KK, fft_prices_m, "s-", label="Merton")
    plt.plot(KK, fft_prices_vg, "^-", label="Variance Gamma")
    plt.xlabel("Strike K")
    plt.ylabel("Call Price")
    plt.title("FFT-Lewis Option Prices Across Strikes")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def demo_short_maturity_warning():
    """
    Demonstrate that naive Fourier inversion can fail for
    short-maturity OTM options due to highly oscillatory integrands.
    """
    print("\n--- Short-Maturity Warning ---")
    S0, r, sig = 100.0, 0.1, 0.2
    T_short = 0.01

    cf_short = partial(cf_normal, mu=(r - 0.5 * sig**2) * T_short,
                       sig=sig * np.sqrt(T_short))

    for K_test in [105.0, 120.0]:
        k = np.log(K_test / S0)
        price_f = call_price_fourier(S0, K_test, r, T_short, cf_short)
        price_bs = bs_call(S0, K_test, T_short, r, sig)
        print(f"  K={K_test}: Fourier={price_f:.6f}, BS={price_bs:.6f}, "
              f"error={abs(price_f - price_bs):.2e}")

    # Plot integrands to show the oscillation problem
    u = np.linspace(1e-15, 100, 200)
    k1 = np.log(105 / S0)
    k2 = np.log(120 / S0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    ax1.plot(u, np.real((np.exp(-u * k1 * 1j) / (u * 1j))
                        * cf_short(u - 1j) / cf_short(-1j)))
    ax1.set_title(f"Integrand of Q1, K=105 (k={k1:.2f})")

    ax2.plot(u, np.real((np.exp(-u * k2 * 1j) / (u * 1j))
                        * cf_short(u - 1j) / cf_short(-1j)))
    ax2.set_title(f"Integrand of Q1, K=120 (k={k2:.2f})")

    plt.suptitle("Oscillatory Integrands for Short-Maturity OTM Options")
    plt.tight_layout()
    plt.show()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    demo_density_recovery()
    demo_option_pricing()
    demo_short_maturity_warning()
