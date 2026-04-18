# Pricing Barrier Options via the Joint Law of (W_t, M_t)

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

Using the joint density $f_{M_T, W_T}(m, w)$ from the reflection principle (see [Reflection Principle](../../ch02/brownian_motion/reflection_principle.md)):

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

- [Barrier Call (Joint Law Pricing)](../../ch07/codes/exotic_barrier_call_joint_law.md)

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

---

## Exercises

**Exercise 1.** The joint density of $(M_T, W_T)$ for standard Brownian motion is $f_{M_T, W_T}(m, w) = \frac{2(2m - w)}{T\sqrt{2\pi T}} \exp\left(-\frac{(2m-w)^2}{2T}\right)$ for $m \geq 0$ and $w \leq m$. Verify that integrating over $m$ from $\max(0, w)$ to $\infty$ recovers the marginal density of $W_T$, which is $\frac{1}{\sqrt{2\pi T}} e^{-w^2/(2T)}$.

??? success "Solution to Exercise 1"
    We need to verify that $\int_{\max(0,w)}^{\infty} f_{M_T, W_T}(m, w)\, dm = \frac{1}{\sqrt{2\pi T}} e^{-w^2/(2T)}$ for all $w$.

    Substituting the joint density:

    $$
    \int_{\max(0,w)}^{\infty} \frac{2(2m - w)}{T\sqrt{2\pi T}} \exp\left(-\frac{(2m-w)^2}{2T}\right) dm
    $$

    Use the substitution $u = 2m - w$, so $du = 2\,dm$ and $dm = du/2$. When $m = \max(0, w)$: if $w \geq 0$, then $u = 2w - w = w$; if $w < 0$, then $u = 0 - w = -w = |w|$. In both cases $u = |w|$. As $m \to \infty$, $u \to \infty$.

    $$
    \int_{|w|}^{\infty} \frac{2u}{T\sqrt{2\pi T}} \exp\left(-\frac{u^2}{2T}\right) \frac{du}{2} = \int_{|w|}^{\infty} \frac{u}{T\sqrt{2\pi T}} \exp\left(-\frac{u^2}{2T}\right) du
    $$

    Now use $\int_a^{\infty} u\, e^{-u^2/(2T)} du = T\, e^{-a^2/(2T)}$:

    $$
    \frac{1}{T\sqrt{2\pi T}} \cdot T \cdot e^{-|w|^2/(2T)} = \frac{1}{\sqrt{2\pi T}} e^{-w^2/(2T)}
    $$

    This is exactly the density of $W_T \sim N(0, T)$, confirming the marginal.

---


**Exercise 2.** For the up-and-out call pricing integral, explain why the integration domain is $\{(w, m) : w_{\min} \leq w \leq b, \; \max(0, w) \leq m \leq b\}$ where $b = \frac{1}{\sigma}\log(H/S_0)$. What determines $w_{\min}$, and why is the constraint $w \leq m$ necessary?

??? success "Solution to Exercise 2"
    The integration domain $\{(w, m) : w_{\min} \leq w \leq b,\; \max(0, w) \leq m \leq b\}$ arises from three constraints:

    **Barrier constraint ($m < b$):** The running maximum $M_T$ must satisfy $M_T < b = \frac{1}{\sigma}\log(H/S_0)$ for the up-and-out option to survive. This restricts the upper limit of the $m$ integration to $b$.

    **In-the-money constraint ($w \geq w_{\min}$):** The call payoff $(S_0 e^{(r-\frac{1}{2}\sigma^2)T + \sigma w} - K)^+$ is positive only when $S_0 e^{(r-\frac{1}{2}\sigma^2)T + \sigma w} > K$, i.e., $w > w_{\min}$ where:

    $$
    w_{\min} = \frac{\log(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma}
    $$

    Below $w_{\min}$, the payoff is zero, so those values of $w$ contribute nothing to the integral.

    **Terminal-maximum consistency ($w \leq m$):** The terminal value of Brownian motion $W_T = w$ cannot exceed the running maximum $M_T = m$ (since $M_T = \sup_{t \leq T} W_t \geq W_T$). This constraint $w \leq m$ means the inner integral over $m$ starts at $\max(0, w)$: we need $m \geq 0$ (since $M_T \geq 0$ for BM starting at 0) and $m \geq w$.

    **Upper bound on $w$:** Since $w \leq m \leq b$, we also need $w \leq b$, which combines with the barrier constraint.

---


**Exercise 3.** The closed-form barrier formula via the image method is $C_{\text{UO}} = C_{\text{BS}}(S_0, K, T) - (S_0/H)^{2\lambda - 2} C_{\text{BS}}(H^2/S_0, K, T)$. Show that this formula can be derived from the joint density integral by completing the integration in closed form. Identify which terms in the joint density integral correspond to $C_{\text{BS}}(S_0, K, T)$ and which correspond to the image correction.

??? success "Solution to Exercise 3"
    The closed-form barrier formula can be derived from the joint density integral by splitting the computation into two parts.

    Starting from:

    $$
    C_{\text{UO}} = e^{-rT} \int \int (S_0 e^{\mu T + \sigma w} - K)^+ f_{M_T, W_T}(m, w)\, \mathbf{1}_{\{m < b\}}\, dm\, dw
    $$

    where $\mu = r - \frac{1}{2}\sigma^2$.

    **First term ($C_{\text{BS}}$):** The unrestricted integral over all $(w, m)$ with $m \geq \max(0, w)$ (no barrier constraint) yields the standard Black-Scholes price $C_{\text{BS}}(S_0, K, T)$, since integrating the payoff against the marginal density of $W_T$ gives the vanilla call price.

    **Image correction term:** The contribution from paths that cross the barrier ($m \geq b$) is:

    $$
    C_{\text{cross}} = e^{-rT} \int \int_{m \geq b} (S_0 e^{\mu T + \sigma w} - K)^+ f_{M_T, W_T}(m, w)\, dm\, dw
    $$

    Using the reflection principle, for each path with $M_T \geq b$ ending at $w$, there corresponds a reflected path starting from $2b$ (in BM space) that ends at $2b - w$. After accounting for the drift via the Girsanov factor $e^{2\mu b/\sigma}$, this integral becomes:

    $$
    C_{\text{cross}} = \left(\frac{S_0}{H}\right)^{2\lambda - 2} C_{\text{BS}}\left(\frac{H^2}{S_0}, K, T\right)
    $$

    The identity $C_{\text{UO}} = C_{\text{BS}} - C_{\text{cross}}$ then gives the closed-form formula.

---


**Exercise 4.** For a down-and-out call with barrier $H < S_0$, the relevant quantity is the running minimum $m_T = \inf_{0 \leq t \leq T} W_t$. Write down the joint density $f_{m_T, W_T}$ analogous to the running maximum density. State the integration domain and the pricing integral for the down-and-out call.

??? success "Solution to Exercise 4"
    For a down-and-out call, the relevant quantity is the running minimum $m_T = \inf_{0 \leq t \leq T} W_t$.

    The joint density of $(m_T, W_T)$ for standard Brownian motion is:

    $$
    f_{m_T, W_T}(m, w) = \frac{2(w - 2m)}{T\sqrt{2\pi T}} \exp\left(-\frac{(w - 2m)^2}{2T}\right), \quad m \leq 0,\; w \geq m
    $$

    This is obtained from the running maximum density by the symmetry of Brownian motion: $-W_t$ has the same law as $W_t$, and $\inf_t W_t = -\sup_t(-W_t)$.

    For a down-and-out call with barrier $H < S_0$, define $b' = \frac{1}{\sigma}\log(H/S_0) < 0$.

    The **integration domain** is:

    $$
    \{(w, m) : w \geq w_{\min},\; b' \leq m \leq \min(0, w),\; m > b'\}
    $$

    The condition $m > b'$ ensures the minimum stays above the barrier (the option survives). The constraint $m \leq w$ ensures the minimum does not exceed the terminal value.

    Actually, for the option to survive, we need $m_T > b'$ (minimum above the barrier level in BM space). The pricing integral is:

    $$
    C_{\text{DO}} = e^{-rT}\int_{w_{\min}}^{\infty}\int_{b'}^{\min(0,w)} (S_0 e^{\mu T + \sigma w} - K)^+ \cdot f_{m_T, W_T}(m, w)\, dm\, dw
    $$

    where $w_{\min} = \frac{\log(K/S_0) - \mu T}{\sigma}$ and $\mu = r - \frac{1}{2}\sigma^2$.

---


**Exercise 5.** Explain why the joint density approach is more general than the image method for barrier option pricing. Give two specific examples of barrier option variants where the image method fails but the joint density approach can still be applied (possibly via numerical integration).

??? success "Solution to Exercise 5"
    The image method (closed-form) requires the barrier structure to be simple enough that the reflection principle produces an exact analytical solution. It works for **single constant barriers** with **standard payoffs** under GBM.

    The **joint density approach** is more general because it works with any function of $(W_T, M_T)$ or $(W_T, m_T)$, even when the resulting integral cannot be evaluated in closed form. It can be computed numerically via quadrature.

    **Two examples where the image method fails but the joint density approach works:**

    1. **Double barrier options** (both upper and lower barriers: $H_L < S_0 < H_U$). The option is knocked out if the price hits either barrier. The image method requires an infinite series of reflections (images of images), which does not simplify to a finite closed form. The joint density approach can handle this by restricting the integration domain to $\{(w, m, m') : m < b_U,\, m' > b_L\}$ and integrating numerically, although the joint density of $(W_T, M_T, m_T)$ is needed.

    2. **Barrier options with rebates that depend on the hitting time.** For example, a knock-out option that pays $R \cdot g(\tau_H)$ (where $g$ is a nonlinear function of the hitting time) when the barrier is hit. The image method gives only the standard exponential-discount rebate. The joint density approach, combined with the distribution of the hitting time, can handle arbitrary rebate functions via numerical integration.

---


**Exercise 6.** In Monte Carlo simulation of barrier options, paths are observed at discrete times, which can miss barrier crossings. Describe the Brownian bridge adjustment: given $S_{t_k}$ and $S_{t_{k+1}}$ at consecutive observation times, write the conditional probability that the path crosses barrier $H$ between $t_k$ and $t_{k+1}$, and explain how this is used to correct the Monte Carlo estimate.

??? success "Solution to Exercise 6"
    The **Brownian bridge adjustment** accounts for barrier crossings between discrete observation times.

    Given simulated values $S_{t_k}$ and $S_{t_{k+1}}$ at consecutive times (both on the same side of the barrier $H$), the continuous path between them may still cross $H$. The conditional distribution of the path between $t_k$ and $t_{k+1}$, given the endpoints, is a **Brownian bridge**.

    For a down barrier $H$, with $S_{t_k} > H$ and $S_{t_{k+1}} > H$, the probability that the continuous path crosses $H$ between $t_k$ and $t_{k+1}$ is:

    $$
    p = \exp\left(-\frac{2\log(S_{t_k}/H)\cdot\log(S_{t_{k+1}}/H)}{\sigma^2 \Delta t}\right)
    $$

    where $\Delta t = t_{k+1} - t_k$. This formula comes from the probability that a Brownian bridge between two points (both above zero) hits zero.

    **How to use this in Monte Carlo:** For each simulated path and each time interval $[t_k, t_{k+1}]$:

    1. Compute the crossing probability $p$ using the formula above.
    2. Generate a uniform random variable $U \sim \text{Uniform}(0,1)$.
    3. If $U < p$, declare the barrier as crossed (knock out the option for that path).

    Alternatively, for a knock-out option, multiply the path's payoff by the **survival probability** $\prod_{k=0}^{M-1}(1 - p_k)$, where $p_k$ is the crossing probability for the $k$-th interval. This provides an unbiased correction that eliminates the systematic overestimation of knock-out prices caused by discrete monitoring.
