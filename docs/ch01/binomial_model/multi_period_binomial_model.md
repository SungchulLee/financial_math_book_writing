# Multi-Period Binomial Model

## Introduction

This section extends the one-period binomial model to **multiple time periods**. The multi-period framework enables:

- **Realistic option pricing**: Options with arbitrary maturities
- **Dynamic delta hedging**: Rebalancing the hedge as the stock evolves
- **American options**: Early exercise decisions at each node
- **Path to continuous time**: Foundation for Black–Scholes convergence

The key insight is that multi-period pricing reduces to **repeated application** of one-period pricing via **backward induction**.

!!! info "Prerequisites"
    - [Binomial Model](binomial_model.md) (one-period setup)
    - [Replicating Portfolio](replicating_portfolio.md) (replication approach)
    - [Delta Hedging](delta_hedging.md) (hedging approach)
    - [Risk-Neutral Measure](risk_neutral_measure.md) (expectation pricing)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Construct a multi-period binomial tree
    2. Price European options via backward induction
    3. Implement dynamic delta hedging through the tree
    4. Price American options with early exercise
    5. Understand the self-financing property

---

## The Multi-Period Tree

### Time Structure

Fix a maturity $T$ and divide it into $N$ equal periods:

$$
\Delta t = \frac{T}{N}
$$

Time points: $t_n = n \cdot \Delta t$ for $n = 0, 1, \ldots, N$.

### Node Indexing

Each node is indexed by $(n, j)$ where:

- $n = 0, 1, \ldots, N$ is the **time index**
- $j = 0, 1, \ldots, n$ is the **state index** (number of up moves)

### Stock Prices

At node $(n, j)$, the stock price is:

$$
\boxed{S_{n,j} = S_0 \cdot u^j \cdot d^{n-j}}
$$

### The Recombining Property

With $u = e^{\sigma\sqrt{\Delta t}}$ and $d = e^{-\sigma\sqrt{\Delta t}} = 1/u$:

$$
ud = 1
$$

An up-then-down path reaches the same price as a down-then-up path. The tree **recombines**, giving only $n+1$ nodes at time $n$ (not $2^n$).

### Tree Visualization ($N = 3$)

```
Time:     0           1           2           3
                                            S_{3,3} = u³S₀
                            S_{2,2} = u²S₀
                S_{1,1} = uS₀               S_{3,2} = u²dS₀ = uS₀
    S_{0,0} = S₀            S_{2,1} = udS₀ = S₀
                S_{1,0} = dS₀               S_{3,1} = ud²S₀ = dS₀
                            S_{2,0} = d²S₀
                                            S_{3,0} = d³S₀
```

### Computational Advantage

| Tree Type | Nodes at Time $n$ | Total Nodes |
|-----------|-------------------|-------------|
| Recombining | $n + 1$ | $O(N^2)$ |
| Non-recombining | $2^n$ | $O(2^N)$ |

---

## Backward Induction for European Options

### The Algorithm

**Step 1: Terminal condition** ($n = N$)

Set option values equal to payoffs:
$$
V_{N,j} = H(S_{N,j})
$$

**Step 2: Backward recursion** ($n = N-1, N-2, \ldots, 0$)

At each node $(n, j)$, the option value is the discounted risk-neutral expectation:

$$
\boxed{V_{n,j} = e^{-r\Delta t}\left[qV_{n+1,j+1} + (1-q)V_{n+1,j}\right]}
$$

where $q = \frac{e^{r\Delta t} - d}{u - d}$.

**Step 3: Output**

The option price is $V_{0,0}$.

### Why Backward Induction Works

At each node, we apply the one-period pricing formula. The option at node $(n,j)$ is a one-period claim with:
- Up-state payoff: $V_{n+1,j+1}$
- Down-state payoff: $V_{n+1,j}$

By risk-neutral pricing:
$$
V_{n,j} = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[V_{n+1} | \text{at node } (n,j)]
$$

---

## Dynamic Delta Hedging

### The Hedging Strategy

At each node $(n, j)$, we construct a **locally replicating portfolio**:

- Hold $\Delta_{n,j}$ shares of stock
- Hold $B_{n,j}$ units of bond (cash)

The portfolio replicates the option over the next period.

### Computing Delta at Each Node

From the one-period hedging formula:

$$
\boxed{\Delta_{n,j} = \frac{V_{n+1,j+1} - V_{n+1,j}}{S_{n,j}(u - d)}}
$$

This is the **local hedge ratio**—the number of shares to hold at node $(n,j)$.

### Computing the Cash Position

$$
\boxed{B_{n,j} = e^{-r\Delta t}\left(V_{n+1,j+1} - \Delta_{n,j} \cdot uS_{n,j}\right)}
$$

Or equivalently:
$$
B_{n,j} = V_{n,j} - \Delta_{n,j} \cdot S_{n,j}
$$

### The Rebalancing Process

1. **At $t = 0$**: Enter position $(\Delta_{0,0}, B_{0,0})$
2. **At $t = \Delta t$**: Stock has moved to state $j$
   - Old portfolio value: $\Delta_{0,0} \cdot S_{1,j} + B_{0,0} \cdot e^{r\Delta t}$
   - This equals $V_{1,j}$ (by construction)
   - **Rebalance** to new position $(\Delta_{1,j}, B_{1,j})$
3. **Repeat** at each time step until maturity

### Self-Financing Property

The rebalancing requires **no external cash**. The value of the old portfolio exactly equals the cost of the new portfolio:

$$
\Delta_{n-1,k} \cdot S_{n,j} + B_{n-1,k} \cdot e^{r\Delta t} = V_{n,j} = \Delta_{n,j} \cdot S_{n,j} + B_{n,j}
$$

This is the **self-financing property**—the hedging strategy is implementable without adding or withdrawing funds.

---

## Complete Numerical Example

### Parameters

| Parameter | Value |
|-----------|-------|
| $S_0$ | $100$ |
| $K$ | $100$ |
| $r$ | $5\%$ per year |
| $\sigma$ | $20\%$ per year |
| $T$ | $1$ year |
| $N$ | $3$ periods |

### Computed Values

$$
\Delta t = \frac{1}{3}, \quad u = e^{0.2\sqrt{1/3}} = 1.1224, \quad d = \frac{1}{u} = 0.8909
$$

$$
e^{r\Delta t} = e^{0.05/3} = 1.0168, \quad q = \frac{1.0168 - 0.8909}{1.1224 - 0.8909} = 0.5439
$$

### Stock Price Tree

| Node | Price |
|------|-------|
| $S_{0,0}$ | $100.00$ |
| $S_{1,1}$ | $112.24$ |
| $S_{1,0}$ | $89.09$ |
| $S_{2,2}$ | $125.98$ |
| $S_{2,1}$ | $100.00$ |
| $S_{2,0}$ | $79.37$ |
| $S_{3,3}$ | $141.40$ |
| $S_{3,2}$ | $112.24$ |
| $S_{3,1}$ | $89.09$ |
| $S_{3,0}$ | $70.72$ |

### Option Values (European Call, $K = 100$)

**Terminal payoffs** ($n = 3$):
$$
V_{3,3} = 41.40, \quad V_{3,2} = 12.24, \quad V_{3,1} = 0, \quad V_{3,0} = 0
$$

**At $n = 2$**:
$$
V_{2,2} = e^{-0.0167}[0.5439 \times 41.40 + 0.4561 \times 12.24] = 0.9835 \times 28.10 = 27.63
$$
$$
V_{2,1} = e^{-0.0167}[0.5439 \times 12.24 + 0.4561 \times 0] = 0.9835 \times 6.66 = 6.55
$$
$$
V_{2,0} = e^{-0.0167}[0.5439 \times 0 + 0.4561 \times 0] = 0
$$

**At $n = 1$**:
$$
V_{1,1} = e^{-0.0167}[0.5439 \times 27.63 + 0.4561 \times 6.55] = 0.9835 \times 18.02 = 17.72
$$
$$
V_{1,0} = e^{-0.0167}[0.5439 \times 6.55 + 0.4561 \times 0] = 0.9835 \times 3.56 = 3.50
$$

**At $n = 0$**:
$$
V_{0,0} = e^{-0.0167}[0.5439 \times 17.72 + 0.4561 \times 3.50] = 0.9835 \times 11.23 = 11.04
$$

!!! success "European Call Price"
    $$C_0 = 11.04$$

### Delta at Each Node

$$
\Delta_{2,2} = \frac{41.40 - 12.24}{125.98 \times 0.2315} = \frac{29.16}{29.16} = 1.00
$$

$$
\Delta_{2,1} = \frac{12.24 - 0}{100 \times 0.2315} = \frac{12.24}{23.15} = 0.529
$$

$$
\Delta_{2,0} = \frac{0 - 0}{79.37 \times 0.2315} = 0
$$

$$
\Delta_{1,1} = \frac{27.63 - 6.55}{112.24 \times 0.2315} = \frac{21.08}{25.98} = 0.812
$$

$$
\Delta_{1,0} = \frac{6.55 - 0}{89.09 \times 0.2315} = \frac{6.55}{20.62} = 0.318
$$

$$
\Delta_{0,0} = \frac{17.72 - 3.50}{100 \times 0.2315} = \frac{14.22}{23.15} = 0.614
$$

### Delta Hedging Through the Tree

**Initial position** ($t = 0$):
- Hold $\Delta_{0,0} = 0.614$ shares: cost $61.40$
- Borrow $B_{0,0} = 11.04 - 61.40 = -50.36$
- Portfolio value: $11.04$ = option price ✓

**After up move** ($t = \Delta t$, stock at $112.24$):
- Stock position: $0.614 \times 112.24 = 68.92$
- Cash position: $-50.36 \times e^{0.0167} = -51.20$
- Portfolio value: $68.92 - 51.20 = 17.72$ = $V_{1,1}$ ✓
- **Rebalance**: Increase to $\Delta_{1,1} = 0.812$ shares
- Buy $0.812 - 0.614 = 0.198$ shares at $112.24$: cost $22.22$
- New cash: $-51.20 - 22.22 = -73.42$

**After down move** ($t = \Delta t$, stock at $89.09$):
- Stock position: $0.614 \times 89.09 = 54.70$
- Cash position: $-50.36 \times e^{0.0167} = -51.20$
- Portfolio value: $54.70 - 51.20 = 3.50$ = $V_{1,0}$ ✓

The hedging strategy **perfectly replicates** the option value at every node.

---

## American Options

### Early Exercise

An **American option** can be exercised at any time up to maturity. At each node, the holder chooses the maximum of:

1. **Exercise value** (intrinsic value): payoff from immediate exercise
2. **Continuation value**: value of holding the option

### Backward Induction for American Options

$$
\boxed{V_{n,j}^{Am} = \max\left(\text{Intrinsic}_{n,j}, \, e^{-r\Delta t}[qV_{n+1,j+1}^{Am} + (1-q)V_{n+1,j}^{Am}]\right)}
$$

**American call**: $\text{Intrinsic}_{n,j} = (S_{n,j} - K)^+$

**American put**: $\text{Intrinsic}_{n,j} = (K - S_{n,j})^+$

### American Put Example

Using the same parameters, price an American put with $K = 100$.

**Terminal payoffs** ($n = 3$):
$$
V_{3,3}^{Am} = 0, \quad V_{3,2}^{Am} = 0, \quad V_{3,1}^{Am} = 10.91, \quad V_{3,0}^{Am} = 29.28
$$

**At $n = 2$**:

$V_{2,2}$: Intrinsic $= (100 - 125.98)^+ = 0$, Continuation $= 0$ → $V_{2,2}^{Am} = 0$

$V_{2,1}$: Intrinsic $= (100 - 100)^+ = 0$, Continuation $= 0.9835[0.5439 \times 0 + 0.4561 \times 10.91] = 4.89$ → $V_{2,1}^{Am} = 4.89$

$V_{2,0}$: Intrinsic $= (100 - 79.37)^+ = 20.63$, Continuation $= 0.9835[0.5439 \times 10.91 + 0.4561 \times 29.28] = 18.96$

$$
V_{2,0}^{Am} = \max(20.63, 18.96) = 20.63 \quad \textbf{(Early exercise optimal!)}
$$

**At $n = 1$**:

$V_{1,1}$: Intrinsic $= 0$, Continuation $= 0.9835[0.5439 \times 0 + 0.4561 \times 4.89] = 2.19$ → $V_{1,1}^{Am} = 2.19$

$V_{1,0}$: Intrinsic $= (100 - 89.09)^+ = 10.91$, Continuation $= 0.9835[0.5439 \times 4.89 + 0.4561 \times 20.63] = 11.87$

$$
V_{1,0}^{Am} = \max(10.91, 11.87) = 11.87 \quad \text{(Hold)}
$$

**At $n = 0$**:

$V_{0,0}$: Intrinsic $= 0$, Continuation $= 0.9835[0.5439 \times 2.19 + 0.4561 \times 11.87] = 6.50$

$$
V_{0,0}^{Am} = 6.50
$$

!!! success "American Put Price"
    $$P_0^{Am} = 6.50$$
    
    The European put price would be approximately $5.57$. The difference $6.50 - 5.57 = 0.93$ is the **early exercise premium**.

### Early Exercise Boundary

The node $(2, 0)$ where $S = 79.37$ shows early exercise is optimal. This defines the **early exercise boundary**—the stock price below which immediate exercise beats holding.

### American Calls on Non-Dividend Stocks

!!! note "No Early Exercise for American Calls"
    For a call on a **non-dividend-paying** stock, early exercise is **never optimal**:
    
    - Exercising gives $S - K$
    - Holding gives at least $S - Ke^{-r(T-t)} > S - K$
    
    The American call equals the European call.

---

## Properties of Multi-Period Delta

### Delta Evolution

As we move through the tree:

- **Stock rises** → Call delta increases (approaches 1)
- **Stock falls** → Call delta decreases (approaches 0)
- **Near expiration** → Delta becomes more extreme (0 or 1)

### Gamma: Rate of Change of Delta

The **gamma** measures how fast delta changes:

$$
\Gamma_{n,j} \approx \frac{\Delta_{n+1,j+1} - \Delta_{n+1,j}}{S_{n+1,j+1} - S_{n+1,j}}
$$

High gamma means more frequent rebalancing is needed.

### Delta at Maturity

At expiration:
$$
\Delta_{N-1,j} = \frac{V_{N,j+1} - V_{N,j}}{S_{N-1,j}(u-d)} = 
\begin{cases}
1 & \text{if both nodes in-the-money} \\
\frac{\text{payoff spread}}{\text{price spread}} & \text{if one node ITM} \\
0 & \text{if both nodes out-of-the-money}
\end{cases}
$$

---

## Algorithm Summary

### European Option Pricing

```
Input: S₀, K, r, σ, T, N, option_type
Output: V₀

1. Δt = T/N, u = exp(σ√Δt), d = 1/u
2. q = (exp(rΔt) - d) / (u - d)
3. For j = 0 to N:
      V[N,j] = payoff(S₀ × uʲ × d^(N-j), K)
4. For n = N-1 down to 0:
      For j = 0 to n:
          V[n,j] = exp(-rΔt) × [q×V[n+1,j+1] + (1-q)×V[n+1,j]]
5. Return V[0,0]
```

### American Option Pricing

Same as European, but step 4 becomes:
```
4. For n = N-1 down to 0:
      For j = 0 to n:
          continuation = exp(-rΔt) × [q×V[n+1,j+1] + (1-q)×V[n+1,j]]
          intrinsic = payoff(S₀ × uʲ × d^(n-j), K)
          V[n,j] = max(intrinsic, continuation)
```

### Memory-Efficient Implementation

Only store one time slice:
```
V = array[N+1]
// Initialize terminal payoffs
For n = N-1 down to 0:
    For j = 0 to n:
        V[j] = exp(-rΔt) × [q×V[j+1] + (1-q)×V[j]]
Return V[0]
```

**Complexity**: $O(N^2)$ time, $O(N)$ space.

---

## Summary

| Concept | Formula |
|---------|---------|
| Stock price at $(n,j)$ | $S_{n,j} = S_0 u^j d^{n-j}$ |
| Risk-neutral probability | $q = \dfrac{e^{r\Delta t} - d}{u-d}$ |
| European backward recursion | $V_{n,j} = e^{-r\Delta t}[qV_{n+1,j+1} + (1-q)V_{n+1,j}]$ |
| American backward recursion | $V_{n,j} = \max(\text{Intrinsic}, \text{Continuation})$ |
| Delta at node | $\Delta_{n,j} = \dfrac{V_{n+1,j+1} - V_{n+1,j}}{S_{n,j}(u-d)}$ |
| Cash position | $B_{n,j} = V_{n,j} - \Delta_{n,j} S_{n,j}$ |

!!! abstract "Key Takeaways"
    1. **Backward induction**: Multi-period pricing reduces to repeated one-period pricing.
    
    2. **Dynamic delta hedging**: The hedge ratio changes at each node and must be rebalanced.
    
    3. **Self-financing**: Rebalancing requires no external cash—the strategy is implementable.
    
    4. **American options**: Compare intrinsic value to continuation value at each node.
    
    5. **Recombining tree**: $O(N^2)$ complexity makes computation tractable.
    
    6. **Convergence**: As $N \to \infty$, the model converges to Black–Scholes.

---

## What's Next

| Section | Topic |
|---------|-------|
| [Binomial to Black–Scholes](binomial_to_black_scholes_limit.md) | Continuous-time limit |
| [FTAP](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md) | General theory of arbitrage-free pricing |
