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
