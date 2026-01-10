# From SDE to the Black–Scholes PDE

## 1. Stock Price Dynamics
Assume the stock price follows geometric Brownian motion:
\[
dS_t = \mu S_t dt + \sigma S_t dW_t.
\]

---

## 2. Risk-Neutral Dynamics
Under the risk-neutral measure:
\[
dS_t = r S_t dt + \sigma S_t dW_t^{\mathbb{Q}}.
\]

---

## 3. Generator
The generator is:
\[
\mathcal{L}f =
rS f_S + \tfrac12 \sigma^2 S^2 f_{SS}.
\]

---

## 4. Pricing PDE
The option price \(V(t,S)\) satisfies:
\[
\boxed{
\partial_t V + rS V_S + \tfrac12 \sigma^2 S^2 V_{SS} - rV = 0.
}
\]

---

## 5. Terminal Condition
\[
V(T,S) = \Phi(S).
\]

---

## 6. Interpretation
This PDE is the cornerstone of modern derivatives pricing.