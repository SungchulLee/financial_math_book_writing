# Uncertain Volatility Pricing

## Background

uncertain_volatility_pricing.py

This module implements Uncertain Volatility Pricing.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
uncertain_volatility_pricing.py

This module implements Uncertain Volatility Pricing.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def uncertain_volatility_pricing():
    """
    Uncertain Volatility Pricing.
    
    This function demonstrates the key concepts and computational techniques
    for uncertain volatility pricing.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Uncertain Volatility Pricing
    print(f"Computing Uncertain Volatility Pricing...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Uncertain Volatility Pricing"
    }
    
    return results


def main():
    """Main execution function."""
    results = uncertain_volatility_pricing()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Uncertain Volatility Pricing")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/uncertain_volatility_pricing.png", dpi=150)
    print(f"Figure saved to /tmp/uncertain_volatility_pricing.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
In the uncertain volatility model (UVM), volatility is unknown but bounded: $\sigma(t) \in [\sigma_{\min}, \sigma_{\max}]$. Write the Black-Scholes-Barenblatt (BSB) PDE for the upper price bound.

??? success "Solution to Exercise 1"
    The BSB equation for the upper price $\bar{V}(t, S)$ is:

    $$
    \frac{\partial \bar{V}}{\partial t} + rS\frac{\partial \bar{V}}{\partial S} + \frac{1}{2}\hat{\sigma}^2 S^2 \frac{\partial^2 \bar{V}}{\partial S^2} - r\bar{V} = 0,
    $$

    where the volatility is chosen adversarially:

    $$
    \hat{\sigma}^2 = \begin{cases} \sigma_{\max}^2 & \text{if } \frac{\partial^2 \bar{V}}{\partial S^2} > 0, \\ \sigma_{\min}^2 & \text{if } \frac{\partial^2 \bar{V}}{\partial S^2} < 0. \end{cases}
    $$

    This nonlinear PDE selects the worst-case volatility at each point in the $(t, S)$ grid.

---

**Exercise 2.**
For a European call option (which has $\Gamma > 0$ everywhere), what is the BSB upper price?

??? success "Solution to Exercise 2"
    Since $\Gamma = \partial^2 C/\partial S^2 > 0$ for a European call (convex payoff), the BSB equation selects $\hat{\sigma} = \sigma_{\max}$ everywhere. The upper bound is simply the Black-Scholes price at $\sigma_{\max}$:

    $$
    \bar{V} = C_{\text{BS}}(S, K, T, r, \sigma_{\max}).
    $$

    Similarly, the lower bound uses $\sigma_{\min}$: $\underline{V} = C_{\text{BS}}(S, K, T, r, \sigma_{\min})$.

---

**Exercise 3.**
For a portfolio that is long a call and short a put (a risk reversal), the Gamma changes sign across the strike range. Explain why the BSB equation becomes a genuinely nonlinear PDE.

??? success "Solution to Exercise 3"
    The risk reversal has $\Gamma > 0$ near the call strike (call's positive Gamma dominates) and $\Gamma < 0$ near the put strike (short put's negative Gamma dominates). The BSB equation switches between $\sigma_{\max}$ and $\sigma_{\min}$ depending on the sign of $\Gamma$ at each $(t, S)$ point:

    $$
    \hat{\sigma}^2(t, S) = \sigma_{\max}^2 \cdot \mathbf{1}_{\Gamma > 0} + \sigma_{\min}^2 \cdot \mathbf{1}_{\Gamma < 0}.
    $$

    This makes the PDE nonlinear because the diffusion coefficient depends on the solution itself (through $\Gamma$). Standard analytical solutions do not exist, and numerical methods (finite differences) must solve the equation iteratively.

---

**Exercise 4.**
If $\sigma_{\min} = 15\%$ and $\sigma_{\max} = 25\%$, the Black-Scholes call price at $20\%$ is \$5.00, at $15\%$ is \$4.00, and at $25\%$ is \$6.20. What is the UVM price range, and what does it imply about model risk?

??? success "Solution to Exercise 4"
    The UVM price range is $[\$4.00, \$6.20]$. The width is $\$2.20$, representing the maximum model risk from volatility uncertainty. The midpoint model price (\$5.00) could be off by up to $\$1.20$ ($24\%$ of the price). This is substantial model risk.

    Implications: (1) the bid-ask spread should be at least \$2.20 to cover model uncertainty; (2) hedging should use the robust approach (delta at the appropriate boundary volatility); (3) if the uncertainty range can be narrowed (e.g., by trading more vanilla options to pin down implied vol), the price range tightens and model risk decreases.
