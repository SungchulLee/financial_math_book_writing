"""
BSHW model and implied volatilities with COS method vs. Black analytic.

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


i = np.complex(0.0, 1.0)
dt = 0.0001


class OptionType(enum.Enum):
    CALL = 1.0
    PUT = -1.0


def call_put_coefficients(cp, a, b, k):
    """Compute COS method coefficients."""
    if cp == OptionType.CALL:
        c = 0.0
        d = b
        psi = np.sin(k * np.pi * (d - a) / (b - a)) - np.sin(k * np.pi * (c - a) / (b - a))
        psi[1:] = psi[1:] * (b - a) / (k[1:] * np.pi)
        psi[0] = d - c
        chi = 1.0 / (1.0 + np.power((k * np.pi / (b - a)), 2.0))
        expr1 = (np.cos(k * np.pi * (d - a) / (b - a)) * np.exp(d) -
                 np.cos(k * np.pi * (c - a) / (b - a)) * np.exp(c))
        expr2 = (k * np.pi / (b - a) * np.sin(k * np.pi * (d - a) / (b - a)) -
                 k * np.pi / (b - a) * np.sin(k * np.pi * (c - a) / (b - a)) * np.exp(c))
        chi = chi * (expr1 + expr2)
        h_k = 2.0 / (b - a) * (chi - psi)
    elif cp == OptionType.PUT:
        c = a
        d = 0.0
        psi = np.sin(k * np.pi * (d - a) / (b - a)) - np.sin(k * np.pi * (c - a) / (b - a))
        psi[1:] = psi[1:] * (b - a) / (k[1:] * np.pi)
        psi[0] = d - c
        chi = 1.0 / (1.0 + np.power((k * np.pi / (b - a)), 2.0))
        expr1 = (np.cos(k * np.pi * (d - a) / (b - a)) * np.exp(d) -
                 np.cos(k * np.pi * (c - a) / (b - a)) * np.exp(c))
        expr2 = (k * np.pi / (b - a) * np.sin(k * np.pi * (d - a) / (b - a)) -
                 k * np.pi / (b - a) * np.sin(k * np.pi * (c - a) / (b - a)) * np.exp(c))
        chi = chi * (expr1 + expr2)
        h_k = 2.0 / (b - a) * (-chi + psi)
    return h_k.reshape([len(h_k), 1])


def call_put_option_price_cos_stoch_ir(cf, cp, s0, tau, k, n, l, p0t):
    """COS method for option pricing with stochastic interest rate."""
    if isinstance(k, list):
        k = np.array(k).reshape([len(k), 1])

    x0 = np.log(s0 / k)
    a = 0.0 - l * np.sqrt(tau)
    b = 0.0 + l * np.sqrt(tau)

    k_vec = np.linspace(0, n - 1, n).reshape([n, 1])
    u = k_vec * np.pi / (b - a)

    h_k = call_put_coefficients(OptionType.PUT, a, b, k_vec)
    mat = np.exp(i * np.outer((x0 - a), u))
    temp = cf(u) * h_k
    temp[0] = 0.5 * temp[0]
    value = k * np.real(mat.dot(temp))

    if cp == OptionType.CALL:
        value = value + s0 - k * p0t
    return value


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


def implied_volatility_black76(cp, market_price, k, t, s_0):
    """Implied volatility."""
    func = lambda sigma: np.power(bs_call_option_price(cp, s_0, k, sigma, t, 0.0) - market_price, 1.0)
    implied_vol = optimize.newton(func, 0.2, tol=1e-9)
    return implied_vol


def ch_bshw(u, t, p0t, lambd, eta, rho, sigma):
    """Characteristic function for BSHW model."""
    def f0t_local(tau):
        return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)
    r0 = f0t_local(0.00001)
    theta = lambda tau: (1.0 / lambd * (f0t_local(tau + dt) - f0t_local(tau - dt)) / (2.0 * dt) +
                         f0t_local(tau) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))
    c = lambda u_val, tau_val: 1.0 / lambd * (i * u_val - 1.0) * (1.0 - np.exp(-lambd * tau_val))

    z_grid = np.linspace(0.0, t, 2500)
    term1 = lambda u_val: 0.5 * sigma * sigma * i * u_val * (i * u_val - 1.0) * t
    term2 = lambda u_val: (i * u_val * rho * sigma * eta / lambd * (i * u_val - 1.0) *
                           (t + 1.0 / lambd * (np.exp(-lambd * t) - 1.0)))
    term3 = lambda u_val: (eta * eta / (4.0 * lambd ** 3.0) * (i + u_val) ** 2.0 *
                           (3.0 + np.exp(-2.0 * lambd * t) - 4.0 * np.exp(-lambd * t) - 2.0 * lambd * t))
    term4 = lambda u_val: lambd * integrate.trapz(theta(t - z_grid) * c(u_val, z_grid), z_grid)
    a = lambda u_val: term1(u_val) + term2(u_val) + term3(u_val) + term4(u_val)

    cf = lambda u_val: np.exp(a(u_val) + c(u_val, t) * r0)

    cf_v = []
    for ui in u:
        cf_v.append(cf(ui))
    return cf_v


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
    k = np.linspace(40.0, 220.0, 100)
    k = np.array(k).reshape([len(k), 1])

    lambd = 0.1
    eta = 0.05
    sigma = 0.2
    rho = 0.3
    s0 = 100
    t = 5.0
    p0t = lambda t_val: np.exp(-0.05 * t_val)

    n = 500
    l = 8

    cf = lambda u: ch_bshw(u, t, p0t, lambd, eta, rho, sigma)
    val_cos = call_put_option_price_cos_stoch_ir(cf, cp, s0, t, k, n, l, p0t(t))
    exact_bshw = bshw_option_price(cp, s0, k, p0t(t), t, eta, sigma, rho, lambd)

    iv = np.zeros((len(k), 1))
    for idx in range(0, len(k)):
        frwd_stock = s0 / p0t(t)
        val_cos_frwd = val_cos[idx] / p0t(t)
        iv[idx] = implied_volatility_black76(cp, val_cos_frwd, k[idx], t, frwd_stock)

    iv_exact = bshw_volatility(t, eta, sigma, rho, lambd)

    print(iv_exact)

    # Plot option prices
    plt.figure(1)
    plt.plot(k, val_cos)
    plt.plot(k, exact_bshw, '--r')
    plt.grid()
    plt.xlabel("strike")
    plt.ylabel("option price")
    plt.legend(["BSHW, COS method", "BSHW, exact solution"])

    # Plot implied volatilities
    plt.figure(2)
    plt.plot(k, iv * 100.0)
    plt.plot(k, np.ones([len(k), 1]) * iv_exact * 100.0, '--r')
    plt.grid()
    plt.xlabel("strike")
    plt.ylabel("Implied Volatility [%]")
    plt.legend(["BSHW, COS method", "BSHW, exact solution"])
    plt.axis([np.min(k), np.max(k), 0, 100])


if __name__ == "__main__":
    main()
