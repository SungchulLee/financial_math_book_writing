# Recurrence and Transience

> "A drunken man will find his way home, but a drunken bird may get lost forever."
>
> — Shizuo Kakutani (as quoted in Durrett, *Probability: Theory and Examples*, 4th ed., p. 162)

Whether a random walk returns to its starting point depends critically on the dimension of the space it lives in. This dichotomy, first established by Pólya (1921), is one of the most striking results in probability theory.

---

## Setup

A random walk on $\mathbb{Z}^d$ is called:

- **Recurrent** if it returns to the origin with probability 1.
- **Transient** if it returns to the origin with probability strictly less than 1, i.e., it eventually escapes to infinity.

Define the **return probability** and **first-return probability** generating functions:

$$U(s) = \sum_{n=0}^{\infty} u_{2n}\, s^{2n}, \qquad F(s) = \sum_{n=1}^{\infty} f_{2n}\, s^{2n}, \qquad s \in [0,1]$$

where

- $u_{2n} := \mathbb{P}(S_{2n} = 0)$ is the probability of being at the origin at time $2n$,
- $f_{2n} := \mathbb{P}(\text{first return to origin at time } 2n)$.

**Renewal relation.** These generating functions satisfy $U(s) = 1/(1 - F(s))$. To see why: condition on the time of the first return. Any visit to 0 at time $2n$ can be decomposed uniquely as a first return at some time $2k \leq 2n$ followed by an independent visit at time $2(n-k)$. In generating-function language this convolution structure gives $U(s) = 1 + F(s)U(s)$, hence $U(s) = 1/(1-F(s))$.

The walk is recurrent if and only if $F(1) = 1$ (return is certain), which by the renewal relation holds if and only if $U(1) = \sum_{n=0}^\infty u_{2n} = \infty$.

---

## Pólya's Recurrence Theorem

![Polya recurrence — sample paths in $d=1,2,3$ illustrating that low-dimensional walks return to 0 while the 3D walk drifts away.](figures/polya_recurrence.png)

**Theorem 1.1.7** (Pólya's Recurrence Theorem)

For the symmetric random walk on $\mathbb{Z}^d$:

- **$d = 1$:** recurrent — returns to origin with probability 1.
- **$d = 2$:** recurrent — returns to origin with probability 1.
- **$d \geq 3$:** transient — positive probability of never returning.

We prove all three cases via the criterion $U(1) = \infty \Leftrightarrow$ recurrent.

---

### Proof for $d = 1$

The probability of return to 0 at time $2n$ is

$$u_{2n} = \mathbb{P}(S_{2n} = 0) = \binom{2n}{n}\left(\frac{1}{2}\right)^{2n}$$

By Stirling's approximation $n! \sim \sqrt{2\pi n}\,(n/e)^n$:

$$\binom{2n}{n} = \frac{(2n)!}{(n!)^2} \sim \frac{\sqrt{4\pi n}\,(2n/e)^{2n}}{2\pi n\,(n/e)^{2n}} = \frac{4^n}{\sqrt{\pi n}}$$

so $u_{2n} \sim \frac{1}{\sqrt{\pi n}}$. Since $\sum_{n=1}^\infty \frac{1}{\sqrt{\pi n}} = \infty$, we have $U(1) = \infty$, hence the walk is **recurrent**.

---

### Proof for $d = 2$

In two dimensions, at each step the walk moves in one of the four directions $\{\pm e_1, \pm e_2\}$, each with probability $1/4$. To return to the origin at time $2n$, the walk must take exactly $k$ steps in the $+e_1$ direction, $k$ steps in the $-e_1$ direction, $n-k$ steps in the $+e_2$ direction, and $n-k$ steps in the $-e_2$ direction, for some $0 \leq k \leq n$. Summing over $k$:

$$u_{2n}^{(2)} = \sum_{k=0}^n \frac{(2n)!}{(k!)^2((n-k)!)^2} \left(\frac{1}{4}\right)^{2n} = \binom{2n}{n}^2 \left(\frac{1}{4}\right)^{2n}$$

where the last equality follows from Vandermonde's identity in self-convolution form: $\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}$ (this is the special case $m = r = n$ of $\sum_k \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$). By Stirling's approximation:

$$u_{2n}^{(2)} = \left[\binom{2n}{n}\left(\frac{1}{2}\right)^{2n}\right]^2 \sim \frac{1}{\pi n}$$

Again $\sum_n u_{2n}^{(2)} = \infty$, so the 2D walk is **recurrent**.

!!! warning "The factorisation $u_{2n}^{(2)} = [u_{2n}^{(1)}]^2$ requires care"
    The identity $u_{2n}^{(2)} = [u_{2n}^{(1)}]^2$ holds because the combinatorial count works out — not because the 2D walk factors into two independent 1D walks. In fact the 2D walk moves only one coordinate per step, so the coordinates are *not* independent walks run simultaneously. The correct derivation is the combinatorial one above.

---

### Proof for $d \geq 3$

In $d$ dimensions, the same multinomial counting argument gives

$$u_{2n}^{(d)} = \sum_{\substack{n_1,\ldots,n_d \geq 0 \\ n_1+\cdots+n_d = n}} \binom{2n}{n_1,n_1,n_2,n_2,\ldots,n_d,n_d}\left(\frac{1}{2d}\right)^{2n}$$

where the sum is over all $(n_1,\ldots,n_d)$ with $n_i \geq 0$ and $\sum_{i=1}^d n_i = n$, and the multinomial coefficient counts paths taking $n_i$ steps in each of the $\pm e_i$ directions. Applying Stirling's formula to the dominant terms of this sum yields $u_{2n}^{(d)} \sim C_d \cdot n^{-d/2}$ for a constant $C_d > 0$. Since $d/2 > 1$ for $d \geq 3$, the series $\sum_n n^{-d/2}$ converges by the $p$-series test. Therefore $U^{(d)}(1) < \infty$, which forces $F^{(d)}(1) < 1$: the walk is **transient**. $\square$

---

## Asymmetric Walk in $d = 1$

For $p \neq 1/2$, any nonzero drift makes the 1D walk transient. By the Strong Law of Large Numbers:

$$\frac{S_n}{n} \to \mathbb{E}[\xi_1] = 2p - 1 \neq 0 \quad \text{almost surely.}$$

So $S_n \to +\infty$ (if $p > 1/2$) or $S_n \to -\infty$ (if $p < 1/2$) almost surely. The walk visits each integer only finitely many times, regardless of how small $|p - 1/2|$ is. There is no threshold — any drift, however small, destroys recurrence.

---

## Implications

The recurrence/transience dichotomy has consequences far beyond the random walk:

- **Statistical mechanics:** recurrence in $d \leq 2$ is related to the absence of a phase transition in the Ising model below dimension 2 (Peierls argument).
- **Polymer physics:** transience in $d \geq 3$ models the fact that a long polymer in 3D has positive probability of having no self-intersections.
- **Population genetics:** in the Wright–Fisher model, the allele frequency process is a martingale whose absorbing boundaries are inevitably hit — in analogy with, but not directly caused by, the recurrence of the 1D walk (see [Applications](applications_random_walk.md) for a precise statement).
- **Potential theory:** the connection $U(1) < \infty \Leftrightarrow$ transient is the probabilistic version of the Green's function being finite.

---

## References

- Pólya, G. (1921). Über eine Aufgabe der Wahrscheinlichkeitsrechnung betreffend die Irrfahrt im Straßennetz. *Mathematische Annalen*, 84(1–2), 149–160.
- Durrett, R. (2010). *Probability: Theory and Examples*, 4th ed. Cambridge University Press.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley.
- Lawler, G. F., & Limic, V. (2010). *Random Walk: A Modern Introduction*. Cambridge University Press.
- Spitzer, F. (1964). *Principles of Random Walk*. Springer.

---

## Exercises

**Exercise 1.** Using Stirling's approximation, show that $u_{2n} = \binom{2n}{n} 2^{-2n} \sim \frac{1}{\sqrt{\pi n}}$ for large $n$. Give explicit upper and lower bounds on $u_{2n}$ that hold for all $n \geq 1$.

---

**Exercise 2.** For the 1D symmetric random walk, the first-return probability generating function satisfies $F(s) = 1 - 1/U(s)$. Using $u_{2n} \sim (\pi n)^{-1/2}$, show that $U(1) = \infty$ and hence $F(1) = 1$, confirming recurrence. Then compute $f_{2n}$ (the probability of first return at time $2n$) for $n = 1, 2, 3$ directly and verify $f_2 = 1/2$, $f_4 = 1/8$, $f_6 = 1/16$.

---

**Exercise 3.** For the asymmetric walk with $p = 0.6$, the Strong Law of Large Numbers gives $S_n/n \to 0.2$ a.s. Use this to show that $\mathbb{P}(S_n = 0 \text{ for infinitely many } n) = 0$. Does this argument require Stirling's approximation?

---

**Exercise 4.** In $d = 2$, the return probability is $u_{2n}^{(2)} \sim \frac{1}{\pi n}$. The series $\sum_{n=1}^N u_{2n}^{(2)} \sim \frac{1}{\pi}\log N$ diverges, but slowly. Estimate the number of steps needed before the expected number of returns to the origin reaches 10. Compare this with $d = 1$, where $\sum_{n=1}^N u_{2n}^{(1)} \sim \frac{2}{\sqrt{\pi}}\sqrt{N}$.

---

**Exercise 5.** In $d = 3$, the return probability is $F^{(3)}(1) \approx 0.340537$. Using the renewal relation $U(1) = 1/(1 - F(1))$, compute the expected total number of visits to the origin $U^{(3)}(1)$. What does this tell you about the "average number of times the 3D walk returns home"?

---

**Exercise 6.** Prove that the $d$-dimensional random walk on $\mathbb{Z}^d$ with $d \geq 3$ is transient by using a generating function argument rather than Stirling's approximation. Specifically, show that $u_{2n}^{(d)} \leq (u_{2n}^{(1)})^d \cdot d^n / 1 = C \cdot n^{-d/2}$ for some constant $C$, and deduce that $\sum_n u_{2n}^{(d)} < \infty$ when $d \geq 3$.
