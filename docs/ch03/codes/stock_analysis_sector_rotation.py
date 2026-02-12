# ============================================================================
# stock_analysis_ACADEMIC_SECTOR_ROTATION_STUDY.py
# ============================================================================
import stock_analysis as sto

def academic_sector_rotation_study():
    """
    Example: Study how S&P 500 sector composition changed over decades.
    """
    print("\n=== Use Case 2: Sector Evolution Study ===")
    
    # Compare composition across decades
    years_to_compare = ['2000', '2010', '2020', '2024']
    
    for year in years_to_compare:
        tickers = sto.get_sp500_tickers_by_year(year, include_index=False)
        print(f"{year}: {len(tickers)} companies")
    
    # Study tech companies that entered during different periods
    tech_boom_2000 = sto.get_sp500_tickers_by_year('2000', include_index=False)
    current_sp500 = sto.get_sp500_tickers_by_year('2024', include_index=False)
    
    # This would typically be followed by sector analysis using company metadata
    print(f"Companies added since 2000: {len(set(current_sp500) - set(tech_boom_2000))}")

academic_sector_rotation_study()