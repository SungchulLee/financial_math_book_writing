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

---

## Exercises

**Exercise 1.** Using a flat market curve at 4\% and Hull-White parameters $\sigma = 0.01$, $\lambda = 0.10$, compute $\theta(t)$ for $t = 0.5, 1, 5, 10$ years. Verify that in the flat-curve case, $\theta(t)$ converges to the long-run level $r + \sigma^2/(2\lambda^2)$ as $t \to \infty$. What is the numerical value of this limit?

??? success "Solution to Exercise 1"
    For a flat market curve at 4%, we have $P^M(0, t) = e^{-0.04\,t}$, so the instantaneous forward rate is $f^M(0, t) = 0.04$ for all $t$, and $\partial f^M / \partial t = 0$. The $\theta(t)$ formula simplifies to:

    $$
    \theta(t) = 0.04 + 0 + \frac{(0.01)^2}{2(0.10)^2}(1 - e^{-2 \cdot 0.10 \cdot t}) = 0.04 + 0.005(1 - e^{-0.2t})
    $$

    Computing at the specified times:

    - $t = 0.5$: $\theta(0.5) = 0.04 + 0.005(1 - e^{-0.1}) = 0.04 + 0.005 \times 0.09516 = 0.04048$
    - $t = 1$: $\theta(1) = 0.04 + 0.005(1 - e^{-0.2}) = 0.04 + 0.005 \times 0.18127 = 0.04091$
    - $t = 5$: $\theta(5) = 0.04 + 0.005(1 - e^{-1.0}) = 0.04 + 0.005 \times 0.63212 = 0.04316$
    - $t = 10$: $\theta(10) = 0.04 + 0.005(1 - e^{-2.0}) = 0.04 + 0.005 \times 0.86466 = 0.04432$

    As $t \to \infty$, $e^{-2\lambda t} \to 0$, so:

    $$
    \lim_{t \to \infty} \theta(t) = r + \frac{\sigma^2}{2\lambda^2} = 0.04 + \frac{(0.01)^2}{2(0.10)^2} = 0.04 + 0.005 = 0.045
    $$

    The long-run level is $0.045$ or 4.5%. The convexity adjustment $\sigma^2/(2\lambda^2)$ raises the drift target above the flat rate to compensate for the Jensen inequality effect in bond pricing.

---

**Exercise 2.** The `compute_B(t, T)` method returns $(e^{-\lambda(T-t)} - 1)/\lambda$. Show that $B(t, T) \to -(T-t)$ as $\lambda \to 0$ and $B(t, T) \to -1/\lambda$ as $T - t \to \infty$. Interpret each limit financially in terms of the bond price sensitivity to the short rate.

??? success "Solution to Exercise 2"
    **Limit as $\lambda \to 0$:** Apply L'Hopital's rule or a Taylor expansion. Write $e^{-\lambda\tau} \approx 1 - \lambda\tau + \frac{1}{2}\lambda^2\tau^2 - \cdots$, so:

    $$
    B(t, T) = \frac{e^{-\lambda(T-t)} - 1}{\lambda} = \frac{-\lambda\tau + \frac{1}{2}\lambda^2\tau^2 - \cdots}{\lambda} = -\tau + \frac{1}{2}\lambda\tau^2 - \cdots
    $$

    As $\lambda \to 0$, $B(t, T) \to -(T - t)$. This is the Vasicek limit with zero mean reversion: the bond price has log-linear sensitivity to the short rate with coefficient $-(T-t)$, identical to the duration of a zero-coupon bond under flat rates.

    **Limit as $T - t \to \infty$:** As $\tau \to \infty$, $e^{-\lambda\tau} \to 0$, so:

    $$
    B(t, T) = \frac{e^{-\lambda\tau} - 1}{\lambda} \to \frac{-1}{\lambda}
    $$

    This means the sensitivity of the bond price to the short rate saturates at $-1/\lambda$. Financially, mean reversion implies that the short rate will eventually revert to its long-run level regardless of its current value. Therefore, very long-dated bonds are insensitive to the current short rate beyond the mean-reversion horizon $1/\lambda$. A rate shock today has an effect that decays exponentially, so the bond price sensitivity cannot grow without bound.

---

**Exercise 3.** The variance of the short rate is $\sigma_r^2(T) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda T})$. This is the same under both $\mathbb{Q}$ and $\mathbb{Q}^T$. Explain why the Girsanov theorem guarantees this invariance. Compute $\sigma_r(T)$ for $T = 1$ and $T = 10$ with $\sigma = 0.01$, $\lambda = 0.05$.

??? success "Solution to Exercise 3"
    The Girsanov theorem states that the change of measure from $\mathbb{Q}$ to $\mathbb{Q}^T$ transforms the drift of the Brownian motion but does not alter the diffusion coefficient. In the Hull-White SDE:

    $$
    dr_t = \lambda(\theta(t) - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    Under $\mathbb{Q}^T$, the SDE becomes:

    $$
    dr_t = \lambda(\theta^{\mathbb{T}}(t) - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}^T}
    $$

    The volatility $\sigma$ is unchanged because the Girsanov density only introduces a drift adjustment to the Brownian motion. Since the conditional variance depends only on $\sigma$ and $\lambda$ (not on the drift), it is invariant under the measure change.

    Computing $\sigma_r(T)$ with $\sigma = 0.01$, $\lambda = 0.05$:

    $$
    \sigma_r^2(T) = \frac{(0.01)^2}{2 \times 0.05}(1 - e^{-2 \times 0.05 \times T}) = 0.001(1 - e^{-0.1T})
    $$

    For $T = 1$:

    $$
    \sigma_r^2(1) = 0.001(1 - e^{-0.1}) = 0.001 \times 0.09516 = 9.516 \times 10^{-5}
    $$

    $$
    \sigma_r(1) = \sqrt{9.516 \times 10^{-5}} \approx 0.00976 = 0.976\%
    $$

    For $T = 10$:

    $$
    \sigma_r^2(10) = 0.001(1 - e^{-1.0}) = 0.001 \times 0.63212 = 6.321 \times 10^{-4}
    $$

    $$
    \sigma_r(10) = \sqrt{6.321 \times 10^{-4}} \approx 0.02514 = 2.514\%
    $$

    The standard deviation grows from 0.976% at 1 year to 2.514% at 10 years, approaching the asymptotic limit $\sigma/\sqrt{2\lambda} = 0.01/\sqrt{0.1} \approx 3.162\%$.

---

**Exercise 4.** The `generate_sample_paths` method uses moment matching: $Z_i \leftarrow (Z_i - \bar{Z})/\text{std}(Z)$. Explain why this reduces Monte Carlo bias. Generate 10,000 paths for $T = 5$ years with $\sigma = 0.01$, $\lambda = 0.05$, flat curve at 3\%, and compare the sample mean and variance of $r_5$ with the analytical values from `compute_mu_r_T(5)` and `compute_sigma_square_r_T(5)`.

??? success "Solution to Exercise 4"
    **Why moment matching reduces bias:** In a standard Monte Carlo simulation, finite-sample draws from $N(0,1)$ will have sample mean $\bar{Z} \neq 0$ and sample variance $s^2 \neq 1$. These sampling errors propagate through the Euler-Maruyama scheme, biasing the terminal distribution of $r_T$. By applying $Z_i \leftarrow (Z_i - \bar{Z})/\text{std}(Z)$, we enforce $\bar{Z} = 0$ and $s^2 = 1$ exactly at each time step, eliminating the first two sources of finite-sample bias. This ensures the simulated paths have the correct drift and diffusion properties at every step.

    For the numerical comparison with $\sigma = 0.01$, $\lambda = 0.05$, flat curve at 3%, $T = 5$:

    **Analytical values:**

    $$
    \mu_r(5) = r_0 e^{-\lambda T} + \lambda \int_0^T \theta(s) e^{-\lambda(T-s)}\,ds
    $$

    With a flat curve, $\theta(s) = r + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda s})$ where $r = 0.03$. The analytical conditional mean evaluates to approximately $\mu_r(5) \approx 0.03 + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda \cdot 5}) \times (\text{integrated contribution}) \approx 0.03079$.

    $$
    \sigma_r^2(5) = \frac{(0.01)^2}{2 \times 0.05}(1 - e^{-0.5}) = 0.001 \times 0.39347 = 3.935 \times 10^{-4}
    $$

    With moment matching and 10,000 paths, the sample mean and variance of $r_5$ should match these analytical values to within $O(1/\sqrt{N})$ statistical error, which for $N = 10{,}000$ is of order $10^{-4}$ for the mean.

---

**Exercise 5.** The `compute_theta_T` method adjusts $\theta(t)$ for the $T$-forward measure. Show that the adjustment $\sigma^2 B(T-t)/\lambda$ has the correct sign to produce a lower expected short rate under the $T$-forward measure compared to $\mathbb{Q}$ (when $T > t$). Why does a lower expected rate under the $T$-forward measure make economic sense for bond pricing?

??? success "Solution to Exercise 5"
    The adjustment to the drift under the $T$-forward measure is:

    $$
    \theta^{\mathbb{T}}(t) - \theta(t) = \frac{\sigma^2}{\lambda}B(T - t) = \frac{\sigma^2}{\lambda} \cdot \frac{e^{-\lambda(T-t)} - 1}{\lambda}
    $$

    Since $B(\tau) = (e^{-\lambda\tau} - 1)/\lambda < 0$ for all $\tau > 0$ (because $e^{-\lambda\tau} < 1$), the adjustment $\frac{\sigma^2}{\lambda}B(T - t)$ is negative when $T > t$.

    Therefore $\theta^{\mathbb{T}}(t) < \theta(t)$, which means the drift of the short rate is lower under the $T$-forward measure than under $\mathbb{Q}$. This produces a lower expected short rate under $\mathbb{Q}^T$.

    **Economic interpretation:** Under the $T$-forward measure $\mathbb{Q}^T$, the numeraire is the zero-coupon bond $P(t, T)$. When the short rate is lower, bond prices are higher. The $T$-forward measure "tilts" the distribution toward states where the bond (the numeraire) has high value, i.e., low-rate states. This is the Radon–Nikodym effect: the measure change reweights paths by $P(t, T)/P(0, T)$, giving more probability weight to paths with low rates. This tilt is essential for the forward-measure pricing formula $\mathbb{E}^{\mathbb{Q}^T}[V(T)] = V(0)/P(0, T)$ to hold.

---

**Exercise 6.** Using the `compute_SwapPrice` method, price a 5-year payer swap (annual payments) with fixed rate $K = 3\%$ at $t = 0$ with $r_0 = 3\%$ and a flat market curve at 3\%. Verify that the swap value is approximately zero (since $K$ equals the par rate). Then compute the swap value at $t = 0$ for $K = 4\%$ and interpret the sign.

??? success "Solution to Exercise 6"
    For a 5-year payer swap with annual payments, $K = 3\%$, $t = 0$, $r_0 = 3\%$, flat curve at 3%:

    $$
    V_{\text{swap}} = N\left[P(0, T_0) - P(0, T_5) - K\sum_{k=1}^{5}\delta_k P(0, T_k)\right]
    $$

    With $\delta_k = 1$ (annual), $T_k = k$, and $P(0, k) = e^{-0.03k}$:

    $$
    \sum_{k=1}^{5} P(0, k) = e^{-0.03} + e^{-0.06} + e^{-0.09} + e^{-0.12} + e^{-0.15}
    $$

    $$
    = 0.97045 + 0.94176 + 0.91393 + 0.88692 + 0.86071 = 4.57377
    $$

    The par rate for this swap satisfies $P(0, 0) - P(0, 5) = K_{\text{par}} \sum P(0, T_k)$, giving $K_{\text{par}} = (1 - e^{-0.15})/4.57377 = 0.13929/4.57377 \approx 0.03046$ or about 3.046% (slightly above 3% due to continuous vs. discrete compounding effects).

    Since the par rate is approximately 3.046%, a swap with $K = 3\%$ has a small positive value for the payer (receiving floating, paying fixed at a rate slightly below par): $V \approx N \times (K_{\text{par}} - K) \times \text{annuity} \approx N \times 0.00046 \times 4.574 \approx 0.0021 \times N$.

    For $K = 4\%$, the payer swap has a negative value because the fixed rate paid (4%) exceeds the par rate (3.046%). The payer is locked into paying above-market fixed rates:

    $$
    V_{\text{swap}}(K=4\%) = N\left[(1 - 0.86071) - 0.04 \times 4.57377\right] = N[0.13929 - 0.18295] = -0.04366 \times N
    $$

    The negative sign confirms the payer is at a disadvantage.

---

**Exercise 7.** The `compute_ZCB_Option_Price` method prices European options on zero-coupon bonds. Price a call on $P(2, 5)$ with strike $K = 0.92$, using $\sigma = 0.01$, $\lambda = 0.05$, and a flat curve at 3\%. Then use put-call parity to obtain the put price. Verify by calling the method directly with `CP=OptionType.PUT`.

??? success "Solution to Exercise 7"
    With $\sigma = 0.01$, $\lambda = 0.05$, flat curve at 3%, we price a call on $P(2, 5)$ with strike $K = 0.92$.

    First, compute the bond price volatility:

    $$
    \sigma_P = \frac{\sigma}{\lambda}(1 - e^{-\lambda(T_2 - T_1)})\sqrt{\frac{1 - e^{-2\lambda T_1}}{2\lambda}}
    $$

    $$
    = \frac{0.01}{0.05}(1 - e^{-0.05 \times 3})\sqrt{\frac{1 - e^{-0.1 \times 2}}{0.1}}
    $$

    $$
    = 0.2 \times (1 - e^{-0.15})\sqrt{\frac{1 - e^{-0.2}}{0.1}}
    $$

    $$
    = 0.2 \times 0.13929 \times \sqrt{\frac{0.18127}{0.1}} = 0.02786 \times \sqrt{1.8127} = 0.02786 \times 1.3464 = 0.03751
    $$

    Next, compute the relevant bond prices:

    $$
    P(0, 2) = e^{-0.06} = 0.94176, \qquad P(0, 5) = e^{-0.15} = 0.86071
    $$

    Compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(P(0,5)/(K \cdot P(0,2)))}{\sigma_P} + \frac{\sigma_P}{2} = \frac{\ln(0.86071/(0.92 \times 0.94176))}{0.03751} + \frac{0.03751}{2}
    $$

    $$
    = \frac{\ln(0.86071/0.86642)}{0.03751} + 0.01876 = \frac{\ln(0.99341)}{0.03751} + 0.01876 = \frac{-0.00661}{0.03751} + 0.01876
    $$

    $$
    = -0.17622 + 0.01876 = -0.15746
    $$

    $$
    d_2 = d_1 - \sigma_P = -0.15746 - 0.03751 = -0.19497
    $$

    The call price:

    $$
    C = P(0,5)\,\mathcal{N}(d_1) - K\,P(0,2)\,\mathcal{N}(d_2) = 0.86071 \times \Phi(-0.15746) - 0.92 \times 0.94176 \times \Phi(-0.19497)
    $$

    $$
    = 0.86071 \times 0.43743 - 0.86642 \times 0.42272 = 0.37647 - 0.36622 = 0.01025
    $$

    Using put-call parity:

    $$
    \text{Put} = C - P(0, 5) + K \cdot P(0, 2) = 0.01025 - 0.86071 + 0.92 \times 0.94176 = 0.01025 - 0.86071 + 0.86642 = 0.01596
    $$

    Calling the method with `CP=OptionType.PUT` directly should return the same value of approximately $0.01596$.
