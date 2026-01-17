# Immersion (H-Hypothesis)

The **immersion property**, also known as the **H-hypothesis** or **(H)-hypothesis**, is a fundamental assumption in credit risk models that ensures martingales under the original filtration remain martingales after enlargement. This property dramatically simplifies pricing and hedging in the presence of default.

---

## Definition of Immersion

### Formal Statement

Given a filtration $(\mathcal{F}_t)$ and an enlargement $(\mathcal{G}_t)$ with $\mathcal{F}_t \subseteq \mathcal{G}_t$, the **immersion property** (or **H-hypothesis**) holds if:

> Every $(\mathcal{F}_t, \mathbb{Q})$-martingale is also a $(\mathcal{G}_t, \mathbb{Q})$-martingale.

Equivalently, for any $\mathcal{F}$-martingale $M$ and any $t \ge 0$:

$$
\mathbb{E}[M_\infty \mid \mathcal{G}_t] = \mathbb{E}[M_\infty \mid \mathcal{F}_t] = M_t.
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
\mathbb{P}(A \mid \mathcal{G}_t) = \mathbb{P}(A \mid \mathcal{F}_t).
$$

This says that default information $\mathcal{H}_t = \sigma(\tau \wedge t)$ is **conditionally independent** of $\mathcal{F}_\infty$ given $\mathcal{F}_t$.

### Tower Property Version

For any integrable $\mathcal{F}_\infty$-measurable $X$:

$$
\mathbb{E}[X \mid \mathcal{G}_t] = \mathbb{E}[X \mid \mathcal{F}_t].
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

In canonical reduced-form (intensity-based) credit models, immersion holds by construction. The key mechanism is the **doubly-stochastic** (Cox process) construction:

1. Default intensity $\lambda_t$ is $\mathcal{F}_t$-adapted
2. Default time is $\tau = \inf\{t : \int_0^t \lambda_s ds \ge E\}$ where $E \sim \text{Exp}(1)$ is independent of $\mathcal{F}_\infty$
3. The independence of $E$ from market factors ensures immersion

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

Under immersion, the price of a defaultable claim paying $X$ at maturity $T$ (if no default) is:

$$
V_t = \mathbf{1}_{\{\tau > t\}} \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} X \mid \mathcal{F}_t\right].
$$

The default indicator $\mathbf{1}_{\{\tau > t\}}$ factors out cleanly because:
- The expectation over market factors uses $\mathcal{F}_t$-conditioning (immersion)
- Default risk enters only through the intensity adjustment $\lambda_s$

### Separation of Market and Credit Risk

Immersion enables a clean decomposition:

$$
\text{Defaultable Price} = \text{Default-Free Price} \times \text{Survival Adjustment}
$$

More precisely, for a zero-recovery defaultable bond:

$$
P^d(t,T) = P(t,T) \cdot S(t,T),
$$

where $P(t,T)$ is the default-free discount factor and $S(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t]$ is the survival probability.

---

## When Immersion Fails

### Structural Models

In structural (Merton-type) models, immersion typically **does not hold**. Default is triggered when firm value $V_t$ crosses a barrier, and $V_t$ is directly linked to market observables.

**Example:** If $V_t$ is correlated with equity prices $S_t$, then observing default (i.e., $V_\tau \le B$) reveals information about the path of $S$:

$$
\mathbb{E}[S_T \mid \mathcal{G}_t] \ne \mathbb{E}[S_T \mid \mathcal{F}_t]
$$

Default signals that firm value was low, which correlates with low equity values.

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
