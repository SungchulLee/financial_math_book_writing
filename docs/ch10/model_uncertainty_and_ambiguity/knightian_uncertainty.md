# Knightian Uncertainty

## Introduction

Knightian uncertainty, named after economist Frank Knight (1921), represents a fundamental distinction between **risk** and **uncertainty** that has profound implications for quantitative finance and decision theory. While risk refers to situations where probability distributions are known or estimable, Knightian uncertainty captures scenarios where probabilities themselves are unknown or unknowable.

## Knight's Risk-Uncertainty Distinction

### Definitions

**Risk**: Situations where the probability distribution over outcomes is known or can be objectively estimated from data. This corresponds to the classical probabilistic framework where:

$$
\mathbb{E}[X] = \int_{\Omega} X(\omega) \, dP(\omega)
$$

for a known probability measure $P$.

**Knightian Uncertainty (Ambiguity)**: Situations where the probability distribution is not uniquely specified, leading to a family of possible probability measures. Decision makers face **model uncertainty** about which probability measure governs the true data-generating process.

### Historical Context and Motivation

Knight (1921) argued that true uncertainty—as opposed to measurable risk—is the source of entrepreneurial profit. In competitive markets, pure risk can be priced through actuarial methods, but genuine uncertainty cannot be fully hedged or insured against.

**Key Insight**: Economic agents often face situations where they have incomplete information about:
- The correct probability model
- Parameter values within a given model class
- The model structure itself (specification uncertainty)

## Mathematical Framework

### Savage's Subjective Expected Utility

Savage (1954) axiomatized decision-making under uncertainty using a unique subjective probability measure. However, this framework assumes that decision makers can always form precise probabilistic beliefs, which Knightian uncertainty challenges.

**Savage's Axioms**: Lead to a representation:

$$
U(f) = \int_{\Omega} u(f(\omega)) \, dP(\omega)
$$

where $u$ is a utility function and $P$ is a unique subjective probability measure.

**Limitation**: Savage's framework cannot accommodate situations where the decision maker is genuinely uncertain about which probability measure to use.

### Multiple Priors Representation

To capture Knightian uncertainty, we generalize from a single probability measure to a set of probability measures.

**Definition** (Set of Priors): Let $\mathcal{P}$ be a convex, closed set of probability measures on $(\Omega, \mathcal{F})$. The decision maker evaluates acts $f: \Omega \to \mathbb{R}$ using:

$$
V(f) = \min_{P \in \mathcal{P}} \mathbb{E}_P[u(f)]
$$

This is known as the **maxmin expected utility** representation (Gilboa-Schmeidler, 1989).

**Interpretation**: The decision maker:
1. Computes expected utility under each plausible probability measure in $\mathcal{P}$
2. Evaluates the act by its worst-case expected utility
3. Exhibits **ambiguity aversion** by focusing on the minimum

### Variational Preferences

An alternative representation uses a penalty function for deviating from a reference measure $P_0$.

**Variational Representation** (Maccheroni, Marinacci, Rustichini, 2006):

$$
V(f) = \min_{P \in \mathcal{P}} \left\{ \mathbb{E}_P[u(f)] + c(P \| P_0) \right\}
$$

where $c(P \| P_0)$ is a convex penalty function, often chosen as relative entropy:

$$
c(P \| P_0) = \theta \cdot D_{\text{KL}}(P \| P_0) = \theta \int_{\Omega} \log\left(\frac{dP}{dP_0}\right) \, dP
$$

with $\theta > 0$ measuring the degree of ambiguity aversion.

**Properties**:
- When $\theta \to 0$: Approaches classical expected utility with measure $P_0$
- When $\theta \to \infty$: Approaches maxmin over $\mathcal{P}$
- Intermediate $\theta$: Balances expected utility and model misspecification concerns

## Ellsberg Paradox and Ambiguity Aversion

### The Ellsberg Experiment

Ellsberg (1961) demonstrated systematic violations of Savage's axioms through the following thought experiment.

**Setup**: Two urns containing red and black balls:
- **Urn 1**: Contains 50 red and 50 black balls (known composition)
- **Urn 2**: Contains 100 balls of unknown composition (ambiguous)

**Bet Structure**:
- Bet A: Win \$100 if red is drawn from Urn 1
- Bet B: Win \$100 if black is drawn from Urn 1
- Bet C: Win \$100 if red is drawn from Urn 2
- Bet D: Win \$100 if black is drawn from Urn 2

**Typical Preferences**: Most people prefer:
- Bet A over Bet C (prefer known risk over ambiguity)
- Bet B over Bet D (prefer known risk over ambiguity)

**Paradox**: Under Savage's framework with subjective probability $p$ for red in Urn 2:
- Preferring A over C implies: $0.5 > p$
- Preferring B over D implies: $0.5 > 1-p$, which means $p > 0.5$

This contradiction demonstrates that people systematically avoid ambiguous situations, violating the independence axiom in Savage's theory.

### Mathematical Analysis

Let $P_{\text{Urn 2}}$ denote the decision maker's beliefs about Urn 2. The observed preferences suggest:

$$
\inf_{P \in \mathcal{P}_2} P(\text{Red}) < 0.5 \quad \text{and} \quad \inf_{P \in \mathcal{P}_2} P(\text{Black}) < 0.5
$$

where $\mathcal{P}_2$ is the set of priors for Urn 2.

This is consistent with maxmin preferences with:

$$
\mathcal{P}_2 = \left\{ P: P(\text{Red}) \in [a, 1-a] \text{ for some } a < 0.5 \right\}
$$

## Applications to Quantitative Finance

### Model Uncertainty in Derivative Pricing

In the Black-Scholes framework, the risk-neutral measure $\mathbb{Q}$ is uniquely determined by no-arbitrage conditions. However, in practice:

1. **Volatility Uncertainty**: True volatility $\sigma$ is unobservable
2. **Jump Risk**: The continuous-path assumption may be violated
3. **Market Incompleteness**: Not all risks can be hedged

**Robust Pricing**: Instead of a single risk-neutral measure $\mathbb{Q}$, consider:

$$
V_t = \inf_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}_{\mathbb{Q}}\left[ e^{-r(T-t)} \Phi(S_T) \, \bigg| \, \mathcal{F}_t \right]
$$

where $\mathcal{Q}$ is a set of equivalent martingale measures compatible with observed market prices.

### Volatility Uncertainty

Consider a European call option under model uncertainty about volatility.

**Setup**: Stock price follows:

$$
dS_t = \mu S_t \, dt + \sigma_t S_t \, dW_t
$$

where $\sigma_t \in [\sigma_{\min}, \sigma_{\max}]$ is uncertain.

**Robust Price**: The buyer (who is ambiguity-averse) solves:

$$
V_{\text{buy}} = \sup_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \text{BS}(S_0, K, r, \sigma, T)
$$

while the seller solves:

$$
V_{\text{sell}} = \inf_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \text{BS}(S_0, K, r, \sigma, T)
$$

This creates a **bid-ask spread** driven by Knightian uncertainty:

$$
V_{\text{sell}} < V_{\text{buy}}
$$

### Portfolio Selection under Ambiguity

The classical Markowitz framework assumes known mean $\mu$ and covariance $\Sigma$ of returns. Under ambiguity:

**Robust Portfolio Problem**:

$$
\max_{w \in \Delta^n} \min_{(\mu, \Sigma) \in \Theta} \left\{ w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w \right\}
$$

where $\Theta$ represents uncertainty about the joint distribution of returns.

**Example**: Uncertainty about the mean return vector:

$$
\Theta = \left\{ (\mu, \Sigma): \|\mu - \hat{\mu}\|_{\Sigma^{-1}} \leq \delta \right\}
$$

leads to the robust portfolio:

$$
w^* = \frac{1}{\lambda(1 + \delta)} \Sigma^{-1} \hat{\mu}
$$

The ambiguity parameter $\delta$ effectively increases risk aversion, leading to more conservative positions.

## Theoretical Properties

### Ambiguity Aversion vs Risk Aversion

**Risk Aversion**: Preference for certain outcomes over risky lotteries with the same expected value:

$$
u(\mathbb{E}[X]) > \mathbb{E}[u(X)]
$$

characterized by concavity of $u$.

**Ambiguity Aversion**: Preference for known probability distributions over ambiguous ones:

$$
\min_{P \in \mathcal{P}} \mathbb{E}_P[u(X)] < \mathbb{E}_{P_{\text{avg}}}[u(X)]
$$

where $P_{\text{avg}} = \int_{\mathcal{P}} P \, d\nu(P)$ for some averaging measure $\nu$.

**Key Distinction**: 
- Risk aversion is about the curvature of utility over outcomes
- Ambiguity aversion is about preferences over probability measures

These are **orthogonal concepts**: one can be risk-neutral but ambiguity-averse.

### Rectangularity and Dynamic Consistency

A critical issue in multiple priors models is maintaining consistency across time.

**Rectangularity** (Epstein-Schneider, 2003): A set of priors $\mathcal{P}$ is rectangular if:

$$
\mathcal{P} = \left\{ P: P(A|\mathcal{F}_t) \in [\underline{p}_t(A), \overline{p}_t(A)] \text{ for all } A \in \mathcal{F}_T, t \leq T \right\}
$$

**Dynamic Consistency**: Requires that optimal plans made at time $t=0$ remain optimal when reconsidered at intermediate times.

**Theorem** (Epstein-Schneider): For maxmin preferences with multiple priors, dynamic consistency holds if and only if the set of priors is rectangular.

### Connection to Robust Control

Knightian uncertainty has deep connections to robust control theory (Hansen-Sargent, 2001).

**Robust Control Problem**:

$$
\min_{u_t} \max_{w_t} \mathbb{E}\left[ \sum_{t=0}^T \left( x_t^\top Q x_t + u_t^\top R u_t - \theta w_t^\top w_t \right) \right]
$$

subject to:

$$
x_{t+1} = A x_t + B u_t + C w_t
$$

where:
- $u_t$ is the control (decision variable)
- $w_t$ represents model misspecification
- $\theta$ measures robustness concerns

**Interpretation**: The decision maker chooses controls assuming nature selects the worst-case model distortion $w_t$, penalized by $\theta w_t^\top w_t$.

**Risk-Sensitive Control**: Setting $\theta = -\beta$ and taking limits yields:

$$
V(x_0) = -\frac{1}{\beta} \log \mathbb{E}\left[ \exp\left(-\beta \sum_{t=0}^T r(x_t, u_t) \right) \right]
$$

which is equivalent to exponential utility preferences over random costs.

## Axiomatization and Representation Theorems

### Gilboa-Schmeidler Axioms

Gilboa and Schmeidler (1989) provided an axiomatic foundation for maxmin expected utility.

**Axioms**:
1. **Weak Order**: Preferences $\succeq$ are complete and transitive
2. **Continuity**: Standard topological continuity
3. **Monotonicity**: If $f(\omega) \geq g(\omega)$ for all $\omega$, then $f \succeq g$
4. **Uncertainty Aversion**: For any $f, g$ and $\alpha \in (0,1)$:
   $$
   f \sim g \implies \alpha f + (1-\alpha) g \succeq f
   $$
5. **State Independence**: Constant acts are ranked by their payoff

**Representation Theorem**: Preferences $\succeq$ satisfy axioms 1-5 if and only if there exists a unique set of priors $\mathcal{P}$ and a unique (up to positive affine transformation) utility function $u$ such that:

$$
f \succeq g \iff \min_{P \in \mathcal{P}} \mathbb{E}_P[u(f)] \geq \min_{P \in \mathcal{P}} \mathbb{E}_P[u(g)]
$$

**Key Axiom**: Uncertainty aversion (axiom 4) is the critical axiom distinguishing this from Savage's framework. It states that averaging over ambiguous acts is (weakly) preferred to the acts themselves.

### Maccheroni-Marinacci-Rustichini Variational Preferences

MMR (2006) generalized this to variational preferences.

**Axiom** (Certainty Independence): For any constant acts $x, y$ and any act $f$, and $\alpha \in (0,1)$:

$$
\alpha x + (1-\alpha) f \succeq \alpha y + (1-\alpha) f \iff x \succeq y
$$

**Representation Theorem**: Preferences satisfy the MMR axioms if and only if:

$$
V(f) = \min_{P \in \mathcal{M}(\Omega)} \left\{ \mathbb{E}_P[u(f)] + c(P) \right\}
$$

where $c: \mathcal{M}(\Omega) \to [0, \infty]$ is a convex, grounded ($\inf_P c(P) = 0$) function.

**Special Cases**:
- $c(P) = 0$ if $P = P_0$, else $c(P) = \infty$: Savage's expected utility
- $c(P) = 0$ if $P \in \mathcal{P}$, else $c(P) = \infty$: Gilboa-Schmeidler maxmin
- $c(P) = \theta D_{\text{KL}}(P \| P_0)$: Multiplier preferences (robust control)

## Calibration and Empirical Evidence

### Measuring Ambiguity Aversion

Several experimental and market-based approaches measure the degree of ambiguity aversion.

**Experimental Design**: Compare choices between:
- Known probability bets (risk)
- Unknown probability bets (ambiguity)

**Ambiguity Premium**: The difference in certainty equivalents:

$$
\pi = CE(\text{known}) - CE(\text{unknown})
$$

**Empirical Findings**:
- Most subjects exhibit $\pi > 0$ (ambiguity aversion)
- Magnitude varies across individuals and contexts
- Professional traders often show less ambiguity aversion

### Market Implications

**Equity Premium Puzzle**: Hansen-Sargent (2001) show that model uncertainty can help explain the historically high equity premium:

$$
\mathbb{E}[R_{\text{equity}}] - R_f = \gamma \sigma^2 + \text{ambiguity premium}
$$

**Options Market**: The implied volatility smile may partially reflect ambiguity aversion about the true volatility process.

**Bid-Ask Spreads**: Wider spreads for less liquid assets may incorporate compensation for model uncertainty.

## Connections to Information Theory

### Relative Entropy and Model Distance

The relative entropy (Kullback-Leibler divergence) provides a natural measure of model distance:

$$
D_{\text{KL}}(P \| Q) = \mathbb{E}_P\left[ \log \frac{dP}{dQ} \right] = \int_{\Omega} \log\left(\frac{dP}{dQ}\right) \, dP
$$

**Properties**:
1. Non-negativity: $D_{\text{KL}}(P \| Q) \geq 0$ with equality iff $P = Q$
2. Not symmetric: $D_{\text{KL}}(P \| Q) \neq D_{\text{KL}}(Q \| P)$ in general
3. Convexity: $D_{\text{KL}}(\cdot \| Q)$ is convex

**Interpretation in Finance**: $D_{\text{KL}}(P \| Q)$ measures the "surprise" or information gained when the true model is $P$ but we believed $Q$.

### Entropic Risk Measures

The entropic risk measure combines ambiguity and risk:

$$
\rho_{\beta}(X) = \frac{1}{\beta} \log \mathbb{E}\left[ e^{\beta X} \right]
$$

**Dual Representation**:

$$
\rho_{\beta}(X) = \sup_{\mathbb{Q} \ll \mathbb{P}} \left\{ \mathbb{E}_{\mathbb{Q}}[X] - \frac{1}{\beta} D_{\text{KL}}(\mathbb{Q} \| \mathbb{P}) \right\}
$$

This shows entropic risk as a variational preference with KL penalty.

**Properties**:
- Coherent for $\beta > 0$
- As $\beta \to 0$: Approaches $\mathbb{E}[X]$ (risk-neutral)
- As $\beta \to \infty$: Approaches $\text{ess sup}(X)$ (worst-case)

## Advanced Topics

### Second-Order Stochastic Dominance and Ambiguity

**Definition** (Second-Order Stochastic Dominance): Distribution $F$ second-order stochastically dominates $G$ (written $F \succeq_{\text{SSD}} G$) if:

$$
\int_{-\infty}^x F(t) \, dt \leq \int_{-\infty}^x G(t) \, dt \quad \text{for all } x \in \mathbb{R}
$$

**Theorem**: All risk-averse expected utility maximizers prefer $F$ to $G$ if and only if $F \succeq_{\text{SSD}} G$.

**Extension to Ambiguity**: For multiple priors preferences:

$$
f \succeq_{\text{SSD}} g \implies \min_{P \in \mathcal{P}} \mathbb{E}_P[u(f)] \geq \min_{P \in \mathcal{P}} \mathbb{E}_P[u(g)]
$$

for all concave $u$ and convex $\mathcal{P}$.

### Smooth Ambiguity Model

Klibanoff, Marinacci, Mukerji (2005) introduced **smooth ambiguity preferences**:

$$
V(f) = \int_{\mathcal{P}} \phi\left( \int_{\Omega} u(f(\omega)) \, dP(\omega) \right) d\mu(P)
$$

where:
- $u$ measures risk aversion
- $\phi$ measures ambiguity aversion
- $\mu$ is a second-order prior over $\mathcal{P}$

**Interpretation**: 
1. Compute expected utility $\mathbb{E}_P[u(f)]$ under each $P$
2. Apply ambiguity aversion function $\phi$
3. Take expectation over second-order beliefs $\mu$

**Advantage**: Separates ambiguity aversion from likelihood judgments, allowing for smoother preferences than maxmin.

### Choquet Expected Utility

Another generalization uses non-additive measures (capacities).

**Capacity**: A function $\nu: \mathcal{F} \to [0,1]$ satisfying:
1. $\nu(\emptyset) = 0$, $\nu(\Omega) = 1$
2. $A \subseteq B \implies \nu(A) \leq \nu(B)$

**Choquet Integral**:

$$
\int_{\Omega} f \, d\nu = \int_0^{\infty} \nu(\{\omega: f(\omega) \geq t\}) \, dt
$$

**Choquet Expected Utility**:

$$
V(f) = \int_{\Omega} u(f(\omega)) \, d\nu(\omega)
$$

**Connection to Ambiguity**: A capacity is **convex** if:

$$
\nu(A \cup B) + \nu(A \cap B) \geq \nu(A) + \nu(B)
$$

which implies ambiguity aversion through the **core** of the capacity:

$$
\text{core}(\nu) = \left\{ P: P(A) \geq \nu(A) \text{ for all } A \in \mathcal{F} \right\}
$$

and:

$$
\int_{\Omega} f \, d\nu = \min_{P \in \text{core}(\nu)} \mathbb{E}_P[f]
$$

## Summary and Key Takeaways

1. **Conceptual Distinction**: Knightian uncertainty separates measurable risk (known probabilities) from genuine uncertainty (unknown probabilities)

2. **Mathematical Frameworks**: Multiple representation theorems capture ambiguity aversion:
   - Gilboa-Schmeidler maxmin expected utility
   - MMR variational preferences
   - Smooth ambiguity preferences
   - Choquet expected utility

3. **Financial Applications**: Model uncertainty affects:
   - Derivative pricing (bid-ask spreads)
   - Portfolio selection (conservative positions)
   - Risk management (stress testing)
   - Asset pricing puzzles (equity premium)

4. **Dynamic Consistency**: Rectangularity is necessary and sufficient for time-consistent preferences with multiple priors

5. **Robust Control Connection**: Knightian uncertainty provides decision-theoretic foundations for robust control in continuous-time finance

6. **Measurement**: Ambiguity aversion can be quantified through experimental elicitation and calibrated to market data

The study of Knightian uncertainty enriches our understanding of decision-making under incomplete information and provides robust approaches to financial modeling when model specification is uncertain.
