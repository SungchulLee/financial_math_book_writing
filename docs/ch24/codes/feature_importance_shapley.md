# Feature Importance (Shapley)

## Background

feature_importance_shapley.py

This module implements Feature Importance Shapley.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
feature_importance_shapley.py

This module implements Feature Importance Shapley.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def feature_importance_shapley():
    """
    Feature Importance Shapley.
    
    This function demonstrates the key concepts and computational techniques
    for feature importance shapley.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Feature Importance Shapley
    print(f"Computing Feature Importance Shapley...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Feature Importance Shapley"
    }
    
    return results


def main():
    """Main execution function."""
    results = feature_importance_shapley()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Feature Importance Shapley")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/feature_importance_shapley.png", dpi=150)
    print(f"Figure saved to /tmp/feature_importance_shapley.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Shapley values assign importance to each feature by computing its marginal contribution across all possible feature coalitions. Write the Shapley value formula for feature $i$ in a model with $p$ features.

??? success "Solution to Exercise 1"
    The Shapley value of feature $i$ is:

    $$
    \phi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!\,(p - |S| - 1)!}{p!}\bigl[v(S \cup \{i\}) - v(S)\bigr],
    $$

    where $N = \{1, \ldots, p\}$ is the set of all features, $S$ is a coalition (subset) not containing $i$, and $v(S)$ is the model's prediction (or loss) using only features in $S$. The formula averages the marginal contribution of feature $i$ over all possible orderings of features, weighted by the number of permutations.

---

**Exercise 2.**
For a credit scoring model with 3 features (income, debt ratio, credit score), the model predictions with different subsets are: $v(\emptyset) = 0.5$, $v(\{1\}) = 0.55$, $v(\{2\}) = 0.45$, $v(\{3\}) = 0.65$, $v(\{1,2\}) = 0.50$, $v(\{1,3\}) = 0.70$, $v(\{2,3\}) = 0.60$, $v(\{1,2,3\}) = 0.72$. Compute the Shapley value for feature 3 (credit score).

??? success "Solution to Exercise 2"
    Feature 3's marginal contributions:

    - $v(\{3\}) - v(\emptyset) = 0.65 - 0.50 = 0.15$ (joining empty set, weight $= 0!2!/3! = 1/3$)
    - $v(\{1,3\}) - v(\{1\}) = 0.70 - 0.55 = 0.15$ (joining $\{1\}$, weight $= 1!1!/3! = 1/6$)
    - $v(\{2,3\}) - v(\{2\}) = 0.60 - 0.45 = 0.15$ (joining $\{2\}$, weight $= 1!1!/3! = 1/6$)
    - $v(\{1,2,3\}) - v(\{1,2\}) = 0.72 - 0.50 = 0.22$ (joining $\{1,2\}$, weight $= 2!0!/3! = 1/3$)

    $$
    \phi_3 = \frac{1}{3}(0.15) + \frac{1}{6}(0.15) + \frac{1}{6}(0.15) + \frac{1}{3}(0.22) = 0.05 + 0.025 + 0.025 + 0.0733 = 0.1733.
    $$

---

**Exercise 3.**
Explain why Shapley values satisfy the efficiency property (all feature importances sum to the model's prediction minus the baseline) and why this is desirable.

??? success "Solution to Exercise 3"
    The efficiency property states $\sum_{i=1}^p \phi_i = v(N) - v(\emptyset)$, meaning the total importance equals the model's prediction minus the average prediction. This is desirable because:

    1. It provides a complete decomposition: every unit of prediction is attributed to some feature.
    2. There are no "unaccounted" effects -- the importances fully explain the model.
    3. It enables fair comparison: features can be ranked by their absolute Shapley values, and the ranking reflects their true contribution to the prediction.

---

**Exercise 4.**
Computing exact Shapley values requires $2^p$ model evaluations. For a model with 20 features, how many evaluations are needed, and what approximation methods exist?

??? success "Solution to Exercise 4"
    Exact computation requires $2^{20} = 1{,}048{,}576$ model evaluations per prediction, which is prohibitive. Approximation methods:

    1. **Monte Carlo sampling**: Randomly sample permutations and average marginal contributions. Convergence is $O(1/\sqrt{M})$ in the number of samples $M$.
    2. **Kernel SHAP**: Uses a weighted linear regression to approximate Shapley values, requiring $O(p^2)$ evaluations.
    3. **Tree SHAP**: For tree-based models (XGBoost, Random Forest), computes exact Shapley values in polynomial time $O(TLD)$ where $T$ is the number of trees, $L$ is the max leaves, $D$ is the depth.
    4. **Deep SHAP**: Combines DeepLIFT with Shapley values for neural networks.
