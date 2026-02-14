# -*- coding: utf-8 -*-
"""
quantpie_empirical_volatility_analysis.py

Empirical analysis of time-varying volatility, fat tails, and leptokurtic
distributions using historical stock data. This module demonstrates the
key empirical failures of the constant volatility assumption.

Based on QuantPie Lecture Notes: Non-constant volatilities, high peak, and fat tails.

Author: Financial Math Library
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy import stats


def download_stock_data(ticker: str, period: str = 'max') -> pd.DataFrame:
    """
    Download historical stock price data using yfinance.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol (e.g., 'WMT', 'AAPL').
    period : str, default 'max'
        Historical period to retrieve ('max', '5y', '1y', etc.).

    Returns
    -------
    pd.DataFrame
        DataFrame with columns ['Open', 'High', 'Low', 'Close', 'Volume',
        'Dividends', 'Stock Splits'].
    """
    print(f"Downloading historical data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    print(f"Data downloaded: {len(df)} trading days from {df.index[0].date()} "
          f"to {df.index[-1].date()}")
    return df


def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily log-returns from closing prices.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with 'Close' column.

    Returns
    -------
    pd.DataFrame
        DataFrame with 'Return' column containing daily percentage changes.
    """
    df = df.copy()
    df['Return'] = df['Close'].pct_change()
    df = df[['Close', 'Return']].iloc[1:]  # Remove NaN from pct_change
    return df


def compute_rolling_volatility(returns: pd.Series, window: int = 30) -> pd.Series:
    """
    Compute rolling window standard deviation (realized volatility).

    Parameters
    ----------
    returns : pd.Series
        Daily returns series.
    window : int, default 30
        Rolling window size in days.

    Returns
    -------
    pd.Series
        Rolling standard deviation series.
    """
    rolling_vol = returns.rolling(window).std()
    return rolling_vol


def compute_distribution_stats(returns: pd.Series) -> dict:
    """
    Compute distribution statistics: mean, std, skewness, kurtosis.

    Parameters
    ----------
    returns : pd.Series
        Daily returns series (no NaN values).

    Returns
    -------
    dict
        Dictionary with keys: 'mean', 'std', 'skewness', 'kurtosis',
        'excess_kurtosis'.
    """
    clean_returns = returns.dropna()

    mean = clean_returns.mean()
    std = clean_returns.std()
    skewness = stats.skew(clean_returns)
    kurtosis_val = stats.kurtosis(clean_returns, fisher=False)  # Excess=False gives Kurt=4 for normal
    excess_kurtosis = stats.kurtosis(clean_returns, fisher=True)  # Excess=True gives Kurt=0 for normal

    return {
        'mean': mean,
        'std': std,
        'skewness': skewness,
        'kurtosis': kurtosis_val,
        'excess_kurtosis': excess_kurtosis
    }


def analyze_tail_events(returns: pd.Series, threshold_sigma: float = 3.0) -> dict:
    """
    Analyze extreme tail events (returns beyond ±threshold_sigma standard deviations).

    Parameters
    ----------
    returns : pd.Series
        Daily returns series.
    threshold_sigma : float, default 3.0
        Number of standard deviations defining tail events.

    Returns
    -------
    dict
        Dictionary with tail statistics including:
        - 'right_tail_count': Number of positive extreme events
        - 'left_tail_count': Number of negative extreme events
        - 'right_tail_pct': Percentage of data in right tail
        - 'left_tail_pct': Percentage of data in left tail
        - 'total_tail_pct': Total percentage in either tail
        - 'normal_tail_probability': Normal distribution prediction
    """
    clean_returns = returns.dropna()
    mu = clean_returns.mean()
    sigma = clean_returns.std()

    threshold_val = threshold_sigma * sigma

    right_tail = clean_returns > (mu + threshold_val)
    left_tail = clean_returns < (mu - threshold_val)

    right_tail_count = right_tail.sum()
    left_tail_count = left_tail.sum()
    total_count = len(clean_returns)

    right_tail_pct = 100 * right_tail_count / total_count
    left_tail_pct = 100 * left_tail_count / total_count
    total_tail_pct = right_tail_pct + left_tail_pct

    # Normal distribution probability
    normal_prob_one_tail = 1 - stats.norm.cdf(threshold_sigma)
    normal_prob_both_tails = 2 * normal_prob_one_tail

    return {
        'threshold_sigma': threshold_sigma,
        'threshold_value': threshold_val,
        'right_tail_count': right_tail_count,
        'left_tail_count': left_tail_count,
        'right_tail_pct': right_tail_pct,
        'left_tail_pct': left_tail_pct,
        'total_tail_pct': total_tail_pct,
        'normal_tail_probability_pct': 100 * normal_prob_both_tails,
    }


def empirical_volatility_analysis(ticker: str = 'WMT', window: int = 30):
    """
    Main analysis function: time-varying volatility, distribution analysis,
    and tail analysis.

    Parameters
    ----------
    ticker : str, default 'WMT'
        Stock ticker symbol.
    window : int, default 30
        Rolling volatility window in days.

    Returns
    -------
    dict
        Comprehensive results including data, statistics, and analysis.
    """
    # Download and prepare data
    df = download_stock_data(ticker, period='max')
    df = compute_returns(df)

    # Compute rolling volatility
    rolling_vol = compute_rolling_volatility(df['Return'], window=window)
    df['Rolling_Vol'] = rolling_vol

    # Remove NaN from rolling volatility
    df_clean = df.dropna()

    # Distribution statistics
    dist_stats = compute_distribution_stats(df_clean['Return'])

    # Tail analysis at different thresholds
    tail_3sigma = analyze_tail_events(df_clean['Return'], threshold_sigma=3.0)
    tail_5sigma = analyze_tail_events(df_clean['Return'], threshold_sigma=5.0)

    print("\n" + "="*70)
    print(f"EMPIRICAL VOLATILITY ANALYSIS: {ticker}")
    print("="*70)

    print(f"\nData period: {df_clean.index[0].date()} to {df_clean.index[-1].date()}")
    print(f"Number of observations: {len(df_clean)}")
    print(f"Rolling volatility window: {window} days")

    print(f"\n{'-'*70}")
    print("RETURN DISTRIBUTION STATISTICS")
    print(f"{'-'*70}")
    print(f"Mean (annualized):        {dist_stats['mean']*252:8.4f} ({dist_stats['mean']:10.6f} daily)")
    print(f"Std Dev (annualized):     {dist_stats['std']*np.sqrt(252):8.4f} ({dist_stats['std']:10.6f} daily)")
    print(f"Skewness:                 {dist_stats['skewness']:10.6f}")
    print(f"  (Normal = 0; Negative = Left-skewed with fat left tail)")
    print(f"Kurtosis (excess):        {dist_stats['excess_kurtosis']:10.6f}")
    print(f"  (Normal = 0; Positive = Heavy-tailed/Leptokurtic)")

    print(f"\n{'-'*70}")
    print("VOLATILITY STATISTICS")
    print(f"{'-'*70}")
    rolling_stats = df_clean['Rolling_Vol'].describe()
    print(f"30-day rolling volatility (daily):")
    print(f"  Min:      {rolling_stats['min']:10.6f}")
    print(f"  25th %ile: {rolling_stats['25%']:10.6f}")
    print(f"  Mean:     {rolling_stats['mean']:10.6f}")
    print(f"  Median:   {rolling_stats['50%']:10.6f}")
    print(f"  75th %ile: {rolling_stats['75%']:10.6f}")
    print(f"  Max:      {rolling_stats['max']:10.6f}")
    print(f"  Std Dev:  {rolling_stats['std']:10.6f}")

    ratio = rolling_stats['max'] / rolling_stats['min']
    print(f"\nMax/Min volatility ratio: {ratio:.2f}x")
    print(f"  (Constant volatility assumption would imply ratio = 1.0)")

    print(f"\n{'-'*70}")
    print("TAIL EVENT ANALYSIS")
    print(f"{'-'*70}")

    print(f"\nReturns beyond ±3σ from mean:")
    print(f"  Right tail (> μ + 3σ):  {tail_3sigma['right_tail_count']:4d} occurrences "
          f"({tail_3sigma['right_tail_pct']:5.2f}%)")
    print(f"  Left tail  (< μ - 3σ):  {tail_3sigma['left_tail_count']:4d} occurrences "
          f"({tail_3sigma['left_tail_pct']:5.2f}%)")
    print(f"  Total:                  {tail_3sigma['right_tail_count'] + tail_3sigma['left_tail_count']:4d} "
          f"({tail_3sigma['total_tail_pct']:5.2f}%)")
    print(f"  Normal distribution predicts: {tail_3sigma['normal_tail_probability_pct']:.4f}%")
    print(f"  Excess over normal:     {tail_3sigma['total_tail_pct'] - tail_3sigma['normal_tail_probability_pct']:.2f}%")

    print(f"\nReturns beyond ±5σ from mean:")
    print(f"  Right tail (> μ + 5σ):  {tail_5sigma['right_tail_count']:4d} occurrences "
          f"({tail_5sigma['right_tail_pct']:5.2f}%)")
    print(f"  Left tail  (< μ - 5σ):  {tail_5sigma['left_tail_count']:4d} occurrences "
          f"({tail_5sigma['left_tail_pct']:5.2f}%)")
    print(f"  Total:                  {tail_5sigma['right_tail_count'] + tail_5sigma['left_tail_count']:4d} "
          f"({tail_5sigma['total_tail_pct']:5.2f}%)")
    print(f"  Normal distribution predicts: {tail_5sigma['normal_tail_probability_pct']:.6f}%")
    print(f"  Excess over normal:     {tail_5sigma['total_tail_pct'] - tail_5sigma['normal_tail_probability_pct']:.4f}%")

    print("\n" + "="*70)

    results = {
        'ticker': ticker,
        'window': window,
        'data': df_clean,
        'dist_stats': dist_stats,
        'tail_3sigma': tail_3sigma,
        'tail_5sigma': tail_5sigma,
        'rolling_stats': rolling_stats
    }

    return results


def create_visualizations(results: dict, output_dir: str = '/tmp'):
    """
    Create comprehensive visualizations of empirical volatility analysis.

    Parameters
    ----------
    results : dict
        Results dictionary from empirical_volatility_analysis().
    output_dir : str, default '/tmp'
        Directory to save figures.
    """
    df = results['data']
    ticker = results['ticker']
    dist_stats = results['dist_stats']
    tail_3sigma = results['tail_3sigma']

    # Figure 1: Price history
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.plot(df.index, df['Close'], linewidth=1.5, color='navy')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    ax.set_title(f'{ticker} Historical Price')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/quantpie_price_history.png', dpi=150)
    print(f"Saved: {output_dir}/quantpie_price_history.png")
    plt.close()

    # Figure 2: Returns and rolling volatility
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))

    # Returns
    ax1.plot(df.index, df['Return'], alpha=0.5, linewidth=0.8, color='steelblue')
    ax1.fill_between(df.index, df['Rolling_Vol'], -df['Rolling_Vol'],
                      alpha=0.3, color='red', label='±30-day Rolling Vol')
    ax1.set_ylabel('Daily Return')
    ax1.set_title(f'{ticker} Daily Returns and Rolling Volatility')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Rolling volatility
    ax2.plot(df.index, df['Rolling_Vol'], linewidth=1.5, color='red', label='30-day rolling std')
    ax2.fill_between(df.index, df['Rolling_Vol'], alpha=0.3, color='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Volatility (daily)')
    ax2.set_title('Time-Varying Volatility')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.savefig(f'{output_dir}/quantpie_returns_and_vol.png', dpi=150)
    print(f"Saved: {output_dir}/quantpie_returns_and_vol.png")
    plt.close()

    # Figure 3: Histogram with normal fit (high peak)
    fig, ax = plt.subplots(figsize=(10, 6))

    mu = dist_stats['mean']
    sigma = dist_stats['std']
    returns = df['Return'].values

    # Histogram
    n_bins = 100
    counts, bins, patches = ax.hist(returns, bins=n_bins, density=True,
                                     alpha=0.7, color='steelblue', edgecolor='black', linewidth=0.5)

    # Normal fit
    x = np.linspace(returns.min(), returns.max(), 200)
    y_normal = stats.norm(mu, sigma).pdf(x)
    ax.plot(x, y_normal, 'r--', linewidth=2.5, label=f'Normal(μ={mu:.6f}, σ={sigma:.6f})')

    ax.set_xlabel('Daily Return')
    ax.set_ylabel('Probability Density')
    ax.set_title(f'{ticker} Return Distribution: High Peak (Leptokurtic)')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/quantpie_high_peak.png', dpi=150)
    print(f"Saved: {output_dir}/quantpie_high_peak.png")
    plt.close()

    # Figure 4: Fat right tail
    fig, ax = plt.subplots(figsize=(10, 6))

    threshold_3sigma = mu + 3 * sigma
    right_tail_mask = returns > threshold_3sigma

    if right_tail_mask.sum() > 0:
        right_tail_returns = returns[right_tail_mask]

        counts, bins, patches = ax.hist(right_tail_returns, bins=30, density=True,
                                        alpha=0.7, color='steelblue', edgecolor='black', linewidth=0.5)

        # Normal fit for comparison
        x = np.linspace(right_tail_returns.min(), right_tail_returns.max(), 100)
        y_normal = stats.norm(mu, sigma).pdf(x)
        ax.plot(x, y_normal, 'r--', linewidth=2.5, label='Normal PDF')

        ax.set_xlabel('Daily Return')
        ax.set_ylabel('Probability Density')
        ax.set_title(f'{ticker} Right Tail (r > μ + 3σ): Fat Tail Evidence')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/quantpie_fat_right_tail.png', dpi=150)
    print(f"Saved: {output_dir}/quantpie_fat_right_tail.png")
    plt.close()

    # Figure 5: Fat left tail
    fig, ax = plt.subplots(figsize=(10, 6))

    threshold_left = mu - 3 * sigma
    left_tail_mask = returns < threshold_left

    if left_tail_mask.sum() > 0:
        left_tail_returns = returns[left_tail_mask]

        counts, bins, patches = ax.hist(left_tail_returns, bins=30, density=True,
                                        alpha=0.7, color='salmon', edgecolor='black', linewidth=0.5)

        # Normal fit for comparison
        x = np.linspace(left_tail_returns.min(), left_tail_returns.max(), 100)
        y_normal = stats.norm(mu, sigma).pdf(x)
        ax.plot(x, y_normal, 'r--', linewidth=2.5, label='Normal PDF')

        ax.set_xlabel('Daily Return')
        ax.set_ylabel('Probability Density')
        ax.set_title(f'{ticker} Left Tail (r < μ - 3σ): Fat Tail & Downside Risk')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/quantpie_fat_left_tail.png', dpi=150)
    print(f"Saved: {output_dir}/quantpie_fat_left_tail.png")
    plt.close()

    print(f"\nAll visualizations saved to {output_dir}/")


def main():
    """Main execution function."""
    # Run empirical analysis
    results = empirical_volatility_analysis(ticker='WMT', window=30)

    # Create visualizations
    create_visualizations(results, output_dir='/tmp')

    return results


if __name__ == "__main__":
    main()
