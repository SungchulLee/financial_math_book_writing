"""
BSHW model implied volatility term structure computation.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.stats as st
import enum
import scipy.optimize as optimize


class OptionType(enum.Enum):
    CALL = 1.0
    PUT = -1.0


def bs_call_option_price(cp, s_0, k, sigma, tau, r):
    """Black-Scholes option price."""
    if isinstance(k, list):
        k = np.array(k).reshape([len(k), 1])
    d1 = (np.log(s_0 / k) + (r + 0.5 * sigma ** 2.0) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    if cp == OptionType.CALL:
        value = st.norm.cdf(d1) * s_0 - st.norm.cdf(d2) * k * np.exp(-r * tau)
    elif cp == OptionType.PUT:
        value = st.norm.cdf(-d2) * k * np.exp(-r * tau) - st.norm.cdf(-d1) * s_0
    return value


def implied_volatility_black76(cp, frwd_market_price, k, t, frwd_stock):
    """Implied volatility using Black76."""
    func = lambda sigma: np.power(bs_call_option_price(cp, frwd_stock, k, sigma, t, 0.0) - frwd_market_price, 1.0)
    implied_vol = optimize.newton(func, 0.2, tol=1e-9)
    return implied_vol


def bshw_volatility(t, eta, sigma, rho, lambd):
    """BSHW model volatility."""
    br = lambda t_val, t_end: 1.0 / lambd * (np.exp(-lambd * (t_end - t_val)) - 1.0)
    sigma_f = lambda t_val: np.sqrt(sigma * sigma + eta * eta * br(t_val, t) * br(t_val, t) -
                                    2.0 * rho * sigma * eta * br(t_val, t))
    z_grid = np.linspace(0.0, t, 2500)
    sigma_c = np.sqrt(1.0 / t * integrate.trapz(sigma_f(z_grid) * sigma_f(z_grid), z_grid))
    return sigma_c


def bshw_option_price(cp, s0, k, p0t, t, eta, sigma, rho, lambd):
    """BSHW option price."""
    frwd_s0 = s0 / p0t
    vol = bshw_volatility(t, eta, sigma, rho, lambd)
    r = 0.0
    black_price = bs_call_option_price(cp, frwd_s0, k, vol, t, r)
    return p0t * black_price


def main():
    """Main computation."""
    cp = OptionType.CALL

    # HW model settings
    lambd = 0.1
    eta = 0.01
    sigma = 0.2
    rho = 0.3
    s0 = 100

    # Strike equals stock value, thus ATM
    k = [100]
    k = np.array(k).reshape([len(k), 1])

    # ZCB curve
    p0t = lambda t: np.exp(-0.05 * t)

    # Maturities at which to compute implied volatility
    t_mat = np.linspace(0.1, 5.0, 20)

    # Effect of lambda
    plt.figure(2)
    plt.grid()
    plt.xlabel('maturity, T')
    plt.ylabel('implied volatility')
    lambda_v = [0.001, 0.1, 0.5, 1.5]
    legend = []
    for lambda_temp in lambda_v:
        iv = np.zeros((len(t_mat), 1))
        for idx in range(0, len(t_mat)):
            t = t_mat[idx]
            val = bshw_option_price(cp, s0, k, p0t(t), t, eta, sigma, rho, lambda_temp)
            frwd_stock = s0 / p0t(t)
            val_frwd = val / p0t(t)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k, t, frwd_stock)
        plt.plot(t_mat, iv * 100.0)
        legend.append('lambda={0}'.format(lambda_temp))
    plt.legend(legend)

    # Effect of eta
    plt.figure(3)
    plt.grid()
    plt.xlabel('maturity, T')
    plt.ylabel('implied volatility')
    eta_v = [0.001, 0.05, 0.1, 0.15]
    legend = []
    for eta_temp in eta_v:
        iv = np.zeros((len(t_mat), 1))
        for idx in range(0, len(t_mat)):
            t = t_mat[idx]
            val = bshw_option_price(cp, s0, k, p0t(t), t, eta_temp, sigma, rho, lambd)
            frwd_stock = s0 / p0t(t)
            val_frwd = val / p0t(t)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k, t, frwd_stock)
        plt.plot(t_mat, iv * 100.0)
        legend.append('eta={0}'.format(eta_temp))
    plt.legend(legend)

    # Effect of sigma
    plt.figure(4)
    plt.grid()
    plt.xlabel('maturity, T')
    plt.ylabel('implied volatility')
    sigma_v = [0.1, 0.2, 0.3, 0.4]
    legend = []
    for sigma_temp in sigma_v:
        iv = np.zeros((len(t_mat), 1))
        for idx in range(0, len(t_mat)):
            t = t_mat[idx]
            val = bshw_option_price(cp, s0, k, p0t(t), t, eta, sigma_temp, rho, lambd)
            frwd_stock = s0 / p0t(t)
            val_frwd = val / p0t(t)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k, t, frwd_stock)
        plt.plot(t_mat, iv * 100.0)
        legend.append('sigma={0}'.format(sigma_temp))
    plt.legend(legend)

    # Effect of rho
    plt.figure(5)
    plt.grid()
    plt.xlabel('maturity, T')
    plt.ylabel('implied volatility')
    rho_v = [-0.7, -0.3, 0.3, 0.7]
    legend = []
    for rho_temp in rho_v:
        iv = np.zeros((len(t_mat), 1))
        for idx in range(0, len(t_mat)):
            t = t_mat[idx]
            val = bshw_option_price(cp, s0, k, p0t(t), t, eta, sigma, rho_temp, lambd)
            frwd_stock = s0 / p0t(t)
            val_frwd = val / p0t(t)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k, t, frwd_stock)
        plt.plot(t_mat, iv * 100.0)
        legend.append('rho={0}'.format(rho_temp))
    plt.legend(legend)


if __name__ == "__main__":
    main()
