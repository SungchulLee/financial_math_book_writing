# Lipschitz Conditions and Linear Growth

The existence and uniqueness theory for stochastic differential equations rests on two fundamental analytical conditions: the **Lipschitz condition** (ensuring uniqueness) and the **linear growth condition** (preventing explosions). This section develops these conditions in detail.

---

## The SDE Setting

Consider the $d$-dimensional SDE driven by $m$-dimensional Brownian motion:

$$
dX_t^i = b^i(t, X_t)\,dt + \sigma^{i\alpha}(t, X_t)\,dW_t^\alpha, \quad X_0 = x \in \mathbb{R}^d
$$

In integral form:

$$
X_t = x + \int_0^t b(s, X_s)\,ds + \int_0^t \sigma(s, X_s)\,dW_s
$$

**Goal**: Under what conditions on $b$ and $\sigma$ does a unique solution exist?

---

## The Lipschitz Condition

### Definition

The coefficients $b: [0,T] \times \mathbb{R}^d \to \mathbb{R}^d$ and $\sigma: [0,T] \times \mathbb{R}^d \to \mathbb{R}^{d \times m}$ satisfy the **(global) Lipschitz condition** if there exists a constant $K > 0$ such that for all $t \in [0,T]$ and $x, y \in \mathbb{R}^d$:

$$
\boxed{
|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K|x - y|
}
$$

Here $|\cdot|$ denotes the Euclidean norm for vectors and the Frobenius norm for matrices:

$$
|\sigma|^2 = \sum_{i,\alpha} (\sigma^{i\alpha})^2
$$

### Interpretation

**Lipschitz continuity** means the coefficients cannot change too rapidly as a function of the state variable $x$. Small changes in position lead to small changes in drift and diffusion.

**Geometric meaning**: The "vector field" $(b, \sigma)$ has bounded "slope" in the spatial direction.

### Why Lipschitz Implies Uniqueness

**Intuition**: If two solutions $X_t$ and $Y_t$ start close together, Lipschitz continuity ensures they cannot diverge too quickly.

**Formal argument** (Gronwall): Let $X_t$ and $Y_t$ be two solutions. Define $Z_t = X_t - Y_t$. Then:

$$
Z_t = \int_0^t [b(s, X_s) - b(s, Y_s)]\,ds + \int_0^t [\sigma(s, X_s) - \sigma(s, Y_s)]\,dW_s
$$

Taking expectations of $|Z_t|^2$ and using the Lipschitz condition:

$$
\mathbb{E}[|Z_t|^2] \leq C \int_0^t \mathbb{E}[|Z_s|^2]\,ds
$$

By Gronwall's inequality with $Z_0 = 0$: $\mathbb{E}[|Z_t|^2] = 0$ for all $t$.

### Examples of Lipschitz Coefficients

**Example 1: Linear SDE**

$$
dX_t = (a + bX_t)\,dt + (c + dX_t)\,dW_t
$$

Lipschitz constant: $K = |b| + |d|$.

**Example 2: Ornstein-Uhlenbeck**

$$
dX_t = -\kappa X_t\,dt + \sigma\,dW_t
$$

Lipschitz constant: $K = \kappa$.

**Example 3: Bounded derivatives**

If $b$ and $\sigma$ are $C^1$ in $x$ with bounded derivatives, they are globally Lipschitz.

### Non-Lipschitz Examples

**Example 4: Square root (CIR model)**

$$
dX_t = \kappa(\theta - X_t)\,dt + \sigma\sqrt{X_t}\,dW_t
$$

The diffusion coefficient $\sigma\sqrt{x}$ is **not Lipschitz** at $x = 0$ since $|\sqrt{x} - \sqrt{y}|/|x-y| \to \infty$ as $x, y \to 0$.

**However**, this SDE still has a unique solution! (Yamada-Watanabe theory applies.)

**Example 5: Power growth**

$$
dX_t = X_t^2\,dt + dW_t
$$

The drift $b(x) = x^2$ is not globally Lipschitz (grows too fast). This can lead to explosion in finite time.

---

## The Linear Growth Condition

### Definition

The coefficients satisfy the **linear growth condition** if there exists $K > 0$ such that for all $t \in [0,T]$ and $x \in \mathbb{R}^d$:

$$
\boxed{
|b(t,x)|^2 + |\sigma(t,x)|^2 \leq K^2(1 + |x|^2)
}
$$

Equivalently: $|b(t,x)| + |\sigma(t,x)| \leq K(1 + |x|)$.

### Interpretation

The coefficients grow **at most linearly** in $|x|$. This prevents the solution from "exploding to infinity" in finite time.

### Why Linear Growth Prevents Explosion

**Heuristic**: If $|b(x)| \sim |x|^p$ with $p > 1$, the ODE $\dot{x} = x^p$ explodes in finite time:

$$
x(t) = \frac{x_0}{(1 - (p-1)x_0^{p-1}t)^{1/(p-1)}} \to \infty \quad \text{as } t \to t^* = \frac{1}{(p-1)x_0^{p-1}}
$$

Linear growth ($p = 1$) gives exponential growth, which is finite for all finite times.

**Formal**: Linear growth ensures $\mathbb{E}[\sup_{0 \leq t \leq T} |X_t|^2] < \infty$.

### Examples

**Linear growth satisfied**:

- $b(x) = \sin(x)$ (bounded, hence linear growth)
- $b(x) = x$ (exactly linear)
- $\sigma(x) = 1 + |x|^{1/2}$ (sublinear)

**Linear growth violated**:

- $b(x) = x^2$ (quadratic growth)
- $\sigma(x) = e^x$ (exponential growth)

---

## The Main Existence and Uniqueness Theorem

**Theorem (Itô)**: Let $b: [0,T] \times \mathbb{R}^d \to \mathbb{R}^d$ and $\sigma: [0,T] \times \mathbb{R}^d \to \mathbb{R}^{d \times m}$ be measurable functions satisfying:

1. **(Lipschitz)**: $|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K|x - y|$

2. **(Linear growth)**: $|b(t,x)|^2 + |\sigma(t,x)|^2 \leq K^2(1 + |x|^2)$

Then for any initial condition $X_0 = x_0 \in \mathbb{R}^d$:

$$
\boxed{
\text{There exists a unique strong solution } X_t \text{ on } [0, T]
}
$$

Moreover, the solution satisfies:

$$
\mathbb{E}\left[\sup_{0 \leq t \leq T} |X_t|^2\right] \leq C(1 + |x_0|^2)e^{CT}
$$

---

## Proof Strategy: Picard Iteration

The proof uses **Picard iteration** (successive approximations), analogous to the ODE case.

### Step 1: Define the Iteration

$$
X_t^{(0)} = x_0
$$

$$
X_t^{(n+1)} = x_0 + \int_0^t b(s, X_s^{(n)})\,ds + \int_0^t \sigma(s, X_s^{(n)})\,dW_s
$$

### Step 2: Show Convergence

Define $e_n(t) = \mathbb{E}[\sup_{0 \leq s \leq t} |X_s^{(n+1)} - X_s^{(n)}|^2]$.

Using Lipschitz + Itô isometry + Doob's inequality:

$$
e_n(t) \leq C \int_0^t e_{n-1}(s)\,ds
$$

By induction: $e_n(t) \leq \frac{(Ct)^n}{n!} e_0(T)$.

Since $\sum_n \sqrt{e_n(T)} < \infty$, the sequence converges uniformly in $L^2$.

### Step 3: Verify the Limit Solves the SDE

Pass to the limit in the integral equation using dominated convergence.

### Step 4: Prove Uniqueness

If $X_t$ and $Y_t$ are two solutions, Gronwall's inequality shows $X_t = Y_t$ a.s.

---

## Local Lipschitz Conditions

### Definition

The coefficients are **locally Lipschitz** if for every $R > 0$, there exists $K_R > 0$ such that:

$$
|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K_R|x - y| \quad \text{for } |x|, |y| \leq R
$$

### Theorem (Local Existence)

Under local Lipschitz + linear growth: there exists a unique solution up to a possible **explosion time**:

$$
\tau_\infty = \lim_{n \to \infty} \tau_n, \quad \tau_n = \inf\{t : |X_t| \geq n\}
$$

If $\mathbb{P}(\tau_\infty = \infty) = 1$, the solution is global.

**Linear growth ensures** $\tau_\infty = \infty$ a.s.

---

## Beyond Lipschitz: Yamada-Watanabe Conditions

For some SDEs with non-Lipschitz coefficients, weaker conditions suffice.

### Yamada-Watanabe Theorem

Consider the one-dimensional SDE:

$$
dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t
$$

**Pathwise uniqueness** holds if:

1. $|b(x) - b(y)| \leq K|x - y|$ (Lipschitz drift)

2. $|\sigma(x) - \sigma(y)| \leq \rho(|x - y|)$ where $\int_0^\epsilon \rho^{-2}(u)\,du = \infty$

**Example**: $\sigma(x) = |x|^\alpha$ with $\alpha \geq 1/2$ satisfies this with $\rho(u) = u^\alpha$.

This explains why the **CIR model** ($\sigma(x) = \sigma\sqrt{x}$, so $\alpha = 1/2$) has a unique solution despite non-Lipschitz diffusion.

---

## Summary of Conditions

| Condition | Ensures | Formula |
|-----------|---------|---------|
| **Lipschitz** | Uniqueness | $\|b(x) - b(y)\| + \|\sigma(x) - \sigma(y)\| \leq K\|x-y\|$ |
| **Linear growth** | No explosion | $\|b(x)\|^2 + \|\sigma(x)\|^2 \leq K^2(1 + \|x\|^2)$ |
| **Local Lipschitz** | Local uniqueness | Lipschitz on bounded sets |
| **Yamada-Watanabe** | Uniqueness for non-Lipschitz $\sigma$ | $\int_0^\epsilon \rho^{-2}(u)\,du = \infty$ |

---

## Practical Checklist

Given an SDE $dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t$:

1. **Check Lipschitz**: Are $b$ and $\sigma$ Lipschitz continuous?
   - Yes → Uniqueness guaranteed
   - No → Check Yamada-Watanabe or other conditions

2. **Check linear growth**: Do $|b(x)|$ and $|\sigma(x)|$ grow at most linearly?
   - Yes → No explosion, global solution exists
   - No → May have finite-time explosion

3. **Standard models**:
   - GBM, Vasicek, OU: Lipschitz + linear growth ✓
   - CIR: Non-Lipschitz but Yamada-Watanabe ✓
   - $dX = X^2\,dt + dW$: May explode ✗

$$
\boxed{
\text{Lipschitz} + \text{Linear Growth} \Longrightarrow \text{Unique Global Solution}
}
$$
