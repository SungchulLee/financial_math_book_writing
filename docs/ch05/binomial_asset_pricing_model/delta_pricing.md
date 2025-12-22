# Delta as a Pricing Coefficient (Local Replication)

## Purpose of This Section

This section introduces **delta ($\Delta$)** as a **pricing coefficient** arising from *static replication* in a one-period binomial model.

> Delta here is **not** a hedging strategy over time.
> It is the coefficient that captures how payoffs change across states and makes pricing possible.

Dynamic hedging is intentionally deferred.

---

## 1. One-Period Replication Setup

Let the stock price evolve as

$$
S_1 =
\begin{cases}
uS_0 & \text{up},\
dS_0 & \text{down},
\end{cases}
\qquad u>d>0.
$$

Let a contingent claim have payoff

$$
H =
\begin{cases}
H_u & \text{up},\
H_d & \text{down}.
\end{cases}
$$

We seek a portfolio ($\Delta,\beta$) such that

$$
\Delta uS_0 + \beta e^r = H_u,
\qquad
\Delta dS_0 + \beta e^r = H_d.
$$

---

## 2. Delta from Replication

Subtracting the two equations eliminates $\beta$:

$$
\boxed{
\Delta = \frac{H_u - H_d}{(u-d)S_0}.
}
$$

This number is:

* uniquely determined,

* independent of probabilities,

* a **slope in payoff space**.

Once $\Delta$ is fixed, $\beta$ adjusts the level.

---

## 3. Interpretation of Delta

* Delta measures **how much the payoff changes** when the state changes

* It is a **linear pricing coefficient**

* It depends only on ($H_u,H_d$) and ($u,d,S_0$)

* No rebalancing, no dynamics, no expectations

> **Delta exists because the payoff space is two-dimensional.**

---

## 4. Example 1: European Call Option

### Setup

Let

$$
S_0 = 100, \quad u = 1.2, \quad d = 0.9, \quad r = 0.05, \quad K = 105.
$$

Payoffs:

$$
C_u = (120-105)^+ = 15,
\qquad
C_d = (90-105)^+ = 0.
$$

---

### Delta

$$
\boxed{
\Delta_{\text{call}}
= \frac{15-0}{(1.2-0.9)\cdot 100}
= \frac{15}{30}
= 0.5.
}
$$

**Interpretation**:

* the call payoff moves halfway with the stock between the two states.

---

## 5. Example 2: European Put Option

Payoffs:

$$
P_u = (105-120)^+ = 0,
\qquad
P_d = (105-90)^+ = 15.
$$

---

### Delta

$$
\boxed{
\Delta_{\text{put}}
= \frac{0-15}{(1.2-0.9)\cdot 100}
= -0.5.
}
$$

**Interpretation**:

* the put payoff moves *oppositely* to the stock.

---

## 6. Example 3: Digital (Binary) Option

Consider a **digital call** paying

$$
H =
\begin{cases}
1 & \text{up},\
0 & \text{down}.
\end{cases}
$$

---

### Delta

$$
\boxed{
\Delta_{\text{digital}}
= \frac{1-0}{(u-d)S_0}.
}
$$

This is the **steepest possible slope** among bounded payoffs.

**Insight**:

* digitals isolate *state changes*,

* they are the “atoms” of payoff space.

---

## 7. Example 4: Forward Contract

A forward payoff is

$$
H = S_1 - K.
$$

Thus:

$$
H_u = uS_0 - K,
\qquad
H_d = dS_0 - K.
$$

---

### Delta

$$
\boxed{
\Delta_{\text{forward}}
= \frac{(u-d)S_0}{(u-d)S_0}
= 1.
}
$$

**Interpretation**:

* a forward moves one-for-one with the stock,

* cash adjusts the level via $-Ke^{-r}$.

---

## 8. Example 5: Put–Call Parity via Delta

Consider the payoff:

$$
C_1 - P_1 = S_1 - K.
$$

Compute deltas:

$$
\Delta_{\text{call}} - \Delta_{\text{put}} = 0.5 - (-0.5) = 1.
$$

This matches the forward’s delta.

> **Put–call parity is a statement about identical deltas and levels**,
> hence identical prices.

---

## 9. Delta and Linearity

If a payoff decomposes as

$$
H = \alpha H^{(1)} + \beta H^{(2)},
$$

then

$$
\Delta_H
= \alpha \Delta_{H^{(1)}} + \beta \Delta_{H^{(2)}}.
$$

Thus:

* delta is **linear in payoffs**,

* pricing reduces to computing slopes and intercepts.

---

## 10. What Delta Is (and Is Not)

### Delta **is**

* a pricing coefficient

* a slope in payoff space

* determined by replication

* static and local

### Delta **is not**

* a probability

* a belief

* a trading rule over time

* a risk measure

Dynamic interpretation comes later.

---

## Key Takeaway

> **Delta is the structural constant of the pricing problem.**

It tells us *how much stock exposure* a payoff contains **at a single step**.
Only after building a multi-period tree does delta become a **hedging process**.
