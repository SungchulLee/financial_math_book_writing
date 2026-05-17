# Donsker's Theorem

Donsker's theorem upgrades convergence of random variables to convergence of entire paths: the scaled random walk $W^{(n)}$ converges as a process to Brownian motion in the path space $C[0,T]$.

---

## From Pointwise to Path Convergence

Recall (see [§ Proof of the CLT via MGF Convergence](mgf_of_random_walk.md)) that for each fixed $t$,

$$S^{(n)}(t) = \frac{S_{\lfloor nt \rfloor}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,t)$$

This is *pointwise-in-$t$* convergence of marginal distributions; Donsker's theorem strengthens this to convergence of the entire path.

Recall (see [§ The Scaled Random Walk](scaling_limit.md)) the construction of the piecewise-linear scaled walk $W^{(n)} \in C[0,T]$. Convergence of finite-dimensional distributions to those of $W$ is necessary but not sufficient for path-space convergence. The additional ingredient is **tightness**.

---

## Tightness

A sequence of probability measures $\{\mu_n\}$ on $C[0,T]$ is **tight** if for every $\varepsilon > 0$ there exists a compact $K \subset C[0,T]$ with $\mu_n(K) \geq 1 - \varepsilon$ for all $n$. By Arzelà–Ascoli, tightness of $\{W^{(n)}\}$ reduces to controlling the modulus of continuity, which follows from a fourth-moment bound via the **Kolmogorov continuity criterion** (Billingsley, 1999, Theorem 12.3); the bound itself is verified in Exercise 4.

---

## Donsker's Invariance Principle

**Theorem 1.1.11** (Donsker, 1951)

Let $\{\xi_i\}$ be i.i.d. with $\mathbb{E}[\xi_i] = 0$ and $\mathbb{E}[\xi_i^2] = 1$, and let $W^{(n)}$ be the piecewise-linear scaled walk

$$W^{(n)}(t) := \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor} + \frac{nt - \lfloor nt \rfloor}{\sqrt{n}}\,\xi_{\lfloor nt \rfloor+1}, \qquad t \in [0,T]$$

Then

$$W^{(n)} \Rightarrow W \quad \text{in } C[0,T] \text{ with the uniform topology}$$

where $\Rightarrow$ denotes weak convergence and $W$ is standard Brownian motion on $[0,T]$.

**Proof sketch.**

1. **Finite-dimensional convergence** via the CLT applied to disjoint blocks of increments.
2. **Tightness** via the fourth-moment estimate and Kolmogorov's criterion.
3. **Conclusion** by Prohorov's theorem. $\square$

---

## Step Functions vs. Piecewise-Linear Paths

Without interpolation, $S^{(n)}$ lives in the Skorokhod space $D[0,T]$ and satisfies $S^{(n)} \Rightarrow W$ in the Skorokhod topology. The piecewise-linear $W^{(n)} \in C[0,T]$ satisfies the stronger statement $W^{(n)} \Rightarrow W$ in the uniform topology. Since $\|S^{(n)} - W^{(n)}\|_\infty = 1/\sqrt{n} \to 0$ a.s., both yield the same weak limit.

---

## Universality

The limit depends only on the mean and variance of the steps, not on their distribution. This is the **invariance principle**: any i.i.d. sequence with $\mathbb{E}[\xi_i] = 0$, $\mathbb{E}[\xi_i^2] = 1$ produces the same Brownian limit.

---

## References

- Donsker, M. D. (1951). An invariance principle for certain probability limit theorems. *Memoirs of the American Mathematical Society*, 6, 1–12.
- Billingsley, P. (1999). *Convergence of Probability Measures*, 2nd ed. Wiley.
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
