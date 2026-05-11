# Heat Equation 1D (Fundamental Solution)

## Background

Heat Equation 1D Fundamental

Educational script demonstrating heat equation 1d fundamental concepts.

---

## Code

```python
"""
Heat Equation 1D Fundamental

Educational script demonstrating heat equation 1d fundamental concepts.
"""

# ============================================================================
# heat_equation_1d_FUNDAMENTAL_SOLUTION.py
# ============================================================================
import heat_equation_1d as he1
import matplotlib.pyplot as plt
import numpy as np

def refactored_fundamental_solution_v1():
    """
    Refactored version using quick_solve with heat kernel method.
    The "Fundamental Solution" corresponds to the "heat_kernel" method.
    """
    print("=== Method 1: Using wrapper quick_solve with heat kernel ===")
    
    # One-line solution using heat kernel (fundamental solution)
    result = he1.quick_solve(
        initial_condition="step",
        method="cn",  # Crank-Nicolson for numerical solution
        L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01,
        start=0.4, end=0.6, value=1.0,
        plot=False, validate=False  # We'll do custom plotting
    )
    
    # Get the solver and compute heat kernel analytical solution
    solver = result["solver"]
    
    # Get analytical solution using heat kernel (fundamental solution)
    u_analytical = solver.solver.get_analytical_solution("heat_kernel")
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(solver.x, solver.solver.u_initial, "--r", label="Initial Temperature")
    ax.plot(solver.x, u_analytical, label="Final Temperature")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (Fundamental Solution)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


def refactored_fundamental_solution_v2():
    """
    Refactored version using HeatEquation1D class directly with heat kernel.
    """
    print("\n=== Method 2: Using HeatEquation1D class with heat kernel ===")
    
    # Create solver instance with same parameters as original
    solver = he1.HeatEquation1D(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    
    # Set step function initial condition (equivalent to your lambda)
    solver.set_initial_condition("step", start=0.4, end=0.6, value=1.0)
    
    # Get analytical solution using heat kernel method (fundamental solution)
    u_analytical = solver.get_analytical_solution("heat_kernel")
    
    # Create the exact plot from your original code
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(solver.x, solver.u_initial, "--r", label="Initial Temperature")
    ax.plot(solver.x, u_analytical, label="Final Temperature")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (Fundamental Solution)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


def refactored_fundamental_solution_v3():
    """
    Refactored version using pure functions with heat kernel.
    """
    print("\n=== Method 3: Using pure functions with heat kernel ===")
    
    from heat_equation_1d.grid import create_grid
    
    # Create grid with same parameters
    params = create_grid(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    
    # Define initial condition function (your original lambda)
    def step_initial_condition(x):
        return np.where((x >= 0.4) & (x <= 0.6), 1.0, 0.0)
    
    # Get initial condition values
    u_initial = step_initial_condition(params.x)
    
    # Get analytical solution using heat kernel (fundamental solution)
    u_analytical = he1.solve_analytical(
        params.x, params.T, step_initial_condition, 
        params.D, params.L, method="heat_kernel"
    )
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(params.x, u_initial, "--r", label="Initial Temperature")
    ax.plot(params.x, u_analytical, label="Final Temperature")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (Fundamental Solution)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


def refactored_fundamental_solution_v4():
    """
    Refactored version using HeatSolver with method chaining.
    """
    print("\n=== Method 4: Using HeatSolver with method chaining ===")
    
    # Create solver and get heat kernel solution
    solver = he1.HeatSolver(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    solver.set_initial_condition("step", start=0.4, end=0.6, value=1.0)
    
    # Get heat kernel analytical solution
    u_analytical = solver.solver.get_analytical_solution("heat_kernel")
    
    # Create custom plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(solver.x, solver.solver.u_initial, "--r", label="Initial Temperature")
    ax.plot(solver.x, u_analytical, label="Final Temperature")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (Fundamental Solution)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


def compare_analytical_methods():
    """
    Compare all three analytical methods for the same initial condition.
    """
    print("\n=== Comparing All Analytical Methods ===")
    
    # Create solver
    solver = he1.HeatEquation1D(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    solver.set_initial_condition("step", start=0.4, end=0.6, value=1.0)
    
    # Get solutions using all three analytical methods
    u_eigenfunction = solver.get_analytical_solution("eigenfunction")
    u_heat_kernel = solver.get_analytical_solution("heat_kernel")
    u_fourier = solver.get_analytical_solution("fourier")
    
    # Create comparison plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(solver.x, solver.u_initial, "--k", linewidth=2, label="Initial Temperature", alpha=0.7)
    ax.plot(solver.x, u_eigenfunction, "-r", linewidth=2, label="Eigenfunction Expansion")
    ax.plot(solver.x, u_heat_kernel, "--b", linewidth=2, label="Heat Kernel (Fundamental Solution)")
    ax.plot(solver.x, u_fourier, "-.g", linewidth=2, label="Fourier Spectral")
    
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Comparison of Analytical Methods")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()
    
    # Check differences between methods
    diff_eigen_kernel = np.max(np.abs(u_eigenfunction - u_heat_kernel))
    diff_eigen_fourier = np.max(np.abs(u_eigenfunction - u_fourier))
    diff_kernel_fourier = np.max(np.abs(u_heat_kernel - u_fourier))
    
    print(f"Max difference between Eigenfunction and Heat Kernel: {diff_eigen_kernel:.2e}")
    print(f"Max difference between Eigenfunction and Fourier: {diff_eigen_fourier:.2e}")
    print(f"Max difference between Heat Kernel and Fourier: {diff_kernel_fourier:.2e}")


def original_style_exact_match():
    """
    Create exact match to your original code style with minimal changes.
    """
    print("\n=== Exact Match to Original Style ===")
    
    # Your original lambda function
    f = lambda x: np.where((x >= 0.4) & (x <= 0.6), 1.0, 0.0)
    
    # Create solver instance (using default parameters to match your original)
    solver = he1.HeatEquation1D()  # Uses default parameters
    
    # Set custom initial condition using your lambda
    solver.set_initial_condition("custom", func=f)
    
    # Get analytical solution using heat kernel (fundamental solution equivalent)
    u_exact = solver.get_analytical_solution("heat_kernel")
    
    x = solver.x
    u_initial = f(x)
    u = u_exact
    
    # Your exact original plotting code
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(solver.x, f(solver.x), "--r", label="Initial Temperature")
    ax.plot(solver.x, u_exact, label="Final Temperature")  # Using the computed solution
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (Fundamental Solution)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


def demonstrate_heat_kernel_theory():
    """
    Demonstrate the heat kernel (fundamental solution) concept.
    """
    print("\n=== Heat Kernel (Fundamental Solution) Theory Demo ===")
    
    # Create fine grid for smooth visualization
    params = he1.create_grid(L=1.0, T=0.1, Nx=200, Nt=1000, D=0.01)
    
    # Step function initial condition
    def step_initial_condition(x):
        return np.where((x >= 0.4) & (x <= 0.6), 1.0, 0.0)
    
    u_initial = step_initial_condition(params.x)
    
    # Get solution at different times using heat kernel
    times = [0.01, 0.03, 0.05, 0.07, 0.1]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot initial condition
    ax.plot(params.x, u_initial, "--k", linewidth=2, label="Initial (t=0)")
    
    # Plot evolution
    colors = ['blue', 'green', 'orange', 'purple', 'red']
    for i, t in enumerate(times):
        u_t = he1.solve_analytical(
            params.x, t, step_initial_condition, 
            params.D, params.L, method="heat_kernel"
        )
        ax.plot(params.x, u_t, color=colors[i], linewidth=2, 
                label=f"t = {t:.2f}")
    
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Heat Diffusion Evolution Using Fundamental Solution (Heat Kernel)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()
    
    print("The heat kernel shows how an initial temperature distribution")
    print("evolves over time through diffusion. The sharp step function")
    print("gradually smooths out as heat spreads from hot to cold regions.")


if __name__ == "__main__":
    # Run all examples
    refactored_fundamental_solution_v1()
    refactored_fundamental_solution_v2()
    refactored_fundamental_solution_v3()
    refactored_fundamental_solution_v4()
    compare_analytical_methods()
    original_style_exact_match()
    demonstrate_heat_kernel_theory()
```

## Exercises

**Exercise 1.**
Write the heat kernel (fundamental solution) $G(x, \xi, t)$ for the 1D heat equation and explain its physical interpretation as a response to a point source.

??? success "Solution to Exercise 1"
    The heat kernel is

    $$
    G(x, \xi, t) = \frac{1}{\sqrt{4\pi D t}}\exp\!\Bigl(-\frac{(x - \xi)^2}{4Dt}\Bigr)
    $$

    Physically, if a unit amount of heat is concentrated at position $\xi$ at time $t = 0$ (a Dirac delta initial condition $u(x,0) = \delta(x - \xi)$), then $G(x, \xi, t)$ gives the temperature at position $x$ at time $t$. The heat spreads symmetrically around $\xi$ with a Gaussian profile whose width grows as $\sqrt{4Dt}$.

---

**Exercise 2.**
Show that the general solution to the heat equation with initial condition $f(x)$ can be written as a convolution $u(x,t) = \int G(x, \xi, t)\,f(\xi)\,d\xi$.

??? success "Solution to Exercise 2"
    By superposition, if $G(x,\xi,t)$ solves $u_t = Du_{xx}$ with $u(x,0) = \delta(x-\xi)$, then for a general $f$:

    $$
    u(x,t) = \int_{-\infty}^{\infty} G(x,\xi,t)\,f(\xi)\,d\xi
    $$

    solves $u_t = Du_{xx}$ with $u(x,0) = f(x)$, because: (1) each $G(\cdot,\xi,t)f(\xi)\,d\xi$ satisfies the PDE, (2) the integral (superposition) also satisfies the PDE by linearity, and (3) as $t \to 0^+$, $G(x,\xi,t) \to \delta(x-\xi)$, so $u(x,0) = \int \delta(x-\xi)f(\xi)\,d\xi = f(x)$.

---

**Exercise 3.**
Compare the heat kernel method to the eigenfunction expansion method for a step function initial condition. Which gives a smoother approximation at early times?

??? success "Solution to Exercise 3"
    The heat kernel method gives a smoother approximation because the convolution with the Gaussian kernel inherently smooths the initial condition. Even for $t$ very small, the Gaussian width $\sqrt{4Dt}$ provides some smoothing.

    The eigenfunction expansion, by contrast, suffers from the Gibbs phenomenon when truncated at $N$ modes. Near discontinuities, it produces oscillations of about 9% of the jump height that persist regardless of $N$. At early times when the true solution is barely smoothed, the eigenfunction method may show more artifacts.

    However, both methods converge to the same solution. The heat kernel method is better for rough initial data, while the eigenfunction method is more efficient for smooth data where few modes suffice.

---

**Exercise 4.**
If the domain is extended by a factor of 3 (from $[0, L]$ to $[-3L, 3L]$), how does this affect the accuracy of the heat kernel method? What determines the optimal extension factor?

??? success "Solution to Exercise 4"
    Domain extension improves accuracy by reducing the influence of the integration boundaries. The heat kernel $G(x,\xi,t)$ decays as $\exp(-(x-\xi)^2/(4Dt))$. For $x \in [0,L]$ and $\xi$ far outside this range (say $|\xi| > 3L$), the kernel is negligibly small when $3L \gg \sqrt{4DT}$.

    The optimal extension factor ensures that $L_{\text{ext}} \gg \sqrt{4DT}$. For $D = 0.01$ and $T = 0.1$, $\sqrt{4DT} = \sqrt{0.004} \approx 0.063$, so an extension to $[-3, 3]$ (factor of 3) provides ample margin. Increasing the extension factor improves accuracy but increases computation cost.
