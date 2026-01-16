# Multidimensional Itô's Lemma

This section presents Itô's formula for multidimensional diffusions using index notation (Einstein summation convention). This is essential for working with systems of SDEs, multi-asset models, and the rigorous formulation of stochastic calculus in higher dimensions.

---

## Setting

Let $W_t = (W_t^{1}, \ldots, W_t^{m})$ be an $m$-dimensional Brownian motion and $X_t = (X_t^{1}, \ldots, X_t^{d})$ an $\mathbb{R}^d$-valued diffusion solving:

$$
\boxed{
dX_t^{i} = b^{i}(t, X_t)\,dt + \sigma^{i\alpha}(t, X_t)\,dW_t^{\alpha}, \qquad i = 1, \ldots, d, \quad \alpha = 1, \ldots, m
}
$$

**Einstein summation convention**: Repeated indices (one upper, one lower, or both on same level) are summed over their range. Here $\alpha$ is summed from $1$ to $m$.

**Notation**:

- $b^{i}: [0,T] \times \mathbb{R}^d \to \mathbb{R}$ is the $i$-th component of drift
- $\sigma^{i\alpha}: [0,T] \times \mathbb{R}^d \to \mathbb{R}$ is the $(i, \alpha)$ entry of the diffusion matrix
- $d \times m$ matrix $\sigma$ maps $m$-dimensional noise to $d$-dimensional state space

---

## Multidimensional Itô's Lemma

Let $f: [0,T] \times \mathbb{R}^d \to \mathbb{R}$ be $C^{1,2}$ (once differentiable in $t$, twice in $x$). Define $Y_t = f(t, X_t)$.

**Theorem (Multidimensional Itô Formula)**:

$$
\boxed{
df(t, X_t) = \frac{\partial f}{\partial t}(t, X_t)\,dt + \frac{\partial f}{\partial x_i}(t, X_t)\,dX_t^{i} + \frac{1}{2}\frac{\partial^2 f}{\partial x_i \partial x_j}(t, X_t)\,d\langle X^{i}, X^{j}\rangle_t
}
$$

---

## Quadratic Covariation

The quadratic covariation term requires computing $d\langle X^i, X^j \rangle_t$.

Since $dX_t^{i} = b^{i}\,dt + \sigma^{i\alpha}\,dW_t^{\alpha}$, only the Brownian parts contribute to quadratic variation.

Using the fundamental relation:

$$
d\langle W^{\alpha}, W^{\beta} \rangle_t = \delta^{\alpha\beta}\,dt
$$

where $\delta^{\alpha\beta}$ is the Kronecker delta, we obtain:

$$
\boxed{
d\langle X^{i}, X^{j} \rangle_t = \sigma^{i\alpha}(t, X_t)\sigma^{j\alpha}(t, X_t)\,dt
}
$$

**Note**: The repeated index $\alpha$ is summed: $\sigma^{i\alpha}\sigma^{j\alpha} = \sum_{\alpha=1}^{m} \sigma^{i\alpha}\sigma^{j\alpha}$.

---

## Expanded Form

Substituting $dX_t^{i}$ and $d\langle X^i, X^j \rangle_t$ explicitly:

$$
\begin{aligned}
df(t, X_t) &= f_t(t, X_t)\,dt + f_i(t, X_t)\left(b^{i}(t, X_t)\,dt + \sigma^{i\alpha}(t, X_t)\,dW_t^{\alpha}\right) \\
&\quad + \frac{1}{2}f_{ij}(t, X_t)\sigma^{i\alpha}(t, X_t)\sigma^{j\alpha}(t, X_t)\,dt
\end{aligned}
$$

where we use the standard shorthand:

$$
f_t = \frac{\partial f}{\partial t}, \qquad f_i = \frac{\partial f}{\partial x_i}, \qquad f_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}
$$

---

## Standard Form

Collecting $dt$ and $dW$ terms gives the most common form:

$$
\boxed{
df(t, X_t) = \left(f_t + b^{i} f_i + \frac{1}{2}\sigma^{i\alpha}\sigma^{j\alpha} f_{ij}\right)dt + \sigma^{i\alpha} f_i\,dW_t^{\alpha}
}
$$

where all functions are evaluated at $(t, X_t)$.

**In words**:

- **Drift of $f$**: Time derivative + advection by drift + Itô correction from diffusion
- **Diffusion of $f$**: Gradient dotted with diffusion matrix

---

## The Diffusion Matrix

Define the **diffusion matrix** (or **variance matrix**):

$$
a^{ij}(t, x) := \sigma^{i\alpha}(t, x)\sigma^{j\alpha}(t, x) = (\sigma\sigma^T)^{ij}
$$

This is a $d \times d$ symmetric non-negative definite matrix.

**Properties**:

- $a^{ij} = a^{ji}$ (symmetric)
- $\xi_i a^{ij} \xi_j \geq 0$ for all $\xi \in \mathbb{R}^d$ (non-negative definite)
- If $\sigma$ has full row rank, $a$ is positive definite (ellipticity)

---

## The Infinitesimal Generator

The **infinitesimal generator** $\mathcal{L}$ of the diffusion $X_t$ is:

$$
\boxed{
(\mathcal{L}f)(t, x) = b^{i}(t, x)\frac{\partial f}{\partial x_i}(t, x) + \frac{1}{2}a^{ij}(t, x)\frac{\partial^2 f}{\partial x_i \partial x_j}(t, x)
}
$$

This allows Itô's formula to be written compactly as:

$$
\boxed{
df(t, X_t) = \left(f_t + \mathcal{L}f\right)(t, X_t)\,dt + \frac{\partial f}{\partial x_i}(t, X_t)\sigma^{i\alpha}(t, X_t)\,dW_t^{\alpha}
}
$$

---

## Vector-Valued Functions

For $f: [0,T] \times \mathbb{R}^d \to \mathbb{R}^k$ with components $f^r$ ($r = 1, \ldots, k$), apply the scalar formula componentwise:

$$
\boxed{
df^{r}(t, X_t) = \left(\frac{\partial f^{r}}{\partial t} + b^{i}\frac{\partial f^{r}}{\partial x_i} + \frac{1}{2}a^{ij}\frac{\partial^2 f^{r}}{\partial x_i \partial x_j}\right)dt + \sigma^{i\alpha}\frac{\partial f^{r}}{\partial x_i}\,dW_t^{\alpha}
}
$$

---

## Examples

### Example 1: Norm Squared

Let $f(x) = |x|^2 = x_i x_i$ (sum over $i$). Then:

$$
f_i = 2x_i, \qquad f_{ij} = 2\delta_{ij}
$$

Itô's formula gives:

$$
d|X_t|^2 = 2X_t^i\,dX_t^i + \frac{1}{2} \cdot 2\delta_{ij} \cdot d\langle X^i, X^j \rangle_t
$$

$$
= 2X_t^i(b^i\,dt + \sigma^{i\alpha}\,dW_t^\alpha) + a^{ii}\,dt
$$

$$
= (2X_t^i b^i + \text{tr}(a))\,dt + 2X_t^i \sigma^{i\alpha}\,dW_t^\alpha
$$

### Example 2: Inner Product

For two diffusions $X_t$ and $Y_t$, the inner product $\langle X_t, Y_t \rangle = X_t^i Y_t^i$ satisfies:

$$
d(X_t^i Y_t^i) = X_t^i\,dY_t^i + Y_t^i\,dX_t^i + d\langle X^i, Y^i \rangle_t
$$

This is the **multidimensional Itô product rule**.

---

## Box Calculus in Multiple Dimensions

The multiplication rules generalize to:

$$
dW_t^\alpha \cdot dW_t^\beta = \delta^{\alpha\beta}\,dt
$$

$$
dW_t^\alpha \cdot dt = 0
$$

$$
dt \cdot dt = 0
$$

**Multiplication table** for $m = 2$:

$$
\begin{array}{|c|c|c|c|}
\hline
\times & dt & dW^1 & dW^2 \\
\hline
dt & 0 & 0 & 0 \\
\hline
dW^1 & 0 & dt & 0 \\
\hline
dW^2 & 0 & 0 & dt \\
\hline
\end{array}
$$

---

## Integral Form

The integral form of multidimensional Itô's lemma is:

$$
f(t, X_t) = f(0, X_0) + \int_0^t \left(f_s + \mathcal{L}f\right)(s, X_s)\,ds + \int_0^t f_i(s, X_s)\sigma^{i\alpha}(s, X_s)\,dW_s^\alpha
$$

---

## Summary

$$
\boxed{
\begin{aligned}
df &= \left(\frac{\partial f}{\partial t} + b^i \frac{\partial f}{\partial x_i} + \frac{1}{2}a^{ij}\frac{\partial^2 f}{\partial x_i \partial x_j}\right)dt + \sigma^{i\alpha}\frac{\partial f}{\partial x_i}\,dW_t^\alpha \\[1em]
&= (f_t + \mathcal{L}f)\,dt + (\nabla f)^T \sigma\,dW_t
\end{aligned}
}
$$

| Dimension | Itô Correction | Generator |
|-----------|---------------|-----------|
| 1D | $\frac{1}{2}\sigma^2 f_{xx}$ | $\mu f_x + \frac{1}{2}\sigma^2 f_{xx}$ |
| $d$D | $\frac{1}{2}a^{ij}f_{ij}$ | $b^i f_i + \frac{1}{2}a^{ij}f_{ij}$ |

**The multidimensional Itô formula is essential for multi-asset finance, systems of interacting particles, and any application involving coupled stochastic dynamics.**
