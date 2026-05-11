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
# heat_equation_1d/analytical.py
# ============================================================================
import numpy as np
import scipy.interpolate as interpolate
from typing import Callable


def solve_eigenfunction_expansion(x: np.ndarray, t: float, initial_func: Callable,
                                 D: float, L: float, N: int = 100) -> np.ndarray:
    """
    Solve using eigenfunction (Fourier sine series) expansion.
    
    For Dirichlet BC: u(x,t) = Σ A_n sin(nπx/L) exp(-Dλ_n t)
    where λ_n = (nπ/L)² and A_n are Fourier coefficients.
    
    Args:
        x: Spatial grid points
        t: Time at which to evaluate solution
        initial_func: Function defining initial condition f(x)
        D: Thermal diffusivity
        L: Domain length
        N: Number of Fourier modes
        
    Returns:
        Analytical solution at time t
    """
    u_analytic = np.zeros_like(x)
    
    for n in range(1, N + 1):
        lambda_n = (n * np.pi / L) ** 2
        
        # Compute Fourier coefficient A_n = (2/L) ∫ f(x) sin(nπx/L) dx
        integrand = initial_func(x) * np.sin(n * np.pi * x / L)
        A_n = (2 / L) * np.trapezoid(integrand, x)
        
        # Add n-th mode contribution
        mode_contribution = A_n * np.sin(n * np.pi * x / L) * np.exp(-D * lambda_n * t)
        u_analytic += mode_contribution
    
    return u_analytic


def solve_heat_kernel(x: np.ndarray, t: float, initial_func: Callable,
                     D: float, L: float, domain_extend: float = 3) -> np.ndarray:
    """
    Solve using heat kernel (Green's function) convolution.
    
    u(x,t) = ∫ G(x,ξ,t) f(ξ) dξ
    where G(x,ξ,t) = (1/√(4πDt)) exp(-(x-ξ)²/(4Dt))
    
    Args:
        x: Spatial grid points
        t: Time at which to evaluate solution
        initial_func: Function defining initial condition f(x)
        D: Thermal diffusivity
        L: Domain length
        domain_extend: Extension factor for integration domain
        
    Returns:
        Analytical solution at time t
    """
    if t <= 0:
        return initial_func(x)
    
    # Extended domain for integration
    xi = np.linspace(-domain_extend * L, domain_extend * L, 5 * len(x))
    
    def heat_kernel(x_val, xi_val):
        """Heat kernel G(x,ξ,t)"""
        return (1 / np.sqrt(4 * np.pi * D * t)) * np.exp(-(x_val - xi_val)**2 / (4 * D * t))
    
    u_analytic = np.zeros_like(x)
    for i, x_val in enumerate(x):
        G_vals = heat_kernel(x_val, xi)
        u_analytic[i] = np.trapezoid(G_vals * initial_func(xi), xi)
    
    return u_analytic


def solve_fourier_spectral(x: np.ndarray, t: float, initial_func: Callable,
                          D: float, L: float, domain_extend: float = 3) -> np.ndarray:
    """
    Solve using FFT-based spectral method.
    
    The heat equation in Fourier space: ∂û/∂t = -4π²Dk²û
    Solution: û(k,t) = û(k,0) exp(-4π²Dk²t)
    
    Args:
        x: Spatial grid points
        t: Time at which to evaluate solution
        initial_func: Function defining initial condition f(x)
        D: Thermal diffusivity
        L: Domain length (not used directly, but kept for API consistency)
        domain_extend: Extension factor for periodic domain
        
    Returns:
        Analytical solution at time t
    """
    if t <= 0:
        return initial_func(x)
    
    # Create extended periodic domain
    L_ext = domain_extend * L
    Nx_ext = 2**int(np.ceil(np.log2(5 * len(x))))  # FFT-friendly size
    x_ext = np.linspace(-L_ext, L_ext, Nx_ext)
    dx = x_ext[1] - x_ext[0]
    
    # Evaluate initial condition on extended domain
    f_vals = initial_func(x_ext)
    
    # FFT and frequency domain
    f_hat = np.fft.fft(f_vals)
    freqs = np.fft.fftfreq(Nx_ext, d=dx)  # frequencies in cycles per unit length
    
    # Apply heat equation evolution in frequency domain
    filter_decay = np.exp(-4 * np.pi**2 * D * freqs**2 * t)
    u_hat = f_hat * filter_decay
    
    # Inverse FFT to get solution
    u_full = np.fft.ifft(u_hat).real
    
    # Interpolate back to original grid
    interp = interpolate.interp1d(x_ext, u_full, kind='cubic', 
                                 fill_value="extrapolate", bounds_error=False)
    u_analytic = interp(x)
    
    return u_analytic


def solve_analytical(x: np.ndarray, t: float, initial_func: Callable,
                    D: float, L: float, method: str = "eigenfunction", 
                    N: int = 100, domain_extend: float = 3) -> np.ndarray:
    """
    Unified interface for analytical solutions.
    
    Args:
        x: Spatial grid points
        t: Time at which to evaluate solution
        initial_func: Function defining initial condition f(x)
        D: Thermal diffusivity
        L: Domain length
        method: "eigenfunction", "heat_kernel", or "fourier"
        N: Number of terms for eigenfunction expansion
        domain_extend: Domain extension factor for other methods
        
    Returns:
        Analytical solution at time t
    """
    if method == "eigenfunction":
        return solve_eigenfunction_expansion(x, t, initial_func, D, L, N)
    elif method == "heat_kernel":
        return solve_heat_kernel(x, t, initial_func, D, L, domain_extend)
    elif method == "fourier":
        return solve_fourier_spectral(x, t, initial_func, D, L, domain_extend)
    else:
        raise ValueError("Method must be 'eigenfunction', 'heat_kernel', or 'fourier'")


def validate_against_analytical(numerical_solution: np.ndarray, x: np.ndarray, 
                               t: float, initial_func: Callable, D: float, L: float,
                               method: str = "eigenfunction") -> dict:
    """
    Validate numerical solution against analytical solution.
    
    Args:
        numerical_solution: Numerical solution array
        x: Spatial grid points
        t: Time of comparison
        initial_func: Initial condition function
        D: Thermal diffusivity
        L: Domain length
        method: Analytical method to use for comparison
        
    Returns:
        Dictionary with validation metrics
    """
    analytical_solution = solve_analytical(x, t, initial_func, D, L, method)
    
    # Calculate error metrics
    absolute_error = np.abs(numerical_solution - analytical_solution)
    relative_error = absolute_error / (np.abs(analytical_solution) + 1e-12)
    
    max_abs_error = np.max(absolute_error)
    max_rel_error = np.max(relative_error)
    l2_error = np.sqrt(np.trapezoid(absolute_error**2, x))
    l2_norm_analytical = np.sqrt(np.trapezoid(analytical_solution**2, x))
    relative_l2_error = l2_error / (l2_norm_analytical + 1e-12)
    
    return {
        "analytical_solution": analytical_solution,
        "absolute_error": absolute_error,
        "relative_error": relative_error,
        "max_absolute_error": max_abs_error,
        "max_relative_error": max_rel_error,
        "l2_error": l2_error,
        "relative_l2_error": relative_l2_error,
        "analytical_method": method
    }


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
For the eigenfunction expansion of the 1D heat equation with Dirichlet boundary conditions on $[0, L]$, derive the formula for the Fourier coefficient $A_n$ when the initial condition is $f(x) = \sin(m\pi x / L)$ for a positive integer $m$.

??? success "Solution to Exercise 1"
    The Fourier coefficients are $A_n = \frac{2}{L}\int_0^L f(x)\sin\!\bigl(\frac{n\pi x}{L}\bigr)dx$. With $f(x) = \sin(m\pi x/L)$:

    $$
    A_n = \frac{2}{L}\int_0^L \sin\!\bigl(\tfrac{m\pi x}{L}\bigr)\sin\!\bigl(\tfrac{n\pi x}{L}\bigr)dx
    $$

    By orthogonality of sine functions, this integral equals $L/2$ if $n = m$ and $0$ otherwise. Therefore $A_n = \delta_{nm}$ (Kronecker delta), and the exact solution is $u(x,t) = \sin(m\pi x/L)\,e^{-D(m\pi/L)^2 t}$.

---

**Exercise 2.**
Write the heat kernel (Green's function) for the 1D heat equation on $\mathbb{R}$ and show that it integrates to 1 for any $t > 0$.

??? success "Solution to Exercise 2"
    The heat kernel is

    $$
    G(x,\xi,t) = \frac{1}{\sqrt{4\pi D t}}\exp\!\Bigl(-\frac{(x-\xi)^2}{4Dt}\Bigr)
    $$

    Integrating over all $\xi$:

    $$
    \int_{-\infty}^{\infty} G(x,\xi,t)\,d\xi = \frac{1}{\sqrt{4\pi Dt}}\int_{-\infty}^{\infty} e^{-(x-\xi)^2/(4Dt)}\,d\xi
    $$

    Substituting $u = (x - \xi)/\sqrt{4Dt}$, $d\xi = -\sqrt{4Dt}\,du$, gives $\int_{-\infty}^{\infty} e^{-u^2}\,du / \sqrt{\pi} = 1$. This confirms that the heat kernel is a probability density in $\xi$ and conserves total mass.

---

**Exercise 3.**
Explain why the FFT-based spectral method assumes periodic boundary conditions. What artifact can arise when solving a heat equation with Dirichlet conditions using FFT without domain extension?

??? success "Solution to Exercise 3"
    The discrete Fourier transform treats the input data as one period of a periodic function. If the initial condition does not satisfy periodic boundary conditions (e.g., $f(0) \ne f(L)$), the FFT implicitly creates discontinuities at the domain boundaries. These discontinuities produce Gibbs phenomena -- spurious oscillations near the boundaries that contaminate the solution.

    Domain extension mitigates this by padding the domain with zeros (or mirror images) so that the effective function is smooth and approximately periodic over the extended interval. This pushes the boundary artifacts far from the physical domain.

---

**Exercise 4.**
Given a numerical solution $u_h$ and an analytical solution $u$ on a grid with spacing $\Delta x$, define the $L^2$ error and the $L^\infty$ error. If the $L^2$ error scales as $O(\Delta x^p)$, what is $p$ called?

??? success "Solution to Exercise 4"
    The $L^2$ error is

    $$
    \|u_h - u\|_{L^2} = \sqrt{\int_0^L (u_h(x) - u(x))^2\,dx} \approx \sqrt{\Delta x \sum_i (u_{h,i} - u_i)^2}
    $$

    The $L^\infty$ error is

    $$
    \|u_h - u\|_{L^\infty} = \max_i |u_{h,i} - u_i|
    $$

    The exponent $p$ is called the **order of convergence** (or convergence rate) of the numerical method. For example, second-order methods such as Crank-Nicolson have $p = 2$ in space, meaning the error is halved when $\Delta x$ is reduced by a factor of $\sqrt{2}$.
