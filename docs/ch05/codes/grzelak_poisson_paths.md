# Grzelak Poisson Paths

## Background

# ======================================================================

Grzelak Poisson Paths

Educational script demonstrating grzelak poisson paths concepts.

---

## Code

```python
"""
# ======================================================================

Grzelak Poisson Paths

Educational script demonstrating grzelak poisson paths concepts.
"""

# This file was placed here in error — Poisson process content belongs in ch07.
# See ch07/codes/grzelak_poisson_process_paths.py for the correct placement.
# This file can be safely deleted.


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
Let $N(t)$ be a Poisson process with intensity $\lambda = 3$. Compute $E[N(2)]$ and $\mathrm{Var}(N(2))$.

??? success "Solution to Exercise 1"
    For a Poisson process with intensity $\lambda$, $N(t) \sim \mathrm{Poisson}(\lambda t)$. Therefore

    $$
    E[N(2)] = \lambda \cdot 2 = 3 \cdot 2 = 6
    $$

    $$
    \mathrm{Var}(N(2)) = \lambda \cdot 2 = 6
    $$

    For a Poisson distribution, the mean and variance are both equal to $\lambda t$.

---

**Exercise 2.**
Define the compensated Poisson process $\tilde{N}(t) = N(t) - \lambda t$. Show that $\tilde{N}(t)$ is a martingale.

??? success "Solution to Exercise 2"
    We need to show $E[\tilde{N}(t) \mid \mathcal{F}_s] = \tilde{N}(s)$ for $s \le t$.

    $$
    E[\tilde{N}(t) \mid \mathcal{F}_s] = E[N(t) - \lambda t \mid \mathcal{F}_s] = E[N(t) \mid \mathcal{F}_s] - \lambda t
    $$

    By the independent increments property, $E[N(t) \mid \mathcal{F}_s] = N(s) + \lambda(t - s)$. Therefore

    $$
    E[\tilde{N}(t) \mid \mathcal{F}_s] = N(s) + \lambda(t-s) - \lambda t = N(s) - \lambda s = \tilde{N}(s)
    $$

    which confirms the martingale property.

---

**Exercise 3.**
Compute the probability that a Poisson process with $\lambda = 5$ has exactly 3 jumps in the interval $[0, 1]$.

??? success "Solution to Exercise 3"
    The number of jumps in $[0,1]$ follows $\mathrm{Poisson}(\lambda \cdot 1) = \mathrm{Poisson}(5)$. Therefore

    $$
    P(N(1) = 3) = \frac{e^{-5} \cdot 5^3}{3!} = \frac{e^{-5} \cdot 125}{6} = \frac{125}{6} \cdot e^{-5} \approx 0.1404
    $$

---

**Exercise 4.**
Describe how to simulate a Poisson process on $[0, T]$ using the inter-arrival time method. If the inter-arrival times are $\tau_1, \tau_2, \ldots$, what is the distribution of each $\tau_k$?

??? success "Solution to Exercise 4"
    Each inter-arrival time $\tau_k$ is independently distributed as $\mathrm{Exponential}(\lambda)$ with density $f(\tau) = \lambda e^{-\lambda \tau}$ for $\tau \ge 0$.

    The simulation algorithm is:

    1. Set $t = 0$ and $n = 0$.
    2. Generate $\tau \sim \mathrm{Exponential}(\lambda)$ (e.g., $\tau = -\ln(U)/\lambda$ where $U \sim \mathrm{Uniform}(0,1)$).
    3. Set $t = t + \tau$.
    4. If $t > T$, stop; otherwise set $n = n + 1$ and record the jump time $t_n = t$.
    5. Repeat from step 2.

    The resulting process $N(t) = \max\{n : t_n \le t\}$ is a Poisson process with intensity $\lambda$.
