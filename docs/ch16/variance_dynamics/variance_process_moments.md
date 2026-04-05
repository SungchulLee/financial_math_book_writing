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

## Exercises

**Exercise 1.** Derive $\mathbb{E}[V_T \mid V_t] = \theta + (V_t - \theta)e^{-\kappa\tau}$ by solving the ODE $\frac{d}{d\tau}\mathbb{E}[V_{t+\tau}] = \kappa(\theta - \mathbb{E}[V_{t+\tau}])$ with initial condition $\mathbb{E}[V_t] = V_t$.

??? success "Solution to Exercise 1"
    We solve the ODE $\frac{d}{d\tau}m(\tau) = \kappa(\theta - m(\tau))$ with initial condition $m(0) = V_t$, where $m(\tau) = \mathbb{E}[V_{t+\tau} \mid V_t]$.

    **Step 1: Rewrite the ODE.**

    $$
    \frac{dm}{d\tau} + \kappa\,m = \kappa\theta
    $$

    This is a first-order linear ODE with constant coefficients.

    **Step 2: Find the integrating factor.** The integrating factor is $\mu(\tau) = e^{\kappa\tau}$. Multiplying both sides:

    $$
    \frac{d}{d\tau}\!\left(e^{\kappa\tau}m\right) = \kappa\theta\,e^{\kappa\tau}
    $$

    **Step 3: Integrate both sides from $0$ to $\tau$.**

    $$
    e^{\kappa\tau}m(\tau) - m(0) = \kappa\theta\int_0^\tau e^{\kappa s}\,ds = \kappa\theta \cdot \frac{e^{\kappa\tau} - 1}{\kappa} = \theta(e^{\kappa\tau} - 1)
    $$

    **Step 4: Solve for $m(\tau)$.**

    $$
    m(\tau) = e^{-\kappa\tau}m(0) + \theta(1 - e^{-\kappa\tau}) = e^{-\kappa\tau}V_t + \theta(1 - e^{-\kappa\tau})
    $$

    Rearranging:

    $$
    \mathbb{E}[V_T \mid V_t] = \theta + (V_t - \theta)e^{-\kappa\tau}
    $$

    This confirms the conditional mean formula. The derivation uses only the linearity of expectation and the fact that $\mathbb{E}[\sigma_v\sqrt{V_s}\,dW_s] = 0$ (the stochastic integral is a martingale with zero expectation).

---

**Exercise 2.** Compute the conditional variance $\operatorname{Var}(V_T \mid V_t) = V_t\frac{\sigma_v^2}{\kappa}(e^{-\kappa\tau} - e^{-2\kappa\tau}) + \frac{\theta\sigma_v^2}{2\kappa}(1 - e^{-\kappa\tau})^2$ for $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$, $V_t = 0.04$, $\tau = 1$. Is the conditional standard deviation of $V_T$ large relative to its mean?

??? success "Solution to Exercise 2"
    With $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$, $V_t = 0.04$, $\tau = 1$:

    First compute the needed quantities:

    $$
    e^{-\kappa\tau} = e^{-2} = 0.1353, \qquad 1 - e^{-\kappa\tau} = 0.8647
    $$

    **Conditional mean:**

    $$
    \mathbb{E}[V_T \mid V_t] = 0.04 + (0.04 - 0.04)e^{-2} = 0.04
    $$

    Since $V_t = \theta$, the expected value remains at $\theta$ for all $\tau$.

    **Conditional variance:**

    $$
    \operatorname{Var}(V_T \mid V_t) = V_t\frac{\sigma_v^2}{\kappa}(e^{-\kappa\tau} - e^{-2\kappa\tau}) + \frac{\theta\sigma_v^2}{2\kappa}(1 - e^{-\kappa\tau})^2
    $$

    Computing each term:

    *First term:*

    $$
    0.04 \times \frac{0.09}{2}(e^{-2} - e^{-4}) = 0.04 \times 0.045 \times (0.1353 - 0.01832) = 0.04 \times 0.045 \times 0.1170 = 0.0002106
    $$

    *Second term:*

    $$
    \frac{0.04 \times 0.09}{4}(0.8647)^2 = 0.0009 \times 0.7477 = 0.0006729
    $$

    *Total:*

    $$
    \operatorname{Var}(V_T \mid V_t) = 0.0002106 + 0.0006729 = 0.0008835
    $$

    **Conditional standard deviation:**

    $$
    \sigma_{V_T} = \sqrt{0.0008835} = 0.02972
    $$

    **Relative to the mean:** The coefficient of variation is:

    $$
    \text{CV} = \frac{0.02972}{0.04} = 0.743
    $$

    The conditional standard deviation is about 74% of the mean. This is large, indicating substantial uncertainty about future variance levels even when starting at the long-run mean. This high variability is characteristic of the CIR process with its square-root diffusion and is consistent with the empirically observed leptokurtic (heavy-tailed) distribution of realized variance.

---

**Exercise 3.** The integrated variance $\bar{V} = \frac{1}{\tau}\int_t^{t+\tau} V_s\,ds$ has conditional mean $\mathbb{E}[\bar{V} \mid V_t] = \theta + (V_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa\tau}$. Compute this for $\tau = 0.25$ (3-month variance swap) with $V_t = 0.05$, $\theta = 0.04$, $\kappa = 2$.

??? success "Solution to Exercise 3"
    The conditional mean of the average variance (variance swap fair strike) is:

    $$
    \mathbb{E}[\bar{V} \mid V_t] = \theta + (V_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa\tau}
    $$

    With $\tau = 0.25$, $V_t = 0.05$, $\theta = 0.04$, $\kappa = 2$:

    $$
    \kappa\tau = 2 \times 0.25 = 0.5
    $$

    $$
    \frac{1 - e^{-\kappa\tau}}{\kappa\tau} = \frac{1 - e^{-0.5}}{0.5} = \frac{1 - 0.6065}{0.5} = \frac{0.3935}{0.5} = 0.7870
    $$

    $$
    \mathbb{E}[\bar{V} \mid V_t] = 0.04 + (0.05 - 0.04) \times 0.7870 = 0.04 + 0.01 \times 0.7870 = 0.04 + 0.007870 = 0.04787
    $$

    The 3-month variance swap fair strike is $K_{\text{var}} = 0.04787$, corresponding to a fair volatility strike of $\sqrt{0.04787} = 21.88\%$.

    Note that this is between $V_t = 0.05$ (current annualized variance, or 22.36% volatility) and $\theta = 0.04$ (long-run variance, or 20% volatility). The factor $0.787$ indicates that over 3 months, the average variance is still dominated by the current variance level, with only partial mean reversion toward $\theta$.

---

**Exercise 4.** The stationary variance of $V_t$ is $\operatorname{Var}_\infty(V) = \theta\sigma_v^2/(2\kappa)$. Compute the coefficient of variation $\text{CV} = \sqrt{\operatorname{Var}_\infty(V)}/\theta$ for the parameters in Exercise 2. A CV greater than 1 indicates very heavy-tailed variance dynamics.

??? success "Solution to Exercise 4"
    The stationary variance of $V_t$ is:

    $$
    \operatorname{Var}_\infty(V) = \frac{\theta\sigma_v^2}{2\kappa}
    $$

    With $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$:

    $$
    \operatorname{Var}_\infty(V) = \frac{0.04 \times 0.09}{4} = \frac{0.0036}{4} = 0.0009
    $$

    The coefficient of variation is:

    $$
    \text{CV} = \frac{\sqrt{\operatorname{Var}_\infty(V)}}{\theta} = \frac{\sqrt{0.0009}}{0.04} = \frac{0.03}{0.04} = 0.75
    $$

    A coefficient of variation of 0.75 means the standard deviation is 75% of the mean. This is less than 1, so the variance dynamics are not *extremely* heavy-tailed, but they are still substantially more variable than a Gaussian model would suggest.

    For comparison, if we increased $\sigma_v$ to $0.5$ (keeping other parameters fixed):

    $$
    \text{CV} = \frac{\sqrt{0.04 \times 0.25 / 4}}{0.04} = \frac{\sqrt{0.0025}}{0.04} = \frac{0.05}{0.04} = 1.25
    $$

    With $\sigma_v = 0.5$, the CV exceeds 1, indicating very heavy-tailed variance dynamics. The threshold CV $= 1$ corresponds to $\sigma_v = \sqrt{2\kappa\theta} = \sqrt{0.16} = 0.4$, which is also the Feller condition boundary. When $\sigma_v > \sqrt{2\kappa\theta}$ (Feller condition violated), the CV exceeds 1 and the variance process can touch zero.

---

**Exercise 5.** Show that $\mathbb{E}[\int_t^T V_s\,ds \mid V_t] = \theta\tau + (V_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa}$ by integrating $\mathbb{E}[V_s \mid V_t]$ from $t$ to $T$. This formula gives the fair value of a variance swap starting at $t$ with maturity $T$.

??? success "Solution to Exercise 5"
    Starting from the conditional mean $\mathbb{E}[V_s \mid V_t] = \theta + (V_t - \theta)e^{-\kappa(s-t)}$ for $s \geq t$:

    $$
    \mathbb{E}\!\left[\int_t^T V_s\,ds \,\middle|\, V_t\right] = \int_t^T \mathbb{E}[V_s \mid V_t]\,ds
    $$

    The interchange of expectation and integration is justified by Fubini's theorem (the integrand is non-negative and integrable).

    Substituting the conditional mean:

    $$
    = \int_t^T \left[\theta + (V_t - \theta)e^{-\kappa(s-t)}\right]ds
    $$

    Using the substitution $u = s - t$ with $du = ds$, and the limits changing to $u \in [0, \tau]$ where $\tau = T - t$:

    $$
    = \int_0^\tau \left[\theta + (V_t - \theta)e^{-\kappa u}\right]du
    $$

    $$
    = \theta\int_0^\tau du + (V_t - \theta)\int_0^\tau e^{-\kappa u}\,du
    $$

    $$
    = \theta\tau + (V_t - \theta)\left[-\frac{1}{\kappa}e^{-\kappa u}\right]_0^\tau
    $$

    $$
    = \theta\tau + (V_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa}
    $$

    This is the variance swap fair value formula. For a variance swap with strike $K_{\text{var}}$ and maturity $T$, the annualized fair strike is:

    $$
    K_{\text{var}} = \frac{1}{\tau}\mathbb{E}^{\mathbb{Q}}\!\left[\int_t^T V_s\,ds \,\middle|\, V_t\right] = \theta + (V_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa\tau}
    $$

    For short maturities ($\kappa\tau \ll 1$), the factor $\frac{1 - e^{-\kappa\tau}}{\kappa\tau} \approx 1$, so $K_{\text{var}} \approx V_t$. For long maturities ($\kappa\tau \gg 1$), the factor vanishes and $K_{\text{var}} \approx \theta$.

---

**Exercise 6.** For the higher moments, the conditional third central moment of $V_T$ is needed for skewness. Without deriving it fully, explain why the CIR process has positive skewness (heavier right tail than left) and relate this to the square-root diffusion.

??? success "Solution to Exercise 6"
    The CIR process $dV_t = \kappa(\theta - V_t)\,dt + \sigma_v\sqrt{V_t}\,dW_t$ has positive skewness for two related reasons:

    **1. The square-root diffusion creates asymmetric volatility.** The diffusion coefficient $\sigma_v\sqrt{V_t}$ is an increasing function of $V_t$. When $V_t$ is above its mean $\theta$, the diffusion is larger, producing larger random fluctuations that can push $V_t$ even further above the mean. When $V_t$ is below the mean, the diffusion is smaller, limiting how far below the mean the process can go. This creates a natural asymmetry: upward excursions are amplified while downward excursions are dampened.

    **2. The non-negativity constraint truncates the left tail.** The process satisfies $V_t \geq 0$ a.s. (and $V_t > 0$ a.s. under the Feller condition). This provides a hard lower bound but no upper bound, automatically creating a right-skewed distribution.

    **3. The stationary distribution is Gamma.** The CIR process converges to a $\text{Gamma}(\alpha, \beta)$ stationary distribution with $\alpha = 2\kappa\theta/\sigma_v^2$ and $\beta = 2\kappa/\sigma_v^2$. The skewness of the Gamma distribution is $2/\sqrt{\alpha}$, which is always positive. For typical parameters ($\alpha$ in the range 1--4), the skewness ranges from 1 to 2, confirming a strongly right-skewed distribution.

    **Connection to the conditional third central moment:** The positive skewness at the distributional level implies that the conditional third central moment $\mathbb{E}[(V_T - \mathbb{E}[V_T|V_t])^3 | V_t]$ is positive. Heuristically, from the recursive moment ODE, the third moment depends on the second moment and inherits the asymmetry of the square-root diffusion. The detailed derivation (through the $n=3$ case of the recursive formula) produces a lengthy but positive expression for all positive parameter values.

    **Financial implication:** The positive skewness of the variance process means that variance spikes (large upward moves in $V_t$) are more common than variance troughs (large downward moves) relative to a symmetric model. This is consistent with the empirical observation that realized volatility has a long right tail -- extreme volatility spikes during market crises are much more dramatic than periods of unusually low volatility.
