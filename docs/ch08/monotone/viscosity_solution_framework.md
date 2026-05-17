# Viscosity Solution Framework

When $u$ has a corner -- say $u(x)=|x|$, or the American-option price at the free boundary -- the second derivative does not exist there, so "u solves $F(u,Du,D^2u)=0$ pointwise" is meaningless. The viscosity trick replaces $u$'s missing derivatives with those of *touching* smooth test functions $\varphi$: $u$ is a **subsolution** if $F(\varphi,D\varphi,D^2\varphi)\le 0$ at every point where $\varphi$ touches $u$ from above, and a **supersolution** if the reverse inequality holds for $\varphi$ touching from below. This single substitution -- "lend $u$ the derivatives of a smooth function tangent to it" -- is the entire content of the **viscosity solution framework**.

---

## Why Classical Solutions Fail

### The Black-Scholes PDE at S = 0

Recall (see [§ Discounting and killing term](../../ch06/bs_pde_structure/discounting_and_killing_term.md)): the Black-Scholes PDE is $V_t + \tfrac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$. Its diffusion coefficient $\tfrac{1}{2}\sigma^2 S^2$ **degenerates** (vanishes) at $S=0$, where the PDE reduces to:

$$
\frac{\partial V}{\partial t} - rV = 0
$$

The character of the equation changes: it is no longer uniformly parabolic. Classical PDE theory requires uniform parabolicity for existence and regularity results to hold.

### Non-Smooth Terminal Data

The European call payoff $\Phi(S) = (S - K)^+$ has a kink (discontinuous first derivative) at $S = K$. While the solution immediately becomes smooth for $t < T$ (the heat equation smooths out kinks), the solution of the **American option problem** may retain a kink at the free boundary for all times.

### Obstacle Problems

American option pricing leads to the variational inequality:

$$
\min\!\left(-\frac{\partial V}{\partial t} - \mathcal{L}V,\; V - \Phi\right) = 0
$$

where $\mathcal{L}V = \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV$. The solution switches between two regimes, and the boundary between them (the free boundary) is not known a priori. Classical solutions cannot handle this minimum condition.

---

## Intuition: Touching from Above and Below

The key idea behind viscosity solutions is to replace derivatives of the (possibly non-smooth) solution with derivatives of smooth **test functions** that touch the solution.

### Geometric Picture

Consider a continuous function $u$ that satisfies a PDE in some generalized sense.

**Subsolution test**: If a smooth function $\varphi$ touches $u$ **from above** at a point $x_0$ (meaning $\varphi \geq u$ near $x_0$ and $\varphi(x_0) = u(x_0)$), then at $x_0$:

- $u$ has a local maximum of $u - \varphi$, so $u - \varphi \leq 0$ near $x_0$
- The derivatives of $\varphi$ at $x_0$ serve as "generalized derivatives" of $u$
- If $u$ were smooth, its derivatives would match those of $\varphi$ at $x_0$

**Supersolution test**: Similarly, if $\varphi$ touches $u$ **from below** at $x_0$ ($\varphi \leq u$ near $x_0$, $\varphi(x_0) = u(x_0)$), the derivatives of $\varphi$ provide "generalized derivatives" from below.

!!! info "Core Principle"
    A viscosity solution does not need to be differentiable. Instead, we test the PDE using the derivatives of any smooth function that touches the solution. The PDE inequality must hold for **every** such test function.

---

## Formal Definitions

Consider the general nonlinear PDE:

$$
F(x, u(x), Du(x), D^2u(x)) = 0
$$

where $x \in \Omega \subset \mathbb{R}^n$, $Du$ is the gradient, and $D^2u$ is the Hessian. The function $F$ is assumed to be **degenerate elliptic**: $F(x, r, p, X) \leq F(x, r, p, Y)$ whenever $X \geq Y$ (in the matrix ordering).

For parabolic equations like Black-Scholes, $x = (\tau, S)$ and the degenerate ellipticity is with respect to the spatial Hessian.

### Viscosity Subsolution

!!! abstract "Definition (Viscosity Subsolution)"
    An upper semicontinuous function $u : \Omega \to \mathbb{R}$ is a **viscosity subsolution** of $F = 0$ if for every $\varphi \in C^2(\Omega)$ and every local maximum point $x_0$ of $u - \varphi$:

    $$
    F(x_0, u(x_0), D\varphi(x_0), D^2\varphi(x_0)) \leq 0
    $$

### Viscosity Supersolution

!!! abstract "Definition (Viscosity Supersolution)"
    A lower semicontinuous function $u : \Omega \to \mathbb{R}$ is a **viscosity supersolution** of $F = 0$ if for every $\varphi \in C^2(\Omega)$ and every local minimum point $x_0$ of $u - \varphi$:

    $$
    F(x_0, u(x_0), D\varphi(x_0), D^2\varphi(x_0)) \geq 0
    $$

### Viscosity Solution

!!! abstract "Definition (Viscosity Solution)"
    A continuous function $u$ is a **viscosity solution** if it is both a viscosity subsolution and a viscosity supersolution.

---

## Semicontinuity

The definitions use semicontinuous functions to handle possible discontinuities.

**Upper semicontinuous (USC)**: $u^*(x) = \limsup_{y \to x} u(y)$. This is the smallest USC function $\geq u$.

**Lower semicontinuous (LSC)**: $u_*(x) = \liminf_{y \to x} u(y)$. This is the largest LSC function $\leq u$.

For continuous functions, $u^* = u_* = u$, and the definitions coincide.

In practice, for Black-Scholes problems with continuous payoffs and reasonable boundary conditions, the viscosity solution is continuous, and the USC/LSC distinction does not arise.

---

## Equivalent Formulation: Semijets

An alternative formulation avoids explicit test functions by using **semijets**.

**Superjet**: The second-order superjet of $u$ at $x_0$ is:

$$
J^{2,+}u(x_0) = \{(p, X) : u(x) \leq u(x_0) + p \cdot (x - x_0) + \tfrac{1}{2}(x-x_0)^T X (x-x_0) + o(|x-x_0|^2)\}
$$

These are the $(p, X)$ pairs such that a quadratic with gradient $p$ and Hessian $X$ touches $u$ from above at $x_0$.

**Subjet**: $J^{2,-}u(x_0)$ is defined analogously with the inequality reversed.

The viscosity subsolution condition becomes: for all $(p, X) \in J^{2,+}u(x_0)$:

$$
F(x_0, u(x_0), p, X) \leq 0
$$

This formulation is more compact and is used in many theoretical proofs.

---

## Classical Solutions are Viscosity Solutions

**Proposition**: If $u \in C^2(\Omega)$ is a classical solution of $F = 0$, then $u$ is a viscosity solution.

*Proof*: Let $\varphi \in C^2$ and suppose $u - \varphi$ has a local maximum at $x_0$. Then:

$$
D(u - \varphi)(x_0) = 0 \quad \Longrightarrow \quad Du(x_0) = D\varphi(x_0)
$$

$$
D^2(u - \varphi)(x_0) \leq 0 \quad \Longrightarrow \quad D^2u(x_0) \leq D^2\varphi(x_0)
$$

Since $F$ is degenerate elliptic ($F$ is non-decreasing in the matrix argument going down):

$$
F(x_0, u(x_0), D\varphi(x_0), D^2\varphi(x_0)) \leq F(x_0, u(x_0), Du(x_0), D^2u(x_0)) = 0
$$

So the subsolution condition holds. The supersolution condition is proved similarly. $\square$

The converse is not generally true: viscosity solutions need not be $C^2$, and when they are, they are classical solutions.

---

## Examples in Financial Mathematics

### Example 1: The Heat Equation

For $u_\tau = u_{xx}$ with continuous initial data, the viscosity solution coincides with the classical solution. Viscosity theory adds nothing new here, but it provides a consistent framework.

### Example 2: Degenerate Diffusion

For $u_\tau = x^2 u_{xx}$ (the Black-Scholes diffusion term), the diffusion degenerates at $x = 0$. The viscosity framework handles this without special treatment of the degenerate boundary.

### Example 3: American Option (Obstacle Problem)

Recall (see [§ American Options](../american_options/free_boundary_problems_american_options.md)): the value satisfies the variational inequality $\min(-u_\tau + \mathcal{L}u, u - \Phi) = 0$. In viscosity sense, the subsolution requires either $-\varphi_\tau + \mathcal{L}\varphi \leq 0$ or $u \leq \Phi$ at each touching point; the supersolution requires the corresponding $\geq 0$ alternative. The free boundary $S^*(t)$ is encoded implicitly.

### Example 4: Discontinuous Payoffs (Digital Options)

A digital (binary) call pays $\Phi(S) = \mathbf{1}_{S > K}$, which is discontinuous at $S = K$. The viscosity framework handles this via the USC/LSC envelopes:

$$
\Phi^*(K) = 1, \quad \Phi_*(K) = 0
$$

The viscosity solution gives the unique price consistent with the no-arbitrage principle.

---

## Why Viscosity Solutions for Numerical Analysis

The viscosity framework is essential for the convergence theory of numerical methods because:

1. **Uniqueness**: Under a comparison principle, viscosity solutions are unique. This gives a well-defined target for numerical approximation
2. **Stability**: Viscosity solutions are stable under uniform convergence and certain relaxed limits (half-relaxed limits). This allows passing to limits of numerical approximations
3. **Generality**: The same framework covers smooth European options, degenerate boundaries, American options, and barrier options
4. **Monotone scheme theory**: The Barles-Souganidis theorem provides a complete convergence result for monotone, stable, consistent schemes, using viscosity solutions as the solution concept

!!! tip "Practical Takeaway"
    For practitioners, viscosity solutions justify the convergence of standard FDM implementations. The key practical requirement is that the numerical scheme be **monotone** (non-negative stencil coefficients), which connects directly to the CFL condition and upwind differencing.

---

## Summary

| Concept | Classical solutions | Viscosity solutions |
|---------|--------------------|--------------------|
| **Regularity** | Requires $u \in C^2$ | Requires only continuity |
| **PDE satisfaction** | Pointwise | Via test functions |
| **Degenerate PDEs** | May fail to exist | Always well-defined |
| **Obstacle problems** | Requires free boundary | Built into the definition |
| **Uniqueness** | Case-by-case | Via comparison principle |
| **Numerical convergence** | Lax equivalence | Barles-Souganidis theorem |

$$
\boxed{
\text{Viscosity solution: } F(x_0, u(x_0), D\varphi(x_0), D^2\varphi(x_0)) \leq 0 \text{ (sub)}, \geq 0 \text{ (super)}
}
$$

Viscosity solutions provide the rigorous mathematical foundation for proving that finite difference schemes converge to the correct answer, especially in the presence of degeneracies and non-smoothness that arise naturally in option pricing.

---

## Exercises

**Exercise 1.** The Black-Scholes PDE has diffusion coefficient $\frac{1}{2}\sigma^2 S^2$, which degenerates at $S = 0$. Explain what the PDE reduces to at $S = 0$ and why this prevents the classical theory from applying uniformly on $[0, \infty)$.

??? success "Solution to Exercise 1"
    At $S = 0$, the diffusion coefficient $\frac{1}{2}\sigma^2 S^2$ vanishes, so the Black-Scholes PDE reduces to

    $$
    \frac{\partial V}{\partial t} - rV = 0
    $$

    This is a first-order ODE in time, with the solution $V(t, 0) = e^{-r(T-t)} V(T, 0) = e^{-r(T-t)} \Phi(0)$.

    Classical PDE theory for parabolic equations relies on **uniform parabolicity**: the diffusion coefficient must be bounded below by a positive constant $\lambda > 0$ on the domain. This ensures the equation has a smoothing effect, which in turn guarantees existence, uniqueness, and regularity of solutions via standard results (e.g., Schauder estimates).

    On the domain $[0, \infty)$, the diffusion coefficient $\frac{1}{2}\sigma^2 S^2$ is zero at $S = 0$, so the equation is **degenerate parabolic**. The character of the equation changes from a second-order parabolic PDE (for $S > 0$) to a first-order ODE (at $S = 0$). Classical interior regularity results require uniform parabolicity and therefore cannot be applied uniformly across $[0, \infty)$. This degeneracy is precisely what motivates the viscosity solution framework, which is designed to handle degenerate elliptic and parabolic equations without requiring uniform parabolicity.

---

**Exercise 2.** State the definition of a viscosity subsolution of the PDE $F(x, u, Du, D^2u) = 0$. Explain the geometric meaning of "a smooth test function $\varphi$ touching $u$ from above at $x_0$" and why the derivatives of $\varphi$ serve as generalized derivatives of $u$.

??? success "Solution to Exercise 2"
    **Definition**: An upper semicontinuous function $u : \Omega \to \mathbb{R}$ is a **viscosity subsolution** of $F(x, u, Du, D^2u) = 0$ if for every $\varphi \in C^2(\Omega)$ and every point $x_0$ at which $u - \varphi$ attains a local maximum:

    $$
    F(x_0, u(x_0), D\varphi(x_0), D^2\varphi(x_0)) \leq 0
    $$

    **Geometric meaning**: A smooth test function $\varphi$ "touches $u$ from above at $x_0$" means $\varphi(x) \geq u(x)$ in a neighborhood of $x_0$ and $\varphi(x_0) = u(x_0)$. Equivalently, $u - \varphi$ has a local maximum at $x_0$ with value zero.

    At this touching point, since $\varphi \geq u$ near $x_0$ with equality at $x_0$, the function $u - \varphi$ has a local maximum at $x_0$. If $u$ were differentiable at $x_0$, then the first-order necessary conditions would give $D(u - \varphi)(x_0) = 0$, so $Du(x_0) = D\varphi(x_0)$. The second-order necessary conditions would give $D^2(u - \varphi)(x_0) \leq 0$, so $D^2u(x_0) \leq D^2\varphi(x_0)$.

    The key insight is that even when $u$ is not differentiable, the derivatives $D\varphi(x_0)$ and $D^2\varphi(x_0)$ serve as "generalized derivatives" that capture what $Du$ and $D^2u$ would be if $u$ were smooth. The touching condition constrains $\varphi$ to agree with $u$ to first order (and be no less curved than $u$) at $x_0$, so testing the PDE on $\varphi$ provides a meaningful one-sided constraint on $u$.

---

**Exercise 3.** Prove that if $u \in C^2$ is a classical solution of $F = 0$ (with $F$ degenerate elliptic), then $u$ is a viscosity solution. The key steps are: (i) at a local max of $u - \varphi$, show $Du = D\varphi$ and $D^2u \leq D^2\varphi$; (ii) use degenerate ellipticity to conclude $F(x_0, u, D\varphi, D^2\varphi) \leq 0$.

??? success "Solution to Exercise 3"
    **Claim**: If $u \in C^2(\Omega)$ satisfies $F(x, u, Du, D^2u) = 0$ pointwise, then $u$ is a viscosity solution.

    **Subsolution property**: Let $\varphi \in C^2$ and suppose $u - \varphi$ has a local maximum at $x_0$. Since $u \in C^2$, the first- and second-order necessary conditions for a local maximum give:

    $$
    D(u - \varphi)(x_0) = 0 \quad \Longrightarrow \quad Du(x_0) = D\varphi(x_0)
    $$

    $$
    D^2(u - \varphi)(x_0) \leq 0 \quad \Longrightarrow \quad D^2u(x_0) \leq D^2\varphi(x_0)
    $$

    Since $F$ is degenerate elliptic, meaning $F(x, r, p, X) \leq F(x, r, p, Y)$ whenever $X \geq Y$ (in the positive semidefinite ordering), and since $D^2\varphi(x_0) \geq D^2u(x_0)$:

    $$
    F(x_0, u(x_0), D\varphi(x_0), D^2\varphi(x_0)) \leq F(x_0, u(x_0), Du(x_0), D^2u(x_0)) = 0
    $$

    where the equality follows from the fact that $u$ is a classical solution. This establishes the subsolution condition.

    **Supersolution property**: Let $\varphi \in C^2$ and suppose $u - \varphi$ has a local minimum at $x_0$. The necessary conditions give $Du(x_0) = D\varphi(x_0)$ and $D^2u(x_0) \geq D^2\varphi(x_0)$. By degenerate ellipticity:

    $$
    F(x_0, u(x_0), D\varphi(x_0), D^2\varphi(x_0)) \geq F(x_0, u(x_0), Du(x_0), D^2u(x_0)) = 0
    $$

    Since both conditions hold, $u$ is a viscosity solution. $\square$

---

**Exercise 4.** For the American option obstacle problem $\min(-u_\tau + \mathcal{L}u, u - \Phi) = 0$, write out the viscosity subsolution and supersolution conditions. Explain how the $\min$ operator encodes the free boundary without explicitly tracking $S^*(t)$.

??? success "Solution to Exercise 4"
    For the American option obstacle problem $\min(-u_\tau + \mathcal{L}u, \; u - \Phi) = 0$, define $F(\tau, S, u, Du, D^2u) = \min(-u_\tau + \mathcal{L}u, \; u - \Phi)$ where $\mathcal{L}u = \frac{1}{2}\sigma^2 S^2 u_{SS} + rSu_S - ru$.

    **Viscosity subsolution condition**: $u$ (upper semicontinuous) is a viscosity subsolution if for every smooth $\varphi$ such that $u - \varphi$ has a local maximum at $(\tau_0, S_0)$:

    $$
    \min\!\left(-\varphi_\tau(\tau_0, S_0) + \mathcal{L}\varphi(\tau_0, S_0), \; u(\tau_0, S_0) - \Phi(S_0)\right) \leq 0
    $$

    This means at least one of the following holds: either $-\varphi_\tau + \mathcal{L}\varphi \leq 0$ (the PDE inequality is satisfied in the viscosity sense) or $u \leq \Phi$ (the value is at or below the payoff).

    **Viscosity supersolution condition**: $u$ (lower semicontinuous) is a viscosity supersolution if for every smooth $\varphi$ such that $u - \varphi$ has a local minimum at $(\tau_0, S_0)$:

    $$
    \min\!\left(-\varphi_\tau(\tau_0, S_0) + \mathcal{L}\varphi(\tau_0, S_0), \; u(\tau_0, S_0) - \Phi(S_0)\right) \geq 0
    $$

    This means **both** conditions hold simultaneously: $-\varphi_\tau + \mathcal{L}\varphi \geq 0$ **and** $u \geq \Phi$.

    **How the $\min$ encodes the free boundary**: The $\min$ operator creates an implicit switching rule. At any point $(\tau, S)$:

    - In the **continuation region** (where $u > \Phi$), the second argument of $\min$ is positive, so the $\min = 0$ condition forces $-u_\tau + \mathcal{L}u = 0$ (the standard Black-Scholes PDE holds).
    - In the **exercise region** (where $u = \Phi$), the first argument need not be zero; instead, $-u_\tau + \mathcal{L}u \geq 0$ (the holder would prefer to exercise).

    The free boundary $S^*(\tau)$ is the curve separating these two regions. The viscosity formulation determines both the solution and the free boundary simultaneously, without requiring explicit tracking of $S^*(\tau)$.

---

**Exercise 5.** The digital call payoff $\Phi(S) = \mathbf{1}_{S > K}$ is discontinuous. The USC and LSC envelopes at $S = K$ are $\Phi^*(K) = 1$ and $\Phi_*(K) = 0$. Explain why the viscosity framework handles this discontinuity while the classical framework cannot.

??? success "Solution to Exercise 5"
    The digital call payoff is $\Phi(S) = \mathbf{1}_{S > K}$, which has a jump discontinuity at $S = K$: $\Phi(K^-) = 0$ and $\Phi(K^+) = 1$, with $\Phi(K)$ undefined or arbitrarily chosen.

    The **USC envelope** is $\Phi^*(K) = \limsup_{S \to K} \Phi(S) = 1$ (taking the larger value at the discontinuity).

    The **LSC envelope** is $\Phi_*(K) = \liminf_{S \to K} \Phi(S) = 0$ (taking the smaller value).

    The classical framework requires the terminal data to be continuous (or at least the solution to be $C^2$ in the interior and continuous up to the boundary). With a discontinuous payoff, even defining what "boundary condition" means is problematic: the PDE solution depends on the value assigned at $S = K$, and there is no canonical classical choice.

    The viscosity framework handles this naturally through the semicontinuity structure:

    - The **viscosity subsolution** uses the USC envelope $\Phi^*$ as terminal data. This gives the largest candidate subsolution, providing an upper bound on the price.
    - The **viscosity supersolution** uses the LSC envelope $\Phi_*$ as terminal data. This gives the smallest candidate supersolution, providing a lower bound.
    - The comparison principle then forces the subsolution to lie below the supersolution, and if both limits agree for $t < T$ (which they do, because the heat equation immediately smooths the data), the viscosity solution is unique.

    The resulting price at any time $t < T$ is the Black-Scholes digital call price $e^{-r(T-t)} N(d_2)$, which is smooth and uniquely determined. The viscosity framework bypasses the discontinuity by never requiring pointwise evaluation of the payoff at $S = K$; instead, the semicontinuous envelopes provide the correct one-sided boundary conditions that produce the unique no-arbitrage price.

---

**Exercise 6.** The Barles-Souganidis theorem requires monotonicity, stability, and consistency for convergence to the viscosity solution. Explain the practical implication for a financial engineer implementing an FDM solver: what specific design choices (regarding stencil coefficients, CFL condition, and time stepping) ensure that the numerical solution converges to the correct option price?

??? success "Solution to Exercise 6"
    The Barles-Souganidis theorem requires **monotonicity**, **stability**, and **consistency**. For a financial engineer implementing an FDM solver, these translate to the following concrete design choices:

    **Stencil coefficients (monotonicity)**: All coefficients in the finite difference stencil must be non-negative. For the Black-Scholes PDE on a uniform grid, the standard central difference discretization of $rSV_S$ produces coefficients $a_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \frac{rS_j}{\Delta S}\right)$ and $c_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + \frac{rS_j}{\Delta S}\right)$. The coefficient $a_j$ can become negative when $rS_j/\Delta S > \sigma^2 S_j^2/(\Delta S)^2$, i.e., when convection dominates diffusion. The remedy is **upwind differencing**: use a one-sided difference for $V_S$ in the direction of the drift, ensuring $a_j \geq 0$.

    **CFL condition (monotonicity + stability)**: For explicit schemes, the time step must satisfy

    $$
    \Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
    $$

    This ensures the central coefficient $b_j = 1 - a_j - c_j \geq 0$, completing the non-negativity requirement. Violating this produces negative coefficients, destroying monotonicity and potentially causing oscillations.

    **Time stepping (monotonicity)**: The fully implicit scheme is unconditionally monotone (the inverse of an M-matrix has non-negative entries) and requires no CFL restriction. Crank-Nicolson is **not** monotone and should be avoided near non-smooth data. The recommended approach is **Rannacher time-stepping**: use 2--4 fully implicit half-steps at the start (to damp high-frequency errors from the payoff kink), then switch to Crank-Nicolson for efficiency. This achieves effectively second-order accuracy while maintaining monotonicity where it matters most.

    These choices ensure all three Barles-Souganidis conditions are satisfied, guaranteeing that the computed prices converge to the correct viscosity solution --- particularly important for American options and barrier options where non-smooth data is unavoidable.
