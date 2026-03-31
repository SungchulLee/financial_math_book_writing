# Green's Function for Parabolic PDEs

A **Green's function** is the response of a linear PDE to a point source -- a delta function impulse at a single point in space and time. For parabolic equations, the Green's function encodes the complete solution operator: once you know how the system responds to a point source, you can build the solution for arbitrary data by superposition. In finance, the Green's function is the **transition density** of the underlying stochastic process.

---

## Intuition

Imagine injecting a unit of heat at a single point $y$ at time $s$. The Green's function $G(t, x; s, y)$ describes how this heat spreads to point $x$ at a later time $t > s$.

- At the injection moment: $G$ is a delta function concentrated at $y$
- For $t > s$: the heat diffuses outward, forming a bell curve that flattens and broadens
- As $t \to \infty$: the heat dissipates (on unbounded domains) or reaches equilibrium (on bounded domains)

The solution for arbitrary initial data $f(x)$ is obtained by superposition:

$$
u(t, x) = \int G(t, x; 0, y)\,f(y)\,dy
$$

Each point $y$ contributes its share $f(y)$ of heat, weighted by the Green's function.

---

## Definition

### The Parabolic Operator

Consider a general parabolic operator:

$$
\mathcal{P}u = \frac{\partial u}{\partial t} - \mathcal{L}u
$$

where $\mathcal{L}$ is a second-order elliptic operator:

$$
\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}
$$

### Green's Function

The **Green's function** $G(t, x; s, y)$ is the fundamental solution of $\mathcal{P}$:

$$
\boxed{
\mathcal{P}_x G(t, x; s, y) = \frac{\partial G}{\partial t} - \mathcal{L}_x G = 0, \quad t > s
}
$$

with the **initial condition**:

$$
\lim_{t \downarrow s} G(t, x; s, y) = \delta(x - y)
$$

Here $\mathcal{L}_x$ denotes differentiation with respect to $x$.

**Interpretation**: $G(t, x; s, y)$ is the solution at $(t, x)$ due to a unit impulse at $(s, y)$.

---

## Construction for the Heat Equation

### Free-Space Green's Function

For the standard heat equation $u_t = \frac{1}{2}u_{xx}$ on $\mathbb{R}$, the Green's function is the **heat kernel**:

$$
\boxed{
G(t, x; s, y) = \frac{1}{\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x-y)^2}{2(t-s)}\right), \quad t > s
}
$$

**Verification:**

1. **Satisfies the heat equation** in $(t, x)$ for $t > s$ -- direct computation (see [Fundamental Solution](../heat_equation/fundamental_solution.md))
2. **Initial condition**: As $t \downarrow s$, $G(t, x; s, y) \to \delta(x - y)$ (the Gaussian concentrates at $y$)

### Translation Invariance

For constant-coefficient equations, the Green's function depends only on differences:

$$
G(t, x; s, y) = G(t - s, x - y; 0, 0) = \Gamma(t - s, x - y)
$$

where $\Gamma(\tau, z) = \frac{1}{\sqrt{2\pi\tau}}\,e^{-z^2/2\tau}$ is the fundamental solution.

---

## Solution by Superposition

### Initial Value Problem

For $u_t = \frac{1}{2}u_{xx}$ with $u(0, x) = f(x)$:

$$
\boxed{
u(t, x) = \int_{-\infty}^{\infty} G(t, x; 0, y)\,f(y)\,dy
}
$$

This is a convolution: $u(t, \cdot) = G(t, \cdot; 0, 0) * f$.

### Source Problem

For $u_t - \frac{1}{2}u_{xx} = h(t, x)$ with $u(0, x) = 0$:

$$
u(t, x) = \int_0^t \int_{-\infty}^{\infty} G(t, x; s, y)\,h(s, y)\,dy\,ds
$$

This is the **Duhamel principle**: the response to a distributed source is the integral of responses to point sources.

### Combined Problem

For $u_t - \frac{1}{2}u_{xx} = h(t,x)$ with $u(0,x) = f(x)$:

$$
u(t, x) = \int G(t, x; 0, y)\,f(y)\,dy + \int_0^t\!\int G(t, x; s, y)\,h(s, y)\,dy\,ds
$$

---

## Properties of the Parabolic Green's Function

### 1. Positivity

$$
G(t, x; s, y) > 0 \quad \text{for all } t > s
$$

Heat always flows from source to surroundings -- the Green's function is everywhere positive. This is the PDE manifestation of the fact that transition densities are non-negative.

### 2. Normalization

$$
\int_{-\infty}^{\infty} G(t, x; s, y)\,dx = 1 \quad \text{for all } t > s
$$

The total amount of "heat" (or probability) is conserved. The Green's function is a probability density in $x$.

### 3. Semigroup Property (Chapman-Kolmogorov)

For $s < r < t$:

$$
\boxed{
G(t, x; s, y) = \int_{-\infty}^{\infty} G(t, x; r, z)\,G(r, z; s, y)\,dz
}
$$

**Interpretation**: The transition from $y$ at time $s$ to $x$ at time $t$ can be decomposed into a transition from $y$ to some intermediate point $z$ at time $r$, followed by a transition from $z$ to $x$. Summing over all possible intermediate states gives the direct transition.

**Probabilistic meaning**: This is the **Chapman-Kolmogorov equation** for the transition density of a Markov process.

### 4. Symmetry (for Self-Adjoint Operators)

When $\mathcal{L}$ is self-adjoint ($\mathcal{L} = \mathcal{L}^*$, which holds for the heat equation but not in general), the Green's function satisfies:

$$
G(t, x; s, y) = G(t, y; s, x)
$$

For non-self-adjoint operators (e.g., with drift), this symmetry fails, but a modified symmetry relates $G$ to the Green's function of the adjoint operator.

### 5. Smoothing

For $t > s$, the map $f \mapsto \int G(t, x; s, y)\,f(y)\,dy$ sends bounded measurable functions to $C^\infty$ functions. This is the **instantaneous regularization** property of parabolic equations.

---

## Construction for Variable Coefficients

### Parametrix Method

For the general operator $\mathcal{L} = \mu(x)\partial_x + \frac{1}{2}\sigma^2(x)\partial_{xx}$, the Green's function is constructed by the **parametrix method**:

1. **Freeze coefficients** at the source point $y$: define $\mathcal{L}_y = \mu(y)\partial_x + \frac{1}{2}\sigma^2(y)\partial_{xx}$, which has the explicit Gaussian Green's function:

$$
G_0(t, x; s, y) = \frac{1}{\sigma(y)\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x - y - \mu(y)(t-s))^2}{2\sigma^2(y)(t-s)}\right)
$$

2. **Correct iteratively**: Write $G = G_0 + G_1 + G_2 + \cdots$ where each correction $G_n$ accounts for the error from the frozen-coefficient approximation.

3. **Convergence**: Under Holder continuity of the coefficients, the series converges and yields a smooth Green's function.

!!! note "Levi's Method"
    This iterative construction is called **Levi's parametrix method**. It is the standard technique for proving existence and deriving short-time asymptotics of the Green's function for variable-coefficient parabolic operators.

### Short-Time Asymptotics

For small $t - s$, the Green's function is approximately Gaussian:

$$
G(t, x; s, y) \approx \frac{1}{\sigma(y)\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x - y - \mu(y)(t-s))^2}{2\sigma^2(y)(t-s)}\right)
$$

The corrections are of order $O((t-s)^{1/2})$ relative to the leading term.

---

## Green's Function and the Adjoint Equation

The Green's function satisfies two PDEs:

| Equation | Variables | PDE |
|---|---|---|
| **Forward** (in $t, x$) | Source $(s, y)$ fixed | $\partial_t G = \mathcal{L}_x G$ |
| **Backward** (in $s, y$) | Observation $(t, x)$ fixed | $-\partial_s G = \mathcal{L}_y^* G$ |

where $\mathcal{L}^*$ is the formal adjoint:

$$
\mathcal{L}^* p = -\frac{\partial}{\partial y}[\mu(y)p] + \frac{1}{2}\frac{\partial^2}{\partial y^2}[\sigma^2(y)p]
$$

!!! info "Financial Interpretation"
    - **Forward equation**: Fix where the process starts; the Green's function (transition density) evolves via Fokker-Planck as you vary the destination
    - **Backward equation**: Fix where you observe; the Green's function solves Kolmogorov backward as you vary the origin

---

## Example: Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$ (constant coefficients), the Green's function is:

$$
G(t, x; s, y) = \frac{1}{\sigma\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x - y - \mu(t-s))^2}{2\sigma^2(t-s)}\right)
$$

This is the density of $X_t \mid X_s = y$, i.e., a normal distribution with:

- Mean: $y + \mu(t-s)$
- Variance: $\sigma^2(t-s)$

**Verification of the semigroup property**: The convolution of two Gaussians is Gaussian with added means and variances -- consistent with the independent increments of Brownian motion with drift.

---

## Example: Ornstein-Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, the Green's function is:

$$
G(t, x; s, y) = \frac{1}{\sqrt{2\pi\,v(t-s)}} \exp\left(-\frac{(x - ye^{-\kappa(t-s)})^2}{2\,v(t-s)}\right)
$$

where the conditional variance is:

$$
v(\tau) = \frac{\sigma^2}{2\kappa}\left(1 - e^{-2\kappa\tau}\right)
$$

**Key features:**

- The conditional mean $ye^{-\kappa\tau}$ reverts toward zero at rate $\kappa$
- The conditional variance $v(\tau) \to \frac{\sigma^2}{2\kappa}$ as $\tau \to \infty$ -- the stationary variance
- The Green's function converges to the stationary density $N(0, \sigma^2/2\kappa)$ regardless of the starting point

---

## Summary

$$
\boxed{
u(t, x) = \int G(t, x; s, y)\,f(y)\,dy \quad \text{(superposition principle)}
}
$$

| Property | Statement |
|---|---|
| **Definition** | $\partial_t G = \mathcal{L}_x G$ with $G(s^+, x; s, y) = \delta(x-y)$ |
| **Positivity** | $G > 0$ for $t > s$ |
| **Normalization** | $\int G\,dx = 1$ |
| **Semigroup** | $G(t,x;s,y) = \int G(t,x;r,z)\,G(r,z;s,y)\,dz$ |
| **Smoothing** | Maps $L^\infty$ to $C^\infty$ |

**The Green's function is the fundamental building block for parabolic PDEs: it solves the equation for a point source, and arbitrary solutions are obtained by superposition. In probability, it is the transition density; in finance, it is the state-price density.**

---

## See Also

- [Fundamental Solution](../heat_equation/fundamental_solution.md) -- the heat kernel as the simplest Green's function
- [Transition Density as Green's Function](transition_density_as_greens_function.md) -- the probabilistic interpretation
- [Spectral Decomposition](spectral_decomposition.md) -- eigenfunction expansion of the Green's function
- [Free vs Bounded Domains](free_vs_bounded_domains.md) -- how boundaries modify the Green's function
- [Kolmogorov Forward Equation](../kolmogorov_equations/kolmogorov_forward.md) -- the PDE that the Green's function satisfies

---

## Exercises

**Exercise 1.**
For the heat equation $\partial_t u = \frac{1}{2}\partial_{xx}u$ on $\mathbb{R}$, verify that the Green's function $G(t,x;0,y) = (2\pi t)^{-1/2}\exp(-(x-y)^2/(2t))$ satisfies the delta function initial condition: show that $\lim_{t \to 0^+} \int_{-\infty}^{\infty} G(t,x;0,y)f(y)\,dy = f(x)$ for continuous $f$.

---

**Exercise 2.**
The superposition principle states $u(t,x) = \int G(t,x;0,y)\,f(y)\,dy$. For $f(y) = e^{-y^2}$ and the free-space heat kernel, evaluate this integral explicitly using the convolution of Gaussians.

---

**Exercise 3.**
Explain why the Green's function $G(t,x;s,y)$ for a parabolic PDE satisfies the **semigroup property** $G(t,x;s,y) = \int G(t,x;r,z)\,G(r,z;s,y)\,dz$ for $s < r < t$. What is the probabilistic interpretation via the Chapman-Kolmogorov equation?

---

**Exercise 4.**
For the operator $\mathcal{L} = \mu(x)\partial_x + \frac{1}{2}\sigma^2(x)\partial_{xx}$, the Green's function satisfies $\partial_t G = \mathcal{L}_x G$ as a function of $(t,x)$ and $\partial_s G = -\mathcal{L}_y^* G$ as a function of $(s,y)$. Identify the adjoint operator $\mathcal{L}^*$ and explain why it involves the forward (Fokker-Planck) equation.

---

**Exercise 5.**
For geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t$, the log-transformation $X_t = \ln S_t$ gives $dX_t = (r - \sigma^2/2)\,dt + \sigma\,dW_t$. Write the Green's function for $X_t$ and explain how it is related to the lognormal transition density of $S_t$.

---

**Exercise 6.**
Explain the role of Green's functions in option pricing: the price of a European derivative with payoff $g(S_T)$ can be written as $V(t,S) = e^{-r(T-t)}\int G(T,y;t,\ln S)\,g(e^y)\,dy$. What is the financial interpretation of the Green's function as a "state price density"?

---

**Exercise 7.**
Consider the generator $\mathcal{L} = \frac{1}{2}\partial_{xx} - \frac{1}{2}\partial_x$ (Brownian motion with drift $-1/2$). Compute the Green's function by completing the square in the exponent, starting from the Gaussian kernel and incorporating the drift shift.

---

## Solutions

??? success "Solution to Exercise 1"
    We must show that $\lim_{t \to 0^+} \int_{-\infty}^{\infty} G(t,x;0,y)\,f(y)\,dy = f(x)$ for continuous $f$. Write

    $$
    \int_{-\infty}^{\infty} G(t,x;0,y)\,f(y)\,dy = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi t}} \exp\!\left(-\frac{(x-y)^2}{2t}\right) f(y)\,dy
    $$

    Substitute $z = (y - x)/\sqrt{t}$, so $y = x + z\sqrt{t}$ and $dy = \sqrt{t}\,dz$:

    $$
    \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-z^2/2}\,f(x + z\sqrt{t})\,dz
    $$

    As $t \to 0^+$, the argument $x + z\sqrt{t} \to x$ for every fixed $z$. Since $f$ is continuous, $f(x + z\sqrt{t}) \to f(x)$. By the dominated convergence theorem (assuming $f$ is bounded or has at most polynomial growth, which is sufficient since the Gaussian provides exponential decay), we can pass the limit inside the integral:

    $$
    \lim_{t \to 0^+} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-z^2/2}\,f(x + z\sqrt{t})\,dz = f(x)\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-z^2/2}\,dz = f(x) \cdot 1 = f(x)
    $$

    This confirms the delta-function initial condition: $G(t, x; 0, y)$ acts as an approximate identity that selects the value $f(x)$ in the limit $t \to 0^+$.

??? success "Solution to Exercise 2"
    We need to evaluate

    $$
    u(t, x) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi t}} \exp\!\left(-\frac{(x-y)^2}{2t}\right) e^{-y^2}\,dy
    $$

    Combine the exponents:

    $$
    -\frac{(x-y)^2}{2t} - y^2 = -\frac{(x-y)^2 + 2ty^2}{2t} = -\frac{x^2 - 2xy + y^2 + 2ty^2}{2t} = -\frac{(1+2t)y^2 - 2xy + x^2}{2t}
    $$

    Complete the square in $y$:

    $$
    (1+2t)y^2 - 2xy = (1+2t)\!\left(y - \frac{x}{1+2t}\right)^2 - \frac{x^2}{1+2t}
    $$

    Therefore

    $$
    -\frac{(1+2t)y^2 - 2xy + x^2}{2t} = -\frac{(1+2t)}{2t}\!\left(y - \frac{x}{1+2t}\right)^2 - \frac{x^2}{2t} + \frac{x^2}{2t(1+2t)}
    $$

    Simplifying the $x^2$ terms: $-\frac{x^2}{2t} + \frac{x^2}{2t(1+2t)} = -\frac{x^2}{1+2t}$.

    The Gaussian integral in $y$ evaluates to $\sqrt{2\pi t/(1+2t)}$, giving

    $$
    u(t, x) = \frac{1}{\sqrt{2\pi t}} \cdot \sqrt{\frac{2\pi t}{1+2t}} \cdot \exp\!\left(-\frac{x^2}{1+2t}\right) = \frac{1}{\sqrt{1+2t}} \exp\!\left(-\frac{x^2}{1+2t}\right)
    $$

    This is a Gaussian that broadens over time: the initial width $1$ increases to $\sqrt{1+2t}$, which is the convolution of two Gaussians with variances $1$ (from $f$) and $t$ (from the heat kernel) giving total variance $(1+2t)/2$.

??? success "Solution to Exercise 3"
    The semigroup property states that for $s < r < t$:

    $$
    G(t, x; s, y) = \int_{-\infty}^{\infty} G(t, x; r, z)\,G(r, z; s, y)\,dz
    $$

    **PDE argument**: Consider the initial value problem $\partial_t u = \mathcal{L}_x u$ with $u(s, x) = \delta(x - y)$. The solution at time $t$ is $u(t, x) = G(t, x; s, y)$. We can equivalently solve in two stages: first evolve from $s$ to $r$ to get $u(r, z) = G(r, z; s, y)$, then use this as initial data and evolve from $r$ to $t$:

    $$
    u(t, x) = \int G(t, x; r, z)\,u(r, z)\,dz = \int G(t, x; r, z)\,G(r, z; s, y)\,dz
    $$

    By uniqueness of the PDE solution, this must equal $G(t, x; s, y)$.

    **Probabilistic interpretation**: This is the Chapman-Kolmogorov equation. For a Markov process $X_t$:

    $$
    p(t, x \mid s, y) = \int p(t, x \mid r, z)\,p(r, z \mid s, y)\,dz
    $$

    This says: the probability of going from $y$ at time $s$ to $x$ at time $t$ equals the sum over all intermediate states $z$ at time $r$ of the probability of going $y \to z$ then $z \to x$. This follows from the Markov property (the future depends on the past only through the present) and the law of total probability.

??? success "Solution to Exercise 4"
    Given $\mathcal{L} = \mu(x)\partial_x + \frac{1}{2}\sigma^2(x)\partial_{xx}$, the Green's function satisfies the **forward equation** $\partial_t G = \mathcal{L}_x G$ in the observation variables $(t, x)$.

    The formal adjoint $\mathcal{L}^*$ is obtained by integration by parts. For any smooth functions $u, v$ vanishing at infinity:

    $$
    \int (\mathcal{L}u)\,v\,dx = \int u\,(\mathcal{L}^* v)\,dx
    $$

    Computing term by term:

    - $\int \mu(x)\,u_x\,v\,dx = -\int u\,\frac{\partial}{\partial x}[\mu(x)\,v]\,dx$ (integration by parts once)
    - $\int \frac{1}{2}\sigma^2(x)\,u_{xx}\,v\,dx = \int u\,\frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x)\,v]\,dx$ (integration by parts twice)

    Therefore

    $$
    \mathcal{L}^* v = -\frac{\partial}{\partial x}[\mu(x)\,v] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x)\,v]
    $$

    The backward equation is $-\partial_s G = \mathcal{L}_y^* G$, which involves $\mathcal{L}^*$ acting on the source variables.

    The adjoint equation $\partial_t p = \mathcal{L}^* p$ is exactly the **Fokker-Planck (forward) equation**: it describes how the probability density $p$ evolves over time. The terms $-\partial_x[\mu\,p]$ represent the advective flux (drift carries probability) and $\frac{1}{2}\partial_{xx}[\sigma^2 p]$ represents the diffusive flux (noise spreads probability). The adjoint structure ensures that probability is conserved: $\frac{d}{dt}\int p\,dx = 0$.

??? success "Solution to Exercise 5"
    Under the log-transformation $X_t = \ln S_t$, Ito's formula gives

    $$
    dX_t = \left(r - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
    $$

    This is Brownian motion with drift $\mu = r - \sigma^2/2$ and diffusion coefficient $\sigma$. The transition density of $X_t$ given $X_s = \ln S$ is Gaussian:

    $$
    p_X(t, x \mid s, \ln S) = \frac{1}{\sigma\sqrt{2\pi(t-s)}} \exp\!\left(-\frac{(x - \ln S - (r - \sigma^2/2)(t-s))^2}{2\sigma^2(t-s)}\right)
    $$

    This is the Green's function $G(t, x; s, \ln S)$ for the PDE $\partial_t u = (r - \sigma^2/2)\partial_x u + \frac{1}{2}\sigma^2\partial_{xx}u$.

    To obtain the transition density of $S_t$ in the original variable, use the change of variables $S_T = e^x$, so $dS_T = e^x\,dx$ and $p_S(t, S_T \mid s, S) = p_X(t, \ln S_T \mid s, \ln S)/S_T$:

    $$
    p_S(t, S_T \mid s, S) = \frac{1}{S_T \sigma\sqrt{2\pi(t-s)}} \exp\!\left(-\frac{(\ln(S_T/S) - (r - \sigma^2/2)(t-s))^2}{2\sigma^2(t-s)}\right)
    $$

    This is the lognormal transition density. The log-space Green's function and the lognormal density are related by the Jacobian factor $1/S_T$ from the exponential change of variables.

??? success "Solution to Exercise 6"
    The European derivative price under risk-neutral pricing is

    $$
    V(t, S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S] = e^{-r(T-t)}\int_0^{\infty} g(S_T)\,p^{\mathbb{Q}}(T, S_T \mid t, S)\,dS_T
    $$

    In log-space ($y = \ln S_T$):

    $$
    V(t, S) = e^{-r(T-t)}\int_{-\infty}^{\infty} g(e^y)\,G(T, y; t, \ln S)\,dy
    $$

    The Green's function $G(T, y; t, \ln S)$ plays the role of a **state-price density** (Arrow-Debreu price). For each terminal state $y$, the quantity $e^{-r(T-t)}G(T, y; t, \ln S)\,dy$ is the price today of a security that pays $\$1$ if the log-price at maturity falls in the interval $[y, y + dy]$ and zero otherwise.

    The Green's function encodes all information needed for pricing because:

    - It captures the dynamics of the underlying process (drift, volatility) through the PDE it satisfies.
    - It incorporates the risk-neutral measure through the drift adjustment ($r$ replaces $\mu$).
    - Any European payoff $g$ can be priced by integrating against $G$ -- different payoffs simply change the weighting function, not the kernel.
    - The discount factor $e^{-r(T-t)}$ accounts for the time value of money.

    Thus, knowing the Green's function is equivalent to knowing all European option prices simultaneously.

??? success "Solution to Exercise 7"
    The generator is $\mathcal{L} = \frac{1}{2}\partial_{xx} - \frac{1}{2}\partial_x$, corresponding to the SDE $dX_t = -\frac{1}{2}\,dt + dW_t$ (Brownian motion with drift $\mu = -1/2$).

    The Green's function for drift-diffusion $dX_t = \mu\,dt + \sigma\,dW_t$ with $\mu = -1/2$ and $\sigma = 1$ is

    $$
    G(t, x; s, y) = \frac{1}{\sqrt{2\pi(t-s)}} \exp\!\left(-\frac{(x - y + \frac{1}{2}(t-s))^2}{2(t-s)}\right)
    $$

    **Derivation by completing the square**: Start with the Gaussian kernel and incorporate the drift. The PDE is $\partial_t u = \frac{1}{2}\partial_{xx}u - \frac{1}{2}\partial_x u$. Make the substitution $u(t, x) = e^{\alpha x + \beta t}\,v(t, x)$ to eliminate the first-order term. Substituting:

    $$
    e^{\alpha x + \beta t}(\beta v + v_t) = \frac{1}{2}e^{\alpha x + \beta t}(\alpha^2 v + 2\alpha v_x + v_{xx}) - \frac{1}{2}e^{\alpha x + \beta t}(\alpha v + v_x)
    $$

    Choosing $\alpha = 1/2$ eliminates the $v_x$ terms (since $2\alpha \cdot \frac{1}{2} - \frac{1}{2} = 0$), and then $\beta = -\alpha^2/2 + \alpha/2 = -1/8 + 1/4 = 1/8$. This gives $v_t = \frac{1}{2}v_{xx}$, the standard heat equation.

    The Green's function of the heat equation is $\Gamma(t, x-y) = (2\pi t)^{-1/2}e^{-(x-y)^2/(2t)}$. Reverting:

    $$
    G(t, x; 0, y) = e^{-\frac{1}{2}(x-y) - \frac{1}{8}t} \cdot \frac{1}{\sqrt{2\pi t}}\,e^{-(x-y)^2/(2t)}
    $$

    Combining the exponentials:

    $$
    -\frac{(x-y)^2}{2t} - \frac{x-y}{2} - \frac{t}{8} = -\frac{(x-y)^2 + t(x-y) + t^2/4}{2t} = -\frac{(x - y + t/2)^2}{2t}
    $$

    Therefore

    $$
    G(t, x; 0, y) = \frac{1}{\sqrt{2\pi t}} \exp\!\left(-\frac{(x - y + t/2)^2}{2t}\right)
    $$

    This is a Gaussian centered at $y - t/2$ (the source point shifted by the drift $-1/2$ over time $t$), confirming that the drift simply translates the center of the heat kernel.
