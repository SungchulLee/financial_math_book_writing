# Conditional Expectation

Conditional expectation is the mathematical engine behind martingale theory. It formalizes the idea of "best prediction given available information" and underlies every major result in this chapter.

---

## Motivation

Suppose we observe a random variable $Y$ and want to predict another random variable $X$. If we know nothing, the best predictor (in the mean-squared sense) is $\mathbb{E}[X]$. But if we observe $Y$, our prediction should update to incorporate the new information. The conditional expectation $\mathbb{E}[X \mid Y]$ is precisely this updated prediction.

In stochastic processes, we replace the single observation $Y$ with a $\sigma$-algebra $\mathcal{G}$ encoding all available information. The conditional expectation $\mathbb{E}[X \mid \mathcal{G}]$ is the best $\mathcal{G}$-measurable prediction of $X$.

---

## Definition via Radon–Nikodym

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space, $\mathcal{G} \subseteq \mathcal{F}$ a sub-$\sigma$-algebra, and $X \in L^1(\Omega, \mathcal{F}, \mathbb{P})$.

**Definition**: The **conditional expectation** $\mathbb{E}[X \mid \mathcal{G}]$ is the unique (up to a.s. equality) random variable satisfying:

1. **Measurability**: $\mathbb{E}[X \mid \mathcal{G}]$ is $\mathcal{G}$-measurable.
2. **Partial averaging**: For every $G \in \mathcal{G}$

$$
\int_G \mathbb{E}[X \mid \mathcal{G}] \, d\mathbb{P} = \int_G X \, d\mathbb{P}
$$

**Existence and uniqueness**: Existence follows from the Radon–Nikodym theorem applied to the signed measure $\nu(G) = \int_G X \, d\mathbb{P}$ on $(\Omega, \mathcal{G})$, which is absolutely continuous with respect to $\mathbb{P}|_\mathcal{G}$. Uniqueness follows because if $Z_1$ and $Z_2$ both satisfy the conditions, then $Z_1 - Z_2$ is $\mathcal{G}$-measurable with $\int_G (Z_1 - Z_2) \, d\mathbb{P} = 0$ for all $G \in \mathcal{G}$, forcing $Z_1 = Z_2$ a.s.

**Notation**: We write $\mathbb{E}[X \mid \mathcal{G}]$, $\mathbb{E}^{\mathcal{G}}[X]$, or $\mathbb{E}[X \mid G]$ interchangeably.

---

## Geometric Interpretation

When $X \in L^2(\Omega, \mathcal{F}, \mathbb{P})$, the conditional expectation has an elegant geometric meaning:

$$
\mathbb{E}[X \mid \mathcal{G}] = \text{orthogonal projection of } X \text{ onto } L^2(\Omega, \mathcal{G}, \mathbb{P})
$$

The subspace $L^2(\mathcal{G}) \subseteq L^2(\mathcal{F})$ consists of all square-integrable $\mathcal{G}$-measurable random variables. The projection minimizes the $L^2$ distance:

$$
\mathbb{E}[X \mid \mathcal{G}] = \arg\min_{Z \in L^2(\mathcal{G})} \mathbb{E}[(X - Z)^2]
$$

This is the best $\mathcal{G}$-measurable approximation to $X$ in the least-squares sense — the "best predictor" interpretation made precise.

**Orthogonality**: The prediction error $X - \mathbb{E}[X \mid \mathcal{G}]$ is orthogonal to every $Z \in L^2(\mathcal{G})$:

$$
\mathbb{E}[(X - \mathbb{E}[X \mid \mathcal{G}]) \cdot Z] = 0 \quad \text{for all } Z \in L^2(\mathcal{G})
$$

---

## Concrete Examples

### Example 1: Discrete Case

Let $\Omega = \{1, 2, 3, 4\}$ with uniform probability $\mathbb{P}(\{k\}) = 1/4$. Let $\mathcal{G} = \sigma(\{\{1,2\}, \{3,4\}\})$ and $X(\omega) = \omega$.

Then $\mathbb{E}[X \mid \mathcal{G}]$ must be $\mathcal{G}$-measurable (constant on $\{1,2\}$ and on $\{3,4\}$) and match integrals over $\mathcal{G}$-sets:

$$
\mathbb{E}[X \mid \mathcal{G}](\omega) = \begin{cases} \frac{1+2}{2} = 1.5 & \omega \in \{1,2\} \\ \frac{3+4}{2} = 3.5 & \omega \in \{3,4\} \end{cases}
$$

This is the average of $X$ within each atom of $\mathcal{G}$.

### Example 2: Independent Random Variables

If $X$ and $Y$ are independent and $\mathcal{G} = \sigma(Y)$, then:

$$
\mathbb{E}[X \mid \mathcal{G}] = \mathbb{E}[X]
$$

Knowing $Y$ provides no information about $X$.

### Example 3: Brownian Motion Increment

Let $W_t$ be standard Brownian motion and $\mathcal{F}_s = \sigma(W_u : u \le s)$ for $s < t$. Then:

$$
\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s
$$

since $W_t - W_s \sim N(0, t-s)$ is independent of $\mathcal{F}_s$ with mean zero.

### Example 4: Gaussian Conditioning

If $(X, Y)$ is jointly Gaussian with means $\mu_X, \mu_Y$, variances $\sigma_X^2, \sigma_Y^2$, and correlation $\rho$, then:

$$
\mathbb{E}[X \mid Y] = \mu_X + \rho \frac{\sigma_X}{\sigma_Y}(Y - \mu_Y)
$$

This is the familiar linear regression formula, now derived as a conditional expectation.

---

## Key Properties

Let $X, Y \in L^1(\mathcal{F})$, $a, b \in \mathbb{R}$, and $\mathcal{H} \subseteq \mathcal{G} \subseteq \mathcal{F}$.

### 1. Linearity

$$
\mathbb{E}[aX + bY \mid \mathcal{G}] = a\,\mathbb{E}[X \mid \mathcal{G}] + b\,\mathbb{E}[Y \mid \mathcal{G}] \quad \text{a.s.}
$$

**Proof**: Both sides satisfy the definition (measurability and partial averaging). Uniqueness gives equality. $\square$

### 2. Tower Property (Law of Total Expectation)

$$
\mathbb{E}\bigl[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}\bigr] = \mathbb{E}[X \mid \mathcal{H}] \quad \text{a.s.}
$$

**Interpretation**: If $\mathcal{H}$ contains less information than $\mathcal{G}$, first conditioning on $\mathcal{G}$ and then on $\mathcal{H}$ is the same as conditioning directly on $\mathcal{H}$. The coarser $\sigma$-algebra "wins."

**Special case**: Taking $\mathcal{H} = \{\emptyset, \Omega\}$ (trivial $\sigma$-algebra):

$$
\mathbb{E}[\mathbb{E}[X \mid \mathcal{G}]] = \mathbb{E}[X]
$$

**Proof**: Let $Z = \mathbb{E}[\mathbb{E}[X|\mathcal{G}]|\mathcal{H}]$. For any $H \in \mathcal{H}$, since $\mathcal{H} \subseteq \mathcal{G}$ we have $H \in \mathcal{G}$, so the definition of $\mathbb{E}[X|\mathcal{G}]$ gives:

$$
\int_H Z \, d\mathbb{P} = \int_H \mathbb{E}[X \mid \mathcal{G}] \, d\mathbb{P} = \int_H X \, d\mathbb{P}
$$

Since $Z$ is $\mathcal{H}$-measurable and satisfies the partial averaging for all $H \in \mathcal{H}$, it equals $\mathbb{E}[X \mid \mathcal{H}]$ by uniqueness. $\square$

### 3. Taking Out What Is Known

If $Y$ is $\mathcal{G}$-measurable and $XY \in L^1$, then:

$$
\mathbb{E}[XY \mid \mathcal{G}] = Y \cdot \mathbb{E}[X \mid \mathcal{G}] \quad \text{a.s.}
$$

**Interpretation**: If $Y$ is already known (i.e., $\mathcal{G}$-measurable), it factors out of the conditional expectation like a constant.

**Proof sketch**: The right side is $\mathcal{G}$-measurable. For any $G \in \mathcal{G}$:

$$
\int_G Y \cdot \mathbb{E}[X \mid \mathcal{G}] \, d\mathbb{P} = \mathbb{E}[Y \cdot \mathbb{E}[X|\mathcal{G}] \cdot \mathbf{1}_G]
$$

Using the definition of conditional expectation, this equals $\int_G XY \, d\mathbb{P}$. Uniqueness completes the proof. $\square$

### 4. Independence

If $X$ is independent of $\mathcal{G}$, then:

$$
\mathbb{E}[X \mid \mathcal{G}] = \mathbb{E}[X] \quad \text{a.s.}
$$

**Proof**: The constant $\mathbb{E}[X]$ is $\mathcal{G}$-measurable, and for any $G \in \mathcal{G}$:

$$
\int_G \mathbb{E}[X] \, d\mathbb{P} = \mathbb{E}[X] \cdot \mathbb{P}(G) = \mathbb{E}[X \cdot \mathbf{1}_G] = \int_G X \, d\mathbb{P}
$$

where the last step uses independence of $X$ and $\mathbf{1}_G$. $\square$

### 5. Positivity and Monotonicity

- If $X \ge 0$ a.s., then $\mathbb{E}[X \mid \mathcal{G}] \ge 0$ a.s.
- If $X \le Y$ a.s., then $\mathbb{E}[X \mid \mathcal{G}] \le \mathbb{E}[Y \mid \mathcal{G}]$ a.s.

### 6. Conditional Jensen's Inequality

If $\varphi: \mathbb{R} \to \mathbb{R}$ is convex and $X, \varphi(X) \in L^1$, then:

$$
\varphi(\mathbb{E}[X \mid \mathcal{G}]) \le \mathbb{E}[\varphi(X) \mid \mathcal{G}] \quad \text{a.s.}
$$

**Applications**:

- $\varphi(x) = |x|$: $|\mathbb{E}[X \mid \mathcal{G}]| \le \mathbb{E}[|X| \mid \mathcal{G}]$
- $\varphi(x) = x^2$: $(\mathbb{E}[X \mid \mathcal{G}])^2 \le \mathbb{E}[X^2 \mid \mathcal{G}]$
- $\varphi(x) = e^x$: $e^{\mathbb{E}[X|\mathcal{G}]} \le \mathbb{E}[e^X \mid \mathcal{G}]$

### 7. Lp Contractivity

For $p \ge 1$:

$$
\|\mathbb{E}[X \mid \mathcal{G}]\|_{L^p} \le \|X\|_{L^p}
$$

**Proof**: Apply conditional Jensen's with $\varphi(x) = |x|^p$ and take expectations:

$$
\mathbb{E}[|\mathbb{E}[X|\mathcal{G}]|^p] \le \mathbb{E}[\mathbb{E}[|X|^p|\mathcal{G}]] = \mathbb{E}[|X|^p] \quad \square
$$

### 8. Conditional Monotone Convergence

If $X_n \ge 0$ and $X_n \uparrow X$ a.s. with $X \in L^1$, then:

$$
\mathbb{E}[X_n \mid \mathcal{G}] \uparrow \mathbb{E}[X \mid \mathcal{G}] \quad \text{a.s.}
$$

Similarly, conditional dominated convergence holds: if $|X_n| \le Y \in L^1$ and $X_n \to X$ a.s., then $\mathbb{E}[X_n \mid \mathcal{G}] \to \mathbb{E}[X \mid \mathcal{G}]$ a.s.

---

## Conditioning on a Random Variable

When $\mathcal{G} = \sigma(Y)$ for a random variable $Y$, we write $\mathbb{E}[X \mid Y]$ for $\mathbb{E}[X \mid \sigma(Y)]$.

By the Doob–Dynkin lemma, $\mathbb{E}[X \mid Y]$ is $\sigma(Y)$-measurable if and only if it is of the form $f(Y)$ for some Borel measurable function $f: \mathbb{R} \to \mathbb{R}$. We call $f$ the **regression function** of $X$ on $Y$.

**Discrete case**: If $Y$ takes countably many values $\{y_k\}$, then on the event $\{Y = y_k\}$:

$$
\mathbb{E}[X \mid Y] = \mathbb{E}[X \mid Y = y_k] := \frac{\mathbb{E}[X \cdot \mathbf{1}_{\{Y = y_k\}}]}{\mathbb{P}(Y = y_k)}
$$

This is the elementary conditional expectation from introductory probability.

---

## Conditional Expectation and Filtrations

In the context of stochastic processes with filtration $(\mathcal{F}_t)_{t \ge 0}$:

- $\mathbb{E}[X \mid \mathcal{F}_t]$ is the best prediction of $X$ using all information available at time $t$.
- The tower property $\mathbb{E}[\mathbb{E}[X \mid \mathcal{F}_t] \mid \mathcal{F}_s] = \mathbb{E}[X \mid \mathcal{F}_s]$ for $s \le t$ encodes that refining our estimate with more information and then averaging over less information gives the less-informed estimate.
- The process $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$ is a martingale — the **Doob martingale** — representing the gradual revelation of $X$ over time.

This connection is the foundation of martingale theory and is developed fully in the companion document *Martingales*.

---

## Summary

| Property | Formula | Interpretation |
|----------|---------|----------------|
| Definition | $\int_G \mathbb{E}[X\|\mathcal{G}]\,d\mathbb{P} = \int_G X\,d\mathbb{P}$ | Partial averaging |
| Geometry | Orthogonal projection onto $L^2(\mathcal{G})$ | Best predictor |
| Tower property | $\mathbb{E}[\mathbb{E}[X\|\mathcal{G}]\|\mathcal{H}] = \mathbb{E}[X\|\mathcal{H}]$ | Coarser $\sigma$-algebra wins |
| Known factor | $\mathbb{E}[XY\|\mathcal{G}] = Y\,\mathbb{E}[X\|\mathcal{G}]$ | $\mathcal{G}$-measurable factors out |
| Independence | $\mathbb{E}[X\|\mathcal{G}] = \mathbb{E}[X]$ | No information gained |
| Jensen | $\varphi(\mathbb{E}[X\|\mathcal{G}]) \le \mathbb{E}[\varphi(X)\|\mathcal{G}]$ | Convexity preserved |
| $L^p$ contraction | $\|\mathbb{E}[X\|\mathcal{G}]\|_p \le \|X\|_p$ | Conditioning reduces spread |

---

## Exercises

### Exercise 1: Computing Conditional Expectations

(a) Let $X \sim \text{Uniform}[0,1]$ and $Y = \lfloor 2X \rfloor$ (the integer part of $2X$, taking values 0 or 1). Compute $\mathbb{E}[X \mid Y]$.

(b) Let $(X, Y)$ be jointly Gaussian with $\mathbb{E}[X] = \mathbb{E}[Y] = 0$, $\text{Var}(X) = \text{Var}(Y) = 1$, $\text{Cov}(X,Y) = \rho$. Verify that $\mathbb{E}[X \mid Y] = \rho Y$.

(c) Let $N \sim \text{Poisson}(\lambda)$ and $X \mid N \sim \text{Binomial}(N, p)$. Compute $\mathbb{E}[X \mid N]$ and then $\mathbb{E}[X]$ using the tower property.

??? success "Solution to Exercise 1"
    **(a)** Since $X \sim \text{Uniform}[0,1]$ and $Y = \lfloor 2X \rfloor$, we have $Y = 0$ when $X \in [0, 1/2)$ and $Y = 1$ when $X \in [1/2, 1]$.

    The conditional expectation $\mathbb{E}[X \mid Y]$ is constant on each atom of $\sigma(Y)$:

    - On $\{Y = 0\}$: $\mathbb{E}[X \mid Y = 0] = \mathbb{E}[X \mid X \in [0, 1/2)] = \frac{1}{1/2}\int_0^{1/2} x\,dx = 2 \cdot \frac{1}{8} = \frac{1}{4}$

    - On $\{Y = 1\}$: $\mathbb{E}[X \mid Y = 1] = \mathbb{E}[X \mid X \in [1/2, 1]] = \frac{1}{1/2}\int_{1/2}^{1} x\,dx = 2 \cdot \frac{3}{8} = \frac{3}{4}$

    Therefore $\mathbb{E}[X \mid Y] = \frac{1}{4}\mathbf{1}_{\{Y=0\}} + \frac{3}{4}\mathbf{1}_{\{Y=1\}} = \frac{2Y + 1}{4}$.

    **(b)** For jointly Gaussian $(X, Y)$ with mean zero, unit variance, and correlation $\rho$, the conditional distribution of $X$ given $Y = y$ is:

    $$
    X \mid Y = y \sim N(\rho y, 1 - \rho^2)
    $$

    Therefore $\mathbb{E}[X \mid Y = y] = \rho y$, so $\mathbb{E}[X \mid Y] = \rho Y$.

    To verify: $\rho Y$ is $\sigma(Y)$-measurable. For the partial averaging condition, for any $B \in \mathcal{B}(\mathbb{R})$:

    $$
    \mathbb{E}[\rho Y \cdot \mathbf{1}_{\{Y \in B\}}] = \rho \mathbb{E}[Y \mathbf{1}_{\{Y \in B\}}]
    $$

    $$
    \mathbb{E}[X \cdot \mathbf{1}_{\{Y \in B\}}] = \mathbb{E}[\mathbb{E}[X \mathbf{1}_{\{Y \in B\}} \mid Y]] = \mathbb{E}[\mathbf{1}_{\{Y \in B\}} \mathbb{E}[X \mid Y]] = \mathbb{E}[\rho Y \cdot \mathbf{1}_{\{Y \in B\}}]
    $$

    The two expressions match, confirming $\mathbb{E}[X \mid Y] = \rho Y$. $\square$

    **(c)** Given $N$, $X \mid N \sim \text{Binomial}(N, p)$, so:

    $$
    \mathbb{E}[X \mid N] = Np
    $$

    By the tower property:

    $$
    \mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X \mid N]] = \mathbb{E}[Np] = p\,\mathbb{E}[N] = p\lambda
    $$

---

### Exercise 2: Tower Property

(a) Let $\mathcal{H} \subseteq \mathcal{G}$. Prove the tower property directly from the definition.

(b) Use the tower property to show $\text{Var}(X) = \mathbb{E}[\text{Var}(X \mid Y)] + \text{Var}(\mathbb{E}[X \mid Y])$.

(c) Apply (b) to the setup of Exercise 1(c) to compute $\text{Var}(X)$.

??? success "Solution to Exercise 2"
    **(a)** Let $\mathcal{H} \subseteq \mathcal{G}$ and let $Z = \mathbb{E}[\mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{H}]$. We verify $Z = \mathbb{E}[X \mid \mathcal{H}]$ by checking the defining properties.

    - *Measurability*: $Z$ is $\mathcal{H}$-measurable by definition of conditional expectation.

    - *Partial averaging*: For any $H \in \mathcal{H}$, since $\mathcal{H} \subseteq \mathcal{G}$ we have $H \in \mathcal{G}$. Then:

    $$
    \int_H Z \, d\mathbb{P} = \int_H \mathbb{E}[X \mid \mathcal{G}] \, d\mathbb{P} = \int_H X \, d\mathbb{P}
    $$

    The first equality uses the definition of $Z$ as conditional expectation of $\mathbb{E}[X \mid \mathcal{G}]$ given $\mathcal{H}$ (partial averaging over $H \in \mathcal{H}$). The second uses the definition of $\mathbb{E}[X \mid \mathcal{G}]$ (partial averaging over $H \in \mathcal{G}$).

    By uniqueness, $Z = \mathbb{E}[X \mid \mathcal{H}]$. $\square$

    **(b)** The **law of total variance** states $\text{Var}(X) = \mathbb{E}[\text{Var}(X \mid Y)] + \text{Var}(\mathbb{E}[X \mid Y])$.

    Start from $\text{Var}(X \mid Y) = \mathbb{E}[X^2 \mid Y] - (\mathbb{E}[X \mid Y])^2$. Taking expectations:

    $$
    \mathbb{E}[\text{Var}(X \mid Y)] = \mathbb{E}[X^2] - \mathbb{E}[(\mathbb{E}[X \mid Y])^2]
    $$

    Also, $\text{Var}(\mathbb{E}[X \mid Y]) = \mathbb{E}[(\mathbb{E}[X \mid Y])^2] - (\mathbb{E}[\mathbb{E}[X \mid Y]])^2 = \mathbb{E}[(\mathbb{E}[X \mid Y])^2] - (\mathbb{E}[X])^2$.

    Adding:

    $$
    \mathbb{E}[\text{Var}(X \mid Y)] + \text{Var}(\mathbb{E}[X \mid Y]) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \text{Var}(X) \quad \square
    $$

    **(c)** From Exercise 1(c): $\mathbb{E}[X \mid N] = Np$ and $\text{Var}(X \mid N) = Np(1-p)$ (variance of $\text{Binomial}(N, p)$).

    $$
    \mathbb{E}[\text{Var}(X \mid N)] = \mathbb{E}[Np(1-p)] = p(1-p)\lambda
    $$

    $$
    \text{Var}(\mathbb{E}[X \mid N]) = \text{Var}(Np) = p^2 \text{Var}(N) = p^2 \lambda
    $$

    Therefore:

    $$
    \text{Var}(X) = p(1-p)\lambda + p^2\lambda = p\lambda(1 - p + p) = p\lambda
    $$

---

### Exercise 3: Taking Out What Is Known

(a) Prove the "taking out what is known" property for bounded $\mathcal{G}$-measurable $Y$.

*Hint*: Verify measurability and check the partial averaging condition using the definition of conditional expectation.

(b) Use this property to show: if $f$ is Borel measurable and $Y$ is $\mathcal{G}$-measurable, then $\mathbb{E}[f(Y) \cdot X \mid \mathcal{G}] = f(Y) \cdot \mathbb{E}[X \mid \mathcal{G}]$.

??? success "Solution to Exercise 3"
    **(a)** We must show that $Y \cdot \mathbb{E}[X \mid \mathcal{G}]$ satisfies the two defining properties of $\mathbb{E}[XY \mid \mathcal{G}]$, assuming $Y$ is bounded and $\mathcal{G}$-measurable.

    - *Measurability*: Since $Y$ is $\mathcal{G}$-measurable and $\mathbb{E}[X \mid \mathcal{G}]$ is $\mathcal{G}$-measurable, their product $Y \cdot \mathbb{E}[X \mid \mathcal{G}]$ is $\mathcal{G}$-measurable.

    - *Partial averaging*: For any $G \in \mathcal{G}$, the product $Y \cdot \mathbf{1}_G$ is $\mathcal{G}$-measurable and bounded. By the definition of conditional expectation:

    $$
    \int_G Y \cdot \mathbb{E}[X \mid \mathcal{G}] \, d\mathbb{P} = \mathbb{E}[Y \cdot \mathbf{1}_G \cdot \mathbb{E}[X \mid \mathcal{G}]]
    $$

    Since $Y \cdot \mathbf{1}_G$ is bounded and $\mathcal{G}$-measurable, the partial averaging property of $\mathbb{E}[X \mid \mathcal{G}]$ applied to the set $G$ with indicator weighted by $Y$ gives (by a standard approximation argument for bounded measurable functions):

    $$
    \mathbb{E}[Y \cdot \mathbf{1}_G \cdot \mathbb{E}[X \mid \mathcal{G}]] = \mathbb{E}[Y \cdot \mathbf{1}_G \cdot X] = \int_G XY \, d\mathbb{P}
    $$

    By uniqueness, $\mathbb{E}[XY \mid \mathcal{G}] = Y \cdot \mathbb{E}[X \mid \mathcal{G}]$. $\square$

    **(b)** Since $Y$ is $\mathcal{G}$-measurable, $f(Y)$ is also $\mathcal{G}$-measurable for any Borel measurable $f$ (composition of measurable functions is measurable). Apply part (a) with $f(Y)$ in place of $Y$:

    $$
    \mathbb{E}[f(Y) \cdot X \mid \mathcal{G}] = f(Y) \cdot \mathbb{E}[X \mid \mathcal{G}]
    $$

    (The result for bounded $f(Y)$ follows directly from (a); for general $f$ with $f(Y) \cdot X \in L^1$, one extends by monotone class or truncation arguments.) $\square$

---

### Exercise 4: Conditional Jensen

(a) Prove Jensen's inequality for conditional expectations: if $\varphi$ is convex and $X, \varphi(X) \in L^1$, then $\varphi(\mathbb{E}[X \mid \mathcal{G}]) \le \mathbb{E}[\varphi(X) \mid \mathcal{G}]$.

*Hint*: Use the supporting hyperplane characterization of convexity: $\varphi(y) \ge \varphi(x) + \varphi'(x)(y - x)$ for all $x, y$ (where $\varphi'$ is a subgradient).

(b) Deduce that $|\mathbb{E}[X \mid \mathcal{G}]| \le \mathbb{E}[|X| \mid \mathcal{G}]$ and use this to prove $L^p$ contractivity.

??? success "Solution to Exercise 4"
    **(a)** Since $\varphi$ is convex, for every $x_0 \in \mathbb{R}$ there exists a subgradient $a(x_0)$ such that:

    $$
    \varphi(y) \ge \varphi(x_0) + a(x_0)(y - x_0) \quad \text{for all } y \in \mathbb{R}
    $$

    Apply this with $x_0 = \mathbb{E}[X \mid \mathcal{G}](\omega)$ and $y = X(\omega)$:

    $$
    \varphi(X) \ge \varphi(\mathbb{E}[X \mid \mathcal{G}]) + a(\mathbb{E}[X \mid \mathcal{G}])(X - \mathbb{E}[X \mid \mathcal{G}])
    $$

    Take conditional expectations given $\mathcal{G}$. Since $\varphi(\mathbb{E}[X \mid \mathcal{G}])$ and $a(\mathbb{E}[X \mid \mathcal{G}])$ are $\mathcal{G}$-measurable:

    $$
    \mathbb{E}[\varphi(X) \mid \mathcal{G}] \ge \varphi(\mathbb{E}[X \mid \mathcal{G}]) + a(\mathbb{E}[X \mid \mathcal{G}]) \cdot \mathbb{E}[X - \mathbb{E}[X \mid \mathcal{G}] \mid \mathcal{G}]
    $$

    The last term is $a(\mathbb{E}[X \mid \mathcal{G}]) \cdot (\mathbb{E}[X \mid \mathcal{G}] - \mathbb{E}[X \mid \mathcal{G}]) = 0$. Therefore:

    $$
    \mathbb{E}[\varphi(X) \mid \mathcal{G}] \ge \varphi(\mathbb{E}[X \mid \mathcal{G}]) \quad \square
    $$

    **(b)** Apply conditional Jensen with $\varphi(x) = |x|$ (convex):

    $$
    |\mathbb{E}[X \mid \mathcal{G}]| \le \mathbb{E}[|X| \mid \mathcal{G}]
    $$

    For $L^p$ contractivity with $p \ge 1$, apply conditional Jensen with $\varphi(x) = |x|^p$:

    $$
    |\mathbb{E}[X \mid \mathcal{G}]|^p \le \mathbb{E}[|X|^p \mid \mathcal{G}]
    $$

    Taking expectations of both sides and using the tower property:

    $$
    \mathbb{E}[|\mathbb{E}[X \mid \mathcal{G}]|^p] \le \mathbb{E}[\mathbb{E}[|X|^p \mid \mathcal{G}]] = \mathbb{E}[|X|^p]
    $$

    Therefore $\|\mathbb{E}[X \mid \mathcal{G}]\|_{L^p} \le \|X\|_{L^p}$. $\square$

---

### Exercise 5: Brownian Motion

Let $(W_t)$ be standard Brownian motion with natural filtration $(\mathcal{F}_t)$.

(a) Compute $\mathbb{E}[W_t^2 \mid \mathcal{F}_s]$ for $s \le t$.

(b) Compute $\mathbb{E}[W_t^3 \mid \mathcal{F}_s]$ for $s \le t$.

*Hint*: Write $W_t = W_s + (W_t - W_s)$ and expand. Use the moments of $W_t - W_s \sim N(0, t-s)$.

(c) For $\lambda \in \mathbb{R}$, compute $\mathbb{E}[e^{\lambda W_t} \mid \mathcal{F}_s]$.

*Hint*: Factor $e^{\lambda W_t} = e^{\lambda W_s} \cdot e^{\lambda(W_t - W_s)}$ and use independence and the moment generating function of a Gaussian.

??? success "Solution to Exercise 5"
    **(a)** Write $W_t = W_s + (W_t - W_s)$ and expand:

    $$
    W_t^2 = W_s^2 + 2W_s(W_t - W_s) + (W_t - W_s)^2
    $$

    Taking conditional expectations and using that $W_t - W_s$ is independent of $\mathcal{F}_s$ with $\mathbb{E}[W_t - W_s] = 0$ and $\mathbb{E}[(W_t - W_s)^2] = t - s$:

    $$
    \mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + 2W_s \cdot 0 + (t - s) = W_s^2 + (t - s)
    $$

    **(b)** Expand $W_t^3 = (W_s + (W_t - W_s))^3$:

    $$
    W_t^3 = W_s^3 + 3W_s^2(W_t - W_s) + 3W_s(W_t - W_s)^2 + (W_t - W_s)^3
    $$

    Let $\Delta = W_t - W_s \sim N(0, t-s)$, independent of $\mathcal{F}_s$. The moments are $\mathbb{E}[\Delta] = 0$, $\mathbb{E}[\Delta^2] = t - s$, $\mathbb{E}[\Delta^3] = 0$ (by symmetry of the Gaussian).

    $$
    \mathbb{E}[W_t^3 \mid \mathcal{F}_s] = W_s^3 + 3W_s^2 \cdot 0 + 3W_s(t-s) + 0 = W_s^3 + 3(t-s)W_s
    $$

    **(c)** Factor $e^{\lambda W_t} = e^{\lambda W_s} \cdot e^{\lambda(W_t - W_s)}$. Since $e^{\lambda W_s}$ is $\mathcal{F}_s$-measurable and $W_t - W_s$ is independent of $\mathcal{F}_s$:

    $$
    \mathbb{E}[e^{\lambda W_t} \mid \mathcal{F}_s] = e^{\lambda W_s} \cdot \mathbb{E}[e^{\lambda(W_t - W_s)}]
    $$

    Since $W_t - W_s \sim N(0, t - s)$, the moment generating function gives:

    $$
    \mathbb{E}[e^{\lambda(W_t - W_s)}] = e^{\lambda^2(t-s)/2}
    $$

    Therefore:

    $$
    \mathbb{E}[e^{\lambda W_t} \mid \mathcal{F}_s] = e^{\lambda W_s + \lambda^2(t-s)/2}
    $$
