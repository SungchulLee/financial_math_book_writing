# Stopping Times and Enlargement of Filtration

Credit risk models represent default as a **random time** $\tau$. To incorporate default into a stochastic framework rigorously, one must understand stopping times and the enlargement of filtrations. This foundational machinery enables consistent pricing and hedging in the presence of default events.

---

## Filtrations and Information Flow

A filtration $(\mathcal{F}_t)_{t \ge 0}$ represents the information available up to time $t$. In default-free models, $\mathcal{F}_t$ typically contains information about market factors such as asset prices, interest rates, and other observable quantities. Formally, we require:

1. **Right-continuity:** $\mathcal{F}_t = \mathcal{F}_{t+} := \bigcap_{s > t} \mathcal{F}_s$
2. **Completeness:** $\mathcal{F}_0$ contains all $\mathbb{P}$-null sets

These are the **usual conditions** ensuring technical regularity.

Introducing default requires expanding this information set to include knowledge of whether default has occurred.

---

## Default Time as a Stopping Time

A random time $\tau: \Omega \to [0, \infty]$ is a **stopping time** with respect to a filtration $(\mathcal{G}_t)$ if

$$
\{\tau \le t\} \in \mathcal{G}_t \quad \text{for all } t \ge 0.
$$

Equivalently, under right-continuous filtrations, $\{\tau < t\} \in \mathcal{G}_t$ for all $t$.

**Interpretation:** At any time $t$, we can determine whether default has already occurred. This is the minimal requirement for default to be observable.

A stronger condition is **predictability**: $\tau$ is predictable if there exists an increasing sequence of stopping times $(\tau_n)$ with $\tau_n < \tau$ on $\{\tau > 0\}$ and $\tau_n \uparrow \tau$. In structural models, default is often predictable (hitting times of continuous processes). In reduced-form models, default is typically **totally inaccessible**—it cannot be anticipated by any announcing sequence.

---

## The Default Indicator Process

The **default indicator** is the process

$$
H_t := \mathbf{1}_{\{\tau \le t\}}.
$$

This is a right-continuous, non-decreasing process that jumps from 0 to 1 at the moment of default. Key properties:

- $H_t$ is $\mathcal{G}_t$-adapted when $\tau$ is a $(\mathcal{G}_t)$-stopping time
- $H_t$ is a **submartingale** (non-decreasing processes are always submartingales)
- The jump $\Delta H_\tau = 1$ occurs at a single random time

---

## Enlargement of Filtration

To model default within the existing market framework, we **enlarge** the default-free filtration $(\mathcal{F}_t)$ to a larger filtration $(\mathcal{G}_t)$ such that:

1. $\tau$ is a stopping time in $(\mathcal{G}_t)$
2. $\mathcal{F}_t \subseteq \mathcal{G}_t$ for all $t$

This process is known as **enlargement of filtration**. The enlarged filtration contains both market information and default information.

### Minimal Enlargement

The **minimal enlargement** making $\tau$ a stopping time is

$$
\mathcal{G}_t = \mathcal{F}_t \vee \mathcal{H}_t,
$$

where $\mathcal{H}_t = \sigma(H_s : s \le t) = \sigma(\mathbf{1}_{\{\tau \le s\}} : s \le t)$.

This can be written more explicitly as

$$
\mathcal{G}_t = \bigcap_{s > t} \left( \mathcal{F}_s \vee \sigma(\tau \wedge s) \right).
$$

Every $\mathcal{G}_t$-measurable random variable $X$ admits the representation

$$
X = X_0 \mathbf{1}_{\{\tau > t\}} + X_1(\tau) \mathbf{1}_{\{\tau \le t\}},
$$

where $X_0$ is $\mathcal{F}_t$-measurable and $X_1(s)$ is $\mathcal{F}_t \otimes \mathcal{B}([0,t])$-measurable.

---

## The Azéma Supermartingale

A fundamental object in the theory is the **Azéma supermartingale**:

$$
G_t := \mathbb{P}(\tau > t \mid \mathcal{F}_t).
$$

This process represents the conditional probability of survival given market information. Key properties:

1. $G_t$ is a **supermartingale** (survival probability cannot increase on average)
2. $G_0 = \mathbb{P}(\tau > 0)$ (typically 1 if default cannot occur instantly)
3. $G_t \to G_\infty = \mathbb{P}(\tau = \infty \mid \mathcal{F}_\infty)$ as $t \to \infty$

The Azéma supermartingale admits the **Doob-Meyer decomposition**:

$$
G_t = M_t - A_t,
$$

where $M_t$ is a martingale and $A_t$ is a predictable increasing process.

---

## Pre-Default and Post-Default Dynamics

The enlarged filtration naturally separates into pre-default and post-default regimes. For any $\mathcal{G}$-adapted process $X_t$:

$$
X_t = X_t^{\text{pre}} \mathbf{1}_{\{\tau > t\}} + X_t^{\text{post}} \mathbf{1}_{\{\tau \le t\}}.
$$

**Pre-default:** On $\{\tau > t\}$, the relevant information is $\mathcal{F}_t$ (market factors only).

**Post-default:** On $\{\tau \le t\}$, we additionally know the exact default time $\tau$.

This decomposition is crucial for pricing defaultable claims, where cashflows differ fundamentally before and after default.

---

## Financial Interpretation

Enlargement of filtration formalizes several key aspects of credit modeling:

1. **Information arrival:** Default news arrives at a random time, enriching the information set
2. **Observability:** Market participants observe default when it occurs (stopping time property)
3. **Pricing consistency:** Arbitrage-free pricing must account for the expanded information
4. **Hedging constraints:** Hedging strategies must be adapted to $(\mathcal{G}_t)$, not just $(\mathcal{F}_t)$

The mathematical framework ensures that pricing and hedging are internally consistent with the observed default events.

---

## Connection to Cox Process Construction

In reduced-form models, default is often constructed via a **doubly-stochastic** (Cox) process. Given an $\mathcal{F}$-adapted intensity process $\lambda_t \ge 0$, define

$$
\Lambda_t := \int_0^t \lambda_s \, ds
$$

and let $E \sim \text{Exp}(1)$ be independent of $\mathcal{F}_\infty$. The default time is

$$
\tau := \inf\{t \ge 0 : \Lambda_t \ge E\} = \Lambda^{-1}(E).
$$

Under this construction:
- $\tau$ is a totally inaccessible stopping time in $(\mathcal{G}_t)$
- The conditional survival probability is $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t) = e^{-\Lambda_t}$
- The Azéma supermartingale has an explicit form

This construction is the workhorse of intensity-based credit models.

---

## Key Takeaways

- Default is modeled as a random time $\tau$, which must be a stopping time for observability
- Filtration enlargement formally incorporates default information into the probability space
- The Azéma supermartingale $G_t = \mathbb{P}(\tau > t \mid \mathcal{F}_t)$ is central to the theory
- Pre-default and post-default dynamics are naturally separated
- The Cox process construction provides a canonical way to generate default times

---

## Further Reading

- Jeanblanc, M., Yor, M., & Chesney, M. (2009). *Mathematical Methods for Financial Markets*. Springer.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer.
- Protter, P. (2005). *Stochastic Integration and Differential Equations*. Springer.
- Jeulin, T. (1980). *Semi-martingales et grossissement d'une filtration*. Lecture Notes in Mathematics 833.
