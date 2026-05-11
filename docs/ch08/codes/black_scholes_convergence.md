# Convergence (General)

## Background

Black Scholes Convergence

Educational script demonstrating black scholes convergence concepts.

---

## Code

```python
"""
Black Scholes Convergence

Educational script demonstrating black scholes convergence concepts.
"""

# ============================================================================
# black_scholes_CONVERGENCE_ANALYSIS.py
# ============================================================================
import black_scholes as bs
   
# Model parameters


if __name__ == "__main__":
    S0 = 100      # Current stock price
    K = 105       # Strike price
    T = 0.25      # 3 months to expiration
    r = 0.05      # 5% risk-free rate
    sigma = 0.2   # 20% volatility
    q = 0.02      # 2% dividend yield
    mu = 0.1
    
    bs.BlackScholes(S0=S0, K=K, T=T, r=r, sigma=sigma, q=q).plot_convergence(
        option_type='call',
        methods=['explicit', 'implicit', 'cn'],
        grid_points=[50, 100, 200, 400, 800, 1600]
        )
```


## Exercises

**Exercise 1.**
Describe a comprehensive convergence analysis for the BS PDE solver. What should be varied independently?

??? success "Solution to Exercise 1"
    Test spatial and temporal convergence separately: (1) fix $N_t$ large, vary $N_S$, measure error vs $\Delta S$, (2) fix $N_S$ large, vary $N_t$, measure error vs $\Delta t$. Then test joint refinement with $\Delta t \propto \Delta S^2$ (maintaining stability for explicit schemes) or $\Delta t \propto \Delta S$ (for implicit/CN schemes to balance errors).

---

**Exercise 2.**
The BS formula provides the exact reference solution. What if no analytical solution exists (e.g., for stochastic volatility)?

??? success "Solution to Exercise 2"
    Use: (1) a very fine-grid numerical solution as a reference, (2) Richardson extrapolation to estimate the exact value, (3) comparison with Monte Carlo (independent method), (4) convergence of the error ratio $e(h)/e(h/2)$ to determine the order without knowing the exact solution.

---

**Exercise 3.**
The convergence analysis compares multiple schemes (explicit, implicit, CN). What convergence orders do you expect?

??? success "Solution to Exercise 3"
    | Scheme | Time order | Space order |
    |--------|:---:|:---:|
    | Explicit | 1 | 2 |
    | Implicit | 1 | 2 |
    | CN | 2 | 2 |
    | CN-log | 2 | 2 |

    All schemes are second-order in space (centered differences). CN achieves second-order in time via the trapezoidal rule. The log-space transformation does not change the convergence order but may improve the constant.

---

**Exercise 4.**
Explain Richardson extrapolation and how it can improve the effective convergence order.

??? success "Solution to Exercise 4"
    For a method with error $V_h = V_{\text{exact}} + ch^p + O(h^{p+1})$, the Richardson extrapolation $V_R = (2^p V_{h/2} - V_h)/(2^p - 1)$ eliminates the leading error term: $V_R = V_{\text{exact}} + O(h^{p+1})$.

    For CN ($p = 2$): $V_R = (4V_{h/2} - V_h)/3$ gives $O(h^4)$ effective accuracy. This doubles the convergence order at the cost of two solves instead of one. Richardson extrapolation is especially useful when grid refinement is expensive.
