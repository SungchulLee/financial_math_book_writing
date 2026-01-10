# ============================================================================
# stock_analysis_NORMALIZED_ADJUST_CLOSE_FAANG_USING_PLOT_MULTIPLE_PRICES_COMPREHENSIVELY.py
# ============================================================================
import stock_analysis as sto

def analyze_faang_comprehensively():
    """Comprehensive analysis with returns and statistics."""
    tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    start_date = '2024-01-01'
    
    stocks = {}
    
    for ticker in tickers:
        # Method chaining: get data, analyze, and store
        stock = sto.USStock(ticker).get_data(start_date).analyze()  # This computes returns, statistics, and moving averages
        stocks[ticker] = stock
        
        # Print summary for each stock
        print(f"\n{ticker} Summary:")
        print(f"  Company: {stock.company_info.get('name', ticker)}")
        print(f"  Data range: {stock.get_data_info()['start_date']} to {stock.get_data_info()['end_date']}")
        print(f"  Total return: {stock.get_price_range()['total_return']:.2f}%")
        
        if stock.statistics:
            arith_stats = stock.statistics.get('arithmetic', {})
            print(f"  Annualized return: {arith_stats.get('mu', 0)*100:.2f}%")
            print(f"  Annualized volatility: {arith_stats.get('sigma', 0)*100:.2f}%")
    
    # Create comparison plot
    dfs = [stock.df for stock in stocks.values()]
    sto.plot_multiple_prices(dfs, tickers, normalize=True, figsize=(12, 6))
    
    return stocks

stocks_comprehensive = analyze_faang_comprehensively()