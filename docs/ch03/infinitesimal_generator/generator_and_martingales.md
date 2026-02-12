# Generator and Martingales

The infinitesimal generator $\mathcal{L}$ and martingales are deeply connected. This page develops the **Dynkin martingale** and the characterization of **harmonic functions**.

---

## The Dynkin Martingale

For a diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ with generator $\mathcal{L}$, define:

$$
\boxed{
M_t := f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds
}
$$

!!! abstract "Theorem"
    For $f \in C^2$, the process $M_t$ is a **local martingale**.
    
    Under integrability conditions, it is a **true martingale**.

---

## Why It's a Martingale

From Itô's lemma:

$$f(X_t) = f(X_0) + \int_0^t (\mathcal{L}f)(X_s)\,ds + \int_0^t f'(X_s)\sigma(X_s)\,dW_s$$

Rearranging:

$$M_t = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds = \int_0^t f'(X_s)\sigma(X_s)\,dW_s$$

The Itô integral is a (local) martingale, so $M_t$ is a (local) martingale.

!!! info "Interpretation"
    $$f(X_t) = \underbrace{f(X_0) + \int_0^t (\mathcal{L}f)(X_s)\,ds}_{\text{predictable drift}} + \underbrace{M_t}_{\text{martingale}}$$
    
    - **Drift**: systematic, predictable change (captured by $\mathcal{L}$)
    - **Martingale**: unpredictable fluctuations (zero-mean increments)

---

## Local vs True Martingale

$M_t$ is always a **local martingale**. For it to be a **true martingale**, we need:

$$\mathbb{E}\left[\int_0^t (f'(X_s)\sigma(X_s))^2\,ds\right] < \infty$$

| Condition | $M_t$ is... |
|-----------|-------------|
| $f \in C^2$ | Local martingale |
| + above integrability | True martingale |
| + bounded $f'\sigma$ | Uniformly integrable martingale |

### What's the Difference?

**True martingale**: 

- $\mathbb{E}[|M_t|] < \infty$ for all $t$
- $\mathbb{E}[M_t | \mathcal{F}_s] = M_s$ 
- Consequence: $\mathbb{E}[M_t] = \mathbb{E}[M_0] = 0$

**Local martingale**: 

- Only "locally" a martingale: there exist $\tau_n \uparrow \infty$ such that $M_{t \wedge \tau_n}$ is a true martingale
- **Problem**: May have $\mathbb{E}[M_t] \neq 0$ or even $\mathbb{E}[M_t] = -\infty$

### Optional Stopping Theorem

For a **true martingale** $M_t$ and stopping time $\tau$:

$$\mathbb{E}[M_\tau] = \mathbb{E}[M_0]$$

(under conditions: $\tau$ bounded, or $\mathbb{E}[\tau] < \infty$ with bounded increments, or $M$ uniformly integrable)

For a **local martingale**: this can **fail**.

### Why Dynkin's Formula Cares

Dynkin's formula:

$$\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}f)(X_s)\,ds\right]$$

The proof uses $\mathbb{E}[M_\tau] = 0$. This requires:

| $M_t$ is... | Dynkin's formula |
|-------------|------------------|
| True martingale + optional stopping conditions | ✓ Works directly |
| Local martingale only | ⚠ May fail without extra work |

### Localization (The Fix)

If $M_t$ is only a local martingale with localizing sequence $\tau_n \uparrow \infty$:

1. Apply Dynkin to $\tau \wedge \tau_n$ (works: $M_{t \wedge \tau_n}$ is a true martingale)
2. Take $n \to \infty$
3. Use dominated or monotone convergence to pass the limit

This is what "careful localization" means — extra technical work to handle the local martingale case.

!!! example "Classic Counterexample: Strict Local Martingale"
    Let $W_t$ be 3D Brownian motion with $|W_0| = 1$. Define $X_t = 1/|W_t|$.
    
    - $X_t$ is a **local martingale** (by Itô's lemma)
    - $X_t$ is **not** a true martingale
    - $\mathbb{E}[X_t] < X_0$ — the expectation **decreases**!
    
    Optional stopping fails: $\mathbb{E}[X_\tau] \neq X_0$ for some stopping times.

---

## Harmonic Functions

!!! abstract "Definition"
    A function $f$ is **$\mathcal{L}$-harmonic** (or simply harmonic) if:
    
    $$\mathcal{L}f(x) = 0 \quad \text{for all } x$$

### Harmonic ⟹ Martingale

If $\mathcal{L}f = 0$, then:

$$M_t = f(X_t) - f(X_0) - \int_0^t 0\,ds = f(X_t) - f(X_0)$$

So $f(X_t) - f(X_0)$ is a martingale, i.e., **$f(X_t)$ is a martingale**.

$$
\boxed{
\mathcal{L}f = 0 \quad \Longrightarrow \quad f(X_t) \text{ is a martingale}
}
$$

---

## Converse: Martingale ⟹ Harmonic?

The converse requires care.

### What We Can Say

If $f(X_t)$ is a martingale, then $M_t = f(X_t) - f(X_0)$ is a martingale with $M_0 = 0$.

But also $M_t = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds$ is a martingale.

So $\int_0^t (\mathcal{L}f)(X_s)\,ds$ must be a martingale. But it's also a continuous finite-variation process.

!!! success "Key Fact"
    A continuous martingale of finite variation is **constant**.

Therefore: $\int_0^t (\mathcal{L}f)(X_s)\,ds = 0$ for all $t$, a.s.

This implies: $(\mathcal{L}f)(X_s) = 0$ for a.e. $s$, along sample paths.

### The Subtlety

This says $\mathcal{L}f(x) = 0$ **for $x$ visited by the process**.

It does **not** automatically give $\mathcal{L}f(x) = 0$ for all $x$.

| Condition | Conclusion |
|-----------|------------|
| $f(X_t)$ martingale | $\mathcal{L}f(X_t) = 0$ a.e. along paths |
| + $X_t$ irreducible | $\mathcal{L}f(x) = 0$ for all $x$ in state space |
| + $f \in C^2$, $\mathcal{L}f$ continuous | $\mathcal{L}f(x) = 0$ everywhere |

!!! example "Counterexample Intuition"
    If $X_t$ never visits some region $A$, we learn nothing about $\mathcal{L}f$ on $A$ from observing $f(X_t)$.

---

## Correct Characterization

Under suitable regularity (e.g., $f \in C^2$, diffusion is non-degenerate):

$$
\boxed{
\mathcal{L}f(x) = 0 \;\forall x \quad \Longleftrightarrow \quad f(X_t) \text{ is a local martingale}
}
$$

!!! note "Why Local Martingale?"
    The equivalence uses **local martingale** (not true martingale) because:
    
    - **⟹ direction**: $\mathcal{L}f = 0$ makes $M_t = f(X_t) - f(X_0)$ a local martingale (Itô integral is always local martingale)
    - **⟸ direction**: We only need "martingale locally" to conclude $\mathcal{L}f = 0$ along paths
    
    For **true martingale**, we need the additional integrability condition:
    $$\mathbb{E}\left[\int_0^t (f'(X_s)\sigma(X_s))^2\,ds\right] < \infty$$

---

## Examples

### Example 1: Brownian Motion

**Process**: $dX_t = dW_t$

**Generator**: $\mathcal{L}f = \frac{1}{2}f''$

**Harmonic functions**: $\mathcal{L}f = 0 \Leftrightarrow f'' = 0 \Leftrightarrow f(x) = ax + b$

| Function | $\mathcal{L}f$ | $f(X_t)$ |
|----------|----------------|----------|
| $f(x) = x$ | $0$ | Martingale ✓ |
| $f(x) = x^2$ | $1 \neq 0$ | Not a martingale |
| $f(x) = x^2 - t$ | — | Martingale (but $f$ depends on $t$) |

---

### Example 2: Brownian Motion in $\mathbb{R}^d$

**Generator**: $\mathcal{L} = \frac{1}{2}\Delta$ (half-Laplacian)

**Harmonic functions**: Solutions to $\Delta f = 0$ (classical harmonic functions)

Examples in $\mathbb{R}^2$: $\log|x|$, $\text{Re}(z^n)$, $\text{Im}(z^n)$

Examples in $\mathbb{R}^3$: $1/|x|$, spherical harmonics

---

### Example 3: Ornstein–Uhlenbeck

**Process**: $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$

**Generator**: $\mathcal{L}f = -\kappa x f'(x) + \frac{\sigma^2}{2}f''(x)$

**Harmonic functions**: Solve $-\kappa x f' + \frac{\sigma^2}{2}f'' = 0$

Only bounded solution: $f(x) = \text{constant}$

(The OU process is ergodic — it visits everything — so non-constant harmonic functions would contradict mean-reversion.)

---

### Example 4: GBM

**Process**: $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$

**Generator**: $\mathcal{L}f = \mu s f'(s) + \frac{\sigma^2 s^2}{2}f''(s)$

**Is $f(s) = s$ harmonic?**

$\mathcal{L}f = \mu s \neq 0$ (unless $\mu = 0$)

So $S_t$ is **not** a martingale (it's a submartingale if $\mu > 0$).

**What is harmonic?** Solve $\mu s f' + \frac{\sigma^2 s^2}{2}f'' = 0$:

$$f(s) = s^{1 - 2\mu/\sigma^2}$$

is harmonic (for appropriate $\mu, \sigma$).

---

## Connection to Martingale Problem

The Stroock–Varadhan **martingale problem** uses this characterization:

!!! abstract "Martingale Problem"
    A probability measure $\mathbb{P}$ on path space **solves the martingale problem** for $\mathcal{L}$ if:
    
    $$M_t^f := f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds$$
    
    is a $\mathbb{P}$-martingale for all $f$ in a suitable class (e.g., $C_c^\infty$).

This gives a **probabilistic characterization** of diffusions:

| Approach | Specifies |
|----------|-----------|
| SDE | Pathwise dynamics |
| PDE (Kolmogorov) | Transition densities |
| Martingale Problem | Which processes have generator $\mathcal{L}$ |

The martingale problem is powerful because:

- Works for degenerate diffusions
- Handles weak solutions
- Generalizes to jump processes

See [Stroock–Varadhan Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md).

---

## Summary

| Statement | Meaning |
|-----------|---------|
| $M_t = f(X_t) - f(X_0) - \int_0^t \mathcal{L}f\,ds$ | Dynkin martingale |
| $\mathcal{L}f = 0$ | $f$ is harmonic |
| $\mathcal{L}f = 0 \Rightarrow f(X_t)$ martingale | Harmonic functions give martingales |
| $f(X_t)$ martingale $\Rightarrow \mathcal{L}f = 0$ | Converse (with caveats) |

$$
\boxed{
M_t = \int_0^t f'(X_s)\sigma(X_s)\,dW_s
}
$$

The Dynkin martingale **is** the Itô integral — the noise that remains after subtracting the systematic drift.

---

## See Also

- [Infinitesimal Generator](infinitesimal_generator.md)
- [Dynkin's Formula](dynkin_formula.md)
- [Applications of Dynkin](applications_of_dynkin.md)
- [Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md)
