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

### Mean Reversion Speed ($\kappa$)

The parameter $\kappa > 0$ controls how quickly variance returns to its long-run level:

- **Half-life of shocks:** $t_{1/2} = \frac{\ln 2}{\kappa}$
- $\kappa = 1$: half-life of 8.3 months
- $\kappa = 3$: half-life of 2.8 months
- $\kappa = 5$: half-life of 1.7 months

**Calibration insight:** $\kappa$ primarily affects the **term structure** of implied volatility. Higher $\kappa$ flattens the term structure faster.

### Long-Run Variance ($\theta$)

The parameter $\theta > 0$ is the **stationary mean** of the variance process:

$$
\lim_{t \to \infty} \mathbb{E}[V_t] = \theta
$$

**Calibration insight:** $\theta$ controls the level of long-maturity implied volatility:

$$
\sigma_{\text{impl}}^2(T \to \infty) \approx \theta
$$

### Volatility of Volatility ($\xi$)

The parameter $\xi > 0$ controls the magnitude of variance fluctuations:

- Higher $\xi$ → more volatile volatility → more pronounced smile **curvature**
- $\xi$ affects both wings of the smile (not just skew)

**Calibration insight:** $\xi$ is identifiable from the **convexity** of the smile:

$$
\frac{\partial^2 \sigma_{\text{impl}}}{\partial k^2} \propto \xi^2
$$

### Correlation ($\rho$)

The parameter $\rho \in (-1, 1)$ controls the correlation between price and variance shocks:

- $\rho < 0$: leverage effect (typical for equities)
- $\rho = 0$: symmetric smile
- $\rho > 0$: inverse leverage (rare)

**Calibration insight:** $\rho$ directly controls the **skew**:

$$
\frac{\partial \sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \propto \rho
$$

### Initial Variance ($V_0$)

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
