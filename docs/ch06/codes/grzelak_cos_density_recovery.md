# Grzelak Cos Density Recovery

## Background

# ======================================================================

Grzelak Cos Density Recovery

Educational script demonstrating grzelak cos density recovery concepts.

---

## Code

```python
"""
# ======================================================================

Grzelak Cos Density Recovery

Educational script demonstrating grzelak cos density recovery concepts.
"""

# This file was placed here in error — COS method content belongs in ch09.
# See ch09/codes/grzelak_density_recovery_fft.py for the correct placement.
# This file can be safely deleted.


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
The COS method recovers a probability density from its characteristic function. Write the characteristic function of the log-normal distribution and explain why it is useful for option pricing.

??? success "Solution to Exercise 1"
    For $\ln(S_T/S_0) \sim \mathcal{N}(\mu_X, \sigma_X^2)$ where $\mu_X = (r - \frac{1}{2}\sigma^2)T$ and $\sigma_X^2 = \sigma^2 T$, the characteristic function is

    $$
    \varphi(u) = E[e^{iu\ln(S_T/S_0)}] = \exp\!\bigl(iu\mu_X - \tfrac{1}{2}u^2\sigma_X^2\bigr)
    $$

    This is useful because: (1) characteristic functions always exist (unlike densities which may not be analytically known), (2) they have simple forms for many models (Heston, VG, NIG), and (3) the COS method can efficiently invert $\varphi$ to get prices without computing the density explicitly.

---

**Exercise 2.**
Explain the COS method. How does it approximate the density using a cosine series expansion?

??? success "Solution to Exercise 2"
    The COS method approximates the density on a truncated interval $[a, b]$ using a cosine series:

    $$
    f(x) \approx \sum_{k=0}^{N-1} {}' A_k \cos\!\Bigl(k\pi\frac{x - a}{b - a}\Bigr)
    $$

    where the prime means the first term is halved, and the coefficients are $A_k = \frac{2}{b-a}\text{Re}\!\bigl[\varphi\bigl(\frac{k\pi}{b-a}\bigr)e^{-ika\pi/(b-a)}\bigr]$.

    The key insight is that the coefficients $A_k$ depend only on the characteristic function $\varphi$, which is known analytically. This avoids numerical integration of the density.

---

**Exercise 3.**
This file is a placeholder (the COS method content belongs in a later chapter). Explain why the COS method is more naturally associated with Fourier methods in option pricing than with the basic BS chapter.

??? success "Solution to Exercise 3"
    The COS method is a Fourier-based technique that exploits the characteristic function for pricing. While it can be applied to BS (where the characteristic function is log-normal), its real power appears in models where the density is not analytically available but the characteristic function is (e.g., Heston, Variance Gamma, NIG).

    In the basic BS chapter, analytical formulas suffice. The COS method becomes essential in later chapters covering stochastic volatility and Levy processes, where it provides an efficient alternative to Monte Carlo for European option pricing.

---

**Exercise 4.**
How many cosine terms $N$ are typically needed for accurate density recovery? What determines the convergence rate of the COS expansion?

??? success "Solution to Exercise 4"
    Typically $N = 64$ to $256$ terms suffice for financial applications. The convergence rate depends on the smoothness of the density:

    - For smooth densities (e.g., log-normal): exponential convergence, so $N = 32$--$64$ gives machine precision.
    - For densities with jumps or kinks: algebraic convergence, requiring $N = 128$--$256$.

    The truncation interval $[a, b]$ must also be chosen carefully: too narrow misses probability mass in the tails; too wide wastes cosine terms on near-zero density regions. A common heuristic is $[a, b] = [\mu \pm 10\sigma]$.
