# Moments of the Random Walk

The first two moments of $S_n$ — its mean and variance — are the most basic quantitative facts about the walk. We derive them in full detail, presenting every algebraic step. Students who are comfortable with these computations should still read the summary table at the end, as the formulas recur throughout the chapter.

---

## Step Distribution

Each increment $\xi_i$ takes values in $\{-1, +1\}$ with

$$\mathbb{P}(\xi_i = +1) = p, \qquad \mathbb{P}(\xi_i = -1) = 1-p$$

We record the moments of a single step first; everything for $S_n$ follows by independence and summation.

### Mean of a Single Step

Applying the definition of expectation directly:

$$\mathbb{E}[\xi_i] = (+1) \cdot p + (-1) \cdot (1-p) = p - 1 + p = 2p - 1$$

We denote this drift per step by $\mu := 2p - 1$. Observe:

- $p > 1/2 \Rightarrow \mu > 0$ (upward bias).
- $p < 1/2 \Rightarrow \mu < 0$ (downward bias).
- $p = 1/2 \Rightarrow \mu = 0$ (no bias; symmetric case).

### Second Moment of a Single Step

Regardless of the sign of $\xi_i$, its square is always 1:

$$\xi_i^2 = (+1)^2 = (-1)^2 = 1 \quad \text{almost surely.}$$

Therefore $\mathbb{E}[\xi_i^2] = 1$.

### Variance of a Single Step

Using the identity $\text{Var}(\xi_i) = \mathbb{E}[\xi_i^2] - (\mathbb{E}[\xi_i])^2$:

$$\text{Var}(\xi_i) = 1 - (2p-1)^2$$

Expanding $(2p-1)^2 = 4p^2 - 4p + 1$:

$$\text{Var}(\xi_i) = 1 - (4p^2 - 4p + 1) = 4p - 4p^2 = 4p(1-p)$$

This expression is maximised at $p = 1/2$, where $\text{Var}(\xi_i) = 1$, and tends to $0$ as $p \to 0$ or $p \to 1$ (degenerate cases with no randomness).

---

## Mean of $S_n$

Since $S_n = \sum_{i=1}^n \xi_i$ and each $\xi_i$ has the same distribution, linearity of expectation gives:

$$\mathbb{E}[S_n] = \mathbb{E}\!\left[\sum_{i=1}^n \xi_i\right] = \sum_{i=1}^n \mathbb{E}[\xi_i] = \sum_{i=1}^n (2p-1) = n(2p-1)$$

!!! note "Linearity of expectation requires no independence"
    The step $\mathbb{E}[\sum_{i=1}^n \xi_i] = \sum_{i=1}^n \mathbb{E}[\xi_i]$ holds for *any* integrable random variables, dependent or not. Independence is not needed for the mean.

**Symmetric case ($p = 1/2$).** The drift vanishes:

$$\mathbb{E}[S_n] = n(2 \cdot \tfrac{1}{2} - 1) = n \cdot 0 = 0 \quad \text{for all } n \geq 0$$

The walk is centred at the origin at every time step. This is equivalent to the martingale property proved in [Martingale Property](martingale_property.md): $\mathbb{E}[S_n \mid \mathcal{F}_{n-1}] = S_{n-1}$ implies $\mathbb{E}[S_n] = \mathbb{E}[S_0] = 0$.

---

## Variance of $S_n$

### Method 1: Additivity of Variance

Since $\xi_1, \xi_2, \ldots, \xi_n$ are **independent**, the variance of their sum equals the sum of their variances:

$$\text{Var}(S_n) = \text{Var}\!\left(\sum_{i=1}^n \xi_i\right) = \sum_{i=1}^n \text{Var}(\xi_i) = \sum_{i=1}^n 4p(1-p) = 4np(1-p)$$

!!! warning "Independence is essential here"
    Unlike linearity of expectation, the identity $\text{Var}(\sum \xi_i) = \sum \text{Var}(\xi_i)$ requires that the $\xi_i$ be **uncorrelated** (pairwise independence suffices). For the random walk the $\xi_i$ are fully independent, so this holds without qualification.

**Symmetric case ($p = 1/2$):**

$$\text{Var}(S_n) = 4n \cdot \tfrac{1}{2} \cdot \tfrac{1}{2} = n$$

The standard deviation is $\sqrt{n}$. After $n$ steps, a typical excursion from the origin is of order $\sqrt{n}$, not $n$. This **diffusive scaling** ($\sim\sqrt{n}$) is the signature of randomness without drift and persists in the Brownian motion limit.

---

### Method 2: Direct Expansion of $\mathbb{E}[S_n^2]$

This derivation makes the role of cross terms explicit, which matters for higher-moment calculations.

**Expand the square:**

$$S_n^2 = \left(\sum_{i=1}^n \xi_i\right)^2 = \sum_{i=1}^n \xi_i^2 + 2\sum_{1 \leq i < j \leq n} \xi_i \xi_j$$

**Take expectations.** For diagonal terms, $\mathbb{E}[\xi_i^2] = 1$. For cross terms with $i \neq j$, independence gives:

$$\mathbb{E}[\xi_i \xi_j] = \mathbb{E}[\xi_i]\,\mathbb{E}[\xi_j] = (2p-1)^2$$

The number of pairs $(i,j)$ with $i < j$ is $\binom{n}{2} = n(n-1)/2$, so:

$$\mathbb{E}[S_n^2] = n \cdot 1 + 2 \cdot \frac{n(n-1)}{2} \cdot (2p-1)^2 = n + n(n-1)(2p-1)^2$$

**Subtract the squared mean:**

$$\text{Var}(S_n) = \mathbb{E}[S_n^2] - (\mathbb{E}[S_n])^2
= n + n(n-1)(2p-1)^2 - n^2(2p-1)^2$$

Factor out $(2p-1)^2$:

$$= n + (2p-1)^2\bigl[n(n-1) - n^2\bigr]
= n + (2p-1)^2 \cdot (-n)
= n\bigl[1-(2p-1)^2\bigr]
= 4np(1-p). \quad\square$$

Both methods agree.

!!! note "Why cross terms vanish when $p = 1/2$"
    In the symmetric case $\mathbb{E}[\xi_i] = 0$, so independence gives $\mathbb{E}[\xi_i \xi_j] = \mathbb{E}[\xi_i]\mathbb{E}[\xi_j] = 0$ for $i \neq j$. Every off-diagonal term vanishes and $\mathbb{E}[S_n^2] = n$ immediately. The vanishing of $\mathbb{E}[\xi_i \xi_j]$ reflects the absence of correlation between non-overlapping steps — a consequence of the Markov property (see [Martingale Property](martingale_property.md)).

---

## Fourth Moment (Symmetric Case)

**Proposition 1.1.1** (Moments of the Random Walk)

For the general walk with parameter $p$:

$$\mathbb{E}[S_n] = n(2p-1), \qquad \text{Var}(S_n) = 4np(1-p)$$

For the symmetric walk ($p = 1/2$):

$$\mathbb{E}[S_n] = 0, \qquad \text{Var}(S_n) = n, \qquad \mathbb{E}[S_n^4] = 3n^2 - 2n$$

**Proof of the fourth moment.** Expand:

$$\mathbb{E}[S_n^4] = \sum_{i,j,k,l=1}^{n} \mathbb{E}[\xi_i \xi_j \xi_k \xi_l]$$

Since $\mathbb{E}[\xi_i] = 0$ and the $\xi_i$ are independent, a term $\mathbb{E}[\xi_i \xi_j \xi_k \xi_l]$ is nonzero only when every distinct index appears an even number of times. The surviving cases are:

- **All four indices equal**, $i = j = k = l$: gives $\mathbb{E}[\xi_i^4] = 1$; there are $n$ such terms. Total contribution: $n$.
- **Exactly two distinct indices**, each appearing twice: the four slots $(i,j,k,l)$ can be partitioned into two equal pairs in exactly three ways — $\{(i=j,\,k=l)\}$, $\{(i=k,\,j=l)\}$, $\{(i=l,\,j=k)\}$. For each pairing, the two index values $a,b$ must be distinct. Since the sum $\sum_{i,j,k,l=1}^n$ runs over **ordered** quadruples, we count ordered pairs $(a,b)$ with $a \neq b$: there are $n$ choices for $a$ and $n-1$ choices for $b$, giving $n(n-1)$ ordered pairs. Each gives $\mathbb{E}[\xi_a^2]\mathbb{E}[\xi_b^2] = 1$. With 3 pairings, total contribution: $3n(n-1)$.

No other cases survive: if three or more distinct indices appear with an odd multiplicity, the expectation factorises to include $\mathbb{E}[\xi_i] = 0$.

Therefore:

$$\mathbb{E}[S_n^4] = n + 3n(n-1) = 3n^2 - 2n. \quad\square$$

---

## Summary Table

| Quantity | General walk | Symmetric walk ($p = 1/2$) |
|---|---|---|
| $\mathbb{E}[\xi_i]$ | $2p-1$ | $0$ |
| $\mathbb{E}[\xi_i^2]$ | $1$ | $1$ |
| $\text{Var}(\xi_i)$ | $4p(1-p)$ | $1$ |
| $\mathbb{E}[S_n]$ | $n(2p-1)$ | $0$ |
| $\text{Var}(S_n)$ | $4np(1-p)$ | $n$ |
| $\mathbb{E}[S_n^4]$ | — | $3n^2 - 2n$ |

---

## References

- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley.
- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.

---

## Exercises

**Exercise 1.** For the asymmetric random walk with $p = 0.7$, compute $\mathbb{E}[S_{50}]$, $\text{Var}(S_{50})$, and $\mathbb{E}[S_{50}^2]$. After how many steps does the mean exceed $2$ standard deviations (i.e., find the smallest $n$ such that $\mathbb{E}[S_n] > 2\sqrt{\text{Var}(S_n)}$)?

---

**Exercise 2.** Verify the fourth moment formula $\mathbb{E}[S_n^4] = 3n^2 - 2n$ for $n = 1$ and $n = 2$ by direct computation. For $n = 1$, $S_1 = \xi_1 \in \{-1, +1\}$, so $S_1^4 = 1$ always. For $n = 2$, enumerate all four equally likely outcomes of $(\xi_1, \xi_2)$ and compute $\mathbb{E}[S_2^4]$.

---

**Exercise 3.** Show that $\text{Var}(S_n^2) = \mathbb{E}[S_n^4] - (\mathbb{E}[S_n^2])^2 = 2n^2 - 2n$ for the symmetric random walk. Then compute $\text{Var}(S_n^2 - n)$ and verify it equals $2n^2 - 2n$. (This is the variance of the quadratic martingale $M_n = S_n^2 - n$.)

---

**Exercise 4.** For the general random walk ($p \neq 1/2$), the direct expansion gives $\mathbb{E}[S_n^2] = n + n(n-1)(2p-1)^2$. Derive $\mathbb{E}[S_n^2]$ independently using the identity $\mathbb{E}[S_n^2] = \text{Var}(S_n) + (\mathbb{E}[S_n])^2$ and the formulas for $\text{Var}(S_n)$ and $\mathbb{E}[S_n]$. Confirm both methods agree.

---

**Exercise 5.** The diffusive scaling $\text{SD}(S_n) = \sqrt{n}$ says that after $n$ steps, typical displacement is of order $\sqrt{n}$. A gambler plays $n = 10{,}000$ fair coin-flip games. Using the normal approximation, estimate the probability that the gambler is ahead by more than $\$200$ (i.e., $\mathbb{P}(S_{10000} > 200)$). Is this a likely outcome?

---

**Exercise 6.** Compute $\mathbb{E}[S_n^3]$ for the symmetric random walk by the index-counting method used for $\mathbb{E}[S_n^4]$. Show that $\mathbb{E}[S_n^3] = 0$ by arguing that all surviving terms in the expansion $\sum_{i,j,k} \mathbb{E}[\xi_i \xi_j \xi_k]$ vanish. Does this generalize: is $\mathbb{E}[S_n^k] = 0$ for all odd $k$? Why or why not?

---

## Solutions

??? success "Solution to Exercise 1"
    With $p = 0.7$, the drift per step is $\mu = 2(0.7) - 1 = 0.4$ and the step variance is $\sigma^2 = 4(0.7)(0.3) = 0.84$.

    $$
    \mathbb{E}[S_{50}] = 50 \cdot 0.4 = 20
    $$

    $$
    \text{Var}(S_{50}) = 50 \cdot 0.84 = 42
    $$

    $$
    \mathbb{E}[S_{50}^2] = \text{Var}(S_{50}) + (\mathbb{E}[S_{50}])^2 = 42 + 400 = 442
    $$

    We need the smallest $n$ such that $\mathbb{E}[S_n] > 2\sqrt{\text{Var}(S_n)}$, i.e., $0.4n > 2\sqrt{0.84n}$. Squaring:

    $$
    0.16n^2 > 4 \cdot 0.84n = 3.36n
    $$

    Dividing by $n$: $0.16n > 3.36$, so $n > 21$. The smallest such $n$ is $n = 22$.

??? success "Solution to Exercise 2"
    **For $n = 1$:** $S_1 = \xi_1 \in \{-1,+1\}$, so $S_1^4 = 1$ always. Thus $\mathbb{E}[S_1^4] = 1$. The formula gives $3(1)^2 - 2(1) = 1$. Confirmed.

    **For $n = 2$:** The four equally likely outcomes $(\xi_1, \xi_2)$ are $(+1,+1)$, $(+1,-1)$, $(-1,+1)$, $(-1,-1)$, giving $S_2 \in \{2, 0, 0, -2\}$. Therefore:

    $$
    \mathbb{E}[S_2^4] = \frac{1}{4}(2^4 + 0^4 + 0^4 + (-2)^4) = \frac{1}{4}(16 + 0 + 0 + 16) = 8
    $$

    The formula gives $3(2)^2 - 2(2) = 12 - 4 = 8$. Confirmed.

??? success "Solution to Exercise 3"
    We have $\mathbb{E}[S_n^2] = n$ and $\mathbb{E}[S_n^4] = 3n^2 - 2n$, so:

    $$
    \text{Var}(S_n^2) = \mathbb{E}[S_n^4] - (\mathbb{E}[S_n^2])^2 = (3n^2 - 2n) - n^2 = 2n^2 - 2n
    $$

    For the quadratic martingale $M_n = S_n^2 - n$:

    $$
    \text{Var}(M_n) = \text{Var}(S_n^2 - n) = \text{Var}(S_n^2)
    $$

    since subtracting a constant does not change the variance. Therefore $\text{Var}(M_n) = 2n^2 - 2n$.

    As a check: $\text{Var}(M_n) = \mathbb{E}[M_n^2] - (\mathbb{E}[M_n])^2 = \mathbb{E}[(S_n^2 - n)^2] - 0^2 = \mathbb{E}[S_n^4] - 2n\mathbb{E}[S_n^2] + n^2 = (3n^2 - 2n) - 2n^2 + n^2 = 2n^2 - 2n$. Confirmed.

??? success "Solution to Exercise 4"
    From the formulas: $\mathbb{E}[S_n] = n(2p-1)$ and $\text{Var}(S_n) = 4np(1-p)$. Using $\mathbb{E}[S_n^2] = \text{Var}(S_n) + (\mathbb{E}[S_n])^2$:

    $$
    \mathbb{E}[S_n^2] = 4np(1-p) + n^2(2p-1)^2
    $$

    Expanding $(2p-1)^2 = 4p^2 - 4p + 1$:

    $$
    = 4np - 4np^2 + 4n^2p^2 - 4n^2p + n^2
    $$

    From the direct expansion: $\mathbb{E}[S_n^2] = n + n(n-1)(2p-1)^2$. Expanding:

    $$
    = n + (n^2 - n)(4p^2 - 4p + 1) = n + 4n^2p^2 - 4n^2p + n^2 - 4np^2 + 4np - n
    $$

    $$
    = 4n^2p^2 - 4n^2p + n^2 - 4np^2 + 4np
    $$

    Both expressions are identical: $4np(1-p) + n^2(2p-1)^2 = 4np - 4np^2 + 4n^2p^2 - 4n^2p + n^2$, which matches the direct expansion.

??? success "Solution to Exercise 5"
    With $n = 10{,}000$ and $p = 1/2$: $\mathbb{E}[S_n] = 0$, $\text{Var}(S_n) = 10{,}000$, so $\text{SD}(S_n) = 100$. By the CLT:

    $$
    \mathbb{P}(S_{10000} > 200) = \mathbb{P}\!\left(\frac{S_{10000}}{100} > 2\right) \approx \mathbb{P}(Z > 2) = 1 - \Phi(2) \approx 0.0228
    $$

    So there is approximately a 2.3% chance the gambler is ahead by more than \$200 after 10,000 games. This is **not** a likely outcome — it corresponds to a 2-standard-deviation event. Despite the large number of games, the typical displacement is only $\sqrt{10{,}000} = 100$ (the standard deviation), and being ahead by \$200 is twice that.

??? success "Solution to Exercise 6"
    Expand $\mathbb{E}[S_n^3] = \sum_{i,j,k=1}^{n} \mathbb{E}[\xi_i \xi_j \xi_k]$. Since $\mathbb{E}[\xi_i] = 0$ and the $\xi_i$ are independent, $\mathbb{E}[\xi_i \xi_j \xi_k]$ is nonzero only when every distinct index appears an even number of times. With three index slots, the possible patterns are:

    - **All three equal** ($i = j = k$): $\mathbb{E}[\xi_i^3] = \mathbb{E}[\xi_i] = 0$ (since $\xi_i^3 = \xi_i$ when $\xi_i \in \{-1,+1\}$). Contribution: 0.
    - **Exactly two equal, one different** (e.g., $i = j \neq k$): $\mathbb{E}[\xi_i^2 \xi_k] = \mathbb{E}[\xi_i^2]\mathbb{E}[\xi_k] = 1 \cdot 0 = 0$. Contribution: 0.
    - **All three distinct**: $\mathbb{E}[\xi_i]\mathbb{E}[\xi_j]\mathbb{E}[\xi_k] = 0$. Contribution: 0.

    Every case gives 0, so $\mathbb{E}[S_n^3] = 0$.

    **Generalization:** Yes, $\mathbb{E}[S_n^k] = 0$ for all odd $k$. This follows from the symmetry $\xi_i \overset{d}{=} -\xi_i$, which implies $S_n \overset{d}{=} -S_n$. For any odd $k$: $\mathbb{E}[S_n^k] = \mathbb{E}[(-S_n)^k] = -\mathbb{E}[S_n^k]$, which forces $\mathbb{E}[S_n^k] = 0$. Alternatively, the index-counting argument shows that with an odd number of index slots, at least one distinct index must appear an odd number of times, introducing a factor of $\mathbb{E}[\xi_i^{\text{odd}}] = 0$.
