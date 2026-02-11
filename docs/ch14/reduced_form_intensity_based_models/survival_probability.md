# Survival Probability

Survival probabilities are central objects in reduced-form credit models. They describe the likelihood that default has not occurred by a given time and form the building blocks for pricing all defaultable claims. Understanding their structure, computation, and relationship to market observables is essential.

---

## Definition and Basic Properties

### Unconditional Survival Probability

The **survival probability** from time 0 to time $T$ is:

$$
S(0,T) := \mathbb{Q}(\tau > T),
$$

where $\tau$ is the default time and $\mathbb{Q}$ is the risk-neutral measure.

### Conditional Survival Probability

Given information at time $t$ (on the pre-default event $\{\tau > t\}$):

$$
S(t,T) := \mathbb{Q}(\tau > T \mid \mathcal{G}_t) = \mathbb{Q}(\tau > T \mid \mathcal{F}_t, \tau > t),
$$

where $\mathcal{G}_t$ is the enlarged filtration and $\mathcal{F}_t$ is the market filtration.

### Key Properties

1. **Monotonicity:** $S(t,T_1) \ge S(t,T_2)$ for $T_1 \le T_2$ (survival probability decreases with horizon)
2. **Boundary conditions:** $S(t,t) = 1$ (certain survival at current time)
3. **Asymptotic behavior:** $S(t,T) \to 0$ as $T \to \infty$ if default is certain eventually
4. **Non-negative:** $0 \le S(t,T) \le 1$

---

## Relation to Intensity

### Fundamental Formula

Under the standard intensity framework with Cox process construction:

$$
S(t,T) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T \lambda_s \, ds\right) \middle| \mathcal{F}_t\right],
$$

where $\lambda_s$ is the default intensity process.

**Derivation:** On $\{\tau > t\}$, using the Cox construction with $\tau = \Lambda^{-1}(E)$ where $E \sim \text{Exp}(1)$ independent of $\mathcal{F}$:

$$
\mathbb{Q}(\tau > T \mid \mathcal{F}_t, \tau > t) = \mathbb{Q}(E > \Lambda_T \mid E > \Lambda_t, \mathcal{F}_t) = \frac{\mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_t)}{\mathbb{Q}(E > \Lambda_t \mid \mathcal{F}_t)}.
$$

Since $E$ is independent of $\mathcal{F}_\infty$:

$$
S(t,T) = \frac{e^{-\Lambda_T}}{e^{-\Lambda_t}} = \exp\left(-\int_t^T \lambda_s ds\right) \quad \text{(given } \mathcal{F}_t\text{)}.
$$

Taking expectation over future intensity:

$$
S(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T \lambda_s ds} \middle| \mathcal{F}_t\right].
$$

### Deterministic Intensity Case

If $\lambda_t = \lambda(t)$ is a deterministic function:

$$
S(t,T) = \exp\left(-\int_t^T \lambda(s) \, ds\right) = e^{-\Lambda(t,T)},
$$

where $\Lambda(t,T) = \int_t^T \lambda(s) ds$ is the cumulative hazard.

---

## Credit Term Structure

### Analogy with Interest Rates

Just as discount factors define the term structure of interest rates, survival probabilities define the **credit term structure**:

| Interest Rates | Credit Risk |
|----------------|-------------|
| Discount factor $P(t,T)$ | Survival probability $S(t,T)$ |
| Spot rate $r(t,T)$ | Hazard rate $h(t,T)$ |
| Forward rate $f(t,T)$ | Forward hazard rate $\lambda_f(t,T)$ |
| Yield curve | Credit curve |

### Implied Hazard Rate

The **continuously compounded hazard rate** for maturity $T$ is:

$$
h(t,T) = -\frac{\ln S(t,T)}{T-t}.
$$

This is the constant intensity that would produce the same survival probability.

### Forward Hazard Rate

The **instantaneous forward hazard rate** is:

$$
\lambda_f(t,T) = -\frac{\partial \ln S(t,T)}{\partial T} = \frac{1}{S(t,T)} \cdot \left(-\frac{\partial S(t,T)}{\partial T}\right).
$$

In the limit $T \to t$: $\lambda_f(t,t) = \lambda_t$ (the spot intensity).

---

## Survival Probabilities for Specific Models

### Piecewise-Constant Intensity

With $\lambda(s) = \lambda_i$ for $s \in (T_{i-1}, T_i]$:

$$
S(0,T) = \exp\left(-\sum_{i=1}^{k-1} \lambda_i (T_i - T_{i-1}) - \lambda_k (T - T_{k-1})\right),
$$

where $T_{k-1} < T \le T_k$.

**Example:** With nodes $T_0=0, T_1=1, T_2=3, T_3=5$ and intensities $\lambda_1=1\%, \lambda_2=1.5\%, \lambda_3=2\%$:

$$
S(0,2) = e^{-0.01 \times 1 - 0.015 \times 1} = e^{-0.025} = 0.9753
$$

$$
S(0,5) = e^{-0.01 \times 1 - 0.015 \times 2 - 0.02 \times 2} = e^{-0.08} = 0.9231
$$

### CIR Intensity Model

With $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma\sqrt{\lambda_t}dW_t$, the survival probability has affine form:

$$
S(t,T) = A(t,T) \exp(-B(t,T) \lambda_t),
$$

where $A(t,T)$ and $B(t,T)$ satisfy Riccati ODEs:

$$
B(t,T) = \frac{2(e^{\gamma(T-t)} - 1)}{(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma},
$$

$$
A(t,T) = \left[\frac{2\gamma e^{(\kappa + \gamma)(T-t)/2}}{(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma}\right]^{2\kappa\theta/\sigma^2},
$$

with $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$.

### Vasicek Intensity Model

With $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma dW_t$ (Gaussian OU process):

$$
S(t,T) = \exp\left(-B(t,T)\lambda_t - A(t,T)\right),
$$

where:

$$
B(t,T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa},
$$

$$
A(t,T) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(t,T) - (T-t)) - \frac{\sigma^2}{4\kappa}B(t,T)^2.
$$

**Note:** Vasicek intensity can become negative, which is economically problematic but sometimes used for analytical convenience.

---

## Default Probability Term Structure

### Cumulative Default Probability

The probability of default by time $T$:

$$
F(t,T) := \mathbb{Q}(\tau \le T \mid \mathcal{G}_t) = 1 - S(t,T).
$$

### Marginal (Period) Default Probability

The probability of default during period $(T_1, T_2]$, conditional on survival to $T_1$:

$$
\mathbb{Q}(\tau \in (T_1, T_2] \mid \tau > T_1) = \frac{S(t, T_1) - S(t, T_2)}{S(t, T_1)} = 1 - \frac{S(t, T_2)}{S(t, T_1)}.
$$

### Default Density

The density of default time (conditional on $\mathcal{F}_t$):

$$
f(t,T) = -\frac{\partial S(t,T)}{\partial T} = S(t,T) \cdot \lambda_f(t,T).
$$

For deterministic intensity: $f(0,T) = \lambda(T) e^{-\int_0^T \lambda(s)ds}$.

---

## Market Observables and Credit Curves

### CDS-Implied Survival Probabilities

Market CDS spreads imply survival probabilities:

1. Observe CDS spreads $s_1, s_2, \ldots, s_n$ for maturities $T_1, T_2, \ldots, T_n$
2. Bootstrap piecewise-constant hazard rates $\lambda_1, \lambda_2, \ldots, \lambda_n$
3. Compute survival curve: $S(0, T_i) = e^{-\sum_{j \le i} \lambda_j (T_j - T_{j-1})}$

### Bond-Implied Survival Probabilities

For a defaultable zero-coupon bond with price $P^d(0,T)$ and recovery $R$:

$$
P^d(0,T) = P(0,T)\left[R + (1-R)S(0,T)\right],
$$

where $P(0,T)$ is the risk-free discount factor.

Solving for survival probability:

$$
S(0,T) = \frac{P^d(0,T)/P(0,T) - R}{1 - R}.
$$

### Credit Curve Shapes

Typical shapes observed in markets:

| Shape | Interpretation | Typical Issuer |
|-------|----------------|----------------|
| Upward sloping | Higher long-term default risk | Investment grade |
| Flat | Constant hazard rate | Stable credit |
| Inverted | Near-term distress, potential recovery | Stressed credits |
| Humped | Medium-term peak risk | Transitional |

---

## Survival Probabilities and Discounting

### Risk-Adjusted Discounting

A key insight: survival-weighted discounting combines interest rate and credit effects:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds} \middle| \mathcal{F}_t\right] = P(t,T) \cdot S(t,T) \quad \text{(under independence)}.
$$

When $r$ and $\lambda$ are independent, risk-adjusted discounting **separates** into interest rate discounting times survival probability.

### Default-Adjusted Discount Factor

The **default-adjusted discount factor** is:

$$
D^d(t,T) := P(t,T) \cdot S(t,T).
$$

This discounts both for time value and credit risk.

### Correlation Effects

If $r_t$ and $\lambda_t$ are correlated:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds}\right] \ne P(t,T) \cdot S(t,T).
$$

Positive correlation ($r$ and $\lambda$ move together) increases the covariance term; negative correlation decreases it. This matters for credit-rate hybrid products.

---

## Computation Methods

### Analytical (Affine Models)

For affine intensity models (CIR, Vasicek), survival probabilities have exponential-affine form:

$$
S(t,T) = A(T-t) e^{-B(T-t)\lambda_t}.
$$

Solve the associated Riccati equations for $A$ and $B$.

### Monte Carlo Simulation

1. Simulate intensity paths $\lambda^{(i)}_s$ for $s \in [t, T]$
2. Compute cumulative hazard: $\Lambda^{(i)} = \int_t^T \lambda^{(i)}_s ds$
3. Estimate: $\hat{S}(t,T) = \frac{1}{N}\sum_{i=1}^N e^{-\Lambda^{(i)}}$

### PDE Methods

Survival probability satisfies a Kolmogorov backward equation:

$$
\frac{\partial S}{\partial t} + \mathcal{L}S - \lambda S = 0, \quad S(T,T) = 1,
$$

where $\mathcal{L}$ is the infinitesimal generator of the intensity process.

---

## Worked Example: CIR Intensity

**Parameters:**
- Current intensity: $\lambda_0 = 2\%$
- Mean-reversion speed: $\kappa = 0.5$
- Long-run mean: $\theta = 3\%$
- Volatility: $\sigma = 10\%$

**Compute $\gamma$:**
$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2} = \sqrt{0.25 + 0.02} = \sqrt{0.27} = 0.5196
$$

**5-year survival probability:**

$$
B(0,5) = \frac{2(e^{0.5196 \times 5} - 1)}{(0.5196 + 0.5)(e^{2.598} - 1) + 2 \times 0.5196}
$$

$$
= \frac{2(13.44 - 1)}{1.0196 \times 12.44 + 1.0392} = \frac{24.88}{13.72} = 1.814
$$

$$
A(0,5) = \left[\frac{2 \times 0.5196 \times e^{(0.5 + 0.5196) \times 2.5}}{(1.0196)(12.44) + 1.0392}\right]^{2 \times 0.5 \times 0.03/0.01}
$$

$$
= \left[\frac{1.0392 \times e^{2.55}}{13.72}\right]^{3} = \left[\frac{13.32}{13.72}\right]^3 = 0.971^3 = 0.915
$$

$$
S(0,5) = 0.915 \times e^{-1.814 \times 0.02} = 0.915 \times e^{-0.0363} = 0.915 \times 0.964 = 0.882
$$

**5-year default probability:** $1 - 0.882 = 11.8\%$

---

## Practical Considerations

### Extrapolation Beyond Observable Maturities

When CDS quotes are unavailable for long maturities:
- Assume constant intensity beyond last observed maturity
- Use parametric models fitted to available data
- Consider regulatory guidance (e.g., ultimate forward rate analogy)

### Interpolation Between Nodes

For maturities between CDS quotes:
- Linear interpolation of hazard rates (simple, may be discontinuous)
- Spline interpolation of survival probabilities (smoother)
- Nelson-Siegel style parametric forms

### Negative Implied Hazard Rates

If bond prices imply $S(t,T_2) > S(t,T_1)$ for $T_2 > T_1$:
- Indicates arbitrage or data error
- May reflect liquidity premiums
- Requires adjustment or investigation

---

## Key Takeaways

- Survival probability $S(t,T) = \mathbb{E}[e^{-\int_t^T \lambda_s ds} | \mathcal{F}_t]$ is the fundamental credit quantity
- For deterministic intensity: $S(t,T) = e^{-\int_t^T \lambda(s)ds}$
- CIR and other affine models give closed-form survival probabilities
- The credit term structure is analogous to the interest rate term structure
- Market instruments (CDS, bonds) reveal survival probabilities
- Survival probabilities are building blocks for all credit derivative pricing

---

## Further Reading

- O'Kane, D. (2008). *Modelling Single-name and Multi-name Credit Derivatives*. Wiley.
- Brigo, D., & Mercurio, F. (2006). *Interest Rate Models: Theory and Practice*. Springer, Chapter 21.
- Duffie, D., & Singleton, K. J. (2003). *Credit Risk: Pricing, Measurement, and Management*. Princeton University Press.
- Schönbucher, P. J. (2003). *Credit Derivatives Pricing Models*. Wiley.
