# Term Structure of Credit Spreads

The **term structure of credit spreads** describes how credit spreads vary across maturities for a given issuer or rating category. Understanding its shape, dynamics, and model-implied properties is fundamental to credit risk pricing, relative value analysis, and risk management. Different credit models produce characteristically different spread curves, and comparing their predictions with empirical data reveals both the strengths and limitations of each framework.

---

## Credit Spread Definitions

### Yield Spread

The **credit spread** (or **yield spread**) is the excess yield on a defaultable bond over the comparable risk-free yield:

$$
s(t,T) = y^d(t,T) - y(t,T)
$$

where:

$$
y^d(t,T) = -\frac{1}{T-t}\ln\frac{P^d(t,T)}{F}, \quad y(t,T) = -\frac{1}{T-t}\ln P(t,T)
$$

### Zero-Coupon Spread (Z-Spread)

For a zero-coupon defaultable bond:

$$
s(t,T) = -\frac{1}{T-t}\ln\frac{P^d(t,T)}{F \cdot P(t,T)}
$$

This measures the parallel shift to the risk-free zero curve that equates the discounted face value to the defaultable bond price.

### CDS Spread

The **CDS spread** for maturity $T$ is the par coupon rate on a credit default swap:

$$
s_{\text{CDS}}(T) = \frac{(1-R)\int_0^T D(0,u) S(0,u) \lambda_u \, du}{\sum_{i=1}^n \Delta_i D(0,t_i) S(0,t_i)}
$$

Under the constant-intensity approximation: $s_{\text{CDS}} \approx (1-R)\lambda$.

### Relationship Between Spreads

In a frictionless market:

$$
s_{\text{bond}}(T) \approx s_{\text{CDS}}(T)
$$

Deviations (the CDS-bond basis) reflect funding costs, liquidity, and counterparty risk.

---

## Spread Curves Under Structural Models

### Merton Model

Under the Merton model with $V_T / D$ log-normally distributed:

$$
s_{\text{Merton}}(T) = -\frac{1}{T}\ln\left[N(d_2) + \frac{1}{L}N(-d_1)\right]
$$

where $L = De^{-rT}/V_0$ is the present-value leverage ratio.

**Short-maturity behavior ($T \to 0$, $V_0 > D$):**

$$
s_{\text{Merton}}(T) \to 0
$$

The spread vanishes because the probability that a continuous diffusion drops below $D$ at a fixed time $T$ decays as $\exp(-c/T)$ for $V_0 > D$.

**Long-maturity behavior ($T \to \infty$):**

$$
s_{\text{Merton}}(T) \to (1-R)\lambda_\infty
$$

where $\lambda_\infty$ depends on the drift and volatility parameters.

**Curve shapes:** The Merton model produces only **upward-sloping** spread curves for firms with $V_0 > D$ (investment-grade), which is a significant empirical limitation.

### Black-Cox (First-Passage) Model

With a default barrier $B < V_0$, the first-passage model generates:

$$
s_{\text{BC}}(T) = -\frac{1}{T}\ln\left[\frac{P^d(0,T)}{D \cdot P(0,T)}\right]
$$

**Short-maturity behavior ($T \to 0$, $V_0 > B$):**

$$
s_{\text{BC}}(T) \to s_0 > 0
$$

The spread remains positive because the barrier can be crossed at any time, giving nonzero instantaneous default risk.

**Curve shapes:** The Black-Cox model can produce:

- **Upward sloping:** Low leverage, barrier far from current value
- **Humped:** Moderate leverage, peak at intermediate maturity
- **Downward sloping:** High leverage, near the barrier

This richer variety is a major improvement over Merton.

### Comparison of Structural Models

| Maturity | Merton | Black-Cox | Empirical |
|----------|--------|-----------|-----------|
| Very short ($< 1$Y) | Near zero | Positive | Positive, often substantial |
| Short (1--3Y) | Low, increasing | Moderate | Moderate |
| Medium (3--7Y) | Increasing | Peak or increasing | Varies by credit quality |
| Long (7--30Y) | Increasing | May decrease | Often flattening or decreasing |

---

## Spread Curves Under Intensity Models

### Deterministic Intensity

With constant risk-free rate $r$ and deterministic intensity $\lambda(t)$:

$$
s(t,T) = \frac{1}{T-t}\int_t^T (1-R)\lambda(s) \, ds
$$

under the RMV recovery convention. The spread is a weighted average of the loss-adjusted intensity over the horizon.

**Constant intensity:** $s(T) = (1-R)\lambda$ for all $T$ (flat spread curve).

**Increasing intensity:** Upward-sloping spread curve.

**Decreasing intensity:** Downward-sloping spread curve.

### Stochastic Intensity (CIR)

With CIR intensity $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma\sqrt{\lambda_t}dW_t$:

$$
s(t,T) = \frac{\alpha(T-t) + \beta(T-t)\lambda_t}{T-t}
$$

where $\alpha$ and $\beta$ are the Riccati solutions.

**Short-maturity limit:**

$$
\lim_{T \to t} s(t,T) = (1-R)\lambda_t
$$

The short-end spread equals the current loss-adjusted intensity.

**Long-maturity limit:**

$$
\lim_{T \to \infty} s(t,T) = (1-R)\theta_\infty
$$

where $\theta_\infty$ depends on the long-run mean and volatility parameters.

**Curve dynamics:**

- If $\lambda_t > \theta$ (high current intensity): **Downward-sloping** (mean reversion pulls intensity down)
- If $\lambda_t < \theta$ (low current intensity): **Upward-sloping** (mean reversion pulls intensity up)
- If $\lambda_t \approx \theta$: Nearly **flat**

---

## Forward Credit Spreads

### Definition

The **instantaneous forward credit spread** at time $t$ for maturity $T$ is:

$$
s_f(t,T) = -\frac{\partial}{\partial T}\ln\frac{P^d(t,T)}{P(t,T)} = (1-R)\lambda_f(t,T)
$$

where $\lambda_f(t,T)$ is the forward hazard rate.

### Relationship to Spot Spread

The spot spread is the average of forward spreads:

$$
s(t,T) = \frac{1}{T-t}\int_t^T s_f(t,u) \, du
$$

### Forward Spread Curve

The forward spread curve reveals the market's expectation of future credit conditions:

- **Rising forward spreads:** Market expects credit deterioration
- **Falling forward spreads:** Market expects credit improvement
- **Humped forward spreads:** Market expects temporary stress

---

## The Credit Spread Puzzle

### Observed vs Model-Implied Spreads

A major empirical finding is that structural models (particularly Merton) significantly **underpredict** observed credit spreads, especially for:

- Investment-grade bonds (BBB and above)
- Short maturities (1--3 years)

This discrepancy is known as the **credit spread puzzle**.

### Quantitative Evidence

Huang and Huang (2012) decomposed observed spreads for various rating categories:

| Rating | Observed Spread (bp) | Default-Explained (bp) | Fraction |
|--------|---------------------|----------------------|----------|
| AAA | 63 | 1 | 2% |
| AA | 91 | 2 | 2% |
| A | 123 | 8 | 7% |
| BBB | 194 | 38 | 20% |
| BB | 320 | 120 | 38% |
| B | 470 | 280 | 60% |

For investment-grade debt, credit risk (expected loss) explains only a small fraction of spreads.

### Explanations for the Puzzle

The residual spread beyond expected default loss reflects:

1. **Systematic risk premium:** Default risk is correlated with the market, requiring compensation beyond expected loss
2. **Liquidity premium:** Corporate bonds are less liquid than Treasuries
3. **Tax effects:** Differential tax treatment of corporate vs government bonds
4. **Jump risk:** Sudden default (not captured by pure diffusion) commands a premium
5. **Recovery uncertainty:** Stochastic recovery rates increase effective loss
6. **Model misspecification:** The Merton/Black-Cox framework may be too simple

---

## Empirical Patterns

### By Credit Quality

Observed spread curve shapes vary systematically with credit quality:

**Investment grade (AAA--BBB):**

- Typically **upward sloping**
- Short-term spreads are small but nonzero
- Spreads increase approximately linearly with maturity

**Speculative grade (BB--B):**

- Often **humped** or **inverted**
- Higher short-term spreads reflecting immediate distress
- Peak at 2--5 year maturity
- May decrease for long maturities (if the firm survives, it recovers)

**Deeply distressed (CCC and below):**

- **Steeply inverted**
- Very high short-term spreads
- Dramatic decline with maturity

### Spread Volatility

The volatility of credit spreads exhibits term structure patterns:

- Short-maturity spread changes are more volatile (in bp terms)
- Long-maturity spreads change more slowly
- Spread volatility is higher for lower-rated issuers
- Spread changes are negatively correlated with equity returns

### Regime Dependence

Spread curves shift dramatically across economic regimes:

- **Expansion:** Low, upward-sloping curves for most issuers
- **Recession:** Higher levels, flatter curves, increased dispersion
- **Crisis (2008):** Extremely elevated, inverted for many issuers

---

## Spread Dynamics and Mean Reversion

### Empirical Spread Dynamics

Credit spreads exhibit strong **mean reversion**:

$$
ds_t \approx \kappa_s(\bar{s} - s_t) \, dt + \sigma_s \, dZ_t
$$

where $\bar{s}$ is the long-run mean spread and $\kappa_s$ is the mean-reversion speed.

Estimated parameters from empirical studies:

- $\kappa_s \approx 0.3$--$0.8$ (half-life of 1--2 years)
- Spread volatility scales with spread level (roughly proportional)
- Mean level varies by rating: $\bar{s}_{\text{BBB}} \approx 150$--200 bp, $\bar{s}_{\text{BB}} \approx 300$--400 bp

### Spread Correlation with Macro Variables

Credit spreads are correlated with:

- **Equity market returns:** Negative correlation ($\rho \approx -0.4$ to $-0.7$)
- **VIX (equity volatility):** Positive correlation ($\rho \approx 0.5$ to $0.8$)
- **GDP growth:** Negative correlation
- **Treasury rates:** Negative correlation (flight to quality)
- **Slope of yield curve:** Negative correlation for IG, weaker for HY

---

## Model Calibration to Spread Curves

### Structural Models

Calibrating structural models to observed spread curves:

1. Given equity price $E_0$ and equity volatility $\sigma_E$, infer $(V_0, \sigma_V)$
2. Compute model-implied spread curve $s^{\text{model}}(T)$
3. Compare with observed curve $s^{\text{obs}}(T)$

Typical findings:

- Good fit at medium maturities (3--7Y) with appropriate barrier
- Poor fit at short maturities (model underpredicts)
- Reasonable fit at long maturities

### Intensity Models

Calibrating intensity models to CDS spread curves:

1. Bootstrap piecewise-constant hazard rates from CDS quotes
2. Fit parametric model (CIR, two-factor) to hazard rates
3. Use calibrated model for off-market pricing and risk

Intensity models achieve exact calibration to the observed curve (piecewise-constant) or excellent fit (parametric), making them preferred for trading desks.

---

## Numerical Example

**Setup:** Compare Merton and CIR intensity model spread curves.

**Common parameters:** $r = 4\%$, $R = 40\%$, $V_0 = 100$, $D = 70$, $\sigma_V = 25\%$

**Merton model spreads:**

At $T = 1$: $d_2 = \frac{\ln(100/70) + (0.04 - 0.03125)}{0.25} = \frac{0.3567 + 0.00875}{0.25} = 1.462$

$$
s(1) = -\ln[N(1.462) + (100/70 e^{-0.04})N(-1.712)] \approx 8 \text{ bp}
$$

At $T = 5$: $d_2 = \frac{0.3567 + 0.04375}{0.559} = 0.716$

$$
s(5) \approx 65 \text{ bp}
$$

At $T = 10$: $d_2 = \frac{0.3567 + 0.0875}{0.791} = 0.562$

$$
s(10) \approx 95 \text{ bp}
$$

**CIR intensity model** with $\lambda_0 = 1.5\%$, $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$:

At $T = 1$: $s(1) \approx (1-R)\lambda_0 = 0.6 \times 1.5\% = 90$ bp

At $T = 5$: $s(5) \approx (1-R)\bar{\lambda}_5 \approx 0.6 \times 1.8\% = 108$ bp

At $T = 10$: $s(10) \approx (1-R)\bar{\lambda}_{10} \approx 0.6 \times 1.95\% = 117$ bp

The CIR model produces a gently upward-sloping curve from 90 bp to 117 bp, while the Merton model produces a steeply rising curve from 8 bp to 95 bp. The CIR curve better matches typical investment-grade patterns, especially at short maturities.

---

## Key Takeaways

- The term structure of credit spreads describes how spreads vary with maturity
- Merton model: spreads vanish at short maturities, always upward-sloping
- Black-Cox model: positive short-term spreads, upward, humped, or inverted curves
- Intensity models: short-end spread equals $(1-R)\lambda_t$; shape driven by mean reversion
- The credit spread puzzle: observed spreads exceed model-predicted expected losses, especially for investment-grade bonds
- Empirical curves are upward-sloping for IG, humped for HY, inverted for distressed
- Spread dynamics exhibit mean reversion and negative correlation with equity markets
- Intensity models calibrate more accurately to observed curves than structural models

---

## Further Reading

- Huang, J.-Z., & Huang, M. (2012). How much of the corporate-treasury yield spread is due to credit risk? *Review of Asset Pricing Studies*, 2(2), 153--202.
- Helwege, J., & Turner, C. M. (1999). The slope of the credit yield curve for speculative-grade issuers. *Journal of Finance*, 54(5), 1869--1884.
- Duffie, D., & Singleton, K. J. (2003). *Credit Risk: Pricing, Measurement, and Management*. Princeton University Press, Chapter 6.
- Lando, D. (2004). *Credit Risk Modeling: Theory and Applications*. Princeton University Press.

---

## Exercises

**Exercise 1.** Under the Merton model with $V_0 = 100$, $D = 70$, $r = 4\%$, $\sigma_V = 25\%$, and $R = 40\%$, compute the credit spread at maturities $T = 1, 5, 10$ years. Verify that the spread at $T = 1$ is very small and describe the shape of the resulting spread curve.

??? success "Solution to Exercise 1"

    **Given:** Merton model with $V_0 = 100$, $D = 70$, $r = 4\% = 0.04$, $\sigma_V = 25\% = 0.25$, $R = 40\% = 0.40$.

    In the Merton model, the defaultable bond price for a zero-coupon bond with face value $D$ and maturity $T$ is:

    $$
    P^d(0,T) = D \cdot e^{-rT}\left[N(d_2) + \frac{V_0}{D \cdot e^{-rT}} N(-d_1)\right] \cdot (1-R) + R \cdot D \cdot e^{-rT}
    $$

    More precisely, the credit spread is:

    $$
    s(T) = -\frac{1}{T}\ln\!\left[N(d_2) + \frac{1}{L}N(-d_1)\right]
    $$

    where $L = D e^{-rT}/V_0$ is the present-value leverage ratio, and:

    $$
    d_1 = \frac{\ln(V_0/D) + (r + \sigma_V^2/2)T}{\sigma_V\sqrt{T}}, \quad d_2 = d_1 - \sigma_V\sqrt{T}
    $$

    **At $T = 1$:**

    $$
    d_1 = \frac{\ln(100/70) + (0.04 + 0.03125) \times 1}{0.25 \times 1} = \frac{0.35667 + 0.07125}{0.25} = \frac{0.42792}{0.25} = 1.7117
    $$

    $$
    d_2 = 1.7117 - 0.25 = 1.4617
    $$

    $$
    L = \frac{70 \cdot e^{-0.04}}{100} = \frac{70 \times 0.96079}{100} = 0.67256
    $$

    $$
    N(d_2) = N(1.4617) = 0.9281, \quad N(-d_1) = N(-1.7117) = 0.0435
    $$

    $$
    s(1) = -\ln\!\left[0.9281 + \frac{0.0435}{0.67256}\right] = -\ln\!\left[0.9281 + 0.0647\right] = -\ln(0.9928) = 0.0072
    $$

    So $s(1) \approx 0.72\% \approx 7$ bp. The spread at $T = 1$ is very small.

    **At $T = 5$:**

    $$
    d_1 = \frac{0.35667 + (0.07125) \times 5}{0.25\sqrt{5}} = \frac{0.35667 + 0.35625}{0.55902} = \frac{0.71292}{0.55902} = 1.2753
    $$

    $$
    d_2 = 1.2753 - 0.55902 = 0.7163
    $$

    $$
    L = \frac{70 \cdot e^{-0.20}}{100} = \frac{70 \times 0.81873}{100} = 0.57311
    $$

    $$
    N(d_2) = N(0.7163) = 0.7631, \quad N(-d_1) = N(-1.2753) = 0.1011
    $$

    $$
    s(5) = -\frac{1}{5}\ln\!\left[0.7631 + \frac{0.1011}{0.57311}\right] = -\frac{1}{5}\ln\!\left[0.7631 + 0.1764\right] = -\frac{1}{5}\ln(0.9395)
    $$

    $$
    s(5) = -\frac{1}{5} \times (-0.0624) = 0.01248 \approx 125 \text{ bp}
    $$

    **At $T = 10$:**

    $$
    d_1 = \frac{0.35667 + 0.07125 \times 10}{0.25\sqrt{10}} = \frac{0.35667 + 0.7125}{0.79057} = \frac{1.06917}{0.79057} = 1.3525
    $$

    $$
    d_2 = 1.3525 - 0.79057 = 0.5619
    $$

    $$
    L = \frac{70 \cdot e^{-0.40}}{100} = \frac{70 \times 0.67032}{100} = 0.46922
    $$

    $$
    N(d_2) = N(0.5619) = 0.7129, \quad N(-d_1) = N(-1.3525) = 0.0881
    $$

    $$
    s(10) = -\frac{1}{10}\ln\!\left[0.7129 + \frac{0.0881}{0.46922}\right] = -\frac{1}{10}\ln\!\left[0.7129 + 0.1878\right] = -\frac{1}{10}\ln(0.9007)
    $$

    $$
    s(10) = -\frac{1}{10} \times (-0.1046) = 0.01046 \approx 105 \text{ bp}
    $$

    **Summary:**

    | Maturity $T$ | $d_2$ | Spread (bp) |
    |---|---|---|
    | 1 | 1.462 | 7 |
    | 5 | 0.716 | 125 |
    | 10 | 0.562 | 105 |

    The spread at $T = 1$ is very small (7 bp), confirming that the Merton model produces near-zero short-term spreads. The spread curve is **upward-sloping** from 1 to 5 years and then slightly decreasing from 5 to 10 years, producing a **humped** shape with a peak around 5 years. For investment-grade firms (where $V_0$ is well above $D$), the curve is predominantly upward-sloping with very low short-end spreads, which is a well-known empirical shortcoming of the Merton model.

---

**Exercise 2.** Explain why the Merton model produces near-zero credit spreads at short maturities for firms with $V_0 > D$. What mathematical property of continuous diffusion processes is responsible? How does the Black-Cox (first-passage) model resolve this issue?

??? success "Solution to Exercise 2"

    **Why the Merton model produces near-zero short-term spreads:**

    In the Merton model, default can only occur at maturity $T$ when the firm value $V_T$ falls below the debt level $D$. The firm value follows a geometric Brownian motion:

    $$
    V_T = V_0 \exp\!\left[\left(r - \frac{\sigma_V^2}{2}\right)T + \sigma_V W_T\right]
    $$

    For $V_0 > D$, the probability of default at maturity $T$ is:

    $$
    \mathbb{Q}(\tau = T) = \mathbb{Q}(V_T < D) = N(-d_2)
    $$

    **The key mathematical property:** For a continuous diffusion process starting at $V_0 > D$, the probability that $V_T < D$ at a fixed time $T$ vanishes exponentially fast as $T \to 0$:

    $$
    N(-d_2) \sim \exp\!\left(-\frac{[\ln(V_0/D)]^2}{2\sigma_V^2 T}\right) \quad \text{as } T \to 0
    $$

    This is because a continuous path starting at $V_0 > D$ cannot jump below $D$ instantaneously. The Brownian motion must traverse the gap $\ln(V_0/D)$ continuously, which has vanishingly small probability over short time horizons. Consequently:

    $$
    s_{\text{Merton}}(T) \to 0 \quad \text{as } T \to 0
    $$

    **This contradicts empirical evidence:** Observed credit spreads for even highly-rated issuers are positive at short maturities (typically 10--50 bp for investment grade). This is the **short-spread puzzle** of the Merton model.

    **How the Black-Cox (first-passage) model resolves this:**

    The Black-Cox model introduces a **default barrier** $B$ (with $B \le V_0$) such that default occurs at the first time $V_t$ hits $B$:

    $$
    \tau = \inf\{t > 0 : V_t \le B\}
    $$

    The critical difference is that default can occur **at any time**, not just at maturity. Even over an infinitesimally short horizon, there is a positive probability that the continuous path touches the barrier, provided $V_0$ is close to $B$. More precisely, for the first-passage time of Brownian motion:

    $$
    \mathbb{Q}(\tau \le T) \sim 2N\!\left(\frac{-\ln(V_0/B)}{\sigma_V\sqrt{T}}\right) \quad \text{for small } T
    $$

    This probability is small but nonzero for any $T > 0$, yielding positive short-term spreads:

    $$
    s_{\text{BC}}(T) \to s_0 > 0 \quad \text{as } T \to 0 \text{ (for } V_0 \text{ near } B\text{)}
    $$

    The Black-Cox model also generates a richer variety of spread curve shapes (upward-sloping, humped, and downward-sloping) depending on the proximity of $V_0$ to $B$, compared to the Merton model which only produces upward-sloping curves for solvent firms.

---

**Exercise 3.** Using a CIR intensity model with $\lambda_0 = 3\%$, $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, and $R = 40\%$, determine qualitatively whether the resulting spread curve is upward-sloping, downward-sloping, or humped. Justify your answer by comparing $\lambda_0$ with $\theta$ and explaining the role of mean reversion.

??? success "Solution to Exercise 3"

    **Given:** CIR intensity with $\lambda_0 = 3\% = 0.03$, $\kappa = 0.5$, $\theta = 2\% = 0.02$, $\sigma = 8\%$, $R = 40\%$.

    **Key observation:** $\lambda_0 = 3\% > \theta = 2\%$. The current intensity exceeds its long-run mean.

    **Qualitative analysis of the spread curve:**

    Under the CIR intensity model, the short-maturity spread is:

    $$
    \lim_{T \to 0} s(0,T) = (1-R)\lambda_0 = 0.60 \times 0.03 = 0.018 = 180 \text{ bp}
    $$

    The long-maturity spread converges to:

    $$
    \lim_{T \to \infty} s(0,T) = (1-R)\theta_\infty
    $$

    where $\theta_\infty$ is related to the long-run mean of $\lambda$. Under the risk-neutral measure, since $\kappa > 0$ and the Feller condition $2\kappa\theta > \sigma^2$ should be checked ($2 \times 0.5 \times 0.02 = 0.02 > 0.0064$, satisfied), the intensity mean-reverts to $\theta = 2\%$. For large $T$, the average intensity $\bar{\lambda}_T = \frac{1}{T}\int_0^T \mathbb{E}[\lambda_s]\,ds$ converges to $\theta$.

    The expected intensity path is:

    $$
    \mathbb{E}[\lambda_t] = \theta + (\lambda_0 - \theta)e^{-\kappa t} = 0.02 + 0.01 \cdot e^{-0.5t}
    $$

    Since $\lambda_0 > \theta$, the expected intensity **decreases** over time from 3% toward 2%. Therefore, the average intensity over $[0,T]$ also decreases as $T$ increases, and the spread curve is **downward-sloping**:

    - Short-end: $s \approx 180$ bp (reflecting the high current intensity)
    - Long-end: $s \to (1-R)\theta = 0.60 \times 0.02 = 120$ bp (reflecting the long-run mean)

    The spread curve slopes downward from 180 bp toward 120 bp because the market "expects" the credit quality to improve as the intensity mean-reverts from its currently elevated level. This pattern is consistent with a speculative-grade issuer currently under stress but expected to recover.

    The role of mean reversion ($\kappa = 0.5$, half-life $= \ln 2/0.5 \approx 1.4$ years) is to determine how quickly the spread curve transitions from the short-end to the long-end level. A higher $\kappa$ would produce a steeper initial decline.

---

**Exercise 4.** The credit spread puzzle states that observed spreads for investment-grade bonds far exceed model-predicted expected losses. Using the Huang-Huang data in the text, compute the fraction of the BBB spread explained by default risk. List three non-default factors that account for the remaining spread.

??? success "Solution to Exercise 4"

    **From the Huang-Huang data:**

    For BBB-rated bonds:

    - Observed spread: 194 bp
    - Default-explained spread: 38 bp
    - Fraction explained by default risk: $38/194 = 19.6\% \approx 20\%$

    Therefore, **only about 20% of the BBB credit spread is explained by expected default losses**. The remaining 80% (approximately 156 bp) is attributable to non-default factors.

    **Three non-default factors accounting for the remaining spread:**

    1. **Systematic risk premium (credit risk premium):** Default events are correlated with the business cycle and market downturns. Investors demand compensation not just for expected losses, but for the fact that defaults tend to cluster during recessions when marginal utility is high. This systematic credit risk premium can be substantial. Under the physical measure, expected losses are even lower than the risk-neutral values, confirming that a large portion of the risk-neutral default intensity reflects a risk premium rather than actual default probability.

    2. **Liquidity premium:** Corporate bonds are significantly less liquid than Treasury bonds. Bid-ask spreads are wider, trading volumes are lower, and large positions are difficult to unwind quickly. Investors require a liquidity premium to compensate for these frictions. Empirical studies estimate liquidity premia of 30--80 bp for investment-grade bonds, which alone could account for a substantial portion of the unexplained spread.

    3. **Tax effects:** Interest on Treasury bonds is exempt from state and local taxes in the US, while corporate bond interest is fully taxable. This differential tax treatment makes Treasuries more valuable on an after-tax basis, inflating the measured spread between corporate and Treasury yields. Studies estimate this tax wedge at 20--40 bp for typical investors.

    Together, these three factors plausibly account for the 156 bp gap between the observed BBB spread and the default-explained component.

---

**Exercise 5.** Define the instantaneous forward credit spread $s_f(t,T) = (1-R)\lambda_f(t,T)$ and show that the spot credit spread is the average of forward spreads:

$$
s(t,T) = \frac{1}{T-t}\int_t^T s_f(t,u)\,du
$$

If forward spreads are rising, what does this imply about the market's expectation of future credit conditions?

??? success "Solution to Exercise 5"

    **Goal:** Define the forward credit spread and show the averaging relationship.

    **Definition:** The instantaneous forward credit spread at time $t$ for maturity $T$ is:

    $$
    s_f(t,T) = (1-R)\lambda_f(t,T)
    $$

    where $\lambda_f(t,T)$ is the forward hazard rate, defined as:

    $$
    \lambda_f(t,T) = -\frac{\partial}{\partial T}\ln S(t,T)
    $$

    with $S(t,T) = \mathbb{Q}(\tau > T \mid \tau > t, \mathcal{F}_t)$ being the survival probability. The forward credit spread can also be written as:

    $$
    s_f(t,T) = -\frac{\partial}{\partial T}\ln\!\left(\frac{P^d(t,T)}{P(t,T)}\right)
    $$

    **Derivation of the averaging relationship:**

    Under the RMV convention with deterministic or independent rates and intensity:

    $$
    \frac{P^d(t,T)}{P(t,T)} = e^{-\int_t^T (1-R)\lambda(t,s)\,ds}
    $$

    Taking the logarithm:

    $$
    \ln\!\left(\frac{P^d(t,T)}{P(t,T)}\right) = -\int_t^T (1-R)\lambda_f(t,s)\,ds = -\int_t^T s_f(t,s)\,ds
    $$

    The spot credit spread (Z-spread) is:

    $$
    s(t,T) = -\frac{1}{T-t}\ln\!\left(\frac{P^d(t,T)}{F \cdot P(t,T)}\right) = \frac{1}{T-t}\int_t^T s_f(t,u)\,du
    $$

    (The $\ln F$ term vanishes when $F = 1$ or is absorbed into the yield definitions.) This confirms that **the spot credit spread is the arithmetic average of instantaneous forward credit spreads** over the interval $[t, T]$.

    **Interpretation of rising forward spreads:**

    If forward spreads $s_f(t,T)$ are increasing in $T$, this means:

    - The market prices in **higher credit losses** at longer horizons.
    - This implies the market expects **credit deterioration** over time -- the issuer's creditworthiness is expected to worsen.
    - The forward hazard rate $\lambda_f(t,T)$ is increasing, meaning the conditional probability of defaulting in the next instant, given survival to time $T$, increases with $T$.
    - Economically, this could reflect anticipated increases in leverage, declining profitability, or approaching debt maturities that increase refinancing risk.

    Note that rising forward spreads produce an **upward-sloping spot spread curve**, since the average of an increasing function exceeds its initial value but lies below its terminal value.

---

**Exercise 6.** A speculative-grade issuer (B-rated) has observed credit spreads of 500 bp at 2Y, 450 bp at 5Y, and 380 bp at 10Y. Describe the shape of this spread curve and provide an economic explanation. What does the inverted shape imply about the market's conditional view of the firm's survival?

??? success "Solution to Exercise 6"

    **Given:** B-rated issuer with observed spreads: 500 bp at 2Y, 450 bp at 5Y, 380 bp at 10Y.

    **Shape of the spread curve:**

    The spread curve is **inverted** (downward-sloping): spreads decrease monotonically from 500 bp at 2Y to 380 bp at 10Y. This is characteristic of speculative-grade or distressed issuers.

    **Economic explanation:**

    1. **Conditional survival effect:** The inverted spread curve reflects a **selection bias** in conditional expectations. At longer horizons, the bond only pays if the firm has survived. For a B-rated issuer with high near-term default risk, survival to year 10 is a much stronger positive signal about the firm's health than survival to year 2. If the firm survives the near-term stress period, it is likely to have improved its financial position, leading to lower conditional default intensity.

    2. **Mean reversion of credit quality:** In the intensity framework, an inverted spread curve arises when $\lambda_0 > \theta$ (current intensity exceeds the long-run mean). The CIR model predicts:

        $$
        s(T) \approx (1-R)\left[\theta + \frac{\lambda_0 - \theta}{T}\int_0^T e^{-\kappa u}\,du\right]
        $$

        Since $\lambda_0$ is high (reflecting B-rated stress), the short-end spread is elevated. As $T$ increases, the weight on $\lambda_0$ diminishes and the spread converges toward $(1-R)\theta$, producing the downward slope.

    3. **Near-term distress, long-term recovery:** The firm faces elevated default risk in the near term (reflected in the 500 bp 2Y spread). However, the market believes that if the firm survives the next few years, its credit profile will improve significantly. This could reflect:
        - Anticipated debt maturity and refinancing risk concentrated in 1--3 years
        - Expected resolution of litigation or regulatory issues
        - Cyclical recovery of the firm's industry

    **What the inverted shape implies about the market's conditional view:**

    The market views the firm as having a **bimodal outcome distribution**:

    - **High probability of near-term default** (justifying the 500 bp short-term spread)
    - **Significant credit improvement conditional on survival** (justifying the declining long-term spread)

    If the firm defaults, it likely happens within the first few years. If it does not default early, it emerges stronger, and the long-term credit outlook is substantially better than the current situation suggests. This is the classic "survive or die" profile of speculative-grade credit.

---

**Exercise 7.** Compare the calibration of structural models and intensity models to an observed credit spread curve. Which model class achieves a better fit at (a) short maturities, (b) medium maturities, and (c) long maturities? Explain why intensity models are preferred by trading desks for mark-to-market purposes.

??? success "Solution to Exercise 7"

    **Comparison of structural and intensity models for calibration to observed spread curves:**

    **(a) Short maturities (less than 1--2 years):**

    **Structural models (Merton/Black-Cox):** Poor fit. The Merton model produces near-zero short-term spreads because continuous diffusion paths require time to traverse the gap between $V_0$ and $D$. Even the Black-Cox model, while producing positive short-term spreads, often underpredicts observed values because the diffusion framework limits the instantaneous default probability.

    **Intensity models:** Excellent fit. The short-maturity spread under an intensity model converges to $(1-R)\lambda_t$, which can be calibrated to match any observed short-end spread by choosing $\lambda_0$ appropriately. This direct relationship between the current intensity and the short-end spread gives intensity models a decisive advantage at the short end.

    **Winner: Intensity models.**

    **(b) Medium maturities (3--7 years):**

    **Structural models:** Reasonable fit, especially Black-Cox with a well-chosen barrier. The 3--7 year range is where structural models perform best because diffusion probabilities are neither negligibly small (as at short horizons) nor dominated by drift (as at very long horizons). With appropriate calibration of $V_0$, $\sigma_V$, and the default barrier, structural models can match medium-term spreads reasonably well.

    **Intensity models:** Excellent fit. Parametric intensity models (CIR, two-factor) have enough flexibility to match medium-term spreads, and piecewise-constant hazard rate bootstrapping achieves exact calibration at CDS maturities (1Y, 3Y, 5Y, 7Y, 10Y).

    **Winner: Both perform adequately; intensity models are slightly better due to exact calibration capability.**

    **(c) Long maturities (7--30 years):**

    **Structural models:** Mixed results. The Merton model tends to overpredict long-term spreads for investment-grade firms (monotonically increasing curve), while empirical curves often flatten or decline at long maturities. Black-Cox can produce the correct flattening through barrier calibration.

    **Intensity models:** Good fit. Long-term spreads converge to $(1-R)\theta$ in CIR-type models, and the mean-reversion parameters can be calibrated to match observed long-end levels. Multi-factor intensity models provide additional flexibility.

    **Winner: Intensity models, with well-specified structural models as a close second.**

    **Why intensity models are preferred by trading desks:**

    1. **Exact calibration to market observables:** Piecewise-constant hazard rates can exactly match quoted CDS spreads at standard maturities. This is essential for mark-to-market: the model must reprice liquid instruments exactly to avoid arbitrage against the desk's own book.

    2. **Computational speed:** Intensity-based pricing involves one-dimensional integrals or closed-form expressions, compared to the iterative solution of the Merton equity-debt system. Speed is critical for real-time pricing and risk management of large portfolios.

    3. **Direct link to traded instruments:** CDS spreads directly imply hazard rates, creating a transparent mapping between market quotes and model parameters. Structural models require inferring firm value and volatility from equity prices, which introduces additional model risk.

    4. **Flexibility:** Intensity models accommodate arbitrary spread curve shapes (upward, flat, humped, inverted) through the choice of $\lambda(t)$ or the parameters of a stochastic intensity process. Structural models are more constrained in the curve shapes they can produce.

    5. **Consistency across products:** The same calibrated hazard rate curve prices bonds, CDS, credit-linked notes, and other credit derivatives consistently. This is essential for relative value trading and hedging across instruments.
