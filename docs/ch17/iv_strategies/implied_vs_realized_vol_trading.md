# Implied vs Realized Vol Trading  
## Trading the Volatility Risk Premium

**Implied vs realized volatility trading** focuses on exploiting the systematic difference between **implied volatility (what the market prices)** and **realized volatility (what actually occurs)**.

This is one of the most fundamental and persistent edges in volatility trading.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/implied_vs_realized_vol_trading_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/implied_vs_realized_vol_trading_risk_premium.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/implied_vs_realized_vol_trading_strategy_returns.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/implied_vs_realized_vol_trading_win_rate.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- Implied volatility (IV) reflects **expected + risk premium**
- Realized volatility (RV) reflects **actual price movement**
- On average:
  \[
  \text{IV} > \text{RV}
  \]
- The difference is called the **volatility risk premium**
- Traders can systematically **sell or buy volatility** to capture this spread

> **You are trading the price of uncertainty versus the realized uncertainty.**

---

## What Are Implied and Realized Volatility?

### Implied Volatility (IV)

- Backed out from option prices
- Forward-looking
- Includes:
  - Expected volatility
  - Risk aversion
  - Tail-risk premium
  - Supply/demand effects

\[
\text{Option Price} = f(S, K, T, r, \sigma_{\text{implied}})
\]

---

### Realized Volatility (RV)

- Measured from historical price returns
- Backward-looking
- Computed as:

\[
\sigma_{\text{realized}} = \sqrt{\frac{252}{N} \sum_{i=1}^N (\log S_i - \log S_{i-1})^2}
\]

- What actually happens in the market

---

## Why IV Is Usually Higher Than RV

IV embeds compensation for:

- Crash risk
- Jump risk
- Model uncertainty
- Hedging demand
- Margin and capital constraints

This creates a **structural premium** paid by option buyers to option sellers.

> **Selling volatility is selling insurance.**

---

## Why the IV–RV Spread Is Tradable

The IV–RV gap is:

- Persistent
- Mean-reverting
- Observable
- Tradeable via options and variance instruments

**Trading opportunity arises when:**

- IV is unusually high relative to expected RV
- IV is unusually low relative to expected RV
- Market overprices or underprices future uncertainty

---

## The Structure

### General IV–RV Trading Construction

IV–RV trades typically involve:

- Selling or buying options (IV)
- Hedging directional exposure
- Letting realized volatility determine P&L

> **You are betting on realized volatility relative to what the option market implies.**

---

### Common IV–RV Trading Structures

#### 1. Short Straddle / Strangle (Classic Vol Selling)

\[
\text{Short Straddle} = -C(K) - P(K)
\]

- Sell implied volatility
- Delta-hedge
- Profit if realized volatility < implied

---

#### 2. Long Straddle (Vol Buying)

\[
\text{Long Straddle} = +C(K) + P(K)
\]

- Buy implied volatility
- Profit if realized volatility > implied
- Used around events or regime shifts

---

#### 3. Gamma Scalping (Pure IV–RV Play)

- Long gamma via options
- Actively delta-hedge
- Profit from realized volatility exceeding implied

---

#### 4. Variance Swaps (Institutional)

\[
\text{Payoff} = (\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)
\]

- Cleanest expression of IV–RV trade
- No vega smile or skew effects
- Not usually accessible to retail traders

---

## The Portfolio

### Generic IV–RV Portfolio

\[
\Pi_{\text{IV-RV}} = \sum_i n_i \cdot V(K_i, T, \sigma_{\text{implied}})
\]

Managed so that:

\[
\Delta \approx 0
\]

The portfolio’s P&L depends primarily on **realized volatility**.

---

## The P&L Formula

### Core P&L Driver

\[
\text{P\&L} \approx \text{Vega} \cdot (\sigma_{\text{implied}} - \sigma_{\text{realized}})
\]

- Short volatility:
  - Profit if RV < IV
- Long volatility:
  - Profit if RV > IV

---

### Decomposition

\[
\text{P\&L} =
\underbrace{\text{Theta}}_{\text{Vol premium}}
+
\underbrace{\text{Gamma P\&L}}_{\text{Realized vol}}
-
\underbrace{\text{Hedging costs}}_{\text{Slippage}}
\]

---

## Concrete Example

### Short Volatility Trade

**Underlying:** SPY  
**Spot:** 450  
**Maturity:** 30 days  
**ATM IV:** 22%

**Trade:**

- Sell ATM straddle
- Delta-hedge daily

**Outcome scenarios:**

1. **Realized vol = 15%**
   - Options decay faster than price moves
   - Theta dominates
   - Profit

2. **Realized vol = 22%**
   - Break-even (before costs)

3. **Realized vol = 30%**
   - Large price swings
   - Gamma losses dominate
   - Loss

---

## Risk Management

### Key Risks

- Tail risk (large jumps)
- Volatility clustering
- Regime shifts
- Gap risk
- Model error

---

### Risk Controls

- Position sizing
- Stop-loss rules
- Use spreads instead of naked options
- Diversify across time and assets
- Avoid known event risk (earnings, macro)

---

## Relationship to Other Volatility Strategies

| Strategy | What It Trades |
|--------|---------------|
| Directional options | Price |
| Skew trading | Strike asymmetry |
| Term structure trades | Time dimension |
| **IV–RV trading** | **Volatility premium** |
| Surface arbitrage | Full surface |

> **IV–RV trading is the foundation of most option-selling strategies.**

---

## When IV–RV Trading Works Best

✅ Normal markets  
✅ High implied volatility environments  
✅ Diversified portfolios  
✅ Systematic execution  

❌ Crisis regimes  
❌ Structural regime shifts  
❌ Illiquid options  
❌ Poor risk controls  

---

## Key Takeaways

- IV usually exceeds RV due to risk premium
- The IV–RV spread is persistent but risky
- Selling volatility earns premium but carries tail risk
- Buying volatility is expensive but convex
- Risk management is essential

---

## One-Line Summary

> **Implied vs realized volatility trading captures the volatility risk premium by betting on how much uncertainty actually materializes versus what the market prices.**
