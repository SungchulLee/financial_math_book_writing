# Grid

## Background

Grid

Educational script demonstrating grid concepts.

---

## Code

```python
"""
Grid

Educational script demonstrating grid concepts.
"""

# ============================================================================
# heat_equation_1d/grid.py
# ============================================================================
import numpy as np
from typing import NamedTuple


class GridParams(NamedTuple):
    """Grid parameters for the 1D heat equation."""
    L: float          # Length of domain
    T: float          # Total time
    Nx: int           # Number of spatial points
    Nt: int           # Number of time steps
    D: float          # Thermal diffusivity
    dx: float         # Spatial step size
    dt: float         # Time step size
    x: np.ndarray     # Spatial grid
    coeff: float      # Diffusion coefficient (D*dt/dx^2)


def create_grid(L: float = 1.0, T: float = 0.1, Nx: int = 100, Nt: int = 1000, 
                D: float = 0.01) -> GridParams:
    """
    Create spatial and temporal grids for the heat equation.
    
    Args:
        L: Length of the rod
        T: Total simulation time
        Nx: Number of spatial grid points
        Nt: Number of time steps
        D: Thermal diffusivity constant
        
    Returns:
        GridParams containing all grid information
    """
    if L <= 0 or T <= 0 or D <= 0:
        raise ValueError("L, T, and D must be positive")
    if Nx < 3 or Nt < 1:
        raise ValueError("Nx must be >= 3, Nt must be >= 1")
    
    dx = L / (Nx - 1)
    dt = T / Nt
    x = np.linspace(0, L, Nx)
    coeff = D * dt / dx**2
    
    return GridParams(L, T, Nx, Nt, D, dx, dt, x, coeff)


def check_stability(coeff: float, method: str = "forward") -> None:
    """
    Check stability condition for explicit schemes.
    
    Args:
        coeff: Diffusion coefficient (D*dt/dx^2)
        method: Numerical method being used
        
    Raises:
        ValueError: If stability condition is violated
    """
    if method == "forward" and coeff > 0.5:
        raise ValueError(
            f"Forward Euler unstable: coeff = {coeff:.4f} > 0.5. "
            f"Reduce dt or increase dx."
        )


def create_time_array(T: float, Nt: int) -> np.ndarray:
    """Create time array for the simulation."""
    return np.linspace(0, T, Nt + 1)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
For a rod of length $L = 1$ with $N_x = 101$ grid points and thermal diffusivity $D = 0.01$, compute the spatial step $\Delta x$. If the time step is $\Delta t = 10^{-4}$, compute the stability parameter $\alpha = D\Delta t / \Delta x^2$ and determine whether Forward Euler is stable.

??? success "Solution to Exercise 1"
    With $N_x = 101$, $\Delta x = L/(N_x - 1) = 1/100 = 0.01$. The stability parameter is

    $$
    \alpha = \frac{D\,\Delta t}{\Delta x^2} = \frac{0.01 \cdot 10^{-4}}{(0.01)^2} = \frac{10^{-6}}{10^{-4}} = 0.01
    $$

    Since $\alpha = 0.01 \le 0.5$, the Forward Euler scheme is stable.

---

**Exercise 2.**
Derive the stability condition $\alpha \le 1/2$ for the Forward Euler discretization of the 1D heat equation using von Neumann analysis.

??? success "Solution to Exercise 2"
    Substituting the Fourier mode $u_j^n = g^n e^{ij\theta}$ into the Forward Euler scheme $u_j^{n+1} = u_j^n + \alpha(u_{j+1}^n - 2u_j^n + u_{j-1}^n)$ gives the amplification factor

    $$
    g = 1 + \alpha(e^{i\theta} - 2 + e^{-i\theta}) = 1 - 2\alpha(1 - \cos\theta) = 1 - 4\alpha\sin^2(\theta/2)
    $$

    For stability we need $|g| \le 1$ for all $\theta$. The worst case is $\theta = \pi$, giving $g = 1 - 4\alpha$. Requiring $-1 \le 1 - 4\alpha \le 1$ yields $\alpha \le 1/2$.

---

**Exercise 3.**
If a simulation requires $N_t = 10{,}000$ time steps with $\Delta t = T/N_t$, and $T = 0.1$, what is $\Delta t$? How would you adjust $N_t$ if $\Delta x$ is halved (and $D$ remains unchanged) to maintain stability of Forward Euler?

??? success "Solution to Exercise 3"
    $\Delta t = 0.1 / 10{,}000 = 10^{-5}$.

    If $\Delta x$ is halved, $\Delta x^2$ is quartered. To keep $\alpha = D\Delta t / \Delta x^2$ unchanged, $\Delta t$ must also be quartered. Therefore $N_t$ must be multiplied by 4, giving $N_t = 40{,}000$.

    This illustrates the severe time-step restriction of explicit methods: halving the spatial mesh requires four times as many time steps.

---

**Exercise 4.**
The `GridParams` named tuple stores the coefficient $\alpha = D\Delta t / \Delta x^2$. Explain why this single parameter fully characterizes the behavior of the Forward Euler scheme for the heat equation (assuming Dirichlet boundary conditions and a fixed grid).

??? success "Solution to Exercise 4"
    The Forward Euler update rule for interior points is $u_j^{n+1} = \alpha\, u_{j-1}^n + (1 - 2\alpha)\,u_j^n + \alpha\, u_{j+1}^n$. This shows that the weight assigned to each grid value depends only on $\alpha$, not on $D$, $\Delta t$, or $\Delta x$ individually. Two simulations with different $D$, $\Delta t$, $\Delta x$ but the same $\alpha$ will produce identical numerical solutions (given the same initial and boundary conditions). Therefore $\alpha$ is the sole dimensionless parameter governing accuracy, stability, and diffusion behavior of the scheme.
