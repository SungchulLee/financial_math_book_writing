# Mean Reversion and Long-Run Variance

Mean reversion is the defining qualitative feature of the CIR variance process: regardless of its current level, the variance is continually pulled toward the long-run target $\theta$. After a volatility spike (such as a market crash), the variance does not stay elevated indefinitely but gradually decays back to its equilibrium level. The speed of this decay, controlled by $\kappa$, determines how persistent volatility shocks are and has direct implications for the term structure of implied volatility, the pricing of long-dated options, and the behavior of variance swaps.

This section analyzes the mean-reversion mechanism in detail: the half-life of variance shocks, the deterministic skeleton of the CIR process, the term structure of expected variance and implied volatility, and the important distinction between physical and risk-neutral mean-reversion parameters. We build on the [moment formulas](variance_process_moments.md) derived in the preceding section.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Compute the half-life of variance shocks and interpret it in calendar time
    - Describe the term structure of expected variance and its dependence on $\kappa$ and $\theta$
    - Explain how mean reversion shapes the term structure of implied volatility
    - Distinguish between physical-measure and risk-neutral-measure mean-reversion parameters
    - Relate the mean-reversion speed to the autocorrelation function of the variance process

---

## The Mean-Reversion Mechanism

### The Deterministic Skeleton

To understand mean reversion, first consider the CIR process without noise ($\sigma_v = 0$):

$$
\frac{dv}{dt} = \kappa(\theta - v)
$$

This ordinary differential equation has the solution:

$$
v(t) = \theta + (v_0 - \theta)\,e^{-\kappa t}
$$

The solution is an exponential decay from $v_0$ toward $\theta$. If $v_0 > \theta$, the variance decreases; if $v_0 < \theta$, it increases. The rate of convergence is governed by $\kappa$.

### Interpretation of Parameters

!!! info "Definition: Mean-Reversion Speed and Long-Run Variance"
    In the CIR variance process $dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t$:

    - **$\kappa > 0$** is the **mean-reversion speed**. It controls how quickly the variance reverts to its long-run level. Units: $[\text{time}]^{-1}$ (typically annualized).
    - **$\theta > 0$** is the **long-run variance** (or long-run mean). It is the level toward which the variance is pulled and the mean of the stationary distribution.

The drift at any point $v$ is $\kappa(\theta - v)$:

- When $v > \theta$: drift is negative (variance pushed downward)
- When $v < \theta$: drift is positive (variance pushed upward)
- When $v = \theta$: drift is zero (equilibrium)

The magnitude of the drift is proportional to the distance $|v - \theta|$ and to $\kappa$, creating a restoring force analogous to a spring.

---

## Half-Life of Variance Shocks

### Definition and Formula

!!! success "Proposition: Half-Life"
    The **half-life** of a variance shock is the time required for the expected deviation from $\theta$ to decay to half its initial value:

    $$
    t_{1/2} = \frac{\ln 2}{\kappa}
    $$

**Proof.** The conditional mean satisfies $\mathbb{E}[v_T | v_t] - \theta = (v_t - \theta)e^{-\kappa\tau}$. Setting $e^{-\kappa\tau} = 1/2$ gives $\tau = \ln 2 / \kappa$. $\square$

### Numerical Examples

| $\kappa$ | Half-life | Interpretation |
|:---:|:---:|:---|
| $0.5$ | 1.39 years | Very slow reversion; shocks persist for over a year |
| $1.0$ | 0.69 years | Moderate reversion; shocks halve in about 8 months |
| $2.0$ | 0.35 years | Typical calibrated value; shocks halve in about 4 months |
| $5.0$ | 0.14 years | Fast reversion; shocks halve in less than 2 months |
| $10.0$ | 0.07 years | Very fast reversion; shocks halve in about 3.5 weeks |

!!! tip "Practical Guidance"
    Equity index options (S&P 500) typically calibrate to $\kappa \approx 1$--$3$ under the risk-neutral measure, corresponding to half-lives of 3--8 months. This means a volatility spike (e.g., a VIX jump from 15 to 40) takes several months to decay halfway back to equilibrium -- consistent with empirical observations after market crises.

---

## Term Structure of Expected Variance

The conditional mean $\mathbb{E}[v_T | v_0] = \theta + (v_0 - \theta)e^{-\kappa\tau}$ defines the **term structure of expected variance**. This function of $\tau$ has distinct shapes depending on whether $v_0$ is above or below $\theta$.

### Cases

**Case 1: $v_0 > \theta$ (variance elevated).** The expected variance decreases from $v_0$ toward $\theta$. The term structure of expected volatility $\sigma(\tau) = \sqrt{\mathbb{E}[v_{t+\tau}|v_t]}$ is downward sloping. This corresponds to a **downward-sloping ATM volatility term structure** in the options market.

**Case 2: $v_0 < \theta$ (variance depressed).** The expected variance increases from $v_0$ toward $\theta$. The term structure is upward sloping. This corresponds to an **upward-sloping ATM volatility term structure**.

**Case 3: $v_0 = \theta$ (at equilibrium).** The expected variance is flat at $\theta$ for all maturities.

!!! note "ATM Volatility Term Structure"
    The ATM implied volatility for maturity $T$ in the Heston model is approximately:

    $$
    \sigma_{\text{ATM}}(T) \approx \sqrt{\frac{1}{T}\int_0^T \mathbb{E}[v_s | v_0]\,ds} = \sqrt{\frac{1}{T}\left[\theta T + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}\right]}
    $$

    This is the square root of the variance swap fair value. For short $T$, $\sigma_{\text{ATM}} \approx \sqrt{v_0}$. For long $T$, $\sigma_{\text{ATM}} \approx \sqrt{\theta}$. The transition between these two regimes is controlled by $\kappa$.

---

## Autocorrelation Function

The autocorrelation of the stationary variance process measures how persistent variance is over time.

!!! success "Proposition: Autocorrelation of the CIR Process"
    In the stationary regime, the autocorrelation function of $v_t$ is:

    $$
    \text{Corr}(v_t, v_{t+\tau}) = e^{-\kappa\tau}
    $$

**Proof.** In the stationary regime, $\text{Cov}(v_t, v_{t+\tau}) = \text{Var}(v_t)\,e^{-\kappa\tau}$. This follows from the conditional mean formula: $\mathbb{E}[v_{t+\tau}|v_t] = \theta + (v_t - \theta)e^{-\kappa\tau}$, so $\text{Cov}(v_t, v_{t+\tau}) = e^{-\kappa\tau}\,\text{Var}(v_t)$. Dividing by $\text{Var}(v_t)$ gives the autocorrelation. $\square$

The autocorrelation decays exponentially with lag $\tau$, confirming that $\kappa$ is the inverse of the characteristic persistence time. The integrated autocorrelation is $\int_0^\infty e^{-\kappa\tau}\,d\tau = 1/\kappa$, which is the **persistence time** of variance shocks.

---

## Physical vs. Risk-Neutral Mean Reversion

### The Volatility Risk Premium

A crucial distinction in the Heston framework is between parameters under the physical measure $\mathbb{P}$ (governing actual market dynamics) and the risk-neutral measure $\mathbb{Q}$ (governing option prices). The variance process dynamics differ under the two measures.

!!! info "Definition: Physical and Risk-Neutral CIR Parameters"
    Under the physical measure:

    $$
    dv_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^{\mathbb{P}}
    $$

    Under the risk-neutral measure:

    $$
    dv_t = \kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^{\mathbb{Q}}
    $$

    The relationship between the two sets of parameters is:

    $$
    \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda_v, \qquad \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda_v}
    $$

    where $\lambda_v$ is the **variance risk premium** parameter.

The vol-of-vol parameter $\sigma_v$ is the same under both measures (the Girsanov change of measure only affects the drift, not the diffusion).

### Implications

**$\lambda_v > 0$ (positive variance risk premium).** This is the empirically dominant case for equity indices. It means:

- $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$: variance mean-reverts faster under $\mathbb{Q}$
- $\theta^{\mathbb{Q}} < \theta^{\mathbb{P}}$: the risk-neutral long-run variance is lower
- The product $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$ is preserved

The preservation of $\kappa\theta$ ensures that the Feller condition ($2\kappa\theta \geq \sigma_v^2$) holds under $\mathbb{Q}$ if and only if it holds under $\mathbb{P}$.

!!! warning "Calibration Identifies Risk-Neutral Parameters"
    When calibrating the Heston model to option prices, the parameters $(\kappa, \theta, \sigma_v, \rho, v_0)$ obtained are the **risk-neutral** parameters $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}}, \sigma_v, \rho, v_0)$. These differ from the physical parameters that govern the actual time series of realized variance. Estimating the physical parameters requires fitting to historical variance data (e.g., realized volatility time series), not to option prices.

---

## Term Structure Regimes

The mean-reversion dynamics create distinct regimes in the variance term structure that have observable consequences in the options market.

??? example "Three Market Regimes"
    Consider $\theta = 0.04$ ($\sqrt{\theta} = 20\%$ volatility), $\kappa = 2.0$:

    **Calm market ($v_0 = 0.02$, $\sqrt{v_0} = 14\%$):**

    | Maturity $T$ | $\mathbb{E}[v_T|v_0]$ | $\sqrt{\mathbb{E}[v_T|v_0]}$ |
    |:---:|:---:|:---:|
    | 1 month | 0.0212 | 14.6% |
    | 3 months | 0.0249 | 15.8% |
    | 6 months | 0.0293 | 17.1% |
    | 1 year | 0.0347 | 18.6% |
    | 2 years | 0.0382 | 19.5% |

    Upward-sloping term structure: longer options are more expensive.

    **Stressed market ($v_0 = 0.09$, $\sqrt{v_0} = 30\%$):**

    | Maturity $T$ | $\mathbb{E}[v_T|v_0]$ | $\sqrt{\mathbb{E}[v_T|v_0]}$ |
    |:---:|:---:|:---:|
    | 1 month | 0.0858 | 29.3% |
    | 3 months | 0.0699 | 26.4% |
    | 6 months | 0.0559 | 23.6% |
    | 1 year | 0.0467 | 21.6% |
    | 2 years | 0.0418 | 20.5% |

    Downward-sloping term structure: shorter options are more expensive (the market expects volatility to decline).

    **Equilibrium ($v_0 = 0.04 = \theta$):** Flat term structure at all maturities.

---

## Persistence and Long Memory

!!! note "CIR vs. Rough Volatility"
    The CIR variance process has exponentially decaying autocorrelation $e^{-\kappa\tau}$, implying **short memory** (or **Markov property**). Empirical studies of realized volatility find that the autocorrelation decays much more slowly -- approximately as a power law $\tau^{2H-1}$ with $H \approx 0.1$ (the **rough volatility** phenomenon).

    This mismatch is one of the main limitations of the Heston model. The rough Heston model, discussed in the [extensions section](../extensions/rough_heston_overview.md), replaces the CIR process with a fractional kernel to match the empirical long-memory behavior. Within the standard Heston framework, the exponential autocorrelation means that long-maturity options depend almost entirely on $\theta$ (not on $v_0$), which is both a simplification and a limitation.

---

## Summary

Mean reversion is the mechanism by which the Heston variance process converges to its long-run level $\theta$. The speed $\kappa$ determines the half-life $\ln 2/\kappa$ of variance shocks and the exponential decay rate of the autocorrelation function. The term structure of expected variance transitions from $v_0$ (short term) to $\theta$ (long term), generating upward-sloping, flat, or downward-sloping implied volatility term structures depending on the current market regime. The distinction between physical and risk-neutral mean-reversion parameters, mediated by the variance risk premium $\lambda_v$, is essential for understanding why calibrated (risk-neutral) parameters differ from historically estimated (physical) parameters.

The [next section](correlation_and_leverage_effect.md) examines the correlation parameter $\rho$ and its role in generating the implied volatility skew through the leverage effect.

---
