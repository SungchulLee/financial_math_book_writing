# Empirical Implied Volatility Smile (SPX Example)


### Introduction


This section illustrates the **implied volatility smile** using real market data for S&P 500 (SPX) index options. The SPX smile is perhaps the most studied volatility surface in quantitative finance, serving as the canonical example of equity index smile behavior.

### Historical Evolution of the SPX Smile


#### 1. Pre-1987: Relatively Flat Smile


Before the October 1987 crash, the SPX implied volatility surface was relatively flat:

- Puts and calls at similar strikes had similar IVs
- The Black-Scholes model was considered adequate
- Market makers did not price significant crash risk

**Typical pre-1987 characteristics:**

- ATM IV: 15-20%
- Skew: Near zero
- Smile curvature: Minimal

#### 2. Post-1987: The Emergence of Skew


Recall (see [§ Skew and Smile](skew_and_smile.md)): the October 1987 crash made permanent the equity smirk — OTM puts became expensive, "crashophobia" was priced in, and the downward-skew/leverage-effect/portfolio-insurance mechanism took hold.

#### 3. Modern Era (2000-Present)


**Current SPX smile characteristics:**

| Feature | Typical Value |
|---------|---------------|
| ATM IV (normal) | 12-18% |
| ATM IV (stressed) | 25-50%+ |
| 25-delta put skew | 4-8 vol points |
| 10-delta put skew | 8-15 vol points |
| OTM call skew | 1-3 vol points |

### Visualizing the SPX Smile


#### 1. Basic Smile Visualization


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


#### 2. Moneyness-Based Visualization


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


#### 3. Multiple Expiries (Term Structure)


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


### Characteristic Features


#### 1. The Volatility Skew


Recall (see [§ Skew and Smile](skew_and_smile.md)): risk-reversal $\text{RR}_{25}=\sigma_{25\Delta C}-\sigma_{25\Delta P}$ and butterfly $\text{BF}_{25}=\tfrac{1}{2}(\sigma_{25\Delta C}+\sigma_{25\Delta P})-\sigma_{\text{ATM}}$ quantify skew and curvature. SPX displays a pronounced **negative skew** $\sigma_{\text{IV}}(K_{\text{OTM put}}) > \sigma_{\text{IV}}(K_{\text{ATM}}) > \sigma_{\text{IV}}(K_{\text{OTM call}})$ with typical values:

| Measure | Typical SPX Value |
|---------|-------------------|
| 25-delta skew $\sigma_{25\Delta P}-\sigma_{\text{ATM}}$ | 4-8% |
| 10-delta skew $\sigma_{10\Delta P}-\sigma_{\text{ATM}}$ | 8-15% |
| Risk reversal $\text{RR}_{25}$ | -5% to -10% |
| Butterfly $\text{BF}_{25}$ | 0.5-2.0 vol pts |

#### 2. Put-Call Parity Check


Implied volatilities from puts and calls at the same strike must agree absent arbitrage, $\sigma_{\text{IV}}^{\text{call}}(K,T)=\sigma_{\text{IV}}^{\text{put}}(K,T)$. Small deviations arise from bid-ask spreads, early-exercise premium (SPY), dividend forecasts, and rate assumptions.

### Comparison Across Markets


#### 1. SPX vs. Individual Stocks


| Feature | SPX | Single Stocks |
|---------|-----|---------------|
| Skew | Steep | Less steep |
| Vol level | Lower | Higher |
| Liquidity | Very high | Variable |
| Jump risk | Priced | More idiosyncratic |

#### 2. SPX vs. Other Indices


| Index | Typical ATM IV | Skew Intensity |
|-------|---------------|----------------|
| SPX | 15-18% | High |
| EURO STOXX 50 | 18-22% | High |
| Nikkei 225 | 18-25% | Moderate |
| VIX | 80-120% | Inverted |

#### 3. SPX vs. VIX Options


**VIX smile characteristics:**

- **Inverted skew:** OTM calls more expensive than OTM puts
- **High ATM vol:** 80-120% typical
- **Mean reversion:** VIX cannot go to zero, bounds the downside

### Seasonality and Patterns


#### 1. Day-of-Week Effects


- **Monday:** Slightly elevated IV (weekend risk)
- **Friday:** Lower IV (approaching weekend decay)

#### 2. Month-End Effects


- **Option expiration week:** Increased volume, potentially volatile
- **Month-end rebalancing:** Institutional flows affect smile

#### 3. Event-Driven Patterns


| Event | Effect on Smile |
|-------|-----------------|
| FOMC meetings | Term structure hump at meeting date |
| Earnings season | Higher single-stock vol, modest SPX impact |
| Elections | Long-dated skew steepens |
| VIX futures expiry | Short-term smile distortions |

### Data Quality Considerations


#### 1. Filtering Criteria


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


#### 2. Liquidity Concentration


SPX option liquidity is concentrated:

- **Strikes:** Multiples of 25 or 50 points
- **Expirations:** Monthly, weekly (Wed, Fri)
- **Moneyness:** Within ±10% of spot

#### 3. Data Sources


| Source | Pros | Cons |
|--------|------|------|
| Yahoo Finance | Free, easy access | Limited history, delayed |
| CBOE | Official, accurate | Paid for historical |
| Bloomberg | Comprehensive | Expensive |
| OptionMetrics | Academic standard | Subscription required |

### Practical Insights for Traders


#### 1. Extracting and Using Implied Volatility


Implied volatility provides a **market consensus forecast** of expected volatility over the remaining life of the option. Practitioners use IV in several ways:

- **Relative value analysis:** Comparing IV to historical realized volatility identifies whether options are "cheap" or "expensive." If $\sigma_{\text{IV}} \gg \hat{\sigma}_{\text{hist}}$, selling volatility may be attractive (and vice versa).
- **Cross-sectional comparison:** Comparing IVs across strikes reveals the market's tail risk pricing. Comparing across maturities reveals expectations about volatility persistence.
- **Regime identification:** Sustained changes in the ATM level or skew slope signal shifts in market risk perception.

#### 2. Trading the Smile


Practitioners exploit the smile structure through targeted strategies:

- **Smile arbitrage:** Trading options across different strikes to exploit perceived mispricing in relative implied volatilities. For example, if the skew appears steeper than model-fair, selling OTM puts and buying ATM options can capture the premium.
- **Risk reversals:** Going long an OTM call and short an OTM put (or vice versa) to express a directional view on the skew. A long risk reversal profits if the skew flattens or the underlying rallies.
- **Butterfly spreads:** Buying a butterfly (long wings, short body) to monetize high smile curvature, or selling a butterfly when curvature appears compressed.

#### 3. Hedging with the Smile


Recall (see [§ Smile Dynamics](../smile_dynamics/dynamic_consistency.md) and [§ IV Sensitivities](../implied_volatility_sensitivities/vega_and_implied_volatility_sensitivity.md)): exotics (barriers, cliquets, autocallables) require smile-adjusted deltas (skew/smile delta) and vanna-volga corrections; naive flat-vol Black-Scholes hedging leaks P&L.

### Interpretation Guidelines


#### 1. What the Smile Tells Us


The SPX smile encodes:

- **Risk-neutral crash probability:** Steeper skew = higher crash expectation
- **Market uncertainty:** Higher ATM = more uncertainty
- **Tail risk pricing:** Wing vols = extreme event premiums

#### 2. Typical Values by Regime


| Regime | ATM IV | 25D Skew | Interpretation |
|--------|--------|----------|----------------|
| Low vol (VIX < 15) | 10-14% | 4-6% | Complacency |
| Normal (VIX 15-20) | 14-18% | 5-8% | Balanced |
| Elevated (VIX 20-30) | 18-25% | 8-12% | Concern |
| Crisis (VIX > 30) | 25-50%+ | 12-25% | Fear |

#### 3. Trading Signals


- **Skew steepening:** Increasing demand for downside protection
- **Skew flattening:** Reduced crash concern
- **ATM spike:** Immediate uncertainty (event, news)
- **Term inversion:** Short-term stress, expected normalization

### Summary


#### Black-Scholes Prediction vs. Market Reality


The SPX smile provides the clearest empirical refutation of the constant-volatility assumption:

| Feature | Black-Scholes Prediction | Market Reality |
|---------|--------------------------|----------------|
| Volatility by strike | Constant across all strikes | U-shaped smile, skewed left |
| Volatility by maturity | Constant across all maturities | Term structure (often upward-sloping) |
| Return distribution | Lognormal, symmetric | Fat tails, negative skew |
| Model fit to market | Single $\sigma$ for all options | Full volatility surface $\sigma_{\text{IV}}(K, T)$ |

This mismatch motivates models that reproduce the observed implied volatility surface; see [§ Dupire local volatility](../../ch13/local_volatility_framework/dupire_formula_and_local_volatility_surface.md) and [§ Stochastic volatility](../../ch14/index.md) (Heston, SABR, jump-diffusion).

#### Key Empirical Facts


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

### Further Reading


- Gatheral, J. *The Volatility Surface*. Comprehensive treatment of empirical smile behavior.
- Cont, R. and Tankov, P. *Financial Modelling with Jump Processes*. Jump risk and smile.
- CBOE. *VIX White Paper*. Official methodology and SPX smile analysis.

---

## Exercises

**Exercise 1.** The SPX implied volatility surface shows 25-delta put skew of 6 vol points and ATM IV of 16%. Compute the implied volatility for a 25-delta put. If the risk reversal $\text{RR}_{25} = -7\%$ and the butterfly $\text{BF}_{25} = 1.5\%$, determine the 25-delta call IV. Verify put-call parity of implied volatility at the same strike.

??? success "Solution to Exercise 1"
    The 25-delta put skew is defined as $\sigma_{25\Delta P} - \sigma_{\text{ATM}}$. Given that the skew is 6 vol points and $\sigma_{\text{ATM}} = 16\%$:

    $$
    \sigma_{25\Delta P} = \sigma_{\text{ATM}} + 6\% = 16\% + 6\% = 22\%
    $$

    Next, we use the risk reversal and butterfly to find the 25-delta call IV. The definitions are:

    $$
    \text{RR}_{25} = \sigma_{25\Delta C} - \sigma_{25\Delta P} = -7\%
    $$

    $$
    \text{BF}_{25} = \frac{1}{2}(\sigma_{25\Delta C} + \sigma_{25\Delta P}) - \sigma_{\text{ATM}} = 1.5\%
    $$

    From the risk reversal:

    $$
    \sigma_{25\Delta C} = \sigma_{25\Delta P} + \text{RR}_{25} = 22\% + (-7\%) = 15\%
    $$

    **Verification using the butterfly:** We check consistency:

    $$
    \text{BF}_{25} = \frac{1}{2}(15\% + 22\%) - 16\% = \frac{1}{2}(37\%) - 16\% = 18.5\% - 16\% = 2.5\%
    $$

    However, the stated butterfly is $1.5\%$, not $2.5\%$. This discrepancy means we should solve the system of equations simultaneously. Let $\sigma_C = \sigma_{25\Delta C}$ and $\sigma_P = \sigma_{25\Delta P}$. From the butterfly:

    $$
    \frac{1}{2}(\sigma_C + \sigma_P) = \sigma_{\text{ATM}} + \text{BF}_{25} = 16\% + 1.5\% = 17.5\%
    $$

    So $\sigma_C + \sigma_P = 35\%$. From the risk reversal: $\sigma_C - \sigma_P = -7\%$. Solving:

    $$
    \sigma_C = \frac{35\% + (-7\%)}{2} = 14\%, \quad \sigma_P = \frac{35\% - (-7\%)}{2} = 21\%
    $$

    The 25-delta call IV is $14\%$ and the 25-delta put IV is $21\%$.

    **Put-call parity of implied volatility:** By put-call parity, a European call and put at the same strike $K$ and maturity $T$ must have the same implied volatility: $\sigma_{\text{IV}}^{\text{call}}(K, T) = \sigma_{\text{IV}}^{\text{put}}(K, T)$. This holds because put-call parity $C - P = S e^{-qT} - K e^{-rT}$ is model-independent, so any implied volatility that prices the call correctly must also price the put correctly at that same strike. The different IVs for 25-delta puts and calls arise because 25-delta puts and 25-delta calls correspond to different strikes, not the same strike.

---

**Exercise 2.** Explain the economic mechanisms behind the emergence of the SPX skew after the October 1987 crash. Why was the smile approximately flat before 1987, and what role did portfolio insurance play in the crash dynamics? Is the persistence of skew since 1987 evidence of rational pricing or behavioral bias?

??? success "Solution to Exercise 2"
    **Pre-1987 (flat smile):** Before October 1987, the SPX smile was approximately flat because the market did not price significant crash risk. Portfolio insurance was a relatively new strategy, and market participants generally trusted the Black-Scholes framework with its constant-volatility assumption. OTM puts were not in high demand, so their prices (and implied volatilities) were close to ATM levels.

    **The 1987 crash and portfolio insurance:** On Black Monday (October 19, 1987), the S&P 500 fell approximately 20% in a single day. Portfolio insurance strategies, which involved dynamically selling index futures as the market declined, created a destructive feedback loop: as the market fell, portfolio insurers sold more futures, pushing prices further down, triggering more selling. This demonstrated that (a) extreme left-tail events are possible and (b) dynamic hedging strategies can amplify crashes rather than protect against them.

    **Emergence of skew:** After 1987, institutional investors recognized the need for static downside protection (OTM puts) rather than dynamic replication. The surge in demand for OTM puts permanently raised their prices relative to ATM and OTM calls, creating the negative skew. Market makers, aware of the tail risk, also began charging higher implied volatilities for OTM puts to compensate for the risk of large discontinuous moves.

    **Persistence since 1987 -- rational or behavioral?** The persistence of skew reflects elements of both rational pricing and behavioral bias:

    - **Rational:** The risk-neutral distribution should have fatter left tails than the lognormal because empirical equity returns exhibit negative skewness and excess kurtosis. The skew prices genuine crash risk and the volatility risk premium (investors demand compensation for bearing left-tail exposure).
    - **Behavioral:** "Crashophobia" may overweight the probability of extreme events beyond what historical data supports. Institutional mandates to buy put protection (regardless of price) create persistent demand pressure. Regulatory requirements (e.g., portfolio risk limits) further amplify demand for OTM puts.

    The fact that the skew has not diminished over nearly four decades suggests it reflects a structural feature of equity markets rather than a temporary anomaly.

---

**Exercise 3.** Using the filtering criteria (minimum volume 50, minimum open interest 100, maximum bid-ask spread 10% of mid), explain why each filter is necessary for reliable smile analysis. For each filter, describe a specific scenario where omitting it would produce a misleading implied volatility estimate.

??? success "Solution to Exercise 3"
    **Minimum volume filter (50):** Options with very low volume may have stale quotes that do not reflect current market conditions. If an option traded only once early in the day at a price reflecting morning volatility, that quote becomes misleading as the market moves. **Example:** An OTM put with volume of 2 might show an implied volatility of 35% based on a single trade from hours ago, while the current fair IV is 25%. Including this point would create a spurious spike in the smile.

    **Minimum open interest filter (100):** Low open interest indicates that few contracts are outstanding, so market makers may not maintain tight quotes. The bid-ask spread may be unreliable, and the mid-price may not represent executable levels. **Example:** A deep OTM call with open interest of 5 might have a bid of \$0.05 and an ask of \$0.50. The mid-price of \$0.275 implies a volatility that is essentially meaningless because neither side of the market is actively quoting. This would distort the right wing of the smile.

    **Maximum bid-ask spread filter (10% of mid):** Wide spreads indicate illiquidity, and the mid-price is an unreliable estimate of fair value. The true implied volatility lies somewhere within a wide range, so using the midpoint introduces noise. **Example:** An option with bid = \$1.00 and ask = \$1.80 has a spread of 44% of mid (\$1.40). The implied volatility from the bid might be 18% while from the ask it might be 24%. Using the mid gives 21%, but the uncertainty is so large that this point adds noise rather than information to the smile. In contrast, a liquid ATM option with bid = \$5.00 and ask = \$5.10 (spread = 2% of mid) gives a reliable IV estimate.

---

**Exercise 4.** The table of typical SPX values by regime classifies VIX < 15 as "complacency" with ATM IV of 10-14% and 25-delta skew of 4-6%. During a transition from normal (VIX = 18) to elevated (VIX = 25), estimate the change in (a) ATM IV, (b) 25-delta put IV, and (c) 10-delta put IV using the ranges given. Which part of the smile moves proportionally more?

??? success "Solution to Exercise 4"
    The transition is from normal (VIX = 18, ATM IV 14-18%, 25D skew 5-8%) to elevated (VIX = 25, ATM IV 18-25%, 25D skew 8-12%).

    **(a) Change in ATM IV:** ATM IV moves from the normal range to the elevated range. Taking representative midpoints: from approximately 16% to approximately 21.5%.

    $$
    \Delta \sigma_{\text{ATM}} \approx 21.5\% - 16\% = +5.5 \text{ vol points}
    $$

    **(b) Change in 25-delta put IV:** The 25-delta put IV equals ATM IV plus the 25-delta skew. In the normal regime: $\sigma_{25\Delta P} \approx 16\% + 6.5\% = 22.5\%$. In the elevated regime: $\sigma_{25\Delta P} \approx 21.5\% + 10\% = 31.5\%$.

    $$
    \Delta \sigma_{25\Delta P} \approx 31.5\% - 22.5\% = +9.0 \text{ vol points}
    $$

    **(c) Change in 10-delta put IV:** Using the 10-delta skew ranges (normal: 6-10%, elevated: not explicitly given, but typically 12-20% based on the relationship between 10-delta and 25-delta skew). The 10-delta skew approximately doubles the 25-delta skew. In the normal regime: $\sigma_{10\Delta P} \approx 16\% + 8\% = 24\%$. In the elevated regime: $\sigma_{10\Delta P} \approx 21.5\% + 16\% = 37.5\%$.

    $$
    \Delta \sigma_{10\Delta P} \approx 37.5\% - 24\% = +13.5 \text{ vol points}
    $$

    **Which part moves proportionally more?** The further OTM puts move proportionally more than ATM. Expressing changes as fractions of the initial level:

    - ATM: $5.5 / 16 \approx 34\%$ relative increase
    - 25-delta put: $9.0 / 22.5 \approx 40\%$ relative increase
    - 10-delta put: $13.5 / 24 \approx 56\%$ relative increase

    The deep OTM puts (10-delta) move proportionally the most. This is because during stress, both the level and the skew steepen simultaneously. The skew component is additive to the ATM level increase, so strikes further from ATM experience a compounding effect: the ATM level rises and the skew widens, both pushing OTM put IV higher.

---

**Exercise 5.** Compare the SPX smile to the VIX smile. The VIX has inverted skew (OTM calls more expensive than OTM puts) and ATM IV of 80-120%. Explain why the VIX smile is inverted while the SPX smile has normal (downward) skew. What property of the VIX as a mean-reverting quantity causes this behavior?

??? success "Solution to Exercise 5"
    **SPX smile (normal/downward skew):** The SPX represents a portfolio of stocks. A market decline increases the leverage ratio of constituent firms (debt-to-equity rises), mechanically increasing equity volatility. Additionally, market declines tend to be sudden and correlated (panic selling, margin calls), while rallies are typically gradual. This creates a strong negative correlation $\rho(dS, d\sigma) < 0$ between returns and volatility. Institutional demand for portfolio insurance (OTM puts) further elevates downside IV. The result is $\sigma_{\text{IV}}(K_{\text{low}}) > \sigma_{\text{IV}}(K_{\text{ATM}}) > \sigma_{\text{IV}}(K_{\text{high}})$.

    **VIX smile (inverted/upward skew):** The VIX measures 30-day expected volatility of the SPX. Its smile is inverted because:

    1. **Positive skew in VIX returns:** The VIX tends to spike upward sharply (e.g., from 15 to 40 during a crisis) but declines gradually. This means OTM calls on the VIX (high VIX strikes) are more valuable than OTM puts (low VIX strikes), reversing the equity pattern.

    2. **Hedging demand for VIX calls:** Investors buy OTM VIX calls as portfolio hedges (since VIX spikes when the market crashes), driving up their prices and implied volatilities.

    3. **VIX mean reversion:** The VIX is strongly mean-reverting with a lower bound near zero. This asymmetry is crucial:
        - The VIX cannot go below zero, so downside moves are bounded, making OTM puts (low strikes) relatively cheap.
        - The VIX has no upper bound and can spike to 80+ during extreme events, making OTM calls (high strikes) expensive.
        - Mean reversion from elevated levels makes very high VIX levels transient, but the instantaneous spike risk is priced into OTM calls.

    The mean-reverting nature creates a right-skewed distribution for VIX levels, which is the mirror image of the left-skewed distribution for equity returns. Since VIX and SPX are negatively correlated ($\rho \approx -0.8$), their smile structures are naturally inverted relative to each other.

---

**Exercise 6.** A trader observes that the SPX 1-month 90% moneyness put has IV of 28% while the ATM IV is 16%. (a) Compute the skew in vol points. (b) If the Black-Scholes model were correct, what would the 90% moneyness IV be? (c) Estimate the risk-neutral probability of a 10% decline over the next month using the normal distribution with the market-implied IV versus the Black-Scholes flat IV. Discuss the difference.

??? success "Solution to Exercise 6"
    The 90% moneyness put has IV of 28% and ATM IV is 16%.

    **(a) Skew in vol points:**

    $$
    \text{Skew} = \sigma_{\text{IV}}(90\%) - \sigma_{\text{ATM}} = 28\% - 16\% = 12 \text{ vol points}
    $$

    **(b) Under Black-Scholes:** If the Black-Scholes model were correct, implied volatility would be constant across all strikes. Therefore the 90% moneyness IV would equal the ATM IV:

    $$
    \sigma_{\text{IV}}^{\text{BS}}(90\%) = \sigma_{\text{ATM}} = 16\%
    $$

    **(c) Risk-neutral probability of a 10% decline:** A 10% decline means $S_T / S_0 \leq 0.90$, or equivalently $\ln(S_T / S_0) \leq \ln(0.90) = -0.10536$.

    Under the risk-neutral measure with volatility $\sigma$ and maturity $T = 1/12$ (one month):

    $$
    \ln(S_T / S_0) \sim \mathcal{N}\!\left(-\frac{\sigma^2 T}{2},\; \sigma^2 T\right)
    $$

    (ignoring the drift term $rT$ for simplicity, or assuming $r \approx 0$).

    **Using market-implied IV ($\sigma = 28\%$):** For the 90% moneyness put, the relevant volatility is 28%:

    $$
    z = \frac{-0.10536 - (-0.28^2 / 24)}{0.28 \sqrt{1/12}} = \frac{-0.10536 + 0.00327}{0.08083} = \frac{-0.10209}{0.08083} = -1.263
    $$

    $$
    \mathbb{P}^{\mathbb{Q}}(S_T \leq 0.90 S_0) = \Phi(-1.263) \approx 10.3\%
    $$

    **Using Black-Scholes flat IV ($\sigma = 16\%$):**

    $$
    z = \frac{-0.10536 - (-0.16^2 / 24)}{0.16 \sqrt{1/12}} = \frac{-0.10536 + 0.00107}{0.04619} = \frac{-0.10429}{0.04619} = -2.258
    $$

    $$
    \mathbb{P}^{\mathbb{Q}}(S_T \leq 0.90 S_0) = \Phi(-2.258) \approx 1.2\%
    $$

    **Discussion:** The market-implied probability of a 10% monthly decline is approximately 10.3%, nearly nine times larger than the Black-Scholes estimate of 1.2%. This dramatic difference reflects the market's pricing of crash risk: the elevated IV for OTM puts assigns much higher probability to large downward moves than a lognormal model with flat volatility would predict. The difference is the quantitative expression of "crashophobia" and the failure of the constant-volatility assumption for tail events.

---

**Exercise 7.** Describe three strategies for trading the SPX smile: smile arbitrage, risk reversals, and butterfly spreads. For each, (a) specify the option positions involved, (b) identify the smile feature being exploited (skew, curvature, or level), and (c) explain the main risk if the trade goes wrong.

??? success "Solution to Exercise 7"
    **1. Smile arbitrage:**

    **(a) Positions:** Sell OTM puts (which have elevated IV due to steep skew) and buy ATM options (straddles or strangles) to hedge the overall vega exposure. Alternatively, sell OTM puts at one strike and buy OTM puts at an adjacent strike where the skew appears too steep, creating a put spread that is short the overpriced skew.

    **(b) Feature exploited:** **Skew.** The trade profits if the implied volatility skew is steeper than the actual realized skew dynamics. In other words, the trader believes OTM puts are overpriced relative to ATM options based on a model of how volatility changes with spot level.

    **(c) Main risk:** A sudden market crash causes realized skew to exceed the implied skew. The short OTM puts suffer large losses as both their intrinsic value increases and their IV spikes. The hedge (long ATM options) may not offset the losses because delta and vega exposures change rapidly during a crash. This is essentially short left-tail risk.

    **2. Risk reversals:**

    **(a) Positions:** A long risk reversal consists of buying an OTM call (e.g., 25-delta) and selling an OTM put (e.g., 25-delta) at the same maturity. A short risk reversal is the opposite: sell OTM call, buy OTM put.

    **(b) Feature exploited:** **Skew (level and direction).** A short risk reversal (sell call, buy put) profits if the skew steepens (put IV rises relative to call IV). A long risk reversal profits if the skew flattens or the underlying rallies. The position is directly linked to the risk reversal quotation $\text{RR}_{25} = \sigma_{25\Delta C} - \sigma_{25\Delta P}$.

    **(c) Main risk:** For a long risk reversal (long call, short put): a sharp market decline causes the short put to move deep ITM while the long call expires worthless. The trade has significant directional (delta) exposure, not just volatility exposure. For a short risk reversal: a strong rally causes similar losses in the opposite direction.

    **3. Butterfly spreads:**

    **(a) Positions:** Buy a butterfly: long 1 OTM put (e.g., 90% strike), short 2 ATM options (100% strike), long 1 OTM call (e.g., 110% strike). This is equivalent to being long the wings and short the body.

    **(b) Feature exploited:** **Curvature (convexity/smile).** The butterfly profits when the smile curvature is high relative to what is realized. The butterfly quotation $\text{BF}_{25} = \frac{1}{2}(\sigma_{25\Delta C} + \sigma_{25\Delta P}) - \sigma_{\text{ATM}}$ measures exactly this curvature premium.

    **(c) Main risk:** If the smile flattens (curvature decreases), the wings lose value relative to ATM. A long butterfly is also short gamma near the ATM strike, so large realized moves around the central strike generate losses. The trade has limited payoff (tent-shaped) but can suffer if the underlying moves sharply and stays away from the central strike, especially if wing IVs decline simultaneously.
