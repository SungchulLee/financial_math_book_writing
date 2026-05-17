# Monetary Risk Measures

**Monetary risk measures** form the axiomatic foundation for the theory of risk quantification. By requiring only two minimal axioms -- **monotonicity** and **translation invariance** -- they provide the broadest framework within which coherent, convex, and more general risk measures are systematically organized. This section develops the hierarchy from monetary through convex to coherent risk measures, with dual representations and key examples at each level.

---

## The Axiomatic Framework

### Setting

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space. A **risk measure** is a mapping:

$$
\rho: \mathcal{X} \to \mathbb{R} \cup \{+\infty\}
$$

where $\mathcal{X}$ is a space of financial positions (random variables representing losses). We work with $\mathcal{X} = L^\infty(\Omega, \mathcal{F}, \mathbb{P})$ (bounded random variables) or $\mathcal{X} = L^p$ for $p \ge 1$.

**Convention:** Positive values of $X \in \mathcal{X}$ represent **losses**, so higher $\rho(X)$ means greater risk.

---

## Monetary Risk Measures

!!! info "Definition"
    A risk measure $\rho: \mathcal{X} \to \mathbb{R}$ is **monetary** if it satisfies:

    1. **Monotonicity:** If $X \le Y$ a.s., then $\rho(X) \le \rho(Y)$
    2. **Translation invariance (cash invariance):** $\rho(X + c) = \rho(X) + c$ for all $c \in \mathbb{R}$

### Interpretation

**Monotonicity** says that higher losses require more capital. If position $X$ is dominated by $Y$ (i.e., $Y$ produces at least as large a loss in every state), then $Y$ is at least as risky.

**Translation invariance** says that adding a certain loss $c$ increases the risk by exactly $c$. Equivalently, setting aside cash $m = \rho(X)$ reduces the risk to zero:

$$
\rho(X - \rho(X)) = \rho(X) - \rho(X) = 0
$$

This gives $\rho(X)$ the interpretation of the **minimum capital requirement**: the smallest cash amount that, when added to the position, makes it acceptable.

### Acceptance Set

The **acceptance set** of a monetary risk measure is:

$$
\mathcal{A}_\rho = \{X \in \mathcal{X} : \rho(X) \le 0\}
$$

**Proposition.** For a monetary risk measure, $\mathcal{A}_\rho$ satisfies:

- $\mathcal{A}_\rho$ is non-empty (contains $X = c$ for sufficiently negative $c$)
- If $X \in \mathcal{A}_\rho$ and $Y \le X$ a.s., then $Y \in \mathcal{A}_\rho$ (monotonicity)
- $\inf\{c : X - c \in \mathcal{A}_\rho\} = \rho(X)$ (reconstruction)

Conversely, any set $\mathcal{A}$ satisfying these properties defines a monetary risk measure via the reconstruction formula. $\square$

---

## Convex Risk Measures

### Definition

!!! info "Definition"
    A monetary risk measure $\rho$ is **convex** if:

    $$
    \rho(\lambda X + (1-\lambda)Y) \le \lambda \rho(X) + (1-\lambda) \rho(Y) \quad \forall \lambda \in [0,1]
    $$

### Interpretation

Convexity encodes a **diversification principle**: a mixture of positions is no riskier than the weighted average of individual risks. This is weaker than subadditivity; it allows for position-size-dependent risk but still rewards diversification.

### Acceptance Set Characterization

$\rho$ is convex if and only if $\mathcal{A}_\rho$ is a **convex set**.

**Proof.** Suppose $\rho$ is convex. If $X, Y \in \mathcal{A}_\rho$ (i.e., $\rho(X) \le 0$ and $\rho(Y) \le 0$), then for $\lambda \in [0,1]$:

$$
\rho(\lambda X + (1-\lambda)Y) \le \lambda \rho(X) + (1-\lambda)\rho(Y) \le 0
$$

so $\lambda X + (1-\lambda)Y \in \mathcal{A}_\rho$. The converse follows from the reconstruction formula. $\square$

### Dual Representation of Convex Risk Measures

!!! info "Theorem (Föllmer-Schied)"
    A convex risk measure $\rho$ on $L^\infty$ that is lower semicontinuous admits the representation:

    $$
    \rho(X) = \sup_{\mathbb{Q} \in \mathcal{M}_1} \left\{\mathbb{E}^{\mathbb{Q}}[X] - \alpha(\mathbb{Q})\right\}
    $$

    where $\mathcal{M}_1$ is the set of probability measures absolutely continuous with respect to $\mathbb{P}$, and $\alpha: \mathcal{M}_1 \to \mathbb{R} \cup \{+\infty\}$ is the **penalty function**:

    $$
    \alpha(\mathbb{Q}) = \sup_{X \in \mathcal{A}_\rho} \mathbb{E}^{\mathbb{Q}}[X]
    $$

**Interpretation:** The risk of $X$ is the worst-case expected loss over all probability models $\mathbb{Q}$, penalized by $\alpha(\mathbb{Q})$ which measures the implausibility of $\mathbb{Q}$. A low penalty means $\mathbb{Q}$ is considered plausible; a high penalty means $\mathbb{Q}$ is extreme and contributes less to the supremum.

### The Entropic Risk Measure

The canonical convex risk measure is the **entropic risk measure**:

$$
\rho_\gamma(X) = \frac{1}{\gamma} \log \mathbb{E}[e^{\gamma X}]
$$

where $\gamma > 0$ is the risk aversion parameter.

**Properties:**

- Monotone and translation invariant: $\rho_\gamma(X + c) = \rho_\gamma(X) + c$
- Convex but **not** positively homogeneous: $\rho_\gamma(2X) \ne 2\rho_\gamma(X)$ in general
- Penalizes tail risk exponentially
- Connected to exponential utility: an agent with utility $U(w) = -e^{-\gamma w}$ prices risk via $\rho_\gamma$

**Dual representation penalty:**

$$
\alpha(\mathbb{Q}) = \frac{1}{\gamma} H(\mathbb{Q} \| \mathbb{P})
$$

where $H(\mathbb{Q} \| \mathbb{P}) = \mathbb{E}^{\mathbb{Q}}\left[\log \frac{d\mathbb{Q}}{d\mathbb{P}}\right]$ is the relative entropy (Kullback-Leibler divergence). Thus:

$$
\rho_\gamma(X) = \sup_{\mathbb{Q}} \left\{\mathbb{E}^{\mathbb{Q}}[X] - \frac{1}{\gamma} H(\mathbb{Q} \| \mathbb{P})\right\}
$$

---

## Coherent Risk Measures

### Definition

!!! info "Definition"
    A monetary risk measure $\rho$ is **coherent** (Artzner, Delbaen, Eber, Heath, 1999) if it satisfies:

    1. **Monotonicity:** $X \le Y$ a.s. $\Rightarrow$ $\rho(X) \le \rho(Y)$
    2. **Translation invariance:** $\rho(X + c) = \rho(X) + c$
    3. **Positive homogeneity:** $\rho(\lambda X) = \lambda \rho(X)$ for $\lambda > 0$
    4. **Subadditivity:** $\rho(X + Y) \le \rho(X) + \rho(Y)$

### Relationship to Convex Risk Measures

**Proposition.** Positive homogeneity + subadditivity $\Rightarrow$ convexity.

**Proof.** For $\lambda \in [0,1]$:

$$
\rho(\lambda X + (1-\lambda)Y) \le \rho(\lambda X) + \rho((1-\lambda)Y) = \lambda \rho(X) + (1-\lambda)\rho(Y)
$$

where the inequality uses subadditivity and the equality uses positive homogeneity. $\square$

Thus: **coherent $\Rightarrow$ convex $\Rightarrow$ monetary**, and each inclusion is strict.

### Acceptance Set Characterization

$\rho$ is coherent if and only if $\mathcal{A}_\rho$ is a **convex cone** (i.e., convex and closed under positive scaling).

### Dual Representation of Coherent Risk Measures

!!! info "Theorem (Artzner-Delbaen)"
    A coherent risk measure $\rho$ on $L^\infty$ that is lower semicontinuous admits the representation:

    $$
    \rho(X) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[X]
    $$

    where $\mathcal{Q} \subseteq \mathcal{M}_1$ is a convex, closed set of probability measures.

**Interpretation:** Coherent risk is the worst-case expected loss over a set of plausible scenarios. There is no penalty function -- equivalently, the penalty is zero on $\mathcal{Q}$ and $+\infty$ outside.

This is a special case of the convex dual with $\alpha(\mathbb{Q}) = 0$ for $\mathbb{Q} \in \mathcal{Q}$ and $\alpha(\mathbb{Q}) = +\infty$ otherwise.

---

## The Hierarchy of Risk Measures

| Property | Monetary | Convex | Coherent |
|----------|----------|--------|----------|
| Monotonicity | Yes | Yes | Yes |
| Translation invariance | Yes | Yes | Yes |
| Convexity | Not required | Yes | Yes (implied) |
| Positive homogeneity | Not required | Not required | Yes |
| Subadditivity | Not required | Not required | Yes |
| Acceptance set | Monotone, nonempty | Convex | Convex cone |
| Dual representation | Not guaranteed | $\sup_\mathbb{Q}\{\mathbb{E}^\mathbb{Q}[X] - \alpha(\mathbb{Q})\}$ | $\sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^\mathbb{Q}[X]$ |

---

## Key Examples

### Value-at-Risk and Expected Shortfall

Recall (see [VaR](../market_risk_measures/value_at_risk_var.md), [ES](../market_risk_measures/expected_shortfall_es.md), [coherent risk measures](../market_risk_measures/coherent_risk_measures.md)) that VaR is monetary but fails subadditivity (hence not coherent), while ES is coherent with dual set $\mathcal{Q} = \{\mathbb{Q} : d\mathbb{Q}/d\mathbb{P} \le 1/(1-\alpha)\}$.

### Entropic Risk Measure

$$
\rho_\gamma(X) = \frac{1}{\gamma} \log \mathbb{E}[e^{\gamma X}]
$$

- Monetary: Yes
- Convex: **Yes**
- Coherent: **No** (fails positive homogeneity)
- Penalty: $\alpha(\mathbb{Q}) = \frac{1}{\gamma} H(\mathbb{Q} \| \mathbb{P})$

### Worst-Case Risk Measure

$$
\rho_{\text{max}}(X) = \text{ess\,sup}(X)
$$

- Monetary: Yes
- Convex: Yes
- Coherent: **Yes** (with $\mathcal{Q} = \mathcal{M}_1$, all probability measures)
- Maximally conservative: the worst possible outcome

---

## From Static to Dynamic

Monetary risk measures provide the foundation for **dynamic (conditional) risk measures**. The conditional versions replace the axioms with $\mathcal{F}_t$-measurable versions:

- **Conditional monotonicity:** $X \le Y$ a.s. $\Rightarrow$ $\rho_t(X) \le \rho_t(Y)$ a.s.
- **Conditional translation invariance:** $\rho_t(X + m) = \rho_t(X) + m$ for $\mathcal{F}_t$-measurable $m$

The conditional dual representation becomes:

$$
\rho_t(X) = \operatorname{ess\,sup}_{\mathbb{Q} \in \mathcal{Q}_t} \mathbb{E}^{\mathbb{Q}}[X \mid \mathcal{F}_t]
$$

The **time-consistency** property $\rho_s(X) = \rho_s(-\rho_t(X))$ for $s < t$ connects conditional risk measures to BSDEs and the dynamic programming principle, bridging to the BSDE-based risk measures developed in this chapter.

---

## Robust Representation and Model Uncertainty

The dual representation $\rho(X) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[X]$ provides a natural framework for **model uncertainty** (ambiguity):

- The set $\mathcal{Q}$ represents plausible probability models
- $\rho(X)$ is the worst-case expected loss over all plausible models
- An agent who is **ambiguity-averse** uses a coherent risk measure to hedge against model misspecification

This connects risk measurement to **distributionally robust optimization**:

$$
\min_{\mathbf{w}} \rho(L_{\mathbf{w}}) = \min_{\mathbf{w}} \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[L_{\mathbf{w}}]
$$

which yields portfolios robust to model uncertainty.

---

## Key Takeaways

- Monetary risk measures require only monotonicity and translation invariance, forming the broadest axiomatic class
- Convex risk measures add the diversification principle through convexity, with a dual representation via penalty functions
- Coherent risk measures (Artzner axioms) add positive homogeneity and subadditivity, with a simpler dual representation as worst-case expectations
- The hierarchy is strict: coherent $\subsetneq$ convex $\subsetneq$ monetary
- VaR is monetary but not convex; ES is coherent; the entropic risk measure is convex but not coherent
- The dual representation connects risk measurement to model uncertainty and robust optimization
- Conditional versions of these axioms lead to dynamic risk measures and the BSDE framework

---

## Further Reading

- Artzner, P., Delbaen, F., Eber, J.-M., & Heath, D. (1999), "Coherent Measures of Risk," *Mathematical Finance*
- Föllmer, H. & Schied, A. (2016), *Stochastic Finance: An Introduction in Discrete Time*, 4th ed.
- Frittelli, M. & Rosazza Gianin, E. (2002), "Putting Order in Risk Measures," *Journal of Banking and Finance*
- Detlefsen, K. & Scandolo, G. (2005), "Conditional and Dynamic Convex Risk Measures"
- Delbaen, F. (2002), "Coherent Risk Measures on General Probability Spaces"

---

## Exercises

**Exercise 1.** A monetary risk measure satisfies monotonicity and translation invariance. State each axiom formally. Verify that the worst-case risk measure $\rho(X) = -\text{ess inf}(X)$ is monetary. Is it also coherent?

??? success "Solution to Exercise 1"

    **Formal axioms.** A risk measure $\rho:\mathcal{X}\to\mathbb{R}$ on a space $\mathcal{X}$ of financial positions (with the loss convention) is monetary if:

    1. **Monotonicity:** For all $X, Y \in \mathcal{X}$, if $X \le Y$ a.s., then $\rho(X) \le \rho(Y)$.
    2. **Translation invariance (cash invariance):** For all $X \in \mathcal{X}$ and $c \in \mathbb{R}$, $\rho(X + c) = \rho(X) + c$.

    **Verification for the worst-case risk measure.** Recall that under the loss convention used in this chapter, the worst-case risk measure is

    $$
    \rho(X) = \operatorname{ess\,sup}(X)
    $$

    (Note: the exercise writes $\rho(X) = -\operatorname{ess\,inf}(X)$. Under the loss convention where $X$ represents losses, we have $-\operatorname{ess\,inf}(X) = \operatorname{ess\,sup}(-X)$. Both formulations define the worst-case measure depending on sign conventions. We verify the axioms for $\rho(X) = -\operatorname{ess\,inf}(X)$.)

    *Monotonicity:* If $X \le Y$ a.s., then $\inf X \ge \inf Y$ does **not** hold in general, but $-\operatorname{ess\,inf}(X) \le -\operatorname{ess\,inf}(Y)$ needs care with the sign convention. Under the convention that $X$ represents gains (positive = good), $\rho(X) = -\operatorname{ess\,inf}(X)$ is the worst-case measure for gains, and monotonicity in that convention reads: $X \ge Y$ a.s. $\Rightarrow$ $\rho(X) \le \rho(Y)$. Equivalently, using the loss convention of this chapter with $\rho(X) = \operatorname{ess\,sup}(X)$:

    If $X \le Y$ a.s., then $\operatorname{ess\,sup}(X) \le \operatorname{ess\,sup}(Y)$, since the supremum operator preserves order. Hence monotonicity holds.

    *Translation invariance:* For any $c \in \mathbb{R}$,

    $$
    \rho(X + c) = \operatorname{ess\,sup}(X + c) = \operatorname{ess\,sup}(X) + c = \rho(X) + c
    $$

    so translation invariance holds. Thus $\rho$ is monetary.

    **Is it coherent?** We verify positive homogeneity and subadditivity.

    *Positive homogeneity:* For $\lambda > 0$,

    $$
    \rho(\lambda X) = \operatorname{ess\,sup}(\lambda X) = \lambda \operatorname{ess\,sup}(X) = \lambda \rho(X)
    $$

    *Subadditivity:* For any $X, Y$,

    $$
    \rho(X + Y) = \operatorname{ess\,sup}(X + Y) \le \operatorname{ess\,sup}(X) + \operatorname{ess\,sup}(Y) = \rho(X) + \rho(Y)
    $$

    since the essential supremum is subadditive. Therefore $\rho$ is coherent. Its dual representation corresponds to $\mathcal{Q} = \mathcal{M}_1$ (the set of all probability measures absolutely continuous w.r.t. $\mathbb{P}$), making it the most conservative coherent risk measure.

---

**Exercise 2.** Show that VaR at level $\alpha$ satisfies monotonicity and translation invariance (hence is monetary) but fails subadditivity. Construct an explicit example with two positions $X$ and $Y$ where $\text{VaR}_\alpha(X + Y) > \text{VaR}_\alpha(X) + \text{VaR}_\alpha(Y)$.

??? success "Solution to Exercise 2"

    **Monotonicity of VaR.** Let $\text{VaR}_\alpha(X) = \inf\{x : \mathbb{P}(X \le x) \ge \alpha\}$. If $X \le Y$ a.s., then for every $x$,

    $$
    \mathbb{P}(Y \le x) \le \mathbb{P}(X \le x)
    $$

    because $\{Y \le x\} \subseteq \{X \le x\}$ a.s. Hence if $\mathbb{P}(X \le x) \ge \alpha$, it follows that $\mathbb{P}(Y \le x) \ge \alpha$ is harder to achieve. More precisely, the quantile function $F_X^{-1}(\alpha) \le F_Y^{-1}(\alpha)$ when $X \le Y$ a.s., so $\text{VaR}_\alpha(X) \le \text{VaR}_\alpha(Y)$.

    **Translation invariance.** For any $c \in \mathbb{R}$,

    $$
    \text{VaR}_\alpha(X + c) = \inf\{x : \mathbb{P}(X + c \le x) \ge \alpha\} = \inf\{x : \mathbb{P}(X \le x - c) \ge \alpha\}
    $$

    Substituting $x' = x - c$, this equals $\inf\{x' + c : \mathbb{P}(X \le x') \ge \alpha\} = \text{VaR}_\alpha(X) + c$.

    Hence VaR is monetary.

    **Failure of subadditivity -- explicit counterexample.** Let $\Omega = \{\omega_1, \omega_2, \ldots, \omega_{100}\}$ with uniform probability $\mathbb{P}(\omega_i) = 1/100$. Define two positions $X$ and $Y$ as follows:

    - $X(\omega_i) = 0$ for $i = 1, \ldots, 99$, and $X(\omega_{100}) = 100$
    - $Y(\omega_i) = 0$ for $i = 1, \ldots, 99$, and $Y(\omega_{99}) = 100$, with the events $\{X = 100\}$ and $\{Y = 100\}$ disjoint

    More precisely, let $X$ and $Y$ be designed so that they each have a single large loss occurring in different states:

    - $X(\omega_i) = \begin{cases} 100 & i = 100 \\ 0 & \text{otherwise}\end{cases}$
    - $Y(\omega_i) = \begin{cases} 100 & i = 99 \\ 0 & \text{otherwise}\end{cases}$

    At level $\alpha = 0.95$:

    $$
    \text{VaR}_{0.95}(X) = 0, \quad \text{VaR}_{0.95}(Y) = 0
    $$

    since $\mathbb{P}(X \le 0) = 99/100 = 0.99 \ge 0.95$ and similarly for $Y$.

    Now consider $X + Y$:

    $$
    (X+Y)(\omega_i) = \begin{cases} 100 & i = 99 \text{ or } i = 100 \\ 0 & \text{otherwise}\end{cases}
    $$

    We have $\mathbb{P}(X + Y \le 0) = 98/100 = 0.98 \ge 0.95$, so $\text{VaR}_{0.95}(X+Y) = 0$.

    This particular example does not violate subadditivity. Let us refine it with more states. Consider $\alpha = 0.95$ and a sample space with $n = 20$ equally likely states. Define:

    - $X(\omega_i) = \begin{cases} 100 & i = 20 \\ 0 & \text{otherwise}\end{cases}$
    - $Y(\omega_i) = \begin{cases} 100 & i = 19 \\ 0 & \text{otherwise}\end{cases}$

    Then $\mathbb{P}(X \le 0) = 19/20 = 0.95 \ge 0.95$, so $\text{VaR}_{0.95}(X) = 0$. Similarly $\text{VaR}_{0.95}(Y) = 0$.

    For $X + Y$: $\mathbb{P}(X+Y \le 0) = 18/20 = 0.90 < 0.95$. Hence $\text{VaR}_{0.95}(X+Y) = 100$.

    Therefore:

    $$
    \text{VaR}_{0.95}(X + Y) = 100 > 0 = \text{VaR}_{0.95}(X) + \text{VaR}_{0.95}(Y)
    $$

    This demonstrates the failure of subadditivity. Diversification (combining $X$ and $Y$) actually increases VaR because the two rare losses, while individually below the quantile threshold, jointly push the combined loss above it.

---

**Exercise 3.** A convex risk measure satisfies monotonicity, translation invariance, and convexity: $\rho(\lambda X + (1-\lambda)Y) \le \lambda\rho(X) + (1-\lambda)\rho(Y)$. Show that every coherent risk measure is convex, but not vice versa. Provide an example of a convex but not coherent risk measure (hint: the entropic risk measure).

??? success "Solution to Exercise 3"

    **Every coherent risk measure is convex.** A coherent risk measure satisfies positive homogeneity and subadditivity. For $\lambda \in [0,1]$:

    $$
    \rho(\lambda X + (1-\lambda)Y) \le \rho(\lambda X) + \rho((1-\lambda)Y) = \lambda\rho(X) + (1-\lambda)\rho(Y)
    $$

    where the inequality uses subadditivity, and the equality uses positive homogeneity (applied with scalars $\lambda$ and $1-\lambda$). This is exactly the convexity condition.

    **Not every convex risk measure is coherent.** The entropic risk measure provides a counterexample. Define:

    $$
    \rho_\gamma(X) = \frac{1}{\gamma}\log\mathbb{E}[e^{\gamma X}]
    $$

    for $\gamma > 0$.

    *Convexity:* By Hölder's inequality (or the log-convexity of the exponential moment generating function), for $\lambda \in [0,1]$:

    $$
    \mathbb{E}[e^{\gamma(\lambda X + (1-\lambda)Y)}] = \mathbb{E}[e^{\gamma\lambda X} \cdot e^{\gamma(1-\lambda)Y}]
    $$

    By Hölder's inequality with conjugate exponents $p = 1/\lambda$ and $q = 1/(1-\lambda)$:

    $$
    \mathbb{E}[e^{\gamma\lambda X} \cdot e^{\gamma(1-\lambda)Y}] \le \left(\mathbb{E}[e^{\gamma X}]\right)^\lambda \left(\mathbb{E}[e^{\gamma Y}]\right)^{1-\lambda}
    $$

    Taking $\frac{1}{\gamma}\log$ of both sides:

    $$
    \rho_\gamma(\lambda X + (1-\lambda)Y) \le \lambda \rho_\gamma(X) + (1-\lambda)\rho_\gamma(Y)
    $$

    So $\rho_\gamma$ is convex.

    *Failure of positive homogeneity:* Consider a constant $\lambda > 0$ with $\lambda \ne 1$. For any non-degenerate random variable $X$:

    $$
    \rho_\gamma(\lambda X) = \frac{1}{\gamma}\log\mathbb{E}[e^{\gamma\lambda X}] = \frac{1}{\gamma}\log\mathbb{E}[e^{(\gamma\lambda) X}]
    $$

    If positive homogeneity held, we would need $\rho_\gamma(\lambda X) = \lambda \rho_\gamma(X)$, i.e.,

    $$
    \frac{1}{\gamma}\log\mathbb{E}[e^{\gamma\lambda X}] = \frac{\lambda}{\gamma}\log\mathbb{E}[e^{\gamma X}]
    $$

    This fails in general. For example, let $X \sim N(0,1)$ and compute:

    $$
    \rho_\gamma(\lambda X) = \frac{1}{\gamma}\log e^{\gamma^2\lambda^2/2} = \frac{\gamma\lambda^2}{2}
    $$

    $$
    \lambda\rho_\gamma(X) = \lambda \cdot \frac{\gamma}{2} = \frac{\gamma\lambda}{2}
    $$

    These are equal only when $\lambda = 1$. Since positive homogeneity fails, $\rho_\gamma$ is not coherent.

---

**Exercise 4.** The dual representation of a coherent risk measure is $\rho(X) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[-X]$ for some set of probability measures $\mathcal{Q}$. For Expected Shortfall at level $\alpha$, describe the set $\mathcal{Q}$ explicitly. Why does this representation have the interpretation of "worst-case expected loss"?

??? success "Solution to Exercise 4"

    **Dual representation of Expected Shortfall.** The coherent dual representation is:

    $$
    \text{ES}_\alpha(X) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[-X]
    $$

    For Expected Shortfall at level $\alpha$, the set $\mathcal{Q}$ is:

    $$
    \mathcal{Q} = \left\{\mathbb{Q} \ll \mathbb{P} \;\bigg|\; \frac{d\mathbb{Q}}{d\mathbb{P}} \le \frac{1}{1-\alpha}\right\}
    $$

    That is, $\mathcal{Q}$ consists of all probability measures $\mathbb{Q}$ absolutely continuous with respect to $\mathbb{P}$ whose Radon–Nikodym derivative is bounded above by $\frac{1}{1-\alpha}$.

    **Why this set?** The constraint $\frac{d\mathbb{Q}}{d\mathbb{P}} \le \frac{1}{1-\alpha}$ means that $\mathbb{Q}$ can place at most $\frac{1}{1-\alpha}$ times as much weight on any event as $\mathbb{P}$ does. The extremal measure in $\mathcal{Q}$ that achieves the supremum concentrates all its extra weight on the worst $(1-\alpha)$ fraction of outcomes. Specifically, the maximizing $\mathbb{Q}^*$ has:

    $$
    \frac{d\mathbb{Q}^*}{d\mathbb{P}} = \frac{1}{1-\alpha} \mathbf{1}_{\{X \ge \text{VaR}_\alpha(X)\}}
    $$

    (with an appropriate adjustment at the boundary if the distribution has an atom at $\text{VaR}_\alpha$). Under this $\mathbb{Q}^*$:

    $$
    \mathbb{E}^{\mathbb{Q}^*}[X] = \frac{1}{1-\alpha}\mathbb{E}[X \cdot \mathbf{1}_{\{X \ge \text{VaR}_\alpha(X)\}}] = \text{ES}_\alpha(X)
    $$

    **Worst-case expected loss interpretation.** The representation $\text{ES}_\alpha(X) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[X]$ says that ES is the worst-case expected loss over all probability models in $\mathcal{Q}$. Each $\mathbb{Q} \in \mathcal{Q}$ can be viewed as a "stress scenario" that reweights the probability of different outcomes. The constraint $\frac{d\mathbb{Q}}{d\mathbb{P}} \le \frac{1}{1-\alpha}$ limits how extreme these stress scenarios can be -- the adversary cannot place arbitrarily large weight on bad outcomes. The worst-case adversary concentrates attention on the tail, yielding the average loss in the worst $(1-\alpha)$ fraction of scenarios, which is precisely the definition of Expected Shortfall.

---

**Exercise 5.** Verify that the entropic risk measure $\rho_\theta(X) = \frac{1}{\theta}\ln\mathbb{E}[e^{-\theta X}]$ satisfies monotonicity and translation invariance. Show that it is convex but not positively homogeneous (hence not coherent). What role does the parameter $\theta$ play as a risk aversion coefficient?

??? success "Solution to Exercise 5"

    We verify each property for $\rho_\theta(X) = \frac{1}{\theta}\ln\mathbb{E}[e^{-\theta X}]$.

    **Note on convention.** The exercise uses $\rho_\theta(X) = \frac{1}{\theta}\ln\mathbb{E}[e^{-\theta X}]$ with a negative sign in the exponent. This corresponds to a gain convention where $X$ represents gains. Under the loss convention used earlier in the chapter ($\rho_\gamma(X) = \frac{1}{\gamma}\log\mathbb{E}[e^{\gamma X}]$), the formulas are equivalent with appropriate sign adjustments. We verify the properties as stated.

    **Monotonicity.** If $X \le Y$ a.s., then $-\theta X \ge -\theta Y$ a.s. (for $\theta > 0$), so $e^{-\theta X} \ge e^{-\theta Y}$ a.s. Hence $\mathbb{E}[e^{-\theta X}] \ge \mathbb{E}[e^{-\theta Y}]$, and since $\ln$ is increasing and $1/\theta > 0$:

    $$
    \rho_\theta(X) = \frac{1}{\theta}\ln\mathbb{E}[e^{-\theta X}] \ge \frac{1}{\theta}\ln\mathbb{E}[e^{-\theta Y}] = \rho_\theta(Y)
    $$

    Under the gain convention, this says higher gains lead to lower risk, which is the correct direction: $X \le Y \Rightarrow \rho_\theta(X) \ge \rho_\theta(Y)$.

    **Translation invariance.** For $c \in \mathbb{R}$:

    $$
    \rho_\theta(X + c) = \frac{1}{\theta}\ln\mathbb{E}[e^{-\theta(X+c)}] = \frac{1}{\theta}\ln\left(e^{-\theta c}\mathbb{E}[e^{-\theta X}]\right) = \frac{1}{\theta}\left(-\theta c + \ln\mathbb{E}[e^{-\theta X}]\right) = \rho_\theta(X) - c
    $$

    This is translation invariance under the gain convention: adding a sure gain $c$ reduces risk by $c$.

    **Convexity.** For $\lambda \in [0,1]$, by Hölder's inequality with exponents $1/\lambda$ and $1/(1-\lambda)$:

    $$
    \mathbb{E}[e^{-\theta(\lambda X + (1-\lambda)Y)}] = \mathbb{E}\left[(e^{-\theta X})^\lambda (e^{-\theta Y})^{1-\lambda}\right] \le \left(\mathbb{E}[e^{-\theta X}]\right)^\lambda \left(\mathbb{E}[e^{-\theta Y}]\right)^{1-\lambda}
    $$

    Taking $\frac{1}{\theta}\ln$:

    $$
    \rho_\theta(\lambda X + (1-\lambda)Y) \le \lambda\,\rho_\theta(X) + (1-\lambda)\,\rho_\theta(Y)
    $$

    **Failure of positive homogeneity.** Let $X \sim N(0,1)$ and $\lambda = 2$. Then:

    $$
    \rho_\theta(2X) = \frac{1}{\theta}\ln\mathbb{E}[e^{-2\theta X}] = \frac{1}{\theta}\ln e^{2\theta^2} = 2\theta
    $$

    $$
    2\,\rho_\theta(X) = \frac{2}{\theta}\ln\mathbb{E}[e^{-\theta X}] = \frac{2}{\theta}\ln e^{\theta^2/2} = \theta
    $$

    Since $2\theta \ne \theta$ for $\theta > 0$, positive homogeneity fails. Therefore $\rho_\theta$ is convex but not coherent.

    **Role of $\theta$ as risk aversion.** The parameter $\theta > 0$ controls the degree of risk aversion:

    - As $\theta \to 0^+$, a Taylor expansion gives $\rho_\theta(X) \to -\mathbb{E}[X]$ (risk-neutral assessment).
    - As $\theta \to \infty$, $\rho_\theta(X) \to -\operatorname{ess\,inf}(X)$ (worst-case assessment).
    - For intermediate $\theta$, the exponential weighting $e^{-\theta X}$ penalizes large losses (small $X$) more heavily, with the penalty increasing in $\theta$.

    The entropic risk measure is directly linked to exponential utility: an agent with utility $U(w) = -e^{-\theta w}$ computes their certainty equivalent via $\rho_\theta$, so $\theta$ is literally the Arrow-Pratt coefficient of absolute risk aversion.

---

**Exercise 6.** Explain the hierarchy: monetary $\supset$ convex $\supset$ coherent risk measures. For each level, provide a representative example and state which additional axioms are required. Why did the Artzner et al. (1999) coherence axioms become the standard framework for regulatory risk measurement?

??? success "Solution to Exercise 6"

    **The hierarchy.** The three classes form a strict chain of inclusions:

    $$
    \text{Coherent} \subsetneq \text{Convex} \subsetneq \text{Monetary}
    $$

    **Level 1: Monetary risk measures.** Axioms required: (i) monotonicity, (ii) translation invariance. Representative example: **Value-at-Risk** $\text{VaR}_\alpha(X) = \inf\{x : \mathbb{P}(X \le x) \ge \alpha\}$. VaR satisfies monotonicity and translation invariance but fails convexity (and hence subadditivity) as shown in Exercise 2.

    **Level 2: Convex risk measures.** Additional axiom beyond monetary: (iii) convexity: $\rho(\lambda X + (1-\lambda)Y) \le \lambda\rho(X) + (1-\lambda)\rho(Y)$. Representative example: **Entropic risk measure** $\rho_\gamma(X) = \frac{1}{\gamma}\log\mathbb{E}[e^{\gamma X}]$. It satisfies monotonicity, translation invariance, and convexity, but fails positive homogeneity (hence is not coherent), as shown in Exercise 5.

    **Level 3: Coherent risk measures.** Additional axioms beyond monetary: (iii) positive homogeneity: $\rho(\lambda X) = \lambda\rho(X)$ for $\lambda > 0$, and (iv) subadditivity: $\rho(X+Y) \le \rho(X) + \rho(Y)$. (These together imply convexity.) Representative example: **Expected Shortfall** $\text{ES}_\alpha(X) = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(X)\,du$.

    **Why each inclusion is strict:**

    - VaR is monetary but not convex $\Rightarrow$ monetary $\supsetneq$ convex.
    - The entropic risk measure is convex but not coherent $\Rightarrow$ convex $\supsetneq$ coherent.

    **Why coherence became the regulatory standard.** The Artzner et al. (1999) axioms became the standard for several reasons:

    1. **Subadditivity captures diversification.** Regulators want risk measures that reward diversification: the risk of a combined portfolio should not exceed the sum of individual risks. VaR's failure of subadditivity means it can penalize diversification, which is economically perverse.

    2. **Positive homogeneity ensures proportionality.** Doubling a position should double its risk. This makes capital requirements scale linearly with position size, which is intuitive and operationally simple.

    3. **Dual representation provides robustness.** The representation $\rho(X) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[X]$ means coherent risk measures can be interpreted as worst-case expected losses under model uncertainty. This aligns with the regulatory goal of conservatism and robustness.

    4. **Basel III/IV adopted ES.** Partly motivated by the theoretical advantages of coherence, the Basel Committee replaced VaR with Expected Shortfall as the primary market risk measure in the Fundamental Review of the Trading Book (FRTB), explicitly citing the subadditivity failure of VaR.

    5. **Mathematical tractability.** Coherent risk measures have cleaner dual representations (no penalty function), which simplifies optimization, capital allocation (via the Euler allocation), and hedging computations.
