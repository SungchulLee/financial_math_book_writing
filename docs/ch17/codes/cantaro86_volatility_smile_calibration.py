"""
Volatility Smile and Model Calibration
=======================================

Based on cantaro86's notebook "4.2 Volatility smile and model calibration.ipynb"
from the Financial-Models-Numerical-Methods repository:
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

This self-contained module demonstrates:
1. How Merton jump-diffusion, Variance Gamma, and Heston stochastic volatility
   models produce implied volatility smiles, while Black-Scholes produces a flat smile.
2. Fourier-based option pricing via Gil-Pelaez inversion and Lewis FFT.
3. Calibration of model parameters to synthetic market data.
4. The practical observation that the Feller condition is rarely satisfied in
   calibrated Heston models.

All implementations are self-contained with no external model library dependencies.
Only numpy, scipy, and matplotlib are required.

References:
    [1] Rebonato, R. (1999) "Volatility and Correlation", Wiley.
    [2] Gatheral, J. (2006) "The Volatility Surface: A Practitioner's Guide", Wiley.
    [3] Cui, del Bano Rollin, Germano (2017) "Full and fast calibration of the
        Heston stochastic volatility model", European J. of Operational Research.
    [4] Schoutens, W. (2004) "Levy Processes in Finance: Pricing Financial
        Derivatives", Wiley.
"""

import numpy as np
import scipy.stats as ss
import scipy.optimize as scpo
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from scipy.integrate import quad
from functools import partial
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")


# =============================================================================
# Section 1: Characteristic Functions
# =============================================================================

def cf_normal(u, t, mu, sigma):
    """
    Characteristic function of a Normal random variable X ~ N(mu*t, sigma^2*t).

    This is the characteristic function of the log-return under Black-Scholes,
    where the log-price increment over time t is normally distributed.

    Parameters
    ----------
    u : array_like
        Fourier variable.
    t : float
        Time horizon.
    mu : float
        Drift (risk-neutral: r - 0.5*sigma^2).
    sigma : float
        Diffusion coefficient.

    Returns
    -------
    complex ndarray
        phi(u) = exp(i*u*mu*t - 0.5*u^2*sigma^2*t)
    """
    return np.exp(1j * u * mu * t - 0.5 * u**2 * sigma**2 * t)


def cf_merton(u, t, mu, sig, lam, muJ, sigJ):
    """
    Characteristic function of the Merton jump-diffusion model at time t.

    The log-price follows:
        X_t = mu*t + sig*W_t + sum_{i=1}^{N_t} J_i
    where N_t ~ Poisson(lam*t) and J_i ~ N(muJ, sigJ^2).

    Parameters
    ----------
    u : array_like
        Fourier variable.
    t : float
        Time horizon.
    mu : float
        Drift of the continuous part (risk-neutral adjusted).
    sig : float
        Diffusion coefficient of the continuous part.
    lam : float
        Jump intensity (average number of jumps per year).
    muJ : float
        Mean of the jump size (in log space).
    sigJ : float
        Standard deviation of the jump size.

    Returns
    -------
    complex ndarray
    """
    return np.exp(
        t * (
            1j * u * mu
            - 0.5 * u**2 * sig**2
            + lam * (np.exp(1j * u * muJ - 0.5 * u**2 * sigJ**2) - 1)
        )
    )


def cf_VG(u, t, mu, theta, sigma, kappa):
    """
    Characteristic function of the Variance Gamma process at time t.

    The VG process is a Brownian motion with drift, time-changed by a
    Gamma process. The log-price is:
        X_t = mu*t + theta*G_t + sigma*W_{G_t}
    where G_t is a Gamma process with unit mean rate and variance rate kappa.

    Parameters
    ----------
    u : array_like
        Fourier variable.
    t : float
        Time horizon.
    mu : float
        Additional drift (risk-neutral adjusted).
    theta : float
        Drift of the Brownian motion subordinated by the Gamma process.
    sigma : float
        Volatility of the subordinated Brownian motion.
    kappa : float
        Variance rate of the Gamma time change.

    Returns
    -------
    complex ndarray
    """
    return np.exp(
        t * (
            1j * mu * u
            - np.log(1 - 1j * theta * kappa * u + 0.5 * kappa * sigma**2 * u**2) / kappa
        )
    )


def cf_heston(u, t, v0, mu, kappa, theta, sigma, rho):
    """
    Characteristic function of the Heston stochastic volatility model.

    Uses the Schoutens (2004) formulation which is numerically more stable
    than the original Heston (1993) formulation. The key difference is using
    g2 = 1/g1 and (xi - d) terms instead of (xi + d), which avoids
    exponentially growing terms.

    The Heston model:
        dS_t = mu*S_t*dt + sqrt(v_t)*S_t*dW_1
        dv_t = kappa*(theta - v_t)*dt + sigma*sqrt(v_t)*dW_2
        dW_1*dW_2 = rho*dt

    Parameters
    ----------
    u : array_like
        Fourier variable.
    t : float
        Time horizon.
    v0 : float
        Initial variance.
    mu : float
        Drift (risk-free rate under risk-neutral measure).
    kappa : float
        Mean reversion speed of variance.
    theta : float
        Long-run variance level.
    sigma : float
        Volatility of variance (vol of vol).
    rho : float
        Correlation between stock and variance Brownian motions.

    Returns
    -------
    complex ndarray

    Notes
    -----
    The Feller condition 2*kappa*theta > sigma^2 ensures that the variance
    process v_t stays strictly positive. In practice, calibrated parameters
    frequently violate this condition.
    """
    xi = kappa - sigma * rho * u * 1j
    d = np.sqrt(xi**2 + sigma**2 * (u**2 + 1j * u))
    g1 = (xi + d) / (xi - d)
    g2 = 1.0 / g1
    cf = np.exp(
        1j * u * mu * t
        + (kappa * theta) / (sigma**2) * (
            (xi - d) * t - 2 * np.log((1 - g2 * np.exp(-d * t)) / (1 - g2))
        )
        + (v0 / sigma**2) * (xi - d) * (1 - np.exp(-d * t)) / (1 - g2 * np.exp(-d * t))
    )
    return cf


# =============================================================================
# Section 2: Fourier Pricing Functions (Gil-Pelaez Inversion)
# =============================================================================

def Q1(k, cf, right_lim):
    """
    Probability of being in-the-money under the stock numeraire measure.

    Computes P(X < k) using the Gil-Pelaez inversion formula, where X is the
    log-moneyness log(K/S0) and cf is the characteristic function of the
    log-price increment.

    Parameters
    ----------
    k : float
        Log-moneyness: log(K / S0).
    cf : callable
        Characteristic function cf(u).
    right_lim : float
        Upper integration limit (use np.inf for exact, or large finite value).

    Returns
    -------
    float
        Probability under stock numeraire.
    """
    def integrand(u):
        return np.real(
            (np.exp(-u * k * 1j) / (u * 1j)) * cf(u - 1j) / cf(-1.0000000000001j)
        )
    return 0.5 + (1.0 / np.pi) * quad(integrand, 1e-15, right_lim, limit=2000)[0]


def Q2(k, cf, right_lim):
    """
    Probability of being in-the-money under the money market numeraire.

    Computes P(X < k) using the Gil-Pelaez inversion formula under the
    risk-neutral measure.

    Parameters
    ----------
    k : float
        Log-moneyness: log(K / S0).
    cf : callable
        Characteristic function cf(u).
    right_lim : float
        Upper integration limit.

    Returns
    -------
    float
        Probability under money market numeraire.
    """
    def integrand(u):
        return np.real(np.exp(-u * k * 1j) / (u * 1j) * cf(u))
    return 0.5 + (1.0 / np.pi) * quad(integrand, 1e-15, right_lim, limit=2000)[0]


def fourier_call_price(S0, K, r, T, cf):
    """
    European call price via Fourier inversion of the characteristic function.

    Uses the decomposition:
        Call = S0 * Q1 - K * exp(-rT) * Q2
    where Q1, Q2 are the in-the-money probabilities under the stock and
    money market numeraire measures respectively.

    Parameters
    ----------
    S0 : float
        Spot price.
    K : float
        Strike price.
    r : float
        Risk-free interest rate.
    T : float
        Time to maturity.
    cf : callable
        Characteristic function of the log-price increment cf(u).

    Returns
    -------
    float
        European call option price.
    """
    k = np.log(K / S0)
    call = S0 * Q1(k, cf, np.inf) - K * np.exp(-r * T) * Q2(k, cf, np.inf)
    return call


# =============================================================================
# Section 3: Lewis FFT Pricing
# =============================================================================

def fft_lewis(K_array, S0, r, T, cf, N=2**15, B=500, interp="cubic"):
    """
    Option pricing via Lewis (2001) FFT representation.

    Uses the Lewis formula:
        Call(K) = S0 - sqrt(S0*K) * exp(-rT) / pi * integral
    where the integral is evaluated using IFFT with Simpson quadrature weights
    and cubic spline interpolation.

    Parameters
    ----------
    K_array : array_like
        Array of strike prices.
    S0 : float
        Spot price.
    r : float
        Risk-free interest rate.
    T : float
        Time to maturity.
    cf : callable
        Characteristic function cf(u) of the log-price increment.
    N : int, optional
        Number of FFT grid points (should be power of 2). Default is 2^15.
    B : float, optional
        Integration upper bound. Default is 500.
    interp : str, optional
        Interpolation method: "cubic" or "linear". Default is "cubic".

    Returns
    -------
    ndarray
        Array of European call option prices corresponding to K_array.

    Notes
    -----
    The integrand involves cf(x - 0.5j) / (x^2 + 0.25) which is the Lewis
    representation. Simpson weights are applied for accuracy, and the IFFT
    provides simultaneous evaluation at all log-moneyness grid points.
    """
    K_array = np.asarray(K_array, dtype=float)
    dx = B / N
    x = np.arange(N) * dx  # integration grid [0, dx, 2*dx, ..., (N-1)*dx]

    # Simpson quadrature weights: 1, 4/3, 2/3, 4/3, 2/3, ..., 4/3, 1
    weight = 3 + (-1) ** (np.arange(N) + 1)
    weight[0] = 1
    weight[N - 1] = 1

    dk = 2 * np.pi / B
    b = N * dk / 2.0
    ks = -b + dk * np.arange(N)  # log-moneyness grid

    # Build integrand for IFFT
    integrand = (
        np.exp(-1j * b * np.arange(N) * dx)
        * cf(x - 0.5j)
        * 1.0 / (x**2 + 0.25)
        * weight * dx / 3.0
    )
    integral_value = np.real(ifft(integrand) * N)

    # Interpolate to requested strikes
    spline = interp1d(ks, integral_value, kind=interp)
    log_moneyness = np.log(S0 / K_array)
    prices = S0 - np.sqrt(S0 * K_array) * np.exp(-r * T) / np.pi * spline(log_moneyness)
    return prices


# =============================================================================
# Section 4: Black-Scholes Formula and Implied Volatility
# =============================================================================

def bs_call_price(S0, K, T, r, sigma):
    """
    Black-Scholes European call option price.

    Parameters
    ----------
    S0 : float
        Spot price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility.

    Returns
    -------
    float
        Call option price.
    """
    if sigma <= 0 or T <= 0:
        return max(S0 - K * np.exp(-r * T), 0.0)
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)


def bs_put_price(S0, K, T, r, sigma):
    """
    Black-Scholes European put option price via put-call parity.
    """
    return bs_call_price(S0, K, T, r, sigma) - S0 + K * np.exp(-r * T)


def implied_vol(price, S0, K, T, r, payoff="call"):
    """
    Extract implied volatility from an option price using Brent's method.

    Finds sigma such that BS(S0, K, T, r, sigma) = price.

    Parameters
    ----------
    price : float
        Observed option price.
    S0 : float
        Spot price.
    K : float
        Strike price.
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    payoff : str, optional
        "call" or "put". Default is "call".

    Returns
    -------
    float
        Implied volatility, or -1 if extraction fails.
    """
    bs_func = bs_call_price if payoff == "call" else bs_put_price

    # Check that the price is within no-arbitrage bounds
    intrinsic = max(S0 - K * np.exp(-r * T), 0.0) if payoff == "call" else max(K * np.exp(-r * T) - S0, 0.0)
    if price < intrinsic - 1e-10:
        return -1.0

    def obj(vol):
        return bs_func(S0, K, T, r, vol) - price

    try:
        iv = scpo.brentq(obj, 1e-12, 10.0, xtol=1e-12, maxiter=200)
        return iv
    except (ValueError, RuntimeError):
        # Fallback: minimization-based approach
        try:
            res = scpo.minimize_scalar(
                lambda vol: (bs_func(S0, K, T, r, vol) - price) ** 2,
                bounds=(1e-12, 10.0),
                method="bounded",
            )
            if res.success and res.fun < 1e-16:
                return res.x
        except Exception:
            pass
    return -1.0


# =============================================================================
# Section 5: Helper -- Build Risk-Neutral Characteristic Functions
# =============================================================================

def _build_cf_bs(r, sigma, T):
    """Build BS characteristic function with risk-neutral drift."""
    mu_rn = r - 0.5 * sigma**2
    return partial(cf_normal, t=T, mu=mu_rn, sigma=sigma)


def _build_cf_merton(r, sig, lam, muJ, sigJ, T):
    """Build Merton CF with risk-neutral drift adjustment."""
    m = lam * (np.exp(muJ + 0.5 * sigJ**2) - 1)  # compensator
    mu_rn = r - 0.5 * sig**2 - m
    return partial(cf_merton, t=T, mu=mu_rn, sig=sig, lam=lam, muJ=muJ, sigJ=sigJ)


def _build_cf_vg(r, theta, sigma, kappa, T):
    """Build VG CF with risk-neutral drift adjustment (omega)."""
    w = -np.log(1 - theta * kappa - 0.5 * kappa * sigma**2) / kappa
    mu_rn = r - w
    return partial(cf_VG, t=T, mu=mu_rn, theta=theta, sigma=sigma, kappa=kappa)


def _build_cf_heston(r, v0, kappa, theta, sigma, rho, T):
    """Build Heston CF (Schoutens formulation)."""
    return partial(cf_heston, t=T, v0=v0, mu=r, kappa=kappa, theta=theta, sigma=sigma, rho=rho)


# =============================================================================
# Section 6: Pricing Wrappers for Strike Arrays
# =============================================================================

def price_bs_strikes(strikes, S0, r, T, sigma):
    """Price European calls for an array of strikes using BS FFT."""
    cf = _build_cf_bs(r, sigma, T)
    return fft_lewis(strikes, S0, r, T, cf)


def price_merton_strikes(strikes, S0, r, T, sig, lam, muJ, sigJ):
    """Price European calls for an array of strikes using Merton FFT."""
    cf = _build_cf_merton(r, sig, lam, muJ, sigJ, T)
    return fft_lewis(strikes, S0, r, T, cf)


def price_vg_strikes(strikes, S0, r, T, theta, sigma, kappa):
    """Price European calls for an array of strikes using VG FFT."""
    cf = _build_cf_vg(r, theta, sigma, kappa, T)
    return fft_lewis(strikes, S0, r, T, cf)


def price_heston_strikes(strikes, S0, r, T, v0, kappa, theta, sigma, rho):
    """Price European calls for an array of strikes using Heston FFT."""
    cf = _build_cf_heston(r, v0, kappa, theta, sigma, rho, T)
    return fft_lewis(strikes, S0, r, T, cf)


# =============================================================================
# Main Demonstration
# =============================================================================

if __name__ == "__main__":

    # -------------------------------------------------------------------------
    # Common parameters
    # -------------------------------------------------------------------------
    S0 = 100.0
    K_atm = 100.0
    T = 1.0
    r = 0.05

    # Model parameters chosen so that processes have comparable variance
    # BS
    bs_sigma = 0.20

    # Merton jump-diffusion
    mert_sig = 0.12
    mert_lam = 0.8
    mert_muJ = -0.10
    mert_sigJ = 0.15

    # Variance Gamma
    vg_sigma = 0.12
    vg_theta = -0.14
    vg_kappa = 0.20

    # Heston stochastic volatility
    hest_v0 = 0.04
    hest_kappa = 1.5
    hest_theta = 0.04
    hest_sigma = 0.6
    hest_rho = -0.7

    strikes = np.arange(50, 151, 5, dtype=float)

    # -------------------------------------------------------------------------
    # Part A: Generate Option Prices Across Strikes
    # -------------------------------------------------------------------------
    print("=" * 72)
    print("PART A: Volatility Smile Generation")
    print("=" * 72)
    print(f"\nParameters: S0={S0}, T={T}, r={r}")
    print(f"  BS:     sigma={bs_sigma}")
    print(f"  Merton: sig={mert_sig}, lam={mert_lam}, muJ={mert_muJ}, sigJ={mert_sigJ}")
    print(f"  VG:     sigma={vg_sigma}, theta={vg_theta}, kappa={vg_kappa}")
    print(f"  Heston: v0={hest_v0}, kappa={hest_kappa}, theta={hest_theta}, "
          f"sigma={hest_sigma}, rho={hest_rho}")

    print("\nPricing options across strikes K = [50, 55, ..., 150] using Lewis FFT...")
    bs_prices = price_bs_strikes(strikes, S0, r, T, bs_sigma)
    mert_prices = price_merton_strikes(strikes, S0, r, T, mert_sig, mert_lam, mert_muJ, mert_sigJ)
    vg_prices = price_vg_strikes(strikes, S0, r, T, vg_theta, vg_sigma, vg_kappa)
    hest_prices = price_heston_strikes(strikes, S0, r, T, hest_v0, hest_kappa, hest_theta, hest_sigma, hest_rho)

    # Replace any negative prices from FFT with a tiny positive value
    for arr in [bs_prices, mert_prices, vg_prices, hest_prices]:
        arr[arr < 0] = 1e-10

    # -------------------------------------------------------------------------
    # Part B: Verify Fourier Inversion vs FFT for a Single Strike
    # -------------------------------------------------------------------------
    print("\n--- Verification: Fourier Inversion vs FFT at K=100 ---")
    cf_bs = _build_cf_bs(r, bs_sigma, T)
    cf_mert = _build_cf_merton(r, mert_sig, mert_lam, mert_muJ, mert_sigJ, T)
    cf_vg = _build_cf_vg(r, vg_theta, vg_sigma, vg_kappa, T)
    cf_hest = _build_cf_heston(r, hest_v0, hest_kappa, hest_theta, hest_sigma, hest_rho, T)

    for name, cf_func in [("BS", cf_bs), ("Merton", cf_mert), ("VG", cf_vg), ("Heston", cf_hest)]:
        fi_price = fourier_call_price(S0, K_atm, r, T, cf_func)
        fft_price = fft_lewis(np.array([K_atm]), S0, r, T, cf_func)[0]
        print(f"  {name:8s}: Fourier inversion = {fi_price:.8f},  FFT = {fft_price:.8f},  "
              f"diff = {abs(fi_price - fft_price):.2e}")

    # -------------------------------------------------------------------------
    # Part C: Extract Implied Volatilities
    # -------------------------------------------------------------------------
    print("\nExtracting implied volatilities...")
    iv_bs = np.array([implied_vol(bs_prices[i], S0, strikes[i], T, r) for i in range(len(strikes))])
    iv_mert = np.array([implied_vol(mert_prices[i], S0, strikes[i], T, r) for i in range(len(strikes))])
    iv_vg = np.array([implied_vol(vg_prices[i], S0, strikes[i], T, r) for i in range(len(strikes))])
    iv_hest = np.array([implied_vol(hest_prices[i], S0, strikes[i], T, r) for i in range(len(strikes))])

    # Report ATM implied vols
    atm_idx = np.argmin(np.abs(strikes - S0))
    print(f"\n--- ATM Implied Volatilities (K={strikes[atm_idx]:.0f}) ---")
    print(f"  BS:     {iv_bs[atm_idx]:.6f}  (input sigma = {bs_sigma})")
    print(f"  Merton: {iv_mert[atm_idx]:.6f}")
    print(f"  VG:     {iv_vg[atm_idx]:.6f}")
    print(f"  Heston: {iv_hest[atm_idx]:.6f}")

    # Report wing implied vols
    low_idx = np.argmin(np.abs(strikes - 70))
    high_idx = np.argmin(np.abs(strikes - 130))
    print(f"\n--- Wing Implied Volatilities ---")
    print(f"  {'Model':8s}  K={strikes[low_idx]:.0f} (left wing)  "
          f"K={strikes[atm_idx]:.0f} (ATM)  K={strikes[high_idx]:.0f} (right wing)")
    print(f"  {'BS':8s}  {iv_bs[low_idx]:.6f}              "
          f"{iv_bs[atm_idx]:.6f}          {iv_bs[high_idx]:.6f}")
    print(f"  {'Merton':8s}  {iv_mert[low_idx]:.6f}              "
          f"{iv_mert[atm_idx]:.6f}          {iv_mert[high_idx]:.6f}")
    print(f"  {'VG':8s}  {iv_vg[low_idx]:.6f}              "
          f"{iv_vg[atm_idx]:.6f}          {iv_vg[high_idx]:.6f}")
    print(f"  {'Heston':8s}  {iv_hest[low_idx]:.6f}              "
          f"{iv_hest[atm_idx]:.6f}          {iv_hest[high_idx]:.6f}")

    # -------------------------------------------------------------------------
    # Part D: Smile Visualization
    # -------------------------------------------------------------------------
    print("\nGenerating volatility smile plots...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))
    fig.suptitle("Volatility Smile: Why Models Matter", fontsize=14)

    # Left panel: Option prices look nearly identical
    ax1.plot(strikes, bs_prices, label="Black-Scholes", linewidth=2)
    ax1.plot(strikes, mert_prices, "--", label="Merton", linewidth=2)
    ax1.plot(strikes, vg_prices, "-.", label="Variance Gamma", linewidth=2)
    ax1.plot(strikes, hest_prices, ":", label="Heston", linewidth=2)
    ax1.set_xlim([70, 150])
    ax1.set_ylim([0, 40])
    ax1.set_xlabel("Strike K")
    ax1.set_ylabel("Call Price")
    ax1.set_title("Option Prices (nearly indistinguishable)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Right panel: Implied volatilities are dramatically different
    valid_bs = iv_bs > 0
    valid_mert = iv_mert > 0
    valid_vg = iv_vg > 0
    valid_hest = iv_hest > 0

    ax2.plot(strikes[valid_bs], iv_bs[valid_bs], label="Black-Scholes (flat)", linewidth=2)
    ax2.plot(strikes[valid_mert], iv_mert[valid_mert], "--", label="Merton", linewidth=2)
    ax2.plot(strikes[valid_vg], iv_vg[valid_vg], "-.", label="Variance Gamma", linewidth=2)
    ax2.plot(strikes[valid_hest], iv_hest[valid_hest], ":", label="Heston", linewidth=2)
    ax2.set_xlabel("Strike K")
    ax2.set_ylabel("Implied Volatility")
    ax2.set_title("Implied Volatilities (dramatically different)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("smile_comparison.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("  Saved: smile_comparison.png")

    # =========================================================================
    # Part E: Calibration to Synthetic Market Data
    # =========================================================================
    print("\n" + "=" * 72)
    print("PART E: Model Calibration to Synthetic Market Data")
    print("=" * 72)

    # Generate synthetic "market" data from Heston with KNOWN parameters
    true_v0 = 0.04
    true_kappa = 1.5
    true_theta = 0.04
    true_sigma = 0.6
    true_rho = -0.7

    calib_strikes = np.arange(70, 131, 2, dtype=float)
    market_prices = price_heston_strikes(
        calib_strikes, S0, r, T, true_v0, true_kappa, true_theta, true_sigma, true_rho
    )
    market_prices[market_prices < 0] = 1e-10

    print(f"\nSynthetic market data generated from Heston model:")
    print(f"  True parameters: v0={true_v0}, kappa={true_kappa}, theta={true_theta}, "
          f"sigma={true_sigma}, rho={true_rho}")
    print(f"  Feller condition: 2*kappa*theta = {2*true_kappa*true_theta:.4f} vs "
          f"sigma^2 = {true_sigma**2:.4f}  -->  "
          f"{'SATISFIED' if 2*true_kappa*true_theta > true_sigma**2 else 'VIOLATED'}")
    print(f"  Number of strikes: {len(calib_strikes)}")
    print(f"  Strike range: [{calib_strikes[0]:.0f}, {calib_strikes[-1]:.0f}]")

    # -----------------------------------------------------------------
    # Calibrate Merton model
    # -----------------------------------------------------------------
    print("\n--- Calibrating Merton model ---")

    def f_mert_calib(x, sig, lam, muJ, sigJ):
        return price_merton_strikes(x, S0, r, T, sig, lam, muJ, sigJ)

    try:
        mert_p0 = [0.15, 1.0, -0.05, 0.2]
        mert_bounds = ([1e-6, 1e-6, -2.0, 1e-6], [2.0, 10.0, 2.0, 2.0])
        params_mert, _ = scpo.curve_fit(
            f_mert_calib, calib_strikes, market_prices,
            p0=mert_p0, bounds=mert_bounds, maxfev=5000
        )
        mert_calib_sig, mert_calib_lam, mert_calib_muJ, mert_calib_sigJ = params_mert
        mert_calib_prices = price_merton_strikes(
            calib_strikes, S0, r, T, mert_calib_sig, mert_calib_lam, mert_calib_muJ, mert_calib_sigJ
        )
        mert_mae = np.mean(np.abs(market_prices - mert_calib_prices))
        print(f"  Calibrated: sig={mert_calib_sig:.4f}, lam={mert_calib_lam:.4f}, "
              f"muJ={mert_calib_muJ:.4f}, sigJ={mert_calib_sigJ:.4f}")
        print(f"  MAE = {mert_mae:.6f}")
    except Exception as e:
        print(f"  Merton calibration failed: {e}")
        mert_calib_prices = None
        mert_mae = np.inf

    # -----------------------------------------------------------------
    # Calibrate VG model
    # -----------------------------------------------------------------
    print("\n--- Calibrating Variance Gamma model ---")

    def f_vg_calib(x, theta, sigma, kappa):
        return price_vg_strikes(x, S0, r, T, theta, sigma, kappa)

    try:
        vg_p0 = [-0.1, 0.2, 0.3]
        vg_bounds = ([-2.0, 1e-6, 1e-6], [2.0, 3.0, 5.0])
        params_vg, _ = scpo.curve_fit(
            f_vg_calib, calib_strikes, market_prices,
            p0=vg_p0, bounds=vg_bounds, maxfev=5000
        )
        vg_calib_theta, vg_calib_sigma, vg_calib_kappa = params_vg
        vg_calib_prices = price_vg_strikes(
            calib_strikes, S0, r, T, vg_calib_theta, vg_calib_sigma, vg_calib_kappa
        )
        vg_mae = np.mean(np.abs(market_prices - vg_calib_prices))
        print(f"  Calibrated: theta={vg_calib_theta:.4f}, sigma={vg_calib_sigma:.4f}, "
              f"kappa={vg_calib_kappa:.4f}")
        print(f"  MAE = {vg_mae:.6f}")
    except Exception as e:
        print(f"  VG calibration failed: {e}")
        vg_calib_prices = None
        vg_mae = np.inf

    # -----------------------------------------------------------------
    # Calibrate Heston model (unconstrained)
    # -----------------------------------------------------------------
    print("\n--- Calibrating Heston model (unconstrained) ---")

    def f_hest_calib(x, rho, sigma, theta_h, kappa_h, v0_h):
        return price_heston_strikes(x, S0, r, T, v0_h, kappa_h, theta_h, sigma, rho)

    try:
        hest_p0 = [-0.5, 0.8, 0.05, 2.0, 0.05]
        hest_bounds = ([-0.999, 1e-6, 1e-6, 1e-6, 1e-6], [0.999, 5.0, 1.0, 20.0, 1.0])
        params_hest, _ = scpo.curve_fit(
            f_hest_calib, calib_strikes, market_prices,
            p0=hest_p0, bounds=hest_bounds, maxfev=5000, xtol=1e-6
        )
        h_rho, h_sigma, h_theta, h_kappa, h_v0 = params_hest
        hest_calib_prices = price_heston_strikes(
            calib_strikes, S0, r, T, h_v0, h_kappa, h_theta, h_sigma, h_rho
        )
        hest_mae = np.mean(np.abs(market_prices - hest_calib_prices))
        feller_val = 2 * h_kappa * h_theta - h_sigma**2
        print(f"  Calibrated: v0={h_v0:.4f}, kappa={h_kappa:.4f}, theta={h_theta:.4f}, "
              f"sigma={h_sigma:.4f}, rho={h_rho:.4f}")
        print(f"  Feller condition: 2*kappa*theta - sigma^2 = {feller_val:.4f}  -->  "
              f"{'SATISFIED' if feller_val > 0 else 'VIOLATED'}")
        print(f"  MAE = {hest_mae:.6f}")
    except Exception as e:
        print(f"  Heston unconstrained calibration failed: {e}")
        hest_calib_prices = None
        hest_mae = np.inf
        h_rho = h_sigma = h_theta = h_kappa = h_v0 = None

    # -----------------------------------------------------------------
    # Calibrate Heston model (Feller-constrained)
    # -----------------------------------------------------------------
    print("\n--- Calibrating Heston model (Feller-constrained via SLSQP) ---")

    def hest_objective(x, prices, strike_arr):
        """Least-squares objective for Heston calibration."""
        rho_c, sigma_c, theta_c, kappa_c, v0_c = x
        try:
            model_prices = price_heston_strikes(
                strike_arr, S0, r, T, v0_c, kappa_c, theta_c, sigma_c, rho_c
            )
            return np.sum((model_prices - prices) ** 2)
        except Exception:
            return 1e10

    def feller_constraint(x):
        """Feller condition: 2*kappa*theta - sigma^2 > 0."""
        _, sigma_c, theta_c, kappa_c, _ = x
        return 2 * kappa_c * theta_c - sigma_c**2 - 1e-6

    try:
        x0_feller = [-0.5, 0.4, 0.10, 3.0, 0.05]
        bounds_feller = [(-0.999, 0.999), (1e-4, 5.0), (1e-4, 2.0), (1e-4, 30.0), (1e-4, 1.0)]
        cons = {"fun": feller_constraint, "type": "ineq"}

        result_feller = scpo.minimize(
            hest_objective, x0=x0_feller,
            args=(market_prices, calib_strikes),
            method="SLSQP", bounds=bounds_feller,
            constraints=cons, tol=1e-6,
            options={"maxiter": 1000}
        )

        hf_rho, hf_sigma, hf_theta, hf_kappa, hf_v0 = result_feller.x
        hest_feller_prices = price_heston_strikes(
            calib_strikes, S0, r, T, hf_v0, hf_kappa, hf_theta, hf_sigma, hf_rho
        )
        hest_feller_mae = np.mean(np.abs(market_prices - hest_feller_prices))
        feller_val_f = 2 * hf_kappa * hf_theta - hf_sigma**2
        print(f"  Optimizer message: {result_feller.message}")
        print(f"  Calibrated: v0={hf_v0:.4f}, kappa={hf_kappa:.4f}, theta={hf_theta:.4f}, "
              f"sigma={hf_sigma:.4f}, rho={hf_rho:.4f}")
        print(f"  Feller condition: 2*kappa*theta - sigma^2 = {feller_val_f:.4f}  -->  "
              f"{'SATISFIED' if feller_val_f > 0 else 'VIOLATED'}")
        print(f"  MAE = {hest_feller_mae:.6f}")
    except Exception as e:
        print(f"  Heston Feller-constrained calibration failed: {e}")
        hest_feller_prices = None
        hest_feller_mae = np.inf

    # -------------------------------------------------------------------------
    # Calibration Summary Table
    # -------------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("CALIBRATION RESULTS SUMMARY")
    print("=" * 72)
    print(f"\n  {'Model':<30s}  {'MAE':>12s}")
    print(f"  {'-'*30}  {'-'*12}")
    print(f"  {'Merton':<30s}  {mert_mae:>12.6f}")
    print(f"  {'Variance Gamma':<30s}  {vg_mae:>12.6f}")
    if hest_mae < np.inf:
        print(f"  {'Heston (unconstrained)':<30s}  {hest_mae:>12.6f}")
    if hest_feller_mae < np.inf:
        print(f"  {'Heston (Feller-constrained)':<30s}  {hest_feller_mae:>12.6f}")

    print(f"\n  Note: The Feller condition (2*kappa*theta > sigma^2) is rarely satisfied")
    print(f"  in practice. The unconstrained Heston fit is typically better than the")
    print(f"  Feller-constrained one because the constraint limits the vol-of-vol,")
    print(f"  which controls the convexity (curvature) of the smile.")

    # -------------------------------------------------------------------------
    # Part F: Calibration Visualization
    # -------------------------------------------------------------------------
    print("\nGenerating calibration plots...")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("Model Calibration to Synthetic Heston Market Data", fontsize=14)

    # Panel 1: Price fit comparison
    ax = axes[0, 0]
    ax.plot(calib_strikes, market_prices, "ko", markersize=4, label="Market (Heston truth)", zorder=5)
    if mert_calib_prices is not None:
        ax.plot(calib_strikes, mert_calib_prices, "-", label="Merton fit", linewidth=1.5)
    if vg_calib_prices is not None:
        ax.plot(calib_strikes, vg_calib_prices, "--", label="VG fit", linewidth=1.5)
    if hest_calib_prices is not None:
        ax.plot(calib_strikes, hest_calib_prices, "-.", label="Heston (unconstr.) fit", linewidth=1.5)
    if hest_feller_prices is not None:
        ax.plot(calib_strikes, hest_feller_prices, ":", label="Heston (Feller) fit", linewidth=1.5)
    ax.set_xlabel("Strike K")
    ax.set_ylabel("Call Price")
    ax.set_title("Calibrated Model Prices vs Market")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 2: Pricing errors
    ax = axes[0, 1]
    if mert_calib_prices is not None:
        ax.plot(calib_strikes, np.abs(market_prices - mert_calib_prices), label="Merton", linewidth=1.5)
    if vg_calib_prices is not None:
        ax.plot(calib_strikes, np.abs(market_prices - vg_calib_prices), "--", label="VG", linewidth=1.5)
    if hest_calib_prices is not None:
        ax.plot(calib_strikes, np.abs(market_prices - hest_calib_prices), "-.", label="Heston (unconstr.)", linewidth=1.5)
    if hest_feller_prices is not None:
        ax.plot(calib_strikes, np.abs(market_prices - hest_feller_prices), ":", label="Heston (Feller)", linewidth=1.5)
    ax.set_xlabel("Strike K")
    ax.set_ylabel("Absolute Error")
    ax.set_title("Pricing Errors by Model")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 3: Implied volatility smile from calibrated models
    ax = axes[1, 0]
    market_iv = np.array([implied_vol(market_prices[i], S0, calib_strikes[i], T, r)
                          for i in range(len(calib_strikes))])
    valid_market = market_iv > 0
    ax.plot(calib_strikes[valid_market], market_iv[valid_market], "ko", markersize=4,
            label="Market IV", zorder=5)

    for label, cal_prices in [
        ("Merton", mert_calib_prices),
        ("VG", vg_calib_prices),
        ("Heston (unconstr.)", hest_calib_prices),
        ("Heston (Feller)", hest_feller_prices),
    ]:
        if cal_prices is not None:
            cal_iv = np.array([implied_vol(cal_prices[i], S0, calib_strikes[i], T, r)
                               for i in range(len(calib_strikes))])
            valid_cal = cal_iv > 0
            ax.plot(calib_strikes[valid_cal], cal_iv[valid_cal], label=label, linewidth=1.5)

    ax.set_xlabel("Strike K")
    ax.set_ylabel("Implied Volatility")
    ax.set_title("Calibrated Implied Volatility Smiles")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 4: ATM zoom of implied volatility
    ax = axes[1, 1]
    zoom_mask = (calib_strikes >= 85) & (calib_strikes <= 115)
    ax.plot(calib_strikes[valid_market & zoom_mask], market_iv[valid_market & zoom_mask],
            "ko", markersize=5, label="Market IV", zorder=5)

    for label, cal_prices in [
        ("Merton", mert_calib_prices),
        ("VG", vg_calib_prices),
        ("Heston (unconstr.)", hest_calib_prices),
        ("Heston (Feller)", hest_feller_prices),
    ]:
        if cal_prices is not None:
            cal_iv = np.array([implied_vol(cal_prices[i], S0, calib_strikes[i], T, r)
                               for i in range(len(calib_strikes))])
            valid_cal = cal_iv > 0
            ax.plot(calib_strikes[valid_cal & zoom_mask], cal_iv[valid_cal & zoom_mask],
                    label=label, linewidth=1.5)

    ax.axvline(S0, color="black", linewidth=0.8, linestyle="--", label="ATM")
    ax.set_xlabel("Strike K")
    ax.set_ylabel("Implied Volatility")
    ax.set_title("ATM Zoom: Implied Volatility Comparison")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("calibration_results.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("  Saved: calibration_results.png")

    # -------------------------------------------------------------------------
    # Part G: Side-by-Side Smile Comparison (Full Range)
    # -------------------------------------------------------------------------
    print("\nGenerating side-by-side smile comparison...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))
    fig.suptitle("Implied Volatility Smiles: Theoretical vs Calibrated", fontsize=14)

    # Left: theoretical smiles from Part A
    ax1.plot(strikes[valid_bs], iv_bs[valid_bs], label="BS (flat)", linewidth=2)
    ax1.plot(strikes[valid_mert], iv_mert[valid_mert], "--", label="Merton", linewidth=2)
    ax1.plot(strikes[valid_vg], iv_vg[valid_vg], "-.", label="VG", linewidth=2)
    ax1.plot(strikes[valid_hest], iv_hest[valid_hest], ":", label="Heston", linewidth=2)
    ax1.set_xlabel("Strike K")
    ax1.set_ylabel("Implied Volatility")
    ax1.set_title("Theoretical Smiles (known parameters)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Right: calibrated smiles from Part E
    ax2.plot(calib_strikes[valid_market], market_iv[valid_market], "ko", markersize=4,
             label="Market IV (truth)", zorder=5)
    for label, cal_prices, ls in [
        ("Merton (calib)", mert_calib_prices, "-"),
        ("VG (calib)", vg_calib_prices, "--"),
        ("Heston unconstr. (calib)", hest_calib_prices, "-."),
        ("Heston Feller (calib)", hest_feller_prices, ":"),
    ]:
        if cal_prices is not None:
            cal_iv = np.array([implied_vol(cal_prices[i], S0, calib_strikes[i], T, r)
                               for i in range(len(calib_strikes))])
            valid_cal = cal_iv > 0
            ax2.plot(calib_strikes[valid_cal], cal_iv[valid_cal], ls, label=label, linewidth=2)
    ax2.set_xlabel("Strike K")
    ax2.set_ylabel("Implied Volatility")
    ax2.set_title("Calibrated Smiles (fit to Heston market data)")
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("smile_side_by_side.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("  Saved: smile_side_by_side.png")

    print("\n" + "=" * 72)
    print("Done. All demonstrations complete.")
    print("=" * 72)
