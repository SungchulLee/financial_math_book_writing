# Random Walk



## Introduction



This section provides computational illustrations of the theoretical concepts developed in **Random Walk Foundations**. Through Monte Carlo simulation, we visualize key properties such as:

- The evolution of random walk paths

- Convergence of scaled random walks to Brownian motion (Donsker's theorem)

- The deterministic nature of quadratic variation

- Verification of moment formulas

These examples serve two purposes: (1) building intuition for abstract limit theorems, and (2) validating theoretical predictions numerically.

**Note:** These simulations are supplementary to the mathematical theory. Understanding the proofs in the previous section is essential; the code merely illustrates the results.

## Example 1 Single



This example simulates a single realization of a simple random walk and visualizes the path.

### 1. Theory Recap



The simple symmetric random walk is defined as:

$$S_n = \sum_{i=1}^n \xi_i, \quad \xi_i \in \{-1, +1\} \text{ with equal probability}$$



Key properties:

- $\mathbb{E}[S_n] = 0$

- $\text{Var}(S_n) = n$

- $[S]_n = n$ (quadratic variation)

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
num_flips = 100
p_heads = 0.5

# Simulate coin flips
np.random.seed(0)
flips = np.random.choice([1, -1], size=num_flips, p=[p_heads, 1-p_heads])

# Count heads tails
heads_count = np.sum(flips == 1)
tails_count = np.sum(flips == -1)
print(f"Heads: {heads_count}, Tails: {tails_count}")

# Cumulative sum
cumsum_flips = np.cumsum(np.insert(flips, 0, 0))

# Plot cumulative sum
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(cumsum_flips, marker='o', linestyle='-', markersize=3)
ax.set_xlabel("Number of Flips", fontsize=12)
ax.set_ylabel("Cumulative Sum $S_n$", fontsize=12)
ax.set_title("Single Realization of Simple Random Walk", fontsize=14)
ax.axhline(0, color='black', linestyle='--', linewidth=1)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 3. Interpretation



- **Path behavior**: The cumulative sum oscillates around zero (since $\mathbb{E}[S_n] = 0$)

- **Typical displacement**: After $n=100$ steps, $S_n$ is typically of order $\sqrt{n} \approx 10$ (consistent with $\text{Var}(S_n) = n$)

- **Irregularity**: The path has a "kink" at every step, foreshadowing the nowhere-differentiability of Brownian motion

## Example 2 Multiple



This example generates multiple independent random walk realizations to visualize the distribution of paths and confirm variance growth.

### 1. Theory Recap



For multiple independent realizations $S_n^{(1)}, \ldots, S_n^{(m)}$:

- Each path has $\mathbb{E}[S_n^{(i)}] = 0$

- Sample variance should approach $\text{Var}(S_n) = n$

- Paths are independent, so observing one path gives no information about others

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
num_flips = 100
num_paths = 10
p_heads = 0.5

np.random.seed(0)

# Simulate coin flips
# Shape num paths num
flips = np.random.choice([1, -1], size=(num_paths, num_flips), 
                        p=[p_heads, 1-p_heads])

# Compute cumulative
# Insert 0 beginning S
cumsum_flips = np.cumsum(np.insert(flips, 0, 0, axis=1), axis=1)

# Plot all paths
fig, ax = plt.subplots(figsize=(12, 6))
for i in range(num_paths):
    ax.plot(cumsum_flips[i], label=f'Path {i + 1}', alpha=0.7)
ax.set_xlabel("Number of Flips", fontsize=12)
ax.set_ylabel("Cumulative Sum $S_n$", fontsize=12)
ax.set_title(f"Multiple Independent Simple Random Walks ({num_paths} Paths)", fontsize=14)
ax.axhline(0, color='black', linestyle='--', linewidth=1)
ax.legend(loc='upper left', fontsize=9, ncol=2)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Display statistics
print("\nPath Statistics:")
print("-" * 60)
heads_count = np.sum(flips == 1, axis=1)
tails_count = np.sum(flips == -1, axis=1)
final_position = cumsum_flips[:, -1]

for i in range(num_paths):
    print(f"Path {i + 1}: Heads = {heads_count[i]:3d}, Tails = {tails_count[i]:3d}, "
          f"Final Position = {final_position[i]:+4d}")

# Verify variance
sample_mean = np.mean(final_position)
sample_var = np.var(final_position, ddof=1)
print(f"\nSample mean at n={num_flips}: {sample_mean:.2f} (theoretical: 0)")
print(f"Sample variance at n={num_flips}: {sample_var:.2f} (theoretical: {num_flips})")
```

### 3. Interpretation



- **Path diversity**: Each colored line represents an independent realization; they diverge due to randomness

- **Variance growth**: The "spread" of paths increases with $n$, consistent with $\text{Var}(S_n) = n$

- **Zero mean**: Although individual paths wander far from zero, the average across paths is close to 0

- **No "memory"**: Past behavior doesn't predict future behavior (Markov property)

## Example 3 Scaled



This example demonstrates **Donsker's theorem** by showing how the scaled random walk $S^{(n)}(t) = S_{[nt]}/\sqrt{n}$ converges to Brownian motion as $n \to \infty$.

### 1. Theory Recap



**Donsker's Invariance Principle** states:

$$S^{(n)}(t) = \frac{1}{\sqrt{n}} S_{[nt]} \Rightarrow W_t \quad \text{in } C[0,T]$$



As $n$ increases:

- Paths become smoother (more interpolation points)

- Variance at time $t$ stabilizes at $t$: $\text{Var}(S^{(n)}(t)) \to t$

- Distribution converges to Gaussian: $S^{(n)}(t) \sim \mathcal{N}(0, t)$

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
T = 1.0  # Time horizon
num_steps_list = [10, 50, 100, 500, 1000]  # Different discretization levels
num_paths = 5  # Number of paths per discretization level

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for idx, n in enumerate(num_steps_list):
    np.random.seed(42)  # Fixed seed for reproducibility
    dt = T / n
    t = np.linspace(0, T, n+1)
    
    ax = axes[idx]
    
    for path_idx in range(num_paths):
        # Generate random walk: S_n = sum of +1/-1 steps
        xi = np.random.choice([1, -1], size=n)
        S = np.cumsum(np.insert(xi, 0, 0))
        
        # Scale: divide by sqrt(n)
        S_scaled = S / np.sqrt(n)
        
        ax.plot(t, S_scaled, alpha=0.7, linewidth=1.5)
    
    # Formatting
    ax.set_title(f'$n = {n}$ steps', fontsize=11)
    ax.set_xlabel('Time $t$', fontsize=10)
    ax.set_ylabel(r'$S^{(n)}(t) = S_{[nt]} / \sqrt{n}$', fontsize=10)
    ax.axhline(0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.grid(alpha=0.3)
    ax.set_ylim(-2.5, 2.5)

# Remove extra subplot
axes[-1].axis('off')

plt.suptitle('Scaled Random Walk Converging to Brownian Motion (Donsker\'s Theorem)', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 3. Interpretation



- **$n = 10$**: Paths are jagged with visible jumps of size $1/\sqrt{10} \approx 0.32$

- **$n = 50$**: Smoother, jumps are $1/\sqrt{50} \approx 0.14$ 
 
- **$n = 100$**: Even smoother, jumps are $1/\sqrt{100} = 0.1$

- **$n = 500, 1000$**: Paths resemble continuous Brownian motion with jumps $\approx 0.05, 0.03$

**Key observations**:

1. As $n \to \infty$, paths become continuous (no visible jumps)

2. Variance at time $t$ remains approximately $t$ across all $n$

3. The limiting process exhibits the characteristic "wiggliness" of Brownian motion

**Verification of Proposition 1.1.5**:
At $t = 1$, the scaled random walk has variance:

$$\text{Var}(S^{(n)}(1)) = \frac{[n]}{n} \approx 1$$


which matches $\text{Var}(W_1) = 1$ for Brownian motion.

## Example 4



This example illustrates the fundamental property that quadratic variation grows linearly with time, not quadratically.

### 1. Theory Recap



**Proposition 1.1.3** states that for the simple random walk:

$$[S]_n = \sum_{i=1}^n (S_i - S_{i-1})^2 = \sum_{i=1}^n \xi_i^2 = n$$



This is **deterministic** (not random!), unlike the path itself. In the continuous limit:

$$\langle W \rangle_t = t$$



This is the foundation for Itô calculus: $(dW_t)^2 = dt$, not 0.

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
num_steps = 1000
num_paths = 20

np.random.seed(0)

# Storage quadratic
QV_paths = np.zeros((num_paths, num_steps))

for path_idx in range(num_paths):
    # Generate random walk
    xi = np.random.choice([1, -1], size=num_steps)
    S = np.cumsum(np.insert(xi, 0, 0))
    
    # Compute quadratic variation: sum of squared increments
    increments_squared = np.diff(S)**2
    QV = np.cumsum(increments_squared)
    QV_paths[path_idx, :] = QV

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1 Sample paths
n_display = 10
for i in range(n_display):
    ax1.plot(range(1, num_steps+1), QV_paths[i, :], alpha=0.5)
ax1.plot(range(1, num_steps+1), range(1, num_steps+1), 
         'r--', linewidth=2, label='$[S]_n = n$ (theoretical)')
ax1.set_xlabel('Time step $n$', fontsize=12)
ax1.set_ylabel('Quadratic Variation $[S]_n$', fontsize=12)
ax1.set_title('Quadratic Variation Paths', fontsize=13)
ax1.legend(fontsize=10)
ax1.grid(alpha=0.3)

# Plot 2 Mean
mean_QV = np.mean(QV_paths, axis=0)
std_QV = np.std(QV_paths, axis=0)
time_steps = range(1, num_steps+1)

ax2.plot(time_steps, mean_QV, 'b-', linewidth=2, label='Mean $[S]_n$')
ax2.fill_between(time_steps, mean_QV - std_QV, mean_QV + std_QV, 
                 alpha=0.3, label='±1 std dev')
ax2.plot(time_steps, time_steps, 'r--', linewidth=2, label='$n$ (theoretical)')
ax2.set_xlabel('Time step $n$', fontsize=12)
ax2.set_ylabel('Quadratic Variation $[S]_n$', fontsize=12)
ax2.set_title(f'Average Quadratic Variation ({num_paths} paths)', fontsize=13)
ax2.legend(fontsize=10)
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Verify quadratic
print(f"\nVerification: [S]_n = n for all paths")
print(f"Mean [S]_{num_steps} = {mean_QV[-1]:.2f}")
print(f"Theoretical value = {num_steps}")
print(f"Difference = {abs(mean_QV[-1] - num_steps):.6f}")
print(f"\nAll paths have [S]_n = n exactly: {np.allclose(QV_paths[:, -1], num_steps)}")
```

### 3. Interpretation



**Left plot**: 

- All paths (colored lines) lie **exactly** on the red dashed line $[S]_n = n$

- This confirms Proposition 1.1.3: quadratic variation is deterministic, not random

- Unlike the random walk itself (which fluctuates), $[S]_n$ has zero variance

**Right plot**:

- Mean across paths equals $n$ (blue line matches red dashed line)

- Standard deviation is zero (the blue shaded region has zero width)

- This is unique to random walks; smooth functions have $[f]_n \to 0$

**Contrast with smooth functions**:

For a differentiable function $f(t)$:

$$\sum_{i=1}^n (f(i/n) - f((i-1)/n))^2 \approx \sum_{i=1}^n (f'(i/n))^2 (1/n)^2 = O(1/n) \to 0$$



For Brownian motion:

$$\lim_{|\Delta t_i| \to 0} \sum_{i=1}^n (W_{t_{i+1}} - W_{t_i})^2 = t \neq 0$$



This is why Itô's formula has the correction term $\frac{1}{2}\sigma^2 S^2 dt$.

## Example 5 Verifying



This example numerically confirms the theoretical variance formulas from Proposition 1.1.1.

### 1. Theory Recap



For the symmetric random walk:

- $\text{Var}(S_n) = n$

- $\mathbb{E}[S_n^4] = 3n^2 - 2n$

We verify these using Monte Carlo simulation.

### 2. Python Implementa



```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
num_trials = 10000  # Number of independent random walks
max_steps = 100

np.random.seed(0)

# Storage
variance_empirical = np.zeros(max_steps)
fourth_moment_empirical = np.zeros(max_steps)

for n in range(1, max_steps + 1):
    # Generate many independent random walks of length n
    xi = np.random.choice([1, -1], size=(num_trials, n))
    S_n = np.sum(xi, axis=1)  # Terminal value of each random walk
    
    # Compute sample moments
    variance_empirical[n-1] = np.var(S_n, ddof=1)
    fourth_moment_empirical[n-1] = np.mean(S_n**4)

# Theoretical values
n_values = np.arange(1, max_steps + 1)
variance_theoretical = n_values
fourth_moment_theoretical = 3 * n_values**2 - 2 * n_values

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Variance plot
ax1.plot(n_values, variance_empirical, 'b-', alpha=0.7, label='Empirical')
ax1.plot(n_values, variance_theoretical, 'r--', linewidth=2, label='Theoretical: $n$')
ax1.set_xlabel('Number of steps $n$', fontsize=12)
ax1.set_ylabel('Variance', fontsize=12)
ax1.set_title(f'Variance of $S_n$ ({num_trials} trials)', fontsize=13)
ax1.legend(fontsize=11)
ax1.grid(alpha=0.3)

# moment plot
ax2.plot(n_values, fourth_moment_empirical, 'b-', alpha=0.7, label='Empirical')
ax2.plot(n_values, fourth_moment_theoretical, 'r--', linewidth=2, 
         label='Theoretical: $3n^2 - 2n$')
ax2.set_xlabel('Number of steps $n$', fontsize=12)
ax2.set_ylabel('Fourth moment $\mathbb{E}[S_n^4]$', fontsize=12)
ax2.set_title(f'Fourth Moment of $S_n$ ({num_trials} trials)', fontsize=13)
ax2.legend(fontsize=11)
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Numerical
print(f"Verification at n = {max_steps}:")
print(f"Empirical variance: {variance_empirical[-1]:.4f}")
print(f"Theoretical variance: {variance_theoretical[-1]}")
print(f"Relative error: {abs(variance_empirical[-1] - variance_theoretical[-1]) / variance_theoretical[-1] * 100:.2f}%")
print()
print(f"Empirical 4th moment: {fourth_moment_empirical[-1]:.2f}")
print(f"Theoretical 4th moment: {fourth_moment_theoretical[-1]:.2f}")
print(f"Relative error: {abs(fourth_moment_empirical[-1] - fourth_moment_theoretical[-1]) / fourth_moment_theoretical[-1] * 100:.2f}%")
```

### 3. Interpretation



- **Left plot**: Blue line (empirical variance) closely tracks red line (theoretical $n$)

- **Right plot**: Fourth moment follows $3n^2 - 2n$ curve accurately

- **Convergence**: With 10,000 trials, relative error is typically < 1%

This confirms Proposition 1.1.1 numerically and demonstrates the power of the Law of Large Numbers.

## Summary



These simulations illustrate several key theoretical results:

1. **Example 1-2**: Basic random walk behavior—zero mean, growing variance, path irregularity

2. **Example 3**: Donsker's theorem—scaled random walks converge to continuous Brownian motion

3. **Example 4**: Quadratic variation is deterministic and equals $t$, unlike smooth functions

4. **Example 5**: Monte Carlo verification of moment formulas

**Key takeaway**: While these simulations build intuition, they cannot replace rigorous proofs. Donsker's theorem requires functional analysis (weak convergence in $C[0,T]$, tightness arguments), which is proven in the next section.

**For further exploration**:

- Modify `p_heads` in Examples 1-2 to study asymmetric random walks

- Increase `num_paths` in Example 3 to see the distribution of Brownian paths

- Study higher moments or other statistics using the framework above

## References



- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
- Kloeden, P. E., & Platen, E. (1992). *Numerical Solution of Stochastic Differential Equations*. Springer.
