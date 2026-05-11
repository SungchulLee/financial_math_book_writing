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
\mathbb{Q}(t < \tau \le t + dt \mid \mathcal{F}_t, \tau > t) \approx \lambda_t \, dt
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
\tau = \inf\{t \ge 0 : \Lambda_t \ge E\} = \Lambda^{-1}(E)
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
\mathbb{Q}(\tau > T \mid \mathcal{F}_t) = \mathbb{Q}(E > \Lambda_T \mid \mathcal{F}_t) = \mathbb{E}\left[e^{-\Lambda_T} \mid \mathcal{F}_t\right]
$$

On the pre-default event $\{\tau > t\}$:

$$
\mathbb{Q}(\tau > T \mid \mathcal{G}_t) = \frac{\mathbb{E}\left[e^{-\Lambda_T} \mid \mathcal{F}_t\right]}{e^{-\Lambda_t}} = \mathbb{E}\left[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t\right]
$$

---

## Hazard Rate Interpretation

### Analogy with Actuarial Science

The hazard rate in credit modeling is analogous to the **force of mortality** in actuarial science:

$$
\lambda(t) = \lim_{h \to 0} \frac{\mathbb{P}(t < \tau \le t+h \mid \tau > t)}{h}
$$

This is the instantaneous conditional default rate.

### Relation to Survival Function

For deterministic intensity $\lambda(t)$, the survival function is:

$$
S(t) = \mathbb{Q}(\tau > t) = \exp\left(-\int_0^t \lambda(s) \, ds\right) = e^{-\Lambda(t)}
$$

The density of default time is:

$$
f(t) = -\frac{dS}{dt} = \lambda(t) S(t) = \lambda(t) e^{-\Lambda(t)}
$$

### Cumulative Hazard

The cumulative hazard function is:

$$
\Lambda(t) = -\ln S(t) = \int_0^t \lambda(s) \, ds
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
\lambda_t = g(X_t, t)
$$

where $X_t$ follows an SDE:

$$
dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t
$$

The intensity inherits randomness from the state variables.

### Common Specifications

**1. Vasicek-type (Ornstein-Uhlenbeck):**

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma \, dW_t
$$

Properties:

- Mean-reverting to long-run level $\theta$
- Gaussian—can become negative (problematic)
- Analytically tractable

**2. CIR-type (Cox-Ingersoll-Ross):**

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma\sqrt{\lambda_t} \, dW_t
$$

Properties:

- Mean-reverting
- Non-negative if $2\kappa\theta \ge \sigma^2$ (Feller condition)
- Affine structure enables closed-form bond prices
- Industry standard for credit modeling

**3. Log-normal:**

$$
d\ln\lambda_t = \kappa(\theta - \ln\lambda_t) \, dt + \sigma \, dW_t
$$

Properties:

- Strictly positive intensity
- Mean-reverting in log-space
- Heavier tails than CIR

**4. Jump-diffusion:**

$$
d\lambda_t = \kappa(\theta - \lambda_t) \, dt + \sigma\sqrt{\lambda_t} \, dW_t + J \, dN_t
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
\lambda(t) = \lambda_i \quad \text{for } t \in (T_{i-1}, T_i], \quad i = 1, \ldots, n
$$

The intervals typically correspond to CDS maturities: 1Y, 2Y, 3Y, 5Y, 7Y, 10Y.

### Survival Probability

With piecewise-constant intensity:

$$
S(0, T) = \exp\left(-\sum_{i: T_i \le T} \lambda_i (T_i - T_{i-1}) - \lambda_{k}(T - T_{k-1})\right)
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
\mathbb{Q}(\tau \in (t, t+dt] \mid \mathcal{F}_t, \tau > t) = \lambda_t \, dt + o(dt)
$$

### Cumulative Default Probability

$$
\mathbb{Q}(\tau \le T \mid \mathcal{F}_t, \tau > t) = 1 - \mathbb{E}\left[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t\right]
$$

### Forward Default Probability

The forward default probability for period $(T_1, T_2]$ conditional on survival to $T_1$:

$$
\mathbb{Q}(\tau \le T_2 \mid \tau > T_1) = 1 - \frac{S(T_2)}{S(T_1)}
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

---

## Exercises

**Exercise 1.** The default intensity $\lambda_t$ is defined heuristically as $\lambda_t \approx \mathbb{Q}(\tau \in (t, t+\Delta t] \mid \tau > t, \mathcal{F}_t) / \Delta t$. For constant intensity $\lambda = 3\%$, compute the probability of default in the next 6 months given survival to time $t$. Then compute the 5-year survival probability $S(0,5)$.

??? success "Solution to Exercise 1"
    We are given constant intensity $\lambda = 3\% = 0.03$.

    **Probability of default in the next 6 months given survival to time $t$:**

    For constant intensity, the conditional default probability over an interval of length $\Delta t = 0.5$ years is:

    $$
    \mathbb{Q}(\tau \in (t, t + 0.5] \mid \tau > t) = 1 - e^{-\lambda \cdot 0.5} = 1 - e^{-0.03 \times 0.5} = 1 - e^{-0.015}
    $$

    Computing:

    $$
    e^{-0.015} \approx 0.98511
    $$

    Therefore:

    $$
    \mathbb{Q}(\tau \in (t, t + 0.5] \mid \tau > t) \approx 1 - 0.98511 = 0.01489 \approx 1.49\%
    $$

    **5-year survival probability:**

    $$
    S(0,5) = e^{-\lambda \cdot 5} = e^{-0.03 \times 5} = e^{-0.15} \approx 0.8607
    $$

    The 5-year default probability is $1 - S(0,5) \approx 1 - 0.8607 = 0.1393 \approx 13.93\%$.

---

**Exercise 2.** Explain the key difference between the structural approach and the reduced-form approach to credit risk modeling. Why does the reduced-form approach produce "surprise" defaults while the structural approach does not? What mathematical property of the default time distinguishes the two frameworks?

??? success "Solution to Exercise 2"
    **Key difference between structural and reduced-form approaches:**

    In the **structural approach** (e.g., Merton 1974, Black-Cox 1976), default is an endogenous event triggered when the firm's asset value $V_t$ crosses a predetermined barrier $D$ (the default boundary). The default time is:

    $$
    \tau = \inf\{t \ge 0 : V_t \le D\}
    $$

    Since $V_t$ is a continuous diffusion process, as $V_t$ approaches $D$ from above, market participants can observe the firm getting closer to distress. The default time $\tau$ is a **predictable stopping time** -- there exists an announcing sequence of stopping times $\tau_n \uparrow \tau$ a.s. This means default can be "seen coming."

    In the **reduced-form approach**, default is modeled as an exogenous event governed by an intensity process $\lambda_t$. The default time is constructed as $\tau = \inf\{t : \Lambda_t \ge E\}$ where $E \sim \text{Exp}(1)$ is independent of all market information. The key mathematical property is that $\tau$ is a **totally inaccessible stopping time** -- no announcing sequence exists.

    **Why structural models do not produce surprise defaults:** Since $V_t$ follows a continuous path, it cannot jump over the barrier. As $V_t \to D$, the conditional probability of default in the next instant approaches 1, making default predictable. Mathematically, the first hitting time of a continuous process to a barrier is a predictable stopping time.

    **Why reduced-form models produce surprise defaults:** The independence of $E$ from $\mathcal{F}_\infty$ means that no amount of market information can reveal the exact time $\tau$. Even knowing the entire intensity path $(\lambda_s)_{s \ge 0}$, the randomness of $E$ ensures default arrives as a genuine surprise. The conditional default probability in the next instant is $\lambda_t \, dt$, which is infinitesimal -- default never becomes "certain" at any moment.

---

**Exercise 3.** The hazard rate function $h(t)$ for a deterministic intensity model is defined by $S(0,t) = e^{-\int_0^t h(s)\,ds}$. Given survival probabilities $S(0,1) = 0.98$, $S(0,3) = 0.93$, and $S(0,5) = 0.87$, compute the average hazard rates over the intervals $[0,1]$, $[0,3]$, and $[0,5]$. Is the hazard rate increasing or decreasing?

??? success "Solution to Exercise 3"
    Given the survival probabilities $S(0,1) = 0.98$, $S(0,3) = 0.93$, and $S(0,5) = 0.87$, we use $S(0,t) = e^{-\int_0^t h(s)\,ds}$ to extract the average hazard rate over each interval.

    **Average hazard rate over $[0,1]$:**

    $$
    \bar{h}_{0,1} = -\frac{\ln S(0,1)}{1} = -\frac{\ln 0.98}{1} = -\frac{-0.02020}{1} = 0.02020 \approx 2.02\%
    $$

    **Average hazard rate over $[0,3]$:**

    $$
    \bar{h}_{0,3} = -\frac{\ln S(0,3)}{3} = -\frac{\ln 0.93}{3} = -\frac{-0.07257}{3} = 0.02419 \approx 2.42\%
    $$

    **Average hazard rate over $[0,5]$:**

    $$
    \bar{h}_{0,5} = -\frac{\ln S(0,5)}{5} = -\frac{\ln 0.87}{5} = -\frac{-0.13926}{5} = 0.02785 \approx 2.79\%
    $$

    **Is the hazard rate increasing or decreasing?**

    The average hazard rates are increasing: $2.02\% < 2.42\% < 2.79\%$. This indicates that the hazard rate is **increasing** over time. We can also extract the marginal (forward) hazard rates for each sub-interval:

    - Over $[0,1]$: $\bar{h} = 2.02\%$
    - Over $[1,3]$: $\bar{h}_{1,3} = \frac{-\ln S(0,3) + \ln S(0,1)}{3-1} = \frac{\ln(0.98/0.93)}{2} = \frac{\ln 1.05376}{2} = \frac{0.05237}{2} = 2.62\%$
    - Over $[3,5]$: $\bar{h}_{3,5} = \frac{-\ln S(0,5) + \ln S(0,3)}{5-3} = \frac{\ln(0.93/0.87)}{2} = \frac{\ln 1.06897}{2} = \frac{0.06670}{2} = 3.33\%$

    The forward hazard rates $2.02\% < 2.62\% < 3.33\%$ confirm that the instantaneous hazard rate is increasing. This pattern is typical for investment-grade credits where the risk of deterioration grows with the time horizon.

---

**Exercise 4.** Consider a piecewise-constant intensity: $\lambda(t) = 1\%$ for $t \in [0,2]$ and $\lambda(t) = 3\%$ for $t \in (2,5]$. Compute $S(0,2)$, $S(0,5)$, and the conditional survival probability $S(2,5 \mid \tau > 2)$. What is the default probability over $[0,5]$?

??? success "Solution to Exercise 4"
    Given piecewise-constant intensity: $\lambda(t) = 1\%$ for $t \in [0,2]$ and $\lambda(t) = 3\%$ for $t \in (2,5]$.

    **Survival probability $S(0,2)$:**

    $$
    S(0,2) = \exp\left(-\int_0^2 \lambda(s)\,ds\right) = \exp(-0.01 \times 2) = e^{-0.02} \approx 0.9802
    $$

    **Survival probability $S(0,5)$:**

    $$
    S(0,5) = \exp\left(-\int_0^5 \lambda(s)\,ds\right) = \exp\left(-0.01 \times 2 - 0.03 \times 3\right) = e^{-0.02 - 0.09} = e^{-0.11} \approx 0.8958
    $$

    **Conditional survival probability $S(2,5 \mid \tau > 2)$:**

    For deterministic intensity, the conditional survival probability given survival to time 2 is:

    $$
    \mathbb{Q}(\tau > 5 \mid \tau > 2) = \frac{S(0,5)}{S(0,2)} = \frac{e^{-0.11}}{e^{-0.02}} = e^{-0.09} \approx 0.9139
    $$

    Alternatively, this equals $\exp\left(-\int_2^5 \lambda(s)\,ds\right) = e^{-0.03 \times 3} = e^{-0.09} \approx 0.9139$.

    **Default probability over $[0,5]$:**

    $$
    \mathbb{Q}(\tau \le 5) = 1 - S(0,5) = 1 - e^{-0.11} \approx 1 - 0.8958 = 0.1042 \approx 10.42\%
    $$

---

**Exercise 5.** A reduced-form model has intensity $\lambda_t = a + b\,r_t$ where $r_t$ is the short rate. Explain the economic rationale for making default intensity depend on the interest rate. If interest rates rise during a recession, what does this specification imply about the correlation between default risk and market conditions?

??? success "Solution to Exercise 5"
    **Economic rationale for $\lambda_t = a + b\,r_t$:**

    Making default intensity depend on the interest rate captures the empirical relationship between monetary conditions and credit risk. The parameter $a > 0$ represents a baseline default intensity independent of rates, while $b$ captures the sensitivity of credit risk to interest rate levels.

    **If $b > 0$ (positive dependence):** Higher interest rates correspond to higher default intensity. This is economically motivated by several channels:

    1. **Debt service burden:** When rates rise, firms with floating-rate debt or those needing to refinance face higher borrowing costs, increasing the probability of financial distress.
    2. **Economic tightening:** Central banks raise rates during inflationary or overheating episodes. If these rate hikes eventually trigger a recession, credit quality deteriorates.
    3. **Discount rate effect:** Higher rates reduce the present value of future cash flows, potentially pushing leveraged firms closer to distress.

    **Implications for recession scenarios:** If interest rates rise during a recession (e.g., due to inflation or central bank policy errors), the specification $\lambda_t = a + b\,r_t$ with $b > 0$ implies that default risk increases simultaneously with rising rates. This creates a **positive correlation** between interest rates and default intensity, which has important pricing implications:

    - Defaultable bond prices fall by more than risk-free bonds (credit spread widens when rates rise)
    - The joint expectation $\mathbb{E}[e^{-\int(r_s + \lambda_s)ds}]$ is lower than $\mathbb{E}[e^{-\int r_s ds}] \cdot \mathbb{E}[e^{-\int \lambda_s ds}]$ because the positive correlation makes high-$r$ and high-$\lambda$ scenarios more likely to occur together
    - Risk-adjusted discount factors are lower than the product of separate discount factors: positive wrong-way risk

    This specification is a simple affine model where the state variable is $X_t = r_t$, and the default-adjusted discount rate is $r_t + \lambda_t = (a + (1+b)\,r_t)$, which remains affine in $r_t$ and thus preserves tractability.

---

**Exercise 6.** List five advantages of reduced-form (intensity-based) models over structural models for practical credit derivatives pricing. For each advantage, provide a specific example where the reduced-form approach is superior.

??? success "Solution to Exercise 6"
    **Five advantages of reduced-form models over structural models:**

    **1. Analytical tractability and closed-form pricing.**
    Reduced-form models, especially affine intensity models (e.g., CIR intensity), yield closed-form or semi-closed-form expressions for survival probabilities, defaultable bond prices, and CDS spreads via the Riccati ODE system. *Example:* Pricing a portfolio of CDS contracts across multiple maturities requires rapid evaluation. Under a CIR intensity model, each CDS spread is computed by evaluating explicit formulas involving $A(\tau)$ and $B(\tau)$. A structural model (e.g., Merton) requires numerical computation of option prices on firm value for each maturity.

    **2. Direct calibration to market observables (CDS spreads, bond spreads).**
    Reduced-form models parameterize default intensity, which maps directly to CDS spreads and survival probabilities observable in the market. *Example:* Bootstrapping piecewise-constant hazard rates from a CDS term structure (1Y, 3Y, 5Y, 7Y, 10Y) is a standard, fast procedure. Structural models require estimating unobservable firm value and asset volatility, making calibration to market credit spreads indirect and often ill-conditioned.

    **3. Surprise default (totally inaccessible stopping time).**
    Reduced-form models produce default as a genuine surprise event, consistent with the empirical observation that defaults often occur suddenly without a smooth warning signal. *Example:* The sudden default of Lehman Brothers in September 2008 or the Enron collapse in 2001 occurred with little advance warning from equity markets. Structural models, where default is a predictable stopping time, cannot reproduce such sudden jumps in default probability.

    **4. Flexibility in incorporating multiple risk factors and correlations.**
    The intensity can depend on any observable or latent state variables -- interest rates, equity prices, macroeconomic factors, or regime indicators. *Example:* In a multi-name credit portfolio, default correlation is naturally modeled by making each name's intensity depend on a common systematic factor $Z_t$: $\lambda_t^{(i)} = a_i + b_i Z_t$. This approach is tractable and widely used in CDO pricing. Structural models require specifying a correlation structure for firm asset values, which is harder to calibrate.

    **5. Generality -- encompasses multiple default causes.**
    The reduced-form framework does not require specifying a single mechanism for default. The intensity aggregates all possible causes of default into one quantity. *Example:* A sovereign entity may default due to political instability, fiscal crisis, external shocks, or contagion. Specifying a firm-value process for a sovereign is economically meaningless, but modeling sovereign default intensity as a function of macro variables (GDP growth, debt/GDP ratio) is natural and well-motivated.
