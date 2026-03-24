# Limiting Cases and Asymptotics

The named functions $B(\tau)$, $A(t,T)$, $V(t,T)$, $\sigma_r^2(t)$, and $\theta(t)$ of the Hull-White model depend on the mean reversion speed $a$ and the volatility $\sigma$. Their behavior in extreme parameter regimes -- $a \to 0$, $a \to \infty$, $\tau \to 0$, $\tau \to \infty$ -- reveals the model's connections to simpler models (Ho-Lee, deterministic rates) and provides approximations useful for intuition, debugging, and numerical validation.

!!! info "Prerequisites"
    - Named functions definition and relationships (sibling sections)
    - Ho-Lee model: $dr = \theta(t)\,dt + \sigma\,dW$
    - Taylor expansion and L'Hopital's rule

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the $a \to 0$ (Ho-Lee) limit of all named functions
    2. Derive the $a \to \infty$ (fast mean reversion) limit
    3. Compute short-maturity and long-maturity asymptotics for $B$, $A$, and $V$
    4. Use limiting formulas for numerical validation of Hull-White implementations

---

## The Duration Function B(tau)

Recall $B(\tau) = (1 - e^{-a\tau})/a$ (positive convention). The limits are:

!!! info "Proposition: Limits of $B(\tau)$"

    $$
    \lim_{a \to 0} B(\tau) = \tau \qquad \lim_{a \to \infty} B(\tau) = 0 \qquad \lim_{\tau \to 0} B(\tau) = 0 \qquad \lim_{\tau \to \infty} B(\tau) = \frac{1}{a}
    $$

???+ note "Proof"
    **$a \to 0$:** Using L'Hopital's rule or the Taylor expansion $e^{-a\tau} = 1 - a\tau + \frac{1}{2}a^2\tau^2 - \cdots$:

    $$
    B(\tau) = \frac{1 - (1 - a\tau + \frac{1}{2}a^2\tau^2 - \cdots)}{a} = \tau - \frac{1}{2}a\tau^2 + \frac{1}{6}a^2\tau^3 - \cdots \;\to\; \tau
    $$

    **$a \to \infty$:** $e^{-a\tau} \to 0$ for $\tau > 0$, so $B(\tau) \to 1/a \to 0$.

    **$\tau \to 0$:** $e^{-a\tau} \to 1$, so $B(\tau) \to 0$.

    **$\tau \to \infty$:** $e^{-a\tau} \to 0$, so $B(\tau) \to 1/a$. $\square$

The Taylor expansion of $B(\tau)$ in powers of $a\tau$ is particularly useful:

$$
B(\tau) = \tau\left(1 - \frac{a\tau}{2} + \frac{(a\tau)^2}{6} - \frac{(a\tau)^3}{24} + \cdots\right)
$$

For $a\tau < 0.1$ (e.g., $a = 0.05$ and $\tau < 2$ years), truncating at the first correction gives $B(\tau) \approx \tau(1 - a\tau/2)$ with relative error below $0.02\%$.

---

## The Ho-Lee Limit (a to 0)

The Ho-Lee model $dr = \theta(t)\,dt + \sigma\,dW$ is the limiting case of Hull-White when mean reversion vanishes. All named functions reduce to simpler expressions.

!!! info "Theorem: Ho-Lee Limits"

    | Hull-White Function | $a \to 0$ Limit (Ho-Lee) |
    |:---|:---|
    | $B(\tau) = \dfrac{1 - e^{-a\tau}}{a}$ | $\tau$ |
    | $\sigma_r^2(t) = \dfrac{\sigma^2}{2a}(1 - e^{-2at})$ | $\sigma^2 t$ |
    | $V(t,T) = \dfrac{\sigma^2}{a^2}\!\left[\tau - 2B(\tau) + \dfrac{B(2\tau)}{2}\right]$ | $\dfrac{\sigma^2 \tau^3}{3}$ |
    | $\theta(t) = f'(0,t) + af(0,t) + \dfrac{\sigma^2}{2a}(1-e^{-2at})$ | $f'(0,t) + \sigma^2 t$ |
    | Bond price $P(t,T)$ | $\dfrac{P^M(0,T)}{P^M(0,t)}\exp\!\left(\tau[f^M(0,t) - r(t)] + \dfrac{\sigma^2}{6}\tau^3\right)$ |

???+ note "Proof of $V(t,T) \to \sigma^2\tau^3/3$"
    Starting from $V = \frac{\sigma^2}{a^2}[\tau - 2B(\tau) + B(2\tau)/2]$ and substituting the Taylor expansions:

    $$
    B(\tau) \approx \tau - \frac{a\tau^2}{2} + \frac{a^2\tau^3}{6}, \qquad B(2\tau) \approx 2\tau - 2a\tau^2 + \frac{4a^2\tau^3}{3}
    $$

    $$
    \tau - 2B(\tau) + \frac{B(2\tau)}{2} \approx \tau - 2\tau + a\tau^2 - \frac{a^2\tau^3}{3} + \tau - a\tau^2 + \frac{2a^2\tau^3}{3} = \frac{a^2\tau^3}{3}
    $$

    Therefore $V \approx \frac{\sigma^2}{a^2} \cdot \frac{a^2\tau^3}{3} = \frac{\sigma^2\tau^3}{3}$. $\square$

???+ note "Proof of $\sigma_r^2(t) \to \sigma^2 t$"
    Expanding $1 - e^{-2at} = 2at - 2a^2t^2 + \cdots$:

    $$
    \sigma_r^2(t) = \frac{\sigma^2}{2a}(2at - 2a^2t^2 + \cdots) = \sigma^2 t - \sigma^2 at^2 + \cdots \;\to\; \sigma^2 t
    $$

    This is the variance of $r(t) = r(0) + \int_0^t \theta(s)\,ds + \sigma W(t)$ in the Ho-Lee model, where $r(t)$ is a Brownian motion with drift. $\square$

!!! tip "Interpretation"
    In the Ho-Lee limit, the short rate variance grows linearly in time (no stabilization), the integrated rate variance grows as $\tau^3$ (faster than $\tau$), and all yield curve movements are exact parallel shifts ($B(\tau)/\tau = 1$ for all $\tau$). The absence of mean reversion makes the model unrealistic for long horizons but useful as a local approximation for short-dated products.

---

## Fast Mean Reversion Limit (a to infinity)

When $a \to \infty$, the short rate reverts instantaneously to $\theta(t)/a$, effectively becoming deterministic. The named functions collapse:

!!! info "Proposition: Fast Mean Reversion Limits"

    $$
    \lim_{a \to \infty} B(\tau) = 0, \qquad \lim_{a \to \infty} \sigma_r^2(t) = 0, \qquad \lim_{a \to \infty} V(t,T) = 0
    $$

    The bond price converges to the market discount factor ratio:

    $$
    \lim_{a \to \infty} P(t,T) = \frac{P^M(0,T)}{P^M(0,t)}
    $$

???+ note "Proof"
    As $a \to \infty$: $e^{-a\tau} \to 0$, so $B(\tau) = (1 - e^{-a\tau})/a \to 1/a \to 0$.

    The variance $\sigma_r^2(t) = \frac{\sigma^2}{2a}(1 - e^{-2at}) \le \frac{\sigma^2}{2a} \to 0$.

    For $V(t,T)$: all three terms in $\tau - 2B(\tau) + B(2\tau)/2$ individually approach $\tau - 0 + 0 = \tau$, but $V = \frac{\sigma^2}{a^2}[\cdots]$ has the $1/a^2$ prefactor, so $V \le \frac{\sigma^2\tau}{a^2} \to 0$.

    In the bond price formula, $B(t,T) \to 0$ eliminates the $r(t)$-dependent and convexity terms, leaving $P(t,T) \to P^M(0,T)/P^M(0,t)$. $\square$

!!! tip "Interpretation"
    Fast mean reversion suppresses all stochastic variation. The short rate tracks $\theta(t)/a$ so closely that the yield curve becomes deterministic. This limit is useful as a sanity check: if an implementation is given $a = 10^6$, all option prices should vanish and bond prices should match the deterministic discounting baseline.

---

## Short-Maturity Asymptotics (tau to 0)

As $\tau \to 0$, the named functions admit Taylor expansions that reveal the local behavior of bond prices near maturity.

!!! info "Proposition: Short-Maturity Expansions"

    $$
    B(\tau) = \tau - \frac{a\tau^2}{2} + \frac{a^2\tau^3}{6} + O(\tau^4)
    $$

    $$
    V(t,T) = \frac{\sigma^2\tau^3}{3} - \frac{\sigma^2 a\tau^4}{6} + O(\tau^5)
    $$

    $$
    A(t,T) = -f^M(0,t)\,\tau + \frac{1}{2}\left[f^M(0,t)^2 + f'(0,t)\right]\tau^2 + O(\tau^3)
    $$

The bond price near maturity satisfies

$$
P(t,T) \approx e^{-r(t)\tau + \frac{1}{2}\sigma_r^{\text{eff}}(\tau)\tau^2 + \cdots}
$$

where the leading term $e^{-r(t)\tau}$ is the simple discounting approximation, valid for $\tau \ll 1/a$.

---

## Long-Maturity Asymptotics (tau to infinity)

As $\tau \to \infty$, all exponentials $e^{-a\tau}$ and $e^{-2a\tau}$ vanish and the named functions approach their asymptotic forms.

!!! info "Proposition: Long-Maturity Limits"

    $$
    B(\tau) \to \frac{1}{a}, \qquad B(\tau)^2 \to \frac{1}{a^2}
    $$

    $$
    V(t,T) \to \frac{\sigma^2}{a^2}\left[\tau - \frac{2}{a} + \frac{1}{2a}\right] = \frac{\sigma^2}{a^2}\left(\tau - \frac{3}{2a}\right)
    $$

    The long yield converges to a constant determined by $P^M(0,T)$:

    $$
    \lim_{\tau \to \infty} R(t,T) = \lim_{\tau \to \infty}\left(-\frac{\ln P^M(0,T)}{\tau}\right) + O(1/\tau) = \bar{f}
    $$

    where $\bar{f}$ is the asymptotic forward rate of the market curve.

The sensitivity of the long yield to the short rate vanishes:

$$
\frac{\partial R(t,T)}{\partial r(t)} = \frac{B(\tau)}{\tau} \to \frac{1}{a\tau} \to 0
$$

This confirms that the Hull-White model, being a one-factor model, cannot independently control the long end of the yield curve.

---

## Summary of All Limits

| Function | $a \to 0$ | $a \to \infty$ | $\tau \to 0$ | $\tau \to \infty$ |
|:---|:---:|:---:|:---:|:---:|
| $B(\tau)$ | $\tau$ | $0$ | $\tau$ | $1/a$ |
| $B(\tau)/\tau$ | $1$ | $0$ | $1$ | $0$ |
| $\sigma_r^2(t)$ | $\sigma^2 t$ | $0$ | $0$ | $\sigma^2/(2a)$ |
| $V(t,T)$ | $\sigma^2\tau^3/3$ | $0$ | $\sigma^2\tau^3/3$ | $\sim\sigma^2\tau/a^2$ |
| $\theta(t)$ | $f'(0,t) + \sigma^2 t$ | $\to \infty$ (absorbs $af$) | $f'(0,0) + af(0,0)$ | $f'(0,t) + af(0,t) + \sigma^2/(2a)$ |

---

## Numerical Validation Example

The limiting formulas provide useful test cases for implementations. Consider $a = 0.001$ (near Ho-Lee) with $\sigma = 0.01$ and $\tau = 5$:

**Exact:**

$$
B(5) = \frac{1 - e^{-0.005}}{0.001} = \frac{1 - 0.99501}{0.001} = 4.9875
$$

**Ho-Lee approximation:** $B(5) \approx 5$. Relative error: $0.25\%$.

**First-order correction:** $B(5) \approx 5(1 - 0.005/2) = 4.9875$. Relative error: $< 10^{-6}$.

For the integrated rate variance:

**Exact:**

$$
V(0,5) = \frac{0.0001}{10^{-6}}\left[5 - 2(4.9875) + \frac{1 - e^{-0.01}}{0.002}\right] \approx 10^5 \times (5 - 9.975 + 4.9875) \approx 4.167 \times 10^{-4} \times 10^5
$$

A careful computation yields $V(0,5) \approx 4.167 \times 10^{-4}$.

**Ho-Lee approximation:** $V(0,5) \approx \frac{0.0001 \times 125}{3} = 4.167 \times 10^{-3}$. This matches to three significant figures, confirming the $a \to 0$ asymptotics.

These test cases should be part of any unit test suite for a Hull-White implementation.

---

## Summary

The named functions of the Hull-White model exhibit clean limiting behavior that connects to simpler models and provides numerical benchmarks. As $a \to 0$, all functions reduce to their Ho-Lee equivalents: $B(\tau) \to \tau$, $\sigma_r^2(t) \to \sigma^2 t$, $V(t,T) \to \sigma^2\tau^3/3$. As $a \to \infty$, stochastic variation vanishes and the model becomes deterministic. Short-maturity expansions recover simple discounting at leading order, while long-maturity limits show that the one-factor structure cannot independently control the long end. These asymptotics serve as essential validation tools for any numerical implementation of the model.

---

## Exercises

**Exercise 1.** Derive the Ho-Lee limit of $\theta(t)$ by taking $a \to 0$ in the formula $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$. Be careful with the indeterminate form in the third term; use L'Hopital's rule or Taylor expansion to show it converges to $\sigma^2 t$.

---

**Exercise 2.** For $a = 0.001$, $\sigma = 0.01$, and $\tau = 5$, compute $B(\tau)$ exactly, using the Ho-Lee approximation $B \approx \tau$, and using the first-order correction $B \approx \tau(1 - a\tau/2)$. Report the relative error of each approximation. At what value of $a\tau$ does the first-order correction achieve a relative error below $10^{-4}$?

---

**Exercise 3.** In the fast mean-reversion limit $a \to \infty$, all option prices should vanish. Explain this result intuitively: what happens to the distribution of $r_t$ when mean reversion is infinitely fast? What does this imply for the value of any convexity-dependent instrument?

---

**Exercise 4.** Derive the short-maturity expansion $V(t,T) = \frac{\sigma^2\tau^3}{3} - \frac{\sigma^2 a\tau^4}{6} + O(\tau^5)$ by substituting the Taylor expansions of $B(\tau)$ and $B(2\tau)$ into the formula $V = \frac{\sigma^2}{a^2}[\tau - 2B(\tau) + B(2\tau)/2]$.

---

**Exercise 5.** The long-maturity yield sensitivity $\partial R/\partial r = B(\tau)/\tau \to 1/(a\tau) \to 0$ shows that long yields are insensitive to the short rate. Explain why this is a fundamental limitation of one-factor models. How does a two-factor extension address this limitation?

---

**Exercise 6.** Design a unit test for a Hull-White implementation using the summary table of limits. Write pseudocode that checks $B(\tau)$, $\sigma_r^2(t)$, and $V(t,T)$ against the Ho-Lee limits for $a = 10^{-6}$ and against the fast-mean-reversion limits for $a = 10^{6}$, with appropriate tolerance bounds.

---

**Exercise 7.** The bond price in the Ho-Lee limit is $P(t,T) = \frac{P^M(0,T)}{P^M(0,t)}\exp(\tau[f^M(0,t) - r(t)] + \frac{\sigma^2}{6}\tau^3)$. Identify the convexity correction term $\frac{\sigma^2}{6}\tau^3$ and explain its sign. Why does this term grow with $\tau^3$ rather than $\tau^2$?
