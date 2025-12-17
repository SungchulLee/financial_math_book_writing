# ============================================================================
# stock_analysis/analysis/returns.py
# ============================================================================
import numpy as np
import pandas as pd

def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute arithmetic returns from price data.
    
    Formula: r_t = (S_t - S_{t-1}) / S_{t-1}
    
    Args:
        df: DataFrame with 'Close' column
    
    Returns:
        DataFrame with additional 'Return' column
    """
    df_copy = df.copy()
    df_copy['Return'] = df_copy['Close'].pct_change()
    df_copy.dropna(inplace=True)
    return df_copy


def compute_log_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute logarithmic returns from price data.
    
    Formula: r_t = log(S_t / S_{t-1})
    
    Args:
        df: DataFrame with 'Close' column
    
    Returns:
        DataFrame with additional 'Return_Log' column
    """
    df_copy = df.copy()
    df_copy['Return_Log'] = np.log(df_copy['Close'] / df_copy['Close'].shift(1))
    df_copy.dropna(inplace=True)
    return df_copy

def compute_both_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute both arithmetic and logarithmic returns.
    
    Args:
        df: DataFrame with 'Close' column
    
    Returns:
        DataFrame with 'Return' and 'Return_Log' columns
    """
    df_copy = df.copy()
    df_copy['Return'] = df_copy['Close'].pct_change()
    df_copy['Return_Log'] = np.log(df_copy['Close'] / df_copy['Close'].shift(1))
    df_copy.dropna(inplace=True)
    return df_copy

def compute_cumulative_returns(df: pd.DataFrame, return_col: str = 'Return') -> pd.DataFrame:
    """
    Compute cumulative returns.
    
    Args:
        df: DataFrame with return column
        return_col: Name of the return column
    
    Returns:
        DataFrame with additional cumulative return column
    """
    df_copy = df.copy()
    df_copy[f'{return_col}_Cumulative'] = (1 + df_copy[return_col]).cumprod() - 1
    return df_copy


def compute_rolling_returns(df: pd.DataFrame, window: int = 21, return_col: str = 'Return') -> pd.DataFrame:
    """
    Compute rolling returns over a specified window.
    
    Args:
        df: DataFrame with return column
        window: Rolling window size (default 21 for ~1 month)
        return_col: Name of the return column
    
    Returns:
        DataFrame with additional rolling return column
    """
    df_copy = df.copy()
    df_copy[f'{return_col}_Rolling_{window}d'] = df_copy[return_col].rolling(window=window).sum()
    return df_copy

def compute_return_metrics(returns: pd.Series) -> dict:
    """
    Compute basic return metrics.
    
    Args:
        returns: Series of returns
    
    Returns:
        Dictionary with return metrics
    """
    return {
        'mean': returns.mean(),
        'std': returns.std(),
        'min': returns.min(),
        'max': returns.max(),
        'skewness': returns.skew(),
        'kurtosis': returns.kurtosis(),
        'sharpe_ratio': returns.mean() / returns.std() if returns.std() > 0 else 0
    }

def compute_drawdown(df: pd.DataFrame, price_col: str = 'Close') -> pd.DataFrame:
    """
    Compute drawdown from peak values.
    
    Args:
        df: DataFrame with price column
        price_col: Name of the price column
    
    Returns:
        DataFrame with drawdown columns
    """
    df_copy = df.copy()
    df_copy['Peak'] = df_copy[price_col].cummax()
    df_copy['Drawdown'] = (df_copy[price_col] - df_copy['Peak']) / df_copy['Peak']
    df_copy['Drawdown_Pct'] = df_copy['Drawdown'] * 100
    return df_copy