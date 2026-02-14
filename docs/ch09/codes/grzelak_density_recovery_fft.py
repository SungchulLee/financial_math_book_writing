# -*- coding: utf-8 -*-
"""
Normal density recovery using Fourier Transform.

Demonstrates density recovery from a characteristic function using
Fast Fourier Transform for normal distribution.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.fft as fft
import scipy.interpolate as interpolate


# =============================================================================
# 1. Core Computation
# =============================================================================

def recover_density(characteristic_func, x, num_grid_points=8192):
    """
    Recover probability density from characteristic function using FFT.

    Parameters
    ----------
    characteristic_func : callable
        Characteristic function phi(u) = E[exp(i*u*X)].
    x : ndarray
        Points at which to evaluate density.
    num_grid_points : int, optional
        Number of grid points for FFT (default: 8192, power of 2).

    Returns
    -------
    density : ndarray
        Recovered density values at points x.
    """
    im = np.complex(0.0, 1.0)  # imaginary unit

    # Specification of grid for u
    u_max = 20.0
    du = u_max / num_grid_points
    u = np.linspace(0, num_grid_points - 1, num_grid_points) * du

    # Grid for x
    b = np.min(x)
    dx = 2.0 * np.pi / (num_grid_points * du)
    x_grid = b + np.linspace(0, num_grid_points - 1, num_grid_points) * dx

    phi = np.exp(-im * b * u) * characteristic_func(u)

    gamma_1 = np.exp(-im * x_grid * u[0]) * characteristic_func(u[0])
    gamma_2 = np.exp(-im * x_grid * u[-1]) * characteristic_func(u[-1])

    phi_boundary = 0.5 * (gamma_1 + gamma_2)

    f_xi = du / np.pi * np.real(fft.fft(phi) - phi_boundary)

    f_interp = interpolate.interp1d(x_grid, f_xi, kind='cubic')

    return f_interp(x)


# =============================================================================
# 2. Visualization
# =============================================================================

def plot_density_recovery(x, f_exact, f_recovered):
    """
    Plot exact vs recovered density.

    Parameters
    ----------
    x : ndarray
        Domain points.
    f_exact : ndarray
        Exact density values.
    f_recovered : ndarray
        Recovered density values.
    """
    plt.figure(1, figsize=(10, 6))
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("$f_X(x)$")
    plt.plot(x, f_exact, '-r', label='Exact')
    plt.plot(x, f_recovered, '--b', label='Recovered')
    plt.legend()
    plt.tight_layout()


# =============================================================================
# 3. Main
# =============================================================================

def main():
    """Recover density from characteristic function for normal distribution."""
    im = np.complex(0.0, 1.0)  # imaginary unit

    # ===== Normal Distribution Parameters =====
    mu = 0.0  # Mean
    sigma = 1.0  # Standard deviation

    # Define characteristic function for normal distribution
    def characteristic_func_normal(u):
        """Characteristic function of N(mu, sigma^2)."""
        return np.exp(im * mu * u - 0.5 * sigma ** 2.0 * u ** 2.0)

    # Domain for density
    x = np.linspace(-8.0, 8.0, 100)
    f_exact = st.norm.pdf(x, mu, sigma)

    # Recovered density via FFT
    f_recovered = recover_density(characteristic_func_normal, x, 2 ** 8)

    plot_density_recovery(x, f_exact, f_recovered)
    plt.show()


if __name__ == "__main__":
    main()
