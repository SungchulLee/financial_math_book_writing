# Conditional Risk Measures

**Conditional risk measures** quantify risk given the information available at a specific time. They form the building blocks of dynamic risk frameworks and enable adaptive, forward-looking risk management.

---

## Motivation

Static risk measures $\rho(X)$ assess risk unconditionally, assuming no prior information.

In practice:
- Risk is reassessed as new information arrives
- Market conditions evolve, affecting risk profiles
- Portfolio positions change dynamically

Conditional risk measures address these needs by making risk assessment **information-dependent**.

---

## Setup

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ be a filtered probability space where:

- $\Omega$ is the sample space
- $\mathcal{F}$ is the $\sigma$-algebra of all events
- $(\mathcal{F}_t)_{t \ge 0}$ is a filtration representing information flow
- $\mathbb{P}$ is the probability measure

A terminal loss $X \in L^\infty(\mathcal{F}_T)$ is $\mathcal{F}_T$-measurable (known at time $T$).

---

## Definition

A **conditional risk measure** at time $t \in [0, T]$ is a mapping:

$$
\rho_t: L^\infty(\mathcal{F}_T) \to L^\infty(\mathcal{F}_t)
$$

such that $\rho_t(X)$ is $\mathcal{F}_t$-measurable for each $X$.

**Interpretation:** 
- $\rho_t(X)(\omega)$ is the risk of terminal loss $X$ as assessed at time $t$ in state $\omega$
- Different realizations of $\mathcal{F}_t$ lead to different risk assessments

---

## Conditional Coherence Axioms

A conditional risk measure $\rho_t$ is **conditionally coherent** if it satisfies:

### Conditional Monotonicity
If $X \le Y$ a.s., then $\rho_t(X) \le \rho_t(Y)$ a.s.

### Conditional Translation Invariance
For any $\mathcal{F}_t$-measurable $m$:
$$
\rho_t(X + m) = \rho_t(X) + m \quad \text{a.s.}
$$

**Note:** The constant $m$ must be $\mathcal{F}_t$-measurable (known at time $t$).

### Conditional Positive Homogeneity
For any $\mathcal{F}_t$-measurable $\lambda > 0$:
$$
\rho_t(\lambda X) = \lambda \rho_t(X) \quad \text{a.s.}
$$

### Conditional Subadditivity
$$
\rho_t(X + Y) \le \rho_t(X) + \rho_t(Y) \quad \text{a.s.}
$$

---

## Conditional Convex Risk Measures

Relaxing positive homogeneity, a conditional risk measure is **conditionally convex** if:

For any $\mathcal{F}_t$-measurable $\lambda \in [0,1]$:
$$
\rho_t(\lambda X + (1-\lambda)Y) \le \lambda \rho_t(X) + (1-\lambda) \rho_t(Y) \quad \text{a.s.}
$$

This generalizes conditional coherence.

---

## Examples

### Conditional Expectation

The simplest conditional risk measure:
$$
\rho_t(X) = \mathbb{E}[X | \mathcal{F}_t]
$$

This is conditionally coherent but **risk-neutral** (no risk aversion).

### Conditional VaR

$$
\text{VaR}_\alpha^t(X) = \inf\{m \in L^\infty(\mathcal{F}_t) : \mathbb{P}(X \le m | \mathcal{F}_t) \ge \alpha\}
$$

The conditional $\alpha$-quantile of $X$ given $\mathcal{F}_t$.

**Warning:** Conditional VaR is NOT conditionally subadditive in general.

### Conditional ES

$$
\text{ES}_\alpha^t(X) = \mathbb{E}[X | X \ge \text{VaR}_\alpha^t(X), \mathcal{F}_t]
$$

Or using the integral representation:
$$
\text{ES}_\alpha^t(X) = \frac{1}{1-\alpha} \int_\alpha^1 \text{VaR}_u^t(X) \, du
$$

Conditional ES is conditionally coherent.

### Conditional Entropic Risk

$$
\rho_t^\gamma(X) = \frac{1}{\gamma} \log \mathbb{E}[e^{\gamma X} | \mathcal{F}_t]
$$

This is conditionally convex but not positively homogeneous.

---

## Dual Representation

Conditionally coherent risk measures admit a dual representation:

$$
\rho_t(X) = \operatorname{ess\,sup}_{\mathbb{Q} \in \mathcal{Q}_t} \mathbb{E}^\mathbb{Q}[X | \mathcal{F}_t]
$$

where $\mathcal{Q}_t$ is a set of probability measures equivalent to $\mathbb{P}$ on $\mathcal{F}_T$.

**Interpretation:** Risk is the worst-case conditional expectation over a set of "stress" measures.

For conditionally convex measures:
$$
\rho_t(X) = \operatorname{ess\,sup}_{\mathbb{Q}} \left\{ \mathbb{E}^\mathbb{Q}[X | \mathcal{F}_t] - \alpha_t(\mathbb{Q}) \right\}
$$

where $\alpha_t(\mathbb{Q})$ is a conditional penalty function.

---

## Normalization Properties

A conditional risk measure is **normalized** if:
$$
\rho_t(0) = 0 \quad \text{a.s.}
$$

Combined with translation invariance, this implies:
$$
\rho_t(c) = c \quad \text{for any } \mathcal{F}_t\text{-measurable } c
$$

---

## Relation to Static Measures

Static risk measures are special cases with **trivial information**:

$$
\rho = \rho_0 \quad \text{where } \mathcal{F}_0 = \{\emptyset, \Omega\}
$$

When $\mathcal{F}_0$ is trivial, $\rho_0(X)$ is a constant (a real number), recovering the static case.

---

## Dynamic Risk Measures

A **dynamic risk measure** is a family $(\rho_t)_{t \in [0,T]}$ of conditional risk measures.

Key requirements:
1. Each $\rho_t$ should be conditionally coherent (or convex)
2. The family should satisfy **time-consistency** (see [Time-Consistency](time_consistency.md))

**Composition:**
$$
\rho_{s,t}(X) := \rho_s(-\rho_t(X))
$$

represents the risk at time $s$ of a position evaluated at time $t$.

---

## Updating Risk Assessments

As information arrives, risk is updated:

**Before event:** $\rho_0(X) = 50$

**After observing $A \in \mathcal{F}_1$:**
$$
\rho_1(X)(\omega) = \begin{cases}
30 & \omega \in A \\
70 & \omega \in A^c
\end{cases}
$$

The conditional risk measure adapts to the realized state.

---

## Conditional Acceptance Sets

Define the **conditional acceptance set**:
$$
\mathcal{A}_t = \{X \in L^\infty(\mathcal{F}_T) : \rho_t(X) \le 0 \text{ a.s.}\}
$$

Properties:
- If $\rho_t$ is monotone: $X \le 0 \Rightarrow X \in \mathcal{A}_t$
- If $\rho_t$ is convex: $\mathcal{A}_t$ is convex
- If $\rho_t$ is coherent: $\mathcal{A}_t$ is a convex cone

**Reconstruction:** 
$$
\rho_t(X) = \operatorname{ess\,inf}\{m \in L^\infty(\mathcal{F}_t) : X - m \in \mathcal{A}_t\}
$$

---

## Relevance Property

A conditional risk measure is **relevant** if:
$$
X < 0 \text{ on } A \text{ (with } \mathbb{P}(A) > 0) \quad \Rightarrow \quad \rho_t(X) < 0 \text{ on } A
$$

Relevance ensures that strict improvements are recognized.

---

## Capital Allocation Under Conditional Risk

For a portfolio $X = \sum_i X_i$, the conditional capital allocation to unit $i$ is:

$$
\text{AC}_i^t = \mathbb{E}[X_i | X \ge \text{VaR}_\alpha^t(X), \mathcal{F}_t]
$$

for conditional ES, satisfying:
$$
\sum_i \text{AC}_i^t = \rho_t(X) \quad \text{a.s.}
$$

This enables **state-dependent capital allocation**.

---

## Practical Applications

### Real-Time Risk Management
Conditional risk measures enable intraday risk updates as market data arrives.

### Scenario-Dependent Capital
Capital requirements can depend on observed market conditions.

### Adaptive Hedging
Hedging strategies can be adjusted based on conditional risk assessments.

### Stress Testing
Conditional measures naturally incorporate stress scenarios as information.

---

## Key Takeaways

- Conditional risk measures map future losses to $\mathcal{F}_t$-measurable random variables
- They generalize static measures by incorporating available information
- Conditional coherence axioms are the natural extension of static coherence
- Conditional ES is coherent; conditional VaR generally is not
- Dual representations connect conditional risk to worst-case expectations
- Dynamic risk measures are families of conditional measures linked by consistency

---

## Further Reading

- Föllmer, H. & Penner, I. (2006), "Convex Risk Measures and the Dynamics of Their Penalty Functions"
- Detlefsen, K. & Scandolo, G. (2005), "Conditional and Dynamic Convex Risk Measures"
- Bion-Nadal, J. (2008), "Dynamic Risk Measures: Time Consistency and Risk Measures from BMO Martingales"
- Cheridito, P. & Kupper, M. (2011), "Composition of Time-Consistent Dynamic Monetary Risk Measures"
- McNeil, A., Frey, R., & Embrechts, P., *Quantitative Risk Management* (conditional ES discussion)
