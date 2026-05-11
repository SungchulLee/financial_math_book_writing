# The Heat Equation

The heat equation is the canonical partial differential equation describing diffusion. It plays a central role in probability theory, stochastic processes, and mathematical finance, serving as the prototype for all parabolic PDEs.

---

## The Equation

In one spatial dimension, the heat equation is:

$$
\boxed{
\frac{\partial u}{\partial t}(t,x) = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}(t,x), \quad (t,x) \in (0,\infty) \times \mathbb{R}
}
$$

with initial condition:

$$
u(0,x) = f(x)
$$

Here $u(t,x)$ represents:

- **Physics**: Temperature at position $x$ and time $t$
- **Probability**: Density of particles diffusing from initial distribution $f$
- **Finance**: Value function for certain derivative contracts

---

## Why the Factor 1/2?

The coefficient $\frac{1}{2}$ aligns with standard Brownian motion ($\text{Var}(B_t) = t$), making the heat kernel equal the Brownian density and the generator $\mathcal{L} = \frac{1}{2}\partial_{xx}$. Physics texts often use $u_t = \kappa u_{xx}$ instead; setting $\kappa = \frac{1}{2}$ gives our normalization.

---

## Physical Derivation

The heat equation arises from two physical principles:

**1. Conservation of energy**: 

$$
\frac{\partial u}{\partial t} = -\frac{\partial q}{\partial x}
$$

where $q$ is the heat flux.

**2. Fourier's law**: Heat flows from hot to cold proportionally to the temperature gradient:

$$
q = -\kappa \frac{\partial u}{\partial x}
$$

Combining these:

$$
\frac{\partial u}{\partial t} = \kappa \frac{\partial^2 u}{\partial x^2}
$$

---

## Classification: Parabolic PDEs

The heat equation is the prototype of **parabolic** PDEs.

**General second-order linear PDE**:

$$
Au_{xx} + 2Bu_{xy} + Cu_{yy} + \text{lower order} = 0
$$

**Classification** (by discriminant $B^2 - AC$):

| Type | Condition | Example | Behavior |
|------|-----------|---------|----------|
| Elliptic | $B^2 - AC < 0$ | Laplace: $u_{xx} + u_{yy} = 0$ | Equilibrium |
| Parabolic | $B^2 - AC = 0$ | Heat: $u_t = u_{xx}$ | Diffusion |
| Hyperbolic | $B^2 - AC > 0$ | Wave: $u_{tt} = u_{xx}$ | Propagation |

---

## Key Qualitative Properties

### 1. Smoothing (Regularization)

Even if the initial data $f$ is rough (e.g., discontinuous), the solution $u(t,\cdot)$ becomes **infinitely differentiable** for any $t > 0$.

**Intuition**: Diffusion averages out irregularities.

### 2. Infinite Speed of Propagation

If $f$ has compact support, $u(t,x) > 0$ for all $x \in \mathbb{R}$ and $t > 0$.

**Contrast with wave equation**: Information travels at finite speed for hyperbolic equations.

### 3. Conservation of Mass

If $\int_{\mathbb{R}} f(x)\,dx = M$, then:

$$
\int_{\mathbb{R}} u(t,x)\,dx = M \quad \text{for all } t > 0
$$

Total "heat" (or probability mass) is conserved.

### 4. Positivity Preservation

If $f(x) \geq 0$ for all $x$, then $u(t,x) \geq 0$ for all $t > 0$ and $x \in \mathbb{R}$.

**Probabilistic meaning**: Densities remain non-negative.

### 5. Decay of Maximum

$$
\max_x u(t,x) \leq \max_x f(x)
$$

The maximum temperature decreases over time (in the absence of sources).

---

## The Heat Equation in Higher Dimensions

In $\mathbb{R}^d$:

$$
\frac{\partial u}{\partial t} = \frac{1}{2}\Delta u = \frac{1}{2}\sum_{i=1}^d \frac{\partial^2 u}{\partial x_i^2}
$$

The fundamental solution becomes:

$$
G(t,x) = \frac{1}{(2\pi t)^{d/2}} \exp\left(-\frac{|x|^2}{2t}\right)
$$

This is the density of $d$-dimensional Brownian motion $B_t \in \mathbb{R}^d$.

---

## Boundary Value Problems

On a bounded domain $\Omega \subset \mathbb{R}^d$:

$$
\begin{cases}
u_t = \frac{1}{2}\Delta u & \text{in } (0,T) \times \Omega \\
u(0,x) = f(x) & \text{initial condition} \\
u(t,x) = g(t,x) & \text{on } (0,T) \times \partial\Omega \text{ (Dirichlet)}
\end{cases}
$$

**Neumann conditions**: Specify $\frac{\partial u}{\partial n}$ on the boundary (insulated boundary).

---

## Connection to Brownian Motion

The heat equation is the analytical counterpart of Brownian motion: solutions can be written as expectations over Brownian paths, formalized by the **Feynman-Kac theorem**. See [Heat Equation and Brownian Motion](heat_equation_and_brownian_motion.md) for the full generator/martingale/density correspondence.

---

## Historical Note

- **Joseph Fourier** (1822): Derived the heat equation and introduced Fourier series to solve it
- **Norbert Wiener** (1923): Constructed Brownian motion rigorously
- **Andrey Kolmogorov** (1931): Connected diffusions to parabolic PDEs
- **Mark Kac** (1949): Probabilistic interpretation of PDE solutions

---

## Summary

$$
\boxed{
u_t = \frac{1}{2}u_{xx} \quad \longleftrightarrow \quad \text{Brownian motion}
}
$$

The heat equation describes:

- Diffusion of heat, particles, or probability
- Smoothing of initial irregularities
- Conservation of total mass
- The analytical side of Brownian motion

**The heat equation is the simplest parabolic PDE and the gateway to understanding diffusion processes.**

---

## QuantPie Derivation

### Derivation from Particle Conservation

The heat equation emerges naturally from modeling particle diffusion. Consider particles randomly moving in space, where the position change $\Delta$ has probability density $\phi(\Delta)$.

**Number of particles at time $t + \tau$:**

$$
f(x, t+\tau) = \int_{-\infty}^{\infty} f(x-\Delta, t) \phi(\Delta) d\Delta
$$

**Taylor expansion:**

- Time: $f(x, t+\tau) = f(x, t) + \frac{\partial f}{\partial t}\tau$
- Position: $f(x-\Delta, t) = f(x, t) - \frac{\partial f}{\partial x}\Delta + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\Delta^2$

**Substituting and using the fact that $\phi$ is even** (symmetric distribution):

$$
f(x, t) + \frac{\partial f}{\partial t}\tau = f(x, t) \int \phi(\Delta)d\Delta - \frac{\partial f}{\partial x}\int \Delta\phi(\Delta)d\Delta + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\int \Delta^2\phi(\Delta)d\Delta
$$

Since $\int \phi(\Delta)d\Delta = 1$ and $\int \Delta\phi(\Delta)d\Delta = 0$ (by symmetry):

$$
\frac{\partial f}{\partial t}\tau = \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\int \Delta^2\phi(\Delta)d\Delta
$$

**Defining diffusion coefficient** $D = \frac{1}{\tau}\int \Delta^2\phi(\Delta)d\Delta$ (variance per unit time):

$$
\frac{\partial f}{\partial t} = \frac{D}{2}\frac{\partial^2 f}{\partial x^2}
$$

**Physical interpretation:** If neighboring regions have more particles on average, particles diffuse in to increase the local density. Conversely, if neighbors are depleted, the region loses particles.

### Fundamental Solution

The heat equation admits a Gaussian fundamental solution (Green's function); see [Fundamental Solution](fundamental_solution.md) for the Fourier derivation and verification, and [Scaling and Invariance](scaling_and_invariance.md) for the self-similarity derivation. The general solution is the convolution $u(x,t) = \int u(x_0,0)\,G(x,t;x_0)\,dx_0$ — superposing point sources weighted by the initial data.

---

## Exercises

**Exercise 1.**
Write the one-dimensional heat equation $\partial_t u = \frac{1}{2}\partial_{xx}u$ and verify that $u(x, t) = e^{-\alpha^2 t/2}\sin(\alpha x)$ is a solution for any constant $\alpha$. What initial condition does this correspond to?

??? success "Solution to Exercise 1"
    The one-dimensional heat equation is:

    $$
    \frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}
    $$

    Let $u(x,t) = e^{-\alpha^2 t/2}\sin(\alpha x)$. We compute each side.

    **Left side**:

    $$
    \partial_t u = -\frac{\alpha^2}{2}e^{-\alpha^2 t/2}\sin(\alpha x)
    $$

    **Right side**: First, $\partial_x u = \alpha e^{-\alpha^2 t/2}\cos(\alpha x)$. Then:

    $$
    \partial_{xx}u = -\alpha^2 e^{-\alpha^2 t/2}\sin(\alpha x)
    $$

    So:

    $$
    \frac{1}{2}\partial_{xx}u = -\frac{\alpha^2}{2}e^{-\alpha^2 t/2}\sin(\alpha x) = \partial_t u \quad \checkmark
    $$

    The initial condition is $u(x,0) = \sin(\alpha x)$. This is a single Fourier mode that decays exponentially in time at rate $\alpha^2/2$. Higher-frequency modes (larger $\alpha$) decay faster, which is the smoothing property of the heat equation.

---

**Exercise 2.**
Use the superposition formula $u(x, t) = \int_{-\infty}^{\infty}u(x_0, 0)\,G(x, t; x_0)\,dx_0$ to solve the heat equation with initial condition $u(x, 0) = e^{-x^2}$. Express your answer in closed form.

??? success "Solution to Exercise 2"
    Using the superposition formula with $u(x_0, 0) = e^{-x_0^2}$ and $G(x,t;x_0) = (4\pi D t)^{-1/2}\exp(-(x-x_0)^2/(4Dt))$ with $D = 1/2$:

    $$
    u(x,t) = \int_{-\infty}^{\infty} e^{-x_0^2} \cdot \frac{1}{\sqrt{2\pi t}}\exp\!\left(-\frac{(x - x_0)^2}{2t}\right)dx_0
    $$

    Combine the exponents:

    $$
    -x_0^2 - \frac{(x-x_0)^2}{2t} = -x_0^2 - \frac{x^2 - 2xx_0 + x_0^2}{2t} = -x_0^2\left(1 + \frac{1}{2t}\right) + \frac{xx_0}{t} - \frac{x^2}{2t}
    $$

    Let $A = 1 + \frac{1}{2t} = \frac{2t+1}{2t}$. Completing the square in $x_0$:

    $$
    -A\left(x_0 - \frac{x}{2tA}\right)^2 + \frac{x^2}{4t^2 A} - \frac{x^2}{2t}
    $$

    The residual term simplifies: $\frac{x^2}{4t^2 A} - \frac{x^2}{2t} = \frac{x^2}{2t}\left(\frac{1}{2tA} - 1\right) = -\frac{x^2}{2t+1}$.

    The Gaussian integral in $x_0$ evaluates to $\sqrt{\pi/A} = \sqrt{2\pi t/(2t+1)}$. Combining:

    $$
    u(x,t) = \frac{1}{\sqrt{2\pi t}} \cdot \sqrt{\frac{2\pi t}{2t+1}} \cdot \exp\!\left(-\frac{x^2}{2t+1}\right) = \frac{1}{\sqrt{2t+1}}\exp\!\left(-\frac{x^2}{2t+1}\right)
    $$

    At $t = 0$: $u(x,0) = e^{-x^2}$, confirming the initial condition. The solution is a Gaussian that broadens over time, with variance growing from $1/2$ to $(2t+1)/2$.

---

**Exercise 3.**
The heat equation describes the diffusion of heat. In one dimension, if heat is initially concentrated at $x = 0$, describe qualitatively how the temperature profile evolves over time. Relate this to the spreading Gaussian kernel.

??? success "Solution to Exercise 3"
    At $t = 0$, the heat is concentrated at $x = 0$, represented by the Dirac delta $\delta(x)$ (or approximately by a very narrow, tall Gaussian).

    As $t$ increases, the temperature profile evolves as the Gaussian kernel $G(t,x) = (2\pi t)^{-1/2}\exp(-x^2/(2t))$:

    - The peak height decreases as $1/\sqrt{t}$
    - The width (standard deviation) grows as $\sqrt{t}$
    - The total area (total heat) is conserved at $1$
    - The profile remains symmetric about $x = 0$

    Physically, heat flows from hot regions to cold regions. The initial concentration spreads outward in both directions. The spreading is self-similar: the profile at any time is just a rescaled version of the profile at any other time, with the characteristic width proportional to $\sqrt{t}$.

---

**Exercise 4.**
Classify the heat equation $\partial_t u = D\,\partial_{xx}u$ in terms of the PDE classification (parabolic, elliptic, hyperbolic). Explain why the parabolic type is associated with diffusion rather than wave propagation.

??? success "Solution to Exercise 4"
    The heat equation $\partial_t u = D\,\partial_{xx}u$ has the form $Au_{xx} + 2Bu_{xt} + Cu_{tt} + \text{lower order} = 0$ where we identify $A = D$, $B = 0$, $C = 0$ (there is no $u_{tt}$ term). The discriminant is:

    $$
    B^2 - AC = 0 - D \cdot 0 = 0
    $$

    Since $B^2 - AC = 0$, the equation is **parabolic**.

    **Why parabolic = diffusion, not waves**: The parabolic type has only a first-order time derivative, meaning information propagates instantaneously (infinite speed of propagation) but with exponential decay of high-frequency modes. In contrast:

    - **Hyperbolic** equations ($B^2 - AC > 0$, e.g., the wave equation $u_{tt} = c^2 u_{xx}$) have a second-order time derivative, supporting wave propagation at finite speed $c$
    - **Elliptic** equations ($B^2 - AC < 0$, e.g., Laplace's equation) describe equilibrium states with no time evolution

    The heat equation describes an irreversible process: initial irregularities are smoothed out and cannot be recovered, reflecting the dissipative nature of diffusion.

---

**Exercise 5.**
Consider the heat equation on a finite interval $[0, L]$ with $u(0, t) = u(L, t) = 0$. Using separation of variables $u(x, t) = X(x)T(t)$, find the general solution as a Fourier sine series. What happens to the solution as $t \to \infty$?

??? success "Solution to Exercise 5"
    Using separation of variables $u(x,t) = X(x)T(t)$, substitute into $\partial_t u = \frac{1}{2}\partial_{xx}u$:

    $$
    X(x)T'(t) = \frac{1}{2}X''(x)T(t) \implies \frac{T'(t)}{T(t)} = \frac{X''(x)}{2X(x)} = -\lambda
    $$

    where $\lambda$ is the separation constant (taken negative for decay).

    **Spatial equation**: $X'' + 2\lambda X = 0$ with $X(0) = X(L) = 0$.

    For nontrivial solutions, $2\lambda > 0$ and $X(x) = \sin(n\pi x/L)$ with $2\lambda_n = (n\pi/L)^2$, giving $\lambda_n = n^2\pi^2/(2L^2)$ for $n = 1, 2, 3, \ldots$

    **Temporal equation**: $T'(t) = -\lambda_n T(t)$, so $T_n(t) = e^{-\lambda_n t} = e^{-n^2\pi^2 t/(2L^2)}$.

    **General solution** by superposition:

    $$
    u(x,t) = \sum_{n=1}^{\infty} b_n \sin\!\left(\frac{n\pi x}{L}\right) e^{-n^2\pi^2 t/(2L^2)}
    $$

    where $b_n = \frac{2}{L}\int_0^L f(x)\sin(n\pi x/L)\,dx$ are the Fourier sine coefficients of the initial data.

    **As $t \to \infty$**: Every exponential $e^{-n^2\pi^2 t/(2L^2)} \to 0$. The $n = 1$ mode decays slowest, so the solution approaches zero, with the decay rate dominated by $e^{-\pi^2 t/(2L^2)}$. Physically, the heat leaks out through the fixed-temperature boundaries until the rod reaches equilibrium at $u = 0$.

---

**Exercise 6.**
The diffusion coefficient $D = \sigma^2/2$ determines the rate of spreading. For $D = 0.045$ (corresponding to $\sigma = 0.30$), compute the standard deviation of the Gaussian kernel after $t = 1$ year and $t = 4$ years. Verify that the standard deviation grows as $\sqrt{t}$.

??? success "Solution to Exercise 6"
    The standard deviation of the Gaussian kernel at time $t$ is $\sigma_{\text{kernel}} = \sqrt{2Dt}$. With $D = 0.045$:

    **After $t = 1$ year**:

    $$
    \sigma_{\text{kernel}} = \sqrt{2 \times 0.045 \times 1} = \sqrt{0.09} = 0.30
    $$

    **After $t = 4$ years**:

    $$
    \sigma_{\text{kernel}} = \sqrt{2 \times 0.045 \times 4} = \sqrt{0.36} = 0.60
    $$

    **Verification of $\sqrt{t}$ growth**: The ratio of standard deviations is $0.60/0.30 = 2 = \sqrt{4/1} = \sqrt{t_2/t_1}$, confirming that the standard deviation grows as $\sqrt{t}$. Doubling the standard deviation requires quadrupling the time, which is the hallmark of diffusive (rather than ballistic) spreading.

---

**Exercise 7.**
Explain why the heat equation is a good model for option pricing through the Black-Scholes PDE. After the change of variables that transforms the Black-Scholes PDE into the heat equation, what do the spatial variable, time variable, and initial condition represent in financial terms?

??? success "Solution to Exercise 7"
    The Black-Scholes PDE for a European option with price $V(S,t)$ is:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
    $$

    This is a parabolic PDE (like the heat equation) because the underlying stock price follows geometric Brownian motion, which is a diffusion process.

    **Change of variables**: Set $x = \log S$ (so $S = e^x$), $\tau = T - t$ (time to maturity), and $V(S,t) = e^{-r\tau}v(x,\tau)$ (remove discounting). After substitution, the PDE becomes:

    $$
    \frac{\partial v}{\partial \tau} = \frac{1}{2}\sigma^2\frac{\partial^2 v}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial v}{\partial x}
    $$

    A further substitution $v(x,\tau) = e^{\alpha x + \beta \tau}w(x,\tau)$ with appropriate $\alpha, \beta$ eliminates the first-order and zeroth-order terms, yielding the standard heat equation $\partial_\tau w = \frac{\sigma^2}{2}\partial_{xx}w$.

    **Financial interpretation of the transformed variables**:

    - **Spatial variable** $x = \log S$: the log-price of the underlying asset
    - **Time variable** $\tau = T - t$: time to maturity (running forward from $0$ at expiry)
    - **Initial condition** $w(x, 0)$: a transformed version of the option payoff $g(e^x)$ at expiry, e.g., $\max(e^x - K, 0)$ for a call option

    The heat equation is the right model because the log-price of a stock under geometric Brownian motion is a diffusion process, and the option price is an expected value of the payoff -- exactly the convolution with the heat kernel.
