# Compounding Rate Simulation

## Background

Yield curve shapes and the Hull-White model (1 Factor).

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak

---

## What This Code Demonstrates

- Forward Rate and Theta Functions =============
- Hull-White Functions =============
- Plotting Functions =============

---

## Code

```python
"""
Yield curve shapes and the Hull-White model (1 Factor).

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
    """Compute forward rate at time tau."""
    dt = 0.01
    return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)


def hw_theta(lambd, eta, p0t):
    """Compute Hull-White theta function."""
    dt = 0.01

    def theta(tau):
        return (1.0 / lambd * (f0t(tau + dt, p0t) - f0t(tau - dt, p0t)) / (2.0 * dt) +
                f0t(tau, p0t) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))

    return theta


# ============= Hull-White Functions =============

def hw_a(lambd, eta, p0t, t1, t2):
    """Compute Hull-White A function."""
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
    """Compute Hull-White B function."""
    return 1.0 / lambd * (np.exp(-lambd * (t2 - t1)) - 1.0)


def hw_zcb(lambd, eta, p0t, t1, t2, r_t1):
    """Compute zero-coupon bond price under Hull-White."""
    b_r = hw_b(lambd, eta, t1, t2)
    a_r = hw_a(lambd, eta, p0t, t1, t2)
    return np.exp(a_r + b_r * r_t1)


def hw_r_0(p0t, lambd, eta):
    """Compute initial interest rate."""
    return f0t(0.001, p0t)


def generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta):
    """Generate Hull-White interest rate paths."""
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


# ============= Plotting Functions =============

def plot_zcb_comparison(num_paths, num_steps, t_end, p0t, lambd, eta, r0, n):
    """Plot ZCB prices from market and HW model."""
    tgrid = np.linspace(0.1, t_end, n)

    exact = np.zeros((n, 1))
    proxy_1f = np.zeros((n, 1))

    for i, ti in enumerate(tgrid):
        proxy_1f[i] = hw_zcb(lambd, eta, p0t, 0.0, ti, r0)
        exact[i] = p0t(ti)

    plt.figure(1)
    plt.grid()
    plt.xlabel('T')
    plt.ylabel('ZCB, P(0,t)')
    plt.plot(tgrid, exact, '-k')
    plt.plot(tgrid, proxy_1f, '--r')
    plt.legend(["Analytical ZCB", "ZCB - 1F Model"])
    plt.title('P(0,T) from Monte Carlo vs. Analytical expression')


def plot_yield_curves(num_paths, num_steps, t_end, p0t, lambd, eta, r0, n):
    """Plot yield curves from MC paths."""
    paths = generate_paths_hw_euler(num_paths, num_steps, t_end, p0t, lambd, eta)
    r = paths["R"]
    time_grid = paths["time"]

    plt.figure(3)
    plt.xlabel('time')
    plt.ylabel('r(t)')
    plt.title('MC Paths + Yield Curve (Hull-White)')
    plt.grid()

    t_end2 = t_end + 40.0
    tgrid2 = np.linspace(t_end + 0.001, t_end2 - 0.01, n)
    zcb = np.zeros((n, 1))
    r_t = r[:, -1]
    yield_curve = np.zeros((n, 1))

    for i in range(0, 20):
        for j, tj in enumerate(tgrid2):
            zcb[j] = hw_zcb(lambd, eta, p0t, t_end, tj, r_t[i])
            yield_curve[j] = -np.log(zcb[j]) / (tj - t_end)

        plt.plot(tgrid2, yield_curve)
        plt.plot(time_grid, r[i, :])


def main():
    """Main computation for yield curve analysis."""
    num_paths = 20000
    num_steps = 100
    lambd = 0.01
    eta = 0.002

    # Large interpolated ZCB curve data (simplified from original)
    ti = np.linspace(0, 40, 400)
    pi = np.exp(-0.05 * ti)

    interpolator = interpolate.splrep(ti, np.log(pi), s=0.00001)
    p0t = lambda t: np.exp(interpolate.splev(t, interpolator, der=0))
    r0 = hw_r_0(p0t, lambd, eta)

    # Plot ZCB comparison
    n = 20
    t_end0 = 49.0
    plot_zcb_comparison(num_paths, num_steps, t_end0, p0t, lambd, eta, r0, n)

    # Plot yield curves
    t_end = 10.0
    plot_yield_curves(num_paths, num_steps, t_end, p0t, lambd, eta, r0, n)


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The compounding rate over a period $[T_1, T_2]$ in the Hull-White model is $R(T_1, T_2) = -\ln P(T_1, T_2)/(T_2 - T_1)$. Explain how this relates to the short rate $r(t)$.

??? success "Solution to Exercise 1"
    The zero-coupon bond price in the Hull-White model is $P(T_1, T_2) = e^{A(T_1,T_2) + B(T_1,T_2)\,r(T_1)}$. The compounding rate is:

    $$
    R(T_1, T_2) = \frac{-A(T_1,T_2) - B(T_1,T_2)\,r(T_1)}{T_2 - T_1}.
    $$

    This is an affine function of $r(T_1)$, so $R$ inherits the Gaussian distribution of $r(T_1)$. As $T_2 \to T_1$, the compounding rate approaches the instantaneous short rate $r(T_1)$. For longer periods, the coefficients $A$ and $B$ capture the term structure effects (mean reversion and volatility).

---

**Exercise 2.**
If $\lambda = 0.05$ and $\eta = 0.01$, compute the long-run standard deviation of the short rate and the stationary distribution.

??? success "Solution to Exercise 2"
    The stationary variance is $\sigma_\infty^2 = \eta^2/(2\lambda) = 0.0001/0.1 = 0.001$. The stationary standard deviation is $\sigma_\infty = \sqrt{0.001} \approx 0.0316 = 3.16\%$.

    The stationary distribution is $r \sim \mathcal{N}(\theta_\infty, \sigma_\infty^2)$, where $\theta_\infty$ is the long-run mean determined by the initial yield curve. A $3.16\%$ standard deviation means rates typically fluctuate within about $\pm 6\%$ of the long-run mean (two standard deviations).

---

**Exercise 3.**
For a flat initial yield curve at $5\%$, what is $\theta(t)$ in the Hull-White model, and how do paths behave?

??? success "Solution to Exercise 3"
    For a flat curve, $f(0,t) = 5\%$ for all $t$ and $\partial f/\partial t = 0$. The theta function becomes:

    $$
    \theta(t) = f(0,t) + \frac{\eta^2}{2\lambda^2}(1 - e^{-2\lambda t}) = 0.05 + \frac{\eta^2}{2\lambda^2}(1 - e^{-2\lambda t}).
    $$

    For small $\eta$, $\theta(t) \approx 0.05$, so paths mean-revert to approximately $5\%$. The correction term $\eta^2/(2\lambda^2)$ represents a convexity adjustment that slightly lifts $\theta$ above the forward rate.

---

**Exercise 4.**
Explain the difference between a continuously compounded rate and a simply compounded (LIBOR-style) rate in the context of Hull-White simulation.

??? success "Solution to Exercise 4"
    The continuously compounded rate $R_c$ satisfies $P(T_1, T_2) = e^{-R_c(T_2 - T_1)}$, so $R_c = -\ln P/(T_2 - T_1)$.

    The simply compounded rate $L$ satisfies $P(T_1, T_2) = 1/(1 + L \cdot (T_2 - T_1))$, so $L = (1/P - 1)/(T_2 - T_1)$.

    The relationship is $L = (e^{R_c \tau} - 1)/\tau$ where $\tau = T_2 - T_1$. For short periods ($\tau \to 0$), $L \approx R_c$. For longer periods, $L > R_c$ due to the convexity of the exponential function. In Hull-White simulation, one typically simulates the short rate $r(t)$, computes bond prices $P(t,T)$ using the analytical formula, and then converts to the desired compounding convention.
