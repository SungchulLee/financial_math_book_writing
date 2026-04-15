# Applications and Examples of Itô Calculus

Once the main rules of stochastic calculus have been developed — Itô's lemma, the product rule, and integration by parts — we can use them to compute stochastic integrals, construct martingales, and solve stochastic differential equations (SDEs).

This section presents a collection of worked examples illustrating how these tools are applied in practice. For the theorem statements being applied throughout, see [Itô's Lemma](ito_lemma.md). For the multiplication rules used in SDE substitutions, see [Itô Rules](ito_rules.md).

---

## 1. Evaluating Stochastic Integrals

One of the most important uses of Itô's lemma is to evaluate stochastic integrals of the form

$$
\int_0^t g(s,B_s)\,dB_s
$$

The key idea is to **choose a function $f(t,x)$** whose derivative with respect to $x$ matches the integrand.

### General Strategy

Choose $f(t,x)$ such that $\frac{\partial f}{\partial x}(t,x) = g(t,x)$. Applying Itô's lemma to $f(t,B_t)$ gives

$$
df(t,B_t)
=
\frac{\partial f}{\partial t}\,dt
+
\frac{\partial f}{\partial x}\,dB_t
+
\frac{1}{2}
\frac{\partial^2 f}{\partial x^2}\,dt
$$

Rearranging isolates the stochastic integral and expresses it in terms of $f(t,B_t)$ and ordinary integrals.

---

### Example 1: Integral of B dB

Choose $f(x) = \frac{x^2}{2}$, so that $f'(x) = x$.

$$
f'(x) = x, \qquad f''(x) = 1
$$

Applying Itô's lemma:

$$
d\!\left(\frac{B_t^2}{2}\right) = B_t\,dB_t + \frac{1}{2}\,dt
$$

Integrating from $0$ to $t$:

$$
\boxed{
\int_0^t B_s\,dB_s = \frac{B_t^2 - t}{2}
}
$$

This identity implies that $B_t^2 - t$ is a martingale.

---

### Example 2: Integral of s dB

The integrand $s$ is **deterministic and square-integrable**. For deterministic integrands, the Itô isometry gives the distribution directly: the integral is Gaussian with zero mean (since all Itô integrals of deterministic square-integrable integrands are centered Gaussian) and variance

$$
\mathbb{E}\!\left[\left(\int_0^t s\,dB_s\right)^2\right]
= \int_0^t s^2\,ds = \frac{t^3}{3}
$$

Therefore (where $\overset{d}{=}$ denotes equality in distribution):

$$
\boxed{
\int_0^t s\,dB_s \overset{d}{=} \mathcal{N}\!\left(0,\frac{t^3}{3}\right)
}
$$

For a path-by-path expression, apply the antiderivative approach with $f(t,x) = tx$, so $f_t = x$, $f_x = t$, $f_{xx} = 0$. Itô's lemma gives:

$$
d(tB_t) = B_t\,dt + t\,dB_t
$$

Integrating and solving for the stochastic integral:

$$
\int_0^t s\,dB_s = tB_t - \int_0^t B_s\,ds
$$

This path-by-path identity is consistent with the Gaussian characterization above.

---

### Example 3: Integral of sB dB

Choose $f(t,x) = \frac{1}{2}tx^2$, so that $\frac{\partial f}{\partial x} = tx$.

$$
\frac{\partial f}{\partial t} = \frac{1}{2}x^2,
\quad
\frac{\partial f}{\partial x} = tx,
\quad
\frac{\partial^2 f}{\partial x^2} = t
$$

Applying the time-dependent Itô formula:

$$
d\!\left(\frac{1}{2}tB_t^2\right)
= \frac{1}{2}B_t^2\,dt + tB_t\,dB_t + \frac{1}{2}t\,dt
$$

Isolating the stochastic term:

$$
tB_t\,dB_t = d\!\left(\frac{1}{2}tB_t^2\right) - \frac{1}{2}B_t^2\,dt - \frac{1}{2}t\,dt
$$

Integrating and evaluating $\int_0^t \frac{1}{2}s\,ds = \frac{1}{4}t^2$:

$$
\boxed{
\int_0^t sB_s\,dB_s
= \frac{1}{2}tB_t^2 - \frac{1}{2}\int_0^t B_s^2\,ds - \frac{1}{4}t^2
}
$$

The integral $\int_0^t B_s^2\,ds$ has no closed form and is left as is. This example shows how **time dependence introduces additional drift terms**.

---

### Example 4: Integral of B² dB

Choose $f(x) = \frac{x^3}{3}$, so that $f'(x) = x^2$.

$$
f'(x) = x^2, \qquad f''(x) = 2x
$$

Applying Itô's lemma:

$$
d\!\left(\frac{B_t^3}{3}\right) = B_t^2\,dB_t + B_t\,dt
$$

Therefore:

$$
\boxed{
\int_0^t B_s^2\,dB_s = \frac{B_t^3}{3} - \int_0^t B_s\,ds
}
$$

The integral $\int_0^t B_s\,ds$ has no closed form and is left as is.

---

### Example 5: Integral of exp(B) dB

Apply Itô's lemma to $f(x) = e^x$:

$$
d(e^{B_t}) = e^{B_t}\,dB_t + \frac{1}{2}e^{B_t}\,dt
$$

Integrating and rearranging:

$$
\boxed{
\int_0^t e^{B_s}\,dB_s = e^{B_t} - 1 - \frac{1}{2}\int_0^t e^{B_s}\,ds
}
$$

The integral $\int_0^t e^{B_s}\,ds$ has no closed form and is left as is.

---

## 2. Constructing Martingales

A sufficient condition for $M_t$ to be a **local martingale** is that its Itô differential has no $dt$ term. Under suitable integrability conditions (such as Novikov's condition for exponential processes), it is a true martingale. Itô's lemma makes the vanishing-drift condition explicit and checkable.

---

### Example 6: The Exponential Martingale

For $\theta \in \mathbb{R}$, define

$$
Z_t = \exp\!\left(\theta B_t - \frac{1}{2}\theta^2 t\right)
$$

Apply Itô's lemma to $f(t,x) = e^{\theta x - \frac{1}{2}\theta^2 t}$:

$$
f_t = -\frac{1}{2}\theta^2 e^{\theta x - \frac{1}{2}\theta^2 t},
\quad
f_x = \theta e^{\theta x - \frac{1}{2}\theta^2 t},
\quad
f_{xx} = \theta^2 e^{\theta x - \frac{1}{2}\theta^2 t}
$$

The $dt$ coefficient is $f_t + \frac{1}{2}f_{xx} = -\frac{1}{2}\theta^2 Z_t + \frac{1}{2}\theta^2 Z_t = 0$, so:

$$
\boxed{dZ_t = \theta Z_t\,dB_t}
$$

Since the $dt$ coefficient vanishes, $Z_t$ is a local martingale. It is a true martingale by Novikov's condition: $\mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\theta^2 T\right)\right] < \infty$ for all finite $T$, which holds since $\theta$ is a constant. This SDE has the explicit solution $Z_t = Z_0\exp(\theta B_t - \frac{1}{2}\theta^2 t)$, confirming that the original definition and the SDE are consistent.

This process is fundamental in **Girsanov's theorem** and **risk-neutral pricing**.

---

## 3. Solving Stochastic Differential Equations

The standard approach is to guess a transformation $f(t, X_t)$ that converts the SDE into a simpler (often deterministic-coefficient) equation, then integrate.

---

### Example 7: Geometric Brownian Motion

Consider

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dB_t, \qquad S_0 = s_0
$$

where $\mu \in \mathbb{R}$ and $\sigma > 0$ are constants. Apply Itô's lemma to $f(x) = \log x$:

$$
f'(x) = \frac{1}{x}, \qquad f''(x) = -\frac{1}{x^2}
$$

First compute the quadratic variation term:

$$
(dS_t)^2 = \sigma^2 S_t^2\,dt
$$

Substituting $dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$ and $(dS_t)^2 = \sigma^2 S_t^2\,dt$:

$$
d(\log S_t)
= \frac{1}{S_t}(\mu S_t\,dt + \sigma S_t\,dB_t) - \frac{1}{2}\frac{1}{S_t^2}\cdot\sigma^2 S_t^2\,dt
= \left(\mu - \frac{1}{2}\sigma^2\right)dt + \sigma\,dB_t
$$

Integrating:

$$
\boxed{
S_t = s_0\exp\!\left[\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma B_t\right]
}
$$

The Itô correction $-\frac{1}{2}\sigma^2$ is the convexity adjustment between arithmetic drift and geometric growth rate. This process is the foundation of the **Black–Scholes model**.

---

## 4. Further Process Transformations

The example below applies Itô's lemma directly to a process transformation, illustrating how the correction term can introduce unexpected drift even when the original function has no explicit time dependence.

---

### Example 8: Reciprocal of Brownian Motion

Let $B_0 = b \neq 0$ (we require $b \neq 0$ since $f(x) = 1/x$ is undefined at $x = 0$) and let $Y_t = 1/B_t$, valid up to $\tau_0 = \inf\{t > 0 : B_t = 0\}$. For $f(x) = 1/x$:

$$
f'(x) = -\frac{1}{x^2}, \qquad f''(x) = \frac{2}{x^3}
$$

Applying Itô's lemma:

$$
d\!\left(\frac{1}{B_t}\right) = -\frac{1}{B_t^2}\,dB_t + \frac{1}{B_t^3}\,dt
$$

The $dt$ term $\frac{1}{B_t^3}\,dt$ is a non-zero drift, so $1/B_t$ is **not** a local martingale. The Itô correction introduces a drift even though $f(x) = 1/x$ has no explicit time dependence. In integral form:

$$
\boxed{
\frac{1}{B_t} = \frac{1}{b} - \int_0^t \frac{1}{B_s^2}\,dB_s + \int_0^t \frac{1}{B_s^3}\,ds
}
$$

---

## Summary

| Technique | Key step | Examples |
|---|---|---|
| Evaluate stochastic integrals | Find $f$ with $f_x = g$; apply Itô's lemma and rearrange | 1–5 |
| Construct martingales | Verify that $dt$ coefficient vanishes; check integrability | 6 |
| Solve SDEs | Apply a simplifying transformation; integrate | 7 |
| Process transformations | Apply Itô's lemma directly; correction term produces non-zero drift from curvature even without explicit time dependence | 8 |

---

## Exercises

**Exercise 1.** Evaluate $\int_0^t B_s^3\,dB_s$ by choosing an appropriate function $f(x)$ with $f'(x) = x^3$ and applying Itô's lemma. Express your answer in terms of $B_t$ and an ordinary integral.

??? success "Solution to Exercise 1"
    Choose $f(x) = \frac{1}{4}x^4$, so $f'(x) = x^3$ and $f''(x) = 3x^2$. Itô's lemma gives:

    $$
    d\!\left(\frac{B_t^4}{4}\right) = B_t^3\,dB_t + \frac{1}{2}(3B_t^2)\,dt
    $$

    Integrating from $0$ to $t$ (with $B_0 = 0$):

    $$
    \frac{B_t^4}{4} = \int_0^t B_s^3\,dB_s + \frac{3}{2}\int_0^t B_s^2\,ds
    $$

    Therefore:

    $$
    \int_0^t B_s^3\,dB_s = \frac{1}{4}B_t^4 - \frac{3}{2}\int_0^t B_s^2\,ds
    $$

---

**Exercise 2.** For $\theta \in \mathbb{R}$, define $M_t = \cos(\theta B_t)\,e^{\theta^2 t/2}$. Apply Itô's lemma to show that $dM_t$ has no $dt$ term, and conclude that $M_t$ is a local martingale. Write the SDE satisfied by $M_t$.

??? success "Solution to Exercise 2"
    For $M_t = \cos(\theta B_t)\,e^{\theta^2 t/2}$, write $f(t, x) = \cos(\theta x)\,e^{\theta^2 t/2}$. Compute:

    - $f_t = \frac{\theta^2}{2}\cos(\theta x)\,e^{\theta^2 t/2}$
    - $f_x = -\theta\sin(\theta x)\,e^{\theta^2 t/2}$
    - $f_{xx} = -\theta^2\cos(\theta x)\,e^{\theta^2 t/2}$

    By Itô's lemma (Version 2):

    $$
    dM_t = \left(\frac{\theta^2}{2}\cos(\theta B_t) + \frac{1}{2}(-\theta^2\cos(\theta B_t))\right)e^{\theta^2 t/2}\,dt - \theta\sin(\theta B_t)\,e^{\theta^2 t/2}\,dB_t
    $$

    The $dt$ coefficient is $\left(\frac{\theta^2}{2} - \frac{\theta^2}{2}\right)\cos(\theta B_t)\,e^{\theta^2 t/2} = 0$. Therefore:

    $$
    dM_t = -\theta\sin(\theta B_t)\,e^{\theta^2 t/2}\,dB_t
    $$

    Since the $dt$ term vanishes, $M_t$ is a local martingale.

---

**Exercise 3.** The Ornstein--Uhlenbeck process satisfies $dX_t = -\theta X_t\,dt + \sigma\,dB_t$ with $X_0 = x_0$. Apply Itô's lemma to $f(t, x) = e^{\theta t}x$ to derive the explicit solution for $X_t$. (Hint: the product-rule approach in Example 7 of the Itô Rules page uses the same idea.)

??? success "Solution to Exercise 3"
    The Ornstein--Uhlenbeck SDE is $dX_t = -\theta X_t\,dt + \sigma\,dB_t$. Let $f(t, x) = e^{\theta t}x$. Then:

    - $f_t = \theta e^{\theta t}x$
    - $f_x = e^{\theta t}$
    - $f_{xx} = 0$

    Since $X_t$ is the Itô process with $\mu_t = -\theta X_t$ and $\sigma_t = \sigma$, Version 3 gives:

    $$
    d(e^{\theta t}X_t) = \left(\theta e^{\theta t}X_t + e^{\theta t}(-\theta X_t) + \frac{1}{2}(0)\sigma^2\right)dt + e^{\theta t}\sigma\,dB_t
    $$

    The $dt$ coefficient simplifies to $0$, so $d(e^{\theta t}X_t) = \sigma e^{\theta t}\,dB_t$. Integrating:

    $$
    e^{\theta t}X_t = x_0 + \sigma\int_0^t e^{\theta s}\,dB_s
    $$

    Therefore:

    $$
    X_t = e^{-\theta t}x_0 + \sigma e^{-\theta t}\int_0^t e^{\theta s}\,dB_s = e^{-\theta t}x_0 + \sigma\int_0^t e^{-\theta(t-s)}\,dB_s
    $$

---

**Exercise 4.** Let $dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$ be geometric Brownian motion. Apply Itô's lemma to $f(x) = x^p$ for a constant $p \in \mathbb{R}$ to compute $d(S_t^p)$. Show that

$$
S_t^p = S_0^p \exp\!\left[\left(p\mu + \frac{1}{2}p(p-1)\sigma^2\right)t + p\sigma B_t\right]
$$

??? success "Solution to Exercise 4"
    For $f(x) = x^p$ with $dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$: $f'(x) = px^{p-1}$, $f''(x) = p(p-1)x^{p-2}$. By Version 3:

    $$
    d(S_t^p) = \left(pS_t^{p-1}\mu S_t + \frac{1}{2}p(p-1)S_t^{p-2}\sigma^2 S_t^2\right)dt + pS_t^{p-1}\sigma S_t\,dB_t
    $$

    Simplifying:

    $$
    d(S_t^p) = \left(p\mu + \frac{1}{2}p(p-1)\sigma^2\right)S_t^p\,dt + p\sigma S_t^p\,dB_t
    $$

    This is a geometric Brownian motion SDE for $S_t^p$ with drift $p\mu + \frac{1}{2}p(p-1)\sigma^2$ and diffusion $p\sigma$. Applying the log and exponentiating (as in Example 7):

    $$
    S_t^p = S_0^p\exp\!\left[\left(p\mu + \frac{1}{2}p(p-1)\sigma^2 - \frac{1}{2}p^2\sigma^2\right)t + p\sigma B_t\right]
    $$

    Simplifying the drift exponent: $p\mu + \frac{1}{2}p(p-1)\sigma^2 - \frac{1}{2}p^2\sigma^2 = p\mu - \frac{1}{2}p\sigma^2 = p(\mu - \frac{1}{2}\sigma^2)$. Alternatively, since $S_t = S_0\exp((\mu - \frac{1}{2}\sigma^2)t + \sigma B_t)$, raising to power $p$ directly:

    $$
    S_t^p = S_0^p\exp\!\left[\left(p\mu + \frac{1}{2}p(p-1)\sigma^2\right)t + p\sigma B_t\right]
    $$

    where the exponent is $p(\mu - \frac{1}{2}\sigma^2)t + p\sigma B_t = (p\mu - \frac{1}{2}p\sigma^2)t + p\sigma B_t$, and we verify: writing $S_t^p$ as a GBM with drift coefficient $p\mu + \frac{1}{2}p(p-1)\sigma^2$ and applying the log-to-exponential conversion with convexity adjustment $-\frac{1}{2}(p\sigma)^2$ confirms the stated formula.

---

**Exercise 5.** Evaluate $\int_0^t (1 + B_s^2)\,dB_s$ by splitting the integral and applying Itô's lemma to appropriate antiderivatives for each term. Express the result using $B_t$ and ordinary integrals.

??? success "Solution to Exercise 5"
    Split the integral: $\int_0^t (1 + B_s^2)\,dB_s = \int_0^t dB_s + \int_0^t B_s^2\,dB_s$.

    The first integral is simply $B_t - B_0 = B_t$.

    For the second integral, choose $f(x) = \frac{1}{3}x^3$ with $f'(x) = x^2$ and $f''(x) = 2x$. Itô's lemma gives:

    $$
    \int_0^t B_s^2\,dB_s = \frac{1}{3}B_t^3 - \int_0^t B_s\,ds
    $$

    Combining:

    $$
    \int_0^t (1 + B_s^2)\,dB_s = B_t + \frac{1}{3}B_t^3 - \int_0^t B_s\,ds
    $$

---

**Exercise 6.** Apply Itô's lemma to $f(x) = \log(x^2) = 2\log(x)$ for $x > 0$ with $dX_t = \mu X_t\,dt + \sigma X_t\,dB_t$. Verify that you obtain twice the result from the $\log(x)$ computation in Example 7. Explain why this must be the case.

??? success "Solution to Exercise 6"
    For $f(x) = \log(x^2) = 2\log(x)$ with $x > 0$ and $dX_t = \mu X_t\,dt + \sigma X_t\,dB_t$:

    $$
    f'(x) = \frac{2}{x}, \qquad f''(x) = -\frac{2}{x^2}
    $$

    By Itô's lemma (Version 3):

    $$
    d(\log(X_t^2)) = \frac{2}{X_t}(\mu X_t\,dt + \sigma X_t\,dB_t) + \frac{1}{2}\left(-\frac{2}{X_t^2}\right)\sigma^2 X_t^2\,dt
    $$

    $$
    = 2\mu\,dt + 2\sigma\,dB_t - \sigma^2\,dt = 2\!\left(\mu - \frac{\sigma^2}{2}\right)dt + 2\sigma\,dB_t
    $$

    This is exactly twice the result from the $\log(x)$ computation: $d(\log X_t) = (\mu - \frac{\sigma^2}{2})\,dt + \sigma\,dB_t$. This must be the case because $\log(x^2) = 2\log(x)$, so by linearity of the differential, $d(\log(X_t^2)) = 2\,d(\log X_t)$.

---

**Exercise 7.** Let $B_0 = b > 0$ and define $Y_t = B_t^2$ for $t < \tau_0 = \inf\{t : B_t = 0\}$. Use Itô's lemma to compute $dY_t$. Then apply Itô's lemma again to $g(y) = \sqrt{y}$ to recover $dB_t$ from $dY_t$, and verify consistency. What regularity condition on $g$ fails at $y = 0$, and why does this matter?

??? success "Solution to Exercise 7"
    For $Y_t = B_t^2$ with $f(x) = x^2$: $f'(x) = 2x$, $f''(x) = 2$. Itô's lemma gives:

    $$
    dY_t = 2B_t\,dB_t + dt
    $$

    Now apply $g(y) = \sqrt{y}$ to $Y_t$. For $y > 0$: $g'(y) = \frac{1}{2}y^{-1/2}$, $g''(y) = -\frac{1}{4}y^{-3/2}$. The quadratic variation of $Y_t$ is $(dY_t)^2 = (2B_t\,dB_t + dt)^2 = 4B_t^2\,dt$ (only the $(dB_t)^2$ term survives). Itô's lemma gives:

    $$
    d(\sqrt{Y_t}) = \frac{1}{2}Y_t^{-1/2}\,dY_t + \frac{1}{2}\left(-\frac{1}{4}\right)Y_t^{-3/2}(dY_t)^2
    $$

    Substituting $Y_t = B_t^2$, $dY_t = 2B_t\,dB_t + dt$, $(dY_t)^2 = 4B_t^2\,dt$:

    $$
    d|B_t| = \frac{1}{2|B_t|}(2B_t\,dB_t + dt) - \frac{1}{8}|B_t|^{-3} \cdot 4B_t^2\,dt
    $$

    $$
    = \frac{B_t}{|B_t|}\,dB_t + \frac{1}{2|B_t|}\,dt - \frac{1}{2|B_t|}\,dt = \operatorname{sgn}(B_t)\,dB_t
    $$

    For $B_t > 0$ (which holds for $t < \tau_0$), $\operatorname{sgn}(B_t) = 1$, so $d(\sqrt{Y_t}) = dB_t$, which is consistent.

    The regularity condition that fails at $y = 0$ is $C^2$ smoothness: $g''(y) = -\frac{1}{4}y^{-3/2} \to -\infty$ as $y \to 0^+$. Itô's lemma requires $g \in C^2$, so the formula breaks down when $B_t$ hits zero (i.e., $Y_t = 0$). This is why we restrict to $t < \tau_0$.
