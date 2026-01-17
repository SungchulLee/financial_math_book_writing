# First-Passage Models

First-passage models extend the Merton framework by allowing default to occur **at any time** before maturity, when the firm's asset value first crosses a default barrier. This addresses a key limitation of the Merton model—that default can only occur at debt maturity—and produces richer credit spread term structures.

---

## Default as Barrier Crossing

### Definition of Default Time

In first-passage models, the default time is defined as the **first hitting time** of a barrier:

$$
\tau = \inf\{t \ge 0 : V_t \le B_t\},
$$

where:
- $V_t$ is the firm's asset value process
- $B_t$ is the default barrier (possibly time-varying)
- Convention: $\inf \emptyset = \infty$ (no default if barrier is never reached)

### Economic Interpretation

Default occurs when:
- Firm value falls to a critical level
- Covenant violations are triggered
- The firm becomes insolvent
- Creditors force liquidation

Unlike Merton's maturity-only default, first-passage models capture **early default** due to financial distress at any point.

---

## Asset Dynamics and Barrier Specifications

### Asset Value Process

Under the risk-neutral measure $\mathbb{Q}$:

$$
dV_t = (r - q)V_t \, dt + \sigma V_t \, dW_t^{\mathbb{Q}},
$$

with solution:

$$
V_t = V_0 \exp\left[\left(r - q - \frac{\sigma^2}{2}\right)t + \sigma W_t^{\mathbb{Q}}\right].
$$

### Common Barrier Specifications

**1. Constant Barrier (Black-Cox)**

$$
B_t = B \quad \text{(constant)}.
$$

Simplest case with analytical tractability.

**2. Exponentially Decaying Barrier**

$$
B_t = B_0 e^{-\gamma t}
$$

Models amortizing debt or improving credit over time.

**3. Exponentially Growing Barrier**

$$
B_t = B_0 e^{\gamma t}
$$

Models accumulating liabilities or covenant tightening.

**4. Coupon-Linked Barrier (Leland)**

$$
B_t = C/r
$$

where $C$ is the coupon rate, representing the capitalized value of perpetual debt service.

**5. Endogenous Barrier**

The barrier is determined optimally by equity holders' decision to default, typically when equity value hits zero.

---

## The Black-Cox Model

### Setup

Black and Cox (1976) extended Merton by introducing a **safety covenant**: default occurs at the first time asset value falls to a constant barrier $B < V_0$.

The default time is:

$$
\tau = \inf\{t \ge 0 : V_t \le B\}.
$$

### Transformation to Standard Form

Define the log-asset process:

$$
X_t = \ln V_t = \ln V_0 + \mu t + \sigma W_t,
$$

where $\mu = r - q - \sigma^2/2$.

Default occurs when $X_t$ first hits $\ln B$. Define $a = \ln(V_0/B) > 0$. Then:

$$
\tau = \inf\{t : X_t - \ln V_0 \le -a\} = \inf\{t : \mu t + \sigma W_t \le -a\}.
$$

This is a **first-passage time** for Brownian motion with drift.

---

## First-Passage Time Distributions

### Survival Probability

The probability that default has not occurred by time $T$ is:

$$
S(0,T) = \mathbb{Q}(\tau > T) = \mathbb{Q}\left(\min_{0 \le t \le T} V_t > B\right).
$$

For GBM with constant barrier, this has a closed-form solution.

### Closed-Form Formula

Let $a = \ln(V_0/B)$ and define:

$$
\nu = \frac{\mu}{\sigma} = \frac{r - q - \sigma^2/2}{\sigma}.
$$

The survival probability is:

$$
S(0,T) = N\left(\frac{a + \nu \sigma T}{\sigma\sqrt{T}}\right) - e^{2\nu a} N\left(\frac{-a + \nu \sigma T}{\sigma\sqrt{T}}\right),
$$

or equivalently:

$$
S(0,T) = N(d_+) - \left(\frac{B}{V_0}\right)^{2\mu/\sigma^2} N(d_-),
$$

where:

$$
d_+ = \frac{\ln(V_0/B) + \mu T}{\sigma\sqrt{T}}, \quad d_- = \frac{\ln(B/V_0) + \mu T}{\sigma\sqrt{T}}.
$$

### Default Probability

The cumulative default probability is:

$$
F(T) = \mathbb{Q}(\tau \le T) = 1 - S(0,T).
$$

### Density of Default Time

The density of the first-passage time is:

$$
f(t) = \frac{a}{\sigma\sqrt{2\pi t^3}} \exp\left(-\frac{(a + \mu t)^2}{2\sigma^2 t}\right), \quad t > 0.
$$

This is the **inverse Gaussian density** (shifted).

---

## Pricing Defaultable Bonds

### Zero-Coupon Bond with Recovery

Consider a defaultable zero-coupon bond paying:
- Face value $D$ at maturity $T$ if no default
- Recovery $R \cdot B$ at default time $\tau$ if default occurs before $T$

The price is:

$$
P^d(0,T) = D \cdot e^{-rT} \cdot S(0,T) + R \cdot B \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-r\tau} \mathbf{1}_{\{\tau \le T\}}\right].
$$

### Expected Discounted Default Payment

The second term involves:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-r\tau} \mathbf{1}_{\{\tau \le T\}}\right] = \int_0^T e^{-rt} f(t) \, dt.
$$

For the Black-Cox model, this has a semi-closed form involving the normal CDF.

### Credit Spread

The credit spread is:

$$
s(T) = -\frac{1}{T} \ln\left(\frac{P^d(0,T)}{D \cdot e^{-rT}}\right).
$$

First-passage models generate non-trivial short-term spreads (unlike Merton), because there is always positive probability of hitting the barrier immediately.

---

## Term Structure of Credit Spreads

### Short-Maturity Behavior

As $T \to 0$:
- Merton model: $s(T) \to 0$ if $V_0 > D$
- First-passage model: $s(T) \to s_0 > 0$ (positive short-term spread)

This is because there is always instantaneous default risk when the barrier can be hit at any time.

### Long-Maturity Behavior

As $T \to \infty$:
- If $\mu > 0$: Asset drifts away from barrier, spreads decrease
- If $\mu < 0$: Default becomes certain, spreads increase
- If $\mu = 0$: Spreads converge to a finite limit

### Hump-Shaped Spread Curves

First-passage models can generate **hump-shaped** credit spread curves, which are empirically observed:
- Short maturities: Positive spread due to immediate default risk
- Medium maturities: Peak spread as default probability accumulates
- Long maturities: Spread may decrease if firm is likely to survive

---

## Extensions of the Black-Cox Model

### Time-Varying Barrier (Longstaff-Schwartz)

Let $B_t = K e^{\gamma t}$ for constants $K$ and $\gamma$:

$$
\tau = \inf\{t : V_t \le K e^{\gamma t}\}.
$$

This is equivalent to first passage of $V_t e^{-\gamma t}$ to level $K$, which can be solved similarly.

### Stochastic Interest Rates (Longstaff-Schwartz, 1995)

Combine first-passage default with Vasicek interest rates:

$$
dr_t = \kappa(\theta - r_t)dt + \sigma_r dW_t^r.
$$

Correlation between $W^r$ and $W^V$ introduces interest rate—credit risk dependence.

### Jump-Diffusion Asset Dynamics

Add jumps to asset value:

$$
dV_t = (r - q - \lambda \bar{k})V_t dt + \sigma V_t dW_t + V_{t-}(J_t - 1)dN_t,
$$

where $N_t$ is a Poisson process with intensity $\lambda$ and $J_t$ is the jump size with $\bar{k} = \mathbb{E}[J - 1]$.

Jumps allow for sudden default, partially addressing short-term spread issues.

---

## Comparison with Merton Model

| Feature | Merton Model | First-Passage Model |
|---------|--------------|---------------------|
| Default timing | Only at maturity $T$ | Any time $t \le T$ |
| Short-term spreads | Near zero | Positive |
| Spread term structure | Always upward sloping | Can be hump-shaped |
| Analytical tractability | Very high | High (constant barrier) |
| Economic realism | Limited | Better |
| Barrier interpretation | Debt face value | Safety covenant level |

---

## Calibration Challenges

### Unobservable Barrier

The default barrier $B$ is not directly observable and must be:
- Estimated from historical defaults
- Calibrated to CDS spreads or bond prices
- Derived from optimal default theory (endogenous barrier)

### Multiple Parameters

The model has parameters $(V_0, \sigma, B)$, but only equity and some credit instruments are observed. Identification requires:
- Joint calibration to equity and credit markets
- Constraints from economic theory (e.g., limited liability)
- Historical default data

### Sensitivity to Barrier Level

Small changes in $B$ can produce large changes in:
- Short-term default probabilities
- Credit spreads
- Hedge ratios

This sensitivity is a source of model risk.

---

## Numerical Example

**Parameters:**
- Asset value: $V_0 = 100$
- Default barrier: $B = 60$
- Risk-free rate: $r = 5\%$
- Asset volatility: $\sigma = 25\%$
- Dividend rate: $q = 2\%$
- Time horizon: $T = 5$ years

**Calculations:**

Drift parameter: $\mu = r - q - \sigma^2/2 = 0.05 - 0.02 - 0.03125 = -0.00125$

Log-barrier distance: $a = \ln(100/60) = 0.5108$

$$
d_+ = \frac{0.5108 + (-0.00125)(5)}{0.25\sqrt{5}} = \frac{0.5046}{0.559} = 0.902
$$

$$
d_- = \frac{-0.5108 + (-0.00125)(5)}{0.25\sqrt{5}} = \frac{-0.5171}{0.559} = -0.925
$$

Exponent: $2\mu/\sigma^2 = 2(-0.00125)/(0.0625) = -0.04$

$$
\left(\frac{B}{V_0}\right)^{2\mu/\sigma^2} = (0.6)^{-0.04} = 1.0205
$$

**Survival probability:**
$$
S(0,5) = N(0.902) - 1.0205 \times N(-0.925) = 0.8165 - 1.0205 \times 0.1775 = 0.635
$$

**5-year default probability:** $36.5\%$

---

## Key Takeaways

- First-passage models allow default at any time via barrier crossing
- They produce positive short-term spreads, unlike Merton
- The Black-Cox model has closed-form survival probabilities
- Spread term structures can be hump-shaped, matching empirical patterns
- The default barrier is economically meaningful but unobservable
- Calibration requires joint estimation from equity and credit markets

---

## Further Reading

- Black, F., & Cox, J. C. (1976). Valuing corporate securities: Some effects of bond indenture provisions. *Journal of Finance*, 31(2), 351–367.
- Longstaff, F. A., & Schwartz, E. S. (1995). A simple approach to valuing risky fixed and floating rate debt. *Journal of Finance*, 50(3), 789–819.
- Leland, H. E. (1994). Corporate debt value, bond covenants, and optimal capital structure. *Journal of Finance*, 49(4), 1213–1252.
- Leland, H. E., & Toft, K. B. (1996). Optimal capital structure, endogenous bankruptcy, and the term structure of credit spreads. *Journal of Finance*, 51(3), 987–1019.
