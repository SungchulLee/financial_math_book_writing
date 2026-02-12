# Coherent Risk Measures

A **coherent risk measure** satisfies a set of axioms that formalize desirable properties of a risk metric, especially with respect to diversification and capital allocation.

---

## The Coherence Axioms

A risk measure $\rho: \mathcal{L} \to \mathbb{R}$ mapping random losses to real numbers is **coherent** if it satisfies:

### Axiom 1: Monotonicity

If $L_1 \le L_2$ almost surely, then $\rho(L_1) \le \rho(L_2)$.

**Interpretation:** Higher losses require more capital.

### Axiom 2: Translation Invariance (Cash Invariance)

$\rho(L + c) = \rho(L) + c$ for all constants $c \in \mathbb{R}$.

**Interpretation:** Adding a certain loss $c$ increases capital requirement by exactly $c$. Equivalently, adding cash $c$ reduces risk by $c$.

### Axiom 3: Positive Homogeneity

$\rho(\lambda L) = \lambda \rho(L)$ for all $\lambda > 0$.

**Interpretation:** Scaling a position scales risk proportionally. No economies or diseconomies of scale.

### Axiom 4: Subadditivity

$\rho(L_1 + L_2) \le \rho(L_1) + \rho(L_2)$.

**Interpretation:** **Diversification cannot increase risk.** Merging portfolios should not require more capital than the sum of separate capital requirements.

---

## Why Subadditivity Matters

Subadditivity encodes the **diversification principle**:

- A risk measure that fails subadditivity can penalize diversification
- Decentralized risk management becomes inconsistent
- Capital allocation to business units may exceed total capital

**Example:** If firm-wide VaR exceeds the sum of desk-level VaRs, the firm appears safer when measured in parts—a paradox.

---

## VaR vs ES: Coherence Comparison

| Property | VaR | ES |
|----------|-----|-----|
| Monotonicity | ✓ | ✓ |
| Translation Invariance | ✓ | ✓ |
| Positive Homogeneity | ✓ | ✓ |
| **Subadditivity** | ✗ (fails) | ✓ |
| **Coherent** | **No** | **Yes** |

VaR fails subadditivity in general, though it is subadditive for elliptically distributed losses (e.g., multivariate normal).

---

## Dual Representation Theorem

**Theorem (Artzner et al., 1999):** A risk measure $\rho$ is coherent if and only if there exists a set $\mathcal{Q}$ of probability measures such that:

$$
\rho(L) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^\mathbb{Q}[L]
$$

**Interpretation:** Coherent risk is the worst-case expected loss over a set of "stress" probability measures. This connects coherent risk measures to:

- Robust statistics (worst-case expectations)
- Model uncertainty (ambiguity aversion)
- Stress testing (adverse scenarios)

**ES dual representation:**
$$
\text{ES}_\alpha(L) = \sup\left\{ \mathbb{E}^\mathbb{Q}[L] : \frac{d\mathbb{Q}}{d\mathbb{P}} \le \frac{1}{1-\alpha} \right\}
$$

---

## Convex Risk Measures

**Convex risk measures** generalize coherent measures by relaxing positive homogeneity.

A risk measure $\rho$ is **convex** if:

1. Monotonicity: $L_1 \le L_2 \Rightarrow \rho(L_1) \le \rho(L_2)$
2. Translation invariance: $\rho(L + c) = \rho(L) + c$
3. **Convexity:** $\rho(\lambda L_1 + (1-\lambda)L_2) \le \lambda\rho(L_1) + (1-\lambda)\rho(L_2)$

**Note:** Positive homogeneity + subadditivity $\Rightarrow$ convexity, so coherent $\Rightarrow$ convex.

### Dual Representation of Convex Risk Measures

$$
\rho(L) = \sup_{\mathbb{Q}} \left\{ \mathbb{E}^\mathbb{Q}[L] - \alpha(\mathbb{Q}) \right\}
$$

where $\alpha(\mathbb{Q})$ is a **penalty function** measuring the plausibility of $\mathbb{Q}$.

### Entropic Risk Measure

A key example of a convex (but not coherent) risk measure:

$$
\rho_\gamma(L) = \frac{1}{\gamma} \log \mathbb{E}[e^{\gamma L}]
$$

where $\gamma > 0$ is the risk aversion parameter.

**Properties:**
- Convex but not positively homogeneous
- Penalizes tail risk exponentially
- Connected to exponential utility: $\rho_\gamma(L) = -\frac{1}{\gamma}\log(-\mathbb{E}[-e^{-\gamma(-L)}])$

---

## Spectral Risk Measures

**Spectral risk measures** form a subclass of coherent measures with explicit tail weighting.

**Definition:** A spectral risk measure has the form:

$$
\rho_\phi(L) = \int_0^1 \phi(u) \, \text{VaR}_u(L) \, du
$$

where $\phi: [0,1] \to \mathbb{R}_+$ is a **spectrum** (weight function) satisfying:

1. $\phi(u) \ge 0$ (non-negativity)
2. $\int_0^1 \phi(u) \, du = 1$ (normalization)
3. $\phi$ is non-decreasing (risk aversion)

**Interpretation:** Spectral measures weight quantiles by $\phi(u)$, putting more weight on worse outcomes.

### Expected Shortfall as a Spectral Measure

ES is spectral with:

$$
\phi_\alpha(u) = \begin{cases}
0 & u < \alpha \\
\frac{1}{1-\alpha} & u \ge \alpha
\end{cases}
$$

This assigns zero weight below the $\alpha$-quantile and uniform weight to the tail.

### Exponential Spectral Measure

$$
\phi(u) = \frac{\gamma e^{\gamma u}}{e^\gamma - 1}
$$

gives increasing weight to worse outcomes, with $\gamma$ controlling the degree of risk aversion.

---

## Law Invariance

A risk measure is **law invariant** if $\rho(L_1) = \rho(L_2)$ whenever $L_1$ and $L_2$ have the same distribution.

**Theorem (Kusuoka, 2001):** Every law-invariant coherent risk measure on $L^\infty$ can be represented as:

$$
\rho(L) = \sup_{\mu \in \mathcal{M}} \int_0^1 \text{ES}_u(L) \, d\mu(u)
$$

where $\mathcal{M}$ is a set of probability measures on $[0,1]$.

This shows that **ES is the building block** of all law-invariant coherent risk measures.

---

## Acceptance Sets

An alternative characterization uses **acceptance sets**:

$$
\mathcal{A} = \{L : \rho(L) \le 0\}
$$

The set of positions requiring no additional capital.

**Properties:**
- Coherent $\rho$ $\Leftrightarrow$ $\mathcal{A}$ is a convex cone containing constants $\le 0$
- Convex $\rho$ $\Leftrightarrow$ $\mathcal{A}$ is convex

**Reconstruction:** Given an acceptance set, the risk measure is:

$$
\rho(L) = \inf\{c : L - c \in \mathcal{A}\}
$$

---

## Capital Allocation with Coherent Measures

Coherent risk measures enable consistent capital allocation via the **Euler principle**:

If $\rho$ is positively homogeneous and differentiable, capital allocated to position $i$ is:

$$
\text{AC}_i = \frac{\partial \rho}{\partial w_i} \cdot w_i
$$

and by Euler's theorem:

$$
\sum_i \text{AC}_i = \rho(L)
$$

**For ES:**
$$
\text{AC}_i = \mathbb{E}[L_i \mid L \ge \text{VaR}_\alpha(L)]
$$

This is the **ES contribution** of position $i$.

---

## Practical Considerations

### Advantages of Coherent Measures

- Reward diversification
- Enable consistent decentralized risk management
- Support meaningful capital allocation
- Connect to robust optimization

### Challenges

- **Estimation:** Coherent measures often require tail estimation, which is data-intensive
- **Model risk:** Tail sensitivity amplifies model errors
- **Complexity:** More sophisticated than VaR

### Regulatory Adoption

Basel III's shift from VaR to ES reflects growing acceptance of coherence as a guiding principle, despite implementation challenges.

---

## Key Takeaways

- Coherence formalizes four desirable risk properties: monotonicity, translation invariance, positive homogeneity, subadditivity
- VaR fails subadditivity and is not coherent; ES satisfies all axioms
- Coherent measures have a dual representation as worst-case expectations
- Convex measures generalize coherent measures by relaxing positive homogeneity
- Spectral measures provide explicit tail weighting, with ES as a special case
- Coherence enables consistent capital allocation and supports diversification

---

## Further Reading

- Artzner, P., Delbaen, F., Eber, J.-M., & Heath, D. (1999), "Coherent Measures of Risk," *Mathematical Finance*
- Föllmer, H. & Schied, A., *Stochastic Finance: An Introduction in Discrete Time*
- Kusuoka, S. (2001), "On Law Invariant Coherent Risk Measures"
- Acerbi, C. (2002), "Spectral Measures of Risk"
- Frittelli, M. & Rosazza Gianin, E. (2002), "Putting Order in Risk Measures"
