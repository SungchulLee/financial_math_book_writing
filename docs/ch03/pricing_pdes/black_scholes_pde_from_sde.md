# SDE Black Scholes


## Stock Price Dynamics

Assume the stock price follows geometric Brownian motion:
\[
dS_t = \mu S_t dt + \sigma S_t dW_t.
\]

---

## Risk Neutral

Under the risk-neutral measure:
\[
dS_t = r S_t dt + \sigma S_t dW_t^{\mathbb{Q}}.
\]

---

## Generator

The generator is:
\[
\mathcal{L}f =
rS f_S + \tfrac12 \sigma^2 S^2 f_{SS}.
\]

---

## Pricing PDE

The option price \(V(t,S)\) satisfies:
\[
\boxed{
\partial_t V + rS V_S + \tfrac12 \sigma^2 S^2 V_{SS} - rV = 0.
}
\]

---

## Terminal Condition

\[
V(T,S) = \Phi(S).
\]

---

## Interpretation

This PDE is the cornerstone of modern derivatives pricing.