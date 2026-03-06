"""
Exposures for IR swaps under the Hull-White model with netting.

This educational code demonstrates exposure calculation for interest rate swaps
under the Hull-White single-factor model, comparing portfolios with and without
netting agreements. Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import enum

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.integrate as integrate


# ============= Option Type Enum =============
class OptionTypeSwap(enum.Enum):
    """Defines swap option types: receiver or payer."""
    RECEIVER = 1.0
    PAYER = -1.0


# ============= Path Generation =============
def generate_paths_hw_euler(num_paths, num_steps, t_end, p0t, lambd, eta):
    """
    Generate Hull-White interest rate paths using Euler scheme.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths to generate.
    num_steps : int
        Number of time steps per path.
    t_end : float
        Terminal time.
    p0t : callable
        Zero coupon bond price function P(0, T).
    lambd : float
        Mean reversion speed parameter.
    eta : float
        Volatility parameter.

    Returns
    -------
    dict
        Dictionary with 'time' array and 'R' array of interest rate paths.
    """
    dt_diff = 0.0001
    f0t = lambda t: -(np.log(p0t(t + dt_diff)) - np.log(p0t(t - dt_diff))) / (2 * dt_diff)

    # Initial interest rate is forward rate at time t -> 0
    r0 = f0t(0.00001)
    theta = lambda t: (
        1.0 / lambd * (f0t(t + dt_diff) - f0t(t - dt_diff)) / (2.0 * dt_diff)
        + f0t(t)
        + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * t))
    )

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = t_end / float(num_steps)
    for i in range(0, num_steps):
        # Normalize samples to ensure mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = (
            r[:, i]
            + lambd * (theta(time[i]) - r[:, i]) * dt
            + eta * (w[:, i + 1] - w[:, i])
        )
        time[i + 1] = time[i] + dt

    paths = {"time": time, "R": r}
    return paths


# ============= Hull-White Model Functions =============
def hw_theta(lambd, eta, p0t):
    """
    Compute the theta parameter for Hull-White model.

    Parameters
    ----------
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.
    p0t : callable
        Zero coupon bond price function.

    Returns
    -------
    callable
        Theta function of time.
    """
    dt_diff = 0.0001
    f0t = lambda t: -(np.log(p0t(t + dt_diff)) - np.log(p0t(t - dt_diff))) / (2 * dt_diff)
    theta = lambda t: (
        1.0 / lambd * (f0t(t + dt_diff) - f0t(t - dt_diff)) / (2.0 * dt_diff)
        + f0t(t)
        + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * t))
    )
    return theta


def hw_a(lambd, eta, p0t, t1, t2):
    """
    Compute the 'A' coefficient for Hull-White ZCB formula.

    Parameters
    ----------
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.
    p0t : callable
        Zero coupon bond price function.
    t1, t2 : float
        Maturity times.

    Returns
    -------
    float
        Coefficient A.
    """
    tau = t2 - t1
    z_grid = np.linspace(0.0, tau, 250)
    b_r = lambda tau: 1.0 / lambd * (np.exp(-lambd * tau) - 1.0)
    theta = hw_theta(lambd, eta, p0t)
    temp1 = lambd * integrate.trapz(theta(t2 - z_grid) * b_r(z_grid), z_grid)

    temp2 = (
        eta * eta / (4.0 * np.power(lambd, 3.0))
        * (np.exp(-2.0 * lambd * tau) * (4 * np.exp(lambd * tau) - 1.0) - 3.0)
        + eta * eta * tau / (2.0 * lambd * lambd)
    )

    return temp1 + temp2


def hw_b(lambd, eta, t1, t2):
    """
    Compute the 'B' coefficient for Hull-White ZCB formula.

    Parameters
    ----------
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility (unused but kept for signature consistency).
    t1, t2 : float
        Maturity times.

    Returns
    -------
    float
        Coefficient B.
    """
    return 1.0 / lambd * (np.exp(-lambd * (t2 - t1)) - 1.0)


def hw_zcb(lambd, eta, p0t, t1, t2, rt1):
    """
    Compute Hull-White zero coupon bond price.

    Parameters
    ----------
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.
    p0t : callable
        Zero coupon bond price function.
    t1, t2 : float
        Evaluation time and maturity.
    rt1 : float or ndarray
        Interest rate(s) at time t1.

    Returns
    -------
    float or ndarray
        ZCB price(s).
    """
    n = np.size(rt1)

    if t1 < t2:
        b_r = hw_b(lambd, eta, t1, t2)
        a_r = hw_a(lambd, eta, p0t, t1, t2)
        return np.exp(a_r + b_r * rt1)
    else:
        return np.ones(n)


def hw_mean_r(p0t, lambd, eta, t):
    """
    Compute mean of Hull-White interest rate at time T.

    Parameters
    ----------
    p0t : callable
        Zero coupon bond price function.
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.
    t : float
        Time.

    Returns
    -------
    float
        Mean interest rate.
    """
    dt_diff = 0.0001
    f0t = lambda t: -(np.log(p0t(t + dt_diff)) - np.log(p0t(t - dt_diff))) / (2.0 * dt_diff)
    r0 = f0t(0.00001)
    theta = hw_theta(lambd, eta, p0t)
    z_grid = np.linspace(0.0, t, 2500)
    temp = lambda z: theta(z) * np.exp(-lambd * (t - z))
    r_mean = r0 * np.exp(-lambd * t) + lambd * integrate.trapz(temp(z_grid), z_grid)
    return r_mean


def hw_r_0(p0t, lambd, eta):
    """
    Compute initial Hull-White interest rate.

    Parameters
    ----------
    p0t : callable
        Zero coupon bond price function.
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.

    Returns
    -------
    float
        Initial interest rate r0.
    """
    dt_diff = 0.0001
    f0t = lambda t: -(np.log(p0t(t + dt_diff)) - np.log(p0t(t - dt_diff))) / (2 * dt_diff)
    r0 = f0t(0.00001)
    return r0


def hw_mu_frwd_measure(p0t, lambd, eta, t):
    """
    Compute mean under forward measure for Hull-White model.

    Parameters
    ----------
    p0t : callable
        Zero coupon bond price function.
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.
    t : float
        Time.

    Returns
    -------
    float
        Mean under forward measure.
    """
    dt_diff = 0.0001
    f0t = lambda t: -(np.log(p0t(t + dt_diff)) - np.log(p0t(t - dt_diff))) / (2 * dt_diff)
    r0 = f0t(0.00001)
    theta = hw_theta(lambd, eta, p0t)
    z_grid = np.linspace(0.0, t, 500)

    theta_hat = lambda t, t_mat: theta(t) + eta * eta / lambd * 1.0 / lambd * (
        np.exp(-lambd * (t_mat - t)) - 1.0
    )

    temp = lambda z: theta_hat(z, t) * np.exp(-lambd * (t - z))

    r_mean = r0 * np.exp(-lambd * t) + lambd * integrate.trapz(temp(z_grid), z_grid)

    return r_mean


def hw_var_r(lambd, eta, t):
    """
    Compute variance of Hull-White interest rate at time T.

    Parameters
    ----------
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.
    t : float
        Time.

    Returns
    -------
    float
        Variance.
    """
    return eta * eta / (2.0 * lambd) * (1.0 - np.exp(-2.0 * lambd * t))


def hw_density(p0t, lambd, eta, t):
    """
    Compute probability density function for Hull-White interest rate.

    Parameters
    ----------
    p0t : callable
        Zero coupon bond price function.
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.
    t : float
        Time.

    Returns
    -------
    callable
        PDF function.
    """
    r_mean = hw_mean_r(p0t, lambd, eta, t)
    r_var = hw_var_r(lambd, eta, t)
    return lambda x: st.norm.pdf(x, r_mean, np.sqrt(r_var))


# ============= Swap Pricing =============
def hw_swap_price(option_type, notional, strike, t, ti, tm, n, r_t, p0t, lambd, eta):
    """
    Compute Hull-White swap price.

    Parameters
    ----------
    option_type : OptionTypeSwap
        Payer or receiver swap.
    notional : float
        Notional amount.
    strike : float
        Strike rate.
    t : float
        Evaluation time.
    ti, tm : float
        Swap start and end times.
    n : int
        Number of payment dates.
    r_t : float or ndarray
        Interest rate(s) at time t.
    p0t : callable
        Zero coupon bond price function.
    lambd : float
        Mean reversion speed.
    eta : float
        Volatility.

    Returns
    -------
    float or ndarray
        Swap price(s).
    """
    if n == 1:
        ti_grid = np.array([ti, tm])
    else:
        ti_grid = np.linspace(ti, tm, n)
    tau = ti_grid[1] - ti_grid[0]

    # Overwrite Ti if t > Ti
    prev_ti = ti_grid[np.where(ti_grid < t)]
    if np.size(prev_ti) > 0:
        ti = prev_ti[-1]

    # Handle case when some payments are already done
    ti_grid = ti_grid[np.where(ti_grid > t)]

    temp = np.zeros(np.size(r_t))

    p_t_ti_lambda = lambda ti_arg: hw_zcb(lambd, eta, p0t, t, ti_arg, r_t)

    for idx, ti_val in enumerate(ti_grid):
        if ti_val > ti:
            temp = temp + tau * p_t_ti_lambda(ti_val)

    p_t_ti = p_t_ti_lambda(ti)
    p_t_tm = p_t_ti_lambda(tm)

    if option_type == OptionTypeSwap.PAYER:
        swap = (p_t_ti - p_t_tm) - strike * temp
    elif option_type == OptionTypeSwap.RECEIVER:
        swap = strike * temp - (p_t_ti - p_t_tm)

    return swap * notional


# ============= Plotting Functions =============
def plot_zcb_comparison(t_grid, exact, proxy):
    """
    Plot ZCB prices from Monte Carlo vs analytical expression.

    Parameters
    ----------
    t_grid : ndarray
        Maturity times.
    exact : ndarray
        Analytical ZCB prices.
    proxy : ndarray
        Monte Carlo ZCB prices.
    """
    plt.figure(1)
    plt.grid()
    plt.plot(t_grid, exact, "-k")
    plt.plot(t_grid, proxy, "--r")
    plt.legend(["Analytical ZCB", "Monte Carlo ZCB"])
    plt.title("P(0,T) from Monte Carlo vs. Analytical expression")


def plot_swap_values(time_grid, values, num_paths=100):
    """
    Plot swap values over time.

    Parameters
    ----------
    time_grid : ndarray
        Time grid.
    values : ndarray
        Values of shape (num_paths, num_steps).
    num_paths : int, optional
        Number of paths to plot.
    """
    plt.figure(2)
    plt.plot(time_grid, values[0:num_paths, :].transpose(), "b")
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("exposure, Value(t)")
    plt.title("Value of a swap")


def plot_positive_exposure(time_grid, exposures, num_paths=100):
    """
    Plot positive exposures over time.

    Parameters
    ----------
    time_grid : ndarray
        Time grid.
    exposures : ndarray
        Positive exposures of shape (num_paths, num_steps).
    num_paths : int, optional
        Number of paths to plot.
    """
    plt.figure(3)
    plt.plot(time_grid, exposures[0:num_paths, :].transpose(), "r")
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("exposure, E(t)")
    plt.title("Positive Exposure E(t)")


def plot_expected_exposure(time_grid, ee, pfe, pfe2=None):
    """
    Plot expected exposure and potential future exposure.

    Parameters
    ----------
    time_grid : ndarray
        Time grid.
    ee : ndarray
        Expected exposure.
    pfe : ndarray
        Potential future exposure (alpha level).
    pfe2 : ndarray, optional
        Secondary PFE at different alpha level.
    """
    plt.figure(5)
    plt.plot(time_grid, ee, "r")
    plt.plot(time_grid, pfe, "k")
    if pfe2 is not None:
        plt.plot(time_grid, pfe2, "--b")
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("EE, PFE(t)")
    plt.title("Discounted Expected (positive) exposure, EE")


def plot_portfolio_metrics(time_grid, ee_port, pfe_port):
    """
    Plot portfolio expected and potential future exposure.

    Parameters
    ----------
    time_grid : ndarray
        Time grid.
    ee_port : ndarray
        Portfolio expected exposure.
    pfe_port : ndarray
        Portfolio potential future exposure.
    """
    plt.figure(6)
    plt.plot(time_grid, ee_port, "r")
    plt.plot(time_grid, pfe_port, "k")
    plt.grid()
    plt.title("Portfolio with two swaps")
    plt.legend(["EE-port", "PFE-port"])


def plot_exposure_comparison(time_grid, ee, ee_port):
    """
    Plot comparison of expected exposures (single swap vs portfolio).

    Parameters
    ----------
    time_grid : ndarray
        Time grid.
    ee : ndarray
        Single swap expected exposure.
    ee_port : ndarray
        Portfolio expected exposure.
    """
    plt.figure(7)
    plt.plot(time_grid, ee, "r")
    plt.plot(time_grid, ee_port, "--r")
    plt.grid()
    plt.title("Comparison of EEs")
    plt.legend(["EE, swap", "EE, portfolio"])


def plot_pfe_comparison(time_grid, pfe, pfe_port):
    """
    Plot comparison of potential future exposures (single swap vs portfolio).

    Parameters
    ----------
    time_grid : ndarray
        Time grid.
    pfe : ndarray
        Single swap PFE.
    pfe_port : ndarray
        Portfolio PFE.
    """
    plt.figure(8)
    plt.plot(time_grid, pfe, "k")
    plt.plot(time_grid, pfe_port, "--k")
    plt.grid()
    plt.title("Comparison of PFEs")
    plt.legend(["PFE, swap", "PFE, portfolio"])


# ============= Main Calculation =============
def main():
    """
    Main computation: compute and plot exposure profiles for IR swaps with/without netting.
    """
    # --------- Configuration ---------
    num_paths = 2000  # Number of Monte Carlo paths
    num_steps = 1000  # Number of time steps per path
    lambd = 0.5  # Hull-White mean reversion speed
    eta = 0.03  # Hull-White volatility
    notional = 10000.0  # Single swap notional
    notional2 = 10000.0  # Second swap notional
    alpha = 0.99  # Confidence level for PFE calculation
    alpha2 = 0.95  # Secondary confidence level

    # Define zero coupon bond curve (market data)
    p0t = lambda t: np.exp(-0.01 * t)
    r0 = hw_r_0(p0t, lambd, eta)

    # --------- ZCB Validation ---------
    # Compare ZCB from Market and Analytical expression
    n_zcb = 25
    t_end_zcb = 50
    t_grid_zcb = np.linspace(0, t_end_zcb, n_zcb)

    exact = np.zeros((n_zcb, 1))
    proxy = np.zeros((n_zcb, 1))
    for i, ti in enumerate(t_grid_zcb):
        proxy[i] = hw_zcb(lambd, eta, p0t, 0.0, ti, r0)
        exact[i] = p0t(ti)

    plot_zcb_comparison(t_grid_zcb, exact, proxy)

    # --------- Swap Exposure Simulation ---------
    # Swap settings
    strike = 0.01  # Strike rate
    ti_swap = 1.0  # Beginning of the swap
    tm_swap = 10.0  # End date of the swap
    n_swap = 10  # Number of payments between ti and tm

    paths = generate_paths_hw_euler(num_paths, num_steps, tm_swap + 1.0, p0t, lambd, eta)
    r = paths["R"]
    time_grid = paths["time"]
    dt = time_grid[1] - time_grid[0]

    # Compute money market account for discounting
    m_t = np.zeros((num_paths, num_steps))
    for i in range(0, num_paths):
        m_t[i, :] = np.exp(np.cumsum(r[i, 0:-1]) * dt)

    # --------- Single Swap Exposures (without netting) ---------
    value = np.zeros((num_paths, num_steps + 1))
    e = np.zeros((num_paths, num_steps + 1))
    ee = np.zeros(num_steps + 1)
    pfe = np.zeros(num_steps + 1)
    pfe2 = np.zeros(num_steps + 1)
    for idx, ti in enumerate(time_grid[0:-2]):
        v = hw_swap_price(
            OptionTypeSwap.PAYER, notional, strike, time_grid[idx], ti_swap, tm_swap, n_swap, r[:, idx], p0t, lambd, eta
        )
        value[:, idx] = v
        e[:, idx] = np.maximum(v, 0.0)
        ee[idx] = np.mean(e[:, idx] / m_t[:, idx])
        pfe[idx] = np.quantile(e[:, idx], alpha)
        pfe2[idx] = np.quantile(e[:, idx], alpha2)

    # --------- Portfolio Exposures (with netting) ---------
    value_port = np.zeros((num_paths, num_steps + 1))
    e_port = np.zeros((num_paths, num_steps + 1))
    ee_port = np.zeros(num_steps + 1)
    pfe_port = np.zeros(num_steps + 1)
    for idx, ti in enumerate(time_grid[0:-2]):
        swap1 = hw_swap_price(
            OptionTypeSwap.PAYER, notional, strike, time_grid[idx], ti_swap, tm_swap, n_swap, r[:, idx], p0t, lambd, eta
        )
        swap2 = hw_swap_price(
            OptionTypeSwap.RECEIVER,
            notional2,
            0.0,
            time_grid[idx],
            tm_swap - 2.0 * (tm_swap - ti_swap) / n_swap,
            tm_swap,
            1,
            r[:, idx],
            p0t,
            lambd,
            eta,
        )

        v_port = swap1 + swap2
        value_port[:, idx] = v_port
        e_port[:, idx] = np.maximum(v_port, 0.0)
        ee_port[idx] = np.mean(e_port[:, idx] / m_t[:, idx])
        pfe_port[idx] = np.quantile(e_port[:, idx], alpha)

    # --------- Generate Plots ---------
    plot_swap_values(time_grid, value)
    plot_positive_exposure(time_grid, e)
    plot_expected_exposure(time_grid, ee, pfe, pfe2)
    plot_portfolio_metrics(time_grid, ee_port, pfe_port)
    plot_exposure_comparison(time_grid, ee, ee_port)
    plot_pfe_comparison(time_grid, pfe, pfe_port)


if __name__ == "__main__":
    main()
