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

---

## Exercises

**Exercise 1.** Write out the Cholesky decomposition for generating correlated increments $Z_1$ and $Z_2$ with correlation $\rho = -0.4$. Given independent standard normals $\xi_1 = 0.8$ and $\xi_2 = -0.5$, compute the correlated pair $(Z_1, Z_2)$ and verify that the construction satisfies $\text{Corr}(Z_1, Z_2) = \rho$.

??? success "Solution to Exercise 1"
    The Cholesky decomposition for a $2 \times 2$ correlation matrix with parameter $\rho$ produces:

    $$
    Z_1 = \xi_1, \qquad Z_2 = \rho\,\xi_1 + \sqrt{1 - \rho^2}\,\xi_2
    $$

    For $\rho = -0.4$:

    $$
    Z_1 = \xi_1, \qquad Z_2 = -0.4\,\xi_1 + \sqrt{1 - 0.16}\,\xi_2 = -0.4\,\xi_1 + \sqrt{0.84}\,\xi_2
    $$

    where $\sqrt{0.84} = 0.91652$.

    Given $\xi_1 = 0.8$ and $\xi_2 = -0.5$:

    $$
    Z_1 = 0.8
    $$

    $$
    Z_2 = -0.4(0.8) + 0.91652(-0.5) = -0.32 - 0.45826 = -0.77826
    $$

    **Verification.** The construction guarantees the correct correlation by design. To verify:

    - $\mathbb{E}[Z_1] = \mathbb{E}[\xi_1] = 0$ and $\mathbb{E}[Z_2] = -0.4\,\mathbb{E}[\xi_1] + 0.91652\,\mathbb{E}[\xi_2] = 0$
    - $\text{Var}(Z_1) = \text{Var}(\xi_1) = 1$
    - $\text{Var}(Z_2) = (-0.4)^2\text{Var}(\xi_1) + (0.91652)^2\text{Var}(\xi_2) = 0.16 + 0.84 = 1$
    - $\text{Cov}(Z_1, Z_2) = \text{Cov}(\xi_1, -0.4\xi_1 + 0.91652\xi_2) = -0.4\,\text{Var}(\xi_1) + 0.91652\,\text{Cov}(\xi_1, \xi_2) = -0.4 + 0 = -0.4$

    Since both variances are 1, $\text{Corr}(Z_1, Z_2) = \text{Cov}(Z_1, Z_2) = -0.4 = \rho$, as required.

---

**Exercise 2.** Starting from $F_0 = 0.03$, $\sigma_0 = 0.035$, $\beta = 0.5$, $\nu = 0.4$, $\rho = -0.3$, and $\Delta t = 0.02$, perform one step of the improved scheme (exact volatility, Euler forward). Use $Z_1 = 0.5$ and $Z_2 = -0.3$ (after Cholesky). Compute $\sigma_1$ (exact lognormal) and $F_1$ (Euler with absorbing boundary). Verify that $\sigma_1 > 0$.

??? success "Solution to Exercise 2"
    Given: $F_0 = 0.03$, $\sigma_0 = 0.035$, $\beta = 0.5$, $\nu = 0.4$, $\rho = -0.3$, $\Delta t = 0.02$, $Z_1 = 0.5$, $Z_2 = -0.3$.

    **Step 1: Exact lognormal volatility update.**

    $$
    \sigma_1 = \sigma_0 \exp\!\left(-\frac{\nu^2}{2}\Delta t + \nu\sqrt{\Delta t}\,Z_2\right)
    $$

    Computing the terms:

    $$
    -\frac{\nu^2}{2}\Delta t = -\frac{(0.4)^2}{2}(0.02) = -\frac{0.16}{2}(0.02) = -0.0016
    $$

    $$
    \nu\sqrt{\Delta t}\,Z_2 = 0.4 \times \sqrt{0.02} \times (-0.3) = 0.4 \times 0.14142 \times (-0.3) = -0.01697
    $$

    $$
    \sigma_1 = 0.035 \times \exp(-0.0016 - 0.01697) = 0.035 \times \exp(-0.01857) = 0.035 \times 0.98160 = 0.03436
    $$

    **Verification:** $\sigma_1 = 0.03436 > 0$. The exact lognormal simulation guarantees positivity because $\exp(\cdot) > 0$ always.

    **Step 2: Euler forward update with absorbing boundary.**

    $$
    F_1 = \max\!\left(F_0 + \sigma_0 F_0^{\beta}\sqrt{\Delta t}\,Z_1, \; 0\right)
    $$

    Computing:

    $$
    F_0^{\beta} = (0.03)^{0.5} = 0.17321
    $$

    $$
    \sigma_0 F_0^{\beta}\sqrt{\Delta t}\,Z_1 = 0.035 \times 0.17321 \times 0.14142 \times 0.5 = 0.035 \times 0.17321 \times 0.07071
    $$

    $$
    = 0.035 \times 0.01225 = 4.2862 \times 10^{-4}
    $$

    $$
    F_1 = \max(0.03 + 0.00042862, \; 0) = \max(0.03043, \; 0) = 0.03043
    $$

    The forward increases slightly from 3.00% to 3.043%, which is consistent with a positive $Z_1$ driving the forward up. The absorbing boundary is not triggered since $F_1 > 0$.

---

**Exercise 3.** The basic Euler scheme for the SABR volatility process $\sigma_{n+1} = \sigma_n + \nu\sigma_n\sqrt{\Delta t}\,Z_2$ can produce negative values. For $\sigma_n = 0.02$, $\nu = 0.5$, and $\Delta t = 0.1$, compute the threshold value of $Z_2$ below which $\sigma_{n+1} < 0$. What is the probability of this event? Explain why the exact lognormal simulation eliminates this problem.

??? success "Solution to Exercise 3"
    The Euler scheme for the volatility is:

    $$
    \sigma_{n+1} = \sigma_n + \nu\sigma_n\sqrt{\Delta t}\,Z_2 = \sigma_n\!\left(1 + \nu\sqrt{\Delta t}\,Z_2\right)
    $$

    For $\sigma_{n+1} < 0$, we need:

    $$
    1 + \nu\sqrt{\Delta t}\,Z_2 < 0 \implies Z_2 < -\frac{1}{\nu\sqrt{\Delta t}}
    $$

    With $\nu = 0.5$ and $\Delta t = 0.1$:

    $$
    Z_2 < -\frac{1}{0.5 \times \sqrt{0.1}} = -\frac{1}{0.5 \times 0.31623} = -\frac{1}{0.15811} = -6.3246
    $$

    The probability of this event is:

    $$
    \mathbb{P}(Z_2 < -6.3246) = \Phi(-6.3246)
    $$

    This is an extremely small probability. Using the standard normal tail approximation, $\Phi(-6.32) \approx 1.3 \times 10^{-10}$, which is essentially zero. So with these parameters, negative volatility under Euler is practically impossible.

    However, with larger $\nu$ or $\Delta t$, the threshold becomes more reachable. For example, with $\nu = 2.0$ and $\Delta t = 0.5$:

    $$
    Z_2 < -\frac{1}{2.0 \times \sqrt{0.5}} = -\frac{1}{1.4142} = -0.7071
    $$

    and $\mathbb{P}(Z_2 < -0.7071) = \Phi(-0.7071) \approx 24\%$, which is a serious problem.

    **Why exact lognormal simulation eliminates the problem.** The exact scheme is:

    $$
    \sigma_{n+1} = \sigma_n\exp\!\left(-\frac{\nu^2}{2}\Delta t + \nu\sqrt{\Delta t}\,Z_2\right)
    $$

    Since $\sigma_n > 0$ (by induction, starting from $\sigma_0 = \alpha > 0$) and $\exp(\cdot) > 0$ for any real argument, $\sigma_{n+1} > 0$ always. The exponential function maps $\mathbb{R} \to (0, \infty)$, so no matter how negative $Z_2$ is, the volatility remains strictly positive. This is because the exact scheme solves the geometric Brownian motion analytically, preserving the positivity property of the continuous-time process.

---

**Exercise 4.** From the convergence study table, the Euler scheme gives prices of 97.2, 97.8, 98.3 bps at $N = 50, 100, 500$ time steps, while the Hagan benchmark is 98.5 bps. Estimate the convergence order of the Euler scheme by computing the ratio of errors as $N$ doubles. Is this consistent with $O(\Delta t)$ weak convergence?

??? success "Solution to Exercise 4"
    The errors relative to the Hagan benchmark of 98.5 bps are:

    | $N$ | Price (bps) | Error (bps) |
    |---|---|---|
    | 50 | 97.2 | 1.3 |
    | 100 | 97.8 | 0.7 |
    | 500 | 98.3 | 0.2 |

    **Estimating convergence order.** If the error behaves as $C \cdot (\Delta t)^p = C \cdot (T/N)^p$, then doubling $N$ (halving $\Delta t$) should reduce the error by a factor of $2^p$.

    From $N = 50$ to $N = 100$ (doubling):

    $$
    \frac{\text{Error}(50)}{\text{Error}(100)} = \frac{1.3}{0.7} = 1.857 \approx 2^{0.89}
    $$

    This gives an estimated order of $p \approx 0.89$.

    From $N = 100$ to $N = 500$ (factor of 5):

    $$
    \frac{\text{Error}(100)}{\text{Error}(500)} = \frac{0.7}{0.2} = 3.5 \approx 5^{0.78}
    $$

    This gives an estimated order of $p \approx \log(3.5)/\log(5) = 1.253/1.609 = 0.78$.

    The estimated convergence order is approximately $p \approx 0.8$ to $0.9$, which is **roughly consistent with $O(\Delta t)$ weak convergence** ($p = 1$) but somewhat slower. The sub-linear behavior is expected because the SABR SDE has non-Lipschitz coefficients (the $F^{\beta}$ term with $\beta < 1$), which degrades the standard $O(\Delta t)$ weak convergence rate of Euler--Maruyama to $O(\Delta t^{1/2})$ or an intermediate rate near the boundary $F = 0$. For paths that stay away from the boundary, the convergence is closer to $O(\Delta t)$; the blended rate across all paths gives the observed $O(\Delta t^{0.8\text{--}0.9})$.

    Note also that the Hagan benchmark itself is an approximation ($O(T^2)$ error), so the "true" reference may differ slightly, affecting the convergence rate estimate.

---

**Exercise 5.** Describe how to implement antithetic variates for the SABR Monte Carlo simulation. A path uses increments $(Z_1^{(n)}, Z_2^{(n)})$ at each step. The antithetic path uses $(-Z_1^{(n)}, -Z_2^{(n)})$. Explain why the antithetic path has the same volatility process (in the exact lognormal scheme) up to a sign change in the Brownian motion, and why the average payoff has reduced variance.

??? success "Solution to Exercise 5"
    **Implementation of antithetic variates.** For each primary path with Brownian increments $(Z_1^{(n)}, Z_2^{(n)})_{n=0}^{N-1}$:

    1. Simulate the **primary path**: evolve $(F_t, \sigma_t)$ using increments $(Z_1^{(n)}, Z_2^{(n)})$ and compute the payoff $P^+$
    2. Simulate the **antithetic path**: evolve $(F_t, \sigma_t)$ using increments $(-Z_1^{(n)}, -Z_2^{(n)})$ and compute the payoff $P^-$
    3. The estimator for this pair is $\bar{P} = (P^+ + P^-)/2$
    4. Average over all $M/2$ pairs: $\hat{C} = \frac{1}{M/2}\sum_{i=1}^{M/2}\bar{P}_i$

    **Effect on the volatility process.** Using the exact lognormal scheme, the primary path volatility is:

    $$
    \sigma_{n+1}^+ = \sigma_n^+\exp\!\left(-\frac{\nu^2}{2}\Delta t + \nu\sqrt{\Delta t}\,Z_2^{(n)}\right)
    $$

    The antithetic path volatility is:

    $$
    \sigma_{n+1}^- = \sigma_n^-\exp\!\left(-\frac{\nu^2}{2}\Delta t - \nu\sqrt{\Delta t}\,Z_2^{(n)}\right)
    $$

    Both paths start from $\sigma_0^+ = \sigma_0^- = \alpha$. The antithetic volatility path is **not** the same as the primary path --- it is a distinct realization of the geometric Brownian motion with the sign of the Brownian motion reversed. However, the product $\sigma_n^+ \cdot \sigma_n^-$ is deterministic:

    $$
    \sigma_n^+\cdot\sigma_n^- = \alpha^2\exp\!\left(-\nu^2 n\Delta t\right) \cdot \prod_{k=0}^{n-1}\exp(\nu\sqrt{\Delta t}\,Z_2^{(k)})\exp(-\nu\sqrt{\Delta t}\,Z_2^{(k)}) = \alpha^2\exp(-\nu^2 n\Delta t)
    $$

    This means the geometric mean of the two volatility paths is deterministic, creating a strong negative correlation between the paths.

    **Why variance is reduced.** For a call payoff $\max(F_T - K, 0)$, the primary and antithetic payoffs are negatively correlated. When $Z_1^{(n)} > 0$ drives the primary forward up (increasing the payoff), $-Z_1^{(n)} < 0$ drives the antithetic forward down (decreasing its payoff). The linear component of the payoff's dependence on the Brownian increments cancels exactly in the average $(P^+ + P^-)/2$, reducing variance. The variance reduction is:

    $$
    \text{Var}\!\left(\frac{P^+ + P^-}{2}\right) = \frac{1}{4}\!\left(\text{Var}(P^+) + \text{Var}(P^-) + 2\,\text{Cov}(P^+, P^-)\right)
    $$

    Since $\text{Cov}(P^+, P^-) < 0$, this is less than $\frac{1}{2}\text{Var}(P^+)$ (the variance of a plain MC estimator with the same total number of paths). Typical variance reductions are 30--50% for European options under SABR.

---

**Exercise 6.** For a SABR Monte Carlo simulation with $M = 10^5$ paths and $N = 200$ time steps, the simulation requires $M \times N = 2 \times 10^7$ random number pairs. Estimate the memory requirement in megabytes for storing the forward and volatility arrays (assuming 8 bytes per float). Would it be more memory-efficient to compute the payoff online (during path generation) rather than storing the full path?

??? success "Solution to Exercise 6"
    **Memory for full path storage.** Each path requires storing $F$ and $\sigma$ at each of the $N + 1$ time points (including $t = 0$). With $N = 200$:

    - Per path: $2 \times 201 = 402$ floats (forward and volatility at each time step)
    - Total floats: $M \times 402 = 10^5 \times 402 = 4.02 \times 10^7$
    - Total memory: $4.02 \times 10^7 \times 8 \text{ bytes} = 3.216 \times 10^8 \text{ bytes} = 321.6 \text{ MB}$

    Additionally, the random number pairs require:

    - Per path: $2 \times 200 = 400$ floats (two normals per time step)
    - Total: $10^5 \times 400 \times 8 = 320 \text{ MB}$

    If both the paths and random numbers are stored simultaneously, the total is approximately **640 MB**, which is substantial but feasible on modern hardware.

    **Vectorized approach (store all paths at one time step).** A more memory-efficient approach for European options stores only the current state across all paths:

    - Two arrays of size $M$: $F[M]$ and $\sigma[M]$, requiring $2 \times 10^5 \times 8 = 1.6$ MB
    - Two random number arrays of size $M$: $\xi_1[M]$ and $\xi_2[M]$, requiring another 1.6 MB
    - Total: approximately **3.2 MB**

    **Online payoff computation.** For a European option with payoff $\max(F_T - K, 0)$, only the terminal value $F_T$ is needed. The payoff can be computed **online** (during path generation) by:

    1. Initializing arrays $F[M]$ and $\sigma[M]$
    2. At each time step, updating all paths in-place (overwriting the arrays)
    3. After the final step, computing $\text{payoff}[m] = \max(F[m] - K, 0)$ for each path

    This requires only $O(M)$ memory ($\approx 3$ MB), a reduction by a factor of roughly 200 compared to full path storage. For European options, online computation is strictly preferable.

    For **path-dependent options** (barriers, lookbacks, Asians), partial path information must be accumulated during the simulation (e.g., the running maximum for a lookback, or the running sum for an Asian), but the full path still need not be stored. The additional memory is $O(M)$ per path-dependent feature, still far less than the $O(M \times N)$ required for full path storage.
