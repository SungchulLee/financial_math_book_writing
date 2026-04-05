# Model Definition

The Heston model is one of the most widely used **stochastic volatility models** in equity, FX, and commodity markets. It extends Black–Scholes by modeling variance as a mean-reverting stochastic process while retaining analytical tractability through its affine structure. This section provides a complete specification of the model and its properties.

---

## Dynamics Under the Risk-Neutral Measure

### The Heston SDE System

Under the risk-neutral measure $\mathbb{Q}$, the Heston model is defined by:

$$
\begin{aligned}
dS_t &= (r - q)S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S \\
dV_t &= \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V \\
d\langle W^S, W^V \rangle_t &= \rho\,dt
\end{aligned}
$$

where:

| Parameter | Symbol | Typical Range | Interpretation |
|-----------|--------|---------------|----------------|
| Asset price | $S_t$ | — | Current price level |
| Instantaneous variance | $V_t$ | — | Current volatility squared |
| Risk-free rate | $r$ | 0–5% | Continuously compounded |
| Dividend yield | $q$ | 0–3% | Continuously compounded |
| Mean-reversion speed | $\kappa$ | 0.5–5 | Rate of return to $\theta$ |
| Long-run variance | $\theta$ | 0.02–0.10 | Stationary variance level |
| Volatility of volatility | $\xi$ | 0.2–1.0 | Vol-of-vol parameter |
| Correlation | $\rho$ | $-0.9$ to $0$ | Price-variance correlation |
| Initial variance | $V_0$ | 0.01–0.10 | Spot variance |

### Log-Price Dynamics

For pricing, it is often convenient to work with $X_t = \log S_t$:

$$
dX_t = \left(r - q - \frac{1}{2}V_t\right)dt + \sqrt{V_t}\,dW_t^S
$$

The pair $(X_t, V_t)$ is a **two-dimensional affine diffusion**.

---

## Interpretation of Parameters

### Mean Reversion Speed (κ)

The parameter $\kappa > 0$ controls how quickly variance returns to its long-run level:

- **Half-life of shocks:** $t_{1/2} = \frac{\ln 2}{\kappa}$
- $\kappa = 1$: half-life of 8.3 months
- $\kappa = 3$: half-life of 2.8 months
- $\kappa = 5$: half-life of 1.7 months

**Calibration insight:** $\kappa$ primarily affects the **term structure** of implied volatility. Higher $\kappa$ flattens the term structure faster.

### Long-Run Variance (θ)

The parameter $\theta > 0$ is the **stationary mean** of the variance process:

$$
\lim_{t \to \infty} \mathbb{E}[V_t] = \theta
$$

**Calibration insight:** $\theta$ controls the level of long-maturity implied volatility:

$$
\sigma_{\text{impl}}^2(T \to \infty) \approx \theta
$$

### Volatility of Volatility (ξ)

The parameter $\xi > 0$ controls the magnitude of variance fluctuations:

- Higher $\xi$ → more volatile volatility → more pronounced smile **curvature**
- $\xi$ affects both wings of the smile (not just skew)

**Calibration insight:** $\xi$ is identifiable from the **convexity** of the smile:

$$
\frac{\partial^2 \sigma_{\text{impl}}}{\partial k^2} \propto \xi^2
$$

### Correlation (ρ)

The parameter $\rho \in (-1, 1)$ controls the correlation between price and variance shocks:

- $\rho < 0$: leverage effect (typical for equities)
- $\rho = 0$: symmetric smile
- $\rho > 0$: inverse leverage (rare)

**Calibration insight:** $\rho$ directly controls the **skew**:

$$
\frac{\partial \sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \propto \rho
$$

### Initial Variance (V_0)

The parameter $V_0 > 0$ is the **current** instantaneous variance:

- Primarily affects short-maturity options
- Often set from ATM implied volatility: $V_0 \approx \sigma_{\text{ATM}}^2$

---

## Stationary Distribution

When $V_t$ reaches its stationary distribution (for $t$ large):

$$
V_{\infty} \sim \text{Gamma}\left(\frac{2\kappa\theta}{\xi^2}, \frac{2\kappa}{\xi^2}\right)
$$

**Stationary moments:**

$$
\begin{aligned}
\mathbb{E}[V_{\infty}] &= \theta \\
\text{Var}[V_{\infty}] &= \frac{\xi^2 \theta}{2\kappa} \\
\text{Skew}[V_{\infty}] &= \frac{2\xi}{\sqrt{2\kappa\theta}}
\end{aligned}
$$

The variance distribution is always right-skewed and bounded below by zero.

---

## Relation to Black–Scholes

### Deterministic Limit

If volatility is deterministic ($\xi = 0$), the variance satisfies:

$$
V_t = V_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})
$$

The model reduces to **time-dependent Black–Scholes**:

$$
C = C^{\text{BS}}\left(S_0, K, T, \bar{\sigma}(T)\right)
$$

where $\bar{\sigma}^2(T) = \frac{1}{T}\int_0^T V_s\,ds$.

### Small Vol-of-Vol Expansion

For small $\xi$, Heston prices can be expanded:

$$
C^{\text{Heston}} = C^{\text{BS}} + \xi \cdot C_1 + \xi^2 \cdot C_2 + O(\xi^3)
$$

The correction terms introduce smile and skew.

### Implied Volatility Approximation

For short maturities and near-ATM options:

$$
\sigma_{\text{impl}}(k, T) \approx \sqrt{V_0} + \frac{\rho\xi}{4\sqrt{V_0}}k + \frac{\xi^2(1-\rho^2)}{8V_0^{3/2}}k^2 + O(T, k^3)
$$

This shows:
- ATM level: $\sqrt{V_0}$
- Skew: $\propto \rho\xi$
- Convexity: $\propto \xi^2$

---

## Parameter Constraints

### Positivity of Variance

For $V_t \geq 0$ to hold, we need $\kappa, \theta, \xi > 0$.

### Feller Condition

The **Feller condition** ensures $V_t > 0$ (strictly positive):

$$
2\kappa\theta \geq \xi^2
$$

See Section 9.3.2 for detailed boundary behavior.

### Existence of Moments

The $n$-th moment of $S_T$ exists under $\mathbb{Q}$ if and only if $n < n^*$ where $n^*$ depends on $(\kappa, \theta, \xi, \rho)$.

**Andersen–Piterbarg condition:** Moments may explode for large $n$, affecting certain exotic pricing.

---

## Simulation of Heston Paths

### Euler Scheme (with Truncation)

The simplest scheme (with variance floor):

$$
\begin{aligned}
V_{t+\Delta} &= V_t + \kappa(\theta - V_t^+)\Delta + \xi\sqrt{V_t^+}\sqrt{\Delta}\,Z_1 \\
S_{t+\Delta} &= S_t \exp\left[\left(r - q - \frac{1}{2}V_t^+\right)\Delta + \sqrt{V_t^+}\sqrt{\Delta}\,Z_2\right]
\end{aligned}
$$

where $V_t^+ = \max(V_t, 0)$ and $(Z_1, Z_2)$ are correlated normals.

### QE Scheme (Andersen)

The **Quadratic-Exponential** scheme is more accurate:
1. Match moments of the non-central $\chi^2$ transition density
2. Use quadratic approximation for small $V$, exponential for large $V$

See Section 9.4 for implementation details.

### Exact Simulation

The variance transition $V_{t+\Delta} | V_t$ follows a scaled non-central $\chi^2$:

$$
V_{t+\Delta} = \frac{\xi^2(1-e^{-\kappa\Delta})}{4\kappa}\chi'^2\left(\frac{4\kappa\theta}{\xi^2}, \frac{4\kappa e^{-\kappa\Delta}}{\xi^2(1-e^{-\kappa\Delta})}V_t\right)
$$

Exact simulation is possible but computationally expensive.

---

## Model Summary

| Property | Heston | Black–Scholes |
|----------|--------|---------------|
| Volatility | Stochastic | Constant |
| # Parameters | 5 ($\kappa, \theta, \xi, \rho, V_0$) | 1 ($\sigma$) |
| Smile | Yes (endogenous) | No |
| Skew | Yes (from $\rho$) | No |
| Term structure | Yes (from $\kappa, \theta$) | Flat |
| Closed-form European | Yes (semi-analytic) | Yes (analytic) |
| Market completeness | No | Yes |
| Computational cost | Moderate | Low |

---

## Key Takeaways

- Heston introduces stochastic variance with mean reversion
- Five risk-neutral parameters: $\kappa, \theta, \xi, \rho, V_0$
- Captures skew ($\rho$), smile curvature ($\xi$), and term structure ($\kappa, \theta$)
- Analytical tractability via affine structure and characteristic functions
- The Feller condition $2\kappa\theta \geq \xi^2$ ensures strict positivity
- Heston is the minimal extension of Black–Scholes that generates realistic smiles

---

## Further Reading

- Heston, S. (1993). *A closed-form solution for options with stochastic volatility with applications to bond and currency options*. Review of Financial Studies.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.
- Andersen, L. (2008). *Efficient simulation of the Heston stochastic volatility model*. Journal of Computational Finance.
- Lord, R., Koekkoek, R., & van Dijk, D. (2010). *A comparison of biased simulation schemes for stochastic volatility models*. Quantitative Finance.

---

## Exercises

**Exercise 1.** Given the Heston parameters $\kappa = 2.5$, $\theta = 0.04$, $\xi = 0.6$, $\rho = -0.7$, and $V_0 = 0.06$, compute: (a) the half-life of variance shocks $t_{1/2} = \ln 2 / \kappa$; (b) the Feller ratio $\nu = 2\kappa\theta/\xi^2$ and whether the Feller condition is satisfied; (c) the stationary variance $\text{Var}[V_\infty] = \xi^2\theta/(2\kappa)$; and (d) the expected path of $V_t$ in the deterministic limit ($\xi = 0$) at $t = 0.5$ and $t = 2.0$.

??? success "Solution to Exercise 1"
    We are given $\kappa = 2.5$, $\theta = 0.04$, $\xi = 0.6$, $\rho = -0.7$, $V_0 = 0.06$.

    **(a)** Half-life of variance shocks:

    $$
    t_{1/2} = \frac{\ln 2}{\kappa} = \frac{0.6931}{2.5} = 0.2773 \text{ years} \approx 3.3 \text{ months}
    $$

    **(b)** Feller ratio:

    $$
    \nu = \frac{2\kappa\theta}{\xi^2} = \frac{2 \times 2.5 \times 0.04}{0.36} = \frac{0.20}{0.36} = 0.5556
    $$

    Since $\nu < 1$, the Feller condition is **not satisfied**. The variance process can reach zero.

    **(c)** Stationary variance:

    $$
    \text{Var}[V_\infty] = \frac{\xi^2\theta}{2\kappa} = \frac{0.36 \times 0.04}{2 \times 2.5} = \frac{0.0144}{5} = 0.00288
    $$

    The stationary standard deviation is $\sqrt{0.00288} \approx 0.0537$.

    **(d)** In the deterministic limit ($\xi = 0$), the variance follows $V_t = V_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})$.

    At $t = 0.5$:

    $$
    V_{0.5} = 0.06 \, e^{-2.5 \times 0.5} + 0.04(1 - e^{-1.25}) = 0.06 \times 0.2865 + 0.04 \times 0.7135 = 0.01719 + 0.02854 = 0.04573
    $$

    At $t = 2.0$:

    $$
    V_{2.0} = 0.06 \, e^{-5.0} + 0.04(1 - e^{-5.0}) = 0.06 \times 0.00674 + 0.04 \times 0.99326 = 0.00040 + 0.03973 = 0.04013
    $$

    As $t$ grows, $V_t \to \theta = 0.04$, consistent with the mean-reverting dynamics.

---

**Exercise 2.** Using the short-maturity implied volatility approximation

$$
\sigma_{\text{impl}}(k, T) \approx \sqrt{V_0} + \frac{\rho\xi}{4\sqrt{V_0}}k + \frac{\xi^2(1-\rho^2)}{8V_0^{3/2}}k^2
$$

with $V_0 = 0.04$, $\rho = -0.65$, and $\xi = 0.50$, compute $\sigma_{\text{impl}}$ at log-moneyness $k = -0.10$ (OTM put), $k = 0$ (ATM), and $k = 0.10$ (OTM call). Plot or sketch the resulting smile and identify the skew and curvature.

??? success "Solution to Exercise 2"
    We have $V_0 = 0.04$, $\rho = -0.65$, $\xi = 0.50$, so $\sqrt{V_0} = 0.20$.

    The approximation formula is:

    $$
    \sigma_{\text{impl}}(k) \approx \sqrt{V_0} + \frac{\rho\xi}{4\sqrt{V_0}}k + \frac{\xi^2(1-\rho^2)}{8V_0^{3/2}}k^2
    $$

    First, compute the coefficients:

    - Slope (skew): $\frac{\rho\xi}{4\sqrt{V_0}} = \frac{(-0.65)(0.50)}{4 \times 0.20} = \frac{-0.325}{0.80} = -0.40625$
    - Curvature: $\frac{\xi^2(1-\rho^2)}{8V_0^{3/2}} = \frac{0.25 \times (1 - 0.4225)}{8 \times 0.008} = \frac{0.25 \times 0.5775}{0.064} = \frac{0.144375}{0.064} = 2.2559$

    Now evaluate at each moneyness:

    **ATM** ($k = 0$):

    $$
    \sigma_{\text{impl}}(0) = 0.20 + 0 + 0 = 20.0\%
    $$

    **OTM put** ($k = -0.10$):

    $$
    \sigma_{\text{impl}}(-0.10) = 0.20 + (-0.40625)(-0.10) + 2.2559 \times 0.01 = 0.20 + 0.04063 + 0.02256 = 0.26319 \approx 26.3\%
    $$

    **OTM call** ($k = 0.10$):

    $$
    \sigma_{\text{impl}}(0.10) = 0.20 + (-0.40625)(0.10) + 2.2559 \times 0.01 = 0.20 - 0.04063 + 0.02256 = 0.18194 \approx 18.2\%
    $$

    The smile exhibits a pronounced **negative skew**: OTM puts have higher implied volatility than OTM calls. The skew is driven by $\rho < 0$ (the slope coefficient is negative). The curvature term $\propto \xi^2$ adds convexity, lifting both wings relative to the ATM level.

---

**Exercise 3.** The Heston model reduces to time-dependent Black–Scholes when $\xi = 0$. In this limit, the effective variance is

$$
\bar{\sigma}^2(T) = \frac{1}{T}\int_0^T V_s\,ds = \theta + \frac{(V_0 - \theta)(1 - e^{-\kappa T})}{\kappa T}
$$

Compute $\bar{\sigma}(T)$ for $T = 0.25, 1.0, 5.0$ with $V_0 = 0.09$, $\theta = 0.04$, $\kappa = 1.5$. Verify that $\bar{\sigma}(T) \to \sqrt{\theta}$ as $T \to \infty$.

??? success "Solution to Exercise 3"
    With $V_0 = 0.09$, $\theta = 0.04$, $\kappa = 1.5$, the effective variance is:

    $$
    \bar{\sigma}^2(T) = \theta + \frac{(V_0 - \theta)(1 - e^{-\kappa T})}{\kappa T} = 0.04 + \frac{0.05(1 - e^{-1.5T})}{1.5T}
    $$

    **At $T = 0.25$:**

    $$
    \bar{\sigma}^2(0.25) = 0.04 + \frac{0.05(1 - e^{-0.375})}{0.375} = 0.04 + \frac{0.05 \times 0.3127}{0.375} = 0.04 + 0.04169 = 0.08169
    $$

    $$
    \bar{\sigma}(0.25) = \sqrt{0.08169} \approx 28.58\%
    $$

    **At $T = 1.0$:**

    $$
    \bar{\sigma}^2(1.0) = 0.04 + \frac{0.05(1 - e^{-1.5})}{1.5} = 0.04 + \frac{0.05 \times 0.7769}{1.5} = 0.04 + 0.02590 = 0.06590
    $$

    $$
    \bar{\sigma}(1.0) = \sqrt{0.06590} \approx 25.67\%
    $$

    **At $T = 5.0$:**

    $$
    \bar{\sigma}^2(5.0) = 0.04 + \frac{0.05(1 - e^{-7.5})}{7.5} = 0.04 + \frac{0.05 \times 0.99945}{7.5} = 0.04 + 0.00666 = 0.04666
    $$

    $$
    \bar{\sigma}(5.0) = \sqrt{0.04666} \approx 21.60\%
    $$

    **Verification:** As $T \to \infty$, the exponential term vanishes and $\bar{\sigma}^2(T) \to \theta = 0.04$, so $\bar{\sigma}(\infty) = \sqrt{0.04} = 20\%$. Since $V_0 = 0.09 > \theta = 0.04$, the effective volatility starts high and decays monotonically toward $\sqrt{\theta} = 20\%$.

---

**Exercise 4.** The stationary distribution of the CIR variance process is Gamma with shape $\alpha = 2\kappa\theta/\xi^2$ and rate $\beta = 2\kappa/\xi^2$. For $\kappa = 3$, $\theta = 0.05$, $\xi = 0.4$: (a) compute the shape and rate parameters; (b) find the mode of the Gamma distribution; (c) compute $\mathbb{P}(V_\infty > 0.10)$ (variance exceeding 10%) using the Gamma CDF. What does this tell you about the frequency of high-volatility regimes?

??? success "Solution to Exercise 4"
    With $\kappa = 3$, $\theta = 0.05$, $\xi = 0.4$:

    **(a)** Shape and rate parameters:

    $$
    \alpha = \frac{2\kappa\theta}{\xi^2} = \frac{2 \times 3 \times 0.05}{0.16} = \frac{0.30}{0.16} = 1.875
    $$

    $$
    \beta = \frac{2\kappa}{\xi^2} = \frac{6}{0.16} = 37.5
    $$

    **(b)** The mode of the Gamma$(\alpha, \beta)$ distribution (for $\alpha > 1$) is:

    $$
    \text{mode} = \frac{\alpha - 1}{\beta} = \frac{0.875}{37.5} = 0.02333
    $$

    The mode is less than the mean $\theta = 0.05$ because the Gamma distribution is right-skewed.

    **(c)** We need $\mathbb{P}(V_\infty > 0.10) = 1 - F_{\text{Gamma}}(0.10; 1.875, 37.5)$, where $F_{\text{Gamma}}$ is the Gamma CDF. Using the substitution $x = \beta \cdot v = 37.5 \times 0.10 = 3.75$, this equals $1 - \frac{\gamma(1.875, 3.75)}{\Gamma(1.875)}$, where $\gamma$ is the lower incomplete gamma function. Numerically, $\mathbb{P}(V_\infty > 0.10) \approx 0.057$, or about 5.7%.

    This means that in the stationary regime, variance exceeds 10% (volatility exceeds $\sqrt{0.10} \approx 31.6\%$) only about 5.7% of the time. High-volatility regimes are relatively rare under these parameters, though not negligible.

---

**Exercise 5.** In the Euler simulation scheme, one step of the variance process is

$$
V_{t+\Delta} = V_t + \kappa(\theta - V_t^+)\Delta + \xi\sqrt{V_t^+}\sqrt{\Delta}\,Z
$$

with $Z \sim \mathcal{N}(0,1)$. Starting from $V_0 = 0.01$ with $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\Delta = 1/252$, compute the threshold value $Z^*$ such that $V_\Delta < 0$ when $Z < Z^*$. What is $\mathbb{P}(Z < Z^*)$? How does this probability change if $V_0 = 0.04$?

??? success "Solution to Exercise 5"
    Starting from $V_0 = 0.01$, with $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\Delta = 1/252$. The Euler step is:

    $$
    V_\Delta = V_0 + \kappa(\theta - V_0)\Delta + \xi\sqrt{V_0}\sqrt{\Delta}\,Z
    $$

    Compute the deterministic part:

    $$
    V_0 + \kappa(\theta - V_0)\Delta = 0.01 + 2(0.04 - 0.01)/252 = 0.01 + 0.06/252 = 0.01 + 0.000238 = 0.010238
    $$

    Compute the stochastic coefficient:

    $$
    \xi\sqrt{V_0}\sqrt{\Delta} = 0.5 \times \sqrt{0.01} \times \sqrt{1/252} = 0.5 \times 0.1 \times 0.06299 = 0.003150
    $$

    Setting $V_\Delta = 0$:

    $$
    0.010238 + 0.003150 \, Z^* = 0 \implies Z^* = -\frac{0.010238}{0.003150} = -3.250
    $$

    The probability is $\mathbb{P}(Z < -3.250) \approx 0.058\%$.

    **For $V_0 = 0.04$:**

    $$
    V_0 + \kappa(\theta - V_0)\Delta = 0.04 + 0 = 0.04
    $$

    $$
    \xi\sqrt{V_0}\sqrt{\Delta} = 0.5 \times 0.2 \times 0.06299 = 0.006299
    $$

    $$
    Z^* = -\frac{0.04}{0.006299} = -6.350
    $$

    The probability $\mathbb{P}(Z < -6.350)$ is essentially zero ($< 10^{-10}$). Starting from the long-run mean $V_0 = \theta$ makes negative variance in a single Euler step virtually impossible, whereas starting from $V_0 = 0.01$ (well below $\theta$) gives a small but nonzero probability.

---

**Exercise 6.** Compare the five Heston parameters $(\kappa, \theta, \xi, \rho, V_0)$ in terms of which implied volatility surface features each primarily controls. For each parameter, state whether it mainly affects (a) the ATM level, (b) the skew (slope), (c) the smile curvature (wings), or (d) the term structure. Justify each answer with the relevant approximation formula or economic intuition.

??? success "Solution to Exercise 6"
    **$V_0$ (initial variance):** Mainly affects **(a) ATM level**, especially for short maturities. The short-maturity approximation gives $\sigma_{\text{impl}}(0, T) \approx \sqrt{V_0}$. It has negligible impact on skew, curvature, or long-dated term structure.

    **$\theta$ (long-run variance):** Mainly affects **(d) term structure** and long-maturity ATM level. As $T \to \infty$, $\sigma_{\text{impl}}^2 \approx \theta$. Together with $\kappa$, it determines how the ATM volatility interpolates between $\sqrt{V_0}$ and $\sqrt{\theta}$.

    **$\kappa$ (mean-reversion speed):** Mainly affects **(d) term structure**. Higher $\kappa$ causes the term structure to flatten more quickly toward $\sqrt{\theta}$. The half-life $t_{1/2} = \ln 2/\kappa$ sets the characteristic time scale.

    **$\rho$ (correlation):** Mainly affects **(b) skew**. From the approximation, the skew slope is $\partial\sigma_{\text{impl}}/\partial k|_{k=0} \propto \rho\xi/(4\sqrt{V_0})$. Negative $\rho$ produces the equity-like downside skew.

    **$\xi$ (vol-of-vol):** Mainly affects **(c) smile curvature**. The curvature coefficient is $\propto \xi^2(1-\rho^2)/(8V_0^{3/2})$. Higher $\xi$ produces more pronounced wings. It also contributes to skew through its product with $\rho$.

---

**Exercise 7.** A trader calibrates the Heston model to S&P 500 options and obtains $V_0 = 0.025$, $\theta = 0.04$, $\kappa = 1.8$, $\xi = 0.55$, $\rho = -0.72$. She then uses $\sigma_{\text{BS}} = \sqrt{V_0} = 15.8\%$ in the Black–Scholes formula for an ATM 1-year call. Using the Heston effective variance formula, compute $\bar{\sigma}(1)$ and the percentage error in using $\sqrt{V_0}$ instead. Explain why this error systematically under- or over-prices the option depending on whether $V_0 < \theta$ or $V_0 > \theta$.

??? success "Solution to Exercise 7"
    With $V_0 = 0.025$, $\theta = 0.04$, $\kappa = 1.8$, $T = 1$:

    $$
    \bar{\sigma}^2(1) = \theta + \frac{(V_0 - \theta)(1 - e^{-\kappa T})}{\kappa T} = 0.04 + \frac{(0.025 - 0.04)(1 - e^{-1.8})}{1.8}
    $$

    $$
    = 0.04 + \frac{(-0.015)(1 - 0.16530)}{1.8} = 0.04 + \frac{(-0.015)(0.83470)}{1.8} = 0.04 - 0.006956 = 0.033044
    $$

    $$
    \bar{\sigma}(1) = \sqrt{0.033044} \approx 18.18\%
    $$

    The trader uses $\sqrt{V_0} = \sqrt{0.025} = 15.81\%$.

    **Percentage error:**

    $$
    \frac{\bar{\sigma}(1) - \sqrt{V_0}}{\bar{\sigma}(1)} = \frac{18.18\% - 15.81\%}{18.18\%} \approx 13.0\%
    $$

    The trader **underestimates** the effective volatility by about 13%, which leads to **underpricing** the call.

    **Systematic direction:** When $V_0 < \theta$, the variance is expected to increase over the option's life, so the effective average variance $\bar{\sigma}^2(T) > V_0$, and using $\sqrt{V_0}$ underprices. Conversely, when $V_0 > \theta$, variance is expected to decrease, $\bar{\sigma}^2(T) < V_0$, and using $\sqrt{V_0}$ overprices. The Heston effective variance accounts for this mean-reverting drift, while the naive Black–Scholes approach ignores it.
