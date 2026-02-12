# Black–Scholes and the Early Exercise Problem

## Introduction

The Black–Scholes formula provides a closed-form solution for European options under specific assumptions. However, the model **cannot directly handle American options** because early exercise introduces a **free boundary** that fundamentally changes the mathematical structure of the problem.

This section explains precisely why the analytical framework breaks down and how the problem transforms from a standard PDE to a **free-boundary PDE** (variational inequality).

!!! info "Prerequisites"
    - [Black–Scholes PDE](../../ch06/bs_pde_derivation/delta_hedging.md) (derivation and structure)
    - [Terminal and Boundary Conditions](../../ch06/bs_pde_structure/terminal_and_boundary_conditions.md) (PDE boundary conditions)
    - [American Option Definition](american_option_definition.md) (optimal stopping formulation)
    - [Free Boundary Problems](../../ch08/american_options/free_boundary_problems_american_options.md) (variational inequality)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Explain why Black–Scholes boundary conditions are insufficient for American options
    2. Formulate the free-boundary PDE for American options
    3. State the smooth-pasting conditions
    4. Describe the complementarity problem

---

## The European Case: Fixed Boundary

For a European option, the Black–Scholes PDE:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0
$$

is solved on the domain $(S, t) \in (0, \infty) \times [0, T)$ with a **fixed terminal condition**:

$$
V(S, T) = \Phi(S)
$$

and boundary conditions at $S = 0$ and $S \to \infty$. The domain is fully specified, and the problem admits a unique closed-form solution via the Feynman–Kac representation.

---

## The American Case: Free Boundary

For an American option, the constraint $V(S, t) \geq \Phi(S)$ must hold for all $(S, t)$. This creates **two regions** with an unknown boundary between them.

### The Two Regions

1. **Continuation region** $\mathcal{C} = \{(S, t) : V(S, t) > \Phi(S)\}$
    - The PDE holds: $\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0$
    - The holder should keep the option

2. **Exercise (stopping) region** $\mathcal{E} = \{(S, t) : V(S, t) = \Phi(S)\}$
    - The option is worth exactly its intrinsic value
    - The holder should exercise immediately

### The Free Boundary $S^*(t)$

The boundary between $\mathcal{C}$ and $\mathcal{E}$ is an **unknown curve** $S^*(t)$ that must be determined as part of the solution:

$$
\boxed{
\begin{aligned}
\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0 &\quad \text{for } S > S^*(t) \text{ (put)} \\
V(S, t) = K - S &\quad \text{for } S \leq S^*(t) \text{ (put)}
\end{aligned}
}
$$

This is fundamentally different from the European case: the **domain of the PDE itself depends on the solution**.

---

## Smooth-Pasting Conditions

At the free boundary, the solution satisfies two conditions that together determine $S^*(t)$:

$$
\boxed{
V(t, S^*(t)) = \Phi(S^*(t)), \qquad \frac{\partial V}{\partial S}(t, S^*(t)) = \Phi'(S^*(t))
}
$$

For an American put with $\Phi(S) = (K - S)^+$:

$$
V(t, S^*) = K - S^*, \qquad V_S(t, S^*) = -1
$$

The **value-matching** condition (first equation) requires continuity. The **smooth-pasting** condition (second equation) requires differentiability at the boundary. Together, they provide the extra equation needed to determine the unknown $S^*(t)$.

!!! note "Why Smooth Pasting?"
    If $V_S$ were discontinuous at $S^*$, the holder could profit from an infinitesimal change in $S$ around the boundary. Smooth pasting is a consequence of the optimality of $S^*(t)$ and can be derived from the principle of **optimality in variational problems**.

---

## The Complementarity Formulation

The free-boundary problem can be restated compactly as a **linear complementarity problem (LCP)**:

$$
\boxed{
\begin{aligned}
V(S, t) &\geq \Phi(S) \\
-\frac{\partial V}{\partial t} - \mathcal{L}V + rV &\geq 0 \\
\left(V - \Phi\right) \cdot \left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV\right) &= 0
\end{aligned}
}
$$

The third equation is the **complementarity condition**: at every point, **at least one** of the two inequalities holds as an equality.

- In $\mathcal{C}$: $V > \Phi$ and the PDE holds ($= 0$)
- In $\mathcal{E}$: $V = \Phi$ and the PDE residual is $\geq 0$

This is equivalent to the variational inequality:

$$
\min\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV, \; V - \Phi\right) = 0
$$

---

## Why No Closed-Form Solution Exists

The Black–Scholes formula relies on:

1. **Known boundary**: The domain is $(0, \infty) \times [0, T]$ with conditions only at $S = 0$, $S \to \infty$, and $t = T$
2. **Linear PDE**: Solved by the heat equation transformation
3. **Feynman–Kac**: Direct probabilistic representation as an expectation

For American options, each of these breaks down:

| Feature | European | American |
|---|---|---|
| Domain | Fixed: $(0, \infty) \times [0, T]$ | Unknown: depends on $S^*(t)$ |
| PDE type | Standard linear PDE | Free-boundary PDE / variational inequality |
| Boundary | Terminal condition only | Terminal + unknown free boundary |
| Probabilistic form | Expectation | Supremum over stopping times |
| Solution | Closed-form | No general closed form |

!!! warning "The Perpetual Exception"
    For a **perpetual American put** ($T = \infty$), the problem becomes time-independent. The exercise boundary is a **constant** $S^*$, and a closed-form solution exists:
    
    $$
    V(S) = \left(\frac{S^*}{S}\right)^\lambda (K - S^*), \quad S^* = \frac{\lambda}{\lambda + 1} K
    $$
    
    where $\lambda = \frac{2r}{\sigma^2}$. This is the only analytically tractable case.

---

## Numerical Approaches

Since closed-form solutions are unavailable, American options require numerical methods:

| Method | Approach | See Also |
|---|---|---|
| Binomial/trinomial trees | Backward induction with $\max$ | [Binomial Pricing](binomial_pricing.md) |
| Finite differences + projection | Discretize PDE, enforce constraint | [American Options Implementation](../../ch08/american_options/american_options_early_exercise_implementation.md) |
| Penalty methods | Soft constraint via large penalty | [Penalty and FD Methods](penalty_and_finite_difference.md) |
| LSM Monte Carlo | Regression-based optimal stopping | [LSM Monte Carlo](lsm_monte_carlo.md) |

---

## Summary

$$
\boxed{
\text{European: standard PDE} \quad \longrightarrow \quad \text{American: free-boundary PDE}
}
$$

| Aspect | European | American |
|---|---|---|
| Mathematical structure | Linear PDE with fixed boundary | Variational inequality with free boundary |
| Domain | Known a priori | Unknown, part of the solution |
| Analytical solution | Closed-form (Black–Scholes) | None in general |
| Required methods | Formula evaluation | Numerical: trees, FD, Monte Carlo |

**The early-exercise feature transforms the pricing problem from a solvable boundary-value problem into a free-boundary problem that, except for perpetual options, requires numerical methods.**
