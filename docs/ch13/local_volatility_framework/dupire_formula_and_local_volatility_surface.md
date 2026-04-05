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

**Exercise 1.** State Dupire's formula in its simplest form (forward coordinates) and identify the role of each partial derivative. What does the numerator $\frac{\partial C}{\partial T}$ correspond to economically? What does the denominator $\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}$ correspond to?

??? success "Solution to Exercise 1"
    Dupire's formula in forward coordinates is

    $$
    \sigma_{\text{loc}}^2(K, T) = \frac{2\,\frac{\partial C}{\partial T}}{K^2\,\frac{\partial^2 C}{\partial K^2}}
    $$

    **Numerator** $\frac{\partial C}{\partial T}$: This is the **calendar spread value** -- the sensitivity of the call price to an increase in maturity. Economically, it measures how much additional optionality is gained by extending the expiration date. A longer-dated option has more time for the underlying to move, so $\frac{\partial C}{\partial T} \geq 0$ for European calls in the absence of arbitrage. This quantity is closely related to the option's theta (with a sign change and discounting adjustment).

    **Denominator** $\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}$: By the Breeden-Litzenberger formula, $\frac{\partial^2 C}{\partial K^2} = e^{-rT} p(K, T)$, where $p(K, T)$ is the risk-neutral density evaluated at the strike. Hence the denominator is $\frac{1}{2}K^2 e^{-rT} p(K, T)$. This measures the concentration of probability mass at strike $K$. Economically, $\frac{\partial^2 C}{\partial K^2}$ is the value of an infinitesimal butterfly spread centered at $K$, which isolates the probability of the underlying finishing near $K$.

    The ratio therefore gives the local variance as the rate of optionality increase per unit probability density -- where the density is high, moderate local volatility suffices to generate time value; where the density is low, local volatility must be large.

---

**Exercise 2.** For a constant implied volatility surface $\sigma_{\text{IV}}(K, T) = 0.25$, verify that Dupire's formula yields $\sigma_{\text{loc}}(K, T) = 0.25$ for all $(K, T)$. Use the Black-Scholes call price to compute the necessary derivatives.

??? success "Solution to Exercise 2"
    When $\sigma_{\text{IV}}(K, T) = 0.25$ for all $(K, T)$, the call price is the standard Black-Scholes price with constant volatility $\sigma = 0.25$. We use Dupire's formula (with drift terms):

    $$
    \sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + qC + (r-q)K\frac{\partial C}{\partial K}}{\frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2}}
    $$

    Since $C$ is the Black-Scholes price with constant $\sigma = 0.25$, it satisfies the Black-Scholes PDE in the maturity variable. The Black-Scholes PDE in strike-maturity space gives:

    $$
    \frac{\partial C}{\partial T} + qC + (r-q)K\frac{\partial C}{\partial K} = \frac{1}{2}\sigma^2 K^2 \frac{\partial^2 C}{\partial K^2}
    $$

    This is precisely the Dupire equation with $\sigma_{\text{loc}}^2 = \sigma^2$. Substituting into Dupire's formula:

    $$
    \sigma_{\text{loc}}^2(K, T) = \frac{\frac{1}{2}\sigma^2 K^2 \frac{\partial^2 C}{\partial K^2}}{\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}} = \sigma^2 = 0.0625
    $$

    Therefore $\sigma_{\text{loc}}(K, T) = 0.25$ for all $(K, T)$, confirming that Black-Scholes is a special case of the local volatility model.

---

**Exercise 3.** Given discrete call prices $C(95, 0.25) = 8.50$, $C(100, 0.25) = 5.80$, $C(105, 0.25) = 3.70$, $C(100, 0.20) = 4.30$, $C(100, 0.30) = 7.10$, with $\Delta K = 5$ and $\Delta T = 0.05$, compute $\sigma_{\text{loc}}^2(100, 0.25)$ using finite-difference approximations. Take $r = 0.03$ and $q = 0$.

??? success "Solution to Exercise 3"
    Using finite differences with $r = 0.03$, $q = 0$, $K = 100$, $T = 0.25$, $\Delta K = 5$, and $\Delta T = 0.05$:

    **Time derivative:**

    $$
    \frac{\partial C}{\partial T}\bigg|_{100, 0.25} \approx \frac{C(100, 0.30) - C(100, 0.20)}{0.30 - 0.20} = \frac{7.10 - 4.30}{0.10} = 28.0
    $$

    **First strike derivative:**

    $$
    \frac{\partial C}{\partial K}\bigg|_{100, 0.25} \approx \frac{C(105, 0.25) - C(95, 0.25)}{2 \times 5} = \frac{3.70 - 8.50}{10} = -0.48
    $$

    **Second strike derivative:**

    $$
    \frac{\partial^2 C}{\partial K^2}\bigg|_{100, 0.25} \approx \frac{C(105, 0.25) - 2C(100, 0.25) + C(95, 0.25)}{5^2} = \frac{3.70 - 11.60 + 8.50}{25} = \frac{0.60}{25} = 0.024
    $$

    **Dupire's formula (with $q = 0$):**

    $$
    \sigma_{\text{loc}}^2(100, 0.25) = \frac{C_T + rKC_K}{\frac{1}{2}K^2 C_{KK}} = \frac{28.0 + 0.03 \times 100 \times (-0.48)}{\frac{1}{2} \times 10000 \times 0.024} = \frac{28.0 - 1.44}{120} = \frac{26.56}{120} \approx 0.2213
    $$

    Therefore $\sigma_{\text{loc}}(100, 0.25) = \sqrt{0.2213} \approx 0.4705$, or about $47.05\%$.

---

**Exercise 4.** The ATM approximation gives $\sigma_{\text{loc}}^2(F, T) \approx \sigma_{\text{IV}}^2 + 2T\sigma_{\text{IV}} \frac{\partial \sigma_{\text{IV}}}{\partial T}$. If $\sigma_{\text{IV}}(F, 0.5) = 20\%$ and $\frac{\partial \sigma_{\text{IV}}}{\partial T} = 0.02$ (IV increases by 2% per year of maturity), compute $\sigma_{\text{loc}}(F, 0.5)$. Is local volatility higher or lower than implied volatility when the term structure is upward sloping?

??? success "Solution to Exercise 4"
    Given: $\sigma_{\text{IV}}(F, 0.5) = 0.20$, $\frac{\partial \sigma_{\text{IV}}}{\partial T} = 0.02$, $T = 0.5$.

    Using the ATM approximation:

    $$
    \sigma_{\text{loc}}^2(F, 0.5) \approx \sigma_{\text{IV}}^2 + 2T\sigma_{\text{IV}}\frac{\partial \sigma_{\text{IV}}}{\partial T} = (0.20)^2 + 2(0.5)(0.20)(0.02)
    $$

    $$
    = 0.04 + 0.004 = 0.044
    $$

    Therefore:

    $$
    \sigma_{\text{loc}}(F, 0.5) = \sqrt{0.044} \approx 0.2098 \approx 20.98\%
    $$

    The local volatility is **higher** than the implied volatility ($20.98\%$ vs $20\%$).

    When the term structure is upward sloping ($\frac{\partial \sigma_{\text{IV}}}{\partial T} > 0$), the local volatility exceeds the implied volatility. This makes intuitive sense: if the market expects higher volatility for longer maturities, the instantaneous volatility at time $T$ must be higher than the average volatility up to time $T$ (which is what implied volatility represents). The implied volatility is a time-averaged quantity, so for the average to be rising, the marginal (local) volatility must exceed the current average.

---

**Exercise 5.** Explain why the Tanaka formula approach to deriving Dupire's result uses local time $L_T^K$ of the process at level $K$. What is the connection between the occupation density of the diffusion and the option price?

??? success "Solution to Exercise 5"
    The **local time** $L_T^K$ of the process $S_t$ at level $K$ measures the amount of time the process spends in an infinitesimal neighborhood of $K$, weighted by the diffusion coefficient. Formally, $L_T^K$ satisfies the occupation times formula:

    $$
    \int_0^T g(S_t) \, d\langle S \rangle_t = \int_0^\infty g(a) L_T^a \, da
    $$

    for any non-negative measurable function $g$.

    **Why local time appears:** Tanaka's formula applied to the convex but non-smooth function $(x - K)^+$ gives:

    $$
    (S_T - K)^+ = (S_0 - K)^+ + \int_0^T \mathbf{1}_{\{S_t > K\}} \, dS_t + \frac{1}{2}L_T^K
    $$

    The local time term $\frac{1}{2}L_T^K$ replaces the second-order term that would appear in Ito's lemma if the function were smooth. It captures the contribution from the "kink" at the strike price $K$.

    **Connection between occupation density and option price:** Taking risk-neutral expectations:

    $$
    C(K, T) = e^{-rT}\mathbb{E}[(S_0 - K)^+] + e^{-rT}\mathbb{E}\left[\int_0^T \mathbf{1}_{\{S_t > K\}}(r-q)S_t \, dt\right] + \frac{1}{2}e^{-rT}\mathbb{E}[L_T^K]
    $$

    The expected local time satisfies:

    $$
    \mathbb{E}[L_T^K] = \int_0^T \sigma_{\text{loc}}^2(K, t)K^2 p(K, t) \, dt
    $$

    where $p(K, t)$ is the risk-neutral transition density. This connects the occupation density of the diffusion to the risk-neutral density, which in turn is related to the option price via the Breeden-Litzenberger formula $p(K, T) = e^{rT}\frac{\partial^2 C}{\partial K^2}$.

    Differentiating $C$ with respect to $T$ isolates the local volatility contribution at time $T$, yielding Dupire's formula. The occupation density approach provides an alternative proof that avoids direct manipulation of the Fokker-Planck PDE and instead relies on the pathwise properties of the diffusion.

---

**Exercise 6.** List four limitations of the local volatility model. For each, describe a specific exotic option that would be mispriced and explain the direction of the error (overpriced or underpriced).

??? success "Solution to Exercise 6"
    **Four limitations and associated mispriced exotics:**

    **1. Sticky-strike smile dynamics.** The local volatility model generates smile dynamics where the implied volatility at a fixed strike remains constant as spot moves ("sticky strike"). In reality, markets exhibit closer to "sticky delta" behavior, where the smile moves with the spot. **Mispriced exotic:** *Cliquet options* (forward-starting options whose strikes reset periodically). Since cliquet payoffs depend on the forward smile, and local volatility predicts a flat forward smile while the market exhibits persistent smile, local volatility **underprices** cliquets -- the realized forward smile is richer than what the model predicts.

    **2. Incorrect spot-volatility correlation.** Local volatility is purely deterministic, so there is no stochastic volatility component or separate correlation parameter. The leverage effect (negative correlation between returns and volatility) is only partially captured. **Mispriced exotic:** *Variance swaps on individual stocks.* The local volatility model underpredicts the convexity of realized variance, leading to **underpricing** of variance swaps relative to stochastic volatility models.

    **3. Flat forward smile.** The model predicts that forward-starting options see a flat implied volatility smile, contradicting market data showing persistent forward smiles. **Mispriced exotic:** *Barrier options* (knock-in, knock-out). The local volatility model generates incorrect transition probabilities for crossing barriers because it misspecifies the conditional distributions of future prices. Up-and-out calls are typically **overpriced** by local volatility (the model underestimates the probability of barrier breach because the local vol near the barrier is too low relative to what stochastic vol models predict).

    **4. No volatility-of-volatility.** Since volatility is deterministic, there is zero "vol of vol" -- the model cannot capture the randomness of future realized volatility. **Mispriced exotic:** *Options on variance* (VIX options, volatility swaptions). These depend critically on the distribution of future realized variance. The local volatility model assigns zero variance to future realized variance, so it systematically **underprices** out-of-the-money VIX calls and other instruments that pay off when volatility spikes.

---

**Exercise 7.** A practitioner has computed the local volatility surface and finds $\sigma_{\text{loc}} = 150\%$ at a deep OTM put strike. (a) Is this economically reasonable? (b) What data quality issue likely caused this? (c) Describe two regularization approaches to address the problem while maintaining arbitrage-free properties.

??? success "Solution to Exercise 7"
    **(a)** A local volatility of $150\%$ is **not economically reasonable**. Annual realized volatility for even the most volatile equities rarely exceeds $80\%$--$100\%$. A local volatility of $150\%$ would imply that if the asset reaches the deep OTM put strike at that time, its instantaneous annualized volatility would be $150\%$, corresponding to daily moves of roughly $150\%/\sqrt{252} \approx 9.5\%$. While distressed assets can exhibit elevated volatility, $150\%$ as a point estimate from a smooth diffusion model is implausibly high and almost certainly an artifact of the data.

    **(b)** The most likely data quality issue is **noise amplification in the denominator of Dupire's formula**. At a deep OTM put strike, the risk-neutral density $p(K, T) = e^{rT}\frac{\partial^2 C}{\partial K^2}$ is very small. Since the denominator of Dupire's formula is $\frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2}$, dividing by a near-zero quantity amplifies small errors in the call price surface. Specifically:

    - Option prices in the wings have wide bid-ask spreads, so the input data is noisy
    - Numerical differentiation of noisy data amplifies errors (each derivative roughly doubles the relative error)
    - The second derivative $C_{KK}$ computed from a finite-difference stencil on illiquid options can be very small or even negative

    **(c)** Two regularization approaches:

    **Approach 1: Tikhonov (smoothness) regularization.** Instead of directly applying Dupire's formula, solve the inverse problem by finding $\sigma_{\text{loc}}(K, T)$ that minimizes:

    $$
    \sum_{i,j}\bigl(C_{\text{model}}(K_i, T_j) - C_{\text{market}}(K_i, T_j)\bigr)^2 + \lambda \int\!\!\int \left[\left(\frac{\partial \sigma_{\text{loc}}}{\partial K}\right)^2 + \left(\frac{\partial \sigma_{\text{loc}}}{\partial T}\right)^2\right] dK\,dT
    $$

    The penalty term $\lambda$ controls the trade-off between data fidelity and smoothness, preventing extreme values in the wings while preserving the no-arbitrage structure.

    **Approach 2: Parametric wing extrapolation.** In the wings where market data is sparse, replace the raw call prices with prices generated by a parametric model (such as SVI or SABR) that has been calibrated to the liquid strikes. The parametric form enforces smooth, monotone behavior of $C(K)$ in the tails, ensuring that $C_{KK}$ remains positive and bounded away from zero. This avoids the division-by-nearly-zero problem while maintaining $C_K \leq 0$ (no call spread arbitrage) and $C_{KK} \geq 0$ (no butterfly arbitrage).
