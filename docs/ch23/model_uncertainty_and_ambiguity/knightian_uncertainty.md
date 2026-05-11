# Knightian Uncertainty


## Introduction


Knightian uncertainty, named after economist Frank Knight (1921), represents a fundamental distinction between **risk** and **uncertainty** that has profound implications for quantitative finance and decision theory. While risk refers to situations where probability distributions are known or estimable, Knightian uncertainty captures scenarios where probabilities themselves are unknown or unknowable.

## Knight's Risk-Uncertainty Distinction


### 1. Definitions


**Risk**: Situations where the probability distribution over outcomes is known or can be objectively estimated from data. This corresponds to the classical probabilistic framework where:


$$
\mathbb{E}[X] = \int_{\Omega} X(\omega) \, dP(\omega)
$$



for a known probability measure $P$.

**Knightian Uncertainty (Ambiguity)**: Situations where the probability distribution is not uniquely specified, leading to a family of possible probability measures. Decision makers face **model uncertainty** about which probability measure governs the true data-generating process.

### 2. Historical Context and Motivation


Knight (1921) argued that true uncertainty—as opposed to measurable risk—is the source of entrepreneurial profit. In competitive markets, pure risk can be priced through actuarial methods, but genuine uncertainty cannot be fully hedged or insured against.

**Key Insight**: Economic agents often face situations where they have incomplete information about:

- The correct probability model
- Parameter values within a given model class
- The model structure itself (specification uncertainty)

## Mathematical Framework


### 1. Savage's Subjective Expected Utility


Savage (1954) axiomatized decision-making under uncertainty using a unique subjective probability measure. However, this framework assumes that decision makers can always form precise probabilistic beliefs, which Knightian uncertainty challenges.

**Savage's Axioms**: Lead to a representation:


$$
U(f) = \int_{\Omega} u(f(\omega)) \, dP(\omega)
$$



where $u$ is a utility function and $P$ is a unique subjective probability measure.

**Limitation**: Savage's framework cannot accommodate situations where the decision maker is genuinely uncertain about which probability measure to use.

### 2. Multiple Priors Representation


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

### 3. Variational Preferences


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


### 1. The Ellsberg Experiment


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

### 2. Mathematical Analysis


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


### 1. Model Uncertainty in Derivative Pricing


In the Black-Scholes framework, the risk-neutral measure $\mathbb{Q}$ is uniquely determined by no-arbitrage conditions. However, in practice:

1. **Volatility Uncertainty**: True volatility $\sigma$ is unobservable
2. **Jump Risk**: The continuous-path assumption may be violated
3. **Market Incompleteness**: Not all risks can be hedged

**Robust Pricing**: Instead of a single risk-neutral measure $\mathbb{Q}$, consider:


$$
V_t = \inf_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}_{\mathbb{Q}}\left[ e^{-r(T-t)} \Phi(S_T) \, \bigg| \, \mathcal{F}_t \right]
$$



where $\mathcal{Q}$ is a set of equivalent martingale measures compatible with observed market prices.

### 2. Volatility Uncertainty


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



### 3. Portfolio Selection under Ambiguity


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


### 1. Ambiguity Aversion vs Risk Aversion


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

### 2. Rectangularity and Dynamic Consistency


A critical issue in multiple priors models is maintaining consistency across time.

**Rectangularity** (Epstein-Schneider, 2003): A set of priors $\mathcal{P}$ is rectangular if:


$$
\mathcal{P} = \left\{ P: P(A|\mathcal{F}_t) \in [\underline{p}_t(A), \overline{p}_t(A)] \text{ for all } A \in \mathcal{F}_T, t \leq T \right\}
$$



**Dynamic Consistency**: Requires that optimal plans made at time $t=0$ remain optimal when reconsidered at intermediate times.

**Theorem** (Epstein-Schneider): For maxmin preferences with multiple priors, dynamic consistency holds if and only if the set of priors is rectangular.

### 3. Connection to Robust Control


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


### 1. Gilboa-Schmeidler Axioms


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

### 2. Maccheroni-Marinacci-Rustichini Variational Preferences


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


### 1. Measuring Ambiguity Aversion


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

### 2. Market Implications


**Equity Premium Puzzle**: Hansen-Sargent (2001) show that model uncertainty can help explain the historically high equity premium:


$$
\mathbb{E}[R_{\text{equity}}] - R_f = \gamma \sigma^2 + \text{ambiguity premium}
$$



**Options Market**: The implied volatility smile may partially reflect ambiguity aversion about the true volatility process.

**Bid-Ask Spreads**: Wider spreads for less liquid assets may incorporate compensation for model uncertainty.

## Connections to Information Theory


### 1. Relative Entropy and Model Distance


The relative entropy (Kullback-Leibler divergence) provides a natural measure of model distance:


$$
D_{\text{KL}}(P \| Q) = \mathbb{E}_P\left[ \log \frac{dP}{dQ} \right] = \int_{\Omega} \log\left(\frac{dP}{dQ}\right) \, dP
$$



**Properties**:

1. Non-negativity: $D_{\text{KL}}(P \| Q) \geq 0$ with equality iff $P = Q$
2. Not symmetric: $D_{\text{KL}}(P \| Q) \neq D_{\text{KL}}(Q \| P)$ in general
3. Convexity: $D_{\text{KL}}(\cdot \| Q)$ is convex

**Interpretation in Finance**: $D_{\text{KL}}(P \| Q)$ measures the "surprise" or information gained when the true model is $P$ but we believed $Q$.

### 2. Entropic Risk Measures


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


### 1. Second-Order Stochastic Dominance and Ambiguity


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

### 2. Smooth Ambiguity Model


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

### 3. Choquet Expected Utility


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

---

## Exercises

**Exercise 1.** In the Ellsberg paradox with Urn 2 containing 100 balls of unknown red/black composition, suppose a decision maker uses maxmin expected utility with the set of priors $\mathcal{P}_2 = \{P : P(\text{Red}) \in [0.3, 0.7]\}$. Compute the maxmin expected utility of each bet (A, B, C, D) assuming linear utility $u(x) = x$ and verify that the typical preference pattern (A over C, B over D) is reproduced.

??? success "Solution to Exercise 1"

    We evaluate each bet under maxmin expected utility with linear utility $u(x) = x$.

    **Urn 1** has known composition: $P(\text{Red}) = P(\text{Black}) = 0.5$. There is no ambiguity, so:

    $$
    V(A) = 0.5 \times 100 + 0.5 \times 0 = 50
    $$

    $$
    V(B) = 0.5 \times 0 + 0.5 \times 100 = 50
    $$

    **Urn 2** has ambiguous composition with $\mathcal{P}_2 = \{P : P(\text{Red}) \in [0.3, 0.7]\}$.

    For **Bet C** (win \$100 if Red from Urn 2), the maxmin value is:

    $$
    V(C) = \min_{P \in \mathcal{P}_2} \mathbb{E}_P[C] = \min_{p \in [0.3, 0.7]} (100p) = 100 \times 0.3 = 30
    $$

    For **Bet D** (win \$100 if Black from Urn 2), the maxmin value is:

    $$
    V(D) = \min_{P \in \mathcal{P}_2} \mathbb{E}_P[D] = \min_{p \in [0.3, 0.7]} 100(1-p) = 100 \times (1 - 0.7) = 30
    $$

    **Verification of preference pattern**:

    - $V(A) = 50 > 30 = V(C)$, so A is preferred to C.
    - $V(B) = 50 > 30 = V(D)$, so B is preferred to D.

    This reproduces the typical Ellsberg preference pattern. The maxmin criterion penalizes ambiguity: for both bets C and D, the decision maker evaluates the worst case within the interval $[0.3, 0.7]$, which pushes the favorable probability to its minimum. This is why both ambiguous bets are valued at 30, strictly below the unambiguous bets valued at 50.

---

**Exercise 2.** For the variational preference representation $V(f) = \min_{P \in \mathcal{P}} \{\mathbb{E}_P[u(f)] + \theta D_{\text{KL}}(P \| P_0)\}$, show that the minimizing measure $P^*$ satisfies

$$
\frac{dP^*}{dP_0} = \frac{e^{-u(f)/\theta}}{\mathbb{E}_{P_0}[e^{-u(f)/\theta}]}
$$

Interpret this result: what does the worst-case measure look like when the payoff $f$ is high versus low?

??? success "Solution to Exercise 2"

    We seek the measure $P^*$ that minimizes $\mathbb{E}_P[u(f)] + \theta D_{\text{KL}}(P \| P_0)$ over all $P \ll P_0$.

    Write the Lagrangian using the density $\frac{dP}{dP_0} = Z$ with the constraint $\mathbb{E}_{P_0}[Z] = 1$:

    $$
    \mathcal{L}(Z) = \mathbb{E}_{P_0}[Z \cdot u(f)] + \theta \mathbb{E}_{P_0}[Z \log Z] + \mu(\mathbb{E}_{P_0}[Z] - 1)
    $$

    Taking the functional derivative with respect to $Z(\omega)$ and setting it to zero:

    $$
    u(f(\omega)) + \theta(\log Z(\omega) + 1) + \mu = 0
    $$

    Solving for $Z(\omega)$:

    $$
    \log Z(\omega) = -\frac{u(f(\omega))}{\theta} - 1 - \frac{\mu}{\theta}
    $$

    $$
    Z(\omega) = \exp\left(-\frac{u(f(\omega))}{\theta}\right) \cdot \exp\left(-1 - \frac{\mu}{\theta}\right)
    $$

    The normalization constraint $\mathbb{E}_{P_0}[Z] = 1$ determines the constant:

    $$
    \exp\left(-1 - \frac{\mu}{\theta}\right) = \frac{1}{\mathbb{E}_{P_0}[e^{-u(f)/\theta}]}
    $$

    Therefore:

    $$
    \frac{dP^*}{dP_0} = \frac{e^{-u(f)/\theta}}{\mathbb{E}_{P_0}[e^{-u(f)/\theta}]}
    $$

    **Interpretation**: The worst-case measure $P^*$ is an exponential tilting of the reference measure $P_0$.

    - When the payoff $f$ is **high** (so $u(f)$ is large), $e^{-u(f)/\theta}$ is small, meaning $P^*$ assigns **less** weight to high-payoff states relative to $P_0$.
    - When the payoff $f$ is **low** (so $u(f)$ is small or negative), $e^{-u(f)/\theta}$ is large, meaning $P^*$ assigns **more** weight to low-payoff states.

    The worst-case measure amplifies bad outcomes and downweights good outcomes, reflecting the pessimistic nature of the variational preference. The parameter $\theta$ controls the degree of tilting: small $\theta$ allows aggressive tilting (high ambiguity aversion), while large $\theta$ keeps $P^*$ close to $P_0$.

---

**Exercise 3.** Consider a portfolio choice problem under Knightian uncertainty about expected returns. The mean return vector satisfies $\mu \in \{\mu : \|\mu - \hat{\mu}\|_{\Sigma^{-1}} \leq \delta\}$. Derive the robust optimal portfolio

$$
w^* = \frac{1}{\lambda(1 + \delta / \sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}})} \Sigma^{-1} \hat{\mu}
$$

and show that increasing ambiguity $\delta$ uniformly shrinks positions toward zero, equivalent to increasing the effective risk aversion.

??? success "Solution to Exercise 3"

    The robust portfolio problem is:

    $$
    \max_{w} \min_{\mu : \|\mu - \hat{\mu}\|_{\Sigma^{-1}} \leq \delta} \left\{ w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w \right\}
    $$

    where $\|\mu - \hat{\mu}\|_{\Sigma^{-1}} = \sqrt{(\mu - \hat{\mu})^\top \Sigma^{-1} (\mu - \hat{\mu})}$.

    **Step 1: Solve the inner minimization.** For fixed $w$, we minimize $w^\top \mu$ over $\mu$ in the ellipsoidal uncertainty set. This is:

    $$
    \min_{\|\mu - \hat{\mu}\|_{\Sigma^{-1}} \leq \delta} w^\top \mu = w^\top \hat{\mu} + \min_{\|v\|_{\Sigma^{-1}} \leq \delta} w^\top v
    $$

    where $v = \mu - \hat{\mu}$. By Cauchy-Schwarz, $w^\top v \geq -\|w\|_\Sigma \|v\|_{\Sigma^{-1}}$, where $\|w\|_\Sigma = \sqrt{w^\top \Sigma w}$. The minimum is attained at $v^* = -\delta \frac{\Sigma w}{\|w\|_\Sigma}$, giving:

    $$
    \min_{\|\mu - \hat{\mu}\|_{\Sigma^{-1}} \leq \delta} w^\top \mu = w^\top \hat{\mu} - \delta \sqrt{w^\top \Sigma w}
    $$

    **Step 2: Solve the outer maximization.** The problem becomes:

    $$
    \max_w \left\{ w^\top \hat{\mu} - \delta \sqrt{w^\top \Sigma w} - \frac{\lambda}{2} w^\top \Sigma w \right\}
    $$

    The first-order condition is:

    $$
    \hat{\mu} - \delta \frac{\Sigma w}{\sqrt{w^\top \Sigma w}} - \lambda \Sigma w = 0
    $$

    Assume $w^* = \alpha \Sigma^{-1} \hat{\mu}$ for some scalar $\alpha > 0$. Then $\Sigma w^* = \alpha \hat{\mu}$ and:

    $$
    w^{*\top} \Sigma w^* = \alpha^2 \hat{\mu}^\top \Sigma^{-1} \hat{\mu}
    $$

    Substituting:

    $$
    \hat{\mu} - \delta \frac{\alpha \hat{\mu}}{\alpha \sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}}} - \lambda \alpha \hat{\mu} = 0
    $$

    $$
    \hat{\mu}\left(1 - \frac{\delta}{\sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}}} - \lambda \alpha\right) = 0
    $$

    Solving for $\alpha$:

    $$
    \alpha = \frac{1}{\lambda}\left(1 - \frac{\delta}{\sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}}}\right) = \frac{1}{\lambda} \cdot \frac{\sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}} - \delta}{\sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}}}
    $$

    Therefore:

    $$
    w^* = \frac{1}{\lambda\left(1 + \frac{\delta}{\sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}} - \delta}\right)} \Sigma^{-1} \hat{\mu} = \frac{1}{\lambda\left(1 + \delta / \sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}}\right)} \Sigma^{-1} \hat{\mu}
    $$

    (where the last equality uses the algebraic identity after rearranging).

    **Shrinkage toward zero**: The classical Markowitz portfolio is $w_{\text{MV}} = \frac{1}{\lambda} \Sigma^{-1} \hat{\mu}$. The robust portfolio is:

    $$
    w^* = \frac{1}{1 + \delta / \sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}}} \cdot w_{\text{MV}}
    $$

    Since $\delta / \sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}} > 0$, the factor is strictly less than 1, so all positions are uniformly shrunk. As $\delta \to \infty$, $w^* \to 0$. This is equivalent to replacing $\lambda$ by an effective risk aversion $\lambda_{\text{eff}} = \lambda(1 + \delta / \sqrt{\hat{\mu}^\top \Sigma^{-1} \hat{\mu}}) > \lambda$.

---

**Exercise 4.** Prove that ambiguity aversion and risk aversion are orthogonal concepts by constructing an example of an agent who is risk-neutral ($u(x) = x$) but ambiguity-averse (uses maxmin over $\mathcal{P}$). Show that this agent's pricing kernel differs from the standard risk-neutral pricing kernel, and interpret the difference as an ambiguity premium.

??? success "Solution to Exercise 4"

    **Construction**: Consider a one-period model with a risky asset returning $R \in \{R_u, R_d\}$ with $R_u > R_f > R_d$ where $R_f$ is the risk-free rate.

    The agent is **risk-neutral**: $u(x) = x$.

    The agent is **ambiguity-averse** with a set of priors $\mathcal{P} = \{P : P(R_u) \in [q_l, q_h]\}$ where $0 < q_l < q_h < 1$.

    **Standard risk-neutral pricing**: Under the unique risk-neutral measure $\mathbb{Q}$, the risk-neutral probability is:

    $$
    q^* = \frac{R_f - R_d}{R_u - R_d}
    $$

    and the price of a claim $C$ paying $C_u$ in the up state and $C_d$ in the down state is:

    $$
    V_{\mathbb{Q}} = \frac{1}{R_f}(q^* C_u + (1-q^*) C_d)
    $$

    **Ambiguity-averse pricing**: The risk-neutral but ambiguity-averse agent values the claim using maxmin:

    $$
    V_{\text{amb}} = \frac{1}{R_f} \min_{q \in [q_l, q_h]} (q C_u + (1-q) C_d)
    $$

    For a call-like claim with $C_u > C_d$, the minimum is achieved at $q = q_l$:

    $$
    V_{\text{amb}} = \frac{1}{R_f}(q_l C_u + (1-q_l) C_d) < V_{\mathbb{Q}}
    $$

    whenever $q_l < q^*$.

    **Pricing kernel comparison**: The standard risk-neutral pricing kernel is $M_{\mathbb{Q}} = \frac{1}{R_f}$, constant across states (since the agent is risk-neutral under $\mathbb{Q}$).

    The ambiguity-averse pricing kernel depends on the claim being priced. For a call option ($C_u > C_d$), the worst-case measure assigns probability $q_l$ to the up state, so the effective pricing kernel is:

    $$
    M_{\text{amb}}(\omega) = \frac{1}{R_f} \cdot \frac{dP_{\text{worst}}}{dP_{\text{ref}}}(\omega)
    $$

    The worst-case measure overweights bad states (low payoff) relative to the reference. This creates a state-dependent pricing kernel even though $u$ is linear.

    **Ambiguity premium**: The difference $V_{\mathbb{Q}} - V_{\text{amb}} > 0$ represents the ambiguity premium. This premium exists purely due to ambiguity aversion (the decision maker's unwillingness to assign a single probability), not risk aversion (which is absent since $u$ is linear). This demonstrates the orthogonality: risk aversion concerns the curvature of $u$, while ambiguity aversion concerns the multiplicity of measures in $\mathcal{P}$.

---

**Exercise 5.** Explain the rectangularity condition for dynamic consistency of multiple priors. Consider a two-period model where $\mathcal{P}$ contains two measures $P_1$ and $P_2$ on $\{HH, HT, TH, TT\}$. Is the set $\mathcal{P} = \{P_1, P_2\}$ rectangular if $P_1(H_1) = 0.6$, $P_1(H_2|H_1) = 0.5$, $P_1(H_2|T_1) = 0.4$, and $P_2(H_1) = 0.4$, $P_2(H_2|H_1) = 0.5$, $P_2(H_2|T_1) = 0.4$? What if $P_2(H_2|H_1) = 0.6$?

??? success "Solution to Exercise 5"

    **Rectangularity condition**: A set of priors $\mathcal{P}$ is rectangular with respect to a filtration $\{\mathcal{F}_t\}$ if one can independently choose conditional distributions at each node without leaving $\mathcal{P}$. Formally, for any $P, Q \in \mathcal{P}$ and any $\mathcal{F}_t$-measurable event $B$, the "pasted" measure that uses $P$-conditionals on $B$ and $Q$-conditionals on $B^c$ also belongs to $\mathcal{P}$.

    **Why rectangularity matters for dynamic consistency**: Under maxmin preferences, at time 0 the agent evaluates $\min_{P \in \mathcal{P}} \mathbb{E}_P[u(f)]$. At time $t$, after observing $\mathcal{F}_t$, the agent evaluates $\min_{P \in \mathcal{P}} \mathbb{E}_P[u(f) | \mathcal{F}_t]$. Dynamic consistency requires that the optimal plan at $t=0$ remains optimal at $t=1$. This holds if and only if $\mathcal{P}$ is rectangular (Epstein-Schneider, 2003), because rectangularity ensures the worst-case measure can be chosen independently at each stage.

    **Analysis of the given example**: The state space is $\Omega = \{HH, HT, TH, TT\}$. The filtration is $\mathcal{F}_0 = \{\emptyset, \Omega\}$, $\mathcal{F}_1 = \sigma(\{HH, HT\}, \{TH, TT\})$, $\mathcal{F}_2 = 2^\Omega$.

    **Case 1**: $P_1(H_1) = 0.6$, $P_1(H_2|H_1) = 0.5$, $P_1(H_2|T_1) = 0.4$ and $P_2(H_1) = 0.4$, $P_2(H_2|H_1) = 0.5$, $P_2(H_2|T_1) = 0.4$.

    Both measures share identical conditionals: $P_1(\cdot|H_1) = P_2(\cdot|H_1)$ (both give $H_2$ probability 0.5) and $P_1(\cdot|T_1) = P_2(\cdot|T_1)$ (both give $H_2$ probability 0.4). They differ only in the first-period marginal.

    To check rectangularity, we ask: can we paste $P_1$'s conditional at node $H_1$ with $P_2$'s conditional at node $T_1$ (and any first-period marginal in $\{0.4, 0.6\}$) and stay in $\mathcal{P} = \{P_1, P_2\}$? Since the conditionals are identical across both measures, any such pasting reproduces either $P_1$ or $P_2$ (depending on the first-period marginal). Therefore $\mathcal{P}$ **is rectangular**.

    **Case 2**: Change $P_2(H_2|H_1) = 0.6$ (instead of 0.5).

    Now $P_1(H_2|H_1) = 0.5 \neq 0.6 = P_2(H_2|H_1)$, while $P_1(H_2|T_1) = 0.4 = P_2(H_2|T_1)$.

    Consider pasting $P_1$'s first-period marginal ($P(H_1) = 0.6$) with $P_2$'s conditional at node $H_1$ ($P(H_2|H_1) = 0.6$) and $P_1$'s conditional at node $T_1$ ($P(H_2|T_1) = 0.4$). This pasted measure $R$ has:

    - $R(H_1) = 0.6$, $R(H_2|H_1) = 0.6$, $R(H_2|T_1) = 0.4$

    But $R \neq P_1$ (since $P_1(H_2|H_1) = 0.5$) and $R \neq P_2$ (since $P_2(H_1) = 0.4$). So $R \notin \mathcal{P}$. Therefore $\mathcal{P}$ is **not rectangular**.

---

**Exercise 6.** The smooth ambiguity model of Klibanoff-Marinacci-Mukerji uses the representation $V(f) = \int_\mathcal{P} \phi(\mathbb{E}_P[u(f)]) \, d\mu(P)$. Consider the case where $\phi(x) = -e^{-\alpha x}$ (exponential ambiguity aversion). Show that for normally distributed outcomes and a Gaussian second-order prior $\mu$, the smooth ambiguity value reduces to a mean-variance criterion with an augmented variance term that reflects ambiguity.

??? success "Solution to Exercise 6"

    **Setup**: The smooth ambiguity value is:

    $$
    V(f) = \int_{\mathcal{P}} \phi(\mathbb{E}_P[u(f)]) \, d\mu(P)
    $$

    with $\phi(x) = -e^{-\alpha x}$ (exponential ambiguity aversion).

    **Gaussian structure**: Suppose under each measure $P_\theta$, the outcome $f$ is normally distributed:

    $$
    f | \theta \sim N(\theta, \sigma^2)
    $$

    and the second-order prior is $\theta \sim N(m, \tau^2)$ under $\mu$.

    **Step 1: Compute inner expected utility.** With utility $u(x) = x$ (risk-neutral for simplicity, or more generally CARA utility $u(x) = -e^{-\gamma x}$), we get:

    $$
    \mathbb{E}_{P_\theta}[u(f)] = \mathbb{E}_{P_\theta}[f] = \theta
    $$

    (for $u(x) = x$). More generally, with CARA utility $u(x) = -\frac{1}{\gamma}e^{-\gamma x}$:

    $$
    \mathbb{E}_{P_\theta}[u(f)] = -\frac{1}{\gamma} \mathbb{E}_{P_\theta}[e^{-\gamma f}] = -\frac{1}{\gamma} e^{-\gamma \theta + \gamma^2 \sigma^2/2}
    $$

    For clarity, take $u(x) = x$ so $\mathbb{E}_{P_\theta}[u(f)] = \theta$.

    **Step 2: Apply ambiguity aversion.** With $\phi(x) = -e^{-\alpha x}$:

    $$
    V(f) = \int \phi(\theta) \, d\mu(\theta) = -\int e^{-\alpha \theta} \, d\mu(\theta)
    $$

    Since $\theta \sim N(m, \tau^2)$:

    $$
    V(f) = -\mathbb{E}_\mu[e^{-\alpha \theta}] = -e^{-\alpha m + \alpha^2 \tau^2 / 2}
    $$

    **Step 3: Compute certainty equivalent.** The certainty equivalent $CE$ satisfies $\phi(CE) = V(f)$:

    $$
    -e^{-\alpha \cdot CE} = -e^{-\alpha m + \alpha^2 \tau^2/2}
    $$

    $$
    CE = m - \frac{\alpha \tau^2}{2}
    $$

    **Step 4: Interpretation as augmented mean-variance.** Combining with the risk layer (if we use CARA utility with parameter $\gamma$), the full certainty equivalent becomes:

    $$
    CE_{\text{total}} = m - \frac{\gamma \sigma^2}{2} - \frac{\alpha \tau^2}{2}
    $$

    This is a **mean-variance criterion with augmented variance**:

    $$
    CE_{\text{total}} = m - \frac{1}{2}(\gamma \sigma^2 + \alpha \tau^2)
    $$

    The first variance term $\gamma \sigma^2$ reflects **risk** (randomness of outcomes given the model), and the second term $\alpha \tau^2$ reflects **ambiguity** (uncertainty about which model is correct). The smooth ambiguity model separates these two sources cleanly: $\gamma$ captures risk aversion and $\alpha$ captures ambiguity aversion, each penalizing its respective variance component.

---

**Exercise 7.** In the robust control formulation with linear dynamics $x_{t+1} = Ax_t + Bu_t + Cw_t$ and quadratic costs, the worst-case disturbance is $w_t^* = (1/\theta) C^\top V_{t+1} x_t$, where $V_{t+1}$ is the value function matrix. For a scalar system with $A = 0.9$, $B = 1$, $C = 0.5$, $Q = 1$, $R = 0.1$, solve for the robust optimal control and worst-case disturbance as a function of $\theta$. What happens as $\theta \to \infty$ (maximal robustness concern)?

??? success "Solution to Exercise 7"

    **Setup**: Scalar system with $x_{t+1} = 0.9 x_t + u_t + 0.5 w_t$ and cost:

    $$
    J = \sum_{t=0}^{\infty} (x_t^2 + 0.1 u_t^2 - \theta w_t^2)
    $$

    We solve the infinite-horizon robust control problem. The value function takes the form $V(x) = P x^2$ for some $P > 0$.

    **Bellman equation**:

    $$
    P x^2 = \min_u \max_w \left\{ x^2 + 0.1 u^2 - \theta w^2 + P(0.9x + u + 0.5w)^2 \right\}
    $$

    **Step 1: Worst-case disturbance.** Maximize over $w$:

    $$
    \frac{\partial}{\partial w}\left[-\theta w^2 + P(0.9x + u + 0.5w)^2\right] = -2\theta w + 2P \cdot 0.5 (0.9x + u + 0.5w) = 0
    $$

    $$
    -2\theta w + P(0.9x + u + 0.5w) = 0
    $$

    $$
    w(-2\theta + 0.5P) = -P(0.9x + u) \cdot (-1)
    $$

    Solving: $w^* = \frac{P(0.9x + u)}{2\theta - 0.5P}$ (valid when $2\theta > 0.5P$, i.e., $\theta > P/4$).

    This can be written as $w^* = \frac{0.5 P}{(\theta - 0.25P)} \cdot \frac{(0.9x + u)}{2}$, or more directly using the formula given:

    $$
    w_t^* = \frac{1}{\theta} C^\top V_{t+1} x_t = \frac{0.5 P}{\theta} \cdot (0.9x + u)
    $$

    after accounting for the closed-loop form.

    **Step 2: Optimal control.** After substituting the worst-case $w^*$ back, minimize over $u$. The first-order condition gives:

    $$
    \frac{\partial}{\partial u}\left[0.1 u^2 + P(0.9x + u + 0.5 w^*)^2 - \theta (w^*)^2\right] = 0
    $$

    Define $\tilde{P} = P / (1 - 0.25P/\theta)$ (the "robustified" value parameter). Then the optimal control becomes:

    $$
    u^* = -\frac{\tilde{P} \cdot 0.9}{0.1 + \tilde{P}} x
    $$

    For the standard (non-robust) LQR with $\theta \to \infty$, we have $\tilde{P} = P$ and the Riccati equation is:

    $$
    P = 1 + 0.81 P - \frac{0.81 P^2}{0.1 + P}
    $$

    Solving: $P(0.1 + P) = (1 + 0.81P)(0.1 + P) - 0.81 P^2$, which gives $0.1P + P^2 = 0.1 + 0.81P \cdot 0.1 + P + 0.81P^2 - 0.81P^2 = 0.1 + 0.081P + P$. Hence $0.1P + P^2 = 0.1 + 0.081P + P$, i.e., $P^2 - 0.981P - 0.1 = 0$. Using the quadratic formula:

    $$
    P = \frac{0.981 + \sqrt{0.981^2 + 0.4}}{2} = \frac{0.981 + \sqrt{1.362}}{2} \approx \frac{0.981 + 1.167}{2} \approx 1.074
    $$

    The standard optimal control gain is:

    $$
    K_{\infty} = \frac{P \cdot 0.9}{0.1 + P} \approx \frac{1.074 \times 0.9}{1.174} \approx 0.823
    $$

    so $u^*_\infty = -0.823 x$ and $w^* = 0$ (no robustness concern).

    **Step 3: Effect of finite $\theta$.** As $\theta$ decreases from infinity:

    - The effective value function parameter $\tilde{P} = P/(1 - 0.25P/\theta) > P$ increases, making the controller more aggressive.
    - The worst-case disturbance $w^* \propto 1/\theta$ grows, injecting more adversarial noise.
    - The control gain $K = \tilde{P} \cdot 0.9 / (0.1 + \tilde{P})$ increases, meaning the controller reacts more strongly to deviations.

    **As $\theta \to \infty$**: The robustness penalty $\theta w^2$ makes any disturbance infinitely costly, so $w^* \to 0$ and the problem reduces to standard LQR. The controller does not hedge against model misspecification.

    **Critical threshold**: The robust solution exists only when $\theta > 0.25P$. Below this threshold, the worst-case disturbance grows without bound, indicating that the level of model uncertainty exceeds what the controller can handle. This breakdown point characterizes the limit of robustness for the given system.
