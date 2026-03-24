# Scaling Limit

The discrete random walk and Brownian motion live in different mathematical spaces: one is defined on $\mathbb{Z}_{\geq 0}$, the other on $[0,\infty)$. To connect them, we embed the random walk into continuous time by a space–time rescaling, then study what happens as the mesh size tends to zero.

---

## The Scaled Random Walk

Fix a time horizon $T > 0$ and a discretization level $n \in \mathbb{N}$. The **scaled random walk** is defined, for $t \in [0,T]$, by

$$S^{(n)}(t) := \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor}$$

where $\lfloor nt \rfloor$ is the integer part of $nt$.

**Why $1/\sqrt{n}$?** We need the variance to remain $O(1)$ in the limit. From [Moments](moments_of_random_walk.md), $\text{Var}(S_{\lfloor nt \rfloor}) = \lfloor nt \rfloor \approx nt$. Dividing by $\sqrt{n}$:

$$\text{Var}(S^{(n)}(t)) = \frac{\lfloor nt \rfloor}{n} \approx t$$

Any other scaling either collapses to 0 or blows up.

---

## Piecewise Linear Interpolation

The process $t \mapsto S^{(n)}(t)$ as defined above is piecewise constant (a step function). For the functional limit theorem we need continuous paths. We therefore use the **piecewise linear interpolation**:

$$W^{(n)}(t) := \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor} + \frac{nt - \lfloor nt \rfloor}{\sqrt{n}}\,\xi_{\lfloor nt \rfloor+1}$$

Here $nt - \lfloor nt \rfloor \in [0,1)$ is the fractional part of $nt$. Between consecutive jump times $k/n$ and $(k+1)/n$, we linearly interpolate using the next increment $\xi_{k+1}$. This defines $W^{(n)} \in C[0,T]$ — the space of continuous functions on $[0,T]$ — for each $n$.

**Notation.** We reserve $S^{(n)}$ for the piecewise-constant (step-function) version and $W^{(n)}$ for the piecewise-linear interpolation. Both converge to the same limit; the distinction matters only for the topology in which convergence is stated. See [Donsker's Theorem](donsker_theorem.md) for details.

---

## Asymptotic Moments

**Proposition 1.1.8** (Convergence of Moments)

For fixed $s < t$ in $[0,T]$:

1. $\mathbb{E}[S^{(n)}(t)] = 0$
2. $\text{Var}(S^{(n)}(t)) \to t$
3. $\text{Cov}(S^{(n)}(s),\, S^{(n)}(t)) \to \min(s,t) = s$

**Proof.**

(1) Follows immediately from $\mathbb{E}[S_{\lfloor nt \rfloor}] = 0$.

(2) Let $\{nt\} := nt - \lfloor nt \rfloor \in [0,1)$ denote the fractional part of $nt$. Then:

$$\text{Var}(S^{(n)}(t)) = \frac{\text{Var}(S_{\lfloor nt \rfloor})}{n} = \frac{\lfloor nt \rfloor}{n} = t - \frac{\{nt\}}{n} \xrightarrow{n\to\infty} t$$

(3) Let $m = \lfloor ns \rfloor$ and $k = \lfloor nt \rfloor$, so $m \leq k$. Since $\mathbb{E}[S_m] = 0$:

$$\text{Cov}(S_m, S_k) = \mathbb{E}[S_m S_k] = \mathbb{E}\!\left[\sum_{i=1}^m \xi_i \sum_{j=1}^k \xi_j\right] = \sum_{i=1}^m\sum_{j=1}^k \mathbb{E}[\xi_i\xi_j] = \sum_{i=1}^m \mathbb{E}[\xi_i^2] = m$$

where cross terms vanish by independence. Therefore:

$$\text{Cov}(S^{(n)}(s), S^{(n)}(t)) = \frac{m}{n} = \frac{\lfloor ns \rfloor}{n} \xrightarrow{n\to\infty} s = \min(s,t). \quad\square$$

These are exactly the moments of Brownian motion: $\mathbb{E}[W_t] = 0$, $\text{Var}(W_t) = t$, $\text{Cov}(W_s, W_t) = \min(s,t)$.

---

## Independent Increments

**Proposition 1.1.9** (Independent Increments)

For $0 \leq t_1 < t_2 < \cdots < t_k \leq T$ with all $t_i$ multiples of $1/n$, the increments

$$S^{(n)}(t_2) - S^{(n)}(t_1),\quad S^{(n)}(t_3) - S^{(n)}(t_2),\quad\ldots,\quad S^{(n)}(t_k) - S^{(n)}(t_{k-1})$$

are independent.

**Proof.** Each increment is a partial sum over a disjoint block of independent $\{\xi_j\}$. Partial sums over disjoint blocks of independent random variables are independent. $\square$

**Remark.** The restriction to dyadic times (multiples of $1/n$) is necessary for the discrete walk: between two such times the increment is a deterministic linear interpolation of a single $\xi_j$, not an independent quantity. In the Brownian limit this restriction is lifted: $W_t - W_s$ and $W_u - W_v$ are independent whenever $[s,t]$ and $[v,u]$ are disjoint, for *any* $s,t,u,v \in [0,T]$. Independence of increments is thus one of the properties that becomes cleaner in the limit.

---

## Path Properties of the Scaled Walk

### Non-Differentiability

For the scaled walk, the difference quotient at jump times $t = k/n$ (for integer $k$) is:

$$\frac{S^{(n)}(t + 1/n) - S^{(n)}(t)}{1/n} = \sqrt{n}\,\xi_{k+1} \in \{-\sqrt{n}, +\sqrt{n}\}$$

This has magnitude $\sqrt{n} \to \infty$. (At intermediate times the step-function $S^{(n)}$ is flat, and the piecewise-linear $W^{(n)}$ has constant slope $\pm\sqrt{n}$ between jump times — so the same conclusion holds throughout each interval.) In the limit, the paths cannot be differentiable. Paley, Wiener, and Zygmund (1933) proved rigorously that Brownian motion is almost surely nowhere differentiable.

### Quadratic Variation of the Scaled Walk

From [Martingale Property](martingale_property.md), $[S]_n = n$ almost surely. For the scaled walk over $[0,t]$:

$$[S^{(n)}]_t = \sum_{i=1}^{\lfloor nt \rfloor} \!\left(S^{(n)}\!\left(\tfrac{i}{n}\right) - S^{(n)}\!\left(\tfrac{i-1}{n}\right)\right)^2
= \frac{1}{n} \sum_{i=1}^{\lfloor nt \rfloor} \xi_i^2 = \frac{\lfloor nt \rfloor}{n} \xrightarrow{n\to\infty} t$$

The quadratic variation of the scaled walk converges to $t$ — the same as Brownian motion's quadratic variation $\langle W\rangle_t = t$. This is the key quantity underlying Itô's formula: formally $(dW_t)^2 = dt$.

---

## What Comes Next

The moment calculations above establish **finite-dimensional convergence**: for any fixed $t$, $S^{(n)}(t) \to \mathcal{N}(0,t)$ in distribution (this is the CLT of [Theorem 1.1.10](mgf_of_random_walk.md)). But finite-dimensional convergence alone does not imply that the *entire process* converges to Brownian motion. The additional ingredient is **tightness** of the measures induced by $\{W^{(n)}\}$ on $C[0,T]$. Tightness plus finite-dimensional convergence gives the full functional limit

$$W^{(n)} \Rightarrow W \quad \text{in } C[0,T] \text{ with the uniform topology.}$$

This is **Donsker's Invariance Principle**, proved in [Donsker's Theorem](donsker_theorem.md).

---

## References

- Billingsley, P. (1999). *Convergence of Probability Measures*, 2nd ed. Wiley.
- Ethier, S. N., & Kurtz, T. G. (1986). *Markov Processes: Characterization and Convergence*. Wiley.
- Paley, R. E. A. C., Wiener, N., & Zygmund, A. (1933). Notes on random functions. *Mathematische Zeitschrift*, 37(1), 647–668.

---

## Exercises

**Exercise 1.** For the scaled random walk $S^{(n)}(t) = S_{\lfloor nt \rfloor}/\sqrt{n}$, compute the exact variance $\text{Var}(S^{(n)}(t))$ as a function of $n$ and $t$, and show that the error $|t - \text{Var}(S^{(n)}(t))| \leq 1/n$ for all $t \in [0, T]$.

---

**Exercise 2.** For fixed $0 < s < t \leq T$ with $s$ and $t$ both multiples of $1/n$, compute the distribution of the increment $S^{(n)}(t) - S^{(n)}(s)$. Show that its mean is 0 and its variance is $t - s$. Why is $S^{(n)}(t) - S^{(n)}(s)$ independent of $S^{(n)}(s)$?

---

**Exercise 3.** The difference quotient of the scaled walk at a jump time $t = k/n$ satisfies $\frac{S^{(n)}(t + 1/n) - S^{(n)}(t)}{1/n} = \sqrt{n}\,\xi_{k+1}$. Compute $\mathbb{E}\left[\left(\frac{S^{(n)}(t+1/n) - S^{(n)}(t)}{1/n}\right)^2\right]$ and explain why this divergence as $n \to \infty$ is consistent with the nowhere-differentiability of Brownian motion.

---

**Exercise 4.** For the scaled walk over $[0, t]$ with the uniform partition at resolution $n$, verify that the quadratic variation is $[S^{(n)}]_t = \lfloor nt \rfloor / n$. Show that this converges to $t$ and that the rate of convergence is $O(1/n)$. Compare this deterministic convergence to the $L^2$ convergence of $[B]_T^{(\Pi_n)} \to T$ for Brownian motion (which has random fluctuations of order $1/\sqrt{n}$).

---

**Exercise 5.** Consider a "biased scaled walk" with $p = 1/2 + c/\sqrt{n}$ for some constant $c > 0$. Show that $\mathbb{E}[S^{(n)}(t)] \to 2ct$ and $\text{Var}(S^{(n)}(t)) \to t$ as $n \to \infty$. What continuous process does this converge to? Relate this to **Brownian motion with drift** $W_t + \mu t$.

---

**Exercise 6.** The covariance structure $\text{Cov}(S^{(n)}(s), S^{(n)}(t)) \to \min(s,t)$ is the defining property of Brownian motion's second-order structure. Verify that $\min(s,t)$ is a **positive semi-definite kernel**: for any $t_1 < t_2 < \cdots < t_k$ and any $a_1, \ldots, a_k \in \mathbb{R}$, show that $\sum_{i,j} a_i a_j \min(t_i, t_j) \geq 0$. (Hint: write $\min(t_i, t_j) = \int_0^T \mathbf{1}_{[0,t_i]}(u)\,\mathbf{1}_{[0,t_j]}(u)\,du$.)
