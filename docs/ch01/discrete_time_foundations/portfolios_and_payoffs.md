# Portfolios and Payoffs

Having established the one-period market model and its probability space in the [previous section](one_period_market_model.md), we now formalize how investors interact with this market through portfolios. In the one-period model, investors make decisions at time $t = 0$ by choosing how many units of each available asset to hold. This choice --- a **portfolio** --- determines the investor's exposure to each possible future state of the world. The resulting terminal wealth, or **payoff**, depends on which state is realized at time $t = 1$. Understanding the set of all achievable payoffs is central to pricing, hedging, and the notion of market completeness that we will develop throughout this chapter.

!!! abstract "Learning Objectives: Portfolios, Payoffs, and Attainability"
    After completing this section, you should be able to:

    - Define a portfolio and compute its initial cost and terminal payoff
    - Construct the payoff matrix for a given market model
    - Determine the attainable set and check whether a given claim is attainable
    - Relate the rank of the payoff matrix to market completeness
    - Distinguish between long and short positions and interpret their financial meaning

---

## Roadmap

This page introduces the following concepts, building directly on the one-period market model:

- **Portfolios**: a vector of holdings across the available assets
- **Portfolio cost**: the initial outlay required to form a portfolio
- **Payoffs**: the state-contingent terminal value of a portfolio
- **The payoff matrix**: the matrix whose columns encode each asset's terminal values
- **The attainable set**: the subspace of payoffs reachable by trading
- **Linear pricing**: the linearity of the cost and payoff maps

---

## Market Setup and Notation

We work within the one-period market model established in the [One-Period Market Model](one_period_market_model.md) page. The economy has two dates, $t = 0$ (today) and $t = 1$ (the future), and a finite state space $\Omega = \{\omega_1, \omega_2, \ldots, \omega_K\}$ of $K$ possible states at time $t = 1$.

There are $d + 1$ traded assets indexed by $j = 0, 1, \ldots, d$:

- **Asset 0** ($S^0$): the **risk-free asset** (bond or money market account). It has initial price $S^0_0 = 1$ and pays $S^0_1 = 1 + r_f$ in every state, where $r_f \geq 0$ is the one-period risk-free interest rate.
- **Assets 1 through $d$** ($S^1, \ldots, S^d$): the **risky assets**. Asset $j$ has initial price $S^j_0 > 0$ and state-contingent terminal value $S^j_1(\omega_k)$ for $k = 1, \ldots, K$.

We collect all initial prices into a vector:

$$
\mathbf{p} = (S^0_0, \, S^1_0, \, \ldots, \, S^d_0)^\top \in \mathbb{R}^{d+1}
$$

---

## Portfolio Definition

### Intuition

Before investing, an agent must decide how many units of each available asset to hold. Buying 3 shares of stock and depositing \$500 in a savings account is an example of a portfolio. Mathematically, we represent this decision as a vector whose entries record the number of units held in each asset. Entries can be negative, corresponding to short selling. This algebraic representation allows us to study trading strategies using the tools of linear algebra.

### Formal Definition

!!! info "Definition: Portfolio"
    A **portfolio** (or **trading strategy**) is a vector

    $$
    \boldsymbol{\theta} = (\theta^0, \theta^1, \ldots, \theta^d)^\top \in \mathbb{R}^{d+1}
    $$

    where $\theta^j$ denotes the number of units of asset $j$ held by the investor. The component $\theta^0$ represents the position in the risk-free asset and $\theta^1, \ldots, \theta^d$ represent positions in the risky assets.

The entries of $\boldsymbol{\theta}$ are real numbers, which means:

- **Fractional holdings** are permitted: $\theta^j = 2.5$ means holding 2.5 units of asset $j$.
- **Short positions** are permitted: $\theta^j < 0$ means the investor has sold asset $j$ short (borrowed and sold it, with an obligation to return it later).
- **Zero position**: $\theta^j = 0$ means no holdings in asset $j$.

### Long and Short Positions

!!! tip "Long vs Short"
    - A **long position** in asset $j$ means $\theta^j > 0$: the investor owns the asset and profits when its value rises.
    - A **short position** in asset $j$ means $\theta^j < 0$: the investor has sold the asset without owning it (short selling) and profits when its value falls.
    - Short selling the risk-free asset ($\theta^0 < 0$) corresponds to **borrowing** at the risk-free rate.
    - A long position in the risk-free asset ($\theta^0 > 0$) corresponds to **lending** (depositing money at the risk-free rate).

---

## Portfolio Cost

### Intuition

Forming a portfolio requires an initial outlay: the investor must pay the market price for each unit of each asset purchased. The total cost at time $t = 0$ is the sum of the quantities held times their respective prices. This cost represents the investor's initial wealth commitment to the portfolio.

### Formal Definition

!!! info "Definition: Portfolio Cost (Initial Value)"
    The **cost** (or **initial value**) of a portfolio $\boldsymbol{\theta}$ is

    $$
    V_0(\boldsymbol{\theta}) = \sum_{j=0}^{d} \theta^j S^j_0 = \boldsymbol{\theta}^\top \mathbf{p}
    $$

    This is the inner product of the portfolio vector with the price vector.

The cost $V_0(\boldsymbol{\theta})$ can be positive, zero, or negative:

- $V_0(\boldsymbol{\theta}) > 0$: the investor pays a net amount to form the portfolio.
- $V_0(\boldsymbol{\theta}) = 0$: the portfolio is **self-financing at inception** --- long positions are funded entirely by short positions.
- $V_0(\boldsymbol{\theta}) < 0$: the investor receives a net cash inflow at time $t = 0$.

---

## Payoff of a Portfolio

### Intuition

Once the portfolio is formed at $t = 0$, the investor holds it until $t = 1$, when the uncertainty resolves. Each asset delivers its terminal value depending on which state $\omega_k$ is realized. The portfolio payoff is the total terminal wealth: the sum of all asset payoffs weighted by the number of units held.

### Formal Definition

!!! info "Definition: Portfolio Payoff"
    The **payoff** (or **terminal value**) of a portfolio $\boldsymbol{\theta}$ in state $\omega_k$ is

    $$
    V_1(\boldsymbol{\theta}, \omega_k) = \sum_{j=0}^{d} \theta^j S^j_1(\omega_k)
    $$

    The payoff across all states defines a random variable $V_1(\boldsymbol{\theta}) : \Omega \to \mathbb{R}$, which we can represent as a vector in $\mathbb{R}^K$:

    $$
    V_1(\boldsymbol{\theta}) = \bigl(V_1(\boldsymbol{\theta}, \omega_1), \, V_1(\boldsymbol{\theta}, \omega_2), \, \ldots, \, V_1(\boldsymbol{\theta}, \omega_K)\bigr)^\top
    $$

The payoff $V_1(\boldsymbol{\theta})$ tells us how much the investor will receive (or owe) in each possible state. This is the object that pricing theory ultimately aims to value.

---

## The Payoff Matrix

### Intuition

To study all possible payoffs simultaneously, we organize the terminal values of every asset in every state into a single matrix. Each row of this matrix corresponds to a state, and each column corresponds to an asset. Multiplying this matrix by a portfolio vector produces the payoff vector, making the payoff map a simple matrix-vector product.

### Formal Definition

!!! info "Definition: Payoff Matrix"
    The **payoff matrix** $\mathbf{D} \in \mathbb{R}^{K \times (d+1)}$ has entries

    $$
    D_{kj} = S^j_1(\omega_k)
    $$

    for $k = 1, \ldots, K$ (states) and $j = 0, 1, \ldots, d$ (assets). Explicitly:

    $$
    \mathbf{D} = \begin{pmatrix} S^0_1(\omega_1) & S^1_1(\omega_1) & \cdots & S^d_1(\omega_1) \\ S^0_1(\omega_2) & S^1_1(\omega_2) & \cdots & S^d_1(\omega_2) \\ \vdots & \vdots & \ddots & \vdots \\ S^0_1(\omega_K) & S^1_1(\omega_K) & \cdots & S^d_1(\omega_K) \end{pmatrix}
    $$

Since $S^0_1(\omega_k) = 1 + r_f$ for all $k$, the first column of $\mathbf{D}$ is the constant vector $(1 + r_f) \, \mathbf{1}_K$.

With this notation, the payoff of a portfolio $\boldsymbol{\theta}$ is:

$$
V_1(\boldsymbol{\theta}) = \mathbf{D} \boldsymbol{\theta}
$$

This compact matrix expression is the key formula that connects portfolios to payoffs.

---

## The Payoff Map and Linearity

### The Payoff Map

The mapping from portfolios to payoffs is given by

$$
\Phi : \mathbb{R}^{d+1} \to \mathbb{R}^K, \quad \Phi(\boldsymbol{\theta}) = \mathbf{D} \boldsymbol{\theta}
$$

This is the **payoff map**. It takes a portfolio and returns the vector of state-contingent terminal values.

### Linearity of the Payoff Map

!!! success "Proposition: Linearity of the Payoff Map"
    The payoff map $\Phi$ is a **linear map**. That is, for any portfolios $\boldsymbol{\theta}, \boldsymbol{\eta} \in \mathbb{R}^{d+1}$ and any scalar $\alpha \in \mathbb{R}$:

    1. **Additivity**: $\Phi(\boldsymbol{\theta} + \boldsymbol{\eta}) = \Phi(\boldsymbol{\theta}) + \Phi(\boldsymbol{\eta})$
    2. **Homogeneity**: $\Phi(\alpha \boldsymbol{\theta}) = \alpha \, \Phi(\boldsymbol{\theta})$

**Proof.** Both properties follow directly from the linearity of matrix multiplication:

1. $\Phi(\boldsymbol{\theta} + \boldsymbol{\eta}) = \mathbf{D}(\boldsymbol{\theta} + \boldsymbol{\eta}) = \mathbf{D}\boldsymbol{\theta} + \mathbf{D}\boldsymbol{\eta} = \Phi(\boldsymbol{\theta}) + \Phi(\boldsymbol{\eta})$
2. $\Phi(\alpha \boldsymbol{\theta}) = \mathbf{D}(\alpha \boldsymbol{\theta}) = \alpha \, \mathbf{D}\boldsymbol{\theta} = \alpha \, \Phi(\boldsymbol{\theta})$

$\square$

### Linearity of the Cost Functional

!!! success "Proposition: Linearity of Portfolio Cost"
    The cost functional $V_0 : \mathbb{R}^{d+1} \to \mathbb{R}$ defined by $V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{p}$ is a **linear functional**:

    1. $V_0(\boldsymbol{\theta} + \boldsymbol{\eta}) = V_0(\boldsymbol{\theta}) + V_0(\boldsymbol{\eta})$
    2. $V_0(\alpha \boldsymbol{\theta}) = \alpha \, V_0(\boldsymbol{\theta})$

**Proof.** Immediate from the linearity of the inner product:

$$
V_0(\boldsymbol{\theta} + \boldsymbol{\eta}) = (\boldsymbol{\theta} + \boldsymbol{\eta})^\top \mathbf{p} = \boldsymbol{\theta}^\top \mathbf{p} + \boldsymbol{\eta}^\top \mathbf{p} = V_0(\boldsymbol{\theta}) + V_0(\boldsymbol{\eta})
$$

$\square$

!!! tip "Financial Interpretation of Linearity"
    Linearity of the cost functional means that the **price of a portfolio equals the portfolio of prices**. There are no transaction costs, no price impact, and no constraints on trade sizes in this model. This is a simplifying assumption that underlies the entire theory. In practice, transaction costs and market frictions break this linearity.

---

## The Attainable Set

### Intuition

Not every conceivable payoff pattern across states can be achieved by trading the available assets. The set of payoffs that *can* be generated by some portfolio is called the attainable set. Since the payoff map is linear, this set has the structure of a linear subspace of $\mathbb{R}^K$. The dimension of this subspace determines how "rich" the market is in terms of the payoff profiles it can produce.

### Formal Definition

!!! info "Definition: Attainable Set"
    The **attainable set** (or **marketed subspace**) is the set of all payoffs achievable by some portfolio:

    $$
    \mathcal{M} = \{ \mathbf{D}\boldsymbol{\theta} : \boldsymbol{\theta} \in \mathbb{R}^{d+1} \} = \operatorname{Im}(\mathbf{D})
    $$

    This is the **column space** (image) of the payoff matrix $\mathbf{D}$.

### Structure of the Attainable Set

!!! success "Proposition: The Attainable Set is a Linear Subspace"
    The attainable set $\mathcal{M}$ is a linear subspace of $\mathbb{R}^K$ with

    $$
    \dim(\mathcal{M}) = \operatorname{rank}(\mathbf{D}) \leq \min(d + 1, K)
    $$

**Proof.** The attainable set $\mathcal{M} = \operatorname{Im}(\mathbf{D})$ is the image of a linear map, which is always a linear subspace. To verify directly:

- **Contains the zero vector**: $\mathbf{D} \cdot \mathbf{0} = \mathbf{0} \in \mathcal{M}$.
- **Closed under addition**: If $\mathbf{y}_1 = \mathbf{D}\boldsymbol{\theta}_1 \in \mathcal{M}$ and $\mathbf{y}_2 = \mathbf{D}\boldsymbol{\theta}_2 \in \mathcal{M}$, then $\mathbf{y}_1 + \mathbf{y}_2 = \mathbf{D}(\boldsymbol{\theta}_1 + \boldsymbol{\theta}_2) \in \mathcal{M}$.
- **Closed under scalar multiplication**: If $\mathbf{y} = \mathbf{D}\boldsymbol{\theta} \in \mathcal{M}$ and $\alpha \in \mathbb{R}$, then $\alpha \mathbf{y} = \mathbf{D}(\alpha\boldsymbol{\theta}) \in \mathcal{M}$.

The dimension equals $\operatorname{rank}(\mathbf{D})$ by the rank-nullity theorem, and the rank is bounded by the minimum of the number of rows and columns. $\square$

### Attainability and Market Completeness

A contingent claim $\mathbf{c} = (c_1, \ldots, c_K)^\top \in \mathbb{R}^K$ is **attainable** (or **replicable**) if $\mathbf{c} \in \mathcal{M}$, that is, if there exists a portfolio $\boldsymbol{\theta}$ such that $\mathbf{D}\boldsymbol{\theta} = \mathbf{c}$.

!!! info "Definition: Complete Market"
    The market is **complete** if every contingent claim is attainable:

    $$
    \mathcal{M} = \mathbb{R}^K
    $$

    This requires $\operatorname{rank}(\mathbf{D}) = K$, which in turn requires at least $K$ assets: $d + 1 \geq K$.

When the market is incomplete ($\operatorname{rank}(\mathbf{D}) < K$), some contingent claims cannot be replicated by any portfolio of the traded assets. This has deep consequences for pricing, which are explored in the [Arrow-Debreu Securities and State Prices](state_prices_arrow_debreu.md) section and the [Complete Markets and Uniqueness](../fundamental_theorem_of_asset_pricing/complete_markets_and_uniqueness.md) section.

---

## Worked Example: A Two-Asset, Three-State Model

Consider a market with $K = 3$ states and $d + 1 = 2$ assets (one risk-free bond and one risky stock).

**Market data:**

| | $t = 0$ price | $\omega_1$ (Boom) | $\omega_2$ (Flat) | $\omega_3$ (Bust) |
|:---|:---:|:---:|:---:|:---:|
| Bond ($S^0$) | \$1.00 | \$1.05 | \$1.05 | \$1.05 |
| Stock ($S^1$) | \$10.00 | \$14.00 | \$10.50 | \$7.00 |

Here $r_f = 0.05$ (5% risk-free rate).

**Step 1: Write down the price vector and payoff matrix.**

$$
\mathbf{p} = \begin{pmatrix} 1 \\ 10 \end{pmatrix}, \qquad \mathbf{D} = \begin{pmatrix} 1.05 & 14 \\ 1.05 & 10.5 \\ 1.05 & 7 \end{pmatrix}
$$

**Step 2: Choose a portfolio and compute its cost and payoff.**

Suppose an investor goes long 3 shares of stock and borrows \$20 at the risk-free rate. This corresponds to $\boldsymbol{\theta} = (-20, \, 3)^\top$.

*Initial cost:*

$$
V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{p} = (-20)(1) + (3)(10) = -20 + 30 = \$10
$$

The investor pays \$10 out of pocket (borrows \$20, uses it plus \$10 of own money to buy \$30 worth of stock).

*Payoff in each state:*

$$
V_1(\boldsymbol{\theta}) = \mathbf{D}\boldsymbol{\theta} = \begin{pmatrix} 1.05 & 14 \\ 1.05 & 10.5 \\ 1.05 & 7 \end{pmatrix} \begin{pmatrix} -20 \\ 3 \end{pmatrix} = \begin{pmatrix} -21 + 42 \\ -21 + 31.5 \\ -21 + 21 \end{pmatrix} = \begin{pmatrix} 21 \\ 10.5 \\ 0 \end{pmatrix}
$$

| State | Bond repayment | Stock proceeds | Net payoff |
|:---|:---:|:---:|:---:|
| Boom ($\omega_1$) | $-\$21.00$ | $+\$42.00$ | $\$21.00$ |
| Flat ($\omega_2$) | $-\$21.00$ | $+\$31.50$ | $\$10.50$ |
| Bust ($\omega_3$) | $-\$21.00$ | $+\$21.00$ | $\$0.00$ |

The investor profits in boom and flat states but breaks even in the bust state. The leverage (borrowing) amplifies both gains and losses relative to a fully funded position.

**Step 3: Characterize the attainable set.**

The payoff matrix $\mathbf{D}$ has 2 columns and 3 rows, so:

$$
\operatorname{rank}(\mathbf{D}) \leq \min(2, 3) = 2
$$

The two columns $(1.05, 1.05, 1.05)^\top$ and $(14, 10.5, 7)^\top$ are linearly independent (since the second is not a scalar multiple of the first), so $\operatorname{rank}(\mathbf{D}) = 2$.

The attainable set $\mathcal{M}$ is a **2-dimensional subspace** of $\mathbb{R}^3$, which is a plane through the origin. Since $\dim(\mathcal{M}) = 2 < 3 = K$, the market is **incomplete**: there exist contingent claims in $\mathbb{R}^3$ that cannot be replicated.

**Step 4: Check attainability of a specific claim.**

Is the claim $\mathbf{c} = (1, 0, 0)^\top$ (an Arrow-Debreu security paying \$1 only in the boom state) attainable?

We need to solve $\mathbf{D}\boldsymbol{\theta} = \mathbf{c}$:

$$
\begin{pmatrix} 1.05 & 14 \\ 1.05 & 10.5 \\ 1.05 & 7 \end{pmatrix} \begin{pmatrix} \theta^0 \\ \theta^1 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
$$

From the second and third equations:

$$
1.05 \, \theta^0 + 10.5 \, \theta^1 = 0 \quad \text{and} \quad 1.05 \, \theta^0 + 7 \, \theta^1 = 0
$$

Subtracting: $3.5 \, \theta^1 = 0$, so $\theta^1 = 0$, and then $\theta^0 = 0$. But $\mathbf{D}(0, 0)^\top = (0, 0, 0)^\top \neq (1, 0, 0)^\top$. The system is inconsistent, confirming that $\mathbf{c} \notin \mathcal{M}$.

This Arrow-Debreu security **cannot** be replicated with only a bond and a stock --- a third independent asset would be needed to complete the market.

---

## Net Payoff and Return

For many applications it is useful to work with the **net payoff** (profit/loss) and the **return** of a portfolio.

!!! info "Definition: Net Payoff and Return"
    The **net payoff** of a portfolio $\boldsymbol{\theta}$ in state $\omega_k$ is the profit or loss relative to the initial cost:

    $$
    \Pi(\boldsymbol{\theta}, \omega_k) = V_1(\boldsymbol{\theta}, \omega_k) - V_0(\boldsymbol{\theta})
    $$

    When $V_0(\boldsymbol{\theta}) \neq 0$, the **gross return** is

    $$
    R(\boldsymbol{\theta}, \omega_k) = \frac{V_1(\boldsymbol{\theta}, \omega_k)}{V_0(\boldsymbol{\theta})}
    $$

    and the **net return** is $R(\boldsymbol{\theta}, \omega_k) - 1$.

For the portfolio in the worked example above ($\boldsymbol{\theta} = (-20, 3)^\top$ with $V_0 = \$10$):

| State | Net payoff | Net return |
|:---|:---:|:---:|
| Boom | $\$21 - \$10 = \$11$ | $110\%$ |
| Flat | $\$10.50 - \$10 = \$0.50$ | $5\%$ |
| Bust | $\$0 - \$10 = -\$10$ | $-100\%$ |

The leveraged portfolio earns 110% in the boom but loses 100% (the entire initial investment) in the bust. For comparison, the risk-free bond returns exactly 5% in every state.

---

## Redundant Assets

An asset is **redundant** if its payoff vector can be replicated by a portfolio of the other assets. Formally, asset $j$ is redundant if the $j$-th column of $\mathbf{D}$ lies in the span of the remaining columns. Removing a redundant asset does not change the attainable set.

!!! success "Proposition: Redundant Assets and the Attainable Set"
    Let $\mathbf{D}$ be the payoff matrix for $d + 1$ assets and let $\widetilde{\mathbf{D}}$ be the matrix obtained by removing a redundant column. Then

    $$
    \operatorname{Im}(\mathbf{D}) = \operatorname{Im}(\widetilde{\mathbf{D}})
    $$

    In particular, $\operatorname{rank}(\mathbf{D}) = \operatorname{rank}(\widetilde{\mathbf{D}})$.

**Proof.** Since the removed column lies in the span of the remaining columns, any linear combination involving it can be rewritten using the remaining columns alone. Therefore the image is unchanged. $\square$

This result implies that what matters for the richness of the market is not the total number of assets but the number of **linearly independent** payoff vectors. A market with 100 assets whose payoff vectors span only a 3-dimensional subspace of $\mathbb{R}^K$ is no more complete than a market with just 3 well-chosen assets.

---

## Summary

| Concept | Definition | Key Formula |
|:---|:---|:---|
| Portfolio | Vector of asset holdings | $\boldsymbol{\theta} \in \mathbb{R}^{d+1}$ |
| Portfolio cost | Initial outlay at $t = 0$ | $V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{p}$ |
| Payoff | Terminal value at $t = 1$ | $V_1(\boldsymbol{\theta}) = \mathbf{D}\boldsymbol{\theta}$ |
| Payoff matrix | Asset payoffs across states | $D_{kj} = S^j_1(\omega_k)$ |
| Attainable set | Payoffs reachable by trading | $\mathcal{M} = \operatorname{Im}(\mathbf{D})$ |
| Complete market | Every claim is attainable | $\operatorname{rank}(\mathbf{D}) = K$ |
| Linear pricing | Price of portfolio = portfolio of prices | $V_0(\boldsymbol{\theta} + \boldsymbol{\eta}) = V_0(\boldsymbol{\theta}) + V_0(\boldsymbol{\eta})$ |

With the portfolio and payoff structure in place, the [next section](arbitrage_and_dominance.md) introduces the concept of arbitrage and establishes when market prices are consistent with the absence of free profit opportunities.
