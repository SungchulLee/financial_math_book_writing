# Tanaka Formula and Payoff Distributions

This section explores the Tanaka formula and its application to understanding non-smooth financial payoffs through a distributional approach. The Tanaka formula provides a rigorous mathematical framework for handling discontinuous derivatives in option pricing theory.

!!! abstract "Learning Objectives"
    After completing this section, you will understand:

    - The Tanaka formula and its derivatives for non-smooth functions
    - How Dirac delta functions arise naturally in option pricing
    - The distributional approach to the Dupire PDE
    - The connection between payoff functions and their derivatives
    - How singular distributions encode important information about option Greeks

---

## Introduction: Non-Smooth Payoffs

Standard calculus breaks down when applied to non-smooth functions like the call option payoff:

$$
(S_T - K)^+ = \max(S_T - K, 0)
$$

At the strike price $K$, this function has a kink (corner), making classical derivatives ill-defined. The Tanaka formula extends Itô's lemma to handle such non-smooth functions by introducing distributional derivatives.

---

## The Tanaka Formula

The Tanaka formula is a generalization of Itô's lemma that applies to non-smooth, convex functions. For a convex function $f(x)$, the Tanaka formula states:

$$
df(X_t) = f'(X_t) dX_t + \frac{1}{2}f''(X_t) d\langle X \rangle_t
$$

where $f'$ and $f''$ are understood in the distributional sense.

### Application to Call Payoff

For the call payoff function $f(s) = (s - K)^+$, we need to compute the derivatives in the distributional sense.

#### First Derivative

The first derivative of $(S_T - K)^+$ with respect to $S_T$ is the Heaviside step function:

$$
\frac{\partial (S_T - K)^+}{\partial S_T} = 1(S_T > K)
$$

where $1(S_T > K)$ is the indicator function that equals 1 when $S_T > K$ and 0 otherwise.

With respect to the strike $K$:

$$
\frac{\partial (S_T - K)^+}{\partial K} = -1(S_T > K)
$$

#### Second Derivative: The Dirac Delta Function

The second derivative of the call payoff is the **Dirac delta function** $\delta(S_T - K)$:

$$
\begin{array}{llllll}
\displaystyle
\frac{\partial^2 (S_T - K)^+}{\partial S_T^2} &=& \displaystyle \delta(S_T - K) \\
\displaystyle
\frac{\partial^2 (S_T - K)^+}{\partial K^2} &=& \displaystyle \delta(S_T - K)
\end{array}$$

The Dirac delta function has the key property:

$$
\int_{-\infty}^{\infty} \delta(x - a) f(x) \, dx = f(a)
$$

It can be understood as the limit of increasingly narrow, increasingly tall distributions centered at $K$:

$$
\delta(x - K) = \lim_{\epsilon \to 0} \frac{1}{\epsilon\sqrt{\pi}} e^{-(x-K)^2/\epsilon^2}
$$

---

## Computing Option Greeks via Distributions

Using the Tanaka formula, we can rigorously compute the Greeks (sensitivities) of options:

### Delta and Gamma

The delta (first derivative with respect to spot) is:

$$
\Delta = \frac{\partial C}{\partial S_T} = e^{-rT}\mathbb{E}^Q\left[\frac{\partial (S_T - K)^+}{\partial S_T}\right] = e^{-rT}\mathbb{E}^Q[1(S_T > K)] = e^{-rT}\int_{K}^{\infty} p(s, T) \, ds
$$

The gamma (second derivative with respect to spot) is:

$$
\Gamma = \frac{\partial^2 C}{\partial S_T^2} = e^{-rT}\mathbb{E}^Q\left[\frac{\partial^2 (S_T - K)^+}{\partial S_T^2}\right] = e^{-rT}\mathbb{E}^Q[\delta(S_T - K)] = e^{-rT}p(K, T)
$$

This shows that the gamma is proportional to the risk-neutral probability density at the strike price. This is a profound result: gamma measures how likely the stock is to end up exactly at the strike price.

### The Strike Derivative

Similarly, with respect to the strike $K$:

$$
\frac{\partial C}{\partial K} = e^{-rT}\mathbb{E}^Q\left[-1(S_T > K)\right] = -e^{-rT}\int_{K}^{\infty} p(s, T) \, ds
$$

$$
\frac{\partial^2 C}{\partial K^2} = e^{-rT}\mathbb{E}^Q[\delta(S_T - K)] = e^{-rT}p(K, T)
$$

---

## Itô's Lemma for Non-Smooth Functions

Using the Tanaka formula, we can apply an extended version of Itô's lemma to the call payoff. Under the risk-neutral measure:

$$
dS_t = rS_t dt + \sigma(t, S_t)S_t dW_t
$$

The change in the call payoff is:

$$
\begin{array}{lll}
d(S_T - K)^+ &=& \displaystyle \frac{\partial (S_T - K)^+}{\partial S_T}dS_T + \frac{1}{2}\frac{\partial^2 (S_T - K)^+}{\partial S_T^2}dS^2_T \\
&=& \displaystyle 1(S_T > K)dS_T + \frac{1}{2}\delta(S_T - K)dS^2_T \\
&=& \displaystyle 1(S_T > K)\left(rS_T dt + \sigma(S_T, T)S_T dW_T\right) + \frac{1}{2}\delta(S_T - K)\sigma^2(S_T, T)S_T^2 dt \\
&=& \displaystyle \left[1(S_T > K)rS_T + \frac{1}{2}\delta(S_T - K)\sigma^2(S_T, T)S_T^2\right] dt + 1(S_T > K)\sigma(S_T, T)S_T dW_T
\end{array}$$

---

## The Distributional Dupire PDE

Taking expectations and differentiating with respect to maturity time $T$:

$$
\frac{\partial}{\partial T}\mathbb{E}^Q(S_T - K)^+ = \mathbb{E}^Q\left[1(S_T > K)rS_T + \frac{1}{2}\delta(S_T - K)\sigma^2(S_T, T)S_T^2\right]
$$

Using the identity $\mathbb{E}^Q[1(S_T > K)S_T] = e^{rT}C - e^{rT}K\frac{\partial C}{\partial K}$, and the fact that the delta function selects values at $S_T = K$:

$$
\mathbb{E}^Q[\delta(S_T - K)\sigma^2(S_T, T)S_T^2] = \sigma^2(K, T)K^2 \mathbb{E}^Q[\delta(S_T - K)] = \sigma^2(K, T)K^2 e^{-rT}\frac{\partial^2 C}{\partial K^2}
$$

This leads to the **Dupire PDE**:

$$
C_T = -rC + r\left(C - KC_K\right) + \frac{1}{2}\sigma^2(K, T)K^2 C_{KK}
$$

which simplifies to:

$$
\boxed{\displaystyle C_T + rK C_K + \frac{1}{2}\sigma^2(K, T)K^2 C_{KK} = rC}
$$

---

## Physical Interpretation

The Tanaka formula reveals that:

1. **Indicator Function**: The term $1(S_T > K)$ represents the exercise feature of the option. It is non-zero only when the option finishes in-the-money.

2. **Delta Function**: The term $\delta(S_T - K)$ concentrates on the strike price and captures the "kink" in the payoff function. It encodes the fact that the payoff function has a discontinuous derivative at $K$.

3. **Volatility and Gamma**: The appearance of the delta function times $\sigma^2(S_T, T)S_T^2$ shows how volatility at the strike price directly affects the option price through the gamma.

4. **Risk-Neutral Density**: The Dupire formula shows that the local volatility can be extracted from the risk-neutral density and option prices:
   $$
   \sigma^2(K, T) = \frac{C_T + rKC_K}{\frac{1}{2}K^2 C_{KK}}
   $$

---

## Key Insights

The distributional approach reveals deep connections in option pricing theory:

- **Non-smooth Functions**: Finance often deals with non-smooth payoffs. The Tanaka formula provides the correct mathematical framework.

- **Gamma and Density**: The second derivative of the option price (gamma) is proportional to the risk-neutral probability density at the strike.

- **Volatility Extraction**: The Dupire formula, derived rigorously via the Tanaka formula, shows how to extract local volatility from observable option prices.

- **Singularity as Information**: The delta function singularity at the strike encodes critical information about the option's sensitivity and the underlying probability distribution.

---

## Summary

The Tanaka formula extends calculus to handle non-smooth functions, which are ubiquitous in finance. By introducing distributional derivatives like the Dirac delta function, we can rigorously apply Itô's lemma to option payoffs. This leads to the Dupire PDE and provides a complete mathematical framework for understanding the relationship between option prices, volatility surfaces, and risk-neutral probability distributions.

The key takeaway is that the apparent singularity in the payoff function (the kink at the strike) is not a defect but rather a feature that carries crucial information: it concentrates the measure of uncertainty at the strike price and directly links to the probability density of the underlying asset.

