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

---

## Exercises

**Exercise 1.**
The non-central chi-squared degrees of freedom are $d = 4\kappa\theta/\xi^2$. For the worked example ($\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$), verify that $d \approx 2.667$. Since $d > 1$, the direct decomposition $\chi^2_d(\lambda) = \chi^2_1(\lambda) + \chi^2_{d-1}(0)$ applies. Explain each component: $\chi^2_1(\lambda) = (Z + \sqrt{\lambda})^2$ with $Z \sim N(0,1)$ captures the non-centrality, and $\chi^2_{d-1}(0)$ is a central chi-squared with $d - 1 \approx 1.667$ degrees of freedom. How would you sample a central chi-squared with non-integer degrees of freedom?

??? success "Solution to Exercise 1"
    **Verification of** $d$: With $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$:

    $$
    d = \frac{4\kappa\theta}{\xi^2} = \frac{4(1.5)(0.04)}{0.09} = \frac{0.24}{0.09} = \frac{8}{3} \approx 2.667
    $$

    Since $d > 1$, the direct decomposition applies: $\chi^2_d(\lambda) = \chi^2_1(\lambda) + \chi^2_{d-1}(0)$.

    **Component 1:** $\chi^2_1(\lambda) = (Z + \sqrt{\lambda})^2$ where $Z \sim N(0,1)$. This is a non-central chi-squared with 1 degree of freedom and non-centrality $\lambda$. It captures the contribution of the initial variance $v_0$ to the terminal distribution---the non-centrality parameter $\lambda$ encodes how much $v_0$ influences $v_T$ after mean reversion over the time horizon $T$.

    **Component 2:** $\chi^2_{d-1}(0)$ is a central chi-squared with $d - 1 \approx 1.667$ degrees of freedom. This represents the "steady-state" variability accumulated from the mean-reverting drift toward $\theta$, independent of the starting point.

    **Sampling a central chi-squared with non-integer degrees of freedom:** A central $\chi^2_\nu(0)$ random variable with arbitrary $\nu > 0$ can be sampled as a **Gamma** random variable:

    $$
    \chi^2_\nu(0) \sim \text{Gamma}(\nu/2, 2)
    $$

    For $\nu = d - 1 \approx 1.667$, this is $\text{Gamma}(0.833, 2)$. Standard methods for sampling Gamma variates with non-integer shape parameter include:

    - **Ahrens-Dieter method**: for shape $\alpha < 1$, use the identity $\text{Gamma}(\alpha, 1) \stackrel{d}{=} \text{Gamma}(\alpha+1,1) \cdot U^{1/\alpha}$ where $U \sim \text{Uniform}(0,1)$
    - **Marsaglia-Tsang method**: efficient for $\alpha > 1/3$, applicable here since $0.833 > 1/3$
    - **Built-in library functions** (e.g., NumPy's `random.gamma`) that implement these algorithms internally

---

**Exercise 2.**
The non-centrality parameter is $\lambda = 4\kappa e^{-\kappa T} v_0 / [\xi^2(1 - e^{-\kappa T})]$. Compute $\lambda$ for $T = 0.1$ and $T = 5.0$ with the worked example parameters. Explain why $\lambda$ decreases with $T$: as $T$ grows, the influence of $v_0$ on $v_T$ diminishes due to mean reversion, and the distribution of $v_T$ converges to the stationary distribution (central chi-squared with $\lambda = 0$).

??? success "Solution to Exercise 2"
    The non-centrality parameter is:

    $$
    \lambda = \frac{4\kappa e^{-\kappa T} v_0}{\xi^2(1 - e^{-\kappa T})}
    $$

    With $\kappa = 1.5$, $v_0 = 0.04$, $\xi^2 = 0.09$:

    **For** $T = 0.1$:

    $$
    e^{-1.5 \times 0.1} = e^{-0.15} \approx 0.8607
    $$

    $$
    \lambda = \frac{4(1.5)(0.8607)(0.04)}{0.09(1 - 0.8607)} = \frac{0.2066}{0.09 \times 0.1393} = \frac{0.2066}{0.01254} \approx 16.48
    $$

    **For** $T = 5.0$:

    $$
    e^{-1.5 \times 5.0} = e^{-7.5} \approx 0.000554
    $$

    $$
    \lambda = \frac{4(1.5)(0.000554)(0.04)}{0.09(1 - 0.000554)} = \frac{0.000133}{0.08995} \approx 0.00148
    $$

    **Why** $\lambda$ **decreases with** $T$: The non-centrality parameter $\lambda$ is proportional to $e^{-\kappa T}/(1 - e^{-\kappa T})$. As $T \to \infty$, $e^{-\kappa T} \to 0$, so $\lambda \to 0$. Physically, mean reversion at rate $\kappa$ causes the variance process to "forget" its initial condition $v_0$ over time. The characteristic memory timescale is $1/\kappa = 1/1.5 \approx 0.67$ years. For $T = 0.1$ (much shorter than $1/\kappa$), the initial condition dominates and $\lambda$ is large. For $T = 5.0$ (about $7.5$ mean-reversion times), the initial condition is almost entirely forgotten and $\lambda \approx 0$.

    When $\lambda = 0$, the distribution becomes a central chi-squared $\chi^2_d(0)$, which is the **stationary distribution** of the CIR process (a Gamma distribution with shape $d/2 = 2\kappa\theta/\xi^2$ and scale $\xi^2/(2\kappa)$). The mean of this stationary distribution is $d \cdot \xi^2/(4\kappa) = \theta$, confirming that the long-run variance is $\theta$.

---

**Exercise 3.**
In Step 3, the log-price is reconstructed using the identity

$$
\int_0^T \sqrt{v_s}\,dW_s^{(2)} = \frac{1}{\xi}[v_T - v_0 - \kappa\theta T + \kappa I_T]
$$

Derive this by integrating the CIR SDE: $v_T - v_0 = \kappa\theta T - \kappa I_T + \xi\int_0^T \sqrt{v_s}\,dW_s^{(2)}$ and solving for the stochastic integral. Why is this identity exact and not an approximation?

??? success "Solution to Exercise 3"
    Starting from the CIR SDE and integrating from $0$ to $T$:

    $$
    \int_0^T dv_s = \int_0^T \kappa(\theta - v_s)\,ds + \int_0^T \xi\sqrt{v_s}\,dW_s^{(2)}
    $$

    The left side gives $v_T - v_0$. The first integral on the right is:

    $$
    \int_0^T \kappa(\theta - v_s)\,ds = \kappa\theta T - \kappa \int_0^T v_s\,ds = \kappa\theta T - \kappa I_T
    $$

    Substituting:

    $$
    v_T - v_0 = \kappa\theta T - \kappa I_T + \xi\int_0^T \sqrt{v_s}\,dW_s^{(2)}
    $$

    Solving for the stochastic integral:

    $$
    \xi\int_0^T \sqrt{v_s}\,dW_s^{(2)} = v_T - v_0 - \kappa\theta T + \kappa I_T
    $$

    $$
    \int_0^T \sqrt{v_s}\,dW_s^{(2)} = \frac{1}{\xi}\left[v_T - v_0 - \kappa\theta T + \kappa I_T\right]
    $$

    **Why this is exact:** The derivation uses only the definition of the CIR SDE and the fundamental theorem of calculus for stochastic integrals. No approximation or discretization is involved. The identity $v_T - v_0 = \int_0^T dv_s$ holds pathwise for any continuous semimartingale. The decomposition of $\int_0^T \kappa(\theta - v_s)\,ds$ is algebraically exact. Therefore the identity holds pathwise (almost surely) for every realization of the Brownian motion, not merely in expectation or distribution.

    This identity is the key that allows the Broadie-Kaya algorithm to avoid simulating the stochastic integral $\int \sqrt{v_s}\,dW_s^{(2)}$ directly. Once $v_0$, $v_T$, and $I_T$ are known, this integral is determined exactly.

---

**Exercise 4.**
The conditional variance of $\ln S_T$ given $v_T$ and $I_T$ is $(1 - \rho^2)I_T$. For $\rho = -0.7$, this equals $0.51 \cdot I_T$. Explain why the conditional variance decreases as $|\rho| \to 1$: when $\rho = \pm 1$, the stock and variance are perfectly correlated, so knowing $v_T$ and $I_T$ determines $\ln S_T$ exactly. What is the conditional variance when $\rho = 0$?

??? success "Solution to Exercise 4"
    The conditional variance of $\ln S_T$ given $(v_T, I_T)$ arises from the independent Brownian component:

    $$
    \text{Var}(\ln S_T \mid v_T, I_T) = (1-\rho^2)\,\text{Var}\!\left(\int_0^T \sqrt{v_s}\,dW_s^{(\perp)} \,\Big|\, I_T\right) = (1-\rho^2)\,I_T
    $$

    where we used the fact that $\text{Var}(\int_0^T \sqrt{v_s}\,dW_s^{(\perp)} \mid I_T) = \int_0^T v_s\,ds = I_T$ by the Ito isometry applied conditionally.

    **For** $\rho = -0.7$: $(1-\rho^2)I_T = (1 - 0.49)I_T = 0.51\,I_T$.

    **As** $|\rho| \to 1$: The factor $(1-\rho^2) \to 0$, so the conditional variance vanishes. This is because when $|\rho| = 1$, the Brownian motion driving the stock is a linear combination of $W^{(2)}$ alone (with no orthogonal component $W^{(\perp)}$). In this case:

    $$
    dW^{(1)} = \pm\,dW^{(2)}
    $$

    The stock and variance are driven by the same single source of randomness. Given $v_T$ and $I_T$, the stochastic integral $\int \sqrt{v_s}\,dW_s^{(2)}$ is exactly determined by the identity from Exercise 3, so $\ln S_T$ is fully determined---there is no remaining randomness.

    **For** $\rho = 0$: $(1-\rho^2)I_T = I_T$. The conditional variance equals the full integrated variance. When $\rho = 0$, the stock and variance are driven by independent Brownian motions. Knowing $v_T$ and $I_T$ tells us nothing about the realization of $W^{(\perp)} = W^{(1)}$, so the full stochastic volatility effect remains in the conditional distribution.

---

**Exercise 5.**
The computational bottleneck of exact simulation is the Fourier inversion for $I_T \mid (v_0, v_T)$. The CDF is computed via $F(x) = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \text{Re}[e^{-iux}\phi(u)/(iu)]\,du$, and root-finding solves $F(x) = U$. If each CDF evaluation requires 100 quadrature points and root-finding needs 20 CDF evaluations, estimate the cost per path (in number of function evaluations) for a European option ($N = 1$ step) and for an Asian option with monthly monitoring ($N = 12$ steps). Compare with the QE scheme cost.

??? success "Solution to Exercise 5"
    **Cost per CDF evaluation:** 100 quadrature points, each requiring one evaluation of $\phi_{I|v_0,v_T}(u)$. So each CDF evaluation costs approximately 100 function evaluations.

    **Cost per sample of** $I_T$: Root-finding requires 20 CDF evaluations, so $20 \times 100 = 2{,}000$ function evaluations per sample.

    **European option** ($N = 1$ step):

    Each path requires:

    - Step 1 (sample $v_T$): $\sim 5$ operations (non-central chi-squared sampling)
    - Step 2 (sample $I_T$): $\sim 2{,}000$ function evaluations
    - Step 3 (sample $\ln S_T$): $\sim 5$ operations (Gaussian draw plus arithmetic)
    - **Total per path:** $\approx 2{,}010$ function evaluations

    **Asian option with monthly monitoring** ($N = 12$ steps):

    Each path requires 12 repetitions of all three steps:

    - **Total per path:** $12 \times 2{,}010 = 24{,}120$ function evaluations

    **QE scheme comparison:** The QE scheme costs approximately 30 operations per step. For $N = 12$ steps: $12 \times 30 = 360$ operations per path. The exact simulation is:

    - European: $2{,}010 / 30 \approx 67$ times more expensive than a single QE step
    - Asian ($N = 12$): $24{,}120 / 360 = 67$ times more expensive than QE with the same number of steps

    For a fixed computational budget, the QE scheme can run approximately 67 times more paths, reducing the standard error by a factor of $\sqrt{67} \approx 8.2$. Since the QE scheme already has near-zero discretization bias, this standard error reduction more than compensates for any tiny remaining bias, making QE the preferred choice for production pricing.

---

**Exercise 6.**
For path-dependent options, the Broadie-Kaya algorithm generates the correct finite-dimensional marginals $(v_{t_k}, S_{t_k})$ at observation times $t_0, t_1, \ldots, t_N$. However, the path between observations is not simulated. Explain why this is adequate for discretely monitored Asian options but problematic for continuously monitored barrier options. Propose a hybrid approach: use exact simulation for the variance and log-price at monitoring dates, and apply a Brownian bridge correction for the barrier between dates.

??? success "Solution to Exercise 6"
    **Discretely monitored Asian options:** An Asian option with discrete monitoring at dates $t_1, \ldots, t_N$ has a payoff depending on $(S_{t_1}, \ldots, S_{t_N})$. The Broadie-Kaya algorithm generates exact samples of $(v_{t_k}, S_{t_k})$ at each monitoring date, so the payoff is computed from the correct joint distribution. No approximation is needed for the path between monitoring dates because the payoff does not depend on it.

    **Continuously monitored barrier options:** A barrier option with barrier $B$ has a payoff that depends on whether $\max_{0 \leq t \leq T} S_t > B$ (or $\min_{0 \leq t \leq T} S_t < B$). The Broadie-Kaya algorithm only generates $(v_{t_k}, S_{t_k})$ at discrete observation times, so it can miss barrier crossings between observation dates. If $S_{t_k} < B$ for all $k$ but $S_t > B$ for some $t \in (t_k, t_{k+1})$, the algorithm incorrectly classifies the path as not having hit the barrier.

    **Hybrid approach with Brownian bridge correction:**

    1. Use exact simulation (Broadie-Kaya) to generate $(v_{t_k}, S_{t_k})$ at the monitoring/observation dates $t_0, t_1, \ldots, t_N$.
    2. Between consecutive dates $t_k$ and $t_{k+1}$, the log-price path conditional on its endpoints is approximately a Brownian bridge (conditional on the integrated variance over the interval).
    3. For a Brownian bridge from $x_a$ to $x_b$ over $[t_k, t_{k+1}]$ with variance rate $\bar{v}_k$, the probability that the maximum exceeds a level $\ln B$ is:

    $$
    \mathbb{P}\!\left(\max_{t_k \leq t \leq t_{k+1}} x_t > \ln B \,\Big|\, x_{t_k}, x_{t_{k+1}}\right) = \exp\!\left(-\frac{2(\ln B - x_{t_k})(\ln B - x_{t_{k+1}})}{\bar{v}_k (t_{k+1} - t_k)}\right)
    $$

    when both $x_{t_k} < \ln B$ and $x_{t_{k+1}} < \ln B$. Here $\bar{v}_k \approx (v_{t_k} + v_{t_{k+1}})/2$ or $I_k / (t_{k+1} - t_k)$.

    4. Use this probability to correct the barrier crossing estimate, either by adjusting the payoff weight or by sampling a barrier-hitting indicator from this conditional probability.

    This hybrid approach combines the zero-bias advantage of exact simulation for the marginal distributions with the Brownian bridge correction for the continuous barrier, though some approximation remains in the bridge step because the true conditional path under stochastic volatility is not exactly a Brownian bridge.

---

**Exercise 7.**
Compare the mean squared error (MSE) of exact simulation versus QE for a European call with $M = 1{,}000$ paths. Exact simulation has zero bias but high cost per path, while QE has near-zero bias and low cost per path. If the QE scheme costs $C_{\text{QE}}$ per path and exact simulation costs $500 \cdot C_{\text{QE}}$ per path, and both achieve the same standard error per path, how many QE paths can be run for the same total cost as $M = 1{,}000$ exact paths? Which approach achieves lower MSE?

??? success "Solution to Exercise 7"
    The MSE decomposes as $\text{MSE} = \text{Bias}^2 + \text{Variance}$.

    **Exact simulation** ($M = 1{,}000$ paths):

    - Bias $= 0$ (exact)
    - Variance $= \sigma_g^2 / M = \sigma_g^2 / 1{,}000$
    - $\text{MSE}_{\text{exact}} = \sigma_g^2 / 1{,}000$

    **QE scheme with equivalent budget:** The total cost of $1{,}000$ exact paths is $1{,}000 \times 500\,C_{\text{QE}} = 500{,}000\,C_{\text{QE}}$. The number of QE paths affordable for the same budget is:

    $$
    M_{\text{QE}} = \frac{500{,}000\,C_{\text{QE}}}{C_{\text{QE}}} = 500{,}000 \text{ paths}
    $$

    For the QE scheme:

    - Bias $\approx \epsilon$ (near zero but not exactly zero; say $\epsilon \approx \$0.01$)
    - Variance $= \sigma_g^2 / 500{,}000$
    - $\text{MSE}_{\text{QE}} = \epsilon^2 + \sigma_g^2 / 500{,}000$

    **Comparison:** The variance ratio is:

    $$
    \frac{\text{Var}_{\text{exact}}}{\text{Var}_{\text{QE}}} = \frac{500{,}000}{1{,}000} = 500
    $$

    The QE scheme has 500 times smaller variance. For the QE scheme's MSE to exceed the exact simulation's MSE, we would need $\epsilon^2 > \sigma_g^2/1{,}000 - \sigma_g^2/500{,}000 \approx \sigma_g^2/1{,}000$. With typical $\sigma_g \approx \$15$ (standard deviation of the discounted payoff), this threshold is $\sigma_g^2/1{,}000 = 225/1{,}000 = 0.225$, requiring $\epsilon > \$0.47$. Since the QE bias is typically $\$0.01$ or less, we have $\epsilon^2 = 0.0001 \ll 0.225$.

    **Conclusion:** The QE scheme achieves dramatically lower MSE for the same computational budget. The QE estimator has $\text{MSE}_{\text{QE}} \approx 225/500{,}000 = 0.00045$, while exact simulation has $\text{MSE}_{\text{exact}} = 225/1{,}000 = 0.225$---roughly 500 times larger. The near-zero bias of QE combined with its low computational cost per path makes it far superior for production pricing. Exact simulation is justified only when zero bias is essential (e.g., benchmarking) or when $M$ is very small and every path must be perfectly accurate.
