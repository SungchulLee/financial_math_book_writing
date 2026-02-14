"""
Shifted GBM and pricing of caplets/floorlets.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import enum
import scipy.optimize as optimize


class OptionType(enum.Enum):
    CALL = 1.0
    PUT = -1.0


def generate_paths_gbm(num_paths, num_steps, t, r, sigma, s_0):
    """Generate GBM paths."""
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    x = np.zeros((num_paths, num_steps + 1))
    w = np.zeros((num_paths, num_steps + 1))
    time = np.zeros(num_steps + 1)

    x[:, 0] = np.log(s_0)
    dt = t / float(num_steps)
    for i in range(0, num_steps):
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        x[:, i + 1] = x[:, i] + (r - 0.5 * sigma * sigma) * dt + sigma * (w[:, i + 1] - w[:, i])
        time[i + 1] = time[i] + dt

    s = np.exp(x)
    return {"time": time, "S": s}


def generate_paths_gbm_shifted(num_paths, num_steps, t, r, sigma, s_0, shift):
    """Generate shifted GBM paths."""
    s_0_shift = s_0 + shift
    if s_0_shift < 0.0:
        raise Exception('Shift is too small!')

    paths = generate_paths_gbm(num_paths, num_steps, t, r, sigma, s_0_shift)
    s_shifted = paths["S"] - shift
    time = paths["time"]
    return {"time": time, "S": s_shifted}


def bs_call_put_option_price(cp, s_0, k, sigma, tau, r):
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


def bs_call_put_option_price_shifted(cp, s_0, k, sigma, tau, r, shift):
    """Black-Scholes option price for shifted GBM."""
    k_new = k + shift
    s_0_new = s_0 + shift
    return bs_call_put_option_price(cp, s_0_new, k_new, sigma, tau, r)


def implied_volatility_black76(cp, market_price, k, t, s_0):
    """Implied volatility using Black76."""
    sigma_grid = np.linspace(0.0, 2.0, 5000)
    opt_price_grid = bs_call_put_option_price(cp, s_0, k, sigma_grid, t, 0.0)
    sigma_initial = np.interp(market_price, opt_price_grid, sigma_grid)
    print("Initial volatility = {0}".format(sigma_initial))
    func = lambda sigma: np.power(bs_call_put_option_price(cp, s_0, k, sigma, t, 0.0) - market_price, 1.0)
    implied_vol = optimize.newton(func, sigma_initial, tol=1e-15)
    print("Final volatility = {0}".format(implied_vol))
    return implied_vol


def main():
    """Main computation."""
    num_paths = 10000
    num_steps = 500
    t = 3.0
    sigma = 0.2
    l0 = -0.05
    shift = 0.1
    k = [0.95]
    cp = OptionType.CALL

    p0t = lambda t: np.exp(-0.1 * t)

    np.random.seed(4)
    paths = generate_paths_gbm_shifted(num_paths, num_steps, t, 0.0, sigma, l0, shift)
    time = paths["time"]
    l = paths["S"]

    print(np.mean(l[:, -1]))

    # Plot first few paths
    plt.figure(1)
    plt.plot(time, np.transpose(l[0:20, :]))
    plt.grid()

    # Shifted lognormal for different shift parameters
    plt.figure(2)
    shift_v = [1.0, 2.0, 3.0, 4.0, 5.0]
    legend = []
    for shift_temp in shift_v:
        x = np.linspace(-shift_temp, 10, 1000)
        lognnorm_pdf = lambda x, t: st.lognorm.pdf(x + shift_temp,
                                                    scale=np.exp(np.log(l0 + shift_temp) + (-0.5 * sigma * sigma) * t),
                                                    s=np.sqrt(t) * sigma)
        pdf_x = lognnorm_pdf(x, t)
        plt.plot(x, pdf_x)
        legend.append('shift={0}'.format(shift_temp))
    plt.legend(legend)
    plt.xlabel('x')
    plt.ylabel('pdf')
    plt.title('shifted lognormal density')
    plt.grid()

    # Call/Put option prices, MC vs. Analytical
    plt.figure(3)
    k = np.linspace(-shift, np.abs(l0) * 3, 25)
    opt_price_mcv = np.zeros((len(k), 1))
    for idx in range(0, len(k)):
        opt_price_mcv[idx] = 0.0
        if cp == OptionType.CALL:
            opt_price_mcv[idx] = p0t(t) * np.mean(np.maximum(l[:, -1] - k[idx], 0.0))
        elif cp == OptionType.PUT:
            opt_price_mcv[idx] = p0t(t) * np.mean(np.maximum(k[idx] - l[:, -1], 0.0))

    opt_price_exact = p0t(t) * bs_call_put_option_price_shifted(cp, l0, k, sigma, t, 0.0, shift)
    plt.plot(k, opt_price_mcv)
    plt.plot(k, opt_price_exact, '--r')
    plt.grid()
    plt.xlabel('strike,K')
    plt.ylabel('option price')
    plt.legend(['Monte Carlo', 'Exact'])

    # Shift Effect on Option prices
    plt.figure(4)
    legend = []
    for shift_temp in [0.2, 0.3, 0.4, 0.5]:
        k = np.linspace(-shift_temp, np.abs(l0) * 6.0, 25)
        opt_price_exact = p0t(t) * bs_call_put_option_price_shifted(cp, l0, k, sigma, t, 0.0, shift_temp)
        plt.plot(k, opt_price_exact)
        legend.append('shift={0}'.format(shift_temp))
    plt.grid()
    plt.xlabel('strike,K')
    plt.ylabel('option price')
    plt.legend(legend)


if __name__ == "__main__":
    main()
