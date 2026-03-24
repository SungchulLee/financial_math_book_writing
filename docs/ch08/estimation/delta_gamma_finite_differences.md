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

---

**Exercise 2.** Given FDM option values $V_{j-1} = 7.20$, $V_j = 9.85$, $V_{j+1} = 12.80$ with $\Delta S = 2$, compute central difference estimates for delta and gamma. Then compute the fourth-order delta estimate if additionally $V_{j-2} = 4.90$ and $V_{j+2} = 16.00$.

---

**Exercise 3.** The bump-and-revalue method for delta requires solving the PDE at $S + \delta S$ and $S - \delta S$. If each PDE solve costs $C$ operations, what is the cost of computing central-difference delta and gamma via bumping? Compare this to the zero additional cost of direct grid extraction.

---

**Exercise 4.** Verify the Black-Scholes PDE consistency relation $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV$ using the following numerical values: $V = 10.45$, $\Delta = 0.56$, $\Gamma = 0.038$, $S = 100$, $r = 0.05$, $\sigma = 0.25$. First compute $\Theta$ from the PDE, then check whether the residual is close to zero.

---

**Exercise 5.** A convergence study at $S = K$ (at the strike) without Rannacher smoothing shows gamma converging at rate $O((\Delta S)^{1/2})$. After applying 4 implicit Rannacher steps, the rate improves to $O((\Delta S)^2)$. Explain the mechanism by which the implicit steps restore the convergence order.

---

**Exercise 6.** On a non-uniform grid with $S_{j-1} = 96$, $S_j = 100$, $S_{j+1} = 106$ (so $h_- = 4$, $h_+ = 6$), apply the non-uniform central difference formulas for delta and gamma. If $V_{j-1} = 6.50$, $V_j = 9.85$, $V_{j+1} = 14.10$, compute both Greeks and compare to what the uniform-grid formulas would give using $\Delta S = 5$ (the average spacing).
