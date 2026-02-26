# ============================================================================
# stock_analysis_CORRELATION_SP500.py
# ============================================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import stock_analysis as sto

def pretty_print_corr(label, series):
    """
    Nicely format and print correlation pairs.
    
    Args:
        label: Description label for the correlation set
        series: Pandas Series with correlation values
    """
    print(f"\n{label}\n")
    for (ticker1, ticker2), value in series.items():
        print(f"{ticker1:<6} {ticker2:<6} {value:>10.6f}")

def normalize_prices(df, start_date='2024-01-01'):
    """
    Normalize prices to start at 100 from a given start date.
    
    Args:
        df: DataFrame with stock prices
        start_date: Starting date for normalization
        
    Returns:
        DataFrame with normalized prices
    """
    # Convert start_date to same timezone as the data (US/Eastern based on -05:00 offset)
    start_date = pd.to_datetime(start_date).tz_localize('US/Eastern')
    
    print(f"🔍 Filtering data from {start_date.date()} onwards...")
    print(f"📊 Original data shape: {df.shape}")
    print(f"📅 Index sample: {df.index[:3].tolist()}")
    
    # Now both have the same timezone, comparison should work
    df_filtered = df[df.index >= start_date].copy()
    
    # Check if we have any data after the start date
    if df_filtered.empty:
        print(f"⚠️ Warning: No data found after {start_date.date()}")
        print(f"   Available data starts from: {df.index[0].date()}")
        print(f"   Available data ends at: {df.index[-1].date()}")
        return df_filtered
    
    print(f"📅 Found {len(df_filtered)} days of data from {df_filtered.index[0].date()} to {df_filtered.index[-1].date()}")
    
    # Normalize each stock to start at 100
    print("🔄 Normalizing prices...")
    normalized_df = df_filtered.div(df_filtered.iloc[0]) * 100
    
    # Remove any columns with NaN values (stocks with insufficient data)
    before_dropna = normalized_df.shape[1]
    normalized_df = normalized_df.dropna(axis=1)
    after_dropna = normalized_df.shape[1]
    
    if before_dropna != after_dropna:
        print(f"🧹 Removed {before_dropna - after_dropna} stocks with insufficient data")
    
    print(f"📈 Successfully normalized {normalized_df.shape[1]} stocks from {start_date.date()}")
    return normalized_df

def compute_sorted_correlations(price_df, plot=True):
    """
    Compute and sort stock correlations.
    
    Args:
        price_df: DataFrame with normalized stock prices
        plot: Whether to create a correlation heatmap
        
    Returns:
        Tuple of (sorted_correlations, closest_to_zero_correlations)
    """
    print("🔄 Computing correlation matrix...")
    
    # Calculate correlation matrix
    corr_matrix = price_df.corr()
    
    # Create a mask for the upper triangle (to avoid duplicate pairs)
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
    
    # Extract upper triangle correlations and remove self-correlations
    correlations = corr_matrix.where(mask).stack()
    correlations = correlations[correlations != 1.0]  # Remove perfect self-correlations
    
    # Sort correlations
    sorted_corr = correlations.sort_values()
    
    # Find correlations closest to zero
    closest_to_zero = correlations.reindex(correlations.abs().sort_values().index)
    
    print(f"📊 Computed {len(correlations)} unique stock pair correlations")
    print(f"📈 Correlation range: {sorted_corr.min():.4f} to {sorted_corr.max():.4f}")
    
    # Create correlation heatmap if requested
    if plot:
        create_correlation_heatmap(corr_matrix, price_df.columns[:50])  # Show top 50 for readability
    
    return sorted_corr, closest_to_zero.head(10)

def create_correlation_heatmap(corr_matrix, tickers_subset):
    """
    Create a correlation heatmap for visualization.
    
    Args:
        corr_matrix: Full correlation matrix
        tickers_subset: Subset of tickers to display (for readability)
    """
    print("📊 Creating correlation heatmap...")
    
    # Create subset correlation matrix for visualization
    subset_corr = corr_matrix.loc[tickers_subset, tickers_subset]
    
    # Create the subplot layout with heatmap on top and histogram on bottom
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(12, 14), gridspec_kw={'height_ratios': [3, 1]})
    
    # Create heatmap with better formatting
    heatmap = sns.heatmap(subset_corr, 
                         cmap='RdBu_r',  # Red-Blue colormap (red=positive, blue=negative)
                         center=0,
                         square=True,
                         linewidths=0.1,  # Add thin lines between cells
                         cbar_kws={'label': 'Correlation Coefficient', 'shrink': 0.8},
                         annot=False,  # Don't annotate individual cells (too crowded)
                         fmt='.2f',
                         xticklabels=True,
                         yticklabels=True,
                         ax=ax0)
    
    # Improve the heatmap formatting
    ax0.set_title('S&P 500 Stock Correlation Matrix (Top 50 Stocks)', fontsize=16, fontweight='bold', pad=20)
    ax0.set_xlabel('Stock Tickers', fontsize=12)
    ax0.set_ylabel('Stock Tickers', fontsize=12)
    
    # Fix the tick rotation - use plt.setp() or tick_params()
    plt.setp(ax0.get_xticklabels(), rotation=45, ha='right', fontsize=8)
    plt.setp(ax0.get_yticklabels(), rotation=0, fontsize=8)
    
    # Create histogram of correlations in the bottom subplot
    # Extract all correlations (upper triangle to avoid duplicates)
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
    correlations = corr_matrix.where(mask).stack()
    correlations = correlations[correlations != 1.0]  # Remove perfect self-correlations
    
    ax1.hist(correlations, bins=100, color='gray', edgecolor='black', alpha=0.7)
    ax1.set_title("Distribution of Pairwise Correlations", fontsize=14, fontweight='bold')
    ax1.set_xlabel("Correlation Value", fontsize=12)
    ax1.set_ylabel("Frequency", fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Add some statistics to the histogram
    mean_corr = correlations.mean()
    ax1.axvline(mean_corr, color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {mean_corr:.3f}')
    ax1.axvline(0, color='black', linestyle='-', linewidth=1, alpha=0.5)
    ax1.legend()
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Force display of the plot
    plt.show()
    
    print("✅ Correlation heatmap and distribution displayed")

if __name__ == "__main__":
    print("🚀 S&P 500 Correlation Analysis")
    print("=" * 50)
    
    # Configuration
    start_date = '2024-01-01'
    csv_path = './stock_analysis/sp500/sp500_data/sp500_2024.csv'
    
    # Load S&P 500 data from CSV file
    price_df = sto.load_data_from_csv(csv_path)
    
    if price_df is not None:
        # Normalize prices from start date
        normalized_df = normalize_prices(price_df, start_date)
        
        # Compute correlations and create visualizations
        sorted_corr, closest_to_zero = compute_sorted_correlations(normalized_df, plot=True)
        
        # Display correlation analysis results
        pretty_print_corr("🔻 Ten Smallest Correlations:", sorted_corr.head(10))
        pretty_print_corr("➖ Ten Correlations Closest to Zero:", closest_to_zero)
        pretty_print_corr("🔺 Ten Largest Correlations:", sorted_corr.tail(10))
        
        print(f"\n📋 Analysis Summary:")
        print(f"   • Analyzed {normalized_df.shape[1]} S&P 500 stocks")
        print(f"   • Time period: {start_date} to {normalized_df.index[-1].date()}")
        print(f"   • Total unique correlations: {len(sorted_corr)}")
        print(f"   • Average correlation: {sorted_corr.mean():.4f}")
        print(f"   • Correlation std dev: {sorted_corr.std():.4f}")
    else:
        print("❌ Could not proceed with analysis due to data loading error.")
        print("Please check the CSV file path and ensure the file exists.")