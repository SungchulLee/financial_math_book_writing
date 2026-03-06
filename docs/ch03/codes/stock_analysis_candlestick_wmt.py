"""
Stock Analysis Candlestick Wmt

Educational script demonstrating stock analysis candlestick wmt concepts.
"""

# ============================================================================
# stock_analysis_CANDLESTICK_WITH_VOLUME_WMT.py
# ============================================================================
import stock_analysis as sto


if __name__ == "__main__":
    sto.USStock("WMT").get_data("2024-12-01").plot('ohlc')       