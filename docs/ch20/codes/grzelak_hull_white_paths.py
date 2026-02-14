"""
Monte Carlo paths for the Hull-White model.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt


# ============= Hull-White Path Generator =============

def generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta):
    """
    Generate interest rate paths using Hull-White model with Euler discretization.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths
    num_steps : int
        Number of time steps
    t : float
        Total time horizon
    p0t : callable
        Zero-coupon bond price function P(0, T)
    lambd : float
        Mean reversion speed
    eta : float
        Volatility parameter

    Returns
    -------
    dict
        Dictionary with 'time' and 'R' keys containing time grid and rates
    """
    # Time-step for numerical differentiation
    dt_diff = 0.0001

    def f0t(tau):
        """Compute forward rate at time tau."""
        return -(np.log(p0t(tau + dt_diff)) - np.log(p0t(tau - dt_diff))) / (2 * dt_diff)

    # Initial interest rate
    r0 = f0t(0.00001)

    def theta(tau):
        """Compute mean-reverting level theta(t)."""
        return (1.0 / lambd * (f0t(tau + dt_diff) - f0t(tau - dt_diff)) / (2.0 * dt_diff) +
                f0t(tau) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = t / float(num_steps)
    for i in range(0, num_steps):
        # Ensure samples have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])

        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = r[:, i] + lambd * (theta(time[i]) - r[:, i]) * dt + eta * (w[:, i + 1] - w[:, i])
        time[i + 1] = time[i] + dt

    return {"time": time, "R": r}


# ============= Plotting Functions =============

def plot_lambda_effect(num_paths, num_steps, t, p0t, eta):
    """
    Plot the effect of mean reversion speed lambda on interest rate paths.

    Parameters
    ----------
    num_paths : int
        Number of paths
    num_steps : int
        Number of steps
    t : float
        Time horizon
    p0t : callable
        Zero-coupon bond function
    eta : float
        Volatility
    """
    plt.figure(1)
    legend = []
    lambda_vec = [-0.01, 0.2, 5.0]

    for lambda_temp in lambda_vec:
        np.random.seed(2)
        paths = generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambda_temp, eta)
        legend.append('lambda={0}'.format(lambda_temp))
        time_grid = paths["time"]
        r = paths["R"]
        plt.plot(time_grid, np.transpose(r))

    plt.grid()
    plt.xlabel("time")
    plt.ylabel("R(t)")
    plt.legend(legend)


def plot_eta_effect(num_paths, num_steps, t, p0t, lambd):
    """
    Plot the effect of volatility eta on interest rate paths.

    Parameters
    ----------
    num_paths : int
        Number of paths
    num_steps : int
        Number of steps
    t : float
        Time horizon
    p0t : callable
        Zero-coupon bond function
    lambd : float
        Mean reversion speed
    """
    plt.figure(2)
    legend = []
    eta_vec = [0.1, 0.2, 0.3]

    for eta_temp in eta_vec:
        np.random.seed(2)
        paths = generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta_temp)
        legend.append('eta={0}'.format(eta_temp))
        time_grid = paths["time"]
        r = paths["R"]
        plt.plot(time_grid, np.transpose(r))

    plt.grid()
    plt.xlabel("time")
    plt.ylabel("R(t)")
    plt.legend(legend)


def main():
    """Main computation for Hull-White path generation and analysis."""
    num_paths = 1
    num_steps = 5000
    t = 50.0
    lambd = 0.5
    eta = 0.01

    # ZCB curve (from market)
    p0t = lambda tau: np.exp(-0.05 * tau)

    # Effect of mean reversion lambda
    plot_lambda_effect(num_paths, num_steps, t, p0t, eta)

    # Effect of volatility
    plot_eta_effect(num_paths, num_steps, t, p0t, lambd)


if __name__ == "__main__":
    main()
