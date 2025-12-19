# Multi-Period Option Pricing

The one-period model reveals the fundamental pricing logic, but realistic option pricing requires extending to multiple time steps. The key algorithmic tool is **backward induction**, which recursively applies one-period pricing from expiration back to the present.

---

## 1. Multi-Period Market Model

### **Time Structure**

Consider a binomial tree with $N$ periods: $t = 0, 1, 2, \ldots, N$.

- **Risk-free asset**: $B_t = (1+r)^t$
- **Stock price**: At each node, $S_{t+1} \in \{uS_t, dS_t\}$

### **Tree Structure**

Starting from $S_0$, the stock price at time $t$ can reach $2^t$ potential values (before recombination). With a **recombining tree** (where up-then-down = down-then-up), we have:

At time $t$, after $j$ up-moves (and $t-j$ down-moves):

$$
S_t(j) = u^j d^{t-j} S_0, \quad j = 0, 1, \ldots, t
$$



### **Risk-Neutral Dynamics**

Under the risk-neutral measure $\mathbb{Q}$:

- At each node, $\mathbb{Q}(\text{up}) = q$, $\mathbb{Q}(\text{down}) = 1-q$
- where $q = \frac{1+r-d}{u-d}$ (same as one-period)
- Transitions are independent across periods

The number of paths to state $j$ at time $t$ is $\binom{t}{j}$.

---

## 2. European Option Pricing

### **Backward Induction Algorithm**

For a European option with payoff $H_N = h(S_N)$ at expiration:

**Step 1** (Terminal payoff): At $t=N$,

$$
V_N(j) = h(S_N(j)) = h(u^j d^{N-j} S_0)
$$



**Step 2** (Backward recursion): For $t = N-1, N-2, \ldots, 0$,

$$
\boxed{V_t(j) = \frac{1}{1+r}\left[q V_{t+1}(j+1) + (1-q)V_{t+1}(j)\right]}
$$



where:
- $V_{t+1}(j+1)$ is the value one period later in the "up" state
- $V_{t+1}(j)$ is the value one period later in the "down" state

**Step 3** (Initial value): The option price is $V_0 = V_0(0)$.

### **Interpretation**

Each step applies the one-period risk-neutral pricing formula:

$$
V_t = \frac{1}{1+r}\mathbb{E}_t^{\mathbb{Q}}[V_{t+1}]
$$



This is the **martingale property** of discounted option values.

### **Closed-Form Solution**

The backward recursion can be "unrolled" to give:

$$
\boxed{V_0 = \frac{1}{(1+r)^N}\sum_{j=0}^{N}\binom{N}{j}q^j(1-q)^{N-j}h(u^j d^{N-j}S_0)}
$$



This is a **risk-neutral expectation** over all terminal paths.

---

## 3. European Call Example

Consider a 3-period model with:

$$
S_0 = 100, \quad u = 1.1, \quad d = 0.95, \quad r = 0.02, \quad K = 105, \quad N = 3
$$



**Step 1**: Risk-neutral probability

$$
q = \frac{1.02 - 0.95}{1.1 - 0.95} = \frac{0.07}{0.15} \approx 0.4667
$$



**Step 2**: Terminal stock prices and call payoffs

| $j$ | $S_3(j)$ | $C_3(j) = (S_3(j) - 105)^+$ |
|-----|----------|------------------------------|
| 0 | $100 \cdot 0.95^3 = 85.74$ | 0 |
| 1 | $100 \cdot 1.1 \cdot 0.95^2 = 99.28$ | 0 |
| 2 | $100 \cdot 1.1^2 \cdot 0.95 = 115.05$ | 10.05 |
| 3 | $100 \cdot 1.1^3 = 133.10$ | 28.10 |

**Step 3**: Backward induction from $t=2$

At $t=2$:

$$
\begin{aligned}
V_2(0) &= \frac{1}{1.02}[0.4667 \cdot 0 + 0.5333 \cdot 0] = 0 \\
V_2(1) &= \frac{1}{1.02}[0.4667 \cdot 0 + 0.5333 \cdot 10.05] \approx 5.26 \\
V_2(2) &= \frac{1}{1.02}[0.4667 \cdot 10.05 + 0.5333 \cdot 28.10] \approx 19.33
\end{aligned}
$$



At $t=1$:

$$
\begin{aligned}
V_1(0) &= \frac{1}{1.02}[0.4667 \cdot 0 + 0.5333 \cdot 5.26] \approx 2.75 \\
V_1(1) &= \frac{1}{1.02}[0.4667 \cdot 5.26 + 0.5333 \cdot 19.33] \approx 12.52
\end{aligned}
$$



At $t=0$:

$$
C_0 = V_0 = \frac{1}{1.02}[0.4667 \cdot 2.75 + 0.5333 \cdot 12.52] \approx 7.81
$$



**Alternative**: Direct formula

$$
\begin{aligned}
C_0 &= \frac{1}{1.02^3}\left[\binom{3}{0}(0.4667)^0(0.5333)^3 \cdot 0 + \binom{3}{1}(0.4667)^1(0.5333)^2 \cdot 0 \right. \\
&\quad\left. + \binom{3}{2}(0.4667)^2(0.5333)^1 \cdot 10.05 + \binom{3}{3}(0.4667)^3(0.5333)^0 \cdot 28.10\right] \\
&= \frac{1}{1.0612}\left[3 \cdot 0.2178 \cdot 0.5333 \cdot 10.05 + 1 \cdot 0.1016 \cdot 28.10\right] \\
&\approx 7.81 \quad \checkmark
\end{aligned}
$$



---

## 4. American Options and Early Exercise

### **Key Difference**

An **American option** can be exercised at any time $t \leq N$, not just at expiration. The holder must decide at each node whether to:

- **Exercise immediately**: Receive intrinsic value $h(S_t)$
- **Hold**: Retain continuation value $V_t^{\text{hold}}$

### **Modified Backward Induction**

**Step 1** (Terminal condition): Same as European

$$
V_N^{\text{Am}}(j) = h(S_N(j))
$$



**Step 2** (Backward recursion with exercise decision): For $t = N-1, \ldots, 0$,

$$
V_t^{\text{hold}}(j) = \frac{1}{1+r}\left[q V_{t+1}^{\text{Am}}(j+1) + (1-q)V_{t+1}^{\text{Am}}(j)\right]
$$




$$
\boxed{V_t^{\text{Am}}(j) = \max\left\{h(S_t(j)), V_t^{\text{hold}}(j)\right\}}
$$



**Interpretation**: At each node, choose the maximum of:
- **Immediate exercise value**: $h(S_t(j))$
- **Continuation value**: Discounted expected value of holding

### **Early Exercise Region**

Define the **early exercise region** as:

$$
\mathcal{E} = \{(t,j) : h(S_t(j)) > V_t^{\text{hold}}(j)\}
$$



At nodes in $\mathcal{E}$, immediate exercise is optimal.

---

## 5. American Put Example

Consider the same parameters as before, but price an American put with $K = 105$.

**Terminal payoffs** at $t=3$:

| $j$ | $S_3(j)$ | $P_3(j) = (105 - S_3(j))^+$ |
|-----|----------|------------------------------|
| 0 | 85.74 | 19.26 |
| 1 | 99.28 | 5.72 |
| 2 | 115.05 | 0 |
| 3 | 133.10 | 0 |

**Backward induction** from $t=2$:

At $t=2$, stock prices: $S_2(0) = 90.25$, $S_2(1) = 104.50$, $S_2(2) = 121.00$

Intrinsic values: $h(S_2(0)) = 14.75$, $h(S_2(1)) = 0.50$, $h(S_2(2)) = 0$

Continuation values:

$$
\begin{aligned}
V_2^{\text{hold}}(0) &= \frac{1}{1.02}[0.4667 \cdot 19.26 + 0.5333 \cdot 5.72] \approx 11.78 \\
V_2^{\text{hold}}(1) &= \frac{1}{1.02}[0.4667 \cdot 5.72 + 0.5333 \cdot 0] \approx 2.62 \\
V_2^{\text{hold}}(2) &= \frac{1}{1.02}[0.4667 \cdot 0 + 0.5333 \cdot 0] = 0
\end{aligned}
$$



**Exercise decisions**:

$$
\begin{aligned}
V_2^{\text{Am}}(0) &= \max\{14.75, 11.78\} = 14.75 \quad \text{(exercise)} \\
V_2^{\text{Am}}(1) &= \max\{0.50, 2.62\} = 2.62 \quad \text{(hold)} \\
V_2^{\text{Am}}(2) &= \max\{0, 0\} = 0
\end{aligned}
$$



At $t=1$, stock prices: $S_1(0) = 95.00$, $S_1(1) = 110.00$

Intrinsic values: $h(S_1(0)) = 10.00$, $h(S_1(1)) = 0$

Continuation values:

$$
\begin{aligned}
V_1^{\text{hold}}(0) &= \frac{1}{1.02}[0.4667 \cdot 14.75 + 0.5333 \cdot 2.62] \approx 8.04 \\
V_1^{\text{hold}}(1) &= \frac{1}{1.02}[0.4667 \cdot 2.62 + 0.5333 \cdot 0] \approx 1.20
\end{aligned}
$$



**Exercise decisions**:

$$
\begin{aligned}
V_1^{\text{Am}}(0) &= \max\{10.00, 8.04\} = 10.00 \quad \text{(exercise)} \\
V_1^{\text{Am}}(1) &= \max\{0, 1.20\} = 1.20 \quad \text{(hold)}
\end{aligned}
$$



At $t=0$:

Intrinsic value: $h(S_0) = (105 - 100)^+ = 5.00$

Continuation value:

$$
V_0^{\text{hold}} = \frac{1}{1.02}[0.4667 \cdot 10.00 + 0.5333 \cdot 1.20] \approx 5.20
$$



**Final decision**:

$$
P_0^{\text{Am}} = \max\{5.00, 5.20\} = 5.20 \quad \text{(hold)}
$$



### **Comparison with European Put**

For the European put, we would compute:

$$
P_0^{\text{Eu}} = \frac{1}{1.02^3}\sum_{j=0}^3 \binom{3}{j}q^j(1-q)^{N-j}(105 - S_3(j))^+ \approx 4.89
$$



The **early exercise premium** is:

$$
P_0^{\text{Am}} - P_0^{\text{Eu}} = 5.20 - 4.89 = 0.31
$$



This premium compensates for the flexibility to exercise early when the put is deep in-the-money.

---

## 6. Optimal Exercise Boundary

For American puts, the **optimal exercise boundary** is the critical stock price $S_t^*$ at each time $t$ below which exercise is optimal:

$$
S_t^* = \sup\{S : (K-S)^+ > V_t^{\text{hold}}(S)\}
$$



**Characteristics**:

1. $S_t^* < K$ (exercise only when in-the-money)
2. $S_t^*$ is decreasing in $t$ (boundary moves up as expiration approaches)
3. At expiration, $S_N^* = K$ (exercise if and only if $S_N < K$)

In our example at $t=2$:
- Exercise at $S_2(0) = 90.25 < S_2^*$
- Hold at $S_2(1) = 104.50 > S_2^*$

This implies $90.25 < S_2^* < 104.50$.

---

## 7. Computational Complexity

### **European Options**

- **Backward induction**: $O(N^2)$ operations (visit each node once)
- **Closed-form formula**: $O(2^N)$ terms, but dominated by $O(N^2)$ using dynamic programming

### **American Options**

- **Backward induction**: $O(N^2)$ operations (same tree traversal, but with max comparison)
- **No closed form**: Must use backward induction due to path-dependent exercise decisions

### **Storage**

For a recombining tree:
- Need to store values at all nodes: $\sum_{t=0}^N (t+1) = O(N^2)$ space
- Can optimize to $O(N)$ by storing only two consecutive time slices

---

## 8. Convergence and Accuracy

As $N \to \infty$ (with appropriate time-step scaling), the binomial model converges to continuous-time models:

- **European options**: Converge to Black-Scholes formula
- **American options**: Converge to solutions of the **free boundary problem**

The convergence rate is typically $O(N^{-1/2})$, which can be improved to $O(N^{-1})$ with Richardson extrapolation.

---

## 9. Greeks via Finite Differences

The binomial tree allows numerical computation of option sensitivities (**Greeks**):

### **Delta** (price sensitivity to stock price)

$$
\Delta_1 = \frac{V_1(1) - V_1(0)}{S_1(1) - S_1(0)}
$$



### **Gamma** (convexity)

$$
\Gamma_2 = \frac{\Delta_2(1) - \Delta_2(0)}{0.5(S_2(2) - S_2(0))}
$$



where

$$
\Delta_2(1) = \frac{V_2(2) - V_2(1)}{S_2(2) - S_2(1)}, \quad \Delta_2(0) = \frac{V_2(1) - V_2(0)}{S_2(1) - S_2(0)}
$$



### **Theta** (time decay)

$$
\Theta = -\frac{V_1(0) - V_0}{\Delta t}
$$



where $\Delta t$ is the time step.

---

## 10. Extensions

The backward induction framework extends to:

1. **Dividends**: Reduce stock price by dividend amount at ex-dividend nodes
2. **Barrier options**: Check knock-in/knock-out conditions at each node
3. **Exotic payoffs**: Path-dependent claims require tracking additional state variables
4. **Trinomial trees**: Three branches (up, middle, down) per node for better convergence
5. **Variable parameters**: Time-dependent $r$, $\sigma$ (through $u, d$)

---

## Summary

Multi-period option pricing via backward induction:

1. **European options**: Simple recursive application of risk-neutral discounting

   $$
   V_t = \frac{1}{1+r}[qV_{t+1}^u + (1-q)V_{t+1}^d]
   $$



2. **American options**: Add early exercise comparison at each node

   $$
   V_t^{\text{Am}} = \max\{h(S_t), \frac{1}{1+r}[qV_{t+1}^{u,\text{Am}} + (1-q)V_{t+1}^{d,\text{Am}}]\}
   $$



3. **Computational efficiency**: $O(N^2)$ algorithm enables rapid pricing for moderate $N$

4. **Convergence**: As $N \to \infty$, recover continuous-time pricing formulas

The backward induction algorithm is the computational workhorse of binomial option pricing and generalizes to any claim that can be valued by no-arbitrage.
