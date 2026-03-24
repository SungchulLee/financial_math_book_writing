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

All three models specify the short rate as a mean-reverting diffusion under the risk-neutral measure $\mathbb{Q}$.

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

$$
B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}
$$

$$
\ln A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\bigl(B(\tau) - \tau\bigr) - \frac{\sigma^2}{4\kappa}\,B(\tau)^2
$$

### CIR

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}, \qquad \gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

$$
A(\tau) = \left(\frac{2\gamma\,e^{(\kappa + \gamma)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)^{2\kappa\theta/\sigma^2}
$$

### Hull-White

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

---

**Exercise 2.** Compute the 10-year zero-coupon bond price under all three models using the numerical example parameters. For Hull-White, assume a flat yield curve $P^M(0,T) = e^{-0.05T}$. Which model gives the highest bond price? Which gives the lowest? Relate the differences to the $B(\tau)$ functions.

---

**Exercise 3.** The Riccati ODE for $B$ is $\dot{B} = -1 + aB + \frac{1}{2}\delta B^2$ with $B(0) = 0$. Show that when $\delta = 0$ (Vasicek/HW), the equation is linear and the solution is $B(\tau) = (1 - e^{-a\tau})/a$. When $\delta = \sigma^2 > 0$ (CIR), explain why the quadratic term causes $B(\tau)$ to saturate at a lower level than $1/a$.

---

**Exercise 4.** All three models admit Jamshidian's decomposition because bond prices are monotone decreasing in $r$. Prove this for each model by computing $\partial P/\partial r$ and showing it is negative. Under what condition on the CIR parameters is this guaranteed?

---

**Exercise 5.** Hull-White fits the initial yield curve exactly while Vasicek and CIR cannot. Suppose the market curve has zero rates $R(0,1) = 3\%$, $R(0,5) = 4\%$, $R(0,10) = 4.5\%$, $R(0,30) = 5\%$. Calibrate a Vasicek model (minimize yield RMSE) and compute the residual errors. Explain structurally why a 3-parameter model cannot perfectly fit 4 or more market points.

---

**Exercise 6.** In the CIR model, the instantaneous volatility of rate changes is $\sigma\sqrt{r_t}$. If $r_t$ doubles from 3% to 6%, by what factor does the volatility increase? Compare this with Vasicek, where the volatility is constant. Which behavior better matches the empirical observation that rate volatility is higher in high-rate environments?

---

**Exercise 7.** A desk must choose between Hull-White and CIR for pricing a 10-year Bermudan swaption with annual exercise dates. List the advantages of each model for this specific product. Consider: (i) curve fit, (ii) rate positivity (the swap is in JPY where rates were near zero), (iii) tree construction complexity, and (iv) calibration to the swaption volatility matrix.
