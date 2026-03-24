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

---

## Exercises

**Exercise 1.** For a European call with $S = K = 100$, $T = 0.5$, $r = 0.03$, and volatility uncertainty $\sigma \in [0.15, 0.30]$, compute the Black-Scholes price at both endpoints to obtain the robust price bounds $[\underline{V}, \overline{V}]$. What is the width of the bounds? If vega at the midpoint volatility $\sigma = 0.225$ is approximately $\nu = 20$, verify that $\overline{V} - \underline{V} \approx \nu(\sigma_{\max} - \sigma_{\min})$.

---

**Exercise 2.** The worst-case hedge is $\Delta^* = \frac{1}{2}(\Delta(\sigma_{\min}) + \Delta(\sigma_{\max}))$. For the option in Exercise 1, compute $\Delta(0.15)$ and $\Delta(0.30)$ and the robust hedge ratio $\Delta^*$. Compare this to the delta at the midpoint volatility $\Delta(0.225)$. Under what conditions does the simple average outperform the midpoint delta?

---

**Exercise 3.** Model risk capital is computed as $\text{MRC} = \alpha \times (\overline{V} - \underline{V})$ with regulatory multiplier $\alpha$. For a portfolio of 1,000 short calls (each with the bounds from Exercise 1), compute the model risk capital for $\alpha = 1.5$. If the trader reduces the volatility uncertainty to $\sigma \in [0.18, 0.25]$ through better calibration, by what percentage does the required capital decrease?

---

**Exercise 4.** A trader uses model averaging with three models: Black-Scholes ($w_1 = 0.3$, $\Delta_1 = 0.55$), Heston ($w_2 = 0.5$, $\Delta_2 = 0.52$), and SABR ($w_3 = 0.2$, $\Delta_3 = 0.58$). Compute the model-averaged delta $\Delta^* = \sum_i w_i \Delta_i$. If the realized P&L under each model's delta is $\$0.10$, $-\$0.05$, and $\$0.20$ respectively, compute the P&L under the averaged hedge. Is the averaged P&L better or worse than the best single model?

---

**Exercise 5.** The P&L variance across models measures robustness. A hedge strategy produces the following P&L under five stress scenarios: $+\$0.50$, $-\$0.30$, $+\$0.10$, $-\$0.80$, $+\$0.20$. Compute the mean P&L, P&L variance, and maximum drawdown. A second (more robust) strategy produces: $+\$0.15$, $-\$0.10$, $+\$0.05$, $-\$0.20$, $+\$0.10$. Compute the same metrics. Which strategy is preferable if the risk limit is a maximum drawdown of $\$0.50$?

---

**Exercise 6.** Robust Greeks are reported as ranges: $\Delta \in [\Delta_{\min}, \Delta_{\max}]$. For a European put with $S = 100$, $K = 95$, $T = 0.25$, $r = 0.03$, compute the delta range arising from volatility uncertainty $\sigma \in [0.18, 0.28]$. Compute the gamma range as well. A trader claims that gamma is "approximately 0.03." Is this precise enough given the model uncertainty? What is the relative uncertainty $(\Gamma_{\max} - \Gamma_{\min})/\bar{\Gamma}$?
