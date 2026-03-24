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


Lognormal models, such as:
- Black’s formula,
- lognormal LIBOR Market Models (LMM),

assume that rates or forward rates remain strictly positive.

Under negative rates:
- logarithms become undefined,
- volatility scaling becomes meaningless,
- calibration may fail or become unstable.

This does not indicate market failure, but rather **model misspecification**.

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


Market practice has adopted several approaches to handle negative rates:

- **Normal (Bachelier) models**  
  Allow rates to take any real value and behave well near zero.

- **Shifted lognormal models**  
  Apply a positive shift to rates before modeling them lognormally.

- **Gaussian short-rate models**  
  Such as Vasicek or Hull–White, which naturally allow negative rates.

Each approach involves trade-offs between realism, tractability, and
consistency with market conventions.

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

---

**Exercise 2.** A normal (Bachelier) caplet formula gives the price as

$$
\text{Caplet} = \delta\,P(0, T_{i+1})\left[(L - K)\,N(d) + \sigma_N\sqrt{T}\,n(d)\right], \qquad d = \frac{L - K}{\sigma_N\sqrt{T}}
$$

where $\sigma_N$ is the normal volatility. Verify that this formula is well-defined for $L < 0$ and $K < 0$. Compute the price for $L = -0.2\%$, $K = -0.1\%$, $\sigma_N = 0.50\%$, $T = 2$, $\delta = 0.5$, and $P(0, T_{i+1}) = 1.004$.

---

**Exercise 3.** A shifted lognormal model replaces $L$ with $L + s$ where $s > 0$ is the shift, ensuring positivity. If the market LIBOR rate is $L = -0.3\%$ and the shift is $s = 3\%$, compute the shifted forward rate and verify it is positive. Discuss how the choice of $s$ affects the implied volatility smile and why different shifts lead to different smile shapes.

---

**Exercise 4.** In the CIR model, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$, the short rate is guaranteed non-negative under the Feller condition $2\kappa\theta \geq \sigma^2$. Explain why this model cannot accommodate negative rates. If rates are observed to be negative, what modifications to the CIR model are possible while preserving analytical tractability?

---

**Exercise 5.** The Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ allows negative rates. Compute the probability that $r_T < 0$ for $r_0 = 1\%$, $\theta = 2\%$, $\kappa = 0.1$, $\sigma = 1.5\%$, and $T = 10$. Use the fact that $r_T$ is normally distributed with mean $\theta + (r_0 - \theta)e^{-\kappa T}$ and variance $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T})$.

---

**Exercise 6.** A trader currently uses the lognormal Black model for swaption pricing and needs to switch to a framework that handles negative rates. Compare three alternatives --- Bachelier (normal), shifted Black, and SABR with shift --- along the dimensions of (a) simplicity, (b) smile fit quality, (c) hedge ratio stability, and (d) consistency with existing market conventions. Which would you recommend and why?
