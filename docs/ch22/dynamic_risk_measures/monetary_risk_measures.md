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

### Value-at-Risk

$$
\text{VaR}_\alpha(X) = \inf\{x : \mathbb{P}(X \le x) \ge \alpha\}
$$

- Monetary: Yes (monotone and translation invariant)
- Convex: **No** in general (fails convexity for non-elliptical distributions)
- Coherent: **No** (fails subadditivity)
- VaR is subadditive for elliptically distributed losses (e.g., multivariate normal)

### Expected Shortfall

$$
\text{ES}_\alpha(X) = \frac{1}{1-\alpha} \int_\alpha^1 \text{VaR}_u(X) \, du
$$

- Monetary: Yes
- Convex: Yes
- Coherent: **Yes**
- Dual set: $\mathcal{Q} = \left\{\mathbb{Q} : \frac{d\mathbb{Q}}{d\mathbb{P}} \le \frac{1}{1-\alpha}\right\}$

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
