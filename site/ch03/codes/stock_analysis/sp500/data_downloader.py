# ============================================================================
# stock_analysis/sp500/data_downloader.py
# ============================================================================
import os
import yfinance as yf
import pandas as pd
import numpy as np
import time
import warnings
from typing import Dict, Tuple, Optional
from .composition import get_sp500_tickers_by_year


def download_sp500(year: str, save_csv: bool = False, sample_size: Optional[int] = None, 
                   delay: float = 0.2) -> Tuple[Dict[str, pd.DataFrame], pd.DataFrame]:
    """
    Download S&P 500 data for a specific year.
    
    Args:
        year: Year as string (e.g., '2020')
        save_csv: Whether to save data as CSV to ./stock_analysis/sp500/sp500_data/
        sample_size: If provided, download only this many stocks (for testing)
        delay: Delay between downloads to avoid rate limiting
        
    Returns:
        Tuple of (stocks_data_dict, sp500_index_dataframe)
    """
    
    print(f"🚀 Downloading S&P 500 data for {year}...")
    
    # Get tickers
    tickers = get_sp500_tickers_by_year(year, include_index=False)
    
    # If sample requested, take first N stocks
    if sample_size:
        tickers = tickers[:sample_size]
        print(f"📊 Sampling {sample_size} stocks...")
    
    print(f"📊 Downloading {len(tickers)} stocks...")
    
    # Date range
    start_date = f'{year}-01-01'
    end_date = f'{int(year)+1}-01-01'
    
    # Download individual stocks
    stocks_data = {}
    failed_count = 0
    
    for i, ticker in enumerate(tickers):
        try:
            ticker_obj = yf.Ticker(ticker)
            data = ticker_obj.history(start=start_date, end=end_date)
            
            if not data.empty:
                stocks_data[ticker] = data
            else:
                failed_count += 1
            
            # Progress and rate limiting
            if (i + 1) % 50 == 0:
                print(f"   📈 Progress: {i+1}/{len(tickers)} ({len(stocks_data)} successful)")
            
            time.sleep(delay)
            
        except Exception as e:
            failed_count += 1
            if failed_count <= 5:  # Only show first 5 errors
                print(f"   ❌ Failed to download {ticker}: {e}")
    
    print(f"✅ Downloaded {len(stocks_data)} stocks successfully")
    if failed_count > 0:
        print(f"❌ Failed to download {failed_count} stocks")
    
    # Download S&P 500 index
    print("📊 Downloading S&P 500 index...")
    try:
        sp500_ticker = yf.Ticker('^GSPC')
        sp500_data = sp500_ticker.history(start=start_date, end=end_date)
        print(f"✅ S&P 500 index downloaded: {len(sp500_data)} days")
    except Exception as e:
        print(f"❌ Failed to download S&P 500 index: {e}")
        sp500_data = pd.DataFrame()
    
    # Save CSV if requested
    if save_csv:
        _save_to_csv(stocks_data, sp500_data, year)
    
    return stocks_data, sp500_data


def create_returns_matrix(year: str, return_type: str = 'simple') -> pd.DataFrame:
    """
    Create a returns matrix for all S&P 500 stocks from a specific year.
    
    Args:
        year: Year as string (e.g., '2020')
        return_type: 'simple' for arithmetic returns, 'log' for logarithmic returns
        
    Returns:
        DataFrame with dates as index and ticker symbols as columns
    """
    
    print(f"📊 Creating {return_type} returns matrix for S&P 500 {year}...")
    
    # Download all stock data (excluding index for returns matrix)
    stocks_data, _ = download_sp500(year)
    
    # Extract closing prices and calculate returns
    all_returns = {}
    
    for ticker, data in stocks_data.items():
        if 'Close' in data.columns and len(data) > 1:
            prices = data['Close']
            
            if return_type == 'simple':
                returns = prices.pct_change()
            elif return_type == 'log':
                returns = np.log(prices / prices.shift(1))
            else:
                raise ValueError("return_type must be 'simple' or 'log'")
            
            all_returns[ticker] = returns
    
    # Combine into a single DataFrame
    returns_df = pd.DataFrame(all_returns)
    returns_df.dropna(how='all', inplace=True)  # Remove days with all NaN
    
    print(f"✅ Created returns matrix: {returns_df.shape[0]} days × {returns_df.shape[1]} stocks")
    
    return returns_df


def get_summary(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Get a summary of downloaded S&P 500 data.
    
    Args:
        data: Dictionary of DataFrames
        
    Returns:
        DataFrame with summary statistics for each ticker
    """
    
    summary_data = []
    
    for ticker, df in data.items():
        if not df.empty and 'Close' in df.columns:
            summary_data.append({
                'ticker': ticker,
                'start_date': df.index[0],
                'end_date': df.index[-1],
                'num_days': len(df),
                'start_price': df['Close'].iloc[0],
                'end_price': df['Close'].iloc[-1],
                'total_return': (df['Close'].iloc[-1] / df['Close'].iloc[0] - 1) * 100,
                'max_price': df['Close'].max(),
                'min_price': df['Close'].min(),
                'avg_volume': df['Volume'].mean() if 'Volume' in df.columns else np.nan
            })
    
    summary_df = pd.DataFrame(summary_data)
    if not summary_df.empty:
        summary_df.set_index('ticker', inplace=True)
    
    return summary_df


def save_data(data: Dict[str, pd.DataFrame], year: str, 
              directory: str = './sp500_data') -> str:
    """
    Save downloaded S&P 500 data to pickle file.
    
    Args:
        data: Dictionary of DataFrames
        year: Year string for filename
        directory: Directory to save files
        
    Returns:
        Path to saved files
    """
    
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # Save data
    stocks_path = os.path.join(directory, f'sp500_data_{year}.pkl')
    pd.to_pickle(data, stocks_path)
    print(f"💾 Saved {len(data)} assets to {stocks_path}")
    
    return directory


def load_data(year: str, directory: str = './sp500_data') -> Dict[str, pd.DataFrame]:
    """
    Load previously saved S&P 500 data.
    
    Args:
        year: Year string
        directory: Directory containing saved files
        
    Returns:
        Dictionary of DataFrames
    """
    
    data_path = os.path.join(directory, f'sp500_data_{year}.pkl')
    
    if os.path.exists(data_path):
        data = pd.read_pickle(data_path)
        print(f"📁 Loaded {len(data)} assets from {data_path}")
        return data
    else:
        raise FileNotFoundError(f"Data file not found: {data_path}")
    

def load_data_from_csv(csv_path='./sp500_data/sp500_2024.csv'):
    """
    Load S&P 500 data from existing CSV file.
    
    Args:
        csv_path: Path to the CSV file containing S&P 500 data
        
    Returns:
        DataFrame with S&P 500 stock prices
    """
    try:
        # Load the CSV file with date as index
        df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
        print(f"✅ Loaded S&P 500 data from {csv_path}")
        print(f"📊 Data shape: {df.shape[0]} days × {df.shape[1]} stocks")
        print(f"📅 Date range: {df.index[0].date()} to {df.index[-1].date()}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: Could not find CSV file at {csv_path}")
        print("Please ensure the file exists or update the path.")
        return None
    except Exception as e:
        print(f"❌ Error loading CSV file: {e}")
        return None


def quick_test():
    """Quick test with just a few popular stocks."""
    
    print("🧪 Quick test download...")
    
    # Test with just 5 popular stocks
    test_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    year = '2020'
    start_date = f'{year}-01-01'
    end_date = f'{int(year)+1}-01-01'
    
    results = {}
    
    for ticker in test_tickers:
        try:
            print(f"   Downloading {ticker}...")
            ticker_obj = yf.Ticker(ticker)
            data = ticker_obj.history(start=start_date, end=end_date)
            
            if not data.empty:
                results[ticker] = data
                print(f"   ✅ {ticker}: {len(data)} days")
            else:
                print(f"   ❌ {ticker}: No data")
                
        except Exception as e:
            print(f"   ❌ {ticker}: Error - {e}")
    
    return results


def _save_to_csv(stocks_data: Dict[str, pd.DataFrame], sp500_data: pd.DataFrame, year: str):
    """
    Internal function to save data as CSV (from the original bulletproof function).
    """
    
    print(f"\n💾 Saving data to CSV...")
    
    # Create target directory
    target_dir = os.path.join('.', 'stock_analysis', 'sp500', 'sp500_data')
    os.makedirs(target_dir, exist_ok=True)
    
    # Extract close prices from all stocks
    all_closes = {}
    for ticker, data in stocks_data.items():
        if 'Close' in data.columns:
            all_closes[ticker] = data['Close']
    
    # Add S&P 500 index if available
    if not sp500_data.empty and 'Close' in sp500_data.columns:
        all_closes['^GSPC'] = sp500_data['Close']
    
    # Create combined DataFrame
    combined_df = pd.DataFrame(all_closes)
    
    # Save to CSV
    save_path = os.path.join(target_dir, f'sp500_{year}.csv')
    combined_df.to_csv(save_path)
    
    if os.path.exists(save_path):
        file_size = os.path.getsize(save_path) / (1024 * 1024)  # MB
        abs_path = os.path.abspath(save_path)
        print(f"✅ Successfully saved CSV!")
        print(f"   📍 Full path: {abs_path}")
        print(f"   📦 Size: {file_size:.2f} MB")
        print(f"   📊 Data: {combined_df.shape[0]} days × {combined_df.shape[1]} assets")


import warnings


# Backwards compatibility aliases with deprecation warnings
def download_sp500_data_simple(year: str, delay: float = 0.2) -> Tuple[Dict[str, pd.DataFrame], pd.DataFrame]:
    """DEPRECATED: Use download_sp500() instead."""
    warnings.warn(
        "download_sp500_data_simple is deprecated and will be removed in a future version. "
        "Use download_sp500() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return download_sp500(year, delay=delay)


def download_sp500_simple(year: str, delay: float = 0.2) -> Tuple[Dict[str, pd.DataFrame], pd.DataFrame]:
    """DEPRECATED: Use download_sp500() instead."""
    warnings.warn(
        "download_sp500_simple is deprecated and will be removed in a future version. "
        "Use download_sp500() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return download_sp500(year, delay=delay)


def download_sp500_sample(year: str, num_stocks: int = 20) -> Dict[str, pd.DataFrame]:
    """DEPRECATED: Use download_sp500(sample_size=num_stocks) instead."""
    warnings.warn(
        "download_sp500_sample is deprecated and will be removed in a future version. "
        "Use download_sp500(sample_size=num_stocks) instead.",
        DeprecationWarning,
        stacklevel=2
    )
    stocks_data, _ = download_sp500(year, sample_size=num_stocks)
    return stocks_data


def download_sp500_batch(year: str, batch_size: int = 50) -> Dict[str, pd.DataFrame]:
    """DEPRECATED: Use download_sp500() instead."""
    warnings.warn(
        "download_sp500_batch is deprecated and will be removed in a future version. "
        "Use download_sp500() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    stocks_data, _ = download_sp500(year)
    return stocks_data


def download_sp500_csv_bulletproof(year='2020'):
    """DEPRECATED: Use download_sp500(save_csv=True) instead."""
    warnings.warn(
        "download_sp500_csv_bulletproof is deprecated and will be removed in a future version. "
        "Use download_sp500(save_csv=True) instead.",
        DeprecationWarning,
        stacklevel=2
    )
    stocks_data, sp500_data = download_sp500(year, save_csv=True)
    
    # Return format matching original function
    target_dir = os.path.join('.', 'stock_analysis', 'sp500', 'sp500_data')
    save_path = os.path.join(target_dir, f'sp500_{year}.csv')
    
    # Create combined DataFrame for return value
    all_closes = {}
    for ticker, data in stocks_data.items():
        if 'Close' in data.columns:
            all_closes[ticker] = data['Close']
    
    if not sp500_data.empty and 'Close' in sp500_data.columns:
        all_closes['^GSPC'] = sp500_data['Close']
    
    combined_df = pd.DataFrame(all_closes)
    return combined_df, save_path


def create_sp500_returns_matrix(year: str, return_type: str = 'simple') -> pd.DataFrame:
    """DEPRECATED: Use create_returns_matrix() instead."""
    warnings.warn(
        "create_sp500_returns_matrix is deprecated and will be removed in a future version. "
        "Use create_returns_matrix() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return create_returns_matrix(year, return_type)


def get_sp500_data_summary(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """DEPRECATED: Use get_summary() instead."""
    warnings.warn(
        "get_sp500_data_summary is deprecated and will be removed in a future version. "
        "Use get_summary() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return get_summary(data)


def save_sp500_data(data: Dict[str, pd.DataFrame], year: str, 
                   directory: str = './sp500_data') -> str:
    """DEPRECATED: Use save_data() instead."""
    warnings.warn(
        "save_sp500_data is deprecated and will be removed in a future version. "
        "Use save_data() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return save_data(data, year, directory)


def load_sp500_data(year: str, directory: str = './sp500_data') -> Dict[str, pd.DataFrame]:
    """DEPRECATED: Use load_data() instead."""
    warnings.warn(
        "load_sp500_data is deprecated and will be removed in a future version. "
        "Use load_data() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return load_data(year, directory)


def quick_test_download():
    """DEPRECATED: Use quick_test() instead."""
    warnings.warn(
        "quick_test_download is deprecated and will be removed in a future version. "
        "Use quick_test() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    return quick_test()


# Main alias for backwards compatibility
download_sp500_data = download_sp500_data_simple


if __name__ == "__main__":
    print("S&P 500 Data Downloader - Simplified Version")
    print("\nNew functions:")
    print("- download_sp500(year, save_csv=False, sample_size=None)")
    print("- create_returns_matrix(year)")
    print("- get_summary(data)")
    print("- save_data(data, year)")
    print("- load_data(year)")
    print("- quick_test()")
    print("\nDeprecated functions (will show warnings):")
    print("- download_sp500_data_simple, download_sp500_simple")
    print("- download_sp500_sample, download_sp500_batch")
    print("- download_sp500_csv_bulletproof")
    print("- create_sp500_returns_matrix")
    print("- get_sp500_data_summary")
    print("- save_sp500_data, load_sp500_data")
    print("- quick_test_download")