# T-Forward Measures

Beyond the risk-neutral measure, it is often convenient to price derivatives under a **forward measure**, associated with a specific maturity \(T\).

---

## 1. Definition of the T-forward measure

Let \(P(t,T)\) be the zero-coupon bond maturing at \(T\).
The **T-forward measure** \(\mathbb{Q}^T\) is defined by choosing \(P(t,T)\) as numéraire.

Under \(\mathbb{Q}^T\),
\[
\frac{S_t}{P(t,T)} \text{ is a martingale}
\]
for any tradable asset \(S_t\) that pays off at or before \(T\).

---

## 2. Pricing under the forward measure

For a payoff \(V_T\) at time \(T\),
\[
V_t = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}[V_T \mid \mathcal{F}_t].
\]

Discounting disappears because the numéraire already matures at \(T\).

---

## 3. Dynamics under the forward measure

Changing from \(\mathbb{Q}\) to \(\mathbb{Q}^T\):
- alters drift terms,
- leaves volatilities unchanged,
- simplifies pricing of forwards, FRAs, and caps.

Many rates become martingales under their natural forward measures.

---

## 4. Practical importance

Forward measures are especially useful for:
- caplets and floorlets,
- forward-starting contracts,
- simplifying drift terms in HJM and LMM.

---

## 5. Key takeaways

- Forward measures use zero-coupon bonds as numeraires.
- Pricing simplifies to expectation without discounting.
- Measure choice is a powerful modeling tool.

---

## Further reading

- Brigo & Mercurio, forward measures.
- Jamshidian, numéraire techniques.
