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

---

**Exercise 2.** A grid refinement study for gamma at $S = K$ (without Rannacher smoothing) gives error ratios of approximately 2.0, 2.4, 2.3 across successive refinements. Compute the observed convergence order $p \approx \log_2(R)$ for each pair. Is the order consistent with the theoretical $O((\Delta S)^{1/2})$ behavior near the strike?

---

**Exercise 3.** Explain why placing a grid node exactly at $S = K$ improves gamma accuracy. If $K = 100$ and $M = 150$ with $S_{\max} = 300$, the uniform grid spacing is $\Delta S = 2$, and $S_{50} = 100$ falls exactly on the strike. But if $M = 149$, does $K$ fall on a node? Compute the nearest grid points and the interpolation error.

---

**Exercise 4.** The sinh stretching formula $S_j = K + K\sinh(\alpha(j/M - 1/2))/\sinh(\alpha/2)$ concentrates points near $K$. For $\alpha = 5$ and $M = 100$, compute the local spacing near $K$ (i.e., $S_{51} - S_{50}$) and compare it to the spacing far from $K$ (e.g., $S_{90} - S_{89}$). How does this non-uniformity improve Greek accuracy?

---

**Exercise 5.** Richardson extrapolation for Greeks: compute delta on grids with $M = 100$ and $M = 200$, obtaining $\Delta(100) = 0.6489$ and $\Delta(200) = 0.6505$. Apply the extrapolation formula $\Delta_{\text{ext}} = (4\Delta(200) - \Delta(100))/3$. If the exact delta is $0.6510$, compare the errors.

---

**Exercise 6.** The PDE residual $|\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma - rV|$ should be small at every grid node. If you observe a large residual at a particular node, list three possible causes and describe how you would diagnose each one.
