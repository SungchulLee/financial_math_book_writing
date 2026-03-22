# CIR SDE and Square-Root Process

The Cox-Ingersoll-Ross (CIR) model, introduced by Cox, Ingersoll, and Ross in 1985, modifies the Vasicek model by replacing the constant diffusion coefficient with a square-root function of the short rate. This seemingly small change has profound consequences: the model prevents negative interest rates (under appropriate parameter conditions), produces level-dependent volatility consistent with empirical observation, and connects to the non-central chi-squared distribution rather than the Gaussian. The CIR process reappears as the variance dynamics in the Heston stochastic volatility model, making it one of the most widely used diffusions in quantitative finance.

---

## The CIR stochastic differential equation

Under the risk-neutral measure $\mathbb{Q}$, the CIR short rate satisfies

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
$$

where:

- $r_t \geq 0$ is the instantaneous short rate
- $\kappa > 0$ is the **mean-reversion speed**
- $\theta > 0$ is the **long-run mean** level
- $\sigma > 0$ is the **volatility parameter** (sometimes called the "vol of vol" by analogy with Heston)
- $W_t$ is a standard Brownian motion under $\mathbb{Q}$

### Parameter interpretation

The drift $\kappa(\theta - r_t)$ is identical to the Vasicek drift: when $r_t > \theta$ the drift is negative (pulling rates down), and when $r_t < \theta$ the drift is positive (pushing rates up). The half-life of mean reversion is $\ln 2 / \kappa$.

The critical difference from Vasicek is the diffusion coefficient $\sigma\sqrt{r_t}$:

- When $r_t$ is large, the volatility is large: $\text{Vol}(dr_t) \approx \sigma\sqrt{r_t}\,\sqrt{dt}$
- When $r_t$ is near zero, the volatility vanishes: $\sigma\sqrt{r_t} \to 0$
- This **level-dependent volatility** matches the empirical observation that interest rate volatility increases with the level of rates

---

## Non-negativity of the short rate

### Intuitive argument

When $r_t$ approaches zero from above, two effects compete:

1. The **drift** $\kappa(\theta - r_t) \to \kappa\theta > 0$ pushes the rate upward
2. The **diffusion** $\sigma\sqrt{r_t} \to 0$ vanishes, eliminating downward random shocks

The vanishing diffusion at zero means that the process cannot be driven below zero by the Brownian noise. Whether the process actually reaches zero depends on the relative strength of the drift versus the diffusion near zero, captured by the Feller condition (discussed in the next section).

### Formal non-negativity

If $r_0 > 0$, the solution remains non-negative: $r_t \geq 0$ for all $t \geq 0$ almost surely. This follows from the comparison theorem for SDEs, since the CIR process dominates the process $dr_t = -\kappa\,r_t\,dt$ (which is non-negative) when $r_t$ is small.

More precisely, the boundary $r = 0$ is classified as:

- **Entrance boundary** (inaccessible) if $2\kappa\theta \geq \sigma^2$ (the Feller condition)
- **Regular boundary** (accessible, instantly reflecting) if $2\kappa\theta < \sigma^2$

In either case, the process remains non-negative. The Feller condition determines only whether zero is reached, not whether the process goes negative (it never does).

---

## Existence and uniqueness of solutions

### The Lipschitz problem

The standard existence-uniqueness theorem for SDEs requires the drift and diffusion to be globally Lipschitz. The CIR diffusion $\sigma\sqrt{r}$ is not Lipschitz at $r = 0$ (since $|\sqrt{x} - \sqrt{y}| \leq |x - y|/(\sqrt{x} + \sqrt{y})$ diverges near zero).

### Yamada-Watanabe conditions

Nevertheless, the CIR SDE has a **unique strong solution** by the Yamada-Watanabe theorem. The key condition is that the diffusion coefficient $h(r) = \sigma\sqrt{r}$ satisfies

$$
|h(x) - h(y)| \leq C\,|x - y|^\alpha \quad \text{for some } \alpha \geq 1/2
$$

Since $|\sqrt{x} - \sqrt{y}| \leq \sqrt{|x - y|}$, the condition holds with $\alpha = 1/2$ and $C = \sigma$. Combined with the linear growth of the drift, this guarantees pathwise uniqueness and strong existence.

---

## Conditional moments

### Conditional mean

Taking the expectation of the SDE:

$$
\frac{d}{dt}\mathbb{E}[r_t] = \kappa(\theta - \mathbb{E}[r_t])
$$

This is the same ODE as for Vasicek, with solution:

$$
\mathbb{E}[r_t \mid r_0] = \theta + (r_0 - \theta)\,e^{-\kappa t}
$$

The conditional mean is identical to the Vasicek mean: both models have the same mean-reversion dynamics.

### Conditional variance

The variance calculation is more involved because the diffusion is state-dependent. Applying Ito's lemma to $r_t^2$:

$$
d(r_t^2) = 2r_t\,dr_t + (dr_t)^2 = 2r_t\,\kappa(\theta - r_t)\,dt + 2\sigma r_t^{3/2}\,dW_t + \sigma^2 r_t\,dt
$$

Taking expectations and using $\text{Var}(r_t) = \mathbb{E}[r_t^2] - (\mathbb{E}[r_t])^2$, one obtains after calculation:

$$
\text{Var}(r_t \mid r_0) = r_0\,\frac{\sigma^2}{\kappa}\!\left(e^{-\kappa t} - e^{-2\kappa t}\right) + \theta\,\frac{\sigma^2}{2\kappa}\!\left(1 - e^{-\kappa t}\right)^2
$$

**Key differences from Vasicek:**

- The variance depends on $r_0$ (not just on time)
- For $r_0 = 0$: $\text{Var}(r_t) = \theta\sigma^2(1 - e^{-\kappa t})^2/(2\kappa)$
- For $r_0 = \theta$: $\text{Var}(r_t) = \theta\sigma^2(1 - e^{-2\kappa t})/(2\kappa)$ (matches Vasicek with $\sigma_{\text{Vas}}^2 = \sigma^2\theta$)

### Stationary distribution moments

As $t \to \infty$:

$$
\mathbb{E}[r_\infty] = \theta, \qquad \text{Var}(r_\infty) = \frac{\theta\sigma^2}{2\kappa}
$$

The stationary mean is $\theta$ (same as Vasicek), but the stationary variance $\theta\sigma^2/(2\kappa)$ depends on the level $\theta$, reflecting the level-dependent volatility.

---

## Comparison with Vasicek

| Property | Vasicek | CIR |
|---|---|---|
| SDE | $dr = \kappa(\theta - r)\,dt + \sigma\,dW$ | $dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW$ |
| Diffusion | Constant: $\sigma$ | State-dependent: $\sigma\sqrt{r}$ |
| Negative rates | Possible | Impossible ($r_t \geq 0$) |
| Distribution | Gaussian | Non-central $\chi^2$ (scaled) |
| Conditional mean | $\theta + (r_0 - \theta)e^{-\kappa t}$ | Same |
| Conditional variance | $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$ | $r_0\frac{\sigma^2}{\kappa}(e^{-\kappa t} - e^{-2\kappa t}) + \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa t})^2$ |
| Bond price form | $A(\tau)\,e^{-B(\tau)\,r}$ | Same (but different $A$, $B$) |
| Analytical options | Black-Scholes type | Non-central $\chi^2$ |

---

## Connection to the Heston model

The CIR process appears as the **variance dynamics** in the Heston (1993) stochastic volatility model:

$$
dv_t = \kappa_v(\theta_v - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^v
$$

where $v_t$ is the instantaneous variance of an asset. The same Feller condition $2\kappa_v\theta_v \geq \sigma_v^2$ ensures that variance stays positive. The analytical tractability of CIR (affine structure, known characteristic function) is the key reason Heston admits semi-closed-form option pricing via Fourier inversion.

---

## Numerical example

Parameters: $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.1$, $r_0 = 0.03$.

**Feller ratio**: $2\kappa\theta/\sigma^2 = 2 \times 0.5 \times 0.04 / 0.01 = 4.0 > 1$. The Feller condition is satisfied, so zero is inaccessible.

**Moments at various horizons:**

| $t$ | $\mathbb{E}[r_t]$ | $\text{Var}(r_t)^{1/2}$ |
|:-:|:-:|:-:|
| 0.5 | 3.22% | 0.99% |
| 1 | 3.39% | 1.20% |
| 5 | 3.96% | 1.41% |
| 10 | 4.00% | 1.41% |
| $\infty$ | 4.00% | 1.41% |

The stationary standard deviation is $\sqrt{\theta\sigma^2/(2\kappa)} = \sqrt{0.04 \times 0.01 / 1.0} = 2.0\%$. Note: this is $\sqrt{0.0004} = 0.02 = 2.0\%$.

---

## Summary

The CIR model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$ replaces the Vasicek constant diffusion with $\sigma\sqrt{r_t}$, ensuring non-negative rates and producing level-dependent volatility. The conditional mean is the same as Vasicek, but the variance depends on the initial rate $r_0$. Strong existence and uniqueness hold by the Yamada-Watanabe theorem despite the non-Lipschitz diffusion at zero. The Feller condition $2\kappa\theta \geq \sigma^2$ determines whether zero is accessible, and the CIR process reappears as the variance dynamics in the Heston model.

---
