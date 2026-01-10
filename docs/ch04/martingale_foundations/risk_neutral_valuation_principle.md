# Risk-Neutral Valuation Principle

## 1. Central Pricing Principle
In arbitrage-free markets:

\[
\boxed{
V_t = \mathbb{E}^{\mathbb{Q}}
\left[
e^{-r(T-t)} \Phi(X_T)
\mid \mathcal{F}_t
\right].
}
\]

---

## 2. Meaning of Risk Neutrality

- Investors behave as if risk preferences do not matter
- Expected returns equal the risk-free rate

---

## 3. PDE Equivalence
Risk-neutral valuation is equivalent to solving:

\[
\partial_t V + \mathcal{L}^{\mathbb{Q}} V - rV = 0
\]

---

## 4. Why the Drift Changes
Changing measure removes risk premia.
Only volatility remains.

---

## 5. Financial Interpretation

- Pricing independent of preferences
- Market prices of risk absorbed into the measure

---

## 6. Connection Forward
The mathematical tool enabling this change is **Girsanov’s theorem**.