# ============================================================================
# stock_analysis_DAILY_RETURN_VS_DAILY_LOG_RETURN.py
# ============================================================================
import matplotlib.pyplot as plt 
import stock_analysis as sto

# Stock analysis configuration
TICKER = "WMT"                    # Walmart stock ticker symbol
START_DATE = "2020-07-01"         # Starting date for historical data retrieval

# Initialize stock object and perform analysis
stock = sto.USStock(TICKER)                          # Create USStock instance for Walmart
stock.get_data(start_date=START_DATE)            # Download historical data (new method, no warning)
stock.compute_returns()                          # Calculate simple and log returns
stock.compute_mu_and_sigma()                     # Compute mean (mu) and standard deviation (sigma)

# Create scatter plot comparing simple returns vs log returns
fig, ax = plt.subplots(figsize=(12, 3))

# Convert pandas Series to numpy arrays to avoid matplotlib indexing issues
returns = stock.df['Return'].values           # Convert to numpy array
log_returns = stock.df['Return_Log'].values   # Convert to numpy array

# Plot relationship between simple returns and log returns
ax.plot(returns, log_returns, "ok", label="Log Return", ms=3)  # Scatter plot points
ax.plot(returns, returns, "--r", label="Return")               # Reference line (y=x)

# Format the plot
ax.set_xlabel('Return')                                    # Label x-axis as simple return
ax.set_ylabel('Log Return')                               # Label y-axis as log return
ax.set_title('Relationship between Return and Log Return') # Descriptive title
ax.legend()                                               # Add legend to distinguish data series

# Display the plot
plt.show()