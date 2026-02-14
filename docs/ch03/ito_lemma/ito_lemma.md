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

### Step 1: Second-Order Taylor Expansion

Start with a second-order Taylor expansion at $(t_{k-1}, B_{t_{k-1}})$:

$$
f(t_k, B_{t_k}) - f(t_{k-1}, B_{t_{k-1}}) = f_t(t_{k-1}, B_{t_{k-1}})\Delta t + f_x(t_{k-1}, B_{t_{k-1}})\Delta B_t$$
$$
+ \frac{1}{2}f_{tt}(t_{k-1}, B_{t_{k-1}})(\Delta t)^2 + \frac{1}{2}f_{xx}(t_{k-1}, B_{t_{k-1}})(\Delta B_t)^2$$
$$
+ f_{tx}(t_{k-1}, B_{t_{k-1}})\Delta B_t \,\Delta t + \cdots
$$

### Step 2: Apply Itô Multiplication Rules

The crucial difference from ordinary calculus is **which terms survive**:

$$
\begin{array}{|c|c|}
\hline
\text{Term} & \text{Order and Fate} \\
\hline
f_t \,dt & O(dt) \,\Rightarrow\, \text{SURVIVES} \\
f_x \,dB_t & O(\sqrt{dt}) \,\Rightarrow\, \text{SURVIVES} \\
\frac{1}{2}f_{tt}(dt)^2 & O(dt^2) \,\Rightarrow\, \text{VANISHES} \\
\frac{1}{2}f_{xx}(dB_t)^2 & O(dt) \,\Rightarrow\, \text{SURVIVES} \quad \text{(KEY!)} \\
f_{tx}\,dt\,dB_t & O(dt^{3/2}) \,\Rightarrow\, \text{VANISHES} \\
\hline
\end{array}
$$

**The key insight:** $(dB_t)^2 = dt$ is the fundamental rule distinguishing stochastic from ordinary calculus.

### Step 3: Telescoping Sum

Summing over a partition $0 = t_0 < t_1 < \cdots < t_n = t$:

$$
f(t, B_t) - f(0, B_0) = \sum_{k=1}^n [f(t_k, B_{t_k}) - f(t_{k-1}, B_{t_{k-1}})]
$$

Each five-term expansion contributes:

$$
\sum_{k=1}^n f_t(\cdot)\,\Delta t \to \int_0^t f_t(s, B_s)\,ds
$$

$$
\sum_{k=1}^n f_x(\cdot)\,\Delta B_t \to \int_0^t f_x(s, B_s)\,dB_s
$$

$$
\sum_{k=1}^n \frac{1}{2}f_{xx}(\cdot)(\Delta B_t)^2 = \sum_{k=1}^n \frac{1}{2}f_{xx}(\cdot)\,\Delta t \to \int_0^t \frac{1}{2}f_{xx}(s, B_s)\,ds
$$

### Step 4: Rigorous Limit

Taking the limit as $\|\Delta\| \to 0$:

- The first integral is a standard Riemann integral
- The second integral is an Itô stochastic integral (well-defined by $\mathcal{F}_t$-measurability)
- The third integral is a standard integral (from quadratic variation)

**Quadratic Variation Property:** For Brownian motion, $[B]_t = t$, which ensures the cross-variation $dt \cdot dB_t = 0$ exactly. This is why the third-order term vanishes while the second-order diffusion term survives.

**Convergence Result:** Under $C^{1,2}$ smoothness of $f$, the sum converges to the integral form of Itô's lemma.

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

## Step-by-Step Application Strategy

When applying Itô's lemma to $df(t, X_t)$ where $dX_t = \mu_t\,dt + \sigma_t\,dB_t$:

**Step 1:** Compute all first and second partial derivatives of $f$:
$$f_t, \quad f_x, \quad f_{xx}$$

**Step 2:** Compute $(dX_t)^2$ symbolically using Itô rules:
$$
(dX_t)^2 = (\mu_t\,dt + \sigma_t\,dB_t)^2 = \sigma_t^2\,(dB_t)^2 = \sigma_t^2\,dt
$$

**Step 3:** Substitute into Itô's lemma formula:
$$
df = \left(f_t + \mu_t f_x + \frac{1}{2}\sigma_t^2 f_{xx}\right)dt + \sigma_t f_x\,dB_t
$$

**Step 4:** Integrate if needed, or use as differential equation.

## Common Mistakes to Avoid

1. **Forgetting the correction term**: $d(B_t^2) = 2B_t\,dB_t + dt$, NOT just $2B_t\,dB_t$

2. **Using ordinary chain rule**: $d(e^{B_t}) \neq e^{B_t}\,dB_t$

3. **Wrong order of operations**: Always compute $(dX_t)^2$ first, then substitute

4. **Confusing Itô and Stratonovich**: The correction term is specific to Itô calculus

5. **Ignoring time derivatives**: If $f = f(t, X_t)$ (time-dependent), don't omit $f_t$

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
