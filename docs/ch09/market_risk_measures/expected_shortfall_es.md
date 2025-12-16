# Expected Shortfall (ES)

**Expected Shortfall (ES)**, also known as Conditional Value-at-Risk (CVaR), addresses key shortcomings of Value-at-Risk by focusing on tail losses beyond the VaR threshold.

---

## 1. Definition

For confidence level \(\alpha\), the Expected Shortfall of loss \(L\) is

\[
\text{ES}_{\alpha}(L)
= \mathbb{E}[L \mid L \ge \text{VaR}_{\alpha}(L)].
\]



It measures the **average loss in the worst \((1-\alpha)\)% of scenarios**.

---

## 2. Interpretation

ES answers the question:
> “If losses exceed VaR, how large are they on average?”

This makes ES a more informative tail risk measure than VaR.

---

## 3. Regulatory relevance

Modern regulations (e.g. Basel III/IV) favor ES over VaR because:
- ES captures tail severity,
- it behaves better under aggregation,
- it discourages excessive tail risk-taking.

---

## 4. Estimation considerations

Estimating ES requires:
- accurate modeling of tail behavior,
- sufficient data in the tail,
- careful numerical implementation.

ES is generally more sensitive to model error than VaR.

---

## 5. Key takeaways

- ES measures expected tail losses beyond VaR.
- It is more conservative and informative than VaR.
- ES is now the regulatory standard for market risk.

---

## Further reading

- Acerbi & Tasche, Expected Shortfall properties.
- Basel Committee on Banking Supervision.
