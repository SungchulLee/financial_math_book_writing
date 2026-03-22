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
