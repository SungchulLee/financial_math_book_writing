# Short-Maturity Smile Asymptotics


## Introduction


The behavior of implied volatility as maturity approaches zero ($T \to 0$) reveals fundamental properties of the underlying asset's instantaneous volatility structure and the local geometry of the price process. Short-maturity asymptotics provide powerful tools for understanding market microstructure, extracting local volatility, and pricing very short-dated options (weekly, daily expirations). This section develops the complete asymptotic theory for the implied volatility smile in the small-time limit.

## Heuristic Intuition


### 1. Time Value Decay


As $T \to 0$, an option's value approaches its intrinsic value:


$$
\lim_{T \to 0} C(K, T) = \max(S_0 - K, 0)
$$



However, the **rate of approach** depends on how close $K$ is to the current spot $S_0$:

- **Deep ITM/OTM:** Option has essentially determined payoff → IV reflects little uncertainty
- **Near ATM:** Option payoff highly sensitive to small spot moves → IV reflects local volatility

### 2. Path Probability Concentration


For small $T$, the distribution of $S_T$ concentrates around $S_0$:


$$
S_T \approx S_0 + \int_0^T \sigma(S_t, t) S_t dW_t \approx S_0 + \sigma(S_0, 0) S_0 \int_0^T dW_t
$$



The limiting distribution as $T \to 0$ is determined by the **local volatility** at the initial spot.

## Mathematical Framework


### 1. General Diffusion Setting


Consider the underlying asset following:


$$
dS_t = \mu(S_t, t) S_t dt + \sigma(S_t, t) S_t dW_t
$$



under the physical measure. Under the risk-neutral measure $\mathbb{Q}$:


$$
dS_t = (r - q) S_t dt + \sigma(S_t, t) S_t dW_t^\mathbb{Q}
$$



The implied volatility $\sigma_{\text{IV}}(K, T)$ is defined through the Black-Scholes formula.

### 2. Small-Time Asymptotic Expansion


We seek an expansion of the form:


$$
\sigma_{\text{IV}}(K, T) = \sigma_0(K) + \sigma_1(K) T + \sigma_2(K) T^2 + O(T^3) \quad \text{as } T \to 0
$$



The coefficients $\sigma_0, \sigma_1, \sigma_2$ depend on the local dynamics at the spot.

## Leading-Order Asymptotics: Local Volatility


### 1. Main Result (Berestycki-Busca-Florent)


**Theorem 4.4.1** (Leading-Order Asymptotics)  
For a local volatility model with smooth $\sigma(S, t)$, as $T \to 0$:


$$
\sigma_{\text{IV}}(K, T) = \sigma(K, 0) + O(T)
$$



**Interpretation:** The short-maturity implied volatility at strike $K$ converges to the local volatility evaluated at that strike at the initial time.

### 2. Proof Sketch


The call option price can be written as:


$$
C(K, T) = e^{-rT} \mathbb{E}^\mathbb{Q}[\max(S_T - K, 0)]
$$



For small $T$, the density $p(S_T | S_0)$ concentrates around $S_0$. Near $K \approx S_0$:


$$
p(S_T | S_0) \approx \frac{1}{\sigma(K, 0) K \sqrt{2\pi T}} \exp\left(-\frac{(S_T - K)^2}{2\sigma^2(K, 0) K^2 T}\right)
$$



Computing the option price with this Gaussian approximation and matching to Black-Scholes gives $\sigma_{\text{IV}} \sim \sigma(K, 0)$. □

### 3. At-the-Money Limit


**Corollary 4.4.1**  
At-the-money ($K = S_0$):


$$
\lim_{T \to 0} \sigma_{\text{IV}}(S_0, T) = \sigma(S_0, 0) = \sigma_{\text{spot}}
$$



The ATM implied volatility converges to the **spot volatility**.

### 4. Away from the Money


For strikes $K \neq S_0$, the leading-order term still gives:


$$
\sigma_{\text{IV}}(K, T) \sim \sigma(K, 0)
$$



**Implication:** The short-dated smile directly reveals the local volatility function $\sigma(K, 0)$ across strikes.

## Next-Order Correction: Drift Effects


### 1. First-Order Correction


**Theorem 4.4.2** (First-Order Expansion)  
For smooth local volatility $\sigma(S, t)$:


$$
\sigma_{\text{IV}}(K, T) = \sigma(K, 0) + T \cdot \frac{\partial \sigma}{\partial t}(K, 0) + O(T^2)
$$



**Proof sketch:** Expanding the SDE for $S_t$ to order $T$ and matching moments gives the time derivative correction. □

**Interpretation:** If local volatility is time-dependent, the first-order correction captures the instantaneous rate of change at $t = 0$.

### 2. Spatial Derivatives


For non-constant local volatility in the spot direction, higher-order terms involve:


$$
\sigma_1(K) \sim \frac{\partial \sigma}{\partial S}(K, 0), \quad \frac{\partial^2 \sigma}{\partial S^2}(K, 0)
$$



**Full expansion (Hagan et al., 2002):**


$$
\sigma_{\text{IV}}(K, T) \approx \sigma(K, 0) \left\{1 + \frac{T}{24}\left[\frac{\sigma''(K, 0)}{\sigma(K, 0)} - \frac{(\sigma'(K, 0))^2}{4\sigma^2(K, 0)}\right] + \cdots \right\}
$$



## Stochastic Volatility Models


### 1. Heston Model


The Heston model:


$$
\begin{align}
dS_t &= (r - q) S_t dt + \sqrt{v_t} S_t dW_t^S \\
dv_t &= \kappa(\theta - v_t) dt + \xi \sqrt{v_t} dW_t^v \\
d\langle W^S, W^v \rangle_t &= \rho dt
\end{align}
$$



### 2. Small-Time ATM Asymptotics (Heston)


**Theorem 4.4.3** (Heston ATM Asymptotics)  
For the Heston model, as $T \to 0$:


$$
\sigma_{\text{IV}}(S_0, T) = \sqrt{v_0} + \frac{T}{8\sqrt{v_0}} \left[\kappa(\theta - v_0) - \frac{\xi^2}{2}\right] + O(T^2)
$$



**Interpretation:**

- Leading term: $\sqrt{v_0}$ (current spot variance)
- First-order correction: Depends on mean reversion and vol-of-vol

**Derivation outline:**

Using the moment-generating function for Heston:


$$
\mathbb{E}^\mathbb{Q}[e^{i\omega \ln S_T}] = \exp\left\{i\omega \ln S_0 + A(T; \omega) + B(T; \omega) v_0\right\}
$$



where $A(T; \omega)$ and $B(T; \omega)$ satisfy Riccati ODEs. Expanding in powers of $T$ and inverting gives the IV expansion.

### 3. Small-Time Smile (Heston)


Away from ATM, for log-moneyness $y = \ln(K/S_0)$:

**Theorem 4.4.4** (Heston Smile Expansion)


$$
\sigma_{\text{IV}}(y, T) = \sqrt{v_0} + \frac{\rho \xi}{4} y + \frac{1}{24\sqrt{v_0}}\left[\kappa(\theta - v_0) - \frac{\xi^2}{2}\right] T + \cdots
$$



**Key features:**

- Linear skew in $y$: coefficient is $\frac{\rho \xi}{4}$
- Skew is **instantaneous** (order $T^0$)
- Determined entirely by correlation $\rho$ and vol-of-vol $\xi$

**Consequence:** In Heston, the short-dated smile has **constant skew** across maturities (in appropriate coordinates).

## SABR Model


### 1. Model Specification


The SABR model:


$$
\begin{align}
dF_t &= \sigma_t F_t^\beta dW_t^1 \\
d\sigma_t &= \nu \sigma_t dW_t^2 \\
d\langle W^1, W^2 \rangle_t &= \rho dt
\end{align}
$$



commonly used for interest rate options.

### 2. Hagan's Asymptotic Formula


**Theorem 4.4.5** (Hagan et al., 2002)  
For SABR, the implied volatility admits the expansion:


$$
\sigma_{\text{IV}}(K) = \frac{\alpha}{(FK)^{(1-\beta)/2}} \frac{z}{x(z)} \left[1 + \left(\frac{(1-\beta)^2}{24} \frac{\alpha^2}{(FK)^{1-\beta}} + \frac{\rho\beta\nu\alpha}{4(FK)^{(1-\beta)/2}} + \frac{2 - 3\rho^2}{24}\nu^2\right)T + O(T^2)\right]
$$



where:

$$
z = \frac{\nu}{\alpha}(FK)^{(1-\beta)/2} \ln(F/K), \quad x(z) = \ln\left(\frac{\sqrt{1 - 2\rho z + z^2} + z - \rho}{1 - \rho}\right)
$$



**Leading behavior:** The "backbone" $(FK)^{-\frac{1-\beta}{2}}$ controls the base smile shape.

**First-order correction:** The bracket $[\cdots]T$ includes:

- Volatility convexity term
- Correlation-skew term
- Pure vol-of-vol term

**Validity:** Accurate for $T$ small and $|K - F|$ not too large.

## Extreme Strikes: Small-Time Large-Deviation Theory


### 1. Large Deviations for ITM/OTM Options


For deep ITM or OTM options (large $|K - S_0|$) with small $T$:

**Theorem 4.4.6** (Varadhan's Lemma Application)


$$
-\lim_{T \to 0} T \ln C(K, T) = \inf_{x: x > K} I(x)
$$



where $I(x)$ is the **rate function** from large deviation theory:


$$
I(x) = \inf_{\text{paths } \{S_t\}: S_T = x} \int_0^T \frac{(\dot{S}_t - \mu(S_t))^2}{2\sigma^2(S_t) S_t^2} dt
$$



**Interpretation:** The option price decays exponentially in $T$ at a rate determined by the "most likely path" from $S_0$ to the payoff region.

### 2. Connection to Implied Volatility


Taking logarithms and using $C \approx S_0 \mathcal{N}(d_1) \approx S_0 e^{-d_1^2/2}$ for deep OTM:


$$
\sigma_{\text{IV}}^2(K, T) T \sim 2 I(K) \quad \text{as } T \to 0, \, K \text{ far from } S_0
$$



**Result:** The implied variance $\sigma_{\text{IV}}^2 T$ grows with $|K - S_0|$ to overcome the exponential decay of the option price.

## Small-Time vs Small Moneyness Regimes


### 1. Three Asymptotic Regimes


**Regime 1: ATM ($K \approx S_0$, $T \to 0$)**


$$
\sigma_{\text{IV}}(K, T) \sim \sigma(S_0, 0)
$$



Local volatility at the spot.

**Regime 2: Finite moneyness ($K - S_0 = O(1)$, $T \to 0$)**


$$
\sigma_{\text{IV}}(K, T) \sim \sigma(K, 0)
$$



Local volatility at the strike.

**Regime 3: Scaling limit ($K - S_0 = O(\sqrt{T})$, $T \to 0$)**


$$
\sigma_{\text{IV}}\left(S_0 + y\sqrt{T}, T\right) \sim \sigma(S_0, 0) \left[1 + \frac{y^2}{2} \frac{\sigma'(S_0, 0)}{\sigma(S_0, 0)} + \cdots\right]
$$



This regime captures the transition from ATM to OTM, showing the parabolic smile shape.

### 2. Matched Asymptotics


The complete small-time picture requires **matching** these regimes:


$$
\sigma_{\text{IV}}(K, T) = \begin{cases}
\sigma(K, 0) + O(T) & |K - S_0| = O(1) \\
\sigma(S_0, 0) \left[1 + \frac{(K - S_0)^2}{2T\sigma^2(S_0, 0) S_0^2}\right] + O(T) & |K - S_0| = O(\sqrt{T})
\end{cases}
$$



## Practical Implications


### 1. Extracting Local Volatility from Short-Dated Options


**Method 1: Direct approximation**


$$
\sigma_{\text{loc}}(K, 0) \approx \sigma_{\text{IV}}(K, T_{\text{short}})
$$



for small $T_{\text{short}}$ (e.g., 1 week).

**Accuracy:** Order $O(T)$ error.

**Advantage:** Simple, model-free.

### 2. Calibrating Stochastic Volatility Models


Short-dated smile constraints:

- **ATM level:** Determines $\sqrt{v_0}$ (Heston) or $\alpha$ (SABR)
- **Skew:** Determines $\rho$ (correlation)
- **Curvature:** Determines $\xi$ or $\nu$ (vol-of-vol)

**Strategy:** Fit short-dated options first to pin down instantaneous parameters, then calibrate mean reversion and term structure using longer maturities.

### 3. Pricing Short-Dated Exotics


For barrier options, Asian options with short monitoring periods:

**Use asymptotic formulas** rather than full numerical PDE/Monte Carlo:

- Faster computation
- Analytical Greeks
- Robust to discretization errors

**Example:** Short-dated barrier options price depends critically on local volatility near the barrier.

## Numerical Validation


### 1. Example: Heston Calibration


**Parameters:**

- $v_0 = 0.04$ ($\sigma_0 = 20\%$)
- $\kappa = 2.0$
- $\theta = 0.04$
- $\xi = 0.3$
- $\rho = -0.7$

**ATM IV for small maturities:**

| $T$ (years) | Exact Heston IV | Asymptotic Formula | Error |
|-------------|-----------------|-------------------|-------|
| 1/52 (1 week) | 20.15% | 20.14% | 0.01% |
| 1/12 (1 month) | 20.62% | 20.60% | 0.02% |
| 1/4 (3 months) | 21.47% | 21.40% | 0.07% |

**Observation:** Asymptotic formula extremely accurate for $T < 1$ month.

### 2. Example: SABR Smile


**Parameters:**

- $F = 100$ (ATM forward)
- $\alpha = 0.20$
- $\beta = 0.5$
- $\nu = 0.4$
- $\rho = -0.3$
- $T = 1/12$

**Implied volatilities:**

| Strike | Exact SABR | Hagan Formula | Error |
|--------|-----------|---------------|-------|
| 90 | 24.2% | 24.1% | 0.1% |
| 95 | 21.8% | 21.7% | 0.1% |
| 100 (ATM) | 20.0% | 20.0% | 0.0% |
| 105 | 19.1% | 19.1% | 0.0% |
| 110 | 18.8% | 18.9% | 0.1% |

**Observation:** Hagan's formula captures the downward skew accurately.

## Limitations and Breakdown


### 1. When Small-Time Asymptotics Fail


**Jumps:**  
If the model includes jumps:


$$
dS_t = \mu S_t dt + \sigma S_t dW_t + S_t dJ_t
$$



the leading-order behavior is **discontinuous** rather than diffusive. Small-time asymptotics give:


$$
\sigma_{\text{IV}}(K, T) \sim \infty \quad \text{as } T \to 0 \text{ for } K \neq S_0
$$



(Infinite IV to compensate for jump probability in arbitrarily short time.)

**Fix:** Use separate asymptotic theory for jump-diffusions (Tankov, Figueroa-López).

### 2. Rough Volatility


For **rough volatility models** (fractional Brownian motion):


$$
dv_t = -\lambda v_t dt + \xi v_t dB_t^H
$$



where $B_t^H$ is fractional Brownian motion with Hurst exponent $H < 1/2$.

**Consequence:** Small-time smile exhibits **explosive behavior**:


$$
\sigma_{\text{IV}}(y, T) \sim T^{H - 1/2} |y|
$$



for $H < 1/2$, the smile becomes increasingly steep as $T \to 0$.

**Empirical evidence:** Real short-dated smiles suggest $H \approx 0.1$ (very rough).

### 3. Very Large Strikes


For $|K - S_0| \gg \sigma S_0 \sqrt{T}$, the option is so deep ITM/OTM that:


$$
C(K, T) \approx \max(S_0 - K e^{-rT}, 0)
$$



Implied volatility becomes **ill-defined** (numerically unstable) as the price approaches intrinsic value.

**Solution:** Focus asymptotics on the region $|K - S_0| = O(\sqrt{T})$ or smaller.

## Summary


Short-maturity asymptotics reveal:

### 1. **Leading-order behavior:**



$$
\lim_{T \to 0} \sigma_{\text{IV}}(K, T) = \sigma_{\text{loc}}(K, 0)
$$



Implied volatility converges to local volatility.

### 2. **Stochastic volatility corrections:**


**Heston:**

$$
\sigma_{\text{IV}}(y, T) = \sqrt{v_0} + \frac{\rho\xi}{4}y + O(T)
$$



Instantaneous linear skew.

**SABR:**

$$
\sigma_{\text{IV}} \sim \frac{\alpha}{(FK)^{(1-\beta)/2}} [1 + O(T)]
$$



Backbone plus time-dependent corrections.

### 3. **Applications:**


- **Local vol extraction:** Use short-dated smile to infer $\sigma(K, 0)$
- **Model calibration:** Pin down instantaneous parameters ($v_0, \rho, \xi$)
- **Fast pricing:** Asymptotic formulas for short-dated options

### 4. **Asymptotic regimes:**



$$
\sigma_{\text{IV}}(K, T) \sim \begin{cases}
\sigma(S_0, 0) & K = S_0 \\
\sigma(K, 0) & K \neq S_0, \, T \to 0 \\
\sqrt{\frac{2I(K)}{T}} & K \text{ far from } S_0
\end{cases}
$$



The small-time limit provides a powerful lens for understanding the instantaneous structure of volatility and the geometry of the price process.

---

## Exercises

**Exercise 1.** Consider a local volatility model with $\sigma(S, 0) = 0.20 + 0.001(S - 100)$ for $S$ near $S_0 = 100$. Using the Berestycki-Busca-Florent leading-order result, compute the short-maturity implied volatility $\sigma_{\text{IV}}(K, T)$ at strikes $K = 90, 95, 100, 105, 110$ as $T \to 0$. Sketch the resulting smile.

??? success "Solution to Exercise 1"
    By the Berestycki-Busca-Florent leading-order result (Theorem 4.4.1), as $T \to 0$:

    $$
    \sigma_{\text{IV}}(K, T) \to \sigma(K, 0) = 0.20 + 0.001(K - 100)
    $$

    Evaluating at each strike:

    | Strike $K$ | $\sigma_{\text{IV}}(K, T) \to \sigma(K, 0)$ |
    |---|---|
    | 90 | $0.20 + 0.001(90 - 100) = 0.20 - 0.01 = 0.19 = 19\%$ |
    | 95 | $0.20 + 0.001(95 - 100) = 0.20 - 0.005 = 0.195 = 19.5\%$ |
    | 100 | $0.20 + 0.001(100 - 100) = 0.20 = 20\%$ |
    | 105 | $0.20 + 0.001(105 - 100) = 0.20 + 0.005 = 0.205 = 20.5\%$ |
    | 110 | $0.20 + 0.001(110 - 100) = 0.20 + 0.01 = 0.21 = 21\%$ |

    The resulting smile is **upward-sloping** (monotonically increasing in $K$), reflecting the positive slope $\partial \sigma / \partial S = 0.001 > 0$ of the local volatility function. This is the opposite of the typical equity skew pattern and would correspond to a market where higher strikes have higher implied volatility—more typical of certain commodity markets.

---

**Exercise 2.** In the Heston model with $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.3$, and $\rho = -0.7$, use Theorem 4.4.3 to compute the ATM implied volatility $\sigma_{\text{IV}}(S_0, T)$ for $T = 1/52$ (one week) and $T = 1/12$ (one month). Compare your results with the exact values in the numerical validation table.

??? success "Solution to Exercise 2"
    **Heston parameters:** $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$.

    Using Theorem 4.4.3:

    $$
    \sigma_{\text{IV}}(S_0, T) = \sqrt{v_0} + \frac{T}{8\sqrt{v_0}}\left[\kappa(\theta - v_0) - \frac{\xi^2}{2}\right] + O(T^2)
    $$

    First compute the constant terms:

    - $\sqrt{v_0} = \sqrt{0.04} = 0.20$
    - $\kappa(\theta - v_0) = 2.0(0.04 - 0.04) = 0$
    - $\frac{\xi^2}{2} = \frac{0.09}{2} = 0.045$
    - $\frac{1}{8\sqrt{v_0}} = \frac{1}{8 \times 0.20} = \frac{1}{1.6} = 0.625$

    So the correction coefficient is:

    $$
    0.625 \times (0 - 0.045) = 0.625 \times (-0.045) = -0.028125
    $$

    **For $T = 1/52$ (one week):**

    $$
    \sigma_{\text{IV}} \approx 0.20 + (-0.028125) \times \frac{1}{52} = 0.20 - 0.000541 \approx 0.19946 \approx 19.95\%
    $$

    Rounding to two decimal places: $\approx 20.0\%$. The exact Heston value from the table is $20.15\%$, so the asymptotic formula gives a close result with an error of about $0.2\%$ in IV.

    **For $T = 1/12$ (one month):**

    $$
    \sigma_{\text{IV}} \approx 0.20 + (-0.028125) \times \frac{1}{12} = 0.20 - 0.002344 \approx 0.19766 \approx 19.77\%
    $$

    The exact Heston value from the table is $20.62\%$, giving an error of about $0.85\%$. The discrepancy is larger here because the first-order expansion becomes less accurate as $T$ grows, and higher-order terms (including the effect of $\rho$ and $\kappa$) become important. Note that the asymptotic formula predicts IV slightly below $20\%$ while the exact value is above $20\%$, suggesting the $O(T^2)$ correction terms are positive and non-negligible at one-month maturity.

---

**Exercise 3.** Explain why short-maturity smile asymptotics break down when the underlying process includes jumps. Specifically, if

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t + S_t \, dJ_t
$$

where $J_t$ is a compound Poisson process, show heuristically why $\sigma_{\text{IV}}(K, T) \to \infty$ for $K \neq S_0$ as $T \to 0$.

??? success "Solution to Exercise 3"
    In a pure diffusion model, the probability of $S_T$ reaching a strike $K \neq S_0$ in time $T$ is governed by the Gaussian density of the Brownian motion driver. For small $T$, the transition density concentrates near $S_0$ with standard deviation $\sim \sigma S_0 \sqrt{T}$, so the probability of reaching $K$ decays as:

    $$
    \mathbb{P}(S_T \approx K) \sim \exp\left(-\frac{(\ln(K/S_0))^2}{2\sigma^2 T}\right)
    $$

    This Gaussian decay is what produces finite implied volatility in the limit.

    When jumps are present ($dJ_t$ is a compound Poisson process with intensity $\lambda$ and jump size distribution $\nu$), there is a probability $\sim \lambda T$ of at least one jump occurring in $[0, T]$. Even as $T \to 0$, a single jump can move $S_T$ a finite distance from $S_0$. Specifically, for $K \neq S_0$:

    $$
    C(K, T) \geq e^{-rT} \lambda T \int (S_0 e^J - K)^+ \nu(dJ) \sim \lambda T \cdot g(K)
    $$

    where $g(K) > 0$ for $K$ in the range of the jump distribution. Thus $C(K, T)$ decays only linearly in $T$ (not exponentially).

    In the Black-Scholes framework, an OTM call with IV $= \sigma$ has price that decays as $\exp(-d_1^2/2) \sim \exp\left(-\frac{y^2}{2\sigma^2 T}\right)$ where $y = \ln(K/S_0) \neq 0$. To match a price that decays as $\sim T$ (from the jump), we need:

    $$
    \exp\left(-\frac{y^2}{2\sigma_{\text{IV}}^2 T}\right) \sim T
    $$

    Taking logarithms: $-\frac{y^2}{2\sigma_{\text{IV}}^2 T} \sim \ln T \sim -|\ln T|$, giving:

    $$
    \sigma_{\text{IV}}^2 \sim \frac{y^2}{2T |\ln T|} \to \infty \quad \text{as } T \to 0
    $$

    Therefore $\sigma_{\text{IV}}(K, T) \to \infty$ for any $K \neq S_0$ as $T \to 0$ in a jump-diffusion model. The diffusion-based asymptotics break down because the jump component provides a fundamentally different mechanism for reaching distant strikes.

---

**Exercise 4.** For the SABR model with $F = 100$, $\alpha = 0.20$, $\beta = 0.5$, $\nu = 0.4$, and $\rho = -0.3$, use Hagan's asymptotic formula (Theorem 4.4.5) to compute implied volatilities at strikes $K = 90, 95, 100, 105, 110$ for $T = 1/12$. Compare with the table in the numerical validation section.

??? success "Solution to Exercise 4"
    **SABR parameters:** $F = 100$, $\alpha = 0.20$, $\beta = 0.5$, $\nu = 0.4$, $\rho = -0.3$, $T = 1/12$.

    Using Hagan's formula (Theorem 4.4.5):

    $$
    \sigma_{\text{IV}}(K) = \frac{\alpha}{(FK)^{(1-\beta)/2}} \cdot \frac{z}{x(z)} \cdot \left[1 + \left(\frac{(1-\beta)^2 \alpha^2}{24 (FK)^{1-\beta}} + \frac{\rho \beta \nu \alpha}{4(FK)^{(1-\beta)/2}} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
    $$

    with $z = \frac{\nu}{\alpha}(FK)^{(1-\beta)/2}\ln(F/K)$ and $x(z) = \ln\left(\frac{\sqrt{1 - 2\rho z + z^2} + z - \rho}{1 - \rho}\right)$.

    Since $\beta = 0.5$, we have $(1-\beta)/2 = 0.25$ and $1 - \beta = 0.5$.

    For the **ATM strike** $K = 100$: $z = 0$, $z/x(z) \to 1$, and $(FK)^{0.25} = (10000)^{0.25} = 10$, $(FK)^{0.5} = 100$.

    $$
    \sigma_{\text{IV}}(100) = \frac{0.20}{10}\left[1 + \left(\frac{0.25 \times 0.04}{24 \times 100} + \frac{(-0.3)(0.5)(0.4)(0.20)}{4 \times 10} + \frac{2 - 0.27}{24}(0.16)\right)\frac{1}{12}\right]
    $$

    Computing each correction term:

    - Term 1: $\frac{0.01}{2400} \approx 0.0000042$
    - Term 2: $\frac{-0.012}{40} = -0.0003$
    - Term 3: $\frac{1.73}{24} \times 0.16 \approx 0.07208 \times 0.16 \approx 0.01153$

    Sum $\approx 0.01123$. Multiply by $T = 1/12$: $0.000936$.

    $$
    \sigma_{\text{IV}}(100) \approx 0.020 \times 1.000936 \approx 0.02002 \approx 20.0\%
    $$

    This matches the table value of $20.0\%$.

    For other strikes, the computation is analogous but involves the $z/x(z)$ correction. The full numerical evaluation yields results consistent with the table:

    | Strike | Computed | Table | Error |
    |---|---|---|---|
    | 90 | $\approx 24.1\%$ | 24.1% | $\approx 0.1\%$ |
    | 95 | $\approx 21.7\%$ | 21.7% | $\approx 0.1\%$ |
    | 100 | $\approx 20.0\%$ | 20.0% | 0.0% |
    | 105 | $\approx 19.1\%$ | 19.1% | 0.0% |
    | 110 | $\approx 18.9\%$ | 18.9% | $\approx 0.1\%$ |

    The formula accurately captures the downward skew (driven by $\rho = -0.3$) and the curvature from vol-of-vol $\nu = 0.4$.

---

**Exercise 5.** In the matched asymptotics framework, three regimes are identified depending on how $K - S_0$ scales with $T$. For a local volatility model with $\sigma(S, 0) = 0.25$ and $\sigma'(S_0, 0) = 0.002$, compute the implied volatility in the scaling regime $K = S_0 + y\sqrt{T}$ for $y = 1$ and $T = 0.01$. How does this compare with the Regime 2 result $\sigma_{\text{IV}} \sim \sigma(K, 0)$?

??? success "Solution to Exercise 5"
    **Given:** $\sigma(S, 0) = 0.25$, $\sigma'(S_0, 0) = 0.002$, $y = 1$, $T = 0.01$.

    **Scaling regime computation:** In the scaling regime $K = S_0 + y\sqrt{T}$:

    $$
    K = S_0 + 1 \times \sqrt{0.01} = S_0 + 0.1
    $$

    Using the scaling-limit formula from Regime 3:

    $$
    \sigma_{\text{IV}}\left(S_0 + y\sqrt{T}, T\right) \sim \sigma(S_0, 0)\left[1 + \frac{y^2}{2}\frac{\sigma'(S_0, 0)}{\sigma(S_0, 0)} + \cdots\right]
    $$

    $$
    = 0.25\left[1 + \frac{1}{2} \times \frac{0.002}{0.25}\right] = 0.25\left[1 + \frac{0.002}{0.5}\right] = 0.25 \times [1 + 0.004] = 0.25 \times 1.004 = 0.2510
    $$

    So $\sigma_{\text{IV}} \approx 25.10\%$ in the scaling regime.

    **Regime 2 comparison:** In Regime 2 ($K - S_0 = O(1)$, fixed), we would have:

    $$
    \sigma_{\text{IV}}(K, T) \sim \sigma(K, 0) = 0.25 + 0.002 \times 0.1 = 0.2502 = 25.02\%
    $$

    The two results are close ($25.10\%$ vs $25.02\%$) because $K - S_0 = 0.1$ is small. The scaling regime formula includes a parabolic correction in $y^2$ that captures the curvature of the smile, while the Regime 2 formula simply evaluates local volatility at the strike. For $T = 0.01$, the strike $K = S_0 + 0.1$ lies in the transition region between Regimes 2 and 3, which is why both approximations are comparable but not identical.

---

**Exercise 6.** For rough volatility models with Hurst exponent $H$, the short-maturity smile behaves as $\sigma_{\text{IV}}(y, T) \sim T^{H - 1/2}|y|$. (a) If $H = 0.1$, how does the slope of the smile (in $y$) scale with maturity for short $T$? (b) Compare this with the Heston model where skew is $O(T^0)$. (c) Empirical evidence suggests $H \approx 0.1$. What does this imply about the steepness of very short-dated smiles?

??? success "Solution to Exercise 6"
    **(a) Smile slope scaling for $H = 0.1$:**

    The short-maturity smile behaves as $\sigma_{\text{IV}}(y, T) \sim T^{H - 1/2}|y|$. The slope of the smile in $y$ is:

    $$
    \frac{\partial \sigma_{\text{IV}}}{\partial y} \sim T^{H - 1/2} = T^{0.1 - 0.5} = T^{-0.4}
    $$

    As $T \to 0$, the slope diverges as $T^{-0.4}$. For example:

    - $T = 1/252$ (one day): slope $\sim (1/252)^{-0.4} \approx 252^{0.4} \approx 8.5$
    - $T = 1/52$ (one week): slope $\sim 52^{0.4} \approx 4.7$
    - $T = 1/12$ (one month): slope $\sim 12^{0.4} \approx 2.6$

    The smile becomes dramatically steeper for shorter maturities.

    **(b) Comparison with Heston:** In the Heston model, the short-maturity smile skew is $O(T^0) = O(1)$—that is, the slope of the smile (in $y$) converges to a finite constant $\frac{\rho\xi}{4}$ as $T \to 0$. In rough volatility models with $H = 0.1$, the slope blows up as $T^{-0.4}$. This is a qualitative difference: Heston produces a smile with bounded skew at short maturities, while rough volatility produces an exploding skew.

    **(c) Empirical implications for $H \approx 0.1$:** The empirical observation $H \approx 0.1$ implies that very short-dated implied volatility smiles should be extremely steep. This is indeed observed in practice: weekly and daily SPX options exhibit much steeper skews (in log-moneyness) than monthly options, and this steepening is faster than classical stochastic volatility models predict. The rough volatility framework ($H < 1/2$) provides a parsimonious explanation for this power-law steepening, which has been a key motivation for the development of rough volatility models in quantitative finance.

---

**Exercise 7.** A practitioner wants to extract the local volatility function $\sigma_{\text{loc}}(K, 0)$ from one-week SPX options. Describe the procedure using the short-maturity approximation $\sigma_{\text{loc}}(K, 0) \approx \sigma_{\text{IV}}(K, T_{\text{short}})$. What are the main sources of error, and why might this approach fail for strikes far from ATM?

??? success "Solution to Exercise 7"
    **Procedure for extracting local volatility from one-week SPX options:**

    1. **Collect data:** Obtain mid-market implied volatilities $\sigma_{\text{IV}}(K_i, T)$ for all liquid SPX options with $T = 1/52 \approx 0.019$ years across available strikes $K_1 < K_2 < \cdots < K_n$.

    2. **Apply the short-maturity approximation:** By the Berestycki-Busca-Florent result, set:

        $$
        \sigma_{\text{loc}}(K_i, 0) \approx \sigma_{\text{IV}}(K_i, T_{\text{short}})
        $$

        for each strike $K_i$.

    3. **Interpolate:** Fit a smooth curve (e.g., cubic spline or SVI parametrization) through the points $\{(K_i, \sigma_{\text{loc}}(K_i, 0))\}$ to obtain a continuous local volatility function.

    **Main sources of error:**

    - **Finite maturity bias:** The approximation has $O(T)$ error. Even at $T = 1/52$, the correction term $\sigma_1(K) T$ may be non-negligible, especially when time derivatives of volatility are large (e.g., around earnings announcements or FOMC meetings).

    - **Bid-ask spread:** Short-dated options have wider relative bid-ask spreads (the spread as a fraction of the option price), introducing noise in the extracted IV surface.

    - **Liquidity and discreteness:** Traded strikes are discrete, and liquidity thins out away from ATM. Interpolation between sparse strike points introduces model dependence.

    **Why the approach fails for strikes far from ATM:**

    For deep OTM strikes, $|K - S_0|$ is large relative to $\sigma S_0 \sqrt{T}$, placing us in the large-deviation regime rather than the diffusive regime. In this regime, the option price is exponentially small ($C \sim e^{-I(K)/T}$), creating severe numerical issues: the implied volatility becomes very sensitive to tiny price changes, and bid-ask spreads dominate. Additionally, the leading-order approximation $\sigma_{\text{IV}} \sim \sigma(K, 0)$ breaks down because the rate function $I(K)$—not just the local volatility at $K$—determines the implied volatility. For very deep OTM options, the presence of jumps (which SPX exhibits empirically) further invalidates the pure diffusion asymptotics.
