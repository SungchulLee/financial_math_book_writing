# Local Martingales

A **local martingale** is a process that behaves like a martingale "locally"—when stopped at appropriate times—but may fail to be a true martingale globally. This distinction is crucial in continuous-time finance, where many natural price processes are local martingales but not martingales.

---

## Definitions

### Martingale

A process $\{M_t\}_{t \geq 0}$ is a **martingale** with respect to filtration $\{\mathcal{F}_t\}$ if:

1. **Adaptedness**: $M_t$ is $\mathcal{F}_t$-measurable for all $t$
2. **Integrability**: $\mathbb{E}[|M_t|] < \infty$ for all $t$
3. **Martingale property**: $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for all $s \leq t$

### Local Martingale

A process $\{M_t\}_{t \geq 0}$ is a **local martingale** if there exists a sequence of stopping times $\{\tau_n\}_{n=1}^{\infty}$ such that:

1. $\tau_n \uparrow \infty$ almost surely (stopping times increase to infinity)
2. The **stopped process** $M_{t \wedge \tau_n}$ is a martingale for each $n$

The sequence $\{\tau_n\}$ is called a **localizing sequence**.

---

## The Key Relationship

$$
\boxed{
\text{Every martingale is a local martingale, but NOT every local martingale is a martingale}
}
$$

A local martingale that is not a true martingale is called a **strict local martingale**.

---

## What Can Go Wrong?

A local martingale fails to be a martingale when:

### 1. Integrability Failure

$\mathbb{E}[|M_t|] = \infty$ for some $t$

### 2. Explosion

The process can blow up to $\pm\infty$ in finite time

### 3. Mass Leakage

Probability mass "escapes to infinity"—the expectation $\mathbb{E}[M_t]$ can decrease over time

---

## Canonical Examples

### Example 1: Itô Integrals

Any Itô integral of the form:

$$
M_t = \int_0^t \sigma_s\,dW_s
$$

is a **local martingale** (assuming $\sigma$ is adapted and locally square-integrable).

It is a **true martingale** if additionally:

$$
\mathbb{E}\left[\int_0^T \sigma_s^2\,ds\right] < \infty
$$

### Example 2: Stochastic Exponential

The stochastic exponential:

$$
Z_t = \exp\left(W_t - \frac{t}{2}\right) = \mathcal{E}(W)_t
$$

satisfies $dZ_t = Z_t\,dW_t$ and is a **true martingale** with $\mathbb{E}[Z_t] = 1$.

### Example 3: Reciprocal of 3D Bessel Process

Let $R_t$ be the 3-dimensional Bessel process (distance from origin of 3D Brownian motion).

The process:

$$
M_t = \frac{1}{R_t}
$$

is a **strict local martingale** (local martingale but NOT a true martingale).

**Why?** As $R_t$ can get arbitrarily close to 0, the expectation $\mathbb{E}[1/R_t]$ grows unboundedly, violating integrability.

### Example 4: Explosion Example

Consider the SDE:

$$
dX_t = X_t^{3/2}\,dW_t, \quad X_0 = 1
$$

This process can **explode to infinity** in finite time.

Define stopping times $\tau_n = \inf\{t : X_t \geq n\}$.

- $X_{t \wedge \tau_n}$ is a martingale for each $n$
- But $X_t$ itself is only a local martingale
- $\mathbb{E}[X_t] < X_0 = 1$ because probability mass escapes

---

## Mathematical Characterization

### The Supermartingale Property

**Theorem**: Every non-negative local martingale is a **supermartingale**:

$$
\mathbb{E}[M_t \mid \mathcal{F}_s] \leq M_s \quad \text{for } s \leq t
$$

**Consequence**: For non-negative local martingales:

$$
\mathbb{E}[M_t] \leq \mathbb{E}[M_0]
$$

with equality if and only if $M$ is a true martingale.

### The Fatou Property

For a non-negative local martingale:

$$
\mathbb{E}[M_{t \wedge \tau_n}] = M_0 \quad \text{for all } n
$$

But taking $n \to \infty$, Fatou's lemma only gives:

$$
\mathbb{E}[M_t] \leq \liminf_{n \to \infty} \mathbb{E}[M_{t \wedge \tau_n}] = M_0
$$

Strict inequality is possible!

---

## Sufficient Conditions for True Martingale

A local martingale $M$ is a true martingale if any of the following hold:

### 1. Bounded

$$
|M_t| \leq C \quad \text{almost surely for all } t
$$

### 2. Dominated

$$
|M_t| \leq Y \quad \text{for some integrable } Y
$$

### 3. $L^p$ Bounded ($p > 1$)

$$
\sup_{t \leq T} \mathbb{E}[|M_t|^p] < \infty
$$

### 4. Square-Integrable Quadratic Variation

For continuous local martingales:

$$
\mathbb{E}[\langle M \rangle_T] < \infty \Rightarrow M \text{ is a true martingale}
$$

### 5. Novikov's Condition (for stochastic exponentials)

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right] < \infty \Rightarrow \mathcal{E}(M) \text{ is a true martingale}
$$

---

## Connection to Generators

If $X_t$ is a diffusion with generator $\mathcal{L}$ and $f \in C^2$, then:

$$
\mathcal{L}f(x) = 0 \quad \text{for all } x
$$

implies $f(X_t)$ is a **local martingale**.

For $f(X_t)$ to be a **true martingale**, we additionally need:
- Integrability: $\mathbb{E}[|f(X_t)|] < \infty$
- No explosion
- Appropriate growth conditions on $f$

---

## Financial Implications

### Discounted Asset Prices

In financial mathematics, discounted asset prices should be (local) martingales under the risk-neutral measure $\mathbb{Q}$.

### Strict Local Martingales and Bubbles

If the discounted price is a **strict local martingale** (not a true martingale):

$$
\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0
$$

This corresponds to a **financial bubble**—the price exceeds the "fundamental value" given by the expectation.

### Put-Call Parity Failure

In bubble models, put-call parity can fail because:

$$
C - P \neq S_0 - Ke^{-rT}
$$

when the stock price is a strict local martingale.

---

## Summary Table

| Property | Martingale | Local Martingale |
|----------|-----------|------------------|
| **Definition** | $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ | $M_{t\wedge\tau_n}$ is martingale |
| **Integrability** | Required: $\mathbb{E}[|M_t|] < \infty$ | Not required |
| **Mean preservation** | $\mathbb{E}[M_t] = \mathbb{E}[M_0]$ | May fail: $\mathbb{E}[M_t] \leq \mathbb{E}[M_0]$ |
| **Explosion** | Cannot explode | Can explode |
| **"Locally fair"** | Yes | Yes |
| **"Globally fair"** | Yes | Not necessarily |

---

## Key Takeaway

$$
\boxed{
\mathcal{L}f = 0 \Rightarrow f(X_t) \text{ is a local martingale}
}
$$

$$
\boxed{
\mathcal{L}f = 0 \text{ and integrability} \Rightarrow f(X_t) \text{ is a true martingale}
}
$$

**The distinction between local martingales and true martingales is essential for rigorous financial modeling, particularly when dealing with explosive processes or bubbles.**
