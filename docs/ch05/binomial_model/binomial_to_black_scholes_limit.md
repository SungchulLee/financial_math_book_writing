# Binomial to Black-Scholes Limit


The **binomial option pricing model** provides an intuitive discrete-time framework for option valuation. A fundamental result is that as the number of time steps increases to infinity, the binomial model **converges** to the **Black-Scholes model**. This connection demonstrates that the sophisticated continuous-time theory emerges naturally from simple discrete approximations.

This section rigorously establishes the convergence of the binomial model to the Black-Scholes framework.

---

## Notation Summary


Throughout this section, we maintain a clear distinction between discrete and continuous time:

**Discrete binomial model:**

- Node index: $i = 0, 1, 2, \ldots, n$
- Stock price at node $i$: $S_i$
- Option value at node $i$: $V_i$
- Time step: $dt = T/n$

**Continuous Black-Scholes model:**

- Continuous time: $t \in [0,T]$
- Stock price at time $t$: $S(t)$
- Option value: $V(S,t)$ (as a function)
- Differentials: $dS(t)$, $dW(t)$, $dt$

---

## Binomial Model Setup


### 1. **Discrete Time Structure**


Consider a time interval $[0, T]$ divided into $n$ steps:

$$
dt = \frac{T}{n}
$$

At each time step, the stock price evolves multiplicatively:

$$
S_{i+1} = \begin{cases}
uS_i & \text{with probability } q \\
dS_i & \text{with probability } 1-q
\end{cases}
$$

where:

- $i = 0, 1, 2, \ldots, n$: **node index** (time step number)
- $u > 1$: **up factor** (multiplicative increase)
- $0 < d < 1$: **down factor** (multiplicative decrease)  
- $q$: **risk-neutral probability** of upward move

### 2. **Parameter Specification**


To ensure convergence to geometric Brownian motion with volatility $\sigma$, the standard choice is:

$$
\boxed{u = e^{\sigma\sqrt{dt}}, \quad d = e^{-\sigma\sqrt{dt}}}
$$

**Rationale**: These choices ensure that:

1. The variance of log-returns matches the continuous-time model
2. The tree is recombining (up-then-down equals down-then-up)
3. The model is well-defined for all $dt > 0$

### 3. **Risk-Neutral Probability**


Under the risk-neutral measure, the expected return equals the risk-free rate:

$$
q \cdot u + (1-q) \cdot d = e^{r dt}
$$

Solving for $q$:

$$
\boxed{q = \frac{e^{r dt} - d}{u - d}}
$$

For small $dt$, using Taylor expansion $e^x \approx 1 + x + \frac{x^2}{2}$:

$$
q = \frac{(1 + rdt) - (1 - \sigma\sqrt{dt})}{2\sigma\sqrt{dt}} + O(dt) = \frac{1}{2} + \frac{r\sqrt{dt}}{2\sigma} + O(dt)
$$

As $dt \to 0$, the probability approaches $\frac{1}{2}$ with a small drift correction.

---

## Convergence of Stock Price Process


### 1. **Log-Price Representation**


After $n$ steps, the stock price is:

$$
S_n = S_0 u^{N_u} d^{N_d}
$$

where:

- $N_u$ = number of up moves
- $N_d$ = number of down moves
- $N_u + N_d = n$

Taking logarithms:

$$
\ln(S_n) = \ln(S_0) + N_u \ln(u) + N_d \ln(d)
$$

Substituting $u = e^{\sigma\sqrt{dt}}$ and $d = e^{-\sigma\sqrt{dt}}$:

$$
\ln(S_n) = \ln(S_0) + \sigma\sqrt{dt}(N_u - N_d)
$$

### 2. **Drift and Diffusion Decomposition**


Define:

$$
X_i = \begin{cases}
+1 & \text{if up move at step } i \\
-1 & \text{if down move at step } i
\end{cases}
$$

Then:

$$
N_u - N_d = \sum_{i=1}^n X_i
$$

Under the risk-neutral measure $\mathbb{Q}$:

$$
\mathbb{E}^{\mathbb{Q}}[X_i] = 2q - 1 = \frac{r\sqrt{dt}}{\sigma} + O(dt)
$$

$$
\text{Var}^{\mathbb{Q}}[X_i] = 1 - (2q-1)^2 = 1 - O(dt)
$$

### 3. **Central Limit Theorem**


As $n \to \infty$ (equivalently $dt \to 0$), by the **Central Limit Theorem**:

$$
\frac{1}{\sqrt{n}}\sum_{i=1}^n (X_i - \mathbb{E}[X_i]) \xrightarrow{d} \mathcal{N}(0, 1)
$$

Since $n = T/dt$ and $\sqrt{n \cdot dt} = \sqrt{T}$:

$$
\sum_{i=1}^n X_i \xrightarrow{d} \mathcal{N}\left(\frac{r T}{\sigma}, n\right) = \mathcal{N}\left(\frac{r T}{\sigma}, \frac{T}{dt}\right)
$$

### 4. **Log-Price Distribution**


Therefore:

$$
\ln(S_n) = \ln(S_0) + \sigma\sqrt{dt} \sum_{i=1}^n X_i
$$

converges in distribution to:

$$
\ln(S(T)) \sim \mathcal{N}\left(\ln(S_0) + \left(r - \frac{1}{2}\sigma^2\right)T, \sigma^2 T\right)
$$

where $S(T)$ denotes the stock price at continuous time $T$.

**Drift correction**: The term $-\frac{1}{2}\sigma^2$ appears due to **Itô's lemma** conversion from $dS/S$ to $d\ln S$.

### 5. **Geometric Brownian Motion**


This log-normal distribution characterizes the solution to the stochastic differential equation:

$$
\boxed{dS(t) = rS(t) \, dt + \sigma S(t) \, dW(t)}
$$

where $t \in [0,T]$ is continuous time. This is the **risk-neutral geometric Brownian motion** underlying the Black-Scholes model.

---

## Matching Variance


### 1. **Instantaneous Variance**


In one time step, the stock return is:

$$
\frac{S_{i+1} - S_i}{S_i} = \begin{cases}
u - 1 \approx \sigma\sqrt{dt} & \text{with prob. } q \\
d - 1 \approx -\sigma\sqrt{dt} & \text{with prob. } 1-q
\end{cases}
$$

The **variance** of the return over $dt$:

$$
\text{Var}\left(\frac{S_{i+1} - S_i}{S_i}\right) \approx \sigma^2 dt
$$

### 2. **Continuous-Time Limit**


Over the full period $[0, T]$, the total variance accumulates:

$$
\text{Var}(\ln(S_n/S_0)) = n \cdot \sigma^2 dt = \sigma^2 T
$$

This matches the variance in the Black-Scholes model:

$$
\text{Var}^{\mathbb{Q}}(\ln(S(T)/S_0)) = \sigma^2 T
$$

**Conclusion**: The binomial parameterization $u = e^{\sigma\sqrt{dt}}$, $d = e^{-\sigma\sqrt{dt}}$ ensures that the discrete model has the **same volatility structure** as the continuous model.

---

## Risk-Neutral Drift Convergence


### 1. **Expected Growth Rate**


Under the risk-neutral measure, the expected stock price after one step is:

$$
\mathbb{E}^{\mathbb{Q}}[S_{i+1} | S_i] = S_i(qu + (1-q)d)
$$

Substituting $q = \frac{e^{r dt} - d}{u - d}$:

$$
qu + (1-q)d = e^{r dt}
$$

Therefore:

$$
\mathbb{E}^{\mathbb{Q}}[S_{i+1} | S_i] = S_i e^{r dt} \approx S_i(1 + rdt)
$$

### 2. **Continuous-Time Equivalent**


As $dt \to 0$, this discrete expectation converges to the infinitesimal increment:

$$
\mathbb{E}^{\mathbb{Q}}[dS(t) | S(t)] = rS(t) \, dt
$$

which is exactly the **drift term** in the Black-Scholes SDE:

$$
dS(t) = rS(t) \, dt + \sigma S(t) \, dW(t)
$$

**Interpretation**: The binomial model's risk-neutral probability is calibrated so that the discrete expected return matches the continuous risk-free rate.

---

## Convergence of Option Pricing


### 1. **Binomial Option Valuation**


In the binomial model, option value at node $i$ is:

$$
V_i = e^{-r dt}\left[qV_{i+1}^{\text{up}} + (1-q)V_{i+1}^{\text{down}}\right]
$$

with terminal condition:

$$
V_n = \text{Payoff}(S_n)
$$

### 2. **Continuous Discounting**


As $dt \to 0$:

$$
e^{-r dt} \approx 1 - rdt + O((dt)^2)
$$

The discrete recursion becomes:

$$
V_i \approx V_{i+1} - rdt \cdot V_i + \text{(variance term)}
$$

Rearranging:

$$
\frac{V_{i+1} - V_i}{dt} \approx rV_i - \text{(second derivative terms)}
$$

### 3. **PDE Limit**


As $n \to \infty$ and $dt \to 0$, this discrete recursion converges to the **Black-Scholes PDE**:

$$
\boxed{\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0}
$$

with terminal condition:

$$
V(S, T) = \text{Payoff}(S)
$$

where $t$ is now continuous time and $V = V(S,t)$ is the option value as a function.

### 4. **Formula Convergence**


For a European call option, the binomial price:

$$
C_{\text{binomial}} = e^{-rT}\sum_{k=0}^n \binom{n}{k} q^k (1-q)^{n-k} (S_0 u^k d^{n-k} - K)^+
$$

converges to the Black-Scholes formula:

$$
C_{\text{BS}} = S_0 \mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
$$

as $n \to \infty$.

**Proof idea**: The binomial sum is a discrete approximation to the integral:

$$
\mathbb{E}^{\mathbb{Q}}[(S(T) - K)^+] = \int_0^\infty (S - K)^+ f(S) \, dS
$$

where $f(S)$ is the log-normal density and $S(T)$ is the stock price at time $T$.

---

## Replication Argument Carries Over


### 1. **Discrete-Time Hedging**


In the binomial model, at each node the option is replicated by a portfolio:

$$
V_i = \Delta_i S_i + B_i
$$

where:

- $\Delta_i = \frac{V_{i+1}^{\text{up}} - V_{i+1}^{\text{down}}}{S_i(u - d)}$ (delta at node $i$)
- $B_i$ = cash position at node $i$

### 2. **Continuous-Time Limit**


As $dt \to 0$:

$$
\Delta_i \to \frac{\partial V}{\partial S}
$$

The discrete hedging strategy converges to the **continuous delta hedging** in Black-Scholes:

$$
\Delta(S,t) = \frac{\partial V}{\partial S} = \mathcal{N}(d_1)
$$

where $(S,t)$ denotes continuous time and space.

**Self-financing**: The portfolio remains self-financing in the limit, meaning no additional cash is injected or withdrawn.

---

## Convergence Rate


### 1. **Error Analysis**


The error between binomial and Black-Scholes prices is:

$$
|C_{\text{binomial}} - C_{\text{BS}}| = O\left(\frac{1}{\sqrt{n}}\right)
$$

**Implication**: To achieve 3 decimal places of accuracy, approximately $n \geq 10^6$ steps may be required.

### 2. **Practical Considerations**


For practical implementations:

- **Small $n$** (e.g., $n = 50-100$): Fast computation, reasonable accuracy for ATM options
- **Large $n$** (e.g., $n = 1000+$): Higher accuracy but computationally expensive
- **Richardson extrapolation**: Can improve convergence rate to $O(1/n)$

---

## Extensions and Generalizations


### 1. **American Options**


The binomial method extends naturally to American options (with early exercise):

$$
V_i^{\text{American}} = \max\left(\text{Payoff}(S_i), e^{-r dt}[qV_{i+1}^{\text{up}} + (1-q)V_{i+1}^{\text{down}}]\right)
$$

There is **no closed-form** Black-Scholes formula for American options, so numerical methods remain essential.

### 2. **Dividends**


For dividend-paying stocks:

- **Continuous dividends**: Replace $r$ with $r - \delta$ in the drift
- **Discrete dividends**: Subtract PV of dividends from stock price at each ex-dividend date

### 3. **Alternative Parameterizations**


Other choices of $u, d$ exist:

- **Cox-Ross-Rubinstein**: $u = e^{\sigma\sqrt{dt}}$, $d = 1/u$
- **Jarrow-Rudd**: $u = e^{(r - \sigma^2/2)dt + \sigma\sqrt{dt}}$, $d = e^{(r - \sigma^2/2)dt - \sigma\sqrt{dt}}$

All converge to the same Black-Scholes limit but may have different convergence rates.

---

## Summary: Binomial vs. Black-Scholes


| Feature | Binomial Model | Black-Scholes Model |
|---------|----------------|---------------------|
| **Time** | Discrete (finite steps) | Continuous |
| **Indexing** | Node index $i = 0, \ldots, n$ | Continuous time $t \in [0,T]$ |
| **Price moves** | $u$ or $d$ per step | Infinitesimal $dW(t)$ |
| **Stock price** | $S_i$ at node $i$ | $S(t)$ at time $t$ |
| **Probability** | Risk-neutral $q$ | Measure $\mathbb{Q}$ |
| **Valuation** | Backward recursion | PDE or expectation |
| **Formula** | Summation over paths | Closed-form (European) |
| **Convergence** | $n \to \infty$ | Limit as $dt \to 0$ |
| **American options** | Easily handled | No closed form |
| **Intuition** | Very clear | Requires SDE theory |
| **Computation** | $O(n^2)$ | Instant (if closed form) |

---

## Practical Takeaway


The binomial tree remains **highly valuable** even after learning the Black-Scholes formula:

### 1. **Advantages of Binomial**


1. **Intuitive**: Easy to understand and explain to non-quants
2. **Flexible**: Handles American options, dividends, time-varying parameters
3. **Robust**: Works even when Black-Scholes assumptions fail
4. **Pedagogical**: Teaches replication and risk-neutral pricing clearly

### 2. **When to Use Each**


- **Black-Scholes**: European options, quick calculations, theoretical analysis
- **Binomial**: American options, exotic features, educational purposes, quick prototyping

### 3. **Complementary Roles**


- **Binomial** provides intuition and numerical approximation
- **Black-Scholes** provides analytical precision and mathematical elegance
- Together they form a complete toolkit for option pricing

---

## Conclusion


The binomial-to-Black-Scholes convergence is more than a mathematical curiosity—it reveals that:

1. **Discrete intuition generalizes**: Simple up/down moves lead to sophisticated continuous models
2. **No-arbitrage is universal**: The same principle governs both discrete and continuous time
3. **Replication works everywhere**: Delta hedging emerges naturally from discrete rebalancing
4. **Limiting processes are powerful**: Many properties (variance, drift, valuation) pass to the limit

This connection demonstrates the **unity of option pricing theory** across time scales and provides confidence that the seemingly abstract Black-Scholes framework rests on solid discrete foundations.

Understanding this limit is essential for:

- Appreciating where Black-Scholes comes from
- Knowing when binomial approximations suffice
- Extending models beyond Black-Scholes assumptions
- Building intuition for continuous-time finance

The binomial model thus serves as both a **practical tool** and a **theoretical bridge** to the continuous-time world of modern quantitative finance.
