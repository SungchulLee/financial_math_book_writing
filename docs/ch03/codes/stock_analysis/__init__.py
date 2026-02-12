# ============================================================================
# stock_analysis/__init__.py
# ============================================================================
"""
Stock Analysis
==============

File structure:
stock_analysis/
├── __init__.py
├── base.py                          # Base classes for stock analysis
├── stocks.py                        # Individual stock analysis and metrics
├── analysis/
│   ├── __init__.py
│   ├── returns.py                   # Return calculations and transformations
│   └── statistics.py                # Statistical analysis and risk metrics
├── data/                            # Data storage directory
├── krx/                            # Korean Exchange (KRX) specific data
├── sp500/
│   ├── __init__.py
│   ├── analysis.py                  # S&P 500 specific analysis
│   ├── composition.py               # Index composition and sector analysis
│   ├── data_downloader.py           # Market data acquisition
│   └── historical_data.py           # Historical data processing
└── visualization/
    ├── __init__.py
    ├── basic_plots.py               # Basic financial charts and plots
    ├── candlestick.py              # OHLC candlestick charts
    └── return_plots.py             # Return distribution and time series plots

Stock Analysis Applications:
- Empirical return distribution analysis
- Volatility clustering and GARCH modeling
- Risk metrics (VaR, CVaR, Sharpe ratios)
- Market regime identification
- Correlation and factor analysis
"""

# Core stock classes
from .stocks import (
    USStock,
    CryptoStock,
    InternationalStock
)

# S&P 500 market data
from .sp500 import (
    download_sp500,
    load_data_from_csv
)

__version__ = "1.0.0"
__author__ = "sungchul@yonsei.ac.kr"
__description__ = "Stock market analysis with multi-market support and risk metrics"