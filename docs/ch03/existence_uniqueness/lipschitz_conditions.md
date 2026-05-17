# Lipschitz Conditions and Linear Growth

This file states the assumptions under which SDEs have a unique global strong solution: the **Lipschitz condition** (controlling uniqueness) and the **linear growth condition** (preventing finite-time explosion). The construction is given in the next section.

!!! tip "Toy mechanism: two ODEs, two failure modes"
    Both conditions are already visible in deterministic ODEs. Take $\dot x = x^p$ on $\mathbb{R}_+$:

    - $p = 1/2$: two solutions start from $x_0 = 0$ — the trivial one and $x(t) = t^2/4$. *Uniqueness fails* because $x^{1/2}$ is not Lipschitz at $0$.
    - $p = 2$: the solution $x(t) = x_0/(1 - x_0 t)$ blows up at $t^* = 1/x_0$. *Existence fails globally* because $x^2$ grows faster than linearly.
    - $p = 1$: $x(t) = x_0 e^t$ — unique and finite for all $t$. Both pathologies disappear.

    Lipschitz is the diffusion-process analogue of "ratio $|f(x) - f(y)|/|x - y|$ is bounded" — exactly what fails at $0$ in the $p = 1/2$ case. Linear growth is the diffusion analogue of $p = 1$. Everything that follows below — global Lipschitz, linear growth, Yamada–Watanabe, local Lipschitz with explosion times — is one of these two mechanisms generalised to the SDE setting.

---

## Setting

Recall (see [§ Stochastic Differential Equations](../sde/sde.md)): the $d$-dimensional SDE is $dX_t = b(t, X_t)\,dt + \sigma(t, X_t)\,dW_t$ with $X_0 = x_0 \in \mathbb{R}^d$, $b : [0,T] \times \mathbb{R}^d \to \mathbb{R}^d$, $\sigma : [0,T] \times \mathbb{R}^d \to \mathbb{R}^{d \times m}$, and $W_t$ an $m$-dimensional Brownian motion.

Norms used throughout: $|\cdot|$ is the Euclidean norm on $\mathbb{R}^d$; for matrices $|\sigma|^2 = \sum_{i,\alpha}(\sigma^{i\alpha})^2$ (Frobenius norm).

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

**Why Lipschitz implies uniqueness (intuition).** The Lipschitz bound controls how the difference between two candidate solutions can grow; a Gronwall argument then forces the difference to remain zero. The full proof is given in the next section.

### Examples of Lipschitz coefficients

**Ornstein–Uhlenbeck** (with mean-reversion speed $\kappa > 0$):

$$
dX_t = -\kappa X_t\,dt + \nu\,dW_t, \qquad K = \kappa
$$

**Affine SDE** (with scalar coefficients $\alpha, \beta, \gamma, \delta$):

$$
dX_t = (\alpha + \beta X_t)\,dt + (\gamma + \delta X_t)\,dW_t,
\qquad K = |\beta| + |\delta|
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
\frac{|\sqrt{x} - \sqrt{0}|}{|x - 0|} = \frac{1}{\sqrt{x}} \to +\infty
$$

So no single constant $K$ bounds the ratio $|\sigma(x)-\sigma(y)|/|x-y|$ near
the origin. Uniqueness for CIR requires the Yamada–Watanabe condition (below).

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

The construction will be given in the next section.

---

## Local Lipschitz Conditions

**Definition.** The coefficients are **locally Lipschitz** if for every $R > 0$
there exists $K_R > 0$ such that

$$
|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K_R|x-y|
\quad \text{for all } |x|, |y| \leq R
$$

Under local Lipschitz alone, a unique continuous solution exists up to the
**explosion time** (since $X_t$ is continuous, each $\tau_n$ is a stopping time):

$$
\tau_\infty = \lim_{n \to \infty} \tau_n, \qquad \tau_n = \inf\{t \geq 0 : |X_t| \geq n\}
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
\int_0^\epsilon \frac{du}{\rho^2(u)} = +\infty \quad \text{for every } \epsilon > 0
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

Hence the CIR model has a pathwise unique solution despite non-Lipschitz diffusion. The relationship between pathwise uniqueness and strong existence is treated in [§ Strong and Weak Solutions](strong_vs_weak.md).

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

---

## Exercises

**Exercise 1.** Consider the SDE

$$
dX_t = (3 + 2X_t)\,dt + (1 - X_t)\,dW_t
$$

Verify that the coefficients satisfy the global Lipschitz condition and identify the Lipschitz constant $K$.

??? success "Solution to Exercise 1"
    The coefficients are $b(t,x) = 3 + 2x$ and $\sigma(t,x) = 1 - x$. For any $x, y \in \mathbb{R}$:

    $$
    |b(t,x) - b(t,y)| = |2x - 2y| = 2|x - y|
    $$

    $$
    |\sigma(t,x) - \sigma(t,y)| = |(1-x) - (1-y)| = |x - y|
    $$

    Therefore:

    $$
    |b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| = 2|x-y| + |x-y| = 3|x-y|
    $$

    The global Lipschitz condition is satisfied with Lipschitz constant $K = 3$.

---

**Exercise 2.** Determine which of the following diffusion coefficients $\sigma(x)$ satisfy the global Lipschitz condition on $\mathbb{R}$. For those that do, give the Lipschitz constant; for those that do not, explain why.

(a) $\sigma(x) = \sin(x)$

(b) $\sigma(x) = |x|^{2/3}$

(c) $\sigma(x) = \dfrac{x}{1 + |x|}$

(d) $\sigma(x) = x^2$

??? success "Solution to Exercise 2"
    **(a)** $\sigma(x) = \sin(x)$. By the mean value theorem, $|\sin(x) - \sin(y)| \leq |x - y|$ for all $x, y \in \mathbb{R}$, since $|\cos(\xi)| \leq 1$ for all $\xi$. So $\sigma$ is globally Lipschitz with $K = 1$.

    **(b)** $\sigma(x) = |x|^{2/3}$. This is **not** globally Lipschitz. Near the origin, consider $x > 0$ and $y = 0$:

    $$
    \frac{|x^{2/3} - 0|}{|x - 0|} = x^{-1/3} \to +\infty \quad \text{as } x \to 0^+
    $$

    No finite constant $K$ can bound the ratio uniformly.

    **(c)** $\sigma(x) = \dfrac{x}{1 + |x|}$. For any $x, y \in \mathbb{R}$, write $f(x) = x/(1+|x|)$. Since $f'(x) = 1/(1+|x|)^2$ for $x \neq 0$ and $|f'(x)| \leq 1$ everywhere, the mean value theorem gives $|f(x) - f(y)| \leq |x - y|$. So $\sigma$ is globally Lipschitz with $K = 1$.

    **(d)** $\sigma(x) = x^2$. This is **not** globally Lipschitz. For $y = 0$:

    $$
    \frac{|x^2|}{|x|} = |x| \to +\infty \quad \text{as } |x| \to \infty
    $$

    The ratio grows without bound, so no finite Lipschitz constant exists.

---

**Exercise 3.** Let $b(x) = -x^3$ and $\sigma(x) = 1$. Show that $b$ is locally Lipschitz but not globally Lipschitz. Then verify that the linear growth condition fails for $b$. What does this imply about the solution to $dX_t = -X_t^3\,dt + dW_t$?

??? success "Solution to Exercise 3"
    **Locally Lipschitz:** For any $R > 0$ and $|x|, |y| \leq R$:

    $$
    |b(x) - b(y)| = |{-x^3 + y^3}| = |x - y| \cdot |x^2 + xy + y^2| \leq |x-y| \cdot 3R^2
    $$

    so $b$ is Lipschitz on the ball of radius $R$ with constant $K_R = 3R^2$.

    **Not globally Lipschitz:** Taking $y = 0$, the ratio $|b(x) - b(0)|/|x| = x^2 \to \infty$ as $|x| \to \infty$, so no single $K$ works for all $x \in \mathbb{R}$.

    **Linear growth fails:** We need $|b(x)|^2 + |\sigma(x)|^2 \leq K^2(1 + |x|^2)$. Since $|b(x)|^2 = x^6$ and $|\sigma(x)|^2 = 1$:

    $$
    x^6 + 1 \leq K^2(1 + x^2)
    $$

    is impossible for large $|x|$, since the left side grows as $|x|^6$ while the right side grows as $|x|^2$.

    **Implication:** Despite the failure of linear growth, the drift $b(x) = -x^3$ is dissipative (it pushes the solution toward the origin for large $|x|$). Local Lipschitz guarantees a unique local solution, and dissipativity prevents explosion. The solution to $dX_t = -X_t^3\,dt + dW_t$ exists globally and is unique, but this cannot be concluded from the standard existence-uniqueness theorem — a Lyapunov function argument is needed instead.

---

**Exercise 4.** Prove that the global Lipschitz condition implies the linear growth condition. Specifically, show that if

$$
|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K|x - y|
$$

for all $x, y \in \mathbb{R}^d$, and $M := \sup_{t \in [0,T]}\bigl(|b(t,0)| + |\sigma(t,0)|\bigr) < \infty$, then

$$
|b(t,x)| + |\sigma(t,x)| \leq (M + K)(1 + |x|)
$$

??? success "Solution to Exercise 4"
    Let $b$ and $\sigma$ satisfy the global Lipschitz condition. For any $t \in [0,T]$ and $x \in \mathbb{R}^d$, apply the Lipschitz bound with $y = 0$:

    $$
    |b(t,x) - b(t,0)| + |\sigma(t,x) - \sigma(t,0)| \leq K|x - 0| = K|x|
    $$

    By the triangle inequality:

    $$
    |b(t,x)| \leq |b(t,0)| + |b(t,x) - b(t,0)| \leq |b(t,0)| + K|x|
    $$

    $$
    |\sigma(t,x)| \leq |\sigma(t,0)| + |\sigma(t,x) - \sigma(t,0)| \leq |\sigma(t,0)| + K|x|
    $$

    Adding these two inequalities:

    $$
    |b(t,x)| + |\sigma(t,x)| \leq \bigl(|b(t,0)| + |\sigma(t,0)|\bigr) + 2K|x| \leq M + 2K|x|
    $$

    where $M = \sup_{t \in [0,T]}(|b(t,0)| + |\sigma(t,0)|)$. To get the stated form, note that $M \leq (M + K)$ and $2K|x| \leq (M+K) \cdot 2|x|$. More directly, since $1 + |x| \geq 1$ and $1 + |x| \geq |x|$:

    $$
    M + 2K|x| \leq M(1 + |x|) + 2K(1+|x|) = (M + 2K)(1 + |x|)
    $$

    A tighter bound matching the stated form uses $|x| \leq 1 + |x|$ and $1 \leq 1 + |x|$:

    $$
    |b(t,x)| + |\sigma(t,x)| \leq M \cdot 1 + K|x| + K|x| \leq M(1+|x|) + K(1+|x|) = (M+K)(1+|x|)
    $$

    This holds because $|b(t,x)| \leq |b(t,0)| + K|x| \leq M + K|x|$ and similarly for $\sigma$, and the Lipschitz bound gives $K|x|$ for each separately (not $2K|x|$ when combined). Specifically:

    $$
    |b(t,x)| + |\sigma(t,x)| \leq M + K|x| \leq (M + K)(1 + |x|)
    $$

    where the last step uses $M \leq (M+K)$ and $K|x| \leq (M+K)|x|$.

---

**Exercise 5.** Consider the diffusion coefficient $\sigma(x) = |x|^\alpha$ for $x \in \mathbb{R}$ and $\alpha \in (0,1)$. Show that $\sigma$ satisfies the Yamada--Watanabe condition by verifying that $\rho(u) = u^\alpha$ gives

$$
\int_0^\epsilon \frac{du}{\rho^2(u)} = \int_0^\epsilon u^{-2\alpha}\,du = +\infty
$$

if and only if $\alpha \geq \tfrac{1}{2}$. What happens when $\alpha < \tfrac{1}{2}$?

??? success "Solution to Exercise 5"
    Take $\rho(u) = u^\alpha$ for $\alpha \in (0,1)$. The Yamada--Watanabe integral becomes:

    $$
    \int_0^\epsilon \frac{du}{\rho^2(u)} = \int_0^\epsilon u^{-2\alpha}\,du
    $$

    The integrand $u^{-2\alpha}$ is integrable near $0$ if and only if $-2\alpha > -1$, i.e., $\alpha < 1/2$. Conversely, the integral diverges if and only if $-2\alpha \leq -1$, i.e., $\alpha \geq 1/2$. Explicitly:

    - If $2\alpha < 1$ (i.e., $\alpha < 1/2$):

    $$
    \int_0^\epsilon u^{-2\alpha}\,du = \frac{\epsilon^{1-2\alpha}}{1 - 2\alpha} < \infty
    $$

    - If $2\alpha = 1$ (i.e., $\alpha = 1/2$):

    $$
    \int_0^\epsilon u^{-1}\,du = \ln\epsilon - \ln 0 = +\infty
    $$

    - If $2\alpha > 1$ (i.e., $\alpha > 1/2$):

    $$
    \int_0^\epsilon u^{-2\alpha}\,du = \frac{u^{1-2\alpha}}{1-2\alpha}\Bigg|_0^\epsilon = +\infty
    $$

    since $1 - 2\alpha < 0$ and $u^{1-2\alpha} \to +\infty$ as $u \to 0^+$.

    Therefore the Yamada--Watanabe condition holds if and only if $\alpha \geq 1/2$.

    When $\alpha < 1/2$, the integral converges, so the Yamada--Watanabe theorem does not apply. Pathwise uniqueness may fail in this regime; indeed, for $dX_t = |X_t|^\alpha\,dW_t$ with $\alpha < 1/2$ and $X_0 = 0$, pathwise uniqueness is known to fail.

---

**Exercise 6.** The Vasicek model is $dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t$ with $\kappa, \sigma > 0$. Compute the Lipschitz constant $K$ for the pair $(b, \sigma)$ and verify the linear growth condition. Then state what the main existence and uniqueness theorem guarantees about the solution.

??? success "Solution to Exercise 6"
    The Vasicek model has $b(t,x) = \kappa(\theta - x) = \kappa\theta - \kappa x$ and $\sigma(t,x) = \sigma$ (constant).

    **Lipschitz condition:** For any $x, y \in \mathbb{R}$:

    $$
    |b(t,x) - b(t,y)| = |\kappa\theta - \kappa x - \kappa\theta + \kappa y| = \kappa|x - y|
    $$

    $$
    |\sigma(t,x) - \sigma(t,y)| = |\sigma - \sigma| = 0
    $$

    So the Lipschitz constant is $K = \kappa$.

    **Linear growth condition:** We have $|b(t,0)| = \kappa\theta$ and $|\sigma(t,0)| = \sigma$, so $M = \kappa\theta + \sigma$. By the result of Exercise 4:

    $$
    |b(t,x)| + |\sigma(t,x)| \leq (M + K)(1 + |x|) = (\kappa\theta + \sigma + \kappa)(1 + |x|)
    $$

    confirming linear growth.

    **Conclusion from the main theorem:** Since the coefficients are globally Lipschitz and satisfy linear growth, the main existence and uniqueness theorem guarantees that for any initial condition $X_0 = x_0$, there exists a unique strong solution $X_t \in C([0,T], \mathbb{R})$ a.s., with the moment bound:

    $$
    \mathbb{E}\!\left[\sup_{0 \leq t \leq T}|X_t|^2\right] \leq C(1 + |x_0|^2)e^{CT}
    $$

---

**Exercise 7.** Let $X_t$ and $Y_t$ be two strong solutions of $dZ_t = b(t,Z_t)\,dt + \sigma(t,Z_t)\,dW_t$ with $X_0 = Y_0$, where the coefficients are globally Lipschitz with constant $K$. Define $\varphi(t) = \mathbb{E}[\sup_{s \leq t}|X_s - Y_s|^2]$. Starting from the estimate

$$
\varphi(t) \leq C \int_0^t \varphi(s)\,ds
$$

apply Gronwall's inequality to conclude that $\varphi(t) = 0$ for all $t \in [0,T]$. Then explain why this proves pathwise uniqueness, not merely uniqueness in law.

??? success "Solution to Exercise 7"
    **Applying Gronwall's inequality:** The integral form of Gronwall's inequality states: if $\varphi : [0,T] \to [0,\infty)$ is a continuous function satisfying

    $$
    \varphi(t) \leq \alpha + \beta \int_0^t \varphi(s)\,ds
    $$

    for constants $\alpha \geq 0$ and $\beta > 0$, then $\varphi(t) \leq \alpha e^{\beta t}$ for all $t \in [0,T]$.

    In our case, $\alpha = 0$ and $\beta = C$, so:

    $$
    \varphi(t) \leq 0 \cdot e^{Ct} = 0
    $$

    Since $\varphi(t) = \mathbb{E}[\sup_{s \leq t}|X_s - Y_s|^2] \geq 0$ by definition, we conclude $\varphi(t) = 0$ for all $t \in [0,T]$.

    **Pathwise uniqueness, not merely uniqueness in law:** The conclusion $\mathbb{E}[\sup_{s \leq t}|X_s - Y_s|^2] = 0$ means that $\sup_{s \leq t}|X_s - Y_s|^2 = 0$ a.s. for each $t$. Taking $t = T$ gives $X_s = Y_s$ for all $s \in [0,T]$ a.s. (the sup over a compact interval of a continuous function being zero forces pointwise equality everywhere).

    This is pathwise uniqueness because $X$ and $Y$ are defined on the **same** probability space with the **same** Brownian motion $W_t$, and we proved $X_t(\omega) = Y_t(\omega)$ for a.e. $\omega$. Uniqueness in law would only assert $\mathrm{Law}(X) = \mathrm{Law}(Y)$, which is a weaker statement — two processes can have the same distribution while taking different values on a common probability space.
