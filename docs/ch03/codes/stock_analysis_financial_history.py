# ============================================================================
# stock_analysis_FINANCIAL_HISTORY_LESSON.py
# ============================================================================
import stock_analysis as sto

def create_financial_history_lesson():
    """
    Example: Create educational content about market evolution.
    """
    print("\n=== Use Case 11: Financial Education ===")
    
    print("S&P 500 Evolution Story:")
    
    # Tell the story of major changes
    milestones = [
        ('2001', 'Amazon enters S&P 500 (survived dot-com crash)'),
        ('2008', 'Lehman Brothers removed (bankruptcy)'),
        ('2014', 'Facebook joins S&P 500'),
        ('2020', 'Tesla enters S&P 500 (EV revolution)'),
    ]
    
    for year, event in milestones:
        tickers = sto.get_sp500_tickers_by_year(year, include_index=False)
        print(f"{year}: {event} (Total: {len(tickers)} companies)")

create_financial_history_lesson()