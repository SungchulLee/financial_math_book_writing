# Intraday Momentum

## Overview
Intraday momentum trading with futures aims to exploit **short-horizon directional persistence** within the trading day using highly liquid, low-cost instruments. Unlike options-based intraday momentum, this approach relies on **linear exposure, execution efficiency, and volatility-adjusted sizing**, not gamma or implied volatility.

This strategy is widely used by **systematic intraday funds, prop desks, and high-frequency CTAs**.

---

## Instruments
- Equity index futures (ES, NQ, RTY)
- Rates futures (ZN, ZB)
- FX futures (6E, 6J)
- Liquid commodity futures (CL, GC)

Key characteristics:
- Linear payoff
- Tight bid–ask spreads
- High intraday liquidity
- No theta or vega

---

## Intraday Momentum

Common intraday signals:
- Opening range breakout (ORB)
- VWAP deviation
- Short-horizon returns:
  
\[
\text{Signal}_t = \text{sign}(P_t - P_{t-\Delta})
\]

where \(\Delta\) is measured in minutes.

Signals are:
- High frequency
- Mean-reverting at very short horizons
- Persistent during macro or news-driven days

---

## Entry and Exit Rules

Typical rules:
- Enter on breakout / momentum confirmation
- Trade only during high-liquidity windows
- Flat by end of session (no overnight risk)

This removes:
- Gap risk
- Overnight funding risk
- News exposure outside trading hours

---

## Position Sizing

Positions are sized using **intraday volatility targeting**:

\[
q_i = \frac{R^*}{\sigma_{i,\text{intra}}}
\]

where:
- \(\sigma_{i,\text{intra}}\): intraday realized volatility
- \(R^*\): target risk per trade

This enforces:
- Capital preservation
- Stability across regimes

---

## Transaction Costs

Critical considerations:
- Bid–ask spread
- Market impact
- Latency sensitivity

Most profits come from:
- Fast execution
- Low turnover filters
- Liquidity-aware sizing

---

## Risk Management

Primary risks:
- Whipsaws
- False breakouts
- Regime shifts

Controls:
- Time-based stops
- Volatility filters
- Max trades per day
- Daily loss limits

---

## Regime Dependence

Intraday momentum performs best when:
- Macro news releases occur
- Volatility is elevated
- Strong opening imbalances exist

Performs poorly when:
- Markets are range-bound
- Volatility is compressed

---

## Comparison with

| Aspect | Futures | Options |
|------|--------|---------|
| Payoff | Linear | Convex |
| Gamma | None | Central |
| IV exposure | None | Critical |
| Time decay | None | Present |
| Execution | Primary edge | Secondary |
| Tail capture | Limited | Strong |

---

## Institutional

Used by:
- Prop trading firms
- Intraday systematic funds
- Execution-driven desks

Often complements:
- Options gamma scalping
- Longer-horizon trend following

---

## Intraday momentum

Intraday momentum with futures is:
- Execution-driven
- Capital efficient
- Highly liquid
- Sensitive to regime and costs

It complements options-based intraday momentum by providing **pure linear exposure without volatility complexity**.