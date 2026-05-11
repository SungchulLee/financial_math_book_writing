# Invariant Measures and Stationarity

## Concept Definition

Let $(X_t)_{t \ge 0}$ be a time-homogeneous Markov process on $\mathbb{R}^d$ with transition semigroup $(P_t)_{t \ge 0}$ defined by

$$
P_t f(x) := \mathbb{E}^x[f(X_t)], \qquad f \text{ bounded measurable}
$$

The semigroup acts on measures from the right: for a probability measure $\mu$,

$$
(\mu P_t)(A) := \int_{\mathbb{R}^d} P_t \mathbf{1}_A(x)\,\mu(\mathrm{d}x) = \mathbb{P}^{\mu}(X_t \in A)
$$

!!! info "Definition: Invariant Measure"
    A probability measure $\pi$ on $\mathbb{R}^d$ is **invariant** for $(P_t)$ if

    $$
    \pi P_t = \pi \qquad \text{for all } t \ge 0
    $$

    equivalently, for all bounded measurable $f$ and all $t \ge 0$:

    $$
    \int_{\mathbb{R}^d} P_t f(x)\,\pi(\mathrm{d}x) = \int_{\mathbb{R}^d} f(x)\,\pi(\mathrm{d}x)
    $$

    In other words: if $X_0 \sim \pi$ then $X_t \sim \pi$ for all $t \ge 0$.

!!! info "Definition: Stationarity"
    A process $(X_t)$ is **stationary** if its finite-dimensional distributions are invariant under time shifts: for all $h \ge 0$ and all $0 \le t_1 < \cdots < t_k$,

    $$
    (X_{t_1 + h}, \dots, X_{t_k + h}) \stackrel{d}{=} (X_{t_1}, \dots, X_{t_k})
    $$

    Starting a Markov process from an invariant measure $\pi$ yields a stationary process.

---

## Why Invariant Measures Matter

An invariant measure describes the **equilibrium distribution** of a stochastic system: the state toward which the process settles in the long run. If $X_t$ converges in law as $t \to \infty$, the limit must be an invariant measure. This connects to ergodicity (time averages equal space averages), stability of stochastic systems, and — in finance — the stationary distribution of mean-reverting processes (e.g., interest rates, volatility).

---

## Explanation

### Generator Characterisation

Using the [generator](diffusion_process_overview.md#infinitesimal-generator) $\mathcal{L}$ defined earlier, $\pi$ is invariant if and only if

$$
\int_{\mathbb{R}^d} (\mathcal{L}f)(x)\,\pi(\mathrm{d}x) = 0
\qquad \text{for all } f \in \mathrm{Dom}(\mathcal{L})
$$

Equivalently, $\mathcal{L}^* \pi = 0$ in the distributional sense. The proof of this equivalence is given [below](#proof--derivation).

### Stationary Fokker–Planck Equation

When $\pi$ has a density, $\mathcal{L}^*\pi = 0$ reduces to the **stationary Fokker–Planck equation** — an elliptic PDE for $\pi$ in terms of the drift $b$ and diffusion matrix $a = \sigma\sigma^\top$. This is the main computational tool for finding invariant densities (see exercises).

### Existence and Uniqueness

An invariant measure need not exist. Existence can be established via **Lyapunov / Foster criteria** (a drift condition ensuring tightness of time-averages) or, for gradient diffusions, by verifying $\int e^{-V}\,\mathrm{d}x < \infty$. Uniqueness follows from irreducibility and non-degeneracy of the diffusion matrix.

### Reversibility

A stronger property than invariance is **reversibility** (detailed balance): $\mathcal{L}$ is self-adjoint in $L^2(\pi)$. This implies the process is time-symmetric under $\pi$. Gradient diffusions are always reversible; adding a non-gradient drift component breaks detailed balance. Reversibility is exactly the condition under which the [time-reversal formula](time_reversal_of_diffusions.md) simplifies: the reversed process has the same generator as the forward process.

---

## Diagram / Example

### Example: Gradient Diffusion (Langevin Equation)

Consider

$$
\mathrm{d}X_t = -\nabla V(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t
$$

where $V : \mathbb{R}^d \to \mathbb{R}$ is smooth and $Z := \int_{\mathbb{R}^d} e^{-V(x)}\,\mathrm{d}x < \infty$.

**Claim.** $\pi(x) = Z^{-1} e^{-V(x)}$ is an invariant density.

**Verification.** Substituting $\pi = Z^{-1}e^{-V}$ into the stationary Fokker–Planck equation $\mathcal{L}^*\pi = 0$ (with $b = -\nabla V$, $a = 2I$), the terms $\nabla\cdot(\nabla V\,\pi)$ and $\Delta\pi$ cancel exactly. $\square$

**Reversibility.** This process is reversible with respect to $\pi$; the gradient structure ensures detailed balance.

### Summary Table

| Property | Condition | Implication |
|---|---|---|
| Invariance | $\pi P_t = \pi$ | Law preserved in time |
| Stationarity | Start from $\pi$ | Shift-invariant distributions |
| Generator condition | $\int \mathcal{L}f\,\mathrm{d}\pi = 0$ | Characterises invariant $\pi$ |
| Reversibility | $\mathcal{L}$ self-adjoint in $L^2(\pi)$ | Time-symmetric dynamics |

---

## Proof / Derivation

We verify the generator condition $\int \mathcal{L}f\,\mathrm{d}\pi = 0$ is equivalent to invariance under mild assumptions.

**Forward direction.** If $\pi P_t = \pi$, then $\int P_t f\,\mathrm{d}\pi = \int f\,\mathrm{d}\pi$ for all $t \ge 0$. The left side is differentiable in $t$; differentiating at $t = 0$ and using the definition of the generator gives $\int \mathcal{L}f\,\mathrm{d}\pi = 0$.

**Backward direction.** Suppose $\int \mathcal{L}f\,\mathrm{d}\pi = 0$ for all $f \in \mathrm{Dom}(\mathcal{L})$. Set $h(t) := \int P_t f\,\mathrm{d}\pi$. Then

$$
h'(t) = \int \mathcal{L}(P_t f)\,\mathrm{d}\pi = 0
$$

where the first equality uses $\frac{\mathrm{d}}{\mathrm{d}t}P_t f = \mathcal{L} P_t f$ (the Kolmogorov forward equation for the semigroup), and the second applies the hypothesis with test function $P_t f \in \mathrm{Dom}(\mathcal{L})$. Hence $h(t) = h(0) = \int f\,\mathrm{d}\pi$ for all $t \ge 0$, confirming $\pi P_t = \pi$. $\square$

---

## What to Remember

- An invariant measure $\pi$ satisfies $\pi P_t = \pi$: the law is preserved under the dynamics.
- Starting from $\pi$ produces a **stationary process**.
- Stationary densities solve the **Fokker–Planck equation** $\mathcal{L}^*\pi = 0$.
- Existence follows from Lyapunov criteria; uniqueness from irreducibility and non-degeneracy.
- **Reversibility** (detailed balance) is stronger than invariance and implies time-symmetry of the process.

---

## Exercises

**Exercise 1.** Consider the one-dimensional Ornstein–Uhlenbeck process $\mathrm{d}X_t = -\theta X_t\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$ with $\theta > 0$. Using the stationary Fokker–Planck equation $\mathcal{L}^*\pi = 0$, show that the invariant density is Gaussian with mean $0$ and variance $\sigma^2/(2\theta)$.

??? success "Solution to Exercise 1"
    The OU process has $b(x) = -\theta x$ and $\sigma(x) = \sigma$ (constant), so $a(x) = \sigma^2$. The generator is

    $$
    \mathcal{L}f(x) = -\theta x\,f'(x) + \frac{\sigma^2}{2}\,f''(x)
    $$

    The stationary Fokker–Planck equation $\mathcal{L}^*\pi = 0$ in one dimension is

    $$
    -\frac{\mathrm{d}}{\mathrm{d}x}\bigl(b(x)\,\pi(x)\bigr) + \frac{1}{2}\frac{\mathrm{d}^2}{\mathrm{d}x^2}\bigl(\sigma^2\,\pi(x)\bigr) = 0
    $$

    Since $\sigma^2$ is constant, this becomes

    $$
    \frac{\mathrm{d}}{\mathrm{d}x}\bigl(\theta x\,\pi(x)\bigr) + \frac{\sigma^2}{2}\,\pi''(x) = 0
    $$

    Integrating once (the integration constant must be zero for $\pi$ to be integrable):

    $$
    \theta x\,\pi(x) + \frac{\sigma^2}{2}\,\pi'(x) = 0
    $$

    This gives

    $$
    \frac{\pi'(x)}{\pi(x)} = -\frac{2\theta x}{\sigma^2}
    $$

    Integrating:

    $$
    \log\pi(x) = -\frac{\theta x^2}{\sigma^2} + C_0
    $$

    so $\pi(x) \propto \exp(-\theta x^2/\sigma^2)$. Normalizing:

    $$
    \pi(x) = \sqrt{\frac{\theta}{\pi\sigma^2}}\,\exp\!\left(-\frac{\theta x^2}{\sigma^2}\right)
    $$

    This is a Gaussian density $\mathcal{N}(0, \sigma^2/(2\theta))$ with mean $0$ and variance $\sigma^2/(2\theta)$.

---

**Exercise 2.** Let $V(x) = \frac{1}{4}x^4 - \frac{1}{2}x^2$ (a double-well potential) on $\mathbb{R}$. Consider the gradient diffusion $\mathrm{d}X_t = -V'(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t$. Write down the invariant density $\pi(x)$ (up to a normalising constant). Sketch $\pi(x)$ and identify the locations of its maxima. Is this process reversible?

??? success "Solution to Exercise 2"
    With $V(x) = \frac{1}{4}x^4 - \frac{1}{2}x^2$ and the gradient diffusion $\mathrm{d}X_t = -V'(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t$, the invariant density is

    $$
    \pi(x) \propto e^{-V(x)} = \exp\!\left(-\frac{1}{4}x^4 + \frac{1}{2}x^2\right)
    $$

    The maxima of $\pi$ occur where $V(x)$ is minimized. Setting $V'(x) = x^3 - x = x(x^2 - 1) = 0$ gives critical points $x = 0, \pm 1$. We have $V''(x) = 3x^2 - 1$, so $V''(0) = -1 < 0$ (local maximum of $V$, hence local minimum of $\pi$) and $V''(\pm 1) = 2 > 0$ (local minima of $V$, hence local maxima of $\pi$).

    Therefore $\pi(x)$ has **two maxima at $x = \pm 1$** and a local minimum at $x = 0$. The density is bimodal, reflecting the double-well structure of $V$.

    **Reversibility:** Yes, this process is reversible. It is a gradient diffusion with constant diffusion matrix ($a = 2I$), which automatically satisfies detailed balance with respect to $\pi(x) \propto e^{-V(x)}$. The generator

    $$
    \mathcal{L}f = -V'(x)f'(x) + f''(x)
    $$

    is self-adjoint in $L^2(\pi)$: for $f, g \in C_c^\infty(\mathbb{R})$,

    $$
    \int (\mathcal{L}f)\,g\,\pi\,\mathrm{d}x = -\int f'\,g'\,\pi\,\mathrm{d}x = \int f\,(\mathcal{L}g)\,\pi\,\mathrm{d}x
    $$

    which follows by integration by parts.

---

**Exercise 3.** Consider the two-dimensional diffusion

$$
\mathrm{d}X_t^1 = -X_t^1\,\mathrm{d}t + X_t^2\,\mathrm{d}t + \mathrm{d}W_t^1, \qquad \mathrm{d}X_t^2 = -X_t^1\,\mathrm{d}t - X_t^2\,\mathrm{d}t + \mathrm{d}W_t^2
$$

Find the invariant measure (hint: try a Gaussian ansatz). Is this process reversible? Justify your answer by checking whether $\mathcal{L}$ is self-adjoint in $L^2(\pi)$.

??? success "Solution to Exercise 3"
    The drift is $b(x) = (-x^1 + x^2,\, -x^1 - x^2)^\top$ and $a = I_2$. Try a Gaussian invariant measure $\pi \sim \mathcal{N}(0, \Sigma)$ with $\Sigma = \text{diag}(\sigma_1^2, \sigma_2^2)$ or more generally a symmetric positive definite matrix.

    The drift can be written $b(x) = Bx$ where

    $$
    B = \begin{pmatrix} -1 & 1 \\ -1 & -1 \end{pmatrix}
    $$

    For a linear SDE $\mathrm{d}X = BX\,\mathrm{d}t + \mathrm{d}W$ with constant $a = I$, the invariant covariance $\Sigma$ solves the **Lyapunov equation**

    $$
    B\Sigma + \Sigma B^\top + I = 0
    $$

    Writing $\Sigma = \begin{pmatrix} a & c \\ c & b \end{pmatrix}$ and $B^\top = \begin{pmatrix} -1 & -1 \\ 1 & -1 \end{pmatrix}$:

    $$
    B\Sigma + \Sigma B^\top = \begin{pmatrix} -2a+2c & -2c+a+b \\ a+b-2c & 2c-2b \end{pmatrix} + \text{correction}
    $$

    Computing directly:

    $$
    B\Sigma = \begin{pmatrix} -a+c & -c+b \\ -a-c & -c-b \end{pmatrix}, \quad \Sigma B^\top = \begin{pmatrix} -a-c & a-c \\ -c-b & c-b \end{pmatrix}
    $$

    $$
    B\Sigma + \Sigma B^\top = \begin{pmatrix} -2a & a-2c+b \\ a-2c+b & -2b \end{pmatrix} = -I = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}
    $$

    From the diagonal entries: $-2a = -1$ gives $a = 1/2$, $-2b = -1$ gives $b = 1/2$. From the off-diagonal: $a - 2c + b = 0$ gives $c = (a+b)/2 = 1/2$.

    Wait — checking: $c = 1/2$ but then $\Sigma = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$ which is singular. Let me recompute.

    Actually, recomputing $\Sigma B^\top$ with $B^\top = \begin{pmatrix}-1&-1\\1&-1\end{pmatrix}$:

    $$
    \Sigma B^\top = \begin{pmatrix}a&c\\c&b\end{pmatrix}\begin{pmatrix}-1&-1\\1&-1\end{pmatrix} = \begin{pmatrix}-a+c & -a-c \\ -c+b & -c-b\end{pmatrix}
    $$

    $$
    B\Sigma + \Sigma B^\top = \begin{pmatrix}-2a+2c & -a-2c+b \\ a+b-2c & 2c-2b\end{pmatrix} + \begin{pmatrix}0&0\\0&0\end{pmatrix}
    $$

    Wait, let me redo this carefully:

    $$
    B\Sigma + \Sigma B^\top = \begin{pmatrix}-a+c-a+c & -c+b-a-c \\ -a-c-c+b & -c-b+c-b \end{pmatrix}
    $$

    Hmm, let me just add element-by-element. $(B\Sigma)_{11} = -a+c$, $(\Sigma B^\top)_{11} = -a+c$, sum $= -2a+2c$. Setting $-2a+2c = -1$ gives $a - c = 1/2$. $(B\Sigma+\Sigma B^\top)_{22} = (-c-b)+(-c-b) = -2c-2b$. Setting $-2b-2c=-1$ gives $b+c=1/2$. Off-diagonal $(1,2)$: $(-c+b)+(-a-c) = -a+b-2c = 0$. So $b = a+2c$.

    From $a-c=1/2$ and $b+c=1/2$: $b = 1/2-c$ and $a = 1/2+c$. From $b=a+2c$: $1/2-c = 1/2+c+2c$, so $-c = 3c$, giving $c = 0$. Then $a = b = 1/2$.

    So $\Sigma = \frac{1}{2}I$ and the invariant measure is $\pi = \mathcal{N}(0, \frac{1}{2}I)$.

    **Reversibility:** The process is reversible if and only if $B\Sigma = \Sigma B^\top$ (the drift is self-adjoint in $L^2(\pi)$). We have $B\Sigma = \frac{1}{2}B$ and $\Sigma B^\top = \frac{1}{2}B^\top$, so reversibility requires $B = B^\top$. But

    $$
    B = \begin{pmatrix}-1&1\\-1&-1\end{pmatrix} \ne \begin{pmatrix}-1&-1\\1&-1\end{pmatrix} = B^\top
    $$

    So the process is **not reversible**. The antisymmetric part of $B$ (the rotation component $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$) generates a probability current that circulates around the origin, breaking detailed balance.

---

**Exercise 4.** Prove that reversibility (detailed balance) implies invariance. That is, show that if for all bounded measurable $f, g$ and all $t \ge 0$,

$$
\int f(x)\,(P_t g)(x)\,\pi(\mathrm{d}x) = \int g(x)\,(P_t f)(x)\,\pi(\mathrm{d}x)
$$

then $\pi P_t = \pi$.

??? success "Solution to Exercise 4"
    Assume detailed balance holds: for all bounded measurable $f, g$ and $t \ge 0$,

    $$
    \int f(x)\,(P_t g)(x)\,\pi(\mathrm{d}x) = \int g(x)\,(P_t f)(x)\,\pi(\mathrm{d}x)
    $$

    To show $\pi P_t = \pi$, we must show $\int P_t f\,\mathrm{d}\pi = \int f\,\mathrm{d}\pi$ for all bounded measurable $f$.

    Set $g \equiv 1$ in the detailed balance condition. Then $P_t g = P_t 1 = 1$ (since $P_t$ is a Markov semigroup, $P_t 1 = 1$). The left side becomes

    $$
    \int f(x) \cdot 1\,\pi(\mathrm{d}x) = \int f\,\mathrm{d}\pi
    $$

    The right side becomes

    $$
    \int 1 \cdot (P_t f)(x)\,\pi(\mathrm{d}x) = \int P_t f\,\mathrm{d}\pi
    $$

    Therefore $\int f\,\mathrm{d}\pi = \int P_t f\,\mathrm{d}\pi$ for all bounded measurable $f$, which is exactly $\pi P_t = \pi$. $\square$

---

**Exercise 5.** Give an example of a diffusion that has an invariant measure but is **not** reversible. (Hint: consider adding a non-gradient drift component to a gradient diffusion.) Verify invariance directly and explain why detailed balance fails.

??? success "Solution to Exercise 5"
    Consider the two-dimensional diffusion

    $$
    \mathrm{d}X_t = b(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t
    $$

    with drift $b(x) = -\nabla V(x) + \gamma(x)$, where $V(x) = \frac{1}{2}|x|^2$ and $\gamma(x) = (-x^2, x^1)^\top$ is a divergence-free rotational field ($\nabla \cdot \gamma = 0$).

    **Invariance:** The stationary Fokker–Planck equation is $\mathcal{L}^*\pi = 0$:

    $$
    -\nabla \cdot (b\,\pi) + \Delta\pi = 0
    $$

    Try $\pi(x) \propto e^{-V(x)} = e^{-|x|^2/2}$. Then $\nabla\pi = -(\nabla V)\pi$ and:

    $$
    -\nabla\cdot(b\,\pi) + \Delta\pi = -\nabla\cdot\bigl((-\nabla V + \gamma)\pi\bigr) + \Delta\pi
    $$

    The gradient part: $-\nabla\cdot(-\nabla V\,\pi) + \Delta\pi = \nabla\cdot(\nabla V\,\pi) + \Delta\pi = 0$ (this is the same cancellation as for the pure gradient diffusion).

    The rotational part: $-\nabla\cdot(\gamma\,\pi) = -\gamma\cdot\nabla\pi - (\nabla\cdot\gamma)\pi = -\gamma\cdot(-\nabla V\,\pi) - 0 = \gamma\cdot\nabla V\,\pi$. Now $\gamma \cdot \nabla V = (-x^2, x^1)\cdot(x^1, x^2) = -x^1 x^2 + x^1 x^2 = 0$. So the rotational drift does not affect the invariant measure.

    Therefore $\pi(x) \propto e^{-|x|^2/2}$ is invariant.

    **Detailed balance fails:** Reversibility requires $\mathcal{L}$ to be self-adjoint in $L^2(\pi)$. The generator is $\mathcal{L}f = (-\nabla V + \gamma)\cdot\nabla f + \Delta f$. The rotational component $\gamma\cdot\nabla f$ is antisymmetric in $L^2(\pi)$ (since $\gamma$ is divergence-free and orthogonal to $\nabla V$):

    $$
    \int (\gamma\cdot\nabla f)\,g\,\pi\,\mathrm{d}x = -\int f\,(\gamma\cdot\nabla g)\,\pi\,\mathrm{d}x
    $$

    This antisymmetric part breaks the self-adjointness of $\mathcal{L}$, so detailed balance fails. Physically, the rotational drift induces a probability current circulating around the origin.

---

**Exercise 6.** Suppose a one-dimensional diffusion $\mathrm{d}X_t = b(X_t)\,\mathrm{d}t + \sigma(X_t)\,\mathrm{d}W_t$ on an interval $(l, r)$ has generator $\mathcal{L}f = b\,f' + \frac{1}{2}\sigma^2 f''$. Using the stationary Fokker–Planck equation, show that any invariant density must satisfy

$$
\pi(x) = \frac{C}{\sigma^2(x)}\exp\!\left(\int^x \frac{2\,b(y)}{\sigma^2(y)}\,\mathrm{d}y\right)
$$

for some normalising constant $C > 0$. Apply this formula to recover the invariant density of the OU process from Exercise 1.

??? success "Solution to Exercise 6"
    The generator is $\mathcal{L}f = bf' + \frac{1}{2}\sigma^2 f''$. The adjoint operator $\mathcal{L}^*$ acts on densities as

    $$
    \mathcal{L}^*\pi = -(b\pi)' + \frac{1}{2}(\sigma^2\pi)''
    $$

    Setting $\mathcal{L}^*\pi = 0$ and integrating once (with the integration constant set to zero for integrability at the boundary):

    $$
    -b(x)\,\pi(x) + \frac{1}{2}\bigl(\sigma^2(x)\,\pi(x)\bigr)' = 0
    $$

    Expanding the derivative:

    $$
    -b\,\pi + \frac{1}{2}(\sigma^2)'\pi + \frac{1}{2}\sigma^2\pi' = 0
    $$

    Dividing by $\frac{1}{2}\sigma^2\pi$:

    $$
    \frac{\pi'}{\pi} = \frac{2b - (\sigma^2)'}{\sigma^2} = \frac{2b}{\sigma^2} - \frac{(\sigma^2)'}{\sigma^2}
    $$

    Integrating:

    $$
    \log\pi(x) = \int^x \frac{2b(y)}{\sigma^2(y)}\,\mathrm{d}y - \log\sigma^2(x) + \text{const}
    $$

    Exponentiating:

    $$
    \pi(x) = \frac{C}{\sigma^2(x)}\exp\!\left(\int^x \frac{2b(y)}{\sigma^2(y)}\,\mathrm{d}y\right)
    $$

    **Application to the OU process:** With $b(x) = -\theta x$ and $\sigma^2 = \sigma^2$ (constant):

    $$
    \pi(x) = \frac{C}{\sigma^2}\exp\!\left(\int^x \frac{-2\theta y}{\sigma^2}\,\mathrm{d}y\right) = \frac{C}{\sigma^2}\exp\!\left(-\frac{\theta x^2}{\sigma^2}\right)
    $$

    This is $\mathcal{N}(0, \sigma^2/(2\theta))$, consistent with Exercise 1.
