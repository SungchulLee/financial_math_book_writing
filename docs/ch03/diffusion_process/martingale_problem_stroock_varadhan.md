# Martingale Problem (Stroock–Varadhan)

## Concept Definition

The **martingale problem** is an alternative formulation of diffusion processes that defines the process entirely through its generator, without reference to a specific Brownian motion or probability space. This approach is essential for proving uniqueness in law and for studying diffusions with irregular coefficients.

Let $b : \mathbb{R}^d \to \mathbb{R}^d$ and $a : \mathbb{R}^d \to \mathbb{R}^{d \times d}$ be measurable, with $a(x)$ symmetric and non-negative definite for all $x$. Define the second-order differential operator

$$
(\mathcal{L}f)(x)
= b^{i}(x)\,\frac{\partial f}{\partial x_i}(x)
+ \frac{1}{2}\,a^{ij}(x)\,\frac{\partial^2 f}{\partial x_i \partial x_j}(x),
\qquad f \in C_c^\infty(\mathbb{R}^d).
$$

(Einstein summation is in force; $i, j$ run from $1$ to $d$.)

!!! info "Definition: Solution to the Martingale Problem"
    Fix an initial law $\mu$ on $\mathbb{R}^d$. A probability measure $\mathbb{P}$ on the path space $C([0,\infty); \mathbb{R}^d)$ **solves the martingale problem for $(\mathcal{L}, \mu)$** if:

    1. The coordinate process $X_0$ has law $\mu$ under $\mathbb{P}$.
    2. For every $f \in C_c^\infty(\mathbb{R}^d)$, the process

    $$
    M_t^f := f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s
    $$

    is a $\mathbb{P}$-martingale with respect to $\mathcal{F}_t = \sigma(X_s : 0 \le s \le t)$.

The martingale problem is **well-posed** if a solution exists and is unique.

---

## Explanation

### Why This Formulation?

The SDE approach requires: (a) a fixed probability space, (b) an explicit Brownian motion $W$, (c) sufficient regularity of $\sigma$ to define the stochastic integral. The martingale problem requires **none of these**. It defines a diffusion purely through the operator $\mathcal{L}$, making it the natural framework when:

- $a(x)$ is degenerate (not strictly positive definite),
- coefficients are merely continuous (not Lipschitz),
- one wants to study **uniqueness in law** independently of pathwise uniqueness.

### Relation to SDEs

If $a = \sigma\sigma^\top$ and $X$ solves the SDE

$$
\mathrm{d}X_t^{i} = b^{i}(X_t)\,\mathrm{d}t + \sigma^{i\alpha}(X_t)\,\mathrm{d}W_t^{\alpha},
$$

then Itô's formula gives

$$
f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s
= \int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^{\alpha},
$$

which is a local martingale (a true martingale under mild integrability conditions). Hence **every strong solution of the SDE solves the martingale problem**. The converse — constructing an SDE from a solution of the martingale problem — requires extracting a Brownian motion. This is done in two steps: first, the **Doob–Meyer decomposition** identifies the quadratic variation of the local martingale $M^f$, which determines $a(x)$; second, the **martingale representation theorem** (Lévy's characterisation) extracts a BM $W$ such that $M^f_t = \int_0^t \partial_i f(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha$, where $\sigma$ is a matrix square root of $a$ with $a = \sigma\sigma^\top$. Both steps are possible when $a(x)$ is strictly positive definite; in the degenerate case the representation breaks down.

### Uniqueness in Law vs Pathwise Uniqueness

These are distinct concepts:

- **Pathwise uniqueness**: any two strong solutions on the same $(\Omega, W)$ agree a.s.
- **Uniqueness in law**: any two solutions of the martingale problem (possibly on different spaces) have the same finite-dimensional distributions.

Well-posedness of the martingale problem is **equivalent to uniqueness in law** for the SDE. Pathwise uniqueness implies uniqueness in law (by the Yamada–Watanabe theorem), but not vice versa.

### The Stroock–Varadhan Theorem

!!! theorem "Theorem (Stroock–Varadhan, 1969–1972)"
    Suppose $b$ is bounded and measurable and $a$ is **bounded, continuous, and uniformly elliptic**: there exists $\lambda > 0$ such that

    $$
    \xi^\top a(x)\,\xi \ge \lambda\,|\xi|^2
    \qquad \text{for all } x, \xi \in \mathbb{R}^d.
    $$

    Then for every initial point $x_0 \in \mathbb{R}^d$, the martingale problem for $(\mathcal{L}, \delta_{x_0})$ has a **unique solution**. Moreover, the solution is a strong Markov process with continuous paths.

This is the central result of Stroock and Varadhan's theory. Its power lies in requiring only **continuity** of $a$ (not Lipschitz), and allowing $b$ to be merely measurable and bounded.

!!! warning "Scope of the Theorem"
    Uniform ellipticity ($a \ge \lambda I$) is essential. For degenerate $a$ (e.g. hypoelliptic operators satisfying Hörmander's condition), well-posedness requires a separate analysis. The theorem does not apply directly to degenerate diffusions.

---

## Diagram / Example

### Example: A Non-Lipschitz Case the SDE Approach Cannot Handle Directly

Consider $d = 1$, $b = 0$, $a(x) = |x|^{2\alpha}$ for $\alpha \in (0, 1/2)$. Then $\sigma(x) = |x|^\alpha$ is Hölder continuous but not Lipschitz at $x = 0$. For this range the SDE $\mathrm{d}X_t = |X_t|^\alpha\,\mathrm{d}W_t$ does **not** have a unique strong solution (Tanaka's example: both $X \equiv 0$ and a non-trivial solution exist). By contrast, for $\alpha \ge 1/2$ the Yamada–Watanabe criterion recovers pathwise uniqueness even without Lipschitz regularity. The martingale problem perspective — studying uniqueness of the measure on path space — can still be pursued in the non-Lipschitz regime even when pathwise uniqueness fails.

### Quadratic Variation Test Function

Taking $f(x) = x^i x^j$ in the martingale problem (this function is not in $C_c^\infty(\mathbb{R}^d)$, but the computation extends to polynomial test functions by a standard localisation argument using a sequence of cut-offs $\chi_n \in C_c^\infty$ with $\chi_n \to 1$):

$$
M_t^{x^i x^j}
= X_t^i X_t^j - X_0^i X_0^j
- \int_0^t \left(b^i(X_s) X_s^j + b^j(X_s) X_s^i + a^{ij}(X_s)\right)\mathrm{d}s.
$$

The $a^{ij}$ term arises from the second-order part of $\mathcal{L}$. This shows that **$a^{ij}(x)\,\mathrm{d}t$ is the quadratic covariation rate**, consistent with the SDE definition $\mathrm{d}\langle X^i, X^j\rangle_t = a^{ij}(X_t)\,\mathrm{d}t$.

---

## Proof / Derivation

We sketch the derivation of $M_t^f$ as a martingale from the SDE.

**Given:** $X$ solves the SDE with coefficients $b$, $\sigma$, $a = \sigma\sigma^\top$.

**Apply Itô's formula** to $f \in C_c^\infty(\mathbb{R}^d)$:

$$
f(X_t)
= f(X_0)
+ \int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\mathrm{d}X_s^i
+ \frac{1}{2}\int_0^t \frac{\partial^2 f}{\partial x_i \partial x_j}(X_s)\,\mathrm{d}\langle X^i, X^j\rangle_s.
$$

Substituting $\mathrm{d}X_s^i = b^i(X_s)\,\mathrm{d}s + \sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha$ and $\mathrm{d}\langle X^i, X^j\rangle_s = a^{ij}(X_s)\,\mathrm{d}s$:

$$
f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s
= \int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha.
$$

The right side is a stochastic integral against $W$, hence a local martingale. To upgrade to a **true martingale**: since $f \in C_c^\infty$, the gradient $\nabla f$ is bounded and supported on a compact set $K \subset \mathbb{R}^d$. Under the SDE's linear growth condition on $\sigma$, one verifies

$$
\mathbb{E}\!\int_0^t \sum_{i=1}^d\sum_{\alpha=1}^m \bigl|\partial_i f(X_s)\bigr|^2 \bigl|\sigma^{i\alpha}(X_s)\bigr|^2\,\mathrm{d}s < \infty,
$$

which (by the Itô isometry) ensures the stochastic integral is square-integrable, hence a true martingale. $\square$

---

## What to Remember

- The martingale problem defines a diffusion via its generator $\mathcal{L}$, without fixing a Brownian motion.
- $M_t^f = f(X_t) - f(X_0) - \int_0^t \mathcal{L}f(X_s)\,\mathrm{d}s$ is a martingale for all test functions $f$.
- The **Stroock–Varadhan theorem**: bounded measurable $b$ + bounded continuous uniformly elliptic $a$ $\Rightarrow$ well-posedness.
- Well-posedness of the martingale problem $\Leftrightarrow$ uniqueness in law for the SDE.
- The martingale problem is the right framework for non-Lipschitz and degenerate coefficients.

---

## Exercises

**Exercise 1.** Let $d = 1$, $b(x) = -\theta x$, and $a(x) = \sigma^2$ (constants $\theta > 0$, $\sigma > 0$). Write down the generator $\mathcal{L}$ and explicitly verify that for $f(x) = x$, the process

$$
M_t^f = X_t - X_0 + \theta\int_0^t X_s\,\mathrm{d}s
$$

is a martingale when $X_t$ is an Ornstein–Uhlenbeck process.

---

**Exercise 2.** Using the test function $f(x) = x^i x^j$ in the martingale problem formulation, derive the identity $\mathrm{d}\langle X^i, X^j \rangle_t = a^{ij}(X_t)\,\mathrm{d}t$. Explain the localisation argument needed since $f(x) = x^i x^j$ is not in $C_c^\infty(\mathbb{R}^d)$.

---

**Exercise 3.** Consider $d = 1$ with $b = 0$ and $\sigma(x) = |x|^\alpha$ for $\alpha \in (0,1)$. For which values of $\alpha$ does the Yamada–Watanabe criterion guarantee pathwise uniqueness of the SDE $\mathrm{d}X_t = |X_t|^\alpha\,\mathrm{d}W_t$? For the remaining values, explain why uniqueness in law (well-posedness of the martingale problem) may still hold or fail.

---

**Exercise 4.** State the conditions of the Stroock–Varadhan theorem. For each condition (bounded measurable $b$, bounded continuous $a$, uniform ellipticity), give a concrete one-dimensional example where the condition is violated and describe what goes wrong (non-existence, non-uniqueness, or both).

---

**Exercise 5.** Show that if $X_t$ is a strong solution to the SDE $\mathrm{d}X_t^i = b^i(X_t)\,\mathrm{d}t + \sigma^{i\alpha}(X_t)\,\mathrm{d}W_t^\alpha$ and $f \in C_c^\infty(\mathbb{R}^d)$, then the stochastic integral

$$
\int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha
$$

is a true martingale (not merely a local martingale). What integrability condition on $\nabla f$ and $\sigma$ is used?

---

**Exercise 6.** Explain the relationship between pathwise uniqueness, uniqueness in law, and well-posedness of the martingale problem. State the Yamada–Watanabe theorem and use it to show that pathwise uniqueness implies uniqueness in law but not vice versa. Give a concrete example where uniqueness in law holds but pathwise uniqueness fails.

---

**Exercise 7.** Let $\mathcal{L}_1$ and $\mathcal{L}_2$ be two generators with the same $a^{ij}$ but different drifts $b_1^i \ne b_2^i$. Suppose both martingale problems are well-posed. Can the two solutions have the same law? Justify your answer by considering the martingale $M_t^f$ for a suitable choice of test function $f$.
