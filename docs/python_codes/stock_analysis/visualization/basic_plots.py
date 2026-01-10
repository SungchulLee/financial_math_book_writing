# ============================================================================
# stock_analysis/visualization/basic_plots.py
# ============================================================================
import matplotlib.pyplot as plt
import pandas as pd
from typing import Tuple, List

def plot_close(df: pd.DataFrame, ticker: str, figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Plot the closing price time series.
    
    Args:
        df: DataFrame with 'Close' column and datetime index
        ticker: Stock ticker symbol for title
        figsize: Figure size tuple (width, height)
    """
    if 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column")
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(df.index.to_numpy(), df['Close'].to_numpy(), label='Close Price', linewidth=1.5, color='#2E86AB')
    
    ax.set_title(f'{ticker} Closing Price', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price ($)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    
    # Format x-axis for better date display
    fig.autofmt_xdate()
    
    plt.tight_layout()
    plt.show()

def plot_price_with_volume(df: pd.DataFrame, ticker: str, figsize: Tuple[int, int] = (12, 8)) -> None:
    """
    Plot closing price with volume subplot.
    
    Args:
        df: DataFrame with 'Close' and 'Volume' columns
        ticker: Stock ticker symbol for title
        figsize: Figure size tuple (width, height)
    """
    required_cols = ['Close', 'Volume']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"DataFrame must contain columns: {missing_cols}")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize, 
                                   gridspec_kw={'height_ratios': [3, 1]}, 
                                   sharex=True)
    
    # Price plot
    ax1.plot(df.index.to_numpy(), df['Close'].to_numpy(), label='Close Price', 
             linewidth=1.5, color='#2E86AB')
    ax1.set_title(f'{ticker} Price and Volume', fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylabel('Price ($)', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Volume plot
    ax2.bar(df.index.to_numpy(), df['Volume'].to_numpy(), alpha=0.7, color='#A23B72', width=1)
    ax2.set_ylabel('Volume', fontsize=12)
    ax2.set_xlabel('Date', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Format x-axis
    fig.autofmt_xdate()
    
    plt.tight_layout()
    plt.show()

def plot_price_with_moving_averages(df: pd.DataFrame, ticker: str,
                                   ma_windows: List[int] = [20, 50, 200],
                                   figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Plot closing price with moving averages.
    
    Args:
        df: DataFrame with 'Close' column
        ticker: Stock ticker symbol for title
        ma_windows: List of moving average window sizes
        figsize: Figure size tuple (width, height)
    """
    if 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column")
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot closing price
    ax.plot(df.index, df['Close'], label='Close Price', 
            linewidth=2, color='#2E86AB', alpha=0.8)
    
    # Plot moving averages
    colors = ['#F18F01', '#C73E1D', '#8B2F97']
    
    for i, window in enumerate(ma_windows):
        ma_col = f'MA_{window}'
        if ma_col in df.columns:
            ma_data = df[ma_col]
        else:
            ma_data = df['Close'].rolling(window=window).mean()
        
        color = colors[i % len(colors)]
        ax.plot(df.index, ma_data, 
                label=f'{window}-day MA', 
                linewidth=1.5, 
                color=color,
                alpha=0.7)
    
    ax.set_title(f'{ticker} Price with Moving Averages', 
                fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price ($)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    
    # Format x-axis
    fig.autofmt_xdate()
    
    plt.tight_layout()
    plt.show()

def plot_multiple_prices(dfs: List[pd.DataFrame], tickers: List[str],
                        normalize: bool = True, 
                        figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Plot multiple stock prices on the same chart.
    
    Args:
        dfs: List of DataFrames with 'Close' columns
        tickers: List of ticker symbols
        normalize: Whether to normalize prices to start at 100
        figsize: Figure size tuple (width, height)
    """
    if len(dfs) != len(tickers):
        raise ValueError("Number of DataFrames must match number of tickers")
    
    fig, ax = plt.subplots(figsize=figsize)
    
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#8B2F97']
    
    for i, (df, ticker) in enumerate(zip(dfs, tickers)):
        if 'Close' not in df.columns:
            raise ValueError(f"DataFrame for {ticker} must contain 'Close' column")
        
        prices = df['Close'].copy()
        if normalize:
            prices = (prices / prices.iloc[0]) * 100
        
        color = colors[i % len(colors)]
        
        # Convert to numpy arrays to avoid pandas/matplotlib compatibility issues
        x_values = df.index.to_numpy() if hasattr(df.index, 'to_numpy') else df.index.values
        y_values = prices.to_numpy() if hasattr(prices, 'to_numpy') else prices.values
        
        ax.plot(x_values, y_values, 
                label=ticker, 
                linewidth=1.5, 
                color=color)
    
    title = 'Stock Price Comparison'
    ylabel = 'Normalized Price (Base=100)' if normalize else 'Price ($)'
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    
    # Format x-axis
    fig.autofmt_xdate()
    
    plt.tight_layout()
    plt.show()

def plot_price_bands(df: pd.DataFrame, ticker: str,
                     window: int = 20, num_std: float = 2.0,
                     figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Plot price with Bollinger Bands.
    
    Args:
        df: DataFrame with 'Close' column
        ticker: Stock ticker symbol for title
        window: Window size for moving average
        num_std: Number of standard deviations for bands
        figsize: Figure size tuple (width, height)
    """
    if 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column")
    
    # Calculate Bollinger Bands
    rolling_mean = df['Close'].rolling(window=window).mean()
    rolling_std = df['Close'].rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * num_std)
    lower_band = rolling_mean - (rolling_std * num_std)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot price and bands
    ax.plot(df.index, df['Close'], label='Close Price', 
            linewidth=2, color='#2E86AB')
    ax.plot(df.index, rolling_mean, label=f'{window}-day MA', 
            linewidth=1.5, color='#F18F01')
    ax.plot(df.index, upper_band, label=f'Upper Band ({num_std}σ)', 
            linewidth=1, color='#C73E1D', linestyle='--')
    ax.plot(df.index, lower_band, label=f'Lower Band ({num_std}σ)', 
            linewidth=1, color='#C73E1D', linestyle='--')
    
    # Fill between bands
    ax.fill_between(df.index, upper_band, lower_band, 
                   alpha=0.1, color='#C73E1D')
    
    ax.set_title(f'{ticker} Price with Bollinger Bands', 
                fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price ($)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    
    # Format x-axis
    fig.autofmt_xdate()
    
    plt.tight_layout()
    plt.show()