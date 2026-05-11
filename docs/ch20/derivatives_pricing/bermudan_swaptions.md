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

??? success "Solution to Exercise 1"
    The inequality $V^{\text{European}} \le V^{\text{Bermudan}} \le V^{\text{American}}$ follows from the nesting of exercise opportunities:

    - **$V^{\text{European}} \le V^{\text{Bermudan}}$:** The European swaption can only be exercised at a single date $T_m$. The Bermudan swaption can be exercised at $T_m$ and at additional dates $T_{m+1}, \ldots, T_{n-1}$. Since the Bermudan holder has strictly more exercise opportunities, they can always replicate the European strategy (exercise only at $T_m$) and potentially do better. Therefore the Bermudan value is at least as large.

    - **$V^{\text{Bermudan}} \le V^{\text{American}}$:** The American swaption can be exercised at any time in $[T_m, T_{n-1}]$, while the Bermudan is restricted to the discrete set $\mathcal{T}$. The American holder has more flexibility, so $V^{\text{American}} \ge V^{\text{Bermudan}}$.

    **When are Bermudan and European values equal?** This happens when early exercise is never optimal, i.e., the early exercise premium is zero. This occurs when:

    - The swaption is deep out-of-the-money, so the probability of profitable exercise at any date is negligible.
    - The time value of the option always exceeds the intrinsic value at the intermediate exercise dates, meaning it is always better to wait. In practice, for at-the-money or in-the-money payer swaptions in a low-rate environment, the early exercise premium is positive and the two values differ.

---

**Exercise 2.** In the backward induction algorithm, the Bellman equation is $V_{ij} = \max(E_{ij}, C_{ij})$. Describe what happens at nodes where $T_i \notin \mathcal{T}$ (not an exercise date). Why is the continuation value the only relevant quantity at such nodes?

??? success "Solution to Exercise 2"
    At nodes where $T_i \notin \mathcal{T}$ (not an exercise date), the holder cannot exercise the option. The only possibility is to continue holding, so:

    $$
    V_{ij} = C_{ij} = e^{-r_{ij}\Delta t}\sum_{l} p_{ijl}\,V_{i+1,l}
    $$

    The exercise value $E_{ij}$ is irrelevant at these nodes because the contract does not permit exercise. The option value is determined entirely by discounting the expected future option values back one time step.

    This is analogous to non-dividend dates for American equity options: between exercise opportunities, the option behaves as a European option over that interval, and its value is simply the continuation (hold) value. The Bellman equation $V = \max(E, C)$ only applies at exercise dates; at all other nodes, it reduces to $V = C$.

---

**Exercise 3.** The exercise boundary $r^*(T_j)$ slopes upward as $T_j$ approaches the final exercise date. Explain this behavior intuitively: why does the holder require a lower rate to exercise early versus late?

??? success "Solution to Exercise 3"
    The exercise boundary $r^*(T_j)$ slopes upward as $T_j$ approaches the final exercise date for the following reasons:

    **Early exercise dates ($T_j$ near $T_m$):** At early dates, the remaining swap has a long tenor, and there are many future exercise dates remaining. The holder requires rates to be substantially below the strike $K$ to justify exercising because:

    1. The time value of the remaining optionality is high (many future exercise opportunities).
    2. Exercising now forfeits the option to exercise later at a potentially better rate.
    3. Only very favorable current rates (very low $r$) make immediate exercise worthwhile.

    Hence $r^*(T_j)$ is low.

    **Late exercise dates ($T_j$ near $T_{n-1}$):** Near the final exercise date, the remaining swap is short and there are few (or no) future exercise opportunities. The time value of waiting is small because:

    1. Little optionality remains.
    2. The remaining swap tenor is short, so the exercise value is smaller in magnitude.
    3. The threshold approaches the European optimal exercise level.

    Hence $r^*(T_j)$ is higher -- the holder is willing to exercise at less favorable rates because waiting has little value.

    The upward slope reflects the decreasing value of the "option to wait" as the final exercise date approaches.

---

**Exercise 4.** In the Longstaff-Schwartz algorithm, the regression is performed only on in-the-money paths. Explain why this restriction improves the accuracy of the continuation value estimate near the exercise boundary.

??? success "Solution to Exercise 4"
    The regression in the Longstaff-Schwartz algorithm is performed only on in-the-money (ITM) paths because:

    1. **Relevance to the exercise decision:** The exercise decision only matters when the option is in the money ($E(T_j) > 0$). For out-of-the-money (OTM) paths, the holder will never exercise regardless of the continuation value, so these paths contribute no information about the exercise boundary.

    2. **Improved regression fit near the boundary:** The exercise boundary lies in the region where the option transitions from ITM to OTM. By restricting the regression to ITM paths, the polynomial fit concentrates on the region where the exercise decision is actually made. Including OTM paths would add data points where $E = 0$ regardless of the continuation value, diluting the regression's accuracy in the critical near-boundary region.

    3. **Numerical stability:** OTM paths have $E = 0$ but potentially large continuation values. Including them would bias the regression toward fitting the relationship between state variables and continuation values in a region where the exercise decision is trivially "hold," wasting degrees of freedom.

    4. **Theoretical justification:** Longstaff and Schwartz show that the optimal stopping rule depends only on the conditional expectation of the continuation value on the set where exercise is feasible. The regression needs to approximate $\mathbb{E}[C \,|\, r, E > 0]$, not $\mathbb{E}[C \,|\, r]$.

---

**Exercise 5.** Compare the trinomial tree and Longstaff-Schwartz approaches for pricing a Bermudan swaption in the one-factor Hull-White model. Which method is more efficient, and why? Under what circumstances would you prefer the Monte Carlo approach?

??? success "Solution to Exercise 5"
    **Trinomial tree:**

    - *Advantages:* Exact backward induction gives the precise Bermudan price (up to discretization). The exercise boundary is computed explicitly at each node. The algorithm is deterministic with no sampling noise. For the one-factor Hull-White model, trees with 500-1000 steps run in under a second.
    - *Limitations:* The tree size grows exponentially with the number of factors. For two-factor models, a two-dimensional tree or lattice is needed, which is feasible but significantly more expensive.

    **Longstaff-Schwartz Monte Carlo:**

    - *Advantages:* Easily extends to multi-factor models (two-factor Hull-White, stochastic volatility). Can handle path-dependent features. Flexible choice of basis functions.
    - *Limitations:* Produces a low-biased estimate. Requires a large number of paths (e.g., 50,000-100,000) for accurate results. The regression quality affects the exercise decision accuracy. Statistical noise requires variance reduction techniques.

    **For one-factor Hull-White:** The trinomial tree is more efficient. It produces exact prices (up to time discretization) without sampling noise, and runs much faster.

    **When to prefer Monte Carlo:** Use Longstaff-Schwartz when:

    - The model has two or more factors (e.g., two-factor Hull-White for better yield curve dynamics).
    - Path-dependent features are present (e.g., callable range accruals).
    - The model is non-Markovian or does not admit a recombining tree.

---

**Exercise 6.** The Longstaff-Schwartz algorithm produces a low-biased estimate. Explain the source of this bias and describe how the Andersen-Broadie dual method provides an upper bound, yielding a confidence interval for the true price.

??? success "Solution to Exercise 6"
    **Source of low bias:** The Longstaff-Schwartz algorithm estimates the continuation value $C(T_j)$ via a least-squares regression. The estimated continuation value $\hat{C}(T_j)$ differs from the true value $C(T_j)$ by a regression error:

    $$
    \hat{C}(T_j) = C(T_j) + \epsilon(T_j)
    $$

    The exercise rule is: exercise if $E(T_j) > \hat{C}(T_j)$. Due to the noise $\epsilon$:

    - When $\hat{C}$ is too low (underestimated), the algorithm exercises too early, accepting a suboptimal exercise value.
    - When $\hat{C}$ is too high (overestimated), the algorithm delays exercise, missing a good exercise opportunity.

    Both types of errors lead to suboptimal exercise decisions, and the resulting average payoff is lower than the true optimally-exercised value. Hence the estimate is low-biased.

    **Andersen-Broadie dual method:** The dual approach provides an upper bound based on the identity:

    $$
    V^{\text{Berm}}(t_0) = \inf_{\{M_j\}} \mathbb{E}\!\left[\max_{T_j \in \mathcal{T}} \left(\frac{E(T_j)}{B(T_j)} - M_j\right)\right] + M_0
    $$

    where the infimum is over martingales $\{M_j\}$ and $B(T_j)$ is the discount factor. By choosing a specific martingale (constructed from the exercise policy estimated by Longstaff-Schwartz), one obtains an upper bound that can be computed via Monte Carlo. The true price lies between the Longstaff-Schwartz lower bound and the Andersen-Broadie upper bound, giving a confidence interval.

---

**Exercise 7.** For a 10-year Bermudan payer swaption with annual exercise rights and $K = 0.04$, describe qualitatively how the early exercise premium $V^{\text{Berm}} - V^{\text{European}}$ depends on the volatility parameter $\sigma$ and the mean reversion speed $\lambda$.

??? success "Solution to Exercise 7"
    **Dependence on $\sigma$ (volatility):**

    - Increasing $\sigma$ raises both the European swaption value and the Bermudan value.
    - The early exercise premium $V^{\text{Berm}} - V^{\text{European}}$ generally increases with $\sigma$. Higher volatility means the short rate visits a wider range of values, creating more situations where early exercise is optimal. With higher $\sigma$, there are more paths where rates drop significantly below $K$ at intermediate dates, making early exercise valuable.
    - However, higher volatility also increases the time value of waiting. The net effect is that the premium increases, but at a slower rate than the option values themselves.

    **Dependence on $\lambda$ (mean reversion):**

    - Higher $\lambda$ reduces the effective volatility of rates at longer horizons through mean reversion. This reduces both European and Bermudan values.
    - The early exercise premium tends to increase with $\lambda$ relative to the European value. With strong mean reversion, a favorable rate observed today is likely to revert toward the long-run mean, so it is better to exercise now rather than wait (since waiting means the favorable rate will likely disappear). This makes early exercise more attractive.
    - Conversely, with low $\lambda$, favorable rates persist, reducing the urgency to exercise early.

    In summary: higher $\sigma$ increases the absolute early exercise premium, and higher $\lambda$ increases the relative importance of early exercise (the premium as a fraction of the European value).
