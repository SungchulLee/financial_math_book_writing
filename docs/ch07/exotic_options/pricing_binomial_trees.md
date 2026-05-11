# Pricing Exotic Options with Binomial Trees

## Introduction

The **binomial tree** method extends naturally to price exotic options by tracking **additional state variables** at each node. For barrier options, we track whether the barrier has been breached; for Asian options, we track the running average; for lookback options, we track the running maximum or minimum. While conceptually straightforward, the state-space expansion introduces computational challenges that limit the method's applicability to low-dimensional exotics.

!!! info "Prerequisites"

    - [Multi-Period Binomial Model](../../ch01/multi_period_model/multi_period_binomial_model.md) (backward induction)
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

??? success "Solution to Exercise 1"
    **CRR parameters** with $S_0 = 100$, $K = 100$, $H = 90$, $T = 1$, $r = 0.05$, $\sigma = 0.20$, $N = 3$:

    $$
    \Delta t = \frac{1}{3}, \quad u = e^{0.20\sqrt{1/3}} = e^{0.1155} \approx 1.1224
    $$

    $$
    d = \frac{1}{u} \approx 0.8909, \quad q = \frac{e^{0.05/3} - 0.8909}{1.1224 - 0.8909} = \frac{1.0168 - 0.8909}{0.2315} \approx 0.5439
    $$

    **Stock price tree** (node $(n,j)$ means step $n$, $j$ up-moves):

    | Step | $j=0$ | $j=1$ | $j=2$ | $j=3$ |
    |---|---|---|---|---|
    | $n=0$ | $100.00$ | | | |
    | $n=1$ | $89.09$ | $112.24$ | | |
    | $n=2$ | $79.38$ | $100.00$ | $126.00$ | |
    | $n=3$ | $70.72$ | $89.09$ | $112.24$ | $141.40$ |

    **Barrier check** ($H = 90$): Node $(1,0) = 89.09 \leq 90$ — breached. Node $(2,0) = 79.38 \leq 90$ — breached. All nodes with $j = 0$ for $n \geq 1$ are at or below the barrier.

    **Terminal payoffs** ($n = 3$):

    - $(3,0)$: $S = 70.72 \leq H \Rightarrow V = 0$
    - $(3,1)$: $S = 89.09 \leq H \Rightarrow V = 0$
    - $(3,2)$: $S = 112.24 > H \Rightarrow V = \max(112.24 - 100, 0) = 12.24$
    - $(3,3)$: $S = 141.40 > H \Rightarrow V = \max(141.40 - 100, 0) = 41.40$

    **Backward induction** ($n = 2$):

    - $(2,0)$: $S = 79.38 \leq H \Rightarrow V = 0$
    - $(2,1)$: $S = 100 > H \Rightarrow V = e^{-0.05/3}[0.5439 \times 12.24 + 0.4561 \times 0] = 0.9835 \times 6.66 \approx 6.55$
    - $(2,2)$: $S = 126.00 > H \Rightarrow V = 0.9835[0.5439 \times 41.40 + 0.4561 \times 12.24] = 0.9835 \times 28.10 \approx 27.64$

    **Backward induction** ($n = 1$):

    - $(1,0)$: $S = 89.09 \leq H \Rightarrow V = 0$
    - $(1,1)$: $S = 112.24 > H \Rightarrow V = 0.9835[0.5439 \times 27.64 + 0.4561 \times 6.55] = 0.9835 \times 17.97 \approx 17.67$

    **Root** ($n = 0$): $S = 100 > H$

    $$
    V_{0,0} = 0.9835[0.5439 \times 17.67 + 0.4561 \times 0] = 0.9835 \times 9.61 \approx 9.45
    $$

    **Vanilla call** (same tree, no barrier): The terminal payoffs are $(0, 0, 12.24, 41.40)$. Backward induction without barrier enforcement at $(1,0)$ gives a nonzero continuation value. Following through:

    - $(2,0)$: $V = 0.9835[0.5439 \times 0 + 0.4561 \times 0] = 0$
    - $(2,1)$: $V = 6.55$ (same)
    - $(2,2)$: $V = 27.64$ (same)
    - $(1,0)$: $V = 0.9835[0.5439 \times 6.55 + 0.4561 \times 0] = 0.9835 \times 3.56 \approx 3.50$
    - $(1,1)$: $V = 17.67$ (same)
    - $(0,0)$: $V = 0.9835[0.5439 \times 17.67 + 0.4561 \times 3.50] = 0.9835 \times 11.21 \approx 11.02$

    **Comparison:** The barrier call ($\approx 9.45$) is cheaper than the vanilla call ($\approx 11.02$), as expected since the knock-out feature reduces value.

---


**Exercise 2.** Explain the "specification error" that causes oscillatory convergence when pricing barrier options on binomial trees. Specifically, for a barrier at $H = 90$ and a CRR tree with $u = e^{\sigma\sqrt{\Delta t}}$, show that $H$ generally does not coincide with any node $S_0 u^j d^{n-j}$. Describe the adaptive mesh refinement technique that mitigates this problem.

??? success "Solution to Exercise 2"
    **Specification error.** In a CRR tree, the stock at node $(n,j)$ takes the value $S_{n,j} = S_0 u^j d^{n-j} = S_0 u^{2j-n}$. For the barrier $H$ to coincide with a node level, we need:

    $$
    H = S_0 u^{2j - n} \quad \Longrightarrow \quad 2j - n = \frac{\ln(H/S_0)}{\sigma\sqrt{\Delta t}}
    $$

    Since $2j - n$ must be an integer but $\frac{\ln(H/S_0)}{\sigma\sqrt{\Delta t}}$ is generally irrational, exact alignment occurs only for special values of $N$.

    For $H = 90$, $S_0 = 100$, $\sigma = 0.20$: we need $\frac{\ln(0.9)}{0.20\sqrt{T/N}} = \frac{-0.10536}{0.20\sqrt{T/N}}$ to be an integer. For $T = 1$, this becomes $\frac{-0.5268}{\sqrt{1/N}}$, which is an integer only for specific values of $N$.

    **Consequence:** When $H$ falls between two adjacent node levels $S_0 u^k$ and $S_0 u^{k-2}$ (for the relevant time step), the tree effectively applies a barrier that oscillates between these two levels as $N$ changes. This causes the computed option price to oscillate rather than converge monotonically.

    **Adaptive mesh refinement.** The idea is to place a finer sub-grid of nodes in a strip around the barrier $H$:

    1. Build the standard CRR tree away from the barrier
    2. Near the barrier, insert additional nodes so that at least one node level coincides with $H$
    3. Use interpolation to connect the fine mesh near $H$ with the coarse mesh elsewhere
    4. Perform backward induction on the combined mesh

    This ensures the barrier is represented exactly at every time step, eliminating the oscillation while keeping computational cost manageable (since the refinement is local).

---


**Exercise 3.** For an Asian option on a 3-step binomial tree, enumerate all possible paths and their corresponding arithmetic averages. Verify that the number of distinct averages is $2^3 = 8$ (one per path), and explain why this exponential growth makes exact tree pricing of Asian options impractical for large $N$.

??? success "Solution to Exercise 3"
    **Path enumeration for a 3-step tree.** At each step the stock moves up ($u$) or down ($d$), giving $2^3 = 8$ paths:

    | Path | Prices visited | Arithmetic average |
    |---|---|---|
    | UUU | $S_0,\, S_0 u,\, S_0 u^2,\, S_0 u^3$ | $\frac{S_0(1 + u + u^2 + u^3)}{4}$ |
    | UUD | $S_0,\, S_0 u,\, S_0 u^2,\, S_0 u$ | $\frac{S_0(1 + u + u^2 + u)}{4}$ |
    | UDU | $S_0,\, S_0 u,\, S_0,\, S_0 u$ | $\frac{S_0(1 + u + 1 + u)}{4}$ |
    | UDD | $S_0,\, S_0 u,\, S_0,\, S_0 d$ | $\frac{S_0(1 + u + 1 + d)}{4}$ |
    | DUU | $S_0,\, S_0 d,\, S_0,\, S_0 u$ | $\frac{S_0(1 + d + 1 + u)}{4}$ |
    | DUD | $S_0,\, S_0 d,\, S_0,\, S_0 d$ | $\frac{S_0(1 + d + 1 + d)}{4}$ |
    | DDU | $S_0,\, S_0 d,\, S_0 d^2,\, S_0 d$ | $\frac{S_0(1 + d + d^2 + d)}{4}$ |
    | DDD | $S_0,\, S_0 d,\, S_0 d^2,\, S_0 d^3$ | $\frac{S_0(1 + d + d^2 + d^3)}{4}$ |

    Note that paths UDD and DUU end at the same terminal node $(3,1)$ but have **different** averages: UDD has average $\frac{S_0(1 + u + 1 + d)}{4}$ while DUU has average $\frac{S_0(1 + d + 1 + u)}{4}$. These are actually equal, so some averages coincide. However, in general, the paths through a given node produce distinct averages.

    The total number of paths is $2^N = 8$. Each path has a potentially distinct average, so the state space for exact pricing is $O(2^N)$. For $N = 100$, this gives $2^{100} \approx 10^{30}$ states, making exact enumeration completely intractable.

    **This exponential growth** is the fundamental reason tree-based methods require approximations (like Hull–White interpolation) for Asian options, while Monte Carlo handles them naturally.

---


**Exercise 4.** The Hull-White approximation for Asian options on trees uses interpolation between representative average values at each node. Describe the algorithm: (a) How are the representative average values chosen at each node? (b) How is backward induction performed with interpolation? (c) What is the computational complexity as a function of $N$ and the number of average grid points $M$?

??? success "Solution to Exercise 4"
    **(a) Choosing representative average values.** At each node $(n, j)$, the possible running averages span a range from the minimum average (all down-moves first, then up-moves) to the maximum average (all up-moves first, then down-moves). Hull and White select $M$ equally spaced representative values $\bar{S}_1, \bar{S}_2, \ldots, \bar{S}_M$ spanning this range at each node.

    Specifically, for node $(n, j)$, define:

    $$
    \bar{S}_{\min}(n,j) = \text{average along path with maximum down-moves first}
    $$

    $$
    \bar{S}_{\max}(n,j) = \text{average along path with maximum up-moves first}
    $$

    The $M$ grid points are spaced uniformly between these extremes.

    **(b) Backward induction with interpolation.** At each node $(n, j)$ with representative average $\bar{S}_m$, the continuation value requires knowing the option value at $(n+1, j+1)$ and $(n+1, j)$ for the **updated** averages:

    $$
    \bar{S}^{\text{up}} = \frac{(n+1)\bar{S}_m + S_{n+1,j+1}}{n+2}, \quad \bar{S}^{\text{down}} = \frac{(n+1)\bar{S}_m + S_{n+1,j}}{n+2}
    $$

    These updated averages generally do not coincide with any grid point at the successor nodes. The option values are obtained by **linear interpolation** between the two nearest grid points.

    The backward induction formula is:

    $$
    V(n, j, \bar{S}_m) = e^{-r\Delta t}\bigl[q\, \hat{V}(n+1, j+1, \bar{S}^{\text{up}}) + (1-q)\, \hat{V}(n+1, j, \bar{S}^{\text{down}})\bigr]
    $$

    where $\hat{V}$ denotes the interpolated value.

    **(c) Computational complexity.** At each time step $n$, there are $n + 1$ spatial nodes. At each node, there are $M$ representative averages. So the total number of states is:

    $$
    \sum_{n=0}^{N} (n+1) \cdot M = M \cdot \frac{(N+1)(N+2)}{2} = O(N^2 M)
    $$

    Each state requires $O(1)$ work (one interpolation and one discounting step). Hence the total complexity is $O(N^2 M)$, which is polynomial in $N$ — a dramatic improvement over the $O(2^N)$ exact method.

---


**Exercise 5.** For a lookback option on a binomial tree, the state at each node is $(S_{n,j}, S_{\max})$. At node $(n, j)$ with $j$ up-moves out of $n$ steps, how many distinct values of $S_{\max}$ are possible? Derive the bound and explain why lookback options have $O(N^3)$ complexity on trees, compared to $O(N^2)$ for barrier options.

??? success "Solution to Exercise 5"
    **Distinct running maxima at node $(n, j)$.** At node $(n, j)$, the stock price is $S_{n,j} = S_0 u^j d^{n-j}$. The running maximum $S_{\max}$ depends on the highest stock price visited along the path to this node.

    The stock prices visited along any path are of the form $S_0 u^{j'} d^{n'-j'}$ for the intermediate nodes. The maximum is achieved at the node with the highest power of $u$ (equivalently, the most up-moves relative to time). Along a path to $(n, j)$, if the maximum number of up-moves reached at any intermediate step $n'$ is $j^* \in \{j, j+1, \ldots, \min(n, j + (n-j))\}$... more precisely, the key observation is:

    The running maximum is $S_0 u^{j^*}$ for some $j^* \geq j$ (since the current up-count is $j$ and the maximum up-count along the path must be at least $j$). Furthermore, $j^*$ can range from $j$ to $\min(n, j + (n-j)) = n$... but more carefully, $j^*$ is bounded by the maximum "height" the path reached, which ranges from $j$ up to some maximum determined by the path.

    The running max is $S_{\max} = S_0 u^{k}$ where $k$ is the maximum net up-count along the path. Since the path ends with $j$ up-moves out of $n$, and the stock price at step $n'$ having $j'$ up-moves is $S_0 u^{2j' - n'}$, the maximum is determined by $\max_{n' \leq n} (2j'_{n'} - n')$.

    At node $(n, j)$, the running maximum can take values $S_0 u^m$ for $m = j, j+1, \ldots, n$ — but not all are achievable. The number of distinct achievable maxima at node $(n,j)$ is bounded by $j + 1$, because the peak height above the starting point ranges from $0$ to $j$ additional up-moves beyond the minimum needed.

    **Total state count:**

    $$
    \sum_{n=0}^{N} \sum_{j=0}^{n} (j+1) = \sum_{n=0}^{N} \frac{(n+1)(n+2)}{2} = O(N^3)
    $$

    **Comparison with barrier options:** Barrier options have only a boolean state (breached or not) at each node, so the state space is simply the number of tree nodes: $\sum_{n=0}^{N}(n+1) = O(N^2)$. The extra factor of $O(N)$ for lookback options comes from tracking the running maximum, which can take $O(N)$ distinct values at nodes in the middle of the tree.

---


**Exercise 6.** Compare the binomial tree and Monte Carlo methods for pricing a down-and-out barrier call with $N = 200$ time steps and $10{,}000$ Monte Carlo paths. Which method gives a more accurate price? Discuss the trade-offs in terms of convergence behavior, computational cost, and ease of implementation for barrier options specifically.

??? success "Solution to Exercise 6"
    **Binomial tree with $N = 200$:**

    - Complexity: $O(N^2) = O(40{,}000)$ operations — very fast
    - **Advantage:** Deterministic, no sampling noise
    - **Disadvantage:** Subject to specification error (oscillatory convergence) unless the barrier aligns with node levels. For $N = 200$, the barrier may or may not align, so the price could be significantly biased
    - Accuracy: Typically within 1–5% of the continuous-barrier analytical price, but the error is oscillatory and non-monotone

    **Monte Carlo with $10{,}000$ paths and $N = 200$ time steps:**

    - Complexity: $O(N \times \text{paths}) = O(2 \times 10^6)$ operations — slower
    - **Advantage:** No specification error in the barrier check (barrier is checked at each simulated time point)
    - **Disadvantage:** Statistical noise with standard error $O(1/\sqrt{10{,}000}) = O(1\%)$; also suffers from discrete monitoring bias (the continuous path may cross the barrier between monitored points)

    **Which is more accurate?** For barrier options specifically, the binomial tree is often **less accurate** due to the specification error, unless $N$ is chosen to align with the barrier. Monte Carlo with a Brownian bridge correction for continuous monitoring can be more reliable, though it requires more computation.

    **Trade-offs summary:**

    | Criterion | Binomial Tree | Monte Carlo |
    |---|---|---|
    | Speed | Fast ($O(N^2)$) | Slower ($O(N \times \text{paths})$) |
    | Convergence | Oscillatory (barrier misalignment) | Smooth ($O(1/\sqrt{N_{\text{paths}}})$) |
    | Bias | Specification error | Discrete monitoring bias |
    | Confidence interval | Not directly available | Naturally produced |
    | Implementation | Simple | Simple |
    | Best use case | When $N$ chosen to align barrier | When combined with variance reduction |

    For practical barrier option pricing, neither method alone is ideal. The binomial tree with adaptive mesh refinement or barrier-aligned $N$, or Monte Carlo with Brownian bridge correction, provides the best accuracy.
