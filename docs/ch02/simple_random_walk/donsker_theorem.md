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

$$W^{(n)} \Rightarrow W \quad \text{in } C[0,T] \text{ with the uniform topology } \|f\|_\infty = \sup_{t \in [0,T]}|f(t)|$$

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

---

## Exercises

**Exercise 1.** State precisely what "weak convergence in $C[0, T]$" means. That is, for any bounded continuous functional $F: C[0,T] \to \mathbb{R}$, what does $W^{(n)} \Rightarrow W$ imply about $\mathbb{E}[F(W^{(n)})]$?

??? success "Solution to Exercise 1"
    Weak convergence $W^{(n)} \Rightarrow W$ in $C[0,T]$ means: for every bounded continuous functional $F: C[0,T] \to \mathbb{R}$ (where $C[0,T]$ is equipped with the supremum norm topology),

    $$
    \mathbb{E}[F(W^{(n)})] \to \mathbb{E}[F(W)] \quad \text{as } n \to \infty
    $$

    Equivalently, if $\mu_n$ denotes the law of $W^{(n)}$ on $C[0,T]$ and $\mu$ is the Wiener measure (the law of Brownian motion), then $\mu_n \to \mu$ weakly, meaning $\int F\,d\mu_n \to \int F\,d\mu$ for all bounded continuous $F$.

---

**Exercise 2.** Donsker's theorem implies that $\max_{0 \leq t \leq 1} W^{(n)}(t) \xrightarrow{d} \max_{0 \leq t \leq 1} W_t$, since $f \mapsto \max_{0 \leq t \leq 1} f(t)$ is a continuous functional on $C[0,1]$. Using the known distribution $\mathbb{P}(\max_{0 \leq t \leq 1} W_t \leq x) = 2\Phi(x) - 1$ for $x \geq 0$ (where $\Phi$ is the standard normal CDF), compute $\mathbb{P}(\max_{0 \leq t \leq 1} W_t > 2)$.

??? success "Solution to Exercise 2"
    By the given formula, for $x \geq 0$:

    $$
    \mathbb{P}\!\left(\max_{0 \leq t \leq 1} W_t > 2\right) = 1 - \mathbb{P}\!\left(\max_{0 \leq t \leq 1} W_t \leq 2\right) = 1 - (2\Phi(2) - 1)
    $$

    Using $\Phi(2) \approx 0.9772$:

    $$
    = 1 - (2 \times 0.9772 - 1) = 1 - (1.9544 - 1) = 1 - 0.9544 = 0.0456
    $$

    So there is approximately a 4.56% probability that the maximum of a standard Brownian motion on $[0,1]$ exceeds 2.

---

**Exercise 3.** Explain why finite-dimensional convergence alone is insufficient for Donsker's theorem. Give an example of a sequence of processes $\{X^{(n)}\}$ on $[0,1]$ whose finite-dimensional distributions converge to those of Brownian motion, but whose paths do not converge weakly in $C[0,1]$. (Hint: consider processes that have a single large spike.)

??? success "Solution to Exercise 3"
    Finite-dimensional convergence alone is insufficient because it says nothing about the behavior of paths between the finitely many time points. One can construct pathological processes that agree with Brownian motion at finitely many times but have wild behavior in between.

    **Example:** Define $X^{(n)}(t) = W^{(n)}(t) + n \cdot g_n(t)$, where $g_n$ is a "spike" function: $g_n(t) = 0$ for $t$ outside the interval $(1/2 - 1/n^2, 1/2 + 1/n^2)$, and $g_n(1/2) = 1/n$, with $g_n$ piecewise linear. Then for any fixed $t \neq 1/2$, $g_n(t) = 0$ for large enough $n$, so the finite-dimensional distributions of $X^{(n)}$ converge to those of $W$. But $\|X^{(n)} - W^{(n)}\|_\infty \geq n \cdot g_n(1/2) = 1$ for all $n$, so $\sup_t |X^{(n)}(t)|$ does not converge to $\sup_t |W_t|$. The laws of $X^{(n)}$ are not tight because the spike prevents equicontinuity.

---

**Exercise 4.** The tightness estimate states $\mathbb{E}[(W^{(n)}(t) - W^{(n)}(s))^4] \leq C|t-s|^2$. For the symmetric random walk with $s$ and $t$ both multiples of $1/n$, compute $\mathbb{E}[(W^{(n)}(t) - W^{(n)}(s))^4]$ exactly in terms of $n$ and $|t-s|$. (Hint: the increment is $(\lfloor n|t-s| \rfloor)^{-1/2}$ times $S_{\lfloor n|t-s| \rfloor}$, and use $\mathbb{E}[S_m^4] = 3m^2 - 2m$.)

??? success "Solution to Exercise 4"
    Let $s$ and $t$ be multiples of $1/n$, and set $m = n|t-s|$ (an integer). The increment is:

    $$
    W^{(n)}(t) - W^{(n)}(s) = \frac{S_{n|t-s|} - S_0}{\sqrt{n}} = \frac{S_m}{\sqrt{n}}
    $$

    where $S_m = \sum_{i=1}^{m} \xi_i$ is a symmetric random walk of $m$ steps (reindexed). Therefore:

    $$
    \mathbb{E}[(W^{(n)}(t) - W^{(n)}(s))^4] = \frac{\mathbb{E}[S_m^4]}{n^2} = \frac{3m^2 - 2m}{n^2}
    $$

    Substituting $m = n|t-s|$:

    $$
    = \frac{3n^2|t-s|^2 - 2n|t-s|}{n^2} = 3|t-s|^2 - \frac{2|t-s|}{n}
    $$

    For all $n \geq 1$:

    $$
    \mathbb{E}[(W^{(n)}(t) - W^{(n)}(s))^4] \leq 3|t-s|^2
    $$

    This confirms the tightness estimate with constant $C = 3$.

---

**Exercise 5.** Donsker's theorem holds for any i.i.d. sequence with mean 0 and variance 1 (universality). Consider $\xi_i$ uniformly distributed on $\{-\sqrt{3}, 0, +\sqrt{3}\}$ with equal probabilities $1/3$. Verify that $\mathbb{E}[\xi_i] = 0$ and $\text{Var}(\xi_i) = 1$, so Donsker's theorem applies. What is qualitatively different about the paths of this scaled walk compared to the $\pm 1$ walk?

??? success "Solution to Exercise 5"
    With $\xi_i$ uniform on $\{-\sqrt{3}, 0, +\sqrt{3}\}$, each with probability $1/3$:

    $$
    \mathbb{E}[\xi_i] = \frac{1}{3}(-\sqrt{3}) + \frac{1}{3}(0) + \frac{1}{3}(\sqrt{3}) = 0
    $$

    $$
    \mathbb{E}[\xi_i^2] = \frac{1}{3}(3) + \frac{1}{3}(0) + \frac{1}{3}(3) = 2
    $$

    Therefore $\text{Var}(\xi_i) = \mathbb{E}[\xi_i^2] - (\mathbb{E}[\xi_i])^2 = 2 - 0 = 2$. The exercise states "verify that $\text{Var}(\xi_i) = 1$," but in fact the variance is 2. Donsker's theorem in its general form requires the scaled walk $W^{(n)}(t) = S_{\lfloor nt \rfloor}/(\sigma\sqrt{n})$ where $\sigma^2 = \text{Var}(\xi_i)$. With $\sigma = \sqrt{2}$, the properly normalized walk $W^{(n)}(t) = S_{\lfloor nt \rfloor}/(\sqrt{2n})$ satisfies $W^{(n)} \Rightarrow W$ in $C[0,T]$.

    **Qualitative difference:** With probability $1/3$ the step is 0, so the walk stays put. The paths of the scaled walk have "flat spots" (intervals where no movement occurs), unlike the $\pm 1$ walk which moves at every step. Additionally, the step size $\sqrt{3}$ is larger than 1, so when the walk does move, it takes bigger jumps. Despite these differences, the continuous limit is the same standard Brownian motion — this is the universality (invariance) principle at work.

---

**Exercise 6.** Using Donsker's theorem and the continuous mapping theorem, prove that the distribution of $\int_0^1 (W^{(n)}(t))^2 \, dt$ converges to the distribution of $\int_0^1 W_t^2 \, dt$ as $n \to \infty$. The latter is known to have the distribution of $\sum_{k=1}^\infty \frac{Z_k^2}{(k - 1/2)^2 \pi^2}$ where $Z_k$ are i.i.d. standard normal. What is $\mathbb{E}[\int_0^1 W_t^2 \, dt]$?

??? success "Solution to Exercise 6"
    Define the functional $\Phi: C[0,1] \to \mathbb{R}$ by $\Phi(f) = \int_0^1 f(t)^2\,dt$. This is a continuous functional on $C[0,1]$ with the supremum norm: if $\|f_n - f\|_\infty \to 0$, then:

    $$
    \left|\int_0^1 f_n(t)^2\,dt - \int_0^1 f(t)^2\,dt\right| \leq \int_0^1 |f_n(t)^2 - f(t)^2|\,dt \leq \|f_n + f\|_\infty \cdot \|f_n - f\|_\infty \to 0
    $$

    By Donsker's theorem, $W^{(n)} \Rightarrow W$ in $C[0,1]$. By the continuous mapping theorem, $\Phi(W^{(n)}) \Rightarrow \Phi(W)$, i.e.:

    $$
    \int_0^1 (W^{(n)}(t))^2\,dt \xrightarrow{d} \int_0^1 W_t^2\,dt
    $$

    For the expected value, using Fubini's theorem:

    $$
    \mathbb{E}\!\left[\int_0^1 W_t^2\,dt\right] = \int_0^1 \mathbb{E}[W_t^2]\,dt = \int_0^1 t\,dt = \frac{1}{2}
    $$
