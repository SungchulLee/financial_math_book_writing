# ============================================================================
# stock_analysis_CREATE_HISTORICAL_SP500_PORTFOLIO.py
# ============================================================================
import stock_analysis as sto

def create_historical_sp500_portfolio():
    """
    Example: Create a portfolio that exactly matches S&P 500 composition for a specific year.
    Useful for ETF providers or historical portfolio reconstruction.
    """
    target_year = '2020'
    portfolio_date = f'{target_year}-01-01'
    
    # Get exact composition for that year
    portfolio_tickers = sto.get_sp500_tickers_by_year(target_year, include_index=False)
    
    print(f"Creating portfolio to match S&P 500 as of {portfolio_date}")
    print(f"Portfolio contains {len(portfolio_tickers)} stocks")
    
    # This could be used to:
    # 1. Calculate historical performance of S&P 500
    # 2. Create a custom ETF with historical composition
    # 3. Compare your portfolio to what S&P 500 actually was
    
    return portfolio_tickers

create_historical_sp500_portfolio()