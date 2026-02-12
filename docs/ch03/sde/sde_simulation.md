# SDE Simulation


Most SDEs lack closed-form solutions, making **numerical simulation** essential for practical applications. This section develops simulation methods from first principles, starting with an intuitive discrete approximation and progressing to rigorous numerical schemes.

---

## From Coin Flips to Brownian Motion


### 1. Discrete Random Walk


Before simulating continuous SDEs, we build intuition through a **discrete random walk** that approximates Brownian motion.

**Setup:** Divide time interval $[0, T]$ into $n$ equal steps of size $\Delta t = T/n$.

$$
\begin{array}{ccccccccccc}
S_0 && S_1 && S_2 && \cdots && S_n \\
t_0 & < & t_1 & < & t_2 & < & \cdots & < & t_n
\end{array}
$$

### 2. Discretizing GBM


For the geometric Brownian motion SDE:

$$
\frac{dS}{S} = \mu\,dt + \sigma\,dB_t
$$

we discretize at times $t_0 < t_1 < t_2 < \cdots < t_n < t_{n+1}$:

$$
\begin{array}{ccccccccccccc}
\frac{dS}{S} & = & \mu & dt & + & \sigma & dB_t \\
\downarrow && \downarrow & \downarrow && \downarrow & \downarrow \\
\frac{S_{n+1} - S_n}{S_n} && \mu & \Delta t && \sigma & \Delta B_n
\end{array}
$$

where $\Delta B_n = B_{t_{n+1}} - B_{t_n} \sim \mathcal{N}(0, \Delta t)$.

**Key insight:** $\Delta B_n \approx \pm\sqrt{\Delta t}$ with equal probability (coin flip).

### 3. Paper-and-Pencil Simulation


**Example:** Simulate GBM with $S_0 = 100$, $\mu = 0.10$, $\sigma = 0.30$, $T = 1$, $n = 10$ (so $\Delta t = 1/10$).

**Updating rule:**

$$
\begin{array}{ccccccccccccc}
\frac{dS}{S} & = & \mu & dt & + & \sigma & dB_t \\
\uparrow && \uparrow & \uparrow && \uparrow & \uparrow \\
\frac{S_{n+1} - S_n}{S_n} && 0.10 & \frac{1}{10} && 0.30 & \pm\sqrt{\frac{1}{10}}
\end{array}
$$

**Simulation table:**

$$
\begin{array}{lrrrrrrrrrrrrrr}
\text{Time} & 0/10 & 1/10 & 2/10 & 3/10 \\
\text{Coin flip} & - & H & H & T \\
\text{Conversion} & - & 1 & 1 & -1 \\
\text{Cum sum} & 0 & 1 & 2 & 1 \\
B_t & 0 & \frac{1}{\sqrt{10}} & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{10}} \\
dt & - & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} \\
dB_t = B_t - B_{t-dt} & - & \frac{1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} \\
\mu \cdot dt + \sigma \cdot dB_t & - & \frac{0.1}{10} + \frac{0.3}{\sqrt{10}} & \frac{0.1}{10} + \frac{0.3}{\sqrt{10}} & \frac{0.1}{10} - \frac{0.3}{\sqrt{10}} \\
S_{t-dt} \cdot (\mu \cdot dt + \sigma \cdot dB_t) & - & 10.4868 & 11.5866 & -10.3602 \\
S_t = S_{t-dt} + S_{t-dt} \cdot (\mu \cdot dt + \sigma \cdot dB_t) & 100 & 110.4868 & 122.0734 & 111.7132 \\
\\
\text{Time} & 4/10 & 5/10 & 6/10 & 7/10 \\
\text{Coin flip} & H & T & T & H \\
\text{Conversion} & 1 & -1 & -1 & 1 \\
\text{Cum sum} & 2 & 1 & 0 & 1 \\
B_t & \frac{2}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{0}{\sqrt{10}} & \frac{1}{\sqrt{10}} \\
dt & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} & \frac{1}{10} \\
dB_t = B_t - B_{t-dt} & \frac{1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} & \frac{1}{\sqrt{10}} \\
\mu \cdot dt + \sigma \cdot dB_t & \frac{0.1}{10} + \frac{0.3}{\sqrt{10}} & \frac{0.1}{10} - \frac{0.3}{\sqrt{10}} & \frac{0.1}{10} - \frac{0.3}{\sqrt{10}} & \frac{0.1}{10} + \frac{0.3}{\sqrt{10}} \\
S_{t-dt} \cdot (\mu \cdot dt + \sigma \cdot dB_t) & 11.7152 & -10.4752 & -9.5861 & 10.8399 \\
S_t = S_{t-dt} + S_{t-dt} \cdot (\mu \cdot dt + \sigma \cdot dB_t) & 123.4284 & 112.9532 & 103.3671 & 114.2070 \\
\\
\text{Time} && 8/10 & 9/10 & 10/10 \\
\text{Coin flip} && H & H & T \\
\text{Conversion} && 1 & 1 & -1 \\
\text{Cum sum} && 2 & 3 & 2 \\
B_t && \frac{2}{\sqrt{10}} & \frac{3}{\sqrt{10}} & \frac{2}{\sqrt{10}} \\
dt && \frac{1}{10} & \frac{1}{10} & \frac{1}{10} \\
dB_t = B_t - B_{t-dt} && \frac{1}{\sqrt{10}} & \frac{1}{\sqrt{10}} & \frac{-1}{\sqrt{10}} \\
\mu \cdot dt + \sigma \cdot dB_t && \frac{0.1}{10} + \frac{0.3}{\sqrt{10}} & \frac{0.1}{10} + \frac{0.3}{\sqrt{10}} & \frac{0.1}{10} - \frac{0.3}{\sqrt{10}} \\
S_{t-dt} \cdot (\mu \cdot dt + \sigma \cdot dB_t) && 11.9767 & 13.2327 & -11.8320 \\
S_t = S_{t-dt} + S_{t-dt} \cdot (\mu \cdot dt + \sigma \cdot dB_t) && 126.1837 & 139.4164 & 127.5844
\end{array}
$$

**Result:** Starting from $S_0 = 100$, we end at $S_T \approx 127.58$ after 10 coin flips.

### 4. From Discrete to Continuous


As $n \to \infty$ (i.e., $\Delta t \to 0$):

- The random walk converges to Brownian motion (by **Donsker's theorem**)
- The discrete stock prices converge to the solution of the SDE
- Coin flips $\{\pm 1\}$ → Gaussian increments $\mathcal{N}(0, \Delta t)$

This limiting process is the foundation of **Euler-Maruyama discretization**.

---

## Euler-Maruyama Scheme


### 1. Derivation


For a general SDE:

$$
dX_t = b(t, X_t)\,dt + \sigma(t, X_t)\,dW_t, \quad X_0 = x
$$

Integrate from $t_n$ to $t_{n+1}$:

$$
X_{t_{n+1}} = X_{t_n} + \int_{t_n}^{t_{n+1}} b(s, X_s)\,ds + \int_{t_n}^{t_{n+1}} \sigma(s, X_s)\,dW_s
$$

**Euler approximation:** Replace $X_s$ with $X_{t_n}$ (constant on $[t_n, t_{n+1}]$):

$$
X_{t_{n+1}} \approx X_{t_n} + b(t_n, X_{t_n})\Delta t + \sigma(t_n, X_{t_n})\Delta W_n
$$

where $\Delta t = t_{n+1} - t_n$ and $\Delta W_n = W_{t_{n+1}} - W_{t_n} \sim \mathcal{N}(0, \Delta t)$.

**Euler-Maruyama scheme:**

$$
\boxed{
X_{n+1} = X_n + b(t_n, X_n)\Delta t + \sigma(t_n, X_n)\Delta W_n
}
$$

### 2. Implementation


**Algorithm:**

1. Set time grid: $t_n = n\Delta t$ for $n = 0, 1, \ldots, N$
2. Initialize: $X_0 = x$
3. For $n = 0, 1, \ldots, N-1$:
   - Generate $\Delta W_n \sim \mathcal{N}(0, \Delta t)$
   - Update: $X_{n+1} = X_n + b(t_n, X_n)\Delta t + \sigma(t_n, X_n)\Delta W_n$

### 3. Python Implementation: General SDE


```python
import numpy as np
import matplotlib.pyplot as plt

def euler_maruyama(b, sigma, X0, T, N, num_paths=1):
    """
    Simulate SDE using Euler-Maruyama scheme.
    
    Parameters:
    -----------
    b : callable
        Drift function b(t, x)
    sigma : callable
        Diffusion function sigma(t, x)
    X0 : float
        Initial condition
    T : float
        Terminal time
    N : int
        Number of time steps
    num_paths : int
        Number of sample paths
    
    Returns:
    --------
    t : array
        Time grid
    X : array
        Simulated paths (num_paths x N+1)
    """
    dt = T / N
    t = np.linspace(0, T, N+1)
    
    X = np.zeros((num_paths, N+1))
    X[:, 0] = X0
    
    for path in range(num_paths):
        for n in range(N):
            dW = np.sqrt(dt) * np.random.randn()
            X[path, n+1] = X[path, n] + b(t[n], X[path, n]) * dt + \
                          sigma(t[n], X[path, n]) * dW
    
    return t, X
```

### 4. Example: Geometric Brownian Motion


```python
# GBM parameters
mu = 0.1
sig = 0.2
S0 = 100

# Drift and diffusion for GBM
b = lambda t, S: mu * S
sigma = lambda t, S: sig * S

# Simulate
T = 1.0
N = 1000
num_paths = 20

t, S = euler_maruyama(b, sigma, S0, T, N, num_paths)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
for path in range(num_paths):
    ax.plot(t, S[path], alpha=0.6)
ax.axhline(S0, color='black', linestyle='--', alpha=0.5, label='$S_0$')
ax.set_xlabel('Time t')
ax.set_ylabel('Stock Price $S_t$')
ax.set_title('GBM via Euler-Maruyama')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 5. Example: Ornstein-Uhlenbeck Process


```python
# OU parameters
kappa = 2.0
theta = 1.0
sig = 0.3
X0 = 0.5

# Drift and diffusion for OU
b = lambda t, X: kappa * (theta - X)
sigma = lambda t, X: sig

# Simulate
t, X = euler_maruyama(b, sigma, X0, T=2.0, N=1000, num_paths=20)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
for path in range(20):
    ax.plot(t, X[path], alpha=0.6)
ax.axhline(theta, color='red', linestyle='--', linewidth=2, 
           label=f'Long-term mean θ = {theta}')
ax.set_xlabel('Time t')
ax.set_ylabel('$X_t$')
ax.set_title('Ornstein-Uhlenbeck Process via Euler-Maruyama')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## Convergence Analysis


### 1. Strong Convergence


**Definition:** A numerical scheme has **strong convergence of order $\gamma$** if:

$$
\mathbb{E}[|X_T - X_T^{\Delta t}|] = O(\Delta t^\gamma)
$$

where $X_T$ is the true solution and $X_T^{\Delta t}$ is the numerical approximation.

**Theorem:** Under Lipschitz and growth conditions on $b$ and $\sigma$, the Euler-Maruyama scheme has **strong order $\gamma = 0.5$**:

$$
\mathbb{E}[|X_T - X_T^{\Delta t}|] \leq C\sqrt{\Delta t}
$$

**Interpretation:** To reduce error by factor of 10, we need $\Delta t \to \Delta t / 100$ (100× more steps).

### 2. Weak Convergence


**Definition:** A scheme has **weak convergence of order $\beta$** if for all sufficiently smooth functions $g$:

$$
|\mathbb{E}[g(X_T)] - \mathbb{E}[g(X_T^{\Delta t})]| = O(\Delta t^\beta)
$$

**Theorem:** Euler-Maruyama has **weak order $\beta = 1.0$**:

$$
|\mathbb{E}[g(X_T)] - \mathbb{E}[g(X_T^{\Delta t})]| \leq C\Delta t
$$

**Practical implication:** For computing expectations (e.g., option prices), Euler-Maruyama converges faster than for pathwise accuracy.

### 3. Numerical Verification of Convergence


```python
def convergence_test_GBM():
    """Test strong convergence order for GBM."""
    mu, sig, S0 = 0.1, 0.2, 100
    T = 1.0
    
    # Exact solution
    np.random.seed(42)
    W_T = np.random.randn(10000) * np.sqrt(T)
    S_exact = S0 * np.exp((mu - 0.5*sig**2)*T + sig*W_T)
    
    # Test different step sizes
    N_values = [10, 20, 50, 100, 200, 500, 1000]
    errors = []
    
    for N in N_values:
        dt = T / N
        # Use same Brownian path
        np.random.seed(42)
        t = np.linspace(0, T, N+1)
        S = np.zeros((10000, N+1))
        S[:, 0] = S0
        
        for path in range(10000):
            np.random.seed(42 + path)
            for n in range(N):
                dW = np.sqrt(dt) * np.random.randn()
                S[path, n+1] = S[path, n] + mu*S[path, n]*dt + sig*S[path, n]*dW
        
        error = np.mean(np.abs(S[:, -1] - S_exact))
        errors.append(error)
    
    # Log-log plot
    dt_values = T / np.array(N_values)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.loglog(dt_values, errors, 'o-', label='Euler-Maruyama')
    ax.loglog(dt_values, 10*np.sqrt(dt_values), '--', label='$O(\sqrt{\Delta t})$')
    ax.set_xlabel('Step size $\Delta t$')
    ax.set_ylabel('Strong error')
    ax.set_title('Strong Convergence of Euler-Maruyama')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
```

---

## Milstein Scheme


### 1. Motivation


Euler-Maruyama has strong order 0.5. Can we do better?

**Idea:** Include more terms from the **Itô-Taylor expansion**.

### 2. Itô-Taylor Expansion


For $Y_t = X_{t+\Delta t}$, expand using Itô's lemma:

$$
\begin{align}
dX_t &= b(X_t)\,dt + \sigma(X_t)\,dW_t \\
d\sigma(X_t) &= \sigma'(X_t)\,dX_t + \frac{1}{2}\sigma''(X_t)(dX_t)^2 \\
&= \sigma'(X_t)[b(X_t)\,dt + \sigma(X_t)\,dW_t] + \frac{1}{2}\sigma''(X_t)\sigma^2(X_t)\,dt
\end{align}
$$

Keeping terms up to order $\Delta t$:

$$
X_{t+\Delta t} = X_t + b(X_t)\Delta t + \sigma(X_t)\Delta W + \frac{1}{2}\sigma(X_t)\sigma'(X_t)[(\Delta W)^2 - \Delta t]
$$

### 3. Milstein Scheme


$$
\boxed{
X_{n+1} = X_n + b(X_n)\Delta t + \sigma(X_n)\Delta W_n + \frac{1}{2}\sigma(X_n)\sigma'(X_n)[(\Delta W_n)^2 - \Delta t]
}
$$

**Key term:** $(\Delta W_n)^2 - \Delta t$ captures the **quadratic variation** correction.

### 4. Convergence


**Theorem:** The Milstein scheme has:
- **Strong order** $\gamma = 1.0$ (vs. 0.5 for Euler-Maruyama)
- **Weak order** $\beta = 1.0$ (same as Euler-Maruyama)

### 5. Python Implementation


```python
def milstein(b, sigma, sigma_prime, X0, T, N, num_paths=1):
    """
    Simulate SDE using Milstein scheme.
    
    Parameters:
    -----------
    b : callable
        Drift function b(t, x)
    sigma : callable
        Diffusion function sigma(t, x)
    sigma_prime : callable
        Derivative of diffusion: d(sigma)/dx
    X0 : float
        Initial condition
    T : float
        Terminal time
    N : int
        Number of time steps
    num_paths : int
        Number of sample paths
    
    Returns:
    --------
    t : array
        Time grid
    X : array
        Simulated paths
    """
    dt = T / N
    t = np.linspace(0, T, N+1)
    
    X = np.zeros((num_paths, N+1))
    X[:, 0] = X0
    
    for path in range(num_paths):
        for n in range(N):
            dW = np.sqrt(dt) * np.random.randn()
            X_n = X[path, n]
            
            # Milstein correction term
            correction = 0.5 * sigma(t[n], X_n) * sigma_prime(t[n], X_n) * \
                        (dW**2 - dt)
            
            X[path, n+1] = X_n + b(t[n], X_n)*dt + sigma(t[n], X_n)*dW + correction
    
    return t, X
```

### 6. Example: GBM with Milstein


```python
# GBM: sigma(S) = sig * S, so sigma'(S) = sig
mu, sig, S0 = 0.1, 0.2, 100

b = lambda t, S: mu * S
sigma = lambda t, S: sig * S
sigma_prime = lambda t, S: sig  # Derivative of (sig * S) w.r.t. S

# Simulate
t_mil, S_mil = milstein(b, sigma, sigma_prime, S0, T=1.0, N=100, num_paths=20)
t_em, S_em = euler_maruyama(b, sigma, S0, T=1.0, N=100, num_paths=20)

# Compare
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

for path in range(20):
    ax1.plot(t_em, S_em[path], alpha=0.6)
ax1.set_title('Euler-Maruyama (100 steps)')
ax1.set_xlabel('Time t')
ax1.set_ylabel('$S_t$')
ax1.grid(True, alpha=0.3)

for path in range(20):
    ax2.plot(t_mil, S_mil[path], alpha=0.6)
ax2.set_title('Milstein (100 steps)')
ax2.set_xlabel('Time t')
ax2.set_ylabel('$S_t$')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Exact Simulation (When Possible)


### 1. Geometric Brownian Motion


For GBM, we have the **exact solution**:

$$
S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
$$

**Exact simulation:** Generate $W_t$ directly and compute $S_t$.

```python
def exact_GBM(S0, mu, sigma, T, N, num_paths):
    """Exact simulation of GBM."""
    dt = T / N
    t = np.linspace(0, T, N+1)
    
    S = np.zeros((num_paths, N+1))
    S[:, 0] = S0
    
    for path in range(num_paths):
        W = np.cumsum(np.concatenate([[0], np.sqrt(dt)*np.random.randn(N)]))
        S[path, :] = S0 * np.exp((mu - 0.5*sigma**2)*t + sigma*W)
    
    return t, S
```

**Advantage:** No discretization error; only Monte Carlo error remains.

### 2. Ornstein-Uhlenbeck Process


The OU process also has an exact solution:

$$
X_t = X_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t}) + \sigma \int_0^t e^{-\kappa(t-s)}\,dW_s
$$

The stochastic integral is Gaussian with known mean and variance.

**Exact simulation (conditional distribution):**

$$
X_{t+\Delta t} | X_t \sim \mathcal{N}\left(X_t e^{-\kappa\Delta t} + \theta(1 - e^{-\kappa\Delta t}), \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\Delta t})\right)
$$

```python
def exact_OU(X0, kappa, theta, sigma, T, N, num_paths):
    """Exact simulation of OU process."""
    dt = T / N
    t = np.linspace(0, T, N+1)
    
    X = np.zeros((num_paths, N+1))
    X[:, 0] = X0
    
    # Precompute constants
    exp_kappa_dt = np.exp(-kappa * dt)
    mean_coef = 1 - exp_kappa_dt
    var = (sigma**2 / (2*kappa)) * (1 - np.exp(-2*kappa*dt))
    std = np.sqrt(var)
    
    for path in range(num_paths):
        for n in range(N):
            mean = X[path, n] * exp_kappa_dt + theta * mean_coef
            X[path, n+1] = mean + std * np.random.randn()
    
    return t, X
```

### 3. Comparison: Exact vs. Euler-Maruyama


```python
# Parameters
kappa, theta, sigma, X0 = 2.0, 1.0, 0.3, 0.5
T, N = 2.0, 50

# Simulate
t_exact, X_exact = exact_OU(X0, kappa, theta, sigma, T, N, num_paths=5000)
t_em, X_em = euler_maruyama(lambda t,x: kappa*(theta-x), 
                            lambda t,x: sigma, 
                            X0, T, N, num_paths=5000)

# Compare distributions at T
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(X_exact[:, -1], bins=50, alpha=0.5, density=True, label='Exact')
ax.hist(X_em[:, -1], bins=50, alpha=0.5, density=True, label='Euler-Maruyama')
ax.set_xlabel('$X_T$')
ax.set_ylabel('Density')
ax.set_title(f'Distribution of $X_T$ (N={N} steps)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Exact: mean={np.mean(X_exact[:,-1]):.4f}, std={np.std(X_exact[:,-1]):.4f}")
print(f"E-M:   mean={np.mean(X_em[:,-1]):.4f}, std={np.std(X_em[:,-1]):.4f}")
```

---

## Advanced Schemes


### 1. Stochastic Runge-Kutta Methods


Higher-order schemes based on Runge-Kutta ideas.

**Example (Order 1.5 strong scheme):**

$$
\begin{align}
K_1 &= b(X_n)\Delta t + \sigma(X_n)\Delta W_n \\
\bar{X} &= X_n + K_1 \\
X_{n+1} &= X_n + \frac{1}{2}[b(X_n) + b(\bar{X})]\Delta t + \sigma(X_n)\Delta W_n
\end{align}
$$

### 2. Predictor-Corrector Methods


**Idea:** Use Euler to predict, then correct using midpoint rule.

```python
def predictor_corrector(b, sigma, X0, T, N, num_paths=1):
    """Heun's method (predictor-corrector) for SDEs."""
    dt = T / N
    t = np.linspace(0, T, N+1)
    
    X = np.zeros((num_paths, N+1))
    X[:, 0] = X0
    
    for path in range(num_paths):
        for n in range(N):
            dW = np.sqrt(dt) * np.random.randn()
            
            # Predictor step (Euler)
            X_pred = X[path, n] + b(t[n], X[path, n])*dt + \
                     sigma(t[n], X[path, n])*dW
            
            # Corrector step
            X[path, n+1] = X[path, n] + \
                          0.5*(b(t[n], X[path,n]) + b(t[n+1], X_pred))*dt + \
                          0.5*(sigma(t[n], X[path,n]) + sigma(t[n+1], X_pred))*dW
    
    return t, X
```

---

## Multidimensional SDEs


### 1. System of SDEs


For $X_t = (X_t^1, \ldots, X_t^d)$ driven by $W_t = (W_t^1, \ldots, W_t^m)$:

$$
dX_t^i = b^i(t, X_t)\,dt + \sum_{j=1}^m \sigma^{ij}(t, X_t)\,dW_t^j
$$

### 2. Correlated Brownian Motions


**Correlation structure:** $d\langle W^i, W^j \rangle_t = \rho_{ij}\,dt$

**Cholesky decomposition:** Write $W_t = L Z_t$ where:
- $Z_t$ has independent components
- $L L^T = \rho$ (correlation matrix)

```python
def correlated_BM(rho, T, N, num_paths):
    """
    Generate correlated Brownian motions.
    
    Parameters:
    -----------
    rho : array
        Correlation matrix (d x d)
    T : float
        Terminal time
    N : int
        Number of steps
    num_paths : int
        Number of paths
    
    Returns:
    --------
    t : array
        Time grid
    W : array
        Brownian motions (num_paths x d x N+1)
    """
    d = rho.shape[0]
    dt = T / N
    t = np.linspace(0, T, N+1)
    
    # Cholesky decomposition
    L = np.linalg.cholesky(rho)
    
    W = np.zeros((num_paths, d, N+1))
    
    for path in range(num_paths):
        # Independent standard normals
        Z = np.random.randn(d, N)
        # Correlate them
        dW = np.sqrt(dt) * (L @ Z)
        # Cumulative sum
        W[path, :, 1:] = np.cumsum(dW, axis=1)
    
    return t, W
```

### 3. Example: Heston Model


$$
\begin{cases}
dS_t = \mu S_t\,dt + \sqrt{V_t} S_t\,dW_t^1 \\
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^2
\end{cases}
$$

with $d\langle W^1, W^2 \rangle_t = \rho\,dt$.

```python
def heston_euler(S0, V0, mu, kappa, theta, xi, rho, T, N, num_paths):
    """Euler-Maruyama for Heston model with full truncation."""
    dt = T / N
    t = np.linspace(0, T, N+1)
    
    S = np.zeros((num_paths, N+1))
    V = np.zeros((num_paths, N+1))
    S[:, 0] = S0
    V[:, 0] = V0
    
    # Correlation
    rho_matrix = np.array([[1, rho], [rho, 1]])
    L = np.linalg.cholesky(rho_matrix)
    
    for path in range(num_paths):
        for n in range(N):
            # Correlated Brownian increments
            Z = np.random.randn(2)
            dW = np.sqrt(dt) * (L @ Z)
            
            # Ensure V stays positive (full truncation)
            V_n = max(V[path, n], 0)
            
            # Update S
            S[path, n+1] = S[path, n] + mu*S[path, n]*dt + \
                          np.sqrt(V_n)*S[path, n]*dW[0]
            
            # Update V
            V[path, n+1] = V[path, n] + kappa*(theta - V_n)*dt + \
                          xi*np.sqrt(V_n)*dW[1]
    
    return t, S, V
```

---

## Error Sources and Mitigation


### 1. Two Types of Error


**Total error = Discretization error + Monte Carlo error**

$$
\text{Error} \approx C_1 \Delta t^\gamma + \frac{C_2}{\sqrt{M}}
$$

where:
- $\gamma$ = strong convergence order
- $M$ = number of Monte Carlo paths

### 2. Optimal Allocation


To minimize computational cost for fixed error $\varepsilon$:

**Balance the errors:**

$$
\Delta t^\gamma \approx \frac{1}{\sqrt{M}}
$$

**Optimal:** $\Delta t \sim \varepsilon^{2/(2\gamma+1)}$, $M \sim \varepsilon^{-4\gamma/(2\gamma+1)}$

**For Euler-Maruyama** ($\gamma = 0.5$):
- $\Delta t \sim \varepsilon^{2/3}$
- $M \sim \varepsilon^{-4/3}$

### 3. Variance Reduction Techniques


**Antithetic variates:** For each path with increments $\Delta W_n$, simulate another with $-\Delta W_n$.

```python
def euler_maruyama_antithetic(b, sigma, X0, T, N, num_paths):
    """Euler-Maruyama with antithetic variance reduction."""
    dt = T / N
    t = np.linspace(0, T, N+1)
    
    # Ensure even number of paths
    num_paths = 2 * (num_paths // 2)
    X = np.zeros((num_paths, N+1))
    X[:, 0] = X0
    
    for pair in range(num_paths // 2):
        dW = np.sqrt(dt) * np.random.randn(N)
        
        # Positive path
        for n in range(N):
            X[2*pair, n+1] = X[2*pair, n] + \
                            b(t[n], X[2*pair, n])*dt + \
                            sigma(t[n], X[2*pair, n])*dW[n]
        
        # Antithetic path
        for n in range(N):
            X[2*pair+1, n+1] = X[2*pair+1, n] + \
                              b(t[n], X[2*pair+1, n])*dt + \
                              sigma(t[n], X[2*pair+1, n])*(-dW[n])
    
    return t, X
```

**Control variates:** Use known expectation to reduce variance.

**Importance sampling:** Change measure to concentrate samples in relevant region.

---

## Practical Considerations


### 1. Choosing the Time Step


**Guidelines:**

1. **Accuracy requirement:** $\Delta t \lesssim \varepsilon^{2/\gamma}$ for error $\varepsilon$
2. **Stability:** For mean-reverting SDEs, $\kappa \Delta t < 1$
3. **Non-negativity:** For CIR/Heston, use small $\Delta t$ or special schemes
4. **Computational budget:** Balance $N$ and $M$

### 2. Monitoring Numerical Stability


```python
def check_stability(X, threshold=1e10):
    """Check if simulation exploded."""
    if np.any(np.isnan(X)) or np.any(np.abs(X) > threshold):
        return False
    return True
```

### 3. Comparing Schemes


```python
def compare_schemes():
    """Compare different schemes for GBM."""
    mu, sig, S0 = 0.1, 0.2, 100
    T, N = 1.0, 100
    
    # Exact
    t, S_exact = exact_GBM(S0, mu, sig, T, N, 10000)
    
    # Euler-Maruyama
    b = lambda t, S: mu * S
    sigma = lambda t, S: sig * S
    t, S_em = euler_maruyama(b, sigma, S0, T, N, 10000)
    
    # Milstein
    sigma_prime = lambda t, S: sig
    t, S_mil = milstein(b, sigma, sigma_prime, S0, T, N, 10000)
    
    # Compare terminal values
    print(f"Exact:   mean={np.mean(S_exact[:,-1]):.4f}, std={np.std(S_exact[:,-1]):.4f}")
    print(f"E-M:     mean={np.mean(S_em[:,-1]):.4f}, std={np.std(S_em[:,-1]):.4f}")
    print(f"Milstein: mean={np.mean(S_mil[:,-1]):.4f}, std={np.std(S_mil[:,-1]):.4f}")
    
    # Error
    print(f"\nMean absolute error:")
    print(f"E-M:      {np.mean(np.abs(S_em[:,-1] - S_exact[:,-1])):.4f}")
    print(f"Milstein: {np.mean(np.abs(S_mil[:,-1] - S_exact[:,-1])):.4f}")
```

---

## Summary


### 1. Scheme Selection Guide


| Scheme | Strong Order | Weak Order | When to Use |
|--------|--------------|------------|-------------|
| **Euler-Maruyama** | 0.5 | 1.0 | General purpose, simple |
| **Milstein** | 1.0 | 1.0 | When $\sigma'$ is available |
| **Exact** | ∞ | ∞ | GBM, OU (when possible) |
| **Predictor-Corrector** | ~1.0 | ~1.5 | Better stability |
| **Runge-Kutta** | 1.5+ | 2.0+ | High accuracy needed |

### 2. Key Takeaways


1. **Euler-Maruyama** is the workhorse: simple, robust, works for most SDEs
2. **Milstein** improves accuracy when diffusion derivative is tractable
3. **Exact simulation** eliminates discretization error when available
4. **Convergence** depends on smoothness of coefficients and scheme order
5. **Error balance:** Discretization error vs. Monte Carlo error
6. **Multidimensional SDEs** require careful treatment of correlation
7. **Variance reduction** can dramatically improve efficiency

### 3. Computational Complexity


For error $\varepsilon$ using Euler-Maruyama:
- Time steps: $N \sim \varepsilon^{-2/3}$
- Paths: $M \sim \varepsilon^{-4/3}$
- **Total cost:** $\sim \varepsilon^{-2}$

For Milstein (strong order 1.0):
- **Total cost:** $\sim \varepsilon^{-5/3}$ (better!)

### 4. From Discrete to Continuous


The journey from coin flips to sophisticated numerical schemes illustrates a fundamental principle:

> **Continuous-time stochastic processes are limits of discrete random walks.**

This insight unifies:
- Donsker's theorem (random walk → Brownian motion)
- Numerical discretization (continuous SDE → discrete scheme)
- Monte Carlo estimation (finite samples → expectations)

Understanding this connection provides both theoretical foundation and practical implementation skills for computational stochastic calculus.
