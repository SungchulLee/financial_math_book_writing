# Transition Densities for Standard SDEs

This section presents **explicit transition densities** for the most important diffusion processes in finance: Brownian motion with drift, geometric Brownian motion, the Ornstein-Uhlenbeck process, and the Cox-Ingersoll-Ross (CIR) process. For each process, we state the SDE, derive or verify the transition density, and discuss its financial applications.

---

## Overview

| Process | SDE | Transition Density | Distribution |
|---|---|---|---|
| **BM with drift** | $dX = \mu\,dt + \sigma\,dW$ | Gaussian | $N(\mu t, \sigma^2 t)$ |
| **GBM** | $dS = \mu S\,dt + \sigma S\,dW$ | Lognormal | $\log S \sim N$ |
| **OU** | $dX = -\kappa X\,dt + \sigma\,dW$ | Gaussian | $N(xe^{-\kappa t}, v(t))$ |
| **CIR** | $dX = \kappa(\theta - X)\,dt + \xi\sqrt{X}\,dW$ | Non-central $\chi^2$ | Scaled $\chi^2$ |

---

## Brownian Motion with Drift

### SDE and Solution

$$
dX_t = \mu\,dt + \sigma\,dW_t, \quad X_0 = x_0
$$

The solution is explicit:

$$
X_t = x_0 + \mu t + \sigma W_t
$$

### Transition Density

$$
\boxed{
p(t, x \mid 0, x_0) = \frac{1}{\sigma\sqrt{2\pi t}} \exp\!\left(-\frac{(x - x_0 - \mu t)^2}{2\sigma^2 t}\right)
}
$$

This is the density of $N(x_0 + \mu t,\, \sigma^2 t)$.

**Conditional moments:**

$$
\mathbb{E}[X_t \mid X_0 = x_0] = x_0 + \mu t, \qquad \text{Var}(X_t \mid X_0 = x_0) = \sigma^2 t
$$

### Derivation

Since $X_t - x_0 = \mu t + \sigma W_t$ and $W_t \sim N(0, t)$, we have $X_t \sim N(x_0 + \mu t, \sigma^2 t)$ immediately from the properties of the normal distribution. $\square$

### Verification via Fokker-Planck

The Fokker-Planck equation for this process is:

$$
\frac{\partial p}{\partial t} = -\mu\frac{\partial p}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}
$$

Substituting the Gaussian density and verifying both sides match confirms the result.

---

## Geometric Brownian Motion

### SDE and Solution

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t, \quad S_0 = s_0
$$

By Ito's lemma applied to $\log S_t$:

$$
S_t = s_0\exp\!\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)
$$

### Transition Density

$$
\boxed{
p(t, S \mid 0, s_0) = \frac{1}{S\sigma\sqrt{2\pi t}} \exp\!\left(-\frac{(\log(S/s_0) - (\mu - \sigma^2/2)t)^2}{2\sigma^2 t}\right)
}
$$

This is the **lognormal density**: $\log S_t \sim N\!\left(\log s_0 + (\mu - \sigma^2/2)t,\, \sigma^2 t\right)$.

**Conditional moments:**

$$
\mathbb{E}[S_t \mid S_0 = s_0] = s_0\,e^{\mu t}
$$

$$
\text{Var}(S_t \mid S_0 = s_0) = s_0^2\,e^{2\mu t}\left(e^{\sigma^2 t} - 1\right)
$$

### Derivation

Set $Y_t = \log S_t$. By Ito's lemma:

$$
dY_t = \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
$$

So $Y_t$ is Brownian motion with drift, and $Y_t \sim N(\log s_0 + (\mu - \sigma^2/2)t, \sigma^2 t)$. The density of $S_t = e^{Y_t}$ follows from the change-of-variables formula:

$$
p_S(S) = p_Y(\log S) \cdot \frac{1}{S}
$$

$\square$

!!! note "The Ito Correction"
    The drift of $\log S_t$ is $\mu - \sigma^2/2$, not $\mu$. The correction $-\sigma^2/2$ arises from the second-order (Ito) term in the stochastic calculus of $\log S$. This is the most common source of errors in financial calculations involving GBM.

### Financial Application

Under the risk-neutral measure ($\mu \to r$), the GBM transition density gives the **Black-Scholes formula** when integrated against the payoff:

$$
C(0, s_0) = e^{-rT}\int_K^{\infty}(S - K)\,p^{\mathbb{Q}}(T, S \mid 0, s_0)\,dS = s_0\Phi(d_1) - Ke^{-rT}\Phi(d_2)
$$

---

## Ornstein-Uhlenbeck Process

### SDE and Solution

$$
dX_t = -\kappa(X_t - \theta)\,dt + \sigma\,dW_t, \quad X_0 = x_0
$$

where $\kappa > 0$ is the mean-reversion speed and $\theta$ is the long-run mean.

The solution (by the integrating factor method):

$$
X_t = \theta + (x_0 - \theta)e^{-\kappa t} + \sigma\int_0^t e^{-\kappa(t-s)}\,dW_s
$$

### Transition Density

$$
\boxed{
p(t, x \mid 0, x_0) = \frac{1}{\sqrt{2\pi v(t)}} \exp\!\left(-\frac{(x - m(t))^2}{2v(t)}\right)
}
$$

where the **conditional mean** and **conditional variance** are:

$$
m(t) = \theta + (x_0 - \theta)e^{-\kappa t}
$$

$$
v(t) = \frac{\sigma^2}{2\kappa}\left(1 - e^{-2\kappa t}\right)
$$

**Key properties:**

- **Mean reversion**: $m(t) \to \theta$ as $t \to \infty$
- **Variance saturation**: $v(t) \to \frac{\sigma^2}{2\kappa}$ as $t \to \infty$
- **Stationary distribution**: $X_\infty \sim N\!\left(\theta, \frac{\sigma^2}{2\kappa}\right)$

### Derivation

The stochastic integral $\sigma\int_0^t e^{-\kappa(t-s)}\,dW_s$ is Gaussian (as a linear functional of Brownian motion) with:

- Mean: $0$
- Variance: $\sigma^2\int_0^t e^{-2\kappa(t-s)}\,ds = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$

Therefore $X_t$ is Gaussian with the stated mean and variance. $\square$

### Financial Application

The OU process models **interest rates** (Vasicek model) and **log-volatility**. The explicit transition density enables:

- Closed-form bond prices in the Vasicek model
- Exact simulation (no discretization error)
- Likelihood-based parameter estimation

---

## Cox-Ingersoll-Ross (CIR) Process

### SDE

$$
dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t, \quad X_0 = x_0 > 0
$$

where $\kappa, \theta, \xi > 0$. The square-root diffusion ensures $X_t \geq 0$.

**Feller condition**: If $2\kappa\theta \geq \xi^2$, then $X_t > 0$ almost surely (the process never reaches zero).

### Transition Density

$$
\boxed{
p(t, x \mid 0, x_0) = c\,e^{-u-v}\left(\frac{v}{u}\right)^{q/2} I_q\!\left(2\sqrt{uv}\right)
}
$$

where:

$$
c = \frac{2\kappa}{\xi^2(1 - e^{-\kappa t})}, \quad u = c\,x_0\,e^{-\kappa t}, \quad v = c\,x, \quad q = \frac{2\kappa\theta}{\xi^2} - 1
$$

and $I_q$ is the **modified Bessel function of the first kind** of order $q$.

### Equivalent Characterization

The transition distribution can be expressed as a **scaled non-central chi-squared**:

$$
2c\,X_t \mid X_0 = x_0 \;\sim\; \chi^2\!\left(\delta,\, \lambda\right)
$$

where:

- Degrees of freedom: $\delta = \frac{4\kappa\theta}{\xi^2}$
- Non-centrality parameter: $\lambda = 2u = \frac{4\kappa x_0 e^{-\kappa t}}{\xi^2(1 - e^{-\kappa t})}$

**Conditional moments:**

$$
\mathbb{E}[X_t \mid X_0 = x_0] = \theta + (x_0 - \theta)e^{-\kappa t}
$$

$$
\text{Var}(X_t \mid X_0 = x_0) = \frac{x_0\xi^2 e^{-\kappa t}(1 - e^{-\kappa t})}{\kappa} + \frac{\theta\xi^2(1 - e^{-\kappa t})^2}{2\kappa}
$$

### Derivation Sketch

**Step 1**: Compute the moment-generating function $M(\alpha) = \mathbb{E}[e^{\alpha X_t} \mid X_0 = x_0]$ by solving the Feynman-Kac PDE:

$$
\frac{\partial M}{\partial t} + \kappa(\theta - x)\frac{\partial M}{\partial x} + \frac{\xi^2 x}{2}\frac{\partial^2 M}{\partial x^2} = 0, \quad M(T, x) = e^{\alpha x}
$$

**Step 2**: Use the affine structure (guess $M = \exp(A(t) + B(t)x)$) to reduce to Riccati ODEs for $A(t)$ and $B(t)$.

**Step 3**: Identify the resulting MGF as that of a non-central chi-squared distribution. $\square$

### Stationary Distribution

As $t \to \infty$:

$$
X_\infty \sim \text{Gamma}\!\left(\frac{2\kappa\theta}{\xi^2},\, \frac{\xi^2}{2\kappa}\right)
$$

with mean $\theta$ and variance $\frac{\theta\xi^2}{2\kappa}$.

### Financial Application

The CIR process models:

- **Interest rates** (CIR short-rate model): $r_t$ follows CIR, and bond prices have closed-form affine solutions
- **Stochastic volatility** (Heston model): The variance $v_t$ follows CIR, enabling semi-analytical option pricing via characteristic functions

---

## Comparison of Transition Densities

| Property | BM with Drift | GBM | OU | CIR |
|---|---|---|---|---|
| **Support** | $\mathbb{R}$ | $(0, \infty)$ | $\mathbb{R}$ | $[0, \infty)$ |
| **Distribution** | Normal | Lognormal | Normal | Non-central $\chi^2$ |
| **Mean reversion** | No | No | Yes | Yes |
| **Stationary dist.** | None | None | Normal | Gamma |
| **Exact simulation** | Yes | Yes | Yes | Yes (via $\chi^2$) |
| **Closed-form density** | Yes | Yes | Yes | Yes (Bessel function) |

---

## General Derivation Methods

When a closed-form density is not immediately obvious, several systematic methods can be employed:

### 1. Solve the Fokker-Planck Equation Directly

Write $\partial_t p = \mathcal{L}^* p$ and solve using Fourier or Laplace transforms.

### 2. Characteristic Function / Moment-Generating Function

Compute $\hat{p}(\xi, t) = \mathbb{E}[e^{i\xi X_t} \mid X_0 = x_0]$ by solving the backward PDE for $\hat{p}$, then invert.

### 3. Change of Variables

Transform the SDE to one with known density (e.g., Lamperti transform to remove state-dependent diffusion).

### 4. Affine Structure

For affine SDEs ($\mu$ and $\sigma^2$ are affine in $x$), the characteristic function is exponential-affine, leading to Riccati ODEs.

!!! tip "The Affine Shortcut"
    GBM, OU, and CIR are all **affine processes**. Their characteristic functions have the form $\mathbb{E}[e^{i\xi X_t}] = \exp(A(t,\xi) + B(t,\xi)x_0)$, where $A$ and $B$ solve coupled Riccati equations. This structure enables closed-form (or semi-analytical) pricing for a wide range of derivatives.

---

## Summary

| Process | Transition Density | Key Feature |
|---|---|---|
| **BM with drift** | $N(x_0 + \mu t,\, \sigma^2 t)$ | Linear growth, no mean reversion |
| **GBM** | Lognormal($\log s_0 + (\mu-\sigma^2/2)t,\, \sigma^2 t$) | Multiplicative noise, positive |
| **OU** | $N(\theta + (x_0-\theta)e^{-\kappa t},\, v(t))$ | Mean-reverting, Gaussian |
| **CIR** | Non-central $\chi^2$ (scaled) | Mean-reverting, non-negative |

$$
\boxed{
\text{Explicit transition densities enable closed-form pricing, exact simulation, and likelihood estimation}
}
$$

**Knowing the transition density of a financial model is equivalent to knowing its Green's function. These explicit formulas are the workhorses of quantitative finance: they provide the analytical foundation for pricing, calibration, and risk management.**

---

## See Also

- [Kolmogorov Forward Equation](kolmogorov_forward.md) -- the PDE that transition densities satisfy
- [Kolmogorov Backward Equation](kolmogorov_backward.md) -- the PDE for expected values
- [Transition Density as Green's Function](../greens_functions/transition_density_as_greens_function.md) -- the PDE-probability connection
- [Feynman-Kac Formula](../feynman_kac/feynman_kac_formula.md) -- adding discounting to expectations
- [Fokker-Planck for Financial Models](fokker_planck_financial_models.md) -- applied Fokker-Planck equations
