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

## References

- Williams, D. (1991). *Probability with Martingales*. Cambridge University Press.
- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley.
