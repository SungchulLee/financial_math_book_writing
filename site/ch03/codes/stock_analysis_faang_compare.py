# ============================================================================
# stock_analysis_NORMALIZED_ADJUST_CLOSE_FAANG_USING_COMPARE_STOCKS.py
# ============================================================================
import stock_analysis as sto

tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
start_date = '2024-01-01'
end_date = '2025-12-31'
stocks = sto.compare_stocks(tickers, start_date, end_date, normalize=True)