# Time Reversal of Diffusions

## Concept Definition

Given the [diffusion](diffusion_process_overview.md) $(X_t)_{0 \le t \le T}$ with drift $b^i(t,x)$ and covariance $a^{ij}(t,x) = \sigma^{i\alpha}\sigma^{j\alpha}$, time reversal asks: what SDE does the reversed process $\widetilde{X}_t := X_{T-t}$ satisfy? Assume $X_t$ admits a smooth positive density $p(t, x)$ for each $t \in (0, T]$.

Define the **time-reversed process**:

$$
\widetilde{X}_t := X_{T-t}, \qquad 0 \le t \le T
$$

!!! info "Theorem (Haussmann–Pardoux, 1986; Anderson, 1982)"
    Under regularity conditions ensuring $p(t,x) > 0$ and sufficient smoothness, $(\widetilde{X}_t)_{0 \le t \le T}$ solves the SDE

    $$
    \mathrm{d}\widetilde{X}_t^{i}
    = \widetilde{b}^{i}(t, \widetilde{X}_t)\,\mathrm{d}t

    + \sigma^{i\alpha}(T-t, \widetilde{X}_t)\,\mathrm{d}\widetilde{W}_t^{\alpha}
    $$

    where $(\widetilde{W}_t)$ is a Brownian motion with respect to the **backward filtration** $\widetilde{\mathcal{F}}_t = \sigma(X_s : T-t \le s \le T)$, and the **reversed drift** is

    $$
    \boxed{
    \widetilde{b}^{i}(t, x)
    = -b^{i}(T-t, x)

    + \frac{1}{p(T-t, x)}\,\frac{\partial}{\partial x_j}\!\bigl(a^{ij}(T-t, x)\,p(T-t, x)\bigr)
    }
    $$

---

## Explanation

### The Score Term and Its Meaning

The reversed drift contains two parts:

$$
\widetilde{b}^{i}(t, x)
= \underbrace{-b^{i}(T-t, x)}_{\text{negated forward drift}}

+ \underbrace{\frac{\partial a^{ij}}{\partial x_j}(T-t,x) + a^{ij}(T-t,x)\,\partial_{x_j} \log p(T-t, x)}_{\text{score correction}}
$$

The **score** $\nabla \log p(t,x) = \nabla_x \log p(t,x)$ is the gradient of the log-density of $X_t$. For constant $a = \sigma\sigma^\top$ (spatially homogeneous diffusion), the formula simplifies to

$$
\widetilde{b}^{i}(t, x) = -b^{i}(T-t, x) + a^{ij}\,\partial_{x_j} \log p(T-t, x)
$$

**Intuition.** When running a diffusion backward, the noise term is unchanged (the diffusion matrix is the same), but the drift must be corrected to account for the flow of probability mass encoded in $p$. The score term steers the reversed process toward regions of higher density, counteracting the tendency of the forward noise to spread out.

### The Backward Filtration

A critical point: $(\widetilde{W}_t)$ is a Brownian motion adapted to the **backward filtration** $\widetilde{\mathcal{F}}_t$, not the forward one. This means $\widetilde{X}$ is a semimartingale in the backward sense. One must distinguish:

- **Forward SDE**: adapted to $(\mathcal{F}_t)$, driven by $W$.
- **Reversed SDE**: adapted to $(\widetilde{\mathcal{F}}_t)$, driven by a new BM $\widetilde{W}$ whose existence is guaranteed by the Doob–Meyer decomposition of $\widetilde{X}$ as a backward semimartingale.

Conflating forward and backward filtrations is the most common source of error in time reversal arguments.

### Connection to Doob's h-Transform

In the constant-$a$ case, the score correction $a\,\nabla\log p$ can be understood via a **Doob $h$-transform**: weighting the path measure by $h(t,x) = p(t,x)$ (the density itself) produces a new drift that guides the process toward the support of $p$. Time reversal is essentially a Doob $h$-transform with $h = p$.

### Connection to Score-Based Generative Models

The score term $\nabla\log p(t,x)$ is precisely what modern **score-based diffusion models** (e.g. DDPM, score matching) learn from data. In the practically common case of **constant** $a = \sigma\sigma^\top$ (spatially homogeneous noise), the reversed SDE takes the explicit form

$$
\mathrm{d}\widetilde{X}_t = \bigl(-b(T-t,\widetilde{X}_t) + a\,\nabla\log p(T-t,\widetilde{X}_t)\bigr)\mathrm{d}t + \sigma\,\mathrm{d}\widetilde{W}_t
$$

For spatially varying $\sigma$, the full formula from the theorem above applies, with the additional divergence term $\partial_{x_j} a^{ij}$. The practical approach: train a neural network to approximate $\nabla\log p(t,x)$ at all noise levels $t$, then run the reversed SDE from pure noise to generate new samples. The Haussmann–Pardoux theorem is the mathematical foundation underlying this entire class of generative models.

---

## Diagram / Example

### Reversible Stationary Case

If $X_0 \sim \pi$ where $\pi$ is the invariant measure and the process is **reversible** (detailed balance holds), then

$$
(X_t)_{0 \le t \le T} \stackrel{d}{=} (X_{T-t})_{0 \le t \le T}
$$

In this case $p(t, x) = \pi(x)$ for all $t$, the score is $\nabla\log\pi(x)$, and one can verify that $\widetilde{b}^i = b^i$: the reversed drift equals the forward drift, consistent with time symmetry.

**Example — Ornstein–Uhlenbeck process.** Consider

$$
\mathrm{d}X_t = -\theta X_t\,\mathrm{d}t + \sigma\,\mathrm{d}W_t, \qquad \theta > 0
$$

The invariant measure is $\pi = \mathcal{N}(0, \sigma^2/2\theta)$, so $\nabla\log\pi(x) = -x/(\sigma^2/2\theta) = -2\theta x/\sigma^2$. Substituting into the reversed drift formula (constant $a = \sigma^2$):

$$
\widetilde{b}(t,x) = -(-\theta x) + \sigma^2 \cdot \left(-\frac{2\theta x}{\sigma^2}\right) = \theta x - 2\theta x = -\theta x = b(x). \checkmark
$$

Time reversal produces the **same OU process**.

### Non-Reversible Case: Drifted Brownian Motion

Let $\mathrm{d}X_t = \mu\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$ on $[0,T]$ with $X_0 = 0$. Then $p(t,x) = \phi(x; \mu t, \sigma^2 t)$ (Gaussian) and

$$
\partial_x \log p(t,x) = -\frac{x - \mu t}{\sigma^2 t}
$$

The reversed drift is

$$
\widetilde{b}(t, x) = -\mu + \sigma^2 \cdot \left(-\frac{x - \mu(T-t)}{\sigma^2(T-t)}\right) = -\mu - \frac{x - \mu(T-t)}{T-t}
$$

This is a **Brownian bridge** drift. To read the direction: $\widetilde{X}_0 = X_T$ (the reversed process starts at the forward endpoint) and $\widetilde{X}_T = X_0 = 0$ (it ends at the forward starting point). The drift $-(x - \mu(T-t))/(T-t)$ pulls $\widetilde{X}$ toward $0$ as $t \to T$, confirming it is a bridge from $X_T$ back to $0$, with the original drift negated. Time reversal converts free Brownian motion (with drift) into a conditioned process pinned at both endpoints.

---

## Proof / Derivation

We sketch the formal derivation of the reversed drift formula in the constant-$a$ case.

**Step 1: Forward Fokker–Planck.** The density $p(t,x)$ satisfies

$$
\partial_t p = -\partial_{x_i}(b^i p) + \frac{1}{2} a^{ij}\,\partial_{x_i x_j} p
$$

**Step 2: Reversed process as backward semimartingale.** By the theory of backward stochastic calculus (see Pardoux 1986), $\widetilde{X}_t = X_{T-t}$ is a semimartingale under $\widetilde{\mathcal{F}}_t$ admitting a decomposition

$$
\mathrm{d}\widetilde{X}_t = \widetilde{b}(t, \widetilde{X}_t)\,\mathrm{d}t + \sigma\,\mathrm{d}\widetilde{W}_t
$$

**Step 3: Identify the drift.** We work in the **constant-$a$** case (the general case requires one extra step noted below). The reversed density $\widetilde{p}(t,x) = p(T-t,x)$ must satisfy the forward Fokker–Planck equation for $\widetilde{X}$:

$$
\partial_t \widetilde{p} = -\partial_{x_i}(\widetilde{b}^i \widetilde{p}) + \frac{1}{2}a^{ij}\,\partial_{x_i x_j}\widetilde{p}
$$

Substituting $\widetilde{p}(t,x) = p(T-t,x)$ so $\partial_t \widetilde{p} = -\partial_t p(T-t,x)$, and using the forward Fokker–Planck for $p$ gives (after rearrangement):

$$
\partial_{x_i}(\widetilde{b}^i \widetilde{p})
= \partial_{x_i}(b^i \widetilde{p}) - a^{ij}\,\partial_{x_i x_j}\widetilde{p}
$$

Dividing by $\widetilde{p} > 0$ and expanding $\partial_{x_j}(a^{ij}\widetilde{p})/\widetilde{p} = \partial_{x_j}a^{ij} + a^{ij}\partial_{x_j}\log\widetilde{p}$ (using constant $a$, so $\partial_{x_j}a^{ij} = 0$) yields $\widetilde{b}^i = -b^i + a^{ij}\partial_{x_j}\log p(T-t,x)$, consistent with the boxed formula. For **spatially varying $a$**, the divergence term $\partial_{x_j}a^{ij}$ is non-zero and the same calculation produces the full formula $\widetilde{b}^i = -b^i + \frac{1}{p}\partial_{x_j}(a^{ij}p)$ stated in the theorem. $\square$

---

## What to Remember

- Time reversal introduces a **score correction** $a\,\nabla\log p(t,x)$ to the negated forward drift.
- The reversed process is a semimartingale with respect to the **backward filtration**; $\widetilde{W}$ is a new BM, not $-W$.
- Under **detailed balance** (reversibility), the reversed drift equals the forward drift and $\widetilde{X} \stackrel{d}{=} X$.
- The score term connects time reversal to **score-based generative models** (diffusion models in ML), where learning $\nabla\log p$ enables sampling by running the SDE in reverse.

---

## Exercises

**Exercise 1.** Let $\mathrm{d}X_t = \mu\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$ on $[0, T]$ with $X_0 = x_0$, where $\mu, \sigma$ are constants. The density of $X_t$ is $p(t, x) = \phi(x;\, x_0 + \mu t,\, \sigma^2 t)$ (Gaussian). Compute the score $\partial_x \log p(t, x)$ and substitute into the reversed drift formula to derive the SDE for $\widetilde{X}_t = X_{T-t}$. Show that $\widetilde{X}$ has a Brownian bridge-type drift.

??? success "Solution to Exercise 1"
    With $X_0 = x_0$, the density of $X_t$ is Gaussian: $p(t, x) = \phi(x;\, x_0 + \mu t,\, \sigma^2 t)$, where $\phi(x; m, v) = (2\pi v)^{-1/2}\exp(-(x-m)^2/(2v))$.

    The score is

    $$
    \partial_x \log p(t, x) = -\frac{x - (x_0 + \mu t)}{\sigma^2 t}
    $$

    The reversed drift formula (constant $a = \sigma^2$) gives

    $$
    \widetilde{b}(t, x) = -b(T-t, x) + a\,\partial_x \log p(T-t, x)
    $$

    Since $b = \mu$ (constant drift):

    $$
    \widetilde{b}(t, x) = -\mu + \sigma^2 \cdot \left(-\frac{x - (x_0 + \mu(T-t))}{\sigma^2(T-t)}\right) = -\mu - \frac{x - x_0 - \mu(T-t)}{T-t}
    $$

    Simplifying:

    $$
    \widetilde{b}(t, x) = -\mu - \frac{x - x_0}{T-t} + \mu = -\frac{x - x_0}{T-t} + \frac{-\mu(T-t) + \mu(T-t)}{T-t}
    $$

    Wait — let us be more careful:

    $$
    \widetilde{b}(t, x) = -\mu - \frac{x - x_0 - \mu(T-t)}{T-t} = -\mu - \frac{x - x_0}{T-t} + \mu = -\frac{x - x_0}{T-t}
    $$

    The reversed SDE is

    $$
    \mathrm{d}\widetilde{X}_t = -\frac{\widetilde{X}_t - x_0}{T - t}\,\mathrm{d}t + \sigma\,\mathrm{d}\widetilde{W}_t
    $$

    This is a **Brownian bridge drift**: $\widetilde{X}_0 = X_T \sim \mathcal{N}(x_0 + \mu T, \sigma^2 T)$ and the drift pulls $\widetilde{X}_t$ toward $x_0$ as $t \to T$, so $\widetilde{X}_T = x_0 = X_0$. The process is a Brownian bridge from the forward endpoint back to the forward starting point.

---

**Exercise 2.** Consider the Ornstein–Uhlenbeck process $\mathrm{d}X_t = -\theta X_t\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$ with $\theta > 0$, started from the invariant distribution $X_0 \sim \mathcal{N}(0, \sigma^2/(2\theta))$. Show that the reversed drift $\widetilde{b}(t, x)$ equals the forward drift $b(x) = -\theta x$, confirming reversibility. What property of the OU process makes this work?

??? success "Solution to Exercise 2"
    The OU process has $b(x) = -\theta x$, $a = \sigma^2$. Started from the invariant distribution $X_0 \sim \pi = \mathcal{N}(0, \sigma^2/(2\theta))$, the process is stationary, so $p(t, x) = \pi(x)$ for all $t$.

    The score is

    $$
    \partial_x \log \pi(x) = \partial_x \left(-\frac{\theta x^2}{\sigma^2}\right) = -\frac{2\theta x}{\sigma^2}
    $$

    The reversed drift is

    $$
    \widetilde{b}(t, x) = -b(T-t, x) + a\,\partial_x \log p(T-t, x) = -(-\theta x) + \sigma^2 \cdot \left(-\frac{2\theta x}{\sigma^2}\right) = \theta x - 2\theta x = -\theta x
    $$

    Therefore $\widetilde{b}(t, x) = -\theta x = b(x)$, confirming that the reversed drift equals the forward drift.

    **What makes this work:** The OU process is a **gradient diffusion** — the drift $b(x) = -\theta x = -\nabla V(x)$ with $V(x) = \frac{\theta}{2}x^2$ and constant diffusion $\sigma$. Gradient diffusions with constant noise are **reversible** (satisfy detailed balance) with respect to their invariant measure $\pi \propto e^{-V}$. Reversibility means $(X_t)_{0 \le t \le T} \stackrel{d}{=} (X_{T-t})_{0 \le t \le T}$ when started from $\pi$, which forces $\widetilde{b} = b$. The key property is the self-adjointness of $\mathcal{L}$ in $L^2(\pi)$.

---

**Exercise 3.** Let $\mathrm{d}X_t = b(X_t)\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$ with constant $\sigma > 0$ and a smooth density $p(t, x) > 0$. Starting from the forward Fokker–Planck equation

$$
\partial_t p = -\partial_x(b\,p) + \frac{\sigma^2}{2}\,\partial_x^2 p
$$

derive the reversed drift formula $\widetilde{b}(t, x) = -b(T-t, x) + \sigma^2\,\partial_x \log p(T-t, x)$ by requiring that the reversed density $\widetilde{p}(t, x) = p(T-t, x)$ satisfies its own Fokker–Planck equation.

??? success "Solution to Exercise 3"
    The forward Fokker–Planck equation for $p(t,x)$ is

    $$
    \partial_t p = -\partial_x(bp) + \frac{\sigma^2}{2}\partial_x^2 p
    $$

    The reversed density is $\widetilde{p}(t,x) = p(T-t, x)$. This must satisfy its own Fokker–Planck equation with drift $\widetilde{b}$:

    $$
    \partial_t \widetilde{p} = -\partial_x(\widetilde{b}\,\widetilde{p}) + \frac{\sigma^2}{2}\partial_x^2 \widetilde{p}
    $$

    Since $\partial_t \widetilde{p}(t,x) = -\partial_t p(T-t, x)$, substituting the forward Fokker–Planck:

    $$
    -\partial_t p(T-t,x) = \partial_x(b\,p)(T-t,x) - \frac{\sigma^2}{2}\partial_x^2 p(T-t,x) = \partial_x(b\,\widetilde{p}) - \frac{\sigma^2}{2}\partial_x^2\widetilde{p}
    $$

    Equating the two expressions for $\partial_t\widetilde{p}$:

    $$
    \partial_x(b\,\widetilde{p}) - \frac{\sigma^2}{2}\partial_x^2\widetilde{p} = -\partial_x(\widetilde{b}\,\widetilde{p}) + \frac{\sigma^2}{2}\partial_x^2\widetilde{p}
    $$

    Rearranging:

    $$
    \partial_x(\widetilde{b}\,\widetilde{p}) = -\partial_x(b\,\widetilde{p}) + \sigma^2\,\partial_x^2\widetilde{p}
    $$

    Integrating with respect to $x$ (the constant of integration is zero for integrability):

    $$
    \widetilde{b}\,\widetilde{p} = -b\,\widetilde{p} + \sigma^2\,\partial_x\widetilde{p}
    $$

    Dividing by $\widetilde{p} > 0$:

    $$
    \widetilde{b}(t,x) = -b(T-t, x) + \sigma^2\,\frac{\partial_x\widetilde{p}(t,x)}{\widetilde{p}(t,x)} = -b(T-t, x) + \sigma^2\,\partial_x\log p(T-t, x)
    $$

    This completes the derivation of the reversed drift formula. $\square$

---

**Exercise 4.** Explain why the reversed Brownian motion $\widetilde{W}_t$ is adapted to the backward filtration $\widetilde{\mathcal{F}}_t = \sigma(X_s : T - t \le s \le T)$ and is generally **not** adapted to the forward filtration $(\mathcal{F}_t)$. Why does this distinction matter when writing the reversed SDE?

??? success "Solution to Exercise 4"
    The reversed process $\widetilde{X}_t = X_{T-t}$ is defined by "reading the path backwards." The reversed Brownian motion $\widetilde{W}_t$ is constructed via the Doob–Meyer decomposition of $\widetilde{X}_t$ as a semimartingale with respect to the backward filtration.

    The backward filtration is $\widetilde{\mathcal{F}}_t = \sigma(X_s : T-t \le s \le T) = \sigma(\widetilde{X}_r : 0 \le r \le t)$. This encodes information about the **future** of the original process (from time $T-t$ to $T$), which is the **past** of the reversed process.

    $\widetilde{W}_t$ is adapted to $\widetilde{\mathcal{F}}_t$ because it is constructed from the martingale part of $\widetilde{X}$ in the backward decomposition. However, $\widetilde{W}_t$ is generally **not** adapted to the forward filtration $\mathcal{F}_t = \sigma(X_s : 0 \le s \le t)$ because knowing the path from $0$ to $t$ does not determine the reversed martingale increments (which depend on the path from $T-t$ to $T$).

    **Why this matters:** The reversed SDE $\mathrm{d}\widetilde{X}_t = \widetilde{b}\,\mathrm{d}t + \sigma\,\mathrm{d}\widetilde{W}_t$ is an Itô equation with respect to $(\widetilde{\mathcal{F}}_t)$, not $(\mathcal{F}_t)$. If one mistakenly uses the forward filtration, the stochastic integral $\int \sigma\,\mathrm{d}\widetilde{W}$ is not well-defined (the integrand must be adapted to the filtration of the driving Brownian motion). Conflating the two filtrations leads to incorrect applications of Itô's formula and erroneous drift calculations.

---

**Exercise 5.** Consider a two-dimensional diffusion with constant diffusion matrix $a = I$ (the $2 \times 2$ identity) and drift $b(x_1, x_2) = (-x_1 + x_2,\, -x_1 - x_2)^\top$. Suppose the process is started from its invariant distribution. Is this process reversible? Compute the reversed drift $\widetilde{b}$ and compare it to $b$.

??? success "Solution to Exercise 5"
    The drift is $b(x) = (-x^1 + x^2,\, -x^1 - x^2)^\top$, written as $b(x) = Bx$ with $B = \begin{pmatrix}-1&1\\-1&-1\end{pmatrix}$, and $a = I$.

    The eigenvalues of $B$ are $-1 \pm i$ (complex with negative real part), so $B$ is stable and an invariant measure exists. As computed in the invariant measures chapter, the invariant covariance $\Sigma$ solves $B\Sigma + \Sigma B^\top + I = 0$, giving $\Sigma = \frac{1}{2}I$.

    **Reversibility check:** A linear diffusion $\mathrm{d}X = BX\,\mathrm{d}t + \mathrm{d}W$ with $a = I$ is reversible if and only if $B$ is symmetric. Here $B \ne B^\top$ (the off-diagonal entries $1$ and $-1$ differ), so the process is **not reversible**.

    **Reversed drift:** With stationary $p(t,x) = \pi(x)$ (since we start from the invariant distribution), the score is

    $$
    \nabla\log\pi(x) = -\Sigma^{-1}x = -2x
    $$

    The reversed drift is

    $$
    \widetilde{b}(t,x) = -b(x) + a\,\nabla\log\pi(x) = -Bx + I\cdot(-2x) = (-B - 2I)x
    $$

    Computing:

    $$
    -B - 2I = \begin{pmatrix}1&-1\\1&1\end{pmatrix} - \begin{pmatrix}2&0\\0&2\end{pmatrix} = \begin{pmatrix}-1&-1\\1&-1\end{pmatrix}
    $$

    So $\widetilde{b}(x) = B^\top x$ where $B^\top = \begin{pmatrix}-1&-1\\1&-1\end{pmatrix}$.

    Comparing: $b(x) = Bx$ and $\widetilde{b}(x) = B^\top x$. Since $B \ne B^\top$, the reversed drift differs from the forward drift, confirming non-reversibility. The reversed process has the rotation component flipped (clockwise instead of counterclockwise).

---

**Exercise 6.** In the context of score-based generative models, the forward process is often taken as $\mathrm{d}X_t = -\frac{1}{2}\beta(t)\,X_t\,\mathrm{d}t + \sqrt{\beta(t)}\,\mathrm{d}W_t$ for a noise schedule $\beta(t) > 0$. Write down the reversed SDE using the time-reversal formula. Identify the score term $\nabla_x \log p(t, x)$ that must be learned. Why does the forward process eventually converge to an (approximately) standard Gaussian as $t \to \infty$?

??? success "Solution to Exercise 6"
    The forward SDE is $\mathrm{d}X_t = -\frac{1}{2}\beta(t)X_t\,\mathrm{d}t + \sqrt{\beta(t)}\,\mathrm{d}W_t$, with time-dependent $b(t,x) = -\frac{1}{2}\beta(t)x$, $\sigma(t) = \sqrt{\beta(t)}$, and $a(t) = \beta(t)$.

    Since $a$ is spatially constant, the reversed drift formula gives

    $$
    \widetilde{b}(t,x) = -b(T-t, x) + a(T-t)\,\nabla_x\log p(T-t, x) = \frac{1}{2}\beta(T-t)\,x + \beta(T-t)\,\nabla_x\log p(T-t, x)
    $$

    The reversed SDE is

    $$
    \mathrm{d}\widetilde{X}_t = \left[\frac{1}{2}\beta(T-t)\,\widetilde{X}_t + \beta(T-t)\,\nabla_x\log p(T-t, \widetilde{X}_t)\right]\mathrm{d}t + \sqrt{\beta(T-t)}\,\mathrm{d}\widetilde{W}_t
    $$

    The **score term** that must be learned is $s_\theta(x, t) \approx \nabla_x\log p(t, x)$ — the gradient of the log-density of the forward process at time $t$.

    **Convergence to Gaussian:** The forward SDE is a time-inhomogeneous OU process. Its solution (with $X_0 = x_0$) is

    $$
    X_t = x_0\,e^{-\frac{1}{2}\int_0^t \beta(s)\,\mathrm{d}s} + \int_0^t e^{-\frac{1}{2}\int_s^t \beta(r)\,\mathrm{d}r}\sqrt{\beta(s)}\,\mathrm{d}W_s
    $$

    As $t \to \infty$, the first term (the "signal") decays to zero provided $\int_0^\infty \beta(s)\,\mathrm{d}s = \infty$. The variance of the second term (the "noise") converges to $\int_0^\infty \beta(s)e^{-\int_s^\infty \beta(r)\,\mathrm{d}r}\,\mathrm{d}s = 1$. Therefore $X_t \to \mathcal{N}(0, I)$ in distribution as $t \to \infty$. The noise schedule $\beta(t)$ controls the rate at which the data distribution is destroyed and replaced by standard Gaussian noise.

---

**Exercise 7.** Explain the connection between time reversal and Doob's $h$-transform. Specifically, for a diffusion with constant $a$ and forward drift $b$, show that the reversed measure on path space can be obtained by an $h$-transform with $h(t, x) = p(T - t, x)$, where $p$ is the forward density. Verify that $h$ is a space-time harmonic function for the adjoint operator.

??? success "Solution to Exercise 7"
    **Doob's $h$-transform** for a diffusion with generator $\mathcal{L}$ and a positive function $h > 0$ defines a new process with generator

    $$
    \mathcal{L}^h f = \frac{1}{h}\mathcal{L}(hf) - \frac{f}{h}\mathcal{L}h
    $$

    For the space-time setting with generator $\partial_t + \mathcal{L}$, a function $h(t,x) > 0$ defines a new drift. In the constant-$a$ case, $\mathcal{L}f = b \cdot \nabla f + \frac{1}{2}\text{tr}(a\,\nabla^2 f)$, and the $h$-transformed process has drift

    $$
    b^h(t,x) = b(t,x) + a\,\frac{\nabla_x h(t,x)}{h(t,x)} = b(t,x) + a\,\nabla_x\log h(t,x)
    $$

    **Time reversal as $h$-transform:** Set $h(t,x) = p(T-t, x)$. The $h$-transformed drift starting from the **negated** forward drift (accounting for time reversal) is

    $$
    \widetilde{b}(t,x) = -b(T-t, x) + a\,\nabla_x\log h(t,x) = -b(T-t, x) + a\,\nabla_x\log p(T-t, x)
    $$

    which is exactly the reversed drift formula.

    **Verification that $h$ is space-time harmonic for the adjoint:** We need to show that $(\partial_t + \mathcal{L}^*)h = 0$, where $\mathcal{L}^*$ is the formal adjoint of $\mathcal{L}$. For constant $a$, $\mathcal{L}^*g = -\nabla\cdot(bg) + \frac{1}{2}\text{tr}(a\,\nabla^2 g)$.

    With $h(t,x) = p(T-t, x)$, we have $\partial_t h(t,x) = -\partial_t p(T-t, x)$. The forward Fokker–Planck equation states $\partial_t p = \mathcal{L}^* p$, so

    $$
    \partial_t h(t,x) = -(\mathcal{L}^* p)(T-t, x)
    $$

    Meanwhile $\mathcal{L}^* h(t, \cdot) = (\mathcal{L}^* p)(T-t, \cdot)$ (since $h(t,x) = p(T-t,x)$ and $\mathcal{L}^*$ acts on $x$). Therefore

    $$
    (\partial_t + \mathcal{L}^*)h = -\mathcal{L}^* p(T-t, \cdot) + \mathcal{L}^* p(T-t, \cdot) = 0
    $$

    confirming that $h(t,x) = p(T-t, x)$ is space-time harmonic for $\partial_t + \mathcal{L}^*$. $\square$
