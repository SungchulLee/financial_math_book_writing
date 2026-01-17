# Robustness vs Optimality


Optimal strategies are model-dependent; robust strategies trade some optimality for stability under uncertainty.

---

## The model dependence problem


In Black–Scholes:
- **Optimal hedge**: Delta = \(N(d_1)\)
- **Optimal price**: Unique, given by the BS formula

In reality:
- Model parameters (\(\sigma\), \(r\), etc.) are uncertain
- Model structure (diffusion, jump, stochastic vol?) is uncertain
- The "optimal" strategy depends on the assumed model

**Key question:** How should we hedge when we don't know the true model?

---

## Two philosophies


**1. Optimal but fragile:**
- Calibrate a specific model
- Compute "optimal" Greeks and hedge ratios
- Performance is excellent if model is correct
- Performance can be disastrous if model is wrong

**2. Robust but suboptimal:**
- Consider a class of possible models
- Choose strategy that performs well across the class
- May not be optimal for any single model
- Avoids catastrophic losses

---

## Robust pricing bounds


Instead of a single price, compute bounds:

\[
\underline{V} \leq V_{\text{true}} \leq \overline{V}
\]

where the bounds hold for all models in an uncertainty set \(\mathcal{M}\).

**Example: volatility uncertainty.** If \(\sigma \in [\sigma_{\min}, \sigma_{\max}]\):

\[
\underline{V} = V^{\text{BS}}(\sigma_{\min}), \qquad \overline{V} = V^{\text{BS}}(\sigma_{\max})
\]

(for vanilla options where vega is positive).

**Width of bounds:**
\[
\overline{V} - \underline{V} \approx \nu \cdot (\sigma_{\max} - \sigma_{\min})
\]

Narrow bounds indicate prices are robust; wide bounds indicate model sensitivity.

---

## Robust hedging strategies


**Worst-case hedging:** Choose hedge that minimizes maximum loss:

\[
\Delta^* = \arg\min_\Delta \max_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \text{HedgingError}(\Delta, \sigma)
\]

For linear dependence on \(\sigma\), this often gives:

\[
\Delta^* = \frac{1}{2}\left(\Delta(\sigma_{\min}) + \Delta(\sigma_{\max})\right)
\]

**Model averaging:** Weight hedges by model probabilities:

\[
\Delta^* = \sum_i w_i \Delta_i
\]

where \(w_i\) are subjective weights on models \(i\).

---

## Stress testing across models


Test P&L under alternative models:

| Model | Key feature | Typical stress |
|:------|:------------|:---------------|
| Black–Scholes | Constant vol | Baseline |
| Local vol | \(\sigma(S,t)\) | Skew sensitivity |
| Heston | \(\sqrt{v}\, dW^{(2)}\) | Vol-of-vol |
| Jump-diffusion | Poisson jumps | Tail risk |
| SABR | \(\sigma_t\) mean-reverting | Smile dynamics |

A robust strategy should have bounded losses across all scenarios.

---

## Stability metrics


**1. P&L variance across models:**
\[
\text{Var}_{\mathcal{M}}(P\&L) = \mathbb{E}_{\mathcal{M}}[(P\&L - \bar{P\&L})^2]
\]

Low variance indicates robustness.

**2. Maximum drawdown:**
\[
\text{MaxDD} = \max_{\text{model} \in \mathcal{M}} (-P\&L)
\]

Robust strategies have bounded MaxDD.

**3. Sharpe ratio stability:**

Does the strategy remain profitable (positive Sharpe) across models?

---

## Model risk capital


Regulators require capital for model uncertainty:

\[
\text{Model Risk Capital} = \alpha \times (\overline{V} - \underline{V})
\]

where \(\alpha\) is a regulatory multiplier.

**Practical computation:**
1. Define model uncertainty set
2. Compute price bounds
3. Reserve capital for the range

---

## Robust Greeks


Instead of pointwise Greeks, report ranges:

\[
\Delta \in [\Delta_{\min}, \Delta_{\max}]
\]

This reflects:
- Uncertainty in implied volatility surface
- Model choice ambiguity
- Calibration error

**Example:** A trader might report "Delta is 0.52 ± 0.03" rather than just "0.52".

---

## Practical robust hedging rules


1. **Don't over-hedge**: If delta is uncertain, partial hedging may be optimal
2. **Diversify hedge instruments**: Use multiple options, not just spot
3. **Monitor hedge slippage**: Track realized vs expected hedge P&L
4. **Set model risk limits**: Cap exposure to model-dependent positions
5. **Use model ensembles**: Average across calibrated models

---

## The robustness-optimality tradeoff


The relationship can be visualized:

```
Expected Return
     ^
     |        * Optimal (fragile)
     |       /
     |      /
     |     /
     |    * Robust (stable)
     |   /
     |  /
     | /
     +-----------------> Worst-Case Loss
```

Robust strategies sacrifice some expected return for reduced tail risk.

---

## Connections to other fields


**1. Robust optimization:** Minimize worst-case cost subject to uncertainty

**2. Distributionally robust:** Optimize over a family of probability measures

**3. Minimax regret:** Minimize the maximum difference from the best strategy in hindsight

**4. Bayesian model averaging:** Weight strategies by posterior model probabilities

> **Forward reference.** Robust pricing and hedging is developed rigorously in **Chapter 13**, including duality theory and superhedging.

---

## What to remember


- Robust design uses stress tests across models (local vol, stochastic vol, jumps)
- Stability of P&L drivers across regimes is often more important than pointwise optimality
- Report Greeks as ranges, not point estimates
- Reserve capital for model uncertainty (price bounds width)
- Optimal strategies can be fragile; robust strategies sacrifice some return for stability
- Practical robustness: diversify hedges, monitor slippage, set model risk limits
