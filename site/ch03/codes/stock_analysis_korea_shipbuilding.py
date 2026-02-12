# ============================================================================
# stock_analysis_NORMALIZED_ADJUST_CLOSE_SHIP_BUILDING_COMPANIES_IN_KOREA.py
# ============================================================================
import matplotlib.pyplot as plt
import yfinance as yf

tickers_str = ['HD Hyundai Heavy Industries', 'Samsung Heavy Industries', 'Hanwha Ocean']
tickers = ['329180.KS', '010140.KS', '042660.KS']
start_date = '2024-01-01'
end_date = "2025-12-31"

normalized_prices = {}

for ticker in tickers:
    df = yf.Ticker(ticker).history(start=start_date, end=end_date)
    normalized_prices[ticker] = df['Close'] / df['Close'].iloc[0] * 100

fig, ax = plt.subplots(figsize=(12, 5))

# Fix: Convert to numpy arrays to avoid pandas/matplotlib compatibility issues
for (ticker, series), ticker_str in zip(normalized_prices.items(), tickers_str):
    # Convert both index and values to numpy arrays
    x_values = series.index.to_numpy() if hasattr(series.index, 'to_numpy') else series.index.values
    y_values = series.to_numpy() if hasattr(series, 'to_numpy') else series.values
    ax.plot(x_values, y_values, label=ticker_str)

ax.set_title(f'Normalized Close Prices (Base 100) since {start_date}')
ax.set_xlabel('Date')
ax.set_ylabel('Price (Normalized to 100)')
ax.legend()
ax.grid(True)
fig.tight_layout()
plt.show()