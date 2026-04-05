# Accuracy and Grid Sensitivity

The accuracy of Greek estimates from finite difference methods depends critically on the spatial and temporal grid resolution. This section analyzes how truncation errors propagate into Greek estimates, how to verify convergence through grid refinement studies, and how to mitigate accuracy degradation near the payoff kink.

---

## Sources of Error in Greek Estimates

Greek estimates from FDM carry errors from multiple sources:

1. **Spatial truncation error**: From replacing derivatives with finite differences ($O((\Delta S)^2)$ for central differences)
2. **Temporal truncation error**: From time-stepping ($O(\Delta\tau)$ for Euler, $O((\Delta\tau)^2)$ for Crank-Nicolson)
3. **Domain truncation error**: From approximating the infinite domain $(0, \infty)$ with $[0, S_{\max}]$
4. **Payoff non-smoothness**: The kink in $(S-K)^+$ reduces convergence order near the strike
5. **Cancellation error**: Differencing nearby solution values amplifies small errors

The total error in a Greek estimate is a combination of all five sources, with the dominant source depending on the grid resolution and the location in the $(S, t)$ plane.

---

## Error Amplification in Differentiation

### The Fundamental Issue

Numerical differentiation **amplifies** errors. If the option price has error $\varepsilon$, then:

**Delta error** (first difference):

$$
\left|\frac{(V_{j+1} + \varepsilon_{j+1}) - (V_{j-1} + \varepsilon_{j-1})}{2\Delta S} - \frac{V_{j+1} - V_{j-1}}{2\Delta S}\right| = \frac{|\varepsilon_{j+1} - \varepsilon_{j-1}|}{2\Delta S} \leq \frac{\varepsilon}{\Delta S}
$$

**Gamma error** (second difference):

$$
\frac{|\varepsilon_{j+1} - 2\varepsilon_j + \varepsilon_{j-1}|}{(\Delta S)^2} \leq \frac{4\varepsilon}{(\Delta S)^2}
$$

!!! warning "Error Amplification"
    Differencing divides by powers of $\Delta S$. Delta amplifies price errors by $1/\Delta S$, and gamma amplifies by $1/(\Delta S)^2$. This means gamma is far more sensitive to grid resolution than delta, and delta is more sensitive than the price itself.

### Implication for Grid Design

The error in the price converges as $O((\Delta S)^2)$. After dividing by $\Delta S$ (for delta) or $(\Delta S)^2$ (for gamma):

| Quantity | Price error | Net convergence |
|----------|-------------|-----------------|
| Price $V$ | $O((\Delta S)^2)$ | $O((\Delta S)^2)$ |
| Delta $\Delta$ | $O((\Delta S)^2) / \Delta S$ | $O((\Delta S)^2)$ |
| Gamma $\Gamma$ | $O((\Delta S)^2) / (\Delta S)^2$ | $O((\Delta S)^2)$ |

For smooth solutions, all three converge at the same rate because the truncation error and the amplification balance: the central difference formulas for delta and gamma are independently $O((\Delta S)^2)$ accurate.

However, when the solution is not smooth (near the strike), the price error is worse than $O((\Delta S)^2)$, and the amplification effect causes gamma to converge much more slowly.

---

## Grid Refinement Studies

### Methodology

A grid refinement study (or convergence study) systematically varies the grid resolution and measures how the error decreases.

**Step 1**: Choose a sequence of grids with $M_k = M_0 \cdot 2^k$ spatial points for $k = 0, 1, 2, \ldots$

**Step 2**: For each grid, compute the Greek estimate $G_k$ at a target point $(S_0, t_0)$

**Step 3**: Compute the error $e_k = |G_k - G_{\text{exact}}|$ (if the analytical value is available) or the successive difference $\delta_k = |G_k - G_{k+1}|$

**Step 4**: The convergence order is:

$$
p \approx \frac{\log(e_k / e_{k+1})}{\log 2}
$$

or equivalently, the slope of the log-log plot of error vs $\Delta S$.

### Example: Delta Convergence (Smooth Region)

European call, $K = 100$, $S = 110$, $T = 0.5$, $\sigma = 0.3$, $r = 0.05$.

| $M$ | $\Delta S$ | $\Delta_{\text{FDM}}$ | Error | Ratio |
|-----|-----------|----------------------|-------|-------|
| 50 | 6.0 | 0.6427 | $8.3 \times 10^{-3}$ | --- |
| 100 | 3.0 | 0.6489 | $2.1 \times 10^{-3}$ | 4.0 |
| 200 | 1.5 | 0.6505 | $5.2 \times 10^{-4}$ | 4.0 |
| 400 | 0.75 | 0.6509 | $1.3 \times 10^{-4}$ | 4.0 |

Exact: $\Delta = 0.6510$. Ratio $\approx 4$ confirms second-order convergence ($p = 2$).

### Example: Gamma Convergence (At the Strike)

European call, $K = 100$, $S = 100$, $T = 0.5$, $\sigma = 0.3$, $r = 0.05$.

**Without Rannacher smoothing**:

| $M$ | $\Gamma_{\text{FDM}}$ | Error | Ratio |
|-----|----------------------|-------|-------|
| 50 | 0.0218 | $3.6 \times 10^{-3}$ | --- |
| 100 | 0.0236 | $1.8 \times 10^{-3}$ | 2.0 |
| 200 | 0.0247 | $7.4 \times 10^{-4}$ | 2.4 |
| 400 | 0.0251 | $3.2 \times 10^{-4}$ | 2.3 |

Ratio $\approx 2$ to $2.4$, indicating convergence around $O((\Delta S)^{1})$ to $O((\Delta S)^{1.3})$, well below the theoretical $O((\Delta S)^2)$.

**With Rannacher smoothing** (4 implicit steps):

| $M$ | $\Gamma_{\text{FDM}}$ | Error | Ratio |
|-----|----------------------|-------|-------|
| 50 | 0.0233 | $2.1 \times 10^{-3}$ | --- |
| 100 | 0.0249 | $5.4 \times 10^{-4}$ | 3.9 |
| 200 | 0.0253 | $1.4 \times 10^{-4}$ | 3.9 |
| 400 | 0.0254 | $3.5 \times 10^{-5}$ | 4.0 |

Ratio $\approx 4$ confirms restored second-order convergence.

---

## Spatial Grid Sensitivity

### Resolution Requirements by Region

| Region | Behavior | Required $\Delta S$ |
|--------|----------|-------------------|
| $S \ll K$ (deep OTM call) | $V \approx 0$, flat | Coarse is adequate |
| $S \approx K$ (at-the-money) | High curvature, gamma peak | Fine resolution critical |
| $S \gg K$ (deep ITM call) | $V \approx S - Ke^{-rT}$, linear | Coarse is adequate |

### Grid Placement: Node at the Strike

Placing a spatial node exactly at $S = K$ dramatically improves accuracy for at-the-money Greeks.

**With $K$ on a node**: The payoff kink is captured exactly, and the difference stencil for gamma at $S = K$ uses the correct values on both sides.

**With $K$ between nodes**: Interpolation is needed, and the difference stencil "smears" the kink, reducing accuracy. The error can be $O((\Delta S)^{1/2})$ for gamma instead of $O((\Delta S)^2)$.

To ensure $K$ falls on a node, choose $\Delta S = K / J$ for some integer $J$, giving $S_J = K$.

### Non-Uniform Grids

A sinh stretching concentrates grid points near the strike:

$$
S_j = K + K \frac{\sinh(\alpha(j/M - 1/2))}{\sinh(\alpha/2)}, \quad j = 0, 1, \ldots, M
$$

where $\alpha > 0$ controls the concentration. Larger $\alpha$ gives more points near $K$.

On non-uniform grids, the standard central difference formulas must be modified. For nodes $S_{j-1}, S_j, S_{j+1}$ with spacings $h_- = S_j - S_{j-1}$ and $h_+ = S_{j+1} - S_j$:

$$
\Delta_j \approx \frac{h_-^2 V_{j+1} + (h_+^2 - h_-^2)V_j - h_+^2 V_{j-1}}{h_+ h_-(h_+ + h_-)}
$$

$$
\Gamma_j \approx \frac{2(h_- V_{j+1} - (h_+ + h_-)V_j + h_+ V_{j-1})}{h_+ h_-(h_+ + h_-)}
$$

---

## Temporal Grid Sensitivity

### Effect on Price and Greeks

| Scheme | Price accuracy | Greek accuracy (spatial) | Greek accuracy (temporal) |
|--------|---------------|--------------------------|---------------------------|
| Explicit | $O(\Delta\tau + (\Delta S)^2)$ | $O((\Delta S)^2)$ | $O(\Delta\tau)$ |
| Implicit | $O(\Delta\tau + (\Delta S)^2)$ | $O((\Delta S)^2)$ | $O(\Delta\tau)$ |
| Crank-Nicolson | $O((\Delta\tau)^2 + (\Delta S)^2)$ | $O((\Delta S)^2)$ | $O((\Delta\tau)^2)$ |

For Crank-Nicolson, matching temporal and spatial accuracy requires:

$$
(\Delta\tau)^2 \sim (\Delta S)^2 \quad \Longrightarrow \quad N \sim M
$$

For the implicit scheme:

$$
\Delta\tau \sim (\Delta S)^2 \quad \Longrightarrow \quad N \sim M^2
$$

The implicit scheme needs many more time steps to achieve the same accuracy as Crank-Nicolson.

### Temporal Sensitivity of Theta

Theta computed from time differencing is directly affected by $\Delta\tau$:

$$
\text{Theta error} \sim O(\Delta\tau) \text{ (backward difference)}
$$

The PDE-based theta formula $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2\Gamma$ avoids this sensitivity entirely.

---

## Richardson Extrapolation for Greeks

Richardson extrapolation can be applied to Greek estimates, not just prices.

### For Delta

Compute delta on grids with $M$ and $2M$ spatial points:

$$
\Delta_{\text{ext}} = \frac{4\Delta(2M) - \Delta(M)}{3}
$$

This produces an $O((\Delta S)^4)$ accurate delta estimate from two $O((\Delta S)^2)$ estimates.

### For Gamma

Similarly:

$$
\Gamma_{\text{ext}} = \frac{4\Gamma(2M) - \Gamma(M)}{3}
$$

!!! tip "Cost-Effective Accuracy"
    Extrapolating from two moderate-resolution grids often gives better accuracy than a single fine grid at comparable total cost. For Greeks, where accuracy is critical for hedging, this is a practical and recommended technique.

---

## Diagnostic Tools

### Self-Consistency Checks

1. **PDE residual**: $|\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma - rV|$ should be small at each node
2. **Put-call parity Greeks**: For European options, $\Delta_{\text{call}} - \Delta_{\text{put}} = 1$, $\Gamma_{\text{call}} = \Gamma_{\text{put}}$, $\mathcal{V}_{\text{call}} = \mathcal{V}_{\text{put}}$
3. **Boundary behavior**: $\Delta \to 1$ and $\Gamma \to 0$ as $S \to \infty$ for calls
4. **Symmetry**: Vega is the same for calls and puts with equal parameters

### Convergence Plots

Plotting the error vs $\Delta S$ on a log-log scale reveals:

- **Slope = 2**: Second-order convergence (expected for smooth regions)
- **Slope < 2**: Reduced convergence (typically near the strike without smoothing)
- **Slope flattening**: Machine precision or cancellation error floor reached
- **Slope increase after extrapolation**: Successful Richardson extrapolation

---

## Summary

| Greek | Smooth region | At strike (no smoothing) | At strike (Rannacher) |
|-------|--------------|-------------------------|----------------------|
| Price $V$ | $O((\Delta S)^2)$ | $O(\Delta S)$ | $O((\Delta S)^2)$ |
| Delta $\Delta$ | $O((\Delta S)^2)$ | $O(\Delta S)$ | $O((\Delta S)^2)$ |
| Gamma $\Gamma$ | $O((\Delta S)^2)$ | $O((\Delta S)^{1/2})$ | $O((\Delta S)^2)$ |

$$
\boxed{
\text{Grid design: place node at } K, \text{ use Rannacher smoothing, verify } p \approx 2 \text{ via refinement study}
}
$$

| Recommendation | Detail |
|---------------|--------|
| **Spatial grid** | Place node at $K$; use non-uniform grid if needed |
| **Temporal grid** | Match $\Delta\tau$ to $\Delta S$ for Crank-Nicolson |
| **Smoothing** | 2-4 Rannacher steps for non-smooth payoffs |
| **Verification** | Grid refinement study with ratio $\approx 4$ |
| **Extrapolation** | Use Richardson extrapolation for Greek estimates |
| **Validation** | Check PDE residual and put-call parity relations |

Reliable Greek estimates require more care than reliable prices. The amplification of errors through differentiation, combined with payoff non-smoothness, makes grid design and convergence verification essential steps in any production-quality FDM implementation.

---

## Exercises

**Exercise 1.** If the option price at each grid node has error $\varepsilon = 10^{-4}$ and $\Delta S = 1$, compute the maximum amplified error in the central difference delta and gamma estimates. Repeat for $\Delta S = 0.5$ and explain the tradeoff between truncation error (which decreases with $\Delta S$) and amplified error (which increases).

??? success "Solution to Exercise 1"
    With $\varepsilon = 10^{-4}$ and $\Delta S = 1$:

    **Delta amplified error:**

    $$
    \text{Error}_\Delta \leq \frac{\varepsilon}{\Delta S} = \frac{10^{-4}}{1} = 10^{-4}
    $$

    **Gamma amplified error:**

    $$
    \text{Error}_\Gamma \leq \frac{4\varepsilon}{(\Delta S)^2} = \frac{4 \times 10^{-4}}{1} = 4 \times 10^{-4}
    $$

    Now with $\Delta S = 0.5$:

    **Delta amplified error:**

    $$
    \text{Error}_\Delta \leq \frac{10^{-4}}{0.5} = 2 \times 10^{-4}
    $$

    **Gamma amplified error:**

    $$
    \text{Error}_\Gamma \leq \frac{4 \times 10^{-4}}{0.25} = 1.6 \times 10^{-3}
    $$

    **The tradeoff:** Halving $\Delta S$ reduces the truncation error by a factor of 4 (for second-order formulas: truncation $\sim (\Delta S)^2$), but doubles the amplified error for delta and quadruples it for gamma. The total error is the sum of both:

    $$
    \text{Total error} = C_1 (\Delta S)^2 + \frac{C_2 \varepsilon}{(\Delta S)^k}
    $$

    where $k = 1$ for delta and $k = 2$ for gamma. There is an optimal $\Delta S$ that minimizes the total error. For gamma, this optimal value is larger than for delta, meaning gamma requires a coarser grid to balance the two error sources --- a counterintuitive but important result for grid design.

---

**Exercise 2.** A grid refinement study for gamma at $S = K$ (without Rannacher smoothing) gives error ratios of approximately 2.0, 2.4, 2.3 across successive refinements. Compute the observed convergence order $p \approx \log_2(R)$ for each pair. Is the order consistent with the theoretical $O((\Delta S)^{1/2})$ behavior near the strike?

??? success "Solution to Exercise 2"
    The error ratios are approximately $R_1 = 2.0$, $R_2 = 2.4$, $R_3 = 2.3$. The observed convergence order is $p = \log_2(R)$:

    - From $R_1 = 2.0$: $p_1 = \log_2(2.0) = 1.0$
    - From $R_2 = 2.4$: $p_2 = \log_2(2.4) \approx 1.26$
    - From $R_3 = 2.3$: $p_3 = \log_2(2.3) \approx 1.20$

    The observed orders range from $1.0$ to $1.26$, averaging about $p \approx 1.15$.

    **Comparison with theory:** The theoretical convergence rate for gamma at the strike without Rannacher smoothing is $O((\Delta S)^{1/2})$, which corresponds to $p = 0.5$. The observed $p \approx 1.15$ is higher than $0.5$, suggesting that the convergence is not purely $O((\Delta S)^{1/2})$.

    This discrepancy is typical in practice. The theoretical $O((\Delta S)^{1/2})$ rate is an asymptotic worst case. On finite grids, the observed rate often appears higher because:

    1. The $O((\Delta S)^{1/2})$ regime may not be fully reached at the grid sizes tested
    2. The error has multiple terms with different powers of $\Delta S$, and the pre-asymptotic behavior blends them
    3. Grid alignment relative to the strike affects the constants

    The key diagnostic is that the ratio is well below $4.0$ (which would indicate $p = 2$), confirming that convergence is degraded compared to the smooth-region rate.

---

**Exercise 3.** Explain why placing a grid node exactly at $S = K$ improves gamma accuracy. If $K = 100$ and $M = 150$ with $S_{\max} = 300$, the uniform grid spacing is $\Delta S = 2$, and $S_{50} = 100$ falls exactly on the strike. But if $M = 149$, does $K$ fall on a node? Compute the nearest grid points and the interpolation error.

??? success "Solution to Exercise 3"
    **Why a node at $K$ helps gamma accuracy:** The payoff $(S-K)^+$ has a kink at $S = K$: the first derivative jumps from 0 to 1. The gamma (second derivative) formula at $S = K$ involves the values at $S_{j-1}$, $S_j = K$, and $S_{j+1}$. When $K$ is exactly on a node:

    - $V_{j-1}$ is in the region $S < K$ where the payoff is flat (for a call)
    - $V_{j+1}$ is in the region $S > K$ where the payoff is linear
    - The stencil correctly captures the transition at the kink

    When $K$ falls between nodes, the kink is "smeared" across two intervals, and the difference stencil does not align with the discontinuity in the derivative. This misalignment causes the gamma estimate to oscillate and converge slowly.

    **Computation for $M = 149$, $S_{\max} = 300$:**

    $$
    \Delta S = \frac{300}{149} \approx 2.01342
    $$

    The node nearest to $K = 100$: $j = \lfloor 100/\Delta S \rceil = \lfloor 49.67 \rceil = 50$, giving $S_{50} = 50 \times 2.01342 \approx 100.671$. The neighboring node is $S_{49} = 49 \times 2.01342 \approx 98.658$.

    So $K = 100$ falls between $S_{49} \approx 98.66$ and $S_{50} \approx 100.67$. The interpolation error is at least $O(\Delta S)$ in the price, and after differencing twice for gamma, this becomes $O(\Delta S / (\Delta S)^2) = O(1/\Delta S)$ in the worst case or $O((\Delta S)^{1/2})$ in practice, significantly worse than the $O((\Delta S)^2)$ rate achievable when $K$ sits on a node.

---

**Exercise 4.** The sinh stretching formula $S_j = K + K\sinh(\alpha(j/M - 1/2))/\sinh(\alpha/2)$ concentrates points near $K$. For $\alpha = 5$ and $M = 100$, compute the local spacing near $K$ (i.e., $S_{51} - S_{50}$) and compare it to the spacing far from $K$ (e.g., $S_{90} - S_{89}$). How does this non-uniformity improve Greek accuracy?

??? success "Solution to Exercise 4"
    The sinh stretching formula is:

    $$
    S_j = K + K\frac{\sinh(\alpha(j/M - 1/2))}{\sinh(\alpha/2)}
    $$

    With $\alpha = 5$, $M = 100$, $K = 100$:

    **Near the strike** ($j = 50$ and $j = 51$): At $j = 50$, $S_{50} = 100 + 100 \cdot \sinh(0)/\sinh(2.5) = 100$ (exactly at the strike). At $j = 51$:

    $$
    S_{51} = 100 + 100 \cdot \frac{\sinh(5(51/100 - 1/2))}{\sinh(2.5)} = 100 + 100 \cdot \frac{\sinh(0.05)}{\sinh(2.5)}
    $$

    $$
    \approx 100 + 100 \cdot \frac{0.05004}{6.0502} \approx 100 + 0.827 = 100.827
    $$

    Local spacing near $K$: $S_{51} - S_{50} \approx 0.827$.

    **Far from the strike** ($j = 89$ and $j = 90$): At $j = 90$:

    $$
    S_{90} = 100 + 100 \cdot \frac{\sinh(5(0.9 - 0.5))}{\sinh(2.5)} = 100 + 100 \cdot \frac{\sinh(2.0)}{\sinh(2.5)}
    $$

    $$
    \approx 100 + 100 \cdot \frac{3.6269}{6.0502} \approx 100 + 59.95 = 159.95
    $$

    At $j = 89$:

    $$
    S_{89} = 100 + 100 \cdot \frac{\sinh(5(0.89 - 0.5))}{\sinh(2.5)} \approx 100 + 100 \cdot \frac{\sinh(1.95)}{\sinh(2.5)}
    $$

    $$
    \approx 100 + 100 \cdot \frac{3.4482}{6.0502} \approx 100 + 56.99 = 156.99
    $$

    Spacing far from $K$: $S_{90} - S_{89} \approx 2.96$.

    **Comparison:** The spacing near the strike ($\approx 0.83$) is about 3.6 times smaller than the spacing far from the strike ($\approx 2.96$). This concentration of grid points near $K$ improves Greek accuracy in the critical region where gamma peaks and delta changes most rapidly, without requiring a uniformly fine grid (which would be wasteful in the flat regions far from the strike).

---

**Exercise 5.** Richardson extrapolation for Greeks: compute delta on grids with $M = 100$ and $M = 200$, obtaining $\Delta(100) = 0.6489$ and $\Delta(200) = 0.6505$. Apply the extrapolation formula $\Delta_{\text{ext}} = (4\Delta(200) - \Delta(100))/3$. If the exact delta is $0.6510$, compare the errors.

??? success "Solution to Exercise 5"
    Given $\Delta(100) = 0.6489$ and $\Delta(200) = 0.6505$, the Richardson extrapolation formula for second-order estimates (doubling the grid) is:

    $$
    \Delta_{\text{ext}} = \frac{4\Delta(200) - \Delta(100)}{3} = \frac{4(0.6505) - 0.6489}{3} = \frac{2.6020 - 0.6489}{3} = \frac{1.9531}{3} = 0.65103
    $$

    **Error comparison** (exact $\Delta = 0.6510$):

    - $|\Delta(100) - 0.6510| = |0.6489 - 0.6510| = 2.1 \times 10^{-3}$
    - $|\Delta(200) - 0.6510| = |0.6505 - 0.6510| = 5.0 \times 10^{-4}$
    - $|\Delta_{\text{ext}} - 0.6510| = |0.65103 - 0.6510| = 3 \times 10^{-5}$

    The extrapolated estimate has error $3 \times 10^{-5}$, which is about **70 times smaller** than the $M = 100$ error and **17 times smaller** than the $M = 200$ error. The extrapolation effectively converts two $O((\Delta S)^2)$ estimates into an $O((\Delta S)^4)$ estimate. The total computational cost is that of solving on both grids ($M = 100$ and $M = 200$), which is roughly $1.25 \times$ the cost of the $M = 200$ solve alone (since the $M = 100$ solve is about 4 times cheaper). This is far more efficient than solving on a single $M = 800$ grid to achieve comparable accuracy.

---

**Exercise 6.** The PDE residual $|\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma - rV|$ should be small at every grid node. If you observe a large residual at a particular node, list three possible causes and describe how you would diagnose each one.

??? success "Solution to Exercise 6"
    Three possible causes of a large PDE residual at a particular node, and how to diagnose each:

    **Cause 1: Insufficient spatial grid resolution.** If $\Delta S$ is too large relative to the local curvature of the solution, the finite difference approximations for $\Delta$ and $\Gamma$ have large truncation errors. These errors propagate into the PDE residual.

    *Diagnosis:* Refine the spatial grid (double $M$) and recompute the residual at the same node. If the residual decreases by a factor of approximately 4 (for second-order methods), spatial resolution was the issue.

    **Cause 2: Proximity to the payoff kink.** Near $S = K$, the non-smoothness of the payoff degrades the accuracy of all Greek estimates, particularly gamma. Even with adequate grid resolution elsewhere, the kink causes locally large errors.

    *Diagnosis:* Check whether the offending node is near $S = K$. Plot the residual across all spatial nodes --- if it peaks sharply at or near the strike while being small elsewhere, the kink is the cause. Applying Rannacher smoothing (2-4 implicit time steps at the start) and re-checking should reduce the residual.

    **Cause 3: Boundary condition contamination.** If $S_{\max}$ is not large enough, or if the boundary condition is inaccurate, the error from the boundary propagates inward. Nodes near $S_{\max}$ (or $S = 0$) are most affected.

    *Diagnosis:* Check whether the offending node is near the domain boundary. Increase $S_{\max}$ (e.g., double it) and recompute. If the residual decreases, the boundary was too close. Alternatively, compare the boundary condition value to the analytical solution (if available) to check for implementation errors in the boundary formula.
