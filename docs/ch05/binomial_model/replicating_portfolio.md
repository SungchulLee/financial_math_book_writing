# Replicating Portfolio

## Introduction

In a complete market, every contingent claim can be **replicated**—there exists a portfolio of traded assets that produces exactly the same payoff in every state of the world. The cost of this replicating portfolio is the unique no-arbitrage price of the claim.

This section develops replication from two complementary perspectives:

1. **Trading Basis**: Replicate derivatives using stock and bond
2. **State Price Basis**: Replicate everything using Arrow-Debreu securities

Both approaches yield the same prices, but the state price perspective reveals the deeper structure of arbitrage-free pricing.

!!! info "Prerequisites"
    - [Binomial Model](binomial_model.md) (market setup, no-arbitrage condition)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Replicate any derivative using stock and bond
    2. Understand Arrow-Debreu securities and state prices
    3. Express stock and bond in terms of state prices
    4. See why all pricing approaches are equivalent
    5. Apply replication to price calls, puts, digitals, and forwards

---

## The Payoff Space

### One-Period Binomial Model

In the one-period binomial model, there are exactly **two possible states** at time $\Delta t$:

- **Up state**: Stock price is $uS_0$
- **Down state**: Stock price is $dS_0$

Any derivative has a payoff that depends on which state occurs:

$$
H = 
\begin{cases}
H_u & \text{(up state)} \\[4pt]
H_d & \text{(down state)}
\end{cases}
$$

We can represent this as a vector in $\mathbb{R}^2$:

$$
H = (H_u, H_d)
$$

### The Payoff Space Is Two-Dimensional

The set of all possible payoffs forms a **two-dimensional vector space**. Any payoff is just a pair of numbers—what you receive in the up state and what you receive in the down state.

To replicate arbitrary payoffs, we need **two linearly independent assets**. The binomial model provides exactly this:

- **Stock**: payoff $(uS_0, \, dS_0)$
- **Bond**: payoff $(e^{r\Delta t}, \, e^{r\Delta t})$

These vectors are linearly independent (the stock payoff varies across states; the bond payoff is constant), so they span $\mathbb{R}^2$.

!!! success "Market Completeness"
    The one-period binomial market is **complete**: any payoff $(H_u, H_d)$ can be replicated by some portfolio of stock and bond.
    
    Completeness implies:
    
    - Every derivative has a unique no-arbitrage price
    - There is exactly one risk-neutral measure $\mathbb{Q}$

---

## Method 1: Replication with Stock and Bond

### The Replication Problem

Given a derivative with payoff $(H_u, H_d)$, find a portfolio $(\Delta, B)$ where:

- $\Delta$ = number of shares of stock
- $B$ = units of bond (cash position)

such that the portfolio replicates the derivative in both states.

### The Replication Equations

**Up state**: Portfolio payoff must equal $H_u$
$$
\Delta \cdot uS_0 + B \cdot e^{r\Delta t} = H_u
$$

**Down state**: Portfolio payoff must equal $H_d$
$$
\Delta \cdot dS_0 + B \cdot e^{r\Delta t} = H_d
$$

This is a system of 2 linear equations in 2 unknowns.

### Solution

**Solving for $\Delta$** (subtract down equation from up equation):

$$
\Delta \cdot S_0(u - d) = H_u - H_d
$$

$$
\boxed{\Delta = \frac{H_u - H_d}{(u - d)S_0}}
$$

**Solving for $B$** (substitute $\Delta$ into up equation):

$$
B = e^{-r\Delta t}(H_u - \Delta \cdot uS_0)
$$

$$
\boxed{B = e^{-r\Delta t}\left(H_u - \frac{(H_u - H_d)u}{u - d}\right) = e^{-r\Delta t}\left(\frac{uH_d - dH_u}{u - d}\right)}
$$

### The Replication Price

The cost of the replicating portfolio at time $0$ is:

$$
\boxed{V_0 = \Delta \cdot S_0 + B}
$$

By the **law of one price**, this must equal the derivative price. If the derivative traded at any other price, arbitrage would be possible.

---

## Examples: Stock-Bond Replication

We use these parameters throughout:

| Parameter | Value |
|-----------|-------|
| $S_0$ | $100$ |
| $u$ | $1.2$ |
| $d$ | $0.9$ |
| $r$ | $5\%$ |
| $\Delta t$ | $1$ year |
| $e^{r\Delta t}$ | $1.0513$ |

### Example 1: European Call (Strike $K = 105$)

**Payoffs:**
$$
H_u = (120 - 105)^+ = 15, \qquad H_d = (90 - 105)^+ = 0
$$

**Replicating portfolio:**
$$
\Delta = \frac{15 - 0}{(1.2 - 0.9) \times 100} = \frac{15}{30} = 0.5
$$

$$
B = e^{-0.05}\left(\frac{1.2 \times 0 - 0.9 \times 15}{1.2 - 0.9}\right) = 0.9512 \times (-45) = -42.80
$$

**Price:**
$$
C_0 = 0.5 \times 100 + (-42.80) = 7.20
$$

**Interpretation**: Buy 0.5 shares, borrow \$42.80.

### Example 2: European Put (Strike $K = 105$)

**Payoffs:**
$$
H_u = (105 - 120)^+ = 0, \qquad H_d = (105 - 90)^+ = 15
$$

**Replicating portfolio:**
$$
\Delta = \frac{0 - 15}{30} = -0.5, \qquad B = 0.9512 \times \frac{1.2 \times 15 - 0.9 \times 0}{0.3} = 57.07
$$

**Price:**
$$
P_0 = -0.5 \times 100 + 57.07 = 7.07
$$

**Interpretation**: Short 0.5 shares, lend \$57.07.

### Example 3: Forward Contract (Forward Price $F$)

**Payoffs:**
$$
H_u = uS_0 - F = 120 - F, \qquad H_d = dS_0 - F = 90 - F
$$

**Replicating portfolio:**
$$
\Delta = \frac{(120 - F) - (90 - F)}{30} = \frac{30}{30} = 1
$$

$$
B = e^{-0.05}(120 - F - 1 \times 120) = -Fe^{-0.05}
$$

**Price:**
$$
V_0 = 1 \times 100 - Fe^{-0.05} = S_0 - Fe^{-r\Delta t}
$$

Setting $V_0 = 0$ (forward has zero initial cost): $F = S_0 e^{r\Delta t} = 105.13$

---

## Method 2: Arrow-Debreu Securities and State Prices

### Arrow-Debreu Securities

An **Arrow-Debreu security** (or **state-contingent claim**) pays \$1 in exactly one state and \$0 in all other states.

In the binomial model, there are two Arrow-Debreu securities:

**Up-state digital** $(\mathbf{1}_u)$:
$$
\mathbf{1}_u = 
\begin{cases}
1 & \text{(up state)} \\
0 & \text{(down state)}
\end{cases}
= (1, 0)
$$

**Down-state digital** $(\mathbf{1}_d)$:
$$
\mathbf{1}_d = 
\begin{cases}
0 & \text{(up state)} \\
1 & \text{(down state)}
\end{cases}
= (0, 1)
$$

### The State Price Basis

The Arrow-Debreu securities form a **basis** for the payoff space. Any payoff $(H_u, H_d)$ can be written as:

$$
\boxed{H = H_u \cdot \mathbf{1}_u + H_d \cdot \mathbf{1}_d}
$$

This is trivially true—you just hold $H_u$ units of the up-state digital and $H_d$ units of the down-state digital.

### State Prices

Let $\psi_u$ and $\psi_d$ denote the **prices** of the Arrow-Debreu securities:

- $\psi_u$ = price of up-state digital (price today of receiving \$1 if up)
- $\psi_d$ = price of down-state digital (price today of receiving \$1 if down)

These are called **state prices** (or **Arrow-Debreu prices**).

### Universal Pricing Formula

Since any payoff is a linear combination of Arrow-Debreu securities:

$$
\boxed{V_0 = \psi_u H_u + \psi_d H_d}
$$

**This is the fundamental pricing formula.** Once you know the state prices, you can price any derivative by simple multiplication.

---

## Deriving State Prices

The state prices must be consistent with the traded asset prices (stock and bond). We derive them by replicating the Arrow-Debreu securities.

### Replicating the Up-State Digital

The up-state digital has payoff $(1, 0)$. Using the stock-bond replication formulas:

$$
\Delta_u = \frac{1 - 0}{(u-d)S_0} = \frac{1}{(u-d)S_0}
$$

$$
B_u = e^{-r\Delta t}\left(\frac{u \cdot 0 - d \cdot 1}{u-d}\right) = e^{-r\Delta t}\left(\frac{-d}{u-d}\right)
$$

**Price of up-state digital:**
$$
\psi_u = \Delta_u S_0 + B_u = \frac{1}{u-d} + e^{-r\Delta t}\left(\frac{-d}{u-d}\right) = \frac{1 - de^{-r\Delta t}}{u-d}
$$

Simplifying:
$$
\boxed{\psi_u = e^{-r\Delta t} \cdot \frac{e^{r\Delta t} - d}{u - d} = e^{-r\Delta t} q}
$$

where $q = \frac{e^{r\Delta t} - d}{u-d}$ is the risk-neutral probability.

### Replicating the Down-State Digital

The down-state digital has payoff $(0, 1)$:

$$
\Delta_d = \frac{0 - 1}{(u-d)S_0} = \frac{-1}{(u-d)S_0}
$$

$$
B_d = e^{-r\Delta t}\left(\frac{u \cdot 1 - d \cdot 0}{u-d}\right) = e^{-r\Delta t}\left(\frac{u}{u-d}\right)
$$

**Price of down-state digital:**
$$
\psi_d = \Delta_d S_0 + B_d = \frac{-1}{u-d} + e^{-r\Delta t}\left(\frac{u}{u-d}\right) = \frac{ue^{-r\Delta t} - 1}{u-d}
$$

Simplifying:
$$
\boxed{\psi_d = e^{-r\Delta t} \cdot \frac{u - e^{r\Delta t}}{u - d} = e^{-r\Delta t}(1-q)}
$$

### State Prices Summary

| Security | Payoff | Price |
|----------|--------|-------|
| Up-state digital | $(1, 0)$ | $\psi_u = e^{-r\Delta t} q$ |
| Down-state digital | $(0, 1)$ | $\psi_d = e^{-r\Delta t}(1-q)$ |

With our parameters ($q = 0.5043$):
$$
\psi_u = 0.9512 \times 0.5043 = 0.4797
$$
$$
\psi_d = 0.9512 \times 0.4957 = 0.4716
$$

---

## Replicating Stock and Bond with Arrow-Debreu Securities

The Arrow-Debreu basis allows us to express the traded assets as linear combinations:

### Stock Replication

The stock payoff is $(uS_0, dS_0)$:

$$
S_{\Delta t} = uS_0 \cdot \mathbf{1}_u + dS_0 \cdot \mathbf{1}_d
$$

**Stock price using state prices:**
$$
S_0 = \psi_u \cdot uS_0 + \psi_d \cdot dS_0 = S_0(\psi_u u + \psi_d d)
$$

This implies:
$$
\boxed{\psi_u u + \psi_d d = 1}
$$

### Bond Replication

The bond payoff is $(e^{r\Delta t}, e^{r\Delta t})$:

$$
B_{\Delta t} = e^{r\Delta t} \cdot \mathbf{1}_u + e^{r\Delta t} \cdot \mathbf{1}_d = e^{r\Delta t}(\mathbf{1}_u + \mathbf{1}_d)
$$

**Bond price using state prices:**
$$
B_0 = 1 = \psi_u \cdot e^{r\Delta t} + \psi_d \cdot e^{r\Delta t} = e^{r\Delta t}(\psi_u + \psi_d)
$$

This implies:
$$
\boxed{\psi_u + \psi_d = e^{-r\Delta t}}
$$

**Interpretation**: The sum of state prices equals the discount factor. Receiving \$1 in every state is equivalent to holding a zero-coupon bond.

---

## Connection to Risk-Neutral Probability

### State Prices and Probability

The state prices can be written as:

$$
\psi_u = e^{-r\Delta t} q, \qquad \psi_d = e^{-r\Delta t}(1-q)
$$

where $q = \frac{e^{r\Delta t} - d}{u-d} \in (0,1)$.

The pricing formula becomes:

$$
V_0 = \psi_u H_u + \psi_d H_d = e^{-r\Delta t}(qH_u + (1-q)H_d) = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[H]
$$

!!! success "State Prices and Risk-Neutral Measure"
    $$
    \psi_u = e^{-r\Delta t} q, \qquad \psi_d = e^{-r\Delta t}(1-q)
    $$
    
    State prices are **discounted risk-neutral probabilities**. The risk-neutral measure $\mathbb{Q}$ encodes the state prices in probability form.

### Why $q$ Is Called "Risk-Neutral"

Under the measure $\mathbb{Q}$ with $\mathbb{Q}(up) = q$:

$$
\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] = q \cdot uS_0 + (1-q) \cdot dS_0 = S_0 e^{r\Delta t}
$$

The stock's expected return equals the risk-free rate—as if investors were neutral to risk.

---

## Examples: State Price Method

Using state prices $\psi_u = 0.4797$ and $\psi_d = 0.4716$:

### European Call (Strike $K = 105$)

$$
C_0 = \psi_u \cdot 15 + \psi_d \cdot 0 = 0.4797 \times 15 = 7.20 \text{ ✓}
$$

### European Put (Strike $K = 105$)

$$
P_0 = \psi_u \cdot 0 + \psi_d \cdot 15 = 0.4716 \times 15 = 7.07 \text{ ✓}
$$

### Forward Contract

$$
V_0 = \psi_u(120 - F) + \psi_d(90 - F) = 0.4797 \times 120 + 0.4716 \times 90 - F(\psi_u + \psi_d)
$$
$$
= 57.56 + 42.44 - F \times 0.9512 = 100 - 0.9512F
$$

Setting $V_0 = 0$: $F = 100/0.9512 = 105.13$ ✓

---

## Comparison of Methods

| Aspect | Stock-Bond Replication | State Price Method |
|--------|------------------------|---------------------|
| **Basis** | $(S, B)$ | $(\mathbf{1}_u, \mathbf{1}_d)$ |
| **Payoffs** | $(uS_0, dS_0)$ and $(e^{r\Delta t}, e^{r\Delta t})$ | $(1, 0)$ and $(0, 1)$ |
| **To price $H$** | Solve 2×2 system for $(\Delta, B)$ | Compute $\psi_u H_u + \psi_d H_d$ |
| **Computation** | Requires solving equations each time | Direct multiplication once $\psi$ known |
| **Insight** | How to construct the hedge | Structure of arbitrage-free pricing |

**Both methods give identical prices** because they span the same payoff space.

---

## The Fundamental Theorems (Preview)

The replication results connect to the **Fundamental Theorems of Asset Pricing**:

!!! info "First Fundamental Theorem"
    The market is **arbitrage-free** if and only if there exist positive state prices $(\psi_u, \psi_d) > 0$.
    
    Equivalently: there exists a risk-neutral measure $\mathbb{Q}$.

!!! info "Second Fundamental Theorem"  
    The market is **complete** if and only if the state prices (equivalently, $\mathbb{Q}$) are unique.

In the one-period binomial model:
- No-arbitrage ($d < e^{r\Delta t} < u$) guarantees positive state prices
- Two assets for two states guarantees uniqueness

See [FTAP](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md) for the general theory.

---

## Summary

| Concept | Formula |
|---------|---------|
| Stock-bond replication | $\Delta = \dfrac{H_u - H_d}{(u-d)S_0}$, $B = e^{-r\Delta t}\dfrac{uH_d - dH_u}{u-d}$ |
| Replication price | $V_0 = \Delta S_0 + B$ |
| Up-state price | $\psi_u = e^{-r\Delta t} q$ |
| Down-state price | $\psi_d = e^{-r\Delta t}(1-q)$ |
| State price formula | $V_0 = \psi_u H_u + \psi_d H_d$ |
| Sum of state prices | $\psi_u + \psi_d = e^{-r\Delta t}$ |

!!! abstract "Key Takeaways"
    1. **Two equivalent bases**: Stock-bond and Arrow-Debreu both span the payoff space.
    
    2. **Replication determines price**: The cost of the replicating portfolio is the unique no-arbitrage price.
    
    3. **State prices are fundamental**: $\psi_u$ and $\psi_d$ encode all pricing information.
    
    4. **State prices = discounted $\mathbb{Q}$-probabilities**: $\psi = e^{-r\Delta t} \times$ risk-neutral probability.
    
    5. **Completeness = unique prices**: Two independent assets for two states means every payoff has a unique price.

---

## What's Next

| Section | Topic |
|---------|-------|
| [Delta Hedging](delta_hedging.md) | Pricing via risk elimination |
| [Risk-Neutral Measure](risk_neutral_measure.md) | The measure $\mathbb{Q}$ and expectation pricing |
| [Multi-Period Model](multi_period_binomial_model.md) | Extending to multiple time steps |
