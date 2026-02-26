# ============================================================================
# stock_analysis_SP500_BASIC_DOWNLOAD.py
# ============================================================================
import yfinance as yf
import pandas as pd
import stock_analysis as sto
import time
from typing import Dict


def get_sample_sp500_data(year: str, num_stocks: int = 20) -> Dict[str, pd.DataFrame]:
    """
    Download a sample of S&P 500 stocks for testing/demo purposes.
    
    Args:
        year: Year as string
        num_stocks: Number of stocks to sample
        
    Returns:
        Dictionary of stock data
    """
    
    print(f"📊 Downloading sample of {num_stocks} S&P 500 stocks for {year}...")
    
    # Get full ticker list and sample
    all_tickers = sto.get_sp500_tickers_by_year(year, include_index=False)
    sample_tickers = all_tickers[:num_stocks]  # Take first N stocks
    
    # Add S&P 500 index
    sample_tickers.append('^GSPC')
    
    # Date range
    start_date = f'{year}-01-01'
    end_date = f'{int(year)+1}-01-01'
    
    sample_data = {}
    
    for ticker in sample_tickers:
        try:
            print(f"   📈 Downloading {ticker}...")
            ticker_obj = yf.Ticker(ticker)
            data = ticker_obj.history(start=start_date, end=end_date)
            
            if not data.empty:
                sample_data[ticker] = data
                print(f"      ✅ Success: {len(data)} days")
            else:
                print(f"      ❌ No data")
            
            time.sleep(0.2)
            
        except Exception as e:
            print(f"      ❌ Error: {e}")
    
    print(f"✅ Sample download complete: {len(sample_data)} assets")
    return sample_data


# Simple usage examples
if __name__ == "__main__":
    
    print("=== S&P 500 Data Download (Compatibility Fixed) ===\n")
    
    # Option 1: Quick test
    print("1. Quick test with popular stocks:")
    test_data = sto.quick_test_download()
    print(f"   Test result: {len(test_data)} stocks downloaded\n")
    
    # Option 2: Sample download
    print("2. Sample download (20 stocks):")
    sample_data = get_sample_sp500_data('2020', num_stocks=10)
    print(f"   Sample result: {len(sample_data)} assets downloaded\n")
    
    # Option 3: Full download instructions
    print("3. For full S&P 500 download, use:")
    print("   stocks, sp500_index = download_sp500_simple('2020')")
    print("   # This downloads all ~500 stocks + S&P 500 index")
    print("   # Takes 5-10 minutes with rate limiting")