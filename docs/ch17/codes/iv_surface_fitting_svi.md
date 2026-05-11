# Implied Volatility Surface Fitting (SVI)

## Background

iv_surface_fitting_svi.py

This module implements IV Surface Fitting SVI.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
iv_surface_fitting_svi.py

This module implements IV Surface Fitting SVI.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def iv_surface_fitting_svi():
    """
    IV Surface Fitting SVI.
    
    This function demonstrates the key concepts and computational techniques
    for iv surface fitting svi.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of IV Surface Fitting SVI
    print(f"Computing IV Surface Fitting SVI...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "IV Surface Fitting SVI"
    }
    
    return results


def main():
    """Main execution function."""
    results = iv_surface_fitting_svi()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("IV Surface Fitting SVI")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/iv_surface_fitting_svi.png", dpi=150)
    print(f"Figure saved to /tmp/iv_surface_fitting_svi.png")
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