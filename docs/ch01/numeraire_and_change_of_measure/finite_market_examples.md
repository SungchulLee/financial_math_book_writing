# Finite Market Examples


Recall (see [§ FTAP](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md)): in a one-period finite market with payoff matrix $X_{ij} = S^j_1(\omega_i) - S^j_0$ (excess returns relative to a unit numéraire $S^0_0 = S^0_1 = 1$), no arbitrage is equivalent to existence of $q \in \mathbb{R}^n_{>0}$ with $\sum_i q_i = 1$ and $X^T q = 0$; the EMM is unique iff the market is complete.

Recall (see [§ State Prices & Arrow–Debreu](../discrete_time_foundations/state_prices_arrow_debreu.md)): when $S^0_0 = S^0_1 = 1$, state prices $\psi_i$ coincide with risk-neutral probabilities $q_i$.

The four worked examples below — complete two-state, incomplete three-state, complete three-state via a second asset, and an arbitrage example — are developed in detail across the [FTAP](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md) and [Complete Markets](../fundamental_theorem_of_asset_pricing/complete_markets_and_uniqueness.md) pages. This page reuses those structural facts to make a different point: **the choice of numéraire is itself a degree of freedom, and pricing is invariant under it**. The exercises below carry out the verification numerically.


## What is Specific to the Numéraire Viewpoint

In a one-period finite market, picking the numéraire amounts to choosing a strictly positive coordinate $N_0, N_1(\omega_i) > 0$ along which to express ratios. Two facts make this concrete:

- The EMM $\mathbb{Q}^N$ associated with $N$ is determined by the requirement that **all** ratios $S^j_t / N_t$ are martingales: $\sum_i q^N_i\, S^j_1(\omega_i)/N_1(\omega_i) = S^j_0/N_0$ for every traded asset $j$.

- The Radon–Nikodym derivative between two numéraires $N, M$ is finite-dimensional and concrete:

$$
\frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}(\omega_i) = \frac{M_1(\omega_i)/M_0}{N_1(\omega_i)/N_0}, \qquad q^M_i = q^N_i \cdot \frac{M_1(\omega_i)/M_0}{N_1(\omega_i)/N_0}
$$

These two ingredients suffice to translate any pricing problem between numéraires by direct arithmetic — there is no Girsanov machinery at this level.


## Example 1: Two-State Market — Money-Market vs Stock Numéraire

Let $\Omega = \{\omega_1, \omega_2\}$, bond $B_0 = 1$, $B_1 = 1.05$, stock $S_0 = 100$, $S_1 = (120, 90)$.

**Money-market numéraire $N = B$.** The martingale condition $\mathbb{E}^{\mathbb{Q}^B}[S_1/B_1] = S_0/B_0$ gives

$$
q^B_1 \cdot \frac{120}{1.05} + (1-q^B_1)\cdot\frac{90}{1.05} = 100 \;\;\Longrightarrow\;\; q^B_1 = \tfrac{1}{2}, \quad \mathbb{Q}^B = (\tfrac{1}{2},\, \tfrac{1}{2})
$$

**Stock numéraire $N = S$.** Requiring $B_1/S_1$ to be a $\mathbb{Q}^S$-martingale, $\mathbb{E}^{\mathbb{Q}^S}[B_1/S_1] = B_0/S_0 = 1/100$:

$$
q^S_1\cdot\frac{1.05}{120} + (1-q^S_1)\cdot\frac{1.05}{90} = \frac{1}{100} \;\;\Longrightarrow\;\; q^S_1 = \tfrac{4}{7}, \quad \mathbb{Q}^S = (\tfrac{4}{7},\, \tfrac{3}{7})
$$

**Radon–Nikodym check.** Using $q^S_i = q^B_i \cdot (S_1(\omega_i)/S_0)/(B_1/B_0)$,

$$
q^S_1 = \tfrac{1}{2}\cdot\frac{120/100}{1.05} = \frac{60}{105} = \tfrac{4}{7}, \qquad q^S_2 = \tfrac{1}{2}\cdot\frac{90/100}{1.05} = \frac{45}{105} = \tfrac{3}{7}
$$

The two computations agree, and $q^S_1 + q^S_2 = 1$ is automatic from the $\mathbb{Q}^B$-martingale property of $S_t/B_t$.

**Pricing invariance.** For the call payoff $\Phi = (\max(S_1 - 100, 0)) = (20, 0)$:

- Under $\mathbb{Q}^B$: $\displaystyle V_0 = \frac{1}{B_1}\mathbb{E}^{\mathbb{Q}^B}[\Phi] = \frac{1}{1.05}\cdot\Big(\tfrac{1}{2}\cdot 20 + \tfrac{1}{2}\cdot 0\Big) = \frac{10}{1.05} = \frac{200}{21}$.
- Under $\mathbb{Q}^S$: $\displaystyle V_0 = S_0 \cdot \mathbb{E}^{\mathbb{Q}^S}\!\left[\frac{\Phi}{S_1}\right] = 100 \cdot\Big(\tfrac{4}{7}\cdot\tfrac{20}{120} + \tfrac{3}{7}\cdot 0\Big) = 100 \cdot \frac{4}{42} = \frac{200}{21}$.

Both numéraires give the identical no-arbitrage price $V_0 = 200/21 \approx 9.52$.


## Example 2: Incomplete Three-State Market — Numéraire Choice Does Not Restore Completeness

Recall (see [§ Complete Markets and Uniqueness](../fundamental_theorem_of_asset_pricing/complete_markets_and_uniqueness.md)): completeness requires $\operatorname{rank}(X) = n - 1$, depending only on the payoff space and not on the numéraire.

Take $\Omega = \{\omega_1,\omega_2,\omega_3\}$, $S^1_0 = 100$, $S^1_1 = (130, 100, 80)$, unit numéraire. The family of EMMs under the unit numéraire is

$$
\mathcal{Q}^{S^0} = \left\{(q_1,\, 1 - \tfrac{5}{2}q_1,\, \tfrac{3}{2}q_1) : 0 < q_1 < \tfrac{2}{5}\right\}
$$

Switching to $S^1$ as numéraire reparametrises this family — each $\mathbb{Q}^{S^0} \in \mathcal{Q}^{S^0}$ maps to a corresponding $\mathbb{Q}^{S^1} \in \mathcal{Q}^{S^1}$ via $L_i = (S^1_1(\omega_i)/S^1_0)/(S^0_1/S^0_0)$ — but the dimension of $\mathcal{Q}^{S^1}$ as a manifold is the same as that of $\mathcal{Q}^{S^0}$. **No numéraire change can complete an incomplete market**; only adding traded assets can.


## Example 3: Complete Three-State Market — Two Numéraires Give Identical Prices

With a second asset $S^2_0 = 50$, $S^2_1 = (40, 60, 45)$ added, the market becomes complete and the EMM under the unit numéraire is $\mathbb{Q}^{S^0} = (4/17,\, 7/17,\, 6/17)$.

Using $S^1$ as numéraire instead, the associated EMM weights become

$$
q^{S^1}_i \;\propto\; q^{S^0}_i \cdot \frac{S^1_1(\omega_i)/S^1_0}{S^0_1(\omega_i)/S^0_0}
$$

giving (after normalisation)

$$
\mathbb{Q}^{S^1} = \left(\frac{4 \cdot 130}{17 \cdot 100}\big/Z,\;\; \frac{7 \cdot 100}{17 \cdot 100}\big/Z,\;\; \frac{6 \cdot 80}{17 \cdot 100}\big/Z\right)
$$

with $Z = (520 + 700 + 480)/1700 = 1$, hence $\mathbb{Q}^{S^1} = (52/170,\, 70/170,\, 48/170)$. The digital option $\Phi = (1,0,0)$ is priced as

$$
V_0 = S^1_0 \cdot \mathbb{E}^{\mathbb{Q}^{S^1}}[\Phi/S^1_1] = 100 \cdot \frac{52}{170} \cdot \frac{1}{130} = \frac{52}{170 \cdot 1.3} = \frac{4}{17}
$$

matching the unit-numéraire price $\mathbb{E}^{\mathbb{Q}^{S^0}}[\Phi] = 4/17$. **This identity is the content of the change-of-numéraire theorem in a finite market.**


## Example 4: Arbitrage Is Numéraire-Invariant

Recall (see [§ FTAP](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md)): NA is equivalent to existence of *some* EMM relative to *some* numéraire. The contrapositive is sharper: if no EMM exists relative to numéraire $N$, then no EMM exists relative to any numéraire $M$, because $q^M_i = q^N_i \cdot L_i$ with $L_i > 0$. The set of measures admitting strictly positive density relative to $\mathbb{Q}^N$ is preserved by $L$; passing to a different numéraire only relabels the candidate EMMs. **Arbitrage cannot be hidden by a change of numéraire.**

For the arbitrage example with $S^1_0 = 100$, $S^1_1 = (110,105,95)$, $S^2_0 = 50$, $S^2_1 = (55,52,48)$ — analysed in [§ FTAP](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md) — the same arbitrage portfolio $\theta = (-2, 5)$ produces a non-negative payoff under any positive normalisation of state values.


## Summary

In finite markets the numéraire framework reduces to two arithmetic operations: (i) recompute the martingale condition $\sum_i q_i\, S^j_1(\omega_i)/N_1(\omega_i) = S^j_0/N_0$ for each new $N$, (ii) verify pricing invariance via the explicit Radon–Nikodym formula $q^M_i = q^N_i\,(M_1(\omega_i)/M_0)/(N_1(\omega_i)/N_0)$. The structural properties — no-arbitrage, completeness, attainability — are *numéraire-invariant*; only the numerical weights change.

---

## Exercises

**Exercise 1.** Consider a two-state market with one risky asset: $S^1_0 = 80$, $S^1_1(\omega_1) = 100$, $S^1_1(\omega_2) = 70$. Find the unique EMM and use it to price a European put option with strike $K = 85$.

??? success "Solution to Exercise 1"
    The payoff matrix is $2 \times 1$:

    $$
    X = \begin{pmatrix} 100 - 80 \\ 70 - 80 \end{pmatrix} = \begin{pmatrix} 20 \\ -10 \end{pmatrix}
    $$

    **Finding the EMM.** We need $q = (q_1, q_2)$ with $q_i > 0$, $q_1 + q_2 = 1$, and $X^T q = 0$:

    $$
    20q_1 - 10q_2 = 0 \implies 20q_1 = 10(1 - q_1) \implies 30q_1 = 10 \implies q_1 = \frac{1}{3}
    $$

    So $q_2 = 2/3$. The unique EMM is $\mathbb{Q} = (1/3, \, 2/3)$.

    **Verification:** $\mathbb{E}^{\mathbb{Q}}[S^1_1] = (1/3)(100) + (2/3)(70) = 100/3 + 140/3 = 240/3 = 80 = S^1_0$. The martingale condition holds.

    **Pricing the put option.** The put with strike $K = 85$ has payoff:

    $$
    \Phi(\omega_1) = \max(85 - 100, 0) = 0, \qquad \Phi(\omega_2) = \max(85 - 70, 0) = 15
    $$

    The no-arbitrage price is:

    $$
    V_0 = \mathbb{E}^{\mathbb{Q}}[\Phi] = \frac{1}{3} \cdot 0 + \frac{2}{3} \cdot 15 = 10
    $$

---

**Exercise 2.** In a three-state market with one risky asset, $S^1_0 = 50$, $S^1_1 = (70, 55, 35)$, parameterize the family of EMMs. Compute the no-arbitrage price interval for a butterfly spread with payoff $\Phi = (0, 10, 0)$. Is this claim attainable?

??? success "Solution to Exercise 2"
    The payoff matrix is $3 \times 1$:

    $$
    X = \begin{pmatrix} 70 - 50 \\ 55 - 50 \\ 35 - 50 \end{pmatrix} = \begin{pmatrix} 20 \\ 5 \\ -15 \end{pmatrix}
    $$

    **Parameterizing EMMs.** From $X^T q = 0$: $20q_1 + 5q_2 - 15q_3 = 0$, i.e., $4q_1 + q_2 - 3q_3 = 0$, giving $q_2 = 3q_3 - 4q_1$.

    From normalization: $q_1 + (3q_3 - 4q_1) + q_3 = 1$, so $-3q_1 + 4q_3 = 1$, giving $q_1 = (4q_3 - 1)/3$.

    For $q_1 > 0$: $q_3 > 1/4$. For $q_2 > 0$: $q_2 = 3q_3 - 4(4q_3 - 1)/3 = (9q_3 - 16q_3 + 4)/3 = (4 - 7q_3)/3 > 0$, so $q_3 < 4/7$.

    The family of EMMs is parameterized by $q_3 \in (1/4, \, 4/7)$:

    $$
    q_1 = \frac{4q_3 - 1}{3}, \quad q_2 = \frac{4 - 7q_3}{3}, \quad q_3 = q_3
    $$

    **Price interval for $\Phi = (0, 10, 0)$:**

    $$
    \mathbb{E}^{\mathbb{Q}}[\Phi] = 10q_2 = \frac{10(4 - 7q_3)}{3}
    $$

    As $q_3$ ranges over $(1/4, 4/7)$:

    - As $q_3 \to 1/4^+$: $\mathbb{E}^{\mathbb{Q}}[\Phi] \to 10(4 - 7/4)/3 = 10(9/4)/3 = 90/12 = 15/2 = 7.5$
    - As $q_3 \to (4/7)^-$: $\mathbb{E}^{\mathbb{Q}}[\Phi] \to 10(4 - 4)/3 = 0$

    The no-arbitrage price interval is $(0, \, 15/2)$.

    **Is $\Phi$ attainable?** We need $c$ and $\theta$ such that $c \cdot \mathbf{1} + X\theta = \Phi$: $c + 20\theta = 0$, $c + 5\theta = 10$, $c - 15\theta = 0$. From the first and third: $c + 20\theta = 0$ and $c - 15\theta = 0$, giving $35\theta = 0$, so $\theta = 0$ and $c = 0$. But then $c + 5\theta = 0 \neq 10$. The system is inconsistent, so $\Phi$ is **not attainable**.

---

**Exercise 3.** Consider a market with $n = 3$ states and $d = 2$ risky assets with payoff matrix

$$
X = \begin{pmatrix} 15 & 8 \\ -5 & 2 \\ -10 & -6 \end{pmatrix}
$$

Determine whether the market is arbitrage-free. If so, find the unique EMM and verify it satisfies the martingale condition for both assets.

??? success "Solution to Exercise 3"
    The payoff matrix is

    $$
    X = \begin{pmatrix} 15 & 8 \\ -5 & 2 \\ -10 & -6 \end{pmatrix}
    $$

    **Solving $X^T q = 0$ with $\sum q_i = 1$:**

    $$
    15q_1 - 5q_2 - 10q_3 = 0 \quad \Longrightarrow \quad 3q_1 - q_2 - 2q_3 = 0 \quad \text{...(i)}
    $$

    $$
    8q_1 + 2q_2 - 6q_3 = 0 \quad \Longrightarrow \quad 4q_1 + q_2 - 3q_3 = 0 \quad \text{...(ii)}
    $$

    Adding (i) and (ii): $7q_1 - 5q_3 = 0$, so $q_1 = 5q_3/7$.

    From (i): $q_2 = 3q_1 - 2q_3 = 15q_3/7 - 2q_3 = q_3/7$.

    Normalization: $5q_3/7 + q_3/7 + q_3 = (5 + 1 + 7)q_3/7 = 13q_3/7 = 1$, so $q_3 = 7/13$.

    Therefore: $q_1 = 5/13$, $q_2 = 1/13$, $q_3 = 7/13$.

    All components are strictly positive, so the market is **arbitrage-free**. The EMM is unique (two equations plus normalization fully determine three unknowns with $\operatorname{rank}(X) = 2 = n - 1$).

    **Verification of the martingale condition:**

    $$
    X^T q = \begin{pmatrix} 15 \cdot \frac{5}{13} - 5 \cdot \frac{1}{13} - 10 \cdot \frac{7}{13} \\ 8 \cdot \frac{5}{13} + 2 \cdot \frac{1}{13} - 6 \cdot \frac{7}{13} \end{pmatrix} = \begin{pmatrix} \frac{75 - 5 - 70}{13} \\ \frac{40 + 2 - 42}{13} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
    $$

    Both assets satisfy the martingale condition under $\mathbb{Q}$.

---

**Exercise 4.** A three-state market has one risky asset and $\operatorname{rank}(X) = 1$. A second risky asset is added with payoff vector $(a, b, c)^T$ and initial price $S^2_0$. What conditions on $(a, b, c)$ ensure that the augmented payoff matrix has rank 2? Under what additional condition on $S^2_0$ does the augmented market remain arbitrage-free?

??? success "Solution to Exercise 4"
    Let the original payoff matrix be $X_1 = (x_1, x_2, x_3)^T$ with $\operatorname{rank}(X_1) = 1$. The second asset's excess return column is $(a - S^2_0, \, b - S^2_0, \, c - S^2_0)^T$.

    The augmented matrix is

    $$
    X = \begin{pmatrix} x_1 & a - S^2_0 \\ x_2 & b - S^2_0 \\ x_3 & c - S^2_0 \end{pmatrix}
    $$

    **Rank 2 condition.** The augmented matrix has $\operatorname{rank}(X) = 2$ if and only if the second column $(a - S^2_0, \, b - S^2_0, \, c - S^2_0)^T$ is not a scalar multiple of the first column $(x_1, x_2, x_3)^T$. That is, there is no $\lambda \in \mathbb{R}$ such that

    $$
    a - S^2_0 = \lambda x_1, \quad b - S^2_0 = \lambda x_2, \quad c - S^2_0 = \lambda x_3
    $$

    Equivalently, the payoff vector $(a, b, c)^T$ should not be of the form $S^2_0 \cdot \mathbf{1} + \lambda (x_1, x_2, x_3)^T$ -- i.e., the second asset's payoff must not be replicable by a portfolio of the numéraire and the first asset.

    **Arbitrage-free condition.** Even with $\operatorname{rank}(X) = 2$, the market is arbitrage-free only if the system $X^T q = 0$, $\sum q_i = 1$ has a solution with all $q_i > 0$. This places a constraint on $S^2_0$: it must equal the risk-neutral expectation of the second asset's payoff under the unique EMM determined by the augmented system.

    Specifically, the unique EMM assigns probabilities $q_i$ determined by both columns of $X$. The value $S^2_0$ must satisfy

    $$
    S^2_0 = q_1 a + q_2 b + q_3 c
    $$

    where $(q_1, q_2, q_3)$ is the unique solution to the system. If $S^2_0$ is set to any other value, no strictly positive solution exists and the market admits arbitrage.

---

**Exercise 5.** In Example 4 of this section, the payoff matrix $X$ has rank 2 but the market admits arbitrage. Explain why high rank alone does not guarantee the absence of arbitrage. What specific property of the columns causes the EMM to require $q_1 = 0$?

??? success "Solution to Exercise 5"
    In Example 4, the payoff matrix has $\operatorname{rank}(X) = 2 = n - 1 = 2$, which is the rank condition for completeness. However, the market admits arbitrage because the system $X^T q = 0$ with $\sum q_i = 1$ and $q_i > 0$ has no solution -- it forces $q_1 = 0$.

    **Why high rank alone is insufficient:** The rank condition $\operatorname{rank}(X) = n - 1$ is necessary for completeness, but completeness also requires no-arbitrage as a prerequisite. The Second FTAP states: "In an **arbitrage-free** market, completeness $\iff$ unique EMM." If no EMM exists at all, the market has arbitrage and the question of completeness is moot.

    **What causes $q_1 = 0$:** The two columns of $X$ are

    $$
    X^{(1)} = (10, 5, -5)^T, \qquad X^{(2)} = (5, 2, -2)^T
    $$

    In states $\omega_2$ and $\omega_3$, the ratio $X^{(1)}_i / X^{(2)}_i$ is $5/2 = (-5)/(-2) = 2.5$ for both states. But in state $\omega_1$, the ratio is $10/5 = 2$. This means the linear combination $X^{(1)} - 2X^{(2)} = (0, 1, -1)^T$ is non-negative in states 2 and 3, while being zero in state 1. The further combination that makes states 2 and 3 net out forces state 1 to have the "free" profit. The system $X^T q = 0$ effectively requires $q_1(10 - 2 \cdot 5) = 0$, and since the coefficient $(10 - 2 \cdot 5) = 0$ is trivially satisfied, the additional constraint from the second equation forces $q_1 = 0$. The inconsistency in the return ratios across states makes it impossible to find a strictly positive pricing vector.

---

**Exercise 6.** Consider a two-state market with $d = 2$ risky assets: $S^1_0 = 20$, $S^1_1 = (25, 16)$, $S^2_0 = 10$, $S^2_1 = (13, 8)$. Check whether $\operatorname{rank}(X) = n - 1 = 1$. If not, is one of the assets redundant? Find the EMM and price the claim $\Phi = (5, 0)$.

??? success "Solution to Exercise 6"
    The payoff matrix is $2 \times 2$:

    $$
    X = \begin{pmatrix} 25 - 20 & 13 - 10 \\ 16 - 20 & 8 - 10 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ -4 & -2 \end{pmatrix}
    $$

    **Rank check.** Computing the determinant: $5 \cdot (-2) - 3 \cdot (-4) = -10 + 12 = 2 \neq 0$. So $\operatorname{rank}(X) = 2$.

    But for completeness we need $\operatorname{rank}(X) = n - 1 = 1$. Instead we have $\operatorname{rank}(X) = 2 > n - 1 = 1$. This means $\ker(X^T)$ has dimension $n - \operatorname{rank}(X) = 2 - 2 = 0$, so the only solution to $X^T q = 0$ is $q = 0$, which is not a valid probability vector.

    Wait -- let us reconsider. With $n = 2$ states and $d = 2$ assets, $\operatorname{rank}(X) = 2$ means $\ker(X^T) = \{0\}$, so there is no non-zero $q$ with $X^T q = 0$. This would mean no EMM exists, suggesting arbitrage.

    However, re-examining: $X^T q = 0$ means

    $$
    5q_1 - 4q_2 = 0, \qquad 3q_1 - 2q_2 = 0
    $$

    From the first: $q_1 = 4q_2/5$. Substituting into the second: $12q_2/5 - 2q_2 = 2q_2/5 = 0$, forcing $q_2 = 0$ and hence $q_1 = 0$. No EMM exists.

    **Is one asset redundant?** Check if the columns are proportional: $(5, -4)^T$ vs $(3, -2)^T$. The ratios are $5/3 \neq (-4)/(-2) = 2$, so they are **not** proportional. Neither asset is redundant (neither can be replicated by the other).

    **Finding the arbitrage.** Since $\operatorname{rank}(X) = 2 = n$, the map $\theta \mapsto X\theta$ is surjective from $\mathbb{R}^2$ to $\mathbb{R}^2$. We can find $\theta$ such that $X\theta = (1, 0)^T$ (profit in state 1 only):

    $$
    5\theta_1 + 3\theta_2 = 1, \qquad -4\theta_1 - 2\theta_2 = 0
    $$

    From the second: $\theta_2 = -2\theta_1$. Substituting: $5\theta_1 - 6\theta_1 = -\theta_1 = 1$, so $\theta_1 = -1$ and $\theta_2 = 2$. The portfolio $\theta = (-1, 2)$ yields payoff $(1, 0)^T$ -- a non-negative, non-zero payoff at zero cost. This is an arbitrage.

    Since no EMM exists, pricing is not well-defined in this market. The claim $\Phi = (5, 0)$ cannot be given a no-arbitrage price.
