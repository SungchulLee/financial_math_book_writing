# Heat Equation 2D (Modular)

## Background

Heat Equation 2D Modular

Educational script demonstrating heat equation 2d modular concepts.

---

## Code

```python
"""
Heat Equation 2D Modular

Educational script demonstrating heat equation 2d modular concepts.
"""

# ============================================================================
# heat_equation_2d_MODULAR.py
# ============================================================================
import heat_equation_2d as he2


def main():
    """Main example demonstrating 2D heat equation solver."""
    print("=== 2D Heat Equation Solver Example ===\n")
    
    # Create grid - smaller for faster computation
    params = he2.create_2d_grid(Lx=1.0, Ly=1.0, T=0.02, Nx=30, Ny=30, Nt=200, D=0.01)
    
    # Get stability information
    stability_info = he2.get_stability_info(params)
    print(f"Grid: {params.Nx}×{params.Ny}, dt={params.dt:.4f}")
    print(f"Stability: rx+ry = {stability_info['stability_parameter']:.3f}")
    print(f"Forward Euler stable: {stability_info['is_stable_forward']}")
    print()
    
    # Test 1: Step function
    print("Test 1: Step function initial condition")
    u_step = he2.step_function_2d(params.X, params.Y, x_range=(0.4, 0.6), y_range=(0.4, 0.6))
    
    results_step = he2.compare_2d_methods(u_step, params)
    he2.plot_method_comparison_2d(params.X, params.Y, u_step, results_step)
    
    # Test 2: Gaussian pulse
    print("\nTest 2: Gaussian pulse initial condition")
    u_gauss = he2.gaussian_pulse_2d(params.X, params.Y, center=(0.3, 0.7), width=(0.05, 0.08))
    
    # Just test one method for the Gaussian
    u_final = he2.solve_crank_nicolson_2d(u_gauss, params)
    he2.plot_2d_solution(params.X, params.Y, u_gauss, u_final, "Crank-Nicolson")
    
    # Test 3: Multiple hotspots
    print("\nTest 3: Multiple hotspots")
    u_multi = he2.multiple_hotspots_2d(params.X, params.Y)
    
    u_final_multi = he2.solve_backward_euler_2d(u_multi, params)
    he2.plot_2d_solution(params.X, params.Y, u_multi, u_final_multi, "Backward Euler")
    
    # Test 4: Cross-sections
    print("\nTest 4: Cross-section analysis")
    he2.plot_cross_sections(params.X, params.Y, u_multi, u_final_multi, "Backward Euler")
    
    # Test 5: Circular pulse
    print("\nTest 5: Circular pulse")
    u_circle = he2.circular_pulse_2d(params.X, params.Y, center=(0.5, 0.5), radius=0.15)
    u_final_circle = he2.solve_backward_euler_2d(u_circle, params)
    he2.plot_2d_solution(params.X, params.Y, u_circle, u_final_circle, "Backward Euler")
    
    print("\n=== All tests completed! ===")


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The modular 2D solver separates grid creation, initial conditions, solvers, and plotting into distinct modules. Explain the software engineering benefit of this separation.

??? success "Solution to Exercise 1"
    This separation follows the **single responsibility principle**: each module handles one concern. Benefits include:

    - **Testability**: Each module can be unit-tested independently (e.g., test that `create_2d_grid` produces correct spacing without running any solver).
    - **Reusability**: Initial conditions can be reused across different solvers; plotting functions work with any solution array.
    - **Maintainability**: Adding a new solver requires changes only in `solvers.py`, not in the grid or plotting code.
    - **Extensibility**: New initial conditions, boundary conditions, or visualization methods can be added without touching existing code.

---

**Exercise 2.**
The `get_stability_info` function returns a dictionary with `is_stable_forward`. How would you extend this to also report the maximum stable time step for Forward Euler?

??? success "Solution to Exercise 2"
    Add a computed field for the maximum stable time step:

    $$
    \Delta t_{\max} = \frac{0.5}{D(1/\Delta x^2 + 1/\Delta y^2)}
    $$

    This follows from $r_x + r_y \le 0.5$, i.e., $D\Delta t(1/\Delta x^2 + 1/\Delta y^2) \le 0.5$.

    The modified function would add `"max_stable_dt": 0.5 / (D * (1/dx**2 + 1/dy**2))` and `"min_stable_Nt": int(np.ceil(T / max_stable_dt))` to the returned dictionary. This gives users actionable guidance on how to adjust parameters for stability.

---

**Exercise 3.**
The cross-section analysis plots temperature along $x$ at fixed $y$ and vice versa. For an initial circular pulse centered at $(0.5, 0.5)$, what symmetry should these cross-sections exhibit?

??? success "Solution to Exercise 3"
    For a circular pulse with center $(0.5, 0.5)$ on a square domain, the initial condition has fourfold symmetry: it is symmetric about both $x = 0.5$ and $y = 0.5$.

    The cross-section at $y = 0.5$ should be identical to the cross-section at $x = 0.5$ (rotational symmetry). Both should be symmetric about their respective midpoints. After evolution under the heat equation (which preserves these symmetries with Dirichlet BCs on a square domain), the cross-sections remain symmetric and identical.

    Any asymmetry in the computed cross-sections indicates numerical error, possibly from grid effects or insufficient resolution.

---

**Exercise 4.**
Compare the circular pulse and Gaussian initial conditions after evolution. Which produces a smoother solution, and why does this matter for numerical accuracy?

??? success "Solution to Exercise 4"
    The Gaussian initial condition is infinitely differentiable ($C^\infty$), while the circular pulse has a discontinuity at its boundary (a jump from amplitude to zero).

    After evolution, both solutions become smooth for $t > 0$ (the heat equation is a smoothing operator). However, at early times, the circular pulse produces steep gradients near its boundary that are harder to resolve numerically. This leads to larger spatial discretization errors and potential oscillations with coarse grids.

    The Gaussian solution is smooth from the start, so numerical methods achieve their full theoretical convergence rate immediately. For benchmarking numerical methods, smooth initial conditions are preferred because they allow clean convergence analysis.
