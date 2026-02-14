"""
Monte Carlo paths for the CIR interest rate process.

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak
"""
import numpy as np
import matplotlib.pyplot as plt


def generate_paths_cir_euler(num_paths, num_steps, T, lmbda, r0, theta, gamma):
    """
    Generate CIR process paths using Euler scheme.

    Parameters
    ----------
    num_paths : int
        Number of simulation paths
    num_steps : int
        Number of time steps
    T : float
        Time to maturity
    lmbda : float
        Mean reversion speed
    r0 : float
        Initial interest rate
    theta : float
        Long-term mean
    gamma : float
        Volatility parameter

    Returns
    -------
    dict
        Dictionary with keys 'time' and 'R' containing time grid and rate paths
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = T / float(num_steps)
    for i in range(0, num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = (r[:, i] + lmbda * (theta - r[:, i]) * dt +
                       gamma * np.sqrt(r[:, i]) * (w[:, i + 1] - w[:, i]))

        # Truncated boundary condition
        r[:, i + 1] = np.maximum(r[:, i + 1], 0.0)
        time[i + 1] = time[i] + dt

    paths = {"time": time, "R": r}
    return paths


def plot_lambda_effect(lmbda_vec, num_paths, num_steps, T, r0, theta, gamma):
    """
    Plot effect of mean reversion speed on CIR paths.

    Parameters
    ----------
    lmbda_vec : list
        List of lambda values to test
    num_paths : int
        Number of paths per lambda
    num_steps : int
        Number of time steps
    T : float
        Time to maturity
    r0 : float
        Initial rate
    theta : float
        Long-term mean
    gamma : float
        Volatility
    """
    plt.figure(1)
    legend = []
    for lmbda_temp in lmbda_vec:
        np.random.seed(2)
        paths = generate_paths_cir_euler(num_paths, num_steps, T, lmbda_temp,
                                         r0, theta, gamma)
        legend.append('lambda={0}'.format(lmbda_temp))
        time_grid = paths["time"]
        r = paths["R"]
        plt.plot(time_grid, np.transpose(r))
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("R(t)")
    plt.legend(legend)


def plot_gamma_effect(gamma_vec, num_paths, num_steps, T, lmbda, r0, theta):
    """
    Plot effect of volatility on CIR paths.

    Parameters
    ----------
    gamma_vec : list
        List of gamma values to test
    num_paths : int
        Number of paths per gamma
    num_steps : int
        Number of time steps
    T : float
        Time to maturity
    lmbda : float
        Mean reversion speed
    r0 : float
        Initial rate
    theta : float
        Long-term mean
    """
    plt.figure(2)
    legend = []
    for gamma_temp in gamma_vec:
        np.random.seed(2)
        paths = generate_paths_cir_euler(num_paths, num_steps, T, lmbda, r0,
                                         theta, gamma_temp)
        legend.append('gamma={0}'.format(gamma_temp))
        time_grid = paths["time"]
        r = paths["R"]
        plt.plot(time_grid, np.transpose(r))
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("R(t)")
    plt.legend(legend)


def main():
    """Run CIR path generation and visualization."""
    # ============= Parameters =============
    num_paths = 1
    num_steps = 500
    T = 50.0
    lmbda = 0.1
    gamma = 0.05
    r0 = 0.05
    theta = 0.05

    # Effect of mean reversion lambda
    lmbda_vec = [0.01, 0.2, 5.0]
    plot_lambda_effect(lmbda_vec, num_paths, num_steps, T, r0, theta, gamma)

    # Effect of the volatility
    gamma_vec = [0.1, 0.2, 0.3]
    plot_gamma_effect(gamma_vec, num_paths, num_steps, T, lmbda, r0, theta)


if __name__ == "__main__":
    main()
