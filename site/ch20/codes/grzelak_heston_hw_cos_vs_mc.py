"""
Heston-Hull-White model pricing with Monte Carlo and COS method comparison.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import scipy.integrate as integrate
import enum


class OptionType(enum.Enum):
    CALL = 1.0
    PUT = -1.0


def call_put_coefficients(cp, a, b, k):
    """Compute COS coefficients."""
    if cp == OptionType.CALL:
        c = 0.0
        d = b
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

    if cp == OptionType.CALL:
        h_k = 2.0 / (b - a) * (chi - psi)
    elif cp == OptionType.PUT:
        h_k = 2.0 / (b - a) * (-chi + psi)

    return h_k.reshape([len(h_k), 1])


def call_put_option_price_cos_stoch_ir(cf, cp, s0, tau, k, n, l, p0t):
    """COS method with stochastic interest rate."""
    if isinstance(k, list):
        k = np.array(k).reshape([len(k), 1])

    i = np.complex(0.0, 1.0)
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


def eu_option_price_from_mc_paths_generalized_stoch_ir(cp, s, k, t, m):
    """Compute option price from Monte Carlo paths."""
    result = np.zeros([len(k), 1])
    if cp == OptionType.CALL:
        for (idx, ki) in enumerate(k):
            result[idx] = np.mean(1.0 / m * np.maximum(s - ki, 0.0))
    elif cp == OptionType.PUT:
        for (idx, ki) in enumerate(k):
            result[idx] = np.mean(1.0 / m * np.maximum(ki - s, 0.0))
    return result


def cir_sample(num_paths, kappa, gamma, vbar, s, t, v_s):
    """CIR sampling."""
    delta = 4.0 * kappa * vbar / gamma / gamma
    c = 1.0 / (4.0 * kappa) * gamma * gamma * (1.0 - np.exp(-kappa * (t - s)))
    kappa_bar = 4.0 * kappa * v_s * np.exp(-kappa * (t - s)) / (gamma * gamma * (1.0 - np.exp(-kappa * (t - s))))
    sample = c * np.random.noncentral_chisquare(delta, kappa_bar, num_paths)
    return sample


def generate_paths_heston_hw_euler(num_paths, num_steps, p0t, t, s_0, kappa, gamma, rhoxr, rhoxv, vbar, v0, lambd, eta):
    """Generate Heston-HW paths with Euler scheme."""
    dt_diff = 0.0001

    def f0t_local(tau):
        return -(np.log(p0t(tau + dt_diff)) - np.log(p0t(tau - dt_diff))) / (2 * dt_diff)

    r0 = f0t_local(0.00001)

    def theta(tau):
        return (1.0 / lambd * (f0t_local(tau + dt_diff) - f0t_local(tau - dt_diff)) / (2.0 * dt_diff) +
                f0t_local(tau) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))

    z1 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    z2 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    z3 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w1 = np.zeros((num_paths, num_steps + 1))
    w2 = np.zeros((num_paths, num_steps + 1))
    w3 = np.zeros((num_paths, num_steps + 1))
    v = np.zeros((num_paths, num_steps + 1))
    x = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    m_t = np.ones((num_paths, num_steps + 1))
    r[:, 0] = r0
    v[:, 0] = v0
    x[:, 0] = np.log(s_0)

    time = np.zeros(num_steps + 1)
    dt = t / float(num_steps)
    for i in range(0, num_steps):
        if num_paths > 1:
            z1[:, i] = (z1[:, i] - np.mean(z1[:, i])) / np.std(z1[:, i])
            z2[:, i] = (z2[:, i] - np.mean(z2[:, i])) / np.std(z2[:, i])
            z3[:, i] = (z3[:, i] - np.mean(z3[:, i])) / np.std(z3[:, i])

        w1[:, i + 1] = w1[:, i] + np.sqrt(dt) * z1[:, i]
        w2[:, i + 1] = w2[:, i] + np.sqrt(dt) * z2[:, i]
        w3[:, i + 1] = w3[:, i] + np.sqrt(dt) * z3[:, i]

        r[:, i + 1] = r[:, i] + lambd * (theta(time[i]) - r[:, i]) * dt + eta * (w1[:, i + 1] - w1[:, i])
        m_t[:, i + 1] = m_t[:, i] * np.exp(0.5 * (r[:, i + 1] + r[:, i]) * dt)
        v[:, i + 1] = v[:, i] + kappa * (vbar - v[:, i]) * dt + gamma * np.sqrt(v[:, i]) * (w2[:, i + 1] - w2[:, i])
        v[:, i + 1] = np.maximum(v[:, i + 1], 0.0)

        term1 = (rhoxr * (w1[:, i + 1] - w1[:, i]) + rhoxv * (w2[:, i + 1] - w2[:, i]) +
                 np.sqrt(1.0 - rhoxr * rhoxr - rhoxv * rhoxv) * (w3[:, i + 1] - w3[:, i]))

        x[:, i + 1] = x[:, i] + (r[:, i] - 0.5 * v[:, i]) * dt + np.sqrt(v[:, i]) * term1
        time[i + 1] = time[i] + dt

        # Moment matching component
        a = s_0 / np.mean(np.exp(x[:, i + 1]) / m_t[:, i + 1])
        x[:, i + 1] = x[:, i + 1] + np.log(a)

    s = np.exp(x)
    return {"time": time, "S": s, "R": r, "M_t": m_t}


def mean_sqrt_v(kappa, v0, vbar, gamma):
    """Expected value of sqrt(V(t))."""
    delta = 4.0 * kappa * vbar / gamma / gamma

    def c(t):
        return 1.0 / (4.0 * kappa) * gamma * gamma * (1.0 - np.exp(-kappa * t))

    def kappa_bar(t):
        return 4.0 * kappa * v0 * np.exp(-kappa * t) / (gamma * gamma * (1.0 - np.exp(-kappa * t)))

    def temp(t):
        return (np.sqrt(2.0 * c(t)) * sp.gamma((1.0 + delta) / 2.0) / sp.gamma(delta / 2.0) *
                sp.hyp1f1(-0.5, delta / 2.0, -kappa_bar(t) / 2.0))

    return temp


def c_h1hw(u, tau, lambd):
    """C function for Heston-HW."""
    i = np.complex(0.0, 1.0)
    c = (i * u - 1.0) / lambd * (1 - np.exp(-lambd * tau))
    return c


def d_h1hw(u, tau, kappa, gamma, rhoxv):
    """D function for Heston-HW."""
    i = np.complex(0.0, 1.0)
    d1 = np.sqrt(np.power(kappa - gamma * rhoxv * i * u, 2) + (u * u + i * u) * gamma * gamma)
    g = (kappa - gamma * rhoxv * i * u - d1) / (kappa - gamma * rhoxv * i * u + d1)
    c = ((1.0 - np.exp(-d1 * tau)) / (gamma * gamma * (1.0 - g * np.exp(-d1 * tau))) *
         (kappa - gamma * rhoxv * i * u - d1))
    return c


def a_h1hw(u, tau, p0t, lambd, eta, kappa, gamma, vbar, v0, rhoxv, rhoxr):
    """A function for Heston-HW."""
    i = np.complex(0.0, 1.0)
    dt_diff = 0.0001

    def f0t_local(t):
        return -(np.log(p0t(t + dt_diff)) - np.log(p0t(t - dt_diff))) / (2.0 * dt_diff)

    def theta(t):
        return (1.0 / lambd * (f0t_local(t + dt_diff) - f0t_local(t - dt_diff)) / (2.0 * dt_diff) +
                f0t_local(t) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * t)))

    d1 = np.sqrt(np.power(kappa - gamma * rhoxv * i * u, 2) + (u * u + i * u) * gamma * gamma)
    g = (kappa - gamma * rhoxv * i * u - d1) / (kappa - gamma * rhoxv * i * u + d1)

    n = 500
    z = np.linspace(0, tau - 1e-10, n)
    f1 = (1.0 - np.exp(-lambd * z)) * theta(tau - z)
    value1 = integrate.trapz(f1, z)

    i_1_adj = (i * u - 1.0) * value1
    i_2 = (tau / (gamma ** 2.0) * (kappa - gamma * rhoxv * i * u - d1) -
           2.0 / (gamma ** 2.0) * np.log((1.0 - g * np.exp(-d1 * tau)) / (1.0 - g)))
    i_3 = (1.0 / (2.0 * lambd ** 3.0) * (i + u) ** 2.0 *
           (3.0 + np.exp(-2.0 * lambd * tau) - 4.0 * np.exp(-lambd * tau) - 2.0 * lambd * tau))

    mean_sqrt_v_func = mean_sqrt_v(kappa, v0, vbar, gamma)
    f2 = mean_sqrt_v_func(tau - z) * (1.0 - np.exp(-lambd * z))
    value2 = integrate.trapz(f2, z)
    i_4 = -1.0 / lambd * (i * u + u ** 2.0) * value2

    return i_1_adj + kappa * vbar * i_2 + 0.5 * eta ** 2.0 * i_3 + eta * rhoxr * i_4


def ch_h1hw_model(p0t, lambd, eta, tau, kappa, gamma, vbar, v0, rhoxv, rhoxr):
    """Characteristic function for H1HW model."""
    dt_diff = 0.0001

    def f0t_local(t):
        return -(np.log(p0t(t + dt_diff)) - np.log(p0t(t - dt_diff))) / (2.0 * dt_diff)

    r0 = f0t_local(0.00001)
    c = lambda u: c_h1hw(u, tau, lambd)
    d = lambda u: d_h1hw(u, tau, kappa, gamma, rhoxv)
    a = lambda u: a_h1hw(u, tau, p0t, lambd, eta, kappa, gamma, vbar, v0, rhoxv, rhoxr)
    cf = lambda u: np.exp(a(u) + c(u) * r0 + d(u) * v0)
    return cf


def main():
    """Main computation."""
    cp = OptionType.CALL

    num_paths = 10000
    num_steps = 500

    lambd = 1.12
    eta = 0.01
    s0 = 100.0
    t = 15.0
    r = 0.1

    # Strike range
    k = np.linspace(.01, 1.8 * s0 * np.exp(r * t), 20)
    k = np.array(k).reshape([len(k), 1])

    # ZCB curve
    p0t = lambda t_val: np.exp(-r * t_val)

    # COS method settings
    n = 2000
    l = 15

    gamma = 0.3
    vbar = 0.05
    v0 = 0.02
    rhoxr = 0.5
    rhoxv = -0.8
    kappa = 0.5

    np.random.seed(1)
    paths = generate_paths_heston_hw_euler(num_paths, num_steps, p0t, t, s0, kappa, gamma, rhoxr, rhoxv, vbar, v0, lambd, eta)
    s = paths["S"]
    m_t = paths["M_t"]

    print(np.mean(s[:, -1] / m_t[:, -1]))
    value_opt_mc = eu_option_price_from_mc_paths_generalized_stoch_ir(cp, s[:, -1], k, t, m_t[:, -1])

    # COS method
    cf2 = ch_h1hw_model(p0t, lambd, eta, t, kappa, gamma, vbar, v0, rhoxv, rhoxr)
    u = np.array([1.0, 2.0, 3.0])
    print(cf2(u))
    val_cos = call_put_option_price_cos_stoch_ir(cf2, cp, s0, t, k, n, l, p0t(t))

    plt.figure(1)
    plt.plot(k, value_opt_mc)
    plt.plot(k, val_cos, '--r')
    plt.ylim([0.0, 110.0])
    plt.legend(['Euler', 'COS'])
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('EU Option Value, K')
    print("Value from the COS method:")
    print(val_cos)


if __name__ == "__main__":
    main()
