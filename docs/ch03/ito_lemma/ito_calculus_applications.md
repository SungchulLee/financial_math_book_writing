# Applications and Examples of Itô Calculus

Once the main rules of stochastic calculus have been developed — Itô's lemma, the product rule, and integration by parts — we can use them to compute stochastic integrals, construct martingales, and solve stochastic differential equations (SDEs).

This section presents a collection of worked examples illustrating how these tools are applied in practice. For the theorem statements being applied throughout, see [Itô's Lemma](ito_lemma.md). For the multiplication rules used in SDE substitutions, see [Itô Rules](ito_rules.md).

---

## 1. Evaluating Stochastic Integrals

One of the most important uses of Itô's lemma is to evaluate stochastic integrals of the form

$$
\int_0^t g(s,B_s)\,dB_s
$$

The key idea is to **choose a function \(f(t,x)\)** whose derivative with respect to \(x\) matches the integrand.

### General Strategy

Choose \(f(t,x)\) such that \(\frac{\partial f}{\partial x}(t,x) = g(t,x)\). Applying Itô's lemma to \(f(t,B_t)\) gives

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

Rearranging isolates the stochastic integral and expresses it in terms of \(f(t,B_t)\) and ordinary integrals.

---

### Example 1: \(\displaystyle\int_0^t B_s\,dB_s\)

Choose \(f(x) = \frac{x^2}{2}\), so that \(f'(x) = x\).

$$
f'(x) = x, \qquad f''(x) = 1
$$

Applying Itô's lemma:

$$
d\!\left(\frac{B_t^2}{2}\right) = B_t\,dB_t + \frac{1}{2}\,dt
$$

Integrating from \(0\) to \(t\):

$$
\boxed{
\int_0^t B_s\,dB_s = \frac{B_t^2 - t}{2}
}
$$

This identity implies that \(B_t^2 - t\) is a martingale.

---

### Example 2: \(\displaystyle\int_0^t s\,dB_s\)

The integrand \(s\) is **deterministic and square-integrable**. For deterministic integrands, the Itô isometry gives the distribution directly: the integral is Gaussian with zero mean (since all Itô integrals of deterministic square-integrable integrands are centered Gaussian) and variance

$$
\mathbb{E}\!\left[\left(\int_0^t s\,dB_s\right)^2\right]
= \int_0^t s^2\,ds = \frac{t^3}{3}
$$

Therefore (where \(\overset{d}{=}\) denotes equality in distribution):

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

### Example 3: \(\displaystyle\int_0^t sB_s\,dB_s\)

Choose \(f(t,x) = \frac{1}{2}tx^2\), so that \(\frac{\partial f}{\partial x} = tx\).

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

The integral \(\int_0^t B_s^2\,ds\) has no closed form and is left as is. This example shows how **time dependence introduces additional drift terms**.

---

### Example 4: \(\displaystyle\int_0^t B_s^2\,dB_s\)

Choose \(f(x) = \frac{x^3}{3}\), so that \(f'(x) = x^2\).

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

The integral \(\int_0^t B_s\,ds\) has no closed form and is left as is.

---

### Example 5: \(\displaystyle\int_0^t e^{B_s}\,dB_s\)

Apply Itô's lemma to \(f(x) = e^x\):

$$
d(e^{B_t}) = e^{B_t}\,dB_t + \frac{1}{2}e^{B_t}\,dt
$$

Integrating and rearranging:

$$
\boxed{
\int_0^t e^{B_s}\,dB_s = e^{B_t} - 1 - \frac{1}{2}\int_0^t e^{B_s}\,ds
}
$$

The integral \(\int_0^t e^{B_s}\,ds\) has no closed form and is left as is.

---

## 2. Constructing Martingales

A sufficient condition for \(M_t\) to be a **local martingale** is that its Itô differential has no \(dt\) term. Under suitable integrability conditions (such as Novikov's condition for exponential processes), it is a true martingale. Itô's lemma makes the vanishing-drift condition explicit and checkable.

---

### Example 6: The Exponential Martingale

For \(\theta \in \mathbb{R}\), define

$$
Z_t = \exp\!\left(\theta B_t - \frac{1}{2}\theta^2 t\right)
$$

Apply Itô's lemma to \(f(t,x) = e^{\theta x - \frac{1}{2}\theta^2 t}\):

$$
f_t = -\frac{1}{2}\theta^2 e^{\theta x - \frac{1}{2}\theta^2 t},
\quad
f_x = \theta e^{\theta x - \frac{1}{2}\theta^2 t},
\quad
f_{xx} = \theta^2 e^{\theta x - \frac{1}{2}\theta^2 t}
$$

The \(dt\) coefficient is \(f_t + \frac{1}{2}f_{xx} = -\frac{1}{2}\theta^2 Z_t + \frac{1}{2}\theta^2 Z_t = 0\), so:

$$
\boxed{dZ_t = \theta Z_t\,dB_t}
$$

Since the \(dt\) coefficient vanishes, \(Z_t\) is a local martingale. It is a true martingale by Novikov's condition: $\mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\theta^2 T\right)\right] < \infty$ for all finite $T$, which holds since $\theta$ is a constant. This SDE has the explicit solution $Z_t = Z_0\exp(\theta B_t - \frac{1}{2}\theta^2 t)$, confirming that the original definition and the SDE are consistent.

This process is fundamental in **Girsanov's theorem** and **risk-neutral pricing**.

---

## 3. Solving Stochastic Differential Equations

The standard approach is to guess a transformation \(f(t, X_t)\) that converts the SDE into a simpler (often deterministic-coefficient) equation, then integrate.

---

### Example 7: Geometric Brownian Motion

Consider

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dB_t, \qquad S_0 = s_0
$$

where \(\mu \in \mathbb{R}\) and \(\sigma > 0\) are constants. Apply Itô's lemma to \(f(x) = \log x\):

$$
f'(x) = \frac{1}{x}, \qquad f''(x) = -\frac{1}{x^2}
$$

First compute the quadratic variation term:

$$
(dS_t)^2 = \sigma^2 S_t^2\,dt
$$

Substituting \(dS_t = \mu S_t\,dt + \sigma S_t\,dB_t\) and \((dS_t)^2 = \sigma^2 S_t^2\,dt\):

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

The Itô correction \(-\frac{1}{2}\sigma^2\) is the convexity adjustment between arithmetic drift and geometric growth rate. This process is the foundation of the **Black–Scholes model**.

---

## 4. Further Process Transformations

The example below applies Itô's lemma directly to a process transformation, illustrating how the correction term can introduce unexpected drift even when the original function has no explicit time dependence.

---

### Example 8: Reciprocal of Brownian Motion

Let \(B_0 = b \neq 0\) (we require $b \neq 0$ since $f(x) = 1/x$ is undefined at $x = 0$) and let \(Y_t = 1/B_t\), valid up to \(\tau_0 = \inf\{t > 0 : B_t = 0\}\). For \(f(x) = 1/x\):

$$
f'(x) = -\frac{1}{x^2}, \qquad f''(x) = \frac{2}{x^3}
$$

Applying Itô's lemma:

$$
d\!\left(\frac{1}{B_t}\right) = -\frac{1}{B_t^2}\,dB_t + \frac{1}{B_t^3}\,dt
$$

The \(dt\) term \(\frac{1}{B_t^3}\,dt\) is a non-zero drift, so \(1/B_t\) is **not** a local martingale. The Itô correction introduces a drift even though $f(x) = 1/x$ has no explicit time dependence. In integral form:

$$
\boxed{
\frac{1}{B_t} = \frac{1}{b} - \int_0^t \frac{1}{B_s^2}\,dB_s + \int_0^t \frac{1}{B_s^3}\,ds
}
$$

---

## Summary

| Technique | Key step | Examples |
|---|---|---|
| Evaluate stochastic integrals | Find \(f\) with \(f_x = g\); apply Itô's lemma and rearrange | 1–5 |
| Construct martingales | Verify that \(dt\) coefficient vanishes; check integrability | 6 |
| Solve SDEs | Apply a simplifying transformation; integrate | 7 |
| Process transformations | Apply Itô's lemma directly; correction term produces non-zero drift from curvature even without explicit time dependence | 8 |

---

## Exercises

**Exercise 1.** Evaluate $\int_0^t B_s^3\,dB_s$ by choosing an appropriate function $f(x)$ with $f'(x) = x^3$ and applying Itô's lemma. Express your answer in terms of $B_t$ and an ordinary integral.

---

**Exercise 2.** For $\theta \in \mathbb{R}$, define $M_t = \cos(\theta B_t)\,e^{\theta^2 t/2}$. Apply Itô's lemma to show that $dM_t$ has no $dt$ term, and conclude that $M_t$ is a local martingale. Write the SDE satisfied by $M_t$.

---

**Exercise 3.** The Ornstein--Uhlenbeck process satisfies $dX_t = -\theta X_t\,dt + \sigma\,dB_t$ with $X_0 = x_0$. Apply Itô's lemma to $f(t, x) = e^{\theta t}x$ to derive the explicit solution for $X_t$. (Hint: the product-rule approach in Example 7 of the Itô Rules page uses the same idea.)

---

**Exercise 4.** Let $dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$ be geometric Brownian motion. Apply Itô's lemma to $f(x) = x^p$ for a constant $p \in \mathbb{R}$ to compute $d(S_t^p)$. Show that

$$
S_t^p = S_0^p \exp\!\left[\left(p\mu + \frac{1}{2}p(p-1)\sigma^2\right)t + p\sigma B_t\right]
$$

---

**Exercise 5.** Evaluate $\int_0^t (1 + B_s^2)\,dB_s$ by splitting the integral and applying Itô's lemma to appropriate antiderivatives for each term. Express the result using $B_t$ and ordinary integrals.

---

**Exercise 6.** Apply Itô's lemma to $f(x) = \log(x^2) = 2\log(x)$ for $x > 0$ with $dX_t = \mu X_t\,dt + \sigma X_t\,dB_t$. Verify that you obtain twice the result from the $\log(x)$ computation in Example 7. Explain why this must be the case.

---

**Exercise 7.** Let $B_0 = b > 0$ and define $Y_t = B_t^2$ for $t < \tau_0 = \inf\{t : B_t = 0\}$. Use Itô's lemma to compute $dY_t$. Then apply Itô's lemma again to $g(y) = \sqrt{y}$ to recover $dB_t$ from $dY_t$, and verify consistency. What regularity condition on $g$ fails at $y = 0$, and why does this matter?
