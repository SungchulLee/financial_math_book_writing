"""
Bsm Functions

Educational script demonstrating bsm functions concepts.
"""

# ---
# title: "BSM Analytical Functions"
# description: >
#   Standalone utility functions for Black-Scholes-Merton pricing:
#     - bsm_call_value  : closed-form European call price
#     - bsm_put_value   : closed-form European put price (via put-call parity)
#     - bsm_vega        : Vega (sensitivity to volatility)
#     - bsm_call_imp_vol: Newton-Raphson implied volatility solver
#
#   These functions are intentionally stateless (no classes) so they
#   can be imported as building blocks elsewhere in the book.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

from math import log, sqrt, exp
from scipy import stats
import numpy as np


# ======================================================================
# ── Black-Scholes-Merton call value ────────────────────────────
def bsm_call_value(S0, K, T, r, sigma):
    """Analytical European call price under BSM.

    Parameters
    ----------
    S0 : float    – current stock price
    K  : float    – strike price
    T  : float    – time to maturity (year fraction)
    r  : float    – risk-free rate (continuous compounding)
    sigma : float – volatility (annualised)

    Returns
    -------
    float – call option present value
    """
    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    value = S0 * stats.norm.cdf(d1) - K * exp(-r * T) * stats.norm.cdf(d2)
    return value


# ── Black-Scholes-Merton put value (via put-call parity) ──────
def bsm_put_value(S0, K, T, r, sigma):
    """Analytical European put price under BSM (put-call parity).

    Parameters
    ----------
    S0, K, T, r, sigma : same as bsm_call_value

    Returns
    -------
    float – put option present value
    """
    call = bsm_call_value(S0, K, T, r, sigma)
    return call - S0 + K * exp(-r * T)


# ── Vega ───────────────────────────────────────────────────────
def bsm_vega(S0, K, T, r, sigma):
    """Vega of a European option under BSM.

    Returns
    -------
    float – partial derivative of the option price w.r.t. sigma
    """
    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    return S0 * stats.norm.pdf(d1) * sqrt(T)


# ── Implied volatility (Newton-Raphson) ────────────────────────
def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est=0.25, tol=1e-10, max_iter=100):
    """Implied volatility of a European call via Newton-Raphson.

    Parameters
    ----------
    C0 : float        – observed market price of the call
    sigma_est : float – initial guess for implied vol
    tol : float       – convergence tolerance
    max_iter : int    – maximum iterations

    Returns
    -------
    float – implied volatility estimate
    """
    for _ in range(max_iter):
        diff = bsm_call_value(S0, K, T, r, sigma_est) - C0
        vega = bsm_vega(S0, K, T, r, sigma_est)
        if abs(vega) < 1e-14:
            break
        sigma_est -= diff / vega
        if abs(diff) < tol:
            break
    return sigma_est


# ── Quick demonstration ────────────────────────────────────────
if __name__ == "__main__":
    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.2

    call = bsm_call_value(S0, K, T, r, sigma)
    put = bsm_put_value(S0, K, T, r, sigma)
    vega = bsm_vega(S0, K, T, r, sigma)

    print(f"BSM Analytical Pricing  (S0={S0}, K={K}, T={T}, r={r}, sigma={sigma})")
    print(f"  Call  : {call:.6f}")
    print(f"  Put   : {put:.6f}")
    print(f"  Vega  : {vega:.6f}")

    # Round-trip: price -> implied vol -> price
    iv = bsm_call_imp_vol(S0, K, T, r, call)
    print(f"  IV    : {iv:.6f}  (should recover {sigma})")
