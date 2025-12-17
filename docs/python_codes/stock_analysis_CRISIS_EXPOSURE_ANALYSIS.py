# ============================================================================
# stock_analysis_CRISIS_EXPOSURE_ANALYSIS.py
# ============================================================================
import stock_analysis as sto

def crisis_exposure_analysis():
    """
    Example: Analyze how different crisis periods affected portfolio composition.
    """
    # Analyze multiple crisis periods
    crisis_periods = [
        ('2000', '2002', 'Dot-com Crash'),
        ('2007', '2009', 'Financial Crisis'), 
        ('2020', '2021', 'COVID Pandemic')
    ]
    
    for start, end, name in crisis_periods:
        survivors = sto.get_sp500_survivors(start, end)
        print(f"{name}: {survivors['survival_rate']:.1%} survival rate")
        print(f"  Dropouts: {len(survivors['dropouts'])}")
        print(f"  New additions: {len(survivors['new_additions'])}")

crisis_exposure_analysis()