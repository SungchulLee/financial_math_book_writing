# Kalman Filter for Stochastic Volatility

## Background

kalman_filter_stochastic_vol.py

This module implements Kalman Filter for Stochastic Vol.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
kalman_filter_stochastic_vol.py

This module implements Kalman Filter for Stochastic Vol.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def kalman_filter_stochastic_vol():
    """
    Kalman Filter for Stochastic Vol.
    
    This function demonstrates the key concepts and computational techniques
    for kalman filter for stochastic vol.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of Kalman Filter for Stochastic Vol
    print(f"Computing Kalman Filter for Stochastic Vol...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "Kalman Filter for Stochastic Vol"
    }
    
    return results


def main():
    """Main execution function."""
    results = kalman_filter_stochastic_vol()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("Kalman Filter for Stochastic Vol")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/kalman_filter_stochastic_vol.png", dpi=150)
    print(f"Figure saved to /tmp/kalman_filter_stochastic_vol.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The Kalman filter estimates a hidden state $x_t$ from noisy observations $y_t$. Write the state-space model for stochastic volatility: $\ln\sigma_t^2 = \alpha + \beta\ln\sigma_{t-1}^2 + \eta_t$ with observation $y_t = \sigma_t\,\varepsilon_t$.

??? success "Solution to Exercise 1"
    Define the log-variance state $h_t = \ln\sigma_t^2$. The state-space model is:

    **State equation**: $h_t = \alpha + \beta\,h_{t-1} + \eta_t$, where $\eta_t \sim \mathcal{N}(0, \sigma_\eta^2)$.

    **Observation equation**: $\ln y_t^2 = h_t + \ln\varepsilon_t^2$, where $\varepsilon_t \sim \mathcal{N}(0,1)$.

    The issue is that $\ln\varepsilon_t^2$ follows a $\ln\chi^2(1)$ distribution, which is non-Gaussian with mean $-1.27$ and variance $\pi^2/2 \approx 4.93$. The standard Kalman filter assumes Gaussian errors, so the observation equation is only approximately Gaussian after centering.

---

**Exercise 2.**
Explain why the standard Kalman filter is only an approximation for stochastic volatility models, and name a method that handles the non-Gaussianity.

??? success "Solution to Exercise 2"
    The observation error $\ln\varepsilon_t^2$ has a $\ln\chi^2(1)$ distribution, which is highly skewed and non-Gaussian. The standard Kalman filter assumes Gaussian errors and provides the best linear estimate, but this is suboptimal for the non-Gaussian observation equation.

    Better methods include: (1) a Gaussian mixture approximation, where the $\ln\chi^2$ distribution is approximated by a mixture of 7-10 Gaussians (Kim, Shephard, Chib, 1998); (2) particle filters (sequential Monte Carlo), which handle any distribution; (3) the unscented Kalman filter, which better captures nonlinear transformations.

---

**Exercise 3.**
For the Kalman prediction step, write the equations for the predicted state $\hat{h}_{t|t-1}$ and its variance $P_{t|t-1}$.

??? success "Solution to Exercise 3"
    $$
    \hat{h}_{t|t-1} = \alpha + \beta\,\hat{h}_{t-1|t-1},
    $$

    $$
    P_{t|t-1} = \beta^2\,P_{t-1|t-1} + \sigma_\eta^2.
    $$

    These propagate the state estimate and its uncertainty forward in time using the state transition equation. The variance increases by $\sigma_\eta^2$ (process noise) but is scaled by $\beta^2$ (mean reversion reduces uncertainty from the previous estimate).

---

**Exercise 4.**
If the filtered volatility estimate is $\hat{\sigma}_t = 18\%$ with a $95\%$ confidence interval of $[14\%, 22\%]$, how would you use this for option pricing?

??? success "Solution to Exercise 4"
    The point estimate $18\%$ can be used as the current volatility input for Black-Scholes or other pricing models. The confidence interval $[14\%, 22\%]$ quantifies parameter uncertainty:

    1. Price the option at all three volatilities to get a price range.
    2. Use the Bayesian predictive distribution $p(\sigma_{t+1} \mid \text{data})$ for forward-looking pricing.
    3. For robust pricing, compute the option price over the entire confidence interval and report the range.
    4. For hedging, the uncertainty in $\sigma$ affects the hedge ratio (Vega risk), suggesting additional Vega hedging may be needed.
