# Portfolios and Payoffs

The [previous page](one_period_market_model.md) fixed the environment:
states, prices $\mathbf{P}$, payoff matrix $\mathbf{X}$, and the risk-free
bond. This page introduces the **trading mechanics** that operate inside
that environment. Investors choose a **portfolio** $\boldsymbol{\theta}$ at
$t = 0$, pay an initial cost $\boldsymbol{\theta}^\top \mathbf{P}$, and
receive a state-contingent **payoff** $\mathbf{X}^\top \boldsymbol{\theta}$
at $t = 1$. The central observation of this page is that both maps are
**linear**, so the whole trading structure is an exercise in linear algebra.

This linearity is the technical engine behind the rest of the chapter: it
makes no-arbitrage a statement about a linear subspace and the
non-negative orthant, and it is what allows the
[FTAP](arbitrage_and_dominance.md) to express asset prices as a linear
functional of payoffs.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Define a portfolio and compute its initial cost and terminal payoff
    - Recognise the payoff map $\boldsymbol{\theta} \mapsto \mathbf{X}^\top\boldsymbol{\theta}$ and the cost functional $\boldsymbol{\theta} \mapsto \boldsymbol{\theta}^\top \mathbf{P}$ as linear maps
    - Determine the attainable set and check whether a given claim is attainable
    - Relate the rank of the payoff matrix to market completeness
    - Distinguish long and short positions and interpret their financial meaning

---

## Notation (recall)

Recall (see [§ One-Period Market Model](one_period_market_model.md)): the
market has finite state space $\Omega = \{\omega_1, \ldots, \omega_S\}$,
$N$ traded assets with price vector $\mathbf{P} \in \mathbb{R}^N$ and
payoff matrix $\mathbf{X} \in \mathbb{R}^{N \times S}$, where row $j$ of
$\mathbf{X}$ gives the payoff of asset $j$ across states. One of the
assets is a risk-free bond with constant payoff $1 + r_f$ and price $1$;
the discount factor is $\beta = 1/(1+r_f)$. We use this notation
throughout without redefinition.

---

## Portfolio Definition

### Intuition

Before investing, an agent must decide how many units of each available asset to hold. Buying 3 shares of stock and depositing \$500 in a savings account is an example of a portfolio. Mathematically, we represent this decision as a vector whose entries record the number of units held in each asset. Entries can be negative, corresponding to short selling. This algebraic representation allows us to study trading strategies using the tools of linear algebra.

### Formal Definition

!!! info "Definition: Portfolio"
    A **portfolio** (or **trading strategy**) is a vector

    $$
    \boldsymbol{\theta} = (\theta_1, \theta_2, \ldots, \theta_N)^\top \in \mathbb{R}^{N}
    $$

    where $\theta_j$ denotes the number of units of asset $j$ held by the investor.

The entries of $\boldsymbol{\theta}$ are real numbers, which means:

- **Fractional holdings** are permitted: $\theta_j = 2.5$ means holding 2.5 units of asset $j$.
- **Short positions** are permitted: $\theta_j < 0$ means the investor has sold asset $j$ short (borrowed and sold it, with an obligation to return it later).
- **Zero position**: $\theta_j = 0$ means no holdings in asset $j$.

### Long and Short Positions

!!! tip "Long vs Short"

    - A **long position** in asset $j$ means $\theta_j > 0$: the investor owns the asset and profits when its value rises.
    - A **short position** in asset $j$ means $\theta_j < 0$: the investor has sold the asset without owning it (short selling) and profits when its value falls.
    - Short selling the risk-free bond corresponds to **borrowing** at the risk-free rate; a long position corresponds to **lending**.

---

## Portfolio Cost and Payoff

### Intuition

Forming a portfolio requires an initial outlay at $t = 0$ — the market price of each unit purchased, summed over assets. At $t = 1$, once the state $\omega_s$ is realised, the portfolio pays the corresponding linear combination of asset payoffs. Both the cost and the payoff are inner products against the data $(\mathbf{P}, \mathbf{X})$ fixed by the one-period model.

### Formal Definition

!!! info "Definition: Cost and Payoff of a Portfolio"
    Given the price vector $\mathbf{P} \in \mathbb{R}^N$ and payoff matrix $\mathbf{X} \in \mathbb{R}^{N \times S}$ from [§ One-Period Market Model](one_period_market_model.md), the **cost** of a portfolio $\boldsymbol{\theta}$ at $t = 0$ is

    $$
    V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{P} = \sum_{j=1}^{N} \theta_j P_j
    $$

    and its **payoff** at $t = 1$ is the vector in $\mathbb{R}^S$

    $$
    V_1(\boldsymbol{\theta}) = \mathbf{X}^\top \boldsymbol{\theta}, \qquad V_1(\boldsymbol{\theta})_s = \sum_{j=1}^{N} \theta_j X_{js}
    $$

The cost $V_0(\boldsymbol{\theta})$ can be positive, zero, or negative:

- $V_0(\boldsymbol{\theta}) > 0$: the investor pays a net amount to form the portfolio.
- $V_0(\boldsymbol{\theta}) = 0$: the portfolio is **self-financing at inception** — long positions are funded entirely by short positions.
- $V_0(\boldsymbol{\theta}) < 0$: the investor receives a net cash inflow at $t = 0$.

The payoff $V_1(\boldsymbol{\theta}) \in \mathbb{R}^S$ records the terminal wealth in each state, the object that pricing theory ultimately aims to value.

---

## Linearity of Cost and Payoff

The compact matrix expressions
$V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{P}$ and
$V_1(\boldsymbol{\theta}) = \mathbf{X}^\top \boldsymbol{\theta}$ make the
following almost a tautology, but it is the structural backbone of the rest
of the chapter.

!!! success "Proposition: Linearity of Cost and Payoff"
    For any portfolios $\boldsymbol{\theta}, \boldsymbol{\eta} \in \mathbb{R}^{N}$ and any scalar $\alpha \in \mathbb{R}$:

    1. $V_0(\boldsymbol{\theta} + \boldsymbol{\eta}) = V_0(\boldsymbol{\theta}) + V_0(\boldsymbol{\eta})$ and $V_0(\alpha\boldsymbol{\theta}) = \alpha V_0(\boldsymbol{\theta})$
    2. $V_1(\boldsymbol{\theta} + \boldsymbol{\eta}) = V_1(\boldsymbol{\theta}) + V_1(\boldsymbol{\eta})$ and $V_1(\alpha\boldsymbol{\theta}) = \alpha V_1(\boldsymbol{\theta})$

**Proof.** Both follow directly from the linearity of matrix multiplication and inner products:

$$
V_0(\alpha\boldsymbol{\theta} + \boldsymbol{\eta}) = (\alpha\boldsymbol{\theta} + \boldsymbol{\eta})^\top \mathbf{P} = \alpha\boldsymbol{\theta}^\top \mathbf{P} + \boldsymbol{\eta}^\top \mathbf{P}
$$

$$
V_1(\alpha\boldsymbol{\theta} + \boldsymbol{\eta}) = \mathbf{X}^\top(\alpha\boldsymbol{\theta} + \boldsymbol{\eta}) = \alpha\mathbf{X}^\top \boldsymbol{\theta} + \mathbf{X}^\top \boldsymbol{\eta}
$$

$\square$

!!! tip "Financial Interpretation of Linearity"
    Linearity of the cost functional means the **price of a portfolio equals the portfolio of prices**: there are no transaction costs, no price impact, and no position limits. This frictionless-markets assumption is the linear-algebraic basis for everything that follows. In practice, transaction costs and market frictions break this linearity.

---

## The Attainable Set

### Intuition

Not every conceivable payoff pattern across states can be achieved by trading the available assets. The set of payoffs that *can* be generated by some portfolio is called the attainable set. Since the payoff map is linear, this set has the structure of a linear subspace of $\mathbb{R}^S$. The dimension of this subspace measures how "rich" the market is in terms of the payoff profiles it can produce.

### Formal Definition

!!! info "Definition: Attainable Set"
    The **attainable set** (or **marketed subspace**) is the set of all payoffs achievable by some portfolio:

    $$
    \mathcal{M} = \{ \mathbf{X}^\top \boldsymbol{\theta} : \boldsymbol{\theta} \in \mathbb{R}^{N} \} = \operatorname{Im}(\mathbf{X}^\top)
    $$

    This is the **column space** (image) of $\mathbf{X}^\top$, equivalently the row space of $\mathbf{X}$.

### Structure of the Attainable Set

!!! success "Proposition: The Attainable Set is a Linear Subspace"
    The attainable set $\mathcal{M}$ is a linear subspace of $\mathbb{R}^S$ with

    $$
    \dim(\mathcal{M}) = \operatorname{rank}(\mathbf{X}) \leq \min(N, S)
    $$

**Proof.** $\mathcal{M} = \operatorname{Im}(\mathbf{X}^\top)$ is the image of a linear map, hence a linear subspace. Its dimension equals $\operatorname{rank}(\mathbf{X}^\top) = \operatorname{rank}(\mathbf{X})$, which is bounded by the smaller of the matrix dimensions. $\square$

### Attainability and Market Completeness

A contingent claim $\mathbf{c} = (c_1, \ldots, c_S)^\top \in \mathbb{R}^S$ is **attainable** (or **replicable**) if $\mathbf{c} \in \mathcal{M}$, that is, if there exists a portfolio $\boldsymbol{\theta}$ such that $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{c}$.

!!! info "Definition: Complete Market"
    The market is **complete** if every contingent claim is attainable:

    $$
    \mathcal{M} = \mathbb{R}^S
    $$

    This requires $\operatorname{rank}(\mathbf{X}) = S$, which in turn requires $N \geq S$.

When the market is incomplete ($\operatorname{rank}(\mathbf{X}) < S$), some contingent claims cannot be replicated by any portfolio of the traded assets. The pricing consequences are developed in [§ State prices](state_prices_arrow_debreu.md) and the chapter on [Complete Markets and Uniqueness](../fundamental_theorem_of_asset_pricing/complete_markets_and_uniqueness.md).

---

## Worked Example: Replication and Incompleteness

This example focuses on the **mechanics** of trading: forming a portfolio,
computing its payoff, and checking whether a target claim is replicable.
(For an intuition-level walkthrough of the underlying market data see
[§ One-Period Market Model](one_period_market_model.md).)

Consider a market with $S = 3$ states (Boom, Flat, Bust) and $N = 2$ assets (bond and stock):

| Asset | $P_j$ | Boom | Flat | Bust |
|:---|:---:|:---:|:---:|:---:|
| Bond ($j=1$) | \$1.00 | \$1.05 | \$1.05 | \$1.05 |
| Stock ($j=2$) | \$10.00 | \$14.00 | \$10.50 | \$7.00 |

so $r_f = 0.05$ and

$$
\mathbf{P} = \begin{pmatrix} 1 \\ 10 \end{pmatrix}, \qquad \mathbf{X} = \begin{pmatrix} 1.05 & 1.05 & 1.05 \\ 14 & 10.5 & 7 \end{pmatrix}
$$

**Step 1: Cost and payoff of a leveraged position.**

An investor goes long 3 shares of stock and borrows \$20 at the risk-free rate, i.e. $\boldsymbol{\theta} = (-20, 3)^\top$. Then

$$
V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{P} = (-20)(1) + (3)(10) = 10
$$

$$
V_1(\boldsymbol{\theta}) = \mathbf{X}^\top \boldsymbol{\theta} = \begin{pmatrix} 1.05 & 14 \\ 1.05 & 10.5 \\ 1.05 & 7 \end{pmatrix} \begin{pmatrix} -20 \\ 3 \end{pmatrix} = \begin{pmatrix} 21 \\ 10.5 \\ 0 \end{pmatrix}
$$

| State | Bond repayment | Stock proceeds | Net payoff |
|:---|:---:|:---:|:---:|
| Boom | $-\$21.00$ | $+\$42.00$ | $\$21.00$ |
| Flat | $-\$21.00$ | $+\$31.50$ | $\$10.50$ |
| Bust | $-\$21.00$ | $+\$21.00$ | $\$0.00$ |

Leverage amplifies both upside and downside relative to a fully funded position.

**Step 2: The attainable set and incompleteness.**

The two rows of $\mathbf{X}$ — equivalently the two columns of $\mathbf{X}^\top$ — are $(1.05, 1.05, 1.05)^\top$ and $(14, 10.5, 7)^\top$. They are not proportional, so $\operatorname{rank}(\mathbf{X}) = 2$ and

$$
\dim(\mathcal{M}) = 2 < 3 = S
$$

Hence $\mathcal{M}$ is a plane through the origin in $\mathbb{R}^3$ and the market is **incomplete**.

**Step 3: A non-attainable claim.**

The Arrow–Debreu claim $\mathbf{c} = (1, 0, 0)^\top$ (paying \$1 only in Boom) requires solving $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{c}$, i.e.

$$
\begin{pmatrix} 1.05 & 14 \\ 1.05 & 10.5 \\ 1.05 & 7 \end{pmatrix}\begin{pmatrix} \theta_1 \\ \theta_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
$$

Subtracting row 3 from row 2 gives $3.5\,\theta_2 = 0$, hence $\theta_2 = 0$ and then $\theta_1 = 0$, contradicting row 1. The system is inconsistent: $\mathbf{c} \notin \mathcal{M}$. Completing the market would require a third linearly independent asset.

---

## Net Payoff and Return

For many applications it is useful to work with the **net payoff** (profit/loss) and the **return** of a portfolio.

!!! info "Definition: Net Payoff and Return"
    The **net payoff** of a portfolio $\boldsymbol{\theta}$ in state $\omega_s$ is the profit or loss relative to the initial cost:

    $$
    \Pi(\boldsymbol{\theta}, \omega_s) = V_1(\boldsymbol{\theta})_s - V_0(\boldsymbol{\theta})
    $$

    When $V_0(\boldsymbol{\theta}) \neq 0$, the **gross return** is

    $$
    R(\boldsymbol{\theta}, \omega_s) = \frac{V_1(\boldsymbol{\theta})_s}{V_0(\boldsymbol{\theta})}
    $$

    and the **net return** is $R(\boldsymbol{\theta}, \omega_s) - 1$.

For the worked-example portfolio ($\boldsymbol{\theta} = (-20, 3)^\top$ with $V_0 = \$10$):

| State | Net payoff | Net return |
|:---|:---:|:---:|
| Boom | $\$21 - \$10 = \$11$ | $110\%$ |
| Flat | $\$10.50 - \$10 = \$0.50$ | $5\%$ |
| Bust | $\$0 - \$10 = -\$10$ | $-100\%$ |

Leverage earns 110% in the boom but loses the entire initial investment in the bust; the bond returns exactly 5% in every state.

---

## Redundant Assets

An asset is **redundant** if its payoff vector can be replicated by a portfolio of the other assets. Formally, asset $j$ is redundant if row $j$ of $\mathbf{X}$ lies in the span of the remaining rows. Removing a redundant asset does not change the attainable set.

!!! success "Proposition: Redundant Assets and the Attainable Set"
    Let $\mathbf{X}$ be the payoff matrix for $N$ assets and let $\widetilde{\mathbf{X}}$ be the matrix obtained by removing a redundant row. Then

    $$
    \operatorname{Im}(\mathbf{X}^\top) = \operatorname{Im}(\widetilde{\mathbf{X}}^\top), \qquad \operatorname{rank}(\mathbf{X}) = \operatorname{rank}(\widetilde{\mathbf{X}})
    $$

**Proof.** Since the removed row lies in the span of the remaining rows, any portfolio combination involving the redundant asset can be replaced by an equivalent combination of the others, leaving the image unchanged. $\square$

What matters for the richness of the market is therefore not the total number of assets but the number of **linearly independent** payoff vectors. A market with 100 assets spanning only a 3-dimensional subspace of $\mathbb{R}^S$ is no more complete than a market with 3 well-chosen assets.

---

## Summary

| Concept | Definition | Key Formula |
|:---|:---|:---|
| Portfolio | Vector of asset holdings | $\boldsymbol{\theta} \in \mathbb{R}^{N}$ |
| Portfolio cost | Initial outlay at $t = 0$ | $V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{P}$ |
| Payoff | Terminal value at $t = 1$ | $V_1(\boldsymbol{\theta}) = \mathbf{X}^\top \boldsymbol{\theta}$ |
| Attainable set | Payoffs reachable by trading | $\mathcal{M} = \operatorname{Im}(\mathbf{X}^\top)$ |
| Complete market | Every claim is attainable | $\operatorname{rank}(\mathbf{X}) = S$ |
| Linearity | Price of portfolio = portfolio of prices | $V_0, V_1$ linear in $\boldsymbol{\theta}$ |

With the portfolio mechanics in place, [§ Arbitrage and dominance](arbitrage_and_dominance.md) introduces the economic restriction — no riskless profit — and proves the linear pricing rule $\mathbf{P} = \mathbf{X}\boldsymbol{\phi}$.

---

## Exercises

**Exercise 1.** Consider the two-asset, three-state model from the worked example. Compute the payoff vector $V_1(\boldsymbol{\theta})$ for the portfolio $\boldsymbol{\theta} = (10, -1)^\top$. In which states does the investor make a profit relative to the initial cost? In which states does the investor lose money?

??? success "Solution to Exercise 1"
    With the price vector and payoff matrix of the worked example,

    $$
    \mathbf{P} = \begin{pmatrix} 1 \\ 10 \end{pmatrix}, \qquad \mathbf{X} = \begin{pmatrix} 1.05 & 1.05 & 1.05 \\ 14 & 10.5 & 7 \end{pmatrix}
    $$

    and $\boldsymbol{\theta} = (10, -1)^\top$:

    **Initial cost:**

    $$
    V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{P} = 10(1) + (-1)(10) = 0
    $$

    **Payoff vector:**

    $$
    V_1(\boldsymbol{\theta}) = \mathbf{X}^\top \boldsymbol{\theta} = \begin{pmatrix} 1.05 & 14 \\ 1.05 & 10.5 \\ 1.05 & 7 \end{pmatrix} \begin{pmatrix} 10 \\ -1 \end{pmatrix} = \begin{pmatrix} -3.5 \\ 0 \\ 3.5 \end{pmatrix}
    $$

    Since $V_0 = 0$ the net payoff equals the payoff:

    - **Boom:** $-\$3.50$ (loss)
    - **Flat:** $\$0$ (break even)
    - **Bust:** $\$3.50$ (profit)

    The portfolio is long bonds and short stock, so it benefits when the stock performs poorly.

---

**Exercise 2.** In a market with $S = 2$ states and $N = 3$ assets (one bond and two stocks), the payoff matrix is

$$
\mathbf{X} = \begin{pmatrix} 1.05 & 1.05 \\ 12 & 9 \\ 8 & 11 \end{pmatrix}
$$

Determine $\operatorname{rank}(\mathbf{X})$ and decide whether the market is complete or incomplete.

??? success "Solution to Exercise 2"
    The matrix has $N = 3$ rows and $S = 2$ columns, so

    $$
    \operatorname{rank}(\mathbf{X}) \leq \min(3, 2) = 2
    $$

    The two columns $(1.05, 12, 8)^\top$ and $(1.05, 9, 11)^\top$ are not proportional, so $\operatorname{rank}(\mathbf{X}) = 2 = S$. The attainable set is $\mathcal{M} = \mathbb{R}^2$ and the market is **complete**.

---

**Exercise 3.** Prove that the cost functional $V_0(\boldsymbol{\theta}) = \boldsymbol{\theta}^\top \mathbf{P}$ satisfies $V_0(\alpha \boldsymbol{\theta}) = \alpha V_0(\boldsymbol{\theta})$ for all $\alpha \in \mathbb{R}$. Explain why this property implies that scaling a portfolio by a constant scales both its cost and its payoff by the same constant.

??? success "Solution to Exercise 3"
    By definition,

    $$
    V_0(\alpha\boldsymbol{\theta}) = (\alpha\boldsymbol{\theta})^\top \mathbf{P} = \alpha(\boldsymbol{\theta}^\top \mathbf{P}) = \alpha \, V_0(\boldsymbol{\theta})
    $$

    using $(\alpha \mathbf{v})^\top \mathbf{w} = \alpha(\mathbf{v}^\top \mathbf{w})$. By linearity of the payoff map,

    $$
    V_1(\alpha\boldsymbol{\theta}) = \mathbf{X}^\top(\alpha\boldsymbol{\theta}) = \alpha \, V_1(\boldsymbol{\theta})
    $$

    so both cost and payoff scale by $\alpha$ — a direct consequence of the frictionless-market assumption (no transaction costs, no price impact, no position limits).

---

**Exercise 4.** Let $\mathbf{X} \in \mathbb{R}^{N \times S}$ be the payoff matrix. Show that if $\boldsymbol{\theta}_1$ and $\boldsymbol{\theta}_2$ are two portfolios with the same payoff vector ($\mathbf{X}^\top\boldsymbol{\theta}_1 = \mathbf{X}^\top\boldsymbol{\theta}_2$), then $\boldsymbol{\theta}_1 - \boldsymbol{\theta}_2 \in \ker(\mathbf{X}^\top)$. If additionally the market satisfies the Law of One Price (see [§ Arbitrage and dominance](arbitrage_and_dominance.md)), what can you conclude about $V_0(\boldsymbol{\theta}_1)$ and $V_0(\boldsymbol{\theta}_2)$?

??? success "Solution to Exercise 4"
    Linearity gives

    $$
    \mathbf{X}^\top(\boldsymbol{\theta}_1 - \boldsymbol{\theta}_2) = \mathbf{0}
    $$

    so $\boldsymbol{\theta}_1 - \boldsymbol{\theta}_2 \in \ker(\mathbf{X}^\top)$.

    Under the Law of One Price, two portfolios with identical payoffs have identical costs, so

    $$
    V_0(\boldsymbol{\theta}_1) = \boldsymbol{\theta}_1^\top \mathbf{P} = \boldsymbol{\theta}_2^\top \mathbf{P} = V_0(\boldsymbol{\theta}_2)
    $$

    Equivalently, for any $\boldsymbol{\alpha} \in \ker(\mathbf{X}^\top)$ we must have $\boldsymbol{\alpha}^\top \mathbf{P} = 0$. The price vector $\mathbf{P}$ is therefore orthogonal to $\ker(\mathbf{X}^\top)$, i.e. lies in $\operatorname{Im}(\mathbf{X})$ — precisely the condition that the cost functional is well-defined on the attainable set.

---

**Exercise 5.** A market has $S = 3$ states and $N = 3$ assets with prices $\mathbf{P} = (1, 20, 5)^\top$ and payoff matrix

$$
\mathbf{X} = \begin{pmatrix} 1.02 & 1.02 & 1.02 \\ 25 & 20 & 15 \\ 7 & 5 & 4 \end{pmatrix}
$$

Determine whether the contingent claim $\mathbf{c} = (3, 1, 0)^\top$ is attainable. If it is, find the replicating portfolio and its cost.

??? success "Solution to Exercise 5"
    We solve $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{c}$:

    $$
    \begin{pmatrix} 1.02 & 25 & 7 \\ 1.02 & 20 & 5 \\ 1.02 & 15 & 4 \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_2 \\ \theta_3 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \\ 0 \end{pmatrix}
    $$

    Subtracting row 2 from row 1: $5\theta_2 + 2\theta_3 = 2$ (i). Subtracting row 3 from row 2: $5\theta_2 + \theta_3 = 1$ (ii). Then (i) − (ii) gives $\theta_3 = 1$, (ii) gives $\theta_2 = 0$, and row 3 gives $1.02\,\theta_1 + 4 = 0$, so $\theta_1 = -4/1.02 \approx -3.9216$.

    The claim is **attainable** with replicating portfolio $\boldsymbol{\theta} = (-4/1.02,\; 0,\; 1)^\top$, and

    $$
    V_0(\boldsymbol{\theta}) = -\tfrac{4}{1.02}(1) + 0(20) + 1(5) = -\tfrac{4}{1.02} + 5 = \tfrac{1.10}{1.02} \approx 1.0784
    $$

---

**Exercise 6.** Explain why removing a redundant asset from the market does not change the set of attainable payoffs. Give a concrete example of two assets whose payoff vectors are linearly dependent and show that removing one does not reduce $\operatorname{rank}(\mathbf{X})$.

??? success "Solution to Exercise 6"
    **Why removing a redundant asset preserves the attainable set:** An asset is redundant if its row in $\mathbf{X}$ is a linear combination of the other rows. If row $j$ satisfies $\mathbf{x}_j = \sum_{i \neq j} \alpha_i \mathbf{x}_i$, then for any portfolio $\boldsymbol{\theta}$ set $\tilde\theta_j = 0$ and $\tilde\theta_i = \theta_i + \alpha_i \theta_j$ for $i \neq j$. Then $\mathbf{X}^\top \tilde{\boldsymbol{\theta}} = \mathbf{X}^\top \boldsymbol{\theta}$, so any payoff achievable with the redundant asset is achievable without it.

    **Concrete example:** With $S = 2$ states, take a bond paying $(1.05, 1.05)$, a stock paying $(12, 6)$, and a redundant asset paying $(2.10, 2.10) = 2 \times (1.05, 1.05)$. Then

    $$
    \mathbf{X} = \begin{pmatrix} 1.05 & 1.05 \\ 12 & 6 \\ 2.10 & 2.10 \end{pmatrix}, \qquad \widetilde{\mathbf{X}} = \begin{pmatrix} 1.05 & 1.05 \\ 12 & 6 \end{pmatrix}
    $$

    Row 3 is twice row 1, so $\operatorname{rank}(\mathbf{X}) = 2 = \operatorname{rank}(\widetilde{\mathbf{X}})$, and the attainable set is unchanged.

---

**Exercise 7.** In a market with $S = 4$ states and $N = 2$ assets, what is the maximum dimension of the attainable set $\mathcal{M}$? How many additional linearly independent assets would be needed to make the market complete?

??? success "Solution to Exercise 7"
    With $\mathbf{X} \in \mathbb{R}^{2 \times 4}$,

    $$
    \dim(\mathcal{M}) = \operatorname{rank}(\mathbf{X}) \leq \min(2, 4) = 2
    $$

    Completeness requires $\dim(\mathcal{M}) = S = 4$, so at least $4 - 2 = 2$ additional linearly independent assets are needed.
