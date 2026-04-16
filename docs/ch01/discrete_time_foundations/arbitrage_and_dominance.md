# Arbitrage and Dominance

An arbitrage opportunity is a trading strategy that generates profit without
risk or net investment. This is the central impossibility condition of
mathematical finance: if markets allowed riskless profits from nothing, prices
would be driven to eliminate them, and no consistent pricing framework could
exist.

Building on the portfolio and payoff framework from the
[preceding section](portfolios_and_payoffs.md), we ask: when can an investor
construct a portfolio with zero cost and non-negative payoff that is strictly
positive somewhere? The answer to this question is the economic content of
the [First Fundamental Theorem](one_period_market_model.md). The absence of
arbitrage will imply the existence of a linear pricing rule
$\mathbf{P} = \mathbf{X}\boldsymbol{\phi}$ with $\boldsymbol{\phi} \gg 0$,
which we construct using state prices in the
[next section](state_prices_arrow_debreu.md).

!!! tip "Key insight: no-arbitrage is the only assumption needed"
    The entire pricing theory of this chapter --- state prices, risk-neutral
    measures, and discounted expectation --- follows from the single economic
    assumption that no arbitrage opportunity exists. No utility function, no
    equilibrium argument, no statistical hypothesis is required. This is why
    the FTAP is called *fundamental*: it derives probability (the
    risk-neutral measure $\mathbb{Q}$) from economics (no-arbitrage), not
    the other way around.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Define Type 1 and Type 2 arbitrage opportunities formally in a discrete one-period model
    - State the Law of One Price and prove that no-arbitrage implies it
    - Define dominance and explain its relationship to arbitrage and to positive state prices
    - Given a payoff matrix and price vector, determine whether an arbitrage opportunity exists
    - Explain the hierarchy: no-arbitrage implies no-dominance implies the Law of One Price

---

## Notation and Market Setup

We work in the one-period market model established in the [One-Period Market Model](one_period_market_model.md) page. Time runs from $t = 0$ (today) to $t = 1$ (future). At $t = 1$, exactly one of $S$ possible states $\omega_1, \omega_2, \ldots, \omega_S$ is realized. There are $N$ traded assets. Asset $j$ has price $P_j$ at $t = 0$ and delivers state-contingent payoff $X_{js}$ at $t = 1$ in state $\omega_s$.

The **price vector** and **payoff matrix** are:

$$
\mathbf{P} = \begin{pmatrix} P_1 \\ P_2 \\ \vdots \\ P_N \end{pmatrix} \in \mathbb{R}^N, \qquad \mathbf{X} = \begin{pmatrix} X_{11} & X_{12} & \cdots & X_{1S} \\ X_{21} & X_{22} & \cdots & X_{2S} \\ \vdots & \vdots & \ddots & \vdots \\ X_{N1} & X_{N2} & \cdots & X_{NS} \end{pmatrix} \in \mathbb{R}^{N \times S}
$$

A **portfolio** is a vector $\boldsymbol{\theta} = (\theta_1, \ldots, \theta_N)^\top \in \mathbb{R}^N$, where $\theta_j$ is the number of units held of asset $j$. The portfolio's cost at $t = 0$ is $\boldsymbol{\theta}^\top \mathbf{P}$, and its payoff in state $\omega_s$ is $(\mathbf{X}^\top \boldsymbol{\theta})_s = \sum_{j=1}^N \theta_j X_{js}$.

---

## Arbitrage Opportunities

### Intuition

Imagine a trader who can assemble a portfolio at zero cost (or receive cash upfront) and be guaranteed never to lose money, while having a chance of making a strict profit. Such a strategy is literally "something for nothing" or "a free lottery" -- it violates any reasonable notion of market equilibrium. If such opportunities existed, every rational agent would scale them up without limit, driving prices to adjust until the opportunity vanished. The assumption that no such strategies exist is the bedrock of asset pricing theory.

### Formal Definition

!!! info "Definition: Arbitrage Opportunity"
    A portfolio $\boldsymbol{\theta} \in \mathbb{R}^N$ is an **arbitrage opportunity** if it satisfies:

    1. $\boldsymbol{\theta}^\top \mathbf{P} \leq 0$ (costs nothing or generates cash at $t = 0$)
    2. $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$ (non-negative payoff in every state at $t = 1$)
    3. At least one of the two inequalities above is strict

    Equivalently, $\boldsymbol{\theta}$ is an arbitrage if $\boldsymbol{\theta}^\top \mathbf{P} \leq 0$, $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$, and $(\boldsymbol{\theta}^\top \mathbf{P}, \mathbf{X}^\top \boldsymbol{\theta}) \neq (0, \mathbf{0})$.

Arbitrage opportunities split naturally into two types that capture distinct ways of getting something for nothing.

### Type 1 Arbitrage (Something for Nothing)

!!! info "Definition: Type 1 Arbitrage"
    A portfolio $\boldsymbol{\theta}$ is a **Type 1 arbitrage** if:

    - $\boldsymbol{\theta}^\top \mathbf{P} = 0$ (zero net cost)
    - $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$ (non-negative payoff in every state)
    - $\mathbf{X}^\top \boldsymbol{\theta} \neq \mathbf{0}$ (strictly positive payoff in at least one state)

A Type 1 arbitrage costs nothing to enter and guarantees a non-negative payoff with a strictly positive payoff in at least one state. The trader invests zero and receives a portfolio whose payoff is non-negative everywhere and strictly positive somewhere -- literally something from nothing.

### Type 2 Arbitrage (Free Lottery)

!!! info "Definition: Type 2 Arbitrage"
    A portfolio $\boldsymbol{\theta}$ is a **Type 2 arbitrage** if:

    - $\boldsymbol{\theta}^\top \mathbf{P} < 0$ (the portfolio generates cash at $t = 0$)
    - $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$ (non-negative payoff in every state)

A Type 2 arbitrage pays the trader cash upfront while guaranteeing no future liability. The trader receives money today and faces no risk of losing money tomorrow -- a free lottery with no downside.

!!! tip "Why Distinguish the Two Types?"
    The distinction matters because the two types have different implications for pricing. Type 1 arbitrage means a zero-cost portfolio has strictly positive value in some states, which implies the market misprices relative payoffs. Type 2 arbitrage means the market misprices the overall cost of a non-negative payoff. Both are impossible in equilibrium, but detecting each requires checking different conditions. Together, they exhaust all possibilities for riskless profit.

### No-Arbitrage Condition

!!! info "Definition: No-Arbitrage"
    A market satisfies the **no-arbitrage condition** (or is **arbitrage-free**) if no portfolio $\boldsymbol{\theta} \in \mathbb{R}^N$ is an arbitrage opportunity. That is, there exists no $\boldsymbol{\theta}$ satisfying the conditions above for either Type 1 or Type 2 arbitrage.

---

## The Law of One Price

### Intuition

If two portfolios produce exactly the same payoff in every future state, they must have the same cost today. Otherwise, an investor could buy the cheaper one and sell the more expensive one, locking in a riskless profit. This simple but powerful observation is the Law of One Price.

### Formal Statement

!!! info "Definition: Law of One Price (LOP)"
    A market satisfies the **Law of One Price** if, for any two portfolios $\boldsymbol{\theta}$ and $\boldsymbol{\eta}$ with identical payoffs in every state,

    $$
    \mathbf{X}^\top \boldsymbol{\theta} = \mathbf{X}^\top \boldsymbol{\eta} \quad \Longrightarrow \quad \boldsymbol{\theta}^\top \mathbf{P} = \boldsymbol{\eta}^\top \mathbf{P}
    $$

Equivalently, the LOP holds if and only if the pricing functional is well-defined on the space of attainable payoffs: if a payoff can be generated by a portfolio, its cost is uniquely determined.

### No-Arbitrage Implies the Law of One Price

!!! success "Proposition: No-Arbitrage Implies the LOP"
    If the market is arbitrage-free, then the Law of One Price holds.

**Proof.** Suppose the LOP fails. Then there exist portfolios $\boldsymbol{\theta}$ and $\boldsymbol{\eta}$ such that $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{X}^\top \boldsymbol{\eta}$ but $\boldsymbol{\theta}^\top \mathbf{P} \neq \boldsymbol{\eta}^\top \mathbf{P}$. Without loss of generality, assume $\boldsymbol{\theta}^\top \mathbf{P} < \boldsymbol{\eta}^\top \mathbf{P}$. Define $\boldsymbol{\alpha} = \boldsymbol{\theta} - \boldsymbol{\eta}$. Then:

- Cost: $\boldsymbol{\alpha}^\top \mathbf{P} = \boldsymbol{\theta}^\top \mathbf{P} - \boldsymbol{\eta}^\top \mathbf{P} < 0$
- Payoff: $\mathbf{X}^\top \boldsymbol{\alpha} = \mathbf{X}^\top \boldsymbol{\theta} - \mathbf{X}^\top \boldsymbol{\eta} = \mathbf{0} \geq \mathbf{0}$

So $\boldsymbol{\alpha}$ is a Type 2 arbitrage, contradicting the no-arbitrage assumption. $\square$

!!! warning "The Converse Is False"
    The Law of One Price does **not** imply no-arbitrage. A market can satisfy the LOP (identical payoffs have identical prices) while still admitting arbitrage through portfolios with different but dominating payoffs. See the example below for a concrete illustration.

---

## Dominance

### Intuition

Dominance captures a weaker form of mispricing than arbitrage. Even if no riskless profit from nothing is available, an investor should never pay more for an asset (or portfolio) that is uniformly outperformed by a cheaper alternative. If asset $A$ pays at least as much as asset $B$ in every state and strictly more in some state, then $A$ dominates $B$, and no rational investor would pay a higher price for $B$ than for $A$.

### Formal Definition

!!! info "Definition: Dominance"
    A portfolio $\boldsymbol{\theta}$ **dominates** a portfolio $\boldsymbol{\eta}$ if:

    1. $(\mathbf{X}^\top \boldsymbol{\theta})_s \geq (\mathbf{X}^\top \boldsymbol{\eta})_s$ for all $s = 1, \ldots, S$ (weakly better payoff in every state)
    2. $\mathbf{X}^\top \boldsymbol{\theta} \neq \mathbf{X}^\top \boldsymbol{\eta}$ (strictly better payoff in at least one state)
    3. $\boldsymbol{\theta}^\top \mathbf{P} \leq \boldsymbol{\eta}^\top \mathbf{P}$ (costs no more)

    The market satisfies the **no-dominance condition** if no portfolio dominates another.

!!! tip "Dominance vs. Arbitrage"
    Every arbitrage opportunity is a case of dominance (the arbitrage portfolio dominates the zero portfolio), but dominance is a weaker condition. A market can be dominance-free and still fail to be arbitrage-free only in the trivial sense -- in fact, the logical hierarchy runs in the other direction:

    $$
    \text{No-arbitrage} \implies \text{No-dominance} \implies \text{Law of One Price}
    $$

    Each implication is strict: examples exist where the weaker condition holds but the stronger one fails.

### No-Dominance and State Prices

The no-dominance condition has a clean characterization in terms of state prices.

!!! success "Theorem: No-Dominance and Positive State Prices"
    The market satisfies no-dominance if and only if there exists a **strictly positive** state price vector $\boldsymbol{\phi} \in \mathbb{R}^S$ with $\phi_s > 0$ for all $s$ such that:

    $$
    \mathbf{P} = \mathbf{X} \, \boldsymbol{\phi}
    $$

This result says that ruling out dominance is exactly what is needed to guarantee a positive linear pricing rule. The connection between no-dominance, no-arbitrage, and state prices is developed fully in the [next section](state_prices_arrow_debreu.md).

---

## The Fundamental No-Arbitrage Characterization

The following theorem is the central result of this page. It provides necessary and sufficient conditions for a finite market to be arbitrage-free.

### Statement

!!! success "Theorem: No-Arbitrage Characterization"
    The following are equivalent for a one-period market with payoff matrix $\mathbf{X} \in \mathbb{R}^{N \times S}$ and price vector $\mathbf{P} \in \mathbb{R}^N$:

    1. The market is **arbitrage-free** (no portfolio $\boldsymbol{\theta}$ is an arbitrage opportunity)
    2. There exists a **strictly positive** vector $\boldsymbol{\phi} \in \mathbb{R}^S_{++}$ such that $\mathbf{P} = \mathbf{X} \, \boldsymbol{\phi}$

This is a finite-dimensional version of the **First Fundamental Theorem of Asset Pricing**. It connects the economic condition (no free lunch) to a mathematical condition (existence of a strictly positive pricing functional). The vector $\boldsymbol{\phi}$ plays the role of a **state price vector**, and its components $\phi_s > 0$ assign a positive price to each unit of payoff in each state.

### Proof

**Direction 2 $\Rightarrow$ 1 (positive state prices rule out arbitrage).**

Suppose $\boldsymbol{\phi} \gg \mathbf{0}$ exists with $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$. Let $\boldsymbol{\theta}$ be any portfolio with $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$. Then:

$$
\boldsymbol{\theta}^\top \mathbf{P} = \boldsymbol{\theta}^\top \mathbf{X} \, \boldsymbol{\phi} = \sum_{s=1}^{S} \phi_s \bigl(\mathbf{X}^\top \boldsymbol{\theta}\bigr)_s
$$

Since $\phi_s > 0$ for all $s$ and $(\mathbf{X}^\top \boldsymbol{\theta})_s \geq 0$ for all $s$, each term in the sum is non-negative, so $\boldsymbol{\theta}^\top \mathbf{P} \geq 0$.

Now suppose additionally that $\mathbf{X}^\top \boldsymbol{\theta} \neq \mathbf{0}$, meaning $(\mathbf{X}^\top \boldsymbol{\theta})_s > 0$ for some state $s$. Then the corresponding term $\phi_s (\mathbf{X}^\top \boldsymbol{\theta})_s > 0$, so $\boldsymbol{\theta}^\top \mathbf{P} > 0$. This means $\boldsymbol{\theta}$ has strictly positive cost, which rules out both Type 1 arbitrage (which requires zero cost) and Type 2 arbitrage (which requires negative cost). $\square$

**Direction 1 $\Rightarrow$ 2 (no-arbitrage implies existence of positive state prices).**

This direction uses the **Separating Hyperplane Theorem** (equivalently, Farkas' Lemma). Define the set of "cost-payoff" vectors achievable by portfolios:

$$
\mathcal{M} = \left\{ \begin{pmatrix} -\boldsymbol{\theta}^\top \mathbf{P} \\ \mathbf{X}^\top \boldsymbol{\theta} \end{pmatrix} \in \mathbb{R}^{1+S} : \boldsymbol{\theta} \in \mathbb{R}^N \right\}
$$

This is a linear subspace of $\mathbb{R}^{1+S}$. The no-arbitrage condition says that $\mathcal{M}$ does not intersect the non-negative orthant $\mathbb{R}^{1+S}_+$ except at the origin. That is:

$$
\mathcal{M} \cap \bigl(\mathbb{R}^{1+S}_+ \setminus \{\mathbf{0}\}\bigr) = \emptyset
$$

By the Separating Hyperplane Theorem, there exists a non-zero vector $\boldsymbol{\psi} = (\psi_0, \psi_1, \ldots, \psi_S)^\top \in \mathbb{R}^{1+S}$ that separates $\mathcal{M}$ from $\mathbb{R}^{1+S}_+ \setminus \{\mathbf{0}\}$. Specifically, $\boldsymbol{\psi}^\top \mathbf{z} \leq 0$ for all $\mathbf{z} \in \mathcal{M}$ and $\boldsymbol{\psi}^\top \mathbf{z} > 0$ for all $\mathbf{z} \in \mathbb{R}^{1+S}_+ \setminus \{\mathbf{0}\}$.

Since $\mathcal{M}$ is a subspace (if $\mathbf{z} \in \mathcal{M}$ then $-\mathbf{z} \in \mathcal{M}$), the first condition strengthens to $\boldsymbol{\psi}^\top \mathbf{z} = 0$ for all $\mathbf{z} \in \mathcal{M}$. The second condition implies $\psi_0 > 0$ and $\psi_s > 0$ for all $s = 1, \ldots, S$ (take $\mathbf{z} = \mathbf{e}_k$ for each coordinate vector).

For any $\boldsymbol{\theta} \in \mathbb{R}^N$:

$$
0 = \psi_0 (-\boldsymbol{\theta}^\top \mathbf{P}) + \sum_{s=1}^{S} \psi_s (\mathbf{X}^\top \boldsymbol{\theta})_s = -\psi_0 \, \boldsymbol{\theta}^\top \mathbf{P} + \boldsymbol{\theta}^\top \mathbf{X} \, \boldsymbol{\psi}_{1:S}
$$

where $\boldsymbol{\psi}_{1:S} = (\psi_1, \ldots, \psi_S)^\top$. Since this holds for all $\boldsymbol{\theta}$:

$$
\psi_0 \, \mathbf{P} = \mathbf{X} \, \boldsymbol{\psi}_{1:S}
$$

Define $\boldsymbol{\phi} = \boldsymbol{\psi}_{1:S} / \psi_0$. Since $\psi_0 > 0$ and $\psi_s > 0$ for all $s$, we have $\boldsymbol{\phi} \gg \mathbf{0}$ and $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$. $\square$

---

## Hierarchy of No-Arbitrage Conditions

The three conditions introduced in this section form a strict hierarchy:

$$
\text{No-arbitrage} \implies \text{No-dominance} \implies \text{Law of One Price}
$$

We proved the first and last implications above. The middle implication (no-arbitrage implies no-dominance) follows because every dominance violation produces a Type 1 arbitrage: if $\boldsymbol{\theta}$ dominates $\boldsymbol{\eta}$ with $\boldsymbol{\theta}^\top \mathbf{P} \leq \boldsymbol{\eta}^\top \mathbf{P}$, then $\boldsymbol{\alpha} = \boldsymbol{\theta} - \boldsymbol{\eta}$ satisfies $\mathbf{X}^\top \boldsymbol{\alpha} \geq \mathbf{0}$, $\mathbf{X}^\top \boldsymbol{\alpha} \neq \mathbf{0}$, and $\boldsymbol{\alpha}^\top \mathbf{P} \leq 0$.

Each implication is strict in general, as the following characterization table shows:

| Condition | Equivalent Pricing Statement |
|:---|:---|
| Law of One Price | There exists a (not necessarily positive) state price vector $\boldsymbol{\phi}$ such that $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$ |
| No-dominance | There exists a **strictly positive** state price vector $\boldsymbol{\phi} \gg \mathbf{0}$ such that $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$ |
| No-arbitrage | There exists a **strictly positive** state price vector $\boldsymbol{\phi} \gg \mathbf{0}$ such that $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$ |

!!! note "No-Dominance vs. No-Arbitrage"
    In the finite-dimensional setting with a full payoff matrix, no-dominance and no-arbitrage both require the existence of strictly positive state prices and are therefore equivalent. The distinction becomes meaningful in infinite-dimensional models or when the payoff space is restricted. In this introductory treatment, the conceptual distinction matters even when the mathematical conditions coincide.

---

## Worked Example: Detecting Arbitrage in a Two-State Market

Consider a market with $S = 2$ states (Boom and Recession) and $N = 3$ assets:

- **Bond**: Price $P_1 = 1$, pays $X_{11} = 1.05$ in both states (risk-free rate $r_f = 5\%$)
- **Stock**: Price $P_2 = 10$, pays $X_{21} = 14$ in Boom and $X_{22} = 8$ in Recession
- **Call option**: Price $P_3 = 2$, pays $X_{31} = 4$ in Boom and $X_{32} = 0$ in Recession

The payoff matrix and price vector are:

$$
\mathbf{X} = \begin{pmatrix} 1.05 & 1.05 \\ 14 & 8 \\ 4 & 0 \end{pmatrix}, \qquad \mathbf{P} = \begin{pmatrix} 1 \\ 10 \\ 2 \end{pmatrix}
$$

### Step 1: Check for State Prices

We seek $\boldsymbol{\phi} = (\phi_1, \phi_2)^\top \gg \mathbf{0}$ satisfying $\mathbf{X}\,\boldsymbol{\phi} = \mathbf{P}$:

$$
\begin{cases} 1.05\,\phi_1 + 1.05\,\phi_2 = 1 \\ 14\,\phi_1 + 8\,\phi_2 = 10 \\ 4\,\phi_1 + 0\,\phi_2 = 2 \end{cases}
$$

From equation (3): $\phi_1 = 0.5$. From equation (1): $1.05(0.5 + \phi_2) = 1$, so $\phi_2 = 1/1.05 - 0.5 \approx 0.9524 - 0.5 = 0.4524$.

Check equation (2): $14(0.5) + 8(0.4524) = 7 + 3.619 = 10.619 \neq 10$.

The system is **inconsistent** -- no state price vector $\boldsymbol{\phi}$ satisfies all three pricing equations simultaneously. By the Fundamental No-Arbitrage Characterization, the market admits arbitrage.

### Step 2: Construct the Arbitrage Portfolio

Since the stock is overpriced relative to the bond and call (equation (2) gives $10.619 > 10$), we should sell the stock and buy a replicating portfolio of the bond and call.

We seek $\theta_1, \theta_3$ such that:

$$
\begin{pmatrix} 1.05 & 4 \\ 1.05 & 0 \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_3 \end{pmatrix} = \begin{pmatrix} 14 \\ 8 \end{pmatrix}
$$

From the second equation: $\theta_1 = 8/1.05 \approx 7.619$. From the first: $1.05(7.619) + 4\theta_3 = 14$, so $4\theta_3 = 14 - 8 = 6$, giving $\theta_3 = 1.5$.

The replicating portfolio costs: $7.619 \times 1 + 1.5 \times 2 = 7.619 + 3 = 10.619$.

Now form the arbitrage portfolio: buy the replicating portfolio and sell 1 unit of stock. With $\boldsymbol{\theta}^* = (-7.619,\; 1,\; -1.5)^\top$:

- **Cost**: $\boldsymbol{\theta}^{*\top} \mathbf{P} = -7.619 + 10 - 3 = -0.619 < 0$ (receives \$0.619 at $t = 0$)
- **Payoff in Boom**: $-7.619(1.05) + 1(14) - 1.5(4) = -8 + 14 - 6 = 0$
- **Payoff in Recession**: $-7.619(1.05) + 1(8) - 1.5(0) = -8 + 8 - 0 = 0$

The portfolio $\boldsymbol{\theta}^*$ costs $-\$0.619$ (the trader receives money upfront) and pays \$0 in every state. This is a **Type 2 arbitrage**: the trader pockets \$0.619 today with no future liability.

!!! example "Summary of the Arbitrage"
    | | Cost at $t = 0$ | Payoff in Boom | Payoff in Recession |
    |:---|:---:|:---:|:---:|
    | Sell 7.619 bonds | $-\$7.619$ | $-\$8.00$ | $-\$8.00$ |
    | Buy 1 stock | $+\$10.00$ | $+\$14.00$ | $+\$8.00$ |
    | Sell 1.5 calls | $-\$3.00$ | $-\$6.00$ | $\$0.00$ |
    | **Total** | **$-\$0.619$** | **$\$0.00$** | **$\$0.00$** |

    The trader receives \$0.619 today and owes nothing in the future, regardless of which state occurs. This is a Type 2 arbitrage.

### Step 3: What Would Eliminate the Arbitrage?

If the stock price were \$10, the state prices consistent with the bond and stock alone would be:

$$
\begin{cases} 1.05\,\phi_1 + 1.05\,\phi_2 = 1 \\ 14\,\phi_1 + 8\,\phi_2 = 10 \end{cases}
$$

This gives $\phi_1 = 1/3$ and $\phi_2 = 1/1.05 - 1/3 \approx 0.6190$. Then the no-arbitrage call price would be $4(1/3) + 0(0.6190) = 4/3 \approx \$1.333$, not \$2. The observed call price of \$2 is too expensive, creating the arbitrage.

---

## A Second Example: Verifying No-Arbitrage

Consider a market with $S = 3$ states and $N = 2$ assets:

- **Bond**: Price $P_1 = 0.95$, pays $X_{1s} = 1$ in every state
- **Stock**: Price $P_2 = 50$, pays $X_{21} = 70$, $X_{22} = 55$, $X_{23} = 40$

$$
\mathbf{X} = \begin{pmatrix} 1 & 1 & 1 \\ 70 & 55 & 40 \end{pmatrix}, \qquad \mathbf{P} = \begin{pmatrix} 0.95 \\ 50 \end{pmatrix}
$$

We need $\boldsymbol{\phi} = (\phi_1, \phi_2, \phi_3)^\top \gg \mathbf{0}$ satisfying:

$$
\begin{cases} \phi_1 + \phi_2 + \phi_3 = 0.95 \\ 70\,\phi_1 + 55\,\phi_2 + 40\,\phi_3 = 50 \end{cases}
$$

This is an underdetermined system ($S = 3 > N = 2$), so there are infinitely many solutions. Parameterize by $\phi_2 = t$. From equation (1): $\phi_1 + \phi_3 = 0.95 - t$. From equation (2): $70\,\phi_1 + 40\,\phi_3 = 50 - 55t$, which gives $30\,\phi_1 = 50 - 55t - 40(0.95 - t) = 50 - 55t - 38 + 40t = 12 - 15t$, so:

$$
\phi_1 = \frac{12 - 15t}{30} = 0.4 - 0.5t, \qquad \phi_3 = 0.95 - t - (0.4 - 0.5t) = 0.55 - 0.5t
$$

For all three state prices to be strictly positive:

- $\phi_1 > 0$: $t < 0.8$
- $\phi_2 > 0$: $t > 0$
- $\phi_3 > 0$: $t < 1.1$

So for any $t \in (0, 0.8)$, we get $\boldsymbol{\phi} \gg \mathbf{0}$. By the Fundamental No-Arbitrage Characterization, this market is **arbitrage-free**. However, the state prices are not unique (the market is incomplete since $N < S$), which means there are multiple risk-neutral pricing rules consistent with the observed prices.

!!! example "Concrete State Prices"
    Choosing $t = 0.3$ gives $\boldsymbol{\phi} = (0.25,\; 0.30,\; 0.40)^\top$, and the corresponding risk-neutral probabilities are:

    $$
    q_s = \frac{\phi_s}{\sum_k \phi_k} = \frac{\phi_s}{0.95}
    $$

    | State | $\phi_s$ | $q_s$ |
    |:---:|:---:|:---:|
    | $\omega_1$ (Boom) | 0.25 | 0.2632 |
    | $\omega_2$ (Moderate) | 0.30 | 0.3158 |
    | $\omega_3$ (Recession) | 0.40 | 0.4211 |

    The risk-neutral measure overweights the recession state, reflecting the market's aggregate risk aversion.

---

## Connection to the Fundamental Theorem of Asset Pricing

The results on this page are the starting point for the **First Fundamental Theorem of Asset Pricing** (FTAP), which is treated in full generality in [Section 1.3](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md). In the finite one-period setting:

- **This page** establishes that no-arbitrage is equivalent to the existence of strictly positive state prices $\boldsymbol{\phi} \gg \mathbf{0}$ with $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$.
- **The [next section](state_prices_arrow_debreu.md)** shows that these state prices define Arrow-Debreu prices and can be re-scaled to produce risk-neutral probabilities, giving the discounted expected value formula $P_j = \frac{1}{1+r_f}\mathbb{E}^{\mathbb{Q}}[X_j]$.
- **Section 1.3** extends these ideas to multi-period and more general settings, where the role of $\boldsymbol{\phi}$ is played by an equivalent martingale measure and the Separating Hyperplane Theorem is replaced by the Hahn-Banach theorem.

---

## Summary

| Concept | Definition | Characterization |
|:---|:---|:---|
| Type 1 Arbitrage | Zero-cost portfolio with non-negative, non-zero payoff | "Something for nothing" |
| Type 2 Arbitrage | Negative-cost portfolio with non-negative payoff | "Free lottery" |
| Law of One Price | Same payoff $\Rightarrow$ same cost | Exists state price vector $\boldsymbol{\phi}$ (possibly with $\phi_s \leq 0$) |
| No-Dominance | No portfolio uniformly outperforms a cheaper one | Exists $\boldsymbol{\phi} \gg \mathbf{0}$ with $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$ |
| No-Arbitrage | No riskless profit from zero or negative investment | Exists $\boldsymbol{\phi} \gg \mathbf{0}$ with $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$ |

The hierarchy of conditions:

$$
\text{No-arbitrage} \implies \text{No-dominance} \implies \text{Law of One Price}
$$

The fundamental result: **a finite one-period market is arbitrage-free if and only if there exists a strictly positive state price vector**. This is the discrete version of the First Fundamental Theorem of Asset Pricing and the gateway to risk-neutral pricing theory.

---

## Exercises

**Exercise 1.** Consider a market with $S = 2$ states and $N = 2$ assets: a bond with price $P_1 = 1$ paying $1.04$ in both states, and a stock with price $P_2 = 25$ paying $X_{21} = 30$ in state $\omega_1$ and $X_{22} = 22$ in state $\omega_2$. Determine whether a strictly positive state price vector $\boldsymbol{\phi}$ exists. Is the market arbitrage-free?

??? success "Solution to Exercise 1"
    We need to find $\boldsymbol{\phi} = (\phi_1, \phi_2)^\top$ satisfying $\mathbf{X}\,\boldsymbol{\phi} = \mathbf{P}$:

    $$
    \begin{cases} 1.04\,\phi_1 + 1.04\,\phi_2 = 1 \\ 30\,\phi_1 + 22\,\phi_2 = 25 \end{cases}
    $$

    From equation (1): $\phi_1 + \phi_2 = 1/1.04 \approx 0.9615$, so $\phi_2 = 0.9615 - \phi_1$.

    Substituting into equation (2):

    $$
    30\,\phi_1 + 22(0.9615 - \phi_1) = 25
    $$

    $$
    30\,\phi_1 + 21.1538 - 22\,\phi_1 = 25
    $$

    $$
    8\,\phi_1 = 3.8462 \implies \phi_1 = 0.4808
    $$

    $$
    \phi_2 = 0.9615 - 0.4808 = 0.4808
    $$

    More precisely, from equation (1): $\phi_1 + \phi_2 = 25/26$. From equation (2): $30\phi_1 + 22\phi_2 = 25$. Solving: $8\phi_1 = 25 - 22 \cdot (25/26) = 25 - 550/26 = (650 - 550)/26 = 100/26$, so $\phi_1 = 100/208 = 25/52$ and $\phi_2 = 25/26 - 25/52 = 25/52$.

    Both state prices are strictly positive: $\phi_1 = 25/52 \approx 0.4808 > 0$ and $\phi_2 = 25/52 \approx 0.4808 > 0$.

    Since a strictly positive state price vector exists, the market is **arbitrage-free**.

---

**Exercise 2.** Prove that the Law of One Price does not imply no-arbitrage by constructing a concrete example of a market (specify the payoff matrix $\mathbf{X}$ and price vector $\mathbf{P}$) that satisfies the LOP but admits a Type 1 arbitrage opportunity.

??? success "Solution to Exercise 2"
    Consider a market with $S = 2$ states and $N = 2$ assets with:

    $$
    \mathbf{X} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \quad \mathbf{P} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
    $$

    **The LOP holds:** The LOP requires that $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{X}^\top \boldsymbol{\eta}$ implies $\boldsymbol{\theta}^\top \mathbf{P} = \boldsymbol{\eta}^\top \mathbf{P}$. Since $\mathbf{P} = \mathbf{0}$, every portfolio has zero cost: $\boldsymbol{\theta}^\top \mathbf{P} = 0$ for all $\boldsymbol{\theta}$. So the LOP is trivially satisfied.

    **A Type 1 arbitrage exists:** Take $\boldsymbol{\theta} = (1, 0)^\top$. Then:

    - Cost: $\boldsymbol{\theta}^\top \mathbf{P} = 0$
    - Payoff: $\mathbf{X}^\top \boldsymbol{\theta} = (1, 0)^\top \geq \mathbf{0}$ and $\neq \mathbf{0}$

    This portfolio costs nothing and pays \$1 in state $\omega_1$ and \$0 in state $\omega_2$. It is a Type 1 arbitrage. Thus, the LOP does not imply no-arbitrage.

---

**Exercise 3.** In a market with $S = 3$ states and $N = 3$ assets, the payoff matrix and price vector are

$$
\mathbf{X} = \begin{pmatrix} 1.05 & 1.05 & 1.05 \\ 20 & 15 & 10 \\ 5 & 3 & 0 \end{pmatrix}, \quad \mathbf{P} = \begin{pmatrix} 1 \\ 12 \\ 2 \end{pmatrix}
$$

Determine whether the market is arbitrage-free by solving for the state price vector. If an arbitrage exists, construct the arbitrage portfolio explicitly.

??? success "Solution to Exercise 3"
    We solve $\mathbf{X}\,\boldsymbol{\phi} = \mathbf{P}$:

    $$
    \begin{cases} 1.05\,\phi_1 + 1.05\,\phi_2 + 1.05\,\phi_3 = 1 \\ 20\,\phi_1 + 15\,\phi_2 + 10\,\phi_3 = 12 \\ 5\,\phi_1 + 3\,\phi_2 + 0\,\phi_3 = 2 \end{cases}
    $$

    From equation (1): $\phi_1 + \phi_2 + \phi_3 = 1/1.05 = 20/21$.

    From equation (2): $20\phi_1 + 15\phi_2 + 10\phi_3 = 12$. Rewrite as $20\phi_1 + 15\phi_2 + 10\phi_3 = 12$.

    Subtract $10 \times$ equation (1-simplified) from equation (2):

    $$
    10\phi_1 + 5\phi_2 = 12 - 10 \cdot \frac{20}{21} = 12 - \frac{200}{21} = \frac{252 - 200}{21} = \frac{52}{21} \quad \cdots \text{(i)}
    $$

    From equation (3): $5\phi_1 + 3\phi_2 = 2 \quad \cdots \text{(ii)}$.

    From (i): $10\phi_1 + 5\phi_2 = 52/21$. From $2 \times$ (ii): $10\phi_1 + 6\phi_2 = 4$. Subtracting (i) from this:

    $$
    \phi_2 = 4 - \frac{52}{21} = \frac{84 - 52}{21} = \frac{32}{21}
    $$

    From (ii): $5\phi_1 = 2 - 3 \cdot (32/21) = 2 - 96/21 = (42 - 96)/21 = -54/21$, so $\phi_1 = -54/105 = -18/35$.

    Since $\phi_1 = -18/35 < 0$, no strictly positive state price vector exists. By the Fundamental No-Arbitrage Characterization, the market **admits arbitrage**.

    **Constructing the arbitrage portfolio:** Since $\phi_1 < 0$, state $\omega_1$ is "overpriced." We look for a portfolio that exploits this. We need $\boldsymbol{\theta}$ such that $\boldsymbol{\theta}^\top \mathbf{P} \leq 0$ and $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$.

    Try to replicate a payoff that is positive only in state $\omega_1$. Let us seek $\boldsymbol{\theta}$ such that $\mathbf{X}^\top \boldsymbol{\theta} = (1, 0, 0)^\top$:

    $$
    \begin{pmatrix} 1.05 & 20 & 5 \\ 1.05 & 15 & 3 \\ 1.05 & 10 & 0 \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_2 \\ \theta_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
    $$

    From row 3: $1.05\theta_1 + 10\theta_2 = 0$, so $\theta_1 = -10\theta_2/1.05$. From row 2: $1.05\theta_1 + 15\theta_2 + 3\theta_3 = 0$, substituting: $-10\theta_2 + 15\theta_2 + 3\theta_3 = 0$, so $5\theta_2 + 3\theta_3 = 0$, giving $\theta_3 = -5\theta_2/3$. From row 1: $1.05\theta_1 + 20\theta_2 + 5\theta_3 = 1$, substituting: $-10\theta_2 + 20\theta_2 - 25\theta_2/3 = 1$, so $10\theta_2 - 25\theta_2/3 = (30\theta_2 - 25\theta_2)/3 = 5\theta_2/3 = 1$, giving $\theta_2 = 3/5$.

    Thus $\theta_1 = -10(3/5)/1.05 = -6/1.05 = -40/7$, $\theta_2 = 3/5$, $\theta_3 = -5(3/5)/3 = -1$.

    The cost is:

    $$
    \boldsymbol{\theta}^\top \mathbf{P} = (-40/7)(1) + (3/5)(12) + (-1)(2) = -40/7 + 36/5 - 2
    $$

    $$
    = \frac{-200 + 252 - 70}{35} = \frac{-18}{35} < 0
    $$

    The portfolio $\boldsymbol{\theta} = (-40/7,\; 3/5,\; -1)^\top$ has negative cost ($-18/35 \approx -\$0.514$) and payoff $(1, 0, 0)^\top \geq \mathbf{0}$. This is an arbitrage: the trader receives \$0.514 today and is guaranteed a non-negative payoff (specifically \$1 in state $\omega_1$ and \$0 otherwise).

---

**Exercise 4.** Let $\boldsymbol{\theta}$ be a portfolio in a one-period market satisfying $\boldsymbol{\theta}^\top \mathbf{P} = 0$ and $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$. Suppose that strictly positive state prices $\boldsymbol{\phi} \gg \mathbf{0}$ exist with $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$. Show that $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{0}$, i.e., the payoff must be identically zero. Explain why this rules out Type 1 arbitrage.

??? success "Solution to Exercise 4"
    We have $\boldsymbol{\theta}^\top \mathbf{P} = 0$ and $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$. Since $\boldsymbol{\phi} \gg \mathbf{0}$ and $\mathbf{P} = \mathbf{X}\,\boldsymbol{\phi}$:

    $$
    0 = \boldsymbol{\theta}^\top \mathbf{P} = \boldsymbol{\theta}^\top \mathbf{X}\,\boldsymbol{\phi} = \sum_{s=1}^{S} \phi_s \, (\mathbf{X}^\top \boldsymbol{\theta})_s
    $$

    Each term in this sum satisfies $\phi_s > 0$ and $(\mathbf{X}^\top \boldsymbol{\theta})_s \geq 0$, so every term is non-negative. A sum of non-negative terms equals zero if and only if every term is zero. Since $\phi_s > 0$ for all $s$, this requires:

    $$
    (\mathbf{X}^\top \boldsymbol{\theta})_s = 0 \quad \text{for all } s = 1, \ldots, S
    $$

    Therefore $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{0}$.

    **Why this rules out Type 1 arbitrage:** A Type 1 arbitrage requires a portfolio with $\boldsymbol{\theta}^\top \mathbf{P} = 0$, $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{0}$, and $\mathbf{X}^\top \boldsymbol{\theta} \neq \mathbf{0}$. We have just shown that the first two conditions force $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{0}$, contradicting the third condition. Hence no Type 1 arbitrage can exist when strictly positive state prices exist.

---

**Exercise 5.** A market has $S = 2$ states and $N = 3$ assets. The bond pays $1.10$ in both states. Stock A has price \$40 and pays \$50 in the boom and \$35 in the recession. Stock B has price \$15 and pays \$20 in the boom and \$12 in the recession. Find the state prices from the bond and Stock A alone. Then check whether Stock B's observed price is consistent with these state prices. If not, construct an arbitrage portfolio.

??? success "Solution to Exercise 5"
    **Bond price:** $P_1 = 1$ (given implicitly by the payoff of $1.10$ and risk-free rate $r_f = 0.10$, so $P_1 = 1$). Actually, the bond price is not explicitly stated. Since the bond pays $1.10$ in both states and $1 + r_f = 1.10$, we have $P_1 = 1$.

    **State prices from bond and Stock A:** Solve $\mathbf{X}\,\boldsymbol{\phi} = \mathbf{P}$:

    $$
    \begin{cases} 1.10\,\phi_1 + 1.10\,\phi_2 = 1 \\ 50\,\phi_1 + 35\,\phi_2 = 40 \end{cases}
    $$

    From equation (1): $\phi_1 + \phi_2 = 1/1.10 = 10/11$.

    Subtract $35 \times$ equation (1-simplified) from equation (2):

    $$
    15\,\phi_1 = 40 - 35 \cdot \frac{10}{11} = 40 - \frac{350}{11} = \frac{440 - 350}{11} = \frac{90}{11}
    $$

    $$
    \phi_1 = \frac{90}{165} = \frac{6}{11}
    $$

    $$
    \phi_2 = \frac{10}{11} - \frac{6}{11} = \frac{4}{11}
    $$

    Both are strictly positive.

    **Check Stock B:** The no-arbitrage price of Stock B should be:

    $$
    P_B^* = 20\,\phi_1 + 12\,\phi_2 = 20 \cdot \frac{6}{11} + 12 \cdot \frac{4}{11} = \frac{120 + 48}{11} = \frac{168}{11} \approx 15.27
    $$

    The observed price is $P_B = 15$, which is less than the no-arbitrage price of $\$15.27$. Stock B is **underpriced**, and an arbitrage exists.

    **Constructing the arbitrage:** Buy Stock B (cheap) and sell the replicating portfolio. We need $\theta_1, \theta_A$ such that:

    $$
    \begin{pmatrix} 1.10 & 50 \\ 1.10 & 35 \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_A \end{pmatrix} = \begin{pmatrix} 20 \\ 12 \end{pmatrix}
    $$

    From the difference of the two rows: $15\,\theta_A = 8$, so $\theta_A = 8/15$. From row 2: $1.10\,\theta_1 + 35(8/15) = 12$, so $1.10\,\theta_1 = 12 - 56/3 = (36 - 56)/3 = -20/3$, giving $\theta_1 = -20/(3 \times 1.10) = -200/33$.

    The replicating portfolio costs: $(-200/33)(1) + (8/15)(40) = -200/33 + 320/15 = -200/33 + 704/33 = 504/33 = 168/11 \approx 15.27$.

    Arbitrage portfolio: buy 1 unit of Stock B and sell the replicating portfolio. Specifically, $\boldsymbol{\theta}^* = (200/33,\; -8/15,\; 1)^\top$:

    - Cost: $200/33 \cdot 1 - 8/15 \cdot 40 + 1 \cdot 15 = 200/33 - 320/15 + 15 = 200/33 - 704/33 + 495/33 = -9/33 = -3/11 \approx -\$0.27$
    - Payoff in Boom: $(200/33)(1.10) - (8/15)(50) + 20 = 220/33 - 400/15 + 20 = 20/3 - 80/3 + 60/3 = 0$
    - Payoff in Recession: $(200/33)(1.10) - (8/15)(35) + 12 = 20/3 - 56/3 + 36/3 = 0$

    The trader receives $\$3/11 \approx \$0.27$ today with zero future liability -- a Type 2 arbitrage.

---

**Exercise 6.** Explain the hierarchy

$$
\text{No-arbitrage} \implies \text{No-dominance} \implies \text{Law of One Price}
$$

by answering: (a) Why does no-arbitrage imply no-dominance? (b) Why does no-dominance imply the LOP? (c) Give a one-sentence economic interpretation of each implication.

??? success "Solution to Exercise 6"
    **(a) No-arbitrage implies no-dominance:** Suppose portfolio $\boldsymbol{\theta}$ dominates portfolio $\boldsymbol{\eta}$: $\mathbf{X}^\top \boldsymbol{\theta} \geq \mathbf{X}^\top \boldsymbol{\eta}$ with strict inequality in some state, and $\boldsymbol{\theta}^\top \mathbf{P} \leq \boldsymbol{\eta}^\top \mathbf{P}$. Define $\boldsymbol{\alpha} = \boldsymbol{\theta} - \boldsymbol{\eta}$. Then $\mathbf{X}^\top \boldsymbol{\alpha} \geq \mathbf{0}$, $\mathbf{X}^\top \boldsymbol{\alpha} \neq \mathbf{0}$, and $\boldsymbol{\alpha}^\top \mathbf{P} \leq 0$. This is an arbitrage opportunity (Type 1 if $\boldsymbol{\alpha}^\top \mathbf{P} = 0$, Type 2 if $\boldsymbol{\alpha}^\top \mathbf{P} < 0$). So if no arbitrage exists, no dominance can exist.

    **(b) No-dominance implies the LOP:** Suppose the LOP fails: there exist $\boldsymbol{\theta}, \boldsymbol{\eta}$ with $\mathbf{X}^\top \boldsymbol{\theta} = \mathbf{X}^\top \boldsymbol{\eta}$ but $\boldsymbol{\theta}^\top \mathbf{P} < \boldsymbol{\eta}^\top \mathbf{P}$. Then $\boldsymbol{\theta}$ has the same payoff as $\boldsymbol{\eta}$ in every state (so weakly better, and not strictly better in any state -- they are equal). However, consider: since $\boldsymbol{\theta}$ has the same payoff but lower cost, the LOP failure actually means $\boldsymbol{\alpha} = \boldsymbol{\theta} - \boldsymbol{\eta}$ gives $\mathbf{X}^\top \boldsymbol{\alpha} = \mathbf{0}$ and $\boldsymbol{\alpha}^\top \mathbf{P} < 0$. Now $\boldsymbol{\alpha}$ dominates $\mathbf{0}$: it costs less ($\boldsymbol{\alpha}^\top \mathbf{P} < 0$) and has non-negative payoff ($\mathbf{X}^\top \boldsymbol{\alpha} = \mathbf{0} \geq \mathbf{0}$). Actually, for dominance we need strict inequality in at least one payoff state, and here the payoff is identically zero. But $\boldsymbol{\alpha}$ is a Type 2 arbitrage (negative cost, non-negative payoff), and any arbitrage is a dominance violation. Specifically, $\boldsymbol{\alpha}$ dominates $\mathbf{0}$ because we can view the negative cost as a strictly better "payoff at $t = 0$." More precisely, if no-dominance holds, then for any $\boldsymbol{\alpha}$ with $\mathbf{X}^\top \boldsymbol{\alpha} \geq \mathbf{X}^\top \mathbf{0} = \mathbf{0}$, we must have $\boldsymbol{\alpha}^\top \mathbf{P} \geq 0$ (otherwise $\boldsymbol{\alpha}$ would dominate $\mathbf{0}$ in the extended sense including cost). In fact, no-dominance implies no-arbitrage in the finite setting, and no-arbitrage implies LOP, so the chain holds.

    **(c) Economic interpretations:**

    - *No-arbitrage $\implies$ no-dominance:* If you cannot get something for nothing, then you certainly cannot get a uniformly better investment for a lower price.
    - *No-dominance $\implies$ LOP:* If no investment can be uniformly outperformed by a cheaper one, then two investments with identical payoffs must cost the same.
