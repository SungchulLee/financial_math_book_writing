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

Recall (see [§ Moments of Brownian Motion](../brownian_motion/moments_of_brownian_motion.md)): these are exactly $\mathbb{E}[W_t]=0$, $\text{Var}(W_t)=t$, $\text{Cov}(W_s,W_t)=\min(s,t)$.

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

The difference quotient at jump times $t = k/n$ is $\sqrt{n}\,\xi_{k+1}$, which diverges as $n\to\infty$ — the discrete fingerprint of the limit's roughness. Recall (see [§ Hölder Continuity and Non-Differentiability](../brownian_motion/holder_continuity_and_non_differentiability.md)): Brownian paths are a.s. nowhere differentiable.

### Quadratic Variation of the Scaled Walk

From [Martingale Property](martingale_property.md), $[S]_n = n$ almost surely. For the scaled walk over $[0,t]$:

$$[S^{(n)}]_t = \sum_{i=1}^{\lfloor nt \rfloor} \!\left(S^{(n)}\!\left(\tfrac{i}{n}\right) - S^{(n)}\!\left(\tfrac{i-1}{n}\right)\right)^2
= \frac{1}{n} \sum_{i=1}^{\lfloor nt \rfloor} \xi_i^2 = \frac{\lfloor nt \rfloor}{n} \xrightarrow{n\to\infty} t$$

The quadratic variation of the scaled walk converges to $t$. Recall (see [§ Quadratic Variation of Brownian Motion](../brownian_motion/quadratic_variation_of_brownian_motion.md)): $[W]_t = t$, and this is the quantity behind Itô's formula $(dW_t)^2 = dt$.

---

## What Comes Next

Finite-dimensional convergence plus tightness yields the full functional limit $W^{(n)} \Rightarrow W$ in $C[0,T]$ — see [Donsker's Theorem](donsker_theorem.md).

---

## References

- Billingsley, P. (1999). *Convergence of Probability Measures*, 2nd ed. Wiley.
- Ethier, S. N., & Kurtz, T. G. (1986). *Markov Processes: Characterization and Convergence*. Wiley.
- Paley, R. E. A. C., Wiener, N., & Zygmund, A. (1933). Notes on random functions. *Mathematische Zeitschrift*, 37(1), 647–668.

---

## Exercises

**Exercise 1.** For the scaled random walk $S^{(n)}(t) = S_{\lfloor nt \rfloor}/\sqrt{n}$, compute the exact variance $\text{Var}(S^{(n)}(t))$ as a function of $n$ and $t$, and show that the error $|t - \text{Var}(S^{(n)}(t))| \leq 1/n$ for all $t \in [0, T]$.

??? success "Solution to Exercise 1"
    The exact variance is:

    $$
    \text{Var}(S^{(n)}(t)) = \frac{\lfloor nt \rfloor}{n}
    $$

    since $\text{Var}(S_{\lfloor nt \rfloor}) = \lfloor nt \rfloor$ and dividing by $(\sqrt{n})^2 = n$. The error is:

    $$
    \left|t - \frac{\lfloor nt \rfloor}{n}\right| = \frac{nt - \lfloor nt \rfloor}{n} = \frac{\{nt\}}{n}
    $$

    where $\{nt\} = nt - \lfloor nt \rfloor \in [0,1)$ is the fractional part. Since $0 \leq \{nt\} < 1$:

    $$
    0 \leq t - \frac{\lfloor nt \rfloor}{n} < \frac{1}{n}
    $$

    Therefore $|t - \text{Var}(S^{(n)}(t))| \leq 1/n$ for all $t \in [0,T]$.

---

**Exercise 2.** For fixed $0 < s < t \leq T$ with $s$ and $t$ both multiples of $1/n$, compute the distribution of the increment $S^{(n)}(t) - S^{(n)}(s)$. Show that its mean is 0 and its variance is $t - s$. Why is $S^{(n)}(t) - S^{(n)}(s)$ independent of $S^{(n)}(s)$?

??? success "Solution to Exercise 2"
    Since $s$ and $t$ are multiples of $1/n$, write $s = m/n$ and $t = k/n$ with $m < k$ integers. Then:

    $$
    S^{(n)}(t) - S^{(n)}(s) = \frac{S_k - S_m}{\sqrt{n}} = \frac{1}{\sqrt{n}}\sum_{i=m+1}^{k} \xi_i
    $$

    This is a sum of $k - m$ independent $\pm 1$ random variables, scaled by $1/\sqrt{n}$. Each $\xi_i$ takes $\pm 1$ with probability $1/2$, so $S_k - S_m$ has the same distribution as $S_{k-m}$. The increment has:

    $$
    \mathbb{E}[S^{(n)}(t) - S^{(n)}(s)] = 0
    $$

    $$
    \text{Var}(S^{(n)}(t) - S^{(n)}(s)) = \frac{k-m}{n} = \frac{k}{n} - \frac{m}{n} = t - s
    $$

    The increment $S^{(n)}(t) - S^{(n)}(s) = (S_k - S_m)/\sqrt{n}$ depends only on $\xi_{m+1}, \ldots, \xi_k$, while $S^{(n)}(s) = S_m/\sqrt{n}$ depends only on $\xi_1, \ldots, \xi_m$. Since the $\xi_i$ are independent, these two quantities depend on disjoint sets of independent random variables and are therefore independent.

---

**Exercise 3.** The difference quotient of the scaled walk at a jump time $t = k/n$ satisfies $\frac{S^{(n)}(t + 1/n) - S^{(n)}(t)}{1/n} = \sqrt{n}\,\xi_{k+1}$. Compute $\mathbb{E}\left[\left(\frac{S^{(n)}(t+1/n) - S^{(n)}(t)}{1/n}\right)^2\right]$ and explain why this divergence as $n \to \infty$ is consistent with the nowhere-differentiability of Brownian motion.

??? success "Solution to Exercise 3"
    At the jump time $t = k/n$:

    $$
    \frac{S^{(n)}(t + 1/n) - S^{(n)}(t)}{1/n} = \frac{(S_{k+1} - S_k)/\sqrt{n}}{1/n} = \frac{\xi_{k+1}\sqrt{n}}{1} = \sqrt{n}\,\xi_{k+1}
    $$

    Taking the second moment:

    $$
    \mathbb{E}\!\left[\left(\frac{S^{(n)}(t+1/n) - S^{(n)}(t)}{1/n}\right)^2\right] = \mathbb{E}[n\,\xi_{k+1}^2] = n \cdot 1 = n
    $$

    This diverges as $n \to \infty$. In the limit, if Brownian motion were differentiable at some time $t$, the difference quotient $(W_{t+h} - W_t)/h$ would converge to a finite limit as $h \to 0$. But the scaled walk's difference quotient has mean square $n \to \infty$ (corresponding to $h = 1/n \to 0$), showing that the derivative, if it existed, would have infinite second moment. This is consistent with the fact that Brownian motion is almost surely nowhere differentiable: the difference quotient diverges rather than converging.

---

**Exercise 4.** For the scaled walk over $[0, t]$ with the uniform partition at resolution $n$, verify that the quadratic variation is $[S^{(n)}]_t = \lfloor nt \rfloor / n$. Show that this converges to $t$ and that the rate of convergence is $O(1/n)$. Compare this deterministic convergence to the $L^2$ convergence of $[B]_T^{(\Pi_n)} \to T$ for Brownian motion (which has random fluctuations of order $1/\sqrt{n}$).

??? success "Solution to Exercise 4"
    At resolution $n$, the uniform partition of $[0,t]$ has points $\{0, 1/n, 2/n, \ldots, \lfloor nt \rfloor/n\}$. The quadratic variation is:

    $$
    [S^{(n)}]_t = \sum_{i=1}^{\lfloor nt \rfloor}\left(\frac{S_i - S_{i-1}}{\sqrt{n}}\right)^2 = \frac{1}{n}\sum_{i=1}^{\lfloor nt \rfloor} \xi_i^2 = \frac{\lfloor nt \rfloor}{n}
    $$

    This is deterministic (since $\xi_i^2 = 1$ always). The convergence to $t$ has rate:

    $$
    \left|t - \frac{\lfloor nt \rfloor}{n}\right| = \frac{\{nt\}}{n} < \frac{1}{n} = O(1/n)
    $$

    For Brownian motion, $[B]_T^{(\Pi_n)} = \sum_{i} (B_{t_{i+1}} - B_{t_i})^2$ converges to $T$ in $L^2$, with $\text{Var}([B]_T^{(\Pi_n)}) = 2T^2/n$, so the fluctuations are of order $1/\sqrt{n}$. The key difference: the random walk's quadratic variation is **deterministic** (zero variance for every $n$), while Brownian motion's sampled quadratic variation is **random** with fluctuations that vanish as $O(1/\sqrt{n})$. The deterministic convergence of the discrete case is a stronger statement.

---

**Exercise 5.** Consider a "biased scaled walk" with $p = 1/2 + c/\sqrt{n}$ for some constant $c > 0$. Show that $\mathbb{E}[S^{(n)}(t)] \to 2ct$ and $\text{Var}(S^{(n)}(t)) \to t$ as $n \to \infty$. What continuous process does this converge to? Relate this to **Brownian motion with drift** $W_t + \mu t$.

??? success "Solution to Exercise 5"
    With $p = 1/2 + c/\sqrt{n}$, each step has mean $\mu_n = 2p - 1 = 2c/\sqrt{n}$ and variance $\sigma_n^2 = 4p(1-p) = 1 - 4c^2/n$. For the scaled walk:

    $$
    \mathbb{E}[S^{(n)}(t)] = \frac{\lfloor nt \rfloor \cdot 2c/\sqrt{n}}{\sqrt{n}} = \frac{2c\lfloor nt \rfloor}{n} \to 2ct
    $$

    $$
    \text{Var}(S^{(n)}(t)) = \frac{\lfloor nt \rfloor \cdot (1 - 4c^2/n)}{n} = \frac{\lfloor nt \rfloor}{n} - \frac{4c^2\lfloor nt \rfloor}{n^2} \to t - 0 = t
    $$

    The scaled walk converges to a process with mean $2ct$ and variance $t$, which is **Brownian motion with drift**: $X_t = 2ct + W_t$, or equivalently $W_t + \mu t$ with $\mu = 2c$. This shows that a small bias of order $1/\sqrt{n}$ in the step probabilities produces a nontrivial drift in the continuous limit, while the diffusive component remains unchanged.

---

**Exercise 6.** The covariance structure $\text{Cov}(S^{(n)}(s), S^{(n)}(t)) \to \min(s,t)$ is the defining property of Brownian motion's second-order structure. Verify that $\min(s,t)$ is a **positive semi-definite kernel**: for any $t_1 < t_2 < \cdots < t_k$ and any $a_1, \ldots, a_k \in \mathbb{R}$, show that $\sum_{i,j} a_i a_j \min(t_i, t_j) \geq 0$. (Hint: write $\min(t_i, t_j) = \int_0^T \mathbf{1}_{[0,t_i]}(u)\,\mathbf{1}_{[0,t_j]}(u)\,du$.)

??? success "Solution to Exercise 6"
    Using the hint, write $\min(t_i, t_j) = \int_0^T \mathbf{1}_{[0,t_i]}(u)\,\mathbf{1}_{[0,t_j]}(u)\,du$. Then:

    $$
    \sum_{i,j=1}^k a_i a_j \min(t_i, t_j) = \sum_{i,j=1}^k a_i a_j \int_0^T \mathbf{1}_{[0,t_i]}(u)\,\mathbf{1}_{[0,t_j]}(u)\,du
    $$

    Exchanging the sum and integral (all terms are finite):

    $$
    = \int_0^T \left(\sum_{i=1}^k a_i \mathbf{1}_{[0,t_i]}(u)\right)\left(\sum_{j=1}^k a_j \mathbf{1}_{[0,t_j]}(u)\right) du = \int_0^T \left(\sum_{i=1}^k a_i \mathbf{1}_{[0,t_i]}(u)\right)^2 du
    $$

    Since the integrand is a square, it is non-negative everywhere, and the integral of a non-negative function is non-negative:

    $$
    \sum_{i,j=1}^k a_i a_j \min(t_i, t_j) = \int_0^T \left(\sum_{i=1}^k a_i \mathbf{1}_{[0,t_i]}(u)\right)^2 du \geq 0
    $$

    This proves that $K(s,t) = \min(s,t)$ is a positive semi-definite kernel, which by the Kolmogorov existence theorem guarantees the existence of a Gaussian process with this covariance structure (i.e., Brownian motion).

---

**Exercise 7.** Reflection Principle (Preview).

Let $M_n = \max_{0 \leq k \leq n} S_k$ be the running maximum of the symmetric random walk.

**(a)** By a symmetry argument, show that for $m > 0$:

$$\mathbb{P}(M_n \geq m) = 2\,\mathbb{P}(S_n \geq m) - \mathbb{P}(S_n = m)$$

*Hint:* Consider the "reflected" path obtained by flipping all steps after the first time the walk hits $m$. By symmetry, paths that hit $m$ and end below $m$ are in bijection with paths that hit $m$ and end above $m$.

**(b)** Use part (a) and the normal approximation to show that for large $n$:

$$\mathbb{P}\!\left(\frac{M_n}{\sqrt{n}} \geq x\right) \approx 2\bigl(1-\Phi(x)\bigr), \qquad x > 0$$

where $\Phi$ is the standard normal CDF. This is the exact distribution of $\max_{0 \leq t \leq 1} W_t$ for Brownian motion, derived rigorously in a later chapter.

??? success "Solution to Exercise 7"
    **(a)** Decompose the event $\{M_n \geq m\}$ by the final position $S_n$. Paths that hit $m$ and end at $S_n = j < m$ are in bijection with paths that hit $m$ and end at $2m - j > m$ — reflect all steps after the first hitting time of $m$. Therefore $\mathbb{P}(M_n \geq m, S_n < m) = \mathbb{P}(S_n > m)$. Combining:

    $$
    \mathbb{P}(M_n \geq m) = \mathbb{P}(S_n > m) + \mathbb{P}(S_n = m) + \mathbb{P}(S_n > m) = 2\mathbb{P}(S_n \geq m) - \mathbb{P}(S_n = m)
    $$

    **(b)** For large $n$, $S_n/\sqrt{n} \approx Z \sim \mathcal{N}(0,1)$ and $\mathbb{P}(S_n = m) \to 0$:

    $$
    \mathbb{P}\!\left(\frac{M_n}{\sqrt{n}} \geq x\right) \approx 2\mathbb{P}(Z \geq x) = 2(1 - \Phi(x))
    $$

    This matches the exact distribution of the running maximum of Brownian motion on $[0,1]$.
