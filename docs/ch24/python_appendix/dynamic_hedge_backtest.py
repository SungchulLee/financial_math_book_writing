"""
Dynamic Volatility Hedge Backtest Module

This module implements tools for backtesting dynamic hedging strategies:
- VIX-scaled hedging
- Conditional hedging rules
- Sigmoid scaling functions
- Performance analysis

Author: Chapter 24 - Variance and Volatility
"""

import numpy as np
import pandas as pd
from typing import Tuple, Dict, Optional, Callable
from dataclasses import dataclass


@dataclass
class DynamicHedgeResult:
    """Results from dynamic hedge backtest."""
    total_pnl: float
    hedge_cost: float
    hedge_gain: float
    avg_hedge_ratio: float
    max_drawdown: float
    sharpe_ratio: float
    n_rebalances: int


def linear_vix_scaling(
    vix: float,
    vix_min: float = 12,
    vix_max: float = 22,
    min_hedge: float = 0.0,
    max_hedge: float = 2.0
) -> float:
    """
    Linear VIX-based hedge scaling.
    
    f(VIX) = max(min_hedge, min(max_hedge, (VIX - vix_min) / (vix_max - vix_min)))
    
    Parameters
    ----------
    vix : float
        Current VIX level
    vix_min : float
        VIX level at which hedge is zero
    vix_max : float
        VIX level at which hedge is at maximum
    min_hedge : float
        Minimum hedge ratio (floor)
    max_hedge : float
        Maximum hedge ratio (cap)
    
    Returns
    -------
    float
        Hedge ratio (0 to max_hedge)
    """
    raw_ratio = (vix - vix_min) / (vix_max - vix_min) if vix_max > vix_min else 0
    return max(min_hedge, min(max_hedge, raw_ratio))


def sigmoid_vix_scaling(
    vix: float,
    vix_mid: float = 20,
    steepness: float = 0.2,
    max_hedge: float = 2.0
) -> float:
    """
    Sigmoid VIX-based hedge scaling (smooth transition).
    
    f(VIX) = max_hedge / (1 + exp(-k × (VIX - VIX_mid)))
    
    Parameters
    ----------
    vix : float
        Current VIX level
    vix_mid : float
        VIX level at sigmoid midpoint (50% hedge)
    steepness : float
        Steepness parameter k
    max_hedge : float
        Maximum hedge ratio
    
    Returns
    -------
    float
        Hedge ratio (0 to max_hedge)
    """
    return max_hedge / (1 + np.exp(-steepness * (vix - vix_mid)))


def conditional_hedge_rule(
    vix: float,
    threshold_low: float = 15,
    threshold_high: float = 25,
    hedge_low: float = 0.0,
    hedge_mid: float = 0.5,
    hedge_high: float = 1.0
) -> float:
    """
    Conditional (tiered) hedge rule.
    
    Parameters
    ----------
    vix : float
        Current VIX level
    threshold_low : float
        VIX threshold below which hedge is minimal
    threshold_high : float
        VIX threshold above which hedge is maximal
    hedge_low : float
        Hedge ratio when VIX < threshold_low
    hedge_mid : float
        Hedge ratio when threshold_low <= VIX < threshold_high
    hedge_high : float
        Hedge ratio when VIX >= threshold_high
    
    Returns
    -------
    float
        Hedge ratio
    """
    if vix < threshold_low:
        return hedge_low
    elif vix < threshold_high:
        return hedge_mid
    else:
        return hedge_high


def realized_vol_scaling(
    realized_vol: float,
    target_vol: float = 0.15,
    max_hedge: float = 2.0
) -> float:
    """
    Scale hedge based on realized volatility.
    
    f(RV) = min(max_hedge, RV / target_vol)
    
    Parameters
    ----------
    realized_vol : float
        Current realized volatility (decimal)
    target_vol : float
        Target/normal volatility
    max_hedge : float
        Maximum hedge ratio
    
    Returns
    -------
    float
        Hedge ratio
    """
    return min(max_hedge, realized_vol / target_vol)


def should_rebalance(
    vix_current: float,
    vix_last: float,
    days_since_last: int,
    threshold_vix: float = 3.0,
    max_days: int = 7
) -> bool:
    """
    Determine if hedge should be rebalanced.
    
    Parameters
    ----------
    vix_current : float
        Current VIX level
    vix_last : float
        VIX at last rebalance
    days_since_last : int
        Days since last rebalance
    threshold_vix : float
        VIX move threshold to trigger rebalance
    max_days : int
        Maximum days between rebalances
    
    Returns
    -------
    bool
        True if should rebalance
    """
    vix_moved = abs(vix_current - vix_last) > threshold_vix
    time_limit = days_since_last >= max_days
    return vix_moved or time_limit


def backtest_dynamic_hedge(
    portfolio_returns: pd.Series,
    vix_series: pd.Series,
    implied_variance: pd.Series,
    scaling_func: Callable[[float], float],
    base_notional: float = 1000.0,
    rebalance_threshold_vix: float = 3.0,
    rebalance_max_days: int = 7,
    hedge_cost_bps: float = 5.0
) -> Tuple[pd.DataFrame, DynamicHedgeResult]:
    """
    Backtest a dynamic hedging strategy.
    
    Parameters
    ----------
    portfolio_returns : pd.Series
        Daily portfolio returns
    vix_series : pd.Series
        VIX levels
    implied_variance : pd.Series
        Implied variance (for hedge P&L calculation)
    scaling_func : Callable
        Function that takes VIX and returns hedge ratio
    base_notional : float
        Base variance notional
    rebalance_threshold_vix : float
        VIX move to trigger rebalance
    rebalance_max_days : int
        Maximum days between rebalances
    hedge_cost_bps : float
        Transaction cost per rebalance (basis points)
    
    Returns
    -------
    Tuple[pd.DataFrame, DynamicHedgeResult]
        Daily results DataFrame and summary statistics
    """
    # Align all series
    df = pd.DataFrame({
        'portfolio_return': portfolio_returns,
        'vix': vix_series,
        'implied_var': implied_variance
    }).dropna()
    
    n_days = len(df)
    
    # Initialize tracking arrays
    hedge_ratios = np.zeros(n_days)
    hedge_notionals = np.zeros(n_days)
    hedge_pnls = np.zeros(n_days)
    rebalance_costs = np.zeros(n_days)
    cumulative_pnl = np.zeros(n_days)
    
    # Track rebalancing
    last_rebalance_vix = df['vix'].iloc[0]
    days_since_rebalance = 0
    n_rebalances = 0
    
    for i in range(n_days):
        current_vix = df['vix'].iloc[i]
        
        # Check if should rebalance
        if i == 0 or should_rebalance(
            current_vix, last_rebalance_vix, 
            days_since_rebalance, rebalance_threshold_vix, rebalance_max_days
        ):
            # Rebalance
            hedge_ratios[i] = scaling_func(current_vix)
            hedge_notionals[i] = base_notional * hedge_ratios[i]
            
            # Transaction cost
            if i > 0:
                notional_change = abs(hedge_notionals[i] - hedge_notionals[i-1])
                rebalance_costs[i] = notional_change * hedge_cost_bps / 10000
                n_rebalances += 1
            
            last_rebalance_vix = current_vix
            days_since_rebalance = 0
        else:
            # Maintain previous hedge
            hedge_ratios[i] = hedge_ratios[i-1]
            hedge_notionals[i] = hedge_notionals[i-1]
            days_since_rebalance += 1
        
        # Calculate hedge P&L (simplified: hedge gains when vol rises)
        if i > 0:
            var_change = df['implied_var'].iloc[i] - df['implied_var'].iloc[i-1]
            # Long variance hedge: gains when variance increases
            hedge_pnls[i] = hedge_notionals[i-1] * var_change * 10000  # Convert to points
        
        # Cumulative P&L (portfolio + hedge - costs)
        if i > 0:
            portfolio_pnl = df['portfolio_return'].iloc[i] * base_notional * 100
            cumulative_pnl[i] = cumulative_pnl[i-1] + portfolio_pnl + hedge_pnls[i] - rebalance_costs[i]
        else:
            cumulative_pnl[i] = 0
    
    # Build results DataFrame
    results_df = pd.DataFrame({
        'date': df.index,
        'vix': df['vix'].values,
        'hedge_ratio': hedge_ratios,
        'hedge_notional': hedge_notionals,
        'hedge_pnl': hedge_pnls,
        'rebalance_cost': rebalance_costs,
        'cumulative_pnl': cumulative_pnl
    })
    results_df.set_index('date', inplace=True)
    
    # Calculate summary statistics
    total_hedge_cost = rebalance_costs.sum() + np.sum(hedge_notionals * 0.01 / 252)  # Add VRP cost
    total_hedge_gain = hedge_pnls.sum()
    total_pnl = cumulative_pnl[-1] if len(cumulative_pnl) > 0 else 0
    
    # Sharpe ratio
    daily_pnl = np.diff(cumulative_pnl)
    sharpe = np.mean(daily_pnl) / np.std(daily_pnl) * np.sqrt(252) if np.std(daily_pnl) > 0 else 0
    
    # Max drawdown
    peak = np.maximum.accumulate(cumulative_pnl)
    drawdown = (peak - cumulative_pnl) / (peak + 1e-10)
    max_dd = drawdown.max()
    
    summary = DynamicHedgeResult(
        total_pnl=total_pnl,
        hedge_cost=total_hedge_cost,
        hedge_gain=total_hedge_gain,
        avg_hedge_ratio=np.mean(hedge_ratios),
        max_drawdown=max_dd,
        sharpe_ratio=sharpe,
        n_rebalances=n_rebalances
    )
    
    return results_df, summary


def compare_hedge_strategies(
    portfolio_returns: pd.Series,
    vix_series: pd.Series,
    implied_variance: pd.Series,
    base_notional: float = 1000.0
) -> pd.DataFrame:
    """
    Compare different dynamic hedging strategies.
    
    Parameters
    ----------
    portfolio_returns : pd.Series
        Daily portfolio returns
    vix_series : pd.Series
        VIX levels
    implied_variance : pd.Series
        Implied variance
    base_notional : float
        Base variance notional
    
    Returns
    -------
    pd.DataFrame
        Comparison of strategy performance
    """
    strategies = {
        'Static (100%)': lambda vix: 1.0,
        'Linear VIX': lambda vix: linear_vix_scaling(vix, 12, 22),
        'Sigmoid VIX': lambda vix: sigmoid_vix_scaling(vix, 20, 0.2),
        'Conditional': lambda vix: conditional_hedge_rule(vix, 15, 25),
        'None': lambda vix: 0.0
    }
    
    results = []
    for name, func in strategies.items():
        _, summary = backtest_dynamic_hedge(
            portfolio_returns, vix_series, implied_variance,
            func, base_notional
        )
        results.append({
            'Strategy': name,
            'Total P&L': summary.total_pnl,
            'Hedge Cost': summary.hedge_cost,
            'Hedge Gain': summary.hedge_gain,
            'Avg Hedge %': summary.avg_hedge_ratio * 100,
            'Max DD': summary.max_drawdown * 100,
            'Sharpe': summary.sharpe_ratio,
            'Rebalances': summary.n_rebalances
        })
    
    return pd.DataFrame(results)


# Example usage and demonstration
if __name__ == "__main__":
    print("=" * 60)
    print("Dynamic Volatility Hedge Backtest - Demonstration")
    print("=" * 60)
    
    np.random.seed(42)
    
    # Generate synthetic data
    n_days = 500
    dates = pd.date_range('2023-01-01', periods=n_days, freq='B')
    
    # Simulate VIX (mean-reverting)
    vix = np.zeros(n_days)
    vix[0] = 18
    for i in range(1, n_days):
        vix[i] = vix[i-1] + 0.1 * (18 - vix[i-1]) + np.random.normal(0, 1)
    vix = np.clip(vix, 10, 60)
    vix_series = pd.Series(vix, index=dates)
    
    # Simulate portfolio returns (negative correlation with VIX)
    returns = -0.01 * (vix / 20 - 1) + np.random.normal(0, 0.01, n_days)
    portfolio_returns = pd.Series(returns, index=dates)
    
    # Simulate implied variance
    implied_variance = pd.Series((vix / 100) ** 2, index=dates)
    
    # Example 1: Scaling functions
    print("\n1. Hedge Scaling Functions")
    print("-" * 40)
    test_vix_levels = [10, 15, 20, 25, 30, 40]
    
    print(f"{'VIX':>6} {'Linear':>8} {'Sigmoid':>8} {'Conditional':>12}")
    print("-" * 40)
    for v in test_vix_levels:
        linear = linear_vix_scaling(v)
        sigmoid = sigmoid_vix_scaling(v)
        cond = conditional_hedge_rule(v)
        print(f"{v:>6} {linear:>8.2f} {sigmoid:>8.2f} {cond:>12.2f}")
    
    # Example 2: Rebalancing logic
    print("\n2. Rebalancing Decision Logic")
    print("-" * 40)
    scenarios = [
        (20, 18, 3, "VIX +2, 3 days"),
        (20, 16, 3, "VIX +4, 3 days"),
        (20, 19, 8, "VIX +1, 8 days"),
        (20, 20, 5, "No change, 5 days"),
    ]
    
    for vix_curr, vix_last, days, desc in scenarios:
        rebal = should_rebalance(vix_curr, vix_last, days)
        print(f"{desc}: {'REBALANCE' if rebal else 'HOLD'}")
    
    # Example 3: Backtest comparison
    print("\n3. Strategy Comparison")
    print("-" * 40)
    comparison = compare_hedge_strategies(
        portfolio_returns, vix_series, implied_variance,
        base_notional=1000
    )
    
    print(comparison.to_string(index=False))
    
    # Example 4: Detailed backtest
    print("\n4. Detailed Linear VIX Hedge Backtest")
    print("-" * 40)
    
    results_df, summary = backtest_dynamic_hedge(
        portfolio_returns, vix_series, implied_variance,
        lambda v: linear_vix_scaling(v, 12, 22),
        base_notional=1000
    )
    
    print(f"Total P&L:        ${summary.total_pnl:,.0f}")
    print(f"Hedge Cost:       ${summary.hedge_cost:,.0f}")
    print(f"Hedge Gain:       ${summary.hedge_gain:,.0f}")
    print(f"Avg Hedge Ratio:  {summary.avg_hedge_ratio:.1%}")
    print(f"Max Drawdown:     {summary.max_drawdown:.1%}")
    print(f"Sharpe Ratio:     {summary.sharpe_ratio:.2f}")
    print(f"Rebalances:       {summary.n_rebalances}")
