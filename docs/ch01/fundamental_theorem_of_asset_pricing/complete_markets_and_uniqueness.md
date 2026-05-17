# Complete Markets and Uniqueness


This page is the canonical home for the **Second Fundamental Theorem of Asset Pricing**: in an arbitrage-free finite market, the EMM is unique if and only if every contingent claim is replicable (the market is **complete**). The First FTAP and its proof are on the [previous page](fundamental_theorem_of_asset_pricing.md); here we develop the uniqueness side, the rank condition $\operatorname{rank}(X) = n - 1$, and the pricing intervals that arise when uniqueness fails.


??? abstract "Learning Objectives"
    After completing this section, you should be able to:

    - State the definition of market completeness and verify it for a given finite market
    - Prove that an arbitrage-free market is complete if and only if the equivalent martingale measure is unique
    - Use the rank condition on the payoff matrix to determine completeness
    - Compute the unique no-arbitrage price of a claim in a complete market
    - Compute the set of arbitrage-free prices for a claim in an incomplete market
    - Explain why adding assets to an incomplete market can restore completeness


## Setup

By the [First FTAP](fundamental_theorem_of_asset_pricing.md), an arbitrage-free finite market admits at least one EMM. The question addressed here is when that measure is unique, and what uniqueness says about the market.

Recall (see [§ Proof of the First FTAP](fundamental_theorem_of_asset_pricing.md#proof-of-the-first-ftap-finite-state-space)): the model has states $\Omega = \{\omega_1, \ldots, \omega_n\}$ with $\mathbb{P}(\omega_i) > 0$, numéraire $S^0$ normalized to $1$, $d$ risky assets, and $n \times d$ excess-return matrix $X_{ij} = S^j_1(\omega_i) - S^j_0$. A strategy $\theta \in \mathbb{R}^d$ produces the zero-cost payoff $X\theta \in \mathbb{R}^n$; an EMM is a vector $q \in \operatorname{int}(\Delta_n)$ with $X^T q = 0$.


### Attainable Claims

A contingent claim $\Phi = (\Phi(\omega_1), \ldots, \Phi(\omega_n))^T \in \mathbb{R}^n$ is **attainable** (or **replicable**) if there exists a self-financing strategy $\theta \in \mathbb{R}^d$ and an initial investment $c \in \mathbb{R}$ such that

$$
c \cdot \mathbf{1} + X\theta = \Phi
$$

where $\mathbf{1} = (1, \ldots, 1)^T$. The vector $X\theta$ represents the zero-cost payoff component, and $c$ is the cost of the replicating portfolio. The set of attainable claims is the affine subspace

$$
\mathcal{A} = \{c \cdot \mathbf{1} + X\theta : c \in \mathbb{R}, \; \theta \in \mathbb{R}^d\} = \operatorname{span}(\mathbf{1}) + \operatorname{Im}(X)
$$


### Market Completeness

**Definition.** An arbitrage-free market is **complete** if every contingent claim is attainable: $\mathcal{A} = \mathbb{R}^n$.

Equivalently, the market is complete if $\operatorname{span}(\mathbf{1}) + \operatorname{Im}(X) = \mathbb{R}^n$. Since $\mathbf{1}$ is always attainable (hold the numéraire), completeness requires that the image of $X$ together with $\mathbf{1}$ spans all of $\mathbb{R}^n$.


### Rank Condition

**Proposition (Rank condition for completeness).**
*The market is complete if and only if*

$$
\operatorname{rank}(X) \geq n - 1
$$

*Proof.* The space $\operatorname{span}(\mathbf{1}) + \operatorname{Im}(X)$ has dimension at most $1 + \operatorname{rank}(X)$. For this to equal $n$, we need $\operatorname{rank}(X) \geq n - 1$. Conversely, if $\operatorname{rank}(X) \geq n - 1$, then $\operatorname{Im}(X)$ is a subspace of dimension at least $n - 1$. Since $\mathbf{1}$ adds at most one more dimension, we get $\dim(\operatorname{span}(\mathbf{1}) + \operatorname{Im}(X)) = n$. $\square$

!!! note "Number of assets required"
    Since $\operatorname{rank}(X) \leq \min(n, d)$, the rank condition $\operatorname{rank}(X) \geq n - 1$ requires $d \geq n - 1$: we need at least as many risky assets as there are states minus one. With $d < n - 1$ risky assets, the market is **generically incomplete** -- no matter how the payoffs are arranged, the payoff matrix cannot have sufficient rank.


## The Second Fundamental Theorem of Asset Pricing


**Theorem (Second FTAP, finite case).**
*In an arbitrage-free finite-state market, the following are equivalent:*

1. *The market is complete (every contingent claim is attainable).*
2. *The equivalent martingale measure is unique.*

$$
\text{No Arbitrage + Complete} \iff \exists!\, \mathbb{Q} \sim \mathbb{P} \text{ such that } \tilde{S}^i \text{ is a } \mathbb{Q}\text{-martingale for all } i
$$


### Proof: Completeness Implies Uniqueness

Suppose the market is complete, so that every $\Phi \in \mathbb{R}^n$ can be written as $\Phi = c \cdot \mathbf{1} + X\theta$ for some $c \in \mathbb{R}$ and $\theta \in \mathbb{R}^d$. Let $\mathbb{Q}_1$ and $\mathbb{Q}_2$ be two EMMs with weight vectors $q^{(1)}$ and $q^{(2)}$, both satisfying $X^T q^{(k)} = 0$ and $\mathbf{1}^T q^{(k)} = 1$.

For any claim $\Phi = c \cdot \mathbf{1} + X\theta$:

$$
\mathbb{E}^{\mathbb{Q}_1}[\Phi] = c \cdot \mathbf{1}^T q^{(1)} + (X\theta)^T q^{(1)} = c + \theta^T X^T q^{(1)} = c
$$

$$
\mathbb{E}^{\mathbb{Q}_2}[\Phi] = c \cdot \mathbf{1}^T q^{(2)} + (X\theta)^T q^{(2)} = c + \theta^T X^T q^{(2)} = c
$$

So $\mathbb{E}^{\mathbb{Q}_1}[\Phi] = \mathbb{E}^{\mathbb{Q}_2}[\Phi]$ for all $\Phi \in \mathbb{R}^n$. Taking $\Phi = \mathbf{1}_{\{\omega_i\}}$ (the indicator function of each state), we obtain

$$
q^{(1)}_i = \mathbb{E}^{\mathbb{Q}_1}[\mathbf{1}_{\{\omega_i\}}] = \mathbb{E}^{\mathbb{Q}_2}[\mathbf{1}_{\{\omega_i\}}] = q^{(2)}_i \qquad \text{for all } i = 1, \ldots, n
$$

Therefore $\mathbb{Q}_1 = \mathbb{Q}_2$. $\square$


### Proof: Uniqueness Implies Completeness

Suppose the EMM $\mathbb{Q}$ with weight vector $q$ is unique. The set of all EMMs is

$$
\mathcal{K} = \{q' \in \operatorname{int}(\Delta_n) : X^T q' = 0, \; \mathbf{1}^T q' = 1\}
$$

where $\operatorname{int}(\Delta_n) = \{q' \in \mathbb{R}^n : q'_i > 0 \text{ for all } i\}$ is the interior of the probability simplex. Uniqueness means $\mathcal{K} = \{q\}$.

The constraint $X^T q' = 0$ defines the kernel of $X^T$, and $\mathbf{1}^T q' = 1$ is an affine constraint. The set of solutions to $X^T q' = 0$ with $\mathbf{1}^T q' = 1$ is an affine subspace of dimension $\dim(\ker(X^T)) - 1$ (provided $\mathbf{1}$ is not in the row space of $X$, which holds generically). For $\mathcal{K}$ to be a singleton, this affine subspace must intersect $\operatorname{int}(\Delta_n)$ in exactly one point, which requires

$$
\dim(\ker(X^T)) = 1
$$

By the rank-nullity theorem, $\dim(\ker(X^T)) = n - \operatorname{rank}(X)$. So uniqueness gives $\operatorname{rank}(X) = n - 1$, which is exactly the rank condition for completeness.

More precisely: the space of zero-cost attainable payoffs is $\operatorname{Im}(X)$, which has dimension $n - 1$. Since the EMM weight vector $q$ lies in $\ker(X^T)$ and $\ker(X^T) = \operatorname{Im}(X)^\perp$, the one-dimensional kernel is spanned by $q$. Every claim $\Phi \in \mathbb{R}^n$ can be decomposed as

$$
\Phi = \mathbb{E}^{\mathbb{Q}}[\Phi] \cdot \mathbf{1} + X\theta
$$

for some portfolio $\theta$, since $\Phi - \mathbb{E}^{\mathbb{Q}}[\Phi] \cdot \mathbf{1}$ lies in the orthogonal complement of $q$ (because $q^T(\Phi - \mathbb{E}^{\mathbb{Q}}[\Phi] \cdot \mathbf{1}) = \mathbb{E}^{\mathbb{Q}}[\Phi] - \mathbb{E}^{\mathbb{Q}}[\Phi] = 0$), which equals $\operatorname{Im}(X)$. Hence $\Phi$ is attainable with initial cost $c = \mathbb{E}^{\mathbb{Q}}[\Phi]$, and the market is complete. $\square$


!!! note "Remark on dimensions"
    The proof reveals a clean algebraic picture. With $n$ states and $d$ risky assets:

    - $\dim(\ker(X^T)) = n - \operatorname{rank}(X)$ counts the "degrees of freedom" for the EMM.
    - Completeness: $\operatorname{rank}(X) = n - 1$, so $\dim(\ker(X^T)) = 1$ -- exactly one EMM.
    - Incompleteness: $\operatorname{rank}(X) < n - 1$, so $\dim(\ker(X^T)) > 1$ -- a family of EMMs.
    - The number of "missing" assets is $n - 1 - \operatorname{rank}(X)$, which equals the number of extra degrees of freedom in the EMM beyond the unique solution.


## Pricing Implications


The general risk-neutral pricing formula $\pi(\Phi) = \mathbb{E}^{\mathbb{Q}}[\Phi/S^0_T]$ was introduced in the [First FTAP page](fundamental_theorem_of_asset_pricing.md#economic-intuition). The Second FTAP determines whether this formula gives a single number or a range.

**Complete markets: unique prices.** With a unique EMM, every claim is replicable and has a single no-arbitrage price $\pi(\Phi) = \mathbb{E}^{\mathbb{Q}}[\Phi/S^0_T]$.

**Incomplete markets: price intervals.** With multiple EMMs, non-attainable claims have a range of no-arbitrage prices

$$
\pi(\Phi) \in \left[\inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}^{\mathbb{Q}}\!\left[\frac{\Phi}{S^0_T}\right], \; \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}^{\mathbb{Q}}\!\left[\frac{\Phi}{S^0_T}\right]\right]
$$

where $\mathcal{M}$ is the set of all EMMs. The lower bound is the **sub-replication price** (the cheapest portfolio whose payoff is dominated by $\Phi$); the upper bound is the **super-replication price** (the cheapest portfolio whose payoff dominates $\Phi$).

For attainable claims, even in an incomplete market, all EMMs assign the same price (since the replication cost is model-independent). The pricing ambiguity applies only to non-attainable claims.

!!! tip "Practical consequence"
    In incomplete markets, additional information beyond no-arbitrage is needed to pin down a unique price. Practitioners resolve this by choosing a specific pricing measure -- for example, by calibrating to observed market prices, minimizing some criterion (e.g., minimal entropy martingale measure), or using utility-based pricing. The no-arbitrage interval provides bounds that any such choice must respect.


## Example 1: A Complete Market (2 States, 1 Risky Asset)


Consider a one-period market with two states $\Omega = \{\omega_1, \omega_2\}$ and one risky asset ($d = 1$). The numéraire satisfies $S^0_0 = S^0_1 = 1$ (zero interest rate). The risky asset has

$$
S^1_0 = 10, \qquad S^1_1(\omega_1) = 12, \qquad S^1_1(\omega_2) = 8
$$

**Payoff matrix.** The $2 \times 1$ excess return matrix is

$$
X = \begin{pmatrix} S^1_1(\omega_1) - S^1_0 \\ S^1_1(\omega_2) - S^1_0 \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \end{pmatrix}
$$

**Rank check.** We have $\operatorname{rank}(X) = 1 = n - 1 = 2 - 1$. The market is complete.

**Finding the unique EMM.** We need $q = (q_1, q_2)^T$ with $q_1, q_2 > 0$, $q_1 + q_2 = 1$, and $X^T q = 0$:

$$
2q_1 - 2q_2 = 0 \implies q_1 = q_2 = \frac{1}{2}
$$

The unique EMM assigns equal probability to each state: $\mathbb{Q}(\omega_1) = \mathbb{Q}(\omega_2) = 1/2$.

**Replicating a call option.** Consider a call option with strike $K = 10$:

$$
\Phi = \begin{pmatrix} \max(12 - 10, 0) \\ \max(8 - 10, 0) \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \end{pmatrix}
$$

We seek $c$ and $\theta$ such that $c \cdot \mathbf{1} + X\theta = \Phi$:

$$
c + 2\theta = 2, \qquad c - 2\theta = 0
$$

Solving: $\theta = 1/2$ and $c = 1$. The replicating portfolio holds $\theta = 1/2$ units of the risky asset with an initial cost of $c = 1$.

**EMM expectation:**

$$
\mathbb{E}^{\mathbb{Q}}[\Phi] = \tfrac{1}{2} \cdot 2 + \tfrac{1}{2} \cdot 0 = 1
$$

matching the replication cost $c = 1$.


## Example 2: An Incomplete Market (3 States, 1 Risky Asset)


Now consider three states $\Omega = \{\omega_1, \omega_2, \omega_3\}$ with the same single risky asset ($d = 1$):

$$
S^1_0 = 10, \qquad S^1_1(\omega_1) = 14, \qquad S^1_1(\omega_2) = 10, \qquad S^1_1(\omega_3) = 7
$$

**Payoff matrix.** The $3 \times 1$ excess return matrix is

$$
X = \begin{pmatrix} 4 \\ 0 \\ -3 \end{pmatrix}
$$

**Rank check.** We have $\operatorname{rank}(X) = 1 < n - 1 = 2$. The market is incomplete.

**Finding all EMMs.** We need $q = (q_1, q_2, q_3)^T$ with $q_i > 0$, $\sum q_i = 1$, and $X^T q = 0$:

$$
4q_1 + 0 \cdot q_2 - 3q_3 = 0 \implies q_1 = \frac{3}{4}q_3
$$

Combined with $q_1 + q_2 + q_3 = 1$:

$$
\frac{3}{4}q_3 + q_2 + q_3 = 1 \implies q_2 = 1 - \frac{7}{4}q_3
$$

For all components to be strictly positive, we need $q_3 > 0$, $q_1 = \frac{3}{4}q_3 > 0$ (automatic), and $q_2 = 1 - \frac{7}{4}q_3 > 0$, giving $q_3 \in (0, 4/7)$. The set of EMMs is a one-parameter family:

$$
\mathbb{Q}_{q_3} : \quad q_1 = \frac{3}{4}q_3, \quad q_2 = 1 - \frac{7}{4}q_3, \quad q_3 \in \left(0, \frac{4}{7}\right)
$$

A continuum of EMMs, parameterized by $q_3$.

**Pricing a non-attainable claim.** For $\Phi = (5, 1, 0)^T$ under $\mathbb{Q}_{q_3}$:

$$
\mathbb{E}^{\mathbb{Q}_{q_3}}[\Phi] = 5 \cdot \frac{3}{4}q_3 + 1 \cdot \left(1 - \frac{7}{4}q_3\right) + 0 \cdot q_3 = 1 + 2q_3
$$

As $q_3$ ranges over $(0, 4/7)$, the expectation ranges over $(1, 15/7) \approx (1, 2.143)$:

$$
\pi(\Phi) \in \left(1, \; \frac{15}{7}\right)
$$

**Pricing an attainable claim.** The claim $\Psi = (4, 0, -3)^T$ equals $X \cdot 1$, attainable with $\theta = 1$, $c = 0$. For any EMM:

$$
\mathbb{E}^{\mathbb{Q}_{q_3}}[\Psi] = 4 \cdot \frac{3}{4}q_3 + 0 \cdot \left(1 - \frac{7}{4}q_3\right) + (-3) \cdot q_3 = 3q_3 - 3q_3 = 0
$$

All EMMs agree on $\pi(\Psi) = 0$ (attainable at zero cost).


## Example 3: Restoring Completeness by Adding an Asset


Starting from the incomplete market in Example 2, suppose we introduce a second risky asset with payoffs

$$
S^2_0 = 5, \qquad S^2_1(\omega_1) = 8, \qquad S^2_1(\omega_2) = 6, \qquad S^2_1(\omega_3) = 2
$$

The payoff matrix becomes $3 \times 2$:

$$
X = \begin{pmatrix} 4 & 3 \\ 0 & 1 \\ -3 & -3 \end{pmatrix}
$$

**Rank check.** The columns $(4, 0, -3)^T$ and $(3, 1, -3)^T$ are linearly independent, so $\operatorname{rank}(X) = 2 = n - 1 = 3 - 1$. The market is now complete.

**Finding the unique EMM.** Solving $X^T q = 0$ with $\sum q_i = 1$:

$$
4q_1 - 3q_3 = 0, \qquad 3q_1 + q_2 - 3q_3 = 0
$$

From the first equation: $q_1 = \frac{3}{4}q_3$. Substituting into the second:

$$
\frac{9}{4}q_3 + q_2 - 3q_3 = 0 \implies q_2 = \frac{3}{4}q_3
$$

With $q_1 + q_2 + q_3 = 1$: $\frac{3}{4}q_3 + \frac{3}{4}q_3 + q_3 = \frac{10}{4}q_3 = 1$, so $q_3 = 2/5$, $q_1 = 3/10$, $q_2 = 3/10$.

All components are strictly positive, confirming the existence (and uniqueness) of the EMM:

$$
\mathbb{Q}(\omega_1) = \frac{3}{10}, \qquad \mathbb{Q}(\omega_2) = \frac{3}{10}, \qquad \mathbb{Q}(\omega_3) = \frac{2}{5}
$$

The market is now both arbitrage-free and complete. Every claim in $\mathbb{R}^3$ has a unique no-arbitrage price. For instance, the claim $\Phi = (5, 1, 0)^T$ from Example 2 now has the definite price

$$
\pi(\Phi) = \frac{3}{10} \cdot 5 + \frac{3}{10} \cdot 1 + \frac{2}{5} \cdot 0 = \frac{18}{10} = 1.8
$$

which lies within the interval $(1, 15/7) \approx (1, 2.143)$ computed earlier -- as it must, since the unique EMM here corresponds to the parameter value $q_3 = 2/5 \in (0, 4/7)$ from the original family.

!!! warning "Completeness requires no-arbitrage"
    When adding assets to restore completeness, one must verify that the augmented market remains arbitrage-free. The Second FTAP assumes no-arbitrage as a prerequisite. The rank condition $\operatorname{rank}(X) = n - 1$ is necessary for completeness, but if the resulting system $X^T q = 0$ with $\sum q_i = 1$ has no solution with all $q_i > 0$, then the augmented market admits arbitrage rather than being complete. Always check both conditions independently.


## Connection to Continuous Time


The finite-state rank condition $d \geq n - 1$ has a continuous-time analogue: with $m$ independent Brownian drivers and $d$ risky assets with non-degenerate volatility, the market is complete when $d = m$ and generically incomplete when $d < m$. In particular, Black–Scholes ($m = d = 1$) is complete with a unique EMM, while stochastic volatility models ($m = 2$, $d = 1$) are incomplete. The mechanics of measure change underlying these statements are treated in [Numeraire and Change of Measure](../numeraire_and_change_of_measure/numeraire_and_change_of_measure.md).


## Summary


The Second Fundamental Theorem of Asset Pricing provides a complete characterization of when derivative pricing is unambiguous:

1. **Complete + no-arbitrage $\iff$ unique EMM**: the market can replicate every claim if and only if the risk-neutral measure is the only one.

2. **Rank condition**: in a finite model with $n$ states and $d$ risky assets, completeness requires $\operatorname{rank}(X) = n - 1$, which necessitates $d \geq n - 1$.

3. **Unique prices in complete markets**: every contingent claim has a unique no-arbitrage price equal to its discounted expectation under the unique EMM.

4. **Price intervals in incomplete markets**: non-attainable claims have a range of no-arbitrage prices $[\inf_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[\Phi/S^0_T], \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[\Phi/S^0_T]]$, bounded by sub- and super-replication costs.

5. **Adding assets can restore completeness**: introducing new traded instruments increases the rank of the payoff matrix, potentially eliminating the pricing ambiguity.

Together with the [First FTAP](fundamental_theorem_of_asset_pricing.md), these results form the theoretical backbone of derivative pricing. The next page, [Numeraire and Change of Measure](../numeraire_and_change_of_measure/numeraire_and_change_of_measure.md), develops the machinery of measure changes that makes these results computationally tractable.


## References

- Harrison, J. M. and Kreps, D. M. (1979). *Martingales and arbitrage in multiperiod securities markets.* Journal of Economic Theory, 20(3), 381--408.

- Harrison, J. M. and Pliska, S. R. (1981). *Martingales and stochastic integrals in the theory of continuous trading.* Stochastic Processes and their Applications, 11(3), 215--260.

- Föllmer, H. and Schied, A. (2016). *Stochastic Finance: An Introduction in Discrete Time.* 4th edition, de Gruyter.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance I: The Binomial Asset Pricing Model.* Springer.

---

## Exercises

**Exercise 1.** Consider a one-period market with $n = 3$ states and $d = 1$ risky asset. The excess return vector is $X = (8, 0, -4)^T$. Show that the market is incomplete and parameterize the full family of EMMs. What is the no-arbitrage price interval for the claim $\Phi = (3, 1, 0)^T$?

??? success "Solution to Exercise 1"
    The payoff matrix is $3 \times 1$:

    $$
    X = \begin{pmatrix} 8 \\ 0 \\ -4 \end{pmatrix}
    $$

    **Rank check:** $\operatorname{rank}(X) = 1 < n - 1 = 2$, so the market is **incomplete**.

    **Finding EMMs.** We need $q = (q_1, q_2, q_3)$ with $q_i > 0$, $\sum q_i = 1$, and $X^T q = 0$:

    $$
    8q_1 + 0 \cdot q_2 - 4q_3 = 0 \implies q_1 = \frac{1}{2}q_3
    $$

    From normalization: $\frac{1}{2}q_3 + q_2 + q_3 = 1$, so $q_2 = 1 - \frac{3}{2}q_3$.

    For strict positivity: $q_3 > 0$, $q_1 = q_3/2 > 0$ (automatic), and $q_2 = 1 - 3q_3/2 > 0$ gives $q_3 < 2/3$. The family of EMMs is:

    $$
    \mathcal{Q} = \left\{\left(\frac{q_3}{2}, \; 1 - \frac{3q_3}{2}, \; q_3\right) : q_3 \in \left(0, \frac{2}{3}\right)\right\}
    $$

    **Price interval for $\Phi = (3, 1, 0)^T$:**

    $$
    \mathbb{E}^{\mathbb{Q}}[\Phi] = 3 \cdot \frac{q_3}{2} + 1 \cdot \left(1 - \frac{3q_3}{2}\right) + 0 \cdot q_3 = \frac{3q_3}{2} + 1 - \frac{3q_3}{2} = 1
    $$

    Remarkably, the price is constant across all EMMs: $\pi(\Phi) = 1$. Despite the market being incomplete, this particular claim has a unique no-arbitrage price. This occurs because $\Phi - 1 \cdot \mathbf{1} = (2, 0, -1)^T = \frac{1}{4}(8, 0, -4)^T = \frac{1}{4}X$, so $\Phi$ is attainable with $\theta = 1/4$ and initial cost $c = 1$.

---

**Exercise 2.** In a market with $n = 4$ states and $d = 3$ risky assets, the payoff matrix has rank 3. Is the market complete? Justify your answer using the rank condition. How many EMMs exist?

??? success "Solution to Exercise 2"
    With $n = 4$ states and $d = 3$ risky assets, the payoff matrix $X$ is $4 \times 3$ with $\operatorname{rank}(X) = 3$.

    The rank condition for completeness requires $\operatorname{rank}(X) = n - 1 = 3$. Since $\operatorname{rank}(X) = 3 = n - 1$, the market **is complete** (assuming it is arbitrage-free).

    The dimension of $\ker(X^T)$ is $n - \operatorname{rank}(X) = 4 - 3 = 1$. Intersecting this one-dimensional kernel with the affine hyperplane $\{\sum q_i = 1\}$ gives a single point. If this point lies in the interior of the simplex (all $q_i > 0$), then the EMM is unique and exactly **one** EMM exists. The market is both arbitrage-free and complete.

---

**Exercise 3.** Prove that in a complete, arbitrage-free market, the replication cost of any contingent claim $\Phi$ equals $\mathbb{E}^{\mathbb{Q}}[\Phi]$, where $\mathbb{Q}$ is the unique EMM. Start from the decomposition $\Phi = c \cdot \mathbf{1} + X\theta$ and use the martingale property of $X$ under $\mathbb{Q}$.

??? success "Solution to Exercise 3"
    If $\Phi$ is attainable, there exist $c \in \mathbb{R}$ and $\theta \in \mathbb{R}^d$ such that

    $$
    \Phi = c \cdot \mathbf{1} + X\theta
    $$

    Taking the expectation under any EMM $\mathbb{Q}$ (with weight vector $q$ satisfying $X^T q = 0$ and $\mathbf{1}^T q = 1$):

    $$
    \mathbb{E}^{\mathbb{Q}}[\Phi] = \mathbb{E}^{\mathbb{Q}}[c \cdot \mathbf{1} + X\theta] = c \cdot \mathbb{E}^{\mathbb{Q}}[\mathbf{1}] + \mathbb{E}^{\mathbb{Q}}[X\theta]
    $$

    Now $\mathbb{E}^{\mathbb{Q}}[\mathbf{1}] = \mathbf{1}^T q = 1$, and

    $$
    \mathbb{E}^{\mathbb{Q}}[X\theta] = q^T(X\theta) = (X^T q)^T \theta = 0^T \theta = 0
    $$

    since $X^T q = 0$ is the martingale condition. Therefore

    $$
    \mathbb{E}^{\mathbb{Q}}[\Phi] = c
    $$

    for every EMM $\mathbb{Q}$. The replication cost $c$ is the unique no-arbitrage price, and it equals the risk-neutral expectation regardless of which EMM is chosen. $\square$

---

**Exercise 4.** An incomplete market has $n = 3$ states and $d = 1$ risky asset with $S^1_0 = 50$ and $S^1_1 = (65, 50, 40)$. A new asset with payoffs $S^2_1 = (10, 5, 0)$ is introduced at price $S^2_0 = a$. For which values of $a$ does the augmented market remain arbitrage-free? For which value of $a$ does the augmented market become complete?

??? success "Solution to Exercise 4"
    The original payoff matrix is $X_1 = (15, -5, -10)^T$ with the excess returns for the first asset. The excess returns for the second asset are $S^2_1 - S^2_0 = (10 - a, \, 5 - a, \, 0 - a)$.

    The augmented payoff matrix is

    $$
    X = \begin{pmatrix} 15 & 10 - a \\ -5 & 5 - a \\ -10 & -a \end{pmatrix}
    $$

    **Finding EMMs for the original market.** From $15q_1 - 5q_2 - 10q_3 = 0$ and $q_1 + q_2 + q_3 = 1$: $q_1 = 2q_3/3 + q_2/3$. Using normalization, the family is parameterized by $q_2$. For the augmented market, adding the second equation $(10-a)q_1 + (5-a)q_2 + (-a)q_3 = 0$ pins down a unique solution (if $\operatorname{rank}(X) = 2$).

    From the first constraint: $3q_1 = q_2 + 2q_3$, so $q_1 = (q_2 + 2q_3)/3$.

    With $q_1 + q_2 + q_3 = 1$: $(q_2 + 2q_3)/3 + q_2 + q_3 = 1$, giving $4q_2 + 5q_3 = 3$.

    The second asset constraint $(10-a)q_1 + (5-a)q_2 - aq_3 = 0$ expands to $10q_1 + 5q_2 - a(q_1 + q_2 + q_3) = 0$, so $10q_1 + 5q_2 = a$.

    Substituting $q_1 = (q_2 + 2q_3)/3$: $10(q_2 + 2q_3)/3 + 5q_2 = a$, giving $25q_2/3 + 20q_3/3 = a$, i.e., $25q_2 + 20q_3 = 3a$.

    From $4q_2 + 5q_3 = 3$: $q_2 = (3 - 5q_3)/4$. Substituting:

    $$
    25 \cdot \frac{3 - 5q_3}{4} + 20q_3 = 3a \implies \frac{75 - 125q_3 + 80q_3}{4} = 3a \implies 75 - 45q_3 = 12a
    $$

    So $q_3 = (75 - 12a)/45 = (25 - 4a)/15$.

    For $q_3 > 0$: $a < 25/4 = 6.25$. Then $q_2 = (3 - 5(25 - 4a)/15)/4 = (45 - 125 + 20a)/(60) = (20a - 80)/60 = (a - 4)/3$. For $q_2 > 0$: $a > 4$. And $q_1 = (q_2 + 2q_3)/3 = ((a-4)/3 + 2(25-4a)/15)/3 = (5a - 20 + 50 - 8a)/(45) = (30 - 3a)/45 = (10 - a)/15$. For $q_1 > 0$: $a < 10$ (automatic given $a < 6.25$).

    The augmented market is **arbitrage-free** for $a \in (4, 25/4)$.

    The market becomes **complete** for any $a$ in this range (since $\operatorname{rank}(X) = 2 = n - 1$ when the second column is not proportional to the first, which holds for $a \neq 5$ in general; one should verify linear independence for the specific value).

---

**Exercise 5.** Suppose the stochastic volatility model has two Brownian motions $(W^1_t, W^2_t)$ driving the stock price $S_t$ and its volatility $\sigma_t$, but only $S_t$ is traded. Explain why this market is incomplete using the counting rule ($d < m$). How many independent sources of risk remain unhedgeable?

??? success "Solution to Exercise 5"
    The stochastic volatility model has $m = 2$ independent sources of randomness (Brownian motions $W^1_t$ and $W^2_t$) but only $d = 1$ traded risky asset ($S_t$). The counting rule states that completeness requires $d \geq m$. Since $d = 1 < 2 = m$, the market is **incomplete**.

    The number of unhedgeable sources of risk is $m - d = 2 - 1 = 1$. Specifically, the stock $S_t$ provides exposure to a particular linear combination of $W^1_t$ and $W^2_t$ (through its volatility vector). By trading $S_t$, one can hedge risk in that direction. However, the orthogonal direction -- the component of risk not spanned by the stock's volatility -- cannot be hedged.

    In a stochastic volatility model, the unhedgeable risk is typically the **volatility risk**: changes in $\sigma_t$ driven by the Brownian motion that is not (or only partially) correlated with the stock's Brownian motion. This is why the EMM is not unique -- different choices of the "market price of volatility risk" correspond to different equivalent martingale measures, and each assigns a different price to volatility-sensitive derivatives.

---

**Exercise 6.** In an incomplete market, the no-arbitrage price of a non-attainable claim $\Phi$ lies in the interval $[\inf_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[\Phi/S^0_T], \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[\Phi/S^0_T]]$. Show that for an attainable claim, the infimum and supremum coincide, so the price is unique even in an incomplete market.

??? success "Solution to Exercise 6"
    Let $\Phi$ be attainable: $\Phi = c \cdot \mathbf{1} + X\theta$ for some $c \in \mathbb{R}$ and $\theta \in \mathbb{R}^d$. For any EMM $\mathbb{Q}$ with weight vector $q$ (satisfying $X^T q = 0$ and $\mathbf{1}^T q = 1$), with $S^0_T = 1$ (normalized numéraire):

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{\Phi}{S^0_T}\right] = \mathbb{E}^{\mathbb{Q}}[\Phi] = q^T \Phi = q^T(c \cdot \mathbf{1} + X\theta) = c \cdot q^T \mathbf{1} + q^T X\theta = c \cdot 1 + (X^T q)^T \theta = c
    $$

    This holds for **every** EMM $\mathbb{Q} \in \mathcal{M}$. Therefore

    $$
    \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}^{\mathbb{Q}}[\Phi] = c = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}^{\mathbb{Q}}[\Phi]
    $$

    The infimum and supremum coincide, giving the unique price $\pi(\Phi) = c$.

    This result makes economic sense: an attainable claim can be perfectly replicated at cost $c$. By no-arbitrage, its price must equal $c$ regardless of the model -- any other price would create an arbitrage by buying (or selling) the claim and implementing the replicating (or reverse) strategy. Since the replication argument uses only the traded assets, it is independent of the choice of EMM, and all measures agree on the price. $\square$
