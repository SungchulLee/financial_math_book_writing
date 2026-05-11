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
# heat_equation_2d/grid.py
# ============================================================================
import numpy as np
from typing import NamedTuple


class Grid2DParams(NamedTuple):
    """Grid parameters for the 2D heat equation."""
    Lx: float; Ly: float; T: float; Nx: int; Ny: int; Nt: int; D: float
    dx: float; dy: float; dt: float; x: np.ndarray; y: np.ndarray
    X: np.ndarray; Y: np.ndarray; rx: float; ry: float


def check_2d_stability(rx: float, ry: float, method: str = "forward") -> None:
    """
    Check stability condition for 2D explicit schemes.
    
    Args:
        rx: Diffusion coefficient in x direction (D*dt/dx^2)
        ry: Diffusion coefficient in y direction (D*dt/dy^2)
        method: Numerical method being used
        
    Raises:
        ValueError: If stability condition is violated
    """
    if method == "forward" and rx + ry > 0.5:
        raise ValueError(
            f"Forward Euler unstable in 2D: rx + ry = {rx + ry:.4f} > 0.5. "
            f"Reduce dt or increase dx/dy."
        )


def create_time_array_2d(T: float, Nt: int) -> np.ndarray:
    """Create time array for the 2D simulation."""
    return np.linspace(0, T, Nt + 1)


def get_stability_info(params):
    """Get stability information for the grid parameters."""
    stability_param = params.rx + params.ry
    return {
        "stability_parameter": stability_param,
        "is_stable_forward": stability_param <= 0.5,
        "rx": params.rx,
        "ry": params.ry,
        "dx": params.dx,
        "dy": params.dy,
        "dt": params.dt
    }


def create_2d_grid(Lx=1.0, Ly=1.0, T=0.1, Nx=50, Ny=50, Nt=1000, D=0.01):
    """Create 2D grid parameters."""
    dx, dy, dt = Lx/(Nx-1), Ly/(Ny-1), T/Nt
    x, y = np.linspace(0, Lx, Nx), np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y, indexing="ij")
    rx, ry = D*dt/dx**2, D*dt/dy**2
    return Grid2DParams(Lx, Ly, T, Nx, Ny, Nt, D, dx, dy, dt, x, y, X, Y, rx, ry)


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
For a 2D grid with $L_x = L_y = 1$, $N_x = N_y = 50$, $N_t = 1000$, $T = 0.1$, and $D = 0.01$, compute the stability parameters $r_x$ and $r_y$ and determine if Forward Euler is stable.

??? success "Solution to Exercise 1"
    $\Delta x = 1/49 \approx 0.0204$, $\Delta y = 1/49 \approx 0.0204$, $\Delta t = 0.1/1000 = 10^{-4}$.

    $$
    r_x = \frac{D\Delta t}{\Delta x^2} = \frac{0.01 \times 10^{-4}}{(0.0204)^2} \approx \frac{10^{-6}}{4.16 \times 10^{-4}} \approx 0.0024
    $$

    By symmetry, $r_y \approx 0.0024$. The stability condition is $r_x + r_y \le 0.5$, and $0.0048 \le 0.5$, so Forward Euler is stable.

---

**Exercise 2.**
Derive the 2D stability condition $r_x + r_y \le 1/2$ for Forward Euler using von Neumann analysis with a 2D Fourier mode $u_{j,k}^n = g^n e^{i(j\theta_x + k\theta_y)}$.

??? success "Solution to Exercise 2"
    Substituting into the 2D Forward Euler scheme gives the amplification factor

    $$
    g = 1 - 2r_x(1 - \cos\theta_x) - 2r_y(1 - \cos\theta_y)
    $$

    The worst case is $\theta_x = \theta_y = \pi$, giving $g = 1 - 4r_x - 4r_y$. For stability, $|g| \le 1$, so $-1 \le 1 - 4(r_x + r_y) \le 1$, which yields $r_x + r_y \le 1/2$.

---

**Exercise 3.**
If the 2D grid uses $N_x = 100$ and $N_y = 100$, how many unknowns are in the flattened system? Why do 2D implicit methods typically use sparse solvers?

??? success "Solution to Exercise 3"
    The flattened system has $N_x \times N_y = 10{,}000$ unknowns. The system matrix is $10{,}000 \times 10{,}000$, which would require 800 MB to store as a dense matrix (assuming 8-byte doubles).

    However, the 2D Laplacian matrix is sparse: each row has at most 5 nonzero entries (the stencil $[1, 1, -4, 1, 1]$). Sparse storage requires only about $5 \times 10{,}000 = 50{,}000$ entries. Sparse solvers (e.g., `scipy.sparse.linalg.spsolve`) exploit this structure, reducing memory from $O(N^2)$ to $O(N)$ and computation from $O(N^3)$ to $O(N^{3/2})$ or better.

---

**Exercise 4.**
Explain the difference between `indexing="ij"` and `indexing="xy"` in `np.meshgrid`. Which convention does the 2D heat equation code use and why?

??? success "Solution to Exercise 4"
    With `indexing="ij"`, `X[i,j]` corresponds to the $i$-th $x$-value and $j$-th $y$-value, so the first index varies with $x$ and the second with $y$. With `indexing="xy"`, the convention is transposed: `X[j,i]` uses row for $y$ and column for $x$.

    The code uses `indexing="ij"` because it matches the natural matrix convention where the first index is the row (x-direction) and second is the column (y-direction). This simplifies the finite difference stencil implementation and the flattening/reshaping operations needed for implicit solvers.
