# Girsanov's Theorem

Girsanov's theorem is a cornerstone of stochastic calculus and mathematical finance. It explains how **changing probability measures changes drift** while preserving Brownian motion structure, enabling the construction of risk-neutral measures for derivative pricing.

This section develops the theorem in three stages: intuition via discrete and continuous examples, formal statement and proof, and financial applications.

---

## 1. Motivation: Why Change Measures?

### **Two Probability Worlds**

In financial modeling, we distinguish between:

- **Physical (real-world) measure $\mathbb{P}$**: Describes actual market dynamics
  - Asset expected returns include risk premia
  - Example: Stock drift $\mu > r$ (equity risk premium)

- **Risk-neutral (pricing) measure $\mathbb{Q}$**: Mathematical construct for valuation
  - Discounted asset prices are martingales
  - Example: Stock drift equals $r$ (no arbitrage)

**The challenge**: Brownian motion under $\mathbb{P}$ generally has non-zero drift under $\mathbb{Q}$. We need a mechanism to transform one measure into another while preserving the Brownian structure.

**Girsanov's answer**: Drift is not intrinsic—it depends on the probability measure. A change of measure can remove or modify drift.

---

## 2. Discrete Analogy: The Biased Coin

Before tackling continuous-time processes, consider a discrete example that captures the essential idea.

### **Setup: Biased Coin**

A coin shows heads with probability $p$ and tails with probability $1-p$ under measure $\mathbb{P}$, where $p \neq \frac{1}{2}$ (biased).

**Goal**: Define a new measure $\mathbb{Q}$ under which the coin is fair (both outcomes have probability $\frac{1}{2}$).

### **Construction: Radon-Nikodym Derivative**

Define the measure change via:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}} = Z
$$



where

$$
Z = \frac{1/2}{p} \cdot \mathbf{1}_{\text{Heads}} + \frac{1/2}{1-p} \cdot \mathbf{1}_{\text{Tails}}
$$



### **Verification**

Under $\mathbb{Q}$:

$$
\mathbb{Q}(\text{Heads}) = \mathbb{P}(\text{Heads}) \cdot \frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\text{Heads}} = p \cdot \frac{1/2}{p} = \frac{1}{2}
$$




$$
\mathbb{Q}(\text{Tails}) = (1-p) \cdot \frac{1/2}{1-p} = \frac{1}{2}
$$



**Interpretation**: The Radon-Nikodym derivative **reweights** outcomes inversely proportional to their original bias, making the coin fair under the new measure.

### **Connection to Girsanov**

This example captures the core mechanism:
- **Bias** (drift in continuous time) is a property of the measure, not the process
- **Reweighting** via exponential martingale changes the measure
- **Structure preserved**: The coin remains a coin (Brownian motion remains Brownian)

---

## 3. Continuous Intuition: Brownian Motion with Drift

### **The Setup**

Let $W_t$ be standard Brownian motion under $\mathbb{P}$. Define:

$$
Y_t := W_t + \theta t
$$



Under $\mathbb{P}$, this has **deterministic drift** $\theta$ and is **not** a Brownian motion.

**Question**: Can we find a measure $\mathbb{Q}$ under which $Y_t$ **is** a standard Brownian motion?

### **The Answer: Yes, via Measure Change**

Define the **exponential martingale** (Radon-Nikodym derivative):

$$
Z_t = \exp\left(-\theta W_t - \frac{1}{2}\theta^2 t\right)
$$



Set:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_t} = Z_t
$$



**Key properties of $Z_t$**:
1. $Z_0 = 1$ (measures agree at $t=0$)
2. $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$ (probability mass preserved)
3. $Z_t$ is a martingale under $\mathbb{P}$ (ensures valid probability measure)

### **Result**

Under $\mathbb{Q}$, the process $Y_t = W_t + \theta t$ **is a standard Brownian motion**.

**Proof sketch**: The drift $\theta$ gets absorbed into the measure change, leaving $Y_t$ driftless under $\mathbb{Q}$.

### **What Changes—and What Doesn't**

After the measure change:
- ✓ **Drift changes**: $\theta$ absorbed into measure
- ✓ **Brownian structure preserved**: $Y_t$ is Brownian under $\mathbb{Q}$
- ✗ **Volatility unchanged**: Quadratic variation remains $t$
- ✗ **Filtration unchanged**: Information structure identical

---

## 4. Path Reweighting Interpretation

### **Paths as Basic Outcomes**

Brownian motion generates **paths** $\omega: [0,T] \to \mathbb{R}$. A probability measure assigns **weights** to these paths.

### **How $Z_t$ Reweights**

The exponential martingale

$$
Z_t = \exp\left(-\theta W_t - \frac{1}{2}\theta^2 t\right)
$$



has two components:

1. **$-\theta W_t$**: Tilts paths upward/downward
   - If $\theta > 0$: Downweight paths with large $W_t$ (positive drift removed)
   - If $\theta < 0$: Upweight paths with large $W_t$ (negative drift removed)

2. **$-\frac{1}{2}\theta^2 t$**: Normalization ensuring $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$
   - Without this, total probability mass wouldn't be preserved
   - This is the **entropy correction** term

**Example**: For $\theta = 1$, paths that reach $W_T = 2$ get weight $e^{-2 - \frac{1}{2}T}$ relative to their original probability.

---

## 5. Financial Motivation: Stock Price Dynamics

### **Stock Under Physical Measure**

Consider geometric Brownian motion:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$



or equivalently:

$$
S_t = S_0 \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right)
$$



Under $\mathbb{P}$:
- Expected return = $\mu$ (includes equity risk premium)
- Not a martingale after discounting

### **Requirement for Pricing**

For no-arbitrage pricing, we need:

$$
e^{-rt}S_t \quad \text{is a martingale under } \mathbb{Q}
$$



This requires replacing drift $\mu$ with risk-free rate $r$.

### **Girsanov Construction**

Set:

$$
\theta = \frac{\mu - r}{\sigma}
$$



(This is the **market price of risk** or **Sharpe ratio**.)

Define the measure change:

$$
Z_t = \exp\left(-\theta W_t - \frac{1}{2}\theta^2 t\right) = \exp\left(-\frac{\mu-r}{\sigma}W_t - \frac{1}{2}\left(\frac{\mu-r}{\sigma}\right)^2 t\right)
$$



### **Result Under $\mathbb{Q}$**

Define:

$$
\tilde{W}_t := W_t + \theta t = W_t + \frac{\mu-r}{\sigma}t
$$



By Girsanov's theorem, $\tilde{W}_t$ is a Brownian motion under $\mathbb{Q}$.

The stock price becomes:

$$
S_t = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)t + \sigma \tilde{W}_t\right)
$$



**Verification**:

$$
e^{-rt}S_t = S_0\exp\left(-\frac{1}{2}\sigma^2 t + \sigma \tilde{W}_t\right)
$$



is a martingale under $\mathbb{Q}$ (standard property of exponential Brownian motion).

---

## 6. Formal Statement of Girsanov's Theorem

### **Setup**

Let $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})$ be a filtered probability space with $W_t$ a standard Brownian motion adapted to $\{\mathcal{F}_t\}$.

Let $\theta_t$ be an adapted process satisfying:

$$
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta_s^2 ds\right)\right] < \infty \quad \text{(Novikov condition)}
$$



Define the **exponential martingale**:

$$
Z_t = \exp\left(-\int_0^t \theta_s dW_s - \frac{1}{2}\int_0^t \theta_s^2 ds\right)
$$



### **Theorem Statement**

Define a new probability measure $\mathbb{Q}$ on $(\Omega, \mathcal{F}_T)$ by:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_T} = Z_T
$$



Then the process

$$
\boxed{\tilde{W}_t := W_t + \int_0^t \theta_s ds}
$$



is a **standard Brownian motion** under $\mathbb{Q}$.

### **Interpretation**

- **Under $\mathbb{P}$**: $W_t$ is Brownian, $\tilde{W}_t$ has drift $\theta_t$
- **Under $\mathbb{Q}$**: $\tilde{W}_t$ is Brownian, $W_t$ would have drift $-\theta_t$

The drift has been "transferred" from the process to the measure.

---

## 7. Proof of Girsanov's Theorem

We verify the two defining properties of Brownian motion: martingale property and quadratic variation.

### **Step 1: $Z_t$ is a Martingale**

By Itô's lemma applied to $Z_t = \exp(Y_t)$ where $Y_t = -\int_0^t \theta_s dW_s - \frac{1}{2}\int_0^t \theta_s^2 ds$:


$$
dZ_t = Z_t\left(-\theta_t dW_t - \frac{1}{2}\theta_t^2 dt + \frac{1}{2}\theta_t^2 dt\right) = -Z_t\theta_t dW_t
$$



This is a stochastic integral with no $dt$ term, so $Z_t$ is a local martingale. The Novikov condition ensures it's a true martingale with $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$.

### **Step 2: Martingale Property of $\tilde{W}_t$ Under $\mathbb{Q}$**

For any $s < t$ and bounded $\mathcal{F}_s$-measurable $\xi$:


$$
\mathbb{E}^{\mathbb{Q}}[\tilde{W}_t - \tilde{W}_s | \mathcal{F}_s] = \mathbb{E}^{\mathbb{P}}\left[Z_t(\tilde{W}_t - \tilde{W}_s) \Big| \mathcal{F}_s\right] / Z_s
$$



Expanding $\tilde{W}_t - \tilde{W}_s = W_t - W_s + \int_s^t \theta_u du$ and using the product rule:


$$
Z_t(\tilde{W}_t - \tilde{W}_s) = Z_s(W_t - W_s) + Z_s\int_s^t \theta_u du - \int_s^t Z_u\theta_u(W_t - W_u) du
$$



Taking conditional expectation under $\mathbb{P}$:
- First term: $\mathbb{E}^{\mathbb{P}}[Z_s(W_t - W_s)|\mathcal{F}_s] = 0$ (Brownian increment independent)
- Second and third terms cancel by martingale property of $\int Z_u\theta_u dW_u$

Therefore:

$$
\mathbb{E}^{\mathbb{Q}}[\tilde{W}_t - \tilde{W}_s | \mathcal{F}_s] = 0
$$



So $\tilde{W}_t$ is a martingale under $\mathbb{Q}$.

### **Step 3: Quadratic Variation**

The quadratic variation is unchanged by measure change (it's a pathwise property):

$$
\langle \tilde{W} \rangle_t = \langle W \rangle_t + \langle \int_0^\cdot \theta_s ds \rangle_t = t + 0 = t
$$



(Finite variation processes have zero quadratic variation.)

### **Step 4: Lévy Characterization**

A continuous martingale with quadratic variation $t$ is a Brownian motion (Lévy's characterization theorem).

Therefore, $\tilde{W}_t$ is a standard Brownian motion under $\mathbb{Q}$. ∎

---

## 8. Examples and Applications

### **Example 1: Constant Drift**

**Problem**: Given $dX_t = \mu dt + \sigma dW_t$ under $\mathbb{P}$, find $\mathbb{Q}$ such that $X_t$ is a martingale.

**Solution**:
- Set $\theta_t = \mu/\sigma$ (constant)
- Define $Z_t = \exp(-\frac{\mu}{\sigma}W_t - \frac{1}{2}\frac{\mu^2}{\sigma^2}t)$
- Under $\mathbb{Q}$ with $d\mathbb{Q}/d\mathbb{P} = Z_T$:


$$
\tilde{W}_t = W_t + \frac{\mu}{\sigma}t
$$



is Brownian, and:

$$
dX_t = \sigma d\tilde{W}_t
$$



(drift removed).

### **Example 2: Time-Varying Drift**

**Problem**: $dX_t = \mu(t) dt + \sigma dW_t$ under $\mathbb{P}$.

**Solution**:
- Set $\theta_t = \mu(t)/\sigma$
- $Z_t = \exp(-\frac{1}{\sigma}\int_0^t \mu(s)dW_s - \frac{1}{2\sigma^2}\int_0^t \mu(s)^2 ds)$
- Under $\mathbb{Q}$:


$$
d\tilde{W}_t = dW_t + \frac{\mu(t)}{\sigma}dt
$$



and $X_t$ evolves as $dX_t = \sigma d\tilde{W}_t$.

### **Example 3: Black-Scholes Risk-Neutral Measure**

**Stock under $\mathbb{P}$**:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$



**Measure change**:

$$
\theta = \frac{\mu - r}{\sigma}, \quad Z_t = \exp\left(-\frac{\mu-r}{\sigma}W_t - \frac{1}{2}\left(\frac{\mu-r}{\sigma}\right)^2 t\right)
$$



**Stock under $\mathbb{Q}$**:

$$
dS_t = rS_t dt + \sigma S_t d\tilde{W}_t
$$



**Option pricing**: For European call with payoff $(S_T - K)^+$:

$$
C_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]
$$



This expectation can be evaluated to yield the Black-Scholes formula.

---

## 9. Computational Illustration

### **Python: Visualizing Measure Change**
```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Parameters
T = 1.0
N = 1000
n_paths = 100
mu = 0.4      # Physical drift (high return)
sigma = 0.2
r = 0.05      # Risk-free rate

# Time grid
dt = T / N
t = np.linspace(0, T, N)

# Generate Brownian paths under P
dW = np.random.normal(0, np.sqrt(dt), (n_paths, N))
W = np.cumsum(dW, axis=1)

# Stock price under P
S_P = np.exp((mu - 0.5*sigma**2)*t + sigma*W)

# Girsanov reweighting
theta = (mu - r) / sigma
Z = np.exp(-theta*W[:, -1] - 0.5*theta**2*T)
Z_normalized = Z / Z.max()  # For visualization

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Under P: all paths equally visible
for i in range(n_paths):
    ax1.plot(t, S_P[i], 'darkred', alpha=0.3, lw=0.8)
ax1.set_title('Stock Paths Under Physical Measure P\n(drift = {:.0f}%)'.format(mu*100))
ax1.set_xlabel('Time')
ax1.set_ylabel('Stock Price')
ax1.grid(True, alpha=0.3)

# Under Q: paths reweighted by Z
for i in range(n_paths):
    ax2.plot(t, S_P[i], 'darkblue', alpha=Z_normalized[i], lw=0.8)
ax2.set_title('Same Paths Under Risk-Neutral Measure Q\n(Girsanov reweighting)')
ax2.set_xlabel('Time')
ax2.set_ylabel('Stock Price')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Interpretation**: Paths with upward drift under $\mathbb{P}$ get downweighted under $\mathbb{Q}$ (faded), reflecting the removal of the risk premium.

---

## 10. Summary and Key Insights

### **What Girsanov Says**

> **Drift is measure-dependent, not intrinsic to the process.**

- A Brownian motion with drift under $\mathbb{P}$ becomes driftless under $\mathbb{Q}$
- The transformation preserves Brownian structure (martingale + quadratic variation)
- The measure change is encoded in an exponential martingale $Z_t$

### **Why It Matters**

1. **Risk-neutral pricing**: Enables transformation from real-world to pricing measure
2. **Martingale representation**: Discounted asset prices become martingales
3. **Stochastic control**: Optimality conditions often require measure changes
4. **Filtering theory**: Observation noise can be handled via measure transformation

### **The Mathematical Insight**

The theorem reveals a deep duality:
- **Drift in the process** ↔ **Tilt in the measure**
- Removing drift from the process = adding tilt to the measure
- The exponential form $e^{-\theta W - \frac{1}{2}\theta^2 t}$ is the unique way to preserve probability structure

### **Connection to Binomial Model**

Girsanov is the **continuous-time analog** of risk-neutral probability $q$ in the binomial model:
- Discrete: Change from $\mathbb{P}$ to $\mathbb{Q}$ by setting $\mathbb{Q}(\text{up}) = q$
- Continuous: Change from $\mathbb{P}$ to $\mathbb{Q}$ via Radon-Nikodym derivative $Z_t$
- Both make discounted prices martingales

Girsanov's theorem is the rigorous foundation for all continuous-time asset pricing models.
