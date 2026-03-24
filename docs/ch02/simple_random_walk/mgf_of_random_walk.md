# Moment Generating Function

The moment generating function (MGF) of $S_n$ encodes all moments in a single formula and provides the most elegant route to the Central Limit Theorem for the random walk.

---

## Definition

For $\lambda \in \mathbb{R}$, the MGF of the symmetric random walk $S_n = \sum_{i=1}^n \xi_i$ is

$$M_{S_n}(\lambda) := \mathbb{E}[e^{\lambda S_n}]$$

**Proposition 1.1.2** (Moment Generating Function)

$$\mathbb{E}[e^{\lambda S_n}] = (\cosh \lambda)^n$$

**Proof.** Since $\xi_1, \ldots, \xi_n$ are independent, the MGF of their sum factors:

$$\mathbb{E}[e^{\lambda S_n}] = \prod_{i=1}^n \mathbb{E}[e^{\lambda \xi_i}]$$

For a single step:

$$\mathbb{E}[e^{\lambda \xi_i}] = e^{+\lambda} \cdot \tfrac{1}{2} + e^{-\lambda} \cdot \tfrac{1}{2} = \frac{e^\lambda + e^{-\lambda}}{2} = \cosh\lambda$$

Therefore $\mathbb{E}[e^{\lambda S_n}] = (\cosh\lambda)^n$. $\square$

---

## Recovering Moments

The $k$-th moment of $S_n$ can be read off by differentiating the MGF $k$ times at $\lambda = 0$:

$$\mathbb{E}[S_n^k] = \left.\frac{d^k}{d\lambda^k} (\cosh\lambda)^n \right|_{\lambda=0}$$

Using the Taylor expansion $\cosh\lambda = 1 + \frac{\lambda^2}{2} + \frac{\lambda^4}{24} + \cdots$ and thus

$$\log\cosh\lambda = \frac{\lambda^2}{2} - \frac{\lambda^4}{12} + \frac{\lambda^6}{45} - \cdots$$

we obtain:

$$\mathbb{E}[e^{\lambda S_n}] = \exp\!\left(n \log\cosh\lambda\right) = \exp\!\left(\frac{n\lambda^2}{2} - \frac{n\lambda^4}{12} + \cdots\right)$$

Reading off coefficients:

- $\mathbb{E}[S_n^2] = n$ (coefficient of $\lambda^2/2!$).
- $\mathbb{E}[S_n^4] = 3n^2 - 2n$ (coefficient of $\lambda^4/4!$, accounting for the cross term from $\bigl(\frac{n\lambda^2}{2}\bigr)^2$).

Both agree with the direct calculations in [Moments of Random Walk](moments_of_random_walk.md).

---

## Proof of the CLT via MGF Convergence

**Theorem 1.1.10** (Central Limit Theorem for the Random Walk)

$$\frac{S_n}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1) \quad \text{as } n \to \infty$$

**Proof.** Substitute $\lambda = \theta / \sqrt{n}$ for fixed $\theta \in \mathbb{R}$:

$$\mathbb{E}\!\left[e^{\theta S_n / \sqrt{n}}\right] = \left(\cosh\frac{\theta}{\sqrt{n}}\right)^n$$

Using $\cosh x = 1 + \frac{x^2}{2} + O(x^4)$ as $x \to 0$:

$$\left(\cosh\frac{\theta}{\sqrt{n}}\right)^n = \left(1 + \frac{\theta^2}{2n} + O(n^{-2})\right)^n \xrightarrow{n\to\infty} e^{\theta^2/2}$$

The function $e^{\theta^2/2}$ is the MGF of $\mathcal{N}(0,1)$, and it is finite for all $\theta \in \mathbb{R}$. Since the MGFs of $S_n/\sqrt{n}$ converge pointwise to a function that is finite on all of $\mathbb{R}$, the MGF convergence theorem (see, e.g., Durrett (2019), Theorem 3.3.6) gives convergence in distribution:

$$\frac{S_n}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1). \quad\square$$

!!! note "MGF convergence theorem"
    The MGF convergence theorem states: if $M_{X_n}(\theta) \to M_X(\theta)$ for all $\theta$ in a neighbourhood of 0, and $M_X(\theta)$ is finite in that neighbourhood, then $X_n \xrightarrow{d} X$. Convergence on a neighbourhood of 0 is all the theorem requires; here we have the stronger statement that convergence holds on all of $\mathbb{R}$.

---

## Cumulants

The **cumulant generating function** is

$$\Lambda(\lambda) := \log \mathbb{E}[e^{\lambda S_n}] = n \log\cosh\lambda$$

The **cumulants** $\kappa_k$ of $S_n$ are defined by $\Lambda(\lambda) = \sum_{k=1}^\infty \kappa_k \frac{\lambda^k}{k!}$. Since $\cosh\lambda$ is an even function, $\log\cosh\lambda$ has only even-degree terms, so all odd cumulants vanish. This reflects the distributional symmetry $S_n \overset{d}{=} -S_n$: a symmetric distribution has all odd cumulants equal to zero.

---

## Large Deviations

For **large deviations**, the rate function governing probabilities of the form $\mathbb{P}(S_n/n \geq x)$ is the Legendre–Fenchel transform of $\log\cosh$:

$$I(x) = \sup_{\lambda \in \mathbb{R}} \bigl(\lambda x - \log\cosh\lambda\bigr)$$

Setting the derivative to zero gives $x = \tanh\lambda$, so $\lambda^* = \tanh^{-1}(x)$. To simplify, use $\tanh^{-1}(x) = \frac{1}{2}\log\frac{1+x}{1-x}$ and $\cosh(\tanh^{-1}(x)) = \frac{1}{\sqrt{1-x^2}}$. Substituting:

$$I(x) = x \cdot \frac{1}{2}\log\frac{1+x}{1-x} - \log\frac{1}{\sqrt{1-x^2}}
= \frac{x}{2}\log\frac{1+x}{1-x} + \frac{1}{2}\log(1-x^2)$$

Writing $\log(1-x^2) = \log(1+x)+\log(1-x)$ and collecting terms yields:

$$I(x) = \frac{1+x}{2}\log(1+x) + \frac{1-x}{2}\log(1-x), \quad |x| \leq 1$$

This gives the large deviation principle $\mathbb{P}(S_n/n \approx x) \approx e^{-nI(x)}$ for $|x| \leq 1$. The constraint $|x| \leq 1$ is natural: since each $\xi_i \in \{-1,+1\}$, the average $S_n/n$ is always confined to $[-1,1]$, and the supremum in the Legendre transform is $+\infty$ for $|x|>1$ by convention.

---

## References

- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 2, 3rd ed. Wiley.
- Dembo, A., & Zeitouni, O. (2010). *Large Deviations Techniques and Applications*, 2nd ed. Springer.

---

## Exercises

**Exercise 1.** For the asymmetric random walk with $\mathbb{P}(\xi_i = +1) = p$ and $\mathbb{P}(\xi_i = -1) = 1-p$, show that the MGF is $\mathbb{E}[e^{\lambda S_n}] = (pe^\lambda + (1-p)e^{-\lambda})^n$. Verify that this reduces to $(\cosh \lambda)^n$ when $p = 1/2$.

---

**Exercise 2.** Using the MGF $M_{S_n}(\lambda) = (\cosh \lambda)^n$ and the formula $\mathbb{E}[S_n^k] = M_{S_n}^{(k)}(0)$, compute $\mathbb{E}[S_n^6]$ for the symmetric random walk. Express your answer as a polynomial in $n$.

---

**Exercise 3.** In the CLT proof, we used the approximation $\left(1 + \frac{\theta^2}{2n} + O(n^{-2})\right)^n \to e^{\theta^2/2}$. Prove this limit rigorously by taking logarithms and using $\log(1+x) = x - x^2/2 + O(x^3)$ for small $x$.

---

**Exercise 4.** The large deviation rate function for the symmetric random walk is $I(x) = \frac{1+x}{2}\log(1+x) + \frac{1-x}{2}\log(1-x)$ for $|x| \leq 1$. Show that $I(x) \geq 0$ with equality only at $x = 0$. Then verify that $I''(0) = 1$, so that near $x = 0$ the rate function is approximately $I(x) \approx x^2/2$, which is consistent with the CLT (Gaussian tail with variance $1/n$).

---

**Exercise 5.** Use Markov's inequality with the MGF to derive a Chernoff bound for the symmetric random walk: show that for $a > 0$,

$$
\mathbb{P}(S_n \geq an) \leq \inf_{\lambda > 0} e^{-\lambda an} (\cosh \lambda)^n = e^{-nI(a)}
$$

Compute this bound numerically for $n = 100$ and $a = 0.3$. Compare with the normal approximation $\mathbb{P}(S_{100} \geq 30)$.

---

**Exercise 6.** The cumulant generating function is $\Lambda(\lambda) = n\log\cosh\lambda$. Show that all odd cumulants of $S_n$ are zero. Compute the first three nonzero cumulants ($\kappa_2$, $\kappa_4$, $\kappa_6$) and verify that the **excess kurtosis** $\kappa_4 / \kappa_2^2 = -2/n$ vanishes as $n \to \infty$, consistent with the CLT (the Gaussian has zero excess kurtosis).
