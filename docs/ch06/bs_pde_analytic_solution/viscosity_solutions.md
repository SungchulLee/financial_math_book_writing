# Viscosity Solutions

This section does not introduce another solution method. Instead, it provides the **rigorous mathematical foundation** that justifies every PDE-based derivation in this chapter.

The heat equation, Fourier, Mellin, Laplace, and separation-of-variables approaches all assumed---implicitly or explicitly---that the solution is smooth enough to differentiate classically ($C^{2,1}$ in $S$ and $t$). The Feynman-Kac representation assumed the solution satisfies the PDE in the pointwise sense. For the standard European call with payoff $(S - K)^+$, these regularity assumptions hold and every derivation is valid.

But many practically important cases fail this smoothness requirement. Discontinuous terminal data (digital options), American-style early exercise (free boundary problems), and degenerate diffusion coefficients all produce solutions that are **not** $C^2$. The question is: what does it *mean* to "solve" the PDE when classical derivatives do not exist? Viscosity solutions answer this question. They provide the framework that guarantees existence, uniqueness, and stability for these pricing PDEs --- ensuring that the pricing operator $\mathcal{P}_\tau$ is well-defined even without classical smoothness, and placing all the methods of this chapter on rigorous footing.

---

## 1. Motivation: Why Classical Solutions Fail

### The Problem with Non-Smooth Payoffs

Consider a digital option with payoff:

$$
\Phi(S) = \mathbb{1}_{S > K}
$$

The Black-Scholes PDE:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

with terminal condition $V(S,T) = \mathbb{1}_{S > K}$ has **no classical solution**---the payoff is discontinuous!

### American Options

The free boundary problem:

$$
\max\left\{-\frac{\partial V}{\partial t} - rS\frac{\partial V}{\partial S} - \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} + rV, \, V - \Phi(S)\right\} = 0
$$

The solution $V$ is typically **not $C^2$** at the free boundary, so classical derivatives don't exist.

### The Gap

**Classical theory**: Requires $C^2$ solutions.

**Reality**: Financial PDEs rarely have $C^2$ solutions.

**Viscosity theory**: Fills this gap!

---

## 2. Fundamental Definitions

### General Parabolic PDE

Consider:

$$
F\left(x, t, u, Du, D^2u\right) = 0 \quad \text{in } \Omega \times (0,T)
$$

where:

- $u: \Omega \times [0,T] \to \mathbb{R}$ is the unknown
- $Du = \nabla u$ is the gradient
- $D^2u$ is the Hessian matrix
- $F$ is the **PDE operator** (possibly nonlinear)

**Boundary condition**: $u(x,T) = g(x)$

### Upper and Lower Semicontinuity

A function $u$ is:

- **Upper semicontinuous (USC)** if $\limsup_{y \to x}u(y) \leq u(x)$
- **Lower semicontinuous (LSC)** if $\liminf_{y \to x}u(y) \geq u(x)$

**Intuition**: USC functions don't have upward jumps; LSC functions don't have downward jumps.

### Test Functions

A function $\phi \in C^2(\Omega \times [0,T])$ is a **test function** for $u$ at $(x_0, t_0)$ if:

$$
u(x,t) - \phi(x,t) \text{ has a local maximum (or minimum) at } (x_0,t_0)
$$

---

## 3. Viscosity Subsolutions

### Definition

A USC function $u$ is a **viscosity subsolution** of $F(x,t,u,Du,D^2u) = 0$ if:

For every $(x_0,t_0) \in \Omega \times (0,T)$ and every $\phi \in C^2$ such that $u - \phi$ has a **local maximum** at $(x_0,t_0)$:

$$
F(x_0, t_0, u(x_0,t_0), D\phi(x_0,t_0), D^2\phi(x_0,t_0)) \leq 0
$$

### Intuition

At points where we can "touch from above" with a smooth function, the PDE inequality $F \leq 0$ holds in the **viscosity sense**.

### Why "Viscosity"?

Historically, this notion arose from adding **artificial viscosity** $\epsilon \Delta u$ to make the equation:

$$
F(x,t,u,Du,D^2u) - \epsilon \Delta u = 0
$$

which has smooth solutions. Taking $\epsilon \to 0$ gives the viscosity solution.

### Black-Scholes Example

For the operator:

$$
F = \frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 u}{\partial S^2} - ru
$$

A function $u$ is a viscosity subsolution if for every test function $\phi$ touching from above:

$$
\frac{\partial \phi}{\partial t} + rS\frac{\partial \phi}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 \phi}{\partial S^2} - r\phi \leq 0
$$

at the touching point.

---

## 4. Viscosity Supersolutions

### Definition

A LSC function $u$ is a **viscosity supersolution** of $F(x,t,u,Du,D^2u) = 0$ if:

For every $(x_0,t_0) \in \Omega \times (0,T)$ and every $\phi \in C^2$ such that $u - \phi$ has a **local minimum** at $(x_0,t_0)$:

$$
F(x_0, t_0, u(x_0,t_0), D\phi(x_0,t_0), D^2\phi(x_0,t_0)) \geq 0
$$

### Intuition

At points where we can "touch from below" with a smooth function, $F \geq 0$ in the viscosity sense.

---

## 5. Viscosity Solutions

### Definition

A continuous function $u$ is a **viscosity solution** if it is both:

1. A viscosity subsolution
2. A viscosity supersolution

$$
u \text{ is a viscosity solution} \iff \text{subsolution AND supersolution}
$$

### Equivalent Definition via Semijets

Define the **second-order superdifferential**:

$$
\overline{D^2}u(x_0,t_0) = \{(p, A) : u(x,t) \leq u(x_0,t_0) + \langle p, (x-x_0,t-t_0) \rangle + \frac{1}{2}\langle A(x-x_0,t-t_0), (x-x_0,t-t_0)\rangle + o(|(x-x_0,t-t_0)|^2)\}
$$

Then $u$ is a viscosity subsolution if:

$$
F(x_0,t_0,u(x_0,t_0), p, A) \leq 0 \quad \forall (p,A) \in \overline{D^2}u(x_0,t_0)
$$

Similarly for supersolutions using the **subdifferential** $\underline{D^2}u$.

### Classical Solutions are Viscosity Solutions

**Proposition**: If $u \in C^2$ is a classical solution, then $u$ is a viscosity solution.

**Proof**: At any point, $\phi(x,t) = u(x,t)$ is a test function, so:

$$
F(x,t,u,Du,D^2u) = 0
$$

This satisfies both $F \leq 0$ (subsolution) and $F \geq 0$ (supersolution). $\square$

---

## 6. Comparison Principle

### Statement

The **comparison principle** is the cornerstone of uniqueness theory.

**Theorem**: Let $u$ be a viscosity subsolution and $v$ be a viscosity supersolution of:

$$
F(x,t,w,Dw,D^2w) = 0 \quad \text{in } \Omega \times (0,T)
$$

Assume:

1. $F$ is **degenerate elliptic**: $F(x,t,r,p,A) \geq F(x,t,r,p,B)$ whenever $A \geq B$
2. $F$ is **continuous** and satisfies appropriate growth conditions
3. $u(x,T) \leq v(x,T)$ for all $x \in \Omega$
4. $u \leq v$ on the parabolic boundary

Then:

$$
u \leq v \quad \text{in } \Omega \times [0,T]
$$

### Degenerate Ellipticity

This means adding more "convexity" (larger $D^2u$) makes $F$ larger. For Black-Scholes:

$$
F = u_t + rSu_S + \frac{\sigma^2 S^2}{2}u_{SS} - ru
$$

We have $\frac{\partial F}{\partial u_{SS}} = \frac{\sigma^2 S^2}{2} \geq 0$, so it is degenerate elliptic.

### Uniqueness Corollary

If viscosity solutions exist, the comparison principle implies **uniqueness**:

If $u_1$ and $u_2$ are both viscosity solutions with the same boundary data, then $u_1 \leq u_2$ and $u_2 \leq u_1$, so $u_1 = u_2$.

---

## 7. Existence Theory

### Perron's Method

Define:

$$
\underline{u}(x,t) = \sup\{v(x,t) : v \text{ is a viscosity subsolution with } v(x,T) \leq g(x)\}
$$

$$
\overline{u}(x,t) = \inf\{w(x,t) : w \text{ is a viscosity supersolution with } w(x,T) \geq g(x)\}
$$

**Theorem**: Under appropriate conditions:

1. $\underline{u}$ is a viscosity subsolution
2. $\overline{u}$ is a viscosity supersolution
3. If $\underline{u} = \overline{u}$, then $u = \underline{u} = \overline{u}$ is the **unique** viscosity solution

### Vanishing Viscosity Method

Add artificial viscosity:

$$
F(x,t,u^\epsilon, Du^\epsilon, D^2u^\epsilon) - \epsilon \Delta u^\epsilon = 0
$$

This has smooth solutions $u^\epsilon$. Under suitable conditions:

$$
u^\epsilon \to u \quad \text{as } \epsilon \to 0
$$

and $u$ is the viscosity solution.

### Approximation by Smooth Functions

Replace the terminal data $g(x)$ by smooth approximations $g_n \in C^\infty$ with $g_n \to g$ uniformly.

Solve for smooth solutions $u_n$ with terminal data $g_n$.

Then $u_n \to u$ where $u$ is the viscosity solution with terminal data $g$.

---

## 8. Connection to Stochastic Control

### Dynamic Programming Principle

For the stochastic control problem:

$$
V(x,t) = \sup_{\alpha \in \mathcal{A}}\mathbb{E}\left[\int_t^T f(X_s^\alpha, \alpha_s)e^{-\int_t^s r(\tau)d\tau}ds + g(X_T^\alpha)e^{-\int_t^T r(\tau)d\tau} \mid X_t = x\right]
$$

where $X^\alpha$ satisfies:

$$
dX_s = b(X_s, \alpha_s)ds + \sigma(X_s, \alpha_s)dW_s
$$

The DPP states:

$$
V(x,t) = \sup_{\alpha}\mathbb{E}\left[\int_t^{t+h}f(X_s^\alpha,\alpha_s)e^{-\int_t^s r\, d\tau}ds + V(X_{t+h}^\alpha, t+h)e^{-\int_t^{t+h}r\, d\tau} \mid X_t = x\right]
$$

### HJB Equation

Taking $h \to 0$ formally gives the **Hamilton-Jacobi-Bellman equation**:

$$
\frac{\partial V}{\partial t} + \sup_{\alpha \in A}\left[b(x,\alpha) \cdot DV + \frac{1}{2}\text{tr}(\sigma\sigma^T(x,\alpha)D^2V) + f(x,\alpha)\right] - rV = 0
$$

### Viscosity Solution Connection

**Theorem**: The value function $V$ defined via the stochastic control problem is a **viscosity solution** of the HJB equation.

**Proof sketch**:

- Use DPP with smooth test functions
- For subsolution: if $\phi$ touches $V$ from above at $(x_0,t_0)$, then for small $h$:

$$
\phi(x_0,t_0) \geq \mathbb{E}[\cdots + \phi(X_{t_0+h}, t_0+h)e^{-rh}]
$$

- Ito's formula + supremum over $\alpha$ gives $F(\phi) \leq 0$
- Similarly for supersolution

This is why viscosity solutions are **natural** for finance!

---

## 9. American Options

### Obstacle Problem

For an American option with payoff $\Phi(S)$:

$$
V(S,t) = \sup_{\tau \in [t,T]}\mathbb{E}^{\mathbb{Q}}[e^{-r(\tau-t)}\Phi(S_\tau) \mid S_t = S]
$$

This is an **optimal stopping problem**.

### Variational Inequality

The value function satisfies:

$$
\min\left\{-\frac{\partial V}{\partial t} - \mathcal{L}V, \, V - \Phi\right\} = 0
$$

where $\mathcal{L}$ is the Black-Scholes operator:

$$
\mathcal{L}V = rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV
$$

### Regions

- **Continuation region**: $\mathcal{C} = \{(S,t) : V(S,t) > \Phi(S)\}$
    - Here: $-\frac{\partial V}{\partial t} - \mathcal{L}V = 0$

- **Stopping region**: $\mathcal{S} = \{(S,t) : V(S,t) = \Phi(S)\}$
    - Here: $-\frac{\partial V}{\partial t} - \mathcal{L}V \leq 0$

### Free Boundary

The boundary $\partial \mathcal{C}$ is the **optimal exercise boundary** $S^*(t)$.

At $S = S^*(t)$, $V$ is typically **not $C^2$**---only $C^1$ (smooth fit).

### Viscosity Solution

$V$ is the unique viscosity solution of the variational inequality with terminal condition $V(S,T) = \Phi(S)$.

**Key properties**:

1. $V \geq \Phi$ (no-arbitrage)
2. $V$ is continuous
3. In $\mathcal{C}$: $V$ is $C^{2,1}$ and satisfies the PDE
4. At the free boundary: only viscosity derivatives exist

---

## 10. Detailed Example: American Put

### Setup

Payoff: $\Phi(S) = (K - S)^+$

The variational inequality:

$$
\min\left\{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV, \, (K-S) - V\right\} = 0
$$

### Properties

1. **Early exercise**: Optimal to exercise when $S \leq S^*(t)$ for some boundary $S^*(t)$
2. **Smooth fit**: $V(S^*(t), t) = K - S^*(t)$ and $\frac{\partial V}{\partial S}(S^*(t), t) = -1$
3. **Non-smooth second derivative**: $\frac{\partial^2 V}{\partial S^2}$ jumps at $S^*(t)$

### Viscosity Formulation

For $S > S^*(t)$ (continuation region):

- Test functions touching from above: $F(\phi) \leq 0$
- Test functions touching from below: $F(\phi) \geq 0$
- Classical solution holds: $F = 0$

At $S = S^*(t)$ (free boundary):

- From above: $\phi$ satisfies $F(\phi) \leq 0$ (or $\phi = K - S$ which gives $V - \Phi = 0$)
- From below: $\phi$ satisfies $F(\phi) \geq 0$

For $S < S^*(t)$ (stopping region):

- $V = K - S$ (payoff)
- Any test function must satisfy the obstacle constraint

### Comparison Principle

Ensures uniqueness: any two viscosity solutions must coincide.

This guarantees that:

$$
V_{\text{viscosity}} = V_{\text{probabilistic}} = \sup_\tau \mathbb{E}[e^{-r\tau}\Phi(S_\tau)]
$$

---

## 11. Regularity Theory

### When is the Viscosity Solution Classical?

**Theorem**: If:

1. The payoff $\Phi$ is $C^2$
2. The coefficients are smooth
3. The operator is uniformly elliptic: $\sigma^2 S^2 \geq c > 0$

Then the viscosity solution is **classical** ($C^{2,1}$).

### Degenerate Case

For Black-Scholes, $\sigma^2 S^2 \to 0$ as $S \to 0$ (**degeneracy**).

The solution may fail to be $C^2$ at $S = 0$ even with smooth payoffs.

### Holder Continuity

**Theorem**: Under mild conditions, viscosity solutions are **locally Holder continuous**:

$$
|u(x,t) - u(y,s)| \leq C(|x-y|^\alpha + |t-s|^{\alpha/2})
$$

for some $\alpha \in (0,1)$.

### Interior Regularity

Away from boundaries and degeneracies, viscosity solutions are typically $C^{2,\alpha}$ (classical).

Singularities only occur at:

- Boundaries
- Degeneracy points
- Free boundaries
- Non-smooth payoffs

---

## 12. Numerical Methods

### Finite Difference Schemes

For the scheme:

$$
\frac{V_j^{n+1} - V_j^n}{\Delta t} + \mathcal{L}_h V_j^{n+1} = 0
$$

**Consistency**: The scheme approximates the PDE.

**Monotonicity**: Increasing $V$ at neighboring points increases the scheme.

**Stability**: Bounded growth of errors.

**Theorem (Barles-Souganidis)**: A consistent, monotone, stable scheme **converges** to the viscosity solution.

### Monotone Schemes

For Black-Scholes, a **monotone scheme** might be:

$$
\frac{V_j^{n+1} - V_j^n}{\Delta t} + r S_j \frac{V_{j+1}^{n+1} - V_{j-1}^{n+1}}{2\Delta S} + \frac{\sigma^2 S_j^2}{2}\frac{V_{j+1}^{n+1} - 2V_j^{n+1} + V_{j-1}^{n+1}}{(\Delta S)^2} - rV_j^{n+1} = 0
$$

provided the **CFL condition** ensures monotonicity.

### American Options

At each time step:

$$
V_j^{n+1} = \max\left\{\Phi(S_j), \text{continuation value}\right\}
$$

This automatically enforces the obstacle constraint.

### Convergence

**Theorem**: The discrete scheme converges to the viscosity solution of the continuous variational inequality.

This justifies **practical algorithms** like:

- Finite differences
- Binomial trees
- Trinomial trees

---

## 13. Obstacle Problems and Penalization

### Penalization Method

Replace the obstacle problem:

$$
\min\{-u_t - \mathcal{L}u, u - g\} = 0
$$

with the penalized equation:

$$
-u_t^\epsilon - \mathcal{L}u^\epsilon - \frac{1}{\epsilon}(u^\epsilon - g)^- = 0
$$

where $(x)^- = \max(-x, 0)$.

### Convergence

As $\epsilon \to 0$:

$$
u^\epsilon \to u
$$

where $u$ is the viscosity solution of the obstacle problem.

**Proof sketch**:

- $u^\epsilon$ is smooth
- Comparison principle for penalized equation
- Stability under limits

### Regularization by Penalty

The penalty term $-\frac{1}{\epsilon}(u^\epsilon - g)^-$ acts as:

- A large negative force when $u^\epsilon < g$ (pushing $u^\epsilon$ up)
- Zero when $u^\epsilon \geq g$ (inactive)

As $\epsilon \to 0$, this enforces $u \geq g$ exactly.

---

## 14. Comparison with Other Solution Concepts

### Classical Solutions

- **Requires**: $C^2$ regularity
- **Applies**: Smooth data, non-degenerate operators
- **Unique**: Yes, when exists
- **Finance**: European options with smooth payoffs

### Weak Solutions

- **Requires**: $H^1$ (Sobolev space)
- **Applies**: Variational formulations
- **Unique**: Not always
- **Finance**: Less common

### Viscosity Solutions

- **Requires**: Only continuity
- **Applies**: Non-smooth data, degenerate/singular operators, optimal control
- **Unique**: Yes, under comparison principle
- **Finance**: American options, stochastic control

### Strong vs. Viscosity

If $u \in C^2$ solves the PDE classically, then:

$$
\text{Classical} \implies \text{Viscosity} \implies \text{Weak}
$$

But the converse is false---viscosity solutions are **more general**.

---

## 15. Probabilistic Interpretation

### Perron-Frobenius Formula

For the obstacle problem:

$$
u(x,t) = \sup_{\tau \leq T-t}\mathbb{E}\left[\int_t^\tau f(X_s)e^{-r(s-t)}ds + g(X_\tau)e^{-r(\tau-t)}\right]
$$

The viscosity solution $u$ **is** the value function.

### Comparison via Probability

To prove comparison, use:

$$
u(x,t) \leq \mathbb{E}[\cdots] \quad \text{for all strategies}
$$

$$
v(x,t) \geq \mathbb{E}[\cdots] \quad \text{for optimal strategy}
$$

Therefore $u \leq v$.

### Martingale Characterization

A function $u$ is a viscosity solution iff the process:

$$
M_t = e^{-rt}u(X_t,t) + \int_0^t e^{-rs}f(X_s,s)ds
$$

is a **supermartingale** for all strategies and a **martingale** for optimal strategies.

---

## 16. Summary

| **Problem** | **Classical Approach** | **Viscosity Approach** |
|---|---|---|
| European call (smooth) | PDE + Feynman-Kac | Same (viscosity = classical) |
| Digital option | Fails (discontinuous) | Viscosity solution exists |
| American put | Free boundary problem | Obstacle problem (viscosity) |
| Stochastic control | Verify HJB formally | Value function is viscosity solution |
| Numerical methods | Ad hoc convergence | Barles-Souganidis theorem |

For a stochastic control problem with value function $V$:

1. $V$ is **continuous**
2. $V$ is a **viscosity solution** of the HJB equation
3. $V$ is the **unique** viscosity solution (comparison principle)
4. Numerical approximations **converge** to $V$

These four statements constitute the complete theoretical toolkit that places the PDE-based pricing methods of this chapter on rigorous footing. In particular, the heat equation derivation, the Feynman-Kac representation, and the Fourier inversion all rely on the pricing PDE having a unique solution that depends continuously on the data. Viscosity theory is what guarantees these properties --- even for the discontinuous payoffs and degenerate coefficients that arise routinely in practice.

With this, the chapter is complete. Every section has presented a different representation of the same pricing semigroup $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$: as a kernel, an expectation, a spectral transform, a resolvent, an eigenfunction expansion, a set of scaling invariants, a measure change, and finally a well-posed operator. The diversity of techniques is not redundancy --- it reflects different coordinate systems on a single mathematical object, and it is this unity that makes the Black--Scholes theory both deep and practical.

---

## Exercises

**Exercise 1.** A digital call option has payoff $\Phi(S) = \mathbf{1}_{\{S > K\}}$, which is discontinuous at $S = K$. Explain why the Black-Scholes PDE with this terminal condition has no classical ($C^{2,1}$) solution. Then describe how the viscosity solution framework resolves this issue, and verify that $V(S,t) = e^{-r(T-t)}\mathcal{N}(d_2)$ is the viscosity solution.

??? success "Solution to Exercise 1"

    **Why the classical solution fails**: A classical ($C^{2,1}$) solution requires that $V(S,t)$ be twice continuously differentiable in $S$ and once in $t$ on the entire domain, including at the terminal time $T$. However, the terminal condition $V(S,T) = \mathbf{1}_{\{S > K\}}$ is discontinuous at $S = K$.

    For $V$ to be $C^{2,1}$ up to $t = T$, the terminal data must be sufficiently smooth. The discontinuity at $S = K$ means that no $C^{2,1}$ function can satisfy $V(S,T) = \mathbf{1}_{\{S > K\}}$ pointwise while also solving the PDE in the classical sense. Near $S = K$ as $t \to T^-$, the solution develops increasingly steep gradients: $\frac{\partial V}{\partial S}$ behaves like a delta function and $\frac{\partial^2 V}{\partial S^2}$ diverges.

    **Viscosity solution framework**: The viscosity approach replaces pointwise derivatives with test function comparisons. A function $V$ is a viscosity solution if for every smooth test function $\phi$ that touches $V$ from above (or below) at a point $(S_0, t_0)$, the PDE inequality holds for $\phi$ at that point. This requires only continuity of $V$, not differentiability.

    **Verification**: The candidate solution is $V(S,t) = e^{-r(T-t)}\mathcal{N}(d_2)$ where

    $$
    d_2 = \frac{\ln(S/K) + (r - \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}
    $$

    For $t < T$, this function is $C^\infty$ in both $S$ and $t$ (as a composition of smooth functions with $S > 0$ and $T - t > 0$), so it is a classical solution on $(0,\infty) \times [0,T)$. Being a classical solution on the interior automatically makes it a viscosity solution there.

    At $t = T$, we verify: as $t \to T^-$, $\sigma\sqrt{T-t} \to 0$, so $d_2 \to +\infty$ if $S > K$ (giving $\mathcal{N}(d_2) \to 1$) and $d_2 \to -\infty$ if $S < K$ (giving $\mathcal{N}(d_2) \to 0$). Thus $V(S,T^-) = \mathbf{1}_{\{S > K\}}$ for $S \neq K$, and the terminal condition is met in the viscosity sense. The viscosity framework extends the notion of solution to accommodate this boundary discontinuity through semicontinuous envelopes.

---

**Exercise 2.** State the definition of a viscosity subsolution and supersolution for the Black-Scholes PDE. Using these definitions, explain why the maximum of two viscosity solutions is a viscosity subsolution but not necessarily a viscosity solution.

??? success "Solution to Exercise 2"

    **Definition of viscosity subsolution**: A function $u$ that is upper semicontinuous (USC) is a viscosity subsolution of the Black-Scholes PDE

    $$
    -\frac{\partial V}{\partial t} - rS\frac{\partial V}{\partial S} - \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} + rV = 0
    $$

    if for every smooth test function $\phi \in C^{2,1}$ such that $u - \phi$ has a local maximum at $(S_0, t_0)$, we have

    $$
    -\frac{\partial \phi}{\partial t}(S_0,t_0) - rS_0\frac{\partial \phi}{\partial S}(S_0,t_0) - \frac{\sigma^2 S_0^2}{2}\frac{\partial^2 \phi}{\partial S^2}(S_0,t_0) + r\,u(S_0,t_0) \leq 0
    $$

    **Definition of viscosity supersolution**: A function $v$ that is lower semicontinuous (LSC) is a viscosity supersolution if for every smooth $\phi$ such that $v - \phi$ has a local minimum at $(S_0, t_0)$:

    $$
    -\frac{\partial \phi}{\partial t}(S_0,t_0) - rS_0\frac{\partial \phi}{\partial S}(S_0,t_0) - \frac{\sigma^2 S_0^2}{2}\frac{\partial^2 \phi}{\partial S^2}(S_0,t_0) + r\,v(S_0,t_0) \geq 0
    $$

    **Why $\max(u_1, u_2)$ is a subsolution**: Let $u_1, u_2$ be viscosity subsolutions and define $w = \max(u_1, u_2)$. At any point $(S_0, t_0)$, suppose $\phi$ touches $w$ from above, i.e., $w - \phi$ has a local maximum at $(S_0, t_0)$. Without loss of generality, assume $w(S_0, t_0) = u_1(S_0, t_0) \geq u_2(S_0, t_0)$. Then $u_1 \leq w \leq \phi$ locally, and $u_1(S_0, t_0) = \phi(S_0, t_0)$, so $\phi$ also touches $u_1$ from above at $(S_0, t_0)$. Since $u_1$ is a subsolution, the subsolution inequality holds for $\phi$ at that point, making $w$ a subsolution.

    **Why it is not necessarily a viscosity solution**: Being a viscosity solution requires being both a subsolution and a supersolution. The function $w = \max(u_1, u_2)$ is generally not a supersolution because at points where $u_1 = u_2$ and the two functions cross, $w$ may develop a corner (a non-smooth kink). At such a corner, a test function touching $w$ from below must lie below the maximum of the two, but the supersolution inequality need not hold for any such test function. In particular, the second derivative of any test function touching $w$ from below at a kink point is constrained in a way that the supersolution inequality may be violated.

---

**Exercise 3.** For an American put option, the value function satisfies the variational inequality $\min\left(-\mathcal{L}V, \, V - (K - S)^+\right) = 0$, where $\mathcal{L}$ is the Black-Scholes differential operator. Interpret each of the two conditions in this inequality financially, and explain why the obstacle problem formulation is natural for early exercise.

??? success "Solution to Exercise 3"

    The variational inequality is $\min\left(-\mathcal{L}V,\, V - (K-S)^+\right) = 0$ where

    $$
    \mathcal{L}V = \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV
    $$

    **First condition: $V \geq (K - S)^+$**. This is the **obstacle constraint**. It states that the American put value is always at least the immediate exercise payoff. Financially, if $V < (K - S)^+$ at any point, an arbitrage opportunity would exist: buy the put for $V$, exercise immediately, and pocket $(K - S)^+ - V > 0$. The holder has the right (not obligation) to exercise at any time, so the option value must dominate the payoff.

    **Second condition: $-\mathcal{L}V \geq 0$**. This states that the option earns at least the risk-free rate in the continuation region. Equivalently, the discounted option value is a supermartingale under the risk-neutral measure. If $-\mathcal{L}V < 0$ at some point, the holder could do better by holding the option (earning more than $r$), which would contradict optimality of exercise.

    **The minimum condition**: The "min = 0" structure encodes the complementarity: at every $(S, t)$, exactly one of the following holds:

    - **Continuation region** ($V > (K-S)^+$): The option is worth more alive than dead, so $\mathcal{L}V = 0$ (the standard Black-Scholes PDE holds). The holder optimally continues.

    - **Exercise region** ($V = (K-S)^+$): The option is exercised immediately. Here $-\mathcal{L}V \geq 0$, meaning the PDE is not satisfied as an equality; instead, the holder captures the payoff.

    **Why the obstacle formulation is natural**: Early exercise creates a free boundary $S^*(t)$ separating the continuation and exercise regions. The classical free-boundary approach must explicitly track this curve, which is analytically difficult. The obstacle problem encodes both the PDE and the free boundary condition in a single variational inequality, allowing the free boundary to emerge as part of the solution rather than being specified a priori. The viscosity framework handles the non-smooth behavior at the free boundary (where $V$ is $C^1$ but not $C^2$) without requiring classical differentiability.

---

**Exercise 4.** The comparison principle for viscosity solutions states that if $u$ is a subsolution and $v$ is a supersolution with $u(S,T) \leq v(S,T)$, then $u \leq v$ everywhere. Explain why this principle is essential for proving uniqueness of viscosity solutions. Give a financial example where non-uniqueness of PDE solutions would lead to arbitrage.

??? success "Solution to Exercise 4"

    **Why comparison implies uniqueness**: Suppose $u$ and $v$ are both viscosity solutions of the Black-Scholes PDE with the same terminal condition $u(S,T) = v(S,T) = g(S)$. A viscosity solution is both a subsolution and a supersolution. Applying the comparison principle:

    - Since $u$ is a subsolution and $v$ is a supersolution with $u(S,T) = g(S) \leq g(S) = v(S,T)$, we get $u \leq v$ everywhere.
    - Since $v$ is a subsolution and $u$ is a supersolution with $v(S,T) \leq u(S,T)$, we get $v \leq u$ everywhere.

    Therefore $u = v$, establishing uniqueness.

    Without comparison, uniqueness can fail: there could be multiple functions satisfying the PDE in some generalized sense. The comparison principle is the crucial analytical tool that prevents this.

    **Financial example of arbitrage from non-uniqueness**: Suppose the Black-Scholes PDE with European call terminal data $g(S) = (S - K)^+$ had two distinct viscosity solutions $V_1(S,t)$ and $V_2(S,t)$ with $V_1(S_0, 0) < V_2(S_0, 0)$ for some $S_0$. A market maker could:

    - Sell the option for $V_2(S_0, 0)$ (claiming this is the correct price)
    - Hedge using the delta from $V_1$ (the cheaper replication cost)
    - Pocket $V_2(S_0, 0) - V_1(S_0, 0) > 0$ as riskless profit

    Both $V_1$ and $V_2$ would be valid self-financing replicating strategies reaching the same terminal payoff, but at different initial costs, violating the law of one price. The comparison principle (and hence uniqueness) ensures that no-arbitrage pricing yields a single, well-defined price.

---

**Exercise 5.** The Barles-Souganidis theorem guarantees convergence of numerical schemes to the viscosity solution if the scheme is monotone, consistent, and stable. For the explicit finite-difference scheme applied to the Black-Scholes PDE, state the CFL condition that ensures monotonicity and explain what happens when it is violated.

??? success "Solution to Exercise 5"

    The explicit finite-difference scheme approximates the Black-Scholes PDE on a grid $(S_i, t^n)$ with spatial step $\Delta S$ and time step $\Delta t$. After transformation to the heat equation (or working directly), the scheme updates values as:

    $$
    V_i^{n} = \alpha_i V_{i-1}^{n+1} + \beta_i V_i^{n+1} + \gamma_i V_{i+1}^{n+1}
    $$

    where the coefficients (for the untransformed BS PDE) are:

    $$
    \alpha_i = \frac{\Delta t}{2}\left(\frac{\sigma^2 i^2}{1} - ri\right)\frac{1}{1+r\Delta t}, \quad \gamma_i = \frac{\Delta t}{2}\left(\sigma^2 i^2 + ri\right)\frac{1}{1+r\Delta t}
    $$

    $$
    \beta_i = 1 - \sigma^2 i^2 \Delta t \cdot \frac{1}{1+r\Delta t}
    $$

    (where $i$ indexes the spatial grid with $S_i = i\Delta S$).

    **Monotonicity condition (CFL)**: The Barles-Souganidis theorem requires the scheme to be **monotone**: the numerical solution at time $t^n$ must be a non-decreasing function of the values at time $t^{n+1}$. This means all coefficients $\alpha_i, \beta_i, \gamma_i$ must be non-negative. The binding constraint is typically $\beta_i \geq 0$, which gives:

    $$
    \sigma^2 i^2 \Delta t \leq 1 \quad \text{for all grid points } i
    $$

    If $i_{\max}$ is the largest grid index, the **CFL condition** is:

    $$
    \Delta t \leq \frac{1}{\sigma^2 i_{\max}^2}
    $$

    Equivalently, in terms of $S_{\max} = i_{\max}\Delta S$:

    $$
    \Delta t \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
    $$

    **When CFL is violated**: If $\Delta t$ is too large, some coefficients become negative. This means the scheme is no longer monotone: increasing the future value at a neighboring node can decrease the current value, which is financially absurd (a higher future payoff should not reduce the current option price). Numerically, the scheme produces **spurious oscillations** that grow exponentially, leading to instability. More fundamentally, without monotonicity, the Barles-Souganidis convergence theorem does not apply, and the finite-difference solution may converge to the wrong function (or not converge at all), rather than to the unique viscosity solution.
