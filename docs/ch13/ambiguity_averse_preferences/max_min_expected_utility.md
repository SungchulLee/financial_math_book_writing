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

### 3. $\varepsilon$-Contamination


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
