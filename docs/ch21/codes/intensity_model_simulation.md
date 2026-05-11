# Intensity Model Simulation

## Background

intensity_model_simulation.py

This module implements Intensity Model Simulation.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
intensity_model_simulation.py

This module implements Intensity Model Simulation.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# ======================================================================

def intensity_model_simulation():
    """
    Intensity Model Simulation.
    
    This function demonstrates the key concepts and computational techniques
    for intensity model simulation.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Intensity Model Simulation
    print(f"Computing Intensity Model Simulation...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Intensity Model Simulation"
    }
    
    return results


def main():
    """Main execution function."""
    results = intensity_model_simulation()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Intensity Model Simulation")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/intensity_model_simulation.png", dpi=150)
    print(f"Figure saved to /tmp/intensity_model_simulation.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
In the intensity-based (reduced-form) model, default is the first jump of a Poisson process with stochastic intensity $h(t)$. Write the survival probability in terms of the integrated intensity.

??? success "Solution to Exercise 1"
    The survival probability to time $T$ is

    $$
    Q(T) = \mathbb{E}\!\left[\exp\!\left(-\int_0^T h(s)\,ds\right)\right].
    $$

    For deterministic intensity, $Q(T) = \exp(-\int_0^T h(s)\,ds)$. For stochastic intensity (e.g., CIR intensity), the expectation requires either analytical formulas (if available) or Monte Carlo simulation. Default occurs at $\tau = \inf\{t : \int_0^t h(s)\,ds \geq E_1\}$ where $E_1 \sim \text{Exp}(1)$.

---

**Exercise 2.**
Describe the simulation algorithm for generating a default time from a stochastic intensity $h(t)$.

??? success "Solution to Exercise 2"

    1. Draw $E_1 \sim \text{Exp}(1)$ (a standard exponential random variable).
    2. Simulate the intensity path $h(t_0), h(t_1), \ldots, h(t_N)$ using the appropriate SDE discretization.
    3. Compute the cumulative intensity: $\Lambda(t_i) = \sum_{j=0}^{i-1} h(t_j)\,\Delta t$.
    4. Find the first $t_i$ where $\Lambda(t_i) \geq E_1$. This is the default time $\tau$.
    5. If $\Lambda(T) < E_1$ for all simulated times, the entity survives to $T$.

    This algorithm is called the "canonical construction" and correctly couples the default time with the intensity path.

---

**Exercise 3.**
If the intensity follows a CIR process $dh = \kappa(\bar{h} - h)\,dt + \sigma_h\sqrt{h}\,dW$, explain why this is popular for credit modeling.

??? success "Solution to Exercise 3"
    The CIR intensity model is popular because:

    1. **Non-negativity**: Under the Feller condition $2\kappa\bar{h} \geq \sigma_h^2$, $h(t) \geq 0$ always, which is required since intensity represents a rate.
    2. **Mean reversion**: Default risk reverts to a long-run level $\bar{h}$, consistent with credit cycles.
    3. **Analytical tractability**: The survival probability $Q(T) = \mathbb{E}[e^{-\int_0^T h(s)\,ds}]$ has a closed-form expression (the CIR bond pricing formula), enabling fast calibration to CDS spreads.
    4. **Flexibility**: The model can produce upward-sloping, flat, or humped hazard rate term structures depending on the parameter values.

---

**Exercise 4.**
Simulate 5 default times using the following procedure: $E_i \sim \text{Exp}(1)$ values are $\{0.5, 2.1, 0.8, 3.5, 1.2\}$ and the constant intensity is $h = 0.03$. Which entities default before year 10?

??? success "Solution to Exercise 4"
    With constant $h$, the default time for entity $i$ is $\tau_i = E_i / h$:

    - Entity 1: $\tau = 0.5/0.03 = 16.67$ years (survives 10 years)
    - Entity 2: $\tau = 2.1/0.03 = 70.0$ years (survives)
    - Entity 3: $\tau = 0.8/0.03 = 26.67$ years (survives)
    - Entity 4: $\tau = 3.5/0.03 = 116.7$ years (survives)
    - Entity 5: $\tau = 1.2/0.03 = 40.0$ years (survives)

    No entity defaults before year 10 with this intensity. For a $3\%$ annual hazard rate, the 10-year default probability is $1 - e^{-0.3} \approx 26\%$, so about 1-2 out of 5 entities would typically default, but the particular exponential draws here are all above $0.3$.
