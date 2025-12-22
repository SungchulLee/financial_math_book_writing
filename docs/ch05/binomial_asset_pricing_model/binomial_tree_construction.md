# Multi-Period Binomial Tree Construction

The **multi-period binomial tree** is the central computational object of discrete-time option pricing.
It is constructed **forward in time** by specifying stock dynamics and **priced backward** by no-arbitrage.

This section unifies:

* how the tree is built,

* how parameters (u,d,q) are chosen,

* how pricing and hedging work on the tree.

---

## 1. From One Period to Many

Fix a maturity (T) and divide it into (N) equal steps of length

$$
\Delta t = \frac{T}{N}, \qquad t_n = n\Delta t.
$$

At each step, the stock price moves:

$$
S_{n+1} =
\begin{cases}
u S_n & \text{(up)} \
d S_n & \text{(down)}
\end{cases}
\quad\text{with } u>d>0.
$$

The risk-free asset grows deterministically:

$$
B_{n+1} = e^{r\Delta t} B_n,
\qquad
B_n = e^{r n\Delta t}.
$$

---

## 2. Node Structure and Recombination

After (n) steps, if the path contains (j) up-moves and (n-j) down-moves, the stock price is

$$
\boxed{
S_{n,j} = S_0, u^j d^{,n-j},
\qquad j=0,1,\dots,n.
}
$$

This shows the **recombining property**:

* the tree has (n+1) nodes at time (n),

* not $2^n$ distinct paths.

This property is crucial for computational efficiency.

---

## 3. Choice of Up and Down Factors

Several standard parameterizations are used.

### 3.1 Linear factors (Wilmott-style)

$$
u = 1 + \sigma\sqrt{\Delta t},
\qquad
d = 1 - \sigma\sqrt{\Delta t}.
$$

* Simple but can fail if $\sigma\sqrt{\Delta t}>1$.

---

### 3.2 Exponential factors (Cox–Ross–Rubinstein)

$$
\boxed{
u = e^{\sigma\sqrt{\Delta t}},
\qquad
d = e^{-\sigma\sqrt{\Delta t}}.
}
$$

* Always positive

* Converges to geometric Brownian motion

* **Most commonly used**

---

### 3.3 Drift-adjusted exponential (Jarrow–Rudd)

$$
u = e^{$r-\tfrac12\sigma^2$\Delta t + \sigma\sqrt{\Delta t}},
\qquad
d = e^{$r-\tfrac12\sigma^2$\Delta t - \sigma\sqrt{\Delta t}}.
$$

* Matches additional moments

* Requires care in interpretation

---

## 4. Risk-Neutral Probability

Let

$$
R = e^{r\Delta t}.
$$

**No-arbitrage** requires:

$$
\boxed{d < R < u.}
$$

Under this condition, define the **risk-neutral up probability**:

$$
\boxed{
q = \frac{R-d}{u-d} = \frac{e^{r\Delta t}-d}{u-d},
\qquad q\in(0,1).
}
$$

Then the stock satisfies the martingale condition:

$$
\mathbb{E}^{\mathbb{Q}}[S_{n+1}\mid\mathcal{F}_n] = R S_n.
$$

---

## 5. Building the Tree (Forward Pass)

To construct the stock-price tree:

1. Fix $S_0, T, N, r, \sigma$
2. Choose (u,d) (typically CRR)
3. Compute (q)
4. Populate nodes using

$$
S_{n,j} = S_0 u^j d^{n-j}
$$

This completes the **forward construction**.

---

## 6. Pricing by Backward Induction

Let a claim have terminal payoff (H$S_N$).
Define its value at node ((n,j)) as $V_{n,j}$.

At maturity:

$$
V_{N,j} = H$S_{N,j}$.
$$

For earlier nodes:

$$
\boxed{
V_{n,j}
= e^{-r\Delta t}
\Big(
q,V_{n+1,j+1} + (1-q),V_{n+1,j}
\Big).
}
$$

This is the **backward induction algorithm**.

---

## 7. Dynamic Replication and Delta

At each node ((n,j)), the replicating portfolio holds

$$
\boxed{
\Delta_{n,j}
= \frac{V_{n+1,j+1}-V_{n+1,j}}
{(u-d)S_{n,j}}.
}
$$

This is **discrete-time delta hedging**:

* the hedge ratio changes across nodes,

* replication is **dynamic**.

---

## 8. Algorithmic View (Summary)

**Forward pass**:

* build stock-price tree $S_{n,j}$

**Backward pass**:

* compute payoffs at maturity

* recurse backward using risk-neutral pricing

**Output**:

* option price $V_0$,

* hedge ratios $\Delta_{n,j}$.

---

## 9. Why This Section Stands Alone

This section contains **one coherent idea**:

> A binomial tree is *constructed forward* and *priced backward* under no-arbitrage.

Separating “how to build” from “multi-period tree” only duplicates notation and interrupts flow.
They belong together.

---

## Summary

* The binomial tree discretizes stock-price evolution.

* Recombination yields (O$N^2$) complexity.

* No-arbitrage determines the unique risk-neutral probability.

* Pricing is backward induction.

* Hedging is node-by-node replication.

* This structure converges to Black–Scholes as $\Delta t \to 0$.
