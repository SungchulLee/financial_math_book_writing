# Breeden–Litzenberger Formula


## Introduction


The Breeden-Litzenberger formula (1978) establishes a fundamental model-free relationship between European option prices and the risk-neutral probability density of the underlying asset. This remarkable result shows that the entire risk-neutral distribution can be recovered from observable option prices without specifying any particular model for asset dynamics.

## The Fundamental Result


### 1. Statement of the Theorem


**Theorem 4.2.1** (Breeden-Litzenberger Formula)  
Let $C(K, T)$ denote the price of a European call option with strike $K$ and maturity $T$. The risk-neutral probability density function $q(S_T)$ of the terminal asset price $S_T$ is given by:


$$
q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}\bigg|_{K}
$$



Equivalently, for the cumulative distribution function:


$$
Q(K) = \mathbb{P}^{\mathbb{Q}}(S_T \leq K) = e^{rT} \left(1 + \frac{\partial C}{\partial K}\bigg|_{K}\right)
$$



### 2. Interpretation


The second derivative of the call price with respect to strike extracts the **discounted** risk-neutral density:


$$
\frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)
$$



This is a **model-free** result: it holds regardless of whether the underlying follows geometric Brownian motion, jump-diffusion, local volatility, or any other process—it relies only on the absence of arbitrage.

## Derivation via Risk-Neutral Pricing


### 1. Starting Point: Call Price Formula


Under the risk-neutral measure $\mathbb{Q}$, the call price is:


$$
C(K, T) = e^{-rT} \mathbb{E}^{\mathbb{Q}}[\max(S_T - K, 0)]
$$



Expanding the expectation:


$$
C(K, T) = e^{-rT} \int_0^\infty \max(S - K, 0) q(S) dS = e^{-rT} \int_K^\infty (S - K) q(S) dS
$$



### 2. First Derivative: Delta with Respect to Strike


Differentiating under the integral sign:


$$
\frac{\partial C}{\partial K} = e^{-rT} \frac{\partial}{\partial K} \int_K^\infty (S - K) q(S) dS
$$



By Leibniz integral rule:


$$
\frac{\partial C}{\partial K} = e^{-rT} \left[ -\int_K^\infty q(S) dS + (K - K) q(K) \right] = -e^{-rT} \int_K^\infty q(S) dS
$$



Recognizing the tail probability:


$$
\frac{\partial C}{\partial K} = -e^{-rT} \mathbb{P}^{\mathbb{Q}}(S_T > K) = -e^{-rT}(1 - Q(K))
$$



Rearranging:


$$
Q(K) = 1 + e^{rT} \frac{\partial C}{\partial K}
$$



### 3. Second Derivative: Extracting the Density


Differentiating once more:


$$
\frac{\partial^2 C}{\partial K^2} = -e^{-rT} \frac{d}{dK} \int_K^\infty q(S) dS = -e^{-rT} \cdot (-q(K)) = e^{-rT} q(K)
$$



Therefore:


$$
q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}
$$



This completes the derivation. □

## Regularity Conditions


### 1. Assumptions for Validity


The Breeden-Litzenberger formula requires:

1. **Twice differentiability:** $C(K, T)$ must be twice continuously differentiable in $K$
2. **No-arbitrage:** Call prices satisfy monotonicity and convexity constraints
3. **Integrability:** The risk-neutral density $q(K)$ must integrate to 1

### 2. Smoothness of Option Prices


In reality, option prices are observed on a discrete grid and may contain noise. For the formula to apply:

**Proposition 4.2.1** (Regularity of Call Price Surface)  
If the underlying asset price has a continuous risk-neutral density $q(S)$, then the call price function $C(K, T)$ is:

- $C^0$ continuous everywhere
- $C^1$ differentiable everywhere
- $C^2$ twice differentiable almost everywhere

*Proof sketch.* The integral representation:


$$
C(K) = e^{-rT} \int_K^\infty (S - K) q(S) dS
$$



is continuous in $K$ by dominated convergence. First derivative exists by fundamental theorem of calculus. Second derivative exists where $q$ is continuous. □

### 3. Violation of Smoothness


In practice, two issues arise:

1. **Atoms in the distribution:** If $\mathbb{P}^{\mathbb{Q}}(S_T = K_0) > 0$ for some $K_0$, then $q$ contains a Dirac delta:

   $$
   q(S) = q_c(S) + p_0 \delta(S - K_0)
   $$


   The call price has a kink at $K_0$ (non-differentiable first derivative).

2. **Dividend jumps:** Ex-dividend jumps create discontinuities in $S_T$ distribution.

## Connection to Arrow-Debreu Securities


### 1. Digital Options as Building Blocks


An **Arrow-Debreu security** (digital option) pays \$1 if $S_T \in [K, K + dK]$ and 0 otherwise. Its price is:


$$
\text{Digital}(K, dK) = e^{-rT} \mathbb{P}^{\mathbb{Q}}(S_T \in [K, K + dK]) = e^{-rT} q(K) dK
$$



### 2. Static Replication via Butterflies


A digital option can be replicated using a **butterfly spread**:

- Long 1 call at $K - \Delta K$
- Short 2 calls at $K$
- Long 1 call at $K + \Delta K$

Cost of butterfly:


$$
B(K, \Delta K) = C(K - \Delta K) - 2C(K) + C(K + \Delta K)
$$



As $\Delta K \to 0$:


$$
\lim_{\Delta K \to 0} \frac{B(K, \Delta K)}{(\Delta K)^2} = \frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)
$$



Therefore:


$$
\text{Digital}(K, dK) \approx B(K, \Delta K) \quad \text{for small } \Delta K
$$



**Interpretation:** The risk-neutral density can be extracted by observing the prices of butterfly spreads across all strikes.

## Discrete Strike Grid: Finite Differences


### 1. Practical Implementation


In practice, options trade at discrete strikes $K_1 < K_2 < \cdots < K_n$. The density is approximated using finite differences:


$$
q(K_i) \approx e^{rT} \frac{C(K_{i-1}) - 2C(K_i) + C(K_{i+1})}{(\Delta K)^2}
$$



where $\Delta K = K_{i+1} - K_i$ (assuming equal spacing for simplicity).

### 2. Second-Order Accurate Formula


For non-uniform grids, use:


$$
\frac{\partial^2 C}{\partial K^2}\bigg|_{K_i} \approx \frac{2}{K_{i+1} - K_{i-1}} \left( \frac{C(K_{i+1}) - C(K_i)}{K_{i+1} - K_i} - \frac{C(K_i) - C(K_{i-1})}{K_i - K_{i-1}} \right)
$$



This is exact for quadratic functions and $O((\Delta K)^2)$ for smooth $C$.

### 3. Interpolation and Smoothing


To obtain density at arbitrary strikes:

1. **Interpolate call prices:** Use cubic splines or other $C^2$ interpolants
2. **Differentiate analytically:** Compute second derivative of interpolant
3. **Apply Breeden-Litzenberger:** Multiply by $e^{rT}$

**Caution:** Interpolation can introduce spurious oscillations, leading to negative densities (arbitrage). Use monotonicity-preserving and convexity-preserving schemes.

## Extension to Put Options


### 1. Put-Call Symmetry


By put-call parity:


$$
P(K, T) = C(K, T) - S_0 e^{-qT} + K e^{-rT}
$$



Differentiating twice:


$$
\frac{\partial^2 P}{\partial K^2} = \frac{\partial^2 C}{\partial K^2}
$$



Therefore, the Breeden-Litzenberger formula applies equally to puts:


$$
q(K) = e^{rT} \frac{\partial^2 P}{\partial K^2}
$$



### 2. Practical Advantage of Puts


For low strikes ($K \ll S_0$), put prices have higher liquidity and tighter spreads than calls. Using puts for the left wing and calls for the right wing provides more accurate density estimation.

## Consistency Conditions


### 1. Non-Negativity Constraint


Since $q(K) \geq 0$ is a probability density, we require:


$$
\frac{\partial^2 C}{\partial K^2} \geq 0 \quad \text{for all } K
$$



This is the **no-butterfly-arbitrage condition**. Violation indicates:

- Mispriced options
- Bid-ask spread effects
- Model-free arbitrage opportunity

### 2. Normalization: Probability Sums to One


The density must integrate to unity:


$$
\int_0^\infty q(S) dS = 1
$$



Equivalently:


$$
e^{rT} \int_0^\infty \frac{\partial^2 C}{\partial K^2} dK = 1
$$



Integrating by parts:


$$
e^{rT} \left[ \frac{\partial C}{\partial K}\bigg|_0^\infty - \int_0^\infty \delta(K - K') \frac{\partial C}{\partial K} dK' \right]
$$



Using boundary conditions:

- $\frac{\partial C}{\partial K}\big|_{K \to 0} = 0$ (deep ITM call has delta 1)
- $\frac{\partial C}{\partial K}\big|_{K \to \infty} = -e^{-rT}$ (OTM call worthless)

This recovers:


$$
e^{rT}(0 - (-e^{-rT})) = 1 \quad \checkmark
$$



## Applications


### 1. Extracting Risk-Neutral Moments


Once the density is known, compute moments:

**Mean (first moment):**


$$
\mathbb{E}^{\mathbb{Q}}[S_T] = \int_0^\infty S \cdot q(S) dS = S_0 e^{(r - q)T}
$$



(This is the forward price under no-arbitrage.)

**Variance (second central moment):**


$$
\text{Var}^{\mathbb{Q}}(S_T) = \int_0^\infty S^2 q(S) dS - (\mathbb{E}^{\mathbb{Q}}[S_T])^2
$$



**Skewness and kurtosis:** Higher moments characterize tail behavior.

### 2. Model-Free Implied Volatility


Recall (see [§ VIX Formula Derivation](vix_formula_derivation.md)): the Breeden-Litzenberger density underlies the **model-free implied variance** $\sigma_{\text{MF}}^2 = (2e^{rT}/T)\int_0^\infty Q(K)/K^2\,dK$ (variance-swap / VIX integral), giving a volatility estimate independent of Black-Scholes.

### 3. Testing Model Assumptions


Compare the empirical density $q_{\text{market}}(K)$ extracted from option prices to model-implied densities:

- **Black-Scholes:** $q_{\text{BS}}$ is lognormal
- **Local volatility:** $q_{\text{LV}}$ from Dupire equation
- **Stochastic volatility:** $q_{\text{SV}}$ from Heston, SABR, etc.

Deviations indicate model misspecification.

## Relationship to Characteristic Function


### 1. Fourier Inversion


The risk-neutral density can also be expressed via the characteristic function:


$$
q(K) = \frac{1}{2\pi} \int_{-\infty}^\infty e^{-i\omega \ln K} \phi(\omega) d\omega
$$



where $\phi(\omega) = \mathbb{E}^{\mathbb{Q}}[e^{i\omega \ln S_T}]$ is the characteristic function.

### 2. Carr-Madan Formula


Carr and Madan (1999) show that call prices can be recovered from the characteristic function:


$$
C(K) = \frac{e^{-rT}}{\pi} \int_0^\infty \text{Re}\left[ \frac{e^{-i\omega \ln K} \phi(\omega - i)}{(\omega^2 + 1)} \right] d\omega
$$



Combining with Breeden-Litzenberger provides an alternative path: $\phi \to C \to q$.

## Numerical Examples


### 1. Example 1: Black-Scholes Density


For $S_T \sim \text{Lognormal}(\mu, \sigma^2 T)$ with $\mu = (r - q - \sigma^2/2)T$:


$$
q_{\text{BS}}(K) = \frac{1}{K \sigma \sqrt{2\pi T}} \exp\left( -\frac{(\ln K - \ln S_0 - \mu)^2}{2\sigma^2 T} \right)
$$



Compute $C(K)$ via Black-Scholes formula, then verify:


$$
e^{rT} \frac{\partial^2 C_{\text{BS}}}{\partial K^2} = q_{\text{BS}}(K)
$$



**Verification:**


$$
\frac{\partial C_{\text{BS}}}{\partial K} = -e^{-rT} \mathcal{N}(d_2)
$$




$$
\frac{\partial^2 C_{\text{BS}}}{\partial K^2} = -e^{-rT} \phi(d_2) \frac{\partial d_2}{\partial K} = e^{-rT} \frac{\phi(d_2)}{K \sigma \sqrt{T}}
$$



Since $\phi(d_2) = \frac{1}{\sqrt{2\pi}} e^{-d_2^2/2}$ and $d_2 = \frac{\ln(S_0/K) + (r - q - \sigma^2/2)T}{\sigma\sqrt{T}}$:


$$
e^{rT} \frac{\partial^2 C_{\text{BS}}}{\partial K^2} = \frac{1}{K \sigma \sqrt{2\pi T}} e^{-d_2^2/2} = q_{\text{BS}}(K) \quad \checkmark
$$



### 2. Example 2: Discrete Grid Recovery


Given market call prices $\{(K_i, C_i)\}_{i=1}^n$:

1. Fit smooth interpolant (e.g., cubic spline with no-arbitrage constraints)
2. Compute $C''(K_i)$ from interpolant
3. Multiply by $e^{rT}$ to get $q(K_i)$
4. Verify $\int q(K) dK \approx 1$ using trapezoidal rule

## Extensions and Generalizations


### 1. Time-Dependent Interest Rates


For stochastic interest rates, the discount factor $e^{-rT}$ is replaced by the price of a zero-coupon bond $B(0, T)$:


$$
q(K) = B(0, T)^{-1} \frac{\partial^2 C}{\partial K^2}
$$



### 2. Dividends and Jumps


Discrete dividends create point masses in the density. Continuous dividend yield $q$ modifies the forward price but preserves the Breeden-Litzenberger structure.

### 3. Multi-Asset Options


For basket options, the joint risk-neutral density can be extracted using higher-dimensional derivatives:


$$
q(K_1, K_2) = e^{rT} \frac{\partial^2 C}{\partial K_1 \partial K_2}
$$



This requires options on the basket at a two-dimensional grid of strikes.

## Limitations and Practical Considerations


### 1. Sparse Strike Grid


Real markets have limited strike coverage, especially in the wings. Extrapolation is required, introducing model dependence.

### 2. Bid-Ask Spreads


Using mid-prices can lead to inconsistencies. Best practice:

- Use bid prices for sold options (butterfly short legs)
- Use ask prices for bought options (butterfly long legs)
- Result: Conservative density estimate

### 3. Negative Probabilities


If $\partial^2 C / \partial K^2 < 0$ at some strike, the extracted "density" is negative—indicating arbitrage or measurement error. Solutions:

- Regularization (smooth to enforce convexity)
- Projection onto arbitrage-free space
- Discard suspect data points

### 4. Tail Behavior


Breeden-Litzenberger requires knowledge of $C(K)$ for all $K \in [0, \infty)$. In practice:

- Lower tail: $K \to 0$ may have no traded options
- Upper tail: $K \to \infty$ requires extrapolation

Standard approach: assume parametric tail (e.g., power law, exponential decay).

## Summary


The Breeden-Litzenberger formula:


$$
q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}
$$



provides a **model-free** method to extract the risk-neutral probability density from option prices. Key properties:

- **No model assumption:** Holds for any arbitrage-free market
- **Direct observable:** Second derivative of call prices
- **Consistency check:** Non-negativity equivalent to no-butterfly-arbitrage
- **Complete information:** Full distribution recovered from option surface

Applications include:

- Risk-neutral moment calculation
- Model validation and comparison
- Density forecasting and tail risk assessment
- Static replication of exotic payoffs

The formula forms the foundation for model-free results in option pricing, establishing that the option market **is** the probability distribution under the risk-neutral measure.

---

## Exercises

**Exercise 1.** Starting from the risk-neutral pricing formula $C(K, T) = e^{-rT} \int_K^\infty (S - K) q(S) \, dS$, derive the Breeden-Litzenberger formula $q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}$ by differentiating twice with respect to $K$. State clearly which differentiation rule you use at each step.

??? success "Solution to Exercise 1"
    Starting from the risk-neutral pricing formula:

    $$
    C(K, T) = e^{-rT} \int_K^\infty (S - K) q(S) \, dS
    $$

    **First derivative.** Apply the Leibniz integral rule to differentiate with respect to the lower limit $K$ and the integrand:

    $$
    \frac{\partial C}{\partial K} = e^{-rT} \left[ \underbrace{-(K - K) q(K)}_{\text{boundary term } = 0} + \int_K^\infty \frac{\partial}{\partial K}(S - K) q(S) \, dS \right]
    $$

    The boundary term vanishes because the integrand $(S - K)$ evaluates to zero at $S = K$. The partial derivative of the integrand gives $-1$, so:

    $$
    \frac{\partial C}{\partial K} = -e^{-rT} \int_K^\infty q(S) \, dS = -e^{-rT} \mathbb{P}^{\mathbb{Q}}(S_T > K)
    $$

    **Second derivative.** Differentiate again with respect to $K$ using the fundamental theorem of calculus:

    $$
    \frac{\partial^2 C}{\partial K^2} = -e^{-rT} \frac{d}{dK} \int_K^\infty q(S) \, dS = -e^{-rT} \cdot (-q(K)) = e^{-rT} q(K)
    $$

    Solving for the density:

    $$
    q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}
    $$

    This is the Breeden-Litzenberger formula. The first step used the Leibniz rule for differentiating an integral with a variable limit, and the second step used the fundamental theorem of calculus.

---

**Exercise 2.** Three call options with the same maturity $T = 0.5$ and $r = 3\%$ have prices $C(95) = 10.20$, $C(100) = 7.50$, $C(105) = 5.30$. Using the finite-difference approximation $q(K) \approx e^{rT} \frac{C(K - \Delta K) - 2C(K) + C(K + \Delta K)}{(\Delta K)^2}$ with $\Delta K = 5$, estimate the risk-neutral density $q(100)$. Verify that $q(100) > 0$.

??? success "Solution to Exercise 2"
    Given $T = 0.5$, $r = 0.03$, $C(95) = 10.20$, $C(100) = 7.50$, $C(105) = 5.30$, and $\Delta K = 5$, apply the finite-difference approximation:

    $$
    q(100) \approx e^{rT} \frac{C(95) - 2C(100) + C(105)}{(\Delta K)^2}
    $$

    Compute the numerator of the finite difference:

    $$
    C(95) - 2C(100) + C(105) = 10.20 - 2(7.50) + 5.30 = 10.20 - 15.00 + 5.30 = 0.50
    $$

    Compute the denominator:

    $$
    (\Delta K)^2 = 25
    $$

    Compute the discount factor:

    $$
    e^{rT} = e^{0.03 \times 0.5} = e^{0.015} \approx 1.01511
    $$

    Therefore:

    $$
    q(100) \approx 1.01511 \times \frac{0.50}{25} = 1.01511 \times 0.02 \approx 0.02030
    $$

    Since $q(100) \approx 0.0203 > 0$, the non-negativity condition is satisfied, confirming no butterfly arbitrage at this strike.

---

**Exercise 3.** The cumulative distribution function is given by $Q(K) = e^{rT}(1 + \frac{\partial C}{\partial K})$. If the call price function is $C(K) = e^{-rT}(F - K + \sigma_0 \sqrt{T} \phi(d))$ for some approximation near ATM, show that $Q(F) \approx 0.5$ (the probability of finishing in the money is near 50% for an ATM option).

??? success "Solution to Exercise 3"
    The CDF is given by $Q(K) = e^{rT}(1 + \frac{\partial C}{\partial K})$. We need to show that $Q(F) \approx 0.5$ for an ATM option (where $K = F$, the forward price).

    From the first derivative result in the Breeden-Litzenberger derivation:

    $$
    \frac{\partial C}{\partial K} = -e^{-rT} \mathbb{P}^{\mathbb{Q}}(S_T > K)
    $$

    At $K = F$ (at-the-money forward):

    $$
    Q(F) = e^{rT}\left(1 + \frac{\partial C}{\partial K}\bigg|_{K=F}\right) = e^{rT}\left(1 - e^{-rT}\mathbb{P}^{\mathbb{Q}}(S_T > F)\right) = e^{rT} - \mathbb{P}^{\mathbb{Q}}(S_T > F)
    $$

    Alternatively, directly:

    $$
    Q(F) = \mathbb{P}^{\mathbb{Q}}(S_T \leq F)
    $$

    For a distribution that is approximately symmetric around the forward (in particular, the lognormal distribution with small $\sigma\sqrt{T}$), we have $\mathbb{P}^{\mathbb{Q}}(S_T \leq F) \approx 0.5$. More precisely, in the Black-Scholes model:

    $$
    Q(F) = \mathcal{N}(d_2)\big|_{K=F} = \Phi\left(\frac{\sigma\sqrt{T}}{2}\right)
    $$

    Wait — correcting: $d_2 = \frac{\ln(F/K) + (-\sigma^2/2)T}{\sigma\sqrt{T}}$. At $K = F$, $\ln(F/F) = 0$, so $d_2 = -\frac{\sigma\sqrt{T}}{2}$. Thus:

    $$
    Q(F) = \Phi\left(-\frac{\sigma_0\sqrt{T}}{2}\right)
    $$

    For small $\sigma_0\sqrt{T}$, $\Phi(-\sigma_0\sqrt{T}/2) \approx 0.5 - \frac{\sigma_0\sqrt{T}}{2\sqrt{2\pi}} \approx 0.5$. The deviation from $0.5$ is of order $\sigma_0\sqrt{T}$, which is small for short maturities or moderate volatility. Hence $Q(F) \approx 0.5$.

---

**Exercise 4.** Using the Breeden-Litzenberger formula, explain why the butterfly spread $C(K - \Delta K) - 2C(K) + C(K + \Delta K) \geq 0$ is equivalent to the non-negativity of the risk-neutral density. What economic interpretation does a negative density have, and why is it inconsistent with no-arbitrage?

??? success "Solution to Exercise 4"
    The butterfly spread cost is:

    $$
    B(K, \Delta K) = C(K - \Delta K) - 2C(K) + C(K + \Delta K)
    $$

    As $\Delta K \to 0$, this approaches:

    $$
    B(K, \Delta K) \approx \frac{\partial^2 C}{\partial K^2} (\Delta K)^2
    $$

    By the Breeden-Litzenberger formula, $\frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)$, so:

    $$
    B(K, \Delta K) \approx e^{-rT} q(K) (\Delta K)^2
    $$

    **Equivalence:** The butterfly spread price is non-negative ($B \geq 0$) if and only if $\frac{\partial^2 C}{\partial K^2} \geq 0$, which is equivalent to $q(K) \geq 0$.

    **Economic interpretation of a negative density:** If $q(K) < 0$ at some strike $K$, then $B(K, \Delta K) < 0$, meaning the butterfly spread has a negative cost. Since the butterfly payoff is always non-negative (it pays $(K - |S_T - K|)^+ / \Delta K \geq 0$ approximately), buying it for a negative price yields a guaranteed non-negative payoff for a positive cash inflow. This is a pure arbitrage: risk-free profit with no initial investment. Such a situation is inconsistent with the no-arbitrage assumption, which requires that any claim with non-negative payoff must have a non-negative price.

---

**Exercise 5.** Suppose the risk-neutral density extracted from SPX options is bimodal (two peaks). What does this indicate about the market's view of future price distribution? Provide a market scenario (such as a pending binary event) that would produce a bimodal risk-neutral density.

??? success "Solution to Exercise 5"
    A **bimodal** risk-neutral density has two distinct peaks, meaning the market assigns elevated probability to two separate price regions while assigning lower probability to intermediate prices.

    **Interpretation:** The market expects the underlying to end up near one of two distinct levels, with relatively low probability of finishing in between. This indicates the market is pricing a **binary outcome** — an event whose resolution will push the price decisively in one of two directions.

    **Market scenario:** Consider a pharmaceutical company awaiting FDA approval for a key drug:

    - **Approval (positive outcome):** The stock jumps to approximately \$120 (first peak)
    - **Rejection (negative outcome):** The stock drops to approximately \$60 (second peak)
    - **Current price:** \$90

    The risk-neutral density would show peaks near \$60 and \$120 with a trough near \$90. Other examples include pending merger announcements (deal closes vs. falls apart), election outcomes affecting regulated industries, and central bank rate decisions with two likely scenarios.

    In the implied volatility space, a bimodal density corresponds to an unusually pronounced smile with very high wing volatilities and a relatively low ATM volatility, creating a deep U-shape.

---

**Exercise 6.** Derive the relationship $\frac{\partial C}{\partial K} = -e^{-rT} \mathbb{P}^{\mathbb{Q}}(S_T > K)$ from the risk-neutral pricing formula. Use this to show that the call delta with respect to strike gives the (discounted) complement of the CDF. Verify that $\frac{\partial C}{\partial K} \to 0$ as $K \to 0$ and $\frac{\partial C}{\partial K} \to -e^{-rT}$ as $K \to \infty$.

??? success "Solution to Exercise 6"
    Starting from the risk-neutral call pricing formula:

    $$
    C(K, T) = e^{-rT} \int_K^\infty (S - K) q(S) \, dS
    $$

    Differentiate with respect to $K$ using the Leibniz rule:

    $$
    \frac{\partial C}{\partial K} = e^{-rT} \left[-(K - K)q(K) + \int_K^\infty (-1) q(S) \, dS\right] = -e^{-rT} \int_K^\infty q(S) \, dS
    $$

    Since $\int_K^\infty q(S) \, dS = \mathbb{P}^{\mathbb{Q}}(S_T > K)$:

    $$
    \frac{\partial C}{\partial K} = -e^{-rT} \mathbb{P}^{\mathbb{Q}}(S_T > K)
    $$

    This shows the call delta with respect to strike equals the discounted complement of the CDF. Equivalently, $-e^{rT}\frac{\partial C}{\partial K} = 1 - Q(K)$, the survival function.

    **Boundary verification:**

    As $K \to 0$: Every positive terminal value exceeds $K = 0$, so $\mathbb{P}^{\mathbb{Q}}(S_T > 0) = 1$ (assuming $S_T > 0$ a.s.). But the call at $K = 0$ is just the forward itself, $C(0) = e^{-rT}F$, and $\frac{\partial C}{\partial K}\big|_{K=0} = -e^{-rT}(1) = -e^{-rT}$.

    Correction: Re-examining, we note from the formula $\frac{\partial C}{\partial K} = -e^{-rT}\mathbb{P}^{\mathbb{Q}}(S_T > K)$. As $K \to 0^+$, $\mathbb{P}^{\mathbb{Q}}(S_T > K) \to 1$, so $\frac{\partial C}{\partial K} \to -e^{-rT}$.

    As $K \to \infty$: $\mathbb{P}^{\mathbb{Q}}(S_T > K) \to 0$, so $\frac{\partial C}{\partial K} \to 0$.

    These match the economic intuition: a deep ITM call ($K \to 0$) loses exactly $e^{-rT}$ per unit increase in strike (it behaves like a short bond minus strike), while a deep OTM call ($K \to \infty$) is insensitive to strike changes.

---

**Exercise 7.** The Breeden-Litzenberger formula requires the second derivative $\frac{\partial^2 C}{\partial K^2}$, but market data provides prices at discrete strikes. Compare three numerical methods for estimating this derivative: (a) centered finite differences, (b) fitting a smooth parametric curve (such as SVI) and differentiating analytically, (c) kernel smoothing. Discuss the tradeoff between accuracy and robustness to noise for each method.

??? success "Solution to Exercise 7"
    **(a) Centered finite differences:**

    $$
    \frac{\partial^2 C}{\partial K^2}\bigg|_{K_i} \approx \frac{C(K_{i-1}) - 2C(K_i) + C(K_{i+1})}{(\Delta K)^2}
    $$

    - **Accuracy:** Second-order accurate $O((\Delta K)^2)$ for smooth functions. Uses only three adjacent data points.
    - **Robustness:** Very sensitive to noise. Numerical differentiation amplifies errors: if option prices have noise of magnitude $\epsilon$, the second derivative estimate has noise of order $\epsilon / (\Delta K)^2$. With $\Delta K = 5$ and $\epsilon = \$0.05$, the noise in the density estimate is $0.05/25 = 0.002$, which can be comparable to the density value itself.
    - **Tradeoff:** Simple and unbiased for smooth data, but unreliable with noisy market quotes.

    **(b) Parametric curve fitting (e.g., SVI):**

    Fit a smooth parametric model such as the SVI (Stochastic Volatility Inspired) parametrization to the implied volatility data:

    $$
    \sigma_{\text{IV}}^2(k) = a + b\left[\rho(k - m) + \sqrt{(k - m)^2 + s^2}\right]
    $$

    where $k = \ln(K/F)$. Convert to call prices and differentiate analytically.

    - **Accuracy:** Provides smooth analytical derivatives. The accuracy depends on how well the parametric form matches the true smile shape. If the model is correct, accuracy is excellent.
    - **Robustness:** Highly robust to noise because the fit averages over many data points. However, model misspecification introduces systematic bias — the extracted density inherits the shape constraints of the parametric family.
    - **Tradeoff:** Most robust to noise but introduces model dependence. The density can only take shapes permitted by the parametric family.

    **(c) Kernel smoothing:**

    Smooth the call prices using a kernel regression:

    $$
    \hat{C}(K) = \frac{\sum_i K_h(K - K_i) C(K_i)}{\sum_i K_h(K - K_i)}
    $$

    where $K_h$ is a kernel function with bandwidth $h$, then differentiate the smoothed function.

    - **Accuracy:** Non-parametric, so no model bias. Accuracy depends on bandwidth selection: too small preserves noise, too large over-smooths and flattens the density.
    - **Robustness:** Intermediate between (a) and (b). More robust than raw finite differences but less constrained than parametric fits. Does not automatically enforce no-arbitrage conditions (may produce negative densities).
    - **Tradeoff:** Flexible and fairly robust, but requires careful bandwidth tuning. The bias-variance tradeoff is controlled by bandwidth: larger $h$ reduces variance but increases bias.

    **Summary:** Method (a) is best for dense, clean data. Method (b) is best for sparse, noisy data where the parametric form is trusted. Method (c) offers a middle ground with no parametric assumptions but requires bandwidth selection.
