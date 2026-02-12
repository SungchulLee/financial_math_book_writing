# ============================================================================
# stock_analysis_COMPARE_ETF_TRACKING_ERROR.py
# ============================================================================
import stock_analysis as sto

def compare_etf_tracking_error():
    """
    Example: Compare different time periods to understand when ETF tracking error might occur.
    """
    # Compare 2020 vs 2024 composition
    comparison = sto.compare_sp500_compositions('2020', '2024')
    
    print(f"Composition stability: {comparison['stability_rate']:.1%}")
    print(f"Total changes: {comparison['total_changes']}")
    
    if comparison['total_changes'] > 20:
        print("⚠️  High turnover period - ETF tracking error likely")
    else:
        print("✅ Stable period - low tracking error expected")

compare_etf_tracking_error()