# Boundary Value Problems

A partial differential equation alone does not determine a unique solution. We must also specify **boundary conditions** -- constraints on the solution at the edges of the domain -- and **initial or terminal conditions**. The choice of conditions is dictated by the PDE type and the physics (or finance) of the problem. A problem is **well-posed** when these conditions guarantee existence, uniqueness, and continuous dependence on the data.

---

## The Parabolic Initial-Boundary Value Problem

The standard setting for financial PDEs is a **parabolic equation on a bounded domain**:

$$
\frac{\partial u}{\partial t} + \mathcal{L}u = f \quad \text{in } (0, T) \times \Omega
$$

with terminal condition:

$$
u(T, x) = g(x) \quad \text{for } x \in \Omega
$$

and boundary conditions on $\partial\Omega$, where $\Omega \subset \mathbb{R}^d$ is the spatial domain and:

$$
\mathcal{L} = \sum_i \mu_i(x)\frac{\partial}{\partial x_i} + \frac{1}{2}\sum_{i,j} a_{ij}(x)\frac{\partial^2}{\partial x_i \partial x_j} - r(x)
$$

is the pricing operator (generator minus discounting).

The **parabolic boundary** consists of the terminal time and the spatial boundary:

$$
\Gamma = \{T\} \times \Omega \;\cup\; [0, T] \times \partial\Omega
$$

!!! note "Time Direction"
    In finance, the terminal condition is given at $t = T$ and the PDE is solved backward. Mathematically this is equivalent (via $\tau = T - t$) to a forward initial value problem.

---

## Types of Boundary Conditions

### Dirichlet Condition (Prescribed Value)

$$
\boxed{u(t, x) = h(t, x) \quad \text{for } (t, x) \in [0,T] \times \partial\Omega}
$$

The solution is prescribed on the boundary. This is the most common type in finance.

**Financial interpretation**: The option price is **known** at the boundary.

**Examples:**

- **European call** as $S \to 0$: $V(t, 0) = 0$ (worthless if stock is zero)
- **European call** as $S \to \infty$: $V(t, S) \approx S - Ke^{-r(T-t)}$ (deep in-the-money)
- **Knock-out barrier option** at barrier $B$: $V(t, B) = 0$ (option knocked out)
- **Killed diffusion**: Process absorbed at boundary $\implies$ $u = 0$ on $\partial\Omega$

### Neumann Condition (Prescribed Flux)

$$
\boxed{\frac{\partial u}{\partial n}(t, x) = h(t, x) \quad \text{for } (t, x) \in [0,T] \times \partial\Omega}
$$

where $\frac{\partial}{\partial n}$ is the outward normal derivative. The **rate of change** of the solution is prescribed, not the value itself.

**Financial interpretation**: The option's **delta** is specified at the boundary.

**Examples:**

- **Put option** as $S \to \infty$: $\frac{\partial V}{\partial S} \to 0$ (delta approaches zero)
- **Reflecting boundary**: Probability mass is reflected back into the domain
- **Symmetry condition**: $\frac{\partial u}{\partial x} = 0$ at a line of symmetry

### Robin Condition (Mixed)

$$
\boxed{\alpha(x)\,u(t, x) + \beta(x)\frac{\partial u}{\partial n}(t, x) = h(t, x) \quad \text{for } (t, x) \in [0,T] \times \partial\Omega}
$$

A linear combination of the solution value and its normal derivative is specified. This interpolates between Dirichlet ($\beta = 0$) and Neumann ($\alpha = 0$).

**Financial interpretation**: A partial absorption/reflection condition, or a **linear relationship between price and delta** at the boundary.

**Example**: Elastic barriers where partial rebates are paid upon hitting the boundary.

---

## Comparison of Boundary Conditions

| Type | Specifies | Probabilistic Meaning | Financial Example |
|---|---|---|---|
| **Dirichlet** | $u = h$ | Absorption (killing) at boundary | Barrier option knockout |
| **Neumann** | $\partial_n u = h$ | Reflection at boundary | No-flux condition |
| **Robin** | $\alpha u + \beta \partial_n u = h$ | Partial absorption/reflection | Elastic barrier |

---

## Well-Posedness in the Sense of Hadamard

A problem is **well-posed** if it satisfies three conditions:

1. **Existence**: A solution exists
2. **Uniqueness**: The solution is unique (in an appropriate function space)
3. **Continuous dependence**: Small changes in the data lead to small changes in the solution

$$
\boxed{
\|u_1 - u_2\| \leq C\left(\|g_1 - g_2\| + \|h_1 - h_2\| + \|f_1 - f_2\|\right)
}
$$

where $g$ is the terminal data, $h$ is the boundary data, and $f$ is the source term.

!!! warning "Ill-Posedness"
    Not all combinations of PDE type and boundary conditions are well-posed:

    - **Backward heat equation** ($u_t + \frac{1}{2}u_{xx} = 0$ with *initial* data at $t = 0$, solving forward): ill-posed. Arbitrarily small perturbations in data can produce arbitrarily large changes in the solution. This reflects the irreversibility of diffusion.
    - **Laplace equation with Cauchy data** (prescribing both $u$ and $\partial_n u$ on part of the boundary): ill-posed (Hadamard's counterexample).

### Correct Pairings

| PDE Type | Well-Posed Problem | Condition Type |
|---|---|---|
| **Elliptic** | Dirichlet/Neumann/Robin on entire $\partial\Omega$ | Boundary only |
| **Parabolic** | Terminal data + boundary conditions on $\partial\Omega$ | Initial/terminal + boundary |
| **Hyperbolic** | Initial data $u(0,x)$, $u_t(0,x)$ + boundary | Two initial + boundary |

---

## The Maximum Principle and Uniqueness

For parabolic equations, the **maximum principle** provides both uniqueness and continuous dependence.

**Theorem (Parabolic Maximum Principle)**: If $u$ satisfies $\partial_t u + \mathcal{L}u \leq 0$ in $(0,T) \times \Omega$ (with $r \geq 0$ in $\mathcal{L}$), then:

$$
\max_{\overline{Q}_T} u = \max_{\Gamma} u
$$

where $\Gamma$ is the parabolic boundary.

**Corollary (Uniqueness)**: If $u_1$ and $u_2$ both solve the same parabolic IBVP, then $w = u_1 - u_2$ satisfies the homogeneous problem with zero data on $\Gamma$. By the maximum principle, $w \leq 0$ and $-w \leq 0$, so $w = 0$. $\square$

**Corollary (Stability)**: The continuous dependence estimate:

$$
\|u_1 - u_2\|_{L^\infty(Q_T)} \leq \max\left(\|g_1 - g_2\|_\infty,\, \|h_1 - h_2\|_\infty\right)
$$

follows directly from the maximum principle.

---

## Boundary Conditions in the Black-Scholes Framework

For a European derivative with payoff $g(S)$ under Black-Scholes dynamics, the PDE domain is typically $(t, S) \in [0, T] \times [0, \infty)$.

### Terminal Condition

$$
V(T, S) = g(S)
$$

This is universal -- it encodes the derivative's payoff structure.

### Boundary at $S = 0$

At $S = 0$, the Black-Scholes operator degenerates: $\frac{1}{2}\sigma^2 S^2 \partial_{SS} \to 0$. The PDE reduces to:

$$
\frac{\partial V}{\partial t} = rV \quad \Longrightarrow \quad V(t, 0) = e^{-r(T-t)} g(0)
$$

For a call ($g(0) = 0$): $V(t, 0) = 0$. For a put ($g(0) = K$): $V(t, 0) = Ke^{-r(T-t)}$.

!!! info "Why No Boundary Condition Is Needed at $S = 0$"
    The degeneracy of the PDE at $S = 0$ means $S = 0$ is an **absorbing boundary** for geometric Brownian motion: once $S_t = 0$, it remains there forever. Probabilistically, $\mathbb{P}(S_t = 0 \text{ for some } t) = 0$, so the boundary is never reached. The PDE determines its own boundary behavior there.

### Boundary as $S \to \infty$

An artificial truncation at $S = S_\text{max}$ requires a far-field boundary condition. Common choices:

| Derivative | Far-Field Condition | Justification |
|---|---|---|
| European call | $V \approx S - Ke^{-r(T-t)}$ | Deep ITM asymptotics |
| European put | $V \approx 0$ | Worthless for large $S$ |
| General | $\frac{\partial^2 V}{\partial S^2} \approx 0$ | Gamma vanishes far from strike |

---

## Barrier Options and Domain Truncation

**Barrier options** provide the cleanest financial example of Dirichlet boundary conditions.

### Down-and-Out Call

Domain: $(t, S) \in [0, T] \times (B, \infty)$ where $B < K$ is the barrier.

$$
\begin{cases}
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0 & \text{for } S > B \\
V(T, S) = (S - K)^+ & \text{terminal condition} \\
V(t, B) = 0 & \text{Dirichlet at barrier}
\end{cases}
$$

The Dirichlet condition $V(t, B) = 0$ encodes the knockout feature: the option becomes worthless upon hitting the barrier.

### Up-and-Out Put

Domain: $(t, S) \in [0, T] \times (0, B)$ where $B > K$ is the upper barrier.

$$
V(t, B) = 0 \quad \text{(knockout at upper barrier)}
$$

### Rebate Barrier Option

If a rebate $R$ is paid upon knockout:

$$
V(t, B) = R \quad \text{(nonzero Dirichlet)}
$$

---

## Free Boundary Problems and American Options

**American options** introduce a fundamentally new type of boundary condition: the **free boundary** (also called the **optimal exercise boundary**).

The holder can exercise at any time $t \leq T$, so the price satisfies the **linear complementarity problem**:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V \leq 0, \quad V \geq g(S), \quad \left(\frac{\partial V}{\partial t} + \mathcal{L}V\right)(V - g) = 0
$$

This decomposes the domain into:

- **Continuation region**: $V > g$ and $\frac{\partial V}{\partial t} + \mathcal{L}V = 0$ (standard PDE)
- **Exercise region**: $V = g$ (option exercised immediately)
- **Free boundary** $S^*(t)$: The curve separating the two regions

At the free boundary, two conditions hold simultaneously:

$$
V(t, S^*(t)) = g(S^*(t)) \quad \text{(value matching)}
$$

$$
\frac{\partial V}{\partial S}(t, S^*(t)) = g'(S^*(t)) \quad \text{(smooth pasting)}
$$

!!! tip "Smooth Pasting"
    The smooth-pasting condition states that not only the price but also the delta is continuous across the free boundary. This is a necessary condition for the optimal exercise policy and emerges naturally from the variational inequality formulation.

---

## Existence and Regularity Theory

For the parabolic IBVP with Dirichlet conditions:

$$
\begin{cases}
\partial_t u + \mathcal{L}u = f & \text{in } Q_T = (0,T) \times \Omega \\
u(T, \cdot) = g & \text{on } \Omega \\
u = h & \text{on } [0,T] \times \partial\Omega
\end{cases}
$$

**Theorem (Classical Existence)**: If $\Omega$ has smooth boundary, coefficients are smooth, $a_{ij}$ is uniformly elliptic, and data $(f, g, h)$ are compatible and smooth, then there exists a unique classical solution $u \in C^{2,1}(\overline{Q}_T)$.

**Theorem (Weak/Viscosity Solutions)**: Under weaker conditions (bounded measurable coefficients, continuous data), the problem admits a unique viscosity solution. This is the appropriate framework for degenerate equations and non-smooth payoffs encountered in finance.

---

## Summary

| Aspect | Description |
|---|---|
| **Dirichlet** | Prescribes $u$ on boundary; absorbing/knockout |
| **Neumann** | Prescribes $\partial_n u$; reflecting/no-flux |
| **Robin** | Linear combination; partial absorption |
| **Well-posedness** | Existence + uniqueness + stability |
| **Maximum principle** | Ensures uniqueness and stability for parabolic PDEs |
| **Free boundary** | American options; exercise boundary determined as part of solution |

$$
\boxed{
\text{PDE} + \text{terminal condition} + \text{boundary conditions} \;\Longrightarrow\; \text{unique, stable solution}
}
$$

**The choice of boundary conditions reflects the financial structure of the derivative: knockout barriers impose Dirichlet conditions, no-arbitrage constraints determine far-field behavior, and early exercise creates free boundaries.**

---

## See Also

- [Why PDEs in Finance](why_pdes_in_finance.md) -- motivation for the PDE approach
- [Classification of Second-Order PDEs](classification_of_second_order_pdes.md) -- which boundary conditions are appropriate for which PDE type
- [Maximum Principle](../heat_equation/maximum_principle.md) -- the tool for uniqueness and stability
- [Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md) -- boundary conditions for diffusion expectations
