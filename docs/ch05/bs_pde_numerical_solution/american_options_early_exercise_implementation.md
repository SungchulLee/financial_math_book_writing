# American Options and Early Exercise: Implementation

European options can only be exercised at expiration, but **American options** may be exercised **at any time before maturity**. This flexibility introduces the **early exercise premium** and turns the problem into a **free boundary problem**.

---

## The Early Exercise Constraint

The payoff of an American option must always satisfy:

$$
V(S, t) \geq \Phi(S)
$$

where $\Phi(S)$ is the intrinsic (payoff) value:

- Call: $\Phi(S) = \max(S - K, 0)$
- Put: $\Phi(S) = \max(K - S, 0)$

At each time step, enforce: $V(S, t) = \max\left( \text{Continuation Value}, \text{Payoff} \right)$.

---

## Modifying the FDM Approach

After solving the linear system at each time step, **project** the solution to satisfy the constraint:

```python
V_new[i] = max(V_new[i], payoff[i])
```

This turns the PDE into a **Linear Complementarity Problem (LCP)**. The projection approach is effective and easy to implement.

---

## Algorithm: Crank-Nicolson with Projection

1. Discretize space and time.
2. Set the terminal payoff as usual.
3. At each time step:
   - Solve the Crank-Nicolson (or implicit) system.
   - For each node, apply: $V_i^{n+1} = \max(V_i^{n+1}, \Phi(S_i))$.

---

## Python Sketch: American Put Option (CN + Projection)

```python
import numpy as np

def american_put_cn(S_max=200, K=100, T=1.0, r=0.05, sigma=0.2, M=100):
    dS = S_max / M
    S = np.linspace(0, S_max, M + 1)
    dt = 0.4 * dS**2 / (sigma**2 * S_max**2)
    N = int(T / dt)
    dt = T / N

    V = np.maximum(K - S, 0)  # American PUT payoff

    a = np.zeros(M - 1)
    b = np.zeros(M - 1)
    c = np.zeros(M - 1)
    payoff = V.copy()

    for i in range(1, M):
        Si = i * dS
        a[i - 1] = -0.25 * dt * ((sigma**2 * Si**2 - r * Si) / dS**2)
        b[i - 1] = 1 + 0.5 * dt * ((sigma**2 * Si**2 + r) / dS**2)
        c[i - 1] = -0.25 * dt * ((sigma**2 * Si**2 + r * Si) / dS**2)

    for n in range(N):
        rhs = np.zeros(M - 1)
        for i in range(1, M):
            Si = i * dS
            alpha = 0.25 * dt * ((sigma**2 * Si**2 - r * Si) / dS**2)
            beta  = -0.5 * dt * ((sigma**2 * Si**2 + r) / dS**2)
            gamma = 0.25 * dt * ((sigma**2 * Si**2 + r * Si) / dS**2)

            rhs[i - 1] = (
                alpha * V[i - 1] +
                (1 - beta) * V[i] +
                gamma * V[i + 1]
            )

        V[1:M] = solve_tridiagonal(a, b, c, rhs)

        # Early exercise projection
        for i in range(1, M):
            V[i] = max(V[i], payoff[i])

        V[0] = K * np.exp(-r * (T - (n + 1) * dt))  # lower bound
        V[M] = 0  # out of the money

    return S, V
```

---

## Visualizing American vs. European Option Value

```python
import matplotlib.pyplot as plt

S, V_am = american_put_cn()
V_eu = np.maximum(K - S, 0)  # Use BS formula for put if desired

plt.figure(figsize=(10, 6))
plt.plot(S, V_am, label='American Put (CN + Projection)')
plt.plot(S, V_eu, '--', label='European Put (Payoff)')
plt.xlabel("Stock Price")
plt.ylabel("Option Value")
plt.title("American vs. European Put Option")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

The **American put value is always above** the European counterpart due to the early exercise option.

---

## Summary

- American options require solving a **free boundary problem**.
- The solution must satisfy the **early exercise constraint** at all times.
- Simple projection methods are effective when combined with Crank-Nicolson or implicit schemes.
- The **difference between American and European values** represents the **early exercise premium**.
