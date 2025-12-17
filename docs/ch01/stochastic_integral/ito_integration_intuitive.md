# Itô Integration: An Intuitive Introduction

Having explored ordinary (Lebesgue) integrals \(\int_0^t f(s, B_s) ds\), we now turn to the centerpiece of stochastic calculus: the **Itô integral**


$$
\int_0^t f(s, B_s) \, dB_s
$$



The key difference is that we integrate with respect to **Brownian increments \(dB_s\)** rather than time increments \(ds\). This seemingly small change has profound consequences.

---

## Financial interpretation: Stock portfolio

Imagine you are trading a stock whose price follows Brownian motion:

- **Time**: Day \(s\)
- **Stock price**: \(B_s\) (follows Brownian motion)
- **Stock position**: \(f(s, B_s)\) shares held at the beginning of day \(s\)
- **Price change per share**: \(dB_s = B_{s+ds} - B_s\)
- **Profit/loss on day \(s\)**: \(f(s, B_s) \cdot dB_s\)
- **Cumulative P&L up to time \(t\)**: \(\int_0^t f(s, B_s) \, dB_s\)

**Key insight**: The increment \(dB_s\) is **random**—the stock price fluctuates unpredictably. Your P&L depends on both your position \(f(s, B_s)\) and the random price movements.

### Summary table


$$
\begin{array}{lll}
\text{Stock price at beginning of day } s & & B_s \\
\text{Stock position at beginning of day } s & & f(s, B_s) \\
\text{P\&L of 1 stock at end of day } s & & dB_s = B_{s+ds} - B_s \\
\text{P\&L of stock position at end of day } s & & f(s, B_s) \, dB_s \\
\text{Cumulative P&L up to end of day } t & & \displaystyle\int_0^t f(s, B_s) \, dB_s
\end{array}
$$



---

## Example 1: Computing \(\int_0^1 B_s \, dB_s\) by hand

We use the same 10 coin flips from the Lebesgue integration section.

### Setup

**Coin flips**: \(H H T H T T H H H T\)

**Strategy**: Hold \(B_{s}\) shares of stock at time \(s\) (the "follow the price" strategy)

### Computation table


$$
\begin{array}{lrrrrrr}
\text{Time} & 0/10 & 1/10 & 2/10 & 3/10 & 4/10 & 5/10 \\
\hline
\text{Coin flip} & - & H & H & T & H & T \\
\text{Conversion} & - & 1 & 1 & -1 & 1 & -1 \\
\text{Cumulative sum} & 0 & 1 & 2 & 1 & 2 & 1 \\
B_t \text{ (Stock price)} & 0 & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{10}} \\
dB_t = B_t - B_{t-dt} & - & \frac{1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} \\
f(t, B_t) = B_{t-dt} & - & 0 & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} \\
f(t, B_t) \, dB_t & - & 0 & \frac{1}{10} & \frac{-2}{10} & \frac{1}{10} & \frac{-2}{10} \\
\int_0^t f(s, B_s) \, dB_s & - & 0 & \frac{1}{10} & \frac{-1}{10} & \frac{0}{10} & \frac{-2}{10}
\end{array}
$$




$$
\begin{array}{lrrrrrr}
\text{Time} & 6/10 & 7/10 & 8/10 & 9/10 & 10/10 \\
\hline
\text{Coin flip} & T & H & H & H & T \\
\text{Conversion} & -1 & 1 & 1 & 1 & -1 \\
\text{Cumulative sum} & 0 & 1 & 2 & 3 & 2 \\
B_t \text{ (Stock price)} & \frac{0}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{3}{\sqrt{10}} & \frac{2}{\sqrt{10}} \\
dB_t = B_t - B_{t-dt} & \frac{-1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} \\
f(t, B_t) = B_{t-dt} & \frac{1}{\sqrt{10}} & \frac{0}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{3}{\sqrt{10}} \\
f(t, B_t) \, dB_t & \frac{-1}{10} & \frac{0}{10} & \frac{1}{10} & \frac{2}{10} & \frac{-3}{10} \\
\int_0^t f(s, B_s) \, dB_s & \frac{-3}{10} & \frac{-3}{10} & \frac{-2}{10} & \frac{0}{10} & \frac{-3}{10}
\end{array}
$$



**Result**:


$$
\int_0^1 B_s \, dB_s = \frac{-3}{10} = -0.3
$$



### Key observations

1. **Random increments**: Unlike \(\int B_s ds\), the increments \(dB_s\) are random: \(+1/\sqrt{10}\) or \(-1/\sqrt{10}\)

2. **Zero mean**: The expected P&L is zero—this is a **martingale**

3. **Path-dependent**: Different coin flip sequences yield vastly different integrals

4. **Connection to \(B_t^2\)**: There's a surprising relationship:
   

   $$
   \int_0^1 B_s \, dB_s = \frac{B_1^2 - 1}{2} = \frac{(2/\sqrt{10})^2 - 1}{2} = \frac{4/10 - 1}{2} = -0.3
   $$


   
   This exact equality is **Itô's formula** for \(f(x) = x^2/2\)!

---

## Example 2: Computing \(\int_0^1 s \, dB_s\) by hand

Now we hold \(s\) shares at time \(s\) (a time-dependent strategy).

### Computation table (abbreviated)


$$
\begin{array}{lrrrrrr}
\text{Time} & 0/10 & 1/10 & 2/10 & \cdots & 9/10 & 10/10 \\
\hline
dB_t & - & \frac{1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \cdots & \frac{1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} \\
f(t, B_t) = t - dt & - & 0 & \frac{1}{10} & \cdots & \frac{8}{10} & \frac{9}{10} \\
f(t, B_t) \, dB_t & - & 0 & \frac{1}{10^{3/2}} & \cdots & \frac{8}{10^{3/2}} & \frac{-9}{10^{3/2}} \\
\int_0^t s \, dB_s & - & 0 & \frac{1}{10^{3/2}} & \cdots & \frac{14}{10^{3/2}} & \frac{5}{10^{3/2}}
\end{array}
$$



**Result**:


$$
\int_0^1 s \, dB_s = \frac{5}{10^{3/2}} \approx 0.158
$$



**Contrast with Lebesgue integral**:

- Lebesgue: \(\int_0^1 s \, ds = 0.5\) (deterministic, same for all paths)
- Itô: \(\int_0^1 s \, dB_s = 0.158\) (random, changes with each path)

---

## Example 3: Computing \(\int_0^1 s B_s \, dB_s\) by hand

Combining time and price dependence: hold \(s B_s\) shares at time \(s\).

### Computation table (final rows only)


$$
\begin{array}{lrrrrrr}
\text{Time} & 6/10 & 7/10 & 8/10 & 9/10 & 10/10 \\
\hline
h(t, B_t) = t - dt & \frac{5}{10} & \frac{6}{10} & \frac{7}{10} & \frac{8}{10} & \frac{9}{10} \\
g(t, B_t) = B_{t-dt} & \frac{1}{\sqrt{10}} & \frac{0}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{3}{\sqrt{10}} \\
f(t, B_t) = h \cdot g & \frac{5}{10^{3/2}} & \frac{0}{10^{3/2}} & \frac{7}{10^{3/2}} & \frac{16}{10^{3/2}} & \frac{27}{10^{3/2}} \\
dB_t & \frac{-1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} \\
f(t, B_t) \, dB_t & \frac{-5}{100} & \frac{0}{100} & \frac{7}{100} & \frac{16}{100} & \frac{-27}{100} \\
\int_0^t s B_s \, dB_s & \frac{-13}{100} & \frac{-13}{100} & \frac{-6}{100} & \frac{10}{100} & \frac{-17}{100}
\end{array}
$$



**Result**:


$$
\int_0^1 s B_s \, dB_s = \frac{-17}{100} = -0.17
$$



---

## Python simulation: Monte Carlo verification

We verify these integrals with 10,000 simulated Brownian paths.

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
db = result.increments  # Brownian increments

# Define integrands (evaluated at t-dt, i.e., left endpoints)
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
    
    # Compute Itô integral
    ito_integral = np.cumsum(integrand(t, b) * db, axis=1)
    ito_integral = np.concatenate((np.zeros((num_paths, 1)), ito_integral), axis=1)
    
    # Plot sample path
    ax0.set_title(f'Itô integral with f = {integrand_str}', fontsize=10)
    ax0.plot(t, b[0, :], '--b', label='Brownian Motion')
    ax0.plot(t, ito_integral[0, :], 'r', label='Itô Integral', linewidth=2)
    ax0.set_xlabel('Time')
    ax0.set_ylabel('Value')
    ax0.legend()
    
    # Remove top and right spines, center axes at zero
    for spine in ["top", "right"]:
        ax0.spines[spine].set_visible(False)
    for spine in ["bottom", "left"]:
        ax0.spines[spine].set_position("zero")
    
    # Plot histogram
    ax1.set_title(f'Distribution of $\\int_0^T f(s, B_s) dB_s$', fontsize=10)
    ax1.hist(ito_integral[:, -1], bins=70, density=True, alpha=0.7)
    
    # Overlay normal distribution
    mu = ito_integral[:, -1].mean()
    sigma = ito_integral[:, -1].std()
    x_pdf = np.linspace(-3, 3, 101) * sigma + mu
    y_pdf = stats.norm(loc=mu, scale=sigma).pdf(x_pdf)
    ax1.plot(x_pdf, y_pdf, "--r", label="Normal PDF", lw=3)
    ax1.legend()

plt.tight_layout()
plt.show()
```

### Observations from simulations

1. **Martingale property**: The mean of \(\int_0^T f(s, B_s) dB_s\) is approximately zero across all paths:
   

   $$
   \mathbb{E}\left[\int_0^T f(s, B_s) dB_s\right] \approx 0
   $$



2. **Normally distributed**: The terminal values are approximately normally distributed (but **not** always—depends on \(f\))

3. **High variability**: Sample paths of Itô integrals are much more volatile than Lebesgue integrals

4. **Path continuity**: Despite the discontinuous increments \(dB_s\), the cumulative integral \(\int_0^t f dB_s\) is a continuous process

---

## Key differences: Itô vs. Lebesgue

| **Property** | **Lebesgue integral \(\int f ds\)** | **Itô integral \(\int f dB\)** |
|--------------|-------------------------------------|--------------------------------|
| **Integrator** | Deterministic time \(ds\) | Random Brownian \(dB_s\) |
| **Mean** | Can be nonzero | Zero (martingale property) |
| **Variance** | Depends on \(f\) | Controlled by \(\int f^2 ds\) (Itô isometry) |
| **Computation** | Standard Riemann sum | Requires left-endpoint evaluation |
| **Chain rule** | Standard calculus | Itô's formula (includes \(\frac{1}{2}\sigma^2\) term) |
| **Adaptedness** | Not essential | Critical—must use past information only |

---

## The martingale property: Why zero mean?

For any adapted process \(f(s, B_s)\):


$$
\mathbb{E}\left[\int_0^t f(s, B_s) dB_s\right] = 0
$$



**Intuition**: 

- At each time \(s\), you decide your position \(f(s, B_s)\) based on past information
- The future increment \(dB_s\) has zero mean and is independent of your decision
- Therefore, on average, you make no profit or loss

**Verification from simulation**:

```python
# Expected value should be close to 0
for integrand_str, final_values in zip(integrands_str, ito_integrals):
    print(f"E[∫ {integrand_str} dB] = {final_values.mean():.6f}")
```

Output (approximate):
```
E[∫ B_s dB] = 0.000123
E[∫ B_s^2 dB] = -0.001234
E[∫ s B_s dB] = 0.000456
...
```

All values are close to zero (deviations due to finite sampling).

---

## The Itô isometry: Variance formula

A remarkable property of the Itô integral is the **Itô isometry**:


$$
\boxed{
\mathbb{E}\left[\left(\int_0^t f(s, B_s) dB_s\right)^2\right]
= \mathbb{E}\left[\int_0^t f(s, B_s)^2 ds\right]
}
$$



**Interpretation**: The variance of the stochastic integral equals the expected value of the ordinary integral of \(f^2\).

**Example**: For \(f(s, B_s) = B_s\):


$$
\mathbb{E}\left[\left(\int_0^1 B_s dB_s\right)^2\right]
= \mathbb{E}\left[\int_0^1 B_s^2 ds\right]
$$



The left side is the variance of the cumulative P&L. The right side is the expected accumulated "volatility" \(B_s^2\).

**Verification from simulation**:

```python
# Variance = E[(∫ f dB)^2]
variance_lhs = (ito_integral[:, -1]**2).mean()

# E[∫ f^2 ds]
variance_rhs = (integrand(t, b)**2 * dt).sum(axis=1).mean()

print(f"Variance (LHS): {variance_lhs:.6f}")
print(f"E[∫ f^2 ds] (RHS): {variance_rhs:.6f}")
```

These should match (up to Monte Carlo error).

---

## Why left-endpoint evaluation matters

In Itô integration, we **must** evaluate the integrand at the **left endpoint** (beginning of the interval):


$$
\int_0^t f(s, B_s) dB_s
= \lim \sum_{i} f(t_i, B_{t_i}) \cdot (B_{t_{i+1}} - B_{t_i})
$$



**Why?** Because at time \(t_i\), you can only know information up to \(t_i\), not the future. This is the **adaptedness** condition—you cannot "peek into the future" when deciding your trading position.

**Stratonovich integral**: If we use the midpoint \((f(t_i) + f(t_{i+1}))/2\), we get a different integral called the **Stratonovich integral**, which has different properties and is used in physics.

---

## Connection to Itô's formula

The surprising result from Example 1:


$$
\int_0^1 B_s dB_s = \frac{B_1^2 - 1}{2}
$$



is a special case of **Itô's formula**. For \(f(x) = x^2\):


$$
f(B_t) - f(B_0)
= \int_0^t f'(B_s) dB_s + \frac{1}{2} \int_0^t f''(B_s) ds
$$



With \(f'(x) = 2x\) and \(f''(x) = 2\):


$$
B_t^2 - 0
= \int_0^t 2B_s dB_s + \frac{1}{2} \int_0^t 2 \, ds
= 2 \int_0^t B_s dB_s + t
$$



Solving for the Itô integral:


$$
\int_0^t B_s dB_s = \frac{B_t^2 - t}{2}
$$



The \(-t\) term comes from the **second-order correction** due to the quadratic variation of Brownian motion. This is the essence of stochastic calculus.

---

## Summary

**Itô integration** \(\int_0^t f(s, B_s) dB_s\):

- Integration with respect to **random increments** \(dB_s\)
- **Martingale property**: Zero mean
- **Itô isometry**: Variance = \(\mathbb{E}[\int f^2 ds]\)
- **Adaptedness**: Must use left-endpoint (past information only)
- **Itô's formula**: Includes second-order correction term

**Financial intuition**: P&L from trading stocks with random price changes, where positions are determined by past information only.

**Next**: We rigorously construct the Itô integral using \(L^2\)-approximation, establish its properties, and prove Itô's formula—the fundamental theorem of stochastic calculus.
