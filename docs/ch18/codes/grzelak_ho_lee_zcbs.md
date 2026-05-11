# Ho-Lee Zero-Coupon Bonds (Grzelak)

## Background

Ho-Lee model simulation and zero-coupon bond pricing.

Simulates the Ho-Lee model and computes zero-coupon bond prices P(0,t).

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak

---

## Code

```python
"""
Ho-Lee model simulation and zero-coupon bond pricing.

Simulates the Ho-Lee model and computes zero-coupon bond prices P(0,t).

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak
"""
import numpy as np
import matplotlib.pyplot as plt


# ======================================================================
# Functions / Classes
# ======================================================================


def f0t(t, p0t):
    """
    Calculate forward rate at time t.

    Parameters
    ----------
    t : float
        Time point
    p0t : callable
        Zero-coupon bond pricing function P(0,T)

    Returns
    -------
    float
        Forward rate f(0,t)
    """
    dt = 0.01
    expr = -(np.log(p0t(t + dt)) - np.log(p0t(t - dt))) / (2 * dt)
    return expr


def generate_paths_ho_lee_euler(num_paths, num_steps, T, p0t, sigma):
    """
    Generate Ho-Lee model paths using Euler scheme.

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
    sigma : float
        Volatility parameter

    Returns
    -------
    dict
        Dictionary with keys 'time', 'R', 'M' containing time grid, rates, and bank account
    """
    dt = T / float(num_steps)

    # Initial interest rate is forward rate at time t->0
    r0 = f0t(0.01, p0t)

    def theta(t):
        """Theta function for Ho-Lee model."""
        return ((f0t(t + dt, p0t) - f0t(t - dt, p0t)) / (2.0 * dt) +
                sigma ** 2.0 * t)

    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    m = np.zeros((num_paths, num_steps + 1))
    m[:, 0] = 1.0
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    for i in range(0, num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = r[:, i] + theta(time[i]) * dt + sigma * (w[:, i + 1] -
                                                                 w[:, i])
        m[:, i + 1] = m[:, i] * np.exp((r[:, i + 1] + r[:, i]) * 0.5 * dt)
        time[i + 1] = time[i] + dt

    paths = {"time": time, "R": r, "M": m}
    return paths


def plot_zcb_comparison(time_grid, p0t_market, p0t_mc):
    """
    Plot comparison of market and Monte Carlo zero-coupon bond prices.

    Parameters
    ----------
    time_grid : array
        Time points
    p0t_market : array
        Market ZCB prices
    p0t_mc : array
        Monte Carlo ZCB prices
    """
    plt.figure(1)
    plt.grid()
    plt.xlabel('T')
    plt.ylabel('P(0,T)')
    plt.plot(time_grid, p0t_market)
    plt.plot(time_grid, p0t_mc, '--r')
    plt.legend(['P(0,t) market', 'P(0,t) Monte Carlo'])
    plt.title('ZCBs from Ho-Lee Model')


def main():
    """Run Ho-Lee model simulation and ZCB pricing."""
    # ============= Parameters =============
    num_paths = 25000
    num_steps = 500
    sigma = 0.007
    T = 40

    # Define a ZCB curve (obtained from market)
    p0t = lambda T: np.exp(-0.1 * T)

    # ============= Monte Carlo Simulation =============
    paths = generate_paths_ho_lee_euler(num_paths, num_steps, T, p0t, sigma)
    m = paths["M"]
    ti = paths["time"]

    # Compare price of ZCB from Monte Carlo and analytical expression
    p_t = np.zeros(num_steps + 1)
    for i in range(0, num_steps + 1):
        p_t[i] = np.mean(1.0 / m[:, i])

    # ============= Plotting =============
    plot_zcb_comparison(ti, p0t(ti), p_t)


# ======================================================================
# Main
# ======================================================================

if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The Ho-Lee model SDE is $dr(t) = \theta(t)\,dt + \sigma\,dW(t)$. If the market zero-coupon bond curve is $P(0,T) = e^{-0.1T}$, compute the forward rate $f(0,T)$ and the drift function $\theta(t)$ for $\sigma = 0.007$.

??? success "Solution to Exercise 1"
    The instantaneous forward rate is

    $$
    f(0,T) = -\frac{\partial}{\partial T}\ln P(0,T) = -\frac{\partial}{\partial T}(-0.1T) = 0.1.
    $$

    The forward rate is constant at $10\%$ for this flat curve. The Ho-Lee drift is

    $$
    \theta(t) = \frac{\partial f}{\partial T}(0,t) + \sigma^2 t = 0 + 0.007^2 \times t = 4.9 \times 10^{-5}\,t.
    $$

    The drift grows linearly with time, capturing the volatility-induced upward adjustment needed to maintain consistency with the market curve.

---

**Exercise 2.**
Explain how the money market account $M(t)$ is computed in the code and why the ZCB price is estimated as $P(0,t) \approx \mathbb{E}[1/M(t)]$.

??? success "Solution to Exercise 2"
    The money market account satisfies $dM = r(t)\,M\,dt$, which is discretized as

    $$
    M(t_{i+1}) = M(t_i)\,\exp\!\left(\frac{r(t_{i+1}) + r(t_i)}{2}\,\Delta t\right),
    $$

    using the trapezoidal rule for numerical integration of $\int_0^t r(s)\,ds$. The risk-neutral pricing formula for a zero-coupon bond is

    $$
    P(0,t) = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{1}{M(t)}\right].
    $$

    This is estimated by averaging $1/M(t)$ across all Monte Carlo paths. The closer this estimate is to the market curve $P(0,t) = e^{-0.1t}$, the better the model calibration.

---

**Exercise 3.**
For $\sigma = 0.007$, $T = 40$, and $N = 25{,}000$ paths, the code compares analytical and Monte Carlo ZCB prices. Estimate the standard error of the Monte Carlo estimate for $P(0,20)$ if the variance of $1/M(20)$ is approximately $0.01$.

??? success "Solution to Exercise 3"
    The standard error of the Monte Carlo estimator is

    $$
    \text{SE} = \frac{\sqrt{\text{Var}(1/M(20))}}{\sqrt{N}} = \frac{\sqrt{0.01}}{\sqrt{25{,}000}} = \frac{0.1}{158.1} \approx 0.000632.
    $$

    The $95\%$ confidence interval for $P(0,20)$ is approximately $\hat{P} \pm 1.96 \times 0.000632 \approx \hat{P} \pm 0.00124$. With the analytical value $P(0,20) = e^{-2} \approx 0.1353$, this represents a relative error of about $0.9\%$.

---

**Exercise 4.**
The Ho-Lee model allows negative interest rates. For $\sigma = 0.007$ and a flat forward curve at $10\%$, estimate the probability that $r(40) < 0$ assuming $r(40)$ is approximately normally distributed.

??? success "Solution to Exercise 4"
    Under the Ho-Lee model with a flat forward curve, $r(t)$ is normally distributed with mean $f(0,t) = 0.1$ and variance $\sigma^2 t = 0.007^2 \times 40 = 0.00196$. The standard deviation is $\sqrt{0.00196} \approx 0.04427$.

    The probability of negative rates is

    $$
    \mathbb{P}(r(40) < 0) = \Phi\!\left(\frac{0 - 0.1}{0.04427}\right) = \Phi(-2.259) \approx 0.012.
    $$

    There is approximately a $1.2\%$ chance of negative rates at year 40. While small, this is non-zero, which is a well-known limitation of Gaussian short-rate models like Ho-Lee.
