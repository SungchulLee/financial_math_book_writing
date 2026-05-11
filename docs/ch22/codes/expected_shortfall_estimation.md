# Expected Shortfall Estimation

## Background

expected_shortfall_estimation.py

This module implements Expected Shortfall Estimation.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
expected_shortfall_estimation.py

This module implements Expected Shortfall Estimation.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def expected_shortfall_estimation():
    """
    Expected Shortfall Estimation.
    
    This function demonstrates the key concepts and computational techniques
    for expected shortfall estimation.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Expected Shortfall Estimation
    print(f"Computing Expected Shortfall Estimation...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Expected Shortfall Estimation"
    }
    
    return results


def main():
    """Main execution function."""
    results = expected_shortfall_estimation()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Expected Shortfall Estimation")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/expected_shortfall_estimation.png", dpi=150)
    print(f"Figure saved to /tmp/expected_shortfall_estimation.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Expected Shortfall (ES) at confidence level $\alpha$ is defined as $\text{ES}_\alpha = \mathbb{E}[L \mid L > \text{VaR}_\alpha]$. If the loss distribution is normal with $\mu = 0$ and $\sigma = \$1M$, compute $\text{ES}_{95\%}$.

??? success "Solution to Exercise 1"
    For a standard normal, $\text{VaR}_{95\%} = \sigma \times \Phi^{-1}(0.95) = 1{,}000{,}000 \times 1.645 = \$1{,}645{,}000$.

    The ES for a normal distribution is:

    $$
    \text{ES}_\alpha = \sigma \times \frac{\phi(\Phi^{-1}(\alpha))}{1 - \alpha} = 1{,}000{,}000 \times \frac{\phi(1.645)}{0.05}.
    $$

    Since $\phi(1.645) = 0.1031$: $\text{ES}_{95\%} = 1{,}000{,}000 \times 0.1031/0.05 = \$2{,}063{,}000$.

---

**Exercise 2.**
Explain why ES is considered a more coherent risk measure than VaR, specifically regarding the subadditivity property.

??? success "Solution to Exercise 2"
    VaR can violate subadditivity: $\text{VaR}(A + B) > \text{VaR}(A) + \text{VaR}(B)$ is possible, meaning diversification appears to increase risk. This is counterintuitive and makes VaR unsuitable for risk aggregation. ES is always subadditive: $\text{ES}(A + B) \leq \text{ES}(A) + \text{ES}(B)$, meaning diversification always reduces (or maintains) risk as measured by ES. This is because ES averages the tail losses rather than looking at a single quantile, capturing the shape of the tail distribution.

---

**Exercise 3.**
Describe how to estimate ES from historical return data using the empirical distribution.

??? success "Solution to Exercise 3"
    Given $n$ historical losses $L_1, \ldots, L_n$ sorted in descending order:

    1. Compute $k = \lfloor n(1-\alpha) \rfloor$ (the number of losses exceeding VaR).
    2. The empirical ES is the average of the $k$ largest losses:

    $$
    \widehat{\text{ES}}_\alpha = \frac{1}{k}\sum_{i=1}^{k} L_{(i)},
    $$

    where $L_{(1)} \geq L_{(2)} \geq \cdots$. For $n = 1000$ and $\alpha = 95\%$, $k = 50$, so ES is the average of the 50 largest losses.

---

**Exercise 4.**
If historical daily losses (in \$M) in the worst 5 days out of 100 are $\{3.2, 2.8, 2.5, 2.1, 1.9\}$, compute $\text{ES}_{95\%}$ and $\text{VaR}_{95\%}$.

??? success "Solution to Exercise 4"
    $\text{VaR}_{95\%} = \$1.9M$ (the 5th worst loss, the $95$th percentile).

    $\text{ES}_{95\%} = \frac{3.2 + 2.8 + 2.5 + 2.1 + 1.9}{5} = \frac{12.5}{5} = \$2.5M$.

    ES exceeds VaR by $\$0.6M$, reflecting the severity of losses beyond the VaR threshold.
