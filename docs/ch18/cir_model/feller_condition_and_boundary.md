# Feller Condition and Boundary Classification

The behavior of the CIR process near zero is governed by the **Feller condition** $2\kappa\theta \geq \sigma^2$, which determines whether the boundary $r = 0$ is accessible. When the condition holds, the drift toward $\theta > 0$ is strong enough to prevent the process from reaching zero. When it is violated, the process touches zero but is instantaneously reflected. This section derives the Feller condition using the speed and scale density apparatus from the theory of one-dimensional diffusions, classifies the boundary according to Feller's taxonomy, and discusses the practical implications for interest rate modeling.

---

## Statement of the Feller condition

For the CIR process

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
$$

with $\kappa > 0$, $\theta > 0$, $\sigma > 0$, the **Feller condition** is

$$
\boxed{2\kappa\theta \geq \sigma^2}
$$

Equivalently, defining the **Feller ratio** $\nu = 2\kappa\theta/\sigma^2$ (which also equals the degrees of freedom of the associated non-central chi-squared distribution):

- $\nu \geq 1$: Feller condition satisfied
- $\nu < 1$: Feller condition violated

When $\nu \geq 1$, the process is strictly positive for all $t > 0$ (assuming $r_0 > 0$). When $\nu < 1$, the process reaches zero in finite time with positive probability.

---

## Intuitive derivation

Near $r = 0$, the CIR SDE behaves like

$$
dr_t \approx \kappa\theta\,dt + \sigma\sqrt{r_t}\,dW_t
$$

The drift pushes the process away from zero at rate $\kappa\theta$, while the diffusion creates random fluctuations of magnitude $\sigma\sqrt{r_t}$. Informally, the "infinitesimal variance" near zero is $\sigma^2 r_t \cdot dt$, which vanishes, while the drift remains $\kappa\theta\,dt > 0$.

Consider the transformed process $Y_t = \sqrt{r_t}$. By Ito's lemma:

$$
dY_t = \frac{1}{2\sqrt{r_t}}\,dr_t - \frac{1}{8r_t^{3/2}}\,(dr_t)^2
$$

$$
= \frac{1}{2Y_t}\!\left[\kappa(\theta - Y_t^2) - \frac{\sigma^2}{4}\right]dt + \frac{\sigma}{2}\,dW_t
$$

Near $Y_t = 0$ (i.e., $r_t \approx 0$), the drift of $Y_t$ is approximately $(\kappa\theta - \sigma^2/4)/(2Y_t)$. This drift is:

- **Repelling from zero** (pushing $Y_t$ upward) if $\kappa\theta > \sigma^2/4$, i.e., $2\kappa\theta > \sigma^2/2$
- **Attracting toward zero** if $\kappa\theta < \sigma^2/4$

The precise threshold is $2\kappa\theta = \sigma^2$, which is the Feller condition.

---

## Boundary classification via scale and speed

### Scale function

For a one-dimensional diffusion $dX_t = \mu(X)\,dt + \sigma_X(X)\,dW_t$ on $(l, r)$, the **scale function** is

$$
s(x) = \int_c^x \exp\!\left(-\int_c^y \frac{2\mu(z)}{\sigma_X^2(z)}\,dz\right)dy
$$

For the CIR process with $\mu(r) = \kappa(\theta - r)$ and $\sigma_X^2(r) = \sigma^2 r$:

$$
\frac{2\mu(r)}{\sigma_X^2(r)} = \frac{2\kappa(\theta - r)}{\sigma^2 r} = \frac{2\kappa\theta}{\sigma^2 r} - \frac{2\kappa}{\sigma^2}
$$

The scale density (integrand of $s$) is

$$
s'(x) = \exp\!\left(-\frac{2\kappa\theta}{\sigma^2}\ln x + \frac{2\kappa}{\sigma^2}x + C\right) = x^{-\nu}\,e^{2\kappa x/\sigma^2}
$$

where $\nu = 2\kappa\theta/\sigma^2$ and we absorbed constants.

### Speed density

The **speed density** is

$$
m(x) = \frac{1}{\sigma_X^2(x)\,s'(x)} = \frac{1}{\sigma^2 x}\,x^{\nu}\,e^{-2\kappa x/\sigma^2} = \frac{x^{\nu - 1}}{\sigma^2}\,e^{-2\kappa x/\sigma^2}
$$

### Boundary behavior at r = 0

The classification depends on the integrability of the scale and speed densities near $0$:

**Scale density near 0:** $s'(x) \sim x^{-\nu}$ as $x \to 0^+$.

- $\int_0^c s'(x)\,dx < \infty$ if and only if $\nu < 1$

**Speed density near 0:** $m(x) \sim x^{\nu-1}$ as $x \to 0^+$.

- $\int_0^c m(x)\,dx < \infty$ if and only if $\nu > 0$ (always true since $\kappa, \theta > 0$)

### Classification

According to Feller's boundary classification:

| Condition | $\int s'$ near 0 | $\int m$ near 0 | Classification | Behavior |
|---|---|---|---|---|
| $\nu \geq 2$ | $= \infty$ | $< \infty$ | **Entrance** | Zero never reached; natural boundary from below |
| $1 \leq \nu < 2$ | $= \infty$ | $< \infty$ | **Entrance** | Zero never reached |
| $0 < \nu < 1$ | $< \infty$ | $< \infty$ | **Regular** | Zero reached in finite time; instantaneous reflection |

When $\nu \geq 1$ (the Feller condition), the boundary at zero is an **entrance boundary**: the process can be started there but cannot reach zero from the interior. The short rate is strictly positive for all $t > 0$.

When $0 < \nu < 1$, the boundary is **regular**: the process reaches zero in finite time with positive probability, but is instantaneously reflected (not absorbed). The process remains non-negative.

---

## Probability of reaching zero

When $\nu < 1$ (Feller condition violated), the probability that the CIR process hits zero before time $T$ is positive. An exact formula involves the non-central chi-squared CDF.

For the hitting time $\tau_0 = \inf\{t > 0 : r_t = 0\}$:

$$
\mathbb{P}(\tau_0 \leq T) > 0 \quad \text{if and only if} \quad \nu < 1
$$

When $\nu \geq 1$: $\mathbb{P}(\tau_0 < \infty) = 0$ (zero is never reached).

---

## Practical implications

### Parameter calibration

When calibrating the CIR model to market data, the Feller condition imposes the constraint $2\kappa\theta \geq \sigma^2$, which restricts the feasible parameter space. This constraint can bind, especially in low-rate environments:

- Low $\theta$ (low long-run rate) reduces $2\kappa\theta$
- High $\sigma$ (high rate volatility) increases $\sigma^2$
- Low $\kappa$ (slow mean reversion) further reduces $2\kappa\theta$

In such environments, the calibrated parameters may violate the Feller condition, meaning the model predicts that rates touch zero with positive probability.

### Simulation near zero

When the Feller condition is violated ($\nu < 1$), Euler-Maruyama discretization of the CIR SDE can produce **negative** values because the discrete approximation overshoots zero. Common remedies:

1. **Truncation**: $r_{t+\Delta t} = \max(\hat{r}_{t+\Delta t}, 0)$ (biased)
2. **Reflection**: $r_{t+\Delta t} = |\hat{r}_{t+\Delta t}|$ (preserves non-negativity)
3. **Exact simulation**: Draw from the non-central chi-squared distribution (unbiased, more expensive)

Even when $\nu \geq 1$, Euler discretization can produce negative values for large $\Delta t$. Exact simulation is always preferred for the CIR model.

### Heston model connection

The Feller condition for the Heston variance process $dv_t = \kappa_v(\theta_v - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t$ is $2\kappa_v\theta_v \geq \sigma_v^2$. In practice, calibrated Heston parameters frequently violate this condition (typical vol-of-vol $\sigma_v$ values are large), requiring careful numerical treatment of near-zero variance paths.

---

## Numerical example

**Case 1: Feller condition satisfied.**
$\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.1$. Feller ratio: $\nu = 2 \times 0.5 \times 0.04 / 0.01 = 4.0$.

Since $\nu = 4 \geq 1$, zero is an entrance boundary. Starting from $r_0 = 0.001$ (near zero), the process is immediately pushed away and never returns to zero.

**Case 2: Feller condition violated.**
$\kappa = 0.1$, $\theta = 0.01$, $\sigma = 0.15$. Feller ratio: $\nu = 2 \times 0.1 \times 0.01 / 0.0225 = 0.089$.

Since $\nu = 0.089 < 1$, zero is a regular boundary. The process touches zero in finite time and is reflected. Simulation requires exact methods or careful truncation to avoid negative values.

**Case 3: Borderline.**
$\kappa = 0.5$, $\theta = 0.02$, $\sigma = 0.1\sqrt{2} \approx 0.1414$. Feller ratio: $\nu = 2 \times 0.5 \times 0.02 / 0.02 = 1.0$.

At the boundary $\nu = 1$, zero is technically an entrance boundary (the process does not reach zero), but it comes arbitrarily close. Simulation is challenging in this borderline case.

---

## Summary

The Feller condition $2\kappa\theta \geq \sigma^2$ (equivalently $\nu = 2\kappa\theta/\sigma^2 \geq 1$) is the fundamental criterion governing the CIR process near zero. When satisfied, the boundary $r = 0$ is an entrance boundary and the short rate is strictly positive. When violated, zero is reached in finite time but the process is instantaneously reflected, maintaining non-negativity. The condition constrains calibration and determines whether simple Euler discretization schemes remain valid or whether exact simulation methods are required.

---

## Exercises

**Exercise 1.** For each parameter set below, compute the Feller ratio $\nu = 2\kappa\theta/\sigma^2$ and classify the boundary at $r = 0$ as entrance or regular: (a) $\kappa = 1.0$, $\theta = 0.05$, $\sigma = 0.20$; (b) $\kappa = 0.2$, $\theta = 0.03$, $\sigma = 0.10$; (c) $\kappa = 0.5$, $\theta = 0.08$, $\sigma = 0.20$.

??? success "Solution to Exercise 1"

    **(a)** $\kappa = 1.0$, $\theta = 0.05$, $\sigma = 0.20$:

    $$
    \nu = \frac{2 \times 1.0 \times 0.05}{0.04} = \frac{0.10}{0.04} = 2.5
    $$

    Since $\nu = 2.5 \geq 1$, the Feller condition is satisfied. Zero is an **entrance boundary** (inaccessible).

    **(b)** $\kappa = 0.2$, $\theta = 0.03$, $\sigma = 0.10$:

    $$
    \nu = \frac{2 \times 0.2 \times 0.03}{0.01} = \frac{0.012}{0.01} = 1.2
    $$

    Since $\nu = 1.2 \geq 1$, the Feller condition is satisfied. Zero is an **entrance boundary** (inaccessible), but just barely.

    **(c)** $\kappa = 0.5$, $\theta = 0.08$, $\sigma = 0.20$:

    $$
    \nu = \frac{2 \times 0.5 \times 0.08}{0.04} = \frac{0.08}{0.04} = 2.0
    $$

    Since $\nu = 2.0 \geq 1$, the Feller condition is satisfied. Zero is an **entrance boundary**. At exactly $\nu = 2$, the density has a finite, nonzero value at the origin (unlike $\nu > 2$ where the density is zero at the origin).

---

**Exercise 2.** Apply Ito's lemma to $Y_t = \sqrt{r_t}$ where $r_t$ follows the CIR SDE. Derive the drift of $Y_t$ near $Y_t = 0$ and show that it behaves like $(\kappa\theta - \sigma^2/4)/(2Y_t)$. Explain why this drift is repelling from zero when $2\kappa\theta > \sigma^2/2$ and relate this to the Feller condition.

??? success "Solution to Exercise 2"

    Let $Y_t = \sqrt{r_t}$, so $r_t = Y_t^2$. By Ito's lemma with $g(r) = \sqrt{r}$:

    $$
    dY_t = g'(r_t)\,dr_t + \frac{1}{2}g''(r_t)(dr_t)^2
    $$

    $$
    g'(r) = \frac{1}{2\sqrt{r}}, \qquad g''(r) = -\frac{1}{4r^{3/2}}
    $$

    With $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$ and $(dr_t)^2 = \sigma^2 r_t\,dt$:

    $$
    dY_t = \frac{1}{2\sqrt{r_t}}[\kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t] - \frac{1}{8r_t^{3/2}}\sigma^2 r_t\,dt
    $$

    $$
    = \frac{1}{2Y_t}[\kappa(\theta - Y_t^2)]\,dt + \frac{\sigma}{2}\,dW_t - \frac{\sigma^2}{8Y_t}\,dt
    $$

    $$
    = \frac{1}{2Y_t}\left[\kappa\theta - \kappa Y_t^2 - \frac{\sigma^2}{4}\right]dt + \frac{\sigma}{2}\,dW_t
    $$

    Near $Y_t = 0$ (i.e., $r_t \approx 0$), the $\kappa Y_t^2$ term is negligible, so:

    $$
    dY_t \approx \frac{\kappa\theta - \sigma^2/4}{2Y_t}\,dt + \frac{\sigma}{2}\,dW_t
    $$

    The drift $(\kappa\theta - \sigma^2/4)/(2Y_t)$ diverges as $Y_t \to 0$:

    - If $\kappa\theta > \sigma^2/4$ (equivalently $4\kappa\theta > \sigma^2$, which is stronger than the Feller condition $2\kappa\theta \geq \sigma^2$), the drift is **positive and repelling** from zero --- it pushes $Y_t$ (and hence $r_t$) away from zero with infinite force.
    - If $\kappa\theta < \sigma^2/4$, the drift is negative, attracting the process toward zero.

    The Feller condition $2\kappa\theta \geq \sigma^2$ (equivalently $\kappa\theta \geq \sigma^2/2$) is a weaker condition than $\kappa\theta > \sigma^2/4$. The precise boundary analysis via scale functions shows that the threshold for inaccessibility is $\nu = 2\kappa\theta/\sigma^2 \geq 1$, not $4\kappa\theta/\sigma^2 \geq 1$. The Ito lemma calculation provides the intuition but overstates the threshold because the constant diffusion $\sigma/2$ for $Y_t$ also plays a role in the boundary behavior.

---

**Exercise 3.** The scale density for the CIR process is $s'(x) = x^{-\nu} e^{2\kappa x/\sigma^2}$. Evaluate $\int_0^c s'(x)\,dx$ for $c = 0.01$ and show that the integral converges if and only if $\nu < 1$. What does the divergence of this integral for $\nu \geq 1$ imply about the accessibility of the boundary?

??? success "Solution to Exercise 3"

    The scale density is $s'(x) = x^{-\nu}e^{2\kappa x/\sigma^2}$. Near $x = 0$, the exponential $e^{2\kappa x/\sigma^2} \to 1$, so $s'(x) \sim x^{-\nu}$.

    $$
    \int_0^c s'(x)\,dx \approx \int_0^c x^{-\nu}\,dx
    $$

    This integral converges if and only if $-\nu > -1$, i.e., $\nu < 1$:

    $$
    \int_0^c x^{-\nu}\,dx = \frac{x^{1-\nu}}{1-\nu}\bigg|_0^c = \frac{c^{1-\nu}}{1-\nu}
    $$

    which is finite when $1 - \nu > 0$ ($\nu < 1$) and diverges when $\nu \geq 1$.

    For $c = 0.01$: if $\nu = 0.5$, $\int_0^{0.01} x^{-0.5}\,dx = 2\sqrt{0.01} = 0.2 < \infty$.
    If $\nu = 1.5$, $\int_0^{0.01} x^{-1.5}\,dx = [-2x^{-0.5}]_0^{0.01}$, which diverges as $x \to 0$.

    **Implications of divergence ($\nu \geq 1$):** In Feller's boundary classification, the divergence of $\int_0^c s'(x)\,dx$ means the boundary at 0 is **not accessible** from the interior. The scale function $s(x) = \int_c^x s'(y)\,dy$ diverges to $-\infty$ as $x \to 0$, meaning the process needs "infinite time" (in the scale metric) to reach zero. Therefore, zero is an entrance boundary: the process can start there but cannot reach it from positive values.

---

**Exercise 4.** A risk manager calibrates the CIR model in a low-rate environment and obtains $\kappa = 0.15$, $\theta = 0.01$, $\sigma = 0.08$. Check the Feller condition. If it is violated, what is the maximum $\sigma$ that would satisfy the Feller condition while keeping $\kappa$ and $\theta$ fixed? Alternatively, what is the minimum $\theta$ that satisfies the condition while keeping $\kappa$ and $\sigma$ fixed?

??? success "Solution to Exercise 4"

    **Check the Feller condition:**

    $$
    2\kappa\theta = 2(0.15)(0.01) = 0.003, \qquad \sigma^2 = (0.08)^2 = 0.0064
    $$

    Since $0.003 < 0.0064$, the Feller condition is **violated**.

    **Maximum $\sigma$ satisfying Feller with fixed $\kappa$ and $\theta$:**

    $$
    \sigma^2 \leq 2\kappa\theta = 0.003 \implies \sigma \leq \sqrt{0.003} \approx 0.05477
    $$

    The maximum volatility is $\sigma_{\max} \approx 0.0548$ or about 5.48%.

    **Minimum $\theta$ satisfying Feller with fixed $\kappa$ and $\sigma$:**

    $$
    2\kappa\theta \geq \sigma^2 \implies \theta \geq \frac{\sigma^2}{2\kappa} = \frac{0.0064}{0.30} \approx 0.02133
    $$

    The minimum long-run mean is $\theta_{\min} \approx 2.13\%$.

    In a low-rate environment with $\theta = 1\%$, the Feller condition severely restricts the allowable volatility. This is a known limitation of the CIR model in near-zero rate regimes.

---

**Exercise 5.** Explain why the Feller condition constrains the feasible region for CIR calibration. Draw the feasible region in the $(\theta, \sigma)$ plane for fixed $\kappa = 0.5$, shading the area where $2\kappa\theta \geq \sigma^2$. What shape is this region?

??? success "Solution to Exercise 5"

    The Feller condition is $2\kappa\theta \geq \sigma^2$. With $\kappa = 0.5$:

    $$
    2(0.5)\theta \geq \sigma^2 \implies \theta \geq \sigma^2
    $$

    In the $(\theta, \sigma)$ plane, this is the region below the parabola $\sigma = \sqrt{\theta}$ (or equivalently above the curve $\theta = \sigma^2$).

    The feasible region is $\{(\theta, \sigma) : \theta \geq \sigma^2,\, \theta > 0,\, \sigma > 0\}$. This is the region **above** the parabola $\theta = \sigma^2$ in the $(\theta, \sigma)$ plane (or equivalently, **below** the curve $\sigma = \sqrt{\theta}$).

    The shape is a **parabolic region**: for each value of $\sigma$, $\theta$ must exceed $\sigma^2$. Alternatively, for each $\theta$, $\sigma$ must be less than $\sqrt{\theta}$. The boundary is the parabola $\theta = \sigma^2$.

    For example, at $\theta = 0.04$ (4%), the maximum $\sigma$ is $\sqrt{0.04} = 0.20$. At $\theta = 0.01$ (1%), the maximum $\sigma$ is $\sqrt{0.01} = 0.10$. The feasible region shrinks as $\theta$ decreases, illustrating the difficulty of maintaining the Feller condition in low-rate environments.

---

**Exercise 6.** In the Heston stochastic volatility model, typical calibrated parameters are $\kappa_v = 2.0$, $\theta_v = 0.04$, and $\sigma_v = 0.5$. Compute the Feller ratio $\nu = 2\kappa_v\theta_v/\sigma_v^2$. Is the Feller condition satisfied? Discuss the practical implications for Monte Carlo simulation of the Heston model when the variance process can touch zero.

??? success "Solution to Exercise 6"

    **Feller ratio:**

    $$
    \nu = \frac{2\kappa_v\theta_v}{\sigma_v^2} = \frac{2 \times 2.0 \times 0.04}{0.25} = \frac{0.16}{0.25} = 0.64
    $$

    Since $\nu = 0.64 < 1$, the Feller condition is **violated**.

    **Practical implications:**

    1. **Variance reaches zero:** The variance process $v_t$ will touch zero in finite time with positive probability. At $v_t = 0$, the asset has zero instantaneous volatility, which is unrealistic.

    2. **Simulation challenges:** Euler-Maruyama applied to $dv_t = 2.0(0.04 - v_t)dt + 0.5\sqrt{v_t}\,dW_t$ will frequently produce negative variance values, especially when $v_t$ is near zero. Each negative value requires a fix (truncation, reflection, or absorption), introducing bias.

    3. **Impact on option prices:** The zero-variance states affect the fat tails of the asset return distribution. Heston models calibrated to equity options typically violate Feller because the market-implied vol-of-vol $\sigma_v$ is high, reflecting the observed mean-reversion and clustering of volatility.

    4. **Standard practice:** Despite the Feller violation, the Heston model remains valid mathematically. The characteristic function (used for semi-analytical option pricing) is well-defined regardless of the Feller condition. For Monte Carlo, practitioners use exact simulation methods (Broadie-Kaya) or the QE scheme (Andersen) to handle the boundary correctly.

---

**Exercise 7.** When $\nu < 1$ and the process reaches zero, it is "instantaneously reflected." Explain what this means mathematically: the process spends zero Lebesgue time at the boundary (i.e., $\int_0^T \mathbf{1}_{\{r_t = 0\}}\,dt = 0$ a.s.), yet it visits zero. Contrast this with an "absorbing" boundary where the process stays at zero once reached. Why is reflection the correct boundary behavior for the CIR process?

??? success "Solution to Exercise 7"

    **Instantaneous reflection** means that the process visits zero (i.e., $\tau_0 = \inf\{t: r_t = 0\} < \infty$ with positive probability) but spends zero Lebesgue time there:

    $$
    \int_0^T \mathbf{1}_{\{r_t = 0\}}\,dt = 0 \quad \text{a.s.}
    $$

    This is analogous to how a standard Brownian motion visits zero uncountably many times but the set of zeros has Lebesgue measure zero. The process touches zero at isolated instants (or on a set of measure zero in time) and immediately moves back into the positive half-line.

    **Contrast with absorption:** At an absorbing boundary, once the process reaches zero, it stays there: $r_t = 0$ for all $t \geq \tau_0$. The process spends positive Lebesgue time at zero, and $\int_0^T \mathbf{1}_{\{r_t = 0\}}\,dt > 0$.

    **Why reflection is correct for CIR:** The CIR SDE has a drift $\kappa(\theta - r_t) \to \kappa\theta > 0$ as $r_t \to 0$, which provides a positive push away from zero. Even when the diffusion (which vanishes at zero) allows the process to touch zero, the drift immediately propels it back. Absorption would be correct only if the drift also vanished at zero (as in the geometric Brownian motion at zero), but for CIR the drift is strictly positive at the boundary. Mathematically, the speed measure $m(x) \sim x^{\nu-1}$ is integrable near zero (since $\nu > 0$), confirming that the boundary is regular (accessible) but not absorbing. The process leaves zero immediately because the drift restores it to the interior.
