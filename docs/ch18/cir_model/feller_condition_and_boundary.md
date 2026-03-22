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
