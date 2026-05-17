# Exact Simulation of Short Rate

Monte Carlo simulation of the Hull-White short rate requires generating values of $r(t + \Delta t)$ given $r(t)$. A naive Euler discretization introduces time-step bias that only vanishes as $\Delta t \to 0$. Because the Hull-White process is a linear SDE (Ornstein-Uhlenbeck with time-dependent drift), its transition distribution is exactly Gaussian, and we can sample $r(t + \Delta t)$ without any discretization error regardless of the step size $\Delta t$. This section derives the exact simulation formula and compares it with the Euler scheme.

## The Exact Transition Distribution

Recall (see [§ Hull-White Short Rate](../short_rate/short_rate_solution.md)): for $s \ge t$,

$$
r(s) = r(t)\,e^{-\lambda(s-t)} + \alpha(s) - \alpha(t)\,e^{-\lambda(s-t)} + \sigma\int_t^s e^{-\lambda(s-u)}\,dW^{\mathbb{Q}}(u)
$$

with $\alpha(s) = f^M(0,s) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda s})^2$. The stochastic integral is Gaussian with zero mean and known variance. Setting $s = t + \Delta t$:

!!! info "Theorem: Exact Simulation Formula"
    The short rate at time $t + \Delta t$ conditional on $r(t)$ is

    $$
    r(t + \Delta t) = r(t)\,e^{-\lambda\Delta t} + \alpha(t + \Delta t) - \alpha(t)\,e^{-\lambda\Delta t} + \sigma\sqrt{\frac{1 - e^{-2\lambda\Delta t}}{2\lambda}}\;Z
    $$

    where $Z \sim \mathcal{N}(0,1)$ is a standard normal random variable independent of $\mathcal{F}(t)$.

Equivalently, in terms of conditional moments:

$$\begin{array}{lllll}
\displaystyle
r(t + \Delta t)\,\Big|\,r(t)
&\sim&\displaystyle
\mathcal{N}\!\left(\mu(t, \Delta t),\; \sigma^2(t, \Delta t)\right)
\end{array}$$

where

$$\begin{array}{lllll}
\displaystyle
\mu(t, \Delta t)
&=&\displaystyle
r(t)\,e^{-\lambda\Delta t} + \alpha(t + \Delta t) - \alpha(t)\,e^{-\lambda\Delta t}
\\[8pt]
\displaystyle
\sigma^2(t, \Delta t)
&=&\displaystyle
\frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda\Delta t}\right)
\end{array}$$

???+ note "Proof"

    Recall (see [§ Hull-White Short Rate](../short_rate/short_rate_solution.md)) the integrating-factor solution gives

    $$
    r(t + \Delta t) = r(t)\,e^{-\lambda\Delta t} + \lambda\int_t^{t+\Delta t}\!\theta^{\mathbb{Q}}(s)e^{-\lambda(t+\Delta t - s)}ds + \sigma\!\int_t^{t+\Delta t}\!e^{-\lambda(t+\Delta t - s)}dW^{\mathbb{Q}}(s)
    $$

    The deterministic integral equals $\alpha(t + \Delta t) - \alpha(t)e^{-\lambda\Delta t}$. By Ito isometry, the stochastic integral has variance $\frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda\Delta t})$ and is Gaussian since the integrand is deterministic. $\square$

## The x(t) Decomposition for Simulation

Using the centered process $x(t) = r(t) - \alpha(t)$, the exact simulation becomes particularly clean because $x(t)$ follows a standard OU process with zero long-run mean:

$$
x(t + \Delta t) = x(t)\,e^{-\lambda\Delta t} + \sigma\sqrt{\frac{1 - e^{-2\lambda\Delta t}}{2\lambda}}\;Z
$$

The short rate is then recovered as $r(t + \Delta t) = x(t + \Delta t) + \alpha(t + \Delta t)$.

!!! tip "Implementation Advantage"
    Simulating $x(t)$ rather than $r(t)$ avoids evaluating $\alpha(t)$ at every intermediate time step during path generation. The function $\alpha$ is only needed when converting back to $r$ for bond price computations.

## Comparison with Euler Discretization

Recall (see [§ SDE Simulation](../../ch03/sde/sde_simulation.md)) the Euler-Maruyama discretization of $dr = \lambda(\theta^{\mathbb{Q}}(t) - r)\,dt + \sigma\,dW$:

$$
r(t + \Delta t) \approx r(t) + \lambda\!\left(\theta^{\mathbb{Q}}(t) - r(t)\right)\Delta t + \sigma\sqrt{\Delta t}\;Z
$$

The key differences from the exact scheme are:

| Property | Exact | Euler |
|:---|:---|:---|
| Mean | $r(t)e^{-\lambda\Delta t} + \alpha(t+\Delta t) - \alpha(t)e^{-\lambda\Delta t}$ | $r(t)(1 - \lambda\Delta t) + \lambda\theta^{\mathbb{Q}}(t)\Delta t$ |
| Variance | $\frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda\Delta t})$ | $\sigma^2\Delta t$ |
| Bias | None (exact) | $O(\Delta t)$ in mean, $O(\Delta t^2)$ in variance |
| Step-size dependence | None | Must use small $\Delta t$ for accuracy |

???+ note "Error Analysis"

    Expanding the exact mean to first order in $\Delta t$:

    $$\begin{array}{lllll}
    \displaystyle
    r(t)e^{-\lambda\Delta t}
    &\approx&\displaystyle
    r(t)(1 - \lambda\Delta t + \tfrac{1}{2}\lambda^2\Delta t^2 - \cdots)
    \end{array}$$

    The Euler scheme retains only the first two terms, introducing a bias of order $\frac{1}{2}\lambda^2 r(t)\Delta t^2$ in the mean. Similarly, the exact variance $\frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda\Delta t}) \approx \sigma^2\Delta t - \lambda\sigma^2\Delta t^2 + \cdots$ differs from the Euler variance $\sigma^2\Delta t$ by $O(\Delta t^2)$.

    For the integrated short rate $\int_0^T r(s)\,ds$ (needed for discounting), the Euler bias accumulates linearly with the number of steps, while the exact scheme has zero bias for any step size.

## Simulating the Discount Factor

For Monte Carlo pricing, we need the stochastic discount factor $M(T) = \exp(\int_0^T r(s)\,ds)$. With the exact scheme, the integral is approximated using the trapezoidal rule:

$$
\int_0^T r(s)\,ds \approx \sum_{i=0}^{N-1} \frac{r(t_i) + r(t_{i+1})}{2}\,\Delta t_i
$$

Although this introduces a small quadrature error, it is much smaller than the discretization bias of the Euler scheme. Alternatively, the exact conditional distribution of $\int_t^{t+\Delta t} r(s)\,ds$ given $(r(t), r(t+\Delta t))$ can be derived (it is Gaussian), enabling an even more accurate quadrature.

!!! info "Proposition: Conditional Integrated Rate"
    Given $r(t)$ and $r(t + \Delta t)$, the integral $\int_t^{t+\Delta t} r(s)\,ds$ conditional on $\{r(t), r(t+\Delta t)\}$ has the distribution

    $$
    \int_t^{t+\Delta t} r(s)\,ds \;\Big|\; r(t), r(t+\Delta t) \;\sim\; \mathcal{N}(\mu_I,\; \sigma_I^2)
    $$

    where the conditional mean and variance can be computed from the joint Gaussian distribution of $(r(t+\Delta t), \int_t^{t+\Delta t} r(s)\,ds)$ given $r(t)$.

## Complete Simulation Algorithm

!!! info "Algorithm: Exact Hull-White Path Simulation"
    **Input**: Parameters $\lambda$, $\sigma$, market curve $P^M(0,\cdot)$, initial rate $r_0$, time grid $0 = t_0 < t_1 < \cdots < t_N = T$, number of paths $M$.

    **For each path** $m = 1, \ldots, M$:

    1. Set $x_0 = r_0 - \alpha(0) = 0$ (since $\alpha(0) = f^M(0,0) = r_0$).
    2. For $i = 0, 1, \ldots, N-1$:
        - $\Delta t_i = t_{i+1} - t_i$
        - Draw $Z_i \sim \mathcal{N}(0,1)$
        - $x_{i+1} = x_i\,e^{-\lambda\Delta t_i} + \sigma\sqrt{\frac{1 - e^{-2\lambda\Delta t_i}}{2\lambda}}\,Z_i$
        - $r_{i+1} = x_{i+1} + \alpha(t_{i+1})$
    3. Compute discount factor: $M^{(m)}(T) = \exp\!\left(\sum_{i=0}^{N-1}\frac{r_i + r_{i+1}}{2}\Delta t_i\right)$

    **Output**: Paths $\{r^{(m)}(t_i)\}$ and discount factors $\{M^{(m)}(T)\}$.

```python
def simulate_hull_white_exact(hw, r0, T, n_steps, n_paths, seed=None):
    """Exact simulation of Hull-White short rate paths."""
    rng = np.random.default_rng(seed)
    dt = T / n_steps
    t_grid = np.linspace(0, T, n_steps + 1)

    # Precompute alpha values
    alpha = np.array([hw.alpha(t) for t in t_grid])

    # Precompute exact transition parameters
    decay = np.exp(-hw.lambd * dt)
    std = hw.sigma * np.sqrt((1 - np.exp(-2 * hw.lambd * dt))
                              / (2 * hw.lambd))

    # Simulate x process
    x = np.zeros((n_paths, n_steps + 1))
    Z = rng.standard_normal((n_paths, n_steps))

    for i in range(n_steps):
        x[:, i + 1] = x[:, i] * decay + std * Z[:, i]

    # Recover r = x + alpha
    r = x + alpha[np.newaxis, :]

    # Compute money market account via trapezoidal rule
    M = np.exp(np.cumsum(
        0.5 * (r[:, :-1] + r[:, 1:]) * dt, axis=1
    ))
    M = np.hstack([np.ones((n_paths, 1)), M])

    return t_grid, r, M
```

## Numerical Validation

The exact simulation can be validated by checking that Monte Carlo bond prices match the analytic formula. For $P(0, T)$:

$$
P^{\text{MC}}(0,T) = \frac{1}{M}\sum_{m=1}^{M} \frac{1}{M^{(m)}(T)}
$$

With exact simulation, this should converge to $P^M(0,T)$ as $M \to \infty$ for any step size $\Delta t$. With Euler discretization, convergence requires both $M \to \infty$ and $\Delta t \to 0$.

---

## Summary

The Hull-White short rate admits exact simulation because its transition distribution is Gaussian with known mean and variance. The exact formula $r(t+\Delta t) = r(t)e^{-\lambda\Delta t} + \alpha(t+\Delta t) - \alpha(t)e^{-\lambda\Delta t} + \sigma\sqrt{(1-e^{-2\lambda\Delta t})/(2\lambda)}\,Z$ eliminates all time-step bias, allowing the use of coarse time grids without sacrificing accuracy. The centered process $x(t) = r(t) - \alpha(t)$ simplifies the simulation further by removing the time-dependent drift. The exact scheme is strictly superior to Euler discretization for Hull-White Monte Carlo and should always be preferred.

---

## Exercises

**Exercise 1.** Verify the exact transition mean $\mu(t,\Delta t) = r(t)e^{-\lambda\Delta t} + \alpha(t+\Delta t) - \alpha(t)e^{-\lambda\Delta t}$ by expanding the Hull-White solution and using the identity $\alpha(s) - \alpha(t)e^{-\lambda(s-t)} = \lambda\int_t^s \theta^{\mathbb{Q}}(u)e^{-\lambda(s-u)}du$. Show that this reduces to the Euler mean $r(t)(1-\lambda\Delta t) + \lambda\theta^{\mathbb{Q}}(t)\Delta t$ to first order in $\Delta t$.

??? success "Solution to Exercise 1"
    The Hull-White solution at time $s = t + \Delta t$ given $r(t)$ is

    $$
    r(t+\Delta t) = r(t)\,e^{-\lambda\Delta t} + \lambda\int_t^{t+\Delta t}\theta^{\mathbb{Q}}(s)\,e^{-\lambda(t+\Delta t - s)}\,ds + \sigma\int_t^{t+\Delta t} e^{-\lambda(t+\Delta t - s)}\,dW^{\mathbb{Q}}(s)
    $$

    Using the identity $\alpha(s) = f^M(0,s) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda s})^2$ and $\lambda\int_t^s \theta^{\mathbb{Q}}(u)e^{-\lambda(s-u)}\,du = \alpha(s) - \alpha(t)e^{-\lambda(s-t)}$, the deterministic integral evaluates to

    $$
    \alpha(t+\Delta t) - \alpha(t)\,e^{-\lambda\Delta t}
    $$

    Taking expectations (the stochastic integral has zero mean):

    $$
    \mu(t,\Delta t) = \mathbb{E}[r(t+\Delta t) \mid r(t)] = r(t)\,e^{-\lambda\Delta t} + \alpha(t+\Delta t) - \alpha(t)\,e^{-\lambda\Delta t}
    $$

    **Reduction to Euler mean:** Expanding to first order in $\Delta t$:

    $$
    r(t)\,e^{-\lambda\Delta t} \approx r(t)(1 - \lambda\Delta t)
    $$

    $$
    \alpha(t+\Delta t) - \alpha(t)\,e^{-\lambda\Delta t} \approx \alpha(t+\Delta t) - \alpha(t)(1 - \lambda\Delta t) \approx \alpha'(t)\Delta t + \lambda\alpha(t)\Delta t
    $$

    Since $\theta^{\mathbb{Q}}(t) = \alpha'(t)/\lambda + \alpha(t)$ (from the relation between $\theta^{\mathbb{Q}}$ and $\alpha$), we get

    $$
    \mu(t,\Delta t) \approx r(t)(1 - \lambda\Delta t) + \lambda\theta^{\mathbb{Q}}(t)\Delta t
    $$

    which is the Euler mean.

---

**Exercise 2.** The exact transition variance is $\frac{\sigma^2}{2\lambda}(1-e^{-2\lambda\Delta t})$, while the Euler variance is $\sigma^2\Delta t$. Show that the relative error of the Euler variance is approximately $\lambda\Delta t$ for small $\Delta t$. For $\lambda = 0.05$ and $\Delta t = 1$ year, compute the percentage error in the Euler variance.

??? success "Solution to Exercise 2"
    The exact variance is $V_{\text{exact}} = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda\Delta t})$. Expanding the exponential:

    $$
    1 - e^{-2\lambda\Delta t} = 2\lambda\Delta t - 2\lambda^2\Delta t^2 + \frac{4\lambda^3\Delta t^3}{3} - \cdots
    $$

    Therefore

    $$
    V_{\text{exact}} = \frac{\sigma^2}{2\lambda}(2\lambda\Delta t - 2\lambda^2\Delta t^2 + \cdots) = \sigma^2\Delta t - \lambda\sigma^2\Delta t^2 + \cdots
    $$

    The Euler variance is $V_{\text{Euler}} = \sigma^2\Delta t$. The absolute error is

    $$
    V_{\text{Euler}} - V_{\text{exact}} = \lambda\sigma^2\Delta t^2 + O(\Delta t^3)
    $$

    The relative error is

    $$
    \frac{V_{\text{Euler}} - V_{\text{exact}}}{V_{\text{exact}}} \approx \frac{\lambda\sigma^2\Delta t^2}{\sigma^2\Delta t} = \lambda\Delta t
    $$

    For $\lambda = 0.05$ and $\Delta t = 1$ year:

    $$
    \text{Relative error} \approx 0.05 \times 1 = 0.05 = 5\%
    $$

    The Euler scheme overestimates the transition variance by approximately 5% with annual time steps and this mean-reversion speed.

---

**Exercise 3.** Explain why simulating the centered process $x(t) = r(t) - \alpha(t)$ is computationally advantageous over simulating $r(t)$ directly. What quantity must be precomputed before simulation, and at what cost?

??? success "Solution to Exercise 3"
    Simulating $x(t) = r(t) - \alpha(t)$ is computationally advantageous because:

    1. **Simpler transition formula:** The centered process follows $x(t+\Delta t) = x(t)\,e^{-\lambda\Delta t} + \sigma\sqrt{(1-e^{-2\lambda\Delta t})/(2\lambda)}\,Z$, which has no time-dependent drift. The transition coefficients $e^{-\lambda\Delta t}$ and $\sigma\sqrt{(1-e^{-2\lambda\Delta t})/(2\lambda)}$ are constants that can be precomputed once.

    2. **Avoid evaluating $\alpha(t)$ at intermediate steps:** During path generation, we only update $x$ using the simple OU recursion. The function $\alpha(t)$ needs to be evaluated only when we need the short rate $r(t_i) = x(t_i) + \alpha(t_i)$, typically at dates where bond prices or payoffs are required.

    **What must be precomputed:** The values $\alpha(t_i)$ for all time steps $t_i$ where the short rate is needed. This requires evaluating

    $$
    \alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2
    $$

    at each required time step. The cost is $O(N)$ evaluations of $\alpha$, performed once before the simulation begins, and stored in an array. The transition parameters ($e^{-\lambda\Delta t}$ and the standard deviation) are computed once as scalars.

---

**Exercise 4.** The money market account is approximated by the trapezoidal rule $\int_0^T r(s)ds \approx \sum_{i=0}^{N-1}\frac{r(t_i)+r(t_{i+1})}{2}\Delta t_i$. What is the order of accuracy of this quadrature for smooth functions? How does this quadrature error compare to the discretization bias of the Euler scheme?

??? success "Solution to Exercise 4"
    The trapezoidal rule has order of accuracy $O(\Delta t^2)$ for smooth functions (it is exact for linear functions and has error proportional to the second derivative of the integrand times $\Delta t^2$).

    More precisely, for a smooth function $f$ on $[a, b]$ with $N$ subintervals of width $h = (b-a)/N$:

    $$
    \left|\int_a^b f(s)\,ds - \sum_{i=0}^{N-1}\frac{f(t_i) + f(t_{i+1})}{2}h\right| \leq \frac{(b-a)h^2}{12}\max|f''|
    $$

    For the integrated short rate $\int_0^T r(s)\,ds$, the trapezoidal error is $O(\Delta t^2)$ per subinterval, or $O(\Delta t^2)$ globally (since there are $N = T/\Delta t$ subintervals, each contributing $O(\Delta t^3)$ error, summing to $O(\Delta t^2)$ total).

    **Comparison with Euler bias:** The Euler discretization introduces an $O(\Delta t)$ bias in the transition mean per time step. Over $N = T/\Delta t$ steps, this accumulates to $O(1)$ bias in the integrated rate (the bias does not vanish as $\Delta t$ changes because the number of steps compensates). More precisely, the Euler bias in $\int_0^T r(s)\,ds$ is $O(\Delta t)$.

    Therefore, the trapezoidal quadrature error $O(\Delta t^2)$ is strictly smaller than the Euler discretization bias $O(\Delta t)$, confirming that the quadrature is not the bottleneck when using exact simulation.

---

**Exercise 5.** For $\lambda = 0.05$, $\sigma = 0.01$, and $r_0 = 0.03$ with a flat market curve $P^M(0,T) = e^{-0.03T}$, compute $\alpha(1)$ and the exact transition parameters $\mu(0,1)$ and $\sigma^2(0,1)$. Generate one sample of $r(1)$ using a standard normal draw $Z = 0.5$.

??? success "Solution to Exercise 5"
    With $\lambda = 0.05$, $\sigma = 0.01$, $r_0 = 0.03$, and flat market curve $P^M(0,T) = e^{-0.03T}$:

    The instantaneous forward rate is $f^M(0,t) = 0.03$ (constant for a flat curve).

    **Computing $\alpha(1)$:**

    $$
    \alpha(1) = f^M(0,1) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda})^2 = 0.03 + \frac{(0.01)^2}{2(0.05)^2}(1 - e^{-0.05})^2
    $$

    $$
    = 0.03 + \frac{0.0001}{0.005}(1 - 0.95123)^2 = 0.03 + 0.02 \times (0.04877)^2
    $$

    $$
    = 0.03 + 0.02 \times 0.002379 = 0.03 + 0.00004758 \approx 0.030048
    $$

    **Transition mean:**

    $$
    \mu(0,1) = r_0\,e^{-\lambda} + \alpha(1) - \alpha(0)\,e^{-\lambda}
    $$

    Since $\alpha(0) = f^M(0,0) + 0 = 0.03$:

    $$
    \mu(0,1) = 0.03 \times e^{-0.05} + 0.030048 - 0.03 \times e^{-0.05} = 0.030048
    $$

    **Transition variance:**

    $$
    \sigma^2(0,1) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda}) = \frac{0.0001}{0.1}(1 - e^{-0.1}) = 0.001 \times 0.09516 = 0.00009516
    $$

    So $\sigma(0,1) = \sqrt{0.00009516} \approx 0.009755$.

    **Sample of $r(1)$ with $Z = 0.5$:**

    $$
    r(1) = \mu(0,1) + \sigma(0,1) \times Z = 0.030048 + 0.009755 \times 0.5 \approx 0.030048 + 0.004878 = 0.034926
    $$

---

**Exercise 6.** The Monte Carlo bond price estimator $\hat{P}(0,T) = \frac{1}{M}\sum_{m=1}^M 1/M^{(m)}(T)$ should converge to $P^M(0,T)$ for any step size with exact simulation. Explain why this does not hold for the Euler scheme and quantify the bias as a function of $\Delta t$.

??? success "Solution to Exercise 6"
    With exact simulation, the conditional distribution $r(t+\Delta t) \mid r(t)$ is exactly Gaussian with the correct mean and variance. Therefore, the simulated paths have the exact law of the continuous-time process at the grid points (the joint distribution of $(r(t_0), r(t_1), \ldots, r(t_N))$ is exact). The only approximation is in the quadrature of $\int_0^T r(s)\,ds$, which introduces an $O(\Delta t^2)$ error that vanishes as $\Delta t \to 0$ but does not bias the estimator systematically for fixed $\Delta t$ (it introduces variance, not bias, when using the trapezoidal rule symmetrically).

    With the Euler scheme, the conditional distribution of $r(t+\Delta t) \mid r(t)$ is Gaussian but with the wrong mean and variance (both off by $O(\Delta t)$ terms). This means the simulated paths do not have the correct law, even at the grid points. Consequently:

    $$
    \mathbb{E}_{\text{Euler}}\!\left[\frac{1}{M(T)}\right] \neq P^M(0, T)
    $$

    for any finite $\Delta t$. The bias is

    $$
    \text{Bias} = \mathbb{E}_{\text{Euler}}\!\left[\frac{1}{M(T)}\right] - P^M(0,T) = O(\Delta t)
    $$

    This $O(\Delta t)$ bias arises from the accumulated errors in the transition mean (each step contributes $O(\Delta t^2)$ bias, and there are $T/\Delta t$ steps, giving $O(\Delta t)$ total). The bias only vanishes as $\Delta t \to 0$, requiring both more paths and finer time steps for convergence.

---

**Exercise 7.** The exact simulation formula involves $\sqrt{(1-e^{-2\lambda\Delta t})/(2\lambda)}$. What happens numerically when $\lambda$ is very small (e.g., $\lambda = 10^{-8}$)? Describe a numerically stable implementation that avoids cancellation error, using a Taylor expansion of $1 - e^{-2\lambda\Delta t}$.

??? success "Solution to Exercise 7"
    The expression $\frac{1 - e^{-2\lambda\Delta t}}{2\lambda}$ involves a difference of two nearly equal numbers when $\lambda$ is very small. For $\lambda = 10^{-8}$ and $\Delta t = 1$:

    $$
    e^{-2\lambda\Delta t} = e^{-2 \times 10^{-8}} \approx 1 - 2 \times 10^{-8} + 2 \times 10^{-16} - \cdots
    $$

    So $1 - e^{-2\lambda\Delta t} \approx 2 \times 10^{-8}$, and dividing by $2\lambda = 2 \times 10^{-8}$ gives approximately $1$. However, in floating-point arithmetic, $e^{-2 \times 10^{-8}}$ is computed as $1 - 2 \times 10^{-8} + \ldots$, and the subtraction $1 - e^{-2\lambda\Delta t}$ loses about 8 digits of precision due to catastrophic cancellation. The subsequent division by the small number $2\lambda$ amplifies the error.

    **Numerically stable implementation:** Use the Taylor expansion

    $$
    \frac{1 - e^{-2\lambda\Delta t}}{2\lambda} = \Delta t - \lambda\Delta t^2 + \frac{2\lambda^2\Delta t^3}{3} - \frac{2\lambda^3\Delta t^4}{3} + \cdots
    $$

    For small $\lambda\Delta t$, truncate after sufficiently many terms:

    $$
    \frac{1 - e^{-2\lambda\Delta t}}{2\lambda} \approx \Delta t\left(1 - \lambda\Delta t + \frac{2(\lambda\Delta t)^2}{3} - \frac{(\lambda\Delta t)^3}{3} + \cdots\right)
    $$

    In code, switch to the Taylor expansion when $\lambda\Delta t < \epsilon$ for some threshold (e.g., $\epsilon = 10^{-4}$):

    ```python
    def stable_variance_factor(lambd, dt):
        x = lambd * dt
        if x < 1e-4:
            return dt * (1 - x + 2*x**2/3 - x**3/3)
        else:
            return (1 - np.exp(-2 * x)) / (2 * lambd)
    ```

    The standard deviation is then $\sigma\sqrt{\text{stable\_variance\_factor}(\lambda, \Delta t)}$. In the limit $\lambda \to 0$, this correctly gives $\sigma\sqrt{\Delta t}$, which is the Brownian motion case (no mean reversion).
