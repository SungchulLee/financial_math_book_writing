# Variance Swaps Under Heston (Closed-Form)

## Introduction

A **variance swap** is a forward contract on realized variance. The buyer pays a fixed variance strike $K_{\text{var}}$ at maturity and receives the realized variance of the underlying asset over the contract period. Variance swaps are among the most liquid volatility derivatives and serve as fundamental building blocks for volatility trading, hedging, and the construction of the VIX index.

The Heston model provides one of the cleanest settings for variance swap pricing because the expected integrated variance $\mathbb{E}^{\mathbb{Q}}\!\left[\frac{1}{T}\int_0^T v_t \, dt\right]$ can be computed **in closed form** directly from the CIR dynamics of the variance process. No Fourier inversion or numerical integration is required --- the result follows from a simple ODE. This section derives the fair variance strike, discusses the connection to the replication formula via log contracts, and addresses the correction needed when monitoring is discrete rather than continuous.

!!! info "Prerequisites"

    - [Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md) (the bivariate SDE)
    - [CIR Variance Process Solution](../variance_dynamics/cir_variance_process_solution.md) (moments of $v_t$)
    - [Mean Reversion and Long-Run Variance](../variance_dynamics/mean_reversion_and_long_run.md) (properties of $v_t$)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define variance swaps and state the fair strike condition
    2. Derive the closed-form expected integrated variance under the Heston model
    3. Compute the fair variance strike for given Heston parameters
    4. Apply the discrete monitoring correction for market-standard variance swaps
    5. Connect the variance swap strike to the log-contract replication formula

---

## Variance Swap Definition

### Contract Structure

A variance swap with maturity $T$ and notional $N_{\text{var}}$ has payoff at maturity:

$$
N_{\text{var}} \left(\sigma_R^2 - K_{\text{var}}\right)
$$

where $\sigma_R^2$ is the annualized **realized variance** and $K_{\text{var}}$ is the **variance strike** (fixed at inception). The realized variance is defined as:

$$
\sigma_R^2 = \frac{252}{n} \sum_{i=1}^{n} \left(\ln \frac{S_{t_i}}{S_{t_{i-1}}}\right)^2
$$

for daily monitoring with $n$ business days and dates $t_0 < t_1 < \cdots < t_n = T$. The factor 252 annualizes the variance. Some contracts use $n - 1$ in the denominator (sample variance convention) or subtract the mean return (demeaned variance), but the zero-mean convention above is standard for equity variance swaps.

### Fair Strike

The variance swap is a zero-cost contract at inception, so the **fair variance strike** is:

$$
K_{\text{var}} = \mathbb{E}^{\mathbb{Q}}[\sigma_R^2]
$$

In the continuous-monitoring limit ($n \to \infty$, $\Delta t \to 0$), the realized variance converges to the **quadratic variation** of the log-price:

$$
\sigma_R^2 \to \frac{1}{T} \langle \ln S \rangle_T = \frac{1}{T} \int_0^T v_t \, dt
$$

where the last equality follows from $d\ln S_t = (r - q - v_t/2)\,dt + \sqrt{v_t}\,dW_t^{(1)}$, so $\langle \ln S \rangle_T = \int_0^T v_t \, dt$.

---

## Closed-Form Fair Strike

### Deriving the Expected Integrated Variance

Recall (see [§ Variance Dynamics](../variance_dynamics/cir_variance_process_solution.md)): $\mathbb{E}^{\mathbb{Q}}[v_t \mid v_0] = \theta + (v_0 - \theta)e^{-\kappa t}$. Integrating over $[0, T]$:

$$
\mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T v_t \, dt \,\Big|\, v_0\right] = \theta T + (v_0 - \theta) \frac{1 - e^{-\kappa T}}{\kappa}
$$

!!! note "Theorem (Fair Variance Strike Under Heston)"
    The continuously monitored fair variance strike under the Heston model is:

    $$
    K_{\text{var}} = \theta + (v_0 - \theta) \frac{1 - e^{-\kappa T}}{\kappa T}
    $$

??? example "Proof"
    Starting from $\mathbb{E}^{\mathbb{Q}}[v_t] = \theta + (v_0 - \theta)e^{-\kappa t}$, integrate:

    $$
    K_{\text{var}} = \frac{1}{T}\mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T v_t \, dt\right] = \frac{1}{T}\left[\theta T + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}\right]
    $$

    $$
    = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    The exchange of expectation and integration is justified by Fubini's theorem, since $\mathbb{E}[\int_0^T |v_t| \, dt] < \infty$ for any CIR process with positive parameters. $\square$

### Limiting Cases

The fair strike has intuitive behavior in several limits:

**Short maturity** ($T \to 0$): Taylor expansion of $e^{-\kappa T} \approx 1 - \kappa T + \frac{1}{2}\kappa^2 T^2$ gives:

$$
K_{\text{var}} \approx v_0 - \frac{1}{2}\kappa(v_0 - \theta)T + \mathcal{O}(T^2)
$$

The fair strike starts at the **current variance** $v_0$ and moves toward $\theta$ at rate $\kappa$.

**Long maturity** ($T \to \infty$): The exponential term vanishes, and:

$$
K_{\text{var}} \to \theta
$$

For long-dated variance swaps, the fair strike converges to the **long-run variance**.

**No mean reversion** ($\kappa \to 0$): Using L'Hopital's rule, $\frac{1 - e^{-\kappa T}}{\kappa T} \to 1$, so:

$$
K_{\text{var}} \to v_0
$$

Without mean reversion, the variance process drifts without returning to $\theta$, and the expected average equals the initial variance.

!!! tip "Term Structure of Variance"
    The function $T \mapsto K_{\text{var}}(T)$ defines the **term structure of fair variance**, analogous to the forward rate curve in interest rate models. If $v_0 < \theta$, the curve slopes upward (contango); if $v_0 > \theta$, it slopes downward (backwardation). Calibrating Heston to variance swap term structures directly identifies $v_0$, $\kappa$, and $\theta$.

---

## Variance of Integrated Variance

The fair strike gives the expected value, but the **variance** of $\frac{1}{T}\int_0^T v_t \, dt$ determines the risk of a variance swap position.

!!! note "Theorem (Variance of Integrated Variance)"
    Under the Heston model:

    $$
    \operatorname{Var}\!\left[\frac{1}{T}\int_0^T v_t \, dt\right] = \frac{\xi^2}{\kappa^2 T^2}\left[\theta T + (v_0 - \theta)\frac{2(1 - e^{-\kappa T})}{\kappa} - \frac{v_0 + \theta}{2\kappa}(1 - e^{-\kappa T})^2 - \theta T \frac{1 - e^{-2\kappa T}}{2\kappa T}\right]
$$

??? example "Proof sketch"
    Compute $\mathbb{E}[(\int_0^T v_t \, dt)^2]$ by writing it as $\int_0^T \int_0^T \mathbb{E}[v_s v_t] \, ds \, dt$. The covariance $\operatorname{Cov}(v_s, v_t)$ for the CIR process is known in closed form:

    $$
    \operatorname{Cov}(v_s, v_t) = \frac{\xi^2}{\kappa}\left[\frac{\theta}{2}(e^{-\kappa|t-s|} - e^{-\kappa(t+s)}) + v_0 e^{-\kappa(t+s)}\frac{e^{\kappa \min(s,t)} - 1}{\kappa}\right]
    $$

    for $0 \leq s, t \leq T$. The double integral is then evaluated by splitting into regions $s < t$ and $s > t$ and using standard exponential integrals. $\square$

The variance of integrated variance scales as $\xi^2 / \kappa$ for large $T$, confirming that vol-of-vol $\xi$ and mean-reversion speed $\kappa$ jointly control the dispersion of realized variance around its expected value.

---

## Discrete Monitoring Correction

### The Discretization Effect

Market-standard variance swaps use daily discrete monitoring, not continuous. The discretely monitored realized variance is:

$$
\sigma_{R,n}^2 = \frac{252}{n} \sum_{i=1}^{n} \left(\ln \frac{S_{t_i}}{S_{t_{i-1}}}\right)^2
$$

The difference between continuous and discrete fair strikes arises because:

$$
\left(\ln \frac{S_{t_i}}{S_{t_{i-1}}}\right)^2 = \int_{t_{i-1}}^{t_i} v_t \, dt + \text{higher-order terms}
$$

The leading correction involves the **convexity** of the log-return squared with respect to the integrated variance over each interval.

### Correction Formula

!!! note "Theorem (Discrete Monitoring Correction)"
    The fair strike for a discretely monitored variance swap under Heston is:

    $$
    K_{\text{var}}^{\text{discrete}} = K_{\text{var}}^{\text{cont}} + \frac{1}{T}\sum_{i=1}^{n} \operatorname{Var}\!\left[\int_{t_{i-1}}^{t_i} v_t \, dt \, \Big| \, v_{t_{i-1}}\right] \cdot \frac{1}{\Delta t_i} + \mathcal{O}(\Delta t^2)
    $$

    For equally spaced dates with $\Delta t = T/n$, the correction simplifies to:

    $$
    K_{\text{var}}^{\text{discrete}} \approx K_{\text{var}}^{\text{cont}} + \frac{\xi^2}{12\kappa}\left(2\theta + \frac{4(v_0 - \theta)}{n} \cdot \frac{1 - e^{-\kappa T}}{1 - e^{-\kappa \Delta t}}\right) \Delta t
    $$

For daily monitoring ($\Delta t \approx 1/252$), this correction is typically less than 0.1% of the fair strike, but it becomes material for weekly or monthly monitoring.

---

## Connection to Log-Contract Replication

### The Model-Free Formula

A fundamental result in variance swap theory is the **model-free replication** formula:

$$
\mathbb{E}^{\mathbb{Q}}[\sigma_R^2] = -\frac{2}{T}\mathbb{E}^{\mathbb{Q}}\!\left[\ln \frac{S_T}{S_0} - \left(\frac{S_T}{S_0} - 1\right)\right]
$$

This expresses the fair variance strike as the price of a **log contract** plus a forward contract. The log contract can be replicated using a continuum of out-of-the-money puts and calls:

$$
-\ln \frac{S_T}{F} = \int_0^F \frac{1}{K^2}(K - S_T)^+ \, dK + \int_F^{\infty} \frac{1}{K^2}(S_T - K)^+ \, dK - \left(\frac{S_T}{F} - 1\right)
$$

where $F = S_0 e^{(r-q)T}$ is the forward price.

### Heston-Specific Consistency

Under Heston, the model-free formula must agree with the closed-form result:

$$
-\frac{2}{T}\mathbb{E}^{\mathbb{Q}}\!\left[\ln \frac{S_T}{S_0}\right] + \frac{2(r-q)}{1} = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
$$

This consistency provides a useful **calibration check**: if Heston option prices are used to compute the replicating portfolio of OTM puts and calls, the resulting variance strike should match the closed-form expression. Any discrepancy indicates either calibration error or numerical inaccuracy in the replication.

!!! warning "Truncation in Practice"
    The integral over strikes extends from $0$ to $\infty$, but in practice it is truncated to the range of available liquid options. This truncation introduces a bias that is model-dependent. Under Heston, the heavy-tailed implied volatility smile means the truncation bias is larger than under Black--Scholes, particularly in the deep OTM put region.

---

## Worked Example

### Parameters

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Initial variance | $v_0$ | 0.04 (20% vol) |
| Mean reversion | $\kappa$ | 1.5 |
| Long-run variance | $\theta$ | 0.06 (24.5% vol) |
| Vol-of-vol | $\xi$ | 0.4 |
| Correlation | $\rho$ | $-0.7$ |

### Fair Strikes by Maturity

| Maturity $T$ | $K_{\text{var}}$ | $\sqrt{K_{\text{var}}}$ (vol) | Interpretation |
|:---:|:---:|:---:|---|
| 1 month | 0.0419 | 20.5% | Near $v_0$; little mean reversion |
| 3 months | 0.0456 | 21.4% | Moving toward $\theta$ |
| 6 months | 0.0498 | 22.3% | Halfway between $v_0$ and $\theta$ |
| 1 year | 0.0540 | 23.2% | Approaching $\theta$ |
| 2 years | 0.0573 | 23.9% | Close to $\theta$ |
| 5 years | 0.0596 | 24.4% | Nearly at $\theta = 0.06$ |

!!! example "Observation"
    Since $v_0 = 0.04 < \theta = 0.06$, the term structure of fair variance is **upward-sloping** (contango). The 1-month strike is close to $v_0$ because mean reversion has not had time to act. The 5-year strike is within 1% of $\theta$ because $e^{-\kappa \cdot 5} = e^{-7.5} \approx 0.0006$, making the exponential correction negligible.

### Sensitivity to Parameters

The fair strike depends on only three Heston parameters: $v_0$, $\kappa$, and $\theta$. It is **independent** of $\xi$ (vol-of-vol) and $\rho$ (correlation). This is because the expected value of the CIR process depends only on the drift parameters, not the diffusion coefficient. However, the **variance** of realized variance (and hence the P&L risk of a variance swap position) does depend on $\xi$.

---

## Summary

| Concept | Formula |
|---------|---------|
| Continuously monitored fair strike | $K_{\text{var}} = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}$ |
| Short maturity limit | $K_{\text{var}} \approx v_0$ |
| Long maturity limit | $K_{\text{var}} \to \theta$ |
| Model-free replication | $K_{\text{var}} = -\frac{2}{T}\mathbb{E}[\ln(S_T/S_0)] + \frac{2(r-q)T}{T}$ |
| Parameter dependence | $v_0, \kappa, \theta$ only (not $\xi, \rho$) |

!!! abstract "Key Takeaways"

    1. **Closed-form pricing**: The Heston fair variance strike has an explicit formula involving only $v_0$, $\kappa$, $\theta$, and $T$. No Fourier inversion is needed.

    2. **Term structure**: The fair strike interpolates between $v_0$ (short maturity) and $\theta$ (long maturity), with the mean-reversion speed $\kappa$ controlling the interpolation rate.

    3. **Independence from vol-of-vol**: The fair strike is independent of $\xi$ and $\rho$, though the P&L risk of a variance swap position depends on $\xi$.

    4. **Discrete monitoring correction**: Market-standard daily monitoring introduces a small correction proportional to $\xi^2 \Delta t / \kappa$.

    5. **Model-free connection**: The variance swap strike equals the price of a log contract, which can be replicated using a strip of OTM options. Under Heston, this provides a consistency check for calibration.

---

## What's Next

| Section | Topic |
|---------|-------|
| [VIX Options Under Heston](vix_options_under_heston.md) | Pricing VIX options using the affine structure |
| [Forward-Start Options](forward_start_options.md) | Conditional characteristic function methods |
| [Asian Options (Monte Carlo)](asian_options_monte_carlo.md) | MC pricing of averaging derivatives |

---

## Exercises

**Exercise 1.**
For Heston parameters $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.05$, compute the fair variance strike $K_{\text{var}}$ for a 1-year variance swap using the formula:

$$
K_{\text{var}} = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
$$

Convert the result to a volatility strike $K_{\text{vol}} = \sqrt{K_{\text{var}}}$ and express in percentage. Does the variance strike lie between $v_0$ and $\theta$?

??? success "Solution to Exercise 1"
    **Computing the fair variance strike.** With $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.05$, $T = 1$:

    $$
    K_{\text{var}} = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    **Step 1.** Compute $e^{-\kappa T} = e^{-2.0} = 0.13534$.

    **Step 2.** Compute the fraction:

    $$
    \frac{1 - e^{-\kappa T}}{\kappa T} = \frac{1 - 0.13534}{2.0 \times 1.0} = \frac{0.86466}{2.0} = 0.43233
    $$

    **Step 3.** Compute the fair strike:

    $$
    K_{\text{var}} = 0.05 + (0.04 - 0.05) \times 0.43233 = 0.05 + (-0.01) \times 0.43233 = 0.05 - 0.004323 = 0.04568
    $$

    **Step 4.** Convert to volatility strike:

    $$
    K_{\text{vol}} = \sqrt{K_{\text{var}}} = \sqrt{0.04568} = 0.2137 = 21.37\%
    $$

    **Verification.** Since $v_0 = 0.04 < \theta = 0.05$, mean reversion pulls the expected variance upward. The fair strike $K_{\text{var}} = 0.04568$ lies between $v_0 = 0.04$ and $\theta = 0.05$, as expected. Specifically:

    $$
    v_0 = 0.04 < K_{\text{var}} = 0.04568 < \theta = 0.05 \quad \checkmark
    $$

    The fair strike is closer to $\theta$ than to $v_0$ because the averaging factor $0.43233$ gives substantial weight to the mean-reversion target over a 1-year horizon.

---

**Exercise 2.**
Show that as $T \to 0$, the fair variance strike $K_{\text{var}} \to v_0$, and as $T \to \infty$, $K_{\text{var}} \to \theta$. Derive these limits from the formula. Compute $K_{\text{var}}$ for $T = 0.01, 0.1, 1, 5, 20$ years using the parameters from Exercise 1 and verify the convergence to $\theta$.

??? success "Solution to Exercise 2"
    **Short maturity limit ($T \to 0$).** Using the Taylor expansion $e^{-\kappa T} \approx 1 - \kappa T + \frac{1}{2}\kappa^2 T^2 - \cdots$:

    $$
    \frac{1 - e^{-\kappa T}}{\kappa T} = \frac{1 - (1 - \kappa T + \frac{1}{2}\kappa^2 T^2 - \cdots)}{\kappa T} = \frac{\kappa T - \frac{1}{2}\kappa^2 T^2 + \cdots}{\kappa T} = 1 - \frac{\kappa T}{2} + \cdots
    $$

    Therefore:

    $$
    K_{\text{var}} = \theta + (v_0 - \theta)(1 - \frac{\kappa T}{2} + \cdots) \to \theta + (v_0 - \theta) = v_0 \quad \text{as } T \to 0
    $$

    **Long maturity limit ($T \to \infty$).** As $T \to \infty$, $e^{-\kappa T} \to 0$, so:

    $$
    \frac{1 - e^{-\kappa T}}{\kappa T} \to \frac{1}{\kappa T} \to 0
    $$

    Therefore:

    $$
    K_{\text{var}} = \theta + (v_0 - \theta) \cdot \frac{1}{\kappa T} \to \theta \quad \text{as } T \to \infty
    $$

    **Numerical verification.** Using $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.05$:

    | $T$ | $e^{-\kappa T}$ | $\frac{1-e^{-\kappa T}}{\kappa T}$ | $K_{\text{var}}$ | $\sqrt{K_{\text{var}}}$ |
    |:---:|:---:|:---:|:---:|:---:|
    | 0.01 | 0.9802 | 0.9901 | 0.04010 | 20.02% |
    | 0.1 | 0.8187 | 0.9063 | 0.04094 | 20.23% |
    | 1.0 | 0.1353 | 0.4323 | 0.04568 | 21.37% |
    | 5.0 | 0.0000454 | 0.1000 | 0.04900 | 22.14% |
    | 20.0 | $\approx 0$ | 0.0250 | 0.04975 | 22.31% |

    The convergence to $\theta = 0.05$ ($\sqrt{\theta} = 22.36\%$) is clearly visible. At $T = 0.01$, the fair strike is within 0.25% of $v_0$. At $T = 20$, it is within 0.5% of $\theta$.

---

**Exercise 3.**
The continuous-monitoring fair variance strike differs from the discrete-monitoring version by a convexity correction. The discrete-monitoring realized variance uses squared log-returns $(\ln S_{t_i}/S_{t_{i-1}})^2$, while the continuous version uses $\int_0^T v_t \, dt / T$. The correction is approximately $K_{\text{var}}^{\text{discrete}} \approx K_{\text{var}}^{\text{cont}} + \frac{1}{3n}(\bar{v}\xi^2/\kappa)$ where $n$ is the number of monitoring dates. For daily monitoring ($n = 252$), $\kappa = 2.0$, $\xi = 0.5$, and $\bar{v} = 0.045$, compute the correction and compare it to the continuous strike.

??? success "Solution to Exercise 3"
    **Discrete monitoring correction.** The approximate correction formula is:

    $$
    K_{\text{var}}^{\text{discrete}} \approx K_{\text{var}}^{\text{cont}} + \frac{1}{3n} \cdot \frac{\bar{v}\xi^2}{\kappa}
    $$

    with $n = 252$ (daily monitoring), $\kappa = 2.0$, $\xi = 0.5$, $\bar{v} = 0.045$.

    **Step 1.** Compute the correction:

    $$
    \text{Correction} = \frac{1}{3 \times 252} \cdot \frac{0.045 \times 0.5^2}{2.0} = \frac{1}{756} \times \frac{0.045 \times 0.25}{2.0}
    $$

    $$
    = \frac{1}{756} \times \frac{0.01125}{2.0} = \frac{1}{756} \times 0.005625 = 0.000007440
    $$

    **Step 2.** Compare to the continuous strike. From Exercise 1, $K_{\text{var}}^{\text{cont}} = 0.04568$. The correction as a percentage of the continuous strike:

    $$
    \frac{0.000007440}{0.04568} = 0.0163\% \approx 0.016\%
    $$

    This is extremely small --- less than 2 basis points of the fair strike. The discrete strike is:

    $$
    K_{\text{var}}^{\text{discrete}} \approx 0.04568 + 0.0000074 = 0.04569
    $$

    The correction is negligible for daily monitoring. However, for weekly monitoring ($n = 52$):

    $$
    \text{Correction}_{\text{weekly}} = \frac{1}{3 \times 52} \times 0.005625 = \frac{0.005625}{156} = 0.0000361
    $$

    This is about 0.08% of the fair strike, still small but potentially material for large notionals. For monthly monitoring ($n = 12$):

    $$
    \text{Correction}_{\text{monthly}} = \frac{1}{36} \times 0.005625 = 0.000156
    $$

    This is 0.34% of the fair strike, which is relevant for pricing.

---

**Exercise 4.**
The VIX index is defined as $\text{VIX}_t = 100\sqrt{K_{\text{var}}(t, t + \tau)}$ where $\tau = 30/365$ and $K_{\text{var}}$ is the fair 30-day variance swap strike. For $v_t = 0.04$, $\kappa = 2.0$, $\theta = 0.05$, compute VIX$_t$. How does VIX change if $v_t$ suddenly increases to 0.09 (a volatility spike)?

??? success "Solution to Exercise 4"
    **Computing VIX under Heston.** The VIX is defined as:

    $$
    \text{VIX}_t = 100\sqrt{K_{\text{var}}(t, t + \tau)}
    $$

    where $\tau = 30/365$ and the 30-day fair variance strike is:

    $$
    K_{\text{var}}(t, t+\tau) = \theta + (v_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa\tau}
    $$

    **Case 1: $v_t = 0.04$.** Compute $\kappa\tau = 2.0 \times 30/365 = 0.16438$.

    $$
    e^{-\kappa\tau} = e^{-0.16438} = 0.8484
    $$

    $$
    \frac{1 - e^{-\kappa\tau}}{\kappa\tau} = \frac{1 - 0.8484}{0.16438} = \frac{0.1516}{0.16438} = 0.9222
    $$

    $$
    K_{\text{var}} = 0.05 + (0.04 - 0.05) \times 0.9222 = 0.05 - 0.009222 = 0.04078
    $$

    $$
    \text{VIX}_t = 100\sqrt{0.04078} = 100 \times 0.20194 = 20.19
    $$

    **Case 2: $v_t = 0.09$ (volatility spike).**

    $$
    K_{\text{var}} = 0.05 + (0.09 - 0.05) \times 0.9222 = 0.05 + 0.04 \times 0.9222 = 0.05 + 0.03689 = 0.08689
    $$

    $$
    \text{VIX}_t = 100\sqrt{0.08689} = 100 \times 0.29477 = 29.48
    $$

    **Summary.** When $v_t$ increases from 0.04 to 0.09 (a 125% increase), VIX increases from 20.19 to 29.48 (a 46% increase). The VIX response is less than proportional because:

    1. The square root dampens the variance change: $\sqrt{0.09}/\sqrt{0.04} = 1.5$, not 2.25.
    2. The coefficient $B = 0.9222 < 1$ means VIX$^2$ does not fully reflect $v_t$ (the 30-day averaging pulls toward $\theta$).
    3. The intercept $a = \theta(1 - B) = 0.05 \times 0.0778 = 0.00389$ provides a positive baseline.

---

**Exercise 5.**
The log-contract replication formula states that the fair variance strike can be expressed as $K_{\text{var}} = -\frac{2}{T}\mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0) - (e^{(r-q)T} - 1)]$. This connects variance swaps to the log-contract. Verify this formula for the Black-Scholes model where $\ln(S_T/S_0) \sim N((r - q - \sigma^2/2)T, \sigma^2 T)$ and show that $K_{\text{var}} = \sigma^2$.

??? success "Solution to Exercise 5"
    **Verifying the log-contract formula under Black--Scholes.** Under Black--Scholes, $\ln(S_T/S_0) \sim N(\mu T, \sigma^2 T)$ where $\mu = r - q - \sigma^2/2$.

    The log-contract replication formula states:

    $$
    K_{\text{var}} = -\frac{2}{T}\left[\mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)] - (e^{(r-q)T} - 1)\right]
    $$

    **Step 1.** Compute $\mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)]$. Under $\mathbb{Q}$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)] = \left(r - q - \frac{\sigma^2}{2}\right)T
    $$

    **Step 2.** Substitute into the formula:

    $$
    K_{\text{var}} = -\frac{2}{T}\left[\left(r - q - \frac{\sigma^2}{2}\right)T - (e^{(r-q)T} - 1)\right]
    $$

    $$
    = -2\left(r - q - \frac{\sigma^2}{2}\right) + \frac{2}{T}(e^{(r-q)T} - 1)
    $$

    **Step 3.** For the exact formula, note that the model-free replication formula is more precisely:

    $$
    K_{\text{var}} = \frac{2}{T}\left[e^{(r-q)T} - 1 - (r-q)T\right] + \frac{2}{T}\left[(r-q)T - \mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)]\right]
    $$

    The first bracket is the forward contract contribution and the second is the log-contract. Substituting $\mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)] = (r-q-\sigma^2/2)T$:

    $$
    K_{\text{var}} = \frac{2}{T}\left[e^{(r-q)T} - 1 - (r-q)T\right] + \frac{2}{T}\left[(r-q)T - (r-q)T + \frac{\sigma^2}{2}T\right]
    $$

    $$
    = \frac{2}{T}\left[e^{(r-q)T} - 1 - (r-q)T\right] + \sigma^2
    $$

    For the continuous-monitoring case, the quadratic variation is exactly $\sigma^2 T$, so $K_{\text{var}} = \sigma^2$ by the definition of realized variance as $\frac{1}{T}\langle \ln S \rangle_T = \sigma^2$.

    The direct argument is cleaner: under Black--Scholes, $d\ln S_t = (r-q-\sigma^2/2)dt + \sigma dW_t$, so the quadratic variation is $\langle \ln S \rangle_T = \sigma^2 T$, and:

    $$
    K_{\text{var}} = \frac{1}{T}\mathbb{E}^{\mathbb{Q}}[\langle \ln S \rangle_T] = \frac{1}{T} \cdot \sigma^2 T = \sigma^2
    $$

    This confirms $K_{\text{var}} = \sigma^2$, independent of $r$, $q$, $S_0$, and $T$. The fair variance strike equals the constant variance in Black--Scholes --- a reassuring consistency check.

---

**Exercise 6.**
A trader buys a 1-year variance swap at $K_{\text{var}} = 0.045$ with notional $N = \$100{,}000$ per variance point. If the realized variance over the year turns out to be $\sigma_R^2 = 0.06$, compute the P&L. Express the result in both variance points and dollars. Now compute the "vega notional" defined as $N_{\text{vega}} = N \cdot 2\sqrt{K_{\text{var}}}$ and explain why this is a more intuitive measure of the swap's exposure.

??? success "Solution to Exercise 6"
    **Variance swap P&L calculation.**

    **Given:** $K_{\text{var}} = 0.045$, $N = \$100{,}000$ per variance point, $\sigma_R^2 = 0.06$.

    **P&L in variance points:**

    $$
    \text{P\&L} = N(\sigma_R^2 - K_{\text{var}}) = 100{,}000 \times (0.06 - 0.045) = 100{,}000 \times 0.015
    $$

    $$
    = \$1{,}500
    $$

    The buyer of the variance swap profits \$1,500.

    **Vega notional.** The vega notional is defined as:

    $$
    N_{\text{vega}} = N \cdot 2\sqrt{K_{\text{var}}} = 100{,}000 \times 2\sqrt{0.045} = 100{,}000 \times 2 \times 0.2121 = \$42{,}426
    $$

    **Why vega notional is more intuitive.** The variance notional $N$ gives exposure in units of variance (decimal squared), which is not intuitive. Traders think in terms of volatility (percentage), not variance.

    The vega notional approximates the P&L for a 1 percentage point (1 "vega point") move in realized volatility. Using a first-order Taylor expansion of $\sigma_R^2 \approx K_{\text{var}} + 2\sqrt{K_{\text{var}}}(\sigma_R - \sqrt{K_{\text{var}}})$:

    $$
    \text{P\&L} \approx N \cdot 2\sqrt{K_{\text{var}}} \cdot (\sigma_R - \sqrt{K_{\text{var}}}) = N_{\text{vega}} \cdot (\sigma_R - \sqrt{K_{\text{var}}})
    $$

    In our example: $\sigma_R = \sqrt{0.06} = 0.2449 = 24.49\%$ and $\sqrt{K_{\text{var}}} = 21.21\%$. The volatility move is $24.49\% - 21.21\% = 3.28\%$. Using vega notional:

    $$
    \text{P\&L} \approx 42{,}426 \times 0.0328 = \$1{,}392
    $$

    This approximation (\$1,392) is close to the exact P&L (\$1,500). The difference arises from the convexity of the variance payoff: $\sigma^2 - K = (\sigma - \sqrt{K})(\sigma + \sqrt{K}) > 2\sqrt{K}(\sigma - \sqrt{K})$ when $\sigma > \sqrt{K}$. The variance swap buyer benefits from this convexity --- the "long convexity" position is a key feature of variance swaps versus volatility swaps.

---

**Exercise 7.**
The sensitivity of the fair variance strike to $v_0$ is $\partial K_{\text{var}} / \partial v_0 = (1 - e^{-\kappa T})/(\kappa T)$. Compute this sensitivity for $\kappa = 2.0$ and $T = 0.5, 1.0, 2.0$. Show that the sensitivity decreases with $T$ (the strike depends less on $v_0$ for longer maturities). Discuss the implication for hedging: a desk holding a long-dated variance swap has less exposure to short-term variance moves.

??? success "Solution to Exercise 7"
    **Computing the sensitivity $\partial K_{\text{var}} / \partial v_0$.** The sensitivity is:

    $$
    \frac{\partial K_{\text{var}}}{\partial v_0} = \frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    For $\kappa = 2.0$:

    **$T = 0.5$:**

    $$
    \frac{\partial K_{\text{var}}}{\partial v_0} = \frac{1 - e^{-1.0}}{1.0} = \frac{1 - 0.3679}{1.0} = 0.6321
    $$

    **$T = 1.0$:**

    $$
    \frac{\partial K_{\text{var}}}{\partial v_0} = \frac{1 - e^{-2.0}}{2.0} = \frac{1 - 0.1353}{2.0} = \frac{0.8647}{2.0} = 0.4323
    $$

    **$T = 2.0$:**

    $$
    \frac{\partial K_{\text{var}}}{\partial v_0} = \frac{1 - e^{-4.0}}{4.0} = \frac{1 - 0.01832}{4.0} = \frac{0.98168}{4.0} = 0.2454
    $$

    | Maturity $T$ | $\kappa T$ | $\partial K_{\text{var}} / \partial v_0$ |
    |:---:|:---:|:---:|
    | 0.5 | 1.0 | 0.6321 |
    | 1.0 | 2.0 | 0.4323 |
    | 2.0 | 4.0 | 0.2454 |

    **Monotone decrease.** To show the sensitivity decreases with $T$, differentiate with respect to $T$:

    $$
    \frac{d}{dT}\left(\frac{1 - e^{-\kappa T}}{\kappa T}\right) = \frac{\kappa T e^{-\kappa T} \cdot \kappa - \kappa(1 - e^{-\kappa T})}{(\kappa T)^2} \cdot T
    $$

    Simplifying, let $x = \kappa T > 0$:

    $$
    \frac{d}{dT}\left(\frac{1 - e^{-x}}{x}\right) = \frac{\kappa(xe^{-x} - 1 + e^{-x})}{x^2} = \frac{\kappa((1+x)e^{-x} - 1)}{x^2}
    $$

    We need to show $(1 + x)e^{-x} < 1$ for $x > 0$. Define $h(x) = (1+x)e^{-x}$. Then $h(0) = 1$ and $h'(x) = -xe^{-x} < 0$ for $x > 0$, so $h$ is strictly decreasing. Therefore $h(x) < 1$ for all $x > 0$, confirming the sensitivity is strictly decreasing in $T$.

    **Hedging implication.** A trading desk holding a long-dated variance swap (e.g., $T = 2$ years) has sensitivity $0.2454$ to $v_0$, meaning a 1 unit change in $v_0$ changes the fair strike by only 0.245 units. In contrast, a short-dated variance swap ($T = 0.5$) has sensitivity $0.6321$ --- nearly three times larger.

    This means:

    - **Short-dated variance swaps** are strongly exposed to current variance conditions. A spike in $v_t$ immediately translates into a large P&L movement.
    - **Long-dated variance swaps** are more exposed to the long-run variance $\theta$ than to current conditions. Their fair strike is relatively insensitive to short-term variance fluctuations because mean reversion dampens the effect of $v_0$ over long horizons.
    - **Hedging strategy:** A desk can partially hedge a long-dated variance swap using short-dated variance swaps, but the hedge ratio must account for the maturity-dependent sensitivity. The hedge ratio is approximately $0.2454/0.6321 = 0.388$: about 0.39 units of the short-dated swap per unit of the long-dated swap.
