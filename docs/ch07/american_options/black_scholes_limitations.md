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

### The Free Boundary S^*(t)

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

---

## Exercises

**Exercise 1.** Explain why the Black-Scholes formula cannot be applied directly to American options. Specifically, identify which step in the Black-Scholes derivation (construction of the hedged portfolio, Ito's lemma, no-arbitrage condition, or solving the PDE) breaks down when early exercise is possible.

??? success "Solution to Exercise 1"
    The Black-Scholes derivation proceeds through several steps, and it is the **solving the PDE** step that breaks down for American options.

    1. **Construction of the hedged portfolio:** Form $\Pi = V - \Delta S$ with $\Delta = \partial V / \partial S$. This step is unchanged for American options; we can still construct a delta-hedged portfolio.

    2. **Application of Ito's lemma:** Ito's lemma applied to $V(S, t)$ gives $dV = V_t \, dt + V_S \, dS + \frac{1}{2}V_{SS}(dS)^2$. This holds wherever $V$ is twice differentiable, which is true in the continuation region. However, $V$ is only $C^1$ (not $C^2$) at the free boundary $S^*(t)$, so Ito's lemma must be applied more carefully.

    3. **No-arbitrage condition:** Setting $d\Pi = r\Pi \, dt$ yields the Black-Scholes PDE $V_t + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$. For American options, this PDE holds only in the **continuation region** $\{S > S^*(t)\}$ (for a put), not everywhere.

    4. **Solving the PDE (the breakdown):** For European options, the PDE is solved on the fixed domain $(0, \infty) \times [0, T)$ with the terminal condition $V(S, T) = \Phi(S)$ and boundary conditions at $S = 0$ and $S \to \infty$. The solution uses the heat equation transformation and yields the Black-Scholes formula.

    For American options, the domain of the PDE is $\{(S, t) : S > S^*(t), \, 0 \leq t < T\}$, where $S^*(t)$ is unknown. The free boundary $S^*(t)$ must be found simultaneously with $V$. This couples the PDE solution to the boundary determination, creating a **free-boundary problem** that cannot be solved by the standard Feynman-Kac / heat equation approach. The additional constraint $V(S, t) \geq \Phi(S)$ and the smooth-pasting conditions at $S^*(t)$ have no analog in the European case.

---


**Exercise 2.** For the perpetual American put ($T = \infty$), the PDE becomes time-independent: $\frac{1}{2}\sigma^2 S^2 V'' + rSV' - rV = 0$ for $S > S^*$. Solve this ODE with boundary conditions $V(S^*) = K - S^*$, $V'(S^*) = -1$ (smooth pasting), and $V(\infty) = 0$. Find $S^*$ and the perpetual put price.

??? success "Solution to Exercise 2"
    For $T = \infty$, the put price depends only on $S$ (not $t$), so $V_t = 0$ and the PDE becomes the ODE:

    $$
    \frac{1}{2}\sigma^2 S^2 V''(S) + rSV'(S) - rV(S) = 0, \quad S > S^*
    $$

    This is a Cauchy-Euler equation. Try $V(S) = S^\gamma$:

    $$
    \frac{1}{2}\sigma^2 \gamma(\gamma - 1) + r\gamma - r = 0
    $$

    $$
    \frac{1}{2}\sigma^2 \gamma^2 + \left(r - \frac{1}{2}\sigma^2\right)\gamma - r = 0
    $$

    The roots are:

    $$
    \gamma = \frac{-(r - \sigma^2/2) \pm \sqrt{(r - \sigma^2/2)^2 + 2\sigma^2 r}}{\sigma^2}
    $$

    One root is $\gamma_1 > 0$ and the other is $\gamma_2 < 0$. Since $V(\infty) = 0$, we need $\gamma < 0$, so:

    $$
    V(S) = A S^{\gamma_2}, \quad \gamma_2 = \frac{-(r - \sigma^2/2) - \sqrt{(r - \sigma^2/2)^2 + 2\sigma^2 r}}{\sigma^2}
    $$

    Let $\lambda = -\gamma_2 > 0$, so $V(S) = A S^{-\lambda}$.

    **Applying boundary conditions at $S^*$:**

    Value-matching: $A (S^*)^{-\lambda} = K - S^*$

    Smooth-pasting: $-\lambda A (S^*)^{-\lambda - 1} = -1$, which gives $A = \frac{(S^*)^{\lambda + 1}}{\lambda}$.

    Substituting into value-matching:

    $$
    \frac{(S^*)^{\lambda+1}}{\lambda} \cdot (S^*)^{-\lambda} = K - S^* \implies \frac{S^*}{\lambda} = K - S^* \implies S^*\left(1 + \frac{1}{\lambda}\right) = K
    $$

    $$
    S^* = \frac{\lambda K}{\lambda + 1}
    $$

    The perpetual American put price for $S > S^*$ is:

    $$
    V(S) = (K - S^*)\left(\frac{S}{S^*}\right)^{-\lambda} = \frac{K}{\lambda + 1}\left(\frac{S(\lambda + 1)}{\lambda K}\right)^{-\lambda}
    $$

    where $\lambda = \frac{2r}{\sigma^2}$ (using the simplified form when $r - \sigma^2/2$ simplifies; more precisely, $\lambda = -\gamma_2$ from the quadratic above).

---


**Exercise 3.** The free boundary $S^*(t)$ for an American put satisfies $S^*(T) = K$ at maturity. As $t$ decreases from $T$, does $S^*$ increase or decrease? Provide an economic argument for the direction of $S^*(t)$ and sketch the free boundary qualitatively.

??? success "Solution to Exercise 3"
    At maturity, $S^*(T) = K$: exercise whenever the put is in the money.

    As $t$ decreases from $T$ (i.e., as time to maturity increases), $S^*(t)$ **decreases**. Equivalently, the exercise boundary moves to the left (lower stock prices).

    **Economic argument:** With more time remaining until maturity:

    - The option has greater **time value** (more chance for favorable stock movements).
    - The holder needs stronger incentive to give up this time value by exercising.
    - Therefore, the stock price must be lower (the put must be deeper in the money) to justify exercise.

    Conversely, as maturity approaches ($t \to T$):

    - Time value diminishes, so the cost of exercising early decreases.
    - Even a moderately in-the-money put should be exercised because little time value remains.
    - The boundary rises toward $K$.

    **Qualitative sketch:** $S^*(t)$ is a monotonically increasing curve from some value $S^*(0) < K$ on the left to $S^*(T) = K$ on the right. The curve is concave, rising steeply near maturity. For large time to maturity, $S^*(t)$ approaches the perpetual boundary $S^*_\infty = \frac{\lambda}{\lambda+1}K$ where $\lambda = 2r/\sigma^2$.

---


**Exercise 4.** Compare the domains of the PDE for a European put (the entire half-plane $S > 0$, $t < T$) and an American put (the continuation region $S > S^*(t)$, $t < T$). Explain why the unknown boundary $S^*(t)$ makes the American problem fundamentally harder.

??? success "Solution to Exercise 4"
    **European PDE domain:** The Black-Scholes PDE holds on the entire half-plane $\{(S, t) : S > 0, \, 0 \leq t < T\}$. The boundary conditions are:

    - Terminal: $V(S, T) = (K - S)^+$
    - $V(0, t) = Ke^{-r(T-t)}$ (put value when $S = 0$)
    - $V(S, t) \to 0$ as $S \to \infty$

    The domain and all boundary conditions are known a priori, so the PDE can be solved directly (via heat equation transformation or Feynman-Kac).

    **American PDE domain:** The PDE holds only in the continuation region $\{(S, t) : S > S^*(t), \, 0 \leq t < T\}$. The boundary conditions are:

    - Terminal: $V(S, T) = (K - S)^+$
    - At the free boundary: $V(S^*(t), t) = K - S^*(t)$ and $V_S(S^*(t), t) = -1$
    - $V(S, t) \to 0$ as $S \to \infty$

    **Why the unknown boundary makes the problem harder:**

    1. The PDE domain itself is part of the unknown, creating a **coupled problem**: you need $S^*(t)$ to define the domain, but you need to solve the PDE to find $S^*(t)$.

    2. Standard solution techniques (Green's function, Fourier transform, Feynman-Kac) require a known domain. The free boundary invalidates these approaches.

    3. Numerically, the free boundary must be tracked or approximated at each time step, adding an inner loop (e.g., Newton iteration or PSOR) to the standard time-stepping algorithm.

    4. The smooth-pasting condition $V_S(S^*, t) = -1$ is an additional constraint that determines $S^*(t)$, but it involves the derivative of the solution at a point that is itself unknown.

---


**Exercise 5.** Barone-Adesi and Whaley (1987) proposed an analytical approximation for the American put. The key idea is to decompose $V_{\text{Am}} = V_{\text{Eu}} + \epsilon(S,t)$ and approximate $\epsilon$. Describe the advantage of this decomposition approach over solving the free-boundary problem directly, and discuss its accuracy limitations for long-dated options.

??? success "Solution to Exercise 5"
    **The decomposition approach:** Write $V_{\text{Am}}(S, t) = V_{\text{Eu}}(S, t) + \epsilon(S, t)$, where $\epsilon$ is the early exercise premium. The European price $V_{\text{Eu}}$ is known analytically, so the problem reduces to finding $\epsilon$.

    **Advantages over solving the free-boundary problem directly:**

    1. **The European part is exact:** $V_{\text{Eu}}$ is computed via Black-Scholes with no approximation error. Only $\epsilon$ needs to be approximated.

    2. **$\epsilon$ is smoother and smaller:** The early exercise premium $\epsilon$ is a smooth, non-negative function that is typically much smaller than $V_{\text{Am}}$ itself. Approximating a small correction is easier than approximating the full solution.

    3. **Simplified PDE for $\epsilon$:** Substituting the decomposition into the variational inequality and using the fact that $V_{\text{Eu}}$ satisfies the Black-Scholes PDE yields a simpler equation for $\epsilon$. Barone-Adesi and Whaley further approximate this by dropping the time derivative term $\epsilon_t$, reducing the PDE to an ODE that can be solved analytically.

    4. **Speed:** The resulting approximation requires only evaluation of the Black-Scholes formula plus a small correction, making it orders of magnitude faster than numerical methods.

    **Accuracy limitations for long-dated options:** The approximation drops $\epsilon_t$ by assuming it is small relative to other terms. This is valid when $T$ is small (the premium changes slowly with time). For long-dated options:

    - The early exercise premium has significant time dependence, so $\epsilon_t$ is not negligible.
    - The approximation can underestimate the true American price by several percent for $T > 1$--$2$ years.
    - The error increases with volatility and interest rate, both of which amplify the early exercise premium.
    - For very long maturities, the error is bounded by the difference between the finite-maturity and perpetual American prices, but it can be practically significant for pricing and hedging.
