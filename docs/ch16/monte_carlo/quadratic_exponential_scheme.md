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

---

## Exercises

**Exercise 1.**
The conditional mean of the CIR transition is $m = \theta + (v_n - \theta)e^{-\kappa\Delta t}$. Show that $m = \theta$ when $v_n = \theta$ (the variance is at its long-run level), $m > \theta$ when $v_n > \theta$, and $m < \theta$ when $v_n < \theta$. For $v_n = 0$ (variance at zero), show that $m = \theta(1 - e^{-\kappa\Delta t})$ and explain why this is strictly positive: the CIR drift pushes the variance away from zero even when the diffusion vanishes.

??? success "Solution to Exercise 1"
    The conditional mean is $m = \theta + (v_n - \theta)e^{-\kappa\Delta t}$. We verify the three cases:

    **Case** $v_n = \theta$:

    $$
    m = \theta + (\theta - \theta)e^{-\kappa\Delta t} = \theta + 0 = \theta
    $$

    When the variance is at its long-run level, the drift is zero and the expected variance remains at $\theta$.

    **Case** $v_n > \theta$: Since $e^{-\kappa\Delta t} \in (0,1)$ for $\kappa > 0$ and $\Delta t > 0$:

    $$
    m = \theta + \underbrace{(v_n - \theta)}_{> 0} \cdot \underbrace{e^{-\kappa\Delta t}}_{> 0} > \theta
    $$

    The mean reverts toward $\theta$ but remains above it: $\theta < m < v_n$.

    **Case** $v_n < \theta$: Similarly:

    $$
    m = \theta + \underbrace{(v_n - \theta)}_{< 0} \cdot \underbrace{e^{-\kappa\Delta t}}_{> 0} < \theta
    $$

    The mean reverts toward $\theta$ but remains below it: $v_n < m < \theta$.

    **Case** $v_n = 0$:

    $$
    m = \theta + (0 - \theta)e^{-\kappa\Delta t} = \theta(1 - e^{-\kappa\Delta t})
    $$

    This is strictly positive because $\theta > 0$ and $1 - e^{-\kappa\Delta t} > 0$ for any $\Delta t > 0$. The economic interpretation is that the CIR drift at $v = 0$ is $\kappa\theta > 0$, pushing the variance away from zero. Even though the diffusion coefficient $\xi\sqrt{v} = 0$ vanishes at $v = 0$, the drift alone ensures that the expected variance is positive after any finite time step. For the standard parameters with $\Delta t = 1/12$:

    $$
    m = 0.04(1 - e^{-1.5/12}) = 0.04(1 - e^{-0.125}) = 0.04 \times 0.1175 \approx 0.00470
    $$

    So even starting from zero variance, the expected variance after one month is about $0.47\%$, roughly one-eighth of the long-run level.

---

**Exercise 2.**
The switching criterion is $\psi = s^2/m^2$. For the worked example ($v_n = 0.04 = \theta$, $\kappa = 1.5$, $\xi = 0.3$, $\Delta t = 1/12$), $\psi \approx 0.148$, well below $\psi_c = 1.5$. Now consider $v_n = 0.001$ (variance near zero) with the same parameters. Recompute $m$, $s^2$, and $\psi$. Does the scheme switch to the exponential branch? At what value of $v_n$ does the transition from quadratic to exponential occur?

??? success "Solution to Exercise 2"
    With $v_n = 0.001$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\Delta t = 1/12$:

    **Conditional mean:**

    $$
    m = 0.04 + (0.001 - 0.04)e^{-1.5/12} = 0.04 - 0.039 \times 0.8825 = 0.04 - 0.03442 = 0.00558
    $$

    **Conditional variance:**

    $$
    s^2 = \frac{v_n \xi^2 e^{-\kappa\Delta t}}{\kappa}(1 - e^{-\kappa\Delta t}) + \frac{\theta\xi^2}{2\kappa}(1 - e^{-\kappa\Delta t})^2
    $$

    $$
    = \frac{0.001 \times 0.09 \times 0.8825}{1.5}(0.1175) + \frac{0.04 \times 0.09}{3.0}(0.1175)^2
    $$

    $$
    = \frac{0.0000794}{1.5}(0.1175) + 0.0012 \times 0.01381
    $$

    $$
    = 0.00000622 + 0.0000166 = 0.0000228
    $$

    **Switching criterion:**

    $$
    \psi = \frac{s^2}{m^2} = \frac{0.0000228}{0.00558^2} = \frac{0.0000228}{0.0000311} \approx 0.733
    $$

    Since $\psi = 0.733 < 1.5 = \psi_c$, the scheme still uses the **quadratic branch** even at $v_n = 0.001$.

    **Finding the transition value:** The scheme switches to exponential when $\psi > 1.5$. As $v_n$ decreases toward zero, $m \to \theta(1 - e^{-\kappa\Delta t}) \approx 0.00470$ and the variance $s^2$ also decreases. At $v_n = 0$:

    $$
    m_0 = 0.00470, \quad s_0^2 = \frac{0.04 \times 0.09}{3.0}(0.1175)^2 = 0.0000166
    $$

    $$
    \psi_0 = \frac{0.0000166}{0.00470^2} = \frac{0.0000166}{0.0000221} \approx 0.751
    $$

    Even at $v_n = 0$, $\psi \approx 0.751 < 1.5$, so the quadratic branch is used. For these particular parameters with monthly time steps, the scheme **never switches** to the exponential branch. The exponential branch is triggered primarily when the Feller condition is more severely violated (larger $\xi$ or smaller $\kappa\theta$), or with longer time steps.

    To force a switch, consider $\xi = 0.8$: then $\xi^2 = 0.64$, and at $v_n = 0$: $s^2 = 0.04 \times 0.64/(3.0) \times 0.1175^2 \approx 0.000118$, $m = 0.00470$, $\psi = 0.000118/0.0000221 \approx 5.34 > 1.5$. So with higher vol-of-vol, the exponential branch activates.

---

**Exercise 3.**
In the quadratic approximation, $v_{n+1} = a(b + Z_v)^2$ with $Z_v \sim N(0,1)$. This is always non-negative, since it is a squared quantity times a positive constant. However, it cannot produce negative variance. Show that $\mathbb{P}(v_{n+1} = 0) = \mathbb{P}(Z_v = -b)$ which has probability zero for a continuous distribution. In what sense does the quadratic approximation handle the zero boundary differently from the exact non-central chi-squared?

??? success "Solution to Exercise 3"
    In the quadratic approximation, $v_{n+1} = a(b + Z_v)^2$ where $a > 0$ and $Z_v \sim N(0,1)$. Since $a > 0$ and $(b + Z_v)^2 \geq 0$, we always have $v_{n+1} \geq 0$.

    The event $v_{n+1} = 0$ occurs when $Z_v = -b$. Since $Z_v$ has a continuous distribution (standard normal), the probability of hitting any single point is zero:

    $$
    \mathbb{P}(v_{n+1} = 0) = \mathbb{P}(Z_v = -b) = 0
    $$

    **Comparison with the exact non-central chi-squared:**

    The exact CIR transition distribution is a scaled non-central chi-squared $v_{n+1} \sim c \cdot \chi^2_d(\lambda)$ where $c = \xi^2(1-e^{-\kappa\Delta t})/(4\kappa)$. When $d < 2$ (Feller condition violated), the non-central chi-squared has a **point mass at zero**: there is a discrete probability $\mathbb{P}(\chi^2_d(\lambda) = 0) > 0$. This happens because $\chi^2_d(\lambda)$ with $d < 2$ is a Poisson mixture of $\chi^2_{d+2N}(0)$ where $N \sim \text{Poisson}(\lambda/2)$. When $N = 0$ and $d < 2$, the central chi-squared $\chi^2_d(0)$ has a density that diverges at zero, and when $d \leq 0$ (extremely violated Feller condition), there is a genuine atom at zero.

    The quadratic approximation differs from the exact distribution in two ways:

    1. **No point mass at zero:** The quadratic approximation assigns zero probability to $v_{n+1} = 0$, whereas the exact distribution may have positive probability there (when $d < 2$). However, the quadratic branch is used only when $\psi$ is small, corresponding to $v_n$ well above zero, so the exact probability of hitting zero is also very small in this regime.

    2. **Tail behavior:** The quadratic form $(b + Z_v)^2$ produces a non-central chi-squared with 1 degree of freedom, while the true distribution has $d$ degrees of freedom. For large $d$ (small $\psi$), the approximation is accurate; for $d$ near 1, the approximation is less precise, which is why the scheme switches to the exponential branch.

    The exponential branch handles the near-zero regime correctly by explicitly assigning probability $p > 0$ to the event $v_{n+1} = 0$, mimicking the point mass in the exact distribution.

---

**Exercise 4.**
In the exponential approximation, $v_{n+1} = 0$ with probability $p = (\psi - 1)/(\psi + 1)$. For $\psi = 2.0$, compute $p$ and $\beta$. Explain the economic meaning: when $\psi$ is large (high coefficient of variation), the variance is near zero and has a significant probability of staying there. Draw 10 samples from this distribution using a table of uniform random numbers and compute the sample mean. How does it compare with $m$?

??? success "Solution to Exercise 4"
    With $\psi = 2.0$:

    $$
    p = \frac{\psi - 1}{\psi + 1} = \frac{2.0 - 1}{2.0 + 1} = \frac{1}{3} \approx 0.333
    $$

    $$
    \beta = \frac{2}{m(\psi + 1)} = \frac{2}{3m}
    $$

    For a concrete example, suppose $m = 0.005$ (variance near zero):

    $$
    \beta = \frac{2}{3 \times 0.005} = \frac{2}{0.015} \approx 133.3
    $$

    **Economic meaning:** With $p = 1/3$, there is a 33.3% probability that the variance stays at zero---a significant chance of zero volatility for the next period. This reflects the behavior of the CIR process near the zero boundary when the Feller condition is violated: the process can touch zero and spend finite time there.

    **Sampling example:** Draw 10 uniform random numbers and apply the rule: if $U \leq p = 1/3$, set $v_{n+1} = 0$; otherwise, $v_{n+1} = \beta^{-1}\ln[(1-p)/(1-U)]$.

    | $U$ | Result | $v_{n+1}$ |
    |-----|--------|-----------|
    | 0.15 | $\leq 1/3$ | 0 |
    | 0.72 | $> 1/3$ | $\frac{1}{133.3}\ln\frac{0.667}{0.28} = 0.00652$ |
    | 0.91 | $> 1/3$ | $\frac{1}{133.3}\ln\frac{0.667}{0.09} = 0.01494$ |
    | 0.05 | $\leq 1/3$ | 0 |
    | 0.88 | $> 1/3$ | $\frac{1}{133.3}\ln\frac{0.667}{0.12} = 0.01278$ |
    | 0.45 | $> 1/3$ | $\frac{1}{133.3}\ln\frac{0.667}{0.55} = 0.00146$ |
    | 0.30 | $\leq 1/3$ | 0 |
    | 0.62 | $> 1/3$ | $\frac{1}{133.3}\ln\frac{0.667}{0.38} = 0.00425$ |
    | 0.78 | $> 1/3$ | $\frac{1}{133.3}\ln\frac{0.667}{0.22} = 0.00832$ |
    | 0.51 | $> 1/3$ | $\frac{1}{133.3}\ln\frac{0.667}{0.49} = 0.00233$ |

    Sample mean $\approx (0 + 0.00652 + 0.01494 + 0 + 0.01278 + 0.00146 + 0 + 0.00425 + 0.00832 + 0.00233)/10 \approx 0.00506$.

    The theoretical mean is $m = 0.005$. The sample mean of $0.00506$ is close to $m$, consistent with the moment-matching construction. With only 10 samples, we expect sampling variability of order $s/\sqrt{10} \approx 0.002$, so the agreement is within expected bounds.

---

**Exercise 5.**
The log-price update uses constants $K_0, K_1, K_2, K_3, K_4$ that ensure the martingale property $\mathbb{E}[S_{n+1}|\mathcal{F}_n] = S_n e^{(r-q)\Delta t}$. Using the formula $x_{n+1} = x_n + K_0 + K_1 v_n + K_2 v_{n+1} + \sqrt{K_3 v_n + K_4 v_{n+1}}\,Z_x$, show that the martingale condition requires $\mathbb{E}[\exp(K_0 + K_1 v_n + K_2 v_{n+1} + \sqrt{K_3 v_n + K_4 v_{n+1}}\,Z_x)] = e^{(r-q)\Delta t}$. Why is this condition harder to enforce analytically in the QE scheme than in the Euler scheme?

??? success "Solution to Exercise 5"
    The log-price update is:

    $$
    x_{n+1} = x_n + K_0 + K_1 v_n + K_2 v_{n+1} + \sqrt{K_3 v_n + K_4 v_{n+1}}\,Z_x
    $$

    The stock price is $S_{n+1} = e^{x_{n+1}}$. The martingale condition under the risk-neutral measure requires:

    $$
    \mathbb{E}[S_{n+1} \mid \mathcal{F}_n] = S_n e^{(r-q)\Delta t}
    $$

    $$
    \mathbb{E}\!\left[e^{x_{n+1}} \mid \mathcal{F}_n\right] = e^{x_n + (r-q)\Delta t}
    $$

    Substituting the update formula:

    $$
    \mathbb{E}\!\left[\exp\!\left(x_n + K_0 + K_1 v_n + K_2 v_{n+1} + \sqrt{K_3 v_n + K_4 v_{n+1}}\,Z_x\right) \mid \mathcal{F}_n\right] = e^{x_n + (r-q)\Delta t}
    $$

    Canceling $e^{x_n}$:

    $$
    \mathbb{E}\!\left[\exp\!\left(K_0 + K_1 v_n + K_2 v_{n+1} + \sqrt{K_3 v_n + K_4 v_{n+1}}\,Z_x\right) \mid \mathcal{F}_n\right] = e^{(r-q)\Delta t}
    $$

    Conditioning on $v_{n+1}$ (which is already generated before sampling $Z_x$) and using $Z_x \sim N(0,1)$ independent of $v_{n+1}$:

    $$
    \mathbb{E}\!\left[e^{\sqrt{K_3 v_n + K_4 v_{n+1}}\,Z_x} \mid v_n, v_{n+1}\right] = \exp\!\left(\frac{K_3 v_n + K_4 v_{n+1}}{2}\right)
    $$

    by the moment generating function of the normal. So the condition becomes:

    $$
    \mathbb{E}\!\left[\exp\!\left(K_0 + K_1 v_n + K_2 v_{n+1} + \frac{K_3 v_n + K_4 v_{n+1}}{2}\right) \mid v_n\right] = e^{(r-q)\Delta t}
    $$

    $$
    e^{K_0 + (K_1 + K_3/2)v_n} \cdot \mathbb{E}\!\left[e^{(K_2 + K_4/2)v_{n+1}} \mid v_n\right] = e^{(r-q)\Delta t}
    $$

    **Why this is harder than in the Euler scheme:** In the Euler scheme, $v_{n+1}$ is a known linear function of $v_n$ and a Gaussian, so the moment generating function $\mathbb{E}[e^{\alpha v_{n+1}} \mid v_n]$ can be computed in closed form (it is log-linear in $v_n$). In the QE scheme, $v_{n+1}$ is generated from either the quadratic or exponential approximation, each with a different, more complex distribution. The moment generating function $\mathbb{E}[e^{\alpha v_{n+1}} \mid v_n]$ must be computed separately for each branch, and it depends on whether the scheme is in the quadratic or exponential regime. This makes exact analytic enforcement of the martingale condition more involved, requiring branch-specific moment calculations or numerical calibration of the constants.

---

**Exercise 6.**
The comparison table shows that QE with $N = 12$ monthly steps has a bias of $-\$0.01$ while Euler full truncation with $N = 252$ daily steps has a bias of $-\$0.05$. The QE scheme is both more accurate and $252/12 \approx 21$ times faster per path. Explain why moment matching is so much more effective than Euler discretization for the CIR process: the QE scheme captures the correct mean and variance of the transition, while Euler introduces systematic bias from truncating negative values.

??? success "Solution to Exercise 6"
    The Euler full-truncation scheme introduces bias through two mechanisms:

    **1. Truncation bias:** When $v_n < 0$ (which should never occur in the true process), the scheme sets $v_n^+ = 0$, eliminating both the drift contribution from the current variance level and the diffusion entirely. This creates a systematic underestimate of the variance: the truncated process spends time at zero that the true process would not, reducing the total integrated variance and hence the option price.

    **2. Discretization bias:** Even without negative variance events, the Euler scheme approximates the nonlinear CIR dynamics with a linear step. The concavity of $\sqrt{v}$ means that $\mathbb{E}[\sqrt{v_{n+1}}] < \sqrt{\mathbb{E}[v_{n+1}]}$ (Jensen's inequality), so the Euler scheme systematically misestimates the diffusion contribution.

    **Why moment matching avoids these problems:** The QE scheme bypasses both issues by matching the exact first two moments of the CIR transition distribution:

    - $\mathbb{E}[v_{n+1}^{\text{QE}} \mid v_n] = m = \mathbb{E}[v_{n+1}^{\text{true}} \mid v_n]$ (exact mean)
    - $\text{Var}[v_{n+1}^{\text{QE}} \mid v_n] = s^2 = \text{Var}[v_{n+1}^{\text{true}} \mid v_n]$ (exact variance)

    Since the option price depends primarily on the mean and variance of the terminal distribution (and to a lesser extent on higher moments), matching these two moments captures the bulk of the pricing-relevant information. The QE scheme never produces "negative variance" because both the quadratic $(a(b+Z)^2 \geq 0)$ and exponential branches are non-negative by construction. There is no truncation event and hence no truncation bias.

    The QE scheme captures in each large time step ($\Delta t = 1/12$) more information about the true transition than the Euler scheme captures in 21 small steps ($21 \times 1/252 \approx 1/12$), because moment matching encodes the analytical solution of the CIR ODE for the moments, while Euler must approximate the same dynamics incrementally.

---

**Exercise 7.**
The threshold $\psi_c$ controls the switching between quadratic and exponential branches. Andersen recommends $\psi_c = 1.5$. Investigate the sensitivity to this choice by computing $\psi$ for $v_n$ ranging from $0.001$ to $0.1$ (with the standard parameters and $\Delta t = 1/12$). For what fraction of the $v_n$ range does the scheme use the exponential branch? What happens if you set $\psi_c = 0.5$ (always exponential) or $\psi_c = 3.0$ (almost always quadratic)? Discuss the accuracy implications.

??? success "Solution to Exercise 7"
    We compute $\psi = s^2/m^2$ for $v_n$ ranging from $0.001$ to $0.1$ with $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\Delta t = 1/12$.

    Let $e^{-\kappa\Delta t} = e^{-0.125} \approx 0.8825$ and $1 - e^{-0.125} \approx 0.1175$.

    **For several representative values:**

    | $v_n$ | $m$ | $s^2$ | $\psi$ | Branch |
    |-------|-----|-------|--------|--------|
    | 0.001 | 0.00558 | $2.28 \times 10^{-5}$ | 0.733 | Quadratic |
    | 0.005 | 0.00912 | $4.50 \times 10^{-5}$ | 0.541 | Quadratic |
    | 0.010 | 0.01355 | $7.28 \times 10^{-5}$ | 0.396 | Quadratic |
    | 0.020 | 0.02240 | $1.28 \times 10^{-4}$ | 0.256 | Quadratic |
    | 0.040 | 0.04000 | $2.37 \times 10^{-4}$ | 0.148 | Quadratic |
    | 0.060 | 0.05765 | $3.46 \times 10^{-4}$ | 0.104 | Quadratic |
    | 0.080 | 0.07530 | $4.56 \times 10^{-4}$ | 0.080 | Quadratic |
    | 0.100 | 0.09295 | $5.65 \times 10^{-4}$ | 0.065 | Quadratic |

    For this parameter set, $\psi$ ranges from about $0.065$ (at $v_n = 0.1$) to $0.733$ (at $v_n = 0.001$). Since $\psi < 1.5$ for all values, the scheme **never uses the exponential branch**. The fraction using the exponential branch is $0\%$.

    Even at $v_n = 0$ (the extreme case), $\psi \approx 0.751 < 1.5$.

    **Effect of alternative thresholds:**

    - $\psi_c = 0.5$: The scheme uses the exponential branch for $v_n \lesssim 0.004$ (roughly $4\%$ of the range $[0.001, 0.1]$). The exponential approximation is less accurate than the quadratic for moderate $\psi$ values because it is designed for the near-zero regime. Forcing its use when $\psi$ is only moderately large introduces unnecessary approximation error.

    - $\psi_c = 3.0$: The scheme almost always uses the quadratic branch (even more so than $\psi_c = 1.5$). For these parameters, this makes no difference since $\psi < 1.5$ everywhere. However, with higher $\xi$ or when the Feller condition is severely violated, some $\psi$ values could exceed 2. The quadratic approximation requires $\psi \leq 2$ for $b^2 \geq 0$, so setting $\psi_c = 3.0$ could cause the quadratic formula to produce $b^2 < 0$ (invalid). Andersen's choice of $\psi_c = 1.5$ provides a safety margin below the $\psi = 2$ boundary where the quadratic approximation breaks down.

    **Summary:** The sensitivity to $\psi_c$ is low for well-behaved parameters but becomes important when $\xi$ is large relative to $\kappa\theta$. The recommended $\psi_c = 1.5$ balances accuracy (using the quadratic where it works well) with robustness (switching to exponential before the quadratic formula becomes invalid).
