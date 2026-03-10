# Donsker's Theorem


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Donsker's Invariance Principle is the functional analogue of the Central Limit Theorem. It upgrades pointwise convergence $S^{(n)}(t) \xrightarrow{d} W_t$ to convergence of the entire process as a random element of the path space $C[0,T]$.

---

## The Central Limit Theorem

**Theorem 1.1.8** (Classical CLT)

Let $\{\xi_i\}_{i \geq 1}$ be i.i.d. with $\mathbb{E}[\xi_i] = 0$ and $\mathbb{E}[\xi_i^2] = \sigma^2 \in (0,\infty)$. Then:

$$\frac{1}{\sqrt{n}}\sum_{i=1}^n \xi_i \xrightarrow{d} \mathcal{N}(0,\sigma^2) \quad \text{as } n \to \infty$$

For the symmetric random walk ($\sigma^2 = 1$), this gives $S_n/\sqrt{n} \xrightarrow{d} \mathcal{N}(0,1)$. Since $S^{(n)}(t) = S_{\lfloor nt \rfloor}/\sqrt{n}$, for each fixed $t$:

$$S^{(n)}(t) \xrightarrow{d} \mathcal{N}(0,t)$$

The MGF proof from [Moment Generating Function](mgf_of_random_walk.md) gives this in one computation.

---

## Why the CLT is Not Enough

The CLT gives **marginal** (pointwise-in-$t$) convergence. But we want to make statements about **paths** — for example:

- Does $\max_{0 \leq t \leq 1} S^{(n)}(t) \to \max_{0 \leq t \leq 1} W_t$?
- Do hitting-time distributions converge?
- Can we approximate the distribution of $\int_0^1 f(S^{(n)}(t))\,dt$?

These require convergence of the **entire path** simultaneously, i.e., convergence in the space $C[0,T]$.

Finite-dimensional distributions converging to those of $W$ is necessary but not sufficient. An additional condition — **tightness** — is needed.

---

## Tightness

A sequence of probability measures $\{\mu_n\}$ on $C[0,T]$ is **tight** if for every $\varepsilon > 0$ there exists a compact set $K \subset C[0,T]$ such that $\mu_n(K) \geq 1 - \varepsilon$ for all $n$.

By the Arzelà–Ascoli theorem, compact sets in $C[0,T]$ are characterised by **equicontinuity**. Therefore tightness reduces to controlling the modulus of continuity of $W^{(n)}$.

**Key estimate.** For the piecewise-linear scaled walk $W^{(n)}$ and $|s-t| \leq \delta$:

$$\mathbb{E}[(W^{(n)}(t) - W^{(n)}(s))^4] \leq C\,|t-s|^2$$

for a constant $C$ independent of $n$. This is the **Kolmogorov tightness criterion**, which implies tightness of $\{W^{(n)}\}$ in $C[0,T]$.

---

## Donsker's Invariance Principle

**Theorem** (Donsker, 1951)

Let $\{\xi_i\}$ be i.i.d. with $\mathbb{E}[\xi_i] = 0$ and $\mathbb{E}[\xi_i^2] = 1$. Let $W^{(n)}$ be the piecewise-linear scaled random walk:

$$W^{(n)}(t) := \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor} + \frac{nt - \lfloor nt \rfloor}{\sqrt{n}}\,\xi_{\lfloor nt \rfloor+1}, \qquad t \in [0,T]$$

Then

$$W^{(n)} \Rightarrow W \quad \text{in } C[0,T] \text{ with the uniform topology,}$$

where $\Rightarrow$ denotes weak convergence of probability measures and $W$ is standard Brownian motion on $[0,T]$.

**Proof sketch.**

1. **Finite-dimensional convergence.** For any $0 \leq t_1 < \cdots < t_k \leq T$, the increments $W^{(n)}(t_{i+1}) - W^{(n)}(t_i)$ are sums of independent $\xi_j$'s over disjoint blocks. The CLT applied to each block gives joint convergence:

$$\bigl(W^{(n)}(t_1),\ldots,W^{(n)}(t_k)\bigr) \xrightarrow{d} \bigl(W_{t_1},\ldots,W_{t_k}\bigr)$$

2. **Tightness.** The fourth-moment estimate above implies tightness via the Kolmogorov–Chentsov criterion.

3. **Conclusion.** Tightness + convergence of finite-dimensional distributions implies weak convergence in $C[0,T]$ (Prohorov's theorem). $\square$

---

## Convergence Spaces: A Clarification

Without piecewise linear interpolation, $S^{(n)}$ is a step function and lives in the Skorokhod space $D[0,T]$ of right-continuous functions with left limits. In that setting, the convergence is

$$S^{(n)} \Rightarrow W \quad \text{in } D[0,T] \text{ with the Skorokhod topology.}$$

Since $W$ has continuous paths and we use piecewise linear interpolation (so $W^{(n)} \in C[0,T]$), the convergence may equivalently be stated in $C[0,T]$ with the **uniform topology** $\|f\|_\infty = \sup_{t \in [0,T]}|f(t)|$. This is the stronger statement and the one used in applications.

---

## Universality

The theorem holds for any i.i.d. sequence with mean 0 and variance 1 — not just $\pm 1$ steps. The limiting Brownian motion does not depend on the distribution of the steps. This is the **invariance principle**: the limit is universal, depending only on the mean and variance.

**Consequence for finance.** By Donsker's theorem, the Cox–Ross–Rubinstein binomial tree (see [Applications](applications_random_walk.md)) converges to geometric Brownian motion as the number of steps grows, validating the continuous-time Black–Scholes model as a limit of discrete hedging models.

---

## References

- Donsker, M. D. (1951). An invariance principle for certain probability limit theorems. *Memoirs of the American Mathematical Society*, 6, 1–12.
- Billingsley, P. (1999). *Convergence of Probability Measures*, 2nd ed. Wiley.
- Ethier, S. N., & Kurtz, T. G. (1986). *Markov Processes: Characterization and Convergence*. Wiley.
- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
