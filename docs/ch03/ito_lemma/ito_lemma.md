# Itô's Lemma

## 1. Concept Definition

Itô's lemma is the **stochastic analogue of the chain rule** — the fundamental computational tool of stochastic calculus. It describes how a smooth function of a stochastic process evolves over time.

!!! tip "Key idea at a glance"

    In ordinary calculus, only first-order terms survive in the chain rule because \((\Delta x)^2\) is negligible. For Brownian motion, \((\Delta B_t)^2 \sim \Delta t\) is **not negligible**, so a second-derivative correction term appears. This **Itô correction** distinguishes stochastic calculus from classical calculus.

!!! info "How this page fits"

    For the derivation of why \((dB_t)^2 = dt\) survives, see [From Taylor to Itô](from_taylor_to_ito.md). For the full multiplication rules and derived identities (product rule, quotient rule), see [Itô Rules](ito_rules.md). For worked examples, see [Applications and Examples](ito_calculus_applications.md). This page states the theorem in its three main forms.

---

## 2. Statement of Itô's Lemma

### Version 1: Function of Brownian Motion Only

Let \(f: \mathbb{R} \to \mathbb{R}\) be \(C^2\) (twice continuously differentiable).

**Theorem (Itô's Lemma).**

$$
\boxed{
df(B_t) = f'(B_t)\,dB_t + \frac{1}{2}f''(B_t)\,dt
}
$$

**Integral form:**

$$
f(B_t) - f(B_0) = \int_0^t f'(B_s)\,dB_s + \frac{1}{2}\int_0^t f''(B_s)\,ds \quad \square
$$

**Quick example.** For \(f(x) = x^2\), we have \(f'(x) = 2x\) and \(f''(x) = 2\), so:

$$
d(B_t^2) = 2B_t\,dB_t + dt
\qquad\Longrightarrow\qquad
\int_0^t B_s\,dB_s = \frac{1}{2}(B_t^2 - t) \quad \text{(with } B_0 = 0\text{)}
$$

The extra \(dt\) is the Itô correction; the classical chain rule would give only \(2B_t\,dB_t\).

---

### Version 2: Function of Time and Brownian Motion

Let \(f: [0,\infty) \times \mathbb{R} \to \mathbb{R}\) be \(C^{1,2}\) (once differentiable in \(t\), twice in \(x\)).

**Theorem (Itô's Lemma, time-dependent).**

$$
\boxed{
df(t, B_t) = \left(\frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\right)dt + \frac{\partial f}{\partial x}\,dB_t
}
$$

**Integral form:**

$$
f(t, B_t) = f(0, B_0)
+ \int_0^t \left(\frac{\partial f}{\partial s}(s, B_s) + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}(s, B_s)\right)ds
+ \int_0^t \frac{\partial f}{\partial x}(s, B_s)\,dB_s \quad \square
$$

**Quick example.** For \(f(t,x) = e^{x - t/2}\):

$$
f_t = -\tfrac{1}{2}e^{x-t/2},\quad
f_x = e^{x-t/2},\quad
f_{xx} = e^{x-t/2}
$$

The \(dt\) coefficient is \(f_t + \frac{1}{2}f_{xx} = -\frac{1}{2}e^{x-t/2} + \frac{1}{2}e^{x-t/2} = 0\), so the \(dt\) terms cancel:

$$
df = e^{B_t - t/2}\,dB_t
$$

Since the \(dt\) coefficient vanishes, $Z_t = e^{B_t - t/2}$ is a **local martingale** (and a true martingale by Novikov's condition: $\mathbb{E}[\exp(\frac{T}{2})] < \infty$ for all finite $T$). This process is the **exponential martingale**.

---

### Version 3: General Itô Process

Let \(X_t\) be an Itô process:

$$
dX_t = \mu_t\,dt + \sigma_t\,dB_t
$$

where \(\mu_t\) and \(\sigma_t\) are adapted processes. For \(f \in C^{1,2}\):

**Theorem (Itô's Lemma, general).**

$$
\boxed{
df(t, X_t) = \left(\frac{\partial f}{\partial t} + \mu_t\frac{\partial f}{\partial x} + \frac{1}{2}\sigma_t^2\frac{\partial^2 f}{\partial x^2}\right)dt + \sigma_t\frac{\partial f}{\partial x}\,dB_t
}
$$

The key step is applying the quadratic variation rule \((dX_t)^2 = \sigma_t^2\,dt\) to the second-order Taylor term. All cross terms involving \(dt\,dB_t\) and \((dt)^2\) vanish by the multiplication table (see [From Taylor to Itô](from_taylor_to_ito.md) for the full derivation and [Itô Rules](ito_rules.md) for the complete table including cross-process terms).

**Integral form:**

$$
f(t, X_t) = f(0, X_0)
+ \int_0^t \left(\frac{\partial f}{\partial s}(s, X_s) + \mu_s\frac{\partial f}{\partial x}(s, X_s) + \frac{1}{2}\sigma_s^2\frac{\partial^2 f}{\partial x^2}(s, X_s)\right)ds
+ \int_0^t \sigma_s\frac{\partial f}{\partial x}(s, X_s)\,dB_s \quad \square
$$

**Quick example.** For \(dS_t = \alpha S_t\,dt + \beta S_t\,dB_t\), where \(\alpha \in \mathbb{R}\) and \(\beta > 0\) are constants, apply Itô's lemma to \(f(x) = \log x\):

$$
f_x = \frac{1}{x}, \qquad f_{xx} = -\frac{1}{x^2}
$$

Substituting into the general formula with drift \(\alpha S_t\) and diffusion \(\beta S_t\):

$$
d(\log S_t)
= \frac{1}{S_t}(\alpha S_t\,dt + \beta S_t\,dB_t) - \frac{1}{2}\frac{1}{S_t^2}\,\beta^2 S_t^2\,dt
= \left(\alpha - \frac{\beta^2}{2}\right)dt + \beta\,dB_t
$$

$$
\boxed{S_t = S_0 \exp\!\left[\left(\alpha - \frac{\beta^2}{2}\right)t + \beta B_t\right]}
$$

The Itô correction \(-\frac{\beta^2}{2}\) is the **convexity adjustment** between the arithmetic drift \(\alpha\) and the geometric growth rate.

---

## 3. Comparison: Classical vs. Stochastic Chain Rule

| | Classical Calculus | Stochastic Calculus |
|---|---|---|
| Chain rule | \(df = f'(x)\,dx\) | \(df = \left(f_t + \mu_t f_x + \frac{1}{2}\sigma_t^2 f_{xx}\right)dt + \sigma_t f_x\,dB_t\) |
| Quadratic term | \((dx)^2 = 0\) | \((dB_t)^2 = dt\) |
| Quadratic variation | \(0\) | \([B]_t = t\) |
| Correction | None | Itô correction \(\frac{1}{2}\sigma_t^2 f_{xx}\,dt\) |

---

## 4. Step-by-Step Application

When computing \(df(t, X_t)\) where \(dX_t = \mu_t\,dt + \sigma_t\,dB_t\):

1. Compute the partial derivatives \(f_t,\; f_x,\; f_{xx}\)
2. Compute \((dX_t)^2 = \sigma_t^2\,dt\) using the Itô multiplication table (see [From Taylor to Itô](from_taylor_to_ito.md))
3. Substitute into the formula:
$$
df = \left(f_t + \mu_t f_x + \tfrac{1}{2}\sigma_t^2 f_{xx}\right)dt + \sigma_t f_x\,dB_t
$$
4. Simplify; if the \(dt\) coefficient vanishes, \(f(t, X_t)\) is a **local martingale** (provided $\sigma_t f_x$ is locally square-integrable, so that the stochastic integral term is a well-defined local martingale). Under an additional integrability condition such as Novikov's condition, it is a true martingale.

For a full set of worked examples — including \(e^{B_t}\), geometric Brownian motion, and the Black-Scholes PDE — see [Applications and Examples](ito_calculus_applications.md).

---

## Exercises

**Exercise 1.** Apply Itô's lemma (Version 1) to $f(x) = x^3$ with $X_t = B_t$. Write down $d(B_t^3)$ and express $\int_0^t B_s^2\,dB_s$ in terms of $B_t^3$ and an ordinary integral.

??? success "Solution to Exercise 1"
    For $f(x) = x^3$: $f'(x) = 3x^2$ and $f''(x) = 6x$. By Itô's lemma (Version 1):

    $$
    d(B_t^3) = 3B_t^2\,dB_t + \frac{1}{2}(6B_t)\,dt = 3B_t^2\,dB_t + 3B_t\,dt
    $$

    Integrating from $0$ to $t$ (with $B_0 = 0$):

    $$
    B_t^3 = 3\int_0^t B_s^2\,dB_s + 3\int_0^t B_s\,ds
    $$

    Solving for the stochastic integral:

    $$
    \int_0^t B_s^2\,dB_s = \frac{1}{3}B_t^3 - \int_0^t B_s\,ds
    $$

---

**Exercise 2.** Let $f(t, x) = e^{-\lambda t}\sin(x)$ where $\lambda$ is a constant. Using Version 2 of Itô's lemma, compute $df(t, B_t)$. For what value of $\lambda$ does the $dt$ coefficient vanish, making $f(t, B_t)$ a local martingale?

??? success "Solution to Exercise 2"
    For $f(t, x) = e^{-\lambda t}\sin(x)$:

    - $f_t = -\lambda e^{-\lambda t}\sin(x)$
    - $f_x = e^{-\lambda t}\cos(x)$
    - $f_{xx} = -e^{-\lambda t}\sin(x)$

    By Itô's lemma (Version 2):

    $$
    df(t, B_t) = \left(-\lambda e^{-\lambda t}\sin(B_t) + \frac{1}{2}(-e^{-\lambda t}\sin(B_t))\right)dt + e^{-\lambda t}\cos(B_t)\,dB_t
    $$

    The $dt$ coefficient is $-(\lambda + \frac{1}{2})e^{-\lambda t}\sin(B_t)$. This vanishes for all $(t, B_t)$ when

    $$
    \lambda = -\frac{1}{2}
    $$

    With $\lambda = -1/2$, the process $e^{t/2}\sin(B_t)$ is a local martingale.

---

**Exercise 3.** Consider the Itô process $dX_t = r X_t\,dt + \sigma X_t\,dB_t$ with constants $r$ and $\sigma > 0$. Apply Version 3 of Itô's lemma to $f(x) = x^2$ to compute $d(X_t^2)$. Express the result in the form $d(X_t^2) = (\cdots)\,dt + (\cdots)\,dB_t$.

??? success "Solution to Exercise 3"
    For $f(x) = x^2$ applied to $X_t$ with $dX_t = rX_t\,dt + \sigma X_t\,dB_t$: $f'(x) = 2x$, $f''(x) = 2$, $\mu_t = rX_t$, $\sigma_t = \sigma X_t$. By Version 3:

    $$
    d(X_t^2) = \left(2X_t \cdot rX_t + \frac{1}{2} \cdot 2 \cdot \sigma^2 X_t^2\right)dt + 2X_t \cdot \sigma X_t\,dB_t
    $$

    Simplifying:

    $$
    d(X_t^2) = (2r + \sigma^2)X_t^2\,dt + 2\sigma X_t^2\,dB_t
    $$

    The process $X_t^2$ itself follows a geometric Brownian motion SDE with drift coefficient $2r + \sigma^2$ and diffusion coefficient $2\sigma$.

---

**Exercise 4.** Verify the comparison table in Section 3 by applying both the classical chain rule and Itô's lemma to $f(x) = e^x$. Specifically:

(a) In the classical case, compute $df = f'(x)\,dx$.

(b) In the stochastic case, compute $d(e^{B_t})$ using Itô's lemma and identify the Itô correction term.

??? success "Solution to Exercise 4"
    **(a)** Classical chain rule: for $f(x) = e^x$, $df = f'(x)\,dx = e^x\,dx$.

    **(b)** Stochastic case with $X_t = B_t$: $f'(x) = e^x$, $f''(x) = e^x$. Itô's lemma gives:

    $$
    d(e^{B_t}) = e^{B_t}\,dB_t + \frac{1}{2}e^{B_t}\,dt
    $$

    The term $\frac{1}{2}e^{B_t}\,dt$ is the Itô correction. It has no classical counterpart and arises from the quadratic variation $(dB_t)^2 = dt$. The correction is always positive (since $e^{B_t} > 0$), reflecting the positive curvature ($f'' > 0$) of the exponential function — symmetric Brownian fluctuations around any point produce a net upward drift.

---

**Exercise 5.** Let $dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$ and $f(x) = x^{-1}$. Apply Itô's lemma to compute $d(S_t^{-1})$. Show that $S_t^{-1}$ satisfies an SDE of the form $d(S_t^{-1}) = \alpha S_t^{-1}\,dt + \beta S_t^{-1}\,dB_t$ and determine $\alpha$ and $\beta$ in terms of $\mu$ and $\sigma$.

??? success "Solution to Exercise 5"
    For $f(x) = x^{-1}$: $f'(x) = -x^{-2}$, $f''(x) = 2x^{-3}$. With $dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$ (so $\mu_t = \mu S_t$, $\sigma_t = \sigma S_t$):

    $$
    d(S_t^{-1}) = \left(-S_t^{-2} \cdot \mu S_t + \frac{1}{2} \cdot 2S_t^{-3} \cdot \sigma^2 S_t^2\right)dt + (-S_t^{-2}) \cdot \sigma S_t\,dB_t
    $$

    Simplifying:

    $$
    d(S_t^{-1}) = (-\mu + \sigma^2)S_t^{-1}\,dt - \sigma S_t^{-1}\,dB_t
    $$

    This is an SDE of the form $d(S_t^{-1}) = \alpha S_t^{-1}\,dt + \beta S_t^{-1}\,dB_t$ with

    $$
    \alpha = -\mu + \sigma^2, \qquad \beta = -\sigma
    $$

    The drift changes from $\mu$ to $-\mu + \sigma^2$: the sign flip comes from the reciprocal, while the extra $\sigma^2$ is the Itô correction due to the positive curvature of $x^{-1}$ for $x > 0$.

---

**Exercise 6.** Using the step-by-step application procedure from Section 4, apply Itô's lemma to $f(t, x) = x\,e^{-rt}$ where $dX_t = r X_t\,dt + \sigma X_t\,dB_t$. Show that the $dt$ coefficient vanishes, and conclude that $X_t e^{-rt}$ is a local martingale. Under what conditions is it a true martingale?

??? success "Solution to Exercise 6"
    For $f(t, x) = xe^{-rt}$ with $dX_t = rX_t\,dt + \sigma X_t\,dB_t$:

    - $f_t = -rx\,e^{-rt}$
    - $f_x = e^{-rt}$
    - $f_{xx} = 0$

    Applying Version 3 with $\mu_t = rX_t$ and $\sigma_t = \sigma X_t$:

    $$
    d(X_t e^{-rt}) = \left(-rX_t e^{-rt} + rX_t \cdot e^{-rt} + \frac{1}{2}\sigma^2 X_t^2 \cdot 0\right)dt + \sigma X_t e^{-rt}\,dB_t
    $$

    The $dt$ coefficient is $-rX_t e^{-rt} + rX_t e^{-rt} = 0$, so

    $$
    d(X_t e^{-rt}) = \sigma X_t e^{-rt}\,dB_t
    $$

    Since the $dt$ coefficient vanishes, $X_t e^{-rt}$ is a local martingale. It is a true martingale if $\sigma X_t e^{-rt}$ is locally square-integrable. Since $X_t$ is geometric Brownian motion ($X_t = X_0 \exp((\mu - \sigma^2/2)t + \sigma B_t)$, with $\mu = r$ here), Novikov's condition $\mathbb{E}[\exp(\frac{1}{2}\int_0^T \sigma^2\,ds)] = e^{\sigma^2 T/2} < \infty$ holds for all finite $T$, so $X_t e^{-rt}$ is a true martingale.

---

**Exercise 7.** Consider $f(x) = \log(1 + x^2)$. Compute $f'(x)$ and $f''(x)$, then apply Itô's lemma (Version 1) to write $d(\log(1 + B_t^2))$. Does the process $\log(1 + B_t^2)$ have a positive or negative drift? Interpret this in terms of the convexity of $f$.

??? success "Solution to Exercise 7"
    For $f(x) = \log(1 + x^2)$:

    $$
    f'(x) = \frac{2x}{1 + x^2}, \qquad f''(x) = \frac{2(1 + x^2) - 2x \cdot 2x}{(1 + x^2)^2} = \frac{2(1 - x^2)}{(1 + x^2)^2}
    $$

    By Itô's lemma (Version 1):

    $$
    d(\log(1 + B_t^2)) = \frac{2B_t}{1 + B_t^2}\,dB_t + \frac{1}{2} \cdot \frac{2(1 - B_t^2)}{(1 + B_t^2)^2}\,dt
    $$

    The drift is

    $$
    \frac{1 - B_t^2}{(1 + B_t^2)^2}\,dt
    $$

    This is positive when $|B_t| < 1$ and negative when $|B_t| > 1$. The sign of the drift reflects the convexity of $f$: for $|x| < 1$, $f''(x) > 0$ (convex), so the Itô correction pushes the drift upward; for $|x| > 1$, $f''(x) < 0$ (concave), so the correction pushes the drift downward. At $|B_t| = 1$, the function has an inflection point and the drift vanishes.
