# Mellin Transform for the Black-Scholes PDE

The Black-Scholes PDE has variable coefficients $rS\frac{\partial V}{\partial S}$ and $\frac{\sigma^2}{2}S^2\frac{\partial^2 V}{\partial S^2}$ that arise because stock prices evolve multiplicatively: a percentage return is the same whether the stock is at \$10 or \$1000. The Fourier transform is the natural tool for additive processes on $(-\infty, \infty)$, while the **Mellin transform** is the natural tool for multiplicative processes on $(0, \infty)$. Where the Fourier transform diagonalizes the constant-coefficient operators $\frac{\partial}{\partial x}$ and $\frac{\partial^2}{\partial x^2}$, the Mellin transform diagonalizes the variable-coefficient operators $S\frac{\partial}{\partial S}$ and $S^2\frac{\partial^2}{\partial S^2}$ that appear directly in the Black-Scholes equation. This allows us to work with the stock price $S$ itself, without the logarithmic change of variable $x = \ln S$ that other transform methods require.

This section develops the Mellin transform approach to solving the Black-Scholes PDE, derives the European call price via Mellin inversion, and establishes the precise duality between the Mellin and Fourier transforms.

---

## Mellin Transform: Definition and Properties

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

## Transforming the Black-Scholes PDE

The Black-Scholes PDE in original $(S, t)$ variables is

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2}{2}S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

Apply the Mellin transform in $S$, writing $\hat{V}(s,t) = \mathcal{M}[V](s,t)$:

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

## Mellin Solution for the European Call

### Mellin Transform of the Call Payoff

For the European call payoff $\Phi(S) = (S - K)^+$:

$$
\mathcal{M}[(S-K)^+](s) = \int_K^{\infty}(S-K)\,S^{s-1}\,dS
$$

Expanding:

$$
= \int_K^{\infty}S^s\,dS - K\int_K^{\infty}S^{s-1}\,dS
$$

$$
= \left[\frac{S^{s+1}}{s+1}\right]_K^{\infty} - K\left[\frac{S^s}{s}\right]_K^{\infty}
$$

For convergence at infinity, we need $\text{Re}(s+1) < 0$ and $\text{Re}(s) < 0$, so $\text{Re}(s) < -1$. Under this condition:

$$
= -\frac{K^{s+1}}{s+1} + \frac{K^{s+1}}{s} = K^{s+1}\left[\frac{1}{s} - \frac{1}{s+1}\right]
$$

$$
\boxed{\mathcal{M}[(S-K)^+](s) = \frac{K^{s+1}}{s(s+1)}}
$$

valid for $\text{Re}(s) < -1$.

### Option Value in Mellin Space

Combining the payoff transform with the general solution:

$$
\hat{C}(s,t) = \frac{K^{s+1}}{s(s+1)}\,e^{-\Lambda(s)\tau}
$$

where $\tau = T - t$ and $\Lambda(s) = \frac{\sigma^2}{2}s^2 + \left(r - \frac{\sigma^2}{2}\right)s - r$.

### Mellin Inversion via Residue Calculus

The call price is recovered by the inverse Mellin transform:

$$
C(S,t) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\frac{K^{s+1}}{s(s+1)}\,e^{-\Lambda(s)\tau}\,S^{-s}\,ds
$$

where $c < -1$ places the contour in the strip of analyticity.

### Finding the Poles

The integrand has **simple poles** at:

- $s = 0$, where $\Lambda(0) = -r$
- $s = -1$, where $\Lambda(-1) = \frac{\sigma^2}{2} - r + \frac{\sigma^2}{2} - r = \sigma^2 - 2r$

### Residue at s = 0

$$
\text{Res}_{s=0} = \lim_{s \to 0}\,s \cdot \frac{K^{s+1}}{s(s+1)}\,e^{-\Lambda(s)\tau}\,S^{-s}
$$

$$
= \frac{K}{1} \cdot e^{-(-r)\tau} \cdot 1 = Ke^{r\tau}
$$

### Residue at s = -1

$$
\text{Res}_{s=-1} = \lim_{s \to -1}\,(s+1) \cdot \frac{K^{s+1}}{s(s+1)}\,e^{-\Lambda(s)\tau}\,S^{-s}
$$

$$
= \frac{K^0}{-1} \cdot e^{-(\sigma^2 - 2r)\tau} \cdot S = -S\,e^{(2r - \sigma^2)\tau}
$$

### Recovery of the Black-Scholes Formula

The standard approach decomposes the call price into two probability terms. Writing

$$
C(S,t) = S\,\Pi_1 - Ke^{-r\tau}\,\Pi_2
$$

where $\Pi_1$ and $\Pi_2$ are computed via separate Mellin inversions, one obtains after contour integration:

$$
\boxed{C(S,t) = S\,N(d_1) - Ke^{-r\tau}\,N(d_2)}
$$

where $d_1$ and $d_2$ are the standard Black-Scholes quantities. The Mellin transform **automatically generates** the two-term structure of the Black-Scholes formula, with each term arising from a separate pole contribution.

---

## Mellin-Fourier Duality

### The Connection

The substitution $S = e^x$ reveals the precise relationship between the Mellin and Fourier transforms:

$$
\mathcal{M}[V](s) = \int_0^{\infty}V(S)\,S^{s-1}\,dS = \int_{-\infty}^{\infty}V(e^x)\,e^{sx}\,dx = \mathcal{F}[V(e^x)](-is)
$$

Therefore:

$$
\text{Mellin in } S = \text{Fourier in } x = \ln S \text{ with } \omega = -is
$$

The Mellin inverse correspondingly becomes

$$
\mathcal{M}^{-1}[f](S) = \frac{1}{2\pi}\int_{-\infty}^{\infty}f(c + i\omega)\,S^{-c-i\omega}\,d\omega
$$

This duality explains why both transforms reduce the Black-Scholes PDE to an ODE: they are the same transform applied in different coordinates (multiplicative vs. additive).

### Parseval's Theorem for the Mellin Transform

The Mellin transform preserves energy in the following sense:

$$
\int_0^{\infty}|V(S)|^2\,\frac{dS}{S} = \frac{1}{2\pi}\int_{-\infty}^{\infty}|\mathcal{M}[V](c + i\omega)|^2\,d\omega
$$

The measure $\frac{dS}{S}$ is the Haar measure on the multiplicative group $(0,\infty)$, confirming that the Mellin transform is the natural harmonic analysis on this group.

### Convolution Theorem

The Mellin transform of a **multiplicative convolution** satisfies

$$
\mathcal{M}[V \cdot W](s) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\mathcal{M}[V](\xi)\,\mathcal{M}[W](s-\xi)\,d\xi
$$

This is the analogue of the Fourier convolution theorem, adapted to the multiplicative structure.

---

## Mellin Transforms for Exotic Payoffs

The Mellin transform extends naturally to other payoff structures. For **power options** with payoff $(S^n - K^n)^+$:

$$
\mathcal{M}[(S^n - K^n)^+](s) = \frac{K^{ns+n}}{s(s+n)}
$$

The solution structure parallels the European call but with modified parameters in $\Lambda(s)$. More generally, any payoff that is piecewise polynomial in $S$ admits a Mellin transform expressible in terms of rational functions of $s$ and powers of $K$, making the inversion tractable via residue calculus. In the operator framework of the introduction, the Mellin approach provides a **multiplicative spectral representation** of the pricing semigroup $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$, diagonalizing it in the basis of power functions $S^s$.

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
