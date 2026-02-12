# ============================================================================
# heat_equation_1d_FFT.py
# ============================================================================
import heat_equation_1d as he1
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def fft_method_simple():
    """
    Simple FFT method using the package's built-in functionality.
    """
    print("=== FFT Spectral Method ===")
    
    # Create solver instance
    solver = he1.HeatEquation1D(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    
    # Set step function initial condition
    solver.set_initial_condition("step", start=0.4, end=0.6, value=1.0)
    
    # Get analytical solution using FFT spectral method
    u_analytical_fft = solver.get_analytical_solution("fourier")
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(solver.x, solver.u_initial, "--r", linewidth=2, label="Initial Temperature")
    ax.plot(solver.x, u_analytical_fft, "-b", linewidth=2, label="FFT Spectral Solution")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (FFT Spectral Method)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()

def custom_fft_implementation():
    """
    Custom FFT implementation showing the mathematical details.
    """
    print("=== Custom FFT Implementation ===")
    
    # Parameters
    L = 1.0
    T = 0.1
    D = 0.01
    Nx = 128  # Use power of 2 for efficient FFT
    
    # Spatial grid
    x = np.linspace(0, L, Nx)
    dx = x[1] - x[0]
    
    # Initial condition - step function
    u_initial = np.where((x >= 0.4) & (x <= 0.6), 1.0, 0.0)
    
    # Extended domain for periodicity (key for FFT)
    L_ext = 3 * L  # Extend domain to reduce boundary effects
    Nx_ext = 2**int(np.ceil(np.log2(5 * Nx)))  # FFT-friendly size
    x_ext = np.linspace(-L_ext, L_ext, Nx_ext)
    dx_ext = x_ext[1] - x_ext[0]
    
    # Evaluate initial condition on extended domain
    u_ext = np.zeros_like(x_ext)
    mask = (x_ext >= 0.4) & (x_ext <= 0.6)
    u_ext[mask] = 1.0
    
    # FFT of initial condition
    u_hat = np.fft.fft(u_ext)
    
    # Frequency domain grid
    freqs = np.fft.fftfreq(Nx_ext, d=dx_ext)  # frequencies in cycles per unit length
    
    # Apply heat equation evolution in frequency domain
    # The heat equation in Fourier space: du_hat/dt = -4*pi^2*D*k^2*u_hat
    # Solution: u_hat(k,t) = u_hat(k,0) * exp(-4*pi^2*D*k^2*t)
    filter_decay = np.exp(-4 * np.pi**2 * D * freqs**2 * T)
    u_hat_final = u_hat * filter_decay
    
    # Inverse FFT to get solution
    u_final_ext = np.fft.ifft(u_hat_final).real
    
    # Interpolate back to original grid
    interp = interpolate.interp1d(x_ext, u_final_ext, kind='cubic', 
                                 fill_value="extrapolate", bounds_error=False)
    u_final = interp(x)
    
    # Create the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Left plot: Solution
    ax1.plot(x, u_initial, "--r", linewidth=2, label="Initial Temperature")
    ax1.plot(x, u_final, "-b", linewidth=2, label="FFT Solution")
    ax1.set_xlabel("Position (x)")
    ax1.set_ylabel("Temperature (u)")
    ax1.set_title("Custom FFT Implementation")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Right plot: Frequency domain
    ax2.semilogy(freqs[:Nx_ext//2], np.abs(u_hat[:Nx_ext//2]), "-g", 
                linewidth=2, label="Initial Spectrum")
    ax2.semilogy(freqs[:Nx_ext//2], np.abs(u_hat_final[:Nx_ext//2]), "-b", 
                linewidth=2, label="Final Spectrum")
    ax2.semilogy(freqs[:Nx_ext//2], filter_decay[:Nx_ext//2], "--r", 
                linewidth=2, label="Decay Filter")
    ax2.set_xlabel("Frequency (cycles/unit)")
    ax2.set_ylabel("Magnitude")
    ax2.set_title("Frequency Domain Evolution")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    return x, u_initial, u_final

def compare_all_methods():
    """
    Compare FFT spectral method with other analytical methods.
    """
    print("=== Comparing All Analytical Methods ===")
    
    # Create solver
    solver = he1.HeatEquation1D(L=1.0, T=0.1, Nx=100, Nt=1000, D=0.01)
    solver.set_initial_condition("step", start=0.4, end=0.6, value=1.0)
    
    # Get solutions using all three analytical methods
    u_eigenfunction = solver.get_analytical_solution("eigenfunction")
    u_heat_kernel = solver.get_analytical_solution("heat_kernel")
    u_fft = solver.get_analytical_solution("fourier")
    
    # Create comparison plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Left plot: All methods
    ax1.plot(solver.x, solver.u_initial, "--k", linewidth=2, label="Initial", alpha=0.7)
    ax1.plot(solver.x, u_eigenfunction, "-r", linewidth=2, label="Eigenfunction")
    ax1.plot(solver.x, u_heat_kernel, "--b", linewidth=2, label="Heat Kernel")
    ax1.plot(solver.x, u_fft, "-.g", linewidth=2, label="FFT Spectral")
    ax1.set_xlabel("Position (x)")
    ax1.set_ylabel("Temperature (u)")
    ax1.set_title("Comparison of Analytical Methods")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Right plot: Differences
    diff_fft_eigen = np.abs(u_fft - u_eigenfunction)
    diff_fft_kernel = np.abs(u_fft - u_heat_kernel)
    
    ax2.semilogy(solver.x, diff_fft_eigen, "-r", linewidth=2, 
                label=f"FFT vs Eigenfunction (max: {np.max(diff_fft_eigen):.2e})")
    ax2.semilogy(solver.x, diff_fft_kernel, "-b", linewidth=2, 
                label=f"FFT vs Heat Kernel (max: {np.max(diff_fft_kernel):.2e})")
    ax2.set_xlabel("Position (x)")
    ax2.set_ylabel("Absolute Difference")
    ax2.set_title("Differences Between Methods")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    print(f"Max difference FFT vs Eigenfunction: {np.max(diff_fft_eigen):.2e}")
    print(f"Max difference FFT vs Heat Kernel: {np.max(diff_fft_kernel):.2e}")

def fft_time_evolution():
    """
    Show time evolution using FFT method.
    """
    print("=== FFT Time Evolution ===")
    
    # Parameters
    L = 1.0
    D = 0.01
    Nx = 128
    
    # Create spatial grid
    x = np.linspace(0, L, Nx)
    
    # Initial condition function
    def step_initial_condition(x):
        return np.where((x >= 0.4) & (x <= 0.6), 1.0, 0.0)
    
    # Time points for evolution
    times = [0.0, 0.02, 0.05, 0.08, 0.1]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = ['black', 'blue', 'green', 'orange', 'red']
    
    for i, t in enumerate(times):
        if t == 0:
            u_t = step_initial_condition(x)
            ax.plot(x, u_t, "--", color=colors[i], linewidth=2, 
                   label=f"t = {t:.2f} (Initial)")
        else:
            # Use FFT spectral method for each time
            u_t = he1.solve_analytical(x, t, step_initial_condition, D, L, method="fourier")
            ax.plot(x, u_t, "-", color=colors[i], linewidth=2, 
                   label=f"t = {t:.2f}")
    
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Heat Diffusion Evolution Using FFT Spectral Method")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()

def original_style_fft():
    """
    Create exact match to original style using FFT method.
    """
    print("=== Original Style with FFT Method ===")
    
    # Original lambda function
    f = lambda x: np.where((x >= 0.4) & (x <= 0.6), 1.0, 0.0)
    
    # Create solver instance
    solver = he1.HeatEquation1D()
    
    # Set custom initial condition using the lambda function
    solver.set_initial_condition("custom", func=f)
    
    # Get analytical solution using FFT spectral method
    u_exact = solver.get_analytical_solution("fourier")
    
    x = solver.x
    u_initial = f(x)
    u = u_exact
    
    # Original plotting code with FFT
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(solver.x, f(solver.x), "--r", label="Initial Temperature")
    ax.plot(solver.x, u_exact, label="Final Temperature")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Temperature (u)")
    ax.set_title("Final Temperature Distribution (FFT Spectral Method)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()

def print_fft_theory():
    """
    Print the theory behind FFT spectral method.
    """
    print("\n" + "="*60)
    print("FFT SPECTRAL METHOD THEORY")
    print("="*60)
    print("""
The FFT spectral method solves the heat equation in frequency domain:

1. Heat equation: du/dt = D * d2u/dx2

2. Fourier transform: u_hat(k,t) = FFT[u(x,t)]

3. In frequency domain: du_hat/dt = -4*pi^2*D*k^2*u_hat

4. Solution: u_hat(k,t) = u_hat(k,0) * exp(-4*pi^2*D*k^2*t)

5. Inverse FFT: u(x,t) = IFFT[u_hat(k,t)]

ADVANTAGES:
- Spectral accuracy (exponential convergence for smooth solutions)
- Natural handling of periodic boundary conditions
- Efficient for smooth initial conditions

LIMITATIONS:
- Assumes periodic boundary conditions
- Less effective for discontinuous initial conditions
- Requires extended domain to minimize boundary effects
    """)
    print("="*60)

if __name__ == "__main__":
    """
    Main execution - run all FFT examples with proper encoding.
    """
    print("Starting FFT Heat Equation Solutions...")
    print("="*60)
    
    try:
        # Run all FFT examples
        fft_method_simple()
        custom_fft_implementation()
        compare_all_methods()
        fft_time_evolution()
        original_style_fft()
        print_fft_theory()
        
        print("\nAll FFT examples completed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your heat_equation_1d package installation.")