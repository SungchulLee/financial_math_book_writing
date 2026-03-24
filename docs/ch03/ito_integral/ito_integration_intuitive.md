# Itô Integration: An Intuitive Introduction

### 1. Concept Definition

The **Itô integral** extends ordinary integration to the setting where the integrator is **Brownian motion** rather than time. Unlike a classical Riemann–Stieltjes integral, a pathwise construction fails because Brownian paths have unbounded variation almost surely. For a process $H_t$ that depends only on information available up to time $t$ and satisfies the square-integrability condition

$$
\mathbb{E}\!\left[\int_0^T H_t^2\,dt\right] < \infty,
$$

we define

$$
\int_0^T H_t\,dB_t
$$

as the $L^2$-limit of left-endpoint sums

$$
\int_0^T H_t\,dB_t
:= \lim_{|\Pi|\to 0} \sum_{k=0}^{n-1} H_{t_k}\bigl(B_{t_{k+1}}-B_{t_k}\bigr),
$$

where $\Pi = \{0=t_0<t_1<\cdots<t_n=T\}$ is a partition of $[0,T]$ and $|\Pi|$ is its mesh size.

The **left endpoint** matters: at time $t_k$, the value $H_{t_k}$ is allowed to use only present and past information. This adaptedness condition reflects the idea that one cannot choose a trading position using future price moves. Formally, the available information is represented by the **filtration** $\mathcal{F}_t = \sigma(B_s : 0 \le s \le t)$, and an adapted process $H_t$ is one for which $H_t$ is $\mathcal{F}_t$-measurable.

#### Why a new integral is needed

For ordinary calculus, we integrate against time:

$$
\int_0^T f(t)\,dt
$$

In stochastic calculus, we want to integrate against Brownian motion:

$$
\int_0^T H_t\,dB_t
$$

This is not just a notational change. Brownian motion is almost surely nowhere differentiable and has infinite variation on every interval, so the quantity $dB_t/dt$ does not exist in the classical sense. A new construction is required.

A key property of Brownian motion is its **quadratic variation**. If we divide $[0,t]$ into many small steps and sum the squared increments, then

$$
\sum_k (B_{t_{k+1}}-B_{t_k})^2 \;\to\; t
$$

in $L^2$ and in probability as the partition becomes finer. Unlike ordinary calculus, these second-order terms do **not vanish**. This non-vanishing quadratic variation is responsible for the correction terms in Itô's formula.

```mermaid
flowchart LR
    A[Brownian path B_t] --> B[Divide time into small intervals]
    B --> C["Compute increments ΔB_k"]
    C --> D["Square increments (ΔB_k)²"]
    D --> E["Sum: Σ(ΔB_k)²"]
    E --> F["Limit → t (quadratic variation)"]
```

Because Brownian increments satisfy $\Delta B \sim \sqrt{\Delta t}$, their squares are of order $\Delta t$, so summing them produces a non-vanishing limit. This is the fundamental reason stochastic calculus differs from ordinary calculus.

---

### 2. Intuition and Financial Interpretation

A useful mental model is a simplified trading problem.

* $B_t$: a stylized price fluctuation process
* $H_t$: the number of shares held at time $t$
* $dB_t$: the random price change over a very short interval
* $H_t\,dB_t$: the incremental profit and loss
* $\int_0^T H_t\,dB_t$: the cumulative profit and loss

The key point is that **the position $H_t$ must be chosen before the next price increment occurs**. This is why the Itô integral uses left-endpoint evaluation.

#### Ordinary accumulation versus stochastic accumulation

In a Lebesgue or Riemann integral, accumulation is driven by deterministic time increments $dt$. In an Itô integral, accumulation is driven by random Brownian increments $dB_t$. The integral itself is therefore a random variable, and as $t$ varies, it becomes a random process.

```mermaid
flowchart LR
    A[Choose position H_t using present and past information]
    A --> B[Brownian motion makes a random increment dB_t]
    B --> C["Incremental gain = H_t dB_t"]
    C --> D[Add gains over many short intervals]
    D --> E["Limit gives the Itô integral ∫ H_t dB_t"]
```

---

### 3. Discrete Approximation from Coin Flips

To build intuition, we approximate Brownian motion by a scaled random walk. (Donsker's theorem makes this precise: the scaling limit of the random walk is Brownian motion.)

Divide $[0,1]$ into $n$ equal steps of size $\Delta t = 1/n$. At each step, let the increment be

$$
\Delta B_k = \pm \sqrt{\Delta t}
$$

with equal probability. This scaling ensures variance accumulates correctly: $\operatorname{Var}(B_t) = t$.

If the integrand is $H_t$, then the discrete Itô sum is

$$
\sum_{k=0}^{n-1} H_{t_k}\,\Delta B_k
$$

This left-point evaluation is the discrete version of the Itô integral.

#### A concrete path

Take $n=10$ and coin flips $H,H,T,H,T,T,H,H,H,T$, identifying heads with $+1$ and tails with $-1$. Each Brownian increment is $\Delta B_k = \pm 1/\sqrt{10}$. The resulting path ends at

$$
B_1 = \frac{2}{\sqrt{10}}
$$

This single path is used in the examples below.

---

### 4. Worked Examples

#### Example 1: Integration of $B$ against $dB$

$$
\int_0^1 B_s\,dB_s
$$

The integrand is the current Brownian level, evaluated at the left endpoint. The discrete approximation is $\sum_{k=0}^{9} B_{t_k}\,\Delta B_k$.

**Financial interpretation**: hold $B_s$ shares at time $s$—a "follow the price" strategy that buys when the price rises and sells when it falls.

| Interval | $B_{t_k}$ | $\Delta B_k$ | Contribution |
| -------- | ------------: | -------------: | ------------------: |
| $[0.0,\,0.1]$ | $0$ | $+1/\sqrt{10}$ | $0$ |
| $[0.1,\,0.2]$ | $1/\sqrt{10}$ | $+1/\sqrt{10}$ | $+1/10$ |
| $[0.2,\,0.3]$ | $2/\sqrt{10}$ | $-1/\sqrt{10}$ | $-2/10$ |
| $[0.3,\,0.4]$ | $1/\sqrt{10}$ | $+1/\sqrt{10}$ | $+1/10$ |
| $[0.4,\,0.5]$ | $2/\sqrt{10}$ | $-1/\sqrt{10}$ | $-2/10$ |
| $[0.5,\,0.6]$ | $1/\sqrt{10}$ | $-1/\sqrt{10}$ | $-1/10$ |
| $[0.6,\,0.7]$ | $0$ | $+1/\sqrt{10}$ | $0$ |
| $[0.7,\,0.8]$ | $1/\sqrt{10}$ | $+1/\sqrt{10}$ | $+1/10$ |
| $[0.8,\,0.9]$ | $2/\sqrt{10}$ | $+1/\sqrt{10}$ | $+2/10$ |
| $[0.9,\,1.0]$ | $3/\sqrt{10}$ | $-1/\sqrt{10}$ | $-3/10$ |

The discrete Itô sum is $-3/10 = -0.3$.

**Verification against Itô's formula**: the exact identity gives

$$
\int_0^1 B_s\,dB_s = \frac{B_1^2-1}{2}
$$

Since $B_1 = 2/\sqrt{10}$, we get $(4/10 - 1)/2 = -0.3$. ✓

The key algebraic reason: $B_{t_{k+1}}^2 - B_{t_k}^2 = 2B_{t_k}\,\Delta B_k + (\Delta B_k)^2$. Telescoping the left side gives $B_1^2 - B_0^2$, and the sum of $(\Delta B_k)^2$ converges to $t$—this is the discrete origin of the $-t/2$ correction in Itô's formula.

---

#### Example 2: Integration of $s$ against $dB$

$$
\int_0^1 s\,dB_s
$$

The integrand is deterministic: $H_s = s$. The discrete approximation is $\sum_{k=0}^{9} t_k\,\Delta B_k$.

**Financial interpretation**: gradually increase your position over time—holding $s$ shares at time $s$ regardless of the current price.

| Interval | $t_k$ | $\Delta B_k$ | Contribution |
| -------- | -----: | -------------: | ----------------: |
| $[0.0,\,0.1]$ | $0$ | $+1/\sqrt{10}$ | $0$ |
| $[0.1,\,0.2]$ | $1/10$ | $+1/\sqrt{10}$ | $+1/10^{3/2}$ |
| $[0.2,\,0.3]$ | $2/10$ | $-1/\sqrt{10}$ | $-2/10^{3/2}$ |
| $[0.3,\,0.4]$ | $3/10$ | $+1/\sqrt{10}$ | $+3/10^{3/2}$ |
| $[0.4,\,0.5]$ | $4/10$ | $-1/\sqrt{10}$ | $-4/10^{3/2}$ |
| $[0.5,\,0.6]$ | $5/10$ | $-1/\sqrt{10}$ | $-5/10^{3/2}$ |
| $[0.6,\,0.7]$ | $6/10$ | $+1/\sqrt{10}$ | $+6/10^{3/2}$ |
| $[0.7,\,0.8]$ | $7/10$ | $+1/\sqrt{10}$ | $+7/10^{3/2}$ |
| $[0.8,\,0.9]$ | $8/10$ | $+1/\sqrt{10}$ | $+8/10^{3/2}$ |
| $[0.9,\,1.0]$ | $9/10$ | $-1/\sqrt{10}$ | $-9/10^{3/2}$ |

The sum is $9/10^{3/2} \approx 0.285$.

Since $H_s = s$ is deterministic, the Itô isometry gives

$$
\operatorname{Var}\!\left(\int_0^1 s\,dB_s\right) = \int_0^1 s^2\,ds = \frac{1}{3}
$$

and the integral is Gaussian: $\int_0^1 s\,dB_s \sim \mathcal{N}(0, 1/3)$.

---

#### Example 3: Integration of $sB_s$ against $dB$

$$
\int_0^1 sB_s\,dB_s
$$

Now the integrand depends on both time and the Brownian path: $H_s = sB_s$. By Itô isometry:

$$
\operatorname{Var}\!\left(\int_0^1 sB_s\,dB_s\right)
= \mathbb{E}\!\left[\int_0^1 s^2 B_s^2\,ds\right]
= \int_0^1 s^2 \mathbb{E}[B_s^2]\,ds
= \int_0^1 s^3\,ds = \frac{1}{4}
$$

This integrand is random, so the distribution of the integral will generally not be Gaussian.

---

### 5. Key Properties

The Itô integral $I_t := \int_0^t H_s\,dB_s$ satisfies four fundamental properties.

**Zero mean**: since the integrand is adapted and the Brownian increment has mean zero,

$$
\mathbb{E}\!\left[\int_0^t H_s\,dB_s\right] = 0
$$

**Martingale property**: for $s < t$,

$$
\mathbb{E}[I_t \mid \mathcal{F}_s] = I_s
$$

The integral accumulates gains from a fair game—each increment has expected value zero given the past.

**Itô isometry**: the variance of the integral equals the time integral of the squared integrand,

$$
\mathbb{E}\!\left[\left(\int_0^t H_s\,dB_s\right)^2\right] = \mathbb{E}\!\left[\int_0^t H_s^2\,ds\right]
$$

**Continuous paths**: the process $t \mapsto I_t$ has continuous sample paths almost surely.

---

### 6. Simulation

The following script simulates $20{,}000$ Brownian paths and computes three Itô integrals, verifying the theoretical standard deviations via Monte Carlo.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

T = 3.0
n_per_year = 252
N = int(T * n_per_year)
dt = T / N
sqrt_dt = np.sqrt(dt)
n_paths = 20000
seed = 42
rng = np.random.default_rng(seed)

t = np.linspace(0.0, T, N + 1)

coins = rng.choice([-1, 1], size=(n_paths, N))
dB = coins * sqrt_dt

B = np.zeros((n_paths, N + 1))
B[:, 1:] = np.cumsum(dB, axis=1)


def ito_integral(integrand_values, dB):
    """Cumulative left-endpoint Itô sum."""
    dI = integrand_values * dB
    I = np.zeros((dI.shape[0], dI.shape[1] + 1))
    I[:, 1:] = np.cumsum(dI, axis=1)
    return I


# Case 1: H_s = s B_s  (theoretical sd = T^2/2)
H1 = t[:-1] * B[:, :-1]
I1 = ito_integral(H1, dB)

# Case 2: H_s = s B_s^2
H2 = t[:-1] * (B[:, :-1] ** 2)
I2 = ito_integral(H2, dB)

# Case 3: H_s = -cos(B_s)
H3 = -np.cos(B[:, :-1])
I3 = ito_integral(H3, dB)

cases = [
    (I1, r"$\int_0^T s B_s\,dB_s$", r"$\int_0^s u B_u\,dB_u$",
     "Case 1: linear integrand", T**2 / 2),
    (I2, r"$\int_0^T s B_s^2\,dB_s$", r"$\int_0^s u B_u^2\,dB_u$",
     "Case 2: nonlinear polynomial integrand", None),
    (I3, r"$-\int_0^T \cos(B_s)\,dB_s$", r"$-\int_0^s \cos(B_u)\,dB_u$",
     "Case 3: bounded nonlinear integrand", None),
]

fig, axes = plt.subplots(3, 2, figsize=(14, 14))

for row, (I, xlabel, path_label, title_prefix, th_sd) in enumerate(cases):
    vals = I[:, -1]
    mu = vals.mean()
    sigma = vals.std(ddof=1)

    ax = axes[row, 0]
    count, bins, _ = ax.hist(vals, bins=80, density=True, alpha=0.6,
                              edgecolor="black", label="Monte Carlo")
    x = np.linspace(bins.min(), bins.max(), 500)
    ax.plot(x, norm.pdf(x, mu, sigma), linewidth=2.5,
            label=f"Normal fit  μ={mu:.3f}, σ={sigma:.3f}")
    if th_sd is not None:
        ax.axvline(0, linestyle=":", color="gray")
        ax.set_title(f"{title_prefix}  (theoretical σ = {th_sd:.3f})")
    else:
        ax.set_title(f"{title_prefix}: terminal distribution")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Density")
    ax.legend(fontsize=9)

    ax = axes[row, 1]
    ax.plot(t, B[0], linewidth=2, label=r"$B_s$")
    ax.plot(t, I[0], linewidth=2, label=path_label)
    ax.axhline(0.0, linewidth=0.8, color="gray")
    ax.set_title(f"{title_prefix}: one sample path")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig("./image/simulation_figure.png", dpi=150)
plt.show()
```

![Simulation figure](./image/simulation_figure.png)

The simulation illustrates three important phenomena.

* **Itô isometry accurately predicts variance**: in Case 1 ($H_s = sB_s$), the simulated standard deviation matches the theoretical value $T^2/2 = 4.5$.
* **Nonlinear random integrands produce non-Gaussian distributions**: in Case 2, the nonlinear dependence on $B_s^2$ yields a visibly skewed distribution.
* **Bounded integrands produce concentrated distributions**: in Case 3, $-\cos(B_s)$ is bounded, so the spread is narrower.

---

### 7. Connection to Itô's Formula

The simulation connects naturally to Itô's formula. For $f(x) = \sin x$,

$$
d(\sin B_t) = \cos(B_t)\,dB_t - \tfrac{1}{2} \sin(B_t)\,dt
$$

so Case 3 is related to a transformed Brownian path together with a drift correction. More generally, Itô's formula shows that whenever $f \in C^2$,

$$
f(B_t) = f(B_0) + \int_0^t f'(B_s)\,dB_s + \frac{1}{2}\int_0^t f''(B_s)\,ds
$$

The stochastic integral $\int f'(B_s)\,dB_s$ is the martingale part and the ordinary integral $\frac{1}{2}\int f''(B_s)\,ds$ is the drift correction arising from quadratic variation.

---

### 8. Summary

The Itô integral $\int_0^T H_t\,dB_t$ is the basic building block of stochastic calculus.

| Feature | Itô integral |
|---------|-------------|
| Definition | $L^2$-limit of left-endpoint sums |
| Integrability | $H$ adapted, $\mathbb{E}[\int H_t^2\,dt] < \infty$ |
| Mean | always zero |
| Variance | $\mathbb{E}[\int H_s^2\,ds]$ (= Var since mean is zero; Itô isometry) |
| Paths | continuous a.s. |
| Deterministic $H$ | Gaussian integral |
| Random $H$ | typically non-Gaussian |

The defining feature of stochastic calculus is that Brownian motion has **non-vanishing quadratic variation**, which forces second-order terms to survive in limits and produces the correction terms seen in Itô's formula. A rigorous $L^2$-approximation framework is needed to handle general integrands, prove the martingale property and Itô isometry, and derive Itô's formula—all of which are developed in the following sections.

??? note "Advanced: predictability vs adaptedness"
    The standard technical framework for the Itô integral requires the integrand to be **predictable** (measurable with respect to the $\sigma$-algebra generated by left-continuous adapted processes) rather than merely adapted. For continuous adapted processes—which are progressively measurable—the distinction is minimal, and the adapted framework captures the main intuition. In the general semimartingale theory, predictability becomes essential.

---

## Exercises

**Exercise 1.** Using the coin-flip approximation with $n = 10$ and the sequence $T, H, T, T, H, H, H, T, H, T$, compute the left-endpoint sum approximation to

$$
\int_0^1 B_s^2\, dB_s
$$

Show all intermediate values of $B_{t_k}$ and each contribution $B_{t_k}^2 \Delta B_k$.

---

**Exercise 2.** A trader holds $H_t = t^2$ shares at time $t$, regardless of price. The cumulative profit and loss is $\int_0^T t^2\, dB_t$. Compute the expected P&L and the variance of the P&L over $[0,1]$.

---

**Exercise 3.** Explain in your own words why the Ito integral uses left-endpoint evaluation rather than midpoint or right-endpoint evaluation. Give a financial argument based on the concept of a trading strategy.

---

**Exercise 4.** For a deterministic integrand $h(t)$, the Ito integral $\int_0^T h(t)\, dB_t$ is Gaussian with mean zero and variance $\int_0^T h(t)^2\, dt$. Verify this for $h(t) = e^{-t}$ on $[0, T]$ by computing the variance explicitly.

---

**Exercise 5.** Using Ito's formula, show that

$$
\int_0^t B_s^2\, dB_s = \frac{1}{3}B_t^3 - \int_0^t B_s\, ds
$$

*Hint*: Apply Ito's formula to $f(x) = x^3/3$.

---

**Exercise 6.** The quadratic variation of Brownian motion states that $\sum_k (\Delta B_k)^2 \to t$ as the partition becomes finer. In the coin-flip model with $n = 10$, compute $\sum_{k=0}^{9} (\Delta B_k)^2$ and compare it to the theoretical value $t = 1$. Why is the sum exactly equal to 1 in this model?

---

**Exercise 7.** Consider two Ito integrals: $I_t = \int_0^t B_s\, dB_s$ and $J_t = \int_0^t s\, dB_s$. Using the Ito isometry, compute $\operatorname{Var}(I_1)$ and $\operatorname{Var}(J_1)$. Which integral has larger variance, and why does this make intuitive sense?
