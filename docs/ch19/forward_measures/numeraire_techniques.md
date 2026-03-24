# Numéraire Techniques


**Numéraire techniques** provide a unified framework for changing probability measures and simplifying derivative pricing by choosing an appropriate reference asset.

---

## What is a numéraire?


A **numéraire** is a strictly positive tradable asset \(N_t\) used to measure value.
Prices expressed in units of \(N_t\) are

\[
\tilde S_t = \frac{S_t}{N_t}.
\]



---

## Fundamental theorem of numéraire change


For any admissible numéraire \(N_t\), there exists a probability measure \(\mathbb{Q}^N\) such that

\[
\frac{S_t}{N_t} \text{ is a martingale under } \mathbb{Q}^N.
\]



This generalizes the risk-neutral measure concept.

---

## Examples of numeraires


Common choices include:
- money-market account \(B_t\) → risk-neutral measure,
- zero-coupon bond \(P(t,T)\) → T-forward measure,
- swap annuity → swap measure.

Each choice simplifies pricing of specific products.

---

## Pricing with numéraires


If payoff \(V_T\) is measurable at \(T\),

\[
V_t = N_t\,\mathbb{E}^{\mathbb{Q}^N}\left[
\frac{V_T}{N_T} \middle| \mathcal{F}_t
\right].
\]



Choosing \(N_t\) wisely can remove discounting or complex drifts.

---

## Key takeaways


- Numéraire choice determines the pricing measure.
- Forward measures are special cases of numéraire techniques.
- Proper numéraire selection simplifies valuation and dynamics.

---

## Further reading


- Geman, El Karoui & Rochet, numéraire theory.
- Brigo & Mercurio, change of measure methods.

---

## Exercises

**Exercise 1.** Let $N_t^{(1)} = B_t$ (money-market account) and $N_t^{(2)} = P(t, T)$ (zero-coupon bond). Write down the Radon--Nikodym derivative $d\mathbb{Q}^{(2)}/d\mathbb{Q}^{(1)}|_{\mathcal{F}_t}$ and verify that it defines a valid density process (i.e., it is a positive martingale under $\mathbb{Q}^{(1)}$ with initial value 1).

---

**Exercise 2.** A derivative pays $V_T = S_T^2$ at time $T$, where $S_t$ follows geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$ under the risk-neutral measure with numéraire $B_t$. Compute $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T^2]$ directly. Then choose $N_t = S_t$ as the numéraire and compute the same price as $S_0\,\mathbb{E}^{\mathbb{Q}^S}[S_T]$, verifying that the two approaches agree. What are the dynamics of $S_t$ under the measure $\mathbb{Q}^S$?

---

**Exercise 3.** Suppose there are two tradable assets $N_t^{(1)}$ and $N_t^{(2)}$ with associated measures $\mathbb{Q}^{(1)}$ and $\mathbb{Q}^{(2)}$. Show that the Radon--Nikodym derivative for the composite change $\mathbb{Q}^{(1)} \to \mathbb{Q}^{(2)}$ is

$$
\frac{d\mathbb{Q}^{(2)}}{d\mathbb{Q}^{(1)}}\bigg|_{\mathcal{F}_t} = \frac{N_t^{(2)} / N_0^{(2)}}{N_t^{(1)} / N_0^{(1)}}
$$

and verify that this is consistent with the individual changes from a common reference measure $\mathbb{Q}$.

---

**Exercise 4.** Explain why the money-market account $B_t = \exp(\int_0^t r_s\,ds)$ is a valid numéraire even when the short rate $r_t$ is stochastic, whereas a zero-coupon bond $P(t, T)$ is only useful as a numéraire for pricing payoffs at or before time $T$. What goes wrong if you try to use $P(t, T)$ to price a payoff at time $T' > T$?

---

**Exercise 5.** A foreign-exchange option pays $\max(X_T - K, 0)$ in domestic currency at time $T$, where $X_t$ is the spot exchange rate. The domestic and foreign money-market accounts are $B_t^d$ and $B_t^f$. Show that $X_t B_t^f / B_t^d$ is a martingale under the domestic risk-neutral measure, and use this to identify the natural numéraire for pricing this option. What is the drift of $X_t$ under the domestic measure?

---

**Exercise 6.** Consider a stock $S_t$ paying a continuous dividend yield $q$. The reinvested stock price $\hat{S}_t = S_t e^{qt}$ is a valid numéraire. Derive the Radon--Nikodym derivative from $\mathbb{Q}$ (money-market numéraire) to $\mathbb{Q}^{\hat{S}}$ (stock numéraire) and show that under $\mathbb{Q}^{\hat{S}}$, the process $B_t/\hat{S}_t$ is a martingale. Use this to price a European put option with payoff $\max(K - S_T, 0)$.
