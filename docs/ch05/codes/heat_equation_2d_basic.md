# Heat Equation 2D (Basic)

## Background

Heat Equation 2D Basic

Educational script demonstrating heat equation 2d basic concepts.

---

## Code

```python
"""
Heat Equation 2D Basic

Educational script demonstrating heat equation 2d basic concepts.
"""

# ============================================================================
# heat_equation_2d_BASIC.py
# ============================================================================
import heat_equation_2d as he2


# Example usage
def main():
    """Main example demonstrating 2D heat equation solver."""
    print("=== 2D Heat Equation Solver Example ===\n")
    
    # Create grid - smaller for faster computation
    params = he2.create_2d_grid(Lx=1.0, Ly=1.0, T=0.02, Nx=30, Ny=30, Nt=200, D=0.01)
    
    print(f"Grid: {params.Nx}×{params.Ny}, dt={params.dt:.4f}")
    print(f"Stability: rx+ry = {params.rx+params.ry:.3f}")
    print()
    
    # Test 1: Step function
    print("Test 1: Step function initial condition")
    u_step = he2.step_function_2d(params.X, params.Y, x_range=(0.4, 0.6), y_range=(0.4, 0.6))
    
    results_step = he2.compare_2d_methods(u_step, params)
    he2.plot_method_comparison_2d(params.X, params.Y, u_step, results_step)
    
    # Test 2: Gaussian pulse
    print("\nTest 2: Gaussian pulse initial condition")
    u_gauss = he2.gaussian_2d(params.X, params.Y, center=(0.3, 0.7), width=(0.05, 0.08))
    
    # Just test one method for the Gaussian
    u_final = he2.solve_crank_nicolson_2d(u_gauss, params)
    he2.plot_2d_solution(params.X, params.Y, u_gauss, u_final, "Crank-Nicolson")
    
    # Test 3: Multiple hotspots
    print("\nTest 3: Multiple hotspots")
    u_multi = (he2.gaussian_2d(params.X, params.Y, (0.3, 0.3), (0.05, 0.05), 1.0) +
               he2.gaussian_2d(params.X, params.Y, (0.7, 0.7), (0.08, 0.05), 0.8) +
               he2.gaussian_2d(params.X, params.Y, (0.3, 0.7), (0.06, 0.08), 1.2))
    
    u_final_multi = he2.solve_backward_euler_2d(u_multi, params)
    he2.plot_2d_solution(params.X, params.Y, u_multi, u_final_multi, "Backward Euler")
    
    print("\n=== All tests completed! ===")


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
For a 2D step function on $[0.4, 0.6] \times [0.4, 0.6]$ with $D = 0.01$ and $T = 0.02$, describe qualitatively how the temperature profile evolves. Does the heated region remain rectangular?

??? success "Solution to Exercise 1"
    At $t = 0$, the temperature is 1 inside the square $[0.4, 0.6]^2$ and 0 outside. As time progresses, heat diffuses outward in all directions equally. The sharp rectangular boundary smooths into a rounded profile because the corners of the rectangle have the highest curvature, causing the fastest diffusion there.

    By $t = 0.02$, the profile resembles a smoothed bump that is nearly circular (for a square initial condition on a square domain). The rectangular shape is lost because corners diffuse faster than edges, and the characteristic diffusion length $\sqrt{4DT} = \sqrt{0.0008} \approx 0.028$ is comparable to the initial patch size.

---

**Exercise 2.**
The code uses `compare_2d_methods` to compare Forward Euler, Backward Euler, Crank-Nicolson, and ADI. Rank these methods by expected accuracy for the given parameters.

??? success "Solution to Exercise 2"
    For $N_x = N_y = 30$, $N_t = 200$, $D = 0.01$, $T = 0.02$: $r_x + r_y \approx 0.024$, well within the stability limit.

    Expected accuracy ranking (best to worst):

    1. **Crank-Nicolson**: $O(\Delta t^2 + \Delta x^2 + \Delta y^2)$
    2. **ADI**: Second-order in time and space (similar to CN but with splitting error)
    3. **Forward Euler**: $O(\Delta t + \Delta x^2 + \Delta y^2)$
    4. **Backward Euler**: $O(\Delta t + \Delta x^2 + \Delta y^2)$ (same order as FE but with more numerical diffusion)

    In practice, CN and ADI produce nearly identical results, and both significantly outperform the first-order methods for this problem.

---

**Exercise 3.**
Why does the code create a multi-hotspot initial condition by summing three Gaussians? Is the result an exact solution to any PDE?

??? success "Solution to Exercise 3"
    The code sums three Gaussians to model a physically motivated scenario: multiple localized heat sources at different positions, intensities, and widths. The sum is simply a superposition of the individual Gaussians.

    This initial condition is not itself a solution to any simple PDE, but because the heat equation is linear, the solution at time $t$ is the sum of the individual Gaussian evolutions. Each Gaussian broadens independently as $\sigma_i(t) = \sqrt{\sigma_{i,0}^2 + 2Dt}$ and reduces in amplitude accordingly.

---

**Exercise 4.**
The Backward Euler method is used for the multiple hotspots test. Explain why this choice is robust for production use, even though it is only first-order in time.

??? success "Solution to Exercise 4"
    Backward Euler is robust because:

    1. **Unconditional stability**: No time-step restriction, so the user can choose $\Delta t$ based on accuracy requirements rather than stability constraints.
    2. **Damping of high frequencies**: Numerical diffusion smooths out high-frequency oscillations that might arise from rough initial conditions.
    3. **Reliable convergence**: The sparse linear system always has a unique solution (the matrix is positive definite).
    4. **Monotonicity**: The solution preserves non-negativity, which is physically correct for temperature.

    For production code where robustness matters more than optimal accuracy, Backward Euler is a safe default. For higher accuracy, one would switch to Crank-Nicolson.
