# Tree Construction for Hull-White

Trinomial trees provide a lattice-based numerical method for pricing interest rate derivatives, particularly those with early exercise features where Monte Carlo methods are less natural. The Hull-White trinomial tree, introduced by Hull and White (1994), discretizes the short rate process on a recombining grid. The construction proceeds in two stages: first, build a symmetric tree for a zero-mean Ornstein-Uhlenbeck process $x_t$; second, shift each time slice to fit the initial yield curve. This section covers the first stage --- the tree geometry, node spacing, and branching probabilities.

## Zero-Mean Process

The Hull-White short rate $r_t$ satisfies $dr_t = [\theta(t) - \lambda r_t]\,dt + \sigma\,dW_t$. To separate the time-dependent drift from the stochastic dynamics, define the zero-mean process

$$
x_t = r_t - \alpha(t)
$$

where $\alpha(t)$ absorbs $\theta(t)$ and will be determined later to fit the initial curve. The process $x_t$ satisfies

$$
dx_t = -\lambda\,x_t\,dt + \sigma\,dW_t, \quad x_0 = 0
$$

The tree is first constructed for $x_t$, then shifted by $\alpha(t_i)$ at each time step $t_i$ so that $r_{ij} = \alpha_i + j\,\Delta x$ at node $(i, j)$.

## Node Spacing

The spatial step $\Delta x$ is chosen so that the trinomial tree matches the variance of $x_t$ over one time step. The conditional variance of $x_{t+\Delta t}$ given $x_t$ is

$$
\text{Var}(x_{t+\Delta t} \mid x_t) = \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda \Delta t}\right) \approx \sigma^2 \Delta t
$$

for small $\Delta t$. The standard choice for the spatial step is

$$
\Delta x = \sigma\sqrt{3\,\Delta t}
$$

This ensures that the branching probabilities remain positive and well-behaved. The factor $\sqrt{3}$ arises from matching the second moment of a trinomial distribution with three equally-spaced outcomes.

## Branching Geometry

At each node $(i, j)$, the process can move to one of three nodes at time $t_{i+1}$. The branching pattern depends on the position of node $j$ relative to the center of the grid.

**Normal branching** (used at most nodes): from node $j$, the process moves to nodes $j+1$ (up), $j$ (middle), or $j-1$ (down).

**Up branching** (used near the upper boundary): from node $j$, the process moves to nodes $j$ (up), $j-1$ (middle), or $j-2$ (down). This pattern prevents the tree from growing unboundedly.

**Down branching** (used near the lower boundary): from node $j$, the process moves to nodes $j+2$ (up), $j+1$ (middle), or $j$ (down).

The boundary between normal and non-normal branching occurs at

$$
j_{\max} = \left\lfloor \frac{0.1844}{\lambda\,\Delta t} \right\rfloor
$$

where the constant $0.1844$ is chosen to ensure positive probabilities. Equivalently, non-normal branching is used when $|j| > j_{\max}$.

## Branching Probabilities

The branching probabilities are determined by matching the first two moments and the normalization condition of the continuous-time process over one time step $\Delta t$.

For a node at position $j$ (representing $x = j\,\Delta x$), the conditional mean and variance of $x_{t+\Delta t}$ are

$$
\mathbb{E}[x_{t+\Delta t} \mid x_t = j\,\Delta x] = j\,\Delta x\,e^{-\lambda \Delta t}
$$

$$
\text{Var}(x_{t+\Delta t} \mid x_t) = \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda \Delta t}\right)
$$

Define $M = j\,\Delta x\,e^{-\lambda \Delta t}$ and $V = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda \Delta t})$.

**Normal branching** ($j \to j+1, j, j-1$): the probabilities $p_u, p_m, p_d$ satisfy

$$
\begin{cases}
p_u + p_m + p_d = 1 \\
p_u(j+1)\Delta x + p_m\,j\,\Delta x + p_d(j-1)\Delta x = M + j\,\Delta x \\
p_u(j+1)^2\Delta x^2 + p_m\,j^2\Delta x^2 + p_d(j-1)^2\Delta x^2 = V + M^2 + 2Mj\,\Delta x + j^2\Delta x^2
\end{cases}
$$

Solving, with $\eta = j\,\Delta x\,e^{-\lambda \Delta t} / \Delta x = j\,e^{-\lambda \Delta t}$ (the mean position in grid units relative to $j$):

$$
p_u = \frac{1}{6} + \frac{1}{2}\left(\eta^2\frac{\Delta x^2}{3\Delta x^2} + \eta\frac{\Delta x}{3\Delta x^2/ \Delta x}\right)
$$

More precisely, defining $\hat{\jmath} = j\,e^{-\lambda \Delta t}$ and using $\Delta x^2 = 3\sigma^2 \Delta t$:

$$
p_u = \frac{1}{6} + \frac{\hat{\jmath}^2\,\Delta x^2 + \hat{\jmath}\,\Delta x\,\Delta x}{2 \cdot 3\sigma^2\Delta t}
$$

The explicit formulas for normal branching simplify to

$$
p_u = \frac{1}{6} + \frac{(j^2 e^{-2\lambda\Delta t} - j\,e^{-\lambda\Delta t})\Delta x^2 + V}{2\Delta x^2}
$$

In practice, using the small-$\Delta t$ approximations $e^{-\lambda\Delta t} \approx 1 - \lambda\Delta t$ and $V \approx \sigma^2\Delta t$, the normal branching probabilities become

$$
p_u = \frac{1}{6} + \frac{j^2\lambda^2\Delta t^2 - j\lambda\Delta t}{2}
$$

$$
p_m = \frac{2}{3} - j^2\lambda^2\Delta t^2
$$

$$
p_d = \frac{1}{6} + \frac{j^2\lambda^2\Delta t^2 + j\lambda\Delta t}{2}
$$

!!! warning "Probability Positivity"
    The probabilities must satisfy $0 \leq p_u, p_m, p_d \leq 1$. For normal branching, this holds when $j^2\lambda^2\Delta t^2 < 2/3$, which is equivalent to $|j| < j_{\max}$. Beyond this boundary, non-normal branching must be used.

**Up branching** ($j \to j, j-1, j-2$): the moment-matching equations give

$$
p_u = \frac{7}{6} + \frac{j^2\lambda^2\Delta t^2 - 3j\lambda\Delta t}{2}
$$

$$
p_m = -\frac{1}{3} - j^2\lambda^2\Delta t^2 + 2j\lambda\Delta t
$$

$$
p_d = \frac{1}{6} + \frac{j^2\lambda^2\Delta t^2 - j\lambda\Delta t}{2}
$$

**Down branching** ($j \to j+2, j+1, j$): by symmetry with up branching,

$$
p_u = \frac{1}{6} + \frac{j^2\lambda^2\Delta t^2 + j\lambda\Delta t}{2}
$$

$$
p_m = -\frac{1}{3} - j^2\lambda^2\Delta t^2 - 2j\lambda\Delta t
$$

$$
p_d = \frac{7}{6} + \frac{j^2\lambda^2\Delta t^2 + 3j\lambda\Delta t}{2}
$$

## Recombining Property

The tree is recombining because the spatial grid is uniform: a sequence of up-middle-down moves returns to the same node regardless of the order. At time step $i$, the node index $j$ ranges from $-j_{\max,i}$ to $j_{\max,i}$, where $j_{\max,i}$ grows initially (as the process diffuses) but is bounded by the non-normal branching boundaries.

The total number of nodes at time step $i$ is at most $2j_{\max} + 1$, independent of $i$ after the initial growth phase. This keeps the tree size manageable: $O(N \cdot j_{\max})$ total nodes for $N$ time steps.

## Visualization of the Trinomial Tree

The tree structure at time step $i$ is:

```
        j_max   ●───●───●
                │ ╲ │ ╱ │
        j_max-1 ●───●───●
                │ ╲ │ ╱ │
          ...   ... ... ...
                │ ╲ │ ╱ │
       -j_max+1 ●───●───●
                │ ╲ │ ╱ │
       -j_max   ●───●───●
                t_i  t_{i+1}
```

Each node connects to three successor nodes, with the branching pattern (normal, up, or down) determined by the node's position $j$.

???+ example "Small Tree Construction"
    Consider $\lambda = 0.1$, $\sigma = 0.01$, $\Delta t = 1$. Then:

    - $\Delta x = 0.01\sqrt{3} \approx 0.01732$
    - $j_{\max} = \lfloor 0.1844 / 0.1 \rfloor = 1$
    - At each time step, nodes are at $j \in \{-1, 0, 1\}$
    - For $j = 0$ (normal branching): $p_u = p_d = 1/6$, $p_m = 2/3$
    - For $j = 1$: $\lambda\Delta t \cdot j = 0.1$, giving $p_u \approx 0.1717$, $p_m \approx 0.6567$, $p_d \approx 0.1717$

    The short rate at node $(i, j)$ is $r_{ij} = \alpha_i + j \cdot 0.01732$, where $\alpha_i$ is determined by calibration to the initial yield curve (covered in the next section).

## Summary

The Hull-White trinomial tree construction discretizes the zero-mean OU process $x_t$ on a recombining grid with spacing $\Delta x = \sigma\sqrt{3\Delta t}$. Three branching patterns (normal, up, down) ensure positive probabilities everywhere by switching to non-normal branching when $|j| > j_{\max}$. The branching probabilities are determined by matching the conditional mean and variance of the continuous-time process. The resulting tree has $O(N \cdot j_{\max})$ nodes total, where $j_{\max}$ is bounded by the mean-reversion parameter. The next section covers calibrating the shift $\alpha_i$ at each time slice to fit the initial yield curve.

---

## Exercises

**Exercise 1.** For $\lambda = 0.05$, $\sigma = 0.01$, and $\Delta t = 0.5$, compute $\Delta x$, $j_{\max}$, and the total number of nodes at a single time step. How does $j_{\max}$ change if $\lambda$ is doubled to $0.10$?

---

**Exercise 2.** Verify that the normal branching probabilities $p_u = \frac{1}{6} + \frac{j^2\lambda^2\Delta t^2 - j\lambda\Delta t}{2}$, $p_m = \frac{2}{3} - j^2\lambda^2\Delta t^2$, $p_d = \frac{1}{6} + \frac{j^2\lambda^2\Delta t^2 + j\lambda\Delta t}{2}$ sum to $1$ for all $j$. Then show that $p_m$ becomes negative when $j^2\lambda^2\Delta t^2 > 2/3$, confirming the need for non-normal branching.

---

**Exercise 3.** The spatial step $\Delta x = \sigma\sqrt{3\Delta t}$ is chosen to match the variance of the continuous-time process. Derive this choice by requiring that the second moment of the trinomial distribution $p_u(\Delta x)^2 + p_m(0)^2 + p_d(-\Delta x)^2$ equals $\sigma^2\Delta t$ when $j = 0$.

---

**Exercise 4.** For the up branching pattern ($j \to j, j-1, j-2$), derive the probabilities by solving the three moment-matching equations: normalization, mean-matching, and variance-matching. Verify that the formulas given in the text are correct.

---

**Exercise 5.** Explain why the tree is recombining. Show that after an up-middle-down sequence and a down-middle-up sequence, the process returns to the same node. What advantage does the recombining property provide for computational complexity?

---

**Exercise 6.** The boundary constant $0.1844$ in $j_{\max} = \lfloor 0.1844/(\lambda\Delta t) \rfloor$ ensures positive probabilities. Derive this constant by finding the value of $j\lambda\Delta t$ at which one of the normal branching probabilities first reaches zero.

---

**Exercise 7.** Compare the trinomial tree with a binomial tree for the Hull-White model. A binomial tree has only two successors per node. Explain why a binomial tree cannot simultaneously match the mean and variance of the OU process while maintaining positive probabilities and a recombining structure.
