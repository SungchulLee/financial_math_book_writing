# Introduction and Overview

Analytical (closed-form) solutions of the Black-Scholes PDE exist only under idealized assumptions. For American options, exotic derivatives, or complex payoffs, we must turn to **numerical methods**. The **Finite Difference Method (FDM)** is one of the most widely used numerical methods for solving PDEs in finance.

---

## Why Finite Difference Methods?

Finite difference methods approximate derivatives in the Black-Scholes PDE using finite changes in function values at discrete points. Instead of solving the PDE continuously, we **discretize the domain** and solve a system of algebraic equations over a grid.

This approach is well-suited to:

- European and American options
- Barrier and other exotic options
- Time- or price-dependent coefficients (e.g., stochastic volatility)

---

## Visualizing the Finite Difference Grid

To understand how FDM works, visualize the $(S, t)$ domain as a grid.

**`visualize_finite_difference_grid.py`**

```python
from black_scholes import draw_finite_difference_grid

draw_finite_difference_grid()
```

In this grid:

- The **horizontal axis** represents the stock price $S$, discretized into $M$ steps of size $\Delta S$.
- The **vertical axis** represents time $t$, going **backward from $T$ to 0**, discretized into $N$ steps of size $\Delta t$.
- Each node represents a point $(S_i, t_n)$ where the option value $V(S_i, t_n)$ will be computed.

The goal is to start from the **terminal condition** at maturity (top row), and use one of the finite difference schemes (explicit, implicit, or Crank-Nicolson) to compute the values row-by-row **backward in time** down to $t=0$.

---

## Key Idea

By replacing derivatives in the Black-Scholes PDE with difference approximations:

- First derivatives (e.g., $\partial V/\partial S$) are approximated by differences between neighboring nodes.
- Second derivatives (e.g., $\partial^2 V/\partial S^2$) are approximated by combining nearby nodes symmetrically.
- The PDE becomes a **system of equations** that can be iteratively solved on the grid.

---

## Black-Scholes Equation Recap

The Black-Scholes PDE for the value $V(S,t)$ of a European option is:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0
$$

where $V(S,t)$ is the option price, $\sigma$ is volatility, $r$ is the risk-free rate, and $t \in [0, T]$.

### Terminal Condition (at maturity $t = T$)

$$
V(S, T) = \max(S - K, 0)
$$

This serves as the **initial condition** for backward time-stepping.

### Boundary Conditions

**As $S \to 0$:** The call becomes worthless: $V(0, t) = 0$.

**As $S \to \infty$:** The call behaves like the underlying minus discounted strike:

$$
V(S, t) \approx S - K e^{-r(T - t)}
$$

### Nature of the PDE

The Black-Scholes PDE is **parabolic** (similar to the heat equation), **backward in time**, and **second-order in space**. This structure is well-suited to finite difference techniques.

---

## Grid Discretization

We consider a rectangular computational domain $S \in [0, S_{\max}]$, $t \in [0, T]$, discretized into $M$ intervals in stock price and $N$ intervals in time.

$$
\Delta S = \frac{S_{\max}}{M}, \quad \Delta t = \frac{T}{N}
$$

Grid points: $S_i = i \Delta S$ for $i = 0, 1, \ldots, M$ and $t_n = n \Delta t$ for $n = 0, 1, \ldots, N$.

Let $V_i^n$ denote the numerical approximation to $V(S_i, t_n)$.

---

## Finite Difference Approximations

### Time Derivative (backward difference)

$$
\frac{\partial V}{\partial t} \approx \frac{V_i^{n+1} - V_i^n}{\Delta t}
$$

### First Spatial Derivative (central difference)

$$
\frac{\partial V}{\partial S} \approx \frac{V_{i+1}^n - V_{i-1}^n}{2 \Delta S}
$$

### Second Spatial Derivative (central difference)

$$
\frac{\partial^2 V}{\partial S^2} \approx \frac{V_{i+1}^n - 2V_i^n + V_{i-1}^n}{(\Delta S)^2}
$$

### Discrete Grid Notation Summary

| Quantity                | Continuous Form               | Discrete Approximation               |
|-------------------------|-------------------------------|--------------------------------------|
| Stock price             | $S \in [0, S_{\max}]$         | $S_i = i \Delta S$, $i = 0,\dots,M$  |
| Time                    | $t \in [0, T]$                | $t_n = n \Delta t$, $n = 0,\dots,N$  |
| Time derivative         | $\frac{\partial V}{\partial t}$ | $\frac{V_i^{n+1} - V_i^n}{\Delta t}$ |
| First derivative in $S$ | $\frac{\partial V}{\partial S}$ | $\frac{V_{i+1}^n - V_{i-1}^n}{2\Delta S}$ |
| Second derivative in $S$| $\frac{\partial^2 V}{\partial S^2}$ | $\frac{V_{i+1}^n - 2V_i^n + V_{i-1}^n}{(\Delta S)^2}$ |

---

## Section Objectives

In this section, we will:

- Understand the mathematical foundation of finite difference schemes.
- Implement three key methods: **explicit**, **implicit**, and **Crank-Nicolson**.
- Learn how to set up boundary and initial conditions relevant for option pricing.
- Explore the numerical stability and accuracy of each scheme.
- Implement a working Python program to compute option prices using FDM.
