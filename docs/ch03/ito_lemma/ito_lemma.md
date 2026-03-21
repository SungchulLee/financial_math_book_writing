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
