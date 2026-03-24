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

### Zero Jumps ($\lambda = 0$)

When $\lambda = 0$, the only nonzero weight is $w_0 = 1$, and $\sigma_0 = \sigma$, $r_0 = r$. The series reduces to a single Black-Scholes price, confirming consistency.

### Pure Jump ($\sigma = 0$)

When $\sigma = 0$, the diffusion component vanishes, and $\sigma_n^2 = n\sigma_J^2/T$. The $n = 0$ term has $\sigma_0 = 0$, giving a degenerate Black-Scholes price (digital payoff behavior). The formula remains valid but the individual terms with small $n$ may require careful numerical treatment.

### Large $\lambda T$

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

---

**Exercise 2.** For the parameters $S_0 = 100$, $K = 100$, $T = 0.5$, $r = 0.05$, $\sigma = 0.20$, $\lambda = 1.0$, $\mu_J = -0.05$, $\sigma_J = 0.20$: (a) Compute $\bar{k}$ and $\lambda'$. (b) Compute the Poisson weights $w_0, w_1, w_2, w_3$. (c) Compute the adjusted volatilities $\sigma_0, \sigma_1, \sigma_2$ and rates $r_0, r_1, r_2$. (d) Estimate the option price by summing the first 4 terms of the series.

---

**Exercise 3.** The truncation error of the Merton series after $M$ terms is bounded by $S_0 \sum_{n=M+1}^{\infty} w_n$. For $\lambda' T = 2$, how many terms are needed to ensure truncation error below $10^{-8}$? Use the Poisson tail bound to estimate.

---

**Exercise 4.** Explain the asymmetric impact of jumps across strikes: why do jumps increase OTM put prices more than OTM call prices when $\mu_J < 0$? Relate your answer to the probability of large downward moves under the conditional distribution $\ln(S_T/S_0) | N_T = n$.

---

**Exercise 5.** In the pure jump case ($\sigma = 0$), the $n = 0$ term has $\sigma_0 = 0$. Explain what happens to $C_{\text{BS}}(S_0, K, T, r_0, 0)$ and why this term produces a digital-like payoff. What is the economic interpretation of the $n = 0$ term in this limiting case?

---

**Exercise 6.** The Merton series formula expresses the option price as a mixture of Black-Scholes prices. Use this interpretation to prove that put-call parity $C - P = S_0 - Ke^{-rT}$ holds for the Merton model without computing the prices explicitly.
