# Bridge to Stochastic Differential Equations

We have now established the empirical motivation for stochastic models: **deterministic ODEs fail to capture the essential features of financial returns**. This final section of our empirical foundation builds a bridge from discrete-time observations to the continuous-time stochastic differential equations that form the mathematical core of modern quantitative finance.

---

## 1. The Journey: From Data to Theory

### 1.1 Where We've Been

**Section 1:** Stock Data and Returns
- Proper data handling (adjusted prices, quality checks)
- Return computation (discrete vs continuous)
- Statistical moment estimation
- Annualization procedures

**Section 2:** Stylized Facts
- Heavy tails (leptokurtosis)
- Volatility clustering (GARCH effects)
- Leverage effect (asymmetric volatility)
- No return autocorrelation
- Aggregational Gaussianity

**Section 3:** Why Deterministic Models Fail
- Zero variance (no randomness)
- Too smooth (differentiable paths)
- Cannot cluster
- No heavy tails
- Need multiplicative noise

### 1.2 Where We're Going

**Chapter 2: Stochastic Differential Equations**

- **Section 2.1:** Itô Integration (mathematical foundations)
- **Section 2.2:** Itô's Lemma (chain rule for stochastic processes)
- **Section 2.3:** SDE Theory (existence, uniqueness, solutions)
- **Section 2.4:** Diffusion Processes (Markov properties)
- **Section 2.5:** Infinitesimal Generator (connection to PDEs)

---

## 2. The Central Question

**How do we go from discrete-time observations to continuous-time models?**

### 2.1 The Discrete-Time Random Walk

Suppose stock prices evolve via a **discrete-time random walk**:

$$
S_{n+1} = S_n + \mu \Delta t + \sigma \sqrt{\Delta t} \cdot Z_n
$$

where:
- $\Delta t$ is the time step (e.g., 1 day = 1/252 years)
- $Z_n \sim \mathcal{N}(0, 1)$ are i.i.d. standard normal
- $\mu$ is drift (expected return per unit time)
- $\sigma$ is diffusion (volatility per unit time)

**In multiplicative form:**

$$
S_{n+1} = S_n \exp\left(\mu \Delta t - \frac{\sigma^2}{2}\Delta t + \sigma \sqrt{\Delta t} \cdot Z_n\right)
$$

### 2.2 Taking the Limit $\Delta t \to 0$

**Question:** What happens as we make the time step infinitesimally small?

**Heuristic argument:**

$$
S(t + \Delta t) - S(t) = \mu S(t) \Delta t + \sigma S(t) \sqrt{\Delta t} \cdot Z
$$

Dividing by $\Delta t$:

$$
\frac{S(t + \Delta t) - S(t)}{\Delta t} = \mu S(t) + \sigma S(t) \frac{Z}{\sqrt{\Delta t}}
$$

As $\Delta t \to 0$:
- First term: $\mu S(t)$ → well-defined
- Second term: $\frac{Z}{\sqrt{\Delta t}} \to$ ???

**The key insight:** The term $\frac{Z}{\sqrt{\Delta t}}$ does **not** go to zero or infinity in a pathological way. Instead, it converges to the **derivative of Brownian motion**:

$$
\frac{Z}{\sqrt{\Delta t}} \rightsquigarrow \frac{dW_t}{dt} \quad \text{(formal notation)}
$$

**Heuristic SDE:**

$$
\boxed{
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
}
$$

This is **Geometric Brownian Motion (GBM)**, the foundation of the Black-Scholes model.

---

## 3. What is $dW_t$?

### 3.1 Brownian Motion Increments

**Brownian motion** $W_t$ is a continuous-time stochastic process with:

1. $W_0 = 0$
2. **Independent increments:** $W_t - W_s$ independent of $W_u - W_v$ for non-overlapping intervals
3. **Gaussian increments:** $W_t - W_s \sim \mathcal{N}(0, t - s)$
4. **Continuous paths:** $t \mapsto W_t$ is continuous

**Infinitesimal increment:**

$$
dW_t = W_{t+dt} - W_t \sim \mathcal{N}(0, dt)
$$

**Key property:**

$$
\mathbb{E}[dW_t] = 0, \quad \mathbb{E}[(dW_t)^2] = dt
$$

This means:

$$
(dW_t)^2 = dt \quad \text{(in mean-square sense)}
$$

**This is the fundamental difference from ordinary calculus!**

### 3.2 Why $(dW_t)^2 = dt$ Matters

In ordinary calculus, $(dx)^2 = 0$ for infinitesimals. But for Brownian motion:

$$
(dW_t)^2 = dt \neq 0
$$

**Consequence:** The chain rule changes!

**Ordinary calculus:**

$$
d f(x) = f'(x) \, dx
$$

**Stochastic calculus (Itô's lemma):**

$$
d f(X_t) = f'(X_t) \, dX_t + \frac{1}{2} f''(X_t) (dX_t)^2
$$

The second-order term survives because $(dX_t)^2$ is not negligible!

---

## 4. From Discrete to Continuous: Rigorous Approach

### 4.1 Donsker's Theorem (Functional CLT)

**Theorem:** Consider the discrete random walk:

$$
S_n^{(\Delta t)} = \sum_{i=1}^n \sqrt{\Delta t} \cdot Z_i
$$

where $Z_i \sim \mathcal{N}(0, 1)$ i.i.d.

**Interpolated process:**

$$
S^{(\Delta t)}(t) = S_{\lfloor t/\Delta t \rfloor}^{(\Delta t)} + (t - \lfloor t/\Delta t \rfloor \Delta t) \frac{S_{\lfloor t/\Delta t \rfloor + 1}^{(\Delta t)} - S_{\lfloor t/\Delta t \rfloor}^{(\Delta t)}}{\Delta t}
$$

**Donsker (1951):** As $\Delta t \to 0$:

$$
S^{(\Delta t)}(t) \xrightarrow{d} W_t \quad \text{(in distribution)}
$$

where $W_t$ is standard Brownian motion.

**Significance:** This rigorously justifies using Brownian motion as the continuous-time limit of discrete random walks.

### 4.2 Implications for SDEs

**Discrete-time GBM:**

$$
S_{n+1} = S_n \exp\left(\mu \Delta t - \frac{\sigma^2}{2}\Delta t + \sigma \sqrt{\Delta t} \cdot Z_n\right)
$$

**Continuous-time limit:**

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
$$

with solution:

$$
S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
$$

---

## 5. The Anatomy of an SDE

### 5.1 General Form

A **stochastic differential equation** has the form:

$$
dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t
$$

where:
- $X_t$ is the **state variable** (e.g., stock price, interest rate)
- $\mu(X_t, t)$ is the **drift function** (deterministic trend)
- $\sigma(X_t, t)$ is the **diffusion function** (volatility)
- $W_t$ is **standard Brownian motion**

### 5.2 Components Explained

**Drift term: $\mu(X_t, t) dt$**

- Represents the **expected change** over infinitesimal time
- Analogous to the deterministic ODE term
- Units: [same as $X$] per unit time
- $\mathbb{E}[dX_t | X_t] = \mu(X_t, t) dt$

**Diffusion term: $\sigma(X_t, t) dW_t$**

- Represents **random fluctuations**
- Intensity controlled by $\sigma(X_t, t)$
- Units: [same as $X$] per $\sqrt{\text{time}}$
- $\text{Var}(dX_t | X_t) = \sigma^2(X_t, t) dt$

### 5.3 Integral Form

The SDE:

$$
dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t
$$

is shorthand for the **integral equation**:

$$
X_t = X_0 + \int_0^t \mu(X_s, s) \, ds + \int_0^t \sigma(X_s, s) \, dW_s
$$

where:
- First integral: ordinary Riemann/Lebesgue integral
- Second integral: **Itô stochastic integral** (needs special definition)

---

## 6. Why We Need Itô Calculus

### 6.1 The Problem

**Question:** How do we make sense of:

$$
\int_0^t \sigma(X_s, s) \, dW_s \quad ?
$$

This is **not** a standard Riemann or Lebesgue integral because:
- $W_t$ is **nowhere differentiable**
- $dW_t/dt$ does not exist
- Cannot use $\int f(t) g'(t) dt$ formula

### 6.2 The Solution: Itô Integral

**Section 2.1** will rigorously define:

$$
\int_0^t f(s) \, dW_s
$$

as the limit of approximating sums:

$$
\lim_{n \to \infty} \sum_{i=0}^{n-1} f(t_i) [W_{t_{i+1}} - W_{t_i}]
$$

where the partition $0 = t_0 < t_1 < \cdots < t_n = t$ gets finer.

**Key properties:**

1. **Linearity:** $\int (af + bg) \, dW = a \int f \, dW + b \int g \, dW$

2. **Martingale:** $\mathbb{E}\left[\int_0^t f(s) \, dW_s\right] = 0$

3. **Itô isometry:** $\mathbb{E}\left[\left(\int_0^t f(s) \, dW_s\right)^2\right] = \int_0^t \mathbb{E}[f^2(s)] \, ds$

---

## 7. Examples of SDEs in Finance

### 7.1 Geometric Brownian Motion (GBM)

**SDE:**

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
$$

**Application:** Stock prices (Black-Scholes model)

**Properties:**
- Always positive: $S_t > 0$ for all $t$ if $S_0 > 0$
- Log-normal distribution
- Constant relative volatility $\sigma$

### 7.2 Ornstein-Uhlenbeck (OU) Process

**SDE:**

$$
dX_t = \kappa(\theta - X_t) \, dt + \sigma \, dW_t
$$

**Application:** Interest rates (Vasicek model), mean-reverting spreads

**Properties:**
- Mean-reverting to level $\theta$ at rate $\kappa$
- Gaussian distribution
- Stationary in long run

### 7.3 Cox-Ingersoll-Ross (CIR) Model

**SDE:**

$$
dr_t = \kappa(\theta - r_t) \, dt + \sigma \sqrt{r_t} \, dW_t
$$

**Application:** Short-term interest rates

**Properties:**
- Mean-reverting
- Always non-negative (if $2\kappa\theta \geq \sigma^2$)
- State-dependent volatility

### 7.4 Heston Stochastic Volatility

**System of SDEs:**

$$
\begin{align}
dS_t &= \mu S_t \, dt + \sqrt{V_t} S_t \, dW_t^S \\
dV_t &= \kappa(\theta - V_t) \, dt + \sigma \sqrt{V_t} \, dW_t^V
\end{align}
$$

with $\text{Corr}(dW_t^S, dW_t^V) = \rho dt$.

**Application:** Option pricing with stochastic volatility

**Properties:**
- Volatility $V_t$ is itself stochastic
- Captures volatility clustering
- Leverage effect via correlation $\rho < 0$

---

## 8. The Road Ahead: Chapter 2 Overview

### 8.1 Section 2.1: Itô Integration

**What we'll learn:**

- **Quadratic variation:** Why $(dW_t)^2 = dt$
- **Construction of Itô integral:** Rigorous definition
- **Itô isometry:** Fundamental tool for computing variances
- **Properties:** Linearity, martingale property, path continuity

**Why it matters:** Cannot work with SDEs without understanding stochastic integration.

### 8.2 Section 2.2: Itô's Lemma

**What we'll learn:**

- **The chain rule for stochastic processes**
- **How to compute $df(X_t)$ when $X_t$ satisfies an SDE**
- **Multi-dimensional version**
- **Integration by parts, product rule, quotient rule**

**Why it matters:** This is the **most important tool** in stochastic calculus. We use it to:
- Solve SDEs
- Derive option pricing PDEs
- Compute expectations and variances
- Transform between different representations

### 8.3 Section 2.3: SDE Theory

**What we'll learn:**

- **Standard SDE examples** (GBM, Vasicek, CIR, etc.)
- **Methods for solving SDEs** analytically
- **Verifying solutions** using Itô's lemma
- **Numerical simulation** when no closed form exists
- **Moment analysis** for understanding distributions

**Why it matters:** These are the actual models used in quantitative finance.

### 8.4 Section 2.4: Diffusion Processes

**What we'll learn:**

- **Markov property** and strong Markov property
- **Generator theory** (infinitesimal generator)
- **Kolmogorov equations** (forward and backward)
- **Connection to PDEs**

**Why it matters:** Links stochastic processes to partial differential equations (basis of PDE methods for option pricing).

---

## 9. From Intuition to Rigor

### 9.1 What We've Established Intuitively

**Heuristic understanding:**

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
$$

means:

- Stock price has drift $\mu S_t$
- Stock price has random fluctuations of size $\sigma S_t$
- Fluctuations are proportional to current price
- Randomness comes from Brownian motion

### 9.2 What We Need to Make Rigorous

1. **What does $dW_t$ mean precisely?**
   → Section 2.1 (Itô Integration)

2. **How do we solve for $S_t$?**
   → Section 2.2 (Itô's Lemma) + Section 2.3 (Solving SDEs)

3. **When do solutions exist and are they unique?**
   → Section 2.5 (Existence & Uniqueness)

4. **How do we compute with $S_t$?**
   → Section 2.2 (Itô's Lemma)

5. **What's the connection to PDEs?**
   → Section 2.4 (Diffusion Processes) + Section 2.6 (Generator)

---

## 10. Summary: The Complete Journey

### 10.1 From Data to Models

```
Stock Price Data
    ↓ (compute returns)
Return Statistics
    ↓ (observe properties)
Stylized Facts
    ↓ (heavy tails, vol clustering, ...)
Deterministic Models FAIL
    ↓ (add randomness)
Discrete Random Walk
    ↓ (take limit Δt → 0)
Brownian Motion
    ↓ (build rigorous theory)
Itô Calculus
    ↓ (construct models)
Stochastic Differential Equations
    ↓ (solve and analyze)
Quantitative Finance Models
```

### 10.2 The Mathematical Edifice

**Foundation:** Brownian motion (Chapter 1)

**Structure:**
- **Floor 1:** Itô Integration (Section 2.1)
- **Floor 2:** Itô's Lemma (Section 2.2)
- **Floor 3:** SDE Theory (Section 2.3)
- **Floor 4:** Diffusion Processes (Section 2.4-2.6)

**Applications:** Everything else in the book builds on this foundation!

---

## 11. Conclusion

We are now ready to begin the rigorous mathematical development of stochastic differential equations. The empirical foundation has been laid:

✓ We understand real financial data  
✓ We know what patterns to capture  
✓ We see why deterministic models fail  
✓ We recognize the need for continuous-time randomness

**Next stop: Section 2.1 - Itô Integration**

The adventure begins with defining:

$$
\int_0^t f(s) \, dW_s
$$

Everything else follows from this fundamental construct.

**Let's build the mathematics.**
