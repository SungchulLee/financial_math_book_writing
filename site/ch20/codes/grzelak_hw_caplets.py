"""
Caplets under the Hull-White Model.

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


class OptionType(enum.Enum):
    """Option type enumeration."""
    CALL = 1.0
    PUT = -1.0


# ============= Forward Rate and Theta Functions =============

def f0t(tau, p0t):
    """Compute forward rate."""
    dt = 0.0001
    return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)


def hw_theta(lambd, eta, p0t):
    """Compute Hull-White theta function."""
    dt = 0.0001

    def theta(tau):
        return (1.0 / lambd * (f0t(tau + dt, p0t) - f0t(tau - dt, p0t)) / (2.0 * dt) +
                f0t(tau, p0t) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))

    return theta


# ============= HW Functions =============

def hw_a(lambd, eta, p0t, t1, t2):
    """Compute HW A function."""
    tau = t2 - t1
    z_grid = np.linspace(0.0, tau, 250)

    def b_r(tau_val):
        return 1.0 / lambd * (np.exp(-lambd * tau_val) - 1.0)

    theta = hw_theta(lambd, eta, p0t)
    temp1 = lambd * integrate.trapz(theta(t2 - z_grid) * b_r(z_grid), z_grid)
    temp2 = (eta * eta / (4.0 * np.power(lambd, 3.0)) *
             (np.exp(-2.0 * lambd * tau) * (4 * np.exp(lambd * tau) - 1.0) - 3.0) +
             eta * eta * tau / (2.0 * lambd * lambd))
    return temp1 + temp2


def hw_b(lambd, eta, t1, t2):
    """Compute HW B function."""
    return 1.0 / lambd * (np.exp(-lambd * (t2 - t1)) - 1.0)


def hw_zcb(lambd, eta, p0t, t1, t2, r_t1):
    """Compute ZCB price."""
    b_r = hw_b(lambd, eta, t1, t2)
    a_r = hw_a(lambd, eta, p0t, t1, t2)
    return np.exp(a_r + b_r * r_t1)


def hw_mean_r(p0t, lambd, eta, t):
    """Compute mean of interest rate."""
    dt = 0.0001

    def f0t_local(tau):
        return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2.0 * dt)

    r0 = f0t_local(0.00001)
    theta = hw_theta(lambd, eta, p0t)
    z_grid = np.linspace(0.0, t, 2500)

    def temp(z):
        return theta(z) * np.exp(-lambd * (t - z))

    r_mean = r0 * np.exp(-lambd * t) + lambd * integrate.trapz(temp(z_grid), z_grid)
    return r_mean


def hw_var_r(lambd, eta, t):
    """Compute variance of interest rate."""
    return eta * eta / (2.0 * lambd) * (1.0 - np.exp(-2.0 * lambd * t))


def hw_r_0(p0t, lambd, eta):
    """Get initial interest rate."""
    dt = 0.0001
    return -(np.log(p0t(dt)) - np.log(p0t(-dt))) / (2 * dt)


def hw_mu_frwd_measure(p0t, lambd, eta, t):
    """Compute mean under forward measure."""
    dt = 0.0001

    def f0t_local(tau):
        return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)

    r0 = f0t_local(0.00001)
    theta = hw_theta(lambd, eta, p0t)
    z_grid = np.linspace(0.0, t, 500)

    def theta_hat(tau, t_end):
        return theta(tau) + eta * eta / lambd * 1.0 / lambd * (np.exp(-lambd * (t_end - tau)) - 1.0)

    def temp(z):
        return theta_hat(z, t) * np.exp(-lambd * (t - z))

    r_mean = r0 * np.exp(-lambd * t) + lambd * integrate.trapz(temp(z_grid), z_grid)
    return r_mean


def hw_zcb_call_put_price(cp, k, lambd, eta, p0t, t1, t2):
    """Compute call/put price on ZCB."""
    b_r = hw_b(lambd, eta, t1, t2)
    a_r = hw_a(lambd, eta, p0t, t1, t2)

    mu_r = hw_mu_frwd_measure(p0t, lambd, eta, t1)
    v_r = np.sqrt(hw_var_r(lambd, eta, t1))

    k_hat = k * np.exp(-a_r)
    a_coef = (np.log(k_hat) - b_r * mu_r) / (b_r * v_r)

    d1 = a_coef - b_r * v_r
    d2 = d1 + b_r * v_r

    term1 = (np.exp(0.5 * b_r * b_r * v_r * v_r + b_r * mu_r) * st.norm.cdf(d1) -
             k_hat * st.norm.cdf(d2))
    value = p0t(t1) * np.exp(a_r) * term1

    if cp == OptionType.CALL:
        return value
    elif cp == OptionType.PUT:
        return value - p0t(t2) + k * p0t(t1)


def hw_caplet_price(cp, notional, k, lambd, eta, p0t, t1, t2):
    """Compute caplet price."""
    if cp == OptionType.CALL:
        n_new = notional * (1.0 + (t2 - t1) * k)
        k_new = 1.0 + (t2 - t1) * k
        caplet = n_new * hw_zcb_call_put_price(OptionType.PUT, 1.0 / k_new, lambd, eta, p0t, t1, t2)
        return caplet
    elif cp == OptionType.PUT:
        return 0.0


def generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta):
    """Generate HW paths."""
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


# ============= Main =============

def main():
    """Main computation for caplet pricing."""
    cp = OptionType.CALL
    num_paths = 20000
    num_steps = 1000
    lambd = 0.02
    eta = 0.02

    # ZCB curve
    p0t = lambda t: np.exp(-0.1 * t)
    r0 = hw_r_0(p0t, lambd, eta)

    # ZCB pricing
    n = 25
    t_end = 50
    tgrid = np.linspace(0, t_end, n)

    exact = np.zeros((n, 1))
    proxy = np.zeros((n, 1))
    for i, ti in enumerate(tgrid):
        proxy[i] = hw_zcb(lambd, eta, p0t, 0.0, ti, r0)
        exact[i] = p0t(ti)

    plt.figure(1)
    plt.grid()
    plt.plot(tgrid, exact, '-k')
    plt.plot(tgrid, proxy, '--r')
    plt.legend(["Analytical ZCB", "Monte Carlo ZCB"])
    plt.title('P(0,T) from Monte Carlo vs. Analytical expression')

    # Caplet pricing
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

    # Caplet pricing
    frwd = 1.0 / (t2 - t1) * (p0t(t1) / p0t(t2) - 1.0)
    k = np.linspace(frwd / 2.0, 3.0 * frwd, 25)
    notional = 1.0

    caplet_price = np.zeros(len(k))
    for idx in range(0, len(k)):
        caplet_price[idx] = hw_caplet_price(cp, notional, k[idx], lambd, eta, p0t, t1, t2)

    plt.figure(3)
    plt.title('Caplet Price')
    plt.plot(k, caplet_price)
    plt.xlabel('strike')
    plt.ylabel('Caplet Price')
    plt.grid()


if __name__ == "__main__":
    main()
