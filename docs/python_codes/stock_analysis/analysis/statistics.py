# ============================================================================
# stock_analysis/analysis/statistics.py
# ============================================================================
import numpy as np
import pandas as pd
from typing import Dict, Optional

def annualize_statistics(returns: pd.Series, trading_days: int = 252) -> Dict[str, float]:
    """
    Compute annualized mean and standard deviation.
    
    Args:
        returns: Series of daily returns
        trading_days: Number of trading days per year
    
    Returns:
        Dictionary with annualized statistics
    """
    return {
        'mu': returns.mean() * trading_days,
        'sigma': returns.std() * np.sqrt(trading_days),
        'daily_mu': returns.mean(),
        'daily_sigma': returns.std()
    }

def compute_mu_and_sigma(df: pd.DataFrame, trading_days: int = 252) -> Dict[str, Dict[str, float]]:
    """
    Compute annualized mean and standard deviation for both return types.
    
    Args:
        df: DataFrame with 'Return' and 'Return_Log' columns
        trading_days: Number of trading days per year
    
    Returns:
        Dictionary with statistics for both return types
    """
    result = {}
    
    if 'Return' in df.columns:
        result['arithmetic'] = annualize_statistics(df['Return'], trading_days)
    
    if 'Return_Log' in df.columns:
        result['logarithmic'] = annualize_statistics(df['Return_Log'], trading_days)
    
    return result


def compute_rolling_stats(df: pd.DataFrame, window: int = 21, 
                         return_col: str = 'Return') -> pd.DataFrame:
    """
    Compute rolling statistics over a specified window.
    
    Args:
        df: DataFrame with return column
        window: Rolling window size
        return_col: Name of the return column
    
    Returns:
        DataFrame with additional rolling statistics columns
    """
    df_copy = df.copy()
    
    if return_col not in df_copy.columns:
        raise ValueError(f"Column '{return_col}' not found in DataFrame")
    
    # Rolling statistics
    df_copy[f'{return_col}_Rolling_Mean_{window}d'] = df_copy[return_col].rolling(window=window).mean()
    df_copy[f'{return_col}_Rolling_Std_{window}d'] = df_copy[return_col].rolling(window=window).std()
    df_copy[f'{return_col}_Rolling_Min_{window}d'] = df_copy[return_col].rolling(window=window).min()
    df_copy[f'{return_col}_Rolling_Max_{window}d'] = df_copy[return_col].rolling(window=window).max()
    
    return df_copy


def compute_correlation_matrix(df: pd.DataFrame, 
                              columns: Optional[list] = None) -> pd.DataFrame:
    """
    Compute correlation matrix for specified columns.
    
    Args:
        df: DataFrame with numerical columns
        columns: List of column names to include (optional)
    
    Returns:
        Correlation matrix DataFrame
    """
    if columns is None:
        # Use all numerical columns
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    return df[columns].corr()


def compute_volatility_metrics(returns: pd.Series, window: int = 21) -> Dict[str, float]:
    """
    Compute various volatility metrics.
    
    Args:
        returns: Series of returns
        window: Window for rolling calculations
    
    Returns:
        Dictionary with volatility metrics
    """
    return {
        'historical_volatility': returns.std(),
        'rolling_volatility_mean': returns.rolling(window=window).std().mean(),
        'rolling_volatility_std': returns.rolling(window=window).std().std(),
        'volatility_of_volatility': returns.rolling(window=window).std().std()
    }


def compute_risk_metrics(returns: pd.Series, risk_free_rate: float = 0.02) -> Dict[str, float]:
    """
    Compute risk-adjusted performance metrics.
    
    Args:
        returns: Series of returns (annualized)
        risk_free_rate: Risk-free rate (annualized)
    
    Returns:
        Dictionary with risk metrics
    """
    excess_returns = returns - risk_free_rate / 252  # Daily risk-free rate
    
    metrics = {
        'sharpe_ratio': excess_returns.mean() / returns.std() if returns.std() > 0 else 0,
        'sortino_ratio': excess_returns.mean() / returns[returns < 0].std() if len(returns[returns < 0]) > 0 else 0,
        'calmar_ratio': 0,  # Would need drawdown calculation
        'max_drawdown': 0,  # Placeholder
        'var_95': returns.quantile(0.05),
        'cvar_95': returns[returns <= returns.quantile(0.05)].mean()
    }
    
    return metrics


def compute_distribution_stats(returns: pd.Series) -> Dict[str, float]:
    """
    Compute distribution statistics for returns.
    
    Args:
        returns: Series of returns
    
    Returns:
        Dictionary with distribution statistics
    """
    return {
        'mean': returns.mean(),
        'median': returns.median(),
        'std': returns.std(),
        'skewness': returns.skew(),
        'kurtosis': returns.kurtosis(),
        'min': returns.min(),
        'max': returns.max(),
        'range': returns.max() - returns.min(),
        'iqr': returns.quantile(0.75) - returns.quantile(0.25),
        'var_95': returns.quantile(0.05),
        'var_99': returns.quantile(0.01)
    }


def compute_moving_averages(df: pd.DataFrame, price_col: str = 'Close', 
                           windows: list = [5, 10, 20, 50, 200]) -> pd.DataFrame:
    """
    Compute moving averages for specified windows.
    
    Args:
        df: DataFrame with price column
        price_col: Name of the price column
        windows: List of window sizes for moving averages
    
    Returns:
        DataFrame with additional moving average columns
    """
    df_copy = df.copy()
    
    for window in windows:
        df_copy[f'MA_{window}'] = df_copy[price_col].rolling(window=window).mean()
    
    return df_copy