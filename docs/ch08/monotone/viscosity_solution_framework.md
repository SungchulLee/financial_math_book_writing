# Viscosity Solution Framework

When the PDE lacks smooth solutions --- due to degenerate diffusion, non-smooth boundary data, or obstacle constraints --- classical solution theory breaks down. Viscosity solutions provide the correct weak solution concept for these problems, replacing pointwise PDE satisfaction with inequalities tested against smooth touching functions.

---

## Why Classical Solutions Fail

### The Black-Scholes PDE at S = 0

The Black-Scholes PDE:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

has diffusion coefficient $\frac{1}{2}\sigma^2 S^2$, which **degenerates** (vanishes) at $S = 0$. At this boundary, the PDE reduces to:

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

The American option value satisfies:

$$
\min(-u_\tau + \mathcal{L}u,\; u - \Phi) = 0
$$

In viscosity sense:

- **Subsolution**: At any local max of $u - \varphi$, either $-\varphi_\tau + \mathcal{L}\varphi \leq 0$ or $u \leq \Phi$
- **Supersolution**: At any local min of $u - \varphi$, either $-\varphi_\tau + \mathcal{L}\varphi \geq 0$ or $u \geq \Phi$

This encodes the free boundary problem without explicitly tracking the boundary $S^*(t)$.

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
