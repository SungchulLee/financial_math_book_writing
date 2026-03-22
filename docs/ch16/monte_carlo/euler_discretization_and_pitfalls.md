# Euler Discretization and Pitfalls

The simplest approach to simulating the Heston model is the Euler-Maruyama scheme, which replaces continuous-time SDEs with discrete time steps. However, the square-root diffusion in the variance process creates a fundamental challenge: the standard Euler scheme can produce **negative variance values**, which are mathematically impossible under the CIR dynamics. This section develops three practical fixes---full truncation, reflection, and absorption---and analyzes the convergence properties and biases of each.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Euler-Maruyama discretization for both the variance and log-price processes in the Heston model
    2. Identify the source of negative variance in naive Euler schemes and explain why standard convergence theory fails
    3. Implement full truncation, reflection, and absorption schemes with their precise update formulas
    4. Compare convergence orders and bias properties across the three schemes

!!! tip "Prerequisites"
    This section builds on the [Heston SDE and parameters](../model_definition/heston_sde_and_parameters.md), the [CIR variance process](../variance_dynamics/cir_variance_process_solution.md), and the [Feller condition](../model_definition/feller_condition_and_boundary.md).

---

## The Heston SDE System

Under the risk-neutral measure $\mathbb{Q}$, the Heston model specifies two coupled SDEs:

$$
dS_t = (r - q) S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1)}
$$

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}
$$

where $d\langle W^{(1)}, W^{(2)} \rangle_t = \rho \, dt$ with $\rho \in [-1, 1]$. The parameters are: risk-free rate $r$, dividend yield $q$, mean-reversion speed $\kappa > 0$, long-run variance $\theta > 0$, vol-of-vol $\xi > 0$, and correlation $\rho$.

Working with the **log-price** $x_t = \ln S_t$ simplifies the stock equation:

$$
dx_t = \left(r - q - \tfrac{1}{2} v_t\right) dt + \sqrt{v_t} \, dW_t^{(1)}
$$

This formulation avoids the multiplicative noise in $S_t$ and is standard for Monte Carlo simulation.

---

## Correlated Brownian Increments

The two Brownian motions $W^{(1)}$ and $W^{(2)}$ are correlated with parameter $\rho$. To generate correlated increments on a discrete grid with step $\Delta t$, apply the **Cholesky decomposition**. Draw two independent standard normals $Z_1, Z_2 \sim N(0,1)$ and set:

$$
\Delta W^{(1)} = \sqrt{\Delta t} \, Z_1
$$

$$
\Delta W^{(2)} = \sqrt{\Delta t} \left( \rho \, Z_1 + \sqrt{1 - \rho^2} \, Z_2 \right)
$$

This ensures $\text{Corr}(\Delta W^{(1)}, \Delta W^{(2)}) = \rho$ and both increments have variance $\Delta t$.

---

## Naive Euler-Maruyama Discretization

The standard Euler-Maruyama scheme discretizes both processes on a uniform grid $0 = t_0 < t_1 < \cdots < t_N = T$ with step $\Delta t = T/N$.

**Variance update:**

$$
\hat{v}_{n+1} = v_n + \kappa(\theta - v_n) \Delta t + \xi \sqrt{v_n} \, \Delta W_n^{(2)}
$$

**Log-price update:**

$$
x_{n+1} = x_n + \left(r - q - \tfrac{1}{2} v_n\right) \Delta t + \sqrt{v_n} \, \Delta W_n^{(1)}
$$

### The Negative Variance Problem

The critical issue is that $\hat{v}_{n+1}$ can become negative. When $v_n$ is small and the random shock $\Delta W_n^{(2)}$ is sufficiently negative, the update produces $\hat{v}_{n+1} < 0$. This occurs because:

1. The diffusion coefficient $\xi \sqrt{v_n}$ is **not globally Lipschitz** --- it has an unbounded derivative as $v_n \to 0^+$.
2. Standard Euler-Maruyama convergence theory requires globally Lipschitz diffusion coefficients, which the CIR process violates.
3. Even when the Feller condition $2\kappa\theta \geq \xi^2$ holds (ensuring the continuous-time process stays strictly positive), the discrete approximation can still generate negative values.

Taking $\sqrt{v_{n+1}}$ of a negative value produces `NaN`, which propagates through the entire simulation. Three practical modifications address this problem.

---

## Full Truncation Scheme

The **full truncation** scheme, introduced by Lord, Koekkoek, and Van Dijk (2010), replaces negative variance values with zero in the diffusion and drift terms while keeping the variance update unrestricted. Define $v_n^+ = \max(v_n, 0)$.

**Variance update:**

$$
v_{n+1} = v_n + \kappa(\theta - v_n^+) \Delta t + \xi \sqrt{v_n^+} \, \Delta W_n^{(2)}
$$

**Log-price update:**

$$
x_{n+1} = x_n + \left(r - q - \tfrac{1}{2} v_n^+\right) \Delta t + \sqrt{v_n^+} \, \Delta W_n^{(1)}
$$

The key idea is that wherever $v_n$ appears under a square root or as an instantaneous variance, the truncated value $v_n^+$ is used. The variance $v_n$ itself is allowed to go negative temporarily; only its role in the diffusion and drift coefficients is truncated.

!!! note "Why Full Truncation Works Well"
    When $v_n < 0$, the drift term $\kappa(\theta - v_n^+) = \kappa\theta$ is maximally mean-reverting, pushing the variance back toward $\theta$. This mimics the behavior of the continuous-time CIR process near zero, where the drift dominates the diffusion.

---

## Reflection Scheme

The **reflection scheme** takes the absolute value of the variance whenever it becomes negative:

$$
\tilde{v}_{n+1} = v_n + \kappa(\theta - v_n) \Delta t + \xi \sqrt{|v_n|} \, \Delta W_n^{(2)}
$$

$$
v_{n+1} = |\tilde{v}_{n+1}|
$$

This is motivated by the fact that the CIR process has a reflecting boundary at zero when the Feller condition is satisfied. By reflecting negative values, the scheme preserves the magnitude of the variance excursion while keeping it non-negative.

The log-price update uses the reflected variance:

$$
x_{n+1} = x_n + \left(r - q - \tfrac{1}{2} v_{n+1}\right) \Delta t + \sqrt{v_{n+1}} \, \Delta W_n^{(1)}
$$

---

## Absorption Scheme

The **absorption scheme** simply sets negative variance to zero:

$$
\tilde{v}_{n+1} = v_n + \kappa(\theta - v_n) \Delta t + \xi \sqrt{\max(v_n, 0)} \, \Delta W_n^{(2)}
$$

$$
v_{n+1} = \max(\tilde{v}_{n+1}, 0)
$$

When the Feller condition is violated ($2\kappa\theta < \xi^2$), the continuous-time process can touch zero and the boundary at zero is absorbing in the sense that the process spends zero Lebesgue time there. The absorption scheme emulates this behavior by clamping negative values.

---

## Convergence Properties

The convergence behavior of these schemes differs from the classical Euler-Maruyama theory because the CIR diffusion coefficient $\sigma(v) = \xi\sqrt{v}$ is only $\frac{1}{2}$-Holder continuous at $v = 0$, not Lipschitz.

### Weak Convergence

For smooth test functions $f$, the **weak error** $|\mathbb{E}[f(v_N)] - \mathbb{E}[f(v_T)]|$ satisfies:

| Scheme | Weak Order |
|--------|-----------|
| Full truncation | $\mathcal{O}(\Delta t)$ |
| Reflection | $\mathcal{O}(\Delta t)$ |
| Absorption | $\mathcal{O}(\Delta t)$ |

All three schemes achieve first-order weak convergence, matching the standard Euler-Maruyama rate despite the non-Lipschitz coefficient.

### Strong Convergence

The **strong error** $\mathbb{E}[|v_N - v_T|^2]^{1/2}$ is more delicate:

| Scheme | Strong Order |
|--------|-------------|
| Full truncation | $\mathcal{O}(\Delta t^{1/2})$ |
| Reflection | $\mathcal{O}(\Delta t^{1/2})$ |
| Absorption | $\mathcal{O}(\Delta t^{1/2})$ |

The strong order $\frac{1}{2}$ is the same as standard Euler-Maruyama, but the constant in the error bound depends on the Feller ratio $2\kappa\theta / \xi^2$. When this ratio is well above 1, the error constant is moderate; when it is close to or below 1, the constant can be large.

### Bias in Option Prices

For European option pricing, the relevant metric is the **weak error in the option price**. Lord, Koekkoek, and Van Dijk (2010) showed empirically that:

- **Full truncation** has the smallest bias among the three schemes for typical Heston parameters.
- **Absorption** tends to underestimate the variance (and thus the option price) because it removes negative excursions entirely.
- **Reflection** can overestimate variance slightly due to the artificial bounce.

---

## Worked Example

Consider a European call under the Heston model with parameters:

| Parameter | Value |
|-----------|-------|
| $S_0$ | $\$100$ |
| $K$ | $\$100$ |
| $r$ | $0.05$ |
| $q$ | $0$ |
| $v_0$ | $0.04$ |
| $\kappa$ | $1.5$ |
| $\theta$ | $0.04$ |
| $\xi$ | $0.3$ |
| $\rho$ | $-0.7$ |
| $T$ | $1.0$ |

The Feller ratio is $2\kappa\theta / \xi^2 = 2(1.5)(0.04) / 0.09 \approx 1.33 > 1$, so the continuous-time process stays strictly positive. Nevertheless, discrete Euler steps can still produce negative variance.

??? example "Euler Full Truncation Algorithm"
    For each Monte Carlo path $m = 1, \ldots, M$ with $N$ time steps:

    1. Set $v_0^{(m)} = v_0$, $x_0^{(m)} = \ln S_0$
    2. For $n = 0, 1, \ldots, N-1$:
        - Draw $Z_1, Z_2 \sim N(0,1)$ independently
        - Set $\Delta W^{(1)} = \sqrt{\Delta t} \, Z_1$ and $\Delta W^{(2)} = \sqrt{\Delta t}(\rho Z_1 + \sqrt{1 - \rho^2} \, Z_2)$
        - Compute $v_n^+ = \max(v_n^{(m)}, 0)$
        - Update: $v_{n+1}^{(m)} = v_n^{(m)} + \kappa(\theta - v_n^+)\Delta t + \xi\sqrt{v_n^+} \, \Delta W^{(2)}$
        - Update: $x_{n+1}^{(m)} = x_n^{(m)} + (r - q - \tfrac{1}{2}v_n^+)\Delta t + \sqrt{v_n^+} \, \Delta W^{(1)}$
    3. Compute payoff: $\text{payoff}^{(m)} = \max(e^{x_N^{(m)}} - K, 0)$
    4. Price: $\hat{C} = e^{-rT} \frac{1}{M}\sum_{m=1}^{M} \text{payoff}^{(m)}$

With $M = 100{,}000$ paths and $N = 252$ steps, the full truncation scheme typically produces a price within $\$0.05$ of the semi-analytical Fourier inversion result for this parameter set.

!!! warning "Feller Condition Violation in Practice"
    Market-calibrated Heston parameters frequently violate the Feller condition ($2\kappa\theta / \xi^2 < 1$). In equity markets, typical calibrated values give Feller ratios between 0.3 and 0.8. When this happens, negative variance events in Euler schemes become frequent, and the choice of fix scheme materially affects the price. Full truncation is generally preferred in this regime.

---

## Comparison of Fix Schemes

The following table summarizes the practical trade-offs:

| Feature | Full Truncation | Reflection | Absorption |
|---------|----------------|------------|------------|
| Variance stays non-negative | No (but $v^+$ used) | Yes | Yes |
| Bias magnitude | Smallest | Moderate | Largest |
| Feller-violated behavior | Best | Acceptable | Poor |
| Implementation complexity | Low | Low | Low |
| Recommended | Yes | Sometimes | Rarely |

The full truncation scheme is the **standard choice** for Euler-based Heston simulation due to its combination of low bias, simplicity, and robustness across parameter regimes.

---

## Summary

The Euler-Maruyama discretization of the Heston model faces a fundamental obstacle: the square-root diffusion coefficient in the CIR variance process is not Lipschitz, causing naive Euler steps to produce negative variance. Three fix schemes---full truncation, reflection, and absorption---restore non-negativity with different bias characteristics. All three achieve weak order $\mathcal{O}(\Delta t)$ and strong order $\mathcal{O}(\Delta t^{1/2})$. Among these, full truncation offers the smallest pricing bias and is the recommended default. For higher accuracy, the [Milstein scheme](milstein_scheme.md) and the [quadratic-exponential scheme](quadratic_exponential_scheme.md) provide improved convergence at moderate additional complexity.
