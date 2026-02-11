import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime as dt

class TreasurySpreadTrade:
    """
    A class for simulating Treasury spread trades based on yield differentials.

    Attributes:
    -----------
    positions : dict
        Dictionary mapping maturities (e.g., '2Y', '5Y') to position weights.
    start : str
        Start date (format: 'YYYY-MM-DD') for historical data.
    end : str
        End date (format: 'YYYY-MM-DD') for historical data.
    data : pd.DataFrame
        DataFrame storing historical yields for each maturity.
    spread : pd.Series
        Time series of computed spread (weighted sum of yields).
    """

    def __init__(self, positions, start="2010-01-01", end=None):
        self.positions = positions
        self.start = pd.to_datetime(start)
        self.end = pd.to_datetime(end) if end else dt.datetime.today()
        self.data = None
        self.spread = None

    def _fred_tickers(self):
        """Map maturity labels to FRED tickers."""
        mapping = {
            "1M": "DGS1MO", "3M": "DGS3MO", "6M": "DGS6MO",
            "1Y": "DGS1", "2Y": "DGS2", "3Y": "DGS3",
            "5Y": "DGS5", "7Y": "DGS7", "10Y": "DGS10",
            "20Y": "DGS20", "30Y": "DGS30"
        }
        return {k: mapping[k] for k in self.positions if k in mapping}

    def load_data(self):
        """Fetch historical yield data from FRED based on selected maturities."""
        tickers = self._fred_tickers()
        df = web.DataReader(list(tickers.values()), "fred", self.start, self.end)
        df.columns = list(tickers.keys())
        self.data = df.dropna()

    def compute_spread(self):
        """Compute the spread time series as a weighted sum of yields."""
        if self.data is None:
            raise ValueError("Data not loaded. Run load_data() first.")

        weights = pd.Series(self.positions)
        self.spread = self.data[list(weights.index)].dot(weights)

    def plot(self):
        """Plot the spread time series."""
        if self.spread is None:
            raise ValueError("Spread not computed. Run compute_spread() first.")

        fig, ax = plt.subplots(figsize=(12, 5))
        self.spread.plot(ax=ax, lw=2, label='Spread')
        ax.axhline(0, color='gray', linestyle='--')
        ax.set_title(f"Treasury Spread Trade: {self.positions}", fontsize=14)
        ax.set_ylabel("Weighted Yield Spread (%)")
        ax.set_xlabel("Date")
        ax.grid(True)
        ax.legend()
        plt.tight_layout()
        plt.show()

    def summary_stats(self):
        """Return summary statistics of the spread."""
        if self.spread is None:
            raise ValueError("Spread not computed. Run compute_spread() first.")

        return {
            "Start Date": self.spread.index[0].date(),
            "End Date": self.spread.index[-1].date(),
            "Mean": self.spread.mean(),
            "Std Dev": self.spread.std(),
            "Min": self.spread.min(),
            "Max": self.spread.max(),
            "Latest": self.spread.iloc[-1]
        }