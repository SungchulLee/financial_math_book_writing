# Hull-White Model Class Guide

This guide describes the design and implementation of the `HullWhite` class, the central object for one-factor Hull-White model computations. The class encapsulates the model parameters $(\sigma, \lambda)$ and the market yield curve $P^M(0,T)$, and provides methods for computing the named functions, bond prices, short rate simulation, and derivative pricing. The companion `.py` file contains the full implementation; this page explains the design choices and maps each method to its mathematical formula.

## Class Overview

The `HullWhite` class is initialized with three inputs:

- `sigma`: the short rate volatility $\sigma > 0$
- `lambd`: the mean-reversion speed $\lambda > 0$
- `P`: a callable representing the market discount curve $P^M(0, T)$

All other quantities ($\theta(t)$, $A(t,T)$, $B(t,T)$, the short rate distribution parameters) are derived from these three inputs.

## Constructor and Parameters

```python
class HullWhite:
    def __init__(self, sigma, lambd, P):
        self.sigma = sigma
        self.lambd = lambd
        self.P = P
```

The market curve `P` is a function $P^M: [0, \infty) \to (0, 1]$ satisfying $P^M(0) = 1$. In practice, this is obtained by interpolating market bond prices or by fitting a parametric model (e.g., Nelson-Siegel) to swap rates.

## Named Function Methods

### compute_B(t, T)

Computes the duration-like function:

$$
B(t, T) = \frac{e^{-\lambda(T-t)} - 1}{\lambda}
$$

This function appears in the bond price formula, the bond volatility, and the measure change.

### compute_A(t, T)

Computes the bond price intercept function by numerical integration:

$$
A(\tau) = -\frac{\sigma^2}{4\lambda^3}\left(3 - 2\lambda\tau - 4e^{-\lambda\tau} + e^{-2\lambda\tau}\right) + \lambda\int_0^\tau \theta(T - \tau')B(\tau')\,d\tau'
$$

The integral is evaluated using the trapezoidal rule on a grid of 250 points. The function `compute_theta` provides the integrand.

### compute_theta(t)

Computes the time-dependent drift:

$$
\theta(t) = f^M(0, t) + \frac{1}{\lambda}\frac{\partial f^M(0, t)}{\partial t} + \frac{\sigma^2}{2\lambda^2}\left(1 - e^{-2\lambda t}\right)
$$

where $f^M(0, t)$ is the instantaneous forward rate, obtained by numerical differentiation of $\ln P^M(0, t)$.

### compute_theta_T(t, T)

Computes the drift under the $T$-forward measure:

$$
\theta^{\mathbb{T}}(t) = \theta(t) + \frac{\sigma^2}{\lambda}B(T - t)
$$

## Bond Pricing Methods

### compute_ZCB(t, T, r_t)

Computes the zero-coupon bond price:

$$
P(t, T) = \exp\!\bigl(A(t, T) + B(t, T)\,r_t\bigr)
$$

### compute_sigma_P(t, T)

Computes the bond price volatility:

$$
\sigma_P(t, T) = \sigma\,B(t, T)
$$

## Short Rate Distribution Methods

### compute_mu_r_T(T)

Computes the conditional mean of $r_T$ under $\mathbb{Q}$:

$$
\mu_r(T) = r_0\,e^{-\lambda T} + \lambda\int_0^T \theta(s)\,e^{-\lambda(T-s)}\,ds
$$

### compute_mu_r_T_ForwardMeasure(T)

Computes the conditional mean of $r_T$ under $\mathbb{Q}^T$:

$$
\mu_r^{\mathbb{T}}(T) = r_0\,e^{-\lambda T} + \lambda\int_0^T \theta^{\mathbb{T}}(s)\,e^{-\lambda(T-s)}\,ds
$$

### compute_sigma_square_r_T(T)

Computes the conditional variance of $r_T$:

$$
\sigma_r^2(T) = \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda T}\right)
$$

This variance is the same under both $\mathbb{Q}$ and $\mathbb{Q}^T$ because the Girsanov transformation only changes the drift, not the diffusion.

## Simulation Methods

### generate_sample_paths(num_paths, num_steps, T, seed)

Generates short rate paths using Euler-Maruyama discretization:

$$
r_{t_{i+1}} = r_{t_i} + \lambda\left(\theta(t_i) - r_{t_i}\right)\Delta t + \sigma\,\sqrt{\Delta t}\,Z_{i+1}
$$

where $Z_{i+1} \sim N(0, 1)$. The method also computes the money market account $M(t_i) = \prod_{k=0}^{i-1}e^{r_{t_k}\Delta t}$.

Returns: time grid `t`, short rate paths `R`, money market account `M`.

!!! tip "Moment Matching"
    When `num_paths > 1`, the normal draws are centered and standardized: $Z_i \leftarrow (Z_i - \bar{Z}) / \text{std}(Z)$. This ensures that the sample mean and variance match the theoretical values exactly, reducing Monte Carlo bias for finite samples.

## Derivative Pricing Methods

### compute_ZCB_Option_Price(K, T1, T2, CP)

Prices a European call or put on a ZCB $P(T_1, T_2)$ with strike $K$:

$$
V = P(0, T_1)\,e^{A(\tau)}\left[e^{\frac{1}{2}B^2(\tau)\sigma_r^2 + B(\tau)\mu_r^{\mathbb{T}}}\,N(d_1) - \hat{K}\,N(d_2)\right]
$$

The put price uses put-call parity: $\text{Put} = \text{Call} - P(0, T_2) + K\,P(0, T_1)$.

### compute_Caplet_Floorlet_Price(N, K, T1, T2, CP)

Prices a caplet or floorlet using the caplet-as-ZCB-put relationship:

$$
\text{Caplet}(K) = (1 + \delta K)\,\text{Put}\!\left(\frac{1}{1+\delta K}\right)
$$

where $\delta = T_2 - T_1$.

### compute_SwapPrice(t, r_t, notional, K, Ti, Tm, n, CP)

Computes the swap value at time $t$ given $r_t$:

$$
V_{\text{swap}} = N\left[P(t, T_i) - P(t, T_m) - K\sum_{k} \delta_k\,P(t, T_k)\right]
$$

## Design Principles

1. **Single responsibility**: each method computes one named function or formula
2. **Composability**: complex computations (e.g., swaption pricing via Jamshidian) compose simpler methods
3. **Market curve as input**: the class takes $P^M(0,T)$ as a callable, allowing any curve representation (interpolation, parametric, bootstrap)
4. **Numerical differentiation**: forward rates and their derivatives are computed by central differences with step size $10^{-4}$, avoiding the need for an explicit forward curve representation

## Summary

The `HullWhite` class implements the complete one-factor Hull-White model computation chain: from model parameters and market curve through named functions ($\theta$, $A$, $B$), bond pricing, short rate simulation, and derivative pricing (ZCB options, caplets, swaps). Each method maps directly to a mathematical formula from the theory sections, with numerical integration and differentiation used where closed-form expressions require the initial forward curve. The class is designed for composability, enabling the construction of higher-level pricing and calibration routines.
