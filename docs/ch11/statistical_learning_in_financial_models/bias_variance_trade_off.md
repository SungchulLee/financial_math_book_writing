# Bias–Variance Trade-Off

The **bias–variance trade-off** is a central concept in statistical learning, governing the balance between model simplicity and flexibility.

---

## 1. Decomposition of error

For an estimator \(\hat f\), the expected prediction error can be decomposed as:

\[
\mathbb{E}[(Y - \hat f(X))^2]
= \text{Bias}^2 + \text{Variance} + \text{Noise}.
\]



This decomposition highlights competing sources of error.

---

## 2. Bias

Bias measures systematic error due to model assumptions:
- overly simple models have high bias,
- misspecified functional forms dominate error.

High bias leads to underfitting.

---

## 3. Variance

Variance measures sensitivity to data fluctuations:
- overly flexible models have high variance,
- estimates change significantly with small data changes.

High variance leads to overfitting.

---

## 4. Implications for finance

Financial data is:
- noisy,
- non-stationary,
- limited in effective sample size.

This makes controlling variance especially important in practice.

---

## 5. Key takeaways

- Bias and variance pull in opposite directions.
- Optimal models balance both.
- Stability often outweighs theoretical accuracy in finance.

---

## Further reading

- Geman, bias–variance in finance.
- Hastie et al., bias–variance trade-off.
