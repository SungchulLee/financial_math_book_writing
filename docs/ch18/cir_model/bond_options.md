# Bond Options Under the CIR Model

European options on zero-coupon bonds are among the most important building blocks for interest rate derivatives. In the CIR model, these options admit closed-form pricing formulas involving the non-central chi-squared distribution --- a direct consequence of the affine structure and the fact that the CIR process preserves its distributional family under the $T$-forward measure change. This section derives the CIR bond option formula, explains the critical rate that separates exercise from non-exercise, and establishes put-call parity for bond options.

---

## Setup and payoff structure

Consider a European call option with maturity $T$ and strike $K$ written on a zero-coupon bond with maturity $S > T$. At expiry, the call pays

$$
C_T = \big(P(T, S) - K\big)^+
$$

Since $P(T,S) = A(S-T)\,e^{-B(S-T)\,r_T}$ is a decreasing function of $r_T$, the option is exercised when $r_T$ is sufficiently low --- specifically, when $P(T,S) > K$.

The corresponding European put has payoff

$$
P_T = \big(K - P(T, S)\big)^+
$$

which is exercised when $r_T$ is sufficiently high.

---

## Critical rate

The bond price $P(T,S) = A(S-T)e^{-B(S-T)r_T}$ equals the strike $K$ when

$$
A(S-T)\,e^{-B(S-T)\,r^*} = K
$$

Solving for the critical rate $r^*$:

$$
r^* = \frac{1}{B(S-T)}\ln\frac{A(S-T)}{K}
$$

The call is exercised when $r_T < r^*$ and the put is exercised when $r_T > r^*$. This critical rate plays the role of the "strike" in rate space and is the threshold that separates the exercise region from the no-exercise region.

!!! note "Analogy with Black-Scholes"
    In the Black-Scholes model, the critical stock price equals the strike directly. In bond option pricing, the critical rate $r^*$ translates the bond-price strike $K$ into the rate domain. The monotone relationship between $P(T,S)$ and $r_T$ ensures a unique critical rate.

---

## Pricing via the T-forward measure

Using the $T$-forward measure $\mathbb{Q}^T$ from the change-of-measure section, the call price at time $t$ is

$$
C(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[\big(P(T,S) - K\big)^+\,\big|\,\mathcal{F}_t\right]
$$

Expanding using the bond price formula:

$$
C(t) = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[\big(A(S-T)e^{-B(S-T)r_T} - K\big)^+\,\big|\,\mathcal{F}_t\right]
$$

Since the exercise region is $\{r_T < r^*\}$:

$$
C(t) = P(t,T)\left[A(S-T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[e^{-B(S-T)r_T}\,\mathbf{1}_{\{r_T < r^*\}}\,\big|\,\mathcal{F}_t\right] - K\,\mathbb{Q}^T(r_T < r^*\,|\,\mathcal{F}_t)\right]
$$

---

## Distribution of the short rate under the forward measure

Under $\mathbb{Q}^T$, the short rate $r_T$ given $r_t$ follows a scaled non-central chi-squared distribution. Define the parameters:

$$
\psi = \frac{(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma}{2\gamma}
$$

$$
\phi = \frac{2\gamma\,e^{\gamma(T-t)}}{\sigma^2\left[(\gamma + \kappa)(e^{\gamma(T-t)}-1) + 2\gamma\right]}
$$

Under the $T$-forward measure, let $c^T$, $d$, and $\lambda^T$ denote the scale, degrees of freedom, and non-centrality parameters respectively:

$$
d = \frac{4\kappa\theta}{\sigma^2}
$$

The non-centrality parameter depends on the current rate:

$$
\lambda^T = \lambda^T(r_t, t, T)
$$

where the explicit form involves the integrated time-dependent drift coefficients from the forward-measure CIR dynamics.

---

## Closed-form call option formula

The CIR call option price is

$$
C(t) = P(t,S)\,\chi^2\!\left(2r^*(\phi + \psi + B(S-T));\; d,\; \lambda_1\right) - K\,P(t,T)\,\chi^2\!\left(2r^*(\phi + \psi);\; d,\; \lambda_2\right)
$$

where $\chi^2(x;\,d,\,\lambda)$ denotes the cumulative distribution function of the non-central chi-squared distribution with $d$ degrees of freedom and non-centrality parameter $\lambda$, evaluated at $x$.

The parameters are:

$$
\phi = \frac{2\gamma}{\sigma^2(e^{\gamma(T-t)} - 1)}
$$

$$
\psi = \frac{\kappa + \gamma}{\sigma^2}
$$

$$
\lambda_1 = \frac{2\phi^2\,r_t\,e^{\gamma(T-t)}}{\phi + \psi + B(S-T)}
$$

$$
\lambda_2 = \frac{2\phi^2\,r_t\,e^{\gamma(T-t)}}{\phi + \psi}
$$

$$
d = \frac{4\kappa\theta}{\sigma^2}
$$

$$
r^* = \frac{1}{B(S-T)}\ln\frac{A(S-T)}{K}
$$

???+ note "Derivation sketch"

    The key step is decomposing the call payoff expectation under $\mathbb{Q}^T$ into two terms. The first term involves $\mathbb{E}^{\mathbb{Q}^T}[e^{-B(S-T)r_T}\mathbf{1}_{\{r_T < r^*\}}]$, which amounts to computing a moment-generating-function-weighted probability under the non-central chi-squared distribution. This can be evaluated using the following property: if $X \sim \chi^2(d, \lambda)$, then $\mathbb{E}[e^{-\alpha X}\mathbf{1}_{\{X < x\}}]$ can be expressed in terms of a non-central chi-squared CDF with adjusted parameters.

    Specifically, multiplying by $e^{-B(S-T)r_T}$ shifts the non-centrality parameter and scale of the chi-squared distribution, producing the parameters $\lambda_1$ and the adjusted argument involving $\phi + \psi + B(S-T)$ in the first CDF. The second term is simply the forward-measure probability $\mathbb{Q}^T(r_T < r^*)$, which is a standard non-central chi-squared CDF with parameters $\lambda_2$ and argument involving $\phi + \psi$.

    The prefactors $P(t,S)$ and $K\,P(t,T)$ arise from collecting the deterministic terms $A(S-T)P(t,T)$ and recognizing that $A(S-T)P(t,T) \cdot (\text{normalization}) = P(t,S)$. $\square$

---

## Put option formula and put-call parity

The European put on the same zero-coupon bond is obtained via **put-call parity** for bond options:

$$
C(t) - P_{\text{put}}(t) = P(t,S) - K\,P(t,T)
$$

This follows from the identity $(x - K)^+ - (K - x)^+ = x - K$ applied to $x = P(T,S)$ and discounting under $\mathbb{Q}$. The put price is therefore

$$
P_{\text{put}}(t) = K\,P(t,T)\left[1 - \chi^2\!\left(2r^*(\phi + \psi);\; d,\; \lambda_2\right)\right] - P(t,S)\left[1 - \chi^2\!\left(2r^*(\phi + \psi + B(S-T));\; d,\; \lambda_1\right)\right]
$$

!!! tip "Computational note"
    The non-central chi-squared CDF is available in standard numerical libraries (e.g., `scipy.stats.ncx2.cdf` in Python). For large non-centrality parameters, the series representation converges slowly; in such cases, asymptotic approximations or saddle-point methods improve numerical stability.

---

## Special cases and limiting behavior

### At-the-money forward

When $K = P(t,S)/P(t,T)$ (the forward bond price), the critical rate $r^*$ simplifies and the two chi-squared CDFs have similar magnitudes, analogous to the Black-Scholes at-the-money case where $N(d_1) \approx N(d_2)$.

### Short expiry limit

As $T - t \to 0$, the distribution of $r_T$ under $\mathbb{Q}^T$ concentrates at $r_t$, and the option price converges to its intrinsic value $(P(t,S) - K)^+$.

### Zero volatility limit

When $\sigma \to 0$, the CIR model becomes deterministic, the non-central chi-squared distribution degenerates to a point mass, and the option price becomes either $P(t,S) - K\,P(t,T)$ (if in the money) or zero (if out of the money).

---

## Numerical example

Consider CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.1$, with $r_0 = 0.05$. Price a European call with expiry $T = 1$ year on a zero-coupon bond maturing at $S = 5$ years, with strike $K = 0.80$.

**Step 1**: Compute $\gamma = \sqrt{0.25 + 0.02} \approx 0.5196$.

**Step 2**: Compute bond prices $P(0,1) \approx 0.9519$ and $P(0,5) \approx 0.7817$.

**Step 3**: Compute the critical rate:

$$
r^* = \frac{1}{B(4)}\ln\frac{A(4)}{0.80}
$$

**Step 4**: Compute $\phi$, $\psi$, $\lambda_1$, $\lambda_2$, $d$ and evaluate the non-central chi-squared CDFs.

**Step 5**: Combine to get the call price $C(0)$.

The exact numerical evaluation requires the non-central chi-squared CDF, which is handled by the Python implementation in a later section.

---

## Summary

The CIR model provides closed-form European bond option prices through the non-central chi-squared distribution. The formula decomposes the call price into two terms --- each involving a non-central chi-squared CDF with different parameters --- analogous to the two normal CDF terms in the Black-Scholes formula. The critical rate $r^* = \frac{1}{B(S-T)}\ln(A(S-T)/K)$ translates the bond strike into the rate domain. Put-call parity $C - P = P(t,S) - KP(t,T)$ completes the framework. The non-central chi-squared distribution arises because the CIR process preserves its distributional family under the $T$-forward measure change, making the entire derivation possible without numerical PDE solvers.
