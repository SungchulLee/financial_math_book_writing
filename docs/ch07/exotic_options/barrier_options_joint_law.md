# Pricing Barrier Options via the Joint Law of $(W_t, M_t)$

## Barrier Option Overview

A **barrier option** is a path-dependent option whose payoff depends on whether the underlying asset hits a certain barrier level during its life. Unlike vanilla options that depend only on the terminal price $S_T$, barrier options require tracking the entire path of the underlying.

We work in the **standard Black–Scholes model** under the risk-neutral measure $\mathbb{Q}$:

$$
dS_t = r S_t\,dt + \sigma S_t\,dW_t
$$

with solution:

$$
S_t = S_0 \exp\!\left( \left(r - \tfrac{1}{2}\sigma^2 \right)t + \sigma W_t \right)
$$

Define the **log-price process**:

$$
X_t := \log S_t = \log S_0 + \left(r - \tfrac{1}{2}\sigma^2 \right)t + \sigma W_t
$$

Let $H$ denote the constant **barrier level** and $K$ the strike price.

---

## Common Barrier Option Types

| Type | Condition | Payoff |
|------|-----------|--------|
| **Up-and-Out** | Knocked out if $\max_{0 \le t \le T} S_t \ge H$ | $(S_T - K)^+ \cdot \mathbf{1}_{\{\max S_t < H\}}$ |
| **Up-and-In** | Activated if $\max_{0 \le t \le T} S_t \ge H$ | $(S_T - K)^+ \cdot \mathbf{1}_{\{\max S_t \ge H\}}$ |
| **Down-and-Out** | Knocked out if $\min_{0 \le t \le T} S_t \le H$ | $(S_T - K)^+ \cdot \mathbf{1}_{\{\min S_t > H\}}$ |
| **Down-and-In** | Activated if $\min_{0 \le t \le T} S_t \le H$ | $(S_T - K)^+ \cdot \mathbf{1}_{\{\min S_t \le H\}}$ |

**In–Out Parity.** For any barrier type, the in-version and out-version satisfy:

$$
C_{\text{In}} + C_{\text{Out}} = C_{\text{Vanilla}}
$$

This follows because the events $\{\text{barrier hit}\}$ and $\{\text{barrier not hit}\}$ partition the sample space.

---

## Up-and-Out Call via Joint Law

### Setup

An **up-and-out call option** knocks out (becomes worthless) if $S_t$ ever reaches or exceeds $H > S_0$ before expiry $T$. Its payoff is:

$$
\text{Payoff} = (S_T - K)^+ \cdot \mathbf{1}_{\left\{ \sup_{0 \le t \le T} S_t < H \right\}}
$$

### Reduction to Brownian Motion

Define the **running maximum** of Brownian motion:

$$
M_T := \sup_{0 \le t \le T} W_t
$$

The supremum of the stock price is:

$$
\sup_{0 \le t \le T} S_t = S_0 \exp\!\left( \sup_{0 \le t \le T} \left[ \left(r - \tfrac{1}{2}\sigma^2\right)t + \sigma W_t \right] \right)
$$

For a standard Brownian motion (without drift), the condition $\sup_{0 \le t \le T} S_t < H$ is equivalent to $M_T < b$, where:

$$
b := \frac{1}{\sigma} \log\!\left( \frac{H}{S_0} \right)
$$

!!! note "Drift Adjustment"
    When $r - \frac{1}{2}\sigma^2 \neq 0$, the supremum of $X_t$ does not reduce exactly to $\sigma M_T$. One approach is to use **Girsanov's theorem** to remove the drift, then apply the joint density under the new measure with a Radon–Nikodym correction. Alternatively, one can use the **joint density of drifted Brownian motion** directly, which involves the reflection principle for drifted processes.

### Pricing via the Joint Density

Using the joint density $f_{M_T, W_T}(m, w)$ from the reflection principle (see [Reflection Principle](../../ch01/brownian_motion/reflection_principle.md)):

$$
f_{M_T, W_T}(m, w) = \frac{2(2m - w)}{T\sqrt{2\pi T}} \exp\!\left( -\frac{(2m - w)^2}{2T} \right), \quad m \ge 0,\; w \le m
$$

The discounted price of the up-and-out call is:

$$
C_{\text{UO}} = e^{-rT} \int_{-\infty}^{\infty} \int_{0}^{b} \left( S_0\, e^{(r - \frac{1}{2}\sigma^2)T + \sigma w} - K \right)^{\!+} f_{M_T, W_T}(m, w)\, dm\, dw
$$

Substituting the joint density:

$$
C_{\text{UO}} = e^{-rT} \int_{-\infty}^{b} \int_{\max(0,w)}^{b}
\left( S_0\, e^{(r - \frac{1}{2}\sigma^2)T + \sigma w} - K \right)^{\!+}
\cdot \frac{2(2m - w)}{T\sqrt{2\pi T}}\, e^{-\frac{(2m-w)^2}{2T}}\, dm\, dw
$$

!!! info "Integration Domain"
    The constraint $w \le m$ (since the terminal value cannot exceed the running maximum) restricts the inner integral to $m \ge \max(0, w)$. The barrier condition restricts $m < b$.

---

## Closed-Form via Reflection Principle

For a **vanilla up-and-out call** with barrier $H > \max(S_0, K)$, a closed-form solution exists using the **image method** (also called the method of images), which is closely related to the reflection principle.

### Formula

$$
C_{\text{UO}}(S_0, K, H, T) = C_{\text{BS}}(S_0, K, T) - \left( \frac{S_0}{H} \right)^{2\lambda - 2} C_{\text{BS}}\!\left( \frac{H^2}{S_0}, K, T \right)
$$

where:

- $C_{\text{BS}}(S, K, T)$ is the standard Black–Scholes European call price,
- $\lambda = \dfrac{r}{\sigma^2} + \dfrac{1}{2}$.

### Derivation Sketch

The idea proceeds in three steps:

1. **Standard BS price** $C_{\text{BS}}$ prices all paths, including those that cross the barrier.

2. **Image charge trick.** For each path that crosses the barrier $H$, the reflection principle associates a "mirror" path starting from $H^2 / S_0$. The probability weight of these reflected paths is captured by the second term.

3. **The exponent** $2\lambda - 2$ arises from the Radon–Nikodym derivative that accounts for the drift when reflecting drifted Brownian motion.

### Other Barrier Types

Using **in–out parity**, the up-and-in call price is:

$$
C_{\text{UI}} = C_{\text{BS}} - C_{\text{UO}} = \left( \frac{S_0}{H} \right)^{2\lambda - 2} C_{\text{BS}}\!\left( \frac{H^2}{S_0}, K, T \right)
$$

For **down-and-out** and **down-and-in** options (barrier $H < S_0$), analogous formulas exist with the running minimum replacing the maximum, and the joint density $f_{m_T, W_T}$ of $\left(\inf_{0 \le t \le T} W_t,\, W_T\right)$.

---

## Numerical Approximation via Joint Density

The joint density approach is powerful because it extends to settings where closed-form solutions are unavailable.

### When to Use Numerical Methods

- **Rebate options**: A fixed payment is made when the barrier is hit.
- **Double barriers**: Both upper and lower barriers are present simultaneously.
- **General payoffs**: Functions of both $S_T$ and $\sup_{0 \le t \le T} S_t$ or $\inf_{0 \le t \le T} S_t$.
- **Time-dependent barriers**: The barrier level changes over time.

### Implementation Strategy

1. **Discretize** the $(w, m)$ domain into a 2D grid.
2. **Evaluate** the integrand: payoff $\times$ joint density at each grid point.
3. **Integrate** using numerical quadrature (e.g., trapezoidal rule or Simpson's rule) or Monte Carlo sampling.

For the up-and-out call, the effective integration domain is:

$$
\{(w, m) : w_{\min} \le w \le b,\;\; \max(0, w) \le m \le b\}
$$

where $w_{\min}$ is chosen so that the payoff is negligible below it (typically $w_{\min} = \frac{1}{\sigma}\log(K/S_0) - (r - \frac{1}{2}\sigma^2)T/\sigma$).

---

## Python Implementation

A complete implementation is available in the appendix:

- [Barrier Call (Joint Law Pricing)](../../python_codes/exotic_options_BARRIER_CALL_JOINT_LAW.py)

The implementation includes:

1. **Closed-form pricing** via the image method formula.
2. **Numerical integration** using the joint density $f_{M_T, W_T}$.
3. **Monte Carlo simulation** with path-level barrier monitoring.
4. **Comparison** of all three methods with convergence analysis.

---

## Summary

| Method | Strengths | Limitations |
|--------|-----------|-------------|
| **Closed-form (Image Method)** | Exact, fast, no discretization error | Limited to simple barrier types |
| **Joint Density Integration** | Handles general payoffs of $(S_T, \max S_t)$ | Requires 2D numerical quadrature |
| **Monte Carlo** | Flexible, handles any path-dependent payoff | Slow convergence, barrier-crossing bias |

The **reflection principle** provides the mathematical foundation for all three approaches:

- It yields the **joint density** $f_{M_T, W_T}$ used in numerical integration.
- It motivates the **image method** that produces closed-form solutions.
- It informs **bias corrections** in Monte Carlo methods (e.g., Brownian bridge adjustments for discrete monitoring).
