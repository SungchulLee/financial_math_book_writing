# Time-Consistency

Dynamic risk measures extend static risk measures to a multi-period setting. **Time-consistency** is a fundamental requirement ensuring that risk assessments remain logically coherent as information evolves over time.

---

## Motivation

In a dynamic setting, risk is evaluated at multiple times $0 \le s < t \le T$.

Consider a risk manager who:
- At time $s$, ranks position $X$ as less risky than $Y$
- At time $t > s$, reverses this ranking

Such **preference reversals** create serious problems:
- Inconsistent capital allocation over time
- Gaming opportunities for traders
- Unstable risk limits

Time-consistency requires that rankings established at one time do not reverse at future times.

---

## Setup: Conditional Risk Measures

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ be a filtered probability space.

A **conditional risk measure** at time $t$ is a mapping:

$$
\rho_t: L^\infty(\mathcal{F}_T) \to L^\infty(\mathcal{F}_t)
$$

that assigns to each terminal loss $X$ an $\mathcal{F}_t$-measurable random variable $\rho_t(X)$.

**Interpretation:** $\rho_t(X)$ is the risk of $X$ as assessed at time $t$, given information $\mathcal{F}_t$.

---

## Definition of Time-Consistency

A family of conditional risk measures $(\rho_t)_{t \in [0,T]}$ is **time-consistent** if for all $s < t$ and all $X, Y \in L^\infty(\mathcal{F}_T)$:

$$
\rho_t(X) \le \rho_t(Y) \quad \text{a.s.} \quad \Rightarrow \quad \rho_s(X) \le \rho_s(Y) \quad \text{a.s.}
$$

**Interpretation:** If $X$ is considered less risky than $Y$ at time $t$, then this ranking must already hold at any earlier time $s$.

---

## The Recursive Formulation

Time-consistency is equivalent to a **recursive structure**:

$$
\rho_s(X) = \rho_s(-\rho_t(X)) \quad \text{for all } s < t
$$

**Interpretation:** The risk at time $s$ of a position $X$ equals the risk at time $s$ of the certain amount $-\rho_t(X)$ that would be needed at time $t$ to offset the risk.

This is the **tower property** for risk measures, analogous to the tower property of conditional expectation.

---

## Cocycle Property

For three times $r < s < t$, time-consistency implies the **cocycle condition**:

$$
\rho_r(X) = \rho_r(-\rho_s(-\rho_t(X)))
$$

More generally, risk assessments can be computed by backward induction through any sequence of intermediate times.

**Computational implication:** Multi-period risk can be computed by:
1. Start at terminal time $T$
2. Work backward, applying single-period risk measures recursively

---

## Time-Consistency of Conditional Expectation

The conditional expectation $\mathbb{E}_t[X] := \mathbb{E}[X | \mathcal{F}_t]$ is time-consistent by the **tower property**:

$$
\mathbb{E}_s[X] = \mathbb{E}_s[\mathbb{E}_t[X]]
$$

This serves as the prototype for time-consistent dynamic risk measures.

---

## Time-Consistency of VaR and ES

### Dynamic VaR

**Dynamic VaR is generally NOT time-consistent.**

**Counterexample:** Consider a two-period model where losses can take different paths. The conditional $\text{VaR}_{0.95}$ at $t=1$ may rank two positions one way, but the marginal distributions at $t=0$ may rank them differently.

The quantile operator does not satisfy the tower property.

### Dynamic ES

**ES can be made time-consistent** under suitable constructions.

Define recursively:
$$
\rho_t(X) = \text{ES}_\alpha(X | \mathcal{F}_t)
$$

with the recursive relationship:
$$
\rho_s(X) = \text{ES}_\alpha(-\rho_t(X) | \mathcal{F}_s)
$$

This construction, sometimes called **iterated ES** or **recursively defined ES**, is time-consistent.

**Caveat:** This is NOT the same as simply computing conditional ES at each time. The recursive definition alters the measure.

---

## Bellman Principle and Dynamic Programming

Time-consistency is equivalent to the **Bellman principle** in dynamic optimization:

> An optimal strategy from time $s$ remains optimal when reconsidered at time $t > s$.

For risk-averse dynamic optimization:
$$
\inf_{\pi} \rho_s\left[\int_s^T c_u \, du + X_T\right] = \inf_{\pi_s} \left\{ c_s + \rho_s\left[\inf_{\pi_{s+}} \rho_{s+}[\cdots]\right] \right\}
$$

Time-consistency ensures that solving the problem recursively (dynamic programming) yields the same solution as solving it globally.

---

## Economic Interpretation

Time-consistency has important economic implications:

### No Preference Reversals
An agent's ranking of alternatives does not flip as time passes (absent new information about the alternatives themselves).

### Stable Capital Allocation
Capital requirements computed at different times remain compatible.

### Coherent Dynamic Decisions
A policy deemed optimal today remains optimal tomorrow (given the same information).

### No Arbitrage Opportunities
Time-inconsistency can create quasi-arbitrage: taking positions that appear risk-free when evaluated at different times.

---

## Acceptance Sets and Time-Consistency

Define the **conditional acceptance set** at time $t$:

$$
\mathcal{A}_t = \{X \in L^\infty(\mathcal{F}_T) : \rho_t(X) \le 0\}
$$

Time-consistency is equivalent to the **stability condition**:

$$
\mathcal{A}_t \cap L^\infty(\mathcal{F}_s) = \mathcal{A}_s \cap L^\infty(\mathcal{F}_s) \quad \text{for } s < t
$$

If a position is acceptable at time $t$, it was already acceptable at time $s$.

---

## Representation via BSDEs

Time-consistent risk measures admit representation via **backward stochastic differential equations** (BSDEs).

A BSDE of the form:
$$
Y_t = X + \int_t^T g(s, Y_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$

defines a time-consistent risk measure $\rho_t(X) = Y_t$ provided the driver $g$ satisfies appropriate conditions.

**Key insight:** The recursive structure of BSDEs naturally encodes time-consistency.

See the [BSDE-Based Risk Measures](bsde_based_risk_measures.md) section for details.

---

## Weak vs Strong Time-Consistency

**Strong time-consistency** (as defined above) requires the recursive property to hold for all pairs of times.

**Weak time-consistency** only requires:
$$
\rho_0(X) \le \rho_0(Y) \quad \Rightarrow \quad \rho_t(X) \le \rho_t(Y) \text{ for all } t
$$

This is a weaker condition that may be more practical but provides fewer guarantees.

---

## Practical Implications

### Model Selection
When choosing dynamic risk measures, time-consistency should be a key criterion.

### Backtesting
Time-consistent measures enable coherent backtesting across horizons.

### Capital Planning
Multi-period capital adequacy assessments require time-consistency.

### Algorithmic Trading
Risk limits that are time-consistent prevent gaming through dynamic trading.

---

## Key Takeaways

- Time-consistency prevents preference reversals in dynamic risk assessment
- The recursive formulation $\rho_s(X) = \rho_s(-\rho_t(X))$ is the defining property
- Conditional expectation is time-consistent; VaR is not; ES can be constructed to be
- Time-consistency is equivalent to the Bellman principle in dynamic optimization
- BSDE-based risk measures are naturally time-consistent
- Without time-consistency, dynamic risk management becomes unstable

---

## Further Reading

- Artzner, P., Delbaen, F., Eber, J.-M., Heath, D., & Ku, H. (2007), "Coherent Multiperiod Risk Adjusted Values and Bellman's Principle"
- Föllmer, H. & Schied, A., *Stochastic Finance* (Chapter 11)
- Cheridito, P., Delbaen, F., & Kupper, M. (2006), "Dynamic Monetary Risk Measures for Bounded Discrete-Time Processes"
- Riedel, F. (2004), "Dynamic Coherent Risk Measures"
- Detlefsen, K. & Scandolo, G. (2005), "Conditional and Dynamic Convex Risk Measures"
