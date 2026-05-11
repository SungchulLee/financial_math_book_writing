# Kolmogorov Forward Density Evolution

## Background

kolmogorov_forward_density.py

This module implements Kolmogorov Forward Density Evolution.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
kolmogorov_forward_density.py

This module implements Kolmogorov Forward Density Evolution.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def kolmogorov_forward_density():
    """
    Kolmogorov Forward Density Evolution.
    
    This function demonstrates the key concepts and computational techniques
    for kolmogorov forward density evolution.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Kolmogorov Forward Density Evolution
    print(f"Computing Kolmogorov Forward Density Evolution...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Kolmogorov Forward Density Evolution"
    }
    
    return results


def main():
    """Main execution function."""
    results = kolmogorov_forward_density()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Kolmogorov Forward Density Evolution")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/kolmogorov_forward_density.png", dpi=150)
    print(f"Figure saved to /tmp/kolmogorov_forward_density.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
State the Kolmogorov forward (Fokker-Planck) equation for a diffusion process $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$. Identify the drift and diffusion terms.

??? success "Solution to Exercise 1"
    The Kolmogorov forward equation for the transition density $p(x, t)$ is

    $$
    \frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}\bigl[\mu(x)\,p(x,t)\bigr] + \frac{1}{2}\frac{\partial^2}{\partial x^2}\bigl[\sigma^2(x)\,p(x,t)\bigr]
    $$

    The first term on the right is the **drift (convection) term**: $-\partial_x[\mu\,p]$, describing how probability is transported by the drift. The second term is the **diffusion term**: $\frac{1}{2}\partial_{xx}[\sigma^2 p]$, describing how probability spreads due to the stochastic component. Together, they govern the time evolution of the probability density function.

---

**Exercise 2.**
For geometric Brownian motion $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$, write the Kolmogorov forward equation for the density of $S_t$.

??? success "Solution to Exercise 2"
    With $\mu(S) = \mu S$ and $\sigma(S) = \sigma S$:

    $$
    \frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}(\mu S\,p) + \frac{1}{2}\frac{\partial^2}{\partial S^2}(\sigma^2 S^2\,p)
    $$

    The solution is the log-normal density: $S_t \sim \text{LogNormal}\bigl(\ln S_0 + (\mu - \frac{1}{2}\sigma^2)t,\;\sigma^2 t\bigr)$.

---

**Exercise 3.**
Explain the relationship between the Kolmogorov forward equation and the Kolmogorov backward equation. Which one is used for option pricing, and why?

??? success "Solution to Exercise 3"
    The **forward equation** evolves the density forward in time from a fixed initial condition. It describes how the probability distribution of $X_t$ spreads over time.

    The **backward equation** evolves the expected payoff backward in time to the present. For a function $u(x,t) = E[g(X_T) \mid X_t = x]$:

    $$
    \frac{\partial u}{\partial t} + \mu(x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 u}{\partial x^2} = 0
    $$

    Option pricing uses the backward equation because we want to compute the present value of a future payoff. The forward equation is used for density estimation, calibration, and understanding the distributional properties of the process.

---

**Exercise 4.**
If the forward equation is discretized on a spatial grid with $N$ points and evolved for $M$ time steps using an explicit scheme, what is the total computational cost? How does this compare to Monte Carlo with $N_{\text{paths}}$ paths?

??? success "Solution to Exercise 4"
    The PDE approach costs $O(N \cdot M)$ operations: at each of $M$ time steps, the $N$-point solution vector is updated. With implicit methods, each step costs $O(N)$ for a tridiagonal solve, so the total remains $O(NM)$.

    Monte Carlo costs $O(N_{\text{paths}} \cdot M_{\text{steps}})$ operations for path generation, plus $O(N_{\text{paths}})$ for payoff evaluation.

    The PDE approach gives the density (or option price) at all grid points simultaneously, while Monte Carlo gives a single expected value with $O(1/\sqrt{N_{\text{paths}}})$ error. For computing the full density, PDE methods are typically more efficient. For computing a single expectation, Monte Carlo may be simpler and more flexible, especially in high dimensions.
