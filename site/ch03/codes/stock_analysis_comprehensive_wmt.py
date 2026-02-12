# ============================================================================
# stock_analysis_COMPREHENSIVE_STOCK_ANALYSIS_WMT.py
# ============================================================================
import matplotlib.pyplot as plt
import stock_analysis as sto

# Stock analysis configuration
ticker = "WMT"                       # Walmart stock ticker symbol
start = "2024-07-01"                 # Starting date for historical data retrieval

# Initialize stock object and perform comprehensive analysis
stock = sto.USStock(ticker)                          # Create USStock instance for Walmart
stock.get_data(start_date=start)                 # Download historical data (new method, no warning)
stock.compute_returns()                          # Calculate simple and log returns
stock.compute_mu_and_sigma()                     # Compute mean (mu) and standard deviation (sigma)

# Extract statistics from the nested statistics dictionary
stats = stock.statistics
arithmetic_stats = stats['arithmetic']          # Statistics for simple returns
logarithmic_stats = stats['logarithmic']        # Statistics for log returns

# Display key statistics
print(f"mu = {arithmetic_stats['mu']:.4f}, sigma = {arithmetic_stats['sigma']:.4f}")
print(f"mu_log = {logarithmic_stats['mu']:.4f}, sigma_log = {logarithmic_stats['sigma']:.4f}")

# Create figure and axes with custom layout
fig, (ax_price, ax_return) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, 
                                          gridspec_kw={'height_ratios': [2, 1]})

# Plot closing price on the primary y-axis
ax_price.plot(stock.df.index.to_numpy(), stock.df.Close.to_numpy(), label="Close", color='blue')

# Add 1-month and 3-month moving averages
stock.df['1M_MA'] = stock.df.Close.rolling(21).mean()      # 21 trading days ≈ 1 month
ax_price.plot(stock.df.index.to_numpy(), stock.df["1M_MA"].to_numpy(), label="1M MA", color='red', ls="--")

stock.df['3M_MA'] = stock.df.Close.rolling(21*3).mean()    # 63 trading days ≈ 3 months
ax_price.plot(stock.df.index.to_numpy(), stock.df["3M_MA"].to_numpy(), label="3M MA", color='green', ls="--")

# Add high-low band to show daily price range
ax_price.fill_between(stock.df.index.to_numpy(), stock.df.High.to_numpy(), stock.df.Low.to_numpy(), 
                     color='blue', alpha=0.2, label="High-Low Band")

# Add volume to the same axis with a secondary y-axis
ax_vol = ax_price.twinx()
ax_vol.bar(stock.df.index.to_numpy(), stock.df.Volume.to_numpy(), color='gray', alpha=0.5, width=0.8, label="Volume")
ax_vol.set_ylim(0, stock.df['Volume'].max() * 5)          # Scale volume to not overwhelm price

# Plot daily returns with enhanced visualization
returns = stock.df['Return'].values                        # Convert to numpy array for matplotlib compatibility
log_returns = stock.df['Return_Log'].values               # Convert to numpy array for matplotlib compatibility

ax_return.plot(stock.df.index.to_numpy(), returns, label='Return', color='orange', lw=5, alpha=0.7)
ax_return.axhline(0, color='black', linestyle='--', linewidth=0.8)  # Zero reference line

# Add rolling volatility band (1-month rolling standard deviation)
stock.df['1M_Vol'] = stock.df['Return'].rolling(21).std()
ax_return.fill_between(stock.df.index.to_numpy(), stock.df['1M_Vol'].to_numpy(), -stock.df['1M_Vol'].to_numpy(), 
                      color='blue', alpha=0.2, label="±1σ Volatility Band")

# Add comprehensive return statistics text box
text_return = (
    f"Return Mean     : {arithmetic_stats['mu']:.4f}\n"
    f"Log Return Mean : {logarithmic_stats['mu']:.4f}\n\n"
    f"Return Std      : {arithmetic_stats['sigma']:.4f}\n"
    f"Log Return Std  : {logarithmic_stats['sigma']:.4f}"
)
ax_return.text(
    0.01, 0.98, text_return,                              # Position in axes coordinates
    transform=ax_return.transAxes,
    fontsize=10,
    verticalalignment='top',
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
)

# Plot log returns for comparison
ax_return.plot(stock.df.index.to_numpy(), log_returns, label='Log Return', color='purple', lw=2)

# Customize axes labels and legends
ax_price.set_ylabel("Price ($)")                          # Price axis label
ax_vol.set_ylabel("Volume")                               # Volume axis label
ax_return.set_ylabel("Daily Returns")                     # Return axis label

# Add legends to appropriate locations
ax_price.legend(loc='upper left')                         # Price and MA legends
ax_vol.legend(loc='upper right')                          # Volume legend
ax_return.legend(loc='upper right')                       # Returns legend

# Remove top spines for cleaner appearance
for ax in [ax_price, ax_vol, ax_return]:
    ax.spines["top"].set_visible(False)

# Set comprehensive title and display
plt.suptitle(f"{ticker} Comprehensive Stock Analysis - Price, Volume & Returns", fontsize=16)
plt.tight_layout()                                        # Automatically adjust subplot spacing
plt.show()                                                # Render the complete analysis