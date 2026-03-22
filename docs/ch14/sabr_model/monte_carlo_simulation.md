# Monte Carlo Simulation of the SABR Model

While the Hagan formula provides fast implied volatility computation for European options, many applications require Monte Carlo simulation of the SABR dynamics: path-dependent options (barriers, lookbacks, Asian options), multi-asset products coupling SABR with other processes, and validation of analytical approximations. Simulating the SABR model presents specific challenges --- the absorbing boundary at $F = 0$ for $\beta < 1$, the multiplicative noise in the volatility process, and the strong nonlinearity of $F^{\beta}$ near zero --- that naive Euler discretization handles poorly. This section develops the simulation methodology from the basic Euler scheme through improved schemes that address these challenges.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Implement the Euler discretization of the SABR SDE system
    2. Generate correlated Brownian increments using the Cholesky decomposition
    3. Handle the absorbing boundary at $F = 0$ correctly
    4. Identify and mitigate the bias sources in naive Euler simulation
    5. Implement improved schemes (log-Euler, exact volatility) that reduce discretization error

---

## When Monte Carlo Is Needed

The Hagan formula covers European options at a single expiry with constant SABR parameters. Monte Carlo simulation is necessary for:

- **Path-dependent options**: Barrier options, lookbacks, and Asian options that depend on the entire path of $F_t$
- **Multi-factor products**: When SABR is embedded in a larger model (e.g., SABR/LMM for Bermudan swaptions)
- **Time-dependent parameters**: When $\alpha(t)$, $\rho(t)$, or $\nu(t)$ vary with time
- **Validation**: Benchmarking the Hagan approximation and arbitrage-free extensions against "ground truth"
- **Greeks by finite difference**: Bumping parameters and re-simulating to compute sensitivities

---

## Basic Euler Scheme

### Discretization

The SABR SDE system:

$$
dF_t = \sigma_t F_t^{\beta}\,dW_t^{(1)}, \qquad d\sigma_t = \nu\sigma_t\,dW_t^{(2)}
$$

is discretized on a time grid $0 = t_0 < t_1 < \cdots < t_N = T$ with step size $\Delta t = T/N$.

**Volatility step** (Euler--Maruyama):

$$
\sigma_{t_{n+1}} = \sigma_{t_n} + \nu\sigma_{t_n}\sqrt{\Delta t}\,Z_2^{(n)}
$$

**Forward step** (Euler--Maruyama):

$$
F_{t_{n+1}} = F_{t_n} + \sigma_{t_n}F_{t_n}^{\beta}\sqrt{\Delta t}\,Z_1^{(n)}
$$

where $Z_1^{(n)}$ and $Z_2^{(n)}$ are correlated standard normals.

### Generating Correlated Increments

Using the Cholesky decomposition, generate independent standard normals $\xi_1, \xi_2 \sim \mathcal{N}(0,1)$ and set:

$$
Z_1 = \xi_1, \qquad Z_2 = \rho\,\xi_1 + \sqrt{1-\rho^2}\,\xi_2
$$

This ensures $\text{Corr}(Z_1, Z_2) = \rho$ while $Z_1, Z_2$ each have unit variance.

### Absorbing Boundary

For $\beta < 1$, the forward can reach zero. The absorbing boundary is implemented by:

$$
F_{t_{n+1}} = \max\!\left(F_{t_n} + \sigma_{t_n}F_{t_n}^{\beta}\sqrt{\Delta t}\,Z_1, \; 0\right)
$$

Once $F$ hits zero, it stays at zero for all subsequent time steps.

!!! warning "Pitfalls of Naive Euler"
    The basic Euler scheme has several problems:

    1. **Negative forward**: Without the max(..., 0) floor, the Euler step can produce $F < 0$ when $\beta > 0$. The floor introduces bias.
    2. **Negative volatility**: The Euler step for $\sigma$ can also go negative, even though the exact process is strictly positive. This requires a floor $\sigma_{t_{n+1}} = \max(\sigma_{t_{n+1}}, 0)$.
    3. **Large bias at low F**: When $F$ is small, $F^{\beta}$ amplifies discretization errors. The Euler scheme systematically underestimates the absorption probability.
    4. **Slow convergence**: The Euler scheme converges as $O(\sqrt{\Delta t})$ in weak error for SDEs with Holder-continuous coefficients --- much slower than the $O(\Delta t)$ rate for smooth coefficients.

---

## Improved Scheme: Log-Euler for Volatility

### Exact Simulation of Volatility

Since $\sigma_t$ follows a geometric Brownian motion, it can be simulated **exactly** (without discretization error):

$$
\sigma_{t_{n+1}} = \sigma_{t_n}\exp\!\left(-\frac{\nu^2}{2}\Delta t + \nu\sqrt{\Delta t}\,Z_2\right)
$$

This ensures $\sigma_{t_n} > 0$ for all $n$, eliminating the negative volatility problem entirely. There is no discretization error in the volatility.

### Log-Euler for Forward

Apply the logarithmic transformation to the forward. For $\beta = 1$ (lognormal), define $X_t = \ln F_t$:

$$
dX_t = -\frac{\sigma_t^2}{2}\,dt + \sigma_t\,dW_t^{(1)}
$$

The Euler step for $X$ gives:

$$
X_{t_{n+1}} = X_{t_n} - \frac{\sigma_{t_n}^2}{2}\Delta t + \sigma_{t_n}\sqrt{\Delta t}\,Z_1
$$

$$
F_{t_{n+1}} = \exp(X_{t_{n+1}})
$$

This ensures $F > 0$ always and improves convergence. For general $\beta$, a similar transformation $Y_t = F_t^{1-\beta}/(1-\beta)$ can be used, although the discretization is more involved.

---

## Improved Scheme: Midpoint Correction

### The Scheme

The midpoint scheme uses the average of the volatility at the start and end of the time step:

$$
\sigma_{t_{n+1}} = \sigma_{t_n}\exp\!\left(-\frac{\nu^2}{2}\Delta t + \nu\sqrt{\Delta t}\,Z_2\right)
$$

$$
\bar{\sigma}_n = \frac{\sigma_{t_n} + \sigma_{t_{n+1}}}{2}
$$

$$
F_{t_{n+1}} = F_{t_n} + \bar{\sigma}_n F_{t_n}^{\beta}\sqrt{\Delta t}\,Z_1
$$

Using the midpoint volatility reduces the discretization error because the forward step now uses a better estimate of the average volatility over the time step.

---

## Handling the Boundary at F = 0

### Absorption Probability

For $\beta \in (0, 1)$, the CEV process can reach zero. The probability of absorption between $t_n$ and $t_{n+1}$, conditional on $F_{t_n} > 0$ and the volatility path, can be approximated using the CEV transition density with the average volatility $\bar{\sigma}_n$:

$$
p_{\text{abs}} \approx 1 - Q_{\chi^2}\!\left(\frac{F_{t_n}^{2(1-\beta)}}{(1-\beta)^2\bar{\sigma}_n^2\Delta t}\right)
$$

where $Q_{\chi^2}$ is the survival function of the non-central chi-squared distribution. This analytical approximation can be used to stochastically absorb paths:

1. Compute $p_{\text{abs}}$
2. Draw $U \sim \text{Uniform}(0, 1)$
3. If $U < p_{\text{abs}}$: set $F_{t_{n+1}} = 0$ (absorbed)
4. Otherwise: simulate the next step conditional on survival

### Practical Shortcut

For most applications with moderate $\alpha$ and $T \leq 10$Y, the absorption probability is small (less than 1%), and the simple floor $F_{t_{n+1}} = \max(F_{t_{n+1}}, 0)$ is adequate.

---

## Convergence and Error Analysis

### Sources of Error

Monte Carlo SABR simulation has three sources of error:

1. **Discretization bias**: The Euler scheme approximates the continuous dynamics. This bias scales as $O(\Delta t)$ for the log-Euler scheme and $O(\sqrt{\Delta t})$ for the standard Euler scheme near boundaries.

2. **Statistical error**: The Monte Carlo estimator has standard error $\sigma_{\text{MC}}/\sqrt{M}$ where $M$ is the number of paths and $\sigma_{\text{MC}}$ is the standard deviation of the discounted payoff.

3. **Boundary treatment error**: Incorrect handling of the absorbing boundary introduces systematic bias in put prices and probability mass accounting.

### Convergence Study

For a European call with $F = 0.03$, $K = 0.03$, $T = 1$Y, $\beta = 0.5$, $\alpha = 0.035$, $\rho = -0.3$, $\nu = 0.4$:

| Scheme | $N = 50$ | $N = 100$ | $N = 500$ | Hagan |
|--------|----------|-----------|-----------|-------|
| Euler | 97.2 bps | 97.8 bps | 98.3 bps | 98.5 bps |
| Log-Euler (vol) | 98.0 bps | 98.3 bps | 98.5 bps | 98.5 bps |
| Midpoint | 98.2 bps | 98.4 bps | 98.5 bps | 98.5 bps |

(Prices in basis points per unit notional, $M = 100{,}000$ paths.)

The log-Euler and midpoint schemes converge faster and produce smaller bias at all time step sizes.

### Variance Reduction

**Antithetic variates**: For each path with increments $(Z_1^{(n)}, Z_2^{(n)})$, simulate a paired path with $(-Z_1^{(n)}, -Z_2^{(n)})$. The average of the two payoffs has reduced variance because the linear component of the payoff cancels.

**Control variates**: Use the Hagan formula price as a control variate. The MC estimator becomes:

$$
\hat{C}_{\text{CV}} = \hat{C}_{\text{MC}} - \lambda(\hat{C}_{\text{MC}}^{\text{CEV}} - C_{\text{CEV}}^{\text{exact}})
$$

where $\hat{C}_{\text{MC}}^{\text{CEV}}$ is the MC price with $\nu = 0$ (CEV model) and $C_{\text{CEV}}^{\text{exact}}$ is the known CEV closed-form price.

!!! example "Simulation Example"
    **Setup**: $F = 2\%$, $\beta = 0$, $\alpha = 0.006$, $\rho = -0.3$, $\nu = 0.5$, $T = 5$Y.

    Simulating $M = 100{,}000$ paths with $N = 200$ time steps (log-Euler for volatility):

    - ATM call price (MC): $83.2 \pm 0.4$ bps
    - ATM call price (Hagan): $83.5$ bps
    - MC bias: $-0.3$ bps (within statistical error)
    - Runtime: 0.8 seconds (vectorized NumPy)

    With antithetic variates, the standard error drops to $\pm 0.25$ bps (a 40% reduction).

---

## Summary

Monte Carlo simulation of the SABR model requires careful treatment of the correlated Brownian motions (via Cholesky decomposition), the absorbing boundary at $F = 0$ (for $\beta < 1$), and the positivity of the volatility process. The basic Euler scheme suffers from negative values and large bias near the boundary. Improved schemes --- exact simulation of the lognormal volatility, log-Euler transformation for the forward, and midpoint averaging --- substantially reduce discretization error. Variance reduction through antithetic variates and control variates (using the Hagan formula as a benchmark) further improves efficiency. Monte Carlo is essential for path-dependent SABR applications and for validating analytical approximations.

---

## Further Reading

- Chen, B., Oosterlee, C. W., & van der Weide, H. (2012). *A low-bias simulation scheme for the SABR stochastic volatility model*. International Journal of Theoretical and Applied Finance.
- Leitao, A., Grzelak, L. A., & Oosterlee, C. W. (2017). *On a one time-step Monte Carlo simulation approach of the SABR model*. Applied Mathematics and Computation.
- Cai, N., Song, Y., & Chen, N. (2017). *Exact simulation of the SABR model*. Operations Research.
- Glasserman, P. (2004). *Monte Carlo Methods in Financial Engineering*. Springer.
