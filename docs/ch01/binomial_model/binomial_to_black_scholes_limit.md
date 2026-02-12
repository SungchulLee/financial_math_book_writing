# Binomial to Black–Scholes Limit

## Introduction

The **binomial option pricing model** provides an intuitive discrete-time framework for option valuation. A fundamental result is that as the number of time steps increases to infinity, the binomial model **converges** to the **Black–Scholes model**. This connection demonstrates that the sophisticated continuous-time theory emerges naturally from simple discrete approximations.

This section rigorously establishes the convergence of the binomial model to the Black–Scholes framework, connecting the discrete random walk to geometric Brownian motion via the **functional central limit theorem** (Donsker's theorem).

!!! info "Prerequisites"
    - [Binomial Model](binomial_model.md) and [Risk-Neutral Pricing](risk_neutral_measure.md)
    - [Donsker's Theorem](../../ch01/brownian_motion/donsker_theorem.md)
    - [Itô's Lemma](../../ch02/ito_lemma/ito_lemma.md)
    - Central Limit Theorem (basic probability)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Parameterize the binomial model to match Black–Scholes volatility
    2. Apply the CLT to show convergence of log-prices to normal distribution
    3. Derive the Itô correction term $-\frac{1}{2}\sigma^2$ from discrete principles
    4. Understand how the binomial recursion converges to the Black–Scholes PDE
    5. Explain the convergence of discrete delta hedging to continuous hedging

---

## Notation Summary

Throughout this section, we maintain a clear distinction between discrete and continuous time:

**Discrete binomial model:**

| Symbol | Meaning |
|--------|---------|
| $n$ | Number of time steps |
| $\Delta t = T/n$ | Length of each time step |
| $i = 0, 1, \ldots, n$ | Node index (time step number) |
| $S_i$ | Stock price at node $i$ (time $t_i = i \cdot \Delta t$) |
| $V_i$ | Option value at node $i$ |
| $u, d$ | Up and down multiplicative factors |
| $q$ | Risk-neutral probability of up move |

**Continuous Black–Scholes model:**

| Symbol | Meaning |
|--------|---------|
| $t \in [0, T]$ | Continuous time |
| $S(t)$ or $S_t$ | Stock price at time $t$ |
| $V(S, t)$ | Option value as function of $(S, t)$ |
| $dS_t$, $dW_t$ | Stochastic differentials |
| $\sigma$ | Volatility parameter |
| $r$ | Risk-free rate |

!!! warning "Notation Convention"
    We use $\Delta t$ (not $dt$) for the discrete time step to clearly distinguish from the infinitesimal $dt$ in continuous-time stochastic calculus. As $n \to \infty$, we have $\Delta t \to 0$.

---

## Binomial Model Setup

### Discrete Time Structure

Consider a time interval $[0, T]$ divided into $n$ equal steps:

$$
\Delta t = \frac{T}{n}
$$

At each time step, the stock price evolves multiplicatively:

$$
S_{i+1} = 
\begin{cases}
u S_i & \text{with probability } q \\[4pt]
d S_i & \text{with probability } 1-q
\end{cases}
$$

where $u > 1$ is the **up factor** and $0 < d < 1$ is the **down factor**.

### Parameter Specification (Cox–Ross–Rubinstein)

To ensure convergence to geometric Brownian motion with volatility $\sigma$, the standard **Cox–Ross–Rubinstein (CRR)** parameterization is:

$$
\boxed{u = e^{\sigma\sqrt{\Delta t}}, \quad d = e^{-\sigma\sqrt{\Delta t}} = \frac{1}{u}}
$$

!!! note "Why These Parameters?"
    These choices ensure:
    
    1. **Variance matching**: The variance of log-returns over $\Delta t$ equals $\sigma^2 \Delta t$
    2. **Recombining tree**: An up move followed by down equals a down move followed by up ($ud = 1$)
    3. **Centering**: $\ln u = -\ln d$, so the tree is symmetric in log-space
    4. **Well-defined**: Valid for all $\Delta t > 0$ and $\sigma > 0$

### Risk-Neutral Probability

Under the risk-neutral measure, the discounted stock price is a martingale:

$$
S_i = e^{-r\Delta t} \mathbb{E}^{\mathbb{Q}}[S_{i+1} | S_i]
$$

This requires:

$$
S_i = e^{-r\Delta t}(q \cdot u S_i + (1-q) \cdot d S_i)
$$

Simplifying:

$$
e^{r\Delta t} = qu + (1-q)d
$$

Solving for $q$:

$$
\boxed{q = \frac{e^{r\Delta t} - d}{u - d}}
$$

### Taylor Expansion of $q$

For small $\Delta t$, we expand each term:

$$
e^{r\Delta t} \approx 1 + r\Delta t + \frac{(r\Delta t)^2}{2} + O(\Delta t^{3/2})
$$

$$
u = e^{\sigma\sqrt{\Delta t}} \approx 1 + \sigma\sqrt{\Delta t} + \frac{\sigma^2 \Delta t}{2} + O(\Delta t^{3/2})
$$

$$
d = e^{-\sigma\sqrt{\Delta t}} \approx 1 - \sigma\sqrt{\Delta t} + \frac{\sigma^2 \Delta t}{2} + O(\Delta t^{3/2})
$$

Therefore:

$$
u - d \approx 2\sigma\sqrt{\Delta t}
$$

$$
e^{r\Delta t} - d \approx (1 + r\Delta t) - (1 - \sigma\sqrt{\Delta t}) = \sigma\sqrt{\Delta t} + r\Delta t
$$

Thus:

$$
q = \frac{\sigma\sqrt{\Delta t} + r\Delta t}{2\sigma\sqrt{\Delta t}} = \frac{1}{2} + \frac{r\sqrt{\Delta t}}{2\sigma} + O(\Delta t)
$$

!!! success "Risk-Neutral Probability Limit"
    As $\Delta t \to 0$:
    
    $$
    q \to \frac{1}{2}
    $$
    
    The probability approaches $\frac{1}{2}$ with a small drift correction of order $\sqrt{\Delta t}$.

---

## Convergence of Stock Price Process

### Log-Price Representation

After $n$ steps, starting from $S_0$, the stock price is:

$$
S_n = S_0 \cdot u^{N_u} \cdot d^{N_d}
$$

where:

- $N_u$ = number of up moves
- $N_d = n - N_u$ = number of down moves

Taking logarithms:

$$
\ln S_n = \ln S_0 + N_u \ln u + N_d \ln d
$$

With $u = e^{\sigma\sqrt{\Delta t}}$ and $d = e^{-\sigma\sqrt{\Delta t}}$:

$$
\ln S_n = \ln S_0 + N_u \cdot \sigma\sqrt{\Delta t} - N_d \cdot \sigma\sqrt{\Delta t}
$$

$$
\ln S_n = \ln S_0 + \sigma\sqrt{\Delta t}(N_u - N_d)
$$

### Random Walk Representation

Define the **step random variables**:

$$
X_i = 
\begin{cases}
+1 & \text{if up move at step } i \quad (\text{prob } q) \\[4pt]
-1 & \text{if down move at step } i \quad (\text{prob } 1-q)
\end{cases}
$$

Then:

$$
N_u - N_d = \sum_{i=1}^{n} X_i
$$

and the log-price becomes:

$$
\ln S_n = \ln S_0 + \sigma\sqrt{\Delta t} \sum_{i=1}^{n} X_i
$$

### Moments of $X_i$

Under the risk-neutral measure $\mathbb{Q}$:

**Mean:**
$$
\mathbb{E}^{\mathbb{Q}}[X_i] = (+1) \cdot q + (-1) \cdot (1-q) = 2q - 1
$$

Using $q = \frac{1}{2} + \frac{r\sqrt{\Delta t}}{2\sigma} + O(\Delta t)$:

$$
\mathbb{E}^{\mathbb{Q}}[X_i] = 2\left(\frac{1}{2} + \frac{r\sqrt{\Delta t}}{2\sigma}\right) - 1 + O(\Delta t) = \frac{r\sqrt{\Delta t}}{\sigma} + O(\Delta t)
$$

**Variance:**
$$
\mathbb{E}^{\mathbb{Q}}[X_i^2] = (+1)^2 \cdot q + (-1)^2 \cdot (1-q) = 1
$$

$$
\text{Var}^{\mathbb{Q}}(X_i) = \mathbb{E}[X_i^2] - (\mathbb{E}[X_i])^2 = 1 - O(\Delta t) \approx 1
$$

### Central Limit Theorem Application

Define the **scaled log-return**:

$$
Y_n := \ln S_n - \ln S_0 = \sigma\sqrt{\Delta t} \sum_{i=1}^{n} X_i
$$

**Mean of $Y_n$:**

$$
\mathbb{E}^{\mathbb{Q}}[Y_n] = \sigma\sqrt{\Delta t} \sum_{i=1}^{n} \mathbb{E}^{\mathbb{Q}}[X_i] = \sigma\sqrt{\Delta t} \cdot n \cdot \frac{r\sqrt{\Delta t}}{\sigma} + O(n \Delta t^{3/2})
$$

Since $n \cdot \Delta t = T$:

$$
\mathbb{E}^{\mathbb{Q}}[Y_n] = rT + O(\sqrt{\Delta t})
$$

**Variance of $Y_n$:**

Since $X_i$ are independent:

$$
\text{Var}^{\mathbb{Q}}(Y_n) = \sigma^2 \Delta t \sum_{i=1}^{n} \text{Var}^{\mathbb{Q}}(X_i) = \sigma^2 \Delta t \cdot n \cdot (1 + O(\Delta t))
$$

$$
\text{Var}^{\mathbb{Q}}(Y_n) = \sigma^2 T + O(\Delta t)
$$

**CLT Convergence:**

By the **Central Limit Theorem**, as $n \to \infty$:

$$
Y_n = \ln(S_n/S_0) \xrightarrow{d} \mathcal{N}(rT, \sigma^2 T)
$$

!!! warning "This Is Not Quite Right!"
    The calculation above gives $\mathbb{E}[\ln(S_n/S_0)] \to rT$, but the correct Black–Scholes result is:
    
    $$\mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)] = \left(r - \frac{1}{2}\sigma^2\right)T$$
    
    Where does the $-\frac{1}{2}\sigma^2$ term come from? This is the **Itô correction**, which we derive next.

---

## The Itô Correction: Where Does $-\frac{1}{2}\sigma^2$ Come From?

The discrepancy arises from a subtle point: the risk-neutral condition constrains the **arithmetic** return, not the **logarithmic** return.

### The Martingale Condition

The risk-neutral measure is defined so that the **discounted stock price** is a martingale:

$$
\mathbb{E}^{\mathbb{Q}}[S_{i+1} | S_i] = S_i \cdot e^{r\Delta t}
$$

This says something about $S_{i+1}$, not about $\ln S_{i+1}$.

### Jensen's Inequality

For a concave function $f(x) = \ln x$, Jensen's inequality states:

$$
\mathbb{E}[\ln X] \leq \ln \mathbb{E}[X]
$$

with equality only if $X$ is constant.

Since $S_{i+1}/S_i$ is random (not constant), we have:

$$
\mathbb{E}^{\mathbb{Q}}\left[\ln\frac{S_{i+1}}{S_i}\right] < \ln \mathbb{E}^{\mathbb{Q}}\left[\frac{S_{i+1}}{S_i}\right] = \ln(e^{r\Delta t}) = r\Delta t
$$

The gap is the **Itô correction**.

### Explicit Calculation

Let $R_i = S_{i+1}/S_i$ be the gross return at step $i$. Then:

$$
R_i = 
\begin{cases}
u = e^{\sigma\sqrt{\Delta t}} & \text{with prob } q \\[4pt]
d = e^{-\sigma\sqrt{\Delta t}} & \text{with prob } 1-q
\end{cases}
$$

The log-return is:

$$
\ln R_i = 
\begin{cases}
\sigma\sqrt{\Delta t} & \text{with prob } q \\[4pt]
-\sigma\sqrt{\Delta t} & \text{with prob } 1-q
\end{cases}
$$

**Expected log-return:**

$$
\mathbb{E}^{\mathbb{Q}}[\ln R_i] = q \cdot \sigma\sqrt{\Delta t} + (1-q) \cdot (-\sigma\sqrt{\Delta t}) = (2q-1)\sigma\sqrt{\Delta t}
$$

Using $q = \frac{1}{2} + \frac{r\sqrt{\Delta t}}{2\sigma} + O(\Delta t)$:

$$
2q - 1 = \frac{r\sqrt{\Delta t}}{\sigma} + O(\Delta t)
$$

$$
\mathbb{E}^{\mathbb{Q}}[\ln R_i] = \frac{r\sqrt{\Delta t}}{\sigma} \cdot \sigma\sqrt{\Delta t} + O(\Delta t^{3/2}) = r\Delta t + O(\Delta t^{3/2})
$$

This gives $\mathbb{E}[\ln R_i] \approx r\Delta t$, which would sum to $rT$ over $n$ steps.

**But wait—we need a more careful expansion!**

### Second-Order Correction

The issue is that we need to track the $O(\Delta t)$ terms more carefully. Let's use a different approach.

The martingale condition gives:

$$
\mathbb{E}^{\mathbb{Q}}[R_i] = e^{r\Delta t}
$$

Now, for any random variable $R > 0$ with small variance, we have the approximation:

$$
\mathbb{E}[\ln R] \approx \ln \mathbb{E}[R] - \frac{\text{Var}(R)}{2(\mathbb{E}[R])^2}
$$

This is a second-order Taylor expansion of $\ln$ around $\mathbb{E}[R]$.

**Variance of $R_i$:**

$$
\mathbb{E}^{\mathbb{Q}}[R_i^2] = q \cdot u^2 + (1-q) \cdot d^2 = q \cdot e^{2\sigma\sqrt{\Delta t}} + (1-q) \cdot e^{-2\sigma\sqrt{\Delta t}}
$$

For small $\Delta t$:

$$
\mathbb{E}^{\mathbb{Q}}[R_i^2] \approx q(1 + 2\sigma\sqrt{\Delta t} + 2\sigma^2\Delta t) + (1-q)(1 - 2\sigma\sqrt{\Delta t} + 2\sigma^2\Delta t)
$$

$$
= 1 + 2\sigma\sqrt{\Delta t}(2q-1) + 2\sigma^2\Delta t
$$

$$
\approx 1 + 2r\Delta t + 2\sigma^2\Delta t + O(\Delta t^{3/2})
$$

Since $\mathbb{E}[R_i] = e^{r\Delta t} \approx 1 + r\Delta t$:

$$
\text{Var}(R_i) = \mathbb{E}[R_i^2] - (\mathbb{E}[R_i])^2 \approx (1 + 2r\Delta t + 2\sigma^2\Delta t) - (1 + 2r\Delta t) = 2\sigma^2\Delta t
$$

Wait, this gives variance $\approx 2\sigma^2\Delta t$, but the correct variance of $R_i - 1$ should be $\sigma^2\Delta t$. Let me redo this more carefully.

**Correct variance calculation:**

$$
R_i = e^{\pm\sigma\sqrt{\Delta t}} \approx 1 \pm \sigma\sqrt{\Delta t} + \frac{\sigma^2\Delta t}{2}
$$

$$
\text{Var}(R_i) \approx \text{Var}(\pm\sigma\sqrt{\Delta t}) = \sigma^2\Delta t \cdot \text{Var}(\pm 1) = \sigma^2\Delta t \cdot 1 = \sigma^2\Delta t
$$

(since $\text{Var}(\text{sign}) = 1 - (2q-1)^2 \approx 1$)

**Applying the correction:**

$$
\mathbb{E}[\ln R_i] \approx \ln \mathbb{E}[R_i] - \frac{\text{Var}(R_i)}{2(\mathbb{E}[R_i])^2}
$$

$$
\approx r\Delta t - \frac{\sigma^2\Delta t}{2 \cdot 1} = \left(r - \frac{\sigma^2}{2}\right)\Delta t
$$

**Summing over $n$ steps:**

$$
\mathbb{E}^{\mathbb{Q}}[\ln(S_n/S_0)] = \sum_{i=1}^{n} \mathbb{E}^{\mathbb{Q}}[\ln R_i] \approx n \cdot \left(r - \frac{\sigma^2}{2}\right)\Delta t = \left(r - \frac{\sigma^2}{2}\right)T
$$

!!! success "Itô Correction Derived"
    The $-\frac{1}{2}\sigma^2$ term arises from the **convexity of the logarithm** (Jensen's inequality). In continuous time, this is captured by Itô's lemma:
    
    $$d\ln S_t = \frac{dS_t}{S_t} - \frac{1}{2}\frac{(dS_t)^2}{S_t^2} = \left(r - \frac{\sigma^2}{2}\right)dt + \sigma dW_t$$
    
    The discrete calculation reproduces this correction in the limit.

---

## Log-Price Distribution and Geometric Brownian Motion

### Final Distribution

Combining the CLT with the Itô correction, as $n \to \infty$:

$$
\ln S_n \xrightarrow{d} \mathcal{N}\left(\ln S_0 + \left(r - \frac{1}{2}\sigma^2\right)T, \, \sigma^2 T\right)
$$

Equivalently, $S_n$ converges in distribution to a **log-normal** random variable:

$$
S_T = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)T + \sigma W_T\right)
$$

where $W_T \sim \mathcal{N}(0, T)$.

### Connection to Geometric Brownian Motion

This log-normal distribution is exactly the solution to the **risk-neutral SDE**:

$$
\boxed{dS_t = rS_t \, dt + \sigma S_t \, dW_t}
$$

where $W_t$ is a standard Brownian motion under $\mathbb{Q}$.

!!! note "Donsker's Theorem"
    The convergence of the scaled random walk to Brownian motion is a special case of **Donsker's theorem** (the functional central limit theorem). See [Donsker's Theorem](../../ch01/brownian_motion/donsker_theorem.md) for the general statement.
    
    Donsker's theorem gives convergence of the entire **path** $\{S_{[nt]/n}\}_{t \in [0,T]}$ to $\{S_t\}_{t \in [0,T]}$, not just the terminal distribution.

---

## Matching Variance

### Per-Step Variance

In one time step, the log-return is:

$$
\ln\frac{S_{i+1}}{S_i} = 
\begin{cases}
+\sigma\sqrt{\Delta t} & \text{with prob } q \\[4pt]
-\sigma\sqrt{\Delta t} & \text{with prob } 1-q
\end{cases}
$$

The variance:

$$
\text{Var}\left(\ln\frac{S_{i+1}}{S_i}\right) = \sigma^2\Delta t \cdot \text{Var}(\pm 1) = \sigma^2\Delta t \cdot (1 - (2q-1)^2)
$$

Since $(2q-1)^2 = O(\Delta t)$:

$$
\text{Var}\left(\ln\frac{S_{i+1}}{S_i}\right) = \sigma^2\Delta t + O(\Delta t^2)
$$

### Total Variance

Over $n$ independent steps:

$$
\text{Var}(\ln(S_n/S_0)) = n \cdot \sigma^2\Delta t = \sigma^2 T
$$

This matches the Black–Scholes variance exactly:

$$
\text{Var}^{\mathbb{Q}}(\ln(S_T/S_0)) = \sigma^2 T
$$

!!! success "Variance Matching"
    The CRR parameterization $u = e^{\sigma\sqrt{\Delta t}}$, $d = e^{-\sigma\sqrt{\Delta t}}$ ensures that the discrete model has the **same volatility structure** as the continuous model for any number of steps $n$.

---

## Convergence of Option Pricing

### Binomial Backward Recursion

In the binomial model, the option value at node $i$ satisfies:

$$
V_i = e^{-r\Delta t}\left[q V_{i+1}^{u} + (1-q) V_{i+1}^{d}\right]
$$

with terminal condition:

$$
V_n = \text{Payoff}(S_n)
$$

where $V_{i+1}^u$ (resp. $V_{i+1}^d$) is the option value at the up (resp. down) successor node.

### Taylor Expansion Approach

To derive the PDE limit, we expand $V$ as a smooth function $V(S, t)$ and examine the discrete recursion.

At node $i$, let $S = S_i$ and $t = i \cdot \Delta t$. The successor values are:

$$
V_{i+1}^u = V(uS, t + \Delta t), \quad V_{i+1}^d = V(dS, t + \Delta t)
$$

**Taylor expand in time:**

$$
V(uS, t + \Delta t) = V(uS, t) + \frac{\partial V}{\partial t}(uS, t)\Delta t + O(\Delta t^2)
$$

**Taylor expand in space** around $S$:

$$
V(uS, t) = V(S, t) + \frac{\partial V}{\partial S}(S, t)(uS - S) + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(S, t)(uS - S)^2 + O((uS-S)^3)
$$

Since $u = e^{\sigma\sqrt{\Delta t}} \approx 1 + \sigma\sqrt{\Delta t} + \frac{\sigma^2\Delta t}{2}$:

$$
uS - S = S(u - 1) \approx S\sigma\sqrt{\Delta t} + O(\Delta t)
$$

$$(uS - S)^2 \approx S^2\sigma^2\Delta t$$

Similarly for the down node:

$$
dS - S \approx -S\sigma\sqrt{\Delta t} + O(\Delta t)
$$

$$(dS - S)^2 \approx S^2\sigma^2\Delta t$$

### Computing the Expectation

The risk-neutral expected successor value is:

$$
q V(uS, t) + (1-q) V(dS, t)
$$

**First-order terms:**

$$
q(uS - S) + (1-q)(dS - S) = S[q(u-1) + (1-q)(d-1)] = S[qu + (1-q)d - 1]
$$

Since $qu + (1-q)d = e^{r\Delta t} \approx 1 + r\Delta t$:

$$
q(uS - S) + (1-q)(dS - S) \approx rS\Delta t
$$

**Second-order terms:**

$$
q(uS - S)^2 + (1-q)(dS - S)^2 \approx S^2\sigma^2\Delta t \cdot [q + (1-q)] = S^2\sigma^2\Delta t
$$

### Assembling the PDE

The backward recursion becomes:

$$
V(S, t) = e^{-r\Delta t}\left[V(S, t) + \frac{\partial V}{\partial S} \cdot rS\Delta t + \frac{1}{2}\frac{\partial^2 V}{\partial S^2} \cdot S^2\sigma^2\Delta t + \frac{\partial V}{\partial t}\Delta t + O(\Delta t^{3/2})\right]
$$

Using $e^{-r\Delta t} \approx 1 - r\Delta t$:

$$
V = (1 - r\Delta t)\left[V + \frac{\partial V}{\partial S} rS\Delta t + \frac{1}{2}\frac{\partial^2 V}{\partial S^2} S^2\sigma^2\Delta t + \frac{\partial V}{\partial t}\Delta t\right] + O(\Delta t^{3/2})
$$

Expanding and keeping terms up to $O(\Delta t)$:

$$
V = V - rV\Delta t + \frac{\partial V}{\partial S} rS\Delta t + \frac{1}{2}\frac{\partial^2 V}{\partial S^2} S^2\sigma^2\Delta t + \frac{\partial V}{\partial t}\Delta t + O(\Delta t^{3/2})
$$

Canceling $V$ and dividing by $\Delta t$:

$$
0 = -rV + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + \frac{\partial V}{\partial t} + O(\sqrt{\Delta t})
$$

Taking $\Delta t \to 0$:

!!! success "Black–Scholes PDE"
    $$
    \boxed{\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0}
    $$
    
    with terminal condition $V(S, T) = \text{Payoff}(S)$.

---

## Convergence of Option Prices

### Binomial Formula for European Call

For a European call with strike $K$, the binomial price is:

$$
C_n = e^{-rT}\sum_{k=0}^{n} \binom{n}{k} q^k (1-q)^{n-k} (S_0 u^k d^{n-k} - K)^+
$$

The payoff is positive only when $S_0 u^k d^{n-k} > K$, i.e., when:

$$
k > k^* := \frac{\ln(K/S_0) - n\ln d}{\ln(u/d)} = \frac{\ln(K/S_0) + n\sigma\sqrt{\Delta t}}{2\sigma\sqrt{\Delta t}}
$$

So the sum effectively runs from $k = \lceil k^* \rceil$ to $n$.

### Black–Scholes Formula

The continuous limit is the **Black–Scholes formula**:

$$
C_{BS} = S_0 \Phi(d_1) - Ke^{-rT}\Phi(d_2)
$$

where $\Phi$ is the standard normal CDF and:

$$
d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
$$

### Convergence

As $n \to \infty$:

$$
C_n \to C_{BS}
$$

**Proof sketch:** The binomial sum is a Riemann sum approximation to:

$$
C_{BS} = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+] = e^{-rT}\int_K^\infty (S - K) f_{S_T}(S) \, dS
$$

where $f_{S_T}$ is the log-normal density of $S_T$. By the CLT, the discrete distribution of $S_n$ converges to this log-normal, so the expectation converges.

---

## Convergence of Delta Hedging

### Discrete Delta

In the binomial model, at node $(i, j)$ with stock price $S$, the replicating portfolio holds:

$$
\Delta_i = \frac{V_{i+1}^u - V_{i+1}^d}{S(u - d)} = \frac{V(uS, t+\Delta t) - V(dS, t+\Delta t)}{S(u - d)}
$$

### Taylor Expansion

Expanding around $(S, t)$:

$$
V(uS, t+\Delta t) - V(dS, t+\Delta t) \approx \frac{\partial V}{\partial S}(S, t) \cdot S(u - d) + O(\Delta t)
$$

Therefore:

$$
\Delta_i \approx \frac{\partial V}{\partial S}(S, t) + O(\sqrt{\Delta t})
$$

### Continuous Limit

As $\Delta t \to 0$:

$$
\Delta_i \to \frac{\partial V}{\partial S}(S, t)
$$

For a European call, this is the **Black–Scholes delta**:

$$
\Delta = \frac{\partial C}{\partial S} = \Phi(d_1)
$$

!!! success "Hedging Convergence"
    The discrete binomial hedging strategy converges to continuous **delta hedging**. The replicating portfolio remains self-financing in the limit.

---

## Convergence Rate

### Error Behavior

For the CRR binomial model pricing European options:

$$
|C_n - C_{BS}| = O\left(\frac{1}{n}\right)
$$

with **oscillations** between odd and even $n$.

!!! warning "Common Misconception"
    Some sources state $O(1/\sqrt{n})$ convergence, but for smooth payoffs (European calls/puts), the CRR model achieves $O(1/n)$ convergence. The $O(1/\sqrt{n})$ rate applies to certain path-dependent options or non-smooth payoffs.

### Practical Guidance

| Steps $n$ | Typical Error | Use Case |
|-----------|---------------|----------|
| 50–100 | ~1% | Quick estimates, American options |
| 500–1000 | ~0.1% | Production pricing |
| 10,000+ | ~0.01% | High-precision benchmarks |

### Acceleration Techniques

- **Richardson extrapolation**: Combine $C_n$ and $C_{2n}$ to cancel leading error term, achieving $O(1/n^2)$
- **Smoothing**: Use $C_n^{smooth} = \frac{1}{2}(C_n + C_{n+1})$ to reduce oscillations
- **Adaptive mesh**: Concentrate nodes near strike for barrier/digital options

---

## Extensions

### American Options

The binomial method handles American options naturally:

$$
V_i^{American} = \max\left(\text{Payoff}(S_i), \, e^{-r\Delta t}[qV_{i+1}^u + (1-q)V_{i+1}^d]\right)
$$

The early exercise boundary emerges from the recursion. There is **no closed-form** Black–Scholes formula for American options.

### Dividends

**Continuous dividend yield $\delta$:** Replace $r$ with $r - \delta$ in the drift:

$$
q = \frac{e^{(r-\delta)\Delta t} - d}{u - d}
$$

**Discrete dividends:** At ex-dividend dates, reduce $S$ by the dividend amount.

### Alternative Parameterizations

| Method | $u$ | $d$ | Notes |
|--------|-----|-----|-------|
| **CRR** | $e^{\sigma\sqrt{\Delta t}}$ | $e^{-\sigma\sqrt{\Delta t}}$ | Symmetric, recombining |
| **Jarrow–Rudd** | $e^{(r-\sigma^2/2)\Delta t + \sigma\sqrt{\Delta t}}$ | $e^{(r-\sigma^2/2)\Delta t - \sigma\sqrt{\Delta t}}$ | Equal probabilities $q = \frac{1}{2}$ |
| **Tian** | Various | Various | Third-moment matching |

All converge to Black–Scholes but with different convergence rates and oscillation patterns.

---

## Summary: Binomial vs. Black–Scholes

| Feature | Binomial Model | Black–Scholes Model |
|---------|----------------|---------------------|
| **Time** | Discrete: $t_i = i\Delta t$ | Continuous: $t \in [0,T]$ |
| **Price process** | Multiplicative jumps $u, d$ | GBM: $dS = rS\,dt + \sigma S\,dW$ |
| **Probability** | Risk-neutral $q$ | Measure $\mathbb{Q}$ |
| **Valuation** | Backward recursion | PDE or $\mathbb{E}^{\mathbb{Q}}$ |
| **European options** | Summation formula | Closed-form (BS formula) |
| **American options** | Early exercise check | No closed form |
| **Computation** | $O(n^2)$ time, $O(n)$ space | Instant (if closed form) |
| **Flexibility** | High (dividends, barriers, etc.) | Limited without extensions |

---

## Key Takeaways

!!! abstract "Summary"
    1. **Parameter matching**: $u = e^{\sigma\sqrt{\Delta t}}$, $d = 1/u$ ensures variance $\sigma^2\Delta t$ per step
    
    2. **CLT convergence**: The scaled random walk $\sum X_i$ converges to Brownian motion
    
    3. **Itô correction**: The $-\frac{1}{2}\sigma^2$ drift adjustment arises from Jensen's inequality (convexity of log)
    
    4. **PDE emergence**: Taylor expansion of the binomial recursion yields the Black–Scholes PDE
    
    5. **Delta convergence**: Discrete hedge ratio $\to \frac{\partial V}{\partial S}$
    
    6. **Practical value**: Binomial remains essential for American options and exotic features

The binomial-to-Black–Scholes limit demonstrates the **unity of option pricing theory**: the same no-arbitrage principles govern both discrete and continuous time, and sophisticated continuous models emerge naturally from simple discrete foundations.
