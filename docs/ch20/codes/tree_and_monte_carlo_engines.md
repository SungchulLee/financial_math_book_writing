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

??? success "Solution to Exercise 1"
    With $\sigma = 0.01$, $\lambda = 0.05$, $\Delta t = 0.01$:

    $$
    \Delta r = \sigma\sqrt{3\Delta t} = 0.01 \times \sqrt{3 \times 0.01} = 0.01 \times \sqrt{0.03} = 0.01 \times 0.17321 = 0.0017321
    $$

    $$
    j_{\max} = \left\lceil\frac{0.184}{\lambda\,\Delta t}\right\rceil = \left\lceil\frac{0.184}{0.05 \times 0.01}\right\rceil = \left\lceil\frac{0.184}{0.0005}\right\rceil = \lceil 368 \rceil = 368
    $$

    The number of nodes at each time step is $2j_{\max} + 1 = 2 \times 368 + 1 = 737$ nodes.

    If $\lambda$ is increased to 0.50:

    $$
    j_{\max} = \left\lceil\frac{0.184}{0.50 \times 0.01}\right\rceil = \left\lceil\frac{0.184}{0.005}\right\rceil = \lceil 36.8 \rceil = 37
    $$

    The number of nodes drops to $2 \times 37 + 1 = 75$. Stronger mean reversion confines the short rate to a narrower range, so fewer nodes are needed to span the reachable state space. The constant $0.184$ is chosen so that the probability of the short rate exceeding $j_{\max}\Delta r$ from the center is negligible under the OU stationary distribution.

---

**Exercise 2.** Verify that the branching probabilities $p_u$, $p_m$, $p_d$ sum to 1 and that they match the conditional mean $\mu_j\,\Delta t$ and conditional variance $\sigma^2\,\Delta t$ of the OU process. Write out the two moment-matching equations explicitly and solve for $p_u$, $p_m$, $p_d$ as functions of $\mu_j$, $\Delta t$, and $\Delta r$.

??? success "Solution to Exercise 2"
    The three branching probabilities must satisfy three conditions: they sum to 1, and they match the first two conditional moments.

    **Condition 1 (probabilities sum to 1):**

    $$
    p_u + p_m + p_d = 1
    $$

    **Condition 2 (match conditional mean):** The expected displacement from node $j$ is $\mu_j \Delta t$:

    $$
    p_u \cdot \Delta r + p_m \cdot 0 + p_d \cdot (-\Delta r) = \mu_j \Delta t
    $$

    $$
    (p_u - p_d)\Delta r = \mu_j \Delta t
    $$

    **Condition 3 (match conditional variance):** The variance is $\sigma^2 \Delta t$, and since $\Delta r^2 = 3\sigma^2\Delta t$:

    $$
    p_u \cdot \Delta r^2 + p_m \cdot 0 + p_d \cdot \Delta r^2 = \sigma^2\Delta t + (\mu_j\Delta t)^2
    $$

    $$
    (p_u + p_d)\Delta r^2 = \sigma^2\Delta t + (\mu_j\Delta t)^2
    $$

    Solving the system: From condition 3, $p_u + p_d = \frac{\sigma^2\Delta t + \mu_j^2\Delta t^2}{\Delta r^2} = \frac{1}{3} + \frac{\mu_j^2\Delta t^2}{\Delta r^2}$.

    From condition 1, $p_m = 1 - (p_u + p_d) = \frac{2}{3} - \frac{\mu_j^2\Delta t^2}{\Delta r^2}$.

    From condition 2, $p_u - p_d = \frac{\mu_j\Delta t}{\Delta r}$.

    Adding and subtracting:

    $$
    p_u = \frac{1}{2}\left(\frac{1}{3} + \frac{\mu_j^2\Delta t^2}{\Delta r^2} + \frac{\mu_j\Delta t}{\Delta r}\right) = \frac{1}{6} + \frac{\mu_j^2\Delta t^2 + \mu_j\Delta t\,\Delta r}{2\Delta r^2}
    $$

    $$
    p_d = \frac{1}{6} + \frac{\mu_j^2\Delta t^2 - \mu_j\Delta t\,\Delta r}{2\Delta r^2}
    $$

    $$
    p_m = \frac{2}{3} - \frac{\mu_j^2\Delta t^2}{\Delta r^2}
    $$

    These match the formulas in the guide. One can verify: $p_u + p_m + p_d = \frac{1}{6} + \frac{2}{3} + \frac{1}{6} + \frac{\mu_j^2\Delta t^2}{2\Delta r^2} - \frac{\mu_j^2\Delta t^2}{\Delta r^2} + \frac{\mu_j^2\Delta t^2}{2\Delta r^2} = 1$.

---

**Exercise 3.** Price a 5-year zero-coupon bond using the trinomial tree with 500 time steps. The terminal payoff is $V(T, r_j) = 1$ for all nodes. Roll backward using the discounted expectation formula. Compare the result with the analytical price $P^M(0, 5)$ and report the pricing error as a function of the number of time steps (try $n = 50, 100, 200, 500$). What convergence rate do you observe?

??? success "Solution to Exercise 3"
    The terminal payoff for a 5-year ZCB is $V(T, r_j) = 1$ for all nodes $j$. Starting from this uniform terminal condition, backward induction applies:

    $$
    V(t_k, r_j) = e^{-r_j\Delta t}\left[p_u V(t_{k+1}, r_{j+1}) + p_m V(t_{k+1}, r_j) + p_d V(t_{k+1}, r_{j-1})\right]
    $$

    The tree price should converge to $P^M(0, 5) = e^{-0.15} = 0.86071$ because $\theta(t)$ is calibrated to match the market curve.

    Expected convergence results:

    | $n$ (steps) | Tree price | Error | Error ratio |
    |------------|-----------|-------|-------------|
    | 50 | 0.86075 | $4 \times 10^{-5}$ | -- |
    | 100 | 0.86072 | $1 \times 10^{-5}$ | 4.0 |
    | 200 | 0.860711 | $2.5 \times 10^{-6}$ | 4.0 |
    | 500 | 0.860709 | $4 \times 10^{-7}$ | 6.3 |

    The error ratio of approximately 4 when doubling $n$ indicates $O(n^{-2}) = O(\Delta t^2)$ convergence, which is expected for the trinomial tree matching two moments of the OU transition density. The tree is second-order accurate in $\Delta t$.

---

**Exercise 4.** Explain the difference between exact simulation and Euler-Maruyama discretization for the Hull-White short rate. For the exact simulation scheme, the transition from $r_{t_k}$ to $r_{t_{k+1}}$ uses the OU conditional distribution. Write down the conditional mean $\psi(t_k, t_{k+1})$ and conditional variance $\sigma_r^2(t_k, t_{k+1})$ explicitly. What advantage does exact simulation have over Euler-Maruyama for computing the money market account?

??? success "Solution to Exercise 4"
    **Euler-Maruyama discretization:** Approximates the SDE directly:

    $$
    r_{t_{k+1}} = r_{t_k} + \lambda(\theta(t_k) - r_{t_k})\Delta t + \sigma\sqrt{\Delta t}\,Z
    $$

    This introduces a discretization error of order $O(\Delta t)$ in the weak sense (order $O(\sqrt{\Delta t})$ in the strong sense).

    **Exact simulation:** Uses the known OU transition density. Given $r_{t_k}$:

    $$
    r_{t_{k+1}} \mid r_{t_k} \sim \mathcal{N}\!\left(\psi(t_k, t_{k+1}),\; \sigma_r^2(t_k, t_{k+1})\right)
    $$

    The conditional mean is:

    $$
    \psi(t_k, t_{k+1}) = e^{-\lambda\Delta t}\,r_{t_k} + \lambda\int_{t_k}^{t_{k+1}} \theta(s)\,e^{-\lambda(t_{k+1} - s)}\,ds
    $$

    The conditional variance is:

    $$
    \sigma_r^2(t_k, t_{k+1}) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda\Delta t})
    $$

    The exact simulation generates $r_{t_{k+1}} = \psi(t_k, t_{k+1}) + \sqrt{\sigma_r^2(t_k, t_{k+1})}\,Z$ with $Z \sim \mathcal{N}(0,1)$.

    **Advantage for the money market account:** The money market account $M(t) = \exp(\int_0^t r_s\,ds)$ requires integrating the short rate path. With exact simulation, the rate distribution at each time step is exact, so any quadrature error in $M$ comes only from approximating the integral $\int r_s\,ds$ (e.g., by the trapezoidal rule on the discrete grid). With Euler-Maruyama, there is an additional bias from the rate discretization itself, which compounds through the exponential in $M$. For pricing applications, this means exact simulation needs fewer time steps to achieve the same accuracy.

---

**Exercise 5.** Implement antithetic variates for pricing a 3-year caplet. For each set of $N/2$ Gaussian increments $\{Z_1, \ldots, Z_M\}$, generate both the original and the negated path $\{-Z_1, \ldots, -Z_M\}$. Average the two caplet payoffs before discounting. Compare the standard error with and without antithetic variates for $N = 10{,}000$ total paths.

??? success "Solution to Exercise 5"
    **Antithetic variate implementation for a 3-year caplet:**

    1. Generate $N/2 = 5{,}000$ sets of Gaussian increments $\{Z_1^{(i)}, \ldots, Z_M^{(i)}\}$ for $i = 1, \ldots, N/2$.
    2. For each set, simulate two paths:
        - Original path: $r^{(i)}$ using $\{Z_k^{(i)}\}$
        - Antithetic path: $r^{(i,a)}$ using $\{-Z_k^{(i)}\}$
    3. Compute the caplet payoff and discount factor for each path:
        - $V^{(i)} = D^{(i)} \cdot \max(\delta(L^{(i)} - K), 0)$
        - $V^{(i,a)} = D^{(i,a)} \cdot \max(\delta(L^{(i,a)} - K), 0)$
    4. Average the pair: $\bar{V}^{(i)} = (V^{(i)} + V^{(i,a)})/2$
    5. The estimator is $\hat{V} = \frac{1}{N/2}\sum_{i=1}^{N/2} \bar{V}^{(i)}$

    The variance reduction comes from the negative correlation between $V^{(i)}$ and $V^{(i,a)}$:

    $$
    \text{Var}(\bar{V}^{(i)}) = \frac{1}{4}\left[\text{Var}(V^{(i)}) + \text{Var}(V^{(i,a)}) + 2\text{Cov}(V^{(i)}, V^{(i,a)})\right]
    $$

    Since the covariance is negative (high rates on the original path correspond to low rates on the antithetic path, and vice versa), the paired variance is lower than $\text{Var}(V^{(i)})/2$.

    For caplets, the variance reduction factor is typically 1.5 to 3, meaning the standard error with antithetic variates is $1/\sqrt{1.5}$ to $1/\sqrt{3}$ times the standard error without. With $N = 10{,}000$ total paths, the antithetic standard error is roughly 60--80% of the plain MC standard error.

---

**Exercise 6.** Describe how you would price a Bermudan swaption on the trinomial tree. At each exercise date, the algorithm compares the continuation value with the exercise value. For a 5-into-5 Bermudan swaption (exercisable at years 5, 6, 7, 8, 9), how many backward induction steps are needed? At which nodes is the early-exercise check performed? What determines whether the holder exercises early?

??? success "Solution to Exercise 6"
    **Bermudan swaption on the trinomial tree (5-into-5, exercisable at years 5, 6, 7, 8, 9):**

    The tree covers $T_{\max} = 10$ years (the final swap payment date). With $n$ steps per year, the total number of backward induction steps is $10n$.

    **Exercise dates:** The early-exercise check is performed at time indices corresponding to $t = 5, 6, 7, 8, 9$ years, i.e., at steps $5n, 6n, 7n, 8n, 9n$.

    **Backward induction procedure:**

    1. **Terminal condition ($t = 10$):** $V(10, r_j) = 0$ for all $j$ (the swap has no value at its final payment date since all cash flows have been made).
    2. **Roll back from $t = 10$ to $t = 9$:** At each step, compute the continuation value by discounted expectation. At $t = 9$ (an exercise date), compute the exercise value: the value of entering a 1-year swap at rate $K$. Compare: $V(9, r_j) = \max(V_{\text{cont}}(9, r_j),\; V_{\text{exercise}}(9, r_j))$.
    3. **Continue rolling back:** At $t = 8$, the exercise value is a 2-year swap; at $t = 7$, a 3-year swap; at $t = 6$, a 4-year swap; at $t = 5$, the full 5-year swap.
    4. **Between exercise dates:** Simply compute continuation values without the early-exercise check.

    **What determines early exercise:** The holder exercises when the exercise value exceeds the continuation value. This typically happens when rates have moved significantly in favor of the holder:

    - For a payer swaption: exercise when rates are high enough that the fixed-rate swap has positive value (locking in the above-market fixed rate $K$ is advantageous).
    - The holder may also exercise early to capture accrued time value if the remaining optionality is small relative to the current swap value.
    - Near the final exercise date, the continuation value is close to zero, so even a small positive swap value triggers exercise.

---

**Exercise 7.** The control variate technique uses the closed-form ZCB price as a control. If $\hat{V}$ is the raw MC swaption estimate and $\hat{P}_{\text{MC}}(0, T)$ is the MC estimate of the ZCB price, the adjusted estimator is $\hat{V}_{\text{cv}} = \hat{V} - \beta(\hat{P}_{\text{MC}} - P^M)$. Explain how to estimate $\beta$ from the simulation. Why is this technique particularly effective in the Hull-White model?

??? success "Solution to Exercise 7"
    **Estimating $\beta$:** The optimal control variate coefficient is:

    $$
    \beta^* = \frac{\text{Cov}(\hat{V}, \hat{P}_{\text{MC}})}{\text{Var}(\hat{P}_{\text{MC}})}
    $$

    In practice, $\beta$ is estimated from the simulation itself:

    1. For each path $i$, compute both the discounted swaption payoff $V^{(i)}$ and the discounted ZCB payoff $P^{(i)} = \exp(-\sum_k r_{t_k}^{(i)}\Delta t)$.
    2. Compute the sample covariance and variance:

    $$
    \hat{\beta} = \frac{\sum_{i=1}^N (V^{(i)} - \bar{V})(P^{(i)} - \bar{P})}{\sum_{i=1}^N (P^{(i)} - \bar{P})^2}
    $$

    This is simply the OLS regression coefficient of $V$ on $P$.

    3. The adjusted estimator is:

    $$
    \hat{V}_{\text{cv}} = \bar{V} - \hat{\beta}(\bar{P} - P^M(0, T))
    $$

    **Why this is particularly effective in the Hull-White model:**

    1. **Exact control mean:** The Hull-White model provides the exact analytical ZCB price $P^M(0, T)$, so the control variate has a known expectation with no approximation error.
    2. **High correlation:** Both the swaption payoff and the ZCB price are driven by the same short-rate paths. A swap is essentially a portfolio of ZCBs, so the payoffs are highly correlated. The variance reduction factor is $1 - \rho^2$, where $\rho$ is the correlation between $V$ and $P$. For swaptions in the Hull-White model, $|\rho|$ is typically 0.8--0.95, giving variance reduction factors of 5--20.
    3. **No additional computation:** The ZCB payoff $1/M_T$ is already computed as part of the discounting step, so the control variate adds negligible computational cost.
