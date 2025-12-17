# ============================================================================
# stock_analysis/stock.py
# ============================================================================
from typing import Optional, Dict
import warnings
from .base import Stock
from .data.fetchers import get_historical_prices, get_crypto_data, get_company_info
from .analysis.returns import compute_both_returns
from .analysis.statistics import compute_mu_and_sigma, compute_moving_averages
from .visualization.basic_plots import plot_close, plot_price_with_volume, plot_multiple_prices
from .visualization.return_plots import plot_returns, plot_return_distribution
from .visualization.candlestick import plot_ohlc_with_ma


class USStock(Stock):
    """
    Implementation for US stock market securities.
    """
    
    def get_data(self, start_date: str, end_date: Optional[str] = None) -> 'USStock':
        """
        Fetch historical data for US stock.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format (optional)
        
        Returns:
            Self for method chaining
        """
        # Call the fetcher function and store the data
        self.df = get_historical_prices(self.ticker, start_date, end_date)
        
        # Get company information
        try:
            self.company_info = get_company_info(self.ticker)
        except Exception:
            self.company_info = {'name': self.ticker}
        
        return self
    
    def get_historical_prices(self, start_date: str, end_date: Optional[str] = None) -> 'USStock':
        """
        DEPRECATED: Use get_data() instead.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format (optional)
        
        Returns:
            Self for method chaining
        """
        warnings.warn(
            "get_historical_prices() is deprecated and will be removed in a future version. "
            "Use get_data() instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.get_data(start_date, end_date)
    
    def compute_returns(self) -> 'USStock':
        """
        Compute simple and logarithmic returns.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        # Compute returns using the analysis module
        self.df = compute_both_returns(self.df)
        return self
    
    def compute_mu_and_sigma(self) -> 'USStock':
        """
        Compute mean (mu) and standard deviation (sigma) of returns.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        if 'Return' not in self.df.columns:
            raise ValueError("Returns not computed. Call compute_returns() first.")
        
        # Compute statistics using the analysis module
        self.statistics = compute_mu_and_sigma(self.df, self.trading_days_per_year)
        return self
    
    def analyze(self) -> 'USStock':
        """
        Perform comprehensive analysis on the stock data.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        # Compute returns
        self.df = compute_both_returns(self.df)
        
        # Compute statistics
        self.statistics = compute_mu_and_sigma(self.df, self.trading_days_per_year)
        
        # Add moving averages
        self.df = compute_moving_averages(self.df)
        
        return self
    
    def plot(self, plot_type: str = 'close', **kwargs) -> 'USStock':
        """
        Create visualizations of the stock data.
        
        Args:
            plot_type: Type of plot ('close', 'ohlc', 'returns', 'volume')
            **kwargs: Additional plotting parameters
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        company_name = self.company_info.get('name', self.ticker)
        
        if plot_type == 'close':
            plot_close(self.df, self.ticker, **kwargs)
        elif plot_type == 'volume':
            plot_price_with_volume(self.df, self.ticker, **kwargs)
        elif plot_type == 'ohlc':
            plot_ohlc_with_ma(self.df, self.ticker, company_name=company_name, **kwargs)
        elif plot_type == 'returns':
            if 'Return' not in self.df.columns:
                self.analyze()
            plot_returns(self.df, self.ticker, **kwargs)
        elif plot_type == 'return_dist':
            if 'Return' not in self.df.columns:
                self.analyze()
            plot_return_distribution(self.df, self.ticker, **kwargs)
        else:
            raise ValueError(f"Unknown plot type: {plot_type}")
        
        return self


class CryptoStock(Stock):
    """
    Implementation for cryptocurrency analysis.
    """
    
    def __init__(self, ticker: str, trading_days_per_year: int = 365):
        """
        Initialize crypto stock (crypto trades 24/7, so 365 days).
        
        Args:
            ticker: Crypto ticker symbol
            trading_days_per_year: Days per year (365 for crypto)
        """
        super().__init__(ticker, trading_days_per_year)
    
    def get_data(self, start_date: str, end_date: Optional[str] = None) -> 'CryptoStock':
        """
        Fetch historical data for cryptocurrency.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format (optional)
        
        Returns:
            Self for method chaining
        """
        # Call the crypto data fetcher function
        self.df = get_crypto_data(self.ticker, start_date, end_date)
        
        # Set basic info for crypto
        self.company_info = {
            'name': self.ticker,
            'type': 'Cryptocurrency',
            'market': '24/7'
        }
        
        return self
    
    def get_historical_prices(self, start_date: str, end_date: Optional[str] = None) -> 'CryptoStock':
        """
        DEPRECATED: Use get_data() instead.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format (optional)
        
        Returns:
            Self for method chaining
        """
        warnings.warn(
            "get_historical_prices() is deprecated and will be removed in a future version. "
            "Use get_data() instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.get_data(start_date, end_date)
    
    def compute_returns(self) -> 'CryptoStock':
        """
        Compute simple and logarithmic returns.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        # Compute returns using the analysis module
        self.df = compute_both_returns(self.df)
        return self
    
    def compute_mu_and_sigma(self) -> 'CryptoStock':
        """
        Compute mean (mu) and standard deviation (sigma) of returns.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        if 'Return' not in self.df.columns:
            raise ValueError("Returns not computed. Call compute_returns() first.")
        
        # Compute statistics using the analysis module
        self.statistics = compute_mu_and_sigma(self.df, self.trading_days_per_year)
        return self
    
    def analyze(self) -> 'CryptoStock':
        """
        Perform analysis on cryptocurrency data.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        # Compute returns
        self.df = compute_both_returns(self.df)
        
        # Compute statistics (using 365 days for crypto)
        self.statistics = compute_mu_and_sigma(self.df, self.trading_days_per_year)
        
        # Add moving averages
        self.df = compute_moving_averages(self.df)
        
        return self
    
    def plot(self, plot_type: str = 'close', **kwargs) -> 'CryptoStock':
        """
        Create visualizations of the cryptocurrency data.
        
        Args:
            plot_type: Type of plot ('close', 'ohlc', 'returns', 'volume')
            **kwargs: Additional plotting parameters
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        if plot_type == 'close':
            plot_close(self.df, self.ticker, **kwargs)
        elif plot_type == 'volume':
            plot_price_with_volume(self.df, self.ticker, **kwargs)
        elif plot_type == 'ohlc':
            plot_ohlc_with_ma(self.df, self.ticker, **kwargs)
        elif plot_type == 'returns':
            if 'Return' not in self.df.columns:
                self.analyze()
            plot_returns(self.df, self.ticker, **kwargs)
        elif plot_type == 'return_dist':
            if 'Return' not in self.df.columns:
                self.analyze()
            plot_return_distribution(self.df, self.ticker, **kwargs)
        else:
            raise ValueError(f"Unknown plot type: {plot_type}")
        
        return self


class InternationalStock(Stock):
    """
    Implementation for international stock markets.
    """
    
    def __init__(self, ticker: str, exchange: str = 'UNKNOWN', trading_days_per_year: int = 252):
        """
        Initialize international stock.
        
        Args:
            ticker: Stock ticker symbol
            exchange: Exchange name (e.g., 'LSE', 'TSE', 'FRA')
            trading_days_per_year: Trading days per year for the exchange
        """
        super().__init__(ticker, trading_days_per_year)
        self.exchange = exchange
    
    def get_data(self, start_date: str, end_date: Optional[str] = None) -> 'InternationalStock':
        """
        Fetch historical data for international stock.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format (optional)
        
        Returns:
            Self for method chaining
        """
        # Call the fetcher function
        self.df = get_historical_prices(self.ticker, start_date, end_date)
        
        # Get company information
        try:
            self.company_info = get_company_info(self.ticker)
            self.company_info['exchange'] = self.exchange
        except Exception:
            self.company_info = {'name': self.ticker, 'exchange': self.exchange}
        
        return self
    
    def get_historical_prices(self, start_date: str, end_date: Optional[str] = None) -> 'InternationalStock':
        """
        DEPRECATED: Use get_data() instead.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format (optional)
        
        Returns:
            Self for method chaining
        """
        warnings.warn(
            "get_historical_prices() is deprecated and will be removed in a future version. "
            "Use get_data() instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.get_data(start_date, end_date)
    
    def compute_returns(self) -> 'InternationalStock':
        """
        Compute simple and logarithmic returns.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        # Compute returns using the analysis module
        self.df = compute_both_returns(self.df)
        return self
    
    def compute_mu_and_sigma(self) -> 'InternationalStock':
        """
        Compute mean (mu) and standard deviation (sigma) of returns.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        if 'Return' not in self.df.columns:
            raise ValueError("Returns not computed. Call compute_returns() first.")
        
        # Compute statistics using the analysis module
        self.statistics = compute_mu_and_sigma(self.df, self.trading_days_per_year)
        return self
    
    def analyze(self) -> 'InternationalStock':
        """
        Perform analysis on international stock data.
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        # Compute returns
        self.df = compute_both_returns(self.df)
        
        # Compute statistics
        self.statistics = compute_mu_and_sigma(self.df, self.trading_days_per_year)
        
        # Add moving averages
        self.df = compute_moving_averages(self.df)
        
        return self
    
    def plot(self, plot_type: str = 'close', **kwargs) -> 'InternationalStock':
        """
        Create visualizations of the international stock data.
        
        Args:
            plot_type: Type of plot ('close', 'ohlc', 'returns', 'volume')
            **kwargs: Additional plotting parameters
        
        Returns:
            Self for method chaining
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        company_name = self.company_info.get('name', self.ticker)
        
        if plot_type == 'close':
            plot_close(self.df, self.ticker, **kwargs)
        elif plot_type == 'volume':
            plot_price_with_volume(self.df, self.ticker, **kwargs)
        elif plot_type == 'ohlc':
            plot_ohlc_with_ma(self.df, self.ticker, company_name=company_name, **kwargs)
        elif plot_type == 'returns':
            if 'Return' not in self.df.columns:
                self.analyze()
            plot_returns(self.df, self.ticker, **kwargs)
        elif plot_type == 'return_dist':
            if 'Return' not in self.df.columns:
                self.analyze()
            plot_return_distribution(self.df, self.ticker, **kwargs)
        else:
            raise ValueError(f"Unknown plot type: {plot_type}")
        
        return self


# Utility functions for multi-stock analysis
def create_stock(ticker: str, stock_type: str = 'us') -> Stock:
    """
    Factory function to create appropriate stock instance.
    
    Args:
        ticker: Stock ticker symbol
        stock_type: Type of stock ('us', 'crypto', 'international')
    
    Returns:
        Appropriate Stock instance
    """
    if stock_type.lower() == 'us':
        return USStock(ticker)
    elif stock_type.lower() == 'crypto':
        return CryptoStock(ticker)
    elif stock_type.lower() == 'international':
        return InternationalStock(ticker)
    else:
        raise ValueError(f"Unknown stock type: {stock_type}")


def compare_stocks(tickers: list, start_date: str, end_date: Optional[str] = None,
                  stock_types: Optional[list] = None, normalize: bool = True) -> Dict[str, Stock]:
    """
    Load and compare multiple stocks.
    
    Args:
        tickers: List of ticker symbols
        start_date: Start date for data
        end_date: End date for data (optional)
        stock_types: List of stock types for each ticker (optional, defaults to 'us')
        normalize: Whether to normalize prices for comparison
    
    Returns:
        Dictionary of Stock instances
    """
    if stock_types is None:
        stock_types = ['us'] * len(tickers)
    
    if len(stock_types) != len(tickers):
        raise ValueError("Number of stock types must match number of tickers")
    
    stocks = {}
    dfs = []
    
    # Load data for all stocks
    for ticker, stock_type in zip(tickers, stock_types):
        stock = create_stock(ticker, stock_type)
        stock.get_data(start_date, end_date)
        stocks[ticker] = stock
        dfs.append(stock.df)
    
    # Create comparison plot
    plot_multiple_prices(dfs, tickers, normalize=normalize)
    
    return stocks


def analyze_single_stock(ticker='AAPL'):
    """Detailed analysis of a single stock."""
    # Create and analyze Apple stock
    data = (USStock(ticker)
           .get_data('2024-01-01')
           .analyze())
    
    # Display summary
    print(f"{ticker} Analysis:")
    print(data)
    print(f"Summary: {data.summary()}")
    
    # Create various plots
    data.plot('close')        # Simple price chart
    data.plot('volume')       # Price with volume
    data.plot('ohlc')         # Candlestick with moving averages
    data.plot('returns')      # Comprehensive returns analysis
    
    return data