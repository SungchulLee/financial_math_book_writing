# Itô–Doeblin Formula

!!! info "Source"
    Converted from **4.3 Itô–Doeblin Formula** in the
    *quantitative-finance-notebooks* collection.
    References: Shreve (2004) *Stochastic Calculus for Finance II*;
    Øksendal (2003) *Stochastic Differential Equations*.

---

## 1. Motivation

In ordinary calculus, the **chain rule** tells us how to differentiate a composite function:

$$
\frac{d}{dt} f(x(t)) = f'(x(t))\, x'(t).
$$

When $x(t)$ is replaced by a stochastic process such as Brownian motion $W_t$, the chain rule must be modified because $W_t$ has **non-zero quadratic variation**. The Itô–Doeblin formula (commonly called **Itô's lemma**) is the stochastic counterpart of the chain rule.

---

## 2. Quadratic Variation of Brownian Motion

Recall that for Brownian motion $W_t$, the **quadratic variation** over $[0, t]$ is:

$$
[W, W]_t = \lim_{n \to \infty} \sum_{k=0}^{n-1} \bigl(W_{t_{k+1}} - W_{t_k}\bigr)^2 = t,
$$

where the limit is taken over partitions $0 = t_0 < t_1 < \cdots < t_n = t$ with mesh going to zero. This is the key property that distinguishes stochastic calculus from ordinary calculus: informally, $(dW_t)^2 = dt$.

The **multiplication rules** for stochastic differentials are:

| | $dt$ | $dW_t$ |
|---|---|---|
| $dt$ | $0$ | $0$ |
| $dW_t$ | $0$ | $dt$ |

---

## 3. Itô–Doeblin Formula (One Dimension)

### 3.1 Statement

Let $f(t, x)$ be a function that is once continuously differentiable in $t$ and twice continuously differentiable in $x$, and let $X_t$ be an **Itô process**:

$$
dX_t = \mu(t, X_t)\, dt + \sigma(t, X_t)\, dW_t.
$$

Then $Y_t = f(t, X_t)$ is also an Itô process, and:

$$
df(t, X_t) = \frac{\partial f}{\partial t}\, dt + \frac{\partial f}{\partial x}\, dX_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\,(dX_t)^2.
$$

Substituting $dX_t$ and applying the multiplication rules:

$$
\boxed{df(t, X_t) = \left(\frac{\partial f}{\partial t} + \mu\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}\right) dt + \sigma \frac{\partial f}{\partial x}\, dW_t.}
$$

### 3.2 Comparison with the Ordinary Chain Rule

In ordinary calculus:

$$
df = \frac{\partial f}{\partial t}\, dt + \frac{\partial f}{\partial x}\, dx.
$$

The Itô formula has the **extra term** $\frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}\, dt$, which arises from the non-zero quadratic variation of Brownian motion.

---

## 4. Examples

### 4.1 Brownian Motion Squared

Let $f(x) = x^2$ and $X_t = W_t$. Then $\frac{\partial f}{\partial x} = 2x$, $\frac{\partial^2 f}{\partial x^2} = 2$, and:

$$
d(W_t^2) = 2W_t\, dW_t + \frac{1}{2}(2)\, dt = 2W_t\, dW_t + dt.
$$

In integral form:

$$
W_t^2 = 2\int_0^t W_s\, dW_s + t,
$$

which gives the famous identity:

$$
\int_0^t W_s\, dW_s = \frac{1}{2}W_t^2 - \frac{1}{2}t.
$$

### 4.2 Geometric Brownian Motion

Let $S_t$ follow:

$$
dS_t = \mu S_t\, dt + \sigma S_t\, dW_t.
$$

Apply Itô's formula to $f(x) = \ln x$. Then $f'(x) = 1/x$, $f''(x) = -1/x^2$:

$$
d(\ln S_t) = \frac{1}{S_t}\, dS_t - \frac{1}{2}\frac{1}{S_t^2}\, \sigma^2 S_t^2\, dt = \left(\mu - \frac{\sigma^2}{2}\right) dt + \sigma\, dW_t.
$$

Integrating:

$$
\ln S_t - \ln S_0 = \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t,
$$

so:

$$
S_t = S_0 \exp\!\left\{\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right\}.
$$

### 4.3 Exponential Martingale

Let $f(x) = e^{\sigma x - \frac{1}{2}\sigma^2 t}$ applied to $X_t = W_t$. Define $Z_t = e^{\sigma W_t - \frac{1}{2}\sigma^2 t}$. By Itô's formula:

$$
dZ_t = \sigma Z_t\, dW_t.
$$

Since the drift term vanishes, $Z_t$ is a **martingale** (the stochastic exponential). This is fundamental to the **Girsanov theorem** and risk-neutral pricing.

---

## 5. Itô–Doeblin Formula (Multi-Dimensional)

Let $\mathbf{W}_t = (W_t^1, \ldots, W_t^d)$ be a $d$-dimensional Brownian motion and let $X_t$ satisfy:

$$
dX_t^i = \mu_i\, dt + \sum_{j=1}^d \sigma_{ij}\, dW_t^j, \quad i = 1, \ldots, n.
$$

For $f(t, x_1, \ldots, x_n) \in C^{1,2}$:

$$
df = \frac{\partial f}{\partial t}\, dt + \sum_{i=1}^n \frac{\partial f}{\partial x_i}\, dX_t^i + \frac{1}{2}\sum_{i=1}^n \sum_{k=1}^n \frac{\partial^2 f}{\partial x_i \partial x_k}\, d[X^i, X^k]_t,
$$

where the **cross-variation** is:

$$
d[X^i, X^k]_t = \sum_{j=1}^d \sigma_{ij}\, \sigma_{kj}\, dt.
$$

---

## 6. Itô Product Rule

For two Itô processes $X_t$ and $Y_t$:

$$
d(X_t Y_t) = X_t\, dY_t + Y_t\, dX_t + dX_t\, dY_t.
$$

The extra term $dX_t\, dY_t$ (the **cross-variation**) is absent in ordinary calculus and is a direct consequence of the Itô formula.

---

## 7. Itô vs Stratonovich

The **Stratonovich integral**, denoted $\circ\, dW_t$, satisfies the ordinary chain rule without correction terms. If

$$
dX_t = \mu\, dt + \sigma \circ dW_t,
$$

then $df(X_t) = f'(X_t) \circ dX_t$, with no second-order correction. The two formulations are related by:

$$
\sigma \circ dW_t = \sigma\, dW_t + \frac{1}{2}\sigma'(X_t)\,\sigma(X_t)\, dt.
$$

In finance, the **Itô convention** is standard because Itô integrals are **non-anticipating** (adapted), which aligns with the requirement that trading strategies cannot look into the future.

---

## 8. Why "Doeblin"?

Wolfgang Doeblin (1915–1940) independently discovered the formula during World War II. His sealed manuscript, deposited at the French Academy of Sciences in 1940, was only opened in 2000. It contained results equivalent to what Kiyosi Itô published in 1951. The name **Itô–Doeblin formula** honors both contributors.
