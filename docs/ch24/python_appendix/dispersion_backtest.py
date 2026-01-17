"""
Dispersion Trading Backtest Module

This module implements tools for backtesting dispersion trading strategies:
- Historical correlation analysis (implied vs realized)
- Dispersion trade P&L simulation
- Gaussian copula approximation for quick sizing
- Correlation swap pricing

Author: Chapter 24 - Variance and Volatility
"""

import numpy as np
import pandas as pd
from typing import Tuple, List, Dict, Optional
from dataclasses import dataclass


@dataclass
class DispersionTradeSpec:
    """Specification for a dispersion trade."""
    index_name: str
    stock_names: List[str]
    stock_weights: np.ndarray
    index_vol_strike: float
    stock_vol_strikes: np.ndarray
    index_notional: float
    stock_notionals: np.ndarray
    maturity_days: int
    hedge_ratio: float = 0.70


def calculate_average_correlation(corr_matrix: pd.DataFrame) -> float:
    """
    Calculate average pairwise correlation from correlation matrix.
    """
    n = len(corr_matrix)
    upper_triangle = np.triu(corr_matrix.values, k=1)
    n_pairs = n * (n - 1) / 2
    if n_pairs == 0:
        return 0.0
    avg_corr = upper_triangle.sum() / n_pairs
    return avg_corr


def calculate_implied_correlation(
    index_implied_vol: float,
    stock_implied_vols: np.ndarray,
    weights: np.ndarray
) -> float:
    """
    Back out implied correlation from index and stock volatilities.
    
    ρ = (σ_index² - Σ w_i² σ_i²) / (2 Σ_{i<j} w_i w_j σ_i σ_j)
    """
    index_var = index_implied_vol ** 2
    variance_term = np.sum(weights ** 2 * stock_implied_vols ** 2)
    
    n = len(weights)
    cov_term = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            cov_term += 2 * weights[i] * weights[j] * stock_implied_vols[i] * stock_implied_vols[j]
    
    if cov_term == 0:
        return 0.0
    
    implied_corr = (index_var - variance_term) / cov_term
    return max(-1.0, min(1.0, implied_corr))


def gaussian_copula_index_vol(
    avg_stock_vol: float,
    avg_correlation: float,
    n_stocks: int
) -> float:
    """
    Approximate index volatility using Gaussian copula formula.
    
    σ_index ≈ σ̄ × √(ρ̄ + (1-ρ̄)/N)
    """
    return avg_stock_vol * np.sqrt(avg_correlation + (1 - avg_correlation) / n_stocks)


def calculate_correlation_swap_strike(
    index_implied_vol: float,
    stock_implied_vols: np.ndarray,
    weights: np.ndarray
) -> float:
    """Calculate fair strike for a correlation swap."""
    return calculate_implied_correlation(index_implied_vol, stock_implied_vols, weights)


def simulate_dispersion_trade_pnl(
    index_returns: np.ndarray,
    stock_returns: np.ndarray,
    trade_spec: DispersionTradeSpec,
    annualization: int = 252
) -> Dict:
    """Simulate P&L for a dispersion trade."""
    n_days = len(index_returns)
    n_stocks = stock_returns.shape[1]
    
    # Calculate realized variances
    index_rv = (annualization / n_days) * np.sum(index_returns ** 2)
    stock_rvs = np.array([
        (annualization / n_days) * np.sum(stock_returns[:, i] ** 2)
        for i in range(n_stocks)
    ])
    
    # Convert to variance points
    index_rv_points = index_rv * 10000
    stock_rv_points = stock_rvs * 10000
    index_strike_points = (trade_spec.index_vol_strike ** 2) * 10000
    stock_strike_points = (trade_spec.stock_vol_strikes ** 2) * 10000
    
    # P&L calculation
    index_pnl = trade_spec.index_notional * (index_strike_points - index_rv_points)
    stock_pnls = trade_spec.stock_notionals * (stock_rv_points - stock_strike_points)
    total_stock_pnl = np.sum(stock_pnls)
    net_pnl = index_pnl + total_stock_pnl
    
    # Calculate realized correlation
    if n_stocks > 1:
        corr_matrix = np.corrcoef(stock_returns.T)
        avg_realized_corr = calculate_average_correlation(pd.DataFrame(corr_matrix))
    else:
        avg_realized_corr = 1.0
    
    implied_corr = calculate_implied_correlation(
        trade_spec.index_vol_strike,
        trade_spec.stock_vol_strikes,
        trade_spec.stock_weights
    )
    
    return {
        'index_realized_vol': np.sqrt(index_rv) * 100,
        'index_strike_vol': trade_spec.index_vol_strike * 100,
        'stock_realized_vol_avg': np.sqrt(np.mean(stock_rvs)) * 100,
        'stock_strike_vol_avg': np.mean(trade_spec.stock_vol_strikes) * 100,
        'index_pnl': index_pnl,
        'stock_pnl': total_stock_pnl,
        'net_pnl': net_pnl,
        'realized_correlation': avg_realized_corr,
        'implied_correlation': implied_corr,
        'correlation_gap': implied_corr - avg_realized_corr,
        'n_days': n_days
    }


def correlation_regime_analysis(
    realized_correlations: np.ndarray,
    vix_levels: np.ndarray
) -> Dict:
    """Analyze correlation regimes based on VIX levels."""
    normal_mask = vix_levels < 20
    elevated_mask = (vix_levels >= 20) & (vix_levels < 30)
    crisis_mask = vix_levels >= 30
    
    results = {
        'normal': {
            'vix_range': '<20',
            'avg_correlation': np.mean(realized_correlations[normal_mask]) if normal_mask.any() else np.nan,
            'std_correlation': np.std(realized_correlations[normal_mask]) if normal_mask.any() else np.nan,
            'count': int(normal_mask.sum())
        },
        'elevated': {
            'vix_range': '20-30',
            'avg_correlation': np.mean(realized_correlations[elevated_mask]) if elevated_mask.any() else np.nan,
            'std_correlation': np.std(realized_correlations[elevated_mask]) if elevated_mask.any() else np.nan,
            'count': int(elevated_mask.sum())
        },
        'crisis': {
            'vix_range': '>=30',
            'avg_correlation': np.mean(realized_correlations[crisis_mask]) if crisis_mask.any() else np.nan,
            'std_correlation': np.std(realized_correlations[crisis_mask]) if crisis_mask.any() else np.nan,
            'count': int(crisis_mask.sum())
        }
    }
    return results


if __name__ == "__main__":
    print("=" * 60)
    print("Dispersion Trading Backtest - Demonstration")
    print("=" * 60)
    
    np.random.seed(42)
    
    # Example 1: Gaussian copula approximation
    print("\n1. Gaussian Copula Approximation")
    print("-" * 40)
    approx_vol = gaussian_copula_index_vol(0.30, 0.50, 20)
    print(f"Average stock vol: 30%, Avg corr: 50%, N=20")
    print(f"Approximate index vol: {approx_vol:.2%}")
    print(f"Dispersion ratio: {0.30 / approx_vol:.2f}x")
    
    # Example 2: Implied correlation
    print("\n2. Implied Correlation")
    print("-" * 40)
    imp_corr = calculate_implied_correlation(
        0.18, np.array([0.25, 0.30, 0.28]), np.array([0.4, 0.35, 0.25])
    )
    print(f"Index vol: 18%, Stock vols: [25%, 30%, 28%]")
    print(f"Implied correlation: {imp_corr:.1%}")
    
    # Example 3: Dispersion trade simulation
    print("\n3. Dispersion Trade Simulation")
    print("-" * 40)
    n_days, n_stocks = 63, 10
    
    true_corr = 0.40
    cov = true_corr * np.ones((n_stocks, n_stocks)) + (1-true_corr) * np.eye(n_stocks)
    cov *= (0.30/np.sqrt(252))**2
    
    stock_returns = np.random.multivariate_normal(np.zeros(n_stocks), cov, n_days)
    index_returns = stock_returns @ (np.ones(n_stocks)/n_stocks)
    
    spec = DispersionTradeSpec(
        index_name='SPX',
        stock_names=[f'S{i}' for i in range(n_stocks)],
        stock_weights=np.ones(n_stocks)/n_stocks,
        index_vol_strike=0.18,
        stock_vol_strikes=np.full(n_stocks, 0.30),
        index_notional=1000,
        stock_notionals=np.full(n_stocks, 70),
        maturity_days=63
    )
    
    result = simulate_dispersion_trade_pnl(index_returns, stock_returns, spec)
    print(f"Index: Strike {result['index_strike_vol']:.0f}%, Realized {result['index_realized_vol']:.1f}%")
    print(f"Stocks: Strike {result['stock_strike_vol_avg']:.0f}%, Realized {result['stock_realized_vol_avg']:.1f}%")
    print(f"Correlation: Implied {result['implied_correlation']:.0%}, Realized {result['realized_correlation']:.0%}")
    print(f"Net P&L: ${result['net_pnl']:,.0f}")
