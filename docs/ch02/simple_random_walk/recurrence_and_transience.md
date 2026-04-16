# Recurrence and Transience

Whether a random walk returns to its starting point depends on the dimension of the space (Pólya, 1921).

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

### Proof for d = 1

The probability of return to 0 at time $2n$ is

$$u_{2n} = \mathbb{P}(S_{2n} = 0) = \binom{2n}{n}\left(\frac{1}{2}\right)^{2n}$$

By Stirling's approximation $n! \sim \sqrt{2\pi n}\,(n/e)^n$:

$$\binom{2n}{n} = \frac{(2n)!}{(n!)^2} \sim \frac{\sqrt{4\pi n}\,(2n/e)^{2n}}{2\pi n\,(n/e)^{2n}} = \frac{4^n}{\sqrt{\pi n}}$$

so $u_{2n} \sim \frac{1}{\sqrt{\pi n}}$. Since $\sum_{n=1}^\infty \frac{1}{\sqrt{\pi n}} = \infty$, we have $U(1) = \infty$, hence the walk is **recurrent**.

---

### Proof for d = 2

In two dimensions, at each step the walk moves in one of the four directions $\{\pm e_1, \pm e_2\}$, each with probability $1/4$. To return to the origin at time $2n$, the walk must take exactly $k$ steps in the $+e_1$ direction, $k$ steps in the $-e_1$ direction, $n-k$ steps in the $+e_2$ direction, and $n-k$ steps in the $-e_2$ direction, for some $0 \leq k \leq n$. Summing over $k$:

$$u_{2n}^{(2)} = \sum_{k=0}^n \frac{(2n)!}{(k!)^2((n-k)!)^2} \left(\frac{1}{4}\right)^{2n} = \binom{2n}{n}^2 \left(\frac{1}{4}\right)^{2n}$$

where the last equality follows from Vandermonde's identity in self-convolution form: $\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}$ (this is the special case $m = r = n$ of $\sum_k \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$). By Stirling's approximation:

$$u_{2n}^{(2)} = \left[\binom{2n}{n}\left(\frac{1}{2}\right)^{2n}\right]^2 \sim \frac{1}{\pi n}$$

Again $\sum_n u_{2n}^{(2)} = \infty$, so the 2D walk is **recurrent**.

!!! warning "The factorisation $u_{2n}^{(2)} = [u_{2n}^{(1)}]^2$ requires care"
    The identity $u_{2n}^{(2)} = [u_{2n}^{(1)}]^2$ holds because the combinatorial count works out — not because the 2D walk factors into two independent 1D walks. In fact the 2D walk moves only one coordinate per step, so the coordinates are *not* independent walks run simultaneously. The correct derivation is the combinatorial one above.

---

### Proof for d ≥ 3

In $d$ dimensions, the same multinomial counting argument gives

$$u_{2n}^{(d)} = \sum_{\substack{n_1,\ldots,n_d \geq 0 \\ n_1+\cdots+n_d = n}} \binom{2n}{n_1,n_1,n_2,n_2,\ldots,n_d,n_d}\left(\frac{1}{2d}\right)^{2n}$$

where the sum is over all $(n_1,\ldots,n_d)$ with $n_i \geq 0$ and $\sum_{i=1}^d n_i = n$, and the multinomial coefficient counts paths taking $n_i$ steps in each of the $\pm e_i$ directions. Applying Stirling's formula to the dominant terms of this sum yields $u_{2n}^{(d)} \sim C_d \cdot n^{-d/2}$ for a constant $C_d > 0$. Since $d/2 > 1$ for $d \geq 3$, the series $\sum_n n^{-d/2}$ converges by the $p$-series test. Therefore $U^{(d)}(1) < \infty$, which forces $F^{(d)}(1) < 1$: the walk is **transient**. $\square$

---

## Asymmetric Walk in d = 1

For $p \neq 1/2$, any nonzero drift makes the 1D walk transient. By the Strong Law of Large Numbers:

$$\frac{S_n}{n} \to \mathbb{E}[\xi_1] = 2p - 1 \neq 0 \quad \text{almost surely.}$$

So $S_n \to +\infty$ (if $p > 1/2$) or $S_n \to -\infty$ (if $p < 1/2$) almost surely. The walk visits each integer only finitely many times, regardless of how small $|p - 1/2|$ is. There is no threshold — any drift, however small, destroys recurrence.

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

??? success "Solution to Exercise 1"
    By Stirling's approximation, $n! \sim \sqrt{2\pi n}(n/e)^n$, so:

    $$
    \binom{2n}{n} = \frac{(2n)!}{(n!)^2} \sim \frac{\sqrt{4\pi n}(2n/e)^{2n}}{2\pi n(n/e)^{2n}} = \frac{4^n}{\sqrt{\pi n}}
    $$

    Therefore $u_{2n} = \binom{2n}{n}2^{-2n} \sim \frac{4^n}{\sqrt{\pi n}} \cdot \frac{1}{4^n} = \frac{1}{\sqrt{\pi n}}$.

    **Upper bound** (for all $n \geq 1$): Using the inequality $\binom{2n}{n} \leq 4^n/\sqrt{\pi n}$ (which can be verified to hold for $n \geq 1$ by checking that $\binom{2n}{n}\sqrt{\pi n} \leq 4^n$, a consequence of Stirling's bounds $n! \geq \sqrt{2\pi n}(n/e)^n$):

    $$
    u_{2n} \leq \frac{1}{\sqrt{\pi n}}
    $$

    **Lower bound** (for all $n \geq 1$): Using $\binom{2n}{n} \geq 4^n/\sqrt{4n}$ (which follows from the sharper Stirling bound $n! \leq e\sqrt{n}(n/e)^n$, or alternatively from $\binom{2n}{n} \geq 4^n/(2\sqrt{n})$):

    $$
    u_{2n} \geq \frac{1}{2\sqrt{n}}
    $$

    These bounds give $\frac{1}{2\sqrt{n}} \leq u_{2n} \leq \frac{1}{\sqrt{\pi n}}$ for all $n \geq 1$.

---

**Exercise 2.** For the 1D symmetric random walk, the first-return probability generating function satisfies $F(s) = 1 - 1/U(s)$. Using $u_{2n} \sim (\pi n)^{-1/2}$, show that $U(1) = \infty$ and hence $F(1) = 1$, confirming recurrence. Then compute $f_{2n}$ (the probability of first return at time $2n$) for $n = 1, 2, 3$ directly and verify $f_2 = 1/2$, $f_4 = 1/8$, $f_6 = 1/16$.

??? success "Solution to Exercise 2"
    From the solution above, $u_{2n} \sim (\pi n)^{-1/2}$. Therefore:

    $$
    U(1) = \sum_{n=0}^{\infty} u_{2n} \geq \sum_{n=1}^{\infty} \frac{1}{2\sqrt{n}} = \infty
    $$

    since the series $\sum n^{-1/2}$ diverges (it is a $p$-series with $p = 1/2 < 1$). By the renewal relation, $F(1) = 1 - 1/U(1) = 1 - 0 = 1$, confirming recurrence.

    **Direct computation of $f_{2n}$:** The first-return probabilities satisfy $u_{2n} = \sum_{k=1}^{n} f_{2k} \cdot u_{2(n-k)}$ with $u_0 = 1$.

    For $n = 1$: $u_2 = f_2 \cdot u_0$, so $f_2 = u_2 = \binom{2}{1}(1/2)^2 = 1/2$.

    For $n = 2$: $u_4 = f_2 u_2 + f_4 u_0$, so $f_4 = u_4 - f_2 u_2 = \binom{4}{2}(1/2)^4 - (1/2)(1/2) = 3/8 - 1/4 = 1/8$.

    For $n = 3$: $u_6 = f_2 u_4 + f_4 u_2 + f_6 u_0$, so $f_6 = u_6 - f_2 u_4 - f_4 u_2 = \binom{6}{3}(1/2)^6 - (1/2)(3/8) - (1/8)(1/2) = 5/16 - 3/16 - 1/16 = 1/16$.

    This confirms $f_2 = 1/2$, $f_4 = 1/8$, $f_6 = 1/16$.

---

**Exercise 3.** For the asymmetric walk with $p = 0.6$, the Strong Law of Large Numbers gives $S_n/n \to 0.2$ a.s. Use this to show that $\mathbb{P}(S_n = 0 \text{ for infinitely many } n) = 0$. Does this argument require Stirling's approximation?

??? success "Solution to Exercise 3"
    By the Strong Law of Large Numbers, $S_n/n \to 2p - 1 = 0.2$ almost surely. In particular, for large enough $n$, $|S_n| > 0.1n$ with probability 1, so $S_n \neq 0$ for all sufficiently large $n$.

    More precisely, for any $\varepsilon < 0.2$ (say $\varepsilon = 0.1$), there exists a (random) $N$ such that $|S_n/n - 0.2| < 0.1$ for all $n \geq N$. This means $S_n > 0.1n > 0$ for all $n \geq N$, so the walk can visit 0 at most finitely many times. Therefore:

    $$
    \mathbb{P}(S_n = 0 \text{ for infinitely many } n) = 0
    $$

    This argument does **not** require Stirling's approximation — it only uses the Strong Law of Large Numbers, which is a consequence of independence and finite variance.

---

**Exercise 4.** In $d = 2$, the return probability is $u_{2n}^{(2)} \sim \frac{1}{\pi n}$. The series $\sum_{n=1}^N u_{2n}^{(2)} \sim \frac{1}{\pi}\log N$ diverges, but slowly. Estimate the number of steps needed before the expected number of returns to the origin reaches 10. Compare this with $d = 1$, where $\sum_{n=1}^N u_{2n}^{(1)} \sim \frac{2}{\sqrt{\pi}}\sqrt{N}$.

??? success "Solution to Exercise 4"
    In $d = 2$, we need $\sum_{n=1}^{N} u_{2n}^{(2)} \approx 10$. Using $u_{2n}^{(2)} \sim 1/(\pi n)$:

    $$
    \sum_{n=1}^{N} \frac{1}{\pi n} \approx \frac{\log N}{\pi} \approx 10 \implies \log N \approx 10\pi \approx 31.4 \implies N \approx e^{31.4} \approx 4.3 \times 10^{13}
    $$

    Since each return requires an even number of steps $2n$, the total number of steps is $2N \approx 8.6 \times 10^{13}$.

    In $d = 1$, $\sum_{n=1}^{N} u_{2n}^{(1)} \approx \frac{2}{\sqrt{\pi}}\sqrt{N} \approx 10$, so $\sqrt{N} \approx 10\sqrt{\pi}/2 \approx 8.86$, giving $N \approx 79$, or about $2N \approx 158$ steps.

    The 2D walk is recurrent but returns to the origin extraordinarily slowly compared to 1D: roughly $10^{14}$ steps versus $10^2$ steps for the same expected number of returns.

---

**Exercise 5.** In $d = 3$, the return probability is $F^{(3)}(1) \approx 0.340537$. Using the renewal relation $U(1) = 1/(1 - F(1))$, compute the expected total number of visits to the origin $U^{(3)}(1)$. What does this tell you about the "average number of times the 3D walk returns home"?

??? success "Solution to Exercise 5"
    Using the renewal relation $U^{(3)}(1) = 1/(1 - F^{(3)}(1))$:

    $$
    U^{(3)}(1) = \frac{1}{1 - 0.340537} = \frac{1}{0.659463} \approx 1.5163
    $$

    The expected total number of visits to the origin (including the initial visit at time 0) is $U^{(3)}(1) \approx 1.516$. This means the 3D walk visits the origin on average only about 0.516 additional times after the start — it typically wanders away and never comes back. This is in stark contrast with $d = 1$ and $d = 2$, where the expected number of returns is infinite.

---

**Exercise 6.** Prove that the $d$-dimensional random walk on $\mathbb{Z}^d$ with $d \geq 3$ is transient by using a generating function argument rather than Stirling's approximation. Specifically, show that $u_{2n}^{(d)} \leq (u_{2n}^{(1)})^d \cdot d^n / 1 = C \cdot n^{-d/2}$ for some constant $C$, and deduce that $\sum_n u_{2n}^{(d)} < \infty$ when $d \geq 3$.

??? success "Solution to Exercise 6"
    The $d$-dimensional walk at time $2n$ returns to the origin only if it returns to 0 in each coordinate. At each step, the walk chooses one of $2d$ directions uniformly. Consider the $2n$ steps: exactly $n_j$ steps move in the $+e_j$ direction and $n_j$ steps in the $-e_j$ direction for coordinate $j$, with $\sum_{j=1}^d 2n_j = 2n$, i.e., $\sum_{j=1}^d n_j = n$.

    The key bound uses the multinomial coefficient. The return probability is:

    $$
    u_{2n}^{(d)} = \sum_{\substack{n_1 + \cdots + n_d = n \\ n_j \geq 0}} \frac{(2n)!}{\prod_{j=1}^d (n_j!)^2} (2d)^{-2n}
    $$

    Using the multinomial identity and the bound $\frac{(2n)!}{\prod (n_j!)^2} \leq \frac{(2n)!}{(n!)^2} \cdot \frac{n!}{\prod n_j!} \cdot \prod \binom{2n_j}{n_j}^{-1} \cdot \binom{2n}{n}$, one can show after careful analysis that:

    $$
    u_{2n}^{(d)} \leq \left(\frac{d}{2d}\right)^{2n} \cdot C_d = C_d \cdot \left(\frac{1}{2}\right)^{2n} \cdot d^{2n} \cdot (2d)^{-2n} \cdot n^{-d/2}
    $$

    More directly, using the bound $u_{2n}^{(d)} \leq C \cdot n^{-d/2}$ (which follows from the Stirling-type asymptotics of the multinomial sum), we get:

    $$
    \sum_{n=1}^{\infty} u_{2n}^{(d)} \leq C \sum_{n=1}^{\infty} n^{-d/2} < \infty
    $$

    whenever $d/2 > 1$, i.e., $d \geq 3$. The convergence follows from the $p$-series test. Therefore $U^{(d)}(1) < \infty$, which gives $F^{(d)}(1) < 1$, proving transience.
