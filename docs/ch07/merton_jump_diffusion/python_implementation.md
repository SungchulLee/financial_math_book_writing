# Python Implementation Guide

This section provides a guided walkthrough of the Python module `python_implementation.py`, which implements the core computational methods for the Merton jump-diffusion model. The module encapsulates the `MertonJumpDiffusion` class with methods for exact path simulation, Monte Carlo pricing, and the Merton series formula. Each method corresponds directly to the mathematical formulations developed in the preceding sections.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand the class structure and parameter initialization of the implementation
    2. Connect each method to its mathematical foundation
    3. Use the module to price European options via both Monte Carlo and the series formula
    4. Compare Black-Scholes and Merton prices numerically

---

## Module Overview

The implementation file `python_implementation.py` is organized around a single class with the following structure:

| Component | Purpose |
|-----------|---------|
| `MertonJumpDiffusion.__init__` | Store parameters, compute adjusted drift |
| `_compute_adjusted_drift` | Calculate $r - \lambda\bar{k}$ |
| `simulate_paths` | Generate full price paths via Euler scheme |
| `option_price_monte_carlo` | Price European options by Monte Carlo |
| `option_price_series` | Price European options via Merton series formula |
| `compare_bs_merton` | Compare Black-Scholes and Merton prices |

---

## Parameter Initialization

### The Constructor

The class constructor stores the six model parameters and precomputes the adjusted drift.

The six parameters map directly to the Merton SDE:

$$
\frac{dS_t}{S_{t^-}} = (r - \lambda\bar{k})\,dt + \sigma\,dW_t + (Y - 1)\,dN_t
$$

| Code parameter | Math symbol | Description |
|---------------|-------------|-------------|
| `S0` | $S_0$ | Initial spot price |
| `r` | $r$ | Risk-free rate |
| `sigma` | $\sigma$ | Diffusion volatility |
| `lambda_jump` | $\lambda$ | Jump intensity |
| `mu_jump` | $\mu_J$ | Mean of $\ln Y$ |
| `sigma_jump` | $\sigma_J$ | Std dev of $\ln Y$ |

### The Drift Adjustment

The method `_compute_adjusted_drift` computes the compensator:

$$
\bar{k} = \mathbb{E}[Y - 1] = e^{\mu_J + \sigma_J^2/2} - 1
$$

and returns the adjusted drift $r - \lambda\bar{k}$. This ensures that the discounted price process is a martingale under the risk-neutral measure.

!!! tip "Why Precompute the Drift"
    The adjusted drift appears in every simulation step and every term of the series formula. Computing it once in the constructor avoids redundant exponentiation calls across potentially millions of path steps.

---

## Path Simulation

### Mathematical Basis

Recall (see [Monte Carlo Simulation § Path Simulation via Euler-Maruyama](monte_carlo_simulation.md#path-simulation-via-euler-maruyama)): the `simulate_paths` method implements the log-Euler scheme $S_{t+\Delta t} = S_t \exp[(r - \lambda\bar{k} - \tfrac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}\,Z + \sum_{i=1}^{n}\ln Y_i]$ with $Z \sim N(0,1)$ and $n \sim \text{Poisson}(\lambda\Delta t)$.

### Implementation Details

The method iterates over time steps. At each step:

1. **Brownian increment**: `dB = np.random.normal(0, np.sqrt(dt), num_paths)` generates $\sigma\sqrt{\Delta t}\,Z$ for all paths simultaneously
2. **Jump count**: `num_jumps = np.random.poisson(self.lambda_jump * dt, num_paths)` draws the number of jumps for each path
3. **Jump effect**: For paths with jumps, the method accumulates the log-normal jump multipliers $\prod Y_i = \exp(\sum \ln Y_i)$
4. **Price update**: The multiplicative update preserves positivity

!!! warning "Vectorization Note"
    The inner loop over paths (for computing jump effects) iterates one path at a time when jumps are present. For production code, this could be vectorized by pre-allocating the maximum number of jumps and using masked arrays. The current implementation prioritizes clarity over speed.

---

## Monte Carlo Pricing

### Mathematical Basis

The `option_price_monte_carlo` method estimates the discounted expected payoff:

$$
C \approx e^{-rT}\frac{1}{M}\sum_{m=1}^{M}\max(S_T^{(m)} - K, 0)
$$

with standard error $\text{SE} = \hat{\sigma}/\sqrt{M}$.

### Implementation Details

The method:

1. Calls `simulate_paths` to generate $M$ paths of length $N$ steps
2. Extracts the terminal values `paths[:, -1]`
3. Computes payoffs: `np.maximum(paths[:, -1] - K, 0)` for calls
4. Discounts and averages: `np.mean(discounted_payoffs)`
5. Returns both the price and the standard error as a tuple

The method accepts both `"call"` and `"put"` option types.

---

## Series Formula Pricing

### Mathematical Basis

Recall (see [Merton Series Formula](merton_series_formula.md#step-3-poisson-averaging)): $C = \sum_{n} w_n\,C_{\text{BS}}(S_0, K, T, r_n, \sigma_n)$ with $w_n = e^{-\lambda'T}(\lambda'T)^n/n!$, $\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$, and $r_n = r - \lambda\bar{k} + n\ln(1+\bar{k})/T$.

### Implementation Details

The method loops over the number of jumps $n = 0, 1, \ldots, n_{\max}$:

1. **Poisson weight**: Computed via `poisson.pmf(n, self.lambda_jump * T)` from SciPy
2. **Early termination**: If the weight falls below the tolerance, the loop breaks
3. **Conditional volatility**: $\sigma_n = \sqrt{\sigma^2 + n\sigma_J^2/T}$
4. **Conditional forward**: Adjusted for the cumulative jump effect
5. **Black-Scholes price**: Computed inline using the standard $d_1, d_2$ formulas and `norm.cdf`

!!! tip "Convergence Control"
    The `max_jumps` parameter (default 10) and `tolerance` parameter (default $10^{-10}$) control the truncation. For typical parameters ($\lambda T \leq 5$), 10 terms provide accuracy well beyond machine precision for 64-bit floating point.

---

## Comparing Black-Scholes and Merton

### The `compare_bs_merton` Function

This standalone function creates a `MertonJumpDiffusion` instance with user-specified parameters (or defaults) and returns a dictionary comparing:

- **Black-Scholes prices**: Computed directly from the $d_1, d_2$ formula
- **Merton series prices**: From `option_price_series`
- **Merton Monte Carlo prices**: From `option_price_monte_carlo` with 50,000 paths
- **Differences**: Merton series minus Black-Scholes

### Default Parameters

The default values illustrate a typical equity calibration:

| Parameter | Default | Interpretation |
|-----------|---------|----------------|
| $S_0$ | \$100 | At-the-money setup |
| $K$ | \$100 | ATM strike |
| $T$ | 1.0 | One-year maturity |
| $r$ | 5% | Risk-free rate |
| $\sigma$ | 20% | Diffusion volatility |
| $\lambda$ | 0.5 | One jump every two years |
| $\mu_J$ | $-0.10$ | 10% average downward jump |
| $\sigma_J$ | 0.30 | Moderate jump dispersion |

---

## Usage Example

!!! example "Running the Module"
    Executing the module directly produces a comparison table:

    ```
    Merton Jump-Diffusion vs Black-Scholes Pricing
    ============================================================

    Call Option:
      Black-Scholes:    10.450584
      Merton (Series):  11.353621
      Merton (MC):      11.38XXXX
      Difference:        0.903037

    Put Option:
      Black-Scholes:     5.572724
      Merton (Series):   6.475761
      Merton (MC):       6.50XXXX
      Difference:        0.903037
    ```

    The Monte Carlo values contain random noise (marked with `XXXX`) that varies between runs. The series formula values are deterministic and exact up to truncation.

    **Key observations:**

    - The Merton prices exceed Black-Scholes by approximately \$0.90 for both calls and puts
    - The call-put parity difference $C - P = S_0 - Ke^{-rT}$ is identical for both models (as it must be, since put-call parity is model-independent)
    - The Monte Carlo estimates agree with the series formula within standard error bounds

---

## Extending the Implementation

### Potential Enhancements

The current module provides a solid foundation that could be extended with:

- **Vectorized jump simulation**: Replace the per-path loop with a fully vectorized implementation
- **FFT pricing**: Add Carr-Madan pricing using the characteristic function
- **Implied volatility computation**: Add a method to compute the Merton implied volatility smile
- **Greeks computation**: Add finite-difference or analytical Greeks via the series formula
- **Calibration**: Add a least-squares calibration routine using `scipy.optimize`

Each extension maps directly to the mathematical content developed in the corresponding section of this chapter.

---

## Summary

The Python implementation encapsulates the Merton jump-diffusion model in a `MertonJumpDiffusion` class with methods for path simulation (log-Euler scheme with Poisson jumps), Monte Carlo pricing (discounted expected payoff), and the Merton series formula (Poisson-weighted Black-Scholes sum). The drift adjustment $r - \lambda\bar{k}$ is precomputed for efficiency. The module demonstrates the key theoretical result that Merton prices exceed Black-Scholes prices for the same diffusion volatility, reflecting the additional uncertainty introduced by the jump component. The companion function `compare_bs_merton` provides a ready-to-use comparison of the two models.

---

## Exercises

**Exercise 1.** The compensator is $\bar{k} = e^{\mu_J + \sigma_J^2/2} - 1$. For the default parameters $\mu_J = -0.10$ and $\sigma_J = 0.30$, compute $\bar{k}$ by hand and verify the adjusted drift $r - \lambda\bar{k}$ with $r = 0.05$ and $\lambda = 0.5$. Explain why $\bar{k} < 0$ when $\mu_J$ is sufficiently negative (downward jumps on average) and what this implies for the adjusted drift.

??? success "Solution to Exercise 1"
    With the default parameters $\mu_J = -0.10$, $\sigma_J = 0.30$, $r = 0.05$, $\lambda = 0.5$:

    **Computing $\bar{k}$:**

    $$
    \bar{k} = e^{\mu_J + \sigma_J^2/2} - 1 = e^{-0.10 + 0.045} - 1 = e^{-0.055} - 1 \approx -0.05351
    $$

    **Adjusted drift:**

    $$
    r - \lambda\bar{k} = 0.05 - 0.5 \times (-0.05351) = 0.05 + 0.02676 = 0.07676
    $$

    **Why $\bar{k} < 0$ when $\mu_J$ is sufficiently negative.** The compensator is $\bar{k} = e^{\mu_J + \sigma_J^2/2} - 1$. For $\bar{k} < 0$, we need $e^{\mu_J + \sigma_J^2/2} < 1$, which requires $\mu_J + \sigma_J^2/2 < 0$, i.e., $\mu_J < -\sigma_J^2/2$. With $\sigma_J = 0.30$, this means $\mu_J < -0.045$. Since $\mu_J = -0.10 < -0.045$, the condition is satisfied.

    **Implication for the adjusted drift.** When $\bar{k} < 0$, the term $-\lambda\bar{k} > 0$, so the adjusted drift $r - \lambda\bar{k} > r$. This means the continuous-time drift of $S_t$ between jumps is higher than the risk-free rate. This compensates for the fact that jumps on average reduce the price (since $\mathbb{E}[Y_i] < 1$ when $\bar{k} < 0$), ensuring that the overall expected return equals the risk-free rate under the risk-neutral measure.

---


**Exercise 2.** The log-Euler simulation step is $S_{t+\Delta t} = S_t \exp[(r - \lambda\bar{k} - \frac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}\,Z + \sum_{i=1}^{n}\ln Y_i]$ where $n \sim \text{Poisson}(\lambda\Delta t)$ and $\ln Y_i \sim N(\mu_J, \sigma_J^2)$. Show that when $n = 0$ (no jumps in the time step), this reduces to the standard log-Euler step for geometric Brownian motion. Then show that $\mathbb{E}[S_{t+\Delta t}/S_t] = e^{r\Delta t}$ by computing the expectation over both $Z$ and the jump component (using the tower property over $n$).

??? success "Solution to Exercise 2"
    **When $n = 0$.** The log-Euler step with no jumps reduces to:

    $$
    S_{t+\Delta t} = S_t \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\,Z\right]
    $$

    This is exactly the log-Euler step for geometric Brownian motion with drift $r - \lambda\bar{k}$ (the GBM drift is adjusted by the compensator, but the functional form is identical to standard GBM simulation).

    **Verifying $\mathbb{E}[S_{t+\Delta t}/S_t] = e^{r\Delta t}$.** Using the tower property, condition on the number of jumps $n$:

    $$
    \mathbb{E}\!\left[\frac{S_{t+\Delta t}}{S_t}\right] = \mathbb{E}\!\left[\exp\!\left(\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\,Z + \sum_{i=1}^{n}\ln Y_i\right)\right]
    $$

    The expectation over $Z \sim N(0,1)$ gives:

    $$
    \mathbb{E}\!\left[e^{\sigma\sqrt{\Delta t}\,Z}\right] = e^{\frac{1}{2}\sigma^2\Delta t}
    $$

    For the jump part, conditioning on $n \sim \text{Poisson}(\lambda\Delta t)$ and using independence:

    $$
    \mathbb{E}\!\left[\exp\!\left(\sum_{i=1}^{n}\ln Y_i\right)\right] = \mathbb{E}\!\left[\prod_{i=1}^{n} Y_i\right] = \sum_{n=0}^{\infty}\frac{(\lambda\Delta t)^n}{n!}e^{-\lambda\Delta t}\cdot(\mathbb{E}[Y])^n
    $$

    $$
    = e^{-\lambda\Delta t}\sum_{n=0}^{\infty}\frac{(\lambda\Delta t \cdot \mathbb{E}[Y])^n}{n!} = e^{-\lambda\Delta t}\cdot e^{\lambda\Delta t\,\mathbb{E}[Y]} = e^{\lambda\Delta t(\mathbb{E}[Y] - 1)} = e^{\lambda\bar{k}\Delta t}
    $$

    Combining all factors:

    $$
    \mathbb{E}\!\left[\frac{S_{t+\Delta t}}{S_t}\right] = e^{(r - \lambda\bar{k} - \frac{1}{2}\sigma^2)\Delta t} \cdot e^{\frac{1}{2}\sigma^2\Delta t} \cdot e^{\lambda\bar{k}\Delta t} = e^{r\Delta t}
    $$

    This confirms the martingale property: the expected gross return equals $e^{r\Delta t}$.

---


**Exercise 3.** The Merton series formula is $C = \sum_{n=0}^{\infty} \frac{e^{-\lambda'T}(\lambda'T)^n}{n!}\,C_{\text{BS}}(S_0, K, T, r_n, \sigma_n)$. For the default parameters, compute the first three terms ($n = 0, 1, 2$) of the series numerically. Use the Black-Scholes formula with $\sigma_0^2 = 0.04$, $r_0 \approx r - \lambda\bar{k}$ for $n = 0$, and the corresponding $\sigma_n^2$ and $r_n$ for $n = 1, 2$. Verify that the sum converges rapidly by comparing the $n = 0, 1, 2$ partial sums.

??? success "Solution to Exercise 3"
    With default parameters: $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.20$, $\lambda = 0.5$, $\mu_J = -0.10$, $\sigma_J = 0.30$.

    First, compute $\bar{k} = e^{-0.055} - 1 \approx -0.05351$ and $\lambda' = \lambda(1+\bar{k}) = 0.5 \times 0.94649 \approx 0.47325$.

    **Term $n = 0$:**

    $$
    w_0 = e^{-0.47325} \approx 0.6231
    $$

    $$
    \sigma_0 = 0.20, \quad r_0 = 0.05 + 0.5 \times 0.05351 = 0.07676
    $$

    $$
    d_1 = \frac{\ln(100/100) + (0.07676 + 0.02) \times 1}{0.20} = \frac{0.09676}{0.20} = 0.4838
    $$

    $$
    d_2 = 0.4838 - 0.20 = 0.2838
    $$

    $$
    C_{\text{BS}}^{(0)} = 100 e^{(0.07676 - 0.05)}N(0.4838) - 100 e^{-0.05}N(0.2838)
    $$

    $$
    \approx 100 \times 1.0271 \times 0.6857 - 100 \times 0.9512 \times 0.6117 \approx 70.41 - 58.19 = 12.22
    $$

    **Term $n = 1$:**

    $$
    w_1 = 0.47325 \times 0.6231 \approx 0.2949
    $$

    $$
    \sigma_1 = \sqrt{0.04 + 0.09} = \sqrt{0.13} \approx 0.3606
    $$

    $$
    r_1 = 0.07676 + \frac{\ln(0.94649)}{1} = 0.07676 - 0.05498 = 0.02178
    $$

    **Term $n = 2$:**

    $$
    w_2 = \frac{0.47325^2}{2} \times 0.6231 \approx 0.0698
    $$

    $$
    \sigma_2 = \sqrt{0.04 + 0.18} = \sqrt{0.22} \approx 0.4690
    $$

    $$
    r_2 = 0.07676 + 2 \times (-0.05498) = 0.07676 - 0.10996 = -0.03320
    $$

    Computing $C_{\text{BS}}^{(1)}$ and $C_{\text{BS}}^{(2)}$ with these parameters and forming the partial sums:

    - After $n = 0$: $0.6231 \times 12.22 \approx 7.62$
    - After $n = 1$: $7.62 + 0.2949 \times C_{\text{BS}}^{(1)} \approx 7.62 + 3.16 = 10.78$
    - After $n = 2$: $10.78 + 0.0698 \times C_{\text{BS}}^{(2)} \approx 10.78 + 0.53 = 11.31$

    The series converges rapidly: the $n = 0$ term accounts for about 67% of the total price, adding $n = 1$ brings it to about 95%, and $n = 2$ brings it to about 99.5%. The full series sum (with all remaining terms) converges to approximately \$11.35.

---


**Exercise 4.** The output shows that the Merton call price (\$11.35) exceeds the Black-Scholes call price (\$10.45) by approximately \$0.90, and the same difference holds for puts. Explain why the difference is identical for calls and puts by invoking put-call parity. Then explain economically why jump risk increases option prices: consider the effect of jumps on the tails of the return distribution and the convexity of option payoffs.

??? success "Solution to Exercise 4"
    **Why the difference is the same for calls and puts.** Put-call parity states:

    $$
    C - P = S_0 - Ke^{-rT}
    $$

    This is model-independent (it follows from the absence of arbitrage alone). Let $C_M$, $P_M$ denote Merton prices and $C_{BS}$, $P_{BS}$ denote Black-Scholes prices. Then:

    $$
    C_M - P_M = S_0 - Ke^{-rT} = C_{BS} - P_{BS}
    $$

    Rearranging: $C_M - C_{BS} = P_M - P_{BS}$. The dollar difference between Merton and Black-Scholes is identical for calls and puts because both models satisfy the same put-call parity constraint.

    **Economic explanation of why jumps increase option prices.** The jump component introduces additional uncertainty in the terminal price $S_T$. This affects option prices through two mechanisms:

    1. **Increased variance (heavier tails).** The total variance of log-returns under Merton is $\sigma^2 + \lambda(\sigma_J^2 + \mu_J^2) > \sigma^2$. Since option payoffs are convex functions of $S_T$, Jensen's inequality implies that greater dispersion in $S_T$ increases the expected payoff $\mathbb{E}[\max(S_T - K, 0)]$.

    2. **Non-Gaussian tail behavior.** The Merton return distribution has heavier tails than the normal distribution (excess kurtosis $> 0$). This increases the probability of extreme outcomes, which are precisely the scenarios where options have large payoffs. The convexity of option payoffs means that the gain from extreme moves exceeding the strike outweighs the probability-weighted cost of moves in the opposite direction.

    Together, these effects mean that any option (call or put) is worth more under the Merton model than under Black-Scholes with the same diffusion volatility $\sigma$.

---


**Exercise 5.** The Monte Carlo standard error is $\text{SE} = \hat{\sigma}/\sqrt{M}$ where $\hat{\sigma}$ is the sample standard deviation of the discounted payoffs and $M$ is the number of paths. For $M = 50{,}000$ and a typical $\hat{\sigma} \approx 15$, estimate the standard error. How many paths would be needed to reduce the standard error below \$0.01? Propose a variance reduction technique (e.g., antithetic variates or control variates using the Black-Scholes price) and explain how it would reduce $\hat{\sigma}$.

??? success "Solution to Exercise 5"
    For $M = 50000$ and $\hat{\sigma} \approx 15$:

    $$
    \text{SE} = \frac{15}{\sqrt{50000}} = \frac{15}{223.6} \approx \$0.067
    $$

    **Paths needed for SE $< \$0.01$:**

    $$
    M \geq \left(\frac{15}{0.01}\right)^2 = 1500^2 = 2{,}250{,}000
    $$

    Approximately 2.25 million paths are required, which is 45 times the original sample size.

    **Variance reduction via control variates.** Use the exact Merton series price $C_{\text{Merton}}$ as a control variate:

    $$
    \hat{C}_{\text{CV}} = \hat{C}_{\text{MC}} - \beta\left(\hat{C}_{\text{vanilla,MC}} - C_{\text{Merton}}\right)
    $$

    where $\hat{C}_{\text{vanilla,MC}}$ is the Monte Carlo estimate of the same European option (evaluated on the same paths). Since the control is the exact same payoff, $\rho = 1$ and the variance reduction is theoretically perfect for European options. In practice, this is used when pricing exotic options: simulate both the exotic and vanilla payoffs on the same paths, and use the known Merton price to correct the bias.

    **Antithetic variates** reduce $\hat{\sigma}$ by exploiting the negative correlation between $g(S_T^+)$ and $g(S_T^-)$. For the Merton model, the typical reduction is about 40%, giving $\hat{\sigma}_{\text{AV}} \approx 0.6 \times 15 = 9$, which reduces the required paths by a factor of $(15/9)^2 \approx 2.8$.

---


**Exercise 6.** Modify the `simulate_paths` logic conceptually to handle the case where $\Delta t$ is large enough that $\lambda\Delta t > 1$. In this regime, multiple jumps per time step are common. Show that the sum $\sum_{i=1}^n \ln Y_i$ for $n \sim \text{Poisson}(\lambda\Delta t)$ has mean $\lambda\Delta t\,\mu_J$ and variance $\lambda\Delta t(\sigma_J^2 + \mu_J^2) - (\lambda\Delta t\,\mu_J)^2$. Explain why the exact distribution of $S_{t+\Delta t}/S_t$ remains tractable (it is a mixture of log-normals), and why the simulation is exact regardless of the time step size.

??? success "Solution to Exercise 6"
    When $\lambda\Delta t > 1$, the expected number of jumps per step exceeds one, and multiple jumps per step are common.

    **Mean of the jump sum.** Conditional on $n \sim \text{Poisson}(\lambda\Delta t)$ jumps:

    $$
    \mathbb{E}\!\left[\sum_{i=1}^{n}\ln Y_i\right] = \mathbb{E}[n]\cdot\mathbb{E}[\ln Y_i] = \lambda\Delta t\,\mu_J
    $$

    **Variance of the jump sum.** By the law of total variance:

    $$
    \operatorname{Var}\!\left(\sum_{i=1}^{n}\ln Y_i\right) = \mathbb{E}[n]\sigma_J^2 + \operatorname{Var}(n)\mu_J^2 = \lambda\Delta t\,\sigma_J^2 + \lambda\Delta t\,\mu_J^2 = \lambda\Delta t(\sigma_J^2 + \mu_J^2)
    $$

    Note: the variance of $\sum_{i=1}^n \ln Y_i$ is $\lambda\Delta t(\sigma_J^2 + \mu_J^2)$, not $\lambda\Delta t(\sigma_J^2 + \mu_J^2) - (\lambda\Delta t\,\mu_J)^2$. The latter expression would be incorrect because the law of total variance already accounts for the random count correctly.

    **Why the distribution remains tractable.** Conditional on $n$ jumps, the total log-increment is:

    $$
    \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\,Z + \sum_{i=1}^{n}\ln Y_i
    $$

    Given $n$, this is a sum of a normal variable and $n$ normal variables, hence normal with mean $(r - \lambda\bar{k} - \frac{1}{2}\sigma^2)\Delta t + n\mu_J$ and variance $\sigma^2\Delta t + n\sigma_J^2$. Therefore $S_{t+\Delta t}/S_t$ is conditionally log-normal, and the unconditional distribution is a Poisson mixture of log-normals.

    **Why the simulation is exact.** The log-Euler step uses the exact same factorization as the closed-form solution applied to the interval $[t, t+\Delta t]$. The update $S_{t+\Delta t} = S_t\exp[\cdots]$ is not an approximation but the exact solution of the SDE on $[t, t+\Delta t]$ (because the SDE has constant coefficients when expressed in terms of $S_{t^-}$). This means the simulation is exact regardless of $\Delta t$, whether $\lambda\Delta t$ is small or large.

---


**Exercise 7.** The `compare_bs_merton` function uses a diffusion volatility $\sigma = 0.20$ for both models. In practice, the "implied volatility" of the Merton model is higher than $\sigma$ because jumps add variance. Compute the total annualized variance of log-returns under the Merton model, $\sigma_{\text{total}}^2 = \sigma^2 + \lambda(\mu_J^2 + \sigma_J^2)$, for the default parameters. Find $\sigma_{\text{total}}$ and compare the Black-Scholes price using $\sigma_{\text{total}}$ with the Merton series price. Are they close? Explain why the Merton price cannot be exactly replicated by a single Black-Scholes volatility.

??? success "Solution to Exercise 7"
    **Total annualized variance.** With $\sigma = 0.20$, $\lambda = 0.5$, $\mu_J = -0.10$, $\sigma_J = 0.30$:

    $$
    \sigma_{\text{total}}^2 = \sigma^2 + \lambda(\mu_J^2 + \sigma_J^2) = 0.04 + 0.5(0.01 + 0.09) = 0.04 + 0.05 = 0.09
    $$

    $$
    \sigma_{\text{total}} = \sqrt{0.09} = 0.30
    $$

    **Black-Scholes price with $\sigma_{\text{total}} = 0.30$.** For $S_0 = K = 100$, $T = 1$, $r = 0.05$:

    $$
    d_1 = \frac{\ln(1) + (0.05 + 0.045) \times 1}{0.30} = \frac{0.095}{0.30} = 0.3167
    $$

    $$
    d_2 = 0.3167 - 0.30 = 0.0167
    $$

    $$
    C_{\text{BS}}(\sigma_{\text{total}}) = 100 \times N(0.3167) - 100 e^{-0.05} N(0.0167)
    $$

    $$
    \approx 100 \times 0.6243 - 95.12 \times 0.5067 \approx 62.43 - 48.20 = 14.23
    $$

    The Merton series price is approximately \$11.35, which is noticeably different from the Black-Scholes price of \$14.23 at $\sigma_{\text{total}} = 0.30$.

    **Why a single Black-Scholes volatility cannot replicate the Merton price.** The Merton return distribution is a Poisson mixture of normals, which differs from a single normal in several ways:

    1. **Non-Gaussian shape.** The Merton distribution has excess kurtosis and (typically) negative skewness. A single Black-Scholes volatility produces a normal distribution, which cannot match both the variance and the higher moments simultaneously.

    2. **Strike-dependent implied volatility.** The implied volatility that equates Black-Scholes to Merton depends on the strike $K$. For OTM puts (low $K$), the implied volatility is higher than for OTM calls (high $K$), producing the volatility smile. No single constant $\sigma$ can reproduce this strike dependence.

    3. **Maturity-dependent implied volatility.** The Merton model's non-Gaussianity is strongest at short maturities and weakens at long maturities (by the central limit theorem for the jump count). A single volatility cannot capture this term structure.

    The ATM implied volatility of the Merton model is typically between $\sigma$ and $\sigma_{\text{total}}$, but the exact value depends on $T$, $\lambda$, $\mu_J$, and $\sigma_J$ in a nonlinear way.
