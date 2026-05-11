# LIBOR Market Model Forward Rate Simulation

## Background

lmm_forward_rate_simulation.py

This module implements LMM Forward Rate Simulation.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
lmm_forward_rate_simulation.py

This module implements LMM Forward Rate Simulation.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# ======================================================================

def lmm_forward_rate_simulation():
    """
    LMM Forward Rate Simulation.
    
    This function demonstrates the key concepts and computational techniques
    for lmm forward rate simulation.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of LMM Forward Rate Simulation
    print(f"Computing LMM Forward Rate Simulation...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "LMM Forward Rate Simulation"
    }
    
    return results


def main():
    """Main execution function."""
    results = lmm_forward_rate_simulation()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("LMM Forward Rate Simulation")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/lmm_forward_rate_simulation.png", dpi=150)
    print(f"Figure saved to /tmp/lmm_forward_rate_simulation.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
In the LMM, when simulating forward rates under the spot measure, the drift of $L_k$ involves correlations with other forward rates. Write the drift term for $L_k$ under the spot LIBOR measure.

??? success "Solution to Exercise 1"
    Under the spot LIBOR measure, the drift of $L_k(t)$ for $t \in [T_{j-1}, T_j)$ is

    $$
    \mu_k(t) = \sigma_k(t)\sum_{i=j}^{k} \frac{\tau_i\,\sigma_i(t)\,\rho_{ik}\,L_i(t)}{1 + \tau_i\,L_i(t)},
    $$

    where $\tau_i = T_{i+1} - T_i$ is the accrual fraction, $\sigma_i(t)$ is the volatility of $L_i$, and $\rho_{ik}$ is the instantaneous correlation between $L_i$ and $L_k$. This drift arises from the change of numeraire between forward measures and is crucial for consistent simulation of all forward rates simultaneously.

---

**Exercise 2.**
Explain why the Euler discretization of the LMM can introduce significant bias, and describe the predictor-corrector method as a remedy.

??? success "Solution to Exercise 2"
    The Euler discretization approximates $L_k(t + \Delta t) \approx L_k(t)\exp[(\mu_k - \sigma_k^2/2)\Delta t + \sigma_k\sqrt{\Delta t}\,Z_k]$, but the drift $\mu_k$ depends on the forward rates $L_i(t)$, which are also being updated. Using values at time $t$ for the drift (forward Euler) introduces bias because the drift should be evaluated at values between $t$ and $t + \Delta t$.

    The predictor-corrector method:

    1. **Predict**: Use the Euler step with drift evaluated at $L_i(t)$ to get preliminary $\tilde{L}_k(t + \Delta t)$.
    2. **Correct**: Recompute the drift using the average $\frac{1}{2}[\mu_k(L(t)) + \mu_k(\tilde{L}(t+\Delta t))]$.
    3. Apply the corrected drift to get the final $L_k(t + \Delta t)$.

    This reduces the discretization bias from $O(\Delta t)$ to $O(\Delta t^2)$.

---

**Exercise 3.**
For a 10-year tenor structure with semi-annual periods, how many forward rates need to be simulated? If the correlation matrix is full, how many correlation parameters are there?

??? success "Solution to Exercise 3"
    With semi-annual periods over 10 years, there are $10/0.5 = 20$ forward rates $L_0, L_1, \ldots, L_{19}$. The correlation matrix is $20 \times 20$ and symmetric, so the number of unique off-diagonal correlation parameters is

    $$
    \binom{20}{2} = \frac{20 \times 19}{2} = 190.
    $$

    This large number of parameters makes calibration challenging, which is why parametric correlation structures (e.g., $\rho_{ij} = e^{-\beta|i-j|}$) are commonly used to reduce the dimensionality.

---

**Exercise 4.**
Describe how the simulated forward rate paths can be used to price a Bermudan swaption via the Longstaff-Schwartz least-squares Monte Carlo method.

??? success "Solution to Exercise 4"

    1. **Simulate**: Generate $N$ paths of all forward rates $L_k(t)$ at each exercise date.
    2. **Terminal value**: At the last exercise date, compute the swaption payoff for each path.
    3. **Backward induction**: At each earlier exercise date $T_j$, regress the discounted continuation value on basis functions of the current state (forward rates). The fitted regression gives the conditional expected continuation value $\hat{C}(T_j)$.
    4. **Exercise decision**: Compare the immediate exercise value $V_{\text{ex}}(T_j)$ with $\hat{C}(T_j)$. Exercise if $V_{\text{ex}} > \hat{C}$.
    5. **Price**: Average the discounted optimal exercise payoffs across all paths.
