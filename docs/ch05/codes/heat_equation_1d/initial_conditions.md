# Initial Conditions

## Background

Initial Conditions

Educational script demonstrating initial conditions concepts.

---

## Code

```python
"""
Initial Conditions

Educational script demonstrating initial conditions concepts.
"""

# ============================================================================
# heat_equation_1d/initial_conditions.py
# ============================================================================
import numpy as np
from typing import Callable


def step_function(x: np.ndarray, start: float = 0.4, end: float = 0.6, 
                  value: float = 1.0, L: float = 1.0) -> np.ndarray:
    """
    Create a step function initial condition.
    
    Args:
        x: Spatial grid points
        start: Relative start position (0 to 1)
        end: Relative end position (0 to 1)
        value: Height of the step
        L: Length of domain
        
    Returns:
        Initial condition array
    """
    u_initial = np.zeros_like(x)
    mask = (x >= start * L) & (x <= end * L)
    u_initial[mask] = value
    return u_initial


def gaussian_pulse(x: np.ndarray, center: float = 0.5, width: float = 0.1, 
                   amplitude: float = 1.0, L: float = 1.0) -> np.ndarray:
    """
    Create a Gaussian pulse initial condition.
    
    Args:
        x: Spatial grid points
        center: Relative center position (0 to 1)
        width: Width parameter (standard deviation)
        amplitude: Peak amplitude
        L: Length of domain
        
    Returns:
        Initial condition array
    """
    x_center = center * L
    return amplitude * np.exp(-(x - x_center)**2 / (2 * width**2))


def sine_wave(x: np.ndarray, n_modes: int = 1, amplitude: float = 1.0, 
              L: float = 1.0) -> np.ndarray:
    """
    Create a sine wave initial condition.
    
    Args:
        x: Spatial grid points
        n_modes: Number of sine modes
        amplitude: Amplitude of the wave
        L: Length of domain
        
    Returns:
        Initial condition array
    """
    return amplitude * np.sin(n_modes * np.pi * x / L)


def triangle_wave(x: np.ndarray, peak_pos: float = 0.5, amplitude: float = 1.0, 
                  L: float = 1.0) -> np.ndarray:
    """
    Create a triangle wave initial condition.
    
    Args:
        x: Spatial grid points
        peak_pos: Relative position of peak (0 to 1)
        amplitude: Peak amplitude
        L: Length of domain
        
    Returns:
        Initial condition array
    """
    x_peak = peak_pos * L
    u_initial = np.zeros_like(x)
    
    # Left side of triangle
    left_mask = x <= x_peak
    u_initial[left_mask] = amplitude * x[left_mask] / x_peak
    
    # Right side of triangle
    right_mask = x > x_peak
    u_initial[right_mask] = amplitude * (L - x[right_mask]) / (L - x_peak)
    
    return u_initial


def custom_function(x: np.ndarray, func: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    """
    Create initial condition from a custom function.
    
    Args:
        x: Spatial grid points
        func: Function that takes x array and returns u array
        
    Returns:
        Initial condition array
    """
    return func(x)


def zero_initial_condition(x: np.ndarray) -> np.ndarray:
    """
    Create zero initial condition (useful for source problems).
    
    Args:
        x: Spatial grid points
        
    Returns:
        Zero initial condition array
    """
    return np.zeros_like(x)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
For a Gaussian pulse $u(x, 0) = A\exp(-(x - x_c)^2 / (2w^2))$ with $A = 1$, $x_c = 0.5$, $w = 0.1$ on $[0, 1]$, compute the total mass $\int_0^1 u(x,0)\,dx$ approximately.

??? success "Solution to Exercise 1"
    Since $w = 0.1$ is small relative to the domain, the Gaussian is well-contained in $[0,1]$, so we approximate using the full-line integral:

    $$
    \int_0^1 e^{-(x-0.5)^2/(2\cdot 0.01)}\,dx \approx \int_{-\infty}^{\infty} e^{-(x-0.5)^2/0.02}\,dx = \sqrt{2\pi \cdot 0.01} = \sqrt{0.02\pi} \approx 0.2507
    $$

    The total mass is approximately $0.251$.

---

**Exercise 2.**
Show that the sine wave initial condition $u(x,0) = \sin(n\pi x / L)$ is an eigenfunction of the 1D heat equation with Dirichlet boundary conditions. What is the corresponding eigenvalue?

??? success "Solution to Exercise 2"
    Substituting $u(x,t) = T(t)\sin(n\pi x/L)$ into $u_t = D u_{xx}$ gives $T'(t)\sin(n\pi x/L) = -D(n\pi/L)^2 T(t)\sin(n\pi x/L)$, so $T'(t) = -D(n\pi/L)^2 T(t)$, with solution $T(t) = e^{-\lambda_n t}$ where

    $$
    \lambda_n = D\left(\frac{n\pi}{L}\right)^2
    $$

    The eigenvalue is $\lambda_n = D n^2\pi^2/L^2$. The exact solution is $u(x,t) = \sin(n\pi x/L)\,e^{-\lambda_n t}$, which decays exponentially with rate proportional to $n^2$.

---

**Exercise 3.**
Compare the step function and triangle wave initial conditions. Which one has Fourier coefficients that decay faster? Explain why this affects numerical convergence.

??? success "Solution to Exercise 3"
    The step function is discontinuous, so its Fourier sine coefficients decay as $O(1/n)$. The triangle wave is continuous (but has a kink), so its coefficients decay as $O(1/n^2)$.

    Faster Fourier decay means fewer modes are needed for an accurate eigenfunction expansion. For numerical methods, smoother initial conditions produce solutions with less high-frequency content, reducing spatial discretization error and leading to faster convergence with grid refinement.

---

**Exercise 4.**
Write a custom initial condition function that models two Gaussian hot spots at positions $x = 0.3$ and $x = 0.7$ with amplitudes 1.0 and 0.5, respectively, both with width $w = 0.05$, on a domain $[0, 1]$.

??? success "Solution to Exercise 4"
    The function is

    $$
    f(x) = \exp\!\Bigl(-\frac{(x - 0.3)^2}{2(0.05)^2}\Bigr) + 0.5\exp\!\Bigl(-\frac{(x - 0.7)^2}{2(0.05)^2}\Bigr)
    $$

    In Python:
    ```python
    def two_hotspots(x):
        return (np.exp(-(x - 0.3)**2 / (2 * 0.05**2))
                + 0.5 * np.exp(-(x - 0.7)**2 / (2 * 0.05**2)))
    ```

    As the heat equation evolves, the two peaks diffuse and eventually merge into a single broad profile that decays toward the Dirichlet boundary values.
