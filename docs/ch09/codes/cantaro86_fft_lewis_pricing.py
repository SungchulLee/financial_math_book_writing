# -*- coding: utf-8 -*-
"""
FFT-based option pricing via the Lewis (2001) integration formula.

This module implements two core routines for Fourier-based option pricing:

  1. fft_Lewis   -- Price European calls across a vector of strikes using
                    the Fast Fourier Transform with Simpson quadrature weights.
  2. IV_from_Lewis -- Extract the Black-Scholes implied volatility from the
                      Lewis formula by numerically inverting the integral.

The demo section prices European calls under geometric Brownian motion,
compares the FFT prices against the closed-form Black-Scholes formula,
extracts implied volatilities, and visualises the results.

Reference:
    cantaro86, "Financial Models Numerical Methods" (FMNM).
    https://github.com/cantaro86/Financial-Models-Numerical-Methods
    Original source: src/FMNM/FFT.py
    Licensed under GNU Affero General Public License v3 (AGPL-3.0).

Theory:
    Lewis, A. L. (2001). A Simple Option Formula for General Jump-Diffusion
    and Other Exponential Levy Processes. Available at SSRN.

    The Lewis formula expresses a European call price as:

        C(K) = S0 - sqrt(S0 * K) * exp(-r * T) / pi
               * integral_0^inf  Re[ exp(-i*k*u) * cf(u - i/2)
                                      / (u^2 + 1/4) ] du

    where k = ln(S0/K) and cf is the characteristic function of the
    log-price under the risk-neutral measure.

    The integral is evaluated on a uniform grid via Simpson's composite
    rule, then computed efficiently with the Inverse FFT, and finally
    the prices at the desired strikes are obtained by interpolation.
"""

import numpy as np
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from scipy.integrate import quad
from scipy.optimize import fsolve
import scipy.stats as st
import matplotlib.pyplot as plt
import time


# =============================================================================
# 1. Characteristic Function (Black-Scholes / Normal)
# =============================================================================

def cf_normal(u, S0, r, T, sigma):
    """
    Characteristic function of log(S_T) under Black-Scholes (GBM).

    Under the risk-neutral measure the log-price satisfies:

        ln(S_T) = ln(S0) + (r - sigma^2/2)*T + sigma*sqrt(T)*Z

    so its characteristic function is:

        E[exp(i*u*ln(S_T))] = exp(i*u*[ln(S0) + (r - sigma^2/2)*T]
                                   - 0.5*sigma^2*T*u^2)

    For the Lewis formula we need cf as a function of the *centred*
    log-return (without the ln(S0) shift), so we define:

        phi(u) = exp(i*u*(r - sigma^2/2)*T - 0.5*sigma^2*T*u^2)

    Parameters
    ----------
    u : ndarray or scalar
        Fourier variable (may be complex).
    S0 : float
        Spot price (unused in centred form, kept for interface clarity).
    r : float
        Risk-free interest rate.
    T : float
        Time to maturity.
    sigma : float
        Volatility.

    Returns
    -------
    ndarray or scalar
        Characteristic function values.
    """
    return np.exp(1j * u * (r - 0.5 * sigma**2) * T
                  - 0.5 * sigma**2 * u**2 * T)


# =============================================================================
# 2. FFT Pricing via Lewis Formula
# =============================================================================

def fft_Lewis(K, S0, r, T, cf, interp="cubic"):
    """
    Price European call options using the Lewis (2001) FFT method.

    The algorithm:
      1. Discretise the integration variable u on [0, B) with N points.
      2. Apply composite Simpson weights for higher-order accuracy.
      3. Construct the integrand including the Lewis kernel 1/(u^2 + 1/4).
      4. Evaluate the integral via the Inverse FFT (O(N log N)).
      5. Interpolate the result onto the requested log-moneyness values.

    Parameters
    ----------
    K : array_like
        Vector of strike prices.
    S0 : float
        Spot price.
    r : float
        Risk-free interest rate.
    T : float
        Time to maturity.
    cf : callable
        Characteristic function cf(u) of the centred log-return.
        Must accept complex arguments (the Lewis formula evaluates
        cf at u - 0.5j).
    interp : str, optional
        Interpolation method: "cubic" (default) or "linear".

    Returns
    -------
    prices : ndarray
        European call prices for each strike in K.
    """
    K = np.asarray(K, dtype=float)

    N = 2**15                   # Number of FFT points (power of 2 for speed)
    B = 500                     # Upper integration limit
    dx = B / N                  # Grid spacing in u-space
    x = np.arange(N) * dx       # Integration grid: u_0, u_1, ..., u_{N-1}

    # --- Simpson composite quadrature weights ---
    # Pattern: 1, 4, 2, 4, 2, ..., 4, 1  (scaled by dx/3)
    weight = 3 + (-1) ** (np.arange(N) + 1)   # alternating 4 and 2
    weight[0] = 1
    weight[N - 1] = 1

    # --- Log-strike grid produced by the FFT ---
    dk = 2 * np.pi / B          # Spacing in log-strike space
    b = N * dk / 2               # Half-width of the log-strike domain
    ks = -b + dk * np.arange(N)  # Centred log-strike grid

    # --- Build the integrand and apply IFFT ---
    # The Lewis integrand (before the IFFT twiddle factor) is:
    #   cf(u - i/2) / (u^2 + 1/4)
    # weighted by Simpson weights and the grid spacing.
    integrand = (np.exp(-1j * b * np.arange(N) * dx)
                 * cf(x - 0.5j)
                 * 1.0 / (x**2 + 0.25)
                 * weight * dx / 3)

    integral_value = np.real(ifft(integrand) * N)

    # --- Interpolate onto the requested strikes ---
    log_moneyness = np.log(S0 / K)

    if interp == "linear":
        spline = interp1d(ks, integral_value, kind="linear")
    elif interp == "cubic":
        spline = interp1d(ks, integral_value, kind="cubic")
    else:
        raise ValueError(f"Unknown interpolation method: {interp}")

    prices = S0 - np.sqrt(S0 * K) * np.exp(-r * T) / np.pi * spline(log_moneyness)

    return prices


# =============================================================================
# 3. Implied Volatility from Lewis Formula
# =============================================================================

def IV_from_Lewis(K, S0, T, r, cf, disp=False):
    """
    Extract Black-Scholes implied volatility from the Lewis formula.

    The idea is to find sigma such that the Lewis integral of the
    *model* characteristic function equals the Lewis integral of
    the Black-Scholes characteristic function with volatility sigma.
    This reduces to finding the root of the difference integral.

    The function tries several initial guesses and returns the first
    successful solution.

    Parameters
    ----------
    K : float
        Strike price (scalar).
    S0 : float
        Spot price.
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    cf : callable
        Characteristic function of the model (centred log-return).
    disp : bool, optional
        If True, print a warning when root-finding fails.

    Returns
    -------
    float
        Implied volatility, or -1 if root-finding fails.
    """
    k = np.log(S0 / K)

    def obj_fun(sig):
        """Difference of Lewis integrals: model cf minus BS cf with vol sig."""
        def integrand(u):
            # Black-Scholes characteristic function for centred log-return
            cf_bs = (np.exp(1j * u * r * T + 0.5 * r * T)
                     * np.exp(-0.5 * T * (u**2 + 0.25) * sig**2))
            return np.real(
                np.exp(u * k * 1j)
                * (cf(u - 0.5j) - cf_bs)
                * 1.0 / (u**2 + 0.25)
            )
        int_value = quad(integrand, 1e-15, 2000, limit=2000, full_output=1)[0]
        return int_value

    # Try several initial guesses to improve robustness
    X0 = [0.2, 1.0, 2.0, 4.0, 0.0001]
    for x0 in X0:
        x, _, solved, msg = fsolve(obj_fun, [x0], full_output=True, xtol=1e-4)
        if solved == 1:
            return x[0]

    if disp:
        print("IV_from_Lewis: root-finding failed for strike", K, "--", msg)
    return -1


# =============================================================================
# 4. Black-Scholes Closed-Form (for validation)
# =============================================================================

def bs_call_price(S0, K, r, T, sigma):
    """
    Black-Scholes closed-form European call price.

    Parameters
    ----------
    S0 : float
        Spot price.
    K : array_like
        Strike price(s).
    r : float
        Risk-free interest rate.
    T : float
        Time to maturity.
    sigma : float
        Volatility.

    Returns
    -------
    ndarray
        Call option prices.
    """
    K = np.asarray(K, dtype=float)
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * st.norm.cdf(d1) - K * np.exp(-r * T) * st.norm.cdf(d2)


# =============================================================================
# 5. Visualisation
# =============================================================================

def plot_results(K, fft_prices, bs_prices, iv_values, sigma_true):
    """
    Create a two-panel figure:
      Left  -- Option prices (FFT vs BS) as a function of strike.
      Right -- Implied volatility smile (should be flat for BS model).

    Parameters
    ----------
    K : ndarray
        Strike prices.
    fft_prices : ndarray
        Prices from fft_Lewis.
    bs_prices : ndarray
        Prices from bs_call_price.
    iv_values : ndarray
        Implied volatilities extracted by IV_from_Lewis.
    sigma_true : float
        True volatility used in the model.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Left panel: option prices ---
    ax1.plot(K, fft_prices, "o-", markersize=4, label="FFT Lewis")
    ax1.plot(K, bs_prices, "x--", markersize=6, label="BS closed-form")
    ax1.set_xlabel("Strike K")
    ax1.set_ylabel("European Call Price")
    ax1.set_title("FFT Lewis vs Black-Scholes")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # --- Right panel: implied volatility ---
    ax2.plot(K, iv_values, "s-", markersize=4, color="tab:orange",
             label="IV from Lewis")
    ax2.axhline(y=sigma_true, color="gray", linestyle="--", linewidth=1,
                label=f"True sigma = {sigma_true}")
    ax2.set_xlabel("Strike K")
    ax2.set_ylabel("Implied Volatility")
    ax2.set_title("Implied Volatility Smile (flat under BS)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()


# =============================================================================
# 6. Main Demo
# =============================================================================

def main():
    """
    End-to-end demonstration:
      1. Define Black-Scholes parameters.
      2. Price European calls via fft_Lewis across a strike range.
      3. Compare with Black-Scholes closed-form prices.
      4. Extract implied volatilities using IV_from_Lewis.
      5. Time the FFT pricer vs the closed-form.
      6. Print a summary table and display plots.
    """

    # ===== Market / Model Parameters =====
    S0 = 100.0           # Spot price
    r = 0.05             # Risk-free rate
    T = 1.0              # Time to maturity (1 year)
    sigma = 0.2          # Volatility (20%)

    # Strikes: range from deep-in-the-money to deep-out-of-the-money
    K = np.linspace(60, 140, 41)

    # Build the characteristic function (closure over model parameters)
    cf = lambda u: cf_normal(u, S0, r, T, sigma)

    # ===== 1. FFT Lewis Pricing =====
    print("=" * 65)
    print("  FFT Lewis Pricing Demo (Black-Scholes Model)")
    print("=" * 65)

    t0 = time.time()
    num_fft_runs = 100
    for _ in range(num_fft_runs):
        fft_prices = fft_Lewis(K, S0, r, T, cf, interp="cubic")
    t_fft = (time.time() - t0) / num_fft_runs

    # ===== 2. Black-Scholes Closed-Form =====
    t0 = time.time()
    for _ in range(num_fft_runs):
        bs_prices = bs_call_price(S0, K, r, T, sigma)
    t_bs = (time.time() - t0) / num_fft_runs

    # ===== 3. Comparison Table =====
    print(f"\nSpot S0 = {S0},  r = {r},  T = {T},  sigma = {sigma}")
    print(f"Number of strikes: {len(K)}")
    print(f"\n{'Strike':>10s} {'FFT Price':>12s} {'BS Price':>12s} {'Abs Error':>12s}")
    print("-" * 50)
    for i in range(0, len(K), 4):  # print every 4th strike to keep output readable
        err = abs(fft_prices[i] - bs_prices[i])
        print(f"{K[i]:10.1f} {fft_prices[i]:12.6f} {bs_prices[i]:12.6f} {err:12.2e}")

    max_err = np.max(np.abs(fft_prices - bs_prices))
    print(f"\nMax absolute error across all strikes: {max_err:.2e}")

    # ===== 4. Timing =====
    print(f"\nTiming ({num_fft_runs} iterations each):")
    print(f"  FFT Lewis   : {t_fft*1000:.3f} ms per call")
    print(f"  BS closed   : {t_bs*1000:.3f} ms per call")
    print(f"  Ratio (FFT/BS): {t_fft/t_bs:.1f}x")

    # ===== 5. Implied Volatility Extraction =====
    print("\nExtracting implied volatilities via IV_from_Lewis ...")
    # Use a coarser strike grid for IV (each call involves numerical integration)
    K_iv = np.linspace(70, 130, 13)
    iv_values = np.zeros(len(K_iv))

    t0 = time.time()
    for i, Ki in enumerate(K_iv):
        iv_values[i] = IV_from_Lewis(Ki, S0, T, r, cf, disp=True)
    t_iv = time.time() - t0

    print(f"\n{'Strike':>10s} {'Implied Vol':>14s} {'Error vs True':>14s}")
    print("-" * 42)
    for i in range(len(K_iv)):
        iv_err = abs(iv_values[i] - sigma)
        print(f"{K_iv[i]:10.1f} {iv_values[i]:14.6f} {iv_err:14.2e}")

    max_iv_err = np.max(np.abs(iv_values - sigma))
    print(f"\nMax IV error: {max_iv_err:.2e}")
    print(f"IV extraction took {t_iv:.2f}s for {len(K_iv)} strikes")

    # ===== 6. Plots =====
    # Re-compute FFT prices on the IV strike grid for the plot
    fft_prices_iv = fft_Lewis(K_iv, S0, r, T, cf)
    bs_prices_iv = bs_call_price(S0, K_iv, r, T, sigma)

    plot_results(K_iv, fft_prices_iv, bs_prices_iv, iv_values, sigma)
    plt.show()

    print("\nDone.")


if __name__ == "__main__":
    main()
