# Forward–Backward Duality

The Kolmogorov forward and backward equations are **adjoint** to each other. This duality is not merely a mathematical curiosity—it reflects two fundamentally different ways of looking at the same diffusion process and has deep implications for computation, interpretation, and applications.

!!! tip "Related Content"
    - [Kolmogorov Forward Equation](kolmogorov_forward.md) — density evolution
    - [Kolmogorov Backward Equation](kolmogorov_backward.md) — expected values
    - [Infinitesimal Generator](../../ch03/infinitesimal_generator/infinitesimal_generator.md) — the operator $\mathcal{L}$

---

## The Two Perspectives

Consider a diffusion process $X_t$ with generator $\mathcal{L}$. We can ask two fundamentally different questions:

### The Backward Question

> "Given that I start at position $x$, what is the expected value of some quantity $g(X_T)$?"

$$u(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$$

This is the **value function** perspective. We fix a payoff $g$ and ask how its expected value depends on where we start.

### The Forward Question

> "Given that I started at position $x_0$, what is the probability density of where I am now?"

$$p(x, t \mid x_0, t_0)$$

This is the **distribution** perspective. We fix a starting point and track where probability mass goes.

---

## The Generator and Its Adjoint

For the SDE $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$:

### The Generator L

$$\mathcal{L} f = \mu(x) \frac{\partial f}{\partial x} + \frac{\sigma^2(x)}{2}\frac{\partial^2 f}{\partial x^2}$$

Acts on **test functions** (payoffs, value functions).

### The Adjoint Generator L^*

$$\mathcal{L}^* f = -\frac{\partial}{\partial x}[\mu(x) f] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x) f]$$

Acts on **probability densities**.

---

## Derivation of the Adjoint

The adjoint is defined by the **duality relation**:

$$\int_{-\infty}^{\infty} f(x) (\mathcal{L}g)(x) \, dx = \int_{-\infty}^{\infty} (\mathcal{L}^* f)(x) g(x) \, dx$$

for suitable test functions $f, g$ with vanishing boundary terms.

??? abstract "Derivation via Integration by Parts"
    
    We compute $\int f \cdot \mathcal{L}g \, dx$ and transfer derivatives from $g$ to $f$.
    
    **Drift term:**
    
    $$\int_{-\infty}^{\infty} f(x) \cdot \mu(x) g'(x) \, dx$$
    
    Integration by parts ($u = f\mu$, $dv = g' dx$):
    
    $$= \underbrace{[f \mu g]_{-\infty}^{\infty}}_{= 0} - \int_{-\infty}^{\infty} \frac{\partial}{\partial x}[f \mu] \cdot g \, dx = -\int_{-\infty}^{\infty} \frac{\partial}{\partial x}[\mu f] \cdot g \, dx$$
    
    **Diffusion term:**
    
    $$\int_{-\infty}^{\infty} f(x) \cdot \frac{\sigma^2(x)}{2} g''(x) \, dx$$
    
    First integration by parts:
    
    $$= \underbrace{\left[\frac{\sigma^2 f}{2} g'\right]_{-\infty}^{\infty}}_{= 0} - \int_{-\infty}^{\infty} \frac{\partial}{\partial x}\left[\frac{\sigma^2 f}{2}\right] g' \, dx$$
    
    Second integration by parts:
    
    $$= -\underbrace{\left[\frac{\partial}{\partial x}\left(\frac{\sigma^2 f}{2}\right) g\right]_{-\infty}^{\infty}}_{= 0} + \int_{-\infty}^{\infty} \frac{\partial^2}{\partial x^2}\left[\frac{\sigma^2 f}{2}\right] g \, dx$$
    
    **Combining:**
    
    $$\int f \cdot \mathcal{L}g \, dx = \int \left( -\frac{\partial}{\partial x}[\mu f] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2 f] \right) g \, dx$$
    
    Therefore:
    
    $$\mathcal{L}^* f = -\frac{\partial}{\partial x}[\mu(x) f] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x) f]$$

---

## Comparison: L vs L^*

| Aspect | Generator $\mathcal{L}$ | Adjoint $\mathcal{L}^*$ |
|--------|------------------------|------------------------|
| **Formula** | $\mu f' + \frac{\sigma^2}{2}f''$ | $-(\mu f)' + \frac{1}{2}(\sigma^2 f)''$ |
| **Acts on** | Test functions, payoffs | Probability densities |
| **Drift term** | $\mu f'$ | $-(\mu f)' = -\mu f' - \mu' f$ |
| **Diffusion term** | $\frac{\sigma^2}{2}f''$ | $\frac{1}{2}(\sigma^2 f)''$ |
| **Derivatives** | On the function $f$ | On the product (coefficient × function) |
| **PDE** | Backward: $\partial_t u = \mathcal{L}u$ | Forward: $\partial_t p = \mathcal{L}^*p$ |

### Key Structural Difference

- **$\mathcal{L}$**: Derivatives act on $f$ alone; coefficients $\mu$, $\sigma^2$ multiply the result
- **$\mathcal{L}^*$**: Derivatives act on the product $\mu f$ or $\sigma^2 f$; coefficients get differentiated too

This difference arises from integration by parts: transferring derivatives from one function to another reverses the direction and brings in derivatives of the coefficients.

---

## The Duality in Action

### Connecting Expected Values and Densities

For any payoff $g$ and density $p$:

$$\mathbb{E}[g(X_T)] = \int_{-\infty}^{\infty} g(x) p(x, T) \, dx$$

**Two ways to compute the same thing:**

1. **Backward approach**: Solve $\partial_t u = \mathcal{L}u$ with $u(0, x) = g(x)$, evaluate $u(T, x_0)$
2. **Forward approach**: Solve $\partial_t p = \mathcal{L}^*p$ with $p(x, 0) = \delta(x - x_0)$, integrate $\int g(x) p(x, T) dx$

The duality ensures both give the same answer.

### The Transition Density Satisfies Both

The transition density $p(x, t \mid x_0, t_0)$ satisfies:

- **Backward equation** in $(x_0, t_0)$: $\frac{\partial p}{\partial t_0} + \mathcal{L}_{x_0} p = 0$
- **Forward equation** in $(x, t)$: $\frac{\partial p}{\partial t} = \mathcal{L}_x^* p$

This is remarkable: the same function satisfies two different PDEs in different variables!

**Interpretation:**

- Fix **destination** $(x, t)$, vary **origin** $(x_0, t_0)$: "From where could we have come?"
- Fix **origin** $(x_0, t_0)$, vary **destination** $(x, t)$: "Where might we end up?"

---

## Physical and Financial Interpretations

### Physical: Particles vs Observers

**Forward (Lagrangian)**: Follow a cloud of particles. The density $p(x,t)$ tells you the particle concentration at each point.

**Backward (Eulerian)**: Stand at a point and ask: "What's the expected value of some measurement, given a particle started at various locations?"

### Financial: Pricing vs Hedging

**Backward**: Given a terminal payoff (option at expiry), find its present value. This is **pricing**.

**Forward**: Given initial capital, track how wealth evolves. This is **portfolio evolution**.

### Information: Filtering vs Prediction

**Backward**: "What can I infer about the past given current observations?"

**Forward**: "What will the distribution be at future times?"

---

## When to Use Which?

| Scenario | Use | Reason |
|----------|-----|--------|
| **Option pricing** | Backward | Know terminal payoff, want present value |
| **Density evolution** | Forward | Track probability mass over time |
| **Monte Carlo** | Either | Backward often more natural for expectations |
| **PDE numerics** | Depends | Forward for density, backward for values |
| **Stationary distribution** | Forward | Solve $\mathcal{L}^* p_\infty = 0$ |
| **First passage problems** | Backward | Expected hitting times via $\mathcal{L}u = -1$ |
| **Diffusion models (ML)** | Both | Forward to noise, backward to denoise |

---

## Constant Coefficients: Self-Adjointness

For **Brownian motion** ($\mu = 0$, $\sigma = 1$):

$$\mathcal{L} = \frac{1}{2}\frac{\partial^2}{\partial x^2}, \quad \mathcal{L}^* = \frac{1}{2}\frac{\partial^2}{\partial x^2}$$

The operator is **self-adjoint**: $\mathcal{L} = \mathcal{L}^*$.

More generally, for constant $\mu$ and $\sigma$:

$$\mathcal{L} = \mu \partial_x + \frac{\sigma^2}{2}\partial_{xx}$$

$$\mathcal{L}^* = -\mu \partial_x + \frac{\sigma^2}{2}\partial_{xx}$$

The drift term changes sign, but diffusion is self-adjoint.

---

## Detailed Balance and Reversibility

A diffusion is **reversible** (or satisfies **detailed balance**) with respect to a density $\pi(x)$ if:

$$\pi(x) p(y, t \mid x, 0) = \pi(y) p(x, t \mid y, 0)$$

**Physical meaning**: The probability flux from $x$ to $y$ equals the flux from $y$ to $x$, when weighted by the equilibrium distribution.

### Condition for Detailed Balance

For a one-dimensional diffusion with stationary distribution $\pi$, detailed balance holds if and only if the probability current vanishes:

$$J = \mu(x)\pi(x) - \frac{1}{2}\frac{\partial}{\partial x}[\sigma^2(x)\pi(x)] = 0$$

This is satisfied by the Ornstein–Uhlenbeck process but not by general diffusions with non-conservative drift.

---

## The Adjoint in Multiple Dimensions

For $X_t \in \mathbb{R}^d$ with $dX_t^i = \mu^i(X_t)\,dt + \sigma^{i\alpha}(X_t)\,dW_t^\alpha$:

**Generator:**

$$\mathcal{L}f = \sum_i \mu^i \frac{\partial f}{\partial x_i} + \frac{1}{2}\sum_{i,j} a^{ij} \frac{\partial^2 f}{\partial x_i \partial x_j}$$

where $a^{ij} = \sum_\alpha \sigma^{i\alpha}\sigma^{j\alpha}$.

**Adjoint:**

$$\mathcal{L}^*f = -\sum_i \frac{\partial}{\partial x_i}[\mu^i f] + \frac{1}{2}\sum_{i,j} \frac{\partial^2}{\partial x_i \partial x_j}[a^{ij} f]$$

The structure is analogous: derivatives move onto the products (coefficient × function).

---

## Spectral Theory Perspective

For nice operators on $L^2$, duality connects to **spectral theory**:

- $\mathcal{L}$ and $\mathcal{L}^*$ have the same **eigenvalues**
- Eigenfunctions are related by the duality pairing
- The stationary distribution $\pi$ (eigenfunction of $\mathcal{L}^*$ with eigenvalue 0) pairs with the constant function $\mathbf{1}$ (eigenfunction of $\mathcal{L}$ with eigenvalue 0)

### Spectral Decomposition

For the OU process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$:

- Eigenvalues: $\lambda_n = n\kappa$ for $n = 0, 1, 2, \ldots$
- Eigenfunctions of $\mathcal{L}$: Hermite polynomials $H_n(x)$
- Eigenfunctions of $\mathcal{L}^*$: $\phi_n(x) = H_n(x) \cdot \pi(x)$ where $\pi$ is the Gaussian stationary density

The transition density has the expansion:

$$p(x, t \mid x_0, 0) = \pi(x) \sum_{n=0}^{\infty} e^{-\lambda_n t} H_n(x) H_n(x_0)$$

---

## Computational Implications

### PDE Methods

**Backward equation** (terminal value problem):

- March backward in time from $t = T$ to $t = 0$
- Natural for option pricing: know payoff at expiry
- Explicit schemes: stable with $\Delta t \leq C \Delta x^2$

**Forward equation** (initial value problem):

- March forward in time from $t = 0$ to $t = T$
- Natural for density evolution
- Same stability constraints

### Monte Carlo

**Backward** (compute $\mathbb{E}[g(X_T)]$):

1. Simulate paths forward
2. Evaluate $g$ at terminal points
3. Average

**Forward** (approximate density):

1. Simulate many paths
2. Build histogram at time $T$
3. Approximate $p(x, T)$

Both require forward simulation of the SDE, but answer different questions.

---

## Connection to Time Reversal

The forward–backward duality is intimately connected to **time reversal** of diffusions.

If $X_t$ has generator $\mathcal{L}$ and stationary distribution $\pi$, then the time-reversed process $\tilde{X}_t = X_{T-t}$ has drift:

$$\tilde{\mu}(x) = -\mu(x) + \sigma^2(x) \frac{\partial \log \pi}{\partial x}(x)$$

The reversed generator $\tilde{\mathcal{L}}$ is related to $\mathcal{L}^*$ via $\pi$:

$$\tilde{\mathcal{L}}f = \frac{1}{\pi}\mathcal{L}^*(\pi f)$$

This is the foundation of:

- **Score-based diffusion models** in ML
- **Stochastic bridges** (conditioned diffusions)
- **Entropy production** in non-equilibrium thermodynamics

---

## Summary

$$
\boxed{
\begin{aligned}
\mathcal{L} &= \mu \partial_x + \frac{\sigma^2}{2}\partial_{xx} \quad &\text{(generator)} \\[6pt]
\mathcal{L}^* &= -\partial_x[\mu \cdot] + \frac{1}{2}\partial_{xx}[\sigma^2 \cdot] \quad &\text{(adjoint)}
\end{aligned}
}
$$

| Equation | Operator | Acts On | Question |
|----------|----------|---------|----------|
| Backward | $\mathcal{L}$ | Values/payoffs | Expected outcome? |
| Forward | $\mathcal{L}^*$ | Densities | Where is probability? |

**The duality principle**: Integrating $(\mathcal{L}f)$ against a density equals integrating $f$ against $(\mathcal{L}^*\text{density})$.

This symmetry between test functions and densities underlies much of diffusion theory, from basic Kolmogorov equations to modern applications in machine learning.

---

## See Also

- [Kolmogorov Forward Equation](kolmogorov_forward.md) — the forward equation in detail
- [Kolmogorov Backward Equation](kolmogorov_backward.md) — the backward equation in detail
- [Infinitesimal Generator](../../ch03/infinitesimal_generator/infinitesimal_generator.md) — definition and properties
- [Invariant Measures](../../ch03/diffusion_process/invariant_measures_and_stationarity.md) — fixed points of $\mathcal{L}^*$
- [Time Reversal of Diffusions](../../ch03/diffusion_process/time_reversal_of_diffusions.md) — reversed dynamics
- [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md) — discounted expectations

---

## Exercises

**Exercise 1.**
For the generator $\mathcal{L} = \mu(x)\partial_x + \frac{\sigma^2(x)}{2}\partial_{xx}$, derive the adjoint $\mathcal{L}^*$ by integrating $\int f(x)(\mathcal{L}g)(x)\,dx$ by parts twice. Identify the boundary terms that must vanish for the duality relation to hold.

---

**Exercise 2.**
For standard Brownian motion ($\mu = 0$, $\sigma = 1$), verify that $\mathcal{L} = \mathcal{L}^* = \frac{1}{2}\partial_{xx}$. Explain why the operator is self-adjoint in this case. For Brownian motion with constant drift $\mu \neq 0$, show that $\mathcal{L} \neq \mathcal{L}^*$ and describe how the drift term changes sign under the adjoint.

---

**Exercise 3.**
Consider the Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$. Write out the generator $\mathcal{L}$ and its adjoint $\mathcal{L}^*$ explicitly. Verify that the stationary density $\pi(x) \propto \exp(-\kappa x^2/\sigma^2)$ satisfies $\mathcal{L}^* \pi = 0$.

---

**Exercise 4.**
The transition density $p(x, t \mid x_0, t_0)$ satisfies both the forward equation in $(x, t)$ and the backward equation in $(x_0, t_0)$. For Brownian motion with drift, verify this explicitly using the Gaussian transition density

$$
p(x, t \mid x_0, t_0) = \frac{1}{\sigma\sqrt{2\pi(t - t_0)}} \exp\left(-\frac{(x - x_0 - \mu(t - t_0))^2}{2\sigma^2(t - t_0)}\right)
$$

by checking that it satisfies both $\partial_t p = \mathcal{L}_x^* p$ and $\partial_{t_0} p + \mathcal{L}_{x_0} p = 0$.

---

**Exercise 5.**
Suppose you want to compute $\mathbb{E}[g(X_T)]$ for a specific payoff $g$ and a specific starting point $x_0$. Describe the backward approach (solve one PDE with terminal condition $g$, evaluate at $x_0$) and the forward approach (solve one PDE with initial condition $\delta(x - x_0)$, integrate against $g$). Under what circumstances is each approach more computationally efficient?

---

**Exercise 6.**
The detailed balance condition states $\pi(x)p(y, t \mid x, 0) = \pi(y)p(x, t \mid y, 0)$. For the Ornstein-Uhlenbeck process, verify that detailed balance holds by using the explicit Gaussian transition density and the Gaussian stationary distribution. Explain the physical meaning: the probability flux from $x$ to $y$ equals the flux from $y$ to $x$ when weighted by $\pi$.

---

**Exercise 7.**
For the OU process, the eigenvalues of $\mathcal{L}$ are $\lambda_n = n\kappa$ and the eigenfunctions are Hermite polynomials $H_n(x)$. Using the spectral expansion $p(x, t \mid x_0, 0) = \pi(x)\sum_{n=0}^{\infty} e^{-\lambda_n t} H_n(x)H_n(x_0)$, explain why the transition density converges to the stationary density $\pi(x)$ as $t \to \infty$. What is the rate of convergence, and which eigenvalue determines it?

---

## Solutions

??? success "Solution to Exercise 1"
    We compute $\int f(x)(\mathcal{L}g)(x)\,dx$ where $\mathcal{L}g = \mu(x)g'(x) + \frac{\sigma^2(x)}{2}g''(x)$.

    **Drift term** — integrate by parts once with $u = f(x)\mu(x)$ and $dv = g'(x)\,dx$:

    $$
    \int_{-\infty}^{\infty} f(x)\mu(x)g'(x)\,dx = \underbrace{[f\mu g]_{-\infty}^{\infty}}_{\text{boundary term } B_1} - \int_{-\infty}^{\infty}\frac{\partial}{\partial x}[f\mu]\,g(x)\,dx
    $$

    **Diffusion term** — integrate by parts twice. First integration by parts:

    $$
    \int_{-\infty}^{\infty} f\frac{\sigma^2}{2}g''\,dx = \underbrace{\left[\frac{\sigma^2 f}{2}g'\right]_{-\infty}^{\infty}}_{\text{boundary term } B_2} - \int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left[\frac{\sigma^2 f}{2}\right]g'\,dx
    $$

    Second integration by parts:

    $$
    -\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left[\frac{\sigma^2 f}{2}\right]g'\,dx = -\underbrace{\left[\frac{\partial}{\partial x}\left(\frac{\sigma^2 f}{2}\right)g\right]_{-\infty}^{\infty}}_{\text{boundary term } B_3} + \int_{-\infty}^{\infty}\frac{\partial^2}{\partial x^2}\left[\frac{\sigma^2 f}{2}\right]g\,dx
    $$

    **Combining**, the duality relation holds when $B_1 = B_2 = B_3 = 0$:

    $$
    \int f(\mathcal{L}g)\,dx = \int\left(-\frac{\partial}{\partial x}[\mu f] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2 f]\right)g\,dx = \int(\mathcal{L}^*f)\,g\,dx
    $$

    The boundary terms that must vanish are:

    - $B_1 = [f(x)\mu(x)g(x)]_{-\infty}^{\infty}$
    - $B_2 = \left[\frac{\sigma^2(x)f(x)}{2}g'(x)\right]_{-\infty}^{\infty}$
    - $B_3 = \left[\frac{\partial}{\partial x}\left(\frac{\sigma^2(x)f(x)}{2}\right)g(x)\right]_{-\infty}^{\infty}$

    These vanish when $f$ and $g$ (along with their derivatives) decay sufficiently fast at $\pm\infty$, or when working with compactly supported test functions.

??? success "Solution to Exercise 2"
    For standard Brownian motion ($\mu = 0$, $\sigma = 1$):

    $$
    \mathcal{L}f = \frac{1}{2}f'', \qquad \mathcal{L}^*f = \frac{1}{2}f''
    $$

    These are identical, so $\mathcal{L} = \mathcal{L}^*$. The operator is self-adjoint because neither the drift term nor the diffusion term depends on $x$. When we integrate by parts, the derivatives of constant coefficients vanish, so transferring derivatives from $g$ to $f$ produces exactly the same expression.

    For Brownian motion with constant drift $\mu \neq 0$ and $\sigma = 1$:

    $$
    \mathcal{L}f = \mu f' + \frac{1}{2}f''
    $$

    Computing the adjoint: the drift term gives $-(\mu f)' = -\mu f'$ (since $\mu$ is constant), and the diffusion term gives $\frac{1}{2}f''$. Therefore:

    $$
    \mathcal{L}^*f = -\mu f' + \frac{1}{2}f''
    $$

    Since $\mathcal{L}f = \mu f' + \frac{1}{2}f''$ and $\mathcal{L}^*f = -\mu f' + \frac{1}{2}f''$, we see $\mathcal{L} \neq \mathcal{L}^*$. The **drift term changes sign** under the adjoint (from $+\mu f'$ to $-\mu f'$), while the diffusion term is unchanged. Physically, taking the adjoint reverses the direction of advection: if probability flows to the right in the forward equation, the backward equation "looks" from the right.

??? success "Solution to Exercise 3"
    For the OU process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, we have $\mu(x) = -\kappa x$ and $\sigma(x) = \sigma$ (constant).

    **Generator:**

    $$
    \mathcal{L}f = -\kappa x f' + \frac{\sigma^2}{2}f''
    $$

    **Adjoint:** For the drift term, $-\frac{\partial}{\partial x}[\mu f] = -\frac{\partial}{\partial x}[-\kappa x f] = \kappa f + \kappa x f' = \kappa\frac{\partial(xf)}{\partial x}$. For the diffusion term (constant $\sigma$), $\frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2 f] = \frac{\sigma^2}{2}f''$. Therefore:

    $$
    \mathcal{L}^*f = \kappa\frac{\partial(xf)}{\partial x} + \frac{\sigma^2}{2}f'' = \kappa f + \kappa x f' + \frac{\sigma^2}{2}f''
    $$

    **Verification that $\pi(x) \propto \exp(-\kappa x^2/\sigma^2)$ satisfies $\mathcal{L}^*\pi = 0$:**

    Compute the derivatives:

    $$
    \pi'(x) = -\frac{2\kappa x}{\sigma^2}\pi(x), \qquad \pi''(x) = \left(\frac{4\kappa^2 x^2}{\sigma^4} - \frac{2\kappa}{\sigma^2}\right)\pi(x)
    $$

    Substituting:

    $$
    \mathcal{L}^*\pi = \kappa\pi + \kappa x\left(-\frac{2\kappa x}{\sigma^2}\right)\pi + \frac{\sigma^2}{2}\left(\frac{4\kappa^2 x^2}{\sigma^4} - \frac{2\kappa}{\sigma^2}\right)\pi
    $$

    $$
    = \pi\left[\kappa - \frac{2\kappa^2 x^2}{\sigma^2} + \frac{2\kappa^2 x^2}{\sigma^2} - \kappa\right] = 0
    $$

??? success "Solution to Exercise 4"
    The transition density for Brownian motion with drift is:

    $$
    p(x, t \mid x_0, t_0) = \frac{1}{\sigma\sqrt{2\pi\tau}}\exp\left(-\frac{(x - x_0 - \mu\tau)^2}{2\sigma^2\tau}\right)
    $$

    where $\tau = t - t_0$. Define $z = x - x_0 - \mu\tau$ for convenience.

    **Forward equation check** ($\partial_t p = \mathcal{L}_x^* p = -\mu\partial_x p + \frac{\sigma^2}{2}\partial_{xx}p$):

    $$
    \frac{\partial p}{\partial t} = p\left(-\frac{1}{2\tau} + \frac{z^2}{2\sigma^2\tau^2} + \frac{\mu z}{\sigma^2\tau}\right)
    $$

    $$
    \frac{\partial p}{\partial x} = -\frac{z}{\sigma^2\tau}p, \qquad \frac{\partial^2 p}{\partial x^2} = \left(\frac{z^2}{\sigma^4\tau^2} - \frac{1}{\sigma^2\tau}\right)p
    $$

    $$
    -\mu\frac{\partial p}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2} = \frac{\mu z}{\sigma^2\tau}p + \frac{\sigma^2}{2}\left(\frac{z^2}{\sigma^4\tau^2} - \frac{1}{\sigma^2\tau}\right)p = p\left(\frac{\mu z}{\sigma^2\tau} + \frac{z^2}{2\sigma^2\tau^2} - \frac{1}{2\tau}\right) = \frac{\partial p}{\partial t} \;\checkmark
    $$

    **Backward equation check** ($\partial_{t_0} p + \mathcal{L}_{x_0} p = 0$, i.e., $\partial_{t_0}p + \mu\partial_{x_0}p + \frac{\sigma^2}{2}\partial_{x_0 x_0}p = 0$):

    Since $\tau = t - t_0$, we have $\partial_{t_0}\tau = -1$. Note $z = x - x_0 - \mu\tau$, so $\partial_{t_0}z = \mu$ and $\partial_{x_0}z = -1$.

    $$
    \frac{\partial p}{\partial t_0} = p\left(\frac{1}{2\tau} - \frac{z^2}{2\sigma^2\tau^2} - \frac{\mu z}{\sigma^2\tau}\right)
    $$

    $$
    \frac{\partial p}{\partial x_0} = \frac{z}{\sigma^2\tau}p, \qquad \frac{\partial^2 p}{\partial x_0^2} = \left(\frac{z^2}{\sigma^4\tau^2} - \frac{1}{\sigma^2\tau}\right)p
    $$

    $$
    \frac{\partial p}{\partial t_0} + \mu\frac{\partial p}{\partial x_0} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x_0^2}
    $$

    $$
    = p\left[\frac{1}{2\tau} - \frac{z^2}{2\sigma^2\tau^2} - \frac{\mu z}{\sigma^2\tau} + \frac{\mu z}{\sigma^2\tau} + \frac{z^2}{2\sigma^2\tau^2} - \frac{1}{2\tau}\right] = 0 \;\checkmark
    $$

??? success "Solution to Exercise 5"
    **Backward approach**: Solve the PDE $\partial_t v + \mathcal{L}v = 0$ with terminal condition $v(T, x) = g(x)$. This gives $v(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$, and evaluating at $(t, x) = (0, x_0)$ gives $v(0, x_0) = \mathbb{E}[g(X_T) \mid X_0 = x_0]$.

    - **Advantages**: Solves one PDE to get the answer for all starting points $x_0$ simultaneously. For a fixed payoff $g$, one PDE solve suffices.
    - **More efficient when**: We have a single payoff $g$ but need the expected value at many different starting points (e.g., option pricing at different spot prices).

    **Forward approach**: Solve the PDE $\partial_t p = \mathcal{L}^* p$ with initial condition $p(x, 0) = \delta(x - x_0)$. This gives the transition density $p(x, T)$, and then:

    $$
    \mathbb{E}[g(X_T)] = \int g(x)p(x, T)\,dx
    $$

    - **Advantages**: Once $p(x, T)$ is known, we can compute expected values for any payoff $g$ by integration.
    - **More efficient when**: We have a fixed starting point $x_0$ but need to evaluate many different payoffs $g$ (e.g., pricing an entire book of options on the same underlying, all starting from the same spot price).

    In summary: backward is efficient for "one payoff, many starting points," while forward is efficient for "one starting point, many payoffs."

??? success "Solution to Exercise 6"
    The OU process has transition density:

    $$
    p(y, t \mid x, 0) = \frac{1}{\sqrt{2\pi v(t)}}\exp\left(-\frac{(y - xe^{-\kappa t})^2}{2v(t)}\right)
    $$

    where $v(t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$, and stationary distribution:

    $$
    \pi(x) = \sqrt{\frac{\kappa}{\pi\sigma^2}}\exp\left(-\frac{\kappa x^2}{\sigma^2}\right)
    $$

    We must verify $\pi(x)p(y, t \mid x, 0) = \pi(y)p(x, t \mid y, 0)$.

    Compute $\pi(x)p(y, t \mid x, 0)$:

    $$
    \propto \exp\left(-\frac{\kappa x^2}{\sigma^2} - \frac{(y - xe^{-\kappa t})^2}{2v(t)}\right)
    $$

    Expanding the exponent:

    $$
    -\frac{\kappa x^2}{\sigma^2} - \frac{y^2 - 2xye^{-\kappa t} + x^2 e^{-2\kappa t}}{2v(t)}
    $$

    Using $v(t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$ and $\frac{1}{2v(t)} = \frac{\kappa}{\sigma^2(1 - e^{-2\kappa t})}$:

    $$
    = -\frac{\kappa x^2}{\sigma^2} - \frac{\kappa}{\sigma^2(1 - e^{-2\kappa t})}(y^2 - 2xye^{-\kappa t} + x^2 e^{-2\kappa t})
    $$

    $$
    = -\frac{\kappa}{\sigma^2}\left[x^2 + \frac{y^2 - 2xye^{-\kappa t} + x^2 e^{-2\kappa t}}{1 - e^{-2\kappa t}}\right]
    $$

    $$
    = -\frac{\kappa}{\sigma^2}\cdot\frac{x^2(1 - e^{-2\kappa t}) + y^2 - 2xye^{-\kappa t} + x^2 e^{-2\kappa t}}{1 - e^{-2\kappa t}}
    $$

    $$
    = -\frac{\kappa}{\sigma^2}\cdot\frac{x^2 + y^2 - 2xye^{-\kappa t}}{1 - e^{-2\kappa t}}
    $$

    This expression is **symmetric in $x$ and $y$**, so swapping $x \leftrightarrow y$ gives the same result. Therefore $\pi(x)p(y,t \mid x, 0) = \pi(y)p(x, t \mid y, 0)$, confirming detailed balance.

    **Physical meaning**: In the stationary regime, if a particle is at position $x$ (drawn from $\pi$), the probability of transitioning to $y$ in time $t$ equals the probability that a particle starting at $y$ transitions to $x$ in the same time. There is no net probability current between any pair of states — the system is in thermodynamic equilibrium.

??? success "Solution to Exercise 7"
    The spectral expansion is:

    $$
    p(x, t \mid x_0, 0) = \pi(x)\sum_{n=0}^{\infty}e^{-n\kappa t}H_n(x)H_n(x_0)
    $$

    where $\lambda_n = n\kappa$ and $H_0(x) = 1$.

    As $t \to \infty$, the exponential factors $e^{-n\kappa t}$ decay to zero for all $n \geq 1$ (since $\kappa > 0$). Only the $n = 0$ term survives:

    $$
    \lim_{t\to\infty}p(x, t \mid x_0, 0) = \pi(x)\cdot e^{0}\cdot H_0(x)H_0(x_0) = \pi(x)
    $$

    since $H_0 = 1$. This shows the transition density converges to the stationary density $\pi(x)$ regardless of the starting point $x_0$.

    **Rate of convergence**: The dominant correction comes from the $n = 1$ term:

    $$
    p(x, t \mid x_0, 0) = \pi(x)\left[1 + e^{-\kappa t}H_1(x)H_1(x_0) + O(e^{-2\kappa t})\right]
    $$

    The rate of convergence is determined by the **spectral gap**, which is the smallest nonzero eigenvalue $\lambda_1 = \kappa$. The transition density converges to the stationary distribution exponentially fast with rate $\kappa$:

    $$
    \|p(\cdot, t \mid x_0, 0) - \pi(\cdot)\| = O(e^{-\kappa t})
    $$

    Larger $\kappa$ (stronger mean reversion) leads to faster convergence to equilibrium.
