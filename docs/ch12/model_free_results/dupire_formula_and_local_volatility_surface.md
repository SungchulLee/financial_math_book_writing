# Dupire's Formula and Local Volatility Surface


## Introduction


Dupire's formula (1994) provides a fundamental model-free relationship between observable European option prices and the **local volatility function** $\sigma_{\text{loc}}(S, t)$. This remarkable result shows that there exists a unique diffusion process consistent with all observed option prices, and the instantaneous volatility of this process can be directly computed from option prices without model calibration.

## The Local Volatility Model


### 1. Model Specification


The **local volatility model** assumes the underlying asset follows:


$$
dS_t = (r - q) S_t dt + \sigma_{\text{loc}}(S_t, t) S_t dW_t
$$



where:

- $\sigma_{\text{loc}}(S, t)$ is a deterministic function of spot and time
- $r$ is the risk-free rate
- $q$ is the dividend yield
- $W_t$ is a standard Brownian motion under the risk-neutral measure $\mathbb{Q}$

**Key distinction from Black-Scholes:** Volatility depends on both $(S, t)$ rather than being constant.

### 2. Forward Kolmogorov Equation


The probability density $p(S, t; S_0, 0)$ of $S_t$ given $S_0$ at time 0 satisfies the **forward Kolmogorov equation** (Fokker-Planck equation):


$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}\left[(r - q) S p\right] + \frac{1}{2} \frac{\partial^2}{\partial S^2}\left[\sigma_{\text{loc}}^2(S, t) S^2 p\right]
$$



This describes the evolution of the probability distribution forward in time.

### 3. Connection to Option Pricing


The call option price is:


$$
C(S_0, K, T) = e^{-rT} \int_0^\infty \max(S - K, 0) p(S, T; S_0, 0) dS
$$



The key insight: if we know $C(K, T)$ for all strikes and maturities, we can invert this relationship to find $\sigma_{\text{loc}}(S, t)$.

## Dupire's Formula: Main Result


### 1. Theorem Statement


**Theorem 4.2.2** (Dupire's Formula)  
The local volatility function can be extracted from the call price surface via:


$$
\sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + q C + (r - q) K \frac{\partial C}{\partial K}}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}}
$$



Equivalently, using forward price $F = S_0 e^{(r-q)T}$ and eliminating drift terms:


$$
\sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T}}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}}
$$



when expressed in forward coordinates.

**Interpretation:** Local volatility at strike $K$ and time $T$ is determined entirely by:

- Time derivative of call price (theta)
- Second strike derivative (gamma via Breeden-Litzenberger)

### 2. Alternative Forms


**Form 1** (Spot-based):


$$
\sigma_{\text{loc}}^2(S, t) = \frac{C_T + (r - q) S C_S + q C}{\frac{1}{2} S^2 C_{SS}}
$$



where subscripts denote partial derivatives.

**Form 2** (Forward-based, most common):


$$
\sigma_{\text{loc}}^2(K, T) = 2 \frac{\frac{\partial C}{\partial T}}{\frac{\partial^2 C}{\partial K^2}} \cdot \frac{1}{K^2}
$$



**Form 3** (In terms of implied volatility):


$$
\sigma_{\text{loc}}^2(K, T) = \frac{\sigma_{\text{IV}}^2 + 2\sigma_{\text{IV}} T \frac{\partial \sigma_{\text{IV}}}{\partial T} + 2(r - q) K T \sigma_{\text{IV}} \frac{\partial \sigma_{\text{IV}}}{\partial K}}{\left(1 + K d_1 \sqrt{T} \frac{\partial \sigma_{\text{IV}}}{\partial K}\right)^2 + \sigma_{\text{IV}} K^2 T \left(\frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2} - d_1 \sqrt{T} \left(\frac{\partial \sigma_{\text{IV}}}{\partial K}\right)^2\right)}
$$



where $d_1 = \frac{\ln(S_0/K) + (r - q + \sigma_{\text{IV}}^2/2)T}{\sigma_{\text{IV}}\sqrt{T}}$.

## Derivation via Forward Kolmogorov Equation


### 1. Step 1: Call Price PDE


The call option price satisfies the backward Kolmogorov equation:


$$
\frac{\partial C}{\partial t} + (r - q) S \frac{\partial C}{\partial S} + \frac{1}{2} \sigma_{\text{loc}}^2(S, t) S^2 \frac{\partial^2 C}{\partial S^2} - r C = 0
$$



with terminal condition $C(S, T, T) = \max(S - K, 0)$.

### 2. Step 2: Differentiate with Respect to Maturity


Fix strike $K$ and differentiate the PDE with respect to $T$ (treating $T$ as a parameter):


$$
\frac{\partial}{\partial T}\left(\frac{\partial C}{\partial t}\right) + (r - q) S \frac{\partial}{\partial T}\left(\frac{\partial C}{\partial S}\right) + \frac{1}{2} \sigma_{\text{loc}}^2(S, T) S^2 \frac{\partial}{\partial T}\left(\frac{\partial^2 C}{\partial S^2}\right) - r \frac{\partial C}{\partial T} = 0
$$



### 3. Step 3: Evaluate at S = K, t = T


At expiry, the call payoff creates a kink at $S = K$:

- $C(S, T, T) = \max(S - K, 0)$
- $\frac{\partial C}{\partial S}\big|_{S=K, t=T} = 1$ (jump in derivative)
- $\frac{\partial^2 C}{\partial S^2}\big|_{S=K, t=T}$ contains Dirac delta

Using the **Dupire argument**: differentiate the option price with respect to maturity and evaluate at the money ($S = K$), giving:


$$
\frac{\partial C}{\partial T}\bigg|_{S=K} = \frac{1}{2} \sigma_{\text{loc}}^2(K, T) K^2 \frac{\partial^2 C}{\partial K^2}\bigg|_{S=K, t=T}
$$



Solving for $\sigma_{\text{loc}}^2$:


$$
\sigma_{\text{loc}}^2(K, T) = 2 \frac{\frac{\partial C}{\partial T}}{\frac{\partial^2 C}{\partial K^2}} \cdot \frac{1}{K^2}
$$



### 4. Step 4: Include Drift Terms (Full Formula)


For general $(S, t)$, the complete derivation includes drift corrections:


$$
\sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + q C + (r - q) K \frac{\partial C}{\partial K}}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}}
$$



The numerator adjusts for the fact that the underlying drifts at rate $r - q$ under the risk-neutral measure. □

## Alternative Derivation: Tanaka's Formula


### 1. Occupation Density Approach


Consider the **local time** $L_t^K$ of the process $S_t$ at level $K$. Tanaka's formula gives:


$$
(S_T - K)^+ = (S_0 - K)^+ + \int_0^T \mathbb{1}_{S_t > K} dS_t + \frac{1}{2} L_T^K
$$



Taking expectations:


$$
C(S_0, K, T) = e^{-rT} \mathbb{E}\left[(S_0 - K)^+ + \int_0^T \mathbb{1}_{S_t > K} (r - q) S_t dt + \frac{1}{2} L_T^K\right]
$$



The local time satisfies:


$$
\mathbb{E}[L_T^K] = \int_0^T \sigma_{\text{loc}}^2(K, t) K^2 p(K, t; S_0, 0) dt
$$



Differentiating with respect to $T$ and using Breeden-Litzenberger:


$$
\frac{\partial C}{\partial T} = \frac{1}{2} \sigma_{\text{loc}}^2(K, T) K^2 \cdot e^{-rT} p(K, T) = \frac{1}{2} \sigma_{\text{loc}}^2(K, T) K^2 \frac{\partial^2 C}{\partial K^2}
$$



This recovers Dupire's formula. □

## Properties of the Local Volatility Surface


### 1. Uniqueness


**Theorem 4.2.3** (Uniqueness of Local Volatility)  
Given a complete arbitrage-free European call price surface $C(K, T)$ for all $K > 0$, $T > 0$, there exists a unique local volatility function $\sigma_{\text{loc}}(S, t)$ such that the diffusion:


$$
dS_t = (r - q) S_t dt + \sigma_{\text{loc}}(S_t, t) S_t dW_t
$$



reproduces the entire call price surface.

*Proof sketch.* The forward Kolmogorov equation is a parabolic PDE with unique solution given smooth initial and boundary conditions. The call prices determine the terminal distribution uniquely via Breeden-Litzenberger. Dupire's formula inverts this relationship. □

### 2. Calibration to Market Prices


The local volatility model is **perfectly calibrated** to vanilla options by construction:

- Input: Market call prices $C_{\text{market}}(K, T)$
- Output: Local volatility surface $\sigma_{\text{loc}}(K, T)$ via Dupire's formula
- Result: Model prices exactly match market prices for all $(K, T)$

This is in stark contrast to parametric models (e.g., Heston) which minimize pricing errors but rarely achieve exact fit.

### 3. Relationship to Implied Volatility


The local volatility at strike $K$ and maturity $T$ is **not** equal to the implied volatility $\sigma_{\text{IV}}(K, T)$:


$$
\sigma_{\text{loc}}(K, T) \neq \sigma_{\text{IV}}(K, T)
$$



**Intuition:** 

- **Implied volatility** is the constant volatility that, when plugged into Black-Scholes, matches the market price
- **Local volatility** is the instantaneous volatility the process will have if it reaches level $K$ at time $T$

The relationship is complex and involves the entire smile surface.

### 4. Smile-Consistent Dynamics


In Black-Scholes, all options on the same underlying have the same implied volatility. In local volatility:

- Each strike-maturity pair has its own implied volatility
- The **smile** $\sigma_{\text{IV}}(K)$ and **term structure** $\sigma_{\text{IV}}(T)$ are endogenous
- The model generates smile dynamics: as spot moves, the smile changes

## Numerical Implementation


### 1. Finite Difference Formula


On a discrete grid $(K_i, T_j)$, approximate derivatives using centered differences:


$$
\frac{\partial C}{\partial T}\bigg|_{K_i, T_j} \approx \frac{C(K_i, T_{j+1}) - C(K_i, T_{j-1})}{T_{j+1} - T_{j-1}}
$$




$$
\frac{\partial^2 C}{\partial K^2}\bigg|_{K_i, T_j} \approx \frac{C(K_{i+1}, T_j) - 2C(K_i, T_j) + C(K_{i-1}, T_j)}{(\Delta K)^2}
$$



Then:


$$
\sigma_{\text{loc}}^2(K_i, T_j) = \frac{2}{ K_i^2} \cdot \frac{C(K_i, T_{j+1}) - C(K_i, T_{j-1})}{T_{j+1} - T_{j-1}} \cdot \frac{(\Delta K)^2}{C(K_{i+1}, T_j) - 2C(K_i, T_j) + C(K_{i-1}, T_j)}
$$



### 2. Stability Issues


**Problem 1: Noise amplification**  
Taking derivatives of noisy data amplifies errors. Small errors in $C$ lead to large errors in $\sigma_{\text{loc}}$.

**Solution:** 

- Smooth the call price surface before differentiation (e.g., spline interpolation)
- Use total variation regularization
- Impose arbitrage-free constraints (convexity in $K$, monotonicity in $T$)

**Problem 2: Division by small numbers**  
Near the wings, $\frac{\partial^2 C}{\partial K^2} \approx 0$, causing $\sigma_{\text{loc}} \to \infty$.

**Solution:**

- Extrapolate wings using parametric forms (e.g., power law tails)
- Cap local volatility at reasonable bounds
- Use regularization penalties for extreme values

### 3. Interpolation of Call Prices


To compute Dupire's formula, we need smooth $C(K, T)$:

1. **Interpolate in strike:** For each maturity, fit cubic splines in $K$ with:
   - Monotonicity constraint: $C_K \leq 0$
   - Convexity constraint: $C_{KK} \geq 0$

2. **Interpolate in maturity:** For each strike, fit smooth curve in $T$:
   - Monotonicity constraint: $C_T \geq 0$

3. **Use arbitrage-free interpolation schemes:**
   - SVI (Stochastic Volatility Inspired) parametrization
   - SSVI (Surface SVI) for joint $(K, T)$ fitting

## Connection to Implied Volatility


### 1. Converting Implied Volatility to Local Volatility


Given the implied volatility surface $\sigma_{\text{IV}}(K, T)$, compute local volatility via:

**Step 1:** Convert $\sigma_{\text{IV}}(K, T)$ to call prices using Black-Scholes formula

**Step 2:** Compute derivatives:

$$
C_T, \quad C_K, \quad C_{KK}
$$



**Step 3:** Apply Dupire's formula

### 2. Explicit Formula in IV Space


Gyöngy's formula provides a direct relationship:


$$
\sigma_{\text{loc}}^2(K, T) = \frac{\sigma_{\text{IV}}^2 + 2\sigma_{\text{IV}} T \left(\frac{\partial \sigma_{\text{IV}}}{\partial T} + (r - q) K \frac{\partial \sigma_{\text{IV}}}{\partial K}\right)}{1 + 2 d_1 K\sqrt{T} \frac{\partial \sigma_{\text{IV}}}{\partial K} + K^2 T \left(\frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2} - d_1^2 \sqrt{T} \left(\frac{\partial \sigma_{\text{IV}}}{\partial K}\right)^2\right)}
$$



This is computationally convenient when starting from implied volatility data.

### 3. ATM Approximation


At-the-money ($K = F = S_0 e^{(r-q)T}$), a useful approximation:


$$
\sigma_{\text{loc}}^2(F, T) \approx \sigma_{\text{IV}}^2(F, T) + 2 T \sigma_{\text{IV}}(F, T) \frac{\partial \sigma_{\text{IV}}}{\partial T}\bigg|_{K=F}
$$



**Interpretation:** Local volatility at the forward is approximately the implied volatility plus a correction for the term structure slope.

## Forward Equation Perspective


### 1. Forward Kolmogorov PDE


The density $p(K, T)$ satisfies:


$$
\frac{\partial p}{\partial T} = \frac{1}{2} \frac{\partial^2}{\partial K^2}\left[\sigma_{\text{loc}}^2(K, T) K^2 p(K, T)\right]
$$



(assuming drift-free coordinates with $F = S_0 e^{(r-q)T}$).

Using Breeden-Litzenberger $p(K, T) = e^{rT} \frac{\partial^2 C}{\partial K^2}$:


$$
\frac{\partial}{\partial T}\left(e^{rT} \frac{\partial^2 C}{\partial K^2}\right) = \frac{1}{2} \frac{\partial^2}{\partial K^2}\left[\sigma_{\text{loc}}^2(K, T) K^2 e^{rT} \frac{\partial^2 C}{\partial K^2}\right]
$$



This is a PDE for $C$ in terms of $\sigma_{\text{loc}}$. Dupire's formula inverts this PDE to solve for $\sigma_{\text{loc}}$ given $C$.

### 2. Existence of Solution


**Theorem 4.2.4** (Well-Posedness)  
If $C(K, T)$ is:

1. $C^2$ in $K$ and $C^1$ in $T$
2. Satisfies no-arbitrage constraints ($C_K \leq 0$, $C_{KK} \geq 0$, $C_T \geq 0$)
3. Has suitable boundary and initial conditions

then the local volatility $\sigma_{\text{loc}}(K, T)$ given by Dupire's formula is:

- Positive
- Bounded
- Yields a well-posed SDE

## Applications and Limitations


### 1. Advantages of Local Volatility


1. **Perfect calibration:** Matches all vanilla option prices exactly
2. **Model-free:** No parameters to estimate (given the surface)
3. **Tractable:** Amenable to PDE and Monte Carlo methods
4. **Complete market:** Unique pricing for exotics (in theory)

### 2. Limitations


1. **Smile dynamics mismatch:**  
   Local volatility generates **sticky-strike** smile dynamics (smile is constant in strike space). Market exhibits **sticky-delta** or hybrid behavior.

2. **Instantaneous volatility unrealistic:**  
   Extracted $\sigma_{\text{loc}}(S, t)$ can be very large (>100%) or very small (<5%) in extreme regions—difficult to justify economically.

3. **Path-dependent pricing issues:**  
   Exotic options (barriers, cliquets) are often mispriced by local volatility due to incorrect correlation between spot and volatility.

4. **Forward smile:**  
   Local volatility predicts a flat forward smile, contradicting market data showing persistent smile.

5. **Leverage effect:**  
   The negative correlation between returns and volatility (leverage effect) is not captured—local vol is purely deterministic.

### 3. Hybrid Models


To address limitations, practitioners use:

- **Stochastic local volatility (SLV):** Combine local volatility with stochastic volatility (e.g., Heston + local vol)
- **Implied tree models:** Discrete analogs that exactly fit vanilla prices
- **Jump-diffusion + local vol:** Add jumps to capture tail risk

## Comparison with Implied Volatility


| Feature | Implied Volatility | Local Volatility |
|---------|-------------------|------------------|
| **Definition** | BS $\sigma$ matching market price for one option | Instantaneous vol if $S_t = K$ at time $t$ |
| **Uniqueness** | Unique for each $(K, T)$ | Unique function $\sigma_{\text{loc}}(S, t)$ |
| **Calibration** | Quotes individual options | Calibrates entire surface |
| **Dynamics** | Static (no evolution model) | Fully specifies diffusion dynamics |
| **Computation** | Newton-Raphson on BS formula | Differentiate entire call surface |

## Summary


Dupire's formula:


$$
\sigma_{\text{loc}}^2(K, T) = \frac{2 \frac{\partial C}{\partial T}}{K^2 \frac{\partial^2 C}{\partial K^2}}
$$



establishes a **model-free, one-to-one relationship** between:

- Observable European call prices $C(K, T)$
- Local volatility function $\sigma_{\text{loc}}(S, t)$

**Key insights:**

1. **Uniqueness:** Every arbitrage-free call surface corresponds to exactly one local vol diffusion
2. **Model-free extraction:** No calibration—direct formula from derivatives of $C$
3. **Perfect fit:** Local vol model exactly reproduces market vanilla prices
4. **Complementarity with B-L:** Breeden-Litzenberger extracts density, Dupire extracts dynamics

**Practical workflow:**


$$
\text{Market Prices} \xrightarrow{\text{B-L}} \text{Risk-Neutral Density} \xrightarrow{\text{Dupire}} \text{Local Volatility Surface}
$$



Together, these model-free results allow complete characterization of the arbitrage-free price surface and the underlying dynamics without assuming a specific parametric model.

---

## Exercises

**Exercise 1.** Starting from the Dupire formula

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + (r - q) K \frac{\partial C}{\partial K} + q C}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}}
$$

explain the role of each term in the numerator. What happens to $\sigma_{\text{loc}}^2$ if $\frac{\partial^2 C}{\partial K^2} \to 0$? Why does this indicate a problem with the input data?

??? success "Solution to Exercise 1"
    The Dupire formula is:

    $$
    \sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + (r - q) K \frac{\partial C}{\partial K} + q C}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}}
    $$

    **Role of each numerator term:**

    - $\frac{\partial C}{\partial T}$: This is the **time value decay** (negative of theta) of the call option. It captures how the option value changes as maturity increases, reflecting the additional variance accumulated over a longer horizon. This is the dominant term and represents the rate at which option value grows with maturity due to increased uncertainty.

    - $(r - q) K \frac{\partial C}{\partial K}$: This is the **drift correction**. Under the risk-neutral measure, the underlying drifts at rate $r - q$. The term $\frac{\partial C}{\partial K}$ is related to the digital option payoff (the probability of finishing ITM). This correction accounts for the fact that the forward price shifts over time, which affects where the density is centered.

    - $qC$: This is the **dividend correction**. A continuous dividend yield $q$ reduces the forward price and affects the present value of the option. When $q > 0$, the call is worth less due to dividend leakage, and this term compensates for that effect in the local volatility extraction.

    **What happens when $\frac{\partial^2 C}{\partial K^2} \to 0$:** The denominator $\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}$ approaches zero, causing $\sigma_{\text{loc}}^2 \to \infty$. By the Breeden-Litzenberger formula, $\frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)$, so a vanishing second derivative means the risk-neutral density is near zero at that strike. This occurs deep in the wings where very few paths of the underlying are expected to reach. The divergence of local volatility indicates that the input call price surface lacks sufficient curvature (information) at that strike, making the local volatility extraction numerically unstable. In practice, this signals either sparse data, noisy quotes, or extrapolation artifacts in the wings.

---

**Exercise 2.** For a flat implied volatility surface $\sigma_{\text{IV}}(K, T) = \sigma_0$ (constant), show that Dupire's formula yields $\sigma_{\text{loc}}(K, T) = \sigma_0$ for all $(K, T)$. This verifies that the Black-Scholes model is the unique local volatility model with flat smile.

??? success "Solution to Exercise 2"
    If $\sigma_{\text{IV}}(K, T) = \sigma_0$ for all $(K, T)$, then the call price is given by the Black-Scholes formula:

    $$
    C(K, T) = S_0 e^{-qT}\mathcal{N}(d_1) - K e^{-rT}\mathcal{N}(d_2)
    $$

    with $d_1 = \frac{\ln(S_0/K) + (r - q + \sigma_0^2/2)T}{\sigma_0\sqrt{T}}$ and $d_2 = d_1 - \sigma_0\sqrt{T}$.

    The Black-Scholes call satisfies the PDE:

    $$
    \frac{\partial C}{\partial T} + (r - q)S\frac{\partial C}{\partial S} + \frac{1}{2}\sigma_0^2 S^2 \frac{\partial^2 C}{\partial S^2} - rC = 0
    $$

    Rewriting in terms of strike derivatives (using the duality between spot and strike), the numerator of Dupire's formula evaluates to:

    $$
    \frac{\partial C}{\partial T} + (r - q)K\frac{\partial C}{\partial K} + qC = \frac{1}{2}\sigma_0^2 K^2 \frac{\partial^2 C}{\partial K^2}
    $$

    This follows from the forward PDE (Dupire equation) satisfied by Black-Scholes prices. Substituting into Dupire's formula:

    $$
    \sigma_{\text{loc}}^2(K, T) = \frac{\frac{1}{2}\sigma_0^2 K^2 \frac{\partial^2 C}{\partial K^2}}{\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}} = \sigma_0^2
    $$

    Therefore $\sigma_{\text{loc}}(K, T) = \sigma_0$ for all $(K, T)$. This confirms that the Black-Scholes model (constant volatility) is the unique local volatility model that produces a flat implied volatility surface.

---

**Exercise 3.** Given call prices $C(K, T)$ on a discrete grid, describe how to numerically compute all partial derivatives needed for Dupire's formula. Use centered finite differences: $\frac{\partial C}{\partial T} \approx \frac{C(K, T + \Delta T) - C(K, T - \Delta T)}{2\Delta T}$ and similar expressions for strike derivatives. What grid spacing issues arise for deep OTM options?

??? success "Solution to Exercise 3"
    The partial derivatives needed for Dupire's formula are $\frac{\partial C}{\partial T}$, $\frac{\partial C}{\partial K}$, and $\frac{\partial^2 C}{\partial K^2}$.

    **Time derivative** (centered finite difference):

    $$
    \frac{\partial C}{\partial T}\bigg|_{(K_i, T_j)} \approx \frac{C(K_i, T_{j+1}) - C(K_i, T_{j-1})}{T_{j+1} - T_{j-1}}
    $$

    For boundary maturities ($j = 1$ or $j = n$), use forward or backward differences.

    **First strike derivative** (centered finite difference):

    $$
    \frac{\partial C}{\partial K}\bigg|_{(K_i, T_j)} \approx \frac{C(K_{i+1}, T_j) - C(K_{i-1}, T_j)}{K_{i+1} - K_{i-1}}
    $$

    **Second strike derivative** (centered finite difference):

    $$
    \frac{\partial^2 C}{\partial K^2}\bigg|_{(K_i, T_j)} \approx \frac{C(K_{i+1}, T_j) - 2C(K_i, T_j) + C(K_{i-1}, T_j)}{(\Delta K)^2}
    $$

    For non-uniform strike spacing, use the generalized formula:

    $$
    \frac{\partial^2 C}{\partial K^2}\bigg|_{K_i} \approx \frac{2}{K_{i+1} - K_{i-1}}\left(\frac{C(K_{i+1}) - C(K_i)}{K_{i+1} - K_i} - \frac{C(K_i) - C(K_{i-1})}{K_i - K_{i-1}}\right)
    $$

    **Grid spacing issues for deep OTM options:**

    1. **Sparse strikes:** Deep OTM strikes are often widely spaced, reducing finite-difference accuracy.
    2. **Small option prices:** Deep OTM options have prices near zero, so relative errors in quotes are large. Finite differences amplify these errors.
    3. **Denominator instability:** $\frac{\partial^2 C}{\partial K^2} \approx 0$ in the wings, causing $\sigma_{\text{loc}}^2$ to blow up (division by near-zero).
    4. **Time derivative noise:** For deep OTM options, $C(K, T)$ changes slowly with $T$, making $\frac{\partial C}{\partial T}$ difficult to estimate reliably.
    5. **Bid-ask contamination:** Deep OTM options have wide bid-ask spreads relative to their midprice, introducing substantial noise into the finite-difference estimates.

---

**Exercise 4.** The forward Kolmogorov (Fokker-Planck) equation for the local volatility model is $\frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}[(r-q)Sp] + \frac{1}{2}\frac{\partial^2}{\partial S^2}[\sigma_{\text{loc}}^2 S^2 p]$. Explain why this is a "forward" equation (evolving in maturity $T$), and contrast it with the "backward" Black-Scholes PDE. Why is the forward equation more natural for calibration from market data?

??? success "Solution to Exercise 4"
    The **forward Kolmogorov equation** (Fokker-Planck) evolves the probability density $p(S, T)$ forward in the maturity variable $T$:

    $$
    \frac{\partial p}{\partial T} = -\frac{\partial}{\partial S}[(r-q)Sp] + \frac{1}{2}\frac{\partial^2}{\partial S^2}[\sigma_{\text{loc}}^2 S^2 p]
    $$

    Given an initial condition $p(S, 0) = \delta(S - S_0)$, this PDE determines the density at any future time $T > 0$. It is a "forward" equation because it propagates information from the known initial state into the future.

    The **backward Black-Scholes PDE** evolves the option price backward from the terminal condition:

    $$
    \frac{\partial C}{\partial t} + (r-q)S\frac{\partial C}{\partial S} + \frac{1}{2}\sigma_{\text{loc}}^2 S^2 \frac{\partial^2 C}{\partial S^2} - rC = 0
    $$

    Given a terminal condition $C(S, T) = \max(S - K, 0)$ at maturity, this PDE determines the price at earlier times $t < T$. It propagates information backward from the known payoff.

    **Why the forward equation is more natural for calibration:** Market data consists of option prices at various maturities $T_1 < T_2 < \cdots$ observed today ($t = 0$). Calibration seeks $\sigma_{\text{loc}}(S, t)$ that reproduces these prices. The forward equation takes the current spot as given and evolves the density to each maturity, directly producing the quantities (marginal densities) that determine call prices via $C(K, T) = e^{-rT}\int_K^\infty (S - K)p(S, T) \, dS$. One forward solve gives prices for all strikes at a given maturity. In contrast, the backward PDE must be solved separately for each strike $K$, requiring many backward solves. Thus the forward equation provides a more efficient framework for calibrating $\sigma_{\text{loc}}$ to the entire option surface.

---

**Exercise 5.** Consider a local volatility surface $\sigma_{\text{loc}}(S, t) = 0.20 + 0.001(S - 100)$ at $t = 0$. Compute the local volatility at $S = 90, 100, 110$. What does this imply about the short-maturity implied volatility smile? Is the smile upward-sloping, downward-sloping, or U-shaped?

??? success "Solution to Exercise 5"
    The local volatility function is $\sigma_{\text{loc}}(S, 0) = 0.20 + 0.001(S - 100)$.

    Evaluating at each spot level:

    - $S = 90$: $\sigma_{\text{loc}}(90, 0) = 0.20 + 0.001(90 - 100) = 0.20 - 0.01 = 0.19$ (19%)
    - $S = 100$: $\sigma_{\text{loc}}(100, 0) = 0.20 + 0.001(100 - 100) = 0.20$ (20%)
    - $S = 110$: $\sigma_{\text{loc}}(110, 0) = 0.20 + 0.001(110 - 100) = 0.20 + 0.01 = 0.21$ (21%)

    **Short-maturity implied volatility smile:** For small $T$, the implied volatility approaches the local volatility:

    $$
    \sigma_{\text{IV}}(K, T) \approx \sigma_{\text{loc}}(K, 0) \quad \text{as } T \to 0
    $$

    Since $\sigma_{\text{loc}}$ is linearly increasing in $S$, the short-maturity implied volatility smile is:

    $$
    \sigma_{\text{IV}}(K) \approx 0.20 + 0.001(K - 100)
    $$

    This is an **upward-sloping** (monotonically increasing) smile: higher strikes have higher implied volatility. This is the opposite of the typical equity skew pattern. Such a pattern might be seen in commodity markets where higher prices are associated with supply disruptions and increased uncertainty. The smile is neither U-shaped nor downward-sloping; it is a simple linear tilt.

---

**Exercise 6.** Dupire's formula can also be expressed in terms of implied volatility rather than call prices. State the version involving $\sigma_{\text{IV}}$, $\frac{\partial \sigma_{\text{IV}}}{\partial T}$, and $\frac{\partial \sigma_{\text{IV}}}{\partial K}$. Why is this "implied volatility form" of Dupire's equation useful in practice despite being more complex?

??? success "Solution to Exercise 6"
    Dupire's formula expressed in terms of implied volatility is:

    $$
    \sigma_{\text{loc}}^2(K, T) = \frac{\sigma_{\text{IV}}^2 + 2\sigma_{\text{IV}} T \frac{\partial \sigma_{\text{IV}}}{\partial T} + 2(r - q) K T \sigma_{\text{IV}} \frac{\partial \sigma_{\text{IV}}}{\partial K}}{\left(1 + K d_1 \sqrt{T} \frac{\partial \sigma_{\text{IV}}}{\partial K}\right)^2 + \sigma_{\text{IV}} K^2 T \left(\frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2} - d_1 \sqrt{T} \left(\frac{\partial \sigma_{\text{IV}}}{\partial K}\right)^2\right)}
    $$

    where $d_1 = \frac{\ln(S_0/K) + (r - q + \sigma_{\text{IV}}^2/2)T}{\sigma_{\text{IV}}\sqrt{T}}$.

    **Why this form is useful in practice:**

    1. **Direct input from market data:** Market participants quote and interpolate implied volatilities, not call prices. The IV-based Dupire formula avoids the intermediate step of converting IV to prices and then differentiating prices.

    2. **Better numerical stability:** Implied volatility surfaces are smoother and better behaved than price surfaces. Derivatives of IV are more stable than derivatives of option prices, especially in the wings where prices are near zero.

    3. **Standard interpolation tools:** Practitioners use well-established IV parametrizations (SVI, SSVI, SABR) that provide analytical expressions for $\frac{\partial \sigma_{\text{IV}}}{\partial K}$, $\frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2}$, and $\frac{\partial \sigma_{\text{IV}}}{\partial T}$. Plugging these directly into the IV-based Dupire formula avoids numerical differentiation entirely.

    4. **Interpretability:** The formula makes the contribution of each smile feature explicit — the ATM level ($\sigma_{\text{IV}}^2$), the term structure slope ($\frac{\partial \sigma_{\text{IV}}}{\partial T}$), the skew ($\frac{\partial \sigma_{\text{IV}}}{\partial K}$), and the curvature ($\frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2}$) each have a clear role.

---

**Exercise 7.** Explain why the local volatility model perfectly calibrates to all vanilla European option prices (existence and uniqueness of $\sigma_{\text{loc}}$), yet may produce unrealistic dynamics for exotic options. Specifically, discuss the forward smile problem: what does the local volatility model predict for the implied volatility smile of a forward-starting option, and how does this compare to market observations?

??? success "Solution to Exercise 7"
    **Perfect calibration to vanillas:** Dupire's formula establishes a one-to-one mapping between an arbitrage-free call price surface $C(K, T)$ and a local volatility function $\sigma_{\text{loc}}(S, t)$. Given any complete, arbitrage-free set of European option prices, there exists a unique continuous diffusion:

    $$
    dS_t = (r - q)S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t
    $$

    that reproduces all vanilla prices exactly. This is guaranteed by Theorem 4.2.3 (uniqueness of local volatility). The calibration is exact by construction — there is no optimization or residual error.

    **Failure for exotic options:** Despite perfect vanilla calibration, the local volatility model produces incorrect dynamics for exotic options because it imposes a specific, deterministic relationship between the spot level and instantaneous volatility. The key issues are:

    1. **Smile dynamics:** The local volatility model generates **sticky-strike** dynamics: as the spot moves, the implied volatility at a fixed strike remains approximately constant. Markets, however, exhibit behavior closer to **sticky-delta** (the smile translates with the spot). This means the model predicts the wrong P&L for delta-hedged exotic positions.

    2. **Spot-vol correlation:** In reality, volatility is stochastic and exhibits a negative correlation with spot (the leverage effect). Local volatility captures the average effect but not the stochastic component, leading to incorrect pricing of path-dependent payoffs.

    **The forward smile problem:** A forward-starting option is struck relative to the spot at a future date $t_1$, with payoff $\max(S_T / S_{t_1} - k, 0)$. Its price depends on the conditional (forward) density $q(S_T \mid S_{t_1})$.

    - **Local volatility prediction:** As $t_1 \to T$, the forward smile flattens and approaches a flat Black-Scholes-like smile. This occurs because the local volatility model's deterministic vol function leaves less and less room for smile generation over a shrinking time window.

    - **Market observation:** Empirically, forward smiles remain pronounced even for short forward windows. Equity markets consistently show a persistent skew in forward-starting options.

    This discrepancy arises because the local volatility model attributes all smile effects to the spot level dependence of volatility, whereas in reality, stochastic volatility and jumps generate smile independently of where the spot is. Stochastic local volatility (SLV) models address this by combining local volatility calibration with a stochastic volatility component that preserves realistic forward smile dynamics.
