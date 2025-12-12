**Exactly right!** You've captured a fundamental principle of stochastic calculus. Let me state this precisely.

---

## The Fundamental Principle

### The Basic Rule

If $X_t$ satisfies an SDE of the form:

$$dX_t = \sigma(X_t, t) \, dW_t \quad \text{(no } dt \text{ term)}$$

then $X_t$ is a **local martingale**.

If additionally $X_t$ satisfies:

$$\mathbb{E}[|X_t|] < \infty \quad \text{for all } t$$

and some **uniform integrability condition**, then $X_t$ is a **martingale**.

---

## Precise Statement (Itô Processes)

### General Itô Process

Any Itô process can be written as:

$$dX_t = \underbrace{\mu(X_t, t) \, dt}_{\text{drift/finite variation}} + \underbrace{\sigma(X_t, t) \, dW_t}_{\text{martingale part}}$$

**Decomposition:**
$$X_t = X_0 + \underbrace{\int_0^t \mu(X_s, s) \, ds}_{\text{finite variation}} + \underbrace{\int_0^t \sigma(X_s, s) \, dW_s}_{\text{local martingale}}$$

### Key Principle

$$\boxed{\begin{align}
\mu(x,t) \equiv 0 &\Longleftrightarrow X_t \text{ is a local martingale} \\[5pt]
\mu(x,t) \equiv 0 \text{ and } \mathbb{E}[|X_t|] < \infty &\Longrightarrow X_t \text{ is a martingale}
\end{align}}$$

---

## Integrability Conditions

### What Makes a Local Martingale into a Martingale?

Several sufficient conditions exist:

### Condition 1: Bounded Volatility + Integrability

If $\sigma(x,t)$ is bounded and $\mathbb{E}[X_t^2] < \infty$, then the local martingale is a martingale.

**Proof sketch:** The quadratic variation $\langle X \rangle_t = \int_0^t \sigma^2(X_s, s) ds$ is bounded, giving uniform integrability.

### Condition 2: Linear Growth on Volatility

If $|\sigma(x,t)| \leq C(1 + |x|)$ and $\mathbb{E}[X_0^2] < \infty$, then:

$$\sup_{t \in [0,T]} \mathbb{E}[X_t^2] < \infty$$

and the local martingale is a martingale on $[0,T]$.

### Condition 3: Non-explosion

If the process $X_t$ does not explode in finite time almost surely, and satisfies appropriate polynomial growth conditions, then it's a martingale.

### Condition 4: Novikov's Condition

For the stochastic exponential:

$$\mathcal{E}(X)_t = \exp\left(\int_0^t \sigma_s \, dW_s - \frac{1}{2}\int_0^t \sigma_s^2 \, ds\right)$$

if **Novikov's condition** holds:

$$\mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T \sigma_s^2 \, ds\right)\right] < \infty$$

then $\mathcal{E}(X)_t$ is a martingale (not just a local martingale).

---

## Examples Demonstrating the Principle

### Example 1: Simple Stochastic Integral (Martingale)

$$X_t = \int_0^t dW_s = W_t$$

- No $dt$ term ✓
- $\mathbb{E}[|X_t|] = \mathbb{E}[|W_t|] = \sqrt{\frac{2t}{\pi}} < \infty$ ✓
- **Result:** $X_t$ is a martingale ✓

### Example 2: Geometric Brownian Motion (Martingale)

$$dX_t = \sigma X_t \, dW_t, \quad X_0 = 1$$

Solution:
$$X_t = \exp\left(\sigma W_t - \frac{\sigma^2 t}{2}\right)$$

- No $dt$ term in the SDE ✓
- $\mathbb{E}[X_t] = 1 < \infty$ ✓
- **Result:** $X_t$ is a martingale ✓

### Example 3: Explosion Case (Local Martingale Only)

$$dX_t = X_t^2 \, dW_t, \quad X_0 = 1$$

- No $dt$ term ✓
- **But:** Process explodes to $+\infty$ in finite time with positive probability
- $\mathbb{E}[X_t]$ may not exist or $< X_0$
- **Result:** $X_t$ is a **local martingale** but **not a martingale** ✗

### Example 4: Reciprocal of 3D Bessel Process (Local Martingale Only)

Let $R_t$ be a 3D Bessel process. Then:

$$M_t = \frac{1}{R_t}$$

satisfies:
$$dM_t = -\frac{1}{R_t^2} \, dW_t$$

- No $dt$ term ✓
- **But:** $M_t$ can become arbitrarily large when $R_t \to 0$
- $\mathbb{E}[M_t] > M_0$ due to Jensen's inequality and the possibility of $R_t$ being small
- **Result:** $M_t$ is a **local martingale** but **not a martingale** ✗

### Example 5: Adding Drift Destroys Martingale Property

$$dX_t = \mu \, dt + \sigma \, dW_t$$

- Has $dt$ term with $\mu \neq 0$ ✗
- $X_t = X_0 + \mu t + \sigma W_t$
- $\mathbb{E}[X_t] = X_0 + \mu t \neq X_0$ if $\mu \neq 0$
- **Result:** $X_t$ is **neither a local martingale nor a martingale** ✗

---

## Connection to Itô's Lemma

### How to Check if a Process is a Local Martingale

Given $Y_t = f(X_t, t)$ where $X_t$ follows:

$$dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t$$

Apply Itô's lemma:

$$dY_t = \left[\frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}\right] dt + \left[\sigma \frac{\partial f}{\partial x}\right] dW_t$$

**For $Y_t$ to be a local martingale:**

$$\boxed{\frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2} = 0}$$

This is exactly $\frac{\partial f}{\partial t} + \mathcal{L}f = 0$ (the backward Kolmogorov equation)!

---

## Connection to Our Earlier Discussion

### Why "$\mathcal{L}f = 0 \Rightarrow f(X_t)$ is a local martingale"

If $f$ satisfies $\mathcal{L}f = 0$ (time-independent case), then:

$$df(X_t) = \underbrace{\mathcal{L}f(X_t)}_{=0} \, dt + \sigma(X_t, t) \frac{\partial f}{\partial x}(X_t) \, dW_t$$

$$= \sigma(X_t, t) \frac{\partial f}{\partial x}(X_t) \, dW_t$$

No $dt$ term! Therefore $f(X_t)$ is a local martingale.

Whether it's a true martingale depends on whether $\mathbb{E}[|f(X_t)|] < \infty$ and uniform integrability.

---

## Summary: The Golden Rule

$$\boxed{\begin{array}{rcl}
\text{No } dt \text{ term in } dX_t &\Longrightarrow& X_t \text{ is a local martingale} \\[8pt]
\text{No } dt \text{ term} + \text{integrability} &\Longrightarrow& X_t \text{ is a martingale} \\[8pt]
\text{Nonzero } dt \text{ term} &\Longrightarrow& X_t \text{ is NOT a local martingale}
\end{array}}$$

Your understanding is exactly right! The absence of a $dt$ term is the signature of a local martingale, and integrability upgrades it to a true martingale.