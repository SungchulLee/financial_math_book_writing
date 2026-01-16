# The Stochastic Exponential

The **stochastic exponential** (or **Doléans-Dade exponential**) is the stochastic analogue of the ordinary exponential function. It is the fundamental tool for constructing Radon-Nikodym derivatives in measure change, and therefore central to Girsanov's theorem and risk-neutral pricing.

---

## Definition

### SDE Definition

Given a continuous semimartingale $X_t$ with $X_0 = 0$, the **stochastic exponential** $\mathcal{E}(X)_t$ is defined as the unique solution to:

$$
\boxed{
d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t, \quad \mathcal{E}(X)_0 = 1
}
$$

### Explicit Formula

$$
\boxed{
\mathcal{E}(X)_t = \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right)
}
$$

where $\langle X \rangle_t$ is the **quadratic variation** of $X$.

---

## Why "Stochastic Exponential"?

### Analogy with Ordinary Exponential

For a deterministic function $x(t)$, the ordinary exponential $e^{x(t)}$ satisfies:

$$
\frac{d}{dt}e^{x(t)} = e^{x(t)} \cdot \frac{dx(t)}{dt}
$$

In differential form: $d(e^{x}) = e^x\,dx$.

### The Stochastic Version

The stochastic exponential satisfies the same multiplicative structure:

$$
d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t
$$

### The Crucial Difference

In ordinary calculus: $e^{x(t)} = e^{\int_0^t dx(s)}$

In stochastic calculus: $\mathcal{E}(X)_t = \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right)$

The term $-\frac{1}{2}\langle X \rangle_t$ is the **Itô correction** arising from quadratic variation.

---

## Derivation via Itô's Lemma

**Goal**: Verify that $Y_t = \exp(X_t - \frac{1}{2}\langle X \rangle_t)$ satisfies $dY_t = Y_t\,dX_t$.

### Step 1: Apply Itô's Lemma

Write $Y_t = f(X_t, \langle X \rangle_t)$ where $f(x,q) = e^{x - q/2}$.

For a local martingale $X_t$ with $dX_t = \sigma_t\,dW_t$:

$$
dY_t = \frac{\partial f}{\partial x}dX_t + \frac{\partial f}{\partial q}d\langle X \rangle_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}d\langle X \rangle_t
$$

### Step 2: Compute Derivatives

$$
\frac{\partial f}{\partial x} = e^{x-q/2}, \quad \frac{\partial f}{\partial q} = -\frac{1}{2}e^{x-q/2}, \quad \frac{\partial^2 f}{\partial x^2} = e^{x-q/2}
$$

### Step 3: Substitute

$$
dY_t = Y_t\,dX_t - \frac{1}{2}Y_t\,d\langle X \rangle_t + \frac{1}{2}Y_t\,d\langle X \rangle_t
$$

$$
= Y_t\,dX_t
$$

The correction terms **cancel exactly**. ✓

---

## Key Properties

### Property 1: Positivity

$$
\mathcal{E}(X)_t > 0 \quad \text{for all } t
$$

The stochastic exponential is always strictly positive.

### Property 2: Local Martingale

If $X_t$ is a local martingale, then $\mathcal{E}(X)_t$ is also a **local martingale**.

**Proof**: $d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t$ has no $dt$ term. ✓

### Property 3: Multiplication Rule

For two semimartingales $X$ and $Y$:

$$
\mathcal{E}(X)_t \cdot \mathcal{E}(Y)_t = \mathcal{E}(X + Y + \langle X, Y \rangle)_t
$$

Compare to the ordinary rule: $e^x \cdot e^y = e^{x+y}$.

### Property 4: Reciprocal

$$
\frac{1}{\mathcal{E}(X)_t} = \mathcal{E}(-X + \langle X \rangle)_t
$$

### Property 5: Unit Expectation (under conditions)

If $\mathcal{E}(X)$ is a true martingale:

$$
\mathbb{E}[\mathcal{E}(X)_t] = \mathcal{E}(X)_0 = 1
$$

---

## Special Cases

### Case 1: $X_t = \sigma W_t$ (deterministic volatility)

$$
\mathcal{E}(\sigma W)_t = \exp\left(\sigma W_t - \frac{\sigma^2 t}{2}\right)
$$

This is the fundamental exponential martingale.

### Case 2: $X_t = \int_0^t \sigma_s\,dW_s$ (stochastic integrand)

$$
\mathcal{E}(X)_t = \exp\left(\int_0^t \sigma_s\,dW_s - \frac{1}{2}\int_0^t \sigma_s^2\,ds\right)
$$

### Case 3: Geometric Brownian Motion

The solution to $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ is:

$$
S_t = S_0 \exp\left(\mu t + \sigma W_t - \frac{\sigma^2 t}{2}\right) = S_0 e^{\mu t} \cdot \mathcal{E}(\sigma W)_t
$$

---

## Connection to Girsanov's Theorem

The stochastic exponential is the **Radon-Nikodym derivative** for measure change.

### Measure Change Setup

To change from measure $\mathbb{P}$ to measure $\mathbb{Q}$:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T
$$

where:

$$
Z_t = \mathcal{E}\left(-\int_0^t \theta_s\,dW_s\right) = \exp\left(-\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
$$

### Girsanov's Result

Under $\mathbb{Q}$:

$$
\tilde{W}_t = W_t + \int_0^t \theta_s\,ds
$$

is a Brownian motion.

---

## Why the Correction Term Matters

### Without Correction

If we naively define $Z_t = e^{X_t}$ for $X_t = W_t$:

$$
Z_t = e^{W_t}
$$

By Itô's lemma:

$$
dZ_t = e^{W_t}dW_t + \frac{1}{2}e^{W_t}dt = Z_t\,dW_t + \frac{1}{2}Z_t\,dt
$$

This has a **drift term**—$e^{W_t}$ is NOT a local martingale!

### With Correction

$$
\mathcal{E}(W)_t = e^{W_t - t/2}
$$

Then:

$$
d\mathcal{E}(W)_t = \mathcal{E}(W)_t\,dW_t
$$

**No drift term**—this IS a local martingale (and a true martingale).

The correction $-\frac{1}{2}\langle X \rangle_t$ precisely removes the drift introduced by Itô's lemma.

---

## When is $\mathcal{E}(X)$ a True Martingale?

The stochastic exponential is always a local martingale but may be a **strict local martingale**.

### Novikov's Condition

If:

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
$$

then $\mathcal{E}\left(\int_0^t \theta_s\,dW_s\right)$ is a **true martingale**.

### Kazamaki's Condition (weaker)

If:

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s\,dW_s\right)\right] < \infty
$$

then $\mathcal{E}\left(\int_0^t \theta_s\,dW_s\right)$ is a true martingale.

---

## Applications in Finance

### 1. Risk-Neutral Measure Construction

The density process for the risk-neutral measure:

$$
Z_t = \mathcal{E}\left(-\int_0^t \frac{\mu_s - r}{\sigma_s}\,dW_s\right)
$$

### 2. Change of Numéraire

Changing from numéraire $M$ to $N$:

$$
\frac{d\mathbb{Q}^N}{d\mathbb{Q}^M} = \frac{N_T/N_0}{M_T/M_0}
$$

### 3. Forward Measure

The density for the $T$-forward measure involves stochastic exponentials of bond volatilities.

---

## Summary

$$
\boxed{
\mathcal{E}(X)_t = \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right)
}
$$

| Property | Statement |
|----------|-----------|
| Definition | Solves $d\mathcal{E} = \mathcal{E}\,dX$ |
| Positivity | $\mathcal{E}(X)_t > 0$ always |
| Local martingale | If $X$ is local martingale, so is $\mathcal{E}(X)$ |
| True martingale | Requires Novikov or Kazamaki condition |
| Use in finance | Radon-Nikodym derivative for measure change |

**The stochastic exponential is the "correct" way to exponentiate stochastic processes, accounting for the Itô correction term, and is essential for all measure-change arguments in finance.**
