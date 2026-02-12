# ============================================================================
# stock_analysis_CREATE_SURVIVORSHIP_BIAS_STUDY.py
# ============================================================================
import stock_analysis as sto

def create_survivorship_bias_study():
    """
    Example: Demonstrate the impact of survivorship bias in long-term studies.
    """
    # Compare 20-year returns using different approaches
    start_year = '2000'
    end_year = '2020'
    
    # Approach 1: Survivorship biased (using current S&P 500)
    current_sp500 = sto.get_sp500_tickers_by_year('2024', include_index=False)
    
    # Approach 2: Historically accurate (using actual 2000 composition)
    historical_sp500_2000 = sto.get_sp500_tickers_by_year(start_year, include_index=False)
    
    # Check the difference
    survivors = sto.get_sp500_survivors(start_year, end_year)
    
    print(f"Companies in 2000: {len(historical_sp500_2000)}")
    print(f"Companies that survived to 2020: {len(survivors['survivors'])}")
    print(f"Survivorship bias impact: {len(survivors['dropouts'])} companies excluded")
    
    # This demonstrates why using current S&P 500 for historical studies is misleading

create_survivorship_bias_study()