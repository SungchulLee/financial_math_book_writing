# Existence and Uniqueness of Implied Volatility

## Introduction

The well-posedness of implied volatility—existence and uniqueness of the inverse pricing map—is fundamental to using volatility as a quoting convention. This section rigorously establishes conditions under which the equation $C_{\text{BS}}(\sigma) = C_{\text{market}}$ admits a unique solution, examines boundary behavior, and explores failure modes when no-arbitrage conditions are violated.

## General Framework for Existence and Uniqueness

### Abstract Formulation

Consider a pricing functional:


$$
F: \mathcal{D} \subset \mathbb{R}_+ \to \mathbb{R}_+, \quad \sigma \mapsto F(\sigma; \theta)
$$



where $\theta = (S, K, T, r, q)$ represents market parameters (including dividend yield $q$ for generality).

**Definition 4.2.1** (Implied Parameter)  
For a given market price $P_{\text{market}}$, the implied parameter $\sigma_*$ is the solution to:


$$
F(\sigma_*; \theta) = P_{\text{market}}
$$



### Conditions for Well-Posedness

**Theorem 4.2.1** (Existence and Uniqueness via Monotonicity)  
Let $F: (a, b) \to \mathbb{R}$ be continuous and strictly monotone. Then for any $P \in (\inf_{\sigma \in (a,b)} F(\sigma), \sup_{\sigma \in (a,b)} F(\sigma))$, there exists a unique $\sigma_* \in (a, b)$ such that $F(\sigma_*) = P$.

*Proof.* 
- **Existence:** By the Intermediate Value Theorem, since $F$ is continuous and $P$ lies in the range of $F$
- **Uniqueness:** Strict monotonicity prevents multiple solutions □

### Application to Black-Scholes

For the Black-Scholes call pricing function:


$$
C_{\text{BS}}: (0, \infty) \to \mathbb{R}_+, \quad \sigma \mapsto S e^{-qT} \Phi(d_1) - K e^{-rT} \Phi(d_2)
$$



We establish:

1. **Domain:** $(0, \infty)$
2. **Monotonicity:** $\partial C_{\text{BS}}/\partial \sigma > 0$ (vega is positive)
3. **Range:** $(C_{\text{intrinsic}}, C_{\text{max}})$ where:
   - $C_{\text{intrinsic}} = \max(S e^{-qT} - K e^{-rT}, 0)$
   - $C_{\text{max}} = S e^{-qT}$ (undiscounted spot for non-dividend case)

## Detailed Analysis of Range and Limits

### Lower Bound: Intrinsic Value Limit

**Theorem 4.2.2** (Zero Volatility Limit)


$$
\lim_{\sigma \to 0^+} C_{\text{BS}}(S, K, T, r, q, \sigma) = \max(S e^{-qT} - K e^{-rT}, 0)
$$



*Proof.* Consider the forward moneyness $m = \frac{S e^{-qT}}{K e^{-rT}} = \frac{S}{K} e^{(r-q)T}$.

As $\sigma \to 0^+$:


$$
d_1 = \frac{\ln m + \sigma^2 T/2}{\sigma \sqrt{T}} \sim \frac{\ln m}{\sigma \sqrt{T}}
$$




$$
d_2 = d_1 - \sigma\sqrt{T} \sim \frac{\ln m}{\sigma \sqrt{T}}
$$



**Case 1:** $m > 1$ (in-the-money forward)
- $\ln m > 0 \Rightarrow d_1, d_2 \to +\infty$
- $\Phi(d_1), \Phi(d_2) \to 1$
- $C_{\text{BS}} \to S e^{-qT} - K e^{-rT}$

**Case 2:** $m < 1$ (out-of-the-money forward)
- $\ln m < 0 \Rightarrow d_1, d_2 \to -\infty$
- $\Phi(d_1), \Phi(d_2) \to 0$
- $C_{\text{BS}} \to 0$

**Case 3:** $m = 1$ (at-the-money forward)
- Requires more careful analysis using $\Phi(x) = \frac{1}{2} + \frac{1}{\sqrt{2\pi}} x + O(x^3)$ for small $x$
- Limit gives $0$ (zero time value at zero volatility) □

### Upper Bound: Infinite Volatility Limit

**Theorem 4.2.3** (Infinite Volatility Limit)


$$
\lim_{\sigma \to \infty} C_{\text{BS}}(S, K, T, r, q, \sigma) = S e^{-qT}
$$



*Proof.* As $\sigma \to \infty$:


$$
d_1 = \frac{\ln(S/K) + (r - q)T}{\sigma\sqrt{T}} + \frac{\sigma\sqrt{T}}{2} \to +\infty
$$



(dominated by the $+\sigma\sqrt{T}/2$ term)


$$
d_2 = d_1 - \sigma\sqrt{T} = \frac{\ln(S/K) + (r - q)T}{\sigma\sqrt{T}} - \frac{\sigma\sqrt{T}}{2} \to -\infty
$$



Therefore:
- $\Phi(d_1) \to 1$
- $\Phi(d_2) \to 0$
- $C_{\text{BS}} \to S e^{-qT} \cdot 1 - K e^{-rT} \cdot 0 = S e^{-qT}$ □

**Economic interpretation:** At infinite volatility, the option has value equal to the discounted spot (assuming immediate exercise), as the optionality dominates completely.

### Characterization of Admissible Prices

**Corollary 4.2.1** (Necessary and Sufficient Conditions for Existence)  
Implied volatility exists for a market price $C_{\text{market}}$ if and only if:


$$
\max(S e^{-qT} - K e^{-rT}, 0) < C_{\text{market}} < S e^{-qT}
$$



These are precisely the **static no-arbitrage bounds** on European call prices.

## Strict Monotonicity: Vega Analysis

### Vega Formula

The derivative of the Black-Scholes price with respect to volatility:


$$
\mathcal{V} := \frac{\partial C_{\text{BS}}}{\partial \sigma} = S e^{-qT} \phi(d_1) \sqrt{T}
$$



where $\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is the standard normal density.

### Positivity and Implications

**Proposition 4.2.1** (Strict Positivity of Vega)  
For all $(S, K, T, r, q, \sigma)$ with $S > 0$, $T > 0$, $\sigma > 0$:


$$
\mathcal{V}(\sigma) > 0
$$



*Proof.* Each factor is strictly positive:
- $S e^{-qT} > 0$ (discounted spot)
- $\phi(d_1) > 0$ (Gaussian density is positive everywhere)
- $\sqrt{T} > 0$ □

**Corollary 4.2.2** (Strict Monotonicity)  
The map $\sigma \mapsto C_{\text{BS}}(\sigma)$ is strictly increasing on $(0, \infty)$.

### Uniform Lower Bound on Vega

While vega is always positive, its magnitude varies with moneyness and maturity. 

**Proposition 4.2.2** (Vega Bounds)  
For $\sigma \in [\sigma_{\min}, \sigma_{\max}]$ and fixed $(S, K, T)$:


$$
\inf_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \mathcal{V}(\sigma) > 0
$$



*Proof.* On any compact interval $[\sigma_{\min}, \sigma_{\max}]$, the continuous positive function $\mathcal{V}$ attains its infimum, which is strictly positive by Proposition 4.2.1. □

This ensures that the inverse map $C \mapsto \sigma_{\text{IV}}$ has bounded derivative:


$$
\frac{d\sigma_{\text{IV}}}{dC} = \frac{1}{\mathcal{V}(\sigma_{\text{IV}})}
$$



## Continuity and Differentiability of the Inverse Map

### Continuous Dependence on Price

**Theorem 4.2.4** (Continuity of Implied Volatility)  
The implied volatility map:


$$
\mathcal{I}: (C_{\text{intrinsic}}, S e^{-qT}) \to (0, \infty), \quad C \mapsto \sigma_{\text{IV}}
$$



is continuous.

*Proof.* Let $C_n \to C$ with $C_n, C \in (C_{\text{intrinsic}}, S e^{-qT})$. Let $\sigma_n = \mathcal{I}(C_n)$.

By definition: $C_{\text{BS}}(\sigma_n) = C_n$

Since $\{\sigma_n\}$ is bounded (contained in preimage of bounded set under continuous $C_{\text{BS}}$), extract convergent subsequence $\sigma_{n_k} \to \sigma_*$.

By continuity of $C_{\text{BS}}$:


$$
C_{\text{BS}}(\sigma_*) = \lim_{k \to \infty} C_{\text{BS}}(\sigma_{n_k}) = \lim_{k \to \infty} C_{n_k} = C
$$



By uniqueness, $\sigma_* = \mathcal{I}(C)$. Full sequence converges by uniqueness of limit. □

### Smoothness via Implicit Function Theorem

**Theorem 4.2.5** (Differentiability of Implied Volatility)  
The implied volatility is $C^\infty$ smooth with:


$$
\frac{d\sigma_{\text{IV}}}{dC} = \frac{1}{\mathcal{V}(\sigma_{\text{IV}})} = \frac{1}{S e^{-qT} \phi(d_1(\sigma_{\text{IV}})) \sqrt{T}}
$$



*Proof.* Apply the Implicit Function Theorem to:


$$
G(C, \sigma) = C_{\text{BS}}(\sigma) - C = 0
$$



We have:
- $\frac{\partial G}{\partial \sigma} = \mathcal{V}(\sigma) \neq 0$ (non-degeneracy condition satisfied)
- $C_{\text{BS}}$ is $C^\infty$ in $\sigma$

Therefore, the implicit function $\sigma_{\text{IV}}(C)$ is $C^\infty$ with:


$$
\frac{d\sigma_{\text{IV}}}{dC} = -\frac{\partial G/\partial C}{\partial G/\partial \sigma} = -\frac{-1}{\mathcal{V}} = \frac{1}{\mathcal{V}}
$$



Higher derivatives follow by differentiation. □

### Second Derivative: Curvature of Inverse Map

Differentiating the relation $C_{\text{BS}}(\sigma_{\text{IV}}(C)) = C$:


$$
\mathcal{V}(\sigma_{\text{IV}}) \frac{d\sigma_{\text{IV}}}{dC} = 1
$$



Differentiate again:


$$
\frac{d\mathcal{V}}{d\sigma}\bigg|_{\sigma=\sigma_{\text{IV}}} \left(\frac{d\sigma_{\text{IV}}}{dC}\right)^2 + \mathcal{V} \frac{d^2\sigma_{\text{IV}}}{dC^2} = 0
$$




$$
\frac{d^2\sigma_{\text{IV}}}{dC^2} = -\frac{d\mathcal{V}/d\sigma}{\mathcal{V}^3}
$$



where $d\mathcal{V}/d\sigma$ is the **vomma** (or volga):


$$
\frac{d\mathcal{V}}{d\sigma} = S e^{-qT} \phi(d_1) \sqrt{T} \cdot \frac{d_1 d_2}{\sigma}
$$



## Boundary Behavior and Non-Existence Cases

### Behavior Near Intrinsic Value

As $C \to C_{\text{intrinsic}}^+$:


$$
\sigma_{\text{IV}}(C) \to 0^+
$$



The rate of convergence depends on moneyness:

**Proposition 4.2.3** (Rate of Convergence to Zero)  
For deep ITM options with $m = S e^{-qT}/(K e^{-rT}) \gg 1$:


$$
\sigma_{\text{IV}} \sim \sqrt{\frac{2|\ln(C/C_{\text{intrinsic}})|}{T}}
$$



as $C \to C_{\text{intrinsic}}^+$.

### Behavior Near Upper Bound

As $C \to (S e^{-qT})^-$:


$$
\sigma_{\text{IV}}(C) \to \infty
$$



**Proposition 4.2.4** (Divergence Rate)  
As $C \to S e^{-qT}$:


$$
\sigma_{\text{IV}} \sim \sqrt{\frac{2 \ln(1/(1 - C/(S e^{-qT})))}{T}}
$$



### Non-Existence: Arbitrage Violations

Implied volatility fails to exist when:

**Case 1:** $C \leq C_{\text{intrinsic}}$  
Price below intrinsic value violates static arbitrage (buy option, exercise immediately for profit)

**Case 2:** $C \geq S e^{-qT}$  
Price at or above discounted spot (short option, buy stock, guaranteed profit)

In practice, small violations occur due to:
- Bid-ask spreads
- Illiquidity
- Stale quotes
- Microstructure noise

These cases are handled by:
- Clipping prices to admissible range
- Rejecting quotes as non-tradable
- Using robust estimation methods

## Stability Analysis

### Lipschitz Continuity

**Theorem 4.2.6** (Local Lipschitz Continuity)  
On any compact interval $[C_1, C_2] \subset (C_{\text{intrinsic}}, S e^{-qT})$, the implied volatility map is Lipschitz continuous:


$$
|\sigma_{\text{IV}}(C') - \sigma_{\text{IV}}(C)| \leq L |C' - C|
$$



where:


$$
L = \sup_{C \in [C_1, C_2]} \frac{1}{\mathcal{V}(\sigma_{\text{IV}}(C))}
$$



*Proof.* By Mean Value Theorem:


$$
\sigma_{\text{IV}}(C') - \sigma_{\text{IV}}(C) = \frac{d\sigma_{\text{IV}}}{dC}\bigg|_{C=\xi} (C' - C)
$$



for some $\xi \in (C, C')$. The Lipschitz constant is the supremum of the derivative. □

### Condition Number Analysis

The **condition number** for the inversion problem:


$$
\kappa = \left| \frac{C}{\sigma_{\text{IV}}} \frac{d\sigma_{\text{IV}}}{dC} \right| = \frac{C}{\sigma_{\text{IV}} \mathcal{V}(\sigma_{\text{IV}})}
$$



measures sensitivity of implied volatility to relative errors in price.

**Proposition 4.2.5** (Ill-Conditioning Regimes)  
The condition number $\kappa \to \infty$ as:
1. $C \to C_{\text{intrinsic}}^+$ (low volatility regime)
2. $T \to 0$ (expiry approach)

This indicates that implied volatility extraction becomes increasingly sensitive to price errors in these regimes.

## Extension to Other Instruments

### Put Options

For European puts, by put-call parity:


$$
P_{\text{BS}}(S, K, T, r, q, \sigma) = C_{\text{BS}}(S, K, T, r, q, \sigma) - S e^{-qT} + K e^{-rT}
$$



Since put-call parity is model-independent:


$$
\sigma_{\text{IV}}^{\text{put}} = \sigma_{\text{IV}}^{\text{call}}
$$



for the same $(K, T)$. The existence and uniqueness analysis is identical, with modified intrinsic value bounds.

### Binary Options

For digital (binary) calls with payoff $\mathbb{1}_{S_T > K}$:


$$
D_{\text{BS}}(\sigma) = e^{-rT} \Phi(d_2)
$$



**Monotonicity fails** for binary options:


$$
\frac{\partial D_{\text{BS}}}{\partial \sigma} = -e^{-rT} \phi(d_2) \frac{d_2}{\sigma} = -e^{-rT} \phi(d_2) \frac{\ln(S/K) + (r - q - \sigma^2/2)T}{\sigma^2 \sqrt{T}}
$$



This can be positive or negative depending on moneyness, destroying uniqueness of implied volatility for digitals.

## Summary

The existence and uniqueness of implied volatility rests on:

1. **Monotonicity:** Strict positivity of vega ensures injectivity
2. **Range characterization:** Limits $\sigma \to 0, \infty$ match arbitrage bounds
3. **Continuity:** Smooth dependence via Implicit Function Theorem
4. **Stability:** Locally Lipschitz with condition number analysis

Key results:
- Implied volatility exists $\iff$ $C \in (C_{\text{intrinsic}}, S e^{-qT})$
- The inverse map is $C^\infty$ smooth
- Numerical inversion is well-conditioned except near boundaries
- Extension to non-vanilla payoffs requires careful monotonicity verification

This rigorous foundation justifies using implied volatility as a fundamental coordinate system for option pricing.
