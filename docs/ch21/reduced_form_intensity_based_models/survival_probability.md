# Survival Probability

Survival probabilities are central objects in reduced-form credit models. They describe the likelihood that default has not occurred by a given time and form the building blocks for pricing all defaultable claims. Understanding their structure, computation, and relationship to market observables is essential.

---

## Definition and Basic Properties

### Unconditional Survival Probability

The **survival probability** from time 0 to time $T$ is:

$$
S(0,T) := \mathbb{Q}(\tau > T)
$$

where $\tau$ is the default time and $\mathbb{Q}$ is the risk-neutral measure.

### Conditional Survival Probability

Given information at time $t$ (on the pre-default event $\{\tau > t\}$):

$$
S(t,T) := \mathbb{Q}(\tau > T \mid \mathcal{G}_t) = \mathbb{Q}(\tau > T \mid \mathcal{F}_t, \tau > t)
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
S(t,T) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T \lambda_s \, ds\right) \middle| \mathcal{F}_t\right]
$$

where $\lambda_s$ is the default intensity process.

**Derivation:** On $\{\tau > t\}$, using the Cox construction with $\tau = \Lambda^{-1}(E)$ where $E \sim \text{Exp}(1)$ independent of $\mathcal{F}$:

$$
\mathbb{Q}(\tau > T \mid \mathcal{F}_t, \tau > t) = \mathbb{Q}(E > \Lambda_T \mid E > \Lambda_t, \mathcal{F}_t) = \frac{\mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_t)}{\mathbb{Q}(E > \Lambda_t \mid \mathcal{F}_t)}
$$

Since $E$ is independent of $\mathcal{F}_\infty$:

$$
S(t,T) = \frac{e^{-\Lambda_T}}{e^{-\Lambda_t}} = \exp\left(-\int_t^T \lambda_s ds\right) \quad \text{(given } \mathcal{F}_t\text{)}
$$

Taking expectation over future intensity:

$$
S(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T \lambda_s ds} \middle| \mathcal{F}_t\right]
$$

### Deterministic Intensity Case

If $\lambda_t = \lambda(t)$ is a deterministic function:

$$
S(t,T) = \exp\left(-\int_t^T \lambda(s) \, ds\right) = e^{-\Lambda(t,T)}
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
h(t,T) = -\frac{\ln S(t,T)}{T-t}
$$

This is the constant intensity that would produce the same survival probability.

### Forward Hazard Rate

The **instantaneous forward hazard rate** is:

$$
\lambda_f(t,T) = -\frac{\partial \ln S(t,T)}{\partial T} = \frac{1}{S(t,T)} \cdot \left(-\frac{\partial S(t,T)}{\partial T}\right)
$$

In the limit $T \to t$: $\lambda_f(t,t) = \lambda_t$ (the spot intensity).

---

## Survival Probabilities for Specific Models

### Piecewise-Constant Intensity

With $\lambda(s) = \lambda_i$ for $s \in (T_{i-1}, T_i]$:

$$
S(0,T) = \exp\left(-\sum_{i=1}^{k-1} \lambda_i (T_i - T_{i-1}) - \lambda_k (T - T_{k-1})\right)
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
S(t,T) = A(t,T) \exp(-B(t,T) \lambda_t)
$$

where $A(t,T)$ and $B(t,T)$ satisfy Riccati ODEs:

$$
B(t,T) = \frac{2(e^{\gamma(T-t)} - 1)}{(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma}
$$

$$
A(t,T) = \left[\frac{2\gamma e^{(\kappa + \gamma)(T-t)/2}}{(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma}\right]^{2\kappa\theta/\sigma^2}
$$

with $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$.

### Vasicek Intensity Model

With $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma dW_t$ (Gaussian OU process):

$$
S(t,T) = \exp\left(-B(t,T)\lambda_t - A(t,T)\right)
$$

where:

$$
B(t,T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa}
$$

$$
A(t,T) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(t,T) - (T-t)) - \frac{\sigma^2}{4\kappa}B(t,T)^2
$$

**Note:** Vasicek intensity can become negative, which is economically problematic but sometimes used for analytical convenience.

---

## Default Probability Term Structure

### Cumulative Default Probability

The probability of default by time $T$:

$$
F(t,T) := \mathbb{Q}(\tau \le T \mid \mathcal{G}_t) = 1 - S(t,T)
$$

### Marginal (Period) Default Probability

The probability of default during period $(T_1, T_2]$, conditional on survival to $T_1$:

$$
\mathbb{Q}(\tau \in (T_1, T_2] \mid \tau > T_1) = \frac{S(t, T_1) - S(t, T_2)}{S(t, T_1)} = 1 - \frac{S(t, T_2)}{S(t, T_1)}
$$

### Default Density

The density of default time (conditional on $\mathcal{F}_t$):

$$
f(t,T) = -\frac{\partial S(t,T)}{\partial T} = S(t,T) \cdot \lambda_f(t,T)
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
P^d(0,T) = P(0,T)\left[R + (1-R)S(0,T)\right]
$$

where $P(0,T)$ is the risk-free discount factor.

Solving for survival probability:

$$
S(0,T) = \frac{P^d(0,T)/P(0,T) - R}{1 - R}
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
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds} \middle| \mathcal{F}_t\right] = P(t,T) \cdot S(t,T) \quad \text{(under independence)}
$$

When $r$ and $\lambda$ are independent, risk-adjusted discounting **separates** into interest rate discounting times survival probability.

### Default-Adjusted Discount Factor

The **default-adjusted discount factor** is:

$$
D^d(t,T) := P(t,T) \cdot S(t,T)
$$

This discounts both for time value and credit risk.

### Correlation Effects

If $r_t$ and $\lambda_t$ are correlated:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds}\right] \ne P(t,T) \cdot S(t,T)
$$

Positive correlation ($r$ and $\lambda$ move together) increases the covariance term; negative correlation decreases it. This matters for credit-rate hybrid products.

---

## Computation Methods

### Analytical (Affine Models)

For affine intensity models (CIR, Vasicek), survival probabilities have exponential-affine form:

$$
S(t,T) = A(T-t) e^{-B(T-t)\lambda_t}
$$

Solve the associated Riccati equations for $A$ and $B$.

### Monte Carlo Simulation

1. Simulate intensity paths $\lambda^{(i)}_s$ for $s \in [t, T]$
2. Compute cumulative hazard: $\Lambda^{(i)} = \int_t^T \lambda^{(i)}_s ds$
3. Estimate: $\hat{S}(t,T) = \frac{1}{N}\sum_{i=1}^N e^{-\Lambda^{(i)}}$

### PDE Methods

Survival probability satisfies a Kolmogorov backward equation:

$$
\frac{\partial S}{\partial t} + \mathcal{L}S - \lambda S = 0, \quad S(T,T) = 1
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

---

## Exercises

**Exercise 1.** For constant intensity $\lambda = 2\%$, compute the survival probability $S(0,T) = e^{-\lambda T}$ for $T = 1, 3, 5, 10$ years. Also compute the corresponding default probabilities $\mathbb{Q}(\tau \le T) = 1 - S(0,T)$. Plot or describe the shape of the survival curve.

??? success "Solution to Exercise 1"
    For constant intensity $\lambda = 2\% = 0.02$, the survival probability is $S(0,T) = e^{-\lambda T}$.

    **Survival probabilities:**

    | $T$ (years) | $S(0,T) = e^{-0.02T}$ | $\mathbb{Q}(\tau \le T) = 1 - S(0,T)$ |
    |:-----------:|:----------------------:|:--------------------------------------:|
    | 1           | $e^{-0.02} = 0.9802$  | $0.0198$ (1.98%)                       |
    | 3           | $e^{-0.06} = 0.9418$  | $0.0582$ (5.82%)                       |
    | 5           | $e^{-0.10} = 0.9048$  | $0.0952$ (9.52%)                       |
    | 10          | $e^{-0.20} = 0.8187$  | $0.1813$ (18.13%)                      |

    **Shape of the survival curve:** The survival curve $S(0,T) = e^{-0.02T}$ is a decreasing exponential function. It starts at 1 (certain survival at $T = 0$) and decays monotonically toward 0 as $T \to \infty$. The rate of decay is governed by $\lambda$: the curve drops by a factor of $e^{-0.02} \approx 0.98$ for each additional year. For constant intensity, the curve is convex (concave upward), meaning the marginal decrease in survival probability per unit time diminishes as $T$ grows -- this is because fewer entities remain "at risk" at longer horizons.

    The default probability curve $F(0,T) = 1 - e^{-0.02T}$ is correspondingly a concave increasing function approaching 1.

---

**Exercise 2.** Show that the conditional survival probability satisfies $S(t,T) = S(0,T)/S(0,t)$ for deterministic intensity. Use this to compute the probability of defaulting between years 3 and 5, given survival to year 3, when $\lambda = 2\%$.

??? success "Solution to Exercise 2"
    **Proof that $S(t,T) = S(0,T)/S(0,t)$ for deterministic intensity:**

    For deterministic intensity $\lambda(s)$, the survival probabilities are:

    $$
    S(0,T) = e^{-\int_0^T \lambda(s)\,ds}, \quad S(0,t) = e^{-\int_0^t \lambda(s)\,ds}
    $$

    The conditional survival probability from $t$ to $T$ is:

    $$
    S(t,T) = e^{-\int_t^T \lambda(s)\,ds}
    $$

    Now compute the ratio:

    $$
    \frac{S(0,T)}{S(0,t)} = \frac{e^{-\int_0^T \lambda(s)\,ds}}{e^{-\int_0^t \lambda(s)\,ds}} = e^{-\int_0^T \lambda(s)\,ds + \int_0^t \lambda(s)\,ds} = e^{-\int_t^T \lambda(s)\,ds} = S(t,T)
    $$

    This confirms $S(t,T) = S(0,T)/S(0,t)$. $\square$

    **Probability of defaulting between years 3 and 5 given survival to year 3:**

    With $\lambda = 2\% = 0.02$:

    $$
    \mathbb{Q}(\tau \in (3,5] \mid \tau > 3) = 1 - \frac{S(0,5)}{S(0,3)} = 1 - \frac{e^{-0.02 \times 5}}{e^{-0.02 \times 3}} = 1 - e^{-0.02 \times 2} = 1 - e^{-0.04}
    $$

    Computing:

    $$
    1 - e^{-0.04} \approx 1 - 0.9608 = 0.0392 \approx 3.92\%
    $$

    Note that for constant intensity, this conditional probability $1 - e^{-\lambda(T_2 - T_1)}$ depends only on the length of the interval $(T_2 - T_1)$, not on the conditioning time. This is the memoryless property of the exponential distribution.

---

**Exercise 3.** The forward default probability over the interval $(T_1, T_2]$ given survival to $T_1$ is

$$
p(T_1, T_2) = 1 - \frac{S(0, T_2)}{S(0, T_1)}
$$

For piecewise-constant intensity $\lambda_1 = 1\%$ on $[0,3]$ and $\lambda_2 = 2.5\%$ on $(3,5]$, compute $p(3,5)$ and compare with $p(0,3)$.

??? success "Solution to Exercise 3"
    Given piecewise-constant intensity $\lambda_1 = 1\%$ on $[0,3]$ and $\lambda_2 = 2.5\%$ on $(3,5]$.

    **Compute survival probabilities:**

    $$
    S(0,3) = e^{-0.01 \times 3} = e^{-0.03} \approx 0.97045
    $$

    $$
    S(0,5) = e^{-0.01 \times 3 - 0.025 \times 2} = e^{-0.03 - 0.05} = e^{-0.08} \approx 0.92312
    $$

    **Forward default probability $p(3,5)$:**

    $$
    p(3,5) = 1 - \frac{S(0,5)}{S(0,3)} = 1 - \frac{e^{-0.08}}{e^{-0.03}} = 1 - e^{-0.05} \approx 1 - 0.95123 = 0.04877 \approx 4.88\%
    $$

    Note that $p(3,5)$ depends only on the intensity over the interval $(3,5]$:

    $$
    p(3,5) = 1 - e^{-\int_3^5 \lambda(s)\,ds} = 1 - e^{-0.025 \times 2} = 1 - e^{-0.05}
    $$

    **Forward default probability $p(0,3)$:**

    $$
    p(0,3) = 1 - S(0,3) = 1 - e^{-0.03} \approx 1 - 0.97045 = 0.02955 \approx 2.96\%
    $$

    **Comparison:** $p(3,5) \approx 4.88\%$ is significantly larger than $p(0,3) \approx 2.96\%$. This reflects the higher intensity in the $(3,5]$ period ($\lambda_2 = 2.5\%$ versus $\lambda_1 = 1\%$). The annualized conditional default rate in $(3,5]$ is approximately $2.5\%$ per year, compared to $1\%$ per year in $[0,3]$, so the two-year forward default probability over $(3,5]$ exceeds the three-year cumulative default probability over $[0,3]$.

---

**Exercise 4.** Under a CIR intensity model, the survival probability has the affine form $S(t,T) = e^{-\alpha(T-t) - \beta(T-t)\lambda_t}$. Explain qualitatively why higher current intensity $\lambda_t$ leads to lower survival probability. For two issuers with $\lambda_0^{(1)} = 1\%$ and $\lambda_0^{(2)} = 3\%$ (same CIR parameters otherwise), which has a steeper survival curve?

??? success "Solution to Exercise 4"
    **Qualitative explanation of why higher $\lambda_t$ leads to lower $S(t,T)$:**

    The survival probability under a CIR intensity model has the form:

    $$
    S(t,T) = A(\tau_h) \exp(-B(\tau_h) \lambda_t)
    $$

    where $\tau_h = T - t$, $A(\tau_h) > 0$, and $B(\tau_h) > 0$ for $\tau_h > 0$.

    Since $B(\tau_h) > 0$, the exponent $-B(\tau_h)\lambda_t$ becomes more negative as $\lambda_t$ increases. Therefore $\exp(-B(\tau_h)\lambda_t)$ decreases as $\lambda_t$ increases, which means $S(t,T)$ decreases.

    The economic intuition is clear: higher current default intensity means the entity is currently in a state of greater credit distress. Although mean reversion will pull $\lambda_t$ back toward $\theta$, a higher starting point $\lambda_t$ implies a higher average intensity over $[t,T]$, leading to a greater cumulative hazard $\int_t^T \lambda_s\,ds$ in expectation and hence lower survival probability.

    **Comparing the two issuers:**

    Issuer (1) has $\lambda_0^{(1)} = 1\%$ and issuer (2) has $\lambda_0^{(2)} = 3\%$, with identical CIR parameters $(\kappa, \theta, \sigma)$ otherwise.

    Issuer (2) has a **steeper survival curve** (faster initial decline in $S(0,T)$). To see this, note that the sensitivity of $S$ to time horizon at $T = 0$ is:

    $$
    \left.\frac{\partial S(0,T)}{\partial T}\right|_{T=0} = -\lambda_0 \cdot S(0,0) = -\lambda_0
    $$

    since $S(0,0) = 1$. For issuer (2), this initial slope is $-3\%$, which is steeper (more negative) than issuer (1)'s slope of $-1\%$.

    As $T$ grows, both survival curves converge because mean reversion pulls both intensities toward the same long-run level $\theta$. The difference between the two curves narrows at rate $e^{-\kappa T}$: specifically, $\ln S^{(2)}(0,T) - \ln S^{(1)}(0,T) \approx -B(T)(\lambda_0^{(2)} - \lambda_0^{(1)})$, and $B(T) \to 2/(\gamma + \kappa)$ as $T \to \infty$, so the gap stabilizes.

---

**Exercise 5.** Survival probabilities can be extracted from CDS spreads using the approximate relation $S(0,T) \approx e^{-\frac{s}{1-R}T}$. A 5-year CDS has spread $s = 150$ bp and recovery $R = 40\%$. Compute the implied 5-year survival probability. What is the implied annual default probability (assuming constant intensity)?

??? success "Solution to Exercise 5"
    Given: 5-year CDS spread $s = 150$ bp $= 0.015$ and recovery $R = 40\% = 0.4$.

    **Implied 5-year survival probability:**

    Using the approximation $S(0,T) \approx e^{-\frac{s}{1-R}T}$:

    $$
    S(0,5) \approx \exp\left(-\frac{0.015}{1 - 0.4} \times 5\right) = \exp\left(-\frac{0.015}{0.6} \times 5\right) = \exp(-0.025 \times 5) = e^{-0.125}
    $$

    Computing:

    $$
    S(0,5) \approx e^{-0.125} \approx 0.8825
    $$

    So the implied 5-year survival probability is approximately $88.25\%$, and the 5-year default probability is approximately $11.75\%$.

    **Implied annual default probability (constant intensity):**

    The implied constant intensity (hazard rate) is:

    $$
    \lambda = \frac{s}{1 - R} = \frac{0.015}{0.6} = 0.025 = 2.5\%
    $$

    The annual default probability (conditional on survival) is:

    $$
    p_{\text{annual}} = 1 - e^{-\lambda} = 1 - e^{-0.025} \approx 1 - 0.97531 = 0.02469 \approx 2.47\%
    $$

    This is the probability of defaulting in any given year, conditional on having survived to the start of that year. With constant intensity, this conditional annual default probability is the same for every year (memoryless property).

---

**Exercise 6.** Prove that the survival probability function $S(0,T)$ satisfies: (a) $S(0,0) = 1$, (b) $S(0,T)$ is non-increasing in $T$, and (c) $\lim_{T \to \infty} S(0,T) = 0$ when $\int_0^\infty \lambda_s\,ds = \infty$ a.s. Explain the economic meaning of each property.

??? success "Solution to Exercise 6"
    We prove each property under the assumption that $\lambda_s \ge 0$ a.s. for all $s$ and $S(0,T) = \mathbb{E}[e^{-\int_0^T \lambda_s\,ds}]$ (with the deterministic case being $S(0,T) = e^{-\int_0^T \lambda(s)\,ds}$).

    **(a) $S(0,0) = 1$:**

    $$
    S(0,0) = \mathbb{E}\left[e^{-\int_0^0 \lambda_s\,ds}\right] = \mathbb{E}[e^0] = \mathbb{E}[1] = 1
    $$

    **Economic meaning:** At the current time, the entity has certainly survived (no time has elapsed for default to occur). The probability of surviving to the present is trivially 1.

    **(b) $S(0,T)$ is non-increasing in $T$:**

    For $T_2 > T_1 \ge 0$:

    $$
    \int_0^{T_2} \lambda_s\,ds = \int_0^{T_1} \lambda_s\,ds + \int_{T_1}^{T_2} \lambda_s\,ds \ge \int_0^{T_1} \lambda_s\,ds
    $$

    since $\lambda_s \ge 0$ implies $\int_{T_1}^{T_2} \lambda_s\,ds \ge 0$. Therefore:

    $$
    e^{-\int_0^{T_2} \lambda_s\,ds} \le e^{-\int_0^{T_1} \lambda_s\,ds} \quad \text{a.s.}
    $$

    Taking expectations:

    $$
    S(0,T_2) = \mathbb{E}\left[e^{-\int_0^{T_2} \lambda_s\,ds}\right] \le \mathbb{E}\left[e^{-\int_0^{T_1} \lambda_s\,ds}\right] = S(0,T_1)
    $$

    $\square$

    **Economic meaning:** The probability of surviving to a later date is always less than or equal to the probability of surviving to an earlier date. Default is an absorbing event -- once an entity defaults, it cannot "un-default." A longer time horizon provides more opportunity for default to occur.

    **(c) $\lim_{T \to \infty} S(0,T) = 0$ when $\int_0^\infty \lambda_s\,ds = \infty$ a.s.:**

    If $\int_0^\infty \lambda_s\,ds = \infty$ almost surely, then for almost every $\omega$:

    $$
    \int_0^T \lambda_s(\omega)\,ds \to \infty \quad \text{as } T \to \infty
    $$

    Therefore:

    $$
    e^{-\int_0^T \lambda_s(\omega)\,ds} \to 0 \quad \text{as } T \to \infty \quad \text{a.s.}
    $$

    Since $0 \le e^{-\int_0^T \lambda_s\,ds} \le 1$, we can apply the **dominated convergence theorem** (with dominating function $g(\omega) = 1$):

    $$
    \lim_{T \to \infty} S(0,T) = \lim_{T \to \infty} \mathbb{E}\left[e^{-\int_0^T \lambda_s\,ds}\right] = \mathbb{E}\left[\lim_{T \to \infty} e^{-\int_0^T \lambda_s\,ds}\right] = \mathbb{E}[0] = 0
    $$

    $\square$

    **Economic meaning:** If the cumulative hazard grows without bound, then default is certain to occur eventually. No entity can survive forever if it faces a positive (on average) default intensity indefinitely. The condition $\int_0^\infty \lambda_s\,ds = \infty$ a.s. is satisfied whenever $\lambda_s$ is bounded below by any positive constant, or more generally when $\lambda_s$ does not decay too quickly. For CIR intensity with $\theta > 0$, mean reversion ensures the intensity stays near $\theta$ in the long run, so the cumulative hazard grows linearly and this condition holds.
