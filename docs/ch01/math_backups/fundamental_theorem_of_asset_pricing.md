# The Fundamental Theorem of Asset Pricing

The **Fundamental Theorem of Asset Pricing (FTAP)** is the cornerstone of modern mathematical finance. It establishes the deep equivalence between economic concepts (no-arbitrage) and probabilistic structures (equivalent martingale measures).

## Setup and Market Model

Consider a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with a filtration $\{\mathcal{F}_t\}_{t=0}^T$ representing information flow.

**Asset Price Process:**
We have $d+1$ assets with price processes $S^0_t, S^1_t, \ldots, S^d_t$:

- $S^0_t$: **Numéraire** (risk-free or risky asset), typically $S^0_t = e^{rt}$ or just the money market account

- $S^i_t$: **Risky assets** for $i = 1, \ldots, d$

**Trading Strategy:**
A **self-financing trading strategy** is a predictable process $\theta_t = (\theta^0_t, \theta^1_t, \ldots, \theta^d_t)$ where $\theta^i_t$ represents holdings in asset $i$.

The **portfolio value** is:

$$V_t(\theta) = \sum_{i=0}^d \theta^i_t S^i_t$$

**Self-financing condition:**

$$dV_t = \sum_{i=0}^d \theta^i_t \, dS^i_t$$

No exogenous cash flows—all gains/losses come from price changes.

**Discounted Prices:**
Define discounted prices relative to the numéraire:

$$\tilde{S}^i_t = \frac{S^i_t}{S^0_t}$$

## Key Definitions

**Arbitrage:**
An **arbitrage opportunity** is a self-financing strategy $\theta$ such that:

1. $V_0(\theta) = 0$ (no initial investment)

2. $V_T(\theta) \geq 0$ almost surely

3. $\mathbb{P}(V_T(\theta) > 0) > 0$ (positive probability of gain)

In other words: *something for nothing*.

**Equivalent Martingale Measure (EMM):**
A probability measure $\mathbb{Q}$ on $(\Omega, \mathcal{F})$ is an **equivalent martingale measure** (also called risk-neutral measure) if:

1. $\mathbb{Q} \sim \mathbb{P}$ (equivalence: $\mathbb{Q}(A) = 0 \iff \mathbb{P}(A) = 0$ for all $A \in \mathcal{F}$)

2. The discounted price processes $\tilde{S}^i_t$ are $\mathbb{Q}$-martingales for all $i = 1, \ldots, d$:

$$\tilde{S}^i_t = \mathbb{E}^{\mathbb{Q}}[\tilde{S}^i_T | \mathcal{F}_t]$$

**Market Completeness:**
A market is **complete** if every contingent claim can be replicated by a self-financing strategy.

## The Fundamental Theorem of Asset Pricing

The theorem comes in two parts:

### FTAP (First Version): No-Arbitrage and EMM Existence

**Theorem 1:** The market admits **no arbitrage** if and only if there exists an **equivalent martingale measure** $\mathbb{Q}$.

$$\text{No Arbitrage} \iff \exists \mathbb{Q} \sim \mathbb{P} \text{ such that } \tilde{S}^i_t \text{ is a } \mathbb{Q}\text{-martingale}$$

### FTAP (Second Version): Completeness and Uniqueness

**Theorem 2:** The market is **complete and arbitrage-free** if and only if there exists a **unique** equivalent martingale measure.

$$\text{Complete + No Arbitrage} \iff \exists! \mathbb{Q} \sim \mathbb{P} \text{ such that } \tilde{S}^i_t \text{ is a } \mathbb{Q}\text{-martingale}$$

## Proof (Finite State Space)

For clarity, I'll prove the finite case. The general continuous-time case requires functional analysis (Hahn-Banach theorem, Riesz representation).

### Setup for Finite Model

Consider a one-period model: $t \in \{0, 1\}$ with finite state space $\Omega = \{\omega_1, \ldots, \omega_n\}$.

Let $\mathbb{P}(\omega_i) = p_i > 0$ for all $i$.

We have $d+1$ assets with:

- Initial prices: $S^j_0$ for $j = 0, \ldots, d$

- Final prices: $S^j_1(\omega_i)$ for each state $\omega_i$

**Discounted payoff matrix:**
Assume $S^0_t = 1$ for simplicity (or discount everything by $S^0_1$). Define the **payoff matrix**:

$$X_{ij} = S^j_1(\omega_i) - S^j_0$$

This is an $n \times d$ matrix where row $i$ represents state $\omega_i$ and column $j$ represents asset $j$.

### Direction 1: No Arbitrage $\Rightarrow$ EMM Exists

**Proof:**

We need to show there exist probabilities $q_i > 0$ (with $\sum_i q_i = 1$) such that:

$$\mathbb{E}^{\mathbb{Q}}[S^j_1] = S^j_0 \quad \text{for all } j = 1, \ldots, d$$

Or equivalently:

$$\sum_{i=1}^n q_i S^j_1(\omega_i) = S^j_0$$

In matrix form, we seek $q \in \mathbb{R}^n$ with $q_i > 0$, $\sum_i q_i = 1$, such that:

$$X^T q = 0$$

where $X$ is the discounted payoff matrix (with $S^j_1$ replaced by $S^j_1 - S^j_0$).

**By contradiction:** Suppose no such $q$ exists. By the **separating hyperplane theorem**, there exists a vector $\theta \in \mathbb{R}^d$ such that:

$$X\theta \cdot q < 0 \quad \text{for all } q \text{ with } q_i > 0, \sum q_i = 1$$

But this means:

$$\sum_{i=1}^n q_i (X\theta)_i < 0$$

for all probability distributions $q$ with $q_i > 0$.

Taking $q = p$ (the physical measure), we get:

$$\mathbb{E}^{\mathbb{P}}[X\theta] < 0$$

But notice: $(X\theta)_i = \sum_{j=1}^d \theta^j X_{ij} = \sum_{j=1}^d \theta^j (S^j_1(\omega_i) - S^j_0)$ is the payoff in state $\omega_i$ of a portfolio with initial value $-\sum_j \theta^j S^j_0$.

Since we can make this strictly negative in expectation by choosing appropriate signs, we can construct:

- If $\mathbb{E}[X\theta] < 0$, consider $-\theta$ so $\mathbb{E}[-X\theta] > 0$

- Portfolio $-\theta$ has initial value $\sum_j \theta^j S^j_0$

- If this is $\leq 0$, we have arbitrage: non-positive cost, positive expected return, non-negative everywhere

Actually, more carefully: if $X\theta \geq 0$ everywhere and $\mathbb{E}[X\theta] > 0$, then strategy $\theta$ is an arbitrage.

The separating hyperplane theorem guarantees we can find such a $\theta$, contradicting no-arbitrage.

Therefore, an EMM $\mathbb{Q}$ exists. $\square$

### Direction 2: EMM Exists $\Rightarrow$ No Arbitrage

**Proof:**

Suppose $\mathbb{Q} \sim \mathbb{P}$ is an EMM, so:

$$\mathbb{E}^{\mathbb{Q}}[S^j_1] = S^j_0 \quad \text{for all } j$$

Consider any self-financing strategy $\theta$ with $V_0 = 0$. Then:

$$V_1 = \sum_{j=1}^d \theta^j (S^j_1 - S^j_0)$$

Taking $\mathbb{Q}$-expectation:

$$\mathbb{E}^{\mathbb{Q}}[V_1] = \sum_{j=1}^d \theta^j \mathbb{E}^{\mathbb{Q}}[S^j_1 - S^j_0] = \sum_{j=1}^d \theta^j (S^j_0 - S^j_0) = 0$$

So if $V_1 \geq 0$ almost surely, then $\mathbb{E}^{\mathbb{Q}}[V_1] \geq 0$, which equals $0$.

This means $\mathbb{Q}(V_1 > 0) = 0$ or $\mathbb{Q}(V_1 = 0) = 1$.

Since $\mathbb{Q} \sim \mathbb{P}$, we have $\mathbb{P}(V_1 > 0) = 0$ as well.

Therefore, no arbitrage exists. $\square$

### Completeness and Uniqueness

**Theorem:** The market is complete $\iff$ the EMM is unique.

**Proof sketch:**

- **Completeness $\Rightarrow$ Uniqueness**: If the market is complete, any contingent claim can be replicated. The price of any claim is uniquely determined by no-arbitrage. Since $\mathbb{E}^{\mathbb{Q}}[\tilde{X}]$ gives the price of claim $X$, and prices are unique, the measure $\mathbb{Q}$ must be unique.

- **Uniqueness $\Rightarrow$ Completeness**: If $\mathbb{Q}$ is unique, the payoff space spans all of $\mathbb{R}^n$ (the state space). Otherwise, there would be orthogonal directions allowing different martingale measures. Full span means any claim can be replicated.

Rigorously: the dimension of the null space of $X^T$ is $n - d - 1$ if and only if rank of $X$ is $d$ and we need $d = n - 1$ for uniqueness.

## Proof (Continuous Time Case - Sketch)

In continuous time, the proof uses **functional analysis**:

**No Arbitrage $\Rightarrow$ EMM:**

1. Define the set of attainable claims $\mathcal{C} = \{V_T(\theta) : \theta \text{ admissible}, V_0 = 0\}$

2. No arbitrage means $\mathcal{C} \cap L^{\infty}_+ = \{0\}$

3. By **Hahn-Banach separation theorem**, there exists a continuous linear functional $\Lambda$ on $L^{\infty}$ such that $\Lambda(X) = 0$ for $X \in \mathcal{C}$ and $\Lambda(X) > 0$ for $X \in L^{\infty}_+$

4. By **Riesz representation**, $\Lambda$ corresponds to a probability measure $\mathbb{Q}$

5. The martingale property follows from $\Lambda$ annihilating $\mathcal{C}$

**EMM $\Rightarrow$ No Arbitrage:** Similar to finite case.

The general continuous-time theory was developed by **Harrison, Kreps, and Pliska** (1979-1981) and extended by **Delbaen and Schachermayer** (1994) using stochastic calculus.

## Economic Intuition

### 1. **Market Efficiency and Consensus Beliefs**

The EMM $\mathbb{Q}$ represents a **consensus probability** under which all assets have the same expected return (the risk-free rate).

If such a consensus exists, there's no "free lunch"—all assets are fairly priced relative to each other.

### 2. **Risk-Neutral Valuation**

Under $\mathbb{Q}$:

$$S^i_t = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)} S^i_T | \mathcal{F}_t]$$

Everyone is "risk-neutral" under this measure—they only care about expected values, not risk. This doesn't mean investors ARE risk-neutral; it means we can PRICE as if they were.

### 3. **Arbitrage as Market Inconsistency**

Arbitrage represents an **inconsistency** in prices:

- Asset A is "too cheap" relative to Asset B

- Exploiting this gap generates risk-free profit

The existence of $\mathbb{Q}$ means prices are **internally consistent**—no such gaps exist.

### 4. **Why Equivalence Matters**

$\mathbb{Q} \sim \mathbb{P}$ ensures:

- Events possible under $\mathbb{P}$ remain possible under $\mathbb{Q}$

- We're not changing the "structure" of uncertainty

- We're only changing "probabilities" not "possibilities"

If $\mathbb{Q}$ were not equivalent to $\mathbb{P}$, we could have arbitrage by betting on events with different probabilities.

### 5. **Completeness = Unique Pricing**

When the EMM is unique:

- Every derivative has a **unique arbitrage-free price**

- Every claim can be **perfectly hedged**

- The market is "informationally complete"

Multiple EMMs mean **price indeterminacy**—derivatives have a range of no-arbitrage prices (bid-ask spread).

## Mathematical Intuition

### 1. **Duality Between Portfolios and Measures**

The FTAP establishes a **duality**:

$$\begin{array}{ccc}
\text{Portfolio strategies } \theta & \leftrightarrow & \text{Probability measures } \mathbb{Q} \\
\text{Arbitrage opportunities} & \leftrightarrow & \text{Non-existence of EMM} \\
\text{Market completeness} & \leftrightarrow & \text{Unique EMM}
\end{array}$$

This is analogous to **duality in optimization**: primal feasibility $\leftrightarrow$ dual feasibility.

### 2. **Martingales as "Fair Games"**

A martingale satisfies:

$$\mathbb{E}[X_{t+1} | \mathcal{F}_t] = X_t$$

This means "no predictable profit"—the best forecast of tomorrow's price is today's price.

The FTAP says: **No arbitrage $\iff$ Prices are fair games under some measure**.

### 3. **Connection to Convex Analysis**

The proof uses the **separating hyperplane theorem**:

- The set of arbitrage portfolios is a convex cone

- The set of positive payoffs is a convex cone 
 
- No arbitrage means these cones don't intersect (except at origin)

- A separating hyperplane exists, which defines the EMM

This is the same principle behind **Lagrange multipliers** and **KKT conditions** in optimization.

### 4. **Change of Measure via Radon-Nikodym**

In continuous time, the measure change is given by:

$$\frac{d\mathbb{Q}}{d\mathbb{P}} = \mathcal{E}\left(-\int_0^T \lambda_s \, dW_s\right)$$

where $\lambda_t$ is the **market price of risk** (Sharpe ratio), and $\mathcal{E}$ is the stochastic exponential:

$$\mathcal{E}(X)_t = \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right)$$

This connects to **Girsanov's theorem**: under $\mathbb{Q}$, the process $W^{\mathbb{Q}}_t = W_t + \int_0^t \lambda_s \, ds$ is a Brownian motion.

### 5. **Geometric Interpretation**

Think of the state space $\Omega$ as $\mathbb{R}^n$.

- Asset payoffs span a subspace $\mathcal{S} \subset \mathbb{R}^n$

- No arbitrage means the "positive cone" doesn't intersect $\mathcal{S}$ (except trivially)

- An EMM is a "pricing functional" orthogonal to $\mathcal{S}$ but positive on the entire space

- Uniqueness means $\mathcal{S}$ has codimension 1 (market spans almost everything)

## Connection to Black-Scholes

In the Black-Scholes model:

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

The **market price of risk** is:

$$\lambda = \frac{\mu - r}{\sigma}$$

The EMM is defined by:

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\left(-\lambda W_T - \frac{\lambda^2 T}{2}\right)$$

Under $\mathbb{Q}$:

$$dS_t = r S_t \, dt + \sigma S_t \, dW^{\mathbb{Q}}_t$$

The discounted stock price $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale, satisfying the FTAP.

Since there's only one source of randomness ($W_t$) and one risky asset, the market is **complete** and $\mathbb{Q}$ is **unique**.

## Summary

The FTAP is profound because it:

1. **Unifies economics and mathematics**: No-arbitrage (economic) $\leftrightarrow$ Martingale measure (probabilistic)

2. **Provides computational framework**: Pricing via expectation $V = \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi]$ instead of solving PDEs

3. **Reveals market structure**: Completeness, dimension of uncertainty, hedgeability

4. **Generalizes broadly**: Works for discrete/continuous time, finite/infinite states, American options, exotic derivatives

The theorem tells us: **If markets are arbitrage-free, there exists a probabilistic "shadow world" where all assets grow at the risk-free rate, and pricing is just expectation in that world.**

Would you like me to discuss the **Consumption-Based Asset Pricing** derivation next, which approaches this from a utility-maximization perspective?


---

# Clarifying the Separating Hyperplane Argument in the FTAP Proof

You're absolutely right to question that statement—I was not clear about which sets we're separating and how the separating hyperplane theorem is being applied. Let me give a **much clearer** proof.

## The Clean Proof

We want to show: **No Arbitrage** $\Rightarrow$ **EMM exists**

In other words, if there's no arbitrage, then there exists $q \in \mathbb{R}^n$ with $q_i > 0$, $\sum_i q_i = 1$, such that:

$$X^T q = 0$$

where $X$ is the payoff matrix ($X_{ij} = S^j_1(\omega_i) - S^j_0$).

### Step 1: Setup - What Are We Trying to Find?

Define the **probability simplex**:

$$\Delta^n = \left\{q \in \mathbb{R}^n : q_i > 0 \text{ for all } i, \sum_{i=1}^n q_i = 1\right\}$$

We want to find $q \in \Delta^n$ such that $X^T q = 0 \in \mathbb{R}^d$.

Equivalently, we're asking: **Does $0 \in \mathbb{R}^d$ lie in the image of $\Delta^n$ under the map $q \mapsto X^T q$?**

### Step 2: Proof by Contradiction

**Assume:** No such $q$ exists. That is, $0 \notin \{X^T q : q \in \Delta^n\}$.

Define the set:

$$\mathcal{S} = \{X^T q : q \in \Delta^n\} \subset \mathbb{R}^d$$

**Key observation:** $\mathcal{S}$ is:

- **Convex** (because $\Delta^n$ is convex and $q \mapsto X^T q$ is linear)

- **Compact** (because $\Delta^n$ is compact and the map is continuous)

- **Does not contain $0$** (by our assumption)

### Step 3: Apply Separating Hyperplane Theorem

Since $\mathcal{S}$ is a compact convex set and $\{0\}$ is a closed convex set, and they're disjoint, by the **strict separation** version of the separating hyperplane theorem, there exists $\theta \in \mathbb{R}^d$ (with $\theta \neq 0$) such that:

$$\theta^T (X^T q) < \theta^T \cdot 0 = 0 \quad \text{for all } q \in \Delta^n$$

Rewriting this (using $\theta^T (X^T q) = (\theta^T X^T) q = (X\theta)^T q = q^T (X\theta)$):

$$\boxed{q^T (X\theta) < 0 \quad \text{for all } q \in \Delta^n}$$

### Step 4: What Does This Tell Us About $X\theta$?

Let me evaluate $q^T(X\theta)$ for specific probability vectors:

**Take $q = e_1 = (1, 0, 0, \ldots, 0)$:**

$$e_1^T(X\theta) = (X\theta)_1 < 0$$

**Take $q = e_2 = (0, 1, 0, \ldots, 0)$:**

$$e_2^T(X\theta) = (X\theta)_2 < 0$$

**Continue for all basis vectors** $e_i$:

$$(X\theta)_i < 0 \quad \text{for all } i = 1, \ldots, n$$

Therefore:

$$\boxed{X\theta < 0 \quad \text{(strictly negative in ALL components)}}$$

### Step 5: Construct an Arbitrage

Now consider the strategy $-\theta$. Its payoff is:

$$X(-\theta) = -X\theta > 0 \quad \text{(strictly positive in ALL states)}$$

This means:

- **Initial cost:** The portfolio $-\theta$ has initial value $-\sum_{j=1}^d \theta^j S^j_0$

- **Payoff at time 1:** Positive in every state $\omega_i$

But wait—we need to verify this is an arbitrage. In the setup where $X_{ij}$ represents the **change** in value, the strategy $-\theta$ costs:

$$V_0(-\theta) = -\sum_{j=1}^d \theta^j S^j_0$$

Hmm, this might not be zero. Let me reconsider the setup.

### Clarification on the Model

Actually, in the standard setup:

- We work with **discounted prices** (discount by $S^0_1 = 1 + r$)

- A self-financing strategy has payoff $X\theta$ at time 1

- No arbitrage means: if $X\theta \geq 0$ and $X\theta \neq 0$, then this is impossible

So the condition $X\theta < 0$ means the strategy has strictly negative payoff in all states. Then $-\theta$ has strictly positive payoff:

$$X(-\theta) > 0$$

And since $X$ represents **excess returns** (discounted gains), a positive payoff vector with zero cost is an arbitrage.

More precisely, in the standard formulation:

- No arbitrage: there is no $\theta$ such that $X\theta \geq 0$ with at least one strict inequality

But we've constructed $\theta$ with $X\theta < 0$ (all strict), which means $-\theta$ satisfies $X(-\theta) > 0$ (all strict), contradicting no arbitrage.

### Step 6: Contradiction

We've shown:

$$\text{If no EMM exists} \Rightarrow \text{Arbitrage exists}$$

By contrapositive:

$$\boxed{\text{No Arbitrage} \Rightarrow \text{EMM exists}}$$

## What Were the Two Sets Being Separated?

To directly answer your question:

**Set 1:** $\mathcal{S} = \{X^T q : q \in \Delta^n\} \subset \mathbb{R}^d$

- This is the set of "expected payoffs" when we weight the payoff columns by probability distributions

**Set 2:** $\{0\} \subset \mathbb{R}^d$

- The origin in asset space

**Separating hyperplane:** Defined by the normal vector $\theta \in \mathbb{R}^d$

The separating condition says:

$$\theta^T s < 0 < \theta^T \cdot 0 = 0 \quad \text{for all } s \in \mathcal{S}$$

Wait, that's backwards. Let me reconsider. We have:

$$\theta^T s < \theta^T \cdot 0 = 0 \quad \text{for all } s \in \mathcal{S}$$

This means $\mathcal{S}$ lies entirely on one side of the hyperplane $\{x : \theta^T x = 0\}$, and that side is where $\theta^T x < 0$.

## Visual Intuition (for $d = 2$, $n = 3$)

Imagine $\mathbb{R}^2$ (two assets). The probability simplex $\Delta^3$ is a triangle in $\mathbb{R}^3$.

The map $q \mapsto X^T q$ takes this triangle and maps it to some region $\mathcal{S}$ in $\mathbb{R}^2$.

If $0 \notin \mathcal{S}$, then $\mathcal{S}$ is a blob in $\mathbb{R}^2$ that doesn't contain the origin.

The separating hyperplane theorem says: there's a line through the origin (defined by normal vector $\theta$) such that $\mathcal{S}$ lies entirely on one side of this line.

The vector $\theta$ then defines a portfolio whose payoffs $X\theta$ have a special property: when weighted by **any** probability distribution, the expected payoff is negative. This is only possible if $X\theta$ is negative in every state!

## Summary of the Corrected Argument

1. **Assume** no EMM exists: $0 \notin \{X^T q : q \in \Delta^n\}$

2. **Apply separating hyperplane:** Find $\theta$ such that $\theta^T(X^T q) < 0$ for all $q \in \Delta^n$

3. **Evaluate at basis vectors:** Get $(X\theta)_i < 0$ for all $i$, so $X\theta < 0$

4. **Construct arbitrage:** Strategy $-\theta$ has payoff $X(-\theta) = -X\theta > 0$ in all states

5. **Contradiction:** This contradicts no-arbitrage

6. **Conclusion:** An EMM must exist

The key insight is that if the "expected payoff set" $\mathcal{S}$ doesn't contain zero, then by geometric separation, there exists a portfolio whose expected payoff is negative **under every possible probability measure**—which is only possible if it's negative in every state!









---





# Risk-Free or Risky Numéraire

Q. Should Numéraire be risk-free asset? I think bond can be served as Numéraire, but it is risky. In fact, I think any stock, say WMT can be served as Numéraire.

A. You're absolutely correct! This is an excellent observation that highlights a subtle but important point about the FTAP.

## Numéraire Can Be Any Strictly Positive Traded Asset

The **numéraire** need not be risk-free. The only mathematical requirement is:

$$S^0_t > 0 \quad \text{almost surely for all } t$$

(strictly positive to avoid division by zero)

**Valid choices of numéraire include:**

- Risk-free bond: $S^0_t = e^{rt}$ (most common in textbooks)

- Risky corporate bond (with default risk)

- Any stock: WMT, AAPL, etc.

- A portfolio: $60\%$ S&P 500 + $40\%$ bonds

- Even a derivative: a zero-coupon bond, or a forward contract

## The Mathematical Framework

When you choose asset $S^0_t$ as numéraire, you work with **normalized prices**:

$$\tilde{S}^i_t = \frac{S^i_t}{S^0_t}$$

The FTAP states: Under the **numéraire-associated measure** $\mathbb{Q}^0$, the normalized processes $\tilde{S}^i_t$ are martingales:

$$\tilde{S}^i_t = \mathbb{E}^{\mathbb{Q}^0}\left[\tilde{S}^i_T \mid \mathcal{F}_t\right]$$

**Key insight:** Each choice of numéraire corresponds to a *different* equivalent martingale measure, but they all give the **same derivative prices** (numéraire-invariant pricing).

## Example: Stock as Numéraire

Suppose you choose WMT stock as numéraire: $S^0_t = S^{\text{WMT}}_t$.

Under the **WMT-forward measure** $\mathbb{Q}^{\text{WMT}}$, we have:

$$\frac{S^{\text{AAPL}}_t}{S^{\text{WMT}}_t} = \mathbb{E}^{\mathbb{Q}^{\text{WMT}}}\left[\frac{S^{\text{AAPL}}_T}{S^{\text{WMT}}_T} \bigg| \mathcal{F}_t\right]$$

The relative price AAPL/WMT is a $\mathbb{Q}^{\text{WMT}}$-martingale.

Similarly:

$$\frac{S^{\text{Bond}}_t}{S^{\text{WMT}}_t} = \mathbb{E}^{\mathbb{Q}^{\text{WMT}}}\left[\frac{S^{\text{Bond}}_T}{S^{\text{WMT}}_T} \bigg| \mathcal{F}_t\right]$$

Even the "risk-free" bond, when normalized by WMT, becomes a $\mathbb{Q}^{\text{WMT}}$-martingale!

## Why We Usually Choose the Risk-Free Asset

The convention $S^0_t = e^{rt}$ is popular because:

1. **Interpretation**: Under $\mathbb{Q}$ (risk-neutral measure), all assets grow *on average* at rate $r$
   
2. **Simplicity**: The numéraire itself is deterministic, so $d(e^{rt}) = re^{rt}dt$ has no stochastic term

3. **Connection to discounting**: Prices become $V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi_T | \mathcal{F}_t]$

4. **Historical**: Black-Scholes-Merton used this convention, and it became standard

But this is **convention, not necessity**.

## Change of Numéraire Theorem

This is formalized in the **Change of Numéraire Theorem**:

**Theorem:** Let $N_t$ and $M_t$ be two numéraires (strictly positive traded assets). Let $\mathbb{Q}^N$ and $\mathbb{Q}^M$ be their associated EMMs. Then:

$$\frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}\bigg|_{\mathcal{F}_T} = \frac{M_T/M_0}{N_T/N_0}$$

This Radon-Nikodym derivative relates the two measures.

**Pricing invariance:** For any derivative with payoff $\Phi_T$:

$$V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}\left[\frac{\Phi_T}{N_T} \bigg| \mathcal{F}_t\right] = M_t \cdot \mathbb{E}^{\mathbb{Q}^M}\left[\frac{\Phi_T}{M_T} \bigg| \mathcal{F}_t\right]$$

Same price, different representations!

## Application: Forward Measure (T-Bond as Numéraire)

A powerful application uses a **zero-coupon bond** maturing at $T$ as numéraire:

$$N_t = P(t,T) = \text{price at time } t \text{ of bond paying } \$1 \text{ at time } T$$

Under the **$T$-forward measure** $\mathbb{Q}^T$:

$$\frac{S_t}{P(t,T)} = \mathbb{E}^{\mathbb{Q}^T}\left[\frac{S_T}{P(T,T)} \bigg| \mathcal{F}_t\right] = \mathbb{E}^{\mathbb{Q}^T}[S_T | \mathcal{F}_t]$$

(since $P(T,T) = 1$)

So $S_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[S_T | \mathcal{F}_t]$.

**This is incredibly useful for pricing interest rate derivatives!**

## Why Your Observation Matters

Your insight connects to several deep ideas:

1. **Gauge freedom**: The choice of numéraire is like choosing coordinates—physics (prices) is invariant, but calculations may be simpler in one frame

2. **No "privileged" risk-free rate**: In incomplete markets or with funding constraints, there may be no universal risk-free rate. Different numéraires can model different funding costs

3. **Hedge fund approach**: Using the stock itself as numéraire leads to elegant derivations (this is the "change of numéraire" method you've been exploring for Black-Scholes)

4. **Multi-currency models**: Each currency has its own numéraire, and change of numéraire relates domestic and foreign risk-neutral measures

## Summary

The FTAP **does not require** a risk-free asset. The statement should be:

**"Choose any strictly positive traded asset $N_t$ as numéraire. Then no-arbitrage ⟺ there exists an equivalent probability measure $\mathbb{Q}^N$ under which all asset prices normalized by $N_t$ are martingales."**

The risk-free bond is just the **most convenient** choice for many applications, but mathematically, **any positive traded asset works**. The fact that the document says "typically $S^0_t = e^{rt}$" is acknowledging this—it's a typical choice, not a requirement.

This flexibility is what makes change of numéraire such a powerful technique in quantitative finance!

