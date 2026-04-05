# Multidimensional Itô's Lemma

The one-dimensional Itô formula (see [Itô's Lemma](ito_lemma.md)) extends naturally to systems of SDEs driven by multiple Brownian motions. This page presents the multidimensional version using index notation, derives the quadratic covariation structure, and works through concrete examples.

## 1. Setting

Let $W_t = (W_t^{1}, \ldots, W_t^{m})$ be an $m$-dimensional Brownian motion and $X_t = (X_t^{1}, \ldots, X_t^{d})$ an $\mathbb{R}^d$-valued diffusion solving:

$$
dX_t^{i} = b^{i}(t, X_t)\,dt + \sigma^{i\alpha}(t, X_t)\,dW_t^{\alpha}, \qquad i = 1, \ldots, d, \quad \alpha = 1, \ldots, m
$$

**Notation**:

- $b^{i}: [0,T] \times \mathbb{R}^d \to \mathbb{R}$ is the $i$-th drift component
- $\sigma^{i\alpha}: [0,T] \times \mathbb{R}^d \to \mathbb{R}$ is the $(i, \alpha)$ entry of the $d \times m$ diffusion matrix
- **Einstein summation convention**: repeated indices are summed over their range. For example, in $\sigma^{i\alpha} dW_t^{\alpha}$, the index $\alpha$ is summed from $1$ to $m$.

!!! warning "Index notation convention"

    This page uses **all superscripts** for index notation, for consistency with the SDE structure above. This deviates from the standard tensor convention (which sums a lower index against an upper index). Here, **any repeated index — regardless of height — denotes summation**. Readers familiar with standard tensor notation should note this difference.

## 2. The Theorem

Let $f: [0,T] \times \mathbb{R}^d \to \mathbb{R}$ be $C^{1,2}$ (once differentiable in $t$, twice in $x$). Write

$$
f_t = \frac{\partial f}{\partial t}, \qquad f_i = \frac{\partial f}{\partial x^i}, \qquad f_{ij} = \frac{\partial^2 f}{\partial x^i \partial x^j}
$$

**Theorem (Multidimensional Itô Formula)**. The process $Y_t = f(t, X_t)$ satisfies:

$$
\boxed{
df(t, X_t) = f_t\,dt + f_i\,dX_t^{i} + \frac{1}{2} f_{ij}\,d\langle X^{i}, X^{j}\rangle_t
}
$$

where all partial derivatives are evaluated at $(t, X_t)$.

**Quadratic covariation.** Since $dX_t^{i} = b^{i}\,dt + \sigma^{i\alpha}\,dW_t^{\alpha}$, only the Brownian parts contribute. The key rule for $m$-dimensional Brownian motion is

$$
d\langle W^{\alpha}, W^{\beta} \rangle_t = \delta^{\alpha\beta}\,dt
$$

which reflects two facts: independent Brownian components ($\alpha \neq \beta$) have zero covariation, while the same component satisfies $(dW^\alpha)^2 = dt$ — see [From Taylor to Itô](from_taylor_to_ito.md) for the 1D derivation. Applying this:

$$
\boxed{
d\langle X^{i}, X^{j} \rangle_t = \sigma^{i\alpha}(t, X_t)\,\sigma^{j\alpha}(t, X_t)\,dt =: a^{ij}(t, X_t)\,dt
}
$$

where $\delta^{\alpha\beta}$ is the Kronecker delta and the repeated index $\alpha$ is summed from $1$ to $m$.

**The diffusion matrix** $a^{ij} := \sigma^{i\alpha}\sigma^{j\alpha} = (\sigma\sigma^T)^{ij}$ is a $d \times d$ symmetric positive-semidefinite matrix. Non-negative definiteness follows from

$$
\sum_{i,j} \xi^i a^{ij} \xi^j = \sum_\alpha \left(\sum_i \sigma^{i\alpha}\xi^i\right)^2 = |\sigma^T\xi|^2 \geq 0
$$

for all $\xi \in \mathbb{R}^d$. It is positive definite (elliptic) if and only if $\sigma$ has full row rank.

## 3. Expanded and Standard Forms

Substituting $dX_t^{i}$ and $d\langle X^i, X^j \rangle_t$ explicitly:

$$
df(t, X_t) = f_t\,dt + f_i\!\left(b^{i}\,dt + \sigma^{i\alpha}\,dW_t^{\alpha}\right) + \frac{1}{2}f_{ij}\,\sigma^{i\alpha}\sigma^{j\alpha}\,dt
$$

Collecting $dt$ and $dW$ terms gives the **standard form**:

$$
\boxed{
df(t, X_t) = \left(f_t + b^{i} f_i + \frac{1}{2}a^{ij} f_{ij}\right)dt + \sigma^{i\alpha} f_i\,dW_t^{\alpha}
}
$$

where all functions are evaluated at $(t, X_t)$.

- **Drift of $f$**: time derivative + advection by drift + Itô correction from curvature
- **Stochastic part of $f$**: $f_i \sigma^{i\alpha} dW_t^{\alpha}$, i.e., the gradient of $f$ contracted with the diffusion matrix $\sigma$, acting on $dW_t$

The **infinitesimal generator** $\mathcal{L}$ packages the *spatial* part of the drift (excluding $f_t$):

$$
(\mathcal{L}f)(t, x) := b^{i}(t, x)\,f_i(t,x) + \frac{1}{2}a^{ij}(t, x)\,f_{ij}(t,x)
$$

so the standard form condenses to:

$$
df(t, X_t) = \bigl(f_t + \mathcal{L}f\bigr)(t, X_t)\,dt + f_i(t, X_t)\,\sigma^{i\alpha}(t, X_t)\,dW_t^{\alpha}
$$

Note that $\mathcal{L}$ acts on spatial variables only and does not include $f_t$; the full drift is $f_t + \mathcal{L}f$. The generator $\mathcal{L}$ governs the expected infinitesimal evolution of $f(t, X_t)$; it appears in the Kolmogorov forward and backward equations and the Feynman–Kac formula — see Kolmogorov Equations and Feynman–Kac Formula.

## 4. Examples

### Example 1: Norm Squared

Let $f(x) = |x|^2 = \sum_i (x^i)^2$. Then $f_t = 0$, $f_i = 2x^i$, $f_{ij} = 2\delta^{ij}$ (where $\delta^{ij} = 1$ if $i = j$ and $0$ otherwise). The standard form gives:

$$
d|X_t|^2 = \left(2\sum_i X_t^i b^i + \sum_i a^{ii}\right)dt + 2\sum_{i,\alpha} X_t^i \sigma^{i\alpha}\,dW_t^\alpha
$$

where $\sum_i a^{ii} = \operatorname{tr}(a) = \operatorname{tr}(\sigma\sigma^T)$ is the sum of all diffusion variances. The Itô correction inflates the drift by $\operatorname{tr}(\sigma\sigma^T)$ relative to the classical chain rule.

### Example 2: Inner Product of Two Diffusions

Let $X_t$ and $Y_t$ be two $\mathbb{R}^d$-valued diffusions with SDEs

$$
dX_t^i = b_X^i\,dt + \sigma_X^{i\alpha}\,dW_t^\alpha, \qquad dY_t^i = b_Y^i\,dt + \sigma_Y^{i\alpha}\,dW_t^\alpha
$$

driven by the same $m$-dimensional Brownian motion. To apply Itô's formula, form the joint process $Z_t = (X_t, Y_t) \in \mathbb{R}^{2d}$ and apply the multidimensional formula to $f(x, y) = \sum_i x^i y^i$.

The gradient of $f$ with respect to $(x,y)$ is the vector of partial derivatives $(\partial f/\partial x^i, \partial f/\partial y^i)_{i=1}^d = (y^i, x^i)_{i=1}^d$. That is, for each fixed $i$: $\partial f/\partial x^i = y^i$ and $\partial f/\partial y^i = x^i$. The only non-zero second-order cross terms are $\partial^2 f/\partial x^i \partial y^i = 1$ for each $i$. Substituting into the formula yields the product rule:

$$
d\!\left(\sum_i X_t^i Y_t^i\right) = \sum_i Y_t^i\,dX_t^i + \sum_i X_t^i\,dY_t^i + \sum_i d\langle X^i, Y^i \rangle_t
$$

Each covariation term evaluates to $d\langle X^i, Y^i \rangle_t = \sum_\alpha \sigma_X^{i\alpha}\sigma_Y^{i\alpha}\,dt$, so summing over $i$:

$$
\boxed{
d\!\left(\sum_i X_t^i Y_t^i\right) = \left(\sum_i Y_t^i b_X^i + \sum_i X_t^i b_Y^i + \sum_{i,\alpha}\sigma_X^{i\alpha}\sigma_Y^{i\alpha}\right)dt + \sum_{i,\alpha}\left(Y_t^i \sigma_X^{i\alpha} + X_t^i \sigma_Y^{i\alpha}\right)dW_t^\alpha
}
$$

This is the **multidimensional Itô product rule**. When $X = Y$ it reduces to Example 1.

## 5. Summary

$$
\boxed{
df(t, X_t)
= \left(f_t + b^i f_i + \tfrac{1}{2}a^{ij}f_{ij}\right)dt
+ \sigma^{i\alpha} f_i\,dW_t^\alpha
}
$$

| | 1D | $d$-dimensional |
|---|---|---|
| SDE | $dX = \mu\,dt + \sigma\,dW$ | $dX^i = b^i\,dt + \sigma^{i\alpha}\,dW^\alpha$ |
| Itô correction | $\tfrac{1}{2}\sigma^2 f_{xx}$ | $\tfrac{1}{2}a^{ij}f_{ij}$, $\;a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}$ |
| Generator $\mathcal{L}$ (spatial only) | $\mu f_x + \tfrac{1}{2}\sigma^2 f_{xx}$ | $b^i f_i + \tfrac{1}{2}a^{ij}f_{ij}$ |
| Full drift of $f$ | $f_t + \mu f_x + \tfrac{1}{2}\sigma^2 f_{xx}$ | $f_t + b^i f_i + \tfrac{1}{2}a^{ij}f_{ij}$ |

The 1D formula is recovered by setting $d = m = 1$, $b^1 = \mu$, $\sigma^{11} = \sigma$, so $a^{11} = \sigma^2$.

---

## Exercises

**Exercise 1.** Let $d = 2$, $m = 2$, with $dX_t^1 = \sigma_1\,dW_t^1$ and $dX_t^2 = \sigma_2\,dW_t^2$ (two independent Brownian motions, no drift). Compute the diffusion matrix $a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}$ and verify that it is diagonal.

??? success "Solution to Exercise 1"
    The diffusion matrix is $\sigma = \begin{pmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{pmatrix}$ (each component driven by its own independent Brownian motion). The diffusion matrix $a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}$ is computed by summing over $\alpha = 1, 2$:

    - $a^{11} = \sigma^{11}\sigma^{11} + \sigma^{12}\sigma^{12} = \sigma_1^2 + 0 = \sigma_1^2$
    - $a^{12} = \sigma^{11}\sigma^{21} + \sigma^{12}\sigma^{22} = 0 + 0 = 0$
    - $a^{21} = \sigma^{21}\sigma^{11} + \sigma^{22}\sigma^{12} = 0 + 0 = 0$
    - $a^{22} = \sigma^{21}\sigma^{21} + \sigma^{22}\sigma^{22} = 0 + \sigma_2^2 = \sigma_2^2$

    So $a = \begin{pmatrix} \sigma_1^2 & 0 \\ 0 & \sigma_2^2 \end{pmatrix}$, which is diagonal. This confirms that independent Brownian drivers produce a diagonal diffusion matrix — the two components have no quadratic covariation.

---

**Exercise 2.** Let $f(x^1, x^2) = x^1 x^2$ with the same setup as Exercise 1. Apply the multidimensional Itô formula to compute $d(X_t^1 X_t^2)$. Show that the Itô correction term vanishes because the two processes are driven by independent Brownian motions.

??? success "Solution to Exercise 2"
    For $f(x^1, x^2) = x^1 x^2$: $f_1 = x^2$, $f_2 = x^1$, $f_{11} = 0$, $f_{22} = 0$, $f_{12} = f_{21} = 1$. From Exercise 1, $a^{ij}$ is diagonal with $a^{12} = 0$. No drift ($b^i = 0$). The Itô correction is:

    $$
    \frac{1}{2}a^{ij}f_{ij} = \frac{1}{2}(a^{11} \cdot 0 + a^{12} \cdot 1 + a^{21} \cdot 1 + a^{22} \cdot 0) = \frac{1}{2}(0 + 0 + 0 + 0) = 0
    $$

    The multidimensional Itô formula gives:

    $$
    d(X_t^1 X_t^2) = X_t^2\,dX_t^1 + X_t^1\,dX_t^2 + 0 = \sigma_1 X_t^2\,dW_t^1 + \sigma_2 X_t^1\,dW_t^2
    $$

    The Itô correction vanishes because $d\langle X^1, X^2\rangle_t = 0$ — the two processes are driven by independent Brownian motions.

---

**Exercise 3.** Now suppose $dX_t^1 = \sigma_1\,dW_t^1$ and $dX_t^2 = \sigma_2\,dW_t^1$ (both driven by the **same** Brownian motion). Compute the diffusion matrix $a^{ij}$ and the quadratic covariation $d\langle X^1, X^2 \rangle_t$. Apply the multidimensional Itô formula to $f(x^1, x^2) = x^1 x^2$ and identify the Itô correction.

??? success "Solution to Exercise 3"
    Now $\sigma = \begin{pmatrix} \sigma_1 \\ \sigma_2 \end{pmatrix}$ (a $2 \times 1$ matrix, since $m = 1$). The diffusion matrix is:

    $$
    a^{ij} = \sigma^{i1}\sigma^{j1} = \begin{pmatrix} \sigma_1^2 & \sigma_1\sigma_2 \\ \sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}
    $$

    The quadratic covariation is $d\langle X^1, X^2\rangle_t = \sigma_1\sigma_2\,dt$.

    For $f(x^1, x^2) = x^1 x^2$: $f_{12} = 1$, all other second derivatives are zero. The Itô correction is:

    $$
    \frac{1}{2}a^{ij}f_{ij} = \frac{1}{2}(0 + \sigma_1\sigma_2 \cdot 1 + \sigma_1\sigma_2 \cdot 1 + 0) = \sigma_1\sigma_2
    $$

    The full formula gives:

    $$
    d(X_t^1 X_t^2) = X_t^2 \sigma_1\,dW_t + X_t^1 \sigma_2\,dW_t + \sigma_1\sigma_2\,dt
    $$

    $$
    = \sigma_1\sigma_2\,dt + (\sigma_1 X_t^2 + \sigma_2 X_t^1)\,dW_t
    $$

    The Itô correction $\sigma_1\sigma_2\,dt$ is non-zero because both processes share the same Brownian motion.

---

**Exercise 4.** Let $X_t = (X_t^1, X_t^2)$ be a 2D process with

$$
dX_t^1 = dW_t^1, \qquad dX_t^2 = dW_t^1 + dW_t^2
$$

where $W^1$ and $W^2$ are independent. Compute the $2 \times 2$ diffusion matrix $a^{ij} = (\sigma\sigma^T)^{ij}$ and verify that it is positive definite.

??? success "Solution to Exercise 4"
    The diffusion matrix is $\sigma = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ (rows correspond to $X^1, X^2$; columns to $W^1, W^2$). The diffusion matrix is:

    $$
    a = \sigma\sigma^T = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}
    $$

    To verify positive definiteness, check that both eigenvalues are positive. The determinant is $1 \cdot 2 - 1 \cdot 1 = 1 > 0$ and the trace is $3 > 0$, so both eigenvalues are positive. Alternatively, $\det(a) = 1 > 0$ and $a^{11} = 1 > 0$, confirming positive definiteness by Sylvester's criterion.

---

**Exercise 5.** For the setting in Example 1 (norm squared), let $d = 3$, $m = 3$, with $dX_t^i = \mu^i\,dt + dW_t^i$ for $i = 1, 2, 3$ (independent standard Brownian motions with constant drifts). Compute $d|X_t|^2$ explicitly. What is the Itô correction term $\operatorname{tr}(\sigma\sigma^T)$ in this case?

??? success "Solution to Exercise 5"
    With $dX_t^i = \mu^i\,dt + dW_t^i$ for $i = 1, 2, 3$, the diffusion matrix is $\sigma = I_{3\times 3}$ (the identity), so $a = \sigma\sigma^T = I$. For $f(x) = |x|^2 = (x^1)^2 + (x^2)^2 + (x^3)^2$:

    - $f_i = 2x^i$, $f_{ij} = 2\delta^{ij}$

    The Itô correction is $\frac{1}{2}a^{ij}f_{ij} = \frac{1}{2}\delta^{ij} \cdot 2\delta^{ij} = \sum_i 1 = 3$. That is, $\operatorname{tr}(\sigma\sigma^T) = \operatorname{tr}(I) = 3$.

    The full formula:

    $$
    d|X_t|^2 = \left(2\sum_{i=1}^3 X_t^i \mu^i + 3\right)dt + 2\sum_{i=1}^3 X_t^i\,dW_t^i
    $$

    The Itô correction contributes $+3\,dt$ to the drift, reflecting the fact that three independent Brownian motions each contribute $+1\,dt$ through their quadratic variation.

---

**Exercise 6.** Consider a 2D geometric Brownian motion:

$$
dS_t^1 = \mu_1 S_t^1\,dt + \sigma_1 S_t^1\,dW_t^1, \qquad dS_t^2 = \mu_2 S_t^2\,dt + \sigma_2 S_t^2\,dW_t^2
$$

with independent Brownian motions. Apply the multidimensional Itô formula to $f(x^1, x^2) = \log(x^1) + \log(x^2) = \log(x^1 x^2)$ to derive the SDE for $\log(S_t^1 S_t^2)$.

??? success "Solution to Exercise 6"
    For $f(x^1, x^2) = \log(x^1) + \log(x^2)$:

    - $f_1 = 1/x^1$, $f_2 = 1/x^2$
    - $f_{11} = -1/(x^1)^2$, $f_{22} = -1/(x^2)^2$, $f_{12} = 0$

    Since $W^1$ and $W^2$ are independent, $a^{12} = 0$, $a^{11} = \sigma_1^2(S_t^1)^2$, $a^{22} = \sigma_2^2(S_t^2)^2$. The drift of $S^i$ is $\mu_i S_t^i$. Applying the formula:

    $$
    d(\log(S_t^1 S_t^2)) = \left(\frac{\mu_1 S_t^1}{S_t^1} + \frac{\mu_2 S_t^2}{S_t^2} + \frac{1}{2}\left(-\frac{\sigma_1^2(S_t^1)^2}{(S_t^1)^2} - \frac{\sigma_2^2(S_t^2)^2}{(S_t^2)^2}\right)\right)dt + \frac{\sigma_1 S_t^1}{S_t^1}\,dW_t^1 + \frac{\sigma_2 S_t^2}{S_t^2}\,dW_t^2
    $$

    Simplifying:

    $$
    d(\log(S_t^1 S_t^2)) = \left(\mu_1 + \mu_2 - \frac{\sigma_1^2}{2} - \frac{\sigma_2^2}{2}\right)dt + \sigma_1\,dW_t^1 + \sigma_2\,dW_t^2
    $$

    This is the sum of the individual log-dynamics: $d\log(S_t^1) + d\log(S_t^2)$, each with its own convexity adjustment $-\sigma_i^2/2$.

---

**Exercise 7.** The infinitesimal generator is defined as $(\mathcal{L}f)(t, x) = b^i f_i + \frac{1}{2}a^{ij}f_{ij}$. For $d = 2$, $m = 1$, with $dX_t^1 = \sigma_1\,dW_t$ and $dX_t^2 = \sigma_2\,dW_t$ (same Brownian motion, no drift), compute $\mathcal{L}f$ for $f(x^1, x^2) = (x^1)^2 + (x^2)^2$. Verify your answer by applying the multidimensional Itô formula directly and reading off the $dt$ coefficient.

??? success "Solution to Exercise 7"
    With $d = 2$, $m = 1$, $b^i = 0$, $\sigma^{11} = \sigma_1$, $\sigma^{21} = \sigma_2$:

    $$
    a^{ij} = \sigma^{i1}\sigma^{j1} = \begin{pmatrix} \sigma_1^2 & \sigma_1\sigma_2 \\ \sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}
    $$

    For $f(x^1, x^2) = (x^1)^2 + (x^2)^2$: $f_1 = 2x^1$, $f_2 = 2x^2$, $f_{11} = 2$, $f_{22} = 2$, $f_{12} = 0$. The generator is:

    $$
    \mathcal{L}f = b^i f_i + \frac{1}{2}a^{ij}f_{ij} = 0 + \frac{1}{2}(\sigma_1^2 \cdot 2 + \sigma_1\sigma_2 \cdot 0 + \sigma_1\sigma_2 \cdot 0 + \sigma_2^2 \cdot 2) = \sigma_1^2 + \sigma_2^2
    $$

    Verification via the multidimensional Itô formula. Since $f_t = 0$, the $dt$ coefficient is $f_t + \mathcal{L}f = \sigma_1^2 + \sigma_2^2$, and the $dW_t$ coefficient is:

    $$
    \sigma^{i1}f_i = \sigma_1 \cdot 2X_t^1 + \sigma_2 \cdot 2X_t^2
    $$

    So:

    $$
    d((X_t^1)^2 + (X_t^2)^2) = (\sigma_1^2 + \sigma_2^2)\,dt + 2(\sigma_1 X_t^1 + \sigma_2 X_t^2)\,dW_t
    $$

    The $dt$ coefficient $\sigma_1^2 + \sigma_2^2$ matches $\mathcal{L}f$, confirming the computation.
