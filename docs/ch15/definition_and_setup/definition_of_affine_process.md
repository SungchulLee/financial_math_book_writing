# Definition of Affine Process

An affine process is a class of stochastic processes with particularly tractable properties. Their defining characteristic is that both the drift and diffusion matrix are linear in the state variable, and the short rate is linear in the state.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand the definition and key properties of affine processes
    2. Recognize when a process is affine
    3. Apply the Duffie-Pan-Singleton framework to model interest rates
    4. Work with the characteristic function of affine processes

---

## Overview

Affine processes form a class of continuous-time stochastic processes that are particularly important in financial mathematics, especially for term structure modeling. Their tractability comes from a linearity structure that allows for closed-form or semi-closed-form solutions for bond prices and derivatives.

---

## Mathematical Framework

### Definition of an Affine Process

A state vector $\mathbf{X}_t \in \mathbb{R}^n$ follows an affine process if its dynamics under a risk-neutral measure $\mathbb{Q}$ are:

$$
d\mathbf{X}_t = \bar{\mu}(\mathbf{X}_t)dt + \bar{\sigma}(\mathbf{X}_t)d\mathbf{W}_t
$$

and satisfy the following **linearity conditions**:

$$
\begin{array}{lll}
\displaystyle \bar{\mu}(\mathbf{X}_t) = a_0 + a_1 \mathbf{X}_t & \quad & \text{(Drift is linear in } \mathbf{X}_t\text{)}\\
\displaystyle \bar{\sigma}(\mathbf{X}_t)\bar{\sigma}(\mathbf{X}_t)^T = c_0 + c_1^T \mathbf{X}_t & \quad & \text{(Diffusion is linear in } \mathbf{X}_t\text{)}\\
\displaystyle r(\mathbf{X}_t) = r_0 + r_1^T \mathbf{X}_t & \quad & \text{(Short rate is linear in } \mathbf{X}_t\text{)}\\
\end{array}
$$

where:
- $a_0 \in \mathbb{R}^n$ and $a_1 \in \mathbb{R}^{n \times n}$ are constant matrices for the drift
- $c_0 \in \mathbb{R}^{n \times n}$ and $c_1 \in \mathbb{R}^{n \times n}$ define the volatility structure
- $r_0 \in \mathbb{R}$ and $r_1 \in \mathbb{R}^n$ define the short rate

### Characteristic Function

The power of the affine framework lies in the conditional characteristic function:

$$
\varphi(\mathbf{X}_t, t, T, \mathbf{u}) := \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r(\mathbf{X}_s)ds} e^{i\mathbf{u}^T\mathbf{X}_T} \Big| \mathcal{F}_t\right]
$$

For an affine process, this takes an **affine form**:

$$
\varphi(\mathbf{X}_t, t, T, \mathbf{u}) = e^{A(\tau, \mathbf{u}) + \mathbf{B}^T(\tau, \mathbf{u})\mathbf{X}_t}
$$

where:
- $\tau = T - t$ is the time to maturity
- $A(\tau, \mathbf{u})$ and $\mathbf{B}(\tau, \mathbf{u})$ are determined by **Riccati equations**
- **Terminal conditions**: $A(0, \mathbf{u}) = 0$ and $\mathbf{B}(0, \mathbf{u}) = \mathbf{u}$

### Riccati Equations

The functions $A(\tau, \mathbf{u})$ and $\mathbf{B}(\tau, \mathbf{u})$ satisfy the system of Riccati equations (with terminal conditions at $\tau = 0$):

$$
\begin{array}{lll}
\displaystyle -\frac{\partial A}{\partial \tau} &=& r_0 - \mathbf{B}^T a_0 - \frac{1}{2}\mathbf{B}^T c_0 \mathbf{B}\\
\displaystyle -\frac{\partial \mathbf{B}}{\partial \tau} &=& r_1 - a_1^T \mathbf{B} - \frac{1}{2}c_1^T \mathbf{B} \mathbf{B}\\
\end{array}
$$

Or equivalently, integrating backward from maturity:

$$
\begin{array}{lll}
\displaystyle \frac{dA}{d\tau} &=& -r_0 + \mathbf{B}^T a_0 + \frac{1}{2}\mathbf{B}^T c_0 \mathbf{B}\\
\displaystyle \frac{d\mathbf{B}}{d\tau} &=& -r_1 + a_1^T \mathbf{B} + \frac{1}{2}\mathbf{B}^T c_1 \mathbf{B}\\
\end{array}
$$

### Bond Pricing

The zero-coupon bond price is directly obtained from the characteristic function:

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r(\mathbf{X}_s)ds} \Big| \mathcal{F}_t\right] = e^{A(T-t, 0) + \mathbf{B}^T(T-t, 0)\mathbf{X}_t}
$$

This gives an **exponential-affine form** for bond prices:

$$
P(t, T) = \exp\left(A(T-t) + \mathbf{B}^T(T-t)\mathbf{X}_t\right)
$$

---

## Key Properties

### 1. Closed-Form Bond Prices

Once the Riccati equations are solved, bond prices have a closed-form exponential-affine structure. This is a major computational advantage.

### 2. Solvability

The Riccati equations can often be solved:
- **Analytically** for certain specifications (e.g., Vasicek, Hull-White)
- **Semi-analytically** for others
- **Numerically** for complex models

### 3. Characteristic Function Availability

The explicit affine form of the characteristic function enables:
- Fourier inversion to compute option prices
- Fast computation of bond prices and yields
- Closed-form or semi-analytical derivatives

### 4. State Space Flexibility

Affine models can incorporate:
- Multiple factors (multidimensional $\mathbf{X}_t$)
- Regime switching
- Jumps (in extended formulations)

---

## Examples of Affine Processes

### Vasicek Model

State variable: $X_t = r_t$ (short rate), one-dimensional.

Dynamics:
$$dr_t = \kappa(\theta - r_t)dt + \sigma dW_t$$

Affine parameters:
- $a_0 = \kappa\theta$, $a_1 = -\kappa$
- $c_0 = \sigma^2$, $c_1 = 0$
- $r_0 = 0$, $r_1 = 1$

This is a classic affine model with analytical Riccati solutions.

### Two-Factor CIR + Vasicek

State variables: $X_t = (r_t, s_t)$ where $r_t$ is a CIR process and $s_t$ is a Vasicek long-rate factor.

Both components are affine, and the sum is affine, making it suitable for modeling mean reversion with stochastic long rates.

### Geometric Brownian Motion (Transformed)

The stock price $S_t$ itself is **not** affine (see the detailed example in the next section), but $X_t = \log S_t$ is affine.

---

## Why Affine Processes Matter

1. **Computational Efficiency**: Closed-form or semi-analytical solutions for bond prices eliminate numerical integration.

2. **Calibration**: The structure enables efficient likelihood-based or moment-matching estimation.

3. **Generality**: Despite linearity restrictions, affine models are flexible enough for practical applications.

4. **Extensions**: The framework extends to affine jump-diffusions, multivariate cases, and hybrid models.

---

## Summary

An affine process is defined by linearity of:
- Drift in the state variable
- Diffusion matrix in the state variable
- Short rate in the state variable

This structure guarantees that the characteristic function (and hence bond prices) have a closed-form exponential-affine structure, leading to tractable analytical and numerical methods. The Duffie-Pan-Singleton framework provides the theoretical foundation for both single and multi-factor affine term structure models.

---

## Further Reading

- Duffie, D., Pan, J., & Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343-1376.
- Filipović, D. *Term-Structure Models: A Graduate Course*. Springer, 2009.
- Brigo, D., & Mercurio, F. *Interest Rate Models - Theory and Practice*. Springer, 2007.
