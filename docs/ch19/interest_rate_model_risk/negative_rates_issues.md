# Negative Rates Issues


The emergence of **negative interest rates** in several markets has highlighted
important limitations and modeling challenges in classical interest rate
frameworks. Negative rates do not represent a market anomaly; rather, they
expose implicit assumptions embedded in many standard models.

This section discusses why negative rates create difficulties for certain
models and how these issues are addressed in practice.

---

## Empirical Reality of Negative Rates


Negative nominal interest rates have been observed in multiple markets,
including:

- EUR, CHF, and JPY government bond yields,
- short-term money market rates,
- overnight indexed swap (OIS) curves.

Therefore, any realistic interest rate model must either:

- accommodate negative rates explicitly, or
- remain well-defined when rates approach or cross zero.

---

## Implicit Positivity Assumptions


Many classical interest rate and derivative pricing models rely on **implicit
positivity assumptions**, even when not stated explicitly.

Examples include:

- lognormal dynamics,
- pricing formulas derived under strictly positive rates,
- volatility specifications proportional to the level of the rate.

When rates become negative, these assumptions may fail, leading to conceptual
or numerical inconsistencies.

---

## Lognormal Models and Their Limitations


Recall (see [§ Shifted and Normal Models](shifted_and_normal_models.md)): lognormal dynamics (Black's formula, lognormal LMM) require strictly positive rates; under negative rates, $\ln(F)$ is undefined, volatility scaling proportional to $F$ breaks down, and calibration fails. This is **model misspecification**, not market failure.

---

## Numerical and Calibration Issues


Negative rates can introduce practical difficulties, including:

- instability in numerical schemes,
- poor calibration performance near zero,
- sensitivity to small shifts in rates.

These effects are particularly pronounced for:

- long-dated instruments,
- low-volatility environments,
- multi-curve frameworks.

---

## Common Modeling Responses


Market practice adopts:

- **Normal (Bachelier)** and **shifted lognormal** models — Recall (see [§ Shifted and Normal Models](shifted_and_normal_models.md)).
- **Gaussian short-rate models** (Vasicek, Hull–White), which naturally allow negative rates.

Each approach trades off realism, tractability, and market convention.

---

## Interpretation as Model Risk


Negative rates should be viewed as a **stress test for model assumptions**.

They reveal:

- hidden structural constraints,
- sensitivity to distributional choices,
- limitations of extrapolating models beyond their design domain.

From a model risk perspective, the key lesson is not to avoid negative rates,
but to **understand which assumptions fail when they occur**.

---

## Concluding Remarks


Negative interest rates do not invalidate financial theory. Instead, they
highlight the importance of:

- explicit modeling assumptions,
- robustness across regimes,
- flexibility in model selection.

In this sense, negative rates serve as a valuable reminder that **models are
approximations**, not laws of nature.

---

## Exercises

**Exercise 1.** Black's formula for a caplet uses the expression $\ln(L/K)$, where $L$ is the forward LIBOR rate and $K$ is the strike. Explain precisely why this formula breaks down when $L < 0$ or $K < 0$. What happens numerically if you attempt to compute $d_1$ and $d_2$ in this case?

??? success "Solution to Exercise 1"

    Black's formula for a caplet on LIBOR rate $L$ with strike $K$ uses the quantities

    $$
    d_1 = \frac{\ln(L/K) + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}
    $$

    **Case $L < 0$:** The logarithm $\ln(L/K)$ requires $L/K > 0$. If $L < 0$ and $K > 0$, then $L/K < 0$ and $\ln(L/K)$ is undefined in the real numbers. The formula cannot be evaluated at all. Numerically, most implementations will return `NaN` or raise a domain error.

    **Case $K < 0$:** Similarly, if $K < 0$ and $L > 0$, then $L/K < 0$ and $\ln(L/K)$ is again undefined. If both $L < 0$ and $K < 0$, then $L/K > 0$ and the logarithm is defined, but the formula is still invalid because Black's formula is derived under the assumption that $L$ follows a lognormal distribution (geometric Brownian motion), which is confined to strictly positive values. If $L$ can be negative, the underlying distributional assumption is violated.

    **Numerical attempt:** If one forces a computation with $L < 0$ and $K > 0$, the complex logarithm gives $\ln|L/K| + i\pi$, producing complex-valued $d_1$ and $d_2$. The cumulative normal function $N(\cdot)$ evaluated at complex arguments has no standard financial interpretation. Implementations typically produce `NaN`, raise exceptions, or (worse) return silently incorrect values.

    The root cause is not a numerical issue but a **model misspecification**: the lognormal SDE $dL = \sigma L\,dW$ has no solution starting from $L(0) < 0$, so the entire probabilistic framework underpinning Black's formula is inapplicable.

---

**Exercise 2.** A normal (Bachelier) caplet formula gives the price as

$$
\text{Caplet} = \delta\,P(0, T_{i+1})\left[(L - K)\,N(d) + \sigma_N\sqrt{T}\,n(d)\right], \qquad d = \frac{L - K}{\sigma_N\sqrt{T}}
$$

where $\sigma_N$ is the normal volatility. Verify that this formula is well-defined for $L < 0$ and $K < 0$. Compute the price for $L = -0.2\%$, $K = -0.1\%$, $\sigma_N = 0.50\%$, $T = 2$, $\delta = 0.5$, and $P(0, T_{i+1}) = 1.004$.

??? success "Solution to Exercise 2"

    The Bachelier caplet formula is

    $$
    \text{Caplet} = \delta\,P(0, T_{i+1})\left[(L - K)\,N(d) + \sigma_N\sqrt{T}\,n(d)\right], \qquad d = \frac{L - K}{\sigma_N\sqrt{T}}
    $$

    **Well-definedness for $L < 0$ and $K < 0$:** The formula involves only $L - K$ (a real number regardless of signs), $\sigma_N\sqrt{T}$ (always positive), $N(d)$ (the standard normal CDF, defined for all real $d$), and $n(d) = \phi(d) = \frac{1}{\sqrt{2\pi}}e^{-d^2/2}$ (the standard normal PDF, also defined for all real $d$). There are no logarithms or ratios requiring positivity. Therefore the formula is well-defined for any real values of $L$ and $K$.

    **Numerical computation with the given parameters:**

    - $L = -0.002$, $K = -0.001$, $\sigma_N = 0.005$, $T = 2$, $\delta = 0.5$, $P(0, T_{i+1}) = 1.004$.

    First compute $d$:

    $$
    d = \frac{L - K}{\sigma_N\sqrt{T}} = \frac{-0.002 - (-0.001)}{0.005\sqrt{2}} = \frac{-0.001}{0.005 \times 1.4142} = \frac{-0.001}{0.007071} = -0.14142
    $$

    Next, look up the normal CDF and PDF:

    $$
    N(-0.14142) \approx 0.4438, \qquad n(-0.14142) = \phi(-0.14142) = \frac{1}{\sqrt{2\pi}}e^{-0.01/2} \approx 0.3955
    $$

    Now compute the two terms inside the brackets:

    $$
    (L - K)\,N(d) = (-0.001)(0.4438) = -0.0004438
    $$

    $$
    \sigma_N\sqrt{T}\,n(d) = (0.007071)(0.3955) = 0.002797
    $$

    Summing:

    $$
    -0.0004438 + 0.002797 = 0.002353
    $$

    Finally:

    $$
    \text{Caplet} = 0.5 \times 1.004 \times 0.002353 = 0.001181
    $$

    The caplet price is approximately **0.1181%** of notional (or about 11.81 basis points times $\delta \cdot P$). The formula works correctly despite both $L$ and $K$ being negative, confirming the robustness of the Bachelier framework.

---

**Exercise 3.** A shifted lognormal model replaces $L$ with $L + s$ where $s > 0$ is the shift, ensuring positivity. If the market LIBOR rate is $L = -0.3\%$ and the shift is $s = 3\%$, compute the shifted forward rate and verify it is positive. Discuss how the choice of $s$ affects the implied volatility smile and why different shifts lead to different smile shapes.

??? success "Solution to Exercise 3"

    **Shifted forward rate:** With $L = -0.3\% = -0.003$ and $s = 3\% = 0.03$:

    $$
    L + s = -0.003 + 0.03 = 0.027 = 2.7\%
    $$

    This is strictly positive, so the shifted rate can be modeled lognormally.

    **Verification:** The shifted lognormal model requires $L + s > 0$. Since $0.027 > 0$, the condition is satisfied. The shifted rate can be used in Black's formula by replacing $L \to L + s$ and $K \to K + s$.

    **Effect of shift on the implied volatility smile:** The choice of $s$ determines the lower bound of the rate distribution ($L > -s$) and the shape of the implied volatility smile when viewed in standard (Black or normal) terms.

    - **Larger shift $s$:** The shifted lognormal distribution approaches a normal distribution (since $\sigma_{\text{SLN}} \cdot (L + s)$ becomes approximately constant across strikes when $s \gg |L|$). The implied Black volatility smile becomes flatter and more symmetric.

    - **Smaller shift $s$:** The model retains more lognormal character. The implied volatility smile shows more pronounced positive skew (in shifted lognormal terms), and the lower bound $-s$ is closer to current rates, creating asymmetry.

    - **Different shifts produce different smile shapes** because the mapping between the shifted lognormal distribution and the market-observed option prices changes. Two calibrations with different $s$ values will match ATM prices (by adjusting $\sigma_{\text{SLN}}$) but will generally disagree on OTM option prices. This disagreement is a manifestation of **model risk**: the shift is a free parameter that cannot be determined from ATM data alone, yet it materially affects the pricing of OTM options.

    In practice, the shift is chosen to ensure all market-observed rates satisfy $L + s > 0$, but beyond this minimum requirement, the choice is somewhat arbitrary and should be treated as part of the model uncertainty.

---

**Exercise 4.** In the CIR model, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$, the short rate is guaranteed non-negative under the Feller condition $2\kappa\theta \geq \sigma^2$. Explain why this model cannot accommodate negative rates. If rates are observed to be negative, what modifications to the CIR model are possible while preserving analytical tractability?

??? success "Solution to Exercise 4"

    **Why CIR cannot accommodate negative rates:**

    The CIR SDE is

    $$
    dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
    $$

    The diffusion coefficient $\sigma\sqrt{r_t}$ requires $r_t \geq 0$. When the Feller condition $2\kappa\theta \geq \sigma^2$ holds, the process is strictly positive ($r_t > 0$ for all $t > 0$ if $r_0 > 0$). Even when the Feller condition is violated, the process can reach zero but is immediately reflected, remaining non-negative. The square-root diffusion is undefined for $r_t < 0$ (it would require the square root of a negative number), so the model structurally excludes negative rates.

    **Modifications preserving analytical tractability:**

    1. **Shifted CIR model:** Define $r_t = x_t - s$ where $x_t$ follows a CIR process and $s > 0$ is a shift:

        $$
        dx_t = \kappa(\theta + s - x_t)\,dt + \sigma\sqrt{x_t}\,dW_t
        $$

        Then $r_t = x_t - s$ can take values in $(-s, \infty)$, accommodating negative rates down to $-s$. Bond prices remain available in closed form since $x_t$ is still a CIR process.

    2. **CIR with additive Gaussian component:** Define $r_t = x_t + y_t$ where $x_t$ follows CIR and $y_t$ follows an OU process:

        $$
        dy_t = -\kappa_y y_t\,dt + \sigma_y\,dW_t^y
        $$

        The Gaussian component allows $r_t$ to become negative. If $x_t$ and $y_t$ are independent, the model remains affine and bond prices have exponential-affine form.

    3. **Vasicek / Hull--White model:** Replace the CIR dynamics entirely with Gaussian dynamics:

        $$
        dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t
        $$

        This is the simplest modification: it preserves full analytical tractability (closed-form bond prices, bond options) while naturally allowing negative rates. The trade-off is losing the non-negativity property, but this is precisely what is needed when rates are observed to be negative.

---

**Exercise 5.** The Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ allows negative rates. Compute the probability that $r_T < 0$ for $r_0 = 1\%$, $\theta = 2\%$, $\kappa = 0.1$, $\sigma = 1.5\%$, and $T = 10$. Use the fact that $r_T$ is normally distributed with mean $\theta + (r_0 - \theta)e^{-\kappa T}$ and variance $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T})$.

??? success "Solution to Exercise 5"

    In the Vasicek model, $r_T$ is normally distributed:

    $$
    r_T \sim N(\mu_T, \, \sigma_T^2)
    $$

    where

    $$
    \mu_T = \theta + (r_0 - \theta)e^{-\kappa T}, \qquad \sigma_T^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T})
    $$

    **Computing $\mu_T$** with $r_0 = 0.01$, $\theta = 0.02$, $\kappa = 0.1$, $T = 10$:

    $$
    e^{-\kappa T} = e^{-0.1 \times 10} = e^{-1} \approx 0.36788
    $$

    $$
    \mu_T = 0.02 + (0.01 - 0.02) \times 0.36788 = 0.02 - 0.01 \times 0.36788 = 0.02 - 0.0036788 = 0.016321
    $$

    **Computing $\sigma_T^2$** with $\sigma = 0.015$:

    $$
    e^{-2\kappa T} = e^{-2} \approx 0.13534
    $$

    $$
    \sigma_T^2 = \frac{(0.015)^2}{2 \times 0.1}(1 - 0.13534) = \frac{0.000225}{0.2} \times 0.86466 = 0.001125 \times 0.86466 = 0.0009727
    $$

    $$
    \sigma_T = \sqrt{0.0009727} \approx 0.03119 = 3.119\%
    $$

    **Probability that $r_T < 0$:**

    $$
    P(r_T < 0) = N\!\left(\frac{0 - \mu_T}{\sigma_T}\right) = N\!\left(\frac{-0.016321}{0.03119}\right) = N(-0.5233)
    $$

    Looking up the standard normal CDF:

    $$
    N(-0.5233) \approx 0.3004
    $$

    Therefore, there is approximately a **30.0%** probability that the short rate is negative at $T = 10$ years. This is a substantial probability, illustrating that the Vasicek model readily produces negative rates when the mean reversion speed is slow ($\kappa = 0.1$) and the volatility ($\sigma = 1.5\%$) is not negligible relative to the mean level ($\theta = 2\%$).

---

**Exercise 6.** A trader currently uses the lognormal Black model for swaption pricing and needs to switch to a framework that handles negative rates. Compare three alternatives --- Bachelier (normal), shifted Black, and SABR with shift --- along the dimensions of (a) simplicity, (b) smile fit quality, (c) hedge ratio stability, and (d) consistency with existing market conventions. Which would you recommend and why?

??? success "Solution to Exercise 6"

    We compare three alternatives along four dimensions:

    **(a) Simplicity:**

    - **Bachelier (normal):** Very simple. Replace $\ln(L/K)$ with $(L-K)$ in the pricing formula. Single parameter $\sigma_N$. No positivity constraint.
    - **Shifted Black:** Moderate complexity. Same formula as Black but with $L + s$ and $K + s$ replacing $L$ and $K$. Requires choosing the shift $s$.
    - **SABR with shift:** Most complex. Four parameters ($\alpha$, $\beta$, $\rho$, $\nu$) plus the shift $s$. Requires Hagan's approximation formula or numerical methods.

    **(b) Smile fit quality:**

    - **Bachelier:** Produces a flat smile in normal vol terms. Cannot capture skew or curvature. Poor for fitting the observed smile across strikes.
    - **Shifted Black:** Also produces a flat smile in shifted Black vol. No better than Bachelier for smile fitting. Only captures the ATM level.
    - **SABR with shift:** Excellent smile fit. The parameters $\rho$ (skew) and $\nu$ (curvature/vol-of-vol) allow flexible fitting of the observed smile across strikes. This is the standard for smile modeling.

    **(c) Hedge ratio stability:**

    - **Bachelier:** Delta is stable across rate levels since the model is linear in rates. However, it may misprice tail risks.
    - **Shifted Black:** Delta depends on the shift $s$, which is exogenous. Different shifts produce different deltas, introducing hedge ratio uncertainty.
    - **SABR with shift:** Delta depends on multiple parameters ($\alpha$, $\beta$, $\rho$, $\nu$, $s$), all of which may change upon recalibration. Hedge ratios can be unstable if parameters are not well-identified.

    **(d) Consistency with existing market conventions:**

    - **Bachelier:** Increasingly adopted (EUR, JPY markets quote normal vols). Clean but may require infrastructure changes for desks built around Black's formula.
    - **Shifted Black:** Very consistent with existing Black vol infrastructure. Minimal code changes (add shift to rate inputs). Widely adopted in EUR swaptions.
    - **SABR with shift:** Consistent with pre-existing SABR infrastructure. Market standard for smile-sensitive products (e.g., CMS, exotics).

    **Recommendation:** For a desk that needs to handle negative rates while maintaining smile fitting capability, **SABR with shift** is the best choice despite its complexity, because it is the only model among the three that can fit the volatility smile across strikes. For vanilla products where smile fitting is not critical, **shifted Black** offers the best trade-off between simplicity and compatibility with existing systems. The Bachelier model is appropriate when maximum simplicity and robustness are prioritized, and no smile modeling is needed.
