# Non-Central Chi-Squared Distribution

The non-central chi-squared distribution appears naturally when modeling squared sums of normally distributed variables with non-zero means. This is essential in the Heston model for understanding the variance dynamics of the underlying asset.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand central and non-central chi-squared distributions
    2. Recognize the role of the non-centrality parameter
    3. Apply the distribution to variance process modeling in Heston

---

## Central Chi-Squared Distribution

Let \((X_1, X_2, \ldots, X_k)\) be \(k\) independent, normally distributed random variables with means \(\mu_i = 0\) and variances \(\sigma_i^2\).

The sum of squared normalized variables follows a chi-squared distribution with \(k\) degrees of freedom:

\[
\sum_{i=1}^{k} \left(\frac{X_i}{\sigma_i}\right)^2 \sim \chi^2_k
\]

The PDF of the central chi-squared distribution with \(k\) degrees of freedom is:

\[
f_{\chi^2_k}(x) = \frac{1}{2^{k/2}\Gamma(k/2)} x^{k/2-1} e^{-x/2}, \quad x > 0
\]

---

## Non-Central Chi-Squared Distribution

Now consider \((X_1, X_2, \ldots, X_k)\) with **non-zero means** \(\mu_i\) and variances \(\sigma_i^2\).

The sum of squared normalized variables follows a **non-central chi-squared distribution** with \(k\) degrees of freedom and **non-centrality parameter**:

\[
\lambda = \sum_{i=1}^{k} \left(\frac{\mu_i}{\sigma_i}\right)^2
\]

### Probability Density Function

The non-central chi-squared distribution can be expressed as a mixture of central chi-squared distributions:

\[
f(x; k, \lambda) = \sum_{i=0}^{\infty} \frac{e^{-\lambda/2}(\lambda/2)^i}{i!} f_{\chi^2(k+2i)}(x)
\]

Alternatively, using a modified Bessel function of the first kind \(I_{\nu}\):

\[
f(x; k, \lambda) = \frac{1}{2} e^{-(x+\lambda)/2} \left(\frac{x}{\lambda}\right)^{k/4-1/2} I_{k/2-1}(\sqrt{\lambda x})
\]

### Properties

- When \(\lambda = 0\), the non-central chi-squared reduces to the central chi-squared distribution.
- The mean is \(k + \lambda\).
- The variance is \(2k + 4\lambda\).
- The distribution is skewed, with skewness increasing as \(\lambda\) increases.

---

## Application to CIR Process Transitions

In the Cox–Ingersoll–Ross (CIR) process for interest rates:

\[
dr = \kappa(\bar{r} - r)dt + \gamma\sqrt{r}dW^{\mathbb{Q}}
\]

The transition distribution of \(r(T)\) conditional on \(r(t)\) follows a non-central chi-squared distribution (scaled). This is crucial for:

- Pricing zero-coupon bonds
- Computing transition probabilities
- Simulating the variance process in Heston

---

## Feller Condition and Boundary Behavior

A critical property of CIR-type processes is the **Feller condition**, which controls whether the process can reach zero:

\[
2\kappa\bar{r} \geq \gamma^2 \quad \Rightarrow \quad r(t) \text{ stays strictly positive a.s.}
\]

\[
2\kappa\bar{r} < \gamma^2 \quad \Rightarrow \quad r(t) \text{ may reach zero; probability mass accumulates at } 0
\]

When the Feller condition is violated, special care is needed in simulation and density recovery to avoid negative rates or variance values.

---

## Summary

The non-central chi-squared distribution characterizes the transition dynamics of variance processes in Heston and interest rate processes in CIR models. Understanding its properties—especially the non-centrality parameter, mean, and variance—is essential for accurate pricing and risk management of derivatives that depend on these processes.
