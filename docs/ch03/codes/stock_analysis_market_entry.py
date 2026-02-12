# ============================================================================
# stock_analysis_TIME_MARKET_ENTRY_STRATEGY.py
# ============================================================================
import stock_analysis as sto

def time_market_entry_strategy():
    """
    Example: Determine optimal times to enter/exit S&P 500 based on composition changes.
    """
    # Theory: High composition volatility = market stress = potential opportunity
    years_to_analyze = ['2008', '2009', '2020', '2021']
    
    for year in years_to_analyze:
        report = sto.generate_sp500_analysis_report(year, year)
        volatility = report['volatility_metrics']['avg_changes_per_year']
        
        print(f"{year}: {volatility:.0f} composition changes")
        if volatility > 15:
            print(f"  🔥 High volatility - potential opportunity")
        else:
            print(f"  📈 Normal period")

time_market_entry_strategy()