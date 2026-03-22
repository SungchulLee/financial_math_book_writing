# Monte Carlo Simulation

The Merton series formula provides exact (up to truncation) European option prices, but many practical applications require Monte Carlo simulation: path-dependent payoffs (barriers, Asians, lookbacks), early exercise features (American options via Longstaff-Schwartz), and risk metrics (VaR, CVA) that depend on the full path distribution. This section develops simulation algorithms for the Merton jump-diffusion, covering both exact sampling and Euler discretization, along with variance reduction techniques that can reduce computational cost by orders of magnitude.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Implement exact simulation of Merton jump-diffusion paths
    2. Formulate the Euler-Maruyama scheme with jumps and analyze its convergence
    3. Apply variance reduction techniques (antithetic variates, control variates)
    4. Estimate Monte Carlo standard errors and determine the required number of paths

---

## Exact Simulation

### The Key Insight

The explicit solution of the Merton SDE is:

$$
S_T = S_0 \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)T + \sigma W_T\right]\prod_{i=1}^{N_T}Y_i
$$

Since $W_T$, $N_T$, and $\{Y_i\}$ are independent, we can simulate each component separately without any time discretization. This produces exact samples from the terminal distribution $S_T$.

### Algorithm

!!! info "Algorithm: Exact Simulation of $S_T$"
    For each path $m = 1, \ldots, M$:

    1. Draw $Z \sim N(0, 1)$ (diffusion component)
    2. Draw $n \sim \text{Poisson}(\lambda T)$ (number of jumps)
    3. If $n > 0$, draw $J_1, \ldots, J_n \sim N(\mu_J, \sigma_J^2)$ (log-jump sizes)
    4. Compute the terminal price:

    $$
    S_T^{(m)} = S_0 \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)T + \sigma\sqrt{T}\,Z + \sum_{i=1}^{n}J_i\right]
    $$

This algorithm requires no time stepping and produces an unbiased sample from the exact distribution. It is suitable for pricing European options and other terminal-value claims.

### European Option Pricing

The Monte Carlo estimator for a European call is:

$$
\hat{C} = e^{-rT}\frac{1}{M}\sum_{m=1}^{M}\max(S_T^{(m)} - K, 0)
$$

with standard error:

$$
\text{SE} = \frac{\hat{\sigma}_{\text{payoff}}}{\sqrt{M}}
$$

where $\hat{\sigma}_{\text{payoff}}$ is the sample standard deviation of the discounted payoffs.

---

## Path Simulation via Euler-Maruyama

### When Full Paths Are Needed

Exact terminal simulation is insufficient for path-dependent payoffs. The Euler-Maruyama scheme discretizes the SDE on a time grid $0 = t_0 < t_1 < \cdots < t_N = T$ with step size $\Delta t = T/N$.

### The Scheme

!!! info "Algorithm: Euler-Maruyama with Jumps"
    Set $S_0^{(m)} = S_0$. For each step $k = 0, 1, \ldots, N-1$:

    1. Draw $Z_k \sim N(0, 1)$ (diffusion increment)
    2. Draw $n_k \sim \text{Poisson}(\lambda\Delta t)$ (jumps in $[t_k, t_{k+1}]$)
    3. If $n_k > 0$, draw $J_1, \ldots, J_{n_k} \sim N(\mu_J, \sigma_J^2)$ and set $\mathcal{J}_k = \sum_{i=1}^{n_k}J_i$; otherwise $\mathcal{J}_k = 0$
    4. Update:

    $$
    S_{t_{k+1}}^{(m)} = S_{t_k}^{(m)}\exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\,Z_k + \mathcal{J}_k\right]
    $$

!!! warning "Use the Log-Euler Scheme"
    The multiplicative update above (exponential of increments) preserves positivity of $S_t$ and is more accurate than the additive Euler scheme $S_{t_{k+1}} = S_{t_k} + \mu S_{t_k}\Delta t + \sigma S_{t_k}\sqrt{\Delta t}Z_k + \ldots$, which can produce negative prices. The log-Euler scheme is exact for the diffusion part (same as the exact solution applied to each step).

### Convergence

The strong convergence order of the Euler-Maruyama scheme for jump-diffusion processes is:

$$
\mathbb{E}[\sup_{0 \leq t \leq T}|S_t - S_t^{(\Delta t)}|^2]^{1/2} = O(\sqrt{\Delta t})
$$

This is the same $O(\sqrt{\Delta t})$ strong order as for pure diffusions. The weak convergence order (relevant for option pricing) is $O(\Delta t)$.

!!! tip "Step Size Considerations"
    For the Merton model, a common guideline is to choose $\Delta t$ small enough that $\lambda\Delta t \ll 1$, so the probability of multiple jumps in a single step is negligible. With $\lambda = 1$ (one jump per year), $\Delta t = 1/252$ (daily) gives $\lambda\Delta t \approx 0.004$, and $\mathbb{P}(n_k \geq 2) \approx 8 \times 10^{-6}$.

---

## Variance Reduction

### Antithetic Variates

For each path with diffusion draws $\{Z_k\}$, generate a twin path with $\{-Z_k\}$ (same jump draws). The antithetic estimator is:

$$
\hat{C}_{\text{AV}} = \frac{1}{2M}\sum_{m=1}^{M}\left[e^{-rT}g(S_T^{(m,+)}) + e^{-rT}g(S_T^{(m,-)})\right]
$$

where $g$ is the payoff function and $S_T^{(m,\pm)}$ denote the original and antithetic paths.

**Variance reduction factor.** For a European call under pure diffusion, antithetic variates reduce variance by about 50%. Under jump-diffusion, the reduction is typically 30--50% because the jump component (which is not negated) contributes unhedged variance.

### Control Variates

The Merton series formula provides an exact benchmark for European options, making it an ideal control variate for path-dependent pricing.

!!! info "Proposition: Control Variate Estimator"
    Let $g_{\text{exotic}}$ and $g_{\text{vanilla}}$ be the exotic and vanilla payoffs evaluated on the same paths. Then

    $$
    \hat{C}_{\text{CV}} = \frac{1}{M}\sum_{m=1}^{M}e^{-rT}g_{\text{exotic}}^{(m)} - \beta\left[\frac{1}{M}\sum_{m=1}^{M}e^{-rT}g_{\text{vanilla}}^{(m)} - C_{\text{Merton}}\right]
    $$

    where $C_{\text{Merton}}$ is the exact price from the series formula and $\beta$ is the optimal control coefficient:

    $$
    \beta^* = \frac{\text{Cov}(g_{\text{exotic}}, g_{\text{vanilla}})}{\text{Var}(g_{\text{vanilla}})}
    $$

Control variates can reduce variance by factors of 10--100 when the exotic payoff is highly correlated with the vanilla payoff (e.g., Asian options).

### Importance Sampling

For deep OTM options, most simulated paths produce zero payoff. Importance sampling shifts the drift to make the option end in-the-money more frequently:

$$
S_T^{\text{IS}} = S_0 \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2 + \theta\sigma\right)T + \sigma\sqrt{T}Z + \mathcal{J}\right]
$$

with a likelihood ratio correction $e^{-\theta Z\sqrt{T} - \frac{1}{2}\theta^2 T}$. The optimal shift $\theta$ targets the region where the payoff is concentrated.

---

## Worked Example

!!! example "Monte Carlo Pricing of a European Call"
    **Parameters:** $S_0 = \$100$, $K = \$105$, $T = 0.5$, $r = 0.05$, $\sigma = 0.20$, $\lambda = 0.5$, $\mu_J = -0.10$, $\sigma_J = 0.30$.

    **Exact price** (Merton series, 20 terms): $C_{\text{Merton}} = \$5.83$

    **Monte Carlo results** ($M = 100{,}000$ paths):

    | Method | Estimate | Std Error | Relative Error |
    |--------|----------|-----------|----------------|
    | Plain MC | \$5.87 | \$0.065 | 1.11% |
    | Antithetic | \$5.85 | \$0.047 | 0.81% |
    | Control variate | \$5.833 | \$0.008 | 0.14% |

    The control variate estimator achieves a standard error 8 times smaller than plain Monte Carlo, equivalent to using 64 times as many paths.

    **Pseudocode for plain Monte Carlo:**

    ```
    for m = 1 to M:
        Z = randn()
        n = poisson(lambda * T)
        J = sum of n draws from N(mu_J, sigma_J^2)
        S_T = S0 * exp((r - lambda*kbar - 0.5*sigma^2)*T + sigma*sqrt(T)*Z + J)
        payoff[m] = max(S_T - K, 0)
    price = exp(-r*T) * mean(payoff)
    se = exp(-r*T) * std(payoff) / sqrt(M)
    ```

---

## Convergence Diagnostics

### Confidence Intervals

A 95% confidence interval for the option price is:

$$
\hat{C} \pm 1.96 \times \text{SE}
$$

For the standard error to be below a target $\epsilon$, the required number of paths is:

$$
M \geq \left(\frac{1.96 \times \hat{\sigma}_{\text{payoff}}}{\epsilon}\right)^2
$$

### Monitoring Convergence

!!! tip "Practical Tips"
    - Plot the running mean and running standard error as functions of the number of paths to check for convergence visually
    - Use batched estimators: divide $M$ paths into $B$ batches of size $M/B$, compute the price in each batch, and use the batch standard deviation to estimate SE
    - For path-dependent options, monitor the convergence of both the time discretization error (by doubling $N$) and the Monte Carlo error (by doubling $M$) separately

---

## Summary

Monte Carlo simulation of the Merton jump-diffusion generates paths by sampling Poisson-distributed jump counts and normally distributed jump sizes alongside the standard Brownian increments. Exact terminal simulation requires no time stepping and produces unbiased samples, while the log-Euler scheme provides full path dynamics at $O(\sqrt{\Delta t})$ strong convergence. Variance reduction through antithetic variates, control variates (using the exact Merton series price), and importance sampling can reduce computational cost by one to two orders of magnitude, making Monte Carlo practical for pricing path-dependent and early-exercise derivatives under jump-diffusion dynamics.
