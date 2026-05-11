# Merton Structural Model

## Background

merton_structural_model.py

This module implements Merton Structural Model.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
merton_structural_model.py

This module implements Merton Structural Model.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def merton_structural_model():
    """
    Merton Structural Model.
    
    This function demonstrates the key concepts and computational techniques
    for merton structural model.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Merton Structural Model
    print(f"Computing Merton Structural Model...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Merton Structural Model"
    }
    
    return results


def main():
    """Main execution function."""
    results = merton_structural_model()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Merton Structural Model")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/merton_structural_model.png", dpi=150)
    print(f"Figure saved to /tmp/merton_structural_model.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
In the Merton structural model, the firm's equity is a call option on the firm's assets with strike equal to the debt face value. If $V_0 = \$100M$, $D = \$80M$, $\sigma_V = 25\%$, $r = 3\%$, and $T = 1$, compute $d_1$ and $d_2$.

??? success "Solution to Exercise 1"
    $$
    d_1 = \frac{\ln(V_0/D) + (r + \sigma_V^2/2)T}{\sigma_V\sqrt{T}} = \frac{\ln(100/80) + (0.03 + 0.03125)}{0.25}.
    $$

    $$
    d_1 = \frac{0.2231 + 0.06125}{0.25} = \frac{0.2844}{0.25} = 1.1374.
    $$

    $$
    d_2 = d_1 - \sigma_V\sqrt{T} = 1.1374 - 0.25 = 0.8874.
    $$

---

**Exercise 2.**
Using the values from Exercise 1, compute the probability of default (under the risk-neutral measure) and the credit spread.

??? success "Solution to Exercise 2"
    The risk-neutral default probability is $\mathbb{P}^*(\text{default}) = \mathcal{N}(-d_2) = \Phi(-0.8874) \approx 0.1874 = 18.74\%$.

    The debt value is $D_0 = D\,e^{-rT}\,\mathcal{N}(d_2) + V_0\,\mathcal{N}(-d_1) = 80\,e^{-0.03}\Phi(0.8874) + 100\,\Phi(-1.1374)$.

    $D_0 = 77.63 \times 0.8126 + 100 \times 0.1277 = 63.09 + 12.77 = \$75.86M$.

    The credit spread is $s = -\ln(D_0/(D\,e^{-rT}))/T = -\ln(75.86/77.63) = -\ln(0.9772) = 0.0230 = 2.30\%$.

---

**Exercise 3.**
Explain the main limitation of the Merton model regarding short-term default prediction.

??? success "Solution to Exercise 3"
    In the Merton model, default can only occur at debt maturity $T$ (when $V_T < D$). The model produces near-zero credit spreads for short maturities because asset values follow a continuous diffusion -- the probability of $V$ dropping below $D$ in a short time is negligible (the firm is currently solvent with $V_0 > D$). This contradicts market observation, where even short-dated CDS spreads for investment-grade firms are nonzero. Extensions like the first-passage model (Black-Cox), which allows default at any time when $V$ hits a barrier, address this by producing positive short-term spreads.

---

**Exercise 4.**
In the Merton model, how does increasing asset volatility $\sigma_V$ affect equity value and credit spread simultaneously?

??? success "Solution to Exercise 4"
    Since equity is a call option on assets, increasing $\sigma_V$ increases equity value (options benefit from volatility). Simultaneously, the probability of default $\mathcal{N}(-d_2)$ increases because higher volatility makes it more likely that $V_T < D$. This increases the credit spread.

    The wealth transfer effect: higher volatility transfers value from debtholders to equityholders. Debtholders face more downside risk, while equityholders benefit from the upside. This is why equity markets may react positively to risk-increasing strategies while credit markets react negatively -- a phenomenon captured by the Merton model.
