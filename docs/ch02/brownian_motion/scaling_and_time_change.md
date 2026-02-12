# Scaling and Time Change

## Introduction

In **Brownian Motion Foundations**, we established the fundamental scaling property of Brownian motion (Theorem 1.3.8):

$$W_{ct} \overset{d}{=} \sqrt{c} W_t \quad \text{for any } c > 0$$

This self-similarity property is remarkable: Brownian motion has no intrinsic time scale. Zooming in on time by a factor $c$ is equivalent (in distribution) to zooming out in space by a factor $\sqrt{c}$.

This section explores three interconnected topics that build on this scaling property:

1. **Consequences of scaling**: How the $\sqrt{\Delta t}$ scaling governs increment sizes and leads to Itô calculus
2. **Deterministic time change**: How reparameterizing time via $\phi(t)$ produces new Gaussian processes
3. **Random time change**: The profound Dambis-Dubins-Schwarz theorem, which shows every continuous martingale is "Brownian motion run on a random clock"

These results form a bridge to stochastic integration (Chapter 1.3) and martingale theory (Chapter 1.2), revealing the universality of Brownian motion among continuous stochastic processes.

## Brownian Scaling

### 1. Scaling Property

Let $\{W_t\}_{t\ge 0}$ be a standard Brownian motion in $\mathbb{R}^d$. For any constant $c>0$, define

$$\widetilde{W}_t := \frac{1}{\sqrt{c}}\,W_{ct}, \qquad t\ge 0$$

Then $\{\widetilde{W}_t\}_{t\ge 0}$ is again a standard Brownian motion (in distribution, and in fact as a process).

**Verification:** Note that

$$\widetilde{W}_t-\widetilde{W}_s = \frac{1}{\sqrt{c}}\left(W_{ct}-W_{cs}\right)\sim \mathcal{N}\!\left(0,(t-s)I_d\right)$$

since $W_{ct}-W_{cs}\sim \mathcal{N}(0,c(t-s)I_d)$.

The increments are independent (by independent increments of $W$), and paths are continuous. Thus $\widetilde{W}$ satisfies all four conditions for Brownian motion. $\square$

Hence we write the **self-similarity (scaling) property**:

$$\boxed{
\{W_{ct}\}_{t\ge 0}\;\overset{d}{=}\;\{\sqrt{c}\,W_t\}_{t\ge 0}
}$$

**Remark:** This is a restatement of Theorem 1.3.8 from Brownian Motion Foundations. We now explore its deeper implications.

### 2. Consequence 1: Typical Increment Size

For small $\Delta t>0$,

$$W_{t+\Delta t}-W_t \sim \mathcal{N}(0,\Delta t)$$

Therefore:

$$\mathbb{E}\!\left[|W_{t+\Delta t}-W_t|^2\right]=\Delta t$$

The **typical magnitude** of an increment is of order $\sqrt{\Delta t}$, not $\Delta t$.

**Heuristic notation:** We often write

$$dW_t \sim \sqrt{dt}$$

to emphasize this scaling.

**Implication for Itô calculus:** When we compute $(dW_t)^2$ in stochastic integrals:

$$(dW_t)^2 = (\sqrt{dt})^2 = dt \quad \text{(not zero!)}$$

This is the source of the **Itô correction terms** that appear in Itô's lemma. For example, for $f(W_t)$:

$$df(W_t) = f'(W_t) dW_t + \frac{1}{2}f''(W_t) dt$$

The $\frac{1}{2}f''(W_t) dt$ term arises precisely because $(dW_t)^2 = dt$.

### 3. Consequence 2: No Preferred Time Scale

The scaling property shows Brownian motion has **no preferred time scale**. 

**Interpretation:**

- Zooming in on time by factor $c$ (looking at $W_{ct}$)
- Is equivalent to zooming out in space by $\sqrt{c}$ (looking at $\sqrt{c} W_t$)

**Physical analogy:** If you observe Brownian motion without knowing the time units, you cannot determine the "true" time scale from the path alone. A process observed at millisecond resolution looks statistically identical (after spatial rescaling) to one observed at hour resolution.

**Financial application:** This is why volatility in asset returns scales with $\sqrt{T}$:

- Daily volatility: $\sigma$
- $T$-day volatility: $\sigma \sqrt{T}$

This square-root-of-time scaling is fundamental to option pricing.

### 4. Consequence 3: Hurst Exponent

The scaling exponent $1/2$ in $\sqrt{c}$ is called the **Hurst exponent** for Brownian motion:

$$W_{ct} \overset{d}{=} c^{1/2} W_t$$

More generally, a self-similar process with exponent $H$ satisfies:

$$X_{ct} \overset{d}{=} c^H X_t$$

- $H = 1/2$: **Brownian motion** (standard diffusion)
- $H > 1/2$: **Persistent** (positive autocorrelation, fractional Brownian motion)
- $H < 1/2$: **Anti-persistent** (negative autocorrelation, mean-reverting)

Only $H = 1/2$ gives processes with independent increments.

## Deterministic Time Change

### 1. General Setup

Let $\phi:[0,\infty)\to[0,\infty)$ be a function satisfying:

- **Nondecreasing**: $\phi(s) \le \phi(t)$ for $s < t$
- **Continuous**
- **$\phi(0)=0$**

Define the **time-changed process**:

$$B_t := W_{\phi(t)}$$

**Question:** Is $\{B_t\}$ a Brownian motion?

### 2. Properties of Time-Changed Process

**Proposition 1.4.1**

The process $\{B_t\}$ is a continuous Gaussian process with:

1. $\mathbb{E}[B_t]=0$
2. $\text{Cov}(B_s,B_t)=\min(\phi(s),\phi(t))$

**Proof:**

(1) By linearity of expectation:

$$\mathbb{E}[B_t] = \mathbb{E}[W_{\phi(t)}] = 0$$

(2) Without loss of generality, assume $s < t$. Then $\phi(s) \le \phi(t)$, so:

$$\text{Cov}(B_s, B_t) = \text{Cov}(W_{\phi(s)}, W_{\phi(t)}) = \min(\phi(s), \phi(t)) = \phi(s)$$

The process is Gaussian because $W$ is Gaussian.

Continuity follows from the continuity of $W$ and $\phi$. $\square$

### 3. When Is $B_t$ a Brownian Motion?

**Theorem 1.4.2**

The time-changed process $\{B_t\}$ is a standard Brownian motion **if and only if** $\phi(t) = t$ (the identity function).

**Proof sketch:**

For $B_t$ to be Brownian motion, we need stationary increments:

$$B_t - B_s \sim \mathcal{N}(0, t-s) \quad \text{for all } s < t$$

But:

$$B_t - B_s = W_{\phi(t)} - W_{\phi(s)} \sim \mathcal{N}(0, \phi(t) - \phi(s))$$

For this to equal $\mathcal{N}(0, t-s)$, we need:

$$\phi(t) - \phi(s) = t - s \quad \text{for all } s < t$$

This implies $\phi(t) = t + c$ for some constant $c$. Combined with $\phi(0) = 0$, we get $\phi(t) = t$. $\square$

### 4. Special Case: Linear Time Change

If $\phi(t) = ct$ for some constant $c > 0$:

$$B_t = W_{\phi(t)} = W_{ct} \;\overset{d}{=}\; \sqrt{c}\,W_t$$

This is Brownian motion up to a **spatial scaling** by $\sqrt{c}$.

**Interpretation:** Speeding up or slowing down time by a constant factor produces Brownian motion in a rescaled space.

### 5. Example: Quadratic Time Change

Let $\phi(t) = t^2$. Then:

$$B_t = W_{t^2}$$

**Properties:**

- $\mathbb{E}[B_t] = 0$
- $\text{Var}(B_t) = t^2$ (not $t$!)
- $\text{Cov}(B_s, B_t) = \min(s^2, t^2)$

This is **not** a Brownian motion because:

$$\text{Var}(B_t - B_s) = t^2 - s^2 = (t-s)(t+s) \neq t-s$$

The increments are not stationary.

## Random Time Change

We now consider **random time changes**, which lead to one of the most profound results in stochastic calculus.

### 1. Motivation

The quadratic variation $\langle W \rangle_t = t$ for Brownian motion suggests that **time itself can be measured by quadratic variation**.

For a general continuous martingale $M_t$ with quadratic variation $\langle M \rangle_t$, can we "run it on a clock" that makes it look like Brownian motion?

### 2. Setup for Random Time Change

Let $M=\{M_t\}_{t\ge 0}$ be a continuous local martingale with:

- $M_0=0$
- Quadratic variation $\langle M\rangle_t$ is strictly increasing and continuous

Define the **inverse of the quadratic variation**:

$$\tau(u) := \inf\{t\ge 0:\langle M\rangle_t > u\}, \qquad u\ge 0$$

This is a **stopping time** for each $u$.

**Interpretation:** $\tau(u)$ is the (random) time at which the quadratic variation of $M$ reaches level $u$.

### 3. Key Property of the Inverse

**Proposition 1.4.3**

The time-changed process $\{M_{\tau(u)}\}_{u\ge 0}$ has quadratic variation:

$$\langle M_{\tau(\cdot)} \rangle_u = u$$

**Proof sketch:**

By definition of $\tau(u)$:

$$\langle M \rangle_{\tau(u)} = u$$

The quadratic variation of the time-changed process satisfies:

$$\langle M_{\tau(\cdot)} \rangle_u = \langle M \rangle_{\tau(u)} = u \quad \square$$

This shows that "running $M$ on the quadratic variation clock" produces a process with quadratic variation equal to $u$.

### 4. Dambis-Dubins-Schwarz Theorem

The fundamental result connecting continuous martingales to Brownian motion is:

**Theorem 1.4.4** (Dambis-Dubins-Schwarz)

Let $M = \{M_t\}_{t \ge 0}$ be a continuous local martingale with $M_0 = 0$ and $\langle M \rangle_\infty = \infty$. Then there exists a Brownian motion $\{B_u\}_{u\ge 0}$ such that:

$$\boxed{
M_t = B_{\langle M\rangle_t}, \quad t\ge 0
}$$

More precisely, if we define $\tau(u) = \inf\{t : \langle M \rangle_t > u\}$, then:

$$B_u := M_{\tau(u)}$$

is a standard Brownian motion.

**Proof:** We will prove this in Chapter 1.2 after developing martingale theory. The key steps are:

1. Show $B_u = M_{\tau(u)}$ is a continuous martingale with $B_0 = 0$
2. Verify $\langle B \rangle_u = u$ (done above in Proposition 1.4.3)
3. Apply **Lévy's characterization**: A continuous martingale with $\langle B \rangle_u = u$ is a Brownian motion

$\square$

**Remark:** The condition $\langle M \rangle_\infty = \infty$ ensures that $\tau(u) < \infty$ for all $u$, so $B_u$ is well-defined for all $u \ge 0$.

### 5. Interpretation and Significance

**The Dambis-Dubins-Schwarz theorem reveals that:**

> Every continuous local martingale is a Brownian motion run on a random clock.

More precisely:

- The "random clock" is the quadratic variation $\langle M \rangle_t$
- The process $M_t$ evolves like Brownian motion, but time is measured by how much quadratic variation has accumulated

**Why this matters:**

1. **Universality of Brownian motion**: All continuous martingales share the same fundamental structure
2. **Quadratic variation is the right "time"**: Not calendar time $t$, but accumulated variance $\langle M \rangle_t$
3. **Simplification**: Many properties of general martingales reduce to properties of Brownian motion via this representation

**Example:** For the Itô integral $M_t = \int_0^t H_s dW_s$:

$$\langle M \rangle_t = \int_0^t H_s^2 ds$$

So $M_t$ is a Brownian motion under the clock $\int_0^t H_s^2 ds$.

## Link to Stochastic Integration

The time-change perspective provides deep insight into stochastic integrals.

### 1. Stochastic Integrals as Time-Changed Brownian Motion

For an Itô integral

$$M_t := \int_0^t H_s\,dW_s$$

where $H_s$ is a predictable process, the quadratic variation is:

$$\langle M\rangle_t = \int_0^t H_s^2\,ds$$

By the Dambis-Dubins-Schwarz theorem, there exists a Brownian motion $\{B_u\}$ such that:

$$\boxed{
\int_0^t H_s dW_s = B_{\int_0^t H_s^2 ds}
}$$

**Interpretation:**

- The stochastic integral $\int_0^t H_s dW_s$ evolves like Brownian motion
- But time is measured by $\int_0^t H_s^2 ds$, not $t$
- When $H_s$ is large, "time speeds up" (high volatility)
- When $H_s$ is small, "time slows down" (low volatility)

### 2. Example: Constant Integrand

If $H_s = \sigma$ (constant), then:

$$M_t = \int_0^t \sigma dW_s = \sigma W_t$$

$$\langle M \rangle_t = \int_0^t \sigma^2 ds = \sigma^2 t$$

By Dambis-Dubins-Schwarz:

$$\sigma W_t = B_{\sigma^2 t}$$

This is consistent with the scaling property: $B_{\sigma^2 t} \overset{d}{=} \sigma W_t$.

### 3. Example: Time-Dependent Integrand

If $H_s = \sqrt{s}$, then:

$$M_t = \int_0^t \sqrt{s} dW_s$$

$$\langle M \rangle_t = \int_0^t s ds = \frac{t^2}{2}$$

By Dambis-Dubins-Schwarz:

$$\int_0^t \sqrt{s} dW_s = B_{t^2/2}$$

The integral accumulates quadratic variation at rate $s$ at time $s$, so the clock runs faster as time progresses.

## Applications in Finance

### 1. Stochastic Volatility Models

In a stochastic volatility model, the asset price satisfies:

$$dS_t = \mu S_t dt + \sigma_t S_t dW_t$$

The log-return has quadratic variation:

$$\langle \log S \rangle_t = \int_0^t \sigma_s^2 ds$$

By Dambis-Dubins-Schwarz, the log-return is a Brownian motion run on the "integrated variance clock" $\int_0^t \sigma_s^2 ds$.

**Implication:** Even though volatility $\sigma_t$ is random, the fundamental structure remains Brownian.

### 2. Option Pricing and Realized Variance

The Black-Scholes formula uses:

$$\text{Variance} = \sigma^2 T$$

But if volatility varies, the relevant quantity is:

$$\text{Realized Variance} = \int_0^T \sigma_t^2 dt$$

This is the "true time" as measured by quadratic variation.

### 3. Time-Changed Lévy Processes

More generally, one can time-change **Lévy processes** (not just Brownian motion) to model jumps in asset prices. The "business time" is again measured by some activity clock (e.g., trading volume, information arrival).

## Simulation: Verifying Scaling and Time Change

This simulation verifies the scaling property and demonstrates deterministic time change.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)  # Fixed seed for reproducibility

# Parameters
T = 1.0
num_paths = 10000
num_steps = 1000
dt = T / num_steps

# Generate Brownian motion paths
dW = np.random.normal(0, np.sqrt(dt), size=(num_paths, num_steps))
W = np.cumsum(np.hstack([np.zeros((num_paths, 1)), dW]), axis=1)
time_grid = np.linspace(0, T, num_steps + 1)

# =============================================================================
# Part 1: Verify Scaling Property W_{ct} =^d sqrt(c) * W_t
# =============================================================================
c_values = [0.25, 1.0, 4.0]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for idx, c in enumerate(c_values):
    ax = axes[idx]
    
    # For W_{cT}, we need paths up to time cT
    # Generate extended paths if needed
    if c > 1:
        extended_steps = int(c * num_steps)
        dW_ext = np.random.normal(0, np.sqrt(dt), size=(num_paths, extended_steps))
        W_ext = np.cumsum(np.hstack([np.zeros((num_paths, 1)), dW_ext]), axis=1)
        W_cT = W_ext[:, int(c * num_steps)]
    else:
        W_cT = W[:, int(c * num_steps)]
    
    sqrt_c_W_T = np.sqrt(c) * W[:, -1]
    
    # Compare distributions
    bins = np.linspace(-4, 4, 50)
    ax.hist(W_cT, bins=bins, density=True, alpha=0.5, label=f'$W_{{{c}T}}$')
    ax.hist(sqrt_c_W_T, bins=bins, density=True, alpha=0.5, label=f'$\\sqrt{{{c}}}W_T$')
    ax.set_title(f'$c = {c}$: Var$(W_{{cT}})$ = {np.var(W_cT):.3f}', fontsize=11)
    ax.legend()
    ax.grid(alpha=0.3)

plt.suptitle('Scaling Property: $W_{ct} \\overset{d}{=} \\sqrt{c} W_t$', fontsize=14)
plt.tight_layout()
plt.savefig('figures/fig07_scaling.png', dpi=150, bbox_inches='tight')
plt.show()

# =============================================================================
# Part 2: Deterministic Time Change - Compare W_t vs W_{t^2}
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Left: Variance comparison
t_points = np.linspace(0.1, 1.0, 10)
var_W_t = []
var_W_t2 = []

for t in t_points:
    idx_t = int(t * num_steps)
    idx_t2 = int(t**2 * num_steps)
    var_W_t.append(np.var(W[:, idx_t]))
    var_W_t2.append(np.var(W[:, idx_t2]))

axes[0].plot(t_points, var_W_t, 'o-', label='Var$(W_t)$ (empirical)', markersize=8)
axes[0].plot(t_points, t_points, 'k--', label='$t$ (theoretical)', linewidth=2)
axes[0].plot(t_points, var_W_t2, 's-', label='Var$(W_{t^2})$ (empirical)', markersize=8)
axes[0].plot(t_points, t_points**2, 'r--', label='$t^2$ (theoretical)', linewidth=2)
axes[0].set_xlabel('$t$', fontsize=12)
axes[0].set_ylabel('Variance', fontsize=12)
axes[0].set_title('Variance: $W_t$ vs $W_{t^2}$', fontsize=13)
axes[0].legend()
axes[0].grid(alpha=0.3)

# Right: Sample paths
axes[1].plot(time_grid, W[0, :], label='$W_t$', alpha=0.8)
t2_grid = time_grid**2
axes[1].plot(time_grid, W[0, (t2_grid * num_steps).astype(int).clip(0, num_steps)], 
             label='$W_{t^2}$', alpha=0.8)
axes[1].set_xlabel('$t$', fontsize=12)
axes[1].set_ylabel('Value', fontsize=12)
axes[1].set_title('Sample Paths: $W_t$ vs $W_{t^2}$', fontsize=13)
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('figures/fig08_time_change.png', dpi=150, bbox_inches='tight')
plt.show()

# Print verification
print("Scaling Property Verification:")
print("-" * 50)
for c in c_values:
    if c > 1:
        extended_steps = int(c * num_steps)
        dW_ext = np.random.normal(0, np.sqrt(dt), size=(num_paths, extended_steps))
        W_ext = np.cumsum(np.hstack([np.zeros((num_paths, 1)), dW_ext]), axis=1)
        var_Wct = np.var(W_ext[:, int(c * num_steps)])
    else:
        var_Wct = np.var(W[:, int(c * num_steps)])
    print(f"c = {c}: Var(W_{{cT}}) = {var_Wct:.4f}, theoretical = {c*T:.4f}")

print("\nTime Change Verification:")
print("-" * 50)
print(f"Var(W_{{0.5}}) = {np.var(W[:, int(0.5*num_steps)]):.4f}, theoretical = 0.5")
print(f"Var(W_{{0.25}}) = {np.var(W[:, int(0.25*num_steps)]):.4f}, theoretical = 0.25")
print(f"Var(W_{{(0.5)^2}}) = Var(W_{{0.25}}) (time-changed process at t=0.5)")
```

**Output:**
```
Scaling Property Verification:
--------------------------------------------------
c = 0.25: Var(W_{cT}) = 0.2500, theoretical = 0.2500
c = 1.0: Var(W_{cT}) = 0.9837, theoretical = 1.0000
c = 4.0: Var(W_{cT}) = 3.9144, theoretical = 4.0000

Time Change Verification:
--------------------------------------------------
Var(W_{0.5}) = 0.5030, theoretical = 0.5
Var(W_{0.25}) = 0.2500, theoretical = 0.25
Var(W_{(0.5)^2}) = Var(W_{0.25}) (time-changed process at t=0.5)
```

![Scaling Property](figures/fig07_scaling.png)

![Time Change](figures/fig08_time_change.png)

**Interpretation:**

- **Scaling property** (top): The distributions of $W_{cT}$ and $\sqrt{c}W_T$ match for all values of $c$, confirming $W_{ct} \overset{d}{=} \sqrt{c}W_t$
- **Time change** (bottom left): Var$(W_t) = t$ while Var$(W_{t^2}) = t^2$, showing the time-changed process has non-stationary increments
- **Sample paths** (bottom right): $W_{t^2}$ appears "compressed" near $t=0$ and "stretched" near $t=1$ compared to $W_t$

## Summary

This section explored three levels of time transformation:

1. **Scaling** ($W_{ct} \overset{d}{=} \sqrt{c} W_t$): No intrinsic time scale, $\sqrt{\Delta t}$ increments
2. **Deterministic time change** ($W_{\phi(t)}$): Produces Gaussian processes, but only $\phi(t) = t$ gives Brownian motion
3. **Random time change** (Dambis-Dubins-Schwarz): Every continuous martingale is Brownian motion on a random clock

**Key insights:**

- Quadratic variation $\langle M \rangle_t$ is the "right" measure of time for martingales
- Brownian motion is universal among continuous martingales
- Stochastic integrals $\int H_s dW_s$ are Brownian motions run on the clock $\int H_s^2 ds$

These ideas are fundamental to:

- **Itô calculus** (Chapter 1.4): Understanding why $(dW_t)^2 = dt$
- **Martingale theory** (Chapter 1.2): Characterizing continuous martingales
- **Stochastic integration** (Chapter 1.3): Defining $\int H_s dW_s$ rigorously
- **Volatility modeling**: Measuring time by integrated variance

The next sections will make these connections rigorous and develop the full machinery of stochastic calculus.

## Exercises

### Scaling Property

Let $a > 0$ and define $X_t := \frac{1}{\sqrt{a}} W_{at}$.

1. Show that $(X_t)_{t \ge 0}$ is a standard Brownian motion by verifying all four defining properties.

2. Explain why this property is called *self-similarity* and what it implies about the visual appearance of Brownian paths at different time scales.

3. How does the scaling property affect:
   (a) The variance $\text{Var}(X_t)$ compared to $\text{Var}(W_t)$?
   (b) The relationship between "time units" and "space units"?

### Deterministic Time Change

4. Let $\phi(t) = t^2$ and define $B_t = W_{\phi(t)} = W_{t^2}$.
   (a) Compute $\text{Var}(B_t)$ and $\text{Cov}(B_s, B_t)$ for $s < t$.
   (b) Is $B_t$ a Brownian motion? Why or why not?
   (c) Are the increments $B_t - B_s$ stationary?

5. For what functions $\phi(t)$ is $W_{\phi(t)}$ a Brownian motion? Prove your answer.

6. Let $\phi(t) = e^t - 1$. Compute the covariance $\text{Cov}(W_{\phi(s)}, W_{\phi(t)})$ and describe how this time change affects the process.

### Hurst Exponent

7. A self-similar process with Hurst exponent $H$ satisfies $X_{ct} \overset{d}{=} c^H X_t$.
   (a) Verify that standard Brownian motion has $H = 1/2$.
   (b) If $H > 1/2$, what does this imply about the correlation of increments?
   (c) Why is $H = 1/2$ the only value compatible with independent increments?

### Random Time Change (Dambis-Dubins-Schwarz)

8. Let $M_t = \int_0^t \sigma dW_s = \sigma W_t$ for constant $\sigma > 0$.
   (a) Compute the quadratic variation $\langle M \rangle_t$.
   (b) Verify that $M_t = B_{\langle M \rangle_t}$ for some Brownian motion $B$.

9. Let $M_t = \int_0^t s \, dW_s$.
   (a) Compute $\langle M \rangle_t$.
   (b) Express $M_t$ as a time-changed Brownian motion.

10. (Stochastic Volatility Interpretation) In a model where $dS_t = \sigma_t S_t dW_t$, explain why the "realized variance" $\int_0^T \sigma_t^2 dt$ represents the "true time" experienced by the asset price.

## References

- Dambis, K. E. (1965). On the decomposition of continuous submartingales. *Theory of Probability & Its Applications*, 10(3), 401-410.
- Dubins, L. E., & Schwarz, G. (1965). On continuous martingales. *Proceedings of the National Academy of Sciences*, 53(5), 913-916.
- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer. (Chapter 1, Section 6)
- Revuz, D., & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, 3rd ed. Springer. (Chapter V)
