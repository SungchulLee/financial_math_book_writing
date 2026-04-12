# Martingale Problem (Stroock–Varadhan)

## Concept Definition

The **martingale problem** is an alternative formulation of diffusion processes that defines the process entirely through its generator, without reference to a specific Brownian motion or probability space. This approach is essential for proving uniqueness in law and for studying diffusions with irregular coefficients.

Let $b : \mathbb{R}^d \to \mathbb{R}^d$ and $a : \mathbb{R}^d \to \mathbb{R}^{d \times d}$ be measurable, with $a(x)$ symmetric and non-negative definite for all $x$. Define the second-order differential operator

$$
(\mathcal{L}f)(x)
= b^{i}(x)\,\frac{\partial f}{\partial x_i}(x)
+ \frac{1}{2}\,a^{ij}(x)\,\frac{\partial^2 f}{\partial x_i \partial x_j}(x),
\qquad f \in C_c^\infty(\mathbb{R}^d)
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
\mathrm{d}X_t^{i} = b^{i}(X_t)\,\mathrm{d}t + \sigma^{i\alpha}(X_t)\,\mathrm{d}W_t^{\alpha}
$$

then Itô's formula gives

$$
f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s
= \int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^{\alpha}
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
- \int_0^t \left(b^i(X_s) X_s^j + b^j(X_s) X_s^i + a^{ij}(X_s)\right)\mathrm{d}s
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
+ \frac{1}{2}\int_0^t \frac{\partial^2 f}{\partial x_i \partial x_j}(X_s)\,\mathrm{d}\langle X^i, X^j\rangle_s
$$

Substituting $\mathrm{d}X_s^i = b^i(X_s)\,\mathrm{d}s + \sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha$ and $\mathrm{d}\langle X^i, X^j\rangle_s = a^{ij}(X_s)\,\mathrm{d}s$:

$$
f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s
= \int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha
$$

The right side is a stochastic integral against $W$, hence a local martingale. To upgrade to a **true martingale**: since $f \in C_c^\infty$, the gradient $\nabla f$ is bounded and supported on a compact set $K \subset \mathbb{R}^d$. Under the SDE's linear growth condition on $\sigma$, one verifies

$$
\mathbb{E}\!\int_0^t \sum_{i=1}^d\sum_{\alpha=1}^m \bigl|\partial_i f(X_s)\bigr|^2 \bigl|\sigma^{i\alpha}(X_s)\bigr|^2\,\mathrm{d}s < \infty
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

??? success "Solution to Exercise 1"
    With $b(x) = -\theta x$ and $a(x) = \sigma^2$, the generator is

    $$
    \mathcal{L}f(x) = -\theta x\,f'(x) + \frac{\sigma^2}{2}\,f''(x)
    $$

    For $f(x) = x$, we have $f'(x) = 1$ and $f''(x) = 0$, so $\mathcal{L}f(x) = -\theta x$. The martingale problem states that

    $$
    M_t^f = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s = X_t - X_0 - \int_0^t (-\theta X_s)\,\mathrm{d}s = X_t - X_0 + \theta\int_0^t X_s\,\mathrm{d}s
    $$

    is a martingale.

    **Verification for OU:** The OU process satisfies $X_t = X_0 e^{-\theta t} + \sigma\int_0^t e^{-\theta(t-s)}\,\mathrm{d}W_s$. Therefore

    $$
    X_t - X_0 + \theta\int_0^t X_s\,\mathrm{d}s = \sigma\int_0^t \mathrm{d}W_s = \sigma W_t
    $$

    To see this: integrating the SDE $\mathrm{d}X_s = -\theta X_s\,\mathrm{d}s + \sigma\,\mathrm{d}W_s$ from $0$ to $t$ gives $X_t - X_0 = -\theta\int_0^t X_s\,\mathrm{d}s + \sigma W_t$, which rearranges to $M_t^f = \sigma W_t$. Since $\sigma W_t$ is a martingale (in fact a Brownian motion scaled by $\sigma$), $M_t^f$ is indeed a martingale.

---

**Exercise 2.** Using the test function $f(x) = x^i x^j$ in the martingale problem formulation, derive the identity $\mathrm{d}\langle X^i, X^j \rangle_t = a^{ij}(X_t)\,\mathrm{d}t$. Explain the localisation argument needed since $f(x) = x^i x^j$ is not in $C_c^\infty(\mathbb{R}^d)$.

??? success "Solution to Exercise 2"
    Take $f(x) = x^i x^j$. Then $\partial_k f = \delta^{ik}x^j + \delta^{jk}x^i$ and $\partial_k\partial_l f = \delta^{ik}\delta^{jl} + \delta^{jk}\delta^{il}$. The generator gives

    $$
    \mathcal{L}(x^ix^j) = b^k(\delta^{ik}x^j + \delta^{jk}x^i) + \frac{1}{2}a^{kl}(\delta^{ik}\delta^{jl} + \delta^{jk}\delta^{il}) = b^i x^j + b^j x^i + a^{ij}
    $$

    The martingale problem asserts that

    $$
    M_t = X_t^i X_t^j - X_0^i X_0^j - \int_0^t \bigl(b^i(X_s)X_s^j + b^j(X_s)X_s^i + a^{ij}(X_s)\bigr)\,\mathrm{d}s
    $$

    is a martingale. Now, from the SDE $\mathrm{d}X^i = b^i\,\mathrm{d}t + \sigma^{i\alpha}\,\mathrm{d}W^\alpha$, by Itô's product rule:

    $$
    \mathrm{d}(X^i X^j) = X^i\,\mathrm{d}X^j + X^j\,\mathrm{d}X^i + \mathrm{d}\langle X^i, X^j\rangle
    $$

    The $\mathrm{d}t$ terms give $b^i X^j + b^j X^i + \mathrm{d}\langle X^i, X^j\rangle / \mathrm{d}t$. Comparing with the $\mathcal{L}(x^ix^j)$ expression, the only way for $M_t$ to be a martingale (no $\mathrm{d}t$ drift in the martingale part) is if

    $$
    \frac{\mathrm{d}\langle X^i, X^j\rangle_t}{\mathrm{d}t} = a^{ij}(X_t)
    $$

    which gives $\mathrm{d}\langle X^i, X^j\rangle_t = a^{ij}(X_t)\,\mathrm{d}t$.

    **Localisation argument:** The function $f(x) = x^ix^j$ is not in $C_c^\infty(\mathbb{R}^d)$. To make the argument rigorous, choose $\chi_n \in C_c^\infty(\mathbb{R}^d)$ with $\chi_n(x) = 1$ for $|x| \le n$, $\chi_n(x) = 0$ for $|x| \ge n+1$, and $0 \le \chi_n \le 1$. Apply the martingale problem to $f_n(x) = \chi_n(x)\,x^ix^j \in C_c^\infty$. For paths that remain in $\{|x| \le n\}$ up to time $t$, $f_n$ and $f$ agree, so the martingale property holds on the event $\{\sup_{s \le t}|X_s| \le n\}$. Letting $n \to \infty$ (using that the process does not explode under the assumed conditions) extends the identity to all paths.

---

**Exercise 3.** Consider $d = 1$ with $b = 0$ and $\sigma(x) = |x|^\alpha$ for $\alpha \in (0,1)$. For which values of $\alpha$ does the Yamada–Watanabe criterion guarantee pathwise uniqueness of the SDE $\mathrm{d}X_t = |X_t|^\alpha\,\mathrm{d}W_t$? For the remaining values, explain why uniqueness in law (well-posedness of the martingale problem) may still hold or fail.

??? success "Solution to Exercise 3"
    The SDE is $\mathrm{d}X_t = |X_t|^\alpha\,\mathrm{d}W_t$ with $b = 0$ and $\sigma(x) = |x|^\alpha$.

    The **Yamada–Watanabe criterion** for pathwise uniqueness in one dimension requires: there exists a strictly increasing function $\rho : [0,\infty) \to [0,\infty)$ with $\rho(0) = 0$ such that $|\sigma(x) - \sigma(y)| \le \rho(|x-y|)$ and $\int_{0+} \rho(u)^{-2}\,\mathrm{d}u = \infty$.

    For $\sigma(x) = |x|^\alpha$, we have $|\sigma(x) - \sigma(y)| \le C|x - y|^\alpha$ (Hölder continuity of $x \mapsto |x|^\alpha$). Taking $\rho(u) = Cu^\alpha$, the integrability condition becomes

    $$
    \int_{0+} u^{-2\alpha}\,\mathrm{d}u = \infty \quad \Longleftrightarrow \quad 2\alpha \le 1 \quad \Longleftrightarrow \quad \alpha \ge \frac{1}{2}
    $$

    So **pathwise uniqueness holds for $\alpha \ge 1/2$**.

    For $\alpha \in (0, 1/2)$: pathwise uniqueness **fails**. The classical example is Tanaka's SDE — both $X_t \equiv 0$ and a non-trivial solution coexist when $X_0 = 0$. However, uniqueness in law (well-posedness of the martingale problem) is a separate question. For $\alpha \in (0, 1/2)$ the covariance matrix $a(x) = |x|^{2\alpha}$ vanishes at $x = 0$, violating uniform ellipticity, so the Stroock–Varadhan theorem does not directly apply. In fact, uniqueness in law also fails for $\alpha \in (0, 1/2)$ with initial condition $x_0 = 0$, since both the zero solution and the non-trivial solution define different laws on path space.

---

**Exercise 4.** State the conditions of the Stroock–Varadhan theorem. For each condition (bounded measurable $b$, bounded continuous $a$, uniform ellipticity), give a concrete one-dimensional example where the condition is violated and describe what goes wrong (non-existence, non-uniqueness, or both).

??? success "Solution to Exercise 4"
    The Stroock–Varadhan theorem requires:

    1. $b$ is **bounded and measurable**
    2. $a$ is **bounded and continuous**
    3. $a$ is **uniformly elliptic**: $\xi^\top a(x)\xi \ge \lambda|\xi|^2$ for all $x, \xi$ and some $\lambda > 0$

    **Violation of bounded measurable $b$:** Take $d = 1$, $b(x) = x^2$, $a(x) = 1$. The drift is unbounded. The SDE $\mathrm{d}X_t = X_t^2\,\mathrm{d}t + \mathrm{d}W_t$ can lead to **finite-time explosion** (the deterministic ODE $\dot{x} = x^2$ blows up in finite time, and for small noise the stochastic solution can also explode). Non-existence of a global solution occurs.

    **Violation of continuity of $a$:** Take $d = 1$, $b = 0$, $a(x) = \mathbf{1}_{x \ge 0} + 2\cdot\mathbf{1}_{x < 0}$ (discontinuous at $x = 0$). With a discontinuous diffusion coefficient $\sigma(x) = \sqrt{a(x)}$, the martingale problem may have **multiple solutions** because paths crossing $x = 0$ can have different local behaviors depending on how the discontinuity is resolved.

    **Violation of uniform ellipticity:** Take $d = 1$, $b = 0$, $a(x) = x^2$ (so $\sigma(x) = |x|$). The SDE is $\mathrm{d}X_t = |X_t|\,\mathrm{d}W_t$. At $x = 0$, the diffusion coefficient vanishes. Both $X \equiv 0$ and non-trivial solutions exist from $X_0 = 0$, so **uniqueness fails** (non-uniqueness of solutions to the martingale problem).

---

**Exercise 5.** Show that if $X_t$ is a strong solution to the SDE $\mathrm{d}X_t^i = b^i(X_t)\,\mathrm{d}t + \sigma^{i\alpha}(X_t)\,\mathrm{d}W_t^\alpha$ and $f \in C_c^\infty(\mathbb{R}^d)$, then the stochastic integral

$$
\int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha
$$

is a true martingale (not merely a local martingale). What integrability condition on $\nabla f$ and $\sigma$ is used?

??? success "Solution to Exercise 5"
    Given: $X$ solves the SDE, and $f \in C_c^\infty(\mathbb{R}^d)$. The stochastic integral is

    $$
    N_t := \int_0^t \partial_i f(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha
    $$

    By the Itô isometry, $N_t$ is a true $L^2$-martingale if

    $$
    \mathbb{E}\!\int_0^t \sum_{i=1}^d \sum_{\alpha=1}^m |\partial_i f(X_s)|^2\,|\sigma^{i\alpha}(X_s)|^2\,\mathrm{d}s < \infty
    $$

    Since $f \in C_c^\infty(\mathbb{R}^d)$, the gradient $\nabla f$ has compact support: there exists $R > 0$ such that $\partial_i f(x) = 0$ for $|x| > R$. Therefore

    $$
    |\partial_i f(X_s)|^2\,|\sigma^{i\alpha}(X_s)|^2 \le \|\nabla f\|_\infty^2 \cdot \sup_{|x| \le R} |\sigma(x)|^2
    $$

    which is a finite constant (since $\sigma$ is continuous and hence bounded on the compact set $\{|x| \le R\}$). Therefore

    $$
    \mathbb{E}\!\int_0^t \sum_{i,\alpha} |\partial_i f(X_s)|^2\,|\sigma^{i\alpha}(X_s)|^2\,\mathrm{d}s \le C^2\,t < \infty
    $$

    where $C = \|\nabla f\|_\infty \cdot \sup_{|x| \le R}|\sigma(x)|$. By the Itô isometry, $N_t$ is square-integrable and hence a true martingale.

    The key integrability condition is: $\nabla f$ is **bounded and compactly supported** (guaranteed by $f \in C_c^\infty$), and $\sigma$ is **locally bounded** (guaranteed by continuity, or more generally by measurability and local boundedness).

---

**Exercise 6.** Explain the relationship between pathwise uniqueness, uniqueness in law, and well-posedness of the martingale problem. State the Yamada–Watanabe theorem and use it to show that pathwise uniqueness implies uniqueness in law but not vice versa. Give a concrete example where uniqueness in law holds but pathwise uniqueness fails.

??? success "Solution to Exercise 6"
    **Pathwise uniqueness:** Two solutions $X, Y$ on the **same** probability space with the **same** Brownian motion $W$ and the same initial condition satisfy $X_t = Y_t$ for all $t \ge 0$ a.s.

    **Uniqueness in law:** Any two solutions of the martingale problem for $(\mathcal{L}, \delta_{x_0})$ — possibly on **different** probability spaces — have the same finite-dimensional distributions.

    **Well-posedness of the martingale problem:** There exists a **unique** probability measure on path space $C([0,\infty);\mathbb{R}^d)$ solving the martingale problem. This is equivalent to uniqueness in law.

    **Yamada–Watanabe theorem:** If the SDE has pathwise uniqueness and a weak solution exists, then a **strong** solution exists and is unique. Consequently, pathwise uniqueness implies uniqueness in law (since all solutions must have the same law as the unique strong solution on any given probability space). The converse is false.

    **Counterexample (uniqueness in law holds, pathwise uniqueness fails):** Consider the SDE $\mathrm{d}X_t = \mathrm{sgn}(X_t)\,\mathrm{d}W_t$ with $X_0 = 0$ in $d = 1$. By Tanaka's formula, if $X_t$ solves this SDE, then $|X_t|$ is a reflecting Brownian motion. The law of $X_t$ is determined: $X_t$ has the same law as a standard Brownian motion (since $\mathrm{d}\langle X \rangle_t = \mathrm{d}t$, Lévy's characterisation gives that $X$ is a BM). So uniqueness in law holds. However, both $X_t = W_t$ and $X_t = -W_t$ solve the SDE on the same probability space (since $\mathrm{sgn}(W_t)\,\mathrm{d}W_t$ and $\mathrm{sgn}(-W_t)\,\mathrm{d}W_t$ both yield Brownian motions), so pathwise uniqueness fails.

---

**Exercise 7.** Let $\mathcal{L}_1$ and $\mathcal{L}_2$ be two generators with the same $a^{ij}$ but different drifts $b_1^i \ne b_2^i$. Suppose both martingale problems are well-posed. Can the two solutions have the same law? Justify your answer by considering the martingale $M_t^f$ for a suitable choice of test function $f$.

??? success "Solution to Exercise 7"
    **No, the two solutions cannot have the same law** (assuming $b_1 \ne b_2$ on a set of positive measure for the law of $X$).

    Choose the test function $f(x) = x^i$ (the $i$-th coordinate function; localisation may be needed as in Exercise 2). Then $\partial_k f = \delta^{ik}$ and $\partial_k\partial_l f = 0$, so

    $$
    \mathcal{L}_1 f(x) = b_1^i(x), \qquad \mathcal{L}_2 f(x) = b_2^i(x)
    $$

    The martingale problem for $\mathcal{L}_1$ requires

    $$
    M_t^{(1)} = X_t^i - X_0^i - \int_0^t b_1^i(X_s)\,\mathrm{d}s
    $$

    to be a martingale, while the martingale problem for $\mathcal{L}_2$ requires

    $$
    M_t^{(2)} = X_t^i - X_0^i - \int_0^t b_2^i(X_s)\,\mathrm{d}s
    $$

    to be a martingale. If the two solutions had the same law $\mathbb{P}$, then both $M^{(1)}$ and $M^{(2)}$ would be $\mathbb{P}$-martingales. Their difference

    $$
    M_t^{(1)} - M_t^{(2)} = \int_0^t \bigl(b_2^i(X_s) - b_1^i(X_s)\bigr)\,\mathrm{d}s
    $$

    would be both a martingale and a process of finite variation. A continuous finite-variation martingale must be constant (by the martingale property, its quadratic variation is zero, and a continuous martingale with zero quadratic variation is a.s. constant). Therefore

    $$
    \int_0^t \bigl(b_2^i(X_s) - b_1^i(X_s)\bigr)\,\mathrm{d}s = 0 \quad \text{for all } t \ge 0, \text{ a.s.}
    $$

    This implies $b_1^i(X_t) = b_2^i(X_t)$ for Lebesgue-a.e. $t$, a.s. If the support of the law of $X_t$ has positive Lebesgue measure (which it does under uniform ellipticity), this forces $b_1^i = b_2^i$ a.e. — contradicting $b_1 \ne b_2$. Hence the two solutions must have different laws.
