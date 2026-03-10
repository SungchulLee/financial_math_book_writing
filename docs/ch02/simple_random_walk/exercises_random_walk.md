# Exercises


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

---

## Exercise 1 — Quadratic Variation

Let $W^{(n)}$ be the piecewise-linear scaled random walk from [Scaling Limit](scaling_limit.md), and let

$$\Pi = \{0 = t_0 < t_1 < \cdots < t_m = T\}$$

be a partition of $[0,T]$ with each $t_i$ a multiple of $1/n$, so that each subinterval $[t_i, t_{i+1}]$ contains exactly one increment $\xi_j$.

**(a)** Show that

$$\mathbb{E}\!\left[\sum_{i=0}^{m-1} (W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2\right] = T$$

**(b)** Show that

$$\sum_{i=0}^{m-1} (W^{(n)}(t_{i+1}) - W^{(n)}(t_i))^2 = T \quad \text{almost surely}$$

(not merely in expectation). *Hint:* Each squared increment equals $1/n$ deterministically.

**(c)** For a differentiable function $f: [0,T] \to \mathbb{R}$ with bounded derivative, show that

$$\sum_{i=0}^{m-1} (f(t_{i+1}) - f(t_i))^2 \to 0 \quad \text{as } |\Pi| \to 0$$

Explain why this distinguishes random walk paths from smooth paths.

---

## Exercise 2 — Higher Moments

Let $S_n = \sum_{i=1}^n \xi_i$ be the symmetric random walk.

**(a)** Verify $\mathbb{E}[S_n^2] = n$ by direct expansion, without using the variance formula.

**(b)** Using the pairing argument from [Moments](moments_of_random_walk.md) (Proposition 1.1.1), compute $\mathbb{E}[S_n^6]$.

*Hint:* Count the number of ways to partition six indices $\{i_1,\ldots,i_6\}$ into groups where each distinct index appears an even number of times. The cases are: one group of 6 all equal; three pairs; one group of 4 and one pair.

**(c)** Show that as $n \to \infty$:

$$\mathbb{E}[S_n^{2k}] = (2k-1)!!\, n^k + O(n^{k-1})$$

where $(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1)$. Compare with the Brownian motion moments $\mathbb{E}[W_1^{2k}] = (2k-1)!!$ and explain the connection.

---

## Exercise 3 — Gambler's Ruin

A gambler starts with $\$a$ and bets $\$1$ per round on a fair coin flip. Let

$$\tau_0 = \inf\{n : S_n = 0\}, \qquad \tau_b = \inf\{n : S_n = b\}, \qquad b > a$$

**(a)** Using the martingale $\{S_n\}$ (Proposition 1.1.3) and the Optional Stopping Theorem applied to the bounded stopping time $\tau = \tau_0 \wedge \tau_b$, show that

$$\mathbb{P}(\tau_b < \tau_0) = \frac{a}{b}$$

**(b)** Let $b \to \infty$. Show that $\mathbb{P}(\tau_0 < \infty) = 1$: the gambler is ruined with probability 1 in an unbounded game.

Reconcile this with Theorem 1.1.6 (recurrence): how can the walk be recurrent — visiting every integer infinitely often — yet the gambler always go broke?

**(c)** Using the martingale $\{S_n^2 - n\}$ (Proposition 1.1.4) and the Optional Stopping Theorem, show that

$$\mathbb{E}[\tau_0 \wedge \tau_b] = a(b - a)$$

What does this give for $\mathbb{E}[\tau_0]$ as $b \to \infty$? Interpret the result.

---

## Exercise 4 — Reflection Principle (Preview)

Let $M_n = \max_{0 \leq k \leq n} S_k$ be the running maximum of the symmetric random walk.

**(a)** By a symmetry argument, show that for $m > 0$:

$$\mathbb{P}(M_n \geq m) = 2\,\mathbb{P}(S_n \geq m) - \mathbb{P}(S_n = m)$$

*Hint:* Consider the "reflected" path obtained by flipping all steps after the first time the walk hits $m$.

**(b)** Use part (a) and the normal approximation to show that for large $n$:

$$\mathbb{P}\!\left(\frac{M_n}{\sqrt{n}} \geq x\right) \approx 2\,\mathbb{P}\!\left(\mathcal{N}(0,1) \geq x\right) = 2\bigl(1-\Phi(x)\bigr), \qquad x > 0$$

where $\Phi$ is the standard normal CDF. This is the distribution of $\max_{0 \leq t \leq 1} W_t$ for Brownian motion.

---

## References

- Williams, D. (1991). *Probability with Martingales*. Cambridge University Press.
- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley.
