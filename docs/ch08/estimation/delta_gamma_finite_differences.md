# Delta and Gamma via Finite Differences

Delta ($\Delta$) and gamma ($\Gamma$) are the most important spatial Greeks for hedging. Finite difference methods provide two natural approaches for estimating them: direct extraction from the solution grid and the bump-and-revalue method. Each has distinct accuracy and cost characteristics.

---

## Definitions

**Delta** measures the sensitivity of the option price to the underlying asset price:

$$
\Delta = \frac{\partial V}{\partial S}
$$

**Gamma** measures the sensitivity of delta (equivalently, the convexity of the price):

$$
\Gamma = \frac{\partial^2 V}{\partial S^2}
$$

Both are evaluated at the current time $t = 0$ (equivalently, at $\tau = T$ in the time-to-maturity formulation) and at a specific asset price $S$.

---

## Direct Extraction from the FDM Grid

After solving the Black-Scholes PDE on a grid $(S_j, \tau_n)$, the option prices $V_j^N$ at $\tau = T$ (i.e., $t = 0$) are available at every spatial node. Delta and gamma can be estimated directly using finite difference formulas applied to this grid.

### Delta Estimates

**Central difference** (second-order accurate):

$$
\boxed{\Delta_j \approx \frac{V_{j+1}^N - V_{j-1}^N}{2\Delta S}}
$$

with truncation error $O((\Delta S)^2)$.

**Forward difference** (first-order, for left boundary $j = 0$):

$$
\Delta_0 \approx \frac{V_1^N - V_0^N}{\Delta S}
$$

**Backward difference** (first-order, for right boundary $j = M$):

$$
\Delta_M \approx \frac{V_M^N - V_{M-1}^N}{\Delta S}
$$

### Gamma Estimate

**Central second difference** (second-order accurate):

$$
\boxed{\Gamma_j \approx \frac{V_{j+1}^N - 2V_j^N + V_{j-1}^N}{(\Delta S)^2}}
$$

with truncation error $O((\Delta S)^2)$.

!!! tip "No Additional PDE Solves"
    Direct extraction requires no additional computation beyond the original PDE solve. Delta and gamma are byproducts of the existing solution grid.

---

## Truncation Error Analysis

### Delta (Central Difference)

Taylor-expanding $V(S \pm \Delta S)$ around $S_j$:

$$
V_{j+1} = V_j + V_S \Delta S + \frac{1}{2}V_{SS}(\Delta S)^2 + \frac{1}{6}V_{SSS}(\Delta S)^3 + O((\Delta S)^4)
$$

$$
V_{j-1} = V_j - V_S \Delta S + \frac{1}{2}V_{SS}(\Delta S)^2 - \frac{1}{6}V_{SSS}(\Delta S)^3 + O((\Delta S)^4)
$$

Subtracting:

$$
\frac{V_{j+1} - V_{j-1}}{2\Delta S} = V_S + \frac{1}{6}V_{SSS}(\Delta S)^2 + O((\Delta S)^4)
$$

The error is $O((\Delta S)^2)$, and the leading error term involves the third derivative $V_{SSS}$.

### Gamma (Central Second Difference)

Adding the Taylor expansions:

$$
\frac{V_{j+1} - 2V_j + V_{j-1}}{(\Delta S)^2} = V_{SS} + \frac{1}{12}V_{SSSS}(\Delta S)^2 + O((\Delta S)^4)
$$

The error is $O((\Delta S)^2)$, with the leading error term involving the fourth derivative $V_{SSSS}$.

### Convergence Rates

| Greek | Formula | Order | Leading error term |
|-------|---------|-------|--------------------|
| $\Delta$ (central) | $(V_{j+1} - V_{j-1}) / (2\Delta S)$ | $O((\Delta S)^2)$ | $\frac{1}{6}V_{SSS}(\Delta S)^2$ |
| $\Delta$ (forward) | $(V_{j+1} - V_j) / \Delta S$ | $O(\Delta S)$ | $\frac{1}{2}V_{SS}\Delta S$ |
| $\Gamma$ (central) | $(V_{j+1} - 2V_j + V_{j-1}) / (\Delta S)^2$ | $O((\Delta S)^2)$ | $\frac{1}{12}V_{SSSS}(\Delta S)^2$ |

---

## The Bump-and-Revalue Method

An alternative approach is to perturb the initial asset price and solve the PDE multiple times.

### Delta by Bumping

Solve the Black-Scholes PDE three times:

1. Base case: $V(S)$ at asset price $S$
2. Up bump: $V(S + \delta S)$ at perturbed price $S + \delta S$
3. Down bump: $V(S - \delta S)$ at perturbed price $S - \delta S$

**Central difference delta**:

$$
\Delta \approx \frac{V(S + \delta S) - V(S - \delta S)}{2\delta S}
$$

**Forward difference delta** (requires only two solves):

$$
\Delta \approx \frac{V(S + \delta S) - V(S)}{\delta S}
$$

### Gamma by Bumping

Using the same three PDE solutions:

$$
\Gamma \approx \frac{V(S + \delta S) - 2V(S) + V(S - \delta S)}{(\delta S)^2}
$$

!!! warning "Cost of Bumping"
    The bump-and-revalue method requires **two additional PDE solves** for delta (central) or **one additional solve** for delta (forward). For gamma, it requires two additional solves. This triples the computational cost compared to direct grid extraction.

---

## Bump-and-Revalue vs Direct Extraction

| Aspect | Direct extraction | Bump-and-revalue |
|--------|-------------------|-------------------|
| **Additional PDE solves** | 0 | 2 (for central $\Delta$ and $\Gamma$) |
| **Accuracy** | Depends on grid spacing $\Delta S$ | Depends on bump size $\delta S$ |
| **Flexibility** | Limited to grid nodes | Any asset price $S$ |
| **Interpolation** | Needed for off-grid $S$ | Not needed |
| **For vega, rho** | Not applicable | Required |

**When to use which**:

- **Direct extraction**: Use for delta and gamma when the current asset price $S$ falls on or near a grid node. This is the default choice due to zero additional cost.
- **Bump-and-revalue**: Use when $S$ does not coincide with a grid node, or when computing Greeks with respect to parameters (vega, rho) rather than state variables.

---

## Grid Placement and the Strike

### The Problem

Option payoffs have a kink at $S = K$. Near the strike, delta changes rapidly and gamma has a peak. If the grid does not resolve this region well, Greek estimates suffer.

### Node at the Strike

Placing a grid node exactly at $S = K$ ensures that the delta and gamma estimates near the strike use the most accurate values. This is achieved by choosing $\Delta S$ such that $K / \Delta S$ is an integer.

### Staggered Grid

If $K$ falls between two nodes $S_j$ and $S_{j+1}$, the central difference for delta at the strike requires interpolation, introducing additional error. The gamma estimate is particularly sensitive because it involves a **second** difference that amplifies the payoff kink.

### Non-Uniform Grids

Concentrating grid points near $K$ while using coarser spacing far from the strike improves Greek accuracy without excessive computational cost. A common choice is a sinh or tanh stretching that clusters points near $K$.

---

## The Theta-Gamma-Delta Relation

The Black-Scholes PDE provides a consistency check for numerically computed Greeks. At any point $(t, S)$ where the PDE holds:

$$
\boxed{\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV}
$$

where $\Theta = \partial V / \partial t$.

### Using the PDE as a Check

After computing $\Delta$, $\Gamma$, and $\Theta$ from the grid:

$$
\text{Residual} = \Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma - rV
$$

This residual should be close to zero. A large residual indicates:

- Insufficient grid resolution
- Boundary condition contamination
- Implementation error

### Using the PDE to Compute Theta

Alternatively, if delta and gamma are computed accurately from the spatial grid, theta can be obtained from the PDE without using the time direction:

$$
\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
$$

This avoids the time-differencing error inherent in computing theta directly from two time levels.

---

## Higher-Order Formulas

### Fourth-Order Delta

Using a five-point stencil:

$$
\Delta_j \approx \frac{-V_{j+2} + 8V_{j+1} - 8V_{j-1} + V_{j-2}}{12\Delta S}
$$

with truncation error $O((\Delta S)^4)$.

### Fourth-Order Gamma

$$
\Gamma_j \approx \frac{-V_{j+2} + 16V_{j+1} - 30V_j + 16V_{j-1} - V_{j-2}}{12(\Delta S)^2}
$$

with truncation error $O((\Delta S)^4)$.

These require the solution at five neighboring nodes and cannot be used at nodes near the boundaries without modification. In practice, the improvement is significant only when the solution is smooth (i.e., away from the strike or after Rannacher smoothing).

---

## Convergence Behavior Near the Strike

For a European call with payoff $(S - K)^+$:

- **Away from the strike** ($|S - K| \gg \Delta S$): The solution is smooth, and delta and gamma converge at the expected second-order rate
- **At the strike** ($S = K$): The payoff kink reduces the convergence rate. Gamma near the strike converges at approximately $O((\Delta S)^{1/2})$ without smoothing

**Effect of Rannacher smoothing**: After 2-4 implicit time steps at the start, the solution is smoothed, and the convergence rate for gamma recovers to approximately $O((\Delta S)^{2})$ even near the strike.

| Scenario | Delta convergence | Gamma convergence |
|----------|-------------------|-------------------|
| Smooth region | $O((\Delta S)^2)$ | $O((\Delta S)^2)$ |
| At strike (no smoothing) | $O(\Delta S)$ | $O((\Delta S)^{1/2})$ |
| At strike (Rannacher) | $O((\Delta S)^2)$ | $O((\Delta S)^2)$ |

---

## Summary

$$
\boxed{
\Delta_j \approx \frac{V_{j+1} - V_{j-1}}{2\Delta S}, \qquad
\Gamma_j \approx \frac{V_{j+1} - 2V_j + V_{j-1}}{(\Delta S)^2}
}
$$

| Aspect | Recommendation |
|--------|---------------|
| **Method** | Direct extraction from FDM grid (zero additional cost) |
| **Formula** | Central differences (second-order accuracy) |
| **Grid** | Place a node at the strike $K$ |
| **Smoothing** | Rannacher time-stepping restores convergence near the strike |
| **Validation** | Check $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV$ |
| **Off-grid** | Use bump-and-revalue with interpolation |

Delta and gamma are the workhorses of delta-hedging. The finite difference grid provides them as a free byproduct of the pricing computation, making FDM an attractive framework for simultaneous pricing and hedging.

---

## Exercises

**Exercise 1.** Using the Taylor expansion of $V(S \pm \Delta S)$ around $S_j$, derive the central difference formula for delta and show that the truncation error is $\frac{1}{6}V_{SSS}(\Delta S)^2 + O((\Delta S)^4)$. Similarly derive the truncation error for the gamma formula.

??? success "Solution to Exercise 1"
    **Delta derivation.** Expand $V_{j+1} = V(S_j + \Delta S)$ and $V_{j-1} = V(S_j - \Delta S)$ around $S_j$:

    $$
    V_{j+1} = V_j + V_S \Delta S + \frac{1}{2}V_{SS}(\Delta S)^2 + \frac{1}{6}V_{SSS}(\Delta S)^3 + \frac{1}{24}V_{SSSS}(\Delta S)^4 + \cdots
    $$

    $$
    V_{j-1} = V_j - V_S \Delta S + \frac{1}{2}V_{SS}(\Delta S)^2 - \frac{1}{6}V_{SSS}(\Delta S)^3 + \frac{1}{24}V_{SSSS}(\Delta S)^4 - \cdots
    $$

    Subtracting the second from the first:

    $$
    V_{j+1} - V_{j-1} = 2V_S \Delta S + \frac{1}{3}V_{SSS}(\Delta S)^3 + O((\Delta S)^5)
    $$

    Dividing by $2\Delta S$:

    $$
    \frac{V_{j+1} - V_{j-1}}{2\Delta S} = V_S + \frac{1}{6}V_{SSS}(\Delta S)^2 + O((\Delta S)^4)
    $$

    The truncation error is $\frac{1}{6}V_{SSS}(\Delta S)^2 + O((\Delta S)^4)$.

    **Gamma derivation.** Adding the two Taylor expansions:

    $$
    V_{j+1} + V_{j-1} = 2V_j + V_{SS}(\Delta S)^2 + \frac{1}{12}V_{SSSS}(\Delta S)^4 + O((\Delta S)^6)
    $$

    Rearranging and dividing by $(\Delta S)^2$:

    $$
    \frac{V_{j+1} - 2V_j + V_{j-1}}{(\Delta S)^2} = V_{SS} + \frac{1}{12}V_{SSSS}(\Delta S)^2 + O((\Delta S)^4)
    $$

    The truncation error for gamma is $\frac{1}{12}V_{SSSS}(\Delta S)^2 + O((\Delta S)^4)$.

---

**Exercise 2.** Given FDM option values $V_{j-1} = 7.20$, $V_j = 9.85$, $V_{j+1} = 12.80$ with $\Delta S = 2$, compute central difference estimates for delta and gamma. Then compute the fourth-order delta estimate if additionally $V_{j-2} = 4.90$ and $V_{j+2} = 16.00$.

??? success "Solution to Exercise 2"
    Given $V_{j-1} = 7.20$, $V_j = 9.85$, $V_{j+1} = 12.80$, $\Delta S = 2$.

    **Central difference delta:**

    $$
    \Delta_j = \frac{V_{j+1} - V_{j-1}}{2\Delta S} = \frac{12.80 - 7.20}{4} = \frac{5.60}{4} = 1.40
    $$

    **Central difference gamma:**

    $$
    \Gamma_j = \frac{V_{j+1} - 2V_j + V_{j-1}}{(\Delta S)^2} = \frac{12.80 - 19.70 + 7.20}{4} = \frac{0.30}{4} = 0.075
    $$

    **Fourth-order delta** with additional values $V_{j-2} = 4.90$, $V_{j+2} = 16.00$:

    $$
    \Delta_j^{(4)} = \frac{-V_{j+2} + 8V_{j+1} - 8V_{j-1} + V_{j-2}}{12\Delta S}
    $$

    $$
    = \frac{-16.00 + 8(12.80) - 8(7.20) + 4.90}{24} = \frac{-16.00 + 102.40 - 57.60 + 4.90}{24} = \frac{33.70}{24} \approx 1.4042
    $$

    The fourth-order estimate ($1.4042$) differs slightly from the second-order estimate ($1.40$), indicating that the higher-order correction term is small for these values.

---

**Exercise 3.** The bump-and-revalue method for delta requires solving the PDE at $S + \delta S$ and $S - \delta S$. If each PDE solve costs $C$ operations, what is the cost of computing central-difference delta and gamma via bumping? Compare this to the zero additional cost of direct grid extraction.

??? success "Solution to Exercise 3"
    The bump-and-revalue method with central differences requires:

    - **Base solve**: $V(S)$ at cost $C$
    - **Up-bump solve**: $V(S + \delta S)$ at cost $C$
    - **Down-bump solve**: $V(S - \delta S)$ at cost $C$

    **For central-difference delta alone**: 3 solves (base + up + down) = $3C$.

    **For central-difference gamma alone**: The same 3 solves suffice (gamma uses $V(S+\delta S) - 2V(S) + V(S-\delta S)$) = $3C$.

    **For both delta and gamma**: Still only 3 solves = $3C$, since both formulas use the same three solutions.

    **Comparison**: Direct grid extraction requires $0$ additional PDE solves beyond the original solve. The bump-and-revalue method requires $2$ additional solves (the up and down bumps), tripling the total cost from $C$ to $3C$.

    For a production system computing Greeks on many options, the factor-of-3 cost increase is significant. Direct grid extraction is strongly preferred for delta and gamma whenever the target asset price coincides with a grid node.

---

**Exercise 4.** Verify the Black-Scholes PDE consistency relation $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV$ using the following numerical values: $V = 10.45$, $\Delta = 0.56$, $\Gamma = 0.038$, $S = 100$, $r = 0.05$, $\sigma = 0.25$. First compute $\Theta$ from the PDE, then check whether the residual is close to zero.

??? success "Solution to Exercise 4"
    Given: $V = 10.45$, $\Delta = 0.56$, $\Gamma = 0.038$, $S = 100$, $r = 0.05$, $\sigma = 0.25$.

    The Black-Scholes PDE gives:

    $$
    \Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    Compute each term:

    - $rV = 0.05 \times 10.45 = 0.5225$
    - $rS\Delta = 0.05 \times 100 \times 0.56 = 2.80$
    - $\frac{1}{2}\sigma^2 S^2\Gamma = \frac{1}{2}(0.0625)(10000)(0.038) = 11.875$

    Therefore:

    $$
    \Theta = 0.5225 - 2.80 - 11.875 = -14.1525
    $$

    **Residual check:** Substituting back into $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma - rV$:

    $$
    -14.1525 + 2.80 + 11.875 - 0.5225 = 0
    $$

    The residual is exactly zero because theta was derived from the PDE. This confirms the algebraic consistency. In a numerical setting where theta is estimated independently from time stepping, the residual would be nonzero but should be small (on the order of the truncation error).

---

**Exercise 5.** A convergence study at $S = K$ (at the strike) without Rannacher smoothing shows gamma converging at rate $O((\Delta S)^{1/2})$. After applying 4 implicit Rannacher steps, the rate improves to $O((\Delta S)^2)$. Explain the mechanism by which the implicit steps restore the convergence order.

??? success "Solution to Exercise 5"
    The European call payoff $(S - K)^+$ has a discontinuous first derivative (a kink) at $S = K$. The second derivative (the "delta function" contribution at the strike) is singular. This non-smoothness directly affects the FDM solution.

    **Why Rannacher smoothing works:**

    1. The Crank-Nicolson scheme is second-order accurate but **not** $L$-stable. It averages the explicit and implicit operators equally, which means it propagates high-frequency components of the initial data (the payoff kink) without fully damping them. These undamped oscillations contaminate the gamma estimate.

    2. The fully implicit (backward Euler) scheme is only first-order in time but is **$L$-stable**: it damps all high-frequency modes. Applying 2-4 fully implicit steps at the start of the time march (near $\tau = 0$, close to the payoff) smooths out the kink in the numerical solution.

    3. After this initial smoothing, the solution is regular enough that Crank-Nicolson can be applied for the remaining time steps at full second-order accuracy.

    4. The cost of the initial implicit steps is negligible (only a few steps out of hundreds), but the benefit is dramatic: gamma convergence improves from $O((\Delta S)^{1/2})$ to $O((\Delta S)^2)$ near the strike.

    The key insight is that the implicit scheme acts as a low-pass filter, removing the non-smooth components that would otherwise persist and degrade convergence throughout the entire computation.

---

**Exercise 6.** On a non-uniform grid with $S_{j-1} = 96$, $S_j = 100$, $S_{j+1} = 106$ (so $h_- = 4$, $h_+ = 6$), apply the non-uniform central difference formulas for delta and gamma. If $V_{j-1} = 6.50$, $V_j = 9.85$, $V_{j+1} = 14.10$, compute both Greeks and compare to what the uniform-grid formulas would give using $\Delta S = 5$ (the average spacing).

??? success "Solution to Exercise 6"
    Given: $S_{j-1} = 96$, $S_j = 100$, $S_{j+1} = 106$, so $h_- = 4$, $h_+ = 6$, and $V_{j-1} = 6.50$, $V_j = 9.85$, $V_{j+1} = 14.10$.

    **Non-uniform delta formula:**

    $$
    \Delta_j = \frac{h_-^2 V_{j+1} + (h_+^2 - h_-^2)V_j - h_+^2 V_{j-1}}{h_+ h_-(h_+ + h_-)}
    $$

    $$
    = \frac{16(14.10) + (36 - 16)(9.85) - 36(6.50)}{6 \times 4 \times 10}
    $$

    $$
    = \frac{225.60 + 197.00 - 234.00}{240} = \frac{188.60}{240} \approx 0.7858
    $$

    **Non-uniform gamma formula:**

    $$
    \Gamma_j = \frac{2(h_- V_{j+1} - (h_+ + h_-)V_j + h_+ V_{j-1})}{h_+ h_-(h_+ + h_-)}
    $$

    $$
    = \frac{2(4(14.10) - 10(9.85) + 6(6.50))}{240}
    $$

    $$
    = \frac{2(56.40 - 98.50 + 39.00)}{240} = \frac{2(-3.10)}{240} = \frac{-6.20}{240} \approx -0.0258
    $$

    **Uniform-grid comparison** with $\Delta S = 5$ (average spacing):

    $$
    \Delta_j^{\text{uniform}} = \frac{V_{j+1} - V_{j-1}}{2\Delta S} = \frac{14.10 - 6.50}{10} = 0.76
    $$

    $$
    \Gamma_j^{\text{uniform}} = \frac{V_{j+1} - 2V_j + V_{j-1}}{(\Delta S)^2} = \frac{14.10 - 19.70 + 6.50}{25} = \frac{0.90}{25} = 0.036
    $$

    The non-uniform formulas give $\Delta \approx 0.786$ and $\Gamma \approx -0.026$, while the uniform approximation gives $\Delta = 0.76$ and $\Gamma = 0.036$. The discrepancy is substantial, particularly for gamma (different sign), demonstrating that applying uniform-grid formulas on a non-uniform grid introduces significant error. The non-uniform formulas correctly account for the asymmetric spacing.
