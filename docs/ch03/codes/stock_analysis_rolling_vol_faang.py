# ============================================================================
# stock_analysis_1M_ROLLING_VOLATILITY_FAANG.py
# ============================================================================
import matplotlib.pyplot as plt
import stock_analysis as sto
#from stock_analysis import USStock  # Import from your stock_analysis package

# Define tickers and date for volatility comparison
tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']    # FAANG stocks for comparison
start_date = '2024-07-01'                             # Starting date for analysis

# Create figure for volatility comparison
fig, ax = plt.subplots(figsize=(12, 5))

# Analyze each stock and plot rolling volatility
for ticker in tickers:
    # Initialize stock object and perform analysis
    stock = sto.USStock(ticker)                            # Create USStock instance
    stock.get_data(start_date)                         # Download historical data (new method, no warning)
    stock.compute_returns()                            # Calculate simple and log returns
    
    # Calculate 1-month (21 trading days) rolling volatility
    stock.df['1M_Vol'] = stock.df['Return'].rolling(21).std()
    
    # Convert pandas data to numpy arrays to avoid matplotlib indexing issues
    dates = stock.df.index.values                     # Convert DatetimeIndex to numpy array
    volatility = stock.df['1M_Vol'].values            # Convert pandas Series to numpy array
    
    # Plot rolling volatility for this stock
    ax.plot(dates, volatility, label=ticker, linewidth=2)

# Customize the volatility comparison chart
ax.set_title('1-Month Rolling Volatility Comparison (FAANG Stocks)', fontsize=14, fontweight='bold')
ax.set_xlabel('Date', fontsize=12)                    # X-axis label
ax.set_ylabel('1-Month Rolling Volatility', fontsize=12)  # Y-axis label
ax.legend(loc='best', fontsize=10)                    # Add legend with stock symbols
ax.grid(True, alpha=0.3)                             # Add subtle grid for readability

# Format the plot for better presentation
fig.tight_layout()                                    # Automatically adjust subplot spacing
plt.show()                                           # Display the volatility comparison