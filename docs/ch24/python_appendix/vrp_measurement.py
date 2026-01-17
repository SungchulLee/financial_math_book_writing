"""
Variance Risk Premium (VRP) Measurement Module

This module implements VRP measurement and forecasting:
- HAR-RV model for realized variance forecasting
- VRP time series construction
- VRP decomposition analysis
- Dynamic scaling rules

Author: Chapter 24 - Variance and Volatility
"""

import numpy as np
import pandas as pd
from typing import Tuple, Dict, Optional
from dataclasses import dataclass
import warnings


@dataclass
class HARRVParams:
    """Parameters for HAR-RV model."""
    alpha: float      # Intercept
    beta_d: float     # Daily RV coefficient
    beta_w: float     # Weekly RV coefficient
    beta_m: float     # Monthly RV coefficient
    r_squared: float  # Model R-squared


def calculate_realized_variance(
    returns: np.ndarray,
    annualization: int = 252
) -> float:
    """
    Calculate realized variance from returns.
    
    RV = (252/n) × Σ r_i²
    """
    n = len(returns)
    return (annualization / n) * np.sum(returns ** 2)


def calculate_realized_variance_series(
    returns: pd.Series,
    window: int = 22,
    annualization: int = 252
) -> pd.Series:
    """
    Calculate rolling realized variance series.
    
    Parameters
    ----------
    returns : pd.Series
        Daily returns
    window : int
        Rolling window (default: 22 days = 1 month)
    annualization : int
        Annualization factor
    
    Returns
    -------
    pd.Series
        Rolling realized variance
    """
    squared_returns = returns ** 2
    rv = squared_returns.rolling(window=window).sum() * (annualization / window)
    return rv


def calculate_har_components(rv_series: pd.Series) -> pd.DataFrame:
    """
    Calculate HAR-RV model components (daily, weekly, monthly averages).
    
    Parameters
    ----------
    rv_series : pd.Series
        Daily realized variance series
    
    Returns
    -------
    pd.DataFrame
        DataFrame with columns: RV_d, RV_w, RV_m
    """
    df = pd.DataFrame(index=rv_series.index)
    
    # Daily RV (most recent)
    df['RV_d'] = rv_series
    
    # Weekly RV (5-day average)
    df['RV_w'] = rv_series.rolling(window=5).mean()
    
    # Monthly RV (22-day average)
    df['RV_m'] = rv_series.rolling(window=22).mean()
    
    return df


def fit_har_rv_model(
    rv_series: pd.Series,
    forecast_horizon: int = 22
) -> HARRVParams:
    """
    Fit HAR-RV model to realized variance series.
    
    Model: RV_{t+h} = α + β_d RV_t + β_w RV^(w)_t + β_m RV^(m)_t + ε
    
    Parameters
    ----------
    rv_series : pd.Series
        Daily realized variance series
    forecast_horizon : int
        Forecast horizon (default: 22 days = 1 month)
    
    Returns
    -------
    HARRVParams
        Fitted model parameters
    """
    # Calculate HAR components
    har_df = calculate_har_components(rv_series)
    
    # Calculate forward realized variance (target)
    har_df['RV_future'] = rv_series.shift(-forecast_horizon)
    
    # Drop missing values
    har_df = har_df.dropna()
    
    if len(har_df) < 100:
        warnings.warn("Insufficient data for reliable HAR-RV estimation")
    
    # OLS regression
    X = har_df[['RV_d', 'RV_w', 'RV_m']].values
    X = np.column_stack([np.ones(len(X)), X])  # Add intercept
    y = har_df['RV_future'].values
    
    # Solve normal equations: β = (X'X)^(-1) X'y
    try:
        beta = np.linalg.lstsq(X, y, rcond=None)[0]
    except np.linalg.LinAlgError:
        warnings.warn("Singular matrix in HAR-RV estimation")
        return HARRVParams(alpha=0, beta_d=0.33, beta_w=0.33, beta_m=0.33, r_squared=0)
    
    # Calculate R-squared
    y_pred = X @ beta
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
    
    return HARRVParams(
        alpha=beta[0],
        beta_d=beta[1],
        beta_w=beta[2],
        beta_m=beta[3],
        r_squared=r_squared
    )


def forecast_realized_variance(
    rv_d: float,
    rv_w: float,
    rv_m: float,
    params: HARRVParams
) -> float:
    """
    Forecast realized variance using HAR-RV model.
    
    Parameters
    ----------
    rv_d : float
        Daily (most recent) realized variance
    rv_w : float
        Weekly average realized variance
    rv_m : float
        Monthly average realized variance
    params : HARRVParams
        Fitted model parameters
    
    Returns
    -------
    float
        Forecasted realized variance
    """
    return (params.alpha + 
            params.beta_d * rv_d + 
            params.beta_w * rv_w + 
            params.beta_m * rv_m)


def calculate_vrp_series(
    implied_variance: pd.Series,
    returns: pd.Series,
    rv_window: int = 22,
    method: str = 'ex_post'
) -> pd.Series:
    """
    Calculate variance risk premium time series.
    
    Parameters
    ----------
    implied_variance : pd.Series
        Implied variance from options (e.g., VIX²)
    returns : pd.Series
        Daily returns
    rv_window : int
        Window for realized variance calculation
    method : str
        'ex_post' (using actual future RV) or 'har_rv' (using HAR forecast)
    
    Returns
    -------
    pd.Series
        VRP time series
    """
    rv_series = calculate_realized_variance_series(returns, window=rv_window)
    
    if method == 'ex_post':
        # VRP_t = IV²_t - RV_{t,t+τ}
        future_rv = rv_series.shift(-rv_window)
        vrp = implied_variance - future_rv
    
    elif method == 'har_rv':
        # VRP_t = IV²_t - E[RV]
        params = fit_har_rv_model(rv_series, forecast_horizon=rv_window)
        har_components = calculate_har_components(rv_series)
        
        forecasted_rv = pd.Series(index=rv_series.index, dtype=float)
        for date in rv_series.dropna().index:
            if date in har_components.index:
                row = har_components.loc[date]
                if not any(pd.isna([row['RV_d'], row['RV_w'], row['RV_m']])):
                    forecasted_rv[date] = forecast_realized_variance(
                        row['RV_d'], row['RV_w'], row['RV_m'], params
                    )
        
        vrp = implied_variance - forecasted_rv
    
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return vrp


def vrp_based_position_sizing(
    vrp: float,
    vix: float,
    base_notional: float,
    vrp_threshold: float = 100,
    vix_cap: float = 25
) -> float:
    """
    Calculate position size based on VRP and VIX.
    
    Parameters
    ----------
    vrp : float
        Current variance risk premium
    vix : float
        Current VIX level
    base_notional : float
        Base position notional
    vrp_threshold : float
        Minimum VRP to trade
    vix_cap : float
        VIX level above which to reduce/exit
    
    Returns
    -------
    float
        Adjusted position notional
    """
    # VIX-based scaling
    vix_scale = max(0, min(1, (vix_cap - vix) / 10))
    
    # VRP-based scaling (more aggressive when VRP high)
    vrp_scale = max(0, min(2, vrp / vrp_threshold))
    
    # Combined scaling
    combined_scale = vix_scale * vrp_scale
    
    return base_notional * combined_scale


def analyze_vrp_statistics(vrp_series: pd.Series) -> Dict:
    """
    Analyze VRP time series statistics.
    
    Parameters
    ----------
    vrp_series : pd.Series
        VRP time series
    
    Returns
    -------
    Dict
        Dictionary with VRP statistics
    """
    vrp_clean = vrp_series.dropna()
    
    return {
        'mean': vrp_clean.mean(),
        'median': vrp_clean.median(),
        'std': vrp_clean.std(),
        'min': vrp_clean.min(),
        'max': vrp_clean.max(),
        'pct_positive': (vrp_clean > 0).mean() * 100,
        'sharpe': vrp_clean.mean() / vrp_clean.std() if vrp_clean.std() > 0 else 0,
        'skewness': vrp_clean.skew(),
        'kurtosis': vrp_clean.kurtosis(),
        'count': len(vrp_clean)
    }


def calculate_vrp_by_vix_regime(
    vrp_series: pd.Series,
    vix_series: pd.Series
) -> Dict:
    """
    Analyze VRP by VIX regime.
    
    Parameters
    ----------
    vrp_series : pd.Series
        VRP time series
    vix_series : pd.Series
        VIX time series
    
    Returns
    -------
    Dict
        VRP statistics by VIX regime
    """
    # Align series
    df = pd.DataFrame({'vrp': vrp_series, 'vix': vix_series}).dropna()
    
    results = {}
    
    # Low VIX regime (< 15)
    mask_low = df['vix'] < 15
    if mask_low.any():
        results['low_vix'] = {
            'vix_range': '<15',
            'mean_vrp': df.loc[mask_low, 'vrp'].mean(),
            'pct_positive': (df.loc[mask_low, 'vrp'] > 0).mean() * 100,
            'count': mask_low.sum()
        }
    
    # Medium VIX regime (15-25)
    mask_med = (df['vix'] >= 15) & (df['vix'] < 25)
    if mask_med.any():
        results['medium_vix'] = {
            'vix_range': '15-25',
            'mean_vrp': df.loc[mask_med, 'vrp'].mean(),
            'pct_positive': (df.loc[mask_med, 'vrp'] > 0).mean() * 100,
            'count': mask_med.sum()
        }
    
    # High VIX regime (>= 25)
    mask_high = df['vix'] >= 25
    if mask_high.any():
        results['high_vix'] = {
            'vix_range': '>=25',
            'mean_vrp': df.loc[mask_high, 'vrp'].mean(),
            'pct_positive': (df.loc[mask_high, 'vrp'] > 0).mean() * 100,
            'count': mask_high.sum()
        }
    
    return results


# Example usage and demonstration
if __name__ == "__main__":
    print("=" * 60)
    print("Variance Risk Premium Measurement - Demonstration")
    print("=" * 60)
    
    np.random.seed(42)
    
    # Generate synthetic data
    n_days = 500
    dates = pd.date_range('2023-01-01', periods=n_days, freq='B')
    
    # Simulate returns with volatility clustering
    vol = np.zeros(n_days)
    vol[0] = 0.15
    for i in range(1, n_days):
        vol[i] = 0.02 + 0.85 * vol[i-1] + 0.10 * np.abs(np.random.normal(0, 0.01))
    
    returns = pd.Series(
        np.random.normal(0, 1, n_days) * vol / np.sqrt(252),
        index=dates
    )
    
    # Simulate implied variance (with VRP)
    rv_series = calculate_realized_variance_series(returns, window=22)
    vrp_true = 100 + 50 * np.random.uniform(-1, 1, n_days)  # VRP varies
    implied_variance = pd.Series(
        rv_series.values + vrp_true / 10000,  # Add VRP
        index=dates
    )
    implied_variance = implied_variance.clip(lower=0.01)  # Ensure positive
    
    # Example 1: HAR-RV model fitting
    print("\n1. HAR-RV Model Fitting")
    print("-" * 40)
    rv_daily = calculate_realized_variance_series(returns, window=1)
    params = fit_har_rv_model(rv_daily.dropna(), forecast_horizon=22)
    
    print(f"HAR-RV Model Parameters:")
    print(f"  α (intercept):  {params.alpha:.6f}")
    print(f"  β_d (daily):    {params.beta_d:.4f}")
    print(f"  β_w (weekly):   {params.beta_w:.4f}")
    print(f"  β_m (monthly):  {params.beta_m:.4f}")
    print(f"  R²:             {params.r_squared:.2%}")
    
    # Example 2: Forecast realized variance
    print("\n2. HAR-RV Forecast Example")
    print("-" * 40)
    rv_d = 0.0256  # 16% vol (daily estimate)
    rv_w = 0.0225  # 15% vol (weekly avg)
    rv_m = 0.0196  # 14% vol (monthly avg)
    
    forecast = forecast_realized_variance(rv_d, rv_w, rv_m, params)
    print(f"Inputs:")
    print(f"  Daily RV:   {rv_d*10000:.0f} ({np.sqrt(rv_d)*100:.1f}% vol)")
    print(f"  Weekly RV:  {rv_w*10000:.0f} ({np.sqrt(rv_w)*100:.1f}% vol)")
    print(f"  Monthly RV: {rv_m*10000:.0f} ({np.sqrt(rv_m)*100:.1f}% vol)")
    print(f"\nForecast RV: {forecast*10000:.0f} ({np.sqrt(forecast)*100:.1f}% vol)")
    
    # Example 3: VRP calculation
    print("\n3. VRP Calculation")
    print("-" * 40)
    vrp_series = calculate_vrp_series(implied_variance, returns, method='ex_post')
    stats = analyze_vrp_statistics(vrp_series * 10000)  # Convert to variance points
    
    print(f"VRP Statistics (variance points):")
    print(f"  Mean:         {stats['mean']:.1f}")
    print(f"  Median:       {stats['median']:.1f}")
    print(f"  Std:          {stats['std']:.1f}")
    print(f"  % Positive:   {stats['pct_positive']:.1f}%")
    print(f"  Sharpe:       {stats['sharpe']:.2f}")
    
    # Example 4: Position sizing
    print("\n4. VRP-Based Position Sizing")
    print("-" * 40)
    base = 100000
    
    scenarios = [
        (150, 12, "Low VIX, High VRP"),
        (100, 18, "Medium VIX, Normal VRP"),
        (50, 28, "High VIX, Low VRP"),
        (-100, 35, "Very High VIX, Negative VRP")
    ]
    
    for vrp, vix, desc in scenarios:
        position = vrp_based_position_sizing(vrp, vix, base)
        print(f"{desc}:")
        print(f"  VRP={vrp:+4.0f}, VIX={vix:2.0f} → Notional=${position:,.0f} ({position/base:.0%})")
