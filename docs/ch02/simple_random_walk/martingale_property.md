# Martingale Property

Recall (see [§ Martingale](../filtration_and_martingale/martingale.md)): a process $\{X_n\}$ adapted to $\{\mathcal{F}_n\}$ with $\mathbb{E}|X_n|<\infty$ is a **martingale** if $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$.

Let $\mathcal{F}_n = \sigma(\xi_1, \ldots, \xi_n)$ be the natural filtration. The process $S_n = \sum_{i=1}^n \xi_i$ is adapted to $\{\mathcal{F}_n\}$ and integrable.

---

## The Martingale Property

**Proposition 1.1.3** (Martingale Property). If $p = 1/2$, then $\{S_n, \mathcal{F}_n\}$ is a martingale:

$$\mathbb{E}[S_{n+1} \mid \mathcal{F}_n]
= \mathbb{E}[S_n + \xi_{n+1} \mid \mathcal{F}_n]
= S_n + \mathbb{E}[\xi_{n+1}]
= S_n. \quad\square$$

!!! note "Asymmetric case"
    If $p \neq 1/2$, then $\mathbb{E}[\xi_{n+1}] = 2p-1 \neq 0$, so $\mathbb{E}[S_{n+1} \mid \mathcal{F}_n] = S_n + (2p-1)$ and the walk is a sub/supermartingale.

---

## The Quadratic Martingale

**Proposition 1.1.4** (Quadratic Martingale). The process $M_n := S_n^2 - n$ is a martingale.

**Proof.**

$$\mathbb{E}[M_{n+1} \mid \mathcal{F}_n]
= \mathbb{E}[(S_n + \xi_{n+1})^2 \mid \mathcal{F}_n] - (n+1)
= S_n^2 + 1 - (n+1)
= S_n^2 - n = M_n. \quad\square$$

---

## Quadratic Variation

**Definition 1.1.4.** $[S]_n := \sum_{i=1}^n (S_i - S_{i-1})^2 = \sum_{i=1}^n \xi_i^2$.

**Proposition 1.1.5.** $[S]_n = n$ almost surely (since $\xi_i^2 = 1$). $\square$

The quadratic variation is deterministic. The decomposition $S_n^2 = [S]_n + M_n$ is the discrete analogue of the Itô decomposition $W_t^2 = t + 2\int_0^t W_s\,dW_s$.

---

## References

- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
- Williams, D. (1991). *Probability with Martingales*. Cambridge University Press.
- Lawler, G. F., & Limic, V. (2010). *Random Walk: A Modern Introduction*. Cambridge University Press.

---

## Exercises

**Exercise 1.** For the asymmetric random walk with $p \neq 1/2$, show that the process $M_n = S_n - n(2p-1)$ is a martingale. Then show that $M_n^2 - 4np(1-p)$ is also a martingale. What are the analogues of Propositions 1.1.3 and 1.1.4 for the centred walk?

??? success "Solution to Exercise 1"
    For the asymmetric walk, $\mathbb{E}[\xi_{n+1}] = 2p - 1 \neq 0$. Define $M_n = S_n - n(2p-1)$. Then:

    $$
    \mathbb{E}[M_{n+1} \mid \mathcal{F}_n] = \mathbb{E}[S_{n+1} - (n+1)(2p-1) \mid \mathcal{F}_n]
    $$

    $$
    = S_n + \mathbb{E}[\xi_{n+1}] - (n+1)(2p-1) = S_n + (2p-1) - (n+1)(2p-1) = S_n - n(2p-1) = M_n
    $$

    So $\{M_n\}$ is a martingale. For the quadratic martingale, let $\sigma^2 = \text{Var}(\xi_i) = 4p(1-p)$. Consider $M_n^2 - n\sigma^2$:

    $$
    \mathbb{E}[M_{n+1}^2 \mid \mathcal{F}_n] = \mathbb{E}[(M_n + \eta_{n+1})^2 \mid \mathcal{F}_n]
    $$

    where $\eta_{n+1} = \xi_{n+1} - (2p-1)$ has mean 0 and variance $\sigma^2 = 4p(1-p)$. Expanding:

    $$
    = M_n^2 + 2M_n \cdot \mathbb{E}[\eta_{n+1}] + \mathbb{E}[\eta_{n+1}^2] = M_n^2 + \sigma^2
    $$

    Therefore $\mathbb{E}[M_{n+1}^2 - (n+1)\sigma^2 \mid \mathcal{F}_n] = M_n^2 + \sigma^2 - (n+1)\sigma^2 = M_n^2 - n\sigma^2$, confirming $M_n^2 - 4np(1-p)$ is a martingale.

    These are the analogues of Propositions 1.1.3 and 1.1.4: the centred walk $M_n = S_n - n\mu$ replaces $S_n$, and the compensator $n\sigma^2 = 4np(1-p)$ replaces $n$.

---

**Exercise 2.** Let $\{S_n\}$ be a symmetric random walk. Use the Optional Stopping Theorem applied to the martingale $M_n = S_n^2 - n$ and the stopping time $\tau = \min\{n : S_n = -a \text{ or } S_n = b\}$ (with $a, b > 0$) to show that $\mathbb{E}[\tau] = ab$.

??? success "Solution to Exercise 2"
    The stopping time $\tau = \min\{n : S_n = -a \text{ or } S_n = b\}$ is finite a.s. by recurrence, and bounded by the first hitting time of the boundary. Applying the Optional Stopping Theorem to $M_n = S_n^2 - n$:

    $$
    \mathbb{E}[M_\tau] = \mathbb{E}[M_0] = S_0^2 - 0 = 0
    $$

    Therefore $\mathbb{E}[S_\tau^2] = \mathbb{E}[\tau]$. At the stopping time, $S_\tau \in \{-a, b\}$, so:

    $$
    \mathbb{E}[S_\tau^2] = a^2 \cdot \mathbb{P}(S_\tau = -a) + b^2 \cdot \mathbb{P}(S_\tau = b)
    $$

    From the first martingale $\mathbb{E}[S_\tau] = 0$:

    $$
    -a \cdot \mathbb{P}(S_\tau = -a) + b \cdot \mathbb{P}(S_\tau = b) = 0
    $$

    With $\mathbb{P}(S_\tau = -a) + \mathbb{P}(S_\tau = b) = 1$, solving gives $\mathbb{P}(S_\tau = b) = a/(a+b)$ and $\mathbb{P}(S_\tau = -a) = b/(a+b)$. Therefore:

    $$
    \mathbb{E}[\tau] = a^2 \cdot \frac{b}{a+b} + b^2 \cdot \frac{a}{a+b} = \frac{ab(a+b)}{a+b} = ab
    $$

---

**Exercise 3.** Prove that the exponential process $Z_n = \left(\frac{1-p}{p}\right)^{S_n}$ is a martingale for any $p \in (0,1)$. For $p = 1/2$, what does this process simplify to, and why is it trivial?

??? success "Solution to Exercise 3"
    Let $Z_n = \left(\frac{1-p}{p}\right)^{S_n}$ and $r = \frac{1-p}{p}$. Then:

    $$
    \mathbb{E}[Z_{n+1} \mid \mathcal{F}_n] = \mathbb{E}[r^{S_{n+1}} \mid \mathcal{F}_n] = \mathbb{E}[r^{S_n + \xi_{n+1}} \mid \mathcal{F}_n] = r^{S_n} \cdot \mathbb{E}[r^{\xi_{n+1}}]
    $$

    Computing the expectation:

    $$
    \mathbb{E}[r^{\xi_{n+1}}] = p \cdot r + (1-p) \cdot r^{-1} = p \cdot \frac{1-p}{p} + (1-p) \cdot \frac{p}{1-p} = (1-p) + p = 1
    $$

    Therefore $\mathbb{E}[Z_{n+1} \mid \mathcal{F}_n] = r^{S_n} = Z_n$, so $\{Z_n\}$ is a martingale.

    For $p = 1/2$: $r = (1-1/2)/(1/2) = 1$, so $Z_n = 1^{S_n} = 1$ for all $n$. The process is the constant martingale $Z_n = 1$, which is trivial (it carries no information about $S_n$).

---

**Exercise 4.** Show that the discrete quadratic variation $[S]_n = n$ implies that the process $S_n^2 - [S]_n = S_n^2 - n$ is a martingale. In other words, derive Proposition 1.1.4 from Proposition 1.1.5 without directly computing $\mathbb{E}[S_{n+1}^2 \mid \mathcal{F}_n]$. (Hint: write $S_{n+1}^2 - S_n^2 = 2S_n \xi_{n+1} + \xi_{n+1}^2$ and use $\xi_{n+1}^2 = [S]_{n+1} - [S]_n = 1$.)

??? success "Solution to Exercise 4"
    We have $S_{n+1}^2 - S_n^2 = (S_n + \xi_{n+1})^2 - S_n^2 = 2S_n\xi_{n+1} + \xi_{n+1}^2$. Since $\xi_{n+1}^2 = [S]_{n+1} - [S]_n = 1$:

    $$
    S_{n+1}^2 - [S]_{n+1} = S_n^2 + 2S_n\xi_{n+1} + 1 - ([S]_n + 1) = (S_n^2 - [S]_n) + 2S_n\xi_{n+1}
    $$

    Taking conditional expectations:

    $$
    \mathbb{E}[S_{n+1}^2 - [S]_{n+1} \mid \mathcal{F}_n] = S_n^2 - [S]_n + 2S_n \cdot \mathbb{E}[\xi_{n+1} \mid \mathcal{F}_n]
    $$

    Since $\xi_{n+1}$ is independent of $\mathcal{F}_n$ and $\mathbb{E}[\xi_{n+1}] = 0$:

    $$
    = S_n^2 - [S]_n + 0 = S_n^2 - [S]_n
    $$

    Since $[S]_n = n$ a.s., this gives $\mathbb{E}[S_{n+1}^2 - (n+1) \mid \mathcal{F}_n] = S_n^2 - n$, which is exactly the statement that $\{S_n^2 - n\}$ is a martingale (Proposition 1.1.4), derived without directly computing $\mathbb{E}[S_{n+1}^2 \mid \mathcal{F}_n]$.

---

**Exercise 5.** Let $\lambda \in \mathbb{R}$ and define $E_n = e^{\lambda S_n} / (\cosh \lambda)^n$. Prove that $\{E_n\}$ is a martingale. Use this to derive the MGF of the hitting time $\tau_a = \min\{n \geq 0 : S_n = a\}$ for $a > 0$: show that $\mathbb{E}[(\cosh \lambda)^{-\tau_a}] = e^{-\lambda a}$ for $\lambda > 0$ (under appropriate stopping conditions).

??? success "Solution to Exercise 5"
    Define $E_n = e^{\lambda S_n}/(\cosh \lambda)^n$. Then:

    $$
    \mathbb{E}[E_{n+1} \mid \mathcal{F}_n] = \frac{e^{\lambda S_n}}{(\cosh\lambda)^{n+1}} \cdot \mathbb{E}[e^{\lambda \xi_{n+1}}] = \frac{e^{\lambda S_n}}{(\cosh\lambda)^{n+1}} \cdot \cosh\lambda = \frac{e^{\lambda S_n}}{(\cosh\lambda)^n} = E_n
    $$

    So $\{E_n\}$ is a martingale. Now apply the Optional Stopping Theorem to $\tau_a = \min\{n : S_n = a\}$. At the stopping time, $S_{\tau_a} = a$, so:

    $$
    \mathbb{E}[E_{\tau_a}] = E_0 = 1
    $$

    $$
    \mathbb{E}\!\left[\frac{e^{\lambda a}}{(\cosh\lambda)^{\tau_a}}\right] = 1
    $$

    Therefore:

    $$
    \mathbb{E}[(\cosh\lambda)^{-\tau_a}] = e^{-\lambda a}
    $$

    This holds for $\lambda > 0$ under appropriate conditions ensuring the Optional Stopping Theorem applies (e.g., $\tau_a < \infty$ a.s. by recurrence, and the stopped process is uniformly integrable, which holds since $\cosh\lambda > 1$ for $\lambda > 0$ makes $E_{n \wedge \tau_a}$ bounded by $e^{\lambda a}$).

---

**Exercise 6.** A process $\{X_n\}$ is called a **submartingale** if $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] \geq X_n$. Show that $|S_n|$ is a submartingale for the symmetric random walk. (Hint: use Jensen's inequality with the convex function $f(x) = |x|$.)

??? success "Solution to Exercise 6"
    Since $\{S_n\}$ is a martingale (for $p = 1/2$) and $f(x) = |x|$ is a convex function, Jensen's inequality for conditional expectations gives:

    $$
    \mathbb{E}[|S_{n+1}| \mid \mathcal{F}_n] \geq |\mathbb{E}[S_{n+1} \mid \mathcal{F}_n]| = |S_n|
    $$

    We also need to verify the other conditions: $|S_n|$ is adapted (since $S_n$ is adapted), and $\mathbb{E}[|S_n|] < \infty$ (since $\mathbb{E}[|S_n|] \leq \sqrt{\mathbb{E}[S_n^2]} = \sqrt{n} < \infty$).

    Therefore $\{|S_n|\}$ satisfies $\mathbb{E}[|S_{n+1}| \mid \mathcal{F}_n] \geq |S_n|$, which is the submartingale condition.

---

**Exercise 7.** Quadratic Variation on Arbitrary Partitions.

Let $W^{(n)}$ be the piecewise-linear scaled random walk from [Scaling Limit](scaling_limit.md), and let

$$\Pi = \{0 = t_0 < t_1 < \cdots < t_m = T\}$$

be a partition of $[0,T]$ with each $t_i$ a multiple of $1/n$, so that each subinterval $[t_i, t_{i+1}]$ contains exactly one increment $\xi_j$.

**(a)** Show that

$$\mathbb{E}\!\left[\sum_{i=0}^{m-1} (W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2\right] = T$$

**(b)** Show that

$$\sum_{i=0}^{m-1} (W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2 = T \quad \text{almost surely}$$

(not merely in expectation). *Hint:* $W^{(n)}$ is piecewise linear with exactly one increment $\xi_j$ per subinterval. Use the fact that $\xi_j^2 = 1$ almost surely to evaluate each squared increment explicitly.

**(c)** For a differentiable function $f: [0,T] \to \mathbb{R}$ with bounded derivative, show that

$$\sum_{i=0}^{m-1} (f(t_{i+1}) - f(t_i))^2 \to 0 \quad \text{as } |\Pi| \to 0$$

Explain why this distinguishes random walk paths from smooth paths.

??? success "Solution to Exercise 7"
    **(a)** The partition has $m$ subintervals, each of length $1/n$, so $m = nT$. Each subinterval contains exactly one increment $\xi_j/\sqrt{n}$, with $(W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2 = \xi_j^2/n$. Taking expectations:

    $$
    \mathbb{E}\!\left[\sum_{i=0}^{m-1}(W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2\right] = \sum_{i=0}^{m-1} \frac{\mathbb{E}[\xi_j^2]}{n} = \frac{m}{n} = T
    $$

    **(b)** Since $\xi_j^2 = 1$ almost surely, each squared increment is $1/n$ almost surely (not just in expectation):

    $$
    \sum_{i=0}^{m-1}(W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2 = \frac{m}{n} = T \quad \text{almost surely}
    $$

    **(c)** By the Mean Value Theorem, $f(t_{i+1}) - f(t_i) = f'(c_i)(t_{i+1} - t_i)$ for some $c_i \in (t_i, t_{i+1})$. If $|f'| \leq M$:

    $$
    \sum_{i=0}^{m-1}(f(t_{i+1}) - f(t_i))^2 \leq M^2 \sum_{i=0}^{m-1}(\Delta t_i)^2 \leq M^2 |\Pi| T \to 0
    $$

    For smooth functions the quadratic variation vanishes; for random walk paths it equals $T > 0$. This non-vanishing quadratic variation is the hallmark of "infinite roughness" and gives rise to the Itô correction term.

---

**Exercise 8.** Gambler's Ruin.

A gambler starts with \$$a$ and bets \$1 per round on a fair coin flip. The walk $\{S_n\}$ starts at $S_0 = a$ and is absorbed at the barriers 0 and $b$ (with $b > a$). Let

$$\tau_0 = \inf\{n : S_n = 0\}, \qquad \tau_b = \inf\{n : S_n = b\}, \qquad \tau = \tau_0 \wedge \tau_b$$

**(a)** Using the martingale $\{S_n\}$ (Proposition 1.1.3) and the Optional Stopping Theorem, show that

$$\mathbb{P}(\tau_b < \tau_0) = \frac{a}{b}$$

**(b)** Let $b \to \infty$. Show that $\mathbb{P}(\tau_0 < \infty) = 1$: the gambler is ruined with probability 1 in an unbounded game.

**(c)** Using the martingale $\{S_n^2 - n\}$ (Proposition 1.1.4) and the Optional Stopping Theorem, show that

$$\mathbb{E}[\tau] = \mathbb{E}[\tau_0 \wedge \tau_b] = a(b - a)$$

??? success "Solution to Exercise 8"
    **(a)** Since $\{S_n\}$ is a martingale, the Optional Stopping Theorem gives $\mathbb{E}[S_\tau] = \mathbb{E}[S_0] = a$. At stopping, $S_\tau \in \{0, b\}$:

    $$
    a = b \cdot \mathbb{P}(\tau_b < \tau_0)
    $$

    Therefore $\mathbb{P}(\tau_b < \tau_0) = a/b$.

    **(b)** Letting $b \to \infty$: $\mathbb{P}(\tau_0 < \tau_b) = 1 - a/b \to 1$. Since $\{\tau_0 < \tau_b\} \nearrow \{\tau_0 < \infty\}$ as $b \to \infty$, $\mathbb{P}(\tau_0 < \infty) = 1$.

    **(c)** The martingale $M_n = S_n^2 - n$ gives $\mathbb{E}[M_\tau] = a^2$, so $\mathbb{E}[\tau] = \mathbb{E}[S_\tau^2] - a^2$. Computing $\mathbb{E}[S_\tau^2] = b^2 \cdot (a/b) = ab$:

    $$
    \mathbb{E}[\tau] = ab - a^2 = a(b-a)
    $$
