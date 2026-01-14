# Wing Asymptotics and Moment Constraints


## Introduction


The **wings** of the implied volatility smile refer to the behavior of $\sigma_{\text{IV}}(K, T)$ as the strike $K$ moves far from the current spot $S_0$ or forward $F$. Understanding wing asymptotics is crucial for:
- Ensuring arbitrage-free extrapolation beyond traded strikes
- Characterizing tail risk and extreme events
- Constraining the moments of the risk-neutral distribution
- Pricing deep out-of-the-money options and variance swaps

This section develops the complete theory of wing asymptotics and establishes fundamental connections to moment constraints.

## Lee's Moment Formula


### 1. Statement of the Theorem


**Theorem 4.4.7** (Lee, 2004)  
Let $q(S_T)$ be the risk-neutral probability density at maturity $T$. Define the growth rate of total implied variance in the wings:


$$
p_+ := \lim_{y \to +\infty} \frac{\sigma_{\text{IV}}^2(y, T) \cdot T}{y}
$$




$$
p_- := \lim_{y \to -\infty} \frac{\sigma_{\text{IV}}^2(y, T) \cdot T}{|y|}
$$



where $y = \ln(K/F)$ is log-moneyness.

Then the **maximum finite moment** of the distribution is characterized by:


$$
p_{\pm} = \frac{2}{m_{\pm}}
$$



where $m_+$ is the largest $p$ such that $\mathbb{E}^\mathbb{Q}[S_T^p] < \infty$ (right tail), and $m_-$ is the largest $p$ such that $\mathbb{E}^\mathbb{Q}[S_T^{-p}] < \infty$ (left tail).

**Interpretation:** The slope of the implied variance in the wings is inversely proportional to the maximum finite moment.

### 2. Proof Sketch


The call option price for large strikes admits the tail expansion:


$$
C(K, T) \sim e^{-rT} \mathbb{E}^\mathbb{Q}[(S_T - K)^+] \sim e^{-rT} \int_K^\infty (S - K) q(S) dS
$$



For large $K$, if the density tail behaves as $q(S) \sim S^{-\alpha}$, then:


$$
C(K, T) \sim K^{1 - \alpha}
$$



Using the Black-Scholes formula approximation for deep OTM:


$$
C(K, T) \approx e^{-rT} S_0 e^{-\frac{1}{2}d_1^2} \sim \exp\left(-\frac{y^2}{2\sigma_{\text{IV}}^2 T}\right)
$$



Matching the power law decay $K^{1-\alpha}$ with the Gaussian tail requires:


$$
\sigma_{\text{IV}}^2(y, T) T \sim \frac{2y}{p}
$$



where $p = \alpha - 1$ is the moment exponent. □

### 3. Special Cases


**Finite variance ($p_+ = p_- = 2$):**


$$
\lim_{|y| \to \infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|} = 2
$$



The wings grow exactly linearly in log-moneyness.

**Infinite variance ($p_+ < 2$ or $p_- < 2$):**

Wings grow slower than linear—flatter smile indicates heavier tails and infinite variance.

**Finite fourth moment ($p_+ = p_- = 4$):**


$$
\lim_{|y| \to \infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|} = \frac{1}{2}
$$



Very steep wings, thin tails.

## Right Wing: Large-Strike Asymptotics


### 1. Power Law Tails


Assume the risk-neutral density has a power law right tail:


$$
q(S) \sim C_+ S^{-\alpha} \quad \text{as } S \to \infty
$$



for some $\alpha > 1$ (to ensure normalization).

**Implications:**
- Finite $p$-th moment: $\mathbb{E}[S_T^p] < \infty$ iff $p < \alpha - 1$
- Maximum finite moment: $m_+ = \alpha - 1$

### 2. Implied Volatility Asymptotics


**Theorem 4.4.8** (Right Wing Asymptotics)  
If $q(S) \sim C_+ S^{-\alpha}$ as $S \to \infty$, then:


$$
\sigma_{\text{IV}}^2(y, T) T \sim \frac{2y}{\alpha - 1} \quad \text{as } y \to +\infty
$$



Equivalently:


$$
\sigma_{\text{IV}}(K, T) \sim \sqrt{\frac{2 \ln(K/F)}{T(\alpha - 1)}}
$$



**Proof:** From Lee's formula with $m_+ = \alpha - 1$, we have $p_+ = \frac{2}{\alpha - 1}$. The result follows by definition of $p_+$. □

### 3. Exponential Tails


If instead the density has exponential decay:


$$
q(S) \sim C_+ e^{-\lambda S} \quad \text{as } S \to \infty
$$



**Implications:**
- All moments are finite: $\mathbb{E}[S_T^p] < \infty$ for all $p$
- Lee's formula: $p_+ = +\infty$

**Wing behavior:**


$$
\sigma_{\text{IV}}^2(y, T) T \gg y \quad \text{as } y \to +\infty
$$



The implied variance grows faster than linear (steep wings).

**Example (Gaussian tail):**  
For lognormal distribution:


$$
q(S) \sim \frac{1}{S\sigma\sqrt{2\pi T}} e^{-\frac{(\ln S - \mu)^2}{2\sigma^2 T}}
$$



The IV wings grow as:


$$
\sigma_{\text{IV}}^2(y, T) T \sim 2|y| + \text{const}
$$



(Linear growth with a different constant than power law.)

## Left Wing: Small-Strike Asymptotics


### 1. Put-Call Symmetry


By put-call parity:


$$
P(K, T) = C(K, T) - S_0 e^{-qT} + K e^{-rT}
$$



The implied volatility of a put equals that of a call:


$$
\sigma_{\text{IV}}^{\text{put}}(K, T) = \sigma_{\text{IV}}^{\text{call}}(K, T)
$$



Thus, left wing analysis proceeds analogously using puts.

### 2. Small-Strike Behavior


Define the left wing slope:


$$
p_- = \lim_{y \to -\infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|}
$$



**Theorem 4.4.9** (Left Wing Asymptotics)  
If the density tail behaves as:


$$
q(S) \sim C_- S^{\beta} \quad \text{as } S \to 0
$$



for some $\beta > -1$ (to ensure integrability), then:


$$
p_- = \frac{2}{\beta + 1}
$$



**Special case (Black-Scholes):**  
Lognormal density has $q(S) \sim S^{-1}$ as $S \to 0$, giving $\beta = -1$. However, this is **boundary case**—technically infinite $p_-$ due to exponential correction.

### 3. Absorbing Barrier at Zero


If there is **probability mass** at $S_T = 0$ (complete default):


$$
\mathbb{P}^\mathbb{Q}(S_T = 0) = p_0 > 0
$$



**Consequence:** The put price has a floor:


$$
P(K, T) \geq K e^{-rT} p_0
$$



This creates a **kink** in the left wing:


$$
\sigma_{\text{IV}}(K, T) \to \infty \quad \text{as } K \to 0
$$



(Infinite IV needed to match the put price floor.)

## Symmetric vs Asymmetric Wings


### 1. Symmetric Distribution


If the risk-neutral density is symmetric around $F$:


$$
q(F + x) = q(F - x) \quad \text{for all } x
$$



Then:


$$
p_+ = p_- = 2
$$



Both wings have finite variance tails.

**Markets:** Foreign exchange options often exhibit near-symmetric wings.

### 2. Asymmetric Distribution (Skewed)


**Equity markets:** Typically exhibit:


$$
p_- < p_+ \quad (\text{or } p_- < 2 < p_+)
$$



**Interpretation:** Left tail is heavier (fatter) than right tail, reflecting crash risk.

**Example:**  
- $p_- = 1.5$ → Inverse cubic tail ($\alpha_- = 2.5$)
- $p_+ = 2.0$ → Quadratic tail (finite variance)

Left wing flatter (higher IV) than right wing.

## Connections to Variance Swaps


### 1. Variance Swap Pricing


The fair strike for a variance swap is:


$$
K_{\text{var}} = \frac{2 e^{rT}}{T} \left(\int_0^F \frac{P(K)}{K^2} dK + \int_F^\infty \frac{C(K)}{K^2} dK\right)
$$



### 2. Wing Contribution


The integral is dominated by the wings:


$$
\int_F^\infty \frac{C(K)}{K^2} dK \sim \int_{y=0}^\infty C(Fe^y) e^{-2y} F dy
$$



For large $y$, using the tail behavior $C(K) \sim K^{1 - \alpha}$:


$$
\int_{y_{\text{large}}}^\infty e^{y(1 - \alpha)} e^{-2y} dy \sim \int_{y_{\text{large}}}^\infty e^{-y(\alpha + 1)} dy
$$



**Convergence condition:** $\alpha + 1 > 1$, i.e., $\alpha > 0$ (finite first moment).

**Connection to Lee's formula:**  
If $\alpha = m_+ + 1 < 3$ (infinite variance), the variance swap integral **diverges**.

**Practical implication:** Variance swaps are not well-defined for distributions with infinite variance, requiring careful wing truncation.

## Arbitrage Constraints on Wings


### 1. Minimum Wing Slope


For the density to be a valid probability measure:

**Lower bound:**


$$
p_{\pm} > 0
$$



**Upper bound (finite first moment):**


$$
p_{\pm} < \infty \quad \Rightarrow \quad \mathbb{E}[S_T] < \infty
$$



The forward price $F = \mathbb{E}^\mathbb{Q}[S_T]$ is finite by no-arbitrage, requiring:


$$
p_+ \geq 2/m_+ \quad \text{with } m_+ \geq 1
$$



Thus:


$$
p_+ \leq 2
$$



Similarly for the left wing.

### 2. Calibration Constraints


When fitting parametric smile models (SVI, SSVI), the wing slopes must satisfy:


$$
0 < p_- \leq 2, \quad 0 < p_+ \leq 2
$$



Violations indicate:
- Mispriced options
- Model over-fitting
- Extrapolation error

**Best practice:** Explicitly constrain wing slopes during calibration.

## Empirical Observations


### 1. Equity Index Wings


**S&P 500 typical values:**
- $p_- \approx 1.0$ to $1.5$ (fat left tail, crash risk)
- $p_+ \approx 2.0$ to $2.5$ (thin right tail)

**Interpretation:** Market prices put insurance heavily (left wing flat), while call side is closer to Gaussian.

### 2. FX Wings


**Major currency pairs (EUR/USD, USD/JPY):**
- $p_- \approx 2.0$
- $p_+ \approx 2.0$

**Interpretation:** Symmetric finite-variance distribution, two-sided jump risk.

### 3. Commodity Wings


**Crude oil:**
- $p_- \approx 1.5$ (supply disruption)
- $p_+ \approx 1.8$ (demand collapse)

**Natural gas:**
- Highly asymmetric depending on season and storage levels

## Wing Approximations in Practice


### 1. Polynomial Extrapolation


For strikes beyond the last traded option, fit:


$$
\sigma_{\text{IV}}^2(y, T) T = a + b|y| + c y^2 + \cdots
$$



**Constraint:** The linear coefficient $b$ should match $p_{\pm}$ from Lee's formula.

### 2. Power Law Tails (SVI)


The SVI parametrization:


$$
w(y) = a + b\left(\rho(y - m) + \sqrt{(y - m)^2 + \sigma^2}\right)
$$



**Wing slopes:**


$$
p_+ = 1 + \rho, \quad p_- = 1 - \rho
$$



**Constraint:** $\rho \in [-1, 1]$ ensures $0 < p_{\pm} < 2$ (finite variance).

**Limitation:** SVI cannot model infinite variance distributions ($p < 2$ arbitrary).

### 3. Rational Function Extrapolation


For more flexible wing behavior:


$$
w(y) \sim a|y| + b \log|y| + c \quad \text{as } |y| \to \infty
$$



This allows for:
- Leading linear term (controls moment)
- Logarithmic correction (finer tail structure)

## Moment-Constrained Calibration


### 1. Imposing Known Moments


If external information provides moment bounds:


$$
\mathbb{E}^\mathbb{Q}[S_T^2] = M_2, \quad \mathbb{E}^\mathbb{Q}[S_T^3] = M_3, \quad \ldots
$$



**Calibration strategy:**

1. Use Lee's formula to determine $p_{\pm}$ from moment constraints
2. Fit smile model with wing slopes constrained to $p_{\pm}$
3. Verify that extracted density has correct moments

**Example:** If variance is known from variance swap:


$$
\mathbb{E}[S_T^2] = F^2 + \text{Var}(S_T) = F^2 + \sigma_{\text{var}}^2 F^2 T
$$



This constrains the wings to decay at least as fast as $p_+ = p_- = 2$.

## Extreme Wing Behavior: Pathological Cases


### 1. Flat Wings ($p \to 0$)


If $\sigma_{\text{IV}}(y, T)$ is constant for large $|y|$:


$$
\sigma_{\text{IV}}(y) = \sigma_\infty \quad \text{for } |y| > y_{\text{large}}
$$



**Consequence (Lee):** All moments are infinite.

**Interpretation:** Extremely heavy tails—unrealistic for most assets.

### 2. Steep Wings ($p \to \infty$)


If IV grows faster than $\sqrt{|y|/T}$:


$$
\sigma_{\text{IV}}^2(y, T) T \sim |y|^\gamma \quad \text{with } \gamma > 1
$$



**Consequence:** Density has **compact support** (zero probability beyond some threshold).

**Interpretation:** Asset price is bounded—possible for commodities (price can't be negative, may have physical upper bound).

## Relationship to Greeks


### 1. Wing Vega


The vega in the wings is:


$$
\mathcal{V}(K) = S_0 e^{-qT} \phi(d_1) \sqrt{T}
$$



For large $K$, $d_1 \to -\infty$, so $\phi(d_1) \to 0$ exponentially.

**Implication:** Deep OTM options have very low vega—changes in wing IV have limited P&L impact unless positions are large.

### 2. Wing Delta


Deep OTM call delta:


$$
\Delta_{\text{call}} = e^{-qT} \Phi(d_1) \to 0 \quad \text{as } K \to \infty
$$



Deep OTM put delta:


$$
\Delta_{\text{put}} = -e^{-qT} \Phi(-d_1) \to -e^{-qT} \quad \text{as } K \to 0
$$



**Wing hedging:** Minimal sensitivity to spot moves, but gamma risk remains.

## Computational Aspects


### 1. Numerical Stability


Computing $\sigma_{\text{IV}}$ for deep OTM options:

**Challenge:** Option price $C(K) \approx 10^{-6}$ or smaller → numerical precision issues

**Solution:**
- Use higher-precision arithmetic
- Work in log-space: compute $\log C$ directly
- Extrapolate from traded strikes using wing asymptotics

### 2. Wing Interpolation Algorithms


**Algorithm:**

1. Fit SVI or SSVI to liquid strikes (90-110% of spot)
2. Determine wing slopes $p_{\pm}$ from fit
3. Extend IV linearly in $\sqrt{|y|}$ for $|y| > y_{\text{liquid}}$:

   $$
   \sigma_{\text{IV}}^2(y, T) T = w_{\text{last}} + p_{\pm} (|y| - y_{\text{liquid}})
   $$



**Guarantee:** Asymptotically correct behavior, arbitrage-free.

## Summary


Wing asymptotics reveal:

### 1. **Lee's moment formula:**



$$
p_{\pm} = \frac{2}{m_{\pm}}
$$



Wing slope inversely proportional to maximum finite moment.

### 2. **Arbitrage constraints:**



$$
0 < p_- \leq 2, \quad 0 < p_+ \leq 2
$$



Finite variance requires wings grow at least linearly in $|y|$.

### 3. **Asymptotic behavior:**


**Power law tail:** $q(S) \sim S^{-\alpha} \Rightarrow \sigma_{\text{IV}}^2 T \sim \frac{2|y|}{\alpha - 1}$

**Exponential tail:** $q(S) \sim e^{-\lambda S} \Rightarrow \sigma_{\text{IV}}^2 T \gg |y|$ (steep)

### 4. **Practical applications:**


- **Extrapolation:** Use power law wings beyond traded strikes
- **Calibration:** Constrain wing slopes to ensure valid density
- **Variance swaps:** Require finite variance ($p_{\pm} = 2$)
- **Moment inference:** Extract tail behavior from observed wings

### 5. **Empirical patterns:**


- **Equity:** Asymmetric ($p_- < p_+$), fat left tail
- **FX:** Symmetric ($p_- \approx p_+ \approx 2$)
- **Commodities:** Variable, depends on market structure

Wing asymptotics provide a rigorous framework for understanding tail risk, constraining models, and ensuring arbitrage-free pricing across the entire strike range.
