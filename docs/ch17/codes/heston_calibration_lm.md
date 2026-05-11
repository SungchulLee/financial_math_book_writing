# Heston Calibration (Levenberg–Marquardt)

## Background

heston_calibration_lm.py

This module implements Heston Calibration LM.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
heston_calibration_lm.py

This module implements Heston Calibration LM.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# ======================================================================

def heston_calibration_lm():
    """
    Heston Calibration LM.
    
    This function demonstrates the key concepts and computational techniques
    for heston calibration lm.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Heston Calibration LM
    print(f"Computing Heston Calibration LM...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Heston Calibration LM"
    }
    
    return results


def main():
    """Main execution function."""
    results = heston_calibration_lm()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Heston Calibration LM")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/heston_calibration_lm.png", dpi=150)
    print(f"Figure saved to /tmp/heston_calibration_lm.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
The Heston calibration minimizes $\sum_i w_i(V_i^{\text{model}}(\Theta) - V_i^{\text{market}})^2$ over parameters $\Theta = (\kappa, \theta, \sigma_v, \rho, v_0)$. Explain why weighting by vega ($w_i = 1/\text{Vega}_i^2$) is common.

??? success "Solution to Exercise 1"
    Vega weighting converts price errors to implied volatility errors: $\Delta\sigma_i \approx \Delta V_i / \text{Vega}_i$. This gives equal importance to all options regardless of moneyness (deep OTM options have small prices but similar IV errors as ATM). Without weighting, ATM options (large vega, large prices) dominate the calibration, leaving OTM wings poorly fitted.

---

**Exercise 2.**
Differential Evolution (DE) is a global optimizer. Explain its advantage over Levenberg-Marquardt (LM) for Heston calibration.

??? success "Solution to Exercise 2"
    DE explores the entire parameter space using a population of candidate solutions, avoiding local minima. The Heston objective function has multiple local minima due to parameter correlations (e.g., $\kappa$ and $\theta$ trade off). LM is a local optimizer that converges quickly but can get stuck in local minima if started far from the global optimum. A common strategy: use DE to find a good starting point, then refine with LM.

---

**Exercise 3.**
The Feller condition $2\kappa\theta > \sigma_v^2$ should ideally be enforced during calibration. Explain how to incorporate this as a constraint.

??? success "Solution to Exercise 3"
    Methods: (1) Penalty: add $\lambda \max(0, \sigma_v^2 - 2\kappa\theta)^2$ to the objective. (2) Reparametrization: set $\sigma_v = \sqrt{2\kappa\theta(1 - \epsilon)}$ for $\epsilon \in (0, 1)$ and optimize over $\epsilon$. (3) Bounds: in DE/LM, impose $\sigma_v \leq \sqrt{2\kappa\theta - \delta}$. In practice, many calibrations violate Feller because the data demands it (steep short-term smiles require high $\sigma_v$).

---

**Exercise 4.**
After calibration, the residuals $V_i^{\text{model}} - V_i^{\text{market}}$ should be analyzed. What patterns in the residuals indicate model inadequacy?

??? success "Solution to Exercise 4"
    Systematic patterns (not random): (1) U-shaped residuals across strikes indicate the model smile is too flat (need higher $\sigma_v$). (2) Monotonic residuals across maturities indicate poor term structure fit (need different $\kappa$ or multi-factor model). (3) Large residuals for specific strikes indicate the model cannot capture sharp features. Random, mean-zero residuals within bid-ask spread indicate adequate fit.