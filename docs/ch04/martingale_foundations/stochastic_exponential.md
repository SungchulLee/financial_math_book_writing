# The Stochastic Exponential

The **stochastic exponential** (or **Doléans-Dade exponential**) is the stochastic analogue of the ordinary exponential function. It is the fundamental tool for constructing Radon–Nikodym derivatives in measure change, and therefore central to Girsanov's theorem and risk-neutral pricing.

!!! info "Prerequisites"
    This section assumes familiarity with:
    
    - [Itô's Lemma](../../ch03/ito_lemma/ito_lemma.md)
    - [Quadratic Variation](../../ch03/ito_integral/quadratic_variation.md)
    - [Local Martingales](local_martingale.md)

---

## Definition

### SDE Definition

Given a continuous semimartingale $X_t$, the **stochastic exponential** $\mathcal{E}(X)_t$ is defined as the unique solution to:

$$
\boxed{
d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t, \quad \mathcal{E}(X)_0 = 1
}
$$

Note that the initial condition is always $\mathcal{E}(X)_0 = 1$, regardless of the value of $X_0$.

### Explicit Formula

For continuous semimartingales:

$$
\boxed{
\mathcal{E}(X)_t = \exp\left(X_t - X_0 - \frac{1}{2}\langle X \rangle_t\right)
}
$$

where $\langle X \rangle_t$ is the **quadratic variation** of $X$.

When $X_0 = 0$ (the most common case in applications), this simplifies to:

$$
\mathcal{E}(X)_t = \exp\left(X_t - \frac{1}{2}\langle X \rangle_t\right)
$$

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

In ordinary calculus: $e^{x(t)} = \exp\left(\int_0^t dx(s)\right) = \exp(x(t) - x(0))$

In stochastic calculus: $\mathcal{E}(X)_t = \exp\left(X_t - X_0 - \frac{1}{2}\langle X \rangle_t\right)$

The term $-\frac{1}{2}\langle X \rangle_t$ is the **Itô correction** arising from quadratic variation. This correction is essential: without it, the exponential would have a drift term and fail to be a local martingale.

---

## Derivation via Itô's Lemma

**Goal**: Verify that $Z_t = \exp(X_t - X_0 - \frac{1}{2}\langle X \rangle_t)$ satisfies $dZ_t = Z_t\,dX_t$.

### Setup

Let $X_t$ be a continuous local martingale with $dX_t = \sigma_t\,dW_t$. Then $d\langle X \rangle_t = \sigma_t^2\,dt$.

Define $Z_t = \exp(X_t - X_0 - \frac{1}{2}\langle X \rangle_t)$.

### Apply Itô's Lemma

Using the Itô formula with $f(x) = e^x$ and the process $Y_t = X_t - X_0 - \frac{1}{2}\langle X \rangle_t$:

$$
dZ_t = Z_t\,dY_t + \frac{1}{2}Z_t\,(dY_t)^2
$$

Now compute $dY_t$ and $(dY_t)^2$:

$$
dY_t = dX_t - \frac{1}{2}d\langle X \rangle_t = \sigma_t\,dW_t - \frac{1}{2}\sigma_t^2\,dt
$$

$$
(dY_t)^2 = (\sigma_t\,dW_t)^2 = \sigma_t^2\,dt = d\langle X \rangle_t
$$

(using the Itô multiplication rules: $(dW_t)^2 = dt$, $dt \cdot dW_t = 0$, $(dt)^2 = 0$)

### Substitute

$$
dZ_t = Z_t\left(\sigma_t\,dW_t - \frac{1}{2}\sigma_t^2\,dt\right) + \frac{1}{2}Z_t \cdot \sigma_t^2\,dt
$$

$$
= Z_t\,\sigma_t\,dW_t - \frac{1}{2}Z_t\,\sigma_t^2\,dt + \frac{1}{2}Z_t\,\sigma_t^2\,dt
$$

$$
= Z_t\,\sigma_t\,dW_t = Z_t\,dX_t
$$

The correction terms **cancel exactly**, leaving no drift. $\square$

---

## Key Properties

### Property 1: Positivity

$$
\mathcal{E}(X)_t > 0 \quad \text{for all } t \geq 0
$$

The stochastic exponential is always strictly positive (exponential of a real number).

### Property 2: Local Martingale Property

If $X_t$ is a continuous local martingale, then $\mathcal{E}(X)_t$ is also a **local martingale**.

**Proof**: From $d\mathcal{E}(X)_t = \mathcal{E}(X)_t\,dX_t$, we see there is no $dt$ term—the SDE has zero drift. $\square$

### Property 3: Multiplication Rule

For two continuous semimartingales $X$ and $Y$:

$$
\boxed{\mathcal{E}(X)_t \cdot \mathcal{E}(Y)_t = \mathcal{E}(X + Y + \langle X, Y \rangle)_t}
$$

Compare to the ordinary rule: $e^x \cdot e^y = e^{x+y}$. The stochastic version has an extra covariation term.

**Proof**: Let $Z_t = \mathcal{E}(X)_t$ and $W_t = \mathcal{E}(Y)_t$. By the Itô product rule:

$$
d(ZW) = Z\,dW + W\,dZ + d\langle Z, W \rangle
$$

Since $dZ = Z\,dX$ and $dW = W\,dY$:

$$
d(ZW) = ZW\,dY + ZW\,dX + ZW\,d\langle X, Y \rangle = ZW\,(dX + dY + d\langle X, Y \rangle)
$$

This shows $ZW = \mathcal{E}(X)\mathcal{E}(Y)$ satisfies the SDE for $\mathcal{E}(X + Y + \langle X, Y \rangle)$. $\square$

### Property 4: Reciprocal

The reciprocal of a stochastic exponential is:

$$
\boxed{\frac{1}{\mathcal{E}(X)_t} = \exp\left(-X_t + X_0 + \frac{1}{2}\langle X \rangle_t\right)}
$$

**Important**: The reciprocal is generally **not** a stochastic exponential itself. We have:

$$
\frac{1}{\mathcal{E}(X)_t} = \mathcal{E}(-X)_t \cdot \exp(\langle X \rangle_t)
$$

This follows from direct computation:

$$
\mathcal{E}(-X)_t = \exp\left(-X_t + X_0 - \frac{1}{2}\langle X \rangle_t\right)
$$

so

$$
\mathcal{E}(-X)_t \cdot \exp(\langle X \rangle_t) = \exp\left(-X_t + X_0 + \frac{1}{2}\langle X \rangle_t\right) = \frac{1}{\mathcal{E}(X)_t}
$$

### Property 5: Unit Expectation (Under Conditions)

If $\mathcal{E}(X)$ is a **true martingale** (not just a local martingale):

$$
\mathbb{E}[\mathcal{E}(X)_t] = \mathcal{E}(X)_0 = 1
$$

This property is essential for measure changes but requires verification via Novikov or Kazamaki conditions.

---

## Special Cases

### Case 1: $X_t = \sigma W_t$ (Constant Volatility)

For $\sigma \in \mathbb{R}$ constant:

$$
\mathcal{E}(\sigma W)_t = \exp\left(\sigma W_t - \frac{\sigma^2 t}{2}\right)
$$

This is the fundamental **exponential martingale**. It satisfies $\mathbb{E}[\mathcal{E}(\sigma W)_t] = 1$ for all $t$ (Novikov is trivially satisfied since $\sigma$ is constant).

### Case 2: $X_t = \int_0^t \sigma_s\,dW_s$ (Stochastic Integrand)

$$
\mathcal{E}(X)_t = \exp\left(\int_0^t \sigma_s\,dW_s - \frac{1}{2}\int_0^t \sigma_s^2\,ds\right)
$$

This is the general form used in Girsanov's theorem. Whether it's a true martingale depends on $\sigma$—see [Novikov and Kazamaki Conditions](novikov_kazamaki_conditions.md).

### Case 3: Geometric Brownian Motion

The solution to $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ with $S_0 > 0$ is:

$$
S_t = S_0 \exp\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)
$$

This can be written as:

$$
S_t = S_0\, e^{\mu t} \cdot \mathcal{E}(\sigma W)_t
$$

The term $\mu - \frac{\sigma^2}{2}$ is the **drift-adjusted growth rate**—the Itô correction $-\frac{\sigma^2}{2}$ appears naturally.

---

## Connection to Girsanov's Theorem

The stochastic exponential is the **Radon–Nikodym derivative** for measure change.

### Measure Change Setup

To change from measure $\mathbb{P}$ to measure $\mathbb{Q}$:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T
$$

where the **density process** is:

$$
Z_t = \mathcal{E}\left(\int_0^\cdot \theta_s\,dW_s\right)_t = \exp\left(\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
$$

Here $\theta_t$ is the **Girsanov kernel** (market price of risk in finance).

### Girsanov's Result

Under $\mathbb{Q}$, the process:

$$
\tilde{W}_t = W_t - \int_0^t \theta_s\,ds
$$

is a standard Brownian motion.

**Validity**: For this measure change to be valid (i.e., $\mathbb{Q}$ is a probability measure equivalent to $\mathbb{P}$), we need $Z_t$ to be a **true martingale** with $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$. This is guaranteed by Novikov's or Kazamaki's condition.

See [Girsanov's Theorem](../girsanov/girsanov_theorem.md) for the complete treatment.

---

## Why the Correction Term Matters

### Without Correction: $e^{W_t}$ Has Drift

If we naively define $Z_t = e^{W_t}$, then by Itô's lemma:

$$
dZ_t = e^{W_t}dW_t + \frac{1}{2}e^{W_t}dt = Z_t\,dW_t + \frac{1}{2}Z_t\,dt
$$

This has a **positive drift term** $\frac{1}{2}Z_t\,dt$. The process $e^{W_t}$ is a **submartingale**, not a martingale:

$$
\mathbb{E}[e^{W_t}] = e^{t/2} > 1 = e^{W_0}
$$

### With Correction: $\mathcal{E}(W)_t$ Is a Martingale

$$
\mathcal{E}(W)_t = e^{W_t - t/2}
$$

Then:

$$
d\mathcal{E}(W)_t = \mathcal{E}(W)_t\,dW_t
$$

**No drift term**—this is a true martingale with $\mathbb{E}[\mathcal{E}(W)_t] = 1$.

The correction $-\frac{1}{2}\langle X \rangle_t$ precisely removes the drift introduced by Itô's lemma.

---

## When Is $\mathcal{E}(X)$ a True Martingale?

The stochastic exponential of a local martingale is always a local martingale, but may be a **strict local martingale** (local martingale that is not a true martingale).

### Sufficient Conditions

**Novikov's Condition**: If

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\langle X \rangle_T\right)\right] < \infty
$$

then $\mathcal{E}(X)$ is a true martingale on $[0,T]$.

**Kazamaki's Condition** (weaker): If $\mathcal{E}(X/2)$ is a submartingale, then $\mathcal{E}(X)$ is a true martingale.

For details and proofs, see [Novikov and Kazamaki Conditions](novikov_kazamaki_conditions.md).

### When Conditions Fail

If neither condition holds, $\mathcal{E}(X)$ may satisfy $\mathbb{E}[\mathcal{E}(X)_T] < 1$. In finance, this corresponds to **asset price bubbles**. See [Local Martingales](local_martingale.md) for examples.

---

## Extension to Discontinuous Processes

For a general semimartingale $X$ with jumps, the **Doléans-Dade exponential** has the more complex form:

$$
\mathcal{E}(X)_t = \exp\left(X_t^c - X_0 - \frac{1}{2}\langle X^c \rangle_t\right) \prod_{0 < s \leq t}(1 + \Delta X_s)\,e^{-\Delta X_s}
$$

where:

- $X^c$ is the continuous martingale part of $X$
- $\Delta X_s = X_s - X_{s-}$ are the jumps

For $\mathcal{E}(X)_t$ to remain positive, we need $\Delta X_s > -1$ for all $s$ (jumps cannot be too negative).

---

## Applications in Finance

### 1. Risk-Neutral Measure Construction

The density process for the risk-neutral measure $\mathbb{Q}$:

$$
Z_t = \mathcal{E}\left(-\int_0^\cdot \frac{\mu - r}{\sigma}\,dW_s\right)_t
$$

where $(\mu - r)/\sigma$ is the **market price of risk** (Sharpe ratio).

### 2. Change of Numéraire

When changing from numéraire $M$ to numéraire $N$:

$$
\frac{d\mathbb{Q}^N}{d\mathbb{Q}^M}\bigg|_{\mathcal{F}_T} = \frac{N_T/N_0}{M_T/M_0}
$$

This ratio involves stochastic exponentials of the volatility difference between the two numéraires.

### 3. Forward Measure

The $T$-forward measure uses the zero-coupon bond $P(t,T)$ as numéraire. The density involves stochastic exponentials of bond volatilities.

See [Forward Measure](../risk-neutral_measure/forward_measure.md) for details.

---

## Summary

$$
\boxed{
\mathcal{E}(X)_t = \exp\left(X_t - X_0 - \frac{1}{2}\langle X \rangle_t\right)
}
$$

| Property | Statement |
|----------|-----------|
| **Definition** | Unique solution to $d\mathcal{E} = \mathcal{E}\,dX$, $\mathcal{E}_0 = 1$ |
| **Positivity** | $\mathcal{E}(X)_t > 0$ always |
| **Local martingale** | If $X$ is a continuous local martingale, so is $\mathcal{E}(X)$ |
| **Multiplication** | $\mathcal{E}(X)\mathcal{E}(Y) = \mathcal{E}(X + Y + \langle X,Y\rangle)$ |
| **True martingale** | Requires Novikov or Kazamaki condition |
| **Finance application** | Radon–Nikodym derivative for measure change |

!!! summary "Key Takeaway"
    The stochastic exponential is the "correct" way to exponentiate stochastic processes, accounting for the Itô correction term $-\frac{1}{2}\langle X \rangle_t$. This correction removes the drift that would otherwise arise, making $\mathcal{E}(X)$ a local martingale. The stochastic exponential is essential for all measure-change arguments in mathematical finance.
