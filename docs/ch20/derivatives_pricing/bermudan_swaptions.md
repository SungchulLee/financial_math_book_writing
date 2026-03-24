# Bermudan Swaptions

A Bermudan swaption grants the holder the right to enter into an interest rate swap at any one of several predetermined exercise dates, combining features of European options (single exercise) and American options (continuous exercise). Since the exercise decision depends on comparing the immediate swap value against the expected value of waiting, Bermudan swaptions cannot be priced in closed form and require numerical methods. This section presents the two main approaches: backward induction on a trinomial tree and Monte Carlo with Longstaff-Schwartz regression.

## Bermudan Swaption Payoff

Consider a Bermudan payer swaption with exercise dates $\mathcal{T} = \{T_m, T_{m+1}, \ldots, T_{n-1}\}$ and an underlying swap with payment dates $T_{m+1}, \ldots, T_n$, fixed rate $K$, and notional $N$. If the holder exercises at date $T_j \in \mathcal{T}$, they enter a swap with remaining payments at $T_{j+1}, \ldots, T_n$, receiving the exercise value

$$
E(T_j) = N\!\left(1 - \sum_{k=j+1}^{n} c_k\,P(T_j, T_k)\right)
$$

where $c_k = K\tau_k$ for $k < n$ and $c_n = K\tau_n + 1$, exactly as in the European swaption payoff.

!!! info "Definition: Bermudan Swaption Value"
    The Bermudan swaption value at time $t_0$ is

    $$
    V^{\text{Berm}}(t_0) = \sup_{\tau \in \mathcal{T}} \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(\tau)}\,E(\tau)^+\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    where the supremum is over all stopping times $\tau$ taking values in $\mathcal{T}$.

The Bermudan value always satisfies

$$
V^{\text{European}} \le V^{\text{Bermudan}} \le V^{\text{American}}
$$

The difference $V^{\text{Berm}} - V^{\text{European}}$ is the early exercise premium.

## Pricing on a Hull-White Trinomial Tree

The Hull-White trinomial tree provides a natural framework for Bermudan pricing via backward induction. The tree discretizes the short rate process and allows exact computation of continuation values at each node.

### Backward Induction Algorithm

At each node $(i, j)$ at time step $i$ with short rate state $j$, define:

- **Exercise value**: $E_{ij}$ = value of entering the swap immediately
- **Continuation value**: $C_{ij}$ = discounted expected value from holding

The Bermudan option value at each node is

$$
V_{ij} = \max\!\left(E_{ij},\; C_{ij}\right)
$$

!!! info "Algorithm: Tree-Based Bermudan Pricing"
    1. **Build the tree**: Construct the Hull-White trinomial tree calibrated to the market yield curve (see tree construction section).
    2. **Terminal values**: At each node at the final exercise date $T_{n-1}$, compute $V_{ij} = \max(E_{ij}, 0)$ where $E_{ij}$ is the swap value given $r_{ij}$.
    3. **Backward step**: For each time step from $T_{n-2}$ back to $T_m$:

        $$
        C_{ij} = e^{-r_{ij}\Delta t}\sum_{l} p_{ijl}\,V_{i+1,l}
        $$

        where $p_{ijl}$ are the branching probabilities to node $(i+1, l)$.

        If $T_i \in \mathcal{T}$ (exercise date):

        $$
        V_{ij} = \max(E_{ij},\; C_{ij})
        $$

        Otherwise: $V_{ij} = C_{ij}$.

    4. **Root value**: $V^{\text{Berm}}(t_0) = V_{0,0}$ at the root node.

### Computing the Exercise Value

At node $(i,j)$ corresponding to time $T_i$ and short rate $r_{ij}$, the exercise value is

$$
E_{ij} = N\!\left(1 - \sum_{k=i+1}^{n} c_k\,P(T_i, T_k; r_{ij})\right)
$$

where each $P(T_i, T_k; r_{ij}) = A(T_i, T_k)\,e^{-B(T_i, T_k)\,r_{ij}}$ uses the Hull-White analytic bond price formula. This avoids the need to roll ZCB prices through the tree for each payment date.

## Exercise Boundary

The exercise boundary is the set of critical short rates $\{r^*(T_j)\}_{j=m}^{n-1}$ at each exercise date where the holder is indifferent between exercising and continuing:

$$
E(T_j, r^*(T_j)) = C(T_j, r^*(T_j))
$$

For a payer swaption, the holder exercises when $r(T_j) < r^*(T_j)$ (low rates make the existing swap valuable). The exercise boundary is not flat: it typically slopes upward as the remaining swap tenor decreases, because shorter swaps require lower rates to be worth exercising.

!!! tip "Interpreting the Exercise Boundary"
    The exercise boundary captures the trade-off between the intrinsic value of exercising now (entering a favorable swap) and the time value of waiting for a potentially better opportunity. Near the final exercise date, the boundary approaches the European optimal exercise rate because there is little optionality left.

## Monte Carlo with Longstaff-Schwartz

For more complex variants (path-dependent features, multiple factors), the Longstaff-Schwartz (2001) least-squares Monte Carlo (LSMC) algorithm provides an alternative to tree-based pricing.

### Algorithm Overview

!!! info "Algorithm: Longstaff-Schwartz for Bermudan Swaptions"
    1. **Simulate paths**: Generate $M$ paths of the short rate $\{r^{(m)}(t)\}$ using exact simulation.
    2. **Terminal payoffs**: At the last exercise date $T_{n-1}$, compute $V^{(m)} = \max(E^{(m)}(T_{n-1}), 0)$ for each path.
    3. **Backward regression**: For each exercise date $T_j$ from $T_{n-2}$ back to $T_m$:
        - Compute the exercise value $E^{(m)}(T_j)$ on each path.
        - Discount future values: $Y^{(m)} = e^{-r^{(m)}(T_j)\Delta t}\,V^{(m)}$ (continuation value estimate).
        - **Regression**: Fit $Y^{(m)} \approx \beta_0 + \beta_1 r^{(m)}(T_j) + \beta_2 [r^{(m)}(T_j)]^2 + \cdots$ using least squares on in-the-money paths.
        - **Exercise decision**: On each path, exercise if $E^{(m)}(T_j) > \hat{C}^{(m)}(T_j)$ where $\hat{C}$ is the regression estimate.
    4. **Price**: Average the discounted payoffs over all paths.

### Regression Basis Functions

Common choices for basis functions in the Hull-White setting include:

- **Polynomial in $r$**: $\{1, r, r^2, r^3\}$ -- simple and effective for single-factor models.
- **Bond prices**: $\{1, P(T_j, T_n), P(T_j, T_n)^2\}$ -- more financially motivated.
- **Swap value**: $\{1, E(T_j), E(T_j)^2\}$ -- directly related to the exercise decision.

!!! warning "Bias Considerations"
    The Longstaff-Schwartz algorithm produces a **low-biased** estimate because the estimated continuation values are noisier than the true values, leading to suboptimal exercise decisions. To obtain an upper bound, the Andersen-Broadie dual method can be used, providing a confidence interval for the true Bermudan price.

## Comparison of Methods

| Method | Advantages | Limitations |
|:---|:---|:---|
| Trinomial tree | Exact backward induction; fast for 1-factor | Curse of dimensionality for multi-factor |
| Longstaff-Schwartz MC | Handles multi-factor and path-dependence | Low-biased; regression quality affects accuracy |
| PDE (finite difference) | Handles 1-2 factors; sharp exercise boundary | Difficult beyond 2 factors |

For the one-factor Hull-White model, the trinomial tree is typically the most efficient method. Longstaff-Schwartz becomes essential when extending to two-factor Hull-White or when incorporating path-dependent features such as callable ranges.

## Numerical Example

Consider a Bermudan payer swaption with exercise dates at years 1 through 9 (annually) on a 10-year swap with fixed rate $K = 0.04$, notional $N = \$1{,}000{,}000$, and Hull-White parameters $\lambda = 0.05$, $\sigma = 0.01$.

**Tree-based pricing**:

```python
def price_bermudan_swaption_tree(hw, N, K, exercise_dates, T_payments, n_steps=500):
    """Price a Bermudan payer swaption on a Hull-White trinomial tree."""
    tree = hw.build_trinomial_tree(T=T_payments[-1], n_steps=n_steps)

    # Initialize terminal values to zero
    V = np.zeros(tree.n_nodes[-1])

    # Backward induction
    for i in range(n_steps - 1, -1, -1):
        t_i = tree.times[i]
        for j in range(tree.n_nodes[i]):
            r_ij = tree.rates[i][j]

            # Continuation value
            C = tree.discount(i, j) * tree.expected_value(i, j, V)

            # Check if this is an exercise date
            if t_i in exercise_dates:
                E = compute_swap_value(hw, N, K, t_i, T_payments, r_ij)
                V_new[j] = max(E, C)
            else:
                V_new[j] = C

        V = V_new

    return V[0]
```

A typical result: the Bermudan swaption is priced at a premium of 5-15% above the corresponding European swaption, with the early exercise premium increasing with volatility and maturity.

## Exercise Strategy Visualization

The exercise boundary $r^*(T_j)$ as a function of the exercise date provides insight into optimal behavior:

- **Early dates** ($T_j$ near $T_m$): $r^*(T_j)$ is low because the holder needs rates to be substantially below the strike to justify forgoing future optionality.
- **Late dates** ($T_j$ near $T_{n-1}$): $r^*(T_j)$ approaches the European threshold because little optionality remains.
- **Shape**: The boundary typically has an upward slope, reflecting the decreasing value of waiting.

---

## Summary

Bermudan swaptions require numerical methods because the early exercise decision at each date depends on the continuation value. The Hull-White trinomial tree enables exact backward induction with the Bellman equation $V = \max(E, C)$ at each exercise node. For multi-factor extensions, the Longstaff-Schwartz Monte Carlo algorithm provides a flexible alternative using least-squares regression to estimate continuation values. The exercise boundary $r^*(T_j)$ characterizes the optimal exercise strategy and slopes upward as the remaining tenor decreases.

---

## Exercises

**Exercise 1.** Explain the inequality $V^{\text{European}} \le V^{\text{Bermudan}} \le V^{\text{American}}$. Why is the Bermudan value always at least as large as the European value? Under what conditions would the Bermudan and European values be equal?

---

**Exercise 2.** In the backward induction algorithm, the Bellman equation is $V_{ij} = \max(E_{ij}, C_{ij})$. Describe what happens at nodes where $T_i \notin \mathcal{T}$ (not an exercise date). Why is the continuation value the only relevant quantity at such nodes?

---

**Exercise 3.** The exercise boundary $r^*(T_j)$ slopes upward as $T_j$ approaches the final exercise date. Explain this behavior intuitively: why does the holder require a lower rate to exercise early versus late?

---

**Exercise 4.** In the Longstaff-Schwartz algorithm, the regression is performed only on in-the-money paths. Explain why this restriction improves the accuracy of the continuation value estimate near the exercise boundary.

---

**Exercise 5.** Compare the trinomial tree and Longstaff-Schwartz approaches for pricing a Bermudan swaption in the one-factor Hull-White model. Which method is more efficient, and why? Under what circumstances would you prefer the Monte Carlo approach?

---

**Exercise 6.** The Longstaff-Schwartz algorithm produces a low-biased estimate. Explain the source of this bias and describe how the Andersen-Broadie dual method provides an upper bound, yielding a confidence interval for the true price.

---

**Exercise 7.** For a 10-year Bermudan payer swaption with annual exercise rights and $K = 0.04$, describe qualitatively how the early exercise premium $V^{\text{Berm}} - V^{\text{European}}$ depends on the volatility parameter $\sigma$ and the mean reversion speed $\lambda$.
