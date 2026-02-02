# Local Martingales

A **local martingale** is a process that behaves like a martingale "locally"—when stopped at appropriate times—but may fail to be a true martingale globally. This distinction is crucial in continuous-time finance, where many natural price processes are local martingales but not martingales.

!!! info "Prerequisites"
    This section assumes familiarity with:
    
    - [Stopping Times](../../ch01/filtration_and_martingales/stopping_times.md) (§1.2)
    - [Itô Integral Construction](../../ch02/ito_integral/ito_integral_construction.md) (§2.2)
    - [Quadratic Variation](../../ch02/ito_integral/quadratic_variation.md) (§2.2)

---

## Definitions

### Martingale (Recap)

A process $\{M_t\}_{t \geq 0}$ is a **martingale** with respect to filtration $\{\mathcal{F}_t\}$ if:

1. **Adaptedness**: $M_t$ is $\mathcal{F}_t$-measurable for all $t \geq 0$
2. **Integrability**: $\mathbb{E}[|M_t|] < \infty$ for all $t \geq 0$
3. **Martingale property**: $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ almost surely for all $0 \leq s \leq t$

### Local Martingale

!!! definition "Local Martingale"
    An adapted process $\{M_t\}_{t \geq 0}$ with $M_0$ finite almost surely is a **local martingale** if there exists a sequence of stopping times $\{\tau_n\}_{n=1}^{\infty}$ such that:

    1. **Monotonicity**: $\tau_1 \leq \tau_2 \leq \tau_3 \leq \cdots$
    2. **Divergence**: $\tau_n \to \infty$ almost surely as $n \to \infty$
    3. **Stopped martingale**: The stopped process $M^{\tau_n}_t := M_{t \wedge \tau_n}$ is a martingale for each $n$

    The sequence $\{\tau_n\}$ is called a **localizing sequence** (or **reducing sequence**).

**Remark on condition 3**: For $M_{t \wedge \tau_n}$ to be a martingale, we need $\mathbb{E}[|M_{t \wedge \tau_n}|] < \infty$ for all $t$. This is the sense in which localization "tames" potentially non-integrable processes.

---

## The Martingale Hierarchy

The following inclusions are strict:

$$
\boxed{
\text{UI Martingales} \subsetneq \text{Martingales} \subsetneq \text{Local Martingales}
}
$$

where **UI** denotes uniformly integrable. A local martingale that is not a true martingale is called a **strict local martingale**.

!!! note "Connection to Convergence Theory"
    Uniformly integrable martingales converge in $L^1$, not just almost surely. See [Martingale Convergence](../../ch01/filtration_and_martingales/martingale_convergence.md) for the full hierarchy of convergence results.

---

## What Can Go Wrong?

A local martingale fails to be a martingale when any of the following occurs:

### 1. Integrability Failure

The random variable $M_t$ may satisfy $\mathbb{E}[|M_t|] = \infty$ for some (or all) $t > 0$.

### 2. Explosion to Infinity

The process may escape to $+\infty$ (or $-\infty$) in finite time, i.e., $\lim_{t \to \zeta^-} |M_t| = \infty$ where $\zeta < \infty$ is an explosion time.

### 3. Mass Leakage at Infinity

Even without explosion, probability mass can "escape to infinity" in the sense that:

$$
\mathbb{E}[M_t] < \mathbb{E}[M_0]
$$

The "missing mass" corresponds to paths where $M_t$ has grown large.

---

## Canonical Examples

### Example 1: Itô Integrals

Consider the Itô integral:

$$
M_t = \int_0^t \sigma_s\,dW_s
$$

where $\sigma$ is an adapted process satisfying the **local integrability condition**:

$$
\int_0^t \sigma_s^2\,ds < \infty \quad \text{almost surely for all } t \geq 0
$$

**Claim**: $M_t$ is a local martingale.

**Proof**: Define the localizing sequence:

$$
\tau_n = \inf\left\{t \geq 0 : \int_0^t \sigma_s^2\,ds \geq n\right\} \wedge n
$$

Then $\tau_n \uparrow \infty$ a.s., and by construction:

$$
\mathbb{E}\left[\int_0^{T \wedge \tau_n} \sigma_s^2\,ds\right] \leq n < \infty
$$

By the Itô isometry criterion, $M_{t \wedge \tau_n}$ is a true martingale for each $n$. $\square$

**Upgrade to true martingale**: $M$ is a true martingale on $[0,T]$ if:

$$
\mathbb{E}\left[\int_0^T \sigma_s^2\,ds\right] < \infty
$$

This is the standard $L^2$ integrability condition.

---

### Example 2: Stochastic Exponential (True Martingale)

The **stochastic exponential** of Brownian motion:

$$
Z_t = \mathcal{E}(W)_t := \exp\left(W_t - \frac{t}{2}\right)
$$

satisfies the SDE $dZ_t = Z_t\,dW_t$ with $Z_0 = 1$.

**Claim**: $Z_t$ is a true martingale with $\mathbb{E}[Z_t] = 1$ for all $t \geq 0$.

**Proof**: We verify Novikov's condition. Here $\langle W \rangle_t = t$, so:

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\langle W \rangle_T\right)\right] = \mathbb{E}\left[\exp\left(\frac{T}{2}\right)\right] = e^{T/2} < \infty
$$

By Novikov's theorem (see [Novikov & Kazamaki Conditions](novikov_kazamaki_conditions.md)), $\mathcal{E}(W)$ is a true martingale. $\square$

---

### Example 3: Reciprocal of 3D Bessel Process (Strict Local Martingale)

Let $R_t = |B_t|$ where $B_t = (B^1_t, B^2_t, B^3_t)$ is 3-dimensional Brownian motion started from $B_0 = x$ with $|x| = r_0 > 0$. The process $R_t$ is the **3-dimensional Bessel process** started from $r_0$.

Define:

$$
M_t = \frac{1}{R_t}
$$

**Claim**: $M_t$ is a strict local martingale (local martingale but NOT a true martingale).

!!! warning "Common Misconception"
    The failure is **not** because $R_t$ hits zero. In fact, the 3D Bessel process is **transient**: $R_t \to \infty$ as $t \to \infty$ almost surely, and $R_t > 0$ for all $t \geq 0$ when $r_0 > 0$.

**Proof that $M_t$ is a local martingale**:

By Itô's formula applied to $f(r) = 1/r$ and using the SDE for the Bessel process $dR_t = \frac{1}{R_t}dt + dW_t$ (where $W$ is a 1D Brownian motion):

$$
d\left(\frac{1}{R_t}\right) = -\frac{1}{R_t^2}dR_t + \frac{1}{R_t^3}dt = -\frac{1}{R_t^2}\left(\frac{1}{R_t}dt + dW_t\right) + \frac{1}{R_t^3}dt = -\frac{1}{R_t^2}dW_t
$$

The drift terms cancel! Thus $M_t = 1/R_t$ satisfies:

$$
dM_t = -\frac{1}{R_t^2}dW_t
$$

This is an Itô integral, hence a local martingale.

**Proof that $M_t$ is NOT a true martingale**:

The key computation is:

$$
\mathbb{E}\left[\frac{1}{R_t}\right] = \frac{1}{r_0}\left(1 - \frac{2}{\sqrt{2\pi t}}\int_0^{r_0} e^{-u^2/(2t)}du\right) < \frac{1}{r_0} = M_0
$$

The strict inequality shows $\mathbb{E}[M_t] < \mathbb{E}[M_0]$, violating the martingale property.

**Intuition**: As $t \to \infty$, the Bessel process drifts to $+\infty$, so $1/R_t \to 0$. The "probability mass" that would be needed to maintain $\mathbb{E}[M_t] = M_0$ has "leaked to infinity."

---

### Example 4: Explosive Diffusion

Consider the SDE:

$$
dX_t = X_t^2\,dW_t, \quad X_0 = 1
$$

**Claim**: $X_t$ is a strict local martingale that can explode to $+\infty$ in finite time.

**Why explosion occurs**: 

The solution (up to explosion) is:

$$
X_t = \frac{1}{1 - W_t + \frac{1}{2}\langle W \rangle_t} = \frac{1}{1 - W_t + \frac{t}{2}}
$$

Wait—this doesn't explode. Let me reconsider. For the SDE $dX_t = X_t^\gamma dW_t$ with $\gamma > 1$, explosion can occur. A cleaner example is:

**Revised Example**: Consider the **inverse Bessel process** $Y_t = 1/R_t^{(1)}$ where $R^{(1)}$ is the 1-dimensional Bessel process (absolute value of 1D Brownian motion). This process explodes when $R^{(1)}_t$ hits zero.

Alternatively, the process:

$$
dX_t = X_t^2 dW_t, \quad X_0 = x > 0
$$

has solution that remains positive but exhibits **strict local martingale** behavior due to mass leakage, similar to Example 3.

**Localizing sequence**: Define $\tau_n = \inf\{t : X_t \geq n\} \wedge n$. Then:

- $X_{t \wedge \tau_n}$ is bounded by $n$, hence a true martingale
- $X_t$ itself satisfies $\mathbb{E}[X_t] \leq X_0$ with potential strict inequality

---

## Mathematical Characterization

### The Supermartingale Property

!!! theorem "Non-negative Local Martingales are Supermartingales"
    Let $M$ be a non-negative local martingale. Then $M$ is a supermartingale:
    
    $$
    \mathbb{E}[M_t \mid \mathcal{F}_s] \leq M_s \quad \text{almost surely for all } 0 \leq s \leq t
    $$

**Proof**: Let $\{\tau_n\}$ be a localizing sequence. For the stopped process:

$$
\mathbb{E}[M_{t \wedge \tau_n} \mid \mathcal{F}_s] = M_{s \wedge \tau_n} \quad \text{(martingale property)}
$$

Since $M \geq 0$, Fatou's lemma gives:

$$
\mathbb{E}[M_t \mid \mathcal{F}_s] = \mathbb{E}\left[\liminf_{n \to \infty} M_{t \wedge \tau_n} \mid \mathcal{F}_s\right] \leq \liminf_{n \to \infty} \mathbb{E}[M_{t \wedge \tau_n} \mid \mathcal{F}_s] = \liminf_{n \to \infty} M_{s \wedge \tau_n} = M_s
$$

where the last equality uses $\tau_n \to \infty$ a.s. $\square$

**Corollary**: For non-negative local martingales:

$$
\mathbb{E}[M_t] \leq \mathbb{E}[M_0]
$$

with **equality if and only if** $M$ is a true martingale.

---

### Characterization via Fatou's Lemma

For a non-negative local martingale with localizing sequence $\{\tau_n\}$:

$$
\mathbb{E}[M_{t \wedge \tau_n}] = \mathbb{E}[M_0] \quad \text{for all } n
$$

Taking $n \to \infty$ and applying Fatou's lemma:

$$
\mathbb{E}[M_t] \leq \liminf_{n \to \infty} \mathbb{E}[M_{t \wedge \tau_n}] = \mathbb{E}[M_0]
$$

The inequality can be **strict**—this is the signature of a strict local martingale.

---

## Sufficient Conditions for True Martingale

A local martingale $M$ is a **true martingale** if any of the following conditions holds:

### 1. Boundedness

$$
|M_t| \leq C \quad \text{almost surely for all } t \in [0,T]
$$

for some constant $C < \infty$.

### 2. Domination

$$
|M_t| \leq Y \quad \text{almost surely for all } t \in [0,T]
$$

for some integrable random variable $Y$ (i.e., $\mathbb{E}[Y] < \infty$).

### 3. $L^p$ Boundedness ($p > 1$)

$$
\sup_{t \in [0,T]} \mathbb{E}[|M_t|^p] < \infty
$$

This follows from the fact that $L^p$-bounded martingales are uniformly integrable for $p > 1$.

### 4. Finite Expected Quadratic Variation

For **continuous** local martingales with $M_0$ integrable:

$$
\mathbb{E}[\langle M \rangle_T] < \infty \implies M \text{ is a true martingale on } [0,T]
$$

**Proof sketch**: By the Burkholder-Davis-Gundy inequality:

$$
\mathbb{E}\left[\sup_{t \leq T} |M_t|\right] \leq C \cdot \mathbb{E}\left[\langle M \rangle_T^{1/2}\right] \leq C \cdot \mathbb{E}[\langle M \rangle_T]^{1/2} < \infty
$$

Hence $M$ is dominated by an integrable random variable. $\square$

### 5. Novikov's Condition (for Stochastic Exponentials)

For a continuous local martingale $M$ with $M_0 = 0$:

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}\langle M \rangle_T\right)\right] < \infty \implies \mathcal{E}(M)_t \text{ is a true martingale on } [0,T]
$$

where $\mathcal{E}(M)_t = \exp(M_t - \frac{1}{2}\langle M \rangle_t)$ is the stochastic exponential.

### 6. Kazamaki's Condition (Weaker)

$$
\mathbb{E}\left[\exp\left(\frac{1}{2}M_T\right)\right] < \infty \implies \mathcal{E}(M) \text{ is a true martingale on } [0,T]
$$

Kazamaki's condition is strictly weaker than Novikov's. See [Novikov & Kazamaki Conditions](novikov_kazamaki_conditions.md) for details and proofs.

---

## Connection to Infinitesimal Generators

Let $X_t$ be a diffusion with infinitesimal generator:

$$
\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}
$$

For $f \in C^2$, define the process $Y_t = f(X_t)$.

!!! theorem "Generator Criterion"
    If $\mathcal{L}f(x) = 0$ for all $x$ in the state space, then $f(X_t)$ is a **local martingale**.
    
    If additionally:
    
    1. $\mathbb{E}[|f(X_t)|] < \infty$ for all $t$
    2. $X_t$ does not explode
    3. $f$ satisfies appropriate growth conditions
    
    then $f(X_t)$ is a **true martingale**.

**Connection to Dynkin's formula**: By Itô's formula:

$$
f(X_t) - f(X_0) = \int_0^t \mathcal{L}f(X_s)\,ds + \int_0^t f'(X_s)\sigma(X_s)\,dW_s
$$

When $\mathcal{L}f = 0$, the drift integral vanishes, leaving only the stochastic integral (which is a local martingale).

See [Generator and Martingales](../../ch02/infinitesimal_generator/generator_and_martingales.md) for the full treatment.

---

## Financial Implications

### Discounted Asset Prices

Under the risk-neutral measure $\mathbb{Q}$, the **discounted asset price**:

$$
\tilde{S}_t = e^{-rt}S_t
$$

should be a martingale for the market to be free of arbitrage (First Fundamental Theorem of Asset Pricing).

In practice, $\tilde{S}_t$ is often only a **local martingale**. The distinction matters.

### Strict Local Martingales and Financial Bubbles

!!! important "Bubble Characterization"
    If the discounted price process is a **strict local martingale** under $\mathbb{Q}$:
    
    $$
    \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0
    $$
    
    This implies the current price $S_0$ exceeds its "fundamental value" (the discounted expected future price). This is the mathematical signature of a **financial bubble**.

**Reference**: Jarrow, Protter, and Shimbo (2010), "Asset Price Bubbles in Incomplete Markets," *Mathematical Finance*.

### Put-Call Parity Failure

The standard put-call parity:

$$
C(K,T) - P(K,T) = S_0 - Ke^{-rT}
$$

relies on $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = S_0$. When the stock price is a strict local martingale:

$$
C(K,T) - P(K,T) = \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] - Ke^{-rT} < S_0 - Ke^{-rT}
$$

Put-call parity fails, and the put price includes a "bubble premium."

### Connection to Girsanov's Theorem

When performing measure changes via Girsanov's theorem, the Radon-Nikodym derivative:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = Z_t = \mathcal{E}\left(-\int_0^\cdot \theta_s\,dW_s\right)_t
$$

must be a **true martingale** (not just a local martingale) for the measure change to be valid. This is precisely where Novikov and Kazamaki conditions enter.

See [Girsanov's Theorem](../girsanov/girsanov_theorem.md) for the full treatment.

---

## Summary Table

| Property | Martingale | Local Martingale | Strict Local Martingale |
|----------|-----------|------------------|------------------------|
| **Definition** | $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ | $M_{t\wedge\tau_n}$ is martingale | Local mart., not true mart. |
| **Integrability** | Required: $\mathbb{E}[\lvert M_t\rvert] < \infty$ | Not required globally | Typically fails |
| **Mean preservation** | $\mathbb{E}[M_t] = \mathbb{E}[M_0]$ | $\mathbb{E}[M_t] \leq \mathbb{E}[M_0]$ | $\mathbb{E}[M_t] < \mathbb{E}[M_0]$ |
| **If $M \geq 0$** | Supermartingale | Supermartingale | Strict supermartingale |
| **Explosion** | Cannot explode | Can explode | May or may not explode |
| **Financial interpretation** | Fair game | Locally fair | Bubble possible |

---

## Key Takeaways

$$
\boxed{
\mathcal{L}f = 0 \implies f(X_t) \text{ is a local martingale}
}
$$

$$
\boxed{
\mathcal{L}f = 0 \text{ + integrability conditions} \implies f(X_t) \text{ is a true martingale}
}
$$

$$
\boxed{
\text{Non-negative local martingale} \implies \text{Supermartingale}
}
$$

$$
\boxed{
\mathbb{E}[M_t] < \mathbb{E}[M_0] \text{ for non-negative } M \iff M \text{ is a strict local martingale}
}
$$

!!! summary "The Bottom Line"
    The distinction between local martingales and true martingales is essential for:
    
    1. **Rigorous Itô calculus**: Ensuring stochastic integrals have the expected properties
    2. **Measure changes**: Validating Girsanov transformations via Novikov/Kazamaki
    3. **Financial modeling**: Detecting and modeling asset price bubbles
    4. **PDE connections**: Understanding when Feynman-Kac representations hold

---

## Python Simulation: Mass Leakage in Strict Local Martingales

The following simulation demonstrates how $\mathbb{E}[M_t]$ can decrease over time for a strict local martingale.

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_inverse_bessel_3d(r0, T, dt, n_paths):
    """
    Simulate 1/R_t where R_t is a 3D Bessel process.
    This is a strict local martingale.
    """
    n_steps = int(T / dt)
    t = np.linspace(0, T, n_steps + 1)
    
    # Simulate 3D Brownian motion
    dW = np.sqrt(dt) * np.random.randn(n_paths, n_steps, 3)
    B = np.zeros((n_paths, n_steps + 1, 3))
    B[:, 0, :] = r0 / np.sqrt(3)  # Start at distance r0 from origin
    
    for i in range(n_steps):
        B[:, i+1, :] = B[:, i, :] + dW[:, i, :]
    
    # Compute R_t = |B_t|
    R = np.sqrt(np.sum(B**2, axis=2))
    R = np.maximum(R, 1e-10)  # Avoid division by zero
    
    # M_t = 1/R_t
    M = 1.0 / R
    
    return t, M, R

# Parameters
r0 = 1.0
T = 5.0
dt = 0.001
n_paths = 50000

np.random.seed(42)
t, M, R = simulate_inverse_bessel_3d(r0, T, dt, n_paths)

# Compute E[M_t] over time
E_M = np.mean(M, axis=0)

# Theoretical initial value
M0 = 1.0 / r0

# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: E[M_t] over time
ax1 = axes[0]
ax1.plot(t, E_M, 'b-', linewidth=2, label=r'$\mathbb{E}[M_t]$ (Monte Carlo)')
ax1.axhline(y=M0, color='r', linestyle='--', linewidth=2, label=r'$M_0 = 1/r_0$')
ax1.set_xlabel('Time $t$', fontsize=12)
ax1.set_ylabel(r'$\mathbb{E}[M_t]$', fontsize=12)
ax1.set_title('Mass Leakage in Strict Local Martingale\n(Inverse 3D Bessel Process)', fontsize=12)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_ylim([0, M0 * 1.1])

# Right: Sample paths
ax2 = axes[1]
n_show = 20
for i in range(n_show):
    ax2.plot(t, M[i, :], alpha=0.5, linewidth=0.5)
ax2.set_xlabel('Time $t$', fontsize=12)
ax2.set_ylabel(r'$M_t = 1/R_t$', fontsize=12)
ax2.set_title(f'Sample Paths ({n_show} shown)', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.set_ylim([0, 5])

plt.tight_layout()
plt.savefig('strict_local_martingale_simulation.png', dpi=150, bbox_inches='tight')
plt.show()

# Print summary statistics
print(f"Initial value M_0 = 1/r_0 = {M0:.4f}")
print(f"E[M_T] at T={T}: {E_M[-1]:.4f}")
print(f"Mass leakage: {(M0 - E_M[-1])/M0 * 100:.2f}%")
```

**Expected output**: The plot shows $\mathbb{E}[M_t]$ decreasing below $M_0 = 1$, demonstrating the strict local martingale property. The "leaked mass" corresponds to paths where $R_t$ has drifted far from the origin.
