# Existence and Uniqueness of Implied Volatility


## Introduction


The well-posedness of implied volatility—existence and uniqueness of the inverse pricing map—is fundamental to using volatility as a quoting convention. This section rigorously establishes conditions under which the equation $C_{\text{BS}}(\sigma) = C_{\text{market}}$ admits a unique solution, examines boundary behavior, and explores failure modes when no-arbitrage conditions are violated.

## General Framework for Existence and Uniqueness


### 1. Abstract Formulation


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



### 2. Conditions for Well-Posedness


**Theorem 4.2.1** (Existence and Uniqueness via Monotonicity)  
Let $F: (a, b) \to \mathbb{R}$ be continuous and strictly monotone. Then for any $P \in (\inf_{\sigma \in (a,b)} F(\sigma), \sup_{\sigma \in (a,b)} F(\sigma))$, there exists a unique $\sigma_* \in (a, b)$ such that $F(\sigma_*) = P$.

*Proof.* 

- **Existence:** By the Intermediate Value Theorem, since $F$ is continuous and $P$ lies in the range of $F$
- **Uniqueness:** Strict monotonicity prevents multiple solutions □

### 3. Application to Black-Scholes


For the Black-Scholes call pricing function:


$$
C_{\text{BS}}: (0, \infty) \to \mathbb{R}_+, \quad \sigma \mapsto S e^{-qT} \mathcal{N}(d_1) - K e^{-rT} \mathcal{N}(d_2)
$$



We establish:

1. **Domain:** $(0, \infty)$
2. **Monotonicity:** $\partial C_{\text{BS}}/\partial \sigma > 0$ (vega is positive)
3. **Range:** $(C_{\text{intrinsic}}, C_{\text{max}})$ where:
   - $C_{\text{intrinsic}} = \max(S e^{-qT} - K e^{-rT}, 0)$
   - $C_{\text{max}} = S e^{-qT}$ (undiscounted spot for non-dividend case)

## Detailed Analysis of Range and Limits


### 1. Lower Bound: Intrinsic Value Limit


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
- $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 1$
- $C_{\text{BS}} \to S e^{-qT} - K e^{-rT}$

**Case 2:** $m < 1$ (out-of-the-money forward)

- $\ln m < 0 \Rightarrow d_1, d_2 \to -\infty$
- $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 0$
- $C_{\text{BS}} \to 0$

**Case 3:** $m = 1$ (at-the-money forward)

- Requires more careful analysis using $\Phi(x) = \frac{1}{2} + \frac{1}{\sqrt{2\pi}} x + O(x^3)$ for small $x$
- Limit gives $0$ (zero time value at zero volatility) □

### 2. Upper Bound: Infinite Volatility Limit


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

- $\mathcal{N}(d_1) \to 1$
- $\mathcal{N}(d_2) \to 0$
- $C_{\text{BS}} \to S e^{-qT} \cdot 1 - K e^{-rT} \cdot 0 = S e^{-qT}$ □

**Economic interpretation:** At infinite volatility, the option has value equal to the discounted spot (assuming immediate exercise), as the optionality dominates completely.

### 3. Characterization of Admissible Prices


**Corollary 4.2.1** (Necessary and Sufficient Conditions for Existence)  
Implied volatility exists for a market price $C_{\text{market}}$ if and only if:


$$
\max(S e^{-qT} - K e^{-rT}, 0) < C_{\text{market}} < S e^{-qT}
$$



These are precisely the **static no-arbitrage bounds** on European call prices.

## Strict Monotonicity: Vega Analysis


### 1. Vega Formula


The derivative of the Black-Scholes price with respect to volatility:


$$
\mathcal{V} := \frac{\partial C_{\text{BS}}}{\partial \sigma} = S e^{-qT} \phi(d_1) \sqrt{T}
$$



where $\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is the standard normal density.

### 2. Positivity and Implications


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

### 3. Uniform Lower Bound on Vega


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


### 1. Continuous Dependence on Price


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

### 2. Smoothness via Implicit Function Theorem


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

### 3. Second Derivative: Curvature of Inverse Map


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


### 1. Behavior Near Intrinsic Value


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

### 2. Behavior Near Upper Bound


As $C \to (S e^{-qT})^-$:


$$
\sigma_{\text{IV}}(C) \to \infty
$$



**Proposition 4.2.4** (Divergence Rate)  
As $C \to S e^{-qT}$:


$$
\sigma_{\text{IV}} \sim \sqrt{\frac{2 \ln(1/(1 - C/(S e^{-qT})))}{T}}
$$



### 3. Non-Existence: Arbitrage Violations


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


### 1. Lipschitz Continuity


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

### 2. Condition Number Analysis


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


### 1. Put Options


For European puts, by put-call parity:


$$
P_{\text{BS}}(S, K, T, r, q, \sigma) = C_{\text{BS}}(S, K, T, r, q, \sigma) - S e^{-qT} + K e^{-rT}
$$



Since put-call parity is model-independent:


$$
\sigma_{\text{IV}}^{\text{put}} = \sigma_{\text{IV}}^{\text{call}}
$$



for the same $(K, T)$. The existence and uniqueness analysis is identical, with modified intrinsic value bounds.

### 2. Binary Options


For digital (binary) calls with payoff $\mathbb{1}_{S_T > K}$:


$$
D_{\text{BS}}(\sigma) = e^{-rT} \mathcal{N}(d_2)
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

---

## Exercises

**Exercise 1.** Consider a European call with $S = 50$, $K = 55$, $T = 0.25$, $r = 3\%$, and $q = 0$. Compute the admissible price interval $(C_{\text{intrinsic}}, S e^{-qT})$ for implied volatility to exist. If $C_{\text{market}} = 0.80$, verify that implied volatility exists.

??? success "Solution to Exercise 1"
    With $S = 50$, $K = 55$, $T = 0.25$, $r = 0.03$, and $q = 0$, compute the admissible interval.

    The lower bound (intrinsic value) is:

    $$
    C_{\text{intrinsic}} = \max(S e^{-qT} - K e^{-rT}, 0) = \max\!\left(50 - 55 e^{-0.03 \times 0.25}, 0\right)
    $$

    Computing $K e^{-rT} = 55 \cdot e^{-0.0075} \approx 55 \cdot 0.99252 = 54.589$.

    Since $50 - 54.589 = -4.589 < 0$, the intrinsic value is:

    $$
    C_{\text{intrinsic}} = 0
    $$

    The upper bound is:

    $$
    S e^{-qT} = 50 \cdot e^{0} = 50
    $$

    Therefore the admissible interval is $(0, 50)$.

    Since $C_{\text{market}} = 0.80$ satisfies $0 < 0.80 < 50$, implied volatility exists. This is an out-of-the-money option ($S < K e^{-rT}$), and the positive market price reflects pure time value, consistent with a well-defined positive implied volatility.

---

**Exercise 2.** Prove that the vega of a Black-Scholes call option satisfies $\mathcal{V} > 0$ for all $\sigma > 0$ directly from the formula

$$
\mathcal{V} = S e^{-qT} \phi(d_1) \sqrt{T}
$$

State explicitly which properties of the Gaussian density $\phi$ and the parameters $S$, $T$ are used.

??? success "Solution to Exercise 2"
    The vega formula is:

    $$
    \mathcal{V} = S e^{-qT} \phi(d_1) \sqrt{T}
    $$

    We show each factor is strictly positive:

    1. $S e^{-qT} > 0$: The spot price $S > 0$ by assumption (a traded asset has positive price), and $e^{-qT} > 0$ since the exponential function is always positive.

    2. $\phi(d_1) > 0$: The standard normal density is $\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$. The prefactor $\frac{1}{\sqrt{2\pi}} > 0$ and $e^{-x^2/2} > 0$ for all $x \in \mathbb{R}$ (the exponential function is everywhere positive). Therefore $\phi(d_1) > 0$ regardless of the value of $d_1$.

    3. $\sqrt{T} > 0$: The time to maturity $T > 0$ by assumption (the option has not yet expired), so $\sqrt{T} > 0$.

    Since all three factors are strictly positive, their product is strictly positive:

    $$
    \mathcal{V} = S e^{-qT} \phi(d_1) \sqrt{T} > 0
    $$

    for all admissible parameter values with $S > 0$, $T > 0$, and $\sigma > 0$.

---

**Exercise 3.** Using the Implicit Function Theorem applied to $G(C, \sigma) = C_{\text{BS}}(\sigma) - C = 0$, derive the formula for the second derivative of implied volatility with respect to price:

$$
\frac{d^2 \sigma_{\text{IV}}}{dC^2} = -\frac{d\mathcal{V}/d\sigma}{\mathcal{V}^3}
$$

Evaluate the sign of this expression at ATM (where $d_1 d_2 \approx 0$) and deep OTM (where $d_1 d_2 > 0$).

??? success "Solution to Exercise 3"
    Starting from $G(C, \sigma) = C_{\text{BS}}(\sigma) - C = 0$ and differentiating implicitly with respect to $C$:

    $$
    \frac{\partial G}{\partial C} + \frac{\partial G}{\partial \sigma} \frac{d\sigma_{\text{IV}}}{dC} = 0
    $$

    Since $\frac{\partial G}{\partial C} = -1$ and $\frac{\partial G}{\partial \sigma} = \mathcal{V}$, we get:

    $$
    \frac{d\sigma_{\text{IV}}}{dC} = \frac{1}{\mathcal{V}}
    $$

    Differentiating again with respect to $C$:

    $$
    \frac{d^2\sigma_{\text{IV}}}{dC^2} = \frac{d}{dC}\left(\frac{1}{\mathcal{V}}\right) = -\frac{1}{\mathcal{V}^2} \frac{d\mathcal{V}}{dC} = -\frac{1}{\mathcal{V}^2} \cdot \frac{d\mathcal{V}}{d\sigma} \cdot \frac{d\sigma_{\text{IV}}}{dC} = -\frac{1}{\mathcal{V}^2} \cdot \frac{d\mathcal{V}}{d\sigma} \cdot \frac{1}{\mathcal{V}}
    $$

    Therefore:

    $$
    \frac{d^2\sigma_{\text{IV}}}{dC^2} = -\frac{d\mathcal{V}/d\sigma}{\mathcal{V}^3}
    $$

    The vomma (derivative of vega with respect to $\sigma$) is:

    $$
    \frac{d\mathcal{V}}{d\sigma} = S e^{-qT} \phi(d_1) \sqrt{T} \cdot \frac{d_1 d_2}{\sigma}
    $$

    **At ATM ($S = K e^{-rT}$):** We have $d_1 = \sigma\sqrt{T}/2$ and $d_2 = -\sigma\sqrt{T}/2$, so $d_1 d_2 = -\sigma^2 T/4 < 0$. Therefore $d\mathcal{V}/d\sigma < 0$, and:

    $$
    \frac{d^2\sigma_{\text{IV}}}{dC^2} = -\frac{(\text{negative})}{\mathcal{V}^3} > 0
    $$

    The inverse map is convex at ATM, meaning the implied volatility curve bows upward as a function of price.

    **Deep OTM ($d_1, d_2$ both large and negative, or both positive for deep ITM):** When the option is sufficiently out-of-the-money, $d_1$ and $d_2$ are both negative and large in magnitude, so $d_1 d_2 > 0$. Then $d\mathcal{V}/d\sigma > 0$ and:

    $$
    \frac{d^2\sigma_{\text{IV}}}{dC^2} = -\frac{(\text{positive})}{\mathcal{V}^3} < 0
    $$

    The inverse map is concave for deep OTM options.

---

**Exercise 4.** The condition number for implied volatility extraction is $\kappa = \frac{C}{\sigma_{\text{IV}} \mathcal{V}(\sigma_{\text{IV}})}$. For a near-ATM option with $S = K = 100$, $T = 1$, $r = 0$, and $\sigma_{\text{IV}} = 0.20$, compute $\kappa$ numerically. Then compute $\kappa$ for a deep OTM option with $K = 130$ (same other parameters) and compare. Explain why implied volatility extraction is harder for OTM options.

??? success "Solution to Exercise 4"
    With $S = K = 100$, $T = 1$, $r = 0$, and $\sigma_{\text{IV}} = 0.20$:

    $$
    d_1 = \frac{\ln(100/100) + (0 + 0.20^2/2) \cdot 1}{0.20 \cdot 1} = \frac{0 + 0.02}{0.20} = 0.10
    $$

    The vega is:

    $$
    \mathcal{V} = S \phi(d_1) \sqrt{T} = 100 \cdot \phi(0.10) \cdot 1
    $$

    Computing $\phi(0.10) = \frac{1}{\sqrt{2\pi}} e^{-0.01/2} = 0.39695 \cdot e^{-0.005} \approx 0.39695 \cdot 0.99501 \approx 0.39497$.

    So $\mathcal{V}_{\text{ATM}} = 100 \times 0.39497 = 39.497$.

    The ATM call price is approximately $C_{\text{ATM}} = 100 \cdot \Phi(0.10) - 100 \cdot \Phi(-0.10) \approx 100(0.53983 - 0.46017) = 7.966$.

    The condition number is:

    $$
    \kappa_{\text{ATM}} = \frac{C}{\sigma_{\text{IV}} \cdot \mathcal{V}} = \frac{7.966}{0.20 \times 39.497} \approx \frac{7.966}{7.899} \approx 1.008
    $$

    Now for the deep OTM option with $K = 130$:

    $$
    d_1 = \frac{\ln(100/130) + 0.02}{0.20} = \frac{-0.26236 + 0.02}{0.20} = \frac{-0.24236}{0.20} = -1.2118
    $$

    $$
    d_2 = d_1 - 0.20 = -1.4118
    $$

    Computing $\phi(-1.2118) = \phi(1.2118) \approx 0.19069$.

    The vega is $\mathcal{V}_{\text{OTM}} = 100 \times 0.19069 = 19.069$.

    The OTM call price: $C = 100 \cdot \Phi(-1.2118) - 130 \cdot \Phi(-1.4118) \approx 100(0.1128) - 130(0.0790) \approx 11.28 - 10.27 = 1.01$.

    The condition number is:

    $$
    \kappa_{\text{OTM}} = \frac{1.01}{0.20 \times 19.069} \approx \frac{1.01}{3.814} \approx 0.265
    $$

    In this case, the OTM condition number is actually smaller. However, the key issue for OTM options is not the relative condition number but the **absolute sensitivity**: vega is much smaller for deep OTM options ($\mathcal{V} = 19.07$ vs. $39.50$), so a fixed dollar error in price produces a larger absolute error in implied volatility via $\Delta \sigma \approx \Delta C / \mathcal{V}$. As options move even further OTM, vega shrinks toward zero while prices also shrink, and the ratio $1/\mathcal{V}$ grows, making extraction increasingly ill-conditioned.

---

**Exercise 5.** The zero-volatility limit of the Black-Scholes price requires a case analysis on the forward moneyness $m = S e^{-qT}/(K e^{-rT})$. For the ATM-forward case $m = 1$, show carefully using the Taylor expansion $\Phi(x) \approx \frac{1}{2} + \frac{x}{\sqrt{2\pi}}$ that $\lim_{\sigma \to 0^+} C_{\text{BS}} = 0$.

??? success "Solution to Exercise 5"
    For the ATM-forward case $m = 1$, we have $\ln m = 0$, so:

    $$
    d_1 = \frac{0 + \sigma^2 T / 2}{\sigma \sqrt{T}} = \frac{\sigma \sqrt{T}}{2}
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = -\frac{\sigma \sqrt{T}}{2}
    $$

    As $\sigma \to 0^+$, both $d_1 \to 0^+$ and $d_2 \to 0^-$. Using the Taylor expansion $\Phi(x) \approx \frac{1}{2} + \frac{x}{\sqrt{2\pi}}$ for small $x$:

    $$
    \mathcal{N}(d_1) \approx \frac{1}{2} + \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}}
    $$

    $$
    \mathcal{N}(d_2) \approx \frac{1}{2} - \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}}
    $$

    With $m = 1$, the ATM-forward condition gives $S e^{-qT} = K e^{-rT}$. Substituting into the Black-Scholes formula:

    $$
    C_{\text{BS}} = S e^{-qT} \mathcal{N}(d_1) - K e^{-rT} \mathcal{N}(d_2) = S e^{-qT} \left[\mathcal{N}(d_1) - \mathcal{N}(d_2)\right]
    $$

    Using the approximations:

    $$
    \mathcal{N}(d_1) - \mathcal{N}(d_2) \approx \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}} + \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}} = \frac{\sigma\sqrt{T}}{\sqrt{2\pi}}
    $$

    Therefore:

    $$
    C_{\text{BS}} \approx S e^{-qT} \cdot \frac{\sigma\sqrt{T}}{\sqrt{2\pi}} \to 0 \quad \text{as } \sigma \to 0^+
    $$

    The call price vanishes linearly in $\sigma$, confirming that the ATM-forward option has zero intrinsic value and its time value disappears as volatility goes to zero.

---

**Exercise 6.** For a binary (digital) call option with payoff $\mathbb{1}_{S_T > K}$, the Black-Scholes price is $D_{\text{BS}}(\sigma) = e^{-rT} \mathcal{N}(d_2)$. Show that $\partial D_{\text{BS}} / \partial \sigma$ can be negative for certain values of moneyness and volatility. Provide a specific numerical example where uniqueness of implied volatility fails for a digital option.

??? success "Solution to Exercise 6"
    The digital call price under Black-Scholes is $D_{\text{BS}}(\sigma) = e^{-rT} \mathcal{N}(d_2)$, where:

    $$
    d_2 = \frac{\ln(S/K) + (r - q - \sigma^2/2)T}{\sigma\sqrt{T}}
    $$

    Computing the derivative with respect to $\sigma$:

    $$
    \frac{\partial D_{\text{BS}}}{\partial \sigma} = e^{-rT} \phi(d_2) \frac{\partial d_2}{\partial \sigma}
    $$

    We compute:

    $$
    \frac{\partial d_2}{\partial \sigma} = \frac{-[\ln(S/K) + (r-q)T]}{\sigma^2 \sqrt{T}} - \frac{\sqrt{T}}{2} = -\frac{d_2}{\sigma} - \sqrt{T}
    $$

    More directly, one can write:

    $$
    \frac{\partial D_{\text{BS}}}{\partial \sigma} = -e^{-rT} \phi(d_2) \left(\frac{d_1}{\sigma}\right)
    $$

    using the relation $d_1 = d_2 + \sigma\sqrt{T}$. The sign of $\partial D_{\text{BS}}/\partial\sigma$ is determined by $-d_1$:

    - If $d_1 > 0$ (roughly ITM): $\partial D_{\text{BS}}/\partial\sigma < 0$ (price decreases with $\sigma$)
    - If $d_1 < 0$ (roughly OTM): $\partial D_{\text{BS}}/\partial\sigma > 0$ (price increases with $\sigma$)

    **Numerical example of non-uniqueness:** Take $S = 100$, $K = 100$, $T = 1$, $r = 0.05$, $q = 0$.

    At $\sigma = 0.10$: $d_1 = \frac{0.05 + 0.005}{0.10} = 0.55$, $d_2 = 0.45$, $D = e^{-0.05} \Phi(0.45) \approx 0.9512 \times 0.6736 \approx 0.6408$.

    At $\sigma = 0.50$: $d_1 = \frac{0.05 + 0.125}{0.50} = 0.35$, $d_2 = -0.15$, $D = e^{-0.05} \Phi(-0.15) \approx 0.9512 \times 0.4404 \approx 0.4189$.

    At $\sigma = 2.00$: $d_1 = \frac{0.05 + 2.0}{2.0} = 1.025$, $d_2 = -0.975$, $D = e^{-0.05} \Phi(-0.975) \approx 0.9512 \times 0.1648 \approx 0.1568$.

    Since $D$ is not monotone in $\sigma$ (it first decreases in this ITM-forward example), a price such as $D = 0.40$ could correspond to two different volatility values. The pricing function first moves in one direction and then reverses, so the inverse map is not unique.

---

**Exercise 7.** Implement the Newton-Raphson iteration for implied volatility:

$$
\sigma_{n+1} = \sigma_n - \frac{C_{\text{BS}}(\sigma_n) - C_{\text{market}}}{S \phi(d_1(\sigma_n)) \sqrt{T}}
$$

Starting from $\sigma_0 = 0.50$, compute three iterations for a call with $S = 100$, $K = 100$, $T = 0.5$, $r = 0.02$, $q = 0$, and $C_{\text{market}} = 8.00$. Verify quadratic convergence by examining the ratio of successive errors.

??? success "Solution to Exercise 7"
    With $S = 100$, $K = 100$, $T = 0.5$, $r = 0.02$, $q = 0$, and $C_{\text{market}} = 8.00$.

    **Iteration 0:** $\sigma_0 = 0.50$

    $$
    d_1 = \frac{\ln(1) + (0.02 + 0.125) \times 0.5}{0.50 \sqrt{0.5}} = \frac{0 + 0.0725}{0.35355} = 0.20506
    $$

    $$
    d_2 = 0.20506 - 0.35355 = -0.14849
    $$

    $$
    C_{\text{BS}}(\sigma_0) = 100 \cdot \Phi(0.20506) - 100 e^{-0.01} \Phi(-0.14849)
    $$

    $$
    \approx 100(0.58125) - 99.005(0.44097) \approx 58.125 - 43.659 = 14.466
    $$

    $$
    \mathcal{V} = 100 \cdot \phi(0.20506) \cdot \sqrt{0.5} = 100 \times 0.39109 \times 0.70711 = 27.654
    $$

    $$
    \sigma_1 = 0.50 - \frac{14.466 - 8.00}{27.654} = 0.50 - 0.23382 = 0.26618
    $$

    **Iteration 1:** $\sigma_1 \approx 0.2662$

    $$
    d_1 = \frac{0 + (0.02 + 0.03543) \times 0.5}{0.2662 \times 0.70711} = \frac{0.02771}{0.18822} = 0.14725
    $$

    $$
    d_2 = 0.14725 - 0.18822 = -0.04097
    $$

    $$
    C_{\text{BS}} \approx 100(0.55853) - 99.005(0.48366) \approx 55.853 - 47.884 = 7.969
    $$

    $$
    \mathcal{V} = 100 \times 0.39457 \times 0.70711 = 27.900
    $$

    $$
    \sigma_2 = 0.2662 - \frac{7.969 - 8.00}{27.900} = 0.2662 + 0.00111 = 0.26731
    $$

    **Iteration 2:** $\sigma_2 \approx 0.2673$

    $$
    d_1 = \frac{(0.02 + 0.03572) \times 0.5}{0.2673 \times 0.70711} = \frac{0.02786}{0.18900} = 0.14741
    $$

    $$
    d_2 = 0.14741 - 0.18900 = -0.04159
    $$

    $$
    C_{\text{BS}} \approx 100(0.55860) - 99.005(0.48341) \approx 55.860 - 47.860 = 8.000
    $$

    The method has converged to $\sigma_{\text{IV}} \approx 0.2673$ after three iterations.

    **Quadratic convergence check:** Let $\sigma^* \approx 0.2673$.

    - Error after iteration 0: $|e_0| = |0.500 - 0.2673| = 0.2327$
    - Error after iteration 1: $|e_1| = |0.2662 - 0.2673| = 0.0011$
    - Error after iteration 2: $|e_2| \approx 0.0000$ (essentially converged)

    The ratio $|e_1|/|e_0|^2 \approx 0.0011/0.0541 \approx 0.020$, and $|e_2|/|e_1|^2$ is of similar order. The dramatic reduction in error (from $0.23$ to $0.001$ to effectively $0$) is characteristic of quadratic convergence, where the number of correct digits roughly doubles with each iteration.
