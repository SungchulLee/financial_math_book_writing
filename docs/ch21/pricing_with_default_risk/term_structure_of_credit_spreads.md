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

---

**Exercise 2.** Explain why the Merton model produces near-zero credit spreads at short maturities for firms with $V_0 > D$. What mathematical property of continuous diffusion processes is responsible? How does the Black-Cox (first-passage) model resolve this issue?

---

**Exercise 3.** Using a CIR intensity model with $\lambda_0 = 3\%$, $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, and $R = 40\%$, determine qualitatively whether the resulting spread curve is upward-sloping, downward-sloping, or humped. Justify your answer by comparing $\lambda_0$ with $\theta$ and explaining the role of mean reversion.

---

**Exercise 4.** The credit spread puzzle states that observed spreads for investment-grade bonds far exceed model-predicted expected losses. Using the Huang-Huang data in the text, compute the fraction of the BBB spread explained by default risk. List three non-default factors that account for the remaining spread.

---

**Exercise 5.** Define the instantaneous forward credit spread $s_f(t,T) = (1-R)\lambda_f(t,T)$ and show that the spot credit spread is the average of forward spreads:

$$
s(t,T) = \frac{1}{T-t}\int_t^T s_f(t,u)\,du
$$

If forward spreads are rising, what does this imply about the market's expectation of future credit conditions?

---

**Exercise 6.** A speculative-grade issuer (B-rated) has observed credit spreads of 500 bp at 2Y, 450 bp at 5Y, and 380 bp at 10Y. Describe the shape of this spread curve and provide an economic explanation. What does the inverted shape imply about the market's conditional view of the firm's survival?

---

**Exercise 7.** Compare the calibration of structural models and intensity models to an observed credit spread curve. Which model class achieves a better fit at (a) short maturities, (b) medium maturities, and (c) long maturities? Explain why intensity models are preferred by trading desks for mark-to-market purposes.
