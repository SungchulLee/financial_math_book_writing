# ============================================================================
# stock_analysis_CORRELATION_HEAT_MAP_FAANG.py
# ============================================================================
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import stock_analysis as sto

# Define tickers and date
tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
start_date = '2024-01-01'

# Store Stock instances and normalized price series
stocks = {}
normalized_prices = {}

# Load data and normalize close prices to start at 100
for ticker in tickers:
    # Use USStock with the new get_data() method (no deprecation warning)
    stock = sto.USStock(ticker)
    stock.get_data(start_date)  # Recommended method
    stocks[ticker] = stock

    # Extract close prices and normalize to start at 100
    close = stock.df['Close']
    normalized = close / close.iloc[0] * 100
    normalized_prices[ticker] = normalized

# Create DataFrame from normalized prices and drop any columns with NaN
price_df = pd.DataFrame(normalized_prices).dropna(axis=1)

# Calculate correlation matrix
corr_matrix = price_df.corr()

# Create correlation heatmap
fig, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(corr_matrix, cmap='coolwarm', ax=ax, annot=True, fmt='.2%')
ax.set_title('Correlation Matrix of Normalized Prices')
plt.show()  