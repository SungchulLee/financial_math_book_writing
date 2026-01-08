# Trend Following with Futures

## Overview
Trend following in futures focuses on capturing sustained directional moves using liquid, leveraged instruments across asset classes. Unlike options-based trend strategies, futures trend following relies on **price momentum, volatility targeting, and risk-managed position sizing**, rather than convexity or implied volatility.

This chapter presents a **systematic, asset-agnostic framework** used by CTAs and managed futures funds.

---

## Instruments
- Equity index futures (ES, NQ, RTY, DAX)
- Rates futures (TY, US, Bund)
- FX futures (6E, 6J, 6B)
- Commodity futures (CL, NG, GC, HG, ZC)

Key properties:
- Linear payoff
- No theta or vega
- Margin-based leverage
- Roll and carry effects

---

## Trend Definition

Common trend signals:
- Moving average crossovers (time-series momentum)
- Breakout rules (e.g. 20–55 day highs/lows)
- Time-series momentum:
  
\[
\text{Signal}_t = \text{sign}(P_t - P_{t-k})
\]

Trends are **directional, persistent, and regime-dependent**.

---

## Position Sizing

Risk is controlled via **volatility targeting**:

\[
w_i = \frac{\sigma^*}{\sigma_i}
\]

where:
- \(\sigma_i\): realized volatility of contract
- \(\sigma^*\): target portfolio volatility

This ensures:
- Equal risk contribution
- Stability across regimes
- Scalability

---

## Portfolio

- Cross-asset diversification
- Correlation-aware aggregation
- Dynamic scaling

Portfolio return:
\[
R_t = \sum_i w_i r_{i,t}
\]

Trend following profits primarily from **crisis convexity and tail persistence**.

---

## Risk Management

Key risks:
- Trend reversals
- Whipsaw markets
- Correlated drawdowns

Controls:
- Volatility scaling
- Stop-losses (optional)
- Signal smoothing
- Asset caps

---

## Carry and Roll Yield

Futures PnL decomposes into:
- Spot return
- Roll yield
- Collateral yield

Backwardation benefits long trends; contango penalizes them.

---

## Regime Behavior

Trend following performs best during:
- Macro dislocations
- Crisis periods
- Persistent inflation / deflation regimes

Underperforms during:
- Range-bound markets
- Rapid mean reversion

---

## Comparison with Options-Based Trend Following

| Aspect | Futures | Options |
|------|--------|---------|
| Payoff | Linear | Convex |
| Time decay | None | Yes |
| Vol exposure | Indirect | Explicit |
| Tail protection | Endogenous | Engineered |

---

## Institutional Perspective

Used by:
- CTAs
- Managed futures funds
- Risk parity overlays
- Crisis alpha sleeves

Trend following futures are often deployed as **portfolio insurance** rather than alpha-only strategies.

---

## Summary

Futures trend following is:
- Systematic
- Diversified
- Scalable
- Robust to model error

It complements option-based trend strategies by providing **linear exposure and crisis convexity through persistence rather than optionality**.