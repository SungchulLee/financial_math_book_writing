#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Variance Gamma (VG) Option Pricer -- Educational Version
=========================================================

Based on the VG_pricer.py, CF.py, probabilities.py, Processes.py, and FFT.py
modules from "Financial Models Numerical Methods" by cantaro86.

Original repository:
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Reference:
    Carr, Madan, Chang (1998) "The Variance Gamma Process and Option Pricing"

The Variance Gamma process is a pure-jump Levy process obtained by evaluating
a Brownian motion with drift (theta) and volatility (sigma) at a random time
given by a Gamma process with variance parameter (kappa).

    X_VG(t) = theta * G(t) + sigma * W(G(t))

where G(t) ~ Gamma(t/kappa, kappa) is the subordinator.

This file is self-contained and implements:
    1. VG characteristic function (cf_VG)
    2. Fourier inversion probabilities Q1, Q2
    3. VG probability density function (VG_pdf)
    4. FFT-based pricing via Lewis (2001) formula (fft_Lewis)
    5. Closed-form pricing (Carr-Madan-Chang 1998)
    6. Monte Carlo pricing via Gamma subordination
    7. Fourier inversion pricing
"""

import numpy as np
import scipy.stats as ss
import scipy.special as scps
from scipy.integrate import quad
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from functools import partial
import matplotlib.pyplot as plt


# ============================================================================
# Characteristic function of the Variance Gamma process
# ============================================================================

def cf_VG(u, t=1, mu=0, theta=-0.1, sigma=0.2, kappa=0.1):
    """
    Characteristic function of a Variance Gamma random variable at time t.

    Parameters
    ----------
    u : array_like
        Fourier variable.
    t : float
        Time horizon.
    mu : float
        Additional drift (typically r - w for risk-neutral pricing).
    theta : float
        Drift of the subordinated Brownian motion.
    sigma : float
        Volatility of the subordinated Brownian motion.
    kappa : float
        Variance rate of the Gamma subordinator.

    Returns
    -------
    complex ndarray
        Values of the characteristic function.

    Notes
    -----
    The VG characteristic function is:

        E[exp(i*u*X_VG(t))] = exp(i*u*mu*t) *
            (1 - i*theta*kappa*u + 0.5*kappa*sigma^2*u^2)^(-t/kappa)
    """
    return np.exp(
        t * (1j * mu * u
             - np.log(1 - 1j * theta * kappa * u
                       + 0.5 * kappa * sigma**2 * u**2) / kappa)
    )


# ============================================================================
# Fourier inversion probabilities (Gil-Pelaez style)
# ============================================================================

def Q1(k, cf, right_lim):
    """
    Probability of being in-the-money under the stock numeraire.

    Computes P(X < k) where X = log(S_T / S_0) under the stock measure.

    Parameters
    ----------
    k : float
        Log-moneyness, k = log(K / S0).
    cf : callable
        Characteristic function of log(S_T / S_0) under the risk-neutral measure.
    right_lim : float
        Upper limit of numerical integration.

    Returns
    -------
    float
        The probability Q1.
    """
    def integrand(u):
        return np.real(
            (np.exp(-u * k * 1j) / (u * 1j))
            * cf(u - 1j) / cf(-1.0000000000001j)
        )
    return 0.5 + (1.0 / np.pi) * quad(integrand, 1e-15, right_lim, limit=2000)[0]


def Q2(k, cf, right_lim):
    """
    Probability of being in-the-money under the money-market numeraire.

    Computes P(X < k) where X = log(S_T / S_0) under the risk-neutral measure.

    Parameters
    ----------
    k : float
        Log-moneyness, k = log(K / S0).
    cf : callable
        Characteristic function of log(S_T / S_0) under the risk-neutral measure.
    right_lim : float
        Upper limit of numerical integration.

    Returns
    -------
    float
        The probability Q2.
    """
    def integrand(u):
        return np.real(
            np.exp(-u * k * 1j) / (u * 1j) * cf(u)
        )
    return 0.5 + (1.0 / np.pi) * quad(integrand, 1e-15, right_lim, limit=2000)[0]


# ============================================================================
# VG probability density function
# ============================================================================

def VG_pdf(x, T, c, theta, sigma, kappa):
    """
    Variance Gamma density function.

    The VG density is expressed in terms of modified Bessel functions of the
    second kind (K_v).

    Parameters
    ----------
    x : array_like
        Points at which to evaluate the density.
    T : float
        Time horizon.
    c : float
        Drift parameter (centering constant).
    theta : float
        Brownian motion drift.
    sigma : float
        Brownian motion volatility.
    kappa : float
        Gamma variance parameter.

    Returns
    -------
    array_like
        Values of the VG density at x.
    """
    return (
        2
        * np.exp(theta * (x - c) / sigma**2)
        / (kappa ** (T / kappa) * np.sqrt(2 * np.pi) * sigma
           * scps.gamma(T / kappa))
        * ((x - c) ** 2
           / (2 * sigma**2 / kappa + theta**2)) ** (T / (2 * kappa) - 0.25)
        * scps.kv(
            T / kappa - 0.5,
            sigma ** (-2)
            * np.sqrt((x - c) ** 2 * (2 * sigma**2 / kappa + theta**2)),
        )
    )


# ============================================================================
# FFT pricing via Lewis (2001) formula
# ============================================================================

def fft_Lewis(K, S0, r, T, cf, interp="cubic"):
    """
    FFT-based option pricing using the Lewis (2001) representation.

    Uses the inverse FFT with Simpson quadrature weights to compute call
    prices for a vector of strikes simultaneously.

    Parameters
    ----------
    K : array_like
        Vector of strike prices.
    S0 : float
        Current spot price.
    r : float
        Risk-free interest rate.
    T : float
        Time to maturity.
    cf : callable
        Characteristic function of log(S_T / S_0).
    interp : str
        Interpolation method ("cubic" or "linear").

    Returns
    -------
    array_like
        Call option prices for each strike in K.
    """
    N = 2**15
    B = 500
    dx = B / N
    x = np.arange(N) * dx

    # Simpson quadrature weights
    weight = np.arange(N)
    weight = 3 + (-1) ** (weight + 1)
    weight[0] = 1
    weight[N - 1] = 1

    dk = 2 * np.pi / B
    b = N * dk / 2
    ks = -b + dk * np.arange(N)

    integrand = (
        np.exp(-1j * b * np.arange(N) * dx)
        * cf(x - 0.5j)
        * 1.0 / (x**2 + 0.25)
        * weight * dx / 3
    )
    integral_value = np.real(ifft(integrand) * N)

    if interp == "linear":
        spline = interp1d(ks, integral_value, kind="linear")
    else:
        spline = interp1d(ks, integral_value, kind="cubic")

    prices = (
        S0 - np.sqrt(S0 * K) * np.exp(-r * T) / np.pi
        * spline(np.log(S0 / K))
    )
    return prices


# ============================================================================
# Closed-form VG call price (Carr-Madan-Chang 1998)
# ============================================================================

def VG_closed_formula(S0, K, T, r, sigma, theta, kappa, payoff="call"):
    """
    Closed-form European option price under the Variance Gamma model.

    Uses the representation from Carr, Madan, Chang (1998) which expresses
    the call price via an auxiliary function Psi involving a numerical integral
    over the Gamma density.

    Parameters
    ----------
    S0 : float
        Current spot price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Risk-free interest rate.
    sigma : float
        VG volatility parameter.
    theta : float
        VG drift parameter.
    kappa : float
        VG variance parameter.
    payoff : str
        "call" or "put".

    Returns
    -------
    float
        Option price.
    """
    def Psy(a, b, g):
        """
        Auxiliary function: integral of the normal CDF weighted by the
        Gamma density.  This is Psi(a, b, gamma) from the CMC paper.
        """
        f = lambda u: (
            ss.norm.cdf(a / np.sqrt(u) + b * np.sqrt(u))
            * u ** (g - 1) * np.exp(-u) / scps.gamma(g)
        )
        result = quad(f, 0, np.inf)
        return result[0]

    # Reparametrization (see CMC 1998, Section 3)
    xi = -theta / sigma**2
    s = sigma / np.sqrt(1 + ((theta / sigma) ** 2) * (kappa / 2))
    alpha = xi * s

    c1 = kappa / 2 * (alpha + s) ** 2
    c2 = kappa / 2 * alpha**2
    d = (1 / s) * (
        np.log(S0 / K)
        + r * T
        + (T / kappa) * np.log((1 - c1) / (1 - c2))
    )

    # Call price
    call = S0 * Psy(
        d * np.sqrt((1 - c1) / kappa),
        (alpha + s) * np.sqrt(kappa / (1 - c1)),
        T / kappa,
    ) - K * np.exp(-r * T) * Psy(
        d * np.sqrt((1 - c2) / kappa),
        alpha * np.sqrt(kappa / (1 - c2)),
        T / kappa,
    )

    if payoff == "call":
        return call
    elif payoff == "put":
        return call - S0 + K * np.exp(-r * T)
    else:
        raise ValueError("payoff must be 'call' or 'put'")


# ============================================================================
# Monte Carlo pricing via Gamma subordination
# ============================================================================

def VG_monte_carlo(S0, K, T, r, sigma, theta, kappa, N=100_000,
                   payoff="call", return_stderr=False):
    """
    Monte Carlo European option pricing under the Variance Gamma model.

    Uses the Gamma subordination representation:
        X_VG(T) = theta * G(T) + sigma * sqrt(G(T)) * Z

    where G(T) ~ Gamma(T/kappa, kappa) and Z ~ N(0,1).

    Parameters
    ----------
    S0 : float
        Current spot price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Risk-free interest rate.
    sigma : float
        VG volatility parameter.
    theta : float
        VG drift parameter.
    kappa : float
        VG variance parameter.
    N : int
        Number of Monte Carlo paths.
    payoff : str
        "call" or "put".
    return_stderr : bool
        If True, also return the standard error.

    Returns
    -------
    float or tuple
        Option price, and optionally the standard error.

    Notes
    -----
    The martingale correction w ensures that E[S_T] = S0 * exp(r*T):

        w = -(1/kappa) * log(1 - theta*kappa - 0.5*kappa*sigma^2)
    """
    # Martingale correction
    w = -np.log(1 - theta * kappa - kappa / 2 * sigma**2) / kappa

    # Gamma subordinator: shape = T/kappa, scale = kappa
    rho = 1 / kappa
    G = ss.gamma(rho * T).rvs(N) / rho  # G ~ Gamma(T/kappa, kappa)

    # Standard normal draws
    Z = ss.norm.rvs(0, 1, N)

    # VG increment at time T
    VG = theta * G + sigma * np.sqrt(G) * Z

    # Terminal stock prices under risk-neutral dynamics
    S_T = S0 * np.exp((r - w) * T + VG)

    # Discounted payoffs
    if payoff == "call":
        payoffs = np.exp(-r * T) * np.maximum(S_T - K, 0)
    elif payoff == "put":
        payoffs = np.exp(-r * T) * np.maximum(K - S_T, 0)
    else:
        raise ValueError("payoff must be 'call' or 'put'")

    price = np.mean(payoffs)

    if return_stderr:
        return price, ss.sem(payoffs)
    return price


# ============================================================================
# Fourier inversion pricing
# ============================================================================

def VG_fourier_inversion(S0, K, T, r, sigma, theta, kappa, payoff="call"):
    """
    European option pricing under the Variance Gamma model via Fourier
    inversion of the characteristic function.

    Uses the decomposition:
        Call = S0 * Q1 - K * exp(-r*T) * Q2

    where Q1 and Q2 are computed by numerically inverting the VG
    characteristic function (Gil-Pelaez style).

    Parameters
    ----------
    S0 : float
        Current spot price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Risk-free interest rate.
    sigma : float
        VG volatility parameter.
    theta : float
        VG drift parameter.
    kappa : float
        VG variance parameter.
    payoff : str
        "call" or "put".

    Returns
    -------
    float
        Option price.
    """
    # Martingale correction
    w = -np.log(1 - theta * kappa - kappa / 2 * sigma**2) / kappa

    # Log-moneyness
    k = np.log(K / S0)

    # Bind the characteristic function with risk-neutral drift
    cf_VG_b = partial(
        cf_VG,
        t=T,
        mu=(r - w),
        theta=theta,
        sigma=sigma,
        kappa=kappa,
    )

    right_lim = 5000  # upper integration bound (np.inf can cause warnings)

    if payoff == "call":
        return (
            S0 * Q1(k, cf_VG_b, right_lim)
            - K * np.exp(-r * T) * Q2(k, cf_VG_b, right_lim)
        )
    elif payoff == "put":
        return (
            K * np.exp(-r * T) * (1 - Q2(k, cf_VG_b, right_lim))
            - S0 * (1 - Q1(k, cf_VG_b, right_lim))
        )
    else:
        raise ValueError("payoff must be 'call' or 'put'")


# ============================================================================
# FFT pricing (wrapper for a single strike)
# ============================================================================

def VG_fft_price(S0, K, T, r, sigma, theta, kappa, payoff="call"):
    """
    FFT-based European option pricing under the Variance Gamma model.

    Parameters
    ----------
    S0 : float
        Current spot price.
    K : float or array_like
        Strike price(s).
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    sigma, theta, kappa : float
        VG model parameters.
    payoff : str
        "call" or "put".

    Returns
    -------
    float or array_like
        Option price(s).
    """
    # Martingale correction
    w = -np.log(1 - theta * kappa - kappa / 2 * sigma**2) / kappa

    cf_VG_b = partial(
        cf_VG,
        t=T,
        mu=(r - w),
        theta=theta,
        sigma=sigma,
        kappa=kappa,
    )

    K_arr = np.atleast_1d(np.asarray(K, dtype=float))
    call_prices = fft_Lewis(K_arr, S0, r, T, cf_VG_b, interp="cubic")

    if payoff == "call":
        result = call_prices
    elif payoff == "put":
        result = call_prices - S0 + K_arr * np.exp(-r * T)
    else:
        raise ValueError("payoff must be 'call' or 'put'")

    if np.isscalar(K):
        return float(result[0])
    return result


# ============================================================================
# Main demonstration
# ============================================================================

if __name__ == "__main__":

    # ---- Model parameters ----
    S0 = 100.0       # spot price
    K = 100.0        # strike (ATM)
    T = 1.0          # maturity (1 year)
    r = 0.05         # risk-free rate

    # VG parameters
    sigma = 0.2      # BM volatility
    theta = -0.15    # BM drift (negative -> left skew)
    kappa = 0.2      # Gamma variance rate

    print("=" * 65)
    print("  Variance Gamma European Call Pricing")
    print("=" * 65)
    print(f"  S0 = {S0},  K = {K},  T = {T},  r = {r}")
    print(f"  sigma = {sigma},  theta = {theta},  kappa = {kappa}")
    print("-" * 65)

    # ---- Method 1: Closed Formula (Carr-Madan-Chang 1998) ----
    price_closed = VG_closed_formula(S0, K, T, r, sigma, theta, kappa,
                                     payoff="call")
    print(f"  Closed formula (CMC 1998):    {price_closed:.6f}")

    # ---- Method 2: Fourier Inversion ----
    price_fourier = VG_fourier_inversion(S0, K, T, r, sigma, theta, kappa,
                                         payoff="call")
    print(f"  Fourier inversion:            {price_fourier:.6f}")

    # ---- Method 3: FFT (Lewis 2001) ----
    price_fft = VG_fft_price(S0, K, T, r, sigma, theta, kappa, payoff="call")
    print(f"  FFT (Lewis):                  {price_fft:.6f}")

    # ---- Method 4: Monte Carlo (Gamma subordination) ----
    np.random.seed(42)
    N_mc = 500_000
    price_mc, se_mc = VG_monte_carlo(S0, K, T, r, sigma, theta, kappa,
                                     N=N_mc, payoff="call",
                                     return_stderr=True)
    print(f"  Monte Carlo ({N_mc:,} paths): {price_mc:.6f}  "
          f"(SE = {se_mc:.6f})")

    print("-" * 65)
    print(f"  Fourier - Closed diff:  {abs(price_fourier - price_closed):.2e}")
    print(f"  FFT     - Closed diff:  {abs(price_fft - price_closed):.2e}")
    print(f"  MC      - Closed diff:  {abs(price_mc - price_closed):.2e}")
    print("=" * 65)

    # ---- Put price via put-call parity check ----
    print()
    put_closed = VG_closed_formula(S0, K, T, r, sigma, theta, kappa,
                                   payoff="put")
    put_fourier = VG_fourier_inversion(S0, K, T, r, sigma, theta, kappa,
                                       payoff="put")
    parity_check = price_closed - put_closed - S0 + K * np.exp(-r * T)
    print(f"  Put price (closed):           {put_closed:.6f}")
    print(f"  Put price (Fourier):          {put_fourier:.6f}")
    print(f"  Put-call parity residual:     {parity_check:.2e}")

    # ==================================================================
    # Plot: VG density vs Normal density
    # ==================================================================
    print()
    print("  Generating VG density vs Normal density plot...")

    # Martingale correction for centering
    w = -np.log(1 - theta * kappa - kappa / 2 * sigma**2) / kappa
    c = r - w  # risk-neutral drift

    # VG distribution moments (for comparison)
    vg_mean = c + theta
    vg_var = sigma**2 + theta**2 * kappa

    x_grid = np.linspace(-1.5, 1.5, 1000)

    # VG density
    # The VG_pdf function uses (x, T, c, theta, sigma, kappa)
    vg_density = VG_pdf(x_grid, T, c, theta, sigma, kappa)

    # Normal density matched on first two moments
    normal_density = ss.norm.pdf(x_grid, loc=vg_mean * T,
                                 scale=np.sqrt(vg_var * T))

    fig, ax = plt.subplots(1, 1, figsize=(9, 5))
    ax.plot(x_grid, vg_density, "b-", linewidth=2, label="Variance Gamma")
    ax.plot(x_grid, normal_density, "r--", linewidth=2,
            label="Normal (matched moments)")
    ax.set_xlabel("x (log-return)", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)
    ax.set_title(
        "VG Density vs Normal Density\n"
        rf"($\sigma$={sigma}, $\theta$={theta}, $\kappa$={kappa})",
        fontsize=13,
    )
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    # Annotate the key features
    ax.annotate(
        "Heavier left tail\n(negative skew from $\\theta < 0$)",
        xy=(-1.0, 0.15), fontsize=9, color="blue",
        ha="center",
    )

    plt.tight_layout()
    plt.savefig("vg_density_vs_normal.png", dpi=150)
    plt.show()
    print("  Plot saved to vg_density_vs_normal.png")
