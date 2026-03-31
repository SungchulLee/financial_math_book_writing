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

---

## Exercises

**Exercise 1.**
For Brownian motion with drift $dX_t = \mu\,dt + \sigma\,dW_t$, compute $\mathbb{E}[X_t^3 \mid X_0 = x_0]$ using the explicit solution $X_t = x_0 + \mu t + \sigma W_t$. Verify your answer by checking that $u(t, x) = \mathbb{E}_x[X_t^3]$ satisfies the backward equation $\partial_t u = \mu\partial_x u + \frac{\sigma^2}{2}\partial_{xx} u$.

---

**Exercise 2.**
For geometric Brownian motion $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$, derive the variance formula

$$
\text{Var}(S_t \mid S_0 = s_0) = s_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)
$$

by first computing $\mathbb{E}[S_t^2]$ using the moment-generating function of the normal distribution. Why does the variance grow exponentially even though $\log S_t$ has variance that grows only linearly?

---

**Exercise 3.**
For the Ornstein-Uhlenbeck process $dX_t = -\kappa(X_t - \theta)\,dt + \sigma\,dW_t$, use the explicit solution

$$
X_t = \theta + (x_0 - \theta)e^{-\kappa t} + \sigma\int_0^t e^{-\kappa(t-s)}\,dW_s
$$

to derive the conditional mean $m(t) = \theta + (x_0 - \theta)e^{-\kappa t}$ and variance $v(t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$. Verify that the variance saturates at $\sigma^2/(2\kappa)$ as $t \to \infty$.

---

**Exercise 4.**
The CIR process $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ has conditional mean $\mathbb{E}[X_t \mid X_0 = x_0] = \theta + (x_0 - \theta)e^{-\kappa t}$, identical to the OU process. Explain why the means coincide despite the processes being quite different. Compute the conditional variance of the CIR process and compare it to the OU variance.

---

**Exercise 5.**
The Feller condition $2\kappa\theta \geq \xi^2$ ensures that the CIR process stays strictly positive. Interpret this condition in terms of the balance between mean reversion (pulling toward $\theta > 0$) and volatility (pushing toward zero). What happens to the transition density near $x = 0$ when the Feller condition is violated?

---

**Exercise 6.**
For the GBM transition density under the risk-neutral measure ($\mu \to r$), derive the Black-Scholes call price by evaluating

$$
C(0, s_0) = e^{-rT}\int_K^{\infty}(S - K)\,p^{\mathbb{Q}}(T, S \mid 0, s_0)\,dS
$$

Show that the integral splits into two terms involving the cumulative normal distribution $\Phi$, yielding $C = s_0\Phi(d_1) - Ke^{-rT}\Phi(d_2)$.

---

**Exercise 7.**
All four processes discussed (BM with drift, GBM, OU, CIR) are affine processes: their characteristic functions have the form $\mathbb{E}[e^{i\xi X_t}] = \exp(A(t, \xi) + B(t, \xi)x_0)$. For the OU process, compute the characteristic function by using the Gaussian transition density and verify the exponential-affine form. Identify $A(t, \xi)$ and $B(t, \xi)$ explicitly.

---

## Solutions

??? success "Solution to Exercise 1"
    The explicit solution is $X_t = x_0 + \mu t + \sigma W_t$. We compute:

    $$
    X_t^3 = (x_0 + \mu t + \sigma W_t)^3
    $$

    Expanding the cube with $a = x_0 + \mu t$ and $Z = \sigma W_t$:

    $$
    X_t^3 = a^3 + 3a^2 Z + 3a Z^2 + Z^3
    $$

    Taking expectations, using $\mathbb{E}[Z] = 0$, $\mathbb{E}[Z^2] = \sigma^2 t$, and $\mathbb{E}[Z^3] = 0$ (odd moments of a Gaussian vanish):

    $$
    \mathbb{E}[X_t^3 \mid X_0 = x_0] = a^3 + 3a\sigma^2 t = (x_0 + \mu t)^3 + 3(x_0 + \mu t)\sigma^2 t
    $$

    So $u(t, x) = (x + \mu t)^3 + 3(x + \mu t)\sigma^2 t$.

    **Verification via the backward equation** $\partial_t u = \mu\partial_x u + \frac{\sigma^2}{2}\partial_{xx}u$:

    Let $a(t) = x + \mu t$. Then $u = a^3 + 3a\sigma^2 t$.

    $$
    \frac{\partial u}{\partial t} = 3a^2\mu + 3\mu\sigma^2 t + 3a\sigma^2 = 3\mu a^2 + 3\sigma^2(a + \mu t)
    $$

    $$
    \frac{\partial u}{\partial x} = 3a^2 + 3\sigma^2 t, \qquad \frac{\partial^2 u}{\partial x^2} = 6a
    $$

    $$
    \mu\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2} = \mu(3a^2 + 3\sigma^2 t) + \frac{\sigma^2}{2}\cdot 6a = 3\mu a^2 + 3\mu\sigma^2 t + 3\sigma^2 a
    $$

    This equals $\partial_t u$. $\checkmark$

??? success "Solution to Exercise 2"
    For GBM, $S_t = s_0\exp((\mu - \sigma^2/2)t + \sigma W_t)$. Therefore:

    $$
    S_t^2 = s_0^2\exp(2(\mu - \sigma^2/2)t + 2\sigma W_t) = s_0^2\exp((2\mu - \sigma^2)t + 2\sigma W_t)
    $$

    Taking expectations and using the MGF of the normal distribution ($\mathbb{E}[e^{cW_t}] = e^{c^2 t/2}$ for any constant $c$):

    $$
    \mathbb{E}[S_t^2] = s_0^2 e^{(2\mu - \sigma^2)t}\cdot\mathbb{E}[e^{2\sigma W_t}] = s_0^2 e^{(2\mu - \sigma^2)t}\cdot e^{2\sigma^2 t} = s_0^2 e^{(2\mu + \sigma^2)t}
    $$

    Since $\mathbb{E}[S_t] = s_0 e^{\mu t}$:

    $$
    \text{Var}(S_t) = \mathbb{E}[S_t^2] - (\mathbb{E}[S_t])^2 = s_0^2 e^{(2\mu + \sigma^2)t} - s_0^2 e^{2\mu t} = s_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)
    $$

    **Why the variance grows exponentially despite linear variance growth in log-space**: The variance of $\log S_t$ is $\sigma^2 t$, which grows linearly. However, the exponential map $S_t = e^{Y_t}$ is a convex transformation. By Jensen's inequality and the properties of the lognormal distribution, the variance of $e^Y$ depends on $e^{\text{Var}(Y)}$, not $\text{Var}(Y)$ itself. Specifically, $\text{Var}(e^Y) = e^{2\mu_Y + \sigma_Y^2}(e^{\sigma_Y^2} - 1)$. As $\sigma_Y^2 = \sigma^2 t$ grows linearly, the factor $e^{\sigma^2 t}$ causes exponential growth of $\text{Var}(S_t)$. This reflects the right-skewness and heavy right tail of the lognormal distribution: extreme upward moves contribute disproportionately to the variance.

??? success "Solution to Exercise 3"
    From the explicit solution:

    $$
    X_t = \theta + (x_0 - \theta)e^{-\kappa t} + \sigma\int_0^t e^{-\kappa(t-s)}\,dW_s
    $$

    **Conditional mean**: The stochastic integral has mean zero, so:

    $$
    m(t) = \mathbb{E}[X_t \mid X_0 = x_0] = \theta + (x_0 - \theta)e^{-\kappa t}
    $$

    **Conditional variance**: By the Ito isometry:

    $$
    v(t) = \text{Var}\left(\sigma\int_0^t e^{-\kappa(t-s)}\,dW_s\right) = \sigma^2\int_0^t e^{-2\kappa(t-s)}\,ds
    $$

    Evaluating the integral with substitution $u = t - s$:

    $$
    v(t) = \sigma^2\int_0^t e^{-2\kappa u}\,du = \sigma^2\left[-\frac{1}{2\kappa}e^{-2\kappa u}\right]_0^t = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    **Variance saturation**: As $t \to \infty$, the exponential $e^{-2\kappa t} \to 0$, so:

    $$
    v(\infty) = \frac{\sigma^2}{2\kappa}
    $$

    This makes physical sense: mean reversion (strength $\kappa$) confines the process, preventing the variance from growing without bound. Stronger mean reversion (larger $\kappa$) gives a smaller asymptotic variance, while larger noise ($\sigma$) increases it.

??? success "Solution to Exercise 4"
    **Why the conditional means coincide**: The conditional mean $\mathbb{E}[X_t \mid X_0 = x_0]$ depends only on the drift term of the SDE, since the stochastic integral always has zero mean. Both the OU process $dX_t = -\kappa(X_t - \theta)\,dt + \sigma\,dW_t$ and the CIR process $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ have the same drift structure $\kappa(\theta - X_t)$. The mean satisfies the ODE:

    $$
    \frac{d}{dt}\mathbb{E}[X_t] = \kappa(\theta - \mathbb{E}[X_t])
    $$

    which gives $\mathbb{E}[X_t] = \theta + (x_0 - \theta)e^{-\kappa t}$ regardless of the diffusion coefficient. The diffusion coefficient affects the variance and higher moments but not the mean.

    **CIR conditional variance**: For the CIR process, define $V(t) = \text{Var}(X_t \mid X_0 = x_0)$. Using Ito's lemma on $X_t^2$:

    $$
    d(X_t^2) = 2X_t\,dX_t + \xi^2 X_t\,dt = [2\kappa\theta X_t - 2\kappa X_t^2 + \xi^2 X_t]\,dt + 2\xi X_t^{3/2}\,dW_t
    $$

    Taking expectations:

    $$
    \frac{d}{dt}\mathbb{E}[X_t^2] = (2\kappa\theta + \xi^2)\mathbb{E}[X_t] - 2\kappa\mathbb{E}[X_t^2]
    $$

    Using $V(t) = \mathbb{E}[X_t^2] - m(t)^2$, one obtains (after algebra):

    $$
    V(t) = \frac{x_0\xi^2 e^{-\kappa t}(1 - e^{-\kappa t})}{\kappa} + \frac{\theta\xi^2(1 - e^{-\kappa t})^2}{2\kappa}
    $$

    **Comparison**: The OU variance $v_{OU}(t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$ depends only on $\sigma$ and $\kappa$, not on $x_0$. The CIR variance depends on $x_0$ because the diffusion coefficient $\xi\sqrt{X_t}$ is state-dependent: starting from a larger $x_0$ means more noise initially. As $t \to \infty$, both variances converge to their stationary values: $\sigma^2/(2\kappa)$ for OU and $\theta\xi^2/(2\kappa)$ for CIR.

??? success "Solution to Exercise 5"
    The Feller condition $2\kappa\theta \geq \xi^2$ balances two competing forces:

    - **Mean reversion** $\kappa(\theta - X_t)$: When $X_t$ is near zero, the drift is approximately $\kappa\theta > 0$, pushing the process upward.
    - **Volatility** $\xi\sqrt{X_t}$: Near $X_t = 0$, the volatility vanishes (since $\sqrt{X_t} \to 0$), which helps keep the process positive. However, the relative strength of volatility compared to drift matters.

    The Feller condition can be rewritten as $\kappa\theta \geq \xi^2/2$. The left side measures the upward pull when $X_t \approx 0$, while the right side measures the tendency of diffusion to push the process toward zero (recall that in the Ito convention, the "effective drift" from the diffusion term contributes a downward push near zero).

    **When the Feller condition is violated** ($2\kappa\theta < \xi^2$): The process can reach zero. The transition density near $x = 0$ behaves as:

    $$
    p(t, x \mid 0, x_0) \sim x^{q}, \qquad q = \frac{2\kappa\theta}{\xi^2} - 1
    $$

    If $q < 0$ (Feller condition violated), the density diverges as $x \to 0^+$, meaning there is a significant probability mass concentrated near zero. The process touches zero with positive probability, though it is instantaneously reflected back. In the extreme case where $q \leq -1$ (i.e., $2\kappa\theta \leq 0$), the density becomes non-integrable and the process is absorbed at zero.

??? success "Solution to Exercise 6"
    Under the risk-neutral measure, $S_T$ has transition density:

    $$
    p^{\mathbb{Q}}(T, S \mid 0, s_0) = \frac{1}{S\sigma\sqrt{2\pi T}}\exp\left(-\frac{(\ln(S/s_0) - (r - \sigma^2/2)T)^2}{2\sigma^2 T}\right)
    $$

    The call price is:

    $$
    C = e^{-rT}\int_K^{\infty}(S - K)p^{\mathbb{Q}}\,dS = e^{-rT}\underbrace{\int_K^{\infty}S\,p^{\mathbb{Q}}\,dS}_{I_1} - e^{-rT}K\underbrace{\int_K^{\infty}p^{\mathbb{Q}}\,dS}_{I_2}
    $$

    **Evaluating $I_2$**: Substituting $z = \frac{\ln(S/s_0) - (r - \sigma^2/2)T}{\sigma\sqrt{T}}$:

    $$
    I_2 = \mathbb{Q}(S_T > K) = \Phi(d_2)
    $$

    where $d_2 = \frac{\ln(s_0/K) + (r - \sigma^2/2)T}{\sigma\sqrt{T}}$.

    **Evaluating $I_1$**: In the integral $\int_K^{\infty}S\,p^{\mathbb{Q}}\,dS$, multiplying $S$ by the lognormal density and completing the square in the exponent:

    $$
    S \cdot p^{\mathbb{Q}} = \frac{1}{\sigma\sqrt{2\pi T}}\exp\left(-\frac{(\ln S - \ln s_0 - (r - \sigma^2/2)T)^2}{2\sigma^2 T}\right)
    $$

    The exponent of $S$ (which equals $e^{\ln S}$) combines with the Gaussian to shift the mean by $\sigma^2 T$:

    $$
    I_1 = s_0 e^{rT}\Phi(d_1)
    $$

    where $d_1 = d_2 + \sigma\sqrt{T} = \frac{\ln(s_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$.

    **Combining:**

    $$
    C = e^{-rT}(s_0 e^{rT}\Phi(d_1) - K\Phi(d_2)) = s_0\Phi(d_1) - Ke^{-rT}\Phi(d_2)
    $$

    This is the **Black-Scholes formula**. $\checkmark$

??? success "Solution to Exercise 7"
    The OU process has transition density $X_t \mid X_0 = x_0 \sim N(m(t), v(t))$ where $m(t) = \theta + (x_0 - \theta)e^{-\kappa t}$ and $v(t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$.

    The characteristic function of a $N(m, v)$ random variable is $\mathbb{E}[e^{i\xi X}] = \exp(i\xi m - \xi^2 v/2)$. Therefore:

    $$
    \mathbb{E}[e^{i\xi X_t} \mid X_0 = x_0] = \exp\left(i\xi m(t) - \frac{\xi^2 v(t)}{2}\right)
    $$

    $$
    = \exp\left(i\xi[\theta + (x_0 - \theta)e^{-\kappa t}] - \frac{\xi^2\sigma^2}{4\kappa}(1 - e^{-2\kappa t})\right)
    $$

    Separating the terms that depend on $x_0$ from those that do not:

    $$
    = \exp\left(\underbrace{i\xi\theta(1 - e^{-\kappa t}) - \frac{\xi^2\sigma^2}{4\kappa}(1 - e^{-2\kappa t})}_{A(t, \xi)} + \underbrace{i\xi e^{-\kappa t}}_{B(t, \xi)}\cdot x_0\right)
    $$

    This confirms the exponential-affine form $\exp(A(t, \xi) + B(t, \xi)x_0)$ with:

    $$
    B(t, \xi) = i\xi e^{-\kappa t}
    $$

    $$
    A(t, \xi) = i\xi\theta(1 - e^{-\kappa t}) - \frac{\sigma^2\xi^2}{4\kappa}(1 - e^{-2\kappa t})
    $$

    Note that $B$ is linear in $\xi$ (reflecting the Gaussian nature) and decays exponentially in $t$ (reflecting mean reversion). The function $A$ contains both the contribution of $\theta$ to the mean and the variance term.
