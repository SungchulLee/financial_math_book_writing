# Robustness vs Optimality


Optimal strategies are model-dependent; robust strategies trade some optimality for stability under uncertainty.

---

## The model dependence problem


In Black–Scholes:

- **Optimal hedge**: Delta = $N(d_1)$
- **Optimal price**: Unique, given by the BS formula

In reality:

- Model parameters ($\sigma$, $r$, etc.) are uncertain
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

$$
\underline{V} \leq V_{\text{true}} \leq \overline{V}
$$

where the bounds hold for all models in an uncertainty set $\mathcal{M}$.

**Example: volatility uncertainty.** If $\sigma \in [\sigma_{\min}, \sigma_{\max}]$:

$$
\underline{V} = V^{\text{BS}}(\sigma_{\min}), \qquad \overline{V} = V^{\text{BS}}(\sigma_{\max})
$$

(for vanilla options where vega is positive).

**Width of bounds:**

$$
\overline{V} - \underline{V} \approx \nu \cdot (\sigma_{\max} - \sigma_{\min})
$$

Narrow bounds indicate prices are robust; wide bounds indicate model sensitivity.

---

## Robust hedging strategies


**Worst-case hedging:** Choose hedge that minimizes maximum loss:

$$
\Delta^* = \arg\min_\Delta \max_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \text{HedgingError}(\Delta, \sigma)
$$

For linear dependence on $\sigma$, this often gives:

$$
\Delta^* = \frac{1}{2}\left(\Delta(\sigma_{\min}) + \Delta(\sigma_{\max})\right)
$$

**Model averaging:** Weight hedges by model probabilities:

$$
\Delta^* = \sum_i w_i \Delta_i
$$

where $w_i$ are subjective weights on models $i$.

---

## Stress testing across models


Test P&L under alternative models:

| Model | Key feature | Typical stress |
|:------|:------------|:---------------|
| Black–Scholes | Constant vol | Baseline |
| Local vol | $\sigma(S,t)$ | Skew sensitivity |
| Heston | $\sqrt{v}\, dW^{(2)}$ | Vol-of-vol |
| Jump-diffusion | Poisson jumps | Tail risk |
| SABR | $\sigma_t$ mean-reverting | Smile dynamics |

A robust strategy should have bounded losses across all scenarios.

---

## Stability metrics


**1. P&L variance across models:**

$$
\text{Var}_{\mathcal{M}}(P\&L) = \mathbb{E}_{\mathcal{M}}[(P\&L - \bar{P\&L})^2]
$$

Low variance indicates robustness.

**2. Maximum drawdown:**

$$
\text{MaxDD} = \max_{\text{model} \in \mathcal{M}} (-P\&L)
$$

Robust strategies have bounded MaxDD.

**3. Sharpe ratio stability:**

Does the strategy remain profitable (positive Sharpe) across models?

---

## Model risk capital


Regulators require capital for model uncertainty:

$$
\text{Model Risk Capital} = \alpha \times (\overline{V} - \underline{V})
$$

where $\alpha$ is a regulatory multiplier.

**Practical computation:**

1. Define model uncertainty set
2. Compute price bounds
3. Reserve capital for the range

---

## Robust Greeks


Instead of pointwise Greeks, report ranges:

$$
\Delta \in [\Delta_{\min}, \Delta_{\max}]
$$

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

??? success "Solution to Exercise 1"
    For a European call with $S = K = 100$, $T = 0.5$, $r = 0.03$, we compute the Black-Scholes price at $\sigma = 0.15$ and $\sigma = 0.30$.

    **At $\sigma = 0.15$:**

    $$
    d_1 = \frac{\ln(100/100) + (0.03 + 0.15^2/2) \times 0.5}{0.15\sqrt{0.5}} = \frac{0 + (0.03 + 0.01125) \times 0.5}{0.15 \times 0.7071} = \frac{0.020625}{0.10607} = 0.1944
    $$

    $$
    d_2 = d_1 - 0.15\sqrt{0.5} = 0.1944 - 0.10607 = 0.0884
    $$

    $$
    N(0.1944) \approx 0.5771, \quad N(0.0884) \approx 0.5352
    $$

    $$
    \underline{V} = 100 \times 0.5771 - 100 e^{-0.015} \times 0.5352 = 57.71 - 98.51 \times 0.5352 = 57.71 - 52.72 = \$4.99
    $$

    **At $\sigma = 0.30$:**

    $$
    d_1 = \frac{0 + (0.03 + 0.045) \times 0.5}{0.30 \times 0.7071} = \frac{0.0375}{0.2121} = 0.1768
    $$

    $$
    d_2 = 0.1768 - 0.2121 = -0.0354
    $$

    $$
    N(0.1768) \approx 0.5702, \quad N(-0.0354) \approx 0.4859
    $$

    $$
    \overline{V} = 100 \times 0.5702 - 98.51 \times 0.4859 = 57.02 - 47.87 = \$9.15
    $$

    The robust price bounds are $[\underline{V}, \overline{V}] = [\$4.99, \$9.15]$.

    Width of bounds: $\overline{V} - \underline{V} = \$9.15 - \$4.99 = \$4.16$.

    **Verification using vega:** At $\sigma = 0.225$ (midpoint), vega is approximately $\nu \approx 20$. The linear approximation gives

    $$
    \overline{V} - \underline{V} \approx \nu(\sigma_{\max} - \sigma_{\min}) = 20 \times (0.30 - 0.15) = 20 \times 0.15 = \$3.00
    $$

    The linear approximation ($\$3.00$) underestimates the actual width ($\$4.16$) because vega itself changes with $\sigma$ (the relationship is convex due to non-zero volga). The first-order approximation is reasonable but not exact over a wide volatility range.

---

**Exercise 2.** The worst-case hedge is $\Delta^* = \frac{1}{2}(\Delta(\sigma_{\min}) + \Delta(\sigma_{\max}))$. For the option in Exercise 1, compute $\Delta(0.15)$ and $\Delta(0.30)$ and the robust hedge ratio $\Delta^*$. Compare this to the delta at the midpoint volatility $\Delta(0.225)$. Under what conditions does the simple average outperform the midpoint delta?

??? success "Solution to Exercise 2"
    We need to compute $\Delta(\sigma)$ for the ATM call with $S = K = 100$, $T = 0.5$, $r = 0.03$.

    Recall $\Delta = N(d_1)$ where $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$.

    **At $\sigma = 0.15$:** From Exercise 1, $d_1 = 0.1944$, so $\Delta(0.15) = N(0.1944) \approx 0.5771$.

    **At $\sigma = 0.30$:** From Exercise 1, $d_1 = 0.1768$, so $\Delta(0.30) = N(0.1768) \approx 0.5702$.

    **Robust hedge ratio:**

    $$
    \Delta^* = \frac{1}{2}(\Delta(0.15) + \Delta(0.30)) = \frac{1}{2}(0.5771 + 0.5702) = 0.5737
    $$

    **At midpoint $\sigma = 0.225$:**

    $$
    d_1 = \frac{0 + (0.03 + 0.225^2/2) \times 0.5}{0.225 \times 0.7071} = \frac{(0.03 + 0.02531) \times 0.5}{0.15910} = \frac{0.02766}{0.15910} = 0.1738
    $$

    $$
    \Delta(0.225) = N(0.1738) \approx 0.5690
    $$

    The robust average ($0.5737$) is slightly higher than the midpoint delta ($0.5690$). The difference is small ($0.0047$) because for ATM options, delta is relatively insensitive to volatility (the $d_1$ formula for ATM options gives $d_1 \approx \sigma\sqrt{T}/2$, which changes slowly).

    The simple average outperforms the midpoint delta when the hedging error is a convex (or concave) function of $\sigma$. If the P&L-vs-$\sigma$ relationship has significant curvature, the average of the endpoint deltas captures the curvature effect that the midpoint delta misses. This is analogous to using the trapezoidal rule vs. midpoint rule for integration.

---

**Exercise 3.** Model risk capital is computed as $\text{MRC} = \alpha \times (\overline{V} - \underline{V})$ with regulatory multiplier $\alpha$. For a portfolio of 1,000 short calls (each with the bounds from Exercise 1), compute the model risk capital for $\alpha = 1.5$. If the trader reduces the volatility uncertainty to $\sigma \in [0.18, 0.25]$ through better calibration, by what percentage does the required capital decrease?

??? success "Solution to Exercise 3"
    From Exercise 1, the price bounds are $[\underline{V}, \overline{V}] = [\$4.99, \$9.15]$, so $\overline{V} - \underline{V} = \$4.16$.

    For a portfolio of 1,000 short calls, the total model risk capital with $\alpha = 1.5$ is

    $$
    \text{MRC} = \alpha \times 1{,}000 \times (\overline{V} - \underline{V}) = 1.5 \times 1{,}000 \times 4.16 = \$6{,}240
    $$

    **With reduced uncertainty $\sigma \in [0.18, 0.25]$:**

    **At $\sigma = 0.18$:**

    $$
    d_1 = \frac{0 + (0.03 + 0.0162) \times 0.5}{0.18 \times 0.7071} = \frac{0.0231}{0.12728} = 0.1815
    $$

    $$
    d_2 = 0.1815 - 0.12728 = 0.0542
    $$

    $$
    N(0.1815) \approx 0.5720, \quad N(0.0542) \approx 0.5216
    $$

    $$
    V(0.18) = 100 \times 0.5720 - 98.51 \times 0.5216 = 57.20 - 51.38 = \$5.82
    $$

    **At $\sigma = 0.25$:**

    $$
    d_1 = \frac{0 + (0.03 + 0.03125) \times 0.5}{0.25 \times 0.7071} = \frac{0.030625}{0.17678} = 0.1732
    $$

    $$
    d_2 = 0.1732 - 0.17678 = -0.0036
    $$

    $$
    N(0.1732) \approx 0.5688, \quad N(-0.0036) \approx 0.4986
    $$

    $$
    V(0.25) = 100 \times 0.5688 - 98.51 \times 0.4986 = 56.88 - 49.12 = \$7.76
    $$

    New width: $7.76 - 5.82 = \$1.94$.

    New MRC $= 1.5 \times 1{,}000 \times 1.94 = \$2{,}910$.

    Percentage decrease:

    $$
    \frac{6{,}240 - 2{,}910}{6{,}240} = \frac{3{,}330}{6{,}240} \approx 53.4\%
    $$

    Better calibration (reducing the volatility uncertainty range from $[0.15, 0.30]$ to $[0.18, 0.25]$) decreases the required model risk capital by approximately $53\%$. This illustrates the direct economic value of improved calibration and model validation.

---

**Exercise 4.** A trader uses model averaging with three models: Black-Scholes ($w_1 = 0.3$, $\Delta_1 = 0.55$), Heston ($w_2 = 0.5$, $\Delta_2 = 0.52$), and SABR ($w_3 = 0.2$, $\Delta_3 = 0.58$). Compute the model-averaged delta $\Delta^* = \sum_i w_i \Delta_i$. If the realized P&L under each model's delta is $\$0.10$, $-\$0.05$, and $\$0.20$ respectively, compute the P&L under the averaged hedge. Is the averaged P&L better or worse than the best single model?

??? success "Solution to Exercise 4"
    The model-averaged delta is

    $$
    \Delta^* = \sum_i w_i \Delta_i = 0.3 \times 0.55 + 0.5 \times 0.52 + 0.2 \times 0.58
    $$

    $$
    = 0.165 + 0.260 + 0.116 = 0.541
    $$

    For the P&L under the averaged hedge: the P&L from hedging at $\Delta^*$ when the "true" delta is $\Delta_i$ depends on the realized move. However, the problem states the realized P&L under each model's own delta is $\$0.10$, $-\$0.05$, and $\$0.20$.

    The model-averaged P&L is

    $$
    \text{P\&L}^* = \sum_i w_i \times \text{P\&L}_i = 0.3 \times 0.10 + 0.5 \times (-0.05) + 0.2 \times 0.20
    $$

    $$
    = 0.030 - 0.025 + 0.040 = \$0.045
    $$

    The best single model is SABR with P&L $= \$0.20$.

    The averaged P&L ($\$0.045$) is worse than the best single model ($\$0.20$) and also worse than the Black-Scholes model ($\$0.10$). However, it is better than the Heston model ($-\$0.05$).

    This illustrates the fundamental tradeoff: model averaging does not beat the best model ex post, but it provides protection against choosing the worst model. The averaged strategy avoids the $-\$0.05$ loss that would result from committing entirely to Heston, while achieving a modest positive return. In practice, since we cannot know which model will be correct in advance, the averaged hedge represents a prudent compromise.

---

**Exercise 5.** The P&L variance across models measures robustness. A hedge strategy produces the following P&L under five stress scenarios: $+\$0.50$, $-\$0.30$, $+\$0.10$, $-\$0.80$, $+\$0.20$. Compute the mean P&L, P&L variance, and maximum drawdown. A second (more robust) strategy produces: $+\$0.15$, $-\$0.10$, $+\$0.05$, $-\$0.20$, $+\$0.10$. Compute the same metrics. Which strategy is preferable if the risk limit is a maximum drawdown of $\$0.50$?

??? success "Solution to Exercise 5"
    **Strategy 1** P&L values: $+0.50, -0.30, +0.10, -0.80, +0.20$.

    Mean P&L:

    $$
    \bar{x}_1 = \frac{0.50 - 0.30 + 0.10 - 0.80 + 0.20}{5} = \frac{-0.30}{5} = -\$0.06
    $$

    Variance:

    $$
    \text{Var}_1 = \frac{1}{5}\sum(x_i - \bar{x})^2 = \frac{(0.56)^2 + (-0.24)^2 + (0.16)^2 + (-0.74)^2 + (0.26)^2}{5}
    $$

    $$
    = \frac{0.3136 + 0.0576 + 0.0256 + 0.5476 + 0.0676}{5} = \frac{1.012}{5} = 0.2024
    $$

    Standard deviation: $\sqrt{0.2024} = \$0.450$.

    Maximum drawdown: $\max(-x_i) = \$0.80$.

    **Strategy 2** P&L values: $+0.15, -0.10, +0.05, -0.20, +0.10$.

    Mean P&L:

    $$
    \bar{x}_2 = \frac{0.15 - 0.10 + 0.05 - 0.20 + 0.10}{5} = \frac{0.00}{5} = \$0.00
    $$

    Variance:

    $$
    \text{Var}_2 = \frac{(0.15)^2 + (-0.10)^2 + (0.05)^2 + (-0.20)^2 + (0.10)^2}{5} = \frac{0.0225 + 0.01 + 0.0025 + 0.04 + 0.01}{5} = \frac{0.085}{5} = 0.017
    $$

    Standard deviation: $\sqrt{0.017} = \$0.130$.

    Maximum drawdown: $\max(-x_i) = \$0.20$.

    **Comparison:**

    | Metric | Strategy 1 | Strategy 2 |
    |:-------|:-----------|:-----------|
    | Mean P&L | $-\$0.06$ | $\$0.00$ |
    | Std dev | $\$0.45$ | $\$0.13$ |
    | Max drawdown | $\$0.80$ | $\$0.20$ |

    If the risk limit is a maximum drawdown of $\$0.50$, then **Strategy 1 violates** the limit (max drawdown $= \$0.80 > \$0.50$) and is inadmissible. **Strategy 2 satisfies** the limit (max drawdown $= \$0.20 < \$0.50$) and is the only permissible choice. Strategy 2 is also better on every metric: higher mean, lower variance, and lower drawdown. This is a clear case where the robust strategy dominates the aggressive one.

---

**Exercise 6.** Robust Greeks are reported as ranges: $\Delta \in [\Delta_{\min}, \Delta_{\max}]$. For a European put with $S = 100$, $K = 95$, $T = 0.25$, $r = 0.03$, compute the delta range arising from volatility uncertainty $\sigma \in [0.18, 0.28]$. Compute the gamma range as well. A trader claims that gamma is "approximately 0.03." Is this precise enough given the model uncertainty? What is the relative uncertainty $(\Gamma_{\max} - \Gamma_{\min})/\bar{\Gamma}$?

??? success "Solution to Exercise 6"
    For a European put with $S = 100$, $K = 95$, $T = 0.25$, $r = 0.03$, the put delta is $\Delta_{\text{put}} = N(d_1) - 1$ and gamma is $\Gamma = N'(d_1)/(S\sigma\sqrt{T})$.

    **At $\sigma = 0.18$:**

    $$
    d_1 = \frac{\ln(100/95) + (0.03 + 0.18^2/2) \times 0.25}{0.18 \times \sqrt{0.25}} = \frac{0.05129 + (0.03 + 0.0162) \times 0.25}{0.18 \times 0.5}
    $$

    $$
    = \frac{0.05129 + 0.01155}{0.09} = \frac{0.06284}{0.09} = 0.6982
    $$

    $$
    \Delta_{\text{put}}(0.18) = N(0.6982) - 1 \approx 0.7574 - 1 = -0.2426
    $$

    $$
    N'(0.6982) = \frac{1}{\sqrt{2\pi}}e^{-0.6982^2/2} = 0.3123
    $$

    $$
    \Gamma(0.18) = \frac{0.3123}{100 \times 0.18 \times 0.5} = \frac{0.3123}{9.0} = 0.03470
    $$

    **At $\sigma = 0.28$:**

    $$
    d_1 = \frac{0.05129 + (0.03 + 0.0392) \times 0.25}{0.28 \times 0.5} = \frac{0.05129 + 0.01730}{0.14} = \frac{0.06859}{0.14} = 0.4900
    $$

    $$
    \Delta_{\text{put}}(0.28) = N(0.4900) - 1 \approx 0.6879 - 1 = -0.3121
    $$

    $$
    N'(0.4900) = \frac{1}{\sqrt{2\pi}}e^{-0.4900^2/2} = 0.3521
    $$

    $$
    \Gamma(0.28) = \frac{0.3521}{100 \times 0.28 \times 0.5} = \frac{0.3521}{14.0} = 0.02515
    $$

    **Delta range:** $\Delta \in [-0.3121, -0.2426]$. The width is $0.0695$.

    **Gamma range:** $\Gamma \in [0.02515, 0.03470]$. Midpoint: $\bar{\Gamma} = (0.02515 + 0.03470)/2 = 0.02993$.

    The relative uncertainty in gamma is

    $$
    \frac{\Gamma_{\max} - \Gamma_{\min}}{\bar{\Gamma}} = \frac{0.03470 - 0.02515}{0.02993} = \frac{0.00955}{0.02993} = 0.319 \approx 32\%
    $$

    The trader's claim that gamma is "approximately 0.03" gives the midpoint accurately. However, the $32\%$ relative uncertainty means gamma could range from $0.025$ to $0.035$, a factor of $1.4$ between the extremes. For risk management purposes, stating "gamma $\approx 0.03$" without the uncertainty band is insufficiently precise. A more informative report would be "$\Gamma \in [0.025, 0.035]$" or "$\Gamma = 0.030 \pm 0.005$." This distinction matters for position sizing and hedging decisions, where a $30\%$ error in gamma translates directly into a $30\%$ error in the no-trade bandwidth and transaction cost estimates.
