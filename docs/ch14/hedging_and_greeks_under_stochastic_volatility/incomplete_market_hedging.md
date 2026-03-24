# Incomplete Market Hedging


Stochastic volatility models operate in **incomplete markets**: not all sources of risk can be hedged using traded assets. This fundamentally changes hedging theory and practice.

---

## Why markets are incomplete


In stochastic volatility models:
- volatility is not directly tradable,
- variance shocks introduce independent risk,
- delta hedging alone cannot eliminate uncertainty.

As a result, perfect replication is impossible.

---

## Consequences for hedging


In an incomplete market:
- hedging strategies are not unique,
- residual risk remains even after optimal hedging,
- hedging performance depends on chosen objective.

This contrasts sharply with Black–Scholes replication.

---

## Common hedging instruments


Practitioners attempt to reduce incompleteness using:
- options of different strikes/maturities (vega hedging),
- variance swaps or volatility indices (when available),
- dynamic rebalancing across the surface.

Still, some risks remain irreducible.

---

## Hedging error as a random variable


Hedging error should be viewed as:

\[
\text{P&L}_{\text{hedge}} = \text{model error} + \text{unhedgeable risk}.
\]



Risk management focuses on:
- distribution of hedging error,
- tail risk,
- robustness across scenarios.

---

## Key takeaways


- Stochastic volatility implies incomplete markets.
- Hedging aims to reduce, not eliminate, risk.
- Residual risk must be measured and managed explicitly.

---

## Further reading


- Schweizer, mean–variance hedging.
- Cont, *Model Uncertainty and Its Impact on Pricing*.

---

## Exercises

**Exercise 1.** In the Heston model, the stock and bond provide two instruments, but there are two sources of risk ($W^S$ and $W^V$). Explain the dimension mismatch and why a single traded option (in addition to the stock and bond) would restore market completeness. What properties must this option have to be useful as a hedging instrument?

---

**Exercise 2.** A trader is short a 3-month ATM call on the S&P 500 and delta-hedges using the underlying. Under the Heston model with $\rho = -0.7$ and $\xi = 0.5$, explain qualitatively why the hedging P&L will have non-zero variance even with continuous rebalancing. Decompose the residual risk into (a) volatility risk and (b) correlation risk.

---

**Exercise 3.** Consider the hedging error decomposition

$$
\text{P\&L}_{\text{hedge}} = \text{Gamma P\&L} + \text{Vega P\&L} + \text{higher-order terms}
$$

If the trader uses Black-Scholes delta to hedge, the gamma P&L depends on $(\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)$. In a stochastic volatility world, $\sigma_{\text{realized}}$ is itself random. Explain why this makes the gamma P&L a random variable with non-zero variance, and contrast with the Black-Scholes case where gamma P&L has zero variance under continuous hedging.

---

**Exercise 4.** A portfolio manager uses variance swaps to partially hedge volatility risk. The variance swap payoff is $\text{RV}^2 - K_{\text{var}}$, where $\text{RV}$ is realized volatility and $K_{\text{var}}$ is the strike. Explain how adding a variance swap to a delta-hedged option position reduces the incompleteness of the market. Does a single variance swap fully complete the market under the Heston model? Why or why not?

---

**Exercise 5.** In an incomplete market, the hedging strategy that minimizes $\mathbb{E}[(H - V_T^\pi)^2]$ is called the mean-variance optimal hedge. Explain why this hedge depends on the risk-neutral measure $\mathbb{Q}$ chosen. If two practitioners use different models (and hence different $\mathbb{Q}$s) but the same instruments, will they arrive at the same hedge? What practical issue does this raise?

---

**Exercise 6.** Explain why the concept of "model error" is especially important in incomplete markets. In a complete market, any model that is arbitrage-free and fits market prices produces the same hedging strategy. In an incomplete market, different models produce different hedges even when they fit the same prices. Describe a scenario where two Heston calibrations with identical fit quality lead to materially different hedging strategies.
