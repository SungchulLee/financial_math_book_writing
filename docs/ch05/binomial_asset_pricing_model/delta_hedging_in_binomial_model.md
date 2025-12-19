# Delta Hedging in the Binomial Model

**Delta hedging** is a dynamic strategy where an option writer continuously adjusts their position in the underlying stock to neutralize the option's price sensitivity. This section reveals that delta hedging and replication are two perspectives on the same mathematical object, and demonstrates how the binomial model implements this strategy through backward induction.

---

## 1. Delta: Definition and Computation

### **Continuous-Time Definition**

The **delta** of an option is the partial derivative of the option price with respect to the stock price:

$$
\Delta_t = \frac{\partial V_t}{\partial S_t}
$$



This measures the **local sensitivity**: how much the option value changes for a small change in the stock price.

### **Binomial Approximation**

In the binomial model, delta is approximated by a **finite difference** at each node. At time $t$, given next-period values $V_{t+1}^u$ (up state) and $V_{t+1}^d$ (down state):


$$
\boxed{\Delta_t = \frac{V_{t+1}^u - V_{t+1}^d}{S_t u - S_t d} = \frac{V_{t+1}^u - V_{t+1}^d}{(u-d)S_t}}
$$



**Interpretation**: This is the slope of the option value as a function of stock price over the next period.

---

## 2. Two Interpretations of the Same Formula

The replicating portfolio formula

$$
V_t = \Delta_t S_t + \beta_t B_t
$$


admits two complementary interpretations.

### **Interpretation 1: Static Replication (Pricing)**

> At each node, the option value **equals** a portfolio of $\Delta_t$ shares and $\beta_t$ bonds.

**Purpose**: **Pricing** via law of one price
- Given $V_{t+1}^u$ and $V_{t+1}^d$, solve for $(\Delta_t, \beta_t)$ that replicates the payoff
- The option price is then $V_t = \Delta_t S_t + \beta_t$
- This is the **backward induction** valuation step

### **Interpretation 2: Dynamic Hedging (Risk Management)**

> The position $\Delta_t$ in the stock **hedges** the option's risk over the next time step.

Rearranging:

$$
\underbrace{V_t - \Delta_t S_t}_{\text{hedged portfolio}} = \beta_t
$$



**Purpose**: **Hedging** via delta neutrality
- An option writer (short the option) holds $+\Delta_t$ shares to offset price risk
- The residual value $V_t - \Delta_t S_t$ is **risk-free** over $[t, t+1]$
- As the stock moves, $\Delta_t$ must be **rebalanced** (dynamic strategy)

### **Unified View**

| Aspect | Replication View | Hedging View |
|--------|-----------------|--------------|
| **Equation** | $V_t = \Delta_t S_t + \beta_t$ | $V_t - \Delta_t S_t = \beta_t$ |
| **Question** | What is $V_t$? | How to neutralize risk? |
| **Focus** | Pricing (no-arbitrage) | Risk management (delta neutrality) |
| **Time** | Instantaneous identity | Dynamic adjustment over $\Delta t$ |
| **Theory** | Law of one price | Martingale property of hedged portfolio |

**Key insight**: These are not different strategies—they are different perspectives on the **same self-financing portfolio**.

---

## 3. Delta Hedging Algorithm

### **Setup**

An option writer has **sold** an option with value $V_t$. To hedge the short position, they must:
1. Hold $\Delta_t$ shares of stock
2. Hold $\beta_t$ in the risk-free account

This ensures the portfolio value matches the option liability at $t+1$ in both states.

### **Backward Induction with Delta**

**Step 1** (Terminal condition): At expiration $t=N$,

$$
V_N(j) = h(S_N(j))
$$



Delta is undefined (no future rebalancing).

**Step 2** (Backward recursion): For $t = N-1, N-2, \ldots, 0$, at each node:

1. **Compute option values** at $t+1$:
   - Up state: $V_{t+1}^u$
   - Down state: $V_{t+1}^d$

2. **Calculate delta**:

   $$
   \Delta_t = \frac{V_{t+1}^u - V_{t+1}^d}{(u-d)S_t}
   $$



3. **Calculate bond position**:

   $$
   \beta_t = \frac{1}{1+r}\left[V_{t+1}^u - \Delta_t \cdot uS_t\right] = \frac{1}{1+r}\left[V_{t+1}^d - \Delta_t \cdot dS_t\right]
   $$



4. **Determine option value**:

   $$
   V_t = \Delta_t S_t + \beta_t
   $$


   
   This equals the risk-neutral expectation:

   $$
   V_t = \frac{1}{1+r}\left[qV_{t+1}^u + (1-q)V_{t+1}^d\right]
   $$



**Step 3**: The initial hedge is $(\Delta_0, \beta_0)$.

---

## 4. Numerical Example: Delta Path for a Call

Consider a 2-period call with:

$$
S_0 = 100, \quad u = 1.1, \quad d = 0.95, \quad r = 0.02, \quad K = 105
$$



### **Terminal Payoffs** (t=2)

| State | $S_2$ | $C_2$ |
|-------|-------|-------|
| uu | 121.00 | 16.00 |
| ud | 104.50 | 0.00 |
| dd | 90.25 | 0.00 |

### **Time t=1 Values and Deltas**

**Up node** ($S_1 = 110$):

$$
C_1^u = \frac{1}{1.02}\left[0.4667 \cdot 16 + 0.5333 \cdot 0\right] \approx 7.32
$$




$$
\Delta_1^u = \frac{16 - 0}{(1.1 - 0.95) \cdot 110} = \frac{16}{16.5} \approx 0.970
$$



**Down node** ($S_1 = 95$):

$$
C_1^d = \frac{1}{1.02}\left[0.4667 \cdot 0 + 0.5333 \cdot 0\right] = 0
$$




$$
\Delta_1^d = \frac{0 - 0}{(1.1 - 0.95) \cdot 95} = 0
$$



### **Time t=0 Delta**


$$
C_0 = \frac{1}{1.02}\left[0.4667 \cdot 7.32 + 0.5333 \cdot 0\right] \approx 3.35
$$




$$
\Delta_0 = \frac{7.32 - 0}{(1.1 - 0.95) \cdot 100} = \frac{7.32}{15} \approx 0.488
$$



### **Delta Evolution**

| Time | State | $S_t$ | $C_t$ | $\Delta_t$ | Interpretation |
|------|-------|-------|-------|------------|----------------|
| 0 | - | 100 | 3.35 | 0.488 | Moderate hedge (OTM call) |
| 1 | Up | 110 | 7.32 | 0.970 | Nearly full hedge (near ATM) |
| 1 | Down | 95 | 0.00 | 0.000 | No hedge (deep OTM, worthless) |

**Observations**:
- Delta **increases** as the option moves in-the-money (up path)
- Delta **decreases** toward zero as the option moves out-of-the-money (down path)
- Deep ITM calls have $\Delta \to 1$ (behave like stock)
- Deep OTM calls have $\Delta \to 0$ (behave like zero)

---

## 5. Self-Financing Property

A key property: the delta hedge is **self-financing** in the binomial model.

### **Definition**

A portfolio is self-financing if changes in value come only from asset returns, not from external cash injections:

$$
V_{t+1} - V_t = \Delta_t(S_{t+1} - S_t) + \beta_t\left[(1+r) - 1\right]
$$



### **Verification**

By construction:

$$
V_{t+1} = \Delta_t S_{t+1} + \beta_t(1+r)
$$




$$
V_t = \Delta_t S_t + \beta_t
$$



Subtracting:

$$
V_{t+1} - V_t = \Delta_t(S_{t+1} - S_t) + \beta_t \cdot r
$$



This confirms no external cash flow is needed to maintain the hedge—the portfolio **self-finances** through stock gains and interest accrual.

---

## 6. Gamma and Higher-Order Greeks

### **Gamma Definition**

**Gamma** measures the **curvature** of the option value—how delta changes with the stock price:

$$
\Gamma_t = \frac{\partial^2 V_t}{\partial S_t^2} = \frac{\partial \Delta_t}{\partial S_t}
$$



### **Binomial Approximation**

At time $t$, using deltas from $t+1$:

$$
\Gamma_t \approx \frac{\Delta_{t+1}^u - \Delta_{t+1}^d}{S_{t+1}^u - S_{t+1}^d} \cdot \frac{2}{S_t(u+d)}
$$



In our example at $t=0$:

$$
\Gamma_0 \approx \frac{0.970 - 0.000}{110 - 95} \cdot \frac{2}{100 \cdot 2.05} \approx 0.0316
$$



### **Interpretation**

- High gamma: Delta changes rapidly (need frequent rebalancing)
- Low gamma: Delta stable (less frequent rebalancing)
- ATM options have highest gamma
- Deep ITM/OTM options have low gamma

### **Other Greeks**

**Theta** (time decay):

$$
\Theta_t \approx -\frac{V_t - V_{t-1}}{\Delta t}
$$



**Vega** (volatility sensitivity): Not directly computable in binomial model with fixed $u, d$, but can be estimated by perturbing $\sigma$ and recomputing.

---

## 7. Continuous Limit and Black-Scholes Delta

As $N \to \infty$ with $\Delta t = T/N \to 0$, the binomial delta converges to the **Black-Scholes delta**.

### **European Call**


$$
\boxed{\Delta_{\text{call}}(t, S_t) = \mathcal{N}(d_1)}
$$



where

$$
d_1 = \frac{\ln(S_t/K) + (r + \frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}
$$



and $\mathcal{N}(\cdot)$ is the standard normal CDF.

### **European Put**


$$
\boxed{\Delta_{\text{put}}(t, S_t) = \mathcal{N}(d_1) - 1 = -\mathcal{N}(-d_1)}
$$



### **Convergence**

The binomial finite difference

$$
\Delta_t^{\text{binom}} = \frac{V_{t+1}^u - V_{t+1}^d}{(u-d)S_t}
$$



converges to the continuous derivative

$$
\lim_{\Delta t \to 0} \Delta_t^{\text{binom}} = \frac{\partial V}{\partial S} = \Delta^{\text{BS}}
$$



This justifies interpreting the binomial replicating portfolio as a discrete-time approximation to **continuous delta hedging** in the Black-Scholes framework.

---

## 8. Practical Considerations

### **Discrete Rebalancing**

In practice, delta hedging faces:
- **Transaction costs**: Each rebalance incurs fees
- **Discrete time**: Cannot rebalance continuously
- **Model error**: True $u, d, r$ unknown

**Trade-off**: More frequent rebalancing → better hedge, higher costs

### **Delta-Gamma Hedging**

To reduce rebalancing frequency, use a portfolio that matches both delta and gamma:
- Hold $\Delta$ shares of stock (delta hedge)
- Hold $\Gamma$ units of another option (gamma hedge)

This provides a better local approximation to the option payoff.

### **Binomial as Practical Tool**

The binomial model:
- Provides explicit rebalancing points
- Allows computation of all Greeks numerically
- Handles early exercise (American options) naturally
- Serves as a **discrete-time implementation** of continuous hedging

---

## Summary

Delta hedging in the binomial model reveals the deep connection between pricing and risk management:

1. **Delta** is the replicating portfolio's stock position: $\Delta_t = \frac{V_{t+1}^u - V_{t+1}^d}{(u-d)S_t}$

2. **Two perspectives**:
   - **Pricing**: The option equals a portfolio $(\Delta_t, \beta_t)$ (law of one price)
   - **Hedging**: The position $\Delta_t$ neutralizes risk over $[t, t+1]$ (delta neutrality)

3. **Dynamic strategy**: Delta changes as the stock moves through the tree—must rebalance at each node

4. **Self-financing**: No external cash needed; portfolio adjusts through asset returns

5. **Convergence**: As $\Delta t \to 0$, binomial delta → Black-Scholes delta

The binomial model provides a finite, algebraic framework for understanding continuous-time delta hedging before confronting stochastic calculus.
