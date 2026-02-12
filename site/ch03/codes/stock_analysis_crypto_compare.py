# ============================================================================
# stock_analysis_NORMALIZED_ADJUST_CLOSE_AAPL_BTC_ETH_USING_COMPARE_STOCKS.py
# ============================================================================
import stock_analysis as sto

mixed_tickers = ['AAPL', 'BTC-USD', 'ETH-USD']
mixed_types = ['us', 'crypto', 'crypto']
mixed_stocks = sto.compare_stocks(mixed_tickers, '2024-01-01', \
                              stock_types=mixed_types, normalize=True)