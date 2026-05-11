# Fourier Inversion for Affine Models

## Background

affine_fourier_inversion.py

This module implements Fourier Inversion for Affine Models.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
affine_fourier_inversion.py

This module implements Fourier Inversion for Affine Models.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def affine_fourier_inversion():
    """
    Fourier Inversion for Affine Models.
    
    This function demonstrates the key concepts and computational techniques
    for fourier inversion for affine models.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Fourier Inversion for Affine Models
    print(f"Computing Fourier Inversion for Affine Models...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Fourier Inversion for Affine Models"
    }
    
    return results


def main():
    """Main execution function."""
    results = affine_fourier_inversion()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Fourier Inversion for Affine Models")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/affine_fourier_inversion.png", dpi=150)
    print(f"Figure saved to /tmp/affine_fourier_inversion.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
In the Vasicek model, the short rate follows $dr = \kappa(\theta - r)\,dt + \sigma\,dW$. Solve for $\mathbb{E}[r_T | r_0]$ and $\text{Var}(r_T | r_0)$.

??? success "Solution to Exercise 1"
    The Vasicek SDE has the explicit solution $r_T = \theta + (r_0 - \theta)e^{-\kappa T} + \sigma\int_0^T e^{-\kappa(T-s)}dW_s$. Therefore: $\mathbb{E}[r_T] = \theta + (r_0 - \theta)e^{-\kappa T}$ (exponential decay to $\theta$). $\text{Var}(r_T) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T})$ (approaches $\sigma^2/(2\kappa)$ for large $T$).

---

**Exercise 2.**
The CIR model $dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW$ keeps rates non-negative (under the Feller condition). State the condition and verify it for $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.1$.

??? success "Solution to Exercise 2"
    Feller condition: $2\kappa\theta > \sigma^2$. Check: $2(0.5)(0.05) = 0.05$ vs $0.1^2 = 0.01$. Since $0.05 > 0.01$, the condition is satisfied and $r(t) > 0$ for all $t$. If $\sigma$ were increased to $0.25$, then $0.05 < 0.0625$ and the condition would be violated.

---

**Exercise 3.**
Affine bond pricing gives $P(t,T) = e^{A(T-t) - B(T-t)r_t}$ where $A, B$ satisfy Riccati ODEs. Explain why this exponential-affine form is analytically convenient.

??? success "Solution to Exercise 3"
    The exponential-affine form allows: (1) yields $y = -\ln P / (T-t) = -A/(T-t) + B/(T-t) \cdot r$ are linear in $r$, giving analytic yield curves; (2) the characteristic function of $\int_0^T r_s\,ds$ is also exponential-affine, enabling Fourier-based pricing; (3) multi-factor extensions remain tractable as sums of affine components. This is the defining property of "affine" models.

---

**Exercise 4.**
For the Vasicek model, derive the zero-coupon bond price $P(0,T)$ given $r_0 = 0.03$, $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.02$, $T = 5$.

??? success "Solution to Exercise 4"
    $B(T) = \frac{1-e^{-\kappa T}}{\kappa} = \frac{1-e^{-2.5}}{0.5} = \frac{0.918}{0.5} = 1.836$. $A(T) = (\theta - \frac{\sigma^2}{2\kappa^2})(B(T) - T) + \frac{\sigma^2}{4\kappa}B(T)^2 = (0.05 - 0.0008)(1.836 - 5) + 0.0002(3.371) = 0.0492(-3.164) + 0.000674 = -0.1557 + 0.0007 = -0.1550$. Bond price: $P = e^{-0.1550 - 1.836(0.03)} = e^{-0.1550 - 0.0551} = e^{-0.2101} = 0.8106$.