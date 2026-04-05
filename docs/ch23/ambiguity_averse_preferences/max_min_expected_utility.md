# Max–Min Expected Utility


## Introduction


**Max-min expected utility (MEU)** provides the foundational framework for rational decision-making under Knightian uncertainty, where decision-makers face ambiguity about the true probability distribution governing outcomes. Unlike classical expected utility theory, which assumes a unique subjective probability, MEU allows for a **set of priors** and evaluates acts by their worst-case expected utility.

This framework, axiomatized by Gilboa and Schmeidler (1989), has profound implications for:
1. **Portfolio selection**: Understanding why investors hold undiversified portfolios or avoid certain asset classes
2. **Asset pricing**: Explaining puzzles like the equity premium and home bias
3. **Risk management**: Justifying conservative positions under model uncertainty
4. **Contract design**: Structuring robust financial instruments

The mathematical foundations connect decision theory, functional analysis, and convex optimization, providing both theoretical insights and practical tools for financial decision-making under ambiguity.

## Classical Expected Utility


### 1. Von Neumann–Morgenstern Framework


**Setup**: Consider a finite state space $\Omega = \{\omega_1, \ldots, \omega_n\}$ and outcome space $X \subseteq \mathbb{R}$.

**Acts**: An act $f: \Omega \to X$ maps states to outcomes. The set of all acts is $\mathcal{F}$.

**Lotteries**: A lottery $p = (p_1, \ldots, p_m)$ assigns probabilities to outcomes $x_1, \ldots, x_m$.

**VNM Axioms**: Preferences $\succeq$ over lotteries satisfy:
1. **Completeness**: For all $p, q$: either $p \succeq q$ or $q \succeq p$
2. **Transitivity**: $p \succeq q$ and $q \succeq r$ implies $p \succeq r$
3. **Continuity**: If $p \succ q \succ r$, there exist $\alpha, \beta \in (0,1)$ such that $\alpha p + (1-\alpha) r \succ q \succ \beta p + (1-\beta) r$
4. **Independence**: $p \succeq q$ iff $\alpha p + (1-\alpha) r \succeq \alpha q + (1-\alpha) r$ for all $\alpha \in (0,1)$

**Representation Theorem** (von Neumann–Morgenstern): Preferences satisfy VNM axioms iff there exists a utility function $u: X \to \mathbb{R}$ such that:

$$
p \succeq q \iff \sum_{i=1}^m p_i u(x_i) \geq \sum_{i=1}^m q_i u(x_i)
$$

The utility function $u$ is unique up to positive affine transformation.

### 2. Savage's Subjective Expected Utility


**Extension to Uncertainty**: Savage (1954) extended VNM to situations where probabilities are not given but must be inferred from behavior.

**Savage Axioms**: Including the **Sure-Thing Principle**:

If $f(\omega) = g(\omega)$ for $\omega \in E$ and $f \succeq g$ when $f(\omega) = h(\omega)$ for $\omega \notin E$, then $f \succeq g$ when $f(\omega) = h'(\omega)$ for $\omega \notin E$.

**Representation Theorem** (Savage): Under the Savage axioms, there exist:
- A unique probability measure $P$ on $\Omega$
- A utility function $u: X \to \mathbb{R}$ (unique up to positive affine transformation)

such that:

$$
f \succeq g \iff \mathbb{E}_P[u(f)] \geq \mathbb{E}_P[u(g)]
$$

**Limitation**: Savage's framework assumes the decision-maker can always form precise probabilistic beliefs, which the Ellsberg paradox challenges.

## The Ellsberg Paradox


### 1. Experimental Setup


**Two-Urn Experiment** (Ellsberg, 1961):

**Urn I**: Contains exactly 50 red and 50 black balls (known composition)
**Urn II**: Contains 100 balls, some red and some black, but exact composition unknown

**Gambles**:
- $f_1$: Win \$100 if red drawn from Urn I
- $f_2$: Win \$100 if black drawn from Urn I  
- $f_3$: Win \$100 if red drawn from Urn II
- $f_4$: Win \$100 if black drawn from Urn II

**Typical Preferences**: Most subjects exhibit:

$$
f_1 \sim f_2 \succ f_3 \sim f_4
$$

preferring gambles with known probabilities over ambiguous ones.

### 2. Violation of Savage's Axioms


**Subjective Probability Argument**: Under Savage's framework, let $p$ be the subjective probability of red in Urn II.

From $f_1 \succ f_3$:

$$
0.5 \cdot u(100) + 0.5 \cdot u(0) > p \cdot u(100) + (1-p) \cdot u(0)
$$

This implies $p < 0.5$.

From $f_2 \succ f_4$:

$$
0.5 \cdot u(100) + 0.5 \cdot u(0) > (1-p) \cdot u(100) + p \cdot u(0)
$$

This implies $1-p < 0.5$, hence $p > 0.5$.

**Contradiction**: No single probability $p$ can rationalize these preferences, violating the Sure-Thing Principle.

### 3. Interpretation


**Ambiguity Aversion**: The Ellsberg preferences reveal that decision-makers systematically avoid **ambiguous** situations where probabilities are unknown, even when the "average" probability might be the same.

**Multiple Priors**: Rather than a single $p$, consider a set $\mathcal{P} = \{P: P(\text{red}) \in [p_{\min}, p_{\max}]\}$.

Ellsberg preferences are consistent with evaluating acts by their **worst-case** expected utility over $\mathcal{P}$.

## Gilboa–Schmeidler Axiomatization


### 1. Setup and Notation


**Probability Space**: $(\Omega, \Sigma)$ where $\Omega$ is a state space and $\Sigma$ is a $\sigma$-algebra.

**Outcome Space**: $X$ is a convex subset of a vector space (typically $\mathbb{R}$).

**Acts**: $\mathcal{F} = \{f: \Omega \to X \text{ measurable}\}$ is the set of acts.

**Constant Acts**: For $x \in X$, denote by $\bar{x}$ the constant act $f(\omega) = x$ for all $\omega$.

**Mixtures**: For acts $f, g$ and $\alpha \in [0,1]$, define $\alpha f + (1-\alpha) g$ pointwise:

$$
(\alpha f + (1-\alpha) g)(\omega) = \alpha f(\omega) + (1-\alpha) g(\omega)
$$

### 2. Gilboa–Schmeidler Axioms


**Axiom 1** (Weak Order): $\succeq$ is complete and transitive.

**Axiom 2** (Continuity): For all $f, g, h \in \mathcal{F}$, the sets $\{\alpha \in [0,1]: \alpha f + (1-\alpha) g \succeq h\}$ and $\{\alpha \in [0,1]: h \succeq \alpha f + (1-\alpha) g\}$ are closed.

**Axiom 3** (Monotonicity): If $f(\omega) \succeq g(\omega)$ for all $\omega \in \Omega$ (comparing constant acts), then $f \succeq g$.

**Axiom 4** (C-Independence): For all $f, g \in \mathcal{F}$, constant acts $\bar{x}$, and $\alpha \in (0,1)$:

$$
f \succeq g \iff \alpha f + (1-\alpha) \bar{x} \succeq \alpha g + (1-\alpha) \bar{x}
$$

**Axiom 5** (Uncertainty Aversion): For all $f, g \in \mathcal{F}$ and $\alpha \in (0,1)$:

$$
f \sim g \implies \alpha f + (1-\alpha) g \succeq f
$$

**Axiom 6** (Non-Degeneracy): There exist $f, g \in \mathcal{F}$ such that $f \succ g$.

### 3. Representation Theorem


**Theorem** (Gilboa–Schmeidler, 1989): Preferences $\succeq$ on $\mathcal{F}$ satisfy Axioms 1-6 if and only if there exist:
- A non-empty, closed, convex set of probability measures $\mathcal{P}$ on $(\Omega, \Sigma)$
- A non-constant affine utility function $u: X \to \mathbb{R}$

such that for all $f, g \in \mathcal{F}$:

$$
f \succeq g \iff \min_{P \in \mathcal{P}} \mathbb{E}_P[u(f)] \geq \min_{P \in \mathcal{P}} \mathbb{E}_P[u(g)]
$$

Moreover:
- $u$ is unique up to positive affine transformation
- $\mathcal{P}$ is unique

**Proof Sketch**:

*Necessity*: Verify that the max-min representation satisfies all axioms.
- Monotonicity and continuity follow from properties of expectations
- C-Independence holds because constant acts have the same expectation under all $P \in \mathcal{P}$
- Uncertainty aversion follows from the convexity of $\mathcal{P}$ and the minimum operator

*Sufficiency*: The proof uses separation arguments in functional analysis.
1. Define a functional $I: B(\Omega) \to \mathbb{R}$ representing preferences over simple acts
2. Show $I$ is monotone, constant-additive, and positively homogeneous
3. Apply a representation theorem for such functionals (Schmeidler, 1989)
4. The key step uses uncertainty aversion to establish that $I$ is **concave**, leading to the minimum over a set of priors

### 4. Key Properties of MEU


**Property 1** (Worst-Case Evaluation): The decision-maker evaluates each act by its minimum expected utility:

$$
V(f) = \min_{P \in \mathcal{P}} \mathbb{E}_P[u(f)]
$$

**Property 2** (Constant Preserving): For constant acts $\bar{x}$:

$$
V(\bar{x}) = u(x)
$$

**Property 3** (Quasi-Concavity): The preference functional is quasi-concave:

$$
V(\alpha f + (1-\alpha) g) \geq \min\{V(f), V(g)\}
$$

**Property 4** (Positive Homogeneity): For $\lambda > 0$:

$$
V(\lambda f) = \lambda V(f)
$$

when $u$ is normalized appropriately.

## Characterization of the Set of Priors


### 1. Revealed Priors


**Definition**: The set of priors $\mathcal{P}$ is **revealed** by preferences through hedging behavior.

**Unambiguous Events**: An event $A \in \Sigma$ is **unambiguous** if:

$$
P(A) = Q(A) \quad \text{for all } P, Q \in \mathcal{P}
$$

**Characterization**: $A$ is unambiguous iff preferences over acts that differ only on $A$ satisfy the independence axiom.

### 2. Core of a Capacity


**Capacity**: A set function $\nu: \Sigma \to [0,1]$ satisfying:
1. $\nu(\emptyset) = 0$, $\nu(\Omega) = 1$
2. $A \subseteq B \implies \nu(A) \leq \nu(B)$

**Core**: The core of capacity $\nu$ is:

$$
\text{core}(\nu) = \{P \in \mathcal{M}_1(\Omega): P(A) \geq \nu(A) \text{ for all } A \in \Sigma\}
$$

**Connection**: Under MEU with priors $\mathcal{P}$:

$$
\nu(A) = \min_{P \in \mathcal{P}} P(A)
$$

and $\mathcal{P} = \text{core}(\nu)$ when $\nu$ is a **convex** capacity.

### 3. ε-Contamination


**Definition**: The $\varepsilon$-contamination model specifies:

$$
\mathcal{P}_{\varepsilon} = \{(1-\varepsilon) P_0 + \varepsilon Q: Q \in \mathcal{M}_1(\Omega)\}
$$

for a reference measure $P_0$ and contamination level $\varepsilon \in [0,1]$.

**MEU with $\varepsilon$-Contamination**:

$$
V(f) = (1-\varepsilon) \mathbb{E}_{P_0}[u(f)] + \varepsilon \inf_{\omega \in \Omega} u(f(\omega))
$$

**Interpretation**: The decision-maker places weight $(1-\varepsilon)$ on the baseline model and weight $\varepsilon$ on the worst possible outcome.

## Financial Applications


### 1. Portfolio Choice Under Ambiguity


**Setup**: An investor chooses portfolio weights $w \in \mathbb{R}^n$ for $n$ assets with random returns $R = (R_1, \ldots, R_n)$.

**Classical Mean-Variance**:

$$
\max_w \left\{ w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w \right\}
$$

where $\mu = \mathbb{E}[R]$ and $\Sigma = \text{Cov}(R)$.

**Ambiguity About Mean**: Consider uncertainty set for expected returns:

$$
\mathcal{U}_{\mu} = \{\mu: (\mu - \hat{\mu})^\top \Sigma^{-1} (\mu - \hat{\mu}) \leq \kappa^2\}
$$

**MEU Portfolio Problem**:

$$
\max_w \min_{\mu \in \mathcal{U}_{\mu}} \left\{ w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w \right\}
$$

**Solution**: The worst-case mean is:

$$
\mu^*(w) = \hat{\mu} - \kappa \frac{\Sigma w}{\sqrt{w^\top \Sigma w}}
$$

Substituting:

$$
\max_w \left\{ w^\top \hat{\mu} - \kappa \sqrt{w^\top \Sigma w} - \frac{\lambda}{2} w^\top \Sigma w \right\}
$$

**Result**: The optimal portfolio is:

$$
w^* = \frac{1}{\lambda + \kappa / \sqrt{w^{*\top} \Sigma w^*}} \Sigma^{-1} \hat{\mu}
$$

Ambiguity aversion $\kappa > 0$ shrinks the position toward zero, reducing leverage.

### 2. Equity Premium Under Ambiguity


**Puzzle**: The historical equity premium ($\approx 6\%$) is too high to be explained by reasonable levels of risk aversion.

**MEU Explanation**: With ambiguity about the equity return distribution:

$$
\mathbb{E}[R_{\text{equity}}] - R_f = \gamma \cdot \text{Cov}(R_{\text{equity}}, C) + \text{Ambiguity Premium}
$$

where the ambiguity premium compensates investors for bearing uncertainty about the true distribution.

**Hansen-Sargent (2001)**: Calibrating with detection error probability $\approx 10\%$ generates equity premium consistent with historical data under reasonable risk aversion ($\gamma \approx 2$).

### 3. Home Bias


**Observation**: Investors hold disproportionately large shares of domestic assets relative to mean-variance optimization.

**MEU Explanation**: Investors may have:
- Precise beliefs about domestic asset returns (small $\mathcal{P}$)
- Ambiguous beliefs about foreign asset returns (large $\mathcal{P}$)

Under MEU, the worst-case expected return for foreign assets is lower, reducing optimal foreign holdings.

**Empirical Support**: Home bias is more pronounced for:
- Assets in unfamiliar markets
- Periods of heightened uncertainty
- Investors with less financial sophistication

### 4. Robust Option Pricing


**Volatility Uncertainty**: The true volatility $\sigma$ lies in $[\underline{\sigma}, \overline{\sigma}]$.

**Set of Risk-Neutral Measures**:

$$
\mathcal{Q} = \{\mathbb{Q}: \text{price process is } \mathbb{Q}\text{-martingale with } \sigma \in [\underline{\sigma}, \overline{\sigma}]\}
$$

**Buyer's Price** (MEU with negative payoff):

$$
V_{\text{buy}} = \max_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \Phi(S_T)]
$$

**Seller's Price** (MEU):

$$
V_{\text{sell}} = \min_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \Phi(S_T)]
$$

**Bid-Ask Spread**: $V_{\text{sell}} - V_{\text{buy}}$ reflects model uncertainty.

## Comparison with Alternative Models


### 1. Choquet Expected Utility


**Definition**: For a capacity $\nu$ and act $f$:

$$
V(f) = \int u(f) \, d\nu
$$

using the Choquet integral.

**Choquet Integral**:

$$
\int u(f) \, d\nu = \int_0^{\infty} \nu(\{u(f) \geq t\}) \, dt + \int_{-\infty}^0 [\nu(\{u(f) \geq t\}) - 1] \, dt
$$

**Relation to MEU**: When $\nu$ is convex:

$$
\int u(f) \, d\nu = \min_{P \in \text{core}(\nu)} \mathbb{E}_P[u(f)]
$$

so Choquet expected utility coincides with MEU.

**Non-Convex Capacities**: CEU is more general, allowing for both ambiguity aversion (convex $\nu$) and ambiguity seeking (concave $\nu$).

### 2. Smooth Ambiguity Model


**Klibanoff-Marinacci-Mukerji (2005)**: Preferences represented by:

$$
V(f) = \int_{\mathcal{P}} \phi\left(\mathbb{E}_P[u(f)]\right) d\mu(P)
$$

where:
- $u$: Utility function (risk attitude)
- $\phi$: Ambiguity attitude function
- $\mu$: Second-order probability over $\mathcal{P}$

**Interpretation**:
1. Compute expected utility $\mathbb{E}_P[u(f)]$ for each $P \in \mathcal{P}$
2. Apply ambiguity transformation $\phi$
3. Average over second-order beliefs $\mu$

**Ambiguity Aversion**: $\phi$ concave $\Leftrightarrow$ ambiguity aversion

**Advantages over MEU**:
- Separates likelihood beliefs ($\mu$) from ambiguity attitudes ($\phi$)
- Allows for smooth preferences (no kinks)
- More tractable for dynamic optimization

### 3. Variational Preferences


**Maccheroni-Marinacci-Rustichini (2006)**:

$$
V(f) = \min_{P \in \mathcal{M}_1(\Omega)} \left\{\mathbb{E}_P[u(f)] + c(P)\right\}
$$

where $c: \mathcal{M}_1(\Omega) \to [0, \infty]$ is a convex, lower semicontinuous cost function with $\inf_P c(P) = 0$.

**Special Cases**:
- **MEU**: $c(P) = 0$ if $P \in \mathcal{P}$, else $c(P) = \infty$
- **Multiplier Preferences**: $c(P) = \theta D_{\text{KL}}(P \| P_0)$

**Axiomatization**: Replace uncertainty aversion with **weak certainty independence**.

## Dynamic Considerations


### 1. Time Consistency Problem


**Issue**: MEU preferences may exhibit **time inconsistency** in dynamic settings.

**Example**: Consider a two-period problem. At $t=0$, the agent plans optimally. At $t=1$, after receiving information, the agent may prefer to deviate from the $t=0$ plan.

**Source**: The minimum over priors may be achieved by different measures at different times.

### 2. Rectangularity


**Definition** (Epstein-Schneider, 2003): A set of priors $\mathcal{P}$ is **rectangular** with respect to filtration $\{\mathcal{F}_t\}$ if:

$$
\mathcal{P} = \{P: P(\cdot | \mathcal{F}_t) \in \mathcal{P}_t(\omega) \text{ for all } t, \omega\}
$$

where $\mathcal{P}_t(\omega)$ is a family of conditional distributions.

**Characterization**: $\mathcal{P}$ is rectangular iff for any $P, Q \in \mathcal{P}$ and stopping time $\tau$, the "pasted" measure $P \otimes_{\tau} Q$ (using $P$ before $\tau$ and $Q$ after) is also in $\mathcal{P}$.

### 3. Dynamic Consistency Theorem


**Theorem** (Epstein-Schneider): MEU preferences are dynamically consistent if and only if the set of priors $\mathcal{P}$ is rectangular.

**Implication**: For dynamic applications, one must either:
1. Restrict to rectangular prior sets
2. Accept time inconsistency and model sophisticated agents
3. Use alternative preference models (e.g., smooth ambiguity)

### 4. Recursive MEU


**Formulation**: With rectangular priors, the value function satisfies:

$$
V_t = \min_{P \in \mathcal{P}_t} \mathbb{E}_P\left[u(c_t) + \beta V_{t+1} \,|\, \mathcal{F}_t\right]
$$

**Bellman Equation**: Under appropriate regularity:

$$
V(x) = \min_{P \in \mathcal{P}} \max_a \left\{\mathbb{E}_P[u(x, a) + \beta V(x') \,|\, x]\right\}
$$

with state transition $x' = f(x, a, \epsilon)$.

## Computational Methods


### 1. Linear Programming Formulation


For finite $\Omega = \{\omega_1, \ldots, \omega_n\}$ and finite $\mathcal{P} = \{P^1, \ldots, P^m\}$:

**Primal Problem** (Find optimal act):

$$
\max_{f \in \mathcal{F}} \min_{k=1,\ldots,m} \sum_{i=1}^n P^k(\omega_i) u(f(\omega_i))
$$

**Epigraph Reformulation**:

$$
\begin{aligned}
\max_{f, t} \quad & t \\
\text{s.t.} \quad & \sum_{i=1}^n P^k(\omega_i) u(f(\omega_i)) \geq t, \quad k = 1, \ldots, m \\
& f \in \mathcal{F}
\end{aligned}
$$

This is a linear program when $u$ is linear and $\mathcal{F}$ is polyhedral.

### 2. Semidefinite Programming


For ellipsoidal uncertainty sets:

$$
\mathcal{U} = \{(\mu, \Sigma): \|A(\mu - \hat{\mu})\|_2 \leq 1, \|B(\Sigma - \hat{\Sigma})\|_F \leq 1\}
$$

The robust portfolio problem can be reformulated as an SDP using Schur complements and S-lemma.

### 3. Sampling-Based Methods


**Monte Carlo**: 
1. Sample $P^1, \ldots, P^N$ from a distribution over $\mathcal{P}$
2. Approximate $\min_{P \in \mathcal{P}} \mathbb{E}_P[u(f)] \approx \min_{k=1,\ldots,N} \mathbb{E}_{P^k}[u(f)]$
3. Increase $N$ for tighter approximation

**Scenario Optimization**: Use worst-case scenarios to construct conservative solutions with probabilistic guarantees.

## Empirical Evidence


### 1. Laboratory Experiments


**Ellsberg-Type Experiments**: Consistent finding of ambiguity aversion across demographics.

**Domain Dependence**: 
- Gains domain: Ambiguity aversion (prefer known probabilities)
- Losses domain: Ambiguity seeking (prefer unknown probabilities)

**Competence Hypothesis** (Heath-Tversky): Ambiguity aversion decreases when subjects feel competent about the domain.

### 2. Field Evidence


**Portfolio Holdings**: 
- Investors underweight ambiguous assets (emerging markets, new technologies)
- Ambiguity aversion correlates with demographic characteristics (age, education)

**Insurance Markets**: 
- Demand for catastrophe insurance exceeds actuarially fair prices
- Consistent with ambiguity aversion about rare events

**Corporate Finance**: 
- Managers exhibit ambiguity aversion in capital budgeting
- Preference for projects with well-understood risks

### 3. Market Implications


**Option Prices**: Implied volatility smiles may reflect ambiguity about the return distribution.

**Credit Spreads**: Excess spreads beyond default probabilities may compensate for ambiguity.

**Liquidity Premium**: Illiquid assets command higher returns partly due to ambiguity about fair value.

## Summary and Key Insights


### 1. Theoretical Contributions


1. **Axiomatic Foundation**: Gilboa-Schmeidler axioms provide rigorous foundation for ambiguity-sensitive preferences

2. **Multiple Priors**: The set $\mathcal{P}$ captures genuine uncertainty about probabilities, not just risk

3. **Worst-Case Evaluation**: MEU formalizes cautious, conservative decision-making

4. **Dynamic Extension**: Rectangularity characterizes when MEU is time-consistent

### 2. Financial Implications


1. **Portfolio Choice**: Ambiguity aversion leads to more conservative, less leveraged positions

2. **Asset Pricing**: Ambiguity premiums help explain equity premium and other puzzles

3. **Risk Management**: MEU justifies stress testing and worst-case analysis

4. **Product Design**: Financial instruments should account for client ambiguity aversion

### 3. Limitations


1. **Extreme Pessimism**: Pure worst-case may be too conservative

2. **Computational Complexity**: Optimization over sets of priors can be challenging

3. **Dynamic Inconsistency**: Without rectangularity, MEU agents are time-inconsistent

4. **Calibration**: Difficult to elicit the set of priors from market data

### 4. Extensions


- Smooth ambiguity models for tractability
- Variational preferences for flexible penalty functions
- Source-dependent ambiguity for domain-specific uncertainty
- Learning and updating of ambiguous beliefs

Max-min expected utility provides the theoretical foundation for understanding decision-making under Knightian uncertainty, with profound implications for financial economics and practical applications in portfolio management, risk assessment, and product design.

---

## Exercises

**Exercise 1.** Consider the Ellsberg two-urn experiment. Suppose a decision-maker has MEU preferences with utility $u(x) = x$ and prior set $\mathcal{P} = \{P : P(\text{red from Urn II}) \in [0.3, 0.7]\}$. Compute the MEU value of each gamble $f_1, f_2, f_3, f_4$ (where a win pays \$100 and a loss pays \$0). Verify that the resulting preference ordering is $f_1 \sim f_2 \succ f_3 \sim f_4$, consistent with Ellsberg-type behavior.

??? success "Solution to Exercise 1"
    The utility is $u(x) = x$ (linear). The prior set for Urn II is $\mathcal{P} = \{P : P(\text{red}) \in [0.3, 0.7]\}$.

    **Gamble $f_1$** (red from Urn I): The composition of Urn I is known exactly, so $P(\text{red}) = 0.5$ for all $P \in \mathcal{P}_{\text{Urn I}}$. There is no ambiguity:

    $$
    V(f_1) = \min_P \mathbb{E}_P[f_1] = 0.5 \times 100 + 0.5 \times 0 = 50
    $$

    **Gamble $f_2$** (black from Urn I): Similarly, $P(\text{black}) = 0.5$ for Urn I:

    $$
    V(f_2) = 0.5 \times 100 + 0.5 \times 0 = 50
    $$

    **Gamble $f_3$** (red from Urn II): The worst-case prior minimizes $P(\text{red}) \times 100$, which is minimized at $P(\text{red}) = 0.3$:

    $$
    V(f_3) = \min_{p \in [0.3, 0.7]} p \times 100 = 0.3 \times 100 = 30
    $$

    **Gamble $f_4$** (black from Urn II): The worst-case prior minimizes $P(\text{black}) \times 100 = (1 - P(\text{red})) \times 100$, which is minimized when $P(\text{red})$ is maximized at $0.7$:

    $$
    V(f_4) = \min_{p \in [0.3, 0.7]} (1 - p) \times 100 = 0.3 \times 100 = 30
    $$

    **Resulting preference ordering:**

    $$
    V(f_1) = V(f_2) = 50 > 30 = V(f_3) = V(f_4)
    $$

    Therefore $f_1 \sim f_2 \succ f_3 \sim f_4$, which is exactly the Ellsberg-type behavior. The known-probability gambles are preferred because the worst-case evaluation penalizes the ambiguous gambles: the MEU agent evaluates Urn II gambles using the most pessimistic prior, which assigns only 30% probability to the winning color. $\blacksquare$

---

**Exercise 2.** Let $\Omega = \{\omega_1, \omega_2, \omega_3\}$ and consider the $\varepsilon$-contamination model with reference measure $P_0 = (0.5, 0.3, 0.2)$ and $\varepsilon = 0.2$. For an act $f$ with $u(f(\omega_1)) = 10$, $u(f(\omega_2)) = 4$, $u(f(\omega_3)) = -2$, compute the MEU value

$$
V(f) = (1-\varepsilon)\,\mathbb{E}_{P_0}[u(f)] + \varepsilon \inf_{\omega \in \Omega} u(f(\omega))
$$

Compare this with the standard expected utility $\mathbb{E}_{P_0}[u(f)]$.

??? success "Solution to Exercise 2"
    **Standard expected utility under $P_0 = (0.5, 0.3, 0.2)$:**

    $$
    \mathbb{E}_{P_0}[u(f)] = 0.5 \times 10 + 0.3 \times 4 + 0.2 \times (-2) = 5 + 1.2 - 0.4 = 5.8
    $$

    **MEU with $\varepsilon$-contamination ($\varepsilon = 0.2$):**

    $$
    V(f) = (1 - \varepsilon)\,\mathbb{E}_{P_0}[u(f)] + \varepsilon\,\inf_{\omega \in \Omega} u(f(\omega))
    $$

    The infimum of utility outcomes is $\inf\{10, 4, -2\} = -2$. Therefore:

    $$
    V(f) = 0.8 \times 5.8 + 0.2 \times (-2) = 4.64 - 0.4 = 4.24
    $$

    **Comparison:** The standard expected utility is $5.8$, while the MEU value is $4.24$, a reduction of $5.8 - 4.24 = 1.56$.

    The $\varepsilon$-contamination model reduces the value by placing weight $\varepsilon = 0.2$ on the worst possible outcome $u = -2$ rather than distributing that weight according to $P_0$. This captures the decision-maker's concern that the reference model $P_0$ might be wrong, with a 20% "contamination" from an adversarial distribution that concentrates all mass on the worst state $\omega_3$. $\blacksquare$

---

**Exercise 3.** In the MEU portfolio problem with ellipsoidal uncertainty set $\mathcal{U}_\mu = \{\mu : (\mu - \hat{\mu})^\top \Sigma^{-1}(\mu - \hat{\mu}) \leq \kappa^2\}$, show that the worst-case mean for portfolio $w$ is

$$
\mu^*(w) = \hat{\mu} - \kappa \frac{\Sigma w}{\sqrt{w^\top \Sigma w}}
$$

by solving the inner minimization problem using Lagrange multipliers. Then show that the robust portfolio problem reduces to

$$
\max_w \left\{ w^\top \hat{\mu} - \kappa \sqrt{w^\top \Sigma w} - \frac{\lambda}{2} w^\top \Sigma w \right\}
$$

??? success "Solution to Exercise 3"
    **Inner minimization problem:** For a fixed portfolio $w$, we solve:

    $$
    \min_{\mu \in \mathcal{U}_\mu} w^\top \mu \quad \text{where} \quad \mathcal{U}_\mu = \{\mu : (\mu - \hat{\mu})^\top \Sigma^{-1}(\mu - \hat{\mu}) \leq \kappa^2\}
    $$

    Set $\delta = \mu - \hat{\mu}$. The problem becomes:

    $$
    \min_\delta w^\top(\hat{\mu} + \delta) \quad \text{s.t.} \quad \delta^\top \Sigma^{-1}\delta \leq \kappa^2
    $$

    which is equivalent to:

    $$
    w^\top \hat{\mu} + \min_{\delta: \delta^\top \Sigma^{-1}\delta \leq \kappa^2} w^\top \delta
    $$

    **Lagrangian approach:** Form the Lagrangian:

    $$
    \mathcal{L}(\delta, \lambda) = w^\top \delta + \lambda(\delta^\top \Sigma^{-1}\delta - \kappa^2)
    $$

    First-order condition: $w + 2\lambda \Sigma^{-1}\delta = 0$, giving $\delta = -\frac{1}{2\lambda}\Sigma w$.

    Substituting into the constraint $\delta^\top \Sigma^{-1}\delta = \kappa^2$:

    $$
    \frac{1}{4\lambda^2}w^\top \Sigma \Sigma^{-1}\Sigma w = \frac{w^\top \Sigma w}{4\lambda^2} = \kappa^2
    $$

    Therefore $\lambda = \frac{\sqrt{w^\top \Sigma w}}{2\kappa}$ and:

    $$
    \delta^* = -\frac{1}{2\lambda}\Sigma w = -\kappa\frac{\Sigma w}{\sqrt{w^\top \Sigma w}}
    $$

    The worst-case mean is:

    $$
    \mu^*(w) = \hat{\mu} + \delta^* = \hat{\mu} - \kappa\frac{\Sigma w}{\sqrt{w^\top \Sigma w}}
    $$

    **Reduction of the robust portfolio problem:** Substituting $\mu^*(w)$ into the objective:

    $$
    \max_w\left\{w^\top\mu^*(w) - \frac{\lambda}{2}w^\top\Sigma w\right\}
    $$

    $$
    = \max_w\left\{w^\top\hat{\mu} - \kappa\frac{w^\top\Sigma w}{\sqrt{w^\top\Sigma w}} - \frac{\lambda}{2}w^\top\Sigma w\right\}
    $$

    $$
    = \max_w\left\{w^\top\hat{\mu} - \kappa\sqrt{w^\top\Sigma w} - \frac{\lambda}{2}w^\top\Sigma w\right\}
    $$

    This is the desired result. The robust portfolio problem adds a penalty proportional to the portfolio's standard deviation (scaled by $\kappa$) on top of the usual variance penalty. This additional term is non-differentiable at $w = 0$, which can cause the robust optimizer to choose $w^* = 0$ (no investment) when the ambiguity is large relative to expected returns. $\blacksquare$

---

**Exercise 4.** Prove that the uncertainty aversion axiom (Axiom 5) is satisfied by MEU preferences. That is, if $\mathcal{P}$ is a closed convex set of priors and $V(f) = \min_{P \in \mathcal{P}} \mathbb{E}_P[u(f)]$, show that $V(f) = V(g)$ implies $V(\alpha f + (1-\alpha)g) \geq V(f)$ for all $\alpha \in (0,1)$.

??? success "Solution to Exercise 4"
    **To prove:** If $V(f) = V(g)$, then $V(\alpha f + (1-\alpha)g) \geq V(f)$ for all $\alpha \in (0,1)$.

    Let $V(f) = V(g) = v$. For any $P \in \mathcal{P}$:

    $$
    \mathbb{E}_P[u(\alpha f + (1-\alpha)g)]
    $$

    Since $u$ is affine (as given in the Gilboa-Schmeidler setup, where acts map to a convex outcome space and $u$ is affine):

    $$
    \mathbb{E}_P[u(\alpha f + (1-\alpha)g)] = \alpha\,\mathbb{E}_P[u(f)] + (1-\alpha)\,\mathbb{E}_P[u(g)]
    $$

    Taking the minimum over $P \in \mathcal{P}$:

    $$
    V(\alpha f + (1-\alpha)g) = \min_{P \in \mathcal{P}}\left\{\alpha\,\mathbb{E}_P[u(f)] + (1-\alpha)\,\mathbb{E}_P[u(g)]\right\}
    $$

    Now we use the key inequality: for any function $\phi(P) = \alpha a(P) + (1-\alpha)b(P)$:

    $$
    \min_P \phi(P) \geq \alpha \min_P a(P) + (1-\alpha)\min_P b(P)
    $$

    This holds because the minimum of a sum is at least the sum of the minima (the worst case for the combined objective cannot be worse than the sum of the individual worst cases taken separately). Formally: for any $P$, $\alpha a(P) + (1-\alpha)b(P) \geq \alpha \min_{P'} a(P') + (1-\alpha)\min_{P''} b(P'')$, so taking $\min_P$ of the left side preserves the inequality.

    Applying this:

    $$
    V(\alpha f + (1-\alpha)g) \geq \alpha\min_{P \in \mathcal{P}}\mathbb{E}_P[u(f)] + (1-\alpha)\min_{P \in \mathcal{P}}\mathbb{E}_P[u(g)]
    $$

    $$
    = \alpha V(f) + (1-\alpha)V(g) = \alpha v + (1-\alpha)v = v = V(f)
    $$

    Therefore $V(\alpha f + (1-\alpha)g) \geq V(f)$. Hedging (mixing) between two equally valued acts is weakly preferred, because the minimum of a convex combination is at least the convex combination of the individual minima --- the worst-case prior for the mixture may differ from the individual worst-case priors, and the mixture forces a compromise that cannot be worse. $\blacksquare$

---

**Exercise 5.** Consider a two-period model where an MEU agent has prior set $\mathcal{P} = \{P_1, P_2\}$ over three states. At $t=0$, event $A = \{\omega_1\}$ or $A^c = \{\omega_2, \omega_3\}$ is observed. Define

$$
P_1 = (0.4, 0.4, 0.2), \quad P_2 = (0.3, 0.2, 0.5)
$$

(a) Compute the unconditional worst-case measure for the act $f$ with $u(f(\omega_1)) = 5$, $u(f(\omega_2)) = 2$, $u(f(\omega_3)) = 8$.
(b) Compute the conditional worst-case measures given $A$ and $A^c$ separately. Does the agent who re-optimizes at $t=1$ follow the same plan chosen at $t=0$? Discuss time consistency.

??? success "Solution to Exercise 5"
    **Part (a): Unconditional worst-case measure.**

    We have $P_1 = (0.4, 0.4, 0.2)$, $P_2 = (0.3, 0.2, 0.5)$, and $u(f) = (5, 2, 8)$.

    Compute expected utilities:

    $$
    \mathbb{E}_{P_1}[u(f)] = 0.4 \times 5 + 0.4 \times 2 + 0.2 \times 8 = 2.0 + 0.8 + 1.6 = 4.4
    $$

    $$
    \mathbb{E}_{P_2}[u(f)] = 0.3 \times 5 + 0.2 \times 2 + 0.5 \times 8 = 1.5 + 0.4 + 4.0 = 5.9
    $$

    The unconditional worst-case measure is $P_1$ (giving the minimum expected utility):

    $$
    V(f) = \min\{4.4, 5.9\} = 4.4, \quad \text{achieved by } P_1
    $$

    **Part (b): Conditional worst-case measures.**

    **Given $A = \{\omega_1\}$:** On $A$, $u(f(\omega_1)) = 5$. Both $P_1(\omega_1) = 0.4 > 0$ and $P_2(\omega_1) = 0.3 > 0$, so both priors assign positive probability to $A$. Conditional on $A$, the utility is simply $u(f(\omega_1)) = 5$ regardless of which prior is used (since $A$ is a singleton). So both priors give the same conditional expected utility of 5.

    **Given $A^c = \{\omega_2, \omega_3\}$:** Compute conditional probabilities:

    Under $P_1$: $P_1(A^c) = 0.6$, so $P_1(\omega_2 | A^c) = 0.4/0.6 = 2/3$, $P_1(\omega_3 | A^c) = 0.2/0.6 = 1/3$.

    $$
    \mathbb{E}_{P_1}[u(f) | A^c] = \frac{2}{3}\times 2 + \frac{1}{3}\times 8 = \frac{4}{3} + \frac{8}{3} = 4
    $$

    Under $P_2$: $P_2(A^c) = 0.7$, so $P_2(\omega_2 | A^c) = 0.2/0.7 = 2/7$, $P_2(\omega_3 | A^c) = 0.5/0.7 = 5/7$.

    $$
    \mathbb{E}_{P_2}[u(f) | A^c] = \frac{2}{7}\times 2 + \frac{5}{7}\times 8 = \frac{4}{7} + \frac{40}{7} = \frac{44}{7} \approx 6.286
    $$

    The conditional worst-case on $A^c$ is $P_1$ (giving the minimum of $4$).

    **Time consistency analysis:** At $t=0$, the unconditional worst-case measure is $P_1$, which gives $V(f) = 4.4$. The agent plans based on this evaluation.

    At $t=1$, after observing $A^c$, the agent re-optimizes and selects the conditional worst-case measure on $A^c$, which is also $P_1$. In this case the worst-case measure happens to be consistent.

    However, consider a different act $g$ with $u(g) = (1, 8, 3)$:

    - $\mathbb{E}_{P_1}[u(g)] = 0.4(1) + 0.4(8) + 0.2(3) = 4.2$
    - $\mathbb{E}_{P_2}[u(g)] = 0.3(1) + 0.2(8) + 0.5(3) = 3.4$

    Unconditionally, $P_2$ is worst-case. But conditional on $A^c$: $\mathbb{E}_{P_1}[u(g)|A^c] = \frac{2}{3}(8) + \frac{1}{3}(3) = 19/3 \approx 6.33$ and $\mathbb{E}_{P_2}[u(g)|A^c] = \frac{2}{7}(8) + \frac{5}{7}(3) = 31/7 \approx 4.43$. The conditional worst case is still $P_2$.

    Time inconsistency arises in general because the prior $\mathcal{P} = \{P_1, P_2\}$ is **not rectangular**: the worst-case prior can switch between $P_1$ and $P_2$ depending on the event observed and the act evaluated. A dynamically consistent MEU agent requires a rectangular prior set, where conditional priors can be freely mixed across events. With only two priors, rectangularity demands a specific product structure that is not guaranteed. $\blacksquare$

---

**Exercise 6.** Let $\nu$ be the capacity defined on $\Omega = \{\omega_1, \omega_2, \omega_3\}$ by $\nu(\{\omega_i\}) = 0.2$ for each singleton and $\nu(\{\omega_i, \omega_j\}) = 0.6$ for each pair. Verify that $\nu$ is convex (i.e., $\nu(A \cup B) + \nu(A \cap B) \geq \nu(A) + \nu(B)$ for all $A, B$). Then compute the core of $\nu$ and show that the Choquet integral of the act $u(f) = (3, 1, 5)$ with respect to $\nu$ equals the minimum expected utility over the core.

??? success "Solution to Exercise 6"
    **Verify convexity of $\nu$.**

    A capacity $\nu$ is convex if $\nu(A \cup B) + \nu(A \cap B) \geq \nu(A) + \nu(B)$ for all $A, B \subseteq \Omega$.

    We have $\Omega = \{\omega_1, \omega_2, \omega_3\}$, $\nu(\emptyset) = 0$, $\nu(\{\omega_i\}) = 0.2$ for each $i$, $\nu(\{\omega_i, \omega_j\}) = 0.6$ for each pair, $\nu(\Omega) = 1$.

    Check all non-trivial pairs:

    **Case 1: $A$ and $B$ are singletons, $A \neq B$.** Say $A = \{\omega_1\}$, $B = \{\omega_2\}$:

    $$
    \nu(A \cup B) + \nu(A \cap B) = \nu(\{\omega_1, \omega_2\}) + \nu(\emptyset) = 0.6 + 0 = 0.6
    $$

    $$
    \nu(A) + \nu(B) = 0.2 + 0.2 = 0.4
    $$

    $0.6 \geq 0.4$. ✓

    **Case 2: $A$ is a singleton, $B$ is a pair.** Say $A = \{\omega_1\}$, $B = \{\omega_1, \omega_2\}$:

    $$
    \nu(A \cup B) + \nu(A \cap B) = \nu(\{\omega_1, \omega_2\}) + \nu(\{\omega_1\}) = 0.6 + 0.2 = 0.8
    $$

    $$
    \nu(A) + \nu(B) = 0.2 + 0.6 = 0.8
    $$

    $0.8 \geq 0.8$. ✓

    **Case 3: $A = \{\omega_1\}$, $B = \{\omega_2, \omega_3\}$ (disjoint):**

    $$
    \nu(A \cup B) + \nu(A \cap B) = \nu(\Omega) + \nu(\emptyset) = 1 + 0 = 1
    $$

    $$
    \nu(A) + \nu(B) = 0.2 + 0.6 = 0.8
    $$

    $1 \geq 0.8$. ✓

    **Case 4: Both are pairs.** Say $A = \{\omega_1, \omega_2\}$, $B = \{\omega_1, \omega_3\}$:

    $$
    \nu(A \cup B) + \nu(A \cap B) = \nu(\Omega) + \nu(\{\omega_1\}) = 1 + 0.2 = 1.2
    $$

    $$
    \nu(A) + \nu(B) = 0.6 + 0.6 = 1.2
    $$

    $1.2 \geq 1.2$. ✓

    All cases satisfy the convexity inequality. $\nu$ is convex. ✓

    **Compute the core of $\nu$.**

    The core is $\text{core}(\nu) = \{P = (p_1, p_2, p_3) : p_i \geq 0, \sum p_i = 1, P(A) \geq \nu(A) \text{ for all } A\}$.

    The constraints are:

    - $p_i \geq \nu(\{\omega_i\}) = 0.2$ for $i = 1, 2, 3$
    - $p_i + p_j \geq \nu(\{\omega_i, \omega_j\}) = 0.6$ for all pairs
    - $p_1 + p_2 + p_3 = 1$

    From $p_i \geq 0.2$ and $\sum p_i = 1$: each $p_i \leq 1 - 2(0.2) = 0.6$. The pair constraint $p_i + p_j \geq 0.6$ is equivalent to $1 - p_k \geq 0.6$, i.e., $p_k \leq 0.4$.

    So the core is:

    $$
    \text{core}(\nu) = \{(p_1, p_2, p_3) : p_i \geq 0.2, \; p_i \leq 0.4, \; p_1 + p_2 + p_3 = 1\}
    $$

    **Choquet integral of $u(f) = (3, 1, 5)$.**

    Order the values: $u(f(\omega_2)) = 1 \leq u(f(\omega_1)) = 3 \leq u(f(\omega_3)) = 5$. In the Choquet integral with a convex capacity, we use the permutation $\pi$ such that $u(f(\omega_{\pi(1)})) \leq u(f(\omega_{\pi(2)})) \leq u(f(\omega_{\pi(3)}))$, i.e., $\pi = (2, 1, 3)$.

    $$
    \int u(f)\,d\nu = u_{\pi(1)} + (u_{\pi(2)} - u_{\pi(1)})\nu(\{\omega_{\pi(2)}, \omega_{\pi(3)}\}) + (u_{\pi(3)} - u_{\pi(2)})\nu(\{\omega_{\pi(3)}\})
    $$

    $$
    = 1 + (3 - 1)\nu(\{\omega_1, \omega_3\}) + (5 - 3)\nu(\{\omega_3\})
    $$

    $$
    = 1 + 2 \times 0.6 + 2 \times 0.2 = 1 + 1.2 + 0.4 = 2.6
    $$

    **Minimum expected utility over the core.** We need:

    $$
    \min_{P \in \text{core}(\nu)} \mathbb{E}_P[u(f)] = \min_{(p_1, p_2, p_3)} 3p_1 + 1p_2 + 5p_3
    $$

    subject to $0.2 \leq p_i \leq 0.4$ and $\sum p_i = 1$.

    To minimize $3p_1 + p_2 + 5p_3$, we want to maximize $p_2$ (coefficient 1, the smallest) and minimize $p_3$ (coefficient 5, the largest). Set $p_2 = 0.4$, $p_3 = 0.2$, then $p_1 = 1 - 0.4 - 0.2 = 0.4$. Check: $0.2 \leq 0.4 \leq 0.4$ ✓.

    $$
    \min_{P \in \text{core}(\nu)} \mathbb{E}_P[u(f)] = 3(0.4) + 1(0.4) + 5(0.2) = 1.2 + 0.4 + 1.0 = 2.6
    $$

    This equals the Choquet integral value of 2.6, confirming that for a convex capacity, the Choquet integral equals the minimum expected utility over the core. $\blacksquare$

---

**Exercise 7.** Consider the robust option pricing problem with volatility uncertainty $\sigma \in [\underline{\sigma}, \overline{\sigma}] = [0.15, 0.30]$. For a European call option with strike $K = 100$, maturity $T = 1$, risk-free rate $r = 0.05$, and current stock price $S_0 = 100$, compute the Black-Scholes prices at both extreme volatilities. The buyer's price is the maximum and the seller's price is the minimum. Calculate the bid-ask spread and explain how this spread relates to ambiguity about the volatility parameter.

??? success "Solution to Exercise 7"
    **Black-Scholes formula:** For a European call with spot $S_0$, strike $K$, maturity $T$, risk-free rate $r$, and volatility $\sigma$:

    $$
    C = S_0 \Phi(d_1) - K e^{-rT}\Phi(d_2)
    $$

    where $d_1 = \frac{\log(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$ and $d_2 = d_1 - \sigma\sqrt{T}$.

    With $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$:

    **Price at $\underline{\sigma} = 0.15$:**

    $$
    d_1 = \frac{\log(1) + (0.05 + 0.0225/2)(1)}{0.15} = \frac{0 + 0.06125}{0.15} = 0.4083
    $$

    $$
    d_2 = 0.4083 - 0.15 = 0.2583
    $$

    $$
    C(\underline{\sigma}) = 100\,\Phi(0.4083) - 100\,e^{-0.05}\Phi(0.2583)
    $$

    Using standard normal tables: $\Phi(0.4083) \approx 0.6585$, $\Phi(0.2583) \approx 0.6019$, $e^{-0.05} \approx 0.9512$.

    $$
    C(0.15) \approx 100(0.6585) - 100(0.9512)(0.6019) = 65.85 - 57.25 = 8.60
    $$

    **Price at $\overline{\sigma} = 0.30$:**

    $$
    d_1 = \frac{0 + (0.05 + 0.09/2)(1)}{0.30} = \frac{0.095}{0.30} = 0.3167
    $$

    $$
    d_2 = 0.3167 - 0.30 = 0.0167
    $$

    $$
    C(\overline{\sigma}) = 100\,\Phi(0.3167) - 100\,e^{-0.05}\Phi(0.0167)
    $$

    $\Phi(0.3167) \approx 0.6242$, $\Phi(0.0167) \approx 0.5067$.

    $$
    C(0.30) \approx 100(0.6242) - 100(0.9512)(0.5067) = 62.42 - 48.20 = 14.22
    $$

    **Buyer's and seller's prices:**

    For a call option (which is convex in $S_T$), the price is increasing in volatility (positive vega). Therefore:

    - **Buyer's price** (maximum over $\mathcal{Q}$): $V_{\text{buy}} = C(\overline{\sigma}) \approx 14.22$
    - **Seller's price** (minimum over $\mathcal{Q}$): $V_{\text{sell}} = C(\underline{\sigma}) \approx 8.60$

    **Bid-ask spread:**

    $$
    \text{Spread} = V_{\text{buy}} - V_{\text{sell}} \approx 14.22 - 8.60 = 5.62
    $$

    **Interpretation:** The bid-ask spread of approximately \$5.62 (on an at-the-money call worth roughly \$8.60--\$14.22) directly reflects the ambiguity about the volatility parameter. The wider the uncertainty interval $[\underline{\sigma}, \overline{\sigma}]$, the larger the spread.

    The buyer, who bears the risk of overpaying, evaluates the option at the highest possible volatility (the most expensive scenario). The seller, who bears the risk of selling too cheaply, evaluates at the lowest volatility. No trade occurs at a single price because buyer and seller use different worst-case models.

    This MEU-based bid-ask spread provides a structural explanation for observed option bid-ask spreads beyond transaction costs: part of the spread compensates market makers for ambiguity about the true volatility dynamics. $\blacksquare$
