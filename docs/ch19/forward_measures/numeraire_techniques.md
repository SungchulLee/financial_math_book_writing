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
