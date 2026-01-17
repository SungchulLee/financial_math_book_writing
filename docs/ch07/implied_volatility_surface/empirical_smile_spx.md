# Empirical Implied Volatility Smile (SPX Example)


## Introduction


This section illustrates the **implied volatility smile** using real market data for S&P 500 (SPX) index options. The SPX smile is perhaps the most studied volatility surface in quantitative finance, serving as the canonical example of equity index smile behavior.

## Historical Evolution of the SPX Smile


### 1. Pre-1987: Relatively Flat Smile


Before the October 1987 crash, the SPX implied volatility surface was relatively flat:
- Puts and calls at similar strikes had similar IVs
- The Black-Scholes model was considered adequate
- Market makers did not price significant crash risk

**Typical pre-1987 characteristics:**
- ATM IV: 15-20%
- Skew: Near zero
- Smile curvature: Minimal

### 2. Post-1987: The Emergence of Skew


The October 1987 crash (Black Monday) fundamentally changed the SPX smile:

**Key changes:**
- Pronounced downside skew emerged
- OTM puts became significantly more expensive
- The "smirk" pattern became permanent

**Mechanism:**
- Portfolio insurance strategies contributed to crash severity
- Investors now demand protection against tail events
- "Crashophobia" priced into OTM puts

### 3. Modern Era (2000-Present)


**Current SPX smile characteristics:**

| Feature | Typical Value |
|---------|---------------|
| ATM IV (normal) | 12-18% |
| ATM IV (stressed) | 25-50%+ |
| 25-delta put skew | 4-8 vol points |
| 10-delta put skew | 8-15 vol points |
| OTM call skew | 1-3 vol points |

## Visualizing the SPX Smile


### 1. Basic Smile Visualization


```python
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Fetch SPX option data
spx = yf.Ticker("^SPX")
expiry = spx.options[1]  # Second available expiry

opt_chain = spx.option_chain(expiry)
calls = opt_chain.calls
puts = opt_chain.puts

# Filter by volume for liquid options
min_volume = 50
calls_filtered = calls[(calls['volume'] >= min_volume) & (calls['impliedVolatility'].notna())]
puts_filtered = puts[(puts['volume'] >= min_volume) & (puts['impliedVolatility'].notna())]

# Get current spot price
spot = spx.history(period="1d")['Close'].iloc[-1]

plt.figure(figsize=(12, 7))
plt.plot(calls_filtered['strike'], calls_filtered['impliedVolatility'] * 100, 
         'b-o', label='Call IV', markersize=4)
plt.plot(puts_filtered['strike'], puts_filtered['impliedVolatility'] * 100, 
         'r-o', label='Put IV', markersize=4)
plt.axvline(x=spot, color='green', linestyle='--', label=f'Spot = {spot:.0f}')
plt.title(f"SPX Implied Volatility Smile (Expiration: {expiry})")
plt.xlabel("Strike")
plt.ylabel("Implied Volatility (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```


### 2. Moneyness-Based Visualization


```python
import pandas as pd

def compute_moneyness(strike, spot, T, r=0.05):
    """Compute log-moneyness k = ln(K/F)"""
    F = spot * np.exp(r * T)
    return np.log(strike / F)

# Assume T from expiry
from datetime import datetime
T = (datetime.strptime(expiry, '%Y-%m-%d') - datetime.now()).days / 365

# Add moneyness column
calls_filtered = calls_filtered.copy()
calls_filtered['moneyness'] = compute_moneyness(calls_filtered['strike'], spot, T)

puts_filtered = puts_filtered.copy()
puts_filtered['moneyness'] = compute_moneyness(puts_filtered['strike'], spot, T)

plt.figure(figsize=(12, 7))
plt.scatter(calls_filtered['moneyness'], calls_filtered['impliedVolatility'] * 100, 
            c='blue', label='Calls', alpha=0.7)
plt.scatter(puts_filtered['moneyness'], puts_filtered['impliedVolatility'] * 100, 
            c='red', label='Puts', alpha=0.7)
plt.axvline(x=0, color='green', linestyle='--', label='ATM')
plt.title(f"SPX IV vs Log-Moneyness (Expiration: {expiry})")
plt.xlabel("Log-Moneyness k = ln(K/F)")
plt.ylabel("Implied Volatility (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```


### 3. Multiple Expiries (Term Structure)


```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for i, exp_idx in enumerate([0, 2, 5, 10]):
    if exp_idx < len(spx.options):
        expiry = spx.options[exp_idx]
        opt_chain = spx.option_chain(expiry)
        
        calls_f = opt_chain.calls[(opt_chain.calls['volume'] >= 20)]
        puts_f = opt_chain.puts[(opt_chain.puts['volume'] >= 20)]
        
        ax = axes[i // 2, i % 2]
        ax.plot(calls_f['strike'], calls_f['impliedVolatility'] * 100, 'b-', label='Calls')
        ax.plot(puts_f['strike'], puts_f['impliedVolatility'] * 100, 'r-', label='Puts')
        ax.axvline(x=spot, color='green', linestyle='--', alpha=0.5)
        ax.set_title(f"Expiry: {expiry}")
        ax.set_xlabel("Strike")
        ax.set_ylabel("IV (%)")
        ax.legend()
        ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```


## Characteristic Features


### 1. The Volatility Skew


The SPX exhibits a pronounced **negative skew**:

$$
\sigma_{\text{IV}}(K_{\text{OTM put}}) > \sigma_{\text{IV}}(K_{\text{ATM}}) > \sigma_{\text{IV}}(K_{\text{OTM call}})
$$


**Quantitative measures:**

| Measure | Definition | Typical SPX Value |
|---------|-----------|-------------------|
| 25-delta skew | $\sigma_{25\Delta P} - \sigma_{\text{ATM}}$ | 4-8% |
| 10-delta skew | $\sigma_{10\Delta P} - \sigma_{\text{ATM}}$ | 8-15% |
| Risk reversal | $\sigma_{25\Delta C} - \sigma_{25\Delta P}$ | -5% to -10% |

### 2. Put-Call Parity Check


Implied volatilities from puts and calls at the same strike should be equal (absent arbitrage):

$$
\sigma_{\text{IV}}^{\text{call}}(K, T) = \sigma_{\text{IV}}^{\text{put}}(K, T)
$$


Small deviations occur due to:
- Bid-ask spreads
- American exercise premium (for SPY options)
- Dividend expectations
- Interest rate assumptions

### 3. Smile Curvature (Butterfly)


The **butterfly spread** measures smile curvature:

$$
\text{Butterfly} = \frac{1}{2}(\sigma_{25\Delta C} + \sigma_{25\Delta P}) - \sigma_{\text{ATM}}
$$


Typical SPX values: 0.5-2.0 vol points

**Interpretation:** Positive butterfly indicates:
- Fat tails in risk-neutral distribution
- Market prices both up and down jump risk

## Comparison Across Markets


### 1. SPX vs. Individual Stocks


| Feature | SPX | Single Stocks |
|---------|-----|---------------|
| Skew | Steep | Less steep |
| Vol level | Lower | Higher |
| Liquidity | Very high | Variable |
| Jump risk | Priced | More idiosyncratic |

### 2. SPX vs. Other Indices


| Index | Typical ATM IV | Skew Intensity |
|-------|---------------|----------------|
| SPX | 15-18% | High |
| EURO STOXX 50 | 18-22% | High |
| Nikkei 225 | 18-25% | Moderate |
| VIX | 80-120% | Inverted |

### 3. SPX vs. VIX Options


**VIX smile characteristics:**
- **Inverted skew:** OTM calls more expensive than OTM puts
- **High ATM vol:** 80-120% typical
- **Mean reversion:** VIX cannot go to zero, bounds the downside

## Seasonality and Patterns


### 1. Day-of-Week Effects


- **Monday:** Slightly elevated IV (weekend risk)
- **Friday:** Lower IV (approaching weekend decay)

### 2. Month-End Effects


- **Option expiration week:** Increased volume, potentially volatile
- **Month-end rebalancing:** Institutional flows affect smile

### 3. Event-Driven Patterns


| Event | Effect on Smile |
|-------|-----------------|
| FOMC meetings | Term structure hump at meeting date |
| Earnings season | Higher single-stock vol, modest SPX impact |
| Elections | Long-dated skew steepens |
| VIX futures expiry | Short-term smile distortions |

## Data Quality Considerations


### 1. Filtering Criteria


For reliable smile analysis, filter options by:

```python
# Recommended filters
min_volume = 50        # Minimum daily volume
min_open_interest = 100 # Minimum open interest
max_spread_pct = 0.10   # Maximum bid-ask spread as % of mid

filtered = options[
    (options['volume'] >= min_volume) &
    (options['openInterest'] >= min_open_interest) &
    ((options['ask'] - options['bid']) / ((options['ask'] + options['bid'])/2) <= max_spread_pct)
]
```


### 2. Liquidity Concentration


SPX option liquidity is concentrated:
- **Strikes:** Multiples of 25 or 50 points
- **Expirations:** Monthly, weekly (Wed, Fri)
- **Moneyness:** Within ±10% of spot

### 3. Data Sources


| Source | Pros | Cons |
|--------|------|------|
| Yahoo Finance | Free, easy access | Limited history, delayed |
| CBOE | Official, accurate | Paid for historical |
| Bloomberg | Comprehensive | Expensive |
| OptionMetrics | Academic standard | Subscription required |

## Interpretation Guidelines


### 1. What the Smile Tells Us


The SPX smile encodes:
- **Risk-neutral crash probability:** Steeper skew = higher crash expectation
- **Market uncertainty:** Higher ATM = more uncertainty
- **Tail risk pricing:** Wing vols = extreme event premiums

### 2. Typical Values by Regime


| Regime | ATM IV | 25D Skew | Interpretation |
|--------|--------|----------|----------------|
| Low vol (VIX < 15) | 10-14% | 4-6% | Complacency |
| Normal (VIX 15-20) | 14-18% | 5-8% | Balanced |
| Elevated (VIX 20-30) | 18-25% | 8-12% | Concern |
| Crisis (VIX > 30) | 25-50%+ | 12-25% | Fear |

### 3. Trading Signals


- **Skew steepening:** Increasing demand for downside protection
- **Skew flattening:** Reduced crash concern
- **ATM spike:** Immediate uncertainty (event, news)
- **Term inversion:** Short-term stress, expected normalization

## Summary


The SPX implied volatility smile exhibits:

1. **Pronounced negative skew** (crashophobia)
2. **Historical evolution** (flat pre-1987, skewed post-1987)
3. **Regime dependence** (steeper in stress)
4. **Term structure** (short-term skew steeper)
5. **Liquidity concentration** (around ATM, standard strikes)

Understanding these patterns is essential for:
- Option pricing and trading
- Risk management
- Model calibration
- Market sentiment analysis

---

## Further Reading


- Gatheral, J. *The Volatility Surface*. Comprehensive treatment of empirical smile behavior.
- Cont, R. and Tankov, P. *Financial Modelling with Jump Processes*. Jump risk and smile.
- CBOE. *VIX White Paper*. Official methodology and SPX smile analysis.
