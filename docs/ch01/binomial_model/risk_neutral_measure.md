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

$$
qu + (1-q)d = \frac{e^{r\Delta t} - d}{u - d} \cdot u + \frac{u - e^{r\Delta t}}{u - d} \cdot d
$$

$$
= \frac{(e^{r\Delta t} - d)u + (u - e^{r\Delta t})d}{u - d} = \frac{ue^{r\Delta t} - ud + ud - de^{r\Delta t}}{u - d}
$$

$$
= \frac{e^{r\Delta t}(u - d)}{u - d} = e^{r\Delta t}
$$

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

$$
V_0^{rep} = \frac{H_u - H_d}{(u-d)S_0} \cdot S_0 + e^{-r\Delta t}\left(H_u - \frac{H_u - H_d}{(u-d)S_0} \cdot uS_0\right)
$$

$$
= \frac{H_u - H_d}{u-d} + e^{-r\Delta t}\left(H_u - \frac{u(H_u - H_d)}{u-d}\right)
$$

$$
= \frac{H_u - H_d}{u-d} + e^{-r\Delta t}\left(\frac{(u-d)H_u - u(H_u - H_d)}{u-d}\right)
$$

$$
= \frac{H_u - H_d}{u-d} + e^{-r\Delta t}\left(\frac{uH_u - dH_u - uH_u + uH_d}{u-d}\right)
$$

$$
= \frac{H_u - H_d}{u-d} + e^{-r\Delta t}\left(\frac{uH_d - dH_u}{u-d}\right)
$$

**Risk-neutral price**:

$$
V_0^{RN} = e^{-r\Delta t}(qH_u + (1-q)H_d)
$$

$$
= e^{-r\Delta t}\left(\frac{e^{r\Delta t} - d}{u-d}H_u + \frac{u - e^{r\Delta t}}{u-d}H_d\right)
$$

$$
= e^{-r\Delta t}\left(\frac{(e^{r\Delta t} - d)H_u + (u - e^{r\Delta t})H_d}{u-d}\right)
$$

$$
= \frac{1}{u-d}\left(\frac{e^{r\Delta t} - d}{e^{r\Delta t}}H_u + \frac{u - e^{r\Delta t}}{e^{r\Delta t}}H_d\right)
$$

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
$$

$$
= e^{-0.05}(0.5043 \times 15 + 0.4957 \times 0)
$$

$$
= 0.9512 \times 7.565 = 7.19
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
$$

$$
= e^{-0.05}(0.5043 \times 0 + 0.4957 \times 15)
$$

$$
= 0.9512 \times 7.436 = 7.07
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
$$

$$
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
$$

$$
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

$$
C_0 - P_0 = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_{\Delta t} - K]
$$

$$
= e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] - Ke^{-r\Delta t}
$$

$$
= e^{-r\Delta t} \cdot S_0 e^{r\Delta t} - Ke^{-r\Delta t} = S_0 - Ke^{-r\Delta t}
$$

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

$$
V_0(\alpha H^{(1)} + \beta H^{(2)}) = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[\alpha H^{(1)} + \beta H^{(2)}]
$$

$$
= \alpha e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[H^{(1)}] + \beta e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[H^{(2)}]
$$

$$
= \alpha V_0(H^{(1)}) + \beta V_0(H^{(2)})
$$

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
