# Skew Trading Spreads  
## Exploiting Put / Call Implied Volatility Differences

**Skew trading spreads** focus on exploiting relative mispricing between **put and call implied volatilities across strikes**, rather than trading the absolute level of volatility or the direction of the underlying.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_mean_reversion.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_opportunity.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_premium.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_returns.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- Implied volatility is **not symmetric across strikes**
- Downside puts usually trade at **higher IV** than upside calls
- This asymmetry is called **volatility skew**
- Skew is structural, but **not constant**
- When skew becomes too steep or too flat, **relative-value trades emerge**

> **Skew trading is not about volatility level — it is about volatility *asymmetry*.**

---

## What Is Volatility Skew?

### Definition

**Volatility skew** refers to the systematic difference between implied volatilities of options at different strikes for the same maturity.

Typical equity skew:

```
IV
↑
40% |\
35% | \
30% |  \
25% |   \____
    |___________→ Strike
     OTM P  ATM  OTM C
```

- OTM puts → high IV (crash risk, insurance demand)
- ATM options → lower IV
- OTM calls → lower or moderately increasing IV

---

### Why Skew Exists

Skew is driven by:

- Demand for downside protection
- Institutional hedging flows
- Leverage and margin constraints
- Behavioral fear asymmetry

Skew reflects **market-implied asymmetry in future return distributions**.

---

## Why Skew Becomes Tradable

Skew is **persistent**, but:

- It changes magnitude
- It mean-reverts
- It overreacts during stress or events

**Trading opportunity arises when:**

- Put IV is *too rich* relative to calls
- Call IV is *too cheap*
- Historical or model-implied skew relationships break

---

## The Structure

### General Skew Trading Construction

Skew trades are typically:

- Same maturity
- Different strikes
- Long cheap volatility
- Short rich volatility
- Often delta-neutral

> **Long relative IV on one wing, short relative IV on the other.**

---

### Common Skew Trading Structures

#### 1. Risk Reversal

\[
\text{Risk Reversal} = \text{Long OTM Call} - \text{Short OTM Put}
\]

- Long upside IV
- Short downside IV
- Strong skew exposure

---

#### 2. Put vs Call Vertical Spread

- Sell expensive put spread
- Buy cheap call spread
- Delta-hedge

---

#### 3. Skewed Butterfly

- Sell rich downside wing
- Buy cheap upside wing
- ATM strike anchors payoff

---

## The Portfolio

\[
\Pi_{\text{skew}} = \sum_i n_i \cdot V(K_i, T, \sigma_i)
\]

Target exposures:

\[
\Delta \approx 0, \quad
\text{Vega}_{\text{down}} < 0, \quad
\text{Vega}_{\text{up}} > 0
\]

---

## The P&L Driver

\[
\text{P\&L} = \sum_i \text{Vega}_i (\sigma_i^{\text{fair}} - \sigma_i^{\text{market}})
\]

Profit comes from **skew normalization**, not direction.

---

## Risk Management

- Control tail risk
- Use spreads instead of naked options
- Hedge delta frequently
- Avoid event-heavy periods
- Define max loss upfront

---

## Relationship to Other Strategies

| Strategy | Dimension |
|--------|-----------|
| Vega trades | Vol level |
| Calendars | Term structure |
| Butterflies | Curvature |
| **Skew trades** | **Put–call asymmetry** |
| Surface arb | Full surface |

---

## Key Takeaways

- Skew trading is **relative-value volatility trading**
- Downside IV is structurally rich
- Delta management is essential
- Skew mean-reverts, but not always quickly

---

## One-Line Summary

> **Skew trading spreads exploit distortions in put–call implied volatility by trading asymmetry rather than volatility level.**
