# Immersion (H-Hypothesis)

The **immersion property**, also known as the **H-hypothesis** or **(H)-hypothesis**, is a fundamental assumption in credit risk models that ensures martingales under the original filtration remain martingales after enlargement. This property dramatically simplifies pricing and hedging in the presence of default.

---

## Definition of Immersion

### Formal Statement

Given a filtration $(\mathcal{F}_t)$ and an enlargement $(\mathcal{G}_t)$ with $\mathcal{F}_t \subseteq \mathcal{G}_t$, the **immersion property** (or **H-hypothesis**) holds if:

> Every $(\mathcal{F}_t, \mathbb{Q})$-martingale is also a $(\mathcal{G}_t, \mathbb{Q})$-martingale.

Equivalently, for any $\mathcal{F}$-martingale $M$ and any $t \ge 0$:

$$
\mathbb{E}[M_\infty \mid \mathcal{G}_t] = \mathbb{E}[M_\infty \mid \mathcal{F}_t] = M_t
$$

### Interpretation

Immersion means that **default does not reveal information about market factors**. Knowing whether and when default occurred does not help predict future values of market processes. The additional information in $\mathcal{G}_t$ beyond $\mathcal{F}_t$ is "orthogonal" to the martingale structure of market prices.

---

## Why Immersion Matters

### Preservation of No-Arbitrage

In financial models, discounted asset prices are martingales under the risk-neutral measure. If immersion holds:

1. Market asset prices remain martingales after including default information
2. No additional drift terms appear due to filtration enlargement
3. The original risk-neutral measure extends naturally to $(\mathcal{G}_t)$
4. Arbitrage-free pricing remains valid in the enlarged setting

Without immersion, default could signal information about future asset prices, creating potential arbitrage opportunities or requiring measure adjustments.

### Tractability of Pricing

Under immersion, pricing defaultable claims simplifies dramatically. For a defaultable claim with payoff $X$ at time $T$:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} X \mid \mathcal{G}_t\right]
$$

decomposes cleanly into pre-default and post-default values without complex cross-terms.

---

## Equivalent Characterizations

The H-hypothesis admits several equivalent formulations:

### Conditional Independence Characterization

Immersion holds if and only if for all $t \ge 0$ and all $A \in \mathcal{F}_\infty$:

$$
\mathbb{P}(A \mid \mathcal{G}_t) = \mathbb{P}(A \mid \mathcal{F}_t)
$$

This says that default information $\mathcal{H}_t = \sigma(\tau \wedge t)$ is **conditionally independent** of $\mathcal{F}_\infty$ given $\mathcal{F}_t$.

### Tower Property Version

For any integrable $\mathcal{F}_\infty$-measurable $X$:

$$
\mathbb{E}[X \mid \mathcal{G}_t] = \mathbb{E}[X \mid \mathcal{F}_t]
$$

### Density Hypothesis Formulation

Under the density hypothesis, immersion is equivalent to: for all $s \ge t$,

$$
\alpha_s^u = \mathbb{E}[\alpha_s^u \mid \mathcal{F}_t] \cdot \frac{\alpha_t^u}{G_t}
$$

where $\alpha_t^u$ is the conditional density of $\tau$ given $\mathcal{F}_t$.

---

## Immersion and Intensity Models

### Natural Satisfaction in Reduced-Form Models

Recall (see [Stopping Times and Enlargement of Filtration](stopping_times_and_enlargement_of_filtration.md)): in the Cox construction with $\mathcal{F}_t$-adapted intensity $\lambda_t$ and an independent exponential trigger $E \perp \mathcal{F}_\infty$, immersion holds because the only "new" randomness in $\tau$ is orthogonal to all market information.

### Mathematical Verification

Under the Cox construction, for any $\mathcal{F}$-martingale $M$:

$$
\mathbb{E}[M_T \mid \mathcal{G}_t] = \mathbb{E}[M_T \mid \mathcal{F}_t, \tau \wedge t, \mathbf{1}_{\{\tau > t\}}]
$$

The key insight is that on $\{\tau > t\}$, the only additional information is that $E > \Lambda_t = \int_0^t \lambda_s ds$. Since $E$ is independent of $\mathcal{F}_\infty$, this event carries no information about $M_T$ beyond what $\mathcal{F}_t$ contains.

Therefore: $\mathbb{E}[M_T \mid \mathcal{G}_t] = \mathbb{E}[M_T \mid \mathcal{F}_t] = M_t$.

---

## Consequences for Pricing

### Pre-Default Pricing Formula

Under immersion, the price of a defaultable claim paying $X$ at maturity $T$ (if no default) factors as $V_t = \mathbf{1}_{\{\tau > t\}}\,\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T (r_s + \lambda_s)\,ds}\,X \mid \mathcal{F}_t]$, and zero-recovery bonds decompose as $P^d(t,T) = P(t,T) \cdot S(t,T)$ — full derivation in [§ Pricing with Default Risk](../pricing_with_default_risk/defaultable_bonds.md).

---

## When Immersion Fails

### Structural Models

In structural (Merton-type) models, immersion typically **does not hold** because default is a hitting time of an $\mathcal{F}$-adapted firm-value process (see [§ Structural Credit Risk Models](../structural_credit_risk_models/black_cox_model.md)), so observing default reveals information about the path of correlated market observables: $\mathbb{E}[S_T \mid \mathcal{G}_t] \ne \mathbb{E}[S_T \mid \mathcal{F}_t]$.

### Information-Based Models

When default conveys information about underlying economic states:

- Credit events may signal broader market stress
- Contagion effects create information spillovers
- Regime switches may be partially revealed by defaults

In these cases, additional **compensator terms** are needed to maintain martingale properties.

### Mathematical Consequences

When immersion fails, for an $\mathcal{F}$-martingale $M$:

$$
M_t = \tilde{M}_t + \int_0^{t \wedge \tau} \frac{d\langle M, G \rangle_s}{G_{s-}}
$$

where $\tilde{M}$ is a $\mathcal{G}$-martingale and the integral term is the **drift correction** due to filtration enlargement. This additional term:

- Complicates pricing formulas
- Couples default risk with market dynamics
- Requires explicit modeling of the covariance $\langle M, G \rangle$

---

## Testing Immersion

### Sufficient Conditions

Immersion holds if any of the following are satisfied:

1. **Independence:** $\tau$ is independent of $\mathcal{F}_\infty$
2. **Cox construction:** $\tau$ is constructed via doubly-stochastic mechanism
3. **Conditional independence:** $\sigma(\tau)$ and $\mathcal{F}_\infty$ are conditionally independent given $\mathcal{F}_t$ for all $t$

### Necessary Conditions

If immersion holds, then:

- $\mathcal{F}$-Brownian motions remain $\mathcal{G}$-Brownian motions
- $\mathcal{F}$-Poisson processes remain $\mathcal{G}$-Poisson processes (with same intensity)
- Predictable representations are preserved

---

## Immersion vs. Avoiding Property

A related but weaker condition is the **avoiding property** (or avoidance of $\mathcal{F}$-stopping times):

> $\tau$ avoids $\mathcal{F}$-stopping times if $\mathbb{P}(\tau = S) = 0$ for all $\mathcal{F}$-stopping times $S$.

Under the density hypothesis:

- Avoidance is weaker than immersion
- Avoidance ensures $\tau$ is totally inaccessible
- Immersion implies avoidance but not conversely

---

## Practical Implications

### Model Selection

Choose models based on the economic context:

| Scenario | Immersion Status | Recommended Model |
|----------|------------------|-------------------|
| Pure credit event, independent of market | Holds | Reduced-form |
| Default driven by firm value | Fails | Structural |
| Credit-equity correlation | May fail | Hybrid |
| Contagion/systemic risk | Fails | Extended reduced-form |

### Hedging Under Immersion

When immersion holds:

- Delta hedging with market instruments is straightforward
- Credit risk is hedged via CDS or default-contingent strategies
- No cross-hedging between market and credit risks is needed

When immersion fails:

- Market hedges must account for default correlation
- Hedging errors arise from ignoring drift corrections
- Model risk increases substantially

---

## Key Takeaways

- Immersion (H-hypothesis) ensures $\mathcal{F}$-martingales remain $\mathcal{G}$-martingales after enlargement
- It holds naturally in reduced-form models with Cox process construction
- Immersion enables clean separation of market and credit risk in pricing
- Structural models typically violate immersion due to firm value linkages
- When immersion fails, drift corrections are needed for proper pricing
- The choice between immersion-compatible models depends on economic modeling goals

---

## Further Reading

- Jeanblanc, M., & Le Cam, Y. (2009). Progressive enlargement of filtrations with initial times. *Stochastic Processes and their Applications*, 119(8), 2523–2543.
- Brémaud, P., & Yor, M. (1978). Changes of filtrations and of probability measures. *Zeitschrift für Wahrscheinlichkeitstheorie*, 45, 269–295.
- Elliott, R. J., Jeanblanc, M., & Yor, M. (2000). On models of default risk. *Mathematical Finance*, 10(2), 179–195.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 6.

---

## Exercises

**Exercise 1.** Let $M_t$ be an $(\mathcal{F}_t, \mathbb{Q})$-martingale and let $\tau$ be a default time constructed via the Cox process with $\mathcal{F}_t$-adapted intensity $\lambda_t$ and an independent exponential trigger $E$. Verify the immersion property by showing $\mathbb{E}[M_T \mid \mathcal{G}_t] = M_t$ on the event $\{\tau > t\}$, using the independence of $E$ from $\mathcal{F}_\infty$.

??? success "Solution to Exercise 1"

    We need to show $\mathbb{E}[M_T \mid \mathcal{G}_t] = M_t$ on $\{\tau > t\}$ under the Cox process construction.

    **Setup.** Under the Cox construction, $\tau = \inf\{t : \Lambda_t \ge E\}$ where $\Lambda_t = \int_0^t \lambda_s\,ds$ is $\mathcal{F}_t$-adapted and $E \sim \text{Exp}(1)$ is independent of $\mathcal{F}_\infty$. The enlarged filtration is $\mathcal{G}_t = \mathcal{F}_t \vee \sigma(\tau \wedge t)$.

    **Step 1: Identify the conditioning information on $\{\tau > t\}$.**

    On the event $\{\tau > t\}$, we know that default has not occurred, which means $E > \Lambda_t$. So the additional information in $\mathcal{G}_t$ beyond $\mathcal{F}_t$ on this event is precisely the knowledge that $E > \Lambda_t$. We can write:

    $$
    \mathbb{E}[M_T \mid \mathcal{G}_t]\,\mathbf{1}_{\{\tau > t\}} = \mathbb{E}[M_T \mid \mathcal{F}_t,\, E > \Lambda_t]\,\mathbf{1}_{\{\tau > t\}}
    $$

    **Step 2: Use independence of $E$ from $\mathcal{F}_\infty$.**

    Since $M_T$ is $\mathcal{F}_T$-measurable (hence $\mathcal{F}_\infty$-measurable) and $E$ is independent of $\mathcal{F}_\infty$, the event $\{E > \Lambda_t\}$ — while involving $\Lambda_t$ which is $\mathcal{F}_t$-measurable — carries no additional information about $M_T$ beyond what $\mathcal{F}_t$ already provides. More precisely, conditionally on $\mathcal{F}_t$, the value $\Lambda_t$ is known, so $\{E > \Lambda_t\}$ becomes a fixed event about $E$ alone. Since $E \perp \mathcal{F}_\infty$, knowing $\{E > \Lambda_t\}$ does not affect the conditional distribution of $M_T$ given $\mathcal{F}_t$:

    $$
    \mathbb{E}[M_T \mid \mathcal{F}_t,\, E > \Lambda_t] = \mathbb{E}[M_T \mid \mathcal{F}_t]
    $$

    **Step 3: Apply the martingale property.**

    Since $M$ is an $(\mathcal{F}_t, \mathbb{Q})$-martingale:

    $$
    \mathbb{E}[M_T \mid \mathcal{F}_t] = M_t
    $$

    **Step 4: Combine.**

    Therefore on $\{\tau > t\}$:

    $$
    \mathbb{E}[M_T \mid \mathcal{G}_t] = \mathbb{E}[M_T \mid \mathcal{F}_t] = M_t
    $$

    This confirms the immersion property on the pre-default event. A similar (simpler) argument applies on $\{\tau \le t\}$, where the exact value of $\tau$ is known but is still a function of $E$ and the $\mathcal{F}$-adapted path of $\Lambda$, so independence again ensures that $M_T$'s conditional expectation is unaffected. $\square$

---

**Exercise 2.** In a structural model where default occurs when firm value $V_t$ hits a barrier $B$, explain why immersion typically fails. Specifically, construct an $\mathcal{F}$-martingale $M_t$ (e.g., a function of $V_t$) and show that observing the event $\{\tau \le t\}$ changes the conditional expectation $\mathbb{E}[M_T \mid \mathcal{G}_t] \neq M_t$.

??? success "Solution to Exercise 2"

    **Setup.** In a structural model, the firm value $V_t$ follows a geometric Brownian motion (or similar diffusion), and default occurs at $\tau = \inf\{t \ge 0 : V_t \le B\}$ for some barrier $B > 0$. Crucially, $V_t$ is $\mathcal{F}_t$-adapted, so $\tau$ is an $\mathcal{F}$-stopping time.

    **Why immersion fails — intuitive argument.**

    Since default is determined by $V_t$ crossing $B$, observing that default has occurred ($\tau \le t$) reveals that $V_\tau = B$ and, more importantly, constrains the path of $V$ up to time $t$. If $V_t$ is correlated with (or equal to) other market prices, this creates informational feedback.

    **Concrete construction.** Let $V_t = V_0 e^{(r - \sigma^2/2)t + \sigma W_t}$ under $\mathbb{Q}$, and consider the $\mathcal{F}$-martingale $M_t = e^{-rt}V_t = V_0 e^{-\sigma^2 t/2 + \sigma W_t}$ (the discounted firm value).

    **Step 1: Compute on $\{\tau \le t\}$.**

    On the event $\{\tau \le t\}$, we know the firm value hit $B$ at some time before $t$. After hitting the barrier, $V$ continues to evolve (in models without immediate liquidation), but the path is constrained. Specifically, the conditional distribution of $V_T$ given $\{\tau \le t\}$ and $\mathcal{F}_t$ is simply determined by $V_t$ (Markov property). However, observing $\{\tau \le t\}$ constrains $V_t$ relative to its unconditional distribution.

    **Step 2: Show the inequality.**

    Consider $T > t$ and the conditional expectation:

    $$
    \mathbb{E}[M_T \mid \mathcal{G}_t, \tau \le t] = \mathbb{E}[e^{-rT}V_T \mid \mathcal{F}_t, \tau \le t]
    $$

    Since $M_t$ is an $\mathcal{F}$-martingale, $\mathbb{E}[M_T \mid \mathcal{F}_t] = M_t$ always holds. But the event $\{\tau \le t\}$ is $\mathcal{F}_t$-measurable (since $\tau$ is an $\mathcal{F}$-stopping time), so conditioning additionally on it restricts us to paths where $V$ hit $B$. Now consider the unconditional vs. conditional values:

    On $\{\tau \le t\}$, the firm value $V_t$ tends to be lower (it hit the barrier). The $\mathcal{F}$-martingale property says $\mathbb{E}[M_T \mid \mathcal{F}_t] = M_t$ regardless, but the key issue arises when we consider more general $\mathcal{F}$-martingales.

    **Step 3: A cleaner example.** Consider $M_t = \mathbb{P}(\tau > T \mid \mathcal{F}_t)$ for some fixed future $T > t$. This is an $\mathcal{F}$-martingale (by tower property). Now:

    - Under $\mathcal{G}_t$ on $\{\tau \le t\}$: $\mathbb{E}[M_T \mid \mathcal{G}_t] = \mathbb{P}(\tau > T \mid \mathcal{G}_t) = 0$ if we define default as permanent (absorbing barrier). But $M_t = \mathbb{P}(\tau > T \mid \mathcal{F}_t) > 0$ in general.

    Thus $\mathbb{E}[M_T \mid \mathcal{G}_t] = 0 \ne M_t$ on $\{\tau \le t\}$, and immersion fails.

    The deeper reason is that in structural models, $\tau$ is predictable (an $\mathcal{F}$-stopping time), so the default event is not a "surprise" — it is determined by market factors, creating an inextricable link between default and market information. $\square$

---

**Exercise 3.** Under immersion, the price of a zero-recovery defaultable bond paying 1 at $T$ if no default is

$$
P^d(t,T) = \mathbf{1}_{\{\tau > t\}} \cdot P(t,T) \cdot S(t,T)
$$

where $S(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T \lambda_s\,ds} \mid \mathcal{F}_t]$. Derive this formula starting from the general pricing expression $P^d(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}} \mid \mathcal{G}_t]$. Clearly indicate where the immersion property is used.

??? success "Solution to Exercise 3"

    **Starting point.** The general pricing expression for a zero-recovery defaultable bond is:

    $$
    P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}} \;\Big|\; \mathcal{G}_t\right]
    $$

    **Step 1: Restrict to the pre-default event.**

    On $\{\tau \le t\}$, the bond has already defaulted with zero recovery, so $P^d(t,T) = 0$. On $\{\tau > t\}$, we have $\{\tau > T\} \subseteq \{\tau > t\}$, so:

    $$
    P^d(t,T) = \mathbf{1}_{\{\tau > t\}} \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}} \;\Big|\; \mathcal{G}_t\right]
    $$

    **Step 2: Use the Cox construction for $\{\tau > T\}$.**

    Under the Cox process construction, $\tau > T$ if and only if $E > \Lambda_T = \int_0^T \lambda_s\,ds$. Since $\Lambda_T - \Lambda_t = \int_t^T \lambda_s\,ds$ is $\mathcal{F}_T$-measurable and $E$ is independent of $\mathcal{F}_\infty$:

    $$
    \mathbb{P}(\tau > T \mid \mathcal{F}_T, \tau > t) = \mathbb{P}(E > \Lambda_T \mid E > \Lambda_t, \mathcal{F}_T) = e^{-(\Lambda_T - \Lambda_t)} = e^{-\int_t^T \lambda_s\,ds}
    $$

    using the memoryless property of the exponential distribution, conditional on $\mathcal{F}_T$ (which determines $\Lambda_T$ and $\Lambda_t$).

    **Step 3: Apply immersion (key step).**

    By immersion, the conditional expectation over $\mathcal{G}_t$ of any $\mathcal{F}_\infty$-measurable quantity reduces to conditioning on $\mathcal{F}_t$. More precisely, on $\{\tau > t\}$:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}} \;\Big|\; \mathcal{G}_t\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,\mathbb{P}(\tau > T \mid \mathcal{F}_T, \tau > t) \;\Big|\; \mathcal{F}_t\right]
    $$

    **Immersion is used here**: the tower property through $\mathcal{F}_T$ and the replacement of $\mathcal{G}_t$-conditioning by $\mathcal{F}_t$-conditioning for $\mathcal{F}_\infty$-measurable random variables.

    **Step 4: Substitute and simplify.**

    Substituting the result from Step 2:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,e^{-\int_t^T \lambda_s\,ds} \;\Big|\; \mathcal{F}_t\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + \lambda_s)\,ds} \;\Big|\; \mathcal{F}_t\right]
    $$

    **Step 5: Factor the result.**

    If $r_t$ and $\lambda_t$ are independent (or more generally, using the tower property):

    $$
    P^d(t,T) = \mathbf{1}_{\{\tau > t\}} \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + \lambda_s)\,ds} \;\Big|\; \mathcal{F}_t\right]
    $$

    When $r$ and $\lambda$ are independent under $\mathbb{Q}$, this further factors as:

    $$
    P^d(t,T) = \mathbf{1}_{\{\tau > t\}} \cdot \underbrace{\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds} \;\Big|\; \mathcal{F}_t\right]}_{P(t,T)} \cdot \underbrace{\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T \lambda_s\,ds} \;\Big|\; \mathcal{F}_t\right]}_{S(t,T)}
    $$

    yielding the desired formula $P^d(t,T) = \mathbf{1}_{\{\tau > t\}} \cdot P(t,T) \cdot S(t,T)$.

    **Where immersion was used:** In Step 3, replacing $\mathbb{E}[\cdot \mid \mathcal{G}_t]$ with $\mathbb{E}[\cdot \mid \mathcal{F}_t]$ for quantities that are $\mathcal{F}_\infty$-measurable. Without immersion, the default indicator would not factor out cleanly, and a drift correction linking market and credit risk would appear. $\square$

---

**Exercise 4.** When immersion fails, an $\mathcal{F}$-martingale $M_t$ decomposes in the enlarged filtration $\mathcal{G}_t$ as

$$
M_t = \tilde{M}_t + \int_0^{t \wedge \tau} \frac{d\langle M, G\rangle_s}{G_{s-}}
$$

Explain the economic meaning of the drift correction term $\int_0^{t \wedge \tau} d\langle M, G\rangle_s / G_{s-}$. Why does this term vanish under the Cox construction?

??? success "Solution to Exercise 4"

    **The decomposition formula.** When immersion fails, an $\mathcal{F}$-martingale $M$ decomposes in $\mathcal{G}$ as:

    $$
    M_t = \tilde{M}_t + \int_0^{t \wedge \tau} \frac{d\langle M, G\rangle_s}{G_{s-}}
    $$

    where $\tilde{M}$ is a $\mathcal{G}$-martingale and $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$ is the Azema supermartingale.

    **Economic meaning of the drift correction.**

    The term $\int_0^{t \wedge \tau} \frac{d\langle M, G\rangle_s}{G_{s-}}$ represents the **information leakage from default to market factors**. Specifically:

    - $\langle M, G \rangle_s$ measures the instantaneous covariance between the market factor $M$ and the survival probability $G$. When $\langle M, G \rangle \ne 0$, movements in market prices are correlated with changes in default likelihood.
    - $1/G_{s-}$ acts as a scaling factor — when the survival probability is small (default is likely), each unit of covariance has a larger informational impact.
    - The integral runs only up to $t \wedge \tau$: the drift correction is active only before default. After default, the information has been fully revealed.

    Economically, this drift term captures the fact that in the enlarged filtration, market prices must be adjusted because observing survival (or default) provides information about future returns. An $\mathcal{F}$-martingale acquires a drift in $\mathcal{G}$ because conditioning on additional default information biases the expected future path.

    **Why this term vanishes under the Cox construction.**

    Under the Cox construction, $\tau = \inf\{t : \int_0^t \lambda_s\,ds \ge E\}$ with $E \sim \text{Exp}(1)$ independent of $\mathcal{F}_\infty$. The survival probability is:

    $$
    G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t) = \mathbb{P}\!\left(E > \int_0^t \lambda_s\,ds \;\Big|\; \mathcal{F}_t\right) = e^{-\int_0^t \lambda_s\,ds} = e^{-\Lambda_t}
    $$

    By Ito's formula:

    $$
    dG_t = -\lambda_t G_t\,dt
    $$

    This is a process of **bounded variation** (purely a $dt$ term with no $dW$ component). Consequently:

    $$
    d\langle M, G \rangle_t = 0
    $$

    because the predictable quadratic covariation between a continuous martingale $M$ and a bounded-variation process $G$ is zero. Since the integrand vanishes identically:

    $$
    \int_0^{t \wedge \tau} \frac{d\langle M, G\rangle_s}{G_{s-}} = 0
    $$

    and therefore $M_t = \tilde{M}_t$, confirming that $M$ remains a $\mathcal{G}$-martingale. This is precisely the immersion property. $\square$

---

**Exercise 5.** Suppose a credit model has two possible default intensities: $\lambda_t = 1\%$ (normal regime) and $\lambda_t = 5\%$ (stress regime), and the regime is correlated with equity returns. Does the immersion property hold? Justify your answer by examining whether default reveals information about the regime, and hence about future equity price dynamics.

??? success "Solution to Exercise 5"

    **Answer: No, immersion does not hold in this model.**

    **Step 1: Model setup.**

    Let $R_t \in \{\text{normal}, \text{stress}\}$ denote the regime at time $t$, with:

    - $\lambda_t = 1\%$ when $R_t = \text{normal}$
    - $\lambda_t = 5\%$ when $R_t = \text{stress}$

    The regime $R_t$ is correlated with equity returns, meaning the equity price process $S_t$ carries information about the current regime. Both $R_t$ and $S_t$ are $\mathcal{F}_t$-adapted.

    **Step 2: Default reveals regime information.**

    The default intensity $\lambda_t$ depends on the regime. Consequently, the **rate** at which defaults arrive differs across regimes. Observing a default event (especially at a particular time) provides statistical information about which regime was active.

    Specifically, by Bayes' theorem, after observing default at time $\tau$:

    $$
    \frac{\mathbb{P}(R_\tau = \text{stress} \mid \tau = t)}{\mathbb{P}(R_\tau = \text{normal} \mid \tau = t)} = \frac{\mathbb{P}(R_\tau = \text{stress})}{\mathbb{P}(R_\tau = \text{normal})} \cdot \frac{\lambda_{\text{stress}}}{\lambda_{\text{normal}}} = \frac{\mathbb{P}(R_\tau = \text{stress})}{\mathbb{P}(R_\tau = \text{normal})} \cdot \frac{5\%}{1\%}
    $$

    Default is five times more likely per unit time in the stress regime, so observing default strongly shifts the posterior toward the stress regime.

    **Step 3: Regime information affects equity dynamics.**

    Since the regime is correlated with equity returns, learning about the regime changes the conditional distribution of future equity prices. If the stress regime is associated with lower expected returns or higher volatility, then:

    $$
    \mathbb{E}[S_T \mid \mathcal{G}_t] \ne \mathbb{E}[S_T \mid \mathcal{F}_t]
    $$

    because $\mathcal{G}_t$ contains the additional information $\{\tau \le t\}$, which signals the stress regime, which in turn affects equity forecasts.

    **Step 4: Immersion fails.**

    For an $\mathcal{F}$-martingale $M_t$ related to equity prices, the conditional expectation given $\mathcal{G}_t$ acquires a drift correction. Default is not "orthogonal" to market factors — it reveals information about the economic regime, which feeds back into asset price dynamics. The information channel is:

    $$
    \text{Default event} \;\longrightarrow\; \text{Regime inference} \;\longrightarrow\; \text{Updated equity forecasts}
    $$

    This violates the core requirement of immersion that default information should not help predict future values of market processes.

    In terms of the mathematical criterion, immersion requires $\mathbb{E}[X \mid \mathcal{G}_t] = \mathbb{E}[X \mid \mathcal{F}_t]$ for all $\mathcal{F}_\infty$-measurable $X$, which fails here because the default event is informative about the regime state. $\square$

---

**Exercise 6.** List three sufficient conditions for the immersion property to hold. For each condition, provide a concrete credit risk model where it is naturally satisfied and explain why.

??? success "Solution to Exercise 6"

    **Condition 1: Independence of $\tau$ from $\mathcal{F}_\infty$.**

    If $\tau$ is independent of $\mathcal{F}_\infty$, then for any $\mathcal{F}_\infty$-measurable $X$:

    $$
    \mathbb{E}[X \mid \mathcal{G}_t] = \mathbb{E}[X \mid \mathcal{F}_t, \tau \wedge t] = \mathbb{E}[X \mid \mathcal{F}_t]
    $$

    since knowledge of $\tau \wedge t$ (derived from the independent $\tau$) provides no information about $\mathcal{F}_\infty$-measurable quantities beyond $\mathcal{F}_t$.

    **Concrete model:** A simple credit model where $\tau \sim \text{Exp}(\lambda)$ with constant intensity $\lambda$ and the equity price follows a geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t$ with $\tau$ independent of the Brownian motion $W$. This is the simplest reduced-form model: default arrives as a Poisson event completely unrelated to market dynamics. Immersion holds trivially because $\tau$ carries no information about $\mathcal{F}$-adapted processes.

    ---

    **Condition 2: Cox process (doubly-stochastic) construction.**

    Default is defined as $\tau = \inf\{t : \int_0^t \lambda_s\,ds \ge E\}$ where $\lambda_t$ is $\mathcal{F}_t$-adapted and $E \sim \text{Exp}(1)$ is independent of $\mathcal{F}_\infty$.

    **Concrete model:** The Lando (1998) intensity-based model where the default intensity is driven by macroeconomic factors:

    $$
    \lambda_t = \exp(\alpha + \beta X_t)
    $$

    with $X_t$ an $\mathcal{F}_t$-adapted factor (e.g., GDP growth, credit spread index) satisfying $dX_t = \kappa(\theta - X_t)\,dt + \eta\,dW_t$. Default is constructed via the Cox mechanism with an independent exponential trigger $E \perp \mathcal{F}_\infty$.

    Immersion holds because the only source of randomness in $\tau$ beyond $\mathcal{F}_\infty$ is the independent trigger $E$. Even though $\lambda_t$ depends on market factors, the actual default event conditional on the entire market history is determined by $E$, which is orthogonal to all market information. The survival probability $G_t = e^{-\Lambda_t}$ is of bounded variation, so $\langle M, G\rangle = 0$ for any $\mathcal{F}$-martingale $M$.

    ---

    **Condition 3: Conditional independence — $\sigma(\tau)$ and $\mathcal{F}_\infty$ are conditionally independent given $\mathcal{F}_t$ for all $t$.**

    This is the most general sufficient condition: for all $t \ge 0$, $A \in \sigma(\tau)$, and $B \in \mathcal{F}_\infty$:

    $$
    \mathbb{P}(A \cap B \mid \mathcal{F}_t) = \mathbb{P}(A \mid \mathcal{F}_t) \cdot \mathbb{P}(B \mid \mathcal{F}_t)
    $$

    **Concrete model:** A multi-name credit portfolio model where each name's default time $\tau_i$ is conditionally independent of market factors given a common factor $Y_t$ that is $\mathcal{F}_t$-adapted. Consider a single-name sub-model where $\tau$ has conditional survival probability:

    $$
    \mathbb{P}(\tau > s \mid \mathcal{F}_t) = \mathbb{E}\!\left[e^{-\int_0^s \lambda_u\,du} \;\Big|\; \mathcal{F}_t\right]
    $$

    with $\lambda_u = h(Y_u)$ for some function $h$, and $\tau$ is constructed so that conditionally on the path of $Y$, the default time is independent of all other $\mathcal{F}$-adapted processes (interest rates, equity, etc.). This conditional independence structure ensures that knowing whether $\tau$ has occurred does not update beliefs about $\mathcal{F}_\infty$-measurable quantities beyond the information already in $\mathcal{F}_t$.

    This encompasses models broader than the strict Cox construction — for instance, models where $\tau$'s conditional law given $\mathcal{F}_t$ evolves as a martingale but $\tau$ is not necessarily constructed via a single exponential trigger. $\square$
