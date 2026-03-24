# The Ordinary Time Integral: An Intuitive Introduction

### 1. Concept Definition

This page introduces **time integrals of stochastic processes** and builds intuition for why these ordinary integrals behave differently from stochastic integrals such as the Itô integral.

The central distinction is the **integrator**. When integrating with respect to **time**,

$$
\int_0^t f(s, B_s)\, ds
$$

the integrator $ds$ is deterministic and smooth. When integrating with respect to **Brownian motion**,

$$
\int_0^t f(s, B_s)\, dB_s
$$

the integrator $dB_s$ is random and irregular. This single difference changes everything.

#### Pathwise construction

The time integral is constructed in three steps.

1. Fix a sample path $\omega$.
2. Treat $s \mapsto f(s, B_s(\omega))$ as an ordinary deterministic function of time.
3. Compute the usual Lebesgue integral.

For each fixed $\omega$, the function $s \mapsto f(s, B_s(\omega))$ is an ordinary time-dependent function. If it is integrable on $[0,t]$, then

$$
\int_0^t f(s, B_s(\omega))\, ds
$$

is defined as a standard Lebesgue integral. Under suitable measurability conditions, the resulting pathwise integral is a **random variable**.

#### Discrete approximation

The integral can be approximated using Riemann sums:

$$
\int_0^t f(s,B_s)\, ds
= \lim_{|\Pi|\to0}
\sum_{k=0}^{n-1} f(t_k,B_{t_k})(t_{k+1}-t_k)
$$

where $\Pi = \{0 = t_0 < t_1 < \cdots < t_n = t\}$ is a partition of the interval.

Because the increment $ds$ is deterministic, **the only randomness comes from the function $f(s,B_s)$**. Any evaluation point (left, midpoint, right) gives the same limit—unlike the stochastic case where the choice of evaluation point matters.

---

### 2. Intuition and Financial Interpretation

Think of $f(s, B_s)$ as a **rate of accumulation** per unit time. Then $f(s,B_s)\,ds$ is the small accumulated amount over a short interval, and

$$
\int_0^t f(s,B_s)\,ds
$$

is the total accumulated quantity over $[0,t]$.

The randomness changes the *shape* of the curve $f(s,B_s)$, but the mechanism of accumulation—multiplying a rate by a time duration and summing—is the same as in ordinary calculus. This contrasts with stochastic integrals where the increment $dB_s$ is itself random.

**Financial examples** of time integrals:

* Cumulative cashflow: $\int_0^t c_s\, ds$
* Accumulated short-rate discount: $\int_0^t r_s\, ds$
* Time-weighted position: $\int_0^t H_s\, ds$

In each case the rate $c_s$, $r_s$, or $H_s$ may be random, but the accumulation mechanism is deterministic.

---

### 3. Discrete Approximation from Coin Flips

To build intuition, we approximate Brownian motion by a scaled random walk.

Divide $[0,1]$ into $n$ equal steps of size $\Delta t = 1/n$. At each step the Brownian increment is approximated by $\Delta B_k = \pm \sqrt{\Delta t}$ with equal probability. This scaling ensures the correct variance: after $k$ steps, $\operatorname{Var}(B_{t_k}) = t_k$.

As the time step shrinks, the scaled random walk converges to Brownian motion (Donsker's theorem). The corresponding discrete sums converge to the continuous-time integral:

$$
\sum_{k=0}^{n-1} f(t_k,B_{t_k})\,\Delta t \;\to\; \int_0^1 f(s,B_s)\,ds
$$

Each term is the area of a thin rectangle with random height $f(t_k,B_{t_k})$ and deterministic width $\Delta t$.

---

### 4. Worked Examples

We illustrate using the coin sequence $H,H,T,H,T,T,H,H,H,T$ with $n=10$, giving increments $\pm 1/\sqrt{10}$.

---

#### Example 1: Integrating $B_s$ with respect to time

$$
\int_0^1 B_s \, ds \approx \sum B_{t_k}\,\Delta t
$$

For this path the discrete sum gives approximately $0.411$.

**Mean and variance**: Since $\mathbb{E}[B_s] = 0$ for all $s$, by linearity and Fubini's theorem:

$$
\mathbb{E}\!\left[\int_0^1 B_s\, ds\right] = \int_0^1 \mathbb{E}[B_s]\, ds = 0
$$

The variance has a clean closed form. Using $\mathbb{E}[B_s B_t] = \min(s,t)$:

$$
\operatorname{Var}\!\left(\int_0^1 B_s\, ds\right)
= \int_0^1 \int_0^1 \min(s,t)\, ds\, dt
$$

Computing explicitly:

$$
\int_0^1 \int_0^1 \min(s,t)\, ds\, dt
= 2\int_0^1 \int_0^t s\, ds\, dt
= 2\int_0^1 \frac{t^2}{2}\, dt
= \int_0^1 t^2\, dt = \frac{1}{3}
$$

This double-integral calculation foreshadows the Itô isometry: both results compute a second moment by reducing a stochastic quantity to an ordinary integral.

---

#### Example 2: Integrating time

When the integrand does not depend on the random path at all, the integral becomes deterministic and is identical for every Brownian path:

$$
\int_0^1 s \, ds = \frac{1}{2}
$$

The Riemann sum approximation gives $\sum t_k\,\Delta t \approx 0.45$, converging to the exact value as the grid becomes finer.

---

#### Example 3: Integrating $sB_s$

Now the integrand depends on both time and the Brownian path:

$$
\int_0^1 s B_s \, ds \approx \sum t_k B_{t_k}\,\Delta t \approx 0.224
$$

This value depends on the realized path. The mean is zero by the same Fubini argument. The variance follows from $\mathbb{E}[B_s^2] = s$:

$$
\operatorname{Var}\!\left(\int_0^1 s B_s\, ds\right)
= \int_0^1 \int_0^1 st\,\mathbb{E}[B_s B_t]\, ds\, dt
= \int_0^1 \int_0^1 st \min(s,t)\, ds\, dt
= 2\int_0^1 t \int_0^t s^2\, ds\, dt
= 2\int_0^1 \frac{t^4}{3}\, dt
= \frac{2}{15}
$$

---

### 5. Monte Carlo Illustration

The following script simulates many Brownian paths and computes several integrals of the form $\int_0^T f(s, B_s)\, ds$.

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from dataclasses import dataclass
from typing import Optional


@dataclass
class BrownianMotionResult:
    time_steps: np.ndarray
    time_step_size: float
    brownian_paths: np.ndarray


class BrownianMotion:
    DEFAULT_STEPS_PER_YEAR = 252

    def __init__(self, maturity_time: float = 1.0, seed: Optional[int] = None):
        if maturity_time <= 0:
            raise ValueError("maturity_time must be positive")
        self.maturity_time = maturity_time
        self.rng = np.random.RandomState(seed)

    def simulate(self, num_paths: int = 1,
                 num_steps: Optional[int] = None) -> BrownianMotionResult:
        if num_paths <= 0:
            raise ValueError("num_paths must be positive")
        if num_steps is None:
            num_steps = int(self.maturity_time * self.DEFAULT_STEPS_PER_YEAR)
        if num_steps <= 0:
            raise ValueError("num_steps must be positive")

        time_steps = np.linspace(0, self.maturity_time, num_steps + 1)
        dt = time_steps[1] - time_steps[0]
        increments = self.rng.standard_normal((num_paths, num_steps)) * np.sqrt(dt)
        brownian_paths = np.concatenate(
            [np.zeros((num_paths, 1)), increments.cumsum(axis=1)], axis=1
        )
        return BrownianMotionResult(time_steps=time_steps,
                                    time_step_size=dt,
                                    brownian_paths=brownian_paths)


if __name__ == "__main__":
    num_paths = 10000
    T = 1

    bm = BrownianMotion(maturity_time=T, seed=0)
    result = bm.simulate(num_paths)

    t = result.time_steps
    dt = result.time_step_size
    b = result.brownian_paths

    # Approximate ∫ f(s,B_s) ds using a left-point Riemann sum.
    # b[:, :-1] excludes the final time point so each row aligns with dt.
    integrands = (
        lambda t, b: b[:, :-1],                    # B_t
        lambda t, b: b[:, :-1] ** 2,               # B_t^2
        lambda t, b: t[:-1] * b[:, :-1],           # t B_t
        lambda t, b: t[:-1] ** 2 * b[:, :-1],      # t^2 B_t
        lambda t, b: t[:-1] * b[:, :-1] ** 2,      # t B_t^2
        lambda t, b: t[:-1] * np.exp(b[:, :-1])    # t e^{B_t}
    )
    labels = ("B_t", "B_t^2", "t B_t", "t^2 B_t", "t B_t^2", "t e^{B_t}")

    fig, axes = plt.subplots(len(integrands), 2, figsize=(12, 3 * len(integrands)))

    for i, (integrand, label) in enumerate(zip(integrands, labels)):
        ax0, ax1 = axes[i, 0], axes[i, 1]

        integral = np.cumsum(integrand(t, b) * dt, axis=1)
        integral = np.concatenate((np.zeros((num_paths, 1)), integral), axis=1)

        ax0.set_title(f"Time integral with f = {label}")
        ax0.plot(t, b[0, :], "--b", label="Brownian Motion")
        ax0.plot(t, integral[0, :], "r", label="Integral")
        ax0.legend()
        ax0.grid(True)

        ax1.set_title(r"Distribution of $\int_0^T f(s,B_s)ds$")
        ax1.hist(integral[:, -1], bins=70, density=True)

        mu = integral[:, -1].mean()
        sigma = integral[:, -1].std()
        x = np.linspace(-3, 3, 101) * sigma + mu
        ax1.plot(x, stats.norm(loc=mu, scale=sigma).pdf(x),
                 "--r", lw=3, label="Normal curve (matching mean and variance)")
        ax1.legend()
        ax1.grid(True)

    plt.tight_layout()
    plt.savefig("./image/lebesgue_integration_intuitive_figure.png", dpi=150)
    plt.show()
```

![Time integral simulation](./image/lebesgue_integration_intuitive_figure.png)

The dashed normal curve matches the simulated mean and variance and serves only as a visual reference. The distribution of these integrals **need not be exactly normal** in general.

---

### 6. Key Observations

Four patterns appear consistently in the simulation.

1. **Each Brownian path produces a different integral value.** The integral $\int_0^T f(s, B_s)\,ds$ depends on the realized path.

2. **Randomness enters through the integrand only.** The increment $ds$ is deterministic; it does not contribute randomness.

3. **Deterministic integrands give deterministic integrals.** For example, $\int_0^1 s\,ds = 0.5$ is the same for every path.

4. **Random integrands give random integrals.** When $f(s,B_s)$ depends on $B_s$, the integral is a random variable.

---

### 7. Comparison with Itô Integrals

Time integrals and Itô integrals differ fundamentally.

| Feature | Time integral $\int f(s,B_s)\,ds$ | Itô integral $\int f(s,B_s)\,dB_s$ |
| --- | --- | --- |
| Integrator | deterministic time $ds$ | Brownian motion $dB_s$ |
| Definition | pathwise Lebesgue integral | $L^2$-limit of left-endpoint sums |
| Randomness | enters through integrand | enters through integrator |
| Mean | depends on integrand | zero (martingale property) |
| Quadratic variation | zero | $\int_0^t f^2\,ds > 0$ |
| Evaluation point | any point gives same limit | left endpoint essential |
| Interpretation | accumulated quantity over time | accumulation against random fluctuations |

---

### 8. Summary

The integral $\int_0^t f(s,B_s)\,ds$ is an ordinary time integral, constructed pathwise as standard Lebesgue integration.

* The increment $ds$ is deterministic; randomness enters only through $f(s,B_s)$.
* Standard Riemann sums converge and any evaluation point gives the same limit.
* The integral is a random variable when $f$ depends on $B_s$, with mean and variance computable by ordinary calculus and Fubini's theorem.

---

### 9. Why Ordinary Calculus Breaks for Brownian Motion

Although Brownian motion is continuous, its **total variation is infinite on every interval** while its **quadratic variation is finite**. This unusual combination is the fundamental reason stochastic calculus differs from ordinary calculus.

The time integral works because $ds$ is smooth. Now suppose we try to define

$$
\int_0^t f(s, B_s)\, dB_s
\approx \sum f(t_k, B_{t_k})(B_{t_{k+1}} - B_{t_k})
$$

Because Brownian paths have infinite variation, summing absolute increments $\sum |B_{t_{k+1}} - B_{t_k}|$ diverges as the partition becomes finer. Moreover, unlike the time integral, the limit of discrete sums **depends on where the integrand is sampled**—left endpoint, midpoint, and right endpoint give different limits. Different conventions lead to different stochastic integrals: most notably the **Itô integral** (left endpoint) and the **Stratonovich integral** (midpoint).

To make sense of $\int_0^t f(s, B_s)\, dB_s$, we must introduce a new definition of integration specifically designed for stochastic processes—the Itô integral studied in the next section.

---

## Exercises

**Exercise 1.** Let $B_t$ be a standard Brownian motion. Compute the mean and variance of the time integral

$$
\int_0^T B_s^2 \, ds
$$

*Hint*: Use Fubini's theorem and $\mathbb{E}[B_s^2] = s$, $\mathbb{E}[B_s^4] = 3s^2$.

---

**Exercise 2.** Using the coin-flip approximation with $n = 10$ and the sequence $T, H, H, T, T, H, T, H, H, H$, compute the discrete Riemann sum approximation to

$$
\int_0^1 B_s \, ds
$$

Compare your answer with the theoretical mean of this integral.

---

**Exercise 3.** Explain why the Riemann sum approximation to $\int_0^t f(s, B_s)\, ds$ converges to the same limit regardless of whether the integrand is evaluated at the left endpoint, midpoint, or right endpoint of each subinterval. Why does this property fail for stochastic integrals of the form $\int_0^t f(s, B_s)\, dB_s$?

---

**Exercise 4.** Compute the variance of

$$
\int_0^T s^2 B_s \, ds
$$

by evaluating the double integral $\int_0^T \int_0^T s^2 t^2 \min(s,t)\, ds\, dt$.

---

**Exercise 5.** In the short-rate model, the discount factor is $D(0,T) = \exp\!\left(-\int_0^T r_s\, ds\right)$, where $r_t = r_0 + \sigma B_t$ for constants $r_0 > 0$ and $\sigma > 0$. Show that $\int_0^T r_s\, ds$ is Gaussian and find its mean and variance.

---

**Exercise 6.** Let $f(s) = e^{-\alpha s}$ for a constant $\alpha > 0$. Show that the integral $\int_0^T f(s) \, ds$ is deterministic and compute its value. Then consider the integral $\int_0^T f(s) B_s \, ds$ and compute its variance.

---

**Exercise 7.** Prove that $\int_0^t B_s \, ds$ has the same distribution as $\int_0^t (t - s) \, dB_s$ by computing the mean and variance of both sides. Why does the representation $\int_0^t B_s\, ds = tB_t - \int_0^t s\, dB_s$ (integration by parts) make this plausible?
