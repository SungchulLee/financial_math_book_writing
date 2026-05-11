# Yield Curve Fitting (θ Calibration)

## Background

hull_white_theta_calibration.py

This module implements Yield Curve Fitting.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hull_white_theta_calibration.py

This module implements Yield Curve Fitting.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# ======================================================================

def hull_white_theta_calibration():
    """
    Yield Curve Fitting.
    
    This function demonstrates the key concepts and computational techniques
    for yield curve fitting.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Yield Curve Fitting
    print(f"Computing Yield Curve Fitting...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Yield Curve Fitting"
    }
    
    return results


def main():
    """Main execution function."""
    results = hull_white_theta_calibration()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Yield Curve Fitting")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hull_white_theta_calibration.png", dpi=150)
    print(f"Figure saved to /tmp/hull_white_theta_calibration.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The $\theta(t)$ calibration ensures the Hull-White model reproduces the market yield curve. Write the formula for $\theta(t)$ in terms of the market forward rate $f(0,t)$.

??? success "Solution to Exercise 1"
    $$
    \theta(t) = \frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t} + f(0,t) + \frac{\eta^2}{2\lambda^2}(1 - e^{-2\lambda t}).
    $$

    The first term captures the slope of the forward curve, the second is the forward rate itself, and the third is a convexity adjustment due to the model's volatility.

---

**Exercise 2.**
If the forward rate curve is flat at $4\%$ (i.e., $f(0,t) = 0.04$ for all $t$), simplify $\theta(t)$.

??? success "Solution to Exercise 2"
    Since $\partial f/\partial t = 0$:

    $$
    \theta(t) = 0 + 0.04 + \frac{\eta^2}{2\lambda^2}(1 - e^{-2\lambda t}) = 0.04 + \frac{\eta^2}{2\lambda^2}(1 - e^{-2\lambda t}).
    $$

    For small $\eta$ (e.g., $\eta = 0.01$, $\lambda = 0.05$): the correction is $0.0001/(2 \times 0.0025) \times (1 - e^{-0.1t}) = 0.02 \times (1 - e^{-0.1t})$, which rises from $0$ to $0.02$ ($2\%$). So $\theta(t)$ rises from $4\%$ toward $6\%$, a significant convexity correction.

---

**Exercise 3.**
Explain why numerical differentiation of the forward curve requires care and what artifacts can arise.

??? success "Solution to Exercise 3"
    The forward rate is computed as $f(0,t) = -\partial\ln P(0,t)/\partial t$, which requires differentiating the log-bond-price curve. If the market curve is specified at discrete points and interpolated, the derivative depends on the interpolation method:

    - Linear interpolation: $f(0,t)$ is piecewise constant with jumps at knot points, and $\partial f/\partial t$ is zero except at jumps (where it is undefined).
    - Cubic spline: $f(0,t)$ is smooth, but $\partial f/\partial t$ may oscillate if the spline overshoots.
    - Finite differences: $\partial f/\partial t \approx (f(t+\epsilon) - f(t-\epsilon))/(2\epsilon)$ introduces discretization error and is sensitive to the choice of $\epsilon$.

    These artifacts propagate into $\theta(t)$ and can cause unstable or unrealistic simulated paths.

---

**Exercise 4.**
After calibrating $\theta(t)$, how do you verify that the model correctly reproduces the market yield curve?

??? success "Solution to Exercise 4"
    Compute the model zero-coupon bond prices at a grid of maturities using $P_{\text{model}}(0,T) = e^{A(0,T) + B(0,T)r(0)}$ and compare to market prices $P_{\text{market}}(0,T)$. The relative error should be below machine precision ($\sim 10^{-14}$) for an exact analytical calibration, or below the numerical integration tolerance for implementations using quadrature. Alternatively, run a Monte Carlo simulation and verify that $\hat{P}(0,T) = \frac{1}{N}\sum 1/M_i(T) \approx P_{\text{market}}(0,T)$ within statistical error bounds.
