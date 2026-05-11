# Swaps under Hull-White

## Background

Swaps computed from yield curve and Hull-White Model.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak

---

## Code

```python
"""
Swaps computed from yield curve and Hull-White Model.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import enum
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy import interpolate
from scipy.optimize import newton


# ======================================================================

class OptionTypeSwap(enum.Enum):
    RECEIVER = 1.0
    PAYER = -1.0


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
    n = np.size(r_t1)
    if t1 < t2:
        b_r = hw_b(lambd, eta, t1, t2)
        a_r = hw_a(lambd, eta, p0t, t1, t2)
        return np.exp(a_r + b_r * r_t1)
    else:
        return np.ones([n])


def hw_r_0(p0t, lambd, eta):
    dt = 0.0001
    return -(np.log(p0t(dt)) - np.log(p0t(-dt))) / (2 * dt)


def swap_price(cp, notional, k, t, ti, tm, n, p0t):
    """Compute swap price from market ZCB curve."""
    if n == 1:
        ti_grid = np.array([ti, tm])
    else:
        ti_grid = np.linspace(ti, tm, n)
    tau = ti_grid[1] - ti_grid[0]

    prev_ti = ti_grid[np.where(ti_grid < t)]
    if np.size(prev_ti) > 0:
        ti = prev_ti[-1]

    ti_grid = ti_grid[np.where(ti_grid > t)]

    temp = 0.0
    for (idx, ti_val) in enumerate(ti_grid):
        if ti_val > ti:
            temp = temp + tau * p0t(ti_val)

    if cp == OptionTypeSwap.PAYER:
        swap = (p0t(ti) - p0t(tm)) - k * temp
    elif cp == OptionTypeSwap.RECEIVER:
        swap = k * temp - (p0t(ti) - p0t(tm))

    return swap * notional


def hw_swap_price(cp, notional, k, t, ti, tm, n, r_t, p0t, lambd, eta):
    """Compute swap price from HW model."""
    if n == 1:
        ti_grid = np.array([ti, tm])
    else:
        ti_grid = np.linspace(ti, tm, n)
    tau = ti_grid[1] - ti_grid[0]

    prev_ti = ti_grid[np.where(ti_grid < t)]
    if np.size(prev_ti) > 0:
        ti = prev_ti[-1]

    ti_grid = ti_grid[np.where(ti_grid > t)]

    temp = np.zeros(np.size(r_t))
    p_t_ti_lambda = lambda ti_val: hw_zcb(lambd, eta, p0t, t, ti_val, r_t)

    for (idx, ti_val) in enumerate(ti_grid):
        if ti_val > ti:
            temp = temp + tau * p_t_ti_lambda(ti_val)

    p_t_ti = p_t_ti_lambda(ti)
    p_t_tm = p_t_ti_lambda(tm)

    if cp == OptionTypeSwap.PAYER:
        swap = (p_t_ti - p_t_tm) - k * temp
    elif cp == OptionTypeSwap.RECEIVER:
        swap = k * temp - (p_t_ti - p_t_tm)

    return swap * notional


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
    """Main computation."""
    num_paths = 2000
    num_steps = 1000
    cp = OptionTypeSwap.PAYER
    lambd = 0.5
    eta = 0.03
    notional = 10000.0

    ti = np.linspace(0, 40, 400)
    pi = np.exp(-0.05 * ti)
    interpolator = interpolate.splrep(ti, pi, s=0.0001)
    p0t = lambda t: interpolate.splev(t, interpolator, der=0)
    r0 = hw_r_0(p0t, lambd, eta)

    # Swap settings
    k = np.linspace(-0.1, 0.1, 25)
    ti_swap = 1.0
    tm_swap = 10.0
    n_swap = 10

    paths = generate_paths_hw_euler(num_paths, num_steps, tm_swap + 1.0, p0t, lambd, eta)
    r = paths["R"]
    time_grid = paths["time"]
    dt = time_grid[1] - time_grid[0]

    m_t = np.zeros((num_paths, num_steps))
    for i in range(0, num_paths):
        m_t[i, :] = np.exp(np.cumsum(r[i, 0:-1]) * dt)

    v_swap_hw = np.zeros(len(k))
    v_swap = np.zeros(len(k))
    t0 = 0
    for (idx, ki) in enumerate(k):
        v_hw = hw_swap_price(cp, notional, ki, t0, ti_swap, tm_swap, n_swap, r0, p0t, lambd, eta)
        v = swap_price(cp, notional, ki, t0, ti_swap, tm_swap, n_swap, p0t)
        v_swap[idx] = v
        v_swap_hw[idx] = v_hw[0]

    plt.figure(2)
    plt.plot(k, v_swap)
    plt.plot(k, v_swap_hw, '--r')
    plt.grid()
    plt.xlabel('strike,K')
    plt.ylabel('Swap value')
    plt.title('Swap pricing')

    # Swap par
    k = 0.0
    print('Swap price for K = 0 is {0}'.format(swap_price(cp, notional, k, t0, ti_swap, tm_swap, n_swap, p0t)))

    # Determine par swap
    func = lambda ki: swap_price(cp, notional, ki, t0, ti_swap, tm_swap, n_swap, p0t)
    k_par = newton(func, 0.0)
    print('Swap price for K_par = {0} is {1}'.format(k_par, swap_price(cp, notional, k_par, t0, ti_swap, tm_swap, n_swap, p0t)))


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
A payer interest rate swap has value $V = P(0, T_0) - P(0, T_n) - K\sum_{i=1}^n \tau_i P(0, T_i)$. If the yield curve is flat at $4\%$ and the swap has quarterly payments over 5 years with $K = 4\%$, show that $V \approx 0$.

??? success "Solution to Exercise 1"
    With a flat curve at $4\%$: $P(0,T) = e^{-0.04T}$, $P(0,0) = 1$, $P(0,5) = e^{-0.2} = 0.8187$. The annuity is $\sum_{i=1}^{20} 0.25 \times e^{-0.04 \times 0.25i}$.

    The par swap rate for this annuity equals $K_{\text{par}} = (1 - P(0,5))/A$ where $A = \sum \tau_i P(0,T_i)$. If $K = K_{\text{par}} = 4\%$ (approximately, for a flat curve), then $V = 0$ by definition of the par rate. The small discrepancy between $4\%$ simple and $4\%$ continuous compounding may produce a residual on the order of basis points.

---

**Exercise 2.**
Under the Hull-White model, the swap rate at time $t$ is stochastic. Express $S(t) = (P(t, T_0) - P(t, T_n))/\sum \tau_i P(t, T_i)$ and explain its distribution.

??? success "Solution to Exercise 2"
    Each $P(t, T_i) = e^{A(t,T_i) + B(t,T_i)\,r(t)}$ is an exponential-affine function of $r(t)$, which is Gaussian. The swap rate $S(t)$ is a ratio of sums of exponentials:

    $$
    S(t) = \frac{e^{A_0 + B_0 r} - e^{A_n + B_n r}}{\sum_i \tau_i e^{A_i + B_i r}}.
    $$

    This is not Gaussian -- it is a nonlinear function of the Gaussian variable $r(t)$. For moderate rate volatility, $S(t)$ is approximately Gaussian (first-order expansion), but for large $\eta$ or long maturities, the nonlinearity becomes important and produces skew in the swap rate distribution.

---

**Exercise 3.**
Compute the 5-year par swap rate for the discount factors $P(0,1) = 0.97$, $P(0,2) = 0.94$, $P(0,3) = 0.91$, $P(0,4) = 0.88$, $P(0,5) = 0.85$ with annual payments.

??? success "Solution to Exercise 3"
    The annuity is $A = 1 \times (0.97 + 0.94 + 0.91 + 0.88 + 0.85) = 4.55$. The par rate is:

    $$
    K = \frac{P(0,0) - P(0,5)}{A} = \frac{1 - 0.85}{4.55} = \frac{0.15}{4.55} = 0.03297 = 3.30\%.
    $$

---

**Exercise 4.**
Explain how the Hull-White model is used to compute the DV01 (dollar value of a basis point) of a swap.

??? success "Solution to Exercise 4"
    The DV01 measures the change in swap value for a 1 basis point parallel shift in the yield curve. Under Hull-White:

    1. Price the swap at the current curve: $V_0$.
    2. Shift the entire initial yield curve up by 1 bp: $P_{\text{new}}(0,T) = P(0,T)\,e^{-0.0001 T}$.
    3. Recalibrate $\theta(t)$ to the shifted curve.
    4. Reprice the swap: $V_{\text{up}}$.
    5. $\text{DV01} = V_{\text{up}} - V_0$.

    This captures both the direct discounting effect and the model-implied change in expected future rates. For a par swap, the DV01 is approximately equal to the annuity value $A$, scaled by the notional and 1 bp.
