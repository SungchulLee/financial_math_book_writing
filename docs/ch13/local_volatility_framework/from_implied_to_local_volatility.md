# From Implied to Local Volatility

*This section covers from implied to local volatility in the context of From Implied To Local Volatility in Chapter 13.*

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand the key concepts of from implied to local volatility
    2. Apply the mathematical framework presented
    3. Connect this topic to related areas in quantitative finance

---

## Overview

This section introduces the fundamental concepts of transforming implied volatility surfaces into local volatility surfaces. The connection between these two surfaces is one of the cornerstones of modern quantitative finance, as it allows us to extract the true local volatility from market-observable implied volatility data.

---

## Key Concepts

The relationship between implied and local volatility can be understood through the lens of the Dupire formula. While implied volatility comes from market data via the Black-Scholes model, local volatility is extracted from option prices using partial derivatives. These two concepts are intimately connected.

---

## Black-Scholes Framework

The Black-Scholes formula provides a fundamental tool for connecting market prices to implied volatility. The call option price is:

$$
C = S_{0}N(d_{1}) - Ke^{-rT}N(d_{2})
$$

where the log-moneyness and variance parameters are defined as:

$$y = \log\frac{K}{S_0e^{rT}}, \quad w = \sigma_{\text{imp}}^2 T$$

and

$$
\begin{aligned}
d_{1} &= -\frac{y}{\sqrt{w}} + \sqrt{w} \\
d_{2} &= -\frac{y}{\sqrt{w}} - \sqrt{w}
\end{aligned}
$$

---

## Change of Variables: From (K, T) to (y, w)

To bridge implied and local volatility, we perform a change of variables from strike-maturity coordinates to log-moneyness and variance coordinates. The partial derivatives transform as follows:

### Time Derivative

$$
C_T = C_y y_T + C_w w_T = -rC_y + \sigma_{\text{imp}}^2 C_w
$$

### Strike Derivative

$$
C_K = C_y y_K + C_w w_K = K^{-1}C_y
$$

### Second Strike Derivative

$$
C_{KK} = (K^{-1}C_y)_K = K^{-2}(C_{yy} - C_y)
$$

---

## Dupire Formula from Implied Volatility (QuantPie)

Using the change of variables, we can express the Dupire formula directly in terms of derivatives with respect to log-moneyness $y$ and variance $w$:

### Setup

The Dupire formula is:

$$
\sigma^2(K,T) = \frac{C_T + rKC_K}{\frac{1}{2} K^2 C_{KK}}
$$

### Application to Black-Scholes Parameters

Substituting the transformed derivatives:

$$
\sigma^2 = \frac{(C_y y_T + C_w w_T) + rK(C_y y_K + C_w w_K)}{\frac{1}{2} K^2 [C_{yy} y_K^2 + 2C_{yw} y_K w_K + C_{ww} w_K^2 + C_y y_{KK} + C_w w_{KK}]}
$$

### Simplified Form

Using the relationships:
- $y_T = -r$, $w_T = \sigma_{\text{imp}}^2$
- $y_K = K^{-1}$, $w_K = 0$
- $y_{KK} = -K^{-2}$, $w_{KK} = 0$

We obtain:

$$
\sigma^2 = \frac{-rC_y + \sigma_{\text{imp}}^2 C_w + rK \cdot K^{-1}C_y}{\frac{1}{2} K^2 \cdot K^{-2}(C_{yy} - C_y)}
$$

This simplifies to:

$$
\sigma^2 = \frac{\sigma_{\text{imp}}^2 C_w}{\frac{1}{2}(C_{yy} - C_y)}
$$

---

## Practical Interpretation

The transformation from implied to local volatility reveals several important points:

1. **Market Data**: Implied volatility surfaces are directly observable from market option prices
2. **Extraction**: Local volatility can be extracted by computing partial derivatives of the call price surface with respect to log-moneyness and variance
3. **Non-parametric Method**: The Dupire formula provides a non-parametric way to construct a local volatility surface that is perfectly consistent with all market option prices
4. **Volatility Smile**: The local volatility surface can capture the volatility smile and term structure observed in market data

---

## Mathematical Framework

The key insight is that the call option price function $C(K, T)$ contains all information about the local volatility surface. Once market prices are observed across strikes and maturities, the Dupire formula uniquely determines the local volatility at each point $(K, T)$ in the strike-maturity space.

This establishes a one-to-one correspondence between:
- Observable call option prices $\{C(K, T) : K > 0, T > 0\}$
- Local volatility surface $\{\sigma(K, T) : K > 0, T > 0\}$

---

## Summary

This section presented the fundamental connection between implied volatility and local volatility. The Black-Scholes framework provides a parametric description of option prices, while the Dupire formula offers a non-parametric extraction of local volatility directly from observed market prices. The change of variables from strike-maturity to log-moneyness-variance coordinates reveals the elegant structure of this relationship and facilitates practical computation of local volatility surfaces from market data.

The ability to extract local volatility surfaces is crucial for:
- Pricing exotic derivatives consistently with market option prices
- Understanding the dynamics implied by the market
- Risk management and sensitivity analysis
- Model calibration and validation

---

## Exercises

**Exercise 1.** Starting from the definitions $y = \log(K / S_0 e^{rT})$ and $w = \sigma_{\text{imp}}^2 T$, verify that $y_T = -r$, $y_K = K^{-1}$, and $y_{KK} = -K^{-2}$. Then confirm that $w_K = 0$ only when implied volatility does not depend on strike. What changes in the derivation if $\sigma_{\text{imp}}$ depends on $K$?

??? success "Solution to Exercise 1"
    Starting from $y = \log(K / S_0 e^{rT}) = \log K - \log S_0 - rT$ and $w = \sigma_{\text{imp}}^2 T$:

    **Derivative $y_T$:** Since $y = \log K - \log S_0 - rT$, differentiating with respect to $T$ gives $y_T = -r$.

    **Derivative $y_K$:** Differentiating $y = \log K - \log S_0 - rT$ with respect to $K$ gives $y_K = 1/K = K^{-1}$.

    **Derivative $y_{KK}$:** Differentiating $y_K = K^{-1}$ with respect to $K$ gives $y_{KK} = -K^{-2}$.

    **For $w_K = 0$:** We have $w = \sigma_{\text{imp}}^2 T$. If $\sigma_{\text{imp}}$ is constant (does not depend on $K$), then $w_K = T \cdot 2\sigma_{\text{imp}} \cdot \frac{\partial \sigma_{\text{imp}}}{\partial K} = 0$.

    **If $\sigma_{\text{imp}}$ depends on $K$:** Then $w_K = 2\sigma_{\text{imp}} T \frac{\partial \sigma_{\text{imp}}}{\partial K} \neq 0$, and the change of variables becomes more involved. The time derivative becomes $C_T = C_y y_T + C_w(w_T + w_{\sigma}\sigma_T)$ where $w$ now depends on $K$ through $\sigma_{\text{imp}}(K, T)$. The strike derivatives acquire additional terms:

    $$
    C_K = C_y y_K + C_w w_K
    $$

    $$
    C_{KK} = C_{yy}y_K^2 + 2C_{yw}y_K w_K + C_{ww}w_K^2 + C_y y_{KK} + C_w w_{KK}
    $$

    The simplified formula $\sigma^2 = \sigma_{\text{imp}}^2 C_w / [\frac{1}{2}(C_{yy} - C_y)]$ no longer holds in this form because the additional $w_K$ and $w_{KK}$ terms do not cancel. The correct approach is to use the full Dupire formula with all derivatives, or to note that the Black-Scholes call price function $C_{\text{BS}}(y, w)$ has specific properties that allow the simplification regardless of the source of $w$.

---

**Exercise 2.** The simplified Dupire formula in $(y, w)$ coordinates is

$$
\sigma^2(K,T) = \frac{\sigma_{\text{imp}}^2 \, C_w}{\frac{1}{2}(C_{yy} - C_y)}
$$

For the Black-Scholes model with constant volatility $\sigma_0$, compute $C_w$ and $C_{yy} - C_y$ explicitly using the Black-Scholes formula. Verify that the formula returns $\sigma^2(K,T) = \sigma_0^2$ for all $(K,T)$.

??? success "Solution to Exercise 2"
    For the Black-Scholes model with constant volatility $\sigma_0$, we have $w = \sigma_0^2 T$ and $d_1 = -y/\sqrt{w} + \sqrt{w}/2$, $d_2 = -y/\sqrt{w} - \sqrt{w}/2$.

    The Black-Scholes call in $(y, w)$ coordinates is:

    $$
    C = S_0 e^{rT}\bigl[N(d_1) - e^y N(d_2)\bigr]
    $$

    **Computing $C_w$:** Using the chain rule and the identity $\frac{\partial d_1}{\partial w} = \frac{y}{2w^{3/2}} + \frac{1}{4\sqrt{w}}$ and $\frac{\partial d_2}{\partial w} = \frac{y}{2w^{3/2}} - \frac{1}{4\sqrt{w}}$:

    $$
    C_w = S_0 e^{rT}\left[n(d_1)\frac{\partial d_1}{\partial w} - e^y n(d_2)\frac{\partial d_2}{\partial w}\right]
    $$

    Using $S_0 e^{rT} n(d_1) = Ke^{rT}e^y n(d_1) = S_0 e^{rT} e^y n(d_2) \cdot e^{-y} = S_0 e^{rT}n(d_1)$ and the identity $n(d_1) = e^y n(d_2)$, this simplifies to:

    $$
    C_w = \frac{S_0 e^{rT} n(d_1)}{2\sqrt{w}}
    $$

    **Computing $C_{yy} - C_y$:** Using the Black-Scholes Greeks in log-moneyness coordinates and the identity $C_{yy} - C_y = S_0 e^{rT} e^y n(d_2) / \sqrt{w}$:

    $$
    C_{yy} - C_y = \frac{S_0 e^{rT} n(d_1)}{\sqrt{w}}
    $$

    (using $e^y n(d_2) = n(d_1)$).

    **Verification:**

    $$
    \frac{\sigma_{\text{imp}}^2 C_w}{\frac{1}{2}(C_{yy} - C_y)} = \frac{\sigma_0^2 \cdot \frac{S_0 e^{rT} n(d_1)}{2\sqrt{w}}}{\frac{1}{2} \cdot \frac{S_0 e^{rT} n(d_1)}{\sqrt{w}}} = \frac{\sigma_0^2}{1} = \sigma_0^2
    $$

    This confirms $\sigma^2(K, T) = \sigma_0^2$ for all $(K, T)$, as expected for constant volatility.

---

**Exercise 3.** The change of variables treats $w = \sigma_{\text{imp}}^2 T$ as independent of $K$, which is valid for the Black-Scholes formula itself but not when $\sigma_{\text{imp}}$ varies across strikes. (a) Explain why the simplified formula $w_K = 0$ still leads to the correct Dupire result. (b) Where does the strike-dependence of implied volatility enter the full Dupire formula?

??? success "Solution to Exercise 3"
    **(a)** The simplified Dupire formula treats $w = \sigma_{\text{imp}}^2 T$ as the Black-Scholes total variance parameter, which is defined implicitly by the equation $C_{\text{market}}(K, T) = C_{\text{BS}}(K, T; w(K, T))$. The key insight is that the Dupire formula operates on the *call price surface* $C(K, T)$, not directly on $\sigma_{\text{imp}}(K, T)$.

    When we write $C(K, T) = C_{\text{BS}}(y(K, T), w(K, T))$ and compute derivatives using the chain rule, the function $C_{\text{BS}}$ is the standard Black-Scholes formula viewed as a function of $y$ and $w$. The simplification $w_K = 0$ refers to treating $C_{\text{BS}}$ as a function where $w$ enters only through its explicit dependence, and all strike dependence enters through $y = \log(K/F)$. The strike dependence of $\sigma_{\text{imp}}$ is already captured in $C(K, T)$ before we decompose it.

    **(b)** The strike dependence of implied volatility enters the full Dupire formula through the *total derivatives* $C_K$ and $C_{KK}$. When we compute $C_K = \frac{\partial C_{\text{BS}}}{\partial y} y_K + \frac{\partial C_{\text{BS}}}{\partial w} w_K$ in the general case where $\sigma_{\text{imp}}$ depends on $K$, the $w_K$ term is nonzero. However, the Dupire formula is written in terms of the actual market derivatives $C_K$ and $C_{KK}$, not the Black-Scholes partials. The formula $\sigma^2 = (C_T + rKC_K) / (\frac{1}{2}K^2 C_{KK})$ uses the total derivatives of the market call price and is correct regardless of whether implied volatility depends on strike.

---

**Exercise 4.** From the Black-Scholes call price $C = S_0 N(d_1) - Ke^{-rT}N(d_2)$, derive the expressions $C_K = -e^{-rT}N(d_2)$ and $C_{KK} = e^{-rT}n(d_2)/(K\sigma_{\text{imp}}\sqrt{T})$ where $n(\cdot)$ is the standard normal density. Use these to show that the denominator of the Dupire formula is proportional to the risk-neutral density at $S_T = K$.

??? success "Solution to Exercise 4"
    Starting from $C = S_0 N(d_1) - Ke^{-rT}N(d_2)$ with $d_1 = \frac{\ln(S_0/K) + (r + \sigma_{\text{imp}}^2/2)T}{\sigma_{\text{imp}}\sqrt{T}}$ and $d_2 = d_1 - \sigma_{\text{imp}}\sqrt{T}$:

    **Deriving $C_K$:** Differentiate with respect to $K$:

    $$
    C_K = S_0 n(d_1)\frac{\partial d_1}{\partial K} - e^{-rT}N(d_2) - Ke^{-rT}n(d_2)\frac{\partial d_2}{\partial K}
    $$

    Using $\frac{\partial d_1}{\partial K} = \frac{\partial d_2}{\partial K} = -\frac{1}{K\sigma_{\text{imp}}\sqrt{T}}$ and the identity $S_0 n(d_1) = Ke^{-rT}n(d_2)$:

    $$
    C_K = Ke^{-rT}n(d_2)\left(-\frac{1}{K\sigma_{\text{imp}}\sqrt{T}}\right) - e^{-rT}N(d_2) - Ke^{-rT}n(d_2)\left(-\frac{1}{K\sigma_{\text{imp}}\sqrt{T}}\right) = -e^{-rT}N(d_2)
    $$

    **Deriving $C_{KK}$:** Differentiate $C_K = -e^{-rT}N(d_2)$:

    $$
    C_{KK} = -e^{-rT}n(d_2)\frac{\partial d_2}{\partial K} = -e^{-rT}n(d_2)\left(-\frac{1}{K\sigma_{\text{imp}}\sqrt{T}}\right) = \frac{e^{-rT}n(d_2)}{K\sigma_{\text{imp}}\sqrt{T}}
    $$

    **Connection to risk-neutral density:** By the Breeden-Litzenberger formula, $C_{KK} = e^{-rT}p(K, T)$. Comparing:

    $$
    p(K, T) = \frac{n(d_2)}{K\sigma_{\text{imp}}\sqrt{T}}
    $$

    This is the lognormal risk-neutral density evaluated at $S_T = K$. The denominator of the Dupire formula $\frac{1}{2}K^2 C_{KK} = \frac{1}{2}K^2 e^{-rT}p(K, T)$ is therefore directly proportional to the risk-neutral density at the strike, confirming that local volatility is extracted by dividing the rate of optionality growth by the concentration of probability mass.

---

**Exercise 5.** Consider a flat implied volatility surface $\sigma_{\text{imp}}(K,T) = 0.25$ for all $K$ and $T$. (a) Compute the local volatility $\sigma(K,T)$ from the Dupire formula. (b) Now consider $\sigma_{\text{imp}}(K,T) = 0.25 - 0.001(K - S_0)$, a linear skew. Describe qualitatively how the local volatility surface differs from constant. (c) Which surface has more curvature in $K$: the implied volatility surface or the local volatility surface?

??? success "Solution to Exercise 5"
    **(a)** With $\sigma_{\text{imp}}(K, T) = 0.25$ for all $K$ and $T$, the Dupire formula gives $\sigma(K, T) = 0.25$. This is because Black-Scholes is a special case of the local volatility model: when implied volatility is constant, the local volatility equals the implied volatility everywhere (as verified in Exercise 2).

    **(b)** With $\sigma_{\text{imp}}(K, T) = 0.25 - 0.001(K - S_0)$, the implied volatility is higher for low strikes (OTM puts) and lower for high strikes (OTM calls). This is a linear skew typical of equity markets.

    The local volatility surface will be **steeper** than the implied volatility surface. Qualitatively:

    - At $K < S_0$: local volatility is higher than implied volatility (roughly double the skew effect)
    - At $K > S_0$: local volatility is lower than implied volatility
    - At $K = S_0$ (ATM): local volatility is approximately equal to implied volatility

    The local volatility skew is approximately twice as steep as the implied volatility skew near ATM because implied volatility represents an average of local volatility along paths, and the averaging effect smooths out roughly half the slope.

    **(c)** The **local volatility surface** has more curvature in $K$. Even though the implied volatility surface is perfectly linear in $K$ (zero curvature $\partial^2\sigma_{\text{imp}}/\partial K^2 = 0$), the local volatility surface develops nonzero curvature. This is because the mapping from implied to local volatility is nonlinear -- it involves the Dupire formula which combines the IV derivatives in a nonlinear way. The denominator of the Dupire formula depends on $K$ and $d_1$, introducing curvature even when the implied volatility input is linear.

---

**Exercise 6.** The Dupire formula requires computing $C_T$, $C_K$, and $C_{KK}$ from market data. In practice, these derivatives must be estimated numerically. (a) Write finite-difference approximations for each derivative. (b) If option prices have bid-ask spreads of 0.5%, estimate the relative error in the local volatility computed from finite differences with strike spacing $\Delta K = 5$ and maturity spacing $\Delta T = 0.25$. (c) Which derivative is most sensitive to noise?

??? success "Solution to Exercise 6"
    **(a)** Finite-difference approximations:

    $$
    C_T \approx \frac{C(K, T + \Delta T) - C(K, T - \Delta T)}{2\Delta T}
    $$

    $$
    C_K \approx \frac{C(K + \Delta K, T) - C(K - \Delta K, T)}{2\Delta K}
    $$

    $$
    C_{KK} \approx \frac{C(K + \Delta K, T) - 2C(K, T) + C(K - \Delta K, T)}{(\Delta K)^2}
    $$

    **(b)** With bid-ask spread of $0.5\%$, the absolute error in each price is approximately $\epsilon \approx 0.005 \times C$, where $C$ is the option price.

    For $C_T$ with $\Delta T = 0.25$: relative error $\approx \frac{2\epsilon}{2\Delta T \cdot C_T} = \frac{0.005 C}{0.25 \cdot C_T}$. With typical $C_T/C \approx 0.1$--$0.5$ per year, the relative error is roughly $2\%$--$10\%$.

    For $C_{KK}$ with $\Delta K = 5$: the second derivative amplifies noise quadratically. The error in $C_{KK}$ is approximately $4\epsilon / (\Delta K)^2 = 4 \times 0.005C / 25 = 0.0008C$. Since $C_{KK} \approx e^{-rT}n(d_2)/(K\sigma\sqrt{T})$, which for ATM options is roughly $C_{KK} \approx 0.008$--$0.02$ when $C \approx 5$--$10$, the relative error in $C_{KK}$ can be $20\%$--$50\%$.

    The resulting relative error in $\sigma_{\text{loc}}^2$ is roughly the sum of the relative errors in the numerator and denominator, potentially $30\%$--$60\%$.

    **(c)** The **second strike derivative $C_{KK}$** is the most sensitive to noise. Each numerical differentiation amplifies the error by a factor of roughly $2/\Delta K$ (for first derivative) or $4/(\Delta K)^2$ (for second derivative). Since $C_{KK}$ involves two differentiations, it has the highest error amplification. Furthermore, $C_{KK}$ appears in the denominator of the Dupire formula, so errors in $C_{KK}$ directly translate to large errors in $\sigma_{\text{loc}}^2$, especially in the wings where $C_{KK}$ is small.

---

**Exercise 7.** The one-to-one correspondence between the call price surface $\{C(K,T)\}$ and the local volatility surface $\{\sigma(K,T)\}$ holds under certain regularity conditions. (a) State the conditions on $C(K,T)$ that are required (smoothness, no-arbitrage). (b) Give an example of a call price surface that violates these conditions. (c) Explain how violations of calendar spread arbitrage ($C_T < 0$) or butterfly arbitrage ($C_{KK} < 0$) would cause the Dupire formula to break down.

??? success "Solution to Exercise 7"
    **(a)** The required conditions on $C(K, T)$ are:

    - **Smoothness:** $C(K, T)$ must be $C^1$ in $T$ (continuously differentiable in maturity) and $C^2$ in $K$ (twice continuously differentiable in strike) so that the partial derivatives in the Dupire formula exist
    - **No butterfly arbitrage:** $C_{KK}(K, T) \geq 0$ for all $K > 0$, ensuring a non-negative risk-neutral density
    - **No calendar spread arbitrage:** $C_T(K, T) + (r-q)KC_K(K, T) + qC(K, T) \geq 0$, ensuring the numerator of the Dupire formula is non-negative
    - **Boundary conditions:** $C(0, T) = S_0 e^{-qT}$ (deep ITM), $C(K, T) \to 0$ as $K \to \infty$ (deep OTM), $C(K, 0) = (S_0 - K)^+$ (zero maturity)
    - **Monotonicity in strike:** $C_K(K, T) \leq 0$ (call prices decrease with strike)

    **(b)** Example of a violating surface: Define $C(K, T) = \max(S_0 e^{-qT} - Ke^{-rT}, 0) + \epsilon \sin(K)$ for small $\epsilon > 0$. The sinusoidal perturbation introduces regions where $C_{KK} < 0$ (butterfly arbitrage) and potentially $C_K > 0$ (call spread arbitrage). Such a surface cannot correspond to any diffusion model.

    **(c)** **Calendar spread arbitrage** ($C_T < 0$ after drift adjustment): If the numerator $C_T + (r-q)KC_K + qC < 0$ at some point $(K_0, T_0)$, then $\sigma_{\text{loc}}^2(K_0, T_0) < 0$ since the denominator is positive. A negative local variance is physically impossible -- it would require imaginary volatility. This means no diffusion model can reproduce the given call prices.

    **Butterfly arbitrage** ($C_{KK} < 0$): If $C_{KK}(K_0, T_0) < 0$, then the denominator of the Dupire formula is negative. Combined with a positive numerator, this yields $\sigma_{\text{loc}}^2 < 0$, again impossible. Moreover, $C_{KK} < 0$ implies a negative risk-neutral density $p(K_0, T_0) < 0$, which has no probabilistic interpretation. At points where $C_{KK} = 0$ exactly, the Dupire formula has a $0/0$ or finite$/0$ singularity, making $\sigma_{\text{loc}}$ undefined or infinite.
