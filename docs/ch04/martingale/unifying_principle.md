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
* [Martingales and No-Arbitrage](../finance/martingale_and_no_arbitrage.md) — the economic requirement demanding control
* [Risk-Neutral Valuation](../finance/risk_neutral_valuation_principle.md) — the payoff of achieving control
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

## The Guiding Principle

### Informal Statement

> A financial model is well-behaved when the key local martingales can be sufficiently controlled — supporting an equivalent (local) martingale measure, well-defined pricing, and, when available, martingale representation. Often this means upgrading to true martingales, though the precise requirement depends on the property being studied.

### Formal Perspective

The most important distinction is between true martingales and strict local martingales. Let $M$ be a nonnegative local martingale. Then $M$ is a supermartingale, and:

**True martingale case.** If $M$ is a true martingale:

$$
\mathbb{E}[M_t] = \mathbb{E}[M_0] \quad \text{for all } t \geq 0
$$

**Strict local martingale case.** If $M$ is not a true martingale:

$$
\mathbb{E}[M_t] < \mathbb{E}[M_0]
$$

which signals **loss of mass**, instability, or economic inconsistency.

---

## Why Local Martingales Are Not Enough

Local martingales arise automatically from Ito calculus:

* Ito integrals $\to$ local martingales
* Drift-free SDEs $\to$ local martingales
* Stochastic exponentials $\to$ local martingales

But finance requires more:

| Requirement     | Why needed                 | Local martingale sufficient? |
| --------------- | -------------------------- | ---------------------------- |
| No-arbitrage    | Fair pricing               | Not always                   |
| Measure change  | Define $\mathbb{Q}$        | Needs true martingale        |
| Pricing formula | Expectations well-defined  | Needs integrability          |
| Hedging         | Stability of value process | Needs stronger control       |

---

## Tools for Controlling Local Martingales

This section introduces several mechanisms to upgrade local martingales.

### 1. Integrability Conditions

* $L^p$ bounds
* Finite quadratic variation

These ensure:

$$
\text{Local martingale} \;\Longrightarrow\; \text{True martingale}
$$

---

### 2. Stochastic Exponential

Transforms additive noise into multiplicative structure:

$$
\mathcal{E}(M)_t = \exp\!\left(M_t - \tfrac{1}{2}\langle M \rangle_t\right)
$$

Key role: candidate density for measure change.

---

### 3. Novikov and Kazamaki Conditions

Ensure:

$$
\mathcal{E}(M) \text{ is a true martingale}
$$

This is critical for:

* Girsanov's theorem
* Existence of the risk-neutral measure

---

### 4. Measure Change (Girsanov)

Reweights probability so that discounted prices become martingales under the new measure $\mathbb{Q}$.

---

### 5. Martingale Representation

Ensures that every $\mathbb{Q}$-martingale can be written as a stochastic integral against the driving Brownian motion. Financial meaning: every contingent claim can be hedged.

---

## When Control Fails

If a local martingale cannot be upgraded:

### 1. Strict Local Martingale

$$
\mathbb{E}[M_t] < M_0
$$

Interpretation: mass escapes to infinity and the model loses probability weight.

---

### 2. Financial Consequences

* Asset price bubbles
* Failure of put-call parity
* Invalid measure change

---

### 3. Example Phenomena

* CEV model with $\beta > 1$
* Inverse Bessel process
* Exploding stochastic exponentials

---

## Big Picture Connections

| Concept                | Role in the control problem       |
| ---------------------- | --------------------------------- |
| Local martingale       | Raw output of stochastic calculus |
| True martingale        | Controlled, usable object         |
| Stochastic exponential | Tool for transformation           |
| Novikov/Kazamaki       | Control conditions                |
| ELMM ($\mathbb{Q}$)   | Controlled probability measure    |
| MRT                    | Completeness (full control)       |

---

## Section Takeaway

> **A financial model is well-behaved when the key local martingales can be sufficiently controlled to support an equivalent (local) martingale measure (no-arbitrage), well-defined pricing via expectations (integrability), and, when available, martingale representation (hedging/completeness). In many important cases, this control takes the form of upgrading local martingales to true martingales, though the precise requirements depend on the property being studied.**

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


**Exercise 1.** Let $W_t$ be a standard Brownian motion and define $M_t = \int_0^t W_s^2\, dW_s$. Show that $M_t$ is a local martingale. Compute its quadratic variation $\langle M \rangle_t$ and verify that $\mathbb{E}[\langle M \rangle_t] < \infty$ for each $t$, concluding that $M_t$ is in fact a true martingale.

??? success "Solution to Exercise 1"
    **Local martingale.** By definition, $M_t = \int_0^t W_s^2\, dW_s$ is an Ito integral with respect to Brownian motion. Every Ito integral against Brownian motion with a progressively measurable integrand is a local martingale (with localizing sequence given by stopping times $\tau_n = \inf\{t : |M_t| \geq n\}$).

    **Quadratic variation.** For the Ito integral $M_t = \int_0^t f_s\, dW_s$ with $f_s = W_s^2$:

    $$
    \langle M \rangle_t = \int_0^t f_s^2\, ds = \int_0^t W_s^4\, ds
    $$

    **Expectation of quadratic variation.** Since $\mathbb{E}[W_s^4] = 3s^2$ (fourth moment of Gaussian):

    $$
    \mathbb{E}[\langle M \rangle_t] = \int_0^t \mathbb{E}[W_s^4]\, ds = \int_0^t 3s^2\, ds = t^3 < \infty
    $$

    **Conclusion.** Since $\mathbb{E}[\langle M \rangle_t] < \infty$ for each $t$, the Ito isometry implies $\mathbb{E}[M_t^2] = \mathbb{E}[\langle M \rangle_t] = t^3 < \infty$. An $L^2$-bounded local martingale is a true martingale (by the martingale convergence theorem applied to the localizing sequence). Therefore $M_t$ is a true martingale. $\square$

---

**Exercise 2.** Let $M_t$ be a continuous local martingale with localizing sequence $(\tau_n)$. Prove that if $M$ is uniformly integrable (i.e., the family $\{M_t : t \geq 0\}$ is uniformly integrable), then $M$ is a true martingale.

??? success "Solution to Exercise 2"
    Let $0 \leq s < t$. Since $(\tau_n)$ is a localizing sequence, $M^{\tau_n}$ is a true martingale for each $n$, so:

    $$
    \mathbb{E}[M_{t \wedge \tau_n} \mid \mathcal{F}_s] = M_{s \wedge \tau_n}
    $$

    As $n \to \infty$, $\tau_n \to \infty$ a.s., so $M_{t \wedge \tau_n} \to M_t$ a.s. and $M_{s \wedge \tau_n} \to M_s$ a.s.

    By uniform integrability of $\{M_t\}$, the family $\{M_{t \wedge \tau_n}\}_n$ is also uniformly integrable (since $|M_{t \wedge \tau_n}| \leq \sup_{u \leq t} |M_u|$ and continuous local martingales on $[0,t]$ inherit UI from the endpoint). Therefore convergence in $L^1$ holds:

    $$
    M_{t \wedge \tau_n} \xrightarrow{L^1} M_t
    $$

    Taking $n \to \infty$ in the conditional expectation (using $L^1$ convergence on both sides):

    $$
    \mathbb{E}[M_t \mid \mathcal{F}_s] = M_s
    $$

    This is the martingale property. $\square$

---

**Exercise 3.** Consider the stochastic exponential $\mathcal{E}(\theta W)_t = \exp\!\left(\theta W_t - \frac{1}{2}\theta^2 t\right)$ where $\theta$ is a constant. Verify the Novikov condition $\mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta^2\, ds\right)\right] < \infty$ and conclude that $\mathcal{E}(\theta W)$ is a true martingale on $[0, T]$. Then explain why this result is essential for the Girsanov construction of the risk-neutral measure in the Black-Scholes model.

??? success "Solution to Exercise 3"
    **Novikov condition.** With constant integrand $\theta$:

    $$
    \frac{1}{2}\int_0^T \theta^2\, ds = \frac{1}{2}\theta^2 T
    $$

    This is a deterministic constant, so:

    $$
    \mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\theta^2 T\right)\right] = \exp\!\left(\frac{1}{2}\theta^2 T\right) < \infty
    $$

    The Novikov condition is satisfied.

    **Conclusion.** By Novikov's theorem, $\mathcal{E}(\theta W)_t$ is a true martingale on $[0, T]$. In particular, $\mathbb{E}[\mathcal{E}(\theta W)_T] = \mathcal{E}(\theta W)_0 = 1$, so $\mathcal{E}(\theta W)_T$ is a valid Radon–Nikodym density.

    **Application to Black-Scholes.** In the Black-Scholes model, the market price of risk is $\theta = (\mu - r)/\sigma$, a constant. The Girsanov density is:

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \mathcal{E}(-\theta W)_T = \exp\!\left(-\theta W_T - \frac{1}{2}\theta^2 T\right)
    $$

    The Novikov condition guarantees this is a true martingale, which ensures that $\mathbb{Q}$ is a well-defined probability measure equivalent to $\mathbb{P}$. Without this, the Girsanov measure change would be invalid and the risk-neutral pricing framework would collapse. The fact that $\theta$ is constant (hence the Novikov condition is trivially satisfied) is one reason the Black-Scholes model is so tractable. $\square$

---

**Exercise 4.** The inverse Bessel(3) process $X_t = 1/R_t$, where $R_t$ is a 3-dimensional Bessel process started at $R_0 = 1$, is a strict local martingale. Explain why $\mathbb{E}[X_t] < X_0 = 1$ for $t > 0$. If $X_t$ were used as the discounted price of a risky asset, explain which of the following would fail: (a) the FTAP, (b) put-call parity, (c) the pricing formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(X_T)]$ for a European call.

??? success "Solution to Exercise 4"
    **Why the expectation drops.** The 3-dimensional Bessel process $R_t$ satisfies $R_t \to \infty$ a.s. as $t \to \infty$, so $X_t = 1/R_t \to 0$ a.s. Since $X_t \geq 0$ and $X_t$ is a continuous local martingale, Fatou's lemma gives:

    $$
    \mathbb{E}[X_t] \leq X_0 = 1
    $$

    If $X_t$ were a true martingale, equality would hold. But the explicit computation (using the known density of the Bessel process) shows $\mathbb{E}[X_t] = 1 - 2\mathcal{N}(-1/\sqrt{t}) + (2/\sqrt{2\pi t})e^{-1/(2t)} < 1$ for $t > 0$. Mass is lost because $X_t$ can approach large values (when $R_t$ is near zero) that contribute to the expectation under stopping but escape to the boundary.

    **(a) FTAP.** The fundamental theorem of asset pricing requires the existence of an equivalent local martingale measure (ELMM). Since $X_t$ is already a local martingale under the given measure, the FTAP is not violated — it only requires a local martingale measure, not a true martingale measure. No-arbitrage (in the NFLVR sense) still holds.

    **(b) Put-call parity.** Standard put-call parity states $C - P = S_0 - Ke^{-rT}$, which relies on $\mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T] = X_0$. Since $\mathbb{E}[X_t] < X_0$, the forward price is strictly less than $X_0 e^{rT}$, and **put-call parity fails** in its standard form. The correction involves the "bubble" term $X_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T] > 0$.

    **(c) Call pricing formula.** For a European call with payoff $(X_T - K)^+$, the formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}(X_T - K)^+]$ gives a value strictly less than the superreplication price. The **call pricing formula undervalues the option** because it misses the bubble component. The correct superreplication price exceeds the risk-neutral expectation. $\square$

---

**Exercise 5.** Suppose $\theta_t$ is a deterministic function of time satisfying $\int_0^T \theta_t^2\, dt < \infty$. Show that the Novikov condition $\mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_t^2\, dt\right)\right] < \infty$ is automatically satisfied, and conclude that the stochastic exponential $\mathcal{E}\!\left(\int_0^\cdot \theta_s\, dW_s\right)$ is a true martingale on $[0, T]$. Give an example of a random (adapted) process $\theta_t$ for which the Novikov condition fails.

??? success "Solution to Exercise 5"
    **Deterministic case.** If $\theta_t$ is deterministic, then $\int_0^T \theta_t^2\, dt$ is a deterministic constant $c < \infty$. Therefore:

    $$
    \mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_t^2\, dt\right)\right] = \exp\!\left(\frac{c}{2}\right) < \infty
    $$

    The Novikov condition is trivially satisfied. By Novikov's theorem, $\mathcal{E}\!\left(\int_0^\cdot \theta_s\, dW_s\right)$ is a true martingale on $[0, T]$.

    This covers all models with deterministic volatility of the market price of risk, including the Black-Scholes model ($\theta_t = (\mu - r)/\sigma$) and the Ho-Lee interest rate model.

    **Random counterexample.** Let $\theta_t = W_t / \sqrt{T - t}$ for $t \in [0, T)$. Then:

    $$
    \int_0^T \theta_t^2\, dt = \int_0^T \frac{W_t^2}{T - t}\, dt
    $$

    This integral diverges a.s. as $t \to T^-$ (since $W_t^2$ does not vanish while $1/(T-t) \to \infty$), so:

    $$
    \mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \frac{W_t^2}{T - t}\, dt\right)\right] = +\infty
    $$

    The Novikov condition fails. The corresponding stochastic exponential may be a strict local martingale, meaning the Girsanov measure change is not valid on $[0, T]$. $\square$

---

**Exercise 6.** Let $M_t$ be a continuous local martingale with $M_0 = 0$. Apply Ito's formula to $f(x) = e^x$ with $X_t = M_t - \frac{1}{2}\langle M \rangle_t$ to verify that $\mathcal{E}(M)_t = \exp\!\left(M_t - \frac{1}{2}\langle M \rangle_t\right)$ satisfies the SDE

$$
d\mathcal{E}(M)_t = \mathcal{E}(M)_t\, dM_t
$$

Conclude that $\mathcal{E}(M)$ is a nonnegative local martingale, and deduce that $\mathbb{E}[\mathcal{E}(M)_t] \leq 1$ for all $t \geq 0$.

??? success "Solution to Exercise 6"
    Define $X_t = M_t - \frac{1}{2}\langle M \rangle_t$ so that $\mathcal{E}(M)_t = e^{X_t}$. Since $\langle M \rangle_t$ has continuous paths of bounded variation:

    $$
    dX_t = dM_t - \frac{1}{2}\, d\langle M \rangle_t, \qquad d\langle X \rangle_t = d\langle M \rangle_t
    $$

    Applying Ito's formula with $f(x) = e^x$ (so $f' = f'' = e^x$):

    $$
    d\mathcal{E}(M)_t = e^{X_t}\, dX_t + \frac{1}{2} e^{X_t}\, d\langle X \rangle_t
    $$

    $$
    = e^{X_t}\!\left(dM_t - \frac{1}{2}\, d\langle M \rangle_t\right) + \frac{1}{2} e^{X_t}\, d\langle M \rangle_t = e^{X_t}\, dM_t = \mathcal{E}(M)_t\, dM_t
    $$

    **Local martingale.** The SDE $d\mathcal{E}(M)_t = \mathcal{E}(M)_t\, dM_t$ has no drift term, so $\mathcal{E}(M)$ is a stochastic integral against the local martingale $M$, hence itself a local martingale.

    **Nonnegativity.** Since $\mathcal{E}(M)_t = \exp(M_t - \frac{1}{2}\langle M \rangle_t)$ is the exponential of a real number, $\mathcal{E}(M)_t > 0$ a.s. for all $t$.

    **Supermartingale bound.** A nonnegative local martingale is a supermartingale (by Fatou's lemma applied to the localizing sequence). Therefore:

    $$
    \mathbb{E}[\mathcal{E}(M)_t] \leq \mathcal{E}(M)_0 = e^{0} = 1
    $$

    Equality holds for all $t$ if and only if $\mathcal{E}(M)$ is a true martingale. This is exactly the gap that the Novikov and Kazamaki conditions are designed to close. $\square$

---

**Exercise 7.** Consider a stochastic volatility model with zero interest rate:

$$
dS_t = S_t\, \sigma_t\, dW_t^{(1)}, \qquad d\sigma_t = \alpha\, \sigma_t\, dW_t^{(2)}
$$

where $W^{(1)}, W^{(2)}$ are independent Brownian motions under $\mathbb{P}$ and $\alpha > 0$.

(a) Explain why the stock price $S_t$ is a local martingale under $\mathbb{P}$.

(b) Show that for any adapted process $\lambda_t$ satisfying the Novikov condition $\mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \lambda_t^2\, dt\right)\right] < \infty$, the measure $\mathbb{Q}^\lambda$ defined by $d\mathbb{Q}^\lambda / d\mathbb{P}|_{\mathcal{F}_T} = \mathcal{E}\!\left(\int_0^\cdot \lambda_s\, dW_s^{(2)}\right)_T$ is an equivalent local martingale measure for $S$. Conclude that the model admits infinitely many such measures.

(c) Using the structural pipeline from this section, identify which step fails to be unique and explain why the martingale representation theorem does not hold for the filtration generated by $S$ alone.

??? success "Solution to Exercise 7"
    **(a)** The SDE $dS_t = S_t \sigma_t\, dW_t^{(1)}$ has no $dt$ term, so $S_t$ is a stochastic integral against Brownian motion (with integrand $S_t \sigma_t$). Every such stochastic integral is a local martingale. Equivalently, $S_t = S_0\, \mathcal{E}\!\left(\int_0^\cdot \sigma_s\, dW_s^{(1)}\right)_t$, which is a local martingale by Exercise 6.

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
