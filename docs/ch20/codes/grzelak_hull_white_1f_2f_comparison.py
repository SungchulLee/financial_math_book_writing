"""
Yield curve shapes with Hull-White 1F and 2F models.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy import interpolate


# ============= Forward Rate and Theta Functions =============

def f0t(tau, p0t):
    """Compute forward rate."""
    dt = 0.01
    return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)


def hw_theta(lambd, eta, p0t):
    """Compute Hull-White theta function."""
    dt = 0.01

    def theta(tau):
        return (1.0 / lambd * (f0t(tau + dt, p0t) - f0t(tau - dt, p0t)) / (2.0 * dt) +
                f0t(tau, p0t) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))

    return theta


# ============= Hull-White 1F Functions =============

def hw_a(lambd, eta, p0t, t1, t2):
    """Compute HW_A function."""
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
    """Compute HW_B function."""
    return 1.0 / lambd * (np.exp(-lambd * (t2 - t1)) - 1.0)


def hw_zcb(lambd, eta, p0t, t1, t2, r_t1):
    """Compute HW ZCB price."""
    b_r = hw_b(lambd, eta, t1, t2)
    a_r = hw_a(lambd, eta, p0t, t1, t2)
    return np.exp(a_r + b_r * r_t1)


def hw2f_zcb(lambd1, lambd2, eta1, eta2, rho, p0t, t1, t2, x_t1, y_t1):
    """Compute 2-factor HW ZCB price."""
    def v_func(t, t_end):
        return ((eta1 ** 2.0) / (lambd1 ** 2.0) * ((t_end - t) + 2.0 / lambd1 * np.exp(-lambd1 * (t_end - t)) -
                1.0 / (2.0 * lambd1) * np.exp(-2.0 * lambd1 * (t_end - t)) - 3.0 / (2.0 * lambd1)) +
                (eta2 ** 2.0) / (lambd2 ** 2.0) * ((t_end - t) + 2.0 / lambd2 * np.exp(-lambd2 * (t_end - t)) -
                1.0 / (2.0 * lambd2) * np.exp(-2.0 * lambd2 * (t_end - t)) - 3.0 / (2.0 * lambd2)) +
                2.0 * rho * eta1 * eta2 / (lambd1 * lambd2) * (t_end - t + 1.0 / lambd1 * (np.exp(-lambd1 * (t_end - t)) - 1.0) +
                1.0 / lambd2 * (np.exp(-lambd2 * (t_end - t)) - 1.0) -
                1.0 / (lambd1 + lambd2) * (np.exp(-(lambd1 + lambd2) * (t_end - t)) - 1.0)))

    int_phi = -np.log(p0t(t2) / p0t(t1) * np.exp(-0.5 * (v_func(0, t2) - v_func(0, t1))))
    a = 1.0 / lambd1 * (1.0 - np.exp(-lambd1 * (t2 - t1)))
    b = 1.0 / lambd2 * (1.0 - np.exp(-lambd2 * (t2 - t1)))

    return np.exp(-int_phi - a * x_t1 - b * y_t1 + 0.5 * v_func(t1, t2))


def hw_r_0(p0t, lambd, eta):
    """Get initial rate."""
    return f0t(0.001, p0t)


def generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta):
    """Generate 1F HW paths."""
    dt_diff = 0.01

    def f0t_local(tau):
        return -(np.log(p0t(tau + dt_diff)) - np.log(p0t(tau - dt_diff))) / (2 * dt_diff)

    r0 = f0t_local(0.01)
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


def generate_paths_hw2f_euler(num_paths, num_steps, t, p0t, lambd1, lambd2, eta1, eta2, rho):
    """Generate 2F HW paths."""
    def phi(tau):
        dt = 0.01
        return (f0t(tau, p0t) + (eta1 ** 2.0) / (2.0 * lambd1 ** 2.0) *
                (1.0 - np.exp(-lambd1 * tau)) ** 2 +
                (eta2 ** 2.0) / (2.0 * lambd2 ** 2.0) *
                (1.0 - np.exp(-lambd2 * tau)) ** 2 +
                rho * eta1 * eta2 / (lambd1 * lambd2) *
                (1.0 - np.exp(-lambd1 * tau)) *
                (1.0 - np.exp(-lambd2 * tau)))

    z1 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    z2 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w1 = np.zeros((num_paths, num_steps + 1))
    w2 = np.zeros((num_paths, num_steps + 1))
    x = np.zeros((num_paths, num_steps + 1))
    y = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = phi(0)
    time = np.zeros(num_steps + 1)

    dt = t / float(num_steps)
    for i in range(0, num_steps):
        if num_paths > 1:
            z1[:, i] = (z1[:, i] - np.mean(z1[:, i])) / np.std(z1[:, i])
            z2[:, i] = (z2[:, i] - np.mean(z2[:, i])) / np.std(z2[:, i])
            z2[:, i] = rho * z1[:, i] + np.sqrt(1.0 - rho ** 2) * z2[:, i]

        w1[:, i + 1] = w1[:, i] + np.sqrt(dt) * z1[:, i]
        w2[:, i + 1] = w2[:, i] + np.sqrt(dt) * z2[:, i]

        x[:, i + 1] = x[:, i] - lambd1 * x[:, i] * dt + eta1 * (w1[:, i + 1] - w1[:, i])
        y[:, i + 1] = y[:, i] - lambd2 * y[:, i] * dt + eta2 * (w2[:, i + 1] - w2[:, i])
        time[i + 1] = time[i] + dt
        r[:, i + 1] = x[:, i + 1] + y[:, i + 1] + phi(time[i + 1])

    return {"time": time, "R": r, "X": x, "Y": y}


def main():
    """Main computation."""
    num_paths = 2000
    num_steps = 100

    lambd = 0.01
    eta = 0.002
    lambd2 = 0.1
    eta2 = 0.002
    rho = -0.2

    # ZCB curve (simplified)
    ti = np.linspace(0, 40, 400)
    pi = np.exp(-0.05 * ti)
    interpolator = interpolate.splrep(ti, pi, s=0.0001)
    p0t = lambda t: interpolate.splev(t, interpolator, der=0)
    r0 = hw_r_0(p0t, lambd, eta)

    # ZCB comparison
    n = 20
    t_end0 = 39.0
    tgrid = np.linspace(0.1, t_end0, n)

    exact = np.zeros((n, 1))
    proxy_1f = np.zeros((n, 1))
    proxy_2f = np.zeros((n, 1))

    for i, ti_val in enumerate(tgrid):
        proxy_1f[i] = hw_zcb(lambd, eta, p0t, 0.0, ti_val, r0)
        proxy_2f[i] = hw2f_zcb(lambd, lambd2, eta, eta2, rho, p0t, 0.0, ti_val, 0.0, 0.0)
        exact[i] = p0t(ti_val)

    plt.figure(1)
    plt.grid()
    plt.plot(tgrid, exact, '-k')
    plt.plot(tgrid, proxy_1f, '--r')
    plt.plot(tgrid, proxy_2f, '.k')
    plt.legend(["Analytical ZCB", "ZCB - 1F Model", "ZCB - 2F Model"])
    plt.title('P(0,T) from Monte Carlo vs. Analytical expression')

    # 2F model analysis
    t_end = 10.0
    paths = generate_paths_hw2f_euler(num_paths, num_steps, t_end, p0t, lambd, lambd2, eta, eta2, rho)
    x = paths["X"]
    y = paths["Y"]
    r = paths["R"]
    time_grid = paths["time"]

    plt.figure(4)
    plt.xlabel('time')
    plt.ylabel('r(t)')
    plt.title('MC Paths + Yield Curve (Hull-White 2F)')
    plt.grid()

    x_t = x[:, -1]
    y_t = y[:, -1]
    t_end2 = t_end + 40.0
    tgrid2 = np.linspace(t_end + 0.001, t_end2, n)
    zcb = np.zeros((n, 1))

    for i in range(0, 20):
        for j, tj in enumerate(tgrid2):
            zcb[j] = hw2f_zcb(lambd, lambd2, eta, eta2, rho, p0t, t_end, tj, x_t[i], y_t[i])

        plt.plot(time_grid, r[i, :])
        plt.plot(tgrid2, zcb)


if __name__ == "__main__":
    main()
