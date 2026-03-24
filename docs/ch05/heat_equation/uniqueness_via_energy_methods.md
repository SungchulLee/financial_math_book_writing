# Uniqueness via Energy Methods

The **maximum principle** provides one route to uniqueness for the heat equation. Energy methods offer a complementary approach that is often more flexible: define an integral quantity (the "energy") that measures how far a solution is from zero, and show this energy can only **decrease** over time. If the energy starts at zero, it must remain zero -- proving the solution is identically zero and hence unique.

!!! tip "Related Content"
    - [Maximum Principle](maximum_principle.md) -- the other main uniqueness tool
    - [Fundamental Solution](fundamental_solution.md) -- the heat kernel
    - [Heat Equation and Brownian Motion](heat_equation_and_brownian_motion.md) -- probabilistic interpretation

---

## The Energy Functional

### Definition

For a function $u(t, x)$ on the domain $Q_T = (0, T] \times (a, b)$, define the **energy**:

$$
\boxed{
E(t) = \frac{1}{2}\int_a^b u(t, x)^2\,dx
}
$$

This is a non-negative quantity that measures the "total magnitude" of $u$ at time $t$. It equals zero if and only if $u(t, \cdot) = 0$ almost everywhere.

### Physical Intuition

The energy $E(t)$ has a natural interpretation:

- In **heat conduction**: $E(t)$ is proportional to the total thermal energy stored in the rod
- In **probability**: If $u$ is a density perturbation, $E(t)$ measures the $L^2$ distance from zero
- In **finance**: For the difference of two portfolio values, $E(t)$ measures the total squared discrepancy

The heat equation **dissipates** energy: diffusion spreads out concentrations, reducing peaks and filling valleys. This smoothing drives $E(t)$ down.

---

## Energy Dissipation for the Heat Equation

### Theorem (Energy Decay)

Let $u$ solve the heat equation on $(0, T] \times (a, b)$:

$$
\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}
$$

with **homogeneous Dirichlet boundary conditions** $u(t, a) = u(t, b) = 0$. Then:

$$
\boxed{
\frac{dE}{dt} = -\frac{1}{2}\int_a^b \left(\frac{\partial u}{\partial x}\right)^2 dx \leq 0
}
$$

The energy is **non-increasing**. It is strictly decreasing unless $u_x \equiv 0$, which (combined with the boundary conditions) forces $u \equiv 0$.

### Proof

Differentiate under the integral sign (justified by the smoothness of solutions to the heat equation):

$$
\frac{dE}{dt} = \int_a^b u\,\frac{\partial u}{\partial t}\,dx
$$

Substitute the heat equation $u_t = \frac{1}{2}u_{xx}$:

$$
\frac{dE}{dt} = \int_a^b u \cdot \frac{1}{2}u_{xx}\,dx
$$

**Integrate by parts**: Using $\int u\,u_{xx}\,dx = [u\,u_x]_a^b - \int u_x^2\,dx$:

$$
\frac{dE}{dt} = \frac{1}{2}\left[u\,u_x\right]_a^b - \frac{1}{2}\int_a^b u_x^2\,dx
$$

The boundary term vanishes because $u(t, a) = u(t, b) = 0$:

$$
\frac{dE}{dt} = -\frac{1}{2}\int_a^b u_x^2\,dx \leq 0
$$

$\square$

!!! note "The Key Step: Integration by Parts"
    The integration by parts transfers one derivative from $u_{xx}$ to $u$, producing the squared gradient $u_x^2$. This is the essential trick in energy methods: convert a product involving second derivatives into a non-negative squared quantity.

---

## Uniqueness Proof

### Theorem (Uniqueness via Energy)

The initial-boundary value problem:

$$
\begin{cases}
u_t = \frac{1}{2}u_{xx} & \text{in } (0, T] \times (a, b) \\
u(0, x) = f(x) & \text{initial condition} \\
u(t, a) = g_a(t),\; u(t, b) = g_b(t) & \text{boundary conditions}
\end{cases}
$$

has **at most one** solution in $C^{2,1}(\overline{Q}_T)$.

### Proof

Suppose $u_1$ and $u_2$ are two solutions with the same data. Let $w = u_1 - u_2$. Then $w$ satisfies:

$$
\begin{cases}
w_t = \frac{1}{2}w_{xx} & \text{(linearity)} \\
w(0, x) = 0 & \text{(same initial data)} \\
w(t, a) = w(t, b) = 0 & \text{(same boundary data)}
\end{cases}
$$

Define the energy of the difference:

$$
E(t) = \frac{1}{2}\int_a^b w(t, x)^2\,dx
$$

**Step 1**: At $t = 0$, since $w(0, x) = 0$:

$$
E(0) = 0
$$

**Step 2**: By the energy decay result:

$$
\frac{dE}{dt} \leq 0 \quad \text{for all } t \in (0, T]
$$

**Step 3**: Since $E(t) \geq 0$ always, and $E(0) = 0$, and $E$ is non-increasing:

$$
E(t) = 0 \quad \text{for all } t \in [0, T]
$$

**Step 4**: $E(t) = 0$ implies $\int_a^b w^2\,dx = 0$, hence $w(t, x) = 0$ for all $x \in [a, b]$.

Therefore $u_1 = u_2$. $\square$

---

## Sharper Energy Estimates

### Poincare Inequality

On the interval $(a, b)$ with homogeneous Dirichlet conditions, the **Poincare inequality** states:

$$
\int_a^b u^2\,dx \leq \frac{(b-a)^2}{\pi^2}\int_a^b u_x^2\,dx
$$

Combining with the energy dissipation:

$$
\frac{dE}{dt} = -\frac{1}{2}\int_a^b u_x^2\,dx \leq -\frac{\pi^2}{(b-a)^2} E(t)
$$

This is a **Gronwall-type inequality**, yielding exponential decay:

$$
\boxed{
E(t) \leq E(0)\,e^{-\pi^2 t / (b-a)^2}
}
$$

**Interpretation**: The energy decays exponentially with rate $\pi^2 / (b-a)^2$. Shorter intervals (smaller $b - a$) lead to faster decay -- the diffusion reaches the boundaries sooner.

### Connection to Spectral Theory

The decay rate $\pi^2 / (b-a)^2$ is the **first eigenvalue** of $-\frac{1}{2}\partial_{xx}$ on $(a, b)$ with Dirichlet conditions. The slowest-decaying mode is the fundamental eigenfunction $\sin\!\left(\frac{\pi(x-a)}{b-a}\right)$, which decays at exactly this rate. All higher modes decay faster.

---

## Extension to Variable Coefficients

### General Parabolic Operator

Consider the variable-coefficient equation:

$$
\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial}{\partial x}\left(\sigma^2(x)\frac{\partial u}{\partial x}\right)
$$

where $\sigma^2(x) \geq \sigma_{\min}^2 > 0$ (uniform ellipticity).

The energy dissipation becomes:

$$
\frac{dE}{dt} = -\frac{1}{2}\int_a^b \sigma^2(x)\,u_x^2\,dx \leq -\frac{\sigma_{\min}^2}{2}\int_a^b u_x^2\,dx
$$

Uniqueness follows by the same argument.

### With Lower-Order Terms

For the equation $u_t = \frac{1}{2}u_{xx} + \mu(x)u_x - r(x)u$ with $r \geq 0$, define the **weighted energy**:

$$
\tilde{E}(t) = \frac{1}{2}\int_a^b e^{-2\lambda t} u^2\,dx
$$

Choosing $\lambda$ large enough to absorb the drift term, one obtains $\frac{d\tilde{E}}{dt} \leq 0$, yielding uniqueness.

!!! example "Financial Application"
    For the Black-Scholes PDE with drift $rS\partial_S$ and discounting $-rV$, the energy method applies after a change of variables $x = \log S$, which transforms the equation into one with bounded coefficients on $\mathbb{R}$.

---

## Neumann Boundary Conditions

For Neumann conditions $u_x(t, a) = u_x(t, b) = 0$, the boundary term in the integration by parts is:

$$
\frac{1}{2}[u\,u_x]_a^b = \frac{1}{2}\left(u(b)u_x(b) - u(a)u_x(a)\right) = 0
$$

The energy dissipation $\frac{dE}{dt} = -\frac{1}{2}\int u_x^2\,dx \leq 0$ still holds. However, the Poincare inequality must be modified: for Neumann conditions, the constant function is in the kernel, so uniqueness holds only **up to a constant**.

---

## Energy Methods vs Maximum Principle

| Aspect | Energy Methods | Maximum Principle |
|---|---|---|
| **What it bounds** | $L^2$ norm ($\int u^2\,dx$) | $L^\infty$ norm ($\max |u|$) |
| **Proof technique** | Integration by parts | Calculus of maxima |
| **Extends to** | Higher dimensions, systems | Scalar equations primarily |
| **Quantitative** | Gives decay rate | Gives pointwise bounds |
| **Regularity needed** | Weaker ($H^1$) | Stronger ($C^2$) |
| **Variable coefficients** | Natural extension | Needs uniform ellipticity |

!!! tip "Complementary Tools"
    Neither method strictly dominates the other. The maximum principle gives sharper pointwise bounds but is harder to extend to systems. Energy methods are more flexible and extend naturally to weak (Sobolev) solutions, making them the primary tool in modern PDE theory.

---

## The Probabilistic Connection

Energy dissipation has a probabilistic interpretation. If $u(t, x)$ represents the density of a perturbation to Brownian motion, then:

$$
E(t) = \frac{1}{2}\int u^2\,dx
$$

decreases because Brownian motion **mixes**: it spreads out any initial concentration. The rate of mixing is governed by the spectral gap (the first eigenvalue), which determines how quickly the process "forgets" its initial condition.

In the language of probability: the transition semigroup is **contractive in $L^2$**.

---

## Summary

$$
\boxed{
E(t) = \frac{1}{2}\int u^2\,dx \quad \Longrightarrow \quad \frac{dE}{dt} = -\frac{1}{2}\int u_x^2\,dx \leq 0
}
$$

| Result | Statement |
|---|---|
| Energy decay | $E(t) \leq E(0)$ for all $t > 0$ |
| Uniqueness | $E(0) = 0 \implies E(t) = 0$ for all $t$ |
| Exponential decay | $E(t) \leq E(0)\,e^{-\pi^2 t/(b-a)^2}$ with Poincare |
| Variable coefficients | Holds with $\sigma_{\min}^2 > 0$ |

**Energy methods prove uniqueness by showing that diffusion dissipates the total squared magnitude of any solution. The energy can only go down, so a solution starting at zero must remain at zero.**

---

## See Also

- [Maximum Principle](maximum_principle.md) -- complementary uniqueness tool
- [Fundamental Solution](fundamental_solution.md) -- explicit solution showing decay
- [Spectral Decomposition](../greens_functions/spectral_decomposition.md) -- eigenfunction expansion and decay rates
- [Scaling and Invariance](scaling_and_invariance.md) -- self-similar structure of the heat equation

---

## Exercises

**Exercise 1.**
Define the energy functional $E(t) = \frac{1}{2}\int_a^b u(x, t)^2\,dx$ for a solution $u$ of the heat equation with homogeneous Dirichlet conditions on $[a, b]$. Compute $E'(t)$ and show that $E'(t) \leq 0$, proving that energy is non-increasing.

---

**Exercise 2.**
Using the energy method, prove uniqueness: if $u$ and $v$ both solve the heat equation with the same initial and boundary data, define $w = u - v$ and show $E_w(t) = 0$ for all $t \geq 0$, hence $w = 0$.

---

**Exercise 3.**
The Poincare inequality states $\int_a^b u^2\,dx \leq C\int_a^b (u')^2\,dx$ for functions vanishing at the endpoints, with $C = (b-a)^2/\pi^2$. Use this together with the energy decay $E'(t) = -\int (u')^2\,dx$ to show $E'(t) \leq -\frac{\pi^2}{(b-a)^2}E(t)$, giving exponential decay $E(t) \leq E(0)e^{-\pi^2 t/(b-a)^2}$.

---

**Exercise 4.**
For Neumann conditions $u_x(a, t) = u_x(b, t) = 0$, the energy $E(t) = \frac{1}{2}\int u^2\,dx$ still decreases, but does it decay to zero? Explain why the Poincare inequality must be modified (applied to $u - \bar{u}$ where $\bar{u}$ is the spatial average) and what the equilibrium solution is.

---

**Exercise 5.**
Explain the financial interpretation of energy decay for barrier option pricing on a bounded domain $[B_l, B_u]$. As $T - t \to \infty$, the option price decays exponentially. Relate the decay rate to the smallest eigenvalue $\lambda_1 = \pi^2 / (2(B_u - B_l)^2)$.

---

**Exercise 6.**
The energy method requires only integration by parts and does not need the explicit form of the solution. Explain why this is an advantage over the maximum principle approach for proving uniqueness, especially for more complex PDEs with variable coefficients.

---

**Exercise 7.**
For the heat equation with a source term $\partial_t u = \frac{1}{2}\partial_{xx}u + f(x, t)$, the energy is no longer monotonically decreasing. Compute $E'(t)$ in this case and identify the additional term. Under what condition on $f$ does the energy still remain bounded?
