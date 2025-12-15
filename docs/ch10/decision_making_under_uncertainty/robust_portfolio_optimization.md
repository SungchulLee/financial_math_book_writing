# Robust Portfolio Optimization

**Robust portfolio optimization** accounts for uncertainty in model inputs, such as expected returns and covariances, by seeking portfolios that perform well across a range of plausible scenarios.

---

## 1. Motivation

Classical mean–variance optimization is highly sensitive to:
- estimation error in expected returns,
- unstable covariance estimates,
- model misspecification.

Robust optimization mitigates these weaknesses.

---

## 2. Robust formulation

A typical robust portfolio problem takes the form
\[
\max_{w} \; \min_{\theta \in \Theta}
\mathbb{E}_{\theta}[U(w)],
\]
where \(\Theta\) represents uncertainty in model parameters.

The portfolio is optimized against worst-case inputs.

---

## 3. Uncertainty sets

Common uncertainty sets include:
- ellipsoidal sets for means,
- factor-based covariance uncertainty,
- moment-based ambiguity sets.

The choice of set determines conservatism.

---

## 4. Practical implications

Robust portfolios typically:
- are more diversified,
- avoid extreme positions,
- exhibit more stable out-of-sample performance.

They trade peak performance for reliability.

---

## 5. Key takeaways

- Robust optimization hedges parameter uncertainty.
- It improves stability and diversification.
- Conservatism is a feature, not a flaw.

---

## Further reading

- Goldfarb & Iyengar, robust portfolio optimization.
- Fabozzi et al., robust asset allocation.
