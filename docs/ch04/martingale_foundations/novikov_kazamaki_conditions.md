# Novikov and Kazamaki Conditions

When does a stochastic exponential define a valid probability measure? The **Novikov condition** and **Kazamaki condition** provide sufficient conditions for the stochastic exponential to be a true martingale, ensuring that measure changes are well-defined.

---

## The Problem

Consider the stochastic exponential:

$$
Z_t = \mathcal{E}\left(-\int_0^t \theta_s\,dW_s\right) = \exp\left(-\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
$$

We want to use $Z_T$ as a Radon-Nikodym derivative:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T
$$

**For this to be valid**, we need:

1. $Z_t \geq 0$ (automatically satisfied by exponential)
2. $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$ (normalization)

The second condition is **not automatic** for local martingales!

---

## When Stochastic Exponentials Fail

### The Issue

$Z_t$ is always a **local martingale** (by Itô's lemma, $dZ_t = -\theta_t Z_t\,dW_t$).

But local martingales can have $\mathbb{E}[Z_T] < Z_0 = 1$ due to:
- Mass escaping to infinity
- Explosion of integrals

### Example of Failure

Consider $\theta_t = W_t$ (the integrand depends on the Brownian motion itself).

The stochastic exponential:

$$
Z_t = \exp\left(-\int_0^t W_s\,dW_s - \frac{1}{2}\int_0^t W_s^2\,ds\right)
$$

may fail to satisfy $\mathbb{E}[Z_T] = 1$ for large $T$.

---

## Novikov's Condition

**Theorem (Novikov, 1972)**: If

$$
\boxed{
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
}
$$

then $Z_t = \mathcal{E}\left(-\int_0^t \theta_s\,dW_s\right)$ is a **true martingale** on $[0,T]$, and in particular:

$$
\mathbb{E}^{\mathbb{P}}[Z_T] = 1
$$

### Interpretation

Novikov's condition requires that the "energy" $\int_0^T \theta_s^2\,ds$ has exponential moments. This prevents the integrand from being too large too often.

### Sufficient but Not Necessary

Novikov's condition is **sufficient** but **not necessary**. There exist martingale exponentials that violate Novikov but are still true martingales.

---

## Kazamaki's Condition

**Theorem (Kazamaki, 1977)**: If

$$
\boxed{
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s\,dW_s\right)\right] < \infty \quad \text{for all } T
}
$$

then $Z_t = \mathcal{E}\left(-\int_0^t \theta_s\,dW_s\right)$ is a true martingale.

### Comparison with Novikov

| Condition | Requires |
|-----------|----------|
| Novikov | $\mathbb{E}\left[e^{\frac{1}{2}\int \theta^2\,ds}\right] < \infty$ |
| Kazamaki | $\mathbb{E}\left[e^{\frac{1}{2}\int \theta\,dW}\right] < \infty$ |

Kazamaki is **weaker** (less restrictive) than Novikov:

$$
\text{Novikov satisfied} \Rightarrow \text{Kazamaki satisfied}
$$

but not conversely.

---

## Practical Verification

### Case 1: Deterministic $\theta$

If $\theta_t = \theta(t)$ is deterministic:

$$
\int_0^T \theta(t)^2\,dt < \infty \Rightarrow \text{Novikov satisfied}
$$

The condition is essentially that $\theta \in L^2[0,T]$.

### Case 2: Bounded $\theta$

If $|\theta_t| \leq M$ almost surely:

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] \leq e^{M^2 T/2} < \infty
$$

Novikov is satisfied.

### Case 3: Black-Scholes

The market price of risk $\theta = (\mu - r)/\sigma$ is constant.

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\theta^2 T\right)\right] = e^{\theta^2 T/2} < \infty \quad \checkmark
$$

Novikov is satisfied for any finite $T$.

### Case 4: Stochastic Volatility

In Heston model, $\theta_t = (\mu - r)/\sqrt{V_t}$ where $V_t$ is stochastic.

Verification requires checking that $V_t$ doesn't approach zero too fast.

---

## Proof Idea for Novikov

**Step 1**: Show that under Novikov's condition:

$$
\mathbb{E}\left[\sup_{t \leq T} Z_t\right] < \infty
$$

**Step 2**: Use the supermartingale convergence theorem to conclude that $Z_t$ is a true martingale.

**Key inequality**: For any local martingale $M$ with $M_0 = 0$:

$$
\mathbb{E}\left[\sup_{t \leq T} \mathcal{E}(M)_t\right] \leq \mathbb{E}\left[\mathcal{E}(M)_T^{1/2}\right]^2
$$

Under Novikov, the right side is finite.

---

## Applications in Finance

### Girsanov Theorem

For Girsanov to produce a valid measure change, we need Novikov (or Kazamaki):

$$
Z_T = \exp\left(-\int_0^T \theta_s\,dW_s - \frac{1}{2}\int_0^T \theta_s^2\,ds\right)
$$

must satisfy $\mathbb{E}[Z_T] = 1$.

### Risk-Neutral Measure Construction

The risk-neutral measure $\mathbb{Q}$ exists if and only if:
1. A market price of risk $\theta$ exists (no-arbitrage)
2. The stochastic exponential is a true martingale (Novikov/Kazamaki)

### Bubbles and Strict Local Martingales

When Novikov fails, $Z_t$ may be a **strict local martingale** with $\mathbb{E}[Z_T] < 1$.

In finance, this corresponds to **asset price bubbles**: the discounted price is a local martingale but not a true martingale.

---

## Beyond Brownian Motion

For general semimartingales, similar conditions exist:

### Doléans-Dade Exponential

For a local martingale $M$:

$$
\mathcal{E}(M)_t = \exp\left(M_t - \frac{1}{2}\langle M \rangle_t\right)
$$

### General Novikov

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right] < \infty \Rightarrow \mathcal{E}(M) \text{ is a true martingale}
$$

---

## Summary

| Condition | Statement | Use |
|-----------|-----------|-----|
| **Novikov** | $\mathbb{E}[e^{\frac{1}{2}\int_0^T \theta^2\,ds}] < \infty$ | Sufficient for $\mathbb{E}[Z_T] = 1$ |
| **Kazamaki** | $\mathbb{E}[e^{\frac{1}{2}\int_0^T \theta\,dW}] < \infty$ | Weaker sufficient condition |

$$
\boxed{
\text{Novikov} \Rightarrow \text{Kazamaki} \Rightarrow Z_t \text{ is a true martingale} \Rightarrow \mathbb{E}[Z_T] = 1
}
$$

**These conditions ensure that Girsanov's theorem produces a valid probability measure, which is essential for the construction of risk-neutral measures in finance.**
