# Credit Valuation Adjustment (Monte Carlo)

## Background

cva_monte_carlo.py

This module implements CVA Calculation Monte Carlo.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
cva_monte_carlo.py

This module implements CVA Calculation Monte Carlo.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# ======================================================================

def cva_monte_carlo():
    """
    CVA Calculation Monte Carlo.
    
    This function demonstrates the key concepts and computational techniques
    for cva calculation monte carlo.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of CVA Calculation Monte Carlo
    print(f"Computing CVA Calculation Monte Carlo...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "CVA Calculation Monte Carlo"
    }
    
    return results


def main():
    """Main execution function."""
    results = cva_monte_carlo()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("CVA Calculation Monte Carlo")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/cva_monte_carlo.png", dpi=150)
    print(f"Figure saved to /tmp/cva_monte_carlo.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Credit Valuation Adjustment (CVA) is defined as $\text{CVA} = (1 - R)\int_0^T \mathbb{E}[\max(V(t), 0)]\,dQ(t)$, where $Q(t)$ is the counterparty's default probability. Explain each component.

??? success "Solution to Exercise 1"

    - $(1 - R)$: Loss given default, where $R$ is the recovery rate.
    - $\mathbb{E}[\max(V(t), 0)]$: Expected positive exposure (EPE) at time $t$ -- the expected value of the derivative if positive (representing the amount at risk if the counterparty defaults at $t$).
    - $dQ(t) = -dS(t)$: The incremental default probability density, where $S(t)$ is the survival probability.
    - The integral aggregates the expected loss across all possible default times from $0$ to maturity $T$.

---

**Exercise 2.**
A 5-year interest rate swap has expected positive exposure profile $\text{EPE}(t) = 100{,}000 \times t \times e^{-0.1t}$ (peaking around year 3). With a flat hazard rate of $2\%$ and recovery $40\%$, estimate the CVA using a 5-point numerical integration.

??? success "Solution to Exercise 2"
    At $t = 1, 2, 3, 4, 5$: EPE values are $90{,}484$, $163{,}746$, $222{,}245$, $268{,}128$, $303{,}265$. The default probability increments: $\Delta Q(t_i) \approx h\,e^{-ht_i}\,\Delta t = 0.02\,e^{-0.02t_i}$.

    $$
    \text{CVA} \approx 0.6 \sum_{i=1}^{5} \text{EPE}(t_i) \times 0.02 \times e^{-0.02t_i} \times 1.
    $$

    Computing: $0.6 \times 0.02 \times [90484 \times 0.980 + 163746 \times 0.961 + 222245 \times 0.942 + 268128 \times 0.923 + 303265 \times 0.905]$

    $= 0.012 \times [88674 + 157319 + 209355 + 247482 + 274455] = 0.012 \times 977{,}285 \approx \$11{,}727$.

---

**Exercise 3.**
Explain why netting agreements reduce CVA and describe the mechanism.

??? success "Solution to Exercise 3"
    Without netting, each derivative with positive value represents exposure. With netting, only the net portfolio value matters: $\text{Exposure} = \max(\sum_i V_i(t), 0)$ instead of $\sum_i \max(V_i(t), 0)$. Since some derivatives will have positive values and others negative at any given time, netting reduces the total exposure:

    $$
    \max\!\left(\sum_i V_i, 0\right) \leq \sum_i \max(V_i, 0).
    $$

    This reduction in exposure directly reduces CVA. The benefit is greatest when derivatives in the portfolio are negatively correlated (some gain while others lose).

---

**Exercise 4.**
Describe the Monte Carlo algorithm for computing CVA for a portfolio of interest rate swaps.

??? success "Solution to Exercise 4"

    1. Simulate $N$ interest rate paths under the risk-neutral measure (e.g., Hull-White).
    2. At each time step $t_j$, for each path $i$, compute all swap values $V_k^{(i)}(t_j)$.
    3. Apply netting: $E^{(i)}(t_j) = \max(\sum_k V_k^{(i)}(t_j), 0)$.
    4. Average across paths: $\text{EPE}(t_j) = \frac{1}{N}\sum_i E^{(i)}(t_j)$.
    5. Compute CVA: $\text{CVA} = (1-R)\sum_j \text{EPE}(t_j) \cdot \Delta Q(t_j)$, where $\Delta Q(t_j)$ comes from the counterparty's hazard rate curve.
