# Vasicek vs CIR vs Hull-White

The three canonical one-factor short rate models---Vasicek, Cox--Ingersoll--Ross (CIR), and Hull--White---share the common structure of a mean-reverting diffusion for $r(t)$, yet differ fundamentally in their volatility specification, distributional properties, and calibration flexibility. This section provides a comprehensive side-by-side comparison, highlighting the mathematical trade-offs that drive model selection in practice.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the SDE, bond price formula, and key distributional properties for each model
    2. Compare the three models across tractability, rate positivity, volatility structure, and calibration
    3. Identify the strengths and weaknesses of each model for specific pricing tasks
    4. Translate parameter conventions between the three models

---

## Model Dynamics

Recall the short-rate framework (see [§ Short-rate framework](../short_rate_models/general_short_rate_framework.md)). All three models specify the short rate as a mean-reverting diffusion under the risk-neutral measure $\mathbb{Q}$.

!!! info "Definition: Model SDEs"

    **Vasicek:**

    $$
    dr(t) = \kappa\bigl(\theta - r(t)\bigr)\,dt + \sigma\,dW(t)
    $$

    **CIR:**

    $$
    dr(t) = \kappa\bigl(\theta - r(t)\bigr)\,dt + \sigma\sqrt{r(t)}\,dW(t)
    $$

    **Hull-White:**

    $$
    dr(t) = \bigl(\theta(t) - a\,r(t)\bigr)\,dt + \sigma\,dW(t)
    $$

The critical distinctions are the diffusion coefficient (constant $\sigma$ vs $\sigma\sqrt{r}$ vs constant $\sigma$) and the drift specification (constant $\theta$ vs constant $\theta$ vs time-dependent $\theta(t)$).

---

## Comprehensive Comparison Table

| Feature | Vasicek | CIR | Hull-White |
|:---|:---:|:---:|:---:|
| **SDE drift** | $\kappa(\theta - r)$ | $\kappa(\theta - r)$ | $\theta(t) - ar$ |
| **SDE diffusion** | $\sigma$ | $\sigma\sqrt{r}$ | $\sigma$ |
| **Distribution of $r(t)$** | Gaussian | Non-central $\chi^2$ | Gaussian |
| **Negative rates** | Possible | Excluded (Feller) | Possible |
| **Bond price form** | $A(\tau)e^{-B(\tau)r}$ | $A(\tau)e^{-B(\tau)r}$ | $A(t,T)e^{-B(\tau)r}$ |
| **$B(\tau)$ formula** | $\dfrac{1 - e^{-\kappa\tau}}{\kappa}$ | $\dfrac{2(e^{\gamma\tau}-1)}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}$ | $\dfrac{1 - e^{-a\tau}}{a}$ |
| **Bond option formula** | Black-type (Gaussian) | Non-central $\chi^2$ | Black-type (Gaussian) |
| **Exact curve fit** | No | No | Yes |
| **Parameters** | $\kappa, \theta, \sigma$ | $\kappa, \theta, \sigma$ | $a, \sigma, P^M(0,\cdot)$ |
| **Time-dependent drift** | No | No | Yes |
| **Affine class** | $A_0(1)$ | $A_1(1)$ | $A_0(1)$ extended |
| **Exact simulation** | Yes (Gaussian) | Yes (non-central $\chi^2$) | Yes (Gaussian) |
| **Euler discretization** | Standard | Requires truncation | Standard |
| **Volatility structure** | Level-independent | Level-dependent ($\propto\sqrt{r}$) | Level-independent |

---

## Bond Price Formulas

All three models produce exponential-affine bond prices $P(t,T) = A(t,T)\,e^{-B(t,T)\,r(t)}$, but the functions $A$ and $B$ differ.

### Vasicek

Recall (see [§ Vasicek SDE and bond pricing](../vasicek_model/vasicek_sde_and_ou_process.md)).

$$
B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}
$$

$$
\ln A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\bigl(B(\tau) - \tau\bigr) - \frac{\sigma^2}{4\kappa}\,B(\tau)^2
$$

### CIR

Recall (see [§ CIR, Feller, and non-central chi-squared](../cir_model/cir_sde_and_square_root_process.md)).

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}, \qquad \gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

$$
A(\tau) = \left(\frac{2\gamma\,e^{(\kappa + \gamma)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)^{2\kappa\theta/\sigma^2}
$$

### Hull-White

Recall (see [§ Hull-White (full treatment)](../../ch20/index.md)).

$$
B(\tau) = \frac{1 - e^{-a\tau}}{a}
$$

$$
A(t,T) = \frac{P^M(0,T)}{P^M(0,t)}\exp\!\left(B(\tau)\,f^M(0,t) - \frac{\sigma^2}{4a}\,B(\tau)^2\left(1 - e^{-2at}\right)\right)
$$

The key difference is that $A(t,T)$ in Hull-White depends on the calendar times $t$ and $T$ individually (through the market curve $P^M$), not just on $\tau = T - t$.

---

## Distributional Properties

### Short Rate Distribution

!!! info "Proposition: Conditional Distributions"

    **Vasicek:** $r(t) \mid r(s) \sim \mathcal{N}\!\left(\theta + (r(s) - \theta)e^{-\kappa(t-s)},\; \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(t-s)})\right)$

    **CIR:** $r(t) \mid r(s)$ follows a scaled non-central chi-squared distribution with $\nu = \frac{4\kappa\theta}{\sigma^2}$ degrees of freedom and non-centrality $\lambda_{\text{nc}} = \frac{4\kappa\,e^{-\kappa(t-s)}}{\sigma^2(1 - e^{-\kappa(t-s)})}\,r(s)$

    **Hull-White:** $r(t) \mid r(s) \sim \mathcal{N}\!\left(\mu(s,t),\; \frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})\right)$ where $\mu(s,t)$ depends on the market curve

The Gaussian models (Vasicek and Hull-White) share the same variance formula but differ in the conditional mean. CIR has a fundamentally different distribution whose variance is $\text{Var}[r(t) \mid r(s)] = r(s)\frac{\sigma^2}{a}(e^{-\kappa(t-s)} - e^{-2\kappa(t-s)}) + \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa(t-s)})^2$, which depends on the current level $r(s)$.

### Rate Positivity

The Feller condition $2\kappa\theta \ge \sigma^2$ guarantees $r(t) > 0$ in the CIR model. Vasicek and Hull-White have no such guarantee: the Gaussian distribution assigns positive probability to negative rates.

!!! warning "Negative Rate Probability"
    In the Vasicek model with stationary distribution $r_\infty \sim \mathcal{N}(\theta, \sigma^2/(2\kappa))$, the probability of negative rates is

    $$
    \mathbb{P}(r_\infty < 0) = \Phi\!\left(-\theta\sqrt{\frac{2\kappa}{\sigma^2}}\right)
    $$

    For $\kappa = 0.1$, $\theta = 0.05$, $\sigma = 0.02$: $\mathbb{P}(r_\infty < 0) \approx \Phi(-1.58) \approx 5.7\%$.

---

## Volatility Structure

The models differ fundamentally in how rate volatility depends on the rate level.

**Vasicek and Hull-White** have constant instantaneous volatility $\sigma$. The quadratic variation of the short rate is

$$
d\langle r \rangle_t = \sigma^2\,dt
$$

regardless of the level of $r(t)$.

**CIR** has level-dependent volatility $\sigma\sqrt{r(t)}$. The quadratic variation is

$$
d\langle r \rangle_t = \sigma^2\,r(t)\,dt
$$

This produces higher volatility when rates are high and lower volatility when rates are low, matching the empirical observation that rate changes scale with the rate level.

!!! tip "Empirical Evidence"
    Studies of US Treasury rates (Chan, Karolyi, Longstaff, Sanders, 1992) find that the volatility elasticity $\gamma$ in $\sigma(r) = \sigma r^\gamma$ is typically between 0.5 and 1.5. The CIR model ($\gamma = 0.5$) understates level dependence, while constant volatility models ($\gamma = 0$) ignore it entirely.

---

## Analytical Tractability

### Bond Options

All three models admit closed-form bond option prices, but the formulas differ in complexity.

**Vasicek and Hull-White** yield Black-type formulas. For a call on $P(T_1, T_2)$ with strike $K$:

$$
\text{Call} = P(0, T_2)\,N(d_+) - K\,P(0, T_1)\,N(d_-)
$$

where

$$
d_{\pm} = \frac{\ln\!\left(\frac{P(0,T_2)}{K\,P(0,T_1)}\right)}{\sigma_P} \pm \frac{\sigma_P}{2}
$$

and $\sigma_P = \frac{\sigma}{a}(1 - e^{-a(T_2 - T_1)})\sqrt{\frac{1 - e^{-2aT_1}}{2a}}$ is the bond price volatility.

**CIR** bond option formulas involve the non-central chi-squared distribution $\chi^2(\nu, \lambda_{\text{nc}})$, which requires numerical evaluation but remains semi-analytical.

### Jamshidian Decomposition

All three models support Jamshidian's trick for coupon bond options because the bond price $P(t,T) = A(t,T)e^{-B(t,T)r}$ is monotone decreasing in $r$ in each case. This reduces a coupon bond option to a sum of zero-coupon bond options.

---

## Calibration Properties

### Initial Curve Fit

| Model | Curve Fit | Mechanism |
|:---|:---:|:---|
| Vasicek | Approximate | 3 parameters fit by least squares |
| CIR | Approximate | 3 parameters fit by least squares |
| Hull-White | Exact | $\theta(t)$ absorbs the entire curve |

Time-homogeneous models (Vasicek, CIR) with only three constant parameters cannot match an arbitrary market yield curve exactly. The residual calibration error creates a mismatch between model and market bond prices that propagates into derivative prices.

Hull-White eliminates this problem by construction: the function $\theta(t)$ is chosen so that

$$
P^{\text{model}}(0,T) = P^{\text{market}}(0,T) \quad \text{for all } T
$$

### Volatility Calibration

After fitting the initial curve, the remaining parameters ($\kappa$, $\sigma$ for Vasicek/CIR; $a$, $\sigma$ for Hull-White) are calibrated to interest rate option prices (caps, swaptions).

!!! info "Proposition: Parameter Roles"
    In all three models:

    - The **mean reversion speed** ($\kappa$ or $a$) controls the decorrelation between short and long rates, and therefore the term structure of volatility
    - The **volatility parameter** ($\sigma$) scales the overall level of option prices
    - The **long-run mean** ($\theta$) primarily affects the long-end yield level (Vasicek and CIR only)

---

## Riccati ODE Structure

The affine bond price formula arises from substituting $P = e^{A + Br}$ into the bond pricing PDE. The resulting ODE for $B$ is a Riccati equation:

$$
\frac{dB}{d\tau} = -1 + aB + \frac{1}{2}\delta\,B^2
$$

where $\delta = 0$ for Vasicek/Hull-White (Gaussian models) and $\delta = \sigma^2$ for CIR.

!!! info "Proposition: Riccati Classification"

    **Vasicek/Hull-White** ($\delta = 0$): The Riccati equation degenerates to a linear ODE with the exponential solution $B(\tau) = (1 - e^{-a\tau})/a$.

    **CIR** ($\delta = \sigma^2 > 0$): The full quadratic Riccati equation has the solution involving $\gamma = \sqrt{a^2 + 2\sigma^2}$, producing a qualitatively different $B(\tau)$ that grows more slowly and remains bounded by $2/(\gamma + a)$.

The Riccati structure places all three models within the Dai-Singleton $A_m(1)$ classification: Vasicek and Hull-White are $A_0(1)$ (no square-root factors), while CIR is $A_1(1)$ (one square-root factor).

---

## Numerical Example

Consider models calibrated to produce similar short-term behavior with $r(0) = 0.05$, mean reversion speed $\kappa = a = 0.1$, and short-rate volatility approximately 1%:

- **Vasicek:** $\kappa = 0.1$, $\theta = 0.05$, $\sigma = 0.01$
- **CIR:** $\kappa = 0.1$, $\theta = 0.05$, $\sigma = 0.0447$ (so that $\sigma\sqrt{r(0)} \approx 0.01$)
- **Hull-White:** $a = 0.1$, $\sigma = 0.01$, $P^M(0,T) = e^{-0.05T}$

The 10-year bond prices under each model are:

$$
B(10) = \frac{1 - e^{-0.1 \times 10}}{0.1} \approx 6.321 \quad \text{(Vasicek and Hull-White)}
$$

For CIR, $\gamma = \sqrt{0.01 + 2 \times 0.002} \approx 0.1183$ and

$$
B_{\text{CIR}}(10) = \frac{2(e^{1.183} - 1)}{(0.2183)(e^{1.183} - 1) + 2(0.1183)} \approx 5.89
$$

The CIR $B$-function is smaller because the quadratic Riccati term dampens the growth relative to the linear case. This translates into a lower bond price sensitivity to rate changes in the CIR model.

---

## Strengths and Weaknesses Summary

### Vasicek

**Strengths:**

- Simplest analytical formulas; ideal for pedagogy and rapid prototyping
- Gaussian distribution enables straightforward Monte Carlo simulation
- Closed-form bond options, caps, and swaptions

**Weaknesses:**

- Cannot fit the initial yield curve exactly
- Permits negative interest rates
- Level-independent volatility is empirically unrealistic

### CIR

**Strengths:**

- Rate positivity guaranteed under the Feller condition
- Level-dependent volatility matches empirical observations
- Semi-analytical bond option pricing

**Weaknesses:**

- Cannot fit the initial yield curve exactly
- Non-central chi-squared distribution is more complex to implement
- Euler discretization requires care (truncation or reflection at zero)
- Feller condition constrains the parameter space

### Hull-White

**Strengths:**

- Exact fit to the initial yield curve by construction
- Closed-form bond options, caps, and swaptions (same complexity as Vasicek)
- Standard production model for vanilla interest rate derivatives
- Efficient tree and Monte Carlo implementations

**Weaknesses:**

- Permits negative interest rates (same as Vasicek)
- Level-independent volatility
- Time-dependent $\theta(t)$ makes the model non-stationary
- Two free parameters ($a$, $\sigma$) may not capture the full volatility surface

---

## Summary

The Vasicek, CIR, and Hull-White models form a natural progression in short rate modeling. Vasicek provides the foundational mean-reverting Gaussian framework with full analytical tractability but cannot fit the market curve. CIR introduces level-dependent volatility and rate positivity at the cost of more complex analytics. Hull-White extends Vasicek with a time-dependent drift that exactly matches the initial term structure, making it the standard choice for production derivative pricing. The choice among the three depends on the application: Vasicek for pedagogy, CIR when rate positivity and realistic volatility matter, and Hull-White when exact curve calibration and closed-form option pricing are required.

---

## Exercises

**Exercise 1.** For the numerical example parameters ($r(0) = 0.05$, $\kappa = 0.1$, $\theta = 0.05$, $\sigma_{\text{Vas}} = 0.01$, $\sigma_{\text{CIR}} = 0.0447$), compute $B^{\text{Vas}}(10)$ and $B^{\text{CIR}}(10)$. Verify that $B^{\text{CIR}} < B^{\text{Vas}}$ and explain the economic reason for this difference.

??? success "Solution to Exercise 1"
    Using the given parameters $r(0) = 0.05$, $\kappa = 0.1$, $\sigma_{\text{Vas}} = 0.01$, $\sigma_{\text{CIR}} = 0.0447$:

    **Vasicek $B$-function:**

    $$
    B^{\text{Vas}}(10) = \frac{1 - e^{-\kappa \cdot 10}}{\kappa} = \frac{1 - e^{-1}}{0.1} = \frac{1 - 0.3679}{0.1} = \frac{0.6321}{0.1} = 6.321
    $$

    **CIR $B$-function:** First compute $\gamma$:

    $$
    \gamma = \sqrt{\kappa^2 + 2\sigma_{\text{CIR}}^2} = \sqrt{0.01 + 2(0.0447)^2} = \sqrt{0.01 + 0.003996} = \sqrt{0.013996} \approx 0.1183
    $$

    Then:

    $$
    B^{\text{CIR}}(10) = \frac{2(e^{\gamma \cdot 10} - 1)}{(\gamma + \kappa)(e^{\gamma \cdot 10} - 1) + 2\gamma}
    $$

    With $e^{1.183} \approx 3.263$:

    $$
    B^{\text{CIR}}(10) = \frac{2(3.263 - 1)}{(0.2183)(3.263 - 1) + 2(0.1183)} = \frac{2(2.263)}{(0.2183)(2.263) + 0.2366} = \frac{4.526}{0.4940 + 0.2366} = \frac{4.526}{0.7306} \approx 6.194
    $$

    Verification: $B^{\text{CIR}}(10) \approx 6.194 < 6.321 = B^{\text{Vas}}(10)$. Confirmed.

    **Economic reason:** In the CIR model, the Riccati ODE for $B$ is $\dot{B} = -1 + \kappa B + \frac{1}{2}\sigma^2 B^2$, where the quadratic term $\frac{1}{2}\sigma^2 B^2 > 0$ acts as an additional positive force that slows the growth of $B$. The CIR $B$-function saturates at the finite limit $B(\infty) = 2/(\gamma + \kappa)$, which is strictly less than $1/\kappa$ (the Vasicek limit). Economically, the level-dependent volatility $\sigma\sqrt{r}$ in CIR creates a convexity effect: higher rates produce higher volatility, which generates a "convexity premium" that reduces the bond's sensitivity to the short rate. This is why CIR bond prices are less sensitive to rate changes (lower $B$) than Vasicek bond prices.

---

**Exercise 2.** Compute the 10-year zero-coupon bond price under all three models using the numerical example parameters. For Hull-White, assume a flat yield curve $P^M(0,T) = e^{-0.05T}$. Which model gives the highest bond price? Which gives the lowest? Relate the differences to the $B(\tau)$ functions.

??? success "Solution to Exercise 2"
    The bond price formula is $P(0,T) = A(\tau)\,e^{-B(\tau)\,r(0)}$ with $\tau = T = 10$ and $r(0) = 0.05$.

    **Vasicek:** Using $B(10) = 6.321$ and

    $$
    \ln A(10) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(10) - 10) - \frac{\sigma^2}{4\kappa}B(10)^2
    $$

    $$
    = \left(0.05 - \frac{0.0001}{0.02}\right)(6.321 - 10) - \frac{0.0001}{0.4}(6.321)^2
    $$

    $$
    = (0.05 - 0.005)(-3.679) - 0.00025(39.955)
    $$

    $$
    = 0.045 \times (-3.679) - 0.009989 = -0.16556 - 0.009989 = -0.17554
    $$

    So $A(10) = e^{-0.17554} \approx 0.8391$ and

    $$
    P^{\text{Vas}}(0,10) = 0.8391 \times e^{-6.321 \times 0.05} = 0.8391 \times e^{-0.3161} = 0.8391 \times 0.7290 \approx 0.6117
    $$

    **Hull-White:** With a flat yield curve $P^M(0,T) = e^{-0.05T}$, the Hull-White model is calibrated so that $\theta(t) = ab + \frac{\sigma^2}{2a^2}(1 - e^{-2at})$ reproduces the flat curve exactly. By construction:

    $$
    P^{\text{HW}}(0,10) = P^M(0,10) = e^{-0.05 \times 10} = e^{-0.5} \approx 0.6065
    $$

    **CIR:** Using $B^{\text{CIR}}(10) \approx 6.194$ and the CIR $A$-function:

    $$
    A(10) = \left(\frac{2\gamma\,e^{(\kappa+\gamma)\cdot 10/2}}{(\gamma+\kappa)(e^{\gamma\cdot 10}-1)+2\gamma}\right)^{2\kappa\theta/\sigma^2}
    $$

    The exponent is $2\kappa\theta/\sigma^2 = 2(0.1)(0.05)/(0.0447)^2 = 0.01/0.001998 \approx 5.005$. With $e^{(\kappa+\gamma)\cdot 5} = e^{0.2183\cdot 5} = e^{1.0915} \approx 2.979$:

    $$
    A(10) = \left(\frac{2(0.1183)(2.979)}{0.7306}\right)^{5.005} = \left(\frac{0.7048}{0.7306}\right)^{5.005} = (0.9647)^{5.005} \approx 0.8353
    $$

    $$
    P^{\text{CIR}}(0,10) = 0.8353 \times e^{-6.194 \times 0.05} = 0.8353 \times e^{-0.3097} = 0.8353 \times 0.7337 \approx 0.6129
    $$

    **Ranking:** $P^{\text{CIR}}(0,10) \approx 0.6129 > P^{\text{Vas}}(0,10) \approx 0.6117 > P^{\text{HW}}(0,10) \approx 0.6065$ (note: the exact ordering of Vasicek and CIR depends sensitively on the $A$-function values; the key structural point is below).

    **Relation to $B(\tau)$:** Since $P = Ae^{-Br}$, a smaller $B$ (as in CIR) means lower sensitivity to the short rate, and the exponential factor $e^{-Br}$ is larger. The $A$-function also differs, but the dominant effect is through $B$: the CIR model's lower $B$ function produces a higher bond price for the same short rate, reflecting the convexity adjustment from level-dependent volatility. Hull-White gives the lowest price because it is calibrated exactly to the flat market curve $e^{-0.05T}$, which is the no-arbitrage reference.

---

**Exercise 3.** The Riccati ODE for $B$ is $\dot{B} = -1 + aB + \frac{1}{2}\delta B^2$ with $B(0) = 0$. Show that when $\delta = 0$ (Vasicek/HW), the equation is linear and the solution is $B(\tau) = (1 - e^{-a\tau})/a$. When $\delta = \sigma^2 > 0$ (CIR), explain why the quadratic term causes $B(\tau)$ to saturate at a lower level than $1/a$.

??? success "Solution to Exercise 3"
    **Case $\delta = 0$ (Vasicek/Hull-White):** The Riccati ODE becomes

    $$
    \dot{B} = -1 + aB, \qquad B(0) = 0
    $$

    This is a first-order linear ODE. The homogeneous solution is $Ce^{a\tau}$, and a particular solution is $B = 1/a$. The general solution is $B(\tau) = 1/a + Ce^{a\tau}$. Applying $B(0) = 0$: $0 = 1/a + C$, so $C = -1/a$. Therefore

    $$
    B(\tau) = \frac{1}{a}(1 - e^{a\tau})
    $$

    Wait -- this gives a growing solution. The sign convention matters. The standard form uses $\dot{B} = -1 + aB$ where $a > 0$, and the boundary condition $B(0) = 0$ with $\tau = T - t$ increasing. Writing the ODE as $dB/d\tau = -1 + aB$:

    $$
    B(\tau) = \frac{1}{a} + Ce^{a\tau}, \quad B(0) = 0 \implies C = -\frac{1}{a}
    $$

    This yields $B(\tau) = (1 - e^{a\tau})/a$, which is negative and growing in magnitude. The issue is the sign convention in the bond price: using $P = e^{A - Br}$ (with a minus sign), the Riccati ODE is $\dot{B} = 1 - aB$, giving

    $$
    B(\tau) = \frac{1 - e^{-a\tau}}{a}
    $$

    which is the standard result. This is verified by direct substitution: $\dot{B} = e^{-a\tau}$ and $1 - aB = 1 - (1 - e^{-a\tau}) = e^{-a\tau}$. As $\tau \to \infty$, $B(\tau) \to 1/a$.

    **Case $\delta = \sigma^2 > 0$ (CIR):** The Riccati ODE (in the convention $P = e^{A - Br}$) becomes

    $$
    \dot{B} = 1 - aB - \tfrac{1}{2}\sigma^2 B^2, \qquad B(0) = 0
    $$

    The quadratic term $-\frac{1}{2}\sigma^2 B^2$ is always non-positive, providing an additional damping force that opposes the growth of $B$. As $B$ increases, this term becomes more significant, causing $B(\tau)$ to grow more slowly than in the linear case.

    The steady-state value is found by setting $\dot{B} = 0$:

    $$
    \tfrac{1}{2}\sigma^2 B_\infty^2 + aB_\infty - 1 = 0 \implies B_\infty = \frac{-a + \sqrt{a^2 + 2\sigma^2}}{\sigma^2} = \frac{2}{\gamma + a}
    $$

    where $\gamma = \sqrt{a^2 + 2\sigma^2}$. Since $\gamma > a$, we have

    $$
    B_\infty^{\text{CIR}} = \frac{2}{\gamma + a} < \frac{1}{a} = B_\infty^{\text{Vas}}
    $$

    The inequality is strict because $\gamma + a > 2a$ (since $\gamma > a$). The CIR $B$-function saturates at a lower level because the quadratic term in the Riccati equation creates additional resistance to growth that is absent in the linear (Vasicek) case. Economically, this reflects the convexity effect of level-dependent volatility.

---

**Exercise 4.** All three models admit Jamshidian's decomposition because bond prices are monotone decreasing in $r$. Prove this for each model by computing $\partial P/\partial r$ and showing it is negative. Under what condition on the CIR parameters is this guaranteed?

??? success "Solution to Exercise 4"
    The bond price in all three models has the form $P(t,T) = A(t,T)\,e^{-B(t,T)\,r(t)}$ where $A(t,T) > 0$ and $B(t,T) > 0$ for $T > t$. Taking the partial derivative with respect to $r$:

    $$
    \frac{\partial P}{\partial r} = -B(t,T)\,A(t,T)\,e^{-B(t,T)\,r(t)} = -B(t,T)\,P(t,T)
    $$

    Since $P(t,T) > 0$ (bond prices are positive) and $B(t,T) > 0$ (for $T > t$), we have

    $$
    \frac{\partial P}{\partial r} = -B(t,T)\,P(t,T) < 0
    $$

    This confirms that bond prices are strictly monotone decreasing in $r$ for all three models.

    **Verification that $B(t,T) > 0$:**

    - **Vasicek and Hull-White:** $B(\tau) = (1 - e^{-a\tau})/a$. For $\tau > 0$ and $a > 0$: $e^{-a\tau} < 1$, so $1 - e^{-a\tau} > 0$, giving $B(\tau) > 0$.
    - **CIR:** $B(\tau) = 2(e^{\gamma\tau} - 1)/[(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma]$. For $\tau > 0$: $e^{\gamma\tau} > 1$, so the numerator is positive. The denominator equals $(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma > 0$ since all terms are positive. Hence $B(\tau) > 0$.

    **Condition on CIR parameters:** The monotonicity $\partial P/\partial r < 0$ holds for all positive $\kappa$, $\theta$, $\sigma$ and all $\tau > 0$ -- there is no additional parameter restriction beyond the standard requirement that the model parameters are positive. In particular, the Feller condition $2\kappa\theta \ge \sigma^2$ is not required for monotonicity; it is required only for strict positivity of the rate process. The $B$-function depends only on $\kappa$, $\sigma$, and $\tau$, not on $\theta$, so the monotonicity is guaranteed regardless of whether the Feller condition holds.

    Jamshidian's decomposition exploits this monotonicity: since each $P(t, T_i)$ is decreasing in $r$, there exists a unique $r^*$ such that the coupon bond price equals the strike. The coupon bond option then decomposes into a sum of zero-coupon bond options with adjusted strikes $K_i = P(r^*, t, T_i)$.

---

**Exercise 5.** Hull-White fits the initial yield curve exactly while Vasicek and CIR cannot. Suppose the market curve has zero rates $R(0,1) = 3\%$, $R(0,5) = 4\%$, $R(0,10) = 4.5\%$, $R(0,30) = 5\%$. Calibrate a Vasicek model (minimize yield RMSE) and compute the residual errors. Explain structurally why a 3-parameter model cannot perfectly fit 4 or more market points.

??? success "Solution to Exercise 5"
    The Vasicek model yield is $R(0,T) = -\ln P(0,T)/T = -[A(T) - B(T)r(0)]/T$, with three parameters $(\kappa, \theta, \sigma)$. We need to minimize

    $$
    \text{RMSE} = \sqrt{\frac{1}{4}\sum_{i=1}^4 \bigl(R^{\text{model}}(0,T_i) - R^{\text{mkt}}(0,T_i)\bigr)^2}
    $$

    over $(\kappa, \theta, \sigma)$ with market rates $R^{\text{mkt}}(0,1) = 3\%$, $R^{\text{mkt}}(0,5) = 4\%$, $R^{\text{mkt}}(0,10) = 4.5\%$, $R^{\text{mkt}}(0,30) = 5\%$.

    **Structural limitation:** The Vasicek yield curve has the asymptotic form

    $$
    R(0,T) = R_\infty - (R_\infty - r(0))\frac{B(T)}{T} + \frac{\sigma^2 B(T)^2}{4\kappa T}
    $$

    where $R_\infty = \theta - \sigma^2/(2\kappa^2)$ is the limiting long yield as $T \to \infty$. The curve shape is determined by three quantities: the short rate $r(0)$, the long rate $R_\infty$, and the curvature controlled by $\kappa$. With 3 free parameters, the model generates a 3-dimensional family of yield curves. The observed curve has 4 independent data points, which generically define a 4-dimensional target. By dimension counting, the 3-parameter Vasicek model cannot exactly interpolate 4 or more market points.

    More precisely, the Vasicek yield curve is concave in $T$ (for typical parameters) and monotonically approaches $R_\infty$ from below. It cannot reproduce yield curves with inflection points, humps, or other shapes that require more than 3 degrees of freedom. The residual errors reflect the mismatch between the parametric yield curve family and the market curve shape.

    For a concrete calibration: setting $\theta \approx 0.052$, $\kappa \approx 0.08$, $\sigma \approx 0.015$, and $r(0) = 0.03$, the model can approximate the general upward slope but will produce residual errors of order 5--20 bps at individual maturities, with the largest errors typically at intermediate tenors where the Vasicek curve shape is most constrained.

---

**Exercise 6.** In the CIR model, the instantaneous volatility of rate changes is $\sigma\sqrt{r_t}$. If $r_t$ doubles from 3% to 6%, by what factor does the volatility increase? Compare this with Vasicek, where the volatility is constant. Which behavior better matches the empirical observation that rate volatility is higher in high-rate environments?

??? success "Solution to Exercise 6"
    In the CIR model, the instantaneous volatility of rate changes is $\sigma\sqrt{r_t}$.

    If $r_t$ doubles from 3% to 6%:

    $$
    \frac{\sigma\sqrt{0.06}}{\sigma\sqrt{0.03}} = \sqrt{\frac{0.06}{0.03}} = \sqrt{2} \approx 1.414
    $$

    The volatility increases by a factor of $\sqrt{2} \approx 41.4\%$.

    In the Vasicek model, the volatility is constant $\sigma$ regardless of the rate level. Doubling the rate from 3% to 6% produces zero change in volatility.

    **Empirical comparison:** The observation that rate volatility is higher in high-rate environments is well-documented. Chan, Karolyi, Longstaff, and Sanders (1992) estimate the volatility elasticity $\gamma$ in $\sigma(r) = \sigma_0 r^\gamma$ and find $\gamma$ typically between 0.5 and 1.5 for US Treasury rates. The CIR model corresponds to $\gamma = 0.5$, which captures the direction of the level dependence (higher rates $\Rightarrow$ higher volatility) but likely understates its magnitude. The Vasicek model corresponds to $\gamma = 0$, which ignores level dependence entirely and is empirically unrealistic.

    The CIR behavior better matches empirical observations, particularly in environments where rates move through a wide range. The $\sqrt{r}$ specification is a compromise: it captures the qualitative feature of level-dependent volatility while maintaining the affine structure and analytical tractability.

---

**Exercise 7.** A desk must choose between Hull-White and CIR for pricing a 10-year Bermudan swaption with annual exercise dates. List the advantages of each model for this specific product. Consider: (i) curve fit, (ii) rate positivity (the swap is in JPY where rates were near zero), (iii) tree construction complexity, and (iv) calibration to the swaption volatility matrix.

??? success "Solution to Exercise 7"
    **Hull-White advantages for 10Y Bermudan swaption:**

    **(i) Curve fit:** Hull-White fits the initial JPY yield curve exactly via $\theta(t)$, ensuring that all discount factors and forward rates match market quotes. This is critical for a Bermudan swaption because the exercise decision depends on the swap value at each exercise date, which in turn depends on the entire forward curve. CIR (time-homogeneous) cannot fit the JPY curve exactly, introducing calibration error into every exercise boundary.

    **(iii) Tree construction:** The Hull-White trinomial tree is straightforward to build: the rate is Gaussian, the tree is recombining, and bond prices at each node are available in closed form via $P(t_i, T) = A(t_i, T)e^{-B(t_i, T)r_{ij}}$. This means the swap value at each exercise node is computed analytically. The CIR tree is more complex: the $\sqrt{r}$ diffusion produces a non-uniform node spacing near zero, and care must be taken to ensure non-negative transition probabilities.

    **(iv) Swaption calibration:** Hull-White has closed-form European swaption prices via Jamshidian's decomposition, enabling fast calibration to the swaption volatility matrix. The Bermudan swaption price is bounded below by the most valuable European swaption, and calibration to the co-terminal swaption set is standard. CIR swaption pricing requires numerical integration over the non-central chi-squared distribution, making calibration slower.

    **CIR advantages for 10Y Bermudan swaption:**

    **(ii) Rate positivity:** This is the most important consideration for JPY, where rates were near zero (and sometimes negative). CIR with the Feller condition guarantees $r_t > 0$, preventing the model from generating negative rates. For a Bermudan swaption, negative rates affect the exercise decision: if the model generates deeply negative rates, the swap value may be distorted, leading to incorrect early exercise boundaries.

    However, the Feller condition $2\kappa\theta \ge \sigma^2$ constrains the parameter space. If JPY rates are near zero (say $\theta \approx 0.001$), maintaining the Feller condition requires very small $\sigma$, which may be inconsistent with observed swaption volatilities.

    **Recommendation:** For JPY near-zero rates, **Hull-White is preferred** despite the negative rate issue, for three reasons: (a) exact curve fit is essential for Bermudan exercise decisions, (b) the closed-form swaption prices enable reliable calibration to the co-terminal swaption set, and (c) the negative rate probability can be managed by using a shifted Hull-White model ($r_t + \delta$ follows Hull-White with $\delta$ chosen to keep rates non-negative in typical scenarios). The CIR model's rate positivity advantage is offset by its inability to fit the yield curve and the Feller condition's constraint on calibration flexibility in a near-zero rate environment.
