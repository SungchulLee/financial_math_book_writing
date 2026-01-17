"""
Variance Swap Pricing Module

This module implements variance swap pricing using the log-contract replication
method (Carr & Madan, Demeterfi et al.). It provides:
- Fair variance strike calculation from option prices
- Discrete monitoring adjustment
- Mark-to-market calculations
- Realized variance computation

Author: Chapter 24 - Variance and Volatility
"""

import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.stats import norm
from typing import Tuple, Optional, List


def calculate_realized_variance(
    prices: np.ndarray,
    annualization_factor: int = 252,
    log_returns: bool = True
) -> float:
    """
    Calculate realized variance from price series.
    
    Parameters
    ----------
    prices : np.ndarray
        Array of prices (daily closes)
    annualization_factor : int
        Number of trading days per year (default: 252)
    log_returns : bool
        If True, use log returns; if False, use simple returns
    
    Returns
    -------
    float
        Annualized realized variance
    
    Example
    -------
    >>> prices = np.array([100, 101, 99, 102, 100])
    >>> rv = calculate_realized_variance(prices)
    >>> print(f"Realized variance: {rv:.2f}")
    """
    if log_returns:
        returns = np.log(prices[1:] / prices[:-1])
    else:
        returns = (prices[1:] - prices[:-1]) / prices[:-1]
    
    n = len(returns)
    # Note: Using n (not n-1) to match market convention for variance swaps
    realized_variance = (annualization_factor / n) * np.sum(returns ** 2)
    
    return realized_variance


def calculate_fair_variance_strike(
    spot: float,
    forward: float,
    strikes: np.ndarray,
    call_prices: np.ndarray,
    put_prices: np.ndarray,
    r: float,
    T: float,
    method: str = 'log_contract'
) -> float:
    """
    Calculate fair variance swap strike using log-contract replication.
    
    Implements the model-free implied variance formula:
    K_var = (2*exp(rT)/T) * [∫_0^F P(K)/K² dK + ∫_F^∞ C(K)/K² dK]
    
    Parameters
    ----------
    spot : float
        Current spot price
    forward : float
        Forward price F = S * exp(rT)
    strikes : np.ndarray
        Array of option strikes (sorted ascending)
    call_prices : np.ndarray
        OTM call prices (for K > forward)
    put_prices : np.ndarray
        OTM put prices (for K < forward)
    r : float
        Risk-free rate (annualized)
    T : float
        Time to maturity (in years)
    method : str
        'log_contract' (default) or 'vix_methodology'
    
    Returns
    -------
    float
        Fair variance strike (annualized, in variance units)
    
    Example
    -------
    >>> strikes = np.array([90, 95, 100, 105, 110])
    >>> calls = np.array([10.5, 6.2, 3.1, 1.2, 0.4])
    >>> puts = np.array([0.3, 0.8, 2.0, 5.0, 9.8])
    >>> K_var = calculate_fair_variance_strike(
    ...     spot=100, forward=101, strikes=strikes,
    ...     call_prices=calls, put_prices=puts, r=0.05, T=0.25
    ... )
    """
    # Use OTM options: puts below forward, calls above forward
    put_mask = strikes < forward
    call_mask = strikes >= forward
    
    # Calculate contribution from puts (K < F)
    put_strikes = strikes[put_mask]
    put_prices_otm = put_prices[put_mask]
    
    if len(put_strikes) > 1:
        dk_puts = np.diff(put_strikes)
        # Use midpoint strikes for integration
        k_mid_puts = (put_strikes[:-1] + put_strikes[1:]) / 2
        p_mid_puts = (put_prices_otm[:-1] + put_prices_otm[1:]) / 2
        put_integral = np.sum(dk_puts * p_mid_puts / (k_mid_puts ** 2))
    else:
        put_integral = 0
    
    # Calculate contribution from calls (K >= F)
    call_strikes = strikes[call_mask]
    call_prices_otm = call_prices[call_mask]
    
    if len(call_strikes) > 1:
        dk_calls = np.diff(call_strikes)
        k_mid_calls = (call_strikes[:-1] + call_strikes[1:]) / 2
        c_mid_calls = (call_prices_otm[:-1] + call_prices_otm[1:]) / 2
        call_integral = np.sum(dk_calls * c_mid_calls / (k_mid_calls ** 2))
    else:
        call_integral = 0
    
    # Fair variance strike
    K_var = (2 * np.exp(r * T) / T) * (put_integral + call_integral)
    
    # Convert to percentage squared (multiply by 10000 for standard convention)
    K_var_pct = K_var * 10000
    
    return K_var_pct


def discrete_monitoring_adjustment(
    K_var_continuous: float,
    skewness: float,
    n_observations: int
) -> float:
    """
    Apply discrete monitoring adjustment to continuous variance strike.
    
    K_var_discrete ≈ K_var_continuous × (1 + skew²/(12n))
    
    Parameters
    ----------
    K_var_continuous : float
        Continuous variance strike
    skewness : float
        Skewness of log-return distribution (typically negative for equities)
    n_observations : int
        Number of discrete observations
    
    Returns
    -------
    float
        Adjusted variance strike for discrete monitoring
    
    Example
    -------
    >>> K_cont = 400  # 20% vol squared
    >>> K_disc = discrete_monitoring_adjustment(K_cont, skewness=-0.5, n_observations=63)
    """
    adjustment = 1 + (skewness ** 2) / (12 * n_observations)
    return K_var_continuous * adjustment


def mark_to_market_variance_swap(
    notional: float,
    strike: float,
    realized_variance_accrued: float,
    forward_variance: float,
    days_elapsed: int,
    days_total: int,
    r: float
) -> float:
    """
    Calculate mark-to-market value of a variance swap position.
    
    Parameters
    ----------
    notional : float
        Variance notional ($ per variance point)
    strike : float
        Original variance strike
    realized_variance_accrued : float
        Realized variance accumulated so far
    forward_variance : float
        Current forward variance strike (from option prices)
    days_elapsed : int
        Trading days elapsed
    days_total : int
        Total trading days in swap
    r : float
        Risk-free rate
    
    Returns
    -------
    float
        Mark-to-market value (positive = gain for long position)
    
    Example
    -------
    >>> mtm = mark_to_market_variance_swap(
    ...     notional=1000, strike=400, realized_variance_accrued=150,
    ...     forward_variance=450, days_elapsed=21, days_total=63, r=0.05
    ... )
    """
    t = days_elapsed / 252
    T = days_total / 252
    tau = T - t  # Time remaining
    
    # Weight of accrued vs forward variance
    w_accrued = days_elapsed / days_total
    w_forward = 1 - w_accrued
    
    # Expected final variance
    expected_final_variance = (
        w_accrued * realized_variance_accrued + 
        w_forward * forward_variance
    )
    
    # Present value of expected payoff
    discount_factor = np.exp(-r * tau)
    mtm = notional * (expected_final_variance - strike) * discount_factor
    
    return mtm


def variance_to_vega_notional(
    variance_notional: float,
    strike_vol: float
) -> float:
    """
    Convert variance notional to vega notional.
    
    N_vega = N_var × 2 × σ_strike
    
    Parameters
    ----------
    variance_notional : float
        Notional in $ per variance point
    strike_vol : float
        Strike volatility (decimal, e.g., 0.20 for 20%)
    
    Returns
    -------
    float
        Vega notional ($ per 1% vol move)
    """
    return variance_notional * 2 * strike_vol * 100


def vega_to_variance_notional(
    vega_notional: float,
    strike_vol: float
) -> float:
    """
    Convert vega notional to variance notional.
    
    N_var = N_vega / (2 × σ_strike)
    
    Parameters
    ----------
    vega_notional : float
        Notional in $ per 1% vol move
    strike_vol : float
        Strike volatility (decimal, e.g., 0.20 for 20%)
    
    Returns
    -------
    float
        Variance notional ($ per variance point)
    """
    return vega_notional / (2 * strike_vol * 100)


def simulate_variance_swap_pnl(
    prices: np.ndarray,
    strike: float,
    notional: float,
    annualization: int = 252
) -> dict:
    """
    Simulate variance swap P&L given a price path.
    
    Parameters
    ----------
    prices : np.ndarray
        Daily price series
    strike : float
        Variance strike (in % squared, e.g., 400 for 20% vol)
    notional : float
        Variance notional ($ per variance point)
    annualization : int
        Annualization factor
    
    Returns
    -------
    dict
        Dictionary with realized variance, P&L, and statistics
    
    Example
    -------
    >>> np.random.seed(42)
    >>> prices = 100 * np.exp(np.cumsum(np.random.normal(0, 0.01, 63)))
    >>> result = simulate_variance_swap_pnl(prices, strike=400, notional=1000)
    """
    # Calculate realized variance
    rv = calculate_realized_variance(prices, annualization)
    
    # Calculate P&L (long variance position)
    pnl = notional * (rv - strike)
    
    # Calculate realized volatility
    realized_vol = np.sqrt(rv) if rv >= 0 else -np.sqrt(-rv)
    strike_vol = np.sqrt(strike)
    
    return {
        'realized_variance': rv,
        'realized_vol': realized_vol,
        'strike': strike,
        'strike_vol': strike_vol,
        'pnl': pnl,
        'pnl_per_vol_point': pnl / (realized_vol - strike_vol) if realized_vol != strike_vol else 0,
        'n_observations': len(prices) - 1
    }


# Example usage and demonstration
if __name__ == "__main__":
    print("=" * 60)
    print("Variance Swap Pricing - Demonstration")
    print("=" * 60)
    
    # Example 1: Realized variance calculation
    print("\n1. Realized Variance Calculation")
    print("-" * 40)
    np.random.seed(42)
    n_days = 63  # 3 months
    daily_vol = 0.20 / np.sqrt(252)  # 20% annual vol
    prices = 100 * np.exp(np.cumsum(np.random.normal(0, daily_vol, n_days)))
    
    rv = calculate_realized_variance(prices)
    print(f"Simulated prices: {n_days} days")
    print(f"Target volatility: 20%")
    print(f"Realized variance: {rv:.2f}")
    print(f"Realized volatility: {np.sqrt(rv):.2f}%")
    
    # Example 2: Variance swap P&L simulation
    print("\n2. Variance Swap P&L Simulation")
    print("-" * 40)
    strike = 400  # 20% vol squared
    notional = 1000  # $1,000 per variance point
    
    result = simulate_variance_swap_pnl(prices, strike, notional)
    print(f"Strike: {result['strike']:.0f} ({result['strike_vol']:.1f}% vol)")
    print(f"Realized: {result['realized_variance']:.2f} ({result['realized_vol']:.2f}% vol)")
    print(f"P&L (long variance): ${result['pnl']:,.2f}")
    
    # Example 3: Notional conversion
    print("\n3. Notional Conversion")
    print("-" * 40)
    vega_target = 100000  # $100,000 per 1% vol
    strike_vol = 0.20
    var_notional = vega_to_variance_notional(vega_target, strike_vol)
    print(f"Target vega notional: ${vega_target:,}")
    print(f"Strike volatility: {strike_vol*100:.0f}%")
    print(f"Required variance notional: ${var_notional:,.2f} per variance point")
    
    # Verify conversion
    vega_back = variance_to_vega_notional(var_notional, strike_vol)
    print(f"Verification: ${vega_back:,.2f} per 1% vol")
    
    # Example 4: Mark-to-market
    print("\n4. Mark-to-Market Calculation")
    print("-" * 40)
    mtm = mark_to_market_variance_swap(
        notional=1000,
        strike=400,
        realized_variance_accrued=150,
        forward_variance=450,
        days_elapsed=21,
        days_total=63,
        r=0.05
    )
    print(f"Notional: $1,000/point")
    print(f"Strike: 400 (20% vol)")
    print(f"Days elapsed: 21 / 63")
    print(f"Realized variance accrued: 150")
    print(f"Forward variance: 450")
    print(f"Mark-to-Market: ${mtm:,.2f}")
    
    # Example 5: Discrete monitoring adjustment
    print("\n5. Discrete Monitoring Adjustment")
    print("-" * 40)
    K_continuous = 400
    skew = -0.5
    n_obs = 63
    K_discrete = discrete_monitoring_adjustment(K_continuous, skew, n_obs)
    print(f"Continuous strike: {K_continuous:.2f}")
    print(f"Skewness: {skew}")
    print(f"Observations: {n_obs}")
    print(f"Discrete strike: {K_discrete:.4f}")
    print(f"Adjustment: {(K_discrete/K_continuous - 1)*10000:.2f} bps")
