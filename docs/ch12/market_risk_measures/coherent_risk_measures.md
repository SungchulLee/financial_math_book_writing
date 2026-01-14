# Coherent Risk Measures


A **coherent risk measure** satisfies a set of axioms that formalize desirable properties of a risk metric, especially with respect to diversification.

---

## Coherence axioms


A risk measure \(\rho(L)\) is **coherent** if it satisfies:

1. **Monotonicity:**  
   If \(L_1 \le L_2\), then \(\rho(L_1) \le \rho(L_2)\).
2. **Translation invariance:**  
   \(\rho(L + c) = \rho(L) + c\).
3. **Positive homogeneity:**  
   \(\rho(\lambda L) = \lambda \rho(L)\) for \(\lambda > 0\).
4. **Subadditivity:**  
   \(\rho(L_1 + L_2) \le \rho(L_1) + \rho(L_2)\).

Subadditivity encodes the diversification principle.

---

## VaR vs ES


- **VaR** generally fails subadditivity and is *not* coherent.
- **Expected Shortfall** satisfies all four axioms and *is* coherent.

This is a key theoretical distinction.

---

## Economic interpretation


Coherent risk measures:
- reward diversification,
- penalize concentration of risk,
- align better with economic intuition.

They are particularly suitable for portfolio-level risk management.

---

## Practical relevance


Despite theoretical appeal:
- coherent measures can be harder to estimate,
- tail sensitivity increases model risk,
- practical implementation requires care.

Nonetheless, coherence is a guiding principle in modern risk management.

---

## Key takeaways


- Coherence formalizes desirable risk properties.
- ES is coherent; VaR generally is not.
- Coherent measures support diversification-aware risk control.

---

## Further reading


- Artzner et al., coherent risk measures.
- Föllmer & Schied, *Stochastic Finance*.
