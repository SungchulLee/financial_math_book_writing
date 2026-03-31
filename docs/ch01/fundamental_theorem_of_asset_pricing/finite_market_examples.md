# Finite Market Examples


The abstract machinery of the [Fundamental Theorem of Asset Pricing](fundamental_theorem_of_asset_pricing.md) comes alive in small, explicitly solvable markets. Working through concrete numerical models builds the intuition that no amount of general theory can provide: one sees exactly how the payoff matrix encodes market structure, how solving a linear system yields the risk-neutral measure, and how the rank of that matrix determines completeness.

This page presents four progressively richer finite-state models. Each example sets up the payoff matrix $X$, solves for the equivalent martingale measure(s) $\mathbb{Q}$, and interprets the results through the lens of the First and Second FTAP.

!!! info "Learning Objectives"
    After completing this section, you should be able to:

    - Given a payoff matrix $X$, solve for all risk-neutral probability vectors $q$ satisfying $X^T q = 0$ with $q_i > 0$
    - Identify whether a finite market admits arbitrage, is complete, or is incomplete
    - Price contingent claims using the EMM in a complete market
    - Compute the no-arbitrage price bounds for an unattainable claim in an incomplete market
    - Detect arbitrage opportunities by checking for the existence of strictly positive state prices


## Roadmap

The four examples illustrate different structural possibilities for a one-period finite-state market:

| Example | States | Risky Assets | Key Concept |
|---------|--------|-------------|-------------|
| 1 | 2 | 1 | Complete market, unique EMM, derivative pricing |
| 2 | 3 | 1 | Incomplete market, family of EMMs, price bounds |
| 3 | 3 | 2 | Complete market via additional asset, unique EMM |
| 4 | 3 | 2 | Arbitrage detection, failure of EMM existence |


## Common Setup

We work in a one-period model ($t \in \{0, 1\}$) with finite state space $\Omega = \{\omega_1, \ldots, \omega_n\}$ and physical probabilities $\mathbb{P}(\omega_i) = p_i > 0$. Following the notation of the [FTAP proof](fundamental_theorem_of_asset_pricing.md), the numéraire $S^0$ is normalized so that $S^0_0 = S^0_1 = 1$ (equivalently, all prices are pre-discounted). There are $d$ risky assets with time-0 prices $S^j_0$ and random time-1 payoffs $S^j_1(\omega_i)$.

The $n \times d$ **payoff matrix** of discounted excess returns is

$$
X_{ij} = S^j_1(\omega_i) - S^j_0, \qquad i = 1, \ldots, n, \quad j = 1, \ldots, d
$$

An **equivalent martingale measure** (EMM) is a probability vector $q = (q_1, \ldots, q_n)$ with $q_i > 0$ for all $i$ and $\sum_i q_i = 1$ satisfying

$$
X^T q = 0
$$

By the [First FTAP](fundamental_theorem_of_asset_pricing.md), the market is arbitrage-free if and only if such a $q$ exists. By the [Second FTAP](fundamental_theorem_of_asset_pricing.md), the market is complete if and only if the EMM is unique.


## Example 1: Two-State Market (Complete)

### Setup

Consider the simplest non-trivial market: two states and one risky asset.

- States: $\Omega = \{\omega_1, \omega_2\}$ with $\mathbb{P}(\omega_1) = p > 0$, $\mathbb{P}(\omega_2) = 1 - p > 0$.
- Risky asset: $S^1_0 = 100$, with

$$
S^1_1(\omega_i) = \begin{cases} 120 & \text{if } i = 1 \quad (\text{up state}) \\ 90 & \text{if } i = 2 \quad (\text{down state}) \end{cases}
$$

The payoff matrix is $n \times d = 2 \times 1$:

$$
X = \begin{pmatrix} S^1_1(\omega_1) - S^1_0 \\ S^1_1(\omega_2) - S^1_0 \end{pmatrix} = \begin{pmatrix} 20 \\ -10 \end{pmatrix}
$$

### Solving for the EMM

We need $q = (q_1, q_2)$ with $q_1, q_2 > 0$, $q_1 + q_2 = 1$, and $X^T q = 0$:

$$
X^T q = 20\, q_1 + (-10)\, q_2 = 0
$$

Substituting $q_2 = 1 - q_1$:

$$
20\, q_1 - 10(1 - q_1) = 0 \quad \Longrightarrow \quad 30\, q_1 = 10 \quad \Longrightarrow \quad q_1 = \frac{1}{3}
$$

So $q_2 = \frac{2}{3}$. Both are strictly positive, confirming that an EMM exists (no arbitrage) and it is unique (the market is complete).

$$
\mathbb{Q} = \left(\frac{1}{3},\; \frac{2}{3}\right)
$$

!!! note "Verification"
    Under $\mathbb{Q}$, the expected discounted price of the risky asset equals its time-0 price:

    $$
    \mathbb{E}^{\mathbb{Q}}[S^1_1] = \frac{1}{3} \cdot 120 + \frac{2}{3} \cdot 90 = 40 + 60 = 100 = S^1_0
    $$

    The martingale condition is satisfied.

### Pricing a Derivative

Consider a European call option with strike $K = 100$. Its payoff is

$$
\Phi(\omega_i) = \max(S^1_1(\omega_i) - K, \; 0) = \begin{cases} 20 & \text{if } i = 1 \\ 0 & \text{if } i = 2 \end{cases}
$$

Since the market is complete, the unique no-arbitrage price is

$$
V_0 = \mathbb{E}^{\mathbb{Q}}[\Phi] = \frac{1}{3} \cdot 20 + \frac{2}{3} \cdot 0 = \frac{20}{3} \approx 6.67
$$

### Replicating Portfolio

Completeness means we can replicate $\Phi$ exactly. We seek $\theta \in \mathbb{R}$ (units of the risky asset) and $\theta^0 \in \mathbb{R}$ (units of the numéraire) such that

$$
\theta^0 + \theta \cdot S^1_1(\omega_i) = \Phi(\omega_i) \quad \text{for } i = 1, 2
$$

This gives the system:

$$
\theta^0 + 120\,\theta = 20, \qquad \theta^0 + 90\,\theta = 0
$$

Subtracting: $30\,\theta = 20$, so $\theta = \frac{2}{3}$. Back-substituting: $\theta^0 = -90 \cdot \frac{2}{3} = -60$.

The replicating portfolio holds $\frac{2}{3}$ units of the stock and borrows $60$ in the numéraire. Its initial cost is

$$
V_0 = \theta^0 + \theta \cdot S^1_0 = -60 + \frac{2}{3} \cdot 100 = -60 + \frac{200}{3} = \frac{20}{3}
$$

This matches the risk-neutral price, as it must.

!!! tip "Interpretation"
    In a two-state, one-asset market, one equation ($X^T q = 0$) with two unknowns ($q_1, q_2$) subject to the constraint $q_1 + q_2 = 1$ leaves zero degrees of freedom. The EMM is pinned down uniquely, the market is complete, and every contingent claim has a unique price and a replicating portfolio. This is the finite analogue of the Black--Scholes setting, where one source of randomness and one risky asset yield a unique EMM.


## Example 2: Three-State Market with One Asset (Incomplete)

### Setup

Now add a third state while keeping only one risky asset.

- States: $\Omega = \{\omega_1, \omega_2, \omega_3\}$ with $p_i > 0$ for all $i$.
- Risky asset: $S^1_0 = 100$, with

$$
S^1_1(\omega_i) = \begin{cases} 130 & \text{if } i = 1 \quad (\text{up}) \\ 100 & \text{if } i = 2 \quad (\text{middle}) \\ 80 & \text{if } i = 3 \quad (\text{down}) \end{cases}
$$

The payoff matrix is $3 \times 1$:

$$
X = \begin{pmatrix} 30 \\ 0 \\ -20 \end{pmatrix}
$$

### The Family of EMMs

We need $q_1, q_2, q_3 > 0$ with $q_1 + q_2 + q_3 = 1$ and $X^T q = 0$:

$$
30\, q_1 + 0 \cdot q_2 + (-20)\, q_3 = 0 \quad \Longrightarrow \quad 30\, q_1 = 20\, q_3 \quad \Longrightarrow \quad q_3 = \frac{3}{2}\, q_1
$$

With the normalization constraint:

$$
q_1 + q_2 + \frac{3}{2}\, q_1 = 1 \quad \Longrightarrow \quad q_2 = 1 - \frac{5}{2}\, q_1
$$

For all components to be strictly positive, we need $q_1 > 0$, $q_3 = \frac{3}{2}\, q_1 > 0$ (automatically satisfied), and $q_2 = 1 - \frac{5}{2}\, q_1 > 0$, which gives $q_1 < \frac{2}{5}$. Therefore the set of EMMs is the one-parameter family

$$
\mathcal{Q} = \left\{\left(q_1,\; 1 - \frac{5}{2}\, q_1,\; \frac{3}{2}\, q_1\right) : 0 < q_1 < \frac{2}{5}\right\}
$$

There are infinitely many EMMs, so the market is **incomplete** by the [Second FTAP](fundamental_theorem_of_asset_pricing.md).

!!! note "Dimensional explanation"
    We have $n = 3$ states and $d = 1$ risky asset. The kernel of $X^T$ has dimension $n - \operatorname{rank}(X) = 3 - 1 = 2$. Intersecting this two-dimensional subspace with the affine hyperplane $\{q : \sum q_i = 1\}$ gives a one-dimensional family (a line segment inside the simplex). Completeness would require $\operatorname{rank}(X) = n - 1 = 2$, but we only have $d = 1 < n - 1 = 2$ risky assets, so the market is generically incomplete.

### Price Bounds for an Unattainable Claim

Consider a "digital option" that pays $\Phi = (1, 0, 0)$: it pays $1$ in the up state and $0$ otherwise. Since the market is incomplete, $\Phi$ is not perfectly replicable, and different EMMs assign different prices.

The no-arbitrage price under a given $\mathbb{Q} \in \mathcal{Q}$ is

$$
V_0(\mathbb{Q}) = \mathbb{E}^{\mathbb{Q}}[\Phi] = q_1 \cdot 1 + q_2 \cdot 0 + q_3 \cdot 0 = q_1
$$

As $q_1$ ranges over $\left(0, \frac{2}{5}\right)$, the no-arbitrage price ranges over the open interval

$$
V_0 \in \left(0,\; \frac{2}{5}\right)
$$

Any price in this interval is consistent with no-arbitrage; any price outside it would create an arbitrage opportunity. The endpoints represent the **sub-replication price** (infimum) and the **super-replication price** (supremum).

??? example "Explicit price bounds for a call option"
    Consider a European call with strike $K = 100$: $\Phi = (\max(130 - 100, 0),\; \max(100 - 100, 0),\; \max(80 - 100, 0)) = (30, 0, 0)$.

    The price under $\mathbb{Q} \in \mathcal{Q}$ is

    $$
    V_0(\mathbb{Q}) = 30\, q_1
    $$

    As $q_1 \in \left(0, \frac{2}{5}\right)$, this gives the no-arbitrage price interval $(0, 12)$. No single price is "correct" without additional information (such as risk preferences or a utility function) or additional traded assets.


## Example 3: Three-State Market with Two Assets (Complete)

### Setup

We restore completeness by introducing a second risky asset.

- States: $\Omega = \{\omega_1, \omega_2, \omega_3\}$ with $p_i > 0$ for all $i$.
- Asset 1: $S^1_0 = 100$, with $S^1_1 = (130, 100, 80)$.
- Asset 2: $S^2_0 = 50$, with $S^2_1 = (40, 60, 45)$.

The payoff matrix is $3 \times 2$:

$$
X = \begin{pmatrix} 130 - 100 & 40 - 50 \\ 100 - 100 & 60 - 50 \\ 80 - 100 & 45 - 50 \end{pmatrix} = \begin{pmatrix} 30 & -10 \\ 0 & 10 \\ -20 & -5 \end{pmatrix}
$$

### Solving for the EMM

We need $q = (q_1, q_2, q_3)$ with $q_i > 0$, $\sum q_i = 1$, and $X^T q = 0$. This gives two equations:

$$
\begin{aligned}
30\, q_1 + 0 \cdot q_2 - 20\, q_3 &= 0 \\
-10\, q_1 + 10\, q_2 - 5\, q_3 &= 0
\end{aligned}
$$

From the first equation: $q_3 = \frac{3}{2}\, q_1$.

Substituting into the second equation:

$$
-10\, q_1 + 10\, q_2 - 5 \cdot \frac{3}{2}\, q_1 = 0 \quad \Longrightarrow \quad -10\, q_1 + 10\, q_2 - \frac{15}{2}\, q_1 = 0 \quad \Longrightarrow \quad q_2 = \frac{35}{20}\, q_1 = \frac{7}{4}\, q_1
$$

Using the normalization constraint:

$$
q_1 + \frac{7}{4}\, q_1 + \frac{3}{2}\, q_1 = 1 \quad \Longrightarrow \quad \frac{4 + 7 + 6}{4}\, q_1 = 1 \quad \Longrightarrow \quad q_1 = \frac{4}{17}
$$

Therefore:

$$
q_1 = \frac{4}{17}, \qquad q_2 = \frac{7}{17}, \qquad q_3 = \frac{6}{17}
$$

All components are strictly positive, so the EMM exists (no arbitrage). It is unique because two equations plus the normalization constraint fully determine the three unknowns. The market is **complete**.

!!! note "Verification"
    Check the martingale condition for both assets:

    $$
    \mathbb{E}^{\mathbb{Q}}[S^1_1] = \frac{4}{17} \cdot 130 + \frac{7}{17} \cdot 100 + \frac{6}{17} \cdot 80 = \frac{520 + 700 + 480}{17} = \frac{1700}{17} = 100 = S^1_0
    $$

    $$
    \mathbb{E}^{\mathbb{Q}}[S^2_1] = \frac{4}{17} \cdot 40 + \frac{7}{17} \cdot 60 + \frac{6}{17} \cdot 45 = \frac{160 + 420 + 270}{17} = \frac{850}{17} = 50 = S^2_0
    $$

    Both assets are martingales under $\mathbb{Q}$.

### Pricing and Replication

In this complete market, every contingent claim has a unique price and a replicating portfolio.

**Pricing.** Consider the digital option from Example 2: $\Phi = (1, 0, 0)$. Its unique no-arbitrage price is

$$
V_0 = \mathbb{E}^{\mathbb{Q}}[\Phi] = \frac{4}{17} \approx 0.235
$$

This lies within the interval $(0, 2/5)$ found in Example 2, as it must: adding a traded asset can only narrow (or maintain) the price interval, never widen it.

**Replication.** We seek $\theta^0, \theta^1, \theta^2$ such that $\theta^0 + \theta^1 S^1_1(\omega_i) + \theta^2 S^2_1(\omega_i) = \Phi(\omega_i)$ for all $i$:

$$
\begin{aligned}
\theta^0 + 130\,\theta^1 + 40\,\theta^2 &= 1 \\
\theta^0 + 100\,\theta^1 + 60\,\theta^2 &= 0 \\
\theta^0 + 80\,\theta^1 + 45\,\theta^2 &= 0
\end{aligned}
$$

Subtracting the second equation from the first: $30\,\theta^1 - 20\,\theta^2 = 1$.

Subtracting the third equation from the second: $20\,\theta^1 + 15\,\theta^2 = 0$, giving $\theta^2 = -\frac{4}{3}\,\theta^1$.

Substituting: $30\,\theta^1 - 20 \cdot \left(-\frac{4}{3}\,\theta^1\right) = 1$, so $30\,\theta^1 + \frac{80}{3}\,\theta^1 = 1$, giving $\frac{170}{3}\,\theta^1 = 1$, hence $\theta^1 = \frac{3}{170}$.

Then $\theta^2 = -\frac{4}{3} \cdot \frac{3}{170} = -\frac{4}{170} = -\frac{2}{85}$.

From the second equation: $\theta^0 = -100 \cdot \frac{3}{170} - 60 \cdot \left(-\frac{2}{85}\right) = -\frac{300}{170} + \frac{120}{85} = -\frac{30}{17} + \frac{24}{17} = -\frac{6}{17}$.

The replicating portfolio cost is

$$
V_0 = \theta^0 + \theta^1 \cdot 100 + \theta^2 \cdot 50 = -\frac{6}{17} + \frac{300}{170} - \frac{100}{85} = -\frac{6}{17} + \frac{30}{17} - \frac{20}{17} = \frac{4}{17}
$$

This confirms the risk-neutral price.

!!! tip "Interpretation"
    With $n = 3$ states and $d = 2$ risky assets, we have $d = n - 1$, and the payoff matrix has full column rank $\operatorname{rank}(X) = 2 = n - 1$. The kernel of $X^T$ is one-dimensional, so after normalizing to the simplex, the EMM is unique. This is the generic condition for completeness in finite markets, as discussed in [Complete Markets and Uniqueness](complete_markets_and_uniqueness.md).


## Example 4: Arbitrage Detection

### Setup

We now present a market where no EMM exists, revealing an arbitrage opportunity.

- States: $\Omega = \{\omega_1, \omega_2, \omega_3\}$ with $p_i > 0$ for all $i$.
- Asset 1: $S^1_0 = 100$, with $S^1_1 = (110, 105, 95)$.
- Asset 2: $S^2_0 = 50$, with $S^2_1 = (55, 52, 48)$.

The payoff matrix is

$$
X = \begin{pmatrix} 10 & 5 \\ 5 & 2 \\ -5 & -2 \end{pmatrix}
$$

### Attempting to Find an EMM

We need $X^T q = 0$ with $q_i > 0$ and $\sum q_i = 1$:

$$
\begin{aligned}
10\, q_1 + 5\, q_2 - 5\, q_3 &= 0 \\
5\, q_1 + 2\, q_2 - 2\, q_3 &= 0
\end{aligned}
$$

From the second equation: $q_3 = \frac{5\, q_1 + 2\, q_2}{2}$.

Substituting into the first equation:

$$
10\, q_1 + 5\, q_2 - 5 \cdot \frac{5\, q_1 + 2\, q_2}{2} = 0 \quad \Longrightarrow \quad 10\, q_1 + 5\, q_2 - \frac{25\, q_1 + 10\, q_2}{2} = 0
$$

Multiplying through by 2:

$$
20\, q_1 + 10\, q_2 - 25\, q_1 - 10\, q_2 = 0 \quad \Longrightarrow \quad -5\, q_1 = 0 \quad \Longrightarrow \quad q_1 = 0
$$

This forces $q_1 = 0$, which violates the strict positivity requirement $q_i > 0$. No EMM exists.

By the [First FTAP](fundamental_theorem_of_asset_pricing.md), the market admits an arbitrage opportunity.

### Finding the Arbitrage Portfolio

Since no EMM exists, the [Separating Hyperplane Theorem](separating_hyperplane_theorem.md) guarantees a separating direction. We seek a portfolio $\theta = (\theta^1, \theta^2) \in \mathbb{R}^2$ such that $X\theta \geq 0$ with at least one strict inequality.

Compute $X\theta$:

$$
X\theta = \begin{pmatrix} 10\,\theta^1 + 5\,\theta^2 \\ 5\,\theta^1 + 2\,\theta^2 \\ -5\,\theta^1 - 2\,\theta^2 \end{pmatrix}
$$

For $X\theta \geq 0$, the third component requires $-5\,\theta^1 - 2\,\theta^2 \geq 0$, i.e., $5\,\theta^1 + 2\,\theta^2 \leq 0$. But the second component requires $5\,\theta^1 + 2\,\theta^2 \geq 0$. Together:

$$
5\,\theta^1 + 2\,\theta^2 = 0 \quad \Longrightarrow \quad \theta^2 = -\frac{5}{2}\,\theta^1
$$

Substituting into the first component:

$$
10\,\theta^1 + 5 \cdot \left(-\frac{5}{2}\,\theta^1\right) = 10\,\theta^1 - \frac{25}{2}\,\theta^1 = -\frac{5}{2}\,\theta^1
$$

For this to be non-negative, we need $\theta^1 \leq 0$. Choose $\theta^1 = -2$, giving $\theta^2 = 5$.

The arbitrage portfolio is $\theta = (-2, 5)$: short 2 units of Asset 1 and buy 5 units of Asset 2. The payoff vector is

$$
X\theta = \begin{pmatrix} 10(-2) + 5(5) \\ 5(-2) + 2(5) \\ -5(-2) - 2(5) \end{pmatrix} = \begin{pmatrix} 5 \\ 0 \\ 0 \end{pmatrix}
$$

The initial cost is zero (since $X$ encodes excess returns from zero-cost positions), the payoff is non-negative in every state, and it is strictly positive in state $\omega_1$. This is an arbitrage.

!!! warning "Economic interpretation"
    The arbitrage arises because the two assets' excess-return columns are nearly proportional but not exactly so. In states $\omega_2$ and $\omega_3$, the ratio of Asset 1's excess return to Asset 2's is $5/2 = (-5)/(-2) = 2.5$. But in state $\omega_1$, the ratio is $10/5 = 2$. This inconsistency means that no single probability weighting can make both columns average to zero simultaneously while keeping $q_1 > 0$. The arbitrageur exploits this by shorting Asset 1 and going long Asset 2 in a proportion ($\theta^2/\theta^1 = -5/2$) that cancels the payoff in states $\omega_2$ and $\omega_3$ while leaving a strict profit in state $\omega_1$.

### State Price Perspective

An equivalent way to detect arbitrage is through **state prices** (also called Arrow--Debreu prices). A state price vector $\psi = (\psi_1, \psi_2, \psi_3)$ satisfies $\psi_i > 0$ for all $i$ and prices each asset correctly:

$$
S^j_0 = \sum_{i=1}^{n} \psi_i \, S^j_1(\omega_i) \quad \text{for } j = 0, 1, \ldots, d
$$

For the numéraire ($S^0_0 = S^0_1 = 1$): $\psi_1 + \psi_2 + \psi_3 = 1$.

For Asset 1: $100 = 110\,\psi_1 + 105\,\psi_2 + 95\,\psi_3$.

For Asset 2: $50 = 55\,\psi_1 + 52\,\psi_2 + 48\,\psi_3$.

Note that the state price vector is related to the EMM by $\psi_i = q_i$ (when the numéraire has value 1 at both times). So the non-existence of strictly positive state prices is equivalent to the non-existence of an EMM. The system above forces $\psi_1 = 0$, confirming the arbitrage.


## Summary of Results

The table below collects the key structural properties across all four examples.

| Property | Example 1 | Example 2 | Example 3 | Example 4 |
|----------|-----------|-----------|-----------|-----------|
| States $n$ | 2 | 3 | 3 | 3 |
| Risky assets $d$ | 1 | 1 | 2 | 2 |
| $\operatorname{rank}(X)$ | 1 | 1 | 2 | 2 |
| $\dim(\ker X^T)$ | 1 | 2 | 1 | 1 |
| EMM exists? | Yes | Yes | Yes | No |
| EMM unique? | Yes | No | Yes | N/A |
| Complete? | Yes | No | Yes | N/A |
| Arbitrage-free? | Yes | Yes | Yes | No |

The pattern is clear:

- **First FTAP**: an EMM exists $\iff$ no arbitrage. Example 4 has no EMM and admits arbitrage; Examples 1--3 have EMMs and are arbitrage-free.
- **Second FTAP**: the EMM is unique $\iff$ market completeness. Examples 1 and 3 have unique EMMs and complete markets; Example 2 has a family of EMMs and an incomplete market.
- **Rank condition**: completeness requires $\operatorname{rank}(X) = n - 1$, which in turn requires at least $d \geq n - 1$ risky assets with linearly independent payoff columns.


## Key Takeaways

The examples on this page demonstrate several core principles:

1. **The EMM condition $X^T q = 0$ is a concrete linear system.** In small markets, finding the risk-neutral measure reduces to solving a handful of linear equations subject to positivity constraints.

2. **Completeness is a rank condition.** A market with $n$ states is complete if and only if the payoff matrix has rank $n - 1$, which requires at least $n - 1$ risky assets with linearly independent payoffs.

3. **Incomplete markets produce price intervals, not unique prices.** When multiple EMMs exist, each assigns a different price to non-replicable claims. The supremum and infimum over all EMMs give the super-replication and sub-replication prices.

4. **Arbitrage manifests as the impossibility of positive state prices.** If no strictly positive probability vector satisfies $X^T q = 0$, the [Separating Hyperplane Theorem](separating_hyperplane_theorem.md) constructively produces the arbitrage portfolio as the separating direction.

These finite-dimensional results carry over to continuous-time models in a natural way, with the linear algebra replaced by functional analysis. The [FTAP page](fundamental_theorem_of_asset_pricing.md) discusses this extension under the heading of NFLVR and the Delbaen--Schachermayer theorem.

---

## Exercises

**Exercise 1.** Consider a two-state market with one risky asset: $S^1_0 = 80$, $S^1_1(\omega_1) = 100$, $S^1_1(\omega_2) = 70$. Find the unique EMM and use it to price a European put option with strike $K = 85$.

---

**Exercise 2.** In a three-state market with one risky asset, $S^1_0 = 50$, $S^1_1 = (70, 55, 35)$, parameterize the family of EMMs. Compute the no-arbitrage price interval for a butterfly spread with payoff $\Phi = (0, 10, 0)$. Is this claim attainable?

---

**Exercise 3.** Consider a market with $n = 3$ states and $d = 2$ risky assets with payoff matrix

$$
X = \begin{pmatrix} 15 & 8 \\ -5 & 2 \\ -10 & -6 \end{pmatrix}
$$

Determine whether the market is arbitrage-free. If so, find the unique EMM and verify it satisfies the martingale condition for both assets.

---

**Exercise 4.** A three-state market has one risky asset and $\operatorname{rank}(X) = 1$. A second risky asset is added with payoff vector $(a, b, c)^T$ and initial price $S^2_0$. What conditions on $(a, b, c)$ ensure that the augmented payoff matrix has rank 2? Under what additional condition on $S^2_0$ does the augmented market remain arbitrage-free?

---

**Exercise 5.** In Example 4 of this section, the payoff matrix $X$ has rank 2 but the market admits arbitrage. Explain why high rank alone does not guarantee the absence of arbitrage. What specific property of the columns causes the EMM to require $q_1 = 0$?

---

**Exercise 6.** Consider a two-state market with $d = 2$ risky assets: $S^1_0 = 20$, $S^1_1 = (25, 16)$, $S^2_0 = 10$, $S^2_1 = (13, 8)$. Check whether $\operatorname{rank}(X) = n - 1 = 1$. If not, is one of the assets redundant? Find the EMM and price the claim $\Phi = (5, 0)$.

---


## Solutions


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


??? success "Solution to Exercise 5"
    In Example 4, the payoff matrix has $\operatorname{rank}(X) = 2 = n - 1 = 2$, which is the rank condition for completeness. However, the market admits arbitrage because the system $X^T q = 0$ with $\sum q_i = 1$ and $q_i > 0$ has no solution -- it forces $q_1 = 0$.

    **Why high rank alone is insufficient:** The rank condition $\operatorname{rank}(X) = n - 1$ is necessary for completeness, but completeness also requires no-arbitrage as a prerequisite. The Second FTAP states: "In an **arbitrage-free** market, completeness $\iff$ unique EMM." If no EMM exists at all, the market has arbitrage and the question of completeness is moot.

    **What causes $q_1 = 0$:** The two columns of $X$ are

    $$
    X^{(1)} = (10, 5, -5)^T, \qquad X^{(2)} = (5, 2, -2)^T
    $$

    In states $\omega_2$ and $\omega_3$, the ratio $X^{(1)}_i / X^{(2)}_i$ is $5/2 = (-5)/(-2) = 2.5$ for both states. But in state $\omega_1$, the ratio is $10/5 = 2$. This means the linear combination $X^{(1)} - 2X^{(2)} = (0, 1, -1)^T$ is non-negative in states 2 and 3, while being zero in state 1. The further combination that makes states 2 and 3 net out forces state 1 to have the "free" profit. The system $X^T q = 0$ effectively requires $q_1(10 - 2 \cdot 5) = 0$, and since the coefficient $(10 - 2 \cdot 5) = 0$ is trivially satisfied, the additional constraint from the second equation forces $q_1 = 0$. The inconsistency in the return ratios across states makes it impossible to find a strictly positive pricing vector.


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
