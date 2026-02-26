# ============================================================================
# stock_analysis/base.py
# ============================================================================
import pandas as pd
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod


class Stock(ABC):
    """
    Abstract base class for stock analysis.
    
    This class defines the interface that all stock implementations should follow.
    Subclasses should implement the abstract methods to provide specific functionality.
    """
    
    def __init__(self, ticker: str, trading_days_per_year: int = 252):
        """
        Initialize the Stock object.
        
        Args:
            ticker: Stock ticker symbol
            trading_days_per_year: Number of trading days per year for annualization
        """
        self.ticker = ticker.upper().strip()
        self.trading_days_per_year = trading_days_per_year
        self.df: Optional[pd.DataFrame] = None
        self.company_info: Dict[str, Any] = {}
        self.statistics: Dict[str, Any] = {}
        
        # Validate ticker
        if not self.ticker:
            raise ValueError("Ticker cannot be empty")
    
    @abstractmethod
    def get_data(self, start_date: str, end_date: Optional[str] = None) -> 'Stock':
        """
        Fetch historical data for the stock.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format (optional)
        
        Returns:
            Self for method chaining
        """
        pass
    
    @abstractmethod
    def analyze(self) -> 'Stock':
        """
        Perform analysis on the stock data.
        
        Returns:
            Self for method chaining
        """
        pass
    
    @abstractmethod
    def plot(self, plot_type: str = 'close') -> 'Stock':
        """
        Create visualizations of the stock data.
        
        Args:
            plot_type: Type of plot to create
        
        Returns:
            Self for method chaining
        """
        pass
    
    def has_data(self) -> bool:
        """
        Check if stock data is available.
        
        Returns:
            True if data is available, False otherwise
        """
        return (self.df is not None) and (not self.df.empty)
    
    def get_price_range(self) -> Dict[str, float]:
        """
        Get price range information.
        
        Returns:
            Dictionary with price range statistics
        """
        if not self.has_data():
            raise ValueError("No data available. Call get_data() first.")
        
        return {
            'min': self.df['Close'].min(),
            'max': self.df['Close'].max(),
            'current': self.df['Close'].iloc[-1],
            'first': self.df['Close'].iloc[0],
            'total_return': (self.df['Close'].iloc[-1] / self.df['Close'].iloc[0] - 1) * 100
        }
    
    def get_data_info(self) -> Dict[str, Any]:
        """
        Get information about the loaded data.
        
        Returns:
            Dictionary with data information
        """
        if not self.has_data():
            return {'status': 'No data loaded'}
        
        return {
            'ticker': self.ticker,
            'start_date': self.df.index[0].strftime('%Y-%m-%d'),
            'end_date': self.df.index[-1].strftime('%Y-%m-%d'),
            'num_observations': len(self.df),
            'columns': list(self.df.columns),
            'has_returns': 'Return' in self.df.columns,
            'has_log_returns': 'Return_Log' in self.df.columns
        }
    
    def summary(self) -> Dict[str, Any]:
        """
        Get a summary of the stock data and analysis.
        
        Returns:
            Dictionary with summary information
        """
        summary_data = {
            'ticker': self.ticker,
            'trading_days_per_year': self.trading_days_per_year,
            'data_info': self.get_data_info()
        }
        
        if self.has_data():
            summary_data['price_range'] = self.get_price_range()
        
        if self.company_info:
            summary_data['company_info'] = self.company_info
        
        if self.statistics:
            summary_data['statistics'] = self.statistics
        
        return summary_data
    
    def __repr__(self) -> str:
        """String representation of the Stock object."""
        status = "with data" if self.has_data() else "no data"
        return f"{self.__class__.__name__}(ticker='{self.ticker}', {status})"
    
    def __str__(self) -> str:
        """Human-readable string representation."""
        if not self.has_data():
            return f"Stock {self.ticker} (no data loaded)"
        
        data_info = self.get_data_info()
        return (f"Stock {self.ticker}\n"
                f"Data: {data_info['start_date']} to {data_info['end_date']}\n"
                f"Observations: {data_info['num_observations']}")
    
    def reset(self) -> 'Stock':
        """
        Reset the stock object to initial state.
        
        Returns:
            Self for method chaining
        """
        self.df = None
        self.company_info = {}
        self.statistics = {}
        return self