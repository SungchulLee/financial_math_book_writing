# Relationships Between Named Functions

The Hull-White model involves a collection of named functions -- $B(\tau)$, $A(t,T)$, $\theta(t)$, $\psi(t)$, $\alpha(t)$, $\sigma_r^2(t)$, and $V(t,T)$ -- that appear in different contexts (bond pricing, option pricing, simulation, calibration). These functions are not independent: they are connected by a web of algebraic and differential relationships that reflect the internal consistency of the model. Understanding these relationships is essential for verifying implementations, simplifying derivations, and recognizing when different-looking formulas are in fact equivalent. This section catalogs the key relationships and proves the most important ones.

!!! info "Prerequisites"
    - Named functions definition (sibling section)
    - Derivation via Riccati equations (sibling section)
    - Hull-White SDE, solution, and conditional distribution
    - Affine bond price formula

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State all major named functions and their definitions
    2. Derive relationships between $B$, $A$, $\theta$, $\psi$, $\alpha$, and $V$
    3. Express bond prices, yields, and forward rates using named functions
    4. Verify internal consistency of the Hull-White formulas
    5. Translate between different notational conventions in the literature

---

## Catalog of Named Functions

For reference, the complete set of named functions with $\tau = T - t$:

| Function | Definition | Role |
|:---|:---|:---|
| $B(\tau)$ | $\dfrac{1-e^{-a\tau}}{a}$ | Duration-like function (note: positive convention) |
| $\theta(t)$ | $f'(0,t) + af(0,t) + \dfrac{\sigma^2}{2a}(1-e^{-2at})$ | Time-dependent drift |
| $\alpha(t)$ | $f(0,t) + \dfrac{\sigma^2}{2a^2}(1-e^{-at})^2$ | Deterministic mean of $r_t$ |
| $\psi(t)$ | $r_0 e^{-at} + a\displaystyle\int_0^t \theta(u) e^{-a(t-u)}\, du$ | Expected short rate given $r_0$ |
| $\sigma_r^2(t)$ | $\dfrac{\sigma^2}{2a}(1-e^{-2at})$ | Variance of $r_t$ given $r_0$ |
| $V(t,T)$ | $\dfrac{\sigma^2}{a^2}\!\left[\tau - 2B(\tau) + \dfrac{1-e^{-2a\tau}}{2a}\right]$ | Variance of $\int_t^T r_s\, ds$ |
| $A(t,T)$ | $\ln\dfrac{P(0,T)}{P(0,t)} + B(\tau) f(0,t) + \dfrac{\sigma^2}{4a} B(\tau)^2(1-e^{-2at})$ | Bond price intercept |

Here $B(\tau)$ uses the **positive** convention $B(\tau) = (1-e^{-a\tau})/a > 0$, so the bond price is $P(t,T) = e^{A(t,T) - B(\tau) r_t}$.

---

## Fundamental Relationships

### B and Its Derivatives

The function $B(\tau) = (1-e^{-a\tau})/a$ satisfies the ODE

$$
B'(\tau) = e^{-a\tau} = 1 - aB(\tau)
$$

with $B(0) = 0$. This can also be written as $aB(\tau) = 1 - e^{-a\tau}$, or equivalently $e^{-a\tau} = 1 - aB(\tau)$.

!!! note "Proposition: Powers of $B$"
    Useful algebraic identities:

    $$
    B(\tau)^2 = \frac{1}{a^2}\bigl(1 - e^{-a\tau}\bigr)^2 = \frac{1}{a^2}\bigl(1 - 2e^{-a\tau} + e^{-2a\tau}\bigr)
    $$

    $$
    B(2\tau) = \frac{1-e^{-2a\tau}}{a} = B(\tau)(1 + e^{-a\tau}) = B(\tau)(2 - aB(\tau))
    $$

The last identity follows from $1 - e^{-2a\tau} = (1-e^{-a\tau})(1+e^{-a\tau})$.

---

### theta, alpha, and psi

The three drift-related functions are connected by differential relationships.

!!! note "Theorem: $\alpha$ Satisfies the Mean ODE"
    The deterministic mean $\alpha(t)$ satisfies

    $$
    \alpha'(t) = \theta(t) - a\,\alpha(t), \qquad \alpha(0) = r_0
    $$

???+ note "Proof"
    Differentiate $\alpha(t) = f(0,t) + \frac{\sigma^2}{2a^2}(1-e^{-at})^2$:

    $$
    \alpha'(t) = f'(0,t) + \frac{\sigma^2}{a}\, e^{-at}(1 - e^{-at})
    $$

    Now compute $\theta(t) - a\alpha(t)$:

    $$
    \theta(t) - a\alpha(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at}) - af(0,t) - \frac{\sigma^2}{2a}(1-e^{-at})^2
    $$

    $$
    = f'(0,t) + \frac{\sigma^2}{2a}\bigl[(1-e^{-2at}) - (1-e^{-at})^2\bigr]
    $$

    Expanding: $(1-e^{-2at}) - (1-e^{-at})^2 = 1 - e^{-2at} - 1 + 2e^{-at} - e^{-2at} = 2e^{-at}(1 - e^{-at})$.

    Therefore $\theta(t) - a\alpha(t) = f'(0,t) + \frac{\sigma^2}{a} e^{-at}(1-e^{-at}) = \alpha'(t)$. $\square$

!!! note "Corollary: $\psi(t) = \alpha(t)$"
    The expected short rate $\psi(t) = \mathbb{E}[r_t \mid r_0]$ equals $\alpha(t)$:

    $$
    \psi(t) = \alpha(t) = f(0,t) + \frac{\sigma^2}{2a^2}(1-e^{-at})^2
    $$

???+ note "Proof"
    Both $\psi(t)$ and $\alpha(t)$ satisfy the same ODE $y' = \theta(t) - ay$ with $y(0) = r_0$ (since $\alpha(0) = f(0,0) + 0 = r_0$). By uniqueness of ODE solutions, $\psi(t) = \alpha(t)$. $\square$

---

### Variance Functions

!!! note "Theorem: Relationship Between $\sigma_r^2$ and $B$"
    The short rate variance can be expressed as

    $$
    \sigma_r^2(t) = \frac{\sigma^2}{2a}(1 - e^{-2at}) = \frac{\sigma^2}{2}\, B(2t)
    $$

    More generally, the conditional variance starting from time $t_0$ is

    $$
    \sigma_r^2(t_0, t) = \frac{\sigma^2}{2a}(1 - e^{-2a(t-t_0)}) = \frac{\sigma^2}{2}\, B(2(t-t_0))
    $$

The variance of the integrated rate $V(t,T)$ also relates to $B$:

!!! note "Proposition: $V$ in Terms of $B$"

    $$
    V(t,T) = \frac{\sigma^2}{a^2}\left[\tau - 2B(\tau) + \frac{B(2\tau)}{2}\right]
    $$

    where $\tau = T - t$.

???+ note "Proof"
    From the definition:

    $$
    V(t,T) = \frac{\sigma^2}{a^2}\left[\tau - \frac{2(1-e^{-a\tau})}{a} + \frac{1-e^{-2a\tau}}{2a}\right] = \frac{\sigma^2}{a^2}\left[\tau - 2B(\tau) + \frac{B(2\tau)}{2}\right]
    $$

    using $B(\tau) = (1-e^{-a\tau})/a$ and $B(2\tau) = (1-e^{-2a\tau})/a$. $\square$

---

## Bond Price in Named Function Notation

Using the named functions with the positive-$B$ convention:

!!! note "Theorem: Bond Price Formula"

    $$
    P(t,T) = \frac{P(0,T)}{P(0,t)}\, \exp\!\left(B(\tau)\bigl[f(0,t) - r_t\bigr] + \frac{\sigma^2}{4a}\, B(\tau)^2(1 - e^{-2at})\right)
    $$

    Equivalently, using $\alpha(t)$:

    $$
    P(t,T) = \frac{P(0,T)}{P(0,t)}\, \exp\!\left(B(\tau)\bigl[\alpha(t) - r_t\bigr] + \frac{1}{2}\bigl[V(0,T) - V(0,t) - V(t,T)\bigr]\right)
    $$

The second form is useful because $\alpha(t) - r_t = -\tilde{r}_t$ is the zero-mean stochastic part of the short rate from the decomposition $r_t = \alpha(t) + \tilde{r}_t$.

---

## Yield and Forward Rate Formulas

!!! note "Proposition: Yield in Terms of Named Functions"
    The continuously compounded yield for maturity $\tau = T - t$ is

    $$
    y(t,T) = -\frac{\ln P(t,T)}{\tau} = \frac{B(\tau)}{\tau}\, r_t - \frac{A(t,T)}{\tau}
    $$

    Since $B(\tau)/\tau \to 1$ as $\tau \to 0$ and $B(\tau)/\tau \to 0$ as $\tau \to \infty$, the yield is sensitive to $r_t$ at the short end and nearly independent of $r_t$ at the long end.

!!! note "Proposition: Forward Rate in Terms of Named Functions"
    The instantaneous forward rate is

    $$
    f(t,T) = e^{-a\tau}\, r_t + \bigl(1 - e^{-a\tau}\bigr)\alpha(t) + f(0,T) - f(0,t)\, e^{-a\tau} + \text{(convexity terms)}
    $$

    The loading on $r_t$ is $e^{-a\tau} = B'(\tau) = 1 - aB(\tau)$.

---

## Consistency Relations

The named functions satisfy several cross-consistency checks that are useful for verifying implementations.

!!! note "Proposition: Consistency Checks"
    The following identities hold:

    **1. Bond price at $t = 0$:**

    $$
    A(0,T) - B(T)\, r_0 = \ln P(0,T) \quad \Longleftrightarrow \quad P(0,T) = e^{A(0,T) - B(T) r_0}
    $$

    **2. Variance decomposition:**

    $$
    V(0,T) = V(0,t) + V(t,T) + 2\, \text{Cov}\!\left[\int_0^t r_s\, ds,\; \int_t^T r_s\, ds\right]
    $$

    (The cross-covariance does not vanish because $r_s$ for $s \leq t$ affects $r_u$ for $u > t$ through mean reversion.)

    **3. Short-rate variance limit:**

    $$
    \lim_{\tau \to 0} \frac{V(t,t+\tau)}{\tau^2} = \text{Var}[r_t] \cdot \frac{1}{\tau^2} \to 0, \qquad \lim_{\tau \to 0} \frac{V(t,t+\tau)}{\tau^3} = \frac{\sigma^2}{3}
    $$

    The $\tau^3$ scaling for small $\tau$ matches the Ho-Lee limit.

    **4. Duration identity:**

    $$
    \frac{\partial P(t,T)}{\partial r_t} = -B(\tau)\, P(t,T)
    $$

    so $B(\tau)$ is the "dollar duration per unit notional" divided by the bond price.

---

## Translation Between Conventions

Different references use different sign conventions. The two main variants:

| Convention | Bond price | $B$ function | Used by |
|:---|:---:|:---:|:---|
| **Positive $B$** | $P = e^{A - Br}$ | $B = (1-e^{-a\tau})/a > 0$ | Brigo-Mercurio, this text |
| **Negative $B$** | $P = e^{A + Br}$ | $B = -(1-e^{-a\tau})/a < 0$ | Some academic papers |

The relationship is simply $B_{\text{neg}} = -B_{\text{pos}}$ and $A$ is the same in both conventions. The positive convention is more natural because $B(\tau) > 0$ has the interpretation of a modified duration.

---

## Summary

The Hull-White named functions form a tightly connected system. The core relationships are: $B(\tau) = (1-e^{-a\tau})/a$ with $B'(\tau) = 1 - aB(\tau)$; $\alpha(t) = \psi(t)$ both satisfying $y' = \theta(t) - ay$; $\sigma_r^2(t) = \frac{\sigma^2}{2} B(2t)$; $V(t,T) = \frac{\sigma^2}{a^2}[\tau - 2B(\tau) + B(2\tau)/2]$; and the bond price $P(t,T) = \frac{P(0,T)}{P(0,t)} \exp(B(\tau)[f(0,t) - r_t] + \frac{\sigma^2}{4a} B(\tau)^2(1-e^{-2at}))$. These identities enable cross-checking of implementations and simplification of complex pricing formulas, and the translation table between sign conventions resolves the most common source of confusion in the literature.

---

## Exercises

**Exercise 1.** Starting from $\alpha(t) = f(0,t) + \frac{\sigma^2}{2a^2}(1-e^{-at})^2$, verify that $\alpha'(t) = \theta(t) - a\alpha(t)$ by computing $\alpha'(t)$ directly and substituting the formula for $\theta(t)$. Show all algebraic steps.

??? success "Solution to Exercise 1"
    Compute $\alpha'(t)$ directly from $\alpha(t) = f(0,t) + \frac{\sigma^2}{2a^2}(1-e^{-at})^2$:

    $$
    \alpha'(t) = f'(0,t) + \frac{\sigma^2}{2a^2}\cdot 2(1-e^{-at})\cdot ae^{-at} = f'(0,t) + \frac{\sigma^2}{a}e^{-at}(1-e^{-at})
    $$

    Now compute $\theta(t) - a\alpha(t)$ using $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$:

    $$
    \theta(t) - a\alpha(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at}) - af(0,t) - \frac{\sigma^2}{2a}(1-e^{-at})^2
    $$

    $$
    = f'(0,t) + \frac{\sigma^2}{2a}\left[(1-e^{-2at}) - (1-e^{-at})^2\right]
    $$

    Expand the bracket:

    $$
    (1-e^{-2at}) - (1-e^{-at})^2 = 1 - e^{-2at} - 1 + 2e^{-at} - e^{-2at} = 2e^{-at} - 2e^{-2at} = 2e^{-at}(1-e^{-at})
    $$

    Therefore:

    $$
    \theta(t) - a\alpha(t) = f'(0,t) + \frac{\sigma^2}{2a}\cdot 2e^{-at}(1-e^{-at}) = f'(0,t) + \frac{\sigma^2}{a}e^{-at}(1-e^{-at}) = \alpha'(t)
    $$

    This confirms $\alpha'(t) = \theta(t) - a\alpha(t)$.

---

**Exercise 2.** Prove the identity $\sigma_r^2(t) = \frac{\sigma^2}{2}B(2t)$ by substituting the definition of $B$. Then use the doubling formula $B(2\tau) = B(\tau)(2 - aB(\tau))$ to express $\sigma_r^2(t)$ in terms of $B(t)$ alone.

??? success "Solution to Exercise 2"
    **First part:** Substitute $B(2t) = (1-e^{-2at})/a$ into $\sigma_r^2(t) = \frac{\sigma^2}{2}B(2t)$:

    $$
    \sigma_r^2(t) = \frac{\sigma^2}{2}\cdot\frac{1-e^{-2at}}{a} = \frac{\sigma^2}{2a}(1-e^{-2at})
    $$

    This matches the definition.

    **Second part:** Use the doubling formula $B(2\tau) = B(\tau)(2 - aB(\tau))$. Setting $\tau = t$:

    $$
    B(2t) = B(t)(2 - aB(t))
    $$

    Therefore:

    $$
    \sigma_r^2(t) = \frac{\sigma^2}{2}B(2t) = \frac{\sigma^2}{2}B(t)(2 - aB(t)) = \sigma^2 B(t) - \frac{a\sigma^2}{2}B(t)^2
    $$

    This expresses the short rate variance purely in terms of $B(t)$, without any exponentials.

---

**Exercise 3.** The duration identity states $\frac{\partial P(t,T)}{\partial r_t} = -B(\tau)P(t,T)$. Derive this from $P(t,T) = e^{A(t,T) - B(\tau)r_t}$. Explain why $B(\tau)$ is called a "duration-like" function and how it differs from Macaulay duration.

??? success "Solution to Exercise 3"
    From $P(t,T) = e^{A(t,T) - B(\tau)r_t}$ (positive-$B$ convention), differentiate with respect to $r_t$:

    $$
    \frac{\partial P(t,T)}{\partial r_t} = -B(\tau)\, e^{A(t,T) - B(\tau)r_t} = -B(\tau)\, P(t,T)
    $$

    This is the duration identity.

    **Why $B(\tau)$ is called "duration-like":** The modified duration $D$ of a bond is defined by $\frac{\partial P}{\partial y} = -D\cdot P$, where $y$ is the yield. In the Hull-White model, $B(\tau)$ plays the analogous role with $r_t$ replacing $y$. For small $\tau$, $B(\tau) \approx \tau$, which matches the Macaulay duration of a zero-coupon bond.

    **How it differs from Macaulay duration:** Macaulay duration is always equal to $\tau$ for a zero-coupon bond, regardless of the interest rate model. In contrast, $B(\tau) = (1-e^{-a\tau})/a < \tau$ for $a > 0$, reflecting the mean-reverting nature of the Hull-White model. Mean reversion dampens the long-run impact of rate changes, so the effective duration saturates at $1/a$ rather than growing linearly with maturity. Only in the $a \to 0$ limit does $B(\tau) \to \tau$, recovering Macaulay duration.

---

**Exercise 4.** Verify the consistency check $A(0,T) - B(T)r_0 = \ln P(0,T)$ numerically for $a = 0.05$, $\sigma = 0.01$, $r_0 = 0.03$, and a flat market curve $P^M(0,T) = e^{-0.03T}$ at $T = 1, 5, 10$.

??? success "Solution to Exercise 4"
    With $a = 0.05$, $\sigma = 0.01$, $r_0 = 0.03$, and a flat market curve $P^M(0,T) = e^{-0.03T}$, we have $f(0,t) = 0.03$ for all $t$.

    The consistency check requires $A(0,T) - B(T)r_0 = \ln P(0,T) = -0.03T$.

    Compute $A(0,T)$ from the formula:

    $$
    A(0,T) = \ln\frac{P^M(0,T)}{P^M(0,0)} + B(T)f(0,0) + \frac{\sigma^2}{4a}B(T)^2(1-e^{0})
    $$

    Since $P^M(0,0) = 1$, $f(0,0) = 0.03$, and $1 - e^0 = 0$:

    $$
    A(0,T) = -0.03T + B(T)\cdot 0.03 + 0 = -0.03T + 0.03\, B(T)
    $$

    Then:

    $$
    A(0,T) - B(T)r_0 = -0.03T + 0.03\, B(T) - 0.03\, B(T) = -0.03T = \ln P^M(0,T) \quad \checkmark
    $$

    This holds for all $T$, not just specific values. Let us verify numerically at each $T$:

    **$T = 1$:** $B(1) = (1-e^{-0.05})/0.05 = 0.97531$. $A(0,1) = -0.03 + 0.03(0.97531) = -0.03 + 0.02926 = -0.00074$. Check: $A(0,1) - B(1)\cdot 0.03 = -0.00074 - 0.02926 = -0.03 = \ln P^M(0,1)$. $\checkmark$

    **$T = 5$:** $B(5) = (1-e^{-0.25})/0.05 = 4.42400$. $A(0,5) = -0.15 + 0.03(4.42400) = -0.15 + 0.13272 = -0.01728$. Check: $-0.01728 - 4.42400(0.03) = -0.01728 - 0.13272 = -0.15$. $\checkmark$

    **$T = 10$:** $B(10) = (1-e^{-0.5})/0.05 = 7.86939$. $A(0,10) = -0.30 + 0.03(7.86939) = -0.30 + 0.23608 = -0.06392$. Check: $-0.06392 - 7.86939(0.03) = -0.06392 - 0.23608 = -0.30$. $\checkmark$

---

**Exercise 5.** The variance decomposition identity involves a cross-covariance term between $\int_0^t r_s\,ds$ and $\int_t^T r_s\,ds$. Explain why this cross-covariance is nonzero in the Hull-White model. Compute it explicitly using the covariance function $\text{Cov}(r_s, r_u) = \frac{\sigma^2}{2a}e^{-a|u-s|}(1-e^{-2a\min(s,u)})$.

??? success "Solution to Exercise 5"
    In the Hull-White model, $r_t$ is an Ornstein-Uhlenbeck process: $r_u = r_t e^{-a(u-t)} + \text{deterministic} + \sigma\int_t^u e^{-a(u-s)}dW_s$ for $u > t$. Therefore $r_u$ depends on $r_s$ for $s \leq t$ through the dependence on $r_t$, and $r_t$ in turn depends on $\{r_s\}_{s \leq t}$ through the SDE dynamics.

    The cross-covariance is nonzero because, for $s \leq t < u$:

    $$
    \text{Cov}(r_s, r_u) = \text{Cov}(r_s, r_t e^{-a(u-t)} + \cdots) = e^{-a(u-t)}\text{Cov}(r_s, r_t)
    $$

    Since $r_t$ carries information about $r_s$ through the mean-reversion dynamics, $\text{Cov}(r_s, r_t) > 0$, and this nonzero covariance propagates to future times. Specifically:

    $$
    \text{Cov}(r_s, r_u) = \frac{\sigma^2}{2a}e^{-a(u-s)}(1-e^{-2a\min(s,u)}) = \frac{\sigma^2}{2a}e^{-a(u-s)}(1-e^{-2as})
    $$

    for $s \leq u$.

    The cross-covariance between the integrals is:

    $$
    \text{Cov}\!\left[\int_0^t r_s\,ds,\, \int_t^T r_u\,du\right] = \int_0^t\int_t^T \text{Cov}(r_s, r_u)\,du\,ds
    $$

    $$
    = \int_0^t\int_t^T \frac{\sigma^2}{2a}e^{-a(u-s)}(1-e^{-2as})\,du\,ds
    $$

    Evaluating the inner integral:

    $$
    \int_t^T e^{-a(u-s)}\,du = e^{as}\cdot\frac{e^{-at} - e^{-aT}}{a} = \frac{e^{-a(t-s)} - e^{-a(T-s)}}{a}
    $$

    Then the outer integral becomes:

    $$
    \frac{\sigma^2}{2a^2}\int_0^t \left[e^{-a(t-s)} - e^{-a(T-s)}\right](1-e^{-2as})\,ds
    $$

    This integral is nonzero and can be evaluated by expanding the product and integrating each exponential term, confirming that the variance decomposition includes a genuine cross-covariance contribution from the mean-reverting dynamics.

---

**Exercise 6.** A reference uses the negative-$B$ convention $P = e^{A + Br}$ with $B = -(1-e^{-a\tau})/a < 0$. Translate the bond price formula, the duration identity, and the yield formula from this section into the negative-$B$ convention. Verify that all pricing results are numerically identical.

??? success "Solution to Exercise 6"
    In the negative-$B$ convention, $B_{\text{neg}} = -B_{\text{pos}} = -(1-e^{-a\tau})/a < 0$ and $P = e^{A + B_{\text{neg}}\, r}$.

    **Bond price formula:** Starting from $P(t,T) = \frac{P(0,T)}{P(0,t)}\exp\left(B_{\text{pos}}(\tau)[f(0,t)-r_t] + \frac{\sigma^2}{4a}B_{\text{pos}}(\tau)^2(1-e^{-2at})\right)$ and noting $B_{\text{pos}} = -B_{\text{neg}}$:

    $$
    P(t,T) = \frac{P(0,T)}{P(0,t)}\exp\!\left(-B_{\text{neg}}(\tau)[f(0,t)-r_t] + \frac{\sigma^2}{4a}B_{\text{neg}}(\tau)^2(1-e^{-2at})\right)
    $$

    $$
    = \frac{P(0,T)}{P(0,t)}\exp\!\left(B_{\text{neg}}(\tau)[r_t - f(0,t)] + \frac{\sigma^2}{4a}B_{\text{neg}}(\tau)^2(1-e^{-2at})\right)
    $$

    (Note $B_{\text{neg}}^2 = B_{\text{pos}}^2$, so the convexity term is unchanged.)

    **Duration identity:** From $P = e^{A + B_{\text{neg}} r}$:

    $$
    \frac{\partial P}{\partial r_t} = B_{\text{neg}}\, P(t,T)
    $$

    Since $B_{\text{neg}} < 0$, this correctly gives $\partial P/\partial r < 0$ (bond prices fall when rates rise).

    **Yield formula:** $y(t,T) = -\frac{\ln P}{\tau} = -\frac{A + B_{\text{neg}} r}{\tau} = -\frac{A}{\tau} - \frac{B_{\text{neg}}}{\tau}r = -\frac{A}{\tau} + \frac{B_{\text{pos}}}{\tau}r$, which is identical to the positive convention result.

    All pricing results are numerically identical because $e^{A - B_{\text{pos}}r} = e^{A + B_{\text{neg}}r}$ by definition of $B_{\text{neg}} = -B_{\text{pos}}$.

---

**Exercise 7.** Using the relationship $B'(\tau) = 1 - aB(\tau)$, show that $\int_0^\tau B(s)\,ds = \frac{\tau - B(\tau)}{a}$. Then use this result to simplify the $A$-function quadrature $\int_t^T \theta(u)B(u,T)\,du$ when $\theta$ is constant.

??? success "Solution to Exercise 7"
    **First part: proving $\int_0^\tau B(s)\,ds = \frac{\tau - B(\tau)}{a}$.**

    From $B'(\tau) = 1 - aB(\tau)$, we can write $aB(\tau) = 1 - B'(\tau)$, so:

    $$
    a\int_0^\tau B(s)\,ds = \int_0^\tau [1 - B'(s)]\,ds = \tau - [B(s)]_0^\tau = \tau - B(\tau) + B(0) = \tau - B(\tau)
    $$

    since $B(0) = 0$. Dividing by $a$:

    $$
    \int_0^\tau B(s)\,ds = \frac{\tau - B(\tau)}{a}
    $$

    **Second part: simplifying the quadrature when $\theta$ is constant.**

    When $\theta$ is constant (Vasicek model), the $A$-function quadrature involves:

    $$
    \int_t^T \theta\, B(u,T)\,du = \theta\int_t^T B(T-u)\,du
    $$

    Substituting $s = T - u$ (so $du = -ds$), with limits $s=0$ to $s=T-t=\tau$:

    $$
    = \theta\int_0^\tau B(s)\,ds = \theta\cdot\frac{\tau - B(\tau)}{a}
    $$

    Therefore the complete $A$-function in the Vasicek case becomes:

    $$
    A(t,T) = \frac{\theta}{a}[\tau - B(\tau)] + \frac{1}{2}\sigma^2\int_t^T B(u,T)^2\,du
    $$

    Using the closed-form integral of $B^2$:

    $$
    A(t,T) = \frac{\theta}{a}[\tau - B(\tau)] + \frac{\sigma^2}{2a^2}\left[\tau - 2B(\tau) + \frac{B(2\tau)}{2}\right]
    $$

    This clean expression avoids any numerical integration and is the standard Vasicek bond price formula.
