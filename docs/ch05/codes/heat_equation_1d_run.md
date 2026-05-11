# Heat Equation 1D (Run)

## Background

Heat Equation 1D Run

Educational script demonstrating heat equation 1d run concepts.

---

## Code

```python
"""
Heat Equation 1D Run

Educational script demonstrating heat equation 1d run concepts.
"""

# ============================================================================
# heat_equation_1d_RUN.py
# ============================================================================
import heat_equation_1d as he1
import numpy as np

def main():
    """Main function that runs all examples with extensive documentation."""
    print("=" * 80)
    print("COMPREHENSIVE HEAT EQUATION SOLVER DEMONSTRATION")
    print("=" * 80)
    print("This script demonstrates three different approaches to solving the 1D heat equation:")
    print("1. Object-oriented class interface")
    print("2. Convenience function approach") 
    print("3. Pure function approach")
    print()
    
    # Run all examples
    example_basic_usage()
    example_method_comparison()
    example_pure_functions()
    example_advanced_features()
    
    print("\n" + "=" * 80)
    print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
    print("=" * 80)

def example_basic_usage():
    """
    Basic usage example with step function using the class interface.
    This demonstrates the most straightforward way to use the solver.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 1: BASIC USAGE WITH CLASS INTERFACE")
    print("=" * 60)
    
    print("Creating HeatEquation1D instance...")
    print("Parameters:")
    print("  - Domain length (L): 1.0")
    print("  - Total time (T): 0.05")
    print("  - Grid points (Nx): 50")
    print("  - Time steps (Nt): 250")
    print("  - Diffusion coefficient (D): 0.01")
    
    # Create and solve using the class interface
    heat = he1.HeatEquation1D(L=1.0, T=0.05, Nx=50, Nt=250, D=0.01)
    
    # Access grid information through the params object
    print(f"\nGrid information:")
    print(f"  - Grid spacing: dx = {heat.params.dx:.4f}")
    print(f"  - Time step: dt = {heat.params.dt:.6f}")
    print(f"  - Stability coefficient: {heat.params.coeff:.3f}")
    print(f"  - Domain: x ∈ [{heat.params.x[0]:.1f}, {heat.params.x[-1]:.1f}]")
    print(f"  - Time: t ∈ [0, {heat.params.T:.3f}]")
    
    # Set initial condition
    print("\nSetting initial condition: step function")
    print("  - Step starts at x = 0.3")
    print("  - Step ends at x = 0.7")
    print("  - Step value = 1.0")
    heat.set_initial_condition("step", start=0.3, end=0.7, value=1.0)
    
    print(f"\nInitial condition statistics:")
    print(f"  - Shape: {heat.u_initial.shape}")
    print(f"  - Min value: {np.min(heat.u_initial):.6f}")
    print(f"  - Max value: {np.max(heat.u_initial):.6f}")
    print(f"  - Mass (integral): {np.trapz(heat.u_initial, heat.x):.6f}")
    
    # Print problem information
    problem_info = heat.info()
    print(f"\nProblem summary:")
    for key, value in problem_info.items():
        if isinstance(value, float):
            print(f"  - {key}: {value:.6f}")
        else:
            print(f"  - {key}: {value}")
    
    # Solve with Crank-Nicolson method
    print("\nSolving with Crank-Nicolson method...")
    solution = heat.solve("cn")
    
    print(f"\nSolution statistics:")
    print(f"  - Shape: {solution.shape}")
    print(f"  - Min value: {np.min(solution):.6f}")
    print(f"  - Max value: {np.max(solution):.6f}")
    print(f"  - Mean value: {np.mean(solution):.6f}")
    print(f"  - Standard deviation: {np.std(solution):.6f}")
    print(f"  - Final mass: {np.trapz(solution, heat.x):.6f}")
    
    # Check mass conservation
    initial_mass = np.trapz(heat.u_initial, heat.x)
    final_mass = np.trapz(solution, heat.x)
    mass_change = abs(final_mass - initial_mass) / initial_mass * 100
    print(f"  - Mass change: {mass_change:.2f}%")
    
    # Validate against analytical solution
    print("\nValidating against analytical solution...")
    try:
        validation = heat.validate_solution("eigenfunction")
        print(f"Validation results:")
        print(f"  - Max absolute error: {validation['max_absolute_error']:.6e}")
        print(f"  - L2 error: {validation['l2_error']:.6e}")
        print(f"  - Relative L2 error: {validation['relative_l2_error']:.6e}")
        print(f"  - Max relative error: {validation['max_relative_error']:.6e}")
    except Exception as e:
        print(f"  - Validation failed: {e}")
    
    # Plot results
    print("\nGenerating plots...")
    try:
        heat.plot(show_analytical=True)
        print("  - Plot created successfully")
    except Exception as e:
        print(f"  - Plot generation failed: {e}")
    
    print("\nBasic usage example completed!")

def example_method_comparison():
    """
    Compare different numerical methods using the convenience function.
    This shows how to compare Forward Euler, Backward Euler, and Crank-Nicolson methods.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 2: METHOD COMPARISON WITH CONVENIENCE FUNCTION")
    print("=" * 60)
    
    print("Using convenience function solve_heat_equation()...")
    print("Parameters:")
    print("  - Initial condition: Gaussian pulse")
    print("  - Method: forward")
    print("  - Domain length (L): 1.0")
    print("  - Total time (T): 0.02")
    print("  - Grid points (Nx): 50")
    print("  - Time steps (Nt): 200")
    print("  - Diffusion coefficient (D): 0.01")
    print("  - Gaussian center: 0.5")
    print("  - Gaussian width: 0.1")
    print("  - Gaussian amplitude: 1.0")
    
    # Use convenience function
    result = he1.solve_heat_equation(
        initial_condition="gaussian",
        method="forward",
        L=1.0, T=0.02, Nx=50, Nt=200, D=0.01,
        center=0.5, width=0.1, amplitude=1.0
    )
    
    print(f"\nConvenience function returned:")
    print(f"  - Keys: {list(result.keys())}")
    
    solver = result["solver"]
    initial_solution = result["u_initial"]
    final_solution = result["u_final"]
    
    print(f"\nInitial solution statistics:")
    print(f"  - Shape: {initial_solution.shape}")
    print(f"  - Max value: {np.max(initial_solution):.6f}")
    print(f"  - Min value: {np.min(initial_solution):.6f}")
    print(f"  - Mass: {np.trapz(initial_solution, result['x']):.6f}")
    
    print(f"\nFinal solution statistics:")
    print(f"  - Shape: {final_solution.shape}")
    print(f"  - Max value: {np.max(final_solution):.6f}")
    print(f"  - Min value: {np.min(final_solution):.6f}")
    print(f"  - Mass: {np.trapz(final_solution, result['x']):.6f}")
    print(f"  - Method used: {result['method']}")
    
    # Compare all methods
    print("\nComparing all numerical methods...")
    try:
        results = solver.compare_all_methods()
        print("Method comparison results:")
        
        for method, solution in results.items():
            if isinstance(solution, np.ndarray):
                print(f"  {method}:")
                print(f"    - Shape: {solution.shape}")
                print(f"    - Max value: {np.max(solution):.6f}")
                print(f"    - Min value: {np.min(solution):.6f}")
                print(f"    - Mass: {np.trapz(solution, result['x']):.6f}")
                
                # Calculate error relative to analytical solution if possible
                try:
                    analytical = solver.get_analytical_solution("eigenfunction")
                    error = np.max(np.abs(solution - analytical))
                    print(f"    - Max error vs analytical: {error:.6e}")
                except:
                    pass
            else:
                print(f"  {method}: {solution}")
        
        # Calculate differences between methods
        method_names = [k for k in results.keys() if isinstance(results[k], np.ndarray)]
        if len(method_names) >= 2:
            print(f"\nMethod differences:")
            for i, method1 in enumerate(method_names):
                for method2 in method_names[i+1:]:
                    if results[method1].shape == results[method2].shape:
                        diff = np.max(np.abs(results[method1] - results[method2]))
                        print(f"  Max difference {method1} vs {method2}: {diff:.6e}")
    
    except Exception as e:
        print(f"  - Method comparison failed: {e}")
    
    # Plot comparison
    print("\nGenerating method comparison plot...")
    try:
        solver.plot_method_comparison()
        print("  - Method comparison plot created successfully")
    except Exception as e:
        print(f"  - Plotting failed: {e}")
    
    print("\nMethod comparison example completed!")

def example_pure_functions():
    """
    Example using pure functions directly.
    This demonstrates the lowest-level interface for maximum control.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 3: PURE FUNCTIONS APPROACH")
    print("=" * 60)
    
    print("Using pure functions for maximum control...")
    print("Parameters:")
    print("  - Domain length (L): 2.0")
    print("  - Total time (T): 0.1")
    print("  - Grid points (Nx): 100")
    print("  - Time steps (Nt): 500")
    print("  - Diffusion coefficient (D): 0.02")
    
    # Create grid using pure function
    print("\nCreating grid with create_grid()...")
    params = he1.create_grid(L=2.0, T=0.1, Nx=100, Nt=500, D=0.02)
    
    print(f"Grid parameters created:")
    print(f"  - dx (spatial step): {params.dx:.6f}")
    print(f"  - dt (time step): {params.dt:.6f}")
    print(f"  - coeff (stability): {params.coeff:.6f}")
    print(f"  - Nx: {params.Nx}")
    print(f"  - Nt: {params.Nt}")
    print(f"  - L: {params.L}")
    print(f"  - T: {params.T}")
    print(f"  - D: {params.D}")
    print(f"  - x range: [{params.x[0]:.3f}, {params.x[-1]:.3f}]")
    
    # Check stability condition
    if params.coeff <= 0.5:
        print(f"  ✓ Stability condition satisfied (coeff = {params.coeff:.3f} ≤ 0.5)")
    else:
        print(f"  ⚠ Stability condition violated (coeff = {params.coeff:.3f} > 0.5)")
    
    # Create initial condition using pure function
    print("\nCreating Gaussian pulse initial condition...")
    print("  - Center: 0.3 (relative position)")
    print("  - Width: 0.2") 
    print("  - Amplitude: 2.0")
    
    try:
        u_init = he1.gaussian_pulse(params.x, center=0.3, width=0.2, amplitude=2.0, L=params.L)
        
        print(f"\nInitial condition statistics:")
        print(f"  - Shape: {u_init.shape}")
        print(f"  - Max value: {np.max(u_init):.6f}")
        print(f"  - Min value: {np.min(u_init):.6f}")
        print(f"  - Integral (mass): {np.trapz(u_init, params.x):.6f}")
        
        # Calculate center of mass
        total_mass = np.trapz(u_init, params.x)
        if total_mass > 1e-12:
            center_of_mass = np.trapz(params.x * u_init, params.x) / total_mass
            print(f"  - Center of mass: {center_of_mass:.6f}")
        
        # Additional analysis
        print(f"\nAdditional analysis:")
        print(f"  - Peak location: x = {params.x[np.argmax(u_init)]:.6f}")
        
        # Full width at half maximum
        fwhm = estimate_fwhm(params.x, u_init)
        print(f"  - Full width at half maximum: {fwhm:.6f}")
        
        # Energy (L2 norm)
        energy = np.sqrt(np.trapz(u_init**2, params.x))
        print(f"  - Energy (L2 norm): {energy:.6f}")
        
        # Now solve using pure functions
        print(f"\nSolving with pure functions...")
        from heat_equation_1d.solvers import solve_crank_nicolson, solve_backward_euler, solve_forward_euler
        
        # Try Crank-Nicolson
        print("  - Solving with Crank-Nicolson...")
        u_final_cn = solve_crank_nicolson(u_init, params.coeff, params.Nt)
        print(f"    Final max: {np.max(u_final_cn):.6f}")
        print(f"    Final mass: {np.trapz(u_final_cn, params.x):.6f}")
        
        # Try Backward Euler  
        print("  - Solving with Backward Euler...")
        u_final_be = solve_backward_euler(u_init, params.coeff, params.Nt)
        print(f"    Final max: {np.max(u_final_be):.6f}")
        print(f"    Final mass: {np.trapz(u_final_be, params.x):.6f}")
        
        # Try Forward Euler (if stable)
        if params.coeff <= 0.5:
            print("  - Solving with Forward Euler...")
            u_final_fe = solve_forward_euler(u_init, params.coeff, params.Nt)
            print(f"    Final max: {np.max(u_final_fe):.6f}")
            print(f"    Final mass: {np.trapz(u_final_fe, params.x):.6f}")
        else:
            print("  - Forward Euler skipped (unstable)")
        
    except Exception as e:
        print(f"Pure function example failed: {e}")
    
    print("\nPure functions example completed!")

def example_advanced_features():
    """
    Demonstrate advanced features and edge cases.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 4: ADVANCED FEATURES AND EDGE CASES")
    print("=" * 60)
    
    print("Testing various initial conditions...")
    
    # Test different initial conditions
    initial_conditions = [
        ("gaussian", {"center": 0.5, "width": 0.1, "amplitude": 1.0}),
        ("step", {"start": 0.2, "end": 0.8, "value": 1.5}),
        ("sine", {"n_modes": 2, "amplitude": 0.8}),
    ]
    
    for ic_name, ic_params in initial_conditions:
        print(f"\nTesting {ic_name} initial condition...")
        try:
            heat = he1.HeatEquation1D(L=1.0, T=0.02, Nx=50, Nt=100, D=0.01)
            heat.set_initial_condition(ic_name, **ic_params)
            
            solution = heat.solve("cn")
            
            print(f"  ✓ Success - Final max: {np.max(solution):.6f}")
            print(f"    Initial mass: {np.trapz(heat.u_initial, heat.x):.6f}")
            print(f"    Final mass: {np.trapz(solution, heat.x):.6f}")
            
            # Try analytical validation
            try:
                validation = heat.validate_solution("eigenfunction")
                print(f"    Max error vs analytical: {validation['max_absolute_error']:.6e}")
            except:
                print(f"    Analytical validation not available")
            
        except Exception as e:
            print(f"  ✗ Failed: {e}")
    
    # Test custom initial condition
    print(f"\nTesting custom initial condition...")
    try:
        def custom_ic(x):
            return np.exp(-((x - 0.5) / 0.1)**2) * np.cos(10 * np.pi * x)
        
        heat = he1.HeatEquation1D(L=1.0, T=0.02, Nx=100, Nt=100, D=0.01)
        heat.set_initial_condition("custom", func=custom_ic)
        
        solution = heat.solve("cn")
        print(f"  ✓ Custom IC success - Final max: {np.max(solution):.6f}")
        
    except Exception as e:
        print(f"  ✗ Custom IC failed: {e}")
    
    # Test stability limits
    print(f"\nTesting stability limits...")
    test_params = [
        {"Nx": 50, "Nt": 1000, "expected": "stable"},   # Small coeff
        {"Nx": 50, "Nt": 50, "expected": "unstable"},   # Large coeff  
        {"Nx": 100, "Nt": 2000, "expected": "stable"},  # Very small coeff
    ]
    
    for params in test_params:
        try:
            heat = he1.HeatEquation1D(L=1.0, T=0.05, Nx=params["Nx"], Nt=params["Nt"], D=0.01)
            coeff = heat.params.coeff
            
            if coeff <= 0.5:
                status = "✓ Stable"
            else:
                status = "⚠ Unstable"
                
            print(f"  Nx={params['Nx']}, Nt={params['Nt']}: coeff={coeff:.3f} - {status}")
            
            # Try to solve with forward method to test stability
            heat.set_initial_condition("gaussian", center=0.5, width=0.1, amplitude=1.0)
            try:
                if coeff <= 0.5:
                    solution = heat.solve("forward")
                    print(f"    Forward Euler succeeded, max value: {np.max(solution):.6f}")
                else:
                    print(f"    Forward Euler skipped (would be unstable)")
            except Exception as e:
                print(f"    Forward Euler failed: {e}")
            
        except Exception as e:
            print(f"  Nx={params['Nx']}, Nt={params['Nt']}: Setup error - {e}")
    
    # Test different analytical methods
    print(f"\nTesting different analytical methods...")
    try:
        heat = he1.HeatEquation1D(L=1.0, T=0.1, Nx=50, Nt=500, D=0.01)
        heat.set_initial_condition("gaussian", center=0.5, width=0.1, amplitude=1.0)
        solution = heat.solve("cn")
        
        analytical_methods = ["eigenfunction", "heat_kernel", "fourier"]
        for method in analytical_methods:
            try:
                analytical = heat.get_analytical_solution(method)
                error = np.max(np.abs(solution - analytical))
                print(f"  {method}: max error = {error:.6e}")
            except Exception as e:
                print(f"  {method}: failed - {e}")
                
    except Exception as e:
        print(f"  Analytical methods test failed: {e}")
    
    print("\nAdvanced features example completed!")

def estimate_fwhm(x, y):
    """Estimate full width at half maximum of a curve."""
    try:
        half_max = np.max(y) / 2
        indices = np.where(y >= half_max)[0]
        if len(indices) > 0:
            return x[indices[-1]] - x[indices[0]]
        return 0.0
    except:
        return 0.0

if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The script uses `np.trapz` to compute mass (integral of $u$ over the domain). Explain the trapezoidal rule and its accuracy for smooth versus discontinuous functions.

??? success "Solution to Exercise 1"
    The trapezoidal rule approximates $\int_a^b f(x)\,dx \approx \Delta x\bigl[\frac{1}{2}f_0 + f_1 + \cdots + f_{N-2} + \frac{1}{2}f_{N-1}\bigr]$ where $\Delta x = (b-a)/(N-1)$.

    For smooth functions, the error is $O(\Delta x^2)$ (second-order). For functions with discontinuities, the error degrades to $O(\Delta x)$ near the jump because the trapezoidal rule cannot accurately capture the area under a step.

    For mass conservation checks, the trapezoidal rule is adequate because the heat equation preserves the integral $\int u\,dx$ (with Neumann BCs) or changes it predictably (with Dirichlet BCs), and the numerical mass change should be small.

---

**Exercise 2.**
The mass change percentage is computed as $|m_f - m_i|/m_i \times 100$. For Dirichlet boundary conditions $u(0) = u(L) = 0$, is mass exactly conserved? Explain.

??? success "Solution to Exercise 2"
    No, mass is not conserved with homogeneous Dirichlet boundary conditions. The boundary condition $u = 0$ at the endpoints acts as a heat sink: heat that reaches the boundary is absorbed. The total mass $\int_0^L u(x,t)\,dx$ decreases monotonically over time.

    The rate of mass loss is governed by the boundary flux: $\frac{d}{dt}\int_0^L u\,dx = D\bigl[\frac{\partial u}{\partial x}\bigr]_0^L = D\bigl[u_x(L,t) - u_x(0,t)\bigr]$. For a centered initial pulse, both boundary fluxes are negative (heat flows out), so mass decreases.

---

**Exercise 3.**
The `estimate_fwhm` function computes the full width at half maximum of the solution profile. How does the FWHM of a Gaussian initial condition evolve under the heat equation?

??? success "Solution to Exercise 3"
    For a Gaussian initial condition $u(x,0) = A\exp(-(x-x_c)^2/(2w^2))$, the solution remains Gaussian:

    $$
    u(x,t) = \frac{A w}{\sqrt{w^2 + 2Dt}}\exp\!\Bigl(-\frac{(x-x_c)^2}{2(w^2 + 2Dt)}\Bigr)
    $$

    The effective width is $w_{\text{eff}}(t) = \sqrt{w^2 + 2Dt}$. The FWHM of a Gaussian is $2\sqrt{2\ln 2}\,w_{\text{eff}}$, so

    $$
    \text{FWHM}(t) = 2\sqrt{2\ln 2}\,\sqrt{w^2 + 2Dt}
    $$

    The FWHM grows as $\sqrt{t}$ for large $t$, reflecting the diffusive broadening.

---

**Exercise 4.**
The script tests different initial conditions (Gaussian, step, sine). Rank them by expected numerical accuracy for Crank-Nicolson with fixed $N_x = 50$, and explain why.

??? success "Solution to Exercise 4"
    Ranked from most to least accurate:

    1. **Sine wave**: This is an eigenfunction of the heat equation, so Crank-Nicolson needs only to track a single mode's exponential decay. The error is purely from time discretization.
    2. **Gaussian**: Smooth and infinitely differentiable, so the spatial discretization achieves its theoretical $O(\Delta x^2)$ rate without complications.
    3. **Step function**: Discontinuous, causing large spatial errors near the jumps. The solution has high-frequency content that decays quickly but is poorly resolved at early times. Errors near the discontinuity dominate.

    This ranking reflects the general principle that smoother initial data produces more accurate numerical solutions.
