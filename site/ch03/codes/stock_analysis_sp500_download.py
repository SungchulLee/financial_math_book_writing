# ============================================================================
# stock_analysis_SP500_DOWNLOAD.py
# ============================================================================
import matplotlib.pyplot as plt
import stock_analysis as sto

year = "2024"
stocks_data, sp500_data = sto.download_sp500(year=year)

fig, ax = plt.subplots(figsize=(12, 5))

tickers = ['AAPL', 'NVDA', 'TSLA', 'SP500']
for ticker in tickers:
    if ticker != "SP500":    
        series = stocks_data[ticker]["Close"]
    else:
        series = sp500_data["Close"]
    idx =series.index.to_numpy()
    prices = series.to_numpy()
    ax.plot(idx, prices/prices[0]*100, label=ticker)

ax.set_title(f'Normalized Close Prices (Base 100) in {year}')
ax.set_xlabel('Date')
ax.set_ylabel('Price (Normalized to 100)')
ax.legend()
ax.grid(True)
fig.tight_layout()
plt.show()
    