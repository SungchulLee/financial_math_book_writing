# Novikov and Kazamaki Conditions

When does a stochastic exponential define a valid probability measure? The **Novikov condition** and **Kazamaki condition** provide sufficient conditions for the stochastic exponential to be a true martingale, ensuring that measure changes are well-defined.

!!! info "Prerequisites"
    This section assumes familiarity with:
    
    - [Local Martingales](local_martingale.md)
    - [Stochastic Exponential](stochastic_exponential.md)
    - [Girsanov's Theorem](../girsanov/girsanov_theorem.md)

---

## The Problem

Consider the stochastic exponential of a continuous local martingale $M_t = \int_0^t \theta_s\,dW_s$:

$$
Z_t = \mathcal{E}(M)_t = \exp\left(M_t - \frac{1}{2}\langle M \rangle_t\right) = \exp\left(\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
$$

We want to use $Z_T$ as a Radon–Nikodym derivative:

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

By Itô's formula, $Z_t$ satisfies $dZ_t = Z_t \theta_t\,dW_t$, which shows $Z_t$ is always a **local martingale**.

But local martingales can have $\mathbb{E}[Z_T] < Z_0 = 1$ due to:

- Mass escaping to infinity
- The integrand $\theta$ being too large too often

### Example of Failure

Consider $\theta_t = \frac{c}{\sqrt{T-t}}$ for $t < T$, where $c > 0$ is a constant. Then:

$$
\int_0^T \theta_s^2\,ds = \int_0^T \frac{c^2}{T-s}\,ds = +\infty
$$

The quadratic variation explodes, and Novikov's condition fails. More precisely, for any $\epsilon > 0$:

$$
\int_0^{T-\epsilon} \theta_s^2\,ds = c^2 \log\left(\frac{T}{\epsilon}\right) \to \infty \quad \text{as } \epsilon \to 0
$$

The stochastic exponential $Z_t$ converges to 0 as $t \to T$, and $\mathbb{E}[Z_T] < 1$.

**Intuition**: The integrand $\theta$ blows up near the terminal time, causing the local martingale to "leak mass to infinity."

---

## Novikov's Condition

**Theorem (Novikov, 1972)**: Let $M_t = \int_0^t \theta_s\,dW_s$ be a continuous local martingale. If

$$
\boxed{
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right] = \mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
}
$$

then $Z_t = \mathcal{E}(M)_t$ is a **true martingale** on $[0,T]$, and in particular:

$$
\mathbb{E}^{\mathbb{P}}[Z_T] = 1
$$

### Interpretation

Novikov's condition requires that the "energy" $\langle M \rangle_T = \int_0^T \theta_s^2\,ds$ has finite exponential moments. This prevents the integrand from being too large too often.

### Key Properties

1. **Sufficient but not necessary**: There exist true martingale exponentials that violate Novikov.

2. **Sign-independent**: Only $\theta^2$ appears, so the sign of $\theta$ is irrelevant.

3. **Deterministic case simplifies**: If $\theta_t = \theta(t)$ is deterministic, Novikov reduces to $\int_0^T \theta(t)^2\,dt < \infty$.

---

## Proof Sketch for Novikov's Condition

The proof proceeds in several steps. We follow the approach in Revuz–Yor (Chapter VIII) and Karatzas–Shreve (Section 3.5).

**Step 1: Exponential martingale inequality**

For any continuous local martingale $M$ with $M_0 = 0$ and any $\lambda > 0$:

$$
\mathbb{P}\left(\sup_{t \leq T} M_t \geq \lambda\right) \leq e^{-\lambda} \mathbb{E}\left[\exp(M_T)\mathbf{1}_{\{\sup_{t \leq T} M_t \geq \lambda\}}\right]
$$

**Step 2: Control the maximum**

Using the inequality from Step 1 and properties of the stochastic exponential, one can show:

$$
\mathbb{E}\left[\sup_{t \leq T} \mathcal{E}(M)_t\right] \leq 2\,\mathbb{E}\left[\mathcal{E}(M)_T^{1/2} \cdot \exp\left(\frac{1}{4}\langle M \rangle_T\right)\right]
$$

**Step 3: Apply Cauchy–Schwarz**

By Cauchy–Schwarz:

$$
\mathbb{E}\left[\mathcal{E}(M)_T^{1/2} \cdot \exp\left(\frac{1}{4}\langle M \rangle_T\right)\right] \leq \mathbb{E}\left[\mathcal{E}(M)_T\right]^{1/2} \cdot \mathbb{E}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right]^{1/2}
$$

**Step 4: Bootstrap**

Under Novikov's condition, the second factor is finite. A careful stopping time argument shows that the local martingale $\mathcal{E}(M)$ is dominated by an integrable random variable, hence is a true martingale.

**Reference**: For the complete proof, see Karatzas–Shreve, *Brownian Motion and Stochastic Calculus*, Proposition 3.5.12, or Revuz–Yor, *Continuous Martingales and Brownian Motion*, Proposition VIII.1.15.

---

## Kazamaki's Condition

Kazamaki's condition is weaker than Novikov's and involves the local martingale $M$ itself rather than its quadratic variation.

**Theorem (Kazamaki, 1977)**: Let $M_t = \int_0^t \theta_s\,dW_s$ be a continuous local martingale with $M_0 = 0$. If

$$
\boxed{
\mathcal{E}\left(\frac{1}{2}M\right)_t = \exp\left(\frac{1}{2}M_t - \frac{1}{8}\langle M \rangle_t\right) \text{ is a submartingale}
}
$$

then $\mathcal{E}(M)_t$ is a true martingale.

### Equivalent Formulations

The submartingale condition is equivalent to:

$$
\sup_{t \leq T} \mathbb{E}\left[\exp\left(\frac{1}{2}M_t\right)\right] < \infty
$$

A sufficient (but slightly stronger) condition often stated in practice:

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}M_T\right)\right] < \infty
$$

### Why Kazamaki Is Weaker

**Proposition**: Novikov's condition implies Kazamaki's condition.

**Proof**: Assume Novikov holds: $\mathbb{E}[\exp(\frac{1}{2}\langle M \rangle_T)] < \infty$.

The process $\exp(\frac{1}{2}M_t)$ can be written as:

$$
\exp\left(\frac{1}{2}M_t\right) = \mathcal{E}\left(\frac{1}{2}M\right)_t \cdot \exp\left(\frac{1}{8}\langle M \rangle_t\right)
$$

Taking expectations and using that $\mathcal{E}(\frac{1}{2}M)$ is a non-negative local martingale (hence a supermartingale):

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}M_t\right)\right] \leq \mathbb{E}\left[\exp\left(\frac{1}{8}\langle M \rangle_t\right)\right] \leq \mathbb{E}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right]^{1/4} < \infty
$$

where we used Jensen's inequality in the last step. Thus Kazamaki's condition is satisfied. $\square$

The converse is **false**: there exist processes satisfying Kazamaki but not Novikov.

---

## Comparison of Conditions

| Condition | Requires | Strength |
|-----------|----------|----------|
| **Novikov** | $\mathbb{E}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right] < \infty$ | Stronger |
| **Kazamaki** | $\sup_{t \leq T}\mathbb{E}\left[\exp\left(\frac{1}{2}M_t\right)\right] < \infty$ | Weaker |

$$
\text{Novikov satisfied} \Rightarrow \text{Kazamaki satisfied} \Rightarrow \mathcal{E}(M) \text{ is a true martingale}
$$

**When to use which**:

- **Novikov**: Easier to verify when $\theta$ has known bounds or growth conditions
- **Kazamaki**: Useful when direct control of $\langle M \rangle$ is difficult but $M$ itself is well-behaved

---

## Practical Verification

### Case 1: Deterministic $\theta$

If $\theta_t = \theta(t)$ is deterministic:

$$
\int_0^T \theta(t)^2\,dt < \infty \Rightarrow \text{Novikov satisfied}
$$

The exponential of a constant is finite, so the condition reduces to $\theta \in L^2[0,T]$.

### Case 2: Bounded $\theta$

If $|\theta_t| \leq M$ almost surely for all $t \in [0,T]$:

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] \leq \exp\left(\frac{M^2 T}{2}\right) < \infty
$$

Novikov is satisfied.

### Case 3: Black–Scholes Model

The market price of risk $\theta = (\mu - r)/\sigma$ is constant.

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\theta^2 T\right)\right] = \exp\left(\frac{\theta^2 T}{2}\right) < \infty \quad \checkmark
$$

Novikov is satisfied for any finite $T$.

### Case 4: Heston Stochastic Volatility Model

In the Heston model, the variance process $V_t$ follows:

$$
dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
$$

The market price of risk for the stock is $\theta_t = (\mu - r)/\sqrt{V_t}$, so:

$$
\int_0^T \theta_s^2\,ds = (\mu - r)^2 \int_0^T \frac{1}{V_s}\,ds
$$

**Novikov verification requires**: $\mathbb{E}\left[\exp\left(\frac{(\mu-r)^2}{2}\int_0^T V_s^{-1}\,ds\right)\right] < \infty$

This holds when the **Feller condition** is satisfied:

$$
2\kappa\bar{V} \geq \xi^2
$$

The Feller condition ensures $V_t > 0$ for all $t$ (the process never hits zero), which prevents $\int_0^T V_s^{-1}\,ds$ from exploding. When Feller is violated, $V_t$ can hit zero, and verification becomes more delicate—one must check whether the time spent near zero is short enough.

**Reference**: For detailed analysis, see Andersen and Piterbarg, *Interest Rate Modeling*, Vol. 1, Chapter 8.

---

## Applications in Finance

### Girsanov's Theorem

For Girsanov's theorem to produce a valid measure change, we need the Radon–Nikodym derivative:

$$
Z_T = \exp\left(\int_0^T \theta_s\,dW_s - \frac{1}{2}\int_0^T \theta_s^2\,ds\right)
$$

to satisfy $\mathbb{E}[Z_T] = 1$. Novikov or Kazamaki provides this guarantee.

### Risk-Neutral Measure Construction

The risk-neutral measure $\mathbb{Q}$ exists and is equivalent to $\mathbb{P}$ if:

1. A market price of risk $\theta$ exists (completeness/no-arbitrage)
2. The stochastic exponential $\mathcal{E}(\int \theta\,dW)$ is a true martingale (Novikov/Kazamaki)

When condition 2 fails, $\mathbb{Q}$ may still exist but could fail to be equivalent to $\mathbb{P}$, or the market may admit arbitrage of the first kind.

### Bubbles and Strict Local Martingales

When both Novikov and Kazamaki fail, $Z_t$ may be a **strict local martingale** with $\mathbb{E}[Z_T] < 1$.

In finance, this corresponds to **asset price bubbles**: the discounted price process is a local martingale but not a true martingale under the pricing measure. See [Local Martingales](local_martingale.md) for the connection between strict local martingales and bubbles.

---

## Extension to General Continuous Local Martingales

For a general continuous local martingale $M$ (not necessarily an Itô integral), the **Doléans-Dade exponential** is:

$$
\mathcal{E}(M)_t = \exp\left(M_t - \frac{1}{2}\langle M \rangle_t\right)
$$

**General Novikov Condition**: If $\mathbb{E}[\exp(\frac{1}{2}\langle M \rangle_T)] < \infty$, then $\mathcal{E}(M)$ is a true martingale on $[0,T]$.

**General Kazamaki Condition**: If $\mathcal{E}(\frac{1}{2}M)$ is a submartingale, then $\mathcal{E}(M)$ is a true martingale.

For discontinuous local martingales (with jumps), the Doléans-Dade exponential has the more complex form:

$$
\mathcal{E}(M)_t = \exp\left(M_t - \frac{1}{2}\langle M^c \rangle_t\right) \prod_{0 < s \leq t}(1 + \Delta M_s)e^{-\Delta M_s}
$$

where $M^c$ is the continuous part and $\Delta M_s = M_s - M_{s-}$ are the jumps. Conditions for this to be a true martingale are more involved.

---

## Summary

| Condition | Statement | Verifies |
|-----------|-----------|----------|
| **Novikov** | $\mathbb{E}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right] < \infty$ | $\mathcal{E}(M)$ is a true martingale |
| **Kazamaki** | $\mathcal{E}\left(\frac{1}{2}M\right)$ is a submartingale | $\mathcal{E}(M)$ is a true martingale |

$$
\boxed{
\text{Novikov} \Rightarrow \text{Kazamaki} \Rightarrow \mathcal{E}(M) \text{ is a true martingale} \Rightarrow \mathbb{E}[\mathcal{E}(M)_T] = 1
}
$$

!!! summary "Key Takeaways"
    1. **Both conditions are sufficient but not necessary** for the stochastic exponential to be a true martingale.
    
    2. **Novikov is easier to verify** when the quadratic variation $\langle M \rangle$ is controlled.
    
    3. **Kazamaki is weaker** and can apply in cases where Novikov fails.
    
    4. **In finance**, these conditions ensure Girsanov's theorem produces valid measure changes, which is essential for risk-neutral pricing.
    
    5. **Failure of both conditions** may indicate the presence of asset price bubbles (strict local martingales).

---

## References

1. Novikov, A.A. (1972). "On an identity for stochastic integrals." *Theory of Probability and Its Applications*, 17(4), 717–720.

2. Kazamaki, N. (1977). "On a problem of Girsanov." *Tôhoku Mathematical Journal*, 29(4), 597–600.

3. Karatzas, I. and Shreve, S.E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer. Section 3.5.

4. Revuz, D. and Yor, M. (1999). *Continuous Martingales and Brownian Motion*, 3rd ed. Springer. Chapter VIII.
