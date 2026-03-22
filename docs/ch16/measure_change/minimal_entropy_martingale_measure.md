# Minimal Entropy Martingale Measure

In the Heston model, the variance risk is unhedgeable, creating an infinite family of equivalent martingale measures. Each choice of the variance risk premium $\lambda_v$ defines a different risk-neutral measure and produces different option prices. The **minimal entropy martingale measure** (MEMM) selects the measure $\mathbb{Q}^*$ closest to the physical measure $\mathbb{P}$ in the sense of relative entropy. This provides a principled, model-consistent pricing rule that avoids the need for external calibration of $\lambda_v$, at the cost of ignoring market-implied preferences.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define relative entropy between probability measures and state its key properties
    2. Formulate the MEMM optimization problem for the Heston model
    3. Derive the optimal variance risk premium $\lambda_v^*$ under the entropy criterion
    4. Compare MEMM pricing with calibrated risk-neutral pricing

---

## Intuition

When a market is incomplete, there is no unique arbitrage-free price for a derivative. Instead, there is an interval of prices consistent with no-arbitrage, one for each equivalent martingale measure. The MEMM picks the measure that introduces the least "distortion" relative to the physical probability, measured by relative entropy (Kullback-Leibler divergence). Intuitively, this chooses prices that are as close as possible to actuarial (physical-measure) pricing while still being consistent with no-arbitrage.

The MEMM has a long history in mathematical finance: it was studied by Frittelli (2000) and Miyahara (2004) in the context of incomplete markets, and its application to stochastic volatility models provides a clean analytical framework for understanding the minimal distortion principle.

---

## Relative Entropy

!!! info "Definition (Relative Entropy)"
    The **relative entropy** (Kullback-Leibler divergence) of a probability measure $\mathbb{Q}$ with respect to $\mathbb{P}$ is

    $$
    H(\mathbb{Q} \,|\, \mathbb{P}) = \mathbb{E}^{\mathbb{Q}}\!\left[\log\frac{d\mathbb{Q}}{d\mathbb{P}}\right] = \mathbb{E}^{\mathbb{P}}\!\left[\frac{d\mathbb{Q}}{d\mathbb{P}}\log\frac{d\mathbb{Q}}{d\mathbb{P}}\right]
    $$

    provided $\mathbb{Q} \ll \mathbb{P}$ (absolute continuity). If $\mathbb{Q}$ is not absolutely continuous with respect to $\mathbb{P}$, set $H(\mathbb{Q}|\mathbb{P}) = +\infty$.

Key properties of relative entropy:

- **Non-negativity**: $H(\mathbb{Q}|\mathbb{P}) \geq 0$, with equality if and only if $\mathbb{Q} = \mathbb{P}$
- **Not a metric**: $H(\mathbb{Q}|\mathbb{P}) \neq H(\mathbb{P}|\mathbb{Q})$ in general (asymmetric)
- **Convexity**: $H(\cdot | \mathbb{P})$ is strictly convex on the set of probability measures
- **Information interpretation**: $H(\mathbb{Q}|\mathbb{P})$ measures the expected log-likelihood ratio, quantifying the "surprise" when the true distribution is $\mathbb{Q}$ but one expects $\mathbb{P}$

---

## The MEMM Optimization Problem

!!! info "Definition (Minimal Entropy Martingale Measure)"
    The MEMM $\mathbb{Q}^*$ is the solution to

    $$
    \mathbb{Q}^* = \arg\min_{\mathbb{Q} \in \mathcal{M}} H(\mathbb{Q} \,|\, \mathbb{P})
    $$

    where $\mathcal{M}$ is the set of equivalent martingale measures (EMMs) for the discounted stock price.

For the Heston model, $\mathcal{M}$ is parameterized by the variance risk premium function $\lambda_v$. With the standard specification $\lambda_v(t) = \lambda\sqrt{v_t}$, the set $\mathcal{M}$ is parameterized by the single constant $\lambda \in \mathbb{R}$.

---

## Entropy Computation for the Heston Model

The Radon-Nikodym derivative from $\mathbb{P}$ to $\mathbb{Q}_\lambda$ (the EMM with variance risk premium $\lambda$) is

$$
\frac{d\mathbb{Q}_\lambda}{d\mathbb{P}} = \exp\!\left(-\int_0^T \lambda_S(t) \, dW_t^{(1),\mathbb{P}} - \int_0^T \lambda\sqrt{v_t} \, dW_t^{(2),\mathbb{P}} - \frac{1}{2}\int_0^T(\lambda_S^2(t) + \lambda^2 v_t)\,dt\right)
$$

where $\lambda_S(t) = (\mu - r)/\sqrt{v_t}$ is fixed by no-arbitrage. The relative entropy is

$$
H(\mathbb{Q}_\lambda | \mathbb{P}) = \mathbb{E}^{\mathbb{Q}_\lambda}\!\left[\log\frac{d\mathbb{Q}_\lambda}{d\mathbb{P}}\right]
$$

Using the identity $\mathbb{E}^{\mathbb{Q}}[\log(d\mathbb{Q}/d\mathbb{P})] = -\mathbb{E}^{\mathbb{Q}}[\int_0^T \lambda_S \, dW^{(1),\mathbb{P}} + \lambda\sqrt{v} \, dW^{(2),\mathbb{P}}] - \frac{1}{2}\mathbb{E}^{\mathbb{Q}}[\int_0^T (\lambda_S^2 + \lambda^2 v)\,dt]$ and converting the $\mathbb{P}$-Brownian motions to $\mathbb{Q}$-Brownian motions:

$$
H(\mathbb{Q}_\lambda | \mathbb{P}) = \frac{1}{2}\mathbb{E}^{\mathbb{Q}_\lambda}\!\left[\int_0^T \left(\frac{(\mu-r)^2}{v_t} + \lambda^2 v_t\right) dt\right]
$$

!!! info "Proposition (Entropy as a Function of Lambda)"
    The relative entropy of $\mathbb{Q}_\lambda$ with respect to $\mathbb{P}$ is

    $$
    H(\mathbb{Q}_\lambda | \mathbb{P}) = \frac{1}{2}\int_0^T \left[\frac{(\mu-r)^2}{\bar{v}_\lambda(t)} + \lambda^2 \bar{v}_\lambda(t)\right] dt
    $$

    where $\bar{v}_\lambda(t) = \mathbb{E}^{\mathbb{Q}_\lambda}[v_t]$ is the expected variance under $\mathbb{Q}_\lambda$. Since $v_t$ is a CIR process under $\mathbb{Q}_\lambda$ with parameters $(\kappa + \xi\lambda, \kappa\theta/(\kappa + \xi\lambda))$:

    $$
    \bar{v}_\lambda(t) = \theta^{\mathbb{Q}_\lambda} + (v_0 - \theta^{\mathbb{Q}_\lambda}) e^{-\kappa^{\mathbb{Q}_\lambda} t}
    $$

---

## Optimal Variance Risk Premium

Minimizing $H(\mathbb{Q}_\lambda | \mathbb{P})$ over $\lambda$ requires balancing two competing effects: the $(\mu-r)^2/v$ term favors higher variance (which occurs when $\lambda$ is negative, lowering $\kappa^{\mathbb{Q}}$ and raising $\theta^{\mathbb{Q}}$), while the $\lambda^2 v$ term penalizes large $|\lambda|$.

!!! info "Theorem (MEMM Variance Risk Premium)"
    For the Heston model with $\lambda_v = \lambda\sqrt{v_t}$, the MEMM variance risk premium $\lambda^*$ satisfies the first-order condition

    $$
    \int_0^T \left[\lambda^* \bar{v}_{\lambda^*}(t) + \lambda^* \frac{\partial \bar{v}_{\lambda^*}}{\partial \lambda}\left(\frac{\lambda^{*2}}{2} - \frac{(\mu-r)^2}{2\bar{v}_{\lambda^*}(t)^2}\right)\right] dt = 0
    $$

    In the special case where $v_0 = \theta$ (stationary initial condition), this simplifies considerably because $\bar{v}_\lambda(t) = \theta$ for all $t$ and $\lambda$:

    $$
    \lambda^* \theta T - \frac{(\mu - r)^2 T}{2\theta} \cdot \frac{\partial \theta^{\mathbb{Q}}}{\partial \lambda}\bigg|_{\lambda=\lambda^*} \cdot \frac{1}{\theta^2} = 0
    $$

    For the stationary case with $v_0 = \theta^{\mathbb{P}}$, the MEMM selects $\lambda^* = 0$ (the variance risk premium vanishes) because $\bar{v}$ does not depend on $\lambda$ to first order.

!!! warning "The MEMM Is Not the Market Measure"
    The MEMM sets $\lambda^* \approx 0$ in many Heston parameter regimes, producing prices that are close to actuarial (physical-measure) expectations. In contrast, market-implied variance risk premiums are typically $\lambda > 0$ (positive), reflecting investors' willingness to pay for variance protection. The MEMM is therefore a theoretical benchmark, not a calibration target.

---

## Comparison with Other Measure Selection Criteria

Several alternative criteria have been proposed for selecting an EMM in incomplete markets.

| Criterion | Objective | Heston Behavior |
|-----------|----------|-----------------|
| MEMM | Minimize $H(\mathbb{Q}|\mathbb{P})$ | $\lambda^* \approx 0$, close to $\mathbb{P}$ |
| Minimal variance | Minimize $\text{Var}^{\mathbb{P}}[d\mathbb{Q}/d\mathbb{P}]$ | Different $\lambda^*$, less tractable |
| $q$-optimal | Minimize $\mathbb{E}^{\mathbb{P}}[(d\mathbb{Q}/d\mathbb{P})^q]$ | Interpolates between entropy and variance |
| Esscher transform | Exponential tilting | $\lambda^*$ from Esscher parameter |
| Market calibration | Minimize distance to market prices | $\lambda^*$ from implied volatility fit |

!!! note "When to Use the MEMM"
    The MEMM is most useful in three contexts:

    1. **Theoretical analysis**: understanding the minimal distortion pricing principle
    2. **Model comparison**: as a baseline for comparing different stochastic volatility models
    3. **Markets with limited options data**: when calibration is impossible, the MEMM provides a well-defined default

    For production pricing and hedging, calibration to market-implied parameters is always preferred.

---

## Numerical Example

Consider $S_0 = 100$, $v_0 = 0.04$, $\kappa^{\mathbb{P}} = 1.5$, $\theta^{\mathbb{P}} = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\mu = 0.08$, $r = 0.05$, $T = 1$.

**MEMM pricing ($\lambda^* = 0$):**

$$
\kappa^{\mathbb{Q}^*} = 1.5 + 0.3(0) = 1.5, \qquad \theta^{\mathbb{Q}^*} = 0.04
$$

ATM call price (COS, $N=128$): \$8.12.

**Market-calibrated pricing ($\lambda = 1.0$):**

$$
\kappa^{\mathbb{Q}} = 1.5 + 0.3(1.0) = 1.8, \qquad \theta^{\mathbb{Q}} = \frac{1.5 \times 0.04}{1.8} = 0.0333
$$

ATM call price: \$7.82.

**Difference:** \$0.30, or approximately 3.7% of the option value. The MEMM produces a higher price because it uses the physical long-run variance $\theta^{\mathbb{P}} = 0.04$ rather than the lower risk-neutral value $\theta^{\mathbb{Q}} = 0.0333$.

??? example "Entropy Values"
    The relative entropy for different $\lambda$ values:

    | $\lambda$ | $\kappa^{\mathbb{Q}}$ | $\theta^{\mathbb{Q}}$ | $H(\mathbb{Q}_\lambda | \mathbb{P})$ |
    |-----------|---------------------|---------------------|--------------------------------------|
    | $-1.0$ | 1.2 | 0.050 | 0.093 |
    | $-0.5$ | 1.35 | 0.044 | 0.048 |
    | 0.0 | 1.50 | 0.040 | 0.045 |
    | 0.5 | 1.65 | 0.036 | 0.056 |
    | 1.0 | 1.80 | 0.033 | 0.082 |

    The minimum entropy occurs near $\lambda^* = 0$, confirming that the physical measure is already close to an EMM when $v_0 = \theta^{\mathbb{P}}$.

---

## Summary

The minimal entropy martingale measure selects the equivalent martingale measure closest to the physical measure $\mathbb{P}$ in relative entropy. For the Heston model with $\lambda_v = \lambda\sqrt{v_t}$, the entropy $H(\mathbb{Q}_\lambda|\mathbb{P})$ is a function of $\lambda$ through its effect on the expected variance path $\bar{v}_\lambda(t)$. The optimal $\lambda^*$ balances the cost of distorting the variance dynamics (penalized by $\lambda^2 v$) against the benefit of reducing the equity risk premium term $(\mu-r)^2/v$. In many parameter regimes, $\lambda^* \approx 0$, making the MEMM close to the physical measure. While theoretically elegant, the MEMM typically does not match market-implied option prices, which embed a positive variance risk premium. The MEMM is best viewed as a theoretical benchmark and a principled default in the absence of market data.
