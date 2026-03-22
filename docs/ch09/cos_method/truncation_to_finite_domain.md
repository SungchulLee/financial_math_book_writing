# Truncation to Finite Domain

The Fourier cosine series and the COS pricing formula are defined on a finite interval $[a, b]$, but the log-price under most financial models has support on the entire real line (or a half-line). Restricting the density to a finite interval introduces a truncation error that must be controlled. Choosing the interval too narrow discards significant probability mass and produces inaccurate prices; choosing it too wide wastes computational effort on regions where the density is negligible and can degrade the convergence rate. This section develops the cumulant-based truncation rule of Fang and Oosterlee (2008), derives error bounds, and provides practical guidance for selecting $[a, b]$ across different models.

!!! info "Prerequisites"
    - [Cosine Coefficients via CF](cosine_coefficients_via_cf.md) (the CF-based coefficient formula and its truncation error)
    - Probability: cumulants, moment-generating functions, tail bounds

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define cumulants and compute them from the characteristic function
    2. Derive the cumulant-based truncation formula for $[a, b]$
    3. Bound the truncation error in terms of the tail probability
    4. Select appropriate truncation intervals for Black--Scholes, Heston, and heavy-tailed models
    5. Diagnose truncation-related errors in COS method implementations

---

## Why Truncation Is Needed

The cosine expansion of a density $f$ requires a bounded interval $[a, b]$. For a density on $\mathbb{R}$, we replace $f$ by its restriction:

$$
\tilde{f}(x) = \begin{cases} f(x) & \text{if } x \in [a, b] \\ 0 & \text{otherwise} \end{cases}
$$

The truncated density is not a probability density (it integrates to $1 - \delta$ where $\delta = P(X \notin [a, b])$), and the cosine coefficients of $\tilde{f}$ differ from those of $f$ by the truncation error analyzed in the previous section. The goal is to choose $[a, b]$ so that $\delta$ is negligible---say, below $10^{-12}$---while keeping $b - a$ as small as possible to maximize the convergence rate of the cosine series.

---

## Cumulants and the Characteristic Function

Cumulants provide a natural characterization of a distribution's location, spread, and shape, and they are readily computable from the characteristic function.

!!! note "Definition: Cumulants"
    The **cumulants** $\{c_n\}_{n=1}^{\infty}$ of a random variable $X$ are defined by the cumulant-generating function:

    $$
    \ln \phi(u) = \sum_{n=1}^{\infty} c_n \frac{(iu)^n}{n!}
    $$

    where $\phi(u) = \mathbb{E}[e^{iuX}]$. The first four cumulants are:

    - $c_1 = \mathbb{E}[X]$ (mean)
    - $c_2 = \text{Var}(X)$ (variance)
    - $c_3 = \mathbb{E}[(X - c_1)^3]$ (third central moment, related to skewness)
    - $c_4 = \mathbb{E}[(X - c_1)^4] - 3c_2^2$ (excess kurtosis times $c_2^2$)

In practice, $c_1$ through $c_4$ are computed by differentiating $\ln\phi(u)$ at $u = 0$:

$$
c_n = \frac{1}{i^n}\frac{d^n}{du^n}\ln\phi(u)\bigg|_{u=0}
$$

For models with closed-form characteristic functions, these derivatives can often be evaluated analytically or by automatic differentiation.

---

## The Cumulant-Based Truncation Rule

Fang and Oosterlee (2008) proposed a truncation rule based on the first four cumulants:

!!! note "Definition: Cumulant-Based Truncation Interval"
    Given a distribution with cumulants $c_1, c_2, c_3, c_4$ and a truncation parameter $L > 0$, the **truncation interval** is

    $$
    [a, b] = \left[c_1 - L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}},\;\; c_1 + L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}}\right]
    $$

    The standard choice is $L = 10$ or $L = 12$.

The formula centers the interval at the mean $c_1$ and scales the half-width using a quantity that accounts for both variance ($c_2$) and excess kurtosis ($c_4$). For a normal distribution ($c_4 = 0$), this simplifies to

$$
[a, b] = [c_1 - L\sqrt{c_2 + c_2\sqrt{2}},\;\; c_1 + L\sqrt{c_2 + c_2\sqrt{2}}]
$$

which is wider than $[c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]$ by a factor of $\sqrt{1 + \sqrt{2}} \approx 1.554$.

!!! tip "Simplified Rule for Light-Tailed Distributions"
    For many practical purposes, the simpler rule

    $$
    [a, b] = [c_1 - L\sqrt{c_2},\; c_1 + L\sqrt{c_2}]
    $$

    with $L = 10$ works well for Black--Scholes and Heston models. The full cumulant formula provides additional safety for distributions with significant excess kurtosis.

---

## Truncation Error Bound

The truncation error is the probability mass outside $[a, b]$, which we bound using tail inequalities.

!!! note "Theorem: Chebyshev-Based Truncation Bound"
    For a random variable $X$ with mean $c_1$ and variance $c_2$:

    $$
    P(X \notin [c_1 - L\sqrt{c_2},\; c_1 + L\sqrt{c_2}]) \leq \frac{1}{L^2}
    $$

    by Chebyshev's inequality. With $L = 10$, this gives $\delta \leq 0.01$.

This bound is extremely conservative for light-tailed distributions. Tighter bounds are available:

!!! note "Proposition: Exponential Tail Bound"
    If $X$ has a moment-generating function $M(\theta) = \mathbb{E}[e^{\theta X}]$ that is finite for $|\theta| < \theta_0$, then for the interval $[a, b] = [c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]$:

    $$
    P(X \notin [a, b]) \leq 2\exp\!\left(-\frac{L^2}{2} + O(L^3/\sqrt{c_2})\right)
    $$

    For the normal distribution, this is exact: $P(|X - \mu| > L\sigma) = \text{erfc}(L/\sqrt{2})$.

With $L = 10$ and a normal-like tail:

$$
\delta \approx \text{erfc}(10/\sqrt{2}) \approx 1.5 \times 10^{-23}
$$

This is far below machine epsilon, making the truncation error completely negligible.

---

## Effect on the COS Pricing Error

The truncation error propagates to the option price through two channels:

**Channel 1: Coefficient error.** The CF-based cosine coefficients $F_k$ differ from the true coefficients $A_k$ by $|\varepsilon_k| \leq 2\delta/(b-a)$. Over $N$ terms, the total coefficient-induced price error is bounded by

$$
|V_{\text{true}} - V_{\text{COS}}^{\text{trunc}}| \leq e^{-rT}\sum_{k=0}^{N-1}|\varepsilon_k|\,|V_k| \leq e^{-rT}\frac{2\delta}{b-a}\sum_{k=0}^{N-1}|V_k|
$$

**Channel 2: Missing payoff mass.** The density outside $[a, b]$ contributes to the option value. For a call option with $b$ large enough that $f(x)$ is negligible for $x > b$, this contribution is bounded by $e^{-rT}\mathbb{E}[(S_T - K)^+\mathbf{1}_{X \notin [a,b]}]$, which is exponentially small for typical truncation parameters.

In practice, with $L = 10$, the truncation error is below $10^{-15}$---far smaller than the series truncation error for any reasonable $N$.

---

## Truncation Intervals for Standard Models

The following table gives typical truncation intervals for common financial models, using $L = 10$:

!!! example "Model-Specific Truncation Intervals"

    | Model | Cumulants | Typical $[a, b]$ |
    |---|---|---|
    | Black--Scholes ($\sigma = 0.2$, $T = 1$) | $c_1 = (r-\sigma^2/2)T$, $c_2 = \sigma^2 T = 0.04$ | $[c_1 - 2.0, c_1 + 2.0]$ |
    | Heston (typical) | $c_2 \approx 0.04$, $c_4 > 0$ | $[c_1 - 2.5, c_1 + 2.5]$ |
    | Variance Gamma ($\sigma = 0.2$, $\nu = 0.5$) | Higher kurtosis | $[c_1 - 4.0, c_1 + 4.0]$ |
    | CGMY ($Y = 0.5$) | Heavy tails | $[c_1 - 6.0, c_1 + 6.0]$ |

    Heavier-tailed models require wider truncation intervals, which in turn require more cosine terms $N$ for the same accuracy (since the cosine frequencies are $k\pi/(b-a)$ and wider intervals mean smaller frequency spacing).

---

## Practical Diagnostics

When implementing the COS method, truncation errors can be diagnosed using the following checks:

1. **Increase $L$ and check stability.** If the price changes when $L$ is increased from 10 to 12, the original truncation was too narrow.

2. **Check $A_0$ normalization.** Since $A_0 = 2/(b-a)\int_a^b f(x)\,dx \approx 2/(b-a)$ for a properly truncated density, the quantity $A_0(b-a)/2$ should be close to 1. A significant deviation indicates truncation loss.

3. **Check recovered density.** Reconstruct $\hat{f}_N(x)$ using the cosine series and verify that $\int_a^b \hat{f}_N(x)\,dx \approx 1$ and $\hat{f}_N(x) \geq 0$ for all $x \in [a, b]$.

!!! warning "Over-Truncation for Short Maturities"
    For very short maturities ($T < 0.01$), the density concentrates sharply near the forward price. The variance $c_2 \propto T$ is small, so the truncation interval $[c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]$ is narrow. However, the density's peak is very high (proportional to $1/\sqrt{c_2}$), requiring more cosine terms to resolve. In such cases, increasing $N$ is more important than widening the interval.

---

## Summary

Truncation to a finite domain is the first step of the COS method, and the cumulant-based rule provides a principled way to choose $[a, b]$:

| Item | Value / Formula |
|---|---|
| Truncation interval | $[c_1 - L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}},\; c_1 + L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}}]$ |
| Typical $L$ | $10$ to $12$ |
| Truncation error | $\delta = P(X \notin [a,b])$, exponentially small for light tails |
| Price error from truncation | $O(\delta)$, negligible compared to series truncation |
| Diagnostic | Check $A_0(b-a)/2 \approx 1$ |

**The cumulant-based truncation rule adapts the interval $[a, b]$ to the distribution's shape, ensuring that the truncation error is negligible while keeping the interval as narrow as possible to maximize the convergence rate of the cosine series.**
