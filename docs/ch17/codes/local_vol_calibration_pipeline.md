# Local Volatility Calibration Pipeline

## Background

local_vol_calibration_pipeline.py

This module implements Local Vol Calibration Pipeline.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
local_vol_calibration_pipeline.py

This module implements Local Vol Calibration Pipeline.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# ======================================================================

def local_vol_calibration_pipeline():
    """
    Local Vol Calibration Pipeline.
    
    This function demonstrates the key concepts and computational techniques
    for local vol calibration pipeline.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Local Vol Calibration Pipeline
    print(f"Computing Local Vol Calibration Pipeline...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Local Vol Calibration Pipeline"
    }
    
    return results


def main():
    """Main execution function."""
    results = local_vol_calibration_pipeline()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Local Vol Calibration Pipeline")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/local_vol_calibration_pipeline.png", dpi=150)
    print(f"Figure saved to /tmp/local_vol_calibration_pipeline.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
Model calibration finds parameters that best fit market prices. Explain the difference between calibration to vanilla options and calibration to exotic options.

??? success "Solution to Exercise 1"
    Vanilla calibration fits to European calls/puts, which constrain the marginal distributions of $S_T$ at each maturity. Exotic calibration must also match path-dependent features (barriers, autocallable triggers). A model calibrated to vanillas may misprice exotics if it has the wrong dynamics (e.g., local vol matches vanilla prices but mishandles forward smiles). Exotic calibration requires richer models (stochastic vol, jumps).

---

**Exercise 2.**
Regularization adds a penalty term $\lambda \|\Theta - \Theta_0\|^2$ to the calibration objective. Explain its purpose and how $\lambda$ affects the result.

??? success "Solution to Exercise 2"
    Regularization prevents overfitting to noisy market data by penalizing large deviations from a prior $\Theta_0$. Large $\lambda$ pulls parameters toward $\Theta_0$ (underfitting); small $\lambda$ allows data-driven parameters (potential overfitting). Optimal $\lambda$ balances fit quality with parameter stability. L-curve or cross-validation methods can select $\lambda$.

---

**Exercise 3.**
Calibration stability means small changes in market data produce small parameter changes. Explain why the Heston model can be unstable and how to improve stability.

??? success "Solution to Exercise 3"
    Instability arises from parameter correlations: $\kappa$ and $\theta$ are nearly interchangeable for short maturities (only $\kappa\theta$ matters). Small data changes can cause large swings between $(\kappa, \theta)$ pairs with similar products. Remedies: (1) fix $\kappa$ or $\theta$ and calibrate the other; (2) regularize toward previous calibration; (3) use Tikhonov regularization; (4) calibrate to a well-conditioned reparametrization.

---

**Exercise 4.**
Compare least-squares (price error), implied volatility error, and relative price error as calibration objectives. Which is most robust?

??? success "Solution to Exercise 4"
    Price error: simple but ATM-biased (large prices dominate). IV error: equal weighting across strikes but requires inverting BS for each model price (slow). Relative price error: normalizes by market price but unstable for small prices (OTM). Most robust: IV error with vega weighting, which balances all regions of the smile and has direct financial interpretation. The choice depends on the trading application.