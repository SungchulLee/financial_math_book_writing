# Event Calendar Spreads  
## Trading Event-Driven Volatility Dislocations

**Event calendar spreads** exploit differences in implied volatility **before and after discrete events** such as earnings, economic releases, or policy announcements.

These strategies trade **when volatility occurs**, not whether price goes up or down.

---

## The Core Insight

**The fundamental idea:**

- Certain events create **localized volatility**
- Options expiring before an event embed **event risk**
- Options expiring after the event embed **less or diluted event risk**
- This creates **term-structure distortions** around the event
- Calendar spreads can isolate and trade this mismatch

> **You are trading the market’s pricing of *when* volatility will occur.**

---

## What Is Event Volatility?

### Discrete Events

Events that materially affect prices over short horizons:

- Earnings announcements
- CPI / inflation releases
- FOMC decisions
- Product launches
- Court rulings or regulatory decisions

These events create:
- Sudden jumps
- Volatility clustering
- Sharp implied volatility differences across maturities

---

### Event vs Non-Event Volatility

For a known event at time $t_E$:

- Options expiring **before** $t_E$: no event risk
- Options expiring **just after** $t_E$: full event risk
- Longer-dated options: event risk **averaged out**

This creates a **kink** in the term structure.

```
IV
↑
50% |        ●  (post-event)
40% |      ●
30% |   ●
20% | ●
    |________________→ Time
        pre     post
        event   event
```

---

## Why Event Volatility Is Tradable

Event-related IV is often:

- Overestimated (fear premium)
- Poorly distributed across maturities
- Mean-reverting immediately after the event

**Opportunities arise when:**

- Front-month IV is excessively inflated
- Back-month IV underprices event impact
- The market misprices event magnitude or timing

---

## The Structure

### General Event Calendar Construction

Event calendar spreads typically:

- Use **same strike**
- Use **different expirations**
- Sell event-rich volatility
- Buy event-diluted volatility

> **Sell concentrated uncertainty, buy diversified uncertainty.**

---

### Common Event Calendar Structures

#### 1. Classic Earnings Calendar Spread

\[
\text{Calendar} = +C(K, T_{\text{after}}) - C(K, T_{\text{before}})
\]

(or puts)

- Sell option expiring right after earnings
- Buy longer-dated option
- Delta-neutral near strike

---

#### 2. Double Calendar Around Events

- Calendar spreads at multiple strikes
- Covers a price range
- Reduces directional sensitivity

---

#### 3. Reverse Calendar (Event Underpricing)

- Buy near-term event volatility
- Sell longer-dated volatility
- Used when market underestimates event risk

---

## The Portfolio

\[
\Pi_{\text{event}} = V(K, T_{\text{after}}, \sigma_{\text{after}})
- V(K, T_{\text{before}}, \sigma_{\text{before}})
\]

Managed such that:

\[
\Delta \approx 0
\]

Primary exposure is to **relative IV across maturities**.

---

## The P&L Formula

### Primary P&L Driver — Event Volatility Decay

\[
\text{P\&L}_{\text{event}} =
\text{Vega}_{\text{near}} \cdot \Delta\sigma_{\text{near}}
+
\text{Vega}_{\text{far}} \cdot \Delta\sigma_{\text{far}}
\]

Typical pattern:

- Near-term IV collapses after event
- Far-term IV changes modestly
- Net profit from **front-month IV crush**

---

### Secondary Effects

- **Theta:** Usually positive
- **Gamma:** Concentrated near event
- **Delta:** Must be actively managed

---

## Concrete Example

### Earnings Calendar Spread

**Stock:** XYZ  
**Spot:** $100  
**Earnings:** In 12 days

**IVs:**

- 2-week ATM call: 65%
- 6-week ATM call: 38%

---

### Trade Construction

- Sell 2-week ATM call
- Buy 6-week ATM call
- Delta hedge

---

## Risk Management

### Key Risks

- Gap risk at the event
- Incorrect event magnitude
- Liquidity near expiration
- Assignment risk
- Volatility regime shifts

---

### Risk Controls

- Use defined-risk calendars
- Avoid extremely short-dated options
- Size conservatively
- Close before expiration if needed
- Diversify across events

---

## Relationship to Other Volatility Strategies

| Strategy | Primary Dimension |
|--------|-------------------|
| IV–RV trading | Volatility premium |
| Mean reversion | Volatility level |
| Skew trading | Strike asymmetry |
| **Event calendars** | **Timing of volatility** |
| Surface arbitrage | Full surface |

> **Event calendar spreads trade *when* volatility happens, not how much.**

---

## When Event Calendars Work Best

✅ Known, scheduled events  
✅ Liquid single-name options  
✅ Moderately elevated IV  
✅ Stable macro backdrop  

❌ Surprise events  
❌ Extreme crisis regimes  
❌ Illiquid names  
❌ Very short expirations  

---

## Key Takeaways

- Event calendars exploit volatility concentration
- Front-month IV often overprices events
- Profit comes from IV collapse, not direction
- Gap risk is real and must be managed
- Best used systematically across many events

---

## One-Line Summary

> **Event calendar spreads profit from mispricing in the timing of volatility around discrete market events.**
