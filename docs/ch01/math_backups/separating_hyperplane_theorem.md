# The Separating Hyperplane Theorem

The **Separating Hyperplane Theorem** is a fundamental result in **convex analysis** that formalizes the geometric intuition: if two disjoint convex sets exist, you can "draw a line (or hyperplane) between them" that separates them.

This theorem is the bridge between **geometry** and **duality theory**, and it's essential for proving the FTAP, optimization theory (Lagrange multipliers, KKT conditions), and game theory (minimax theorems).

## Statement of the Theorem

### Version 1: Separating Hyperplane Theorem (Basic)

**Theorem:** Let $C$ and $D$ be non-empty, disjoint convex sets in $\mathbb{R}^n$ (i.e., $C \cap D = \emptyset$). If at least one of them is **open**, then there exists a non-zero vector $p \in \mathbb{R}^n$ and a scalar $\alpha \in \mathbb{R}$ such that:

$$p^T x \leq \alpha \quad \text{for all } x \in C$$
$$p^T x \geq \alpha \quad \text{for all } x \in D$$

The hyperplane $H = \{x \in \mathbb{R}^n : p^T x = \alpha\}$ **separates** $C$ and $D$.

### Version 2: Strict Separation

**Theorem:** If $C$ is a non-empty, **closed** convex set and $D$ is a non-empty, **compact** convex set with $C \cap D = \emptyset$, then there exists a **strict separation**: there exist $p \in \mathbb{R}^n$ and $\alpha, \beta \in \mathbb{R}$ with $\alpha < \beta$ such that:

$$p^T x \leq \alpha < \beta \leq p^T y \quad \text{for all } x \in C, y \in D$$

This is a **strong separation** with a "gap" between the sets.

### Version 3: Supporting Hyperplane Theorem

**Theorem:** Let $C$ be a non-empty convex set in $\mathbb{R}^n$ and let $x_0 \in \partial C$ (boundary of $C$). Then there exists a non-zero vector $p \in \mathbb{R}^n$ such that:

$$p^T x_0 = \sup_{x \in C} p^T x$$

The hyperplane $H = \{x : p^T x = p^T x_0\}$ is called a **supporting hyperplane** at $x_0$.

## Proof (Finite Dimensional Case)

I'll prove Version 1 in detail. The key is to reduce it to the case of separating a convex set from a point.

### Lemma: Separation of a Point from a Closed Convex Set

**Lemma:** Let $C \subset \mathbb{R}^n$ be a non-empty, closed convex set, and let $y \notin C$. Then there exists $p \in \mathbb{R}^n$ with $p \neq 0$ such that:

$$p^T x < p^T y \quad \text{for all } x \in C$$

**Proof of Lemma:**

**Step 1:** Find the closest point in $C$ to $y$.

Since $C$ is closed and convex, there exists a unique point $x_0 \in C$ such that:
$$\|x_0 - y\| = \inf_{x \in C} \|x - y\| = d(y, C)$$

This follows from the fact that the function $x \mapsto \|x - y\|^2$ is strictly convex and coercive on the closed convex set $C$.

**Step 2:** Define the separating direction.

Let $p = y - x_0$. Note that $p \neq 0$ since $y \notin C$.

**Step 3:** Show $p$ separates $C$ and $\{y\}$.

For any $x \in C$, we need to show:
$$p^T x < p^T y$$

Equivalently:
$$(y - x_0)^T x < (y - x_0)^T y$$
$$(y - x_0)^T (x - y) < 0$$
$$(y - x_0)^T (x - x_0) < (y - x_0)^T (y - x_0)$$

**Step 4:** Use the minimality of $x_0$.

Since $x_0$ minimizes $\|x - y\|$ over $C$, for any $x \in C$ and $\lambda \in [0, 1]$, the point $x_\lambda = x_0 + \lambda(x - x_0) \in C$ (by convexity).

The function:
$$f(\lambda) = \|x_0 + \lambda(x - x_0) - y\|^2 = \|x_0 - y + \lambda(x - x_0)\|^2$$

achieves its minimum over $[0, 1]$ at $\lambda = 0$.

Therefore, $f'(0) \geq 0$:
$$f'(\lambda) = 2(x_0 - y + \lambda(x - x_0))^T(x - x_0)$$
$$f'(0) = 2(x_0 - y)^T(x - x_0) \geq 0$$
$$(y - x_0)^T(x - x_0) \leq 0$$

**Step 5:** Show strict inequality.

We have:
$$\|x_\lambda - y\|^2 = \|x_0 - y\|^2 + 2\lambda(x_0 - y)^T(x - x_0) + \lambda^2\|x - x_0\|^2$$

If $(y - x_0)^T(x - x_0) = 0$ for some $x \in C$ with $x \neq x_0$, then for small $\lambda > 0$:
$$\|x_\lambda - y\|^2 = \|x_0 - y\|^2 + \lambda^2\|x - x_0\|^2 > \|x_0 - y\|^2$$

Wait, this would contradict minimality only if we can choose $\lambda$ to decrease the distance. Let me reconsider.

Actually, if $(y - x_0)^T(x - x_0) = 0$, we need to be more careful. But notice:

$$\|x - y\|^2 = \|x - x_0 + x_0 - y\|^2 = \|x - x_0\|^2 + 2(x - x_0)^T(x_0 - y) + \|x_0 - y\|^2$$

Since $(x - x_0)^T(x_0 - y) \geq 0$ (from our calculation), if $x \neq x_0$, then:
$$\|x - y\|^2 \geq \|x_0\|^2 + \|x - x_0\|^2 > \|x_0 - y\|^2$$

This uses the fact that if $(x - x_0)^T(x_0 - y) = 0$ and $x \neq x_0$, the vectors are orthogonal, so we get strict inequality.

Therefore:
$$(y - x_0)^T(x - x_0) < (y - x_0)^T(y - x_0)$$

which gives us:
$$p^T x < p^T y$$

$\square$

### Proof of Main Theorem (Version 1)

Let $C$ and $D$ be disjoint convex sets with $D$ open.

**Step 1:** Form the Minkowski difference.

Define:
$$E = C - D = \{c - d : c \in C, d \in D\}$$

**Claim:** $E$ is convex, open, and $0 \notin E$.

- **Convex:** If $e_1 = c_1 - d_1 \in E$ and $e_2 = c_2 - d_2 \in E$, then for $\lambda \in [0,1]$:
$$\lambda e_1 + (1-\lambda)e_2 = [\lambda c_1 + (1-\lambda)c_2] - [\lambda d_1 + (1-\lambda)d_2] \in C - D = E$$

- **Open:** Since $D$ is open and translation/scaling preserve openness, $C - D$ is open. (For any $c - d \in E$, there's a ball around $d$ in $D$, so a ball around $c - d$ in $E$.)

- **$0 \notin E$:** If $0 \in E$, then $c = d$ for some $c \in C, d \in D$, contradicting $C \cap D = \emptyset$.

**Step 2:** Take closure and apply the lemma.

Let $\bar{E}$ be the closure of $E$. Then $\bar{E}$ is closed and convex, and $0 \notin E$ means $0 \notin \bar{E}$ (since $E$ is open and doesn't contain $0$).

By the lemma, there exists $p \neq 0$ such that:
$$p^T e \leq 0 \quad \text{for all } e \in \bar{E}$$

Actually, we need strict inequality for points in $E$. Since $E$ is open and $0 \notin E$, we can get:
$$p^T e < p^T 0 = 0 \quad \text{for all } e \in E$$

**Step 3:** Translate back to $C$ and $D$.

For any $c \in C$ and $d \in D$, we have $c - d \in E$, so:
$$p^T(c - d) < 0$$
$$p^T c < p^T d$$

This holds for all $c \in C$ and $d \in D$.

Let:
$$\alpha = \sup_{c \in C} p^T c, \quad \beta = \inf_{d \in D} p^T d$$

We've shown $\alpha \leq \beta$. In fact, since $D$ is open, we can get $\alpha < \beta$ for strict separation, but the weak version $\alpha \leq \beta$ suffices for basic separation.

Therefore, the hyperplane $\{x : p^T x = \alpha\}$ separates $C$ and $D$. $\square$

## Geometric Intuition

### 1. **The Hyperplane as a "Fence"**

Imagine two disjoint convex shapes in 3D space (say, two convex polyhedra). The theorem guarantees you can place a flat plane between them so that one shape is entirely on one side and the other shape is entirely on the other side.

The vector $p$ is the **normal vector** to the hyperplane—it points "perpendicular" to the separating plane.

### 2. **Why Convexity Matters**

Consider two non-convex sets:

```
  C:  ( )    D:  ( )
       |          |
```

If they "wrap around" each other, no straight line can separate them. Convexity ensures the sets are "blob-like"—no weird indentations or wrapping.

### 3. **Supporting Hyperplanes**

At any boundary point of a convex set, you can place a hyperplane that "touches" the set at that point but doesn't penetrate it. This is like placing a table (hyperplane) under a convex object—it supports it at a point.

### 4. **Dual Interpretation**

The separating vector $p$ defines a **linear functional** $f(x) = p^T x$.

The theorem says: if $C$ and $D$ are disjoint and convex, there exists a linear functional such that:
- $f$ is "small" on $C$
- $f$ is "large" on $D$

This connects geometry to **functional analysis**.

## The Hahn-Banach Theorem (Infinite Dimensions)

In infinite-dimensional spaces, we need the **Hahn-Banach theorem**, which generalizes the separating hyperplane theorem.

### Hahn-Banach Theorem (Analytic Form)

**Theorem:** Let $X$ be a real vector space, $Y \subset X$ a linear subspace, and $p: X \to \mathbb{R}$ a sublinear functional (i.e., $p(\lambda x) = \lambda p(x)$ for $\lambda \geq 0$ and $p(x + y) \leq p(x) + p(y)$).

If $f: Y \to \mathbb{R}$ is a linear functional with $f(y) \leq p(y)$ for all $y \in Y$, then there exists a linear extension $F: X \to \mathbb{R}$ such that:
1. $F(y) = f(y)$ for all $y \in Y$
2. $F(x) \leq p(x)$ for all $x \in X$

### Hahn-Banach Theorem (Geometric Form)

**Theorem:** Let $X$ be a normed vector space, and let $C, D \subset X$ be non-empty convex sets with $C \cap D = \emptyset$.

1. If $C$ is open, there exists a continuous linear functional $\phi \in X^*$ and $\alpha \in \mathbb{R}$ such that:
$$\phi(c) < \alpha \leq \phi(d) \quad \text{for all } c \in C, d \in D$$

2. If $C$ is closed and $D$ is compact, there exists **strict separation**.

The proof uses the **axiom of choice** (via Zorn's lemma) to extend linear functionals.

## Connection to the FTAP

Now let's see how this applies to the Fundamental Theorem of Asset Pricing.

### Setup

Recall the finite state space model:
- States: $\Omega = \{\omega_1, \ldots, \omega_n\}$
- Assets: $j = 1, \ldots, d$
- Payoff matrix: $X$ where $X_{ij} = S^j_1(\omega_i) - S^j_0$

**Key sets:**

1. **Attainable payoffs** starting from zero wealth:
$$\mathcal{C} = \{X\theta : \theta \in \mathbb{R}^d\} \subset \mathbb{R}^n$$
This is the column space of $X$.

2. **Positive orthant:**
$$\mathbb{R}^n_+ = \{v \in \mathbb{R}^n : v_i \geq 0 \text{ for all } i\}$$

**No arbitrage condition:**
$$\mathcal{C} \cap \mathbb{R}^n_+ = \{0\}$$

(No portfolio with zero initial cost has non-negative payoff everywhere and positive payoff somewhere.)

### Applying the Separating Hyperplane Theorem

Since $\mathcal{C}$ is a linear subspace (hence convex and closed) and $\mathbb{R}^n_{++} = \{v : v_i > 0\}$ is an open convex cone, and they're disjoint (by no-arbitrage), the separating hyperplane theorem gives us a vector $q \in \mathbb{R}^n$ with $q \neq 0$ such that:

$$q^T (X\theta) \leq 0 \quad \text{for all } \theta \in \mathbb{R}^d$$
$$q^T v > 0 \quad \text{for all } v \in \mathbb{R}^n_{++}$$

The second condition implies $q_i > 0$ for all $i$ (take $v = e_i$, the $i$-th standard basis vector).

The first condition, holding for all $\theta$, implies:
$$X^T q = 0$$

This means:
$$\sum_{i=1}^n q_i X_{ij} = 0 \quad \text{for all } j$$

Or equivalently:
$$\sum_{i=1}^n q_i (S^j_1(\omega_i) - S^j_0) = 0$$
$$\sum_{i=1}^n q_i S^j_1(\omega_i) = S^j_0 \sum_{i=1}^n q_i$$

Normalizing $\mathbb{Q}(\omega_i) = q_i / \sum_k q_k$, we get:
$$\mathbb{E}^{\mathbb{Q}}[S^j_1] = S^j_0$$

This is exactly the **equivalent martingale measure**!

### The Geometric Picture

- $\mathcal{C}$ = achievable payoffs = hyperplane through origin
- $\mathbb{R}^n_+$ = non-negative payoffs = positive cone
- No arbitrage = these don't intersect (except at origin)
- Separating hyperplane = probability vector $q$ that prices all assets correctly
- The dual space interpretation: $q$ is a "state-price density" or "pricing kernel"

## Additional Theorems and Variants

### Minkowski's Theorem (Alternative Form)

**Theorem:** Two non-empty convex sets $C, D \subset \mathbb{R}^n$ can be strictly separated if and only if their **relative interiors** are disjoint.

The relative interior $\text{ri}(C)$ is the interior of $C$ relative to its affine hull.

### Farkas' Lemma (Finite Dimensional)

**Lemma:** Let $A$ be an $m \times n$ matrix and $b \in \mathbb{R}^m$. Exactly one of the following holds:
1. There exists $x \in \mathbb{R}^n$ with $x \geq 0$ and $Ax = b$
2. There exists $y \in \mathbb{R}^m$ with $A^T y \geq 0$ and $b^T y < 0$

This is the **linear programming** version of the separating hyperplane theorem.

**Proof sketch:** Statement 1 says $b \in \text{cone}(A)$ (the cone generated by columns of $A$). Statement 2 says there exists a hyperplane through the origin that separates $b$ from $\text{cone}(A)$. By the separating hyperplane theorem, exactly one can be true.

### Krein-Milman Theorem

**Theorem:** Every non-empty compact convex set in a locally convex topological vector space is the **closed convex hull** of its extreme points.

This is used in optimization theory and economics (e.g., representing mixed strategies as convex combinations of pure strategies).

## Visualization in $\mathbb{R}^2$ and $\mathbb{R}^3$

### Example 1: Two Disjoint Disks in $\mathbb{R}^2$

Let $C = \{x : \|x - (0, 0)\| \leq 1\}$ and $D = \{x : \|x - (3, 0)\| \leq 1\}$.

The separating line is $x_1 = 1.5$ (vertical line), with normal vector $p = (1, 0)$.

We have:
- $p^T x \leq 1.5$ for all $x \in C$
- $p^T x \geq 1.5$ for all $x \in D$

### Example 2: Cone and Point in $\mathbb{R}^3$

Let $C = \{(x, y, z) : z \geq \sqrt{x^2 + y^2}\}$ (upward cone) and consider the point $(-1, 0, 0) \notin C$.

The supporting hyperplane at the closest point on the cone boundary has normal vector pointing toward $(-1, 0, 0)$.

The separating plane would have equation $p_1 x_1 + p_2 x_2 + p_3 x_3 = \alpha$ for appropriate $p$ and $\alpha$.

## Summary

The separating hyperplane theorem is fundamental because it:

1. **Connects geometry and analysis:** Convex sets (geometric) $\leftrightarrow$ Linear functionals (analytic)

2. **Enables duality theory:** Every "feasibility" question has a "dual" characterization via separating functionals

3. **Underlies optimization:** Lagrange multipliers, KKT conditions, linear programming duality all use separating hyperplanes

4. **Proves the FTAP:** No-arbitrage (geometric condition on payoff cones) $\leftrightarrow$ Existence of EMM (separating functional = state prices)

5. **Generalizes broadly:** From $\mathbb{R}^n$ to Banach spaces via Hahn-Banach, maintaining the same intuition

The key insight: **If two "blob-like" (convex) sets don't touch, you can always slide a flat surface (hyperplane) between them.** This simple geometric idea has profound implications across mathematics, economics, and finance.

Would you like me to continue with the **Consumption-Based Asset Pricing** derivation of the Black-Scholes PDE?