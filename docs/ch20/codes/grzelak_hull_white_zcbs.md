# Hull-White Zero-Coupon Bonds

## Background

Hull-White model simulation for Zero-Coupon Bond pricing.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak

---

## What This Code Demonstrates

- Forward Rate and Theta Functions =============
- Path Generation =============
- Plotting =============

---

## Code

```python
"""
Hull-White model simulation for Zero-Coupon Bond pricing.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt


# ============= Forward Rate and Theta Functions =============

def f0t(tau, p0t):
    """
    Compute forward rate at time tau.

    Parameters
    ----------
    tau : float
        Time point
    p0t : callable
        Zero-coupon bond function P(0, T)

    Returns
    -------
    float
        Forward rate f(0, tau)
    """
    dt = 0.01
    return -(np.log(p0t(tau + dt)) - np.log(p0t(tau - dt))) / (2 * dt)


def hw_theta(lambd, eta, p0t):
    """
    Compute Hull-White theta function (mean-reverting level).

    Parameters
    ----------
    lambd : float
        Mean reversion speed
    eta : float
        Volatility
    p0t : callable
        Zero-coupon bond function

    Returns
    -------
    callable
        Theta function
    """
    dt = 0.01

    def theta(tau):
        """Mean-reverting level at time tau."""
        return (1.0 / lambd * (f0t(tau + dt, p0t) - f0t(tau - dt, p0t)) / (2.0 * dt) +
                f0t(tau, p0t) + eta * eta / (2.0 * lambd * lambd) * (1.0 - np.exp(-2.0 * lambd * tau)))

    return theta


# ============= Path Generation =============

def generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta):
    """
    Generate Hull-White interest rate paths with money market account.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths
    num_steps : int
        Number of time steps
    t : float
        Total time horizon
    p0t : callable
        Zero-coupon bond function P(0, T)
    lambd : float
        Mean reversion speed
    eta : float
        Volatility

    Returns
    -------
    dict
        Dictionary with 'time', 'R', and 'M' keys
    """
    dt_diff = 0.01

    def f0t_local(tau):
        """Local forward rate function."""
        return -(np.log(p0t(tau + dt_diff)) - np.log(p0t(tau - dt_diff))) / (2 * dt_diff)

    # Initial interest rate
    r0 = f0t_local(0.01)

    # Get theta function
    theta = hw_theta(lambd, eta, p0t)

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    m = np.zeros((num_paths, num_steps + 1))
    m[:, 0] = 1.0
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = t / float(num_steps)
    for i in range(0, num_steps):
        # Ensure samples have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])

        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = r[:, i] + lambd * (theta(time[i]) - r[:, i]) * dt + eta * (w[:, i + 1] - w[:, i])
        m[:, i + 1] = m[:, i] * np.exp((r[:, i + 1] + r[:, i]) * 0.5 * dt)
        time[i + 1] = time[i] + dt

    return {"time": time, "R": r, "M": m}


# ============= Plotting =============

def main():
    """Main computation for Hull-White ZCB analysis."""
    num_paths = 25000
    num_steps = 25
    lambd = 0.02
    eta = 0.02

    # ZCB curve (from market)
    p0t = lambda t: np.exp(-0.1 * t)

    # Monte Carlo simulation
    t = 40
    paths = generate_paths_hw_euler(num_paths, num_steps, t, p0t, lambd, eta)
    m = paths["M"]
    ti = paths["time"]

    # Compute ZCB prices from simulation
    p_t_mc = np.zeros(num_steps + 1)
    for i in range(0, num_steps + 1):
        p_t_mc[i] = np.mean(1.0 / m[:, i])

    # Compare with market ZCB
    plt.figure(1)
    plt.grid()
    plt.xlabel('T')
    plt.ylabel('P(0,T)')
    plt.plot(ti, p0t(ti))
    plt.plot(ti, p_t_mc, '--r')
    plt.legend(['P(0,t) market', 'P(0,t) Monte Carlo'])
    plt.title('ZCBs from Hull-White Model')


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The Hull-White ZCB price formula is $P(t_1, t_2) = e^{A(t_1,t_2) + B(t_1,t_2)\,r(t_1)}$. Show that $P(0, T) = P_{\text{market}}(0, T)$ when $r(0) = f(0, 0)$.

??? success "Solution to Exercise 1"
    At $t_1 = 0$, the $A$ and $B$ coefficients are calibrated such that $e^{A(0,T) + B(0,T)\,r(0)} = P_{\text{market}}(0,T)$. This is ensured by the choice of $\theta(t)$:

    $$
    \theta(t) = \frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t} + f(0,t) + \frac{\eta^2}{2\lambda^2}(1 - e^{-2\lambda t}).
    $$

    By construction, the model's zero-coupon bond prices at time $0$ match the market exactly. The coefficients $A$ and $B$ are derived from the Ricatti equations of the affine term structure model and incorporate $\theta(t)$ through numerical integration.

---

**Exercise 2.**
The Monte Carlo ZCB price estimate is $\hat{P}(0,T) = \frac{1}{N}\sum_{i=1}^N 1/M_i(T)$ where $M_i(T)$ is the money market account on path $i$. Explain the statistical interpretation and expected accuracy.

??? success "Solution to Exercise 2"
    This estimator follows from the risk-neutral pricing formula $P(0,T) = \mathbb{E}^{\mathbb{Q}}[1/M(T)]$. By the law of large numbers, $\hat{P} \to P(0,T)$ as $N \to \infty$. The standard error is $\text{SE} = \text{std}(1/M(T))/\sqrt{N}$. With $N = 25{,}000$ paths and typical interest rate parameters, the relative error is usually below $0.5\%$, providing a good match to the analytical market curve.

---

**Exercise 3.**
If the Monte Carlo estimate for $P(0, 20)$ is $0.1360$ while the market value is $P(0, 20) = e^{-0.1 \times 20} = 0.1353$, compute the relative error and suggest how to reduce it.

??? success "Solution to Exercise 3"
    The relative error is $(0.1360 - 0.1353)/0.1353 = 0.0052 = 0.52\%$.

    To reduce this error: (1) increase the number of paths (doubling paths halves the standard error); (2) use antithetic variates (simulate both $Z$ and $-Z$ paths); (3) use the analytical ZCB price as a control variate, since its expectation is known exactly; (4) apply moment matching (normalize Brownian increments as the code does).

---

**Exercise 4.**
The coefficient $B(t_1, t_2) = (e^{-\lambda(t_2 - t_1)} - 1)/\lambda$ is always negative. Explain the economic meaning of this sign.

??? success "Solution to Exercise 4"
    Since $B < 0$, the bond price $P = e^{A + Br}$ is a decreasing function of $r$: higher short rates imply lower bond prices. This is the fundamental inverse relationship between rates and bond prices. The magnitude $|B|$ represents the duration-like sensitivity of the bond to the short rate. As $\lambda \to 0$ (no mean reversion), $|B| \to t_2 - t_1$ (full maturity effect). As $\lambda$ increases, $|B|$ decreases because mean reversion limits the impact of current rate changes on long-term rates.
