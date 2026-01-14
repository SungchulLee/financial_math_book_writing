# No-Arbitrage Drift Condition


A defining feature of the HJM framework is that **no-arbitrage uniquely determines the drift** of forward rates once their volatility structure is specified.

---

## Risk-neutral requirement


Discounted bond prices must be martingales:


\[
\frac{P(t,T)}{B_t} \text{ is a martingale},
\]



where \(B_t\) is the money-market account.

This constraint fixes the drift of \(f(t,T)\).

---

## HJM drift condition


If


\[
df(t,T) = \alpha(t,T)dt + \sum_{i=1}^n \sigma_i(t,T)dW_t^i,
\]



then no-arbitrage implies


\[
\alpha(t,T)
= \sum_{i=1}^n \sigma_i(t,T)
\int_t^T \sigma_i(t,u)du.
\]



Thus:
- volatility is a modeling input,
- drift is implied, not chosen.

---

## Consequences


- Arbitrary forward volatility choices are allowed (subject to regularity).
- No separate market price of risk appears under \(\mathbb{Q}\).
- The initial curve is matched exactly.

---

## Practical implications


- Model calibration focuses on volatility structures.
- Numerical implementation requires discretization in maturity.
- Regularity assumptions are critical for stability.

---

## Key takeaways


- No-arbitrage fixes HJM drift.
- Volatility fully determines dynamics.
- This is a key conceptual shift from short-rate models.

---

## Further reading


- Heath, Jarrow & Morton (1992).
- Björk, *Arbitrage Theory in Continuous Time*.
