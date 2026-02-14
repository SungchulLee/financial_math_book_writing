"""
Ho-Lee model simulation and zero-coupon bond pricing.

Simulates the Ho-Lee model and computes zero-coupon bond prices P(0,t).

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak
"""
import numpy as np
import matplotlib.pyplot as plt


def f0t(t, p0t):
    """
    Calculate forward rate at time t.

    Parameters
    ----------
    t : float
        Time point
    p0t : callable
        Zero-coupon bond pricing function P(0,T)

    Returns
    -------
    float
        Forward rate f(0,t)
    """
    dt = 0.01
    expr = -(np.log(p0t(t + dt)) - np.log(p0t(t - dt))) / (2 * dt)
    return expr


def generate_paths_ho_lee_euler(num_paths, num_steps, T, p0t, sigma):
    """
    Generate Ho-Lee model paths using Euler scheme.

    Parameters
    ----------
    num_paths : int
        Number of simulation paths
    num_steps : int
        Number of time steps
    T : float
        Time to maturity
    p0t : callable
        Zero-coupon bond pricing function
    sigma : float
        Volatility parameter

    Returns
    -------
    dict
        Dictionary with keys 'time', 'R', 'M' containing time grid, rates, and bank account
    """
    dt = T / float(num_steps)

    # Initial interest rate is forward rate at time t->0
    r0 = f0t(0.01, p0t)

    def theta(t):
        """Theta function for Ho-Lee model."""
        return ((f0t(t + dt, p0t) - f0t(t - dt, p0t)) / (2.0 * dt) +
                sigma ** 2.0 * t)

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    m = np.zeros((num_paths, num_steps + 1))
    m[:, 0] = 1.0
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    for i in range(0, num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = r[:, i] + theta(time[i]) * dt + sigma * (w[:, i + 1] -
                                                                 w[:, i])
        m[:, i + 1] = m[:, i] * np.exp((r[:, i + 1] + r[:, i]) * 0.5 * dt)
        time[i + 1] = time[i] + dt

    paths = {"time": time, "R": r, "M": m}
    return paths


def plot_zcb_comparison(time_grid, p0t_market, p0t_mc):
    """
    Plot comparison of market and Monte Carlo zero-coupon bond prices.

    Parameters
    ----------
    time_grid : array
        Time points
    p0t_market : array
        Market ZCB prices
    p0t_mc : array
        Monte Carlo ZCB prices
    """
    plt.figure(1)
    plt.grid()
    plt.xlabel('T')
    plt.ylabel('P(0,T)')
    plt.plot(time_grid, p0t_market)
    plt.plot(time_grid, p0t_mc, '--r')
    plt.legend(['P(0,t) market', 'P(0,t) Monte Carlo'])
    plt.title('ZCBs from Ho-Lee Model')


def main():
    """Run Ho-Lee model simulation and ZCB pricing."""
    # ============= Parameters =============
    num_paths = 25000
    num_steps = 500
    sigma = 0.007
    T = 40

    # Define a ZCB curve (obtained from market)
    p0t = lambda T: np.exp(-0.1 * T)

    # ============= Monte Carlo Simulation =============
    paths = generate_paths_ho_lee_euler(num_paths, num_steps, T, p0t, sigma)
    m = paths["M"]
    ti = paths["time"]

    # Compare price of ZCB from Monte Carlo and analytical expression
    p_t = np.zeros(num_steps + 1)
    for i in range(0, num_steps + 1):
        p_t[i] = np.mean(1.0 / m[:, i])

    # ============= Plotting =============
    plot_zcb_comparison(ti, p0t(ti), p_t)


if __name__ == "__main__":
    main()
