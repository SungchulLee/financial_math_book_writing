# Conditional Expectation

Conditional expectation is the engine of martingale theory. Given information encoded by a σ-algebra $\mathcal{G}$, it produces the best $\mathcal{G}$-measurable prediction of a random variable $X$. Every theorem in this chapter — the martingale property, optional sampling, Doob's inequalities, the Doob–Meyer decomposition — is ultimately a statement about conditional expectations.

---

## Motivation: Best Prediction

If we know nothing, the best prediction of $X$ (in mean-squared sense) is the constant $\mathbb{E}[X]$. If we observe information $\mathcal{G}$ — a sub-σ-algebra of $\mathcal{F}$ — the prediction should update to the best $\mathcal{G}$-measurable random variable approximating $X$. This updated prediction is $\mathbb{E}[X \mid \mathcal{G}]$.

---

## Definition via Radon–Nikodym

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space, $\mathcal{G} \subseteq \mathcal{F}$ a sub-σ-algebra, and $X \in L^1(\Omega, \mathcal{F}, \mathbb{P})$.

!!! abstract "Definition (Conditional Expectation)"
    $\mathbb{E}[X \mid \mathcal{G}]$ is the a.s.-unique random variable satisfying:

    1. **Measurability**: $\mathbb{E}[X \mid \mathcal{G}]$ is $\mathcal{G}$-measurable.
    2. **Partial averaging**: $\int_G \mathbb{E}[X \mid \mathcal{G}] \, d\mathbb{P} = \int_G X \, d\mathbb{P}$ for every $G \in \mathcal{G}$.

**Proof of existence and uniqueness.** Define the signed measure $\nu(G) := \int_G X \, d\mathbb{P}$ on $(\Omega, \mathcal{G})$. Since $\mathbb{P}(G) = 0 \Rightarrow \nu(G) = 0$, $\nu$ is absolutely continuous w.r.t. $\mathbb{P}|_\mathcal{G}$. By Radon–Nikodym there is a $\mathcal{G}$-measurable density $Z = d\nu/d\mathbb{P}|_\mathcal{G}$; this $Z$ satisfies both properties. If $Z_1, Z_2$ both work, $\int_G (Z_1 - Z_2) \, d\mathbb{P} = 0$ for all $G \in \mathcal{G}$ with $Z_1 - Z_2$ being $\mathcal{G}$-measurable, forcing $Z_1 = Z_2$ a.s. $\square$

---

## Geometric Interpretation

For $X \in L^2$, conditional expectation is the **orthogonal projection** of $X$ onto the closed subspace $L^2(\mathcal{G}) \subseteq L^2(\mathcal{F})$:

$$
\mathbb{E}[X \mid \mathcal{G}] = \arg\min_{Z \in L^2(\mathcal{G})} \mathbb{E}[(X - Z)^2]
$$

The residual $X - \mathbb{E}[X \mid \mathcal{G}]$ is orthogonal to every $Z \in L^2(\mathcal{G})$:

$$
\mathbb{E}[(X - \mathbb{E}[X \mid \mathcal{G}]) \cdot Z] = 0 \quad \text{for all } Z \in L^2(\mathcal{G})
$$

This is the "best predictor" property made precise.

---

## Examples

!!! example "Discrete atoms"
    $\Omega = \{1,2,3,4\}$ with uniform probability, $\mathcal{G} = \sigma(\{\{1,2\},\{3,4\}\})$, $X(\omega) = \omega$. Then $\mathbb{E}[X \mid \mathcal{G}]$ is constant on each atom:

    $$
    \mathbb{E}[X \mid \mathcal{G}] = \begin{cases} 1.5 & \text{on } \{1,2\} \\ 3.5 & \text{on } \{3,4\} \end{cases}
    $$

    — the average of $X$ within each atom.

!!! example "Independence"
    If $X \perp \mathcal{G}$, then $\mathbb{E}[X \mid \mathcal{G}] = \mathbb{E}[X]$ a.s. Knowing $\mathcal{G}$ provides no information about $X$.

!!! example "Brownian increment"
    Let $W$ be standard Brownian motion, $\mathcal{F}_s = \sigma(W_u : u \le s)$, $s < t$. Since $W_t - W_s \sim N(0, t-s)$ is independent of $\mathcal{F}_s$ and $W_s$ is $\mathcal{F}_s$-measurable,

    $$
    \mathbb{E}[W_t \mid \mathcal{F}_s] = W_s + \mathbb{E}[W_t - W_s \mid \mathcal{F}_s] = W_s
    $$

    This computation is the prototype for all Brownian martingale calculations.

---

## Key Properties

Let $X, Y \in L^1$, $a, b \in \mathbb{R}$, and $\mathcal{H} \subseteq \mathcal{G} \subseteq \mathcal{F}$.

**1. Linearity.**

$$
\mathbb{E}[aX + bY \mid \mathcal{G}] = a\,\mathbb{E}[X \mid \mathcal{G}] + b\,\mathbb{E}[Y \mid \mathcal{G}] \quad \text{a.s.}
$$

**2. Tower property.**

$$
\mathbb{E}\bigl[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}\bigr] = \mathbb{E}[X \mid \mathcal{H}] \quad \text{a.s.}
$$

The coarser σ-algebra wins. Special case ($\mathcal{H} = \{\emptyset, \Omega\}$): $\mathbb{E}[\mathbb{E}[X \mid \mathcal{G}]] = \mathbb{E}[X]$.

*Proof sketch*: For $H \in \mathcal{H} \subseteq \mathcal{G}$, $\int_H \mathbb{E}[X|\mathcal{G}]\,d\mathbb{P} = \int_H X\,d\mathbb{P}$. Combined with $\mathcal{H}$-measurability of the left side, uniqueness gives the result.

**3. Taking out what is known.** If $Y$ is $\mathcal{G}$-measurable and $XY \in L^1$,

$$
\mathbb{E}[XY \mid \mathcal{G}] = Y \cdot \mathbb{E}[X \mid \mathcal{G}] \quad \text{a.s.}
$$

**4. Independence.** If $X \perp \mathcal{G}$, then $\mathbb{E}[X \mid \mathcal{G}] = \mathbb{E}[X]$ a.s.

**5. Positivity / monotonicity.** $X \ge 0 \Rightarrow \mathbb{E}[X \mid \mathcal{G}] \ge 0$; $X \le Y \Rightarrow \mathbb{E}[X \mid \mathcal{G}] \le \mathbb{E}[Y \mid \mathcal{G}]$.

**6. Conditional Jensen.** For convex $\varphi$ with $X, \varphi(X) \in L^1$,

$$
\varphi(\mathbb{E}[X \mid \mathcal{G}]) \le \mathbb{E}[\varphi(X) \mid \mathcal{G}] \quad \text{a.s.}
$$

Applied with $\varphi(x) = |x|^p$ and taking expectations gives **$L^p$ contractivity** for $p \ge 1$:

$$
\|\mathbb{E}[X \mid \mathcal{G}]\|_{L^p} \le \|X\|_{L^p}
$$

**7. Conditional MCT / DCT.** Monotone and dominated convergence hold inside $\mathbb{E}[\,\cdot \mid \mathcal{G}]$.

---

## Conditioning on a Random Variable

When $\mathcal{G} = \sigma(Y)$, write $\mathbb{E}[X \mid Y]$. By the Doob–Dynkin lemma, $\mathbb{E}[X \mid Y] = f(Y)$ for some Borel $f$ — the **regression function**. In the discrete case with $\mathbb{P}(Y = y_k) > 0$,

$$
\mathbb{E}[X \mid Y = y_k] = \frac{\mathbb{E}[X \cdot \mathbf{1}_{\{Y = y_k\}}]}{\mathbb{P}(Y = y_k)}
$$

For jointly Gaussian $(X, Y)$ with means $\mu_X, \mu_Y$, variances $\sigma_X^2, \sigma_Y^2$, correlation $\rho$,

$$
\mathbb{E}[X \mid Y] = \mu_X + \rho \frac{\sigma_X}{\sigma_Y}(Y - \mu_Y)
$$

— the linear regression formula, recovered as a conditional expectation.

---

## Connection to Filtrations

For a filtration $(\mathcal{F}_t)$ and $X \in L^1(\mathcal{F})$, the process

$$
M_t := \mathbb{E}[X \mid \mathcal{F}_t]
$$

is the **Doob martingale**: the best prediction of $X$ using information up to $t$. The tower property is exactly the martingale property for $M$: for $s \le t$, $\mathbb{E}[M_t \mid \mathcal{F}_s] = \mathbb{E}[\mathbb{E}[X \mid \mathcal{F}_t] \mid \mathcal{F}_s] = \mathbb{E}[X \mid \mathcal{F}_s] = M_s$. This observation is the entry point to the next section, [Martingales](martingales.md).

---

## Summary

| Property | Formula |
|---|---|
| Definition | $\int_G \mathbb{E}[X \mid \mathcal{G}]\,d\mathbb{P} = \int_G X\,d\mathbb{P}$ for $G \in \mathcal{G}$ |
| Geometry | Orthogonal projection onto $L^2(\mathcal{G})$ |
| Tower | $\mathbb{E}[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}] = \mathbb{E}[X \mid \mathcal{H}]$, $\mathcal{H} \subseteq \mathcal{G}$ |
| Known factor | $\mathbb{E}[XY \mid \mathcal{G}] = Y\,\mathbb{E}[X \mid \mathcal{G}]$, $Y$ $\mathcal{G}$-meas. |
| Independence | $\mathbb{E}[X \mid \mathcal{G}] = \mathbb{E}[X]$, $X \perp \mathcal{G}$ |
| Jensen | $\varphi(\mathbb{E}[X \mid \mathcal{G}]) \le \mathbb{E}[\varphi(X) \mid \mathcal{G}]$, $\varphi$ convex |
| $L^p$ contraction | $\|\mathbb{E}[X \mid \mathcal{G}]\|_p \le \|X\|_p$ |

---

## Exercises

**Exercise 1.** Let $X \sim \text{Uniform}[0,1]$ and $Y = \lfloor 2X \rfloor$. Compute $\mathbb{E}[X \mid Y]$.

??? success "Solution to Exercise 1"
    $Y = 0$ on $[0, 1/2)$ and $Y = 1$ on $[1/2, 1]$, each with probability $1/2$. Conditional expectation is the uniform average on each atom:

    $$
    \mathbb{E}[X \mid Y = 0] = \frac{1}{1/2}\int_0^{1/2} x\,dx = \frac{1}{4}, \qquad \mathbb{E}[X \mid Y = 1] = \frac{3}{4}
    $$

    So $\mathbb{E}[X \mid Y] = \frac{2Y + 1}{4}$.

---

**Exercise 2.** Let $N \sim \text{Poisson}(\lambda)$ and, given $N$, $X \sim \text{Binomial}(N, p)$.

(a) Compute $\mathbb{E}[X \mid N]$ and deduce $\mathbb{E}[X]$.

(b) Use the law of total variance $\mathrm{Var}(X) = \mathbb{E}[\mathrm{Var}(X \mid N)] + \mathrm{Var}(\mathbb{E}[X \mid N])$ to compute $\mathrm{Var}(X)$.

??? success "Solution to Exercise 2"
    **(a)** $\mathbb{E}[X \mid N] = Np$ (mean of Binomial). Tower: $\mathbb{E}[X] = \mathbb{E}[Np] = p\lambda$.

    **(b)** $\mathrm{Var}(X \mid N) = Np(1-p)$, so $\mathbb{E}[\mathrm{Var}(X \mid N)] = p(1-p)\lambda$. And $\mathrm{Var}(\mathbb{E}[X \mid N]) = p^2 \mathrm{Var}(N) = p^2 \lambda$. Sum: $\mathrm{Var}(X) = p\lambda(1-p) + p^2\lambda = p\lambda$. (Consistent with $X \sim \text{Poisson}(p\lambda)$.)

---

**Exercise 3.** Prove the **"taking out what is known"** property: if $Y$ is bounded and $\mathcal{G}$-measurable and $X \in L^1$, then $\mathbb{E}[XY \mid \mathcal{G}] = Y \cdot \mathbb{E}[X \mid \mathcal{G}]$.

??? success "Solution to Exercise 3"
    The RHS is $\mathcal{G}$-measurable (product of $\mathcal{G}$-measurable functions). For the partial averaging, it suffices to verify on indicators $Y = \mathbf{1}_H$ with $H \in \mathcal{G}$, then extend by linearity and monotone limits.

    For $G \in \mathcal{G}$:

    $$
    \int_G \mathbf{1}_H \cdot \mathbb{E}[X \mid \mathcal{G}]\,d\mathbb{P} = \int_{G \cap H} \mathbb{E}[X \mid \mathcal{G}]\,d\mathbb{P} = \int_{G \cap H} X\,d\mathbb{P} = \int_G \mathbf{1}_H \cdot X\,d\mathbb{P}
    $$

    using that $G \cap H \in \mathcal{G}$ and the partial averaging property of $\mathbb{E}[X \mid \mathcal{G}]$. Uniqueness concludes. Standard extension (simple → bounded measurable via MCT) gives the general case. $\square$

---

**Exercise 4.** Prove **conditional Jensen's inequality**: if $\varphi : \mathbb{R} \to \mathbb{R}$ is convex with $X, \varphi(X) \in L^1$, then $\varphi(\mathbb{E}[X \mid \mathcal{G}]) \le \mathbb{E}[\varphi(X) \mid \mathcal{G}]$.

??? success "Solution to Exercise 4"
    By convexity, at every $x_0$ there is a subgradient $a(x_0)$ with $\varphi(y) \ge \varphi(x_0) + a(x_0)(y - x_0)$ for all $y$. Set $x_0 = \mathbb{E}[X \mid \mathcal{G}]$ and $y = X$:

    $$
    \varphi(X) \ge \varphi(\mathbb{E}[X \mid \mathcal{G}]) + a(\mathbb{E}[X \mid \mathcal{G}])\bigl(X - \mathbb{E}[X \mid \mathcal{G}]\bigr)
    $$

    The first two terms on the RHS are $\mathcal{G}$-measurable; taking conditional expectation and using linearity plus "taking out what is known" on the last term gives

    $$
    \mathbb{E}[\varphi(X) \mid \mathcal{G}] \ge \varphi(\mathbb{E}[X \mid \mathcal{G}]) + a(\mathbb{E}[X \mid \mathcal{G}]) \cdot 0 = \varphi(\mathbb{E}[X \mid \mathcal{G}]) \quad \square
    $$

---

**Exercise 5.** Let $W$ be standard Brownian motion with natural filtration $(\mathcal{F}_t)$ and $s \le t$.

(a) Compute $\mathbb{E}[W_t^2 \mid \mathcal{F}_s]$ and $\mathbb{E}[W_t^3 \mid \mathcal{F}_s]$.

(b) For $\lambda \in \mathbb{R}$, compute $\mathbb{E}[e^{\lambda W_t} \mid \mathcal{F}_s]$.

??? success "Solution to Exercise 5"
    Let $\Delta = W_t - W_s \sim N(0, t-s)$, independent of $\mathcal{F}_s$, with $\mathbb{E}[\Delta] = 0$, $\mathbb{E}[\Delta^2] = t-s$, $\mathbb{E}[\Delta^3] = 0$.

    **(a)** $W_t^2 = W_s^2 + 2W_s \Delta + \Delta^2$, so $\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + (t - s)$.

    $W_t^3 = W_s^3 + 3W_s^2\Delta + 3W_s\Delta^2 + \Delta^3$, so $\mathbb{E}[W_t^3 \mid \mathcal{F}_s] = W_s^3 + 3(t-s)W_s$.

    **(b)** $e^{\lambda W_t} = e^{\lambda W_s} e^{\lambda \Delta}$. With $e^{\lambda W_s}$ $\mathcal{F}_s$-measurable and $\Delta \perp \mathcal{F}_s$:

    $$
    \mathbb{E}[e^{\lambda W_t} \mid \mathcal{F}_s] = e^{\lambda W_s} \cdot \mathbb{E}[e^{\lambda \Delta}] = e^{\lambda W_s + \lambda^2(t-s)/2}
    $$

    Equivalently, $M_t := e^{\lambda W_t - \lambda^2 t/2}$ satisfies $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ — the exponential martingale, used throughout Girsanov theory.

---

**Exercise 6.** Let $\mathcal{H} \subseteq \mathcal{G} \subseteq \mathcal{F}$ and $X \in L^2$. Prove the **Pythagorean decomposition**:

$$
\|X - \mathbb{E}[X \mid \mathcal{H}]\|_{L^2}^2 = \|X - \mathbb{E}[X \mid \mathcal{G}]\|_{L^2}^2 + \|\mathbb{E}[X \mid \mathcal{G}] - \mathbb{E}[X \mid \mathcal{H}]\|_{L^2}^2
$$

Interpret geometrically.

??? success "Solution to Exercise 6"
    Write $X - \mathbb{E}[X \mid \mathcal{H}] = (X - \mathbb{E}[X \mid \mathcal{G}]) + (\mathbb{E}[X \mid \mathcal{G}] - \mathbb{E}[X \mid \mathcal{H}])$. The two summands are orthogonal in $L^2$: the first is orthogonal to all of $L^2(\mathcal{G})$ (it is the projection residual), and the second lies in $L^2(\mathcal{G})$ (both terms are $\mathcal{G}$-measurable, using $\mathcal{H} \subseteq \mathcal{G}$). Squared $L^2$-norms add. $\square$

    *Geometrically*: $L^2(\mathcal{H}) \subseteq L^2(\mathcal{G}) \subseteq L^2(\mathcal{F})$ is a chain of nested closed subspaces; projecting to the smaller space can be done by first projecting to the intermediate space and then to the smaller — and the Pythagorean theorem applies to the two orthogonal legs. This is the $L^2$ shadow of the tower property.
