"""
Correlation Analysis Module

This module implements tools for implied vs realized correlation tracking:
- Rolling correlation calculation
- Implied correlation extraction
- Correlation regime classification
- VIX-correlation relationship analysis

Author: Chapter 24 - Variance and Volatility
"""

import numpy as np
import pandas as pd
from typing import Tuple, Dict, List, Optional
from dataclasses import dataclass


@dataclass
class CorrelationRegime:
    """Classification of correlation regime."""
    regime: str  # 'normal', 'elevated', 'crisis'
    correlation: float
    vix_level: float
    description: str


def calculate_rolling_correlation(
    returns1: pd.Series,
    returns2: pd.Series,
    window: int = 20
) -> pd.Series:
    """
    Calculate rolling correlation between two return series.
    
    Parameters
    ----------
    returns1 : pd.Series
        First return series
    returns2 : pd.Series
        Second return series
    window : int
        Rolling window in days
    
    Returns
    -------
    pd.Series
        Rolling correlation
    """
    return returns1.rolling(window=window).corr(returns2)


def calculate_average_pairwise_correlation(
    returns_df: pd.DataFrame,
    window: int = 20
) -> pd.Series:
    """
    Calculate rolling average pairwise correlation for a basket.
    
    Parameters
    ----------
    returns_df : pd.DataFrame
        DataFrame with columns as different assets
    window : int
        Rolling window
    
    Returns
    -------
    pd.Series
        Average pairwise correlation over time
    """
    n_assets = len(returns_df.columns)
    n_pairs = n_assets * (n_assets - 1) / 2
    
    result = pd.Series(index=returns_df.index, dtype=float)
    
    for i in range(window, len(returns_df)):
        window_data = returns_df.iloc[i-window:i]
        corr_matrix = window_data.corr()
        
        # Extract upper triangle (excluding diagonal)
        upper_tri = np.triu(corr_matrix.values, k=1)
        avg_corr = upper_tri.sum() / n_pairs if n_pairs > 0 else 0
        result.iloc[i] = avg_corr
    
    return result


def calculate_implied_correlation_series(
    index_iv: pd.Series,
    stock_ivs: pd.DataFrame,
    weights: np.ndarray
) -> pd.Series:
    """
    Calculate implied correlation time series.
    
    ρ_implied = (σ_index² - Σ w_i² σ_i²) / (2 Σ_{i<j} w_i w_j σ_i σ_j)
    
    Parameters
    ----------
    index_iv : pd.Series
        Index implied volatility time series
    stock_ivs : pd.DataFrame
        Stock implied volatilities (columns = stocks)
    weights : np.ndarray
        Index weights
    
    Returns
    -------
    pd.Series
        Implied correlation series
    """
    result = pd.Series(index=index_iv.index, dtype=float)
    n_stocks = len(weights)
    
    for date in index_iv.index:
        if date not in stock_ivs.index:
            continue
            
        idx_var = index_iv[date] ** 2
        stock_vols = stock_ivs.loc[date].values
        
        # Variance term
        var_term = np.sum(weights ** 2 * stock_vols ** 2)
        
        # Covariance term
        cov_term = 0.0
        for i in range(n_stocks):
            for j in range(i + 1, n_stocks):
                cov_term += 2 * weights[i] * weights[j] * stock_vols[i] * stock_vols[j]
        
        if cov_term > 0:
            impl_corr = (idx_var - var_term) / cov_term
            result[date] = max(-1, min(1, impl_corr))
    
    return result


def classify_correlation_regime(
    correlation: float,
    vix: float
) -> CorrelationRegime:
    """
    Classify current correlation regime.
    
    Parameters
    ----------
    correlation : float
        Current realized correlation
    vix : float
        Current VIX level
    
    Returns
    -------
    CorrelationRegime
        Regime classification
    """
    if vix >= 30 or correlation >= 0.70:
        return CorrelationRegime(
            regime='crisis',
            correlation=correlation,
            vix_level=vix,
            description='High correlation, elevated systemic risk'
        )
    elif vix >= 20 or correlation >= 0.55:
        return CorrelationRegime(
            regime='elevated',
            correlation=correlation,
            vix_level=vix,
            description='Above-normal correlation, increased caution'
        )
    else:
        return CorrelationRegime(
            regime='normal',
            correlation=correlation,
            vix_level=vix,
            description='Normal correlation, dispersion opportunities'
        )


def estimate_vix_correlation_relationship(
    vix_series: pd.Series,
    correlation_series: pd.Series
) -> Dict:
    """
    Estimate the empirical VIX-correlation relationship.
    
    Model: ρ = α + β × VIX
    
    Parameters
    ----------
    vix_series : pd.Series
        VIX levels
    correlation_series : pd.Series
        Realized correlations
    
    Returns
    -------
    Dict
        Regression coefficients and statistics
    """
    # Align series
    df = pd.DataFrame({'vix': vix_series, 'corr': correlation_series}).dropna()
    
    if len(df) < 30:
        return {'alpha': 0.15, 'beta': 0.015, 'r_squared': 0, 'n_obs': len(df)}
    
    # OLS regression
    X = np.column_stack([np.ones(len(df)), df['vix'].values])
    y = df['corr'].values
    
    try:
        beta = np.linalg.lstsq(X, y, rcond=None)[0]
    except:
        return {'alpha': 0.15, 'beta': 0.015, 'r_squared': 0, 'n_obs': len(df)}
    
    # R-squared
    y_pred = X @ beta
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
    
    return {
        'alpha': beta[0],
        'beta': beta[1],
        'r_squared': r_squared,
        'n_obs': len(df)
    }


def predict_correlation_from_vix(
    vix: float,
    alpha: float = 0.15,
    beta: float = 0.015
) -> float:
    """
    Predict correlation from VIX using linear model.
    
    ρ_predicted = α + β × VIX
    
    Parameters
    ----------
    vix : float
        VIX level
    alpha : float
        Intercept (correlation when VIX = 0)
    beta : float
        Slope (correlation increase per VIX point)
    
    Returns
    -------
    float
        Predicted correlation
    """
    pred = alpha + beta * vix
    return max(0, min(1, pred))  # Bound to [0, 1]


def calculate_correlation_term_structure(
    returns_df: pd.DataFrame,
    horizons: List[int] = [5, 10, 22, 44, 66]
) -> pd.DataFrame:
    """
    Calculate correlation at different time horizons.
    
    Parameters
    ----------
    returns_df : pd.DataFrame
        Asset returns
    horizons : List[int]
        List of windows (in days) to compute correlation
    
    Returns
    -------
    pd.DataFrame
        Average correlation at each horizon
    """
    results = {}
    
    for horizon in horizons:
        corr_series = calculate_average_pairwise_correlation(returns_df, window=horizon)
        results[f'{horizon}d'] = corr_series.mean()
    
    return pd.DataFrame([results])


def analyze_correlation_gap(
    implied_correlation: pd.Series,
    realized_correlation: pd.Series
) -> Dict:
    """
    Analyze the gap between implied and realized correlation.
    
    Parameters
    ----------
    implied_correlation : pd.Series
        Implied correlation series
    realized_correlation : pd.Series
        Realized correlation series
    
    Returns
    -------
    Dict
        Gap statistics
    """
    # Align series
    df = pd.DataFrame({
        'implied': implied_correlation,
        'realized': realized_correlation
    }).dropna()
    
    gap = df['implied'] - df['realized']
    
    return {
        'mean_gap': gap.mean(),
        'median_gap': gap.median(),
        'std_gap': gap.std(),
        'pct_positive': (gap > 0).mean() * 100,
        'max_gap': gap.max(),
        'min_gap': gap.min(),
        'implied_mean': df['implied'].mean(),
        'realized_mean': df['realized'].mean(),
        'correlation_of_series': df['implied'].corr(df['realized']),
        'n_obs': len(df)
    }


def generate_correlation_trading_signal(
    implied_corr: float,
    realized_corr: float,
    vix: float,
    threshold_gap: float = 0.10,
    max_vix: float = 30
) -> Dict:
    """
    Generate correlation trading signal.
    
    Parameters
    ----------
    implied_corr : float
        Current implied correlation
    realized_corr : float
        Current realized correlation
    vix : float
        Current VIX level
    threshold_gap : float
        Minimum gap to generate signal
    max_vix : float
        VIX above which to avoid correlation trades
    
    Returns
    -------
    Dict
        Trading signal and rationale
    """
    gap = implied_corr - realized_corr
    
    if vix >= max_vix:
        return {
            'signal': 'FLAT',
            'strength': 0,
            'rationale': f'VIX too high ({vix:.0f}), avoid correlation exposure'
        }
    
    if gap > threshold_gap:
        strength = min(1.0, gap / 0.20)
        return {
            'signal': 'SHORT_CORRELATION',  # Dispersion trade
            'strength': strength,
            'rationale': f'Implied ({implied_corr:.0%}) > Realized ({realized_corr:.0%}) by {gap:.0%}'
        }
    elif gap < -threshold_gap:
        strength = min(1.0, -gap / 0.20)
        return {
            'signal': 'LONG_CORRELATION',  # Reverse dispersion
            'strength': strength,
            'rationale': f'Implied ({implied_corr:.0%}) < Realized ({realized_corr:.0%}) by {-gap:.0%}'
        }
    else:
        return {
            'signal': 'NEUTRAL',
            'strength': 0,
            'rationale': f'Gap too small ({gap:.0%}), no clear opportunity'
        }


# Example usage and demonstration
if __name__ == "__main__":
    print("=" * 60)
    print("Correlation Analysis - Demonstration")
    print("=" * 60)
    
    np.random.seed(42)
    
    # Generate synthetic data
    n_days = 252
    n_stocks = 10
    dates = pd.date_range('2024-01-01', periods=n_days, freq='B')
    
    # Simulate correlated returns
    true_corr = 0.45
    cov = true_corr * np.ones((n_stocks, n_stocks)) + (1 - true_corr) * np.eye(n_stocks)
    cov *= (0.25 / np.sqrt(252)) ** 2
    
    stock_returns = pd.DataFrame(
        np.random.multivariate_normal(np.zeros(n_stocks), cov, n_days),
        index=dates,
        columns=[f'Stock{i}' for i in range(n_stocks)]
    )
    
    # Simulate VIX
    vix = 15 + 5 * np.sin(np.linspace(0, 4*np.pi, n_days)) + np.random.normal(0, 2, n_days)
    vix = np.clip(vix, 10, 40)
    vix_series = pd.Series(vix, index=dates)
    
    # Example 1: Rolling correlation
    print("\n1. Rolling Average Correlation")
    print("-" * 40)
    avg_corr = calculate_average_pairwise_correlation(stock_returns, window=20)
    print(f"True correlation: {true_corr:.0%}")
    print(f"Mean realized correlation: {avg_corr.mean():.1%}")
    print(f"Std realized correlation: {avg_corr.std():.1%}")
    print(f"Min/Max: {avg_corr.min():.1%} / {avg_corr.max():.1%}")
    
    # Example 2: VIX-correlation relationship
    print("\n2. VIX-Correlation Relationship")
    print("-" * 40)
    
    # Estimate relationship
    relationship = estimate_vix_correlation_relationship(vix_series, avg_corr)
    print(f"Model: ρ = {relationship['alpha']:.3f} + {relationship['beta']:.4f} × VIX")
    print(f"R-squared: {relationship['r_squared']:.2%}")
    
    # Predictions
    print(f"\nPredictions:")
    for v in [12, 18, 25, 35]:
        pred = predict_correlation_from_vix(v, relationship['alpha'], relationship['beta'])
        print(f"  VIX = {v}: Predicted ρ = {pred:.1%}")
    
    # Example 3: Regime classification
    print("\n3. Correlation Regime Classification")
    print("-" * 40)
    
    scenarios = [
        (0.35, 15),
        (0.55, 22),
        (0.75, 40),
        (0.80, 25)
    ]
    
    for corr, v in scenarios:
        regime = classify_correlation_regime(corr, v)
        print(f"ρ={corr:.0%}, VIX={v}: {regime.regime.upper()} - {regime.description}")
    
    # Example 4: Trading signals
    print("\n4. Correlation Trading Signals")
    print("-" * 40)
    
    signal_scenarios = [
        (0.55, 0.35, 18, "Implied high, realized low"),
        (0.35, 0.50, 18, "Implied low, realized high"),
        (0.45, 0.42, 18, "Small gap"),
        (0.60, 0.40, 35, "High VIX")
    ]
    
    for impl, real, v, desc in signal_scenarios:
        signal = generate_correlation_trading_signal(impl, real, v)
        print(f"\n{desc}:")
        print(f"  Implied: {impl:.0%}, Realized: {real:.0%}, VIX: {v}")
        print(f"  Signal: {signal['signal']}")
        print(f"  Rationale: {signal['rationale']}")
    
    # Example 5: Correlation term structure
    print("\n5. Correlation Term Structure")
    print("-" * 40)
    term_struct = calculate_correlation_term_structure(stock_returns)
    print(term_struct.to_string(index=False))
