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

---

## Exercises

**Exercise 1.** A non-central chi-squared random variable $X \sim \chi^2(\nu, \lambda)$ with $\nu$ degrees of freedom and non-centrality $\lambda$ has mean $\nu + \lambda$ and variance $2(\nu + 2\lambda)$. Verify these formulas for $\nu = 4$ and $\lambda = 3$.

---

**Exercise 2.** For the CIR process, the scaled transition density gives $v_T/c \sim \chi^2(\delta, \lambda)$ where $\delta = 4\kappa\theta/\sigma_v^2$ and $c = \sigma_v^2(1 - e^{-\kappa\tau})/(4\kappa)$. Compute $\delta$ and $c$ for $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$, $\tau = 1$.

---

**Exercise 3.** The non-central chi-squared CDF can be computed as a mixture of central chi-squared CDFs: $F_{\chi^2(\nu,\lambda)}(x) = \sum_{k=0}^\infty \frac{e^{-\lambda/2}(\lambda/2)^k}{k!} F_{\chi^2(\nu+2k)}(x)$. Explain why this is a Poisson-weighted sum and relate the Poisson parameter $\lambda/2$ to the CIR non-centrality.

---

**Exercise 4.** When $\delta < 2$ (Feller condition violated), the density $f_{\chi^2(\delta, \lambda)}(x)$ has a singularity at $x = 0$. Explain the physical meaning: for the variance process, this means there is positive probability of $V_T$ being exactly zero. How does the non-centrality $\lambda$ (which depends on $v_t$) affect this probability?

---

**Exercise 5.** To sample from a non-central chi-squared distribution, one common method uses $\chi^2(\nu, \lambda) = \chi^2(\nu - 1) + (Z + \sqrt{\lambda})^2$ where $Z \sim N(0,1)$ and $\chi^2(\nu-1)$ is central chi-squared (valid for $\nu \geq 1$). Describe the steps to generate a sample of $v_T$ given $v_t$ using this decomposition.

---

**Exercise 6.** Compare the computational cost of exact sampling from the non-central chi-squared distribution versus Euler discretization with $N$ time steps. For what values of $N$ does exact sampling become preferable?
