# ============================================================================
# stock_analysis/visualization/return_plots.py
# ============================================================================
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from typing import Optional, Tuple, List, Dict


def plot_returns(df: pd.DataFrame, ticker: str,
                figsize: Tuple[int, int] = (15, 10)) -> None:
    """
    Plot comprehensive returns analysis with time series and histograms.
    
    Args:
        df: DataFrame with 'Return' and 'Return_Log' columns
        ticker: Stock ticker symbol
        figsize: Figure size tuple (width, height)
    """
    required_cols = ['Return', 'Return_Log']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"DataFrame must contain return columns: {missing_cols}")
    
    fig, axes = plt.subplots(2, 3, figsize=figsize)
    fig.suptitle(f'{ticker} Returns Analysis', fontsize=16, fontweight='bold', y=0.98)
    
    # Time series plots
    ax1, ax2 = axes[0, 0], axes[0, 1]
    
    # Arithmetic returns time series
    ax1.plot(df.index.to_numpy(), df['Return'].to_numpy(), color='#2E86AB', linewidth=0.8, alpha=0.8)
    ax1.set_title('Arithmetic Returns Time Series', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Return')
    ax1.grid(True, alpha=0.3)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Log returns time series
    ax2.plot(df.index.to_numpy(), df['Return_Log'].to_numpy(), color='#A23B72', linewidth=0.8, alpha=0.8)
    ax2.set_title('Log Returns Time Series', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Log Return')
    ax2.grid(True, alpha=0.3)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Combined time series
    ax3 = axes[0, 2]
    ax3.plot(df.index.to_numpy(), df['Return'].to_numpy(), label='Arithmetic', color='#2E86AB', linewidth=0.8, alpha=0.7)
    ax3.plot(df.index.to_numpy(), df['Return_Log'].to_numpy(), label='Logarithmic', color='#A23B72', linewidth=0.8, alpha=0.7)
    ax3.set_title('Returns Comparison', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Return')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    
    # Histogram plots with normal fits
    ax4, ax5 = axes[1, 0], axes[1, 1]
    
    # Arithmetic returns histogram
    _plot_return_histogram(ax4, df['Return'], 'Arithmetic Returns', '#2E86AB')
    
    # Log returns histogram
    _plot_return_histogram(ax5, df['Return_Log'], 'Log Returns', '#A23B72')
    
    # Q-Q plot
    ax6 = axes[1, 2]
    _plot_qq_plot(ax6, df['Return'], 'Arithmetic Returns Q-Q Plot')
    
    plt.tight_layout()
    plt.show()


def _plot_return_histogram(ax, returns: pd.Series, title: str, color: str) -> None:
    """Helper function to plot return histogram with normal distribution overlay."""
    mu, sigma = returns.mean(), returns.std()
    
    # Histogram
    n, bins, patches = ax.hist(returns, bins=30, density=True, alpha=0.7, color=color, edgecolor='white')
    
    # Normal distribution overlay
    x = np.linspace(returns.min(), returns.max(), 100)
    normal_fit = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, normal_fit, '--', color='red', linewidth=2, label='Normal Fit')
    
    # Statistics text
    stats_text = f'μ = {mu:.4f}\nσ = {sigma:.4f}\nSkew = {returns.skew():.3f}\nKurt = {returns.kurtosis():.3f}'
    ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, verticalalignment='top',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8), fontsize=9)
    
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel('Return')
    ax.set_ylabel('Density')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def _plot_qq_plot(ax, returns: pd.Series, title: str) -> None:
    """Helper function to create Q-Q plot against normal distribution."""
    stats.probplot(returns, dist="norm", plot=ax)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def plot_return_distribution(df: pd.DataFrame, ticker: str,
                           return_col: str = 'Return',
                           figsize: Tuple[int, int] = (12, 8)) -> None:
    """
    Plot detailed return distribution analysis.
    
    Args:
        df: DataFrame with return column
        ticker: Stock ticker symbol
        return_col: Name of the return column to analyze
        figsize: Figure size tuple (width, height)
    """
    if return_col not in df.columns:
        raise ValueError(f"Column '{return_col}' not found in DataFrame")
    
    returns = df[return_col].dropna()
    
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    fig.suptitle(f'{ticker} {return_col} Distribution Analysis', fontsize=16, fontweight='bold')
    
    # Histogram with multiple distribution fits
    ax1 = axes[0, 0]
    mu, sigma = returns.mean(), returns.std()
    
    # Histogram
    ax1.hist(returns, bins=50, density=True, alpha=0.7, color='#2E86AB', edgecolor='white')
    
    # Distribution fits
    x = np.linspace(returns.min(), returns.max(), 100)
    
    # Normal distribution
    normal_fit = stats.norm.pdf(x, mu, sigma)
    ax1.plot(x, normal_fit, '--', color='red', linewidth=2, label='Normal')
    
    # t-distribution fit
    try:
        t_params = stats.t.fit(returns)
        t_fit = stats.t.pdf(x, *t_params)
        ax1.plot(x, t_fit, '--', color='green', linewidth=2, label='t-distribution')
    except:
        pass
    
    ax1.set_title('Distribution Comparison', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Return')
    ax1.set_ylabel('Density')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Box plot
    ax2 = axes[0, 1]
    box_plot = ax2.boxplot(returns, patch_artist=True)
    box_plot['boxes'][0].set_facecolor('#2E86AB')
    box_plot['boxes'][0].set_alpha(0.7)
    ax2.set_title('Box Plot', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Return')
    ax2.grid(True, alpha=0.3)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Q-Q plot against normal
    ax3 = axes[1, 0]
    _plot_qq_plot(ax3, returns, 'Q-Q Plot vs Normal')
    
    # Statistics summary
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    stats_dict = {
        'Count': len(returns),
        'Mean': returns.mean(),
        'Std Dev': returns.std(),
        'Min': returns.min(),
        'Max': returns.max(),
        'Skewness': returns.skew(),
        'Kurtosis': returns.kurtosis(),
        'VaR (5%)': returns.quantile(0.05),
        'VaR (1%)': returns.quantile(0.01),
        'Sharpe Ratio': returns.mean() / returns.std() if returns.std() > 0 else 0
    }
    
    stats_text = '\n'.join([f'{k}: {v:.4f}' if isinstance(v, float) else f'{k}: {v}' 
                           for k, v in stats_dict.items()])
    
    ax4.text(0.1, 0.9, 'Distribution Statistics:', fontsize=14, fontweight='bold',
            transform=ax4.transAxes, verticalalignment='top')
    ax4.text(0.1, 0.8, stats_text, fontsize=11, transform=ax4.transAxes,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.5))
    
    plt.tight_layout()
    plt.show()


def plot_cumulative_returns(df: pd.DataFrame, ticker: str,
                          return_col: str = 'Return',
                          benchmark_df: Optional[pd.DataFrame] = None,
                          benchmark_ticker: Optional[str] = None,
                          figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Plot cumulative returns over time.
    
    Args:
        df: DataFrame with return column
        ticker: Stock ticker symbol
        return_col: Name of the return column
        benchmark_df: Optional benchmark DataFrame for comparison
        benchmark_ticker: Benchmark ticker symbol
        figsize: Figure size tuple (width, height)
    """
    if return_col not in df.columns:
        raise ValueError(f"Column '{return_col}' not found in DataFrame")
    
    # Calculate cumulative returns
    cumulative_returns = (1 + df[return_col]).cumprod() - 1
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot main stock cumulative returns
    ax.plot(df.index.to_numpy(), cumulative_returns.to_numpy() * 100, 
           label=f'{ticker} Cumulative Return', 
           linewidth=2, color='#2E86AB')
    
    # Plot benchmark if provided
    if benchmark_df is not None and benchmark_ticker is not None:
        if return_col in benchmark_df.columns:
            benchmark_cum_returns = (1 + benchmark_df[return_col]).cumprod() - 1
            ax.plot(benchmark_df.index.to_numpy(), benchmark_cum_returns.to_numpy() * 100,
                   label=f'{benchmark_ticker} Cumulative Return',
                   linewidth=2, color='#A23B72', linestyle='--')
    
    # Add horizontal line at 0%
    ax.axhline(y=0, color='black', linestyle='-', alpha=0.5, linewidth=0.8)
    
    ax.set_title(f'Cumulative Returns Comparison', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Cumulative Return (%)', fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Format x-axis
    fig.autofmt_xdate()
    
    plt.tight_layout()
    plt.show()


def plot_rolling_returns(df: pd.DataFrame, ticker: str,
                        windows: List[int] = [21, 63, 252],
                        return_col: str = 'Return',
                        figsize: Tuple[int, int] = (15, 10)) -> None:
    """
    Plot rolling returns for different time windows.
    
    Args:
        df: DataFrame with return column
        ticker: Stock ticker symbol
        windows: List of rolling window sizes (in days)
        return_col: Name of the return column
        figsize: Figure size tuple (width, height)
    """
    if return_col not in df.columns:
        raise ValueError(f"Column '{return_col}' not found in DataFrame")
    
    fig, axes = plt.subplots(len(windows), 1, figsize=figsize, sharex=True)
    if len(windows) == 1:
        axes = [axes]
    
    fig.suptitle(f'{ticker} Rolling Returns Analysis', fontsize=16, fontweight='bold', y=0.98)
    
    colors = ['#2E86AB', '#A23B72', '#F18F01']
    
    for i, window in enumerate(windows):
        ax = axes[i]
        
        # Calculate rolling returns (annualized)
        rolling_returns = df[return_col].rolling(window=window).mean() * 252
        rolling_std = df[return_col].rolling(window=window).std() * np.sqrt(252)
        
        # Plot rolling mean
        ax.plot(df.index.to_numpy(), rolling_returns.to_numpy() * 100, 
               color=colors[i % len(colors)], linewidth=1.5,
               label=f'{window}-day Rolling Return')
        
        # Add confidence bands
        upper_band = (rolling_returns + rolling_std) * 100
        lower_band = (rolling_returns - rolling_std) * 100
        
        ax.fill_between(df.index.to_numpy(), upper_band.to_numpy(), lower_band.to_numpy(), 
                       alpha=0.2, color=colors[i % len(colors)])
        
        # Add horizontal line at 0%
        ax.axhline(y=0, color='black', linestyle='-', alpha=0.5, linewidth=0.8)
        
        # Labels for window interpretation
        window_labels = {21: '1-Month', 63: '3-Month', 252: '1-Year'}
        window_label = window_labels.get(window, f'{window}-day')
        
        ax.set_title(f'{window_label} Rolling Returns (Annualized)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Return (%)', fontsize=11)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    
    axes[-1].set_xlabel('Date', fontsize=12)
    
    # Format x-axis
    fig.autofmt_xdate()
    
    plt.tight_layout()
    plt.show()


def plot_return_correlation_matrix(dfs: List[pd.DataFrame], 
                                  tickers: List[str],
                                  return_col: str = 'Return',
                                  figsize: Tuple[int, int] = (10, 8)) -> None:
    """
    Plot correlation matrix of returns for multiple stocks.
    
    Args:
        dfs: List of DataFrames with return columns
        tickers: List of ticker symbols
        return_col: Name of the return column
        figsize: Figure size tuple (width, height)
    """
    if len(dfs) != len(tickers):
        raise ValueError("Number of DataFrames must match number of tickers")
    
    # Combine returns into a single DataFrame
    returns_df = pd.DataFrame()
    for df, ticker in zip(dfs, tickers):
        if return_col not in df.columns:
            raise ValueError(f"Column '{return_col}' not found in DataFrame for {ticker}")
        returns_df[ticker] = df[return_col]
    
    # Calculate correlation matrix
    corr_matrix = returns_df.corr()
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create heatmap
    im = ax.imshow(corr_matrix, cmap='RdYlBu', aspect='auto', vmin=-1, vmax=1)
    
    # Set ticks and labels
    ax.set_xticks(range(len(tickers)))
    ax.set_yticks(range(len(tickers)))
    ax.set_xticklabels(tickers)
    ax.set_yticklabels(tickers)
    
    # Rotate x-axis labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Add correlation values to cells
    for i in range(len(tickers)):
        for j in range(len(tickers)):
            text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.3f}',
                          ha="center", va="center", color="black", fontweight='bold')
    
    # Add colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('Correlation Coefficient', rotation=-90, va="bottom")
    
    ax.set_title('Return Correlation Matrix', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.show()


def plot_drawdown_analysis(df: pd.DataFrame, ticker: str,
                          price_col: str = 'Close',
                          figsize: Tuple[int, int] = (12, 8)) -> None:
    """
    Plot drawdown analysis showing price and underwater curve.
    
    Args:
        df: DataFrame with price column
        ticker: Stock ticker symbol
        price_col: Name of the price column
        figsize: Figure size tuple (width, height)
    """
    if price_col not in df.columns:
        raise ValueError(f"Column '{price_col}' not found in DataFrame")
    
    # Calculate drawdown
    peak = df[price_col].cummax()
    drawdown = (df[price_col] - peak) / peak * 100
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize, 
                                   gridspec_kw={'height_ratios': [2, 1]},
                                   sharex=True)
    
    # Price chart with peaks
    ax1.plot(df.index.to_numpy(), df[price_col].to_numpy(), label='Price', linewidth=1.5, color='#2E86AB')
    ax1.plot(df.index.to_numpy(), peak.to_numpy(), label='Peak', linewidth=1, color='red', alpha=0.7)
    ax1.fill_between(df.index.to_numpy(), df[price_col].to_numpy(), peak.to_numpy(), alpha=0.3, color='red')
    
    ax1.set_title(f'{ticker} Price and Drawdown Analysis', fontsize=16, fontweight='bold')
    ax1.set_ylabel('Price ($)', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Drawdown (underwater curve)
    ax2.fill_between(df.index.to_numpy(), drawdown.to_numpy(), 0, alpha=0.7, color='red')
    ax2.plot(df.index.to_numpy(), drawdown.to_numpy(), color='darkred', linewidth=1)
    
    # Add statistics
    max_dd = drawdown.min()
    max_dd_date = drawdown.idxmin()
    
    ax2.axhline(y=max_dd, color='black', linestyle='--', alpha=0.7)
    ax2.text(0.02, 0.1, f'Max Drawdown: {max_dd:.2f}%\nDate: {max_dd_date.strftime("%Y-%m-%d")}',
            transform=ax2.transAxes, verticalalignment='bottom',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    ax2.set_title('Drawdown (Underwater Curve)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Drawdown (%)', fontsize=12)
    ax2.set_xlabel('Date', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Format x-axis
    fig.autofmt_xdate()
    
    plt.tight_layout()
    plt.show()