"""
Barrier Option Pricing Module
=============================

Comprehensive implementation of barrier option pricing including:
- Closed-form solutions (Reiner-Rubinstein)
- Monte Carlo with discrete monitoring
- Broadie-Glasserman-Kou discrete monitoring adjustment
- Greeks computation

Reference: Chapter 22 - Structured Products
"""

import numpy as np
from scipy.stats import norm
from typing import Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class BarrierType(Enum):
    """Enumeration of barrier option types."""
    DOWN_AND_OUT_CALL = "DOC"
    DOWN_AND_OUT_PUT = "DOP"
    DOWN_AND_IN_CALL = "DIC"
    DOWN_AND_IN_PUT = "DIP"
    UP_AND_OUT_CALL = "UOC"
    UP_AND_OUT_PUT = "UOP"
    UP_AND_IN_CALL = "UIC"
    UP_AND_IN_PUT = "UIP"


@dataclass
class BarrierOptionParams:
    """Parameters for barrier option pricing."""
    S0: float          # Current stock price
    K: float           # Strike price
    H: float           # Barrier level
    T: float           # Time to maturity (years)
    r: float           # Risk-free rate
    q: float           # Dividend yield
    sigma: float       # Volatility
    rebate: float = 0  # Rebate paid if knocked out


def black_scholes_call(S: float, K: float, T: float, r: float, q: float, sigma: float) -> float:
    """Standard Black-Scholes call price."""
    if T <= 0:
        return max(S - K, 0)
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def black_scholes_put(S: float, K: float, T: float, r: float, q: float, sigma: float) -> float:
    """Standard Black-Scholes put price."""
    if T <= 0:
        return max(K - S, 0)
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)


def down_and_out_call(params: BarrierOptionParams) -> float:
    """
    Price a down-and-out call option using Reiner-Rubinstein closed-form formula.
    
    The option pays max(S_T - K, 0) if the stock never touches barrier H from above.
    """
    S0, K, H, T, r, q, sigma = params.S0, params.K, params.H, params.T, params.r, params.q, params.sigma
    
    if S0 <= H:
        return params.rebate * np.exp(-r * T)
    
    lambda_ = (r - q + 0.5 * sigma**2) / sigma**2
    x1 = (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    y1 = (np.log(H**2 / (S0 * K)) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    
    sqrtT = np.sqrt(T)
    
    term1 = S0 * np.exp(-q * T) * norm.cdf(x1)
    term2 = K * np.exp(-r * T) * norm.cdf(x1 - sigma * sqrtT)
    term3 = S0 * np.exp(-q * T) * (H / S0)**(2 * lambda_) * norm.cdf(y1)
    term4 = K * np.exp(-r * T) * (H / S0)**(2 * lambda_ - 2) * norm.cdf(y1 - sigma * sqrtT)
    
    return (term1 - term2) - (term3 - term4)


def down_and_in_call(params: BarrierOptionParams) -> float:
    """Price a down-and-in call option using parity."""
    S0, K, H, T, r, q, sigma = params.S0, params.K, params.H, params.T, params.r, params.q, params.sigma
    
    if S0 <= H:
        return black_scholes_call(S0, K, T, r, q, sigma)
    
    vanilla = black_scholes_call(S0, K, T, r, q, sigma)
    doc = down_and_out_call(params)
    return vanilla - doc


# Broadie-Glasserman-Kou adjustment constant
BETA_BGK = 0.5826  # ≈ -ζ(1/2) / √(2π)


def bgk_barrier_adjustment(H: float, sigma: float, dt: float, is_down_barrier: bool) -> float:
    """
    Compute Broadie-Glasserman-Kou adjusted barrier for discrete monitoring.
    
    Parameters
    ----------
    H : float - Original barrier level
    sigma : float - Volatility (annualized)
    dt : float - Monitoring interval (in years)
    is_down_barrier : bool - True for down barriers, False for up barriers
        
    Returns
    -------
    float - Adjusted barrier level
    """
    adjustment = BETA_BGK * sigma * np.sqrt(dt)
    
    if is_down_barrier:
        return H * np.exp(adjustment)  # Adjust upward
    else:
        return H * np.exp(-adjustment)  # Adjust downward


def monte_carlo_barrier_option(
    params: BarrierOptionParams,
    barrier_type: BarrierType,
    n_paths: int = 100000,
    n_steps: int = 252,
    seed: Optional[int] = None
) -> Tuple[float, float]:
    """
    Price barrier option using Monte Carlo simulation.
    
    Returns
    -------
    tuple - (price, standard_error)
    """
    if seed is not None:
        np.random.seed(seed)
    
    S0, K, H, T, r, q, sigma = params.S0, params.K, params.H, params.T, params.r, params.q, params.sigma
    
    dt = T / n_steps
    drift = (r - q - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt)
    
    Z = np.random.standard_normal((n_paths, n_steps))
    log_returns = drift + diffusion * Z
    log_prices = np.log(S0) + np.cumsum(log_returns, axis=1)
    S = np.exp(log_prices)
    
    S_T = S[:, -1]
    
    is_down = "DOWN" in barrier_type.name
    is_out = "OUT" in barrier_type.name
    is_call = "CALL" in barrier_type.name
    
    if is_down:
        barrier_hit = np.min(S, axis=1) <= H
    else:
        barrier_hit = np.max(S, axis=1) >= H
    
    if is_call:
        vanilla_payoff = np.maximum(S_T - K, 0)
    else:
        vanilla_payoff = np.maximum(K - S_T, 0)
    
    if is_out:
        payoff = np.where(barrier_hit, params.rebate, vanilla_payoff)
    else:
        payoff = np.where(barrier_hit, vanilla_payoff, 0)
    
    discounted_payoff = np.exp(-r * T) * payoff
    price = np.mean(discounted_payoff)
    se = np.std(discounted_payoff) / np.sqrt(n_paths)
    
    return price, se


if __name__ == "__main__":
    print("=" * 60)
    print("Barrier Option Pricing Examples")
    print("=" * 60)
    
    params = BarrierOptionParams(
        S0=100, K=100, H=90, T=1, r=0.05, q=0.02, sigma=0.25
    )
    
    print(f"\nParameters: S0=${params.S0}, K=${params.K}, H=${params.H}")
    print(f"T={params.T}yr, r={params.r*100}%, q={params.q*100}%, σ={params.sigma*100}%")
    
    vanilla = black_scholes_call(params.S0, params.K, params.T, params.r, params.q, params.sigma)
    doc = down_and_out_call(params)
    dic = down_and_in_call(params)
    
    print(f"\nVanilla Call:        ${vanilla:.4f}")
    print(f"Down-and-Out Call:   ${doc:.4f}")
    print(f"Down-and-In Call:    ${dic:.4f}")
    print(f"Sum (= Vanilla):     ${doc + dic:.4f}")
    
    # BGK Adjustment
    print("\nBGK Discrete Monitoring Adjustment:")
    for freq, name in [(252, "Daily"), (52, "Weekly"), (12, "Monthly")]:
        H_adj = bgk_barrier_adjustment(params.H, params.sigma, 1/freq, True)
        print(f"  {name}: H={params.H} → H_adj={H_adj:.2f}")
    
    # Monte Carlo
    mc_price, mc_se = monte_carlo_barrier_option(
        params, BarrierType.DOWN_AND_OUT_CALL, n_paths=100000, seed=42
    )
    print(f"\nMC Down-and-Out Call: ${mc_price:.4f} ± ${1.96*mc_se:.4f}")
