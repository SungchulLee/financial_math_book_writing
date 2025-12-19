# Risk-Neutral Probability

The **risk-neutral probability** is a cornerstone of modern derivative pricing. It is **not** a belief about real-world outcomes, but rather a mathematical construct that makes **discounted asset prices martingales** and enables arbitrage-free valuation.

---

## 1. Motivation: The Pricing Problem

In the binomial model, we established:
- **No-arbitrage condition**: $d < 1+r < u$
- **Replication**: Any claim can be replicated using $(\Delta, \beta)$
- **Unique pricing**: The law of one price determines $V_0$

But the replication formulas contain $\Delta$ and $\beta$, which depend on future payoffs. Is there a **direct formula** for $V_0$ without explicitly solving for the replicating portfolio?

**Answer**: Yes, via the **risk-neutral expectation**.

---

## 2. Definition and Construction

### **Risk-Neutral Probability**

Under the no-arbitrage condition $d < 1+r < u$, define:


$$
\boxed{q := \frac{(1+r)-d}{u-d}}
$$



**Properties**:
1. $0 < q < 1$ (follows from no-arbitrage)
2. $q$ depends only on $(u, d, r)$—**not** on the claim being priced
3. $q$ is the probability that makes discounted stock prices martingales

### **Why This Formula?**

We require the stock's **expected return** under $\mathbb{Q}$ to equal the risk-free rate. Under probability measure $\mathbb{Q}$ where $\mathbb{Q}(\text{up}) = q$:


$$
\mathbb{E}^{\mathbb{Q}}[S_1] = q(uS_0) + (1-q)(dS_0)
$$



Setting this equal to the risk-free growth:

$$
\mathbb{E}^{\mathbb{Q}}[S_1] = (1+r)S_0
$$



Solving for $q$:

$$
q(uS_0) + (1-q)(dS_0) = (1+r)S_0
$$



$$
q(u-d) = (1+r) - d
$$



$$
q = \frac{(1+r)-d}{u-d}
$$



This is the **unique** probability measure that makes the stock's expected return equal to $r$.

---

## 3. Martingale Property

### **Discounted Stock Price**

Under $\mathbb{Q}$, the **discounted stock price** is a martingale:


$$
\boxed{\mathbb{E}^{\mathbb{Q}}\left[\frac{S_1}{1+r}\right] = S_0}
$$



**Proof**:

$$
\mathbb{E}^{\mathbb{Q}}\left[\frac{S_1}{1+r}\right] = \frac{1}{1+r}\left[q(uS_0) + (1-q)(dS_0)\right] = \frac{(1+r)S_0}{1+r} = S_0
$$



**Interpretation**: Under $\mathbb{Q}$, the stock grows on average at the risk-free rate, so its discounted value remains constant.

### **General Martingale Property**

More generally, any **attainable payoff** $V_1$ has discounted value that is a martingale under $\mathbb{Q}$:

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\left[\frac{V_1}{1+r}\right]
$$



This is the foundation of **martingale pricing**.

---

## 4. Risk-Neutral Pricing Formula

### **One-Period Formula**

For any contingent claim with payoffs $H_u$ (up) and $H_d$ (down):


$$
\boxed{V_0 = \frac{1}{1+r}\,\mathbb{E}^{\mathbb{Q}}[H] = \frac{1}{1+r}\big(qH_u + (1-q)H_d\big)}
$$



**Key insight**: This formula:
- Requires **no knowledge** of the replicating portfolio $(\Delta, \beta)$
- Depends only on $q$ (market property) and payoffs $H_u, H_d$
- Yields the **same price** as replication (law of one price)

### **Equivalence to Replication**

The risk-neutral formula and replication formula must agree:

$$
\frac{1}{1+r}[qH_u + (1-q)H_d] = \Delta S_0 + \beta
$$



This can be verified by substituting:

$$
\Delta = \frac{H_u - H_d}{(u-d)S_0}, \quad \beta = \frac{uH_d - dH_u}{(u-d)(1+r)}
$$



Both perspectives yield the **same unique price**.

---

## 5. Interpretation: Risk-Neutral vs. Real-World

### **What $q$ Is NOT**

$q$ is **not**:
- The "true" probability of an up-move
- Derived from statistical estimation
- Related to investor beliefs about stock returns

### **What $q$ IS**

$q$ is:
- A **pricing tool** that simplifies valuation
- The probability that makes the market **arbitrage-free**
- An **equivalent martingale measure** (risk-neutral measure)

### **The Risk-Neutral "World"**

In the risk-neutral world:
- All investors act as if **risk-neutral** (no risk premium demanded)
- All assets earn the **risk-free rate** on average
- Asset prices are **fair game** (martingales after discounting)

**Why it works for pricing**: The **risk premium** that real investors demand is implicitly "baked into" the probability transformation from $\mathbb{P}$ (real-world) to $\mathbb{Q}$ (risk-neutral). The price we compute under $\mathbb{Q}$ is the **no-arbitrage price** in the real market.

### **Mathematical Perspective**

Real-world probability $\mathbb{P}$:
- Reflects actual likelihood of up/down moves
- Stock expected return includes risk premium: $\mathbb{E}^{\mathbb{P}}[S_1] = (1+\mu)S_0$ where $\mu > r$

Risk-neutral probability $\mathbb{Q}$:
- Adjusted probability that removes risk premium
- Stock expected return equals risk-free rate: $\mathbb{E}^{\mathbb{Q}}[S_1] = (1+r)S_0$

The **change of measure** from $\mathbb{P}$ to $\mathbb{Q}$ absorbs the risk premium, allowing pricing via simple expectation.

---

## 6. Multi-Period Extension

The one-period formula extends naturally to $N$ periods.

### **Independent Transitions**

At each node, the same $q$ applies:
- Transition probability up = $q$
- Transition probability down = $1-q$
- Transitions are **independent** across periods

### **Path Probability**

A path with $j$ up-moves (and $N-j$ down-moves) has probability:

$$
\mathbb{Q}(\text{path with } j \text{ ups}) = q^j(1-q)^{N-j}
$$



Number of such paths: $\binom{N}{j}$

### **Terminal State Probability**

Probability of reaching terminal state $j$ (after $j$ up-moves):

$$
\mathbb{Q}(\text{state } j) = \binom{N}{j}q^j(1-q)^{N-j}
$$



### **Multi-Period Pricing Formula**

For a European claim with terminal payoff $H_N$:

$$
V_0 = \frac{1}{(1+r)^N}\mathbb{E}^{\mathbb{Q}}[H_N] = \frac{1}{(1+r)^N}\sum_{j=0}^N \binom{N}{j}q^j(1-q)^{N-j}H_j
$$



where $H_j$ is the payoff in terminal state $j$.

---

## 7. Connection to FTAP

The risk-neutral probability is the discrete-time manifestation of a deep theorem.

### **First Fundamental Theorem of Asset Pricing (FTAP)**

> **No-arbitrage** $\iff$ There exists an **equivalent martingale measure** $\mathbb{Q}$

In the binomial model:
- **No-arbitrage**: $d < 1+r < u$
- **Existence of $\mathbb{Q}$**: $q = \frac{(1+r)-d}{u-d} \in (0,1)$

### **Second Fundamental Theorem**

> **Market completeness** $\iff$ **Uniqueness** of $\mathbb{Q}$

In the binomial model:
- Two assets (stock, bond) span two states $\Rightarrow$ complete market
- Unique $q$ $\Rightarrow$ unique pricing measure

---

## 8. Example: European Call

**Setup**: $S_0 = 100$, $u = 1.1$, $d = 0.95$, $r = 0.02$, $K = 105$

**Step 1**: Compute $q$

$$
q = \frac{1.02 - 0.95}{1.1 - 0.95} = \frac{0.07}{0.15} \approx 0.4667
$$



**Step 2**: Terminal payoffs
- Up: $S_1^u = 110$, $C_u = (110-105)^+ = 5$
- Down: $S_1^d = 95$, $C_d = (95-105)^+ = 0$

**Step 3**: Risk-neutral price

$$
C_0 = \frac{1}{1.02}[0.4667 \times 5 + 0.5333 \times 0] = \frac{2.33}{1.02} \approx 2.29
$$



**Verification via replication**:

$$
\Delta = \frac{5-0}{15} = \frac{1}{3}, \quad \beta = \frac{1.1 \times 0 - 0.95 \times 5}{0.15 \times 1.02} \approx -31.05
$$



$$
C_0 = \frac{1}{3} \times 100 - 31.05 = 33.33 - 31.05 = 2.28 \approx 2.29 \quad \checkmark
$$



Both methods yield the same price (minor rounding difference).

---

## Summary

The risk-neutral probability $q = \frac{(1+r)-d}{u-d}$ provides a powerful pricing framework:

1. **Definition**: The unique probability making discounted stock prices martingales

2. **Pricing formula**: $V_0 = \frac{1}{1+r}\mathbb{E}^{\mathbb{Q}}[H]$ (no replication calculation needed)

3. **Interpretation**: Not a real-world probability, but a pricing tool that absorbs the risk premium

4. **Equivalence**: Yields identical prices to replication (law of one price)

5. **Foundation**: Discrete-time instance of the Fundamental Theorem of Asset Pricing

6. **Extension**: Naturally generalizes to multi-period trees via independent transitions

This perspective transforms option pricing from a portfolio construction problem into an expectation calculation, paving the way for continuous-time martingale pricing.
