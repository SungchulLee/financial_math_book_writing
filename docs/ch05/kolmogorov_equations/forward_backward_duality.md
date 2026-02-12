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

### The Generator $\mathcal{L}$

$$\mathcal{L} f = \mu(x) \frac{\partial f}{\partial x} + \frac{\sigma^2(x)}{2}\frac{\partial^2 f}{\partial x^2}$$

Acts on **test functions** (payoffs, value functions).

### The Adjoint Generator $\mathcal{L}^*$

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

## Comparison: $\mathcal{L}$ vs $\mathcal{L}^*$

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
