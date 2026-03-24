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

---

**Exercise 2.** Prove the identity $\sigma_r^2(t) = \frac{\sigma^2}{2}B(2t)$ by substituting the definition of $B$. Then use the doubling formula $B(2\tau) = B(\tau)(2 - aB(\tau))$ to express $\sigma_r^2(t)$ in terms of $B(t)$ alone.

---

**Exercise 3.** The duration identity states $\frac{\partial P(t,T)}{\partial r_t} = -B(\tau)P(t,T)$. Derive this from $P(t,T) = e^{A(t,T) - B(\tau)r_t}$. Explain why $B(\tau)$ is called a "duration-like" function and how it differs from Macaulay duration.

---

**Exercise 4.** Verify the consistency check $A(0,T) - B(T)r_0 = \ln P(0,T)$ numerically for $a = 0.05$, $\sigma = 0.01$, $r_0 = 0.03$, and a flat market curve $P^M(0,T) = e^{-0.03T}$ at $T = 1, 5, 10$.

---

**Exercise 5.** The variance decomposition identity involves a cross-covariance term between $\int_0^t r_s\,ds$ and $\int_t^T r_s\,ds$. Explain why this cross-covariance is nonzero in the Hull-White model. Compute it explicitly using the covariance function $\text{Cov}(r_s, r_u) = \frac{\sigma^2}{2a}e^{-a|u-s|}(1-e^{-2a\min(s,u)})$.

---

**Exercise 6.** A reference uses the negative-$B$ convention $P = e^{A + Br}$ with $B = -(1-e^{-a\tau})/a < 0$. Translate the bond price formula, the duration identity, and the yield formula from this section into the negative-$B$ convention. Verify that all pricing results are numerically identical.

---

**Exercise 7.** Using the relationship $B'(\tau) = 1 - aB(\tau)$, show that $\int_0^\tau B(s)\,ds = \frac{\tau - B(\tau)}{a}$. Then use this result to simplify the $A$-function quadrature $\int_t^T \theta(u)B(u,T)\,du$ when $\theta$ is constant.
