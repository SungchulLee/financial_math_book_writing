# Binary and Quanto Options: Alternative Decomposition Perspectives

This optional advanced topic explores how contingent claims can be decomposed and replicated using **binary (digital) options** and **quanto contracts**—an alternative to Arrow-Debreu state price valuation that bridges pricing theory with financial product design.

**Prerequisites**: Complete understanding of Arrow-Debreu state prices, replication, and risk-neutral valuation.

---

## 1. Conceptual Framework: Two Decomposition Paradigms

### **Arrow-Debreu State Price Approach**

**Philosophy**: Axiomatic, foundational, rooted in economic theory

**Basis elements**: Pure state-contingent claims
- Pay $1 in exactly one terminal state $j$
- Pay $0 in all other states
- Form a **complete basis** for the $(n+1)$-dimensional payoff space

**Valuation formula**:

$$
V_0 = \sum_{j=0}^n \pi_j V_j
$$


where $\pi_j = e^{-rT}\binom{n}{j}q^j(1-q)^{n-j}$ is the state price.

**Characteristics**:
- **Global**: Prices over all terminal nodes simultaneously
- **Linear**: Payoff space as vector space with natural basis
- **Complete markets**: Assumes every terminal state can be priced
- **Theoretical**: Connects to general equilibrium (Arrow-Debreu economy)

### **Binary/Quanto Decomposition Approach**

**Philosophy**: Instrumental, practical, rooted in financial engineering

**Basis elements**: Event-contingent claims
- **Binary options**: Pay $1$ if $S_T > K$, $0$ otherwise
- **Quanto contracts**: Pay scaled amount based on conditions (e.g., $S_T \cdot \mathbf{1}_{\{S_T > K\}}$)

**Valuation via integral representation**:

$$
(S_T - K)^+ = \int_K^\infty \mathbf{1}_{\{S_T > x\}} dx
$$



**Characteristics**:
- **Local/event-based**: Focuses on thresholds and ranges
- **Path-agnostic**: Conditions rather than exact states
- **Constructive**: Built from tradable instruments
- **Practical**: Aligns with how exotic products are designed

---

## 2. Mathematical Equivalence: Call as Integral of Binaries

### **Fundamental Identity**

For any realization $S_T$:

$$
\boxed{(S_T - K)^+ = \int_K^\infty \mathbf{1}_{\{S_T > x\}} dx}
$$



**Proof** (by cases):

*Case 1: $S_T \leq K$*
- For all $x \geq K$: $S_T \leq K \leq x$, so $\mathbf{1}_{\{S_T > x\}} = 0$
- Therefore: $\int_K^\infty 0 \, dx = 0 = (S_T - K)^+$ ✓

*Case 2: $S_T > K$*
- For $x \in [K, S_T)$: $\mathbf{1}_{\{S_T > x\}} = 1$
- For $x \geq S_T$: $\mathbf{1}_{\{S_T > x\}} = 0$
- Therefore: $\int_K^\infty \mathbf{1}_{\{S_T > x\}} dx = \int_K^{S_T} 1 \, dx = S_T - K = (S_T - K)^+$ ✓

### **Pricing Implication**

Taking risk-neutral expectation:

$$
\begin{aligned}
C_0 &= e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+] \\
&= e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[\int_K^\infty \mathbf{1}_{\{S_T > x\}} dx\right] \\
&= \int_K^\infty e^{-rT}\mathbb{Q}(S_T > x) dx \quad \text{(by Fubini)} \\
&= \int_K^\infty \text{Digital}(x) dx
\end{aligned}
$$



**Interpretation**: A vanilla call is a **continuum of binary options** stacked over strikes from $K$ to $\infty$.

**Connection to Greeks**:

$$
\frac{\partial C}{\partial K} = -\text{Digital}(K) = -e^{-rT}\mathbb{Q}(S_T > K)
$$



This is the **Breeden-Litzenberger formula**: the second derivative of call prices w.r.t. strike recovers the risk-neutral density.

---

## 3. Quanto Contracts: Definition and Examples

### **What is a Quanto?**

A **quanto** (quantity-adjusted) derivative pays based on a foreign asset but settles in domestic currency at a **fixed exchange rate**, eliminating FX risk.

**Generic quanto call payoff**:

$$
\text{Quanto Call} = (S_T - K)^+ \cdot Q
$$


where:
- $S_T$ = foreign asset price (in foreign currency)
- $K$ = strike (in foreign currency)
- $Q$ = fixed FX conversion rate (set at contract inception)

### **Example 1: Quanto Call on Nikkei 225**

**Setup**: U.S. investor wants Nikkei exposure without JPY/USD risk

**Contract**:
- Underlying: Nikkei 225 (in JPY)
- Strike: ¥30,000
- Fixed FX: $Q = 1/150$ (1 USD = 150 JPY)
- Maturity: 3 months

**Payoff (in USD)**:

$$
\text{Payoff} = \frac{1}{150} \cdot \max(S_T - 30000, 0)
$$



If Nikkei closes at ¥32,000:

$$
\text{Payoff} = \frac{2000}{150} \approx \$13.33
$$



**Key feature**: Regardless of actual JPY/USD rate at maturity, conversion uses fixed $Q = 1/150$.

### **Example 2: Quanto Put on Euro STOXX 50**

**Payoff (in USD)**:

$$
\text{Payoff} = \frac{1}{0.9} \cdot \max(4000 - S_T, 0)
$$


where $Q = 1/0.9$ (1 USD = 0.9 EUR, fixed).

### **Example 3: Equity-Linked Quanto Note**

**Structured payoff** (periodic coupons):

At each observation date $t_i$ (year $i$):

$$
\text{Coupon}_i = \begin{cases}
\text{Principal} \cdot \alpha & \text{if } S_{t_i} \geq K \text{ (target met)} \\
\text{Principal} \cdot \frac{S_{t_i}}{S_0} \cdot Q & \text{otherwise (performance-linked)}
\end{cases}
$$



**Use case**: Offers guaranteed principal + upside participation in foreign market, all in domestic currency.

---

## 4. Tradability and Market Reality

### **Are Binary Options Tradable?**

**Short answer**: Yes, but with limitations.

**Market structure**:
- **Exchange-traded**: Rare on major exchanges
- **OTC markets**: Common in FX, equity exotics, institutional derivatives
- **Retail**: Often restricted due to regulatory concerns (gambling-like characteristics)

**Practical note**: In pricing theory, we assume binaries are tradable (market completeness). In practice, they're synthesized via spreads or delta hedging.

### **Are Quanto Contracts Tradable?**

**Short answer**: Yes, widely traded.

**Common uses**:
- **FX derivatives**: Cross-currency equity/commodity exposure
- **Structured products**: Equity-linked notes, guaranteed funds
- **Institutional hedging**: Currency-hedged international portfolios

**Examples**:
- Quanto equity index options (Nikkei, DAX, FTSE)
- Currency-hedged ETFs (synthetic quantos)
- Structured notes with embedded quanto features

---

## 5. Comparison: Arrow-Debreu vs. Binary/Quanto

| Aspect | Arrow-Debreu | Binary/Quanto |
|--------|--------------|---------------|
| **Philosophical basis** | Economic theory (complete markets) | Financial engineering (replication) |
| **Basis elements** | State-contingent (one terminal node) | Event-contingent (threshold/range) |
| **Scope** | All terminal states | Specific conditions |
| **Mathematical form** | Discrete summation over states | Integral over strikes/barriers |
| **Tradability** | Theoretical (not directly traded) | Practical (OTC markets) |
| **Applications** | Pricing theory, general equilibrium | Product design, exotic derivatives |
| **Complexity** | Conceptually clean | Implementation-focused |

**Bottom line**: Both yield identical prices in complete markets, but emphasize different aspects:
- **Arrow-Debreu**: "What is the value of reaching state $j$?"
- **Binary/Quanto**: "What is the value of crossing threshold $K$?"

---

## 6. Replication Using Quanto Options in Binomial Model

### **Setup**

Consider replicating an option using two quanto-type instruments:
- **Up-quanto**: Pays $Q_u = C_u - K$ if stock moves up
- **Down-quanto**: Pays $Q_d = C_d - K$ if stock moves down

### **Replicating Portfolio**

Hold $\alpha$ units of up-quanto and $\beta$ units of down-quanto such that:

$$
\alpha Q_u + \beta Q_d = C_0
$$



**Matching conditions**:
- Up state: $\alpha Q_u \cdot u + \beta Q_d \cdot u = C_u$
- Down state: $\alpha Q_u \cdot d + \beta Q_d \cdot d = C_d$

**Solution**:

$$
\alpha = \frac{C_u - C_d}{Q_u(u - d)}, \quad \beta = \frac{C_u - \alpha Q_u u}{Q_d u}
$$



### **Connection to Delta Hedging**

Notice that:

$$
\alpha = \frac{C_u - C_d}{(C_u - K)(u - d)}
$$



If we define $Q_u = C_u - K \approx \Delta \cdot S_0 \cdot (u-1)$ for small moves, this recovers the **delta**:

$$
\Delta = \frac{C_u - C_d}{S_0(u - d)}
$$



**Insight**: Quanto-based replication is **algebraically equivalent** to delta hedging—just repackaged as structured products.

---

## 7. Advanced: Binary Option Pricing in Binomial Model

### **Binary Call Payoff**


$$
\text{Digital}(K) = \mathbf{1}_{\{S_T > K\}}
$$



### **Binomial Pricing**

At terminal time with $n$ steps:

$$
\text{Digital}_0(K) = e^{-rT}\sum_{j: S_0 u^j d^{n-j} > K} \binom{n}{j}q^j(1-q)^{n-j}
$$



Define $j^* = \min\{j : S_0 u^j d^{n-j} > K\}$. Then:

$$
\text{Digital}_0(K) = e^{-rT}\sum_{j=j^*}^n \binom{n}{j}q^j(1-q)^{n-j}
$$



**As $n \to \infty$**: Converges to Black-Scholes digital:

$$
\text{Digital}(K) = e^{-rT}\mathcal{N}(d_2)
$$



where $d_2 = \frac{\ln(S_0/K) + (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$.

---

## 8. Pedagogical Summary

### **When to Use Each Perspective**

**Arrow-Debreu state prices**:
- Teaching fundamental theorems of asset pricing
- Connecting to general equilibrium theory
- Proving market completeness
- Understanding risk-neutral valuation foundations

**Binary/Quanto decomposition**:
- Designing structured products
- Understanding exotic option Greeks
- Building intuition for barrier/digital features
- Practical hedging and replication strategies

### **Key Takeaways**

1. **Mathematical equivalence**: Both approaches yield identical prices in complete markets

2. **Complementary perspectives**:
   - Arrow-Debreu = "state-based" (which terminal node?)
   - Binary/Quanto = "event-based" (did we cross threshold?)

3. **Practical bridge**: Quanto options connect theoretical pricing to tradable instruments

4. **Unified framework**: All decompositions ultimately rely on no-arbitrage and market completeness

---

## Summary

Binary and quanto option decompositions provide an alternative lens for understanding contingent claim pricing:

- **Call as integral of binaries**: $(S_T - K)^+ = \int_K^\infty \mathbf{1}_{\{S_T > x\}} dx$

- **Quanto contracts**: Currency-hedged derivatives eliminating FX risk via fixed conversion

- **Replication**: Quanto-based portfolios algebraically equivalent to delta hedging

- **Theoretical connection**: Complements Arrow-Debreu by emphasizing event-contingent rather than state-contingent payoffs

This advanced topic bridges pricing theory with financial engineering practice, showing how academic frameworks translate to real-world derivative products.
