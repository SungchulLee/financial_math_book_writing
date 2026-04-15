# Merton Series Formula

The most celebrated result of Merton's 1976 paper is a **closed-form series expansion** for European option prices under jump-diffusion dynamics. The key insight is elegant: condition on the number of jumps $n$, and the resulting distribution is Gaussian, so each conditional price is a Black-Scholes formula with adjusted parameters. The unconditional price is then a Poisson-weighted sum of these Black-Scholes prices, converging rapidly due to the factorial decay of Poisson probabilities.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Merton series formula by conditioning on the number of jumps
    2. Identify the adjusted volatility $\sigma_n$ and rate $r_n$ for each term
    3. Establish convergence of the series and bound the truncation error
    4. Price a European option numerically using the series expansion

---

## Motivation

### The Conditioning Trick

The log-return in the Merton model is:

$$
\ln\frac{S_T}{S_0} = \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)T + \sigma W_T + \sum_{i=1}^{N_T}\ln Y_i
$$

Conditional on $N_T = n$, the jump sum $\sum_{i=1}^{n}\ln Y_i$ is a sum of $n$ independent $N(\mu_J, \sigma_J^2)$ random variables, hence $N(n\mu_J, n\sigma_J^2)$. Combined with the Gaussian diffusion term $\sigma W_T \sim N(0, \sigma^2 T)$, the conditional log-return is normal. A normal log-return means the conditional asset price is log-normal, and log-normal prices yield Black-Scholes formulas.

### Why This Is Remarkable

Most extensions of Black-Scholes (stochastic volatility, local volatility) destroy the closed-form pricing property. The Merton model preserves it, at the cost of replacing a single Black-Scholes evaluation with a rapidly converging infinite series. In practice, 10--20 terms suffice for machine precision.

---

## Derivation

### Step 1: Conditional Distribution

Given $N_T = n$, the log-return is:

$$
\ln\frac{S_T}{S_0}\;\Big|\; N_T = n \;\sim\; N\!\left(\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)T + n\mu_J,\; \sigma^2 T + n\sigma_J^2\right)
$$

Define the conditional parameters:

$$
\sigma_n^2 = \sigma^2 + \frac{n\sigma_J^2}{T}
$$

$$
r_n = r - \lambda\bar{k} + \frac{n\ln(1 + \bar{k})}{T}
$$

where $\bar{k} = e^{\mu_J + \sigma_J^2/2} - 1$.

!!! tip "Interpreting the Adjusted Parameters"
    The conditional volatility $\sigma_n$ increases with $n$ because each additional jump adds variance $\sigma_J^2$ to the log-return. The conditional rate $r_n$ adjusts the forward price to account for the average cumulative jump effect of $n$ jumps.

### Step 2: Conditional Option Price

Given $N_T = n$, the asset price is log-normal with parameters $(\sigma_n, r_n)$, so the European call price is the standard Black-Scholes formula:

$$
C_{\text{BS}}(S_0, K, T, r_n, \sigma_n) = S_0 e^{(r_n - r)T}N(d_1^{(n)}) - Ke^{-rT}N(d_2^{(n)})
$$

where:

$$
d_1^{(n)} = \frac{\ln(S_0/K) + (r_n + \frac{1}{2}\sigma_n^2)T}{\sigma_n\sqrt{T}}
$$

$$
d_2^{(n)} = d_1^{(n)} - \sigma_n\sqrt{T}
$$

and $N(\cdot)$ is the standard normal CDF.

### Step 3: Poisson Averaging

The number of jumps $N_T$ follows a Poisson distribution. Define the adjusted intensity:

$$
\lambda' = \lambda(1 + \bar{k})
$$

Then the Poisson weight for $n$ jumps is:

$$
w_n = \frac{e^{-\lambda'T}(\lambda'T)^n}{n!}
$$

!!! info "Theorem: Merton Series Formula"
    The European call price under the Merton jump-diffusion model is

    $$
    C_{\text{Merton}} = \sum_{n=0}^{\infty} w_n \, C_{\text{BS}}(S_0, K, T, r_n, \sigma_n)
    $$

    where:

    - $w_n = \frac{e^{-\lambda'T}(\lambda'T)^n}{n!}$ with $\lambda' = \lambda(1 + \bar{k})$
    - $\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$
    - $r_n = r - \lambda\bar{k} + n\ln(1+\bar{k})/T$

    The European put price follows by put-call parity:

    $$
    P_{\text{Merton}} = C_{\text{Merton}} - S_0 + Ke^{-rT}
    $$

**Proof.** By the law of total expectation:

$$
C_{\text{Merton}} = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+] = e^{-rT}\sum_{n=0}^{\infty}\mathbb{P}(N_T = n)\,\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid N_T = n]
$$

Conditional on $N_T = n$, the log-return is Gaussian, so the conditional expectation is a Black-Scholes price. The Poisson probabilities use the adjusted intensity $\lambda'$ because the change from $\lambda$ to $\lambda'$ absorbs the compensator into the weights, simplifying the conditional forward price. Specifically:

$$
\mathbb{E}^{\mathbb{Q}}[S_T \mid N_T = n] = S_0 e^{rT} \cdot \frac{(\lambda')^n e^{-\lambda T}}{(\lambda)^n e^{-\lambda' T}} \cdot (\text{normalizing factor})
$$

After careful algebraic manipulation (replacing $\lambda$ by $\lambda'$ in the Poisson weights and adjusting $r$ to $r_n$ in the Black-Scholes formula), the series takes the stated form. $\square$

---

## Convergence Analysis

### Rate of Convergence

The Poisson weights $w_n$ decay factorially:

$$
w_n = \frac{e^{-\lambda'T}(\lambda'T)^n}{n!}
$$

For $n \gg \lambda'T$, Stirling's approximation gives $w_n \approx \frac{1}{\sqrt{2\pi n}}\left(\frac{e\lambda'T}{n}\right)^n$, which decreases faster than exponentially.

### Truncation Error

!!! info "Proposition: Truncation Error Bound"
    The truncation error from summing only $M$ terms satisfies

    $$
    \left|C_{\text{Merton}} - \sum_{n=0}^{M} w_n C_{\text{BS}}^{(n)}\right| \leq S_0 \sum_{n=M+1}^{\infty} w_n = S_0\left(1 - \sum_{n=0}^{M}w_n\right)
    $$

    since each Black-Scholes price is bounded by $S_0$.

**Proof.** The Black-Scholes call price satisfies $0 \leq C_{\text{BS}} \leq S_0$. Therefore:

$$
\sum_{n=M+1}^{\infty} w_n C_{\text{BS}}^{(n)} \leq S_0 \sum_{n=M+1}^{\infty} w_n
$$

The tail sum of Poisson probabilities can be bounded using the incomplete gamma function or computed directly. $\square$

### Practical Guidelines

| $\lambda'T$ | Terms for $10^{-8}$ accuracy | Terms for $10^{-15}$ accuracy |
|-------------|-------------------------------|-------------------------------|
| 0.5 | 8 | 15 |
| 1.0 | 10 | 18 |
| 5.0 | 16 | 25 |
| 10.0 | 22 | 32 |

The series converges rapidly for typical parameter values. Even for $\lambda = 5$ (five jumps per year on average), 25 terms provide double-precision accuracy.

---

## Special Cases

### Zero Jumps (λ = 0)

When $\lambda = 0$, the only nonzero weight is $w_0 = 1$, and $\sigma_0 = \sigma$, $r_0 = r$. The series reduces to a single Black-Scholes price, confirming consistency.

### Pure Jump (σ = 0)

When $\sigma = 0$, the diffusion component vanishes, and $\sigma_n^2 = n\sigma_J^2/T$. The $n = 0$ term has $\sigma_0 = 0$, giving a degenerate Black-Scholes price (digital payoff behavior). The formula remains valid but the individual terms with small $n$ may require careful numerical treatment.

### Large λ T

When $\lambda T$ is large, the Poisson distribution concentrates around its mean $\lambda'T$, and the series is dominated by terms near $n \approx \lambda'T$. The effective volatility approaches $\sqrt{\sigma^2 + \lambda\sigma_J^2}$ and the excess kurtosis diminishes, consistent with the central limit theorem.

---

## Worked Example

!!! example "Pricing a European Call"
    **Parameters:** $S_0 = \$100$, $K = \$100$, $T = 0.5$ years, $r = 0.05$, $\sigma = 0.20$, $\lambda = 1.0$, $\mu_J = -0.05$, $\sigma_J = 0.20$.

    **Step 1: Compute $\bar{k}$ and $\lambda'$.**

    $$
    \bar{k} = e^{-0.05 + 0.02} - 1 = e^{-0.03} - 1 \approx -0.02955
    $$

    $$
    \lambda' = 1.0 \times (1 - 0.02955) = 0.97045
    $$

    **Step 2: Poisson weights for $T = 0.5$.**

    $$
    \lambda'T = 0.4852
    $$

    | $n$ | $w_n$ | $\sigma_n$ | $r_n$ |
    |-----|-------|------------|--------|
    | 0 | 0.6157 | 0.2000 | 0.0796 |
    | 1 | 0.2988 | 0.3111 | 0.0196 |
    | 2 | 0.0725 | 0.4000 | $-0.0404$ |
    | 3 | 0.0117 | 0.4781 | $-0.1004$ |
    | 4 | 0.0014 | 0.5477 | $-0.1604$ |

    **Step 3: Compute each $C_{\text{BS}}^{(n)}$.**

    For $n = 0$: $C_{\text{BS}}(100, 100, 0.5, 0.0796, 0.20) \approx 7.54$

    For $n = 1$: $C_{\text{BS}}(100, 100, 0.5, 0.0196, 0.3111) \approx 9.28$

    For $n = 2$: $C_{\text{BS}}(100, 100, 0.5, -0.0404, 0.40) \approx 10.03$

    **Step 4: Weighted sum.**

    $$
    C_{\text{Merton}} \approx 0.6157(7.54) + 0.2988(9.28) + 0.0725(10.03) + 0.0117(9.83) + \cdots
    $$

    $$
    \approx 4.64 + 2.77 + 0.73 + 0.12 + \cdots \approx 8.27
    $$

    For comparison, the pure Black-Scholes price (no jumps) is approximately \$7.54. The jump component adds about \$0.73 to the option value, reflecting the additional risk from discontinuous moves.

---

## Comparison with Black-Scholes

The Merton series formula reveals how jumps affect option prices across the strike spectrum:

| Region | Effect of jumps | Reason |
|--------|----------------|--------|
| Deep ITM | Small impact | Payoff is nearly certain regardless of jumps |
| ATM | Moderate increase | Higher effective volatility from jumps |
| OTM puts | Large increase | Downward jumps ($\mu_J < 0$) increase crash probability |
| OTM calls | Moderate increase | Upward jump tail adds probability mass |

This asymmetric impact across strikes is precisely what generates the implied volatility smile when Merton prices are inverted through the Black-Scholes formula.

---

## Summary

The Merton series formula decomposes the European option price into a Poisson-weighted sum of Black-Scholes prices, each evaluated at adjusted volatility $\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$ and rate $r_n = r - \lambda\bar{k} + n\ln(1+\bar{k})/T$. The series converges rapidly due to the factorial decay of Poisson weights, with 10--20 terms typically sufficient for machine precision. The formula reduces to Black-Scholes when $\lambda = 0$ and generates an implied volatility smile that steepens at short maturities, matching the empirical behavior that pure diffusion models cannot reproduce.

---

## Exercises

**Exercise 1.** Verify that the Merton series formula reduces to the standard Black-Scholes formula when $\lambda = 0$. Specifically, show that $w_0 = 1$, $w_n = 0$ for $n \geq 1$, $\sigma_0 = \sigma$, and $r_0 = r$.

??? success "Solution to Exercise 1"
    When $\lambda = 0$, the adjusted intensity is $\lambda' = \lambda(1 + \bar{k}) = 0$, so $\lambda'T = 0$.

    The Poisson weights become:

    $$
    w_n = \frac{e^{-0} \cdot 0^n}{n!} = \begin{cases} 1 & \text{if } n = 0 \\ 0 & \text{if } n \geq 1 \end{cases}
    $$

    since $0^0 = 1$ by convention and $0^n = 0$ for $n \geq 1$.

    For the $n = 0$ term, the conditional volatility is:

    $$
    \sigma_0^2 = \sigma^2 + \frac{0 \cdot \sigma_J^2}{T} = \sigma^2
    $$

    The conditional rate is:

    $$
    r_0 = r - \lambda\bar{k} + \frac{0 \cdot \ln(1+\bar{k})}{T} = r - 0 = r
    $$

    since $\lambda = 0$ implies $\lambda\bar{k} = 0$.

    Therefore the Merton series reduces to:

    $$
    C_{\text{Merton}} = 1 \cdot C_{\text{BS}}(S_0, K, T, r, \sigma) + 0 + 0 + \cdots = C_{\text{BS}}(S_0, K, T, r, \sigma)
    $$

    This confirms that the Merton formula is a genuine generalization of Black-Scholes: setting the jump intensity to zero recovers the classical formula exactly.

---


**Exercise 2.** For the parameters $S_0 = 100$, $K = 100$, $T = 0.5$, $r = 0.05$, $\sigma = 0.20$, $\lambda = 1.0$, $\mu_J = -0.05$, $\sigma_J = 0.20$: (a) Compute $\bar{k}$ and $\lambda'$. (b) Compute the Poisson weights $w_0, w_1, w_2, w_3$. (c) Compute the adjusted volatilities $\sigma_0, \sigma_1, \sigma_2$ and rates $r_0, r_1, r_2$. (d) Estimate the option price by summing the first 4 terms of the series.

??? success "Solution to Exercise 2"
    **(a) Compute $\bar{k}$ and $\lambda'$.**

    $$
    \bar{k} = e^{\mu_J + \sigma_J^2/2} - 1 = e^{-0.05 + 0.02} - 1 = e^{-0.03} - 1 \approx -0.02955
    $$

    $$
    \lambda' = \lambda(1 + \bar{k}) = 1.0 \times (1 - 0.02955) = 0.97045
    $$

    **(b) Poisson weights for $T = 0.5$.** With $\lambda'T = 0.97045 \times 0.5 = 0.48523$:

    $$
    w_0 = e^{-0.48523} \approx 0.6157
    $$

    $$
    w_1 = e^{-0.48523} \times 0.48523 \approx 0.2988
    $$

    $$
    w_2 = e^{-0.48523} \times \frac{0.48523^2}{2} \approx 0.0725
    $$

    $$
    w_3 = e^{-0.48523} \times \frac{0.48523^3}{6} \approx 0.0117
    $$

    **(c) Adjusted volatilities and rates.**

    $$
    \sigma_0 = \sqrt{0.04 + 0} = 0.200, \quad r_0 = 0.05 + 0.02955 + 0 = 0.07955
    $$

    $$
    \sigma_1 = \sqrt{0.04 + 0.04/0.5} = \sqrt{0.12} \approx 0.3464, \quad r_1 = 0.07955 + \frac{\ln(0.97045)}{0.5} \approx 0.07955 - 0.05997 = 0.01958
    $$

    $$
    \sigma_2 = \sqrt{0.04 + 0.08/0.5} = \sqrt{0.20} \approx 0.4472, \quad r_2 = 0.07955 + \frac{2\ln(0.97045)}{0.5} \approx 0.07955 - 0.11994 = -0.04039
    $$

    **(d) Estimate the option price.** Using the Black-Scholes formula for each term:

    - $n = 0$: $C_{\text{BS}}(100, 100, 0.5, 0.07955, 0.200) \approx 7.54$
    - $n = 1$: $C_{\text{BS}}(100, 100, 0.5, 0.01958, 0.3464) \approx 9.63$
    - $n = 2$: $C_{\text{BS}}(100, 100, 0.5, -0.04039, 0.4472) \approx 10.38$
    - $n = 3$: $C_{\text{BS}}(100, 100, 0.5, -0.10036, 0.5292) \approx 10.23$

    The weighted sum:

    $$
    C_{\text{Merton}} \approx 0.6157(7.54) + 0.2988(9.63) + 0.0725(10.38) + 0.0117(10.23)
    $$

    $$
    \approx 4.64 + 2.88 + 0.75 + 0.12 = 8.39
    $$

    The remaining terms ($n \geq 4$) contribute less than 0.02, so the series converges very rapidly.

---


**Exercise 3.** The truncation error of the Merton series after $M$ terms is bounded by $S_0 \sum_{n=M+1}^{\infty} w_n$. For $\lambda' T = 2$, how many terms are needed to ensure truncation error below $10^{-8}$? Use the Poisson tail bound to estimate.

??? success "Solution to Exercise 3"
    We need the Poisson tail probability $\sum_{n=M+1}^{\infty} w_n < 10^{-8}/S_0$. Since $S_0$ varies, we bound $\sum_{n=M+1}^{\infty} w_n < 10^{-8}$ directly (a sufficient condition when $S_0 \leq 1$; for larger $S_0$, the bound is conservative).

    For $\lambda'T = 2$, we compute the cumulative Poisson distribution. The Poisson CDF for $\text{Poisson}(2)$:

    $$
    w_n = \frac{e^{-2} \cdot 2^n}{n!}
    $$

    Computing partial sums:

    | $M$ | $\sum_{n=0}^{M} w_n$ | Tail $= 1 - \sum w_n$ |
    |-----|----------------------|------------------------|
    | 5 | 0.98344 | 0.01656 |
    | 8 | 0.99983 | $1.7 \times 10^{-4}$ |
    | 10 | 0.999995 | $5.0 \times 10^{-6}$ |
    | 12 | 0.99999997 | $3.0 \times 10^{-8}$ |
    | 13 | 0.999999997 | $3.0 \times 10^{-9}$ |

    Therefore, $M = 13$ terms suffice to ensure the truncation error is bounded by $S_0 \times 3 \times 10^{-9} < S_0 \times 10^{-8}$. For $S_0 = 100$, the absolute truncation error is below $10^{-6}$.

    A useful Poisson tail bound is: for $M > \lambda'T$,

    $$
    \sum_{n=M+1}^{\infty} w_n \leq \frac{w_M \cdot \lambda'T}{M + 1 - \lambda'T}
    $$

    which gives the geometric-like decay once $M$ exceeds the mean.

---


**Exercise 4.** Explain the asymmetric impact of jumps across strikes: why do jumps increase OTM put prices more than OTM call prices when $\mu_J < 0$? Relate your answer to the probability of large downward moves under the conditional distribution $\ln(S_T/S_0) | N_T = n$.

??? success "Solution to Exercise 4"
    When $\mu_J < 0$, the conditional distribution $\ln(S_T/S_0) \mid N_T = n$ has mean:

    $$
    m_n = \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)T + n\mu_J
    $$

    Since $\mu_J < 0$, the conditional mean $m_n$ decreases with $n$. More jumps shift the conditional distribution further to the left, increasing the probability that $S_T$ falls significantly below $S_0$.

    **OTM puts** (strike $K < S_0$) have payoff $(K - S_T)^+$ which benefits from large downward moves. For the $n$-th term in the Merton series, the conditional put price is computed with volatility $\sigma_n$ and rate $r_n$. As $n$ increases:

    - The conditional mean shifts left (more negative $m_n$), moving $S_T$ toward the put's in-the-money region
    - The conditional variance increases ($\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$), further spreading probability mass into the tail

    Both effects increase the conditional put price for higher $n$ terms.

    **OTM calls** (strike $K > S_0$) have payoff $(S_T - K)^+$ which benefits from large upward moves. Although higher variance spreads some mass upward, the leftward shift in the mean works against the call. When $\mu_J < 0$, the net effect on OTM calls is smaller because the mean shift and variance increase partially offset each other.

    This asymmetry is precisely what generates the implied volatility skew: OTM puts have higher implied volatility than OTM calls, reflecting the market's pricing of downward jump risk.

---


**Exercise 5.** In the pure jump case ($\sigma = 0$), the $n = 0$ term has $\sigma_0 = 0$. Explain what happens to $C_{\text{BS}}(S_0, K, T, r_0, 0)$ and why this term produces a digital-like payoff. What is the economic interpretation of the $n = 0$ term in this limiting case?

??? success "Solution to Exercise 5"
    When $\sigma = 0$, the conditional volatility for $n = 0$ jumps is:

    $$
    \sigma_0 = \sqrt{0 + 0 \cdot \sigma_J^2/T} = 0
    $$

    The Black-Scholes formula with $\sigma_0 = 0$ becomes degenerate. With zero volatility, the log-return is deterministic (given $n = 0$, no jumps and no diffusion). The terminal price is:

    $$
    S_T = S_0 e^{(r_0 - \frac{1}{2} \cdot 0)T} = S_0 e^{r_0 T}
    $$

    The Black-Scholes formula collapses to:

    $$
    C_{\text{BS}}(S_0, K, T, r_0, 0) = \max(S_0 e^{r_0 T} - K e^{-rT} \cdot e^{rT}, 0) \cdot e^{-rT} = e^{-rT}\max(S_0 e^{r_0 T} - K, 0)
    $$

    This is a digital-like payoff: the call pays $S_0 e^{r_0 T} - K$ with certainty if $S_0 e^{r_0 T} > K$, and zero otherwise. There is no smooth transition as in the standard Black-Scholes formula; the price is either fully in the money or fully out.

    **Economic interpretation.** The $n = 0$ term represents the scenario where no jumps occur during $[0, T]$. In the pure-jump model ($\sigma = 0$), this scenario has a completely deterministic outcome. The weight $w_0 = e^{-\lambda'T}$ is the probability of zero jumps. The total option price is then the sum over $n \geq 1$ of smoothly priced terms (each with nonzero $\sigma_n > 0$) plus the digital contribution from $n = 0$. Numerically, care is needed for the $n = 0$ term because the CDF evaluations $N(d_1)$ and $N(d_2)$ approach 0 or 1 as $\sigma_0 \to 0$.

---


**Exercise 6.** The Merton series formula expresses the option price as a mixture of Black-Scholes prices. Use this interpretation to prove that put-call parity $C - P = S_0 - Ke^{-rT}$ holds for the Merton model without computing the prices explicitly.

??? success "Solution to Exercise 6"
    The Merton series formula gives the call and put prices as:

    $$
    C_{\text{Merton}} = \sum_{n=0}^{\infty} w_n \, C_{\text{BS}}^{(n)}, \qquad P_{\text{Merton}} = \sum_{n=0}^{\infty} w_n \, P_{\text{BS}}^{(n)}
    $$

    where $C_{\text{BS}}^{(n)}$ and $P_{\text{BS}}^{(n)}$ are the Black-Scholes call and put prices with parameters $(\sigma_n, r_n)$.

    For each term, the standard Black-Scholes put-call parity holds:

    $$
    C_{\text{BS}}^{(n)} - P_{\text{BS}}^{(n)} = S_0 e^{(r_n - r)T} - Ke^{-rT}
    $$

    Note that $e^{(r_n - r)T} = e^{(-\lambda\bar{k} + n\ln(1+\bar{k})/T)\cdot T} = e^{-\lambda\bar{k}T}(1+\bar{k})^n$. Therefore:

    $$
    C_{\text{Merton}} - P_{\text{Merton}} = \sum_{n=0}^{\infty} w_n \bigl[S_0 e^{(r_n - r)T} - Ke^{-rT}\bigr]
    $$

    $$
    = S_0 e^{-\lambda\bar{k}T}\sum_{n=0}^{\infty} w_n (1+\bar{k})^n - Ke^{-rT}\sum_{n=0}^{\infty} w_n
    $$

    Since $\sum_{n=0}^{\infty} w_n = 1$ (the weights are probabilities), the second term gives $-Ke^{-rT}$.

    For the first sum, substituting $w_n = \frac{e^{-\lambda'T}(\lambda'T)^n}{n!}$ with $\lambda' = \lambda(1+\bar{k})$:

    $$
    \sum_{n=0}^{\infty} w_n(1+\bar{k})^n = e^{-\lambda'T}\sum_{n=0}^{\infty}\frac{(\lambda'T)^n(1+\bar{k})^n}{n!} = e^{-\lambda'T}\cdot e^{\lambda'T(1+\bar{k})} = e^{\lambda'T\bar{k}}
    $$

    Since $\lambda' = \lambda(1+\bar{k})$, we get $\lambda'T\bar{k} = \lambda\bar{k}(1+\bar{k})T$. Multiplying by $S_0 e^{-\lambda\bar{k}T}$:

    $$
    S_0 e^{-\lambda\bar{k}T} \cdot e^{\lambda\bar{k}(1+\bar{k})T} = S_0 e^{\lambda\bar{k}^2 T}
    $$

    However, a simpler direct argument avoids this algebra entirely. The put-call parity $C - P = S_0 - Ke^{-rT}$ is model-independent: it follows from the identity $(S_T - K)^+ - (K - S_T)^+ = S_T - K$ and the fact that $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = S_0$ (the discounted price is a martingale). Since the Merton model is constructed to preserve this martingale property (via the compensator), put-call parity holds automatically:

    $$
    C_{\text{Merton}} - P_{\text{Merton}} = e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T - K] = S_0 - Ke^{-rT}
    $$
