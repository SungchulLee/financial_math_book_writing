# Default Intensity and Hazard Rates

Reduced-form (intensity-based) credit models treat default as an exogenous random event governed by a **default intensity** or **hazard rate**. Rather than deriving default from firm value dynamics, these models specify the conditional instantaneous probability of default directly. This approach prioritizes tractability and calibration to market prices.

---

## Conceptual Framework

### From Structural to Reduced-Form

**Structural approach:** Default is endogenous, triggered when firm value hits a barrier.

**Reduced-form approach:** Default is exogenous, modeled as a random event with specified conditional probability.

The reduced-form approach does not ask "why" default occurs—only "when" and "with what probability."

### Advantages of Reduced-Form Models

1. **Tractability:** Pricing formulas have closed or semi-closed forms
2. **Calibration:** Direct link to market observables (CDS spreads)
3. **Flexibility:** Intensity can depend on any state variables
4. **Generality:** Encompasses multiple default causes
5. **Surprise default:** Default is genuinely unpredictable (totally inaccessible stopping time)

---

## Default Intensity: Definition

### Heuristic Definition

Let $\tau$ denote the random default time. The **default intensity** (or **hazard rate**) $\lambda_t$ is an $\mathcal{F}_t$-adapted, non-negative process such that:

$$
\mathbb{Q}(t < \tau \le t + dt \mid \mathcal{F}_t, \tau > t) \approx \lambda_t \, dt.
$$

**Interpretation:** Given survival to time $t$ and current market information, the probability of defaulting in the next instant $dt$ is approximately $\lambda_t \, dt$.

### Rigorous Definition

More precisely, the intensity is defined through the **compensator** of the default indicator process $H_t = \mathbf{1}_{\{\tau \le t\}}$:

$$
A_t = \int_0^{t \wedge \tau} \lambda_s \, ds
$$

is the $(\mathcal{G}_t, \mathbb{Q})$-compensator of $H_t$, meaning:

$$
M_t := H_t - A_t = \mathbf{1}_{\{\tau \le t\}} - \int_0^{t \wedge \tau} \lambda_s \, ds
$$

is a $(\mathcal{G}_t, \mathbb{Q})$-martingale.

---

## The Doubly-Stochastic (Cox Process) Construction

### Construction

The standard way to construct a default time with given intensity is via the **Cox process** (doubly-stochastic Poisson process):

1. Let $(\lambda_t)_{t \ge 0}$ be an $\mathcal{F}_t$-adapted non-negative intensity process
2. Define the **cumulative intensity**: $\Lambda_t = \int_0^t \lambda_s \, ds$
3. Let $E \sim \text{Exp}(1)$ be independent of $\mathcal{F}_\infty$
4. Define the default time:

$$
\tau = \inf\{t \ge 0 : \Lambda_t \ge E\} = \Lambda^{-1}(E).
$$

### Properties of Cox Construction

Under this construction:
- $\tau$ is a totally inaccessible $(\mathcal{G}_t)$-stopping time (surprise default)
- The intensity interpretation is exact: $\lambda_t$ is the hazard rate
- Immersion (H-hypothesis) holds automatically
- Default is conditionally independent of $\mathcal{F}_\infty$ given $\Lambda_\tau$

### Survival Probability

The conditional survival probability given $\mathcal{F}_t$ is:

$$
\mathbb{Q}(\tau > T \mid \mathcal{F}_t) = \mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_t) = \mathbb{E}\left[e^{-\Lambda_T} \mid \mathcal{F}_t\right].
$$

On the pre-default event $\{\tau > t\}$:

$$
\mathbb{Q}(\tau > T \mid \mathcal{G}_t) = \frac{\mathbb{E}\left[e^{-\Lambda_T} \mid \mathcal{F}_t\right]}{e^{-\Lambda_t}} = \mathbb{E}\left[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t\right].
$$

---

## Hazard Rate Interpretation

### Analogy with Actuarial Science

The hazard rate in credit modeling is analogous to the **force of mortality** in actuarial science:

$$
\lambda(t) = \lim_{h \to 0} \frac{\mathbb{P}(t < \tau \le t+h \mid \tau > t)}{h}.
$$

This is the instantaneous conditional default rate.

### Relation to Survival Function

For deterministic intensity $\lambda(t)$, the survival function is:

$$
S(t) = \mathbb{Q}(\tau > t) = \exp\left(-\int_0^t \lambda(s) \, ds\right) = e^{-\Lambda(t)}.
$$

The density of default time is:

$$
f(t) = -\frac{dS}{dt} = \lambda(t) S(t) = \lambda(t) e^{-\Lambda(t)}.
$$

### Cumulative Hazard

The cumulative hazard function is:

$$
\Lambda(t) = -\ln S(t) = \int_0^t \lambda(s) \, ds.
$$

This relationship allows estimation of intensity from survival data.

---

## Stochastic Intensity Models

### Why Stochastic Intensity?

Constant or deterministic intensity is too restrictive:
- Credit quality evolves randomly over time
- Market conditions affect default probability
- Spread volatility requires stochastic intensity

### General Framework

Let $\lambda_t$ be driven by state variables $X_t$:

$$
\lambda_t = g(X_t, t),
$$

where $X_t$ follows an SDE:

$$
dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t.
$$

The intensity inherits randomness from the state variables.

### Common Specifications

**1. Vasicek-type (Ornstein-Uhlenbeck):**

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma \, dW_t.
$$

Properties:
- Mean-reverting to long-run level $\theta$
- Gaussian—can become negative (problematic)
- Analytically tractable

**2. CIR-type (Cox-Ingersoll-Ross):**

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma\sqrt{\lambda_t} \, dW_t.
$$

Properties:
- Mean-reverting
- Non-negative if $2\kappa\theta \ge \sigma^2$ (Feller condition)
- Affine structure enables closed-form bond prices
- Industry standard for credit modeling

**3. Log-normal:**

$$
d\ln\lambda_t = \kappa(\theta - \ln\lambda_t) \, dt + \sigma \, dW_t.
$$

Properties:
- Strictly positive intensity
- Mean-reverting in log-space
- Heavier tails than CIR

**4. Jump-diffusion:**

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma\sqrt{\lambda_t} \, dW_t + J \, dN_t,
$$

where $N_t$ is a Poisson process and $J$ is jump size.

Properties:
- Captures sudden credit deterioration
- More realistic for crisis scenarios
- Complicates pricing

---

## Piecewise-Constant Intensity

### Practical Calibration Standard

For calibration to CDS term structures, piecewise-constant intensity is ubiquitous:

$$
\lambda(t) = \lambda_i \quad \text{for } t \in (T_{i-1}, T_i], \quad i = 1, \ldots, n.
$$

The intervals typically correspond to CDS maturities: 1Y, 2Y, 3Y, 5Y, 7Y, 10Y.

### Survival Probability

With piecewise-constant intensity:

$$
S(0, T) = \exp\left(-\sum_{i: T_i \le T} \lambda_i (T_i - T_{i-1}) - \lambda_{k}(T - T_{k-1})\right),
$$

where $T_{k-1} < T \le T_k$.

### Advantages

1. Exact fit to any number of CDS quotes
2. Easy bootstrapping algorithm
3. No distributional assumptions
4. Industry standard

### Disadvantages

1. Discontinuous intensity—economically unrealistic
2. Sensitive to quote errors
3. No dynamics—static snapshot only
4. Interpolation needed for off-market maturities

---

## Information Structure

### Intensity Filtration

The intensity $\lambda_t$ is $\mathcal{F}_t$-measurable, where $\mathcal{F}_t$ contains:
- Interest rate information
- Equity prices (if intensity depends on equity)
- Macroeconomic indicators
- Other market factors

Crucially, $\mathcal{F}_t$ does **not** contain information about the specific timing of $\tau$.

### Surprise Default

In reduced-form models with intensity, default is always a surprise:
- $\tau$ is totally inaccessible (no announcing sequence)
- Even with complete market information, exact default time is unknown
- Default "arrives" at an unexpected moment

This contrasts with structural models where default becomes predictable as firm value approaches the barrier.

### Immersion

Under the Cox construction, immersion holds automatically:
- $\mathcal{F}$-martingales remain $\mathcal{G}$-martingales
- Market dynamics are unchanged by default revelation
- Clean separation of market and credit risk

---

## Intensity and Default Probability

### Instantaneous Default Probability

$$
\mathbb{Q}(\tau \in (t, t+dt] \mid \mathcal{F}_t, \tau > t) = \lambda_t \, dt + o(dt).
$$

### Cumulative Default Probability

$$
\mathbb{Q}(\tau \le T \mid \mathcal{F}_t, \tau > t) = 1 - \mathbb{E}\left[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t\right].
$$

### Forward Default Probability

The forward default probability for period $(T_1, T_2]$ conditional on survival to $T_1$:

$$
\mathbb{Q}(\tau \le T_2 \mid \tau > T_1) = 1 - \frac{S(T_2)}{S(T_1)}.
$$

---

## Numerical Example

**Setup:**
- Piecewise-constant intensity: $\lambda_1 = 100$ bp (year 0-1), $\lambda_2 = 150$ bp (year 1-3)
- Compute survival probabilities

**Calculations:**

1-year survival:
$$
S(0,1) = e^{-0.01 \times 1} = e^{-0.01} = 0.9900
$$

2-year survival:
$$
S(0,2) = e^{-0.01 \times 1 - 0.015 \times 1} = e^{-0.025} = 0.9753
$$

3-year survival:
$$
S(0,3) = e^{-0.01 \times 1 - 0.015 \times 2} = e^{-0.04} = 0.9608
$$

**Default probabilities:**
- 1-year: $1.00\%$
- 2-year: $2.47\%$
- 3-year: $3.92\%$

---

## Key Takeaways

- Default intensity $\lambda_t$ governs the instantaneous conditional probability of default
- The Cox process construction creates default times with specified intensity
- Intensity is $\mathcal{F}_t$-adapted—driven by observable market factors
- CIR-type intensity is the standard choice for analytical tractability
- Piecewise-constant intensity is used for CDS calibration
- Reduced-form models produce surprise default (totally inaccessible)
- Immersion holds automatically under the Cox construction

---

## Further Reading

- Duffie, D., & Singleton, K. J. (1999). Modeling term structures of defaultable bonds. *Review of Financial Studies*, 12(4), 687–720.
- Lando, D. (1998). On Cox processes and credit risky securities. *Review of Derivatives Research*, 2(2–3), 99–120.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapters 7–8.
- Jarrow, R. A., & Turnbull, S. M. (1995). Pricing derivatives on financial securities subject to credit risk. *Journal of Finance*, 50(1), 53–85.
