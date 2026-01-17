"""
Range Accrual Pricing Module
============================

Implementation of range accrual note pricing including:
- Single range accruals
- Dual range accruals
- Step coupon structures
- Monte Carlo simulation with daily counting

Reference: Chapter 22 - Structured Products
"""

import numpy as np
from scipy.stats import norm
from typing import Tuple, Optional, List
from dataclasses import dataclass


@dataclass
class RangeAccrualParams:
    """Parameters for range accrual note pricing."""
    S0: float               # Initial stock price
    principal: float        # Note principal
    T: float                # Maturity (years)
    r: float                # Risk-free rate
    q: float                # Dividend yield
    sigma: float            # Volatility
    lower_barrier: float    # Lower range barrier (as % of initial)
    upper_barrier: float    # Upper range barrier (as % of initial)
    coupon_rate: float      # Annual coupon rate (max)
    accrual_days: int       # Business days per year (typically 252)


def monte_carlo_range_accrual(
    params: RangeAccrualParams,
    n_paths: int = 100000,
    seed: Optional[int] = None
) -> dict:
    """
    Price range accrual using Monte Carlo simulation.
    
    Simulates daily prices and counts in-range days.
    """
    if seed is not None:
        np.random.seed(seed)
    
    S0 = params.S0
    principal = params.principal
    T = params.T
    r = params.r
    q = params.q
    sigma = params.sigma
    
    L = params.lower_barrier * S0
    U = params.upper_barrier * S0
    n_days = int(params.accrual_days * T)
    dt = T / n_days
    
    # Simulate paths
    drift = (r - q - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt)
    
    Z = np.random.standard_normal((n_paths, n_days))
    log_returns = drift + diffusion * Z
    log_prices = np.log(S0) + np.cumsum(log_returns, axis=1)
    S = np.exp(log_prices)
    
    # Count in-range days for each path
    in_range = (S > L) & (S < U)
    days_in_range = np.sum(in_range, axis=1)
    
    # Coupon payments
    coupon_fraction = days_in_range / n_days
    coupons = params.coupon_rate * T * coupon_fraction * principal
    
    # Total payoff
    payoffs = principal + coupons
    discounted = np.exp(-r * T) * payoffs
    
    price = np.mean(discounted)
    std_error = np.std(discounted) / np.sqrt(n_paths)
    
    return {
        'price': price,
        'std_error': std_error,
        'price_pct': price / principal * 100,
        'expected_coupon': np.mean(coupons),
        'coupon_fraction': np.mean(coupon_fraction),
        'expected_range_days': np.mean(days_in_range),
        'prob_full_coupon': np.mean(days_in_range == n_days),
        'prob_zero_coupon': np.mean(days_in_range == 0)
    }


def dual_range_accrual(
    S0_1: float, S0_2: float, principal: float, T: float, r: float,
    q1: float, q2: float, sigma1: float, sigma2: float, rho: float,
    lower1: float, upper1: float, lower2: float, upper2: float,
    coupon_rate: float, n_paths: int = 50000, seed: Optional[int] = None
) -> dict:
    """Price dual range accrual (requires both assets in range)."""
    if seed is not None:
        np.random.seed(seed)
    
    n_days = int(252 * T)
    dt = T / n_days
    
    L1, U1 = lower1 * S0_1, upper1 * S0_1
    L2, U2 = lower2 * S0_2, upper2 * S0_2
    
    # Cholesky for correlation
    L_chol = np.array([[1, 0], [rho, np.sqrt(1 - rho**2)]])
    
    S1 = np.zeros((n_paths, n_days))
    S2 = np.zeros((n_paths, n_days))
    
    drift1 = (r - q1 - 0.5 * sigma1**2) * dt
    drift2 = (r - q2 - 0.5 * sigma2**2) * dt
    diff1 = sigma1 * np.sqrt(dt)
    diff2 = sigma2 * np.sqrt(dt)
    
    for i in range(n_days):
        Z_indep = np.random.standard_normal((2, n_paths))
        Z_corr = L_chol @ Z_indep
        
        if i == 0:
            S1[:, i] = S0_1 * np.exp(drift1 + diff1 * Z_corr[0])
            S2[:, i] = S0_2 * np.exp(drift2 + diff2 * Z_corr[1])
        else:
            S1[:, i] = S1[:, i-1] * np.exp(drift1 + diff1 * Z_corr[0])
            S2[:, i] = S2[:, i-1] * np.exp(drift2 + diff2 * Z_corr[1])
    
    both_in_range = ((S1 > L1) & (S1 < U1)) & ((S2 > L2) & (S2 < U2))
    days_in_range = np.sum(both_in_range, axis=1)
    
    coupon_fraction = days_in_range / n_days
    coupons = coupon_rate * T * coupon_fraction * principal
    
    payoffs = principal + coupons
    discounted = np.exp(-r * T) * payoffs
    
    return {
        'price': np.mean(discounted),
        'std_error': np.std(discounted) / np.sqrt(n_paths),
        'coupon_fraction': np.mean(coupon_fraction),
        'expected_range_days': np.mean(days_in_range)
    }


if __name__ == "__main__":
    print("=" * 60)
    print("Range Accrual Pricing Examples")
    print("=" * 60)
    
    params = RangeAccrualParams(
        S0=100, principal=10000, T=1, r=0.05, q=0.02, sigma=0.20,
        lower_barrier=0.85, upper_barrier=1.15,
        coupon_rate=0.08, accrual_days=252
    )
    
    print(f"\nParameters:")
    print(f"  S0=${params.S0}, Range: [{params.lower_barrier*100}%, {params.upper_barrier*100}%]")
    print(f"  Max Coupon: {params.coupon_rate*100}%, Volatility: {params.sigma*100}%")
    
    mc = monte_carlo_range_accrual(params, n_paths=100000, seed=42)
    
    print(f"\nMonte Carlo Results:")
    print(f"  Price: ${mc['price']:.2f} ({mc['price_pct']:.2f}%)")
    print(f"  Expected Coupon: ${mc['expected_coupon']:.2f}")
    print(f"  Days in Range: {mc['expected_range_days']:.1f} / 252")
    print(f"  Coupon Fraction: {mc['coupon_fraction']*100:.1f}%")
    print(f"  Prob Full Coupon: {mc['prob_full_coupon']*100:.2f}%")
    
    # Dual range
    print("\n" + "-" * 50)
    print("Dual Range Accrual:")
    
    dual = dual_range_accrual(
        S0_1=100, S0_2=100, principal=10000, T=1, r=0.05,
        q1=0.02, q2=0.01, sigma1=0.20, sigma2=0.25, rho=0.6,
        lower1=0.85, upper1=1.15, lower2=0.80, upper2=1.20,
        coupon_rate=0.12, n_paths=50000, seed=42
    )
    
    print(f"  Price: ${dual['price']:.2f}")
    print(f"  Days Both in Range: {dual['expected_range_days']:.1f}")
    print(f"  Coupon Fraction: {dual['coupon_fraction']*100:.1f}%")
