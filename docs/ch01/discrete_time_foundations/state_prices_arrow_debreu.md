# Arrow-Debreu Securities and State Prices

Arrow-Debreu securities and state prices are foundational concepts in financial economics that provide a unified framework for pricing any financial asset. Introduced by Kenneth Arrow and Gérard Debreu in the 1950s, these ideas establish the theoretical basis for no-arbitrage pricing, risk-neutral valuation, and the completeness of financial markets.

!!! abstract "Learning Objectives"
    After completing this section, you should understand:
    
    - What Arrow-Debreu securities are and how they define state prices
    - How state prices relate to no-arbitrage conditions and risk-neutral pricing
    - The connection between state prices, stochastic discount factors, and equivalent martingale measures
    - How to extract state prices from observed market prices
    - Practical applications to derivative pricing and portfolio theory

---

## Setup: A Discrete-State Economy

Consider a single-period economy with time $t = 0$ (today) and $t = 1$ (future). At $t = 1$, exactly one of $S$ possible **states of the world** $\omega_1, \omega_2, \ldots, \omega_S$ will occur. Each state $\omega_s$ occurs with a known physical (real-world) probability $p_s > 0$, where

$$
\sum_{s=1}^{S} p_s = 1
$$

There are $N$ traded assets in this economy. Asset $j$ has a known price $P_j$ at $t = 0$ and delivers a state-contingent payoff $X_j(\omega_s) = X_{js}$ at $t = 1$. We can organize these payoffs into a **payoff matrix**:

$$
\mathbf{X} = \begin{pmatrix} X_{11} & X_{12} & \cdots & X_{1S} \\ X_{21} & X_{22} & \cdots & X_{2S} \\ \vdots & \vdots & \ddots & \vdots \\ X_{N1} & X_{N2} & \cdots & X_{NS} \end{pmatrix}
$$

where row $j$ represents the payoffs of asset $j$ across all states, and column $s$ represents the payoffs of all assets in state $s$.

<figure markdown="span">
  ![State Economy Diagram](./image/state_economy_diagram.svg)
  <figcaption markdown="span">Figure 1: A single-period economy. From the current state at $t = 0$, the economy transitions with probabilities $p_1, p_2, \ldots, p_S$ into one of $S$ possible states at $t = 1$. Each state $\omega_s$ determines a column of the payoff matrix $\mathbf{X}$, giving the payoffs $(X_{1s}, X_{2s}, \ldots, X_{Ns})^\top$ for all $N$ assets.</figcaption>
</figure>

---

## Arrow-Debreu Securities

### Definition

!!! info "Definition: Arrow-Debreu Security"
    An **Arrow-Debreu security** (also called a **pure state security** or **primitive security**) for state $s$ is a financial contract that pays exactly **1 unit of currency** if state $\omega_s$ occurs and **0** in all other states.

Formally, the Arrow-Debreu security for state $s$ has the payoff vector:

$$
\mathbf{e}_s = (0, \ldots, 0, \underbrace{1}_{s\text{-th position}}, 0, \ldots, 0)^\top
$$

If we have $S$ states, there are $S$ possible Arrow-Debreu securities $\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_S$, which together form the **identity matrix** $\mathbf{I}_S$.

### Intuition

Arrow-Debreu securities isolate and "price" individual states of the world. They decompose uncertainty into its most elementary components. Any asset with an arbitrary payoff profile can be viewed as a portfolio of Arrow-Debreu securities:

$$
\text{If asset } j \text{ pays } X_{js} \text{ in state } s, \text{ then: } \quad \mathbf{X}_j = \sum_{s=1}^{S} X_{js} \, \mathbf{e}_s
$$

This makes Arrow-Debreu securities the "building blocks" of all financial claims.

!!! example "Example: Two-State Economy"
    Suppose the economy has two states: **Boom** ($\omega_1$) and **Recession** ($\omega_2$).
    
    - The Arrow-Debreu security for Boom pays $(1, 0)$: you receive \$1 if the economy booms, \$0 otherwise.
    - The Arrow-Debreu security for Recession pays $(0, 1)$: you receive \$1 if recession occurs, \$0 otherwise.
    
    A stock that pays \$120 in Boom and \$80 in Recession is equivalent to holding 120 units of the Boom Arrow-Debreu security and 80 units of the Recession Arrow-Debreu security.

---

## State Prices

### Definition

!!! info "Definition: State Price"
    The **state price** $\phi_s$ is the price at $t = 0$ of the Arrow-Debreu security for state $s$. That is, $\phi_s$ is the cost today of receiving \$1 if and only if state $\omega_s$ occurs at $t = 1$.

The vector of state prices is:

$$
\boldsymbol{\phi} = (\phi_1, \phi_2, \ldots, \phi_S)^\top
$$

### Pricing Any Asset with State Prices

If state prices exist, the price of **any** asset $j$ with payoffs $(X_{j1}, X_{j2}, \ldots, X_{jS})$ is simply:

$$
\boxed{P_j = \sum_{s=1}^{S} \phi_s \, X_{js} = \boldsymbol{\phi}^\top \mathbf{X}_j}
$$

This is the **fundamental pricing equation**. It says that an asset's price equals the sum of its payoffs in each state, weighted by the state prices.

In matrix form for all $N$ assets:

$$
\mathbf{P} = \mathbf{X} \, \boldsymbol{\phi}
$$

where $\mathbf{P} = (P_1, P_2, \ldots, P_N)^\top$ is the vector of asset prices.

### Properties of State Prices

!!! tip "Key Properties"
    Under the assumption of **no arbitrage**:

    1. **Positivity**: $\phi_s > 0$ for all $s = 1, 2, \ldots, S$. Every state is "valuable" — investors are willing to pay a positive price for insurance against any possible state.
    
    2. **Sum relates to the risk-free rate**: If a risk-free bond exists paying \$1 in every state, its price is
    
    $$
    P_{\text{rf}} = \sum_{s=1}^{S} \phi_s = \frac{1}{1 + r_f}
    $$
    
    where $r_f$ is the one-period risk-free interest rate. Thus, $\sum_s \phi_s < 1$ when $r_f > 0$.
    
    3. **Linearity**: Pricing is linear — the price of a portfolio equals the portfolio of prices.

---

## No-Arbitrage and the Existence of State Prices

### Arbitrage

An **arbitrage opportunity** is a trading strategy that costs nothing (or less) today and yields a non-negative payoff in all future states with a strictly positive payoff in at least one state. Formally, a portfolio $\boldsymbol{\theta} = (\theta_1, \ldots, \theta_N)^\top$ is an arbitrage if:

$$
\boldsymbol{\theta}^\top \mathbf{P} \leq 0, \quad \mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}, \quad \text{and} \quad \mathbf{X}^\top \boldsymbol{\theta} \neq \mathbf{0}
$$

### The Fundamental Theorem (First Version)

!!! success "Theorem: No-Arbitrage $\iff$ Existence of Positive State Prices"
    There are **no arbitrage opportunities** in the market if and only if there exists a strictly positive state price vector $\boldsymbol{\phi} \gg \mathbf{0}$ such that:
    
    $$
    \mathbf{P} = \mathbf{X} \, \boldsymbol{\phi}
    $$

This is a form of the **First Fundamental Theorem of Asset Pricing** in finite-state settings. It connects the economic condition (no free lunch) to a mathematical condition (existence of positive pricing functionals).

**Proof sketch**:

- ($\Leftarrow$) If $\boldsymbol{\phi} \gg 0$ exists, then any portfolio $\boldsymbol{\theta}$ with $\mathbf{X}^\top \boldsymbol{\theta} \geq 0$ must have $\boldsymbol{\theta}^\top \mathbf{P} = \boldsymbol{\theta}^\top \mathbf{X} \boldsymbol{\phi} \geq 0$, ruling out arbitrage.
- ($\Rightarrow$) Follows from the **Separating Hyperplane Theorem** (Farkas' Lemma): if no arbitrage exists, the set of achievable payoffs and the positive orthant can be separated, implying the existence of $\boldsymbol{\phi} \gg 0$.

---

## State Prices and Risk-Neutral Pricing

### Constructing the Risk-Neutral Measure

State prices naturally give rise to **risk-neutral probabilities**. Define:

$$
\boxed{q_s = \phi_s \,(1 + r_f) = \frac{\phi_s}{\sum_{k=1}^{S} \phi_k}}
$$

Since $\phi_s > 0$ for all $s$ and $\sum_s q_s = 1$, the $q_s$ form a valid probability measure $\mathbb{Q}$, called the **risk-neutral measure** (or **equivalent martingale measure**).

### Risk-Neutral Pricing Formula

Under $\mathbb{Q}$, the fundamental pricing equation becomes:

$$
P_j = \sum_{s=1}^{S} \phi_s \, X_{js} = \frac{1}{1+r_f} \sum_{s=1}^{S} q_s \, X_{js} = \frac{1}{1+r_f} \, \mathbb{E}^{\mathbb{Q}}[X_j]
$$

$$
\boxed{P_j = \frac{\mathbb{E}^{\mathbb{Q}}[X_j]}{1 + r_f}}
$$

!!! tip "Interpretation"
    Under the risk-neutral measure, every asset earns the risk-free rate in expectation. The asset price equals the **discounted expected payoff under $\mathbb{Q}$**. This is not because investors are risk-neutral — rather, risk aversion is already embedded in the distortion from $p_s$ to $q_s$.

### Comparing Physical and Risk-Neutral Probabilities

| State | Physical Prob. $p_s$ | State Price $\phi_s$ | Risk-Neutral Prob. $q_s$ |
|:---:|:---:|:---:|:---:|
| Boom | High | Low (relative to $p_s$) | Low |
| Recession | Low | High (relative to $p_s$) | High |

Risk-neutral probabilities **overweight bad states** (where marginal utility is high) and **underweight good states** relative to physical probabilities. This reflects the market's aggregate risk aversion.

---

## Stochastic Discount Factor (Pricing Kernel)

The **stochastic discount factor** (SDF), also called the **pricing kernel**, connects state prices to physical probabilities:

$$
\boxed{m_s = \frac{\phi_s}{p_s}}
$$

The SDF allows us to write the pricing equation using physical probabilities:

$$
P_j = \sum_{s=1}^{S} \phi_s \, X_{js} = \sum_{s=1}^{S} p_s \, m_s \, X_{js} = \mathbb{E}^{\mathbb{P}}[m \cdot X_j]
$$

$$
\boxed{P_j = \mathbb{E}^{\mathbb{P}}[m \cdot X_j]}
$$

!!! info "Interpretation of the SDF"
    - $m_s$ reflects the **marginal rate of substitution** between consumption today and consumption in state $s$.
    - In equilibrium models (e.g., CCAPM), $m_s = \beta \frac{u'(C_1(\omega_s))}{u'(C_0)}$, where $\beta$ is the time discount factor and $u$ is the utility function.
    - The SDF is high in "bad" states (low consumption) and low in "good" states (high consumption).

### Relationships Summary

The three representations — state prices, risk-neutral probabilities, and the SDF — are equivalent ways to enforce no-arbitrage:

$$
\phi_s = \frac{q_s}{1 + r_f} = p_s \cdot m_s
$$

| Representation | Pricing Formula | Key Object |
|:---|:---|:---|
| State Prices | $P = \sum_s \phi_s X_s$ | $\phi_s$ |
| Risk-Neutral | $P = \frac{1}{1+r_f}\mathbb{E}^{\mathbb{Q}}[X]$ | $q_s$ |
| SDF / Pricing Kernel | $P = \mathbb{E}^{\mathbb{P}}[m \cdot X]$ | $m_s$ |

---

## Complete Markets

### Definition

!!! info "Definition: Complete Market"
    A market is **complete** if every state-contingent payoff can be replicated by a portfolio of traded assets. Formally, the market is complete if for any payoff vector $\mathbf{c} \in \mathbb{R}^S$, there exists a portfolio $\boldsymbol{\theta} \in \mathbb{R}^N$ such that $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{c}$.

This requires $\text{rank}(\mathbf{X}) = S$, which in turn requires $N \geq S$ (at least as many assets as states).

### Uniqueness of State Prices

!!! success "Theorem: Completeness $\iff$ Unique State Prices"
    If the market is arbitrage-free, then:

    - **Complete market**: The state price vector $\boldsymbol{\phi}$ is **unique**. There is a unique risk-neutral measure $\mathbb{Q}$ and a unique SDF.
    - **Incomplete market**: Multiple state price vectors (and risk-neutral measures) are consistent with no-arbitrage. Assets can be priced, but not all contingent claims have a unique price.

This is related to the **Second Fundamental Theorem of Asset Pricing**.

!!! example "Example: Complete vs. Incomplete"
    **Complete**: 3 states, 3 linearly independent assets $\Rightarrow$ $\text{rank}(\mathbf{X}) = 3 = S$ $\Rightarrow$ unique $\boldsymbol{\phi}$.
    
    **Incomplete**: 3 states, 2 assets $\Rightarrow$ $\text{rank}(\mathbf{X}) \leq 2 < 3$ $\Rightarrow$ infinitely many $\boldsymbol{\phi}$ consistent with no-arbitrage.

---

## Extracting State Prices from Market Data

### From Observed Prices

Given $N$ assets with price vector $\mathbf{P}$ and payoff matrix $\mathbf{X}$, state prices solve:

$$
\mathbf{X} \, \boldsymbol{\phi} = \mathbf{P}
$$

- If $N = S$ and $\mathbf{X}$ has full rank: $\boldsymbol{\phi} = \mathbf{X}^{-1} \mathbf{P}$ (unique solution).
- If $N > S$: overdetermined system; use least squares or check consistency.
- If $N < S$: underdetermined; infinitely many solutions (incomplete market).

### Numerical Example

!!! example "Extracting State Prices: Two-State Example"
    Consider two states (Boom, Recession) and two assets:
    
    - **Risk-free bond**: Price = \$0.95, pays \$1 in both states.
    - **Stock**: Price = \$50, pays \$70 in Boom, \$40 in Recession.
    
    The payoff matrix and price vector are:
    
    $$
    \mathbf{X} = \begin{pmatrix} 1 & 1 \\ 70 & 40 \end{pmatrix}, \quad \mathbf{P} = \begin{pmatrix} 0.95 \\ 50 \end{pmatrix}
    $$
    
    Solving $\mathbf{X} \boldsymbol{\phi} = \mathbf{P}$:
    
    $$
    \begin{cases} \phi_1 + \phi_2 = 0.95 \\ 70\phi_1 + 40\phi_2 = 50 \end{cases}
    $$
    
    From the first equation: $\phi_2 = 0.95 - \phi_1$. Substituting:
    
    $$
    70\phi_1 + 40(0.95 - \phi_1) = 50 \implies 30\phi_1 = 12 \implies \phi_1 = 0.4
    $$
    
    $$
    \phi_2 = 0.95 - 0.4 = 0.55
    $$
    
    **Results**:
    
    | | Boom ($\omega_1$) | Recession ($\omega_2$) |
    |:---|:---:|:---:|
    | State Price $\phi_s$ | 0.40 | 0.55 |
    | Risk-Neutral Prob. $q_s = \phi_s / 0.95$ | 0.4211 | 0.5789 |
    
    Note that $\phi_2 > \phi_1$: the market prices recession insurance more highly than boom insurance, reflecting aggregate risk aversion. The risk-neutral probability of recession (0.5789) exceeds its physical probability (which might be, say, 0.3), distorting probabilities toward the "bad" state.

---

## From Option Prices: The Breeden-Litzenberger Result

In continuous-state settings, state prices can be extracted from **European option prices**. If $C(K)$ denotes the price of a European call option with strike $K$ on an asset with terminal price $S_T$, and the state price density is $\phi(s)$, then:

$$
C(K) = \int_K^{\infty} (s - K) \, \phi(s) \, ds
$$

Differentiating twice with respect to $K$:

$$
\boxed{\phi(K) = e^{r_f T} \frac{\partial^2 C}{\partial K^2}\bigg|_{K}}
$$

This is the **Breeden-Litzenberger formula**. It shows that the curvature of the call price function with respect to the strike price reveals the state price density (and hence the risk-neutral density).

!!! tip "Practical Implication"
    Butterfly spreads (long calls at $K - \Delta K$ and $K + \Delta K$, short two calls at $K$) approximate $\frac{\partial^2 C}{\partial K^2}$ and thus provide discrete estimates of state prices. This is the basis for extracting implied risk-neutral distributions from option markets.

---

## Multi-Period Extension

In a multi-period setting with times $t = 0, 1, \ldots, T$, the state price framework extends naturally via **state-price processes**.

### State-Price Deflator

A **state-price deflator** (or **numeraire portfolio process**) $\{\pi_t\}$ satisfies:

$$
P_t^{(j)} = \frac{1}{\pi_t} \mathbb{E}_t^{\mathbb{P}}[\pi_T \cdot X_T^{(j)}]
$$

for any asset $j$, where $\mathbb{E}_t^{\mathbb{P}}[\cdot]$ denotes the conditional expectation under the physical measure given information at time $t$.

### Recursive Pricing

Between any two adjacent periods $t$ and $t+1$:

$$
P_t = \mathbb{E}_t^{\mathbb{P}}[m_{t+1} \cdot (P_{t+1} + D_{t+1})]
$$

where $m_{t+1} = \pi_{t+1}/\pi_t$ is the **one-period SDF** and $D_{t+1}$ is any intermediate dividend.

---

## Connections to Other Topics

!!! note "Broader Context"
    State prices and Arrow-Debreu securities connect to many central topics in financial mathematics:
    
    - **Risk-Neutral Valuation**: State prices provide the discrete foundation for the risk-neutral pricing approach used in continuous-time models (Black-Scholes, etc.).
    - **Fundamental Theorems of Asset Pricing**: The existence and uniqueness of state prices correspond to the first and second fundamental theorems.
    - **Derivative Pricing**: Options and other derivatives are priced as portfolios of Arrow-Debreu securities.
    - **Term Structure Models**: State prices across maturities determine the yield curve and the prices of zero-coupon bonds.
    - **Portfolio Theory**: Complete markets allow perfect hedging; incomplete markets require optimization under constraints.
    - **Consumption-Based Models**: The SDF interpretation links asset pricing to macroeconomic fundamentals via the Euler equation.

---

## Summary

| Concept | Definition | Key Formula |
|:---|:---|:---|
| Arrow-Debreu Security | Pays \$1 in one state, \$0 otherwise | Payoff $= \mathbf{e}_s$ |
| State Price $\phi_s$ | Price of the Arrow-Debreu security for state $s$ | $P_j = \sum_s \phi_s X_{js}$ |
| Risk-Neutral Probability $q_s$ | $\phi_s$ rescaled to sum to 1 | $q_s = \phi_s(1+r_f)$ |
| Stochastic Discount Factor $m_s$ | State price per unit probability | $m_s = \phi_s / p_s$ |
| Complete Market | Every payoff is replicable | $\text{rank}(\mathbf{X}) = S$ |
| Breeden-Litzenberger | State prices from option prices | $\phi(K) = e^{rT} \partial^2 C / \partial K^2$ |

---

## Exercises

**Exercise 1.** Consider a two-state economy with states $\Omega = \{\omega_1, \omega_2\}$. A risk-free bond has price $P_{\text{rf}} = 0.90$ and pays \$1 in both states. A stock has price $P_2 = 60$ and pays \$80 in state $\omega_1$ and \$50 in state $\omega_2$. Compute the state prices $\phi_1$ and $\phi_2$, the risk-neutral probabilities $q_1$ and $q_2$, and the stochastic discount factor values $m_1$ and $m_2$ assuming physical probabilities $p_1 = 0.5$ and $p_2 = 0.5$.

---

**Exercise 2.** Prove that if no-arbitrage holds and a risk-free bond exists paying \$1 in every state, then the sum of the state prices satisfies

$$
\sum_{s=1}^{S} \phi_s = \frac{1}{1 + r_f}
$$

where $r_f$ is the risk-free rate. What does this imply about the relationship between state prices and risk-neutral probabilities?

---

**Exercise 3.** In a three-state economy with $\Omega = \{\omega_1, \omega_2, \omega_3\}$, the payoff matrix and price vector are

$$
\mathbf{X} = \begin{pmatrix} 1 & 1 & 1 \\ 60 & 50 & 40 \\ 10 & 5 & 0 \end{pmatrix}, \quad \mathbf{P} = \begin{pmatrix} 0.96 \\ 48 \\ 4.80 \end{pmatrix}
$$

Solve $\mathbf{X}\,\boldsymbol{\phi} = \mathbf{P}$ for the state price vector $\boldsymbol{\phi}$. Verify that all components are strictly positive and compute the implied risk-free rate.

---

**Exercise 4.** Show that the stochastic discount factor $m_s = \phi_s / p_s$ satisfies

$$
\mathbb{E}^{\mathbb{P}}[m] = \frac{1}{1 + r_f}
$$

when a risk-free bond exists. Interpret this result in terms of the relationship between the SDF and the time value of money.

---

**Exercise 5.** A market has two states and two traded assets (a bond and a stock). The state prices are $\phi_1 = 0.35$ and $\phi_2 = 0.60$. A new derivative is introduced with payoff $\Phi(\omega_1) = 10$ and $\Phi(\omega_2) = 3$. Using the fundamental pricing equation, compute the no-arbitrage price of this derivative. Then verify your answer using the risk-neutral pricing formula $P = \frac{1}{1+r_f}\mathbb{E}^{\mathbb{Q}}[\Phi]$.

---

**Exercise 6.** Explain why the Breeden-Litzenberger formula $\phi(K) = e^{r_f T} \frac{\partial^2 C}{\partial K^2}$ implies that the call price $C(K)$ must be a convex function of the strike price $K$ in an arbitrage-free market. What would a violation of convexity imply about state prices?

---

## Solutions

??? success "Solution to Exercise 1"
    **State prices:** Solve $\mathbf{X}\,\boldsymbol{\phi} = \mathbf{P}$:

    $$
    \begin{cases} \phi_1 + \phi_2 = 0.90 \\ 80\,\phi_1 + 50\,\phi_2 = 60 \end{cases}
    $$

    From equation (1): $\phi_2 = 0.90 - \phi_1$. Substituting into equation (2):

    $$
    80\,\phi_1 + 50(0.90 - \phi_1) = 60 \implies 30\,\phi_1 = 60 - 45 = 15 \implies \phi_1 = 0.50
    $$

    $$
    \phi_2 = 0.90 - 0.50 = 0.40
    $$

    **Risk-neutral probabilities:** The risk-free rate satisfies $1/(1 + r_f) = \sum_s \phi_s = 0.90$, so $r_f = 1/0.90 - 1 = 10/9 - 1 = 1/9 \approx 0.1111$ (about $11.11\%$). Then:

    $$
    q_1 = \frac{\phi_1}{\sum_s \phi_s} = \frac{0.50}{0.90} = \frac{5}{9} \approx 0.5556
    $$

    $$
    q_2 = \frac{\phi_2}{\sum_s \phi_s} = \frac{0.40}{0.90} = \frac{4}{9} \approx 0.4444
    $$

    **Stochastic discount factor:** With $p_1 = p_2 = 0.5$:

    $$
    m_1 = \frac{\phi_1}{p_1} = \frac{0.50}{0.50} = 1.00
    $$

    $$
    m_2 = \frac{\phi_2}{p_2} = \frac{0.40}{0.50} = 0.80
    $$

    **Verification:** $P_2 = \mathbb{E}^{\mathbb{P}}[m \cdot X_2] = 0.5(1.00)(80) + 0.5(0.80)(50) = 40 + 20 = 60$. Correct.

    Note that $m_2 < m_1$: the SDF is lower in the recession state, which is unusual. Typically the SDF is higher in bad states (reflecting higher marginal utility). Here the "recession" state has a lower SDF, which could occur if the economy has unusual risk preferences or if state $\omega_2$ is not truly the "bad" state in terms of aggregate consumption.

??? success "Solution to Exercise 2"
    Suppose a risk-free bond exists with payoff $X_{\text{rf},s} = 1$ for all $s = 1, \ldots, S$ and price $P_{\text{rf}}$. The fundamental pricing equation gives:

    $$
    P_{\text{rf}} = \sum_{s=1}^{S} \phi_s \cdot X_{\text{rf},s} = \sum_{s=1}^{S} \phi_s \cdot 1 = \sum_{s=1}^{S} \phi_s
    $$

    The risk-free bond has gross return $(1 + r_f)$, meaning:

    $$
    P_{\text{rf}} = \frac{1}{1 + r_f}
    $$

    (investing $P_{\text{rf}}$ today yields \$1 in every state, so the gross return is $1/P_{\text{rf}} = 1 + r_f$). Combining:

    $$
    \sum_{s=1}^{S} \phi_s = \frac{1}{1 + r_f}
    $$

    **Implication for risk-neutral probabilities:** Define $q_s = \phi_s (1 + r_f)$ for each $s$. Then:

    $$
    \sum_{s=1}^{S} q_s = (1 + r_f) \sum_{s=1}^{S} \phi_s = (1 + r_f) \cdot \frac{1}{1 + r_f} = 1
    $$

    Since $\phi_s > 0$ (no-arbitrage), we have $q_s > 0$ for all $s$. Therefore the $q_s$ form a valid probability measure. This is the risk-neutral measure $\mathbb{Q}$, and the state prices are precisely the discounted risk-neutral probabilities: $\phi_s = q_s / (1 + r_f)$.

??? success "Solution to Exercise 3"
    We solve the system $\mathbf{X}\,\boldsymbol{\phi} = \mathbf{P}$:

    $$
    \begin{cases} \phi_1 + \phi_2 + \phi_3 = 0.96 \\ 60\,\phi_1 + 50\,\phi_2 + 40\,\phi_3 = 48 \\ 10\,\phi_1 + 5\,\phi_2 + 0 \cdot \phi_3 = 4.80 \end{cases}
    $$

    Note that equation (2) equals $10 \times$ equation (1) plus $50\phi_1 + 40\phi_2 + 30\phi_3$... Let us solve directly.

    Subtract $40 \times$ equation (1) from equation (2):

    $$
    20\,\phi_1 + 10\,\phi_2 = 48 - 38.4 = 9.6 \quad \cdots \text{(i)}
    $$

    So $2\phi_1 + \phi_2 = 0.96$.

    From equation (3): $10\phi_1 + 5\phi_2 = 4.80$, so $2\phi_1 + \phi_2 = 0.96$ ... (ii).

    Equations (i) and (ii) are identical: $2\phi_1 + \phi_2 = 0.96$. This means we have one free parameter. Let $\phi_1 = t$. Then $\phi_2 = 0.96 - 2t$ and from equation (1): $\phi_3 = 0.96 - t - (0.96 - 2t) = t$.

    So $\boldsymbol{\phi} = (t,\; 0.96 - 2t,\; t)^\top$.

    For strict positivity: $t > 0$, $0.96 - 2t > 0 \implies t < 0.48$, and $t > 0$. So $t \in (0, 0.48)$.

    For example, choosing $t = 0.16$: $\boldsymbol{\phi} = (0.16,\; 0.64,\; 0.16)^\top$.

    **Verification:** $\phi_1 + \phi_2 + \phi_3 = 0.16 + 0.64 + 0.16 = 0.96$. Check equation (2): $60(0.16) + 50(0.64) + 40(0.16) = 9.6 + 32 + 6.4 = 48$. Check equation (3): $10(0.16) + 5(0.64) = 1.6 + 3.2 = 4.8$. All correct.

    All components are strictly positive for any $t \in (0, 0.48)$, confirming the market is arbitrage-free.

    **Implied risk-free rate:**

    $$
    \frac{1}{1 + r_f} = \sum_{s=1}^{3} \phi_s = 0.96 \implies 1 + r_f = \frac{1}{0.96} = \frac{25}{24} \implies r_f = \frac{1}{24} \approx 4.167\%
    $$

    Note that the state prices are not unique (the market has 3 states but the system has only 2 independent equations from 3 assets), confirming the market is incomplete.

??? success "Solution to Exercise 4"
    The SDF is $m_s = \phi_s / p_s$. Taking the expectation under the physical measure $\mathbb{P}$:

    $$
    \mathbb{E}^{\mathbb{P}}[m] = \sum_{s=1}^{S} p_s \, m_s = \sum_{s=1}^{S} p_s \cdot \frac{\phi_s}{p_s} = \sum_{s=1}^{S} \phi_s
    $$

    When a risk-free bond exists (as shown in Exercise 2):

    $$
    \sum_{s=1}^{S} \phi_s = \frac{1}{1 + r_f}
    $$

    Therefore:

    $$
    \mathbb{E}^{\mathbb{P}}[m] = \frac{1}{1 + r_f}
    $$

    **Interpretation:** The expected value of the SDF under the physical measure equals the discount factor. This means the SDF "on average" discounts future payoffs at the risk-free rate. Applying the SDF pricing formula to the risk-free bond with constant payoff \$1:

    $$
    P_{\text{rf}} = \mathbb{E}^{\mathbb{P}}[m \cdot 1] = \mathbb{E}^{\mathbb{P}}[m] = \frac{1}{1 + r_f}
    $$

    This confirms that the time value of money (as captured by $r_f$) is embedded in the average level of the SDF. The SDF fluctuates around its mean $1/(1 + r_f)$, being higher in bad states and lower in good states. This state-dependence is what distinguishes risky asset pricing from riskless discounting.

??? success "Solution to Exercise 5"
    **Using the fundamental pricing equation:**

    $$
    P_{\Phi} = \phi_1 \cdot \Phi(\omega_1) + \phi_2 \cdot \Phi(\omega_2) = 0.35 \times 10 + 0.60 \times 3 = 3.50 + 1.80 = 5.30
    $$

    **Verification via risk-neutral pricing:** First, find the risk-free rate:

    $$
    \frac{1}{1 + r_f} = \phi_1 + \phi_2 = 0.35 + 0.60 = 0.95 \implies r_f = \frac{1}{0.95} - 1 = \frac{1}{19} \approx 5.263\%
    $$

    The risk-neutral probabilities are:

    $$
    q_1 = \frac{\phi_1}{0.95} = \frac{0.35}{0.95} = \frac{7}{19} \approx 0.3684
    $$

    $$
    q_2 = \frac{\phi_2}{0.95} = \frac{0.60}{0.95} = \frac{12}{19} \approx 0.6316
    $$

    The risk-neutral expected payoff is:

    $$
    \mathbb{E}^{\mathbb{Q}}[\Phi] = q_1 \cdot 10 + q_2 \cdot 3 = \frac{7}{19} \cdot 10 + \frac{12}{19} \cdot 3 = \frac{70 + 36}{19} = \frac{106}{19}
    $$

    The discounted expected payoff is:

    $$
    P_{\Phi} = \frac{1}{1 + r_f} \cdot \mathbb{E}^{\mathbb{Q}}[\Phi] = 0.95 \times \frac{106}{19} = \frac{0.95 \times 106}{19} = \frac{100.7}{19} = 5.30
    $$

    Both methods give the same no-arbitrage price of **\$5.30**.

??? success "Solution to Exercise 6"
    The Breeden-Litzenberger formula states:

    $$
    \phi(K) = e^{r_f T} \frac{\partial^2 C}{\partial K^2}
    $$

    In an arbitrage-free market, state prices must be strictly positive: $\phi(K) > 0$ for all $K$ in the support of the asset's terminal distribution. Since $e^{r_f T} > 0$, positivity of $\phi(K)$ requires:

    $$
    \frac{\partial^2 C}{\partial K^2} > 0 \quad \text{for all } K
    $$

    This is precisely the condition that $C(K)$ is a **convex** function of $K$. (A twice-differentiable function is convex if and only if its second derivative is non-negative everywhere.)

    **What a violation of convexity would imply:** If $C(K)$ were not convex at some strike $K_0$, then $\frac{\partial^2 C}{\partial K^2}\big|_{K_0} < 0$, which would give $\phi(K_0) < 0$. A negative state price means the market assigns a negative value to receiving \$1 in a particular state of the world. This is economically absurd and constitutes an arbitrage opportunity.

    Concretely, a violation of convexity can be exploited via a **butterfly spread**: buy calls at strikes $K_0 - \Delta K$ and $K_0 + \Delta K$, and sell two calls at strike $K_0$. If $C(K)$ is locally concave at $K_0$, this butterfly spread has a negative cost (you receive a net premium) but a non-negative payoff in every state. This is a Type 2 arbitrage. Therefore, in an arbitrage-free market, call prices must be convex in the strike price.
