# Replicating Portfolio and Pricing 

This section develops **replication-based pricing** in the one-period binomial model and illustrates it through a sequence of concrete examples.

The key message is simple and powerful:

> **In a complete market, the price of a contingent claim equals the cost of a portfolio that replicates its payoff.**

---

## 1. Payoff Space and Completeness

In the one-period binomial model, the terminal payoff space is **two-dimensional**:

$$
H = (H_u, H_d)
$$

Any two linearly independent payoffs form a basis of this space.
Because the stock and bond generate two independent payoffs, the market is **complete**.

As a consequence:

* every contingent claim can be replicated,

* the no-arbitrage price is **unique**.

---

## 2. Replication Using Stock and Bond

Let a claim have payoff

$$
H = \left\{
\begin{array}{ll}
H_u & \text{up} \\
H_d & \text{down}
\end{array}
\right.
$$

We seek a portfolio ($\Delta,\beta$) such that

$$
\begin{aligned}
\Delta uS_0 + \beta e^{r dt} &= H_u \\
\Delta dS_0 + \beta e^{r dt} &= H_d
\end{aligned}
$$

Solving,

$$
\boxed{
\Delta = \frac{H_u - H_d}{(u-d)S_0}
}
\qquad
\boxed{
\beta = \frac{H_u - \Delta uS_0}{e^{r dt}}
}
$$

The **replication price** is

$$
\boxed{
V_0 = \Delta S_0 + \beta
}
$$

This price is forced by no-arbitrage.

---

## 3. Example 1: European Call Option

### Setup

Let

$$
S_0 = 100, \quad u = 1.2, \quad d = 0.9, \quad r = 0.05, \quad dt = 1, \quad K = 105
$$

Then $e^{r dt} = e^{0.05} \approx 1.0513$.

Payoffs:

$$
C_u = (120 - 105)^+ = 15, \qquad
C_d = (90 - 105)^+ = 0
$$

---

### Replication

$$
\Delta = \frac{15 - 0}{(1.2 - 0.9)\cdot 100} = \frac{15}{30} = 0.5
$$

$$
\beta
= \frac{15 - 0.5 \cdot 120}{e^{0.05}}
= \frac{-45}{1.0513}
\approx -42.86
$$

---

### Price

$$
C_0 = 0.5 \cdot 100 - 42.86 = 7.14
$$

**Interpretation**:

* long 0.5 shares of stock,

* borrow cash to finance the hedge,

* payoff is matched in both states.

---

## 4. Example 2: European Put Option

### Setup

Using the same parameters as Example 1:

$$
S_0 = 100, \quad u = 1.2, \quad d = 0.9, \quad r = 0.05, \quad dt = 1, \quad K = 105
$$

Payoffs:

$$
P_u = (105 - 120)^+ = 0, \qquad
P_d = (105 - 90)^+ = 15
$$

---

### Replication

$$
\Delta = \frac{0 - 15}{(1.2 - 0.9)\cdot 100} = -0.5
$$

$$
\beta = \frac{0 - (-0.5)\cdot 120}{e^{0.05}}
\approx 57.10
$$

---

### Price

$$
P_0 = -0.5 \cdot 100 + 57.10 = 7.10 \approx 7.14
$$

**Interpretation**:

* short the stock,

* lend money in the bank,

* hedge benefits from price decreases.

---

## 5. Example 3: Digital (Binary) Option

Consider a **digital call** paying:

$$
H =
\begin{cases}
1 & \text{if } S_{dt} = uS_0 \\
0 & \text{if } S_{dt} = dS_0
\end{cases}
$$

---

### Replication

$$
\Delta = \frac{1 - 0}{(u-d)S_0}, \qquad
\beta = \frac{1 - \Delta uS_0}{e^{r dt}}
$$

---

### Price

$$
V_0 = \Delta S_0 + \beta = e^{-r dt} q,
\qquad
q = \frac{e^{r dt} - d}{u-d}
$$

This example shows that **risk-neutral probability is literally the price of a digital claim**.

---

## 6. Example 4: Forward Contract

A forward payoff is

$$
H = S_{dt} - K
$$

Thus,

$$
H_u = uS_0 - K, \qquad
H_d = dS_0 - K
$$

---

### Replication

$$
\Delta = \frac{(u-d)S_0}{(u-d)S_0} = 1,
\qquad
\beta = -\frac{K}{e^{r dt}}
$$

---

### Price

$$
V_0 = S_0 - Ke^{-r dt}
$$

This recovers the standard forward price directly from replication.

---

## 7. Put–Call Parity (Replication View)

Consider two portfolios:

* **A**: long call + $Ke^{-r dt}$ in bank

* **B**: long put + one share of stock

Terminal payoffs coincide in all states, hence

$$
\boxed{
C_0 - P_0 = S_0 - Ke^{-r dt}
}
$$

Put–call parity is therefore **a replication identity**, not an assumption.

---

## 8. Interpretation of Delta and Beta

Across all examples:

* $\Delta$ measures **local sensitivity** of payoff to the stock,

* $\beta$ adjusts the cash position to match levels,

* signs of $\Delta$ encode economic intuition:

  * calls: $\Delta > 0$,

  * puts: $\Delta < 0$,

  * forwards: $\Delta = 1$.

At this stage:

* delta is a **pricing coefficient**,

* not yet a trading strategy over time.

Dynamic hedging is introduced later.

---

## 9. Key Takeaways

1. Replication yields prices **without probabilities**.
2. Prices are linear in payoffs.
3. Every one-period derivative reduces to solving two equations.
4. Calls, puts, digitals, and forwards are handled uniformly.
5. Risk-neutral pricing will repackage these results probabilistically.

---

## Summary

In the one-period binomial model:

$$
\boxed{
V_0 = \Delta S_0 + \beta
}
$$

is the **fundamental pricing formula**, where ($\Delta,\beta$) are chosen to replicate the payoff.

This logic extends directly to:

* multi-period trees (via backward induction),

* dynamic replication,

* and ultimately the Black–Scholes framework.
