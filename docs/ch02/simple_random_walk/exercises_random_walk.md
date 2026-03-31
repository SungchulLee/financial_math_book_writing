# Exercises

---

## Exercise 1 — Quadratic Variation

Let $W^{(n)}$ be the piecewise-linear scaled random walk from [Scaling Limit](scaling_limit.md), and let

$$\Pi = \{0 = t_0 < t_1 < \cdots < t_m = T\}$$

be a partition of $[0,T]$ with each $t_i$ a multiple of $1/n$, so that each subinterval $[t_i, t_{i+1}]$ contains exactly one increment $\xi_j$.

**(a)** Show that

$$\mathbb{E}\!\left[\sum_{i=0}^{m-1} (W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2\right] = T$$

**(b)** Show that

$$\sum_{i=0}^{m-1} (W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2 = T \quad \text{almost surely}$$

(not merely in expectation). *Hint:* $W^{(n)}$ is piecewise linear with exactly one increment $\xi_j$ per subinterval. Use the fact that $\xi_j^2 = 1$ almost surely to evaluate each squared increment explicitly — no randomness survives the squaring.

**(c)** For a differentiable function $f: [0,T] \to \mathbb{R}$ with bounded derivative, show that

$$\sum_{i=0}^{m-1} (f(t_{i+1}) - f(t_i))^2 \to 0 \quad \text{as } |\Pi| \to 0$$

Explain why this distinguishes random walk paths from smooth paths.

---

## Exercise 2 — Higher Moments

Let $S_n = \sum_{i=1}^n \xi_i$ be the symmetric random walk.

**(a)** Verify $\mathbb{E}[S_n^2] = n$ by direct expansion, without using the variance formula.

**(b)** Using the pairing argument from [Moments](moments_of_random_walk.md) (Proposition 1.1.1), compute $\mathbb{E}[S_n^6]$.

*Hint:* $\mathbb{E}[\xi_{i_1}\cdots\xi_{i_6}]$ is nonzero only when every distinct index appears an even number of times. The cases where this holds (and $\mathbb{E}[\xi^{\text{odd power}}] = 0$ does not force zero) are: (i) all six indices equal; (ii) one group of four equal indices and one pair; (iii) three distinct pairs. The case of two groups of three equal indices gives $\mathbb{E}[\xi_a^3]\mathbb{E}[\xi_b^3] = 0$ because odd moments vanish, so this case does not contribute.

**(c)** Show that as $n \to \infty$:

$$\mathbb{E}[S_n^{2k}] = (2k-1)!!\, n^k + O(n^{k-1})$$

where $(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1)$. Compare with the Brownian motion moments $\mathbb{E}[W_1^{2k}] = (2k-1)!!$ and explain the connection.

---

## Exercise 3 — Gambler's Ruin

A gambler starts with $\$a$ and bets $\$1$ per round on a fair coin flip. The walk $\{S_n\}$ starts at $S_0 = a$ and is absorbed at the barriers 0 and $b$ (with $b > a$). Let

$$\tau_0 = \inf\{n : S_n = 0\}, \qquad \tau_b = \inf\{n : S_n = b\}, \qquad \tau = \tau_0 \wedge \tau_b$$

**(a)** Using the martingale $\{S_n\}$ (Proposition 1.1.3) and the Optional Stopping Theorem applied to the bounded stopping time $\tau$, show that

$$\mathbb{P}(\tau_b < \tau_0) = \frac{a}{b}$$

**(b)** Let $b \to \infty$. Show that $\mathbb{P}(\tau_0 < \infty) = 1$: the gambler is ruined with probability 1 in an unbounded game.

To reconcile this with Theorem 1.1.7 (recurrence): the unrestricted walk is recurrent and visits every integer infinitely often, including 0. However, in the gambler's ruin setup the walk starts at $a > 0$ and is *absorbed* at 0 — it cannot continue after reaching 0. There is no contradiction: recurrence describes the unrestricted walk, while ruin describes the absorbed walk.

**(c)** Using the martingale $\{S_n^2 - n\}$ (Proposition 1.1.4) and the Optional Stopping Theorem, show that

$$\mathbb{E}[\tau] = \mathbb{E}[\tau_0 \wedge \tau_b] = a(b - a)$$

As $b \to \infty$, $\mathbb{E}[\tau_0 \wedge \tau_b] = a(b-a) \to \infty$. Since $\tau_0 \wedge \tau_b \nearrow \tau_0$ as $b \to \infty$ — because for large enough $b$, ruin at 0 occurs before the walk reaches $b$, so $\tau_0 < \tau_b$ and $\tau_0 \wedge \tau_b = \tau_0$ — monotone convergence gives $\mathbb{E}[\tau_0] = \lim_{b\to\infty} \mathbb{E}[\tau_0 \wedge \tau_b] = \infty$. The expected time to ruin is infinite, even though ruin is certain — the gambler is ruined with probability 1, but ruin can take arbitrarily long.

---

## Exercise 4 — Reflection Principle (Preview)

Let $M_n = \max_{0 \leq k \leq n} S_k$ be the running maximum of the symmetric random walk.

**(a)** By a symmetry argument, show that for $m > 0$:

$$\mathbb{P}(M_n \geq m) = 2\,\mathbb{P}(S_n \geq m) - \mathbb{P}(S_n = m)$$

*Hint:* Consider the "reflected" path obtained by flipping all steps after the first time the walk hits $m$. Show that $\{\text{walk hits } m \text{ and ends above } m\}$, $\{\text{walk hits } m \text{ and ends at } m\}$, and $\{\text{walk hits } m \text{ and ends below } m\}$ account for all paths reaching $m$, and that the first and third events have equal probability by symmetry.

**(b)** Use part (a) and the normal approximation to show that for large $n$:

$$\mathbb{P}\!\left(\frac{M_n}{\sqrt{n}} \geq x\right) \approx 2\,\mathbb{P}\!\left(\mathcal{N}(0,1) \geq x\right) = 2\bigl(1-\Phi(x)\bigr), \qquad x > 0$$

where $\Phi$ is the standard normal CDF. This is the exact distribution of $\max_{0 \leq t \leq 1} W_t$ for Brownian motion, which will be derived rigorously in a later chapter.

---

---

## Solutions

??? success "Solution to Exercise 1"
    **(a)** The partition has $m$ subintervals, each of length $1/n$, so $m = nT$. Each subinterval contains exactly one increment $\xi_j/\sqrt{n}$, with $(W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2 = \xi_j^2/n$. Taking expectations:

    $$
    \mathbb{E}\!\left[\sum_{i=0}^{m-1}(W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2\right] = \sum_{i=0}^{m-1} \frac{\mathbb{E}[\xi_j^2]}{n} = \sum_{i=0}^{m-1}\frac{1}{n} = \frac{m}{n} = \frac{nT}{n} = T
    $$

    **(b)** Since $\xi_j^2 = 1$ almost surely (because $\xi_j \in \{-1, +1\}$), each squared increment is $\xi_j^2/n = 1/n$ almost surely (not just in expectation). Therefore:

    $$
    \sum_{i=0}^{m-1}(W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2 = \sum_{i=0}^{m-1}\frac{1}{n} = \frac{m}{n} = T \quad \text{almost surely}
    $$

    **(c)** By the Mean Value Theorem, $f(t_{i+1}) - f(t_i) = f'(c_i)(t_{i+1} - t_i)$ for some $c_i \in (t_i, t_{i+1})$. If $|f'| \leq M$:

    $$
    \sum_{i=0}^{m-1}(f(t_{i+1}) - f(t_i))^2 = \sum_{i=0}^{m-1}(f'(c_i))^2(\Delta t_i)^2 \leq M^2 \sum_{i=0}^{m-1}(\Delta t_i)^2 \leq M^2 |\Pi| \sum_{i=0}^{m-1}\Delta t_i = M^2 |\Pi| T \to 0
    $$

    as $|\Pi| \to 0$. For smooth functions the quadratic variation vanishes, while for random walk paths it equals $T > 0$. This non-vanishing quadratic variation is the hallmark of paths with "infinite roughness" and is what gives rise to the Itô correction term.

??? success "Solution to Exercise 2"
    **(a)** $\mathbb{E}[S_n^2] = \sum_{i,j=1}^n \mathbb{E}[\xi_i\xi_j]$. For $i = j$: $\mathbb{E}[\xi_i^2] = 1$, contributing $n$ terms. For $i \neq j$: $\mathbb{E}[\xi_i\xi_j] = \mathbb{E}[\xi_i]\mathbb{E}[\xi_j] = 0$. Therefore $\mathbb{E}[S_n^2] = n$.

    **(b)** We need to count ordered 6-tuples $(i_1,\ldots,i_6)$ where each distinct index appears an even number of times:

    - **All six equal** ($i_1 = \cdots = i_6$): $\mathbb{E}[\xi_i^6] = 1$. There are $n$ choices. Contribution: $n$.
    - **One group of 4, one group of 2** (e.g., index $a$ appears 4 times, index $b$ appears 2 times, $a \neq b$): $\mathbb{E}[\xi_a^4]\mathbb{E}[\xi_b^2] = 1$. The number of ways to choose which 4 of the 6 slots get index $a$ is $\binom{6}{4} = 15$. Ordered pairs $(a,b)$ with $a \neq b$: $n(n-1)$. Contribution: $15n(n-1)$.
    - **Three distinct pairs** (indices $a, b, c$ each appearing exactly twice, all distinct): $\mathbb{E}[\xi_a^2]\mathbb{E}[\xi_b^2]\mathbb{E}[\xi_c^2] = 1$. The number of ways to partition 6 slots into 3 pairs is $\frac{6!}{(2!)^3 \cdot 3!} \cdot 3! = \frac{6!}{(2!)^3} = 90$. Wait — we need to be more careful. The number of ways to assign 3 distinct labels $(a,b,c)$ to 6 positions so that each label appears exactly twice is $\binom{6}{2}\binom{4}{2}\binom{2}{2} = 90$. The number of ordered triples $(a,b,c)$ of distinct indices is $n(n-1)(n-2)$. But since relabelling $(a,b,c)$ among themselves is already accounted for in the 90 slot assignments (each assignment specifies which slots get $a$, which get $b$, which get $c$), we use ordered triples: $n(n-1)(n-2)$. But actually the 90 already counts assignments distinguishing $a,b,c$. So contribution: $90 \cdot \frac{n(n-1)(n-2)}{3!} \cdot 1$... Let us count differently. The sum over ordered 6-tuples where exactly 3 distinct values each appear exactly twice: pick the 3 distinct values as an ordered triple $(a,b,c)$: $n(n-1)(n-2)/6$ unordered triples, but we should count ordered tuples. The number of ordered 6-tuples with $a$ appearing in 2 specified positions, $b$ in 2, $c$ in 2 is: pick 2 positions for $a$ ($\binom{6}{2}$), 2 for $b$ ($\binom{4}{2}$), remaining 2 for $c$: $15 \times 6 = 90$. Multiply by ordered triples: but this overcounts by $3!$ since permuting $(a,b,c)$ with their slot assignments gives the same 6-tuple only if we also permute slots — which we don't. So total ordered 6-tuples: $90 \times \frac{n!}{(n-3)!} / 3! \cdot 3! = 90 \times n(n-1)(n-2)/1$... Actually the simplest approach: for each unordered set $\{a,b,c\}$ of 3 distinct indices, the number of ordered 6-tuples using exactly these indices, each twice, is $\frac{6!}{2!2!2!} = 90$. The number of such sets is $\binom{n}{3}$. Contribution: $90\binom{n}{3} = 15n(n-1)(n-2)$.

    Total: $\mathbb{E}[S_n^6] = n + 15n(n-1) + 15n(n-1)(n-2) = n + 15n^2 - 15n + 15n^3 - 45n^2 + 30n = 15n^3 - 30n^2 + 16n$.

    **(c)** The leading term of $\mathbb{E}[S_n^{2k}]$ comes from the case where all indices appear in distinct pairs. The number of ways to pair $2k$ slots is $(2k-1)!! = (2k)!/(2^k k!)$, and the number of ways to choose $k$ distinct indices is $\sim n^k/k!$ (but the pairing already accounts for the ordering). More precisely, for each of the $(2k-1)!!$ pairings, the number of ordered $2k$-tuples is asymptotically $n^k$, giving leading term $(2k-1)!! \cdot n^k$. The lower-order terms arise from index collisions and contribute $O(n^{k-1})$.

    For Brownian motion: $\mathbb{E}[W_1^{2k}] = (2k-1)!!$ since $W_1 \sim \mathcal{N}(0,1)$ and the $2k$-th moment of a standard normal is $(2k-1)!!$. The connection is the CLT: $S_n/\sqrt{n} \to \mathcal{N}(0,1)$, so $\mathbb{E}[(S_n/\sqrt{n})^{2k}] = \mathbb{E}[S_n^{2k}]/n^k \to (2k-1)!!$.

??? success "Solution to Exercise 3"
    **(a)** Since $\{S_n\}$ is a martingale, the Optional Stopping Theorem gives $\mathbb{E}[S_\tau] = \mathbb{E}[S_0] = a$. At stopping, $S_\tau \in \{0, b\}$:

    $$
    a = 0 \cdot \mathbb{P}(S_\tau = 0) + b \cdot \mathbb{P}(S_\tau = b) = b \cdot \mathbb{P}(\tau_b < \tau_0)
    $$

    Therefore $\mathbb{P}(\tau_b < \tau_0) = a/b$.

    **(b)** Letting $b \to \infty$: $\mathbb{P}(\tau_0 < \tau_b) = 1 - a/b \to 1$. Since $\{\tau_0 < \tau_b\} \nearrow \{\tau_0 < \infty\}$ as $b \to \infty$ (for large enough $b$, ruin at 0 occurs before the walk ever reaches $b$), by continuity of probability: $\mathbb{P}(\tau_0 < \infty) = 1$.

    **(c)** The martingale $M_n = S_n^2 - n$ gives $\mathbb{E}[M_\tau] = \mathbb{E}[M_0] = a^2 - 0 = a^2$:

    $$
    \mathbb{E}[S_\tau^2 - \tau] = a^2
    $$

    $$
    \mathbb{E}[\tau] = \mathbb{E}[S_\tau^2] - a^2
    $$

    Computing $\mathbb{E}[S_\tau^2] = 0^2 \cdot (1-a/b) + b^2 \cdot (a/b) = ab$:

    $$
    \mathbb{E}[\tau] = ab - a^2 = a(b-a)
    $$

??? success "Solution to Exercise 4"
    **(a)** Let $p_m = \mathbb{P}(M_n \geq m)$ denote the probability that the walk reaches level $m$ by time $n$. Decompose this event according to the final position:

    - Paths that reach $m$ and end at $S_n = j \geq m$: these also satisfy $S_n \geq m$, so they are counted in $\mathbb{P}(S_n \geq m)$.
    - Paths that reach $m$ and end at $S_n = j < m$: by the reflection principle, reflect all steps after the first hitting time of $m$. This creates a bijection between paths that hit $m$ and end at $j < m$, and paths that hit $m$ and end at $2m - j > m$. The reflected paths end above $m$.

    The bijection shows: $\mathbb{P}(M_n \geq m,\, S_n < m) = \mathbb{P}(M_n \geq m,\, S_n > m) = \mathbb{P}(S_n > m)$ (since any path with $S_n > m$ must have $M_n \geq m$).

    Therefore:

    $$
    p_m = \mathbb{P}(S_n > m) + \mathbb{P}(S_n = m) + \mathbb{P}(S_n > m) = 2\mathbb{P}(S_n > m) + \mathbb{P}(S_n = m) = 2\mathbb{P}(S_n \geq m) - \mathbb{P}(S_n = m)
    $$

    **(b)** For large $n$, $S_n/\sqrt{n} \approx Z \sim \mathcal{N}(0,1)$ and $\mathbb{P}(S_n = m) \to 0$ (the point mass vanishes in the continuous limit). Therefore:

    $$
    \mathbb{P}\!\left(\frac{M_n}{\sqrt{n}} \geq x\right) \approx 2\mathbb{P}(S_n/\sqrt{n} \geq x) = 2\mathbb{P}(Z \geq x) = 2(1 - \Phi(x))
    $$

    This is $\mathbb{P}(\max_{0 \leq t \leq 1} W_t \geq x) = 2(1-\Phi(x))$, which is the exact distribution of the running maximum of Brownian motion on $[0,1]$.

---

## References

- Williams, D. (1991). *Probability with Martingales*. Cambridge University Press.
- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley.
