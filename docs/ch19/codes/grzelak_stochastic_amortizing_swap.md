# Stochastic Amortizing Swap

## Background

Stochastic amortization of mortgages with incentive function and rational behavior.

Based on "Financial Engineering" course by L.A. Grzelak and Emanuele Cassamassima.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak and Emanuele Cassamassima

---

## Code

```python
"""
Stochastic amortization of mortgages with incentive function and rational behavior.

Based on "Financial Engineering" course by L.A. Grzelak and Emanuele Cassamassima.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak and Emanuele Cassamassima
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import scipy.integrate as integrate


# ======================================================================
# Functions / Classes
# ======================================================================


def generate_paths_hw_euler(num_paths, num_steps, T, p0t, lmbda, eta):
    """
    Generate Hull-White model paths using Euler scheme.

    Parameters
    ----------
    num_paths : int
        Number of simulation paths
    num_steps : int
        Number of time steps
    T : float
        Time to maturity
    p0t : callable
        Zero-coupon bond pricing function
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility parameter

    Returns
    -------
    dict
        Dictionary with keys 'time' and 'R' containing time grid and rate paths
    """
    dt = 0.0001
    def f0t_calc(t):
        """Calculate forward rate."""
        return -(np.log(p0t(t + dt)) - np.log(p0t(t - dt))) / (2 * dt)

    r0 = f0t_calc(0.00001)
    def theta(t):
        """Theta function for HW model."""
        return (1.0 / lmbda * (f0t_calc(t + dt) - f0t_calc(t - dt)) / (2.0 * dt) +
                f0t_calc(t) + eta * eta / (2.0 * lmbda * lmbda) *
                (1.0 - np.exp(-2.0 * lmbda * t)))

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = T / float(num_steps)
    for i in range(0, num_steps):
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = (r[:, i] + lmbda * (theta(time[i]) - r[:, i]) * dt +
                       eta * (w[:, i + 1] - w[:, i]))
        time[i + 1] = time[i] + dt

    paths = {"time": time, "R": r}
    return paths


def hw_theta(lmbda, eta, p0t):
    """
    Compute theta function for Hull-White model.

    Parameters
    ----------
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility
    p0t : callable
        Zero-coupon bond pricing function

    Returns
    -------
    callable
        Theta function
    """
    dt = 0.0001
    def f0t_calc(t):
        return -(np.log(p0t(t + dt)) - np.log(p0t(t - dt))) / (2 * dt)

    def theta_func(t):
        return (1.0 / lmbda * (f0t_calc(t + dt) - f0t_calc(t - dt)) / (2.0 * dt) +
                f0t_calc(t) + eta * eta / (2.0 * lmbda * lmbda) *
                (1.0 - np.exp(-2.0 * lmbda * t)))
    return theta_func


def hw_a(lmbda, eta, p0t, t1, t2):
    """
    Compute A parameter for HW ZCB pricing.

    Parameters
    ----------
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility
    p0t : callable
        Zero-coupon bond pricing function
    t1 : float
        Start time
    t2 : float
        End time

    Returns
    -------
    float
        A parameter value
    """
    tau = t2 - t1
    z_grid = np.linspace(0.0, tau, 250)
    def b_r(tau_val):
        return 1.0 / lmbda * (np.exp(-lmbda * tau_val) - 1.0)

    theta = hw_theta(lmbda, eta, p0t)
    temp1 = lmbda * integrate.trapz(theta(t2 - z_grid) * b_r(z_grid), z_grid)
    temp2 = (eta * eta / (4.0 * np.power(lmbda, 3.0)) *
             (np.exp(-2.0 * lmbda * tau) * (4 * np.exp(lmbda * tau) - 1.0) - 3.0) +
             eta * eta * tau / (2.0 * lmbda * lmbda))

    return temp1 + temp2


def hw_b(lmbda, eta, t1, t2):
    """
    Compute B parameter for HW ZCB pricing.

    Parameters
    ----------
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility (unused)
    t1 : float
        Start time
    t2 : float
        End time

    Returns
    -------
    float
        B parameter value
    """
    return 1.0 / lmbda * (np.exp(-lmbda * (t2 - t1)) - 1.0)


def hw_zcb(lmbda, eta, p0t, t1, t2, r_t1):
    """
    Compute HW zero-coupon bond price.

    Parameters
    ----------
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility
    p0t : callable
        Zero-coupon bond pricing function
    t1 : float
        Current time
    t2 : float
        Maturity time
    r_t1 : array or float
        Interest rate at time t1

    Returns
    -------
    array or float
        ZCB price P(t1, t2)
    """
    n = np.size(r_t1)

    if t1 < t2:
        b_r = hw_b(lmbda, eta, t1, t2)
        a_r = hw_a(lmbda, eta, p0t, t1, t2)
        return np.exp(a_r + b_r * r_t1)
    else:
        return np.ones(n)


def swap_rate_hw(t, t_i, t_m, n, r_t, p0t, lmbda, eta):
    """
    Compute swap rate under Hull-White model.

    Parameters
    ----------
    t : float
        Current time
    t_i : float
        Swap start time
    t_m : float
        Swap end time
    n : int
        Number of payment dates
    r_t : array
        Interest rate paths at time t
    p0t : callable
        Zero-coupon bond pricing function
    lmbda : float
        Mean reversion speed
    eta : float
        Volatility

    Returns
    -------
    array
        Swap rates
    """
    if n == 1:
        ti_grid = np.array([t_i, t_m])
    else:
        ti_grid = np.linspace(t_i, t_m, n)
    tau = ti_grid[1] - ti_grid[0]

    # Overwrite t_i if t > t_i
    prev_ti = ti_grid[np.where(ti_grid < t)]
    if np.size(prev_ti) > 0:
        t_i = prev_ti[-1]

    # Handle case when some payments are already done
    ti_grid = ti_grid[np.where(ti_grid > t)]

    temp = np.zeros(np.size(r_t))

    def p_t_ti_lambda(ti):
        return hw_zcb(lmbda, eta, p0t, t, ti, r_t)

    for idx, ti in enumerate(ti_grid):
        if ti > t_i:
            temp = temp + tau * p_t_ti_lambda(ti)

    p_t_ti = p_t_ti_lambda(t_i)
    p_t_tm = p_t_ti_lambda(t_m)

    swap_rate = (p_t_ti - p_t_tm) / temp

    return swap_rate


def bullet(rate, notional, periods, cpr):
    """
    Compute bullet mortgage payment profile with variable prepayment.

    Parameters
    ----------
    rate : float
        Periodic interest rate
    notional : float
        Initial loan amount
    periods : int
        Number of periods
    cpr : array
        Time-varying conditional prepayment rate

    Returns
    -------
    ndarray
        Shape (periods+1, 6) payment profile
    """
    m = np.zeros((periods + 1, 6))
    m[:, 0] = np.arange(periods + 1)
    m[0, 1] = notional

    for t in range(1, periods):
        m[t, 4] = rate * m[t - 1, 1]      # Interest quote
        m[t, 3] = 0                       # Notional quote (zero for bullet)
        scheduled_outstanding = m[t - 1, 1] - m[t, 3]
        m[t, 2] = scheduled_outstanding * cpr[t]    # Prepayment
        m[t, 1] = scheduled_outstanding - m[t, 2]   # Notional at next time
        m[t, 5] = m[t, 4] + m[t, 2] + m[t, 3]

    # Final period
    m[periods, 4] = rate * m[periods - 1, 1]
    m[periods, 3] = m[periods - 1, 1]
    m[periods, 5] = m[periods, 4] + m[periods, 2] + m[periods, 3]
    return m


def annuity(rate, notional, periods, cpr):
    """
    Compute annuity mortgage payment profile with variable prepayment.

    Parameters
    ----------
    rate : float
        Periodic interest rate
    notional : float
        Initial loan amount
    periods : int
        Number of periods
    cpr : array
        Time-varying conditional prepayment rate

    Returns
    -------
    ndarray
        Shape (periods+1, 6) payment profile
    """
    m = np.zeros((periods + 1, 6))
    m[:, 0] = np.arange(periods + 1)
    m[0, 1] = notional

    for t in range(1, periods + 1):
        remaining_periods = periods - (t - 1)

        # Installment, C(t_i)
        m[t, 5] = rate * m[t - 1, 1] / (1 - 1 / (1 + rate) ** remaining_periods)

        # Interest payment, I(t_i) = rate * N(t_i)
        m[t, 4] = rate * m[t - 1, 1]

        # Notional payment, Q(t_i) = C(t_i) - I(t_i)
        m[t, 3] = m[t, 5] - m[t, 4]

        # Prepayment, P(t_i) = CPR[t] * (N(t_i) - Q(t_i))
        m[t, 2] = cpr[t] * (m[t - 1, 1] - m[t, 3])

        # Notional, N(t_{i+1}) = N(t_i) - Q(t_i) - P(t_i)
        m[t, 1] = m[t - 1, 1] - m[t, 3] - m[t, 2]

    return m


def plot_incentive_vs_rate(new_rate, incentive, label):
    """Plot incentive function vs swap rate."""
    plt.figure(1)
    plt.plot(new_rate, incentive)
    plt.xlabel('S(t)')
    plt.ylabel('Incentive')
    plt.grid()


def plot_incentive_vs_epsilon(epsilon, incentive):
    """Plot incentive function vs epsilon."""
    plt.figure(2)
    plt.plot(epsilon, incentive)
    plt.xlabel('epsilon= K - S(t)')
    plt.ylabel('Incentive')
    plt.grid()


def plot_stochastic_incentive(epsilon, incentive):
    """Plot stochastic incentive scatter."""
    plt.figure(3)
    plt.plot(epsilon, incentive, '.r')
    plt.xlabel('epsilon= K - S(t)')
    plt.ylabel('Incentive')
    plt.grid()
    plt.title('Incentive for prepayment given stochastic S(t)')


def plot_swap_distribution(s_values):
    """Plot histogram of swap rates."""
    plt.figure(4)
    plt.hist(s_values, bins=50)
    plt.grid()
    plt.title('Swap distribution at Tend')


def plot_notional_profiles(ti_grid, n_paths):
    """
    Plot notional profiles for sample paths.

    Parameters
    ----------
    ti_grid : array
        Time grid
    n_paths : array
        Notional paths (num_paths, num_steps+1)
    """
    plt.figure(6)
    plt.grid()
    plt.xlabel('time')
    plt.ylabel('notional')

    n = 100
    for k in range(0, n):
        plt.plot(ti_grid, n_paths[k, :], '-b')


def main():
    """Run stochastic amortization analysis."""
    # ============= Define Incentive Functions =============
    irrational = lambda x: 0.04 + 0.1 / (1 + np.exp(200 * (-x)))
    rational = lambda x: 0.04 * (x > 0.0)

    incentive_function = irrational

    # ============= Parameters =============
    k = 0.05
    new_rate = np.linspace(-0.1, 0.1, 150)
    epsilon = k - new_rate
    incentive = incentive_function(epsilon)

    plot_incentive_vs_rate(new_rate, incentive, '')
    plot_incentive_vs_epsilon(epsilon, incentive)

    # ============= Stochastic Interest Rates =============
    num_paths = 2000
    num_steps = 30
    lmbda = 0.05
    eta = 0.01
    t_end = 30

    # Market ZCB
    p0t = lambda T: np.exp(-0.05 * T)
    paths = generate_paths_hw_euler(num_paths, num_steps, t_end, p0t,
                                     lmbda, eta)
    r = paths["R"]
    ti_grid = paths["time"]

    # Compute swap rates
    s = np.zeros((num_paths, num_steps + 1))
    for i, ti in enumerate(ti_grid):
        s[:, i] = swap_rate_hw(ti, ti, t_end + ti, 30, r[:, i], p0t,
                               lmbda, eta)

    # Incentive for new swap rate
    epsilon = k - s[:, -1]
    incentive = incentive_function(epsilon)
    plot_stochastic_incentive(epsilon, incentive)
    plot_swap_distribution(s[:, -1])

    # ============= Stochastic Notional Profile =============
    mortgage_profile = annuity
    notional = 1000000
    n = np.zeros((num_paths, num_steps + 1))

    for i in range(0, num_paths):
        epsilon = k - s[i, :]
        lambda_cpr = incentive_function(epsilon)
        notional_profile = mortgage_profile(k, notional, num_steps,
                                            lambda_cpr)
        n[i, :] = notional_profile[:, 1]

    plot_notional_profiles(ti_grid, n)

    annuity_profile_no_prepay = mortgage_profile(
        k, notional, num_steps, np.zeros(num_steps + 1))
    plt.plot(ti_grid, annuity_profile_no_prepay[:, 1], '--r')
    plt.title('Notional profile')


# ======================================================================
# Main
# ======================================================================

if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
In the stochastic amortizing swap, the prepayment rate depends on the stochastic swap rate $S(t)$. Explain why the notional profile becomes path-dependent and what this implies for pricing.

??? success "Solution to Exercise 1"
    The CPR at time $t$ is $\Lambda(\varepsilon_t)$ where $\varepsilon_t = K - S(t)$ and $S(t)$ is a stochastic process. Since $S(t)$ follows different paths in each Monte Carlo scenario, the CPR varies across paths. The outstanding notional at time $t$ depends on all previous CPR values (and hence all previous swap rates), making it path-dependent:

    $$
    N(t) = N(t-1) - Q(t) - \Lambda(\varepsilon_t)(N(t-1) - Q(t)).
    $$

    This path-dependency means the product cannot be priced by a simple closed-form formula; Monte Carlo simulation across many interest rate scenarios is required.

---

**Exercise 2.**
The Hull-White model is used to generate stochastic interest rate paths. Write the SDE and explain how the $\theta(t)$ function ensures calibration to the initial yield curve.

??? success "Solution to Exercise 2"
    The Hull-White SDE is

    $$
    dr(t) = \lambda[\theta(t) - r(t)]\,dt + \eta\,dW(t),
    $$

    where $\theta(t)$ is chosen so that the model reproduces the observed term structure:

    $$
    \theta(t) = \frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t} + f(0,t) + \frac{\eta^2}{2\lambda^2}(1 - e^{-2\lambda t}).
    $$

    Here $f(0,t)$ is the market instantaneous forward rate. This choice ensures $P_{\text{model}}(0,T) = P_{\text{market}}(0,T)$ for all $T$, so the model is automatically calibrated to the initial yield curve.

---

**Exercise 3.**
Compare the "rational" and "irrational" incentive functions used in the code. What is the CPR when $\varepsilon = 0$ for each?

??? success "Solution to Exercise 3"

    - **Irrational**: $\Lambda(\varepsilon) = 0.04 + 0.1/(1 + e^{200(-\varepsilon)})$. At $\varepsilon = 0$: $\Lambda(0) = 0.04 + 0.1/(1 + 1) = 0.04 + 0.05 = 0.09$ ($9\%$ CPR). Even when there is no rate advantage, some borrowers still prepay (due to moving, divorce, etc.).
    - **Rational**: $\Lambda(\varepsilon) = 0.04 \cdot \mathbf{1}_{\varepsilon > 0}$. At $\varepsilon = 0$: $\Lambda(0) = 0$ ($0\%$ CPR). The step function assumes borrowers only prepay when there is a strictly positive benefit.

    The irrational model is more realistic because it includes a baseline prepayment rate for non-financial reasons.

---

**Exercise 4.**
If the mortgage rate is $K = 5\%$ and the Hull-White model generates 2000 swap rate paths at maturity, how would you estimate the expected notional profile and its confidence bands?

??? success "Solution to Exercise 4"
    For each of the 2000 paths, compute the notional schedule $N_i(t)$ for $i = 1, \ldots, 2000$ by applying the incentive function to the path-specific swap rates. The expected notional profile is

    $$
    \hat{N}(t) = \frac{1}{2000}\sum_{i=1}^{2000} N_i(t).
    $$

    The 95% confidence bands at each time point are the $2.5$th and $97.5$th percentiles of $\{N_i(t)\}_{i=1}^{2000}$. This shows the range of outcomes: in low-rate scenarios, heavy prepayment shrinks the notional quickly; in high-rate scenarios, minimal prepayment keeps the notional near its scheduled path.
