# Invariant Measures and Stationarity

## Concept Definition

Let $(X_t)_{t \ge 0}$ be a time-homogeneous Markov process on $\mathbb{R}^d$ with transition semigroup $(P_t)_{t \ge 0}$ defined by

$$
P_t f(x) := \mathbb{E}^x[f(X_t)], \qquad f \text{ bounded measurable}.
$$

The semigroup acts on measures from the right: for a probability measure $\mu$,

$$
(\mu P_t)(A) := \int_{\mathbb{R}^d} P_t \mathbf{1}_A(x)\,\mu(\mathrm{d}x) = \mathbb{P}^{\mu}(X_t \in A).
$$

!!! info "Definition: Invariant Measure"
    A probability measure $\pi$ on $\mathbb{R}^d$ is **invariant** for $(P_t)$ if

    $$
    \pi P_t = \pi \qquad \text{for all } t \ge 0,
    $$

    equivalently, for all bounded measurable $f$ and all $t \ge 0$:

    $$
    \int_{\mathbb{R}^d} P_t f(x)\,\pi(\mathrm{d}x) = \int_{\mathbb{R}^d} f(x)\,\pi(\mathrm{d}x).
    $$

    In other words: if $X_0 \sim \pi$ then $X_t \sim \pi$ for all $t \ge 0$.

!!! info "Definition: Stationarity"
    A process $(X_t)$ is **stationary** if its finite-dimensional distributions are invariant under time shifts: for all $h \ge 0$ and all $0 \le t_1 < \cdots < t_k$,

    $$
    (X_{t_1 + h}, \dots, X_{t_k + h}) \stackrel{d}{=} (X_{t_1}, \dots, X_{t_k}).
    $$

    Starting a Markov process from an invariant measure $\pi$ yields a stationary process.

---

## Explanation

### Generator Characterisation

Let $\mathcal{L}$ be the infinitesimal generator of $(P_t)$. If $\pi$ is invariant, differentiating $\int P_t f\,\mathrm{d}\pi = \int f\,\mathrm{d}\pi$ at $t = 0$ gives

$$
\int_{\mathbb{R}^d} (\mathcal{L}f)(x)\,\pi(\mathrm{d}x) = 0
\qquad \text{for all } f \in \mathrm{Dom}(\mathcal{L}).
$$

The interchange of differentiation and integration is justified by dominated convergence when $f \in \mathrm{Dom}(\mathcal{L})$ (so $\frac{P_t f - f}{t} \to \mathcal{L}f$ in $L^\infty$ and is uniformly bounded). In terms of the formal $L^2$-adjoint $\mathcal{L}^*$, this is $\mathcal{L}^* \pi = 0$.

### Fokker–Planck Equation for Stationary Densities

For a diffusion with drift $b$ and covariance matrix $a = \sigma\sigma^\top$, if $\pi$ has a density (also denoted $\pi$), stationarity requires $\mathcal{L}^*\pi = 0$:

$$
0
= -\frac{\partial}{\partial x_i}\!\bigl(b^{i}(x)\,\pi(x)\bigr)
+ \frac{1}{2}\,\frac{\partial^2}{\partial x_i \partial x_j}\!\bigl(a^{ij}(x)\,\pi(x)\bigr).
$$

This is the **stationary Fokker–Planck equation**. It is an elliptic PDE for the unknown density $\pi$.

### Existence of Invariant Measures

An invariant measure need not exist for every diffusion. Sufficient conditions include:

- **Lyapunov / Foster criterion**: there exist a function $V \ge 1$, a compact set $C$, and constants $\alpha > 0$, $K < \infty$ such that $\mathcal{L}V(x) \le -\alpha V(x) + K\,\mathbf{1}_C(x)$. This implies tightness of the time-averages $\frac{1}{T}\int_0^T P_t(x, \cdot)\,\mathrm{d}t$ and, by Prokhorov, existence of an invariant measure.
- **Gradient diffusion**: if $\int e^{-V(x)}\,\mathrm{d}x < \infty$, the gradient diffusion has invariant density $\pi \propto e^{-V}$ (see Example below).

Uniqueness typically requires irreducibility (every open set is reachable) and a non-degeneracy condition on $a$.

### Reversibility and Detailed Balance

A stronger condition than invariance is **reversibility**.

!!! info "Definition: Reversibility"
    A stationary process $(X_t)$ with invariant measure $\pi$ is **reversible** (satisfies **detailed balance**) if for all bounded measurable $f, g$ and all $t \ge 0$:

    $$
    \int f(x)\,(P_t g)(x)\,\pi(\mathrm{d}x)
    = \int g(x)\,(P_t f)(x)\,\pi(\mathrm{d}x).
    $$

    Equivalently, $\mathcal{L}$ is self-adjoint in $L^2(\pi)$.

Reversibility implies that the process is **time-symmetric**: $(X_t)_{0 \le t \le T}$ and $(X_{T-t})_{0 \le t \le T}$ have the same law whenever $X_0 \sim \pi$. This connects directly to time reversal of diffusions; see [Time Reversal of Diffusions](time_reversal_of_diffusions.md).

---

## Diagram / Example

### Example: Gradient Diffusion (Langevin Equation)

Consider

$$
\mathrm{d}X_t = -\nabla V(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t,
$$

where $V : \mathbb{R}^d \to \mathbb{R}$ is smooth and $Z := \int_{\mathbb{R}^d} e^{-V(x)}\,\mathrm{d}x < \infty$.

**Claim.** $\pi(x) = Z^{-1} e^{-V(x)}$ is an invariant density.

**Verification via Fokker–Planck.** Here $b^i = -\partial_i V$ and $a^{ij} = 2\delta^{ij}$. The stationary equation $\mathcal{L}^*\pi = 0$ becomes

$$
\frac{\partial}{\partial x_i}\!\bigl(\partial_i V \cdot \pi\bigr) + \Delta \pi = 0.
$$

Substituting $\pi = Z^{-1}e^{-V}$ and computing each term separately (for a fixed index $i$, no sum):

$$
\frac{\partial}{\partial x_i}\!\bigl(\partial_i V \cdot e^{-V}\bigr)
= e^{-V}\bigl(\partial_i^2 V - (\partial_i V)^2\bigr),
\qquad
\partial_i^2(e^{-V}) = e^{-V}\bigl((\partial_i V)^2 - \partial_i^2 V\bigr).
$$

Summing over $i$: the two contributions cancel term by term, giving $\mathcal{L}^*\pi = 0$. $\square$

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
h'(t) = \int \mathcal{L}(P_t f)\,\mathrm{d}\pi = 0,
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

---

**Exercise 2.** Let $V(x) = \frac{1}{4}x^4 - \frac{1}{2}x^2$ (a double-well potential) on $\mathbb{R}$. Consider the gradient diffusion $\mathrm{d}X_t = -V'(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t$. Write down the invariant density $\pi(x)$ (up to a normalising constant). Sketch $\pi(x)$ and identify the locations of its maxima. Is this process reversible?

---

**Exercise 3.** Construct a Lyapunov function $V(x) = 1 + |x|^2$ for the diffusion $\mathrm{d}X_t = -X_t\,\mathrm{d}t + \mathrm{d}W_t$ in $\mathbb{R}^d$. Verify the Foster–Lyapunov criterion $\mathcal{L}V(x) \le -\alpha V(x) + K\,\mathbf{1}_C(x)$ by computing $\mathcal{L}V$, and find explicit constants $\alpha > 0$, $K < \infty$, and a compact set $C$.

---

**Exercise 4.** Consider the two-dimensional diffusion

$$
\mathrm{d}X_t^1 = -X_t^1\,\mathrm{d}t + X_t^2\,\mathrm{d}t + \mathrm{d}W_t^1, \qquad \mathrm{d}X_t^2 = -X_t^1\,\mathrm{d}t - X_t^2\,\mathrm{d}t + \mathrm{d}W_t^2.
$$

Find the invariant measure (hint: try a Gaussian ansatz). Is this process reversible? Justify your answer by checking whether $\mathcal{L}$ is self-adjoint in $L^2(\pi)$.

---

**Exercise 5.** Prove that reversibility (detailed balance) implies invariance. That is, show that if for all bounded measurable $f, g$ and all $t \ge 0$,

$$
\int f(x)\,(P_t g)(x)\,\pi(\mathrm{d}x) = \int g(x)\,(P_t f)(x)\,\pi(\mathrm{d}x),
$$

then $\pi P_t = \pi$.

---

**Exercise 6.** Give an example of a diffusion that has an invariant measure but is **not** reversible. (Hint: consider adding a non-gradient drift component to a gradient diffusion.) Verify invariance directly and explain why detailed balance fails.

---

**Exercise 7.** Suppose a one-dimensional diffusion $\mathrm{d}X_t = b(X_t)\,\mathrm{d}t + \sigma(X_t)\,\mathrm{d}W_t$ on an interval $(l, r)$ has generator $\mathcal{L}f = b\,f' + \frac{1}{2}\sigma^2 f''$. Using the stationary Fokker–Planck equation, show that any invariant density must satisfy

$$
\pi(x) = \frac{C}{\sigma^2(x)}\exp\!\left(\int^x \frac{2\,b(y)}{\sigma^2(y)}\,\mathrm{d}y\right)
$$

for some normalising constant $C > 0$. Apply this formula to recover the invariant density of the OU process from Exercise 1.
