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

Recall (see [§ Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md)): the log-price form is $dx_t = (r - q - \tfrac{1}{2} v_t)\,dt + \sqrt{v_t}\,dW_t^{(1)}$ and $dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$, with $d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt$. The log-price formulation avoids multiplicative noise in $S_t$ and is standard for Monte Carlo simulation.

---

## Correlated Brownian Increments

Recall (see [§ SDE Simulation](../../ch03/sde/sde_simulation.md)): to generate correlated increments via Cholesky, draw $Z_1, Z_2 \sim N(0,1)$ and set $\Delta W^{(1)} = \sqrt{\Delta t}\,Z_1$ and $\Delta W^{(2)} = \sqrt{\Delta t}(\rho Z_1 + \sqrt{1-\rho^2}\,Z_2)$, giving $\text{Corr}(\Delta W^{(1)}, \Delta W^{(2)}) = \rho$.

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

---

## Exercises

**Exercise 1.**
The Cholesky decomposition generates correlated Brownian increments as $\Delta W^{(2)} = \sqrt{\Delta t}(\rho Z_1 + \sqrt{1 - \rho^2}\,Z_2)$. Verify that $\text{Var}(\Delta W^{(2)}) = \Delta t$ and $\text{Cov}(\Delta W^{(1)}, \Delta W^{(2)}) = \rho\,\Delta t$. For $\rho = -0.7$, compute the coefficient of $Z_2$ and explain why the $Z_2$ component represents the variance risk that is orthogonal to the stock.

??? success "Solution to Exercise 1"
    We need to verify the variance and covariance of the Cholesky-generated increments. Recall $\Delta W^{(1)} = \sqrt{\Delta t}\,Z_1$ and $\Delta W^{(2)} = \sqrt{\Delta t}(\rho\,Z_1 + \sqrt{1-\rho^2}\,Z_2)$ where $Z_1, Z_2 \sim N(0,1)$ are independent.

    **Variance of** $\Delta W^{(2)}$:

    $$
    \text{Var}(\Delta W^{(2)}) = \Delta t \,\text{Var}(\rho Z_1 + \sqrt{1-\rho^2}\,Z_2)
    $$

    Since $Z_1$ and $Z_2$ are independent:

    $$
    \text{Var}(\rho Z_1 + \sqrt{1-\rho^2}\,Z_2) = \rho^2 \text{Var}(Z_1) + (1-\rho^2)\text{Var}(Z_2) = \rho^2 + 1 - \rho^2 = 1
    $$

    Therefore $\text{Var}(\Delta W^{(2)}) = \Delta t$.

    **Covariance:**

    $$
    \text{Cov}(\Delta W^{(1)}, \Delta W^{(2)}) = \Delta t\,\text{Cov}(Z_1, \rho Z_1 + \sqrt{1-\rho^2}\,Z_2)
    $$

    $$
    = \Delta t\left[\rho\,\text{Var}(Z_1) + \sqrt{1-\rho^2}\,\text{Cov}(Z_1, Z_2)\right] = \Delta t\,[\rho \cdot 1 + 0] = \rho\,\Delta t
    $$

    **For** $\rho = -0.7$: The coefficient of $Z_2$ is $\sqrt{1-(-0.7)^2} = \sqrt{1-0.49} = \sqrt{0.51} \approx 0.7141$.

    The $Z_2$ component represents variance risk orthogonal to the stock because $Z_2$ is independent of $Z_1$ (which drives $\Delta W^{(1)}$, the stock's Brownian motion). The $Z_2$ component captures the part of variance randomness that cannot be hedged by trading the underlying stock. With $\rho = -0.7$, approximately 51% of the variance of $\Delta W^{(2)}$ comes from the orthogonal component $Z_2$, and 49% is shared with the stock risk $Z_1$. This orthogonal variance risk is what generates the volatility risk premium and is the source of the Heston model's ability to produce implied volatility skew.

---

**Exercise 2.**
The Feller ratio is $2\kappa\theta/\xi^2$. For the worked example parameters ($\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$), the ratio is approximately 1.33. Now consider market-calibrated parameters $\kappa = 2.0$, $\theta = 0.02$, $\xi = 0.5$, giving a Feller ratio of 0.32. With $v_n = 0.01$, $\Delta t = 1/252$, and a random draw $Z_2 = -2.5$, compute the naive Euler update $\hat{v}_{n+1}$. Is it negative? Repeat for full truncation, reflection, and absorption, showing the three different corrected values.

??? success "Solution to Exercise 2"
    **Feller ratio:** $2\kappa\theta/\xi^2 = 2(2.0)(0.02)/0.25 = 0.08/0.25 = 0.32 < 1$, so the Feller condition is violated.

    **Naive Euler update:** With $v_n = 0.01$, $\Delta t = 1/252$, and $Z_2 = -2.5$:

    First compute $\Delta W^{(2)}$. For the variance equation only, we need the $Z_2$-driven increment. Taking $\rho Z_1 + \sqrt{1-\rho^2}\,Z_2$ aside, the variance is driven by a single effective normal. For simplicity, assume the shock to the variance equation is $\Delta W^{(2)} = \sqrt{\Delta t}\,Z_2' = \sqrt{1/252}\cdot(-2.5) \approx -0.1575$ where $Z_2'$ is the effective normal shock to the variance.

    $$
    \hat{v}_{n+1} = 0.01 + 2.0(0.02 - 0.01)\frac{1}{252} + 0.5\sqrt{0.01}\cdot(-0.1575)
    $$

    $$
    = 0.01 + 0.0000794 + 0.5(0.1)(-0.1575) = 0.01 + 0.0000794 - 0.007875
    $$

    $$
    = 0.002204
    $$

    This is positive in this case. However, let us use a more extreme scenario to illustrate the negative variance problem. With $Z_2 = -3.5$, we get $\Delta W^{(2)} = \sqrt{1/252}(-3.5) \approx -0.2205$:

    $$
    \hat{v}_{n+1} = 0.01 + 0.0000794 + 0.5(0.1)(-0.2205) = 0.01 + 0.0000794 - 0.01102 = -0.000941
    $$

    This is negative. Now apply the three fix schemes (using $Z_2 = -3.5$):

    **Full truncation:** Since $v_n = 0.01 > 0$, we have $v_n^+ = 0.01$. The update is the same as naive Euler:

    $$
    v_{n+1} = 0.01 + 2.0(0.02 - 0.01)(1/252) + 0.5\sqrt{0.01}(-0.2205) = -0.000941
    $$

    The value $v_{n+1}$ is allowed to be negative; only the next step uses $v_{n+1}^+ = \max(-0.000941, 0) = 0$ in the diffusion and drift coefficients.

    **Reflection:** Compute $\tilde{v}_{n+1} = -0.000941$, then $v_{n+1} = |\tilde{v}_{n+1}| = 0.000941$.

    **Absorption:** Compute $\tilde{v}_{n+1} = -0.000941$, then $v_{n+1} = \max(\tilde{v}_{n+1}, 0) = 0$.

    The three corrected values are: full truncation keeps $-0.000941$ (corrects at point of use), reflection gives $0.000941$, and absorption gives $0$. The reflection scheme preserves the magnitude of the excursion, while absorption removes it entirely.

---

**Exercise 3.**
In the full truncation scheme, when $v_n < 0$, the drift term becomes $\kappa(\theta - 0) = \kappa\theta > 0$ (maximally mean-reverting) and the diffusion term is $\xi\sqrt{0} = 0$. Show that the next update is deterministic: $v_{n+1} = v_n + \kappa\theta\,\Delta t$. How many consecutive steps are needed for $v$ to return to positive territory if $v_n = -0.005$? Use $\kappa = 1.5$, $\theta = 0.04$, $\Delta t = 1/252$.

??? success "Solution to Exercise 3"
    When $v_n < 0$ in the full truncation scheme, $v_n^+ = 0$. The update becomes:

    $$
    v_{n+1} = v_n + \kappa(\theta - 0)\Delta t + \xi\sqrt{0}\,\Delta W_n^{(2)} = v_n + \kappa\theta\,\Delta t
    $$

    The diffusion term vanishes entirely, making the update **deterministic**. Each step adds exactly $\kappa\theta\,\Delta t$ to the current variance.

    With $v_n = -0.005$, $\kappa = 1.5$, $\theta = 0.04$, $\Delta t = 1/252$:

    $$
    \kappa\theta\,\Delta t = 1.5 \times 0.04 \times \frac{1}{252} = \frac{0.06}{252} \approx 0.000238
    $$

    Starting from $v_n = -0.005$, after $k$ deterministic steps:

    $$
    v_{n+k} = -0.005 + k \cdot 0.000238
    $$

    We need $v_{n+k} > 0$, i.e., $k > 0.005 / 0.000238 \approx 21.0$.

    Therefore **22 consecutive deterministic steps** are needed for the variance to return to positive territory. At step 21, $v_{n+21} = -0.005 + 21(0.000238) = -0.005 + 0.005 = 0.0$, which is not strictly positive. At step 22, $v_{n+22} = -0.005 + 22(0.000238) = 0.000238 > 0$.

    In terms of time, this corresponds to $22/252 \approx 0.087$ years, or roughly 4.4 weeks. During this entire period, the simulated stock price evolves with zero volatility---a significant distortion of the true dynamics.

---

**Exercise 4.**
The reflection scheme sets $v_{n+1} = |\tilde{v}_{n+1}|$. Argue that this introduces a positive bias in the variance distribution: the probability of $v_{n+1} = x > 0$ under reflection includes both the probability of $\tilde{v}_{n+1} = x$ and $\tilde{v}_{n+1} = -x$. How does this bias affect the option price? Would you expect reflected-Euler call prices to be systematically higher or lower than the true price?

??? success "Solution to Exercise 4"
    Let $\tilde{v}_{n+1}$ denote the pre-reflection value. Under the reflection scheme, $v_{n+1} = |\tilde{v}_{n+1}|$. Consider the distribution of $v_{n+1}$ for $x > 0$:

    $$
    \mathbb{P}(v_{n+1} \leq x) = \mathbb{P}(|\tilde{v}_{n+1}| \leq x) = \mathbb{P}(-x \leq \tilde{v}_{n+1} \leq x)
    $$

    The density of $v_{n+1}$ at $x > 0$ is:

    $$
    f_{v_{n+1}}(x) = f_{\tilde{v}}(x) + f_{\tilde{v}}(-x)
    $$

    where $f_{\tilde{v}}$ is the density of the pre-reflection value. This means every positive value $x$ receives probability mass from both $\tilde{v} = x$ and $\tilde{v} = -x$.

    **Bias in the mean:** The expected value of the reflected variable is:

    $$
    \mathbb{E}[|\tilde{v}_{n+1}|] = \mathbb{E}[\tilde{v}_{n+1} \cdot \mathbf{1}_{\tilde{v}_{n+1} \geq 0}] + \mathbb{E}[-\tilde{v}_{n+1} \cdot \mathbf{1}_{\tilde{v}_{n+1} < 0}]
    $$

    $$
    = \mathbb{E}[\tilde{v}_{n+1}] + 2\mathbb{E}[-\tilde{v}_{n+1} \cdot \mathbf{1}_{\tilde{v}_{n+1} < 0}]
    $$

    Since $\mathbb{E}[-\tilde{v}_{n+1} \cdot \mathbf{1}_{\tilde{v}_{n+1} < 0}] > 0$ whenever $\mathbb{P}(\tilde{v}_{n+1} < 0) > 0$, we have $\mathbb{E}[|\tilde{v}_{n+1}|] > \mathbb{E}[\tilde{v}_{n+1}]$. The reflection introduces a **positive bias** in the variance.

    **Effect on option prices:** Higher variance leads to higher option prices for both calls and puts (variance enters through the vega channel). Therefore, the reflection scheme systematically **overestimates** the option price. European call prices computed with the reflection scheme will be biased upward relative to the true Heston price, with the magnitude of the bias increasing as the probability of negative pre-reflection values grows (i.e., when the Feller condition is more severely violated).

---

**Exercise 5.**
The weak convergence order of 1 means that the pricing bias decreases linearly with $\Delta t$. If the Euler full-truncation bias at $\Delta t = 1/252$ is $\$0.05$, estimate the bias at $\Delta t = 1/504$ and $\Delta t = 1/1008$. How many steps are needed to reduce the bias below $\$0.001$? Compare the total computational cost (paths $\times$ steps) against using the QE scheme with 12 steps and near-zero bias.

??? success "Solution to Exercise 5"
    Weak convergence of order 1 means the bias satisfies $\text{Bias}(\Delta t) = C \cdot \Delta t + \mathcal{O}(\Delta t^2)$ for some constant $C$. Given $\text{Bias}(1/252) = \$0.05$, we estimate $C \approx 0.05 \times 252 = 12.6$.

    **At** $\Delta t = 1/504$ (halving the step size):

    $$
    \text{Bias}(1/504) \approx C \cdot \frac{1}{504} = \frac{12.6}{504} \approx \$0.025
    $$

    **At** $\Delta t = 1/1008$:

    $$
    \text{Bias}(1/1008) \approx \frac{12.6}{1008} \approx \$0.0125
    $$

    **Steps needed for bias** $< \$0.001$:

    $$
    C \cdot \frac{1}{N} < 0.001 \implies N > \frac{12.6}{0.001} = 12{,}600 \text{ steps}
    $$

    **Computational cost comparison:**

    - Euler with $N = 12{,}600$ steps and $M = 100{,}000$ paths: total work $= M \times N = 1.26 \times 10^9$ step-evaluations.
    - QE scheme with $N = 12$ steps and near-zero bias: total work $= M \times N = 100{,}000 \times 12 = 1.2 \times 10^6$ step-evaluations.

    The QE scheme achieves comparable or better accuracy with roughly **1,000 times less computation**. Even accounting for the higher per-step cost of QE (approximately $3\times$ that of Euler), the QE scheme is still about 300 times more efficient. This dramatic difference arises because the QE scheme's moment-matching approach captures the CIR transition distribution far more accurately per step than the Euler discretization.

---

**Exercise 6.**
The log-price update uses $v_n^+$ in both the drift and diffusion: $x_{n+1} = x_n + (r - q - \frac{1}{2}v_n^+)\Delta t + \sqrt{v_n^+}\,\Delta W_n^{(1)}$. When $v_n^+ = 0$, the update becomes $x_{n+1} = x_n + (r - q)\Delta t$ with no randomness. Explain how this affects the simulated stock price distribution during periods of zero variance and why it can cause the Monte Carlo estimator to underestimate the true option price.

??? success "Solution to Exercise 6"
    When $v_n^+ = 0$, the log-price update reduces to:

    $$
    x_{n+1} = x_n + (r - q)\Delta t + \sqrt{0}\,\Delta W_n^{(1)} = x_n + (r - q)\Delta t
    $$

    The stock price evolves **deterministically** as $S_{n+1} = S_n e^{(r-q)\Delta t}$ during these steps. This has several consequences:

    **Loss of diffusion:** The stock price accumulates no randomness during zero-variance periods. In the true continuous-time Heston model, even when $v_t$ is very small, $\sqrt{v_t}$ is still positive and the stock retains some stochastic behavior. The truncation creates artificial periods of zero volatility that do not exist in the continuous model.

    **Effect on the terminal distribution:** The truncated paths have less total integrated variance than the true paths:

    $$
    \sum_{n=0}^{N-1} v_n^+ \Delta t \leq \sum_{n=0}^{N-1} v_n \Delta t \quad \text{(with equality when } v_n \geq 0 \text{ for all } n\text{)}
    $$

    Lower integrated variance leads to a narrower terminal distribution of $\ln S_T$, which reduces the expected payoff of convex claims (calls and puts).

    **Underestimation of option prices:** For a European call, the price is an increasing function of the total variance (via the vega effect). By removing variance during truncated periods, the Monte Carlo estimator systematically underestimates the spread of the terminal stock price distribution, leading to a **downward bias** in the estimated call price. This effect is most pronounced when the Feller condition is violated and the variance frequently visits near-zero levels, causing many truncation events per path.

---

**Exercise 7.**
Implement the Euler full-truncation scheme with $M = 10{,}000$ paths and $N = 252$ steps for the worked example parameters. Compute the European call price and its 95% confidence interval. Then repeat with $N = 50$ steps (weekly) and $N = 12$ steps (monthly). How does the bias change with $N$? At what point does the bias dominate the Monte Carlo standard error?

??? success "Solution to Exercise 7"
    This exercise requires implementation. We outline the algorithm, expected results, and analysis.

    **Algorithm (Euler full truncation):** For each path $m = 1, \ldots, M$:

    1. Initialize $v_0 = 0.04$, $x_0 = \ln(100)$
    2. For each step $n = 0, \ldots, N-1$: draw $Z_1, Z_2 \sim N(0,1)$, set $v_n^+ = \max(v_n, 0)$, update
        - $v_{n+1} = v_n + \kappa(\theta - v_n^+)\Delta t + \xi\sqrt{v_n^+}\sqrt{\Delta t}(\rho Z_1 + \sqrt{1-\rho^2}Z_2)$
        - $x_{n+1} = x_n + (r - q - v_n^+/2)\Delta t + \sqrt{v_n^+}\sqrt{\Delta t}\,Z_1$
    3. Payoff: $(e^{x_N} - K)^+$

    Price: $\hat{C} = e^{-rT}\frac{1}{M}\sum_{m=1}^M \text{payoff}^{(m)}$.

    **Expected results** (the Fourier-inversion benchmark is approximately $\$10.36$):

    | $N$ | $\Delta t$ | $\hat{C}$ (approx) | Std Error | Bias |
    |-----|-----------|---------------------|-----------|------|
    | 252 | $1/252$ | $\$10.31$ | $\$0.15$ | $\approx -\$0.05$ |
    | 50 | $1/50$ | $\$10.11$ | $\$0.15$ | $\approx -\$0.25$ |
    | 12 | $1/12$ | $\$9.76$ | $\$0.15$ | $\approx -\$0.60$ |

    **Analysis:** The Monte Carlo standard error (for $M = 10{,}000$) is approximately $\$0.15$ regardless of $N$, since it depends on the payoff variance, not the time step. The bias scales as $\mathcal{O}(\Delta t)$:

    - At $N = 252$: bias $\approx \$0.05 \ll$ std error $\$0.15$. The standard error dominates; the bias is buried in sampling noise.
    - At $N = 50$: bias $\approx \$0.25 >$ std error $\$0.15$. The bias is now comparable to the standard error and begins to dominate.
    - At $N = 12$: bias $\approx \$0.60 \gg$ std error $\$0.15$. The bias completely dominates; adding more paths will not improve accuracy.

    The crossover point where bias equals the standard error occurs roughly when $C/N \approx \sigma_g/\sqrt{M}$. With $C \approx 12.6$ and $\sigma_g \approx 15$, this gives $N \approx 12.6\sqrt{M}/15 = 12.6 \times 100/15 \approx 84$ steps. For $N < 84$, the bias dominates; for $N > 84$, the standard error dominates. This highlights the importance of choosing $N$ large enough that the discretization error is smaller than the Monte Carlo sampling error.
