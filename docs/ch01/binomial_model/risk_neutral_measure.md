# Risk-Neutral Pricing

## Introduction

Risk-neutral pricing is one of the central principles of modern asset pricing:

> **In an arbitrage-free market, the price of a contingent claim equals the discounted expectation of its payoff under a risk-neutral measure.**

This section shows how the risk-neutral pricing formula emerges from no-arbitrage, proves its equivalence to replication, and applies it to price various derivatives.

!!! info "Prerequisites"
    - [Binomial Model](binomial_model.md) (market setup, risk-neutral probability)
    - [Replicating Portfolio](replicating_portfolio.md) (replication approach)
    - [Delta Hedging](delta_hedging.md) (hedging approach)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. State and apply the risk-neutral pricing formula
    2. Prove that risk-neutral pricing equals replication pricing
    3. Verify the martingale property of discounted prices
    4. Price calls, puts, digitals, and forwards using expectation
    5. Understand what risk-neutral probability is (and is not)

!!! note "Three Equivalent Approaches"
    This section presents the **risk-neutral pricing approach**. The same prices are obtained via:
    
    - [Replicating Portfolio](replicating_portfolio.md): Match payoffs with stock + bond
    - [Delta Hedging](delta_hedging.md): Construct risk-free hedged portfolio
    
    All three approaches yield identical prices.

---

## From Replication to Expectation

In the replication approach, we:

1. Find a portfolio $(\Delta, B)$ matching the payoff in all states
2. Set the price equal to the portfolio cost: $V_0 = \Delta S_0 + B$

Risk-neutral pricing asks a different question:

> *Is there a probability measure under which prices can be computed by expectation alone?*

The answer is **yes**, and that measure is uniquely determined by no-arbitrage.

---

## The Risk-Neutral Probability

### Definition

In the one-period binomial model with:

$$
S_{\Delta t} \in \{uS_0, \, dS_0\}, \qquad B_{\Delta t} = e^{r\Delta t}
$$

the **risk-neutral probability** of an up move is:

$$
\boxed{q = \frac{e^{r\Delta t} - d}{u - d}}
$$

### Properties

1. **Valid probability**: $0 < q < 1$ if and only if $d < e^{r\Delta t} < u$ (no-arbitrage condition)

2. **Model-dependent only**: $q$ depends only on $(u, d, r, \Delta t)$, not on the payoff being priced

3. **Unique**: There is exactly one value of $q$ satisfying the martingale condition

### The Risk-Neutral Measure

Define a probability measure $\mathbb{Q}$ on the state space $\{\text{up}, \text{down}\}$ by:

$$
\mathbb{Q}(\text{up}) = q, \qquad \mathbb{Q}(\text{down}) = 1 - q
$$

This is called the **risk-neutral measure** (or **equivalent martingale measure**).

---

## The Martingale Property

Under the risk-neutral measure $\mathbb{Q}$, the **discounted stock price** is a martingale.

### Verification

The expected stock price under $\mathbb{Q}$ is:

$$
\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] = q \cdot uS_0 + (1-q) \cdot dS_0 = S_0[qu + (1-q)d]
$$

Substituting $q = \frac{e^{r\Delta t} - d}{u - d}$:

$$\begin{array}{lll}
qu + (1-q)d 
&=&\displaystyle \frac{e^{r\Delta t} - d}{u - d} \cdot u + \frac{u - e^{r\Delta t}}{u - d} \cdot d\\
&=&\displaystyle \frac{(e^{r\Delta t} - d)u + (u - e^{r\Delta t})d}{u - d}\\ 
&=&\displaystyle \frac{ue^{r\Delta t} - ud + ud - de^{r\Delta t}}{u - d}\\
&=&\displaystyle \frac{e^{r\Delta t}(u - d)}{u - d} = e^{r\Delta t}
\end{array}$$

Therefore:

$$
\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] = S_0 \cdot e^{r\Delta t}
$$

Dividing both sides by $e^{r\Delta t}$:

!!! success "Martingale Property"

    $$
    \boxed{\mathbb{E}^{\mathbb{Q}}\left[\frac{S_{\Delta t}}{e^{r\Delta t}}\right] = S_0}
    $$
    
    The discounted stock price is a **martingale** under $\mathbb{Q}$.

**Interpretation**: Under $\mathbb{Q}$, the stock's expected return equals the risk-free rate. This is why $\mathbb{Q}$ is called "risk-neutral"—it's as if investors don't require any risk premium.

---

## The Risk-Neutral Pricing Formula

### Statement

For any contingent claim with payoff $H \in \{H_u, H_d\}$:

$$
\boxed{V_0 = e^{-r\Delta t} \mathbb{E}^{\mathbb{Q}}[H] = e^{-r\Delta t}(qH_u + (1-q)H_d)}
$$

### Proof of Equivalence to Replication

We show that the risk-neutral price equals the replication price.

**Replication price** (from [Replicating Portfolio](replicating_portfolio.md)):

$$
V_0^{rep} = \Delta S_0 + B
$$

where:

$$
\Delta = \frac{H_u - H_d}{(u-d)S_0}, \qquad B = e^{-r\Delta t}(H_u - \Delta \cdot uS_0)
$$

Substituting:

$$\begin{array}{lll}
V_0^{rep} 
&=&\displaystyle \frac{H_u - H_d}{(u-d)S_0} \cdot S_0 + e^{-r\Delta t}\left(H_u - \frac{H_u - H_d}{(u-d)S_0} \cdot uS_0\right)\\
&=&\displaystyle \frac{H_u - H_d}{u-d} + e^{-r\Delta t}\left(H_u - \frac{u(H_u - H_d)}{u-d}\right)\\
&=&\displaystyle \frac{H_u - H_d}{u-d} + e^{-r\Delta t}\left(\frac{(u-d)H_u - u(H_u - H_d)}{u-d}\right)\\
&=&\displaystyle \frac{H_u - H_d}{u-d} + e^{-r\Delta t}\left(\frac{uH_u - dH_u - uH_u + uH_d}{u-d}\right)\\
&=&\displaystyle \frac{H_u - H_d}{u-d} + e^{-r\Delta t}\left(\frac{uH_d - dH_u}{u-d}\right)
\end{array}$$

**Risk-neutral price**:

$$\begin{array}{lll}
V_0^{RN} 
&=&\displaystyle e^{-r\Delta t}(qH_u + (1-q)H_d)\\
&=&\displaystyle e^{-r\Delta t}\left(\frac{e^{r\Delta t} - d}{u-d}H_u + \frac{u - e^{r\Delta t}}{u-d}H_d\right)\\
&=&\displaystyle e^{-r\Delta t}\left(\frac{(e^{r\Delta t} - d)H_u + (u - e^{r\Delta t})H_d}{u-d}\right)\\
&=&\displaystyle \frac{1}{u-d}\left(\frac{e^{r\Delta t} - d}{e^{r\Delta t}}H_u + \frac{u - e^{r\Delta t}}{e^{r\Delta t}}H_d\right)
\end{array}$$

To show $V_0^{rep} = V_0^{RN}$, we can verify algebraically (or more simply, note that both give the unique no-arbitrage price, so they must be equal).

!!! success "Equivalence Theorem"

    $$
    V_0 = \Delta S_0 + B = e^{-r\Delta t}(qH_u + (1-q)H_d)
    $$
    
    **Replication pricing and risk-neutral pricing give the same answer.**

---

## Numerical Examples

We use consistent parameters throughout:

| Parameter | Value |
|-----------|-------|
| Initial stock price | $S_0 = 100$ |
| Up factor | $u = 1.2$ |
| Down factor | $d = 0.9$ |
| Risk-free rate | $r = 5\%$ |
| Time step | $\Delta t = 1$ year |
| Strike price | $K = 105$ |

**Computed values:**

$$
e^{r\Delta t} = e^{0.05} = 1.0513
$$

$$
q = \frac{1.0513 - 0.9}{1.2 - 0.9} = \frac{0.1513}{0.3} = 0.5043
$$

$$
1 - q = 0.4957
$$

---

## Example 1: European Call Option

### Payoffs

$$
S_{\Delta t}^{up} = 120, \quad S_{\Delta t}^{down} = 90
$$

$$
H_u = (120 - 105)^+ = 15, \qquad H_d = (90 - 105)^+ = 0
$$

### Risk-Neutral Price

$$
C_0 = e^{-r\Delta t}(qH_u + (1-q)H_d)
= e^{-0.05}(0.5043 \times 15 + 0.4957 \times 0)
= 7.19
$$

!!! success "European Call Price"

    $$C_0 = 7.19$$
    
    This matches the replication price from [Replicating Portfolio Pricing](replicating_portfolio.md).

---

## Example 2: European Put Option

### Payoffs

$$
H_u = (105 - 120)^+ = 0, \qquad H_d = (105 - 90)^+ = 15
$$

### Risk-Neutral Price

$$
P_0 = e^{-r\Delta t}(qH_u + (1-q)H_d)
= e^{-0.05}(0.5043 \times 0 + 0.4957 \times 15)
= 7.07
$$

!!! success "European Put Price"

    $$P_0 = 7.07$$

### Verification via Put–Call Parity

$$
C_0 - P_0 = 7.19 - 7.07 = 0.12
$$

$$
S_0 - Ke^{-r\Delta t} = 100 - 105 \times 0.9512 = 100 - 99.88 = 0.12 \text{ ✓}
$$

---

## Example 3: Digital (Binary) Call Option

A digital call pays $\$1$ if the stock is above the strike, and $\$0$ otherwise.

### Payoffs

$$
H_u = 1, \qquad H_d = 0
$$

### Risk-Neutral Price

$$
V_0 = e^{-r\Delta t}(q \cdot 1 + (1-q) \cdot 0) = e^{-r\Delta t} \cdot q
= 0.9512 \times 0.5043 = 0.48
$$

!!! success "Digital Call Price"

    $$V_0 = e^{-r\Delta t} q = 0.48$$
    
    **Key insight**: The price of a digital call equals the **discounted risk-neutral probability** of finishing in-the-money.
    
    This reveals the deep meaning of $q$: risk-neutral probabilities are **prices in disguise**.

---

## Example 4: Forward Contract

A forward contract obligates the holder to buy the stock at price $F$ at maturity.

### Payoff

$$
H = S_{\Delta t} - F
$$

$$
H_u = uS_0 - F = 120 - F, \qquad H_d = dS_0 - F = 90 - F
$$

### Risk-Neutral Price

$$
V_0 = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_{\Delta t} - F]
= e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] - e^{-r\Delta t}F
$$

Using $\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] = S_0 e^{r\Delta t}$ (martingale property):

$$
V_0 = e^{-r\Delta t} \cdot S_0 e^{r\Delta t} - Fe^{-r\Delta t} = S_0 - Fe^{-r\Delta t}
$$

### Forward Price

A forward contract has zero initial value by definition. Setting $V_0 = 0$:

$$
0 = S_0 - Fe^{-r\Delta t}
$$

$$
F = S_0 e^{r\Delta t} = 100 \times 1.0513 = 105.13
$$

!!! success "Forward Price"

    $$F = S_0 e^{r\Delta t} = 105.13$$
    
    The forward price is the spot price grown at the risk-free rate.

---

## Put–Call Parity via Risk-Neutral Pricing

### Derivation

For a call and put with the same strike $K$:

$$
C_0 - P_0 = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[(S_{\Delta t} - K)^+] - e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[(K - S_{\Delta t})^+]
$$

Using the identity $(S - K)^+ - (K - S)^+ = S - K$:

$$\begin{array}{lll}
C_0 - P_0 
&=&\displaystyle e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_{\Delta t} - K]\\
&=&\displaystyle e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] - Ke^{-r\Delta t}\\
&=&\displaystyle e^{-r\Delta t} \cdot S_0 e^{r\Delta t} - Ke^{-r\Delta t} = S_0 - Ke^{-r\Delta t}
\end{array}$$

!!! success "Put–Call Parity"

    $$
    \boxed{C_0 - P_0 = S_0 - Ke^{-r\Delta t}}
    $$
    
    Put–call parity is a **risk-neutral identity**—a direct consequence of the pricing formula.

---

## Linearity of Risk-Neutral Pricing

Risk-neutral pricing is **linear** in payoffs:

$$
V_0(\alpha H^{(1)} + \beta H^{(2)}) = \alpha V_0(H^{(1)}) + \beta V_0(H^{(2)})
$$

### Example: Bull Spread

A bull spread consists of:
- Long call with strike $K_1$
- Short call with strike $K_2 > K_1$

The price is:

$$
V_0^{bull} = C_0(K_1) - C_0(K_2)
$$

No additional calculation is needed—linearity allows decomposition of complex payoffs into simpler components.

### Why Linearity Holds

Linearity follows from the expectation operator:

$$\begin{array}{lll}
V_0(\alpha H^{(1)} + \beta H^{(2)})\\
&=&\displaystyle e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[\alpha H^{(1)} + \beta H^{(2)}]\\
&=&\displaystyle \alpha e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[H^{(1)}] + \beta e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[H^{(2)}]\\
&=&\displaystyle \alpha V_0(H^{(1)}) + \beta V_0(H^{(2)})
\end{array}$$

---

## What Risk-Neutral Probability Is (and Is Not)

### It IS:

| Property | Explanation |
|----------|-------------|
| A **pricing device** | Converts no-arbitrage pricing into an expectation calculation |
| An **equivalent martingale measure** | Makes discounted prices martingales |
| **Uniquely determined** | The no-arbitrage condition pins down exactly one $q$ |
| The **price of a digital** | $q = e^{r\Delta t} \times (\text{price of digital paying 1 in up state})$ |

### It IS NOT:

| Property | Explanation |
|----------|-------------|
| A **real-world probability** | The actual probability $p$ of an up move doesn't appear in pricing |
| A **forecast** | It doesn't predict which state will occur |
| A **subjective belief** | It's determined by market prices, not opinions |
| **Risk premium inclusive** | By construction, it removes risk premia |

!!! warning "Key Distinction"
    - **Physical measure $\mathbb{P}$**: Describes actual probabilities; used for forecasting and risk management
    - **Risk-neutral measure $\mathbb{Q}$**: Pricing device; used for derivative valuation
    
    The relationship between $\mathbb{P}$ and $\mathbb{Q}$ is the subject of [Girsanov's Theorem](../../ch04/girsanov/girsanov_theorem.md).

---

## Multi-Period Extension

In an $N$-period binomial tree, the risk-neutral pricing formula generalizes naturally.

### Terminal Payoffs

Let $V_{N,j}$ denote the payoff at terminal node $(N, j)$ (after $j$ up moves):

$$
V_{N,j} = H(S_0 u^j d^{N-j})
$$

### Risk-Neutral Pricing Formula

$$
\boxed{V_0 = e^{-rN\Delta t} \sum_{j=0}^{N} \binom{N}{j} q^j (1-q)^{N-j} V_{N,j}}
$$

where $\binom{N}{j} q^j (1-q)^{N-j}$ is the risk-neutral probability of reaching node $(N, j)$.

### Equivalence to Backward Induction

This formula is equivalent to backward induction:

$$
V_{n,j} = e^{-r\Delta t}(qV_{n+1,j+1} + (1-q)V_{n+1,j})
$$

Both methods give the same price. Backward induction is computationally more efficient for path-independent options, while the direct formula is useful for analysis.

See [Multi-Period Binomial Model](multi_period_binomial_model.md) for complete details.

---

## Summary

| Concept | Formula |
|---------|---------|
| Risk-neutral probability | $q = \dfrac{e^{r\Delta t} - d}{u - d}$ |
| Martingale property | $\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] = S_0 e^{r\Delta t}$ |
| Risk-neutral pricing | $V_0 = e^{-r\Delta t}(qH_u + (1-q)H_d)$ |
| Digital call price | $V_0 = e^{-r\Delta t} q$ |
| Forward price | $F = S_0 e^{r\Delta t}$ |
| Put–call parity | $C_0 - P_0 = S_0 - Ke^{-r\Delta t}$ |

!!! abstract "Key Takeaways"
    1. **Risk-neutral pricing = discounted expectation**: $V_0 = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[H]$
    
    2. **Equivalent to replication**: Risk-neutral pricing gives the same answer as constructing the replicating portfolio.
    
    3. **Martingale property**: Under $\mathbb{Q}$, discounted prices are martingales—the expected return equals the risk-free rate.
    
    4. **$q$ is a pricing device**: Risk-neutral probability is not a forecast of what will happen, but a tool for computing prices.
    
    5. **Linearity**: Complex payoffs can be priced by decomposition.
    
    6. **Extends to multi-period**: The same principle applies via backward induction or direct summation.

---

## What's Next

| Section | Topic |
|---------|-------|
| [Multi-Period Binomial Model](multi_period_binomial_model.md) | Backward induction in trees |
| [Binomial to Black–Scholes Limit](binomial_to_black_scholes_limit.md) | Continuous-time convergence |

---

## Exercises

**Exercise 1.** Consider a one-period binomial model with $S_0 = 50$, $u = 1.3$, $d = 0.8$, $r = 3\%$, and $\Delta t = 1$. Compute the risk-neutral probability $q$ and verify that $0 < q < 1$. Then price a European call with strike $K = 55$ using the risk-neutral pricing formula.

??? success "Solution to Exercise 1"
    Given $S_0 = 50$, $u = 1.3$, $d = 0.8$, $r = 3\%$, $\Delta t = 1$.

    **Risk-neutral probability:**

    $$
    q = \frac{e^{0.03} - 0.8}{1.3 - 0.8} = \frac{1.03045 - 0.8}{0.5} = \frac{0.23045}{0.5} = 0.4609
    $$

    **Verify $0 < q < 1$:** $0 < 0.4609 < 1$ $\checkmark$

    **Stock prices at $\Delta t$:** $S_u = 65$, $S_d = 40$.

    **Call payoffs** ($K = 55$):

    $$
    H_u = (65 - 55)^+ = 10, \qquad H_d = (40 - 55)^+ = 0
    $$

    **Risk-neutral price:**

    $$
    C_0 = e^{-0.03}(0.4609 \times 10 + 0.5391 \times 0) = 0.97045 \times 4.609 = 4.47
    $$

---

**Exercise 2.** In the standard one-period binomial model, prove that the risk-neutral pricing formula $V_0 = e^{-r\Delta t}(qH_u + (1-q)H_d)$ is a **linear** functional of the payoff vector $(H_u, H_d)$. That is, show that for any payoffs $H^{(1)}$, $H^{(2)}$ and scalars $\alpha$, $\beta$:

$$
V_0(\alpha H^{(1)} + \beta H^{(2)}) = \alpha V_0(H^{(1)}) + \beta V_0(H^{(2)})
$$

Explain why this property is economically important for pricing portfolios of derivatives.

??? success "Solution to Exercise 2"
    The risk-neutral pricing formula is $V_0(H) = e^{-r\Delta t}(qH_u + (1-q)H_d)$. For payoffs $H^{(1)} = (H_u^{(1)}, H_d^{(1)})$ and $H^{(2)} = (H_u^{(2)}, H_d^{(2)})$ and scalars $\alpha, \beta$:

    $$
    V_0(\alpha H^{(1)} + \beta H^{(2)}) = e^{-r\Delta t}\bigl(q(\alpha H_u^{(1)} + \beta H_u^{(2)}) + (1-q)(\alpha H_d^{(1)} + \beta H_d^{(2)})\bigr)
    $$

    $$
    = e^{-r\Delta t}\bigl(\alpha(qH_u^{(1)} + (1-q)H_d^{(1)}) + \beta(qH_u^{(2)} + (1-q)H_d^{(2)})\bigr)
    $$

    $$
    = \alpha \, e^{-r\Delta t}(qH_u^{(1)} + (1-q)H_d^{(1)}) + \beta \, e^{-r\Delta t}(qH_u^{(2)} + (1-q)H_d^{(2)})
    $$

    $$
    = \alpha \, V_0(H^{(1)}) + \beta \, V_0(H^{(2)})
    $$

    **Economic importance:** Linearity means that a portfolio of derivatives can be priced by summing the individual prices. This allows traders to decompose complex payoffs into simpler components (calls, puts, digitals), price each piece separately, and sum. It also implies that hedging a portfolio is equivalent to hedging each component, and that there are no "portfolio effects" in arbitrage-free pricing.

---

**Exercise 3.** A **straddle** consists of a long call and a long put with the same strike $K$. Using the parameters $S_0 = 100$, $u = 1.2$, $d = 0.9$, $r = 5\%$, $\Delta t = 1$, and $K = 105$, compute the risk-neutral price of the straddle in two ways: (a) by pricing the straddle payoff directly, and (b) by summing the individual call and put prices. Verify that both methods agree.

??? success "Solution to Exercise 3"
    With $S_0 = 100$, $u = 1.2$, $d = 0.9$, $r = 5\%$, $\Delta t = 1$, $K = 105$, and $q = 0.5043$.

    **Straddle payoff** = call payoff + put payoff:

    - Up: $H_u = (120 - 105)^+ + (105 - 120)^+ = 15 + 0 = 15$
    - Down: $H_d = (90 - 105)^+ + (105 - 90)^+ = 0 + 15 = 15$

    **(a) Direct pricing:**

    $$
    V_0^{\text{straddle}} = e^{-0.05}(0.5043 \times 15 + 0.4957 \times 15) = e^{-0.05} \times 15 = 0.9512 \times 15 = 14.27
    $$

    **(b) Sum of individual prices:**

    $$
    C_0 = e^{-0.05}(0.5043 \times 15 + 0.4957 \times 0) = 0.9512 \times 7.5645 = 7.19
    $$

    $$
    P_0 = e^{-0.05}(0.5043 \times 0 + 0.4957 \times 15) = 0.9512 \times 7.4355 = 7.07
    $$

    $$
    C_0 + P_0 = 7.19 + 7.07 = 14.26
    $$

    Both methods agree (up to rounding). $\checkmark$

    Note: in this particular example, the straddle pays 15 in both states, making it equivalent to a deterministic payoff. Its price equals $15 \times e^{-r\Delta t}$, which is just the present value of \$15.

---

**Exercise 4.** Prove that in the one-period binomial model, the risk-neutral probability $q$ satisfies $0 < q < 1$ if and only if the no-arbitrage condition $d < e^{r\Delta t} < u$ holds. What happens to the pricing formula if $q \leq 0$ or $q \geq 1$?

??? success "Solution to Exercise 4"
    The risk-neutral probability is $q = \frac{e^{r\Delta t} - d}{u - d}$.

    **($\Rightarrow$)** Assume $d < e^{r\Delta t} < u$. Then:

    - Numerator: $e^{r\Delta t} - d > 0$ (since $e^{r\Delta t} > d$)
    - Denominator: $u - d > 0$ (since $u > d$)
    - So $q > 0$

    Also $e^{r\Delta t} - d < u - d$ (since $e^{r\Delta t} < u$), so $q < 1$. Hence $0 < q < 1$.

    **($\Leftarrow$)** Assume $q \in (0,1)$.

    - $q > 0$ means $e^{r\Delta t} - d > 0$, so $e^{r\Delta t} > d$
    - $q < 1$ means $e^{r\Delta t} - d < u - d$, so $e^{r\Delta t} < u$

    **What if $q \leq 0$ or $q \geq 1$:**

    If $q \leq 0$, then $e^{r\Delta t} \leq d$, meaning the risk-free rate dominates even the worst stock return. The "risk-neutral measure" assigns zero or negative weight to the up state, so it is not a valid probability. Arbitrage exists: buy stock financed by borrowing.

    If $q \geq 1$, then $e^{r\Delta t} \geq u$, meaning the risk-free rate dominates even the best stock return. The measure assigns zero or negative weight to the down state. Arbitrage exists: short stock and invest in the bank.

    In both cases, the pricing formula breaks down because no equivalent martingale measure exists.

---

**Exercise 5.** A digital put pays $\$1$ if the stock finishes below the strike and $\$0$ otherwise. Using the same parameters as in the text ($S_0 = 100$, $u = 1.2$, $d = 0.9$, $r = 5\%$, $\Delta t = 1$, $K = 105$), compute the digital put price. Show that the sum of the digital call price and the digital put price equals $e^{-r\Delta t}$, and explain why this identity must hold.

??? success "Solution to Exercise 5"
    A digital put pays $H_u = 0$ (stock above strike) and $H_d = 1$ (stock below strike), with $K = 105$.

    Since $S_u = 120 > 105$ and $S_d = 90 < 105$:

    $$
    V_0^{\text{dig put}} = e^{-r\Delta t}(q \times 0 + (1-q) \times 1) = e^{-0.05}(1 - q) = 0.9512 \times 0.4957 = 0.4716
    $$

    **Digital call price** (from the text): $V_0^{\text{dig call}} = e^{-r\Delta t} q = 0.9512 \times 0.5043 = 0.4797$.

    **Sum:**

    $$
    V_0^{\text{dig call}} + V_0^{\text{dig put}} = 0.4797 + 0.4716 = 0.9513 \approx e^{-0.05} = 0.9512
    $$

    (The small difference is due to rounding.) $\checkmark$

    **Why this must hold:** A portfolio of one digital call and one digital put pays \$1 in **every** state (if the stock is above the strike, the digital call pays 1; if below, the digital put pays 1). This combined payoff is equivalent to a zero-coupon bond paying \$1 at maturity. By no-arbitrage, its price must equal $e^{-r\Delta t}$, the discount factor.

---

**Exercise 6.** Suppose a one-period binomial model has $S_0 = 100$, $u = 1.15$, $d = 0.85$, $r = 2\%$, and $\Delta t = 0.5$. An exotic derivative pays $H = S_{\Delta t}^2 / S_0$ in both states. Compute the risk-neutral price $V_0$ and the replicating portfolio $(\Delta, B)$. Verify that the replication price equals the risk-neutral price.

??? success "Solution to Exercise 6"
    Given $S_0 = 100$, $u = 1.15$, $d = 0.85$, $r = 2\%$, $\Delta t = 0.5$.

    **Stock prices:** $S_u = 115$, $S_d = 85$.

    **Payoffs:** $H = S_{\Delta t}^2 / S_0$:

    $$
    H_u = \frac{115^2}{100} = \frac{13225}{100} = 132.25, \qquad H_d = \frac{85^2}{100} = \frac{7225}{100} = 72.25
    $$

    **Risk-neutral probability:**

    $$
    q = \frac{e^{0.02 \times 0.5} - 0.85}{1.15 - 0.85} = \frac{e^{0.01} - 0.85}{0.30} = \frac{1.01005 - 0.85}{0.30} = \frac{0.16005}{0.30} = 0.5335
    $$

    **Risk-neutral price:**

    $$
    V_0 = e^{-0.01}(0.5335 \times 132.25 + 0.4665 \times 72.25)
    $$

    $$
    = 0.99005 \times (70.54 + 33.70) = 0.99005 \times 104.24 = 103.21
    $$

    **Replicating portfolio:**

    $$
    \Delta = \frac{H_u - H_d}{(u-d)S_0} = \frac{132.25 - 72.25}{0.30 \times 100} = \frac{60}{30} = 2.0
    $$

    $$
    B = e^{-0.01}\left(\frac{1.15 \times 72.25 - 0.85 \times 132.25}{0.30}\right) = 0.99005 \times \frac{83.09 - 112.41}{0.30} = 0.99005 \times (-97.73) = -96.76
    $$

    **Replication price:**

    $$
    V_0^{rep} = \Delta S_0 + B = 2.0 \times 100 + (-96.76) = 200 - 96.76 = 103.24
    $$

    The risk-neutral price and replication price agree (up to rounding). $\checkmark$
