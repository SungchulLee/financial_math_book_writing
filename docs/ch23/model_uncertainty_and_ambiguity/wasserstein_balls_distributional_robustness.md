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

??? success "Solution to Exercise 1"

    **1-Wasserstein distance**: For $P = \frac{1}{2}\delta_0 + \frac{1}{2}\delta_2$ and $Q = \frac{1}{2}\delta_1 + \frac{1}{2}\delta_3$ on $\mathbb{R}$ with $d(x,y) = |x-y|$, we use the quantile formula:

    $$
    W_1(P, Q) = \int_0^1 |F_P^{-1}(u) - F_Q^{-1}(u)| \, du
    $$

    The quantile functions are:

    - $F_P^{-1}(u) = 0$ for $u \in (0, 0.5]$ and $F_P^{-1}(u) = 2$ for $u \in (0.5, 1]$
    - $F_Q^{-1}(u) = 1$ for $u \in (0, 0.5]$ and $F_Q^{-1}(u) = 3$ for $u \in (0.5, 1]$

    Therefore:

    $$
    W_1(P, Q) = \int_0^{0.5} |0 - 1| \, du + \int_{0.5}^1 |2 - 3| \, du = 0.5 \times 1 + 0.5 \times 1 = 1
    $$

    Alternatively, the optimal transport plan moves mass $\frac{1}{2}$ from 0 to 1 (cost $\frac{1}{2} \times 1 = 0.5$) and mass $\frac{1}{2}$ from 2 to 3 (cost $\frac{1}{2} \times 1 = 0.5$), giving total cost $W_1 = 1$.

    **Total variation distance**: $P$ and $Q$ have disjoint supports ($\{0, 2\}$ vs. $\{1, 3\}$), so:

    $$
    \|P - Q\|_{\text{TV}} = \sup_{A} |P(A) - Q(A)|
    $$

    Taking $A = \{0, 2\}$: $P(A) = 1$, $Q(A) = 0$, so $|P(A) - Q(A)| = 1$. Therefore $\|P - Q\|_{\text{TV}} = 1$.

    Alternatively, using the $L^1$ formula with dominating measure $\mu = P + Q$:

    $$
    \|P - Q\|_{\text{TV}} = \frac{1}{2}\sum_x |P(\{x\}) - Q(\{x\})| = \frac{1}{2}(0.5 + 0.5 + 0.5 + 0.5) = 1
    $$

    **Comparison**: Both distances equal 1, but they capture fundamentally different information. Consider instead $Q' = \frac{1}{2}\delta_{0.1} + \frac{1}{2}\delta_{2.1}$ (a slight perturbation of $P$). Then:

    - $\|P - Q'\|_{\text{TV}} = 1$ (still maximal, since supports are disjoint)
    - $W_1(P, Q') = 0.5 \times 0.1 + 0.5 \times 0.1 = 0.1$ (small, reflecting proximity)

    The Wasserstein distance captures that $P$ and $Q$ are "geometrically close" (each atom is shifted by exactly 1 unit), while TV distance treats any shift in support the same regardless of magnitude. The Wasserstein distance uses the ground metric on $\mathbb{R}$ to distinguish between "nearby" and "far away" distributions, making it more appropriate for applications where the magnitude of distributional shifts matters (e.g., financial returns).

---

**Exercise 2.** Let $\hat{P}_n = \frac{1}{n}\sum_{i=1}^n \delta_{X_i}$ be the empirical distribution of $n$ samples from $P^* = N(0,1)$. Using the concentration inequality $\mathbb{P}(W_1(\hat{P}_n, P^*) > \varepsilon) \leq C e^{-c n \varepsilon^2}$, determine the radius $\varepsilon_n$ needed so that $P^* \in \mathcal{P}_W(\varepsilon_n) = \{P : W_1(P, \hat{P}_n) \leq \varepsilon_n\}$ with probability at least 95% when $n = 100$.

??? success "Solution to Exercise 2"

    **Given**: $\hat{P}_n$ is the empirical distribution of $n = 100$ i.i.d. samples from $P^* = N(0,1)$, and the concentration inequality is:

    $$
    \mathbb{P}(W_1(\hat{P}_n, P^*) > \varepsilon) \leq C e^{-c n \varepsilon^2}
    $$

    (Note: for the 1-dimensional case with $p = 1$, the rate is $\varepsilon^2$ rather than $\varepsilon^{\max(d,2)}$ since $d = 1$ gives $\max(1,2) = 2$.)

    **Requirement**: $P^* \in \mathcal{P}_W(\varepsilon_n)$ with probability at least 95%, i.e.:

    $$
    \mathbb{P}(W_1(\hat{P}_n, P^*) \leq \varepsilon_n) \geq 0.95
    $$

    This means:

    $$
    \mathbb{P}(W_1(\hat{P}_n, P^*) > \varepsilon_n) \leq 0.05
    $$

    Using the concentration bound:

    $$
    C e^{-c n \varepsilon_n^2} \leq 0.05
    $$

    Solving for $\varepsilon_n$:

    $$
    e^{-c n \varepsilon_n^2} \leq \frac{0.05}{C}
    $$

    $$
    -c n \varepsilon_n^2 \leq \log\frac{0.05}{C}
    $$

    $$
    \varepsilon_n^2 \geq \frac{1}{cn}\log\frac{C}{0.05}
    $$

    $$
    \varepsilon_n = \sqrt{\frac{\log(C/0.05)}{cn}}
    $$

    For $n = 100$:

    $$
    \varepsilon_{100} = \sqrt{\frac{\log(C/0.05)}{100c}} = \frac{1}{10}\sqrt{\frac{\log(C/0.05)}{c}}
    $$

    For standard Gaussian data, typical constants are $C \approx 2$ and $c \approx 1/2$ (from sub-Gaussian tail bounds). This gives:

    $$
    \varepsilon_{100} = \frac{1}{10}\sqrt{\frac{\log(2/0.05)}{0.5}} = \frac{1}{10}\sqrt{\frac{\log 40}{0.5}} = \frac{1}{10}\sqrt{\frac{3.689}{0.5}} = \frac{1}{10}\sqrt{7.378} \approx \frac{2.716}{10} \approx 0.272
    $$

    The general scaling is $\varepsilon_n = O(n^{-1/2})$, reflecting the parametric convergence rate in one dimension. With $n = 100$, the radius is on the order of $0.2$--$0.3$, which represents a meaningful level of distributional uncertainty.

---

**Exercise 3.** For the distributionally robust portfolio problem $\min_w \sup_{P \in \mathcal{P}_W(\varepsilon)} \mathbb{E}_P[-w^\top R]$, explain why the worst-case distribution shifts probability mass to make the portfolio return as negative as possible while staying within the Wasserstein ball. For a single asset with $\hat{P}_n = \frac{1}{3}\delta_{-0.05} + \frac{1}{3}\delta_{0.02} + \frac{1}{3}\delta_{0.08}$ and $\varepsilon = 0.03$, compute the worst-case expected return for a long position $w = 1$.

??? success "Solution to Exercise 3"

    **Why the worst case shifts mass negatively**: For the problem $\sup_{P \in \mathcal{P}_W(\varepsilon)} \mathbb{E}_P[-w^\top R]$, with $w = 1$ (long position in a single asset), we want to maximize $\mathbb{E}_P[-R]$, i.e., minimize $\mathbb{E}_P[R]$. The worst-case distribution shifts mass toward lower return values. The Wasserstein constraint limits how far mass can be moved: the average distance (in the ground metric) between the original and perturbed returns cannot exceed $\varepsilon$.

    **Computation**: The empirical distribution is $\hat{P}_3 = \frac{1}{3}\delta_{-0.05} + \frac{1}{3}\delta_{0.02} + \frac{1}{3}\delta_{0.08}$ with $\varepsilon = 0.03$.

    The reference expected return is:

    $$
    \mathbb{E}_{\hat{P}_3}[R] = \frac{1}{3}(-0.05 + 0.02 + 0.08) = \frac{0.05}{3} \approx 0.01667
    $$

    Using the strong duality result for 1-Wasserstein DRO with linear loss $\ell(\xi) = -\xi$ (which is 1-Lipschitz when the ground metric is $|\cdot|$):

    $$
    \sup_{P: W_1(P, \hat{P}_3) \leq \varepsilon} \mathbb{E}_P[-R] = \mathbb{E}_{\hat{P}_3}[-R] + \varepsilon \cdot \text{Lip}(-R)
    $$

    Since $\ell(r) = -r$ has Lipschitz constant 1 (for $d(r, r') = |r - r'|$):

    $$
    \sup_{P: W_1(P, \hat{P}_3) \leq \varepsilon} \mathbb{E}_P[-R] = -0.01667 + 0.03 \times 1 = 0.01333
    $$

    Therefore the worst-case expected return is:

    $$
    \inf_{P: W_1(P, \hat{P}_3) \leq \varepsilon} \mathbb{E}_P[R] = 0.01667 - 0.03 = -0.01333
    $$

    **Interpretation**: The worst-case distribution shifts each atom leftward by 0.03, giving $\hat{P}^* = \frac{1}{3}\delta_{-0.08} + \frac{1}{3}\delta_{-0.01} + \frac{1}{3}\delta_{0.05}$, which has expected return $-0.01333$. The Wasserstein ball of radius 0.03 transforms a mildly positive expected return (1.67%) into a negative worst-case return ($-1.33$%), reflecting the impact of distributional uncertainty on a long position.

---

**Exercise 4.** State and prove the strong duality result for the Wasserstein DRO problem: $\sup_{P \in \mathcal{P}_W(\varepsilon)} \mathbb{E}_P[\ell(x, \xi)] = \inf_{\lambda \geq 0} \{\lambda \varepsilon + \mathbb{E}_{\hat{P}_n}[\sup_{\xi'} \{\ell(x, \xi') - \lambda d(\xi, \xi')\}]\}$. Interpret the dual variable $\lambda$ as a "transportation price" and explain its role in balancing robustness against conservatism.

??? success "Solution to Exercise 4"

    **Statement (Strong Duality)**: For the type-1 Wasserstein ball ($p = 1$) centered at the empirical distribution $\hat{P}_n = \frac{1}{n}\sum_{i=1}^n \delta_{\hat{\xi}_i}$:

    $$
    \sup_{Q: W_1(Q, \hat{P}_n) \leq \varepsilon} \mathbb{E}_Q[\ell(x, \xi)] = \inf_{\lambda \geq 0} \left\{ \lambda \varepsilon + \frac{1}{n} \sum_{i=1}^n \sup_{\xi'} \left\{ \ell(x, \xi') - \lambda \, d(\hat{\xi}_i, \xi') \right\} \right\}
    $$

    **Proof**:

    *Step 1 (Primal reformulation)*: The left-hand side can be written as an optimal transport problem. Any $Q$ with $W_1(Q, \hat{P}_n) \leq \varepsilon$ can be represented through a coupling $\pi$ of $Q$ and $\hat{P}_n$:

    $$
    \sup_{Q: W_1(Q, \hat{P}_n) \leq \varepsilon} \mathbb{E}_Q[\ell(x, \xi)] = \sup_{\pi \in \Pi} \left\{ \int \ell(x, \xi') \, d\pi(\xi, \xi') : \int d(\xi, \xi') \, d\pi \leq \varepsilon, \; \pi_1 = \hat{P}_n \right\}
    $$

    Since $\hat{P}_n$ is discrete, the coupling decomposes as $\pi = \frac{1}{n}\sum_{i=1}^n \delta_{\hat{\xi}_i} \otimes Q_i$ where $Q_i$ is the conditional distribution of $\xi'$ given $\xi = \hat{\xi}_i$:

    $$
    = \sup_{Q_1, \ldots, Q_n} \left\{ \frac{1}{n} \sum_{i=1}^n \mathbb{E}_{Q_i}[\ell(x, \xi')] : \frac{1}{n}\sum_{i=1}^n \mathbb{E}_{Q_i}[d(\hat{\xi}_i, \xi')] \leq \varepsilon \right\}
    $$

    *Step 2 (Lagrangian relaxation)*: Introduce multiplier $\lambda \geq 0$ for the transport constraint:

    $$
    \leq \inf_{\lambda \geq 0} \sup_{Q_1, \ldots, Q_n} \left\{ \frac{1}{n}\sum_{i=1}^n \mathbb{E}_{Q_i}[\ell(x, \xi')] + \lambda\left(\varepsilon - \frac{1}{n}\sum_{i=1}^n \mathbb{E}_{Q_i}[d(\hat{\xi}_i, \xi')]\right) \right\}
    $$

    $$
    = \inf_{\lambda \geq 0} \left\{ \lambda \varepsilon + \frac{1}{n}\sum_{i=1}^n \sup_{Q_i} \mathbb{E}_{Q_i}[\ell(x, \xi') - \lambda d(\hat{\xi}_i, \xi')] \right\}
    $$

    *Step 3 (Pointwise supremum)*: Since each $Q_i$ can be any distribution, and $\sup_Q \mathbb{E}_Q[g(\xi')] = \sup_{\xi'} g(\xi')$ (the supremum of a linear functional over all distributions is the pointwise supremum):

    $$
    = \inf_{\lambda \geq 0} \left\{ \lambda \varepsilon + \frac{1}{n}\sum_{i=1}^n \sup_{\xi'} \{\ell(x, \xi') - \lambda d(\hat{\xi}_i, \xi')\} \right\}
    $$

    *Step 4 (Strong duality)*: Weak duality (primal $\leq$ dual) follows from Steps 1-3. Strong duality (equality) holds because the primal problem is a linear optimization over couplings (a convex program), and Slater's condition is satisfied when $\varepsilon > 0$ (the constraint $W_1 \leq \varepsilon$ has a strictly feasible point, namely $Q = \hat{P}_n$ with $W_1 = 0 < \varepsilon$). $\square$

    **Interpretation of $\lambda$**: The dual variable $\lambda$ acts as a **transportation price** (unit cost per unit distance of probability mass displacement):

    - **Large $\lambda$**: Transportation is expensive, so the worst-case distribution stays close to $\hat{P}_n$. The term $\lambda \varepsilon$ dominates, and robustness costs are high but perturbations are small. Each $\sup_{\xi'}\{\ell(x,\xi') - \lambda d(\hat{\xi}_i, \xi')\}$ is close to $\ell(x, \hat{\xi}_i)$ since moving far from $\hat{\xi}_i$ incurs a large penalty.

    - **Small $\lambda$**: Transportation is cheap, so the worst-case distribution can shift mass to adversarial locations far from the empirical data. The inner suprema explore extreme values of $\ell$, making the formulation more conservative.

    The optimal $\lambda^*$ balances the budget term $\lambda \varepsilon$ against the per-sample worst-case losses, effectively calibrating the trade-off between robustness (protection against distribution shifts) and conservatism (overly pessimistic evaluations).

---

**Exercise 5.** Show that the Wasserstein DRO problem with quadratic loss $\ell(w, r) = -(w^\top r)$ and 2-Wasserstein ball is equivalent to a regularized mean-variance problem. Specifically, derive that $\sup_{P \in \mathcal{P}_{W_2}(\varepsilon)} \mathbb{E}_P[-w^\top R] = -w^\top \hat{\mu} + \varepsilon \|w\|_2$, establishing the connection between distributional robustness and norm regularization.

??? success "Solution to Exercise 5"

    **Setup**: We have the DRO problem with linear loss $\ell(w, r) = -(w^\top r)$ (negative portfolio return) and 2-Wasserstein ball $\mathcal{P}_{W_2}(\varepsilon)$.

    We want to show:

    $$
    \sup_{P: W_2(P, \hat{P}_n) \leq \varepsilon} \mathbb{E}_P[-w^\top R] = -w^\top \hat{\mu} + \varepsilon \|w\|_2
    $$

    **Step 1: Reformulate using Kantorovich duality.** For the 2-Wasserstein case with linear loss, we use the fact that for any coupling $\pi$ of $P$ and $\hat{P}_n$:

    $$
    \mathbb{E}_P[-w^\top R] = \mathbb{E}_\pi[-w^\top r'] = \mathbb{E}_{\hat{P}_n}[-w^\top r] + \mathbb{E}_\pi[-w^\top(r' - r)]
    $$

    where $(r, r') \sim \pi$ with $r$-marginal $\hat{P}_n$ and $r'$-marginal $P$.

    **Step 2: Bound the perturbation term.** By Cauchy-Schwarz:

    $$
    \mathbb{E}_\pi[-w^\top(r' - r)] \leq \mathbb{E}_\pi[\|w\|_2 \|r' - r\|_2] \leq \|w\|_2 \sqrt{\mathbb{E}_\pi[\|r'-r\|_2^2]}
    $$

    The last step uses Jensen's inequality ($\mathbb{E}[X] \leq \sqrt{\mathbb{E}[X^2]}$). The constraint $W_2(P, \hat{P}_n) \leq \varepsilon$ means:

    $$
    \inf_\pi \sqrt{\mathbb{E}_\pi[\|r'-r\|_2^2]} \leq \varepsilon
    $$

    Therefore $\mathbb{E}_\pi[\|r'-r\|_2^2] \leq \varepsilon^2$ for the optimal coupling, giving:

    $$
    \sup_{P: W_2(P, \hat{P}_n) \leq \varepsilon} \mathbb{E}_P[-w^\top R] \leq -w^\top \hat{\mu} + \varepsilon \|w\|_2
    $$

    **Step 3: Attainment.** The upper bound is achieved by the distribution that shifts all mass in the direction $-w / \|w\|_2$ by distance $\varepsilon$. Specifically, define $P^*$ as the distribution of $R' = R + \varepsilon \cdot \frac{-w}{\|w\|_2}$ where $R \sim \hat{P}_n$. Then:

    $$
    W_2(P^*, \hat{P}_n) = \varepsilon \quad \text{(deterministic shift)}
    $$

    and:

    $$
    \mathbb{E}_{P^*}[-w^\top R'] = -w^\top \hat{\mu} - w^\top \left(\frac{-\varepsilon w}{\|w\|_2}\right) = -w^\top \hat{\mu} + \frac{\varepsilon \|w\|_2^2}{\|w\|_2} = -w^\top \hat{\mu} + \varepsilon \|w\|_2
    $$

    **Connection to regularization**: The DRO portfolio problem becomes:

    $$
    \min_w \sup_{P \in \mathcal{P}_{W_2}(\varepsilon)} \mathbb{E}_P[-w^\top R] = \min_w \{-w^\top \hat{\mu} + \varepsilon \|w\|_2\}
    $$

    This is empirical risk minimization ($-w^\top \hat{\mu}$) plus an $\ell_2$-norm regularization penalty ($\varepsilon \|w\|_2$). The Wasserstein radius $\varepsilon$ plays the role of the regularization parameter. This provides a decision-theoretic justification for norm-penalized portfolio optimization: shrinking portfolio weights toward zero is equivalent to hedging against distributional uncertainty in the return distribution.

---

**Exercise 6.** Compare Wasserstein and KL divergence ambiguity sets for computing worst-case CVaR. For the empirical distribution $\hat{P}_3 = \frac{1}{3}\delta_{-0.10} + \frac{1}{3}\delta_{0.00} + \frac{1}{3}\delta_{0.05}$ of portfolio returns, compute the worst-case $\text{CVaR}_{0.95}$ under a Wasserstein ball of radius $\varepsilon = 0.02$. Explain why the Wasserstein formulation can produce losses more extreme than any observed data point, while the KL formulation cannot.

??? success "Solution to Exercise 6"

    **Setup**: $\hat{P}_3 = \frac{1}{3}\delta_{-0.10} + \frac{1}{3}\delta_{0.00} + \frac{1}{3}\delta_{0.05}$ with $\varepsilon = 0.02$ and confidence level $\alpha = 0.05$ (so $\text{CVaR}_{0.95}$ is the expected loss in the worst 5% of cases).

    **Empirical CVaR at 95%**: CVaR$_{0.95}$ under $\hat{P}_3$ is the conditional expectation of losses below the 5th percentile. Since we have 3 equally weighted atoms at returns $\{-0.10, 0.00, 0.05\}$ (or losses $\{0.10, 0.00, -0.05\}$):

    The VaR$_{0.95}$ is the $5\%$ quantile of the loss distribution. With only 3 atoms, the worst loss is $0.10$ with probability $1/3 \approx 33.3\%$. Since $5\% < 33.3\%$, VaR$_{0.95} = 0.10$ and CVaR$_{0.95} = 0.10$ (the expected loss conditional on being in the worst 5% tail, which falls entirely within the atom at loss $= 0.10$).

    **Worst-case CVaR under Wasserstein ball**: Using the result from the chapter:

    $$
    \sup_{Q: W_1(Q, \hat{P}_3) \leq \varepsilon} \text{CVaR}_\alpha^Q(L) = \text{CVaR}_\alpha^{\hat{P}_3}(L) + \frac{\varepsilon}{\alpha}
    $$

    With $\varepsilon = 0.02$ and $\alpha = 0.05$:

    $$
    \text{Worst-case CVaR}_{0.95} = 0.10 + \frac{0.02}{0.05} = 0.10 + 0.40 = 0.50
    $$

    **Why the Wasserstein formulation produces extreme losses**: The worst-case CVaR of 0.50 (a 50% loss) far exceeds any observed data point (maximum observed loss is 10%). This happens because the Wasserstein ball allows the adversarial distribution to move mass to points outside the empirical support. Specifically, the worst-case distribution can shift the left-tail atom from $-0.10$ to a much more extreme negative return, creating a scenario more severe than anything in the historical data.

    The formula $\varepsilon/\alpha$ amplifies the Wasserstein radius by $1/\alpha = 20$. The intuition is: CVaR focuses on the $\alpha = 5\%$ tail, but the Wasserstein budget of $\varepsilon = 0.02$ can be concentrated entirely on this 5% tail. Since the tail has probability mass $\alpha$, the per-unit-mass perturbation is $\varepsilon / \alpha$, creating a large shift in the conditional tail expectation.

    **KL formulation comparison**: Under a KL ball, any $Q \ll \hat{P}_3$ must be supported on $\{-0.10, 0.00, 0.05\}$. The worst case can only reweight these three atoms, not introduce new ones. The maximum loss under any reweighting is still 0.10 (achieved by putting all mass on the worst atom). Therefore:

    $$
    \sup_{Q: D_{\text{KL}}(Q \| \hat{P}_3) \leq \eta} \text{CVaR}_{0.95}^Q(L) \leq 0.10
    $$

    regardless of $\eta$. The KL-based worst-case CVaR is bounded by the most extreme observed data point (0.10), while the Wasserstein-based formulation (0.50) can explore losses 5x worse than any historical observation. This is the fundamental difference: KL-based robustness reweights existing scenarios, while Wasserstein-based robustness creates new scenarios.

---

**Exercise 7.** A stress testing framework uses Wasserstein balls to generate adverse scenarios. Given an empirical joint distribution of equity returns and credit spreads, describe how to solve $\sup_{P \in \mathcal{P}_W(\varepsilon)} \mathbb{E}_P[\text{Portfolio Loss}]$ computationally. What ground metric $d$ is appropriate for the joint space of returns and spreads, and how does the choice of metric affect the generated stress scenarios?

??? success "Solution to Exercise 7"

    **Problem formulation**: Given $n$ historical observations of joint equity returns $r_i$ and credit spread changes $s_i$, the empirical distribution is $\hat{P}_n = \frac{1}{n}\sum_{i=1}^n \delta_{(r_i, s_i)}$. We solve:

    $$
    \sup_{P: W_p(P, \hat{P}_n) \leq \varepsilon} \mathbb{E}_P[\text{Loss}(r, s)]
    $$

    **Computational approach using strong duality**: Applying the dual reformulation for the 1-Wasserstein case:

    $$
    = \inf_{\lambda \geq 0} \left\{ \lambda \varepsilon + \frac{1}{n}\sum_{i=1}^n \sup_{(r', s')} \left\{ \text{Loss}(r', s') - \lambda \, d((r_i, s_i), (r', s')) \right\} \right\}
    $$

    **Step 1** (Inner optimization): For each historical scenario $(r_i, s_i)$, solve:

    $$
    \max_{(r', s')} \left\{ \text{Loss}(r', s') - \lambda \, d((r_i, s_i), (r', s')) \right\}
    $$

    If Loss is a smooth function of $(r, s)$, this is a standard nonlinear optimization problem in 2 dimensions. If Loss is convex and piecewise linear (e.g., for portfolios of vanilla instruments), the inner problem admits closed-form solutions or efficient LP formulations.

    **Step 2** (Outer optimization): The function $g(\lambda) = \lambda \varepsilon + \frac{1}{n}\sum_i h_i(\lambda)$ where $h_i(\lambda)$ is the optimal value of each inner problem is convex in $\lambda$ (as the pointwise supremum of affine functions). Minimize over $\lambda \geq 0$ using bisection or golden section search.

    **Step 3** (Scenario recovery): The worst-case distribution is $P^* = \frac{1}{n}\sum_{i=1}^n \delta_{(r_i^*, s_i^*)}$ where $(r_i^*, s_i^*)$ are the optimizers of the inner problems at $\lambda = \lambda^*$.

    **Choice of ground metric**: The metric $d$ on $\mathbb{R}^2$ (returns $\times$ spreads) must account for the different scales and financial significance of the two dimensions.

    *Option 1: Weighted Euclidean norm*:

    $$
    d((r_1, s_1), (r_2, s_2)) = \sqrt{w_r(r_1 - r_2)^2 + w_s(s_1 - s_2)^2}
    $$

    where $w_r, w_s > 0$ are weights reflecting the relative importance or scale of each variable. A natural choice is $w_r = 1/\sigma_r^2$ and $w_s = 1/\sigma_s^2$ (Mahalanobis-like), so that a 1-sigma move in either dimension contributes equally.

    *Option 2: Mahalanobis distance*:

    $$
    d(\xi_1, \xi_2) = \sqrt{(\xi_1 - \xi_2)^\top \hat{\Sigma}^{-1} (\xi_1 - \xi_2)}
    $$

    where $\hat{\Sigma}$ is the empirical covariance. This accounts for correlations between returns and spreads, measuring perturbations in units of statistical significance.

    *Option 3: $\ell_1$ norm*:

    $$
    d((r_1, s_1), (r_2, s_2)) = |r_1 - r_2| + |s_1 - s_2|
    $$

    This leads to separable inner problems (can perturb $r$ and $s$ independently).

    **Impact on stress scenarios**:

    - **Euclidean metric**: The worst-case perturbation moves each scenario along the direction of steepest increase in Loss, forming a "ball" of perturbations. Cross-effects between $r$ and $s$ are treated independently.

    - **Mahalanobis metric**: Perturbations along the principal axes of the empirical distribution are penalized differently. Perturbations along the direction of high historical correlation (e.g., equity drop + spread widening) are cheaper (smaller $d$), so the stress scenarios naturally preserve empirical correlation structure. This produces more plausible stress scenarios.

    - **$\ell_1$ metric**: The worst-case perturbation concentrates its budget on one dimension (the most impactful). This produces "corner" scenarios where either returns drop sharply with unchanged spreads, or spreads widen sharply with unchanged returns. These may miss the important joint tail events.

    **Practical recommendation**: Use the Mahalanobis distance for the ground metric. This ensures that stress scenarios maintain realistic correlation structure (equity sell-offs coinciding with credit spread widening, as typically observed in crises) while exploring worst-case magnitudes within the Wasserstein budget. The radius $\varepsilon$ should be calibrated using the finite-sample concentration inequality or by backtesting against historical stress periods.
