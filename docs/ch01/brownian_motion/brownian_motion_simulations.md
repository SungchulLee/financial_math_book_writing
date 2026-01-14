# Brownian Motion



## Introduction



This section provides computational illustrations of the theoretical properties of Brownian motion developed in **Brownian Motion Foundations**. Through Monte Carlo simulation, we verify and visualize:

- Gaussian distribution of $W_t \sim \mathcal{N}(0, t)$
- Path continuity and nowhere differentiability
- Quadratic variation $\langle W \rangle_t = t$
- Self-similarity and scaling properties
- First passage time distributions

These examples serve two purposes: (1) building intuition for abstract properties, and (2) validating theoretical predictions numerically.

**Note:** These simulations are supplementary to the mathematical theory. Understanding the proofs in the previous section is essential; the code merely illustrates the results.

## Monte Carlo



### 1. Discrete Approxim



To simulate Brownian motion on $[0, T]$ with $n$ time steps:

1. **Time discretization:** $t_i = i \cdot \Delta t$ where $\Delta t = T/n$
2. **Independent increments:** $\Delta W_i = W_{t_{i+1}} - W_{t_i} \sim \mathcal{N}(0, \Delta t)$
3. **Path construction:** $W_{t_i} = \sum_{j=1}^{i} \Delta W_j$ (cumulative sum)

**Convergence:** As $n \to \infty$ (i.e., $\Delta t \to 0$), the discrete approximation converges to true Brownian motion.

## Example 1 Basic Path



This example simulates multiple Brownian motion paths and verifies the Gaussian distribution at maturity.

### 1. Theory Recap



**Theorem:** Brownian motion satisfies:

- $W_0 = 0$ almost surely
- $W_t \sim \mathcal{N}(0, t)$ for each $t > 0$
- Paths are continuous

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Simulation
num_paths = 10_000   # Number of Brownian motion paths
num_steps = 1_000    # Number of time steps
maturity_time = 2    # Maturity time for Brownian motion (T = 2)

# Set random seed
np.random.seed(0)

# Generate time
dt = maturity_time / num_steps
time_steps = np.linspace(0, maturity_time, num_steps + 1)

# Generate Brownian
# Each increment N 0
dW = np.random.normal(0, np.sqrt(dt), size=(num_paths, num_steps))
brownian_paths = np.cumsum(np.hstack([np.zeros((num_paths, 1)), dW]), axis=1)

# Create figure two
fig, (ax_paths, ax_distribution) = plt.subplots(1, 2, figsize=(12, 4))

# Plot 10 sample paths
ax_paths.set_title(f'Ten Sample Paths of $W_t$', fontsize=13)
for i in range(10):
    ax_paths.plot(time_steps, brownian_paths[i, :], alpha=0.7, linewidth=1.5)
ax_paths.set_xlabel('Time $t$', fontsize=11)
ax_paths.set_ylabel('$W_t$', fontsize=11)
ax_paths.axhline(0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
ax_paths.grid(alpha=0.3)

# Plot distribution
ax_distribution.set_title(f'Distribution of $W_{{{maturity_time}}}$', fontsize=13)
counts, bin_edges, patches = ax_distribution.hist(
    brownian_paths[:, -1], 
    bins=100, 
    density=True, 
    alpha=0.6,
    color='steelblue',
    label=f"$W_{{{maturity_time}}}$ Samples"
)

# Overlay theoretical
x_range = np.linspace(bin_edges[0], bin_edges[-1], 200)
theoretical_pdf = stats.norm(loc=0, scale=np.sqrt(maturity_time)).pdf(x_range)
ax_distribution.plot(x_range, theoretical_pdf, '--r', linewidth=2, 
                     label=f"$\mathcal{{N}}(0,{maturity_time})$ PDF")
ax_distribution.set_xlabel('$W_T$', fontsize=11)
ax_distribution.set_ylabel('Density', fontsize=11)
ax_distribution.legend(fontsize=10)
ax_distribution.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Verify mean variance
sample_mean = np.mean(brownian_paths[:, -1])
sample_var = np.var(brownian_paths[:, -1], ddof=1)
theoretical_mean = 0
theoretical_var = maturity_time

print(f"Verification of Distribution at t = {maturity_time}:")
print(f"Sample mean: {sample_mean:.6f} (theoretical: {theoretical_mean})")
print(f"Sample variance: {sample_var:.6f} (theoretical: {theoretical_var})")
print(f"Mean error: {abs(sample_mean - theoretical_mean):.6f}")
print(f"Variance error: {abs(sample_var - theoretical_var):.6f}")

# Kolmogorov Smirnov
ks_statistic, p_value = stats.kstest(
    brownian_paths[:, -1] / np.sqrt(maturity_time),
    'norm'
)
print(f"\nKolmogorov-Smirnov test:")
print(f"KS statistic: {ks_statistic:.6f}")
print(f"p-value: {p_value:.6f}")
print(f"Result: {'PASS' if p_value > 0.05 else 'FAIL'} (normality at 5% significance)")
```

### 3. Interpretation



**Left plot (Sample Paths):**
- Paths start at origin ($W_0 = 0$)
- Continuous but "wiggly" — characteristic of Brownian motion
- Paths diverge as time increases (variance grows linearly)
- No visible pattern or trend (zero drift)

**Right plot (Distribution at Maturity):**
- Histogram (blue) matches theoretical Gaussian density (red dashed line)
- Centered at 0 with spread $\sqrt{T} = \sqrt{2} \approx 1.41$
- KS test confirms Gaussian distribution (p-value > 0.05)

**Key verification:** With 10,000 paths, sample statistics closely match theoretical values, validating:
- $\mathbb{E}[W_T] = 0$
- $\text{Var}(W_T) = T$
- $W_T \sim \mathcal{N}(0, T)$

## Example 2 Quadratic



This example verifies that quadratic variation equals $t$, a fundamental property for Itô calculus.

### 1. Theory Recap



**Theorem 1.3.10:** For any partition with mesh $|\Pi_n| \to 0$:

$$\sum_{i=0}^{n-1} (W_{t_{i+1}} - W_{t_i})^2 \xrightarrow{\mathbb{P}} T$$



This distinguishes Brownian motion from smooth functions (which have zero quadratic variation).

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
maturity_time = 1.0
num_steps_list = [10, 50, 100, 500, 1000, 5000]  # Different discretization levels
num_trials = 1000  # Number of independent Brownian paths

np.random.seed(42)

# Storage quadratic
qv_results = []

for num_steps in num_steps_list:
    dt = maturity_time / num_steps
    qv_paths = np.zeros(num_trials)
    
    for trial in range(num_trials):
        # Generate Brownian motion path
        dW = np.random.normal(0, np.sqrt(dt), size=num_steps)
        W = np.cumsum(np.insert(dW, 0, 0))
        
        # Compute quadratic variation
        increments_squared = np.diff(W)**2
        qv_paths[trial] = np.sum(increments_squared)
    
    qv_results.append({
        'num_steps': num_steps,
        'mean': np.mean(qv_paths),
        'std': np.std(qv_paths),
        'paths': qv_paths
    })

# Plot results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1 Convergence
means = [r['mean'] for r in qv_results]
stds = [r['std'] for r in qv_results]
steps = [r['num_steps'] for r in qv_results]

ax1.errorbar(steps, means, yerr=stds, fmt='o-', capsize=5, 
             label='Sample mean ± std', linewidth=2, markersize=8)
ax1.axhline(maturity_time, color='r', linestyle='--', linewidth=2, 
            label=f'Theoretical: $T = {maturity_time}$')
ax1.set_xlabel('Number of time steps $n$', fontsize=12)
ax1.set_ylabel('Quadratic Variation', fontsize=12)
ax1.set_title('Convergence of Quadratic Variation', fontsize=13)
ax1.set_xscale('log')
ax1.legend(fontsize=10)
ax1.grid(alpha=0.3)

# Plot 2 Distribution
finest_qv = qv_results[-1]['paths']
ax2.hist(finest_qv, bins=50, density=True, alpha=0.6, 
         color='steelblue', label=f'$n = {num_steps_list[-1]}$ steps')
ax2.axvline(maturity_time, color='r', linestyle='--', linewidth=2,
            label=f'Theoretical: $T = {maturity_time}$')
ax2.axvline(np.mean(finest_qv), color='green', linestyle='-', linewidth=2,
            label=f'Sample mean: {np.mean(finest_qv):.4f}')
ax2.set_xlabel('Quadratic Variation', fontsize=12)
ax2.set_ylabel('Density', fontsize=12)
ax2.set_title(f'Distribution of $[W]_T$ ({num_trials} trials)', fontsize=13)
ax2.legend(fontsize=10)
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Numerical
print("Quadratic Variation Convergence:")
print("-" * 70)
print(f"{'Steps':>10} {'Mean QV':>12} {'Std Dev':>12} {'Error':>12}")
print("-" * 70)
for result in qv_results:
    error = abs(result['mean'] - maturity_time)
    print(f"{result['num_steps']:>10} {result['mean']:>12.6f} {result['std']:>12.6f} {error:>12.6f}")
print("-" * 70)
print(f"Theoretical value: {maturity_time}")
```

### 3. Interpretation



**Left plot (Convergence):**
- As $n$ increases (finer discretization), mean quadratic variation converges to $T = 1$
- Standard deviation decreases with $n$ (by Theorem 1.3.10, variance $\sim 2T|\Pi_n| \to 0$)
- Error bars shrink as $n$ grows, confirming convergence in probability

**Right plot (Distribution at Fine Discretization):**
- Distribution is centered near $T = 1$ (green line)
- Sample mean (green) very close to theoretical value (red dashed)
- Narrow distribution indicates concentration around $T$

**Key insight:** Unlike smooth functions where $\sum (\Delta f)^2 \to 0$, Brownian motion has non-zero quadratic variation equal to $t$. This is the foundation for:
- Itô's lemma: $(dW_t)^2 = dt$
- Stochastic integration theory
- Correction terms in stochastic calculus

## Example 3 Self



This example verifies the scaling property: $W_{ct} \overset{d}{=} \sqrt{c} W_t$.

### 1. Theory Recap



**Theorem 1.3.8:** For any $c > 0$:

$$W_{ct} \overset{d}{=} \sqrt{c} W_t$$



This means Brownian motion has no intrinsic time scale.

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Parameters
T = 1.0
num_paths = 5000
num_steps = 1000
c_values = [0.25, 1, 4]  # Scaling factors

np.random.seed(0)

# Generate base
dt = T / num_steps
dW = np.random.normal(0, np.sqrt(dt), size=(num_paths, num_steps))
W = np.cumsum(np.hstack([np.zeros((num_paths, 1)), dW]), axis=1)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for idx, c in enumerate(c_values):
    ax = axes[idx]
    
    # Method 1: W_{cT} (sample at scaled time)
    scaled_time_index = int(c * num_steps)
    if scaled_time_index <= num_steps:
        W_ct = W[:, scaled_time_index]
    else:
        # Need to generate longer path
        extra_steps = scaled_time_index - num_steps
        dW_extra = np.random.normal(0, np.sqrt(dt), size=(num_paths, extra_steps))
        W_extended = np.cumsum(np.hstack([W, dW_extra]), axis=1)
        W_ct = W_extended[:, scaled_time_index]
    
    # Method 2: sqrt(c) * W_T (scaled in space)
    sqrt_c_W_T = np.sqrt(c) * W[:, -1]
    
    # Plot distributions
    bins = np.linspace(-3*np.sqrt(c*T), 3*np.sqrt(c*T), 50)
    
    ax.hist(W_ct, bins=bins, density=True, alpha=0.5, 
            color='blue', label=f'$W_{{{c}T}}$')
    ax.hist(sqrt_c_W_T, bins=bins, density=True, alpha=0.5, 
            color='red', label=f'$\sqrt{{{c}}} W_T$')
    
    # Theoretical N(0, cT) density
    x_range = np.linspace(bins[0], bins[-1], 200)
    theoretical_pdf = stats.norm(0, np.sqrt(c*T)).pdf(x_range)
    ax.plot(x_range, theoretical_pdf, 'k--', linewidth=2, 
            label=f'$\mathcal{{N}}(0, {c}T)$')
    
    ax.set_xlabel('Value', fontsize=11)
    ax.set_ylabel('Density', fontsize=11)
    ax.set_title(f'Scaling: $c = {c}$', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

plt.suptitle('Self-Similarity: $W_{ct} \overset{d}{=} \sqrt{c} W_t$', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Statistical tests
print("Self-Similarity Verification:")
print("-" * 70)
for c in c_values:
    scaled_time_index = min(int(c * num_steps), num_steps)
    W_ct = W[:, scaled_time_index]
    sqrt_c_W_T = np.sqrt(c) * W[:, -1]
    
    # Two-sample KS test
    ks_stat, p_value = stats.ks_2samp(W_ct, sqrt_c_W_T)
    
    print(f"c = {c}:")
    print(f"  Mean of W_{{cT}}: {np.mean(W_ct):.6f}")
    print(f"  Mean of sqrt(c)*W_T: {np.mean(sqrt_c_W_T):.6f}")
    print(f"  Var of W_{{cT}}: {np.var(W_ct):.6f}")
    print(f"  Var of sqrt(c)*W_T: {np.var(sqrt_c_W_T):.6f}")
    print(f"  KS test p-value: {p_value:.4f} ({'PASS' if p_value > 0.05 else 'FAIL'})")
    print()
```

### 3. Interpretation



**Three panels show different scaling factors:**
- $c = 0.25$: Compressed time $\leftrightarrow$ Compressed space
- $c = 1$: Identity (both distributions are $W_T$)
- $c = 4$: Extended time $\leftrightarrow$ Expanded space

**Key observations:**
- Blue and red histograms overlap almost perfectly
- Both match the theoretical Gaussian density (black dashed)
- KS test confirms distributions are statistically indistinguishable

**Implication:** You cannot distinguish "zooming in time" from "zooming in space" — Brownian motion looks the same at all scales. This is why volatility in finance scales as $\sqrt{T}$.

## Example 4 First



This example simulates the first hitting time $\tau_a = \inf\{t : W_t = a\}$ and verifies its distribution.

### 1. Theory Recap



**Theorem:** The first passage time $\tau_a$ has density:

$$f_{\tau_a}(t) = \frac{|a|}{\sqrt{2\pi t^3}} \exp\left(-\frac{a^2}{2t}\right), \quad t > 0$$



**Key facts:**
- $\mathbb{P}(\tau_a < \infty) = 1$ (recurrence)
- $\mathbb{E}[\tau_a] = \infty$ (infinite expected hitting time)

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
a = 1.0  # Barrier level
num_paths = 10_000
T_max = 5.0  # Maximum simulation time
num_steps = 5_000

np.random.seed(0)

# Storage first
first_passage_times = []

dt = T_max / num_steps
time_grid = np.linspace(0, T_max, num_steps + 1)

for _ in range(num_paths):
    # Generate Brownian motion path
    dW = np.random.normal(0, np.sqrt(dt), size=num_steps)
    W = np.cumsum(np.insert(dW, 0, 0))
    
    # Find first passage time
    crossing_indices = np.where(W >= a)[0]
    if len(crossing_indices) > 0:
        first_crossing_index = crossing_indices[0]
        first_passage_times.append(time_grid[first_crossing_index])

# Convert array
first_passage_times = np.array(first_passage_times)

# Plot distribution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Histogram first
counts, bins, _ = ax1.hist(first_passage_times, bins=50, density=True, 
                            alpha=0.6, color='steelblue', 
                            label='Simulated')

# Theoretical density
t_range = np.linspace(0.01, T_max, 500)
theoretical_density = (np.abs(a) / np.sqrt(2 * np.pi * t_range**3)) * \
                      np.exp(-a**2 / (2 * t_range))
ax1.plot(t_range, theoretical_density, 'r--', linewidth=2, 
         label='Theoretical')
ax1.set_xlabel('First Passage Time $\\tau_a$', fontsize=12)
ax1.set_ylabel('Density', fontsize=12)
ax1.set_title(f'Distribution of $\\tau_{{{a}}}$ ({len(first_passage_times)}/{num_paths} paths hit)', 
              fontsize=13)
ax1.legend(fontsize=11)
ax1.grid(alpha=0.3)
ax1.set_xlim(0, 5)

# Sample paths showing
ax2.set_title(f'Sample Paths Hitting Level $a = {a}$', fontsize=13)
np.random.seed(0)
for i in range(10):
    dW = np.random.normal(0, np.sqrt(dt), size=num_steps)
    W = np.cumsum(np.insert(dW, 0, 0))
    
    crossing_indices = np.where(W >= a)[0]
    if len(crossing_indices) > 0:
        first_crossing = crossing_indices[0]
        ax2.plot(time_grid[:first_crossing+1], W[:first_crossing+1], 
                alpha=0.6, linewidth=1.5)
        ax2.plot(time_grid[first_crossing], W[first_crossing], 
                'ro', markersize=6)

ax2.axhline(a, color='black', linestyle='--', linewidth=2, label=f'Barrier $a = {a}$')
ax2.set_xlabel('Time $t$', fontsize=12)
ax2.set_ylabel('$W_t$', fontsize=12)
ax2.legend(fontsize=10)
ax2.grid(alpha=0.3)
ax2.set_xlim(0, 5)

plt.tight_layout()
plt.show()

# Statistics
hitting_probability = len(first_passage_times) / num_paths
mean_fpt = np.mean(first_passage_times)
median_fpt = np.median(first_passage_times)

print(f"First Passage Time Statistics for a = {a}:")
print(f"Hitting probability by t = {T_max}: {hitting_probability:.4f}")
print(f"Sample mean of τ_a (conditional on hitting): {mean_fpt:.4f}")
print(f"Sample median of τ_a: {median_fpt:.4f}")
print(f"\nNote: Theoretical E[τ_a] = ∞, but conditional on hitting by T_max,")
print(f"      the sample mean is finite.")
```

### 3. Interpretation



**Left plot (Distribution):**
- Simulated histogram (blue) matches theoretical density (red dashed)
- Distribution is right-skewed with heavy tail
- Most passages occur early, but some take very long

**Right plot (Sample Paths):**
- Ten paths that hit level $a = 1$ before $t = 5$
- Red dots mark the first passage time for each path
- Paths exhibit diverse behavior — some hit quickly, others wander

**Key observations:**
- $\mathbb{P}(\tau_a \le T_{\text{max}})$ < 1, but $\mathbb{P}(\tau_a < \infty) = 1$ theoretically
- Sample mean is finite (because we condition on hitting within $T_{\max}$)
- True expected value $\mathbb{E}[\tau_a] = \infty$ cannot be verified by simulation

**Application:** This distribution is fundamental for:
- Barrier option pricing
- Credit risk modeling (default time)
- Risk management (Value-at-Risk)

## Example 5 Covariance



This example verifies the covariance formula $\mathbb{E}[W_s W_t] = \min(s,t)$.

### 1. Theory Recap



**Theorem 1.3.5:** For all $s, t \ge 0$:

$$\mathbb{E}[W_s W_t] = \min(s,t)$$



### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
T = 2.0
num_paths = 10_000
num_time_points = 20

np.random.seed(0)

# Generate time points
time_points = np.linspace(0, T, num_time_points + 1)
dt = T / num_time_points

# Generate Brownian
dW = np.random.normal(0, np.sqrt(dt), size=(num_paths, num_time_points))
W = np.cumsum(np.hstack([np.zeros((num_paths, 1)), dW]), axis=1)

# Compute sample
sample_cov = np.cov(W.T)

# Compute theoretical
theoretical_cov = np.minimum(time_points[:, None], time_points[None, :])

# Plot
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 4))

# Sample covariance
im1 = ax1.imshow(sample_cov, cmap='RdBu_r', origin='lower', 
                 extent=[0, T, 0, T], vmin=0, vmax=T)
ax1.set_title('Sample Covariance', fontsize=12)
ax1.set_xlabel('Time $t$', fontsize=11)
ax1.set_ylabel('Time $s$', fontsize=11)
plt.colorbar(im1, ax=ax1)

# Theoretical
im2 = ax2.imshow(theoretical_cov, cmap='RdBu_r', origin='lower', 
                 extent=[0, T, 0, T], vmin=0, vmax=T)
ax2.set_title('Theoretical Covariance: $\min(s,t)$', fontsize=12)
ax2.set_xlabel('Time $t$', fontsize=11)
ax2.set_ylabel('Time $s$', fontsize=11)
plt.colorbar(im2, ax=ax2)

# Difference error
diff = sample_cov - theoretical_cov
im3 = ax3.imshow(diff, cmap='RdBu_r', origin='lower', 
                 extent=[0, T, 0, T], vmin=-0.1, vmax=0.1)
ax3.set_title('Difference (Sample - Theoretical)', fontsize=12)
ax3.set_xlabel('Time $t$', fontsize=11)
ax3.set_ylabel('Time $s$', fontsize=11)
plt.colorbar(im3, ax=ax3)

plt.tight_layout()
plt.show()

# Numerical
test_pairs = [(0.5, 1.0), (1.0, 1.5), (0.25, 1.75)]
print("Covariance Verification at Specific Points:")
print("-" * 70)
print(f"{'s':>8} {'t':>8} {'Sample Cov':>15} {'Theoretical':>15} {'Error':>12}")
print("-" * 70)
for s, t in test_pairs:
    s_idx = int(s / T * num_time_points)
    t_idx = int(t / T * num_time_points)
    sample = sample_cov[s_idx, t_idx]
    theoretical = min(s, t)
    error = abs(sample - theoretical)
    print(f"{s:>8.2f} {t:>8.2f} {sample:>15.6f} {theoretical:>15.6f} {error:>12.6f}")
print("-" * 70)

# Overall error metric
rmse = np.sqrt(np.mean((sample_cov - theoretical_cov)**2))
max_error = np.max(np.abs(sample_cov - theoretical_cov))
print(f"\nOverall Error Metrics:")
print(f"RMSE: {rmse:.6f}")
print(f"Max absolute error: {max_error:.6f}")
```

### 3. Interpretation



**Three heatmaps:**
1. **Sample covariance** (left): Estimated from 10,000 simulated paths
2. **Theoretical covariance** (middle): $\min(s,t)$ structure
3. **Difference** (right): Nearly zero everywhere (small errors)

**Key observations:**
- Sample and theoretical covariances are visually identical
- Difference plot shows small random errors around zero
- Diagonal is $\min(t,t) = t$ (variance grows linearly)
- Off-diagonal reflects correlation structure

**Verification table** shows numerical agreement at specific $(s,t)$ pairs with errors < 0.01.

**Significance:** The $\min(s,t)$ covariance structure:
- Implies correlation $\text{Corr}(W_s, W_t) = \sqrt{s/t}$ for $s < t$
- Underlies the construction via Kolmogorov extension theorem
- Determines the geometry of Brownian paths

## Summary



These simulations verify key theoretical properties of Brownian motion:

1. **Example 1**: Gaussian distribution $W_t \sim \mathcal{N}(0,t)$ and continuous paths
2. **Example 2**: Quadratic variation $\langle W \rangle_t = t$ (foundation for Itô calculus)
3. **Example 3**: Self-similarity $W_{ct} \overset{d}{=} \sqrt{c} W_t$ (scale invariance)
4. **Example 4**: First passage time distribution and recurrence
5. **Example 5**: Covariance structure $\mathbb{E}[W_s W_t] = \min(s,t)$

**Key computational techniques:**
- Incremental construction via $\Delta W_i \sim \mathcal{N}(0, \Delta t)$
- Convergence testing as $n \to \infty$
- Statistical hypothesis testing (KS test, two-sample tests)
- Visualization of path properties

**Limitations of simulation:**
- Cannot prove $\mathbb{E}[\tau_a] = \infty$ (requires theory)
- Discretization introduces approximation error
- Nowhere differentiability is theoretical (numerically, paths appear smooth at fine scales)

For deeper exploration, consider:
- Implementing Euler-Maruyama scheme for SDEs
- Simulating geometric Brownian motion
- Computing option prices via Monte Carlo
- Exploring Brownian bridge and other conditioned processes

## References



- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
- Kloeden, P. E., & Platen, E. (1992). *Numerical Solution of Stochastic Differential Equations*. Springer.
- Shreeve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models*. Springer.
