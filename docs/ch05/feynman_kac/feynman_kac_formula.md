# The Feynman–Kac Formula

The **Feynman–Kac formula** is one of the most profound results connecting stochastic differential equations to partial differential equations. It provides a probabilistic representation of solutions to parabolic PDEs and serves as the mathematical foundation for option pricing, risk-neutral valuation, and countless applications in physics and engineering.

---

## Motivation: Why Connect SDEs and PDEs?

Two fundamental perspectives exist for studying diffusion processes:

1. **Probabilistic (SDE)**: Sample paths, expectations, distributions
2. **Analytical (PDE)**: Deterministic equations for expected values

The Feynman–Kac formula bridges these perspectives:

$$
\text{PDE solution} \longleftrightarrow \text{Expected value along SDE paths}
$$

**Why this matters:**

- **Numerical methods**: Monte Carlo (SDE) vs finite differences (PDE)
- **Intuition**: Probabilistic interpretation of PDE solutions
- **Finance**: Risk-neutral pricing as an expectation
- **Physics**: Path integral formulation of quantum mechanics

---

## The Classical Feynman–Kac Formula

### Setting

Consider the SDE:

$$
dX_s = \mu(s, X_s)\,ds + \sigma(s, X_s)\,dW_s, \quad X_t = x
$$

on the interval $[t, T]$, where $X_t = x$ is the initial condition at time $t$.

### Theorem (Feynman–Kac)

Let $u(t, x)$ be a solution to the **parabolic PDE**:

$$
\boxed{
\frac{\partial u}{\partial t} + \mu(t,x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(t,x)\frac{\partial^2 u}{\partial x^2} - r(t,x)u + f(t,x) = 0
}
$$

with **terminal condition**:

$$
u(T, x) = g(x)
$$

Under suitable regularity conditions, $u$ has the **probabilistic representation**:

$$
\boxed{
u(t, x) = \mathbb{E}\left[ e^{-\int_t^T r(s, X_s)\,ds} g(X_T) + \int_t^T e^{-\int_t^s r(\tau, X_\tau)\,d\tau} f(s, X_s)\,ds \,\Big|\, X_t = x \right]
}
$$

### Special Cases

**Case 1: No discounting, no source ($r = 0$, $f = 0$)**

$$
\frac{\partial u}{\partial t} + \mu \frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 u}{\partial x^2} = 0
$$

$$
u(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]
$$

**Case 2: Constant discounting ($r = $ const, $f = 0$)**

$$
u(t, x) = e^{-r(T-t)} \mathbb{E}[g(X_T) \mid X_t = x]
$$

**Case 3: Killing/discounting only ($f = 0$)**

$$
u(t, x) = \mathbb{E}\left[ e^{-\int_t^T r(s, X_s)\,ds} g(X_T) \,\Big|\, X_t = x \right]
$$

---

## Proof Sketch

**Step 1**: Define the process

$$
Y_s = e^{-\int_t^s r(\tau, X_\tau)\,d\tau} u(s, X_s) + \int_t^s e^{-\int_t^\tau r(\xi, X_\xi)\,d\xi} f(\tau, X_\tau)\,d\tau
$$

**Step 2**: Apply Itô's lemma to $e^{-\int_t^s r\,d\tau} u(s, X_s)$:

$$
d\left(e^{-\int_t^s r\,d\tau} u\right) = e^{-\int_t^s r\,d\tau} \left[ -r\,u\,ds + du \right]
$$

where by Itô's lemma:

$$
du = \left( \frac{\partial u}{\partial s} + \mu \frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 u}{\partial x^2} \right) ds + \sigma \frac{\partial u}{\partial x} dW_s
$$

**Step 3**: Substitute the PDE (which says the bracketed term equals $ru - f$):

$$
d\left(e^{-\int_t^s r\,d\tau} u\right) = e^{-\int_t^s r\,d\tau} \left[ -ru + ru - f \right] ds + (\text{martingale term})
$$

$$
= -e^{-\int_t^s r\,d\tau} f\,ds + (\text{martingale term})
$$

**Step 4**: Therefore $Y_s$ is a martingale (the $-f$ term cancels with the integral term).

**Step 5**: By the martingale property:

$$
Y_t = \mathbb{E}[Y_T \mid \mathcal{F}_t]
$$

$$
u(t, x) = \mathbb{E}\left[ e^{-\int_t^T r\,d\tau} g(X_T) + \int_t^T e^{-\int_t^s r\,d\tau} f(s, X_s)\,ds \,\Big|\, X_t = x \right]
$$

$\square$

---

## The Converse: From Expectation to PDE

**Theorem (Converse Feynman–Kac)**: Define

$$
u(t, x) := \mathbb{E}\left[ e^{-\int_t^T r(s, X_s)\,ds} g(X_T) \,\Big|\, X_t = x \right]
$$

Under suitable regularity (e.g., $g$ bounded continuous, coefficients Lipschitz), $u$ is a viscosity solution (and under stronger conditions, a classical solution) to:

$$
\frac{\partial u}{\partial t} + \mathcal{L}u - ru = 0, \quad u(T, x) = g(x)
$$

where $\mathcal{L}$ is the generator of $X_t$.

---

## Connection to the Infinitesimal Generator

The PDE in Feynman–Kac can be written compactly as:

$$
\frac{\partial u}{\partial t} + \mathcal{L}u - ru + f = 0
$$

where the **infinitesimal generator** is:

$$
\mathcal{L} = \mu(t,x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(t,x)\frac{\partial^2}{\partial x^2}
$$

**Interpretation**:

- $\frac{\partial u}{\partial t}$: Time evolution
- $\mathcal{L}u$: Spatial diffusion (drift + volatility)
- $-ru$: Discounting/killing
- $f$: Source/running payoff

---

## Application 1: Black–Scholes Option Pricing

### Setup

Under the risk-neutral measure $\mathbb{Q}$, the stock price follows:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

where $r$ is the risk-free rate.

### European Call Option

The call option with strike $K$ and maturity $T$ has payoff $g(S) = (S - K)^+$.

**By Feynman–Kac**, the price $V(t, S)$ satisfies:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
$$

with $V(T, S) = (S - K)^+$.

**Probabilistic representation**:

$$
V(t, S) = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid S_t = S]
$$

**Explicit solution (Black–Scholes formula)**:

$$
V(t, S) = S\,\Phi(d_1) - Ke^{-r(T-t)}\Phi(d_2)
$$

where:

$$
d_1 = \frac{\log(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}, \quad d_2 = d_1 - \sigma\sqrt{T-t}
$$

---

## Application 2: Bond Pricing with Stochastic Interest Rates

### Vasicek Model

The short rate follows:

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t
$$

### Zero-Coupon Bond

The price of a zero-coupon bond paying $1$ at maturity $T$ is:

$$
P(t, r) = \mathbb{E}\left[ e^{-\int_t^T r_s\,ds} \,\Big|\, r_t = r \right]
$$

**By Feynman–Kac**, $P$ satisfies:

$$
\frac{\partial P}{\partial t} + \kappa(\theta - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2 \frac{\partial^2 P}{\partial r^2} - rP = 0
$$

with $P(T, r) = 1$.

**Explicit solution**:

$$
P(t, r) = A(t, T) e^{-B(t, T) r}
$$

where $A$ and $B$ are deterministic functions (affine term structure).

---

## Application 3: Expected Exit Time (Boundary Value Problem)

### Problem

For Brownian motion $X_t = W_t$ starting at $x \in (a, b)$, find the expected exit time:

$$
u(x) = \mathbb{E}_x[\tau], \quad \tau = \inf\{t \geq 0 : X_t \notin (a, b)\}
$$

### Feynman–Kac Formulation

The function $u(x)$ satisfies:

$$
\mathcal{L}u = -1, \quad u(a) = u(b) = 0
$$

where $\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$ for Brownian motion.

**PDE**:

$$
\frac{1}{2}u''(x) = -1
$$

**Solution**:

$$
u(x) = (x - a)(b - x)
$$

**Interpretation**: Maximum expected exit time at the midpoint $(a+b)/2$.

---

## Multidimensional Feynman–Kac

For an $\mathbb{R}^d$-valued diffusion:

$$
dX_t^i = \mu^i(t, X_t)\,dt + \sigma^{i\alpha}(t, X_t)\,dW_t^\alpha
$$

The Feynman–Kac PDE becomes:

$$
\frac{\partial u}{\partial t} + \mu^i \frac{\partial u}{\partial x^i} + \frac{1}{2}a^{ij}\frac{\partial^2 u}{\partial x^i \partial x^j} - ru + f = 0
$$

where $a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}$ is the diffusion matrix.

---

## Numerical Methods: Monte Carlo vs PDE

The Feynman–Kac formula enables two numerical approaches:

### Monte Carlo (SDE-based)

1. Simulate $N$ paths of $X_t$
2. Compute average of $e^{-\int r\,ds} g(X_T)$
3. Estimate: $\hat{u} = \frac{1}{N}\sum_{i=1}^N e^{-\int_t^T r(s, X_s^{(i)})\,ds} g(X_T^{(i)})$

**Advantages**: High dimensions, complex payoffs, path-dependent options

**Disadvantages**: Slow convergence ($O(1/\sqrt{N})$), variance reduction needed

### Finite Differences (PDE-based)

1. Discretize the PDE on a grid
2. Solve backward from terminal condition
3. Interpolate to get $u(t, x)$

**Advantages**: Fast for low dimensions, all option values at once

**Disadvantages**: Curse of dimensionality, complex boundaries difficult

---

## Regularity Conditions

The Feynman–Kac formula requires:

1. **Coefficients**: $\mu, \sigma, r$ are continuous, satisfy linear growth
2. **Terminal condition**: $g$ is continuous with polynomial growth
3. **Source term**: $f$ is continuous with polynomial growth
4. **Ellipticity**: $\sigma^2(t, x) > 0$ (uniform ellipticity for classical solutions)

**Without ellipticity**: The PDE may have only viscosity solutions, not classical solutions.

---

## Historical Note

The formula is named after:

- **Richard Feynman** (1918–1988): Developed path integral formulation of quantum mechanics
- **Mark Kac** (1914–1984): Proved the rigorous mathematical connection

Feynman's insight: Quantum mechanical propagators can be represented as integrals over all possible paths. Kac made this rigorous using Brownian motion and showed the connection to parabolic PDEs.

---

## Summary

$$
\boxed{
\text{PDE: } \frac{\partial u}{\partial t} + \mathcal{L}u - ru + f = 0 \quad \Longleftrightarrow \quad u(t,x) = \mathbb{E}\left[ e^{-\int_t^T r\,ds} g(X_T) + \int_t^T e^{-\int_t^s r\,d\tau} f\,ds \,\Big|\, X_t = x \right]
}
$$

| Component | PDE Term | Probabilistic Meaning |
|-----------|----------|----------------------|
| Generator $\mathcal{L}$ | Drift + diffusion | Expected local change |
| $-ru$ | Discounting | Killing/interest rate |
| $f$ | Source term | Running payoff |
| $g(x)$ | Terminal condition | Final payoff |

**The Feynman–Kac formula is the fundamental bridge between stochastic analysis and partial differential equations.**

---

## QuantPie Derivation

### Proof via Martingale Methods

**Define the process:**

$$
Y(s) = e^{-\int_t^s V(X_\tau, \tau)d\tau} u(X_s, s) + \int_t^s e^{-\int_t^r V(X_\tau, \tau)d\tau} f(X_r, r)dr
$$

where $u$ solves the PDE:

$$
\frac{\partial u}{\partial t} + \mu(t,x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(t,x)\frac{\partial^2 u}{\partial x^2} - V(t,x)u + f(t,x) = 0
$$

**Applying Itô's Lemma** to the first term:

$$
d\left(e^{-\int_t^s V d\tau}\right) = -V(X_s, s)e^{-\int_t^s V d\tau}ds
$$

$$
du(X_s, s) = \left(\frac{\partial u}{\partial s} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2}\right)ds + \sigma\frac{\partial u}{\partial x}dW_s
$$

**Computing $dY$:**

$$
dY = e^{-\int_t^s V d\tau}\left[-Vu + du\right] + e^{-\int_t^s V d\tau}f ds + (\text{higher order})
$$

$$
= e^{-\int_t^s V d\tau}\left[-Vu + \frac{\partial u}{\partial s} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2} + f\right]ds + (\text{martingale})
$$

**The bracketed term equals zero by the PDE**, leaving only the martingale part:

$$
dY = e^{-\int_t^s V d\tau}\sigma\frac{\partial u}{\partial x}dW_s
$$

**Therefore $Y(s)$ is a martingale:**

$$
Y(t) = \mathbb{E}[Y(T) | \mathcal{F}_t]
$$

$$
u(t, x) = \mathbb{E}\left[e^{-\int_t^T V d\tau}u(X_T, T) + \int_t^T e^{-\int_t^s V d\tau}f(X_s, s)ds \,\Big|\, X_t = x\right]
$$

### Examples: Diffusion Equations

**Example 1: Pure Diffusion (No Drift, No Discounting)**

$$
\frac{\partial u}{\partial t} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2} = 0, \quad u(T, x) = x^2
$$

**Stochastic process:** $dX = \sigma dB_t$

$$
X_T = X_t + \sigma(B_T - B_t)
$$

**Solution by Feynman-Kac:**

$$
\begin{aligned}
u(t, X_t) &= \mathbb{E}[X_T^2 | X_t] \\
&= \mathbb{E}[(X_t + \sigma(B_T - B_t))^2] \\
&= X_t^2 + \sigma^2(T - t)
\end{aligned}
$$

**Example 2: Diffusion with Drift**

$$
\frac{\partial u}{\partial t} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2} + \mu\frac{\partial u}{\partial x} = 0, \quad u(T, x) = x^2
$$

**Stochastic process:** $dX = \mu dt + \sigma dB_t$

$$
X_T = X_t + \mu(T - t) + \sigma(B_T - B_t)
$$

**Solution:**

$$
\begin{aligned}
u(t, X_t) &= \mathbb{E}[X_T^2] \\
&= \mathbb{E}[(X_t + \mu(T-t) + \sigma(B_T - B_t))^2] \\
&= (X_t + \mu(T-t))^2 + \sigma^2(T-t)
\end{aligned}
$$

### Key Insight

The Feynman-Kac formula shows that **solving the PDE is equivalent to computing an expectation**. This opens two computational paths:

1. **Analytical:** Solve the PDE directly (finite differences, separation of variables)
2. **Probabilistic:** Simulate the SDE and average payoffs (Monte Carlo)

Each approach has advantages depending on dimensionality and problem structure.
