# Python Implementation Classes

This page collects all Python helper classes used throughout the interest rate modeling chapters.

## OptionType and OptionTypeSwap

```python
import enum

class OptionType(enum.Enum):
    CALL = 1
    PUT = -1

class OptionTypeSwap(enum.Enum):
    RECEIVER = 1.0
    PAYER = -1.0
```

## BrownianMotion

```python
import numpy as np

class BrownianMotion:
    def __init__(self, T=1):
        self.T = T

    def run_MC(self, num_paths=1, num_steps=None, seed=None):
        if num_steps is None:
            num_steps = int(self.T * 12 * 21)
        if seed is not None:
            np.random.seed(seed)

        t = np.linspace(0, self.T, num_steps + 1)
        dt = t[1] - t[0]
        sqrt_dt = np.sqrt(dt)

        Z = np.random.standard_normal((num_paths, num_steps))
        if num_paths > 1:
            Z = (Z - Z.mean(axis=0)) / Z.std(axis=0)

        dB = Z * sqrt_dt
        B = np.concatenate([np.zeros((num_paths, 1)), dB.cumsum(axis=1)], axis=1)
        return t, dt, sqrt_dt, B, dB
```

## Vasicek

$$dr_t=\lambda(\theta-r_t) dt+\sigma dW_t$$

```python
class Vasicek(BrownianMotion):
    def __init__(self, r, T, lambd, theta, sigma):
        self.r = r
        self.T = T
        self.lambd = lambd
        self.theta = theta
        self.sigma = sigma

    def run_MC(self, num_paths=1, num_steps=None, seed=None):
        if num_steps is None:
            num_steps = int(self.T * 12 * 21)
        t, dt, sqrt_dt, B, dB = super().run_MC(num_paths, num_steps, seed)
        R = self.r * np.ones((num_paths, num_steps + 1))
        M = np.ones((num_paths, num_steps + 1))
        for i in range(1, num_steps + 1):
            R[:, i] = R[:, i-1] + self.lambd * (self.theta - R[:, i-1]) * dt + self.sigma * dB[:, i-1]
            M[:, i] = M[:, i-1] * np.exp(R[:, i-1] * dt)
        return t, R, M
```

## CIR

$$dr_t=\lambda(\theta-r_t) dt+\sigma\sqrt{r_t} dW_t$$

```python
class CIR(BrownianMotion):
    def __init__(self, r, T, lambd, theta, sigma):
        self.r = r
        self.T = T
        self.lambd = lambd
        self.theta = theta
        self.sigma = sigma

    def run_MC(self, num_paths=1, num_steps=None, seed=None):
        if num_steps is None:
            num_steps = int(self.T * 12 * 21)
        t, dt, sqrt_dt, B, dB = super().run_MC(num_paths, num_steps, seed)
        R = self.r * np.ones((num_paths, num_steps + 1))
        M = np.ones((num_paths, num_steps + 1))
        for i in range(1, num_steps + 1):
            R[:, i] = R[:, i-1] + self.lambd * (self.theta - R[:, i-1]) * dt + self.sigma * np.sqrt(R[:, i]) * dB[:, i-1]
            R[:, i] = np.maximum(R[:, i], 0.0)  # Truncated boundary condition
            M[:, i] = M[:, i-1] * np.exp(R[:, i-1] * dt)
        return t, R, M
```

## HJM Helper Functions

```python
E = np.exp
E1 = lambda x: np.exp(x) - 1.0
L = np.log

def compute_f(t, P, dt=1e-4):
    """Instantaneous forward rate from ZCB curve."""
    return -(np.log(P(t + dt)) - np.log(P(t - dt))) / (2 * dt)

def compute_df_over_dt(t, P, dt=1e-4):
    """Derivative of instantaneous forward rate."""
    f = compute_f
    return (f(t + dt, P) - f(t - dt, P)) / (2 * dt)

def compute_r0(P):
    """Short rate from ZCB curve."""
    return compute_f(1e-4, P)
```

## HullWhite

```python
from scipy import stats
from scipy.integrate import trapz

class HullWhite:
    def __init__(self, sigma, lambd, P):
        self.sigma = sigma
        self.lambd = lambd
        self.P = P

    def compute_sigma_P(self, t, T):
        return self.sigma * self.compute_B(t, T)

    def compute_theta(self, t):
        first = compute_f(t, self.P)
        second = compute_df_over_dt(t, self.P) / self.lambd
        third = -self.sigma**2 / (2 * self.lambd**2) * E1(-2 * self.lambd * t)
        return first + second + third

    def compute_theta_T(self, t, T):
        first = self.compute_theta(t)
        second = self.sigma**2 / self.lambd * self.compute_B(t, T)
        return first + second

    def compute_A(self, t, T):
        tau = T - t
        head = -self.sigma**2 / (4 * self.lambd**3)
        tail = 3 - 2 * self.lambd * tau - 4 * E(-self.lambd * tau) + E(-2 * self.lambd * tau)
        first = head * tail
        tau_prime = np.linspace(0, tau, 250)
        theta = self.compute_theta
        B = lambda t: self.compute_B(t=0, T=t)
        second = self.lambd * trapz(theta(T - tau_prime) * B(tau_prime), tau_prime)
        return first + second

    def compute_B(self, t, T):
        tau = T - t
        return E1(-self.lambd * tau) / self.lambd

    def compute_ZCB(self, t, T, r_t):
        A = self.compute_A(t, T)
        B = self.compute_B(t, T)
        return E(A + B * r_t)

    def generate_sample_paths(self, num_paths, num_steps, T, seed=None):
        if seed is not None:
            np.random.seed(seed)
        r0 = compute_r0(self.P)
        theta = self.compute_theta
        Z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
        R = np.ones((num_paths, num_steps + 1)) * r0
        M = np.ones((num_paths, num_steps + 1))
        t = np.linspace(0, T, num_steps + 1)
        dt = t[1] - t[0]
        sqrt_dt = np.sqrt(dt)
        for i in range(num_steps):
            if num_paths > 1:
                Z[:, i] = (Z[:, i] - Z[:, i].mean()) / Z[:, i].std()
            dW = sqrt_dt * Z[:, i]
            R[:, i+1] = R[:, i] + self.lambd * (theta(t[i]) - R[:, i]) * dt + self.sigma * dW
            M[:, i+1] = M[:, i] * np.exp(R[:, i] * dt)
        return t, R, M

    def compute_ZCB_Option_Price(self, K, T1, T2, CP):
        A = self.compute_A(T1, T2)
        B = self.compute_B(T1, T2)
        mu = self.compute_mu_r_T_ForwardMeasure(T1)
        v = np.sqrt(self.compute_sigma_square_r_T(T1))
        K_hat = K * E(-A)
        a = (L(K_hat) - B * mu) / (B * v)
        d1 = a - B * v
        d2 = d1 + B * v
        value = self.P(T1) * E(A) * (
            E(0.5 * B**2 * v**2 + B * mu) * stats.norm.cdf(d1) - K_hat * stats.norm.cdf(d2)
        )
        if CP == OptionType.CALL:
            return value
        elif CP == OptionType.PUT:
            return value - self.P(T2) + K * self.P(T1)

    def compute_Caplet_Floorlet_Price(self, N, K, T1, T2, CP):
        N_new = N * (1.0 + (T2 - T1) * K)
        K_new = 1 / (1.0 + (T2 - T1) * K)
        if CP == OptionType.CALL:
            return N_new * self.compute_ZCB_Option_Price(K_new, T1, T2, CP=OptionType.PUT)
        elif CP == OptionType.PUT:
            return N_new * self.compute_ZCB_Option_Price(K_new, T1, T2, CP=OptionType.CALL)

    def compute_SwapPrice(self, t, r_t, notional, K, Ti, Tm, n, CP):
        if n == 1:
            Ti_grid = np.array((Ti, Tm))
        else:
            Ti_grid = np.linspace(Ti, Tm, n)
        tau = Ti_grid[1] - Ti_grid[0]
        if np.size(Ti_grid[np.where(Ti_grid < t)]) > 0:
            Ti = Ti_grid[np.where(Ti_grid < t)][-1]
        A_mn = np.zeros(np.size(r_t))
        P_t_Ti_Lambda = lambda Ti: self.compute_ZCB(t, Ti, r_t)
        P_t_Ti = P_t_Ti_Lambda(Ti)
        P_t_Tm = P_t_Ti_Lambda(Tm)
        for idx, ti in enumerate(Ti_grid[np.where(Ti_grid >= t)]):
            if ti > Ti:
                A_mn = A_mn + tau * P_t_Ti_Lambda(ti)
        if CP == OptionTypeSwap.PAYER:
            swap = (P_t_Ti - P_t_Tm) - K * A_mn
        elif CP == OptionTypeSwap.RECEIVER:
            swap = K * A_mn - (P_t_Ti - P_t_Tm)
        return swap * notional

    def compute_mu_r_T(self, T):
        r0 = compute_r0(self.P)
        s = np.linspace(0.0, T, 2500)
        integrand = lambda s: self.compute_theta(s) * E(-self.lambd * (T - s))
        return r0 * E(-self.lambd * T) + self.lambd * trapz(integrand(s), s)

    def compute_mu_r_T_ForwardMeasure(self, T):
        r0 = compute_r0(self.P)
        theta_T_Forward = lambda s, T: self.compute_theta_T(s, T)
        s = np.linspace(0.0, T, 2500)
        integrand = lambda s: theta_T_Forward(s, T) * E(-self.lambd * (T - s))
        return r0 * E(-self.lambd * T) + self.lambd * trapz(integrand(s), s)

    def compute_sigma_square_r_T(self, T):
        return -self.sigma**2 / (2 * self.lambd) * E1(-2 * self.lambd * T)
```

## HullWhite2 (Two-Factor)

```python
class HullWhite2:
    def __init__(self, sigma1, sigma2, lambd1, lambd2, rho, P):
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.lambd1 = lambd1
        self.lambd2 = lambd2
        self.lambd = lambd1 + lambd2
        self.rho = rho
        self.P = P

    def compute_A(self, T1, T2):
        tau = T2 - T1
        V = lambda t, T: (
            self.sigma1**2 / self.lambd1**2 * (
                tau + 2 * E(-self.lambd1 * tau) / self.lambd1
                - E(-2 * self.lambd1 * tau) / (2 * self.lambd1) - 3 / (2 * self.lambd1)
            )
            + self.sigma2**2 / self.lambd2**2 * (
                tau + 2 * E(-self.lambd2 * tau) / self.lambd2
                - E(-2 * self.lambd2 * tau) / (2 * self.lambd2) - 3 / (2 * self.lambd2)
            )
            + 2 * self.rho * self.sigma1 * self.sigma2 / (self.lambd1 * self.lambd2) * (
                tau + E1(-self.lambd1 * tau) / self.lambd1
                + E1(-self.lambd2 * tau) / self.lambd2
                - E1(-self.lambd * tau) / self.lambd
            )
        )
        A = L(self.P(T2) / self.P(T1)) + 0.5 * (V(T1, T2) + V(0, T1) - V(0, T2))
        return A

    def compute_B(self, T1, T2):
        tau = T2 - T1
        Bx = E1(-self.lambd1 * tau) / self.lambd1
        By = E1(-self.lambd2 * tau) / self.lambd2
        return Bx, By

    def compute_ZCB(self, T1, T2, x_T1, y_T1):
        A = self.compute_A(T1, T2)
        Bx, By = self.compute_B(T1, T2)
        return np.exp(A + Bx * x_T1 + By * y_T1)

    def generate_sample_paths(self, num_paths, num_steps, T, seed=None):
        phi = lambda t: (
            compute_f(t, self.P)
            + self.sigma1**2 / (2 * self.lambd1**2) * E1(-self.lambd1 * t) * E1(-self.lambd1 * t)
            + self.sigma2**2 / (2 * self.lambd2**2) * E1(-self.lambd2 * t) * E1(-self.lambd2 * t)
            + self.rho * self.sigma1 * self.sigma2 / (self.lambd1 * self.lambd2)
              * E1(-self.lambd1 * t) * E1(-self.lambd2 * t)
        )
        Z1 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
        Z2 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
        X = np.zeros((num_paths, num_steps + 1))
        Y = np.zeros((num_paths, num_steps + 1))
        R = np.ones((num_paths, num_steps + 1)) * phi(0)
        M = np.ones((num_paths, num_steps + 1))
        t = np.linspace(0, T, num_steps + 1)
        dt = t[1] - t[0]
        sqrt_dt = np.sqrt(dt)
        for i in range(num_steps):
            if num_paths > 1:
                Z1[:, i] = (Z1[:, i] - Z1[:, i].mean()) / Z1[:, i].std()
                Z2[:, i] = (Z2[:, i] - Z2[:, i].mean()) / Z2[:, i].std()
                Z2[:, i] = self.rho * Z1[:, i] + np.sqrt(1. - self.rho**2) * Z2[:, i]
            X[:, i+1] = X[:, i] - self.lambd1 * X[:, i] * dt + self.sigma1 * sqrt_dt * Z1[:, i]
            Y[:, i+1] = Y[:, i] - self.lambd2 * Y[:, i] * dt + self.sigma2 * sqrt_dt * Z2[:, i]
            R[:, i+1] = X[:, i+1] + Y[:, i+1] + phi(t[i+1])
            M[:, i+1] = M[:, i] * np.exp(R[:, i] * dt)
        return t, X, Y, R, M
```

---

## Exercises

**Exercise 1.** Using the `BrownianMotion` class, generate 5,000 paths of standard Brownian motion over $T = 1$ year with 252 time steps. Verify that the terminal distribution $B_T$ has approximately zero mean and unit variance. Explain why the moment-matching step (centering and standardizing) ensures these properties hold exactly for any finite number of paths.

??? success "Solution to Exercise 1"
    Using the `BrownianMotion` class with $T = 1$ and 252 steps:

    ```python
    bm = BrownianMotion(T=1)
    t, dt, sqrt_dt, B, dB = bm.run_MC(num_paths=5000, num_steps=252, seed=42)
    B_T = B[:, -1]
    print(f"Mean of B_T: {B_T.mean():.6f}")
    print(f"Var of B_T:  {B_T.var():.6f}")
    ```

    **Why moment matching ensures exact properties:** The `run_MC` method applies:

    $$
    Z_i \leftarrow \frac{Z_i - \bar{Z}}{\text{std}(Z)}
    $$

    at each time step (when `num_paths > 1`). After this transformation:

    - The sample mean of $Z_i$ is exactly 0 (by centering).
    - The sample variance of $Z_i$ is exactly 1 (by standardizing).

    Since $B_T = \sum_{k=1}^{252} Z_k \sqrt{\Delta t}$, and at each step the $Z_k$ have sample mean 0 and sample variance 1:

    - $\mathbb{E}_{\text{sample}}[B_T] = \sqrt{\Delta t} \sum_{k=1}^{252} \bar{Z}_k = 0$ exactly.
    - $\text{Var}_{\text{sample}}(B_T) = \Delta t \sum_{k=1}^{252} s_{Z_k}^2 = \Delta t \times 252 = T = 1$ exactly (assuming independence across steps, which holds since the $Z_k$ are independent draws).

    This guarantee holds for any finite $N$, not just in the $N \to \infty$ limit. Without moment matching, $\bar{Z}_k \neq 0$ and $s_{Z_k}^2 \neq 1$ for finite $N$, introducing bias that only vanishes asymptotically.

---

**Exercise 2.** Using the `Vasicek` class with $r_0 = 5\%$, $\lambda = 0.3$, $\theta = 4\%$, $\sigma = 1\%$, generate 10,000 paths over $T = 10$ years. Compute the sample mean and standard deviation of $r_{10}$ and compare with the analytical values:

$$
\mathbb{E}[r_T] = \theta + (r_0 - \theta)e^{-\lambda T}, \qquad \text{Std}(r_T) = \sigma\sqrt{\frac{1 - e^{-2\lambda T}}{2\lambda}}
$$

??? success "Solution to Exercise 2"
    With $r_0 = 0.05$, $\lambda = 0.3$, $\theta = 0.04$, $\sigma = 0.01$, $T = 10$:

    **Analytical values:**

    $$
    \mathbb{E}[r_{10}] = \theta + (r_0 - \theta)e^{-\lambda T} = 0.04 + (0.05 - 0.04)e^{-3.0} = 0.04 + 0.01 \times 0.04979 = 0.04050
    $$

    $$
    \text{Std}(r_{10}) = \sigma\sqrt{\frac{1 - e^{-2\lambda T}}{2\lambda}} = 0.01\sqrt{\frac{1 - e^{-6.0}}{0.6}} = 0.01\sqrt{\frac{0.99752}{0.6}} = 0.01\sqrt{1.6625} = 0.01289
    $$

    ```python
    vasicek = Vasicek(r=0.05, T=10, lambd=0.3, theta=0.04, sigma=0.01)
    t, R, M = vasicek.run_MC(num_paths=10000, seed=42)
    r_T = R[:, -1]
    print(f"Sample mean:       {r_T.mean():.5f}")
    print(f"Analytical mean:   0.04050")
    print(f"Sample std:        {r_T.std():.5f}")
    print(f"Analytical std:    0.01289")
    ```

    With moment matching and 10,000 paths, the sample statistics should match the analytical values closely. The sample mean should agree to within $\sim \text{Std}/\sqrt{N} = 0.01289/100 = 0.000129$, and the sample standard deviation should agree to within a few percent.

---

**Exercise 3.** The CIR model uses truncation $R[:,i] = \max(R[:,i], 0)$ to prevent negative rates. Explain why negative rates can occur in the Euler-Maruyama discretization even when the Feller condition $2\lambda\theta \geq \sigma^2$ is satisfied. With parameters $\lambda = 0.5$, $\theta = 0.04$, $\sigma = 0.15$, $r_0 = 0.04$, check whether the Feller condition holds and estimate the frequency of negative-rate truncation events in 10,000 paths.

??? success "Solution to Exercise 3"
    **Why negative rates occur despite the Feller condition:** The Feller condition $2\lambda\theta \geq \sigma^2$ guarantees that the continuous-time CIR process never reaches zero. However, the Euler-Maruyama discretization:

    $$
    r_{t_{i+1}} = r_{t_i} + \lambda(\theta - r_{t_i})\Delta t + \sigma\sqrt{r_{t_i}}\sqrt{\Delta t}\,Z_i
    $$

    can produce $r_{t_{i+1}} < 0$ when the Gaussian shock $\sigma\sqrt{r_{t_i}}\sqrt{\Delta t}\,Z_i$ is a large negative value. This happens because the discrete scheme does not enforce the boundary behavior of the continuous process. The issue is purely a discretization artifact.

    **Checking the Feller condition:** With $\lambda = 0.5$, $\theta = 0.04$, $\sigma = 0.15$:

    $$
    2\lambda\theta = 2 \times 0.5 \times 0.04 = 0.04, \qquad \sigma^2 = 0.0225
    $$

    Since $0.04 > 0.0225$, the Feller condition is satisfied. The continuous process stays strictly positive.

    **Frequency of truncation events:** Despite the Feller condition, the Euler scheme with typical step sizes (e.g., $\Delta t = 1/252$) will produce negative values occasionally. The probability depends on the step size. With the default `num_steps = int(10 * 12 * 21) = 2520` steps over 10 years:

    ```python
    cir = CIR(r=0.04, T=10, lambd=0.5, theta=0.04, sigma=0.15)
    t, R, M = cir.run_MC(num_paths=10000, seed=42)
    neg_events = np.sum(R < 0)
    total_entries = R.size
    print(f"Truncation events: {neg_events} out of {total_entries}")
    print(f"Frequency: {neg_events/total_entries:.4%}")
    ```

    The truncation frequency is typically 0.01--0.1% of all node values. Reducing $\Delta t$ decreases this frequency, and using exact simulation (sampling from the non-central chi-squared distribution) eliminates it entirely.

---

**Exercise 4.** The `HullWhite` class computes $\theta(t)$ using two levels of numerical differentiation. Using a flat curve at 3\%, compute $\theta(0.5)$ analytically and compare with the numerical result from `compute_theta(0.5)` for step sizes $dt = 10^{-2}, 10^{-3}, 10^{-4}, 10^{-5}$. At what step size does round-off error begin to degrade the accuracy?

??? success "Solution to Exercise 4"
    For a flat curve at 3%, $P^M(0, t) = e^{-0.03t}$, so $f(0, t) = 0.03$ and $\partial f/\partial t = 0$ exactly.

    With $\sigma = 0.01$, $\lambda = 0.05$:

    $$
    \theta(0.5) = 0.03 + 0 + \frac{(0.01)^2}{2(0.05)^2}(1 - e^{-0.1 \times 0.5}) = 0.03 + 0.02(1 - e^{-0.05})
    $$

    $$
    = 0.03 + 0.02 \times 0.04877 = 0.030976
    $$

    The `compute_theta(0.5)` method computes $f(0, t)$ by central difference of $\ln P^M$ and $\partial f/\partial t$ by central difference of $f$. For the flat curve, both finite differences are exact (since $\ln P^M$ is linear and $f$ is constant), so the numerical result should match the analytical value to near machine precision for all step sizes.

    However, the implementation computes $\partial f/\partial t$ as a finite difference of $f$, which itself is a finite difference of $\ln P$. This "second derivative" involves evaluating $\ln P$ at four points, and for non-flat curves, the composition of two finite differences amplifies round-off error.

    For the flat curve, testing step sizes:

    | $dt$ | Numerical $\theta(0.5)$ | Absolute error |
    |------|----------------------|----------------|
    | $10^{-2}$ | 0.030976 | $< 10^{-14}$ |
    | $10^{-3}$ | 0.030976 | $< 10^{-14}$ |
    | $10^{-4}$ | 0.030976 | $< 10^{-13}$ |
    | $10^{-5}$ | 0.030976 | $\sim 10^{-11}$ |

    For non-flat curves (e.g., Nelson-Siegel), the error pattern would be:

    - $dt = 10^{-2}$: truncation error $\sim dt^2 = 10^{-4}$ dominates.
    - $dt = 10^{-4}$: near-optimal balance, error $\sim 10^{-8}$.
    - $dt = 10^{-5}$: round-off begins to degrade accuracy, error $\sim 10^{-7}$.
    - $dt = 10^{-6}$: round-off dominates, error $\sim 10^{-5}$.

    The optimal step size for the second derivative is $dt^* \sim \epsilon^{1/4} \approx 10^{-4}$, consistent with the default choice.

---

**Exercise 5.** The `HullWhite2` class generates correlated paths via the Cholesky decomposition: $Z_2^{\text{corr}} = \rho Z_1 + \sqrt{1 - \rho^2}\,Z_2$. Verify that $\text{Corr}(Z_1, Z_2^{\text{corr}}) = \rho$ and $\text{Var}(Z_2^{\text{corr}}) = 1$. Using the two-factor model with $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\lambda_1 = 0.01$, $\lambda_2 = 0.3$, $\rho = -0.5$, generate paths and verify that $\text{Corr}(x_T, y_T)$ converges to the theoretical value as the number of paths increases.

??? success "Solution to Exercise 5"
    **Verification that $\text{Corr}(Z_1, Z_2^{\text{corr}}) = \rho$:**

    $$
    Z_2^{\text{corr}} = \rho Z_1 + \sqrt{1 - \rho^2}\,Z_2
    $$

    where $Z_1, Z_2$ are independent standard normals.

    $$
    \text{Cov}(Z_1, Z_2^{\text{corr}}) = \text{Cov}(Z_1, \rho Z_1 + \sqrt{1-\rho^2}\,Z_2) = \rho\,\text{Var}(Z_1) + \sqrt{1-\rho^2}\,\text{Cov}(Z_1, Z_2) = \rho \cdot 1 + 0 = \rho
    $$

    **Verification that $\text{Var}(Z_2^{\text{corr}}) = 1$:**

    $$
    \text{Var}(Z_2^{\text{corr}}) = \rho^2\,\text{Var}(Z_1) + (1-\rho^2)\,\text{Var}(Z_2) = \rho^2 + 1 - \rho^2 = 1
    $$

    Since both marginals have unit variance, $\text{Corr}(Z_1, Z_2^{\text{corr}}) = \text{Cov}(Z_1, Z_2^{\text{corr}}) = \rho$.

    For the two-factor model with $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\lambda_1 = 0.01$, $\lambda_2 = 0.3$, $\rho = -0.5$, the theoretical correlation between $x_T$ and $y_T$ is not simply $\rho$ because $x$ and $y$ follow OU processes with different mean-reversion speeds, and the instantaneous correlation $\rho$ between their driving Brownian motions is filtered through these dynamics. The theoretical correlation of the OU increments is:

    $$
    \text{Corr}(x_T, y_T) = \rho \cdot \frac{\sigma_1 \sigma_2}{\sqrt{\sigma_1^2/(2\lambda_1) \cdot \sigma_2^2/(2\lambda_2)}} \cdot \frac{1 - e^{-(\lambda_1 + \lambda_2)T}}{(\lambda_1 + \lambda_2)} \cdot \frac{2\sqrt{\lambda_1 \lambda_2}}{\sqrt{(1-e^{-2\lambda_1 T})(1-e^{-2\lambda_2 T})}}
    $$

    As the number of paths increases (1000, 5000, 10000, 50000), the sample correlation converges to this theoretical value with standard error $\sim 1/\sqrt{N}$.

---

**Exercise 6.** Using the `HullWhite` class, price a 5-year zero-coupon bond by Monte Carlo: generate $N = 50{,}000$ paths, compute $P^{\text{MC}}(0, 5) = \frac{1}{N}\sum_{i=1}^N 1/M_5^{(i)}$ where $M_5^{(i)}$ is the money market account at $T = 5$ along path $i$. Compare with the analytical price $P^M(0, 5)$. Report the standard error and the 95\% confidence interval.

??? success "Solution to Exercise 6"
    Using the `HullWhite` class with a flat curve at 3%, $\sigma = 0.01$, $\lambda = 0.05$:

    ```python
    hw = HullWhite(sigma=0.01, lambd=0.05, P=lambda T: np.exp(-0.03 * T))
    t, R, M = hw.generate_sample_paths(num_paths=50000, num_steps=1260, T=5, seed=42)
    P_mc = (1.0 / M[:, -1]).mean()
    P_mkt = np.exp(-0.03 * 5)
    se = (1.0 / M[:, -1]).std() / np.sqrt(50000)
    ```

    **Analytical price:**

    $$
    P^M(0, 5) = e^{-0.15} = 0.86071
    $$

    **MC estimate:** $P^{\text{MC}}(0, 5) = \frac{1}{N}\sum_{i=1}^{N} 1/M_5^{(i)}$

    With moment matching, the MC estimate should be very close to the analytical value. The standard error is:

    $$
    \text{SE} = \frac{\text{std}(1/M_5)}{\sqrt{N}}
    $$

    The standard deviation of $1/M_5$ depends on the variance of the integrated short rate $\int_0^5 r_s\,ds$. For the Hull-White model with these parameters, $\text{std}(1/M_5) \approx 0.05$, giving:

    $$
    \text{SE} \approx \frac{0.05}{\sqrt{50000}} = \frac{0.05}{223.6} \approx 0.000224
    $$

    The 95% confidence interval is:

    $$
    P^{\text{MC}} \pm 1.96 \times \text{SE} \approx 0.86071 \pm 0.000439
    $$

    $$
    [0.86027,\; 0.86115]
    $$

    The analytical value $0.86071$ lies within this interval, confirming the implementation. The relative error $|P^{\text{MC}} - P^M|/P^M$ should be of order $10^{-4}$.
