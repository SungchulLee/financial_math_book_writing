# ============================================================================
# stock_analysis_DEVELOP_DEFENSIVE_STRATEGY.py
# ============================================================================
import stock_analysis as sto

def develop_defensive_strategy():
    """
    Example: Identify companies that survived multiple crises for defensive investing.
    """
    # Find companies that survived ALL major crises since 2000
    dot_com_survivors = sto.get_sp500_survivors('2000', '2002')['survivors']
    financial_crisis_survivors = sto.get_sp500_survivors('2007', '2009')['survivors']
    covid_survivors = sto.get_sp500_survivors('2020', '2021')['survivors']
    
    # Companies that survived all three crises
    super_survivors = list(set(dot_com_survivors) & 
                          set(financial_crisis_survivors) & 
                          set(covid_survivors))
    
    print(f"Super survivors (survived all 3 crises): {len(super_survivors)}")
    print(f"Examples: {super_survivors[:10]}")
    
    # These could form the basis of a defensive portfolio

develop_defensive_strategy()