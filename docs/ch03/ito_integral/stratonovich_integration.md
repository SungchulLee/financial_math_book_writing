# The Stratonovich Integral


## Introduction


Stochastic calculus provides a fundamental framework for modeling systems influenced by randomness. Financial mathematics, physics, and engineering all rely on stochastic processes to describe the evolution of complex systems over time. Among these processes, **Brownian motion** (or Wiener process) plays a central role.

Two principal notions of stochastic integration with respect to Brownian motion are the **Itô integral** and the **Stratonovich integral**. Although both define integrals of stochastic processes against Brownian motion, they differ significantly in interpretation, mathematical properties, and applications. This section introduces the Stratonovich integral, explains how it differs from the Itô integral, and illustrates the distinction through both theory and simulation.

---

## Step-Function Approximations of Stochastic Integrals


Let \( \{B_t\}_{t \ge 0} \) be a standard Brownian motion. Consider the following two piecewise constant processes:

\[
\phi_1(t, \omega)
= \sum_{j \ge 0} B_{j 2^{-n}}(\omega)
\, \mathbf{1}_{[j 2^{-n}, (j+1)2^{-n})}(t),
\]

\[
\phi_2(t, \omega)
= \sum_{j \ge 0} B_{(j+1)2^{-n}}(\omega)
\, \mathbf{1}_{[j 2^{-n}, (j+1)2^{-n})}(t).
\]

Here, \( \mathbf{1}_{[a,b)} \) denotes the indicator function of the interval \( [a,b) \).
The process \( \phi_1 \) samples Brownian motion at the **left endpoints**, while \( \phi_2 \) samples it at the **right endpoints** of each interval.

Such step functions are fundamental in the construction of stochastic integrals, serving as discrete approximations analogous to Riemann sums. The choice of evaluation point—left, right, or midpoint—ultimately determines the interpretation of the resulting stochastic integral.

---

## Expected Values of the Corresponding Stochastic Integrals


### 1. Left-Endpoint Approximation (Itô)


For \( \phi_1 \), the stochastic integral satisfies

\[
\mathbb{E}\left[ \int_0^T \phi_1(t)\, dB_t \right]
= \sum_j \mathbb{E}\bigl[ B_{t_j} (B_{t_{j+1}} - B_{t_j}) \bigr].
\]

Since Brownian increments are independent of the past and have mean zero,

\[
\mathbb{E}[B_{t_j} (B_{t_{j+1}} - B_{t_j})] = 0,
\]

which implies

\[
\mathbb{E}\left[ \int_0^T \phi_1(t)\, dB_t \right] = 0.
\]

This reflects the **martingale property** of the Itô integral when the integrand is adapted.

---

### 2. Right-Endpoint Approximation


For \( \phi_2 \), we compute

\[
\mathbb{E}\left[ \int_0^T \phi_2(t)\, dB_t \right]
= \sum_j \mathbb{E}\bigl[ B_{t_{j+1}} (B_{t_{j+1}} - B_{t_j}) \bigr].
\]

By the Itô isometry,

\[
\mathbb{E}[ B_{t_{j+1}} (B_{t_{j+1}} - B_{t_j}) ]
= \mathbb{E}[ (B_{t_{j+1}} - B_{t_j})^2 ]
= 2^{-n}.
\]

Summing over all intervals yields

\[
\mathbb{E}\left[ \int_0^T \phi_2(t)\, dB_t \right] = T.
\]

This calculation reveals the accumulation of **quadratic variation**, which does not vanish under right- or midpoint-type discretizations.

---

## Itô versus Stratonovich Integrals


The difference between Itô and Stratonovich integration arises from the choice of evaluation point within each partition interval.

### 1. Itô Integral


If the integrand is evaluated at the **left endpoint**,

\[
t_j^* = t_j,
\]

the resulting integral is the **Itô integral**,

\[
\int_0^T f(t,\omega)\, dB_t.
\]

Key properties include:

- Martingale property
- Itô isometry
- Failure of the classical chain rule (necessitating Itô’s lemma)

---

### 2. Stratonovich Integral


If the integrand is evaluated at the **midpoint**,

\[
t_j^* = \frac{t_j + t_{j+1}}{2},
\]

the limit defines the **Stratonovich integral**,

\[
\int_0^T f(t,\omega) \circ dB_t.
\]

This integral obeys the **classical chain rule**, making it resemble ordinary Riemann integration. For this reason, the Stratonovich integral is often preferred in physical and geometric modeling contexts.

---

## Quadratic Variation and Its Role


Brownian motion satisfies

\[
\mathbb{E}\bigl[(B_{t_{j+1}} - B_{t_j})^2\bigr] = 2^{-n},
\]

and the total quadratic variation over \( [0,T] \) is

\[
\langle B \rangle_T = T.
\]

This nonzero quadratic variation distinguishes Brownian paths from smooth functions and explains why different discretizations lead to different limiting integrals. The Itô integral excludes quadratic variation from the drift, while the Stratonovich integral incorporates it implicitly.

---

## Numerical Illustration: Itô vs. Stratonovich


Both integrals may be viewed as limits of discrete sums approximating

\[
\int_0^T B_t\, dB_t,
\]

but they differ in evaluation rules.

```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
T = 1.0
N = 1000
seed = 42

# Brownian motion simulation (assumed implemented elsewhere)
bm = BrownianMotion(maturity_time=T, seed=seed)
result = bm.simulate(num_paths=1, num_steps=N)

t = result.time_steps
dt = result.time_step_size
W = result.brownian_paths[0]
dW = result.increments[0]

# Itô integral (left-point rule)
ito_integral = np.concatenate(([0], np.cumsum(W[:-1] * dW)))

# Stratonovich integral (midpoint rule)
stratonovich_integral = np.concatenate(
    ([0], np.cumsum(0.5 * (W[:-1] + W[1:]) * dW))
)

# Plot
plt.figure(figsize=(12,6))
plt.plot(t, W, label="Brownian Motion")
plt.plot(t, ito_integral, "--", label="Itô Integral")
plt.plot(t, stratonovich_integral, "--", label="Stratonovich Integral")
plt.legend()
plt.title(r"Itô vs. Stratonovich: $\int_0^T B_t \, dB_t$")
plt.show()
```

---

## Conversion Between Itô and Stratonovich

The two integrals are related by a **correction term** involving the quadratic covariation.

### Conversion Formula

For a process $f(t, X_t)$ where $X_t$ satisfies an SDE, the Stratonovich integral can be expressed in terms of the Itô integral:

$$
\boxed{
\int_0^t f(s, X_s) \circ dW_s = \int_0^t f(s, X_s)\,dW_s + \frac{1}{2}\int_0^t \frac{\partial f}{\partial x}(s, X_s)\sigma(s, X_s)\,ds
}
$$

**Equivalently**:

$$
\int_0^t f \circ dW = \int_0^t f\,dW + \frac{1}{2}[f, W]_t
$$

where $[f, W]_t$ is the quadratic covariation between $f$ and $W$.

### Example: $\int B_t \circ dB_t$

Using the conversion formula with $f(x) = x$ and $\sigma = 1$:

$$
\int_0^t B_s \circ dB_s = \int_0^t B_s\,dB_s + \frac{1}{2}\int_0^t 1\,ds
$$

$$
= \frac{1}{2}(B_t^2 - t) + \frac{1}{2}t = \frac{1}{2}B_t^2
$$

This is exactly what the classical chain rule would give! (No Itô correction needed for Stratonovich.)

---

## The Stratonovich Chain Rule

A key advantage of Stratonovich calculus is that the **classical chain rule holds**.

**Theorem**: For $f \in C^2$ and $X_t$ satisfying a Stratonovich SDE:

$$
df(X_t) = f'(X_t) \circ dX_t
$$

**No second-order correction term appears!**

### Comparison

| Property | Itô | Stratonovich |
|----------|-----|--------------|
| Chain rule | $df = f'dX + \frac{1}{2}f''(dX)^2$ | $df = f' \circ dX$ |
| Martingale | Yes (for adapted integrands) | No |
| Riemann sum | Left endpoint | Midpoint |
| Physics | Less natural | More natural |
| Finance | Standard choice | Rarely used |

---

## The Wong-Zakai Theorem

The **Wong-Zakai theorem** provides deep insight into why the Stratonovich integral appears naturally in physics.

### Statement

Consider the SDE:

$$
dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t
$$

Now replace Brownian motion $W_t$ by a **smooth approximation** $W_t^{(n)}$ (e.g., piecewise linear interpolation), and solve the **ordinary** differential equation:

$$
\frac{dX_t^{(n)}}{dt} = b(X_t^{(n)}) + \sigma(X_t^{(n)})\frac{dW_t^{(n)}}{dt}
$$

**Wong-Zakai Theorem**: As $n \to \infty$, the solutions $X_t^{(n)}$ converge to the solution of the **Stratonovich SDE**:

$$
dX_t = b(X_t)\,dt + \sigma(X_t) \circ dW_t
$$

**NOT** the Itô SDE!

### Interpretation

- Physical systems with smooth noise (filtered white noise) naturally lead to Stratonovich equations
- The Itô integral requires "anticipating" that noise is truly white (delta-correlated)
- When modeling physical systems, Stratonovich is often more appropriate

### Converting Wong-Zakai to Itô

If physical reasoning suggests a Stratonovich SDE:

$$
dX_t = b(X_t)\,dt + \sigma(X_t) \circ dW_t
$$

The equivalent Itô SDE is:

$$
\boxed{
dX_t = \left(b(X_t) + \frac{1}{2}\sigma(X_t)\sigma'(X_t)\right)dt + \sigma(X_t)\,dW_t
}
$$

The extra drift term $\frac{1}{2}\sigma\sigma'$ is called the **noise-induced drift** or **Stratonovich correction**.

---

## When to Use Which?

### Use Itô When:

1. **Mathematical finance**: Risk-neutral pricing, hedging, Black-Scholes
2. **Filtering theory**: Kalman filter, signal processing
3. **Martingale methods**: Change of measure, Girsanov theorem
4. **Numerical simulation**: Euler-Maruyama naturally gives Itô

### Use Stratonovich When:

1. **Physics**: Langevin equations, thermodynamics, fluctuation-dissipation
2. **Geometric problems**: Stochastic flows on manifolds
3. **Deriving from physical principles**: Wong-Zakai limit of colored noise
4. **Preserving symmetries**: Stratonovich respects coordinate transformations

---

## Example: Overdamped Langevin Equation

In physics, the overdamped Langevin equation is often written as:

$$
\gamma \frac{dx}{dt} = -V'(x) + \sqrt{2\gamma k_B T}\,\xi(t)
$$

where $\xi(t)$ is "white noise."

**Physical interpretation** (Wong-Zakai) suggests Stratonovich:

$$
dx = -\frac{V'(x)}{\gamma}\,dt + \sqrt{\frac{2k_B T}{\gamma}} \circ dW_t
$$

**Equivalent Itô form** (for state-independent diffusion, they coincide):

$$
dx = -\frac{V'(x)}{\gamma}\,dt + \sqrt{\frac{2k_B T}{\gamma}}\,dW_t
$$

When diffusion is state-dependent, the correction term becomes crucial!

---

## Summary

$$
\boxed{
\int f \circ dW = \int f\,dW + \frac{1}{2}\int f'\sigma\,dt
}
$$

| Aspect | Itô Integral | Stratonovich Integral |
|--------|--------------|----------------------|
| **Definition** | Left endpoint | Midpoint |
| **Chain rule** | Modified (Itô's lemma) | Classical |
| **Martingale** | Yes | No |
| **Wong-Zakai limit** | No | Yes |
| **Finance** | Standard | Rare |
| **Physics** | Requires care | Natural |

**The choice between Itô and Stratonovich is not about correctness—both are mathematically valid. The choice depends on the modeling context and which properties are most important for your application.**
