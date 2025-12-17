# ============================================================================
# stock_analysis_SP500_VALIDATE_HISTORICAL_PORTFOLIO_COMPLIANCE.py
# ============================================================================
import stock_analysis as sto

def validate_historical_portfolio_compliance():
    """
    Example: Validate that a historical portfolio was compliant with S&P 500 at that time.
    """
    # Scenario: Client claims their 2008 portfolio was "S&P 500 compliant"
    client_portfolio_2008 = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'META']  # Suspicious!
    actual_sp500_2008 = sto.get_sp500_tickers_by_year('2008', include_index=False)
    
    # Check compliance
    valid_holdings = [ticker for ticker in client_portfolio_2008 
                     if ticker in actual_sp500_2008]
    invalid_holdings = [ticker for ticker in client_portfolio_2008 
                       if ticker not in actual_sp500_2008]
    
    print(f"Client's 2008 portfolio compliance check:")
    print(f"Valid holdings: {valid_holdings}")
    print(f"Invalid holdings (not in S&P 500 in 2008): {invalid_holdings}")
    
    # TSLA wasn't added until 2020, META (Facebook) until 2014!
    compliance_rate = len(valid_holdings) / len(client_portfolio_2008)
    print(f"Compliance rate: {compliance_rate:.1%}")

validate_historical_portfolio_compliance()