# Black-Karasinski Python Implementation Guide

This guide describes the design and usage of the Black-Karasinski (BK) trinomial tree implementation in the companion `python_implementation.py` module. The BK model is non-affine and has no closed-form bond or option prices, so a trinomial tree is the standard pricing engine. The code constructs the tree in log-rate space $x = \ln r$, calibrates the time-dependent drift $\theta(t)$ to the market yield curve by forward induction, and prices derivatives by backward induction. Each method is mapped to its mathematical formula from the preceding theory sections.

!!! info "Prerequisites"
    - [Log-Normal Short Rate SDE](log_normal_short_rate_sde.md) (BK dynamics: $d(\ln r) = [\theta(t) - a\ln r]\,dt + \sigma\,dW$)
    - [Trinomial Tree Implementation](trinomial_tree_implementation.md) (tree construction theory)
    - [No Closed-Form Bond Prices](no_closed_form_bond_prices.md) (why numerical methods are required)

!!! abstract "Learning Objectives"
    By the end of this guide, you will be able to:

    1. Explain the class architecture and its inputs (yield curve, mean reversion, volatility)
    2. Map the trinomial tree construction to the branching probability formulas
    3. Describe how $\theta(t_k)$ is calibrated at each time step via forward induction
    4. Price zero-coupon bonds and caplets by backward induction on the tree
    5. Identify numerical parameters (time steps, $j_{\max}$) and their impact on accuracy

---

## Class Overview

The `BlackKarasinski` class encapsulates the model and the tree:

```python
class BlackKarasinski:
    def __init__(self, a, sigma, P, n_steps=100):
        self.a = a          # mean-reversion speed
        self.sigma = sigma  # log-rate volatility
        self.P = P          # market discount curve P^M(0, T)
        self.n_steps = n_steps
```

The market curve `P` is a callable $P^M: [0, \infty) \to (0, 1]$ satisfying $P^M(0) = 1$. All tree construction and pricing methods derive from these three inputs.

---

## Tree Construction

### Grid parameters

The tree discretizes the log-rate $x = \ln r$ on a uniform grid:

$$
\Delta x = \sigma\sqrt{3\Delta t}, \qquad j_{\max} = \left\lceil\frac{0.184}{a\,\Delta t}\right\rceil
$$

The time step $\Delta t = T_{\max}/N$ where $N$ is `n_steps` and $T_{\max}$ is the longest maturity to be priced.

### Branching probabilities

At node $(t_k, x_j)$ with conditional drift $\mu_j = \theta(t_k) - a\,x_j$, the standard branching probabilities are:

$$
p_u = \frac{1}{6} + \frac{(\mu_j\,\Delta t)^2 + \mu_j\,\Delta t\,\Delta x}{2\,\Delta x^2}
$$

$$
p_m = \frac{2}{3} - \frac{(\mu_j\,\Delta t)^2}{\Delta x^2}
$$

$$
p_d = \frac{1}{6} + \frac{(\mu_j\,\Delta t)^2 - \mu_j\,\Delta t\,\Delta x}{2\,\Delta x^2}
$$

When $|j| > j_{\max}$, the code switches to up-branching or down-branching geometry to keep all probabilities in $[0, 1]$.

```python
def _branching_probs(self, j, theta_k, dt, dx):
    mu = (theta_k - self.a * j * dx) * dt
    if abs(j) <= self.j_max:
        # Standard branching
        pu = 1/6 + (mu**2 + mu * dx) / (2 * dx**2)
        pm = 2/3 - mu**2 / dx**2
        pd = 1/6 + (mu**2 - mu * dx) / (2 * dx**2)
    elif j > 0:
        # Down branching for high rates
        ...
    else:
        # Up branching for low rates
        ...
    return pu, pm, pd
```

---

## Calibration of Theta

### Forward induction

The drift $\theta(t_k)$ at each time step is determined by matching the market discount factor $P^M(0, t_{k+1})$. The procedure is:

1. At time $t_0 = 0$, the tree has a single node at $x_0 = \ln r(0)$ with Arrow-Debreu price $Q(0, 0) = 1$
2. At each subsequent step $t_k$, the Arrow-Debreu prices $Q(k, j)$ propagate forward:

$$
Q(k+1, j') = \sum_{j} Q(k, j)\,e^{-e^{x_j}\Delta t}\,p(j \to j')
$$

3. Choose $\theta(t_k)$ so that

$$
\sum_j Q(k+1, j) = P^M(0, t_{k+1})
$$

This is a one-dimensional root-finding problem (bisection or Newton) at each time step because $\theta(t_k)$ affects the branching probabilities and hence the forward propagation.

```python
def calibrate_theta(self, T_max):
    """Calibrate theta(t_k) at each time step."""
    dt = T_max / self.n_steps
    dx = self.sigma * np.sqrt(3 * dt)
    ...
    for k in range(self.n_steps):
        # Solve for theta[k] matching P^M(0, t_{k+1})
        target = self.P((k + 1) * dt)
        theta_k = brentq(lambda th: self._forward_step(Q, th, k, dt, dx) - target, -2, 2)
        self.theta[k] = theta_k
        Q = self._propagate(Q, theta_k, k, dt, dx)
```

---

## Bond and Derivative Pricing

### Zero-coupon bond

To price a bond maturing at $T$:

1. Set terminal values: $V(T, x_j) = 1$ for all $j$
2. Roll backward: $V(t_k, x_j) = e^{-e^{x_j}\Delta t}[p_u V(t_{k+1}, j_u) + p_m V(t_{k+1}, j_m) + p_d V(t_{k+1}, j_d)]$
3. Read $V(0, x_0)$

### Caplet

A caplet with reset $T_i$ and payment $T_{i+1}$:

1. Compute the LIBOR rate at each node at $T_i$: $L_j = \frac{1}{\delta}(1/P_{\text{tree}}(T_i, T_{i+1}; x_j) - 1)$
2. Set payoff at $T_{i+1}$: $V(T_{i+1}, x_j) = \delta[L_j - K]^+$
3. Roll backward to $t = 0$

### European swaption

Swaptions are priced similarly: compute the swap value at the exercise date at each node, set the payoff as $[\text{swap value}]^+$, and roll backward.

---

## Numerical Parameters

| Parameter | Default | Effect |
|-----------|---------|--------|
| `n_steps` | 100 | Higher = more accurate, $O(N^2)$ cost |
| $j_{\max}$ | $\lceil 0.184/(a\Delta t)\rceil$ | Controls tree width |
| $\Delta x$ | $\sigma\sqrt{3\Delta t}$ | Log-rate spacing |

!!! tip "Convergence Testing"
    Run pricing at 50, 100, and 200 steps. If the 100-step and 200-step prices agree to 4 decimal places, 100 steps is sufficient. For swaptions with long tenors (10Y+), 200+ steps may be needed.

---

## Summary

| Component | Method | Mathematical basis |
|-----------|--------|-------------------|
| Tree grid | `__init__` | $\Delta x = \sigma\sqrt{3\Delta t}$, $j_{\max}$ cutoff |
| Probabilities | `_branching_probs` | Mean/variance matching for OU in log-rate |
| $\theta$ calibration | `calibrate_theta` | Forward induction matching $P^M(0, t_k)$ |
| Bond pricing | `price_bond` | Backward induction with $e^{x_j}$ discounting |
| Caplet pricing | `price_caplet` | LIBOR payoff + backward induction |

For calibration of the model parameters $(a, \sigma)$ to market cap volatilities using this tree, see [Calibration to Cap Volatilities](calibration_to_cap_volatilities.md). For a comparison with the Hull-White tree implementation, see [Comparison with Hull-White](comparison_with_hull_white.md).
