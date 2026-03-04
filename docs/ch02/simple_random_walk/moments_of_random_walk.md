# Moments of the Random Walk

The first two moments of $S_n$ — its mean and variance — are the most basic quantitative facts about the walk. We derive them in full detail, presenting every algebraic step. Students who are comfortable with these computations should still read the summary table at the end, as the formulas recur throughout the chapter.

---

## Step Distribution

Each increment $X_i$ takes values in $\{-1, +1\}$ with

$$\mathbb{P}(X_i = +1) = p, \qquad \mathbb{P}(X_i = -1) = 1-p.$$

We record the moments of a single step first; everything for $S_n$ follows by independence and summation.

### Mean of a Single Step

Applying the definition of expectation directly:

$$\mathbb{E}[X_i] = (+1) \cdot p + (-1) \cdot (1-p) = p - 1 + p = 2p - 1.$$

We denote this drift per step by $\mu := 2p - 1$. Observe:

- $p > 1/2 \Rightarrow \mu > 0$ (upward bias).
- $p < 1/2 \Rightarrow \mu < 0$ (downward bias).
- $p = 1/2 \Rightarrow \mu = 0$ (no bias; symmetric case).

### Second Moment of a Single Step

Regardless of the sign of $X_i$, its square is always 1:

$$X_i^2 = (+1)^2 = (-1)^2 = 1 \quad \text{almost surely.}$$

Therefore $\mathbb{E}[X_i^2] = 1$.

### Variance of a Single Step

Using the identity $\text{Var}(X_i) = \mathbb{E}[X_i^2] - (\mathbb{E}[X_i])^2$:

$$\text{Var}(X_i) = 1 - (2p-1)^2.$$

Expanding $(2p-1)^2 = 4p^2 - 4p + 1$:

$$\text{Var}(X_i) = 1 - (4p^2 - 4p + 1) = 4p - 4p^2 = 4p(1-p).$$

This expression is maximised at $p = 1/2$, where $\text{Var}(X_i) = 1$, and tends to $0$ as $p \to 0$ or $p \to 1$ (degenerate cases with no randomness).

---

## Mean of $S_n$

Since $S_n = \sum_{i=1}^n X_i$ and each $X_i$ has the same distribution, linearity of expectation gives:

$$\mathbb{E}[S_n] = \mathbb{E}\!\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n \mathbb{E}[X_i] = \sum_{i=1}^n (2p-1) = n(2p-1).$$

!!! note "Linearity of expectation requires no independence"
    The step $\mathbb{E}[\sum_{i=1}^n X_i] = \sum_{i=1}^n \mathbb{E}[X_i]$ holds for *any* integrable random variables, dependent or not. Independence is not needed for the mean.

**Symmetric case ($p = 1/2$).** The drift vanishes:

$$\mathbb{E}[S_n] = n(2 \cdot \tfrac{1}{2} - 1) = n \cdot 0 = 0 \quad \text{for all } n \geq 0.$$

The walk is centred at the origin at every time step. This is not a coincidence — it is equivalent to the martingale property proved in [Martingale Property](martingale_property.md): $\mathbb{E}[S_n \mid \mathcal{F}_{n-1}] = S_{n-1}$ implies $\mathbb{E}[S_n] = \mathbb{E}[S_0] = 0$.

---

## Variance of $S_n$

### Method 1: Additivity of Variance

Since $X_1, X_2, \ldots, X_n$ are **independent**, the variance of their sum equals the sum of their variances:

$$\text{Var}(S_n) = \text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) = \sum_{i=1}^n 4p(1-p) = 4np(1-p).$$

!!! warning "Independence is essential here"
    Unlike linearity of expectation, the identity $\text{Var}(\sum X_i) = \sum \text{Var}(X_i)$ requires that the $X_i$ be **uncorrelated** (pairwise independence suffices). For the random walk the $X_i$ are fully independent, so this holds without qualification.

**Symmetric case ($p = 1/2$):**

$$\text{Var}(S_n) = 4n \cdot \tfrac{1}{2} \cdot \tfrac{1}{2} = n.$$

The standard deviation is $\text{SD}(S_n) = \sqrt{n}$. After $n$ steps, a typical excursion from the origin is of order $\sqrt{n}$, not $n$. This **diffusive scaling** ($\sim\sqrt{n}$) is the signature of randomness without drift and persists in the Brownian motion limit.

---

### Method 2: Direct Expansion of $\mathbb{E}[S_n^2]$

This second derivation is longer but makes the role of the cross terms explicit, which is important for higher-moment calculations.

**Expand the square:**

$$S_n^2 = \left(\sum_{i=1}^n X_i\right)^2 = \sum_{i=1}^n X_i^2 + 2\sum_{1 \leq i < j \leq n} X_i X_j.$$

**Take expectations.** For the diagonal terms, $\mathbb{E}[X_i^2] = 1$. For cross terms with $i \neq j$, independence gives:

$$\mathbb{E}[X_i X_j] = \mathbb{E}[X_i]\,\mathbb{E}[X_j] = (2p-1)^2.$$

The number of pairs $(i,j)$ with $i < j$ is $\binom{n}{2} = n(n-1)/2$, so:

$$\mathbb{E}[S_n^2] = n \cdot 1 + 2 \cdot \frac{n(n-1)}{2} \cdot (2p-1)^2 = n + n(n-1)(2p-1)^2.$$

**Subtract the squared mean:**

$$\text{Var}(S_n) = \mathbb{E}[S_n^2] - (\mathbb{E}[S_n])^2
= n + n(n-1)(2p-1)^2 - n^2(2p-1)^2.$$

Factor out $(2p-1)^2$:

$$= n + (2p-1)^2\bigl[n(n-1) - n^2\bigr]
= n + (2p-1)^2 \cdot (-n)
= n\bigl[1-(2p-1)^2\bigr]
= 4np(1-p). \quad\square$$

Both methods agree, as required.

---

### Method 3: Covariance Expansion (Symmetric Case)

For $p = 1/2$ there is a third, particularly transparent route that shows *why* the cross terms vanish.

$$\mathbb{E}[S_n^2] = \mathbb{E}\!\left[\left(\sum_{i=1}^n \xi_i\right)^2\right]
= \sum_{i=1}^n \mathbb{E}[\xi_i^2] + 2\sum_{i < j} \mathbb{E}[\xi_i \xi_j].$$

- **Diagonal:** $\mathbb{E}[\xi_i^2] = 1$ for all $i$.
- **Off-diagonal:** By independence, $\mathbb{E}[\xi_i \xi_j] = \mathbb{E}[\xi_i]\,\mathbb{E}[\xi_j] = 0 \cdot 0 = 0$ for $i \neq j$.

Therefore every cross term vanishes and:

$$\mathbb{E}[S_n^2] = n + 0 = n \implies \text{Var}(S_n) = n.$$

The vanishing of $\mathbb{E}[\xi_i \xi_j]$ reflects the absence of any correlation between non-overlapping steps: the walk has no memory (Markov property, [Martingale Property](martingale_property.md)).

---

## Fourth Moment (Symmetric Case)

**Proposition 1.1.1** (Moments of the Random Walk)

For the general walk with parameter $p$:

$$\mathbb{E}[S_n] = n(2p-1), \qquad \text{Var}(S_n) = 4np(1-p).$$

For the symmetric walk ($p = 1/2$):

$$\mathbb{E}[S_n] = 0, \qquad \text{Var}(S_n) = n, \qquad \mathbb{E}[S_n^4] = 3n^2 - 2n.$$

**Proof of the fourth moment.** Expand:

$$\mathbb{E}[S_n^4] = \sum_{i,j,k,l=1}^{n} \mathbb{E}[\xi_i \xi_j \xi_k \xi_l].$$

Since $\mathbb{E}[\xi_i] = 0$ and the $\xi_i$ are independent, a term $\mathbb{E}[\xi_i \xi_j \xi_k \xi_l]$ is nonzero only when every index appears an even number of times. The distinct cases are:

- **$i=j=k=l$:** gives $\mathbb{E}[\xi_i^4] = 1$; there are $n$ such terms. Total: $n$.
- **Two distinct pairs**, e.g.\ $i=j \neq k=l$: gives $\mathbb{E}[\xi_i^2]\mathbb{E}[\xi_k^2] = 1$; there are $\binom{n}{2}$ choices of $\{i,k\}$ and 3 ways to partition four indices into two pairs. Total: $3n(n-1)$.

Therefore:

$$\mathbb{E}[S_n^4] = n + 3n(n-1) = 3n^2 - 2n. \quad\square$$

---

## Summary Table

| Quantity | General walk | Symmetric walk |
|---|---|---|
| $\mathbb{E}[X_i]$ | $2p-1$ | $0$ |
| $\mathbb{E}[X_i^2]$ | $1$ | $1$ |
| $\text{Var}(X_i)$ | $4p(1-p)$ | $1$ |
| $\mathbb{E}[S_n]$ | $n(2p-1)$ | $0$ |
| $\text{Var}(S_n)$ | $4np(1-p)$ | $n$ |
| $\text{SD}(S_n)$ | $2\sqrt{np(1-p)}$ | $\sqrt{n}$ |
| $\mathbb{E}[S_n^4]$ | — | $3n^2 - 2n$ |

---

## References

- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley.
- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
