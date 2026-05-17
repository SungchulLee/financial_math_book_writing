# Annuity Measure and Change of Numeraire

!!! tip "Key Idea"
    Choosing the right numeraire simplifies pricing. Under the annuity measure, the swap rate becomes a martingale, making swaption pricing tractable.

---

## Motivation

In interest rate markets, different choices of numeraire lead to different probability measures. The key idea is:

> By selecting an appropriate numeraire, we can transform asset prices into martingales under the associated measure.

This simplifies the computation of expectations.

---

## Change of Numeraire

Recall (see [§ Risk-Neutral / Forward Measure](../../ch04/risk_neutral/forward_measure.md)) that for any strictly positive tradable numeraire $N(t)$ there is a measure $\mathbb{Q}^N$ under which $X(t)/N(t)$ is a martingale for every tradable $X(t)$. The relevant numeraire / measure / martingale triples are:

| Numeraire | Measure | Martingale |
|----------|--------|-----------|
| Money market account | Risk-neutral | Discounted asset prices |
| Zero-coupon bond $P(t,T)$ | $T$-forward measure | Forward prices |
| Swap annuity $A(t)$ | **Annuity measure** | Swap rate |

---

## The Swap Annuity

For a swap with payment dates $T_{m+1}, \dots, T_n$, define:

$$
A_{m,n}(t) = \sum_{k=m+1}^n \tau_k P(t, T_k)
$$

This is the present value of a unit fixed-rate leg.

---

## Annuity Measure

Take the annuity $A_{m,n}(t)$ as numeraire.

Under the associated measure $\mathbb{Q}^A$:

$$
\frac{X(t)}{A_{m,n}(t)}
$$

is a martingale for any tradable $X(t)$.

---

## Swap Rate as a Martingale

Recall the swap rate:

$$
S_{m,n}(t) = \frac{P(t,T_m) - P(t,T_n)}{A_{m,n}(t)}
$$

Under the annuity measure:

$$
S_{m,n}(t) \text{ is a martingale under } \mathbb{Q}^A
$$

---

!!! tip "Key Idea"
    The swap rate becomes a martingale only under the annuity measure. This is why it is the natural underlying for swaption pricing.

---

## Pricing with the Annuity Measure

Consider a payoff at time $T_m$:

$$
V(T_m) = N\,A_{m,n}(T_m)\,g(S_{m,n}(T_m))
$$

Then its value at time $t$ is:

$$
V(t) = N\,A_{m,n}(t)\,\mathbb{E}^{\mathbb{Q}^A}\bigl[g(S_{m,n}(T_m)) \mid \mathcal{F}_t\bigr]
$$

---

## Interpretation

- The annuity plays the role of a **discount factor for the swap cash-flow stream**
- The swap rate behaves like a **forward price**
- Pricing reduces to an expectation of a function of a martingale

---

## Connection to Chapter 6

Recall (see [§ Black Formula](../../ch06/index.md)) the forward-measure analogue: forward price is a martingale under the $T$-forward measure, giving the Black formula. The annuity measure plays the exact same role for the swap rate, leading to the Black swaption formula.

---

## Why This Matters

Without the change of numeraire:

- swap rate has drift
- pricing becomes complicated

With the annuity measure:

- drift disappears
- pricing reduces to Black-type formula

---

!!! note "Big Picture"
    The choice of numeraire is not a technical trick but a structural principle:

    > choose the numeraire that matches the payoff structure.

    For swaptions, the annuity is the natural choice because the payoff is proportional to the annuity.

---

## Exercises

**Exercise 1.** Show that the swap rate $S_{m,n}(t) = \frac{P(t,T_m) - P(t,T_n)}{A_{m,n}(t)}$ is a martingale under the annuity measure $\mathbb{Q}^A$. Identify the numeraire and verify that the numerator $P(t,T_m) - P(t,T_n)$ is a tradable asset.

??? success "Solution"
    Under any measure $\mathbb{Q}^N$ associated with numeraire $N(t)$, the ratio $X(t)/N(t)$ is a martingale for every tradable asset $X(t)$. Take $N(t) = A_{m,n}(t)$ (the swap annuity) and $X(t) = P(t,T_m) - P(t,T_n)$ (the value of the floating leg minus fixed-leg principal exchange). Both $P(t,T_m)$ and $P(t,T_n)$ are prices of tradable zero-coupon bonds, so their difference is the value of a self-financing portfolio and hence tradable. Therefore:

    $$
    \frac{X(t)}{A_{m,n}(t)} = \frac{P(t,T_m) - P(t,T_n)}{A_{m,n}(t)} = S_{m,n}(t)
    $$

    is a $\mathbb{Q}^A$-martingale by the fundamental theorem of asset pricing applied with numeraire $A_{m,n}(t)$. In particular:

    $$
    \mathbb{E}^{\mathbb{Q}^A}\bigl[S_{m,n}(T) \mid \mathcal{F}_t\bigr] = S_{m,n}(t)
    $$

    for all $t \le T \le T_m$. $\square$

---

**Exercise 2.** Explain why the swap rate $S_{m,n}(t)$ is *not* a martingale under the risk-neutral (money-market) measure $\mathbb{Q}$. What additional drift term arises, and why does this complicate swaption pricing?

??? success "Solution"
    Under the risk-neutral measure $\mathbb{Q}$, the numeraire is the money-market account $B(t) = \exp\!\bigl(\int_0^t r(s)\,ds\bigr)$. The ratio $X(t)/B(t)$ is a martingale for any tradable $X(t)$. Consider the discounted annuity $A_{m,n}(t)/B(t)$ and the discounted floating-leg value $[P(t,T_m) - P(t,T_n)]/B(t)$; both are $\mathbb{Q}$-martingales individually.

    However, the swap rate is a *ratio* of two such quantities:

    $$
    S_{m,n}(t) = \frac{P(t,T_m) - P(t,T_n)}{A_{m,n}(t)}
    $$

    A ratio of two martingales is generally not a martingale. By Ito's quotient rule, $S_{m,n}(t)$ acquires a drift under $\mathbb{Q}$ that involves the covariance between the numerator and denominator. Specifically, the drift depends on the stochastic dynamics of the annuity factor itself.

    This complicates swaption pricing because the expectation $\mathbb{E}^{\mathbb{Q}}[\cdot]$ of the payoff cannot be written as a simple function of $S_{m,n}(t)$ alone --- one must also model the joint dynamics of the annuity and the discount factor. The annuity measure eliminates this difficulty by absorbing the annuity into the numeraire, making the swap rate driftless. $\square$

---

**Exercise 3.** Let $g$ be a general payoff function of the swap rate. Using the annuity measure, derive the pricing formula for a derivative with time-$T_m$ payoff $V(T_m) = A_{m,n}(T_m)\,g\!\bigl(S_{m,n}(T_m)\bigr)$. Express the time-$t$ value $V(t)$ and explain why no explicit model for $A_{m,n}$ is needed.

??? success "Solution"
    By the change-of-numeraire pricing formula with numeraire $A_{m,n}(t)$, the time-$t$ value of any time-$T_m$ payoff $V(T_m)$ is:

    $$
    V(t) = A_{m,n}(t)\,\mathbb{E}^{\mathbb{Q}^A}\!\left[\frac{V(T_m)}{A_{m,n}(T_m)}\;\bigg|\;\mathcal{F}_t\right]
    $$

    Substituting $V(T_m) = A_{m,n}(T_m)\,g\!\bigl(S_{m,n}(T_m)\bigr)$:

    $$
    V(t) = A_{m,n}(t)\,\mathbb{E}^{\mathbb{Q}^A}\!\left[\frac{A_{m,n}(T_m)\,g(S_{m,n}(T_m))}{A_{m,n}(T_m)}\;\bigg|\;\mathcal{F}_t\right] = A_{m,n}(t)\,\mathbb{E}^{\mathbb{Q}^A}\!\bigl[g(S_{m,n}(T_m)) \mid \mathcal{F}_t\bigr]
    $$

    The annuity $A_{m,n}(T_m)$ cancels in numerator and denominator, so the expectation depends only on the distribution of $S_{m,n}(T_m)$ under $\mathbb{Q}^A$. Since $S_{m,n}(t)$ is a $\mathbb{Q}^A$-martingale, we need only specify its volatility structure (not the full term-structure dynamics of $A_{m,n}$). For example, if $S_{m,n}$ follows a lognormal process under $\mathbb{Q}^A$, the expectation reduces to a Black-type formula regardless of how the annuity evolves. $\square$

---

**Exercise 4.** Compare the $T$-forward measure (with numeraire $P(t,T)$) and the annuity measure (with numeraire $A_{m,n}(t)$). For each measure, state (a) the martingale quantity, (b) the natural derivative it prices, and (c) why one cannot simply use the forward measure to price swaptions.

??? success "Solution"
    **(a) Martingale quantities.**

    - Under the $T$-forward measure $\mathbb{Q}^T$ with numeraire $P(t,T)$, the forward price $F(t,T) = X(t)/P(t,T)$ of any tradable asset $X$ is a martingale.
    - Under the annuity measure $\mathbb{Q}^A$ with numeraire $A_{m,n}(t)$, the swap rate $S_{m,n}(t) = [P(t,T_m) - P(t,T_n)]/A_{m,n}(t)$ is a martingale.

    **(b) Natural derivatives.**

    - The forward measure is the natural setting for pricing caplets and floorlets, whose payoffs at a single date $T$ are functions of a single forward rate $F(t;T_{k-1},T_k)$.
    - The annuity measure is the natural setting for pricing swaptions, whose payoffs are proportional to the annuity factor and depend on the swap rate.

    **(c) Why the forward measure fails for swaptions.**

    A swaption payoff at exercise date $T_m$ is:

    $$
    V(T_m) = A_{m,n}(T_m)\,\bigl(S_{m,n}(T_m) - K\bigr)^+
    $$

    Under the $T_m$-forward measure with numeraire $P(t,T_m)$, the pricing formula becomes:

    $$
    V(t) = P(t,T_m)\,\mathbb{E}^{\mathbb{Q}^{T_m}}\!\left[\frac{A_{m,n}(T_m)}{P(T_m,T_m)}\bigl(S_{m,n}(T_m) - K\bigr)^+\;\bigg|\;\mathcal{F}_t\right]
    $$

    The ratio $A_{m,n}(T_m)/P(T_m,T_m)$ does not cancel and is stochastic, so we must model the joint distribution of $A_{m,n}(T_m)$ and $S_{m,n}(T_m)$. Moreover, $S_{m,n}(t)$ is not a martingale under $\mathbb{Q}^{T_m}$ (it acquires a drift), preventing a clean Black-type formula. By contrast, the annuity measure eliminates $A_{m,n}$ from the expectation and makes $S_{m,n}$ driftless, yielding the standard Black swaption formula directly. $\square$
