# Vasicek Schemes

## Background

This page presents the Python implementation for **Vasicek Schemes**.

---

## Code

```python
"""
Vasicek Schemes

Educational script demonstrating vasicek schemes concepts.
"""

# ============================================================================
# vasicek/vasicek_schemes.py
# ============================================================================
import numpy as np
from typing import Callable
from .vasicek_base import VasicekParameters, VasicekScheme, VasicekNumericalError


def euler_maruyama_scheme(
    params: VasicekParameters,
    brownian_increments: np.ndarray,
    dt: float,
    **kwargs  # Absorb unused parameters for consistency with CIR


if __name__ == "__main__":
    ) -> np.ndarray:
        """Euler-Maruyama discretization scheme for Vasicek."""
        num_paths, num_steps = brownian_increments.shape
        rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
        for i in range(num_steps):
            current_rates = rates[:, i]
        
            # Vasicek dynamics: dr = a(b - r)dt + σ dW
            drift = params.a * (params.b - current_rates) * dt
            diffusion = params.sigma * brownian_increments[:, i]
        
            rates[:, i + 1] = current_rates + drift + diffusion
    
        return rates


    def exact_scheme(
        params: VasicekParameters,
        brownian_increments: np.ndarray,
        dt: float,
        **kwargs
    ) -> np.ndarray:
        """
        Exact simulation scheme for Vasicek model.
    
        The Vasicek model has a known exact solution:
        r(t+dt) = r(t)*exp(-a*dt) + b*(1-exp(-a*dt)) + σ*sqrt((1-exp(-2*a*dt))/(2*a))*Z
        where Z ~ N(0,1)
        """
        num_paths, num_steps = brownian_increments.shape
        rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
        # Pre-calculate coefficients
        exp_a_dt = np.exp(-params.a * dt)
        mean_coeff = 1 - exp_a_dt
    
        if params.a != 0:
            var_coeff = params.sigma * np.sqrt((1 - np.exp(-2 * params.a * dt)) / (2 * params.a))
        else:
            var_coeff = params.sigma * np.sqrt(dt)
    
        for i in range(num_steps):
            current_rates = rates[:, i]
        
            # Exact Vasicek transition
            mean_term = current_rates * exp_a_dt + params.b * mean_coeff
            noise_term = var_coeff * brownian_increments[:, i] / np.sqrt(dt)  # Convert to standard normal
        
            rates[:, i + 1] = mean_term + noise_term
    
        return rates


    def milstein_scheme(
        params: VasicekParameters,
        brownian_increments: np.ndarray,
        dt: float,
        **kwargs
    ) -> np.ndarray:
        """
        Milstein scheme for Vasicek model.
    
        For Vasicek, Milstein is the same as Euler-Maruyama since the diffusion
        coefficient is constant (no dependence on r).
        """
        return euler_maruyama_scheme(params, brownian_increments, dt, **kwargs)


    # Scheme registry
    SCHEME_REGISTRY = {
        VasicekScheme.EULER_MARUYAMA: euler_maruyama_scheme,
        VasicekScheme.EXACT: exact_scheme,
        VasicekScheme.MILSTEIN: milstein_scheme,
    }


    def get_scheme_simulator(scheme: VasicekScheme) -> Callable:
        """Get the appropriate scheme simulator function."""
        if scheme not in SCHEME_REGISTRY:
            raise VasicekNumericalError(f"Unknown scheme: {scheme}")
    
        return SCHEME_REGISTRY[scheme]
```

## Exercises

**Exercise 1.**
Write the Euler-Maruyama update step for the Vasicek model. Why is the Milstein scheme identical to Euler-Maruyama for Vasicek?

??? success "Solution to Exercise 1"
    The Euler-Maruyama step is

    $$
    r_{i+1} = r_i + a(b - r_i)\,\Delta t + \sigma\,\Delta W_i.
    $$

    The Milstein correction adds $\frac{1}{2}\sigma(r)\sigma'(r)(\Delta W^2 - \Delta t)$. For Vasicek, $\sigma(r) = \sigma$ (constant), so $\sigma'(r) = 0$. The correction term vanishes, making Milstein identical to Euler-Maruyama.

---

**Exercise 2.**
The exact scheme computes $r(t + \Delta t) = r(t)e^{-a\Delta t} + b(1 - e^{-a\Delta t}) + v_c \cdot Z$. The code converts Brownian increments to standard normals via `brownian_increments[:, i] / np.sqrt(dt)`. Explain this conversion.

??? success "Solution to Exercise 2"
    The `BrownianMotion` parent class generates increments $\Delta W_i \sim \mathcal{N}(0, \Delta t)$, i.e., $\Delta W_i = \sqrt{\Delta t}\,Z_i$ where $Z_i \sim \mathcal{N}(0,1)$. The exact scheme needs standard normal variates $Z_i$, so the code recovers them by dividing: $Z_i = \Delta W_i / \sqrt{\Delta t}$. The variance coefficient $v_c = \sigma\sqrt{(1 - e^{-2a\Delta t})/(2a)}$ already incorporates the correct scaling, so it must be multiplied by a standard normal rather than the raw Brownian increment.

---

**Exercise 3.**
For $a = 0.1$, $\sigma = 0.02$, and $\Delta t = 0.01$, compute the pre-calculated coefficients `exp_a_dt`, `mean_coeff`, and `var_coeff` used in the exact scheme.

??? success "Solution to Exercise 3"
    $$
    e^{-a\Delta t} = e^{-0.001} \approx 0.999000.
    $$

    $$
    \text{mean\_coeff} = 1 - e^{-a\Delta t} = 1 - 0.999000 = 0.001000.
    $$

    $$
    \text{var\_coeff} = \sigma\sqrt{\frac{1 - e^{-2a\Delta t}}{2a}} = 0.02\sqrt{\frac{1 - e^{-0.002}}{0.2}} = 0.02\sqrt{\frac{0.001998}{0.2}} = 0.02\sqrt{0.009990} \approx 0.02 \times 0.09995 = 0.001999.
    $$

---

**Exercise 4.**
The scheme registry maps each `VasicekScheme` enum to a function. Describe the advantages of this registry pattern compared to using if-else statements inside the simulation loop.

??? success "Solution to Exercise 4"
    The registry pattern (`SCHEME_REGISTRY` dictionary) has several advantages:

    1. **Open-closed principle**: New schemes can be added by inserting an entry in the dictionary without modifying existing code or the simulation loop.
    2. **Single dispatch**: The `get_scheme_simulator` function performs a single dictionary lookup $O(1)$, whereas a chain of if-else statements has $O(n)$ comparison cost and becomes unwieldy as schemes are added.
    3. **Testability**: Each scheme function can be unit-tested independently since it is a standalone function with a well-defined signature.
    4. **Separation of concerns**: The simulation engine does not need to know the details of each scheme; it simply calls the function returned by the registry.
