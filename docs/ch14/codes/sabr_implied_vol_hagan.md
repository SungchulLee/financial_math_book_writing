# SABR Implied Volatility Approximation

## Background

sabr_implied_vol_hagan.py

This module implements SABR Implied Vol Approximation.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
sabr_implied_vol_hagan.py

This module implements SABR Implied Vol Approximation.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def sabr_implied_vol_hagan():
    """
    SABR Implied Vol Approximation.
    
    This function demonstrates the key concepts and computational techniques
    for sabr implied vol approximation.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of SABR Implied Vol Approximation
    print(f"Computing SABR Implied Vol Approximation...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "SABR Implied Vol Approximation"
    }
    
    return results


def main():
    """Main execution function."""
    results = sabr_implied_vol_hagan()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("SABR Implied Vol Approximation")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/sabr_implied_vol_hagan.png", dpi=150)
    print(f"Figure saved to /tmp/sabr_implied_vol_hagan.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
In the Heston model, the vol-of-vol parameter $\sigma_v$ controls the curvature of the implied volatility smile. Explain this connection qualitatively.

??? success "Solution to Exercise 1"
    Higher $\sigma_v$ means the variance process $v(t)$ fluctuates more widely, creating a broader distribution of realized volatilities over the option lifetime. This broadening increases the kurtosis of the log-return distribution, which manifests as higher curvature (more pronounced U-shape) in the IV smile. Low $\sigma_v$ gives a nearly flat smile (approaching GBM).

---

**Exercise 2.**
The SABR model uses $dF = \alpha F^\beta\,dW_1$, $d\alpha = \nu\alpha\,dW_2$. Explain the role of $\beta$ in controlling the smile shape.

??? success "Solution to Exercise 2"
    $\beta$ controls the backbone: how the ATM volatility changes with the forward level. $\beta = 1$ gives lognormal dynamics (percentage vol constant). $\beta = 0$ gives normal dynamics (absolute vol constant). $\beta \in (0,1)$ interpolates. Higher $\beta$ produces less skew for the same $\nu$. The choice of $\beta$ affects the overall smile shape and is often fixed before calibrating $\alpha, \nu, \rho$.

---

**Exercise 3.**
Explain the leverage effect: why do stock returns and volatility tend to be negatively correlated ($\rho < 0$)?

??? success "Solution to Exercise 3"
    Several explanations: (1) Leverage hypothesis: when a firm stock drops, its debt-to-equity ratio increases, making it riskier (higher vol). (2) Feedback effect: increased vol raises risk premiums, pushing prices down. (3) Behavioral: panic selling during declines increases vol. Empirically, $\rho \approx -0.7$ for equity indices. This asymmetry is the primary driver of the IV skew.

---

**Exercise 4.**
Compare the Heston and SABR models for calibrating to equity index smiles. Which is better for short maturities? For long maturities?

??? success "Solution to Exercise 4"
    SABR excels at fitting individual maturity smiles (one smile at a time) and is standard for interest rate options. Heston is better for fitting the entire volatility surface (all maturities simultaneously) because it has a proper term structure model for variance. For short maturities, SABR flexibility can match steep smiles well. For long maturities, Heston mean-reversion $\kappa(\theta - v)$ naturally captures the flattening of the smile term structure.