# Why PDEs in Finance

Partial differential equations arise naturally in quantitative finance whenever we ask: **what is the fair price of a derivative today, given uncertainty about the future?** The answer turns out to satisfy a deterministic PDE, even though the underlying asset follows a random process. This remarkable fact is the foundation of modern derivatives pricing.

---

## The Core Insight

Consider a derivative with payoff $g(S_T)$ at maturity $T$. Under the risk-neutral measure, its price at time $t$ is:

$$
V(t, S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S]
$$

This expectation is a **function of the current state** $(t, S)$. The Feynman-Kac theorem guarantees that this function satisfies a parabolic PDE:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
$$

with terminal condition $V(T, S) = g(S)$.

!!! quote "The Central Principle"
    **Expected values of diffusion processes satisfy partial differential equations.** Every pricing problem for a Markovian underlying reduces to solving a PDE.

---

## From Stochastic Process to PDE

### The Generator Connection

For a general diffusion:

$$
dX_t = \mu(t, X_t)\,dt + \sigma(t, X_t)\,dW_t
$$

the **infinitesimal generator** is the differential operator:

$$
\mathcal{L} = \mu(t,x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(t,x)\frac{\partial^2}{\partial x^2}
$$

The generator encodes the local dynamics of the process. Any expected value $u(t,x) = \mathbb{E}[g(X_T) \mid X_t = x]$ satisfies:

$$
\frac{\partial u}{\partial t} + \mathcal{L}u = 0, \quad u(T, x) = g(x)
$$

With discounting at rate $r(t,x)$, the PDE becomes:

$$
\frac{\partial u}{\partial t} + \mathcal{L}u - r\,u = 0
$$

This is the **Feynman-Kac equation**, and it is the master equation of financial PDE theory.

### Why Does a Random Process Lead to a Deterministic Equation?

The key is the **Markov property**. Because the future of $X_t$ depends only on its current state, the conditional expectation $u(t,x)$ is a well-defined function of $(t,x)$ alone. The PDE then describes how this function must evolve to remain consistent with the stochastic dynamics.

Intuitively:

- **Drift** $\mu$ contributes a first-order (transport) term
- **Volatility** $\sigma$ contributes a second-order (diffusion) term
- **Discounting** $r$ contributes a zeroth-order (decay) term

---

## Three Approaches to Derivative Pricing

Given the price $V(t,S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S]$, there are three computational strategies.

### Approach 1: PDE (Finite Differences)

Solve the PDE on a discretized grid in $(t, S)$ space, marching backward from the terminal condition.

**Procedure:**

1. Discretize the domain: grid points $(t_n, S_j)$
2. Apply a finite difference scheme (explicit, implicit, or Crank-Nicolson)
3. March backward from $V(T, S_j) = g(S_j)$ to $V(0, S_0)$

**Example**: For a European call under Black-Scholes, the PDE is:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

A Crank-Nicolson scheme with 200 time steps and 400 spatial nodes typically gives accuracy to several decimal places.

### Approach 2: Monte Carlo Simulation

Simulate paths of $S_t$ and average the discounted payoff.

**Procedure:**

1. Simulate $N$ independent paths of $S_t$ from $t$ to $T$
2. Compute the discounted payoff for each path: $e^{-r(T-t)} g(S_T^{(i)})$
3. Estimate: $\hat{V} = \frac{1}{N}\sum_{i=1}^N e^{-r(T-t)} g(S_T^{(i)})$

The standard error is $O(1/\sqrt{N})$, independent of dimension.

### Approach 3: Tree Methods

Discretize the stochastic process into a recombining lattice and compute expectations by backward induction.

**Procedure:**

1. Build a binomial or trinomial tree for $S_t$
2. Assign terminal payoffs at the final nodes
3. Discount backward through the tree: $V_j^n = e^{-r\Delta t}[\hat{p}\,V_{j+1}^{n+1} + (1-\hat{p})\,V_j^{n+1}]$

Trees are a discrete approximation to the PDE and converge to the continuous solution as the mesh refines.

---

## Comparison of Methods

| Criterion | PDE (Finite Diff.) | Monte Carlo | Trees |
|---|---|---|---|
| **Dimension** | 1--3 variables | Any dimension | 1--2 variables |
| **Convergence** | $O(\Delta x^2 + \Delta t^2)$ | $O(1/\sqrt{N})$ | $O(\Delta t)$ |
| **Greeks** | Direct from grid | Requires bump-and-reprice | Finite differences on tree |
| **Early exercise** | Free boundary methods | Least-squares MC (Longstaff-Schwartz) | Natural via backward induction |
| **Path dependence** | Difficult (add state variables) | Natural | Difficult |
| **All strikes at once** | Yes (full grid) | No (one payoff per run) | Yes (full tree) |

!!! tip "When to Use PDEs"
    PDEs excel when:

    - The problem is low-dimensional (1--3 state variables)
    - You need Greeks (sensitivities) — they come directly from the PDE solution
    - You need prices for many strikes/maturities simultaneously
    - Early exercise or free boundaries are present (American options)
    - High accuracy is required with modest computational cost

!!! tip "When to Use Monte Carlo"
    Monte Carlo excels when:

    - The problem is high-dimensional (basket options, CDOs)
    - The payoff is path-dependent (Asian, lookback, barrier)
    - The model is complex (stochastic volatility + jumps)
    - Moderate accuracy suffices

---

## The Black-Scholes PDE as a Canonical Example

The most important financial PDE is the **Black-Scholes equation**. Under geometric Brownian motion:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

the price $V(t, S)$ of any European derivative with payoff $g(S_T)$ satisfies:

$$
\boxed{
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
}
$$

**Key features:**

1. **Parabolic**: The equation is second-order in $S$ and first-order in $t$, with the classification determined by the positive coefficient $\frac{1}{2}\sigma^2 S^2 > 0$ for $S > 0$
2. **Terminal condition**: $V(T, S) = g(S)$ specifies the payoff at maturity
3. **Boundary conditions**: Depend on the specific derivative (e.g., $V(t, 0) = 0$ for a call)
4. **Universal**: The same PDE holds for calls, puts, digitals, and any European payoff — only the terminal condition changes

### Derivation via Hedging

The PDE can also be derived by a **replicating portfolio argument** (the original Black-Scholes derivation):

1. Form a portfolio $\Pi = V - \Delta S$ where $\Delta = \partial V / \partial S$
2. By Ito's lemma: $d\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt$
3. No-arbitrage requires $d\Pi = r\Pi\,dt$
4. Substituting and rearranging yields the Black-Scholes PDE

This hedging derivation and the Feynman-Kac probabilistic derivation are two sides of the same coin.

---

## Beyond Black-Scholes

The PDE framework extends naturally to richer models:

### Stochastic Volatility (Heston Model)

$$
dS_t = rS_t\,dt + \sqrt{v_t}\,S_t\,dW_t^S
$$

$$
dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^v
$$

The option price satisfies a **two-dimensional PDE** in $(t, S, v)$:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho\xi v S\frac{\partial^2 V}{\partial S\partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} - rV = 0
$$

### Jump-Diffusion (Merton Model)

With jumps of random size $J$, the PDE becomes a **partial integro-differential equation** (PIDE):

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - rV + \lambda\int_{\mathbb{R}}\left[V(t, Se^z) - V(t, S)\right]\nu(dz) = 0
$$

where $\lambda$ is the jump intensity and $\nu$ is the jump size distribution.

### Stochastic Interest Rates

When the short rate $r_t$ follows its own diffusion, bond prices satisfy PDEs of the form:

$$
\frac{\partial P}{\partial t} + \mathcal{L}_r P - r P = 0
$$

where $\mathcal{L}_r$ is the generator of the short-rate process.

---

## The PDE Perspective on Greeks

A major advantage of the PDE approach is that **Greeks are built into the solution**. Since $V(t,S)$ is computed on an entire grid, its derivatives are immediately available:

| Greek | Definition | PDE Interpretation |
|---|---|---|
| Delta ($\Delta$) | $\frac{\partial V}{\partial S}$ | Slope of the solution surface |
| Gamma ($\Gamma$) | $\frac{\partial^2 V}{\partial S^2}$ | Curvature of the solution surface |
| Theta ($\Theta$) | $\frac{\partial V}{\partial t}$ | Time decay, recoverable from the PDE itself |
| Vega | $\frac{\partial V}{\partial \sigma}$ | Sensitivity to volatility (requires re-solving) |

!!! note "Theta from the PDE"
    The Black-Scholes PDE itself gives $\Theta$ directly:

    $$
    \Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    This is a **model-independent relationship** (within Black-Scholes) connecting the Greeks.

---

## Historical Context

The PDE approach to finance has a rich history:

- **1900**: Bachelier models stock prices as Brownian motion and derives option prices via the heat equation — decades before Black-Scholes
- **1973**: Black, Scholes, and Merton derive the Black-Scholes PDE via hedging and connect it to risk-neutral expectations
- **1977**: Brennan and Schwartz solve American option pricing as a free boundary PDE problem
- **1993**: Heston's stochastic volatility model leads to a 2D pricing PDE with a semi-analytical solution
- **2000s**: PIDE methods for jump models; ADI schemes for multi-factor models

---

## Summary

$$
\boxed{
\text{Derivative price} = \text{Conditional expectation} = \text{PDE solution}
}
$$

The PDE approach to finance rests on three pillars:

| Pillar | Statement |
|---|---|
| **Feynman-Kac** | Expected values of diffusions satisfy parabolic PDEs |
| **Risk-neutral pricing** | Derivative prices are discounted expectations under $\mathbb{Q}$ |
| **Generator** | The drift and volatility of the underlying determine the PDE coefficients |

**PDEs provide the analytical backbone of quantitative finance: they yield closed-form solutions when available, efficient numerical schemes when not, and Greeks as a natural byproduct.**

---

## See Also

- [The SDE-PDE Bridge](sde_pde_bridge.md) -- the mathematical connection between diffusions and PDEs
- [Classification of Second-Order PDEs](classification_of_second_order_pdes.md) -- elliptic, parabolic, hyperbolic
- [Boundary Value Problems](boundary_value_problems.md) -- Dirichlet, Neumann, Robin conditions
- [Feynman-Kac Formula](../feynman_kac/feynman_kac_formula.md) -- the rigorous statement and proof
- [Black-Scholes PDE](../../ch06/bs_pde_structure/discounting_and_killing_term.md) -- detailed PDE structure
