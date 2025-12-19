# Arrow–Debreu State Price Valuation

Arrow–Debreu state prices provide an alternative pricing framework that complements backward induction. Instead of recursively computing values from terminal nodes backward, state price valuation adopts a **forward-looking perspective**: the option price is a weighted sum of terminal payoffs, where weights are present values of state-contingent claims.

This approach reveals the deep connection between discrete binomial pricing and continuous-time theory, and connects financial mathematics to general equilibrium economics.

---

## 1. Arrow–Debreu Securities

### **Definition**

An **Arrow–Debreu security** (or **pure state-contingent claim**) is a contract that pays:

$$
\text{AD}_j(T) = 
\begin{cases}
1 & \text{if state } j \text{ is realized at time } T \\
0 & \text{otherwise}
\end{cases}
$$



In a binomial tree with $n$ periods, there are $n+1$ possible terminal states, indexed by $j = 0, 1, \ldots, n$, corresponding to the number of up-moves.

### **Economic Interpretation**

Arrow–Debreu securities are the **elementary building blocks** of contingent claims:
- Any European derivative with terminal payoff $V_j$ in state $j$ can be **replicated** as:

  $$
  V(T) = \sum_{j=0}^n V_j \cdot \text{AD}_j(T)
  $$



- The market is **complete** if and only if all Arrow–Debreu securities can be traded (or synthetically constructed)

- In the binomial model, completeness is guaranteed: the two assets (stock and bond) span the two-dimensional state space at each node

---

## 2. State Prices

### **Definition**

The **state price** $\pi_j$ is the present value (price at $t=0$) of an Arrow–Debreu security for terminal state $j$:

$$
\pi_j = \text{Price today of receiving } \$1 \text{ if and only if state } j \text{ occurs at } T
$$



### **Computation in Binomial Model**

For a binomial tree with parameters $(n, u, d, r, q)$:

**Terminal state $j$**: Asset has moved up $j$ times, down $n-j$ times
- Terminal stock price: $S_j = S_0 u^j d^{n-j}$
- Number of paths to state $j$: $\binom{n}{j}$
- Risk-neutral probability of any single path: $q^j(1-q)^{n-j}$
- Risk-neutral probability of state $j$: $\mathbb{Q}(\text{state } j) = \binom{n}{j}q^j(1-q)^{n-j}$

**State price formula**:

$$
\boxed{\pi_j = e^{-rT} \cdot \binom{n}{j} q^j (1-q)^{n-j}}
$$



where:
- $e^{-rT}$ is the discount factor over $T = n\Delta t$
- $q = \frac{e^{r\Delta t} - d}{u - d}$ is the risk-neutral probability (or $q = \frac{1+r-d}{u-d}$ if rates are simple)

**Components**:

$$
\pi_j = \underbrace{e^{-rT}}_{\text{time value}} \times \underbrace{\binom{n}{j}q^j(1-q)^{n-j}}_{\mathbb{Q}(\text{reaching state } j)}
$$



---

## 3. Pricing via State Prices

### **Valuation Formula**

For any European contingent claim with terminal payoffs $\{V_0, V_1, \ldots, V_n\}$:

$$
\boxed{V_0 = \sum_{j=0}^n \pi_j V_j = e^{-rT}\sum_{j=0}^n \binom{n}{j}q^j(1-q)^{n-j} V_j}
$$



This is the **state price representation** of the option value.

### **Interpretation**

The price today is:

$$
V_0 = \sum_{j=0}^n (\text{Cost of state } j) \times (\text{Payoff in state } j)
$$



Equivalently:

$$
V_0 = e^{-rT} \mathbb{E}^{\mathbb{Q}}[V_T]
$$



This is identical to the **risk-neutral expectation formula**, but derived from a state-contingent pricing perspective rather than martingale theory.

---

## 4. Example: 3-Period European Call

Consider:

$$
S_0 = 100, \quad u = 1.1, \quad d = 0.95, \quad r = 0.02, \quad \Delta t = 1, \quad n = 3, \quad K = 105
$$



**Step 1**: Risk-neutral probability

$$
q = \frac{1.02 - 0.95}{1.1 - 0.95} = \frac{0.07}{0.15} \approx 0.4667
$$



**Step 2**: Terminal states and payoffs

| $j$ | $S_j = 100 \cdot 1.1^j \cdot 0.95^{3-j}$ | $C_j = (S_j - 105)^+$ |
|-----|------------------------------------------|------------------------|
| 0 | 85.74 | 0 |
| 1 | 99.28 | 0 |
| 2 | 115.05 | 10.05 |
| 3 | 133.10 | 28.10 |

**Step 3**: State prices

Discount factor: $e^{-rT} = e^{-0.02 \cdot 3} \approx 0.9418$

| $j$ | $\binom{3}{j}$ | $q^j(1-q)^{3-j}$ | $\pi_j$ |
|-----|----------------|------------------|---------|
| 0 | 1 | $(0.5333)^3 = 0.1517$ | $0.9418 \times 0.1517 = 0.1429$ |
| 1 | 3 | $(0.4667)(0.5333)^2 = 0.1327$ | $0.9418 \times 3 \times 0.1327 = 0.3750$ |
| 2 | 3 | $(0.4667)^2(0.5333) = 0.1162$ | $0.9418 \times 3 \times 0.1162 = 0.3285$ |
| 3 | 1 | $(0.4667)^3 = 0.1016$ | $0.9418 \times 0.1016 = 0.0957$ |

**Verification**: $\sum_{j=0}^3 \pi_j = 0.1429 + 0.3750 + 0.3285 + 0.0957 = 0.9421 \approx e^{-0.06}$ ✓

**Step 4**: Option price

$$
\begin{aligned}
C_0 &= \sum_{j=0}^3 \pi_j C_j \\
&= 0.1429 \times 0 + 0.3750 \times 0 + 0.3285 \times 10.05 + 0.0957 \times 28.10 \\
&= 3.30 + 2.69 \\
&= 5.99
\end{aligned}
$$



This matches the result from backward induction.

---

## 5. Comparison with Backward Induction

### **Two Computational Approaches**

**Backward Induction** (recursive):

$$
V_t = \frac{1}{1+r}[qV_{t+1}^u + (1-q)V_{t+1}^d]
$$


- Visits each node: $\sum_{t=0}^n (t+1) = O(n^2)$ operations
- Stores intermediate values at each node
- Naturally handles American options (early exercise)

**State Price Summation** (direct):

$$
V_0 = e^{-rT}\sum_{j=0}^n \binom{n}{j}q^j(1-q)^{n-j}V_j
$$


- Single summation over $n+1$ terminal states: $O(n)$ operations (ignoring binomial coefficient computation)
- Only requires terminal payoffs
- European options only

### **When to Use Each**

| Feature | Backward Induction | State Prices |
|---------|-------------------|--------------|
| **American options** | ✓ Natural | ✗ Not applicable |
| **Greeks** | ✓ Easy (finite differences) | ~ Requires recomputation |
| **Path-dependent** | ✓ Flexible | ✗ Terminal payoffs only |
| **Theoretical insight** | Moderate | ✓ High (connection to expectations) |
| **Computational cost** | $O(n^2)$ | $O(n)$ for terminal evaluation |
| **Implementation** | Iterative | Closed-form summation |

---

## 6. Connection to Risk-Neutral Valuation

### **Equivalence**

The state price formula

$$
V_0 = \sum_{j=0}^n \pi_j V_j
$$



is mathematically identical to the risk-neutral expectation

$$
V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[V_T]
$$



because:

$$
\mathbb{E}^{\mathbb{Q}}[V_T] = \sum_{j=0}^n \mathbb{Q}(\text{state } j) \cdot V_j = \sum_{j=0}^n \binom{n}{j}q^j(1-q)^{n-j} V_j
$$



### **Different Interpretations**

**Risk-neutral valuation** emphasizes:
- Changing the probability measure from $\mathbb{P}$ to $\mathbb{Q}$
- Discounted assets are martingales under $\mathbb{Q}$
- Pricing via expectation under the equivalent martingale measure

**State price valuation** emphasizes:
- Elementary state-contingent securities as building blocks
- Market completeness (spanning terminal states)
- Connection to general equilibrium (Arrow-Debreu economy)

Both lead to the **same price**—they are complementary perspectives, not competing methods.

---

## 7. Theoretical Significance

### **Fundamental Theorems Connection**

The **First Fundamental Theorem of Asset Pricing** states:
> No-arbitrage ⟺ Existence of a risk-neutral measure $\mathbb{Q}$

The **Second Fundamental Theorem** states:
> Market completeness ⟺ Uniqueness of $\mathbb{Q}$

State prices provide an explicit construction:
- $\pi_j > 0$ for all $j$ ⟹ No arbitrage (positive state prices)
- Unique $\{\pi_0, \ldots, \pi_n\}$ ⟹ Complete market (unique pricing)

### **Connection to Continuous Time**

As $n \to \infty$ with $\Delta t \to 0$:

$$
\sum_{j=0}^n \pi_j V_j \to \mathbb{E}^{\mathbb{Q}}\left[e^{-rT}V(S_T)\right] = \int_0^\infty e^{-rT} V(S) f^{\mathbb{Q}}(S) dS
$$



where $f^{\mathbb{Q}}$ is the risk-neutral density (e.g., lognormal in Black-Scholes).

This is the **Feynman-Kac formula**: the PDE solution $V(t,S)$ equals the expected discounted terminal payoff under $\mathbb{Q}$.

### **General Equilibrium Link**

In a complete Arrow-Debreu economy:
- Agents trade state-contingent claims
- Equilibrium prices $\{\pi_j\}$ emerge from supply-demand
- Asset prices are linear functionals of payoffs

The binomial model is a **finite-state realization** of Arrow-Debreu general equilibrium with:
- Two traded assets (stock, bond) ⟹ Complete market
- Unique state prices ⟹ No-arbitrage equilibrium
- Linear pricing ⟹ All derivatives are redundant securities

---

## 8. Extensions and Limitations

### **Advantages**

1. **Closed-form insight**: Direct formula for European options
2. **Theoretical clarity**: Explicit connection to fundamental theorems
3. **Numerical efficiency**: $O(n)$ evaluation for terminal payoffs
4. **Probabilistic interpretation**: Natural expectation-based framework

### **Limitations**

1. **European only**: Cannot handle early exercise
2. **Path-independent only**: Terminal payoffs must not depend on intermediate values
3. **No Greeks**: Requires full recomputation or finite difference approximation
4. **Binomial probability**: Computing $\binom{n}{j}$ for large $n$ requires care (use recursion or logarithms)

### **Exotic Extensions**

For path-dependent claims (barriers, lookbacks), state prices can be generalized to **path-contingent prices**:

$$
\pi_{\text{path}} = e^{-rT} \cdot q^{j_{\text{up}}}(1-q)^{j_{\text{down}}}
$$



where the price depends on the entire path, not just the terminal state. This requires enumerating $2^n$ paths rather than $n+1$ states.

---

## Summary

Arrow–Debreu state price valuation offers a complementary framework to backward induction:

1. **State prices** $\pi_j = e^{-rT}\binom{n}{j}q^j(1-q)^{n-j}$ represent the present value of unit payoffs in terminal state $j$

2. **Pricing formula**: $V_0 = \sum_{j=0}^n \pi_j V_j$ (forward aggregation vs. backward recursion)

3. **Equivalence**: Mathematically identical to risk-neutral expectation $V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[V_T]$

4. **Theoretical insight**: Connects to fundamental theorems, general equilibrium, and Feynman-Kac formula

5. **Practical use**: Efficient for European options with terminal payoffs; complements backward induction

This perspective completes the theoretical foundations of binomial pricing and prepares for the transition to continuous-time models.
