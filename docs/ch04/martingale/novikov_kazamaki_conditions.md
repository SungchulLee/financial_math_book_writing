# Novikov and Kazamaki Conditions

This section provides the conditions guaranteeing that a [stochastic exponential](stochastic_exponential.md) is a true martingale, so that the Girsanov measure change produces a valid probability measure (see [Unifying Principle](unifying_principle.md)).

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

In short, this determines whether $\mathbb{Q}$ exists as a valid equivalent measure. We want to use $Z_T$ as a Radon–Nikodym derivative:

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

As a result, the stochastic exponential may fail to be a true martingale, and the candidate density process may **degenerate** (for example, by collapsing toward zero). In such cases, the measure change defined by $Z_T$ is not guaranteed to produce a valid equivalent probability measure.

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

**Sketch.** Using the identity $\exp(\frac{1}{2}M_t) = \mathcal{E}(\frac{1}{2}M)_t \cdot \exp(\frac{1}{8}\langle M \rangle_t)$ and applying Hölder-type estimates together with the supermartingale property of $\mathcal{E}(\frac{1}{2}M)$, one obtains uniform bounds on $\mathbb{E}[\exp(\frac{1}{2}M_t)]$ under Novikov's condition. A complete proof can be found in Revuz–Yor (Chapter VIII) or Karatzas–Shreve (Section 3.5). $\square$

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

### Case 1: Deterministic θ

If $\theta_t = \theta(t)$ is deterministic:

$$
\int_0^T \theta(t)^2\,dt < \infty \Rightarrow \text{Novikov satisfied}
$$

The exponential of a constant is finite, so the condition reduces to $\theta \in L^2[0,T]$.

### Case 2: Bounded θ

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

The **Feller condition** is:

$$
2\kappa\bar{V} \geq \xi^2
$$

When the Feller condition holds, the variance process remains strictly positive, which helps prevent divergence of $\int_0^T V_s^{-1}\,ds$. However, verifying Novikov's condition in this setting generally requires more detailed analysis beyond positivity alone. When Feller is violated, $V_t$ can hit zero, and verification becomes more delicate—one must check whether the time spent near zero is short enough.

**Reference**: For detailed analysis, see Andersen and Piterbarg, *Interest Rate Modeling*, Vol. 1, Chapter 8.

---

## Applications in Finance

### Girsanov's Theorem

For the [Girsanov measure change](stochastic_exponential.md#connection-to-girsanovs-theorem) to be valid, the density $Z_T = \mathcal{E}(M)_T$ must satisfy $\mathbb{E}[Z_T] = 1$. Novikov or Kazamaki provides this guarantee.

### Risk-Neutral Measure Construction

The risk-neutral measure $\mathbb{Q}$ exists and is equivalent to $\mathbb{P}$ when both a suitable market price of risk $\theta$ is specified and the stochastic exponential is a true martingale (Novikov/Kazamaki). When the latter fails, $\mathbb{Q}$ may fail to be equivalent to $\mathbb{P}$, or the market may admit arbitrage of the first kind.

### Bubbles and Strict Local Martingales

When both conditions fail, $Z_t$ may be a [strict local martingale](local_martingale.md#strict-local-martingales-and-financial-bubbles) with $\mathbb{E}[Z_T] < 1$, corresponding to asset price bubbles.

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

!!! abstract "Key Takeaways"
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

---

## Exercises

**Exercise 1.**
In the Black-Scholes model, the market price of risk is $\theta = (\mu - r)/\sigma$ with $\mu = 0.10$, $\sigma = 0.25$, and $r = 0.03$. Verify Novikov's condition explicitly for $T = 10$ and conclude that the Girsanov measure change is valid.

??? success "Solution to Exercise 1"
    With $\mu = 0.10$, $\sigma = 0.25$, and $r = 0.03$, the market price of risk is:

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.10 - 0.03}{0.25} = 0.28
    $$

    Since $\theta$ is constant, the Novikov condition becomes:

    $$
    \mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^{10} \theta^2\,ds\right)\right] = \exp\left(\frac{\theta^2 \cdot 10}{2}\right) = \exp\left(\frac{0.0784 \cdot 10}{2}\right) = \exp(0.392) \approx 1.480 < \infty
    $$

    The quantity inside the expectation is deterministic and finite, so Novikov's condition is trivially satisfied. Therefore $\mathcal{E}(-\theta W^{\mathbb{P}})_T$ is a true martingale with $\mathbb{E}[Z_T] = 1$, and the Girsanov measure change from $\mathbb{P}$ to $\mathbb{Q}$ is valid for $T = 10$.

---

**Exercise 2.**
Consider a deterministic but time-varying market price of risk $\theta(t) = \alpha e^{\beta t}$ with $\alpha > 0$ and $\beta > 0$. Compute $\int_0^T \theta(t)^2\,dt$ and determine for which values of $T$ the Novikov condition holds. What happens as $T \to \infty$?

??? success "Solution to Exercise 2"
    With $\theta(t) = \alpha e^{\beta t}$:

    $$
    \int_0^T \theta(t)^2\,dt = \int_0^T \alpha^2 e^{2\beta t}\,dt = \frac{\alpha^2}{2\beta}\left(e^{2\beta T} - 1\right)
    $$

    Since $\theta(t)$ is deterministic, the Novikov condition reduces to:

    $$
    \exp\left(\frac{1}{2}\int_0^T \theta(t)^2\,dt\right) = \exp\left(\frac{\alpha^2}{4\beta}(e^{2\beta T} - 1)\right) < \infty
    $$

    This is finite for **every finite $T$**, since the exponential of any finite number is finite. Thus Novikov's condition holds for all $T < \infty$.

    As $T \to \infty$: $\int_0^T \theta(t)^2\,dt \to \infty$ (exponential growth), so $\exp(\frac{1}{2}\int_0^\infty \theta(t)^2\,dt) = +\infty$. On any finite horizon, the Girsanov measure change is valid, but the condition does not extend to infinite horizon. The exponential growth of $\theta(t)$ means the market price of risk becomes arbitrarily large, which would require increasingly extreme probability reweighting.

---

**Exercise 3.**
Prove that Novikov's condition implies Kazamaki's condition. Specifically, show that if $\mathbb{E}[\exp(\frac{1}{2}\langle M \rangle_T)] < \infty$, then $\sup_{t \leq T}\mathbb{E}[\exp(\frac{1}{2}M_t)] < \infty$. (Hint: write $\exp(\frac{1}{2}M_t)$ in terms of $\mathcal{E}(\frac{1}{2}M)_t$ and $\exp(\frac{1}{8}\langle M \rangle_t)$, then use the supermartingale property.)

??? success "Solution to Exercise 3"
    Assume Novikov holds: $\mathbb{E}[\exp(\frac{1}{2}\langle M \rangle_T)] < \infty$. We want to show $\sup_{t \leq T}\mathbb{E}[\exp(\frac{1}{2}M_t)] < \infty$.

    Write:

    $$
    \exp\left(\frac{1}{2}M_t\right) = \mathcal{E}\left(\frac{1}{2}M\right)_t \cdot \exp\left(\frac{1}{8}\langle M \rangle_t\right)
    $$

    This follows from the definition of the stochastic exponential:

    $$
    \mathcal{E}\left(\frac{1}{2}M\right)_t = \exp\left(\frac{1}{2}M_t - \frac{1}{2}\cdot\frac{1}{4}\langle M \rangle_t\right) = \exp\left(\frac{1}{2}M_t - \frac{1}{8}\langle M \rangle_t\right)
    $$

    Now $\mathcal{E}(\frac{1}{2}M)$ is a non-negative local martingale, hence a supermartingale: $\mathbb{E}[\mathcal{E}(\frac{1}{2}M)_t] \leq \mathcal{E}(\frac{1}{2}M)_0 = 1$.

    Taking expectations using Cauchy–Schwarz:

    $$
    \mathbb{E}\left[\exp\left(\frac{1}{2}M_t\right)\right] = \mathbb{E}\left[\mathcal{E}\left(\frac{1}{2}M\right)_t \cdot \exp\left(\frac{1}{8}\langle M \rangle_t\right)\right]
    $$

    $$
    \leq \left(\mathbb{E}\left[\mathcal{E}\left(\frac{1}{2}M\right)_t^2\right]\right)^{1/2} \cdot \left(\mathbb{E}\left[\exp\left(\frac{1}{4}\langle M \rangle_t\right)\right]\right)^{1/2}
    $$

    Alternatively, a simpler bound: since $\mathcal{E}(\frac{1}{2}M)_t \leq 1$ is not generally true, we use Jensen's inequality more carefully. Since $\langle M \rangle_t \leq \langle M \rangle_T$ for $t \leq T$:

    $$
    \mathbb{E}\left[\exp\left(\frac{1}{2}M_t\right)\right] \leq \mathbb{E}\left[\exp\left(\frac{1}{8}\langle M \rangle_T\right)\right] \leq \mathbb{E}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right]^{1/4} < \infty
    $$

    where the last step uses Jensen's inequality with the convex function $x \mapsto x^4$ (or equivalently, $\frac{1}{8} \leq \frac{1}{2}$ combined with monotonicity of the exponential). The bound is uniform in $t \leq T$, so $\sup_{t \leq T}\mathbb{E}[\exp(\frac{1}{2}M_t)] < \infty$, which is Kazamaki's condition.

---

**Exercise 4.**
For the Heston model with $\theta_t = (\mu - r)/\sqrt{V_t}$, explain why Novikov's condition involves $\mathbb{E}[\exp(\frac{(\mu-r)^2}{2}\int_0^T V_s^{-1}\,ds)]$. State the Feller condition $2\kappa\bar{V} \geq \xi^2$ and explain its role in ensuring $V_t > 0$. Why does $V_t$ hitting zero cause the Novikov condition to potentially fail?

??? success "Solution to Exercise 4"
    In the Heston model, $\theta_t = (\mu - r)/\sqrt{V_t}$, so:

    $$
    \int_0^T \theta_s^2\,ds = \int_0^T \frac{(\mu-r)^2}{V_s}\,ds = (\mu-r)^2 \int_0^T \frac{ds}{V_s}
    $$

    Novikov's condition requires:

    $$
    \mathbb{E}\left[\exp\left(\frac{(\mu-r)^2}{2}\int_0^T V_s^{-1}\,ds\right)\right] < \infty
    $$

    The **Feller condition** $2\kappa\bar{V} \geq \xi^2$ ensures that the CIR process $V_t$ never reaches zero. Specifically, when Feller holds, $V_t > 0$ for all $t > 0$ a.s. (the boundary at zero is **entrance**, not accessible). This keeps $1/V_s$ bounded in a neighborhood of zero, preventing $\int_0^T V_s^{-1}\,ds$ from exploding.

    When Feller is violated ($2\kappa\bar{V} < \xi^2$), $V_t$ can hit zero. Near zero, $1/V_s$ diverges, and $\int_0^T V_s^{-1}\,ds$ may become infinite. If the process spends too much time near zero, the exponential moment in Novikov's condition blows up, and the stochastic exponential may fail to be a true martingale. This would invalidate the Girsanov measure change and potentially signal the presence of arbitrage or bubbles in the model.

---

**Exercise 5.**
Consider $\theta_t = c / \sqrt{T - t}$ for $t < T$ with $c > 0$. Show that $\int_0^T \theta_s^2\,ds$ diverges logarithmically. Despite this divergence, explain why the stochastic exponential $Z_t$ may still be well-defined as a local martingale, and identify the defect $\delta = 1 - \mathbb{E}[Z_T]$.

??? success "Solution to Exercise 5"
    With $\theta_t = c/\sqrt{T-t}$ for $t < T$:

    $$
    \int_0^T \theta_s^2\,ds = \int_0^T \frac{c^2}{T-s}\,ds = c^2\left[-\ln(T-s)\right]_0^T = c^2 \lim_{\epsilon \to 0^+}(\ln T - \ln \epsilon) = +\infty
    $$

    The integral diverges logarithmically: $\int_0^{T-\epsilon} \theta_s^2\,ds = c^2 \ln(T/\epsilon)$.

    Despite this, the stochastic exponential $Z_t = \exp(\int_0^t \theta_s\,dW_s - \frac{1}{2}\int_0^t \theta_s^2\,ds)$ is still well-defined as a local martingale for $t < T$, because $\int_0^t \theta_s^2\,ds < \infty$ for each $t < T$. The process $Z_t$ satisfies $dZ_t = Z_t \theta_t\,dW_t$ and is a non-negative local martingale, hence a supermartingale.

    As $t \to T$, the explosive growth of $\theta_t$ causes $Z_t \to 0$ a.s., leading to:

    $$
    \mathbb{E}[Z_T] < 1
    $$

    The defect $\delta = 1 - \mathbb{E}[Z_T] > 0$ represents the "mass" lost to infinity. The exact value depends on $c$ and the specific path structure, but $\delta > 0$ confirms that $Z$ is a strict local martingale and cannot serve as a valid Radon–Nikodym derivative for an equivalent measure.

---

**Exercise 6.**
Suppose $|\theta_t| \leq M$ almost surely for some constant $M > 0$ and all $t \in [0, T]$. Show that both the Novikov condition and the Kazamaki condition are satisfied. What is the upper bound on $\mathbb{E}[\exp(\frac{1}{2}\int_0^T \theta_s^2\,ds)]$ in terms of $M$ and $T$?

??? success "Solution to Exercise 6"
    If $|\theta_t| \leq M$ a.s. for all $t \in [0,T]$, then:

    $$
    \int_0^T \theta_s^2\,ds \leq M^2 T \quad \text{a.s.}
    $$

    **Novikov's condition**:

    $$
    \mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] \leq \exp\left(\frac{M^2 T}{2}\right) < \infty
    $$

    So Novikov is satisfied with upper bound $\exp(M^2 T / 2)$.

    **Kazamaki's condition**: Since Novikov implies Kazamaki (proved in Exercise 3), Kazamaki is automatically satisfied. Alternatively, direct verification: $M_t = \int_0^t \theta_s\,dW_s$ is a continuous martingale with $\langle M \rangle_t \leq M^2 t$, and:

    $$
    \sup_{t \leq T}\mathbb{E}\left[\exp\left(\frac{1}{2}M_t\right)\right] \leq \sup_{t \leq T}\exp\left(\frac{1}{8}M^2 t\right) \cdot 1 \leq \exp\left(\frac{M^2 T}{8}\right) < \infty
    $$

    (using the supermartingale bound from the proof that Novikov implies Kazamaki).

---

**Exercise 7.**
Construct a process $M_t$ for which Kazamaki's condition is satisfied but Novikov's condition fails. (Hint: consider a process where $M_t$ has controlled moments but $\langle M \rangle_T$ has heavy tails. You may describe the construction conceptually rather than giving an explicit formula.)

??? success "Solution to Exercise 7"
    **Construction** (conceptual): Let $\tau$ be a random time with $\mathbb{P}(\tau \leq T) = 1$ and define $\theta_t$ to be a process that is bounded for $t < \tau$ but has a carefully chosen blow-up at $t = \tau$.

    More concretely, consider $M_t = \int_0^t \theta_s\,dW_s$ where $\theta_s$ is chosen so that:

    - $\langle M \rangle_T = \int_0^T \theta_s^2\,ds$ has a **heavy-tailed** distribution (e.g., comparable to an exponential or Pareto random variable), so $\mathbb{E}[\exp(\frac{1}{2}\langle M \rangle_T)] = \infty$ — Novikov fails.

    - $M_T$ itself remains "controlled" enough that $\mathbb{E}[\exp(\frac{1}{2}M_T)] < \infty$ — Kazamaki holds.

    This is possible because $M_T$ has both positive and negative fluctuations (it is a martingale centered at zero), while $\langle M \rangle_T$ is always non-negative and monotone increasing. The quadratic variation accumulates without cancellation, while the martingale $M_T$ benefits from cancellations between positive and negative increments.

    A classical example from Kazamaki (1977): take $\theta_s$ to depend on $W$ itself in such a way that $\int_0^T \theta_s^2\,ds$ has moments growing faster than exponential, but $M_T = \int_0^T \theta_s\,dW_s$ has controlled exponential moments due to the "centering" effect of the stochastic integral. The separation arises precisely because $\langle M \rangle$ measures accumulated volatility (always additive), while $M$ itself benefits from martingale cancellations.

---

**Exercise 8.**
A candidate claims: "If $\int_0^T \theta_s^2\,ds < \infty$ almost surely, then Novikov's condition holds." Is this correct? Explain the distinction between the almost sure condition and Novikov's condition.

??? success "Solution to Exercise 8"
    The claim is **false**. Novikov's condition requires

    $$
    \mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
    $$

    Almost sure finiteness of $\int_0^T \theta_s^2\,ds$ is much weaker: it guarantees that the Itô integral $\int_0^t \theta_s\,dW_s$ exists and the stochastic exponential $Z_t$ is well-defined as a local martingale, but it says nothing about exponential integrability. The random variable $\int_0^T \theta_s^2\,ds$ can be a.s. finite yet have tails heavy enough that its exponential moment is infinite.

    In other words, a.s. finiteness gives **existence** of the candidate density, while Novikov gives **validity** as a true martingale with $\mathbb{E}[Z_T] = 1$.
