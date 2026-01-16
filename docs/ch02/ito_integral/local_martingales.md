# Local Martingales

The distinction between **martingales** and **local martingales** is one of the subtle but crucial points in stochastic calculus. While every martingale is a local martingale, the converse is false—and this distinction has important implications for option pricing, stochastic integration, and the theory of SDEs.

---

## Motivation: When Itô Integrals Fail to Be Martingales

Recall that the Itô integral

$$
M_t = \int_0^t H_s\,dW_s
$$

is a martingale when $\mathbb{E}\left[\int_0^T H_s^2\,ds\right] < \infty$.

**But what if this condition fails?**

Consider $H_s = e^{W_s}$. Then:

$$
\mathbb{E}\left[\int_0^T e^{2W_s}\,ds\right] = \int_0^T \mathbb{E}[e^{2W_s}]\,ds = \int_0^T e^{2s}\,ds = \frac{e^{2T} - 1}{2}
$$

This is finite for any fixed $T$, so $\int_0^t e^{W_s}\,dW_s$ is a martingale on $[0, T]$.

**But consider** $H_s = 1/W_s$ near zero, or integrands that grow too fast. The integral may still be well-defined as a **local martingale**, even when it fails to be a true martingale.

---

## Definition

A continuous adapted process $(M_t)_{t \geq 0}$ is a **local martingale** if there exists a sequence of stopping times $(\tau_n)_{n \geq 1}$ with:

1. $\tau_n \uparrow \infty$ almost surely (the stopping times increase to infinity)
2. For each $n$, the **stopped process** $M_t^{\tau_n} := M_{t \wedge \tau_n}$ is a martingale

The sequence $(\tau_n)$ is called a **localizing sequence**.

**Interpretation**: A local martingale is "locally a martingale"—it behaves like a martingale up to each stopping time $\tau_n$, but may fail the global integrability condition.

---

## Relationship Between Martingales and Local Martingales

$$
\text{Martingale} \Longrightarrow \text{Local Martingale}
$$

**Proof**: If $M_t$ is a martingale, take $\tau_n = n$ (constant stopping times). Then $M_t^{\tau_n} = M_{t \wedge n}$ is a martingale by the optional stopping theorem. $\square$

**The converse is FALSE**: There exist local martingales that are not martingales.

---

## The Canonical Example: Exponential Local Martingale

Consider the **stochastic exponential**:

$$
Z_t = \exp\left(W_t - \frac{t}{2}\right)
$$

**Claim 1**: $Z_t$ is a local martingale.

**Proof**: Apply Itô's lemma to $f(x, t) = e^{x - t/2}$:

$$
dZ_t = Z_t\left(dW_t - \frac{1}{2}dt\right) + \frac{1}{2}Z_t\,dt = Z_t\,dW_t
$$

So $Z_t = 1 + \int_0^t Z_s\,dW_s$, which is a local martingale (Itô integrals are always local martingales). $\square$

**Claim 2**: $Z_t$ is actually a **true martingale**.

**Proof**: We verify $\mathbb{E}[Z_t] = 1$ for all $t$:

$$
\mathbb{E}[Z_t] = \mathbb{E}\left[e^{W_t - t/2}\right] = e^{-t/2} \cdot e^{t/2} = 1
$$

using $\mathbb{E}[e^{\theta W_t}] = e^{\theta^2 t/2}$. Since $Z_t \geq 0$ and $\mathbb{E}[Z_t] = \mathbb{E}[Z_0] = 1$, it's a martingale. $\square$

---

## A True Local Martingale (Not a Martingale)

**Example**: Consider the 3-dimensional Bessel process $R_t = |W_t|$ where $W_t \in \mathbb{R}^3$. Define:

$$
M_t = \frac{1}{R_t}
$$

**Facts**:

1. $M_t$ is a local martingale (can be verified via Itô's lemma)
2. $M_t \to 0$ as $t \to \infty$ almost surely
3. $\mathbb{E}[M_t] = \mathbb{E}[M_0] = 1/R_0$ for small $t$, but $\mathbb{E}[M_t] \to 0$ as $t \to \infty$

Since $\mathbb{E}[M_t]$ is not constant, $M_t$ is **not** a martingale!

**Another example**: Let $\tau = \inf\{t : W_t = 1\}$ and define:

$$
M_t = W_{t \wedge \tau}
$$

This is a bounded martingale. But the related process built from certain unbounded integrands can be a strict local martingale.

---

## Characterization: When Is a Local Martingale a Martingale?

**Theorem**: A non-negative local martingale $M_t$ with $M_0 = c$ satisfies:

$$
\mathbb{E}[M_t] \leq c \quad \text{for all } t
$$

It is a true martingale if and only if $\mathbb{E}[M_t] = c$ for all $t$.

**Proof**: By Fatou's lemma applied to the localizing sequence:

$$
\mathbb{E}[M_t] = \mathbb{E}[\lim_n M_{t \wedge \tau_n}] \leq \liminf_n \mathbb{E}[M_{t \wedge \tau_n}] = c
$$

$\square$

**Corollary**: A non-negative local martingale is a **supermartingale**.

---

## The Novikov Condition

**Theorem (Novikov)**: Let $H_t$ be an adapted process. The stochastic exponential

$$
Z_t = \exp\left(\int_0^t H_s\,dW_s - \frac{1}{2}\int_0^t H_s^2\,ds\right)
$$

is a **true martingale** (not just local) if the **Novikov condition** holds:

$$
\boxed{
\mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T H_s^2\,ds\right)\right] < \infty
}
$$

**Significance**: This condition guarantees that change of measure via Girsanov's theorem is valid.

---

## The Kazamaki Condition

**Theorem (Kazamaki)**: The stochastic exponential $Z_t$ is a true martingale if:

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\int_0^T H_s\,dW_s\right)\right] < \infty \quad \text{for all } T
$$

This is weaker than Novikov's condition and sometimes easier to verify.

---

## Implications for Itô Integrals

**Theorem**: For any adapted process $H$ with $\int_0^T H_s^2\,ds < \infty$ a.s., the Itô integral

$$
M_t = \int_0^t H_s\,dW_s
$$

is a **local martingale**.

**When is it a true martingale?**

1. **Sufficient**: $\mathbb{E}\left[\int_0^T H_s^2\,ds\right] < \infty$ (square-integrable integrand)

2. **Necessary and sufficient**: $\mathbb{E}[M_T^2] < \infty$ and $\mathbb{E}[M_t | \mathcal{F}_s] = M_s$

---

## Implications for Option Pricing

In mathematical finance, the distinction matters critically:

**Risk-Neutral Pricing**: Under the risk-neutral measure $\mathbb{Q}$, discounted asset prices should be martingales.

**Problem**: If $S_t/B_t$ (discounted stock price) is only a local martingale, not a true martingale, then:

- Arbitrage may exist
- Standard pricing formulas may fail
- Bubbles can occur

**Example (Stock Price Bubble)**: If $S_t$ follows a process where $S_t/B_t$ is a strict local martingale, then:

$$
\mathbb{E}^{\mathbb{Q}}[S_T/B_T] < S_0/B_0
$$

This means the "fair price" of the stock is less than its current price—a bubble!

---

## Localization Technique

**Strategy**: To prove properties of local martingales, use localization:

1. Take a localizing sequence $\tau_n$
2. Prove the property for each stopped martingale $M^{\tau_n}$
3. Take limits as $n \to \infty$

**Example**: Proving the quadratic variation of a local martingale.

Let $M_t$ be a continuous local martingale. Define:

$$
\tau_n = \inf\{t : |M_t| \geq n\}
$$

Then $M^{\tau_n}$ is a bounded martingale, so standard results apply. The quadratic variation $[M]_t$ is well-defined as the limit.

---

## Quadratic Variation of Local Martingales

**Theorem**: Every continuous local martingale $M_t$ has a well-defined **quadratic variation** $[M]_t$ such that:

$$
M_t^2 - [M]_t \quad \text{is a local martingale}
$$

**For Itô integrals**:

$$
\left[\int_0^\cdot H_s\,dW_s\right]_t = \int_0^t H_s^2\,ds
$$

---

## Summary Table

| Property | Martingale | Local Martingale |
|----------|------------|------------------|
| Definition | $\mathbb{E}[M_t | \mathcal{F}_s] = M_s$ | Stopped processes are martingales |
| Integrability | $\mathbb{E}|M_t| < \infty$ | Only locally |
| Itô integral condition | $\mathbb{E}[\int H^2\,ds] < \infty$ | $\int H^2\,ds < \infty$ a.s. |
| Non-negative case | $\mathbb{E}[M_t] = \mathbb{E}[M_0]$ | $\mathbb{E}[M_t] \leq \mathbb{E}[M_0]$ |
| Girsanov | Valid measure change | Need Novikov/Kazamaki |

---

## Key Takeaways

1. **Every martingale is a local martingale**, but not vice versa.

2. **Itô integrals are always local martingales**; they're true martingales when the integrand is square-integrable.

3. **Non-negative local martingales are supermartingales** (expectations can decrease).

4. **The Novikov condition** ensures stochastic exponentials are true martingales.

5. **In finance**, strict local martingales (not true martingales) correspond to **bubbles**.

6. **Localization** is a powerful technique: prove results for bounded martingales, then extend.

$$
\boxed{
\text{Local Martingale} + \text{Integrability} = \text{Martingale}
}
$$
