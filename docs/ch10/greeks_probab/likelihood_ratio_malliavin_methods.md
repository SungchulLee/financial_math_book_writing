# Likelihood Ratio and Malliavin-Type Methods


Likelihood ratio methods move derivatives from the payoff to the distribution, enabling Greeks for nonsmooth payoffs.

---

## Score identity


If $X^\theta$ has density $p_\theta$,

$$
V(\theta)=\mathbb{E}_\theta[\Phi(X^\theta)]
=\int \Phi(x)p_\theta(x)\,\mathrm{d}x
$$


then

$$
\boxed{
V'(\theta)=\mathbb{E}_\theta\!\left[\Phi(X^\theta)\frac{\partial}{\partial \theta}\log p_\theta(X^\theta)\right]
}
$$


This avoids $\Phi'$. The quantity $\frac{\partial}{\partial\theta}\log p_\theta$ is called the **score function**.

---

## Black–Scholes: Explicit LR estimators


In Black–Scholes, $\log S_T = \log S + (r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z$ where $Z \sim \mathcal{N}(0,1)$.

The density of $Z$ is $p(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}$, so $\frac{\partial}{\partial z}\log p(z) = -z$.

**Delta via LR.** Treating $S$ as a location parameter:

$$
\boxed{\Delta = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot \frac{Z}{S\sigma\sqrt{\tau}}\right]}
$$

where $Z = \frac{\log(S_T/S) - (r-\frac12\sigma^2)\tau}{\sigma\sqrt{\tau}}$ is the driving standard normal.

**Verification.** For a call, this yields $\Delta = N(d_1)$ after evaluation.

**Vega via LR.** The volatility appears in both the drift and diffusion:

$$
\boxed{\nu = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot \frac{Z^2 - 1 - Z\sigma\sqrt{\tau}}{\sigma}\right]}
$$

Alternatively:

$$
\nu = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot \left(\frac{Zd_1}{\sigma} - \sqrt{\tau}\right)\right]
$$

**Gamma via LR.** The LR gamma estimator involves the second derivative of the log-density:

$$
\boxed{\Gamma = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot \frac{Z^2 - Z\sigma\sqrt{\tau} - 1}{S^2\sigma^2\tau}\right]}
$$

This formula works even for digital options where pathwise gamma is undefined.

---

## Variance comparison


LR estimators often have higher variance than pathwise estimators:

| Greek | Pathwise variance | LR variance | Ratio |
|:------|:------------------|:------------|:------|
| Delta (smooth) | $\mathcal{O}(1)$ | $\mathcal{O}(1/\tau)$ | LR worse for short $\tau$ |
| Vega (smooth) | $\mathcal{O}(\tau)$ | $\mathcal{O}(1)$ | Comparable |
| Gamma (kinked) | N/A | $\mathcal{O}(1/\tau)$ | Only LR available |

**Variance reduction.** Control variates and antithetic sampling can significantly reduce LR variance.

---

## Malliavin calculus perspective (conceptual)


For diffusions driven by Brownian motion, Malliavin calculus provides a systematic framework for LR-type formulas.

**Key objects:**
- **Malliavin derivative** $D_s X_T$: sensitivity of $X_T$ to perturbations of $W_s$
- **Skorokhod integral** $\delta(\cdot)$: adjoint of $D$
- **Malliavin covariance** $\langle DX_T, DX_T \rangle_{L^2[0,T]}$

**Integration by parts formula.** For $F = \Phi(X_T)$ and suitable $u$:

$$
\mathbb{E}[\Phi'(X_T) \cdot u] = \mathbb{E}[\Phi(X_T) \cdot H(u)]
$$

where $H(u)$ is a **Malliavin weight** involving Skorokhod integrals and the inverse Malliavin covariance.

---

## Explicit Malliavin weights for Black–Scholes


**Delta weight:**

$$
H_\Delta = \frac{W_T - W_t}{S\sigma\tau} = \frac{\sqrt{\tau}Z}{S\sigma\tau} = \frac{Z}{S\sigma\sqrt{\tau}}
$$

This recovers the LR delta formula.

**Gamma weight:** The second-order Malliavin weight is:

$$
\boxed{H_\Gamma = \frac{1}{S^2\sigma^2\tau}\left(H_2(Z) - \frac{Z}{\sigma\sqrt{\tau}}\right)}
$$

where $H_2(z) = z^2 - 1$ is the second Hermite polynomial. This gives:

$$
\Gamma = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot H_\Gamma\right]
$$

**Vega weight:**

$$
H_\nu = \frac{Z^2 - 1}{\sigma} - \sqrt{\tau}Z
$$

---

## Localization and truncation


Near maturity, LR weights can have heavy tails (e.g., $Z/\sqrt{\tau}$ blows up). Practical implementations use:

1. **Truncation**: Cap $|Z|$ at some threshold
2. **Localization**: Use pathwise methods away from kinks, LR near kinks
3. **Smoothing**: Replace digital payoffs with smooth approximations

---

## Applications beyond vanilla options


LR/Malliavin methods are essential for:

- **Digital options**: Pathwise delta is undefined
- **Barrier options**: Delta involves hitting probabilities
- **Asian options**: Multiple sources of non-smoothness
- **Path-dependent exotics**: Complex dependence on trajectory

---

## What to remember


- LR/Malliavin methods handle kinked payoffs well by moving derivatives to the density.
- Explicit LR formulas exist for all Black–Scholes Greeks.
- The cost is potentially high variance from heavy-tailed weights, especially for short maturities.
- Malliavin calculus provides the theoretical foundation; Hermite polynomials appear in higher-order weights.
- Practical implementations combine pathwise (away from kinks) with LR (near kinks).

---

## Exercises

**Exercise 1.** For the Black--Scholes model with $S_T = S\exp((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z)$, verify the LR delta formula $\Delta = \mathbb{E}[e^{-r\tau}\Phi(S_T) \cdot Z/(S\sigma\sqrt{\tau})]$ by applying it to a European call $\Phi(x) = (x-K)^+$ and showing it yields $N(d_1)$.

??? success "Solution to Exercise 1"
    We have $S_T = S\exp\!\left((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z\right)$ with $Z \sim \mathcal{N}(0,1)$. The LR delta formula is

    $$
    \Delta = \mathbb{E}\!\left[e^{-r\tau}(S_T - K)^+ \cdot \frac{Z}{S\sigma\sqrt{\tau}}\right]
    $$

    The condition $S_T > K$ is equivalent to $Z > -d_2$ where $d_2 = \frac{\ln(S/K) + (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$. So:

    $$
    \Delta = \frac{e^{-r\tau}}{S\sigma\sqrt{\tau}}\int_{-d_2}^{\infty}(S e^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z} - K)\,z\,\frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz
    $$

    Split into two integrals:

    $$
    I_1 = \frac{e^{-r\tau}}{S\sigma\sqrt{\tau}}\int_{-d_2}^{\infty} S e^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z}\,z\,\frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz
    $$

    Completing the square: $(r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z - \frac{z^2}{2} = r\tau - \frac{1}{2}(z - \sigma\sqrt{\tau})^2$. Substituting $u = z - \sigma\sqrt{\tau}$:

    $$
    I_1 = \frac{1}{\sigma\sqrt{\tau}}\int_{-d_1}^{\infty}(u + \sigma\sqrt{\tau})\frac{e^{-u^2/2}}{\sqrt{2\pi}}\,du = \frac{1}{\sigma\sqrt{\tau}}\!\left[N'(d_1) + \sigma\sqrt{\tau}\,N(d_1)\right]
    $$

    using $\int_{-d_1}^{\infty} u\,\phi(u)\,du = \phi(d_1) = N'(d_1)$ and $\int_{-d_1}^{\infty}\phi(u)\,du = N(d_1)$.

    For the second integral:

    $$
    I_2 = -\frac{Ke^{-r\tau}}{S\sigma\sqrt{\tau}}\int_{-d_2}^{\infty}z\,\frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz = -\frac{Ke^{-r\tau}}{S\sigma\sqrt{\tau}}N'(d_2)
    $$

    Since $N'(d_2) = N'(d_1) \cdot \frac{S}{Ke^{-r\tau}}$ (which follows from $d_1 = d_2 + \sigma\sqrt{\tau}$ and the identity $SN'(d_1) = Ke^{-r\tau}N'(d_2)$), we get $I_2 = -\frac{N'(d_1)}{\sigma\sqrt{\tau}}$.

    Combining: $\Delta = I_1 + I_2 = \frac{N'(d_1)}{\sigma\sqrt{\tau}} + N(d_1) - \frac{N'(d_1)}{\sigma\sqrt{\tau}} = N(d_1)$.

---

**Exercise 2.** The LR vega estimator involves the weight $(Z^2 - 1 - Z\sigma\sqrt{\tau})/\sigma$. Compute the variance of this weight for $\sigma = 0.20$ and $\tau = 0.25$. Compare it to the variance of the pathwise vega weight $S_T(\sqrt{\tau}Z - \sigma\tau)$. Which has higher variance?

??? success "Solution to Exercise 2"
    The LR vega weight is $w_{\text{LR}} = \frac{Z^2 - 1 - Z\sigma\sqrt{\tau}}{\sigma}$.

    Since $Z \sim \mathcal{N}(0,1)$, we compute each moment:

    - $\mathbb{E}[Z^2] = 1$, $\mathbb{E}[Z^4] = 3$, $\mathbb{E}[Z^3] = 0$, $\mathbb{E}[Z] = 0$

    The variance is $\text{Var}(w_{\text{LR}}) = \mathbb{E}[w_{\text{LR}}^2] - (\mathbb{E}[w_{\text{LR}}])^2$.

    First, $\mathbb{E}[w_{\text{LR}}] = \frac{\mathbb{E}[Z^2] - 1 - \sigma\sqrt{\tau}\mathbb{E}[Z]}{\sigma} = \frac{1 - 1 - 0}{\sigma} = 0$.

    Next, $w_{\text{LR}}^2 = \frac{(Z^2-1)^2 - 2(Z^2-1)Z\sigma\sqrt{\tau} + Z^2\sigma^2\tau}{\sigma^2}$. Taking expectations:

    - $\mathbb{E}[(Z^2-1)^2] = \mathbb{E}[Z^4 - 2Z^2 + 1] = 3 - 2 + 1 = 2$
    - $\mathbb{E}[(Z^2-1)Z] = \mathbb{E}[Z^3 - Z] = 0$
    - $\mathbb{E}[Z^2] = 1$

    So $\text{Var}(w_{\text{LR}}) = \frac{2 + \sigma^2\tau}{\sigma^2} = \frac{2}{0.04} + 0.25 = 50 + 0.25 = 50.25$.

    For the pathwise vega weight $w_{\text{PW}} = S_T(\sqrt{\tau}Z - \sigma\tau)$, the variance depends on the joint distribution of $S_T$ and $Z$. Since $S_T = Se^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z}$:

    $$
    \text{Var}(w_{\text{PW}}) = S^2\,\text{Var}\!\left(e^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z}(\sqrt{\tau}Z - \sigma\tau)\right)
    $$

    This requires computing $\mathbb{E}[e^{2\sigma\sqrt{\tau}Z}(\sqrt{\tau}Z - \sigma\tau)^2]$ and similar terms. Using moment generating function techniques with $S=100$, $\sigma=0.20$, $\tau=0.25$, $r=0.05$:

    The pathwise weight has variance of order $S^2\tau \cdot e^{\sigma^2\tau} \approx 10000 \times 0.25 \times 1.01 \approx 2525$.

    The LR weight variance is $50.25$ (dimensionless), but it multiplies $e^{-2r\tau}\mathbb{E}[\Phi(S_T)^2]$ in the full estimator variance. For comparable payoff scales, the LR estimator often has higher variance than pathwise because of the $2/\sigma^2 = 50$ term, which dominates for small $\sigma$.

---

**Exercise 3.** The Malliavin delta weight is $H_\Delta = Z/(S\sigma\sqrt{\tau})$. For $\tau = 1/252$ (one day), $\sigma = 0.20$, $S = 100$, compute $\mathbb{E}[H_\Delta^2]$ and explain why LR estimators have high variance for short maturities.

??? success "Solution to Exercise 3"
    The Malliavin delta weight is $H_\Delta = \frac{Z}{S\sigma\sqrt{\tau}}$, so

    $$
    H_\Delta^2 = \frac{Z^2}{S^2\sigma^2\tau}
    $$

    Since $Z \sim \mathcal{N}(0,1)$, $\mathbb{E}[Z^2] = 1$. Therefore:

    $$
    \mathbb{E}[H_\Delta^2] = \frac{1}{S^2\sigma^2\tau}
    $$

    Substituting $S = 100$, $\sigma = 0.20$, $\tau = 1/252$:

    $$
    \mathbb{E}[H_\Delta^2] = \frac{1}{100^2 \times 0.04 \times (1/252)} = \frac{1}{10000 \times 0.04/252} = \frac{252}{400} = 0.63
    $$

    While $\mathbb{E}[H_\Delta^2] = 0.63$ may seem moderate, the issue is the $1/\tau$ scaling. The **variance of the full LR delta estimator** is

    $$
    \text{Var}\!\left(e^{-r\tau}\Phi(S_T) H_\Delta\right) \geq \text{Var}(H_\Delta) \cdot (\text{typical payoff scale})^2
    $$

    and $\text{Var}(H_\Delta) = \frac{1}{S^2\sigma^2\tau} \propto \frac{1}{\tau}$. As $\tau \to 0$:

    - The weight $H_\Delta = Z/(S\sigma\sqrt{\tau})$ has standard deviation $1/(S\sigma\sqrt{\tau})$, which blows up as $\sqrt{252} \approx 15.87$ for one-day maturity compared to $1$ for one-year maturity.
    - Individual sample contributions $\Phi(S_T) \cdot H_\Delta$ can be very large in magnitude, causing the Monte Carlo average to converge slowly.
    - The number of paths needed for a given accuracy scales as $O(1/\tau)$, making LR estimation impractical for very short maturities without variance reduction.

---

**Exercise 4.** Consider a digital call with payoff $\Phi(S_T) = \mathbf{1}_{S_T > K}$. Explain why pathwise differentiation fails for this payoff (what is $\Phi'$?), while the LR method produces a valid estimator. Write down the LR delta estimator for the digital call.

??? success "Solution to Exercise 4"
    The digital call payoff is $\Phi(S_T) = \mathbf{1}_{S_T > K}$.

    **Why pathwise differentiation fails:** The pathwise delta formula requires $\Phi'(S_T)$. For the digital payoff, $\Phi$ is discontinuous at $S_T = K$:

    $$
    \Phi'(x) = \delta(x - K) \quad \text{(Dirac delta, in the distributional sense)}
    $$

    This is not a function, and $\Phi$ is not Lipschitz continuous (the essential requirement for pathwise methods). The dominated convergence theorem fails because the difference quotients $\frac{\Phi(x+h) - \Phi(x)}{h}$ do not converge to an integrable function near $x = K$: they oscillate wildly (being $\pm 1/h$ in a neighborhood of $K$).

    **The LR method produces a valid estimator** because it avoids differentiating $\Phi$ entirely. Using the score function $\frac{Z}{S\sigma\sqrt{\tau}}$:

    $$
    \Delta_{\text{digital}} = \mathbb{E}\!\left[e^{-r\tau}\mathbf{1}_{S_T > K} \cdot \frac{Z}{S\sigma\sqrt{\tau}}\right]
    $$

    This is well-defined because $\mathbf{1}_{S_T > K}$ is bounded and $Z/(S\sigma\sqrt{\tau})$ has finite moments. The estimator involves only the payoff itself (not its derivative) multiplied by the score weight.

    Expanding, with $Z = \frac{\log(S_T/S) - (r-\frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$:

    $$
    \Delta_{\text{digital}} = \frac{e^{-r\tau}}{S\sigma\sqrt{\tau}}\mathbb{E}\!\left[\mathbf{1}_{S_T > K} \cdot Z\right] = \frac{e^{-r\tau}}{S\sigma\sqrt{\tau}}\int_{-d_2}^{\infty} z\,\frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz = \frac{e^{-r\tau} N'(d_2)}{S\sigma\sqrt{\tau}}
    $$

    This equals the known digital delta $\frac{e^{-r\tau}N'(d_2)}{S\sigma\sqrt{\tau}}$.

---

**Exercise 5.** The Malliavin gamma weight involves the second Hermite polynomial $H_2(z) = z^2 - 1$. Show that $\mathbb{E}[H_2(Z)] = 0$ and $\mathbb{E}[H_2(Z)^2] = 2$ for $Z \sim \mathcal{N}(0,1)$. Why does the appearance of Hermite polynomials in higher-order weights increase the variance of the estimator?

??? success "Solution to Exercise 5"
    Let $Z \sim \mathcal{N}(0,1)$ and $H_2(z) = z^2 - 1$.

    **Show $\mathbb{E}[H_2(Z)] = 0$:**

    $$
    \mathbb{E}[H_2(Z)] = \mathbb{E}[Z^2 - 1] = \mathbb{E}[Z^2] - 1 = 1 - 1 = 0
    $$

    **Show $\mathbb{E}[H_2(Z)^2] = 2$:**

    $$
    \mathbb{E}[H_2(Z)^2] = \mathbb{E}[(Z^2 - 1)^2] = \mathbb{E}[Z^4 - 2Z^2 + 1]
    $$

    Using $\mathbb{E}[Z^4] = 3$ (the fourth moment of a standard normal):

    $$
    \mathbb{E}[H_2(Z)^2] = 3 - 2(1) + 1 = 2
    $$

    These results are special cases of the orthogonality relation for Hermite polynomials: $\mathbb{E}[H_m(Z)H_n(Z)] = n!\,\delta_{mn}$. For $m = n = 2$: $\mathbb{E}[H_2(Z)^2] = 2! = 2$. For $m = 2, n = 0$: $\mathbb{E}[H_2(Z) \cdot 1] = 0$.

    **Why Hermite polynomials increase variance of higher-order estimators:**

    The $n$-th order Malliavin weight involves $H_n(Z)$, whose variance is $n!$. Since $n!$ grows rapidly:

    - $\text{Var}(H_1) = 1! = 1$ (delta weights)
    - $\text{Var}(H_2) = 2! = 2$ (gamma weights)
    - $\text{Var}(H_3) = 3! = 6$ (third-order speed/color weights)
    - $\text{Var}(H_n) = n!$ (general $n$-th order)

    The factorial growth means that LR/Malliavin estimators for higher-order Greeks have inherently higher variance. Moreover, the weights are multiplied by $1/(S^n\sigma^n\tau^{n/2})$ factors, compounding the variance issue. This is why gamma LR estimators require significantly more paths than delta estimators, and why third-order Greeks via LR methods are rarely practical without aggressive variance reduction.

---

**Exercise 6.** A practitioner wants to estimate gamma for a barrier option near the barrier. She has access to both finite-difference and LR methods. The finite-difference method uses step $h = 1$, and the LR method uses $N = 100{,}000$ Monte Carlo paths. Discuss the tradeoffs: which method is likely more accurate near the barrier, and why? What variance reduction techniques could improve the LR estimator?

??? success "Solution to Exercise 6"
    **Finite-difference method near the barrier:**

    For a barrier option, the price function $V(S)$ has a discontinuity (or kink) in its first or second derivative at the barrier level $B$. The finite-difference gamma estimator

    $$
    \hat{\Gamma} = \frac{V(S+h) - 2V(S) + V(S-h)}{h^2}
    $$

    with $h = 1$ has a problem when $S$ is near $B$: the shifted points $S \pm h$ may straddle the barrier, so $V(S+h)$ and $V(S-h)$ come from different regimes (one above, one below the barrier). This introduces large bias that does not decrease with more Monte Carlo paths. The finite-difference approximation effectively smooths the gamma over a window of width $2h$, missing the sharp localized behavior near the barrier.

    **LR method near the barrier:**

    The LR gamma estimator

    $$
    \hat{\Gamma}_{\text{LR}} = \frac{1}{N}\sum_{i=1}^N e^{-r\tau}\Phi(S_T^{(i)}) \cdot w_\Gamma(Z^{(i)})
    $$

    does not require perturbing $S$. It evaluates the payoff at the actual stock price and uses the Malliavin/LR weight to capture the second-order sensitivity. Near the barrier, the payoff $\Phi(S_T)$ varies sharply, and the LR weights can have high variance, but the estimator is **unbiased** for any $S$ (including near the barrier).

    **Which is more accurate near the barrier?** The LR method is likely more accurate because:

    - It is unbiased at the exact value of $S$, whereas finite differences introduce bias from straddling the barrier
    - With $N = 100{,}000$ paths, the standard error can be controlled
    - The finite-difference bias near barriers can be the dominant error source and cannot be reduced by adding paths

    **Variance reduction techniques for the LR estimator:**

    - **Control variates:** Use a related vanilla option (whose LR gamma is known analytically) as a control variate to reduce variance
    - **Antithetic variates:** Pair each path $Z^{(i)}$ with $-Z^{(i)}$ to reduce variance from odd moments
    - **Importance sampling:** Tilt the distribution to sample more paths near the barrier, where the payoff variation is greatest
    - **Stratified sampling:** Stratify on $Z$ to ensure uniform coverage of the probability space
    - **Conditional Monte Carlo:** Condition on the maximum/minimum of the path (relevant for barrier options) to reduce the indicator-function-induced variance
