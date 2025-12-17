# The Stratonovich Integral

## Introduction

Stochastic calculus provides a fundamental framework for modeling systems influenced by randomness. Financial mathematics, physics, and engineering all rely on stochastic processes to describe the evolution of complex systems over time. Among these processes, **Brownian motion** (or Wiener process) plays a central role.

Two principal notions of stochastic integration with respect to Brownian motion are the **Itô integral** and the **Stratonovich integral**. Although both define integrals of stochastic processes against Brownian motion, they differ significantly in interpretation, mathematical properties, and applications. This section introduces the Stratonovich integral, explains how it differs from the Itô integral, and illustrates the distinction through both theory and simulation.

---

## 1. Step-Function Approximations of Stochastic Integrals

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

## 2. Expected Values of the Corresponding Stochastic Integrals

### 2.1 Left-Endpoint Approximation (Itô)

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

### 2.2 Right-Endpoint Approximation

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

## 3. Itô versus Stratonovich Integrals

The difference between Itô and Stratonovich integration arises from the choice of evaluation point within each partition interval.

### 3.1 Itô Integral

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

### 3.2 Stratonovich Integral

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

## 4. Quadratic Variation and Its Role

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

## 5. Numerical Illustration: Itô vs. Stratonovich

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
