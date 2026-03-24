# Local Volatility Surface Construction

Constructing the local volatility surface from market data is the computational realization of Dupire's formula. While the formula itself is elegant — a ratio of partial derivatives of the call price surface — its numerical implementation faces substantial challenges. The call surface must be differentiated twice in strike and once in time, operations that amplify noise and can produce negative or unbounded values if the input data is not carefully prepared. This section develops the complete pipeline from smoothed market data (the output of interpolation and smoothing) to a validated local volatility surface $\sigma_{\text{loc}}(K, T)$, covering numerical differentiation, regularization, and diagnostic checks.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Implement Dupire's formula numerically using finite differences on a smoothed call price surface
    - Apply Dupire's formula in implied volatility space using the Gatheral-Jacquier formulation
    - Identify and mitigate sources of numerical instability (small denominator, wing extrapolation, sparse maturity grid)
    - Apply Tikhonov regularization and positivity constraints to produce a well-behaved surface
    - Validate the constructed surface by repricing vanilla options

## Numerical Dupire Formula

### The Formula in Price Space

Dupire's formula expresses local volatility in terms of call price derivatives:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + qC + (r - q)K\frac{\partial C}{\partial K}}{\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}}
$$

Given a smooth call price surface $\hat{C}(K, T)$ (from the interpolation step), the derivatives are approximated by finite differences.

### Finite Difference Approximations

**Time derivative** (centered difference):

$$
\frac{\partial C}{\partial T}\bigg|_{K_i, T_j} \approx \frac{\hat{C}(K_i, T_{j+1}) - \hat{C}(K_i, T_{j-1})}{T_{j+1} - T_{j-1}}
$$

At the boundary maturities, use one-sided differences:

$$
\frac{\partial C}{\partial T}\bigg|_{K_i, T_1} \approx \frac{\hat{C}(K_i, T_2) - \hat{C}(K_i, T_1)}{T_2 - T_1}
$$

**Strike derivatives** (centered differences on a non-uniform grid):

$$
\frac{\partial C}{\partial K}\bigg|_{K_i, T_j} \approx \frac{\hat{C}(K_{i+1}, T_j) - \hat{C}(K_{i-1}, T_j)}{K_{i+1} - K_{i-1}}
$$

$$
\frac{\partial^2 C}{\partial K^2}\bigg|_{K_i, T_j} \approx \frac{2}{K_{i+1} - K_{i-1}}\left(\frac{\hat{C}(K_{i+1}, T_j) - \hat{C}(K_i, T_j)}{K_{i+1} - K_i} - \frac{\hat{C}(K_i, T_j) - \hat{C}(K_{i-1}, T_j)}{K_i - K_{i-1}}\right)
$$

For a uniform grid with spacing $\Delta K$, this simplifies to the standard centered second difference:

$$
\frac{\partial^2 C}{\partial K^2}\bigg|_{K_i, T_j} \approx \frac{\hat{C}(K_{i+1}, T_j) - 2\hat{C}(K_i, T_j) + \hat{C}(K_{i-1}, T_j)}{(\Delta K)^2}
$$

### Assembly

Combining these approximations yields $\sigma_{\text{loc}}^2(K_i, T_j)$ at each grid point. Points where the denominator is too small (below a threshold $\epsilon_{\min}$) or the numerator is negative are flagged and handled by the regularization step described below.

## Dupire Formula in Implied Volatility Space

### Motivation

An alternative to differentiating call prices is to express Dupire's formula directly in terms of implied volatility derivatives. This is often more stable because the implied volatility surface is smoother than the price surface.

### The Gatheral-Jacquier Formula

Given the implied volatility surface $\sigma_{\text{IV}}(K, T)$, the local volatility is:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\sigma_{\text{IV}}^2 + 2\sigma_{\text{IV}}T\frac{\partial \sigma_{\text{IV}}}{\partial T} + 2(r - q)K\sigma_{\text{IV}}T\frac{\partial \sigma_{\text{IV}}}{\partial K}}{\left(1 + Kd_1\sqrt{T}\frac{\partial \sigma_{\text{IV}}}{\partial K}\right)^2 + \sigma_{\text{IV}}K^2 T\left(\frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2} - d_1\sqrt{T}\left(\frac{\partial \sigma_{\text{IV}}}{\partial K}\right)^2\right)}
$$

where $d_1 = \frac{\ln(S_0/K) + (r - q + \sigma_{\text{IV}}^2/2)T}{\sigma_{\text{IV}}\sqrt{T}}$.

This formula requires only the first and second derivatives of $\sigma_{\text{IV}}$ with respect to strike, and the first derivative with respect to maturity. When the IV surface is represented by an analytic parametrization (SVI, SSVI), these derivatives can be computed analytically, avoiding finite differences entirely.

### Total Variance Formulation

In terms of total variance $w(y, T) = \sigma_{\text{IV}}^2(y, T) \cdot T$ and log-moneyness $y = \ln(K/F)$, the formula simplifies to:

$$
\sigma_{\text{loc}}^2 = \frac{\frac{\partial w}{\partial T}}{\left(1 - \frac{y}{w}\frac{\partial w}{\partial y}\right)^2 - \frac{1}{4}\left(\frac{\partial w}{\partial y}\right)^2\left(\frac{1}{w} + \frac{1}{4}\right) + \frac{1}{2}\frac{\partial^2 w}{\partial y^2}}
$$

The denominator is precisely Durrleman's condition $g(y, T) \geq 0$, so positivity of the denominator is equivalent to absence of butterfly arbitrage.

!!! note "Analytic Derivatives from SVI"
    For the SVI parametrization $w(y) = a + b(\rho(y-m) + \sqrt{(y-m)^2 + \sigma^2})$, the derivatives are:

    $$
    \frac{\partial w}{\partial y} = b\left(\rho + \frac{y - m}{\sqrt{(y-m)^2 + \sigma^2}}\right)
    $$

    $$
    \frac{\partial^2 w}{\partial y^2} = \frac{b\sigma^2}{((y-m)^2 + \sigma^2)^{3/2}}
    $$

    These are smooth, bounded, and free of numerical differentiation noise, making SVI-based construction particularly robust.

## Regularization

### The Ill-Posedness Problem

Even after smoothing, the local volatility surface can exhibit problematic behavior:

1. **Spikes:** Where $C_{KK}$ is close to zero (deep OTM/ITM), $\sigma_{\text{loc}}$ diverges
2. **Oscillations:** Residual noise in $C$ produces high-frequency oscillations in $\sigma_{\text{loc}}$
3. **Negative values:** Numerical errors can produce $\sigma_{\text{loc}}^2 < 0$ at isolated points

These issues stem from the **ill-posedness** of the inverse problem: small perturbations in $C$ produce large changes in $\sigma_{\text{loc}}$.

### Tikhonov Regularization

Instead of applying Dupire's formula pointwise, solve the inverse problem with a regularization penalty:

$$
\min_{\sigma_{\text{loc}}} \left\{\sum_{i,j} w_{ij}\left(C_{\text{model}}(K_i, T_j; \sigma_{\text{loc}}) - \hat{C}(K_i, T_j)\right)^2 + \lambda_1 \int\!\!\int \left(\frac{\partial \sigma_{\text{loc}}}{\partial K}\right)^2 dK \, dT + \lambda_2 \int\!\!\int \left(\frac{\partial \sigma_{\text{loc}}}{\partial T}\right)^2 dK \, dT\right\}
$$

where $C_{\text{model}}(K_i, T_j; \sigma_{\text{loc}})$ is the price computed by solving the forward PDE with the candidate $\sigma_{\text{loc}}$, and $\lambda_1, \lambda_2 > 0$ are regularization parameters penalizing roughness.

This formulation:

- Ensures $\sigma_{\text{loc}}$ is smooth (via the penalty terms)
- Matches market prices approximately (via the data-fidelity term)
- Requires solving a PDE at each optimization step (computationally expensive)

### Positivity Constraints

Enforce $\sigma_{\text{loc}}^2(K, T) > 0$ by either:

1. **Parametrization:** Write $\sigma_{\text{loc}} = e^{f(K, T)}$ where $f$ is unconstrained
2. **Projection:** After each Dupire computation, set $\sigma_{\text{loc}}^2 = \max(\sigma_{\text{loc}}^2, \sigma_{\min}^2)$ with $\sigma_{\min} = 1\%$
3. **Constrained optimization:** Include $\sigma_{\text{loc}}^2 \geq \sigma_{\min}^2$ as an explicit constraint

### Bounding the Surface

In addition to positivity, practitioners typically enforce upper bounds:

$$
\sigma_{\min}^2 \leq \sigma_{\text{loc}}^2(K, T) \leq \sigma_{\max}^2
$$

with $\sigma_{\min} \in [0.5\%, 2\%]$ and $\sigma_{\max} \in [100\%, 300\%]$. Values outside this range almost always indicate data or numerical problems rather than genuine market dynamics.

## Handling Sparse Data

### Maturity Gaps

Market data often has large gaps between available maturities (e.g., 1M, 2M, 3M, 6M, 1Y, 2Y). Between maturities, the local volatility must be interpolated from the total variance interpolation performed in the smoothing step. The time derivative $\partial C / \partial T$ is particularly sensitive to the maturity gap:

$$
\text{error in } \partial_T C \sim O\left(\frac{(\Delta T)^2}{12}\frac{\partial^3 C}{\partial T^3}\right)
$$

Larger $\Delta T$ increases the error, leading to inaccurate local volatility between maturities.

**Mitigation:** Use the total variance formulation $w_T = \partial w / \partial T$, which is directly available from the interpolation step without additional finite differencing.

### Strike Gaps

In the wings, strikes become sparse and option prices are small, making $C_{KK}$ both noisy and near zero. Strategies include:

1. **SVI extrapolation:** Use the SVI parametrization to extend the smile to extreme strikes with controlled wing behavior
2. **Flat local vol extrapolation:** Beyond the last reliable data point, set $\sigma_{\text{loc}}(K, T) = \sigma_{\text{loc}}(K_{\text{last}}, T)$
3. **Density tail modeling:** Fit parametric tails (e.g., generalized Pareto) to the risk-neutral density and back out the corresponding local volatility

### Short-Maturity Challenges

Near expiry ($T < 1$ month), the option surface is steep in time and the forward variance can change rapidly. The local volatility surface near short maturities requires:

- Dense maturity interpolation points
- Careful handling of the $T \to 0$ limit, where $\sigma_{\text{loc}}(K, 0) = \sigma_{\text{IV}}(K, 0)$ (Berestycki-Busca-Florent)
- Explicit incorporation of known events (earnings, dividends) that create term structure jumps

## Validation

### Repricing Test

The most important diagnostic: if the constructed $\sigma_{\text{loc}}(K, T)$ is correct, solving the local volatility PDE (or running Monte Carlo) should reproduce the market call prices used as input.

**Procedure:**

1. Solve the forward PDE $\partial_T p = \frac{1}{2}\partial_{KK}[\sigma_{\text{loc}}^2 K^2 p]$ with the constructed surface
2. Compute call prices: $C_{\text{reprice}}(K, T) = e^{-rT}\int_K^\infty (S - K) p(S, T) \, dS$
3. Compare: $|C_{\text{reprice}} - C_{\text{market}}| < \epsilon_{\text{tol}}$

Typical tolerance: within 0.5 vol points in implied volatility terms.

### Visual Diagnostics

Useful plots for quality assessment:

1. **Local vol surface:** 3D plot of $\sigma_{\text{loc}}(K, T)$ — look for spikes, negative regions, and unrealistic values
2. **Term structure slices:** $\sigma_{\text{loc}}(K, T)$ at fixed $K$ as a function of $T$ — should be smooth and bounded
3. **Smile slices:** $\sigma_{\text{loc}}(K, T)$ at fixed $T$ as a function of $K$ — typically decreasing for equity indices
4. **Implied vol comparison:** Overlay the original market IV and the IV implied by the repriced surface
5. **Risk-neutral density:** $q(K) = e^{rT} C_{KK}$ — should be positive and integrate to 1

### Stability Test

Perturb the input data by adding noise within bid-ask spreads and reconstruct the surface. A stable construction should produce local volatility surfaces that differ by at most a few percentage points. Large sensitivity indicates insufficient regularization.

!!! example "Construction Diagnostic"
    After constructing the local volatility surface for SPX options, a typical diagnostic summary might show:

    | Metric | Value | Acceptable Range |
    |--------|-------|-----------------|
    | $\sigma_{\text{loc}}$ range | 8%--65% | 1%--200% |
    | Repricing RMSE (IV) | 0.12 vol pts | < 0.5 vol pts |
    | Negative $\sigma_{\text{loc}}^2$ points | 0 | 0 |
    | Max $|\Delta\sigma_{\text{loc}}|$ under noise | 2.1% | < 5% |

    All metrics are within acceptable bounds, indicating a reliable construction.

## From $(K, T)$ to $(S, t)$

### Coordinate Transformation

Dupire's formula produces $\sigma_{\text{loc}}(K, T)$ — the local volatility as a function of strike and maturity. For PDE pricing and Monte Carlo simulation, we need $\sigma_{\text{loc}}(S, t)$ — the local volatility as a function of spot and time.

For a European option evaluated at $t = 0$ with current spot $S_0$, the two are related by a simple relabeling: the strike $K$ in Dupire's formula plays the role of the future spot $S$, and the maturity $T$ plays the role of the future time $t$:

$$
\sigma_{\text{loc}}(S, t) = \sigma_{\text{loc}}(K = S, T = t)
$$

This identification holds because Dupire's formula gives the instantaneous volatility the diffusion has when it reaches level $K$ at time $T$.

### Grid Mapping

When the Dupire surface is computed on a $(K, T)$ grid and the FDM or Monte Carlo scheme uses an $(S, t)$ grid, interpolation is required. The same bilinear or bicubic interpolation used within each framework applies.

## Summary

Local volatility surface construction transforms market data into a usable function $\sigma_{\text{loc}}(S, t)$ through a multi-stage pipeline:

1. **Input:** Smoothed, arbitrage-free call price or implied volatility surface (from interpolation and smoothing)
2. **Numerical differentiation:** Compute $\partial_T C$, $\partial_K C$, $\partial_{KK} C$ via finite differences or analytic derivatives of parametric models
3. **Dupire's formula:** Apply in price space or implied volatility space to obtain $\sigma_{\text{loc}}^2(K, T)$
4. **Regularization:** Enforce smoothness, positivity, and boundedness to handle ill-conditioning
5. **Validation:** Reprice vanilla options to verify consistency, check for negative values and spikes
6. **Coordinate mapping:** Convert from $(K, T)$ to $(S, t)$ for use in pricing engines

The quality of the local volatility surface depends critically on the quality of the input data and the smoothing step. Garbage in, garbage out -- no amount of regularization can compensate for fundamentally flawed input data.

---

## Exercises

**Exercise 1.** Given a smooth call price surface with $C(100, 1) = 10.45$, $C(105, 1) = 7.80$, $C(95, 1) = 13.60$, $C(100, 0.9) = 9.90$, $C(100, 1.1) = 10.95$, and parameters $r = 3\%$, $q = 1\%$, compute the local volatility $\sigma_{\text{loc}}(100, 1)$ using Dupire's formula with centered finite differences. Use $\Delta K = 5$ and $\Delta T = 0.1$.

---

**Exercise 2.** The Gatheral-Jacquier formula expresses local volatility in terms of implied volatility derivatives. Explain why this formulation is often more numerically stable than differentiating call prices directly. Under what conditions does it avoid finite differences entirely?

---

**Exercise 3.** Consider the total variance formulation of Dupire's formula:

$$
\sigma_{\text{loc}}^2 = \frac{\partial_T w}{\left(1 - \frac{y}{w}\partial_y w\right)^2 - \frac{1}{4}(\partial_y w)^2\left(\frac{1}{w} + \frac{1}{4}\right) + \frac{1}{2}\partial_{yy} w}
$$

Verify that when the total variance surface is flat ($w(y, T) = \sigma_0^2 T$, independent of $y$), the formula correctly gives $\sigma_{\text{loc}} = \sigma_0$.

---

**Exercise 4.** Tikhonov regularization adds penalty terms $\lambda_1 \int\!\!\int (\partial_K \sigma_{\text{loc}})^2 \, dK\,dT + \lambda_2 \int\!\!\int (\partial_T \sigma_{\text{loc}})^2 \, dK\,dT$ to the objective function. Explain the effect of increasing $\lambda_1$ relative to $\lambda_2$. In what market scenario (e.g., steep skew vs flat skew, sparse vs dense maturities) would you choose a larger $\lambda_2$?

---

**Exercise 5.** After constructing a local volatility surface, the repricing test yields an RMSE of 2.5 implied volatility points. List three possible causes of this large repricing error and for each cause describe a corrective action.

---

**Exercise 6.** Explain the coordinate transformation from $(K, T)$ to $(S, t)$ in the context of Dupire's formula. Why is it valid to set $\sigma_{\text{loc}}(S, t) = \sigma_{\text{loc}}(K = S, T = t)$? Under what circumstances does this simple relabeling fail, and what additional steps are needed?

---

**Exercise 7.** Using the SVI parametrization $w(y) = a + b(\rho(y-m) + \sqrt{(y-m)^2 + \sigma^2})$, compute the analytic first and second derivatives $\partial_y w$ and $\partial_{yy} w$. Verify that $\partial_{yy} w > 0$ for all $y$, which guarantees the butterfly no-arbitrage condition is not violated by the convexity term alone.
