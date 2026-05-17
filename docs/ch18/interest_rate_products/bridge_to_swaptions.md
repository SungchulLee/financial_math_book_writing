# From Swaps to Swaptions

!!! tip "Key Idea"
    A swaption is an option on a swap. It inherits the structure of swaps but introduces nonlinear payoff and volatility dependence — making it the interest rate analogue of a stock option.

Recall (see [§ Swap Valuation](swap_valuation.md)): a swap is a binding agreement whose value is $V_{\text{swap}} = N A_{m,n}(t)(S_{m,n}(t) - K)$. A **swaption** gives the holder the right, not the obligation, to enter such a swap in the future.

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

Recall (see [§ Interest Rate Swap](interest_rate_swap.md)): the swap rate $S_{m,n}(t)$ is a martingale under the annuity measure $\mathbb{Q}^A$ (numeraire $A_{m,n}(t)$), making it the natural underlying for swaption pricing — the swap-rate analogue of the $T_k$-forward martingale property in [§ Forward Rate Agreement](forward_rate_agreement.md).

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

Pricing swaptions requires three ingredients: forward swap rates (from the yield curve), a discounting framework (annuity measure), and volatility assumptions. The Black (1976) approach for European swaptions is developed in [§ Black Swaption Formula](../swaption_pricing/black_swaption_formula.md); short-rate alternatives in [§ General Short-Rate Framework](../short_rate_models/general_short_rate_framework.md); LMM in [§ Chapter 19](../../ch19/index.md).

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

---

**Exercise 5.** Using the annuity measure $\mathbb{Q}^A$ (numeraire $A_{m,n}(t)$), explain why the time-$t$ value of a European payer swaption with strike $K$ expiring at $T_m$ is

$$
V(t) = N A_{m,n}(t) \, \mathbb{E}^{\mathbb{Q}^A}\!\left[(S_{m,n}(T_m) - K)^+ \,\big|\, \mathcal{F}(t)\right]
$$

Identify why the discount factor in front of the expectation is the annuity factor rather than $P(t, T_m)$, and explain how this relates to the swap-rate martingale property.

??? success "Solution to Exercise 5"

    **Numeraire choice.** The annuity measure $\mathbb{Q}^A$ has numeraire $A_{m,n}(t) = \sum_{k=m+1}^n \tau_k P(t,T_k)$. By the change-of-numeraire theorem, for any traded asset $V(t)$:

    $$
    \frac{V(t)}{A_{m,n}(t)} = \mathbb{E}^{\mathbb{Q}^A}\!\left[\frac{V(T_m)}{A_{m,n}(T_m)} \,\Big|\, \mathcal{F}(t)\right]
    $$

    **Swaption payoff.** The payer swaption at expiry $T_m$ pays $V(T_m) = N A_{m,n}(T_m)(S_{m,n}(T_m) - K)^+$, so $V(T_m)/A_{m,n}(T_m) = N (S_{m,n}(T_m) - K)^+$. Multiplying both sides by $A_{m,n}(t)$:

    $$
    V(t) = N A_{m,n}(t) \, \mathbb{E}^{\mathbb{Q}^A}\!\left[(S_{m,n}(T_m) - K)^+ \,\big|\, \mathcal{F}(t)\right]
    $$

    **Why the annuity factor, not $P(t, T_m)$.** The payoff is not a single cash flow at $T_m$; it depends on a swap that pays from $T_{m+1}$ through $T_n$. The annuity factor aggregates the discount factors for the entire payment schedule, which is precisely the "right" discounting for swap-rate-based payoffs.

    **Swap-rate martingale property.** Under $\mathbb{Q}^A$, $S_{m,n}(t)$ is a martingale (recall [§ Interest Rate Swap](interest_rate_swap.md), Exercise 5). This means no drift correction is needed when modelling $S_{m,n}(t)$, e.g., as $dS = \sigma S \, dW^A$, leading directly to the Black (1976) formula for swaptions.

---

**Exercise 6.** Modelling the swap rate as geometric Brownian motion $dS_{m,n}(t) = \sigma S_{m,n}(t) \, dW^A(t)$ under $\mathbb{Q}^A$, derive the Black (1976) formula for a payer swaption:

$$
V_{\text{payer}}(t) = N A_{m,n}(t) \bigl[S_{m,n}(t) \Phi(d_1) - K \Phi(d_2)\bigr]
$$

where $d_1 = \frac{\ln(S/K) + \sigma^2 (T_m - t)/2}{\sigma \sqrt{T_m - t}}$ and $d_2 = d_1 - \sigma \sqrt{T_m - t}$. Why does this formula resemble Black–Scholes for stock options?

??? success "Solution to Exercise 6"

    **Setup.** Under $\mathbb{Q}^A$, with $S(t) := S_{m,n}(t)$ following $dS = \sigma S \, dW^A$, the log of $S(T_m)$ given $\mathcal{F}(t)$ is normal:

    $$
    \ln S(T_m) \sim \mathcal{N}\!\left(\ln S(t) - \tfrac{1}{2}\sigma^2 (T_m - t),\; \sigma^2 (T_m - t)\right)
    $$

    This is the same lognormal distribution that arises for stock prices in Black–Scholes (with $r = 0$ here because the swap rate is already a martingale under $\mathbb{Q}^A$).

    **Expectation of the payoff.** Writing $\tau := T_m - t$, the standard lognormal call-option computation gives:

    $$
    \mathbb{E}^{\mathbb{Q}^A}\!\left[(S(T_m) - K)^+ \,\big|\, \mathcal{F}(t)\right] = S(t) \Phi(d_1) - K \Phi(d_2)
    $$

    with

    $$
    d_1 = \frac{\ln(S(t)/K) + \tfrac{1}{2}\sigma^2 \tau}{\sigma \sqrt{\tau}}, \qquad d_2 = d_1 - \sigma \sqrt{\tau}
    $$

    Multiplying by the numeraire $N A_{m,n}(t)$ from Exercise 5:

    $$
    V_{\text{payer}}(t) = N A_{m,n}(t)\bigl[S(t) \Phi(d_1) - K \Phi(d_2)\bigr]
    $$

    **Why it looks like Black–Scholes.** Three correspondences make the formulas isomorphic:

    | Black–Scholes | Black (1976) for swaptions |
    |---|---|
    | Stock price $S_t$ (martingale under $\mathbb{Q}^*$ = $e^{-rt}$-numeraire) | Swap rate $S_{m,n}(t)$ (martingale under $\mathbb{Q}^A$) |
    | Discount factor $e^{-r(T-t)}$ | Annuity factor $A_{m,n}(t)$ |
    | Volatility $\sigma$ of $\ln S$ | Volatility $\sigma$ of $\ln S_{m,n}$ |

    The key insight is that choosing the annuity as numeraire eliminates the drift in $S_{m,n}(t)$, exactly as the bank-account numeraire eliminates drift (up to $r$) for $S_t$ in Black–Scholes. The remaining computation is identical: a lognormal call-option expectation.