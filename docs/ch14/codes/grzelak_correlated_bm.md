# Correlated Brownian Motion (Grzelak)

## Background

Correlated Brownian motions with various correlation parameters.

Demonstrates the generation of two correlated Brownian motions using
standardized normal increments. Illustrates how correlation affects the
joint behavior of stochastic processes.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.

---

## Code

```python
# -*- coding: utf-8 -*-
"""
Correlated Brownian motions with various correlation parameters.

Demonstrates the generation of two correlated Brownian motions using
standardized normal increments. Illustrates how correlation affects the
joint behavior of stochastic processes.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Core Computation
# =============================================================================

def generate_paths_correlated_bm(num_paths, num_steps, t, rho):
    """
    Generate correlated Brownian motion paths.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths.
    num_steps : int
        Number of time steps.
    t : float
        Terminal time.
    rho : float
        Correlation coefficient between W1 and W2.

    Returns
    -------
    paths : dict
        Dictionary containing:
        - 'time': time grid of shape (num_steps+1,)
        - 'W1': W1 paths of shape (num_paths, num_steps+1)
        - 'W2': W2 paths of shape (num_paths, num_steps+1)
    """
    z1 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    z2 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w1 = np.zeros((num_paths, num_steps + 1))
    w2 = np.zeros((num_paths, num_steps + 1))

    dt = t / float(num_steps)
    time = np.zeros(num_steps + 1)

    for i in range(0, num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z1[:, i] = (z1[:, i] - np.mean(z1[:, i])) / np.std(z1[:, i])
            z2[:, i] = (z2[:, i] - np.mean(z2[:, i])) / np.std(z2[:, i])

        # Correlate noises
        z2[:, i] = rho * z1[:, i] + np.sqrt(1.0 - rho**2) * z2[:, i]

        w1[:, i + 1] = w1[:, i] + np.sqrt(dt) * z1[:, i]
        w2[:, i + 1] = w2[:, i] + np.sqrt(dt) * z2[:, i]

        time[i + 1] = time[i] + dt

    # Store the results
    paths = {"time": time, "W1": w1, "W2": w2}
    return paths


# =============================================================================
# 2. Plotting Functions
# =============================================================================

def plot_paths(time_grid, w1, w2, title):
    """
    Plot Brownian motion paths.

    Parameters
    ----------
    time_grid : ndarray
        Time grid of shape (num_steps+1,).
    w1 : ndarray
        W1 paths of shape (num_paths, num_steps+1).
    w2 : ndarray
        W2 paths of shape (num_paths, num_steps+1).
    title : str
        Title for the figure.

    Returns
    -------
    None
    """
    plt.figure()
    plt.plot(time_grid, np.transpose(w1))
    plt.plot(time_grid, np.transpose(w2))
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("W(t)")
    plt.title(title)


# =============================================================================
# 3. Main Computation
# =============================================================================

def main():
    """Run demonstration of correlated Brownian motions."""
    # Parameters
    num_paths = 1
    num_steps = 500
    t = 1.0

    # ===== Negative correlation =====
    rho = -0.9
    paths = generate_paths_correlated_bm(num_paths, num_steps, t, rho)
    time_grid = paths["time"]
    w1 = paths["W1"]
    w2 = paths["W2"]
    plot_paths(time_grid, w1, w2, "Correlated BM (rho = -0.9)")

    # ===== Positive correlation =====
    rho = 0.9
    paths = generate_paths_correlated_bm(num_paths, num_steps, t, rho)
    time_grid = paths["time"]
    w1 = paths["W1"]
    w2 = paths["W2"]
    plot_paths(time_grid, w1, w2, "Correlated BM (rho = 0.9)")

    # ===== Zero correlation =====
    rho = 0.0
    paths = generate_paths_correlated_bm(num_paths, num_steps, t, rho)
    time_grid = paths["time"]
    w1 = paths["W1"]
    w2 = paths["W2"]
    plot_paths(time_grid, w1, w2, "Correlated BM (rho = 0.0)")


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
To generate two correlated Brownian motions $W_1, W_2$ with $\text{Corr}(W_1, W_2) = \rho$, write the construction using independent normals $Z_1, Z_2$.

??? success "Solution to Exercise 1"
    $W_1 = Z_1$ and $W_2 = \rho Z_1 + \sqrt{1 - \rho^2} Z_2$. Then $\mathbb{E}[W_2] = 0$, $\text{Var}(W_2) = \rho^2 + 1 - \rho^2 = 1$, and $\text{Cov}(W_1, W_2) = \rho$. The increments scale: $\Delta W_1 = \sqrt{\Delta t} Z_1$, $\Delta W_2 = \sqrt{\Delta t}(\rho Z_1 + \sqrt{1-\rho^2}Z_2)$.

---

**Exercise 2.**
For $\rho = -0.9$, describe qualitatively how the two Brownian motion paths relate visually.

??? success "Solution to Exercise 2"
    With $\rho = -0.9$, the paths move in nearly opposite directions: when $W_1$ increases, $W_2$ almost always decreases, and vice versa. The paths appear as "mirror images" with some noise. This models the leverage effect: stock price up ($W_1$ up) correlates with volatility down ($W_2$ down).

---

**Exercise 3.**
Verify that the Cholesky decomposition of $\Sigma = \begin{pmatrix}1 & \rho\\\rho & 1\end{pmatrix}$ gives $L = \begin{pmatrix}1 & 0\\\rho & \sqrt{1-\rho^2}\end{pmatrix}$, and that $LL^T = \Sigma$.

??? success "Solution to Exercise 3"
    $LL^T = \begin{pmatrix}1 & 0\\\rho & \sqrt{1-\rho^2}\end{pmatrix}\begin{pmatrix}1 & \rho\\0 & \sqrt{1-\rho^2}\end{pmatrix} = \begin{pmatrix}1 & \rho\\\rho & \rho^2 + 1 - \rho^2\end{pmatrix} = \begin{pmatrix}1 & \rho\\\rho & 1\end{pmatrix} = \Sigma$. This confirms $L$ is the lower-triangular Cholesky factor, and $Y = LZ$ produces correlated normals from independent $Z$.

---

**Exercise 4.**
For a 3-factor model with correlation matrix $\Sigma_{3\times3}$, explain how the Cholesky decomposition generalizes.

??? success "Solution to Exercise 4"
    For $\Sigma \in \mathbb{R}^{3\times3}$ (symmetric positive definite), the Cholesky factorization gives $\Sigma = LL^T$ where $L$ is lower triangular. Given independent $Z = (Z_1, Z_2, Z_3)^T$, the correlated vector is $Y = LZ$. The algorithm computes $L_{ij} = (\Sigma_{ij} - \sum_{k=1}^{j-1}L_{ik}L_{jk})/L_{jj}$ with $L_{jj} = \sqrt{\Sigma_{jj} - \sum_{k=1}^{j-1}L_{jk}^2}$. This generalizes to any dimension and is the standard method for generating correlated multi-factor models.