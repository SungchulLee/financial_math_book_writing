# Progressive vs Initial Enlargement

There are two fundamentally different ways to enlarge a filtration to include a default time: **progressive enlargement** and **initial enlargement**. They differ in how and when information about default is revealed, with profound implications for pricing, hedging, and the mathematical structure of the model.

---

## Progressive Enlargement

In **progressive enlargement**, information about default is revealed only when it occurs. The market learns of default at the moment it happens—not before.

### Definition

The progressively enlarged filtration is

$$
\mathcal{G}_t := \mathcal{F}_t \vee \sigma(\tau \wedge t) = \mathcal{F}_t \vee \sigma(H_s : s \le t)
$$

where $H_s = \mathbf{1}_{\{\tau \le s\}}$ is the default indicator.

Equivalently, with right-continuous regularization:

$$
\mathcal{G}_t = \bigcap_{s > t} \left( \mathcal{F}_s \vee \sigma(\tau \wedge s) \right)
$$

### Information Content

At time $t$, a market participant observing $\mathcal{G}_t$ knows:
- All market information up to time $t$ (contained in $\mathcal{F}_t$)
- Whether default has occurred by time $t$
- If default has occurred, the exact time $\tau$ when it happened

Crucially, they do **not** know the future default time if $\tau > t$.

### Key Properties

1. **$\tau$ is a stopping time:** $\{\tau \le t\} \in \mathcal{G}_t$ by construction
2. **Surprise default:** On $\{\tau > t\}$, there is no advance knowledge of $\tau$
3. **Causality preserved:** Information arrives as events unfold
4. **Natural for market models:** Reflects how default information actually propagates

### Characterization of G_t-Measurability

A random variable $X$ is $\mathcal{G}_t$-measurable if and only if it has the form

$$
X = Y \mathbf{1}_{\{\tau > t\}} + Z(\tau) \mathbf{1}_{\{\tau \le t\}}
$$

where:
- $Y$ is $\mathcal{F}_t$-measurable
- $Z: [0,t] \times \Omega \to \mathbb{R}$ is $\mathcal{B}([0,t]) \otimes \mathcal{F}_t$-measurable

This decomposition shows that post-default, the exact timing $\tau$ becomes available information.

---

## Initial Enlargement

In **initial enlargement**, the default time is known from the very beginning (time 0). This models a situation where an agent has complete foreknowledge of when default will occur.

### Definition

The initially enlarged filtration is

$$
\mathcal{G}_t := \mathcal{F}_t \vee \sigma(\tau)
$$

Here, $\sigma(\tau)$ represents complete knowledge of the default time, available at all times.

### Information Content

At any time $t$, an observer of $\mathcal{G}_t$ knows:
- All market information up to time $t$
- The exact value of $\tau$ (regardless of whether $\tau \le t$ or $\tau > t$)

This is strictly more information than progressive enlargement provides.

### Financially Unrealistic but Mathematically Useful

Initial enlargement corresponds to **insider information**—knowing default time in advance is equivalent to having perfect foresight about a specific event. While unrealistic for default modeling, it serves important theoretical purposes:

1. **Benchmark calculations:** Provides upper bounds on information value
2. **Mathematical tractability:** Conditional expectations simplify
3. **Insider trading analysis:** Models agents with private information
4. **Theoretical completeness:** Illuminates the role of information in pricing

---

## Mathematical Comparison

### Filtration Inclusion

The filtrations satisfy a strict inclusion:

$$
\mathcal{F}_t \subsetneq \mathcal{G}_t^{\text{prog}} \subsetneq \mathcal{G}_t^{\text{init}}
$$

Progressive enlargement adds "just enough" information to observe default, while initial enlargement adds "complete" information about $\tau$.

### Conditional Expectations

For a random variable $X$:

**Progressive:** $\mathbb{E}[X \mid \mathcal{G}_t^{\text{prog}}]$ depends on whether $\tau \le t$ or $\tau > t$

**Initial:** $\mathbb{E}[X \mid \mathcal{G}_t^{\text{init}}] = \mathbb{E}[X \mid \mathcal{F}_t, \tau]$ conditions on the known value of $\tau$

### Example: Survival Probability

Consider computing $\mathbb{P}(\tau > T \mid \mathcal{G}_t)$ for $T > t$:

**Progressive enlargement ($\tau > t$):**

$$
\mathbb{P}(\tau > T \mid \mathcal{G}_t^{\text{prog}}) = \frac{\mathbb{P}(\tau > T \mid \mathcal{F}_t)}{\mathbb{P}(\tau > t \mid \mathcal{F}_t)} = \frac{G_T^{\mathcal{F}}}{G_t^{\mathcal{F}}}
$$

where $G_s^{\mathcal{F}} = \mathbb{P}(\tau > s \mid \mathcal{F}_t)$.

**Initial enlargement:**

$$
\mathbb{P}(\tau > T \mid \mathcal{G}_t^{\text{init}}) = \mathbf{1}_{\{\tau > T\}}
$$

since $\tau$ is known exactly.

---

## Semimartingale Preservation

A critical question is whether $\mathcal{F}$-semimartingales remain semimartingales in the enlarged filtration.

### Progressive Enlargement

Under mild conditions (the **density hypothesis** or **intensity hypothesis**), every $(\mathcal{F}, \mathbb{P})$-semimartingale remains a $(\mathcal{G}^{\text{prog}}, \mathbb{P})$-semimartingale. The decomposition involves:

$$
X_t = \tilde{X}_t + \int_0^{t \wedge \tau} \frac{d\langle X, G \rangle_s}{G_{s-}}
$$

where $\tilde{X}$ is a $\mathcal{G}$-martingale and $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$.

### Initial Enlargement (Jacod's Criterion)

For initial enlargement, the situation is more delicate. Jacod's theorem states that $\mathcal{F}$-semimartingales remain $\mathcal{G}^{\text{init}}$-semimartingales if and only if the conditional law of $\tau$ given $\mathcal{F}_\infty$ is absolutely continuous with respect to some $\sigma$-finite measure.

When this fails, fundamental pricing theory breaks down in the enlarged filtration.

---

## Implications for Credit Modeling

### Why Progressive Enlargement is Standard

1. **Causality:** Default cannot be foreseen—it arrives as a surprise
2. **Intensity framework:** Reduced-form models naturally produce progressive enlargement
3. **Market consistency:** Market prices reflect progressively revealed information
4. **Hedging feasibility:** Trading strategies must be adapted to observable information

### When Initial Enlargement Appears

1. **Theoretical benchmarks:** Computing maximal hedge values
2. **Structural model analysis:** Studying anticipative aspects
3. **Regulatory stress testing:** Worst-case scenarios with perfect information
4. **Academic investigations:** Understanding information's role in pricing

---

## The Density Hypothesis

A key technical condition ensuring tractability under progressive enlargement is the **density hypothesis**.

### Statement

There exists a family of non-negative $\mathcal{F}_t$-measurable random variables $(\alpha_t^u)_{u \ge 0}$ such that for all $t \ge 0$:

$$
\mathbb{P}(\tau > u \mid \mathcal{F}_t) = \int_u^\infty \alpha_t^s \, ds \quad \text{for } u \ge 0
$$

The function $u \mapsto \alpha_t^u$ is the conditional density of $\tau$ given $\mathcal{F}_t$.

### Implications

Under the density hypothesis:
- The Azéma supermartingale has absolutely continuous sample paths
- Default intensity exists: $\lambda_t = \alpha_t^t / G_t$ on $\{\tau > t\}$
- Semimartingale decompositions have explicit forms
- Pricing formulas simplify significantly

---

## Worked Example: Exponential Default Time

Let $\tau \sim \text{Exp}(\lambda)$ be independent of $(\mathcal{F}_t)$ with constant intensity $\lambda > 0$.

### Progressive Enlargement

The survival probability is $G_t = e^{-\lambda t}$ (deterministic since $\tau$ is independent of $\mathcal{F}$).

On $\{\tau > t\}$:

$$
\mathbb{P}(\tau > T \mid \mathcal{G}_t) = \mathbb{P}(\tau > T \mid \tau > t) = e^{-\lambda(T-t)}
$$

This follows from the memoryless property of the exponential distribution.

### Initial Enlargement

Given $\mathcal{G}_t^{\text{init}} = \mathcal{F}_t \vee \sigma(\tau)$:

$$
\mathbb{P}(\tau > T \mid \mathcal{G}_t^{\text{init}}) = \mathbf{1}_{\{\tau > T\}}
$$

The uncertainty is completely resolved by knowing $\tau$.

---

## Key Takeaways

- **Progressive enlargement** reveals default information gradually—the standard choice for credit models
- **Initial enlargement** assumes full foreknowledge—useful for theoretical analysis
- Progressive enlargement preserves causality and aligns with market information flow
- The density hypothesis ensures tractability under progressive enlargement
- Most pricing and hedging results in credit risk rely on progressive enlargement
- Semimartingale preservation requires careful verification in either case

---

## Further Reading

- Jeulin, T., & Yor, M. (1978). Grossissement d'une filtration et semi-martingales. *Séminaire de Probabilités XII*, Lecture Notes in Mathematics 649.
- Jacod, J. (1985). Grossissement initial, hypothèse (H'), et théorème de Girsanov. *Séminaire de Probabilités XIX*.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 5.
- Protter, P. (2005). *Stochastic Integration and Differential Equations*. Springer, Chapter VI.

---

## Exercises

**Exercise 1.** Let $\tau \sim \text{Exp}(\lambda)$ be independent of $\mathcal{F}_t$. Under progressive enlargement, compute $\mathbb{P}(\tau > T \mid \mathcal{G}_t^{\text{prog}})$ on the event $\{\tau > t\}$ for $T > t$. Compare this with the result under initial enlargement. Explain the economic difference between the two answers.

---

**Exercise 2.** Show that for any time $t$, the filtrations satisfy the strict inclusion $\mathcal{F}_t \subsetneq \mathcal{G}_t^{\text{prog}} \subsetneq \mathcal{G}_t^{\text{init}}$. Provide a concrete random variable that is $\mathcal{G}_t^{\text{init}}$-measurable but not $\mathcal{G}_t^{\text{prog}}$-measurable on the event $\{\tau > t\}$.

---

**Exercise 3.** Under progressive enlargement, every $\mathcal{G}_t$-measurable random variable $X$ has the form

$$
X = Y\,\mathbf{1}_{\{\tau > t\}} + Z(\tau)\,\mathbf{1}_{\{\tau \le t\}}
$$

For the specific case where $X$ represents the mark-to-market value of a defaultable bond, identify the economic meaning of $Y$ (the pre-default component) and $Z(\tau)$ (the post-default component). How does recovery at default enter through $Z(\tau)$?

---

**Exercise 4.** Explain why initial enlargement corresponds to "insider information" in the context of credit risk. A trader who knows the exact default time $\tau$ in advance can construct arbitrage strategies. Describe one such strategy for a CDS contract and explain why the no-arbitrage principle fails under initial enlargement without appropriate measure changes.

---

**Exercise 5.** Under progressive enlargement with the density hypothesis, an $\mathcal{F}$-semimartingale $X_t$ decomposes as

$$
X_t = \tilde{X}_t + \int_0^{t \wedge \tau} \frac{d\langle X, G\rangle_s}{G_{s-}}
$$

For $X_t = W_t$ (a standard Brownian motion) and $G_t = e^{-\lambda t}$ (constant intensity), compute the drift correction. Show that $W_t$ remains a $\mathcal{G}$-martingale, confirming immersion.

---

**Exercise 6.** Jacod's criterion states that $\mathcal{F}$-semimartingales remain $\mathcal{G}^{\text{init}}$-semimartingales if the conditional law of $\tau$ given $\mathcal{F}_\infty$ is absolutely continuous. Give an example of a default time $\tau$ for which this condition fails (hint: consider $\tau$ that is $\mathcal{F}_\infty$-measurable). Explain why semimartingale preservation breaks down in this case.
