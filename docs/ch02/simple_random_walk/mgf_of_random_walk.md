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

## References

- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 2, 3rd ed. Wiley.

---

## Exercises

**Exercise 1.** For the asymmetric random walk with $\mathbb{P}(\xi_i = +1) = p$ and $\mathbb{P}(\xi_i = -1) = 1-p$, show that the MGF is $\mathbb{E}[e^{\lambda S_n}] = (pe^\lambda + (1-p)e^{-\lambda})^n$. Verify that this reduces to $(\cosh \lambda)^n$ when $p = 1/2$.

??? success "Solution to Exercise 1"
    For the asymmetric walk, the MGF of a single step is:

    $$
    \mathbb{E}[e^{\lambda \xi_i}] = p e^{\lambda} + (1-p) e^{-\lambda}
    $$

    By independence, the MGF of $S_n = \sum_{i=1}^n \xi_i$ factors:

    $$
    \mathbb{E}[e^{\lambda S_n}] = \prod_{i=1}^n \mathbb{E}[e^{\lambda \xi_i}] = (pe^{\lambda} + (1-p)e^{-\lambda})^n
    $$

    When $p = 1/2$:

    $$
    \frac{1}{2}e^{\lambda} + \frac{1}{2}e^{-\lambda} = \frac{e^{\lambda} + e^{-\lambda}}{2} = \cosh\lambda
    $$

    so the formula reduces to $(\cosh\lambda)^n$ as required.

---

**Exercise 2.** Differentiate $M_{S_n}(\lambda) = (\cosh\lambda)^n$ twice and evaluate at $\lambda = 0$ to recover $\mathbb{E}[S_n^2] = n$. Verify against the direct calculation in [Moments of Random Walk](moments_of_random_walk.md).

??? success "Solution to Exercise 2"
    Let $M(\lambda) = (\cosh\lambda)^n$. First derivative: $M'(\lambda) = n(\cosh\lambda)^{n-1}\sinh\lambda$. At $\lambda = 0$: $M'(0) = n \cdot 1 \cdot 0 = 0 = \mathbb{E}[S_n]$.

    Second derivative: $M''(\lambda) = n(n-1)(\cosh\lambda)^{n-2}\sinh^2\lambda + n(\cosh\lambda)^{n-1}\cosh\lambda = n(n-1)(\cosh\lambda)^{n-2}\sinh^2\lambda + n(\cosh\lambda)^n$. At $\lambda = 0$: $M''(0) = 0 + n \cdot 1 = n = \mathbb{E}[S_n^2]$, agreeing with the direct calculation.

---

**Exercise 3.** In the CLT proof, we used the approximation $\left(1 + \frac{\theta^2}{2n} + O(n^{-2})\right)^n \to e^{\theta^2/2}$. Prove this limit rigorously by taking logarithms and using $\log(1+x) = x - x^2/2 + O(x^3)$ for small $x$.

??? success "Solution to Exercise 3"
    Let $a_n = 1 + \frac{\theta^2}{2n} + O(n^{-2})$. We need to show $a_n^n \to e^{\theta^2/2}$. Take logarithms:

    $$
    n\log a_n = n\log\!\left(1 + \frac{\theta^2}{2n} + O(n^{-2})\right)
    $$

    Using $\log(1+x) = x - x^2/2 + O(x^3)$ with $x = \frac{\theta^2}{2n} + O(n^{-2})$:

    $$
    \log a_n = \frac{\theta^2}{2n} + O(n^{-2}) - \frac{1}{2}\left(\frac{\theta^2}{2n}\right)^2 + O(n^{-3}) = \frac{\theta^2}{2n} + O(n^{-2})
    $$

    Therefore:

    $$
    n\log a_n = n \cdot \left(\frac{\theta^2}{2n} + O(n^{-2})\right) = \frac{\theta^2}{2} + O(n^{-1}) \xrightarrow{n\to\infty} \frac{\theta^2}{2}
    $$

    By continuity of the exponential, $a_n^n = e^{n\log a_n} \to e^{\theta^2/2}$.

---

