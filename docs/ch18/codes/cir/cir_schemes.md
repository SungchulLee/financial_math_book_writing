# Cir Schemes

## Background

This page presents the Python implementation for **Cir Schemes**.

---

## Code

```python
"""
Cir Schemes

Educational script demonstrating cir schemes concepts.
"""

# ============================================================================
# cir/cir_schemes.py
# ============================================================================
import numpy as np
from typing import Callable
from .cir_base import CIRParameters, CIRScheme, CIRNumericalError


def euler_maruyama_scheme(
    params: CIRParameters,
    brownian_increments: np.ndarray,
    dt: float,
    absorption_fix: bool = True


if __name__ == "__main__":
    ) -> np.ndarray:
        """Euler-Maruyama discretization scheme for CIR."""
        num_paths, num_steps = brownian_increments.shape
        rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
        for i in range(num_steps):
            current_rates = rates[:, i]
        
            # Ensure non-negative rates for square root
            current_rates_pos = np.maximum(current_rates, 0.0)
            sqrt_rates = np.sqrt(current_rates_pos)
        
            # CIR dynamics: dr = κ(θ - r)dt + σ√r dW
            drift = params.kappa * (params.theta - current_rates) * dt
            diffusion = params.sigma * sqrt_rates * brownian_increments[:, i]
        
            rates[:, i + 1] = current_rates + drift + diffusion
        
            # Apply absorption at zero if requested
            if absorption_fix:
                rates[:, i + 1] = np.maximum(rates[:, i + 1], 0.0)
    
        return rates


    def milstein_scheme(
        params: CIRParameters,
        brownian_increments: np.ndarray,
        dt: float,
        absorption_fix: bool = True
    ) -> np.ndarray:
        """Milstein discretization scheme with second-order correction."""
        num_paths, num_steps = brownian_increments.shape
        rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
        for i in range(num_steps):
            current_rates = rates[:, i]
            current_rates_pos = np.maximum(current_rates, 0.0)
            sqrt_rates = np.sqrt(current_rates_pos)
        
            dW = brownian_increments[:, i]
        
            # Euler part
            drift = params.kappa * (params.theta - current_rates) * dt
            diffusion = params.sigma * sqrt_rates * dW
        
            # Milstein correction: 0.5 * σ * (∂σ/∂r) * (dW² - dt)
            # For CIR: σ(r) = σ√r, so ∂σ/∂r = σ/(2√r)
            milstein_correction = 0.25 * params.sigma**2 * (dW**2 - dt)
        
            rates[:, i + 1] = current_rates + drift + diffusion + milstein_correction
        
            if absorption_fix:
                rates[:, i + 1] = np.maximum(rates[:, i + 1], 0.0)
    
        return rates


    def truncated_euler_scheme(
        params: CIRParameters,
        brownian_increments: np.ndarray,
        dt: float,
        absorption_fix: bool = True
    ) -> np.ndarray:
        """Truncated Euler scheme that handles negative rates more carefully."""
        num_paths, num_steps = brownian_increments.shape
        rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
        for i in range(num_steps):
            current_rates = rates[:, i]
        
            # Drift uses original rate for mean reversion
            drift = params.kappa * (params.theta - current_rates) * dt
        
            # Diffusion uses truncated rate to avoid sqrt of negative
            current_rates_pos = np.maximum(current_rates, 0.0)
            sqrt_rates = np.sqrt(current_rates_pos)
            diffusion = params.sigma * sqrt_rates * brownian_increments[:, i]
        
            rates[:, i + 1] = current_rates + drift + diffusion
        
            # Always apply truncation in this scheme
            rates[:, i + 1] = np.maximum(rates[:, i + 1], 0.0)
    
        return rates


    def exact_scheme(
        params: CIRParameters,
        brownian_increments: np.ndarray,
        dt: float,
        absorption_fix: bool = True
    ) -> np.ndarray:
        """
        Exact simulation scheme using non-central chi-squared distribution.
    
        Note: This is a placeholder implementation.
        Full exact simulation requires sampling from non-central chi-squared.
        """
        # For now, fall back to Milstein which is more accurate than Euler
        return milstein_scheme(params, brownian_increments, dt, absorption_fix)


    # Scheme registry
    SCHEME_REGISTRY = {
        CIRScheme.EULER_MARUYAMA: euler_maruyama_scheme,
        CIRScheme.MILSTEIN: milstein_scheme,
        CIRScheme.TRUNCATED_EULER: truncated_euler_scheme,
        CIRScheme.EXACT: exact_scheme,
    }


    def get_scheme_simulator(scheme: CIRScheme) -> Callable:
        """Get the appropriate scheme simulator function."""
        if scheme not in SCHEME_REGISTRY:
            raise CIRNumericalError(f"Unknown scheme: {scheme}")
    
        return SCHEME_REGISTRY[scheme]
```

## Exercises

**Exercise 1.**
Write the Euler-Maruyama update step for the CIR model and explain why the absorption fix $r_{i+1} = \max(r_{i+1}, 0)$ is needed.

??? success "Solution to Exercise 1"
    The Euler-Maruyama step is

    $$
    r_{i+1} = r_i + \kappa(\theta - r_i)\,\Delta t + \sigma\sqrt{r_i}\,\Delta W_i.
    $$

    Even though the continuous CIR process remains non-negative under the Feller condition, the discrete approximation can produce negative values. When $r_i$ is small and $\Delta W_i$ is a large negative draw, the diffusion term $\sigma\sqrt{r_i}\,\Delta W_i$ can dominate and push $r_{i+1}$ below zero. The absorption fix applies $r_{i+1} = \max(r_{i+1}, 0)$, which reflects the path at zero, ensuring the square root $\sqrt{r_{i+1}}$ remains well-defined at the next step.

---

**Exercise 2.**
The Milstein correction for the CIR model adds the term $\frac{1}{4}\sigma^2(\Delta W_i^2 - \Delta t)$ to the Euler-Maruyama step. Derive this correction starting from the general Milstein formula.

??? success "Solution to Exercise 2"
    The general Milstein scheme for an SDE $dX = a(X)\,dt + b(X)\,dW$ adds the correction

    $$
    \frac{1}{2}\,b(X)\,b'(X)\,(\Delta W^2 - \Delta t).
    $$

    For the CIR model, $b(r) = \sigma\sqrt{r}$, so

    $$
    b'(r) = \frac{\sigma}{2\sqrt{r}}.
    $$

    The correction term becomes

    $$
    \frac{1}{2}\,\sigma\sqrt{r}\,\cdot\,\frac{\sigma}{2\sqrt{r}}\,(\Delta W^2 - \Delta t) = \frac{\sigma^2}{4}\,(\Delta W^2 - \Delta t).
    $$

    This is independent of $r$, making implementation straightforward. It improves the strong convergence order from $O(\sqrt{\Delta t})$ (Euler) to $O(\Delta t)$ (Milstein).

---

**Exercise 3.**
Compare the truncated Euler scheme to the standard Euler-Maruyama scheme. Under what conditions does the truncated scheme offer a significant advantage?

??? success "Solution to Exercise 3"
    In the standard Euler-Maruyama scheme, the drift term uses the actual (possibly negative) rate: $\kappa(\theta - r_i)\,\Delta t$. In the truncated Euler scheme, the diffusion coefficient uses $\sqrt{\max(r_i, 0)}$ while the drift still uses the original $r_i$, and the final output is truncated: $r_{i+1} = \max(r_{i+1}, 0)$.

    The truncated scheme offers a significant advantage when the Feller condition is violated or nearly violated ($2\kappa\theta < \sigma^2$), because rates frequently approach zero. In this regime, the standard scheme may produce many negative values before truncation, leading to biased statistics. The truncated scheme handles the boundary more carefully, reducing bias near zero while maintaining mean-reversion behavior through the untruncated drift.

---

**Exercise 4.**
The scheme registry maps `CIRScheme.EXACT` to a function that currently falls back to Milstein. Describe what a true exact scheme implementation would require and why it is more computationally expensive.

??? success "Solution to Exercise 4"
    A true exact scheme exploits the fact that the CIR transition distribution is known: $c \cdot r(t + \Delta t) \mid r(t)$ follows a non-central chi-squared distribution $\chi'^2(2q + 2, \lambda)$, where

    $$
    c = \frac{2\kappa}{\sigma^2(1 - e^{-\kappa\Delta t})}, \quad q = \frac{2\kappa\theta}{\sigma^2} - 1, \quad \lambda = c\,r(t)\,e^{-\kappa\Delta t}.
    $$

    At each step, one samples from this distribution and rescales: $r(t + \Delta t) = \chi'^2 / c$. This eliminates discretization error entirely but is more expensive because sampling from a non-central chi-squared distribution requires either Poisson mixing (sample a Poisson variate, then a chi-squared) or rejection methods, both of which are slower than sampling a single Gaussian for Euler-Maruyama.
