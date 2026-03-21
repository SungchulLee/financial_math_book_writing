#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Characteristic Functions and Fourier Inversion for Option Pricing.

This module collects characteristic functions for common stochastic processes
used in quantitative finance, together with probability and density functions
obtained by Fourier inversion.

Characteristic functions included:
    - Normal, Gamma, Poisson (basic distributions)
    - Merton jump-diffusion
    - Variance Gamma (VG)
    - Normal Inverse Gaussian (NIG)
    - Heston stochastic volatility (original and Schoutens formulation)

Probability / density functions included:
    - Q1, Q2  -- risk-neutral probabilities via CF inversion (stock and
      money-market numeraire)
    - Gil-Pelaez PDF inversion
    - Closed-form densities for Merton, VG
    - Heston density via CF inversion

Credit:
    Original implementations by cantaro86
    Repository: https://github.com/cantaro86/Financial-Models-Numerical-Methods
    Book: "Financial Models Numerical Methods" by Ferreiro-Castilla et al.

    Adapted for the Quant Finance with Python course (Chapter 9 --
    Fourier Pricing Methods).
"""

import numpy as np
from scipy.integrate import quad
from math import factorial
import scipy.special as scps


# =============================================================================
# 1. Characteristic Functions
# =============================================================================

def cf_normal(u, mu=0.0, sig=1.0):
    """
    Characteristic function of a Normal random variable.

    phi(u) = exp(i*u*mu - 0.5*u^2*sig^2)

    Parameters
    ----------
    u : float or ndarray
        Evaluation point(s) in the transform domain.
    mu : float
        Mean of the normal distribution.
    sig : float
        Standard deviation of the normal distribution.

    Returns
    -------
    complex or ndarray of complex
        Value(s) of the characteristic function.
    """
    return np.exp(1j * u * mu - 0.5 * u**2 * sig**2)


def cf_gamma(u, a=1.0, b=2.0):
    """
    Characteristic function of a Gamma random variable.

    phi(u) = (1 - b*i*u)^(-a)

    Parameters
    ----------
    u : float or ndarray
        Evaluation point(s).
    a : float
        Shape parameter.
    b : float
        Scale parameter.

    Returns
    -------
    complex or ndarray of complex
    """
    return (1 - b * u * 1j) ** (-a)


def cf_poisson(u, lam=1.0):
    """
    Characteristic function of a Poisson random variable.

    phi(u) = exp(lam * (exp(i*u) - 1))

    Parameters
    ----------
    u : float or ndarray
        Evaluation point(s).
    lam : float
        Rate (intensity) parameter, lam > 0.

    Returns
    -------
    complex or ndarray of complex
    """
    return np.exp(lam * (np.exp(1j * u) - 1))


def cf_merton(u, t=1.0, mu=1.0, sig=2.0, lam=0.8, muJ=0.0, sigJ=0.5):
    """
    Characteristic function of a Merton jump-diffusion process at time t.

    The log-price follows:
        dX = (mu - 0.5*sig^2) dt + sig dW + J dN

    where N is a Poisson process with intensity lam and jumps J ~ N(muJ, sigJ^2).

    Parameters
    ----------
    u : float or ndarray
        Evaluation point(s).
    t : float
        Time horizon.
    mu : float
        Drift of the diffusion part.
    sig : float
        Volatility (diffusion coefficient).
    lam : float
        Jump intensity (Poisson rate).
    muJ : float
        Mean jump size.
    sigJ : float
        Standard deviation of jump size.

    Returns
    -------
    complex or ndarray of complex
    """
    return np.exp(
        t * (
            1j * u * mu
            - 0.5 * u**2 * sig**2
            + lam * (np.exp(1j * u * muJ - 0.5 * u**2 * sigJ**2) - 1)
        )
    )


def cf_VG(u, t=1.0, mu=0.0, theta=-0.1, sigma=0.2, kappa=0.1):
    """
    Characteristic function of a Variance Gamma process at time t.

    The VG process is a Brownian motion with drift, time-changed by a
    Gamma process.

    Parameters
    ----------
    u : float or ndarray
        Evaluation point(s).
    t : float
        Time horizon.
    mu : float
        Additional drift.
    theta : float
        Drift of the subordinated Brownian motion.
    sigma : float
        Volatility of the subordinated Brownian motion.
    kappa : float
        Variance rate of the Gamma subordinator.

    Returns
    -------
    complex or ndarray of complex
    """
    return np.exp(
        t * (
            1j * mu * u
            - np.log(1 - 1j * theta * kappa * u + 0.5 * kappa * sigma**2 * u**2)
            / kappa
        )
    )


def cf_NIG(u, t=1.0, mu=0.0, theta=-0.1, sigma=0.2, kappa=0.1):
    """
    Characteristic function of a Normal Inverse Gaussian process at time t.

    The NIG process is a Brownian motion with drift, time-changed by an
    Inverse Gaussian process.

    Parameters
    ----------
    u : float or ndarray
        Evaluation point(s).
    t : float
        Time horizon.
    mu : float
        Additional drift.
    theta : float
        Drift of the subordinated Brownian motion.
    sigma : float
        Volatility of the subordinated Brownian motion.
    kappa : float
        Variance of the Inverse Gaussian subordinator.

    Returns
    -------
    complex or ndarray of complex
    """
    return np.exp(
        t * (
            1j * mu * u
            + 1 / kappa
            - np.sqrt(1 - 2j * theta * kappa * u + kappa * sigma**2 * u**2) / kappa
        )
    )


def cf_Heston(u, t, v0, mu, kappa, theta, sigma, rho):
    """
    Heston (1993) characteristic function -- original formulation.

    This is the form published in Heston's seminal 1993 paper.  It can
    suffer from numerical instability for certain parameter combinations
    because the ratio g1 = (xi+d)/(xi-d) may blow up when d*t is large.

    Parameters
    ----------
    u : float or ndarray
        Evaluation point(s).
    t : float
        Time to maturity.
    v0 : float
        Initial variance.
    mu : float
        Drift (risk-free rate minus dividend yield for pricing).
    kappa : float
        Mean-reversion speed of variance.
    theta : float
        Long-run variance level.
    sigma : float
        Vol-of-vol.
    rho : float
        Correlation between asset and variance Brownian motions.

    Returns
    -------
    complex or ndarray of complex
    """
    xi = kappa - sigma * rho * u * 1j
    d = np.sqrt(xi**2 + sigma**2 * (u**2 + 1j * u))
    g1 = (xi + d) / (xi - d)

    cf = np.exp(
        1j * u * mu * t
        + (kappa * theta) / (sigma**2)
        * ((xi + d) * t - 2 * np.log((1 - g1 * np.exp(d * t)) / (1 - g1)))
        + (v0 / sigma**2)
        * (xi + d) * (1 - np.exp(d * t)) / (1 - g1 * np.exp(d * t))
    )
    return cf


def cf_Heston_good(u, t, v0, mu, kappa, theta, sigma, rho):
    """
    Heston characteristic function -- Schoutens (2004) formulation.

    This algebraically equivalent rearrangement avoids the numerical
    blow-up present in the original Heston formula by working with
    g2 = 1/g1 and using exp(-d*t) instead of exp(+d*t).

    Reference:
        Schoutens, Simons & Tistaert (2004). "A perfect calibration!
        Now what?"

    Parameters
    ----------
    u : float or ndarray
        Evaluation point(s).
    t : float
        Time to maturity.
    v0 : float
        Initial variance.
    mu : float
        Drift.
    kappa : float
        Mean-reversion speed of variance.
    theta : float
        Long-run variance level.
    sigma : float
        Vol-of-vol.
    rho : float
        Correlation between asset and variance Brownian motions.

    Returns
    -------
    complex or ndarray of complex
    """
    xi = kappa - sigma * rho * u * 1j
    d = np.sqrt(xi**2 + sigma**2 * (u**2 + 1j * u))
    g1 = (xi + d) / (xi - d)
    g2 = 1 / g1

    cf = np.exp(
        1j * u * mu * t
        + (kappa * theta) / (sigma**2)
        * ((xi - d) * t - 2 * np.log((1 - g2 * np.exp(-d * t)) / (1 - g2)))
        + (v0 / sigma**2)
        * (xi - d) * (1 - np.exp(-d * t)) / (1 - g2 * np.exp(-d * t))
    )
    return cf


# =============================================================================
# 2. Probability Functions (Fourier Inversion)
# =============================================================================

def Q1(k, cf, right_lim):
    """
    Probability under the stock numeraire: P(X < k).

    Used in the decomposition of the European call price:
        C = S0 * Q1 - K * exp(-rT) * Q2

    where Q1 is the "delta" probability computed under the stock-price
    measure (numeraire = stock).

    The inversion formula is:
        Q1 = 1/2 + 1/pi * int_0^inf Re[ e^{-iuk} phi(u-i) / (iu * phi(-i)) ] du

    Parameters
    ----------
    k : float
        Log-moneyness level (typically log(K/F) or log(K)).
    cf : callable
        Characteristic function phi(u).
    right_lim : float
        Upper limit of numerical integration (use np.inf for full integral).

    Returns
    -------
    float
        Probability Q1(k).
    """
    def integrand(u):
        return np.real(
            (np.exp(-u * k * 1j) / (u * 1j))
            * cf(u - 1j) / cf(-1.0000000000001j)
        )

    return 1 / 2 + 1 / np.pi * quad(integrand, 1e-15, right_lim, limit=2000)[0]


def Q2(k, cf, right_lim):
    """
    Probability under the money-market numeraire: P(X < k).

    Used in the decomposition of the European call price:
        C = S0 * Q1 - K * exp(-rT) * Q2

    where Q2 is the probability under the risk-neutral (money-market)
    measure.

    The inversion formula is:
        Q2 = 1/2 + 1/pi * int_0^inf Re[ e^{-iuk} phi(u) / (iu) ] du

    Parameters
    ----------
    k : float
        Log-moneyness level.
    cf : callable
        Characteristic function phi(u).
    right_lim : float
        Upper limit of numerical integration.

    Returns
    -------
    float
        Probability Q2(k).
    """
    def integrand(u):
        return np.real(np.exp(-u * k * 1j) / (u * 1j) * cf(u))

    return 1 / 2 + 1 / np.pi * quad(integrand, 1e-15, right_lim, limit=2000)[0]


def Gil_Pelaez_pdf(x, cf, right_lim):
    """
    Recover the probability density function via the Gil-Pelaez inversion formula.

    f(x) = 1/pi * int_0^inf Re[ e^{-iux} phi(u) ] du

    This is the real-line analogue of inverting the characteristic function
    to obtain the density at a single point x.

    Parameters
    ----------
    x : float
        Point at which to evaluate the density.
    cf : callable
        Characteristic function phi(u).
    right_lim : float
        Upper limit of numerical integration (use np.inf for exact result).

    Returns
    -------
    float
        Density f(x).
    """
    def integrand(u):
        return np.real(np.exp(-u * x * 1j) * cf(u))

    return 1 / np.pi * quad(integrand, 1e-15, right_lim)[0]


# =============================================================================
# 3. Closed-Form Density Functions
# =============================================================================

def Merton_pdf(x, T, mu, sig, lam, muJ, sigJ):
    """
    Merton jump-diffusion density function (series expansion).

    The density is an infinite mixture of normals weighted by Poisson
    probabilities.  The series is truncated at 20 terms.

    Parameters
    ----------
    x : float or ndarray
        Point(s) at which to evaluate the density.
    T : float
        Time horizon.
    mu : float
        Drift of the diffusion.
    sig : float
        Volatility of the diffusion.
    lam : float
        Jump intensity.
    muJ : float
        Mean jump size.
    sigJ : float
        Std deviation of jump size.

    Returns
    -------
    float or ndarray
        Density value(s).
    """
    tot = 0.0
    for k in range(20):
        tot += (
            (lam * T) ** k
            * np.exp(-((x - mu * T - k * muJ) ** 2) / (2 * (T * sig**2 + k * sigJ**2)))
            / (factorial(k) * np.sqrt(2 * np.pi * (sig**2 * T + k * sigJ**2)))
        )
    return np.exp(-lam * T) * tot


def VG_pdf(x, T, c, theta, sigma, kappa):
    """
    Variance Gamma density function (closed form via modified Bessel function).

    Parameters
    ----------
    x : float or ndarray
        Point(s) at which to evaluate the density.
    T : float
        Time horizon.
    c : float
        Centering constant (often mu*T or a convexity correction).
    theta : float
        Drift of the subordinated Brownian motion.
    sigma : float
        Volatility of the subordinated Brownian motion.
    kappa : float
        Variance rate of the Gamma time-change.

    Returns
    -------
    float or ndarray
        Density value(s).
    """
    return (
        2
        * np.exp(theta * (x - c) / sigma**2)
        / (
            kappa ** (T / kappa)
            * np.sqrt(2 * np.pi)
            * sigma
            * scps.gamma(T / kappa)
        )
        * (
            (x - c) ** 2
            / (2 * sigma**2 / kappa + theta**2)
        ) ** (T / (2 * kappa) - 1 / 4)
        * scps.kv(
            T / kappa - 1 / 2,
            sigma ** (-2)
            * np.sqrt((x - c) ** 2 * (2 * sigma**2 / kappa + theta**2)),
        )
    )


def Heston_pdf(i, t, v0, mu, theta, sigma, kappa, rho):
    """
    Heston density by Fourier inversion using Gil-Pelaez formula.

    Computes the probability density of the log-stock price under the
    Heston stochastic volatility model by inverting the characteristic
    function ``cf_Heston_good``.

    Parameters
    ----------
    i : float
        Point at which to evaluate the density.
    t : float
        Time horizon.
    v0 : float
        Initial variance.
    mu : float
        Drift of the log-stock price.
    theta : float
        Long-run variance.
    sigma : float
        Volatility of variance (vol-of-vol).
    kappa : float
        Mean-reversion speed.
    rho : float
        Correlation between stock and variance Brownian motions.

    Returns
    -------
    float
        Density value at *i*.
    """
    from functools import partial

    cf_H = partial(
        cf_Heston_good,
        t=t,
        v0=v0,
        mu=mu,
        theta=theta,
        sigma=sigma,
        kappa=kappa,
        rho=rho,
    )
    return Gil_Pelaez_pdf(i, cf_H, np.inf)


# =============================================================================
# 4. Main -- Educational Demonstrations
# =============================================================================

def main():
    """
    Demonstrate characteristic functions and Fourier inversion techniques
    for option pricing and density recovery.

    Five demonstrations:
        (a) Plot the CF of a Normal random variable (real and imaginary parts).
        (b) Recover the Normal PDF from its CF using Gil-Pelaez inversion.
        (c) Price a European call via Q1/Q2 with Black-Scholes CF.
        (d) Compare the original Heston CF vs Schoutens formulation.
        (e) Plot Variance Gamma and Merton density functions.
    """
    import matplotlib.pyplot as plt
    import scipy.stats as st
    from functools import partial

    # -----------------------------------------------------------------
    # (a) Characteristic function of a Normal RV
    # -----------------------------------------------------------------
    print("=" * 65)
    print("(a) Characteristic function of a Normal RV")
    print("=" * 65)

    mu, sig = 0.0, 1.0
    u_grid = np.linspace(-6, 6, 500)
    phi_vals = cf_normal(u_grid, mu=mu, sig=sig)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    fig.suptitle(
        r"Characteristic function of $X \sim \mathcal{N}$"
        f"({mu}, {sig}$^2$)",
        fontsize=13,
    )

    axes[0].plot(u_grid, np.real(phi_vals), "b-", linewidth=1.5)
    axes[0].set_title("Real part")
    axes[0].set_xlabel("u")
    axes[0].set_ylabel(r"Re $\varphi(u)$")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(u_grid, np.imag(phi_vals), "r-", linewidth=1.5)
    axes[1].set_title("Imaginary part")
    axes[1].set_xlabel("u")
    axes[1].set_ylabel(r"Im $\varphi(u)$")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    print("  Re[phi(u)] = exp(-u^2/2) * cos(mu*u)")
    print("  Im[phi(u)] = exp(-u^2/2) * sin(mu*u)")
    print("  For mu=0 the imaginary part is identically zero.\n")

    # -----------------------------------------------------------------
    # (b) Recover Normal PDF from its CF via Gil-Pelaez
    # -----------------------------------------------------------------
    print("=" * 65)
    print("(b) Gil-Pelaez inversion: recover Normal PDF from CF")
    print("=" * 65)

    mu_b, sig_b = 2.0, 0.8
    cf_b = partial(cf_normal, mu=mu_b, sig=sig_b)

    x_grid = np.linspace(mu_b - 4 * sig_b, mu_b + 4 * sig_b, 120)
    pdf_exact = st.norm.pdf(x_grid, mu_b, sig_b)

    # Vectorize Gil-Pelaez (it operates on scalars because of quad)
    pdf_recovered = np.array([Gil_Pelaez_pdf(xi, cf_b, right_lim=50) for xi in x_grid])

    max_err = np.max(np.abs(pdf_exact - pdf_recovered))
    print(f"  Parameters: mu={mu_b}, sigma={sig_b}")
    print(f"  Max |exact - recovered|  = {max_err:.2e}\n")

    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.plot(x_grid, pdf_exact, "k-", linewidth=2, label="scipy norm.pdf")
    ax2.plot(x_grid, pdf_recovered, "r--", linewidth=1.5, label="Gil-Pelaez inversion")
    ax2.set_xlabel("x")
    ax2.set_ylabel("f(x)")
    ax2.set_title(
        f"Normal PDF recovery via Gil-Pelaez  "
        r"($\mu$=" + f"{mu_b}, " + r"$\sigma$=" + f"{sig_b})"
    )
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()

    # -----------------------------------------------------------------
    # (c) European call price via Q1 / Q2 (Black-Scholes CF)
    # -----------------------------------------------------------------
    print("=" * 65)
    print("(c) European call pricing via Q1 / Q2")
    print("=" * 65)

    S0 = 100.0      # spot price
    K = 105.0        # strike
    r = 0.05         # risk-free rate
    T = 1.0          # maturity
    sigma_bs = 0.2   # Black-Scholes volatility

    # CF of log(S_T) under risk-neutral measure for GBM
    #   log S_T = log S0 + (r - 0.5*sigma^2)*T + sigma*sqrt(T)*Z
    # so phi_{log S_T}(u) = exp(iu*(log S0 + (r-0.5*sig^2)*T) - 0.5*sig^2*T*u^2)
    def cf_bs(u):
        drift = np.log(S0) + (r - 0.5 * sigma_bs**2) * T
        return np.exp(1j * u * drift - 0.5 * sigma_bs**2 * T * u**2)

    k = np.log(K)  # log-strike
    q1 = Q1(k, cf_bs, right_lim=500)
    q2 = Q2(k, cf_bs, right_lim=500)

    call_fourier = S0 * q1 - K * np.exp(-r * T) * q2

    # Black-Scholes analytical price for comparison
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma_bs**2) * T) / (sigma_bs * np.sqrt(T))
    d2 = d1 - sigma_bs * np.sqrt(T)
    call_bs = S0 * st.norm.cdf(d1) - K * np.exp(-r * T) * st.norm.cdf(d2)

    print(f"  S0={S0}, K={K}, r={r}, T={T}, sigma={sigma_bs}")
    print(f"  Q1 (stock numeraire)       = {q1:.8f}")
    print(f"  Q2 (money-market numeraire) = {q2:.8f}")
    print(f"  Call (Fourier Q1/Q2)       = {call_fourier:.6f}")
    print(f"  Call (Black-Scholes)       = {call_bs:.6f}")
    print(f"  Absolute error             = {abs(call_fourier - call_bs):.2e}\n")

    # -----------------------------------------------------------------
    # (d) Heston CF: original vs Schoutens (good) formulation
    # -----------------------------------------------------------------
    print("=" * 65)
    print("(d) Heston CF: original vs Schoutens formulation")
    print("=" * 65)

    # Heston parameters
    v0_h = 0.04       # initial variance
    mu_h = 0.05       # drift
    kappa_h = 1.5     # mean-reversion speed
    theta_h = 0.04    # long-run variance
    sigma_h = 0.3     # vol-of-vol
    rho_h = -0.7      # correlation
    T_h = 1.0         # maturity

    u_heston = np.linspace(0.01, 50, 400)

    phi_original = np.array([
        cf_Heston(ui, T_h, v0_h, mu_h, kappa_h, theta_h, sigma_h, rho_h)
        for ui in u_heston
    ])
    phi_good = np.array([
        cf_Heston_good(ui, T_h, v0_h, mu_h, kappa_h, theta_h, sigma_h, rho_h)
        for ui in u_heston
    ])

    fig3, axes3 = plt.subplots(1, 2, figsize=(12, 4))
    fig3.suptitle("Heston CF: Original (1993) vs Schoutens (2004)", fontsize=13)

    axes3[0].plot(u_heston, np.real(phi_original), "b-", label="Original", alpha=0.8)
    axes3[0].plot(u_heston, np.real(phi_good), "r--", label="Schoutens", alpha=0.8)
    axes3[0].set_title("Real part")
    axes3[0].set_xlabel("u")
    axes3[0].legend()
    axes3[0].grid(True, alpha=0.3)

    axes3[1].plot(u_heston, np.imag(phi_original), "b-", label="Original", alpha=0.8)
    axes3[1].plot(u_heston, np.imag(phi_good), "r--", label="Schoutens", alpha=0.8)
    axes3[1].set_title("Imaginary part")
    axes3[1].set_xlabel("u")
    axes3[1].legend()
    axes3[1].grid(True, alpha=0.3)

    plt.tight_layout()

    max_diff_re = np.max(np.abs(np.real(phi_original) - np.real(phi_good)))
    max_diff_im = np.max(np.abs(np.imag(phi_original) - np.imag(phi_good)))
    print(f"  Parameters: v0={v0_h}, kappa={kappa_h}, theta={theta_h}, "
          f"sigma={sigma_h}, rho={rho_h}")
    print(f"  Max |Re(original) - Re(Schoutens)| = {max_diff_re:.2e}")
    print(f"  Max |Im(original) - Im(Schoutens)| = {max_diff_im:.2e}")
    print("  Both formulations are algebraically equivalent.")
    print("  Schoutens form is numerically more stable for large u*t.\n")

    # -----------------------------------------------------------------
    # (e) Variance Gamma and Merton density functions
    # -----------------------------------------------------------------
    print("=" * 65)
    print("(e) Variance Gamma and Merton density functions")
    print("=" * 65)

    T_e = 1.0

    # -- Variance Gamma --
    theta_vg = -0.1
    sigma_vg = 0.2
    kappa_vg = 0.1
    c_vg = 0.0  # centering

    x_vg = np.linspace(-1.5, 1.0, 300)
    # Protect against x == c (Bessel singularity)
    x_vg = x_vg[np.abs(x_vg - c_vg) > 1e-10]
    pdf_vg = VG_pdf(x_vg, T_e, c_vg, theta_vg, sigma_vg, kappa_vg)

    # -- Merton --
    mu_m = -0.1
    sig_m = 0.15
    lam_m = 0.8
    muJ_m = -0.05
    sigJ_m = 0.1

    x_m = np.linspace(-1.5, 1.0, 300)
    pdf_m = Merton_pdf(x_m, T_e, mu_m, sig_m, lam_m, muJ_m, sigJ_m)

    fig4, axes4 = plt.subplots(1, 2, figsize=(12, 4))

    axes4[0].plot(x_vg, pdf_vg, "b-", linewidth=1.5)
    axes4[0].set_title(
        f"Variance Gamma PDF\n"
        r"$\theta$=" + f"{theta_vg}, "
        r"$\sigma$=" + f"{sigma_vg}, "
        r"$\kappa$=" + f"{kappa_vg}",
        fontsize=11,
    )
    axes4[0].set_xlabel("x")
    axes4[0].set_ylabel("f(x)")
    axes4[0].grid(True, alpha=0.3)

    axes4[1].plot(x_m, pdf_m, "r-", linewidth=1.5)
    axes4[1].set_title(
        f"Merton Jump-Diffusion PDF\n"
        r"$\mu$=" + f"{mu_m}, "
        r"$\sigma$=" + f"{sig_m}, "
        r"$\lambda$=" + f"{lam_m}",
        fontsize=11,
    )
    axes4[1].set_xlabel("x")
    axes4[1].set_ylabel("f(x)")
    axes4[1].grid(True, alpha=0.3)

    plt.tight_layout()

    print(f"  VG params:     theta={theta_vg}, sigma={sigma_vg}, kappa={kappa_vg}")
    print(f"  Merton params: mu={mu_m}, sig={sig_m}, lam={lam_m}, "
          f"muJ={muJ_m}, sigJ={sigJ_m}")
    print("  Plots displayed.\n")

    # -----------------------------------------------------------------
    # Show all figures
    # -----------------------------------------------------------------
    print("=" * 65)
    print("All demonstrations complete. Close plot windows to exit.")
    print("=" * 65)
    plt.show()


if __name__ == "__main__":
    main()
