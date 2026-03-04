# Moment Generating Function

The moment generating function (MGF) of $S_n$ encodes all moments in a single formula and provides the most elegant route to the Central Limit Theorem for the random walk.

---

## Definition

For $\lambda \in \mathbb{R}$, the MGF of the symmetric random walk $S_n = \sum_{i=1}^n \xi_i$ is

$$M_{S_n}(\lambda) := \mathbb{E}[e^{\lambda S_n}].$$

**Proposition 1.1.2** (Moment Generating Function)

$$\mathbb{E}[e^{\lambda S_n}] = (\cosh \lambda)^n.$$

**Proof.** Since $\xi_1, \ldots, \xi_n$ are independent, the MGF of their sum factors:

$$\mathbb{E}[e^{\lambda S_n}] = \prod_{i=1}^n \mathbb{E}[e^{\lambda \xi_i}].$$

For a single step:

$$\mathbb{E}[e^{\lambda \xi_i}] = e^{+\lambda} \cdot \tfrac{1}{2} + e^{-\lambda} \cdot \tfrac{1}{2} = \frac{e^\lambda + e^{-\lambda}}{2} = \cosh\lambda.$$

Therefore $\mathbb{E}[e^{\lambda S_n}] = (\cosh\lambda)^n$. $\square$

---

## Recovering Moments

The $k$-th moment of $S_n$ can be read off by differentiating the MGF $k$ times at $\lambda = 0$:

$$\mathbb{E}[S_n^k] = \left.\frac{d^k}{d\lambda^k} (\cosh\lambda)^n \right|_{\lambda=0}.$$

Using the Taylor expansion $\cosh\lambda = 1 + \frac{\lambda^2}{2} + \frac{\lambda^4}{24} + \cdots$ and thus

$$\log\cosh\lambda = \frac{\lambda^2}{2} - \frac{\lambda^4}{12} + \frac{\lambda^6}{45} - \cdots$$

we obtain:

$$\mathbb{E}[e^{\lambda S_n}] = \exp\!\left(n \log\cosh\lambda\right) = \exp\!\left(\frac{n\lambda^2}{2} - \frac{n\lambda^4}{12} + \cdots\right).$$

Reading off coefficients:

- $\mathbb{E}[S_n^2] = n$ (coefficient of $\lambda^2/2!$).
- $\mathbb{E}[S_n^4] = 3n^2 - 2n$ (coefficient of $\lambda^4/4!$, after accounting for the cross term from $(\frac{n\lambda^2}{2})^2$).

Both agree with the direct calculations in [Moments of Random Walk](moments_of_random_walk.md).

---

## One-Line Proof of the CLT

Substitute $\lambda = \theta / \sqrt{n}$ for fixed $\theta \in \mathbb{R}$:

$$\mathbb{E}\!\left[e^{\theta S_n / \sqrt{n}}\right] = \left(\cosh\frac{\theta}{\sqrt{n}}\right)^n.$$

Using $\cosh x = 1 + \frac{x^2}{2} + O(x^4)$ as $x \to 0$:

$$\left(\cosh\frac{\theta}{\sqrt{n}}\right)^n = \left(1 + \frac{\theta^2}{2n} + O(n^{-2})\right)^n \xrightarrow{n\to\infty} e^{\theta^2/2}.$$

Since $e^{\theta^2/2}$ is the MGF of $\mathcal{N}(0,1)$, convergence of MGFs implies convergence in distribution:

$$\frac{S_n}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1).$$

This is the Central Limit Theorem for the symmetric random walk — proved in one computation. The full CLT and its role in Donsker's theorem are developed in [Scaling Limit](scaling_limit.md) and [Donsker's Theorem](donsker_theorem.md).

---

## Cumulants and Large Deviations

The **cumulant generating function** is

$$\Lambda(\lambda) := \log \mathbb{E}[e^{\lambda S_n}] = n \log\cosh\lambda.$$

The **cumulants** $\kappa_k$ of $S_n$ are the coefficients in $\Lambda(\lambda) = \sum_{k=1}^\infty \kappa_k \frac{\lambda^k}{k!}$. Since $\log\cosh\lambda$ has only even-degree terms, all odd cumulants vanish, consistent with the symmetric distribution.

For **large deviations**, the rate function governing probabilities of the form $\mathbb{P}(S_n/n \geq x)$ is the Legendre–Fenchel transform of $\log\cosh$:

$$I(x) = \sup_{\lambda \in \mathbb{R}} \bigl(\lambda x - \log\cosh\lambda\bigr).$$

This can be evaluated explicitly: $I(x) = \frac{1+x}{2}\log(1+x) + \frac{1-x}{2}\log(1-x)$ for $|x| \leq 1$, giving the large deviation principle $\mathbb{P}(S_n/n \approx x) \approx e^{-nI(x)}$.

---

## References

- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 2, 3rd ed. Wiley.
- Dembo, A., & Zeitouni, O. (2010). *Large Deviations Techniques and Applications*, 2nd ed. Springer.
