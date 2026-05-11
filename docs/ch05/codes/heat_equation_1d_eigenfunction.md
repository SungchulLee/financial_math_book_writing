# Heat Equation 1D (Eigenfunction Expansion)

## Background

Heat Equation 1D Eigenfunction

Educational script demonstrating heat equation 1d eigenfunction concepts.

---

## Code

```python
"""
Heat Equation 1D Eigenfunction

Educational script demonstrating heat equation 1d eigenfunction concepts.
"""

# ============================================================================
# heat_equation_1d_EIGENFUNCTION_EXPANSION.py
# ============================================================================
import heat_equation_1d as he1
import numpy as np
import matplotlib.pyplot as plt

def refactored_example_v1():
    """Refactored version using the wrapper's quick_solve function."""
    print("=== Method 1: Using wrapper quick_solve ===")
    
    # One-line solution with step function initial condition
    result = he1.quick_solve(
        initial_condition="step",
        method="cn",  # Crank-Nicolson
        L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01,
        start=0.4, end=0.6, value=1.0,
        plot=True, validate=True
    )
    
    print(f"Max absolute error: {result['error_summary']['max_absolute_error']:.2e}")
    print(f"L2 error: {result['error_summary']['l2_error']:.2e}")


def refactored_example_v2():
    """Refactored version using the main HeatEquation1D class."""
    print("\n=== Method 2: Using HeatEquation1D class directly ===")
    
    # Create solver instance
    solver = he1.HeatEquation1D(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    
    # Set step function initial condition
    solver.set_initial_condition("step", start=0.4, end=0.6, value=1.0)
    
    # Solve using Crank-Nicolson
    u_numerical = solver.solve("cn")
    
    # Get analytical solution
    u_analytical = solver.get_analytical_solution("eigenfunction")
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(solver.x, solver.u_initial, "--r", linewidth=2, label="Initial Temperature")
    ax.plot(solver.x, u_analytical, "-b", linewidth=2, label="Analytical Solution")
    ax.plot(solver.x, u_numerical, "og", markersize=4, alpha=0.7, label="Numerical Solution")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (Eigenfunction Expansion)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()
    
    # Validate the solution
    validation = solver.validate_solution("eigenfunction")
    print(f"Max absolute error: {validation['max_absolute_error']:.2e}")
    print(f"L2 error: {validation['l2_error']:.2e}")


def refactored_example_v3():
    """Refactored version using pure functions."""
    print("\n=== Method 3: Using pure functions ===")
    
    # Create grid
    params = he1.create_grid(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    
    # Define initial condition function
    def step_initial_condition(x):
        return np.where((x >= 0.4) & (x <= 0.6), 1.0, 0.0)
    
    # Get initial condition values
    u_initial = step_initial_condition(params.x)
    
    # Solve numerically
    u_numerical = he1.solve_crank_nicolson(u_initial, params.coeff, params.Nt)
    
    # Get analytical solution
    u_analytical = he1.solve_analytical(
        params.x, params.T, step_initial_condition, 
        params.D, params.L, method="eigenfunction"
    )
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(params.x, u_initial, "--r", linewidth=2, label="Initial Temperature")
    ax.plot(params.x, u_analytical, "-b", linewidth=2, label="Analytical Solution")
    ax.plot(params.x, u_numerical, "og", markersize=4, alpha=0.7, label="Numerical Solution")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (Eigenfunction Expansion)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()
    
    # Calculate errors
    abs_error = np.abs(u_numerical - u_analytical)
    max_error = np.max(abs_error)
    l2_error = np.sqrt(np.trapz(abs_error**2, params.x))
    
    print(f"Max absolute error: {max_error:.2e}")
    print(f"L2 error: {l2_error:.2e}")


def refactored_example_v4():
    """Refactored version using the wrapper's HeatSolver with method chaining."""
    print("\n=== Method 4: Using HeatSolver with method chaining ===")
    
    # Solve with method chaining
    solver = (he1.HeatSolver(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
              .set_initial_condition("step", start=0.4, end=0.6, value=1.0)
              .solve("cn"))
    solver.plot(show_analytical=True)
    validation = solver.validate("eigenfunction")
    print(f"Validation results:")
    print(f"  - Max absolute error: {validation['max_absolute_error']:.6e}")
    print(f"  - L2 error: {validation['l2_error']:.6e}")
    print(f"  - Relative L2 error: {validation['relative_l2_error']:.6e}")
    print(f"  - Max relative error: {validation['max_relative_error']:.6e}")


def original_style_plot():
    """Create a plot that matches your original style exactly."""
    print("\n=== Creating plot matching original style ===")
    
    # Create solver and get solutions
    solver = he1.HeatEquation1D(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    solver.set_initial_condition("step", start=0.4, end=0.6, value=1.0)
    
    # Get analytical solution (this is what you were trying to do)
    u_analytical = solver.get_analytical_solution("eigenfunction")
    
    # Create the exact plot from your original code
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(solver.x, solver.u_initial, "--r", label="Initial Temperature")
    ax.plot(solver.x, u_analytical, label="Final Temperature")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (Eigenfunction Expansion)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


def comprehensive_example():
    """Comprehensive example showing all methods comparison."""
    print("\n=== Comprehensive Example: All Methods vs Analytical ===")
    
    from heat_equation_1d.wrapper import benchmark_methods
    
    # Compare all numerical methods against analytical solution
    results = benchmark_methods(
        initial_condition="step",
        L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01,
        start=0.4, end=0.6, value=1.0
    )
    
    print("\nMethod Comparison Results:")
    for method, metrics in results["validation"].items():
        print(f"\n{method.replace('_', ' ').title()}:")
        print(f"  Max Absolute Error: {metrics['max_abs_error']:.2e}")
        print(f"  L2 Error: {metrics['l2_error']:.2e}")
        print(f"  Max Relative Error: {metrics['max_rel_error']:.2e}")


if __name__ == "__main__":
    # Run all examples
    refactored_example_v1()
    refactored_example_v2() 
    refactored_example_v3()
    refactored_example_v4()
    original_style_plot()
    comprehensive_example()
```

## Exercises

**Exercise 1.**
For the eigenfunction expansion of the heat equation with a step function $f(x) = 1$ on $[0.4, 0.6]$ and $L = 1$, derive the Fourier coefficient $A_n$.

??? success "Solution to Exercise 1"
    $$
    A_n = \frac{2}{L}\int_0^L f(x)\sin(n\pi x/L)\,dx = 2\int_{0.4}^{0.6}\sin(n\pi x)\,dx
    $$

    $$
    = 2\left[-\frac{\cos(n\pi x)}{n\pi}\right]_{0.4}^{0.6} = \frac{2}{n\pi}\bigl[\cos(0.4 n\pi) - \cos(0.6 n\pi)\bigr]
    $$

    Using the product-to-sum formula: $\cos A - \cos B = 2\sin\!\bigl(\frac{A+B}{2}\bigr)\sin\!\bigl(\frac{B-A}{2}\bigr)$, we get $A_n = \frac{4}{n\pi}\sin(0.5 n\pi)\sin(0.1 n\pi)$.

---

**Exercise 2.**
How many Fourier modes $N$ are needed for the eigenfunction expansion to approximate the step function initial condition to within $L^\infty$ error of approximately 5%?

??? success "Solution to Exercise 2"
    For a step function, the Gibbs phenomenon causes an overshoot of about 9% regardless of $N$. However, away from the discontinuity, the error decreases as $N$ increases. The partial sum approximation error away from discontinuities scales as $O(1/N)$.

    For 5% accuracy in the $L^\infty$ sense including boundary effects, we need $N \approx 100$ or more. Due to the Gibbs phenomenon at discontinuities, the $L^\infty$ error cannot be reduced below approximately 9% of the jump height using truncated Fourier series. Using $N = 100$ modes provides good accuracy in the interior while accepting the Gibbs oscillation at the edges.

---

**Exercise 3.**
Compare the `quick_solve` wrapper approach to the direct `HeatEquation1D` class approach. What are the trade-offs in terms of flexibility versus convenience?

??? success "Solution to Exercise 3"
    The `quick_solve` function is a one-call convenience: it creates the solver, sets the initial condition, solves, optionally validates, and optionally plots. It is ideal for quick exploratory work.

    The `HeatEquation1D` class offers more flexibility: you can solve with different methods without re-creating the object, access intermediate states, compare methods, and perform custom analysis. The class is better for systematic studies (convergence, stability) where you need to reuse the same setup with variations.

---

**Exercise 4.**
After solving with Crank-Nicolson and validating against the eigenfunction expansion, the max absolute error is $3.2 \times 10^{-4}$. If you double $N_x$ (keeping the same $\alpha$ by adjusting $N_t$), what error do you expect for a second-order method?

??? success "Solution to Exercise 4"
    For a second-order method, the error scales as $O(\Delta x^2)$. Doubling $N_x$ halves $\Delta x$, so $\Delta x^2$ is quartered. The expected error is

    $$
    E_{\text{new}} \approx \frac{3.2 \times 10^{-4}}{4} = 8.0 \times 10^{-5}
    $$

    To maintain the same $\alpha = D\Delta t/\Delta x^2$ with halved $\Delta x$, we need $\Delta t$ quartered, hence $N_t$ quadrupled. This fourfold increase in time steps combined with doubled spatial points makes the refined computation about 8 times more expensive.
