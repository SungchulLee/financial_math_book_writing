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

Recall (see [§ Breeden-Litzenberger](../../ch12/model_free_results/breeden_litzenberger_formula.md)) for $C_K = -e^{-rT}\int_K^\infty p(s,T)\,ds$ and $C_{KK} = e^{-rT}p(K,T)$, which follow from the distributional derivatives of the call payoff with respect to $K$.
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

---

## Exercises

**Exercise 1.** Compute the first and second distributional derivatives of the put payoff $(K - S_T)^+$ with respect to $S_T$. Express the second derivative in terms of the Dirac delta function and compare with the call payoff case.

??? success "Solution to Exercise 1"
    The put payoff is $f(S_T) = (K - S_T)^+ = \max(K - S_T, 0)$.

    **First distributional derivative with respect to $S_T$:**

    $$
    \frac{\partial(K - S_T)^+}{\partial S_T} = -\mathbf{1}(S_T < K)
    $$

    This is the negative of the Heaviside step function (with value $-1$ when $S_T < K$ and $0$ when $S_T > K$). Compared to the call case where $\partial(S_T - K)^+/\partial S_T = \mathbf{1}(S_T > K)$, the put derivative is negative and activates on the opposite side of the strike.

    **Second distributional derivative with respect to $S_T$:**

    $$
    \frac{\partial^2(K - S_T)^+}{\partial S_T^2} = \delta(S_T - K)
    $$

    This is the **same** Dirac delta function as in the call case. This makes sense because the put and call payoffs are related by put-call parity:

    $$
    (K - S_T)^+ = (S_T - K)^+ - (S_T - K)
    $$

    The linear term $(S_T - K)$ has zero second derivative, so:

    $$
    \frac{\partial^2(K - S_T)^+}{\partial S_T^2} = \frac{\partial^2(S_T - K)^+}{\partial S_T^2} - 0 = \delta(S_T - K)
    $$

    Both call and put payoffs produce the same second derivative because they share the same "kink" at $S_T = K$, just oriented in opposite directions. The Dirac delta captures this curvature singularity, which is identical in both cases.

---

**Exercise 2.** Using the sifting property of the Dirac delta function, evaluate the following integral:

$$
\int_0^{\infty} \delta(S - K) \, S^2 \sigma^2(S, T) \, p(S, T) \, dS
$$

where $p(S, T)$ is the risk-neutral density. Explain the financial interpretation of this result in the context of the Dupire PDE.

??? success "Solution to Exercise 2"
    Using the sifting property $\int_{-\infty}^{\infty}\delta(S - K)f(S)\,dS = f(K)$:

    $$
    \int_0^{\infty}\delta(S - K)\,S^2\sigma^2(S, T)\,p(S, T)\,dS = K^2\sigma^2(K, T)\,p(K, T)
    $$

    The Dirac delta selects the integrand evaluated at $S = K$.

    **Financial interpretation:** This quantity appears in the diffusion term of the Dupire PDE. In the derivation, the extended Ito formula applied to the call payoff produces the term $\frac{1}{2}\mathbb{E}^Q[\delta(S_T - K)\sigma^2(S_T, T)S_T^2]$, which evaluates to:

    $$
    \frac{1}{2}K^2\sigma^2(K, T)\,p(K, T) = \frac{1}{2}\sigma^2(K, T)K^2 e^{rT}C_{KK}
    $$

    using the Breeden-Litzenberger identity $p(K, T) = e^{rT}C_{KK}$. This is precisely the denominator of the Dupire formula multiplied by $\sigma^2(K, T)$. Economically, this represents the contribution of the local variance at strike $K$ to the rate of change of the option price, weighted by the probability of the underlying being at $K$ at time $T$. It measures how much the diffusion of the underlying at the strike price contributes to the option's time value.

---

**Exercise 3.** The gamma of a European call option satisfies $\Gamma = e^{-rT} p(K, T)$. Suppose the risk-neutral density at maturity $T = 1$ is lognormal with parameters $\mu = \ln(100) + (0.05 - 0.5 \times 0.04)$ and $\sigma = 0.2$. Compute the gamma for a call with strike $K = 100$, risk-free rate $r = 5\%$, and current spot $S_0 = 100$.

??? success "Solution to Exercise 3"
    Given: lognormal density with $\mu = \ln(100) + (0.05 - 0.5 \times 0.04) = \ln(100) + 0.03$, $\sigma = 0.2$, $T = 1$, $K = 100$, $r = 0.05$.

    The lognormal density at $S = K = 100$ is:

    $$
    p(100, 1) = \frac{1}{100 \times 0.2\sqrt{2\pi \times 1}}\exp\!\left(-\frac{(\ln 100 - \mu)^2}{2 \times 0.04 \times 1}\right)
    $$

    Computing $\ln 100 - \mu = \ln 100 - \ln 100 - 0.03 = -0.03$:

    $$
    p(100, 1) = \frac{1}{100 \times 0.2\sqrt{2\pi}}\exp\!\left(-\frac{(-0.03)^2}{0.08}\right) = \frac{1}{20\sqrt{2\pi}}\exp\!\left(-\frac{0.0009}{0.08}\right)
    $$

    $$
    = \frac{1}{20 \times 2.5066}\exp(-0.01125) = \frac{1}{50.133} \times 0.98882 = 0.01972
    $$

    The gamma is:

    $$
    \Gamma = e^{-rT}p(K, T) = e^{-0.05}\times 0.01972 = 0.9512 \times 0.01972 \approx 0.01876
    $$

    This means a $\$1$ move in the spot price changes the delta by approximately $0.019$.

---

**Exercise 4.** Consider the "straddle" payoff $|S_T - K|$. Write this payoff in terms of call and put payoffs, then compute its first and second distributional derivatives with respect to $S_T$. Show that the second derivative involves a constant term plus a Dirac delta contribution.

??? success "Solution to Exercise 4"
    The straddle payoff is $|S_T - K| = (S_T - K)^+ + (K - S_T)^+$.

    This decomposition follows from $|x| = x^+ + (-x)^+ = \max(x, 0) + \max(-x, 0)$.

    **First distributional derivative:**

    $$
    \frac{\partial|S_T - K|}{\partial S_T} = \frac{\partial(S_T - K)^+}{\partial S_T} + \frac{\partial(K - S_T)^+}{\partial S_T} = \mathbf{1}(S_T > K) + (-\mathbf{1}(S_T < K))
    $$

    $$
    = \mathbf{1}(S_T > K) - \mathbf{1}(S_T < K) = \text{sgn}(S_T - K)
    $$

    where $\text{sgn}$ is the sign function (equals $+1$ for $S_T > K$ and $-1$ for $S_T < K$).

    **Second distributional derivative:**

    $$
    \frac{\partial^2|S_T - K|}{\partial S_T^2} = \frac{\partial}{\partial S_T}\text{sgn}(S_T - K) = 2\delta(S_T - K)
    $$

    The factor of 2 arises because the sign function jumps by 2 (from $-1$ to $+1$) at $S_T = K$. Equivalently, from the decomposition:

    $$
    \frac{\partial^2|S_T - K|}{\partial S_T^2} = \delta(S_T - K) + \delta(S_T - K) = 2\delta(S_T - K)
    $$

    Each of the call and put payoff contributes one Dirac delta. There is no "constant term" in the second derivative -- the second distributional derivative is purely singular, consisting only of the Dirac delta contribution with coefficient 2. The straddle has twice the gamma of a single call or put at the same strike.

---

**Exercise 5.** Starting from the extended Ito formula applied to $(S_T - K)^+$, verify that taking expectations of both sides and differentiating with respect to $T$ produces the Dupire PDE:

$$
C_T + rK C_K + \frac{1}{2}\sigma^2(K, T)K^2 C_{KK} = rC
$$

Identify which step uses the Dirac delta sifting property and which step uses the martingale property of the discounted stock price.

??? success "Solution to Exercise 5"
    Starting from the extended Ito formula applied to $(S_T - K)^+$:

    $$
    (S_T - K)^+ = (S_0 - K)^+ + \int_0^T \mathbf{1}(S_t > K)\,dS_t + \frac{1}{2}\int_0^T \delta(S_t - K)\,d\langle S \rangle_t
    $$

    Substituting $dS_t = rS_t\,dt + \sigma(S_t, t)S_t\,dW_t$ and $d\langle S \rangle_t = \sigma^2(S_t, t)S_t^2\,dt$:

    $$
    (S_T - K)^+ = (S_0 - K)^+ + \int_0^T \mathbf{1}(S_t > K)rS_t\,dt + \int_0^T \mathbf{1}(S_t > K)\sigma(S_t, t)S_t\,dW_t + \frac{1}{2}\int_0^T \delta(S_t - K)\sigma^2(S_t, t)S_t^2\,dt
    $$

    **Taking expectations** (Step using the martingale property): The stochastic integral $\int_0^T \mathbf{1}(S_t > K)\sigma(S_t, t)S_t\,dW_t$ is a martingale (under integrability conditions), so its expectation is zero:

    $$
    \mathbb{E}^Q[(S_T - K)^+] = (S_0 - K)^+ + \int_0^T r\,\mathbb{E}^Q[\mathbf{1}(S_t > K)S_t]\,dt + \frac{1}{2}\int_0^T \sigma^2(K, t)K^2\,\mathbb{E}^Q[\delta(S_t - K)]\,dt
    $$

    **Step using the Dirac delta sifting property:** The term $\mathbb{E}^Q[\delta(S_t - K)\sigma^2(S_t, t)S_t^2] = \sigma^2(K, t)K^2 p(K, t)$, where the delta function selects $S_t = K$, replacing $\sigma^2(S_t, t)S_t^2$ by its value at $S_t = K$.

    **Differentiating with respect to $T$:** Since $C(K, T) = e^{-rT}\mathbb{E}^Q[(S_T - K)^+]$:

    $$
    e^{rT}C_T + re^{rT}C = r\,\mathbb{E}^Q[\mathbf{1}(S_T > K)S_T] + \frac{1}{2}\sigma^2(K, T)K^2 p(K, T)
    $$

    Using $\mathbb{E}^Q[\mathbf{1}(S_T > K)S_T] = e^{rT}(C - KC_K)$ (from the call price integral) and $p(K, T) = e^{rT}C_{KK}$:

    $$
    e^{rT}C_T + re^{rT}C = re^{rT}(C - KC_K) + \frac{1}{2}\sigma^2(K, T)K^2 e^{rT}C_{KK}
    $$

    Dividing by $e^{rT}$:

    $$
    C_T + rC = rC - rKC_K + \frac{1}{2}\sigma^2(K, T)K^2 C_{KK}
    $$

    $$
    C_T = -rKC_K + \frac{1}{2}\sigma^2(K, T)K^2 C_{KK}
    $$

    Rearranging: $C_T + rKC_K + \frac{1}{2}\sigma^2(K, T)K^2 C_{KK} = rC$ -- but note the sign. Correctly:

    $$
    C_T + rKC_K = \frac{1}{2}\sigma^2(K, T)K^2 C_{KK}
    $$

    which gives $C_T + rKC_K - \frac{1}{2}\sigma^2 K^2 C_{KK} = 0$, or equivalently $\frac{1}{2}\sigma^2 K^2 C_{KK} - rKC_K = C_T$, confirming the Dupire PDE.

---

**Exercise 6.** Prove that for any twice-differentiable function $g(S)$ with compact support, the Breeden-Litzenberger identity

$$
g(S_T) = g(F) + g'(F)(S_T - F) + \int_0^F g''(K)(K - S_T)^+ \, dK + \int_F^{\infty} g''(K)(S_T - K)^+ \, dK
$$

holds, where $F = \mathbb{E}^Q[S_T]$. Hint: use the distributional decomposition of $g''$ and the call/put payoff second derivatives.

??? success "Solution to Exercise 6"
    We prove the identity for arbitrary $S_T > 0$. Define the right-hand side as:

    $$
    R = g(F) + g'(F)(S_T - F) + \int_0^F g''(K)(K - S_T)^+\,dK + \int_F^\infty g''(K)(S_T - K)^+\,dK
    $$

    **Case 1: $S_T \geq F$.** In this case, $(K - S_T)^+ = 0$ for $K \leq F \leq S_T$, so the put integral vanishes except when $K > S_T$ (but the domain is $[0, F]$, so it vanishes entirely). The call integral is:

    $$
    \int_F^\infty g''(K)(S_T - K)^+\,dK = \int_F^{S_T} g''(K)(S_T - K)\,dK
    $$

    Integrate by parts with $u = (S_T - K)$ and $dv = g''(K)\,dK$:

    $$
    = \left[(S_T - K)g'(K)\right]_F^{S_T} + \int_F^{S_T} g'(K)\,dK = 0 - (S_T - F)g'(F) + g(S_T) - g(F)
    $$

    Therefore:

    $$
    R = g(F) + g'(F)(S_T - F) - (S_T - F)g'(F) + g(S_T) - g(F) = g(S_T)
    $$

    **Case 2: $S_T < F$.** The call integral vanishes (since $(S_T - K)^+ = 0$ for $K \geq F > S_T$). The put integral is:

    $$
    \int_0^F g''(K)(K - S_T)^+\,dK = \int_{S_T}^F g''(K)(K - S_T)\,dK
    $$

    Integrate by parts with $u = (K - S_T)$ and $dv = g''(K)\,dK$:

    $$
    = \left[(K - S_T)g'(K)\right]_{S_T}^F - \int_{S_T}^F g'(K)\,dK = (F - S_T)g'(F) - 0 - g(F) + g(S_T)
    $$

    Therefore:

    $$
    R = g(F) + g'(F)(S_T - F) + (F - S_T)g'(F) - g(F) + g(S_T)
    $$

    $$
    = g(F) + g'(F)(S_T - F) - g'(F)(S_T - F) - g(F) + g(S_T) = g(S_T)
    $$

    In both cases $R = g(S_T)$, proving the identity. The key insight is that option payoffs $(S_T - K)^+$ and $(K - S_T)^+$ serve as a basis for representing any twice-differentiable function, with $g''(K)$ acting as the "coefficient" at each strike. This is the continuous analogue of representing a function by its Taylor expansion, where the calls and puts replace the polynomial basis functions.
