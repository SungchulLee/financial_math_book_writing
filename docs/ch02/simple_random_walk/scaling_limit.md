# Scaling Limit

The discrete random walk and Brownian motion live in different mathematical spaces: one is defined on $\mathbb{Z}_{\geq 0}$, the other on $[0,\infty)$. To connect them, we embed the random walk into continuous time by a space–time rescaling, then study what happens as the mesh size tends to zero.

---

## The Scaled Random Walk

Fix a time horizon $T > 0$ and a discretization level $n \in \mathbb{N}$. The **scaled random walk** is defined, for $t \in [0,T]$, by

$$S^{(n)}(t) := \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor}$$

where $\lfloor nt \rfloor$ is the integer part of $nt$.

**Why $1/\sqrt{n}$?** We need the variance to remain $O(1)$ in the limit. From [Moments](moments_of_random_walk.md), $\text{Var}(S_{\lfloor nt \rfloor}) = \lfloor nt \rfloor \approx nt$. Dividing by $\sqrt{n}$:

$$\text{Var}(S^{(n)}(t)) = \frac{\lfloor nt \rfloor}{n} \approx t.$$

Any other scaling either collapses to 0 or blows up.

---

## Piecewise Linear Interpolation

The process $t \mapsto S^{(n)}(t)$ as defined above is piecewise constant (a step function). For the functional limit theorem we need continuous paths. We therefore use the **piecewise linear interpolation**:

$$W^{(n)}(t) := \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor} + \frac{nt - \lfloor nt \rfloor}{\sqrt{n}}\,\xi_{\lfloor nt \rfloor+1}.$$

Between consecutive jump times $k/n$ and $(k+1)/n$, we linearly interpolate using the next increment $\xi_{k+1}$. This defines $W^{(n)} \in C[0,T]$ — the space of continuous functions on $[0,T]$ — for each $n$.

---

## Asymptotic Moments

**Proposition 1.1.7** (Convergence of Moments)

For fixed $s < t$ in $[0,T]$:

1. $\mathbb{E}[S^{(n)}(t)] = 0$
2. $\text{Var}(S^{(n)}(t)) \to t$
3. $\text{Cov}(S^{(n)}(s),\, S^{(n)}(t)) \to \min(s,t) = s$

**Proof.**

(1) Follows immediately from $\mathbb{E}[S_{\lfloor nt \rfloor}] = 0$.

(2) Writing $\{nt\} := nt - \lfloor nt \rfloor \in [0,1)$ for the fractional part of $nt$:

$$\text{Var}(S^{(n)}(t)) = \frac{\text{Var}(S_{\lfloor nt \rfloor})}{n} = \frac{\lfloor nt \rfloor}{n} = t - \frac{\{nt\}}{n} \xrightarrow{n\to\infty} t.$$

(3) Let $m = \lfloor ns \rfloor$ and $k = \lfloor nt \rfloor$, so $m \leq k$. Since $\mathbb{E}[S_m] = 0$:

$$\text{Cov}(S_m, S_k) = \mathbb{E}[S_m S_k] = \mathbb{E}\!\left[\sum_{i=1}^m \xi_i \sum_{j=1}^k \xi_j\right] = \sum_{i=1}^m\sum_{j=1}^k \mathbb{E}[\xi_i\xi_j] = \sum_{i=1}^m \mathbb{E}[\xi_i^2] = m,$$

where cross terms vanish by independence. Therefore:

$$\text{Cov}(S^{(n)}(s), S^{(n)}(t)) = \frac{m}{n} = \frac{\lfloor ns \rfloor}{n} \xrightarrow{n\to\infty} s = \min(s,t). \quad\square$$

These are exactly the moments of Brownian motion: $\mathbb{E}[W_t] = 0$, $\text{Var}(W_t) = t$, $\text{Cov}(W_s, W_t) = \min(s,t)$.

---

## Structural Properties

### Markov Property

**Proposition 1.1.9**

$\{S_n\}$ is a Markov chain with respect to $\{\mathcal{F}_n\}$:

$$\mathbb{P}(S_{n+1} = j \mid S_n = i,\, S_{n-1},\ldots, S_0) = \mathbb{P}(S_{n+1} = j \mid S_n = i).$$

**Proof.** $S_{n+1} = S_n + \xi_{n+1}$ and $\xi_{n+1}$ is independent of $\mathcal{F}_n$, so the transition probability depends only on $S_n$. $\square$

The scaled process $S^{(n)}(t)$ inherits this Markov property at dyadic times, which persists in the Brownian limit.

### Independent Increments

**Proposition 1.1.10** (Independent Increments)

For $0 \leq t_1 < t_2 < \cdots < t_k \leq T$ with all $t_i$ multiples of $1/n$, the increments

$$S^{(n)}(t_2) - S^{(n)}(t_1),\quad S^{(n)}(t_3) - S^{(n)}(t_2),\quad\ldots,\quad S^{(n)}(t_k) - S^{(n)}(t_{k-1})$$

are independent.

**Proof.** Each increment is a partial sum of disjoint, independent blocks of $\{\xi_j\}$. $\square$

**Remark.** Independence of increments is preserved in the limit: Brownian motion is a **Lévy process** — a process with stationary independent increments.

---

## Path Properties of the Scaled Walk

### Non-Differentiability

The discrete walk has a "corner" at every integer time: the slope $\xi_n \in \{-1,+1\}$ changes at each step. For the scaled version, the difference quotient at scale $1/n$ is:

$$\frac{S^{(n)}(t + 1/n) - S^{(n)}(t)}{1/n} = \sqrt{n}\,\xi_{\lfloor nt \rfloor + 1} \in \{-\sqrt{n}, +\sqrt{n}\}.$$

This has magnitude $\sqrt{n} \to \infty$. In the limit, the paths cannot be differentiable. Paley, Wiener, and Zygmund (1933) proved rigorously that Brownian motion is almost surely nowhere differentiable.

### Quadratic Variation of the Scaled Walk

From [Martingale Property](martingale_property.md), $[S]_n = n$. For the scaled walk over $[0,t]$:

$$[S^{(n)}]_t = \sum_{i=1}^{\lfloor nt \rfloor} \!\left(S^{(n)}\!\left(\tfrac{i}{n}\right) - S^{(n)}\!\left(\tfrac{i-1}{n}\right)\right)^2
= \frac{1}{n} \sum_{i=1}^{\lfloor nt \rfloor} \xi_i^2 = \frac{\lfloor nt \rfloor}{n} \xrightarrow{n\to\infty} t.$$

The quadratic variation of the scaled walk converges to $t$ — the same as Brownian motion's quadratic variation $\langle W\rangle_t = t$. This is the key quantity underlying Itô's formula: formally $(dW_t)^2 = dt$.

---

## What Comes Next

The moment calculations above establish **finite-dimensional convergence**: for any fixed $t$, $S^{(n)}(t) \to \mathcal{N}(0,t)$ in distribution (this is just the CLT). But this is not enough to conclude that the *entire process* $\{S^{(n)}(t)\}_{t\in[0,T]}$ converges to Brownian motion.

What is needed in addition is **tightness** of the sequence of probability measures on $C[0,T]$. This, combined with the CLT, gives the full functional convergence

$$W^{(n)} \Rightarrow W \quad \text{in } C[0,T] \text{ with the uniform topology.}$$

This is **Donsker's Invariance Principle**, proved in [Donsker's Theorem](donsker_theorem.md).

---

## References

- Billingsley, P. (1999). *Convergence of Probability Measures*, 2nd ed. Wiley.
- Ethier, S. N., & Kurtz, T. G. (1986). *Markov Processes: Characterization and Convergence*. Wiley.
- Paley, R. E. A. C., Wiener, N., & Zygmund, A. (1933). Notes on random functions. *Mathematische Zeitschrift*, 37(1), 647–668.
