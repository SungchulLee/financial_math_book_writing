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

---

## Exercises

**Exercise 1.** State the time-consistency property for a dynamic risk measure $\{\rho_t\}_{t=0}^T$: if $\rho_s(X) \le \rho_s(Y)$ for some $s > t$, then $\rho_t(X) \le \rho_t(Y)$. Explain why this property is economically desirable: a risk assessment that is worse at a future time should also be worse when evaluated today.

??? success "Solution to Exercise 1"

    **Formal statement.** A dynamic risk measure $\{\rho_t\}_{t=0}^T$ is **time-consistent** if for all $0 \le t < s \le T$ and all $X, Y \in L^\infty(\mathcal{F}_T)$:

    $$
    \rho_s(X) \le \rho_s(Y) \quad \text{a.s.} \quad \Longrightarrow \quad \rho_t(X) \le \rho_t(Y) \quad \text{a.s.}
    $$

    Equivalently, in the recursive formulation:

    $$
    \rho_t(X) = \rho_t(-\rho_s(X)) \quad \text{for all } t < s
    $$

    **Economic desirability.** Time-consistency is economically desirable for several fundamental reasons:

    1. **No preference reversals.** If at a future time $s$ the risk assessment concludes that position $X$ is less risky than $Y$ (i.e., $\rho_s(X) \le \rho_s(Y)$), then this ranking should also hold when evaluated from the earlier time $t$. If this failed, a risk manager could simultaneously hold $X$ as "safer" at one time and "riskier" at another -- creating contradictory risk reports and undermining the credibility of the risk framework.

    2. **Capital allocation stability.** If $\rho_t(X) > \rho_t(Y)$ but later $\rho_s(X) < \rho_s(Y)$, capital set aside at time $t$ for position $X$ would be excessive when re-evaluated at time $s$, leading to inefficient use of capital and potential regulatory inconsistencies.

    3. **Prevention of gaming.** Traders could exploit time-inconsistency to circumvent risk limits. If a strategy appears acceptable under $\rho_s$ but unacceptable under $\rho_t$, a trader could time their risk reporting to present the favorable assessment.

    4. **Dynamic programming compatibility.** Time-consistency is equivalent to the Bellman principle: optimal decisions computed at $t=0$ remain optimal when reconsidered at $t=1$ with the same information. Without this, multi-period risk management and optimization become intractable, as strategies cannot be computed by backward induction.

    In summary, a risk assessment that is worse at a future time (with more information) should also be worse when evaluated today -- otherwise the risk framework provides guidance that will be contradicted by its own future assessments.

---

**Exercise 2.** Show that the dynamic VaR $\{\text{VaR}_\alpha^t\}$ is not time-consistent by constructing a two-period counterexample. Use two positions $X$ and $Y$ where $\text{VaR}_\alpha^1(X) \le \text{VaR}_\alpha^1(Y)$ in every state at $t=1$, but $\text{VaR}_\alpha^0(X) > \text{VaR}_\alpha^0(Y)$ at $t=0$.

??? success "Solution to Exercise 2"

    **Counterexample showing dynamic VaR is not time-consistent.**

    Consider a two-period model with $t = 0, 1$ and $T = 1$, using $\alpha = 0.5$ for simplicity.

    **Setup.** Let $\Omega = \{\omega_1, \omega_2, \omega_3, \omega_4\}$ with $\mathbb{P}(\omega_i) = 1/4$ for each $i$. At $t=1$, the filtration $\mathcal{F}_1$ distinguishes two states: $A = \{\omega_1, \omega_2\}$ and $A^c = \{\omega_3, \omega_4\}$, each with probability $1/2$.

    Define two positions:

    $$
    X(\omega) = \begin{cases} 10 & \omega = \omega_1 \\ 0 & \omega = \omega_2 \\ 2 & \omega = \omega_3 \\ 2 & \omega = \omega_4 \end{cases}, \quad Y(\omega) = \begin{cases} 4 & \omega = \omega_1 \\ 4 & \omega = \omega_2 \\ 8 & \omega = \omega_3 \\ 0 & \omega = \omega_4 \end{cases}
    $$

    **At $t=1$ (conditional on $\mathcal{F}_1$).** In state $A$:

    - $X \mid A$ takes values $\{0, 10\}$ each with conditional probability $1/2$. So $\text{VaR}_{0.5}^1(X) = 0$ on $A$.
    - $Y \mid A$ takes values $\{4, 4\}$. So $\text{VaR}_{0.5}^1(Y) = 4$ on $A$.

    Hence $\text{VaR}_{0.5}^1(X) = 0 \le 4 = \text{VaR}_{0.5}^1(Y)$ on $A$.

    In state $A^c$:

    - $X \mid A^c$ takes values $\{2, 2\}$. So $\text{VaR}_{0.5}^1(X) = 2$ on $A^c$.
    - $Y \mid A^c$ takes values $\{0, 8\}$ each with conditional probability $1/2$. So $\text{VaR}_{0.5}^1(Y) = 0$ on $A^c$.

    Hence $\text{VaR}_{0.5}^1(X) = 2 > 0 = \text{VaR}_{0.5}^1(Y)$ on $A^c$.

    So at $t=1$, the ranking of $X$ vs $Y$ depends on the state -- there is no uniform ordering. But for time-consistency failure, we need a stronger example.

    **Refined counterexample.** Let $\Omega = \{\omega_1, \omega_2, \omega_3, \omega_4\}$ with equal probabilities $1/4$. At $t=1$: $A = \{\omega_1, \omega_2\}$, $A^c = \{\omega_3, \omega_4\}$. Use $\alpha = 0.5$.

    $$
    X(\omega) = \begin{cases} 1 & \omega = \omega_1 \\ 5 & \omega = \omega_2 \\ 1 & \omega = \omega_3 \\ 5 & \omega = \omega_4 \end{cases}, \quad Y(\omega) = \begin{cases} 3 & \omega = \omega_1 \\ 3 & \omega = \omega_2 \\ 3 & \omega = \omega_3 \\ 3 & \omega = \omega_4 \end{cases}
    $$

    At $t=1$, on $A$: $\text{VaR}_{0.5}^1(X) = 1$, $\text{VaR}_{0.5}^1(Y) = 3$. So $X$ is less risky on $A$.

    On $A^c$: $\text{VaR}_{0.5}^1(X) = 1$, $\text{VaR}_{0.5}^1(Y) = 3$. So $X$ is less risky on $A^c$.

    Hence $\text{VaR}_{0.5}^1(X) \le \text{VaR}_{0.5}^1(Y)$ everywhere. Time-consistency requires $\text{VaR}_{0.5}^0(X) \le \text{VaR}_{0.5}^0(Y)$.

    At $t=0$: The unconditional distribution of $X$ is $\{1, 5, 1, 5\}$ with equal probability $1/4$, so $\text{VaR}_{0.5}^0(X) = 1$. For $Y$: $\text{VaR}_{0.5}^0(Y) = 3$. Here $1 \le 3$, so no violation.

    The failure of time-consistency for VaR is more subtle and typically arises from the non-convexity of VaR. A clean demonstration uses $\alpha$ close to $1$:

    Let $\alpha = 0.9$. Take $\Omega$ with 100 equally likely states. At $t=1$, states split into two groups of 50 each (events $A$ and $A^c$). Define:

    - In group $A$: $X$ has 45 states at $0$ and 5 states at $100$. So $\text{VaR}_{0.9}^1(X \mid A) = 0$.
    - In group $A$: $Y$ has 44 states at $0$ and 6 states at $10$. So $\text{VaR}_{0.9}^1(Y \mid A) = 0$.
    - In group $A^c$: $X$ has 45 states at $0$ and 5 states at $100$. So $\text{VaR}_{0.9}^1(X \mid A^c) = 0$.
    - In group $A^c$: $Y$ has 44 states at $0$ and 6 states at $10$. So $\text{VaR}_{0.9}^1(Y \mid A^c) = 0$.

    At $t=1$: $\text{VaR}_{0.9}^1(X) = 0 = \text{VaR}_{0.9}^1(Y)$ in both states. Hence trivially $\text{VaR}_{0.9}^1(X) \le \text{VaR}_{0.9}^1(Y)$.

    At $t=0$: $X$ has 90 states at $0$ and 10 at $100$, so $\text{VaR}_{0.9}^0(X) = 0$. $Y$ has 88 states at $0$ and 12 at $10$, so $\text{VaR}_{0.9}^0(Y) = 0$. Again no violation.

    The standard proof of VaR's time-inconsistency relies on the failure of the recursive identity $\rho_0(X) = \rho_0(-\rho_1(X))$. Specifically, $\text{VaR}_\alpha(\text{VaR}_\alpha(X \mid \mathcal{F}_1)) \ne \text{VaR}_\alpha(X)$ in general because the quantile operator does not satisfy a tower property -- composing quantiles does not reproduce the unconditional quantile. This is fundamentally because VaR ignores the magnitude of losses beyond the quantile, and this lost information cannot be recovered by recomposition.

---

**Exercise 3.** Dynamic Expected Shortfall defined via backward recursion $\rho_t(X) = \text{ES}_\alpha(\rho_{t+1}(X) \mid \mathcal{F}_t)$ with terminal condition $\rho_T(X) = -X$ is time-consistent. Explain why the recursive composition guarantees time-consistency. What happens if we use $\rho_t(X) = \text{ES}_\alpha(X \mid \mathcal{F}_t)$ directly (without recursion)?

??? success "Solution to Exercise 3"

    **Why recursive composition guarantees time-consistency.** Define the dynamic ES recursively:

    $$
    \rho_T(X) = -X, \quad \rho_t(X) = \text{ES}_\alpha(\rho_{t+1}(X) \mid \mathcal{F}_t) \quad \text{for } t = T-1, \ldots, 0
    $$

    (The sign convention here: $\rho_T(X) = -X$ converts gains to losses, or one can set $\rho_T(X) = X$ if $X$ already represents losses.)

    **Time-consistency by construction.** For any $t < s$, consider $\rho_t(X)$. By the recursive definition, it is obtained by applying $\text{ES}_\alpha$ backward from $s$ (through $s-1, s-2, \ldots, t$) to $\rho_s(X)$. This is exactly:

    $$
    \rho_t(X) = \rho_t(-\rho_s(X))
    $$

    because $\rho_t(-\rho_s(X))$ means "apply the backward recursion from time $t$ to time $s$ with terminal condition $\rho_s(X)$" -- which is precisely what the original recursion does when decomposed at the intermediate time $s$. The recursive structure factors cleanly: the computation from $T$ to $t$ equals the computation from $T$ to $s$ followed by the computation from $s$ to $t$.

    **What happens without recursion?** If we define $\rho_t(X) = \text{ES}_\alpha(X \mid \mathcal{F}_t)$ directly (each $\rho_t$ computes ES of the terminal loss $X$ given current information), then:

    $$
    \rho_s(\rho_t(X)) = \text{ES}_\alpha(\text{ES}_\alpha(X \mid \mathcal{F}_t) \mid \mathcal{F}_s)
    $$

    This is **not** equal to $\rho_s(X) = \text{ES}_\alpha(X \mid \mathcal{F}_s)$ in general, because the ES operator does not satisfy a tower property. The issue is that $\text{ES}_\alpha(X \mid \mathcal{F}_t)$ is a nonlinear function of the conditional distribution, and evaluating ES of this nonlinear transformation differs from evaluating ES of $X$ directly.

    Concretely, $\text{ES}_\alpha(X \mid \mathcal{F}_t)$ averages the top $(1-\alpha)$ quantiles of $X$ conditional on $\mathcal{F}_t$. When we then compute $\text{ES}_\alpha$ of this $\mathcal{F}_t$-measurable quantity conditional on $\mathcal{F}_s$ (with $s < t$), we are averaging the worst $(1-\alpha)$ realizations of the conditional ES -- this double tail-averaging is not the same as a single tail-average of $X$. The non-recursive approach thus violates the recursive identity and is time-inconsistent.

---

**Exercise 4.** Time-consistency is equivalent to the "tower property" or "recursiveness": $\rho_t = \rho_t \circ \rho_s$ for $t \le s$. Explain this equivalence. Compare with the tower property of conditional expectations $\mathbb{E}[\cdot \mid \mathcal{F}_t] = \mathbb{E}[\mathbb{E}[\cdot \mid \mathcal{F}_s] \mid \mathcal{F}_t]$.

??? success "Solution to Exercise 4"

    **Time-consistency is equivalent to recursiveness.** The recursive formulation states: for $t \le s$,

    $$
    \rho_t(X) = \rho_t(-\rho_s(X))
    $$

    This can be written as $\rho_t = \rho_t \circ (-\rho_s)$, meaning evaluating risk at time $t$ is the same as first evaluating risk at time $s$ and then assessing the resulting risk at time $t$.

    **Equivalence proof.** ($\Rightarrow$) Assume time-consistency: $\rho_s(X) \le \rho_s(Y) \Rightarrow \rho_t(X) \le \rho_t(Y)$. We show $\rho_t(X) = \rho_t(-\rho_s(X))$.

    Note that $\rho_s(-\rho_s(X)) = \rho_s(X) - \rho_s(X) = 0$ (by translation invariance, since $\rho_s(X)$ is $\mathcal{F}_s$-measurable) -- wait, more carefully: $\rho_s(X - \rho_s(X)) = \rho_s(X) - \rho_s(X) = 0$ by translation invariance. Also, $\rho_s((-\rho_s(X))) = \rho_s(X)$ (since $-\rho_s(X)$ is $\mathcal{F}_s$-measurable, and by normalization $\rho_s(m) = m$ for $\mathcal{F}_s$-measurable $m$... this requires normalization).

    The standard proof proceeds as follows. Define $\hat{X} = X + \rho_s(X)$ (adjusted position). Then $\rho_s(\hat{X}) = \rho_s(X) + \rho_s(X)$... Let us use a cleaner argument.

    Consider two positions: $X$ and $Z$ where $Z$ is defined to have the same time-$s$ risk as $X$, i.e., $\rho_s(Z) = \rho_s(X)$. By time-consistency, $\rho_t(Z) = \rho_t(X)$. In particular, taking $Z = -\rho_s(X)$ (a position that is $\mathcal{F}_s$-measurable), we need $\rho_s(-\rho_s(X)) = \rho_s(X)$ (by normalization: $\rho_s(m) = m$ for $\mathcal{F}_s$-measurable $m$). Then time-consistency gives $\rho_t(X) = \rho_t(-\rho_s(X))$.

    ($\Leftarrow$) Assume recursiveness: $\rho_t(X) = \rho_t(-\rho_s(X))$. If $\rho_s(X) \le \rho_s(Y)$, then $-\rho_s(X) \ge -\rho_s(Y)$, so by monotonicity of $\rho_t$:

    $$
    \rho_t(X) = \rho_t(-\rho_s(X)) \le \rho_t(-\rho_s(Y)) = \rho_t(Y)
    $$

    (using that $-\rho_s(X) \le -\rho_s(Y)$ implies $\rho_t(-\rho_s(X)) \le \rho_t(-\rho_s(Y))$ by monotonicity of $\rho_t$ applied to $\mathcal{F}_s$-measurable quantities). This gives time-consistency.

    **Comparison with conditional expectation.** The tower property of conditional expectation is:

    $$
    \mathbb{E}[X \mid \mathcal{F}_t] = \mathbb{E}[\mathbb{E}[X \mid \mathcal{F}_s] \mid \mathcal{F}_t] \quad \text{for } t \le s
    $$

    The recursive formulation of time-consistency is the nonlinear analogue:

    $$
    \rho_t(X) = \rho_t(-\rho_s(X)) \quad \text{for } t \le s
    $$

    For conditional expectation, $\rho_t(X) = -\mathbb{E}[X \mid \mathcal{F}_t]$ (the negative expectation as a risk measure), and the recursion becomes:

    $$
    -\mathbb{E}[X \mid \mathcal{F}_t] = -\mathbb{E}[\mathbb{E}[X \mid \mathcal{F}_s] \mid \mathcal{F}_t]
    $$

    which is exactly the tower property. Thus, time-consistency for general risk measures generalizes the tower property from linear (expectation) to nonlinear (risk measure) settings. The key structural difference is that while the tower property for expectations follows from the definition of conditional expectation and the $\sigma$-algebra inclusion $\mathcal{F}_t \subseteq \mathcal{F}_s$, the recursive property for risk measures must be imposed as an axiom or derived from the specific construction (e.g., BSDEs).

---

**Exercise 5.** In a three-period model, a risk manager evaluates position $X$ at times $t = 0, 1, 2$. At $t = 1$, in state $\omega_1$, $\rho_1(X) = 5$; in state $\omega_2$, $\rho_1(X) = 3$. A time-consistent risk measure at $t=0$ must give $\rho_0(X) \ge 3$ (since the position is risky in at least one state). Compute $\rho_0(X)$ if the $t=0$ measure is $\text{ES}_{0.5}$ of $\rho_1(X)$ where both states are equally likely.

??? success "Solution to Exercise 5"

    **Setup.** At $t=1$, in state $\omega_1$: $\rho_1(X) = 5$; in state $\omega_2$: $\rho_1(X) = 3$. Both states are equally likely: $\mathbb{P}(\omega_1) = \mathbb{P}(\omega_2) = 1/2$.

    **Computing $\rho_0(X) = \text{ES}_{0.5}(\rho_1(X))$.** The random variable $\rho_1(X)$ takes values $\{3, 5\}$ with equal probability $1/2$.

    First, compute $\text{VaR}_{0.5}(\rho_1(X))$. The $0.5$-quantile of the distribution $\{3, 5\}$ (each with probability $1/2$) is $3$ (the median, or more precisely, $\inf\{x: \mathbb{P}(\rho_1(X) \le x) \ge 0.5\} = 3$).

    Then:

    $$
    \text{ES}_{0.5}(\rho_1(X)) = \frac{1}{1-0.5}\int_{0.5}^1 \text{VaR}_u(\rho_1(X))\,du
    $$

    For $u \in (0.5, 1]$, $\text{VaR}_u(\rho_1(X)) = 5$ (since $\mathbb{P}(\rho_1(X) \le 3) = 0.5$ and the next value is $5$). Therefore:

    $$
    \text{ES}_{0.5}(\rho_1(X)) = \frac{1}{0.5}\int_{0.5}^1 5\,du = 2 \times 5 \times 0.5 = 5
    $$

    So $\rho_0(X) = 5$.

    Alternatively, $\text{ES}_{0.5}(\rho_1(X)) = \mathbb{E}[\rho_1(X) \mid \rho_1(X) \ge \text{VaR}_{0.5}(\rho_1(X))] = \mathbb{E}[\rho_1(X) \mid \rho_1(X) \ge 3]$. Since both values $3$ and $5$ satisfy $\ge 3$, this equals $\mathbb{E}[\rho_1(X)] = (3+5)/2 = 4$.

    There is a subtlety at the boundary. Since $\mathbb{P}(\rho_1(X) \ge 3) = 1 > 1 - \alpha = 0.5$, we need to be careful. The precise formula is:

    $$
    \text{ES}_{0.5}(\rho_1(X)) = \frac{1}{1 - 0.5}\left[\mathbb{E}[\rho_1(X) \cdot \mathbf{1}_{\rho_1(X) > 3}] + 3 \cdot (0.5 - \mathbb{P}(\rho_1(X) > 3))\right]
    $$

    $$
    = 2\left[\frac{1}{2} \cdot 5 + 3 \cdot (0.5 - 0.5)\right] = 2 \times 2.5 = 5
    $$

    Wait, let us reconsider. We have $\mathbb{P}(\rho_1(X) > 3) = \mathbb{P}(\omega_1) = 1/2 = 1 - \alpha$. So the tail probability exactly equals $1 - \alpha$, and:

    $$
    \text{ES}_{0.5}(\rho_1(X)) = \frac{1}{0.5}\mathbb{E}[\rho_1(X) \cdot \mathbf{1}_{\rho_1(X) > 3}] = 2 \times \frac{1}{2} \times 5 = 5
    $$

    Hmm, but this excludes the boundary atom. The standard continuous formula gives:

    $$
    \text{ES}_{0.5} = \frac{1}{0.5}\int_{0.5}^{1}\text{VaR}_u\,du
    $$

    For $u \in (0.5, 1)$: $\text{VaR}_u = 5$ (since $\mathbb{P}(\rho_1 \le 3) = 0.5$ and the jump to $5$ occurs at $u = 0.5$). So the integral equals $5 \times 0.5 = 2.5$ and $\text{ES}_{0.5} = 2.5 / 0.5 = 5$.

    Therefore $\rho_0(X) = 5$.

    **Verification.** We have $\rho_0(X) = 5 \ge 3$, confirming that the time-$0$ risk is at least as large as the minimum possible time-$1$ risk. In fact, $\rho_0(X) = 5$ equals the maximum of $\rho_1(X)$ across states. This makes sense: $\text{ES}_{0.5}$ applied to a two-point distribution with equal probabilities picks out the expected value in the upper tail, which here is the single state $\omega_1$ where $\rho_1(X) = 5$.

    The time-consistent risk at $t=0$ correctly reflects that in the worst half of scenarios at $t=1$, the risk is $5$.

---

**Exercise 6.** Discuss the practical implications of time-consistency for multi-period portfolio optimization. Why does a time-inconsistent risk measure lead to dynamically inconsistent investment decisions (i.e., the optimal plan at $t=0$ is no longer optimal at $t=1$)? How does this relate to the concept of "dynamic programming principle"?

??? success "Solution to Exercise 6"

    **Time-inconsistency leads to dynamically inconsistent investment decisions.** Consider a multi-period portfolio optimization problem where an investor minimizes risk over a planning horizon $[0, T]$:

    $$
    \min_{\pi} \rho_0(X_T^\pi)
    $$

    where $\pi = (\pi_0, \pi_1, \ldots, \pi_{T-1})$ is the investment strategy and $X_T^\pi$ is the terminal portfolio value.

    At $t=0$, the investor solves this problem and obtains an optimal strategy $\pi^* = (\pi_0^*, \pi_1^*, \ldots, \pi_{T-1}^*)$.

    At $t=1$, the investor re-evaluates using $\rho_1$:

    $$
    \min_{\pi_1, \ldots, \pi_{T-1}} \rho_1(X_T^\pi)
    $$

    **If $\rho$ is time-consistent,** then $\rho_0(X_T^\pi) = \rho_0(-\rho_1(X_T^\pi))$. The overall optimization decomposes recursively:

    $$
    \min_{\pi_0} \rho_0\!\left(-\min_{\pi_1, \ldots, \pi_{T-1}} \rho_1(X_T^\pi)\right)
    $$

    The optimal $(\pi_1^*, \ldots, \pi_{T-1}^*)$ chosen at $t=0$ (as part of the full optimization) remains optimal when re-evaluated at $t=1$ under $\rho_1$. The investor has no incentive to deviate from the pre-committed plan.

    **If $\rho$ is time-inconsistent,** then $\rho_0(X_T^\pi) \ne \rho_0(-\rho_1(X_T^\pi))$ in general. The strategy $\pi^*$ that minimizes $\rho_0$ may not minimize $\rho_1$ when time $1$ arrives. The investor at $t=1$ would prefer a different continuation strategy $\hat{\pi}_1 \ne \pi_1^*$. This means:

    - The investor at $t=0$ cannot trust their own future behavior.
    - Pre-commitment (if possible) leads to a different outcome than dynamic re-optimization.
    - The concept of "optimal strategy" becomes ambiguous -- optimal according to which time's preferences?

    **Connection to the dynamic programming principle (DPP).** The DPP states:

    $$
    V_t = \min_{\pi_t} \rho_t(-V_{t+1})
    $$

    where $V_t$ is the value function at time $t$. This recursive decomposition is valid **if and only if** $\rho$ is time-consistent. The DPP allows solving the multi-period problem by working backward one period at a time, which is both computationally tractable and ensures dynamic consistency.

    When $\rho$ is time-inconsistent:

    - The DPP fails: $V_t \ne \min_{\pi_t} \rho_t(-V_{t+1})$.
    - Backward induction does not reproduce the global optimum.
    - The Bellman equation has no meaningful solution in the usual sense.
    - One must either (a) pre-commit to the $t=0$ optimal plan (ignoring future re-optimization), (b) solve for a subgame-perfect equilibrium (the "consistent planning" approach of Strotz), or (c) accept that the "optimal" plan will be revised at each period.

    **Practical consequences for portfolio management:**

    - **VaR-based optimization** is time-inconsistent: a portfolio optimized under VaR at $t=0$ will generally not be VaR-optimal at $t=1$, creating pressure to rebalance in ways that may increase overall risk.
    - **ES-based recursive optimization** (iterated ES) is time-consistent and supports dynamic programming, making it suitable for multi-period risk budgeting and capital planning.
    - **BSDE-based risk measures** are time-consistent by construction and provide the continuous-time analogue of the dynamic programming principle, enabling consistent risk management over continuous trading horizons.
