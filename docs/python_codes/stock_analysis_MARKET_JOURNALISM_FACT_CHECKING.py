# ============================================================================
# stock_analysis_MARKET_JOURNALISM_FACT_CHECKING.py
# ============================================================================
import stock_analysis as sto

def market_journalism_fact_checking():
    """
    Example: Fact-check claims about S&P 500 historical performance.
    """
    # Claim: "Tech companies dominated S&P 500 in 2000"
    # Let's check this with actual data
    
    sp500_2000 = sto.get_sp500_tickers_by_year('2000', include_index=False)
    
    # Known tech companies in 2000
    tech_companies_2000 = ['MSFT', 'INTC', 'CSCO', 'ORCL', 'IBM']
    tech_in_sp500 = [ticker for ticker in tech_companies_2000 if ticker in sp500_2000]
    
    print(f"Tech companies in S&P 500 in 2000: {len(tech_in_sp500)}")
    print(f"Total S&P 500 companies: {len(sp500_2000)}")
    print(f"Tech percentage: {len(tech_in_sp500)/len(sp500_2000):.1%}")

market_journalism_fact_checking()