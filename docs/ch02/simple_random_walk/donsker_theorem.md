# Donsker's Theorem

Donsker's Invariance Principle is the functional analogue of the Central Limit Theorem. It upgrades pointwise convergence $S^{(n)}(t) \xrightarrow{d} \mathcal{N}(0,t)$ to convergence of the entire process as a random element of the path space $C[0,T]$.

---

## Recap: The CLT and Its Limitation

By [Theorem 1.1.10](mgf_of_random_walk.md), for each fixed $t$:

$$S^{(n)}(t) = \frac{S_{\lfloor nt \rfloor}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,t)$$

This is **marginal** (pointwise-in-$t$) convergence. But we want to make statements about **paths** — for example:

- Does $\max_{0 \leq t \leq 1} W^{(n)}(t) \to \max_{0 \leq t \leq 1} W_t$ in distribution?
- Do hitting-time distributions converge?
- Can we approximate the distribution of $\int_0^1 f(W^{(n)}(t))\,dt$?

These require convergence of the **entire path** simultaneously, i.e., weak convergence in $C[0,T]$.

Convergence of finite-dimensional distributions to those of $W$ is necessary but not sufficient. The additional condition is **tightness**.

---

## Tightness

A sequence of probability measures $\{\mu_n\}$ on $C[0,T]$ is **tight** if for every $\varepsilon > 0$ there exists a compact set $K \subset C[0,T]$ such that $\mu_n(K) \geq 1 - \varepsilon$ for all $n$.

By the Arzelà–Ascoli theorem, compact sets in $C[0,T]$ are characterised by equicontinuity. Therefore tightness reduces to controlling the modulus of continuity of $W^{(n)}$.

**Key estimate.** For the piecewise-linear scaled walk $W^{(n)}$ and $s, t \in [0,T]$:

$$\mathbb{E}[(W^{(n)}(t) - W^{(n)}(s))^4] \leq C\,|t-s|^2$$

for a constant $C$ independent of $n$. A proof of this estimate proceeds by noting that $W^{(n)}(t) - W^{(n)}(s)$ is a sum of at most $\lfloor n|t-s| \rfloor + 1$ independent increments of size $1/\sqrt{n}$, so the fourth moment is bounded by $C(\lfloor n|t-s|\rfloor/n)^2 \leq C|t-s|^2$. For a complete proof see Billingsley (1999), Theorem 12.3.

This moment estimate controls the modulus of continuity of $W^{(n)}$: by the **Kolmogorov continuity criterion** (see Billingsley (1999), Theorem 12.3), an estimate $\mathbb{E}[|X(t)-X(s)|^\alpha] \leq C|t-s|^{1+\beta}$ with $\alpha, \beta > 0$ implies that the laws of $\{X^{(n)}\}$ are tight in $C[0,T]$ via Arzelà–Ascoli. Here $\alpha = 4$ and $\beta = 1$, so the criterion applies directly.

---

## Donsker's Invariance Principle

**Theorem 1.1.11** (Donsker, 1951)

Let $\{\xi_i\}$ be i.i.d. with $\mathbb{E}[\xi_i] = 0$ and $\mathbb{E}[\xi_i^2] = 1$. Let $W^{(n)}$ be the piecewise-linear scaled random walk:

$$W^{(n)}(t) := \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor} + \frac{nt - \lfloor nt \rfloor}{\sqrt{n}}\,\xi_{\lfloor nt \rfloor+1}, \qquad t \in [0,T]$$

Then

$$W^{(n)} \Rightarrow W \quad \text{in } C[0,T] \text{ with the uniform topology,}$$

where $\Rightarrow$ denotes weak convergence of probability measures and $W$ is standard Brownian motion on $[0,T]$.

**Proof sketch.**

1. **Finite-dimensional convergence.** For any $0 \leq t_1 < \cdots < t_k \leq T$, write each increment $W^{(n)}(t_{i+1}) - W^{(n)}(t_i)$ as a sum of independent $\xi_j$'s over a block of indices, plus an interpolation remainder of size $O(1/\sqrt{n})$ that vanishes in probability. The CLT applied to each block gives joint convergence of the increments to independent Gaussians, and hence:

$$\bigl(W^{(n)}(t_1),\ldots,W^{(n)}(t_k)\bigr) \xrightarrow{d} \bigl(W_{t_1},\ldots,W_{t_k}\bigr)$$

2. **Tightness.** The fourth-moment estimate above implies tightness of $\{W^{(n)}\}$ in $C[0,T]$ via the Kolmogorov continuity criterion.

3. **Conclusion.** By Prohorov's theorem, tightness combined with convergence of all finite-dimensional distributions implies weak convergence in $C[0,T]$. $\square$

---

## Step Functions vs.\ Piecewise-Linear Paths

Without piecewise-linear interpolation, $S^{(n)}$ is a step function living in the Skorokhod space $D[0,T]$ of right-continuous functions with left limits. In that setting:

$$S^{(n)} \Rightarrow W \quad \text{in } D[0,T] \text{ with the Skorokhod topology.}$$

The piecewise-linear version $W^{(n)}$ lies in $C[0,T]$ and satisfies

$$W^{(n)} \Rightarrow W \quad \text{in } C[0,T] \text{ with the uniform topology } \|f\|_\infty = \sup_{t \in [0,T]}|f(t)|.$$

The latter is the stronger statement. Within each interval $[k/n,(k+1)/n]$, $S^{(n)}$ is constant while $W^{(n)}$ linearly interpolates a single increment of size $\pm 1/\sqrt{n}$; the maximum deviation within any such interval is therefore exactly $1/\sqrt{n}$. Hence $\|S^{(n)} - W^{(n)}\|_\infty = 1/\sqrt{n} \to 0$ almost surely, so both versions give the same weak limit.

---

## Universality

The theorem holds for any i.i.d. sequence with mean 0 and variance 1 — not just $\pm 1$ steps. The limiting Brownian motion does not depend on the distribution of the steps. This is the **invariance principle**: the limit is universal, depending only on the mean and variance.

**Consequence for finance.** By Donsker's theorem, the Cox–Ross–Rubinstein binomial tree (see [Applications](applications_random_walk.md)) converges to geometric Brownian motion as the number of steps grows, validating the continuous-time Black–Scholes model as a limit of discrete hedging models.

---

## References

- Donsker, M. D. (1951). An invariance principle for certain probability limit theorems. *Memoirs of the American Mathematical Society*, 6, 1–12.
- Billingsley, P. (1999). *Convergence of Probability Measures*, 2nd ed. Wiley. (See Theorem 12.3 for the tightness estimate.)
- Ethier, S. N., & Kurtz, T. G. (1986). *Markov Processes: Characterization and Convergence*. Wiley.
- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
