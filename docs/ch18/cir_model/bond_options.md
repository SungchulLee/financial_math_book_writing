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

---

## Exercises

**Exercise 1.** For CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.1$, compute $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$. Then compute the bond price functions $A(4)$ and $B(4)$ for a 4-year zero-coupon bond. Given a strike $K = 0.80$, find the critical rate $r^* = \frac{1}{B(4)}\ln\frac{A(4)}{K}$.

??? success "Solution to Exercise 1"

    We are given $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.1$.

    **Step 1: Compute $\gamma$.**

    $$
    \gamma = \sqrt{\kappa^2 + 2\sigma^2} = \sqrt{0.25 + 0.02} = \sqrt{0.27} \approx 0.5196
    $$

    **Step 2: Compute $B(4)$.**

    First, $e^{\gamma \cdot 4} = e^{0.5196 \times 4} = e^{2.0785} \approx 7.991$.

    $$
    B(4) = \frac{2(e^{\gamma \cdot 4} - 1)}{(\gamma + \kappa)(e^{\gamma \cdot 4} - 1) + 2\gamma} = \frac{2(7.991 - 1)}{(0.5196 + 0.5)(7.991 - 1) + 2(0.5196)}
    $$

    $$
    = \frac{2 \times 6.991}{1.0196 \times 6.991 + 1.0392} = \frac{13.982}{7.128 + 1.039} = \frac{13.982}{8.167} \approx 1.712
    $$

    **Step 3: Compute $A(4)$.**

    Let $D(4) = (\gamma + \kappa)(e^{\gamma \cdot 4} - 1) + 2\gamma = 8.167$ (from above). The exponent is $2\kappa\theta/\sigma^2 = 2(0.5)(0.06)/0.01 = 6$.

    $$
    A(4) = \left(\frac{2\gamma \, e^{(\kappa + \gamma) \cdot 4/2}}{D(4)}\right)^6 = \left(\frac{1.0392 \times e^{2.0392}}{8.167}\right)^6
    $$

    $$
    = \left(\frac{1.0392 \times 7.684}{8.167}\right)^6 = \left(\frac{7.986}{8.167}\right)^6 \approx (0.9778)^6 \approx 0.8742
    $$

    **Step 4: Compute $r^*$.**

    $$
    r^* = \frac{1}{B(4)} \ln \frac{A(4)}{K} = \frac{1}{1.712} \ln \frac{0.8742}{0.80} = \frac{1}{1.712} \ln(1.0928) = \frac{0.0887}{1.712} \approx 0.0518
    $$

    The critical rate is approximately $r^* \approx 5.18\%$.

---

**Exercise 2.** Explain the economic meaning of the critical rate $r^*$. If $r_T < r^*$, why is the call option on the bond exercised? How does the critical rate change if the strike $K$ increases? What happens in the limiting case $K \to 0$ and $K \to 1$?

??? success "Solution to Exercise 2"

    The critical rate $r^*$ is the short rate at option expiry $T$ that makes the underlying bond price exactly equal to the strike: $P(T,S) = K$. It translates the bond-price strike into the rate domain.

    **Why the call is exercised when $r_T < r^*$:** The bond price $P(T,S) = A(S-T)e^{-B(S-T)r_T}$ is a **decreasing** function of $r_T$. When $r_T < r^*$, the bond price exceeds $K$, so the call payoff $(P(T,S) - K)^+ > 0$ and the option is exercised.

    **Effect of increasing $K$:** From $r^* = \frac{1}{B(S-T)}\ln\frac{A(S-T)}{K}$, increasing $K$ decreases the ratio $A(S-T)/K$, which decreases $\ln(A(S-T)/K)$, and therefore decreases $r^*$. A higher strike means the bond price must be even higher (rates must be even lower) for exercise, so the exercise region shrinks.

    **Limiting case $K \to 0$:** Then $\ln(A/K) \to +\infty$, so $r^* \to +\infty$. The call is almost always exercised since virtually any rate satisfies $r_T < r^*$.

    **Limiting case $K \to 1$:** Since $P(T,S) \leq 1$ for positive rates, and $A(S-T) < 1$ for $S - T > 0$, we have $A/K < 1$, so $\ln(A/K) < 0$ and $r^* < 0$. Since the CIR process is non-negative, $r_T < r^* < 0$ is impossible, and the call is never exercised. The option is worthless.

---

**Exercise 3.** The CIR call option formula involves two non-central chi-squared CDF evaluations with different parameters $\lambda_1$ and $\lambda_2$. Explain the role of each term by analogy with the Black-Scholes formula $C = S\,\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$. Which CIR term corresponds to the "delta-weighted asset value" and which to the "discounted strike probability"?

??? success "Solution to Exercise 3"

    The Black-Scholes call formula is $C = S\,\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$, where:

    - The first term $S\,\mathcal{N}(d_1)$ is the delta-weighted asset value --- the present value of the asset conditional on exercise, weighted by the probability of exercise under the stock-numeraire measure.
    - The second term $Ke^{-rT}\mathcal{N}(d_2)$ is the discounted strike times the risk-neutral exercise probability.

    In the CIR bond option formula:

    $$
    C(t) = P(t,S)\,\chi^2(x_1;\,d,\,\lambda_1) - K\,P(t,T)\,\chi^2(x_2;\,d,\,\lambda_2)
    $$

    - **First term** $P(t,S)\,\chi^2(x_1; d, \lambda_1)$: This is the analogue of $S\,\mathcal{N}(d_1)$. Here $P(t,S)$ plays the role of the underlying asset price $S$, and $\chi^2(x_1; d, \lambda_1)$ is the exercise probability under a measure change that uses $P(t,S)$ as numeraire (the $S$-forward measure). The parameter shift from $\lambda_2$ to $\lambda_1$ (which involves $B(S-T)$) reflects this additional measure change, analogous to the shift from $d_2$ to $d_1$ in Black-Scholes.

    - **Second term** $K\,P(t,T)\,\chi^2(x_2; d, \lambda_2)$: This is the analogue of $Ke^{-rT}\mathcal{N}(d_2)$. Here $K\,P(t,T)$ is the present value of the strike, and $\chi^2(x_2; d, \lambda_2)$ is the exercise probability under the $T$-forward measure $\mathbb{Q}^T$.

    The key structural parallel is that both formulas decompose the call price into "asset leg minus strike leg," each weighted by an exercise probability under a different numeraire measure.

---

**Exercise 4.** Verify put-call parity for CIR bond options. Starting from $C(t) - P_{\text{put}}(t) = P(t,S) - K\,P(t,T)$, use the call formula involving $\chi^2(x_1; d, \lambda_1)$ and $\chi^2(x_2; d, \lambda_2)$ to derive the put formula. Show that the complementary probabilities $1 - \chi^2(\cdot)$ appear naturally.

??? success "Solution to Exercise 4"

    Starting from the call formula:

    $$
    C(t) = P(t,S)\,\chi^2(x_1; d, \lambda_1) - K\,P(t,T)\,\chi^2(x_2; d, \lambda_2)
    $$

    Put-call parity states:

    $$
    C(t) - P_{\text{put}}(t) = P(t,S) - K\,P(t,T)
    $$

    Solving for the put:

    $$
    P_{\text{put}}(t) = C(t) - P(t,S) + K\,P(t,T)
    $$

    $$
    = P(t,S)\,\chi^2(x_1; d, \lambda_1) - K\,P(t,T)\,\chi^2(x_2; d, \lambda_2) - P(t,S) + K\,P(t,T)
    $$

    Regrouping:

    $$
    = K\,P(t,T)\left[1 - \chi^2(x_2; d, \lambda_2)\right] - P(t,S)\left[1 - \chi^2(x_1; d, \lambda_1)\right]
    $$

    The complementary probabilities $1 - \chi^2(\cdot)$ appear naturally because the put is exercised when $r_T > r^*$ (the complement of the call exercise event $r_T < r^*$). This is exactly the put formula stated in the section, confirming that put-call parity holds for CIR bond options.

---

**Exercise 5.** In the zero-volatility limit $\sigma \to 0$, the CIR model becomes deterministic with $r_t = \theta + (r_0 - \theta)e^{-\kappa t}$. For $\kappa = 0.5$, $\theta = 0.06$, $r_0 = 0.05$, compute $r_T$ at $T = 1$ year. Then compute $P(T, S)$ for $S = 5$ directly (using the deterministic forward rate) and determine whether a call with strike $K = 0.80$ would be exercised.

??? success "Solution to Exercise 5"

    With $\sigma = 0$, the CIR SDE becomes the ODE $dr_t = \kappa(\theta - r_t)\,dt$ with solution:

    $$
    r_t = \theta + (r_0 - \theta)e^{-\kappa t}
    $$

    For $\kappa = 0.5$, $\theta = 0.06$, $r_0 = 0.05$, at $T = 1$:

    $$
    r_1 = 0.06 + (0.05 - 0.06)e^{-0.5} = 0.06 - 0.01 \times 0.6065 = 0.06 - 0.006065 = 0.053935
    $$

    To compute $P(T,S) = P(1,5)$, we need $\int_1^5 r_s\,ds$ with the deterministic rate path $r_s = 0.06 + (0.053935 - 0.06)e^{-0.5(s-1)}$:

    $$
    \int_1^5 r_s\,ds = \int_1^5 \left[0.06 - 0.006065\,e^{-0.5(s-1)}\right]ds
    $$

    $$
    = 0.06 \times 4 - 0.006065 \times \frac{1 - e^{-2}}{0.5} = 0.24 - 0.006065 \times 1.7293 = 0.24 - 0.01049 = 0.22951
    $$

    Therefore:

    $$
    P(1,5) = e^{-0.22951} \approx 0.7948
    $$

    Since $P(1,5) \approx 0.7948 < K = 0.80$, the call with strike $K = 0.80$ would **not** be exercised. In the deterministic case, the rate is too high for the bond price to exceed the strike.

---

**Exercise 6.** For the at-the-money forward case $K = P(t,S)/P(t,T)$, show that the critical rate $r^*$ satisfies $B(S-T)\,r^* = \ln A(S-T) - \ln K$. Express $r^*$ in terms of the model yield $R(t,T,S) = -\ln P(t,S)/(S-T) + \ln P(t,T)/(S-T)$ and the functions $A$, $B$. What does the ATM condition imply about the relative magnitudes of $\lambda_1$ and $\lambda_2$?

??? success "Solution to Exercise 6"

    At the money forward, $K = P(t,S)/P(t,T)$. The critical rate satisfies:

    $$
    B(S-T)\,r^* = \ln A(S-T) - \ln K = \ln A(S-T) - \ln\frac{P(t,S)}{P(t,T)}
    $$

    Since $P(t,S) = A(S-t)e^{-B(S-t)r_t}$ and $P(t,T) = A(T-t)e^{-B(T-t)r_t}$:

    $$
    \ln\frac{P(t,S)}{P(t,T)} = \ln\frac{A(S-t)}{A(T-t)} - [B(S-t) - B(T-t)]r_t
    $$

    The model yield spread is $R(t,T,S) = \frac{\ln P(t,T) - \ln P(t,S)}{S-T}$, so $\ln(P(t,S)/P(t,T)) = -(S-T)R(t,T,S)$.

    Substituting back:

    $$
    r^* = \frac{\ln A(S-T) + (S-T)R(t,T,S)}{B(S-T)}
    $$

    **Relative magnitudes of $\lambda_1$ and $\lambda_2$:** Recall

    $$
    \lambda_1 = \frac{2\phi^2 r_t e^{\gamma(T-t)}}{\phi + \psi + B(S-T)}, \qquad \lambda_2 = \frac{2\phi^2 r_t e^{\gamma(T-t)}}{\phi + \psi}
    $$

    Since $B(S-T) > 0$, the denominator of $\lambda_1$ is larger than that of $\lambda_2$, so $\lambda_1 < \lambda_2$. At the ATM forward condition, the two chi-squared CDFs have similar magnitudes (analogous to $\mathcal{N}(d_1) \approx \mathcal{N}(d_2)$ in Black-Scholes ATM), but they are not exactly equal because the non-central chi-squared distribution is not symmetric and the parameter shift affects the distribution shape.

---

**Exercise 7.** The non-central chi-squared CDF can be numerically unstable for large non-centrality parameters $\lambda$. For $d = 12$, $\lambda = 500$, explain why the series representation $\chi^2(x; d, \lambda) = \sum_{k=0}^{\infty} e^{-\lambda/2}\frac{(\lambda/2)^k}{k!}\,F_{\chi^2(d+2k)}(x)$ converges slowly. What alternative numerical methods (saddle-point approximation, Gaussian approximation) could be used, and under what conditions are they accurate?

??? success "Solution to Exercise 7"

    The series $\chi^2(x; d, \lambda) = \sum_{k=0}^{\infty} e^{-\lambda/2}\frac{(\lambda/2)^k}{k!}\,F_{\chi^2(d+2k)}(x)$ is a Poisson-weighted sum where the weights are $w_k = e^{-\lambda/2}(\lambda/2)^k/k!$.

    For $\lambda = 500$, the Poisson mean is $\lambda/2 = 250$. The weights $w_k$ are negligible for $k$ far from 250. Specifically, most of the probability mass concentrates around $k \approx 250 \pm \sqrt{250} \approx 250 \pm 16$. The series thus requires summing $O(\sqrt{\lambda})$ terms with significant weight, which means roughly 30--50 terms are needed. However, each term involves evaluating a central chi-squared CDF $F_{\chi^2(d+2k)}(x)$ with very large degrees of freedom ($d + 2k \approx 512$), and computing the Poisson weights for large $k$ involves factorials that overflow standard floating-point arithmetic without careful use of log-space computation.

    **Alternative methods:**

    1. **Gaussian (normal) approximation:** For large $\lambda$, the non-central chi-squared is approximately normal: $\chi^2(d, \lambda) \approx \mathcal{N}(d + \lambda,\, 2(d + 2\lambda))$. For $d = 12$, $\lambda = 500$: mean $\approx 512$, variance $\approx 2024$. This approximation is accurate when $\lambda \gg d$, with error $O(1/\sqrt{\lambda})$.

    2. **Saddle-point approximation:** This uses the cumulant generating function of the non-central chi-squared to produce a more accurate approximation than the Gaussian. The saddle-point method is accurate to $O(1/\lambda)$ and handles the skewness of the distribution, making it superior to the normal approximation for tail probabilities.

    The Gaussian approximation is accurate for central quantiles when $\lambda \gg 1$. The saddle-point approximation is preferable for tail probabilities (deep in- or out-of-the-money options) where the normal approximation's symmetry assumption introduces larger errors.
