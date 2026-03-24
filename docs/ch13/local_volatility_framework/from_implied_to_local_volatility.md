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

---

**Exercise 2.** The simplified Dupire formula in $(y, w)$ coordinates is

$$
\sigma^2(K,T) = \frac{\sigma_{\text{imp}}^2 \, C_w}{\frac{1}{2}(C_{yy} - C_y)}
$$

For the Black-Scholes model with constant volatility $\sigma_0$, compute $C_w$ and $C_{yy} - C_y$ explicitly using the Black-Scholes formula. Verify that the formula returns $\sigma^2(K,T) = \sigma_0^2$ for all $(K,T)$.

---

**Exercise 3.** The change of variables treats $w = \sigma_{\text{imp}}^2 T$ as independent of $K$, which is valid for the Black-Scholes formula itself but not when $\sigma_{\text{imp}}$ varies across strikes. (a) Explain why the simplified formula $w_K = 0$ still leads to the correct Dupire result. (b) Where does the strike-dependence of implied volatility enter the full Dupire formula?

---

**Exercise 4.** From the Black-Scholes call price $C = S_0 N(d_1) - Ke^{-rT}N(d_2)$, derive the expressions $C_K = -e^{-rT}N(d_2)$ and $C_{KK} = e^{-rT}n(d_2)/(K\sigma_{\text{imp}}\sqrt{T})$ where $n(\cdot)$ is the standard normal density. Use these to show that the denominator of the Dupire formula is proportional to the risk-neutral density at $S_T = K$.

---

**Exercise 5.** Consider a flat implied volatility surface $\sigma_{\text{imp}}(K,T) = 0.25$ for all $K$ and $T$. (a) Compute the local volatility $\sigma(K,T)$ from the Dupire formula. (b) Now consider $\sigma_{\text{imp}}(K,T) = 0.25 - 0.001(K - S_0)$, a linear skew. Describe qualitatively how the local volatility surface differs from constant. (c) Which surface has more curvature in $K$: the implied volatility surface or the local volatility surface?

---

**Exercise 6.** The Dupire formula requires computing $C_T$, $C_K$, and $C_{KK}$ from market data. In practice, these derivatives must be estimated numerically. (a) Write finite-difference approximations for each derivative. (b) If option prices have bid-ask spreads of 0.5%, estimate the relative error in the local volatility computed from finite differences with strike spacing $\Delta K = 5$ and maturity spacing $\Delta T = 0.25$. (c) Which derivative is most sensitive to noise?

---

**Exercise 7.** The one-to-one correspondence between the call price surface $\{C(K,T)\}$ and the local volatility surface $\{\sigma(K,T)\}$ holds under certain regularity conditions. (a) State the conditions on $C(K,T)$ that are required (smoothness, no-arbitrage). (b) Give an example of a call price surface that violates these conditions. (c) Explain how violations of calendar spread arbitrage ($C_T < 0$) or butterfly arbitrage ($C_{KK} < 0$) would cause the Dupire formula to break down.

