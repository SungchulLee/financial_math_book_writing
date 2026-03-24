# Exact Simulation of Short Rate

Monte Carlo simulation of the Hull-White short rate requires generating values of $r(t + \Delta t)$ given $r(t)$. A naive Euler discretization introduces time-step bias that only vanishes as $\Delta t \to 0$. Because the Hull-White process is a linear SDE (Ornstein-Uhlenbeck with time-dependent drift), its transition distribution is exactly Gaussian, and we can sample $r(t + \Delta t)$ without any discretization error regardless of the step size $\Delta t$. This section derives the exact simulation formula and compares it with the Euler scheme.

## The Exact Transition Distribution

Recall the Hull-White short rate solution: for $s \ge t$,

$$
r(s) = r(t)\,e^{-\lambda(s-t)} + \alpha(s) - \alpha(t)\,e^{-\lambda(s-t)} + \sigma\int_t^s e^{-\lambda(s-u)}\,dW^{\mathbb{Q}}(u)
$$

where $\alpha(s) = f^M(0,s) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda s})^2$. The stochastic integral is Gaussian with zero mean and known variance. Setting $s = t + \Delta t$:

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

    From the general solution of the Hull-White SDE using the integrating factor $e^{\lambda t}$:

    $$\begin{array}{lllll}
    \displaystyle
    r(t + \Delta t)
    &=&\displaystyle
    r(t)\,e^{-\lambda\Delta t} + \lambda\int_t^{t+\Delta t} \theta^{\mathbb{Q}}(s)\,e^{-\lambda(t+\Delta t - s)}\,ds + \sigma\int_t^{t+\Delta t} e^{-\lambda(t+\Delta t - s)}\,dW^{\mathbb{Q}}(s)
    \end{array}$$

    The deterministic integral evaluates to $\alpha(t + \Delta t) - \alpha(t)e^{-\lambda\Delta t}$ using the identity $\alpha(s) = f^M(0,s) + \frac{\sigma^2}{2\lambda^2}(1-e^{-\lambda s})^2$ and the relation $\lambda\int_t^s \theta^{\mathbb{Q}}(u)e^{-\lambda(s-u)}du = \alpha(s) - \alpha(t)e^{-\lambda(s-t)}$.

    The stochastic integral has variance

    $$
    \sigma^2\int_t^{t+\Delta t} e^{-2\lambda(t+\Delta t - s)}\,ds = \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda\Delta t}\right)
    $$

    by the Ito isometry. Since the integrand is deterministic, the stochastic integral is Gaussian, giving the stated transition distribution. $\square$

## The x(t) Decomposition for Simulation

Using the centered process $x(t) = r(t) - \alpha(t)$, the exact simulation becomes particularly clean because $x(t)$ follows a standard OU process with zero long-run mean:

$$
x(t + \Delta t) = x(t)\,e^{-\lambda\Delta t} + \sigma\sqrt{\frac{1 - e^{-2\lambda\Delta t}}{2\lambda}}\;Z
$$

The short rate is then recovered as $r(t + \Delta t) = x(t + \Delta t) + \alpha(t + \Delta t)$.

!!! tip "Implementation Advantage"
    Simulating $x(t)$ rather than $r(t)$ avoids evaluating $\alpha(t)$ at every intermediate time step during path generation. The function $\alpha$ is only needed when converting back to $r$ for bond price computations.

## Comparison with Euler Discretization

The Euler-Maruyama discretization of $dr = \lambda(\theta^{\mathbb{Q}}(t) - r)\,dt + \sigma\,dW$ reads

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

---

**Exercise 2.** The exact transition variance is $\frac{\sigma^2}{2\lambda}(1-e^{-2\lambda\Delta t})$, while the Euler variance is $\sigma^2\Delta t$. Show that the relative error of the Euler variance is approximately $\lambda\Delta t$ for small $\Delta t$. For $\lambda = 0.05$ and $\Delta t = 1$ year, compute the percentage error in the Euler variance.

---

**Exercise 3.** Explain why simulating the centered process $x(t) = r(t) - \alpha(t)$ is computationally advantageous over simulating $r(t)$ directly. What quantity must be precomputed before simulation, and at what cost?

---

**Exercise 4.** The money market account is approximated by the trapezoidal rule $\int_0^T r(s)ds \approx \sum_{i=0}^{N-1}\frac{r(t_i)+r(t_{i+1})}{2}\Delta t_i$. What is the order of accuracy of this quadrature for smooth functions? How does this quadrature error compare to the discretization bias of the Euler scheme?

---

**Exercise 5.** For $\lambda = 0.05$, $\sigma = 0.01$, and $r_0 = 0.03$ with a flat market curve $P^M(0,T) = e^{-0.03T}$, compute $\alpha(1)$ and the exact transition parameters $\mu(0,1)$ and $\sigma^2(0,1)$. Generate one sample of $r(1)$ using a standard normal draw $Z = 0.5$.

---

**Exercise 6.** The Monte Carlo bond price estimator $\hat{P}(0,T) = \frac{1}{M}\sum_{m=1}^M 1/M^{(m)}(T)$ should converge to $P^M(0,T)$ for any step size with exact simulation. Explain why this does not hold for the Euler scheme and quantify the bias as a function of $\Delta t$.

---

**Exercise 7.** The exact simulation formula involves $\sqrt{(1-e^{-2\lambda\Delta t})/(2\lambda)}$. What happens numerically when $\lambda$ is very small (e.g., $\lambda = 10^{-8}$)? Describe a numerically stable implementation that avoids cancellation error, using a Taylor expansion of $1 - e^{-2\lambda\Delta t}$.
