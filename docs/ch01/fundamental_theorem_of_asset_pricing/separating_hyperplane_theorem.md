# The Separating Hyperplane Theorem


The **Separating Hyperplane Theorem** is a fundamental result in convex analysis that formalizes a basic geometric intuition: two disjoint convex sets can always be separated by a hyperplane. This seemingly simple observation has far-reaching consequences. It is the mathematical engine behind the proof of the [Fundamental Theorem of Asset Pricing](fundamental_theorem_of_asset_pricing.md), and it underpins Lagrange duality, KKT conditions, linear programming duality, and minimax theorems in game theory.

This page states the three main versions of the theorem (weak separation, strict separation, and supporting hyperplanes), gives complete proofs of the first two, and develops the connection to the FTAP in detail.


## Statements of the Theorem


### Weak Separation

**Theorem 1 (Separating Hyperplane Theorem).**
*Let $C, D \subset \mathbb{R}^n$ be non-empty disjoint convex sets. Then there exists a non-zero vector $p \in \mathbb{R}^n$ and a scalar $\alpha \in \mathbb{R}$ such that*

$$p^T x \leq \alpha \quad \text{for all } x \in C, \qquad p^T x \geq \alpha \quad \text{for all } x \in D$$

The hyperplane $H = \{x \in \mathbb{R}^n : p^T x = \alpha\}$ **separates** $C$ and $D$, with $C$ on one side and $D$ on the other.

!!! warning "Weak separation allows contact"
    Weak separation permits $p^T x = \alpha$ for points in both $C$ and $D$ simultaneously. The sets may "touch" the hyperplane on the same side. This version requires no topological assumptions (neither openness nor closedness) beyond convexity and disjointness.


### Strict Separation

**Theorem 2 (Strict Separating Hyperplane Theorem).**
*Let $C \subset \mathbb{R}^n$ be a non-empty closed convex set and $D \subset \mathbb{R}^n$ a non-empty compact convex set, with $C \cap D = \emptyset$. Then there exists $p \in \mathbb{R}^n$ with $p \neq 0$ and scalars $\alpha < \beta$ such that*

$$p^T x \leq \alpha < \beta \leq p^T y \qquad \text{for all } x \in C, \; y \in D$$

There is a positive gap between the two sets: no point of either set lies within the open strip $\{x : \alpha < p^T x < \beta\}$.

!!! note "Why both closed and compact?"
    Closedness of $C$ and compactness of $D$ are essential. Two closed convex sets that are merely closed (but neither is compact) can be disjoint yet asymptotically approach each other, making strict separation impossible. A standard counterexample: $C = \{(x,y) : y \leq 0\}$ and $D = \{(x,y) : xy \geq 1, \; x > 0\}$ are closed, convex, and disjoint, but $\inf_{c \in C, d \in D} \|c - d\| = 0$.


### Supporting Hyperplane

**Theorem 3 (Supporting Hyperplane Theorem).**
*Let $C \subset \mathbb{R}^n$ be a non-empty convex set with non-empty interior, and let $x_0 \in \partial C$ (the boundary of $C$). Then there exists a non-zero vector $p \in \mathbb{R}^n$ such that*

$$p^T x \leq p^T x_0 \qquad \text{for all } x \in C$$

The hyperplane $H = \{x : p^T x = p^T x_0\}$ is called a **supporting hyperplane** to $C$ at $x_0$. It "touches" the boundary without penetrating the interior.


## Proof of Strict Separation (Theorem 2)


We prove Theorem 2, which is the version used in the FTAP. The proof proceeds in two stages: first we establish a key lemma about separating a point from a closed convex set, then we extend to two sets.


### Lemma: Separation of a Point from a Closed Convex Set

**Lemma.**
*Let $C \subset \mathbb{R}^n$ be a non-empty closed convex set, and let $y \notin C$. Then there exists a non-zero $p \in \mathbb{R}^n$ and a scalar $\gamma$ such that*

$$p^T x < \gamma < p^T y \qquad \text{for all } x \in C$$

**Proof.**

**Step 1: Existence of a nearest point.**
Since $C$ is closed, the continuous function $x \mapsto \|x - y\|^2$ attains its infimum on $C$. Since it is also strictly convex, the minimizer is unique. Denote it $x_0 \in C$:

$$\|x_0 - y\| = \inf_{x \in C} \|x - y\| = d(y, C) > 0$$

The strict positivity $d(y, C) > 0$ follows from $y \notin C$ and $C$ closed.

**Step 2: Define the separating direction.**
Set $p = y - x_0 \neq 0$ and $\gamma = p^T x_0 + \frac{1}{2}\|p\|^2 = \frac{1}{2}(p^T x_0 + p^T y)$, which is the midpoint value.

**Step 3: Establish the key inequality $(y - x_0)^T(x - x_0) \leq 0$ for all $x \in C$.**

For any $x \in C$ and $\lambda \in [0, 1]$, the point $x_\lambda = (1 - \lambda)x_0 + \lambda x$ lies in $C$ by convexity. Define

$$f(\lambda) = \|x_\lambda - y\|^2 = \|(x_0 - y) + \lambda(x - x_0)\|^2$$

Since $x_0$ is the minimizer, $f$ attains its minimum on $[0,1]$ at $\lambda = 0$. Therefore $f'(0) \geq 0$:

$$f'(\lambda) = 2\bigl((x_0 - y) + \lambda(x - x_0)\bigr)^T(x - x_0)$$

$$f'(0) = 2(x_0 - y)^T(x - x_0) \geq 0$$

Rearranging:

$$(y - x_0)^T(x - x_0) \leq 0 \qquad \text{for all } x \in C$$

**Step 4: Deduce strict separation.**

Using the inequality from Step 3:

$$p^T x = (y - x_0)^T x = (y - x_0)^T(x - x_0) + (y - x_0)^T x_0 \leq 0 + p^T x_0 = p^T x_0$$

Meanwhile:

$$p^T y = (y - x_0)^T y = (y - x_0)^T(y - x_0) + (y - x_0)^T x_0 = \|p\|^2 + p^T x_0$$

So for every $x \in C$:

$$p^T x \leq p^T x_0 < p^T x_0 + \|p\|^2 = p^T y$$

where the strict inequality holds because $\|p\|^2 > 0$. The midpoint $\gamma = p^T x_0 + \frac{1}{2}\|p\|^2$ satisfies $p^T x \leq p^T x_0 < \gamma < p^T y$ for all $x \in C$. $\square$


### Proof of Theorem 2

**Proof.**
Let $C$ be closed convex and $D$ be compact convex with $C \cap D = \emptyset$.

**Step 1: Reduce to separating a point from a closed convex set.**

Define the **Minkowski difference**:

$$E = C - D = \{c - d : c \in C, \; d \in D\}$$

Since $C \cap D = \emptyset$, we have $0 \notin E$. The set $E$ is convex (as the Minkowski sum of two convex sets). We claim $E$ is closed. To see this, let $e_k = c_k - d_k \to e$ with $c_k \in C$, $d_k \in D$. Since $D$ is compact, $d_k$ has a convergent subsequence $d_{k_j} \to d \in D$. Then $c_{k_j} = e_{k_j} + d_{k_j} \to e + d$. Since $C$ is closed, $e + d \in C$, so $e = (e + d) - d \in C - D = E$.

Therefore $E$ is a non-empty closed convex set with $0 \notin E$.

**Step 2: Apply the lemma.**

By the lemma (with $y = 0$ and the set $E$), there exist $p \neq 0$ and $\delta > 0$ such that

$$p^T e < -\delta < 0 \qquad \text{for all } e \in E$$

More precisely, since $0 \notin E$ and $E$ is closed, the lemma gives $p^T e \leq p^T x_0 < 0$ where $x_0$ is the nearest point of $E$ to the origin. Setting $\delta = -p^T x_0 > 0$ would give $p^T e \leq -\delta$ for all $e \in E$.

**Step 3: Translate back to $C$ and $D$.**

For all $c \in C$ and $d \in D$, since $c - d \in E$:

$$p^T c - p^T d = p^T(c - d) \leq -\delta < 0$$

Therefore $p^T c + \delta \leq p^T d$ for all $c \in C$, $d \in D$. Setting

$$\alpha = \sup_{c \in C} p^T c, \qquad \beta = \inf_{d \in D} p^T d$$

we get $\alpha + \delta \leq \beta$, so $\alpha < \beta$, and the hyperplanes $p^T x = \alpha$ and $p^T x = \beta$ strictly separate $C$ and $D$. $\square$


## Proof of Weak Separation (Theorem 1)


We now prove the most general finite-dimensional version.

**Proof.**
Let $C, D \subset \mathbb{R}^n$ be non-empty disjoint convex sets.

**Step 1: Minkowski difference.**

Define $E = C - D$. Then $E$ is convex and $0 \notin E$ (since $C \cap D = \emptyset$).

**Step 2: Separate the origin from $\overline{E}$.**

The closure $\overline{E}$ is a closed convex set. There are two cases.

*Case 1: $0 \notin \overline{E}$.* Apply the lemma to $\overline{E}$ and $y = 0$: there exists $p \neq 0$ with $p^T e \leq p^T x_0 < 0$ for all $e \in \overline{E}$, hence $p^T(c - d) < 0$ for all $c \in C$, $d \in D$, which gives $p^T c < p^T d$. Setting $\alpha = \sup_C p^T c$ yields the desired separation.

*Case 2: $0 \in \overline{E} \setminus E$.* The origin lies on the boundary of $\overline{E}$. Since $\overline{E}$ has $0 \in \partial \overline{E}$, by the supporting hyperplane theorem (Theorem 3, which can be proved independently using a limiting argument), there exists $p \neq 0$ with $p^T e \leq p^T 0 = 0$ for all $e \in \overline{E}$. In particular $p^T(c - d) \leq 0$ for all $c \in C$, $d \in D$, giving $p^T c \leq p^T d$. Setting $\alpha = \sup_C p^T c$ gives weak separation. $\square$

!!! note "Open set refinement"
    If one of the sets (say $D$) is **open**, the separation can be made one-sided strict: $p^T c \leq \alpha < p^T d$ for all $c \in C$, $d \in D$. This is because $D$ open implies $p^T d > \inf_{d' \in D} p^T d'$ is achievable strictly. This refinement is used in some formulations of the FTAP proof.


## Geometric Intuition


**The hyperplane as a barrier.** Two disjoint convex sets in $\mathbb{R}^3$ (say, two convex polyhedra) can always be separated by a flat plane placed between them, with one set entirely on each side. The vector $p$ is the normal to this plane—it indicates the "direction of separation."

**Why convexity is essential.** Non-convex sets can interlock or wrap around each other so that no hyperplane separates them. Consider two interlocking crescents: each is path-connected but non-convex, and no straight line separates them. Convexity prevents such interleaving.

**Supporting hyperplanes as tangent planes.** At any boundary point of a convex set, a hyperplane can be placed that touches the boundary without penetrating the interior. This is the convex-analysis analogue of a tangent plane: the hyperplane "supports" the set from outside.

**Dual interpretation.** The separating vector $p$ defines a linear functional $\ell(x) = p^T x$. Separation says $\ell$ is bounded above on $C$ and bounded below on $D$, with the bounds consistent. This connects geometry (convex sets) to functional analysis (linear functionals), a bridge that becomes essential in infinite dimensions.


## The Hahn–Banach Theorem and Infinite Dimensions


The proofs above rely on the existence of nearest points in closed convex sets, a property that holds in $\mathbb{R}^n$ but fails in general infinite-dimensional spaces. The appropriate generalization is the **Hahn–Banach theorem**.

### Analytic Form

**Theorem (Hahn–Banach, analytic version).**
*Let $X$ be a real vector space, $Y \subset X$ a linear subspace, and $p : X \to \mathbb{R}$ a sublinear functional (positive homogeneous and subadditive). If $f : Y \to \mathbb{R}$ is linear with $f(y) \leq p(y)$ for all $y \in Y$, then there exists a linear extension $F : X \to \mathbb{R}$ satisfying $F|_Y = f$ and $F(x) \leq p(x)$ for all $x \in X$.*

The proof uses Zorn's lemma (equivalently, the axiom of choice) to extend $f$ one dimension at a time.

### Geometric Form

**Theorem (Hahn–Banach, geometric version).**
*Let $X$ be a topological vector space and $C, D \subset X$ non-empty disjoint convex sets.*

1. *If $C$ is open, there exists a continuous linear functional $\phi \in X^*$ and $\alpha \in \mathbb{R}$ with $\phi(c) < \alpha \leq \phi(d)$ for all $c \in C$, $d \in D$.*

2. *If $C$ is closed and $D$ is compact, there exists strict separation: $\phi(c) \leq \alpha < \beta \leq \phi(d)$ for all $c \in C$, $d \in D$.*

This is the infinite-dimensional counterpart of Theorems 1 and 2. In applications to the FTAP, the relevant spaces are $L^p$ or $L^\infty$ function spaces.

### The Kreps–Yan Extension

For the continuous-time FTAP, the standard Hahn–Banach theorem is not quite sufficient because the positive cone in $L^\infty$ has empty interior in many topologies. The **Kreps–Yan theorem** provides the needed refinement:

**Theorem (Kreps–Yan).**
*Let $\mathcal{C}$ be a closed convex cone in $L^\infty(\Omega, \mathcal{F}, \mathbb{P})$ containing $-L^\infty_+$ (i.e., all non-positive functions). If $\mathcal{C} \cap L^\infty_+ = \{0\}$, then there exists a strictly positive $\mathbb{Q} \in L^1$ (i.e., $d\mathbb{Q}/d\mathbb{P} > 0$ a.s.) such that $\mathbb{E}^{\mathbb{Q}}[X] \leq 0$ for all $X \in \mathcal{C}$.*

This is the functional-analytic engine behind the Delbaen–Schachermayer proof of the FTAP in continuous time: the cone $\mathcal{C}$ is the set of superhedgeable claims, and $\mathbb{Q}$ is the equivalent (local) martingale measure.


## Connection to the FTAP


The separating hyperplane theorem is the core mathematical tool in the proof of the [First Fundamental Theorem of Asset Pricing](fundamental_theorem_of_asset_pricing.md). Here we spell out the connection explicitly.

### Setup

Consider the one-period finite-state model: states $\Omega = \{\omega_1, \ldots, \omega_n\}$ with $\mathbb{P}(\omega_i) > 0$, and $d$ risky assets with payoff matrix $X \in \mathbb{R}^{n \times d}$ where $X_{ij} = S^j_1(\omega_i) - S^j_0$. A portfolio $\theta \in \mathbb{R}^d$ generates the zero-cost payoff vector $X\theta \in \mathbb{R}^n$.

### The two sets

The no-arbitrage condition involves two convex subsets of $\mathbb{R}^n$:

**Set 1: Attainable payoffs.**

$$\mathcal{V} = \{X\theta : \theta \in \mathbb{R}^d\} = \operatorname{Im}(X) \subset \mathbb{R}^n$$

This is a linear subspace (hence convex and closed).

**Set 2: Strictly positive payoffs.**

$$\mathbb{R}^n_{++} = \{v \in \mathbb{R}^n : v_i > 0 \text{ for all } i\}$$

This is an open convex cone.

### No-arbitrage as disjointness

The no-arbitrage condition states that no zero-cost portfolio achieves a non-negative, non-zero payoff:

$$\mathcal{V} \cap \mathbb{R}^n_+ = \{0\}$$

Since $\mathbb{R}^n_{++} \subset \mathbb{R}^n_+ \setminus \{0\}$, this implies the stronger statement $\mathcal{V} \cap \mathbb{R}^n_{++} = \emptyset$. We now have two disjoint convex sets: the closed subspace $\mathcal{V}$ and the open cone $\mathbb{R}^n_{++}$.

### Applying the theorem

By Theorem 1 (with the open-set refinement), there exists a non-zero $q \in \mathbb{R}^n$ such that

$$q^T(X\theta) \leq 0 \quad \text{for all } \theta \in \mathbb{R}^d, \qquad q^T v > 0 \quad \text{for all } v \in \mathbb{R}^n_{++}$$

**From the first inequality** (applied to both $\theta$ and $-\theta$): since $q^T(X\theta) \leq 0$ and $q^T(X(-\theta)) = -q^T(X\theta) \leq 0$, we conclude $q^T(X\theta) = 0$ for all $\theta$. In matrix form:

$$X^T q = 0$$

**From the second inequality**: evaluating at the standard basis vectors $v = e_i \in \mathbb{R}^n_{++}$ gives $q_i = q^T e_i > 0$ for each $i$.

### Constructing the EMM

We have $q \in \mathbb{R}^n$ with $q_i > 0$ for all $i$ and $X^T q = 0$. Normalizing:

$$\mathbb{Q}(\omega_i) = \frac{q_i}{\sum_{k=1}^n q_k}$$

defines a probability measure with $\mathbb{Q} \sim \mathbb{P}$ (since $q_i > 0$ and $\mathbb{P}(\omega_i) > 0$). The condition $X^T q = 0$ expands to

$$\sum_{i=1}^n q_i\bigl(S^j_1(\omega_i) - S^j_0\bigr) = 0 \quad \text{for all } j$$

Dividing by $\sum_k q_k$:

$$\mathbb{E}^{\mathbb{Q}}[S^j_1] = S^j_0 \quad \text{for all } j$$

This is the **martingale condition**: discounted asset prices are $\mathbb{Q}$-martingales. Therefore $\mathbb{Q}$ is an equivalent martingale measure, completing the proof that no-arbitrage implies EMM existence.

### Geometric summary

The picture in $\mathbb{R}^n$ is clean:

- $\mathcal{V} = \operatorname{Im}(X)$ is a subspace through the origin (the space of achievable payoffs).
- $\mathbb{R}^n_{++}$ is the open positive orthant (desirable payoffs).
- No-arbitrage says these are disjoint.
- The separating hyperplane, defined by normal vector $q$, is a **state-price vector**: it assigns a positive "price" $q_i$ to each state $\omega_i$ such that all traded assets are fairly priced.
- After normalization, $q$ becomes a probability measure—the risk-neutral measure.

The elegance of the FTAP is that an economic condition (no free lunch) translates, via a geometric theorem (separation), into a probabilistic structure (martingale measure).


## Related Results


### Farkas' Lemma

**Lemma (Farkas).**
*Let $A \in \mathbb{R}^{m \times n}$ and $b \in \mathbb{R}^m$. Exactly one of the following systems has a solution:*

1. *$Ax = b$ with $x \geq 0$,*
2. *$A^T y \geq 0$ and $b^T y < 0$.*

This is the linear programming incarnation of the separating hyperplane theorem. Statement 1 says $b$ lies in the cone generated by the columns of $A$. Statement 2 says a hyperplane through the origin separates $b$ from that cone. The theorem of the alternative guarantees that exactly one holds. The FTAP proof can alternatively be organized using Farkas' lemma directly.

### Minkowski's Separation Theorem

**Theorem (Minkowski).**
*Two non-empty convex sets in $\mathbb{R}^n$ can be properly separated if and only if their relative interiors are disjoint.*

Here $\operatorname{ri}(C)$ denotes the interior of $C$ relative to its affine hull. This version handles lower-dimensional convex sets that have empty interior in $\mathbb{R}^n$ but non-empty relative interior.


## Summary


The separating hyperplane theorem asserts that disjoint convex sets can be separated by a hyperplane. This simple geometric principle has several precise formulations (weak, strict, supporting), each with different topological hypotheses, and generalizes to infinite dimensions via the Hahn–Banach and Kreps–Yan theorems.

For quantitative finance, its most important consequence is the proof of the FTAP: the no-arbitrage condition (disjointness of the attainable payoff subspace from the positive orthant) yields, via separation, a strictly positive pricing functional that, after normalization, becomes the equivalent martingale measure. The separating hyperplane is, in a precise sense, the mathematical embodiment of the principle that consistent prices admit a risk-neutral representation.


## References

- Rockafellar, R. T. (1970). *Convex Analysis.* Princeton University Press.

- Boyd, S. and Vandenberghe, L. (2004). *Convex Optimization.* Cambridge University Press.

- Luenberger, D. G. (1969). *Optimization by Vector Space Methods.* Wiley.

- Föllmer, H. and Schied, A. (2016). *Stochastic Finance: An Introduction in Discrete Time.* 4th edition, de Gruyter.

- Delbaen, F. and Schachermayer, W. (2006). *The Mathematics of Arbitrage.* Springer.
