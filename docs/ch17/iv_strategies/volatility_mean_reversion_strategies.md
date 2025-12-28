# Volatility Mean Reversion Strategies  
## Trading the Cyclical Nature of Volatility

**Volatility mean reversion strategies** exploit the empirical fact that volatility tends to **revert toward a long-term average** after periods of unusually high or low levels.

Rather than predicting direction, these strategies trade the **dynamics of uncertainty itself**.

---

## The Core Insight

**The fundamental idea:**

- Volatility is **not a random walk**
- It exhibits **clustering** and **mean reversion**
- Periods of high volatility are usually followed by lower volatility
- Periods of low volatility are usually followed by higher volatility
- This behavior is observable across asset classes and time scales

\[
\mathbb{E}[\sigma_{t+h} \mid \sigma_t] \rightarrow \bar{\sigma}
\]

> **Volatility spikes are temporary; calm does not last forever.**

---

## Why Volatility Mean-Reverts

Volatility mean reversion arises from:

- Market microstructure
- Leverage constraints
- Risk targeting and deleveraging
- Option hedging flows
- Behavioral overreaction and normalization

High volatility triggers:
- Risk reduction
- Lower leverage
- Reduced trading activity

Low volatility triggers:
- Increased leverage
- Risk-taking
- Crowded positioning

---

## What Mean Reversion Means in Practice

### Volatility Regimes

Volatility tends to oscillate between regimes:

- **Low-vol regime:** complacency, carry trades
- **Normal regime:** balanced risk-taking
- **High-vol regime:** stress, deleveraging

Each regime is unstable.

```
Vol
↑
40% |     ●
30% |   ●   ●
20% | ●       ●
10% |     ●
    |________________→ Time
```

Mean reversion strategies attempt to **fade extremes**, not predict exact turning points.

---

## The Structure

### General Mean Reversion Construction

Mean reversion trades typically:

- Sell volatility after **large spikes**
- Buy volatility after **unusually calm periods**
- Are expressed via options, variance, or volatility indices
- Are often combined with **time diversification**

> **You trade volatility when it is extreme relative to its own history.**

---

### Common Mean Reversion Structures

#### 1. Short Volatility After Spikes

- Sell ATM straddles or strangles
- Sell variance exposure
- Collect elevated implied volatility

Used when:
- IV is far above historical norms
- Market stress is subsiding

---

#### 2. Long Volatility After Compression

- Buy straddles or strangles
- Long gamma positions
- Prepare for volatility expansion

Used when:
- Volatility is unusually low
- Markets are complacent
- Leverage is elevated

---

#### 3. VIX Mean Reversion Trades

- Short VIX futures after spikes
- Long VIX after deep compression
- Trade volatility directly

---

#### 4. Calendar-Based Mean Reversion

- Sell near-term volatility spikes
- Buy longer-dated volatility
- Exploit normalization of term structure

---

## The Portfolio

\[
\Pi_{\text{MR}} = \sum_i n_i \cdot V(T_i, \sigma_i)
\]

Typically managed so that:

\[
\Delta \approx 0
\]

with exposure concentrated in **volatility level**, not direction.

---

## The P&L Formula

### Primary P&L Driver — Volatility Normalization

\[
\text{P\&L}_{\text{MR}} =
\text{Vega} \cdot (\sigma_{\text{entry}} - \sigma_{\text{exit}})
\]

- Short vol: profit if volatility declines
- Long vol: profit if volatility rises

---

### Secondary Effects

- **Theta:** Often positive when selling vol
- **Gamma:** Negative for short vol, positive for long vol
- **Delta:** Hedged or minimized

---

## Concrete Example

### Short Volatility After a Spike

**Underlying:** SPX  
**Spot:** 4400  
**VIX:** 38 (historical avg ≈ 20)

**Trade:**
- Sell 30-day ATM straddle
- Delta hedge

**Thesis:**
- Volatility spike caused by temporary shock
- Expect normalization

---

## Risk Management

### Key Risks

- Volatility can stay elevated longer than expected
- Regime shifts (new normal)
- Gap risk
- Correlation breakdown
- Model overconfidence

---

### Risk Controls

- Trade smaller size at extremes
- Scale in gradually
- Use defined-risk structures
- Diversify across maturities
- Hard stop-loss rules

---

## Relationship to Other Volatility Strategies

| Strategy | Primary Focus |
|--------|---------------|
| IV–RV trading | Volatility risk premium |
| Skew trading | Asymmetry |
| Term structure trading | Time dimension |
| **Mean reversion** | **Volatility level dynamics** |
| Surface arbitrage | Full surface |

> **Mean reversion is the backbone of volatility trading.**

---

## Key Takeaways

- Volatility mean reverts, but not instantly
- Extremes offer opportunity, not timing certainty
- Short vol earns carry but risks tails
- Long vol is costly but convex
- Risk management is essential

---

## One-Line Summary

> **Volatility mean reversion strategies trade extremes in uncertainty, betting that fear and complacency are temporary.**
