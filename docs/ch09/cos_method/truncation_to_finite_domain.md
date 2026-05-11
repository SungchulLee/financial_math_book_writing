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

---

## Exercises

**Exercise 1.** For $X \sim N(0, 1)$, the cumulants are $c_1 = 0$, $c_2 = 1$, $c_3 = 0$, $c_4 = 0$. Compute the cumulant-based truncation interval $[a, b]$ using the formula $[c_1 - L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}},\; c_1 + L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}}]$ with $L = 10$. Compare this to the simpler rule $[c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]$ and explain the difference.

??? success "Solution to Exercise 1"
    For $X \sim N(0, 1)$, the cumulants are $c_1 = 0$, $c_2 = 1$, $c_3 = 0$, $c_4 = 0$.

    **Full cumulant formula:** Substituting into $[c_1 - L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}},\; c_1 + L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}}]$:

    $$
    c_2 + \sqrt{c_4 + 2c_2^2} = 1 + \sqrt{0 + 2} = 1 + \sqrt{2} \approx 2.4142
    $$

    The half-width is $L\sqrt{1 + \sqrt{2}} = 10\sqrt{2.4142} \approx 10 \times 1.554 = 15.54$.

    $$
    [a, b] = [-15.54, 15.54]
    $$

    **Simplified rule:** $[c_1 - L\sqrt{c_2},\; c_1 + L\sqrt{c_2}] = [-10, 10]$.

    **Comparison:** The full cumulant formula gives an interval that is wider by a factor of $\sqrt{1 + \sqrt{2}} \approx 1.554$. The extra width comes from the $\sqrt{c_4 + 2c_2^2}$ term, which for the normal distribution evaluates to $\sqrt{2}$ even though $c_4 = 0$ (because of the $2c_2^2$ contribution). This provides additional safety margin. However, for $N(0,1)$, even the simpler interval $[-10, 10]$ captures all but $P(|X| > 10) \approx 1.5 \times 10^{-23}$ of the probability, so the extra width is unnecessary in practice. The full formula is designed to accommodate distributions with significant excess kurtosis ($c_4 > 0$), where the simpler rule might be too narrow.

---

**Exercise 2.** Compute the first four cumulants $c_1, c_2, c_3, c_4$ for the Variance Gamma model with parameters $\sigma = 0.12$, $\theta = -0.14$, $\nu = 0.2$, $r = 0.05$, $T = 1$. Using the formulas $c_2 = (\sigma^2 + \nu\theta^2)T$, $c_4 = (3\sigma^4\nu + 12\sigma^2\theta^2\nu^2 + 6\theta^4\nu^3)T$, determine the truncation interval with $L = 12$. How much wider is this interval compared to the Black-Scholes case with the same variance?

??? success "Solution to Exercise 2"
    For the Variance Gamma model with $\sigma = 0.12$, $\theta = -0.14$, $\nu = 0.2$, $T = 1$:

    **Cumulant $c_2$ (variance):**

    $$
    c_2 = (\sigma^2 + \nu\theta^2)T = (0.0144 + 0.2 \times 0.0196)\times 1 = 0.0144 + 0.00392 = 0.01832
    $$

    **Cumulant $c_4$ (excess kurtosis related):**

    $$
    c_4 = (3\sigma^4\nu + 12\sigma^2\theta^2\nu^2 + 6\theta^4\nu^3)T
    $$

    Computing each term:

    - $3\sigma^4\nu = 3 \times (0.12)^4 \times 0.2 = 3 \times 2.0736\times 10^{-4}\times 0.2 = 1.244\times 10^{-4}$
    - $12\sigma^2\theta^2\nu^2 = 12\times 0.0144\times 0.0196\times 0.04 = 1.355\times 10^{-4}$
    - $6\theta^4\nu^3 = 6\times 3.842\times 10^{-4}\times 0.008 = 1.844\times 10^{-5}$

    $$
    c_4 = (1.244 + 1.355 + 0.1844)\times 10^{-4} \approx 2.783\times 10^{-4}
    $$

    **Truncation interval with $L = 12$:**

    $$
    c_2 + \sqrt{c_4 + 2c_2^2} = 0.01832 + \sqrt{2.783\times 10^{-4} + 2\times(0.01832)^2}
    $$

    $$
    = 0.01832 + \sqrt{2.783\times 10^{-4} + 6.712\times 10^{-4}} = 0.01832 + \sqrt{9.495\times 10^{-4}}
    $$

    $$
    = 0.01832 + 0.03081 = 0.04913
    $$

    Half-width: $L\sqrt{0.04913} = 12\times 0.2217 = 2.660$.

    $$
    [a, b] = [c_1 - 2.660,\; c_1 + 2.660]
    $$

    so $b - a = 5.32$.

    **Comparison with Black--Scholes of the same variance:** For Black--Scholes with $c_2 = 0.01832$ and $c_4 = 0$, using $L = 12$:

    $$
    c_2 + \sqrt{0 + 2c_2^2} = 0.01832 + 0.01832\sqrt{2} = 0.01832 + 0.02591 = 0.04423
    $$

    Half-width: $12\sqrt{0.04423} = 12\times 0.2103 = 2.524$, giving $b - a = 5.048$.

    The Variance Gamma interval ($b - a = 5.32$) is wider than the Black--Scholes interval ($b - a = 5.05$) by about 5.4%, reflecting the additional kurtosis of the VG model.

---

**Exercise 3.** The Chebyshev-based truncation bound gives $P(X \notin [c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]) \leq 1/L^2$. For $L = 10$, this yields $\delta \leq 0.01$. Why is this bound extremely conservative for a normal distribution? Compute the exact value of $P(|X| > 10)$ for $X \sim N(0, 1)$ and compare to the Chebyshev bound.

??? success "Solution to Exercise 3"
    The Chebyshev bound gives $P(|X| > 10) \leq 1/10^2 = 0.01$ for $X \sim N(0,1)$.

    The exact value is:

    $$
    P(|X| > 10) = 2\Phi(-10) = 2\times\frac{1}{2}\text{erfc}(10/\sqrt{2}) \approx 1.524\times 10^{-23}
    $$

    The Chebyshev bound ($0.01$) overestimates the true probability by a factor of about $6.6 \times 10^{20}$, which is roughly 21 orders of magnitude.

    **Why so conservative:** Chebyshev's inequality uses only the mean and variance of the distribution. It must hold for *all* distributions with those moments, including heavy-tailed distributions that concentrate much more mass in the tails than the Gaussian. For example, a two-point distribution $P(X = \pm 10) = 0.005$, $P(X = 0) = 0.99$ has $\text{Var}(X) = 0.5$, and for appropriately scaled versions, the Chebyshev bound is tight. The normal distribution has exponentially decaying tails ($f(x) \sim e^{-x^2/2}$), which makes the polynomial Chebyshev bound absurdly loose. The exponential tail bound $P(|X| > L) \approx 2e^{-L^2/2}$ is much tighter and nearly exact for the Gaussian.

---

**Exercise 4.** Explain the interaction between the truncation interval width $b - a$ and the COS convergence rate. If $[a, b]$ is widened by a factor of 2, how does this affect (a) the truncation error $\varepsilon_1$, (b) the cosine frequencies $\omega_k = k\pi/(b-a)$, and (c) the number of terms $N$ needed for a given series truncation error $\varepsilon_2$? What is the optimal balance?

??? success "Solution to Exercise 4"
    **(a) Effect on truncation error $\varepsilon_1$:** Widening $[a, b]$ by a factor of 2 captures more probability mass, reducing $\delta = P(X \notin [a,b])$. For sub-Gaussian tails, $\delta$ decreases exponentially with the interval half-width, so doubling the interval reduces $\varepsilon_1$ dramatically (e.g., from $10^{-20}$ to $10^{-80}$ for a Gaussian).

    **(b) Effect on cosine frequencies:** The frequencies are $\omega_k = k\pi/(b-a)$. Doubling $b - a$ halves all frequencies: $\omega_k^{\text{new}} = k\pi/(2(b-a)) = \omega_k/2$. This means the cosine basis functions oscillate more slowly, and the series needs more terms to capture the same level of detail in the density.

    **(c) Effect on $N$:** The exponential convergence rate is $\varepsilon_2 \sim e^{-\beta N\pi/(b-a)}$. Doubling $b - a$ halves the exponent, so to maintain the same $\varepsilon_2$, we need to double $N$. More precisely, if $N_1$ terms suffice for interval $b - a$, then $N_2 = 2N_1$ terms are needed for interval $2(b - a)$ to achieve the same series error.

    **Optimal balance:** The optimal $[a, b]$ minimizes the total error $\varepsilon_1 + \varepsilon_2$. Since $\varepsilon_1$ decreases exponentially with the interval width while $\varepsilon_2$ increases (for fixed $N$), the optimum occurs where both errors are comparable. In practice, the truncation error is already negligible ($< 10^{-15}$) for $L = 10$, so the series error dominates and the interval should be kept as narrow as possible while maintaining negligible truncation error.

---

**Exercise 5.** The diagnostic check "$A_0(b-a)/2 \approx 1$" verifies proper truncation. For a correctly truncated density, $A_0 = 2/(b-a)\int_a^b f(x)\,dx \approx 2/(b-a)$, so $A_0(b-a)/2 \approx 1$. If you observe $A_0(b-a)/2 = 0.95$, what does this indicate about the truncation interval? Estimate the fraction of probability mass outside $[a, b]$.

??? success "Solution to Exercise 5"
    If $A_0(b-a)/2 = 0.95$, then:

    $$
    \frac{b-a}{2}\cdot\frac{2}{b-a}\int_a^b f(x)\,dx = \int_a^b f(x)\,dx = 0.95
    $$

    Since $\int_{-\infty}^{\infty}f(x)\,dx = 1$ for a probability density, the fraction of probability mass outside $[a, b]$ is:

    $$
    P(X \notin [a, b]) = 1 - \int_a^b f(x)\,dx = 1 - 0.95 = 0.05
    $$

    This means 5% of the probability mass lies outside the truncation interval, which is far too much for accurate pricing. The resulting truncation error bound is $|\varepsilon_k| \leq 2\times 0.05/(b-a) = 0.1/(b-a)$, which can lead to significant price errors.

    This situation indicates the truncation interval is too narrow. The remedy is to increase $L$ (e.g., from 6 to 10 or 12) or check whether the cumulant computation is correct. For a properly truncated density with $L = 10$, one should observe $A_0(b-a)/2 > 1 - 10^{-15}$.

---

**Exercise 6.** For very short maturities ($T = 0.001$), the density concentrates sharply near the forward price. Compute $c_2 = \sigma^2 T$ for $\sigma = 0.20$ and determine the half-width $L\sqrt{c_2}$ with $L = 10$. Explain why the COS method requires many more terms $N$ for short maturities even though the truncation interval is narrow, and suggest a practical strategy for handling this regime.

---

??? success "Solution to Exercise 6"
    For $\sigma = 0.20$ and $T = 0.001$:

    $$
    c_2 = \sigma^2 T = 0.04\times 0.001 = 4\times 10^{-5}
    $$

    The half-width is:

    $$
    L\sqrt{c_2} = 10\sqrt{4\times 10^{-5}} = 10\times 6.325\times 10^{-3} = 0.06325
    $$

    So $b - a = 2\times 0.06325 = 0.1265$, a very narrow interval.

    **Why many terms $N$ are needed:** The density peak height is proportional to $1/\sqrt{c_2} = 1/\sqrt{4\times 10^{-5}} \approx 158$, meaning the density is very tall and sharply peaked. Although the truncation interval is narrow, the cosine series on $[a, b]$ has basis functions with frequencies $\omega_k = k\pi/(b-a) = k\pi/0.1265$. The density changes rapidly relative to $b - a$, but the key issue is that the *absolute* number of oscillations needed to resolve the density shape is determined by the density's intrinsic smoothness, not the interval width.

    More precisely, the analyticity strip width $\beta$ (in absolute terms) is roughly independent of $T$ for the Black--Scholes model, but $b - a \propto \sqrt{T}$. The convergence rate $e^{-\beta N\pi/(b-a)}$ improves with smaller $b - a$ only if $\beta$ scales the same way. For log-normal densities, the Gaussian decay of coefficients gives $|A_k| \sim e^{-\sigma^2 T k^2\pi^2/(2(b-a)^2)}$. With $b - a = 2L\sigma\sqrt{T}$, this becomes $|A_k| \sim e^{-k^2\pi^2/(8L^2)}$, which is actually independent of $T$. So in the Black--Scholes case, $N$ does not grow with decreasing $T$.

    However, for stochastic volatility models, short maturities produce densities with sharper features (near-ATM kinks from discrete monitoring, or mixed distributions from variance process), requiring more terms. The practical strategy is:

    1. Use a fine grid of $N$ values and check convergence empirically via Richardson extrapolation.
    2. Scale $N$ inversely with $\sqrt{T}$ as a starting heuristic for non-Gaussian models.
    3. Consider alternative methods (FFT or direct quadrature) for very short maturities where the COS method requires $N > 500$.
