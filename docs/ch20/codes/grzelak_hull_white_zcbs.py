"""
Hull-White model simulation for Zero-Coupon Bond pricing.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt


# ============= Forward Rate and Theta Functions =============

def f0t(tau, p0t):
    """
    Compute forward rate at time tau.

    Parameters
    ----------
    tau : float
        Time point
    p0t : callable
        Zero-coupon bond function P(0, T)

    Returns
    -------
    float
        Forward rate f(0, tau)
    """
    dt = 0.01
    return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)


def hw_theta(lambd, eta, p0t):
    """
    Compute Hull-White theta function (mean-reverting level).

    Parameters
    ----------
    lambd : float
        Mean reversion speed
    eta : float
        Volatility
    p0t : callable
        Zero-coupon bond function

    Returns
    -------
    callable
        Theta function
    """
    dt = 0.01

    def theta(tau):
        """Mean-reverting level at time tau."""
        return (1.0 / lambd * (f0t(tau + dt, p0t) - f0t(tau - dt, p0t)) / (2.0 * dt) +
                f0t(tau, p0t) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))

    return theta


# ============= Path Generation =============

def generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta):
    """
    Generate Hull-White interest rate paths with money market account.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths
    num_steps : int
        Number of time steps
    t : float
        Total time horizon
    p0t : callable
        Zero-coupon bond function P(0, T)
    lambd : float
        Mean reversion speed
    eta : float
        Volatility

    Returns
    -------
    dict
        Dictionary with 'time', 'R', and 'M' keys
    """
    dt_diff = 0.01

    def f0t_local(tau):
        """Local forward rate function."""
        return -(np.log(p0t(tau + dt_diff)) - np.log(p0t(tau - dt_diff))) / (2 * dt_diff)

    # Initial interest rate
    r0 = f0t_local(0.01)

    # Get theta function
    theta = hw_theta(lambd, eta, p0t)

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    m = np.zeros((num_paths, num_steps + 1))
    m[:, 0] = 1.0
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = t / float(num_steps)
    for i in range(0, num_steps):
        # Ensure samples have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])

        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = r[:, i] + lambd * (theta(time[i]) - r[:, i]) * dt + eta * (w[:, i + 1] - w[:, i])
        m[:, i + 1] = m[:, i] * np.exp((r[:, i + 1] + r[:, i]) * 0.5 * dt)
        time[i + 1] = time[i] + dt

    return {"time": time, "R": r, "M": m}


# ============= Plotting =============

def main():
    """Main computation for Hull-White ZCB analysis."""
    num_paths = 25000
    num_steps = 25
    lambd = 0.02
    eta = 0.02

    # ZCB curve (from market)
    p0t = lambda t: np.exp(-0.1 * t)

    # Monte Carlo simulation
    t = 40
    paths = generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta)
    m = paths["M"]
    ti = paths["time"]

    # Compute ZCB prices from simulation
    p_t_mc = np.zeros(num_steps + 1)
    for i in range(0, num_steps + 1):
        p_t_mc[i] = np.mean(1.0 / m[:, i])

    # Compare with market ZCB
    plt.figure(1)
    plt.grid()
    plt.xlabel('T')
    plt.ylabel('P(0,T)')
    plt.plot(ti, p0t(ti))
    plt.plot(ti, p_t_mc, '--r')
    plt.legend(['P(0,t) market', 'P(0,t) Monte Carlo'])
    plt.title('ZCBs from Hull-White Model')


if __name__ == "__main__":
    main()
