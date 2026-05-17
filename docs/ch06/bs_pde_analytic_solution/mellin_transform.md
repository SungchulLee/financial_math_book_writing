# Mellin Transform for the Black-Scholes PDE

Everything in this subsection follows from one sentence:

> **The Mellin transform in $x$ is the Fourier transform in $\log x$.**

The Mellin transform follows from one simple calculation:

$$
S \frac{d}{dS}\, S^s = s \cdot S^s
$$

**Power laws are eigenfunctions of the scaling operator $S\, \partial_S$** — the multiplicative analogue of plane waves $e^{i\omega x}$ being eigenfunctions of $\partial_x$. The Mellin transform decomposes any function on $(0, \infty)$ into these power-law modes, and in those coordinates the variable-coefficient Black–Scholes operator collapses to a quadratic polynomial in the Mellin variable $s$.

We build the picture in the same order a reader naturally builds intuition: the toy eigenfunction calculation first, then the transform definition, and only then the Black–Scholes PDE in Mellin space.

---

## 1. Why Mellin? A Toy Mechanism

Before any finance, work the eigenvalue calculation. Consider the **scaling operator**

$$
D := S \frac{d}{dS}
$$

acting on functions of $S \in (0, \infty)$. Apply $D$ to a power-law $S^s$ with $s \in \mathbb{C}$:

$$
D \cdot S^s = S \cdot s\, S^{s-1} = s \cdot S^s
$$

Iterating,

$$
D^n \cdot S^s = s^n \cdot S^s, \qquad S^2 \frac{d^2}{dS^2}\, S^s = D(D - 1)\, S^s = s(s - 1)\, S^s
$$

These two identities are the Mellin analogue of the Fourier eigenfunction relation $\partial_x\, e^{i\omega x} = i\omega \cdot e^{i\omega x}$ — they are the entire mechanism that makes the rest of the subsection work.

### 1.1 Why Mellin and Not Fourier?

The Fourier transform decomposes $f(x)$ into plane waves $e^{i\omega x}$ — the eigenfunctions of *translation*, $x \mapsto x + a$. Each plane wave is invariant (up to a phase) under shifting by $a$.

The Mellin transform decomposes $V(S)$ into power-laws $S^{-s}$ — the eigenfunctions of *dilation*, $S \mapsto \lambda S$. Each power-law $S^{-s}$ is invariant (up to a scaling factor $\lambda^{-s}$) under multiplication by $\lambda$.

Stock prices evolve **multiplicatively**: a $5\%$ return is the same whether $S = \$10$ or $\$1000$. The natural symmetry group of the Black–Scholes problem is therefore the multiplicative group $(0, \infty)$, not the additive group $\mathbb{R}$ — and Mellin is built for exactly that group.

### 1.2 Diagonalization Picture

A constant-coefficient operator in $x$ — say $-\partial_x^2 + \mu^2$ — commutes with translations and is diagonalized by Fourier. The Black–Scholes spatial operator

$$
\mathcal{L}_S = \frac{\sigma^2}{2} S^2 \frac{d^2}{dS^2} + r S \frac{d}{dS} - r
$$

is **not** constant-coefficient in $S$ (the coefficients $S^2$ and $S$ depend explicitly on $S$), so Fourier in $S$ would not diagonalize it directly. But written in terms of the scaling operator $D = S\, \partial_S$,

$$
\mathcal{L}_S = \frac{\sigma^2}{2}\, D(D - 1) + r D - r
$$

— a **polynomial in $D$ alone** — and every $D$-polynomial is diagonalized by power-law modes. Hence Mellin in $S$ diagonalizes the BS operator without first changing variables to $x = \ln S$.

In Mellin coordinates, the action on power-law modes becomes a *scalar* multiplication:

$$
\mathcal{L}_S\, S^{-s} = \Lambda(s)\, S^{-s}, \qquad \Lambda(s) = \frac{\sigma^2}{2}\, s(s - 1) - r s - r
$$

(reading off from $D \cdot S^{-s} = -s \cdot S^{-s}$). The eigenvalue $\Lambda(s)$ is the **Mellin symbol** of the BS operator — analogous to the Fourier characteristic exponent $\psi(\omega)$.

!!! tip "Core principle"
    The Mellin transform decomposes functions on $(0, \infty)$ into power-law modes $S^{-s}$, which are joint eigenfunctions of the **scaling operator** $D = S\, \partial_S$ and of every operator that is a polynomial in $D$. For the Black–Scholes generator, this turns the second-order spatial operator into a quadratic polynomial $\Lambda(s)$ in the Mellin variable.

This is the mechanism. Black–Scholes is the application.

### 1.3 Mellin = Fourier in Disguise

The change of variable $x = \ln S$ converts the Mellin integral into a Fourier-type integral:

$$
\mathcal{M}[V](s) = \int_0^\infty V(S)\, S^{s - 1}\, dS \underset{x = \ln S}{=} \int_{-\infty}^\infty V(e^x)\, e^{s x}\, dx
$$

— the Mellin transform of $V(S)$ at the point $s$ is the two-sided Laplace / generalized Fourier transform of the function $x \mapsto V(e^x)$. So Mellin in $S$ and Fourier in $x = \ln S$ are *the same transform written in different coordinates*; the toy eigenfunction identity $D\, S^s = s\, S^s$ is the spatial-side translation of $\partial_x\, e^{s x} = s\, e^{s x}$. The reason we keep Mellin as a separate development is that the multiplicative variable $S$ is the financially natural one: power-law modes $S^{-s}$ are gearing/moneyness exponents that map directly onto market language, whereas $e^{i\omega x}$ does not.

This subsection is therefore best read as an *alternative perspective* on the Black-Scholes formula rather than a self-contained derivation: the cleanest contour analysis still proceeds through the Fourier picture of [§ Fourier Transform](fourier_transform.md). What the Mellin viewpoint adds is the multiplicative-symmetry interpretation and a clean operator-algebra story tied directly to financial coordinates.

---

## 2. Mellin Transform: Definition and Properties

### Definition

The Mellin transform of a function $V(S)$ defined on $(0, \infty)$ is

$$
\boxed{\mathcal{M}[V](s) = \int_0^{\infty} V(S)\,S^{s-1}\,dS}
$$

where $s \in \mathbb{C}$ lies in the **strip of analyticity** $c_1 < \text{Re}(s) < c_2$ determined by the growth of $V$ near $S = 0$ and $S = \infty$.

The **inverse Mellin transform** recovers $V$ via a Bromwich-type contour integral:

$$
\boxed{V(S) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\mathcal{M}[V](s)\,S^{-s}\,ds}
$$

where the real number $c$ is chosen so the vertical contour $\text{Re}(s) = c$ lies within the strip of analyticity.

### Transform Properties for Black-Scholes Operators

The key properties that make the Mellin transform effective for the Black-Scholes PDE are:

$$
\mathcal{M}\left[S\frac{\partial V}{\partial S}\right](s) = s\,\mathcal{M}[V](s)
$$

$$
\mathcal{M}\left[S^2\frac{\partial^2 V}{\partial S^2}\right](s) = s(s-1)\,\mathcal{M}[V](s)
$$

Both results follow from integration by parts, assuming that boundary terms at $S = 0$ and $S = \infty$ vanish. The essential point is that the Mellin transform converts the variable-coefficient differential operators $S\frac{d}{dS}$ and $S^2\frac{d^2}{dS^2}$ into **polynomial multipliers** in the transform variable $s$.

---

## 3. Transforming the Black-Scholes PDE

!!! note "Recall"
    The Black-Scholes PDE and its terminal/boundary conditions are stated in [§ Introduction](intro.md); the heat-equation form and risk-neutral framing are developed in [§ Heat Equation](heat_equation.md) and [§ Feynman–Kac](feynman_kac.md).

Apply the Mellin transform in $S$ directly to the BS PDE in $(S, t)$ variables, writing $\hat{V}(s,t) = \mathcal{M}[V](s,t)$:

$$
\frac{\partial \hat{V}}{\partial t} + rs\,\hat{V} + \frac{\sigma^2}{2}s(s-1)\,\hat{V} - r\,\hat{V} = 0
$$

Collecting terms:

$$
\boxed{\frac{\partial \hat{V}}{\partial t} + \Lambda(s)\,\hat{V} = 0}
$$

where the **Mellin symbol** of the Black-Scholes operator is

$$
\boxed{\Lambda(s) = \frac{\sigma^2}{2}s^2 + \left(r - \frac{\sigma^2}{2}\right)s - r}
$$

This is a **first-order ODE in $t$** with $s$ appearing only as a parameter. The entire spatial structure of the PDE has been absorbed into the algebraic function $\Lambda(s)$.

### General Solution

The ODE has the immediate solution

$$
\boxed{\hat{V}(s,t) = \hat{V}(s,T)\,e^{-\Lambda(s)(T-t)}}
$$

With the terminal condition $V(S,T) = \Phi(S)$, we have $\hat{V}(s,T) = \mathcal{M}[\Phi](s)$, so the complete solution in Mellin space is

$$
\boxed{V(S,t) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\mathcal{M}[\Phi](s)\,e^{-\Lambda(s)(T-t)}\,S^{-s}\,ds}
$$

---

## 4. Mellin Solution for the European Call

### Mellin Transform of the Call Payoff

For the European call payoff $\Phi(S) = (S - K)^+$, a direct calculation gives

$$
\mathcal{M}[(S-K)^+](s) = \int_K^{\infty}(S-K)\,S^{s-1}\,dS = \frac{K^{s+1}}{s(s+1)}
$$

The integral converges at $S = \infty$ only when $\text{Re}(s) < -1$, so this identity is meaningful on the half-plane $\text{Re}(s) < -1$.

??? note "Analytic strip"
    The Mellin transform of an integrable function is, in general, holomorphic on a vertical strip $c_1 < \text{Re}(s) < c_2$ — its **fundamental strip** — determined by the decay of the function at $0$ and at $\infty$. For the call payoff $(S - K)^+$, the function vanishes for $S < K$ (so there is no constraint at $S = 0$) but grows linearly at infinity, forcing $\text{Re}(s) < -1$. Strictly speaking the "strip" here is the half-plane $\text{Re}(s) < -1$.

    The inverse Mellin contour $\text{Re}(s) = c$ **must lie inside this strip** for the inversion integral to represent the original function. Recovering the option price by deforming the contour to the right (toward $\text{Re}(s) = 0$) crosses the poles at $s = -1$ and $s = 0$, which lie *outside* the fundamental strip. The standard residue calculation below treats this contour deformation **formally**: full justification requires bounding the integrand on closing arcs and checking that no other singularities (e.g. from $e^{-\Lambda(s)\tau}$, which is entire, or growth of $S^{-s}$) obstruct the deformation. We do not attempt that here.

### Option Value in Mellin Space

Combining the payoff transform with the general solution gives

$$
\hat{C}(s,t) = \frac{K^{s+1}}{s(s+1)}\,e^{-\Lambda(s)\tau}, \qquad \tau = T-t
$$

and the call price is recovered by

$$
C(S,t) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\frac{K^{s+1}}{s(s+1)}\,e^{-\Lambda(s)\tau}\,S^{-s}\,ds, \qquad c < -1
$$

The integrand has **simple poles** at $s = 0$ and $s = -1$, where $\Lambda(0) = -r$ and $\Lambda(-1) = \sigma^2 - 2r$. From [§ Heat Equation](heat_equation.md), the BS call has the form $C = S N(d_1) - Ke^{-r\tau} N(d_2)$ with $d_{1,2}$ as defined there; the Mellin inversion **naturally produces this two-term structure** because the two poles correspond (heuristically) to the two terms. The pole *positions* are visible from $\frac{1}{s(s+1)}$, but the $N(d_1)$ and $N(d_2)$ factors come from the imaginary-axis integral that survives the residue computation, not from the residues themselves.

??? note "Advanced Remark: Mellin residue calculation"
    Treating the contour deformation **formally**, the residues are

    $$
    \text{Res}_{s=0}\bigl[\hat{C}(s,t)\,S^{-s}\bigr] = K\,e^{r\tau}, \qquad \text{Res}_{s=-1}\bigl[\hat{C}(s,t)\,S^{-s}\bigr] = -S\,e^{(2r - \sigma^2)\tau}
    $$

    A naive "sum of residues" gives the wrong answer: the BS call formula (see [§ Heat Equation](heat_equation.md)) arises only after one keeps the contour integral and identifies the surviving Gaussian integrals along $\text{Re}(s) = c$ as the normal CDFs. Recovering those CDF factors is the same Gaussian completion-of-square computation carried out in [§ Feynman–Kac](feynman_kac.md) and [§ Fourier Transform](fourier_transform.md). A fully rigorous treatment requires verifying decay of the integrand along closing arcs, checking that the deformed contour encloses no other singularities, and tracking convergence of the residual line integral.

---

## 5. Mellin-Fourier Duality

The substitution $S = e^x$ relates the two transforms directly:

$$
\mathcal{M}[V](s) = \int_{-\infty}^{\infty}V(e^x)\,e^{sx}\,dx = \mathcal{F}[V(e^x)](-is)
$$

So a Mellin transform in $S$ is a Fourier transform in $x = \ln S$ with $\omega = -is$. This is why both transforms reduce the Black-Scholes PDE to an ODE: they are the same harmonic analysis, written in multiplicative ($S$) versus additive ($\ln S$) coordinates. The $e^{i\omega x}$ machinery developed in [§ Fourier Transform](fourier_transform.md) transfers verbatim under $\omega \leftrightarrow -is$.

The Mellin Parseval identity takes the form

$$
\int_0^{\infty}|V(S)|^2\,\frac{dS}{S} = \frac{1}{2\pi}\int_{-\infty}^{\infty}|\mathcal{M}[V](c + i\omega)|^2\,d\omega
$$

The measure $\frac{dS}{S}$ is the Haar measure on the multiplicative group $(0, \infty)$ — the right invariant measure under $S \mapsto \lambda S$ — confirming that the Mellin transform is the natural harmonic analysis on this group, just as the Fourier transform is natural on the additive group $\mathbb{R}$.

---

## 6. Mellin Transforms for Exotic Payoffs

Any payoff that is piecewise polynomial in $S$ has a Mellin transform expressible as a rational function of $s$ times powers of $K$, so the inversion remains tractable. For instance, the **power option** payoff $(S^n - K^n)^+$ transforms (see Exercise 5) to $\frac{nK^{n+s}}{s(s+n)}$, valid for $\text{Re}(s) < -n$. Within the pricing-semigroup framing of [§ Introduction](intro.md), the Mellin approach is a **multiplicative spectral representation** that diagonalizes the semigroup on the basis of power functions $S^s$ — the multiplicative analogue of the Fourier exponentials $e^{i\omega x}$.

---

## Exercises

**Exercise 1.** Compute the Mellin transform of the European put payoff $(K - S)^+$ and determine its strip of analyticity. Compare with the call payoff transform and relate the two via put-call parity in transform space.

??? success "Solution to Exercise 1"
    The Mellin transform of the European put payoff $(K - S)^+$ is:

    $$
    \mathcal{M}[(K-S)^+](s) = \int_0^{K}(K-S)\,S^{s-1}\,dS
    $$

    $$
    = K\int_0^K S^{s-1}\,dS - \int_0^K S^s\,dS = K\left[\frac{S^s}{s}\right]_0^K - \left[\frac{S^{s+1}}{s+1}\right]_0^K
    $$

    The lower limits vanish when $\text{Re}(s) > 0$ (for the first integral) and $\text{Re}(s) > -1$ (for the second). So we need $\text{Re}(s) > 0$:

    $$
    = \frac{K^{s+1}}{s} - \frac{K^{s+1}}{s+1} = K^{s+1}\left(\frac{1}{s} - \frac{1}{s+1}\right) = \frac{K^{s+1}}{s(s+1)}
    $$

    The **strip of analyticity** is $\text{Re}(s) > 0$.

    **Comparison with the call.** The Mellin transform of the call payoff is also $\frac{K^{s+1}}{s(s+1)}$ but valid for $\text{Re}(s) < -1$. The two transforms have the **same functional form** on **different strips of analyticity** (put: $\text{Re}(s) > 0$; call: $\text{Re}(s) < -1$).

    **Put-call parity in transform space.** Since $(S-K)^+ - (K-S)^+ = S - K$, and $\mathcal{M}[S](s)$ and $\mathcal{M}[K](s)$ are defined on their own strips, the transform of $S - K$ relates the two payoff transforms via analytic continuation across the strip $-1 < \text{Re}(s) < 0$ that separates them.

---

**Exercise 2.** Verify that the Mellin transform converts the Black-Scholes operator $\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV$ into a polynomial in $s$ by computing each term separately via integration by parts.

??? success "Solution to Exercise 2"
    **First term:** $\mathcal{M}\left[S^2 V_{SS}\right](s)$. We use repeated integration by parts.

    Starting from $\mathcal{M}[SV_S](s) = \int_0^{\infty}SV_S \cdot S^{s-1}\,dS = \int_0^{\infty}S^s V_S\,dS$. Integrating by parts with boundary terms vanishing:

    $$
    = \left[S^s V\right]_0^{\infty} - s\int_0^{\infty}S^{s-1}V\,dS = -s\,\hat{V}(s)
    $$

    For the second-order term, using the identity $S^2 V_{SS} = \frac{d}{dS}(S^2 V_S) - 2SV_S$ and applying the Mellin transform, or equivalently using the standard result:

    $$
    \mathcal{M}\left[S^2 V_{SS}\right](s) = s(s-1)\,\hat{V}(s)
    $$

    Note: The sign convention depends on the definition used. With the convention in the text where $\mathcal{M}[SV_S] = s\hat{V}$ (absorbing the sign into the operator convention), the full Black-Scholes operator becomes:

    $$
    \frac{\sigma^2}{2}s(s-1) + rs - r = \frac{\sigma^2}{2}s^2 + \left(r - \frac{\sigma^2}{2}\right)s - r = \Lambda(s)
    $$

    This is a **quadratic polynomial in $s$**, confirming that the Mellin transform converts the variable-coefficient differential operator into an algebraic multiplier. $\square$

---

**Exercise 3.** The Mellin symbol $\Lambda(s) = \frac{\sigma^2}{2}s^2 + \left(r - \frac{\sigma^2}{2}\right)s - r$ has two real roots. Find them and interpret their financial meaning in terms of the growth rates of the homogeneous solutions $S^{-s}$ of the Black-Scholes equation.

??? success "Solution to Exercise 3"
    Setting $\Lambda(s) = 0$:

    $$
    \frac{\sigma^2}{2}s^2 + \left(r - \frac{\sigma^2}{2}\right)s - r = 0
    $$

    Using the quadratic formula:

    $$
    s = \frac{-\left(r - \frac{\sigma^2}{2}\right) \pm \sqrt{\left(r - \frac{\sigma^2}{2}\right)^2 + 2\sigma^2 r}}{\sigma^2}
    $$

    The discriminant simplifies:

    $$
    \left(r - \frac{\sigma^2}{2}\right)^2 + 2\sigma^2 r = r^2 - r\sigma^2 + \frac{\sigma^4}{4} + 2r\sigma^2 = r^2 + r\sigma^2 + \frac{\sigma^4}{4} = \left(r + \frac{\sigma^2}{2}\right)^2
    $$

    Therefore:

    $$
    s = \frac{-(r - \frac{\sigma^2}{2}) \pm (r + \frac{\sigma^2}{2})}{\sigma^2}
    $$

    The two roots are:

    - $s_+ = \frac{-(r - \frac{\sigma^2}{2}) + (r + \frac{\sigma^2}{2})}{\sigma^2} = \frac{\sigma^2}{\sigma^2} = 1$
    - $s_- = \frac{-(r - \frac{\sigma^2}{2}) - (r + \frac{\sigma^2}{2})}{\sigma^2} = \frac{-2r}{\sigma^2}$

    **Financial interpretation.** The roots of $\Lambda$ correspond to solutions of the **perpetual** (time-independent) Black-Scholes equation $\frac{\sigma^2}{2}S^2 V'' + rSV' - rV = 0$. The Euler-type ansatz $V = S^\lambda$ yields $\Lambda(-\lambda) = 0$, so the homogeneous solutions are $V = S^{-s_+} = S^{-1}$ and $V = S^{-s_-} = S^{2r/\sigma^2}$.

    However, one can equivalently parametrize by writing $\lambda = -s$, giving $\lambda_1 = -1$ (corresponding to $V = S^{-1}$, which is not financially meaningful by itself) and $\lambda_2 = 2r/\sigma^2$ (corresponding to $V = S^{2r/\sigma^2}$).

    More directly: the factorization $\Lambda(s) = \frac{\sigma^2}{2}(s - 1)(s + \frac{2r}{\sigma^2})$ shows that $s = 1$ and $s = -2r/\sigma^2$ are the roots. These are distinct from the poles $s = 0$ and $s = -1$ of the call payoff transform. The root $s_+ = 1$ corresponds to $V(S) = S$, the trivially growing solution (holding the stock). The root $s_- = -2r/\sigma^2$ corresponds to $V(S) = S^{2r/\sigma^2}$, which appears in the pricing of perpetual American options. $\square$

---

**Exercise 4.** Using the Mellin-Fourier duality $\mathcal{M}[V](s) = \mathcal{F}[V(e^x)](-is)$, show that the Mellin symbol $\Lambda(s)$ and the Fourier characteristic exponent $\psi(\omega) = -\frac{\sigma^2 \omega^2}{2} + i\omega(r - \frac{\sigma^2}{2}) - r$ are related by $\Lambda(s) = \psi(-is)$.

??? success "Solution to Exercise 4"
    The Fourier characteristic exponent for the log-price Black-Scholes PDE is:

    $$
    \psi(\omega) = -\frac{\sigma^2\omega^2}{2} + i\omega\left(r - \frac{\sigma^2}{2}\right) - r
    $$

    Substituting $\omega = -is$:

    $$
    \psi(-is) = -\frac{\sigma^2(-is)^2}{2} + i(-is)\left(r - \frac{\sigma^2}{2}\right) - r
    $$

    $$
    = -\frac{\sigma^2(-s^2)}{2} + s\left(r - \frac{\sigma^2}{2}\right) - r
    $$

    $$
    = \frac{\sigma^2 s^2}{2} + \left(r - \frac{\sigma^2}{2}\right)s - r = \Lambda(s)
    $$

    This confirms $\Lambda(s) = \psi(-is)$, which is a direct consequence of the Mellin-Fourier duality. The substitution $\omega = -is$ (equivalently $s = i\omega$) maps the Fourier frequency variable to the Mellin complex variable, and the two transforms produce the same ODE structure under this correspondence. $\square$

---

**Exercise 5.** Compute the Mellin transform of the power option payoff $(S^n - K^n)^+$ for general $n > 0$ and determine the strip of analyticity. Show that the case $n = 1$ recovers the standard call payoff transform.

??? success "Solution to Exercise 5"
    The Mellin transform is:

    $$
    \mathcal{M}[(S^n - K^n)^+](s) = \int_{K}^{\infty}(S^n - K^n)\,S^{s-1}\,dS
    $$

    $$
    = \int_K^{\infty}S^{n+s-1}\,dS - K^n\int_K^{\infty}S^{s-1}\,dS
    $$

    For convergence at infinity, we need $\text{Re}(n + s) < 0$ and $\text{Re}(s) < 0$, so $\text{Re}(s) < -n$. Under this condition:

    $$
    = -\frac{K^{n+s}}{n+s} - K^n\left(-\frac{K^s}{s}\right) = -\frac{K^{n+s}}{n+s} + \frac{K^{n+s}}{s}
    $$

    $$
    = K^{n+s}\left(\frac{1}{s} - \frac{1}{n+s}\right) = K^{n+s}\cdot\frac{n}{s(n+s)}
    $$

    Therefore:

    $$
    \mathcal{M}[(S^n - K^n)^+](s) = \frac{nK^{n+s}}{s(n+s)}
    $$

    valid for $\text{Re}(s) < -n$.

    **Verification for $n = 1$:**

    $$
    \frac{1 \cdot K^{1+s}}{s(1+s)} = \frac{K^{s+1}}{s(s+1)}
    $$

    This matches the call payoff transform $\frac{K^{s+1}}{s(s+1)}$ with strip $\text{Re}(s) < -1$. $\square$
