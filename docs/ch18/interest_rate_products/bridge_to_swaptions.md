# From Swaps to Swaptions

!!! tip "Key Idea"
    A swaption is an option on a swap. It inherits the structure of swaps but introduces nonlinear payoff and volatility dependence — making it the interest rate analogue of a stock option.

A swap is a binding agreement to exchange fixed and floating payments. But what if a trader wants the **right**, not the obligation, to enter a swap in the future? This leads to the concept of a **swaption**.

---

## Definition

A **swaption** is an option that gives its holder the right to enter into an interest rate swap at a specified future date.

Two main types:

- **Payer swaption:** right to enter a swap paying fixed, receiving floating  
- **Receiver swaption:** right to receive fixed, pay floating  

---

## Payoff Structure

Let $S_T$ denote the swap rate at option maturity.

For a payer swaption:

$$
\text{Payoff} = N A \, (S_T - K)^+
$$

where:
- $A$ is the swap annuity
- $K$ is the strike rate

---

## Key Contrast with Swaps

| Instrument | Payoff | Nature |
|-----------|-------|-------|
| Swap | Linear | Obligation |
| Swaption | Nonlinear | Optional |

- Swap payoff: symmetric, linear  
- Swaption payoff: asymmetric, convex  

---

## Interpretation

The swaption payoff resembles a call option:

- underlying: **swap rate**
- payoff: convex function of rate
- value depends on **volatility**

---

!!! tip "Key Idea"
    A swaption is to swaps what an option is to forwards: it introduces convexity and makes pricing depend on volatility.

---

## From Black–Scholes to Black Model

In equity markets:

- option on stock → Black–Scholes model  

In interest rate markets:

- option on forward/swap rate → **Black (1976) model**

The pricing principle remains the same:

- choose a numéraire  
- express payoff in forward measure  
- take expectation  

---

## Conceptual Bridge

The transition follows the same pattern as in Chapter 6:

| Chapter 6 | Chapter 18 |
|----------|-----------|
| Forward | Swap |
| Option | Swaption |
| Linear payoff | Linear cash flow stream |
| Convex payoff | Convex function of swap rate |

---

## Why This Matters

Swaptions are among the most actively traded instruments in fixed income markets. They serve three critical functions: hedging interest rate risk (a corporate treasurer can lock in the right to enter a favorable swap), trading volatility (swaption prices directly encode the market's view of rate uncertainty), and calibrating interest rate models (swaption prices are the primary targets against which term structure models are fitted).

Pricing swaptions requires three ingredients: forward swap rates (from the yield curve), a discounting framework (annuity measure), and volatility assumptions. Depending on how volatility is modeled, this leads to the Black (1976) model for simple European swaptions, short-rate models (Vasicek, CIR, Hull-White) for path-dependent products, or LIBOR market models (LMM) for joint dynamics of multiple forward rates.

---

!!! note "Big Picture"
    Swaps demonstrated that derivative pricing can be reduced to discounting known cash flows. Swaptions extend this idea by introducing optionality, requiring probabilistic modeling of future rates. This mirrors the fundamental transition from linear pricing (deterministic structure) to nonlinear pricing (stochastic dynamics).

---

## Exercises

**Exercise 1.** A 1-year into 3-year payer swaption has strike $K = 3.5\%$. At the swaption maturity ($T = 1$), the prevailing 3-year par swap rate is $S_T = 4.2\%$ and the swap annuity factor is $A = 2.75$. The notional is $N = 10{,}000{,}000$. Compute the swaption payoff.

??? success "Solution to Exercise 1"
    The payer swaption payoff is:

    $$
    N A (S_T - K)^+ = 10{,}000{,}000 \times 2.75 \times (0.042 - 0.035)^+ = 10{,}000{,}000 \times 2.75 \times 0.007 = 192{,}500
    $$

    The swaption holder exercises and enters a payer swap paying 3.5% while the market rate is 4.2%, locking in a favorable below-market fixed rate.

---

**Exercise 2.** If the swap rate at expiry in Exercise 1 were $S_T = 3.0\%$ instead, what would the swaption payoff be? Explain the holder's decision.

??? success "Solution to Exercise 2"
    $$
    N A (S_T - K)^+ = 10{,}000{,}000 \times 2.75 \times (0.030 - 0.035)^+ = 10{,}000{,}000 \times 2.75 \times 0 = 0
    $$

    The holder does not exercise. Entering a payer swap at 3.5% when the market rate is only 3.0% would mean overpaying on the fixed leg. The swaption expires worthless and the holder loses only the premium paid at inception.

---

**Exercise 3.** Explain the analogy between the transition from forwards to options (Chapter 6) and the transition from swaps to swaptions. In each case, identify what plays the role of the underlying, what creates nonlinearity, and what new parameter the pricing depends on.

??? success "Solution to Exercise 3"
    | | Chapter 6 | Chapter 18 |
    |---|---|---|
    | Linear instrument | Forward contract | Interest rate swap |
    | Underlying | Stock price $S_T$ | Swap rate $S_T$ |
    | Option instrument | Call/put option | Payer/receiver swaption |
    | Source of nonlinearity | $(S_T - K)^+$ payoff | $(S_T - K)^+$ applied to swap rate |
    | New parameter | Volatility $\sigma$ of stock | Volatility $\sigma$ of swap rate |
    | Pricing method | Black-Scholes PDE | Black (1976) model under annuity measure |

    In both cases, the transition from linear to nonlinear payoff means that static replication no longer suffices and pricing becomes dependent on volatility. The forward/swap determines the level; the option/swaption adds convexity.

---

**Exercise 4.** A receiver swaption gives the right to enter a swap receiving fixed at rate $K$. Write down the payoff formula for a receiver swaption and show that payer-receiver swaption parity holds:

$$
V_{\text{payer}}(K) - V_{\text{receiver}}(K) = V_{\text{swap}}(K)
$$

where $V_{\text{swap}}(K)$ is the value of a payer swap with fixed rate $K$.

??? success "Solution to Exercise 4"
    The receiver swaption payoff is:

    $$
    N A (K - S_T)^+
    $$

    The holder exercises when $S_T < K$ (receiving an above-market fixed rate is valuable).

    For parity, note that the payer payoff minus the receiver payoff is:

    $$
    N A (S_T - K)^+ - N A (K - S_T)^+ = N A (S_T - K)
    $$

    using the identity $(x)^+ - (-x)^+ = x$. But $N A (S_T - K)$ is exactly the value at time $T$ of a payer swap with fixed rate $K$. Discounting to time 0:

    $$
    V_{\text{payer}}(K) - V_{\text{receiver}}(K) = V_{\text{swap}}(K)
    $$

    This is the swaption analogue of put-call parity. $\square$