# Ito Formula for Jump Processes

The classical Ito formula transforms a twice-differentiable function of a continuous semimartingale into a new semimartingale, producing the famous $\tfrac{1}{2}\sigma^2 f''$ correction term that distinguishes stochastic calculus from ordinary calculus. When the underlying process has jumps, however, each discontinuity contributes a finite increment $f(X_t) - f(X_{t^-})$ that must be tracked separately. This section develops the **Ito formula for jump-diffusion processes** and applies it to derive the log-price dynamics in the Merton model.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the Ito formula for a process driven by Brownian motion and a compound Poisson process
    2. Identify the three distinct components: drift, diffusion, and jump
    3. Apply the formula to derive $d(\ln S_t)$ in the Merton jump-diffusion model
    4. Explain the role of the compensated Poisson process in the martingale decomposition

---

## Motivation

### From Continuous to Discontinuous Paths

Recall the standard Ito formula for a $C^2$ function $f$ applied to a continuous Ito process $X_t$:

$$
df(X_t) = f'(X_t)\,dX_t + \frac{1}{2}f''(X_t)\,(dX_t)^2
$$

This formula accounts for the non-vanishing quadratic variation of Brownian motion. But if $X_t$ can jump, the Taylor expansion reasoning behind this formula breaks down at each discontinuity. At a jump time $T_i$, the value of $f$ changes from $f(X_{T_i^-})$ to $f(X_{T_i})$ instantaneously, and this finite change is not captured by the continuous-path Ito correction.

The solution is to add a **jump correction term** that explicitly sums the discrete changes in $f$ at each jump, while subtracting the linearized contribution $f'(X_{t^-})\Delta X_t$ that is already counted by the differential term.

---

## Stochastic Integration with Respect to the Poisson Process

### The Poisson Integral

For a predictable (left-continuous) process $H_t$, the stochastic integral with respect to the Poisson process $N_t$ is defined path-by-path as a Lebesgue-Stieltjes integral:

$$
\int_0^t H_s\,dN_s = \sum_{i=1}^{N_t} H_{T_i}
$$

where $T_1, T_2, \ldots$ are the jump times of $N$. This is a finite sum (almost surely) on any bounded interval, so no limiting procedure is needed.

### The Compensated Poisson Integral

The compensated Poisson process $\tilde{N}_t = N_t - \lambda t$ is a martingale, and the integral

$$
\int_0^t H_s\,d\tilde{N}_s = \int_0^t H_s\,dN_s - \lambda\int_0^t H_s\,ds = \sum_{i=1}^{N_t} H_{T_i} - \lambda\int_0^t H_s\,ds
$$

is also a martingale (provided $H$ satisfies appropriate integrability conditions). The compensated integral plays the same role for jump processes that the Ito integral plays for diffusions: it is a centered, mean-zero building block.

!!! info "Proposition: Isometry of the Compensated Poisson Integral"
    If $\mathbb{E}\!\left[\int_0^t H_s^2\,ds\right] < \infty$, then

    $$
    \mathbb{E}\!\left[\left(\int_0^t H_s\,d\tilde{N}_s\right)^2\right] = \lambda\int_0^t \mathbb{E}[H_s^2]\,ds
    $$

**Proof.** Write $M_t = \int_0^t H_s\,d\tilde{N}_s$. Since $M$ is a martingale, $\mathbb{E}[M_t^2] = \mathbb{E}[\langle M \rangle_t]$, where the predictable quadratic variation is $\langle M \rangle_t = \lambda \int_0^t H_s^2\,ds$. This follows from the fact that $\tilde{N}$ has predictable quadratic variation $\langle \tilde{N} \rangle_t = \lambda t$. $\square$

---

## The Ito Formula for Jump-Diffusion Processes

### Setup

Consider a process $X_t$ satisfying the general jump-diffusion SDE:

$$
dX_t = \mu(t, X_{t^-})\,dt + \sigma(t, X_{t^-})\,dW_t + \gamma(t, X_{t^-})\,dJ_t
$$

where $W_t$ is a standard Brownian motion and $J_t = \sum_{i=1}^{N_t} Z_i$ is a compound Poisson process with intensity $\lambda$ and jump sizes $\{Z_i\}$. Between jump times, $X_t$ evolves as a continuous Ito process; at each jump time $T_i$, it receives an additive increment $\gamma(T_i, X_{T_i^-}) Z_i$.

### The Formula

!!! info "Theorem: Ito Formula for Jump-Diffusion Processes"
    Let $f \in C^{1,2}([0,\infty) \times \mathbb{R})$. Then

    $$
    f(t, X_t) = f(0, X_0) + \int_0^t \frac{\partial f}{\partial s}(s, X_{s^-})\,ds + \int_0^t \frac{\partial f}{\partial x}(s, X_{s^-})\,dX_s^c + \frac{1}{2}\int_0^t \frac{\partial^2 f}{\partial x^2}(s, X_{s^-})\,\sigma^2(s, X_{s^-})\,ds + \sum_{0 < s \leq t}\left[f(s, X_s) - f(s, X_{s^-})\right]
    $$

    where $X_t^c$ denotes the continuous part of $X_t$ (the drift plus diffusion, excluding jumps).

Equivalently, in differential notation:

$$
df(t, X_t) = \left(\frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}\right)dt + \sigma\frac{\partial f}{\partial x}\,dW_t + \left[f(t, X_t) - f(t, X_{t^-})\right]dN_t
$$

where the arguments of $\mu$, $\sigma$, and the partial derivatives are evaluated at $(t, X_{t^-})$, and the jump term is understood to be nonzero only at the (countably many) jump times.

### Structure of the Three Terms

The formula has three distinct components:

1. **Continuous Ito part**: The first three terms inside the parentheses are exactly the standard Ito formula applied to the continuous part of $X$. This includes the $\tfrac{1}{2}\sigma^2 f''$ correction.

2. **Diffusion martingale**: The $\sigma f'\,dW_t$ term is a continuous martingale.

3. **Jump term**: At each jump time $T_i$, the process $f(t, X_t)$ changes by $f(T_i, X_{T_i}) - f(T_i, X_{T_i^-})$. This is a finite difference, not an infinitesimal correction. Unlike the continuous Ito correction which involves $f''$, the jump correction involves the exact nonlinear change in $f$.

!!! warning "No Second-Order Jump Correction"
    In the continuous Ito formula, the $\tfrac{1}{2}f''$ term arises because $(dW_t)^2 = dt$ in the limit. For jumps, no such second-order correction is needed because the jumps are finite and occur one at a time. The full nonlinear change $f(X_s) - f(X_{s^-})$ is tracked exactly.

---

## Proof Sketch

The proof proceeds by separating the time interval $[0, t]$ at the jump times $T_1, T_2, \ldots, T_{N_t}$.

**Between jumps.** On each interval $(T_{i-1}, T_i)$ (with $T_0 = 0$), the process $X$ is continuous and the standard Ito formula applies:

$$
f(T_i^-, X_{T_i^-}) - f(T_{i-1}, X_{T_{i-1}}) = \int_{T_{i-1}}^{T_i} \left(\frac{\partial f}{\partial s} + \mu\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 f}{\partial x^2}\right)ds + \int_{T_{i-1}}^{T_i} \sigma\frac{\partial f}{\partial x}\,dW_s
$$

**At jumps.** At time $T_i$, the contribution is:

$$
f(T_i, X_{T_i}) - f(T_i, X_{T_i^-})
$$

**Summing.** Telescoping over all intervals and adding the jump contributions:

$$
f(t, X_t) - f(0, X_0) = \sum_{i} \bigl[f(T_i^-, X_{T_i^-}) - f(T_{i-1}, X_{T_{i-1}})\bigr] + \sum_i \bigl[f(T_i, X_{T_i}) - f(T_i, X_{T_i^-})\bigr] + \text{(final interval)}
$$

Combining the continuous integrals across all sub-intervals and collecting the jump terms yields the stated formula. $\square$

---

## Application: Log-Price in the Merton Model

### Setup

The Merton jump-diffusion SDE under $\mathbb{Q}$ is:

$$
\frac{dS_t}{S_{t^-}} = (r - \lambda\bar{k})\,dt + \sigma\,dW_t + (Y - 1)\,dN_t
$$

where $Y$ is the jump multiplier at a jump time. We apply the Ito formula for jump processes with $f(S) = \ln S$.

### Continuous Part

Between jumps, $S_t$ follows geometric Brownian motion with drift $r - \lambda\bar{k}$. The standard Ito formula gives:

$$
d(\ln S_t)^{\text{cont}} = \frac{1}{S_t}\,dS_t^c - \frac{1}{2}\frac{1}{S_t^2}(dS_t^c)^2
$$

where $dS_t^c = S_{t^-}(r - \lambda\bar{k})\,dt + S_{t^-}\sigma\,dW_t$ is the continuous part. Therefore:

$$
d(\ln S_t)^{\text{cont}} = \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)dt + \sigma\,dW_t
$$

### Jump Part

At each jump time $T_i$, the price jumps from $S_{T_i^-}$ to $S_{T_i} = S_{T_i^-} \cdot Y_i$, so:

$$
\ln S_{T_i} - \ln S_{T_i^-} = \ln Y_i
$$

### Combined Formula

Assembling both parts:

$$
\ln S_t = \ln S_0 + \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)t + \sigma W_t + \sum_{i=1}^{N_t} \ln Y_i
$$

!!! info "Proposition: Log-Price Decomposition"
    The log-price in the Merton model decomposes as

    $$
    \ln S_t = \ln S_0 + \underbrace{\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)t}_{\text{deterministic drift}} + \underbrace{\sigma W_t}_{\text{diffusion}} + \underbrace{\sum_{i=1}^{N_t} \ln Y_i}_{\text{jumps}}
    $$

    Exponentiating yields the explicit solution:

    $$
    S_t = S_0 \exp\!\left[\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right]\prod_{i=1}^{N_t} Y_i
    $$

This factorization is the foundation of the Merton series formula: conditioning on $N_t = n$, the log-return is normally distributed, and the option price becomes a Poisson-weighted sum of Black-Scholes prices.

---

## The Compensated Jump Decomposition

For certain calculations (especially martingale arguments), it is useful to rewrite the jump term using the compensated Poisson process.

!!! info "Proposition: Martingale Decomposition"
    The log-price can be written as

    $$
    \ln S_t = \ln S_0 + \left(r - \frac{1}{2}\sigma^2 - \lambda\bar{k} + \lambda\mu_J\right)t + \sigma W_t + \sum_{i=1}^{N_t}\ln Y_i - \lambda\mu_J t
    $$

    where the last two terms form a compensated compound Poisson martingale $\sum_{i=1}^{N_t}\ln Y_i - \lambda\mu_J t$ (since $\mathbb{E}[\ln Y_i] = \mu_J$).

**Proof.** Add and subtract $\lambda\mu_J t$:

$$
\sum_{i=1}^{N_t}\ln Y_i = \left(\sum_{i=1}^{N_t}\ln Y_i - \lambda\mu_J t\right) + \lambda\mu_J t
$$

The term in parentheses has mean zero (it is the compensated compound Poisson process for $\ln Y_i$), and $\lambda\mu_J t$ is absorbed into the drift. $\square$

---

## Worked Example

!!! example "Applying the Ito Formula to a Power Function"
    Consider $f(S) = S^2$ applied to the Merton jump-diffusion. We compute $d(S_t^2)$.

    **Continuous part.** With $f'(S) = 2S$ and $f''(S) = 2$:

    $$
    d(S_t^2)^{\text{cont}} = 2S_{t^-}\,dS_t^c + \frac{1}{2}\cdot 2 \cdot (dS_t^c)^2
    $$

    $$
    = 2S_{t^-}^2\bigl[(r - \lambda\bar{k})\,dt + \sigma\,dW_t\bigr] + S_{t^-}^2\sigma^2\,dt
    $$

    $$
    = S_{t^-}^2\bigl[2(r - \lambda\bar{k}) + \sigma^2\bigr]\,dt + 2S_{t^-}^2\sigma\,dW_t
    $$

    **Jump part.** At each jump time $T_i$:

    $$
    S_{T_i}^2 - S_{T_i^-}^2 = S_{T_i^-}^2(Y_i^2 - 1)
    $$

    **Combined:**

    $$
    d(S_t^2) = S_{t^-}^2\bigl[2(r - \lambda\bar{k}) + \sigma^2\bigr]\,dt + 2S_{t^-}^2\sigma\,dW_t + S_{t^-}^2(Y^2 - 1)\,dN_t
    $$

    This illustrates the general pattern: the jump correction involves $f(SY) - f(S)$ rather than $f'(S)\cdot S(Y-1)$, capturing the nonlinear effect of jumps.

---

## Summary

The Ito formula for jump-diffusion processes extends the classical Ito formula by adding an exact finite-difference term at each jump time. The continuous part contributes the standard $\tfrac{1}{2}\sigma^2 f''$ correction, while the jump part contributes $\sum[f(X_s) - f(X_{s^-})]$ without any second-order approximation. Applied to $f(S) = \ln S$ in the Merton model, the formula yields the log-price decomposition into drift, diffusion, and compound Poisson components, which is the starting point for the characteristic function, the Merton series formula, and the PIDE formulation developed in subsequent sections.

---

## Exercises

**Exercise 1.** Apply the Ito formula for jump processes to $f(S) = \ln S$ in the Merton model to derive $d(\ln S_t) = (r - \lambda\bar{k} - \frac{1}{2}\sigma^2)\,dt + \sigma\,dW_t + \ln Y\,dN_t$. Carefully separate the continuous and jump parts, and explain why there is no second-order jump correction (unlike the $\frac{1}{2}\sigma^2$ term from the diffusion).

??? success "Solution to Exercise 1"
    We apply the Ito formula for jump processes to $f(S) = \ln S$ with $f'(S) = 1/S$ and $f''(S) = -1/S^2$.

    **Continuous part.** Between jumps, $S_t$ satisfies $dS_t^c = S_{t^-}(r - \lambda\bar{k})\,dt + S_{t^-}\sigma\,dW_t$. The standard Ito formula gives:

    $$
    d(\ln S_t)^{\text{cont}} = \frac{1}{S_{t^-}}\,dS_t^c + \frac{1}{2}\left(-\frac{1}{S_{t^-}^2}\right)(dS_t^c)^2
    $$

    Since $(dS_t^c)^2 = S_{t^-}^2\sigma^2\,dt$, we obtain:

    $$
    d(\ln S_t)^{\text{cont}} = (r - \lambda\bar{k})\,dt + \sigma\,dW_t - \frac{1}{2}\sigma^2\,dt = \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)dt + \sigma\,dW_t
    $$

    **Jump part.** At each jump time $T_i$, the price jumps from $S_{T_i^-}$ to $S_{T_i} = S_{T_i^-} \cdot Y_i$. The jump contribution to $\ln S$ is:

    $$
    \ln S_{T_i} - \ln S_{T_i^-} = \ln(S_{T_i^-} Y_i) - \ln S_{T_i^-} = \ln Y_i
    $$

    **Combined.** Assembling both parts:

    $$
    d(\ln S_t) = \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)dt + \sigma\,dW_t + \ln Y\,dN_t
    $$

    **Why no second-order jump correction.** The continuous Ito correction $\frac{1}{2}\sigma^2$ arises because Brownian motion has nonzero quadratic variation: infinitely many infinitesimal increments accumulate to produce a finite second-order effect via $(dW_t)^2 = dt$. For jumps, each discontinuity is a finite, isolated event (jumps occur one at a time with probability one). The full nonlinear change $f(X_s) - f(X_{s^-})$ is computed exactly as a finite difference, so no Taylor approximation is needed and no second-order correction term appears.

---


**Exercise 2.** Apply the Ito formula for jump processes to $f(S) = S^2$. (a) Compute the continuous part $d(S_t^2)^{\text{cont}}$ using $f'(S) = 2S$ and $f''(S) = 2$. (b) Compute the jump part $S_{T_i}^2 - S_{T_i^-}^2 = S_{T_i^-}^2(Y_i^2 - 1)$. (c) Combine both parts and write the full SDE for $S_t^2$.

??? success "Solution to Exercise 2"
    We apply the Ito formula to $f(S) = S^2$ with $f'(S) = 2S$ and $f''(S) = 2$.

    **(a) Continuous part.** The continuous part of the SDE is $dS_t^c = S_{t^-}(r - \lambda\bar{k})\,dt + S_{t^-}\sigma\,dW_t$, so $(dS_t^c)^2 = S_{t^-}^2\sigma^2\,dt$. Then:

    $$
    d(S_t^2)^{\text{cont}} = 2S_{t^-}\,dS_t^c + \frac{1}{2}(2)(dS_t^c)^2
    $$

    $$
    = 2S_{t^-} \cdot S_{t^-}\bigl[(r - \lambda\bar{k})\,dt + \sigma\,dW_t\bigr] + S_{t^-}^2\sigma^2\,dt
    $$

    $$
    = S_{t^-}^2\bigl[2(r - \lambda\bar{k}) + \sigma^2\bigr]\,dt + 2S_{t^-}^2\sigma\,dW_t
    $$

    **(b) Jump part.** At jump time $T_i$, $S_{T_i} = S_{T_i^-} Y_i$, so:

    $$
    S_{T_i}^2 - S_{T_i^-}^2 = (S_{T_i^-} Y_i)^2 - S_{T_i^-}^2 = S_{T_i^-}^2(Y_i^2 - 1)
    $$

    **(c) Combined SDE.** Adding the continuous and jump parts:

    $$
    d(S_t^2) = S_{t^-}^2\bigl[2(r - \lambda\bar{k}) + \sigma^2\bigr]\,dt + 2S_{t^-}^2\sigma\,dW_t + S_{t^-}^2(Y^2 - 1)\,dN_t
    $$

    Note: the jump correction involves $f(SY) - f(S) = S^2(Y^2 - 1)$, which differs from $f'(S) \cdot S(Y - 1) = 2S^2(Y - 1)$. The difference $S^2(Y^2 - 1) - 2S^2(Y - 1) = S^2(Y - 1)^2$ captures the nonlinear effect of jumps on the squared price.

---


**Exercise 3.** Explain the key structural difference between the continuous Ito correction ($\frac{1}{2}\sigma^2 f''$) and the jump correction ($f(X_s) - f(X_{s^-})$). Why does the continuous part require a Taylor approximation to second order while the jump part uses the exact finite difference?

??? success "Solution to Exercise 3"
    **Continuous Ito correction.** In the standard Ito formula, the correction $\frac{1}{2}\sigma^2 f''(X_t)\,dt$ arises from the quadratic variation of Brownian motion. Over an infinitesimal interval $dt$, the increment $dW_t$ is of order $\sqrt{dt}$, so $(dW_t)^2 = dt$ in the mean-square limit. Since $X_t$ accumulates infinitely many such infinitesimal increments on any bounded interval, the second-order Taylor term does not vanish and must be retained. This is a genuinely stochastic phenomenon with no counterpart in ordinary calculus.

    **Jump correction.** At each jump time, the process makes a single finite jump $\Delta X_s = X_s - X_{s^-}$. The change in $f$ is:

    $$
    f(X_s) - f(X_{s^-})
    $$

    This is an exact finite difference that can be computed directly without any Taylor expansion. Since jumps arrive one at a time (the probability of simultaneous jumps is zero for a Poisson process), each individual jump contribution is a well-defined finite quantity. There is no accumulation of infinitesimal jump increments, and hence no need for a limiting argument or a second-order correction.

    **Structural difference.** The continuous correction is an aggregate effect of infinitely many infinitesimal random increments whose second-order contributions sum to a finite quantity. The jump correction is a pointwise exact evaluation at finitely many (random) times. This distinction is the fundamental reason why the continuous Ito formula requires $f \in C^2$ while the jump correction only requires $f$ to be measurable.

---


**Exercise 4.** Using the compensated jump decomposition, write $\ln S_t = \ln S_0 + (r - \frac{1}{2}\sigma^2 - \lambda\bar{k} + \lambda\mu_J)t + \sigma W_t + (\sum_{i=1}^{N_t}\ln Y_i - \lambda\mu_J t)$. Verify that the last two terms form a martingale by showing that their expectation is zero. Why is this decomposition useful for pricing and risk management?

??? success "Solution to Exercise 4"
    Starting from the log-price formula:

    $$
    \ln S_t = \ln S_0 + \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)t + \sigma W_t + \sum_{i=1}^{N_t}\ln Y_i
    $$

    we add and subtract $\lambda\mu_J t$ (where $\mu_J = \mathbb{E}[\ln Y_i]$):

    $$
    \ln S_t = \ln S_0 + \left(r - \frac{1}{2}\sigma^2 - \lambda\bar{k} + \lambda\mu_J\right)t + \sigma W_t + \left(\sum_{i=1}^{N_t}\ln Y_i - \lambda\mu_J t\right)
    $$

    **Verifying the martingale property.** Define $M_t = \sum_{i=1}^{N_t}\ln Y_i - \lambda\mu_J t$. We compute its expectation:

    $$
    \mathbb{E}[M_t] = \mathbb{E}\!\left[\sum_{i=1}^{N_t}\ln Y_i\right] - \lambda\mu_J t
    $$

    By the tower property, $\mathbb{E}\!\left[\sum_{i=1}^{N_t}\ln Y_i\right] = \mathbb{E}[N_t]\cdot\mathbb{E}[\ln Y_i] = \lambda t \cdot \mu_J$. Therefore:

    $$
    \mathbb{E}[M_t] = \lambda t \mu_J - \lambda\mu_J t = 0
    $$

    More generally, for $s < t$, the conditional expectation $\mathbb{E}[M_t - M_s \mid \mathcal{F}_s] = 0$ follows from the independent and stationary increments of the compound Poisson process and the Poisson process. Hence $M_t$ is a martingale.

    **Why this is useful.** The decomposition separates $\ln S_t$ into a deterministic drift and two independent martingale components ($\sigma W_t$ and $M_t$). This is essential for:

    - **Pricing**: martingale components vanish under expectation, simplifying risk-neutral valuation
    - **Hedging**: the two independent sources of randomness (diffusion and jump) require separate hedging strategies
    - **Risk management**: the variance of log-returns decomposes cleanly into diffusion and jump contributions

---


**Exercise 5.** The proof of the Ito formula for jump processes works by splitting $[0, t]$ at jump times and applying the standard Ito formula on each continuous segment. Carry out this argument explicitly for a single jump time $T_1$: write $f(t, X_t) - f(0, X_0) = [f(T_1^-, X_{T_1^-}) - f(0, X_0)] + [f(T_1, X_{T_1}) - f(T_1, X_{T_1^-})] + [f(t, X_t) - f(T_1, X_{T_1})]$ and identify the continuous Ito terms and the jump term.

??? success "Solution to Exercise 5"
    Assume there is exactly one jump at time $T_1 \in (0, t)$. We write:

    $$
    f(t, X_t) - f(0, X_0) = \underbrace{[f(T_1^-, X_{T_1^-}) - f(0, X_0)]}_{\text{(I)}} + \underbrace{[f(T_1, X_{T_1}) - f(T_1, X_{T_1^-})]}_{\text{(II)}} + \underbrace{[f(t, X_t) - f(T_1, X_{T_1})]}_{\text{(III)}}
    $$

    **Term (I): Continuous Ito formula on $[0, T_1)$.** On this interval, $X$ has no jumps and evolves as a continuous Ito process. By the standard Ito formula:

    $$
    f(T_1^-, X_{T_1^-}) - f(0, X_0) = \int_0^{T_1}\left(\frac{\partial f}{\partial s} + \mu\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 f}{\partial x^2}\right)ds + \int_0^{T_1}\sigma\frac{\partial f}{\partial x}\,dW_s
    $$

    This contains the drift, the $\frac{1}{2}\sigma^2 f''$ correction, and the diffusion martingale term.

    **Term (II): Jump contribution.** At time $T_1$, the process jumps from $X_{T_1^-}$ to $X_{T_1} = X_{T_1^-} + \gamma(T_1, X_{T_1^-})Z_1$. The contribution is the exact finite difference:

    $$
    f(T_1, X_{T_1}) - f(T_1, X_{T_1^-})
    $$

    This is the jump term. No Taylor approximation is used; the full nonlinear change in $f$ is recorded.

    **Term (III): Continuous Ito formula on $(T_1, t]$.** After the jump, $X$ again evolves continuously. By the standard Ito formula:

    $$
    f(t, X_t) - f(T_1, X_{T_1}) = \int_{T_1}^{t}\left(\frac{\partial f}{\partial s} + \mu\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 f}{\partial x^2}\right)ds + \int_{T_1}^{t}\sigma\frac{\partial f}{\partial x}\,dW_s
    $$

    **Combining all three terms.** Adding (I), (II), and (III):

    $$
    f(t, X_t) - f(0, X_0) = \int_0^{t}\left(\frac{\partial f}{\partial s} + \mu\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 f}{\partial x^2}\right)ds + \int_0^{t}\sigma\frac{\partial f}{\partial x}\,dW_s + [f(T_1, X_{T_1}) - f(T_1, X_{T_1^-})]
    $$

    The continuous integrals from (I) and (III) combine into a single integral over $[0, t]$ (the integrands are well-defined at $T_1$ since we use left limits), and the jump term appears as an isolated additive correction. This is precisely the Ito formula for jump processes applied to the case of a single jump.
