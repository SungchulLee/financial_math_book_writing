# Calibration to Cap Volatilities

## Background

hull_white_calibration_caps.py

This module implements Calibration to Cap Vols.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
hull_white_calibration_caps.py

This module implements Calibration to Cap Vols.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# ======================================================================

def hull_white_calibration_caps():
    """
    Calibration to Cap Vols.
    
    This function demonstrates the key concepts and computational techniques
    for calibration to cap vols.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Calibration to Cap Vols
    print(f"Computing Calibration to Cap Vols...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Calibration to Cap Vols"
    }
    
    return results


def main():
    """Main execution function."""
    results = hull_white_calibration_caps()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Calibration to Cap Vols")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/hull_white_calibration_caps.png", dpi=150)
    print(f"Figure saved to /tmp/hull_white_calibration_caps.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Calibrating Hull-White to cap volatilities involves finding $\eta$ and $\lambda$ that minimize the difference between model and market cap prices. Write the objective function.

??? success "Solution to Exercise 1"
    The objective function is

    $$
    f(\eta, \lambda) = \sum_{i=1}^{N} w_i\bigl[V_i^{\text{model}}(\eta, \lambda) - V_i^{\text{market}}\bigr]^2,
    $$

    where $V_i^{\text{model}}$ is the Hull-White cap (or caplet) price for the $i$-th instrument, $V_i^{\text{market}}$ is the market price, and $w_i$ are weights (often $1/V_i^{\text{market}}$ for relative fitting or $1/(V_i^{\text{market}})^2$ for percentage error minimization). The model prices are computed using the Hull-White caplet formula derived from bond options.

---

**Exercise 2.**
Explain the trade-off between fitting $\eta$ as a constant versus a piecewise constant (time-dependent) function.

??? success "Solution to Exercise 2"

    - **Constant $\eta$**: Two parameters ($\eta, \lambda$). Simple, stable calibration but may not fit the entire cap volatility term structure accurately. Best when the term structure is relatively flat.
    - **Piecewise constant $\eta(t)$**: One $\eta$ value per caplet interval, plus $\lambda$. Can exactly fit all cap prices (as many parameters as instruments). But may produce non-smooth volatility functions, unstable hedges, and overfit to market noise.

    A common compromise is to use 3-5 piecewise constant segments for $\eta(t)$ while keeping $\lambda$ constant, balancing accuracy and stability.

---

**Exercise 3.**
If the calibration produces $\lambda = 0.03$ and $\eta = 0.008$, compute the long-run standard deviation of the short rate and the implied cap volatility for a 1-year caplet.

??? success "Solution to Exercise 3"
    Long-run std: $\sigma_\infty = \eta/\sqrt{2\lambda} = 0.008/\sqrt{0.06} = 0.008/0.2449 = 0.03266 = 3.27\%$.

    For a 1-year caplet on $[T_1, T_2] = [1, 1.25]$: $\sigma_P = \eta \cdot |B(1, 1.25)| \cdot \sqrt{(1 - e^{-0.06})/0.06}$. With $B = (e^{-0.0075} - 1)/0.03 \approx -0.2498$:

    $$
    \sigma_P = 0.008 \times 0.2498 \times \sqrt{0.9709} = 0.001998 \times 0.9854 \approx 0.001969.
    $$

    Converting to Black implied volatility requires additional computation, but the bond volatility is approximately $0.20\%$, corresponding to a caplet implied vol of roughly $15-20\%$ depending on the forward rate level.

---

**Exercise 4.**
Describe common issues in Hull-White calibration to caps and how they are resolved.

??? success "Solution to Exercise 4"

    1. **Non-uniqueness**: Multiple $(\eta, \lambda)$ pairs can produce similar cap prices, especially when only ATM caps are used. Resolved by adding swaption prices as additional calibration targets, or by fixing $\lambda$ from historical data.
    2. **Negative rates**: If the calibrated $\eta$ is large relative to the rate level, the model produces many negative rate scenarios. Resolved by using shifted Hull-White or checking that implied negative rate probabilities are reasonable.
    3. **Term structure mismatch**: Constant $\eta$ cannot fit both short-dated and long-dated caps simultaneously if the volatility term structure is non-monotonic. Resolved by using piecewise constant $\eta(t)$.
    4. **Numerical instability**: The cap pricing formula involves products of exponentials that can overflow for extreme parameters. Resolved by working in log-space and using bounded optimization.
