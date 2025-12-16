# Value-at-Risk (VaR)

**Value-at-Risk (VaR)** is the most widely used market risk measure in finance. It summarizes potential losses over a fixed horizon at a given confidence level.

---

## 1. Definition

Let \(L\) denote the (random) loss of a portfolio over a given horizon.
For a confidence level \(\alpha \in (0,1)\), the Value-at-Risk is defined as

\[
\text{VaR}_{\alpha}(L)
= \inf\{x \in \mathbb{R} : \mathbb{P}(L \le x) \ge \alpha\}.
\]



It represents the smallest loss threshold that will not be exceeded with probability \(\alpha\).

---

## 2. Interpretation

A statement such as
> “The one-day 99% VaR is 10 million”
means that, under the model,
- losses exceed 10 million with probability at most 1% over one day.

VaR is a **quantile-based** risk measure.

---

## 3. Common estimation methods

VaR is typically estimated using:
- **historical simulation**,
- **parametric (variance–covariance) methods**,
- **Monte Carlo simulation**.

Each method reflects different modeling assumptions.

---

## 4. Strengths and limitations

Strengths:
- intuitive and easy to communicate,
- widely adopted by regulators and institutions.

Limitations:
- ignores the magnitude of extreme losses beyond the quantile,
- not subadditive in general (fails diversification principle),
- sensitive to distributional assumptions.

---

## 5. Key takeaways

- VaR measures a quantile of the loss distribution.
- It is simple but incomplete as a tail risk measure.
- Its limitations motivate alternative measures.

---

## Further reading

- Jorion, *Value at Risk*.
- McNeil, Frey & Embrechts, *Quantitative Risk Management*.
