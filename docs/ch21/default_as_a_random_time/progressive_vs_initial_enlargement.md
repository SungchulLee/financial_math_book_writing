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

??? success "Solution to Exercise 1"

    **Progressive enlargement on $\{\tau > t\}$ for $T > t$.**

    Since $\tau \sim \text{Exp}(\lambda)$ is independent of $\mathcal{F}_t$, the survival probability is deterministic: $G_s = \mathbb{P}(\tau > s \mid \mathcal{F}_t) = e^{-\lambda s}$. Using the standard progressive enlargement formula on $\{\tau > t\}$:

    $$
    \mathbb{P}(\tau > T \mid \mathcal{G}_t^{\text{prog}}) = \frac{\mathbb{P}(\tau > T \mid \mathcal{F}_t)}{\mathbb{P}(\tau > t \mid \mathcal{F}_t)} = \frac{G_T}{G_t} = \frac{e^{-\lambda T}}{e^{-\lambda t}} = e^{-\lambda(T-t)}
    $$

    This can also be derived directly from the memoryless property of the exponential distribution: $\mathbb{P}(\tau > T \mid \tau > t) = e^{-\lambda(T-t)}$.

    **Initial enlargement.**

    Under initial enlargement, the exact value of $\tau$ is known at all times. Therefore:

    $$
    \mathbb{P}(\tau > T \mid \mathcal{G}_t^{\text{init}}) = \mathbf{1}_{\{\tau > T\}}
    $$

    This is either 0 or 1 — there is no uncertainty about survival.

    **Economic comparison.**

    - Under **progressive enlargement**, a market participant on the event $\{\tau > t\}$ knows only that default has not yet occurred. The survival probability $e^{-\lambda(T-t)}$ reflects genuine uncertainty about whether default will happen between $t$ and $T$. This uncertainty decreases the value of defaultable claims and generates a credit spread. The market participant must hedge this residual default risk.

    - Under **initial enlargement**, the agent knows $\tau$ exactly. If $\tau > T$, the agent is certain no default will occur and values the claim at its default-free price. If $\tau \le T$, the agent knows default will happen and can act accordingly. There is no credit spread from the perspective of this insider — only deterministic knowledge.

    The difference $e^{-\lambda(T-t)}$ vs. $\mathbf{1}_{\{\tau > T\}}$ quantifies the **value of knowing the default time in advance**. The insider's certainty eliminates the need for credit risk premia entirely. $\square$

---

**Exercise 2.** Show that for any time $t$, the filtrations satisfy the strict inclusion $\mathcal{F}_t \subsetneq \mathcal{G}_t^{\text{prog}} \subsetneq \mathcal{G}_t^{\text{init}}$. Provide a concrete random variable that is $\mathcal{G}_t^{\text{init}}$-measurable but not $\mathcal{G}_t^{\text{prog}}$-measurable on the event $\{\tau > t\}$.

??? success "Solution to Exercise 2"

    **Showing $\mathcal{F}_t \subsetneq \mathcal{G}_t^{\text{prog}}$.**

    By definition, $\mathcal{G}_t^{\text{prog}} = \mathcal{F}_t \vee \sigma(\tau \wedge t)$, so $\mathcal{F}_t \subseteq \mathcal{G}_t^{\text{prog}}$ automatically. To show strict inclusion, consider the event $A = \{\tau \le t\}$. This event is in $\mathcal{G}_t^{\text{prog}}$ (by construction of the default indicator process). However, if $\tau$ is not an $\mathcal{F}$-stopping time — as in reduced-form models — then $\{\tau \le t\} \notin \mathcal{F}_t$ in general. For concreteness, if $\tau$ is constructed via a Cox process with $E \perp \mathcal{F}_\infty$, the event $\{\tau \le t\} = \{E \le \Lambda_t\}$ depends on $E$, which is not $\mathcal{F}_t$-measurable. Hence $\mathcal{F}_t \subsetneq \mathcal{G}_t^{\text{prog}}$.

    **Showing $\mathcal{G}_t^{\text{prog}} \subsetneq \mathcal{G}_t^{\text{init}}$.**

    By definition, $\mathcal{G}_t^{\text{init}} = \mathcal{F}_t \vee \sigma(\tau)$ and $\mathcal{G}_t^{\text{prog}} = \mathcal{F}_t \vee \sigma(\tau \wedge t)$. Since $\sigma(\tau \wedge t) \subseteq \sigma(\tau)$ (knowing $\tau$ determines $\tau \wedge t$), we have $\mathcal{G}_t^{\text{prog}} \subseteq \mathcal{G}_t^{\text{init}}$. For strict inclusion, we need to exhibit a random variable measurable with respect to $\mathcal{G}_t^{\text{init}}$ but not $\mathcal{G}_t^{\text{prog}}$.

    **A concrete random variable.** Consider the event $\{\tau > t\}$ and the random variable:

    $$
    X = \tau \cdot \mathbf{1}_{\{\tau > t\}}
    $$

    Under **initial enlargement**, $X$ is $\mathcal{G}_t^{\text{init}}$-measurable because $\tau$ is $\sigma(\tau)$-measurable and $\{\tau > t\} \in \sigma(\tau)$.

    Under **progressive enlargement** on $\{\tau > t\}$, the $\mathcal{G}_t^{\text{prog}}$-measurable information includes $\mathcal{F}_t$ and the knowledge that $\tau > t$, but **not** the exact future value of $\tau$. The representation theorem for $\mathcal{G}_t^{\text{prog}}$-measurable random variables states that on $\{\tau > t\}$, any $\mathcal{G}_t^{\text{prog}}$-measurable random variable equals an $\mathcal{F}_t$-measurable random variable. But $X = \tau$ on $\{\tau > t\}$, and $\tau$ is not $\mathcal{F}_t$-measurable (in reduced-form models, $\tau$ depends on the independent trigger $E$). Hence $X$ is not $\mathcal{G}_t^{\text{prog}}$-measurable.

    **Economic interpretation:** Under progressive enlargement on $\{\tau > t\}$, we know default hasn't happened yet but not when it will happen. Under initial enlargement, we know exactly when it will happen. The random variable $\tau \cdot \mathbf{1}_{\{\tau > t\}}$ — the future default time, observed prior to default — captures this informational gap. $\square$

---

**Exercise 3.** Under progressive enlargement, every $\mathcal{G}_t$-measurable random variable $X$ has the form

$$
X = Y\,\mathbf{1}_{\{\tau > t\}} + Z(\tau)\,\mathbf{1}_{\{\tau \le t\}}
$$

For the specific case where $X$ represents the mark-to-market value of a defaultable bond, identify the economic meaning of $Y$ (the pre-default component) and $Z(\tau)$ (the post-default component). How does recovery at default enter through $Z(\tau)$?

??? success "Solution to Exercise 3"

    **The decomposition.** A $\mathcal{G}_t$-measurable random variable $X$ can be written as:

    $$
    X = Y\,\mathbf{1}_{\{\tau > t\}} + Z(\tau)\,\mathbf{1}_{\{\tau \le t\}}
    $$

    where $Y$ is $\mathcal{F}_t$-measurable and $Z(s)$ is $\mathcal{B}([0,t]) \otimes \mathcal{F}_t$-measurable.

    **Economic meaning of $Y$ (pre-default component).**

    On the event $\{\tau > t\}$, no default has occurred, so the bond is still "alive." The value $Y$ is $\mathcal{F}_t$-measurable, meaning it depends only on market information (interest rates, credit spreads, implied volatilities, etc.) and not on any default-specific information. This is the **pre-default mark-to-market value** of the bond.

    For a defaultable bond with maturity $T$ and zero recovery, under immersion:

    $$
    Y = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + \lambda_s)\,ds} \;\Big|\; \mathcal{F}_t\right]
    $$

    This represents the discounted expected payoff, adjusted for both time value of money ($r_s$) and credit risk ($\lambda_s$). The trader uses this to quote the bond price, compute credit spreads, and manage risk. Since $Y$ depends on $\mathcal{F}_t$, it moves with interest rate curves, credit curves, and other market factors.

    **Economic meaning of $Z(\tau)$ (post-default component) and recovery.**

    On $\{\tau \le t\}$, default has occurred at the known time $\tau$. The function $Z(\tau)$ represents the **post-default value**, which depends on:

    - The exact default time $\tau$ (known post-default)
    - Market conditions at time $t$ (through $\mathcal{F}_t$-measurability in $\omega$)

    **Recovery at default enters through $Z(\tau)$ as follows.** If the bond has a recovery payment of $R(\tau)$ at default time $\tau$ (e.g., a fraction of face value), then the post-default value at time $t > \tau$ is the time-$t$ value of having received this recovery. Specifically:

    $$
    Z(\tau) = R(\tau) \cdot e^{\int_\tau^t r_s\,ds}
    $$

    in the simplest case where recovery is reinvested at the risk-free rate, or

    $$
    Z(\tau) = R(\tau) \cdot \frac{B_t}{B_\tau}
    $$

    where $B_t$ is the money market account.

    Common recovery models map to specific forms of $Z$:

    - **Recovery of face value (RFV):** $R(\tau) = \delta$ (fixed fraction), so $Z(\tau) = \delta \cdot B_t / B_\tau$
    - **Recovery of treasury (RT):** $R(\tau) = \delta \cdot P(\tau, T)$, so $Z(\tau) = \delta \cdot P(\tau, T) \cdot B_t / B_\tau$
    - **Recovery of market value (RMV):** $R(\tau) = \delta \cdot V_{\tau-}$, requiring the pre-default value just before default

    The dependence of $Z$ on $\tau$ (not just on $t$) reflects that recovery terms, accrued interest, and reinvestment depend on when exactly default occurred within $[0, t]$. $\square$

---

**Exercise 4.** Explain why initial enlargement corresponds to "insider information" in the context of credit risk. A trader who knows the exact default time $\tau$ in advance can construct arbitrage strategies. Describe one such strategy for a CDS contract and explain why the no-arbitrage principle fails under initial enlargement without appropriate measure changes.

??? success "Solution to Exercise 4"

    **Why initial enlargement corresponds to insider information.**

    Under initial enlargement, the filtration is $\mathcal{G}_t^{\text{init}} = \mathcal{F}_t \vee \sigma(\tau)$, meaning the agent knows $\tau$ at time 0. In credit markets, this is equivalent to an insider who knows in advance exactly when a firm will default. This is strictly more information than any market participant has, and it creates opportunities to trade on this foreknowledge.

    **An arbitrage strategy using a CDS contract.**

    Consider a Credit Default Swap (CDS) with maturity $T$ on a reference entity whose default time is $\tau$.

    - The CDS protection buyer pays a periodic premium $c$ (the CDS spread) and receives a payment of $(1 - R)$ (loss given default) if $\tau \le T$.
    - The CDS is fairly priced at inception: the expected present value of premium payments equals the expected present value of the default leg.

    **Insider's strategy:**

    *Case 1: The insider knows $\tau > T$ (no default before maturity).*

    The insider **sells CDS protection** (receives the premium leg). She collects premium payments $c$ at each payment date and never has to pay the default leg. The CDS was priced assuming a positive default probability, so the premium reflects compensation for default risk that will never materialize. The insider earns a risk-free profit equal to the present value of all premium payments.

    *Case 2: The insider knows $\tau = t^* \le T$ (default at known time $t^*$).*

    The insider **buys CDS protection** just before $t^*$ (or at inception if the spread is favorable). She pays a small amount of premium before $t^*$ and receives the large default payment $(1 - R)$ at $\tau = t^*$. If she times the purchase close to $t^*$, the premium cost is negligible relative to the payout. Alternatively, she can also short the defaultable bond just before $t^*$.

    In either case, the insider constructs a strategy with positive expected payoff and zero risk — a clear arbitrage.

    **Why no-arbitrage fails without measure changes.**

    The Fundamental Theorem of Asset Pricing requires that there exists an equivalent martingale measure under which discounted prices are martingales with respect to the trading filtration. Under $\mathcal{G}^{\text{init}}$, the CDS spread process is not a $\mathcal{G}^{\text{init}}$-semimartingale (in general) because the insider's information creates discontinuities in conditional expectations.

    More formally, the original risk-neutral measure $\mathbb{Q}$ (constructed for $\mathcal{F}_t$-adapted trading) is typically not an equivalent martingale measure for $\mathcal{G}_t^{\text{init}}$-adapted strategies. To restore no-arbitrage in the enlarged filtration, one must:

    1. Apply Jacod's absolute continuity condition to ensure semimartingale preservation
    2. Perform a **measure change** (Girsanov-type transformation) to absorb the informational drift into a new probability measure
    3. Restrict the class of admissible strategies to prevent unbounded information exploitation

    The measure change introduces an additional drift that exactly offsets the insider's informational advantage, restoring fair pricing. Without this adjustment, the original $\mathbb{Q}$ allows arbitrage under $\mathcal{G}^{\text{init}}$-adapted trading. This is the mathematical formalization of why insider trading (with perfect information about default timing) is incompatible with standard no-arbitrage pricing. $\square$

---

**Exercise 5.** Under progressive enlargement with the density hypothesis, an $\mathcal{F}$-semimartingale $X_t$ decomposes as

$$
X_t = \tilde{X}_t + \int_0^{t \wedge \tau} \frac{d\langle X, G\rangle_s}{G_{s-}}
$$

For $X_t = W_t$ (a standard Brownian motion) and $G_t = e^{-\lambda t}$ (constant intensity), compute the drift correction. Show that $W_t$ remains a $\mathcal{G}$-martingale, confirming immersion.

??? success "Solution to Exercise 5"

    **Setup.** We have $X_t = W_t$ (standard $\mathcal{F}$-Brownian motion) and $G_t = e^{-\lambda t}$ for constant intensity $\lambda > 0$. We need to compute the drift correction in the decomposition:

    $$
    W_t = \tilde{W}_t + \int_0^{t \wedge \tau} \frac{d\langle W, G\rangle_s}{G_{s-}}
    $$

    **Step 1: Compute $dG_t$.**

    Since $G_t = e^{-\lambda t}$ with constant $\lambda$:

    $$
    dG_t = -\lambda e^{-\lambda t}\,dt = -\lambda G_t\,dt
    $$

    This is a deterministic, absolutely continuous (bounded variation) process. There is no stochastic (martingale) component in $G$.

    **Step 2: Compute $\langle W, G \rangle_t$.**

    The predictable quadratic covariation $\langle W, G \rangle$ between a continuous martingale $W$ and a bounded variation process $G$ is zero. This follows from the definition: $\langle W, G \rangle$ is the unique predictable process such that $WG - \langle W, G \rangle$ is a local martingale. Since $G$ is deterministic (bounded variation), the product $W_t G_t$ is already a semimartingale whose finite variation part involves only $\int W_s\,dG_s + \int G_s\,dW_s$ (by integration by parts), and the cross term is:

    $$
    \langle W, G \rangle_t = 0
    $$

    More directly: $G_t$ has zero quadratic variation (it is $C^1$ and deterministic), so any covariation with $W$ vanishes.

    **Step 3: Evaluate the drift correction.**

    $$
    \int_0^{t \wedge \tau} \frac{d\langle W, G\rangle_s}{G_{s-}} = \int_0^{t \wedge \tau} \frac{0}{G_{s-}} = 0
    $$

    **Step 4: Conclusion.**

    The decomposition becomes:

    $$
    W_t = \tilde{W}_t + 0 = \tilde{W}_t
    $$

    So $W_t$ is itself a $\mathcal{G}$-martingale — no drift correction is needed. This confirms the **immersion property**: the $\mathcal{F}$-Brownian motion $W_t$ remains a $\mathcal{G}$-martingale (in fact, a $\mathcal{G}$-Brownian motion) after progressive enlargement.

    **Interpretation.** The drift correction vanishes because $G_t = e^{-\lambda t}$ is deterministic, reflecting the fact that default risk (governed by constant $\lambda$) is independent of the Brownian motion driving market prices. There is no covariation between the market factor $W$ and the survival probability $G$, so observing default provides no information about the Brownian motion's future behavior. $\square$

---

**Exercise 6.** Jacod's criterion states that $\mathcal{F}$-semimartingales remain $\mathcal{G}^{\text{init}}$-semimartingales if the conditional law of $\tau$ given $\mathcal{F}_\infty$ is absolutely continuous. Give an example of a default time $\tau$ for which this condition fails (hint: consider $\tau$ that is $\mathcal{F}_\infty$-measurable). Explain why semimartingale preservation breaks down in this case.

??? success "Solution to Exercise 6"

    **The task:** Find a default time $\tau$ for which Jacod's absolute continuity condition fails, and explain why semimartingale preservation breaks down.

    **Example: $\tau$ is $\mathcal{F}_\infty$-measurable.**

    Let $W_t$ be a standard Brownian motion generating $\mathcal{F}_t$, and define:

    $$
    \tau = \inf\{t \ge 0 : W_t = 1\}
    $$

    the first hitting time of level 1. This is an $\mathcal{F}$-stopping time, hence $\tau$ is $\mathcal{F}_\infty$-measurable (in fact, $\tau$ is $\mathcal{F}_\tau$-measurable).

    **Step 1: Check Jacod's condition.**

    Jacod's criterion requires that the conditional law of $\tau$ given $\mathcal{F}_\infty$ is absolutely continuous with respect to some $\sigma$-finite measure $\eta$ on $(\mathbb{R}_+, \mathcal{B}(\mathbb{R}_+))$:

    $$
    \mathbb{P}(\tau \in \cdot \mid \mathcal{F}_\infty) \ll \eta
    $$

    Since $\tau$ is $\mathcal{F}_\infty$-measurable, the conditional law of $\tau$ given $\mathcal{F}_\infty$ is a **Dirac mass**:

    $$
    \mathbb{P}(\tau \in A \mid \mathcal{F}_\infty) = \delta_{\tau(\omega)}(A) = \mathbf{1}_{\{\tau(\omega) \in A\}}
    $$

    A Dirac mass $\delta_x$ is **not** absolutely continuous with respect to Lebesgue measure (or any diffuse $\sigma$-finite measure), because $\delta_x(\{x\}) = 1$ while $\eta(\{x\}) = 0$ for any diffuse $\eta$. Jacod's condition fails.

    **Step 2: Why semimartingale preservation breaks down.**

    Under initial enlargement with $\mathcal{G}_t^{\text{init}} = \mathcal{F}_t \vee \sigma(\tau)$, knowing $\tau$ in advance means knowing that $W_t$ will hit level 1 at the precise time $\tau$. Consider the Brownian motion $W_t$ as an $\mathcal{F}$-semimartingale (in fact, a martingale).

    In the enlarged filtration, one can define the process:

    $$
    A_t = \frac{1 - W_t}{\tau - t} \quad \text{for } t < \tau
    $$

    which represents the "required drift" for $W$ to reach level 1 at time $\tau$. This quantity is $\mathcal{G}_t^{\text{init}}$-adapted (since $\tau$ is known). The Brownian motion $W_t$ should decompose into a $\mathcal{G}$-martingale plus a drift involving this term. Formally, under initial enlargement with $\tau$ being a hitting time, the decomposition would require:

    $$
    W_t = \tilde{W}_t + \int_0^t \frac{1 - W_s}{\tau - s}\,ds
    $$

    where $\tilde{W}$ is a $\mathcal{G}$-martingale (this is the Brownian bridge decomposition). However, the integral $\int_0^t \frac{1 - W_s}{\tau - s}\,ds$ **diverges** as $t \to \tau$ because the denominator $\tau - s \to 0$ while the numerator $1 - W_s \to 0$ (since $W_\tau = 1$), but the rate of convergence is not fast enough to ensure integrability in all cases.

    More fundamentally, the issue is that knowing $\tau$ (an $\mathcal{F}$-stopping time) provides so much information about the path of $W$ that the semimartingale structure cannot be preserved under any equivalent measure. The filtration $\mathcal{G}^{\text{init}}$ is "too large" — it contains predictable information about the martingale's future, creating singularities in the Radon–Nikodym density process that would be needed for a Girsanov-type transformation.

    In terms of the general theory, when $\tau$ is $\mathcal{F}_\infty$-measurable, the initial enlargement $\mathcal{F}_t \vee \sigma(\tau)$ is equivalent to giving an insider knowledge of a functional of the entire path. The Dirac nature of the conditional law means there is no "smoothing" that would allow the information to be absorbed into a drift correction, and the fundamental semimartingale property — which underlies all of stochastic calculus and no-arbitrage pricing — breaks down. $\square$
