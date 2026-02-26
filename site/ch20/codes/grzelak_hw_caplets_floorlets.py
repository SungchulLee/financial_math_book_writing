"""
Caplets and floorlets under the Hull-White Model.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import enum
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.integrate as integrate
import scipy.optimize as optimize


class OptionType(enum.Enum):
    CALL = 1.0
    PUT = -1.0


def f0t(tau, p0t):
    dt = 0.0001
    return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)


def hw_theta(lambd, eta, p0t):
    dt = 0.0001
    def theta(tau):
        return (1.0 / lambd * (f0t(tau + dt, p0t) - f0t(tau - dt, p0t)) / (2.0 * dt) +
                f0t(tau, p0t) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))
    return theta


def hw_a(lambd, eta, p0t, t1, t2):
    tau = t2 - t1
    z_grid = np.linspace(0.0, tau, 250)
    b_r = lambda tau_val: 1.0 / lambd * (np.exp(-lambd * tau_val) - 1.0)
    theta = hw_theta(lambd, eta, p0t)
    temp1 = lambd * integrate.trapz(theta(t2 - z_grid) * b_r(z_grid), z_grid)
    temp2 = (eta * eta / (4.0 * np.power(lambd, 3.0)) *
             (np.exp(-2.0 * lambd * tau) * (4 * np.exp(lambd * tau) - 1.0) - 3.0) +
             eta * eta * tau / (2.0 * lambd * lambd))
    return temp1 + temp2


def hw_b(lambd, eta, t1, t2):
    return 1.0 / lambd * (np.exp(-lambd * (t2 - t1)) - 1.0)


def hw_zcb(lambd, eta, p0t, t1, t2, r_t1):
    b_r = hw_b(lambd, eta, t1, t2)
    a_r = hw_a(lambd, eta, p0t, t1, t2)
    return np.exp(a_r + b_r * r_t1)


def hw_var_r(lambd, eta, t):
    return eta * eta / (2.0 * lambd) * (1.0 - np.exp(-2.0 * lambd * t))


def hw_mu_frwd_measure(p0t, lambd, eta, t):
    dt = 0.0001
    def f0t_local(tau):
        return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)
    r0 = f0t_local(0.00001)
    theta = hw_theta(lambd, eta, p0t)
    z_grid = np.linspace(0.0, t, 500)
    theta_hat = lambda tau, t_end: theta(tau) + eta * eta / lambd * 1.0 / lambd * (np.exp(-lambd * (t_end - tau)) - 1.0)
    temp = lambda z: theta_hat(z, t) * np.exp(-lambd * (t - z))
    r_mean = r0 * np.exp(-lambd * t) + lambd * integrate.trapz(temp(z_grid), z_grid)
    return r_mean


def hw_zcb_call_put_price(cp, k, lambd, eta, p0t, t1, t2):
    b_r = hw_b(lambd, eta, t1, t2)
    a_r = hw_a(lambd, eta, p0t, t1, t2)
    mu_r = hw_mu_frwd_measure(p0t, lambd, eta, t1)
    v_r = np.sqrt(hw_var_r(lambd, eta, t1))
    k_hat = k * np.exp(-a_r)
    a_coef = (np.log(k_hat) - b_r * mu_r) / (b_r * v_r)
    d1 = a_coef - b_r * v_r
    d2 = d1 + b_r * v_r
    term1 = np.exp(0.5 * b_r * b_r * v_r * v_r + b_r * mu_r) * st.norm.cdf(d1) - k_hat * st.norm.cdf(d2)
    value = p0t(t1) * np.exp(a_r) * term1
    if cp == OptionType.CALL:
        return value
    elif cp == OptionType.PUT:
        return value - p0t(t2) + k * p0t(t1)


def hw_caplet_floorlet_price(cp, notional, k, lambd, eta, p0t, t1, t2):
    if cp == OptionType.CALL:
        n_new = notional * (1.0 + (t2 - t1) * k)
        k_new = 1.0 + (t2 - t1) * k
        caplet = n_new * hw_zcb_call_put_price(OptionType.PUT, 1.0 / k_new, lambd, eta, p0t, t1, t2)
        return caplet
    elif cp == OptionType.PUT:
        n_new = notional * (1.0 + (t2 - t1) * k)
        k_new = 1.0 + (t2 - t1) * k
        floorlet = n_new * hw_zcb_call_put_price(OptionType.CALL, 1.0 / k_new, lambd, eta, p0t, t1, t2)
        return floorlet
    return 0.0


def bs_call_put_option_price(cp, s_0, k, sigma, tau, r):
    if isinstance(k, list):
        k = np.array(k).reshape([len(k), 1])
    d1 = (np.log(s_0 / k) + (r + 0.5 * sigma ** 2.0) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    if cp == OptionType.CALL:
        value = st.norm.cdf(d1) * s_0 - st.norm.cdf(d2) * k * np.exp(-r * tau)
    elif cp == OptionType.PUT:
        value = st.norm.cdf(-d2) * k * np.exp(-r * tau) - st.norm.cdf(-d1) * s_0
    return value


def implied_volatility_black76(cp, market_price, k, t, s_0):
    sigma_grid = np.linspace(0.0, 5.0, 5000)
    opt_price_grid = bs_call_put_option_price(cp, s_0, k, sigma_grid, t, 0.0)
    sigma_initial = np.interp(market_price, opt_price_grid, sigma_grid)
    print("Strike = {0}".format(k))
    print("Initial volatility = {0}".format(sigma_initial))
    func = lambda sigma: np.power(bs_call_put_option_price(cp, s_0, k, sigma, t, 0.0) - market_price, 1.0)
    implied_vol = optimize.newton(func, sigma_initial, tol=1e-15)
    print("Final volatility = {0}".format(implied_vol))
    if implied_vol > 2.0:
        implied_vol = 0.0
    return implied_vol


def generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta):
    dt_diff = 0.0001
    def f0t_local(tau):
        return -(np.log(p0t(tau + dt_diff)) - np.log(p0t(tau - dt_diff))) / (2 * dt_diff)
    r0 = f0t_local(0.00001)
    theta = hw_theta(lambd, eta, p0t)
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)
    dt = t / float(num_steps)
    for i in range(0, num_steps):
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = r[:, i] + lambd * (theta(time[i]) - r[:, i]) * dt + eta * (w[:, i + 1] - w[:, i])
        time[i + 1] = time[i] + dt
    return {"time": time, "R": r}


def main():
    cp = OptionType.CALL
    num_paths = 20000
    num_steps = 1000
    lambd = 0.02
    eta = 0.02
    p0t = lambda t: np.exp(-0.1 * t)

    n = 25
    t_end = 50
    tgrid = np.linspace(0, t_end, n)
    exact = np.zeros((n, 1))
    proxy = np.zeros((n, 1))
    r0 = f0t(0.0001, p0t)
    for i, ti in enumerate(tgrid):
        proxy[i] = hw_zcb(lambd, eta, p0t, 0.0, ti, r0)
        exact[i] = p0t(ti)

    plt.figure(1)
    plt.grid()
    plt.plot(tgrid, exact, '-k')
    plt.plot(tgrid, proxy, '--r')
    plt.legend(["Analytical ZCB", "Monte Carlo ZCB"])
    plt.title('P(0,T) from Monte Carlo vs. Analytical expression')

    t1 = 4.0
    t2 = 8.0
    paths = generate_paths_hw_euler(num_paths, num_steps, t1, p0t, lambd, eta)
    r = paths["R"]
    time_grid = paths["time"]
    dt = time_grid[1] - time_grid[0]
    m_t = np.zeros((num_paths, num_steps))
    for i in range(0, num_paths):
        m_t[i, :] = np.exp(np.cumsum(r[i, :-1]) * dt)

    kvec = np.linspace(0.01, 1.7, 50)
    price_mc_v = np.zeros((len(kvec), 1))
    price_th_v = np.zeros((len(kvec), 1))
    p_t1_t2 = hw_zcb(lambd, eta, p0t, t1, t2, r[:, -1])
    for i, k in enumerate(kvec):
        if cp == OptionType.CALL:
            price_mc_v[i] = np.mean(1.0 / m_t[:, -1] * np.maximum(p_t1_t2 - k, 0.0))
        elif cp == OptionType.PUT:
            price_mc_v[i] = np.mean(1.0 / m_t[:, -1] * np.maximum(k - p_t1_t2, 0.0))
        price_th_v[i] = hw_zcb_call_put_price(cp, k, lambd, eta, p0t, t1, t2)

    plt.figure(2)
    plt.grid()
    plt.plot(kvec, price_mc_v)
    plt.plot(kvec, price_th_v, '--r')
    plt.legend(['Monte Carlo', 'Theoretical'])
    plt.title('Option on ZCB')

    frwd = 1.0 / (t2 - t1) * (p0t(t1) / p0t(t2) - 1.0)
    k = np.linspace(frwd / 2.0, 3.0 * frwd, 25)

    plt.figure(3)
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('implied volatility')
    eta_v = [0.01, 0.02, 0.03, 0.04]
    legend = []
    notional = 1.0
    for eta_temp in eta_v:
        opt_price = hw_caplet_floorlet_price(cp, notional, k, lambd, eta_temp, p0t, t1, t2)
        iv = np.zeros((len(k), 1))
        for idx in range(0, len(k)):
            val_frwd = opt_price[idx] / p0t(t2) / (t2 - t1)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k[idx], t2, frwd)
        plt.plot(k, iv * 100.0)
        legend.append('eta={0}'.format(eta_temp))
    plt.legend(legend)

    plt.figure(4)
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('implied volatility')
    lambda_v = [0.01, 0.03, 0.05, 0.09]
    legend = []
    for lambda_temp in lambda_v:
        opt_price = hw_caplet_floorlet_price(cp, notional, k, lambda_temp, eta, p0t, t1, t2)
        iv = np.zeros((len(k), 1))
        for idx in range(0, len(k)):
            val_frwd = opt_price[idx] / p0t(t2) / (t2 - t1)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k[idx], t2, frwd)
        plt.plot(k, iv * 100.0)
        legend.append('lambda={0}'.format(lambda_temp))
    plt.legend(legend)

    print('frwd={0}'.format(frwd * p0t(t2)))


if __name__ == "__main__":
    main()
