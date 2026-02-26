#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Normal Inverse Gaussian (NIG) Option Pricer -- Educational Version
===================================================================

Based on the NIG_pricer.py, CF.py, probabilities.py, and Processes.py modules
from "Financial Models Numerical Methods" by cantaro86.

Original repository:
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

The Normal Inverse Gaussian process is a pure-jump Levy process obtained by
evaluating a Brownian motion with drift (theta) and volatility (sigma) at a
random time given by an Inverse Gaussian subordinator with variance
parameter (kappa).

    X_NIG(t) = theta * IG(t) + sigma * W(IG(t))

where IG(t) ~ InverseGaussian(t, t^2/kappa) is the subordinator.

This file is self-contained and implements:
    1. NIG characteristic function (cf_NIG)
    2. Fourier inversion probabilities Q1, Q2
    3. NIG probability density function (NIG_pdf)
    4. Monte Carlo pricing via Inverse Gaussian subordination
    5. Fourier inversion pricing
"""

import numpy as np
import scipy.stats as ss
import scipy.special as scps
from scipy.integrate import quad
from functools import partial
import matplotlib.pyplot as plt


# ============================================================================
# Characteristic function of the Normal Inverse Gaussian process
# ============================================================================

def cf_NIG(u, t=1, mu=0, theta=-0.1, sigma=0.2, kappa=0.1):
    """
    Characteristic function of a Normal Inverse Gaussian random variable
    at time t.

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
        Variance of the Inverse Gaussian subordinator.

    Returns
    -------
    complex ndarray
        Values of the characteristic function.

    Notes
    -----
    The NIG characteristic function is:

        E[exp(i*u*X_NIG(t))] = exp(i*u*mu*t) *
            exp( (t/kappa) * (1 - sqrt(1 - 2i*theta*kappa*u + kappa*sigma^2*u^2)) )

    The condition for the cf to be well-defined requires:

        1 - 2*theta*kappa*u_imag + kappa*sigma^2*(u_real^2 - u_imag^2) >= 0

    which determines the strip of analyticity.
    """
    return np.exp(
        t * (1j * mu * u
             + 1.0 / kappa
             - np.sqrt(1 - 2j * theta * kappa * u
                        + kappa * sigma**2 * u**2) / kappa)
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
# NIG probability density function
# ============================================================================

def NIG_pdf(x, T, c, theta, sigma, kappa):
    """
    Normal Inverse Gaussian density function.

    The NIG density involves the modified Bessel function of the second kind
    K_1 (order 1), reflecting the Inverse Gaussian subordination.

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
        Inverse Gaussian variance parameter.

    Returns
    -------
    array_like
        Values of the NIG density at x.

    Notes
    -----
    Defining:
        A = theta / sigma^2
        B = sqrt(theta^2 + sigma^2/kappa) / sigma^2
        C = (T/pi) * exp(T/kappa) * sqrt(theta^2/(kappa*sigma^2) + 1/kappa^2)

    the density is:

        f(x) = C * exp(A*(x - c*T)) * K_1(B*sqrt((x-c*T)^2 + T^2*sigma^2/kappa))
                / sqrt((x - c*T)^2 + T^2*sigma^2/kappa)
    """
    A = theta / (sigma**2)
    B = np.sqrt(theta**2 + sigma**2 / kappa) / sigma**2
    C = (T / np.pi * np.exp(T / kappa)
         * np.sqrt(theta**2 / (kappa * sigma**2) + 1.0 / kappa**2))

    arg = np.sqrt((x - c * T) ** 2 + T**2 * sigma**2 / kappa)

    return C * np.exp(A * (x - c * T)) * scps.kv(1, B * arg) / arg


# ============================================================================
# Monte Carlo pricing via Inverse Gaussian subordination
# ============================================================================

def NIG_monte_carlo(S0, K, T, r, sigma, theta, kappa, N=100_000,
                    payoff="call", return_stderr=False):
    """
    Monte Carlo European option pricing under the Normal Inverse Gaussian model.

    Uses the Inverse Gaussian subordination representation:
        X_NIG(T) = theta * IG(T) + sigma * sqrt(IG(T)) * Z

    where IG(T) ~ InverseGaussian(mu_s, lam) with:
        lam  = T^2 / kappa      (shape parameter)
        mu_s = T / lam           (mean parameter, as used by scipy)

    and Z ~ N(0,1).

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
        NIG volatility parameter.
    theta : float
        NIG drift parameter.
    kappa : float
        NIG variance parameter (of the IG subordinator).
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

        w = (1 - sqrt(1 - 2*theta*kappa - kappa*sigma^2)) / kappa

    The Inverse Gaussian IG(T) has mean T and variance T*kappa.
    scipy.stats.invgauss uses the parametrization IG(mu_s, scale=lam) where
    the distribution has mean mu_s * lam = T and variance mu_s^3 * lam^2
    = T * kappa.
    """
    # Martingale correction
    w = (1 - np.sqrt(1 - 2 * theta * kappa - kappa * sigma**2)) / kappa

    # Inverse Gaussian subordinator
    lam = T**2 / kappa        # scale parameter
    mu_s = T / lam            # scipy's mu parameter (= kappa / T)

    IG = ss.invgauss.rvs(mu=mu_s, scale=lam, size=N)

    # Standard normal draws
    Z = ss.norm.rvs(0, 1, N)

    # NIG increment at time T
    X = theta * IG + sigma * np.sqrt(IG) * Z

    # Terminal stock prices under risk-neutral dynamics
    S_T = S0 * np.exp((r - w) * T + X)

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

def NIG_fourier_inversion(S0, K, T, r, sigma, theta, kappa, payoff="call"):
    """
    European option pricing under the Normal Inverse Gaussian model via
    Fourier inversion of the characteristic function.

    Uses the decomposition:
        Call = S0 * Q1 - K * exp(-r*T) * Q2

    where Q1 and Q2 are computed by numerically inverting the NIG
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
        NIG volatility parameter.
    theta : float
        NIG drift parameter.
    kappa : float
        NIG variance parameter.
    payoff : str
        "call" or "put".

    Returns
    -------
    float
        Option price.
    """
    # Martingale correction
    w = (1 - np.sqrt(1 - 2 * theta * kappa - kappa * sigma**2)) / kappa

    # Log-moneyness
    k = np.log(K / S0)

    # Bind the characteristic function with risk-neutral drift
    cf_NIG_b = partial(
        cf_NIG,
        t=T,
        mu=(r - w),
        theta=theta,
        sigma=sigma,
        kappa=kappa,
    )

    right_lim = np.inf  # NIG cf decays fast enough for infinite limits

    if payoff == "call":
        return (
            S0 * Q1(k, cf_NIG_b, right_lim)
            - K * np.exp(-r * T) * Q2(k, cf_NIG_b, right_lim)
        )
    elif payoff == "put":
        return (
            K * np.exp(-r * T) * (1 - Q2(k, cf_NIG_b, right_lim))
            - S0 * (1 - Q1(k, cf_NIG_b, right_lim))
        )
    else:
        raise ValueError("payoff must be 'call' or 'put'")


# ============================================================================
# Main demonstration
# ============================================================================

if __name__ == "__main__":

    # ---- Model parameters ----
    S0 = 100.0       # spot price
    K = 100.0        # strike (ATM)
    T = 1.0          # maturity (1 year)
    r = 0.05         # risk-free rate

    # NIG parameters
    sigma = 0.2      # BM volatility
    theta = -0.15    # BM drift (negative -> left skew)
    kappa = 0.2      # IG variance rate

    print("=" * 65)
    print("  Normal Inverse Gaussian European Call Pricing")
    print("=" * 65)
    print(f"  S0 = {S0},  K = {K},  T = {T},  r = {r}")
    print(f"  sigma = {sigma},  theta = {theta},  kappa = {kappa}")
    print("-" * 65)

    # ---- Method 1: Fourier Inversion ----
    price_fourier = NIG_fourier_inversion(S0, K, T, r, sigma, theta, kappa,
                                          payoff="call")
    print(f"  Fourier inversion:            {price_fourier:.6f}")

    # ---- Method 2: Monte Carlo (Inverse Gaussian subordination) ----
    np.random.seed(42)
    N_mc = 500_000
    price_mc, se_mc = NIG_monte_carlo(S0, K, T, r, sigma, theta, kappa,
                                      N=N_mc, payoff="call",
                                      return_stderr=True)
    print(f"  Monte Carlo ({N_mc:,} paths): {price_mc:.6f}  "
          f"(SE = {se_mc:.6f})")

    print("-" * 65)
    print(f"  MC - Fourier diff:    {abs(price_mc - price_fourier):.2e}")
    print("=" * 65)

    # ---- Put prices ----
    print()
    put_fourier = NIG_fourier_inversion(S0, K, T, r, sigma, theta, kappa,
                                        payoff="put")
    np.random.seed(42)
    put_mc, put_se = NIG_monte_carlo(S0, K, T, r, sigma, theta, kappa,
                                     N=N_mc, payoff="put",
                                     return_stderr=True)
    parity_check = price_fourier - put_fourier - S0 + K * np.exp(-r * T)
    print(f"  Put price (Fourier):          {put_fourier:.6f}")
    print(f"  Put price (MC):               {put_mc:.6f}  (SE = {put_se:.6f})")
    print(f"  Put-call parity residual:     {parity_check:.2e}")

    # ==================================================================
    # Plot: NIG density
    # ==================================================================
    print()
    print("  Generating NIG density plot...")

    # Martingale correction for centering
    w = (1 - np.sqrt(1 - 2 * theta * kappa - kappa * sigma**2)) / kappa
    c = r - w  # risk-neutral drift

    # NIG distribution moments
    nig_mean = c * T + theta * T
    nig_var = (sigma**2 + theta**2 * kappa) * T

    x_grid = np.linspace(-1.5, 1.5, 1000)

    # NIG density
    nig_density = NIG_pdf(x_grid, T, c, theta, sigma, kappa)

    # Normal density matched on first two moments for comparison
    normal_density = ss.norm.pdf(x_grid, loc=nig_mean,
                                 scale=np.sqrt(nig_var))

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left panel: linear scale
    axes[0].plot(x_grid, nig_density, "b-", linewidth=2,
                 label="NIG")
    axes[0].plot(x_grid, normal_density, "r--", linewidth=2,
                 label="Normal (matched moments)")
    axes[0].set_xlabel("x (log-return)", fontsize=12)
    axes[0].set_ylabel("Density", fontsize=12)
    axes[0].set_title(
        "NIG vs Normal Density (linear scale)\n"
        rf"($\sigma$={sigma}, $\theta$={theta}, $\kappa$={kappa})",
        fontsize=12,
    )
    axes[0].legend(fontsize=10)
    axes[0].grid(True, alpha=0.3)

    # Right panel: log scale to emphasize tail behavior
    axes[1].semilogy(x_grid, nig_density, "b-", linewidth=2,
                     label="NIG")
    axes[1].semilogy(x_grid, normal_density, "r--", linewidth=2,
                     label="Normal (matched moments)")
    axes[1].set_xlabel("x (log-return)", fontsize=12)
    axes[1].set_ylabel("Density (log scale)", fontsize=12)
    axes[1].set_title(
        "NIG vs Normal Density (log scale)\n"
        "Heavy tails clearly visible",
        fontsize=12,
    )
    axes[1].legend(fontsize=10)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim(bottom=1e-6)

    # Annotate tail behavior
    axes[1].annotate(
        "NIG heavy tail",
        xy=(-1.2, 0.003), fontsize=9, color="blue",
        arrowprops=dict(arrowstyle="->", color="blue"),
        xytext=(-0.8, 0.05),
    )

    plt.tight_layout()
    plt.savefig("nig_density.png", dpi=150)
    plt.show()
    print("  Plot saved to nig_density.png")
