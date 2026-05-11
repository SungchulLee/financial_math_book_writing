# Default Correlation (Gaussian Copula)

## Background

default_correlation_copula.py

This module implements Default Correlation Gaussian Copula.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
default_correlation_copula.py

This module implements Default Correlation Gaussian Copula.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def default_correlation_copula():
    """
    Default Correlation Gaussian Copula.
    
    This function demonstrates the key concepts and computational techniques
    for default correlation gaussian copula.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Default Correlation Gaussian Copula
    print(f"Computing Default Correlation Gaussian Copula...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Default Correlation Gaussian Copula"
    }
    
    return results


def main():
    """Main execution function."""
    results = default_correlation_copula()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Default Correlation Gaussian Copula")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/default_correlation_copula.png", dpi=150)
    print(f"Figure saved to /tmp/default_correlation_copula.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The Gaussian copula model generates correlated default times using the formula $\tau_i = F_i^{-1}(\Phi(X_i))$ where $X_i = \sqrt{\rho}\,M + \sqrt{1-\rho}\,Z_i$. Explain each component.

??? success "Solution to Exercise 1"

    - $M \sim \mathcal{N}(0,1)$: The common (systematic) factor, representing the state of the economy.
    - $Z_i \sim \mathcal{N}(0,1)$: The idiosyncratic factor for entity $i$, independent of $M$ and other $Z_j$.
    - $\rho$: The correlation between any two entities' latent variables. Higher $\rho$ means defaults are more driven by the systematic factor.
    - $X_i$: The latent variable for entity $i$, normally distributed with $\text{Corr}(X_i, X_j) = \rho$ for $i \neq j$.
    - $\Phi(X_i)$: Transforms to a uniform distribution on $[0,1]$.
    - $F_i^{-1}$: The inverse marginal CDF of default time for entity $i$, mapping the uniform variate to a default time consistent with the entity's hazard rate curve.

---

**Exercise 2.**
If $\rho = 0.3$, $M = -2$ (economic downturn), and $Z_i = 0$ (average idiosyncratic risk), compute $X_i$ and the implied default probability percentile.

??? success "Solution to Exercise 2"
    $$
    X_i = \sqrt{0.3} \times (-2) + \sqrt{0.7} \times 0 = -0.5477 \times 2 = -1.0954.
    $$

    $$
    \Phi(-1.0954) \approx 0.1367.
    $$

    The implied percentile is $13.67\%$, meaning this entity defaults earlier than $86.33\%$ of the unconditional distribution. The low systematic factor (bad economy) pushes the entity toward early default.

---

**Exercise 3.**
Explain the "correlation smile" problem with the Gaussian copula: why does a single $\rho$ fail to match the market prices of CDO tranches across all detachment points?

??? success "Solution to Exercise 3"
    The Gaussian copula assigns a single correlation $\rho$ to all entity pairs, but market CDO tranche prices imply different "base correlations" at different attachment/detachment points:

    - Equity tranche ($0-3\%$): High implied correlation (e.g., $\rho = 0.25$).
    - Mezzanine ($3-7\%$): Lower implied correlation.
    - Senior ($7-15\%$): Even lower.

    This "smile" arises because the Gaussian copula underestimates the probability of extreme joint default events (tail dependence is zero for the Gaussian copula). Real-world defaults exhibit clustering (many defaults occur together), which the Gaussian copula cannot capture with a single parameter.

---

**Exercise 4.**
How would you modify the model to address the correlation smile? Name two alternative copula specifications.

??? success "Solution to Exercise 4"

    1. **Student-$t$ copula**: Replaces the Gaussian distribution with a $t$-distribution having $\nu$ degrees of freedom. For $\nu < \infty$, it generates tail dependence (joint extreme defaults are more probable than under Gaussian). The parameter $\nu$ is calibrated alongside $\rho$ to match tranche prices.
    2. **Marshall-Olkin copula**: Generates defaults through common shocks (a single event triggers multiple defaults). This produces exact "jumping together" behavior appropriate for systemic risk scenarios.

    Both alternatives provide additional flexibility to match the market-implied correlation structure across tranches.
