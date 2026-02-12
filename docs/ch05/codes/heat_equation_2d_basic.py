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