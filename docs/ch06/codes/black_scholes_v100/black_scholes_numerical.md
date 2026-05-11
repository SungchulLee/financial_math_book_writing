# Black Scholes Numerical

## Background

Black Scholes Numerical

Educational script demonstrating black scholes numerical concepts.

---

## Code

```python
"""
Black Scholes Numerical

Educational script demonstrating black scholes numerical concepts.
"""

# ============================================================================
# black_scholes/black_scholes_numerical.py
# ============================================================================
import numpy as np
from .black_scholes_base import BlackScholesBase
from .black_scholes_schemes import explicit_scheme, implicit_scheme, cn_scheme, explicit_log_scheme, implicit_log_scheme, cn_log_scheme

class BlackScholesNumericalSolver(BlackScholesBase):
    def solve(self, method="explicit", option_type="put", **kwargs):
        if method == "explicit":
            return self.explicit(option_type=option_type, **kwargs)
        elif method == "implicit":
            return self.implicit(option_type=option_type, **kwargs)
        elif method == "cn":
            return self.cn(option_type=option_type, **kwargs)
        elif method == "explicit_log":
            return self.explicit_log(option_type=option_type, **kwargs)
        elif method == "implicit_log":
            return self.implicit_log(option_type=option_type, **kwargs)
        elif method == "cn_log":
            return self.cn_log(option_type=option_type, **kwargs)
        else:
            raise ValueError(f"Unknown method: {method}. Choose from 'explicit', 'implicit', 'cn', 'explicit_log', 'implicit_log', 'cn_log'.")
        
    def _payoff(self, S, option_type):
        """Calculate option payoff at expiration."""
        if option_type == 'put':
            return np.maximum(self.K - S, 0)
        elif option_type == 'call':
            return np.maximum(S - self.K, 0)
        else:
            raise ValueError("option_type must be 'put' or 'call'")

    def _check_stability_explicit(self, Smax, dS, dt):
        """Check stability condition for explicit finite difference scheme in original stock space."""
        coeff = (self.sigma**2 * Smax**2 * dt) / (dS**2)
        if coeff > 1:
            raise ValueError(f"⚠️ Unstable explicit scheme: sigma² * Smax² * dt / dS² = {coeff:.4f} > 1. "
                            "Reduce dt or increase dS.")

    def explicit(self, option_type='put', Smin=0, Smax=200, NS=100, NT=None, early_exercise=False):
        dS = (Smax - Smin) / (NS - 1)
        if NT is None:
            dt_stable = (dS ** 2) / (self.sigma ** 2 * Smax ** 2)
            NT = int(np.ceil(self.T / (0.5 * dt_stable)))
        if NT < 2:
            raise ValueError("NT must be at least 2 for time-stepping.")
        dt = self.T / (NT - 1)

        self._check_stability_explicit(Smax, dS, dt)

        return explicit_scheme(self, option_type, Smin, Smax, NS, NT, early_exercise)

    def implicit(self, option_type='put', Smin=1e-3, Smax=500, NS=100, NT=100, early_exercise=False):
        return implicit_scheme(self, option_type, Smin, Smax, NS, NT, early_exercise)

    def cn(self, option_type='put', Smin=0, Smax=200, NS=100, NT=100, early_exercise=False):
        return cn_scheme(self, option_type, Smin, Smax, NS, NT, early_exercise)

    def _check_stability_explicit_log(self, dx, dt):
        """Check CFL stability condition for explicit finite difference scheme in log-price space."""
        coeff = self.sigma**2 * dt / dx**2
        if coeff > 1:
            raise ValueError(f"⚠️ Unstable scheme: sigma^2 * dt / dx^2 = {coeff:.4f} > 1. "
                            "Reduce dt or increase dx to satisfy stability condition.")

    def explicit_log(self, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=None, early_exercise=False):
        xmin, xmax = np.log(Smin), np.log(Smax)
        dx = (xmax - xmin) / (NX - 1)

        if NT is None:
            dt_stable = dx**2 / self.sigma**2
            NT = int(np.ceil(self.T / (0.5 * dt_stable)))
        if NT < 2:
            raise ValueError("NT must be at least 2 for time stepping.")
        dt = self.T / (NT - 1)

        self._check_stability_explicit_log(dx, dt)
        return explicit_log_scheme(self, option_type, Smin, Smax, NX, NT, early_exercise)

    def implicit_log(self, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=100, early_exercise=False):
        return implicit_log_scheme(self, option_type, Smin, Smax, NX, NT, early_exercise)

    def cn_log(self, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=100, early_exercise=False):
        return cn_log_scheme(self, option_type, Smin, Smax, NX, NT, early_exercise)


if __name__ == "__main__":
    pass
```
## Exercises

**Exercise 1.**
Describe the explicit finite difference scheme for the Black-Scholes PDE in stock-price space. What is the stability condition?

??? success "Solution to Exercise 1"
    The BS PDE $V_t + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$ is discretized backward in time on a grid $(S_i, t_j)$:

    $$
    V_i^{j} = a_i V_{i-1}^{j+1} + b_i V_i^{j+1} + c_i V_{i+1}^{j+1}
    $$

    where $a_i = \frac{\Delta t}{2}(\sigma^2 i^2 - ri)$, $b_i = 1 - \Delta t(\sigma^2 i^2 + r)$, $c_i = \frac{\Delta t}{2}(\sigma^2 i^2 + ri)$ for $S_i = i\Delta S$.

    The stability condition requires $b_i \ge 0$ for all $i$, which gives $\Delta t \le 1/(\sigma^2 i_{\max}^2 + r)$, becoming very restrictive for large $i_{\max}$ (high stock prices).

---

**Exercise 2.**
Explain the advantage of transforming to log-price coordinates $x = \ln S$ before applying finite differences.

??? success "Solution to Exercise 2"
    In log-coordinates, the BS PDE becomes $V_t + \frac{1}{2}\sigma^2 V_{xx} + (r - \frac{1}{2}\sigma^2)V_x - rV = 0$, which has constant coefficients. This means:

    1. The finite difference stencil has uniform spacing and constant coefficients, simplifying implementation.
    2. The stability condition is independent of the grid location (no $i^2$ factor).
    3. The grid naturally resolves the region near ATM where the option value changes most rapidly.
    4. Boundary conditions are easier to formulate ($x \to -\infty$ and $x \to +\infty$).

---

**Exercise 3.**
Compare the explicit, implicit, and Crank-Nicolson schemes for the BS PDE. Which is typically used in practice?

??? success "Solution to Exercise 3"

    - **Explicit**: Cheap per step but conditionally stable. Rarely used for production pricing due to the severe time-step restriction.
    - **Implicit**: Unconditionally stable, $O(\Delta t)$ accuracy. Robust but low accuracy.
    - **Crank-Nicolson**: Unconditionally stable, $O(\Delta t^2 + \Delta x^2)$ accuracy. The standard choice for production BS PDE solvers.

    Crank-Nicolson is most common because it combines unconditional stability with second-order accuracy. However, it can produce oscillations near discontinuities (e.g., the option payoff kink at $S = K$), which are mitigated by Rannacher time stepping (using a few implicit steps at the start).

---

**Exercise 4.**
The class provides `solve(method, option_type)` with six scheme variants. Describe when you would prefer log-space schemes over stock-price-space schemes.

??? success "Solution to Exercise 4"
    Log-space schemes are preferred when:

    1. The volatility is high (the stock price range spans several orders of magnitude).
    2. A uniform grid is desired (log-space gives uniform relative resolution).
    3. Constant-coefficient methods simplify implementation and analysis.
    4. The option is far from the money (log-space better resolves the tail regions).

    Stock-price-space schemes are simpler to implement and may be preferred for low-volatility problems or when boundary conditions are naturally expressed in terms of $S$ rather than $\ln S$. They are also more intuitive for understanding the connection between the PDE and the financial payoff.
