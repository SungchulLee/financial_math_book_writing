# ============================================================================
# stock_analysis_DAILY_RETURN_DISTRIBUTION_AAPL.py
# ============================================================================
import matplotlib.pyplot as plt
import scipy.stats as stats
import stock_analysis as sto

# Stock analysis configuration
TICKER = "AAPL"                      # Apple stock ticker symbol
START_DATE = "2020-07-01"            # Starting date for historical data retrieval
END_DATE = '2022-12-31'              # Ending date for historical data retrieval

# Initialize stock object and perform analysis
stock = sto.USStock(TICKER)                                      # Create USStock instance for Apple
stock.get_data(start_date=START_DATE, end_date=END_DATE)     # Download historical data (new method, no warning)
stock.compute_returns()                                      # Calculate simple and log returns

# Extract return statistics for normal distribution overlay
returns = stock.df['Return'].values                          # Convert to numpy array for matplotlib compatibility
mu = stock.df['Return'].mean()                              # Mean of daily returns
sigma = stock.df['Return'].std()                            # Standard deviation of daily returns

# Create complex subplot layout for detailed distribution analysis
fig = plt.figure(figsize=(12, 6))
ax0 = plt.subplot2grid((2, 3), (0, 0), colspan=3)          # Main histogram (top row, full width)
ax1 = plt.subplot2grid((2, 3), (1, 0))                     # Left tail detail (bottom left)
ax2 = plt.subplot2grid((2, 3), (1, 1))                     # Center peak detail (bottom center)
ax3 = plt.subplot2grid((2, 3), (1, 2))                     # Right tail detail (bottom right)
fig.tight_layout()

# Main histogram with normal distribution overlay
n, bins, _ = ax0.hist(returns, density=True, bins=50)       # Create histogram and get bin data
ax0.plot(bins, stats.norm(mu, sigma).pdf(bins), '--r', alpha=0.5)  # Overlay theoretical normal distribution

print(f"Bins shape: {bins.shape}")                         # Debug: show bins array dimensions

# Detailed view of left tail (first 16 bins)
ax1.bar(bins[:16], n[:16], width=0.005, align='edge')      # Bar chart of left tail frequencies
ax1.plot(bins[:16+1], stats.norm(mu, sigma).pdf(bins[:16+1]), '--r', alpha=0.5)  # Normal curve for left tail

# Detailed view of center peak (around bin 25, ±10 bins with +4 extension)
center_start, center_end = 25-10, 25+4                     # Define center region indices
ax2.bar(bins[center_start:center_end], n[center_start:center_end], width=0.005, align='edge')  # Center bars
ax2.plot(bins[center_start:center_end+1], stats.norm(mu, sigma).pdf(bins[center_start:center_end+1]), '--r', alpha=0.5)  # Center normal curve

# Detailed view of right tail (last 16 bins)
ax3.bar(bins[-16:], n[-16:], width=0.005, align='edge')    # Bar chart of right tail frequencies
ax3.plot(bins[-(15+1):], stats.norm(mu, sigma).pdf(bins[-(15+1):]), '--r', alpha=0.5)  # Normal curve for right tail

# Add descriptive titles to each subplot
ax0.set_title('Daily Return Distribution')                  # Main distribution title
ax1.set_title('Heavy Left Tail')                          # Left tail analysis
ax2.set_title('High Peak')                                 # Center peak analysis
ax3.set_title('Heavy Right Tail')                         # Right tail analysis

# Adjust layout and display
plt.tight_layout()                                         # Automatically adjust subplot spacing
plt.show()                                                 # Render the complete figure