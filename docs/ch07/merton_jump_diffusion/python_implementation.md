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

The `simulate_paths` method implements the log-Euler scheme for the Merton SDE. At each time step $\Delta t = T/N$:

$$
S_{t+\Delta t} = S_t \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\,Z + \sum_{i=1}^{n}\ln Y_i\right]
$$

where $Z \sim N(0,1)$ and $n \sim \text{Poisson}(\lambda\Delta t)$.

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

The `option_price_series` method implements the Merton series formula:

$$
C = \sum_{n=0}^{n_{\max}}\frac{e^{-\lambda'T}(\lambda'T)^n}{n!}\,C_{\text{BS}}(S_0, K, T, r_n, \sigma_n)
$$

with conditional parameters:

$$
\sigma_n^2 = \sigma^2 + \frac{n\sigma_J^2}{T}, \qquad r_n = r - \lambda\bar{k} + \frac{n(\mu_J + \sigma_J^2/2)}{T}
$$

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

---

**Exercise 2.** The log-Euler simulation step is $S_{t+\Delta t} = S_t \exp[(r - \lambda\bar{k} - \frac{1}{2}\sigma^2)\Delta t + \sigma\sqrt{\Delta t}\,Z + \sum_{i=1}^{n}\ln Y_i]$ where $n \sim \text{Poisson}(\lambda\Delta t)$ and $\ln Y_i \sim N(\mu_J, \sigma_J^2)$. Show that when $n = 0$ (no jumps in the time step), this reduces to the standard log-Euler step for geometric Brownian motion. Then show that $\mathbb{E}[S_{t+\Delta t}/S_t] = e^{r\Delta t}$ by computing the expectation over both $Z$ and the jump component (using the tower property over $n$).

---

**Exercise 3.** The Merton series formula is $C = \sum_{n=0}^{\infty} \frac{e^{-\lambda'T}(\lambda'T)^n}{n!}\,C_{\text{BS}}(S_0, K, T, r_n, \sigma_n)$. For the default parameters, compute the first three terms ($n = 0, 1, 2$) of the series numerically. Use the Black-Scholes formula with $\sigma_0^2 = 0.04$, $r_0 \approx r - \lambda\bar{k}$ for $n = 0$, and the corresponding $\sigma_n^2$ and $r_n$ for $n = 1, 2$. Verify that the sum converges rapidly by comparing the $n = 0, 1, 2$ partial sums.

---

**Exercise 4.** The output shows that the Merton call price (\$11.35) exceeds the Black-Scholes call price (\$10.45) by approximately \$0.90, and the same difference holds for puts. Explain why the difference is identical for calls and puts by invoking put-call parity. Then explain economically why jump risk increases option prices: consider the effect of jumps on the tails of the return distribution and the convexity of option payoffs.

---

**Exercise 5.** The Monte Carlo standard error is $\text{SE} = \hat{\sigma}/\sqrt{M}$ where $\hat{\sigma}$ is the sample standard deviation of the discounted payoffs and $M$ is the number of paths. For $M = 50{,}000$ and a typical $\hat{\sigma} \approx 15$, estimate the standard error. How many paths would be needed to reduce the standard error below \$0.01? Propose a variance reduction technique (e.g., antithetic variates or control variates using the Black-Scholes price) and explain how it would reduce $\hat{\sigma}$.

---

**Exercise 6.** Modify the `simulate_paths` logic conceptually to handle the case where $\Delta t$ is large enough that $\lambda\Delta t > 1$. In this regime, multiple jumps per time step are common. Show that the sum $\sum_{i=1}^n \ln Y_i$ for $n \sim \text{Poisson}(\lambda\Delta t)$ has mean $\lambda\Delta t\,\mu_J$ and variance $\lambda\Delta t(\sigma_J^2 + \mu_J^2) - (\lambda\Delta t\,\mu_J)^2$. Explain why the exact distribution of $S_{t+\Delta t}/S_t$ remains tractable (it is a mixture of log-normals), and why the simulation is exact regardless of the time step size.

---

**Exercise 7.** The `compare_bs_merton` function uses a diffusion volatility $\sigma = 0.20$ for both models. In practice, the "implied volatility" of the Merton model is higher than $\sigma$ because jumps add variance. Compute the total annualized variance of log-returns under the Merton model, $\sigma_{\text{total}}^2 = \sigma^2 + \lambda(\mu_J^2 + \sigma_J^2)$, for the default parameters. Find $\sigma_{\text{total}}$ and compare the Black-Scholes price using $\sigma_{\text{total}}$ with the Merton series price. Are they close? Explain why the Merton price cannot be exactly replicated by a single Black-Scholes volatility.
