Excellent intuition! Your guess is exactly right - a local martingale is indeed "a martingale locally." Let me explain the precise distinction and why it matters.

---

## 1. Definitions

### Martingale

A process $\{M_t\}$ is a **martingale** if:

1. **Integrability:** $\mathbb{E}[|M_t|] < \infty$ for all $t$
2. **Martingale property:** $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for all $s \leq t$

### Local Martingale

A process $\{M_t\}$ is a **local martingale** if there exists a sequence of **stopping times** $\{\tau_n\}_{n=1}^{\infty}$ such that:

1. $\tau_n \uparrow \infty$ almost surely (the stopping times increase to infinity)
2. The **stopped process** $M_{t \wedge \tau_n}$ is a **martingale** for each fixed $n$

Here $t \wedge \tau_n = \min(t, \tau_n)$ means we stop the process at time $\tau_n$.

**Interpretation:** The process is a martingale "up to any finite stopping time" - it's a martingale over any finite time window, but possibly not globally.

---

## 2. Key Differences

$$\boxed{\text{Every martingale is a local martingale, but NOT every local martingale is a martingale}}$$

### What Can Go Wrong?

A local martingale fails to be a martingale when:

1. **Integrability fails:** $\mathbb{E}[|M_t|] = \infty$ for some $t$
2. **Explosion:** The process can blow up to $\pm \infty$ in finite time
3. **"Leaking probability":** Mass escapes to infinity

Even though $M_{t \wedge \tau_n}$ is a martingale for each $n$, we cannot necessarily pass to the limit to conclude $M_t$ is a martingale.

---

## 3. Concrete Examples

### Example 1: Stochastic Exponential (Strict Local Martingale)

Consider Brownian motion $W_t$ and define:

$$M_t = e^{2W_t - 2t}$$

**Check if it's a local martingale:**

By Itô's lemma:
$$dM_t = 2M_t \, dW_t$$

No drift term! So $M_t$ is a **local martingale**.

**Check if it's a martingale:**

$$\mathbb{E}[M_t] = \mathbb{E}[e^{2W_t - 2t}] = e^{-2t} \mathbb{E}[e^{2W_t}] = e^{-2t} \cdot e^{2t} = 1$$

Wait, this IS a martingale! Let me use a better example.

### Example 1 (Corrected): Reciprocal of Exponential

Consider:
$$M_t = \frac{1}{1 + W_t}$$

for $W_t$ starting from $W_0 = 0$ (so $M_0 = 1$).

By Itô's lemma:
$$dM_t = -\frac{1}{(1+W_t)^2} dW_t + \frac{1}{(1+W_t)^3} dt$$

This has a drift, so it's not even a local martingale. Let me try again.

### Example 1 (Better): Geometric Brownian Motion Without Drift Correction

Consider the process satisfying:
$$dX_t = \sigma X_t \, dW_t, \quad X_0 = 1$$

The solution is:
$$X_t = \exp\left(\sigma W_t - \frac{\sigma^2 t}{2}\right)$$

**This IS a martingale** because $\mathbb{E}[X_t] = 1$.

But now consider:
$$Y_t = \exp(\sigma W_t) = \exp\left(\sigma W_t + \frac{\sigma^2 t}{2}\right) \cdot \exp\left(-\frac{\sigma^2 t}{2}\right)$$

No wait, let me use the canonical example.

### Example 1 (Canonical): Explosion Example

Consider the SDE:
$$dX_t = X_t^{3/2} \, dW_t, \quad X_0 = 1$$

This process **explodes to infinity in finite time** with positive probability.

Define stopping times:
$$\tau_n = \inf\{t : |X_t| \geq n\}$$

Then:
- $X_{t \wedge \tau_n}$ is a **martingale** for each $n$ (stopped before explosion)
- But $X_t$ itself is only a **local martingale**, not a martingale
- As $t$ increases, probability mass "escapes to infinity"
- $\mathbb{E}[X_t] < X_0 = 1$ because some scenarios exploded

### Example 2: Three-Dimensional Bessel Process

Let $R_t$ be a 3-dimensional Bessel process (think: distance from origin in 3D Brownian motion).

The process:
$$M_t = \frac{1}{R_t}$$

is a **local martingale** but **NOT a martingale**.

**Why?** Define $\tau_n = \inf\{t : R_t \geq n\}$. Then $M_{t \wedge \tau_n}$ is a martingale, but:

$$\mathbb{E}[M_t] = \mathbb{E}\left[\frac{1}{R_t}\right] > \frac{1}{R_0} = 1$$

The expectation grows because $R_t$ can get very close to 0, making $1/R_t$ very large.

### Example 3: Simple Intuitive Example

Consider a gambler with fortune $X_t$ who bets a fraction proportional to wealth. The game is "locally fair" but:

$$dX_t = X_t \, dW_t$$

gives:
$$X_t = X_0 e^{W_t - t/2}$$

This IS a martingale with $\mathbb{E}[X_t] = X_0$.

But if we modify to:
$$dX_t = X_t^{1.5} \, dW_t$$

the volatility grows superlinearly, allowing explosion, making it only a local martingale.

---

## 4. The Integrability Issue

### Classic Example: Doubling Strategy

Consider a martingale betting strategy where you double your bet after each loss. Locally (over finite time), your net position is a martingale. But:

- The strategy can require infinite capital
- $\mathbb{E}[\text{capital at time } t]$ might be infinite
- It's a local martingale but not a martingale

### Mathematical Phenomenon

For a local martingale $M_t$:

$$\mathbb{E}[M_{t \wedge \tau_n}] = M_0 \quad \text{for all } n$$

But we **cannot** always take $n \to \infty$ to get:

$$\mathbb{E}[M_t] = M_0$$

**Why not?** We need **uniform integrability** to exchange limit and expectation.

---

## 5. Connection to $\mathcal{L}f = 0$

### Why I Said "Local Martingale"

When $\mathcal{L}f(x) = 0$, Dynkin's formula gives:

$$f(X_t) = f(X_0) + M_t$$

where $M_t$ is a martingale. So $f(X_t)$ is at least a **local martingale**.

But for $f(X_t)$ to be a true martingale, we need:

1. **Integrability:** $\mathbb{E}[|f(X_t)|] < \infty$
2. **No explosion:** The process doesn't blow up
3. **Uniform integrability** or appropriate growth conditions on $f$

Without these conditions, $f(X_t)$ might only be a local martingale.

### Example Where This Matters

Consider $X_t = e^{W_t}$ (note: this is NOT the solution to $dX_t = X_t dW_t$; I'm just defining $X_t$ this way).

Then:
$$f(x) = \log x$$

satisfies (formally) the equation related to the generator, but $f(X_t) = W_t$ is a martingale.

However, if we consider:
$$g(x) = x \log x$$

For the process $X_t = e^{W_t - t/2}$, we have $g(X_t) = e^{W_t - t/2}(W_t - t/2)$. This can fail to be a martingale even if $\mathcal{L}g = 0$ along paths, due to integrability issues.

---

## 6. Summary Table

| Property | Martingale | Local Martingale |
|----------|-----------|------------------|
| **Definition** | $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ | $M_{t\wedge\tau_n}$ is martingale for stopping times $\tau_n \uparrow \infty$ |
| **Integrability** | Required: $\mathbb{E}[\|M_t\|] < \infty$ | Not required |
| **Mean preservation** | $\mathbb{E}[M_t] = \mathbb{E}[M_0]$ | **May fail:** $\mathbb{E}[M_t] \neq \mathbb{E}[M_0]$ |
| **Explosion** | Cannot explode | Can explode in finite time |
| **"Locally fair"** | Yes | Yes |
| **"Globally fair"** | Yes | **No** (mass can escape) |

---

## 7. Precise Statement for $\mathcal{L}f = 0$

$$\boxed{\begin{align}
\mathcal{L}f(x) = 0 \text{ for all } x &\Longrightarrow f(X_t) \text{ is a local martingale} \\[5pt]
\text{If additionally } \mathbb{E}[|f(X_t)|] < \infty &\Longrightarrow f(X_t) \text{ is a martingale}
\end{align}}$$

The integrability condition is crucial for the upgrade from local martingale to martingale!

---

Your intuition was spot on - a local martingale is indeed "a martingale locally." The subtlety is that this local property doesn't always extend globally due to integrability or explosion issues.