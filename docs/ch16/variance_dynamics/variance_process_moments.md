# Variance Process Moments

The moments of the CIR variance process -- both conditional (given $v_t$) and unconditional (stationary) -- are essential building blocks in the Heston framework. The conditional mean $\mathbb{E}[v_T | v_t]$ reveals the mean-reversion dynamics, the conditional variance $\text{Var}(v_T | v_t)$ quantifies uncertainty about future variance levels, and the integrated variance $\mathbb{E}[\int_t^T v_s\,ds | v_t]$ determines variance swap fair values. All these moments have closed-form expressions, derivable either from the non-central chi-squared transition density or directly from the SDE.

This section derives the first two conditional moments by two methods (SDE-based and distribution-based), extends to higher moments via a recursive formula, and computes the moments of the integrated variance. We assume familiarity with the [CIR transition density](cir_variance_process_solution.md).

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Derive $\mathbb{E}[v_T | v_t]$ and $\text{Var}(v_T | v_t)$ from the CIR SDE
    - Verify these moments using the non-central chi-squared distribution
    - Compute higher conditional moments via the recursive ODE method
    - Derive $\mathbb{E}[\int_t^T v_s\,ds | v_t]$ and $\text{Var}(\int_t^T v_s\,ds | v_t)$
    - State the stationary (unconditional) mean, variance, skewness, and kurtosis

---

## Conditional Mean

### Derivation from the SDE

!!! success "Proposition: Conditional Mean of v_T"
    For the CIR process $dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t$:

    $$
    \mathbb{E}[v_T \mid v_t] = \theta + (v_t - \theta)\,e^{-\kappa\tau}
    $$

    where $\tau = T - t$.

**Proof.** Define $m(\tau) = \mathbb{E}[v_{t+\tau} | v_t]$. Taking expectations of the SDE:

$$
\frac{dm}{d\tau} = \kappa(\theta - m(\tau))
$$

The stochastic integral $\mathbb{E}[\sigma_v\sqrt{v_s}\,dW_s] = 0$ vanishes because it is a martingale. This is a first-order linear ODE with initial condition $m(0) = v_t$. The solution is:

$$
m(\tau) = \theta + (v_t - \theta)\,e^{-\kappa\tau}
$$

$\square$

### Interpretation

The conditional mean is a weighted average of the current variance $v_t$ and the long-run level $\theta$, with the weight on $v_t$ decaying exponentially at rate $\kappa$:

- At $\tau = 0$: $\mathbb{E}[v_T | v_t] = v_t$ (trivially)
- As $\tau \to \infty$: $\mathbb{E}[v_T | v_t] \to \theta$ (mean reversion)
- At $\tau = \ln 2/\kappa$ (the half-life): $\mathbb{E}[v_T | v_t] = \frac{1}{2}(v_t + \theta)$

### Verification from the Non-Central Chi-Squared Distribution

From the [transition density](cir_variance_process_solution.md), $v_T | v_t \sim c\,\chi^2_\delta(\lambda)$ where $c = \sigma_v^2(1-e^{-\kappa\tau})/(4\kappa)$, $\delta = 4\kappa\theta/\sigma_v^2$, and $\lambda = 4\kappa v_t e^{-\kappa\tau}/(\sigma_v^2(1-e^{-\kappa\tau}))$. The mean of a non-central chi-squared is $\delta + \lambda$, so:

$$
\mathbb{E}[v_T | v_t] = c(\delta + \lambda) = \frac{\sigma_v^2(1-e^{-\kappa\tau})}{4\kappa}\left(\frac{4\kappa\theta}{\sigma_v^2} + \frac{4\kappa v_t e^{-\kappa\tau}}{\sigma_v^2(1-e^{-\kappa\tau})}\right) = \theta(1-e^{-\kappa\tau}) + v_t e^{-\kappa\tau}
$$

which matches the SDE-derived formula. $\square$

---

## Conditional Variance

!!! success "Proposition: Conditional Variance of v_T"
    For the CIR process:

    $$
    \text{Var}(v_T \mid v_t) = v_t\,\frac{\sigma_v^2 e^{-\kappa\tau}}{\kappa}(1 - e^{-\kappa\tau}) + \theta\,\frac{\sigma_v^2}{2\kappa}(1 - e^{-\kappa\tau})^2
    $$

**Proof.** Define $s(\tau) = \mathbb{E}[v_{t+\tau}^2 | v_t]$. Applying Ito's lemma to $v^2$:

$$
d(v_t^2) = 2v_t\,dv_t + (dv_t)^2 = 2v_t[\kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t] + \sigma_v^2 v_t\,dt
$$

$$
= [2\kappa\theta v_t - 2\kappa v_t^2 + \sigma_v^2 v_t]\,dt + 2\sigma_v v_t^{3/2}\,dW_t
$$

Taking expectations:

$$
\frac{ds}{d\tau} = (2\kappa\theta + \sigma_v^2)\,m(\tau) - 2\kappa\,s(\tau)
$$

where $m(\tau) = \mathbb{E}[v_{t+\tau}|v_t] = \theta + (v_t-\theta)e^{-\kappa\tau}$. This is a first-order linear ODE in $s$ with initial condition $s(0) = v_t^2$.

Solving via the integrating factor $e^{2\kappa\tau}$:

$$
s(\tau) = e^{-2\kappa\tau}v_t^2 + (2\kappa\theta + \sigma_v^2)\int_0^\tau e^{-2\kappa(\tau-u)}m(u)\,du
$$

After evaluating the integral and simplifying:

$$
s(\tau) = \left[\theta + (v_t - \theta)e^{-\kappa\tau}\right]^2 + v_t\,\frac{\sigma_v^2 e^{-\kappa\tau}}{\kappa}(1-e^{-\kappa\tau}) + \theta\,\frac{\sigma_v^2}{2\kappa}(1-e^{-\kappa\tau})^2
$$

Since $\text{Var}(v_T|v_t) = s(\tau) - m(\tau)^2$ and the first term equals $m(\tau)^2$, the result follows. $\square$

### Interpretation

The conditional variance has two components:

1. **Initial-condition-dependent term**: $v_t \cdot \frac{\sigma_v^2 e^{-\kappa\tau}}{\kappa}(1 - e^{-\kappa\tau})$, which is proportional to $v_t$ and decays with $\tau$
2. **Stationary term**: $\theta \cdot \frac{\sigma_v^2}{2\kappa}(1 - e^{-\kappa\tau})^2$, which grows from zero and saturates at $\theta\sigma_v^2/(2\kappa)$

For short $\tau$: $\text{Var}(v_T|v_t) \approx v_t\sigma_v^2\tau$ (the variance grows linearly, proportional to the current level).

For large $\tau$: $\text{Var}(v_T|v_t) \to \theta\sigma_v^2/(2\kappa)$ (the stationary variance, independent of $v_t$).

---

## Higher Conditional Moments

Higher conditional moments $\mathbb{E}[v_T^n | v_t]$ can be computed recursively.

!!! success "Proposition: Recursive Moment Formula"
    Define $m_n(\tau) = \mathbb{E}[v_{t+\tau}^n | v_t]$. Then for $n \geq 1$:

    $$
    \frac{dm_n}{d\tau} = n\kappa\theta\,m_{n-1}(\tau) + \left(\tfrac{1}{2}n(n-1)\sigma_v^2 - n\kappa\right)m_n(\tau)
    $$

    with initial condition $m_n(0) = v_t^n$.

**Proof.** Apply Ito's lemma to $v^n$:

$$
d(v_t^n) = nv_t^{n-1}\,dv_t + \tfrac{1}{2}n(n-1)v_t^{n-2}(dv_t)^2
$$

$$
= nv_t^{n-1}[\kappa(\theta-v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t] + \tfrac{1}{2}n(n-1)\sigma_v^2 v_t^{n-1}\,dt
$$

Taking expectations and noting $\mathbb{E}[dW_t] = 0$:

$$
\frac{dm_n}{d\tau} = n\kappa\theta\,m_{n-1} - n\kappa\,m_n + \tfrac{1}{2}n(n-1)\sigma_v^2\,m_n
$$

$\square$

The recursion shows that $m_n$ depends on $m_{n-1}$, so moments can be computed sequentially: $m_0 = 1 \to m_1 \to m_2 \to m_3 \to \cdots$

??? example "Third Conditional Moment"
    The third moment satisfies:

    $$
    \frac{dm_3}{d\tau} = 3\kappa\theta\,m_2(\tau) + (3\sigma_v^2 - 3\kappa)\,m_3(\tau)
    $$

    This ODE can be solved given $m_2(\tau)$ (already computed), but the closed-form expression is lengthy. In practice, the first two moments suffice for most applications (moment matching in simulation schemes, variance swap pricing).

---

## Integrated Variance Moments

The integrated variance $\int_t^T v_s\,ds$ appears in variance swap pricing and in the Broadie-Kaya exact simulation scheme. Its moments have closed-form expressions.

!!! success "Proposition: Integrated Variance Moments"
    Define $V_\tau = \int_t^{t+\tau} v_s\,ds$. Then:

    $$
    \mathbb{E}[V_\tau \mid v_t] = \theta\tau + (v_t - \theta)\,\frac{1 - e^{-\kappa\tau}}{\kappa}
    $$

    $$
    \text{Var}(V_\tau \mid v_t) = \frac{\sigma_v^2}{\kappa^2}\left[\theta\tau - 2(v_t - \theta)\frac{e^{-\kappa\tau} - 1}{\kappa} - \frac{v_t(e^{-\kappa\tau} - 1)^2}{\kappa} - \frac{\theta(1-e^{-\kappa\tau})^2}{2\kappa}\right]
    $$

**Proof (mean).** Integrate the conditional mean formula:

$$
\mathbb{E}[V_\tau | v_t] = \int_0^\tau \mathbb{E}[v_{t+s} | v_t]\,ds = \int_0^\tau \left[\theta + (v_t - \theta)e^{-\kappa s}\right]ds = \theta\tau + (v_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa}
$$

$\square$

!!! note "Variance Swap Fair Value"
    The fair strike of a variance swap with maturity $T$ is:

    $$
    K_{\text{var}} = \frac{1}{T}\mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T v_s\,ds\right] = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    For short maturities ($\kappa T \ll 1$), $K_{\text{var}} \approx v_0$. For long maturities ($\kappa T \gg 1$), $K_{\text{var}} \approx \theta$. This formula is one of the rare closed-form results for exotic pricing under Heston.

---

## Stationary (Unconditional) Moments

As $\tau \to \infty$, the CIR process reaches its stationary Gamma distribution (see [CIR transition density](cir_variance_process_solution.md)). The unconditional moments are:

| Moment | Formula | Value (typical parameters) |
|:---|:---:|:---:|
| Mean | $\theta$ | $0.04$ |
| Variance | $\frac{\theta\sigma_v^2}{2\kappa}$ | $\frac{0.04 \times 0.25}{4} = 0.0025$ |
| Skewness | $\frac{\sigma_v}{\sqrt{\kappa\theta}} \cdot \sqrt{2}$ | $\frac{0.5}{\sqrt{0.08}} \cdot 1.414 = 2.5$ |
| Excess kurtosis | $\frac{3\sigma_v^2}{\kappa\theta}$ | $\frac{0.75}{0.08} = 9.375$ |

The typical parameters used: $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.5$.

!!! warning "Heavy Tails of the Stationary Distribution"
    The stationary distribution of the CIR process is a Gamma distribution, which has positive skewness and excess kurtosis. With typical calibrated parameters, the skewness exceeds 2 and the kurtosis exceeds 9, indicating a strongly right-skewed, heavy-tailed distribution for the variance. This means variance spikes (e.g., during market crises) are much more likely than a Gaussian model would suggest.

---

## Worked Example: Moment Calculations

??? example "Full Moment Calculation"
    Parameters: $\kappa = 2.0$, $\theta = 0.04$, $\sigma_v = 0.5$, $v_t = 0.06$, $\tau = 0.25$ years.

    **Conditional mean:**

    $$
    \mathbb{E}[v_T|v_t] = 0.04 + (0.06 - 0.04)e^{-0.5} = 0.04 + 0.02 \times 0.6065 = 0.04 + 0.01213 = 0.05213
    $$

    **Conditional variance:**

    $$
    \text{Var}(v_T|v_t) = 0.06 \cdot \frac{0.25 \times 0.6065}{2}(1-0.6065) + 0.04 \cdot \frac{0.25}{4}(1-0.6065)^2
    $$

    $$
    = 0.06 \times 0.0758 \times 0.3935 + 0.04 \times 0.0625 \times 0.1548 = 0.001789 + 0.000387 = 0.002176
    $$

    Standard deviation: $\sqrt{0.002176} \approx 0.0467$.

    **Coefficient of variation:** $0.0467 / 0.05213 \approx 0.90$. The standard deviation is 90\% of the mean, confirming the high uncertainty in future variance levels.

    **Integrated variance mean:**

    $$
    \mathbb{E}[V_{0.25}|v_t] = 0.04 \times 0.25 + (0.06 - 0.04)\frac{1-e^{-0.5}}{2} = 0.01 + 0.02 \times 0.1967 = 0.01 + 0.003935 = 0.01394
    $$

    The annualized variance swap strike is $K_{\text{var}} = 0.01394/0.25 = 0.05574$, corresponding to a volatility of $\sqrt{0.05574} \approx 23.6\%$.

---

## Summary

The CIR variance process has closed-form conditional moments at all orders, derivable from a recursive ODE system or from the non-central chi-squared transition density. The conditional mean $\mathbb{E}[v_T|v_t] = \theta + (v_t - \theta)e^{-\kappa\tau}$ exhibits exponential mean-reversion, while the conditional variance captures both the current-state-dependent and stationary components. The integrated variance $\int_t^T v_s\,ds$ has a closed-form mean that directly gives the variance swap fair value. The stationary distribution is Gamma with mean $\theta$, variance $\theta\sigma_v^2/(2\kappa)$, and substantial positive skewness.

The [next section](mean_reversion_and_long_run.md) examines the mean-reversion mechanism in detail, including the half-life, the term structure of variance, and the distinction between physical and risk-neutral mean-reversion parameters.

---
