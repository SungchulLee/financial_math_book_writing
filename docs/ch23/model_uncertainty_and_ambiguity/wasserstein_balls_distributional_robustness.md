# Wasserstein Balls and Distributional Robustness


## Introduction


When specifying an ambiguity set of probability measures for robust decision-making, the choice of metric on the space of distributions is crucial. While Kullback-Leibler divergence and total variation distance have long served as standard tools, the **Wasserstein distance** offers a geometrically natural alternative that respects the underlying metric structure of the outcome space and metrizes weak convergence on Polish spaces.

**Distributional robustness** with Wasserstein balls addresses a central challenge: given an empirical distribution $\hat{P}_n$ estimated from $n$ data points, how should we optimize decisions when the true distribution $P^*$ may differ from $\hat{P}_n$? By centering a Wasserstein ball around $\hat{P}_n$, we obtain an ambiguity set with three key properties:

1. **Geometric awareness**: The Wasserstein distance accounts for the distance between outcomes, not just probability mass transfer
2. **Finite-sample guarantees**: The ball radius can be calibrated so that $P^* \in \mathcal{P}$ with high probability
3. **Tractable reformulations**: For many loss functions, the worst-case problem admits finite-dimensional dual formulations

This framework has become central to robust portfolio optimization, risk measurement, and machine learning applications in finance.

## Optimal Transport and Wasserstein Distance


### 1. The Monge-Kantorovich Problem


The Wasserstein distance originates from the theory of **optimal transport**, which studies the most efficient way to redistribute one probability distribution into another.

**Monge Problem** (1781): Given probability measures $P$ and $Q$ on a metric space $(\mathcal{X}, d)$, find a transport map $T: \mathcal{X} \to \mathcal{X}$ with $T_\# P = Q$ (push-forward) that minimizes total cost:

$$
\inf_{T: T_\# P = Q} \int_{\mathcal{X}} d(x, T(x))^p \, dP(x)
$$

**Limitation**: A transport map may not exist (e.g., when $P$ is a Dirac mass and $Q$ is not).

**Kantorovich Relaxation** (1942): Replace the map $T$ with a coupling (joint distribution) $\pi$ having marginals $P$ and $Q$:

$$
\Pi(P, Q) = \left\{ \pi \in \mathcal{M}_1(\mathcal{X} \times \mathcal{X}) : \pi(\cdot \times \mathcal{X}) = P, \; \pi(\mathcal{X} \times \cdot) = Q \right\}
$$

The relaxed problem always has a solution.

### 2. Wasserstein Distance


**Definition** (p-Wasserstein Distance): For $p \geq 1$ and probability measures $P, Q$ on a Polish metric space $(\mathcal{X}, d)$ with finite $p$-th moments:

$$
W_p(P, Q) = \left( \inf_{\pi \in \Pi(P, Q)} \int_{\mathcal{X} \times \mathcal{X}} d(x, y)^p \, d\pi(x, y) \right)^{1/p}
$$

**Properties**:

1. **Metric**: $W_p$ is a proper metric on the space $\mathcal{P}_p(\mathcal{X})$ of distributions with finite $p$-th moment

2. **Metrizes weak convergence**: On compact $\mathcal{X}$, $W_p(P_n, P) \to 0$ if and only if $P_n \xrightarrow{w} P$

3. **Triangle inequality**: $W_p(P, R) \leq W_p(P, Q) + W_p(Q, R)$

4. **Dominance**: $W_p(P, Q) \leq W_q(P, Q)$ for $p \leq q$ (on bounded spaces)

### 3. The 1-Wasserstein Distance and Kantorovich-Rubinstein Duality


The case $p = 1$ admits a particularly elegant dual characterization.

**Theorem** (Kantorovich-Rubinstein Duality): For probability measures $P, Q$ on a Polish metric space $(\mathcal{X}, d)$:

$$
W_1(P, Q) = \sup_{f \in \text{Lip}_1(\mathcal{X})} \left\{ \int_{\mathcal{X}} f \, dP - \int_{\mathcal{X}} f \, dQ \right\}
$$

where $\text{Lip}_1(\mathcal{X}) = \{ f : |f(x) - f(y)| \leq d(x,y) \text{ for all } x, y \}$ is the set of 1-Lipschitz functions.

**Proof Sketch**: The primal problem is a linear program over couplings $\pi$. By LP duality, the dual variables correspond to Lipschitz functions acting as potentials. The constraint that the dual is finite forces the Lipschitz condition. Strong duality holds by compactness of the set of couplings. $\square$

**Financial Interpretation**: $W_1(P, Q)$ measures the maximum difference in expected values of a 1-Lipschitz payoff function under the two distributions. This captures the idea that distributions close in Wasserstein distance yield similar prices for "well-behaved" derivatives.

### 4. Computation for Discrete Distributions


For empirical distributions $P = \sum_{i=1}^m p_i \delta_{x_i}$ and $Q = \sum_{j=1}^n q_j \delta_{y_j}$, the Wasserstein distance becomes a linear program:

$$
W_p^p(P, Q) = \min_{\pi_{ij} \geq 0} \sum_{i=1}^m \sum_{j=1}^n \pi_{ij} \, d(x_i, y_j)^p
$$

subject to $\sum_j \pi_{ij} = p_i$ and $\sum_i \pi_{ij} = q_j$.

**Complexity**: This transportation problem can be solved in $O((m+n)^3 \log(m+n))$ time, or approximately using Sinkhorn's algorithm with entropic regularization.

**One-Dimensional Case**: When $\mathcal{X} = \mathbb{R}$, the Wasserstein distance has a closed form:

$$
W_p(P, Q) = \left( \int_0^1 |F_P^{-1}(u) - F_Q^{-1}(u)|^p \, du \right)^{1/p}
$$

where $F_P^{-1}$ and $F_Q^{-1}$ are the quantile functions.

## Wasserstein Ambiguity Sets


### 1. Definition and Motivation


**Definition** (Wasserstein Ball): Given a center distribution $\hat{P}$ (typically the empirical measure) and radius $\varepsilon > 0$:

$$
\mathcal{B}_{\varepsilon}(\hat{P}) = \left\{ Q \in \mathcal{P}_p(\mathcal{X}) : W_p(Q, \hat{P}) \leq \varepsilon \right\}
$$

**Motivation**: Given $n$ i.i.d. observations $\hat{x}_1, \ldots, \hat{x}_n$ from the true distribution $P^*$, the empirical measure is $\hat{P}_n = \frac{1}{n} \sum_{i=1}^n \delta_{\hat{x}_i}$. The ball $\mathcal{B}_\varepsilon(\hat{P}_n)$ serves as a confidence region for $P^*$.

### 2. Finite-Sample Guarantees


**Theorem** (Concentration of Empirical Measure): Let $P^*$ be a distribution on $\mathbb{R}^d$ with finite moment generating function in a neighborhood of the origin. Then for $n$ sufficiently large:

$$
\mathbb{P}\left( W_p(P^*, \hat{P}_n) > \varepsilon \right) \leq c_1 \exp(-c_2 n \varepsilon^{\max(d, 2)})
$$

for constants $c_1, c_2 > 0$ depending on $P^*$ and $d$.

**Consequence**: Setting the radius $\varepsilon_n = O(n^{-1/\max(d,2)})$ ensures $P^* \in \mathcal{B}_{\varepsilon_n}(\hat{P}_n)$ with probability at least $1 - \beta$ for prescribed confidence level $\beta$.

**Curse of Dimensionality**: The convergence rate degrades with dimension $d$. For $d \geq 3$, the rate $n^{-1/d}$ is significantly slower than the parametric rate $n^{-1/2}$.

### 3. Comparison with Other Ambiguity Sets


| **Ambiguity Set** | **Ball Definition** | **Strengths** | **Weaknesses** |
|---|---|---|---|
| KL divergence | $D_{\text{KL}}(Q \| \hat{P}) \leq \eta$ | Exponential tilting; tractable | Requires $Q \ll \hat{P}$; no support extension |
| Total variation | $\| Q - \hat{P} \|_{\text{TV}} \leq \delta$ | Simple; metric | Ignores geometry; too conservative |
| Moment-based | $\mathbb{E}_Q[g_i] \in \mathcal{C}_i$ | Uses observable statistics | May include unrealistic measures |
| Wasserstein | $W_p(Q, \hat{P}) \leq \varepsilon$ | Geometric; allows support extension | Slower convergence in high dimensions |

**Key Advantage of Wasserstein**: Unlike KL balls, Wasserstein balls allow the alternative distribution $Q$ to have support outside $\text{supp}(\hat{P})$. This is essential when the empirical distribution is discrete but the true distribution is continuous.

## Distributionally Robust Optimization


### 1. General Problem Formulation


**Distributionally Robust Optimization (DRO)**: Given a loss function $\ell(x, \xi)$ depending on decision $x \in \mathcal{X}$ and random parameter $\xi$:

$$
\inf_{x \in \mathcal{X}} \sup_{Q \in \mathcal{B}_\varepsilon(\hat{P})} \mathbb{E}_Q[\ell(x, \xi)]
$$

**Interpretation**: The decision-maker minimizes the worst-case expected loss over all distributions in the Wasserstein ball. This hedges against estimation error in $\hat{P}$.

### 2. Strong Duality for Wasserstein DRO


**Theorem** (Blanchet-Murthy, 2019): Under mild regularity conditions on $\ell$, for the type-1 Wasserstein ball ($p = 1$):

$$
\sup_{Q: W_1(Q, \hat{P}) \leq \varepsilon} \mathbb{E}_Q[\ell(x, \xi)] = \inf_{\lambda \geq 0} \left\{ \lambda \varepsilon + \mathbb{E}_{\hat{P}}\left[ \sup_{\xi'} \left\{ \ell(x, \xi') - \lambda \, d(\xi, \xi') \right\} \right] \right\}
$$

**Proof Outline**:

*Step 1*: Write the inner supremum as an optimal transport problem between $\hat{P}$ and $Q$ with cost $d(\xi, \xi')^p$, subject to the constraint that the total transport cost does not exceed $\varepsilon^p$.

*Step 2*: Introduce Lagrange multiplier $\lambda$ for the transport cost constraint.

*Step 3*: Exchange the order of optimization (justified by Sion's minimax theorem, since the problem is convex in $Q$ and linear in $\lambda$).

*Step 4*: The inner optimization over $Q$ decouples into pointwise suprema, yielding the stated formula. $\square$

### 3. Tractable Reformulations


**Case 1** (Linear Loss): If $\ell(x, \xi) = a(x)^\top \xi + b(x)$ and $d(\xi, \xi') = \|\xi - \xi'\|$:

$$
\sup_{Q \in \mathcal{B}_\varepsilon(\hat{P})} \mathbb{E}_Q[\ell(x, \xi)] = \mathbb{E}_{\hat{P}}[\ell(x, \xi)] + \varepsilon \|a(x)\|_*
$$

where $\|\cdot\|_*$ is the dual norm. This shows the worst-case expectation adds a regularization term proportional to the radius $\varepsilon$.

**Case 2** (Convex Piecewise Linear Loss): If $\ell(x, \xi) = \max_{k=1,\ldots,K} \{a_k(x)^\top \xi + b_k(x)\}$:

$$
\sup_{Q \in \mathcal{B}_\varepsilon(\hat{P})} \mathbb{E}_Q[\ell(x, \xi)] = \inf_{\lambda \geq 0} \left\{ \lambda \varepsilon + \frac{1}{n} \sum_{i=1}^n \max_{k} \left\{ a_k(x)^\top \hat{\xi}_i + b_k(x) + \lambda \|a_k(x)\|_* \right\} \right\}
$$

which is a finite-dimensional convex program.

**Case 3** (Quadratic Loss): For $\ell(x, \xi) = (\xi - x)^2$ and 2-Wasserstein distance:

$$
\sup_{Q: W_2(Q, \hat{P}) \leq \varepsilon} \mathbb{E}_Q[(\xi - x)^2] = \mathbb{E}_{\hat{P}}[(\xi - x)^2] + \varepsilon^2 + 2\varepsilon \sqrt{\text{Var}_{\hat{P}}(\xi - x)}
$$

## Connection to Regularization


### 1. Wasserstein DRO as Regularized Empirical Risk Minimization


A remarkable connection links distributionally robust optimization with statistical regularization.

**Theorem** (Esfahani-Kuhn, 2018): For the 1-Wasserstein DRO problem with loss $\ell$ that is Lipschitz in $\xi$:

$$
\inf_{x} \sup_{Q: W_1(Q, \hat{P}_n) \leq \varepsilon} \mathbb{E}_Q[\ell(x, \xi)] = \inf_x \left\{ \frac{1}{n} \sum_{i=1}^n \ell(x, \hat{\xi}_i) + \varepsilon \cdot \text{Lip}(\ell(x, \cdot)) \right\}
$$

where $\text{Lip}(\ell(x, \cdot))$ denotes the Lipschitz constant of $\ell$ with respect to $\xi$.

**Interpretation**: The Wasserstein DRO is equivalent to empirical risk minimization with a regularization penalty proportional to the Lipschitz constant of the loss. Larger Wasserstein radius $\varepsilon$ corresponds to stronger regularization.

### 2. Specific Regularization Correspondences


**Logistic Regression**: With log-loss $\ell(w, (x, y)) = \log(1 + \exp(-y \cdot w^\top x))$ and $\ell_2$ ground metric:

$$
\text{DRO} \iff \min_w \frac{1}{n} \sum_{i=1}^n \log(1 + \exp(-y_i w^\top x_i)) + \varepsilon \|w\|_2
$$

This recovers $\ell_2$-regularized logistic regression.

**Linear Regression**: With squared loss and $\ell_2$ metric, the DRO formulation yields a form of ridge regression where the regularization strength is controlled by $\varepsilon$.

### 3. Out-of-Sample Performance Guarantees


**Theorem**: For the DRO optimal decision $x_n^*$:

$$
\mathbb{P}\left( \mathbb{E}_{P^*}[\ell(x_n^*, \xi)] \leq \sup_{Q \in \mathcal{B}_{\varepsilon_n}(\hat{P}_n)} \mathbb{E}_Q[\ell(x_n^*, \xi)] \right) \geq 1 - \beta
$$

provided $\varepsilon_n$ is chosen to satisfy the concentration inequality.

**Implication**: The worst-case cost from the DRO serves as an upper confidence bound on the true out-of-sample performance. This provides a principled alternative to cross-validation.

## Financial Applications


### 1. Distributionally Robust Portfolio Optimization


**Setup**: An investor selects portfolio weights $w$ for $d$ assets with return vector $R$.

**Classical Mean-Variance**:

$$
\max_w \left\{ w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w \right\}
$$

**DRO Portfolio Problem**: Using a Wasserstein ball around the empirical distribution of returns:

$$
\max_w \inf_{Q: W_p(Q, \hat{P}_n) \leq \varepsilon} \left\{ \mathbb{E}_Q[w^\top R] - \frac{\lambda}{2} \text{Var}_Q(w^\top R) \right\}
$$

**Tractable Reformulation** (1-Wasserstein, mean only): When the ambiguity affects only the mean:

$$
\max_w \left\{ w^\top \hat{\mu} - \varepsilon \|w\| - \frac{\lambda}{2} w^\top \hat{\Sigma} w \right\}
$$

**Effect**: The penalty $\varepsilon\|w\|$ shrinks portfolio weights toward zero, preventing extreme positions that arise from estimation error. This provides a geometric interpretation of shrinkage in portfolio theory.

### 2. Distributionally Robust Risk Measurement


**Worst-Case CVaR**: Consider the Conditional Value-at-Risk under distributional uncertainty:

$$
\sup_{Q: W_1(Q, \hat{P}_n) \leq \varepsilon} \text{CVaR}_\alpha^Q(L)
$$

where $L$ is a loss random variable.

**Theorem**: For 1-Wasserstein ambiguity with Lipschitz loss:

$$
\sup_{Q: W_1(Q, \hat{P}_n) \leq \varepsilon} \text{CVaR}_\alpha^Q(L) = \text{CVaR}_\alpha^{\hat{P}_n}(L) + \frac{\varepsilon}{\alpha}
$$

**Interpretation**: Worst-case CVaR adds a buffer proportional to the Wasserstein radius and inversely proportional to the confidence level $\alpha$. More extreme risk measures (smaller $\alpha$) are more sensitive to distributional uncertainty.

### 3. Robust Option Pricing


**Setup**: Price a European derivative with payoff $\Phi(S_T)$ when the risk-neutral distribution is uncertain.

**Wasserstein Pricing Bounds**: Given observed option prices implying an empirical risk-neutral distribution $\hat{Q}$:

$$
\overline{V} = \sup_{Q: W_p(Q, \hat{Q}) \leq \varepsilon} \mathbb{E}_Q[e^{-rT} \Phi(S_T)]
$$

$$
\underline{V} = \inf_{Q: W_p(Q, \hat{Q}) \leq \varepsilon} \mathbb{E}_Q[e^{-rT} \Phi(S_T)]
$$

**Advantage over KL-based bounds**: The Wasserstein bounds allow the worst-case distribution to place mass at stock price levels not observed in the market data, capturing tail risk scenarios absent from the empirical distribution.

### 4. Stress Testing and Scenario Analysis


**Worst-Case Scenario**: The distribution $Q^*$ achieving the supremum in the DRO identifies the most adversarial scenario:

$$
Q^* = \arg\sup_{Q: W_p(Q, \hat{P}) \leq \varepsilon} \mathbb{E}_Q[\ell(\xi)]
$$

For the 1-Wasserstein case, the worst-case distribution shifts mass toward high-loss regions, with the shift magnitude bounded by the Lipschitz constant of the loss.

**Reverse Stress Test**: Find the smallest Wasserstein perturbation causing a specified loss threshold $L_0$:

$$
\varepsilon^* = \inf \left\{ \varepsilon > 0 : \sup_{Q: W_1(Q, \hat{P}) \leq \varepsilon} \mathbb{E}_Q[\ell(\xi)] \geq L_0 \right\}
$$

This identifies how much the distribution must change to trigger a crisis-level loss.

## Theoretical Foundations


### 1. Wasserstein Balls and Weak Convergence


**Theorem**: On a compact metric space $\mathcal{X}$, the Wasserstein ball $\mathcal{B}_\varepsilon(\hat{P})$ is:

1. **Convex**: If $Q_1, Q_2 \in \mathcal{B}_\varepsilon(\hat{P})$, then $\alpha Q_1 + (1-\alpha) Q_2 \in \mathcal{B}_\varepsilon(\hat{P})$ for $\alpha \in [0,1]$

2. **Weakly compact**: $\mathcal{B}_\varepsilon(\hat{P})$ is compact in the weak topology

3. **Tight**: For every $\delta > 0$, there exists a compact $K \subseteq \mathcal{X}$ with $Q(K) \geq 1 - \delta$ for all $Q \in \mathcal{B}_\varepsilon(\hat{P})$

**Proof** (Convexity): For $Q_1, Q_2 \in \mathcal{B}_\varepsilon(\hat{P})$, let $\pi_1, \pi_2$ be optimal couplings. Then $\alpha \pi_1 + (1-\alpha)\pi_2$ is a coupling of $\alpha Q_1 + (1-\alpha)Q_2$ and $\hat{P}$, with transport cost at most $\alpha W_p^p(Q_1, \hat{P}) + (1-\alpha) W_p^p(Q_2, \hat{P}) \leq \varepsilon^p$. $\square$

### 2. Minimax Theorem for Wasserstein DRO


**Theorem** (Interchangeability): Under the following conditions:
- $\mathcal{X}$ is compact and convex
- $\ell(x, \xi)$ is convex in $x$ and upper semicontinuous in $\xi$
- $\varepsilon > 0$

the minimax identity holds:

$$
\inf_{x \in \mathcal{X}} \sup_{Q \in \mathcal{B}_\varepsilon(\hat{P})} \mathbb{E}_Q[\ell(x, \xi)] = \sup_{Q \in \mathcal{B}_\varepsilon(\hat{P})} \inf_{x \in \mathcal{X}} \mathbb{E}_Q[\ell(x, \xi)]
$$

**Proof**: The Wasserstein ball is weakly compact (by Prokhorov's theorem). The map $Q \mapsto \mathbb{E}_Q[\ell(x, \xi)]$ is weakly continuous for each $x$. Apply Sion's minimax theorem. $\square$

### 3. Convergence of DRO Solutions


**Theorem** (Asymptotic Consistency): Let $x_n^*$ be the DRO optimal decision with Wasserstein radius $\varepsilon_n \to 0$ such that $n \varepsilon_n^{\max(d,2)} \to \infty$. Then:

$$
x_n^* \to x^* \quad \text{as } n \to \infty
$$

where $x^* = \arg\min_x \mathbb{E}_{P^*}[\ell(x, \xi)]$ is the true optimal decision.

**Interpretation**: As data accumulates, the DRO solution converges to the oracle solution that knows the true distribution. The Wasserstein ball shrinks but maintains coverage of $P^*$ with high probability.

## Wasserstein Distance vs Other Divergences


### 1. Comparison with KL Divergence


**KL Divergence**: $D_{\text{KL}}(Q \| P) = \mathbb{E}_Q[\log(dQ/dP)]$

**Key Differences**:

- **Support**: KL requires $Q \ll P$ (absolute continuity). Wasserstein allows $\text{supp}(Q) \neq \text{supp}(P)$
- **Geometry**: Wasserstein uses the metric on $\mathcal{X}$; KL is "metric-free"
- **Convergence**: Wasserstein metrizes weak convergence; KL does not
- **Computation**: KL yields exponential tilting (closed-form); Wasserstein requires LP or duality

**When to Use Wasserstein**: Preferred when the empirical distribution has discrete support (e.g., historical return scenarios) but the true distribution is continuous.

**When to Use KL**: Preferred when the reference measure is continuous and exponential tilting formulas provide closed-form solutions (e.g., Hansen-Sargent robust control).

### 2. Wasserstein vs phi-Divergences


**phi-Divergence Ball**: $\mathcal{B}_\phi = \{ Q : D_\phi(Q \| \hat{P}) \leq \eta \}$ where $D_\phi(Q \| P) = \int \phi(dQ/dP) \, dP$.

**Structural Difference**: All $\phi$-divergence balls satisfy $Q \ll \hat{P}$, so the worst-case distribution cannot explore scenarios outside the empirical support. For discrete $\hat{P}_n$ with $n$ atoms, the worst-case distribution under any $\phi$-divergence ball also has at most $n$ atoms.

In contrast, the Wasserstein ball allows the worst-case distribution to spread mass to new locations, providing protection against unseen scenarios.

## Computational Methods


### 1. Reformulation via Semi-Infinite Programming


The Wasserstein DRO:

$$
\sup_{Q: W_1(Q, \hat{P}_n) \leq \varepsilon} \mathbb{E}_Q[\ell(\xi)]
$$

with empirical $\hat{P}_n = \frac{1}{n}\sum_{i=1}^n \delta_{\hat{\xi}_i}$ can be reformulated using the dual as:

$$
\inf_{\lambda \geq 0} \left\{ \lambda \varepsilon + \frac{1}{n} \sum_{i=1}^n \sup_{\xi' \in \mathcal{X}} \left\{ \ell(\xi') - \lambda \, d(\hat{\xi}_i, \xi') \right\} \right\}
$$

Each inner supremum is a one-dimensional optimization problem when $\mathcal{X} \subseteq \mathbb{R}$.

### 2. Sinkhorn Algorithm for Entropic Regularization


**Entropic Regularization**: Approximate the Wasserstein distance by:

$$
W_p^{(\gamma)}(P, Q) = \left( \inf_{\pi \in \Pi(P,Q)} \int d(x,y)^p \, d\pi + \gamma D_{\text{KL}}(\pi \| P \otimes Q) \right)^{1/p}
$$

**Sinkhorn Algorithm**: Alternating projections in dual space converge to the optimal entropic coupling in $O(n^2 / \gamma)$ iterations.

**Advantage**: The entropic regularization makes the problem strongly convex, enabling much faster computation than exact LP solvers for large $n$.

### 3. Cutting-Plane Methods


For problems where the inner supremum is hard to solve globally, a cutting-plane approach iteratively:

1. Solve the outer minimization with a finite subset of scenarios
2. Add the worst-case scenario from the inner maximization
3. Repeat until convergence

This is particularly effective when $\ell$ is convex but not smooth.

## Advanced Topics


### 1. Wasserstein Distributionally Robust Chance Constraints


**Chance Constraint**: Require $\mathbb{P}(\ell(x, \xi) \leq 0) \geq 1 - \alpha$.

**Robust Version**: Require the constraint to hold for all $Q$ in the Wasserstein ball:

$$
\inf_{Q: W_1(Q, \hat{P}_n) \leq \varepsilon} Q(\ell(x, \xi) \leq 0) \geq 1 - \alpha
$$

**Reformulation**: Under convexity of $\ell$ in $\xi$, this can be converted to a tractable second-order cone program (SOCP).

### 2. Multi-Period DRO


**Dynamic Setting**: In a multi-period portfolio problem, distributional uncertainty applies at each stage. The Wasserstein ball must be defined for the joint distribution across periods.

**Rectangular Ambiguity**: Assume independence across stages:

$$
\mathcal{B} = \mathcal{B}_{\varepsilon_1}(\hat{P}_1) \times \cdots \times \mathcal{B}_{\varepsilon_T}(\hat{P}_T)
$$

This preserves dynamic consistency and allows for Bellman equation formulations.

**Non-Rectangular Ambiguity**: Allowing dependence across stages is more realistic but computationally harder, requiring approximation techniques.

### 3. Gao-Kleywegt Growth Rates


**Theorem** (Gao-Kleywegt, 2023): For the type-$\infty$ Wasserstein DRO (where $p \to \infty$):

$$
W_\infty(Q, \hat{P}) = \inf_{\pi \in \Pi(Q, \hat{P})} \text{ess sup}_\pi \, d(x, y)
$$

the worst-case expectation admits the representation:

$$
\sup_{Q: W_\infty(Q, \hat{P}_n) \leq \varepsilon} \mathbb{E}_Q[\ell(\xi)] = \frac{1}{n} \sum_{i=1}^n \sup_{\xi': d(\hat{\xi}_i, \xi') \leq \varepsilon} \ell(\xi')
$$

This has the clean interpretation: each data point can be perturbed by at most $\varepsilon$ in the ground metric.

## Summary and Key Takeaways


1. **Wasserstein Distance**: Provides a geometrically natural metric on distributions that metrizes weak convergence and respects the underlying metric structure of outcomes

2. **Ambiguity Sets**: Wasserstein balls centered at empirical distributions offer finite-sample coverage guarantees and allow support extension beyond observed data points

3. **Duality**: Strong duality results transform infinite-dimensional worst-case problems into tractable finite-dimensional convex programs

4. **Regularization Connection**: Wasserstein DRO is equivalent to regularized empirical risk minimization, providing a principled justification for regularization techniques

5. **Financial Applications**: The framework applies to robust portfolio optimization (shrinkage of weights), worst-case risk measurement (CVaR buffers), robust option pricing (tail risk exploration), and stress testing

6. **Computational Tractability**: For common loss functions and ground metrics, the worst-case problem admits LP, SOCP, or SDP reformulations that scale to realistic problem sizes

7. **Trade-Off**: Compared to KL divergence, Wasserstein offers geometric awareness and support extension at the cost of slower convergence rates in high dimensions and more complex duality formulas

---

## Exercises

**Exercise 1.** Compute the 1-Wasserstein distance $W_1(P, Q)$ between $P = \frac{1}{2}\delta_0 + \frac{1}{2}\delta_2$ and $Q = \frac{1}{2}\delta_1 + \frac{1}{2}\delta_3$ on $\mathbb{R}$ with ground metric $d(x,y) = |x - y|$. Compare this with the total variation distance $\|P - Q\|_{\text{TV}}$ and explain why the Wasserstein distance better captures the geometric proximity of the two distributions.

---

**Exercise 2.** Let $\hat{P}_n = \frac{1}{n}\sum_{i=1}^n \delta_{X_i}$ be the empirical distribution of $n$ samples from $P^* = N(0,1)$. Using the concentration inequality $\mathbb{P}(W_1(\hat{P}_n, P^*) > \varepsilon) \leq C e^{-c n \varepsilon^2}$, determine the radius $\varepsilon_n$ needed so that $P^* \in \mathcal{P}_W(\varepsilon_n) = \{P : W_1(P, \hat{P}_n) \leq \varepsilon_n\}$ with probability at least 95% when $n = 100$.

---

**Exercise 3.** For the distributionally robust portfolio problem $\min_w \sup_{P \in \mathcal{P}_W(\varepsilon)} \mathbb{E}_P[-w^\top R]$, explain why the worst-case distribution shifts probability mass to make the portfolio return as negative as possible while staying within the Wasserstein ball. For a single asset with $\hat{P}_n = \frac{1}{3}\delta_{-0.05} + \frac{1}{3}\delta_{0.02} + \frac{1}{3}\delta_{0.08}$ and $\varepsilon = 0.03$, compute the worst-case expected return for a long position $w = 1$.

---

**Exercise 4.** State and prove the strong duality result for the Wasserstein DRO problem: $\sup_{P \in \mathcal{P}_W(\varepsilon)} \mathbb{E}_P[\ell(x, \xi)] = \inf_{\lambda \geq 0} \{\lambda \varepsilon + \mathbb{E}_{\hat{P}_n}[\sup_{\xi'} \{\ell(x, \xi') - \lambda d(\xi, \xi')\}]\}$. Interpret the dual variable $\lambda$ as a "transportation price" and explain its role in balancing robustness against conservatism.

---

**Exercise 5.** Show that the Wasserstein DRO problem with quadratic loss $\ell(w, r) = -(w^\top r)$ and 2-Wasserstein ball is equivalent to a regularized mean-variance problem. Specifically, derive that $\sup_{P \in \mathcal{P}_{W_2}(\varepsilon)} \mathbb{E}_P[-w^\top R] = -w^\top \hat{\mu} + \varepsilon \|w\|_2$, establishing the connection between distributional robustness and norm regularization.

---

**Exercise 6.** Compare Wasserstein and KL divergence ambiguity sets for computing worst-case CVaR. For the empirical distribution $\hat{P}_3 = \frac{1}{3}\delta_{-0.10} + \frac{1}{3}\delta_{0.00} + \frac{1}{3}\delta_{0.05}$ of portfolio returns, compute the worst-case $\text{CVaR}_{0.95}$ under a Wasserstein ball of radius $\varepsilon = 0.02$. Explain why the Wasserstein formulation can produce losses more extreme than any observed data point, while the KL formulation cannot.

---

**Exercise 7.** A stress testing framework uses Wasserstein balls to generate adverse scenarios. Given an empirical joint distribution of equity returns and credit spreads, describe how to solve $\sup_{P \in \mathcal{P}_W(\varepsilon)} \mathbb{E}_P[\text{Portfolio Loss}]$ computationally. What ground metric $d$ is appropriate for the joint space of returns and spreads, and how does the choice of metric affect the generated stress scenarios?
