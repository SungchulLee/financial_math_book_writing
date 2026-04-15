# Quadratic Variation

### 1. Concept Definition

**Quadratic variation** measures the cumulative size of squared increments of a stochastic process. For a partition $\Pi = \{0 = t_0 < t_1 < \cdots < t_n = T\}$ with mesh $\|\Pi\| = \max_k(t_k - t_{k-1})$, the **quadratic variation sum** of a process $X$ is

$$
Q(X, \Pi) := \sum_{k=1}^n (X_{t_k} - X_{t_{k-1}})^2
$$

If this sum converges as $\|\Pi\| \to 0$, the limit is the **quadratic variation** $[X]_T$. More precisely, the quadratic variation process $[X]_t$ is defined on $[0,t]$ for each $t \ge 0$.

Two facts are foundational:

$$
\boxed{[W]_t = t}
\qquad\text{for standard Brownian motion } W_t
$$

$$
\boxed{[A]_T = 0}
\qquad\text{for any process of finite (total) variation}
$$

These two facts have a single consequence: **Brownian motion is categorically different from any smooth or piecewise smooth path**. A differentiable function has zero quadratic variation; Brownian motion has quadratic variation equal to $t$. This distinction is the mechanism behind every correction term in stochastic calculus.

---

### 2. Explanation

#### Why quadratic variation matters

In ordinary calculus, when expanding $f(x + h) - f(x)$ by Taylor's theorem, the second-order term $f''(x)h^2/2$ is negligible because $h^2 \ll h$ as $h \to 0$. In stochastic calculus, the second-order term **survives** because Brownian increments satisfy $(\Delta W)^2 \approx \Delta t$ rather than $(\Delta W)^2 \ll \Delta t$.

This is why Itô's formula has an extra term compared to the ordinary chain rule:

$$
df(W_t) = f'(W_t)\,dW_t + \frac{1}{2}f''(W_t)\,dt
$$

The $\frac{1}{2}f''(W_t)\,dt$ term comes from summing $f''(W_{t_k})(\Delta W_k)^2 \approx f''(W_{t_k})\Delta t_k \to \int f''(W_t)\,dt$. This is exactly the quadratic variation.

#### Proof that [W]ₜ = t

We show $Q(W, \Pi) \to t$ in $L^2$ (and hence in probability) as $\|\Pi\| \to 0$.

Write $\Delta W_k = W_{t_k} - W_{t_{k-1}}$ and $\Delta t_k = t_k - t_{k-1}$. Since $\Delta W_k \sim \mathcal{N}(0, \Delta t_k)$ and the increments are independent:

$$
\mathbb{E}[Q(W, \Pi)]
= \sum_k \mathbb{E}[(\Delta W_k)^2]
= \sum_k \Delta t_k = t
$$

For the variance, use $\operatorname{Var}((\Delta W_k)^2) = 2(\Delta t_k)^2$ (fourth moment of a centred normal):

$$
\operatorname{Var}(Q(W, \Pi))
= \sum_k \operatorname{Var}((\Delta W_k)^2)
= 2\sum_k (\Delta t_k)^2
\le 2\|\Pi\| \sum_k \Delta t_k
= 2\|\Pi\|\, t \;\to\; 0
$$

Since $\mathbb{E}[Q(W,\Pi)] = t$ and $\operatorname{Var}(Q(W,\Pi)) \to 0$, we have $Q(W,\Pi) \to t$ in $L^2$. $\square$

#### Why smooth paths have zero quadratic variation

For a function $f: [0,T] \to \mathbb{R}$ with $|f'(t)| \le M$ for all $t$, each increment satisfies $|f(t_k) - f(t_{k-1})| \le M \Delta t_k$, so

$$
Q(f, \Pi) = \sum_k (f(t_k) - f(t_{k-1}))^2 \le M \sum_k |\Delta f_k| \cdot \Delta t_k \le M^2 \sum_k (\Delta t_k)^2 \le M^2 \|\Pi\| T \to 0
$$

More generally, any process of **bounded variation** has zero quadratic variation.

#### The Itô multiplication table

Quadratic variation is the rigorous content behind the heuristic rules used in stochastic calculus. For a multidimensional Brownian motion $W_t = (W_t^1, \ldots, W_t^m)$:

$$
\boxed{
(dt)^2 = 0, \qquad dt\, dW_t^\alpha = 0, \qquad dW_t^\alpha\, dW_t^\beta = \delta^{\alpha\beta}\, dt
}
$$

These rules arise from the covariation formula $[W^\alpha, W^\beta]_t = \delta^{\alpha\beta} t$.

**Derivation of $dW^\alpha\, dW^\beta = \delta^{\alpha\beta}\,dt$.** For $\alpha = \beta$: we have just shown $[W^\alpha]_t = t$, so $(dW^\alpha)^2 \to dt$. For $\alpha \ne \beta$: $W^\alpha$ and $W^\beta$ are independent Brownian motions with independent increments $\Delta W_k^\alpha$ and $\Delta W_k^\beta$, so

$$
\mathbb{E}\!\left[\sum_k \Delta W_k^\alpha \Delta W_k^\beta\right] = \sum_k \mathbb{E}[\Delta W_k^\alpha]\mathbb{E}[\Delta W_k^\beta] = 0
$$

and the variance of the sum also tends to zero, giving $[W^\alpha, W^\beta]_t = 0$.

#### Quadratic variation of Itô integrals

Let $M_t = \int_0^t H_s\, dW_s$ with $H$ square-integrable and adapted. Then $M$ is a continuous martingale and

$$
\boxed{[M]_t = \int_0^t H_s^2\, ds}
$$

More generally, for $M_t = \int_0^t H_s\, dW_s$ and $N_t = \int_0^t K_s\, dW_s$:

$$
\boxed{[M, N]_t = \int_0^t H_s K_s\, ds}
$$

This generalizes both formulas: setting $H_s = K_s = 1$ gives $[W,W]_t = t$.

---

### 3. Diagram

```mermaid
flowchart TD
    A["Partition Π of [0,T]"]
    A --> B["Quadratic variation sum: Q(X, Π) = Σ(ΔX_k)²"]

    B --> C{"Process type?"}

    C --> D["Smooth / finite variation — e.g. f(t) = t, sin(t)"]
    C --> E["Brownian motion W_t"]
    C --> F["Itô integral M_t = ∫H_s dW_s"]

    D --> G["(ΔX)² ~ (Δt)² — sum → 0 — [A]_T = 0"]
    E --> H["(ΔW)² ~ Δt — E[Q] = t, Var[Q] → 0 — [W]_T = T"]
    F --> I["(ΔM)² ~ H²Δt — [M]_T = ∫H_s² ds"]

    H --> J["Itô formula correction: ½f''(W_t)dt"]
    I --> J
    G --> K["Ordinary chain rule — no correction needed"]
```

---

### 4. Examples

#### Example 1: Quadratic variation of Wₜ — numerical verification

The following script simulates many Brownian paths and plots the quadratic variation sum against the theoretical value $t$.

```python
import numpy as np
import matplotlib.pyplot as plt

T = 1.0
N = 500
dt = T / N
n_paths = 2000
seed = 42
rng = np.random.default_rng(seed)

t = np.linspace(0, T, N + 1)

dW = rng.standard_normal((n_paths, N)) * np.sqrt(dt)
W = np.concatenate([np.zeros((n_paths, 1)), np.cumsum(dW, axis=1)], axis=1)

# Cumulative quadratic variation: [W]_t = Σ_{k: t_k ≤ t} (ΔW_k)²
qv = np.cumsum(dW ** 2, axis=1)
qv = np.concatenate([np.zeros((n_paths, 1)), qv], axis=1)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Left: several sample paths of cumulative QV versus t
ax = axes[0]
for i in range(10):
    ax.plot(t, qv[i], "b", alpha=0.4, linewidth=0.8)
ax.plot(t, t, "r--", linewidth=2, label=r"$[W]_t = t$ (theoretical)")
ax.plot(t, qv.mean(axis=0), "k", linewidth=2, label="Monte Carlo mean")
ax.set_title("Cumulative quadratic variation of $W_t$")
ax.set_xlabel("$t$")
ax.set_ylabel("$[W]_t$")
ax.legend()
ax.grid(True)

# Right: QV at T=1 — distribution across paths
ax = axes[1]
ax.hist(qv[:, -1], bins=60, density=True, alpha=0.7, edgecolor="black")
ax.axvline(1.0, color="r", linestyle="--", linewidth=2, label=r"$[W]_T = T = 1$")
ax.axvline(qv[:, -1].mean(), color="k", linestyle="-", linewidth=2,
           label=f"Monte Carlo mean = {qv[:, -1].mean():.4f}")
ax.set_title(r"Distribution of $[W]_1$ across paths")
ax.set_xlabel(r"$[W]_1$")
ax.set_ylabel("Density")
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.savefig("./image/quadratic_variation_figure.png", dpi=150)
plt.show()

print(f"Monte Carlo mean of [W]_1  : {qv[:, -1].mean():.6f}")
print(f"Monte Carlo std of [W]_1   : {qv[:, -1].std():.6f}")
print(f"Theoretical value          : {T:.6f}")
print(f"Theoretical std (N={N})    : {np.sqrt(2 * dt * T):.6f}")
```

![Quadratic variation figure](./image/quadratic_variation_figure.png)

Each sample path of $[W]_t$ (blue) fluctuates around the deterministic line $t$ (red). The Monte Carlo mean (black) tracks $t$ closely. The right panel shows that $[W]_1$ concentrates tightly around $1$—consistent with $\operatorname{Var}([W]_T) = 2T \cdot \Delta t \to 0$ as $\Delta t \to 0$.

---

#### Example 2: Quadratic variation of the Ornstein-Uhlenbeck process

The OU process $dX_t = -\theta X_t\,dt + \sigma\,dB_t$ has $\sigma_t = \sigma$ (constant). Therefore:

$$
[X]_t = \int_0^t \sigma^2\, ds = \sigma^2 t
$$

The drift $-\theta X_t\,dt$ contributes nothing to the quadratic variation. This confirms that **quadratic variation detects only the diffusion coefficient**, regardless of the drift.

---

#### Example 3: Itô's formula from quadratic variation

Apply Itô's formula to $f(x) = x^2$ with $X_t = W_t$:

$$
W_t^2 = W_0^2 + \int_0^t 2W_s\,dW_s + \int_0^t 1\, d[W]_s
= 0 + 2\int_0^t W_s\,dW_s + t
$$

where $d[W]_s = ds$ since $[W]_s = s$.

Rearranging:

$$
\int_0^t W_s\, dW_s = \frac{W_t^2 - t}{2}
$$

The $-t/2$ correction is exactly the quadratic variation of $W$ on $[0,t]$. In ordinary calculus, $\int_0^t x\, dx = x^2/2$; in stochastic calculus, the answer is $W_t^2/2 - t/2$ because the quadratic variation term $\frac{1}{2} \cdot 2 \cdot [W]_t = t$ must be subtracted.

---

### 5. Summary

* The quadratic variation $[X]_t$ is the $L^2$ (and probability) limit of the sum of squared increments $\sum_k (\Delta X_k)^2$ as the partition mesh tends to zero.
* For Brownian motion, $[W]_t = t$, proved by computing that $\mathbb{E}[Q] = t$ and $\operatorname{Var}(Q) \to 0$.
* For smooth or finite-variation processes, $[A]_t = 0$.
* For an Itô integral $M_t = \int_0^t H_s\,dW_s$, the quadratic variation is $[M]_t = \int_0^t H_s^2\,ds$.
* The Itô multiplication table $dW^\alpha\,dW^\beta = \delta^{\alpha\beta}\,dt$ is the symbolic expression of these quadratic variation identities.
* Quadratic variation is the reason Itô's formula differs from the ordinary chain rule: second-order Taylor terms survive in the stochastic setting because $(\Delta W)^2 \approx \Delta t \not\to 0$.

---

## Exercises

**Exercise 1.** Let $f(t) = t^2$ on $[0,1]$. For a uniform partition with $n$ subintervals, compute the quadratic variation sum $Q(f, \Pi) = \sum_{k=1}^n (f(t_k) - f(t_{k-1}))^2$ explicitly. Show that $Q(f, \Pi) \to 0$ as $n \to \infty$, confirming that smooth functions have zero quadratic variation.

??? success "Solution to Exercise 1"
    On a uniform partition $t_k = k/n$, $\Delta t = 1/n$, and $f(t_k) = (k/n)^2$. The increments are:

    $$
    f(t_k) - f(t_{k-1}) = \frac{k^2}{n^2} - \frac{(k-1)^2}{n^2} = \frac{2k - 1}{n^2}
    $$

    The quadratic variation sum is:

    $$
    Q(f, \Pi) = \sum_{k=1}^n \left(\frac{2k-1}{n^2}\right)^2 = \frac{1}{n^4}\sum_{k=1}^n (2k-1)^2
    $$

    Using $\sum_{k=1}^n (2k-1)^2 = \frac{n(2n-1)(2n+1)}{3}$:

    $$
    Q(f, \Pi) = \frac{(2n-1)(2n+1)}{3n^3} = \frac{4n^2 - 1}{3n^3}
    $$

    As $n \to \infty$:

    $$
    Q(f, \Pi) = \frac{4n^2 - 1}{3n^3} \sim \frac{4}{3n} \to 0
    $$

    This confirms that the smooth function $f(t) = t^2$ has zero quadratic variation.

---

**Exercise 2.** Using the identity $\operatorname{Var}((\Delta W_k)^2) = 2(\Delta t_k)^2$ for a Gaussian increment, show that

$$
\operatorname{Var}(Q(W, \Pi)) = 2 \sum_{k=1}^n (\Delta t_k)^2
$$

For a uniform partition with $n$ subintervals on $[0,T]$, evaluate this expression and verify it tends to zero as $n \to \infty$.

??? success "Solution to Exercise 2"
    Since $\Delta W_k \sim \mathcal{N}(0, \Delta t_k)$ and increments are independent:

    $$
    Q(W, \Pi) = \sum_{k=1}^n (\Delta W_k)^2
    $$

    Each $(\Delta W_k)^2$ is an independent random variable. For a centered Gaussian $Z \sim \mathcal{N}(0, \sigma^2)$, $\operatorname{Var}(Z^2) = \mathbb{E}[Z^4] - (\mathbb{E}[Z^2])^2 = 3\sigma^4 - \sigma^4 = 2\sigma^4$.

    So $\operatorname{Var}((\Delta W_k)^2) = 2(\Delta t_k)^2$, and by independence:

    $$
    \operatorname{Var}(Q(W, \Pi)) = \sum_{k=1}^n \operatorname{Var}((\Delta W_k)^2) = 2\sum_{k=1}^n (\Delta t_k)^2
    $$

    For a uniform partition on $[0, T]$: $\Delta t_k = T/n$ for all $k$:

    $$
    \operatorname{Var}(Q(W, \Pi)) = 2\sum_{k=1}^n \frac{T^2}{n^2} = 2n \cdot \frac{T^2}{n^2} = \frac{2T^2}{n} \to 0 \quad \text{as } n \to \infty
    $$

---

**Exercise 3.** Let $X_t = \mu t + \sigma W_t$ be Brownian motion with drift. Compute the quadratic variation $[X]_t$. Does the drift $\mu t$ contribute to the quadratic variation? Justify your answer.

??? success "Solution to Exercise 3"
    Write $X_t = \mu t + \sigma W_t$. The increment is $\Delta X_k = \mu \Delta t_k + \sigma \Delta W_k$. The quadratic variation sum is:

    $$
    \sum_k (\Delta X_k)^2 = \sum_k (\mu \Delta t_k + \sigma \Delta W_k)^2
    $$

    $$
    = \mu^2 \sum_k (\Delta t_k)^2 + 2\mu\sigma \sum_k \Delta t_k \Delta W_k + \sigma^2 \sum_k (\Delta W_k)^2
    $$

    As the mesh $\|\Pi\| \to 0$:

    - $\sum_k (\Delta t_k)^2 \le \|\Pi\| \cdot T \to 0$
    - $\sum_k \Delta t_k \Delta W_k \to 0$ in probability (by a similar argument, the variance is bounded by $\sum_k (\Delta t_k)^2 \cdot \Delta t_k \to 0$)
    - $\sum_k (\Delta W_k)^2 \to t$ in $L^2$

    Therefore $[X]_t = \sigma^2 t$. The drift $\mu t$ does **not** contribute to the quadratic variation, because the drift increments $\mu \Delta t_k$ are of order $\Delta t_k$, so their squares $\mu^2 (\Delta t_k)^2$ are of order $(\Delta t_k)^2$ and vanish when summed.

---

**Exercise 4.** Let $M_t = \int_0^t s\, dW_s$. Compute the quadratic variation $[M]_t$ and use it to verify that $M_t^2 - [M]_t$ is a martingale by computing $\mathbb{E}[M_t^2 - [M]_t]$.

??? success "Solution to Exercise 4"
    Since $M_t = \int_0^t s\, dW_s$, the quadratic variation is:

    $$
    [M]_t = \int_0^t s^2\, ds = \frac{t^3}{3}
    $$

    To verify that $M_t^2 - [M]_t$ is a martingale, compute its expectation. By the Ito isometry:

    $$
    \mathbb{E}[M_t^2] = \mathbb{E}\!\left[\int_0^t s^2\, ds\right] = \frac{t^3}{3}
    $$

    Therefore:

    $$
    \mathbb{E}[M_t^2 - [M]_t] = \frac{t^3}{3} - \frac{t^3}{3} = 0
    $$

    for all $t$, which is consistent with $M_t^2 - [M]_t$ being a martingale (a martingale starting at zero has constant expectation equal to zero).

---

**Exercise 5.** Using the Ito multiplication table, compute $(dX_t)^2$ for the Ornstein-Uhlenbeck process $dX_t = -\theta X_t\, dt + \sigma\, dW_t$. What is $[X]_t$?

??? success "Solution to Exercise 5"
    The OU process has $dX_t = -\theta X_t\, dt + \sigma\, dW_t$. Using the multiplication rules:

    $$
    (dX_t)^2 = (-\theta X_t\, dt + \sigma\, dW_t)^2
    $$

    Expanding:

    $$
    = \theta^2 X_t^2 (dt)^2 - 2\theta X_t \sigma\, dt\, dW_t + \sigma^2 (dW_t)^2
    $$

    Applying $(dt)^2 = 0$, $dt\, dW_t = 0$, $(dW_t)^2 = dt$:

    $$
    (dX_t)^2 = \sigma^2\, dt
    $$

    Therefore $d[X]_t = \sigma^2\, dt$, giving $[X]_t = \sigma^2 t$.

---

**Exercise 6.** Prove that if a process $A_t$ has bounded total variation on $[0,T]$, then $[A]_T = 0$. *Hint*: Bound $\sum_k (\Delta A_k)^2 \le \max_k |\Delta A_k| \cdot \sum_k |\Delta A_k|$ and argue that $\max_k |\Delta A_k| \to 0$ for a continuous finite-variation process.

??? success "Solution to Exercise 6"
    Let $V = \sup_\Pi \sum_k |A_{t_k} - A_{t_{k-1}}| < \infty$ be the total variation of $A$ on $[0,T]$. For any partition $\Pi$:

    $$
    \sum_k (\Delta A_k)^2 = \sum_k |\Delta A_k|^2 \le \left(\max_k |\Delta A_k|\right) \cdot \sum_k |\Delta A_k| \le \left(\max_k |\Delta A_k|\right) \cdot V
    $$

    Since $A_t$ is continuous (and hence uniformly continuous on $[0,T]$), as the mesh $\|\Pi\| \to 0$, $\max_k |\Delta A_k| \to 0$. Since $V < \infty$ is a fixed finite constant:

    $$
    \sum_k (\Delta A_k)^2 \le \left(\max_k |\Delta A_k|\right) \cdot V \to 0 \cdot V = 0
    $$

    Therefore $[A]_T = 0$.

---

**Exercise 7.** Apply Ito's formula to $f(x) = x^4$ with $X_t = W_t$ to derive

$$
W_t^4 = 4\int_0^t W_s^3\, dW_s + 6\int_0^t W_s^2\, ds
$$

Use this identity and the Ito isometry to compute $\mathbb{E}\!\left[\left(\int_0^t W_s^3\, dW_s\right)^2\right]$. *Hint*: You will need $\mathbb{E}[W_s^6] = 15s^3$.

??? success "Solution to Exercise 7"
    Apply Ito's formula to $f(x) = x^4$ with $X_t = W_t$. We have $f'(x) = 4x^3$ and $f''(x) = 12x^2$:

    $$
    W_t^4 = 0 + \int_0^t 4W_s^3\, dW_s + \frac{1}{2}\int_0^t 12W_s^2\, ds = 4\int_0^t W_s^3\, dW_s + 6\int_0^t W_s^2\, ds
    $$

    Now compute $\mathbb{E}[(\int_0^t W_s^3\, dW_s)^2]$ using the Ito isometry:

    $$
    \mathbb{E}\!\left[\left(\int_0^t W_s^3\, dW_s\right)^2\right] = \mathbb{E}\!\left[\int_0^t W_s^6\, ds\right] = \int_0^t \mathbb{E}[W_s^6]\, ds
    $$

    Using $\mathbb{E}[W_s^6] = 15s^3$ (the sixth moment of $\mathcal{N}(0, s)$ is $15s^3$):

    $$
    = \int_0^t 15s^3\, ds = 15 \cdot \frac{t^4}{4} = \frac{15t^4}{4}
    $$
