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

---

## Exercises

**Exercise 1.**
State the Feynman-Kac formula for the special case $r = 0$, $f = 0$. Write the PDE and its probabilistic representation. For the SDE $dX_s = \sigma\,dW_s$ with $g(x) = x^4$, compute $u(t, x) = \mathbb{E}[X_T^4 | X_t = x]$ and verify your answer satisfies the PDE.

??? success "Solution to Exercise 1"
    With $r = 0$ and $f = 0$, the Feynman-Kac formula reduces to:

    **PDE**: $\frac{\partial u}{\partial t} + \frac{1}{2}\sigma^2(t,x)\frac{\partial^2 u}{\partial x^2} = 0$ (using $\mu = 0$ for $dX_s = \sigma\,dW_s$)

    **Probabilistic representation**: $u(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$

    For $g(x) = x^4$ and $dX_s = \sigma\,dW_s$, we have $X_T = x + \sigma(W_T - W_t)$. Let $Z = W_T - W_t \sim N(0, T-t)$.

    $$
    u(t, x) = \mathbb{E}[(x + \sigma Z)^4]
    $$

    Expanding via the binomial theorem and using $\mathbb{E}[Z] = 0$, $\mathbb{E}[Z^2] = T - t$, $\mathbb{E}[Z^3] = 0$, and $\mathbb{E}[Z^4] = 3(T-t)^2$:

    $$
    u(t, x) = x^4 + 6x^2\sigma^2(T - t) + 3\sigma^4(T - t)^2
    $$

    **Verification**: $u_t = -6x^2\sigma^2 - 6\sigma^4(T - t)$, $u_{xx} = 12x^2 + 12\sigma^2(T - t)$. Then:

    $$
    u_t + \frac{1}{2}\sigma^2 u_{xx} = -6x^2\sigma^2 - 6\sigma^4(T-t) + \frac{1}{2}\sigma^2(12x^2 + 12\sigma^2(T-t)) = 0 \;\checkmark
    $$

---

**Exercise 2.**
In the proof of the Feynman-Kac formula, the process $Y_s = e^{-\int_t^s r\,d\tau}u(s, X_s)$ is shown to be a martingale when $f = 0$. Explain which step in the proof ensures the $ds$ term vanishes, and why the Ito correction from the exponential and from $u(s, X_s)$ must both be accounted for.

??? success "Solution to Exercise 2"
    In the proof, we define $Y_s = e^{-\int_t^s r\,d\tau}u(s, X_s)$ and apply Ito's lemma to obtain:

    $$
    dY_s = e^{-\int_t^s r\,d\tau}\!\left[\partial_s u + \mathcal{L}u - r\,u\right]ds + e^{-\int_t^s r\,d\tau}\,\sigma\,u_x\,dW_s
    $$

    The step that ensures the $ds$ term vanishes is **Step 3 / Step 4**: we substitute the PDE $\partial_t u + \mathcal{L}u - r\,u = 0$ into the bracketed expression. The Ito lemma on $u(s, X_s)$ produces the terms $\partial_s u + \mu\,u_x + \frac{1}{2}\sigma^2\,u_{xx}$, which equals $\partial_s u + \mathcal{L}u$. The product rule with the exponential discount factor $e^{-\int r\,d\tau}$ contributes the $-r\,u$ term.

    Both corrections must be accounted for:

    - The Ito correction from $u(s, X_s)$: the term $\frac{1}{2}\sigma^2 u_{xx}$ arises from the quadratic variation of $X_s$.
    - The correction from the exponential: $d(e^{-\int_t^s r\,d\tau}) = -r\,e^{-\int_t^s r\,d\tau}\,ds$ contributes the $-r\,u$ factor.

    Together, the drift of $Y_s$ is $e^{-\int r\,d\tau}(\partial_s u + \mathcal{L}u - r\,u) = 0$ by the PDE, leaving only the martingale part.

---

**Exercise 3.**
For the expected exit time problem with $\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$, $a = 0$, $b = 1$, verify that $u(x) = x(1-x)$ satisfies $\frac{1}{2}u''(x) = -1$ with $u(0) = u(1) = 0$. What is the maximum expected exit time and where is it achieved?

??? success "Solution to Exercise 3"
    With $a = 0$, $b = 1$, we need $u(x) = x(1-x)$ to satisfy $\frac{1}{2}u''(x) = -1$ with $u(0) = u(1) = 0$.

    **Boundary conditions**: $u(0) = 0 \cdot 1 = 0$ $\checkmark$, $u(1) = 1 \cdot 0 = 0$ $\checkmark$.

    **PDE**: $u'(x) = 1 - 2x$, $u''(x) = -2$. Therefore:

    $$
    \frac{1}{2}u''(x) = \frac{1}{2}(-2) = -1 \;\checkmark
    $$

    **Maximum expected exit time**: Since $u(x) = x(1-x) = -(x - 1/2)^2 + 1/4$ is a downward-opening parabola, the maximum is at $x = 1/2$ with value $u(1/2) = 1/4$.

    The maximum expected exit time is $1/4$, achieved at the midpoint $x = 1/2$ of the interval $[0, 1]$. This makes intuitive sense: starting at the center maximizes the distance to both boundaries, so the Brownian motion takes the longest (in expectation) to exit.

---

**Exercise 4.**
Consider the converse Feynman-Kac theorem: define $u(t,x) = \mathbb{E}[e^{-r(T-t)}g(X_T) | X_t = x]$ where $dX_s = \mu X_s\,ds + \sigma X_s\,dW_s$ (geometric Brownian motion) and $g(x) = (x - K)^+$. Write the PDE that $u$ satisfies without solving it explicitly. This is the Black-Scholes PDE.

??? success "Solution to Exercise 4"
    For geometric Brownian motion $dX_s = \mu X_s\,ds + \sigma X_s\,dW_s$, the infinitesimal generator is:

    $$
    \mathcal{L} = \mu x\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2}{\partial x^2}
    $$

    By the converse Feynman-Kac theorem, $u(t, x) = \mathbb{E}[e^{-r(T-t)}(X_T - K)^+ \mid X_t = x]$ satisfies:

    $$
    \frac{\partial u}{\partial t} + \mu x\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2 u}{\partial x^2} - r\,u = 0
    $$

    with terminal condition $u(T, x) = (x - K)^+$.

    Under risk-neutral pricing where $\mu = r$ (the drift equals the risk-free rate), this becomes the **Black-Scholes PDE**:

    $$
    \frac{\partial u}{\partial t} + rx\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2 u}{\partial x^2} - r\,u = 0
    $$

---

**Exercise 5.**
For the multidimensional Feynman-Kac formula with two assets $X_t = (S_t^1, S_t^2)$, write the generator $\mathcal{L}$ in terms of the drift vector $(\mu^1, \mu^2)$, the diffusion matrix $a^{ij} = \sum_\alpha \sigma^{i\alpha}\sigma^{j\alpha}$, and partial derivatives. Identify the cross-derivative term $a^{12}\partial^2 u / \partial x^1 \partial x^2$ and explain its financial significance.

??? success "Solution to Exercise 5"
    For two correlated assets, the diffusion matrix has entries $a^{ij} = \sum_\alpha \sigma^{i\alpha}\sigma^{j\alpha}$. The generator is:

    $$
    \mathcal{L} = \mu^1\frac{\partial}{\partial x^1} + \mu^2\frac{\partial}{\partial x^2} + \frac{1}{2}a^{11}\frac{\partial^2}{\partial (x^1)^2} + a^{12}\frac{\partial^2}{\partial x^1 \partial x^2} + \frac{1}{2}a^{22}\frac{\partial^2}{\partial (x^2)^2}
    $$

    where the diagonal terms are $a^{11} = \sum_\alpha (\sigma^{1\alpha})^2$ and $a^{22} = \sum_\alpha (\sigma^{2\alpha})^2$, and the cross term is $a^{12} = \sum_\alpha \sigma^{1\alpha}\sigma^{2\alpha}$.

    In financial terms, if $S^1$ and $S^2$ are two stock prices with volatilities $\sigma_1$, $\sigma_2$ and correlation $\rho$, then $a^{11} = \sigma_1^2 (S^1)^2$, $a^{22} = \sigma_2^2 (S^2)^2$, and $a^{12} = \rho\sigma_1\sigma_2 S^1 S^2$.

    **Financial significance of the cross-derivative term**: The term $a^{12}\frac{\partial^2 u}{\partial x^1 \partial x^2} = \rho\sigma_1\sigma_2 S^1 S^2\frac{\partial^2 u}{\partial S^1 \partial S^2}$ captures the effect of **correlation** between the two assets on the derivative price. When $\rho > 0$, the assets tend to move together, and this cross-sensitivity (sometimes called "cross-gamma") measures how the option value changes when both assets move simultaneously. For products like spread options, basket options, or quanto options, this correlation term is crucial and cannot be ignored.

---

**Exercise 6.**
Compare Monte Carlo and finite difference methods for computing the Feynman-Kac solution. For a European call option in the Black-Scholes model ($d = 1$), explain why finite differences are efficient. For a basket option on $d = 10$ stocks, explain why Monte Carlo is preferred. What is the "curse of dimensionality"?

??? success "Solution to Exercise 6"
    **Monte Carlo**: Justified by writing $u(t,x) = \mathbb{E}[e^{-\int r\,ds}g(X_T) \mid X_t = x]$, we simulate $N$ independent paths of the SDE, compute the discounted payoff for each, and average. The error is $O(1/\sqrt{N})$ regardless of dimension.

    **Finite differences**: Justified by the PDE $\partial_t u + \mathcal{L}u - ru + f = 0$, we discretize on a grid and solve backward from the terminal condition. The cost grows as $O(N_{\text{grid}}^d)$ where $d$ is the spatial dimension.

    **European call ($d = 1$)**: Finite differences are efficient. A grid of $N_S = 200$ stock prices and $N_t = 100$ time steps gives $20{,}000$ points, and the tridiagonal linear system is solved in $O(N_S)$ per time step. The method provides the option value at every grid point simultaneously, which is useful for computing Greeks. Monte Carlo achieves comparable accuracy only with thousands of paths.

    **Basket option ($d = 10$)**: Monte Carlo is strongly preferred. A finite difference grid with $N = 50$ points per dimension would require $50^{10} \approx 10^{17}$ grid points, which is computationally impossible. Monte Carlo, however, remains feasible: simulating $10^6$ paths of 10 correlated stocks is routine, with cost $O(10^6 \times 10 \times N_t)$.

    The **curse of dimensionality** refers to the exponential growth of grid-based methods with dimension $d$. The number of grid points scales as $N^d$, making PDE methods impractical for $d \geq 4$. Monte Carlo avoids this curse because its convergence rate $O(1/\sqrt{N})$ does not depend on $d$.

---

**Exercise 7.**
The Feynman-Kac formula requires regularity conditions including uniform ellipticity ($\sigma^2(t,x) > 0$). Explain what goes wrong at $x = 0$ for the CEV model $dX_t = \sigma X_t^{\beta}\,dW_t$ with $\beta \in (0, 1)$, where $\sigma^2(t,x) = \sigma^2 x^{2\beta}$ vanishes at the origin. What type of solution (classical or viscosity) can still be obtained?

??? success "Solution to Exercise 7"
    In the CEV model $dX_t = \sigma X_t^{\beta}\,dW_t$ with $\beta \in (0, 1)$, the diffusion coefficient is $\sigma^2(t, x) = \sigma^2 x^{2\beta}$. At $x = 0$, this vanishes: $\sigma^2(t, 0) = 0$.

    **What goes wrong**: The Feynman-Kac PDE is:

    $$
    \frac{\partial u}{\partial t} + \frac{1}{2}\sigma^2 x^{2\beta}\frac{\partial^2 u}{\partial x^2} = 0
    $$

    At $x = 0$, the second-order term disappears entirely, and the PDE degenerates from parabolic to first-order (or trivial). This means:

    1. **Loss of uniform ellipticity**: The condition $\sigma^2(t, x) \geq \epsilon > 0$ (required for classical regularity theory) fails at $x = 0$.
    2. **Ito's lemma may not apply classically**: The proof of Feynman-Kac requires $u \in C^{1,2}$, but the degenerate PDE may not admit $C^{1,2}$ solutions. The second derivative $u_{xx}$ may blow up near $x = 0$ to compensate for the vanishing diffusion coefficient.
    3. **Boundary behavior**: For $\beta \in (0, 1)$, the process $X_t$ can reach zero, and the behavior at zero (absorption vs. reflection) must be specified, adding a boundary condition that the standard Feynman-Kac setup does not address.

    **Viscosity solutions**: Even when classical ($C^{1,2}$) solutions do not exist, the function $u(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$ is still well-defined as an expectation. It can be shown to be a **viscosity solution** of the degenerate PDE. Viscosity solutions require only continuity (not differentiability) and are defined through comparison with smooth test functions. Uniqueness of viscosity solutions can often be established even for degenerate equations, preserving the Feynman-Kac connection in a weaker but rigorous sense.
