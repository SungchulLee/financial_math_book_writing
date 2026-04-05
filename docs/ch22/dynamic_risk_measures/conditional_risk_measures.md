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

---

## Exercises

**Exercise 1.** Define the conditional Value-at-Risk $\text{VaR}_\alpha(X \mid \mathcal{F}_t)$ as the $\alpha$-quantile of the conditional loss distribution given $\mathcal{F}_t$. If portfolio loss $X$ given $\mathcal{F}_t$ is normally distributed with conditional mean $\mu_t$ and conditional variance $\sigma_t^2$, express $\text{VaR}_{0.99}(X \mid \mathcal{F}_t)$ in closed form.

??? success "Solution to Exercise 1"

    If $X \mid \mathcal{F}_t \sim N(\mu_t, \sigma_t^2)$, then the conditional quantile function (conditional VaR) at level $\alpha$ is:

    $$
    \text{VaR}_\alpha(X \mid \mathcal{F}_t) = \mu_t + \sigma_t \Phi^{-1}(\alpha)
    $$

    where $\Phi^{-1}$ is the quantile function of the standard normal distribution.

    For $\alpha = 0.99$, we have $\Phi^{-1}(0.99) = 2.3263$ (to four decimal places). Therefore:

    $$
    \text{VaR}_{0.99}(X \mid \mathcal{F}_t) = \mu_t + 2.3263\,\sigma_t
    $$

    **Interpretation.** Both $\mu_t$ and $\sigma_t$ are $\mathcal{F}_t$-measurable, meaning they are known at time $t$ and depend on the information available. The conditional VaR shifts with the conditional mean (location) and scales with the conditional volatility (dispersion). In high-volatility regimes (large $\sigma_t$), the VaR increases; in low-volatility regimes, it decreases. This adaptivity to current conditions is precisely the advantage of conditional risk measures over their static counterparts.

---

**Exercise 2.** Explain why a conditional risk measure must be $\mathcal{F}_t$-measurable. Give an economic example where a static (unconditional) risk measure gives misleading results because it ignores currently available information.

??? success "Solution to Exercise 2"

    **$\mathcal{F}_t$-measurability requirement.** A conditional risk measure $\rho_t(X)$ must be $\mathcal{F}_t$-measurable because it represents the risk assessment using only the information available at time $t$. Formally, $\rho_t: L^\infty(\mathcal{F}_T) \to L^\infty(\mathcal{F}_t)$ maps terminal losses to quantities that can be computed from $\mathcal{F}_t$-observable data. If $\rho_t(X)$ were not $\mathcal{F}_t$-measurable, it would require "future" information unavailable at time $t$, making it operationally meaningless for decision-making.

    **Economic example.** Consider a portfolio of equities where a risk manager computes the unconditional (static) $\text{VaR}_{0.99}$ using the full historical distribution. Suppose the portfolio has:

    - In calm markets (70% of the time): daily losses $\sim N(0, 1)$, so $\text{VaR}_{0.99} \approx 2.33$
    - In crisis markets (30% of the time): daily losses $\sim N(5, 9)$, so $\text{VaR}_{0.99} \approx 5 + 3 \times 2.33 = 11.99$

    The unconditional distribution is a mixture, and the unconditional $\text{VaR}_{0.99}$ (computed from the mixture) will be some intermediate value -- say approximately $7$.

    Now suppose the risk manager observes clear signs that the market has entered crisis mode (e.g., VIX has spiked, credit spreads have widened). The static VaR of $7$ is dangerously misleading:

    - It **underestimates** risk in the current crisis state, where the true conditional VaR is $\approx 12$.
    - It would **overestimate** risk in calm markets, where the true conditional VaR is $\approx 2.3$.

    By using the conditional risk measure $\text{VaR}_{0.99}(X \mid \mathcal{F}_t)$ that conditions on the current market regime, the risk manager obtains the correct state-dependent risk assessment. The static measure averages over regimes and fails to reflect the current environment.

---

**Exercise 3.** The conditional Expected Shortfall at level $\alpha$ is $\text{ES}_\alpha(X \mid \mathcal{F}_t) = \mathbb{E}[X \mid X \ge \text{VaR}_\alpha(X \mid \mathcal{F}_t), \mathcal{F}_t]$. Verify that conditional ES is a coherent conditional risk measure by checking (conditionally): monotonicity, translation invariance, positive homogeneity, and subadditivity.

??? success "Solution to Exercise 3"

    We verify each conditional coherence axiom for $\text{ES}_\alpha(X \mid \mathcal{F}_t) = \mathbb{E}[X \mid X \ge \text{VaR}_\alpha(X \mid \mathcal{F}_t), \mathcal{F}_t]$.

    Equivalently, using the integral representation:

    $$
    \text{ES}_\alpha(X \mid \mathcal{F}_t) = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(X \mid \mathcal{F}_t)\,du
    $$

    **Conditional monotonicity.** If $X \le Y$ a.s., then the conditional distribution of $X$ given $\mathcal{F}_t$ is stochastically dominated by that of $Y$. Hence for every $u \in [\alpha, 1]$:

    $$
    \text{VaR}_u(X \mid \mathcal{F}_t) \le \text{VaR}_u(Y \mid \mathcal{F}_t) \quad \text{a.s.}
    $$

    Integrating over $u \in [\alpha, 1]$ and dividing by $(1-\alpha)$:

    $$
    \text{ES}_\alpha(X \mid \mathcal{F}_t) \le \text{ES}_\alpha(Y \mid \mathcal{F}_t) \quad \text{a.s.}
    $$

    **Conditional translation invariance.** For $\mathcal{F}_t$-measurable $m$, since $m$ is a known constant given $\mathcal{F}_t$:

    $$
    \text{VaR}_u(X + m \mid \mathcal{F}_t) = \text{VaR}_u(X \mid \mathcal{F}_t) + m \quad \text{a.s.}
    $$

    Therefore:

    $$
    \text{ES}_\alpha(X + m \mid \mathcal{F}_t) = \frac{1}{1-\alpha}\int_\alpha^1 \left[\text{VaR}_u(X \mid \mathcal{F}_t) + m\right]du = \text{ES}_\alpha(X \mid \mathcal{F}_t) + m \quad \text{a.s.}
    $$

    **Conditional positive homogeneity.** For $\mathcal{F}_t$-measurable $\lambda > 0$:

    $$
    \text{VaR}_u(\lambda X \mid \mathcal{F}_t) = \lambda\,\text{VaR}_u(X \mid \mathcal{F}_t) \quad \text{a.s.}
    $$

    since $\lambda$ is a known positive constant given $\mathcal{F}_t$, and quantiles scale linearly with positive constants. Then:

    $$
    \text{ES}_\alpha(\lambda X \mid \mathcal{F}_t) = \frac{1}{1-\alpha}\int_\alpha^1 \lambda\,\text{VaR}_u(X \mid \mathcal{F}_t)\,du = \lambda\,\text{ES}_\alpha(X \mid \mathcal{F}_t) \quad \text{a.s.}
    $$

    **Conditional subadditivity.** This is the most delicate property. The key tool is the dual representation. Conditional ES can be written as:

    $$
    \text{ES}_\alpha(X \mid \mathcal{F}_t) = \sup_{\mathbb{Q} \in \mathcal{Q}_t} \mathbb{E}^{\mathbb{Q}}[X \mid \mathcal{F}_t]
    $$

    where $\mathcal{Q}_t = \{\mathbb{Q} \ll \mathbb{P} \mid \frac{d\mathbb{Q}}{d\mathbb{P}}\big|_{\mathcal{F}_T} \le \frac{1}{1-\alpha}\}$. Since the supremum of linear functions is subadditive:

    $$
    \text{ES}_\alpha(X + Y \mid \mathcal{F}_t) = \sup_{\mathbb{Q} \in \mathcal{Q}_t} \mathbb{E}^{\mathbb{Q}}[X + Y \mid \mathcal{F}_t]
    $$

    $$
    \le \sup_{\mathbb{Q} \in \mathcal{Q}_t} \mathbb{E}^{\mathbb{Q}}[X \mid \mathcal{F}_t] + \sup_{\mathbb{Q} \in \mathcal{Q}_t} \mathbb{E}^{\mathbb{Q}}[Y \mid \mathcal{F}_t]
    $$

    $$
    = \text{ES}_\alpha(X \mid \mathcal{F}_t) + \text{ES}_\alpha(Y \mid \mathcal{F}_t) \quad \text{a.s.}
    $$

    The inequality holds because the supremum over $\mathbb{Q}$ of a sum is at most the sum of the suprema (the maximizing $\mathbb{Q}$ may differ for $X$ and $Y$).

    Therefore conditional ES satisfies all four axioms and is a conditionally coherent risk measure.

---

**Exercise 4.** A portfolio's conditional loss distribution is modeled as $X_T \mid \mathcal{F}_t \sim N(\mu_t, \sigma_t^2)$ with $\mu_t = 100 + 0.5(S_t - 100)$ and $\sigma_t = 20$, where $S_t$ is the current stock price. Compute $\text{VaR}_{0.95}(X_T \mid \mathcal{F}_t)$ for $S_t = 90$ and $S_t = 110$. How does current market information change the risk assessment?

??? success "Solution to Exercise 4"

    For a conditional Gaussian loss $X_T \mid \mathcal{F}_t \sim N(\mu_t, \sigma_t^2)$ with $\mu_t = 100 + 0.5(S_t - 100)$ and $\sigma_t = 20$, the conditional VaR at level $\alpha = 0.95$ is:

    $$
    \text{VaR}_{0.95}(X_T \mid \mathcal{F}_t) = \mu_t + \sigma_t \Phi^{-1}(0.95) = \mu_t + 20 \times 1.6449
    $$

    $$
    = \mu_t + 32.90
    $$

    **Case $S_t = 90$:**

    $$
    \mu_t = 100 + 0.5(90 - 100) = 100 - 5 = 95
    $$

    $$
    \text{VaR}_{0.95}(X_T \mid \mathcal{F}_t) = 95 + 32.90 = 127.90
    $$

    **Case $S_t = 110$:**

    $$
    \mu_t = 100 + 0.5(110 - 100) = 100 + 5 = 105
    $$

    $$
    \text{VaR}_{0.95}(X_T \mid \mathcal{F}_t) = 105 + 32.90 = 137.90
    $$

    **How market information changes the risk assessment.** The conditional mean $\mu_t$ depends on the current stock price $S_t$ through the linear relationship $\mu_t = 100 + 0.5(S_t - 100)$. When $S_t = 90$ (stock has fallen), the expected loss is lower ($\mu_t = 95$), leading to a lower VaR of $127.90$. When $S_t = 110$ (stock has risen), the expected loss is higher ($\mu_t = 105$), leading to a higher VaR of $137.90$.

    This demonstrates how conditional risk measures adapt to current market conditions. The difference of $10$ in VaR between the two scenarios ($137.90 - 127.90 = 10$) arises entirely from the information contained in the current stock price. A static (unconditional) risk measure would assign a single number regardless of $S_t$, ignoring this relevant market signal. The conditional measure correctly adjusts capital requirements based on observable market state.

---

**Exercise 5.** Explain how conditional risk measures serve as building blocks for dynamic risk measures. Specifically, show how a sequence of conditional risk measures $\{\rho_t\}_{t=0}^T$ can be composed to define a time-consistent dynamic risk measure via backward recursion.

??? success "Solution to Exercise 5"

    **Conditional risk measures as building blocks.** A dynamic risk measure is a family $\{\rho_t\}_{t=0}^T$ of conditional risk measures, where each $\rho_t: L^\infty(\mathcal{F}_T) \to L^\infty(\mathcal{F}_t)$ assesses risk at time $t$.

    **Backward recursion for time-consistency.** The key insight is that time-consistency requires the recursive (tower-like) property:

    $$
    \rho_s(X) = \rho_s(-\rho_t(X)) \quad \text{for all } s < t
    $$

    This means the risk at an earlier time $s$ can be computed by first evaluating risk at a later time $t$, and then applying the earlier risk measure to the result.

    **Construction via backward recursion.** Given a family of one-step conditional risk measures $\{\rho_{t,t+1}\}$, we define:

    1. **Terminal condition:** $\rho_T(X) = X$ (at maturity, the risk is the loss itself).

    2. **Backward step:** For $t = T-1, T-2, \ldots, 0$:

    $$
    \rho_t(X) = \rho_{t,t+1}(-\rho_{t+1}(X))
    $$

    Here $\rho_{t,t+1}$ is a one-period conditional risk measure from time $t$ to $t+1$.

    **Why this is time-consistent.** By construction, for any $s < t$:

    $$
    \rho_s(X) = \rho_{s,s+1}(-\rho_{s+1}(-\rho_{s+2}(\cdots(-\rho_t(X))\cdots)))
    $$

    Now consider $\rho_s(-\rho_t(X))$: this applies the same backward recursion from $s$ to $t$ to the "terminal value" $\rho_t(X)$, yielding the exact same chain of compositions. Hence $\rho_s(X) = \rho_s(-\rho_t(X))$, which is precisely time-consistency.

    **Concrete example.** If $\rho_{t,t+1} = \text{ES}_\alpha(\cdot \mid \mathcal{F}_t)$ for each $t$, then:

    $$
    \rho_{T-1}(X) = \text{ES}_\alpha(X \mid \mathcal{F}_{T-1})
    $$

    $$
    \rho_{T-2}(X) = \text{ES}_\alpha(-\rho_{T-1}(X) \mid \mathcal{F}_{T-2}) = \text{ES}_\alpha(-\text{ES}_\alpha(X \mid \mathcal{F}_{T-1}) \mid \mathcal{F}_{T-2})
    $$

    and so on. This iterated ES construction is time-consistent. In contrast, defining $\rho_t(X) = \text{ES}_\alpha(X \mid \mathcal{F}_t)$ directly (without recursion) is in general **not** time-consistent, because $\text{ES}_\alpha(X \mid \mathcal{F}_s) \ne \text{ES}_\alpha(\text{ES}_\alpha(X \mid \mathcal{F}_t) \mid \mathcal{F}_s)$ -- the ES operator does not satisfy a tower property.

---

**Exercise 6.** In a two-period model ($t = 0, 1, 2$), a position has conditional distributions $X_2 \mid \mathcal{F}_1 \sim N(\mu_1, 1)$ where $\mu_1$ is $\mathcal{F}_1$-measurable. Compute $\rho_1(X_2) = \text{ES}_{0.95}(X_2 \mid \mathcal{F}_1)$ as a function of $\mu_1$. Then compute $\rho_0(X_2) = \text{ES}_{0.95}(\rho_1(X_2))$ and verify that the composition produces a time-consistent assessment.

??? success "Solution to Exercise 6"

    **Step 1: Compute $\rho_1(X_2) = \text{ES}_{0.95}(X_2 \mid \mathcal{F}_1)$.** Given $X_2 \mid \mathcal{F}_1 \sim N(\mu_1, 1)$, the conditional ES at level $\alpha = 0.95$ for a normal distribution is:

    $$
    \text{ES}_\alpha(X \mid \mathcal{F}_1) = \mu_1 + \sigma \cdot \frac{\phi(\Phi^{-1}(\alpha))}{1 - \alpha}
    $$

    where $\phi$ is the standard normal density, $\Phi^{-1}$ is the standard normal quantile, and $\sigma = 1$. Computing the constant:

    $$
    \Phi^{-1}(0.95) = 1.6449, \quad \phi(1.6449) = \frac{1}{\sqrt{2\pi}}e^{-1.6449^2/2} = 0.10314
    $$

    $$
    \frac{\phi(1.6449)}{1 - 0.95} = \frac{0.10314}{0.05} = 2.0627
    $$

    Therefore:

    $$
    \rho_1(X_2) = \mu_1 + 2.0627
    $$

    This is $\mathcal{F}_1$-measurable since $\mu_1$ is $\mathcal{F}_1$-measurable.

    **Step 2: Compute $\rho_0(X_2) = \text{ES}_{0.95}(\rho_1(X_2))$.** We need the unconditional distribution of $\rho_1(X_2) = \mu_1 + 2.0627$. This depends on the distribution of $\mu_1$.

    Suppose $\mu_1$ has a known distribution. For concreteness, assume $\mu_1 \sim N(m_0, \sigma_0^2)$ for some $m_0$ and $\sigma_0^2$ (this is a reasonable specification in a Gaussian model). Then $\rho_1(X_2) \sim N(m_0 + 2.0627, \sigma_0^2)$.

    Applying the ES formula again:

    $$
    \rho_0(X_2) = \text{ES}_{0.95}(\rho_1(X_2)) = (m_0 + 2.0627) + \sigma_0 \cdot 2.0627
    $$

    $$
    = m_0 + 2.0627(1 + \sigma_0)
    $$

    **Step 3: Verify time-consistency.** Time-consistency requires $\rho_0(X_2) = \rho_0(-\rho_1(X_2))$. By the recursive construction, $\rho_0$ is defined precisely as $\text{ES}_{0.95}$ applied to $\rho_1(X_2)$, which is:

    $$
    \rho_0(X_2) = \text{ES}_{0.95}(\rho_1(X_2) \mid \mathcal{F}_0) = \text{ES}_{0.95}(\rho_1(X_2))
    $$

    since $\mathcal{F}_0$ is trivial (no information at time $0$). This is exactly the composition $\rho_0(-\rho_1(X_2))$ (where we identify $\rho_1(X_2)$ as the one-step "loss" seen from time $0$).

    The time-consistency check is: does $\rho_0$ computed via the two-step recursion agree with $\rho_0$ applied to $-\rho_1$? By construction, yes. The recursive definition ensures:

    $$
    \rho_0(X_2) = \text{ES}_{0.95}\!\Big(\text{ES}_{0.95}(X_2 \mid \mathcal{F}_1)\Big) = \rho_0(-\rho_1(X_2))
    $$

    This is time-consistent because the composition of ES at each step produces a coherent assessment: the risk at $t=0$ correctly aggregates both the uncertainty about $\mu_1$ (resolved at $t=1$) and the residual risk of $X_2$ given $\mu_1$. The two-step recursion avoids the pitfall of computing $\text{ES}_{0.95}(X_2)$ directly (which would use the unconditional distribution and could give a different, time-inconsistent answer).
