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

    Under the integrability condition $\mathbb{E}\left[\int_0^t (f'(X_s)\sigma(X_s))^2\,ds\right] < \infty$, it is a **true martingale**.

---

## Why It's a Martingale

From Itô's lemma:

$$f(X_t) = f(X_0) + \int_0^t (\mathcal{L}f)(X_s)\,ds + \int_0^t f'(X_s)\sigma(X_s)\,dW_s$$

Rearranging:

$$M_t = \int_0^t f'(X_s)\sigma(X_s)\,dW_s$$

The Itô integral is a (local) martingale, so $M_t$ is a (local) martingale. $\square$

!!! info "Interpretation"

    $$f(X_t) = \underbrace{f(X_0) + \int_0^t (\mathcal{L}f)(X_s)\,ds}_{\text{predictable drift}} + \underbrace{M_t}_{\text{martingale}}$$

    - **Drift**: systematic, predictable change (captured by $\mathcal{L}$)
    - **Martingale**: unpredictable fluctuations (zero-mean increments)

The Dynkin martingale **is** the Itô integral — the noise that remains after subtracting the systematic drift.

$$
\boxed{
M_t = \int_0^t f'(X_s)\sigma(X_s)\,dW_s
}
$$

---

## Local vs True Martingale

| Condition | $M_t$ is... |
|-----------|-------------|
| $f \in C^2$ | Local martingale |
| + $\mathbb{E}\left[\int_0^t (f'\sigma)^2\,ds\right] < \infty$ | True martingale |
| + bounded $f'\sigma$ and finite horizon $T$ | Uniformly integrable martingale |

**True martingale** means $\mathbb{E}[|M_t|] < \infty$, $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$, and in particular $\mathbb{E}[M_t] = 0$.

**Local martingale** means only that there exist $\tau_n \uparrow \infty$ such that $M_{t \wedge \tau_n}$ is a true martingale. This does not guarantee $\mathbb{E}[M_t] = 0$.

!!! example "Classic Counterexample: Strict Local Martingale"
    Let $W_t$ be 3D Brownian motion with $|W_0| = 1$. Define $X_t = 1/|W_t|$.

    - $X_t$ is a **local martingale** (by Itô's lemma)
    - $X_t$ is **not** a true martingale: $\mathbb{E}[X_t] < X_0$ — the expectation decreases.
    - Optional stopping fails: $\mathbb{E}[X_\tau] \neq X_0$ for some stopping times.

### Optional Stopping and Dynkin's Formula

Dynkin's formula uses $\mathbb{E}[M_\tau] = 0$, which requires optional stopping to hold:

| $M_t$ is... | Dynkin's formula |
|-------------|------------------|
| True martingale + optional stopping conditions | ✓ Works directly |
| Local martingale only | ⚠ May fail without extra work |

**Localization fix**: If $M_t$ is only a local martingale with localizing sequence $\tau_n \uparrow \infty$, apply Dynkin to $\tau \wedge \tau_n$ (which works since $M_{t \wedge \tau_n}$ is a true martingale), then take $n \to \infty$ using dominated or monotone convergence.

---

## Harmonic Functions

!!! abstract "Definition"
    A function $f$ is **$\mathcal{L}$-harmonic** if:

    $$\mathcal{L}f(x) = 0 \quad \text{for all } x$$

### Harmonic $\Rightarrow$ Local Martingale

If $\mathcal{L}f = 0$:

$$M_t = f(X_t) - f(X_0) - \int_0^t 0\,ds = f(X_t) - f(X_0)$$

So $f(X_t) - f(X_0)$ is a local martingale, i.e., **$f(X_t)$ is a local martingale**.

$$
\boxed{
\mathcal{L}f = 0 \quad \Longrightarrow \quad f(X_t) \text{ is a local martingale}
}
$$

---

## Converse: Martingale $\Rightarrow$ Harmonic?

If $f(X_t)$ is a martingale, then $M_t = f(X_t) - f(X_0)$ is a martingale, and also $M_t = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds$ is a martingale. So $\int_0^t (\mathcal{L}f)(X_s)\,ds$ must be a martingale. But it is also a continuous finite-variation process.

**Key fact**: A continuous martingale of finite variation is constant. (Proof: by the Doob–Meyer decomposition, such a process has zero quadratic variation, hence is a.s. constant.)

Therefore $\int_0^t (\mathcal{L}f)(X_s)\,ds = 0$ for all $t$, a.s., which implies $(\mathcal{L}f)(X_s) = 0$ for a.e.\ $s$ along sample paths.

### The Subtlety

This says $\mathcal{L}f(x) = 0$ **for $x$ visited by the process** — not automatically for all $x$.

| Condition | Conclusion |
|-----------|------------|
| $f(X_t)$ martingale | $(\mathcal{L}f)(X_t) = 0$ a.e.\ along paths |
| + $X_t$ irreducible | $\mathcal{L}f(x) = 0$ for all $x$ in state space |
| + $f \in C^2$, $\mathcal{L}f$ continuous | $\mathcal{L}f(x) = 0$ everywhere |

If $X_t$ never visits some region $A$, we learn nothing about $\mathcal{L}f$ on $A$ from the martingale property alone.

---

## Correct Characterization

Under suitable regularity ($f \in C^2$, diffusion **non-degenerate** and **irreducible**):

$$
\boxed{
\mathcal{L}f(x) = 0 \;\forall x \quad \Longleftrightarrow \quad f(X_t) \text{ is a local martingale (under non-degeneracy and irreducibility)}
}
$$

The $\Leftarrow$ direction requires non-degeneracy so the process visits all of the state space. Without it, we can only conclude $\mathcal{L}f = 0$ along visited paths. For the equivalence with **true martingale**, the additional condition $\mathbb{E}\left[\int_0^t (f'\sigma)^2\,ds\right] < \infty$ is needed.

---

## Examples

### Example 1: Brownian Motion

**Generator**: $\mathcal{L}f = \frac{1}{2}f''$

**Harmonic functions**: $\mathcal{L}f = 0 \Leftrightarrow f'' = 0 \Leftrightarrow f(x) = ax + b$

| Function | $\mathcal{L}f$ | $f(X_t)$ |
|----------|----------------|----------|
| $f(x) = x$ | $0$ | Martingale ✓ |
| $f(x) = x^2$ | $1 \neq 0$ | Not a martingale |
| $f(x,t) = x^2 - t$ | $\tilde{\mathcal{L}}f = 0$ | Martingale (time-dependent; uses extended generator $\tilde{\mathcal{L}} = \partial_t + \mathcal{L}$) |

---

### Example 2: Brownian Motion in $\mathbb{R}^d$

**Generator**: $\mathcal{L} = \frac{1}{2}\Delta$

**Harmonic functions**: Solutions to $\Delta f = 0$ (classical harmonic functions).

Examples in $\mathbb{R}^2$: $\log|x|$, $\text{Re}(z^n)$, $\text{Im}(z^n)$ (all away from the origin where $f \notin C^2$).
Examples in $\mathbb{R}^3$: $1/|x|$ (away from origin), spherical harmonics.

---

### Example 3: Ornstein–Uhlenbeck

**Generator**: $\mathcal{L}f = -\kappa x f'(x) + \frac{\sigma^2}{2}f''(x)$

**Harmonic functions**: Solve $-\kappa x f' + \frac{\sigma^2}{2}f'' = 0$. The general solution involves parabolic cylinder functions; among bounded solutions, only $f(x) = \text{constant}$ qualifies. This is consistent with the OU process being ergodic — a non-constant bounded harmonic function would contradict mean-reversion to the stationary distribution.

---

### Example 4: GBM

**Generator**: $\mathcal{L}f = \mu s f'(s) + \frac{\sigma^2 s^2}{2}f''(s)$

**Is $f(s) = s$ harmonic?** $\mathcal{L}(s) = \mu s \neq 0$ (unless $\mu = 0$). So $S_t$ is **not** a martingale (it is a submartingale if $\mu > 0$).

**Harmonic functions**: We solve $\mu s f' + \frac{\sigma^2 s^2}{2}f'' = 0$ on $(0,\infty)$. Testing $f(s) = s^\alpha$:

$$\mathcal{L}(s^\alpha) = \mu \alpha s^\alpha + \frac{\sigma^2}{2}\alpha(\alpha - 1)s^\alpha = s^\alpha\left[\mu\alpha + \frac{\sigma^2}{2}\alpha(\alpha-1)\right]$$

Setting this to zero for $\alpha \neq 0$ (the case $\alpha = 0$ gives the trivial constant solution $f = 1$):

$$\mu + \frac{\sigma^2}{2}(\alpha - 1) = 0 \implies \alpha = 1 - \frac{2\mu}{\sigma^2}$$

$$\boxed{f(s) = s^{1 - 2\mu/\sigma^2} \text{ is } \mathcal{L}\text{-harmonic on } (0,\infty), \text{ provided } \mu \neq \frac{\sigma^2}{2}}$$

When $\mu = \sigma^2/2$, the nontrivial exponent degenerates to zero and only constant solutions exist.

---

## Connection to Martingale Problem

The Stroock–Varadhan **martingale problem** uses this characterization as its foundation:

!!! abstract "Martingale Problem (Stroock–Varadhan)"
    A probability measure $\mathbb{P}$ on path space **solves the martingale problem** for $\mathcal{L}$ if:

    $$M_t^f := f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds$$

    is a $\mathbb{P}$-martingale for all $f \in C_c^\infty$.

This gives a probabilistic characterization of diffusions without requiring pathwise SDE solutions. See [Stroock–Varadhan Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md) for the full development, including uniqueness theory and applications to degenerate diffusions.

---

## Summary

| Statement | Meaning |
|-----------|---------|
| $M_t = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds$ | Dynkin martingale = Itô integral |
| $\mathcal{L}f = 0$ | $f$ is $\mathcal{L}$-harmonic |
| $\mathcal{L}f = 0 \Rightarrow f(X_t)$ local martingale | Harmonic functions give local martingales |
| $f(X_t)$ martingale $\Rightarrow \mathcal{L}f = 0$ | Converse holds under non-degeneracy and irreducibility |

---

## See Also

- [Infinitesimal Generator](infinitesimal_generator.md)
- [Dynkin's Formula](dynkin_formula.md)
- [Applications of Dynkin](applications_of_dynkin.md)
- [Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md)
