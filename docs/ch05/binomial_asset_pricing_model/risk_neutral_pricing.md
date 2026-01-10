# Risk-Neutral Pricing

Risk-neutral pricing is one of the central principles of modern asset pricing:

> **In an arbitrage-free market, the price of a contingent claim equals the discounted expectation of its payoff under a risk-neutral measure.**

In the binomial model, this principle emerges naturally from no-arbitrage and provides a direct, computation-friendly pricing formula.

---

## 1. From Replication to Expectation

Earlier, prices were obtained by **replication**:

* construct a portfolio that matches payoffs,

* invoke the law of one price.

Risk-neutral pricing asks a different question:

> *Is there a probability measure under which prices can be computed by expectation alone?*

The answer is **yes**, and that measure is uniquely determined by no-arbitrage.

---

## 2. Risk-Neutral Probability

### Definition

In a one-period binomial model with

$$
S_{dt} \in \{uS_0, dS_0\}, \qquad B_{dt} = e^{r dt}
$$

the **risk-neutral probability** is

$$
\boxed{
q = \frac{e^{r dt} - d}{u - d}
}
$$

### Properties

* \(0 < q < 1\) if and only if $d < e^{r dt} < u$

* \(q\) depends **only** on \((u,d,r,dt)\)

* \(q\) is independent of the payoff being priced

---

## 3. Martingale Interpretation

Under the probability measure $\mathbb{Q}$ defined by

$$
\mathbb{Q}(\text{up}) = q,
\qquad
\mathbb{Q}(\text{down}) = 1-q
$$

the discounted stock price satisfies

$$
\boxed{
\mathbb{E}^{\mathbb{Q}}\left[\frac{S_{dt}}{e^{r dt}}\right] = S_0
}
$$

That is, **discounted prices are martingales**.

This property extends to *all* attainable payoffs.

---

## 4. Risk-Neutral Pricing Formula

For any one-period contingent claim with payoffs $H_u, H_d$,

$$
\boxed{
V_0
= e^{-r dt}\mathbb{E}^{\mathbb{Q}}[H]
= e^{-r dt}\big(qH_u + (1-q)H_d\big)
}
$$

This formula:

* avoids solving replication equations,

* makes pricing purely probabilistic,

* is equivalent to replication by no-arbitrage.

---

## 5. Example 1: European Call Option

### Setup

Let

$$
S_0 = 100, \quad
u = 1.2, \quad
d = 0.9, \quad
r = 0.05, \quad
dt = 1, \quad
K = 105
$$

Then $e^{r dt} = e^{0.05} \approx 1.0513$.

Payoffs:

$$
C_u = (120 - 105)^+ = 15,
\qquad
C_d = (90 - 105)^+ = 0
$$

### Pricing

First compute

$$
q = \frac{e^{0.05} - 0.9}{1.2 - 0.9} = \frac{1.0513 - 0.9}{0.3} \approx 0.504
$$

Then

$$
\boxed{
C_0
= e^{-0.05}\big[0.504 \cdot 15 + 0.496 \cdot 0\big]
\approx 7.14
}
$$

**Interpretation**:

* no replication needed,

* price is a discounted weighted average of payoffs.

---

## 6. Example 2: European Put Option

### Setup

Using the same parameters as Example 1:

$$
S_0 = 100, \quad
u = 1.2, \quad
d = 0.9, \quad
r = 0.05, \quad
dt = 1, \quad
K = 105
$$

Payoffs:

$$
P_u = (105 - 120)^+ = 0,
\qquad
P_d = (105 - 90)^+ = 15
$$

### Pricing

$$
\boxed{
P_0
= e^{-0.05}\big[0.504 \cdot 0 + 0.496 \cdot 15\big]
\approx 7.14
}
$$

---

## 7. Example 3: Digital (Binary) Option

Consider a digital claim paying

$$
H =
\begin{cases}
1 & \text{up}\\
0 & \text{down}
\end{cases}
$$

### Pricing

$$
\boxed{
V_0
= e^{-r dt}\mathbb{Q}(\text{up})
= e^{-r dt} q
}
$$

**Insight**:

* risk-neutral probability is literally the **price of a digital payoff**,

* probabilities here are *prices in disguise*.

---

## 8. Example 4: Forward Contract

A forward payoff is

$$
H = S_1 - K
$$

### Pricing

$$
\begin{aligned}
V_0
&= e^{-r dt}\mathbb{E}^{\mathbb{Q}}[S_{dt} - K] \\
&= e^{-r dt}\big[e^{r dt} S_0 - K\big] \\
&= \boxed{S_0 - Ke^{-r dt}}
\end{aligned}
$$

This recovers the standard forward price directly from expectation.

---

## 9. Example 5: Put–Call Parity

Using risk-neutral pricing,

$$
\begin{aligned}
C_0 - P_0
&= e^{-r dt}\mathbb{E}^{\mathbb{Q}}[S_{dt} - K] \\
&= S_0 - Ke^{-r dt}
\end{aligned}
$$

$$
\boxed{
C_0 - P_0 = S_0 - Ke^{-r dt}
}
$$

Put–call parity is therefore a **risk-neutral identity**, not a separate assumption.

---

## 10. Linearity of Risk-Neutral Pricing

For any payoffs $H_1, H_2$ and scalars $\alpha, \beta$,

$$
V_0(\alpha H_1 + \beta H_2)
= \alpha V_0(H_1) + \beta V_0(H_2)
$$

This linearity explains why:

* complex payoffs can be decomposed,

* state prices and binaries work,

* pricing reduces to expectation.

---

## 11. What Risk-Neutral Probability Is (and Is Not)

### It **is**

* a pricing device,

* an equivalent martingale measure,

* uniquely pinned down by no-arbitrage.

### It **is not**

* a real-world probability,

* an estimate of beliefs,

* a forecast of outcomes.

> Risk-neutral pricing removes risk premia by construction.

---

## 12. Multi-Period Preview

In an $N$-period binomial tree, let $H_{Ndt}$ denote the random payoff at time $Ndt$, and let $H_j$ denote the **specific payoff value** at the terminal node reached after exactly $j$ up moves:

$$
H_j = H(S_0 u^j d^{N-j})
$$

Then the risk-neutral pricing formula becomes:

$$
\boxed{
V_0
= e^{-r N dt}\mathbb{E}^{\mathbb{Q}}[H_{Ndt}]
= e^{-r N dt}
\sum_{j=0}^N
\binom{N}{j} q^j (1-q)^{N-j} H_j
}
$$

Here:

* $\mathbb{E}^{\mathbb{Q}}[H_{Ndt}]$ is the expectation of the **random payoff**,
* $H_j$ are the $N+1$ **deterministic payoff values** at terminal nodes,
* $\binom{N}{j} q^j (1-q)^{N-j}$ is the probability of reaching the $j$-th terminal node.

This leads directly to **backward induction** and tree-based pricing.

---

## Summary

Risk-neutral pricing reframes asset valuation as:

1. choose the risk-neutral measure,
2. compute expected payoff,
3. discount at the risk-free rate.

In the binomial model, this approach:

* is equivalent to replication,

* simplifies computation,

* generalizes cleanly to multi-period trees,

* forms the bridge to Black–Scholes theory.
