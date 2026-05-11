# Analytical

## Background

Analytical

Educational script demonstrating analytical concepts.

---

## Code

```python
"""
Analytical

Educational script demonstrating analytical concepts.
"""

# ============================================================================
# heat_equation_2d/analytical.py
# ============================================================================
import numpy as np
from typing import Callable


def solve_analytical_2d(X: np.ndarray, Y: np.ndarray, t: float, 
                       initial_func: Callable, D: float, Lx: float, Ly: float,
                       method: str = "eigenfunction", N: int = 20) -> np.ndarray:
    """
    Basic analytical solution for 2D heat equation (simplified version).
    
    For now, this provides a simple eigenfunction expansion for sine wave initial conditions.
    """
    if method == "eigenfunction":
        # Only works for sine wave initial conditions
        try:
            # Try to detect if this is a sine wave
            # This is a simplified implementation
            return _solve_sine_eigenfunction(X, Y, t, D, Lx, Ly, N)
        except:
            # Fallback: return zeros if analytical solution fails
            print("Analytical solution not available for this initial condition")
            return np.zeros_like(X)
    else:
        print(f"Analytical method '{method}' not implemented yet")
        return np.zeros_like(X)


def _solve_sine_eigenfunction(X: np.ndarray, Y: np.ndarray, t: float, 
                             D: float, Lx: float, Ly: float, N: int = 20) -> np.ndarray:
    """Simple eigenfunction solution for (1,1) sine mode."""
    # For u(x,y,0) = sin(πx/Lx)sin(πy/Ly), the analytical solution is:
    # u(x,y,t) = sin(πx/Lx)sin(πy/Ly) * exp(-D*π²*(1/Lx² + 1/Ly²)*t)
    
    lambda_11 = np.pi**2 * (1/Lx**2 + 1/Ly**2)
    return np.sin(np.pi * X / Lx) * np.sin(np.pi * Y / Ly) * np.exp(-D * lambda_11 * t)


def validate_against_analytical_2d(numerical_solution: np.ndarray, 
                                  X: np.ndarray, Y: np.ndarray, t: float,
                                  initial_func: Callable, D: float, 
                                  Lx: float, Ly: float,
                                  method: str = "eigenfunction") -> dict:
    """
    Basic validation against analytical solution.
    """
    try:
        analytical_solution = solve_analytical_2d(X, Y, t, initial_func, D, Lx, Ly, method)
        
        # Calculate error metrics
        absolute_error = np.abs(numerical_solution - analytical_solution)
        relative_error = absolute_error / (np.abs(analytical_solution) + 1e-12)
        
        # Calculate grid spacing for integration
        dx = X[0, 1] - X[0, 0] if X.shape[1] > 1 else 1.0
        dy = Y[1, 0] - Y[0, 0] if Y.shape[0] > 1 else 1.0
        
        return {
            "max_abs_error": np.max(absolute_error),
            "max_rel_error": np.max(relative_error),
            "mean_abs_error": np.mean(absolute_error),
            "mean_rel_error": np.mean(relative_error),
            "l2_error": np.sqrt(dx * dy * np.sum(absolute_error**2)),
            "l2_norm_analytical": np.sqrt(dx * dy * np.sum(analytical_solution**2)),
            "relative_l2_error": np.sqrt(dx * dy * np.sum(absolute_error**2)) / 
                               (np.sqrt(dx * dy * np.sum(analytical_solution**2)) + 1e-12)
        }
    except Exception as e:
        print(f"Validation failed: {e}")
        return {
            "max_abs_error": float('nan'),
            "max_rel_error": float('nan'), 
            "mean_abs_error": float('nan'),
            "mean_rel_error": float('nan'),
            "l2_error": float('nan'),
            "l2_norm_analytical": float('nan'),
            "relative_l2_error": float('nan')
        }


# Placeholder functions to match the expected interface
def solve_analytical(x: np.ndarray, t: float, initial_func: Callable, 
                    D: float, L: float, method: str = "eigenfunction") -> np.ndarray:
    """1D analytical solution placeholder."""
    # This is for 1D compatibility - just return zeros for now
    return np.zeros_like(x)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
For the 2D heat equation with Dirichlet boundary conditions on $[0, L_x] \times [0, L_y]$, write the eigenfunction corresponding to mode numbers $(m, n)$ and its eigenvalue.

??? success "Solution to Exercise 1"
    The eigenfunction is $\phi_{m,n}(x,y) = \sin(m\pi x/L_x)\sin(n\pi y/L_y)$ with eigenvalue

    $$
    \lambda_{m,n} = D\pi^2\left(\frac{m^2}{L_x^2} + \frac{n^2}{L_y^2}\right)
    $$

    The exact solution for this mode is $u(x,y,t) = \phi_{m,n}(x,y)\,e^{-\lambda_{m,n} t}$. Higher-order modes (larger $m$ or $n$) decay faster.

---

**Exercise 2.**
Compute $\lambda_{1,1}$ for a square domain $L_x = L_y = 1$ with $D = 0.01$. After what time $t^*$ has this mode decayed to 1% of its initial amplitude?

??? success "Solution to Exercise 2"
    $$
    \lambda_{1,1} = 0.01 \cdot \pi^2(1 + 1) = 0.02\pi^2 \approx 0.1974
    $$

    Setting $e^{-\lambda_{1,1} t^*} = 0.01$ gives $t^* = -\ln(0.01)/\lambda_{1,1} = \ln(100)/0.1974 \approx 4.605/0.1974 \approx 23.3$. So the fundamental mode takes about 23.3 time units to decay to 1%.

---

**Exercise 3.**
Why is the analytical solution for the 2D heat equation limited to certain initial conditions (e.g., sine waves)? What alternative approaches exist for arbitrary initial data?

??? success "Solution to Exercise 3"
    The eigenfunction expansion requires computing double Fourier coefficients $A_{m,n} = \frac{4}{L_x L_y}\int_0^{L_x}\int_0^{L_y} f(x,y)\sin(m\pi x/L_x)\sin(n\pi y/L_y)\,dy\,dx$. For arbitrary $f$, these integrals must be evaluated numerically, which is expensive and may be inaccurate for non-smooth $f$.

    Alternative approaches: (1) 2D heat kernel convolution $u = \iint G_{\text{2D}} f\,d\xi\,d\eta$, (2) 2D FFT spectral method (fast but assumes periodicity), (3) direct numerical solution via finite differences or finite elements (most general).

---

**Exercise 4.**
Define the relative $L^2$ error between a numerical solution $u_h$ and an analytical solution $u_a$ on a 2D grid. Write the discrete approximation using grid spacings $\Delta x$ and $\Delta y$.

??? success "Solution to Exercise 4"
    The relative $L^2$ error is

    $$
    e_{\text{rel}} = \frac{\|u_h - u_a\|_{L^2}}{\|u_a\|_{L^2}} = \frac{\sqrt{\iint (u_h - u_a)^2\,dx\,dy}}{\sqrt{\iint u_a^2\,dx\,dy}}
    $$

    Discretized on a grid:

    $$
    e_{\text{rel}} \approx \frac{\sqrt{\Delta x\,\Delta y \sum_{i,j}(u_{h,ij} - u_{a,ij})^2}}{\sqrt{\Delta x\,\Delta y \sum_{i,j} u_{a,ij}^2}}
    $$

    The $\Delta x\,\Delta y$ factors cancel, simplifying to the ratio of discrete $\ell^2$ norms, but including them provides a mesh-independent error measure.
