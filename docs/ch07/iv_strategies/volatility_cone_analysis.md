# Volatility Cone Analysis  
## Using Historical Volatility Ranges to Identify IV Opportunities

**Volatility cone analysis** compares current implied volatility to the historical distribution of realized volatility over different horizons, helping identify when implied volatility is **unusually high or low** relative to history.

This approach provides a **statistical framework** for volatility trading decisions.

---

## The Core Insight

**The fundamental idea:**

- Realized volatility fluctuates within **historical ranges**
- For each time horizon, volatility has:
  - A minimum
  - A maximum
  - A central tendency
- Implied volatility can be compared to these ranges
- Extreme deviations signal **potential trading opportunities**

> **You trade implied volatility relative to where realized volatility has historically lived.**

---

## What Is a Volatility Cone?

### Definition

A **volatility cone** is constructed by:

1. Measuring realized volatility over rolling windows
2. Using multiple lookback horizons
3. Computing statistical bands (e.g., min, max, percentiles)

For each maturity $T$:

\[
\sigma_{\text{realized}}(T) \in 
[\sigma_{\min}(T), \sigma_{\max}(T)]
\]

Plotting these bands across maturities forms a **cone**.

---

### Visual Intuition

```
Vol
↑
50% |        ┌──────── Max
40% |      ┌─┘
30% |    ┌─┘        ← Implied Vol
20% |  ┌─┘
10% |─┘───────────── Min
    |________________→ Time Horizon
      10d 30d 60d 90d
```

---

## Why Volatility Cones Are Useful

Volatility cones help answer:

- Is current IV **high or low** relative to history?
- Is the market pricing **too much or too little uncertainty**?
- Which maturities are statistically stretched?
- Where does mean reversion favor selling or buying volatility?

They provide **context**, not predictions.

---

## The Structure

### General Cone-Based Trading Framework

Cone-based trades typically:

- Compare IV to historical RV percentiles
- Sell volatility near the **upper cone**
- Buy volatility near the **lower cone**
- Are combined with risk management and filters

> **The cone defines the playing field; trades are taken at the edges.**

---

### Common Cone-Based Structures

#### 1. Short Volatility at Upper Cone

- Sell ATM straddles or strangles
- Sell variance exposure
- Used when IV is near historical maximums

---

#### 2. Long Volatility at Lower Cone

- Buy straddles or strangles
- Long gamma positions
- Used when IV is near historical minimums

---

#### 3. Maturity-Selective Trades

- Sell volatility only at maturities above the cone
- Buy volatility only at maturities below the cone
- Creates term-structure relative-value trades

---

#### 4. Cone-Filtered Strategies

- Apply cone filter to:
  - IV–RV trades
  - Mean reversion strategies
  - Event trades
- Avoid trades when IV sits in the middle of the cone

---

## The Portfolio

\[
\Pi_{\text{cone}} = \sum_i n_i \cdot V(T_i, \sigma_{\text{implied}, i})
\]

Managed such that:

\[
\Delta \approx 0
\]

Primary exposure is to **volatility level relative to historical bounds**.

---

## The P&L Formula

### Primary P&L Driver — Volatility Normalization

\[
\text{P\&L}_{\text{cone}} =
\text{Vega} \cdot (\sigma_{\text{implied}} - \sigma_{\text{realized}})
\]

Cone analysis does not generate P&L itself; it **identifies favorable entry points**.

---

## Concrete Example

### Short Volatility Using the Cone

**Underlying:** SPY  
**Maturity:** 30 days  

**Historical RV (30-day window):**
- Min: 10%
- Median: 18%
- Max: 32%

**Current ATM IV:** 34%

---

### Trade Decision

- IV is **above historical max**
- Expect volatility normalization
- Sell 30-day ATM straddle
- Delta hedge

---

## Risk Management

### Key Risks

- Structural regime changes
- New volatility environments
- Event-driven volatility
- Overreliance on historical data

---

### Risk Controls

- Combine cone with macro filters
- Avoid major scheduled events
- Scale positions at extremes
- Use defined-risk structures
- Stop trading when cone breaks

---

## Relationship to Other Volatility Strategies

| Strategy | Role of Cone |
|--------|---------------|
| IV–RV trading | Entry filter |
| Mean reversion | Regime context |
| Skew trading | Volatility level filter |
| Event calendars | Post-event check |
| Surface arbitrage | Risk constraint |

---

## Key Takeaways

- Volatility cones define historical volatility ranges
- IV extremes relative to the cone signal opportunity
- Cones guide *when* to trade, not *how*
- Best used as a filter, not a standalone system
- History informs risk, not certainty

---

## One-Line Summary

> **Volatility cone analysis uses historical realized volatility ranges to identify when implied volatility is statistically extreme and potentially mispriced.**
