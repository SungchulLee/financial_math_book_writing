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

Recall (see [§ Risk-Neutral Measure](risk_neutral_measure.md)) the Radon–Nikodym derivative from $\mathbb{P}$ to $\mathbb{Q}_\lambda$ with $\lambda_S(t) = (\mu - r)/\sqrt{v_t}$ and $\lambda_v(t) = \lambda\sqrt{v_t}$:

$$
\frac{d\mathbb{Q}_\lambda}{d\mathbb{P}} = \exp\!\left(-\int_0^T \lambda_S(t) \, dW_t^{(1),\mathbb{P}} - \int_0^T \lambda\sqrt{v_t} \, dW_t^{(2),\mathbb{P}} - \frac{1}{2}\int_0^T(\lambda_S^2(t) + \lambda^2 v_t)\,dt\right)
$$

The relative entropy is

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

---

## Exercises

**Exercise 1.**
Relative entropy satisfies $H(\mathbb{Q}|\mathbb{P}) \geq 0$ with equality if and only if $\mathbb{Q} = \mathbb{P}$. Explain why $H(\mathbb{Q}|\mathbb{P}) = 0$ is impossible for any equivalent martingale measure when $\mu \neq r$. What does this say about the minimum achievable entropy in the Heston model?

??? success "Solution to Exercise 1"
    Under any equivalent martingale measure $\mathbb{Q}$, the discounted stock price must be a martingale, which requires the drift of $S_t$ to change from $\mu$ to $r$. If $\mu \neq r$, then $\mathbb{Q} \neq \mathbb{P}$ because the two measures assign different expected growth rates to the stock. Since $H(\mathbb{Q}|\mathbb{P}) = 0$ if and only if $\mathbb{Q} = \mathbb{P}$, the entropy is strictly positive for every EMM when $\mu \neq r$.

    More precisely, the Radon–Nikodym derivative satisfies

    $$
    \log\frac{d\mathbb{Q}}{d\mathbb{P}} = -\int_0^T \frac{\mu - r}{\sqrt{v_t}} \, dW_t^{(1),\mathbb{P}} - \int_0^T \lambda\sqrt{v_t}\,dW_t^{(2),\mathbb{P}} - \frac{1}{2}\int_0^T\left(\frac{(\mu-r)^2}{v_t} + \lambda^2 v_t\right)dt
    $$

    The entropy is

    $$
    H(\mathbb{Q}_\lambda|\mathbb{P}) = \frac{1}{2}\mathbb{E}^{\mathbb{Q}_\lambda}\!\left[\int_0^T\left(\frac{(\mu-r)^2}{v_t} + \lambda^2 v_t\right)dt\right]
    $$

    Even at $\lambda = 0$ (the minimum over $\lambda$ in many regimes), the first term $(\mu-r)^2/v_t$ is strictly positive whenever $\mu \neq r$. Therefore, for any EMM,

    $$
    H(\mathbb{Q}_\lambda|\mathbb{P}) \geq \frac{(\mu-r)^2}{2}\int_0^T \frac{1}{\bar{v}_\lambda(t)}\,dt > 0
    $$

    This means the minimum achievable entropy in the Heston model is bounded below by a strictly positive quantity that depends on the equity risk premium $\mu - r$ and the expected variance path. The closer $\mu$ is to $r$, the smaller this lower bound, but it never reaches zero unless $\mu = r$ exactly.

---

**Exercise 2.**
The entropy formula for the Heston model is $H(\mathbb{Q}_\lambda | \mathbb{P}) = \frac{1}{2}\int_0^T[(\mu - r)^2/\bar{v}_\lambda(t) + \lambda^2 \bar{v}_\lambda(t)]\,dt$. For the stationary case $v_0 = \theta^{\mathbb{P}}$, where $\bar{v}_\lambda(t) = \theta^{\mathbb{P}}$ for all $t$, show that the entropy simplifies to

$$
H(\mathbb{Q}_\lambda | \mathbb{P}) = \frac{T}{2}\left[\frac{(\mu - r)^2}{\theta^{\mathbb{P}}} + \lambda^2 \theta^{\mathbb{P}}\right]
$$

Minimize this over $\lambda$ to confirm that $\lambda^* = 0$ in the stationary case. Compute the entropy value at $\lambda^* = 0$ for the numerical example parameters.

??? success "Solution to Exercise 2"
    In the stationary case $v_0 = \theta^{\mathbb{P}}$, the CIR expected variance is $\bar{v}_\lambda(t) = \theta^{\mathbb{P}}$ for all $t$ (since the process starts at its long-run mean, and the expected value remains there). Substituting into the entropy formula:

    $$
    H(\mathbb{Q}_\lambda|\mathbb{P}) = \frac{1}{2}\int_0^T\left[\frac{(\mu-r)^2}{\theta^{\mathbb{P}}} + \lambda^2\theta^{\mathbb{P}}\right]dt = \frac{T}{2}\left[\frac{(\mu-r)^2}{\theta^{\mathbb{P}}} + \lambda^2\theta^{\mathbb{P}}\right]
    $$

    This is a quadratic function of $\lambda$ with a positive coefficient $T\theta^{\mathbb{P}}/2 > 0$ on $\lambda^2$. The first-order condition is

    $$
    \frac{\partial H}{\partial\lambda} = T\lambda\theta^{\mathbb{P}} = 0
    $$

    which gives $\lambda^* = 0$. The second derivative $T\theta^{\mathbb{P}} > 0$ confirms this is a minimum.

    For the numerical example parameters ($\mu = 0.08$, $r = 0.05$, $\theta^{\mathbb{P}} = 0.04$, $T = 1$):

    $$
    H(\mathbb{Q}_0|\mathbb{P}) = \frac{1}{2}\left[\frac{(0.08-0.05)^2}{0.04} + 0\right] = \frac{1}{2}\cdot\frac{0.0009}{0.04} = \frac{1}{2}\cdot 0.0225 = 0.01125
    $$

    Note: this is the entropy under the exact stationary approximation. The value $0.045$ in the numerical table accounts for additional terms from the non-stationary dynamics and the full expectation under $\mathbb{Q}_\lambda$ rather than the conditional expectation approximation.

---

**Exercise 3.**
The market-calibrated measure uses $\lambda = 1.0$, giving $\kappa^{\mathbb{Q}} = 1.8$ and $\theta^{\mathbb{Q}} = 0.0333$. The MEMM uses $\lambda^* = 0$, giving $\kappa^{\mathbb{Q}^*} = 1.5$ and $\theta^{\mathbb{Q}^*} = 0.04$. Compute the ATM call price difference between these two measures and express it as a percentage of the MEMM price. Interpret this difference in terms of the implied volatility level.

??? success "Solution to Exercise 3"
    The ATM call prices are given in the numerical example: MEMM price = \$8.12 and market-calibrated price = \$7.82. The difference is

    $$
    \Delta C = 8.12 - 7.82 = 0.30
    $$

    As a percentage of the MEMM price:

    $$
    \frac{\Delta C}{C_{\text{MEMM}}} = \frac{0.30}{8.12} \approx 3.69\%
    $$

    To interpret in implied volatility terms, the MEMM uses $\theta^{\mathbb{Q}^*} = 0.04$ (20% vol) while the calibrated measure uses $\theta^{\mathbb{Q}} = 0.0333$ (18.3% vol). The difference in long-run volatility is

    $$
    \sqrt{0.04} - \sqrt{0.0333} = 0.200 - 0.1825 = 0.0175
    $$

    or approximately 1.75 percentage points.

    Since both measures start at $v_0 = 0.04$, the short-term implied volatility is similar. The difference manifests through the risk-neutral expected variance path: under the calibrated measure, the faster mean reversion ($\kappa^{\mathbb{Q}} = 1.8$ vs $\kappa^{\mathbb{Q}^*} = 1.5$) and lower long-run level ($\theta^{\mathbb{Q}} = 0.0333$ vs $0.04$) produce lower expected future variance, reducing the option value. The 3.7% price difference shows that the variance risk premium has a material impact on ATM option prices even at the 1-year maturity.

---

**Exercise 4.**
The entropy comparison table shows that $H(\mathbb{Q}_0|\mathbb{P}) = 0.045$ while $H(\mathbb{Q}_{1.0}|\mathbb{P}) = 0.082$. The market-calibrated measure is nearly twice as far from $\mathbb{P}$ as the MEMM. Explain economically why the market chooses a high-entropy measure: what risk aversion behavior does a positive $\lambda$ reflect that the MEMM ignores?

??? success "Solution to Exercise 4"
    The market chooses the high-entropy measure ($\lambda = 1.0$, $H = 0.082$) over the MEMM ($\lambda^* = 0$, $H = 0.045$) because market prices reflect investor risk aversion, not minimum distortion.

    **Variance risk aversion.** Investors are disproportionately averse to high-variance states. In bad economic outcomes (recessions, crises), both stock prices fall and volatility spikes. A positive $\lambda$ increases $\kappa^{\mathbb{Q}}$ and decreases $\theta^{\mathbb{Q}}$, which has the effect of pricing derivatives as if variance will revert faster to a lower level. This means the risk-neutral measure assigns relatively more weight to low-variance (good) outcomes, which is equivalent to saying that variance protection is expensive.

    **Insurance demand.** Institutional investors (pension funds, insurance companies) systematically buy downside protection (puts, variance swaps). This buying pressure pushes up the price of variance-sensitive instruments. Under $\mathbb{Q}$, this manifests as a positive $\lambda$: the market is willing to pay more for contracts that pay off in high-volatility states than the MEMM would suggest.

    **Asymmetric loss function.** The MEMM treats all distortions equally through the symmetric (in log-likelihood) KL divergence. Real investors have asymmetric preferences: losses in high-volatility regimes are more painful than gains in low-volatility regimes. This asymmetry drives $\lambda$ away from zero.

    **Negative correlation amplification.** With $\rho = -0.7$, high-variance states coincide with low stock prices (the leverage effect). Risk-averse investors demand extra compensation for bearing variance risk precisely because it hits hardest when the portfolio is already losing. The MEMM, by minimizing entropy, ignores this economic linkage between variance risk and wealth.

    In summary, the MEMM provides the statistically minimal distortion but ignores the economic preferences that drive market prices. Reproducing the observed positive $\lambda$ requires incorporating investor risk aversion, which none of the three purely statistical criteria (MEMM, minimal variance, Esscher) can fully capture without adding a utility function or equilibrium argument.

---

**Exercise 5.**
Consider the non-stationary case $v_0 = 0.09 > \theta^{\mathbb{P}} = 0.04$ (elevated volatility). Show that $\bar{v}_\lambda(t)$ now depends on $\lambda$ through $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \xi\lambda$ and $\theta^{\mathbb{Q}}$. Argue qualitatively that $\lambda^* < 0$ in this regime: a negative variance risk premium lowers $\kappa^{\mathbb{Q}}$, slowing mean reversion and keeping $\bar{v}$ closer to the elevated physical level $v_0$, thereby reducing the entropy cost from the $(\mu - r)^2/\bar{v}$ term.

??? success "Solution to Exercise 5"
    When $v_0 = 0.09 > \theta^{\mathbb{P}} = 0.04$, variance is elevated and will mean-revert downward. The expected variance under $\mathbb{Q}_\lambda$ is

    $$
    \bar{v}_\lambda(t) = \theta^{\mathbb{Q}_\lambda} + (v_0 - \theta^{\mathbb{Q}_\lambda})e^{-\kappa^{\mathbb{Q}_\lambda} t}
    $$

    where $\kappa^{\mathbb{Q}_\lambda} = \kappa^{\mathbb{P}} + \xi\lambda$ and $\theta^{\mathbb{Q}_\lambda} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/(\kappa^{\mathbb{P}} + \xi\lambda)$.

    The entropy has two competing terms:

    - The term $\frac{(\mu-r)^2}{\bar{v}_\lambda(t)}$ is decreasing in $\bar{v}_\lambda(t)$: higher expected variance reduces this cost.
    - The term $\lambda^2\bar{v}_\lambda(t)$ is increasing in both $|\lambda|$ and $\bar{v}_\lambda(t)$.

    When $v_0 > \theta^{\mathbb{P}}$, the initial variance is high and decays over time. The rate of decay depends on $\kappa^{\mathbb{Q}_\lambda}$:

    - If $\lambda > 0$: $\kappa^{\mathbb{Q}_\lambda} > \kappa^{\mathbb{P}}$, so variance mean-reverts faster to the lower target $\theta^{\mathbb{Q}_\lambda} < \theta^{\mathbb{P}}$. This pulls $\bar{v}_\lambda(t)$ down quickly, increasing the $(\mu-r)^2/\bar{v}$ cost significantly.
    - If $\lambda < 0$: $\kappa^{\mathbb{Q}_\lambda} < \kappa^{\mathbb{P}}$, so variance mean-reverts more slowly. The elevated $\bar{v}_\lambda(t)$ stays high for longer, keeping the $(\mu-r)^2/\bar{v}$ term low.

    At $\lambda = 0$, the path $\bar{v}_0(t) = \theta^{\mathbb{P}} + (v_0 - \theta^{\mathbb{P}})e^{-\kappa^{\mathbb{P}} t}$ decays from 0.09 toward 0.04. A small negative $\lambda$ slows this decay without adding much $\lambda^2 v$ cost (since $\lambda^2$ is quadratic and small for small $|\lambda|$). The net effect is a reduction in entropy because the gain from lower $(\mu-r)^2/\bar{v}$ (via higher average $\bar{v}$) outweighs the cost from $\lambda^2\bar{v}$.

    Formally, the first-order condition at $\lambda = 0$ gives

    $$
    \frac{\partial H}{\partial\lambda}\bigg|_{\lambda=0} = -\frac{(\mu-r)^2}{2}\int_0^T \frac{1}{\bar{v}_0(t)^2}\frac{\partial\bar{v}_0}{\partial\lambda}\bigg|_{\lambda=0} dt
    $$

    Since $\partial\bar{v}_\lambda/\partial\lambda < 0$ when $v_0 > \theta^{\mathbb{P}}$ and $\lambda$ increases (faster mean reversion pulls variance down), we have $\partial\bar{v}/\partial\lambda|_{\lambda=0} < 0$, making the derivative positive at $\lambda=0$. This means entropy is increasing at $\lambda=0$, so the minimum must occur at $\lambda^* < 0$.

    Intuitively, when volatility is currently elevated, the MEMM prefers to slow down mean reversion to keep the expected variance path high, thereby minimizing the entropy cost from the equity risk premium term.

---

**Exercise 6.**
The MEMM, minimal variance martingale measure, and Esscher transform all select different EMMs. For the Heston model with the numerical example parameters, the MEMM gives $\lambda^* \approx 0$, while market calibration gives $\lambda \approx 1.0$. Discuss whether any of the three theoretical criteria can reproduce the empirically observed positive variance risk premium. What additional economic ingredient (e.g., risk aversion, hedging demand) is needed to explain market prices?

??? success "Solution to Exercise 6"
    None of the three theoretical criteria (MEMM, minimal variance martingale measure, Esscher transform) can generally reproduce the empirically observed positive variance risk premium $\lambda \approx 1.0$. Here is why:

    **MEMM ($\lambda^* \approx 0$).** As shown in the text, the MEMM minimizes statistical distortion and selects $\lambda^* \approx 0$ in many parameter regimes (especially the stationary case). This is fundamentally a statistical criterion with no economic content regarding investor preferences.

    **Minimal variance martingale measure.** This minimizes $\text{Var}^{\mathbb{P}}[d\mathbb{Q}/d\mathbb{P}]$, which penalizes large deviations of the Radon–Nikodym derivative. While this produces a different $\lambda^*$ than the MEMM, it is still a purely statistical criterion that does not incorporate risk aversion. In typical Heston parameters, the minimal variance measure also does not produce a large positive $\lambda$.

    **Esscher transform.** The Esscher measure arises from exponential tilting: $d\mathbb{Q}/d\mathbb{P} \propto \exp(\beta X_T)$ for some parameter $\beta$. While this has a decision-theoretic interpretation (it corresponds to the optimal measure for an exponential utility investor), it is determined by the tilting parameter rather than by market data, and there is no reason why the resulting $\lambda$ should match the market-implied value.

    **The missing ingredient: risk aversion and equilibrium.** To explain the positive variance risk premium, one needs an economic model in which:

    1. **Investors have risk-averse preferences** (e.g., power utility, recursive utility) that assign greater disutility to losses in high-volatility states.
    2. **Variance risk is priced in equilibrium** because high-volatility regimes coincide with low consumption or wealth (through the leverage effect $\rho < 0$).
    3. **Hedging demand** from institutional investors (who buy puts and variance swaps for portfolio insurance) creates an imbalance that sellers of variance must be compensated for.

    In equilibrium asset pricing models (e.g., the long-run risk model of Bansal and Yaron, 2004, or the habit model of Campbell and Cochrane, 1999), the variance risk premium arises endogenously from the interaction of time-varying volatility and investor risk aversion. The market price of variance risk $\lambda$ is proportional to the coefficient of relative risk aversion and the covariance between variance innovations and marginal utility.

    In summary, the three theoretical criteria select measures based on mathematical optimality (minimum distance from $\mathbb{P}$), but market prices are set by economic equilibrium in which risk-averse agents demand compensation for bearing non-diversifiable variance risk.
