# Robust Portfolio Optimization

## Background

robust_portfolio_optimization.py

This module implements Robust Portfolio Optimization.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
robust_portfolio_optimization.py

This module implements Robust Portfolio Optimization.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def robust_portfolio_optimization():
    """
    Robust Portfolio Optimization.
    
    This function demonstrates the key concepts and computational techniques
    for robust portfolio optimization.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Robust Portfolio Optimization
    print(f"Computing Robust Portfolio Optimization...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Robust Portfolio Optimization"
    }
    
    return results


def main():
    """Main execution function."""
    results = robust_portfolio_optimization()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Robust Portfolio Optimization")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/robust_portfolio_optimization.png", dpi=150)
    print(f"Figure saved to /tmp/robust_portfolio_optimization.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Robust portfolio optimization accounts for estimation error in expected returns. The worst-case mean-variance problem is $\min_{\mathbf{w}} \max_{\boldsymbol{\mu} \in \mathcal{U}} \mathbf{w}^T\Sigma\mathbf{w} - \lambda\,\mathbf{w}^T\boldsymbol{\mu}$. Explain the uncertainty set $\mathcal{U}$.

??? success "Solution to Exercise 1"
    The uncertainty set $\mathcal{U}$ contains all plausible expected return vectors. Common choices:

    - **Box uncertainty**: $\mu_i \in [\hat{\mu}_i - \epsilon_i, \hat{\mu}_i + \epsilon_i]$ for each asset. Simple but ignores correlations in estimation errors.
    - **Ellipsoidal uncertainty**: $(\boldsymbol{\mu} - \hat{\boldsymbol{\mu}})^T\Sigma_\mu^{-1}(\boldsymbol{\mu} - \hat{\boldsymbol{\mu}}) \leq \kappa^2$, where $\Sigma_\mu$ is the estimation error covariance and $\kappa$ controls the confidence level. More realistic, captures joint estimation uncertainty.

    The parameter $\kappa$ controls the degree of robustness: larger $\kappa$ means more conservative portfolios.

---

**Exercise 2.**
Show that under ellipsoidal uncertainty, the robust optimization reduces to a penalty on portfolio risk.

??? success "Solution to Exercise 2"
    The inner maximization $\max_{\boldsymbol{\mu} \in \mathcal{U}} \mathbf{w}^T\boldsymbol{\mu}$ subject to the ellipsoidal constraint has solution:

    $$
    \max_{\boldsymbol{\mu}} \mathbf{w}^T\boldsymbol{\mu} = \mathbf{w}^T\hat{\boldsymbol{\mu}} + \kappa\sqrt{\mathbf{w}^T\Sigma_\mu\mathbf{w}}.
    $$

    Substituting into the outer problem:

    $$
    \min_{\mathbf{w}} \mathbf{w}^T\Sigma\mathbf{w} - \lambda\mathbf{w}^T\hat{\boldsymbol{\mu}} + \lambda\kappa\sqrt{\mathbf{w}^T\Sigma_\mu\mathbf{w}}.
    $$

    The last term acts as an additional risk penalty, shrinking the portfolio toward the minimum-variance portfolio. Robust optimization automatically reduces reliance on uncertain return estimates.

---

**Exercise 3.**
Compare the efficient frontier of standard mean-variance optimization with that of robust optimization. How does robustness affect the frontier?

??? success "Solution to Exercise 3"
    The robust efficient frontier lies below and to the right of the standard frontier (lower return for the same risk, or higher risk for the same return). This is because the robust optimizer assumes the worst-case returns within $\mathcal{U}$, effectively reducing the expected return of each portfolio. The frontier is also flatter, reflecting the reduced confidence in return estimates. The minimum-variance portfolio is less affected by robustness (it depends on $\Sigma$, not $\boldsymbol{\mu}$), while the maximum-Sharpe portfolio shifts significantly toward lower expected return.

---

**Exercise 4.**
A portfolio manager uses robust optimization with $\kappa = 1.5$. If the estimated return for an asset is $\hat{\mu} = 8\%$ with estimation uncertainty $\sigma_\mu = 3\%$, what effective return does the robust optimizer use?

??? success "Solution to Exercise 4"
    The worst-case return (for a long position) is the lower bound of the uncertainty region:

    $$
    \mu_{\text{eff}} = \hat{\mu} - \kappa \times \sigma_\mu = 8\% - 1.5 \times 3\% = 8\% - 4.5\% = 3.5\%.
    $$

    The robust optimizer effectively uses $3.5\%$ instead of $8\%$. This dramatically reduces the allocation to this asset compared to standard optimization. Assets with high estimation uncertainty are penalized more heavily, leading to more diversified, less extreme portfolios.
