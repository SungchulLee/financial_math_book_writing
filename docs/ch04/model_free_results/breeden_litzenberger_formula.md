# Breeden–Litzenberger Formula

## Introduction

The Breeden-Litzenberger formula (1978) establishes a fundamental model-free relationship between European option prices and the risk-neutral probability density of the underlying asset. This remarkable result shows that the entire risk-neutral distribution can be recovered from observable option prices without specifying any particular model for asset dynamics.

## The Fundamental Result

### Statement of the Theorem

**Theorem 4.2.1** (Breeden-Litzenberger Formula)  
Let $C(K, T)$ denote the price of a European call option with strike $K$ and maturity $T$. The risk-neutral probability density function $q(S_T)$ of the terminal asset price $S_T$ is given by:

$$
q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}\bigg|_{K}
$$

Equivalently, for the cumulative distribution function:

$$
Q(K) = \mathbb{P}^{\mathbb{Q}}(S_T \leq K) = e^{rT} \left(1 + \frac{\partial C}{\partial K}\bigg|_{K}\right)
$$

### Interpretation

The second derivative of the call price with respect to strike extracts the **discounted** risk-neutral density:

$$
\frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)
$$

This is a **model-free** result: it holds regardless of whether the underlying follows geometric Brownian motion, jump-diffusion, local volatility, or any other process—it relies only on the absence of arbitrage.

## Derivation via Risk-Neutral Pricing

### Starting Point: Call Price Formula

Under the risk-neutral measure $\mathbb{Q}$, the call price is:

$$
C(K, T) = e^{-rT} \mathbb{E}^{\mathbb{Q}}[\max(S_T - K, 0)]
$$

Expanding the expectation:

$$
C(K, T) = e^{-rT} \int_0^\infty \max(S - K, 0) q(S) dS = e^{-rT} \int_K^\infty (S - K) q(S) dS
$$

### First Derivative: Delta with Respect to Strike

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

### Second Derivative: Extracting the Density

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

### Assumptions for Validity

The Breeden-Litzenberger formula requires:

1. **Twice differentiability:** $C(K, T)$ must be twice continuously differentiable in $K$
2. **No-arbitrage:** Call prices satisfy monotonicity and convexity constraints
3. **Integrability:** The risk-neutral density $q(K)$ must integrate to 1

### Smoothness of Option Prices

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

### Violation of Smoothness

In practice, two issues arise:

1. **Atoms in the distribution:** If $\mathbb{P}^{\mathbb{Q}}(S_T = K_0) > 0$ for some $K_0$, then $q$ contains a Dirac delta:
   $$
   q(S) = q_c(S) + p_0 \delta(S - K_0)
   $$
   The call price has a kink at $K_0$ (non-differentiable first derivative).

2. **Dividend jumps:** Ex-dividend jumps create discontinuities in $S_T$ distribution.

## Connection to Arrow-Debreu Securities

### Digital Options as Building Blocks

An **Arrow-Debreu security** (digital option) pays \$1 if $S_T \in [K, K + dK]$ and 0 otherwise. Its price is:

$$
\text{Digital}(K, dK) = e^{-rT} \mathbb{P}^{\mathbb{Q}}(S_T \in [K, K + dK]) = e^{-rT} q(K) dK
$$

### Static Replication via Butterflies

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

### Practical Implementation

In practice, options trade at discrete strikes $K_1 < K_2 < \cdots < K_n$. The density is approximated using finite differences:

$$
q(K_i) \approx e^{rT} \frac{C(K_{i-1}) - 2C(K_i) + C(K_{i+1})}{(\Delta K)^2}
$$

where $\Delta K = K_{i+1} - K_i$ (assuming equal spacing for simplicity).

### Second-Order Accurate Formula

For non-uniform grids, use:

$$
\frac{\partial^2 C}{\partial K^2}\bigg|_{K_i} \approx \frac{2}{K_{i+1} - K_{i-1}} \left( \frac{C(K_{i+1}) - C(K_i)}{K_{i+1} - K_i} - \frac{C(K_i) - C(K_{i-1})}{K_i - K_{i-1}} \right)
$$

This is exact for quadratic functions and $O((\Delta K)^2)$ for smooth $C$.

### Interpolation and Smoothing

To obtain density at arbitrary strikes:

1. **Interpolate call prices:** Use cubic splines or other $C^2$ interpolants
2. **Differentiate analytically:** Compute second derivative of interpolant
3. **Apply Breeden-Litzenberger:** Multiply by $e^{rT}$

**Caution:** Interpolation can introduce spurious oscillations, leading to negative densities (arbitrage). Use monotonicity-preserving and convexity-preserving schemes.

## Extension to Put Options

### Put-Call Symmetry

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

### Practical Advantage of Puts

For low strikes ($K \ll S_0$), put prices have higher liquidity and tighter spreads than calls. Using puts for the left wing and calls for the right wing provides more accurate density estimation.

## Consistency Conditions

### Non-Negativity Constraint

Since $q(K) \geq 0$ is a probability density, we require:

$$
\frac{\partial^2 C}{\partial K^2} \geq 0 \quad \text{for all } K
$$

This is the **no-butterfly-arbitrage condition**. Violation indicates:
- Mispriced options
- Bid-ask spread effects
- Model-free arbitrage opportunity

### Normalization: Probability Sums to One

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

### Extracting Risk-Neutral Moments

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

### Model-Free Implied Volatility

The Breeden-Litzenberger density can be used to define a **model-free implied variance**:

$$
\sigma_{\text{MF}}^2 = \frac{2e^{rT}}{T} \int_0^\infty \frac{C(K) - \max(S_0 e^{-qT} - K e^{-rT}, 0)}{K^2} dK
$$

This integral of option prices across all strikes provides a volatility estimate independent of Black-Scholes.

### Testing Model Assumptions

Compare the empirical density $q_{\text{market}}(K)$ extracted from option prices to model-implied densities:
- **Black-Scholes:** $q_{\text{BS}}$ is lognormal
- **Local volatility:** $q_{\text{LV}}$ from Dupire equation
- **Stochastic volatility:** $q_{\text{SV}}$ from Heston, SABR, etc.

Deviations indicate model misspecification.

## Relationship to Characteristic Function

### Fourier Inversion

The risk-neutral density can also be expressed via the characteristic function:

$$
q(K) = \frac{1}{2\pi} \int_{-\infty}^\infty e^{-i\omega \ln K} \phi(\omega) d\omega
$$

where $\phi(\omega) = \mathbb{E}^{\mathbb{Q}}[e^{i\omega \ln S_T}]$ is the characteristic function.

### Carr-Madan Formula

Carr and Madan (1999) show that call prices can be recovered from the characteristic function:

$$
C(K) = \frac{e^{-rT}}{\pi} \int_0^\infty \text{Re}\left[ \frac{e^{-i\omega \ln K} \phi(\omega - i)}{(\omega^2 + 1)} \right] d\omega
$$

Combining with Breeden-Litzenberger provides an alternative path: $\phi \to C \to q$.

## Numerical Examples

### Example 1: Black-Scholes Density

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
\frac{\partial C_{\text{BS}}}{\partial K} = -e^{-rT} \Phi(d_2)
$$

$$
\frac{\partial^2 C_{\text{BS}}}{\partial K^2} = -e^{-rT} \phi(d_2) \frac{\partial d_2}{\partial K} = e^{-rT} \frac{\phi(d_2)}{K \sigma \sqrt{T}}
$$

Since $\phi(d_2) = \frac{1}{\sqrt{2\pi}} e^{-d_2^2/2}$ and $d_2 = \frac{\ln(S_0/K) + (r - q - \sigma^2/2)T}{\sigma\sqrt{T}}$:

$$
e^{rT} \frac{\partial^2 C_{\text{BS}}}{\partial K^2} = \frac{1}{K \sigma \sqrt{2\pi T}} e^{-d_2^2/2} = q_{\text{BS}}(K) \quad \checkmark
$$

### Example 2: Discrete Grid Recovery

Given market call prices $\{(K_i, C_i)\}_{i=1}^n$:

1. Fit smooth interpolant (e.g., cubic spline with no-arbitrage constraints)
2. Compute $C''(K_i)$ from interpolant
3. Multiply by $e^{rT}$ to get $q(K_i)$
4. Verify $\int q(K) dK \approx 1$ using trapezoidal rule

## Extensions and Generalizations

### Time-Dependent Interest Rates

For stochastic interest rates, the discount factor $e^{-rT}$ is replaced by the price of a zero-coupon bond $B(0, T)$:

$$
q(K) = B(0, T)^{-1} \frac{\partial^2 C}{\partial K^2}
$$

### Dividends and Jumps

Discrete dividends create point masses in the density. Continuous dividend yield $q$ modifies the forward price but preserves the Breeden-Litzenberger structure.

### Multi-Asset Options

For basket options, the joint risk-neutral density can be extracted using higher-dimensional derivatives:

$$
q(K_1, K_2) = e^{rT} \frac{\partial^2 C}{\partial K_1 \partial K_2}
$$

This requires options on the basket at a two-dimensional grid of strikes.

## Limitations and Practical Considerations

### Sparse Strike Grid

Real markets have limited strike coverage, especially in the wings. Extrapolation is required, introducing model dependence.

### Bid-Ask Spreads

Using mid-prices can lead to inconsistencies. Best practice:
- Use bid prices for sold options (butterfly short legs)
- Use ask prices for bought options (butterfly long legs)
- Result: Conservative density estimate

### Negative Probabilities

If $\partial^2 C / \partial K^2 < 0$ at some strike, the extracted "density" is negative—indicating arbitrage or measurement error. Solutions:
- Regularization (smooth to enforce convexity)
- Projection onto arbitrage-free space
- Discard suspect data points

### Tail Behavior

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
