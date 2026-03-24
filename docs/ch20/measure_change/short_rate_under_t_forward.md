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

---

**Exercise 2.** For $\lambda = 0.05$, $\sigma = 0.01$, and $T = 10$, compute $\theta^T(t) - \theta^{\mathbb{Q}}(t)$ at $t = 0$, $t = 5$, and $t = 9.5$. Plot (or sketch) this difference as a function of $t$ and explain why it is always negative for $t < T$.

---

**Exercise 3.** Verify that the conditional variance $\sigma_r^2(t_0, t) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(t-t_0)})$ is the same under $\mathbb{Q}$ and $\mathbb{Q}^T$ by showing that Girsanov's theorem does not change the quadratic variation of $r(t)$.

---

**Exercise 4.** Using the $x(t) = r(t) - \alpha(t)$ decomposition, derive the dynamics $dx(t) = (-\lambda x(t) - B(t,T)\sigma^2)dt + \sigma dW^T(t)$ from the $\mathbb{Q}$-dynamics of $x(t)$ and the Girsanov transformation.

---

**Exercise 5.** Consider the numerical example with $\lambda = 0.05$, $\sigma = 0.01$, $T = 10$, and $r(0) = 0.03$. Compute $\mu_r^{T=10}(0, 5)$ and $\mu_r^{\mathbb{Q}}(0, 5)$ for a flat forward curve $f^M(0,t) = 0.03$. Verify that $\mu_r^{T=10}(0,5) < \mu_r^{\mathbb{Q}}(0,5)$.

---

**Exercise 6.** Explain why the conditional mean under $\mathbb{Q}^T$ is lower than under $\mathbb{Q}$. Relate this to the fact that the $T$-forward measure tilts probability toward states where bond prices are high (i.e., interest rates are low).

---

**Exercise 7.** For the bond option pricing formula, we need $r(T) \sim \mathcal{N}(\mu_r^T(t_0, T), \sigma_r^2(t_0, T))$ under $\mathbb{Q}^T$. Explain what goes wrong if one mistakenly uses the $\mathbb{Q}$-distribution of $r(T)$ instead. How would the option price be biased?
