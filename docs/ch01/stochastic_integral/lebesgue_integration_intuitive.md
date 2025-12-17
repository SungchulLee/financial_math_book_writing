# Lebesgue Integration: An Intuitive Introduction

Before diving into the rigorous construction of stochastic integrals, we begin with a familiar type of integration—the ordinary (Lebesgue/Riemann) integral of the form:


$$
\int_0^t f(s, B_s) \, ds
$$



where \(f(s, B_s)\) is a function that may depend on both time \(s\) and the Brownian motion path \(B_s\).

This section builds intuition through:
1. A **financial interpretation** (bond portfolio profit/loss)
2. **Paper-and-pencil examples** with discrete coin flips
3. **Python simulations** showing convergence

---

## Financial interpretation: Bond portfolio

Imagine you are managing a bond portfolio where:

- **Time**: Day \(s\)
- **Stock price**: \(B_s\) (follows Brownian motion)
- **Bond position**: \(f(s, B_s)\) bonds held at the beginning of day \(s\)
- **Daily return per bond**: \(ds\) (the time increment itself)
- **Profit/loss on day \(s\)**: \(f(s, B_s) \cdot ds\)
- **Cumulative P&L up to time \(t\)**: \(\int_0^t f(s, B_s) \, ds\)

**Key insight**: This is an ordinary integral—the randomness comes from \(B_s\) affecting the bond position \(f(s, B_s)\), but the increment \(ds\) is deterministic.

### Summary table


$$
\begin{array}{lll}
\text{Stock price at beginning of day } s & & B_s \\
\text{Bond position at beginning of day } s & & f(s, B_s) \\
\text{P\&L of 1 bond at end of day } s & & ds \\
\text{P\&L of bond position at end of day } s & & f(s, B_s) \, ds \\
\text{Cumulative P\&L up to end of day } t & & \displaystyle\int_0^t f(s, B_s) \, ds
\end{array}
$$



---

## Example 1: Computing \(\int_0^1 B_s \, ds\) by hand

We simulate Brownian motion using 10 coin flips, then compute the integral manually.

### Setup

**Coin flips**: \(H H T H T T H H H T\)

**Conversion**: \(H \to +1\), \(T \to -1\)

**Brownian path**: Cumulative sum scaled by \(1/\sqrt{10}\)

### Computation table


$$
\begin{array}{lrrrrrr}
\text{Time} & 0/10 & 1/10 & 2/10 & 3/10 & 4/10 & 5/10 \\
\hline
\text{Coin flip} & - & H & H & T & H & T \\
\text{Conversion} & - & 1 & 1 & -1 & 1 & -1 \\
\text{Cumulative sum} & 0 & 1 & 2 & 1 & 2 & 1 \\
B_t & 0 & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{10}} \\
dt & - & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} \\
f(t, B_t) = B_{t-dt} & - & 0 & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} \\
f(t, B_t) \, dt & - & 0 & \frac{1}{10^{3/2}} & \frac{2}{10^{3/2}} & \frac{1}{10^{3/2}} & \frac{2}{10^{3/2}} \\
\int_0^t f(s, B_s) \, ds & - & 0 & \frac{1}{10^{3/2}} & \frac{3}{10^{3/2}} & \frac{4}{10^{3/2}} & \frac{6}{10^{3/2}}
\end{array}
$$




$$
\begin{array}{lrrrrrr}
\text{Time} & 6/10 & 7/10 & 8/10 & 9/10 & 10/10 \\
\hline
\text{Coin flip} & T & H & H & H & T \\
\text{Conversion} & -1 & 1 & 1 & 1 & -1 \\
\text{Cumulative sum} & 0 & 1 & 2 & 3 & 2 \\
B_t & \frac{0}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{3}{\sqrt{10}} & \frac{2}{\sqrt{10}} \\
dt & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} \\
f(t, B_t) = B_{t-dt} & \frac{1}{\sqrt{10}} & \frac{0}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{3}{\sqrt{10}} \\
f(t, B_t) \, dt & \frac{1}{10^{3/2}} & \frac{0}{10^{3/2}} & \frac{1}{10^{3/2}} & \frac{2}{10^{3/2}} & \frac{3}{10^{3/2}} \\
\int_0^t f(s, B_s) \, ds & \frac{7}{10^{3/2}} & \frac{7}{10^{3/2}} & \frac{8}{10^{3/2}} & \frac{10}{10^{3/2}} & \frac{13}{10^{3/2}}
\end{array}
$$



**Result**:


$$
\int_0^1 B_s \, ds = \frac{13}{10^{3/2}} \approx 0.411
$$



**Note**: This value depends on the specific Brownian path. Different coin flip sequences yield different integrals.

---

## Example 2: Computing \(\int_0^1 s \, ds\) by hand

Using the same coin flips, we compute the deterministic integral.

### Computation table (abbreviated)


$$
\begin{array}{lrrrrrr}
\text{Time} & 0/10 & 1/10 & 2/10 & \cdots & 9/10 & 10/10 \\
\hline
f(t, B_t) = t - dt & - & 0 & \frac{1}{10} & \cdots & \frac{8}{10} & \frac{9}{10} \\
f(t, B_t) \, dt & - & 0 & \frac{1}{100} & \cdots & \frac{8}{100} & \frac{9}{100} \\
\int_0^t s \, ds & - & 0 & \frac{1}{100} & \cdots & \frac{36}{100} & \frac{45}{100}
\end{array}
$$



**Result**:


$$
\int_0^1 s \, ds = \frac{45}{100} = 0.45
$$



**Comparison with calculus**:


$$
\int_0^1 s \, ds = \left[\frac{s^2}{2}\right]_0^1 = 0.5
$$



With only 10 time steps, we get \(0.45\). As we refine the partition (more coin flips), the approximation converges to the exact value \(0.5\).

---

## Example 3: Computing \(\int_0^1 s B_s \, ds\) by hand

Now we integrate a function depending on both time and the Brownian path.

### Computation table (abbreviated)


$$
\begin{array}{lrrrrrr}
\text{Time} & 0/10 & 1/10 & 2/10 & \cdots & 9/10 & 10/10 \\
\hline
h(t, B_t) = t - dt & - & 0 & \frac{1}{10} & \cdots & \frac{8}{10} & \frac{9}{10} \\
g(t, B_t) = B_{t-dt} & - & 0 & \frac{1}{\sqrt{10}} & \cdots & \frac{2}{\sqrt{10}} & \frac{3}{\sqrt{10}} \\
f(t, B_t) = h \cdot g & - & 0 & \frac{1}{10^{3/2}} & \cdots & \frac{16}{10^{3/2}} & \frac{27}{10^{3/2}} \\
f(t, B_t) \, dt & - & 0 & \frac{1}{10^{5/2}} & \cdots & \frac{16}{10^{5/2}} & \frac{27}{10^{5/2}} \\
\int_0^t s B_s \, ds & - & 0 & \frac{1}{10^{5/2}} & \cdots & \frac{44}{10^{5/2}} & \frac{71}{10^{5/2}}
\end{array}
$$



**Result**:


$$
\int_0^1 s B_s \, ds = \frac{71}{10^{5/2}} \approx 0.224
$$



---

## Python simulation: Monte Carlo verification

We now verify these integrals using Monte Carlo simulation with many Brownian paths.

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from brownian_motion import BrownianMotion

num_paths = 10_000
T = 1

# Simulate Brownian motion
bm = BrownianMotion(maturity_time=T, seed=0)
result = bm.simulate(num_paths)
t = result.time_steps
dt = result.time_step_size
b = result.brownian_paths

# Define integrands
integrands = (
    lambda t, b: b[:, :-1],              # B_s
    lambda t, b: b[:, :-1]**2,           # B_s^2
    lambda t, b: t[:-1] * b[:, :-1],     # s B_s
    lambda t, b: t[:-1]**2 * b[:, :-1],  # s^2 B_s
    lambda t, b: t[:-1] * b[:, :-1]**2,  # s B_s^2
    lambda t, b: t[:-1] * np.exp(b[:, :-1]),  # s e^{B_s}
)

integrands_str = (
    "B_s",
    "B_s^2",
    "s B_s",
    "s^2 B_s",
    "s B_s^2",
    "s e^{B_s}",
)

fig, axes = plt.subplots(len(integrands), 2, figsize=(12, 3*len(integrands)))

for i, integrand, integrand_str in zip(range(len(integrands)), integrands, integrands_str):
    ax0, ax1 = axes[i, 0], axes[i, 1]
    
    # Compute Lebesgue integral
    lebesgue_integral = np.cumsum(integrand(t, b) * dt, axis=1)
    lebesgue_integral = np.concatenate((np.zeros((num_paths, 1)), lebesgue_integral), axis=1)
    
    # Plot sample path
    ax0.set_title(f'Lebesgue integral with f = {integrand_str}', fontsize=10)
    ax0.plot(t, b[0, :], '--b', label='Brownian Motion')
    ax0.plot(t, lebesgue_integral[0, :], 'r', label='Lebesgue Integral')
    ax0.set_xlabel('Time')
    ax0.set_ylabel('Value')
    ax0.grid(True)
    ax0.legend()
    
    # Plot histogram
    ax1.set_title(f'Distribution of $\\int_0^T f(s, B_s) ds$', fontsize=10)
    ax1.hist(lebesgue_integral[:, -1], bins=70, density=True)
    
    # Overlay normal distribution
    mu = lebesgue_integral[:, -1].mean()
    sigma = lebesgue_integral[:, -1].std()
    x_pdf = np.linspace(-3, 3, 101) * sigma + mu
    y_pdf = stats.norm(loc=mu, scale=sigma).pdf(x_pdf)
    ax1.plot(x_pdf, y_pdf, "--r", label="Normal PDF", lw=3)
    ax1.legend()
    ax1.grid(True)

plt.tight_layout()
plt.show()
```

### Observations from simulations

1. **Sample paths**: Each Brownian path yields a different integral \(\int_0^T f(s, B_s) ds\)

2. **Distribution**: The terminal values \(\int_0^T f(s, B_s) ds\) across many paths are approximately normally distributed

3. **Deterministic integrands**: When \(f(s, B_s) = h(s)\) depends only on time (not on \(B_s\)), all paths give the same integral:
   

   $$
   \int_0^1 s \, ds = 0.5 \quad \text{(exact)}
   $$



4. **Random integrands**: When \(f(s, B_s)\) depends on \(B_s\), the integral is a random variable

---

## Key differences from Itô integrals

The integrals in this section are **ordinary (Lebesgue) integrals** with respect to time \(ds\). They differ fundamentally from **Itô integrals** \(\int f(s, B_s) dB_s\):

| **Feature** | **Lebesgue integral \(\int f ds\)** | **Itô integral \(\int f dB\)** |
|-------------|-------------------------------------|--------------------------------|
| Integrator | Deterministic time \(ds\) | Random Brownian increment \(dB_s\) |
| Computation | Standard Riemann sum | Requires adapted integrands |
| Properties | Finite variation | Infinite variation, quadratic variation \(= t\) |
| Mean | Can be nonzero | Always zero (martingale) |
| Applications | Deterministic drift, accumulation | Stochastic diffusion, trading P&L |

**Financial interpretation**:

- \(\int f(s, B_s) ds\): P&L from holding \(f(s, B_s)\) bonds, earning deterministic return \(ds\)
- \(\int f(s, B_s) dB_s\): P&L from holding \(f(s, B_s)\) stocks, with random price changes \(dB_s\)

---

## Connection to rigorous theory

In the next sections, we will:

1. **Prove** that Brownian motion has unbounded variation, making pathwise Riemann-Stieltjes integration impossible for \(\int f dB\)

2. **Construct** the Itô integral \(\int f dB\) via \(L^2\)-approximation rather than pathwise limits

3. **Establish** that the Itô integral is a **martingale** with zero mean, unlike Lebesgue integrals

The paper-and-pencil examples here serve as computational intuition, but the rigorous construction requires measure-theoretic probability and martingale theory.

---

## Summary

**Lebesgue integration** \(\int_0^t f(s, B_s) ds\):

- Ordinary integration with deterministic increment \(ds\)
- Computable via Riemann sums (partition, evaluate, sum)
- The randomness enters through \(f(s, B_s)\), not through \(ds\)
- Applications: Accumulation of drift, deterministic time-dependent processes

**Next**: We introduce the **Itô integral** \(\int_0^t f(s, B_s) dB_s\), where the increment \(dB_s\) itself is random. This requires a fundamentally different construction.
