# Itô's Lemma

Itô's lemma is the **fundamental theorem of stochastic calculus**—the stochastic analogue of the chain rule. It is the single most important computational tool for working with stochastic differential equations and underlies virtually all of mathematical finance, from option pricing to risk management.

---

## The Classical Chain Rule (Review)

For a smooth function $f(x)$ and a differentiable path $x(t)$:

$$
\frac{d}{dt}f(x(t)) = f'(x(t)) \cdot \frac{dx}{dt}
$$

Or in differential notation:

$$
df = f'(x)\,dx
$$

**Key feature**: Only **first-order** terms survive.

---

## Why the Classical Chain Rule Fails for Brownian Motion

For Brownian motion $B_t$:

1. $B_t$ is **nowhere differentiable**: $\frac{dB_t}{dt}$ does not exist
2. The **quadratic variation** is non-zero: $(dB_t)^2 = dt$

**Consequence**: Second-order terms in Taylor expansion **do not vanish**.

---

## The Itô Rules (Box Calculus)

For Brownian motion differentials, the multiplication rules are:

$$
\boxed{
(dt)^2 = 0, \qquad dt \cdot dB_t = 0, \qquad (dB_t)^2 = dt
}
$$

**Multiplication table**:

$$
\begin{array}{|c|c|c|}
\hline
\times & dt & dB_t \\
\hline
dt & 0 & 0 \\
\hline
dB_t & 0 & dt \\
\hline
\end{array}
$$

**Interpretation**:

- $dt$ is "infinitely small" compared to $dB_t \sim \sqrt{dt}$
- $(dB_t)^2 \sim dt$ is the **same order** as $dt$
- This is the mathematical content of quadratic variation

---

## Statement of Itô's Lemma

### Version 1: Function of Brownian Motion Only

Let $f: \mathbb{R} \to \mathbb{R}$ be $C^2$ (twice continuously differentiable). Then:

$$
\boxed{
df(B_t) = f'(B_t)\,dB_t + \frac{1}{2}f''(B_t)\,dt
}
$$

**Integral form**:

$$
f(B_t) - f(B_0) = \int_0^t f'(B_s)\,dB_s + \frac{1}{2}\int_0^t f''(B_s)\,ds
$$

### Version 2: Function of Time and Brownian Motion

Let $f: [0,\infty) \times \mathbb{R} \to \mathbb{R}$ be $C^{1,2}$ (once in $t$, twice in $x$). Then:

$$
\boxed{
df(t, B_t) = \frac{\partial f}{\partial t}\,dt + \frac{\partial f}{\partial x}\,dB_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\,dt
}
$$

Equivalently:

$$
\boxed{
df = \left(\frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\right)dt + \frac{\partial f}{\partial x}\,dB_t
}
$$

**Integral form**:

$$
f(t, B_t) = f(0, B_0) + \int_0^t \left(\frac{\partial f}{\partial s} + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\right)(s, B_s)\,ds + \int_0^t \frac{\partial f}{\partial x}(s, B_s)\,dB_s
$$

### Version 3: General Itô Process

Let $X_t$ be an Itô process:

$$
dX_t = \mu_t\,dt + \sigma_t\,dB_t
$$

For $f \in C^{1,2}$:

$$
\boxed{
df(t, X_t) = \frac{\partial f}{\partial t}\,dt + \frac{\partial f}{\partial x}\,dX_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}(dX_t)^2
}
$$

Using $(dX_t)^2 = \sigma_t^2\,dt$:

$$
\boxed{
df(t, X_t) = \left(\frac{\partial f}{\partial t} + \mu_t\frac{\partial f}{\partial x} + \frac{1}{2}\sigma_t^2\frac{\partial^2 f}{\partial x^2}\right)dt + \sigma_t\frac{\partial f}{\partial x}\,dB_t
}
$$

---

## Proof Sketch

**Step 1**: Taylor expand to second order:

$$
f(t+dt, x+dx) - f(t,x) = f_t\,dt + f_x\,dx + \frac{1}{2}f_{tt}(dt)^2 + f_{tx}\,dt\,dx + \frac{1}{2}f_{xx}(dx)^2 + \cdots
$$

**Step 2**: Apply Itô rules with $dx = dB_t$:

- $(dt)^2 = 0$
- $dt \cdot dB_t = 0$  
- $(dB_t)^2 = dt$

**Step 3**: Keep only terms of order $dt$:

$$
df = f_t\,dt + f_x\,dB_t + \frac{1}{2}f_{xx}\,dt
$$

**Rigorous proof**: Involves approximating $B_t$ by step functions, applying the deterministic Taylor expansion to each step, summing, and taking limits. The quadratic variation ensures the second-order term converges to $\frac{1}{2}\int f_{xx}\,ds$.

---

## Key Examples

### Example 1: $f(x) = x^2$

$$
d(B_t^2) = 2B_t\,dB_t + \frac{1}{2}\cdot 2\,dt = 2B_t\,dB_t + dt
$$

**Integral form**:

$$
B_t^2 = 2\int_0^t B_s\,dB_s + t
$$

**Corollary**: The famous Itô integral formula:

$$
\int_0^t B_s\,dB_s = \frac{1}{2}(B_t^2 - t)
$$

### Example 2: $f(x) = e^x$

$$
d(e^{B_t}) = e^{B_t}\,dB_t + \frac{1}{2}e^{B_t}\,dt
$$

**Note**: $e^{B_t}$ is **not** a martingale (the $dt$ term has non-zero drift).

### Example 3: Exponential Martingale $f(t,x) = e^{x - t/2}$

$$
df = \left(-\frac{1}{2}e^{x-t/2} + \frac{1}{2}e^{x-t/2}\right)dt + e^{x-t/2}\,dB_t = e^{B_t - t/2}\,dB_t
$$

The $dt$ terms **cancel**! So $Z_t = e^{B_t - t/2}$ is a martingale.

### Example 4: Geometric Brownian Motion

Let $S_t$ satisfy $dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$. Apply Itô to $f(x) = \log x$:

$$
d(\log S_t) = \frac{1}{S_t}\,dS_t - \frac{1}{2}\frac{1}{S_t^2}(dS_t)^2
$$

$$
= \frac{1}{S_t}(\mu S_t\,dt + \sigma S_t\,dB_t) - \frac{1}{2S_t^2}\sigma^2 S_t^2\,dt
$$

$$
= \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma\,dB_t
$$

**Solution**:

$$
\log S_t = \log S_0 + \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma B_t
$$

$$
\boxed{S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma B_t\right]}
$$

---

## The Itô Correction Term

The term $\frac{1}{2}f''(x)\,dt$ is called the **Itô correction** or **Itô drift**.

**Physical interpretation**: Even without explicit drift, the curvature of $f$ combined with the "roughness" of Brownian motion creates an effective drift.

**Financial interpretation**: The convexity adjustment in option pricing; the difference between arithmetic and geometric means.

---

## Connection to PDEs

Itô's lemma connects SDEs to partial differential equations.

**Observation**: If $f(t, B_t)$ is a martingale, then its $dt$ coefficient must be zero:

$$
\frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^2 f}{\partial x^2} = 0
$$

This is the **heat equation** (backward in time)!

**General connection**: For the SDE $dX_t = \mu(x)\,dt + \sigma(x)\,dB_t$, the function $u(t,x) = \mathbb{E}[g(X_T) | X_t = x]$ satisfies:

$$
\frac{\partial u}{\partial t} + \mu(x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 u}{\partial x^2} = 0
$$

This is the **Kolmogorov backward equation** and the foundation of the **Feynman-Kac formula**.

---

## Common Mistakes to Avoid

1. **Forgetting the correction term**: $d(B_t^2) = 2B_t\,dB_t + dt$, NOT just $2B_t\,dB_t$

2. **Using ordinary chain rule**: $d(e^{B_t}) \neq e^{B_t}\,dB_t$

3. **Wrong order of operations**: Always compute $(dX_t)^2$ first, then substitute

4. **Confusing Itô and Stratonovich**: The correction term is specific to Itô calculus

---

## Summary

$$
\boxed{
\text{Itô's Lemma: } df(t, X_t) = \left(f_t + \mu f_x + \frac{1}{2}\sigma^2 f_{xx}\right)dt + \sigma f_x\,dB_t
}
$$

| Classical Calculus | Stochastic Calculus |
|-------------------|---------------------|
| $df = f'(x)\,dx$ | $df = f'(x)\,dx + \frac{1}{2}f''(x)(dx)^2$ |
| $(dx)^2 = 0$ | $(dB_t)^2 = dt$ |
| Chain rule | Itô's lemma |
| No correction | Itô correction term |

**Itô's lemma is the chain rule for stochastic calculus, with a correction term arising from quadratic variation.**
