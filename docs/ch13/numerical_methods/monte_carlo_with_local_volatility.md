# Monte Carlo with Local Volatility

While finite difference methods solve the local volatility PDE efficiently for European and simple barrier options, many exotic derivatives — path-dependent claims such as Asian options, lookback options, and autocallables — require Monte Carlo simulation. Under local volatility, the SDE

$$
dS_t = (r - q) S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t
$$

must be discretized with a volatility function that changes at every point in space and time. This section develops the discretization schemes, analyzes their convergence properties, and presents the variance reduction techniques that make Monte Carlo practical for local volatility pricing.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Discretize the local volatility SDE using Euler-Maruyama and Milstein schemes
    - Explain why the log-Euler scheme is preferred for multiplicative noise
    - Interpolate the local volatility surface during path simulation
    - Analyze the weak and strong convergence rates under local volatility
    - Apply variance reduction techniques (antithetic variates, control variates) in the local volatility setting

## Euler-Maruyama Scheme

### Direct Discretization

The simplest discretization of the local volatility SDE over a time step $\Delta t = t_{n+1} - t_n$ is the **Euler-Maruyama** scheme:

$$
S_{n+1} = S_n + (r - q) S_n \Delta t + \sigma_{\text{loc}}(S_n, t_n) S_n \sqrt{\Delta t} \, Z_n
$$

where $Z_n \sim \mathcal{N}(0, 1)$ are independent standard normal random variables.

This scheme is straightforward but has two drawbacks:

1. **Positivity:** There is no guarantee that $S_{n+1} > 0$. For large volatility and large $\Delta t$, the scheme can produce negative values.
2. **First-order accuracy:** The weak convergence rate is $O(\Delta t)$, requiring many time steps for accurate pricing.

### Log-Euler Scheme

A better approach applies Euler-Maruyama to $X_t = \ln S_t$. By Ito's lemma:

$$
dX_t = \left(r - q - \frac{1}{2}\sigma_{\text{loc}}^2(e^{X_t}, t)\right) dt + \sigma_{\text{loc}}(e^{X_t}, t) \, dW_t
$$

The Euler discretization of $X_t$ gives:

$$
X_{n+1} = X_n + \left(r - q - \frac{1}{2}\sigma_{\text{loc}}^2(e^{X_n}, t_n)\right) \Delta t + \sigma_{\text{loc}}(e^{X_n}, t_n) \sqrt{\Delta t} \, Z_n
$$

Exponentiating:

$$
S_{n+1} = S_n \exp\left[\left(r - q - \frac{1}{2}\sigma_n^2\right) \Delta t + \sigma_n \sqrt{\Delta t} \, Z_n\right]
$$

where $\sigma_n = \sigma_{\text{loc}}(S_n, t_n)$.

**Advantages of the log-Euler scheme:**

- $S_{n+1} > 0$ unconditionally (exponential of a real number is always positive)
- Exact for geometric Brownian motion ($\sigma$ constant)
- Same $O(\Delta t)$ weak convergence as direct Euler, but smaller error constants

!!! tip "The Log-Euler Scheme as Default"
    The log-Euler scheme should be the default choice for local volatility Monte Carlo. It preserves positivity automatically, matches the exact Black-Scholes dynamics when $\sigma_{\text{loc}}$ is constant, and requires no additional computational cost over direct Euler.

## Milstein Scheme

### Higher-Order Correction

The **Milstein scheme** adds a correction term that captures the curvature of the diffusion coefficient, improving the strong convergence from $O(\sqrt{\Delta t})$ to $O(\Delta t)$.

For the SDE $dS_t = \mu S_t \, dt + \sigma(S_t, t) S_t \, dW_t$ with $\mu = r - q$, the Milstein scheme is:

$$
S_{n+1} = S_n + \mu S_n \Delta t + \sigma_n S_n \sqrt{\Delta t} \, Z_n + \frac{1}{2}\sigma_n S_n \frac{\partial(\sigma S)}{\partial S}\bigg|_{S_n, t_n} \left((\sqrt{\Delta t} \, Z_n)^2 - \Delta t\right)
$$

The derivative of the diffusion function $a(S) = \sigma(S, t) S$ is:

$$
a'(S) = \sigma(S, t) + S \frac{\partial \sigma}{\partial S}(S, t)
$$

So the Milstein correction involves $\partial \sigma_{\text{loc}} / \partial S$, the spatial derivative of the local volatility surface.

### Practical Considerations

Computing $\partial \sigma_{\text{loc}} / \partial S$ at each simulation point requires either:

- **Finite differences:** $\frac{\partial \sigma}{\partial S} \approx \frac{\sigma(S + h, t) - \sigma(S - h, t)}{2h}$, requiring two additional surface lookups per step
- **Analytic derivatives:** If $\sigma_{\text{loc}}$ is stored as a parametric function or spline, differentiate analytically

The added cost and complexity of the Milstein scheme are often not justified for pricing (which depends on weak convergence), since Euler and Milstein have the same weak convergence rate $O(\Delta t)$. Milstein is more useful for:

- Hedging (Greeks) where strong convergence matters
- Coupling methods (e.g., multilevel Monte Carlo)

## Surface Interpolation During Simulation

### The Lookup Problem

At each time step and for each path, the scheme requires $\sigma_{\text{loc}}(S_n, t_n)$. The local volatility surface is typically stored on a finite grid $(K_i, T_j)$. Since $S_n$ and $t_n$ generally do not coincide with grid points, interpolation is needed at every evaluation.

For $N_{\text{paths}}$ paths with $N_{\text{steps}}$ time steps each, the total number of surface evaluations is:

$$
N_{\text{eval}} = N_{\text{paths}} \times N_{\text{steps}}
$$

With typical values $N_{\text{paths}} = 10^5$ to $10^6$ and $N_{\text{steps}} = 100$ to $1000$, this requires $10^7$ to $10^9$ interpolations.

### Interpolation Methods

**Bilinear interpolation:** For a regular grid, find the cell containing $(S_n, t_n)$ and interpolate:

$$
\sigma_{\text{loc}}(S, t) \approx (1 - u)(1 - v)\sigma_{i,j} + u(1 - v)\sigma_{i+1,j} + (1 - u)v\sigma_{i,j+1} + uv\sigma_{i+1,j+1}
$$

where $u = (S - K_i)/(K_{i+1} - K_i)$ and $v = (t - T_j)/(T_{j+1} - T_j)$. Bilinear interpolation is fast ($O(1)$ per lookup with grid indexing) but only $C^0$ continuous, which can introduce small jumps in the volatility along paths.

**Bicubic spline interpolation:** Provides $C^2$ continuity and smoother paths but is more expensive per evaluation. Pre-computing spline coefficients on the grid reduces the per-lookup cost to $O(1)$.

!!! warning "Boundary Handling"
    When a simulated path reaches a spot level outside the local volatility grid (either very high or very low), the interpolation must extrapolate. Common strategies:

    - **Flat extrapolation:** $\sigma_{\text{loc}}(S, t) = \sigma_{\text{loc}}(K_{\text{boundary}}, t)$ for $S$ beyond the grid
    - **Clamping:** Force $S$ to the nearest grid boundary for the volatility lookup
    - **Linear extrapolation:** Continue the edge gradient, but cap at $\sigma_{\max}$

    The choice affects the distribution of extreme paths and can impact exotic pricing, particularly for barrier options near the grid boundary.

## Convergence Analysis

### Weak Convergence

For pricing (computing expectations), **weak convergence** determines accuracy:

$$
|\mathbb{E}[f(S_T^{\Delta t})] - \mathbb{E}[f(S_T)]| \leq C_f \Delta t^{\beta}
$$

where $\beta$ is the weak order of convergence.

**Theorem 13.5.3** (Weak Convergence under Local Volatility)
If $\sigma_{\text{loc}}(S, t)$ is bounded, Lipschitz continuous in $S$ uniformly in $t$, and the payoff $f$ is a polynomial growth function, then:

- The Euler-Maruyama scheme has weak order $\beta = 1$
- The Milstein scheme has weak order $\beta = 1$
- Both require $\sigma_{\text{loc}} \in C^{2,1}$ (twice differentiable in $S$, once in $t$) for the full order

In practice, the weak convergence rate means that halving $\Delta t$ halves the discretization bias.

### Strong Convergence

For path-dependent quantities and coupling estimators, **strong convergence** matters:

$$
\mathbb{E}[|S_T^{\Delta t} - S_T|^2]^{1/2} \leq C \Delta t^{\gamma}
$$

- Euler-Maruyama: $\gamma = 1/2$ (strong order 0.5)
- Milstein: $\gamma = 1$ (strong order 1.0)

### Discretization Bias

The discretization bias for a European call under local volatility with the log-Euler scheme is approximately:

$$
\text{bias} \approx -\frac{\Delta t}{12}\mathbb{E}\left[\int_0^T \left(\sigma_{\text{loc}} \frac{\partial \sigma_{\text{loc}}}{\partial S} S\right)^2 dt\right]
$$

This bias is proportional to $\Delta t$ and to the gradient of the local volatility surface. Steep local volatility gradients (as occur near barriers or during high-skew regimes) increase the bias, requiring more time steps.

## Variance Reduction

### Antithetic Variates

Generate paths in pairs using $Z_n$ and $-Z_n$:

$$
S_{n+1}^{(+)} = S_n^{(+)} \exp\left[\left(r - q - \frac{\sigma_n^2}{2}\right)\Delta t + \sigma_n \sqrt{\Delta t} \, Z_n\right]
$$

$$
S_{n+1}^{(-)} = S_n^{(-)} \exp\left[\left(r - q - \frac{\sigma_n^2}{2}\right)\Delta t - \sigma_n \sqrt{\Delta t} \, Z_n\right]
$$

The estimator $\hat{C} = \frac{1}{2}(\Phi(S^{(+)}) + \Phi(S^{(-)}))$ reduces variance by exploiting the negative correlation between the two paths. Under local volatility, antithetic paths share the same volatility sequence (evaluated at different spots), so the correlation is slightly lower than under constant volatility. Typical variance reduction: 30--60% for vanilla options.

### Control Variates

Use a known benchmark to reduce variance. A natural control variate for local volatility pricing is the **Black-Scholes price** computed with ATM implied volatility $\sigma_0$:

$$
\hat{C}_{\text{CV}} = \hat{C}_{\text{LV}} - \beta\left(\hat{C}_{\text{BS}} - C_{\text{BS}}^{\text{exact}}\right)
$$

where $\hat{C}_{\text{LV}}$ is the Monte Carlo estimate under local volatility, $\hat{C}_{\text{BS}}$ is the Monte Carlo estimate under constant $\sigma_0$, $C_{\text{BS}}^{\text{exact}}$ is the closed-form Black-Scholes price, and $\beta$ is the optimal regression coefficient:

$$
\beta = \frac{\text{Cov}(\hat{C}_{\text{LV}}, \hat{C}_{\text{BS}})}{\text{Var}(\hat{C}_{\text{BS}})}
$$

The correlation between local vol and Black-Scholes paths is typically high (0.95+), yielding substantial variance reduction (5--20x for European options).

### Importance Sampling

For deep OTM options, importance sampling shifts the drift of the simulated paths to increase the probability of exercise:

$$
dX_t = \left(r - q - \frac{\sigma_n^2}{2} + \theta(t)\right) dt + \sigma_n \, dW_t
$$

where $\theta(t)$ is the drift shift. The payoff is weighted by the likelihood ratio:

$$
L = \exp\left(-\int_0^T \theta(t) \, dW_t - \frac{1}{2}\int_0^T \theta(t)^2 \, dt\right)
$$

The optimal $\theta(t)$ minimizes the second moment of the weighted payoff. Under local volatility, the optimal shift depends on the path-dependent volatility, making analytical solutions unavailable. Practical implementations use constant or piecewise-constant shifts determined by pilot simulations.

## Time-Stepping Considerations

### Adaptive Time Stepping

When $\sigma_{\text{loc}}(S, t)$ varies significantly across the domain, a uniform time step may be inefficient. **Adaptive time stepping** adjusts $\Delta t$ based on the local volatility:

$$
\Delta t_n = \min\left(\Delta t_{\max}, \frac{c}{\sigma_{\text{loc}}^2(S_n, t_n)}\right)
$$

where $c$ is a constant chosen so that the "variance per step" $\sigma_n^2 \Delta t_n$ remains roughly constant. This places more steps in high-volatility regions (where discretization error is largest) and fewer steps in low-volatility regions.

### Maturity Alignment

Time steps should align with the maturities of the local volatility surface to avoid interpolation errors. If the surface is specified at maturities $T_1, T_2, \ldots, T_p$, ensure that these times are included in the time grid.

For path-dependent options with observation dates (e.g., Asian options with monthly fixings), the fixing dates should also be included in the time grid.

!!! example "Pricing an Asian Option under Local Volatility"
    Consider a monthly-fixing arithmetic Asian call on the S&P 500 with strike $K = 4500$ and maturity $T = 1$ year. Using the log-Euler scheme with $N = 250$ time steps, $10^5$ paths, and antithetic variates:

    | Method | Price | Std Error | Time |
    |--------|-------|-----------|------|
    | Plain MC | 142.37 | 0.89 | 12.3s |
    | Antithetic | 142.51 | 0.62 | 13.1s |
    | Control variate (BS) | 142.44 | 0.18 | 14.7s |
    | Antithetic + CV | 142.46 | 0.14 | 15.2s |

    The control variate using a constant-volatility geometric Asian as benchmark reduces the standard error by a factor of 6, making the simulation practical with modest computational resources.

## Comparison with FDM

| Feature | FDM | Monte Carlo |
|---------|-----|-------------|
| European options | Efficient ($O(MN)$) | Less efficient |
| Path-dependent options | Difficult or impossible | Natural |
| High dimensions | Curse of dimensionality | Dimension-independent convergence |
| Greeks | Direct from grid | Requires bumping or pathwise/LR methods |
| Accuracy | Deterministic, controllable | Statistical, $O(1/\sqrt{N_{\text{paths}}})$ |
| Local vol interpolation | Once per grid point | Once per path per step |

For European options under local volatility, FDM is preferred. For exotic and path-dependent options, Monte Carlo is the primary tool. In practice, many desks use FDM for vanilla calibration and Greeks, and Monte Carlo for exotic pricing, both relying on the same local volatility surface.

## Summary

Monte Carlo simulation under local volatility requires careful treatment of the space-dependent diffusion coefficient:

1. The **log-Euler scheme** provides positivity-preserving, first-order weak convergence and should be the default discretization
2. The **Milstein scheme** improves strong convergence but requires the spatial derivative $\partial \sigma_{\text{loc}} / \partial S$, adding complexity
3. **Surface interpolation** at every time step and path dominates the per-step cost; efficient grid lookup and caching are essential
4. **Discretization bias** scales with $\Delta t$ and with the gradient of $\sigma_{\text{loc}}$, requiring more steps in steep-volatility regions
5. **Variance reduction** via antithetic variates and Black-Scholes control variates can reduce computational cost by an order of magnitude
6. The choice between FDM and Monte Carlo depends on the payoff structure: FDM for Europeans, Monte Carlo for path-dependent exotics

---

## Exercises

**Exercise 1.** Write out the log-Euler discretization step for the local volatility SDE. Starting from $S_n = 100$, $\sigma_{\text{loc}}(100, t_n) = 0.25$, $r = 3\%$, $q = 1\%$, $\Delta t = 0.01$, and $Z_n = 0.5$, compute $S_{n+1}$ using the log-Euler scheme. Verify that $S_{n+1} > 0$ regardless of the value of $Z_n$.

??? success "Solution to Exercise 1"
    The log-Euler discretization step is:

    $$
    S_{n+1} = S_n \exp\left[\left(r - q - \frac{1}{2}\sigma_n^2\right)\Delta t + \sigma_n \sqrt{\Delta t}\, Z_n\right]
    $$

    where $\sigma_n = \sigma_{\text{loc}}(S_n, t_n)$.

    With $S_n = 100$, $\sigma_n = 0.25$, $r = 0.03$, $q = 0.01$, $\Delta t = 0.01$, and $Z_n = 0.5$:

    **Drift term:**

    $$
    r - q - \frac{1}{2}\sigma_n^2 = 0.03 - 0.01 - \frac{1}{2}(0.0625) = 0.02 - 0.03125 = -0.01125
    $$

    **Exponent:**

    $$
    (-0.01125)(0.01) + 0.25\sqrt{0.01}(0.5) = -0.0001125 + 0.25(0.1)(0.5) = -0.0001125 + 0.0125 = 0.0123875
    $$

    **Result:**

    $$
    S_{n+1} = 100 \exp(0.0123875) = 100 \times 1.01246 = 101.246
    $$

    **Positivity verification:** The log-Euler scheme computes $S_{n+1} = S_n \exp(\cdot)$. Since $S_n > 0$ and the exponential function is strictly positive for any real argument, $S_{n+1} > 0$ regardless of the value of $Z_n$. Even for extreme draws (e.g., $Z_n = -10$), the exponent becomes a large negative number, but $\exp(\text{large negative}) > 0$ always. This is the fundamental advantage of the log-Euler scheme over the direct Euler scheme, which can produce negative values when $\sigma \sqrt{\Delta t} |Z_n| > 1$.

---

**Exercise 2.** The Milstein scheme for the local volatility SDE requires the derivative $\partial \sigma_{\text{loc}} / \partial S$. Suppose the local volatility surface is stored on a grid with spacing $\Delta S = 1$. Write the finite difference formula for $\partial \sigma_{\text{loc}} / \partial S$ at $(S_n, t_n)$ and estimate the additional computational cost per time step compared to the Euler scheme, for $N_{\text{paths}} = 10^5$.

??? success "Solution to Exercise 2"
    The centered finite difference for the spatial derivative of local volatility at $(S_n, t_n)$ with grid spacing $\Delta S = 1$ is:

    $$
    \frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S_n, t_n} \approx \frac{\sigma_{\text{loc}}(S_n + 1, t_n) - \sigma_{\text{loc}}(S_n - 1, t_n)}{2}
    $$

    This requires two additional lookups of the local volatility surface: one at $S_n + 1$ and one at $S_n - 1$, both at the same time $t_n$.

    **Computational cost comparison per time step:**

    For the Euler scheme, each path requires one surface evaluation per time step: $\sigma_{\text{loc}}(S_n, t_n)$. The total cost per time step is $N_{\text{paths}}$ lookups.

    For the Milstein scheme, each path requires three surface evaluations per time step: $\sigma_{\text{loc}}(S_n, t_n)$, $\sigma_{\text{loc}}(S_n + h, t_n)$, and $\sigma_{\text{loc}}(S_n - h, t_n)$. The total cost per time step is $3 N_{\text{paths}}$ lookups.

    With $N_{\text{paths}} = 10^5$, the Euler scheme requires $10^5$ lookups per time step, while Milstein requires $3 \times 10^5$ lookups per time step. The additional cost is $2 \times 10^5$ lookups per time step, a factor of 3 increase in surface evaluation cost. Since surface interpolation often dominates the per-step cost in local volatility Monte Carlo, this represents a significant overhead. This is one reason why Milstein is seldom used for pricing (where weak convergence suffices and both schemes are $O(\Delta t)$), though it is valuable for applications requiring strong convergence.

---

**Exercise 3.** Consider two interpolation methods for looking up $\sigma_{\text{loc}}(S_n, t_n)$ during simulation: bilinear interpolation ($C^0$ continuity) and bicubic spline interpolation ($C^2$ continuity). Explain how the lack of $C^1$ continuity in bilinear interpolation can affect simulated paths. In what type of exotic product would this difference be most significant?

??? success "Solution to Exercise 3"
    **Bilinear interpolation** ($C^0$ continuity) produces a local volatility function that is continuous but has discontinuous first derivatives along the grid lines of the stored surface. As a simulated path crosses a grid line in either the spot or time direction, the volatility experienced by the path changes slope abruptly.

    **Effect on simulated paths:** The discontinuity in the volatility gradient means the drift adjustment $-\frac{1}{2}\sigma^2$ in the log-Euler scheme also has a kink. Over many small time steps, these kinks introduce a systematic discretization bias that is absent with smoother interpolation. The paths effectively experience a slightly different drift near each grid line.

    **Bicubic spline interpolation** ($C^2$ continuity) eliminates these kinks, producing smooth volatility along each path. The gradient and curvature of the volatility surface are continuous, so the discretization error converges more smoothly with decreasing $\Delta t$.

    **Where the difference is most significant:** The difference matters most for path-dependent exotic products where the payoff is sensitive to the realized path of the underlying, particularly:

    - **Barrier options:** The payoff depends on whether the path crosses a specific level. Discontinuities in the volatility gradient near the barrier level can alter the probability of crossing, affecting the price.
    - **Lookback options:** The payoff depends on the running maximum or minimum, which is sensitive to the local behavior of the path, including small-scale volatility fluctuations.
    - **Autocallables and target redemption notes:** These products have path-dependent trigger conditions, and the kinks from bilinear interpolation can introduce artifacts in the trigger probability near grid lines.

    For plain vanilla European options, where pricing depends only on the terminal distribution, the impact of $C^0$ versus $C^2$ interpolation is typically small.

---

**Exercise 4.** A Monte Carlo simulation under local volatility with $10^5$ paths and 200 time steps produces a European call price of $\hat{C}_{\text{LV}} = 8.42$ with standard error 0.12. A parallel Black-Scholes simulation with the same paths yields $\hat{C}_{\text{BS}} = 8.15$, while the exact Black-Scholes price is $C_{\text{BS}}^{\text{exact}} = 8.20$. The estimated correlation between $\hat{C}_{\text{LV}}$ and $\hat{C}_{\text{BS}}$ is 0.97. Compute the control variate estimator $\hat{C}_{\text{CV}}$ and estimate the variance reduction factor.

??? success "Solution to Exercise 4"
    The control variate estimator is:

    $$
    \hat{C}_{\text{CV}} = \hat{C}_{\text{LV}} - \beta(\hat{C}_{\text{BS}} - C_{\text{BS}}^{\text{exact}})
    $$

    With correlation $\rho = 0.97$ between $\hat{C}_{\text{LV}}$ and $\hat{C}_{\text{BS}}$, the optimal $\beta$ is:

    $$
    \beta = \frac{\text{Cov}(\hat{C}_{\text{LV}}, \hat{C}_{\text{BS}})}{\text{Var}(\hat{C}_{\text{BS}})} = \rho \frac{\text{SD}(\hat{C}_{\text{LV}})}{\text{SD}(\hat{C}_{\text{BS}})}
    $$

    Since both simulations use the same number of paths, and assuming standard errors are proportional to standard deviations (both have the same $N_{\text{paths}}$), we can approximate $\beta \approx \rho \cdot \text{SE}_{\text{LV}} / \text{SE}_{\text{BS}}$. With similar variance structures, a reasonable approximation is $\beta \approx 1$ (since the local volatility and Black-Scholes prices are closely correlated and have similar magnitudes). Using $\beta = 1$ for simplicity:

    $$
    \hat{C}_{\text{CV}} = 8.42 - 1 \times (8.15 - 8.20) = 8.42 - (-0.05) = 8.47
    $$

    **Variance reduction factor:** The variance of the control variate estimator relative to the original is:

    $$
    \frac{\text{Var}(\hat{C}_{\text{CV}})}{\text{Var}(\hat{C}_{\text{LV}})} = 1 - \rho^2 = 1 - (0.97)^2 = 1 - 0.9409 = 0.0591
    $$

    The variance reduction factor is approximately $1/0.0591 \approx 16.9$, meaning the control variate reduces variance by roughly a factor of 17. Equivalently, the standard error is reduced by a factor of $\sqrt{16.9} \approx 4.1$, so the new standard error is approximately $0.12 / 4.1 \approx 0.029$.

---

**Exercise 5.** The discretization bias for the log-Euler scheme is approximately:

$$
\text{bias} \approx -\frac{\Delta t}{12}\mathbb{E}\left[\int_0^T \left(\sigma_{\text{loc}} \frac{\partial \sigma_{\text{loc}}}{\partial S} S\right)^2 dt\right]
$$

Explain why steep local volatility gradients (large $|\partial \sigma_{\text{loc}} / \partial S|$) increase the bias. For a local volatility surface with a skew of $\partial \sigma_{\text{loc}} / \partial S = -0.003$ near the money, estimate whether $\Delta t = 1/250$ (daily steps) is sufficient for a one-year European option, or whether finer stepping is needed.

??? success "Solution to Exercise 5"
    The discretization bias formula:

    $$
    \text{bias} \approx -\frac{\Delta t}{12}\mathbb{E}\left[\int_0^T \left(\sigma_{\text{loc}} \frac{\partial \sigma_{\text{loc}}}{\partial S} S\right)^2 dt\right]
    $$

    shows that the bias is proportional to $(\sigma_{\text{loc}} \cdot (\partial \sigma_{\text{loc}} / \partial S) \cdot S)^2$. A steep local volatility gradient (large $|\partial \sigma_{\text{loc}} / \partial S|$) increases this quantity quadratically. Intuitively, when the local volatility changes rapidly with spot, the Euler discretization "freezes" the volatility at $\sigma_{\text{loc}}(S_n, t_n)$ for the entire time step, whereas the true process samples a range of volatilities as $S$ moves during $[t_n, t_{n+1}]$. The steeper the gradient, the worse this "freezing" approximation.

    **Estimation for $\Delta t = 1/250$:** With $\partial \sigma_{\text{loc}} / \partial S = -0.003$ near ATM, $\sigma_{\text{loc}} \approx 0.20$ (typical), and $S \approx 100$:

    $$
    \sigma_{\text{loc}} \frac{\partial \sigma_{\text{loc}}}{\partial S} S = 0.20 \times (-0.003) \times 100 = -0.06
    $$

    $$
    \left(\sigma_{\text{loc}} \frac{\partial \sigma_{\text{loc}}}{\partial S} S\right)^2 = 0.0036
    $$

    The bias per unit time is approximately:

    $$
    |\text{bias}| \approx \frac{\Delta t}{12} \times 0.0036 \times T = \frac{(1/250)}{12} \times 0.0036 \times 1 \approx 1.2 \times 10^{-6}
    $$

    This is extremely small compared to typical option prices (order of magnitude $\$1$--$\$10$). For a one-year European option, $\Delta t = 1/250$ (daily steps) is more than sufficient. Even with a moderate skew of $-0.003$ per unit spot, the discretization bias is negligible. Finer stepping would only be needed for much steeper gradients (e.g., near a barrier where $|\partial \sigma_{\text{loc}}/\partial S|$ can be an order of magnitude larger) or for very high-precision requirements.

---

**Exercise 6.** Describe the adaptive time stepping rule $\Delta t_n = \min(\Delta t_{\max}, c / \sigma_{\text{loc}}^2(S_n, t_n))$. If the local volatility ranges from 10% to 60% across the grid, compute the ratio of the smallest to the largest time step size. What is the advantage of this approach over uniform time stepping for pricing a barrier option?

??? success "Solution to Exercise 6"
    The adaptive time stepping rule is:

    $$
    \Delta t_n = \min\left(\Delta t_{\max},\; \frac{c}{\sigma_{\text{loc}}^2(S_n, t_n)}\right)
    $$

    This sets the time step inversely proportional to the local variance, so that the "variance per step" $\sigma_n^2 \Delta t_n \approx c$ remains approximately constant across all steps.

    **Ratio of smallest to largest time step:** When $\sigma_{\text{loc}}$ ranges from 10% to 60%, the time steps (assuming neither hits $\Delta t_{\max}$) are:

    $$
    \Delta t_{\text{large}} = \frac{c}{\sigma_{\min}^2} = \frac{c}{(0.10)^2} = \frac{c}{0.01} = 100c
    $$

    $$
    \Delta t_{\text{small}} = \frac{c}{\sigma_{\max}^2} = \frac{c}{(0.60)^2} = \frac{c}{0.36} \approx 2.78c
    $$

    The ratio is:

    $$
    \frac{\Delta t_{\text{small}}}{\Delta t_{\text{large}}} = \frac{\sigma_{\min}^2}{\sigma_{\max}^2} = \frac{(0.10)^2}{(0.60)^2} = \frac{0.01}{0.36} = \frac{1}{36} \approx 0.028
    $$

    The smallest time step is 36 times smaller than the largest.

    **Advantage for barrier option pricing:** Barrier options are particularly sensitive to the behavior of the local volatility near the barrier level. If the local volatility is high near the barrier (as often occurs for OTM barriers in skewed markets), the discretization error is concentrated there. With uniform time stepping, the step size is the same everywhere and must be small enough for the worst case (highest volatility region), wasting computational effort in low-volatility regions. Adaptive stepping automatically places more (smaller) steps when the path is in the high-volatility region near the barrier, where accuracy matters most, and uses fewer (larger) steps when the path is far from the barrier in low-volatility regions. This achieves the same accuracy as uniform stepping with significantly fewer total steps, reducing computational cost.
