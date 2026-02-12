# Delta Hedging

## Introduction

This section develops option pricing through the **hedging argument**:

> **Combine an option with stock to eliminate risk. The resulting risk-free portfolio must earn the risk-free rate. This determines the option price.**

Unlike replication (which asks "what portfolio matches the payoff?"), hedging asks "what portfolio eliminates risk?" Both approaches yield the same price, but the hedging perspective provides crucial insight into risk management and the economic meaning of delta.

!!! info "Prerequisites"
    - [Binomial Model](binomial_model.md) (market setup, no-arbitrage condition)
    - [Replicating Portfolio](replicating_portfolio.md) (replication approach)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Construct a hedged portfolio that eliminates stock price risk
    2. Derive the hedge ratio (delta) that makes a portfolio risk-free
    3. Apply the no-arbitrage principle to determine option prices
    4. Understand the economic meaning of delta as a sensitivity measure
    5. See the equivalence between hedging and replication

---

## The Hedging Problem

### The Challenge

An option's payoff depends on the stock price—it's **risky**. The holder of a call option gains if the stock rises and loses if it falls. This exposure to stock price movements is called **stock price risk** or **delta risk**.

### The Insight

By combining the option with a position in the underlying stock, we can **offset** the option's sensitivity to stock price movements. If we choose the stock position carefully, the combined portfolio has the **same value regardless of whether the stock goes up or down**.

A portfolio with the same value in all states is **risk-free**.

### The Principle

A risk-free portfolio must earn the risk-free rate—otherwise, arbitrage is possible. This constraint determines the option price.

---

## Setting Up the Hedged Portfolio

### The Portfolio

Consider a portfolio consisting of:

- **Short 1 option** (we sell the option, receiving its price $V_0$)
- **Long $\Delta$ shares of stock** (we buy $\Delta$ shares, paying $\Delta S_0$)

The quantity $\Delta$ is called the **hedge ratio** or simply **delta**.

!!! note "Sign Convention"
    We use the **option writer's perspective**: short the option, hedge with long stock.
    
    Equivalently, from the option holder's perspective: long the option, hedge with short stock. The analysis is symmetric.

### Portfolio Values

**At time $0$:**
$$
\Pi_0 = \Delta \cdot S_0 - V_0
$$

**At time $\Delta t$ (up state):**
$$
\Pi_{\Delta t}^{up} = \Delta \cdot uS_0 - H_u
$$

**At time $\Delta t$ (down state):**
$$
\Pi_{\Delta t}^{down} = \Delta \cdot dS_0 - H_d
$$

where $H_u$ and $H_d$ are the option payoffs in the up and down states.

---

## Finding the Hedge Ratio

### The Risk-Elimination Condition

For the portfolio to be risk-free, its terminal value must be **the same in both states**:

$$
\Pi_{\Delta t}^{up} = \Pi_{\Delta t}^{down}
$$

$$
\Delta \cdot uS_0 - H_u = \Delta \cdot dS_0 - H_d
$$

### Solving for Delta

Rearranging:

$$
\Delta \cdot uS_0 - \Delta \cdot dS_0 = H_u - H_d
$$

$$
\Delta \cdot S_0(u - d) = H_u - H_d
$$

!!! success "The Hedge Ratio (Delta)"
    $$
    \boxed{\Delta = \frac{H_u - H_d}{(u - d)S_0}}
    $$
    
    Delta is the **ratio of the option's payoff spread to the stock's price spread**.

### Interpretation of Delta

- **$\Delta > 0$**: Option payoff increases when stock rises (e.g., call) → hedge with long stock
- **$\Delta < 0$**: Option payoff increases when stock falls (e.g., put) → hedge with short stock  
- **$|\Delta|$**: Magnitude of stock position needed to hedge one option

---

## The Risk-Free Portfolio Value

With $\Delta = \frac{H_u - H_d}{(u-d)S_0}$, the portfolio has the same terminal value in both states.

### Computing the Terminal Value

Substituting into the up-state value:

$$
\Pi_{\Delta t} = \Delta \cdot uS_0 - H_u = \frac{H_u - H_d}{(u-d)S_0} \cdot uS_0 - H_u
$$

$$
= \frac{u(H_u - H_d)}{u - d} - H_u = \frac{uH_u - uH_d - (u-d)H_u}{u - d}
$$

$$
= \frac{uH_u - uH_d - uH_u + dH_u}{u - d} = \frac{dH_u - uH_d}{u - d}
$$

**Verification** (down state):

$$
\Pi_{\Delta t} = \Delta \cdot dS_0 - H_d = \frac{d(H_u - H_d)}{u - d} - H_d = \frac{dH_u - uH_d}{u - d} \text{ ✓}
$$

!!! success "Risk-Free Terminal Value"
    $$
    \boxed{\Pi_{\Delta t} = \frac{dH_u - uH_d}{u - d}}
    $$
    
    This value is **deterministic**—it doesn't depend on which state occurs.

---

## The No-Arbitrage Pricing Principle

### The Fundamental Principle

> **A risk-free portfolio must earn exactly the risk-free rate.**

### Why This Must Be True

**If the portfolio earned more than $r$:**
- Borrow at rate $r$
- Invest in the portfolio
- Earn the spread risk-free → **arbitrage**

**If the portfolio earned less than $r$:**
- Short the portfolio
- Lend at rate $r$  
- Earn the spread risk-free → **arbitrage**

Since arbitrage cannot exist in equilibrium, all risk-free portfolios must earn rate $r$.

### Applying the Principle

The hedged portfolio is risk-free, so:

$$
\Pi_{\Delta t} = \Pi_0 \cdot e^{r\Delta t}
$$

Substituting:

$$
\frac{dH_u - uH_d}{u - d} = (\Delta S_0 - V_0) \cdot e^{r\Delta t}
$$

---

## Deriving the Option Price

Solving for $V_0$:

$$
\Delta S_0 - V_0 = e^{-r\Delta t} \cdot \frac{dH_u - uH_d}{u - d}
$$

$$
V_0 = \Delta S_0 - e^{-r\Delta t} \cdot \frac{dH_u - uH_d}{u - d}
$$

Substituting $\Delta = \frac{H_u - H_d}{(u-d)S_0}$:

$$
V_0 = \frac{H_u - H_d}{u - d} - e^{-r\Delta t} \cdot \frac{dH_u - uH_d}{u - d}
$$

$$
V_0 = \frac{1}{u-d}\left[(H_u - H_d) - e^{-r\Delta t}(dH_u - uH_d)\right]
$$

$$
V_0 = \frac{1}{u-d}\left[H_u(1 - de^{-r\Delta t}) + H_d(ue^{-r\Delta t} - 1)\right]
$$

Multiplying by $\frac{e^{r\Delta t}}{e^{r\Delta t}}$:

$$
V_0 = e^{-r\Delta t} \cdot \frac{1}{u-d}\left[H_u(e^{r\Delta t} - d) + H_d(u - e^{r\Delta t})\right]
$$

!!! success "Option Pricing Formula (via Hedging)"
    $$
    \boxed{V_0 = e^{-r\Delta t}\left[\frac{e^{r\Delta t} - d}{u - d} H_u + \frac{u - e^{r\Delta t}}{u - d} H_d\right]}
    $$

### Risk-Neutral Probability Emerges

Define $q := \frac{e^{r\Delta t} - d}{u - d}$. Then:

$$
\boxed{V_0 = e^{-r\Delta t}(qH_u + (1-q)H_d)}
$$

The risk-neutral probability **emerges from hedging**—it was not assumed!

---

## Numerical Example

### Setup

| Parameter | Value |
|-----------|-------|
| $S_0$ | $100$ |
| $u$ | $1.2$ |
| $d$ | $0.9$ |
| $r$ | $5\%$ |
| $\Delta t$ | $1$ year |
| Strike | $K = 105$ |

**Stock prices at $\Delta t$:**
- Up: $S_{\Delta t}^{up} = 120$
- Down: $S_{\Delta t}^{down} = 90$

### European Call Option

**Payoffs:**
$$
H_u = (120 - 105)^+ = 15, \qquad H_d = (90 - 105)^+ = 0
$$

**Delta:**
$$
\Delta = \frac{15 - 0}{(1.2 - 0.9) \times 100} = \frac{15}{30} = 0.5
$$

**Risk-free portfolio terminal value:**
$$
\Pi_{\Delta t} = \frac{0.9 \times 15 - 1.2 \times 0}{0.3} = \frac{13.5}{0.3} = 45
$$

**Initial portfolio value** (via no-arbitrage):
$$
\Pi_0 = e^{-0.05} \times 45 = 0.9512 \times 45 = 42.80
$$

**Option price:**
$$
V_0 = \Delta S_0 - \Pi_0 = 0.5 \times 100 - 42.80 = 7.20
$$

### Verification

**Up state:**
- Portfolio: $0.5 \times 120 - 15 = 60 - 15 = 45$ ✓
- Return: $45 / 42.80 = 1.0514 = e^{0.05}$ ✓

**Down state:**
- Portfolio: $0.5 \times 90 - 0 = 45$ ✓
- Return: $45 / 42.80 = 1.0514 = e^{0.05}$ ✓

!!! success "Result"
    The hedged portfolio earns exactly the risk-free rate in both states, confirming $C_0 = 7.20$.

### European Put Option

**Payoffs:**
$$
H_u = 0, \qquad H_d = 15
$$

**Delta:**
$$
\Delta = \frac{0 - 15}{30} = -0.5
$$

**Risk-free portfolio terminal value:**
$$
\Pi_{\Delta t} = \frac{0.9 \times 0 - 1.2 \times 15}{0.3} = \frac{-18}{0.3} = -60
$$

Note: Negative terminal value means we **owe** money. This is because with $\Delta < 0$, we're short stock + short put.

Let's redo with long put + short stock (holder's perspective):

**Portfolio**: Long 1 put + short $|\Delta| = 0.5$ shares

**Terminal values:**
- Up: $0 - 0.5 \times 120 = -60$
- Down: $15 - 0.5 \times 90 = 15 - 45 = -30$

These aren't equal! The issue is we need to hedge from the **writer's** perspective for a put.

**Correct portfolio**: Short 1 put + long $\Delta = -0.5$ shares (i.e., short 0.5 shares)

**Initial value:**
$$
\Pi_0 = -0.5 \times 100 - (-V_0) = -50 + V_0
$$

**Terminal values:**
- Up: $-0.5 \times 120 - 0 = -60$
- Down: $-0.5 \times 90 - 15 = -45 - 15 = -60$ ✓

Both give $-60$, so the portfolio is risk-free (with negative value—a liability).

**No-arbitrage:**
$$
-60 = (V_0 - 50) \times e^{0.05}
$$
$$
V_0 - 50 = -60 \times e^{-0.05} = -57.07
$$
$$
V_0 = 50 - 57.07 = -7.07
$$

Wait, this is negative! Let me reconsider the sign convention.

**Corrected analysis**: For a put with $\Delta < 0$, the hedged portfolio (short put, long $\Delta$ shares) means we're actually **short** $|\Delta|$ shares:

$$
\Pi_0 = \Delta S_0 - V_0 = -0.5 \times 100 - V_0 = -50 - V_0
$$

$$
\Pi_{\Delta t} = -0.5 \times uS_0 - H_u = -60 - 0 = -60 \text{ (up)}
$$
$$
\Pi_{\Delta t} = -0.5 \times dS_0 - H_d = -45 - 15 = -60 \text{ (down)}
$$

No-arbitrage: $-60 = (-50 - V_0) \times e^{0.05}$
$$
-50 - V_0 = -60 \times e^{-0.05} = -57.07
$$
$$
V_0 = -50 + 57.07 = 7.07
$$

!!! success "European Put Price"
    $$P_0 = 7.07$$

---

## Delta as Sensitivity

### The Meaning of Delta

Delta measures how much the option value changes when the stock price changes:

$$
\Delta = \frac{H_u - H_d}{(u-d)S_0} = \frac{\text{Option payoff change}}{\text{Stock price change}}
$$

In continuous time, this becomes:

$$
\Delta = \frac{\partial V}{\partial S}
$$

### Delta for Different Options

| Option | Delta | Meaning |
|--------|-------|---------|
| Call | $0 < \Delta < 1$ | Gains when stock rises |
| Put | $-1 < \Delta < 0$ | Gains when stock falls |
| Stock | $\Delta = 1$ | Perfect correlation |
| Bond | $\Delta = 0$ | No stock exposure |
| Forward | $\Delta = 1$ | Full stock exposure |

### Delta as Hedge Ratio

To hedge an option position:
- **Long 1 call** → **Short $\Delta$ shares** (where $\Delta > 0$)
- **Long 1 put** → **Long $|\Delta|$ shares** (where $\Delta < 0$, so long)

The hedge neutralizes the portfolio's sensitivity to small stock price movements.

---

## Equivalence to Replication

### The Two Approaches

**Replication** (from [Replicating Portfolio](replicating_portfolio.md)):
- Find $(\Delta, B)$ such that $\Delta S_{\Delta t} + B e^{r\Delta t} = H$ in all states
- Price = $\Delta S_0 + B$

**Hedging** (this section):
- Find $\Delta$ such that $\Delta S_{\Delta t} - H$ is constant
- Apply no-arbitrage to determine price

### Why They're Equivalent

Both approaches:
1. Use the same $\Delta = \frac{H_u - H_d}{(u-d)S_0}$
2. Apply no-arbitrage (law of one price / risk-free rate)
3. Yield the same price formula

The replication approach solves for the portfolio directly. The hedging approach constructs a risk-free combination and backs out the price. They're two sides of the same coin.

---

## Why Physical Probability Doesn't Appear

The hedging argument works **regardless of the actual probabilities** of up and down moves.

- The hedge eliminates risk in **both** states
- The risk-free portfolio earns $r$ no matter which state occurs
- The actual probability $p$ of an up move never enters the calculation

This is the deep insight of arbitrage pricing: **prices are determined by what can be hedged, not by beliefs about probabilities**.

---

## Summary

| Concept | Formula |
|---------|---------|
| Hedged portfolio | $\Pi = \Delta S - V$ (short option, long $\Delta$ shares) |
| Hedge ratio | $\Delta = \dfrac{H_u - H_d}{(u-d)S_0}$ |
| Risk-free condition | $\Pi_{\Delta t}^{up} = \Pi_{\Delta t}^{down}$ |
| No-arbitrage | $\Pi_{\Delta t} = \Pi_0 \cdot e^{r\Delta t}$ |
| Option price | $V_0 = e^{-r\Delta t}(qH_u + (1-q)H_d)$ |

!!! abstract "Key Takeaways"
    1. **Hedging eliminates risk**: By holding $\Delta$ shares against an option, the portfolio becomes risk-free.
    
    2. **No-arbitrage determines price**: A risk-free portfolio must earn the risk-free rate—this pins down the option price.
    
    3. **Delta emerges naturally**: The hedge ratio is uniquely determined by the risk-elimination condition.
    
    4. **Risk-neutral probability emerges**: The quantity $q$ appears from hedging—it's not assumed a priori.
    
    5. **Equivalent to replication**: Hedging and replication are different perspectives on the same mathematics.
    
    6. **Physical probability irrelevant**: The hedge works in all states, so actual probabilities don't affect the price.

---

## What's Next

| Section | Topic |
|---------|-------|
| [Risk-Neutral Measure](risk_neutral_measure.md) | The measure $\mathbb{Q}$ and expectation pricing |
| [Multi-Period Model](multi_period_binomial_model.md) | Dynamic delta hedging over multiple periods |
| [Binomial to Black–Scholes](binomial_to_black_scholes_limit.md) | Continuous-time limit |
