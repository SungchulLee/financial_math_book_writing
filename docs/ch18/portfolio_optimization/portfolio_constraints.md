

# Portfolio Constraints and Institutional Mandates



In real-world investment environments, portfolios are rarely optimized in an unconstrained setting. Institutional mandates, regulatory requirements, fiduciary responsibilities, and practical considerations impose a wide array of constraints on portfolio construction. These constraints transform the canonical mean-variance optimization problem into a **constrained quadratic program**, often introducing non-convexities and solution path dependencies. From a theoretical perspective, constraints alter the shape of the feasible set and the efficient frontier. From a practical standpoint, they embed investor policy into the optimization process, aligning mathematical solutions with legal, operational, and philosophical objectives.

This section provides a rigorous treatment of constraint modeling in portfolio optimization, characterizes the mathematical and economic implications of various constraint classes, and presents computational techniques for solving constrained portfolio problems under institutional mandates.



## 1. The General Constrained Optimization Problem



We begin by generalizing the mean-variance optimization problem in the presence of constraints:



**Risk-Return Formulation**

$$
\min_{\mathbf{w} \in \mathcal{W}} \; \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w} \quad \text{subject to} \quad \mathbf{w}^T \boldsymbol{\mu} \geq \mu_{\text{target}}, \quad \sum_{i=1}^n w_i = 1
$$



**Sharpe Ratio Maximization**

$$
\max_{\mathbf{w} \in \mathcal{W}} \; \frac{\mathbf{w}^T \boldsymbol{\mu} - r_f}{\sqrt{\mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}}}
$$



**Utility-Based Formulation**

$$
\max_{\mathbf{w} \in \mathcal{W}} \; \mathbf{w}^T \boldsymbol{\mu} - \frac{1}{2} \lambda \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}
$$


In all cases, the constraint set $\mathcal{W}$ encodes institutional, regulatory, and operational limits.



## 2. Common Classes of Portfolio Constraints



### A. Budget and Full Investment Constraints


The standard simplex constraint:
$$
\sum_{i=1}^n w_i = 1
$$
ensures that the portfolio is fully invested. It may be relaxed in the presence of a risk-free asset or leverage.



### B. Box Constraints (Bounds on Individual Weights)


$$
a_i \leq w_i \leq b_i \quad \text{for all } i
$$

- **No short-selling**: $a_i = 0$
- **Exposure caps**: $b_i < 1$ to limit concentration
- Box constraints maintain convexity and are easily handled by QP solvers.



### C. Group and Sector Constraints


Let $\mathcal{G}_k$ denote the index set of assets in group $k$ (e.g., sectors, countries, styles). Then:

$$
\sum_{i \in \mathcal{G}_k} w_i \leq c_k
$$

These constraints enforce diversification by limiting exposure to correlated subsets.



### D. Cardinality Constraints


$$
\sum_{i=1}^n \delta_i \leq K, \quad \delta_i \in \{0, 1\}, \quad w_i \leq \delta_i
$$

These limit the number of active positions in the portfolio, commonly used in institutional mandates to reduce operational complexity or focus on high-conviction bets.

- **Implication**: introduces integer variables → the problem becomes a **Mixed Integer Quadratic Program (MIQP)**.



### E. Turnover and Transaction Cost Constraints


Let $\mathbf{w}^{\text{prev}}$ be the portfolio at the previous period. Then:

$$
\sum_{i=1}^n |w_i - w_i^{\text{prev}}| \leq \tau
$$

Limits rebalancing activity, implicitly controlling transaction costs. These constraints are **non-smooth** (due to the $L_1$ norm) but can be convexified using auxiliary variables.



### F. Risk Exposure and Factor Constraints


Suppose $\mathbf{B}$ is a matrix of asset exposures to risk factors. A factor constraint can be written as:

$$
\mathbf{B}^T \mathbf{w} \in [\boldsymbol{l}, \boldsymbol{u}]
$$

enforcing minimum/maximum exposure to systematic risk sources (e.g., beta, duration, credit, ESG scores).



### G. Regulatory and Legal Constraints


Examples include:

- **UCITS constraints** (in Europe): max 10% in any single issuer, max 40% in combined exposures > 5% each.
- **ERISA rules** (in the U.S.): fiduciary prudence, liquidity, and conflict-of-interest provisions.

These are often encoded as layered logical constraints or nested weight bounds.





## 3. Theoretical Implications of Constraints



Imposing constraints has both **mathematical** and **economic** consequences:

- **Geometry**: Constraints reshape the feasible set, truncating the efficient frontier and removing dominated portfolios.
- **Duality**: Each constraint introduces a **shadow price** or **Lagrange multiplier**, representing the marginal loss in objective for tightening the constraint.
- **Suboptimality**: Constraints impose opportunity costs—optimal portfolios under constraints are never better (and typically worse) than those in the unconstrained problem.
- **Instability**: Some constraints improve robustness (e.g., turnover limits), while others exacerbate sensitivity to input error (e.g., cardinality constraints).



## 4. Solving Constrained Optimization Problems



The solution method depends on the nature of constraints:

- **Convex QP**: Box, group, budget constraints → solvable with `cvxpy`, `quadprog`, or interior-point methods.
- **Mixed Integer QP (MIQP)**: Cardinality, logical constraints → requires `Gurobi`, `CPLEX`, or `SCIP`.
- **Augmented Lagrangian or Penalty Methods**: For soft constraints or when enforcing inexact satisfaction.



#### Python Example: Python with `cvxpy`



```python
import cvxpy as cp

w = cp.Variable(n)
objective = cp.Maximize(mu @ w - 0.5 * cp.quad_form(w, Sigma))
constraints = [
    cp.sum(w) == 1,
    w >= 0,
    w <= 0.2,
    B.T @ w <= factor_upper_bound
]

prob = cp.Problem(objective, constraints)
prob.solve()
```

This framework accommodates layering multiple institutional constraints with high numerical stability.



## 5. Strategic Implications of Constraints



Constraints do not merely limit portfolios—they **reflect institutional identity** and strategic policy. As such, constraint design is part of investment architecture, serving roles such as:

- **Governance and Accountability**: Codify investment beliefs, fiduciary duties, and oversight mechanisms.
- **Risk Control**: Bound leverage, sector tilt, factor exposure, and liquidity risk.
- **Custom Benchmarking**: Align with customized mandates rather than off-the-shelf indexes.
- **Behavioral Anchors**: Reduce performance chasing or manager discretion.

Optimal portfolios must be both **mathematically sound** and **institutionally acceptable**—a balance achieved by embedding constraints that reflect the philosophy, goals, and obligations of the investor.



## Summary



Constraints are not merely technical frictions but foundational elements of institutional portfolio construction. They formalize the real-world limits within which investment decisions are made and link quantitative optimization with policy, governance, and compliance. Understanding the structure, function, and impact of constraints allows practitioners to design better models, communicate trade-offs more effectively, and bridge the gap between theory and implementation in institutional asset management.




