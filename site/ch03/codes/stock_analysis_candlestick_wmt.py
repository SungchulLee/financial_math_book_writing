# ============================================================================
# stock_analysis_CANDLESTICK_WITH_VOLUME_WMT.py
# ============================================================================
import stock_analysis as sto

sto.USStock("WMT").get_data("2024-12-01").plot('ohlc')       