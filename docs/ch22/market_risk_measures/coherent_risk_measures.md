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

---

## Exercises

**Exercise 1.** State the four axioms of a coherent risk measure (monotonicity, subadditivity, positive homogeneity, translation invariance). Verify that Expected Shortfall $\text{ES}_\alpha$ satisfies all four axioms. Which axiom does VaR fail?

??? success "Solution to Exercise 1"

    **The four axioms of a coherent risk measure $\rho$:**

    1. **Monotonicity:** If $L_1 \le L_2$ a.s., then $\rho(L_1) \le \rho(L_2)$. Larger losses require more capital.

    2. **Translation invariance:** $\rho(L + c) = \rho(L) + c$ for all $c \in \mathbb{R}$. Adding a certain loss $c$ increases the risk measure by exactly $c$.

    3. **Positive homogeneity:** $\rho(\lambda L) = \lambda \rho(L)$ for $\lambda > 0$. Scaling a position scales risk proportionally.

    4. **Subadditivity:** $\rho(L_1 + L_2) \le \rho(L_1) + \rho(L_2)$. Diversification does not increase risk.

    **Verification that ES satisfies all four axioms:**

    Using the integral representation $\text{ES}_\alpha(L) = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(L)\,du$:

    *Monotonicity:* If $L_1 \le L_2$ a.s., then $\text{VaR}_u(L_1) \le \text{VaR}_u(L_2)$ for all $u$, so:

    $$
    \text{ES}_\alpha(L_1) = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(L_1)\,du \le \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(L_2)\,du = \text{ES}_\alpha(L_2)
    $$

    *Translation invariance:* $\text{VaR}_u(L+c) = \text{VaR}_u(L) + c$, so:

    $$
    \text{ES}_\alpha(L+c) = \frac{1}{1-\alpha}\int_\alpha^1 [\text{VaR}_u(L) + c]\,du = \text{ES}_\alpha(L) + c
    $$

    *Positive homogeneity:* $\text{VaR}_u(\lambda L) = \lambda \text{VaR}_u(L)$ for $\lambda > 0$, so:

    $$
    \text{ES}_\alpha(\lambda L) = \frac{1}{1-\alpha}\int_\alpha^1 \lambda \text{VaR}_u(L)\,du = \lambda \text{ES}_\alpha(L)
    $$

    *Subadditivity:* This follows from the fact that for comonotonic random variables, $\text{VaR}_u(L_1+L_2) = \text{VaR}_u(L_1) + \text{VaR}_u(L_2)$, and for general random variables, $\text{VaR}_u(L_1+L_2) \le \text{VaR}_u(L_1) + \text{VaR}_u(L_2)$ after integrating against the uniform weight on $[\alpha,1]$. More precisely, using the Rockafellar-Uryasev optimization formulation:

    $$
    \text{ES}_\alpha(L_1+L_2) = \min_v \left\{v + \frac{1}{1-\alpha}\mathbb{E}[(L_1+L_2-v)^+]\right\}
    $$

    Setting $v = v_1 + v_2$ and using $(a+b-v_1-v_2)^+ \le (a-v_1)^+ + (b-v_2)^+$:

    $$
    \text{ES}_\alpha(L_1+L_2) \le \text{ES}_\alpha(L_1) + \text{ES}_\alpha(L_2)
    $$

    **Which axiom does VaR fail?** VaR fails **subadditivity**. One can construct examples (e.g., independent Bernoulli losses) where $\text{VaR}_\alpha(L_1 + L_2) > \text{VaR}_\alpha(L_1) + \text{VaR}_\alpha(L_2)$.

---

**Exercise 2.** The subadditivity axiom states $\rho(X+Y) \le \rho(X) + \rho(Y)$. Explain its economic significance in terms of diversification. Construct a numerical example with two Bernoulli loss variables where VaR at the 95% level violates subadditivity.

??? success "Solution to Exercise 2"

    **Economic significance of subadditivity:**

    The subadditivity axiom $\rho(X+Y) \le \rho(X) + \rho(Y)$ formalizes the **diversification principle**: merging two portfolios should not increase the total risk capital requirement. This has critical practical implications:

    - **Decentralized risk management:** If a firm has business units with risks $X$ and $Y$, the total capital needed for the combined firm should not exceed the sum of capital for each unit. Without subadditivity, a firm could reduce its measured risk by splitting into separate entities -- a perverse incentive.
    - **Capital allocation:** Subadditivity ensures that allocated capital sums to at most the total capital, enabling consistent top-down and bottom-up risk budgeting.
    - **Regulatory consistency:** A regulator requiring capital based on a non-subadditive measure creates incentives for regulatory arbitrage through corporate structure changes.

    **Numerical example with Bernoulli losses:**

    Let $X_1, X_2$ be independent with:

    - $\mathbb{P}(X_i = 100) = 0.04$ and $\mathbb{P}(X_i = 0) = 0.96$ for $i = 1, 2$

    **Individual VaR:** Since $F_{X_i}(0) = 0.96 \ge 0.95$:

    $$
    \text{VaR}_{0.95}(X_1) = \text{VaR}_{0.95}(X_2) = 0
    $$

    **Portfolio distribution** ($X_1 + X_2$, independent):

    | Value | Probability | Cumulative |
    |-------|-------------|------------|
    | 0 | $0.96^2 = 0.9216$ | 0.9216 |
    | 100 | $2(0.04)(0.96) = 0.0768$ | 0.9984 |
    | 200 | $0.04^2 = 0.0016$ | 1.0000 |

    Since $F_{X_1+X_2}(0) = 0.9216 < 0.95$, the 95th percentile is:

    $$
    \text{VaR}_{0.95}(X_1 + X_2) = 100
    $$

    **Subadditivity violation:**

    $$
    \text{VaR}_{0.95}(X_1 + X_2) = 100 > 0 + 0 = \text{VaR}_{0.95}(X_1) + \text{VaR}_{0.95}(X_2)
    $$

    Combining two zero-VaR positions produces a positive VaR -- diversification is penalized.

---

**Exercise 3.** The dual representation theorem states that a coherent risk measure can be written as $\rho(X) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[-X]$. Explain the economic interpretation: $\rho$ evaluates the worst-case expected loss over a set of "stress" probability measures $\mathcal{Q}$. What determines the set $\mathcal{Q}$ for Expected Shortfall?

??? success "Solution to Exercise 3"

    **Dual representation theorem (Artzner et al., 1999):**

    A coherent risk measure can be written as:

    $$
    \rho(X) = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[X]
    $$

    **Economic interpretation:**

    - The set $\mathcal{Q}$ represents a family of **stress scenarios** or **adverse probability measures** (sometimes called "generalized scenarios" or "test measures").
    - For each $\mathbb{Q} \in \mathcal{Q}$, $\mathbb{E}^\mathbb{Q}[X]$ evaluates the expected loss under that stress scenario.
    - The risk measure takes the **worst case** over all plausible scenarios.
    - This connects to **model uncertainty** (ambiguity aversion): the decision-maker does not trust a single model and instead evaluates risk under the most adverse model in a set.
    - It also connects to **stress testing**: the regulator or risk manager asks "what is the worst expected outcome across a range of plausible stress environments?"

    **The set $\mathcal{Q}$ for Expected Shortfall:**

    For $\text{ES}_\alpha$, the dual representation is:

    $$
    \text{ES}_\alpha(L) = \sup\left\{\mathbb{E}^\mathbb{Q}[L] : \frac{d\mathbb{Q}}{d\mathbb{P}} \le \frac{1}{1-\alpha}\right\}
    $$

    The set $\mathcal{Q}$ consists of all probability measures $\mathbb{Q}$ that are absolutely continuous with respect to $\mathbb{P}$ and whose Radon–Nikodym derivative (likelihood ratio) is bounded above by $\frac{1}{1-\alpha}$.

    **Interpretation:** For $\alpha = 0.95$, the constraint is $\frac{d\mathbb{Q}}{d\mathbb{P}} \le 20$. This means $\mathbb{Q}$ can multiply the probability of any event by at most 20. The worst-case $\mathbb{Q}^*$ concentrates probability mass on the worst $5\%$ of outcomes, reweighting them by a factor of $\frac{1}{1-\alpha} = 20$ and assigning zero weight to the remaining $95\%$. This is exactly the conditional expectation in the worst tail, which is the definition of ES.

---

**Exercise 4.** Positive homogeneity requires $\rho(\lambda X) = \lambda\,\rho(X)$ for $\lambda > 0$. Explain why this axiom implies that doubling a position doubles the risk. Is this always economically reasonable? When might a convex (but not positively homogeneous) risk measure be more appropriate?

??? success "Solution to Exercise 4"

    **Positive homogeneity** states that $\rho(\lambda X) = \lambda \rho(X)$ for all $\lambda > 0$.

    **Why doubling a position doubles the risk:**

    If a portfolio has loss $X$ and we double the position to $2X$, positive homogeneity requires $\rho(2X) = 2\rho(X)$. This means risk scales linearly with position size. The economic reasoning is:

    - A position twice as large should require twice as much capital.
    - There are no economies of scale in risk: holding more of the same risk does not reduce the per-unit risk.
    - This ensures consistent capital allocation across desks with different position sizes.

    **When positive homogeneity may not be economically reasonable:**

    1. **Liquidity risk:** Doubling a large position may more than double the risk because liquidating a larger position incurs greater market impact costs. A \$100M position in an illiquid bond is more than twice as risky as a \$50M position due to price impact during forced selling.

    2. **Concentration risk:** Very large positions in a single name may face non-linear risk amplification (e.g., being unable to hedge, counterparty credit deterioration).

    3. **Margin/funding risk:** Larger positions require proportionally more margin, and funding costs may increase non-linearly during stress.

    **When convex (but not positively homogeneous) risk measures are more appropriate:**

    A convex risk measure satisfies:

    $$
    \rho(\lambda X + (1-\lambda)Y) \le \lambda \rho(X) + (1-\lambda)\rho(Y), \quad 0 \le \lambda \le 1
    $$

    but not necessarily $\rho(\lambda X) = \lambda \rho(X)$. This allows for:

    - **Superlinear scaling:** $\rho(2X) > 2\rho(X)$, capturing the idea that concentration amplifies risk.
    - **Liquidity adjustment:** The penalty for large positions can be built into the measure.

    The **entropic risk measure** $\rho_\gamma(L) = \frac{1}{\gamma}\log \mathbb{E}[e^{\gamma L}]$ is convex but not positively homogeneous. It satisfies $\rho_\gamma(\lambda L) \ge \lambda \rho_\gamma(L)$ for $\lambda > 1$ (via Jensen's inequality applied to the convex function $e^{\gamma \cdot}$), capturing the economic intuition that scaling up a risky position increases risk more than proportionally.

---

**Exercise 5.** A portfolio has two positions: $X_1$ with $\text{ES}_{0.95}(X_1) = 10$ and $X_2$ with $\text{ES}_{0.95}(X_2) = 15$. Using the subadditivity property, what can you conclude about $\text{ES}_{0.95}(X_1 + X_2)$? Compute the exact $\text{ES}_{0.95}(X_1 + X_2)$ if $X_1$ and $X_2$ are independent standard normals.

??? success "Solution to Exercise 5"

    **Upper bound from subadditivity:**

    Since ES is subadditive:

    $$
    \text{ES}_{0.95}(X_1 + X_2) \le \text{ES}_{0.95}(X_1) + \text{ES}_{0.95}(X_2) = 10 + 15 = 25
    $$

    We can only conclude that $\text{ES}_{0.95}(X_1 + X_2) \le 25$. The exact value depends on the joint distribution (the copula) of $X_1$ and $X_2$.

    **Exact computation for independent standard normals:**

    Let $X_1, X_2 \sim N(0,1)$ independently. Since the problem states $\text{ES}_{0.95}(X_1) = 10$ and $\text{ES}_{0.95}(X_2) = 15$, these are not standard normals with unit variance. However, let us compute the exact ES for the sum.

    For standard normals $Z_1, Z_2 \sim N(0,1)$ independently, the sum $Z_1 + Z_2 \sim N(0, 2)$ has standard deviation $\sqrt{2}$.

    The ES formula for $N(0, \sigma^2)$ at level $\alpha$ is:

    $$
    \text{ES}_\alpha = \sigma \cdot \frac{\phi(\Phi^{-1}(\alpha))}{1 - \alpha}
    $$

    For $\alpha = 0.95$: $\Phi^{-1}(0.95) = 1.645$, $\phi(1.645) \approx 0.1031$:

    $$
    \text{ES}_{0.95}(Z_i) = 1 \times \frac{0.1031}{0.05} = 2.063
    $$

    $$
    \text{ES}_{0.95}(Z_1 + Z_2) = \sqrt{2} \times \frac{0.1031}{0.05} = \sqrt{2} \times 2.063 \approx 2.917
    $$

    **Diversification benefit:**

    $$
    \text{ES}_{0.95}(Z_1) + \text{ES}_{0.95}(Z_2) = 2 \times 2.063 = 4.126
    $$

    $$
    \text{ES}_{0.95}(Z_1 + Z_2) = 2.917 < 4.126
    $$

    The ratio is $2.917 / 4.126 = \sqrt{2}/2 \approx 0.707$, confirming that ES rewards diversification. For the original problem with $\text{ES}_{0.95}(X_1) = 10$ and $\text{ES}_{0.95}(X_2) = 15$, if $X_1 = 10Z_1/2.063$ and $X_2 = 15Z_2/2.063$ (scaled normals), then $X_1 + X_2 \sim N(0, \sigma_1^2 + \sigma_2^2)$ where $\sigma_1 = 10/2.063$ and $\sigma_2 = 15/2.063$:

    $$
    \text{ES}_{0.95}(X_1+X_2) = \sqrt{\sigma_1^2 + \sigma_2^2} \times 2.063 = \sqrt{10^2 + 15^2}\frac{2.063}{2.063} = \sqrt{325} \approx 18.03
    $$

    This is indeed less than $10 + 15 = 25$, confirming subadditivity with a substantial diversification benefit.

---

**Exercise 6.** The Basel Committee replaced VaR with Expected Shortfall in its Fundamental Review of the Trading Book (FRTB). Explain the regulatory motivation for this change. What practical challenges arise from using ES instead of VaR (e.g., backtesting difficulty, elicitability)?

??? success "Solution to Exercise 6"

    **Regulatory motivation for replacing VaR with ES:**

    1. **Subadditivity and diversification:** VaR is not subadditive, meaning it can penalize diversification. Under a VaR-based regime, a bank could reduce its capital requirement by splitting into separate entities -- a form of regulatory arbitrage. ES is subadditive and thus rewards diversification, aligning capital requirements with economic intuition.

    2. **Tail risk capture:** VaR only measures a quantile threshold and is completely blind to the severity of losses beyond that threshold (the "cliff effect"). ES measures the average loss in the tail, providing information about how bad losses can be, not just the probability of exceeding a threshold.

    3. **Manipulation resistance:** Under VaR, traders can structure positions to have risk concentrated just beyond the VaR threshold (e.g., selling deep out-of-the-money options). ES captures these hidden tail risks because it averages over the entire tail.

    4. **Theoretical soundness:** ES is a coherent risk measure satisfying all four axioms of Artzner et al. (1999). The coherence framework provides a principled foundation for capital allocation and risk aggregation.

    5. **Confidence level choice:** FRTB uses ES at the 97.5% level, which is calibrated to produce similar capital levels as the former 99% VaR while providing better tail sensitivity.

    **Practical challenges of using ES instead of VaR:**

    1. **Backtesting difficulty:** ES is not directly elicitable -- there is no scoring function that ES uniquely minimizes. This makes it fundamentally harder to backtest ES than VaR, where a simple exceedance count suffices. The Kupiec and Christoffersen tests for VaR have no direct ES analogue. Instead, practitioners must use:
        - Joint backtesting of (VaR, ES) using the Fissler-Ziegel framework
        - The Acerbi-Szekely test based on tail expectations
        - McNeil-Frey residual approaches

    2. **Estimation uncertainty:** ES depends on the mean of tail observations, which are scarce by definition. The estimation variance of ES is higher than that of VaR. For a sample of size $n$, only about $n(1-\alpha)$ observations contribute to the ES estimate, leading to noisy estimates especially at high confidence levels.

    3. **Model sensitivity:** ES is more sensitive to model assumptions in the far tail. Small changes in the assumed distribution can produce large changes in ES, amplifying model risk. This is the flip side of ES being more informative about the tail.

    4. **Procyclicality:** Because ES responds to tail severity, it can be more procyclical than VaR -- rising sharply during stress episodes and increasing capital requirements precisely when banks can least afford to raise capital.

    5. **Computational cost:** ES estimation, particularly via Monte Carlo, requires more simulations to achieve a given precision compared to VaR quantile estimation, because the tail average has higher variance than the quantile estimator.
