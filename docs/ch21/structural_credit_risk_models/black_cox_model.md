# Black-Cox Model

The **Black-Cox model** (1976) extends the Merton framework by allowing default to occur at any time before maturity, not only at the debt maturity date. Default is triggered when the firm's asset value first crosses a **time-dependent barrier**, reflecting safety covenants or minimum net worth requirements. This first-passage approach produces more realistic credit spreads, particularly for short maturities.

---

## Motivation and Setup

### Limitations of the Merton Model

In the Merton model, default occurs only at maturity $T$ when $V_T < D$. This restriction leads to:

- **Vanishing short-term spreads:** For solvent firms ($V_0 > D$), the probability of default in a short interval is negligible under diffusion
- **No early default:** Firms cannot default due to cash-flow crises or covenant violations before maturity
- **Unrealistic term structure:** Spread curves are always upward-sloping for investment-grade firms

Black and Cox addressed these shortcomings by introducing a **safety covenant** that triggers default whenever firm value falls to a specified barrier.

### Model Assumptions

Consider a firm with:

- Asset value process $(V_t)_{t \ge 0}$ under the risk-neutral measure $\mathbb{Q}$
- Risk-neutral dynamics:

$$
dV_t = (r - q)V_t \, dt + \sigma V_t \, dW_t^{\mathbb{Q}}
$$

where $r$ is the risk-free rate, $q$ is the payout rate, and $\sigma$ is asset volatility.

- A **default barrier** $B_t$ that may depend on time
- Face value of debt $D$ due at maturity $T$

---

## Default Mechanism

### First-Passage Default Time

Default occurs at the first time the asset value touches or crosses the barrier:

$$
\tau = \inf\{t \ge 0 : V_t \le B_t\}
$$

with the convention $\inf \emptyset = +\infty$ (no default if the barrier is never reached).

At maturity, if the firm has survived (i.e., $\tau > T$), default can still occur in the Merton sense if $V_T < D$. The combined default time is therefore:

$$
\tau^* = \tau \wedge T \cdot \mathbf{1}_{\{\tau \le T\}} + T \cdot \mathbf{1}_{\{\tau > T, \, V_T < D\}} + \infty \cdot \mathbf{1}_{\{\tau > T, \, V_T \ge D\}}
$$

In many treatments, the barrier default dominates and the maturity check is secondary.

### Economic Interpretation

The barrier $B_t$ represents:

- **Safety covenants** in bond indentures requiring minimum asset coverage
- **Regulatory thresholds** (e.g., bank capital requirements)
- **Endogenous default boundaries** chosen optimally by equity holders
- **Effective liquidation triggers** from creditor actions

---

## Time-Dependent Barrier Specifications

### Constant Barrier

The simplest case sets $B_t = B$ for all $t$, where $B < V_0$. This is the original Black-Cox specification.

### Exponential Barrier

A more general specification uses an exponentially varying barrier:

$$
B_t = K e^{\gamma(T-t)}
$$

where $K$ is the barrier level at maturity and $\gamma$ is the growth/decay rate.

- $\gamma > 0$: Barrier decreases toward maturity (amortizing protection)
- $\gamma < 0$: Barrier increases toward maturity (tightening covenant)
- $\gamma = 0$: Constant barrier $B_t = K$

Black and Cox specifically studied the case $B_t = K e^{-\gamma(T-t)}$ with $\gamma > 0$, representing a covenant that becomes less restrictive as maturity approaches.

### Transformation to Constant-Barrier Problem

For an exponential barrier $B_t = K e^{\gamma t}$, define the transformed process:

$$
\tilde{V}_t = V_t e^{-\gamma t}
$$

Then $V_t \le K e^{\gamma t}$ if and only if $\tilde{V}_t \le K$, reducing to a constant-barrier first-passage problem for $\tilde{V}_t$ with adjusted drift $\tilde{\mu} = r - q - \sigma^2/2 - \gamma$.

---

## Survival Probability

### Log-Transform and Brownian Motion

Define $X_t = \ln V_t$. Then:

$$
X_t = X_0 + \mu t + \sigma W_t^{\mathbb{Q}}
$$

where $\mu = r - q - \sigma^2/2$ and $X_0 = \ln V_0$.

For a constant barrier $B$, default occurs when $X_t$ first hits $\ln B$. Define the log-barrier distance:

$$
a = \ln(V_0 / B) > 0
$$

The default time becomes the first-passage time of a Brownian motion with drift $\mu$ to level $-a$:

$$
\tau = \inf\{t \ge 0 : \mu t + \sigma W_t \le -a\}
$$

### Closed-Form Survival Probability

The survival probability up to time $T$ is:

$$
S(0,T) = \mathbb{Q}(\tau > T) = N(d_+) - \left(\frac{B}{V_0}\right)^{2\mu/\sigma^2} N(d_-)
$$

where:

$$
d_+ = \frac{\ln(V_0/B) + \mu T}{\sigma\sqrt{T}}, \quad d_- = \frac{\ln(B/V_0) + \mu T}{\sigma\sqrt{T}}
$$

and $N(\cdot)$ is the standard normal CDF.

!!! tip "Derivation Sketch"
    The formula follows from the **reflection principle** for Brownian motion with drift. For a drifted Brownian motion $Y_t = \mu t + \sigma W_t$, the probability $\mathbb{P}(\min_{0 \le s \le t} Y_s > -a)$ is obtained by combining the direct path probability with the reflected path contribution, weighted by $e^{-2\mu a/\sigma^2}$.

### General Forward Survival Probability

For $t < T$, on the event $\{\tau > t\}$:

$$
S(t,T) = \mathbb{Q}(\tau > T \mid \tau > t, \mathcal{F}_t) = N(d_+^t) - \left(\frac{B}{V_t}\right)^{2\mu/\sigma^2} N(d_-^t)
$$

where:

$$
d_+^t = \frac{\ln(V_t/B) + \mu(T-t)}{\sigma\sqrt{T-t}}, \quad d_-^t = \frac{\ln(B/V_t) + \mu(T-t)}{\sigma\sqrt{T-t}}
$$

---

## Density of Default Time

### First-Passage Time Density

The density of the default time $\tau$ is given by the **inverse Gaussian** distribution:

$$
f_\tau(t) = \frac{a}{\sigma\sqrt{2\pi t^3}} \exp\left(-\frac{(a + \mu t)^2}{2\sigma^2 t}\right), \quad t > 0
$$

where $a = \ln(V_0/B)$.

**Properties:**

- $f_\tau(t) \to 0$ as $t \to 0^+$ (no instantaneous default for $V_0 > B$)
- $f_\tau(t) \to 0$ as $t \to \infty$ (if $\mu > 0$)
- Unimodal: single peak at the most likely default time
- $\int_0^\infty f_\tau(t) dt = 1$ if $\mu \le 0$, and $< 1$ if $\mu > 0$ (positive drift means the firm may never default)

### Expected Discounted Default Indicator

A key quantity for bond pricing is:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-r\tau} \mathbf{1}_{\{\tau \le T\}}\right] = \int_0^T e^{-rt} f_\tau(t) \, dt
$$

This can be evaluated in closed form using:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-r\tau} \mathbf{1}_{\{\tau \le T\}}\right] = \left(\frac{B}{V_0}\right)^{\alpha_+} N(h_+) + \left(\frac{B}{V_0}\right)^{\alpha_-} N(h_-)
$$

where:

$$
\alpha_{\pm} = \frac{-\mu \pm \sqrt{\mu^2 + 2r\sigma^2}}{\sigma^2}
$$

$$
h_+ = \frac{-a + \sqrt{\mu^2 + 2r\sigma^2} \cdot T}{\sigma\sqrt{T}}, \quad h_- = \frac{-a - \sqrt{\mu^2 + 2r\sigma^2} \cdot T}{\sigma\sqrt{T}}
$$

---

## Pricing Defaultable Bonds

### Zero-Coupon Bond with Recovery

Consider a zero-coupon bond with face value $D$, maturity $T$, and recovery at default:

- If $\tau > T$: bondholder receives $D$
- If $\tau \le T$: bondholder receives $R \cdot B$ at time $\tau$ (recovery of barrier value)

The bond price is:

$$
P^d(0,T) = D \cdot e^{-rT} \cdot S(0,T) + R \cdot B \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-r\tau} \mathbf{1}_{\{\tau \le T\}}\right]
$$

### Credit Spread

The yield on the defaultable bond is:

$$
y^d = -\frac{1}{T}\ln\left(\frac{P^d(0,T)}{D}\right)
$$

and the credit spread is:

$$
s(T) = y^d - r = -\frac{1}{T}\ln\left(\frac{P^d(0,T)}{D \cdot e^{-rT}}\right)
$$

---

## Short-Term Spread Behavior

### Comparison with Merton

A critical advantage of the Black-Cox model is its behavior for short maturities.

**Merton model ($T \to 0$, $V_0 > D$):**

$$
s_{\text{Merton}}(T) \to 0
$$

The spread vanishes because the probability that a continuous diffusion reaches the barrier at maturity shrinks faster than $T$.

**Black-Cox model ($T \to 0$, $V_0 > B$):**

$$
s_{\text{Black-Cox}}(T) \to s_0 > 0
$$

The spread remains positive because there is always a nonzero instantaneous probability of the diffusion path touching the barrier.

More precisely, for $V_0$ close to $B$:

$$
s(T) \approx \frac{\sigma^2}{2} \cdot \frac{N'(d_+)}{N(d_+)} \cdot \frac{1}{\sqrt{T}} + O(1)
$$

which diverges as $T \to 0$, matching the empirically observed pattern for distressed firms.

### Term Structure Shapes

The Black-Cox model generates richer term structures than Merton:

| Firm Quality | Leverage | Spread Curve Shape |
|-------------|----------|-------------------|
| High quality | Low | Upward sloping |
| Medium quality | Moderate | Humped (peak at intermediate maturity) |
| Distressed | High | Downward sloping |

The hump-shaped curve arises because:

- At short maturities, barrier proximity dominates
- At long maturities, positive drift pulls the firm away from default
- The peak reflects the balance between these forces

---

## Equity and Debt Valuation

### Equity Value

In the Black-Cox model, equity is a **down-and-out call option** on firm value with barrier $B$ and strike $D$:

$$
E_0 = \mathbb{E}^{\mathbb{Q}}\left[e^{-rT}(V_T - D)^+ \mathbf{1}_{\{\tau > T\}}\right]
$$

This is a standard barrier option with closed-form solution:

$$
E_0 = V_0 e^{-qT}\left[N(d_1) - \left(\frac{B}{V_0}\right)^{2(r-q)/\sigma^2 + 1} N(e_1)\right] - D e^{-rT}\left[N(d_2) - \left(\frac{B}{V_0}\right)^{2(r-q)/\sigma^2 - 1} N(e_2)\right]
$$

where $d_1, d_2$ are the standard Black-Scholes terms and $e_1, e_2$ are their barrier-adjusted counterparts.

### Debt Value

Debt value follows from the balance sheet identity:

$$
B_0^{\text{debt}} = V_0 - E_0
$$

minus the present value of payouts. Alternatively, it is the sum of survival and recovery components.

---

## Numerical Example

**Parameters:**

- Asset value: $V_0 = 100$
- Default barrier: $B = 65$
- Face value of debt: $D = 80$
- Risk-free rate: $r = 5\%$
- Asset volatility: $\sigma = 25\%$
- Payout rate: $q = 2\%$
- Maturity: $T = 5$ years
- Recovery: $R = 40\%$

**Step 1: Drift parameter**

$$
\mu = r - q - \sigma^2/2 = 0.05 - 0.02 - 0.03125 = -0.00125
$$

**Step 2: Log-barrier distance**

$$
a = \ln(100/65) = 0.4308
$$

**Step 3: Survival probability**

$$
d_+ = \frac{0.4308 + (-0.00125)(5)}{0.25\sqrt{5}} = \frac{0.4245}{0.5590} = 0.7594
$$

$$
d_- = \frac{-0.4308 + (-0.00125)(5)}{0.25\sqrt{5}} = \frac{-0.4371}{0.5590} = -0.7819
$$

Exponent: $2\mu/\sigma^2 = 2(-0.00125)/0.0625 = -0.04$

$$
\left(\frac{B}{V_0}\right)^{2\mu/\sigma^2} = (0.65)^{-0.04} = e^{-0.04 \ln 0.65} = e^{0.01724} = 1.0174
$$

$$
S(0,5) = N(0.7594) - 1.0174 \times N(-0.7819) = 0.7762 - 1.0174 \times 0.2171 = 0.7762 - 0.2209 = 0.5553
$$

**Step 4: 5-year default probability**

$$
\mathbb{Q}(\tau \le 5) = 1 - 0.5553 = 44.47\%
$$

**Step 5: Bond price (with recovery at barrier)**

Protection leg:

$$
P^d(0,5) \approx 80 \times e^{-0.25} \times 0.5553 + 0.40 \times 65 \times (1 - 0.5553) \times e^{-0.25 \times 0.5} \approx 34.59 + 22.70 = 57.29
$$

(Here we approximate the expected discounted default payment.)

**Step 6: Credit spread**

$$
y^d = -\frac{1}{5}\ln\left(\frac{57.29}{80}\right) = \frac{0.3339}{5} = 6.68\%
$$

$$
s = 6.68\% - 5.00\% = 1.68\% = 168 \text{ bp}
$$

---

## Comparison: Black-Cox vs Merton

| Feature | Merton Model | Black-Cox Model |
|---------|-------------|-----------------|
| Default timing | Only at maturity $T$ | Any time $t \le T$ |
| Default trigger | $V_T < D$ | $V_t \le B_t$ |
| Short-term spreads | Near zero for solvent firms | Positive |
| Spread term structure | Upward sloping only | Upward, humped, or inverted |
| Barrier | Implicit (debt face value) | Explicit (covenant level) |
| Recovery mechanism | $\min(V_T, D)$ at maturity | $R \cdot B$ at first passage |
| Mathematical tools | European option pricing | Barrier option pricing |
| Calibration difficulty | Moderate | Higher (barrier is unobservable) |

---

## Extensions

### Stochastic Interest Rates (Longstaff-Schwartz)

Combining first-passage default with stochastic rates:

$$
dr_t = \kappa(\theta - r_t)dt + \sigma_r dW_t^r
$$

with correlation $\rho$ between $W^r$ and $W^V$, allowing interest rate-credit risk dependence.

### Endogenous Default Barrier (Leland)

Equity holders choose the default barrier optimally to maximize equity value. The endogenous barrier satisfies the **smooth-pasting condition**:

$$
\left.\frac{\partial E}{\partial V}\right|_{V = B^*} = 0
$$

yielding:

$$
B^* = \frac{C}{r} \cdot \frac{\alpha_+}{\alpha_+ + 1}
$$

where $C$ is the coupon rate and $\alpha_+$ is the positive root of the characteristic equation.

### Jump-Diffusion Models

Adding jumps to the asset value process:

$$
\frac{dV_t}{V_{t-}} = (r - q - \lambda \bar{k})dt + \sigma dW_t + (J - 1)dN_t
$$

Jumps generate truly instantaneous default risk even when the firm is far from the barrier, further improving short-term spread calibration.

---

## Key Takeaways

- The Black-Cox model introduces a default barrier allowing early default via first-passage
- Default time has the inverse Gaussian distribution with closed-form survival probability
- Short-term credit spreads are positive, unlike the Merton model
- The model generates upward-sloping, humped, and inverted spread curves
- Equity is a down-and-out call option on firm value
- The barrier level is economically meaningful but unobservable, posing calibration challenges
- Extensions include stochastic rates, endogenous barriers, and jump-diffusion dynamics

---

## Further Reading

- Black, F., & Cox, J. C. (1976). Valuing corporate securities: Some effects of bond indenture provisions. *Journal of Finance*, 31(2), 351--367.
- Leland, H. E. (1994). Corporate debt value, bond covenants, and optimal capital structure. *Journal of Finance*, 49(4), 1213--1252.
- Longstaff, F. A., & Schwartz, E. S. (1995). A simple approach to valuing risky fixed and floating rate debt. *Journal of Finance*, 50(3), 789--819.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 3.

---

## Exercises

**Exercise 1.** In the Black-Cox model with constant barrier $B = 60$, firm value $V_0 = 100$, asset volatility $\sigma_V = 25\%$, risk-free rate $r = 4\%$, and maturity $T = 5$, compute the first-passage default probability using the formula for the hitting time of geometric Brownian motion. Compare with the Merton default probability where default only occurs at $T$.

---

**Exercise 2.** Explain why the Black-Cox model produces positive credit spreads at short maturities, unlike the Merton model. Relate this to the first-passage property: the firm can default at any instant if it is close to the barrier. What role does the ratio $V_0/B$ play in determining short-term spreads?

---

**Exercise 3.** Consider an exponential barrier $B_t = B_0\,e^{\gamma t}$ where $\gamma < r$. Explain the economic interpretation: the barrier represents a growing minimum net worth requirement. If $B_0 = 50$, $\gamma = 2\%$, and $r = 4\%$, compute $B_5$ and discuss whether this barrier is realistic for a typical corporate borrower.

---

**Exercise 4.** The Black-Cox model can produce upward-sloping, humped, or downward-sloping credit spread curves depending on the firm's distance to the barrier. For a firm with $V_0/B = 2$ (far from barrier), describe the expected spread curve shape. Repeat for $V_0/B = 1.1$ (near barrier). Explain the economic intuition.

---

**Exercise 5.** Compare the Black-Cox model with the Merton model along three dimensions: (a) timing of possible default, (b) short-maturity credit spread behavior, and (c) variety of credit spread curve shapes. Which model is better suited for pricing short-dated credit derivatives?

---

**Exercise 6.** In the Black-Cox model, safety covenants trigger early default when asset value hits the barrier. Explain how this feature models real-world covenant violations in loan agreements. What happens to the model's default probability if the barrier $B$ is raised (more stringent covenants)?
