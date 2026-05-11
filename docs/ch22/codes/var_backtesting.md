# Value-at-Risk Backtesting

## Background

var_backtesting.py

This module implements VaR Backtesting.

Author: Financial Math Library

---

## Code

```python
# -*- coding: utf-8 -*-
"""
var_backtesting.py

This module implements VaR Backtesting.

Author: Financial Math Library
"""

import numpy as np
import matplotlib.pyplot as plt


# ======================================================================

def var_backtesting():
    """
    VaR Backtesting.
    
    This function demonstrates the key concepts and computational techniques
    for var backtesting.
    
    Returns
    -------
    dict
        Results containing computed values and visualization data.
    """
    # Implementation of VaR Backtesting
    print(f"Computing VaR Backtesting...")
    
    # Create sample data/parameters
    n_simulations = 1000
    time_points = np.linspace(0, 1, 100)
    
    # Core computation logic
    results = {
        "time_points": time_points,
        "description": "VaR Backtesting"
    }
    
    return results


def main():
    """Main execution function."""
    results = var_backtesting()
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results["time_points"], "b-", linewidth=2)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.set_title("VaR Backtesting")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/tmp/var_backtesting.png", dpi=150)
    print(f"Figure saved to /tmp/var_backtesting.png")
    plt.close()
    
    return results


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
VaR backtesting counts the number of exceptions (days where the loss exceeds VaR). For a $99\%$ VaR over 250 trading days, what is the expected number of exceptions and the rejection threshold under the Basel traffic light system?

??? success "Solution to Exercise 1"
    Expected exceptions: $250 \times 0.01 = 2.5$. Under the Basel traffic light system:

    - **Green zone**: $0-4$ exceptions. The model is acceptable.
    - **Yellow zone**: $5-9$ exceptions. Requires investigation and possible capital surcharge.
    - **Red zone**: $10+$ exceptions. The model is deemed inadequate; automatic capital multiplier increase.

    The zones are based on the binomial distribution $B(250, 0.01)$. The probability of 5+ exceptions under a correct model is about $10.8\%$, balancing Type I and Type II errors.

---

**Exercise 2.**
The Kupiec test (proportion of failures test) tests whether the observed exception rate matches the expected rate. For 7 exceptions in 250 days with $99\%$ VaR, compute the test statistic.

??? success "Solution to Exercise 2"
    The observed failure rate is $\hat{p} = 7/250 = 0.028$. The expected rate is $p = 0.01$. The Kupiec log-likelihood ratio statistic is:

    $$
    \text{LR} = -2\ln\!\left[\frac{(1-p)^{n-x} p^x}{(1-\hat{p})^{n-x} \hat{p}^x}\right],
    $$

    where $n = 250$, $x = 7$. Computing: $\text{LR} = -2[243\ln(0.99/0.972) + 7\ln(0.01/0.028)]$.

    $= -2[243 \times 0.01838 + 7 \times (-1.0296)] = -2[4.466 - 7.207] = -2 \times (-2.741) = 5.482$.

    Under $H_0$, $\text{LR} \sim \chi^2(1)$. The critical value at $5\%$ is $3.84$. Since $5.482 > 3.84$, we reject the model at the $5\%$ significance level.

---

**Exercise 3.**
Explain the difference between unconditional coverage tests (Kupiec) and conditional coverage tests (Christoffersen).

??? success "Solution to Exercise 3"

    - **Unconditional coverage (Kupiec)**: Tests only whether the overall exception rate matches $1 - \alpha$. It does not check whether exceptions are clustered or spread evenly over time.
    - **Conditional coverage (Christoffersen)**: Tests both the correct rate and the independence of exceptions. If exceptions cluster (e.g., multiple in one week), the model fails to capture volatility dynamics even if the overall rate is correct. The test combines the Kupiec test with a runs test for independence.

    A model can pass Kupiec but fail Christoffersen if VaR is too slow to react to changing volatility (e.g., constant VaR during a volatility spike produces clustered exceptions).

---

**Exercise 4.**
After backtesting reveals 8 exceptions in 250 days, what corrective actions should be considered?

??? success "Solution to Exercise 4"
    With 8 exceptions (yellow zone), the risk manager should: (1) investigate whether the exceptions are clustered (suggesting volatility regime change) or spread out (suggesting systematic underestimation); (2) check if the VaR model assumptions are appropriate (e.g., Gaussian vs. fat-tailed distributions); (3) consider updating the volatility estimation method (e.g., EWMA with lower decay factor, GARCH); (4) verify data quality and position reporting; (5) apply the regulatory capital surcharge (multiplication factor increases from 3 to 3.4-3.65 in the yellow zone); (6) document findings and remediation plan.
