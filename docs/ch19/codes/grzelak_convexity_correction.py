"""
Convexity correction for forward-starting LIBOR rates.

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak
"""
import enum
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


class OptionType(enum.Enum):
    """Option type enumeration."""
    CALL = 1.0
    PUT = -1.0


def generate_paths_hw_euler(num_paths, num_steps, T, p0t, lmbda, eta):
    """
    Generate Hull-White model paths using Euler scheme.

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
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility parameter

    Returns
    -------
    dict
        Dictionary with keys 'time' and 'R' containing time grid and rate paths
    """
    dt = 0.0001
    def f0t_calc(t):
        """Calculate forward rate."""
        return -(np.log(p0t(t + dt)) - np.log(p0t(t - dt))) / (2 * dt)

    r0 = f0t_calc(0.00001)
    def theta(t):
        """Theta function for HW model."""
        return (1.0 / lmbda * (f0t_calc(t + dt) - f0t_calc(t - dt)) / (2.0 * dt) +
                f0t_calc(t) + eta * eta / (2.0 * lmbda * lmbda) *
                (1.0 - np.exp(-2.0 * lmbda * t)))

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = T / float(num_steps)
    for i in range(0, num_steps):
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = (r[:, i] + lmbda * (theta(time[i]) - r[:, i]) * dt +
                       eta * (w[:, i + 1] - w[:, i]))
        time[i + 1] = time[i] + dt

    paths = {"time": time, "R": r}
    return paths


def hw_theta(lmbda, eta, p0t):
    """
    Compute theta function for Hull-White model.

    Parameters
    ----------
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility
    p0t : callable
        Zero-coupon bond pricing function

    Returns
    -------
    callable
        Theta function at time t
    """
    dt = 0.0001
    def f0t_calc(t):
        return -(np.log(p0t(t + dt)) - np.log(p0t(t - dt))) / (2 * dt)

    def theta_func(t):
        return (1.0 / lmbda * (f0t_calc(t + dt) - f0t_calc(t - dt)) / (2.0 * dt) +
                f0t_calc(t) + eta * eta / (2.0 * lmbda * lmbda) *
                (1.0 - np.exp(-2.0 * lmbda * t)))

    return theta_func


def hw_a(lmbda, eta, p0t, t1, t2):
    """
    Compute A parameter for HW ZCB pricing.

    Parameters
    ----------
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility
    p0t : callable
        Zero-coupon bond pricing function
    t1 : float
        Start time
    t2 : float
        End time

    Returns
    -------
    float
        A parameter value
    """
    tau = t2 - t1
    z_grid = np.linspace(0.0, tau, 250)
    def b_r(tau_val):
        return 1.0 / lmbda * (np.exp(-lmbda * tau_val) - 1.0)

    theta = hw_theta(lmbda, eta, p0t)
    temp1 = lmbda * integrate.trapz(theta(t2 - z_grid) * b_r(z_grid), z_grid)
    temp2 = (eta * eta / (4.0 * np.power(lmbda, 3.0)) *
             (np.exp(-2.0 * lmbda * tau) * (4 * np.exp(lmbda * tau) - 1.0) - 3.0) +
             eta * eta * tau / (2.0 * lmbda * lmbda))

    return temp1 + temp2


def hw_b(lmbda, eta, t1, t2):
    """
    Compute B parameter for HW ZCB pricing.

    Parameters
    ----------
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility (unused, kept for API consistency)
    t1 : float
        Start time
    t2 : float
        End time

    Returns
    -------
    float
        B parameter value
    """
    return 1.0 / lmbda * (np.exp(-lmbda * (t2 - t1)) - 1.0)


def hw_zcb(lmbda, eta, p0t, t1, t2, r_t1):
    """
    Compute HW zero-coupon bond price.

    Parameters
    ----------
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility
    p0t : callable
        Zero-coupon bond pricing function
    t1 : float
        Current time
    t2 : float
        Maturity time
    r_t1 : array or float
        Interest rate at time t1

    Returns
    -------
    array or float
        ZCB price P(t1, t2)
    """
    b_r = hw_b(lmbda, eta, t1, t2)
    a_r = hw_a(lmbda, eta, p0t, t1, t2)
    return np.exp(a_r + b_r * r_t1)


def plot_zcb_comparison(t_grid, exact, proxy):
    """
    Plot ZCB from market vs. analytical expression.

    Parameters
    ----------
    t_grid : array
        Time grid
    exact : array
        Exact (market) ZCB prices
    proxy : array
        Analytical proxy ZCB prices
    """
    plt.figure(1)
    plt.grid()
    plt.plot(t_grid, exact, '-k')
    plt.plot(t_grid, proxy, '--r')
    plt.legend(["Analytical ZCB", "Monte Carlo ZCB"])
    plt.title('P(0,T) from Monte Carlo vs. Analytical expression')


def plot_convexity_correction(sigma_range, cc_values):
    """
    Plot convexity correction as function of volatility.

    Parameters
    ----------
    sigma_range : array
        Volatility values
    cc_values : array
        Convexity correction values
    """
    plt.figure(2)
    plt.plot(sigma_range, cc_values)
    plt.grid()
    plt.xlabel('sigma')
    plt.ylabel('cc')


def plot_derivative_price(sigma_range, mc_result, forward_price):
    """
    Plot derivative price with and without convexity correction.

    Parameters
    ----------
    sigma_range : array
        Volatility values
    mc_result : float
        Monte Carlo price
    forward_price : array
        Forward price array
    """
    plt.figure(3)
    plt.plot(sigma_range, mc_result * np.ones(len(sigma_range)))
    plt.plot(sigma_range, forward_price, '--r')
    plt.grid()
    plt.xlabel('sigma')
    plt.ylabel('value of derivative')
    plt.legend(['market price', 'price with cc'])


def main():
    """Run convexity correction analysis."""
    # ============= Parameters =============
    num_paths = 20000
    num_steps = 1000
    lmbda = 0.02
    eta = 0.02
    p0t = lambda T: np.exp(-0.1 * T)
    r0 = hw_theta(lmbda, eta, p0t)(0.00001)

    # ============= ZCB Comparison =============
    n = 25
    t_end = 50
    t_grid = np.linspace(0, t_end, n)

    exact = np.zeros(n)
    proxy = np.zeros(n)
    for i, ti in enumerate(t_grid):
        proxy[i] = hw_zcb(lmbda, eta, p0t, 0.0, ti, r0)
        exact[i] = p0t(ti)

    plot_zcb_comparison(t_grid, exact, proxy)

    # ============= Convexity Correction Analysis =============
    t1 = 4.0
    t2 = 8.0

    paths = generate_paths_hw_euler(num_paths, num_steps, t1, p0t, lmbda, eta)
    r = paths["R"]
    time_grid = paths["time"]
    dt = time_grid[1] - time_grid[0]

    m_t = np.zeros((num_paths, num_steps))
    for i in range(0, num_paths):
        m_t[i, :] = np.exp(np.cumsum(r[i, :-1]) * dt)

    p_t1_t2 = hw_zcb(lmbda, eta, p0t, t1, t2, r[:, -1])
    l_t1_t2 = 1.0 / (t2 - t1) * (1.0 / p_t1_t2 - 1)
    mc_result = np.mean(1 / m_t[:, -1] * l_t1_t2)
    print('Price of E(L(T1,T1,T2)/M(T1)) = {0}'.format(mc_result))

    l_t0_t1_t2 = 1.0 / (t2 - t1) * (p0t(t1) / p0t(t2) - 1.0)

    def convexity_correction(sigma):
        """Convexity correction function."""
        return (p0t(t2) * (l_t0_t1_t2 + (t2 - t1) * l_t0_t1_t2 ** 2.0 *
                np.exp(sigma ** 2 * t1)) - l_t0_t1_t2)

    sigma = 0.2
    print('Price of E(L(T1,T1,T2)/M(T1)) = {0} (no cc)'.format(l_t0_t1_t2))
    print('Price of E(L(T1,T1,T2)/M(T1)) = {0} (with cc, sigma={1})'.format(
        l_t0_t1_t2 + convexity_correction(sigma), sigma))

    # ============= Plotting =============
    sigma_range = np.linspace(0.0, 0.6, 100)
    plot_convexity_correction(sigma_range, convexity_correction(sigma_range))

    forward_price = l_t0_t1_t2 + convexity_correction(sigma_range)
    plot_derivative_price(sigma_range, mc_result, forward_price)


if __name__ == "__main__":
    main()
