# Pricing Exotic Options with Binomial Trees

## Introduction

The **binomial tree** method extends naturally to price exotic options by tracking **additional state variables** at each node. For barrier options, we track whether the barrier has been breached; for Asian options, we track the running average; for lookback options, we track the running maximum or minimum. While conceptually straightforward, the state-space expansion introduces computational challenges that limit the method's applicability to low-dimensional exotics.

!!! info "Prerequisites"
    - [Multi-Period Binomial Model](../../ch01/binomial_model/multi_period_binomial_model.md) (backward induction)
    - [Binomial Pricing of American Options](../american_options/binomial_pricing.md) (early-exercise on trees)
    - [Barrier Options](barrier_options.md) (payoff definitions)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Implement a binomial tree for down-and-out barrier call options
    2. Understand state-space expansion for path-dependent options
    3. Identify convergence issues specific to barrier options on trees
    4. Recognize computational limits of tree methods for complex exotics

---

## Binomial Tree Recap

In the Cox–Ross–Rubinstein (CRR) framework with $N$ time steps:

$$
\Delta t = \frac{T}{N}, \quad u = e^{\sigma\sqrt{\Delta t}}, \quad d = \frac{1}{u}, \quad q = \frac{e^{r\Delta t} - d}{u - d}
$$

The stock price at node $(n, j)$ is:

$$
S_{n,j} = S_0 \cdot u^j \cdot d^{n - j}, \quad 0 \leq j \leq n \leq N
$$

For vanilla options, backward induction gives the option value at each node:

$$
V_{n,j} = e^{-r\Delta t}\left[q\, V_{n+1,j+1} + (1-q)\, V_{n+1,j}\right]
$$

---

## Barrier Options on Binomial Trees

### Algorithm: Down-and-Out Call

For a down-and-out call with strike $K$ and barrier $H < S_0$, we modify the standard backward induction by **enforcing the barrier condition at every node**:

!!! note "Down-and-Out Barrier Call Algorithm"
    **Step 1.** Build the CRR stock price tree: $S_{n,j} = S_0 \cdot u^j \cdot d^{n-j}$
    
    **Step 2.** Set terminal values with barrier enforcement:
    
    $$V_{N,j} = \begin{cases} (S_{N,j} - K)^+ & \text{if } S_{N,j} > H \\ 0 & \text{if } S_{N,j} \leq H \end{cases}$$
    
    **Step 3.** Backward induction with barrier:
    
    $$V_{n,j} = \begin{cases} e^{-r\Delta t}\left[q\, V_{n+1,j+1} + (1-q)\, V_{n+1,j}\right] & \text{if } S_{n,j} > H \\ 0 & \text{if } S_{n,j} \leq H \end{cases}$$
    
    **Step 4.** The barrier option price is $V_{0,0}$.

The barrier check at each node simulates discrete monitoring at the tree's time resolution.

### Implementation

```python
import numpy as np

def barrier_call_binomial(S, K, H, T, r, sigma, N):
    """Price a down-and-out barrier call using a binomial tree."""
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Build stock price tree
    ST = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(i + 1):
            ST[j, i] = S * (u ** j) * (d ** (i - j))

    # Terminal payoffs with barrier
    C = np.maximum(ST[:, N] - K, 0)
    C[ST[:, N] <= H] = 0

    # Backward induction with barrier enforcement
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            if ST[j, i] > H:
                C[j] = np.exp(-r * dt) * (p * C[j + 1] + (1 - p) * C[j])
            else:
                C[j] = 0

    return C[0]
```

### Convergence Issues

Barrier options on binomial trees exhibit **oscillatory convergence** as a function of $N$. The oscillation occurs because the barrier level $H$ generally does not coincide exactly with a row of nodes in the tree.

**Barrier alignment.** When $H$ falls between two adjacent node levels, the effective barrier applied by the tree alternates between the two levels as $N$ changes, causing price oscillation. This is sometimes called the **specification error**.

**Remedies include:**

- **Adaptive mesh refinement**: Place extra nodes near the barrier
- **Interpolation**: Adjust option values at nodes near the barrier by linear interpolation
- **Choosing $N$ to align with barrier**: Select $N$ such that $H = S_0 \cdot u^j \cdot d^{n-j}$ for some integers $j, n$

---

## Asian Options on Binomial Trees

### State-Space Expansion

For an Asian option, the payoff depends on the running average $\bar{S}_n = \frac{1}{n+1}\sum_{k=0}^{n} S_k$. To price this on a tree, each node must track **both the current price and the running average**, creating a two-dimensional state space.

At time step $n$ with $j$ up-moves, there are $\binom{n}{j}$ distinct paths, each potentially producing a different running average. The total number of distinct averages across all nodes grows combinatorially:

$$
\text{Total states} = \sum_{n=0}^{N} \sum_{j=0}^{n} \binom{n}{j} = \sum_{n=0}^{N} 2^n = 2^{N+1} - 1
$$

This **exponential growth** makes exact tree pricing of Asian options computationally intractable for large $N$.

### Hull–White Approximation

Hull and White (1993) proposed a practical approximation:

1. At each node $(n, j)$, define a **discrete grid of representative average values**
2. Compute option values at each grid point by backward induction
3. Use **interpolation** between grid points

This reduces the complexity from exponential to polynomial in $N$, at the cost of introducing interpolation error.

---

## Lookback Options on Binomial Trees

For lookback options, each node must track the **running maximum** (or minimum) in addition to the current price. The state space is $(S_{n,j}, S_{\max})$ where $S_{\max}$ varies depending on the path taken to reach node $(n, j)$.

The number of distinct running maxima at node $(n, j)$ can be bounded by $j + 1$ (since each of the $j + 1$ possible high-water marks corresponds to a different set of paths). This produces a state space that grows quadratically rather than exponentially, making tree-based lookback pricing more tractable than Asian option pricing.

---

## Computational Complexity Comparison

| Exotic Type | State Variables | State Space Growth | Tree Practicality |
|---|---|---|---|
| Barrier | Price + barrier status (boolean) | $O(N^2)$ | Practical |
| Asian (exact) | Price + running average | $O(2^N)$ | Impractical |
| Asian (Hull–White) | Price + discretized average | $O(N^2 \cdot M)$ | Practical with approximation |
| Lookback | Price + running max/min | $O(N^3)$ | Feasible for moderate $N$ |
| Multi-asset | Multiple prices | $O(N^d)$ where $d$ = dimension | Impractical for $d \geq 3$ |

---

## Summary

| Aspect | Description |
|---|---|
| Core idea | Extend binomial tree with additional state variables |
| Barrier options | Practical: enforce barrier condition at each node |
| Asian options | Impractical without approximation (exponential states) |
| Lookback options | Feasible but computationally heavy (cubic growth) |
| Main limitation | Curse of dimensionality as state space expands |
| Key issue | Oscillatory convergence for barrier options (specification error) |

**Binomial trees extend naturally to exotic option pricing by tracking path-dependent state variables, but the exponential growth of state spaces for complex path dependencies limits their practical use to barrier options and low-dimensional problems.**

---

## Exercises

**Exercise 1.** For a down-and-out call with $S_0 = 100$, $K = 100$, $H = 90$, $T = 1$, $r = 5\%$, $\sigma = 20\%$, build a 3-step CRR binomial tree. At each node, compute the stock price, identify whether the barrier has been breached, and calculate the option value using backward induction with barrier enforcement. Compare your result with the vanilla call price from the same tree.

---

**Exercise 2.** Explain the "specification error" that causes oscillatory convergence when pricing barrier options on binomial trees. Specifically, for a barrier at $H = 90$ and a CRR tree with $u = e^{\sigma\sqrt{\Delta t}}$, show that $H$ generally does not coincide with any node $S_0 u^j d^{n-j}$. Describe the adaptive mesh refinement technique that mitigates this problem.

---

**Exercise 3.** For an Asian option on a 3-step binomial tree, enumerate all possible paths and their corresponding arithmetic averages. Verify that the number of distinct averages is $2^3 = 8$ (one per path), and explain why this exponential growth makes exact tree pricing of Asian options impractical for large $N$.

---

**Exercise 4.** The Hull-White approximation for Asian options on trees uses interpolation between representative average values at each node. Describe the algorithm: (a) How are the representative average values chosen at each node? (b) How is backward induction performed with interpolation? (c) What is the computational complexity as a function of $N$ and the number of average grid points $M$?

---

**Exercise 5.** For a lookback option on a binomial tree, the state at each node is $(S_{n,j}, S_{\max})$. At node $(n, j)$ with $j$ up-moves out of $n$ steps, how many distinct values of $S_{\max}$ are possible? Derive the bound and explain why lookback options have $O(N^3)$ complexity on trees, compared to $O(N^2)$ for barrier options.

---

**Exercise 6.** Compare the binomial tree and Monte Carlo methods for pricing a down-and-out barrier call with $N = 200$ time steps and $10{,}000$ Monte Carlo paths. Which method gives a more accurate price? Discuss the trade-offs in terms of convergence behavior, computational cost, and ease of implementation for barrier options specifically.
