# Empirical Implied Volatility Smile (SPX Example)


This section illustrates the **implied volatility smile** using real market data for S&P 500 (SPX) index options.

```python
import yfinance as yf
import matplotlib.pyplot as plt

spx = yf.Ticker("^SPX")
expiry = spx.options[1]

opt_chain = spx.option_chain(expiry)
calls = opt_chain.calls
puts = opt_chain.puts

min_volume = 50
calls_filtered = calls[(calls['volume'] >= min_volume) & (calls['impliedVolatility'].notna())]
puts_filtered = puts[(puts['volume'] >= min_volume) & (puts['impliedVolatility'].notna())]

plt.figure(figsize=(10, 6))
plt.plot(calls_filtered['strike'], calls_filtered['impliedVolatility'], label='Call IV')
plt.plot(puts_filtered['strike'], puts_filtered['impliedVolatility'], label='Put IV')
plt.title(f"SPX Implied Volatility Smile (Expiration: {expiry})")
plt.xlabel("Strike")
plt.ylabel("Implied Volatility")
plt.legend()
plt.grid(True)
plt.show()
```

The plot exhibits the characteristic **equity volatility skew**, with higher implied volatilities for OTM puts.
