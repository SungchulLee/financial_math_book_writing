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
# heat_equation_2d/initial_conditions.py
# ============================================================================
import numpy as np
from typing import Callable, Tuple


def step_function_2d(X, Y, x_range=(0.4, 0.6), y_range=(0.4, 0.6), value=1.0, **kwargs):
    """Create 2D step function initial condition."""
    u = np.zeros_like(X)
    Lx, Ly = X.max(), Y.max()
    x1, x2 = x_range[0]*Lx, x_range[1]*Lx
    y1, y2 = y_range[0]*Ly, y_range[1]*Ly
    mask = (X >= x1) & (X <= x2) & (Y >= y1) & (Y <= y2)
    u[mask] = value
    return u


def gaussian_pulse_2d(X, Y, center=(0.5, 0.5), width=(0.1, 0.1), amplitude=1.0, **kwargs):
    """Create 2D Gaussian initial condition."""
    Lx, Ly = X.max(), Y.max()
    xc, yc = center[0]*Lx, center[1]*Ly
    return amplitude * np.exp(-((X-xc)**2/(2*width[0]**2) + (Y-yc)**2/(2*width[1]**2)))

def gaussian_2d(X, Y, center=(0.5, 0.5), width=(0.1, 0.1), amplitude=1.0):
    """Create 2D Gaussian initial condition."""
    Lx, Ly = X.max(), Y.max()
    xc, yc = center[0]*Lx, center[1]*Ly
    return amplitude * np.exp(-((X-xc)**2/(2*width[0]**2) + (Y-yc)**2/(2*width[1]**2)))


def circular_pulse_2d(X, Y, center=(0.5, 0.5), radius=0.1, amplitude=1.0, **kwargs):
    """Create 2D circular pulse initial condition."""
    Lx, Ly = X.max(), Y.max()
    xc, yc = center[0]*Lx, center[1]*Ly
    distance = np.sqrt((X-xc)**2 + (Y-yc)**2)
    u = np.zeros_like(X)
    mask = distance <= radius
    u[mask] = amplitude
    return u


def sine_wave_2d(X: np.ndarray, Y: np.ndarray,
                 n_modes: Tuple[int, int] = (1, 1),
                 amplitude: float = 1.0,
                 Lx: float = 1.0, Ly: float = 1.0) -> np.ndarray:
    """
    Create a 2D sine wave initial condition.
    
    Args:
        X: 2D array of x coordinates
        Y: 2D array of y coordinates
        n_modes: Number of sine modes in (x, y) directions
        amplitude: Amplitude of the wave
        Lx: Length in x direction
        Ly: Length in y direction
        
    Returns:
        2D initial condition array
    """
    return amplitude * (np.sin(n_modes[0] * np.pi * X / Lx) * 
                       np.sin(n_modes[1] * np.pi * Y / Ly))


def sinusoidal_2d(X, Y, modes=(1, 1), amplitude=1.0, **kwargs):
    """Create 2D sinusoidal initial condition."""
    Lx, Ly = X.max(), Y.max()
    return amplitude * np.sin(modes[0] * np.pi * X / Lx) * np.sin(modes[1] * np.pi * Y / Ly)


def multiple_hotspots_2d(X, Y, hotspots=None, **kwargs):
    """Create multiple hotspots initial condition."""
    if hotspots is None:
        hotspots = [
            {"center": (0.3, 0.3), "width": (0.05, 0.05), "amplitude": 1.0},
            {"center": (0.7, 0.7), "width": (0.08, 0.05), "amplitude": 0.8},
            {"center": (0.3, 0.7), "width": (0.06, 0.08), "amplitude": 1.2}
        ]
    
    u = np.zeros_like(X)
    for hotspot in hotspots:
        u += gaussian_pulse_2d(X, Y, **hotspot)
    
    return u


def ring_pattern_2d(X: np.ndarray, Y: np.ndarray,
                    center: Tuple[float, float] = (0.5, 0.5),
                    inner_radius: float = 0.2, outer_radius: float = 0.3,
                    amplitude: float = 1.0,
                    Lx: float = 1.0, Ly: float = 1.0) -> np.ndarray:
    """
    Create a ring pattern initial condition.
    
    Args:
        X: 2D array of x coordinates
        Y: 2D array of y coordinates
        center: Relative center position (0 to 1) in (x, y)
        inner_radius: Inner radius of the ring
        outer_radius: Outer radius of the ring
        amplitude: Amplitude in the ring
        Lx: Length in x direction
        Ly: Length in y direction
        
    Returns:
        2D initial condition array
    """
    x_center = center[0] * Lx
    y_center = center[1] * Ly
    
    u_initial = np.zeros_like(X)
    distance = np.sqrt((X - x_center)**2 + (Y - y_center)**2)
    
    mask = (distance >= inner_radius * min(Lx, Ly)) & (distance <= outer_radius * min(Lx, Ly))
    u_initial[mask] = amplitude
    
    return u_initial


def custom_function_2d(X: np.ndarray, Y: np.ndarray, 
                       func: Callable[[np.ndarray, np.ndarray], np.ndarray]) -> np.ndarray:
    """
    Create initial condition from a custom function.
    
    Args:
        X: 2D array of x coordinates
        Y: 2D array of y coordinates
        func: Function that takes X, Y arrays and returns u array
        
    Returns:
        2D initial condition array
    """
    return func(X, Y)


def zero_initial_condition_2d(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Create zero initial condition (useful for source problems).
    
    Args:
        X: 2D array of x coordinates
        Y: 2D array of y coordinates
        
    Returns:
        Zero initial condition array
    """
    return np.zeros_like(X)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Write the formula for a 2D Gaussian pulse centered at $(x_c, y_c)$ with widths $(\sigma_x, \sigma_y)$ and amplitude $A$. What does the contour plot look like when $\sigma_x \ne \sigma_y$?

??? success "Solution to Exercise 1"
    $$
    f(x,y) = A\exp\!\Bigl(-\frac{(x - x_c)^2}{2\sigma_x^2} - \frac{(y - y_c)^2}{2\sigma_y^2}\Bigr)
    $$

    When $\sigma_x \ne \sigma_y$, the contours are ellipses with semi-axes proportional to $\sigma_x$ and $\sigma_y$. If $\sigma_x > \sigma_y$, the Gaussian is elongated in the $x$-direction. The principal axes of the ellipse align with the coordinate axes because there is no cross term $xy$.

---

**Exercise 2.**
For the ring pattern initial condition with inner radius $r_1 = 0.2$ and outer radius $r_2 = 0.3$ on a unit square, estimate the total mass (area integral of $u$).

??? success "Solution to Exercise 2"
    The ring has amplitude 1 in the annular region $r_1 \le \sqrt{(x-0.5)^2 + (y-0.5)^2} \le r_2$. The area of this annulus is

    $$
    \pi(r_2^2 - r_1^2) = \pi(0.09 - 0.04) = 0.05\pi \approx 0.157
    $$

    Since the amplitude is 1, the total mass equals the area: approximately $0.157$. (This assumes the ring fits entirely within the domain, which it does for a unit square centered at $(0.5, 0.5)$.)

---

**Exercise 3.**
The `multiple_hotspots_2d` function superimposes several Gaussian pulses. Under the heat equation, do the hotspots interact? Explain using the linearity of the PDE.

??? success "Solution to Exercise 3"
    Yes, the hotspots interact through the heat equation because diffusion is a global process. However, the interaction is purely additive due to linearity. If $u_1$ and $u_2$ are solutions for individual hotspots, then $u_1 + u_2$ is the solution for both hotspots combined.

    At early times, well-separated hotspots evolve independently (their Gaussian profiles have negligible overlap). As time progresses, the spreading profiles begin to overlap and merge. The final equilibrium (for Dirichlet BCs) is $u = 0$ everywhere.

---

**Exercise 4.**
Compare the 2D step function and circular pulse initial conditions. Which produces sharper gradients, and how does this affect the numerical solution quality?

??? success "Solution to Exercise 4"
    Both have discontinuities at their boundaries, but:

    - The **step function** has straight-line discontinuities along the rectangle edges, creating corners where two edges meet at right angles. These corners produce the sharpest gradients.
    - The **circular pulse** has a smooth (curved) boundary, but still has a jump discontinuity.

    Both produce Gibbs-like oscillations in spectral methods and first-order accuracy degradation in finite differences. However, the corners of the step function create stronger singularities in the solution gradient, making it slightly harder to resolve numerically. Smoothed versions (e.g., replacing the step with a tanh transition) would improve accuracy significantly.
