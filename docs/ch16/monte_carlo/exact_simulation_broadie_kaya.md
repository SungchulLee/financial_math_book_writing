# Exact Simulation (Broadie-Kaya)

Every discretization scheme---Euler, Milstein, QE---introduces some approximation error by replacing continuous dynamics with discrete steps. Broadie and Kaya (2006) developed an **exact simulation** algorithm that samples from the true joint distribution of $(v_T, \ln S_T)$ without any time discretization. The algorithm exploits the known transition distribution of the CIR variance process and the conditional Gaussianity of the log-price given the integrated variance. The trade-off is computational cost: sampling the integrated variance requires a Fourier inversion that is significantly more expensive per path than the QE scheme.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the exact transition distribution of the CIR variance process using the non-central chi-squared
    2. Derive the conditional distribution of the integrated variance given the variance endpoints
    3. Reconstruct the exact log-price distribution from the integrated variance
    4. Assess the computational cost-accuracy trade-off of exact simulation versus discretization schemes

!!! tip "Prerequisites"
    This section requires the [non-central chi-squared distribution](../variance_dynamics/non_central_chi_squared.md), the [CIR process solution](../variance_dynamics/cir_variance_process_solution.md), and familiarity with the [QE scheme](quadratic_exponential_scheme.md).

---

## Overview of the Algorithm

The Broadie-Kaya algorithm generates exact samples of $(v_T, \ln S_T)$ in three steps:

1. **Sample the terminal variance** $v_T$ from its exact non-central chi-squared distribution
2. **Sample the integrated variance** $\int_0^T v_s \, ds$ from its exact conditional distribution given $(v_0, v_T)$
3. **Compute the log-price** $\ln S_T$ from a conditional Gaussian distribution given $v_T$ and $\int_0^T v_s \, ds$

Each step is exact, so the combined sample is drawn from the true distribution with no discretization bias.

---

## Step 1: Sampling the Terminal Variance

The CIR process $dv_t = \kappa(\theta - v_t) dt + \xi\sqrt{v_t} \, dW_t^{(2)}$ has a known transition distribution. Conditional on $v_0$, the terminal variance $v_T$ satisfies:

$$
v_T \sim \frac{\xi^2(1 - e^{-\kappa T})}{4\kappa} \, \chi^2_d(\lambda)
$$

where $\chi^2_d(\lambda)$ denotes the non-central chi-squared distribution with:

- **Degrees of freedom**: $d = \frac{4\kappa\theta}{\xi^2}$
- **Non-centrality parameter**: $\lambda = \frac{4\kappa e^{-\kappa T} v_0}{\xi^2(1 - e^{-\kappa T})}$

Sampling from the non-central chi-squared can be done via:

- **Direct decomposition**: when $d > 1$, write $\chi^2_d(\lambda) = \chi^2_1(\lambda) + \chi^2_{d-1}(0)$, where $\chi^2_1(\lambda) = (Z + \sqrt{\lambda})^2$ with $Z \sim N(0,1)$ and $\chi^2_{d-1}(0)$ is a central chi-squared
- **Poisson mixture**: when $d \leq 1$, sample $N \sim \text{Poisson}(\lambda/2)$ and then $\chi^2_{d+2N}(0)$

!!! note "Feller Condition Connection"
    The degrees of freedom $d = 4\kappa\theta/\xi^2$ directly relate to the Feller condition: $d \geq 2$ is equivalent to $2\kappa\theta \geq \xi^2$. When $d < 2$ (Feller violated), the non-central chi-squared has a point mass near zero, which the Poisson mixture correctly handles.

---

## Step 2: Sampling the Integrated Variance

The critical and most challenging step is sampling the **integrated variance**:

$$
I_T = \int_0^T v_s \, ds
$$

conditional on both endpoints $v_0$ and $v_T$. The exact conditional distribution of $I_T \mid (v_0, v_T)$ does not have a standard closed-form density, but its **characteristic function** is known.

### Characteristic Function of the Integrated Variance

Broadie and Kaya show that the conditional characteristic function of $I_T$ given $(v_0, v_T)$ can be expressed using the Bessel function. Define:

$$
\phi_{I|v_0, v_T}(u) = \mathbb{E}\left[e^{iu I_T} \,\Big|\, v_0, v_T\right]
$$

This characteristic function has the form:

$$
\phi_{I|v_0, v_T}(u) = \frac{\gamma(u) e^{-\frac{1}{2}(\gamma(u) - \kappa)T}}{\kappa(1 - e^{-\gamma(u) T})} \cdot \frac{1 - e^{-\kappa T}}{1} \cdot \exp\!\left(\frac{v_0 + v_T}{\xi^2}\left[\frac{\kappa(1 + e^{-\kappa T})}{1 - e^{-\kappa T}} - \frac{\gamma(u)(1 + e^{-\gamma(u)T})}{1 - e^{-\gamma(u)T}}\right]\right)
$$

where:

$$
\gamma(u) = \sqrt{\kappa^2 - 2\xi^2 iu}
$$

The exact formula involves a ratio of modified Bessel functions $I_\nu$ and requires careful numerical evaluation.

### Fourier Inversion

To sample from this distribution, compute the CDF via numerical Fourier inversion:

$$
F_{I|v_0,v_T}(x) = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iux}\phi_{I|v_0,v_T}(u)}{iu}\right] du
$$

Then apply the **inverse CDF method**: draw $U \sim \text{Uniform}(0,1)$ and solve $F_{I|v_0,v_T}(x) = U$ for $x$ using root-finding (bisection or Newton's method).

!!! warning "Computational Cost"
    Each evaluation of the CDF requires a numerical integration (typically 50--200 quadrature points), and the root-finding requires 10--30 CDF evaluations. This makes sampling $I_T$ approximately 500--6000 times more expensive than a single QE variance step. This cost is the principal disadvantage of exact simulation.

---

## Step 3: Reconstructing the Log-Price

Given exact samples of $v_T$ and $I_T = \int_0^T v_s \, ds$, the log-price has a **conditional Gaussian** distribution. From the Heston SDE:

$$
\ln S_T = \ln S_0 + (r - q)T - \frac{1}{2}I_T + \rho \int_0^T \sqrt{v_s} \, dW_s^{(2)} + \sqrt{1 - \rho^2} \int_0^T \sqrt{v_s} \, dW_s^{(\perp)}
$$

The integral involving $W^{(2)}$ is related to the variance increment by:

$$
\int_0^T \sqrt{v_s} \, dW_s^{(2)} = \frac{1}{\xi}\left[v_T - v_0 - \kappa\theta T + \kappa I_T\right]
$$

The integral involving the independent Brownian motion $W^{(\perp)}$ is conditionally Gaussian:

$$
\int_0^T \sqrt{v_s} \, dW_s^{(\perp)} \,\Big|\, I_T \sim N\!\left(0, \, I_T\right)
$$

Combining these, the exact log-price is:

$$
\ln S_T = \ln S_0 + (r - q)T - \frac{1}{2}I_T + \frac{\rho}{\xi}\left[v_T - v_0 - \kappa\theta T + \kappa I_T\right] + \sqrt{(1 - \rho^2) I_T} \, Z
$$

where $Z \sim N(0,1)$ is independent of everything else. This is an **exact** expression---no approximation has been made.

---

## Complete Broadie-Kaya Algorithm

For each Monte Carlo path:

1. **Sample $v_T$**: Draw from the scaled non-central chi-squared distribution
2. **Sample $I_T$**: Compute the conditional CDF via Fourier inversion of $\phi_{I|v_0,v_T}$ and apply the inverse CDF method
3. **Sample $\ln S_T$**: Draw $Z \sim N(0,1)$ and compute:

$$
\ln S_T = \ln S_0 + (r - q)T - \frac{1}{2}I_T + \frac{\rho}{\xi}(v_T - v_0 - \kappa\theta T + \kappa I_T) + \sqrt{(1-\rho^2)I_T} \, Z
$$

4. **Compute payoff**: $\text{payoff} = g(e^{\ln S_T})$ for the desired derivative

The price estimate is $\hat{V} = e^{-rT} \frac{1}{M}\sum_{m=1}^M \text{payoff}^{(m)}$.

---

## Multi-Step Extension

For path-dependent options requiring intermediate values $(v_{t_k}, S_{t_k})$ at times $0 = t_0 < t_1 < \cdots < t_N = T$, apply the algorithm recursively:

1. At each step, sample $v_{t_{k+1}}$ from the non-central chi-squared given $v_{t_k}$
2. Sample $I_k = \int_{t_k}^{t_{k+1}} v_s \, ds$ given $(v_{t_k}, v_{t_{k+1}})$
3. Compute $\ln S_{t_{k+1}}$ from the conditional Gaussian

Each step is exact, so the path $(v_{t_0}, S_{t_0}), \ldots, (v_{t_N}, S_{t_N})$ has the correct finite-dimensional marginal distributions. However, the path between observation times is not simulated, which limits applicability to continuously monitored barriers.

---

## Computational Cost Comparison

| Method | Cost per Path ($N$ steps) | Discretization Bias | Implementation |
|--------|--------------------------|--------------------:|----------------|
| Euler (full trunc.) | $\mathcal{O}(N)$ | $\mathcal{O}(\Delta t)$ | Simple |
| QE scheme | $\mathcal{O}(N)$ | Near zero | Moderate |
| Exact (Broadie-Kaya) | $\mathcal{O}(N \cdot C_{\text{inv}})$ | Zero | Complex |

Here $C_{\text{inv}} \approx 500$--$6000$ is the cost of one Fourier inversion for $I_T$. For European options, the QE scheme with $N = 12$ monthly steps provides accuracy comparable to exact simulation at a fraction of the cost.

!!! tip "When to Use Exact Simulation"
    Exact simulation is most valuable when:

    - **Benchmarking**: validating discretization schemes against a bias-free reference
    - **Exotic payoffs**: path-dependent options where discretization bias is hard to quantify
    - **Small sample sizes**: when the number of paths $M$ is small and every path must be accurate
    - **Research**: establishing theoretical properties of Heston-based estimators

    For production pricing of vanilla options, the QE scheme is preferred.

---

## Worked Example

Consider a European call with parameters:

| Parameter | Value |
|-----------|-------|
| $S_0$ | $\$100$ |
| $K$ | $\$100$ |
| $r$ | $0.05$ |
| $v_0$ | $0.04$ |
| $\kappa$ | $1.5$ |
| $\theta$ | $0.04$ |
| $\xi$ | $0.3$ |
| $\rho$ | $-0.7$ |
| $T$ | $1.0$ |

**Step 1**: Compute the non-central chi-squared parameters:

$$
d = \frac{4(1.5)(0.04)}{0.09} = \frac{0.24}{0.09} \approx 2.667
$$

$$
\lambda = \frac{4(1.5)e^{-1.5}(0.04)}{0.09(1 - e^{-1.5})} \approx \frac{0.0535}{0.0706} \approx 0.758
$$

Since $d > 1$, use the direct decomposition to sample $v_T$.

**Step 2**: Given the sampled $v_T$, evaluate $\phi_{I|v_0,v_T}$ on a quadrature grid and compute the CDF. Find $I_T$ by root-finding.

**Step 3**: Draw $Z \sim N(0,1)$ and compute $\ln S_T$ exactly.

With $M = 10{,}000$ paths, the exact simulation produces a price estimate with zero discretization bias, though the standard error from Monte Carlo sampling remains $\mathcal{O}(M^{-1/2})$.

---

## Summary

The Broadie-Kaya exact simulation algorithm eliminates discretization bias entirely by sampling from the true Heston transition distributions. The three-step procedure---non-central chi-squared for $v_T$, Fourier inversion for $\int v_s \, ds$, conditional Gaussian for $\ln S_T$---produces exact samples at the cost of an expensive numerical inversion per step. For production use, the [QE scheme](quadratic_exponential_scheme.md) provides a better cost-accuracy trade-off, but exact simulation remains the gold standard for benchmarking and research. Combining exact simulation with [variance reduction techniques](variance_reduction_techniques.md) can partially offset the computational overhead.
