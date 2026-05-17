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

### Grid parameters and branching probabilities

Recall (see [§ Trinomial Tree Implementation](trinomial_tree_implementation.md)) the grid spacing $\Delta x = \sigma\sqrt{3\Delta t}$ and width $j_{\max} = \lceil 0.184/(a\Delta t)\rceil$, with standard branching probabilities determined by mean/variance matching of the conditional OU increment. The code switches to up- or down-branching when $|j| > j_{\max}$ to keep probabilities in $[0,1]$.

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

Recall (see [§ Trinomial Tree Implementation](trinomial_tree_implementation.md)) that $\theta(t_k)$ is found at each time step by propagating Arrow-Debreu prices $Q(k,j)$ forward and solving $\sum_j Q(k+1,j) = P^M(0,t_{k+1})$ for $\theta(t_k)$ (a one-dimensional root-find at each step).

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

---

## Exercises

**Exercise 1.** Given $a = 0.10$, $\sigma = 0.20$, and $\Delta t = 0.01$ year, compute the grid spacing $\Delta x = \sigma\sqrt{3\Delta t}$ and the maximum node index $j_{\max} = \lceil 0.184/(a\Delta t) \rceil$. How many nodes exist at a given time step (in terms of $j_{\max}$)?

??? success "Solution to Exercise 1"
    With $a = 0.10$, $\sigma = 0.20$, $\Delta t = 0.01$:

    **Grid spacing**:

    $$
    \Delta x = \sigma\sqrt{3\Delta t} = 0.20\sqrt{3 \times 0.01} = 0.20\sqrt{0.03} = 0.20 \times 0.17321 = 0.03464
    $$

    **Maximum node index**:

    $$
    j_{\max} = \left\lceil\frac{0.184}{a\,\Delta t}\right\rceil = \left\lceil\frac{0.184}{0.10 \times 0.01}\right\rceil = \left\lceil\frac{0.184}{0.001}\right\rceil = \lceil 184 \rceil = 184
    $$

    **Number of nodes at a given time step**: The nodes run from $j = -j_{\max}$ to $j = +j_{\max}$, giving

    $$
    2j_{\max} + 1 = 2 \times 184 + 1 = 369 \text{ nodes}
    $$

    Note that in practice, not all nodes may be reachable at every time step (the tree grows gradually), but at later time steps, up to 369 nodes can be active.

---

**Exercise 2.** At node $(t_k, x_j)$ with $j = 3$, $\Delta x = 0.03464$, $\theta(t_k) = -0.25$, $a = 0.10$, and $\Delta t = 0.01$, compute the conditional drift $\mu_j = \theta(t_k) - a \cdot j \cdot \Delta x$ and then the standard branching probabilities $p_u$, $p_m$, $p_d$. Verify that $p_u + p_m + p_d = 1$ and all probabilities are non-negative.

??? success "Solution to Exercise 2"
    At node $(t_k, x_j)$ with $j = 3$, $\Delta x = 0.03464$, $\theta(t_k) = -0.25$, $a = 0.10$, $\Delta t = 0.01$:

    **Conditional drift**:

    $$
    \mu_j = \theta(t_k) - a \cdot j \cdot \Delta x = -0.25 - 0.10 \times 3 \times 0.03464 = -0.25 - 0.01039 = -0.26039
    $$

    **Drift times time step**:

    $$
    \mu_j \Delta t = -0.26039 \times 0.01 = -0.002604
    $$

    **Intermediate quantities**:

    $$
    \frac{(\mu_j \Delta t)^2}{\Delta x^2} = \frac{(-0.002604)^2}{(0.03464)^2} = \frac{6.781 \times 10^{-6}}{1.200 \times 10^{-3}} = 0.005651
    $$

    $$
    \frac{\mu_j \Delta t}{\Delta x} = \frac{-0.002604}{0.03464} = -0.07516
    $$

    **Branching probabilities**:

    $$
    p_u = \frac{1}{6} + \frac{(\mu_j \Delta t)^2}{2\Delta x^2} + \frac{\mu_j \Delta t}{2\Delta x} = 0.16667 + 0.002826 + (-0.03758) = 0.13191
    $$

    $$
    p_m = \frac{2}{3} - \frac{(\mu_j \Delta t)^2}{\Delta x^2} = 0.66667 - 0.005651 = 0.66102
    $$

    $$
    p_d = \frac{1}{6} + \frac{(\mu_j \Delta t)^2}{2\Delta x^2} - \frac{\mu_j \Delta t}{2\Delta x} = 0.16667 + 0.002826 + 0.03758 = 0.20707
    $$

    **Verification**: $p_u + p_m + p_d = 0.13191 + 0.66102 + 0.20707 = 1.00000$. All probabilities are non-negative: $p_u = 0.132 > 0$, $p_m = 0.661 > 0$, $p_d = 0.207 > 0$.

    The negative drift ($\mu_j < 0$) shifts probability toward the down branch ($p_d > p_u$), reflecting mean reversion pulling the rate back toward the center when $j > 0$ (rate above the long-run mean).

---

**Exercise 3.** Explain the role of the Arrow-Debreu prices $Q(k, j)$ in the forward induction procedure. If at time step $k$ there are 5 active nodes with Arrow-Debreu prices $Q(k, -2) = 0.02$, $Q(k, -1) = 0.15$, $Q(k, 0) = 0.55$, $Q(k, 1) = 0.20$, $Q(k, 2) = 0.03$, what is the model discount factor $P^{\text{model}}(0, t_k)$? How does this relate to the calibration condition?

??? success "Solution to Exercise 3"
    Arrow-Debreu prices $Q(k, j)$ represent the present value at time $0$ of a security that pays \$1 if and only if node $(t_k, j)$ is reached. They aggregate the probability-weighted discounting across all paths from the root to that node.

    **Role in forward induction**: The Arrow-Debreu prices carry the combined information of path probabilities and accumulated discounting. They propagate forward through the tree via

    $$
    Q(k+1, j') = \sum_{j \to j'} Q(k, j) \cdot p_{j \to j'} \cdot e^{-r_j \Delta t}
    $$

    This eliminates the need for backward induction when calibrating $\theta(t_k)$.

    **Model discount factor**: The model discount factor to time $t_k$ is the sum of all Arrow-Debreu prices at that time step:

    $$
    P^{\text{model}}(0, t_k) = \sum_j Q(k, j)
    $$

    This is because a zero-coupon bond paying \$1 at $t_k$ pays \$1 at every node at $t_k$, so its value is the sum of all state prices.

    With the given values:

    $$
    P^{\text{model}}(0, t_k) = 0.02 + 0.15 + 0.55 + 0.20 + 0.03 = 0.95
    $$

    **Relation to calibration**: The calibration condition requires $P^{\text{model}}(0, t_k) = P^{\text{mkt}}(0, t_k)$. If the market discount factor to $t_k$ is 0.95, then the model is correctly calibrated at this step. The forward induction calibration adjusts $\theta(t_{k-1})$ (the drift at the previous step) to ensure this equality holds at each time step.

---

**Exercise 4.** The `calibrate_theta` method uses `brentq` to solve for $\theta(t_k)$ at each time step. Explain why the calibration equation $\sum_j Q(k+1, j) = P^{\text{mkt}}(0, t_{k+1})$ is monotone in $\theta(t_k)$ (i.e., why the root is unique). What is the economic intuition for why increasing $\theta(t_k)$ changes the sum of Arrow-Debreu prices?

??? success "Solution to Exercise 4"
    The calibration equation is $\sum_j Q(k+1, j) = P^{\text{mkt}}(0, t_{k+1})$, where

    $$
    Q(k+1, j') = \sum_j Q(k, j) \cdot p_{j \to j'}(\theta_k) \cdot e^{-e^{x_j}\Delta t}
    $$

    **Why it is nonlinear in $\theta_k$**: The branching probabilities $p_u$, $p_m$, $p_d$ depend on $\theta_k$ through the conditional drift $\mu_j = \theta_k - ax_j$. Specifically, the probabilities are quadratic polynomials in $\mu_j \Delta t$ (and hence in $\theta_k$). When these probabilities multiply the Arrow-Debreu prices $Q(k,j)$ and sum over $j$, the resulting function of $\theta_k$ is a sum of quadratics in $\theta_k$, making the overall equation nonlinear (quadratic) in $\theta_k$.

    **Economic intuition for monotonicity**: Increasing $\theta_k$ raises the drift of the log rate $x_{t_{k+1}}$, which shifts the short rate distribution at $t_{k+1}$ upward (higher rates). Higher short rates at $t_{k+1}$ mean higher discounting, which reduces the one-period discount factors $e^{-e^{x_j}\Delta t}$. This in turn reduces the Arrow-Debreu prices $Q(k+1, j)$ and hence their sum. Therefore:

    $$
    \theta_k \uparrow \;\implies\; r_{t_{k+1}} \uparrow \;\implies\; \text{discount factors} \downarrow \;\implies\; \sum_j Q(k+1, j) \downarrow
    $$

    The function $\sum_j Q(k+1, j)$ is monotonically decreasing in $\theta_k$, guaranteeing a unique root for any target $P^{\text{mkt}}(0, t_{k+1}) \in (0, 1)$.

    **Robustness of bisection vs. Newton**: Bisection is more robust because it only requires monotonicity (guaranteed) and bounded brackets. Newton's method is faster (quadratic convergence vs. linear) but requires computing the derivative of $\sum_j Q(k+1, j)$ with respect to $\theta_k$, which involves differentiating the branching probabilities. In practice, both work well, but bisection (or Brent's method, which combines bisection with interpolation) is preferred for its guaranteed convergence without derivative computation.

---

**Exercise 5.** Describe how the backward induction for a caplet differs from that for a zero-coupon bond. Specifically, for a caplet with reset $T_i$ and payment $T_{i+1}$, explain: (i) what terminal condition is set at $T_{i+1}$, (ii) how the LIBOR rate $L_j$ is computed at each node at $T_i$, and (iii) why a separate bond price computation is needed at $T_i$ nodes.

??? success "Solution to Exercise 5"
    **Zero-coupon bond**: Terminal condition $V(T, x_j) = 1$ for all $j$. Backward induction rolls the constant terminal value back through the tree, with discounting at each node. No payoff computation is needed at intermediate nodes --- only discounting.

    **Caplet**: The differences are:

    **(i) Terminal condition at $T_{i+1}$**: Instead of $V = 1$, the caplet payoff is $V(T_{i+1}, x_j) = \delta[L_j - K]^+$, where $L_j$ is the LIBOR rate at node $j$ at the reset date $T_i$. Strictly speaking, the payoff at $T_{i+1}$ depends on the LIBOR rate observed at $T_i$, so the payoff must be set based on the rate information at $T_i$.

    **(ii) LIBOR rate computation at $T_i$**: At each node $(T_i, x_j)$, the one-period bond price $P_{\text{tree}}(T_i, T_{i+1}; x_j)$ is computed by a single-step backward induction:

    $$
    P_{\text{tree}}(T_i, T_{i+1}; x_j) = e^{-e^{x_j}\delta}\left[p_u \cdot 1 + p_m \cdot 1 + p_d \cdot 1\right] = e^{-e^{x_j}\delta}
    $$

    (since the bond pays 1 at all successor nodes). Then the LIBOR rate is

    $$
    L_j = \frac{1}{\delta}\left[\frac{1}{P_{\text{tree}}(T_i, T_{i+1}; x_j)} - 1\right] = \frac{1}{\delta}(e^{e^{x_j}\delta} - 1)
    $$

    **(iii) Why a separate bond price is needed**: The LIBOR rate $L_j$ is not directly available from the log-rate $x_j$; it depends on the one-period discount factor, which requires knowing how the tree discounts between $T_i$ and $T_{i+1}$. This is a bond price computation (albeit a simple one-step one). Without this bond price, the caplet payoff cannot be evaluated, since the caplet is an option on the LIBOR rate, not on the short rate directly. The relationship $L_j \approx e^{x_j}$ holds only approximately for small $\delta$; for accurate pricing, the exact tree-based bond price must be used.

---

**Exercise 6.** A practitioner runs the BK tree with `n_steps = 50` and gets a 5-year zero-coupon bond price of 0.7695. With `n_steps = 100`, the price is 0.7700, and with `n_steps = 200`, it is 0.7701. Use Richardson extrapolation to estimate the converged bond price from the 50-step and 100-step results. How does your extrapolated value compare to the 200-step result?

??? success "Solution to Exercise 6"
    The tree convergence is first order: the error is approximately $E(N) = c/N + O(1/N^2)$ for some constant $c$, where $N$ is `n_steps`.

    Given:

    - $P_{50} = 0.7695$ (50 steps)
    - $P_{100} = 0.7700$ (100 steps)
    - $P_{200} = 0.7701$ (200 steps)

    For first-order convergence with $\Delta t \propto 1/N$, the error scales as $E_N \approx c \cdot \Delta t = c'/N$. With two resolutions $N$ and $2N$:

    $$
    P_N = P_\infty + \frac{c'}{N}, \qquad P_{2N} = P_\infty + \frac{c'}{2N}
    $$

    Subtracting: $P_N - P_{2N} = \frac{c'}{2N}$, so $c' = 2N(P_N - P_{2N})$.

    The Richardson extrapolation combines the two:

    $$
    P_{\text{Rich}} = 2P_{2N} - P_N
    $$

    Using $N = 50$ and $2N = 100$:

    $$
    P_{\text{Rich}} = 2 \times 0.7700 - 0.7695 = 1.5400 - 0.7695 = 0.7705
    $$

    Comparing with the 200-step result of $0.7701$, the Richardson extrapolated value ($0.7705$) overshoots slightly, suggesting that the convergence is not purely first-order (there are higher-order terms). Nevertheless, the Richardson estimate ($0.7705$) is closer to the converged value than either the 50-step ($0.7695$) or 100-step ($0.7700$) results alone.

    A more refined approach would use 100 and 200 steps for Richardson extrapolation: $P_{\text{Rich}} = 2 \times 0.7701 - 0.7700 = 0.7702$, which would be expected to be more accurate since both base estimates are closer to convergence.

---

**Exercise 7.** The code switches from standard branching to up/down branching when $|j| > j_{\max}$. Explain why standard branching produces negative probabilities for large $|j|$ by examining the formula for $p_m$ as $|\mu_j \Delta t|$ grows relative to $\Delta x$. What is the economic scenario (in terms of the short rate level) that triggers the branching switch?

??? success "Solution to Exercise 7"
    The standard branching middle probability is

    $$
    p_m = \frac{2}{3} - \frac{(\mu_j \Delta t)^2}{\Delta x^2}
    $$

    where $\mu_j = \theta(t_k) - a \cdot j \cdot \Delta x$. As $|j|$ increases, $|a \cdot j \cdot \Delta x|$ grows, making $|\mu_j|$ larger (the mean-reverting drift becomes stronger at nodes far from the center).

    With $\Delta x = \sigma\sqrt{3\Delta t}$, we have $\Delta x^2 = 3\sigma^2 \Delta t$, so

    $$
    \frac{(\mu_j \Delta t)^2}{\Delta x^2} = \frac{\mu_j^2 \Delta t^2}{3\sigma^2 \Delta t} = \frac{\mu_j^2 \Delta t}{3\sigma^2}
    $$

    For $p_m$ to become negative, we need

    $$
    \frac{\mu_j^2 \Delta t}{3\sigma^2} > \frac{2}{3} \implies |\mu_j| > \frac{\sigma\sqrt{2}}{\sqrt{\Delta t}}
    $$

    Since $\mu_j \approx -a \cdot j \cdot \Delta x$ for large $|j|$ (the $\theta$ contribution is bounded), the condition becomes approximately

    $$
    a \cdot |j| \cdot \sigma\sqrt{3\Delta t} > \frac{\sigma\sqrt{2}}{\sqrt{\Delta t}} \implies |j| > \frac{\sqrt{2}}{\sqrt{3}\,a\,\Delta t} = \frac{0.8165}{a\,\Delta t}
    $$

    The threshold $j_{\max} = \lceil 0.184/(a\Delta t) \rceil$ is set conservatively below this bound to also ensure $p_u \geq 0$ and $p_d \geq 0$.

    **Economic scenario**: Large $|j|$ corresponds to the log rate $x_j = j \cdot \Delta x$ being far from the center. For $j \gg 0$, the short rate $r = e^{x_j}$ is extremely high; for $j \ll 0$, the rate is extremely low. In both cases, the mean-reverting drift is very strong (pulling rates back to normal levels), and the drift displacement $|\mu_j \Delta t|$ exceeds the grid spacing $\Delta x$. This means the expected move in one time step is larger than one grid step, making the standard three-node branching unable to allocate non-negative probabilities. The up/down branching shifts the successor nodes to accommodate the large drift, ensuring valid probabilities while preserving the mean and variance matching conditions.
