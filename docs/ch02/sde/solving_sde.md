# Solving Stochastic Differential Equations

This section develops analytical solution methods through a carefully structured learning path, where each technique is motivated by concrete examples before systematic generalization.

**Reference:** For additional perspectives, see [Korean lecture series](https://www.youtube.com/watch?v=G61MAT5OgTM&list=PLXziV1DL41og-CJN6Q1tLiU4DreSZmi_P&index=9)

---

## 1. Introduction

### 1.1 General Form of an SDE

An Itô stochastic differential equation takes the form:

$$
dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t
$$

where:
- $X_t$ is the stochastic process (unknown function)
- $\mu(X_t, t)$ is the **drift term** (deterministic trend)
- $\sigma(X_t, t)$ is the **diffusion term** (random fluctuation intensity)
- $W_t$ is standard **Brownian motion**

### 1.2 What Does "Solving" Mean?

We seek an **explicit formula** for $X_t$ as a function of $W_t$ and $t$:

$$
X_t = f(W_t, t, X_0)
$$

This allows us to:
- Compute exact distributions
- Calculate moments analytically
- Price derivatives in closed form
- Benchmark numerical schemes

### 1.3 Key Observation

**Most SDEs do not have closed-form solutions.** The techniques in this section work for special classes of SDEs with particular structures.

When analytical solutions don't exist, we use:
- Numerical simulation (see SDE Simulation section)
- Moment analysis (see Moment Analysis section)
- PDE methods
- Asymptotic approximations

---

## 2. Three Core Examples

We begin with three fundamental SDEs that motivate our solution methods. Understanding these deeply provides the foundation for all subsequent techniques.

### 2.1 Example 1: Brownian Motion with Drift

**SDE:**

$$
dX_t = \mu\,dt + \sigma\,dW_t, \quad X_0 \in \mathbb{R}
$$

**Physical interpretation:**
- Particle subject to constant force ($\mu$)
- Plus random thermal fluctuations ($\sigma dW_t$)

**Solution:**

This is the simplest non-trivial SDE. Direct integration yields:

$$
\begin{align}
X_t &= X_0 + \int_0^t \mu\,ds + \int_0^t \sigma\,dW_s \\
&= X_0 + \mu t + \sigma B_t
\end{align}
$$

where $B_t = \int_0^t dW_s$ is Brownian motion.

**Distribution:**

$$
\boxed{
X_t \sim \mathcal{N}(X_0 + \mu t, \sigma^2 t)
}
$$

**Properties:**
- **Gaussian process** with linear mean growth
- Stationary and independent increments
- Fundamental building block in stochastic processes
- Arises as solution to **Langevin equation** in statistical mechanics

**Why this matters:** This example motivates **Method 1: Direct Integration**.

### 2.2 Example 2: Geometric Brownian Motion

**SDE:**

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t, \quad S_0 > 0
$$

**Financial interpretation:**
- Stock price with expected return $\mu$
- Volatility proportional to price level ($\sigma S_t$)
- Foundation of Black-Scholes-Merton theory

**Attempt 1: Direct integration?**

$$
S_t \stackrel{?}{=} S_0 + \int_0^t \mu S_s\,ds + \int_0^t \sigma S_s\,dW_s
$$

This doesn't help because $S_s$ appears inside the integrals!

**Key insight:** The **multiplicative** structure suggests a **logarithmic transformation**.

**Solution via transformation:**

Define $Y_t = \log S_t$. By Itô's lemma:

$$
\begin{align}
dY_t &= \frac{1}{S_t}dS_t - \frac{1}{2}\frac{1}{S_t^2}(dS_t)^2 \\
&= \frac{1}{S_t}(\mu S_t\,dt + \sigma S_t\,dW_t) - \frac{1}{2S_t^2} \cdot \sigma^2 S_t^2\,dt \\
&= \mu\,dt + \sigma\,dW_t - \frac{\sigma^2}{2}\,dt \\
&= \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
\end{align}
$$

This is now **linear** like Example 1! Integrating:

$$
\log S_t = \log S_0 + \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t
$$

Exponentiating:

$$
\boxed{
S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
}
$$

**Distribution:**

$$
\log S_t \sim \mathcal{N}\left(\log S_0 + \left(\mu - \frac{\sigma^2}{2}\right)t, \sigma^2 t\right)
$$

Therefore $S_t$ is **log-normally distributed**.

**The Itô correction term:**

The $-\frac{\sigma^2}{2}$ term is not arbitrary—it arises from the quadratic variation:

$$
(dS_t)^2 = \sigma^2 S_t^2\,dt
$$

This is unique to stochastic calculus and does not appear in ordinary calculus.

**Why this matters:** This example motivates **Method 2: Itô's Lemma (Change of Variables)**.

### 2.3 Example 3: Vasicek Model (Mean-Reverting Process)

**SDE:**

$$
dr_t = a(b - r_t)\,dt + \sigma\,dW_t, \quad a > 0, \quad b \in \mathbb{R}
$$

**Financial interpretation:**
- Interest rate $r_t$ pulled toward long-run level $b$
- Speed of mean reversion: $a$
- Constant volatility: $\sigma$

**Rewrite:**

$$
dr_t + ar_t\,dt = ab\,dt + \sigma\,dW_t
$$

This looks like an ODE plus noise! Recall from ODEs: for $\frac{dy}{dt} + ay = f(t)$, we use integrating factor $e^{at}$.

**Solution via integrating factor:**

Multiply both sides by $e^{at}$:

$$
e^{at}dr_t + ae^{at}r_t\,dt = abe^{at}\,dt + \sigma e^{at}\,dW_t
$$

The left side is exactly $d(e^{at}r_t)$ because:

$$
d(e^{at}r_t) = e^{at}dr_t + ae^{at}r_t\,dt
$$

(No Itô correction: $e^{at}$ is non-random!)

Therefore:

$$
d(e^{at}r_t) = abe^{at}\,dt + \sigma e^{at}\,dW_t
$$

Integrate from $0$ to $t$:

$$
e^{at}r_t - r_0 = ab\int_0^t e^{as}\,ds + \sigma\int_0^t e^{as}\,dW_s
$$

$$
e^{at}r_t = r_0 + ab\frac{e^{at} - 1}{a} + \sigma\int_0^t e^{as}\,dW_s
$$

**Solution:**

$$
\boxed{
r_t = r_0 e^{-at} + b(1 - e^{-at}) + \sigma e^{-at}\int_0^t e^{as}\,dW_s
}
$$

**Alternative form:**

$$
r_t = r_0 e^{-at} + b(1 - e^{-at}) + \sigma\int_0^t e^{-a(t-s)}\,dW_s
$$

**Long-term behavior:**

$$
\lim_{t \to \infty} \mathbb{E}[r_t] = b, \quad \lim_{t \to \infty} \text{Var}(r_t) = \frac{\sigma^2}{2a}
$$

The process is **Gaussian** and **mean-reverting**.

**Limitation:** May become negative (problematic for interest rates).

**Why this matters:** This example motivates **Method 3: Integrating Factor**.

---

## 3. Method 1: Direct Integration

### 3.1 When It Works

**Class of SDEs:** Additive noise with simple drift.

$$
dX_t = b(t)\,dt + \sigma(t)\,dW_t
$$

where $b(t)$ and $\sigma(t)$ are known functions of time only (not of $X_t$).

### 3.2 General Solution

$$
\boxed{
X_t = X_0 + \int_0^t b(s)\,ds + \int_0^t \sigma(s)\,dW_s
}
$$

- First integral: ordinary Riemann integral
- Second integral: Itô stochastic integral

### 3.3 Special Cases

**Constant coefficients** (Example 1):

$$
dX_t = \mu\,dt + \sigma\,dW_t \quad \Rightarrow \quad X_t = X_0 + \mu t + \sigma W_t
$$

**Time-dependent drift:**

$$
dX_t = \sin(t)\,dt + \sigma\,dW_t \quad \Rightarrow \quad X_t = X_0 + (1 - \cos(t)) + \sigma W_t
$$

**Time-dependent volatility:**

$$
dX_t = 0\,dt + e^{-t}\,dW_t \quad \Rightarrow \quad X_t = X_0 + \int_0^t e^{-s}\,dW_s
$$

### 3.4 Computing Moments

For $X_t = X_0 + \int_0^t b(s)\,ds + \int_0^t \sigma(s)\,dW_s$:

**Mean:**

$$
\mathbb{E}[X_t] = X_0 + \int_0^t b(s)\,ds
$$

**Variance (using Itô isometry):**

$$
\text{Var}(X_t) = \mathbb{E}\left[\left(\int_0^t \sigma(s)\,dW_s\right)^2\right] = \int_0^t \sigma^2(s)\,ds
$$

### 3.5 Limitations

**Does NOT work for:**
- Multiplicative noise: $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$
- State-dependent coefficients: $dr_t = a(b - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$

For these, we need more sophisticated methods.

---

## 4. Method 2: Itô's Lemma (Change of Variables)

### 4.1 The Fundamental Tool

**Itô's Lemma** is the chain rule for stochastic calculus. For $Y_t = f(X_t)$ where $X_t$ satisfies:

$$
dX_t = b(X_t, t)\,dt + \sigma(X_t, t)\,dW_t
$$

we have:

$$
\boxed{
dY_t = \left(\frac{\partial f}{\partial t} + b\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 f}{\partial x^2}\right)dt + \sigma\frac{\partial f}{\partial x}\,dW_t
}
$$

**Key difference from ordinary calculus:** The second derivative term $\frac{1}{2}\sigma^2 f_{xx}$.

### 4.2 Strategy for Solving SDEs

**Goal:** Find transformation $Y_t = f(X_t)$ such that:

$$
dY_t = \text{simple SDE (e.g., constant coefficients)}
$$

Then:
1. Solve for $Y_t$ using direct integration
2. Invert: $X_t = f^{-1}(Y_t)$

### 4.3 The GBM Example Revisited (Example 2)

**SDE:**

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

**Transformation:** $Y_t = \log S_t$

$$
\frac{\partial f}{\partial S} = \frac{1}{S}, \quad \frac{\partial^2 f}{\partial S^2} = -\frac{1}{S^2}
$$

**Apply Itô's lemma:**

$$
\begin{align}
d(\log S_t) &= \frac{1}{S_t}(\mu S_t\,dt + \sigma S_t\,dW_t) + \frac{1}{2}\left(-\frac{1}{S_t^2}\right)(\sigma S_t)^2\,dt \\
&= \mu\,dt + \sigma\,dW_t - \frac{\sigma^2}{2}\,dt \\
&= \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
\end{align}
$$

Now use Method 1 (direct integration):

$$
\log S_t = \log S_0 + \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t
$$

Invert:

$$
S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
$$

### 4.4 General Power Transformations

**SDE:**

$$
dX_t = bX_t\,dt + \sigma X_t^\beta\,dW_t
$$

**Try transformation:** $Y_t = X_t^{1-\beta}$ for $\beta \neq 1$.

After applying Itô's lemma, we get:

$$
dY_t = (1-\beta)bY_t\,dt - \frac{(1-\beta)\beta\sigma^2}{2}Y_t^{(2\beta-1)/(1-\beta)}\,dt + (1-\beta)\sigma\,dW_t
$$

This is simpler only for special $\beta$ values.

**Special case:** $\beta = 1/2$ gives a nearly linear SDE.

### 4.5 Choosing the Right Transformation

**Guidelines:**

| SDE Form | Try Transformation |
|----------|-------------------|
| $dX = \mu X\,dt + \sigma X\,dW$ | $\log X$ |
| $dX = bX^2\,dt + \sigma X\,dW$ | $1/X$ |
| $dX = bX\,dt + \sigma X^\beta\,dW$ | $X^{1-\beta}$ |
| $dX = b(X)\,dt + \sigma\sqrt{X}\,dW$ | $\sqrt{X}$ (Lamperti) |

---

## 5. Method 3: Integrating Factor (Linear SDEs)

### 5.1 When It Works

**Class of SDEs:** Linear in $X_t$ with deterministic coefficients.

$$
dX_t = [a(t) + b(t)X_t]\,dt + [c(t) + d(t)X_t]\,dW_t
$$

### 5.2 The Vasicek Example Revisited (Example 3)

**SDE:**

$$
dr_t = a(b - r_t)\,dt + \sigma\,dW_t
$$

**Rewrite in standard form:**

$$
dr_t + ar_t\,dt = ab\,dt + \sigma\,dW_t
$$

**Integrating factor:** $\mu(t) = e^{at}$

**Key insight:** Multiplying by $e^{at}$ makes the left side a perfect differential:

$$
d(e^{at}r_t) = e^{at}dr_t + ae^{at}r_t\,dt
$$

**Why no Itô correction?** Because $e^{at}$ is deterministic (no $dW$ term).

**General solution:**

$$
r_t = r_0 e^{-at} + b(1 - e^{-at}) + \sigma e^{-at}\int_0^t e^{as}\,dW_s
$$

### 5.3 General Linear SDE Solution

For:

$$
dX_t = [a(t) + b(t)X_t]\,dt + c(t)\,dW_t
$$

**Integrating factor:** $\mu(t) = \exp\left(\int_0^t b(s)\,ds\right)$

**Solution:**

$$
X_t = \frac{1}{\mu(t)}\left[X_0 + \int_0^t \mu(s)a(s)\,ds + \int_0^t \mu(s)c(s)\,dW_s\right]
$$

### 5.4 When There's Diffusion in $X_t$

For:

$$
dX_t = b(t)X_t\,dt + d(t)X_t\,dW_t
$$

The integrating factor must account for **both** drift and diffusion:

$$
Y_t = X_t \exp\left(-\int_0^t b(s)\,ds + \frac{1}{2}\int_0^t d^2(s)\,ds - \int_0^t d(s)\,dW_s\right)
$$

Then $Y_t$ is a **martingale**.

---

## 6. More Core Examples

### 6.1 Standard Brownian Motion

**SDE:**

$$
dB_t = dW_t, \quad B_0 = 0
$$

**Solution:**

This **defines** Brownian motion itself:

$$
B_t = \int_0^t dW_s = B_t
$$

**Properties:**
- $B_t \sim \mathcal{N}(0, t)$
- Continuous paths
- Independent increments
- Markov property
- Martingale property

**Why this matters:** Brownian motion is the building block of all Itô processes.

### 6.2 Cox-Ingersoll-Ross (CIR) Model

**SDE:**

$$
dr_t = a(b - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
$$

**Why it's different:**

- **State-dependent diffusion** $\sigma\sqrt{r_t}$ (unlike Vasicek)
- Ensures **non-negativity** if $2ab \geq \sigma^2$ (Feller condition)
- **No closed-form path solution**

**What we CAN find:**

1. **Distribution:** Scaled non-central chi-squared

$$
r_t \sim \frac{\sigma^2(1-e^{-at})}{4a}\chi_{\nu}^2\left(\frac{4ae^{-at}}{\sigma^2(1-e^{-at})}r_0\right)
$$

where $\nu = \frac{4ab}{\sigma^2}$.

2. **Moments:** (see Moment Analysis section)

$$
\mathbb{E}[r_t] = r_0 e^{-at} + b(1 - e^{-at})
$$

3. **Characteristic function:** Satisfies Riccati ODE

**Solution approach:**

- **Lamperti transform** to unit diffusion (see Method 5)
- **Exact simulation** via non-central chi-squared
- **Numerical methods** with positivity preservation

**Why this matters:** Motivates **Method 5: Separation of Variables (Lamperti Transform)**.

---

## 7. Method 4: Martingale Representation

### 7.1 Principle

If $M_t = g(X_t, t)$ is a **martingale**, then:

$$
\mathbb{E}[M_t | \mathcal{F}_s] = M_s
$$

This constrains the distribution of $X_t$.

### 7.2 Finding Martingales via Itô's Lemma

For $M_t$ to be a martingale, its drift must vanish:

$$
\frac{\partial g}{\partial t} + b(x)\frac{\partial g}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 g}{\partial x^2} = 0
$$

This is the **backward Kolmogorov equation**.

### 7.3 Example: Exponential Martingale

For $dX_t = \mu\,dt + \sigma\,dW_t$, consider:

$$
M_t = \exp\left[\lambda X_t - \left(\lambda\mu + \frac{\lambda^2\sigma^2}{2}\right)t\right]
$$

**Verification:** Apply Itô's lemma to check $dM_t$ has no $dt$ term.

**Applications:**
- Change of measure (Girsanov)
- Large deviations theory
- Moment generating functions

---

## 8. Method 5: Separation of Variables (Lamperti Transform)

### 8.1 Goal

Transform SDE with state-dependent diffusion to **unit diffusion**:

$$
dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t \quad \Rightarrow \quad dY_t = \tilde{b}(Y_t)\,dt + dW_t
$$

### 8.2 Lamperti Transform

**Transformation:**

$$
Y_t = h(X_t) = \int_{X_0}^{X_t} \frac{du}{\sigma(u)}
$$

**Result:** The transformed SDE has unit diffusion coefficient.

### 8.3 Example: CIR Model

**SDE:**

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
$$

**Lamperti transform:**

$$
Y_t = \int_{r_0}^{r_t} \frac{du}{\sigma\sqrt{u}} = \frac{2}{\sigma}(\sqrt{r_t} - \sqrt{r_0})
$$

**Inverted:** $r_t = \left(\frac{\sigma}{2}Y_t + \sqrt{r_0}\right)^2$

The transformed SDE relates to **squared Bessel processes**.

---

## 9. Method 6: Variation of Constants

### 9.1 For Non-Homogeneous Linear SDEs

**SDE:**

$$
dX_t = [\alpha(t) - \beta(t)X_t]\,dt + \sigma(t)\,dW_t
$$

**Strategy:**
1. Solve homogeneous part: $dY_t = -\beta(t)Y_t\,dt$
2. Use solution as integrating factor
3. Add particular solution

**Solution:**

$$
X_t = \frac{1}{\mu(t)}\left[X_0 + \int_0^t \mu(s)\alpha(s)\,ds + \int_0^t \mu(s)\sigma(s)\,dW_s\right]
$$

where $\mu(t) = \exp\left(\int_0^t \beta(s)\,ds\right)$.

### 9.2 Application: Time-Dependent Mean Reversion

Generalizes Vasicek to time-dependent parameters (useful for fitting yield curves).

---

## 10. Method 7: Feynman-Kac (SDE ↔ PDE Connection)

### 10.1 The Bridge

Given SDE:

$$
dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t
$$

Define:

$$
u(t, x) = \mathbb{E}[\phi(X_T) | X_t = x]
$$

Then $u$ satisfies the **backward Kolmogorov PDE**:

$$
\frac{\partial u}{\partial t} + b(x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 u}{\partial x^2} = 0
$$

### 10.2 Black-Scholes as Feynman-Kac

For GBM under risk-neutral measure:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

The call option price:

$$
C(t, S_t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ | S_t]
$$

satisfies the Black-Scholes PDE.

---

## 11. Method 8: Girsanov's Theorem (Change of Measure)

### 11.1 Changing the Drift

**Girsanov's Theorem:** We can change the drift by changing probability measure.

Under $\mathbb{P}$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

Under $\mathbb{Q}$ (with market price of risk $\theta = \frac{\mu - r}{\sigma}$):

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

where $W_t^{\mathbb{Q}} = W_t + \theta t$.

### 11.2 Application: Risk-Neutral Pricing

Now $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale, enabling:

$$
\text{Option Price} = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\text{Payoff} | \mathcal{F}_t]
$$

---

## 12. Method 9: Similarity Solutions

### 12.1 Scale-Invariant SDEs

For SDEs with homogeneity properties, seek solutions:

$$
X_t = t^\alpha f(W_t/t^\beta)
$$

### 12.2 Example: Quadratic SDE

$$
dX_t = X_t^2\,dt + dW_t
$$

May exhibit **finite-time explosion**. Similarity methods help characterize blow-up behavior.

---

## 13. Summary: Matching Methods to SDEs

| SDE Structure | Best Method | Example |
|--------------|-------------|---------|
| Additive noise: $dX = b(t)\,dt + \sigma(t)\,dW$ | **Direct Integration** | BM with drift |
| Multiplicative: $dS = \mu S\,dt + \sigma S\,dW$ | **Itô's Lemma** (log transform) | GBM |
| Linear: $dr = a(b-r)\,dt + \sigma\,dW$ | **Integrating Factor** | Vasicek |
| State-dependent diffusion: $dr = a(b-r)\,dt + \sigma\sqrt{r}\,dW$ | **Lamperti Transform** | CIR |
| Time-dependent linear | **Variation of Constants** | Hull-White |
| Need distributions | **Feynman-Kac** | Option pricing |
| Change of drift | **Girsanov** | Risk-neutral measure |

---

## 14. When No Closed-Form Solution Exists

### 14.1 The Reality

**Most SDEs lack analytical solutions**, including:
- Heston model (stochastic volatility)
- SABR model (with $\beta \neq 0, 1$)
- Multi-factor models
- Jump-diffusions
- General non-linear SDEs

### 14.2 Alternative Approaches

1. **Numerical Simulation**
   - Euler-Maruyama (see SDE Simulation section)
   - Milstein scheme
   - Higher-order methods

2. **Moment Analysis**
   - Compute $\mathbb{E}[X_t^n]$ via ODEs
   - See Moment Analysis section

3. **Characteristic Functions**
   - For affine models (Heston, CIR)
   - Semi-analytical option pricing

4. **PDE Methods**
   - Finite differences
   - Finite elements

5. **Asymptotic Expansions**
   - Small parameter approximations
   - Singular perturbation theory

---

## 15. Worked Example: Custom SDE

**Problem:** Solve

$$
dX_t = (1 - X_t)\,dt + \sqrt{X_t}\,dW_t, \quad X_0 = 1
$$

**Step 1: Recognize structure**

This is CIR-type with $\kappa = 1$, $\theta = 1$, $\sigma = 1$.

**Step 2: Check Feller condition**

$$
2\kappa\theta = 2(1)(1) = 2 \geq \sigma^2 = 1 \quad \checkmark
$$

Therefore $X_t > 0$ for all $t > 0$.

**Step 3: No closed-form path solution**

But we can find:

**Moments:**

$$
\mathbb{E}[X_t] = 1 \quad \text{(constant!)}
$$

$$
\text{Var}[X_t] = e^{-t}(1 - e^{-t}) + \frac{1}{2}(1 - e^{-t})^2
$$

**Distribution:** Scaled non-central $\chi^2$ with $\nu = 4$.

**Simulation:** Use exact CIR simulation or Euler-Maruyama with positivity preservation.

---

## 16. The Art of Solving SDEs

### 16.1 Recognition is Key

Success requires **pattern recognition**:

1. **Identify structure** (linear, multiplicative, separable)
2. **Choose method** based on structure
3. **Apply technique** systematically
4. **Verify solution** (see Verifying Solutions section)

### 16.2 When to Stop Looking

If after trying:
- Direct integration
- Standard transformations (log, power, Lamperti)
- Integrating factor

you still don't have a solution, the SDE likely has **no closed form**.

Switch to:
- Numerical methods
- Moment analysis
- Asymptotic approximations

### 16.3 Value of Analytical Solutions

Even when numerical methods are needed, analytical solutions provide:

1. **Intuition** for long-term behavior
2. **Benchmarks** for numerical schemes
3. **Special cases** for testing
4. **Parameter bounds** from limiting cases
5. **Connections** to PDEs and probability

### 16.4 The Complete Toolkit

Solving SDEs requires combining:
- **Stochastic calculus** (Itô's lemma)
- **ODE techniques** (integrating factors)
- **PDE methods** (Feynman-Kac)
- **Probability theory** (martingales, measures)
- **Numerical analysis** (when all else fails)

Mastering these connections is the essence of modern quantitative finance.

---

## 17. Cross-References

For related topics, see:

- **SDE Examples**: Detailed properties of standard models
- **Verifying Solutions**: How to check if your solution is correct
- **SDE Simulation**: Numerical methods when analytical solutions don't exist
- **Moment Analysis**: Computing statistical properties
- **Diffusion Processes**: Generator theory and PDEs

Understanding how to solve SDEs is central to all of quantitative finance and computational stochastic calculus.
