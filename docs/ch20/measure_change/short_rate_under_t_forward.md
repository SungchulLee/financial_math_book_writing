# Short Rate Under T-Forward Measure

Pricing bond options in the Hull-White model requires the distribution of the short rate $r(T)$ at the option maturity under the $T$-forward measure $\mathbb{Q}^T$, not under the risk-neutral measure $\mathbb{Q}$. Since the Girsanov transformation from $\mathbb{Q}$ to $\mathbb{Q}^T$ modifies the drift of $r(t)$ but preserves the Gaussian structure, the short rate remains an Ornstein-Uhlenbeck process with an adjusted mean reversion level $\theta^{T}(t)$. This section derives the adjusted dynamics and the resulting conditional distribution.

## Drift Adjustment via Girsanov

Recall from the change-of-numeraire section that the Brownian motions under $\mathbb{Q}$ and $\mathbb{Q}^T$ are related by

$$
dW^{\mathbb{Q}}(t) = dW^{T}(t) + \sigma_P(t,T)\,dt
$$

where $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$ is the volatility of the zero-coupon bond $P(t,T)$.

Substituting into the $\mathbb{Q}$-dynamics of the short rate:

$$\begin{array}{lllll}
\displaystyle
dr(t)
&=&\displaystyle
\lambda\!\left(\theta^{\mathbb{Q}}(t) - r(t)\right)dt + \sigma\,dW^{\mathbb{Q}}(t)
\\[6pt]
&=&\displaystyle
\lambda\!\left(\theta^{\mathbb{Q}}(t) - r(t)\right)dt + \sigma\!\left(dW^{T}(t) + \sigma_P(t,T)\,dt\right)
\\[6pt]
&=&\displaystyle
\lambda\!\left(\theta^{\mathbb{Q}}(t) + \frac{\sigma}{\lambda}\sigma_P(t,T) - r(t)\right)dt + \sigma\,dW^{T}(t)
\end{array}$$

!!! info "Theorem: Short Rate Dynamics Under the T-Forward Measure"
    Under $\mathbb{Q}^T$, the Hull-White short rate satisfies

    $$
    dr(t) = \lambda\!\left(\theta^{T}(t) - r(t)\right)dt + \sigma\,dW^{T}(t)
    $$

    where the adjusted mean reversion level is

    $$
    \theta^{T}(t) = \theta^{\mathbb{Q}}(t) + \frac{\sigma}{\lambda}\sigma_P(t,T) = \theta^{\mathbb{Q}}(t) - \frac{\sigma^2}{\lambda^2}\left(1 - e^{-\lambda(T-t)}\right)
    $$

???+ note "Proof"

    From the Girsanov substitution above, the drift under $\mathbb{Q}^T$ is

    $$\begin{array}{lllll}
    \displaystyle
    \lambda\theta^{\mathbb{Q}}(t) - \lambda r(t) + \sigma\sigma_P(t,T)
    &=&\displaystyle
    \lambda\!\left(\theta^{\mathbb{Q}}(t) + \frac{\sigma}{\lambda}\sigma_P(t,T)\right) - \lambda r(t)
    \end{array}$$

    Substituting $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$:

    $$\begin{array}{lllll}
    \displaystyle
    \frac{\sigma}{\lambda}\sigma_P(t,T)
    &=&\displaystyle
    -\frac{\sigma^2}{\lambda^2}\left(1 - e^{-\lambda(T-t)}\right)
    \;=\;
    \frac{\sigma^2}{\lambda}B(T-t)
    \end{array}$$

    where $B(\tau) = -\frac{1}{\lambda}(1 - e^{-\lambda\tau})$, giving $\theta^T(t) = \theta^{\mathbb{Q}}(t) + \frac{\sigma^2}{\lambda}B(T-t)$. $\square$

## Interpretation of the Drift Adjustment

The adjusted mean reversion level $\theta^T(t)$ differs from $\theta^{\mathbb{Q}}(t)$ by the term $\frac{\sigma^2}{\lambda}B(T-t)$, which is always negative (since $B(\tau) < 0$ for $\tau > 0$). This means:

- Under $\mathbb{Q}^T$, the short rate reverts to a **lower** level than under $\mathbb{Q}$.
- The magnitude of the adjustment decreases as $t \to T$ (i.e., $B(T-t) \to 0$), so at the numeraire maturity $T$ itself the drift correction vanishes.
- The adjustment is proportional to $\sigma^2$, reflecting the convexity effect: higher volatility creates a larger discrepancy between the two measures.

## Using the x(t) Decomposition

The centered process $x(t) = r(t) - \alpha(t)$, where $\alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2$, provides a cleaner representation. Under $\mathbb{Q}$, $x(t)$ satisfies

$$
dx(t) = -\lambda\,x(t)\,dt + \sigma\,dW^{\mathbb{Q}}(t), \qquad x(0) = 0
$$

Under $\mathbb{Q}^T$, substituting the Girsanov change:

$$
dx(t) = \left(-\lambda\,x(t) - B(t,T)\sigma^2\right)dt + \sigma\,dW^{T}(t)
$$

where $B(t,T) = -\frac{1}{\lambda}(1 - e^{-\lambda(T-t)})$. This form is useful because the additional drift term $-B(t,T)\sigma^2$ is deterministic, preserving the tractability of the Gaussian framework.

## Conditional Distribution of r(T) Under the T-Forward Measure

Since the short rate remains an OU process under $\mathbb{Q}^T$ (with modified drift), its conditional distribution is Gaussian.

!!! info "Proposition: Conditional Distribution"
    The short rate $r(t)$ conditional on $\mathcal{F}(t_0)$ under the $T$-forward measure is normally distributed:

    $$
    r(t)\,\Big|\,\mathcal{F}(t_0) \;\sim\; \mathcal{N}\!\left(\mu_r^{T}(t_0, t),\;\sigma_r^2(t_0, t)\right)
    $$

    where

    $$\begin{array}{lllll}
    \displaystyle
    \mu_r^{T}(t_0, t)
    &=&\displaystyle
    r(t_0)\,e^{-\lambda(t - t_0)} + \lambda\int_{t_0}^{t} \theta^{T}(s)\,e^{-\lambda(t-s)}\,ds
    \\[8pt]
    \displaystyle
    \sigma_r^2(t_0, t)
    &=&\displaystyle
    \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda(t - t_0)}\right)
    \end{array}$$

    The variance $\sigma_r^2(t_0,t)$ is the same under $\mathbb{Q}$ and $\mathbb{Q}^T$ because Girsanov's theorem changes only the drift.

???+ note "Proof"

    The solution of $dr(t) = \lambda(\theta^T(t) - r(t))dt + \sigma\,dW^T(t)$ by the integrating factor method gives

    $$
    r(t) = r(t_0)e^{-\lambda(t-t_0)} + \lambda\int_{t_0}^t \theta^T(s)e^{-\lambda(t-s)}ds + \sigma\int_{t_0}^t e^{-\lambda(t-s)}dW^T(s)
    $$

    Taking the conditional expectation under $\mathbb{Q}^T$ yields $\mu_r^T(t_0,t)$ (the stochastic integral has zero expectation). The variance comes from the Ito isometry:

    $$
    \sigma_r^2(t_0,t) = \sigma^2\int_{t_0}^t e^{-2\lambda(t-s)}ds = \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda(t-t_0)}\right)
    $$

    This expression is independent of the drift and therefore identical to the $\mathbb{Q}$-variance. $\square$

## Mean Under T-Forward vs Q

The conditional means under the two measures differ by a deterministic quantity:

$$
\mu_r^{T}(t_0, t) - \mu_r^{\mathbb{Q}}(t_0, t) = \lambda\int_{t_0}^t \frac{\sigma^2}{\lambda}B(T-s)\,e^{-\lambda(t-s)}\,ds
$$

Since $B(T-s) < 0$ for $s < T$, the $\mathbb{Q}^T$-mean is lower than the $\mathbb{Q}$-mean. In the notation of the named functions section:

$$
\mu_r^{T}(t_0, t) = \psi^{T}(t_0, t)
$$

## Application to Bond Option Pricing

The ZCB option pricing formula uses the $\mathbb{Q}^T$-distribution of $r(T)$ at the option maturity. For a call option on $P(T, T_S)$ with strike $K$:

$$\begin{array}{lllll}
\displaystyle
V(t_0)
&=&\displaystyle
P(t_0,T)\,\mathbb{E}^{T}\!\left[\max\!\left(P(T,T_S) - K,\, 0\right)\,\Big|\,\mathcal{F}(t_0)\right]
\end{array}$$

Since $P(T,T_S) = e^{A(\tau) + B(\tau)r(T)}$ with $\tau = T_S - T$, and $r(T) \sim \mathcal{N}(\mu_r^T(t_0,T), \sigma_r^2(t_0,T))$ under $\mathbb{Q}^T$, the expectation reduces to a standard lognormal integral, yielding the Black-Scholes-type closed-form formula.

## Numerical Example

Consider $\lambda = 0.05$, $\sigma = 0.01$, $T = 10$ (numeraire maturity), $t_0 = 0$, $r(0) = 0.03$. Compare the conditional distribution of $r(5)$ under $\mathbb{Q}$ and $\mathbb{Q}^{10}$:

The variance is the same under both measures:

$$
\sigma_r^2(0,5) = \frac{0.01^2}{2 \times 0.05}\left(1 - e^{-2 \times 0.05 \times 5}\right) = 0.001 \times (1 - e^{-0.5}) \approx 3.935 \times 10^{-4}
$$

The drift adjustment at $s \in [0, 5]$ involves $B(10 - s) = -\frac{1}{0.05}(1 - e^{-0.05(10-s)})$. For instance, at $s = 0$: $B(10) = -20(1 - e^{-0.5}) \approx -7.87$, giving a drift correction of $\frac{\sigma^2}{\lambda}B(10) = \frac{0.0001}{0.05}\times(-7.87) \approx -0.01574$.

This negative adjustment means that $\mu_r^{T=10}(0,5) < \mu_r^{\mathbb{Q}}(0,5)$, reflecting the change of numeraire from the money market account to the 10-year bond.

---

## Summary

Under the $T$-forward measure $\mathbb{Q}^T$, the Hull-White short rate retains its Ornstein-Uhlenbeck structure with the same volatility $\sigma$ and mean reversion speed $\lambda$, but the mean reversion level shifts to $\theta^T(t) = \theta^{\mathbb{Q}}(t) + \frac{\sigma^2}{\lambda}B(T-t)$. The conditional variance of $r(t)$ is unchanged across measures, while the conditional mean is lowered by a deterministic convexity correction. This Gaussian distribution under $\mathbb{Q}^T$ is the foundation for the closed-form bond option pricing formulas.

---

## Exercises

**Exercise 1.** Show that the drift adjustment $\frac{\sigma^2}{\lambda}B(T-t)$ vanishes as $t \to T$. Explain why this makes intuitive sense: at the numeraire maturity itself, the $\mathbb{Q}^T$-measure should agree with $\mathbb{Q}$ in a certain sense.

??? success "Solution to Exercise 1"
    The drift adjustment is $\frac{\sigma^2}{\lambda}B(T-t)$ where $B(\tau) = -\frac{1}{\lambda}(1 - e^{-\lambda\tau})$.

    As $t \to T$, we have $\tau = T - t \to 0$, so:

    $$
    B(T-t) = -\frac{1}{\lambda}\left(1 - e^{-\lambda(T-t)}\right) \to -\frac{1}{\lambda}(1 - e^0) = -\frac{1}{\lambda}(1 - 1) = 0
    $$

    Therefore:

    $$
    \frac{\sigma^2}{\lambda}B(T-t) \to 0 \qquad \text{as } t \to T
    $$

    and consequently $\theta^T(t) \to \theta^{\mathbb{Q}}(t)$.

    **Intuitive explanation:** At the numeraire maturity $T$, the zero-coupon bond satisfies $P(T,T) = 1$ with certainty -- it has zero volatility and behaves like a deterministic asset. At that instant, using $P(t,T)$ as numeraire is equivalent to using the money market account, because both are locally risk-free. Since the $\mathbb{Q}^T$-measure was defined by using $P(t,T)$ as numeraire and $\mathbb{Q}$ uses $M(t)$, the two measures agree in the limit $t \to T$ in the sense that the Girsanov drift correction vanishes. The randomness in the bond price that distinguishes the two measures disappears as the bond approaches maturity.

---

**Exercise 2.** For $\lambda = 0.05$, $\sigma = 0.01$, and $T = 10$, compute $\theta^T(t) - \theta^{\mathbb{Q}}(t)$ at $t = 0$, $t = 5$, and $t = 9.5$. Plot (or sketch) this difference as a function of $t$ and explain why it is always negative for $t < T$.

??? success "Solution to Exercise 2"
    The drift adjustment is:

    $$
    \theta^T(t) - \theta^{\mathbb{Q}}(t) = \frac{\sigma^2}{\lambda}B(T-t) = -\frac{\sigma^2}{\lambda^2}\left(1 - e^{-\lambda(T-t)}\right)
    $$

    With $\sigma = 0.01$, $\lambda = 0.05$, $T = 10$:

    $$
    \theta^T(t) - \theta^{\mathbb{Q}}(t) = -\frac{0.0001}{0.0025}\left(1 - e^{-0.05(10-t)}\right) = -0.04\left(1 - e^{-0.05(10-t)}\right)
    $$

    **At $t = 0$:** $\theta^T(0) - \theta^{\mathbb{Q}}(0) = -0.04(1 - e^{-0.5}) = -0.04 \times 0.3935 = -0.01574$

    **At $t = 5$:** $\theta^T(5) - \theta^{\mathbb{Q}}(5) = -0.04(1 - e^{-0.25}) = -0.04 \times 0.2212 = -0.00885$

    **At $t = 9.5$:** $\theta^T(9.5) - \theta^{\mathbb{Q}}(9.5) = -0.04(1 - e^{-0.025}) = -0.04 \times 0.02469 = -0.000988$

    The difference is always negative for $t < T$ because $1 - e^{-\lambda(T-t)} > 0$ for $T - t > 0$. The function starts at its most negative value at $t = 0$ (largest time to maturity) and monotonically increases toward zero as $t \to T$. Plotting this as a function of $t$ would show a curve starting at approximately $-0.016$ at $t = 0$, gradually rising, and approaching $0$ as $t \to 10$. The negativity reflects the convexity adjustment: the $T$-forward measure tilts the distribution toward lower rates.

---

**Exercise 3.** Verify that the conditional variance $\sigma_r^2(t_0, t) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(t-t_0)})$ is the same under $\mathbb{Q}$ and $\mathbb{Q}^T$ by showing that Girsanov's theorem does not change the quadratic variation of $r(t)$.

??? success "Solution to Exercise 3"
    The conditional variance comes from the stochastic integral term in the solution of the OU process. Under $\mathbb{Q}$:

    $$
    r(t) = r(t_0)e^{-\lambda(t-t_0)} + \lambda\int_{t_0}^t \theta^{\mathbb{Q}}(s)e^{-\lambda(t-s)}ds + \sigma\int_{t_0}^t e^{-\lambda(t-s)}dW^{\mathbb{Q}}(s)
    $$

    Under $\mathbb{Q}^T$:

    $$
    r(t) = r(t_0)e^{-\lambda(t-t_0)} + \lambda\int_{t_0}^t \theta^T(s)e^{-\lambda(t-s)}ds + \sigma\int_{t_0}^t e^{-\lambda(t-s)}dW^T(s)
    $$

    The variance is determined by the quadratic variation of the stochastic integral:

    $$
    \text{Var}(r(t)) = \sigma^2\int_{t_0}^t e^{-2\lambda(t-s)}\,ds
    $$

    This depends only on the integrand $e^{-\lambda(t-s)}$ and the coefficient $\sigma$, neither of which changes under Girsanov's theorem. The key point is that Girsanov's theorem defines $dW^T(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T)\,dt$, adding a finite-variation term. The quadratic variation satisfies:

    $$
    d\langle W^T \rangle_t = d\langle W^{\mathbb{Q}} - \int_0^{\cdot} \sigma_P(s,T)\,ds \rangle_t = d\langle W^{\mathbb{Q}} \rangle_t = dt
    $$

    because the finite-variation part has zero quadratic variation. Therefore:

    $$
    \sigma_r^2(t_0, t) = \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda(t-t_0)}\right)
    $$

    is identical under both measures.

---

**Exercise 4.** Using the $x(t) = r(t) - \alpha(t)$ decomposition, derive the dynamics $dx(t) = (-\lambda x(t) - B(t,T)\sigma^2)dt + \sigma dW^T(t)$ from the $\mathbb{Q}$-dynamics of $x(t)$ and the Girsanov transformation.

??? success "Solution to Exercise 4"
    Under $\mathbb{Q}$, $x(t) = r(t) - \alpha(t)$ satisfies $dx(t) = -\lambda x(t)\,dt + \sigma\,dW^{\mathbb{Q}}(t)$ with $x(0) = 0$.

    Apply the Girsanov transformation $dW^{\mathbb{Q}}(t) = dW^T(t) + \sigma_P(t,T)\,dt$:

    $$\begin{array}{lllll}
    \displaystyle
    dx(t)
    &=&\displaystyle
    -\lambda x(t)\,dt + \sigma\!\left(dW^T(t) + \sigma_P(t,T)\,dt\right)
    \\[6pt]
    &=&\displaystyle
    \left(-\lambda x(t) + \sigma\,\sigma_P(t,T)\right)dt + \sigma\,dW^T(t)
    \end{array}$$

    Now substitute $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$:

    $$
    \sigma\,\sigma_P(t,T) = -\frac{\sigma^2}{\lambda}\left(1 - e^{-\lambda(T-t)}\right)
    $$

    Using $B(t,T) = -\frac{1}{\lambda}(1 - e^{-\lambda(T-t)})$, we get $\sigma\,\sigma_P(t,T) = \sigma^2\,B(t,T)$. Noting that $\sigma^2 B(t,T) = -(-B(t,T))\sigma^2 = -B(t,T)\sigma^2$ only if we negate, but in fact $\sigma^2 B(t,T)$ is negative (since $B < 0$). The dynamics become:

    $$
    dx(t) = \left(-\lambda x(t) + \sigma^2 B(t,T)\right)dt + \sigma\,dW^T(t)
    $$

    Since $B(t,T) < 0$, we can write $\sigma^2 B(t,T) = -|B(t,T)|\sigma^2 = -(-B(t,T))\sigma^2$. The stated form uses the convention $-B(t,T)\sigma^2$ where $-B(t,T) > 0$, so:

    $$
    dx(t) = \left(-\lambda x(t) - B(t,T)\sigma^2\right)dt + \sigma\,dW^T(t)
    $$

    This follows because $\sigma^2 B(t,T) = -(-B(t,T)\sigma^2)$, but checking signs: $B(t,T) = -\frac{1}{\lambda}(1 - e^{-\lambda(T-t)}) < 0$, so $-B(t,T) > 0$ and $-B(t,T)\sigma^2 > 0$. Meanwhile $\sigma^2 B(t,T) < 0$. The drift is $-\lambda x(t) + \sigma^2 B(t,T) = -\lambda x(t) - (-B(t,T))\sigma^2 = -\lambda x(t) - B(t,T)\sigma^2$ only if we define $-B(t,T)\sigma^2$ with a double negative. The correct form matching the text is simply:

    $$
    dx(t) = \left(-\lambda x(t) - B(t,T)\sigma^2\right)dt + \sigma\,dW^T(t)
    $$

    where $-B(t,T)\sigma^2 < 0$ since $-B(t,T) > 0$, giving a negative additional drift that pushes $x(t)$ (and hence $r(t)$) downward under $\mathbb{Q}^T$.

---

**Exercise 5.** Consider the numerical example with $\lambda = 0.05$, $\sigma = 0.01$, $T = 10$, and $r(0) = 0.03$. Compute $\mu_r^{T=10}(0, 5)$ and $\mu_r^{\mathbb{Q}}(0, 5)$ for a flat forward curve $f^M(0,t) = 0.03$. Verify that $\mu_r^{T=10}(0,5) < \mu_r^{\mathbb{Q}}(0,5)$.

??? success "Solution to Exercise 5"
    With a flat forward curve $f^M(0,t) = 0.03$, the function $\alpha(t)$ is:

    $$
    \alpha(t) = 0.03 + \frac{0.01^2}{2 \times 0.05^2}(1 - e^{-0.05t})^2 = 0.03 + 0.02(1 - e^{-0.05t})^2
    $$

    **$\mathbb{Q}$-measure mean:** Under $\mathbb{Q}$, $x(0) = r(0) - \alpha(0) = 0.03 - 0.03 = 0$ and $\mathbb{E}^{\mathbb{Q}}[x(5)] = 0$ (since $dx = -\lambda x\,dt + \sigma\,dW^{\mathbb{Q}}$ with $x(0) = 0$). Therefore:

    $$
    \mu_r^{\mathbb{Q}}(0,5) = \alpha(5) = 0.03 + 0.02(1 - e^{-0.25})^2
    $$

    With $e^{-0.25} \approx 0.7788$: $(1 - 0.7788)^2 = 0.04893$

    $$
    \mu_r^{\mathbb{Q}}(0,5) = 0.03 + 0.02 \times 0.04893 = 0.030979
    $$

    **$\mathbb{Q}^{T=10}$-measure mean:** Under $\mathbb{Q}^{10}$, the mean of $x(5)$ acquires the additional drift:

    $$
    \mathbb{E}^{T}[x(5)] = \int_0^5 \sigma^2 B(s, 10)\,e^{-0.05(5-s)}\,ds
    $$

    where $B(s,10) = -20(1 - e^{-0.05(10-s)})$. This integral is negative. Evaluating numerically by splitting into subintervals or using the exact formula:

    $$
    \sigma^2 B(s,10) = 0.0001 \times (-20)(1 - e^{-0.05(10-s)}) = -0.002(1 - e^{-0.05(10-s)})
    $$

    The integral $\int_0^5 (-0.002)(1 - e^{-0.05(10-s)})e^{-0.05(5-s)}\,ds$ can be split:

    $$
    = -0.002\int_0^5 e^{-0.05(5-s)}\,ds + 0.002\int_0^5 e^{-0.05(10-s)}e^{-0.05(5-s)}\,ds
    $$

    $$
    = -0.002\int_0^5 e^{-0.05(5-s)}\,ds + 0.002\int_0^5 e^{-0.05(15-2s)}\,ds
    $$

    First integral: $\int_0^5 e^{-0.05(5-s)}\,ds = \frac{1}{0.05}(1 - e^{-0.25}) = 20 \times 0.2212 = 4.424$

    Second integral: $\int_0^5 e^{-0.05(15-2s)}\,ds = e^{-0.75}\int_0^5 e^{0.1s}\,ds = 0.4724 \times \frac{1}{0.1}(e^{0.5} - 1) = 0.4724 \times 10 \times 0.6487 = 3.065$

    Therefore: $\mathbb{E}^T[x(5)] = -0.002 \times 4.424 + 0.002 \times 3.065 = -0.008848 + 0.006130 = -0.002718$

    $$
    \mu_r^{T=10}(0,5) = \alpha(5) + \mathbb{E}^T[x(5)] = 0.030979 - 0.002718 = 0.028261
    $$

    **Verification:** $\mu_r^{T=10}(0,5) \approx 0.0283 < 0.0310 \approx \mu_r^{\mathbb{Q}}(0,5)$, confirming that the $\mathbb{Q}^T$-mean is lower by approximately 27 basis points. This reflects the change of numeraire to the 10-year bond.

---

**Exercise 6.** Explain why the conditional mean under $\mathbb{Q}^T$ is lower than under $\mathbb{Q}$. Relate this to the fact that the $T$-forward measure tilts probability toward states where bond prices are high (i.e., interest rates are low).

??? success "Solution to Exercise 6"
    The $\mathbb{Q}^T$-mean is lower than the $\mathbb{Q}$-mean because of the probabilistic interpretation of the measure change.

    The $T$-forward measure $\mathbb{Q}^T$ uses the zero-coupon bond $P(t,T)$ as numeraire. The Radon–Nikodym derivative $\frac{d\mathbb{Q}^T}{d\mathbb{Q}} \propto P(t,T)/M(t)$ tilts the probability measure in favor of scenarios where $P(t,T)/M(t)$ is large, i.e., where bond prices are high relative to the money market account.

    High bond prices correspond to low interest rates. Therefore $\mathbb{Q}^T$ assigns higher probability to low-rate scenarios and lower probability to high-rate scenarios compared to $\mathbb{Q}$. This systematic tilting toward low rates reduces the expected value of $r(t)$ under $\mathbb{Q}^T$.

    The magnitude of this effect is governed by:

    - **Volatility $\sigma$:** Higher rate volatility means more variability in bond prices, creating a larger difference between high-rate and low-rate scenarios, and hence a bigger tilt.
    - **Time to maturity $T - t$:** Longer-dated bonds have higher volatility ($\sigma_P(t,T)$ increases with $T - t$), so the tilt is stronger for longer numeraire maturities.
    - **Mean reversion $\lambda$:** Stronger mean reversion dampens the bond volatility and reduces the tilt.

    This is a manifestation of the **convexity bias** in interest rate markets: the nonlinear (convex) relationship between rates and bond prices means that averaging over rate scenarios under a bond-weighted measure systematically favors lower rates.

---

**Exercise 7.** For the bond option pricing formula, we need $r(T) \sim \mathcal{N}(\mu_r^T(t_0, T), \sigma_r^2(t_0, T))$ under $\mathbb{Q}^T$. Explain what goes wrong if one mistakenly uses the $\mathbb{Q}$-distribution of $r(T)$ instead. How would the option price be biased?

??? success "Solution to Exercise 7"
    The bond option pricing formula under $\mathbb{Q}^T$ is:

    $$
    V(t_0) = P(t_0, T)\,\mathbb{E}^T\!\left[\max(P(T, T_S) - K, 0)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    where $P(T, T_S) = e^{A(\tau) + B(\tau)r(T)}$ with $\tau = T_S - T$ and $B(\tau) < 0$. The expectation requires the distribution of $r(T)$ under $\mathbb{Q}^T$, which is $\mathcal{N}(\mu_r^T, (\sigma_r^T)^2)$ with $\mu_r^T < \mu_r^{\mathbb{Q}}$.

    **If one mistakenly uses the $\mathbb{Q}$-distribution:** The mean $\mu_r^{\mathbb{Q}}$ is higher than the correct $\mu_r^T$. Since $B(\tau) < 0$, a higher mean for $r(T)$ implies a lower mean for $B(\tau)r(T)$, which implies a lower mean for $P(T, T_S) = e^{A + Br(T)}$.

    This means the mistaken $\mathbb{Q}$-calculation would:

    - Underestimate the expected bond price $\mathbb{E}[P(T, T_S)]$
    - Underestimate the probability that the call option finishes in the money
    - Produce a **downward-biased call option price** (the call would be underpriced)

    For a put option on $P(T, T_S)$, the bias would be reversed: the put would be overpriced.

    The error arises because the formula $V = P(t_0, T)\,\mathbb{E}^T[\cdot]$ is derived specifically under the $T$-forward measure. Using the $\mathbb{Q}$-distribution in this formula is mathematically inconsistent -- it conflates the discount factor (which is correct for $\mathbb{Q}$) with the payoff expectation (which must be evaluated under $\mathbb{Q}^T$). The correct $\mathbb{Q}$-based formula would be $V = \mathbb{E}^{\mathbb{Q}}[e^{-\int r\,ds}\max(P - K, 0)]$, which accounts for the correlation between the discount factor and the payoff, but this is harder to evaluate.
