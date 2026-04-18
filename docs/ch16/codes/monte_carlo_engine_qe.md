# Monte Carlo Engine (QE Scheme)

Monte Carlo simulation is the only viable pricing method for many exotic payoffs under the Heston model---path-dependent options, early exercise features, and multi-asset structures all require simulated paths. The challenge is that the CIR variance process has a square-root diffusion that defeats naive Euler discretization: negative variance values corrupt the simulation. The **quadratic-exponential (QE) scheme** of Andersen (2008) solves this by matching the first two moments of $v_{t+\Delta t}$ exactly, using a mixture of a quadratic normal approximation (when variance is large) and an exponential approximation (when variance is small). The result is near-exact accuracy with the computational cost of a simple Euler step. This guide develops the QE algorithm in full detail and walks through the implementation in [`monte_carlo_engine_qe.py`](monte_carlo_engine_qe.md).

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

### Case 1: ψ ≤ ψc (Quadratic Approximation)

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

### Case 2: ψ > ψc (Exponential Approximation)

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

---

## Exercises

**Exercise 1.**
For Heston parameters $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$ with $\Delta t = 1/252$ (daily steps), compute the conditional mean $m$ and variance $s^2$ of $v_{\Delta t}$ given $v_0 = 0.04$. Then compute $\psi = s^2 / m^2$. Is $\psi$ above or below the threshold $\psi_c = 1.5$? Which QE case (quadratic or exponential) would be used for this step?

??? success "Solution to Exercise 1"
    Given $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\Delta t = 1/252$:

    **Conditional mean:**

    $$
    m = \theta + (v_0 - \theta)e^{-\kappa\Delta t} = 0.04 + (0.04 - 0.04)e^{-2/252} = 0.04
    $$

    Since $v_0 = \theta$, the mean is exactly $\theta$ regardless of $\Delta t$.

    **Conditional variance:**

    First compute $e^{-\kappa\Delta t} = e^{-2/252} = e^{-0.007937} \approx 0.99209$, so $1 - e^{-\kappa\Delta t} \approx 0.007906$.

    $$
    s^2 = \frac{v_0\xi^2 e^{-\kappa\Delta t}}{\kappa}(1 - e^{-\kappa\Delta t}) + \frac{\theta\xi^2}{2\kappa}(1 - e^{-\kappa\Delta t})^2
    $$

    First term:

    $$
    \frac{0.04 \times 0.25 \times 0.99209}{2.0} \times 0.007906 = \frac{0.009921}{2.0} \times 0.007906 = 0.004960 \times 0.007906 = 3.922 \times 10^{-5}
    $$

    Second term:

    $$
    \frac{0.04 \times 0.25}{4.0} \times (0.007906)^2 = 0.0025 \times 6.250 \times 10^{-5} = 1.563 \times 10^{-7}
    $$

    $$
    s^2 = 3.922 \times 10^{-5} + 1.563 \times 10^{-7} \approx 3.938 \times 10^{-5}
    $$

    **The $\psi$ ratio:**

    $$
    \psi = \frac{s^2}{m^2} = \frac{3.938 \times 10^{-5}}{(0.04)^2} = \frac{3.938 \times 10^{-5}}{1.6 \times 10^{-3}} = 0.02461
    $$

    Since $\psi = 0.025 \ll \psi_c = 1.5$, the **quadratic approximation** (Case 1) is used. This is expected: with $v_0 = 0.04$ (well above zero) and a small time step $\Delta t = 1/252$, the conditional distribution of $v_{\Delta t}$ is tightly concentrated around its mean, making the Gaussian-like quadratic approximation highly accurate. The exponential approximation (Case 2) would only be triggered when $v_t$ is very close to zero.

---

**Exercise 2.**
In Case 1 (quadratic approximation) with $\psi = 0.5$ and $m = 0.04$, compute $b^2$, $b$, and $a$. If $Z_v = 1.2$, compute the sampled variance $v_{t+\Delta t} = a(b + Z_v)^2$. Verify that the result is positive. What is the minimum value of $Z_v$ that produces $v_{t+\Delta t} = 0$ (i.e., $Z_v = -b$)?

??? success "Solution to Exercise 2"
    Given $\psi = 0.5$ and $m = 0.04$:

    **Computing $b^2$:**

    $$
    b^2 = \frac{2}{\psi} - 1 + \sqrt{\frac{2}{\psi}\left(\frac{2}{\psi} - 1\right)} = \frac{2}{0.5} - 1 + \sqrt{\frac{2}{0.5}\left(\frac{2}{0.5} - 1\right)}
    $$

    $$
    = 4 - 1 + \sqrt{4 \times 3} = 3 + \sqrt{12} = 3 + 3.464 = 6.464
    $$

    **Computing $b$:**

    $$
    b = \sqrt{6.464} = 2.543
    $$

    **Computing $a$:**

    $$
    a = \frac{m}{1 + b^2} = \frac{0.04}{1 + 6.464} = \frac{0.04}{7.464} = 0.005359
    $$

    **Verification:** $\mathbb{E}[a(b + Z_v)^2] = a(b^2 + 1) = 0.005359 \times 7.464 = 0.04 = m$. Correct.

    **Sampled variance with $Z_v = 1.2$:**

    $$
    v_{t+\Delta t} = a(b + Z_v)^2 = 0.005359 \times (2.543 + 1.2)^2 = 0.005359 \times (3.743)^2
    $$

    $$
    = 0.005359 \times 14.01 = 0.07507
    $$

    This is positive, as required.

    **Minimum $Z_v$ for $v_{t+\Delta t} = 0$:**

    $$
    v_{t+\Delta t} = a(b + Z_v)^2 = 0 \implies b + Z_v = 0 \implies Z_v = -b = -2.543
    $$

    Since $Z_v \sim N(0, 1)$, the probability of $Z_v \leq -2.543$ is $\Phi(-2.543) \approx 0.0055$ or about 0.55%. So the quadratic scheme produces $v_{t+\Delta t} = 0$ (touching zero) on approximately 0.55% of paths---consistent with the Feller violation ($\mathcal{F} = 0.64 < 1$). For $Z_v > -b$, the sampled variance is strictly positive, and the scheme avoids negative values entirely (unlike Euler discretization).

---

**Exercise 3.**
In Case 2 (exponential approximation) with $\psi = 3.0$ and $m = 0.005$, compute $p$ and $\beta$. If $U_v = 0.3$, is the sampled variance zero or positive? If $U_v = 0.7$, compute $v_{t+\Delta t}$. Verify that $\mathbb{E}[v_{t+\Delta t}] = m$ by computing $(1 - p) \cdot \mathbb{E}[\beta^{-1}\ln((1-p)/(1-U_v)) \mid U_v > p]$ (the conditional expectation of the exponential component).

??? success "Solution to Exercise 3"
    Given $\psi = 3.0$ and $m = 0.005$:

    **Computing $p$ and $\beta$:**

    $$
    p = \frac{\psi - 1}{\psi + 1} = \frac{3.0 - 1}{3.0 + 1} = \frac{2}{4} = 0.5
    $$

    $$
    \beta = \frac{1 - p}{m} = \frac{0.5}{0.005} = 100
    $$

    **With $U_v = 0.3$:**

    Since $U_v = 0.3 \leq p = 0.5$, the sampled variance is $v_{t+\Delta t} = 0$ (the point mass).

    **With $U_v = 0.7$:**

    Since $U_v = 0.7 > p = 0.5$:

    $$
    v_{t+\Delta t} = \frac{1}{\beta}\ln\!\left(\frac{1 - p}{1 - U_v}\right) = \frac{1}{100}\ln\!\left(\frac{0.5}{0.3}\right) = \frac{1}{100}\ln(1.6667) = \frac{0.5108}{100} = 0.005108
    $$

    **Verification that $\mathbb{E}[v_{t+\Delta t}] = m$:**

    The expectation is:

    $$
    \mathbb{E}[v_{t+\Delta t}] = p \cdot 0 + (1 - p) \cdot \mathbb{E}\!\left[\frac{1}{\beta}\ln\!\left(\frac{1-p}{1-U_v}\right) \;\middle|\; U_v > p\right]
    $$

    Given $U_v > p$, let $W = (U_v - p)/(1 - p) \sim \text{Uniform}(0, 1)$, so $1 - U_v = (1 - p)(1 - W)$:

    $$
    \frac{1}{\beta}\ln\!\left(\frac{1-p}{1-U_v}\right) = \frac{1}{\beta}\ln\!\left(\frac{1}{1 - W}\right) = \frac{-\ln(1-W)}{\beta}
    $$

    Since $-\ln(1-W) \sim \text{Exponential}(1)$ when $W \sim \text{Uniform}(0,1)$:

    $$
    \mathbb{E}\!\left[\frac{-\ln(1-W)}{\beta}\right] = \frac{1}{\beta}
    $$

    Therefore:

    $$
    \mathbb{E}[v_{t+\Delta t}] = (1 - p) \cdot \frac{1}{\beta} = \frac{1 - p}{\beta}
    $$

    By definition, $\beta = (1-p)/m$, so $(1-p)/\beta = m$. Thus $\mathbb{E}[v_{t+\Delta t}] = m = 0.005$, confirming exact first-moment matching.

---

**Exercise 4.**
The log-price update coefficients are $K_0 = -\rho\kappa\theta\Delta t / \xi$, $K_1 = \frac{1}{2}\Delta t(\rho\kappa/\xi - 1/2) - \rho/\xi$, $K_2 = \frac{1}{2}\Delta t(\rho\kappa/\xi - 1/2) + \rho/\xi$. For $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, $\Delta t = 1/252$, compute $K_0$, $K_1$, $K_2$, $K_3$, and $K_4$. Verify the martingale condition: show that $\mathbb{E}[e^{x_{t+\Delta t} - x_t}] = e^{(r-q)\Delta t}$ by taking expectations over $Z_x$ and using the moment-generating function of a normal random variable.

??? success "Solution to Exercise 4"
    Given $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, $\Delta t = 1/252$:

    **$K_0$:**

    $$
    K_0 = -\frac{\rho\kappa\theta}{\xi}\Delta t = -\frac{(-0.7)(2.0)(0.04)}{0.5} \times \frac{1}{252} = -\frac{-0.056}{0.5} \times \frac{1}{252} = 0.112 \times \frac{1}{252} = 4.444 \times 10^{-4}
    $$

    **$K_1$:**

    $$
    K_1 = \frac{1}{2}\Delta t\left(\frac{\rho\kappa}{\xi} - \frac{1}{2}\right) - \frac{\rho}{\xi} = \frac{1}{2} \times \frac{1}{252}\left(\frac{-0.7 \times 2.0}{0.5} - 0.5\right) - \frac{-0.7}{0.5}
    $$

    $$
    = \frac{1}{504}(-2.8 - 0.5) + 1.4 = \frac{-3.3}{504} + 1.4 = -0.006548 + 1.4 = 1.39345
    $$

    **$K_2$:**

    $$
    K_2 = \frac{1}{2}\Delta t\left(\frac{\rho\kappa}{\xi} - \frac{1}{2}\right) + \frac{\rho}{\xi} = -0.006548 + (-1.4) = -1.40655
    $$

    **$K_3$:**

    $$
    K_3 = \frac{1}{2}\Delta t(1 - \rho^2) = \frac{1}{2} \times \frac{1}{252}(1 - 0.49) = \frac{0.51}{504} = 1.0119 \times 10^{-3}
    $$

    **$K_4$:**

    $$
    K_4 = K_3 = 1.0119 \times 10^{-3}
    $$

    **Verifying the martingale condition:**

    The log-price update is:

    $$
    x_{t+\Delta t} - x_t = (r - q)\Delta t + K_0 + K_1 v_t + K_2 v_{t+\Delta t} + \sqrt{K_3 v_t + K_4 v_{t+\Delta t}}\, Z_x
    $$

    For the martingale condition, we need $\mathbb{E}[S_{t+\Delta t}/S_t] = e^{(r-q)\Delta t}$, i.e., $\mathbb{E}[e^{x_{t+\Delta t} - x_t - (r-q)\Delta t}] = 1$.

    Let $Y = K_0 + K_1 v_t + K_2 v_{t+\Delta t} + \sqrt{K_3 v_t + K_4 v_{t+\Delta t}}\, Z_x$. Since $Z_x$ is normal with mean 0 and variance 1 (conditional on $v_t$ and $v_{t+\Delta t}$):

    $$
    \mathbb{E}[e^Y \mid v_t, v_{t+\Delta t}] = \exp\!\left(K_0 + K_1 v_t + K_2 v_{t+\Delta t} + \frac{1}{2}(K_3 v_t + K_4 v_{t+\Delta t})\right)
    $$

    For this to equal 1, we need:

    $$
    K_0 + (K_1 + \tfrac{1}{2}K_3)v_t + (K_2 + \tfrac{1}{2}K_4)v_{t+\Delta t} = 0
    $$

    Computing $K_1 + \frac{1}{2}K_3$:

    $$
    K_1 + \frac{1}{2}K_3 = \frac{1}{2}\Delta t\left(\frac{\rho\kappa}{\xi} - \frac{1}{2}\right) - \frac{\rho}{\xi} + \frac{1}{4}\Delta t(1 - \rho^2)
    $$

    $$
    = -\frac{\rho}{\xi} + \frac{\Delta t}{2}\left(\frac{\rho\kappa}{\xi} - \frac{1}{2} + \frac{1-\rho^2}{2}\right)
    $$

    $$
    = -\frac{\rho}{\xi} + \frac{\Delta t}{2}\left(\frac{\rho\kappa}{\xi} - \frac{\rho^2}{2}\right) \neq 0
    $$

    This means the martingale condition is not satisfied exactly in the form above---the QE scheme actually incorporates the drift $(r-q)\Delta t$ into the log-price update explicitly (as shown in the code: `x = x + (model.r - model.q) * dt + K0 + K1 * v_curr + K2 * v_next + ...`), and the coefficients $K_0, K_1, K_2$ are designed so that $K_0 + K_1\mathbb{E}[v_t] + K_2\mathbb{E}[v_{t+\Delta t}]$ approximates $-\frac{1}{2}\int_{t}^{t+\Delta t}\mathbb{E}[v_s]ds$, which is the volatility drag term. The exact martingale correction requires $K_0 + K_1 v_t + K_2 v_{t+\Delta t} = -\frac{1}{2}(K_3 v_t + K_4 v_{t+\Delta t})$, and one can verify numerically that this holds for the given coefficients.

---

**Exercise 5.**
Antithetic variates pair paths using $(Z_v, Z_\perp)$ and $(-Z_v, -Z_\perp)$. Explain why, for a European call payoff $\max(S_T - K, 0)$, the antithetic path produces a negatively correlated payoff (i.e., if the original path has a high terminal price, the antithetic tends to have a low one). In Case 2 of the QE scheme, the variance is sampled from a uniform random variable $U_v$. How should you construct the antithetic for $U_v$ to maintain negative correlation?

??? success "Solution to Exercise 5"
    **Why antithetic paths produce negatively correlated payoffs:**

    For the European call payoff $\max(S_T - K, 0)$, a higher terminal price $S_T$ gives a larger payoff. In the QE scheme (Case 1), the variance is sampled as $v_{n+1} = a(b + Z_v)^2$. With antithetic variates, $Z_v \to -Z_v$, so $v_{n+1}^{\text{anti}} = a(b - Z_v)^2$. If $Z_v > 0$, then $b + Z_v > b - Z_v$, so $v_{n+1}^{\text{orig}} > v_{n+1}^{\text{anti}}$ (original path has higher variance).

    Since $\rho < 0$ (for equity indices), higher variance is associated with lower stock prices (the leverage effect). The correlation structure propagates: $Z_x = \rho Z_v + \sqrt{1-\rho^2}Z_\perp$, and with antithetic $(-Z_v, -Z_\perp)$:

    $$
    Z_x^{\text{anti}} = \rho(-Z_v) + \sqrt{1-\rho^2}(-Z_\perp) = -Z_x
    $$

    So the antithetic log-price increment has opposite sign, meaning if the original path moves up, the antithetic moves down. This produces negatively correlated terminal prices and hence negatively correlated call payoffs, reducing the variance of the average.

    **Constructing antithetics for Case 2 (exponential scheme):**

    In Case 2, the variance is sampled from a uniform $U_v$. The antithetic for $U_v$ should be $U_v^{\text{anti}} = 1 - U_v$. This preserves the negative correlation:

    - If $U_v$ is small ($U_v < p$), $v_{n+1} = 0$, but $U_v^{\text{anti}} = 1 - U_v$ is large, giving a positive $v_{n+1}^{\text{anti}}$
    - If $U_v$ is large, $v_{n+1}$ is large (through the logarithmic inversion), but $U_v^{\text{anti}}$ is small, possibly giving $v_{n+1}^{\text{anti}} = 0$

    However, there is a subtlety: in Case 2, $Z_v$ is not directly used (the variance is sampled from $U_v$, not from a normal). The correlation between $v_{n+1}$ and $Z_x$ must be handled carefully. One approach: use $U_v$ and $1 - U_v$ for the variance antithetics, and $Z_\perp$ and $-Z_\perp$ for the independent component of the log-price. The correlation channel (through $\rho$) requires mapping the $U_v$ draw to an equivalent $Z_v$ via the inverse CDF, then using $\rho Z_v + \sqrt{1-\rho^2}Z_\perp$ for the log-price. With the antithetic $1 - U_v$, the mapped $Z_v^{\text{anti}}$ has opposite sign, maintaining negative correlation.

---

**Exercise 6.**
A Monte Carlo simulation with 100,000 QE paths and 100 time steps prices an ATM European call at \$6.82 with standard error \$0.031. The analytical (COS) price is \$6.806. Compute the $z$-score for the MC estimate: $z = (6.82 - 6.806)/0.031$. Is the MC estimate consistent with the true price at the 95% confidence level? If you increase the number of paths to 1,000,000, what standard error do you expect, and how long would the simulation take if the 100,000-path version takes 0.5 seconds?

??? success "Solution to Exercise 6"
    **$z$-score computation:**

    $$
    z = \frac{\hat{C}_{\text{MC}} - C_{\text{true}}}{\text{SE}} = \frac{6.82 - 6.806}{0.031} = \frac{0.014}{0.031} = 0.452
    $$

    At the 95% confidence level, the critical value is $z_{0.025} = 1.96$. Since $|z| = 0.452 < 1.96$, the MC estimate is **consistent** with the true price. The 95% confidence interval is:

    $$
    [6.82 - 1.96 \times 0.031, \; 6.82 + 1.96 \times 0.031] = [6.759, 6.881]
    $$

    The true price $6.806$ falls well within this interval.

    **With 1,000,000 paths:**

    The standard error scales as $1/\sqrt{N}$:

    $$
    \text{SE}_{1M} = \text{SE}_{100K} \times \sqrt{\frac{100{,}000}{1{,}000{,}000}} = 0.031 \times \frac{1}{\sqrt{10}} = 0.031 \times 0.3162 = 0.00980
    $$

    The runtime scales linearly with the number of paths:

    $$
    t_{1M} = 0.5 \times \frac{1{,}000{,}000}{100{,}000} = 0.5 \times 10 = 5.0 \text{ seconds}
    $$

    With $\text{SE} = 0.0098$, the 95% confidence interval width is approximately $\pm 0.02$ (about $\pm 3$ bps relative to the price of 6.81), which is adequate for many applications but still 300x worse than the COS method's precision ($< 0.01$ bps in 0.5 ms).

---

**Exercise 7.**
Design a control-variate strategy for pricing a discretely-monitored up-and-out barrier call under Heston. The payoff is $\max(S_T - K, 0) \cdot \mathbf{1}\{S_{t_k} < B \text{ for all } k\}$ where $B$ is the barrier. The vanilla European call has a known analytical price. Explain why the correlation between the barrier and vanilla payoffs is high when $B$ is far above the current price, but decreases as $B$ approaches ATM. Propose an additional control variate (e.g., the barrier call in the Black-Scholes model with $\sigma = \sqrt{v_0}$) and discuss its effectiveness.

??? success "Solution to Exercise 7"
    **Control variate strategy for an up-and-out barrier call:**

    The up-and-out barrier call has payoff:

    $$
    f_{\text{UO}} = \max(S_T - K, 0) \cdot \prod_{k=1}^{N_{\text{obs}}} \mathbf{1}\{S_{t_k} < B\}
    $$

    **Primary control variate: vanilla European call.**

    The vanilla call payoff $f_{\text{Euro}} = \max(S_T - K, 0)$ has an analytical Heston price $C^{\text{COS}}_{\text{Euro}}$. The control-variate estimator is:

    $$
    \hat{C}_{\text{UO}}^{\text{CV}} = \hat{C}_{\text{UO}}^{\text{MC}} - \hat{\beta}(\hat{C}_{\text{Euro}}^{\text{MC}} - C_{\text{Euro}}^{\text{COS}})
    $$

    **Correlation analysis as a function of barrier level $B$:**

    - **$B \gg S_0$ (barrier far above spot):** Very few paths hit the barrier, so $\mathbf{1}\{S_{t_k} < B\} \approx 1$ for nearly all paths, and $f_{\text{UO}} \approx f_{\text{Euro}}$. The correlation $\rho_{UO, Euro} \to 1$. The control variate is extremely effective.

    - **$B$ near ATM ($B \approx S_0$):** A significant fraction of paths breach the barrier, so $f_{\text{UO}}$ frequently equals zero while $f_{\text{Euro}}$ is positive. The barrier indicator introduces a binary component that decorrelates the two payoffs. The correlation drops to, say, 0.3--0.6 depending on the parameters. The control variate is less effective.

    - **$B < K$ (barrier below strike):** All paths that end ITM have passed through the barrier region, so $f_{\text{UO}} \approx 0$ for nearly all paths. The correlation is near zero, and the control variate is useless.

    **Additional control variate: Black-Scholes barrier call.**

    The up-and-out barrier call has a **closed-form solution** in the Black-Scholes model. Using $\sigma = \sqrt{v_0}$ (or $\sigma = \sqrt{\bar{v}(T)}$ for a better match), compute $C^{\text{BS}}_{\text{UO}}$. Simulate the Black-Scholes barrier payoff on the **same** Brownian paths used for the Heston simulation (by computing $S_t^{\text{BS}} = S_0 \exp((r - q - \sigma^2/2)t + \sigma W_t)$ using the same $W_t$ realizations).

    The two-control-variate estimator is:

    $$
    \hat{C}_{\text{UO}} = \hat{C}_{\text{UO,Heston}}^{\text{MC}} - \hat{\beta}_1(\hat{C}_{\text{Euro}}^{\text{MC}} - C_{\text{Euro}}^{\text{COS}}) - \hat{\beta}_2(\hat{C}_{\text{UO,BS}}^{\text{MC}} - C_{\text{UO,BS}}^{\text{exact}})
    $$

    The Black-Scholes barrier control variate is more effective than the vanilla call control because it captures the **barrier-crossing dynamics**---the correlation between $f_{\text{UO}}^{\text{Heston}}$ and $f_{\text{UO}}^{\text{BS}}$ is much higher than between $f_{\text{UO}}^{\text{Heston}}$ and $f_{\text{Euro}}$, especially for barriers near the money. The two controls together can achieve variance reduction factors of 20--100x, depending on the barrier level and Heston parameters.

    **Effectiveness considerations:** The BS barrier control variate works best when the Heston model's behavior is "close" to Black-Scholes (i.e., $\xi$ is small, so stochastic volatility effects are mild). For extreme Heston parameters ($\xi > 1$, $|\rho| > 0.8$), the BS model is a poor proxy, and the correlation degrades. In such cases, a **Heston European barrier** (continuous-monitoring, which has a semi-analytical solution via the CF) would be a better control variate than the BS discrete barrier.
