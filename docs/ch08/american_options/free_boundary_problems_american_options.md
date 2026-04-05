# Free Boundary Problems and American Options

American options can be exercised at any time before expiration, leading to an **optimal stopping problem**. Numerically, this becomes a **free boundary problem** or equivalently a **variational inequality** (obstacle problem).

---

## The American Option Problem

### Optimal Stopping Formulation

Under risk-neutral dynamics $dS_t = rS_t\,dt + \sigma S_t\,dW_t$:

$$
\boxed{
V(t,S) = \sup_{\tau \in \mathcal{T}_{t,T}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r(\tau-t)}\Phi(S_\tau) \mid S_t = S\right]
}
$$

where $\mathcal{T}_{t,T}$ is the set of stopping times in $[t,T]$.

### The Variational Inequality

The American option price satisfies:

$$
\boxed{
\min\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV, \; V - \Phi\right) = 0
}
$$

where $\mathcal{L}V = \frac{1}{2}\sigma^2 S^2 V_{SS} + rS V_S$ is the Black-Scholes generator.

### Two Regions

1. **Continuation region** $\mathcal{C}$: $V > \Phi$, and the PDE holds:

   $$\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0$$

2. **Exercise region** $\mathcal{E}$: $V = \Phi$ (immediate exercise is optimal)

---

## The Free Boundary

### Definition

The **exercise boundary** $S^*(t)$ separates the two regions:

- **American put**: $\mathcal{E} = \{S < S^*(t)\}$
- **American call (no dividends)**: Never optimal to exercise early ($S^* = \infty$)
- **American call (with dividends)**: $\mathcal{E} = \{S > S^*(t)\}$

### Smooth Pasting Conditions

At the free boundary $S = S^*(t)$:

$$
\boxed{
V(t, S^*(t)) = \Phi(S^*(t)), \quad \frac{\partial V}{\partial S}(t, S^*(t)) = \Phi'(S^*(t))
}
$$

For an American put with $\Phi(S) = (K-S)^+$:

$$
V(t, S^*) = K - S^*, \quad V_S(t, S^*) = -1
$$

### Early Exercise Premium

$$
V_{\text{American}} = V_{\text{European}} + \text{Early Exercise Premium}
$$

The premium is always non-negative and reflects the value of the exercise option.

---

## Numerical Methods: Projection

### Simple Projection Method

After each time step, **project** onto the constraint:

$$
\boxed{
u_j^{n+1} \leftarrow \max(u_j^{n+1}, \Phi_j)
}
$$

### Algorithm (Implicit + Projection)

```
1. Solve (I - Δτ A)ũ^{n+1} = u^n  (unconstrained)
2. Project: u_j^{n+1} = max(ũ_j^{n+1}, Φ_j) for all j
3. Repeat for next time step
```

### Issues

- Simple but may lose accuracy near the free boundary
- First-order in time (even with Crank-Nicolson base scheme)
- Smooth pasting not explicitly enforced

---

## Linear Complementarity Problem (LCP)

### Formulation

The discrete problem at each time step is:

$$
\boxed{
\begin{aligned}
& L\mathbf{u} \geq \mathbf{f} \\
& \mathbf{u} \geq \boldsymbol{\Phi} \\
& (L\mathbf{u} - \mathbf{f})^T(\mathbf{u} - \boldsymbol{\Phi}) = 0
\end{aligned}
}
$$

where $L = I - \Delta\tau A$ and $\mathbf{f} = \mathbf{u}^n$.

### Interpretation

- Either $u_j > \Phi_j$ (continuation) and the PDE holds: $(L\mathbf{u})_j = f_j$
- Or $u_j = \Phi_j$ (exercise) and the constraint binds

---

## PSOR Algorithm

The **Projected Successive Over-Relaxation (PSOR)** method solves the LCP efficiently.

### Algorithm

For iteration $k+1$:

$$
\tilde{u}_j^{(k+1)} = (1-\omega)u_j^{(k)} + \frac{\omega}{l_{jj}}\left(f_j - \sum_{i<j} l_{ji}u_i^{(k+1)} - \sum_{i>j} l_{ji}u_i^{(k)}\right)
$$

$$
u_j^{(k+1)} = \max(\tilde{u}_j^{(k+1)}, \Phi_j)
$$

### Parameters

- $\omega \in (1, 2)$: over-relaxation parameter (typically $\omega \approx 1.2$)
- Converges when $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\| < \epsilon$

### Convergence

- Linear convergence rate
- Typically 5-20 iterations per time step
- Total cost: $O(MN \cdot \text{iterations})$

---

## Penalty Method

### Idea

Replace the hard constraint with a soft penalty:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - rV + \rho(V - \Phi)^- = 0
$$

where $(x)^- = \min(x, 0)$ and $\rho \gg 1$ is the penalty parameter.

### Discrete Form

$$
(I - \Delta\tau A + \Delta\tau \rho P)\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta\tau \rho P\boldsymbol{\Phi}
$$

where $P$ is a diagonal matrix with $P_{jj} = 1$ if $u_j < \Phi_j$, else $0$.

### Properties

- Smooth formulation (no explicit constraint)
- Easy to implement with existing solvers
- Error $\sim O(1/\rho)$ from penalty approximation
- Typically $\rho = 10^6$ to $10^8$

---

## Brennan-Schwartz Algorithm

For American puts specifically, there's an elegant direct method.

### Key Observation

The exercise boundary $S^*(t)$ increases as $t \to T$ (from below).

### Algorithm

Work backward from maturity:
1. Find the grid point where exercise first becomes optimal
2. Set $u_j = \Phi_j$ for $j \leq j^*$
3. Solve PDE only for $j > j^*$

### Advantage

No iteration required—direct solve at each time step.

---

## Front-Fixing Methods

Transform coordinates to fix the free boundary.

### Coordinate Transform

Let $\xi = S/S^*(t)$ so that the boundary is always at $\xi = 1$.

### Transformed PDE

Additional terms appear involving $\dot{S}^*$, which must be determined as part of the solution.

### Advantage

High accuracy near the free boundary.

### Disadvantage

More complex implementation; boundary must be tracked.

---

## Convergence and Accuracy

### Order of Convergence

| Method | Time Order | Space Order |
|--------|------------|-------------|
| Projection + Implicit | 1 | 2 |
| PSOR + C-N | 1-1.5 | 2 |
| Penalty | 1 | 2 |
| Front-fixing | 2 | 2 |

**Note**: The free boundary introduces non-smoothness that typically limits time accuracy to first-order.

### Grid Considerations

- Place grid points near expected $S^*$
- Adaptive grids can improve efficiency
- Smoothing at maturity helps (Rannacher)

---

## Comparison of Methods

| Method | Ease | Accuracy | Speed |
|--------|------|----------|-------|
| Projection | Easy | Low | Fast |
| PSOR | Moderate | Good | Moderate |
| Penalty | Easy | Good | Fast |
| Front-fixing | Hard | High | Moderate |

---

## Summary

$$
\boxed{
\min\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV, \; V - \Phi\right) = 0
}
$$

| Aspect | Description |
|--------|-------------|
| Problem type | Free boundary / obstacle problem |
| Constraint | $V \geq \Phi$ (can exercise anytime) |
| Free boundary | $S^*(t)$ separates exercise/continuation |
| Smooth pasting | $V$ and $V_S$ continuous at boundary |

| Method | Key Idea |
|--------|----------|
| Projection | Enforce $u \geq \Phi$ after each step |
| PSOR | Iteratively solve LCP |
| Penalty | Soft constraint via large $\rho$ |
| Front-fixing | Track boundary explicitly |

**American option pricing requires specialized numerical techniques to handle the free boundary between continuation and exercise regions.**

---

## Exercises

**Exercise 1.** For an American put with $K = 100$, $r = 0.05$, $\sigma = 0.20$, explain why the exercise boundary $S^*(t)$ satisfies $S^*(t) < K$ for $t < T$ and $S^*(T) = K$. Why is early exercise never optimal for an American call on a non-dividend-paying stock?

??? success "Solution to Exercise 1"
    **Why $S^*(t) < K$ for $t < T$:**

    At the exercise boundary $S^*(t)$, the holder exercises the put and receives $K - S^*(t)$. If $S^*(t) = K$, the exercise payoff would be zero, so there would be no reason to exercise. Hence $S^*(t) < K$.

    More precisely, the holder exercises when the expected gain from holding (continuation value) equals the intrinsic value. Since $r > 0$, holding the put when the stock is very low ties up the option and delays receiving the strike cash $K$. The interest lost on $K$ makes early exercise optimal once $S$ falls below some critical level $S^*(t)$ that is strictly less than $K$.

    **Why $S^*(T) = K$:**

    At expiration, the put is exercised whenever $S < K$ (the payoff $(K-S)^+$ is positive). There is no remaining time value, so $S^*(T) = K$.

    **Why early exercise of an American call on a non-dividend-paying stock is never optimal:**

    For a non-dividend-paying stock, the European call price satisfies $C_E \geq S - Ke^{-r(T-t)}$. Since $e^{-r(T-t)} < 1$ for $t < T$, we have

    $$
    C_E \geq S - Ke^{-r(T-t)} > S - K = \Phi(S)
    $$

    for in-the-money options. The call value always exceeds the immediate exercise payoff, so early exercise is never optimal. Intuitively, exercising early means paying $K$ now rather than later, forfeiting interest on $K$, and there are no dividends to offset this cost.

---

**Exercise 2.** State the smooth pasting conditions at the free boundary $S = S^*(t)$ for an American put. Explain geometrically why both $V(t, S^*) = K - S^*$ and $V_S(t, S^*) = -1$ must hold simultaneously.

??? success "Solution to Exercise 2"
    The smooth pasting conditions at $S = S^*(t)$ for an American put with payoff $\Phi(S) = (K - S)^+$ are:

    **Value matching:** $V(t, S^*(t)) = K - S^*(t)$

    **Slope matching:** $V_S(t, S^*(t)) = -1$

    **Geometric interpretation:**

    The value matching condition says that the option value curve meets the intrinsic value line $K - S$ at the boundary. This is simply the requirement that the option value is continuous.

    The slope matching condition ($V_S = -1$) requires that the option value curve is *tangent* to the intrinsic value line at the boundary. Geometrically, the option value curve "kisses" the payoff line from above rather than meeting it at a corner.

    If the slope were discontinuous (say $V_S(t, S^{*+}) \neq -1$), then a small perturbation of the boundary location would either increase the option value (contradicting optimality) or create an arbitrage opportunity. Specifically:

    - If $|V_S| < 1$ at the boundary, the holder could improve the stopping strategy by exercising slightly earlier (lower $S^*$).
    - If $|V_S| > 1$ at the boundary, the holder could improve by exercising slightly later (higher $S^*$).

    The optimal boundary is the one where no local improvement is possible, which requires the tangency condition.

---

**Exercise 3.** The simple projection method enforces $u_j^{n+1} \leftarrow \max(u_j^{n+1}, \Phi_j)$ after each time step. Suppose at a given time step, the unconstrained implicit solve yields $\tilde{u} = (48, 12, 3, 0.5)^T$ on a grid with $S = (40, 80, 120, 160)$ and the put payoff is $\Phi = (60, 20, 0, 0)^T$. Apply the projection and identify the exercise and continuation regions.

??? success "Solution to Exercise 3"
    Given the unconstrained solution $\tilde{u} = (48, 12, 3, 0.5)^T$ on the grid $S = (40, 80, 120, 160)$ and put payoff $\Phi = (60, 20, 0, 0)^T$:

    Apply projection $u_j = \max(\tilde{u}_j, \Phi_j)$ componentwise:

    - $j = 1$: $u_1 = \max(48, 60) = 60$ (constraint active)
    - $j = 2$: $u_2 = \max(12, 20) = 20$ (constraint active)
    - $j = 3$: $u_3 = \max(3, 0) = 3$ (unconstrained)
    - $j = 4$: $u_4 = \max(0.5, 0) = 0.5$ (unconstrained)

    The projected solution is $\mathbf{u} = (60, 20, 3, 0.5)^T$.

    **Exercise region:** $\{S = 40, S = 80\}$ where $u_j = \Phi_j$ (the constraint binds and immediate exercise is optimal).

    **Continuation region:** $\{S = 120, S = 160\}$ where $u_j > \Phi_j$ (the PDE solution exceeds the payoff and holding is optimal).

    The free boundary lies between $S = 80$ and $S = 120$, which is consistent with the exercise boundary being below the strike $K = 100$.

---

**Exercise 4.** Write out the linear complementarity problem (LCP) for a single time step of the implicit scheme: $(I - \Delta\tau A)\mathbf{u}^{n+1} \geq \mathbf{u}^n$, $\mathbf{u}^{n+1} \geq \boldsymbol{\Phi}$, $(L\mathbf{u}^{n+1} - \mathbf{u}^n)^T(\mathbf{u}^{n+1} - \boldsymbol{\Phi}) = 0$. Explain the complementarity condition in terms of the exercise and continuation regions.

??? success "Solution to Exercise 4"
    The linear complementarity problem for a single time step with $L = I - \Delta\tau A$ (or more precisely $L = I + \Delta\tau A$ in the time-to-maturity formulation) is:

    **Condition 1 (PDE residual non-negative):**

    $$
    L\mathbf{u}^{n+1} - \mathbf{u}^n \geq \mathbf{0}
    $$

    This means the discrete PDE residual is non-negative at every grid point.

    **Condition 2 (Early exercise constraint):**

    $$
    \mathbf{u}^{n+1} \geq \boldsymbol{\Phi}
    $$

    The option value must be at or above the payoff at every grid point.

    **Condition 3 (Complementarity):**

    $$
    (L\mathbf{u}^{n+1} - \mathbf{u}^n)^T(\mathbf{u}^{n+1} - \boldsymbol{\Phi}) = 0
    $$

    **Interpretation:** The complementarity condition requires that for each grid point $j$, at least one of the two inequalities holds with equality:

    - **Continuation region** ($u_j^{n+1} > \Phi_j$): Since the factor $(u_j^{n+1} - \Phi_j) > 0$, the complementarity condition forces $(L\mathbf{u}^{n+1} - \mathbf{u}^n)_j = 0$. The discrete PDE is satisfied exactly. The option is worth more than immediate exercise, so the holder continues.

    - **Exercise region** ($u_j^{n+1} = \Phi_j$): The factor $(u_j^{n+1} - \Phi_j) = 0$, so the product is zero regardless of the residual. The PDE residual satisfies $(L\mathbf{u}^{n+1} - \mathbf{u}^n)_j \geq 0$, meaning the option would be "overpriced" by the PDE alone --- the continuation value is below the payoff, so exercising is optimal.

    The two conditions cannot simultaneously have strict inequality: we cannot have both $u_j > \Phi_j$ and $(L\mathbf{u})_j > q_j$, because the first implies the PDE holds with equality.

---

**Exercise 5.** The penalty method replaces the hard constraint with $\rho(V - \Phi)^-$ for large $\rho$. If $\rho = 10^6$, estimate the penalty approximation error. What value of $\rho$ would be needed to make the penalty error smaller than the discretization error on a grid with $\Delta S = 1$ and $\Delta\tau = 0.01$?

??? success "Solution to Exercise 5"
    **Penalty approximation error with $\rho = 10^6$:**

    The error bound is $|V - V^\rho| \leq C/\rho$, so for $\rho = 10^6$, the penalty error is of order $10^{-6}$ (times a constant $C$ that depends on the problem parameters). In dollar terms, this is negligible for option prices of order $\$1$-$\$100$.

    **Balancing penalty and discretization errors:**

    The discretization error for a second-order scheme in space and first-order in time (typical near the free boundary) is:

    $$
    E_{\text{disc}} \sim O(\Delta\tau) + O(\Delta S^2)
    $$

    With $\Delta S = 1$ and $\Delta\tau = 0.01$:

    $$
    E_{\text{disc}} \sim 0.01 + 1 = O(1)
    $$

    The dominant discretization error is $O(\Delta S^2) = O(1)$. To make the penalty error smaller:

    $$
    \frac{C}{\rho} < \Delta S^2 = 1
    $$

    So $\rho > C$ suffices. Even $\rho = 10^2$ would make the penalty error negligible relative to the spatial discretization error.

    However, for the time discretization error $O(\Delta\tau) = O(0.01)$, we need $\rho > C/0.01 = 100C$, so $\rho \approx 10^3$ to $10^4$ is sufficient (depending on the constant $C$, typically $C \sim O(1)$ to $O(10)$).

    In practice, $\rho = 10^4$ is more than adequate for this grid resolution.

---

**Exercise 6.** Compare the four methods for American option pricing (projection, PSOR, penalty, front-fixing) in terms of implementation complexity, accuracy near the free boundary, and computational cost per time step. Which method would you recommend for a production implementation pricing American puts on a single underlying?

??? success "Solution to Exercise 6"
    **Projection method:**

    - *Implementation*: Trivial --- solve the unconstrained system, then apply $u_j \leftarrow \max(u_j, \Phi_j)$.
    - *Accuracy*: Low near the free boundary due to splitting error (the PDE and constraint are enforced sequentially, not simultaneously).
    - *Cost*: One tridiagonal solve per time step (cheapest).

    **PSOR:**

    - *Implementation*: Moderate --- requires the LCP formulation, the sweep loop, and tuning of $\omega$.
    - *Accuracy*: Good --- solves the LCP exactly (to iteration tolerance), so the constraint and PDE are coupled.
    - *Cost*: 5-20 sweeps per time step, each costing $O(M)$. Total cost is moderate.

    **Penalty method:**

    - *Implementation*: Easy --- add a penalty term to the existing PDE solver and use Newton iteration.
    - *Accuracy*: Good --- error $O(1/\rho)$ from penalization, but no splitting error. With $\rho = 10^6$, the penalty error is negligible.
    - *Cost*: 2-4 Newton iterations per time step, each requiring one tridiagonal solve. Comparable to or slightly more than projection.

    **Front-fixing:**

    - *Implementation*: Hard --- requires a coordinate transformation, tracking the boundary $S^*(t)$, and solving the transformed PDE with additional terms.
    - *Accuracy*: High --- the free boundary is resolved exactly (by construction), and smooth pasting is enforced.
    - *Cost*: One PDE solve per time step plus boundary update. Moderate total cost.

    **Recommendation for production:** The **penalty method** offers the best balance of ease of implementation, accuracy, and speed for a single-asset American put. It integrates seamlessly into existing finite difference infrastructure, has negligible approximation error for reasonable $\rho$, and requires only a few Newton iterations. PSOR is a close second and is preferred if exact LCP solutions (without penalty approximation) are required.

---

**Exercise 7.** The early exercise premium is defined as $V_{\text{American}} - V_{\text{European}}$. For an at-the-money put with $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$, the European put price is approximately $\$5.57$. If a numerical solver gives an American put price of $\$6.08$, what is the early exercise premium? Is this magnitude reasonable?

??? success "Solution to Exercise 7"
    The early exercise premium is:

    $$
    V_{\text{American}} - V_{\text{European}} = \$6.08 - \$5.57 = \$0.51
    $$

    As a percentage of the European price:

    $$
    \frac{0.51}{5.57} \approx 9.2\%
    $$

    **Is this magnitude reasonable?**

    Yes, this is a reasonable magnitude. For an at-the-money put with these parameters:

    - The interest rate $r = 0.05$ creates an incentive for early exercise (receiving $K$ earlier earns interest).
    - The volatility $\sigma = 0.20$ creates an incentive to wait (the option might become more valuable).
    - For $T = 1$ year, the early exercise premium is typically 5-15% of the European price for moderate interest rates and volatilities.

    The premium of approximately 9% of the European price falls squarely within the expected range. As a rough check, the maximum possible early exercise premium for a put is bounded by the interest savings from receiving $K$ immediately:

    $$
    K(1 - e^{-rT}) = 100(1 - e^{-0.05}) \approx \$4.88
    $$

    The observed premium of $\$0.51$ is well below this upper bound, which is consistent since only deep in-the-money options would capture the full interest benefit.
