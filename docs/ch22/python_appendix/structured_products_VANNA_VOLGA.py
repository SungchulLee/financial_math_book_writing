"""
Vanna-Volga Hedging Module
==========================

Implementation of smile-aware hedging for exotic options including:
- Vanna and Volga computation
- Vanna-Volga pricing adjustment
- 25-delta risk reversal hedging
- Butterfly spread hedging

Reference: Chapter 22 - Structured Products (Section 22.4)
"""

import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
from typing import Tuple, Optional, Callable
from dataclasses import dataclass


@dataclass
class VolSurfaceParams:
    """Parameters for volatility surface."""
    atm_vol: float          # ATM volatility
    rr_25: float            # 25-delta risk reversal (call vol - put vol)
    bf_25: float            # 25-delta butterfly (average wing - ATM)
    T: float                # Time to maturity
    r: float                # Risk-free rate
    q: float                # Dividend yield


@dataclass
class ExoticGreeks:
    """Greeks for exotic options."""
    delta: float
    gamma: float
    vega: float
    vanna: float            # ∂²V/∂S∂σ = ∂Δ/∂σ = ∂vega/∂S
    volga: float            # ∂²V/∂σ² = ∂vega/∂σ


def black_scholes_price(S: float, K: float, T: float, r: float, q: float, 
                        sigma: float, is_call: bool = True) -> float:
    """Black-Scholes option price."""
    if T <= 0:
        return max(S - K, 0) if is_call else max(K - S, 0)
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if is_call:
        return S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)


def bs_delta(S: float, K: float, T: float, r: float, q: float, 
             sigma: float, is_call: bool = True) -> float:
    """Black-Scholes delta."""
    if T <= 0:
        return 1.0 if (is_call and S > K) else (0.0 if is_call else (-1.0 if S < K else 0.0))
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    
    if is_call:
        return np.exp(-q * T) * norm.cdf(d1)
    else:
        return -np.exp(-q * T) * norm.cdf(-d1)


def bs_vega(S: float, K: float, T: float, r: float, q: float, sigma: float) -> float:
    """Black-Scholes vega (per 1% vol move)."""
    if T <= 0:
        return 0.0
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return S * np.exp(-q * T) * norm.pdf(d1) * np.sqrt(T) * 0.01


def bs_vanna(S: float, K: float, T: float, r: float, q: float, sigma: float) -> float:
    """
    Black-Scholes vanna: ∂²V/∂S∂σ = ∂Δ/∂σ
    
    Measures how delta changes with volatility.
    """
    if T <= 0:
        return 0.0
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Vanna = -e^(-qT) * N'(d1) * d2 / σ
    return -np.exp(-q * T) * norm.pdf(d1) * d2 / sigma


def bs_volga(S: float, K: float, T: float, r: float, q: float, sigma: float) -> float:
    """
    Black-Scholes volga: ∂²V/∂σ² = ∂vega/∂σ
    
    Measures convexity of option value with respect to volatility.
    """
    if T <= 0:
        return 0.0
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Volga = S * e^(-qT) * √T * N'(d1) * d1 * d2 / σ
    return S * np.exp(-q * T) * np.sqrt(T) * norm.pdf(d1) * d1 * d2 / sigma


def implied_vol_from_delta(
    S: float, T: float, r: float, q: float,
    target_delta: float, vol_surface: VolSurfaceParams,
    is_call: bool = True
) -> float:
    """
    Get implied volatility for a given delta using smile parameterization.
    
    Uses a simple quadratic smile approximation:
    σ(Δ) = σ_ATM + slope * (Δ - 0.5) + curvature * (Δ - 0.5)²
    """
    # Simple smile interpolation
    # 25Δ put → Δ = -0.25
    # 25Δ call → Δ = 0.25 (forward delta convention varies)
    # ATM → Δ = 0.5
    
    atm = vol_surface.atm_vol
    rr = vol_surface.rr_25  # 25Δ call vol - 25Δ put vol
    bf = vol_surface.bf_25  # Average wing - ATM
    
    # Smile parameters from market quotes
    # σ_25Δcall = ATM + RR/2 + BF
    # σ_25Δput = ATM - RR/2 + BF
    # σ_ATM = ATM
    
    if is_call:
        delta_normalized = target_delta  # 0 to 1
    else:
        delta_normalized = 1 + target_delta  # -1 to 0 → 0 to 1
    
    # Quadratic interpolation
    x = delta_normalized - 0.5  # Center at ATM
    
    # Fit: σ(x) = ATM + a*x + b*x²
    # At x = -0.25 (25Δ put): ATM - a*0.25 + b*0.0625 = ATM - RR/2 + BF
    # At x = +0.25 (25Δ call): ATM + a*0.25 + b*0.0625 = ATM + RR/2 + BF
    # Solving: a = 2*RR, b = 16*BF
    
    a = 2 * rr
    b = 16 * bf
    
    sigma = atm + a * x + b * x**2
    
    return max(sigma, 0.01)  # Floor at 1%


def strike_from_delta(
    S: float, T: float, r: float, q: float, sigma: float,
    target_delta: float, is_call: bool = True
) -> float:
    """
    Find strike corresponding to a given delta.
    
    Uses root finding on BS delta formula.
    """
    def delta_diff(K):
        return bs_delta(S, K, T, r, q, sigma, is_call) - target_delta
    
    # Bounds for strike
    K_low = S * 0.5
    K_high = S * 2.0
    
    try:
        K = brentq(delta_diff, K_low, K_high)
    except ValueError:
        # If root finding fails, use approximation
        d1_target = norm.ppf(abs(target_delta) * np.exp(q * T))
        K = S * np.exp(-(d1_target * sigma * np.sqrt(T) - (r - q + 0.5 * sigma**2) * T))
    
    return K


def compute_exotic_greeks(
    price_func: Callable[[float, float], float],
    S: float,
    sigma: float,
    bump_spot: float = 0.01,
    bump_vol: float = 0.01
) -> ExoticGreeks:
    """
    Compute Greeks for an exotic option using finite differences.
    
    Parameters
    ----------
    price_func : callable
        Function that takes (S, sigma) and returns option price
    S : float
        Current spot price
    sigma : float
        Current volatility
    bump_spot : float
        Relative spot bump size
    bump_vol : float
        Absolute volatility bump size
        
    Returns
    -------
    ExoticGreeks
        All Greeks including vanna and volga
    """
    dS = S * bump_spot
    dsigma = bump_vol
    
    # Base price
    V = price_func(S, sigma)
    
    # Spot bumps
    V_up = price_func(S + dS, sigma)
    V_down = price_func(S - dS, sigma)
    
    # Vol bumps
    V_vol_up = price_func(S, sigma + dsigma)
    V_vol_down = price_func(S, sigma - dsigma)
    
    # Cross bumps for vanna
    V_up_vol_up = price_func(S + dS, sigma + dsigma)
    V_up_vol_down = price_func(S + dS, sigma - dsigma)
    V_down_vol_up = price_func(S - dS, sigma + dsigma)
    V_down_vol_down = price_func(S - dS, sigma - dsigma)
    
    # Greeks
    delta = (V_up - V_down) / (2 * dS)
    gamma = (V_up - 2 * V + V_down) / (dS ** 2)
    vega = (V_vol_up - V_vol_down) / 2  # Per 1% vol
    
    # Vanna: ∂²V/∂S∂σ
    vanna = (V_up_vol_up - V_up_vol_down - V_down_vol_up + V_down_vol_down) / (4 * dS * dsigma)
    
    # Volga: ∂²V/∂σ²
    volga = (V_vol_up - 2 * V + V_vol_down) / (dsigma ** 2)
    
    return ExoticGreeks(delta=delta, gamma=gamma, vega=vega, vanna=vanna, volga=volga)


def vanna_volga_adjustment(
    exotic_greeks: ExoticGreeks,
    vol_surface: VolSurfaceParams,
    S: float,
    T: float,
    r: float,
    q: float
) -> dict:
    """
    Compute Vanna-Volga pricing adjustment for exotic options.
    
    The adjustment accounts for the cost of hedging vanna and volga
    risk using vanilla options at different strikes.
    
    Parameters
    ----------
    exotic_greeks : ExoticGreeks
        Greeks of the exotic option
    vol_surface : VolSurfaceParams
        Volatility surface parameters
    S : float
        Current spot price
    T : float
        Time to maturity
    r : float
        Risk-free rate
    q : float
        Dividend yield
        
    Returns
    -------
    dict
        Contains adjustment amount and hedge ratios
    """
    atm_vol = vol_surface.atm_vol
    
    # Find 25-delta strikes
    K_25d_call = strike_from_delta(S, T, r, q, atm_vol, 0.25, is_call=True)
    K_25d_put = strike_from_delta(S, T, r, q, atm_vol, -0.25, is_call=False)
    K_atm = S * np.exp((r - q) * T)  # ATM forward
    
    # Get implied vols at these strikes
    sigma_25d_call = vol_surface.atm_vol + vol_surface.rr_25 / 2 + vol_surface.bf_25
    sigma_25d_put = vol_surface.atm_vol - vol_surface.rr_25 / 2 + vol_surface.bf_25
    sigma_atm = vol_surface.atm_vol
    
    # Vanna and volga of hedging instruments
    vanna_put = bs_vanna(S, K_25d_put, T, r, q, sigma_25d_put)
    vanna_call = bs_vanna(S, K_25d_call, T, r, q, sigma_25d_call)
    vanna_atm = bs_vanna(S, K_atm, T, r, q, sigma_atm)
    
    volga_put = bs_volga(S, K_25d_put, T, r, q, sigma_25d_put)
    volga_call = bs_volga(S, K_25d_call, T, r, q, sigma_25d_call)
    volga_atm = bs_volga(S, K_atm, T, r, q, sigma_atm)
    
    # Cost of wings vs ATM (smile cost)
    put_bs_atm = black_scholes_price(S, K_25d_put, T, r, q, sigma_atm, is_call=False)
    put_bs_smile = black_scholes_price(S, K_25d_put, T, r, q, sigma_25d_put, is_call=False)
    put_cost = put_bs_smile - put_bs_atm
    
    call_bs_atm = black_scholes_price(S, K_25d_call, T, r, q, sigma_atm, is_call=True)
    call_bs_smile = black_scholes_price(S, K_25d_call, T, r, q, sigma_25d_call, is_call=True)
    call_cost = call_bs_smile - call_bs_atm
    
    # Solve for hedge ratios
    # We want: x_p * vanna_p + x_c * vanna_c = exotic_vanna
    #          x_p * volga_p + x_c * volga_c = exotic_volga
    
    A = np.array([
        [vanna_put, vanna_call],
        [volga_put, volga_call]
    ])
    
    b = np.array([exotic_greeks.vanna, exotic_greeks.volga])
    
    try:
        x = np.linalg.solve(A, b)
        x_put = x[0]
        x_call = x[1]
    except np.linalg.LinAlgError:
        x_put = exotic_greeks.vanna / (vanna_put + 1e-10)
        x_call = exotic_greeks.volga / (volga_call + 1e-10)
    
    # Total adjustment
    adjustment = x_put * put_cost + x_call * call_cost
    
    return {
        'adjustment': adjustment,
        'put_hedge_ratio': x_put,
        'call_hedge_ratio': x_call,
        'K_25d_put': K_25d_put,
        'K_25d_call': K_25d_call,
        'put_cost': put_cost,
        'call_cost': call_cost
    }


def compute_smile_hedge(
    exotic_greeks: ExoticGreeks,
    S: float,
    vol_surface: VolSurfaceParams
) -> dict:
    """
    Compute smile hedging strategy using risk reversal and butterfly.
    
    Returns
    -------
    dict
        Hedge notionals for RR and BF
    """
    # Risk reversal hedge for vanna
    # RR has vanna ≈ 2 * vanna_25d_call (buy call, sell put)
    # To hedge exotic vanna, use: notional_RR = -exotic_vanna / (2 * vanna_25d)
    
    T = vol_surface.T
    r = vol_surface.r if hasattr(vol_surface, 'r') else 0.05
    q = vol_surface.q if hasattr(vol_surface, 'q') else 0.02
    sigma = vol_surface.atm_vol
    
    K_25d_call = strike_from_delta(S, T, r, q, sigma, 0.25, is_call=True)
    vanna_25d = bs_vanna(S, K_25d_call, T, r, q, sigma)
    
    rr_notional = -exotic_greeks.vanna / (2 * vanna_25d) if vanna_25d != 0 else 0
    
    # Butterfly hedge for volga
    # BF has volga ≈ volga_25d_call + volga_25d_put - 2*volga_ATM
    # Simplified: use straddle if vega exposure acceptable
    
    K_atm = S * np.exp((r - q) * T)
    volga_atm = bs_volga(S, K_atm, T, r, q, sigma)
    
    bf_notional = -exotic_greeks.volga / (2 * volga_atm) if volga_atm != 0 else 0
    
    return {
        'risk_reversal_notional': rr_notional,
        'butterfly_notional': bf_notional,
        'residual_vanna': exotic_greeks.vanna + rr_notional * 2 * vanna_25d,
        'residual_volga': exotic_greeks.volga + bf_notional * 2 * volga_atm
    }


if __name__ == "__main__":
    print("=" * 60)
    print("Vanna-Volga Hedging Examples")
    print("=" * 60)
    
    # Market parameters
    S = 100
    T = 1.0
    r = 0.05
    q = 0.02
    
    vol_surface = VolSurfaceParams(
        atm_vol=0.20,
        rr_25=0.02,      # 25Δ call 1% higher than 25Δ put
        bf_25=0.01,      # Wings 1% above ATM
        T=T,
        r=r,
        q=q
    )
    
    print(f"\nMarket Parameters:")
    print(f"  S = ${S}, T = {T}yr, r = {r*100}%, q = {q*100}%")
    print(f"  ATM Vol: {vol_surface.atm_vol*100}%")
    print(f"  25Δ Risk Reversal: {vol_surface.rr_25*100}%")
    print(f"  25Δ Butterfly: {vol_surface.bf_25*100}%")
    
    # Example: Down-and-in put exotic
    print("\n" + "-" * 50)
    print("Example: Down-and-In Put Greeks")
    print("-" * 50)
    
    # Simulate exotic option pricing function
    def exotic_price(S_val, sigma_val):
        """Simplified exotic pricing (would use proper model in practice)."""
        K = 100
        H = 85  # Barrier
        # Using BS as base, with barrier adjustment
        bs = black_scholes_price(S_val, K, T, r, q, sigma_val, is_call=False)
        # Knock-in adjustment (simplified)
        hit_prob = norm.cdf((np.log(H/S_val) + (r - q - 0.5*sigma_val**2)*T) / (sigma_val*np.sqrt(T)))
        return bs * (0.5 + 0.5 * hit_prob)
    
    exotic = compute_exotic_greeks(exotic_price, S, vol_surface.atm_vol)
    
    print(f"\nExotic Greeks:")
    print(f"  Delta: {exotic.delta:.4f}")
    print(f"  Gamma: {exotic.gamma:.6f}")
    print(f"  Vega:  {exotic.vega:.4f}")
    print(f"  Vanna: {exotic.vanna:.6f}")
    print(f"  Volga: {exotic.volga:.4f}")
    
    # Vanna-Volga adjustment
    print("\n" + "-" * 50)
    print("Vanna-Volga Adjustment")
    print("-" * 50)
    
    vv_adj = vanna_volga_adjustment(exotic, vol_surface, S, T, r, q)
    
    print(f"  25Δ Put Strike: ${vv_adj['K_25d_put']:.2f}")
    print(f"  25Δ Call Strike: ${vv_adj['K_25d_call']:.2f}")
    print(f"  Put Smile Cost: ${vv_adj['put_cost']:.4f}")
    print(f"  Call Smile Cost: ${vv_adj['call_cost']:.4f}")
    print(f"  Put Hedge Ratio: {vv_adj['put_hedge_ratio']:.4f}")
    print(f"  Call Hedge Ratio: {vv_adj['call_hedge_ratio']:.4f}")
    print(f"  Total VV Adjustment: ${vv_adj['adjustment']:.4f}")
    
    # Smile hedge
    print("\n" + "-" * 50)
    print("Smile Hedging Strategy")
    print("-" * 50)
    
    hedge = compute_smile_hedge(exotic, S, vol_surface)
    
    print(f"  Risk Reversal Notional: {hedge['risk_reversal_notional']:.4f}")
    print(f"  Butterfly Notional: {hedge['butterfly_notional']:.4f}")
    print(f"  Residual Vanna: {hedge['residual_vanna']:.6f}")
    print(f"  Residual Volga: {hedge['residual_volga']:.4f}")
    
    # Compare vanilla Greeks for reference
    print("\n" + "-" * 50)
    print("Vanilla Greeks for Comparison (ATM Put)")
    print("-" * 50)
    
    K_atm = S * np.exp((r - q) * T)
    sigma = vol_surface.atm_vol
    
    vanilla_vanna = bs_vanna(S, K_atm, T, r, q, sigma)
    vanilla_volga = bs_volga(S, K_atm, T, r, q, sigma)
    
    print(f"  Vanna: {vanilla_vanna:.6f}")
    print(f"  Volga: {vanilla_volga:.4f}")
    print(f"  Exotic/Vanilla Vanna Ratio: {exotic.vanna/vanilla_vanna:.2f}x")
    print(f"  Exotic/Vanilla Volga Ratio: {exotic.volga/vanilla_volga:.2f}x")
