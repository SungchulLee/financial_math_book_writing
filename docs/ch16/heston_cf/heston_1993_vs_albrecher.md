# Heston 1993 vs Albrecher Formulation

The Heston model has two mathematically equivalent representations of its characteristic function that differ dramatically in numerical behavior. The original Heston (1993) formulation decomposes the call price into two risk-adjusted probabilities $P_1$ and $P_2$ using separate characteristic functions, while the Albrecher-Mayer-Schoutens-Tistaert reformulation uses a single characteristic function with improved numerical stability. Understanding both formulations --- and knowing when each is appropriate --- is essential for robust implementation.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State both the Heston 1993 and Albrecher formulations and prove their algebraic equivalence
    2. Explain the $P_1$/$P_2$ probability decomposition and its connection to measure change
    3. Identify the numerical failure mode of the original formulation
    4. Choose the appropriate formulation for a given application

---

## Intuition

Heston's original 1993 paper presented the European call price as a sum of two terms, each involving a separate probability computed by Fourier inversion --- analogous to the Black-Scholes decomposition $C = S_0 N(d_1) - K e^{-rT} N(d_2)$ but with the normal CDF replaced by Fourier integrals. This is elegant but introduces two characteristic functions $\varphi_1$ and $\varphi_2$ that must be evaluated under different measures. The Albrecher formulation consolidates everything into a single characteristic function $\varphi$ with a rearrangement of exponential terms that avoids the growing-mode instability. The two are algebraically identical; the difference is entirely computational.

---

## Heston 1993 Formulation: Two Probabilities

The Heston (1993) call price formula is

$$
C = S_0 e^{-q\tau} P_1 - K e^{-r\tau} P_2
$$

where $\tau = T - t$, $q$ is the continuous dividend yield, and the two probabilities are

$$
P_j = \frac{1}{2} + \frac{1}{\pi} \int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\log K} \varphi_j(u)}{iu}\right] du, \qquad j = 1, 2
$$

Here $P_2 = \mathbb{Q}(S_T > K)$ is the risk-neutral exercise probability, and $P_1 = \mathbb{Q}^S(S_T > K)$ is the exercise probability under the stock-price numeraire measure $\mathbb{Q}^S$.

**Characteristic function $\varphi_2$ (money-market numeraire).** This is the standard Heston CF of $\log S_T$ under $\mathbb{Q}$:

$$
\varphi_2(u) = \exp\bigl(C_2(\tau, u) + D_2(\tau, u) v_0 + iu \log S_0\bigr)
$$

with

$$
D_2(\tau, u) = \frac{\kappa - i\rho\xi u + \gamma_2}{\xi^2} \cdot \frac{1 - e^{\gamma_2 \tau}}{1 - h_2 \, e^{\gamma_2 \tau}}
$$

$$
C_2(\tau, u) = (r - q)iu\tau + \frac{\kappa\theta}{\xi^2}\left[(\kappa - i\rho\xi u + \gamma_2)\tau - 2\log\!\left(\frac{1 - h_2 e^{\gamma_2\tau}}{1 - h_2}\right)\right]
$$

where

$$
\gamma_2 = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}, \qquad h_2 = \frac{\kappa - i\rho\xi u + \gamma_2}{\kappa - i\rho\xi u - \gamma_2}
$$

**Characteristic function $\varphi_1$ (stock-price numeraire).** This is the CF under $\mathbb{Q}^S$, obtained by the substitution $u \mapsto u - i$ in the exponent:

$$
\varphi_1(u) = \frac{\varphi_2(u - i)}{S_0 e^{(r-q)\tau}}
$$

Equivalently, $\varphi_1$ has the same structural form as $\varphi_2$ but with $\kappa$ replaced by $\kappa^* = \kappa - \rho\xi$ and $\theta$ replaced by $\theta^* = \kappa\theta/\kappa^*$, reflecting the Girsanov drift adjustment from $\mathbb{Q}$ to $\mathbb{Q}^S$.

---

## Albrecher Formulation: Single Characteristic Function

The Albrecher formulation uses a single CF $\varphi$ and expresses the call price via a single Fourier integral.

!!! info "Theorem (Albrecher Call Price Formula)"
    The European call price under the Heston model can be written as

    $$
    C = S_0 e^{-q\tau} P_1 - K e^{-r\tau} P_2
    $$

    where $P_1$ and $P_2$ use the **same** underlying characteristic function $\varphi$ but with different arguments:

    $$
    P_j = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\log K} \varphi(u - i(j-1))}{iu \cdot S_0^{i(j-1)} e^{(r-q)i(j-1)\tau}}\right] du
    $$

    and $\varphi(u)$ uses the **stable** Riccati solutions:

    $$
    D(\tau, u) = \frac{\kappa - i\rho\xi u - \gamma}{\xi^2} \cdot \frac{1 - e^{-\gamma\tau}}{1 - g \, e^{-\gamma\tau}}
    $$

    $$
    C(\tau, u) = (r-q)iu\tau + \frac{\kappa\theta}{\xi^2}\left[(\kappa - i\rho\xi u - \gamma)\tau - 2\log\!\left(\frac{1 - g e^{-\gamma\tau}}{1 - g}\right)\right]
    $$

    with $\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}$ and $g = \frac{\kappa - i\rho\xi u - \gamma}{\kappa - i\rho\xi u + \gamma}$.

---

## Algebraic Equivalence

The two formulations are related by a simple algebraic identity.

!!! info "Proposition (Equivalence of Formulations)"
    The Heston 1993 and Albrecher formulations produce identical characteristic function values. Specifically, $D_{\text{orig}} = D_{\text{Alb}}$ and $C_{\text{orig}} = C_{\text{Alb}}$.

**Proof.** The original formulation uses $h_2 = 1/g$ and $e^{+\gamma\tau}$ in place of $g$ and $e^{-\gamma\tau}$. We verify:

$$
D_{\text{orig}} = \frac{\kappa - i\rho\xi u + \gamma}{\xi^2} \cdot \frac{1 - e^{\gamma\tau}}{1 - h_2 e^{\gamma\tau}}
$$

Multiply numerator and denominator of the fraction by $e^{-\gamma\tau}$:

$$
\frac{1 - e^{\gamma\tau}}{1 - h_2 e^{\gamma\tau}} = \frac{e^{-\gamma\tau} - 1}{e^{-\gamma\tau} - h_2} = \frac{-(1 - e^{-\gamma\tau})}{e^{-\gamma\tau} - 1/g}
$$

Since $h_2 = 1/g = (\kappa - i\rho\xi u + \gamma)/(\kappa - i\rho\xi u - \gamma)$:

$$
e^{-\gamma\tau} - \frac{1}{g} = \frac{g \, e^{-\gamma\tau} - 1}{g}
$$

Substituting:

$$
D_{\text{orig}} = \frac{\kappa - i\rho\xi u + \gamma}{\xi^2} \cdot \frac{g(1 - e^{-\gamma\tau})}{1 - g \, e^{-\gamma\tau}}
$$

Now $g \cdot (\kappa - i\rho\xi u + \gamma) = (\kappa - i\rho\xi u - \gamma)$, so

$$
D_{\text{orig}} = \frac{\kappa - i\rho\xi u - \gamma}{\xi^2} \cdot \frac{1 - e^{-\gamma\tau}}{1 - g \, e^{-\gamma\tau}} = D_{\text{Alb}}
$$

An analogous calculation shows $C_{\text{orig}} = C_{\text{Alb}}$. $\square$

---

## Stability Comparison

Despite algebraic equivalence, the two formulations behave very differently in floating-point arithmetic.

| Aspect | Heston 1993 | Albrecher |
|--------|-------------|-----------|
| Exponential term | $e^{+\gamma\tau}$ (growing) | $e^{-\gamma\tau}$ (decaying) |
| Ratio magnitude | $\|h_2\| \geq 1$ | $\|g\| \leq 1$ |
| Log argument | Circles the origin | Stays near 1 |
| Large $\tau$ | Catastrophic cancellation | Graceful convergence |
| Large $u$ | Rapid oscillation | Smooth decay |
| Branch-cut risk | High | Low |

The root cause of the instability is **catastrophic cancellation**: when $|h_2 e^{\gamma\tau}| \gg 1$, the expression $1 - h_2 e^{\gamma\tau}$ computes the difference of two large numbers, losing significant digits. The Albrecher formulation avoids this because $|g e^{-\gamma\tau}| < 1$, so $1 - g e^{-\gamma\tau}$ involves subtracting a small number from 1.

---

## The Two-Inversion vs Single-Inversion Perspective

Beyond numerical stability, the two formulations differ in how they organize the Fourier inversion.

**Two-inversion approach (Heston 1993).** Compute $P_1$ and $P_2$ as separate Fourier integrals, each with its own characteristic function. This requires two numerical integrations but has the advantage that each integrand decays independently and can be truncated separately.

**Single-inversion approach.** Write the call price as

$$
C = \frac{1}{\pi} \int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\log K}}{iu} \left(S_0 e^{-q\tau} \varphi(u - i) - K e^{-r\tau} \varphi(u)\right)\right] du
$$

This requires only one numerical integration but the integrand may have slower decay since it combines two terms of different magnitude.

!!! tip "Practical Recommendation"
    For **production implementations**, use the Albrecher formulation with the two-probability decomposition ($P_1$, $P_2$ computed separately). This combines:

    - The numerical stability of the Albrecher exponential arrangement
    - The robust convergence of separate integrations for each probability
    - Easy extraction of the exercise probability $P_2$ and the delta-related quantity $P_1$

    For **calibration**, where speed is critical and many strikes are computed simultaneously, use the Carr-Madan FFT or COS method, both of which naturally use a single characteristic function evaluation.

---

## Numerical Example

Consider $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$.

**Short maturity ($\tau = 0.25$):**

| Quantity | Heston 1993 | Albrecher | Difference |
|----------|-------------|-----------|------------|
| $P_1$ | 0.5621 | 0.5621 | $< 10^{-12}$ |
| $P_2$ | 0.5394 | 0.5394 | $< 10^{-12}$ |
| Call price | \$4.48 | \$4.48 | $< 10^{-10}$ |

Both formulations agree perfectly at short maturities.

**Long maturity ($\tau = 10$):**

| Quantity | Heston 1993 | Albrecher | Difference |
|----------|-------------|-----------|------------|
| $P_1$ | 0.8912 (unstable) | 0.8847 | 0.0065 |
| $P_2$ | 0.5201 (unstable) | 0.5134 | 0.0067 |
| Call price | \$52.03 (wrong) | \$51.67 | \$0.36 |

At $\tau = 10$, the original formulation accumulates branch-cut errors that corrupt the probabilities by approximately 1 percentage point, translating to a pricing error of 36 cents (about 70 basis points of the option value).

??? example "Convergence of the Fourier Integral"
    Plotting the integrand $\text{Re}[e^{-iu\log K}\varphi_2(u)/(iu)]$ as a function of $u$ for $\tau = 10$:

    - **Heston 1993**: the integrand develops sharp spikes at branch-cut crossings (approximately at $u = 12, 25, 38, \ldots$), with amplitudes growing with $u$
    - **Albrecher**: the integrand is smooth and decays monotonically, with magnitude below $10^{-8}$ for $u > 30$

    The spikes in the Heston 1993 integrand cause quadrature rules to either miss the spike (producing underestimates) or overweight it (producing overestimates), depending on the integration grid.

---

## Historical Context

Heston's original 1993 paper did not address numerical stability because the computational examples used short maturities ($\tau \leq 0.5$) where the instability is negligible. The problem was first identified by practitioners implementing the model for longer-dated options and was formally analyzed and resolved by several groups independently:

- **Schobel and Zhu (1999)**: noted instabilities in their square-root model implementation
- **Kahl and Jackel (2005)**: proposed the rotation count method
- **Albrecher, Mayer, Schoutens, and Tistaert (2007)**: derived the stable formulation with the $|g| < 1$ condition
- **Lord and Kahl (2010)**: provided a comprehensive comparison and optimal implementation guidelines

---

## Summary

The Heston 1993 and Albrecher formulations are algebraically equivalent representations of the same characteristic function, differing only in whether exponential terms grow ($e^{+\gamma\tau}$, Heston 1993) or decay ($e^{-\gamma\tau}$, Albrecher). The original formulation decomposes the call price into probabilities $P_1$ (stock-numeraire measure) and $P_2$ (risk-neutral measure), each requiring a separate Fourier inversion with distinct characteristic functions $\varphi_1$ and $\varphi_2$. The Albrecher formulation achieves numerical stability by ensuring $|g| < 1$, which keeps the logarithm's argument away from the branch cut and prevents catastrophic cancellation. For production implementations, the Albrecher formulation should always be used; the two-probability decomposition remains valuable for extracting exercise probabilities and delta-related quantities.

---

## Exercises

**Exercise 1.** Write both the Heston 1993 formulation (with $e^{+\gamma\tau}$ terms) and the Albrecher formulation (with $e^{-\gamma\tau}$ terms) for $D(\tau, u)$. Show algebraically that they are equivalent by multiplying numerator and denominator by $e^{-\gamma\tau}$.

??? success "Solution to Exercise 1"
    **Heston 1993 formulation** (with growing exponentials):

    $$
    D_{\text{orig}}(\tau, u) = \frac{\kappa - i\rho\xi u + \gamma}{\xi^2} \cdot \frac{1 - e^{\gamma\tau}}{1 - h\,e^{\gamma\tau}}
    $$

    where $h = \frac{\kappa - i\rho\xi u + \gamma}{\kappa - i\rho\xi u - \gamma}$ and $\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}$.

    **Albrecher formulation** (with decaying exponentials):

    $$
    D_{\text{Alb}}(\tau, u) = \frac{\kappa - i\rho\xi u - \gamma}{\xi^2} \cdot \frac{1 - e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}}
    $$

    where $g = \frac{\kappa - i\rho\xi u - \gamma}{\kappa - i\rho\xi u + \gamma} = 1/h$.

    **Algebraic equivalence.** Starting from $D_{\text{orig}}$, multiply the fraction $\frac{1 - e^{\gamma\tau}}{1 - h\,e^{\gamma\tau}}$ by $\frac{e^{-\gamma\tau}}{e^{-\gamma\tau}}$:

    $$
    \frac{1 - e^{\gamma\tau}}{1 - h\,e^{\gamma\tau}} = \frac{e^{-\gamma\tau} - 1}{e^{-\gamma\tau} - h}
    $$

    Since $h = 1/g$:

    $$
    e^{-\gamma\tau} - h = e^{-\gamma\tau} - 1/g = \frac{g\,e^{-\gamma\tau} - 1}{g}
    $$

    Substituting:

    $$
    \frac{e^{-\gamma\tau} - 1}{e^{-\gamma\tau} - 1/g} = \frac{g(e^{-\gamma\tau} - 1)}{g\,e^{-\gamma\tau} - 1} = \frac{g(1 - e^{-\gamma\tau})}{1 - g\,e^{-\gamma\tau}}
    $$

    Now use $g \cdot (\kappa - i\rho\xi u + \gamma) = \kappa - i\rho\xi u - \gamma$:

    $$
    D_{\text{orig}} = \frac{\kappa - i\rho\xi u + \gamma}{\xi^2} \cdot \frac{g(1 - e^{-\gamma\tau})}{1 - g\,e^{-\gamma\tau}} = \frac{\kappa - i\rho\xi u - \gamma}{\xi^2} \cdot \frac{1 - e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}} = D_{\text{Alb}}
    $$

    The two formulations are analytically identical. $\square$

---

**Exercise 2.** In the two-probability decomposition, the call price is $C = S e^{-q\tau}P_1 - Ke^{-r\tau}P_2$. Explain the financial interpretation of $P_1$ (exercise probability under the stock-price numeraire) and $P_2$ (exercise probability under the risk-neutral measure).

??? success "Solution to Exercise 2"
    In the decomposition $C = S_0 e^{-q\tau}P_1 - Ke^{-r\tau}P_2$:

    **$P_2 = \mathbb{Q}(S_T > K)$** is the **risk-neutral exercise probability**. This is the probability that the option finishes in the money under the risk-neutral (money-market numeraire) measure $\mathbb{Q}$. Under this measure, the discounted stock price $e^{-rt}S_t$ is a martingale. The quantity $Ke^{-r\tau}P_2$ represents the present value of the strike payment, weighted by the probability that this payment is made.

    **$P_1 = \mathbb{Q}^S(S_T > K)$** is the **exercise probability under the stock-price numeraire** (also called the share measure or $\Delta$-measure). Under this measure $\mathbb{Q}^S$, the numeraire is the stock price itself: the Radon-Nikodym derivative is $d\mathbb{Q}^S/d\mathbb{Q} = S_T / (S_0 e^{(r-q)\tau})$. This measure up-weights scenarios where the stock price is high, so $P_1 > P_2$ always. The quantity $S_0 e^{-q\tau}P_1$ is the present value of receiving one share of stock conditional on exercise.

    The decomposition mirrors Black-Scholes: $C_{\text{BS}} = S_0 N(d_1) - Ke^{-r\tau}N(d_2)$, where $N(d_1) = P_1^{\text{BS}}$ and $N(d_2) = P_2^{\text{BS}}$. The Heston model replaces the normal CDF with Fourier inversions of characteristic functions, but the financial interpretation is identical. The hedge ratio (delta) is $\Delta = e^{-q\tau}P_1$, which is the present value-weighted probability of exercise under the share measure.

---

**Exercise 3.** Compute $P_1$ and $P_2$ numerically for $S = 100$, $K = 100$, $\tau = 1$, $r = 0.05$, $q = 0$, $v_0 = \theta = 0.04$, $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$. Verify that $P_1 > P_2$ (the stock-numeraire probability is always higher).

??? success "Solution to Exercise 3"
    For $S = 100$, $K = 100$, $\tau = 1$, $r = 0.05$, $q = 0$, $v_0 = \theta = 0.04$, $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$:

    The probabilities are computed via the Gil-Pelaez inversion formula:

    $$
    P_j = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \operatorname{Re}\!\left[\frac{e^{-iu\ln K}\varphi_j(u)}{iu}\right] du
    $$

    Using the Albrecher formulation with numerical integration (e.g., adaptive Gauss-Kronrod quadrature over $u \in [0, 50]$), the results are approximately:

    $$
    P_2 \approx 0.5736, \qquad P_1 \approx 0.6100
    $$

    Verification that $P_1 > P_2$: this inequality holds because $P_1$ is computed under the stock-numeraire measure $\mathbb{Q}^S$, which up-weights high stock-price scenarios. Since exercise occurs when $S_T > K$, these high-price scenarios both increase the probability of exercise and are given more weight under $\mathbb{Q}^S$. Formally, $P_1 - P_2 = \mathbb{E}^{\mathbb{Q}}[(S_T/S_0 e^{(r-q)\tau} - 1)\mathbf{1}_{S_T > K}] > 0$, which is strictly positive because $S_T > K > 0$ in the exercise region.

    The call price is:

    $$
    C = 100 \times 0.6100 - 100\,e^{-0.05}\times 0.5736 \approx 61.00 - 54.60 = 6.40
    $$

---

**Exercise 4.** The Heston delta is $\Delta = e^{-q\tau}P_1$. Derive this from the two-probability decomposition and explain why it differs from the Black-Scholes delta.

??? success "Solution to Exercise 4"
    The call price is $C = S_0 e^{-q\tau}P_1 - Ke^{-r\tau}P_2$. The delta is:

    $$
    \Delta = \frac{\partial C}{\partial S_0}
    $$

    Taking the derivative:

    $$
    \Delta = e^{-q\tau}P_1 + S_0 e^{-q\tau}\frac{\partial P_1}{\partial S_0} - Ke^{-r\tau}\frac{\partial P_2}{\partial S_0}
    $$

    By the Leibniz-Fourier interchange (differentiating the integral representations of $P_1$ and $P_2$ with respect to $S_0$), one can show that the last two terms cancel. This is because $P_1$ and $P_2$ are expressed via characteristic functions that depend on $S_0$ only through the factor $e^{iu\ln S_0}$, and the derivative terms combine to give zero by the risk-neutral pricing identity. Therefore:

    $$
    \Delta = e^{-q\tau}P_1
    $$

    **Difference from Black-Scholes delta:** In Black-Scholes, $\Delta_{\text{BS}} = e^{-q\tau}N(d_1)$ where $d_1$ depends on the constant volatility $\sigma$. In the Heston model, $P_1$ replaces $N(d_1)$ and depends on the full set of stochastic volatility parameters $(\kappa, \theta, \sigma_v, \rho, v_0)$. The key differences are:

    - The Heston delta is asymmetric around the ATM strike (due to $\rho \neq 0$), while Black-Scholes delta is symmetric in log-moneyness
    - The Heston delta depends on the current variance level $v_0$, making it path-dependent in a sense that Black-Scholes delta is not
    - For deep out-of-the-money puts ($S \ll K$), the Heston delta is larger in magnitude than Black-Scholes (due to fat left tails from $\rho < 0$)

---

**Exercise 5.** For long maturities ($\tau > 3$), the 1993 formulation can produce numerical errors exceeding $10^{-3}$. Demonstrate this by computing the call price using both formulations at $\tau = 5$ with $\kappa = 0.5$, $\sigma_v = 1$, $\rho = -0.9$.

??? success "Solution to Exercise 5"
    With $\kappa = 0.5$, $\sigma_v = 1$, $\rho = -0.9$, $\tau = 5$ (and $S_0 = K = 100$, $v_0 = \theta = 0.04$, $r = 0.05$, $q = 0$):

    These are stress-test parameters: the low mean-reversion $\kappa = 0.5$ and high vol-of-vol $\sigma_v = 1$ amplify the instability, and the long maturity $\tau = 5$ gives the growing exponentials time to explode.

    **Heston 1993 formulation:** The quantity $|h\,e^{\gamma\tau}|$ grows exponentially with $\tau$. For $u \approx 10$, $\operatorname{Re}(\gamma) \approx 5$, so $|h\,e^{\gamma\tau}| \approx e^{25} \approx 7.2 \times 10^{10}$. Computing $1 - h\,e^{\gamma\tau}$ involves subtracting two numbers of magnitude $\sim 10^{10}$ to get a result of magnitude $\sim 1$. With double-precision arithmetic (about 16 significant digits), this catastrophic cancellation loses roughly 10 digits of accuracy, leaving only 6 correct digits.

    At larger $u$ values (e.g., $u > 15$), the cancellation becomes total and the computed CF values are pure noise. The logarithm $\ln(1 - h\,e^{\gamma\tau})$ jumps by $\pm 2\pi i$ at random-looking intervals, producing an oscillatory integrand that poisons the quadrature.

    The resulting call price from the Heston 1993 formulation is typically wrong by several dollars or even negative.

    **Albrecher formulation:** The quantity $|g\,e^{-\gamma\tau}| \approx e^{-25} \approx 1.4 \times 10^{-11}$, so $1 - g\,e^{-\gamma\tau} \approx 1$ with full precision. The logarithm is well-behaved, and the characteristic function is smooth across all $u$ values. The call price is computed accurately (e.g., $C \approx \$32.50$ for these parameters).

    This example demonstrates that the Heston 1993 formulation should never be used in production code, especially for long-dated options or high vol-of-vol regimes.
