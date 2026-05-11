# Density Recovery Fast Fourier Transform (Grzelak)

## Background

Normal density recovery using Fourier Transform.

Demonstrates density recovery from a characteristic function using
Fast Fourier Transform for normal distribution.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.

---

## Code

```python
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
```


## Exercises

**Exercise 1.**
The FFT-based density recovery uses $f(x) = \frac{du}{\pi}\text{Re}[\text{FFT}(\varphi(u)e^{-ibu})]$ with boundary correction. Explain the role of the boundary correction term.

??? success "Solution to Exercise 1"
    The trapezoidal rule approximation of $\int_0^{u_{\max}} e^{-iux}\varphi(u)du$ treats the endpoints specially: the first and last values get weight $1/2$. The boundary correction $\phi_{\text{boundary}} = \frac{1}{2}(e^{-ix u_0}\varphi(u_0) + e^{-ix u_{\max}}\varphi(u_{\max}))$ subtracts the double-counted endpoint contributions from the FFT result, converting the sum from a rectangle rule to a proper trapezoidal rule.

---

**Exercise 2.**
The grid parameters are $u_{\max} = 20$ and $N = 2^8 = 256$. Compute the frequency spacing $du$ and the corresponding spatial resolution $dx = 2\pi/(N \cdot du)$.

??? success "Solution to Exercise 2"
    $du = u_{\max}/N = 20/256 = 0.078125$. $dx = 2\pi/(N \cdot du) = 2\pi/20 = 0.3142$. The spatial grid covers $[b, b + N \cdot dx]$ where $b = \min(x)$. For $x \in [-8, 8]$, $N \cdot dx = 256 \times 0.314 = 80.4$, which is more than sufficient.

---

**Exercise 3.**
Cubic interpolation is used to evaluate the recovered density at arbitrary $x$ points. Why is interpolation necessary rather than evaluating the FFT result directly?

??? success "Solution to Exercise 3"
    The FFT produces density values on a specific grid $x_k = b + k \cdot dx$ determined by the frequency parameters. The desired evaluation points $x$ generally do not coincide with this grid. Cubic interpolation maps the FFT output to arbitrary points with $O(dx^4)$ accuracy, which is consistent with the underlying trapezoidal quadrature accuracy.

---

**Exercise 4.**
For the standard normal, $u_{\max} = 20$ is sufficient because $|\varphi(u)| = e^{-u^2/2} < 10^{-87}$ at $u = 20$. Estimate the required $u_{\max}$ for a Cauchy distribution with CF $\varphi(u) = e^{-|u|}$.

??? success "Solution to Exercise 4"
    For the Cauchy CF: $|\varphi(u)| = e^{-|u|}$. To achieve $|\varphi(u_{\max})| < 10^{-8}$: $e^{-u_{\max}} < 10^{-8}$, giving $u_{\max} > 8\ln 10 \approx 18.4$. So $u_{\max} = 20$ suffices. However, the Cauchy density has heavy tails requiring a wider spatial domain. With $N = 256$ and $u_{\max} = 20$: $dx = 0.314$, giving spatial range $\approx 80$, which captures the Cauchy tails adequately.