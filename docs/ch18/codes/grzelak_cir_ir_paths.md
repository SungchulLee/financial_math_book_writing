# Cox-Ingersoll-Ross Interest Rate Paths (Grzelak)

## Background

Monte Carlo paths for the CIR interest rate process.

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak

---

## Code

```python
"""
Monte Carlo paths for the CIR interest rate process.

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


def generate_paths_cir_euler(num_paths, num_steps, T, lmbda, r0, theta, gamma):
    """
    Generate CIR process paths using Euler scheme.

    Parameters
    ----------
    num_paths : int
        Number of simulation paths
    num_steps : int
        Number of time steps
    T : float
        Time to maturity
    lmbda : float
        Mean reversion speed
    r0 : float
        Initial interest rate
    theta : float
        Long-term mean
    gamma : float
        Volatility parameter

    Returns
    -------
    dict
        Dictionary with keys 'time' and 'R' containing time grid and rate paths
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))
    r = np.zeros((num_paths, num_steps + 1))
    r[:, 0] = r0
    time = np.zeros(num_steps + 1)

    dt = T / float(num_steps)
    for i in range(0, num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        r[:, i + 1] = (r[:, i] + lmbda * (theta - r[:, i]) * dt +
                       gamma * np.sqrt(r[:, i]) * (w[:, i + 1] - w[:, i]))

        # Truncated boundary condition
        r[:, i + 1] = np.maximum(r[:, i + 1], 0.0)
        time[i + 1] = time[i] + dt

    paths = {"time": time, "R": r}
    return paths


def plot_lambda_effect(lmbda_vec, num_paths, num_steps, T, r0, theta, gamma):
    """
    Plot effect of mean reversion speed on CIR paths.

    Parameters
    ----------
    lmbda_vec : list
        List of lambda values to test
    num_paths : int
        Number of paths per lambda
    num_steps : int
        Number of time steps
    T : float
        Time to maturity
    r0 : float
        Initial rate
    theta : float
        Long-term mean
    gamma : float
        Volatility
    """
    plt.figure(1)
    legend = []
    for lmbda_temp in lmbda_vec:
        np.random.seed(2)
        paths = generate_paths_cir_euler(num_paths, num_steps, T, lmbda_temp,
                                         r0, theta, gamma)
        legend.append('lambda={0}'.format(lmbda_temp))
        time_grid = paths["time"]
        r = paths["R"]
        plt.plot(time_grid, np.transpose(r))
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("R(t)")
    plt.legend(legend)


def plot_gamma_effect(gamma_vec, num_paths, num_steps, T, lmbda, r0, theta):
    """
    Plot effect of volatility on CIR paths.

    Parameters
    ----------
    gamma_vec : list
        List of gamma values to test
    num_paths : int
        Number of paths per gamma
    num_steps : int
        Number of time steps
    T : float
        Time to maturity
    lmbda : float
        Mean reversion speed
    r0 : float
        Initial rate
    theta : float
        Long-term mean
    """
    plt.figure(2)
    legend = []
    for gamma_temp in gamma_vec:
        np.random.seed(2)
        paths = generate_paths_cir_euler(num_paths, num_steps, T, lmbda, r0,
                                         theta, gamma_temp)
        legend.append('gamma={0}'.format(gamma_temp))
        time_grid = paths["time"]
        r = paths["R"]
        plt.plot(time_grid, np.transpose(r))
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("R(t)")
    plt.legend(legend)


def main():
    """Run CIR path generation and visualization."""
    # ============= Parameters =============
    num_paths = 1
    num_steps = 500
    T = 50.0
    lmbda = 0.1
    gamma = 0.05
    r0 = 0.05
    theta = 0.05

    # Effect of mean reversion lambda
    lmbda_vec = [0.01, 0.2, 5.0]
    plot_lambda_effect(lmbda_vec, num_paths, num_steps, T, r0, theta, gamma)

    # Effect of the volatility
    gamma_vec = [0.1, 0.2, 0.3]
    plot_gamma_effect(gamma_vec, num_paths, num_steps, T, lmbda, r0, theta)


# ======================================================================
# Main
# ======================================================================

if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The CIR SDE is $dr = \lambda(\theta - r)\,dt + \gamma\sqrt{r}\,dW$. For the default parameters $\lambda = 0.1$, $\theta = 0.05$, $\gamma = 0.05$, and $r_0 = 0.05$, compute the Feller parameter and the expected rate at $T = 50$.

??? success "Solution to Exercise 1"
    The Feller parameter is

    $$
    \frac{2\lambda\theta}{\gamma^2} = \frac{2 \times 0.1 \times 0.05}{0.05^2} = \frac{0.01}{0.0025} = 4.0.
    $$

    Since $4.0 \geq 1$, the Feller condition is satisfied. The expected rate at $T = 50$ is

    $$
    \mathbb{E}[r(50)] = \theta + (r_0 - \theta)e^{-\lambda T} = 0.05 + 0 \cdot e^{-5} = 0.05.
    $$

    Since $r_0 = \theta$, the expected rate equals $\theta$ for all $t$.

---

**Exercise 2.**
The code normalizes Brownian increments so they have mean zero and variance one. Explain why this is done and what effect it has on the simulation quality.

??? success "Solution to Exercise 2"
    The normalization step adjusts each column of random samples $z_i$ by subtracting the sample mean and dividing by the sample standard deviation:

    $$
    z_i^{\text{norm}} = \frac{z_i - \bar{z}_i}{s_i}.
    $$

    This ensures that the empirical first two moments of the increments exactly match the theoretical values ($\mu = 0$, $\sigma = 1$), removing sampling noise in these moments. This variance reduction technique improves convergence of Monte Carlo estimates, particularly for a moderate number of paths, because the Brownian increments used by all paths are exactly centered and properly scaled.

---

**Exercise 3.**
The `plot_lambda_effect` function tests $\lambda \in \{0.01, 0.2, 5.0\}$. Describe qualitatively how each value affects the CIR paths over a 50-year horizon.

??? success "Solution to Exercise 3"

    - $\lambda = 0.01$: Very slow mean reversion. Paths wander freely and may deviate far from $\theta = 0.05$ for extended periods. The process behaves almost like a random walk with a tiny drift.
    - $\lambda = 0.2$: Moderate mean reversion. Paths exhibit visible attraction toward $\theta$, returning within a few years after deviations. The variance is moderate.
    - $\lambda = 5.0$: Very strong mean reversion. Paths are tightly clustered around $\theta$ with small fluctuations. The process rapidly corrects any deviation, and the half-life of a shock is $\ln(2)/5 \approx 0.14$ years (about 7 weeks).

---

**Exercise 4.**
If the volatility parameter is changed to $\gamma = 0.3$ while keeping $\lambda = 0.1$ and $\theta = 0.05$, does the Feller condition still hold? What practical consequence does this have for the Euler simulation with the truncation boundary $r = \max(r, 0)$?

??? success "Solution to Exercise 4"
    The Feller parameter becomes

    $$
    \frac{2 \times 0.1 \times 0.05}{0.3^2} = \frac{0.01}{0.09} \approx 0.111.
    $$

    Since $0.111 < 1$, the Feller condition is strongly violated. The continuous CIR process can reach zero with positive probability, and the Euler discretization will frequently produce negative rates. The truncation $r = \max(r, 0)$ acts as an absorbing boundary at zero, introducing upward bias in the simulated rate distribution. Many paths will hit zero and be reflected, leading to an accumulation of paths near zero that does not match the theoretical transition density.
