# Lipschitz Conditions and Linear Growth

The existence and uniqueness theory for SDEs rests on two analytical conditions:
the **Lipschitz condition** (controlling uniqueness) and the **linear growth condition**
(preventing finite-time explosion). Together they guarantee a unique, globally-defined
strong solution. The constructive proof is given in [Picard Iteration](picard_iteration.md);
the distinction between strong and weak solutions is developed in
[Strong vs Weak Solutions](strong_vs_weak.md).

---

## Setting

Consider the $d$-dimensional SDE driven by an $m$-dimensional Brownian motion
$W_t = (W_t^1, \ldots, W_t^m)$:

$$
dX_t = b(t, X_t)\,dt + \sigma(t, X_t)\,dW_t, \qquad X_0 = x_0 \in \mathbb{R}^d
$$

where $b : [0,T] \times \mathbb{R}^d \to \mathbb{R}^d$ and
$\sigma : [0,T] \times \mathbb{R}^d \to \mathbb{R}^{d \times m}$.

Norms used throughout: $|\cdot|$ is the Euclidean norm on $\mathbb{R}^d$; for
matrices $|\sigma|^2 = \sum_{i,\alpha}(\sigma^{i\alpha})^2$ (Frobenius norm).

---

## The Lipschitz Condition

**Definition.** The coefficients $(b, \sigma)$ satisfy the **global Lipschitz condition**
if there exists $K > 0$ such that for all $t \in [0,T]$ and $x, y \in \mathbb{R}^d$:

$$
\boxed{|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K|x - y|}
$$

**Interpretation.** Lipschitz continuity bounds how rapidly the coefficients can vary
with the state $x$. The drift vector field has a uniformly bounded spatial slope,
and each column of $\sigma$ varies at most proportionally to displacement.

**Why Lipschitz implies uniqueness.** Suppose $X_t$ and $Y_t$ are two solutions with
$X_0 = Y_0 = x_0$. Set $Z_t = X_t - Y_t$. Then:

$$
Z_t = \int_0^t \bigl[b(s,X_s) - b(s,Y_s)\bigr]\,ds
      + \int_0^t \bigl[\sigma(s,X_s) - \sigma(s,Y_s)\bigr]\,dW_s
$$

Using the Lipschitz bound, the Itô isometry, and Doob's maximal inequality one
obtains:

$$
\mathbb{E}\Bigl[\sup_{s \leq t}|Z_s|^2\Bigr] \leq C \int_0^t \mathbb{E}|Z_s|^2\,ds
$$

Gronwall's inequality with $Z_0 = 0$ then gives
$\mathbb{E}[\sup_{s \leq t}|Z_s|^2] = 0$ for all $t$, hence $X_t = Y_t$ a.s.
The full estimates are carried out in [Picard Iteration](picard_iteration.md).

### Examples of Lipschitz coefficients

**Ornstein–Uhlenbeck** (with mean-reversion speed $\kappa > 0$):

$$
dX_t = -\kappa X_t\,dt + \nu\,dW_t, \qquad K = \kappa.
$$

**Affine SDE** (with scalar coefficients $\alpha, \beta, \gamma, \delta$):

$$
dX_t = (\alpha + \beta X_t)\,dt + (\gamma + \delta X_t)\,dW_t,
\qquad K = |\beta| + |\delta|.
$$

**Smooth, bounded-derivative case.** If $b$ and $\sigma$ are $C^1$ in $x$ with
bounded partial derivatives, the mean value theorem gives global Lipschitz with
$K = \sup_x(|\nabla_x b| + |\nabla_x \sigma|)$.

### A non-Lipschitz example: the CIR model

$$
dX_t = \kappa(\theta - X_t)\,dt + \sigma\sqrt{X_t}\,dW_t
$$

The diffusion coefficient $\sigma\sqrt{x}$ fails global Lipschitz at $x = 0$.
Taking $y = 0$ and letting $x \to 0^+$:

$$
\frac{|\sqrt{x} - \sqrt{0}|}{|x - 0|} = \frac{1}{\sqrt{x}} \to +\infty.
$$

So no single constant $K$ bounds the ratio $|\sigma(x)-\sigma(y)|/|x-y|$ near
the origin. Uniqueness here requires the Yamada–Watanabe condition; see below.

---

## The Linear Growth Condition

**Definition.** The coefficients satisfy the **linear growth condition** if there
exists $K > 0$ such that for all $t \in [0,T]$ and $x \in \mathbb{R}^d$:

$$
\boxed{|b(t,x)|^2 + |\sigma(t,x)|^2 \leq K^2(1 + |x|^2)}
$$

Equivalently, $|b(t,x)| + |\sigma(t,x)| \leq K(1 + |x|)$.

**Why linear growth prevents explosion.** Compare the ODE $\dot{x} = x^p$:

- $p > 1$: solution explodes at finite time $t^* = \tfrac{1}{(p-1)x_0^{p-1}}$.
- $p = 1$: solution $x(t) = x_0 e^t$ is finite for all $t < \infty$.

Linear growth keeps the SDE in the $p = 1$ regime, yielding the a-priori bound:

$$
\mathbb{E}\Bigl[\sup_{0 \leq t \leq T}|X_t|^2\Bigr] \leq C(T)(1 + |x_0|^2)
$$

for a constant $C(T)$ that is finite for each finite $T$.

### Examples

| Coefficient | Linear growth? | Note |
|---|---|---|
| $b(x) = \sin x$ | ✓ | bounded |
| $b(x) = \kappa(\theta - x)$ | ✓ | affine |
| $\sigma(x) = \sqrt{x},\ x \geq 0$ | ✓ | sublinear |
| $b(x) = x^2$ | ✗ | may explode |
| $\sigma(x) = e^x$ | ✗ | may explode |

---

## The Main Existence and Uniqueness Theorem

**Theorem (Itô).** Let $b$ and $\sigma$ be measurable and satisfy the global
Lipschitz and linear growth conditions with constant $K$. Then for any
$\mathcal{F}_0$-measurable initial condition $X_0 = x_0 \in \mathbb{R}^d$:

$$
\boxed{\text{There exists a unique strong solution } X_t \in C([0,T],\mathbb{R}^d)\ \text{a.s.}}
$$

The solution satisfies the moment bound:

$$
\mathbb{E}\Bigl[\sup_{0 \leq t \leq T}|X_t|^2\Bigr] \leq C(1+|x_0|^2)e^{CT}
$$

for a constant $C$ depending only on $K$ and dimension.

!!! note "Lipschitz implies linear growth"
    Global Lipschitz implies linear growth with the same constant $K$. Indeed,
    $|b(t,x)| \leq |b(t,0)| + K|x|$, and the theorem assumes
    $\sup_{t \in [0,T]}|b(t,0)| < \infty$ (satisfied whenever $b$ is measurable
    and bounded at $x=0$, e.g. if $b$ is continuous). The two conditions are
    listed separately only to highlight their distinct roles: Lipschitz controls
    *uniqueness*, linear growth controls *non-explosion*.

The proof constructs the solution via Picard iteration; see
[Picard Iteration](picard_iteration.md) for the full argument.

---

## Local Lipschitz Conditions

**Definition.** The coefficients are **locally Lipschitz** if for every $R > 0$
there exists $K_R > 0$ such that

$$
|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K_R|x-y|
\quad \text{for all } |x|, |y| \leq R.
$$

Under local Lipschitz alone, a unique continuous solution exists up to the
**explosion time** (since $X_t$ is continuous, each $\tau_n$ is a stopping time):

$$
\tau_\infty = \lim_{n \to \infty} \tau_n, \qquad \tau_n = \inf\{t \geq 0 : |X_t| \geq n\}.
$$

Adding the linear growth condition forces $\mathbb{P}(\tau_\infty = \infty) = 1$,
recovering a global solution.

---

## Beyond Lipschitz: Yamada–Watanabe Conditions

For one-dimensional SDEs, the diffusion coefficient need not be Lipschitz for
pathwise uniqueness to hold.

**Theorem (Yamada–Watanabe).** Consider $dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t$
on $\mathbb{R}$. Pathwise uniqueness holds if:

1. $b$ is globally Lipschitz: $|b(x) - b(y)| \leq K|x-y|$.
2. $\sigma$ satisfies $|\sigma(x) - \sigma(y)| \leq \rho(|x-y|)$ for a function
   $\rho : (0,\infty) \to (0,\infty)$ with

$$
\int_0^\epsilon \frac{du}{\rho^2(u)} = +\infty \quad \text{for every } \epsilon > 0.
$$

The divergence is required at $0$: for any fixed $\epsilon > 0$ the tail integral
$\int_\epsilon^1 \rho^{-2}(u)\,du$ is finite whenever $\rho$ is bounded away from
zero on $[\epsilon, 1]$, so the condition is purely a constraint on the behaviour
of $\rho$ near $u = 0$.

**CIR application.** Take $\sigma(x) = \sigma_0\sqrt{x}$ for $x \geq 0$. To bound
$|\sigma(x) - \sigma(y)|$, use the elementary inequality $|\sqrt{x} - \sqrt{y}|
\leq \sqrt{|x-y|}$ (which follows from $(\sqrt{x}-\sqrt{y})^2 \leq |x-y|$ when
$x, y \geq 0$), giving $|\sigma(x) - \sigma(y)| \leq \sigma_0|x - y|^{1/2}$, so
$\rho(u) = \sigma_0 u^{1/2}$. Then:

$$
\int_0^\epsilon \frac{du}{\sigma_0^2\,u} = +\infty. \quad \checkmark
$$

Hence the CIR model has a pathwise unique solution despite non-Lipschitz diffusion.
The relationship between pathwise uniqueness and strong existence is detailed in
[Strong vs Weak Solutions](strong_vs_weak.md).

---

## Summary

$$
\boxed{\text{Lipschitz} + \text{Linear Growth} \implies \text{Unique Global Strong Solution}}
$$

| Condition | Role | Formula |
|---|---|---|
| **Global Lipschitz** | Uniqueness | $|b(x)-b(y)|+|\sigma(x)-\sigma(y)|\leq K|x-y|$ |
| **Linear growth** | No explosion | $|b(x)|^2+|\sigma(x)|^2\leq K^2(1+|x|^2)$ |
| **Local Lipschitz** | Local uniqueness | Lipschitz on each ball $|x|,|y|\leq R$ |
| **Yamada–Watanabe** | Uniqueness for $|\sigma|\sim|x|^\alpha$, $\alpha\geq\tfrac{1}{2}$ | $\int_0^\epsilon \rho^{-2}(u)\,du=\infty$ |

**Standard models at a glance:**

- GBM, Vasicek, OU: global Lipschitz + linear growth ✓
- CIR: linear growth + Yamada–Watanabe ✓
- $dX = X^2\,dt + dW$: linear growth violated, may explode ✗
