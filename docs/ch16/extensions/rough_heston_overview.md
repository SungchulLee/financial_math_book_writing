# Rough Heston Model (Overview)

## Introduction

Recall the rough-volatility empirical findings (see [§ Rough Volatility](../../ch14/extensions_and_variants/sabr_model.md)): equity log-volatility behaves like fractional Brownian motion with **Hurst parameter** $H \approx 0.1 \ll 0.5$, producing power-law scaling $\mathbb{E}[|v_{t+\Delta} - v_t|^2] \sim \Delta^{2H}$.

Recall standard Heston (see [§ Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md)): the CIR variance process is Markovian with $H = 0.5$ and cannot reproduce this roughness. The **rough Heston model** (El Euch and Rosenbaum, 2019) replaces CIR with a Volterra-type integral equation driven by the **fractional kernel** $K_H(t) = t^{H-1/2} / \Gamma(H + 1/2)$. The process is non-Markovian, but the characteristic function still satisfies a (fractional) Riccati equation.

This section provides an overview of the rough Heston framework, its mathematical foundations, key results, and implications for option pricing and calibration.

!!! info "Prerequisites"

    - [Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md) (standard Heston)
    - [Riccati ODE System](../heston_cf/riccati_ode_system.md) (standard Riccati)
    - [Affine Structure and Riccati](../model_definition/affine_structure_and_riccati.md) (affine framework)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the empirical evidence for rough volatility and the role of the Hurst parameter $H$
    2. Write down the rough Heston variance dynamics using the fractional kernel
    3. State the fractional (Volterra) Riccati equation for the characteristic function
    4. Explain the key results of El Euch and Rosenbaum on the rough Heston characteristic function
    5. Compare rough Heston with standard Heston in terms of smile dynamics and calibration

---

## Empirical Evidence for Rough Volatility

### The Hurst Parameter

For a stochastic process $Y_t$, the **Hurst parameter** $H \in (0, 1)$ characterizes the roughness of sample paths through the scaling relation:

$$
\mathbb{E}[|Y_{t+\Delta} - Y_t|^q] \sim \Delta^{qH} \quad \text{as } \Delta \to 0
$$

for integer moments $q \geq 1$. Standard Brownian motion has $H = 1/2$. Processes with $H < 1/2$ are **rougher** (more irregular) than Brownian motion, while $H > 1/2$ produces smoother paths.

### Gatheral, Jaisson, and Rosenbaum (2018)

The seminal empirical study analyzed the log-realized variance of equity indices and found:

1. **$H \approx 0.1$ universally**: Across major equity indices (S&P 500, EURO STOXX 50, DAX), the estimated Hurst parameter of log-realized volatility is approximately $H \approx 0.1$, consistent across time periods and estimation methods.

2. **Power-law autocorrelation**: The autocorrelation of $|\Delta X_t|^q$ decays as $\Delta^{2H}$ for small $\Delta$, ruling out Markovian models (which produce exponential decay).

3. **Scaling across time scales**: The fractional scaling holds from tick data ($\Delta = $ seconds) to daily returns ($\Delta = 1$ day), suggesting a universal roughness feature.

!!! warning "Standard Heston Implies $H = 0.5$"
    The CIR variance process in the standard Heston model is a Markov diffusion with sample paths that scale as $\Delta^{1/2}$ locally. This is fundamentally inconsistent with the observed $H \approx 0.1$ roughness of realized variance. The standard Heston model cannot reproduce the power-law autocorrelation structure of volatility.

---

## Rough Heston Variance Dynamics

### The Volterra Integral Equation

The rough Heston model replaces the CIR SDE with a **Volterra-type stochastic integral equation**:

$$
v_t = v_0 + \int_0^t K_H(t - s) \, \kappa(\theta - v_s) \, ds + \int_0^t K_H(t - s) \, \xi \sqrt{v_s} \, dW_s^{(2)}
$$

where the **fractional kernel** is:

$$
K_H(t) = \frac{t^{H - 1/2}}{\Gamma(H + 1/2)}
$$

for $H \in (0, 1/2)$ and $\Gamma$ is the gamma function.

### Comparison with Standard Heston

| Feature | Standard Heston ($H = 0.5$) | Rough Heston ($H < 0.5$) |
|---------|---------------------------|--------------------------|
| Variance dynamics | $dv_t = \kappa(\theta - v_t)dt + \xi\sqrt{v_t}dW_t^{(2)}$ | Volterra integral with kernel $K_H$ |
| Kernel | $K_{0.5}(t) = 1$ (Dirac-like) | $K_H(t) = t^{H-1/2}/\Gamma(H+1/2)$, singular at $t = 0$ |
| Markov property | Yes | No (path-dependent) |
| Local regularity | $H = 0.5$ | $H \approx 0.1$ |
| Autocorrelation decay | Exponential: $e^{-\kappa\Delta}$ | Power-law: $\Delta^{2H}$ |

### Key Properties

The fractional kernel $K_H$ is **singular at the origin** for $H < 1/2$: $K_H(0^+) = +\infty$. This singularity amplifies the effect of recent noise increments relative to distant ones, creating the rough behavior. The total kernel mass over $[0, T]$ is:

$$
\int_0^T K_H(s) \, ds = \frac{T^{H + 1/2}}{\Gamma(H + 3/2)}
$$

which is finite for all $H > 0$.

!!! tip "Physical Intuition"
    The kernel $K_H$ acts as a **memory filter**. In standard Heston ($H = 0.5$, $K = 1$), each Brownian increment contributes equally to the variance regardless of when it occurred. In rough Heston ($H = 0.1$), recent increments are amplified by the factor $(t - s)^{H - 1/2}$, which diverges as $s \to t$. This creates **short-range memory** with rapid local fluctuations but slow long-range decay --- exactly the pattern observed in realized volatility.

---

## Characteristic Function and the Fractional Riccati Equation

### The Affine Structure Survives

Despite losing the Markov property, the rough Heston model retains a form of **affine structure**. The characteristic function of the log-price $X_T = \ln S_T$ can be expressed as:

$$
\phi(u, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{iu X_T} \mid X_0, v_0\right] = \exp\!\left(iu X_0 + iu(r - q)T + g(0, u)\right)
$$

where $g(0, u)$ satisfies a system involving the solution to a **fractional Riccati equation**.

### The Volterra Riccati Equation

!!! note "Theorem (El Euch and Rosenbaum, 2019)"
    The characteristic function of $X_T$ under the rough Heston model satisfies:

    $$
    g(0, u) = v_0 \int_0^T h(s, u) \, ds + \kappa\theta \int_0^T \int_0^s K_H(s - r) h(r, u) \, dr \, ds
    $$

    where $h(t, u)$ solves the **fractional Riccati equation**:

    $$
    h(t, u) = \int_0^t K_H(t - s) F(h(s, u)) \, ds + K_H(t) \cdot D_0(u)
    $$

    with the Riccati nonlinearity:

    $$
    F(x) = \frac{1}{2}\xi^2 x^2 + (\rho\xi iu - \kappa)x + \frac{1}{2}(iu - u^2)
    $$

    and initial condition $D_0(u) = 0$. Here $F$ is the same quadratic that appears in the standard Heston Riccati ODE.

### Comparison with Standard Riccati

Recall the standard Heston Riccati ODE $dD/d\tau = F(D)$ with $D(0,u)=0$ (see [§ Riccati ODE System](../heston_cf/riccati_ode_system.md)). The rough Heston replaces this with a **Volterra integral equation** of the second kind:

$$
h(t) = \int_0^t K_H(t - s) F(h(s)) \, ds
$$

When $H = 1/2$ and $K_{1/2}(t) = 1/\Gamma(1) = 1$, this reduces to $h(t) = \int_0^t F(h(s)) \, ds$, which is equivalent to $h'(t) = F(h(t))$ --- recovering the standard Riccati ODE. The fractional Riccati is thus a **genuine generalization** of the Heston Riccati system.

---

## Numerical Solution

### Adams Scheme

The fractional Riccati equation does not have a closed-form solution for $H \neq 1/2$. Numerical solution uses **fractional Adams methods** adapted for Volterra integral equations:

1. Discretize $[0, T]$ into $N$ steps with $\Delta t = T/N$
2. At each step $t_n$, approximate:

$$
h(t_n) \approx \sum_{k=0}^{n-1} w_{n,k} \, K_H(t_n - t_k) \, F(h(t_k)) \, \Delta t
$$

where $w_{n,k}$ are quadrature weights (trapezoidal or product integration). The complexity is $\mathcal{O}(N^2)$ due to the non-local kernel, compared to $\mathcal{O}(N)$ for the standard Riccati ODE.

### Markovian Approximation

An alternative approach approximates the non-Markovian rough Heston by a **multi-factor Markovian system**. The fractional kernel is expanded as:

$$
K_H(t) \approx \sum_{j=1}^{M} c_j \, e^{-\gamma_j t}
$$

using a sum of $M$ exponentials. Each exponential factor introduces an auxiliary Markov state variable, converting the Volterra equation into a system of $M$ coupled Riccati ODEs. With $M = 5$--$10$ factors, this approximation achieves accuracy comparable to direct numerical solution of the fractional Riccati while enabling efficient pricing via standard affine methods.

---

## Implications for Option Pricing

### Short-Maturity Behavior

The rough Heston model produces fundamentally different short-maturity implied volatility behavior compared to standard Heston:

!!! note "Theorem (ATM Skew Explosion)"
    Under the rough Heston model with Hurst parameter $H$, the ATM implied volatility skew satisfies:

    $$
    \left.\frac{\partial \sigma_{\text{imp}}}{\partial \ln K}\right|_{K = F} \sim C \cdot T^{H - 1/2} \quad \text{as } T \to 0
    $$

    for a constant $C$ depending on the model parameters.

For $H = 0.1$, the exponent is $H - 1/2 = -0.4$, so the skew **diverges** as $T^{-0.4}$ for short maturities. In contrast, the standard Heston skew is proportional to $T^0 = 1$ (constant in the short-maturity limit). The rough Heston explosion is consistent with empirical observations of very steep short-maturity equity skews.

### Calibration Quality

Empirical calibration studies show that rough Heston with $H \approx 0.1$ and only five parameters (same count as standard Heston, with $H$ replacing one degree of freedom) can achieve:

- **Better short-maturity fit** than standard Heston
- **Comparable long-maturity fit** to standard Heston
- **Better joint fit** across the entire term structure of the implied volatility surface

The rough Heston model does not require the separate jump component of Bates to achieve steep short-maturity smiles --- the roughness provides this feature naturally.

### Computational Cost

The main disadvantage of rough Heston is computational:

| Operation | Standard Heston | Rough Heston |
|-----------|----------------|--------------|
| CF evaluation | $\mathcal{O}(1)$ (closed form) | $\mathcal{O}(N^2)$ (fractional Adams) |
| Option pricing | $\mathcal{O}(N_u)$ | $\mathcal{O}(N_u \cdot N^2)$ |
| Monte Carlo (per step) | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ (path-dependent) |

where $N_u$ is the number of quadrature points for Fourier inversion and $N$ is the Riccati discretization. The Markovian approximation reduces the CF evaluation to $\mathcal{O}(M)$ at the cost of introducing $M$ auxiliary state variables.

---

## Worked Example: Skew Comparison

### Parameters

| Parameter | Value |
|-----------|-------|
| $v_0$ | 0.04 |
| $\kappa$ | 2.0 |
| $\theta$ | 0.04 |
| $\xi$ | 0.5 |
| $\rho$ | $-0.7$ |

### ATM Skew by Maturity

| Maturity | Standard Heston ($H = 0.5$) | Rough Heston ($H = 0.1$) |
|:---:|:---:|:---:|
| 1 week | $-2.8$ | $-8.5$ |
| 1 month | $-2.7$ | $-5.1$ |
| 3 months | $-2.5$ | $-3.6$ |
| 1 year | $-2.1$ | $-2.3$ |
| 2 years | $-1.8$ | $-1.9$ |

(Skew measured as $\partial\sigma_{\text{imp}} / \partial\ln K$ at ATM, in percentage per unit log-moneyness.)

!!! example "Observations"

    1. The rough Heston ATM skew at 1 week ($-8.5$) is **three times steeper** than standard Heston ($-2.8$), matching the empirically observed steep short-maturity equity skew.
    2. At 1--2 year maturities, the two models produce similar skews ($-2.3$ vs $-1.8$), as the long-term behavior is governed by mean reversion in both cases.
    3. The rough Heston skew increases rapidly as $T \to 0$, consistent with the $T^{H-1/2}$ power law. Standard Heston skew is approximately constant for short maturities.

---

## Summary

| Concept | Description |
|---------|-------------|
| Hurst parameter | $H \approx 0.1$ from high-frequency variance analysis |
| Fractional kernel | $K_H(t) = t^{H-1/2}/\Gamma(H+1/2)$ |
| Variance dynamics | Volterra integral with kernel $K_H$ |
| CF equation | Fractional Riccati: $h(t) = \int_0^t K_H(t-s)F(h(s))ds$ |
| ATM skew scaling | $T^{H-1/2}$ (diverges for $H < 1/2$) |

!!! abstract "Key Takeaways"

    1. **Empirical roughness**: Realized volatility has Hurst parameter $H \approx 0.1$, ruling out Markovian diffusion models like standard Heston ($H = 0.5$).

    2. **Fractional kernel**: The rough Heston model replaces the CIR SDE with a Volterra integral driven by the singular kernel $K_H(t) = t^{H-1/2}/\Gamma(H+1/2)$.

    3. **Fractional Riccati**: The characteristic function satisfies a Volterra Riccati integral equation, generalizing the standard Heston Riccati ODE. No closed-form solution exists for $H \neq 1/2$.

    4. **Steep short-maturity skew**: The ATM skew diverges as $T^{H-1/2}$ for $H < 1/2$, naturally producing the steep short-maturity smiles that standard Heston cannot fit without jumps.

    5. **Computational trade-off**: The non-Markovian dynamics increase computational cost ($\mathcal{O}(N^2)$ for CF evaluation), but Markovian multi-factor approximations largely mitigate this.

---

## What's Next

| Section | Topic |
|---------|-------|
| [Bates Model](bates_model.md) | Jump-based alternative for short-maturity smile |
| [Double Heston Model](double_heston_model.md) | Multi-factor Markovian approach |
| [Time-Dependent Parameters](time_dependent_parameters.md) | Piecewise-constant calibration |

---

## Exercises

**Exercise 1.**
The fractional kernel is $K_H(t) = t^{H-1/2}/\Gamma(H+1/2)$. For $H = 0.1$, compute $K_H(t)$ at $t = 0.001, 0.01, 0.1, 1.0$. Compare with the standard Markovian case $H = 0.5$ where $K_{0.5}(t) = 1/\Gamma(1) = 1$ (constant kernel). Explain why the rough kernel $K_{0.1}(t) \propto t^{-0.4}$ diverges as $t \to 0$ and what this means for the regularity of variance paths.

??? success "Solution to Exercise 1"
    The fractional kernel is $K_H(t) = t^{H-1/2}/\Gamma(H+1/2)$.

    **For $H = 0.1$:** We need $\Gamma(0.6)$. Using the gamma function, $\Gamma(0.6) \approx 1.4892$. The kernel is:

    $$
    K_{0.1}(t) = \frac{t^{0.1 - 0.5}}{\Gamma(0.6)} = \frac{t^{-0.4}}{1.4892}
    $$

    Computing at the specified values:

    | $t$ | $t^{-0.4}$ | $K_{0.1}(t)$ | $K_{0.5}(t)$ |
    |:---:|:---:|:---:|:---:|
    | 0.001 | $0.001^{-0.4} = 10^{1.2} = 15.849$ | $10.643$ | $1$ |
    | 0.01 | $0.01^{-0.4} = 10^{0.8} = 6.310$ | $4.237$ | $1$ |
    | 0.1 | $0.1^{-0.4} = 10^{0.4} = 2.512$ | $1.687$ | $1$ |
    | 1.0 | $1.0^{-0.4} = 1$ | $0.672$ | $1$ |

    **Key observations:**

    The rough kernel $K_{0.1}(t) \propto t^{-0.4}$ diverges as $t \to 0^+$ because $-0.4 < 0$. In contrast, the standard kernel $K_{0.5}(t) = 1$ is a constant.

    The divergence of $K_{0.1}$ at the origin has a direct consequence for the regularity of variance paths. In the Volterra integral:

    $$
    v_t = v_0 + \int_0^t K_H(t-s) \, \kappa(\theta - v_s) \, ds + \int_0^t K_H(t-s) \, \xi\sqrt{v_s} \, dW_s
    $$

    the singular kernel amplifies the effect of the most recent Brownian increments (where $t - s \approx 0$). This produces a variance process whose increments over short intervals $\Delta$ scale as $\Delta^H = \Delta^{0.1}$, meaning the variance changes almost as much over a small interval as over a larger one. The paths are highly irregular ("rough") with local fluctuations that are much more pronounced than those of the standard CIR process ($H = 0.5$).

    Quantitatively, at $t = 0.001$ (roughly 6 hours of trading), the rough kernel value is $10.643$ --- more than 10 times the standard kernel value of $1$. This means that a noise increment at lag $\Delta = 0.001$ is amplified 10-fold relative to the standard case, producing the erratic short-term fluctuations observed in realized volatility data.

---

**Exercise 2.**
The Hurst parameter $H$ controls the roughness of volatility paths via $\mathbb{E}[|v_{t+\Delta} - v_t|^2] \sim \Delta^{2H}$. For $H = 0.1$, compute this scaling for $\Delta = 1$ day, 1 hour, and 1 minute (in fractions of a year). Compare with $H = 0.5$. Why does smaller $H$ produce "rougher" paths?

??? success "Solution to Exercise 2"
    The scaling relation is $\mathbb{E}[|v_{t+\Delta} - v_t|^2] \sim \Delta^{2H}$. We compute this for both $H = 0.1$ and $H = 0.5$.

    First, convert time intervals to fractions of a year (assuming 252 trading days, 6.5 hours per day):

    - 1 day: $\Delta = 1/252 \approx 0.003968$
    - 1 hour: $\Delta = 1/(252 \times 6.5) \approx 0.000610$
    - 1 minute: $\Delta = 1/(252 \times 6.5 \times 60) \approx 0.00001017$

    **For $H = 0.1$ ($2H = 0.2$):**

    | Time scale | $\Delta$ | $\Delta^{0.2}$ |
    |:---:|:---:|:---:|
    | 1 day | $3.968 \times 10^{-3}$ | $(3.968 \times 10^{-3})^{0.2} = 0.3280$ |
    | 1 hour | $6.10 \times 10^{-4}$ | $(6.10 \times 10^{-4})^{0.2} = 0.2247$ |
    | 1 minute | $1.017 \times 10^{-5}$ | $(1.017 \times 10^{-5})^{0.2} = 0.1029$ |

    **For $H = 0.5$ ($2H = 1.0$):**

    | Time scale | $\Delta$ | $\Delta^{1.0}$ |
    |:---:|:---:|:---:|
    | 1 day | $3.968 \times 10^{-3}$ | $3.968 \times 10^{-3}$ |
    | 1 hour | $6.10 \times 10^{-4}$ | $6.10 \times 10^{-4}$ |
    | 1 minute | $1.017 \times 10^{-5}$ | $1.017 \times 10^{-5}$ |

    **Comparison of ratios:** Going from 1 day to 1 minute (a factor of $390$ reduction in $\Delta$):

    - $H = 0.5$: the variance of increments decreases by factor $390^1 = 390$
    - $H = 0.1$: the variance of increments decreases by factor $390^{0.2} = 3.30$

    Smaller $H$ produces "rougher" paths because the increments shrink much more slowly as the time scale decreases. With $H = 0.1$, the minute-to-minute fluctuations in variance are only about 3 times smaller than the day-to-day fluctuations (in mean-square), whereas with $H = 0.5$, they are 390 times smaller. This means the rough process exhibits substantial variability at every time scale, producing paths that are visually much more jagged and irregular. The local Holder exponent of the paths is $H$, so smaller $H$ means less regularity and more rapid oscillation.

---

**Exercise 3.**
In the rough Heston model, the variance process is non-Markovian: $v_t$ depends on the entire history $\{v_s : s < t\}$, not just the current state. Explain why this makes Monte Carlo simulation more expensive than for the standard Heston model. If a standard Heston QE step requires $O(1)$ operations, and a rough Heston step requires accessing the full history, what is the cost per path of $N$ steps?

??? success "Solution to Exercise 3"
    In the standard Heston model with the QE scheme, simulating the variance at step $n+1$ requires only the current variance $v_n$ (Markov property). The cost per step is $\mathcal{O}(1)$.

    In the rough Heston model, the variance at step $n$ depends on the entire history through the Volterra integral:

    $$
    v_{t_n} = v_0 + \sum_{k=0}^{n-1} K_H(t_n - t_k) \, \kappa(\theta - v_{t_k}) \, \Delta t + \sum_{k=0}^{n-1} K_H(t_n - t_k) \, \xi\sqrt{v_{t_k}} \, \Delta W_k
    $$

    To compute $v_{t_n}$, one must evaluate the convolution sum over all previous steps $k = 0, 1, \ldots, n-1$. This requires:

    - Storing the full history $\{v_{t_0}, v_{t_1}, \ldots, v_{t_{n-1}}\}$ and $\{\Delta W_0, \ldots, \Delta W_{n-1}\}$: $\mathcal{O}(n)$ memory
    - Computing the weighted sum with kernel weights $K_H(t_n - t_k)$ for each $k$: $\mathcal{O}(n)$ operations per step

    Over a full path of $N$ steps, the total cost is:

    $$
    \sum_{n=1}^{N} \mathcal{O}(n) = \mathcal{O}(N^2)
    $$

    compared to $\mathcal{O}(N)$ for the standard Heston model. For a typical daily simulation over 1 year ($N = 252$), the rough Heston Monte Carlo is approximately $252/2 \approx 126$ times more expensive per path.

    **Mitigation strategies:**

    1. **Truncation:** Discard kernel contributions beyond a cutoff lag $L$ (since $K_H(t) \to 0$ as $t \to \infty$), reducing cost to $\mathcal{O}(NL)$
    2. **Markovian approximation:** Approximate $K_H$ by a sum of $M$ exponentials, converting the Volterra equation into $M$ coupled Markovian SDEs with $\mathcal{O}(MN)$ total cost
    3. **Hybrid schemes:** Use the exact fractional kernel for recent lags and an exponential approximation for distant lags

---

**Exercise 4.**
The characteristic function of the rough Heston model satisfies a fractional Riccati equation. Unlike the standard Riccati ODE (which has a closed-form solution), the fractional Riccati must be solved numerically. Describe the Adams method for solving fractional ODEs and explain why it is well-suited to this problem.

??? success "Solution to Exercise 4"
    The fractional Riccati equation for the rough Heston model is a Volterra integral equation of the second kind:

    $$
    h(t) = \int_0^t K_H(t - s) \, F(h(s)) \, ds
    $$

    where $F(x) = \frac{1}{2}\xi^2 x^2 + (\rho\xi iu - \kappa)x + \frac{1}{2}(iu - u^2)$ and $K_H(t) = t^{H-1/2}/\Gamma(H+1/2)$.

    **The Adams method** for Volterra equations proceeds as follows:

    **Step 1 (Discretization):** Choose a uniform grid $t_n = n\Delta t$ for $n = 0, 1, \ldots, N$ with $\Delta t = T/N$. Set $h(0) = 0$.

    **Step 2 (Predictor):** At step $n$, approximate the integral using an explicit quadrature (Adams-Bashforth type):

    $$
    h^P(t_n) = \sum_{k=0}^{n-1} b_{n,k} \, K_H(t_n - t_k) \, F(h(t_k)) \, \Delta t
    $$

    where $b_{n,k}$ are the quadrature weights (e.g., trapezoidal: $b_{n,0} = b_{n,n-1} = 1/2$, $b_{n,k} = 1$ otherwise).

    **Step 3 (Corrector):** Refine using the implicit Adams-Moulton formula that includes the predicted value:

    $$
    h(t_n) = \sum_{k=0}^{n-1} b_{n,k} \, K_H(t_n - t_k) \, F(h(t_k)) \, \Delta t + b_{n,n} \, K_H(\Delta t) \, F(h^P(t_n)) \, \Delta t
    $$

    This predictor-corrector approach is repeated for each $n$.

    **Why the Adams method is well-suited:**

    1. **Handles the singular kernel:** The kernel $K_H(t) = t^{H-1/2}/\Gamma(H+1/2)$ is singular at $t = 0$ for $H < 1/2$. The Adams scheme can incorporate product integration weights $w_{n,k} = \int_{t_k}^{t_{k+1}} K_H(t_n - s) \, ds$ that analytically integrate the singular kernel factor, avoiding numerical instability from evaluating $K_H$ at the singularity.

    2. **Naturally handles non-locality:** The convolution structure of the Volterra equation means each step requires the full history. The Adams method computes this sum incrementally --- at step $n$, one adds the contribution of step $n-1$ to the running sum, reusing the $\mathcal{O}(n-1)$ computation from the previous step (though the kernel weights change, requiring $\mathcal{O}(n)$ work per step).

    3. **Good convergence:** With product integration to handle the kernel singularity, the Adams method achieves convergence of order $\min(p, 1+H)$ where $p$ is the order of the underlying quadrature. For $H = 0.1$, this limits the convergence to about order $1.1$, but practical accuracy is sufficient with moderate $N$.

    4. **Complex-valued:** The Riccati function $F$ and solution $h$ are complex-valued (since $u$ is the Fourier variable). The Adams method handles complex arithmetic without modification.

---

**Exercise 5.**
Empirically, $H \approx 0.1$ for equity indices. The ATM skew in the rough Heston model behaves as $T^{H-1/2}$ for short maturities. Compare $T^{0.1 - 0.5} = T^{-0.4}$ (rough Heston) with $T^{-0.5}$ (standard Heston) for $T = 1/252, 1/52, 1/12$. Which model produces steeper short-maturity skews? How does this compare with the Bates model's approach to steep short-maturity smiles?

??? success "Solution to Exercise 5"
    We compare the ATM skew scaling $T^{H-1/2}$ for both models at short maturities.

    **Rough Heston ($H = 0.1$):** Skew $\sim T^{-0.4}$

    | Maturity | $T$ (years) | $T^{-0.4}$ |
    |:---:|:---:|:---:|
    | 1 day | $1/252 = 0.003968$ | $0.003968^{-0.4} = 22.14$ |
    | 1 week | $1/52 = 0.01923$ | $0.01923^{-0.4} = 12.75$ |
    | 1 month | $1/12 = 0.08333$ | $0.08333^{-0.4} = 7.25$ |

    **Standard Heston ($H = 0.5$):** Skew $\sim T^{0} = 1$ (constant). The ATM skew approaches the finite limit $\rho\xi/(4\sqrt{v_0})$ as $T \to 0$.

    | Maturity | $T$ (years) | $T^{0}$ |
    |:---:|:---:|:---:|
    | 1 day | $1/252$ | $1$ |
    | 1 week | $1/52$ | $1$ |
    | 1 month | $1/12$ | $1$ |

    **Comparison:** The rough Heston skew at 1 day is $22.14$ times the long-maturity baseline, while the standard Heston skew is constant. The rough Heston model produces dramatically steeper short-maturity skews, diverging as $T \to 0$.

    Note: the standard Heston exponent is $H - 1/2 = 0$ (constant skew limit), not $T^{-0.5}$. The $T^{-0.5}$ scaling would correspond to $H = 0$, which is not physical.

    **Comparison with the Bates model:** The Bates model achieves steep short-maturity skews through a fundamentally different mechanism --- discrete jumps in the stock price. The Bates short-maturity skew converges to a finite constant $\lambda\mu_J/(2\sqrt{v_0})$ as $T \to 0$ (it does not diverge). The rough Heston skew actually **diverges** as $T^{-0.4}$, which better matches the empirical observation that equity skews become extremely steep at very short maturities.

    Key differences:

    - **Bates:** Skew $\to$ finite constant as $T \to 0$. Requires three extra parameters ($\lambda, \mu_J, \sigma_J$). The jump mechanism is somewhat ad hoc and does not explain the roughness of realized volatility paths.
    - **Rough Heston:** Skew $\to \infty$ as $T \to 0$. Requires one extra parameter ($H$, replacing one degree of freedom). The rough mechanism is directly motivated by the empirical observation of $H \approx 0.1$ in realized volatility. However, the computational cost is significantly higher.

---

**Exercise 6.**
The rough Heston model nests the standard Heston model as the special case $H = 0.5$. Verify that the fractional kernel $K_{0.5}(t) = 1/\Gamma(1) = 1$ is constant and that the Volterra integral equation reduces to the standard CIR ODE. Discuss the practical implications: if $H = 0.5$ were the true value, would the rough Heston framework add any value?

??? success "Solution to Exercise 6"
    **Verification that $K_{0.5}(t) = 1$:**

    $$
    K_{0.5}(t) = \frac{t^{0.5 - 0.5}}{\Gamma(0.5 + 0.5)} = \frac{t^0}{\Gamma(1)} = \frac{1}{1} = 1
    $$

    Since $\Gamma(1) = 0! = 1$ and $t^0 = 1$ for all $t > 0$, the kernel is indeed constant.

    **Reduction to the CIR ODE:** Substituting $K_{0.5}(t) = 1$ into the Volterra integral equation for the variance:

    $$
    v_t = v_0 + \int_0^t 1 \cdot \kappa(\theta - v_s) \, ds + \int_0^t 1 \cdot \xi\sqrt{v_s} \, dW_s
    $$

    $$
    = v_0 + \int_0^t \kappa(\theta - v_s) \, ds + \int_0^t \xi\sqrt{v_s} \, dW_s
    $$

    Differentiating both sides with respect to $t$ (by the fundamental theorem of calculus and the properties of Ito integrals):

    $$
    dv_t = \kappa(\theta - v_t) \, dt + \xi\sqrt{v_t} \, dW_t
    $$

    This is exactly the standard CIR SDE.

    Similarly, the fractional Riccati equation with $K_{0.5} = 1$:

    $$
    h(t) = \int_0^t 1 \cdot F(h(s)) \, ds
    $$

    Differentiating: $h'(t) = F(h(t))$ with $h(0) = 0$, which is the standard Heston Riccati ODE.

    **Practical implications if $H = 0.5$ were the true value:**

    If empirical analysis showed $H = 0.5$, the rough Heston framework would add **no value** over the standard Heston model:

    1. **Mathematically equivalent:** The rough Heston model with $H = 0.5$ is exactly the standard Heston model, so no additional modeling power is gained.

    2. **Computational cost is strictly higher:** The Volterra formulation requires $\mathcal{O}(N^2)$ operations for CF evaluation (or $\mathcal{O}(MN)$ with Markovian approximation), compared to the closed-form $\mathcal{O}(1)$ Riccati solution of standard Heston. Using the rough Heston numerical framework when $H = 0.5$ would be computationally wasteful, since the exact closed-form solution is available.

    3. **Monte Carlo is path-dependent for no reason:** The Volterra simulation stores full path history at $\mathcal{O}(N^2)$ cost, while the Markovian CIR simulation requires only the current state at $\mathcal{O}(N)$ cost.

    4. **No smile improvement:** The standard Heston limitations (constant short-maturity skew, exponential autocorrelation decay) would persist, since $H = 0.5$ produces identical dynamics.

    The entire motivation for rough Heston rests on the empirical finding $H \approx 0.1 \ll 0.5$. If this finding were overturned, the rough volatility program would lose its justification, and practitioners would be better served by standard Heston or its Markovian extensions (double Heston, Bates).
