# Moment Analysis of SDEs


This section presents **rigorous analytical derivations** of moments for fundamental stochastic differential equations. Understanding moments is essential for:

- Characterizing distributions of stochastic processes
- Pricing derivatives and computing risk measures
- Calibrating models to market data
- Deriving approximate solutions and asymptotic behavior

We develop complete derivations using stochastic calculus tools including **Itô's lemma**, **Itô isometry**, **integrating factors**, and **moment ODEs**.

---

## Standard Brownian Motion


### 1. Definition


The **standard Brownian motion** (Wiener process) $B_t$ satisfies:

$$
dB_t = dW_t, \quad B_0 = 0
$$

### 2. Basic Moments


Since $B_t \sim \mathcal{N}(0, t)$ by construction:

$$
\boxed{
\mathbb{E}[B_t] = 0, \quad \text{Var}(B_t) = t
}
$$

### 3. Higher Moments


For a Gaussian random variable $X \sim \mathcal{N}(0, \sigma^2)$:

**Odd moments:**

$$
\mathbb{E}[X^{2k+1}] = 0 \quad \text{for all } k \geq 0
$$

**Even moments:**

$$
\mathbb{E}[X^{2k}] = \sigma^{2k} \cdot (2k-1)!! = \sigma^{2k} \cdot \frac{(2k)!}{2^k k!}
$$

where $(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1)$.

**For Brownian motion:**

$$
\boxed{
\mathbb{E}[B_t^{2k}] = t^k \cdot (2k-1)!!
}
$$

**Examples:**
- $\mathbb{E}[B_t^2] = t$
- $\mathbb{E}[B_t^4] = 3t^2$
- $\mathbb{E}[B_t^6] = 15t^3$
- $\mathbb{E}[B_t^8] = 105t^4$

### 4. Moment Generating Function


$$
M_B(u, t) = \mathbb{E}[e^{uB_t}] = e^{u^2 t/2}
$$

**Derivation:** Since $B_t \sim \mathcal{N}(0, t)$:

$$
\mathbb{E}[e^{uB_t}] = \int_{-\infty}^\infty e^{ux} \frac{1}{\sqrt{2\pi t}} e^{-x^2/(2t)} dx = e^{u^2 t/2}
$$

---

## Brownian Motion with Drift and Volatility


### 1. SDE


Let $X_t$ satisfy:

$$
dX_t = \mu\,dt + \sigma\,dW_t, \quad X_0 \in \mathbb{R}
$$

### 2. Solution


This is a linear SDE. Integrating:

$$
X_t = X_0 + \mu t + \sigma B_t
$$

### 3. First Two Moments


Since $B_t \sim \mathcal{N}(0, t)$:

$$
\boxed{
\mathbb{E}[X_t] = X_0 + \mu t, \quad \text{Var}(X_t) = \sigma^2 t
}
$$

**Distribution:** $X_t \sim \mathcal{N}(X_0 + \mu t, \sigma^2 t)$

### 4. Higher Moments


Since $X_t$ is Gaussian:

$$
\mathbb{E}[(X_t - \mathbb{E}[X_t])^n] = \begin{cases}
0 & \text{if } n \text{ odd} \\
\sigma^n t^{n/2} (n-1)!! & \text{if } n \text{ even}
\end{cases}
$$

### 5. Moment Generating Function


$$
M_X(u, t) = \mathbb{E}[e^{uX_t}] = \exp\left[u(X_0 + \mu t) + \frac{u^2 \sigma^2 t}{2}\right]
$$

### 6. Conditional Moments


For $s < t$:

$$
\mathbb{E}[X_t | X_s] = X_s + \mu(t - s)
$$

$$
\text{Var}(X_t | X_s) = \sigma^2(t - s)
$$

---

## Geometric Brownian Motion


### 1. SDE


The GBM process satisfies:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t, \quad S_0 > 0
$$

### 2. Solution


Define $Y_t = \log S_t$ and apply **Itô's lemma**:

$$
f(S) = \log S, \quad f'(S) = \frac{1}{S}, \quad f''(S) = -\frac{1}{S^2}
$$

$$
\begin{align}
dY_t &= \frac{1}{S_t}dS_t + \frac{1}{2}\left(-\frac{1}{S_t^2}\right)(dS_t)^2 \\
&= \frac{1}{S_t}(\mu S_t dt + \sigma S_t dW_t) - \frac{1}{2S_t^2} \cdot \sigma^2 S_t^2 dt \\
&= \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma dW_t
\end{align}
$$

Integrating:

$$
\log S_t = \log S_0 + \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma B_t
$$

$$
\boxed{
S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma B_t\right]
}
$$

### 3. First Two Moments


Let $Z = \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma B_t \sim \mathcal{N}\left(\left(\mu - \frac{\sigma^2}{2}\right)t, \sigma^2 t\right)$.

For a Gaussian $Z \sim \mathcal{N}(m, v^2)$:

$$
\mathbb{E}[e^Z] = e^{m + v^2/2}
$$

**Expectation:**

$$
\begin{align}
\mathbb{E}[S_t] &= S_0 \mathbb{E}[e^Z] \\
&= S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \frac{\sigma^2 t}{2}\right] \\
&= S_0 e^{\mu t}
\end{align}
$$

**Second moment:**

$$
\mathbb{E}[S_t^2] = S_0^2 \mathbb{E}[e^{2Z}]
$$

For $2Z \sim \mathcal{N}(2(\mu - \sigma^2/2)t, 4\sigma^2 t)$:

$$
\mathbb{E}[e^{2Z}] = \exp\left[2\left(\mu - \frac{\sigma^2}{2}\right)t + \frac{4\sigma^2 t}{2}\right] = e^{2\mu t + \sigma^2 t}
$$

Therefore:

$$
\mathbb{E}[S_t^2] = S_0^2 e^{2\mu t + \sigma^2 t}
$$

**Variance:**

$$
\begin{align}
\text{Var}(S_t) &= \mathbb{E}[S_t^2] - (\mathbb{E}[S_t])^2 \\
&= S_0^2 e^{2\mu t + \sigma^2 t} - S_0^2 e^{2\mu t} \\
&= S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)
\end{align}
$$

$$
\boxed{
\mathbb{E}[S_t] = S_0 e^{\mu t}, \quad \text{Var}(S_t) = S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)
}
$$

### 4. Higher Moments


**General $n$-th moment:**

$$
\mathbb{E}[S_t^n] = S_0^n \mathbb{E}[e^{nZ}]
$$

For $nZ \sim \mathcal{N}(n(\mu - \sigma^2/2)t, n^2\sigma^2 t)$:

$$
\boxed{
\mathbb{E}[S_t^n] = S_0^n \exp\left[n\mu t + \frac{n(n-1)}{2}\sigma^2 t\right]
}
$$

**Verification for $n=1, 2$:**
- $n=1$: $\mathbb{E}[S_t] = S_0 e^{\mu t}$ ✓
- $n=2$: $\mathbb{E}[S_t^2] = S_0^2 e^{2\mu t + \sigma^2 t}$ ✓

### 5. Moment Generating Function


$$
\boxed{
M_S(u, t) = \mathbb{E}[e^{uS_t}] = \begin{cases}
\text{No closed form} & \text{(log-normal distribution)} \\
\text{Use } \mathbb{E}[S_t^n] \text{ instead} & 
\end{cases}
}
$$

**Alternative: Log moment generating function**

For $\log S_t \sim \mathcal{N}(m, v^2)$ with $m = \log S_0 + (\mu - \sigma^2/2)t$ and $v^2 = \sigma^2 t$:

$$
\mathbb{E}[e^{u \log S_t}] = \mathbb{E}[S_t^u] = S_0^u e^{u\mu t + u(u-1)\sigma^2 t/2}
$$

### 6. Conditional Moments


For $s < t$:

$$
\mathbb{E}[S_t | S_s] = S_s e^{\mu(t-s)}
$$

$$
\text{Var}(S_t | S_s) = S_s^2 e^{2\mu(t-s)}(e^{\sigma^2(t-s)} - 1)
$$

**Derivation:** Since $S_t = S_s \exp[(drifts) + \sigma(B_t - B_s)]$, conditioning on $S_s$ gives independent increments.

### 7. Skewness and Kurtosis


The log-normal distribution is **right-skewed** and **heavy-tailed**.

**Skewness:**

$$
\text{Skew}(S_t) = (e^{\sigma^2 t} + 2)\sqrt{e^{\sigma^2 t} - 1}
$$

**Excess kurtosis:**

$$
\text{Kurt}(S_t) = e^{4\sigma^2 t} + 2e^{3\sigma^2 t} + 3e^{2\sigma^2 t} - 6
$$

Both increase with $\sigma^2 t$, showing heavier tails for higher volatility or longer time.

---

## Vasicek Model


### 1. SDE


The Vasicek model is defined by:

$$
dr_t = a(b - r_t)\,dt + \sigma\,dW_t, \quad r_0 = r(0)
$$

where:
- $a > 0$ is the mean reversion speed
- $b$ is the long-term mean
- $\sigma$ is the volatility

### 2. Solution via Integrating Factor


Rewrite as:

$$
dr_t + ar_t\,dt = ab\,dt + \sigma\,dW_t
$$

Multiply both sides by the integrating factor $e^{at}$:

$$
e^{at}dr_t + ae^{at}r_t\,dt = abe^{at}\,dt + \sigma e^{at}\,dW_t
$$

The left side is $d(r_t e^{at})$:

$$
d(r_t e^{at}) = abe^{at}\,dt + \sigma e^{at}\,dW_t
$$

Integrate from $0$ to $t$:

$$
r_t e^{at} - r_0 = ab\int_0^t e^{as}\,ds + \sigma\int_0^t e^{as}\,dW_s
$$

$$
r_t e^{at} = r_0 + ab\frac{e^{at} - 1}{a} + \sigma\int_0^t e^{as}\,dW_s
$$

$$
\boxed{
r_t = r_0 e^{-at} + b(1 - e^{-at}) + \sigma e^{-at}\int_0^t e^{as}\,dW_s
}
$$

### 3. Expectation


Using linearity of expectation and $\mathbb{E}[\int e^{as}\,dW_s] = 0$:

$$
\boxed{
\mathbb{E}[r_t] = r_0 e^{-at} + b(1 - e^{-at})
}
$$

**Long-term behavior:**

$$
\lim_{t \to \infty} \mathbb{E}[r_t] = b
$$

The process **mean-reverts** to $b$ with speed $a$.

### 4. Variance


The only stochastic term is:

$$
I_t = \sigma e^{-at}\int_0^t e^{as}\,dW_s
$$

Use **Itô isometry**:

$$
\mathbb{E}[I_t^2] = \sigma^2 e^{-2at} \mathbb{E}\left[\left(\int_0^t e^{as}\,dW_s\right)^2\right] = \sigma^2 e^{-2at} \int_0^t e^{2as}\,ds
$$

$$
= \sigma^2 e^{-2at} \cdot \frac{e^{2at} - 1}{2a} = \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

Since $\mathbb{E}[I_t] = 0$:

$$
\boxed{
\text{Var}(r_t) = \frac{\sigma^2}{2a}(1 - e^{-2at})
}
$$

**Long-term variance:**

$$
\lim_{t \to \infty} \text{Var}(r_t) = \frac{\sigma^2}{2a}
$$

**Stationary distribution:** $r_\infty \sim \mathcal{N}\left(b, \frac{\sigma^2}{2a}\right)$

### 5. Complete Moment Summary


$$
\boxed{
\begin{align}
\mathbb{E}[r_t] &= r_0 e^{-at} + b(1 - e^{-at}) \\
\text{Var}(r_t) &= \frac{\sigma^2}{2a}(1 - e^{-2at})
\end{align}
}
$$

### 6. Conditional Moments


For $s < t$, the increment $r_t - r_s$ depends on $r_s$.

From the solution form:

$$
r_t = r_s e^{-a(t-s)} + b(1 - e^{-a(t-s)}) + \sigma e^{-a(t-s)}\int_s^t e^{a u}\,dW_u
$$

Therefore:

$$
\mathbb{E}[r_t | r_s] = r_s e^{-a(t-s)} + b(1 - e^{-a(t-s)})
$$

$$
\text{Var}(r_t | r_s) = \frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})
$$

### 7. Covariance Function


For $s < t$:

$$
\text{Cov}(r_s, r_t) = \text{Var}(r_s) \cdot e^{-a(t-s)}
$$

**Proof:** Use tower property:

$$
\text{Cov}(r_s, r_t) = \mathbb{E}[r_s r_t] - \mathbb{E}[r_s]\mathbb{E}[r_t]
$$

After algebra (using $\mathbb{E}[r_t | r_s] = \alpha + \beta r_s$):

$$
\text{Cov}(r_s, r_t) = \frac{\sigma^2}{2a}(1 - e^{-2as}) \cdot e^{-a(t-s)}
$$

**Correlation:**

$$
\rho(s, t) = e^{-a|t-s|}
$$

This is an **exponentially decaying autocorrelation**, characteristic of OU processes.

---

## Cox-Ingersoll-Ross (CIR) Model


### 1. SDE


The CIR model is defined by:

$$
dr_t = a(b - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t, \quad r_0 > 0
$$

where:
- $a > 0$ is the mean reversion speed
- $b > 0$ is the long-term mean
- $\sigma > 0$ is the volatility parameter
- **Feller condition:** $2ab \geq \sigma^2$ ensures $r_t > 0$ for all $t$

### 2. Expectation


Let $m(t) = \mathbb{E}[r_t]$. Taking expectations of both sides:

$$
\mathbb{E}[dr_t] = a(b - \mathbb{E}[r_t])\,dt + \sigma \mathbb{E}[\sqrt{r_t}]\,dW_t
$$

The stochastic integral has zero expectation, giving:

$$
\frac{dm}{dt} = a(b - m(t))
$$

This is a linear ODE with solution:

$$
\boxed{
\mathbb{E}[r_t] = r_0 e^{-at} + b(1 - e^{-at})
}
$$

**Note:** Same as Vasicek! The state-dependent volatility doesn't affect the mean.

### 3. Variance via Second Moment


To find variance, we need $\mathbb{E}[r_t^2]$.

**Apply Itô's lemma** to $f(r) = r^2$:

$$
f'(r) = 2r, \quad f''(r) = 2
$$

$$
\begin{align}
d(r_t^2) &= 2r_t\,dr_t + \frac{1}{2} \cdot 2 \cdot (dr_t)^2 \\
&= 2r_t[a(b - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t] + \sigma^2 r_t\,dt \\
&= [2ab r_t - 2ar_t^2 + \sigma^2 r_t]\,dt + 2\sigma r_t^{3/2}\,dW_t \\
&= [(2ab + \sigma^2)r_t - 2ar_t^2]\,dt + 2\sigma r_t^{3/2}\,dW_t
\end{align}
$$

**Take expectation:**

$$
\frac{d}{dt}\mathbb{E}[r_t^2] = (2ab + \sigma^2)\mathbb{E}[r_t] - 2a\mathbb{E}[r_t^2]
$$

Let $m_2(t) = \mathbb{E}[r_t^2]$ and $m(t) = \mathbb{E}[r_t]$. This is a **linear first-order ODE**:

$$
\frac{dm_2}{dt} + 2am_2 = (2ab + \sigma^2)m(t)
$$

### 4. Solving the Second Moment ODE


**Integrating factor:** $\mu(t) = e^{2at}$

Multiply both sides:

$$
e^{2at}\frac{dm_2}{dt} + 2ae^{2at}m_2 = (2ab + \sigma^2)e^{2at}m(t)
$$

$$
\frac{d}{dt}[e^{2at}m_2] = (2ab + \sigma^2)e^{2at}m(t)
$$

Integrate from $0$ to $t$:

$$
e^{2at}m_2(t) - m_2(0) = (2ab + \sigma^2)\int_0^t e^{2as}m(s)\,ds
$$

Substitute $m(s) = r_0 e^{-as} + b(1 - e^{-as})$:

$$
\begin{align}
\int_0^t e^{2as}m(s)\,ds &= \int_0^t e^{2as}[r_0 e^{-as} + b(1 - e^{-as})]\,ds \\
&= r_0 \int_0^t e^{as}\,ds + b\int_0^t [e^{2as} - e^{as}]\,ds \\
&= r_0 \frac{e^{at} - 1}{a} + b\left[\frac{e^{2at} - 1}{2a} - \frac{e^{at} - 1}{a}\right]
\end{align}
$$

After substitution and simplification:

$$
m_2(t) = r_0^2 e^{-2at} + \frac{\sigma^2}{a}r_0 e^{-at}(1 - e^{-at}) + b^2(1 - e^{-at})^2 + \frac{\sigma^2 b}{2a}(1 - e^{-at})^2
$$

### 5. Variance Formula


$$
\text{Var}(r_t) = m_2(t) - m(t)^2
$$

After considerable algebra:

$$
\boxed{
\text{Var}(r_t) = \frac{\sigma^2}{a}\left[r_0 e^{-at}(1 - e^{-at}) + \frac{b}{2}(1 - e^{-at})^2\right]
}
$$

**Alternative form:**

$$
\text{Var}(r_t) = r_0\frac{\sigma^2}{a}(e^{-at} - e^{-2at}) + \frac{b\sigma^2}{2a}(1 - e^{-at})^2
$$

### 6. Long-Term Variance


$$
\lim_{t \to \infty} \text{Var}(r_t) = \frac{b\sigma^2}{2a}
$$

**Stationary distribution:** $r_\infty$ follows a scaled non-central chi-squared distribution with mean $b$ and variance $\frac{b\sigma^2}{2a}$.

### 7. Conditional Moments


For $s < t$:

$$
\mathbb{E}[r_t | r_s] = r_s e^{-a(t-s)} + b(1 - e^{-a(t-s)})
$$

$$
\text{Var}(r_t | r_s) = r_s \frac{\sigma^2}{a}(e^{-a(t-s)} - e^{-2a(t-s)}) + \frac{b\sigma^2}{2a}(1 - e^{-a(t-s)})^2
$$

---

## Ornstein-Uhlenbeck Process (General Form)


### 1. SDE


$$
dX_t = -\gamma X_t\,dt + \sigma\,dW_t, \quad X_0 = x
$$

This is a **centered** version of Vasicek with $b = 0$.

### 2. Moments


$$
\mathbb{E}[X_t] = x e^{-\gamma t}
$$

$$
\text{Var}(X_t) = \frac{\sigma^2}{2\gamma}(1 - e^{-2\gamma t})
$$

### 3. Stationary Distribution


For $t \to \infty$ starting from the stationary distribution:

$$
X_t \sim \mathcal{N}\left(0, \frac{\sigma^2}{2\gamma}\right)
$$

---

## General Techniques for Moment Computation


### 1. Method 1: Direct from Solution


If an **explicit solution** exists, compute moments directly using properties of Gaussian or log-normal distributions.

**Example:** GBM, Vasicek, OU

### 2. Method 2: Itô's Lemma for Powers


To find $\mathbb{E}[X_t^n]$, apply Itô's lemma to $f(x) = x^n$:

$$
d(X_t^n) = nx^{n-1}\,dX_t + \frac{n(n-1)}{2}X_t^{n-2}(dX_t)^2
$$

Take expectations to get an ODE for $m_n(t) = \mathbb{E}[X_t^n]$.

**Example:** CIR second moment

### 3. Method 3: Moment ODEs from Generator


For SDE $dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t$, the generator is:

$$
\mathcal{L} = b(x)\frac{\partial}{\partial x} + \frac{\sigma^2(x)}{2}\frac{\partial^2}{\partial x^2}
$$

Then:

$$
\frac{d}{dt}\mathbb{E}[f(X_t)] = \mathbb{E}[\mathcal{L}f(X_t)]
$$

For $f(x) = x^n$:

$$
\frac{dm_n}{dt} = \mathbb{E}[b(X_t) \cdot nx^{n-1}] + \mathbb{E}[\frac{\sigma^2(X_t)}{2} \cdot n(n-1)x^{n-2}]
$$

This gives a **hierarchy of moment ODEs**.

### 4. Method 4: Characteristic Functions


The **characteristic function** is:

$$
\phi(u, t) = \mathbb{E}[e^{iuX_t}]
$$

Moments can be recovered via:

$$
\mathbb{E}[X_t^n] = \frac{1}{i^n}\frac{\partial^n \phi}{\partial u^n}\Big|_{u=0}
$$

For affine processes (Vasicek, CIR, Heston), $\phi$ satisfies a Riccati ODE.

---

## Comparison Table


| Model | $\mathbb{E}[X_t]$ | $\text{Var}(X_t)$ | Distribution |
|-------|-------------------|-------------------|--------------|
| **Brownian Motion** | $0$ | $t$ | $\mathcal{N}(0, t)$ |
| **BM with Drift** | $X_0 + \mu t$ | $\sigma^2 t$ | $\mathcal{N}(X_0 + \mu t, \sigma^2 t)$ |
| **GBM** | $S_0 e^{\mu t}$ | $S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)$ | Log-normal |
| **Vasicek** | $r_0 e^{-at} + b(1-e^{-at})$ | $\frac{\sigma^2}{2a}(1-e^{-2at})$ | $\mathcal{N}(\cdot, \cdot)$ |
| **CIR** | $r_0 e^{-at} + b(1-e^{-at})$ | $\frac{\sigma^2}{a}[r_0 e^{-at}(1-e^{-at}) + \frac{b}{2}(1-e^{-at})^2]$ | Scaled $\chi^2$ |

---

## Verification via Simulation


### 1. Python Implementation


```python
import numpy as np
import matplotlib.pyplot as plt

def verify_CIR_moments(a, b, sigma, r0, T, N, num_paths=10000):
    """
    Verify CIR moments via Monte Carlo simulation.
    """
    dt = T / N
    t_grid = np.linspace(0, T, N+1)
    
    # Simulate paths
    r = np.zeros((num_paths, N+1))
    r[:, 0] = r0
    
    for path in range(num_paths):
        for n in range(N):
            dW = np.sqrt(dt) * np.random.randn()
            r_n = max(r[path, n], 0)  # Ensure positivity
            r[path, n+1] = r[path, n] + a*(b - r_n)*dt + sigma*np.sqrt(r_n)*dW
    
    # Theoretical moments
    def theoretical_mean(t):
        return r0 * np.exp(-a*t) + b*(1 - np.exp(-a*t))
    
    def theoretical_var(t):
        return (sigma**2/a) * (r0*np.exp(-a*t)*(1-np.exp(-a*t)) + 
                               (b/2)*(1-np.exp(-a*t))**2)
    
    # Compare
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Mean
    simulated_mean = np.mean(r, axis=0)
    theoretical_mean_values = theoretical_mean(t_grid)
    
    ax1.plot(t_grid, simulated_mean, label='Simulated', linewidth=2)
    ax1.plot(t_grid, theoretical_mean_values, '--', label='Theoretical', linewidth=2)
    ax1.set_xlabel('Time t')
    ax1.set_ylabel('Mean $\\mathbb{E}[r_t]$')
    ax1.set_title('CIR Process: Mean')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Variance
    simulated_var = np.var(r, axis=0)
    theoretical_var_values = theoretical_var(t_grid)
    
    ax2.plot(t_grid, simulated_var, label='Simulated', linewidth=2)
    ax2.plot(t_grid, theoretical_var_values, '--', label='Theoretical', linewidth=2)
    ax2.set_xlabel('Time t')
    ax2.set_ylabel('Variance $\\text{Var}(r_t)$')
    ax2.set_title('CIR Process: Variance')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Print final values
    print(f"At t={T}:")
    print(f"Mean:     Simulated = {simulated_mean[-1]:.6f}, "
          f"Theoretical = {theoretical_mean_values[-1]:.6f}")
    print(f"Variance: Simulated = {simulated_var[-1]:.6f}, "
          f"Theoretical = {theoretical_var_values[-1]:.6f}")

# Example usage
verify_CIR_moments(a=2.0, b=0.05, sigma=0.1, r0=0.03, T=2.0, N=1000)
```

### 2. Verification for GBM


```python
def verify_GBM_moments(mu, sigma, S0, T, N, num_paths=10000):
    """Verify GBM moments."""
    dt = T / N
    t_grid = np.linspace(0, T, N+1)
    
    # Exact simulation
    S = np.zeros((num_paths, N+1))
    S[:, 0] = S0
    
    for path in range(num_paths):
        W = np.cumsum(np.concatenate([[0], np.sqrt(dt)*np.random.randn(N)]))
        S[path, :] = S0 * np.exp((mu - 0.5*sigma**2)*t_grid + sigma*W)
    
    # Theoretical
    theoretical_mean = S0 * np.exp(mu * t_grid)
    theoretical_var = S0**2 * np.exp(2*mu*t_grid) * (np.exp(sigma**2*t_grid) - 1)
    
    # Compare
    simulated_mean = np.mean(S, axis=0)
    simulated_var = np.var(S, axis=0)
    
    print(f"Mean error: {np.max(np.abs(simulated_mean - theoretical_mean)):.6f}")
    print(f"Var error:  {np.max(np.abs(simulated_var - theoretical_var)):.6f}")
```

---

## Applications


### 1. Option Pricing


**Black-Scholes formula** uses $\mathbb{E}[S_T]$ under risk-neutral measure.

### 2. Risk Management


**Value-at-Risk (VaR)** depends on distribution quantiles, which are determined by moments.

### 3. Model Calibration


Match theoretical moments to market-implied moments (e.g., from option prices).

### 4. Parameter Estimation


**Method of moments:** Equate sample moments to theoretical moments and solve for parameters.

**Example for OU process:**

$$
\hat{\gamma} = -\frac{1}{\Delta t}\log\left(\frac{\text{Cov}(X_{t+\Delta t}, X_t)}{\text{Var}(X_t)}\right)
$$

---

## Summary


### 1. Key Takeaways


1. **Gaussian processes** (BM, Vasicek, OU) have simple moment formulas
2. **Log-normal processes** (GBM) require MGF techniques
3. **State-dependent volatility** (CIR) requires moment ODEs
4. **Mean reversion** leads to stationary distributions
5. **Itô isometry** is essential for computing variances of stochastic integrals

### 2. Computational Strategy


1. **Try explicit solution first** (works for linear SDEs)
2. **Use Itô's lemma** for powers to get moment ODEs
3. **Solve ODE hierarchy** for higher moments
4. **Verify via simulation** for complex models

### 3. Connection to Other Topics


- **Feynman-Kac:** Moments relate to PDE solutions
- **Characteristic functions:** Fourier transform of distribution
- **Filtering theory:** Conditional moments for state estimation
- **Asymptotic analysis:** Long-term behavior and stationary distributions

Understanding moments provides both analytical insight and practical tools for working with stochastic processes in quantitative finance.
