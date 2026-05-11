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

$$\begin{array}{lll}
\Pi_{\Delta t} 
&=&\displaystyle \Delta \cdot uS_0 - H_u\\ 
&=&\displaystyle \frac{H_u - H_d}{(u-d)S_0} \cdot uS_0 - H_u\\
&=&\displaystyle \frac{u(H_u - H_d)}{u - d} - H_u\\
&=&\displaystyle \frac{uH_u - uH_d - (u-d)H_u}{u - d}\\
&=&\displaystyle \frac{uH_u - uH_d - uH_u + dH_u}{u - d}\\
&=&\displaystyle \frac{dH_u - uH_d}{u - d}
\end{array}$$

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

Solving $\Delta S_0 - V_0 = e^{-r\Delta t} \cdot \frac{dH_u - uH_d}{u - d}$ for $V_0$ and substituting $\Delta = (H_u - H_d)/((u-d)S_0)$, the algebra collapses to the same formula obtained by [replication](replicating_portfolio.md):

$$
\boxed{V_0 = e^{-r\Delta t}(qH_u + (1-q)H_d)}, \qquad q := \frac{e^{r\Delta t} - d}{u - d}
$$

The risk-neutral probability $q$ **emerges from hedging** — it was not assumed.

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

**Verification:**

- Up state: $0.5 \times 120 - 15 = 45$ ✓
- Down state: $0.5 \times 90 - 0 = 45$ ✓
- Return: $45 / 42.80 = e^{0.05}$ ✓

!!! success "Result"
    The hedged portfolio earns exactly the risk-free rate in both states, confirming $C_0 = 7.20$.

### European Put Option

**Payoffs:**

$$
H_u = (105 - 120)^+ = 0, \qquad H_d = (105 - 90)^+ = 15
$$

**Delta:**

$$
\Delta = \frac{H_u - H_d}{(u - d)S_0} = \frac{0 - 15}{0.3 \times 100} = -0.5
$$

The negative delta means the put gains when the stock falls, so the hedge requires **shorting 0.5 shares** of stock.

**Hedged portfolio** (short 1 put, long $\Delta = -0.5$ shares, i.e., short 0.5 shares):

$$
\Pi_0 = \Delta S_0 - V_0 = -0.5 \times 100 - V_0 = -50 - V_0
$$

**Terminal values:**

$$
\Pi_{\Delta t}^{up} = -0.5 \times 120 - 0 = -60
$$

$$
\Pi_{\Delta t}^{down} = -0.5 \times 90 - 15 = -60 \checkmark
$$

The portfolio is risk-free with terminal value $-60$ (a liability — consistent with being short stock and short put).

**No-arbitrage** ($\Pi_{\Delta t} = \Pi_0 \cdot e^{r\Delta t}$):

$$
-60 = (-50 - V_0) \times e^{0.05}
$$

$$
-50 - V_0 = -60 \times e^{-0.05} = -57.07
$$

$$
V_0 = -50 + 57.07 = 7.07
$$

!!! success "European Put Price"

    $$P_0 = 7.07$$
    
    **Verification via risk-neutral pricing:**
    
    $$q = \frac{e^{0.05} - 0.9}{0.3} \approx 0.504$$
    
    $$P_0 = e^{-0.05}(0.504 \times 0 + 0.496 \times 15) = e^{-0.05} \times 7.44 \approx 7.08$$
    
    The tiny residual difference is due to rounding throughout; both methods are consistent.

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
| [Multi-Period Model](../multi_period_model/multi_period_binomial_model.md) | Dynamic delta hedging over multiple periods |
| [Binomial to Black–Scholes](../binomial_to_black_scholes/binomial_to_black_scholes_limit.md) | Continuous-time limit |

---

## Exercises

**Exercise 1.** In the one-period binomial model with $S_0 = 60$, $u = 1.3$, $d = 0.75$, $r = 6\%$, and $\Delta t = 1$, compute the hedge ratio $\Delta$ for a European call with strike $K = 65$. Construct the hedged portfolio (short 1 call, long $\Delta$ shares) and verify that it has the same terminal value in both states. Confirm that this terminal value equals $\Pi_0 \cdot e^{r\Delta t}$.

??? success "Solution to Exercise 1"
    Given $S_0 = 60$, $u = 1.3$, $d = 0.75$, $r = 6\%$, $\Delta t = 1$, and $K = 65$.

    **Stock prices at $\Delta t$:**

    - Up: $S_u = 1.3 \times 60 = 78$
    - Down: $S_d = 0.75 \times 60 = 45$

    **Call payoffs:**

    $$
    H_u = (78 - 65)^+ = 13, \qquad H_d = (45 - 65)^+ = 0
    $$

    **Hedge ratio:**

    $$
    \Delta = \frac{H_u - H_d}{(u - d)S_0} = \frac{13 - 0}{(1.3 - 0.75) \times 60} = \frac{13}{33} = 0.3939
    $$

    **Hedged portfolio** (short 1 call, long $\Delta$ shares):

    - Up state: $\Pi_{\Delta t}^{up} = 0.3939 \times 78 - 13 = 30.727 - 13 = 17.727$
    - Down state: $\Pi_{\Delta t}^{down} = 0.3939 \times 45 - 0 = 17.727$

    Both states give the same terminal value $\Pi_{\Delta t} = 17.727$ $\checkmark$

    **Verification** ($\Pi_{\Delta t} = \Pi_0 \cdot e^{r\Delta t}$):

    $$
    \Pi_0 = e^{-0.06} \times 17.727 = 0.94176 \times 17.727 = 16.695
    $$

    $$
    V_0 = \Delta S_0 - \Pi_0 = 0.3939 \times 60 - 16.695 = 23.636 - 16.695 = 6.94
    $$

    Check: $\Pi_0 \cdot e^{0.06} = 16.695 \times 1.06184 = 17.727$ $\checkmark$

---

**Exercise 2.** A derivative has the payoff $H_u = 5$ in the up state and $H_d = 20$ in the down state. Using $S_0 = 100$, $u = 1.2$, $d = 0.9$, $r = 5\%$, and $\Delta t = 1$, compute the hedge ratio $\Delta$. Explain the economic intuition for why $\Delta < 0$ in this case and describe what "short $\Delta$ shares" means in practice.

??? success "Solution to Exercise 2"
    Given $H_u = 5$, $H_d = 20$, $S_0 = 100$, $u = 1.2$, $d = 0.9$, $r = 5\%$, $\Delta t = 1$.

    **Hedge ratio:**

    $$
    \Delta = \frac{H_u - H_d}{(u - d)S_0} = \frac{5 - 20}{0.3 \times 100} = \frac{-15}{30} = -0.5
    $$

    **Economic intuition:** $\Delta < 0$ because the derivative pays **more when the stock falls** ($H_d = 20 > H_u = 5$). This is a "put-like" payoff pattern. To hedge a short position in this derivative, you need to **short stock** (not buy it), because when the stock falls you owe a larger payoff, and the short stock position gains to offset it.

    In practice, "short $\Delta = -0.5$ shares" means holding a **short position** of 0.5 shares. When paired with the short derivative position, if the stock falls, the short stock position gains value, offsetting the larger derivative payout. If the stock rises, the short stock position loses, but the derivative payout is smaller.

---

**Exercise 3.** Prove algebraically that the option pricing formula derived from the hedging argument:

$$
V_0 = e^{-r\Delta t}\left[\frac{e^{r\Delta t} - d}{u - d} H_u + \frac{u - e^{r\Delta t}}{u - d} H_d\right]
$$

is identical to the replication price $V_0 = \Delta S_0 + B$ where $\Delta = \frac{H_u - H_d}{(u-d)S_0}$ and $B = e^{-r\Delta t}\frac{uH_d - dH_u}{u-d}$.

??? success "Solution to Exercise 3"
    We show the hedging formula equals the replication price. Start from the hedging formula:

    $$
    V_0 = e^{-r\Delta t}\left[\frac{e^{r\Delta t} - d}{u - d} H_u + \frac{u - e^{r\Delta t}}{u - d} H_d\right]
    $$

    Expand:

    $$
    V_0 = \frac{1}{u - d}\left[\frac{(e^{r\Delta t} - d)H_u + (u - e^{r\Delta t})H_d}{e^{r\Delta t}}\right]
    $$

    $$
    = \frac{1}{u - d}\left[e^{-r\Delta t}(e^{r\Delta t} - d)H_u + e^{-r\Delta t}(u - e^{r\Delta t})H_d\right]
    $$

    $$
    = \frac{1}{u - d}\left[(1 - de^{-r\Delta t})H_u + (ue^{-r\Delta t} - 1)H_d\right]
    $$

    Now compute $\Delta S_0 + B$ from the replication formulas:

    $$
    \Delta S_0 = \frac{H_u - H_d}{u - d}
    $$

    $$
    B = e^{-r\Delta t}\frac{uH_d - dH_u}{u - d}
    $$

    $$
    \Delta S_0 + B = \frac{H_u - H_d}{u - d} + \frac{e^{-r\Delta t}(uH_d - dH_u)}{u - d}
    $$

    $$
    = \frac{(H_u - H_d) + e^{-r\Delta t}(uH_d - dH_u)}{u - d}
    $$

    $$
    = \frac{H_u(1 - de^{-r\Delta t}) + H_d(-1 + ue^{-r\Delta t})}{u - d}
    $$

    $$
    = \frac{(1 - de^{-r\Delta t})H_u + (ue^{-r\Delta t} - 1)H_d}{u - d}
    $$

    This is identical to the hedging formula above. $\square$

---

**Exercise 4.** Using the text's parameters ($S_0 = 100$, $u = 1.2$, $d = 0.9$, $r = 5\%$, $\Delta t = 1$), compute $\Delta$ for a forward contract with forward price $F = 105.13$. Explain why $\Delta = 1$ for a forward and relate this to the forward's payoff structure.

??? success "Solution to Exercise 4"
    A forward contract with forward price $F = 105.13$ has payoffs:

    $$
    H_u = uS_0 - F = 120 - 105.13 = 14.87, \qquad H_d = dS_0 - F = 90 - 105.13 = -15.13
    $$

    **Delta:**

    $$
    \Delta = \frac{H_u - H_d}{(u - d)S_0} = \frac{14.87 - (-15.13)}{0.3 \times 100} = \frac{30}{30} = 1
    $$

    **Why $\Delta = 1$:** A forward contract's payoff is $S_{\Delta t} - F$, which is **linear** in $S_{\Delta t}$ with slope 1. When the stock moves by $\delta S$, the forward payoff changes by exactly $\delta S$. The sensitivity of the forward to the stock is always 1 — holding 1 share perfectly hedges the forward.

    This makes economic sense: a forward is a commitment to buy the stock, so its price exposure is identical to holding the stock itself. The constant $F$ simply shifts the payoff level but does not change the sensitivity to stock price movements.

---

**Exercise 5.** Suppose an investor holds a portfolio of 100 European call options on a stock, each with the delta computed in the text ($\Delta = 0.5$). How many shares of the underlying stock should the investor hold (or short) to delta-hedge the entire position? If the stock price moves from $S_0 = 100$ to $S_0' = 102$, estimate the change in the portfolio value of the 100 calls using the delta approximation $\delta V \approx \Delta \cdot \delta S$.

??? success "Solution to Exercise 5"
    With $\Delta = 0.5$ per call and 100 calls:

    **Total delta exposure:** $100 \times 0.5 = 50$

    To delta-hedge, the investor should **short 50 shares** of the underlying stock. This offsets the positive delta of the long call position.

    **Delta approximation for stock move from $S_0 = 100$ to $S_0' = 102$:**

    $$
    \delta S = 102 - 100 = 2
    $$

    $$
    \delta V \approx \Delta \times \delta S = 0.5 \times 2 = 1 \text{ per call}
    $$

    For 100 calls:

    $$
    \delta V_{\text{total}} \approx 100 \times 1 = 100
    $$

    The estimated change in portfolio value is approximately \$100. This is a first-order approximation; the actual change also depends on the gamma (second-order term).

---

**Exercise 6.** Explain why the physical probability $p$ of an up move does not appear in the delta-hedging derivation. Specifically, show that the hedge ratio $\Delta$ and the resulting option price $V_0$ are the same regardless of whether $p = 0.3$, $p = 0.5$, or $p = 0.9$. What role does $p$ play in the real world, and why is it irrelevant for pricing?

??? success "Solution to Exercise 6"
    The physical probability $p$ does not appear because the hedging argument is based on **eliminating risk in every state**, not on the likelihood of each state.

    **Formal argument:** The hedge ratio is:

    $$
    \Delta = \frac{H_u - H_d}{(u - d)S_0}
    $$

    This depends only on the payoffs $(H_u, H_d)$ and the price factors $(u, d, S_0)$. The probability $p$ does not enter. The risk-free portfolio terminal value is:

    $$
    \Pi_{\Delta t} = \frac{dH_u - uH_d}{u - d}
    $$

    Again, no $p$. The no-arbitrage principle $\Pi_{\Delta t} = \Pi_0 e^{r\Delta t}$ then determines $V_0$ as:

    $$
    V_0 = e^{-r\Delta t}(qH_u + (1-q)H_d)
    $$

    where $q = (e^{r\Delta t} - d)/(u - d)$. Since $q$ depends only on $(u, d, r, \Delta t)$, neither $\Delta$ nor $V_0$ depends on $p$. Whether $p = 0.3$, $p = 0.5$, or $p = 0.9$, the formulas are identical.

    **Role of $p$ in the real world:** The physical probability $p$ determines:

    - The **expected return** of the option position: $\mathbb{E}^{\mathbb{P}}[H] = pH_u + (1-p)H_d$
    - The **probability of profit or loss** for unhedged positions
    - **Risk measures** like VaR and CVaR

    However, $p$ is irrelevant for pricing because the hedge works in **every** state. The option price is what it costs to set up the replicating portfolio, and this cost depends only on the structure of the market $(u, d, r)$, not on which outcome is more likely.
