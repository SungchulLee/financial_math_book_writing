# Binomial to Black-Scholes Limit

The **binomial option pricing model** provides an intuitive discrete-time framework for option valuation. A fundamental result is that as the number of time steps increases to infinity, the binomial model **converges** to the **Black-Scholes model**. This connection demonstrates that the sophisticated continuous-time theory emerges naturally from simple discrete approximations.

This section rigorously establishes the convergence of the binomial model to the Black-Scholes framework.

---

## 1. Binomial Model Setup

### **Discrete Time Structure**

Consider a time interval $[0, T]$ divided into $n$ steps:



$$
\Delta t = \frac{T}{n}
$$



At each time step, the stock price evolves multiplicatively:



$$
S_{i+1} = \begin{cases}
uS_i & \text{with probability } q \\
dS_i & \text{with probability } 1-q
\end{cases}
$$



where:

- $u > 1$: **up factor** (multiplicative increase)

- $0 < d < 1$: **down factor** (multiplicative decrease)  

- $q$: **risk-neutral probability** of upward move

### **Parameter Specification**

To ensure convergence to geometric Brownian motion with volatility $\sigma$, the standard choice is:



$$
\boxed{u = e^{\sigma\sqrt{\Delta t}}, \quad d = e^{-\sigma\sqrt{\Delta t}}}
$$



**Rationale**: These choices ensure that:

1. The variance of log-returns matches the continuous-time model
2. The tree is recombining (up-then-down equals down-then-up)
3. The model is well-defined for all $\Delta t > 0$

### **Risk-Neutral Probability**

Under the risk-neutral measure, the expected return equals the risk-free rate:



$$
q \cdot u + (1-q) \cdot d = e^{r\Delta t}
$$



Solving for $q$:



$$
\boxed{q = \frac{e^{r\Delta t} - d}{u - d}}
$$



For small $\Delta t$, using Taylor expansion $e^x \approx 1 + x + \frac{x^2}{2}$:



$$
q = \frac{$1 + r\Delta t$ - $1 - \sigma\sqrt{\Delta t}$}{2\sigma\sqrt{\Delta t}} + O$\Delta t$ = \frac{1}{2} + \frac{r\sqrt{\Delta t}}{2\sigma} + O$\Delta t$
$$



As $\Delta t \to 0$, the probability approaches $\frac{1}{2}$ with a small drift correction.

---

## 2. Convergence of Stock Price Process

### **Log-Price Representation**

After $n$ steps, the stock price is:



$$
S_T = S_0 u^{N_u} d^{N_d}
$$



where:

- $N_u$ = number of up moves

- $N_d$ = number of down moves

- $N_u + N_d = n$

Taking logarithms:



$$
\ln$S_T$ = \ln$S_0$ + N_u \ln(u) + N_d \ln(d)
$$



Substituting $u = e^{\sigma\sqrt{\Delta t}}$ and $d = e^{-\sigma\sqrt{\Delta t}}$:



$$
\ln$S_T$ = \ln$S_0$ + \sigma\sqrt{\Delta t}$N_u - N_d$
$$



### **Drift and Diffusion Decomposition**

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
\mathbb{E}^{\mathbb{Q}}[X_i] = 2q - 1 = \frac{r\sqrt{\Delta t}}{\sigma} + O$\Delta t$
$$





$$
\text{Var}^{\mathbb{Q}}$X_i$ = 1 - (2q-1)^2 = 1 - O$\Delta t$
$$



### **Central Limit Theorem**

As $n \to \infty$ $equivalently $\Delta t \to 0

$$
, by the **Central Limit Theorem**:
$$


\frac{1}{\sqrt{n}}\sum_{i=1}^n $X_i - \mathbb{E}[X_i]$ \xrightarrow{d} \mathcal{N}(0, 1)


$$
Since $n = T/\Delta t$ and $\sqrt{n\Delta t} = \sqrt{T}$:
$$


\sum_{i=1}^n X_i \xrightarrow{d} \mathcal{N}\left$\frac{r\sqrt{T}}{\sigma} \cdot \sqrt{n\Delta t}, n\right$


$$
### **Log-Price Distribution**

Therefore:
$$


\ln$S_T$ = \ln$S_0$ + \sigma\sqrt{\Delta t} \sum_{i=1}^n X_i


$$
converges in distribution to:
$$


\ln$S_T$ \sim \mathcal{N}\left(\ln$S_0$ + \left$r - \frac{1}{2}\sigma^2\right$T, \sigma^2 T\right)


$$
**Drift correction**: The term $-\frac{1}{2}\sigma^2$ appears due to **Itô's lemma** $conversion from $dS/S$ to $d\ln S
$$

.

### **Geometric Brownian Motion**

This log-normal distribution characterizes the solution to the stochastic differential equation:



$$
\boxed{dS_t = rS_t dt + \sigma S_t dW_t}
$$



which is the **risk-neutral geometric Brownian motion** underlying the Black-Scholes model.

---

## 3. Matching Variance

### **Instantaneous Variance**

In one time step, the stock return is:



$$
\frac{S_{i+1} - S_i}{S_i} = \begin{cases}
u - 1 \approx \sigma\sqrt{\Delta t} & \text{with prob. } q \\
d - 1 \approx -\sigma\sqrt{\Delta t} & \text{with prob. } 1-q
\end{cases}
$$



The **variance** of the return over $\Delta t$:



$$
\text{Var}\left$\frac{S_{i+1} - S_i}{S_i}\right$ \approx \sigma^2 \Delta t
$$



### **Continuous-Time Limit**

Over the full period $[0, T]$, the total variance accumulates:



$$
\text{Var}(\ln$S_T/S_0$) = n \cdot \sigma^2 \Delta t = \sigma^2 T
$$



This matches the variance in the Black-Scholes model:



$$
\text{Var}^{\mathbb{Q}}(\ln$S_T/S_0$) = \sigma^2 T
$$



**Conclusion**: The binomial parameterization $u = e^{\sigma\sqrt{\Delta t}}$, $d = e^{-\sigma\sqrt{\Delta t}}$ ensures that the discrete model has the **same volatility structure** as the continuous model.

---

## 4. Risk-Neutral Drift Convergence

### **Expected Growth Rate**

Under the risk-neutral measure, the expected stock price after one step is:



$$
\mathbb{E}^{\mathbb{Q}}[S_{i+1} | S_i] = S_i(qu + (1-q)d)
$$



Substituting $q = \frac{e^{r\Delta t} - d}{u - d}$:



$$
qu + (1-q)d = e^{r\Delta t}
$$



Therefore:



$$
\mathbb{E}^{\mathbb{Q}}[S_{i+1} | S_i] = S_i e^{r\Delta t} \approx S_i$1 + r\Delta t$
$$



### **Continuous-Time Equivalent**

As $\Delta t \to 0$, this discrete expectation converges to:



$$
\mathbb{E}^{\mathbb{Q}}[dS_t | S_t] = rS_t dt
$$



which is exactly the **drift term** in the Black-Scholes SDE:



$$
dS_t = rS_t dt + \sigma S_t dW_t
$$



**Interpretation**: The binomial model's risk-neutral probability is calibrated so that the discrete expected return matches the continuous risk-free rate.

---

## 5. Convergence of Option Pricing

### **Binomial Option Valuation**

In the binomial model, option value at time $i$ is:



$$
V_i = \frac{1}{1 + r\Delta t}\left[qV_{i+1}^{\text{up}} + (1-q)V_{i+1}^{\text{down}}\right]
$$



with terminal condition:



$$
V_n = \text{Payoff}$S_n$
$$



### **Continuous Discounting**

As $\Delta t \to 0$:



$$
\frac{1}{1 + r\Delta t} = e^{-r\Delta t} \approx 1 - r\Delta t + O($\Delta t$^2)
$$



The discrete recursion becomes:



$$
V_i \approx V_{i+1} - r\Delta t \cdot V_i + \text{(variance term)}
$$



Rearranging:



$$
\frac{V_{i+1} - V_i}{\Delta t} \approx rV_i - \text{(second derivative terms)}
$$



### **PDE Limit**

As $n \to \infty$ and $\Delta t \to 0$, this discrete recursion converges to the **Black-Scholes PDE**:



$$
\boxed{\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0}
$$



with terminal condition:



$$
V(S, T) = \text{Payoff}(S)
$$



### **Formula Convergence**

For a European call option, the binomial price:



$$
C_{\text{binomial}} = e^{-rT}\sum_{k=0}^n \binom{n}{k} q^k (1-q)^{n-k} $S_0 u^k d^{n-k} - K$^+
$$



converges to the Black-Scholes formula:



$$
C_{\text{BS}} = S_0 \mathcal{N}$d_1$ - Ke^{-rT}\mathcal{N}$d_2$
$$



as $n \to \infty$.

**Proof idea**: The binomial sum is a discrete approximation to the integral:



$$
\mathbb{E}^{\mathbb{Q}}[$S_T - K$^+] = \int_0^\infty (S - K)^+ f(S) dS
$$



where $f(S)$ is the log-normal density.

---

## 6. Replication Argument Carries Over

### **Discrete-Time Hedging**

In the binomial model, at each node the option is replicated by a portfolio:



$$
V_i = \Delta_i S_i + B_i
$$



where:

- $\Delta_i = \frac{V_{i+1}^{\text{up}} - V_{i+1}^{\text{down}}}{S_i(u - d)}$ (delta)

- $B_i$ = cash position

### **Continuous-Time Limit**

As $\Delta t \to 0$:



$$
\Delta_i \to \frac{\partial V}{\partial S}
$$



The discrete hedging strategy converges to the **continuous delta hedging** in Black-Scholes:



$$
\Delta(S,t) = \frac{\partial V}{\partial S} = \mathcal{N}$d_1$
$$



**Self-financing**: The portfolio remains self-financing in the limit, meaning no additional cash is injected or withdrawn.

---

## 7. Convergence Rate

### **Error Analysis**

The error between binomial and Black-Scholes prices is:



$$
|C_{\text{binomial}} - C_{\text{BS}}| = O\left$\frac{1}{\sqrt{n}}\right$
$$



**Implication**: To achieve 3 decimal places of accuracy, approximately $n \geq 10^6$ steps may be required.

### **Practical Considerations**

For practical implementations:

- **Small $n$** $e.g., $n = 50-100

$$
: Fast computation, reasonable accuracy for ATM options

- **Large $n$** $e.g., $n = 1000+
$$

: Higher accuracy but computationally expensive

- **Richardson extrapolation**: Can improve convergence rate to $O(1/n)$

---

## 8. Extensions and Generalizations

### **American Options**

The binomial method extends naturally to American options (with early exercise):



$$
V_i^{\text{American}} = \max\left(\text{Payoff}$S_i$, e^{-r\Delta t}[qV_{i+1}^{\text{up}} + (1-q)V_{i+1}^{\text{down}}]\right)
$$



There is **no closed-form** Black-Scholes formula for American options, so numerical methods remain essential.

### **Dividends**

For dividend-paying stocks:

- **Continuous dividends**: Replace $r$ with $r - \delta$ in the drift

- **Discrete dividends**: Subtract PV of dividends from stock price at each ex-dividend date

### **Alternative Parameterizations**

Other choices of $u, d$ exist:

- **Cox-Ross-Rubinstein**: $u = e^{\sigma\sqrt{\Delta t}}$, $d = 1/u$

- **Jarrow-Rudd**: $u = e^{$r - \sigma^2/2$\Delta t + \sigma\sqrt{\Delta t}}$, $d = e^{$r - \sigma^2/2$\Delta t - \sigma\sqrt{\Delta t}}$

All converge to the same Black-Scholes limit but may have different convergence rates.

---

## 9. Summary: Binomial vs. Black-Scholes

| Feature | Binomial Model | Black-Scholes Model |
|---------|----------------|---------------------|
| **Time** | Discrete (finite steps) | Continuous |
| **Price moves** | $u$ or $d$ per step | Infinitesimal $dW_t$ |
| **Probability** | Risk-neutral $q$ | Measure $\mathbb{Q}$ |
| **Valuation** | Backward recursion | PDE or expectation |
| **Formula** | Summation over paths | Closed-form (European) |
| **Convergence** | $n \to \infty$ | Limit as $\Delta t \to 0$ |
| **American options** | Easily handled | No closed form |
| **Intuition** | Very clear | Requires SDE theory |
| **Computation** | $O$n^2$$ | Instant (if closed form) |

---

## 10. Practical Takeaway

The binomial tree remains **highly valuable** even after learning the Black-Scholes formula:

### **Advantages of Binomial**

1. **Intuitive**: Easy to understand and explain to non-quants
2. **Flexible**: Handles American options, dividends, time-varying parameters
3. **Robust**: Works even when Black-Scholes assumptions fail
4. **Pedagogical**: Teaches replication and risk-neutral pricing clearly

### **When to Use Each**

- **Black-Scholes**: European options, quick calculations, theoretical analysis

- **Binomial**: American options, exotic features, educational purposes, quick prototyping

### **Complementary Roles**

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
