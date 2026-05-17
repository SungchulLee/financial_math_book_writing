# First-Passage Models

First-passage models extend the Merton framework by allowing default to occur **at any time** before maturity, when the firm's asset value first crosses a default barrier. This addresses a key limitation of the Merton model—that default can only occur at debt maturity—and produces richer credit spread term structures.

---

## Default as Barrier Crossing

### Definition of Default Time

In first-passage models, the default time is defined as the **first hitting time** of a barrier:

$$
\tau = \inf\{t \ge 0 : V_t \le B_t\}
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
dV_t = (r - q)V_t \, dt + \sigma V_t \, dW_t^{\mathbb{Q}}
$$

with solution:

$$
V_t = V_0 \exp\left[\left(r - q - \frac{\sigma^2}{2}\right)t + \sigma W_t^{\mathbb{Q}}\right]
$$

### Common Barrier Specifications

**1. Constant Barrier (Black-Cox)**

$$
B_t = B \quad \text{(constant)}
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

Recall (see [§ Black-Cox Model](black_cox_model.md)) for the full derivation. Briefly: with constant barrier $B < V_0$ and $\tau = \inf\{t : V_t \le B\}$, set $a = \ln(V_0/B)$ and $\mu = r - q - \sigma^2/2$. Recall the [first-passage time](../../ch02/brownian_motion/first_passage_times.md) reduction:

$$
\tau = \inf\{t : \mu t + \sigma W_t \le -a\}.
$$

The survival probability, default CDF, and inverse-Gaussian default-time density follow from the reflection principle:

$$
S(0,T) = N(d_+) - (B/V_0)^{2\mu/\sigma^2} N(d_-), \qquad F(T) = 1 - S(0,T),
$$

$$
f(t) = \frac{a}{\sigma\sqrt{2\pi t^3}} \exp\!\left(-\frac{(a + \mu t)^2}{2\sigma^2 t}\right), \quad t > 0,
$$

with $d_\pm = (\pm\ln(V_0/B) + \mu T)/(\sigma\sqrt{T})$.

---

## Pricing Defaultable Bonds

Recall (see [§ Pricing Defaultable Bonds](black_cox_model.md#pricing-defaultable-bonds); deeper treatment in [pricing with default risk](../pricing_with_default_risk/defaultable_bonds.md)). For a zero-coupon bond paying $D$ at $T$ if $\tau > T$ and $RB$ at $\tau$ otherwise,

$$
P^d(0,T) = D e^{-rT} S(0,T) + RB\,\mathbb{E}^{\mathbb{Q}}\!\left[e^{-r\tau}\mathbf{1}_{\{\tau\le T\}}\right],
$$

and $s(T) = -\frac{1}{T}\ln[P^d(0,T)/(D e^{-rT})]$. Unlike Merton, $s(T) > 0$ as $T \to 0$ because the barrier may be hit immediately.

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
\tau = \inf\{t : V_t \le K e^{\gamma t}\}
$$

This is equivalent to first passage of $V_t e^{-\gamma t}$ to level $K$, which can be solved similarly.

### Stochastic Interest Rates (Longstaff-Schwartz, 1995)

Combine first-passage default with Vasicek interest rates:

$$
dr_t = \kappa(\theta - r_t)dt + \sigma_r dW_t^r
$$

Correlation between $W^r$ and $W^V$ introduces interest rate—credit risk dependence.

### Jump-Diffusion Asset Dynamics

Add jumps to asset value:

$$
dV_t = (r - q - \lambda \bar{k})V_t dt + \sigma V_t dW_t + V_{t-}(J_t - 1)dN_t
$$

where $N_t$ is a Poisson process with intensity $\lambda$ and $J_t$ is the jump size with $\bar{k} = \mathbb{E}[J - 1]$.

Jumps allow for sudden default, partially addressing short-term spread issues.

---

## Comparison with Merton Model

Recall (see [§ Comparison: Black-Cox vs Merton](black_cox_model.md#comparison-black-cox-vs-merton)) for the full table.

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

Recall (see [§ Numerical Example](black_cox_model.md#numerical-example)) for a worked first-passage calculation with $V_0=100$, $B=65$, $\sigma=25\%$, $T=5$.

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

---

## Exercises

**Exercise 1.** For geometric Brownian motion $dV_t = rV_t\,dt + \sigma_V V_t\,dW_t$ with $V_0 = 100$ and a constant barrier $B = 60$, the first-passage time $\tau = \inf\{t : V_t \le B\}$ has a known distribution. Compute the probability $\mathbb{Q}(\tau \le 5)$ using $\sigma_V = 25\%$ and $r = 4\%$. Compare with the Merton probability $\mathbb{Q}(V_5 \le D)$ for $D = 60$.

??? success "Solution to Exercise 1"
    **Given:** $V_0 = 100$, $B = 60$ (constant barrier), $\sigma_V = 0.25$, $r = 0.04$, $q = 0$, $T = 5$, $D = 60$ (for Merton comparison).

    **Step 1: First-passage default probability.**

    The risk-neutral drift: $\mu = r - q - \sigma_V^2/2 = 0.04 - 0 - 0.03125 = 0.00875$.

    Log-barrier distance: $a = \ln(V_0/B) = \ln(100/60) = 0.5108$.

    $$
    d_+ = \frac{a + \mu T}{\sigma_V\sqrt{T}} = \frac{0.5108 + 0.00875 \times 5}{0.25\sqrt{5}} = \frac{0.55455}{0.55902} = 0.9920
    $$

    $$
    d_- = \frac{-a + \mu T}{\sigma_V\sqrt{T}} = \frac{-0.5108 + 0.04375}{0.55902} = \frac{-0.46705}{0.55902} = -0.8354
    $$

    Reflection exponent: $2\mu/\sigma_V^2 = 2(0.00875)/0.0625 = 0.28$.

    $$
    \left(\frac{B}{V_0}\right)^{2\mu/\sigma_V^2} = (0.60)^{0.28} = e^{0.28 \ln(0.60)} = e^{-0.14302} = 0.8668
    $$

    Survival probability:

    $$
    S(0,5) = N(0.9920) - 0.8668 \times N(-0.8354) = 0.8394 - 0.8668 \times 0.2017
    $$

    $$
    = 0.8394 - 0.1749 = 0.6645
    $$

    **First-passage default probability:**

    $$
    \mathbb{Q}(\tau \le 5) = 1 - 0.6645 = 0.3355 \approx 33.6\%
    $$

    **Step 2: Merton default probability.**

    In the Merton model with $D = 60$, default occurs only if $V_T < D$:

    $$
    d_2^{\text{Merton}} = \frac{\ln(V_0/D) + (r - \sigma_V^2/2)T}{\sigma_V\sqrt{T}} = \frac{0.5108 + 0.04375}{0.55902} = 0.9920
    $$

    $$
    \mathbb{Q}^{\text{Merton}}(V_5 < 60) = N(-0.9920) = 0.1606 \approx 16.1\%
    $$

    **Comparison:** The first-passage probability ($33.6\%$) is roughly **twice** the Merton probability ($16.1\%$). The difference arises because the first-passage model counts all paths that touch the barrier at any point during $[0, 5]$, including those that subsequently recover above 60 by $T = 5$. The Merton model only counts paths ending below 60, missing the "transient defaults." Mathematically, $\{\min_{0 \le t \le 5} V_t \le 60\} \supseteq \{V_5 \le 60\}$, so the first-passage probability always exceeds the Merton probability.

---

**Exercise 2.** Explain why first-passage models produce positive credit spreads at arbitrarily short maturities while the Merton model does not. What property of the hitting time distribution of Brownian motion is responsible?

??? success "Solution to Exercise 2"
    **Why first-passage models produce positive short-term spreads while Merton does not:**

    **Merton model:** Default requires $V_T < D$ at the single terminal date. For a continuous diffusion starting at $V_0 > D$, the probability that $V_T$ ends below $D$ in time $T$ is:

    $$
    N(-d_2) = N\left(\frac{-\ln(V_0/D) - (r - \sigma^2/2)T}{\sigma\sqrt{T}}\right)
    $$

    As $T \to 0$, the argument approaches $-\ln(V_0/D)/(\sigma\sqrt{T}) \to -\infty$ (since $\ln(V_0/D) > 0$). The normal CDF at $-\infty$ is zero, and the convergence is super-exponential: $N(-d_2) \sim e^{-a^2/(2\sigma^2 T)}$. The credit spread, which is proportional to $-\frac{1}{T}\ln(1 - (1-R)N(-d_2))$, vanishes as $T \to 0$.

    **First-passage model:** The default event is $\{\min_{0 \le t \le T} V_t \le B\}$, which requires the continuous path to touch the barrier at *some* point. The key property of Brownian motion responsible for positive short-term spreads is the **regularity of the paths**: Brownian paths are continuous but nowhere differentiable, and they oscillate infinitely often in any interval. This means:

    - For any $\varepsilon > 0$, the Brownian path visits levels within $\varepsilon$ of any nearby point in arbitrarily short time intervals.
    - The first-passage time density $f(t) = \frac{a}{\sigma\sqrt{2\pi t^3}} \exp\left(-\frac{(a + \mu t)^2}{2\sigma^2 t}\right)$ is positive for all $t > 0$.

    For the credit spread, the annualized default rate implied by first-passage gives $s(T) > 0$ for all $T > 0$. Specifically, for the credit spread as $T \to 0$:

    $$
    s(T) = -\frac{1}{T}\ln S(0,T) \to s_0
    $$

    where $s_0$ depends on the barrier proximity. For firms close to the barrier ($a$ small), this limit is large and positive.

    The mathematical property responsible is the **recurrence of Brownian motion**: in any neighborhood of the starting point, Brownian motion returns infinitely often, ensuring that nearby barriers are hit with positive probability over any time interval.

---

**Exercise 3.** In the Leland (1994) model, the default barrier is chosen endogenously by equity holders to maximize equity value. Explain why equity holders choose a barrier below the face value of debt. What trade-off between tax benefits of debt and bankruptcy costs determines the optimal barrier?

??? success "Solution to Exercise 3"
    **Leland's endogenous default barrier:**

    In the Leland (1994) model, equity holders have **limited liability** and choose when to default optimally. They continue operating the firm (and paying coupons to debt holders) as long as equity value is positive, and they default when it becomes optimal to stop.

    **Why equity holders choose a barrier below the face value of debt:**

    Equity holders choose to default when the firm's asset value $V$ falls low enough that the cost of continuing (coupon payments) exceeds the expected benefit of the option to recover. Key considerations:

    1. **Limited liability:** Equity holders cannot lose more than their investment. Even when $V < D$, equity has positive value because it is a call option -- there is a chance that $V$ will rise above $D$ before maturity.

    2. **Option value of continuation:** As long as there is a chance of recovering, equity holders prefer to keep the firm alive. The option value of equity is positive whenever $V > 0$, even if $V < D$.

    3. **Coupon burden:** Equity holders must service the debt by paying coupons $C$. When $V$ is very low, the cost of coupon payments (which come from asset value) exceeds the expected benefit from the recovery option.

    4. **The default boundary $B^*$ satisfies the smooth-pasting condition:**

    $$
    \left.\frac{\partial E}{\partial V}\right|_{V = B^*} = 0
    $$

    This condition ensures that equity holders default optimally -- they stop precisely when the marginal value of an extra dollar of assets equals zero for equity holders.

    The resulting optimal barrier is:

    $$
    B^* = \frac{C}{r} \cdot \frac{\alpha_+}{\alpha_+ + 1}
    $$

    where $\alpha_+$ is the positive root of $\frac{1}{2}\sigma^2 \alpha(\alpha - 1) + r\alpha - r = 0$. Since $\alpha_+/(\alpha_+ + 1) < 1$, we have $B^* < C/r$. For typical parameters, $B^*$ is well below the total face value of debt.

    **The trade-off determining the optimal barrier:**

    The optimal capital structure and default boundary balance two forces:

    - **Tax benefits of debt:** Interest payments are tax-deductible, creating a tax shield with present value proportional to debt level. Higher debt increases the tax shield.
    - **Bankruptcy costs:** When the firm defaults, a fraction of asset value is lost to legal fees, fire-sale discounts, and operational disruption. Higher debt (or a higher barrier) increases the expected present value of bankruptcy costs.

    The optimal barrier $B^*$ balances these: equity holders tolerate negative net worth (paying coupons from depleted assets) as long as the tax benefits plus the option value of recovery exceed the expected bankruptcy costs. They trigger default only when this balance tips.

---

**Exercise 4.** A first-passage model with constant barrier $B$ produces a credit spread curve. Describe qualitatively the curve shape for (a) $V_0/B = 3$ (low leverage), (b) $V_0/B = 1.5$ (moderate leverage), and (c) $V_0/B = 1.05$ (near-default). Which case produces a humped curve?

??? success "Solution to Exercise 4"
    **(a) $V_0/B = 3$ (low leverage): Upward-sloping curve.**

    With $V_0/B = 3$, the log-distance $a = \ln 3 = 1.099$ is large. For short maturities, the barrier is far away -- the probability of a Brownian path traveling distance $a \approx 1.1$ in short time is negligible. The default probability is very small, and the annualized spread starts near zero.

    As maturity increases, the diffusion has more time to explore, and the cumulative probability of touching the barrier grows. The spread increases monotonically with $T$. For very long maturities with positive drift $\mu > 0$, the growth rate of the spread may slow or level off, but the curve remains upward-sloping throughout.

    This resembles investment-grade credit curves, where longer-dated bonds carry higher spreads because more things can go wrong over a longer horizon.

    **(b) $V_0/B = 1.5$ (moderate leverage): Hump-shaped curve.**

    With $V_0/B = 1.5$, the log-distance $a = \ln 1.5 = 0.405$ is moderate. This creates a three-phase spread evolution:

    - **Short maturities:** The barrier is close enough that there is meaningful default probability even at short horizons. Spreads start at a modest positive level.
    - **Medium maturities (peak):** Default probability accumulates as more paths reach the barrier. The annualized spread peaks at some intermediate maturity, typically 2--5 years depending on $\sigma$ and $\mu$.
    - **Long maturities:** If $\mu > 0$, the firm's asset value drifts away from the barrier. Conditional on surviving to intermediate dates, the firm is likely in better shape. The additional default probability per unit time decreases, and the annualized spread declines.

    The resulting **hump-shaped** curve is characteristic of BB- to BBB-rated credits. This is the most empirically relevant shape for many corporate issuers.

    **(c) $V_0/B = 1.05$ (near-default): Downward-sloping curve.**

    With $V_0/B = 1.05$, the log-distance $a = \ln 1.05 = 0.0488$ is very small. The firm is teetering at the edge of default:

    - **Short maturities:** The barrier is almost touching the current asset value. Even small fluctuations can trigger default. The annualized spread is extremely high -- possibly hundreds or thousands of basis points.
    - **Medium and long maturities:** If the firm survives the immediate crisis, positive drift ($\mu > 0$) pulls it away from the barrier. The marginal default hazard decreases over time. The annualized spread declines as the horizon extends.

    The resulting **downward-sloping** (inverted) curve is characteristic of distressed or CCC-rated credits. Empirically, distressed firms often have very high short-term spreads that decline with maturity, reflecting the market's view that the main risk is imminent default.

    **Summary:** The hump-shaped curve arises at **moderate** leverage ($V_0/B \approx 1.3$--$1.8$), where neither the short-term barrier proximity nor the long-term drift dominates uniformly.

---

**Exercise 5.** The Longstaff-Schwartz model allows for stochastic interest rates in addition to stochastic firm value. Explain why the correlation between interest rates and firm value affects credit spreads. If rates and firm value are negatively correlated, what happens to credit spreads during a rate increase?

??? success "Solution to Exercise 5"
    **The Longstaff-Schwartz model with correlated stochastic rates:**

    In the Longstaff-Schwartz (1995) model, the interest rate follows:

    $$
    dr_t = \kappa(\theta - r_t)dt + \sigma_r dW_t^r
    $$

    and the firm value process depends on $r_t$:

    $$
    dV_t = (r_t - q)V_t dt + \sigma_V V_t dW_t^V
    $$

    The Brownian motions $W^r$ and $W^V$ have correlation $\rho = \text{Corr}(dW^r, dW^V)$.

    **Why correlation affects credit spreads:**

    The credit spread depends on the joint distribution of interest rates and default events. The defaultable bond price is:

    $$
    P^d(0,T) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_0^T r_s \, ds\right) \cdot D \cdot \mathbf{1}_{\{\tau > T\}}\right] + \text{recovery term}
    $$

    The correlation $\rho$ affects this expectation because the discount factor $\exp(-\int_0^T r_s \, ds)$ and the survival indicator $\mathbf{1}_{\{\tau > T\}}$ are not independent when $\rho \neq 0$.

    Specifically:

    - The bond price involves $\mathbb{E}[\text{discount factor} \times \text{survival}]$, which is not the product $\mathbb{E}[\text{discount factor}] \times \mathbb{E}[\text{survival}]$ when the two are correlated.
    - Using the covariance decomposition: $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] + \text{Cov}(X,Y)$.
    - The sign of $\rho$ determines the sign of this covariance adjustment.

    **Negative correlation ($\rho < 0$): Rate increase $\implies$ wider spreads.**

    When $\rho < 0$, interest rates and firm value move in opposite directions. During a rate increase ($r$ rises):

    1. Firm value tends to **decrease** (negative correlation): $V_t$ falls.
    2. The firm moves **closer to the barrier**: default probability increases.
    3. Meanwhile, the higher rate increases the discount factor's penalty on distant cash flows.
    4. The survival-weighted discount factor is lower than the product of the unconditional expectations.

    The combined effect is:

    - Default is more likely precisely when discount rates are high (bad timing for creditors).
    - The bond price $P^d$ is lower than it would be with $\rho = 0$.
    - Credit spreads are **wider**.

    Intuitively, negative correlation creates a "wrong-way risk" for creditors: rates rise when the firm is weakening, amplifying losses. Conversely, positive correlation ($\rho > 0$) creates a natural hedge: rates rise when the firm strengthens, narrowing spreads.

    This mechanism is empirically relevant because there is evidence of negative correlation between interest rates and default rates in certain sectors (e.g., cyclical industries where rate hikes coincide with economic slowdowns).

---

**Exercise 6.** Compare the first-passage model with the reduced-form intensity model in terms of: (a) mathematical tractability, (b) calibration to CDS spreads, (c) short-maturity spread behavior, and (d) economic interpretability. Under what circumstances would you prefer one framework over the other?

??? success "Solution to Exercise 6"
    **(a) Mathematical tractability.**

    - **First-passage (structural) models:** The Black-Cox model with constant barrier has a closed-form survival probability using the reflection principle. Extensions to time-varying barriers or stochastic rates can be more complex but often retain semi-analytical solutions. However, with jumps or multiple state variables, tractability can decrease significantly.

    - **Reduced-form (intensity) models:** Generally very tractable. The survival probability is $S(0,T) = \mathbb{E}[\exp(-\int_0^T \lambda_s \, ds)]$, which has closed-form solutions for affine intensity models (e.g., CIR intensity). Pricing of CDS, bonds, and derivatives often reduces to computing exponential moments of affine processes. Winner: **reduced-form** for multi-name and exotic credit products.

    **(b) Calibration to CDS spreads.**

    - **First-passage models:** Calibration is indirect. One must specify $(V_0, \sigma_V, B)$ and then derive spreads. The barrier $B$ is unobservable, and the mapping from parameters to spreads is nonlinear. Joint calibration to equity and CDS can be complex, and the model may not fit the full CDS term structure precisely.

    - **Reduced-form models:** Calibration is straightforward. CDS spreads are approximately $s \approx (1 - R)\lambda$, where $\lambda$ is the hazard rate. One can bootstrap a piecewise-constant hazard rate curve directly from CDS quotes at multiple tenors, exactly matching market prices. Winner: **reduced-form** for CDS calibration.

    **(c) Short-maturity spread behavior.**

    - **First-passage models:** Produce positive short-term spreads (as discussed above), which is a significant advantage. The spread behavior near $T = 0$ depends on the firm's distance to the barrier.

    - **Reduced-form models:** Also produce positive short-term spreads, since $\lim_{T \to 0} s(T) = (1 - R)\lambda_0 > 0$ when $\lambda_0 > 0$. The default intensity $\lambda_t$ directly controls the short-term default rate. Result: **both** produce positive short-term spreads, though the mechanisms differ.

    **(d) Economic interpretability.**

    - **First-passage models:** Strong economic content. Default is driven by firm value falling below a barrier that represents insolvency or covenant violation. The model explains *why* default occurs and connects credit to equity through the firm's balance sheet.

    - **Reduced-form models:** Default arrives as an exogenous Poisson event with intensity $\lambda_t$. There is no mechanism explaining *why* default occurs -- it is a statistical description. The intensity may be correlated with economic variables but does not explain the causal link. Winner: **first-passage** for economic intuition.

    **When to prefer each framework:**

    | Use Case | Preferred Approach |
    |----------|-------------------|
    | Pricing vanilla CDS and corporate bonds | Reduced-form (easy calibration) |
    | Single-name credit analysis | Structural (economic insight) |
    | Multi-name portfolio credit risk | Reduced-form (tractable correlation) |
    | Equity-credit relative value | Structural (natural link) |
    | CVA/counterparty risk | Reduced-form (computational ease) |
    | Understanding default drivers | Structural (firm value fundamentals) |
    | Short-dated exotic credit derivatives | Both viable; structural preferred for consistency with equity |

    In practice, many institutions use **hybrid approaches**: structural models to understand economic drivers and generate trading ideas, combined with reduced-form models for pricing and risk management.
