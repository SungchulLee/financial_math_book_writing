# Rough Heston Model (Overview)

## Introduction

High-frequency analysis of realized volatility reveals a striking empirical fact: the **log-volatility** of equity indices behaves like a fractional Brownian motion with **Hurst parameter** $H \approx 0.1$, far below the classical value $H = 0.5$ of standard Brownian motion. This means volatility paths are **rougher** than Brownian motion --- they have more rapid local fluctuations and exhibit power-law behavior $\mathbb{E}[|v_{t+\Delta} - v_t|^2] \sim \Delta^{2H}$ with $H < 0.5$.

The standard Heston model, built on the CIR process (a Markovian diffusion with $H = 0.5$), cannot reproduce this roughness signature. The **rough Heston model** (El Euch and Rosenbaum, 2019) replaces the CIR variance process with a Volterra-type integral equation driven by a **fractional kernel** $K_H(t) = t^{H-1/2} / \Gamma(H + 1/2)$. The resulting process is non-Markovian, but the characteristic function still satisfies a (fractional) Riccati equation, preserving much of the analytical tractability of the standard Heston model.

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

In the standard Heston model, the function $D(\tau, u)$ satisfies the ODE:

$$
\frac{dD}{d\tau} = F(D), \qquad D(0, u) = 0
$$

The rough Heston replaces this ODE with a **Volterra integral equation** of the second kind:

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
