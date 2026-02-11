

# Convex Optimization and the Sharpe Ratio Frontier



While stochastic simulation provides an empirical perspective on the feasible set of portfolios, optimization techniques grounded in convex analysis offer a precise and computationally efficient means of locating portfolios that satisfy specific optimality criteria. Among these, the maximization of the **Sharpe Ratio**—which characterizes the slope of the Capital Market Line—plays a central role in the construction of risk-adjusted optimal portfolios. This section develops the mathematical formulation of the Sharpe maximization problem under convex constraints and demonstrates its solution via numerical optimization techniques.



## 1. Revisiting the Sharpe Ratio as a Portfolio Objective



The **Sharpe Ratio**, defined as the excess return per unit of risk, is given by:

$$
S(\mathbf{w}) = \frac{\mathbf{w}^T \boldsymbol{\mu} - r_f}{\sqrt{\mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}}}
$$

where:

- $\mathbf{w} \in \mathbb{R}^n$ is the portfolio weight vector,
- $\boldsymbol{\mu} \in \mathbb{R}^n$ is the vector of expected returns,
- $r_f \in \mathbb{R}$ is the risk-free rate,
- $\boldsymbol{\Sigma} \in \mathbb{R}^{n \times n}$ is the covariance matrix of asset returns.

The tangency portfolio is the solution to the problem:

$$
\mathbf{w}^* = \arg\max_{\mathbf{w} \in \mathcal{W}} \; S(\mathbf{w})
$$

subject to:

$$
\sum_{i=1}^n w_i = 1, \quad w_i \geq 0 \text{ (optional)}
$$

Due to the nonlinearity of the objective function (ratio of affine to quadratic), the problem is not convex in its original form. However, it can be reformulated as a **quadratic program** (QP) via scale invariance and normalization.



## 2. Convex Reformulation via Variance Minimization



Consider the equivalent optimization problem:

$$
\min_{\mathbf{w}} \; \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w} \quad \text{subject to} \quad \mathbf{w}^T (\boldsymbol{\mu} - r_f \mathbf{1}) = 1
$$

This problem minimizes the portfolio variance under the constraint that the portfolio's excess return equals one unit. Since this is a **quadratically constrained linear program**, it admits a unique global optimum if $\boldsymbol{\Sigma}$ is positive definite (as it typically is, assuming no perfectly colinear assets).

The optimal solution to this problem, denoted $\mathbf{w}_{\text{MSR}}$, can then be rescaled to ensure that the weights sum to one, yielding the tangency portfolio.

Alternatively, one can use numerical solvers to directly maximize the Sharpe Ratio subject to a normalization constraint, bypassing reformulation.



## 3. Numerical Optimization via `scipy.optimize.minimize`



We now implement a numerical solution using `scipy.optimize.minimize`. Define the **negative Sharpe Ratio** objective:

```python
def negative_sharpe_ratio(w, mu, sigma, rf):
    port_return = w @ mu
    port_vol = np.sqrt(w @ sigma @ w.T)
    return - (port_return - rf) / port_vol
```

Constraints and bounds can be specified explicitly:

```python
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bounds = [(0, 1)] * len(mu)  # No short-selling
x0 = np.ones(len(mu)) / len(mu)  # Initial guess

result = minimize(
    negative_sharpe_ratio,
    x0,
    args=(mu.values, sigma.values, risk_free_rate),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)
```

The result object contains:

- `result.x`: optimal weight vector,
- `-result.fun`: value of the maximum Sharpe Ratio,
- diagnostic flags regarding convergence.

This approach allows for highly flexible specification of additional constraints (e.g., sector constraints, turnover penalties, minimum allocation thresholds) and is robust to non-Gaussian return structures.



## 4. Comparison to Simulated Portfolios



While the simulated efficient frontier provides a comprehensive empirical portrait of feasible portfolios, the convex optimization procedure yields the precise solution to the Sharpe Ratio maximization problem under the specified constraints. Comparing these two approaches enables both verification and sensitivity analysis:

- **Alignment of Optima**: The optimal portfolio from convex optimization should match the empirical tangency point from simulation.
- **Stability**: If small perturbations to inputs (e.g., $\mu$, $\Sigma$) lead to large changes in $\mathbf{w}^*$, the problem is ill-conditioned.
- **Dimensionality Effects**: Optimization is especially advantageous when the asset universe is large or when constraints are highly structured.



## 5. Visualization of the Tangency Portfolio and CML



Upon obtaining the tangency portfolio, the **Capital Market Line (CML)** can be computed and visualized. The CML represents all portfolios formed as linear combinations of the risk-free asset and the tangency portfolio:

$$
\mu_C = r_f + \frac{\mu_T - r_f}{\sigma_T} \cdot \sigma_C
$$

where $(\mu_T, \sigma_T)$ are the return and volatility of the tangency portfolio.

```python
tangency_return = mu.values @ result.x
tangency_vol = np.sqrt(result.x @ sigma.values @ result.x)
cml_x = np.linspace(0, tangency_vol + 0.05, 100)
cml_y = risk_free_rate + ((tangency_return - risk_free_rate) / tangency_vol) * cml_x

plt.plot(cml_x, cml_y, '--', label='Capital Market Line', color='green')
plt.scatter(tangency_vol, tangency_return, color='gold', label='Tangency Portfolio')
```

This line provides a visual reference for the maximum achievable Sharpe Ratio and serves as a guide for constructing leveraged portfolios or capital allocation lines.

## Summary





This section has formally introduced convex optimization as a principled and computationally efficient mechanism for constructing optimal portfolios under mean-variance criteria. The maximization of the Sharpe Ratio, whether implemented via transformation or direct numerical methods, yields a unique and interpretable solution under reasonable assumptions. The juxtaposition of convex optimization and stochastic simulation enables a hybrid approach—leveraging both theoretical rigor and empirical flexibility—that is well-suited for modern portfolio construction.

