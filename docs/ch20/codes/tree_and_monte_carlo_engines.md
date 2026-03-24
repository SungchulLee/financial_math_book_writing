# Tree and Monte Carlo Engines Guide

While the Hull-White model has closed-form prices for vanilla European derivatives, path-dependent products (Bermudan swaptions, callable bonds, range accruals) and products requiring early exercise require numerical engines. This guide describes the two main numerical pricing engines in the companion `tree_and_monte_carlo_engines.py`: a Hull-White trinomial tree and a Monte Carlo simulator. Each engine builds on the `HullWhite` model class and its named functions.

!!! info "Prerequisites"
    - [Hull-White Model Class Guide](hull_white_model_class.md) (model parameters and named functions)
    - [Short Rate Solution](../short_rate/short_rate_solution.md) (OU process solution for exact simulation)
    - [Bond and Derivative Pricing Classes Guide](bond_derivative_pricing_classes.md) (closed-form benchmarks)

!!! abstract "Learning Objectives"
    By the end of this guide, you will be able to:

    1. Construct a Hull-White trinomial tree with calibrated $\theta(t)$
    2. Price derivatives by backward induction on the tree, including early-exercise products
    3. Simulate short-rate paths using the exact OU transition density
    4. Price derivatives by Monte Carlo with discounting along simulated paths
    5. Apply variance reduction (antithetic variates, control variates) to improve efficiency

---

## Trinomial Tree Engine

### Tree construction

The Hull-White trinomial tree is built for the short rate $r_t$ directly (unlike Black-Karasinski, which works in log-rate space). The tree uses:

$$
\Delta r = \sigma\sqrt{3\Delta t}, \qquad j_{\max} = \left\lceil\frac{0.184}{\lambda\,\Delta t}\right\rceil
$$

At each node $(t_k, r_j)$ where $r_j = r_0 + j\,\Delta r$, the branching probabilities match the conditional mean and variance of the OU process:

$$
p_u = \frac{1}{6} + \frac{(\mu_j\,\Delta t)^2 + \mu_j\,\Delta t\,\Delta r}{2\,\Delta r^2}
$$

$$
p_m = \frac{2}{3} - \frac{(\mu_j\,\Delta t)^2}{\Delta r^2}
$$

$$
p_d = \frac{1}{6} + \frac{(\mu_j\,\Delta t)^2 - \mu_j\,\Delta t\,\Delta r}{2\,\Delta r^2}
$$

where $\mu_j = \theta(t_k) - \lambda r_j$.

### Theta calibration on the tree

The drift $\theta(t_k)$ is calibrated at each time step by forward induction, matching the market discount factor $P^M(0, t_{k+1})$:

```python
class HullWhiteTree:
    def __init__(self, hw_model, T_max, n_steps):
        self.hw = hw_model
        self.dt = T_max / n_steps
        self.dr = hw_model.sigma * np.sqrt(3 * self.dt)
        self.j_max = int(np.ceil(0.184 / (hw_model.lambd * self.dt)))
        self.theta = np.zeros(n_steps)
        self._calibrate_theta()
```

### Backward induction

For a generic payoff $V(T, r)$ at maturity $T$:

1. Set terminal values: $V(T, r_j)$ for all nodes at time $T$
2. Roll backward:

$$
V(t_k, r_j) = e^{-r_j\Delta t}\left[p_u\,V(t_{k+1}, r_{j+1}) + p_m\,V(t_{k+1}, r_j) + p_d\,V(t_{k+1}, r_{j-1})\right]
$$

3. For early-exercise products (Bermudan swaptions), at each exercise date compare the continuation value with the exercise value and take the maximum.

```python
def price(self, payoff_func, exercise_dates=None):
    """Price a derivative by backward induction.

    payoff_func: callable(t_k, r_j) -> payoff value
    exercise_dates: list of time indices for early exercise (optional)
    """
    V = np.array([payoff_func(self.n_steps, r_j) for r_j in self.rate_grid])
    for k in range(self.n_steps - 1, -1, -1):
        V_new = np.zeros_like(V)
        for j in range(-self.j_max, self.j_max + 1):
            pu, pm, pd = self._probs(k, j)
            V_new[j] = np.exp(-self.rate(k, j) * self.dt) * (
                pu * V[j+1] + pm * V[j] + pd * V[j-1]
            )
        if exercise_dates and k in exercise_dates:
            for j in range(-self.j_max, self.j_max + 1):
                V_new[j] = max(V_new[j], payoff_func(k, self.rate(k, j)))
        V = V_new
    return V[0]
```

---

## Monte Carlo Engine

### Exact simulation

The Hull-White short rate follows an OU process with known transition density. Given $r_{t_k}$, the rate at $t_{k+1} = t_k + \Delta t$ is:

$$
r_{t_{k+1}} = \psi(t_k, t_{k+1}) + e^{-\lambda\Delta t}(r_{t_k} - \psi(t_k, t_{k+1})) + \sigma_r(t_k, t_{k+1})\,Z
$$

where $Z \sim \mathcal{N}(0,1)$, $\psi$ is the conditional mean function, and $\sigma_r^2$ is the conditional variance. This is an exact simulation (no discretization error in the rate itself).

```python
class HullWhiteMC:
    def __init__(self, hw_model, n_paths=10000, n_steps=100):
        self.hw = hw_model
        self.n_paths = n_paths
        self.n_steps = n_steps

    def simulate(self, T, r0):
        dt = T / self.n_steps
        rates = np.zeros((self.n_paths, self.n_steps + 1))
        rates[:, 0] = r0
        for k in range(self.n_steps):
            t_k = k * dt
            psi = self.hw.compute_psi_conditional(t_k, t_k + dt, rates[:, k])
            var = self.hw.compute_var(t_k, t_k + dt)
            Z = np.random.randn(self.n_paths)
            rates[:, k+1] = psi + np.sqrt(var) * Z
        return rates
```

### Pricing by Monte Carlo

The price of a derivative with payoff $V(T)$ at maturity $T$ is:

$$
V(0) = \frac{1}{N}\sum_{i=1}^N \exp\!\left(-\sum_{k=0}^{M-1} r_{t_k}^{(i)}\,\Delta t\right) V^{(i)}(T)
$$

```python
def price(self, T, r0, payoff_func):
    rates = self.simulate(T, r0)
    dt = T / self.n_steps
    discount = np.exp(-np.sum(rates[:, :-1] * dt, axis=1))
    payoffs = np.array([payoff_func(rates[i, :]) for i in range(self.n_paths)])
    return np.mean(discount * payoffs)
```

### Variance reduction

**Antithetic variates**: For each path with Gaussian increments $Z_1, \ldots, Z_M$, generate a mirror path with $-Z_1, \ldots, -Z_M$. Average the two payoffs before discounting.

**Control variates**: Use the closed-form ZCB price as a control. The adjusted estimator is:

$$
\hat{V}_{\text{cv}} = \hat{V} - \beta\left(\hat{P}_{\text{MC}}(0,T) - P^M(0,T)\right)
$$

where $\beta$ is the regression coefficient estimated from the simulation.

!!! tip "When to Use Which Engine"
    | Product | Recommended engine |
    |---------|-------------------|
    | European bond option, cap, swaption | Closed-form (fastest) |
    | Bermudan swaption | Trinomial tree |
    | Callable bond | Trinomial tree |
    | Path-dependent (range accrual, TARNs) | Monte Carlo |
    | Portfolio-level XVA | Monte Carlo |

---

## Summary

| Engine | Method | Strengths | Limitations |
|--------|--------|-----------|-------------|
| Trinomial tree | Backward induction | Early exercise, deterministic, fast for 1-factor | Curse of dimensionality for multi-factor |
| Monte Carlo | Forward simulation | Path-dependent payoffs, scalable | No early exercise (without LSM), statistical error |

For closed-form pricing of European derivatives, see [Bond and Derivative Pricing Classes Guide](bond_derivative_pricing_classes.md). For the calibration workflow that uses all three engines, see [Calibration Pipeline Guide](calibration_pipeline.md).

---

## Exercises

**Exercise 1.** For the Hull-White trinomial tree with $\sigma = 0.01$, $\lambda = 0.05$, and $\Delta t = 0.01$, compute the rate spacing $\Delta r = \sigma\sqrt{3\Delta t}$ and the maximum node index $j_{\max} = \lceil 0.184/(\lambda\,\Delta t) \rceil$. How many nodes does the tree have at each time step? What happens to $j_{\max}$ if $\lambda$ is increased to 0.50?

---

**Exercise 2.** Verify that the branching probabilities $p_u$, $p_m$, $p_d$ sum to 1 and that they match the conditional mean $\mu_j\,\Delta t$ and conditional variance $\sigma^2\,\Delta t$ of the OU process. Write out the two moment-matching equations explicitly and solve for $p_u$, $p_m$, $p_d$ as functions of $\mu_j$, $\Delta t$, and $\Delta r$.

---

**Exercise 3.** Price a 5-year zero-coupon bond using the trinomial tree with 500 time steps. The terminal payoff is $V(T, r_j) = 1$ for all nodes. Roll backward using the discounted expectation formula. Compare the result with the analytical price $P^M(0, 5)$ and report the pricing error as a function of the number of time steps (try $n = 50, 100, 200, 500$). What convergence rate do you observe?

---

**Exercise 4.** Explain the difference between exact simulation and Euler-Maruyama discretization for the Hull-White short rate. For the exact simulation scheme, the transition from $r_{t_k}$ to $r_{t_{k+1}}$ uses the OU conditional distribution. Write down the conditional mean $\psi(t_k, t_{k+1})$ and conditional variance $\sigma_r^2(t_k, t_{k+1})$ explicitly. What advantage does exact simulation have over Euler-Maruyama for computing the money market account?

---

**Exercise 5.** Implement antithetic variates for pricing a 3-year caplet. For each set of $N/2$ Gaussian increments $\{Z_1, \ldots, Z_M\}$, generate both the original and the negated path $\{-Z_1, \ldots, -Z_M\}$. Average the two caplet payoffs before discounting. Compare the standard error with and without antithetic variates for $N = 10{,}000$ total paths.

---

**Exercise 6.** Describe how you would price a Bermudan swaption on the trinomial tree. At each exercise date, the algorithm compares the continuation value with the exercise value. For a 5-into-5 Bermudan swaption (exercisable at years 5, 6, 7, 8, 9), how many backward induction steps are needed? At which nodes is the early-exercise check performed? What determines whether the holder exercises early?

---

**Exercise 7.** The control variate technique uses the closed-form ZCB price as a control. If $\hat{V}$ is the raw MC swaption estimate and $\hat{P}_{\text{MC}}(0, T)$ is the MC estimate of the ZCB price, the adjusted estimator is $\hat{V}_{\text{cv}} = \hat{V} - \beta(\hat{P}_{\text{MC}} - P^M)$. Explain how to estimate $\beta$ from the simulation. Why is this technique particularly effective in the Hull-White model?
