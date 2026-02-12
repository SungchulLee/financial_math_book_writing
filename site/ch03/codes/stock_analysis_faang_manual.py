# ============================================================================
# stock_analysis_NORMALIZED_ADJUST_CLOSE_FAANG_USING_PLOT_MULTIPLE_PRICES_MANUALLY.py
# ============================================================================
import stock_analysis as sto

def analyze_faang_manually():
    """Manual approach with explicit control over each step."""
    tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    start_date = '2024-01-01'
    
    # Store Stock instances
    stocks = {}
    dfs = []
    
    # Load data for each stock (method chaining approach)
    for ticker in tickers:
        stock = sto.USStock(ticker).get_data(start_date)
        stocks[ticker] = stock
        dfs.append(stock.df)
    
    # Create the comparison plot using our plotting function
    sto.plot_multiple_prices(dfs, tickers, normalize=True, figsize=(12, 6))
    
    return stocks

stocks_manual = analyze_faang_manually()