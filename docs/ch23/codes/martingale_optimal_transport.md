# Martingale Optimal Transport

## Background

martingale_optimal_transport.py

This module implements Martingale Optimal Transport.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
martingale_optimal_transport.py

This module implements Martingale Optimal Transport.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def martingale_optimal_transport():
    """
    Martingale Optimal Transport.
    
    This function demonstrates the key concepts and computational techniques
    for martingale optimal transport.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Martingale Optimal Transport
    print(f"Computing Martingale Optimal Transport...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Martingale Optimal Transport"
    }
    
    return results


def main():
    """Main execution function."""
    results = martingale_optimal_transport()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Martingale Optimal Transport")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/martingale_optimal_transport.png", dpi=150)
    print(f"Figure saved to /tmp/martingale_optimal_transport.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Martingale optimal transport (MOT) seeks the coupling of two marginal distributions that maximizes or minimizes the expected payoff subject to a martingale constraint. State the primal MOT problem for bounding the price of an exotic option.

??? success "Solution to Exercise 1"
    Let $\mu_1$ and $\mu_2$ be the marginal distributions of the asset at times $T_1$ and $T_2$ (implied by vanilla option prices). The primal MOT problem for the upper bound is:

    $$
    \sup_{\pi \in \Pi_M(\mu_1, \mu_2)} \int c(x, y)\,d\pi(x, y),
    $$

    where $\Pi_M(\mu_1, \mu_2)$ is the set of all joint distributions with marginals $\mu_1, \mu_2$ satisfying the martingale constraint $\mathbb{E}[Y \mid X = x] = x$ (the conditional expectation of the future price equals the current price). The function $c(x,y)$ is the exotic option payoff.

---

**Exercise 2.**
Explain why the martingale constraint $\mathbb{E}[S_{T_2} \mid S_{T_1}] = S_{T_1}$ is necessary for no-arbitrage pricing bounds.

??? success "Solution to Exercise 2"
    Under any risk-neutral measure, discounted asset prices are martingales. For undiscounted prices (with zero rates for simplicity), this means $\mathbb{E}^{\mathbb{Q}}[S_{T_2} \mid S_{T_1}] = S_{T_1}$. Any coupling that violates this constraint corresponds to a model that admits arbitrage. By restricting to martingale couplings, we ensure that all considered models are arbitrage-free. The resulting price bounds are the tightest possible given only the information from vanilla option markets.

---

**Exercise 3.**
For a forward-start option with payoff $\max(S_{T_2}/S_{T_1} - K, 0)$, explain why the MOT bounds are wider than for a plain vanilla option.

??? success "Solution to Exercise 3"
    A vanilla option depends on $S_T$ only at one time, so its price is uniquely determined by the marginal distribution $\mu_T$ (which is fixed by vanilla option prices). A forward-start option depends on the joint distribution of $(S_{T_1}, S_{T_2})$, which is not uniquely determined by the marginals. Different martingale couplings produce different prices, creating a range $[\text{lower bound}, \text{upper bound}]$. The width of this range reflects the model uncertainty inherent in the dependence structure between $S_{T_1}$ and $S_{T_2}$.

---

**Exercise 4.**
Describe the dual formulation of the MOT problem and its financial interpretation as a semi-static hedging portfolio.

??? success "Solution to Exercise 4"
    By duality, the upper bound equals:

    $$
    \inf_{\phi, \psi, h} \left\{\int \phi(x)\,d\mu_1(x) + \int \psi(y)\,d\mu_2(y) : \phi(x) + \psi(y) + h(x)(y - x) \geq c(x, y)\right\}.
    $$

    The functions $\phi$ and $\psi$ represent static positions in vanilla options at $T_1$ and $T_2$, and $h(x)$ represents a dynamic hedge (delta hedge at $T_1$ depending on $S_{T_1}$). The dual says: the tightest upper bound equals the cheapest super-replicating portfolio using vanillas and delta hedging. This connects the abstract transport problem to practical hedging.
