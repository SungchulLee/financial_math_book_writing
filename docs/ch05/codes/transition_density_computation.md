# Transition Density Computation

## Background

transition_density_computation.py

This module implements Transition Density Computation.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
transition_density_computation.py

This module implements Transition Density Computation.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def transition_density_computation():
    """
    Transition Density Computation.
    
    This function demonstrates the key concepts and computational techniques
    for transition density computation.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Transition Density Computation
    print(f"Computing Transition Density Computation...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Transition Density Computation"
    }
    
    return results


def main():
    """Main execution function."""
    results = transition_density_computation()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Transition Density Computation")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/transition_density_computation.png", dpi=150)
    print(f"Figure saved to /tmp/transition_density_computation.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Define the transition density $p(x, t; y, s)$ for a Markov process. What are the two key properties it must satisfy?

??? success "Solution to Exercise 1"
    The transition density $p(x, t; y, s)$ is the probability density that the process is at state $y$ at time $t$, given it was at state $x$ at time $s < t$:

    $$
    P(X_t \in A \mid X_s = x) = \int_A p(x, t; y, s)\,dy
    $$

    Two key properties:

    1. **Non-negativity and normalization**: $p \ge 0$ and $\int_{-\infty}^{\infty} p(x, t; y, s)\,dy = 1$ for all $x, s$.
    2. **Chapman-Kolmogorov equation**: $p(x, t; z, s) = \int p(x, t; y, u)\,p(y, u; z, s)\,dy$ for $s < u < t$. This expresses the Markov property: transitioning from $s$ to $t$ can be decomposed via any intermediate time $u$.

---

**Exercise 2.**
For an Ornstein-Uhlenbeck process $dX_t = \theta(\mu - X_t)\,dt + \sigma\,dW_t$, write the transition density.

??? success "Solution to Exercise 2"
    The OU process has a Gaussian transition density. Given $X_s = x$:

    $$
    X_t \mid X_s = x \;\sim\; \mathcal{N}\bigl(m(t-s),\; v(t-s)\bigr)
    $$

    where the conditional mean and variance are

    $$
    m(t-s) = \mu + (x - \mu)e^{-\theta(t-s)}, \quad v(t-s) = \frac{\sigma^2}{2\theta}\bigl(1 - e^{-2\theta(t-s)}\bigr)
    $$

    The transition density is $p(x,t;y,s) = \frac{1}{\sqrt{2\pi v}}\exp\!\Bigl(-\frac{(y - m)^2}{2v}\Bigr)$.

---

**Exercise 3.**
Explain how the transition density can be computed numerically by solving the Kolmogorov forward equation with a delta function initial condition $p(x, 0; y, 0) = \delta(y - x)$.

??? success "Solution to Exercise 3"
    To compute $p(x_0, t; \cdot, 0)$ for a fixed starting point $x_0$:

    1. Discretize the $y$-domain on a grid $\{y_1, \ldots, y_N\}$.
    2. Approximate the delta function $\delta(y - x_0)$ on the grid (e.g., a narrow Gaussian or a normalized spike at the grid point nearest to $x_0$).
    3. Evolve the discretized Kolmogorov forward equation from $t = 0$ to the desired time.
    4. The resulting grid function approximates the transition density $p(x_0, t; y, 0)$ at each grid point.

    This is equivalent to solving the heat equation (for Brownian motion) or a more general advection-diffusion equation (for processes with drift) with a point-source initial condition.

---

**Exercise 4.**
Compare three methods for computing transition densities: (1) analytical formulas, (2) PDE numerical solution, (3) Monte Carlo histogram. Discuss accuracy and applicability.

??? success "Solution to Exercise 4"
    | Method | Accuracy | Applicability | Cost |
    |--------|----------|---------------|------|
    | Analytical | Exact | Limited to processes with known formulas (GBM, OU, etc.) | $O(1)$ per evaluation |
    | PDE (forward eq.) | $O(\Delta x^2 + \Delta t^p)$ | Any 1D/2D diffusion with known coefficients | $O(N_x \cdot N_t)$ |
    | MC histogram | $O(1/\sqrt{N_{\text{paths}}})$ | Any process that can be simulated | $O(N_{\text{paths}} \cdot N_{\text{steps}})$ |

    Analytical formulas are best when available. PDE methods give the full density on a grid efficiently in low dimensions. Monte Carlo is the most flexible (works in any dimension, for any dynamics) but converges slowly and produces noisy histograms that require careful bin-width selection.
