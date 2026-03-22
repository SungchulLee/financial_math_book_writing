# Monte Carlo Engine (QE Scheme)

Monte Carlo simulation is the only viable pricing method for many exotic payoffs under the Heston model---path-dependent options, early exercise features, and multi-asset structures all require simulated paths. The challenge is that the CIR variance process has a square-root diffusion that defeats naive Euler discretization: negative variance values corrupt the simulation. The **quadratic-exponential (QE) scheme** of Andersen (2008) solves this by matching the first two moments of $v_{t+\Delta t}$ exactly, using a mixture of a quadratic normal approximation (when variance is large) and an exponential approximation (when variance is small). The result is near-exact accuracy with the computational cost of a simple Euler step. This guide develops the QE algorithm in full detail and walks through the implementation in [`monte_carlo_engine_qe.py`](monte_carlo_engine_qe.py).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the conditional mean and variance of $v_{t+\Delta t}$ given $v_t$ under the CIR process
    2. Implement the QE scheme with the psi-based switching criterion between quadratic and exponential approximations
    3. Construct the log-price update using the martingale correction
    4. Generate full Heston paths and price European and path-dependent options

!!! tip "Prerequisites"
    This section builds on the [Euler discretization and pitfalls](../monte_carlo/euler_discretization_and_pitfalls.md), the [QE scheme theory](../monte_carlo/quadratic_exponential_scheme.md), and the [`HestonModel` class](heston_model_class.md).

---

## Conditional Moments of the CIR Process

The variance process $v_t$ follows:

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi\sqrt{v_t} \, dW_t^{(2)}
$$

Given $v_t$, the conditional distribution of $v_{t+\Delta t}$ is non-central chi-squared. Its first two moments are:

$$
m = \mathbb{E}[v_{t+\Delta t} | v_t] = \theta + (v_t - \theta)e^{-\kappa\Delta t}
$$

$$
s^2 = \text{Var}[v_{t+\Delta t} | v_t] = \frac{v_t \xi^2 e^{-\kappa\Delta t}}{\kappa}(1 - e^{-\kappa\Delta t}) + \frac{\theta\xi^2}{2\kappa}(1 - e^{-\kappa\Delta t})^2
$$

The key ratio that determines the shape of the conditional distribution is:

$$
\psi = \frac{s^2}{m^2}
$$

When $\psi$ is small (large $v_t$), the distribution is approximately Gaussian. When $\psi$ is large (small $v_t$ near zero), the distribution has a point mass at zero and an exponential tail.

---

## The QE Algorithm

The QE scheme samples $v_{t+\Delta t}$ by matching these two moments using one of two approximations, selected by comparing $\psi$ to a threshold $\psi_c$ (typically $\psi_c = 1.5$).

### Case 1: $\psi \leq \psi_c$ (Quadratic Approximation)

When $\psi$ is small, the conditional distribution is approximately normal and the variance is far from zero. Use a **quadratic** transformation of a standard normal:

$$
v_{t+\Delta t} = a(b + Z_v)^2
$$

where $Z_v \sim N(0, 1)$ and the parameters $a$ and $b$ are chosen to match $m$ and $s^2$:

$$
b^2 = \frac{2}{\psi} - 1 + \sqrt{\frac{2}{\psi}\left(\frac{2}{\psi} - 1\right)} = \frac{2}{\psi} - 1 + \sqrt{\frac{2}{\psi}} \cdot \sqrt{\frac{2}{\psi} - 1}
$$

$$
a = \frac{m}{1 + b^2}
$$

The condition $\psi \leq \psi_c$ with $\psi_c \leq 2$ ensures $b^2 \geq 0$, so the square root is real. The sampled $v_{t+\Delta t} = a(b + Z_v)^2 \geq 0$ is guaranteed non-negative.

!!! note "Moment Matching Verification"
    With $Z_v \sim N(0,1)$: $\mathbb{E}[a(b + Z_v)^2] = a(b^2 + 1) = m$ and $\text{Var}[a(b + Z_v)^2] = 2a^2(b^2 + 1)^2\psi/(2) = s^2$. The first two moments match exactly by construction.

### Case 2: $\psi > \psi_c$ (Exponential Approximation)

When $\psi$ is large, the variance is near zero and the conditional distribution has a significant point mass at zero. Use an **exponential** distribution mixed with a point mass:

$$
v_{t+\Delta t} = \begin{cases} 0 & \text{with probability } p \\ \beta^{-1} \ln\!\left(\frac{1 - p}{1 - U_v}\right) & \text{with probability } 1 - p \end{cases}
$$

where $U_v \sim \text{Uniform}(0, 1)$ and:

$$
p = \frac{\psi - 1}{\psi + 1}, \qquad \beta = \frac{1 - p}{m} = \frac{2}{m(\psi + 1)}
$$

In practice, this is implemented as:

$$
v_{t+\Delta t} = \begin{cases} 0 & \text{if } U_v \leq p \\ \beta^{-1} \ln\!\left(\frac{1 - p}{1 - U_v}\right) & \text{if } U_v > p \end{cases}
$$

### Switching Threshold

The threshold $\psi_c = 1.5$ is Andersen's recommended default. Values between 1.0 and 2.0 work well. The constraint $\psi_c \leq 2$ ensures $b^2 \geq 0$ in Case 1.

---

## Log-Price Update

Given $v_t$ and the sampled $v_{t+\Delta t}$, the log-price $x_t = \ln S_t$ is updated using:

$$
x_{t+\Delta t} = x_t + K_0 + K_1 v_t + K_2 v_{t+\Delta t} + \sqrt{K_3 v_t + K_4 v_{t+\Delta t}} \, Z_x
$$

where $Z_x \sim N(0, 1)$ is correlated with the variance innovation: $Z_x = \rho Z_v + \sqrt{1 - \rho^2} Z_\perp$ with $Z_\perp \sim N(0, 1)$ independent. The coefficients are:

$$
K_0 = -\frac{\rho\kappa\theta}{\xi}\Delta t
$$

$$
K_1 = \frac{1}{2}\Delta t\left(\frac{\rho\kappa}{\xi} - \frac{1}{2}\right) - \frac{\rho}{\xi}
$$

$$
K_2 = \frac{1}{2}\Delta t\left(\frac{\rho\kappa}{\xi} - \frac{1}{2}\right) + \frac{\rho}{\xi}
$$

$$
K_3 = \frac{1}{2}\Delta t(1 - \rho^2)
$$

$$
K_4 = \frac{1}{2}\Delta t(1 - \rho^2)
$$

!!! warning "Martingale Correction"
    The coefficients $K_0, K_1, K_2$ include the drift $(r - q)\Delta t$ implicitly through the martingale condition. The exact form ensures that $\mathbb{E}[S_{t+\Delta t}/S_t] = e^{(r-q)\Delta t}$, preserving the risk-neutral drift. Using the "wrong" drift formula (e.g., adding $(r - q - v_t/2)\Delta t$ directly) introduces discretization bias.

---

## Full Path Generation

### Algorithm Summary

For each path $\omega$ and each time step $n = 0, 1, \ldots, N_t - 1$:

1. Compute $m$, $s^2$, and $\psi = s^2 / m^2$ from $v_n$
2. If $\psi \leq \psi_c$: sample $Z_v \sim N(0,1)$, set $v_{n+1} = a(b + Z_v)^2$
3. If $\psi > \psi_c$: sample $U_v \sim U(0,1)$, set $v_{n+1}$ from the exponential scheme
4. Sample $Z_\perp \sim N(0,1)$, compute $Z_x = \rho Z_v + \sqrt{1 - \rho^2} Z_\perp$ (Case 1) or generate $Z_x$ independently (Case 2)
5. Update $x_{n+1} = x_n + K_0 + K_1 v_n + K_2 v_{n+1} + \sqrt{K_3 v_n + K_4 v_{n+1}} Z_x$

### Implementation

```python
def heston_qe_paths(model, T, N_t, N_paths, seed=None):
    """
    Generate Heston paths using the QE scheme.

    Parameters
    ----------
    model : HestonModel
    T : float
        Maturity
    N_t : int
        Number of time steps
    N_paths : int
        Number of paths
    seed : int, optional

    Returns
    -------
    S : ndarray, shape (N_paths, N_t + 1)
        Spot price paths
    v : ndarray, shape (N_paths, N_t + 1)
        Variance paths
    """
    rng = np.random.default_rng(seed)
    dt = T / N_t
    psi_c = 1.5

    # Precompute constants
    exp_kdt = np.exp(-model.kappa * dt)
    K0 = -(model.rho * model.kappa * model.theta / model.xi) * dt
    K1 = 0.5 * dt * (model.rho * model.kappa / model.xi - 0.5) \
         - model.rho / model.xi
    K2 = 0.5 * dt * (model.rho * model.kappa / model.xi - 0.5) \
         + model.rho / model.xi
    K3 = 0.5 * dt * (1 - model.rho**2)
    K4 = 0.5 * dt * (1 - model.rho**2)

    # Initialize arrays
    x = np.full(N_paths, np.log(model.S0))
    v_curr = np.full(N_paths, model.v0)

    S = np.zeros((N_paths, N_t + 1))
    v_out = np.zeros((N_paths, N_t + 1))
    S[:, 0] = model.S0
    v_out[:, 0] = model.v0

    for n in range(N_t):
        # Conditional moments
        m = model.theta + (v_curr - model.theta) * exp_kdt
        m = np.maximum(m, 1e-8)
        s2 = (v_curr * model.xi**2 * exp_kdt / model.kappa
              * (1 - exp_kdt)
              + model.theta * model.xi**2 / (2 * model.kappa)
              * (1 - exp_kdt)**2)
        psi = s2 / m**2

        # Sample v_{n+1}
        v_next = np.zeros(N_paths)
        Zv = np.zeros(N_paths)

        # Case 1: psi <= psi_c (quadratic)
        mask1 = psi <= psi_c
        if np.any(mask1):
            b2 = 2 / psi[mask1] - 1 + np.sqrt(
                2 / psi[mask1] * (2 / psi[mask1] - 1))
            b_val = np.sqrt(np.maximum(b2, 0))
            a_val = m[mask1] / (1 + b2)
            Zv[mask1] = rng.standard_normal(np.sum(mask1))
            v_next[mask1] = a_val * (b_val + Zv[mask1])**2

        # Case 2: psi > psi_c (exponential)
        mask2 = ~mask1
        if np.any(mask2):
            p = (psi[mask2] - 1) / (psi[mask2] + 1)
            beta = (1 - p) / m[mask2]
            Uv = rng.uniform(size=np.sum(mask2))
            v_next[mask2] = np.where(
                Uv <= p, 0,
                np.log((1 - p) / np.maximum(1 - Uv, 1e-15)) / beta)

        v_next = np.maximum(v_next, 0)

        # Log-price update
        Zperp = rng.standard_normal(N_paths)
        Zx = model.rho * Zv + np.sqrt(1 - model.rho**2) * Zperp
        x = (x + (model.r - model.q) * dt + K0
             + K1 * v_curr + K2 * v_next
             + np.sqrt(np.maximum(K3 * v_curr + K4 * v_next, 0)) * Zx)

        v_curr = v_next
        S[:, n + 1] = np.exp(x)
        v_out[:, n + 1] = v_curr

    return S, v_out
```

---

## Pricing European Options

Given simulated paths, the European call price is:

$$
\hat{C} = e^{-rT} \frac{1}{N_{\text{paths}}} \sum_{i=1}^{N_{\text{paths}}} \max(S_T^{(i)} - K, 0)
$$

with standard error:

$$
\text{SE} = \frac{\hat{\sigma}_{\text{payoff}}}{\sqrt{N_{\text{paths}}}}
$$

```python
def mc_european_call(model, K, T, N_t=100, N_paths=100_000, seed=42):
    S, _ = heston_qe_paths(model, T, N_t, N_paths, seed)
    payoff = np.maximum(S[:, -1] - K, 0)
    price = np.exp(-model.r * T) * np.mean(payoff)
    se = np.exp(-model.r * T) * np.std(payoff) / np.sqrt(N_paths)
    return price, se
```

---

## Variance Reduction

### Antithetic Variates

Generate paths in pairs using $(Z_v, Z_\perp)$ and $(-Z_v, -Z_\perp)$. The payoff estimator becomes:

$$
\hat{C}_{\text{anti}} = e^{-rT} \frac{1}{N_{\text{paths}}} \sum_{i=1}^{N_{\text{paths}}/2} \frac{f(S_T^{(i,+)}) + f(S_T^{(i,-)})}{2}
$$

This reduces variance by a factor of 2--4 for European options due to the negative correlation between the two paths.

### Control Variates

Use the analytical European call price $C^{\text{Fourier}}$ (from the COS or Gil-Pelaez engine) as a control variate:

$$
\hat{C}_{\text{cv}} = \hat{C}_{\text{MC}} - \beta\left(\hat{C}_{\text{MC,European}} - C^{\text{Fourier}}\right)
$$

where $\beta$ is the optimal regression coefficient. This is especially powerful for exotic options whose payoff is correlated with the European payoff.

---

## Summary

The QE scheme provides near-exact simulation of the Heston variance process by matching conditional moments through a psi-based switching rule: the quadratic approximation $v = a(b + Z)^2$ when variance is large ($\psi \leq 1.5$), and the exponential approximation when variance is near zero ($\psi > 1.5$). The log-price update uses precomputed coefficients $K_0, \ldots, K_4$ that automatically enforce the martingale condition. Combined with antithetic variates and control variates, the QE-based Monte Carlo engine achieves pricing accuracy comparable to Fourier methods for European options while extending naturally to path-dependent and exotic payoffs.
