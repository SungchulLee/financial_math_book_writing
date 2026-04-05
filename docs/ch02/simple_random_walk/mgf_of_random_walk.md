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

**Exercise 2.** Using the MGF $M_{S_n}(\lambda) = (\cosh \lambda)^n$ and the formula $\mathbb{E}[S_n^k] = M_{S_n}^{(k)}(0)$, compute $\mathbb{E}[S_n^6]$ for the symmetric random walk. Express your answer as a polynomial in $n$.

??? success "Solution to Exercise 2"
    We need $\mathbb{E}[S_n^6] = M_{S_n}^{(6)}(0)$ where $M_{S_n}(\lambda) = (\cosh\lambda)^n$. Using the cumulant generating function $\Lambda(\lambda) = n\log\cosh\lambda$ and the Taylor expansion:

    $$
    \log\cosh\lambda = \frac{\lambda^2}{2} - \frac{\lambda^4}{12} + \frac{\lambda^6}{45} - \cdots
    $$

    So $\Lambda(\lambda) = \frac{n\lambda^2}{2} - \frac{n\lambda^4}{12} + \frac{n\lambda^6}{45} - \cdots$, giving cumulants $\kappa_2 = n$, $\kappa_4 = -2n$, $\kappa_6 = 16n$.

    The sixth moment is related to cumulants by:

    $$
    \mathbb{E}[S_n^6] = \kappa_6 + 15\kappa_4\kappa_2 + 15\kappa_2^3 + 10\kappa_3^2
    $$

    Since $\kappa_3 = 0$ (odd cumulant):

    $$
    \mathbb{E}[S_n^6] = 16n + 15(-2n)(n) + 15n^3 = 16n - 30n^2 + 15n^3
    $$

    Therefore $\mathbb{E}[S_n^6] = 15n^3 - 30n^2 + 16n$.

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

**Exercise 4.** The large deviation rate function for the symmetric random walk is $I(x) = \frac{1+x}{2}\log(1+x) + \frac{1-x}{2}\log(1-x)$ for $|x| \leq 1$. Show that $I(x) \geq 0$ with equality only at $x = 0$. Then verify that $I''(0) = 1$, so that near $x = 0$ the rate function is approximately $I(x) \approx x^2/2$, which is consistent with the CLT (Gaussian tail with variance $1/n$).

??? success "Solution to Exercise 4"
    **$I(x) \geq 0$ with equality only at $x = 0$:** Define $f(x) = \frac{1+x}{2}\log(1+x) + \frac{1-x}{2}\log(1-x)$ for $|x| \leq 1$. At $x = 0$: $f(0) = \frac{1}{2}\log 1 + \frac{1}{2}\log 1 = 0$. The first derivative is:

    $$
    f'(x) = \frac{1}{2}\log(1+x) - \frac{1}{2}\log(1-x) = \frac{1}{2}\log\frac{1+x}{1-x}
    $$

    So $f'(0) = 0$. The second derivative is:

    $$
    f''(x) = \frac{1}{2}\cdot\frac{1}{1+x} + \frac{1}{2}\cdot\frac{1}{1-x} = \frac{1}{1-x^2}
    $$

    Since $f''(x) > 0$ for all $|x| < 1$, $f$ is strictly convex on $(-1,1)$. A strictly convex function with $f(0) = 0$ and $f'(0) = 0$ satisfies $f(x) > 0$ for all $x \neq 0$ in $(-1,1)$.

    **Verification that $I''(0) = 1$:** From above, $f''(0) = 1/(1-0) = 1$. Therefore near $x = 0$:

    $$
    I(x) \approx \frac{1}{2}I''(0)x^2 = \frac{x^2}{2}
    $$

    The large deviation principle gives $\mathbb{P}(S_n/n \approx x) \approx e^{-nI(x)} \approx e^{-nx^2/2}$ for small $x$. With $x = a/\sqrt{n}$, this gives $\mathbb{P}(S_n \approx a\sqrt{n}) \approx e^{-a^2/2}$, matching the Gaussian tail from the CLT.

---

**Exercise 5.** Use Markov's inequality with the MGF to derive a Chernoff bound for the symmetric random walk: show that for $a > 0$,

$$
\mathbb{P}(S_n \geq an) \leq \inf_{\lambda > 0} e^{-\lambda an} (\cosh \lambda)^n = e^{-nI(a)}
$$

Compute this bound numerically for $n = 100$ and $a = 0.3$. Compare with the normal approximation $\mathbb{P}(S_{100} \geq 30)$.

??? success "Solution to Exercise 5"
    By Markov's inequality, for any $\lambda > 0$:

    $$
    \mathbb{P}(S_n \geq an) = \mathbb{P}(e^{\lambda S_n} \geq e^{\lambda an}) \leq \frac{\mathbb{E}[e^{\lambda S_n}]}{e^{\lambda an}} = e^{-\lambda an}(\cosh\lambda)^n
    $$

    Optimizing over $\lambda > 0$:

    $$
    \mathbb{P}(S_n \geq an) \leq \inf_{\lambda > 0} e^{-n(\lambda a - \log\cosh\lambda)} = e^{-nI(a)}
    $$

    For $n = 100$, $a = 0.3$: we need $I(0.3) = \frac{1.3}{2}\log 1.3 + \frac{0.7}{2}\log 0.7 = 0.65 \cdot 0.2624 + 0.35 \cdot (-0.3567) = 0.1706 - 0.1248 = 0.0457$.

    $$
    \mathbb{P}(S_{100} \geq 30) \leq e^{-100 \cdot 0.0457} = e^{-4.57} \approx 0.0104
    $$

    For the normal approximation: $\mathbb{P}(S_{100} \geq 30) = \mathbb{P}(Z \geq 30/\sqrt{100}) = \mathbb{P}(Z \geq 3) = 1 - \Phi(3) \approx 0.00135$. The Chernoff bound ($\approx 0.0104$) is a valid upper bound but is looser than the exact Gaussian estimate. The discrepancy is expected because the Chernoff bound applies for all $n$, while the normal approximation is an asymptotic result.

---

**Exercise 6.** The cumulant generating function is $\Lambda(\lambda) = n\log\cosh\lambda$. Show that all odd cumulants of $S_n$ are zero. Compute the first three nonzero cumulants ($\kappa_2$, $\kappa_4$, $\kappa_6$) and verify that the **excess kurtosis** $\kappa_4 / \kappa_2^2 = -2/n$ vanishes as $n \to \infty$, consistent with the CLT (the Gaussian has zero excess kurtosis).

??? success "Solution to Exercise 6"
    The cumulant generating function is $\Lambda(\lambda) = n\log\cosh\lambda$. Since $\cosh\lambda = \cosh(-\lambda)$ is an even function, $\log\cosh\lambda$ contains only even powers of $\lambda$. Therefore $\Lambda(\lambda) = \sum_{k=1}^\infty \kappa_k \frac{\lambda^k}{k!}$ has $\kappa_k = 0$ for all odd $k$: all odd cumulants vanish.

    Using the expansion $\log\cosh\lambda = \frac{\lambda^2}{2} - \frac{\lambda^4}{12} + \frac{\lambda^6}{45} - \cdots$:

    $$
    \Lambda(\lambda) = n\left(\frac{\lambda^2}{2} - \frac{\lambda^4}{12} + \frac{\lambda^6}{45} - \cdots\right)
    $$

    Reading off $\kappa_k \frac{\lambda^k}{k!}$:

    - $\kappa_2 = n$ (from $\frac{n\lambda^2}{2} = \kappa_2\frac{\lambda^2}{2!}$)
    - $\kappa_4 = -2n$ (from $-\frac{n\lambda^4}{12} = \kappa_4\frac{\lambda^4}{4!}$, so $\kappa_4 = -\frac{n \cdot 24}{12} = -2n$)
    - $\kappa_6 = 16n$ (from $\frac{n\lambda^6}{45} = \kappa_6\frac{\lambda^6}{6!}$, so $\kappa_6 = \frac{n \cdot 720}{45} = 16n$)

    The excess kurtosis is:

    $$
    \frac{\kappa_4}{\kappa_2^2} = \frac{-2n}{n^2} = \frac{-2}{n} \xrightarrow{n\to\infty} 0
    $$

    This vanishing is consistent with the CLT: $S_n/\sqrt{n} \to \mathcal{N}(0,1)$, and the Gaussian distribution has excess kurtosis 0.
