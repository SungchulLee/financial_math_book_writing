# Controlling Local Martingales


## Guiding Principle

> **Everything in this section is about controlling local martingales.**

The pages that follow develop a single unifying idea:

$$
\text{Financial modeling} = \text{constructing, transforming, and controlling local martingales}
$$

Local martingales arise naturally from stochastic calculus, but they are often **too weak** for financial applications. The central problem is therefore:

> **When and how can we upgrade a local martingale into a true martingale?**

This question underlies every page in this section:

* [Local Martingales](local_martingale.md) — the raw, uncontrolled object
* [Stochastic Exponential](stochastic_exponential.md) — the transformation enabling control
* [Novikov and Kazamaki Conditions](novikov_kazamaki_conditions.md) — technical guarantees that control is valid
* [Martingales and No-Arbitrage](../risk_neutral/martingale_and_no_arbitrage.md) — the economic requirement demanding control
* [Risk-Neutral Valuation](../risk_neutral/risk_neutral_valuation_principle.md) — the payoff of achieving control
* [Martingale Representation Theorem](martingale_representation_theorem.md) — full control (completeness and hedging)

---

## The Structural Pipeline

The entire section can be understood as the following pipeline:

``` mermaid
flowchart LR

A[Stochastic calculus] --> B[Local martingales]
B --> C[Stochastic exponential]
C --> D[Measure change]
D --> E[Risk-neutral measure Q]
E --> F[Pricing as expectation]
F --> G[Martingale representation]
G --> H[Hedging strategies]

B --> X[Failure: strict local martingale]
X --> Y[Bubbles / pricing anomalies]
```

---

## The Precise Statement

> A financial model is well-behaved when the key local martingales can be sufficiently controlled — supporting an equivalent (local) martingale measure, well-defined pricing, and, when available, martingale representation. Often this means upgrading to true martingales, though the precise requirement depends on the property being studied.

---

## Why Local Martingales Are Not Enough

Local martingales arise naturally from Ito calculus, but most financial results require additional control (integrability, measure change, or representation).

---

## Tools for Control (Preview)

Each subsection of this chapter addresses one step in controlling local martingales:

- **Integrability conditions** → upgrade to true martingales
- **Stochastic exponential** → build multiplicative processes
- **Novikov/Kazamaki** → ensure valid measure change
- **Girsanov theorem** → construct new probability measures
- **Martingale representation** → achieve full hedging

Each tool removes a specific failure mode.

---

## When Control Fails

If control fails, local martingales may become strict local martingales, leading to phenomena such as bubbles and pricing inconsistencies.

---

## How to Read This Section

When reading each subsection, keep asking:

1. What is the local martingale here?
2. Why is it not automatically a true martingale?
3. What condition ensures it becomes one?
4. What breaks if it fails?

If you track these four questions, the entire chapter becomes a single coherent story rather than a collection of technical results.

---

## Exercises


**Exercise 1.** The inverse Bessel(3) process $X_t = 1/R_t$, where $R_t$ is a 3-dimensional Bessel process started at $R_0 = 1$, is a strict local martingale. Explain why $\mathbb{E}[X_t] < X_0 = 1$ for $t > 0$. If $X_t$ were used as the discounted price of a risky asset, explain which of the following would fail: (a) the FTAP, (b) put-call parity, (c) the pricing formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(X_T)]$ for a European call.

??? success "Solution to Exercise 1"
    **Why the expectation drops.** The 3-dimensional Bessel process $R_t$ satisfies $R_t \to \infty$ a.s. as $t \to \infty$, so $X_t = 1/R_t \to 0$ a.s. Since $X_t \geq 0$ and $X_t$ is a continuous local martingale, Fatou's lemma gives:

    $$
    \mathbb{E}[X_t] \leq X_0 = 1
    $$

    If $X_t$ were a true martingale, equality would hold. But the explicit computation (using the known density of the Bessel process) shows $\mathbb{E}[X_t] = 1 - 2\mathcal{N}(-1/\sqrt{t}) + (2/\sqrt{2\pi t})e^{-1/(2t)} < 1$ for $t > 0$. Mass is lost because $X_t$ can approach large values (when $R_t$ is near zero) that contribute to the expectation under stopping but escape to the boundary.

    **(a) FTAP.** The fundamental theorem of asset pricing requires the existence of an equivalent local martingale measure (ELMM). Since $X_t$ is already a local martingale under the given measure, the FTAP is not violated — it only requires a local martingale measure, not a true martingale measure. No-arbitrage (in the NFLVR sense) still holds.

    **(b) Put-call parity.** Standard put-call parity states $C - P = S_0 - Ke^{-rT}$, which relies on $\mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T] = X_0$. Since $\mathbb{E}[X_t] < X_0$, the forward price is strictly less than $X_0 e^{rT}$, and **put-call parity fails** in its standard form. The correction involves the "bubble" term $X_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T] > 0$.

    **(c) Call pricing formula.** For a European call with payoff $(X_T - K)^+$, the formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}(X_T - K)^+]$ gives a value strictly less than the superreplication price. The **call pricing formula undervalues the option** because it misses the bubble component. The correct superreplication price exceeds the risk-neutral expectation. $\square$

---

**Exercise 2.** Consider a stochastic volatility model with zero interest rate:

$$
dS_t = S_t\, \sigma_t\, dW_t^{(1)}, \qquad d\sigma_t = \alpha\, \sigma_t\, dW_t^{(2)}
$$

where $W^{(1)}, W^{(2)}$ are independent Brownian motions under $\mathbb{P}$ and $\alpha > 0$.

(a) Explain why the stock price $S_t$ is a local martingale under $\mathbb{P}$.

(b) Show that for any adapted process $\lambda_t$ satisfying the Novikov condition $\mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \lambda_t^2\, dt\right)\right] < \infty$, the measure $\mathbb{Q}^\lambda$ defined by $d\mathbb{Q}^\lambda / d\mathbb{P}|_{\mathcal{F}_T} = \mathcal{E}\!\left(\int_0^\cdot \lambda_s\, dW_s^{(2)}\right)_T$ is an equivalent local martingale measure for $S$. Conclude that the model admits infinitely many such measures.

(c) Using the structural pipeline from this section, identify which step fails to be unique and explain why the martingale representation theorem does not hold for the filtration generated by $S$ alone.

??? success "Solution to Exercise 2"
    **(a)** The SDE $dS_t = S_t \sigma_t\, dW_t^{(1)}$ has no $dt$ term, so $S_t$ is a stochastic integral against Brownian motion (with integrand $S_t \sigma_t$). Every such stochastic integral is a local martingale. Equivalently, $S_t = S_0\, \mathcal{E}\!\left(\int_0^\cdot \sigma_s\, dW_s^{(1)}\right)_t$, which is a local martingale (see [Stochastic Exponential](stochastic_exponential.md)).

    **(b)** The Girsanov density $\mathcal{E}\!\left(\int_0^\cdot \lambda_s\, dW_s^{(2)}\right)_T$ is a true martingale by the Novikov condition, so $\mathbb{Q}^\lambda$ is a well-defined probability measure equivalent to $\mathbb{P}$.

    Under $\mathbb{Q}^\lambda$, Girsanov's theorem gives:

    $$
    \widetilde{W}_t^{(2)} = W_t^{(2)} - \int_0^t \lambda_s\, ds \quad \text{is a } \mathbb{Q}^\lambda\text{-Brownian motion}
    $$

    Crucially, since $W^{(1)}$ is independent of $\mathcal{E}(\lambda \cdot W^{(2)})$, the process $W^{(1)}$ remains a Brownian motion under $\mathbb{Q}^\lambda$. Therefore $S_t$ still satisfies $dS_t = S_t \sigma_t\, dW_t^{(1)}$ with $W^{(1)}$ a $\mathbb{Q}^\lambda$-Brownian motion, so $S_t$ remains a local martingale under $\mathbb{Q}^\lambda$.

    Since $\lambda$ is arbitrary (subject to the Novikov condition), there are infinitely many equivalent local martingale measures.

    **(c)** In the structural pipeline:

    $$
    \text{Local martingales} \to \text{Stochastic exponential} \to \text{Measure change} \to \mathbb{Q} \to \text{Pricing} \to \text{MRT} \to \text{Hedging}
    $$

    the step "$\text{Measure change} \to \mathbb{Q}$" fails to be unique. Multiple valid $\mathbb{Q}^\lambda$ exist, and each assigns different prices to claims that depend on $\sigma_t$ (such as variance swaps or volatility options).

    The martingale representation theorem fails for the filtration generated by $S$ alone because the market is driven by two independent sources of randomness ($W^{(1)}, W^{(2)}$) but only one is tradeable. A $\mathbb{Q}$-martingale adapted to the full filtration $\mathcal{F}_t = \sigma(W_s^{(1)}, W_s^{(2)} : s \leq t)$ generally requires integrals against both $W^{(1)}$ and $W^{(2)}$, but only the $W^{(1)}$ component can be replicated by trading $S$. This is the hallmark of an **incomplete market**: control of local martingales is partial, not full. $\square$
