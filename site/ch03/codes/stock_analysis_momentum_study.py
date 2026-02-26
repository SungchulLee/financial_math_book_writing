# ============================================================================
# stock_analysis_STUDY_MOMENTUM_WITH_HISTORICAL_ACCURACY.py
# ============================================================================
import stock_analysis as sto

def study_momentum_with_historical_accuracy():
    """
    Example: Study momentum effect using historically accurate S&P 500 data.
    """
    # Research: "Does momentum work better in stable vs volatile periods?"
    
    # Get compositions for different volatility periods
    stable_period_tickers = sto.get_sp500_tickers_by_year('2017', include_index=False)  # Stable year
    volatile_period_tickers = sto.get_sp500_tickers_by_year('2008', include_index=False)  # Crisis year
    
    print(f"Stable period (2017): {len(stable_period_tickers)} companies")
    print(f"Volatile period (2008): {len(volatile_period_tickers)} companies")
    
    # This would be followed by performance analysis
    # using the historically accurate ticker lists

study_momentum_with_historical_accuracy()