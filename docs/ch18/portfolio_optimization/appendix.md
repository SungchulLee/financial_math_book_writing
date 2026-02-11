# Appendix



This appendix serves as an advanced supplement to the primary exposition of portfolio optimization by elucidating core mathematical derivations, furnishing robust implementation templates in Python for numerical modeling, and presenting a comprehensive case study leveraging historical financial data. The objective is not only to reinforce theoretical principles but to bridge the gap between mathematical formalism and empirical deployment, thereby equipping the reader with a research-grade framework for quantitative portfolio analysis.





## 1. Analytical Derivation: The Global Minimum Variance Portfolio




**Objective**: Determine the asset allocation vector that minimizes portfolio variance under the constraint of full capital deployment. This archetypal quadratic program provides the analytical nucleus around which modern portfolio theory (MPT) is constructed.



#### Problem Formulation


Let $\boldsymbol{\Sigma} \in \mathbb{R}^{n \times n}$ denote a symmetric, positive definite covariance matrix encapsulating the pairwise return volatilities across $n$ assets. The optimization problem is given by:

$$ \min_{\mathbf{w} \in \mathbb{R}^n} \; \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w} \quad \text{subject to} \quad \mathbf{1}^T \mathbf{w} = 1 $$

This is a strictly convex program with affine constraints, ensuring uniqueness of the optimal solution.



#### Lagrangian Duality and First-Order Conditions


Define the Lagrangian:

$$ \mathcal{L}(\mathbf{w}, \lambda) = \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w} - \lambda(\mathbf{1}^T \mathbf{w} - 1) $$

The Karush-Kuhn-Tucker conditions reduce to:

- $ 2\boldsymbol{\Sigma} \mathbf{w} - \lambda \mathbf{1} = 0 $
- $ \mathbf{1}^T \mathbf{w} = 1 $

Solving yields:

$$ \mathbf{w} = \frac{\boldsymbol{\Sigma}^{-1} \mathbf{1}}{\mathbf{1}^T \boldsymbol{\Sigma}^{-1} \mathbf{1}} $$

This closed-form expression defines the unique minimum variance portfolio on the efficient frontier and establishes a benchmark from which all risk-efficient allocations can be derived.



## 2. Programmatic Infrastructure in Python



This section provides a suite of modular Python scripts designed for high-reliability implementation of key portfolio optimization workflows. Utilizing NumPy, Pandas, and SciPy, these code patterns are adaptable to high-dimensional settings and can be integrated into enterprise-level financial systems.



#### Data Engineering and Preprocessing


```python
import yfinance as yf
import pandas as pd
import numpy as np

tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'META']
data = yf.download(tickers, start='2022-01-01', end='2024-01-01')['Adj Close']
returns = data.pct_change().dropna()
mu = returns.mean() * 252
sigma = returns.cov() * 252
```



#### Closed-Form Minimum Variance Portfolio


```python
from numpy.linalg import inv

ones = np.ones(len(mu))
inv_sigma = inv(sigma)
w_minvar = inv_sigma @ ones / (ones.T @ inv_sigma @ ones)
```


#### Maximum Sharpe Ratio via Constrained Optimization



```python
from scipy.optimize import minimize

def neg_sharpe(w, mu, sigma, rf):
    ret = w @ mu
    vol = np.sqrt(w @ sigma @ w)
    return -((ret - rf) / vol)

constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bounds = [(0, 1)] * len(mu)
x0 = np.ones(len(mu)) / len(mu)

result = minimize(neg_sharpe, x0, args=(mu, sigma, 0.03), bounds=bounds, constraints=constraints)
w_sharpe = result.x
```

These templates offer extensibility to multi-period settings, transaction cost modeling, and robust optimization under parameter uncertainty.

#### Analytical Commentary


- The feasible set is manifest as a dense cloud in mean-volatility space.
- The boundary arc constitutes the efficient frontier.
- The tangency and minimum variance portfolios serve as key portfolio benchmarks.



## 3. Empirical Case Study: Construction of an Optimized FAANG Portfolio



We now present a full-stack implementation of portfolio optimization using the FAANG stocks, chosen for their liquidity, market capitalization, and representation of innovation-driven equity segments.



#### Universe and Data Scope


- **Constituents**: META, AAPL, AMZN, NFLX, GOOG
- **Sample Period**: January 2022 through January 2024



#### Methodological Pipeline


1. Historical price ingestion and returns engineering
2. Annualized moments estimation
3. Monte Carlo simulation of random portfolios
4. Non-parametric construction of the efficient frontier
5. Extraction of extremal portfolios (e.g., min-var, tangency)
6. Visualization of the feasible set and frontier topology



#### Efficient Frontier Visualization: Monte Carlo Simulation


```python
import matplotlib.pyplot as plt

n_assets = len(mu)
n_portfolios = 50000
weights = np.random.rand(n_portfolios, n_assets)
weights /= weights.sum(axis=1, keepdims=True)

rets = weights @ mu.values
vols = np.sqrt(np.einsum('ij,jk,ik->i', weights, sigma.values, weights))
sharpes = (rets - 0.03) / vols

plt.figure(figsize=(10,6))
plt.scatter(vols, rets, c=sharpes, cmap='viridis', alpha=0.2)
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility (σ)')
plt.ylabel('Expected Return (μ)')
plt.title('Efficient Frontier: FAANG Portfolio')
plt.grid(True)
plt.show()
```

## 4. Risk Attribution: Euler Decomposition in Practice



To ensure the internal coherence of portfolio construction, we perform volatility decomposition via Euler’s theorem. This allows for precise auditing of risk contribution by asset and provides a platform for constraint calibration.





#### Python Implementation


```python
port_vol = np.sqrt(w_sharpe @ sigma.values @ w_sharpe)
marg_contrib = sigma.values @ w_sharpe / port_vol
risk_contrib = w_sharpe * marg_contrib

df_rc = pd.DataFrame({
    'Weight': w_sharpe,
    'Marginal Contribution': marg_contrib,
    'Risk Contribution': risk_contrib
}, index=mu.index)

df_rc['% Risk Contribution'] = df_rc['Risk Contribution'] / port_vol
```



#### Interpretation


- Risk dominance may not align with weight dominance—highlighting portfolio concentration risk.
- This decomposition is foundational for risk budgeting, regulatory reporting, and stress-testing.

## Summary





This appendix has synthesized theoretical rigor, computational robustness, and empirical relevance into a unified portfolio optimization module. Through formal proofs, scalable implementation architectures, and real-world validation, it enables advanced practitioners to both construct and interrogate portfolio solutions with precision. These tools not only reinforce quantitative competence but also support the operational and governance needs of institutional asset management.

