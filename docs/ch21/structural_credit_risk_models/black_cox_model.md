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

??? success "Solution to Exercise 1"
    **Given:** Constant barrier $B = 60$, $V_0 = 100$, $\sigma_V = 0.25$, $r = 0.04$, $T = 5$, $q = 0$.

    **Step 1: Compute the Black-Cox first-passage default probability.**

    The risk-neutral drift is $\mu = r - q - \sigma_V^2/2 = 0.04 - 0 - 0.03125 = 0.00875$.

    The log-barrier distance is $a = \ln(V_0/B) = \ln(100/60) = 0.5108$.

    $$
    d_+ = \frac{a + \mu T}{\sigma_V\sqrt{T}} = \frac{0.5108 + 0.00875 \times 5}{0.25\sqrt{5}} = \frac{0.5108 + 0.04375}{0.55902} = \frac{0.55455}{0.55902} = 0.9920
    $$

    $$
    d_- = \frac{-a + \mu T}{\sigma_V\sqrt{T}} = \frac{-0.5108 + 0.04375}{0.55902} = \frac{-0.46705}{0.55902} = -0.8354
    $$

    The exponent in the reflection term:

    $$
    \frac{2\mu}{\sigma_V^2} = \frac{2 \times 0.00875}{0.0625} = 0.28
    $$

    $$
    \left(\frac{B}{V_0}\right)^{2\mu/\sigma_V^2} = (0.60)^{0.28} = e^{0.28 \ln(0.60)} = e^{0.28 \times (-0.5108)} = e^{-0.14302} = 0.8668
    $$

    **Survival probability:**

    $$
    S(0,5) = N(d_+) - \left(\frac{B}{V_0}\right)^{2\mu/\sigma_V^2} N(d_-) = N(0.9920) - 0.8668 \times N(-0.8354)
    $$

    $$
    = 0.8394 - 0.8668 \times 0.2017 = 0.8394 - 0.1749 = 0.6645
    $$

    **First-passage default probability:**

    $$
    \mathbb{Q}(\tau \le 5) = 1 - S(0,5) = 1 - 0.6645 = 0.3355 \approx 33.6\%
    $$

    **Step 2: Compute the Merton default probability.**

    In the Merton model, default occurs only if $V_T < D$. Using $D = 60$ (same as barrier) and the terminal distribution:

    $$
    d_2^{\text{Merton}} = \frac{\ln(V_0/D) + (r - \sigma_V^2/2)T}{\sigma_V\sqrt{T}} = \frac{0.5108 + 0.00875 \times 5}{0.55902} = 0.9920
    $$

    $$
    \mathbb{Q}^{\text{Merton}}(V_T < 60) = N(-d_2^{\text{Merton}}) = N(-0.9920) = 0.1606 \approx 16.1\%
    $$

    **Comparison:** The Black-Cox default probability ($33.6\%$) is more than double the Merton probability ($16.1\%$). This is because the first-passage model captures all paths that touch $B = 60$ at any time $t \in [0, 5]$, including paths that later recover above 60 by maturity. The Merton model only counts paths ending below 60, missing the paths that crossed 60 at intermediate times but recovered. The first-passage probability must always be at least as large as the terminal probability.

---

**Exercise 2.** Explain why the Black-Cox model produces positive credit spreads at short maturities, unlike the Merton model. Relate this to the first-passage property: the firm can default at any instant if it is close to the barrier. What role does the ratio $V_0/B$ play in determining short-term spreads?

??? success "Solution to Exercise 2"
    **Why the Black-Cox model produces positive short-term spreads:**

    In the Merton model, default occurs only at the terminal date $T$, requiring $V_T < D$. For a continuous diffusion starting at $V_0 > D$, the probability that $V_T < D$ for small $T$ is governed by:

    $$
    \mathbb{Q}(V_T < D) = N\left(\frac{\ln(D/V_0) - (r - \sigma^2/2)T}{\sigma\sqrt{T}}\right) \approx N\left(\frac{-a}{\sigma\sqrt{T}}\right) \to 0
    $$

    as $T \to 0$, where $a = \ln(V_0/D) > 0$. The argument of $N(\cdot)$ goes to $-\infty$ as $T \to 0$, so the probability (and hence the spread) vanishes.

    In the Black-Cox model, default can occur at **any** time. Even for short horizons, there is a nonzero probability that the continuous Brownian path touches the barrier. The first-passage probability for a Brownian motion with drift to hit a barrier at distance $a$ satisfies:

    $$
    \mathbb{Q}(\tau \le T) \approx 2N\left(\frac{-a}{\sigma\sqrt{T}}\right) + \text{drift correction}
    $$

    for small $T$. Although this also goes to zero as $T \to 0$ when $V_0 > B$, the credit spread $s(T) = -\frac{1}{T}\ln S(0,T)$ can remain positive or even diverge.

    More precisely, the survival probability satisfies $S(0,T) = 1 - c \cdot e^{-a^2/(2\sigma^2 T)} + \ldots$ for small $T$, and the spread behaves as:

    $$
    s(T) \sim \frac{a^2}{2\sigma^2 T} \cdot \frac{1}{T} \cdot e^{-a^2/(2\sigma^2 T)}
    $$

    which is positive for all $T > 0$, though it can be very small for large $a$.

    **Role of $V_0/B$:** The ratio $V_0/B$ determines the log-barrier distance $a = \ln(V_0/B)$. When $V_0/B$ is close to 1 (firm is near the barrier), $a$ is small, and the short-term default probability is significant because the Brownian path can easily reach the barrier. The short-term spread scales as $\sigma^2/(2\sqrt{T})$ times a function of $a/(\sigma\sqrt{T})$. For $V_0/B$ close to 1, spreads are large at all maturities, including very short ones. For $V_0/B \gg 1$, the barrier is far away, and short-term spreads, while technically positive, are negligibly small.

---

**Exercise 3.** Consider an exponential barrier $B_t = B_0\,e^{\gamma t}$ where $\gamma < r$. Explain the economic interpretation: the barrier represents a growing minimum net worth requirement. If $B_0 = 50$, $\gamma = 2\%$, and $r = 4\%$, compute $B_5$ and discuss whether this barrier is realistic for a typical corporate borrower.

??? success "Solution to Exercise 3"
    **Given:** Exponential barrier $B_t = B_0 e^{\gamma t}$ with $B_0 = 50$, $\gamma = 0.02$, $r = 0.04$.

    **Economic interpretation:**

    The exponentially growing barrier $B_t = B_0 e^{\gamma t}$ models a **growing minimum net worth requirement**. This represents:

    - **Covenant escalation:** Loan agreements that require the borrower to maintain an asset base growing at rate $\gamma$, reflecting expected business growth.
    - **Inflation-adjusted thresholds:** If nominal liabilities grow with inflation at rate $\gamma$, the real protective buffer must keep pace.
    - **Regulatory capital requirements:** Banks and financial institutions often face capital requirements that grow with their asset base.

    The condition $\gamma < r$ (here $0.02 < 0.04$) ensures that the barrier grows more slowly than the risk-free rate. If the barrier grew faster than $r$, the risk-neutral expected asset value would eventually be overtaken by the barrier with certainty, making the firm fundamentally unsustainable.

    **Compute $B_5$:**

    $$
    B_5 = B_0 e^{\gamma \times 5} = 50 \times e^{0.02 \times 5} = 50 \times e^{0.10} = 50 \times 1.1052 = 55.26
    $$

    **Realism assessment:** Starting at $B_0 = 50$ (against $V_0 = 100$, say), the barrier grows from 50 to 55.26 over 5 years, an increase of about 10.5%. This is a moderate tightening. For a typical corporate borrower:

    - The growth rate $\gamma = 2\%$ is reasonable -- it approximates long-run inflation, ensuring covenants maintain real value.
    - The barrier-to-asset ratio starts at $B_0/V_0 = 0.50$ and, assuming the firm grows at rate $r = 4\%$ in expectation, the ratio $B_t/\mathbb{E}[V_t]$ stays roughly stable since $\gamma < r$.
    - The level is realistic for a well-capitalized firm: creditors typically require asset coverage ratios (assets/liabilities) above 1.5--2.0, corresponding to a barrier around 50--67% of asset value.

    In practice, covenant levels are often adjusted at discrete dates rather than continuously, but the exponential specification provides a tractable continuous-time approximation to this discrete tightening.

---

**Exercise 4.** The Black-Cox model can produce upward-sloping, humped, or downward-sloping credit spread curves depending on the firm's distance to the barrier. For a firm with $V_0/B = 2$ (far from barrier), describe the expected spread curve shape. Repeat for $V_0/B = 1.1$ (near barrier). Explain the economic intuition.

??? success "Solution to Exercise 4"
    **Case 1: $V_0/B = 2$ (far from barrier) -- Upward-sloping spread curve.**

    When the firm's asset value is twice the barrier level, the log-distance $a = \ln(2) \approx 0.693$ is large relative to the diffusion scale $\sigma\sqrt{T}$ for short maturities. This means:

    - **Short maturities ($T$ small):** The probability of the Brownian path traveling distance $a$ in a short time is extremely small ($\sim e^{-a^2/(2\sigma^2 T)}$), so spreads are very low.
    - **Medium maturities:** As $T$ increases, the diffusion has more time to reach the barrier, and default probability grows. Spreads increase.
    - **Long maturities:** If $\mu > 0$ (positive risk-neutral drift), the firm drifts further from the barrier on average, partially offsetting the increased diffusion range. Spreads continue to rise but at a decreasing rate.

    Overall shape: **upward-sloping**, similar to the Merton model. The firm is safe enough that spreads increase with horizon as more time allows for default.

    **Case 2: $V_0/B = 1.1$ (near barrier) -- Downward-sloping spread curve.**

    When the firm is very close to the barrier, $a = \ln(1.1) \approx 0.095$ is very small. This means:

    - **Short maturities ($T$ small):** Even in a short interval, the Brownian path can easily reach the nearby barrier. The default probability is significant, and the annualized spread $s(T) = -\frac{1}{T}\ln S(0,T)$ can be very large because the per-period risk is high.
    - **Medium maturities:** Additional default probability accumulates, but the denominator $T$ also grows, so the annualized spread starts to moderate.
    - **Long maturities:** If $\mu > 0$, the firm's expected asset value drifts away from the barrier over time. The probability of *surviving* to long horizons increases the conditional survival component, and the annualized spread decreases.

    Overall shape: **downward-sloping** (inverted). The highest risk is at short horizons when the firm may imminently hit the barrier.

    **Which case produces a humped curve?** A **moderate** distance to barrier, such as $V_0/B \approx 1.3$--$1.6$, produces a hump-shaped curve. At short maturities, the barrier is still far enough that spreads start low. At intermediate maturities, default probability accumulates significantly, pushing spreads to a peak. At long maturities, mean reversion (positive drift) pulls spreads back down. This hump shape is one of the key advantages of the Black-Cox model over Merton, as it matches empirically observed spread curves for medium-quality credits.

---

**Exercise 5.** Compare the Black-Cox model with the Merton model along three dimensions: (a) timing of possible default, (b) short-maturity credit spread behavior, and (c) variety of credit spread curve shapes. Which model is better suited for pricing short-dated credit derivatives?

??? success "Solution to Exercise 5"
    **(a) Timing of possible default.**

    - **Merton model:** Default can occur **only at maturity** $T$. The default event is $\{V_T < D\}$. No matter how low the asset value drops at intermediate dates, default is not triggered until the debt matures.
    - **Black-Cox model:** Default can occur **at any time** $t \in [0, T]$. The default time is $\tau = \inf\{t : V_t \le B_t\}$. If the firm survives to maturity ($\tau > T$), an additional Merton-type check may apply. This is far more realistic, as real-world defaults are triggered by cash-flow crises, covenant breaches, or creditor actions that can happen at any time.

    **(b) Short-maturity credit spread behavior.**

    - **Merton model:** For a solvent firm ($V_0 > D$), the credit spread $s(T) \to 0$ as $T \to 0$. The probability of a continuous diffusion ending below the strike in a vanishing time interval goes to zero super-exponentially. This contradicts the empirical observation that even high-quality borrowers have non-trivial short-term spreads.
    - **Black-Cox model:** Credit spreads remain **positive** at short maturities, $s(T) \to s_0 > 0$ as $T \to 0$ (or can even diverge for near-barrier firms). The first-passage mechanism ensures that there is always instantaneous default risk, producing realistic short-term spreads. For distressed firms near the barrier, short-term spreads can be very large.

    **(c) Variety of credit spread curve shapes.**

    - **Merton model:** The spread curve is essentially **always upward-sloping** for solvent firms ($V_0 > D$). Spreads start near zero and increase with maturity. There is no mechanism to generate hump-shaped or inverted curves.
    - **Black-Cox model:** Depending on the ratio $V_0/B$, the model generates **three distinct shapes**:
        - *Upward-sloping:* Low leverage, firm far from barrier.
        - *Hump-shaped:* Moderate leverage, peak at intermediate maturity.
        - *Downward-sloping (inverted):* High leverage, firm near barrier.

    This flexibility is empirically important, as all three shapes are observed in credit markets.

    **Recommendation for short-dated credit derivatives:** The Black-Cox model (or more generally, a first-passage model) is clearly superior for pricing **short-dated credit derivatives** such as 1-month or 3-month CDS contracts, short-term credit options, and near-term default probability estimation. The Merton model's vanishing short-term spreads make it unsuitable for these instruments. The first-passage framework correctly captures the instantaneous default risk that drives short-dated pricing.

---

**Exercise 6.** In the Black-Cox model, safety covenants trigger early default when asset value hits the barrier. Explain how this feature models real-world covenant violations in loan agreements. What happens to the model's default probability if the barrier $B$ is raised (more stringent covenants)?

??? success "Solution to Exercise 6"
    **How the barrier models covenant violations:**

    In real-world loan agreements, **financial covenants** are contractual provisions that require the borrower to maintain certain financial ratios or minimum values. Common covenants include:

    - **Minimum net worth:** Total assets minus total liabilities must exceed a threshold.
    - **Maximum leverage ratio:** Debt-to-equity or debt-to-assets ratio must stay below a ceiling.
    - **Interest coverage ratio:** EBITDA/interest expense must exceed a minimum (e.g., 2.0x).
    - **Minimum asset coverage:** Asset value must exceed a specified multiple of debt.

    The Black-Cox barrier $B_t$ directly models these covenants. When the firm's asset value $V_t$ falls to the barrier level $B_t$, this represents a covenant violation -- the firm has failed to maintain the required financial health metric. Upon violation:

    - Creditors may **accelerate** the debt (demand immediate repayment).
    - The firm may be forced into **technical default** even if it has positive cash flow.
    - Creditors may renegotiate terms, impose stricter conditions, or seize collateral.
    - The firm may be forced into bankruptcy proceedings.

    The first-passage mechanism ($\tau = \inf\{t : V_t \le B_t\}$) captures the key feature that covenant violations trigger default at the **first** instance of breach, regardless of subsequent recovery. This is realistic: once a covenant is violated, the legal consequences are immediate, even if the firm's fundamentals might improve later.

    **Effect of raising the barrier $B$:**

    If the barrier $B$ is increased (more stringent covenants), the default probability **increases** unambiguously. This follows from the mathematical structure:

    - The log-barrier distance $a = \ln(V_0/B)$ decreases when $B$ increases.
    - In the survival probability formula:

    $$
    S(0,T) = N(d_+) - \left(\frac{B}{V_0}\right)^{2\mu/\sigma^2} N(d_-)
    $$

    both $d_+$ decreases (reducing $N(d_+)$) and $B/V_0$ increases (increasing the reflection term's magnitude for typical parameter values), so $S(0,T)$ decreases.

    - The default probability $\mathbb{Q}(\tau \le T) = 1 - S(0,T)$ therefore increases.

    **Intuition:** A higher barrier means the firm has less room to maneuver before triggering a covenant breach. The asset value needs to fall by a smaller amount to cross the barrier. In the extreme, if $B \to V_0$, default becomes nearly instantaneous ($\tau \to 0$). Conversely, $B \to 0$ makes the barrier irrelevant (the firm never defaults via first passage, reverting to a Merton-like setup).

    This has practical implications: borrowers with **tight covenants** (high $B$) face higher model-implied default probabilities, wider credit spreads, and shorter expected time-to-default, even if their underlying asset dynamics are identical to firms with looser covenants.
