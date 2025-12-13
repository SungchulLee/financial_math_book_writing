Excellent question! The notation $\mathcal{E}(X)_t$ denotes the **stochastic exponential** (also called the **Doléans-Dade exponential**) of a process $X_t$. It's a fundamental object in stochastic calculus.

---

## 1. Definition of Stochastic Exponential

### For a Continuous Local Martingale

Given a continuous semimartingale $X_t$ (starting at $X_0 = 0$), the **stochastic exponential** $\mathcal{E}(X)_t$ is defined as the unique solution to:

$$\boxed{d\mathcal{E}(X)_t = \mathcal{E}(X)_t \, dX_t, \quad \mathcal{E}(X)_0 = 1}$$

### Explicit Formula

$$\boxed{\mathcal{E}(X)_t = \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right)}$$

where $\langle X \rangle_t$ is the **quadratic variation** of $X_t$.

---

## 2. Special Case: When $X_t$ is a Stochastic Integral

If $X_t = \int_0^t \sigma_s \, dW_s$ (a stochastic integral with respect to Brownian motion), then:

$$\langle X \rangle_t = \int_0^t \sigma_s^2 \, ds$$

and the stochastic exponential is:

$$\boxed{\mathcal{E}(X)_t = \exp\left(\int_0^t \sigma_s \, dW_s - \frac{1}{2}\int_0^t \sigma_s^2 \, ds\right)}$$

---

## 3. Why is it Called "Stochastic Exponential"?

### Analogy with Ordinary Exponential

For a deterministic function $x(t)$, the ordinary exponential $e^{x(t)}$ satisfies:

$$\frac{d}{dt}e^{x(t)} = e^{x(t)} \cdot \frac{dx(t)}{dt}$$

or in differential form:
$$d(e^{x(t)}) = e^{x(t)} \, dx(t)$$

The stochastic exponential $\mathcal{E}(X)_t$ is the **stochastic analogue**:

$$d\mathcal{E}(X)_t = \mathcal{E}(X)_t \, dX_t$$

### The Crucial Difference: The $-\frac{1}{2}\langle X \rangle_t$ Term

In the ordinary case:
$$\frac{d}{dt}e^{x(t)} = e^{x(t)} \Rightarrow e^{x(t)} = e^{\int_0^t dx(s)}$$

In the stochastic case, due to **Itô's correction term**:

$$\mathcal{E}(X)_t = \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right)$$

The $-\frac{1}{2}\langle X \rangle_t$ appears because of the second-order term in Itô's lemma!

---

## 4. Derivation Using Itô's Lemma

### Why the Formula Works

Let $Y_t = \exp(X_t - \frac{1}{2}\langle X \rangle_t)$. We want to show $dY_t = Y_t \, dX_t$.

**Step 1:** Write $Y_t = f(X_t, \langle X \rangle_t)$ where $f(x, q) = e^{x - q/2}$.

**Step 2:** Apply Itô's lemma (for processes with finite variation and stochastic parts):

If $X_t$ is a local martingale with $dX_t = \sigma_t \, dW_t$, then:

$$dY_t = \frac{\partial f}{\partial x} dX_t + \frac{\partial f}{\partial q} d\langle X \rangle_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2} d\langle X \rangle_t$$

**Step 3:** Calculate partial derivatives:

$$\frac{\partial f}{\partial x} = e^{x - q/2}, \quad \frac{\partial f}{\partial q} = -\frac{1}{2}e^{x - q/2}, \quad \frac{\partial^2 f}{\partial x^2} = e^{x - q/2}$$

**Step 4:** Substitute:

$$dY_t = Y_t \, dX_t - \frac{1}{2}Y_t \, d\langle X \rangle_t + \frac{1}{2}Y_t \, d\langle X \rangle_t$$

$$= Y_t \, dX_t$$

The two terms involving $d\langle X \rangle_t$ **cancel exactly**! ✓

---

## 5. Key Properties

### Property 1: No Drift Term

Since $d\mathcal{E}(X)_t = \mathcal{E}(X)_t \, dX_t$ and if $X_t$ is a local martingale (no $dt$ term), then:

$$\boxed{\mathcal{E}(X)_t \text{ is a local martingale}}$$

### Property 2: Positivity

$$\mathcal{E}(X)_t > 0 \quad \text{for all } t$$

The stochastic exponential is always strictly positive (unlike $X_t$ itself, which can be negative).

### Property 3: Multiplication Rule

$$\mathcal{E}(X)_t \cdot \mathcal{E}(Y)_t = \mathcal{E}(X + Y + \langle X, Y \rangle)_t$$

Compare to: $e^x \cdot e^y = e^{x+y}$ (no correction term in deterministic case).

### Property 4: Reciprocal

$$\frac{1}{\mathcal{E}(X)_t} = \mathcal{E}(-X - \langle X \rangle)_t$$

---

## 6. Examples

### Example 1: Geometric Brownian Motion

Consider:
$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

Rewrite as:
$$\frac{dS_t}{S_t} = \mu \, dt + \sigma \, dW_t$$

Integrating:
$$\log S_t - \log S_0 = \mu t + \sigma W_t + \text{(Itô correction)}$$

The solution is:
$$S_t = S_0 \exp\left(\mu t + \sigma W_t - \frac{\sigma^2 t}{2}\right)$$

$$= S_0 \exp(\mu t) \cdot \exp\left(\sigma W_t - \frac{\sigma^2 t}{2}\right)$$

$$= S_0 e^{\mu t} \cdot \mathcal{E}(\sigma W)_t$$

Here $X_t = \sigma W_t$, so $\langle X \rangle_t = \sigma^2 t$, giving:

$$\mathcal{E}(\sigma W)_t = \exp\left(\sigma W_t - \frac{\sigma^2 t}{2}\right)$$

### Example 2: Pure Stochastic Exponential

$$dM_t = M_t \, dW_t, \quad M_0 = 1$$

This is exactly $M_t = \mathcal{E}(W)_t$, so:

$$M_t = \exp\left(W_t - \frac{t}{2}\right)$$

**Check:** $\langle W \rangle_t = t$, so:

$$\mathcal{E}(W)_t = \exp\left(W_t - \frac{1}{2} \cdot t\right) = \exp\left(W_t - \frac{t}{2}\right)$$ ✓

### Example 3: Novikov's Condition Revisited

For $X_t = \int_0^t \sigma_s \, dW_s$, we have:

$$\mathcal{E}(X)_t = \exp\left(\int_0^t \sigma_s \, dW_s - \frac{1}{2}\int_0^t \sigma_s^2 \, ds\right)$$

**Novikov's condition** states: if

$$\mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T \sigma_s^2 \, ds\right)\right] < \infty$$

then $\mathcal{E}(X)_t$ is a **true martingale** (not just a local martingale).

---

## 7. Connection to Girsanov Theorem

The stochastic exponential is **central to change of measure** in stochastic calculus.

### Radon-Nikodym Derivative

If we want to change probability measure from $\mathbb{P}$ to $\mathbb{Q}$, the Radon-Nikodym derivative is often:

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = \mathcal{E}(X)_t$$

for some appropriate process $X_t$.

### Girsanov Theorem Application

Under $\mathbb{P}$: $W_t$ is a Brownian motion

Under $\mathbb{Q}$: $\tilde{W}_t = W_t - \int_0^t \theta_s \, ds$ is a Brownian motion

The likelihood ratio is:

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = \mathcal{E}\left(-\int_0^t \theta_s \, dW_s\right)_t = \exp\left(-\int_0^t \theta_s \, dW_s - \frac{1}{2}\int_0^t \theta_s^2 \, ds\right)$$

---

## 8. Why the $-\frac{1}{2}\langle X \rangle_t$ Term Matters

### Without the Correction

If we naively defined $Z_t = e^{X_t}$ for a stochastic integral $X_t = \int_0^t dW_s = W_t$:

$$Z_t = e^{W_t}$$

By Itô's lemma:

$$dZ_t = e^{W_t} dW_t + \frac{1}{2}e^{W_t} dt$$

This has a **drift term**! So $e^{W_t}$ is **not a local martingale**.

### With the Correction

$$\mathcal{E}(W)_t = e^{W_t - t/2}$$

Then:

$$d\mathcal{E}(W)_t = \mathcal{E}(W)_t \, dW_t$$

**No drift term!** So $\mathcal{E}(W)_t$ **is a local martingale** (and actually a true martingale).

The correction term $-\frac{1}{2}\langle X \rangle_t$ is precisely what's needed to remove the drift!

---

## 9. Summary

$$\boxed{\begin{align}
\mathcal{E}(X)_t &= \text{stochastic exponential of } X_t \\[5pt]
&= \text{solution to } d\mathcal{E}(X)_t = \mathcal{E}(X)_t \, dX_t \\[5pt]
&= \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right) \\[10pt]
\text{Key property:} & \quad \text{If } X_t \text{ is a local martingale,} \\
& \quad \text{then } \mathcal{E}(X)_t \text{ is also a local martingale}
\end{align}}$$

The stochastic exponential is the "correct" way to exponentiate stochastic processes, accounting for the Itô correction term!