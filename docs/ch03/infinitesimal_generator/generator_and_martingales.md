# Generator and Martingales

Starting from the
[fundamental decomposition](infinitesimal_generator.md#the-fundamental-decomposition)

$$
f(X_t) = f(X_0) + \int_0^t (\mathcal{L}f)(X_s)\,ds + M_t
$$

this page studies the remaining term $M_t$ — the noise left after the drift is
removed — and the special case $\mathcal{L}f = 0$ of **harmonic functions**.

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

This follows directly from the Itô computation already done when deriving the generator (see [§ Generator of a Diffusion Process](infinitesimal_generator.md#generator-of-a-diffusion-process)): subtracting the drift term from $df(X_t)$ leaves exactly the stochastic-integral remainder

$$
\boxed{
M_t = \int_0^t f'(X_s)\sigma(X_s)\,dW_s
}
$$

an Itô integral, hence a (local) martingale. $\square$

**The Dynkin martingale is the Itô integral** — the unpredictable, zero-mean fluctuations that remain once the drift captured by $\mathcal{L}$ is removed from the master decomposition.

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

Harmonic functions correspond to eliminating the drift term in the fundamental
decomposition entirely: if $\mathcal{L}f = 0$, then $f(X_t) = f(X_0) + M_t$ — pure
noise.

!!! abstract "Definition"
    A function $f$ is **$\mathcal{L}$-harmonic** if:

    $$\mathcal{L}f(x) = 0 \quad \text{for all } x$$

### Harmonic ⇒ Local Martingale

If $\mathcal{L}f = 0$:

$$M_t = f(X_t) - f(X_0) - \int_0^t 0\,ds = f(X_t) - f(X_0)$$

So $f(X_t) - f(X_0)$ is a local martingale, i.e., **$f(X_t)$ is a local martingale**.

$$
\boxed{
\mathcal{L}f = 0 \quad \Longrightarrow \quad f(X_t) \text{ is a local martingale}
}
$$

---

## Converse: Martingale ⇒ Harmonic?

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

### Example 2: Brownian Motion in ℝᵈ

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

Recall (see [§ Stroock–Varadhan Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md)): a measure $\mathbb{P}$ on path space solves the martingale problem for $\mathcal{L}$ if $M_t^f$ above is a $\mathbb{P}$-martingale for all $f \in C_c^\infty$ — turning this page's characterization into a definition of the diffusion.

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

---

## Exercises

**Exercise 1.** For the Ornstein--Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, write down the Dynkin martingale $M_t^f$ for $f(x) = x^2$. Express it explicitly as an Ito integral and verify that $\mathbb{E}[M_t^f] = 0$.

??? success "Solution to Exercise 1"
    The OU generator is $\mathcal{L}f = -\kappa x\,f'(x) + \frac{\sigma^2}{2}f''(x)$. For $f(x) = x^2$:

    - $f'(x) = 2x$, $f''(x) = 2$

    $$
    \mathcal{L}(x^2) = -\kappa x \cdot 2x + \frac{\sigma^2}{2}\cdot 2 = -2\kappa x^2 + \sigma^2
    $$

    The Dynkin martingale is:

    $$
    M_t^f = X_t^2 - X_0^2 - \int_0^t (-2\kappa X_s^2 + \sigma^2)\,ds = X_t^2 - X_0^2 + 2\kappa\int_0^t X_s^2\,ds - \sigma^2 t
    $$

    To express as an Ito integral, apply Ito's lemma to $f(X_t) = X_t^2$:

    $$
    d(X_t^2) = 2X_t\,dX_t + (dX_t)^2 = 2X_t(-\kappa X_t\,dt + \sigma\,dW_t) + \sigma^2\,dt
    $$

    $$
    = (-2\kappa X_t^2 + \sigma^2)\,dt + 2\sigma X_t\,dW_t
    $$

    Rearranging: $d(X_t^2) - (-2\kappa X_t^2 + \sigma^2)\,dt = 2\sigma X_t\,dW_t$. Integrating:

    $$
    M_t^f = \int_0^t 2\sigma X_s\,dW_s
    $$

    This is an Ito integral with respect to $W_t$, hence a local martingale. To verify $\mathbb{E}[M_t^f] = 0$, note that $\mathbb{E}\!\left[\int_0^t 4\sigma^2 X_s^2\,ds\right] < \infty$ for any finite $t$ (since $\mathbb{E}[X_s^2]$ is bounded on $[0,t]$ by the second moment formula), so the Ito integral is a true martingale with $\mathbb{E}[M_t^f] = 0$.

---

**Exercise 2.** Consider geometric Brownian motion $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ on $(0, \infty)$. In Example 4, it was shown that $f(s) = s^{\alpha}$ with $\alpha = 1 - 2\mu/\sigma^2$ is $\mathcal{L}$-harmonic.

(a) Verify directly that $\mathcal{L}(s^{\alpha}) = 0$ for this value of $\alpha$.

(b) What does this imply about the process $S_t^{\alpha}$? Is it a true martingale or only a local martingale? (Hint: consider whether $\mathbb{E}[S_t^{\alpha}]$ remains constant.)

??? success "Solution to Exercise 2"
    **(a)** The GBM generator is $\mathcal{L}f = \mu s\,f'(s) + \frac{\sigma^2 s^2}{2}f''(s)$. For $f(s) = s^\alpha$:

    - $f'(s) = \alpha s^{\alpha - 1}$, $f''(s) = \alpha(\alpha-1)s^{\alpha-2}$

    $$
    \mathcal{L}(s^\alpha) = \mu s \cdot \alpha s^{\alpha-1} + \frac{\sigma^2 s^2}{2}\cdot \alpha(\alpha-1)s^{\alpha-2} = s^\alpha\!\left[\mu\alpha + \frac{\sigma^2}{2}\alpha(\alpha-1)\right]
    $$

    With $\alpha = 1 - 2\mu/\sigma^2$:

    $$
    \mu\alpha + \frac{\sigma^2}{2}\alpha(\alpha - 1) = \mu\!\left(1 - \frac{2\mu}{\sigma^2}\right) + \frac{\sigma^2}{2}\!\left(1 - \frac{2\mu}{\sigma^2}\right)\!\left(-\frac{2\mu}{\sigma^2}\right)
    $$

    $$
    = \mu - \frac{2\mu^2}{\sigma^2} + \frac{\sigma^2}{2}\cdot\left(-\frac{2\mu}{\sigma^2}\right)\!\left(1 - \frac{2\mu}{\sigma^2}\right) = \mu - \frac{2\mu^2}{\sigma^2} - \mu + \frac{2\mu^2}{\sigma^2} = 0
    $$

    So $\mathcal{L}(s^\alpha) = 0$, confirming $f(s) = s^\alpha$ is $\mathcal{L}$-harmonic.

    **(b)** Since $\mathcal{L}(s^\alpha) = 0$, the process $S_t^\alpha$ is a local martingale. To check whether it is a true martingale, compute $\mathbb{E}[S_t^\alpha]$ directly. Since $S_t = s_0 \exp\!\left[(\mu - \sigma^2/2)t + \sigma W_t\right]$:

    $$
    S_t^\alpha = s_0^\alpha \exp\!\left[\alpha(\mu - \sigma^2/2)t + \alpha\sigma W_t\right]
    $$

    $$
    \mathbb{E}[S_t^\alpha] = s_0^\alpha \exp\!\left[\alpha(\mu - \sigma^2/2)t + \frac{\alpha^2\sigma^2}{2}t\right] = s_0^\alpha \exp\!\left[\left(\alpha\mu - \frac{\alpha\sigma^2}{2} + \frac{\alpha^2\sigma^2}{2}\right)t\right]
    $$

    The exponent is $\left[\mu\alpha + \frac{\sigma^2}{2}\alpha(\alpha - 1)\right]t = 0$ by the calculation in part (a). Therefore $\mathbb{E}[S_t^\alpha] = s_0^\alpha$ for all $t$, confirming $S_t^\alpha$ is a **true martingale** (not merely a local martingale).

---

**Exercise 3.** Let $W_t$ be standard Brownian motion and define $f(x, t) = e^{\theta x - \theta^2 t/2}$ for a constant $\theta$. Show that $\tilde{\mathcal{L}}f = 0$ where $\tilde{\mathcal{L}} = \partial_t + \frac{1}{2}\partial_{xx}$ is the extended generator. Conclude that $f(W_t, t)$ is a martingale (the exponential martingale).

??? success "Solution to Exercise 3"
    The extended generator for BM is $\tilde{\mathcal{L}} = \partial_t + \frac{1}{2}\partial_{xx}$. For $f(x,t) = e^{\theta x - \theta^2 t/2}$:

    $$
    \frac{\partial f}{\partial t} = -\frac{\theta^2}{2}e^{\theta x - \theta^2 t/2}
    $$

    $$
    \frac{\partial f}{\partial x} = \theta\, e^{\theta x - \theta^2 t/2}, \qquad \frac{\partial^2 f}{\partial x^2} = \theta^2 e^{\theta x - \theta^2 t/2}
    $$

    Therefore:

    $$
    \tilde{\mathcal{L}}f = -\frac{\theta^2}{2}e^{\theta x - \theta^2 t/2} + \frac{1}{2}\theta^2 e^{\theta x - \theta^2 t/2} = 0
    $$

    Since $\tilde{\mathcal{L}}f = 0$, the process $f(W_t, t) = e^{\theta W_t - \theta^2 t/2}$ satisfies the Dynkin martingale condition: the drift in $df$ vanishes, and $f(W_t, t)$ is a local martingale. It is in fact a true martingale since $\mathbb{E}[e^{\theta W_t - \theta^2 t/2}] = e^{-\theta^2 t/2}\cdot e^{\theta^2 t/2} = 1$ for all $t$. This is the classical **exponential martingale** (also known as the Wald martingale or Doleans-Dade exponential).

---

**Exercise 4.** Let $X_t$ be a continuous martingale with finite variation (i.e., $X_t$ has paths of bounded variation on every $[0, T]$). Prove that $X_t = X_0$ a.s. for all $t$. (Hint: use the fact that the quadratic variation $[X]_t = 0$ for finite-variation processes, and for a continuous local martingale, $[X]_t = 0$ implies $X_t$ is constant.) Explain why this result is crucial for the converse direction: martingale $\Rightarrow$ harmonic.

??? success "Solution to Exercise 4"
    Let $X_t$ be a continuous martingale with paths of bounded variation on every $[0, T]$.

    **Step 1**: For a continuous finite-variation process, the quadratic variation is zero: $[X]_t = 0$ for all $t$. This follows because $[X]_t = \lim_{n\to\infty}\sum_{k}(X_{t_{k+1}} - X_{t_k})^2$, and for a bounded-variation process, $\max_k |X_{t_{k+1}} - X_{t_k}| \to 0$, so:

    $$
    \sum_k (X_{t_{k+1}} - X_{t_k})^2 \leq \max_k |X_{t_{k+1}} - X_{t_k}| \cdot \sum_k |X_{t_{k+1}} - X_{t_k}| \to 0 \cdot \mathrm{TV}(X) = 0
    $$

    **Step 2**: By the martingale representation structure, any continuous local martingale $M_t$ satisfies $M_t = M_0 + \int_0^t H_s\,dW_s$ for some predictable process $H_s$ (by the Brownian martingale representation theorem in the Brownian filtration, or more generally by the Kunita-Watanabe characterization). Its quadratic variation is $[M]_t = \int_0^t H_s^2\,ds$. If $[M]_t = 0$, then $H_s = 0$ a.e., so $M_t = M_0$.

    Alternatively, without invoking representation: $X_t - X_0$ is a continuous local martingale with $[X - X_0]_t = [X]_t = 0$. By the identity $\mathbb{E}[(X_t - X_s)^2 \mid \mathcal{F}_s] = \mathbb{E}[[X]_t - [X]_s \mid \mathcal{F}_s] = 0$, we get $X_t = X_s$ a.s. for all $s \leq t$, hence $X_t = X_0$ a.s.

    **Why this matters for the converse**: If $f(X_t)$ is a martingale, then $M_t = f(X_t) - f(X_0)$ is a martingale and also $M_t = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds + \int_0^t (\mathcal{L}f)(X_s)\,ds$. The process $A_t = \int_0^t (\mathcal{L}f)(X_s)\,ds$ is continuous and of finite variation, and $M_t - A_t$ is a martingale by the Dynkin construction. So $A_t = M_t - (M_t - A_t)$ is a difference of two martingales, hence a martingale. Being both a continuous finite-variation process and a martingale, $A_t$ must be constant: $A_t = A_0 = 0$. This forces $\int_0^t (\mathcal{L}f)(X_s)\,ds = 0$ for all $t$, implying $\mathcal{L}f = 0$ along the paths of $X$.

---

**Exercise 5.** For standard Brownian motion in $\mathbb{R}^2$ with generator $\mathcal{L} = \frac{1}{2}\Delta = \frac{1}{2}(\partial_{xx} + \partial_{yy})$, verify that the following functions are $\mathcal{L}$-harmonic:

(a) $f(x, y) = x^2 - y^2$

(b) $f(x, y) = e^x \cos(y)$

(c) $f(x, y) = \ln(x^2 + y^2)$ for $(x, y) \neq (0, 0)$

For each, state what the harmonic property implies about $f(W_t^1, W_t^2)$ where $(W_t^1, W_t^2)$ is 2D Brownian motion.

??? success "Solution to Exercise 5"
    **(a)** $f(x,y) = x^2 - y^2$:

    $$
    \partial_{xx}f = 2, \qquad \partial_{yy}f = -2
    $$

    $$
    \Delta f = 2 + (-2) = 0 \implies \mathcal{L}f = \frac{1}{2}\cdot 0 = 0 \checkmark
    $$

    So $f(W_t^1, W_t^2) = (W_t^1)^2 - (W_t^2)^2$ is a local martingale.

    **(b)** $f(x,y) = e^x \cos(y)$:

    $$
    \partial_{xx}f = e^x\cos(y), \qquad \partial_{yy}f = -e^x\cos(y)
    $$

    $$
    \Delta f = e^x\cos(y) - e^x\cos(y) = 0 \implies \mathcal{L}f = 0 \checkmark
    $$

    So $f(W_t^1, W_t^2) = e^{W_t^1}\cos(W_t^2)$ is a local martingale. (This is the real part of $e^{W_t^1 + iW_t^2}$, connected to conformal invariance of 2D BM.)

    **(c)** $f(x,y) = \ln(x^2 + y^2)$ for $(x,y) \neq (0,0)$:

    $$
    \partial_x f = \frac{2x}{x^2+y^2}, \qquad \partial_{xx}f = \frac{2(x^2+y^2) - 2x\cdot 2x}{(x^2+y^2)^2} = \frac{2(y^2 - x^2)}{(x^2+y^2)^2}
    $$

    By symmetry:

    $$
    \partial_{yy}f = \frac{2(x^2 - y^2)}{(x^2+y^2)^2}
    $$

    $$
    \Delta f = \frac{2(y^2 - x^2) + 2(x^2 - y^2)}{(x^2+y^2)^2} = 0 \implies \mathcal{L}f = 0 \checkmark
    $$

    So $\ln((W_t^1)^2 + (W_t^2)^2) = \ln|B_t|^2 = 2\ln|B_t|$ (where $B_t$ is 2D BM) is a local martingale, provided $B_t \neq 0$. Since 2D BM is neighborhood-recurrent but point-recurrent only at the starting point, $\ln|B_t|$ is well-defined for $B_0 \neq 0$. This is the classical result that $\ln|B_t|$ is a local martingale for 2D BM.

---

**Exercise 6.** Consider a diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ where $\sigma(x) = 0$ for $x \in [1, 2]$ but $\sigma(x) > 0$ elsewhere. Explain why the equivalence $\mathcal{L}f = 0 \Leftrightarrow f(X_t)$ is a local martingale may fail in this setting. Which specific condition (non-degeneracy or irreducibility) is violated, and what is the consequence for the converse direction?

??? success "Solution to Exercise 6"
    The condition violated is **non-degeneracy**. Since $\sigma(x) = 0$ for $x \in [1,2]$, the diffusion coefficient vanishes on an entire interval. Within $[1,2]$, the process follows the ODE $dX_t = \mu(X_t)\,dt$ with no randomness — it moves deterministically and cannot explore the region $[1,2]$ freely.

    The consequence for the converse direction: suppose $f(X_t)$ is a martingale. The argument that $\mathcal{L}f = 0$ relies on the process visiting all points in the state space. If $X_t$ starts outside $[1,2]$ and enters this interval, it moves deterministically through it, never "sampling" all points densely. So even if $f(X_t)$ is a martingale, we can only conclude $\mathcal{L}f(x) = 0$ for points $x$ actually visited by the process.

    Concretely, on $[1,2]$ the generator reduces to $\mathcal{L}f(x) = \mu(x)f'(x)$ (purely first-order). A function $f$ could satisfy $\mu(x)f'(x) \neq 0$ at some $x \in [1,2]$ that the process traverses only once (deterministically), yet $f(X_t)$ might still be a martingale globally because the non-zero generator contribution on $[1,2]$ is compensated by the behavior elsewhere. The equivalence $\mathcal{L}f = 0 \Leftrightarrow f(X_t)$ local martingale breaks down because the degenerate region prevents the process from being irreducible in the sense needed for the converse.

---

**Exercise 7.** In the Stroock--Varadhan martingale problem, one requires $M_t^f = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds$ to be a martingale for all $f \in C_c^\infty$.

(a) Why is it sufficient to test only functions in $C_c^\infty$ (smooth with compact support) rather than all $C^2$ functions?

(b) Give an intuitive explanation for why the martingale problem characterization uniquely determines the law of $X_t$ under non-degeneracy conditions.

??? success "Solution to Exercise 7"
    **(a)** The space $C_c^\infty$ is sufficient because it is **dense** in the relevant function spaces (such as $C_0^2$ or $L^2$) and the generator is a local operator for diffusions. More precisely:

    - The martingale property $\mathbb{E}[M_t^f \mid \mathcal{F}_s] = M_s^f$ for all $f \in C_c^\infty$ determines all finite-dimensional distributions of $X_t$. This is because the test functions $f \in C_c^\infty$ separate points: for any two distinct probability measures on path space, there exists $f \in C_c^\infty$ for which the martingale condition distinguishes them.
    - Technically, $C_c^\infty$ is a core for the generator of any non-degenerate diffusion, meaning the closure of $\mathcal{L}|_{C_c^\infty}$ equals the full generator. Testing the martingale property on a core suffices to determine the process.

    **(b)** Intuitively, the generator $\mathcal{L}$ encodes both the drift $\mu(x)$ and the diffusion coefficient $a(x) = \sigma\sigma^\top(x)$ at every point $x$. The martingale condition $\mathbb{E}[M_t^f \mid \mathcal{F}_s] = M_s^f$ for all smooth $f$ forces the conditional mean and conditional variance of infinitesimal increments to match $\mu$ and $a$ respectively. Under non-degeneracy ($a(x)$ is positive definite), the second-order terms in $\mathcal{L}$ uniquely determine the diffusion matrix, and the first-order terms uniquely determine the drift. Since the law of a Markov process is determined by its infinitesimal transition rates (equivalently, by $\mu$ and $a$), uniqueness follows. This is the Stroock-Varadhan uniqueness theorem: non-degenerate $a(x)$ with suitable regularity guarantees that the martingale problem has a unique solution.

---

**Exercise 8.**
Let $X_t$ solve $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ and let $f \in C^2$. Show that if $\mathcal{L}f = 0$, where $\mathcal{L} = \mu(x)\partial_x + \frac{1}{2}\sigma^2(x)\partial_{xx}$ is the infinitesimal generator, then $f(X_t)$ is a local martingale.

??? success "Solution to Exercise 8"
    Apply Itô's formula to $f(X_t)$:

    $$
    df(X_t) = f'(X_t)\,dX_t + \frac{1}{2}f''(X_t)\,(dX_t)^2
    $$

    Since $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ and $(dX_t)^2 = \sigma^2(X_t)\,dt$:

    $$
    df(X_t)
    = \left[\mu(X_t)f'(X_t) + \frac{1}{2}\sigma^2(X_t)f''(X_t)\right]dt + f'(X_t)\sigma(X_t)\,dW_t
    $$

    That is,

    $$
    df(X_t) = \mathcal{L}f(X_t)\,dt + f'(X_t)\sigma(X_t)\,dW_t.
    $$

    If $\mathcal{L}f = 0$, the drift term vanishes, leaving

    $$
    f(X_t) = f(X_0) + \int_0^t f'(X_s)\sigma(X_s)\,dW_s,
    $$

    which is an Itô integral plus a constant. Hence $f(X_t)$ is a local martingale.

    **Interpretation.** The condition $\mathcal{L}f = 0$ means $f$ is harmonic for the diffusion. Harmonic functions kill the drift, leaving only noise — and pure noise gives a local martingale.

---

**Exercise 9.**
For the 3D Bessel process reciprocal $M_t = 1/R_t$ starting from $R_0 = r_0 > 0$, verify the Itô computation: apply Itô's formula to $f(r) = 1/r$ and the SDE $dR_t = (1/R_t)\,dt + dW_t$ to obtain $dM_t = -M_t^2\,dW_t$. Explain why the absence of a $dt$ term confirms $M_t$ is a local martingale, and why the drift terms from $f'$ and $f''$ cancel exactly.

??? success "Solution to Exercise 9"
    Let $f(r) = 1/r$, so $f'(r) = -1/r^2$ and $f''(r) = 2/r^3$. By Itô's formula applied to $M_t = f(R_t)$:

    $$
    dM_t = f'(R_t)\,dR_t + \frac{1}{2}f''(R_t)\,(dR_t)^2
    $$

    With $dR_t = \frac{1}{R_t}\,dt + dW_t$, we have $(dR_t)^2 = dt$ (since $(dW_t)^2 = dt$ and all other terms vanish). Substituting:

    $$
    dM_t = -\frac{1}{R_t^2}\left(\frac{1}{R_t}\,dt + dW_t\right) + \frac{1}{2}\cdot\frac{2}{R_t^3}\,dt
    $$

    $$
    = -\frac{1}{R_t^3}\,dt - \frac{1}{R_t^2}\,dW_t + \frac{1}{R_t^3}\,dt
    $$

    $$
    = -\frac{1}{R_t^2}\,dW_t = -M_t^2\,dW_t
    $$

    The drift terms cancel exactly: $f'(R_t) \cdot \mu(R_t) + \frac{1}{2}f''(R_t) \cdot 1 = -R_t^{-3} + R_t^{-3} = 0$. This happens because $f(r) = 1/r$ is a **harmonic function** for the 3D Bessel generator $\mathcal{L} = \frac{1}{r}\frac{\partial}{\partial r} + \frac{1}{2}\frac{\partial^2}{\partial r^2}$, i.e., $\mathcal{L}f = 0$.

    The absence of a $dt$ term means $M_t$ is a pure stochastic integral $M_t = M_0 + \int_0^t (-M_s^2)\,dW_s$, which is by definition a local martingale. The drift cancellation is not coincidental — it reflects the deep connection between harmonic functions and martingales via the generator criterion.
