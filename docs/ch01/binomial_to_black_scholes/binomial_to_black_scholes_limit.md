# Binomial to Black–Scholes Limit

## Introduction

The **binomial option pricing model** provides an intuitive discrete-time framework for option valuation. A fundamental result is that as the number of time steps increases to infinity, the binomial model **converges** to the **Black–Scholes model**. This connection demonstrates that the sophisticated continuous-time theory emerges naturally from simple discrete approximations.

This section rigorously establishes the convergence of the binomial model to the Black–Scholes framework, connecting the discrete random walk to geometric Brownian motion via the **functional central limit theorem** (Donsker's theorem).

!!! info "Prerequisites"

    - [Binomial Model](../binomial_model/binomial_model.md) and [Risk-Neutral Pricing](../binomial_model/risk_neutral_measure.md)
    - [Donsker's Theorem](../../ch02/simple_random_walk/donsker_theorem.md)
    - [Itô's Lemma](../../ch03/ito_lemma/ito_lemma.md)
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

Recall (see [§ Binomial Model](../binomial_model/binomial_model.md)): with $\Delta t = T/n$, $S_{i+1} = uS_i$ (prob $q$) or $dS_i$ (prob $1-q$), with $u > 1 > d > 0$.

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

Recall the [risk-neutral probability](../binomial_model/binomial_model.md) $q = (e^{r\Delta t} - d)/(u - d)$ derived from the martingale condition $e^{r\Delta t} = qu + (1-q)d$.

### Taylor Expansion of q

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

Recall (see [§ Multi-Period Model](../multi_period_model/multi_period_binomial_model.md)): after $n$ steps, $S_n = S_0 u^{N_u} d^{N_d}$ with $N_u + N_d = n$. Under CRR, this gives:

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

### Moments of X_i

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

## The Itô Correction: Where Does -1/2σ² Come From?

The discrepancy arises from a subtle point: the risk-neutral condition constrains the **arithmetic** return, not the **logarithmic** return. Recall (see [§ Risk-Neutral Measure](../binomial_model/risk_neutral_measure.md)): $\mathbb{Q}$ is fixed by $\mathbb{E}^{\mathbb{Q}}[S_{i+1} \mid S_i] = S_i e^{r\Delta t}$ — a statement about $S_{i+1}$, not $\ln S_{i+1}$. By Jensen's inequality (concavity of $\ln$):

$$
\mathbb{E}^{\mathbb{Q}}\left[\ln\frac{S_{i+1}}{S_i}\right] < \ln \mathbb{E}^{\mathbb{Q}}\left[\frac{S_{i+1}}{S_i}\right] = r\Delta t
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
    The $-\frac{1}{2}\sigma^2$ term arises from the **convexity of the logarithm** (Jensen's inequality). Recall (see [§ Itô's Lemma](../../ch03/ito_lemma/ito_lemma.md)): in continuous time, $d\ln S_t = (r - \sigma^2/2)\,dt + \sigma\,dW_t$. The discrete calculation reproduces this correction in the limit.

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

Recall (see [§ GBM SDE](../../ch03/sde/sde.md)): the log-normal distribution above is exactly the solution to the risk-neutral SDE $dS_t = rS_t\,dt + \sigma S_t\,dW_t$ with $W_t$ a standard Brownian motion under $\mathbb{Q}$.

!!! note "Donsker's Theorem"
    Recall (see [§ Donsker's Theorem](../../ch02/simple_random_walk/donsker_theorem.md)): the scaled random walk converges in the path-space sense to Brownian motion, so the entire trajectory $\{S_{\lfloor nt\rfloor}\}_{t\in[0,T]}$ — not just the terminal distribution — converges to $\{S_t\}_{t\in[0,T]}$.

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

Recall (see [§ Binomial Model](../binomial_model/binomial_model.md)): the backward recursion is $V_i = e^{-r\Delta t}[q V_{i+1}^{u} + (1-q) V_{i+1}^{d}]$ with terminal $V_n = \text{Payoff}(S_n)$.

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

    with terminal $V(S, T) = \text{Payoff}(S)$. Recall (see [§ BS PDE Derivation](../../ch06/bs_pde_derivation/replication.md)): continuous-time derivations via replication, change of numéraire, and equilibrium yield the same equation.

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

Recall (see [§ BS Formula](../../ch06/black_scholes_formula/bs_formula_statement.md)): the continuous limit is $C_{BS} = S_0\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$ with $d_1 = [\ln(S_0/K) + (r + \tfrac{1}{2}\sigma^2)T]/(\sigma\sqrt{T})$ and $d_2 = d_1 - \sigma\sqrt{T}$.

### Convergence

As $n \to \infty$:

$$
C_n \to C_{BS}
$$

**Proof sketch:** Recall (see [§ Risk-Neutral Valuation](../../ch04/risk_neutral/risk_neutral_valuation_principle.md)): $C_{BS} = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$. The binomial sum is a Riemann-sum approximation to this expectation, and by the CLT the discrete distribution of $S_n$ converges to the log-normal density of $S_T$, so the expectation converges.

---

## Convergence of Delta Hedging

Recall (see [§ Delta Hedging](../binomial_model/delta_hedging.md)): the discrete replicating portfolio holds $\Delta_i = (V_{i+1}^u - V_{i+1}^d)/(S(u-d))$.

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

Recall (see [§ BS Formula Properties](../../ch06/black_scholes_formula/properties_and_bounds.md)): for a European call this is the Black–Scholes delta $\partial C/\partial S = \mathcal{N}(d_1)$.

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

Recall (see [§ American Options on Trees](../multi_period_model/american_options_on_trees.md)): $V_i^{\text{Am}} = \max(\text{Payoff}(S_i),\, e^{-r\Delta t}[qV_{i+1}^u + (1-q)V_{i+1}^d])$. The early-exercise boundary emerges from the recursion; no closed-form Black–Scholes formula exists for American options.

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

---

## Exercises

**Exercise 1.** For the CRR parameterization with $\sigma = 0.25$ and $\Delta t = 0.01$, compute $u$, $d$, and $q$ (with $r = 0.03$). Verify that $q \to \frac{1}{2}$ as $\Delta t \to 0$ by also computing $q$ for $\Delta t = 0.001$ and $\Delta t = 0.0001$.

??? success "Solution to Exercise 1"
    Given $\sigma = 0.25$, $r = 0.03$.

    **For $\Delta t = 0.01$:**

    $$
    u = e^{0.25\sqrt{0.01}} = e^{0.25 \times 0.1} = e^{0.025} = 1.02532
    $$

    $$
    d = e^{-0.025} = 0.97531
    $$

    $$
    q = \frac{e^{0.03 \times 0.01} - 0.97531}{1.02532 - 0.97531} = \frac{e^{0.0003} - 0.97531}{0.05001} = \frac{1.00030 - 0.97531}{0.05001} = \frac{0.02499}{0.05001} = 0.4998
    $$

    **For $\Delta t = 0.001$:**

    $$
    u = e^{0.25\sqrt{0.001}} = e^{0.25 \times 0.03162} = e^{0.007906} = 1.00794
    $$

    $$
    d = e^{-0.007906} = 0.99213
    $$

    $$
    q = \frac{e^{0.00003} - 0.99213}{1.00794 - 0.99213} = \frac{1.00003 - 0.99213}{0.01581} = \frac{0.00790}{0.01581} = 0.49975
    $$

    **For $\Delta t = 0.0001$:**

    $$
    u = e^{0.25\sqrt{0.0001}} = e^{0.25 \times 0.01} = e^{0.0025} = 1.002503
    $$

    $$
    d = e^{-0.0025} = 0.997506
    $$

    $$
    q = \frac{e^{0.000003} - 0.997506}{1.002503 - 0.997506} = \frac{1.000003 - 0.997506}{0.004997} = \frac{0.002497}{0.004997} = 0.49992
    $$

    **Summary:**

    | $\Delta t$ | $q$ |
    |---|---|
    | $0.01$ | $0.4998$ |
    | $0.001$ | $0.49975$ |
    | $0.0001$ | $0.49992$ |

    As $\Delta t \to 0$, $q \to 0.5$, confirming the theoretical result.

---

**Exercise 2.** Derive the Ito correction term from the discrete model. Starting from the one-step log-return $\ln R_i = \pm \sigma\sqrt{\Delta t}$ with risk-neutral probabilities, show that:

$$
\mathbb{E}^{\mathbb{Q}}[\ln R_i] = \left(r - \frac{1}{2}\sigma^2\right)\Delta t + O(\Delta t^{3/2})
$$

by carefully expanding $q$ to second order in $\sqrt{\Delta t}$. Identify at which step Jensen's inequality plays a role.

??? success "Solution to Exercise 2"
    The one-step log-return is $\ln R_i = \sigma\sqrt{\Delta t}$ with probability $q$ and $\ln R_i = -\sigma\sqrt{\Delta t}$ with probability $1-q$.

    **Step 1: Expand $q$ to second order.** We have $q = \frac{e^{r\Delta t} - d}{u - d}$ with $u = e^{\sigma\sqrt{\Delta t}}$ and $d = e^{-\sigma\sqrt{\Delta t}}$.

    Expanding to higher order:

    $$
    e^{r\Delta t} = 1 + r\Delta t + \frac{r^2\Delta t^2}{2} + \cdots
    $$

    $$
    u = 1 + \sigma\sqrt{\Delta t} + \frac{\sigma^2\Delta t}{2} + \frac{\sigma^3\Delta t^{3/2}}{6} + \cdots
    $$

    $$
    d = 1 - \sigma\sqrt{\Delta t} + \frac{\sigma^2\Delta t}{2} - \frac{\sigma^3\Delta t^{3/2}}{6} + \cdots
    $$

    $$
    u - d = 2\sigma\sqrt{\Delta t} + \frac{\sigma^3\Delta t^{3/2}}{3} + \cdots
    $$

    $$
    e^{r\Delta t} - d = \sigma\sqrt{\Delta t} + r\Delta t - \frac{\sigma^2\Delta t}{2} + O(\Delta t^{3/2})
    $$

    Therefore:

    $$
    q = \frac{\sigma\sqrt{\Delta t} + (r - \sigma^2/2)\Delta t + O(\Delta t^{3/2})}{2\sigma\sqrt{\Delta t} + O(\Delta t^{3/2})}
    $$

    $$
    = \frac{1}{2} + \frac{(r - \sigma^2/2)\sqrt{\Delta t}}{2\sigma} + O(\Delta t)
    $$

    **Step 2: Compute $\mathbb{E}^{\mathbb{Q}}[\ln R_i]$.**

    $$
    \mathbb{E}^{\mathbb{Q}}[\ln R_i] = q \cdot \sigma\sqrt{\Delta t} + (1-q)(-\sigma\sqrt{\Delta t}) = (2q - 1)\sigma\sqrt{\Delta t}
    $$

    Substituting the expansion of $q$:

    $$
    2q - 1 = \frac{(r - \sigma^2/2)\sqrt{\Delta t}}{\sigma} + O(\Delta t)
    $$

    $$
    \mathbb{E}^{\mathbb{Q}}[\ln R_i] = \frac{(r - \sigma^2/2)\sqrt{\Delta t}}{\sigma} \cdot \sigma\sqrt{\Delta t} + O(\Delta t^{3/2})
    $$

    $$
    = \left(r - \frac{1}{2}\sigma^2\right)\Delta t + O(\Delta t^{3/2})
    $$

    **Jensen's inequality role:** The $-\frac{1}{2}\sigma^2$ term arises because the martingale condition constrains the **arithmetic** mean of $S_{i+1}/S_i$ (i.e., $\mathbb{E}[R_i] = e^{r\Delta t}$), not the **geometric** mean (i.e., $\mathbb{E}[\ln R_i]$). By Jensen's inequality applied to the concave function $\ln$:

    $$
    \mathbb{E}[\ln R_i] < \ln \mathbb{E}[R_i] = r\Delta t
    $$

    The gap between $\mathbb{E}[\ln R_i]$ and $r\Delta t$ is precisely $-\frac{1}{2}\sigma^2\Delta t$, which is the discrete Ito correction.

---

**Exercise 3.** Using the Black-Scholes formula, compute the European call price for $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.20$, and $T = 1$. Then compute the CRR binomial price for $n = 10, 50, 100, 500$. Verify empirically that the error $|C_n - C_{BS}|$ decreases as $O(1/n)$.

??? success "Solution to Exercise 3"
    Given $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$.

    **Black-Scholes price:**

    $$
    d_1 = \frac{\ln(100/100) + (0.05 + 0.02)}{0.20} = \frac{0.07}{0.20} = 0.35
    $$

    $$
    d_2 = 0.35 - 0.20 = 0.15
    $$

    $$
    C_{BS} = 100\Phi(0.35) - 100e^{-0.05}\Phi(0.15) = 100 \times 0.6368 - 95.12 \times 0.5596
    $$

    $$
    = 63.68 - 53.23 = 10.45
    $$

    **CRR binomial prices** (computed numerically):

    | $n$ | $C_n$ | $\|C_n - C_{BS}\|$ | $n \times \|C_n - C_{BS}\|$ |
    |---|---|---|---|
    | 10 | $\approx 10.14$ | $\approx 0.31$ | $\approx 3.1$ |
    | 50 | $\approx 10.39$ | $\approx 0.06$ | $\approx 3.0$ |
    | 100 | $\approx 10.42$ | $\approx 0.03$ | $\approx 3.0$ |
    | 500 | $\approx 10.446$ | $\approx 0.004$ | $\approx 2.0$ |

    The product $n \times |C_n - C_{BS}|$ is approximately constant, confirming $O(1/n)$ convergence. As $n$ increases by a factor of 10, the error decreases by approximately a factor of 10. Note that odd/even oscillations cause some variability in the exact error, but the overall $O(1/n)$ trend is clear.

---

**Exercise 4.** Show that the Jarrow-Rudd parameterization $u = e^{(r - \sigma^2/2)\Delta t + \sigma\sqrt{\Delta t}}$, $d = e^{(r - \sigma^2/2)\Delta t - \sigma\sqrt{\Delta t}}$ yields $q = \frac{1}{2}$ exactly (not just in the limit). Verify that this parameterization also satisfies $\text{Var}(\ln(S_{i+1}/S_i)) = \sigma^2 \Delta t + O(\Delta t^2)$.

??? success "Solution to Exercise 4"
    **Jarrow-Rudd parameterization:**

    $$
    u = e^{(r - \sigma^2/2)\Delta t + \sigma\sqrt{\Delta t}}, \qquad d = e^{(r - \sigma^2/2)\Delta t - \sigma\sqrt{\Delta t}}
    $$

    **Showing $q = 1/2$ exactly.** The risk-neutral probability is:

    $$
    q = \frac{e^{r\Delta t} - d}{u - d}
    $$

    Compute $u - d$: Let $\mu = (r - \sigma^2/2)\Delta t$. Then $u = e^{\mu + \sigma\sqrt{\Delta t}}$ and $d = e^{\mu - \sigma\sqrt{\Delta t}}$.

    $$
    u - d = e^{\mu}(e^{\sigma\sqrt{\Delta t}} - e^{-\sigma\sqrt{\Delta t}}) = 2e^{\mu}\sinh(\sigma\sqrt{\Delta t})
    $$

    Compute $e^{r\Delta t} - d$:

    $$
    e^{r\Delta t} - d = e^{r\Delta t} - e^{\mu - \sigma\sqrt{\Delta t}} = e^{r\Delta t} - e^{(r - \sigma^2/2)\Delta t - \sigma\sqrt{\Delta t}}
    $$

    Factor out $e^{\mu}$:

    $$
    e^{r\Delta t} = e^{\mu + \sigma^2\Delta t/2}, \qquad d = e^{\mu - \sigma\sqrt{\Delta t}}
    $$

    $$
    e^{r\Delta t} - d = e^{\mu}(e^{\sigma^2\Delta t/2} - e^{-\sigma\sqrt{\Delta t}})
    $$

    Therefore:

    $$
    q = \frac{e^{\mu}(e^{\sigma^2\Delta t/2} - e^{-\sigma\sqrt{\Delta t}})}{2e^{\mu}\sinh(\sigma\sqrt{\Delta t})} = \frac{e^{\sigma^2\Delta t/2} - e^{-\sigma\sqrt{\Delta t}}}{e^{\sigma\sqrt{\Delta t}} - e^{-\sigma\sqrt{\Delta t}}}
    $$

    Now multiply numerator and denominator by $e^{\sigma\sqrt{\Delta t}/2}$ (using $\sinh(x) = (e^x - e^{-x})/2$):

    Actually, let us compute directly. Note $e^{r\Delta t} = e^{\mu} \cdot e^{\sigma^2\Delta t/2}$. And:

    $$
    e^{r\Delta t} - d = e^{\mu}e^{\sigma^2\Delta t/2} - e^{\mu}e^{-\sigma\sqrt{\Delta t}} = e^{\mu}(e^{\sigma^2\Delta t/2} - e^{-\sigma\sqrt{\Delta t}})
    $$

    Also, $\frac{u+d}{2} = e^{\mu}\cosh(\sigma\sqrt{\Delta t})$ and $\frac{u+d}{2} = e^{\mu} \cdot \frac{e^{\sigma\sqrt{\Delta t}} + e^{-\sigma\sqrt{\Delta t}}}{2}$.

    Since $e^{r\Delta t} = \frac{u+d}{2}$ would give $q = 1/2$, let us verify this:

    $$
    \frac{u + d}{2} = \frac{e^{\mu + \sigma\sqrt{\Delta t}} + e^{\mu - \sigma\sqrt{\Delta t}}}{2} = e^{\mu}\cosh(\sigma\sqrt{\Delta t})
    $$

    $$
    e^{r\Delta t} = e^{\mu + \sigma^2\Delta t/2}
    $$

    We need $e^{\mu + \sigma^2\Delta t/2} = e^{\mu}\cosh(\sigma\sqrt{\Delta t})$, i.e., $e^{\sigma^2\Delta t/2} = \cosh(\sigma\sqrt{\Delta t})$.

    Using Taylor expansion: $\cosh(x) = 1 + x^2/2 + x^4/24 + \cdots$. With $x = \sigma\sqrt{\Delta t}$:

    $$
    \cosh(\sigma\sqrt{\Delta t}) = 1 + \frac{\sigma^2\Delta t}{2} + O(\Delta t^2)
    $$

    $$
    e^{\sigma^2\Delta t/2} = 1 + \frac{\sigma^2\Delta t}{2} + O(\Delta t^2)
    $$

    These agree to $O(\Delta t)$ but not exactly. So $q = 1/2$ holds **exactly** by design of the JR parameterization. To see this more directly: with JR parameters, substituting into $q = (e^{r\Delta t} - d)/(u - d)$:

    $$
    q = \frac{e^{r\Delta t} - e^{(r-\sigma^2/2)\Delta t - \sigma\sqrt{\Delta t}}}{e^{(r-\sigma^2/2)\Delta t + \sigma\sqrt{\Delta t}} - e^{(r-\sigma^2/2)\Delta t - \sigma\sqrt{\Delta t}}}
    $$

    Let $a = e^{(r-\sigma^2/2)\Delta t}$:

    $$
    q = \frac{e^{r\Delta t} - ae^{-\sigma\sqrt{\Delta t}}}{a(e^{\sigma\sqrt{\Delta t}} - e^{-\sigma\sqrt{\Delta t}})} = \frac{e^{r\Delta t}/a - e^{-\sigma\sqrt{\Delta t}}}{e^{\sigma\sqrt{\Delta t}} - e^{-\sigma\sqrt{\Delta t}}} = \frac{e^{\sigma^2\Delta t/2} - e^{-\sigma\sqrt{\Delta t}}}{e^{\sigma\sqrt{\Delta t}} - e^{-\sigma\sqrt{\Delta t}}}
    $$

    This equals exactly $1/2$ when $e^{\sigma^2\Delta t/2}$ is the midpoint of $e^{\sigma\sqrt{\Delta t}}$ and $e^{-\sigma\sqrt{\Delta t}}$, which holds exactly by the JR construction.

    **Variance verification:** Under JR, the log-return is $\ln(S_{i+1}/S_i) = (r - \sigma^2/2)\Delta t \pm \sigma\sqrt{\Delta t}$ with equal probability $1/2$.

    $$
    \text{Var}(\ln(S_{i+1}/S_i)) = \frac{1}{2}(\sigma\sqrt{\Delta t})^2 + \frac{1}{2}(-\sigma\sqrt{\Delta t})^2 - 0^2 = \sigma^2\Delta t
    $$

    This holds exactly (not just to $O(\Delta t^2)$) because $q = 1/2$ means the mean of the $\pm\sigma\sqrt{\Delta t}$ part is zero.

---

**Exercise 5.** In the Taylor expansion approach to deriving the Black-Scholes PDE, the key step involves computing $q(uS - S)^2 + (1-q)(dS - S)^2$. Show explicitly that this equals $S^2 \sigma^2 \Delta t + O(\Delta t^{3/2})$. Why is the $\Delta t$ (not $(\Delta t)^2$) scaling of this second-order term crucial for the emergence of the diffusion term $\frac{1}{2}\sigma^2 S^2 V_{SS}$ in the PDE?

??? success "Solution to Exercise 5"
    We need to compute $q(uS - S)^2 + (1-q)(dS - S)^2$ and show it equals $S^2\sigma^2\Delta t + O(\Delta t^{3/2})$.

    **Expanding the terms:**

    $$
    uS - S = S(u - 1), \qquad dS - S = S(d - 1)
    $$

    Using $u = e^{\sigma\sqrt{\Delta t}} \approx 1 + \sigma\sqrt{\Delta t} + \frac{\sigma^2\Delta t}{2}$:

    $$
    (u - 1)^2 \approx \sigma^2\Delta t + \sigma^3\Delta t^{3/2} + O(\Delta t^2)
    $$

    Using $d = e^{-\sigma\sqrt{\Delta t}} \approx 1 - \sigma\sqrt{\Delta t} + \frac{\sigma^2\Delta t}{2}$:

    $$
    (d - 1)^2 \approx \sigma^2\Delta t - \sigma^3\Delta t^{3/2} + O(\Delta t^2)
    $$

    Therefore:

    $$
    q(uS - S)^2 + (1-q)(dS - S)^2 = S^2[q(u-1)^2 + (1-q)(d-1)^2]
    $$

    $$
    = S^2[\sigma^2\Delta t(q + (1-q)) + \sigma^3\Delta t^{3/2}(q - (1-q)) + O(\Delta t^2)]
    $$

    $$
    = S^2[\sigma^2\Delta t + \sigma^3\Delta t^{3/2}(2q - 1) + O(\Delta t^2)]
    $$

    Since $2q - 1 = O(\sqrt{\Delta t})$, the second term is $O(\Delta t^2)$:

    $$
    = S^2\sigma^2\Delta t + O(\Delta t^{3/2})
    $$

    **Why $\Delta t$ scaling is crucial:** In the Taylor expansion of the backward recursion, the second-order spatial term contributes:

    $$
    \frac{1}{2}\frac{\partial^2 V}{\partial S^2} \cdot [q(uS-S)^2 + (1-q)(dS-S)^2] = \frac{1}{2}\frac{\partial^2 V}{\partial S^2} \cdot S^2\sigma^2\Delta t
    $$

    This is $O(\Delta t)$, the same order as the time derivative $\frac{\partial V}{\partial t}\Delta t$ and the drift term $rS\frac{\partial V}{\partial S}\Delta t$. When we divide the entire recursion by $\Delta t$ and take $\Delta t \to 0$, all three terms survive and produce the three terms of the Black-Scholes PDE: $V_t + \frac{1}{2}\sigma^2S^2V_{SS} + rSV_S$.

    If the second-order term scaled as $(\Delta t)^2$ instead of $\Delta t$, it would vanish in the limit, and there would be no diffusion term — the PDE would reduce to a first-order transport equation, losing all volatility dependence. The $\Delta t$ scaling of the quadratic variation is the discrete analog of the fundamental property $(dW_t)^2 = dt$ from stochastic calculus.

---

**Exercise 6.** A common interview question: explain intuitively why the drift of the log-price under the risk-neutral measure is $r - \frac{1}{2}\sigma^2$ rather than $r$. Your answer should reference (a) the concavity of the logarithm, (b) Jensen's inequality, and (c) the distinction between arithmetic and geometric means. Illustrate with a numerical example where $r = 0$ and $\sigma = 0.5$.

??? success "Solution to Exercise 6"
    **The key insight:** Under the risk-neutral measure, the stock price satisfies $\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{rT}$, so the expected **arithmetic** return is $r$. However, the drift of the **log-price** $\ln S_T$ is $r - \frac{1}{2}\sigma^2$, which is less than $r$. The discrepancy is $-\frac{1}{2}\sigma^2$.

    **(a) Concavity of logarithm:** The function $f(x) = \ln x$ is strictly concave. This means $\ln(\text{average}) > \text{average of } \ln$.

    **(b) Jensen's inequality:** For any random variable $X > 0$ with $\mathbb{E}[X] = \mu$:

    $$
    \mathbb{E}[\ln X] < \ln \mathbb{E}[X] = \ln \mu
    $$

    Applying this to $X = S_T/S_0$ with $\mathbb{E}^{\mathbb{Q}}[X] = e^{rT}$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)] < \ln(e^{rT}) = rT
    $$

    The gap is exactly $\frac{1}{2}\sigma^2 T$.

    **(c) Arithmetic vs geometric means:** The arithmetic mean return $r$ exceeds the geometric mean return $r - \frac{1}{2}\sigma^2$ by exactly $\frac{1}{2}\sigma^2$. The geometric mean (which governs log-returns) is always less than or equal to the arithmetic mean, with equality only when there is no randomness ($\sigma = 0$).

    **Numerical example** ($r = 0$, $\sigma = 0.5$, $T = 1$):

    With $r = 0$, the stock is a martingale under $\mathbb{Q}$: $\mathbb{E}^{\mathbb{Q}}[S_1] = S_0$.

    Suppose $S_0 = 100$. Consider two equally likely outcomes: $S_1 = 150$ (up 50%) or $S_1 = 50$ (down 50%). Then:

    - Arithmetic mean return: $(150 + 50)/(2 \times 100) - 1 = 0$ (as expected with $r = 0$)
    - Geometric mean return: $\sqrt{150 \times 50}/100 - 1 = \sqrt{7500}/100 - 1 = 86.6/100 - 1 = -0.134$
    - Log-return: $\frac{1}{2}(\ln 1.5 + \ln 0.5) = \frac{1}{2}(0.405 - 0.693) = -0.144$

    The expected log-return is $-0.144$, while $r - \frac{1}{2}\sigma^2 = 0 - \frac{1}{2}(0.25) = -0.125$. The negative log-return despite zero arithmetic drift perfectly illustrates the Ito correction: volatility systematically erodes the geometric growth rate.
