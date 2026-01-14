# Why Deterministic Models Fail


Having documented the empirical properties of financial returns in the previous sections, we now confront a fundamental question: **Can deterministic models adequately describe asset price dynamics?**

The answer, as we shall demonstrate rigorously, is **no**. Deterministic ordinary differential equations (ODEs), while elegant and mathematically tractable, are fundamentally incompatible with the stylized facts observed in real financial data. This section explains why deterministic approaches fail and motivates the need for stochastic differential equations.

---

## The Deterministic Growth Model


### 1. Exponential Growth ODE


The simplest model for asset prices is exponential growth:

$$
\frac{dS}{dt} = \mu S
$$

where:
- $S(t)$ is the asset price at time $t$
- $\mu$ is the constant growth rate (expected return)

**Solution:**

$$
S(t) = S_0 e^{\mu t}
$$

This is a **smooth, deterministic trajectory** with no randomness.

### 2. Properties of the Deterministic Model


**1. Perfect predictability:**

Given $S_0$ and $\mu$, the price at any future time is **exactly known**:

$$
S(t) = S_0 e^{\mu t} \quad \text{for all } t \geq 0
$$

**2. Smoothness:**

The path $t \mapsto S(t)$ is **infinitely differentiable**:

$$
S'(t) = \mu S(t), \quad S''(t) = \mu^2 S(t), \quad \text{etc.}
$$

**3. No volatility:**

The instantaneous return is **constant**:

$$
\frac{dS/dt}{S} = \mu \quad \text{(deterministic)}
$$

**4. Monotonicity:**

- If $\mu > 0$: $S(t)$ strictly increases
- If $\mu < 0$: $S(t)$ strictly decreases  
- If $\mu = 0$: $S(t) = S_0$ (constant)

### 3. Comparison with Real Data


Let's compare the deterministic model with actual stock prices:

```python
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def compare_deterministic_vs_real(ticker, start_date, end_date):
    """
    Compare deterministic exponential growth with real stock prices.
    """
    # Get real data
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    
    # Compute parameters from data
    S0 = df['Close'].iloc[0]
    ST = df['Close'].iloc[-1]
    T = len(df) / 252  # Time in years
    
    # Fit deterministic model: S(T) = S0 * exp(mu * T)
    mu = np.log(ST / S0) / T
    
    # Generate deterministic trajectory
    t = np.linspace(0, T, len(df))
    S_det = S0 * np.exp(mu * t)
    
    # Plot comparison
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df.index, df['Close'], label='Real Stock Price', 
            linewidth=1.5, alpha=0.8)
    ax.plot(df.index, S_det, label='Deterministic Model', 
            linestyle='--', linewidth=2, color='red')
    
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price ($)', fontsize=12)
    ax.set_title(f'{ticker}: Deterministic Model vs Reality', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print(f"Fitted growth rate: μ = {mu:.4f} ({mu*100:.2f}% per year)")
    print(f"Initial price: ${S0:.2f}")
    print(f"Final price (actual): ${ST:.2f}")
    print(f"Final price (model): ${S_det[-1]:.2f}")
    print(f"Error: {abs(ST - S_det[-1]):.2f} ({abs(ST - S_det[-1])/ST * 100:.2f}%)")

# Example
compare_deterministic_vs_real("AAPL", "2023-01-01", "2023-12-31")
```

**Observation:** The deterministic model:
- ✅ Gets the **endpoints** correct (by construction)
- ❌ Completely **misses all intermediate fluctuations**
- ❌ Cannot capture **volatility**
- ❌ Cannot model **risk**

---

## Fundamental Incompatibilities


### 1. Failure 1: No Randomness


**Stylized Fact:** Returns exhibit unpredictable fluctuations.

**Deterministic Model:**

$$
r_t = \frac{S(t+\Delta t) - S(t)}{S(t)} = e^{\mu \Delta t} - 1 \approx \mu \Delta t
$$

This is **constant** and **perfectly predictable**!

**Reality:**

$$
r_t = \text{random variable with } \mathbb{E}[r_t] \approx \mu \Delta t, \quad \text{Var}(r_t) > 0
$$

**Conclusion:** Deterministic models have **zero variance** → Cannot match observed volatility.

### 2. Failure 2: Too Smooth


**Stylized Fact:** Stock prices have **nowhere-differentiable paths** (like Brownian motion).

**Deterministic ODE:** Requires $S(t)$ to be **continuously differentiable**:

$$
\frac{dS}{dt} = \text{well-defined at all times}
$$

**Reality:** Price paths are continuous but **not differentiable**:

$$
\lim_{\Delta t \to 0} \frac{S(t + \Delta t) - S(t)}{\Delta t} = \text{does not exist}
$$

This is a rigorous result from the theory of Brownian motion.

**Demonstration:**

```python
def demonstrate_nondifferentiability(df):
    """
    Show that returns don't converge as Δt → 0.
    """
    prices = df['Close'].values
    
    # Compute returns at different time scales
    dt_values = [1, 5, 10, 20]  # Days
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    for idx, dt in enumerate(dt_values):
        # Compute returns
        returns = (prices[dt:] - prices[:-dt]) / prices[:-dt]
        
        # Normalize by sqrt(dt) (should be stable for Brownian motion)
        normalized = returns / np.sqrt(dt)
        
        # Plot
        axes[idx].hist(normalized, bins=50, density=True, 
                       alpha=0.7, edgecolor='black')
        axes[idx].set_title(f'Returns / √(Δt), Δt = {dt} days')
        axes[idx].set_xlabel('Normalized Return')
        axes[idx].set_ylabel('Density')
        axes[idx].grid(True, alpha=0.3)
        
        # Statistics
        std = np.std(normalized)
        axes[idx].axvline(std, color='red', linestyle='--', 
                         label=f'Std = {std:.4f}')
        axes[idx].axvline(-std, color='red', linestyle='--')
        axes[idx].legend()
    
    plt.tight_layout()
    plt.show()
    
    print("\nIf prices were differentiable (ODE model):")
    print("  → Returns / Δt would converge to a constant")
    print("\nActual behavior (Brownian motion):")
    print("  → Returns / √Δt converge to a stable distribution")
```

### 3. Failure 3: Cannot Capture Volatility Clustering


**Stylized Fact:** Volatility clusters (GARCH effects).

**Deterministic Model:** Volatility is **zero** everywhere!

$$
\text{Var}\left(\frac{dS}{dt}\Big|_t\right) = 0 \quad \text{for all } t
$$

**Reality:** Volatility is time-varying:

$$
\sigma_t = \sigma(t, \text{information}) \quad \text{(changes over time)}
$$

Periods of high volatility followed by high volatility, etc.

**Fundamental impossibility:** A deterministic ODE **cannot** generate time-varying volatility because it has **no volatility** to begin with.

### 4. Failure 4: No Heavy Tails


**Stylized Fact:** Returns have fat-tailed distributions (excess kurtosis).

**Deterministic Model:** Return distribution is a **Dirac delta function**:

$$
P(r_t = \mu \Delta t) = 1, \quad P(r_t \neq \mu \Delta t) = 0
$$

This is **infinitely peaked** at one point with **no tails** whatsoever.

**Reality:** Returns have continuous distribution with heavy tails.

### 5. Failure 5: No Leverage Effect


**Stylized Fact:** Negative returns correlate with increased volatility.

**Deterministic Model:** No correlation possible because:
1. Returns are constant ($\mu \Delta t$)
2. Volatility is zero

**Reality:** $\text{Corr}(r_t, \sigma_{t+1}) \approx -0.6$ (strong negative correlation).

---

## Adding Noise: The Naive Approach


### 1. Attempt: Add Random Shocks


**Idea:** Modify the deterministic model by adding random "shocks":

$$
S(t + \Delta t) = S(t) e^{\mu \Delta t} + \epsilon_t
$$

where $\epsilon_t \sim \mathcal{N}(0, \sigma^2 \Delta t)$ is random noise.

### 2. Problems with This Approach


**Problem 1: Non-positive prices**

With additive noise, $S(t)$ can become **negative**:

$$
S(t + \Delta t) = S(t) e^{\mu \Delta t} + \epsilon_t < 0 \quad \text{if } \epsilon_t < -S(t)e^{\mu \Delta t}
$$

This is economically nonsensical (prices must be positive).

**Problem 2: Incorrect scaling**

The noise $\epsilon_t$ has **constant variance** $\sigma^2 \Delta t$ regardless of price level.

**Reality:** Volatility scales with price (volatility of \$100 stock ≠ volatility of \$10 stock).

**Problem 3: No continuous-time limit**

As $\Delta t \to 0$, what happens?

$$
S(t + \Delta t) - S(t) = S(t)(\mu \Delta t + o(\Delta t)) + \epsilon_t
$$

Dividing by $\Delta t$:

$$
\frac{S(t + \Delta t) - S(t)}{\Delta t} = S(t)\mu + \frac{\epsilon_t}{\Delta t}
$$

But $\frac{\epsilon_t}{\Delta t} \to \infty$ as $\Delta t \to 0$ (noise grows without bound!).

**Conclusion:** Simple additive noise doesn't work.

---

## Better Attempt: Multiplicative Noise


### 1. Discrete-Time Model


**Improved idea:** Make noise proportional to price:

$$
S(t + \Delta t) = S(t) \cdot e^{\mu \Delta t + \sigma \epsilon_t}
$$

where $\epsilon_t \sim \mathcal{N}(0, \Delta t)$.

**Advantages:**
- ✅ Prices remain **positive** (exponential is always positive)
- ✅ Volatility **scales with price** level
- ✅ Log-returns are additive

### 2. Taking the Continuous-Time Limit


**Question:** What happens as $\Delta t \to 0$?

For small $\Delta t$:

$$
S(t + \Delta t) = S(t) \exp\left(\mu \Delta t + \sigma \sqrt{\Delta t} \cdot Z\right)
$$

where $Z \sim \mathcal{N}(0, 1)$.

Taking logarithms:

$$
\log S(t + \Delta t) - \log S(t) = \mu \Delta t + \sigma \sqrt{\Delta t} \cdot Z
$$

Dividing by $\Delta t$:

$$
\frac{\log S(t + \Delta t) - \log S(t)}{\Delta t} = \mu + \sigma \frac{Z}{\sqrt{\Delta t}}
$$

As $\Delta t \to 0$, the term $\frac{Z}{\sqrt{\Delta t}} \to \infty$ but in a **controlled way**!

**This is precisely a Brownian motion increment:**

$$
\frac{W(t + \Delta t) - W(t)}{\sqrt{\Delta t}} \sim \mathcal{N}(0, 1)
$$

### 3. Heuristic Continuous-Time Limit


Formally (heuristically):

$$
d(\log S) = \mu \, dt + \sigma \, dW_t
$$

where $W_t$ is **Brownian motion**.

**But wait!** We want an equation for $S$, not $\log S$.

Using the "chain rule" (actually **Itô's lemma**, which we'll study later):

$$
dS = \mu S \, dt + \sigma S \, dW_t
$$

**This is a stochastic differential equation (SDE)**, not an ODE!

---

## Why We Need Stochastic Calculus


### 1. The Problem with Ordinary Calculus


**Ordinary calculus assumes:**

$$
df = f'(x) \, dx
$$

**But for stochastic processes:**

$$
d(\log S) \neq \frac{1}{S} dS \quad \text{(WRONG!)}
$$

**The correct formula (Itô's lemma) includes a correction term:**

$$
d(\log S) = \frac{1}{S} dS - \frac{1}{2S^2} (dS)^2
$$

The term $(dS)^2 = \sigma^2 S^2 dt$ is **not zero** in stochastic calculus!

### 2. Fundamental Difference: $(dW_t)^2 = dt$


**In ordinary calculus:**

$$
(dx)^2 = 0 \quad \text{(infinitesimal squared is zero)}
$$

**In stochastic calculus:**

$$
(dW_t)^2 = dt \quad \text{(NOT zero!)}
$$

This is the **quadratic variation** of Brownian motion, a fundamental result.

**Consequence:** We need a completely new calculus framework.

---

## Summary: The Path to SDEs


### 1. The Logical Flow


```
Empirical Observations
        ↓
Stylized Facts
    ↓ ↓ ↓
1. Randomness
2. Non-differentiability  
3. Volatility clustering
4. Heavy tails
5. Leverage effect
        ↓
Deterministic ODEs FAIL
        ↓
Add Random Shocks
        ↓
Multiplicative Noise
        ↓
Continuous-Time Limit
        ↓
NEED: Stochastic Differential Equations
        ↓
NEED: Stochastic Calculus (Itô)
```

### 2. What We Need to Learn


To properly model financial returns, we must develop:

1. **Brownian Motion Theory** (Chapter 1)
   - Continuous but nowhere differentiable
   - Quadratic variation
   - Martingale properties

2. **Stochastic Integration** (Section 2.1)
   - Itô integral: $\int f(t) \, dW_t$
   - Itô isometry
   - Properties of stochastic integrals

3. **Itô's Lemma** (Section 2.2)
   - Chain rule for stochastic processes
   - $(dW_t)^2 = dt$ rule
   - Multi-dimensional version

4. **Stochastic Differential Equations** (Section 2.3)
   - Defining and solving SDEs
   - Existence and uniqueness
   - Connection to PDEs

### 3. The Geometric Brownian Motion Model


The correct continuous-time model is:

$$
\boxed{
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
}
$$

**Properties:**
- ✅ **Random**: Contains Brownian motion $W_t$
- ✅ **Positive**: Solution is $S_t = S_0 \exp\left[(\mu - \frac{\sigma^2}{2})t + \sigma W_t\right] > 0$
- ✅ **Volatility**: Standard deviation is $\sigma \sqrt{t}$ (scales with time)
- ✅ **Non-differentiable**: Paths have same regularity as Brownian motion
- ✅ **Log-normal**: $\log S_t$ is Gaussian

**But we cannot understand this model without:**
- Itô calculus
- Stochastic integration theory
- Quadratic variation
- Martingale theory

---

## Comparison Table


| Property | Deterministic ODE | Real Stock Returns | Stochastic SDE |
|----------|------------------|-------------------|----------------|
| **Randomness** | None (perfectly predictable) | High (unpredictable) | Yes (via $dW_t$) |
| **Differentiability** | Smooth paths | Nowhere differentiable | Nowhere differentiable |
| **Volatility** | Zero | Time-varying, ~15-30% | $\sigma$ (constant or time-varying) |
| **Heavy tails** | No tails (deterministic) | Yes (kurtosis ~7-10) | Possible (with jumps or stoch vol) |
| **Vol clustering** | N/A (no vol) | Yes (ARCH/GARCH) | Requires extensions (GARCH, stoch vol) |
| **Leverage effect** | N/A | Yes ($\rho \approx -0.6$) | Requires correlated vol |
| **Positive prices** | Yes | Yes | Yes (if properly formulated) |
| **Mathematical framework** | Ordinary calculus | ??? | **Itô calculus** |

---

## Conclusion


**The verdict is clear:**

Deterministic ordinary differential equations are **fundamentally inadequate** for modeling financial asset prices because:

1. They have **zero randomness** (but markets are unpredictable)
2. They are **too smooth** (but prices are non-differentiable)
3. They have **zero volatility** (but risk is central to finance)
4. They **cannot cluster** (but volatility clusters empirically)
5. They **cannot have heavy tails** (but crashes are too frequent)

**The solution:**

We must move to **stochastic differential equations**, which require a rigorous foundation in:

- Brownian motion (Chapter 1)
- Stochastic integration (Section 2.1)
- Itô's lemma (Section 2.2)
- SDE theory (Section 2.3)

**Next:** We bridge from this motivation to the formal mathematics of SDEs.
