# ============================================================================
# stock_analysis_BACKTEST_STRATEGY_WITHOUT_SURVIVORSHIP_BIAS.py
# ============================================================================
import stock_analysis as sto

def backtest_strategy_without_survivorship_bias():
    """
    Example: Backtest a momentum strategy using historical S&P 500 composition.
    This avoids survivorship bias by using the actual composition from each period.
    """
    # Research question: "How would a momentum strategy perform during the 2008 crisis?"
    crisis_start = '2007'
    crisis_end = '2009'
    
    # Get the ACTUAL S&P 500 composition at the start of 2007
    # (not the current composition which would be survivorship biased)
    pre_crisis_tickers = sto.get_sp500_tickers_by_year(crisis_start, include_index=False)
    
    print(f"Backtesting {len(pre_crisis_tickers)} companies that were ACTUALLY in S&P 500 in {crisis_start}")
    print("This avoids survivorship bias - we're not using companies that survived until today")
    
    # Check which companies survived the crisis
    survivors = sto.get_sp500_survivors(crisis_start, crisis_end)
    print(f"Survival rate during crisis: {survivors['survival_rate']:.1%}")
    print(f"Companies that didn't survive: {len(survivors['dropouts'])}")
    
    # Example dropouts (companies that were removed during crisis)
    notable_dropouts = survivors['dropouts'][:5]
    print(f"Notable crisis casualties: {notable_dropouts}")
    
    return pre_crisis_tickers

backtest_strategy_without_survivorship_bias()