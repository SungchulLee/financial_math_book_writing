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

Under the Heston model, $v_t$ follows the CIR process:

$$
dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
$$

The conditional expectation of $v_t$ given $v_0$ is:

$$
\mathbb{E}^{\mathbb{Q}}[v_t \mid v_0] = \theta + (v_0 - \theta)e^{-\kappa t}
$$

Integrating over $[0, T]$:

$$
\mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T v_t \, dt \,\Big|\, v_0\right] = \int_0^T \left[\theta + (v_0 - \theta)e^{-\kappa t}\right] dt
$$

Evaluating the integral:

$$
= \theta T + (v_0 - \theta) \int_0^T e^{-\kappa t} \, dt = \theta T + (v_0 - \theta) \frac{1 - e^{-\kappa T}}{\kappa}
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
