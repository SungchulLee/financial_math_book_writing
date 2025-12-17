import yfinance as yf
import pandas as pd
from typing import Optional


def get_historical_prices(ticker: str, start_date: str, end_date: Optional[str] = None) -> pd.DataFrame:
    """
    Download historical price data using yfinance.
    
    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format (optional, defaults to today)
    
    Returns:
        DataFrame with OHLCV data
    
    Raises:
        ValueError: If no data found for the given ticker and date range
    """
    try:
        ticker_obj = yf.Ticker(ticker)
        df = ticker_obj.history(start=start_date, end=end_date)
        
        if df.empty:
            raise ValueError(f"No data found for ticker '{ticker}' in the given date range.")
        
        return df
    
    except Exception as e:
        raise ValueError(f"Error fetching data for {ticker}: {str(e)}")


def get_crypto_data(ticker: str, start_date: str, end_date: Optional[str] = None) -> pd.DataFrame:
    """
    Fetch cryptocurrency data.
    
    Args:
        ticker: Crypto ticker symbol (e.g., 'BTC-USD', 'ETH-USD')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format (optional, defaults to today)
    
    Returns:
        DataFrame with OHLCV data
    
    Note:
        Currently uses yfinance for crypto data, but can be extended
        to use specialized crypto APIs like CoinGecko, Binance, etc.
    """
    # For now, using yfinance which supports major crypto pairs
    # This can be extended to use specialized crypto APIs
    try:
        # Ensure ticker has the right format for yfinance crypto
        if not ticker.endswith('-USD') and not ticker.endswith('-USDT'):
            ticker = f"{ticker}-USD"
        
        return get_historical_prices(ticker, start_date, end_date)
    
    except Exception as e:
        raise ValueError(f"Error fetching crypto data for {ticker}: {str(e)}")


def validate_ticker(ticker: str) -> str:
    """
    Validate and normalize ticker symbol.
    
    Args:
        ticker: Raw ticker symbol
    
    Returns:
        Normalized ticker symbol
    """
    if not ticker or not isinstance(ticker, str):
        raise ValueError("Ticker must be a non-empty string")
    
    return ticker.upper().strip()


def get_company_info(ticker: str) -> dict:
    """
    Get basic company information.
    
    Args:
        ticker: Stock ticker symbol
    
    Returns:
        Dictionary with company information
    """
    try:
        ticker_obj = yf.Ticker(ticker)
        info = ticker_obj.info
        
        # Extract key information
        return {
            'name': info.get('longName', ticker),
            'sector': info.get('sector', 'Unknown'),
            'industry': info.get('industry', 'Unknown'),
            'market_cap': info.get('marketCap', 0),
            'currency': info.get('currency', 'USD'),
            'country': info.get('country', 'Unknown'),
            'website': info.get('website', ''),
            'business_summary': info.get('longBusinessSummary', '')[:200] + '...' if info.get('longBusinessSummary') else ''
        }
    
    except Exception as e:
        return {'name': ticker, 'error': str(e)}