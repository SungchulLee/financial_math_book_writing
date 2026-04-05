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

## Exercises

**Exercise 1.** Compute the half-life of mean reversion $t_{1/2} = \ln 2/\kappa$ for $\kappa = 1$ and $\kappa = 5$. In each case, how many trading days does it take for a variance shock to decay by 50%?

??? success "Solution to Exercise 1"
    The half-life is $t_{1/2} = \ln 2 / \kappa$.

    **Case 1: $\kappa = 1$.**

    $$
    t_{1/2} = \frac{\ln 2}{1} = 0.6931 \text{ years}
    $$

    Assuming 252 trading days per year: $0.6931 \times 252 \approx 175$ trading days, or roughly 8.3 calendar months. A variance shock takes about 175 trading days to decay by 50%.

    **Case 2: $\kappa = 5$.**

    $$
    t_{1/2} = \frac{\ln 2}{5} = 0.1386 \text{ years}
    $$

    In trading days: $0.1386 \times 252 \approx 35$ trading days, or roughly 1.7 calendar months. The variance shock decays by 50% in about 7 weeks.

    The five-fold increase in $\kappa$ produces a five-fold decrease in half-life. With $\kappa = 1$, volatility shocks persist for the better part of a year, consistent with the slow decay observed after major market crises. With $\kappa = 5$, shocks dissipate in under two months, which would be appropriate for markets where volatility reverts quickly.

---

**Exercise 2.** For $\kappa = 2$, $\theta = 0.04$, and $V_0 = 0.09$ (post-crash elevated variance), compute $\mathbb{E}[V_t]$ at $t = 0.25, 0.5, 1, 2$ years. Plot or sketch the mean-reversion trajectory.

??? success "Solution to Exercise 2"
    Using $\kappa = 2$, $\theta = 0.04$, and $V_0 = 0.09$:

    $$
    \mathbb{E}[V_t] = \theta + (V_0 - \theta)e^{-\kappa t} = 0.04 + 0.05\,e^{-2t}
    $$

    Computing at each time point:

    **At $t = 0.25$ years:**

    $$
    \mathbb{E}[V_{0.25}] = 0.04 + 0.05\,e^{-0.5} = 0.04 + 0.05 \times 0.6065 = 0.04 + 0.03033 = 0.07033
    $$

    **At $t = 0.5$ years:**

    $$
    \mathbb{E}[V_{0.5}] = 0.04 + 0.05\,e^{-1.0} = 0.04 + 0.05 \times 0.3679 = 0.04 + 0.01839 = 0.05839
    $$

    **At $t = 1$ year:**

    $$
    \mathbb{E}[V_1] = 0.04 + 0.05\,e^{-2.0} = 0.04 + 0.05 \times 0.1353 = 0.04 + 0.00677 = 0.04677
    $$

    **At $t = 2$ years:**

    $$
    \mathbb{E}[V_2] = 0.04 + 0.05\,e^{-4.0} = 0.04 + 0.05 \times 0.01832 = 0.04 + 0.000916 = 0.04092
    $$

    | $t$ (years) | $\mathbb{E}[V_t]$ | $\sqrt{\mathbb{E}[V_t]}$ (vol) |
    |:---:|:---:|:---:|
    | $0$ | $0.0900$ | $30.0\%$ |
    | $0.25$ | $0.0703$ | $26.5\%$ |
    | $0.50$ | $0.0584$ | $24.2\%$ |
    | $1.00$ | $0.0468$ | $21.6\%$ |
    | $2.00$ | $0.0409$ | $20.2\%$ |
    | $\infty$ | $0.0400$ | $20.0\%$ |

    The trajectory shows the expected variance decaying monotonically from $V_0 = 0.09$ (30% volatility) toward $\theta = 0.04$ (20% volatility). The half-life is $\ln 2 / 2 \approx 0.35$ years, and by $t = 2$ years the variance is within 2.3% of its long-run level.

---

**Exercise 3.** The term structure of implied variance for an ATM option is approximately $\mathbb{E}[\bar{V}_{0,T}] = \theta + (V_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}$. Compute this for $T = 0.1, 0.5, 1, 5$ years with $\kappa = 2$, $\theta = 0.04$, $V_0 = 0.06$. Is the term structure upward-sloping or downward-sloping?

??? success "Solution to Exercise 3"
    The term structure of expected average variance (variance swap fair strike) is:

    $$
    \mathbb{E}[\bar{V}_{0,T}] = \theta + (V_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    With $\kappa = 2$, $\theta = 0.04$, $V_0 = 0.06$:

    **At $T = 0.1$ years:**

    $$
    \mathbb{E}[\bar{V}_{0,0.1}] = 0.04 + 0.02 \times \frac{1 - e^{-0.2}}{0.2} = 0.04 + 0.02 \times \frac{0.1813}{0.2} = 0.04 + 0.02 \times 0.9063 = 0.05813
    $$

    **At $T = 0.5$ years:**

    $$
    \mathbb{E}[\bar{V}_{0,0.5}] = 0.04 + 0.02 \times \frac{1 - e^{-1.0}}{1.0} = 0.04 + 0.02 \times 0.6321 = 0.05264
    $$

    **At $T = 1$ year:**

    $$
    \mathbb{E}[\bar{V}_{0,1}] = 0.04 + 0.02 \times \frac{1 - e^{-2.0}}{2.0} = 0.04 + 0.02 \times \frac{0.8647}{2.0} = 0.04 + 0.02 \times 0.4323 = 0.04865
    $$

    **At $T = 5$ years:**

    $$
    \mathbb{E}[\bar{V}_{0,5}] = 0.04 + 0.02 \times \frac{1 - e^{-10}}{10} = 0.04 + 0.02 \times \frac{0.99995}{10} = 0.04 + 0.02 \times 0.09999 = 0.04200
    $$

    | $T$ | $\mathbb{E}[\bar{V}_{0,T}]$ | $\sqrt{\mathbb{E}[\bar{V}_{0,T}]}$ (vol) |
    |:---:|:---:|:---:|
    | $0.1$ | $0.05813$ | $24.1\%$ |
    | $0.5$ | $0.05264$ | $22.9\%$ |
    | $1.0$ | $0.04865$ | $22.1\%$ |
    | $5.0$ | $0.04200$ | $20.5\%$ |

    The term structure is **downward-sloping** because $V_0 = 0.06 > \theta = 0.04$. The current variance is elevated above its long-run level, so shorter-maturity variance swaps have higher fair strikes than longer-maturity ones. As $T \to \infty$, $\mathbb{E}[\bar{V}_{0,T}] \to \theta = 0.04$, corresponding to a 20% implied volatility level.

---

**Exercise 4.** Explain why a higher $\kappa$ produces a flatter implied volatility term structure: the variance converges to $\theta$ faster, so the effect of the current $V_0$ dissipates quickly for longer maturities.

??? success "Solution to Exercise 4"
    A higher $\kappa$ means the variance process reverts to $\theta$ more quickly. The formula for the expected average variance is:

    $$
    \mathbb{E}[\bar{V}_{0,T}] = \theta + (V_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    The key factor is $g(\kappa, T) = \frac{1 - e^{-\kappa T}}{\kappa T}$, which measures how much the current variance $V_0$ influences the average variance over $[0, T]$.

    For large $\kappa$: the exponential $e^{-\kappa T}$ decays rapidly, so $g(\kappa, T) \approx 1/(\kappa T)$ for moderate $T$. The contribution of $(V_0 - \theta)$ to the average variance shrinks as $1/(\kappa T)$. This means that even for short maturities, the expected average variance is close to $\theta$.

    For small $\kappa$: the exponential decays slowly, so $g(\kappa, T) \approx 1 - \kappa T/2$ for small $T$. The current variance $V_0$ dominates the average for a long period.

    **The resulting term structure:** When $\kappa$ is large, the transition from $V_0$ to $\theta$ happens quickly. Even short-maturity options "see" a variance close to $\theta$, so the term structure is nearly flat at $\sqrt{\theta}$ for all but the very shortest maturities. When $\kappa$ is small, the transition is slow, and the term structure exhibits a pronounced slope from $\sqrt{V_0}$ (short end) to $\sqrt{\theta}$ (long end).

    In the options market, a flat implied volatility term structure signals that the market expects current volatility conditions to persist (or equivalently, that mean reversion is fast enough that the current state is already at equilibrium). A steep term structure signals that the current volatility differs substantially from its long-run level and that mean reversion is slow enough for this difference to matter across maturities.

---

**Exercise 5.** The variance risk premium $\lambda_v$ causes the risk-neutral $\kappa^{\mathbb{Q}}$ to differ from the physical $\kappa^{\mathbb{P}}$. If $\kappa^{\mathbb{P}} = 3$ and $\lambda_v = -1.5$ (investors dislike variance risk), what is $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda_v$? Is mean reversion faster or slower under the risk-neutral measure?

??? success "Solution to Exercise 5"
    With $\kappa^{\mathbb{P}} = 3$ and $\lambda_v = -1.5$:

    $$
    \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda_v = 3 + (-1.5) = 1.5
    $$

    Mean reversion is **slower** under the risk-neutral measure ($\kappa^{\mathbb{Q}} = 1.5 < 3 = \kappa^{\mathbb{P}}$).

    **Interpretation:** A negative $\lambda_v$ means investors are willing to pay a premium to hedge against variance risk. In the risk-neutral world (the world consistent with option prices), variance shocks are more persistent than they are in reality. This makes options appear more expensive than a physical-measure model would suggest, reflecting the **variance risk premium**.

    The half-life under each measure is:

    $$
    t_{1/2}^{\mathbb{P}} = \frac{\ln 2}{3} = 0.231 \text{ years} \approx 2.8 \text{ months}
    $$

    $$
    t_{1/2}^{\mathbb{Q}} = \frac{\ln 2}{1.5} = 0.462 \text{ years} \approx 5.5 \text{ months}
    $$

    Under the risk-neutral measure, variance shocks take twice as long to decay, which inflates the prices of long-dated options relative to what the physical-measure dynamics would predict.

    Note that the risk-neutral long-run variance is:

    $$
    \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{Q}}} = \frac{3\,\theta^{\mathbb{P}}}{1.5} = 2\,\theta^{\mathbb{P}}
    $$

    So $\theta^{\mathbb{Q}} > \theta^{\mathbb{P}}$: the risk-neutral long-run variance is higher, further reflecting the premium investors demand for bearing variance risk.

---

**Exercise 6.** The autocorrelation function of $V_t$ in stationarity is $\operatorname{Corr}(V_t, V_{t+h}) = e^{-\kappa h}$. For $\kappa = 2$, compute the autocorrelation at lags of 1 day, 1 week, 1 month, and 1 year. At what lag does the correlation drop below 0.1?

??? success "Solution to Exercise 6"
    For $\kappa = 2$, the autocorrelation function is $\operatorname{Corr}(V_t, V_{t+h}) = e^{-2h}$, where $h$ is measured in years.

    Using the convention: 1 day $= 1/252$ years, 1 week $= 5/252$ years, 1 month $= 21/252$ years.

    **Lag of 1 day ($h = 1/252 = 0.003968$):**

    $$
    e^{-2 \times 0.003968} = e^{-0.007937} = 0.9921
    $$

    **Lag of 1 week ($h = 5/252 = 0.01984$):**

    $$
    e^{-2 \times 0.01984} = e^{-0.03968} = 0.9611
    $$

    **Lag of 1 month ($h = 21/252 = 0.08333$):**

    $$
    e^{-2 \times 0.08333} = e^{-0.1667} = 0.8465
    $$

    **Lag of 1 year ($h = 1$):**

    $$
    e^{-2 \times 1} = e^{-2} = 0.1353
    $$

    | Lag | $h$ (years) | Autocorrelation |
    |:---|:---:|:---:|
    | 1 day | $0.00397$ | $0.9921$ |
    | 1 week | $0.01984$ | $0.9611$ |
    | 1 month | $0.08333$ | $0.8465$ |
    | 1 year | $1.0$ | $0.1353$ |

    **When does correlation drop below 0.1?** We solve $e^{-2h} = 0.1$:

    $$
    -2h = \ln(0.1) = -2.3026 \implies h = \frac{2.3026}{2} = 1.1513 \text{ years}
    $$

    This is approximately $1.1513 \times 252 \approx 290$ trading days, or about 13.8 months. After roughly 14 months, the variance process has essentially "forgotten" its current state and is driven primarily by the stationary distribution around $\theta$.
