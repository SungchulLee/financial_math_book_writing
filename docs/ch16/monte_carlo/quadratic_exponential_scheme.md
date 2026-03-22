# Quadratic-Exponential Scheme (Andersen)

Euler and Milstein schemes discretize the CIR variance SDE step-by-step, accumulating discretization bias over many small increments. A fundamentally different approach is to **match the exact conditional moments** of the CIR transition distribution, producing a discrete sample $v_{n+1}$ whose first two moments agree with the true distribution $v(t_{n+1}) \mid v(t_n)$. Andersen's (2008) **quadratic-exponential (QE) scheme** implements this idea by switching between two simple approximations depending on the shape of the conditional distribution. The result is near-exact accuracy for the variance process at a computational cost barely exceeding Euler.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Compute the exact conditional mean and variance of the CIR transition
    2. Derive the switching criterion based on the coefficient of variation $\psi = s^2 / m^2$
    3. Implement both the quadratic (small $\psi$) and exponential (large $\psi$) approximations with moment matching
    4. Construct the full QE algorithm including the log-price update

!!! tip "Prerequisites"
    This section uses the [CIR transition distribution](../variance_dynamics/non_central_chi_squared.md) and builds on the [Euler](euler_discretization_and_pitfalls.md) and [Milstein](milstein_scheme.md) sections.

---

## Exact Conditional Moments of CIR

The CIR variance process has a known transition distribution (non-central chi-squared), from which the conditional moments follow in closed form. Given $v_n = v(t_n)$, the moments of $v_{n+1} = v(t_{n+1})$ with $\Delta t = t_{n+1} - t_n$ are:

**Conditional mean:**

$$
m = \mathbb{E}[v_{n+1} \mid v_n] = \theta + (v_n - \theta) e^{-\kappa \Delta t}
$$

**Conditional variance:**

$$
s^2 = \text{Var}[v_{n+1} \mid v_n] = \frac{v_n \xi^2 e^{-\kappa \Delta t}}{\kappa}\left(1 - e^{-\kappa \Delta t}\right) + \frac{\theta \xi^2}{2\kappa}\left(1 - e^{-\kappa \Delta t}\right)^2
$$

These moments are exact --- they come directly from the non-central chi-squared transition density, not from any approximation.

---

## The Switching Criterion

The key observation behind the QE scheme is that the shape of the conditional distribution $v_{n+1} \mid v_n$ changes qualitatively depending on the ratio:

$$
\psi = \frac{s^2}{m^2}
$$

This is the squared **coefficient of variation** of the conditional distribution.

- When $\psi$ is **small** (say $\psi \leq \psi_c$), the conditional distribution is roughly symmetric around $m$, resembling a shifted chi-squared with many degrees of freedom. A **quadratic** (squared Gaussian) approximation works well.
- When $\psi$ is **large** ($\psi > \psi_c$), the conditional distribution has significant probability mass near zero and a heavy right tail. An **exponential** approximation captures this shape.

Andersen recommends the threshold $\psi_c = 1.5$, though values between 1 and 2 give similar performance.

---

## Quadratic Approximation (Small Psi)

When $\psi \leq \psi_c$, approximate $v_{n+1}$ as a quadratic function of a standard normal:

$$
v_{n+1} = a(b + Z_v)^2
$$

where $Z_v \sim N(0,1)$ and the parameters $a > 0$, $b \geq 0$ are chosen to match the first two moments.

**Moment matching**: The mean and variance of $a(b + Z_v)^2$ are:

$$
\mathbb{E}[a(b + Z_v)^2] = a(b^2 + 1), \qquad \text{Var}[a(b + Z_v)^2] = 2a^2(1 + 2b^2)
$$

Setting these equal to $m$ and $s^2$ and solving:

$$
b^2 = \frac{2}{\psi} - 1 + \sqrt{\frac{2}{\psi}} \sqrt{\frac{2}{\psi} - 1} \geq 0 \quad (\text{valid when } \psi \leq 2)
$$

$$
a = \frac{m}{1 + b^2}
$$

!!! note "Why Quadratic?"
    The non-central chi-squared distribution with many degrees of freedom is well-approximated by a squared Gaussian. Since $v_{n+1}$ has $d = 4\kappa\theta/\xi^2$ degrees of freedom, this approximation improves as $d$ increases---which corresponds to small $\psi$ (large mean relative to variance).

---

## Exponential Approximation (Large Psi)

When $\psi > \psi_c$, the conditional distribution concentrates near zero with a long right tail. Approximate $v_{n+1}$ using a mixture of a point mass at zero and an exponential:

$$
v_{n+1} = \begin{cases} 0 & \text{with probability } p \\ \beta^{-1} \ln\!\left(\frac{1 - p}{1 - U}\right) & \text{with probability } 1 - p \end{cases}
$$

where $U \sim \text{Uniform}(0,1)$ and the parameters $p \in [0,1)$, $\beta > 0$ are chosen to match moments.

**Moment matching**: The mean and variance of this mixture are:

$$
\mathbb{E}[v_{n+1}] = \frac{1-p}{\beta}, \qquad \text{Var}[v_{n+1}] = \frac{(1-p)(2-p)}{\beta^2}
$$

Solving:

$$
p = \frac{\psi - 1}{\psi + 1}, \qquad \beta = \frac{1 - p}{m} = \frac{2}{m(\psi + 1)}
$$

The constraint $p \geq 0$ requires $\psi \geq 1$, which is satisfied whenever we enter this branch ($\psi > \psi_c \geq 1$).

**Sampling**: Draw $U \sim \text{Uniform}(0,1)$. If $U \leq p$, set $v_{n+1} = 0$. Otherwise, set:

$$
v_{n+1} = \beta^{-1} \ln\!\left(\frac{1 - p}{1 - U}\right)
$$

---

## Log-Price Update

Having sampled $v_{n+1}$, the log-price $x = \ln S$ must be updated consistently. The QE scheme uses a **martingale-correcting** approach. Over the interval $[t_n, t_{n+1}]$, the exact log-price increment is:

$$
x_{n+1} - x_n = (r - q)\Delta t - \frac{1}{2}\int_{t_n}^{t_{n+1}} v_s \, ds + \int_{t_n}^{t_{n+1}} \sqrt{v_s} \, dW_s^{(1)}
$$

The integrated variance $\int v_s \, ds$ is approximated by the trapezoidal rule:

$$
\int_{t_n}^{t_{n+1}} v_s \, ds \approx \frac{\Delta t}{2}(v_n + v_{n+1})
$$

The stochastic integral is approximated using the correlation structure:

$$
\int_{t_n}^{t_{n+1}} \sqrt{v_s} \, dW_s^{(1)} \approx \rho \int_{t_n}^{t_{n+1}} \sqrt{v_s} \, dW_s^{(2)} + \sqrt{1 - \rho^2} \int_{t_n}^{t_{n+1}} \sqrt{v_s} \, dW_s^{(\perp)}
$$

The first integral is linked to the variance increment:

$$
\int_{t_n}^{t_{n+1}} \sqrt{v_s} \, dW_s^{(2)} = \frac{1}{\xi}\left[v_{n+1} - v_n - \kappa(\theta - v_n)\Delta t + \kappa \int_{t_n}^{t_{n+1}} v_s \, ds \right]
$$

The second integral involves the independent Brownian motion $W^{(\perp)}$ and is approximated as $\sqrt{(1-\rho^2) \Delta t \cdot \frac{1}{2}(v_n + v_{n+1})} \, Z_x$ where $Z_x \sim N(0,1)$ is independent of $Z_v$.

The complete log-price update is:

$$
x_{n+1} = x_n + K_0 + K_1 v_n + K_2 v_{n+1} + \sqrt{K_3 v_n + K_4 v_{n+1}} \, Z_x
$$

where the constants are:

$$
K_0 = (r - q)\Delta t + \frac{\rho}{\xi}\left[-\kappa\theta\Delta t\right]
$$

$$
K_1 = \frac{\Delta t}{2}\left(\kappa\frac{\rho}{\xi} - \frac{1}{2}\right) - \frac{\rho}{\xi}
$$

$$
K_2 = \frac{\Delta t}{2}\left(\kappa\frac{\rho}{\xi} - \frac{1}{2}\right) + \frac{\rho}{\xi}
$$

$$
K_3 = \frac{\Delta t}{2}(1 - \rho^2), \qquad K_4 = \frac{\Delta t}{2}(1 - \rho^2)
$$

!!! warning "Martingale Correction"
    The constants $K_0, K_1, K_2$ must be calibrated so that $\mathbb{E}[S_{n+1} \mid \mathcal{F}_n] = S_n e^{(r-q)\Delta t}$, ensuring the discounted price is a martingale. Andersen provides the exact expressions that guarantee this property. Using the wrong constants introduces a systematic drift bias.

---

## Complete QE Algorithm

The full algorithm for one time step from $(x_n, v_n)$ to $(x_{n+1}, v_{n+1})$ is:

**Step 1**: Compute conditional moments $m$ and $s^2$ from $v_n$.

**Step 2**: Compute $\psi = s^2 / m^2$.

**Step 3**: Sample $v_{n+1}$:

- If $\psi \leq \psi_c$: compute $b^2$ and $a$, draw $Z_v \sim N(0,1)$, set $v_{n+1} = a(b + Z_v)^2$.
- If $\psi > \psi_c$: compute $p$ and $\beta$, draw $U \sim \text{Uniform}(0,1)$, apply the exponential rule.

**Step 4**: Draw $Z_x \sim N(0,1)$ independent of $Z_v$ (and $U$).

**Step 5**: Update $x_{n+1}$ using the log-price formula with constants $K_0, \ldots, K_4$.

---

## Worked Example

Consider the standard Heston parameters:

| Parameter | Value |
|-----------|-------|
| $v_0$ | $0.04$ |
| $\kappa$ | $1.5$ |
| $\theta$ | $0.04$ |
| $\xi$ | $0.3$ |
| $\Delta t$ | $1/12$ (monthly) |

**Conditional moments:**

$$
m = 0.04 + (0.04 - 0.04)e^{-1.5/12} = 0.04
$$

$$
s^2 = \frac{0.04 \cdot 0.09 \cdot e^{-1.5/12}}{1.5}(1 - e^{-1.5/12}) + \frac{0.04 \cdot 0.09}{3.0}(1 - e^{-1.5/12})^2
$$

$$
\approx 0.000219 + 0.0000178 \approx 0.000237
$$

**Switching criterion:**

$$
\psi = \frac{0.000237}{0.04^2} = \frac{0.000237}{0.0016} \approx 0.148
$$

Since $\psi = 0.148 < 1.5 = \psi_c$, we use the **quadratic approximation**:

$$
b^2 = \frac{2}{0.148} - 1 + \sqrt{\frac{2}{0.148}}\sqrt{\frac{2}{0.148} - 1} \approx 12.51 + \sqrt{13.51 \cdot 12.51} \approx 12.51 + 13.0 = 25.51
$$

$$
a = \frac{0.04}{1 + 25.51} = \frac{0.04}{26.51} \approx 0.001509
$$

Drawing $Z_v = 0.5$: $v_{n+1} = 0.001509 \cdot (5.051 + 0.5)^2 = 0.001509 \cdot 30.82 \approx 0.0465$.

??? example "Comparison: QE vs Euler (100,000 paths)"
    For a European call with $S_0 = \$100$, $K = \$100$, $T = 1$, $r = 0.05$:

    | Scheme | Steps | Price | Std Error | Bias vs Fourier |
    |--------|-------|-------|-----------|----------------|
    | Euler (full trunc.) | 252 | $\$10.31$ | $\$0.03$ | $-\$0.05$ |
    | QE | 12 | $\$10.35$ | $\$0.03$ | $-\$0.01$ |
    | QE | 52 | $\$10.36$ | $\$0.03$ | $< \$0.01$ |
    | Fourier (exact) | --- | $\$10.36$ | --- | --- |

    The QE scheme with only 12 monthly steps achieves better accuracy than Euler with 252 daily steps, a $20\times$ reduction in computational cost per path.

---

## Summary

Andersen's QE scheme matches the exact conditional mean and variance of the CIR transition at each step, switching between a quadratic (squared Gaussian) approximation when the variance is well above zero and an exponential approximation when it is near zero. The switching is controlled by the coefficient of variation $\psi = s^2/m^2$ with threshold $\psi_c \approx 1.5$. The scheme achieves near-exact accuracy for the variance distribution with minimal computational overhead, making it the **standard method** for Heston Monte Carlo in practice. For truly bias-free simulation, the [exact simulation](exact_simulation_broadie_kaya.md) method of Broadie and Kaya eliminates all discretization error.
