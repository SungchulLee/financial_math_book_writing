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

---

## Exercises

**Exercise 1.** Implement the exact simulation algorithm for $S_T$ under the Merton model. For $S_0 = 100$, $K = 100$, $T = 0.5$, $r = 0.05$, $\sigma = 0.20$, $\lambda = 1.0$, $\mu_J = -0.08$, $\sigma_J = 0.25$, price a European call using $M = 50{,}000$ paths. Compare your Monte Carlo estimate with the Merton series formula result.

??? success "Solution to Exercise 1"
    **Algorithm.** For each path $m = 1, \ldots, 50000$:

    1. Draw $Z \sim N(0, 1)$
    2. Draw $n \sim \text{Poisson}(\lambda T) = \text{Poisson}(0.5)$
    3. If $n > 0$, draw $J_1, \ldots, J_n \sim N(-0.08, 0.0625)$ and set $\mathcal{J} = \sum_{i=1}^n J_i$; else $\mathcal{J} = 0$
    4. Compute $S_T^{(m)} = 100 \exp[(0.09758 - 0.02) \times 0.5 + 0.20\sqrt{0.5}\,Z + \mathcal{J}]$

    where $\bar{k} = e^{-0.08 + 0.03125} - 1 \approx -0.04758$ and the drift term is $r - \lambda\bar{k} - \frac{1}{2}\sigma^2 = 0.05 + 0.04758 - 0.02 = 0.07758$.

    The Monte Carlo call price estimator is:

    $$
    \hat{C} = e^{-0.05 \times 0.5} \cdot \frac{1}{50000}\sum_{m=1}^{50000}\max(S_T^{(m)} - 100, 0)
    $$

    The standard error is $\text{SE} = e^{-rT}\hat{\sigma}_{\text{payoff}}/\sqrt{50000}$.

    For comparison, the Merton series formula gives an exact benchmark. The Monte Carlo estimate should agree with the series formula within approximately $\pm 2 \times \text{SE}$ (95% confidence interval). With $M = 50000$ paths, the standard error is typically around \$0.05--\$0.10, so the Monte Carlo and series formula estimates should differ by less than \$0.20.

---


**Exercise 2.** Explain why the exact simulation algorithm produces unbiased samples while the Euler-Maruyama scheme introduces discretization bias. For what types of payoffs (European, path-dependent, barrier) is exact simulation sufficient, and when must you use the Euler scheme?

??? success "Solution to Exercise 2"
    **Why exact simulation is unbiased.** The exact simulation algorithm draws $S_T$ directly from its exact distribution using the closed-form solution:

    $$
    S_T = S_0 \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)T + \sigma\sqrt{T}\,Z + \sum_{i=1}^{n}J_i\right]
    $$

    Since $Z$, $n$, and $\{J_i\}$ are sampled from their exact distributions, each $S_T^{(m)}$ is an exact draw from the terminal distribution. The Monte Carlo estimator $\hat{C} = e^{-rT}\frac{1}{M}\sum g(S_T^{(m)})$ is therefore unbiased for any payoff function $g$.

    **Why Euler-Maruyama introduces bias.** The Euler scheme approximates the continuous-time SDE at discrete time points. Between grid points, the scheme assumes a locally linear (or log-linear) evolution, which is only exact for the geometric Brownian motion component. The discretization introduces a systematic error of order $O(\Delta t)$ in the weak sense (option prices).

    **When each method is appropriate:**

    - **European options**: Exact simulation is sufficient and preferred because the payoff depends only on $S_T$. No time stepping is needed.
    - **Path-dependent options** (Asian, lookback): The Euler scheme is required because the payoff depends on intermediate values $S_{t_1}, S_{t_2}, \ldots, S_{t_N}$. Exact simulation gives only the terminal value.
    - **Barrier options**: The Euler scheme is needed, but with care: the continuous-time barrier crossing between grid points must be accounted for (Brownian bridge correction) to avoid bias from discrete monitoring.

---


**Exercise 3.** The antithetic variate method negates the Brownian increments $\{Z_k\}$ but keeps the same jump draws. Explain why the jump component limits the variance reduction factor compared to the pure diffusion case. Estimate the expected variance reduction for a European call when jumps contribute 40% of the total variance.

??? success "Solution to Exercise 3"
    **Why jumps limit variance reduction.** Antithetic variates replace $Z$ with $-Z$ for the Brownian component but keep the same Poisson draws $n$ and log-jump sizes $\{J_i\}$. The variance of the estimator decomposes as:

    $$
    \operatorname{Var}(\hat{C}_{\text{AV}}) = \frac{1}{4}\operatorname{Var}\bigl(g(S_T^+) + g(S_T^-)\bigr)
    $$

    If the payoff were a function of $Z$ alone (pure diffusion), the negative correlation between $g(S_T^+)$ and $g(S_T^-)$ would reduce the variance significantly. However, the jump component is common to both paths:

    $$
    S_T^{\pm} = S_0 \exp\!\left[\text{drift} \pm \sigma\sqrt{T}|Z| + \sum J_i\right]
    $$

    The jump sum $\sum J_i$ is identical in both paths, so the randomness from jumps is not reduced at all by the antithetic technique.

    **Estimating variance reduction when jumps contribute 40% of total variance.** The total variance of $\ln S_T$ is $V_{\text{total}} = V_{\text{diff}} + V_{\text{jump}}$ where $V_{\text{jump}} = 0.4\,V_{\text{total}}$ and $V_{\text{diff}} = 0.6\,V_{\text{total}}$.

    Antithetic variates eliminate (roughly) the variance from the diffusion component, reducing it by a factor close to $1 - \rho$ where $\rho \approx 1$ for the diffusion part. In the ideal case, the antithetic method eliminates the diffusion variance entirely, leaving only the jump variance:

    $$
    \text{Variance reduction ratio} \approx \frac{V_{\text{jump}}}{V_{\text{total}}} = 0.4
    $$

    So the variance is reduced to about 40% of the original (a 60% reduction). This is less than the nearly 100% reduction achievable for pure diffusion. In practice, the payoff nonlinearity reduces the efficiency further, giving a typical variance reduction of 30--50% as stated in the text.

---


**Exercise 4.** Describe the control variate estimator $\hat{C}_{\text{CV}} = \hat{C}_{\text{exotic}} - \beta(\hat{C}_{\text{vanilla}} - C_{\text{Merton}})$ where $C_{\text{Merton}}$ is the exact series price. (a) Explain why the optimal $\beta^*$ equals $\text{Cov}(g_{\text{exotic}}, g_{\text{vanilla}})/\text{Var}(g_{\text{vanilla}})$. (b) For an Asian call under Merton dynamics, would you expect the European call or the geometric average Asian call to be a better control variate?

??? success "Solution to Exercise 4"
    **(a) Derivation of optimal $\beta^*$.** The control variate estimator is:

    $$
    \hat{C}_{\text{CV}} = \hat{C}_{\text{exotic}} - \beta(\hat{C}_{\text{vanilla}} - C_{\text{Merton}})
    $$

    Its variance is:

    $$
    \operatorname{Var}(\hat{C}_{\text{CV}}) = \operatorname{Var}(\hat{C}_{\text{exotic}}) - 2\beta\operatorname{Cov}(\hat{C}_{\text{exotic}}, \hat{C}_{\text{vanilla}}) + \beta^2\operatorname{Var}(\hat{C}_{\text{vanilla}})
    $$

    Minimizing over $\beta$ by taking the derivative and setting it to zero:

    $$
    \frac{d}{d\beta}\operatorname{Var}(\hat{C}_{\text{CV}}) = -2\operatorname{Cov}(\hat{C}_{\text{exotic}}, \hat{C}_{\text{vanilla}}) + 2\beta\operatorname{Var}(\hat{C}_{\text{vanilla}}) = 0
    $$

    $$
    \beta^* = \frac{\operatorname{Cov}(\hat{C}_{\text{exotic}}, \hat{C}_{\text{vanilla}})}{\operatorname{Var}(\hat{C}_{\text{vanilla}})} = \frac{\operatorname{Cov}(g_{\text{exotic}}, g_{\text{vanilla}})}{\operatorname{Var}(g_{\text{vanilla}})}
    $$

    The minimum variance is:

    $$
    \operatorname{Var}(\hat{C}_{\text{CV}})^* = \operatorname{Var}(\hat{C}_{\text{exotic}})(1 - \rho^2)
    $$

    where $\rho$ is the correlation between the exotic and vanilla payoffs. Higher correlation means greater variance reduction.

    **(b) Choice of control variate for an Asian call.** The geometric average Asian call has a closed-form price (under GBM, and approximately under jump-diffusion), making it a natural candidate. However, the European call is more commonly used because:

    - Its exact Merton price is readily available from the series formula
    - Its payoff $\max(S_T - K, 0)$ is highly correlated with the arithmetic Asian payoff since both depend on the terminal price and the overall path level

    The geometric average Asian call would be a better control variate if its exact price is available, because its payoff structure (average of prices along the path) more closely resembles the arithmetic Asian payoff, yielding higher correlation $\rho$ and thus greater variance reduction. In practice, if a closed-form geometric Asian price is available under the Merton model, it should be preferred; otherwise, the European call with the exact Merton series price is the practical choice.

---


**Exercise 5.** For the Euler-Maruyama scheme, explain the guideline $\lambda\Delta t \ll 1$. (a) What is the probability of two or more jumps in a single time step when $\lambda = 2$ and $\Delta t = 1/252$? (b) Why does the log-Euler scheme $S_{t+\Delta t} = S_t \exp[\ldots]$ preserve positivity while the additive Euler scheme can produce negative prices?

??? success "Solution to Exercise 5"
    The guideline $\lambda\Delta t \ll 1$ ensures that within each time step, the probability of more than one jump is negligible. This simplifies the simulation (at most zero or one jump per step) and avoids accumulation of discretization errors from multiple-jump steps.

    **(a) Probability of two or more jumps.** For $\lambda = 2$ and $\Delta t = 1/252$, the expected jumps per step are $\lambda\Delta t = 2/252 \approx 0.00794$. The number of jumps follows $\text{Poisson}(0.00794)$:

    $$
    \mathbb{P}(n \geq 2) = 1 - \mathbb{P}(n = 0) - \mathbb{P}(n = 1)
    $$

    $$
    \mathbb{P}(n = 0) = e^{-0.00794} \approx 0.99209
    $$

    $$
    \mathbb{P}(n = 1) = 0.00794 \times e^{-0.00794} \approx 0.00788
    $$

    $$
    \mathbb{P}(n \geq 2) = 1 - 0.99209 - 0.00788 \approx 0.0000315 \approx 3.15 \times 10^{-5}
    $$

    This is very small, so the guideline $\lambda\Delta t \ll 1$ is comfortably satisfied with daily time steps even for $\lambda = 2$.

    **(b) Positivity of the log-Euler scheme.** The log-Euler update is:

    $$
    S_{t+\Delta t} = S_t \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\,Z + \mathcal{J}\right]
    $$

    Since $S_t > 0$ and the exponential function is always positive ($e^x > 0$ for all $x \in \mathbb{R}$), we have $S_{t+\Delta t} > 0$ regardless of the values of $Z$ and $\mathcal{J}$. Positivity is guaranteed by construction.

    The additive Euler scheme updates as:

    $$
    S_{t+\Delta t} = S_t + S_t(r - \lambda\bar{k})\Delta t + S_t\sigma\sqrt{\Delta t}\,Z + S_t\sum(Y_i - 1)
    $$

    For a large negative draw of $Z$ (e.g., $Z = -5$) or a severe downward jump ($Y_i \ll 1$), the right-hand side can become negative. This is an artifact of the linear discretization that does not respect the multiplicative structure of geometric Brownian motion.
