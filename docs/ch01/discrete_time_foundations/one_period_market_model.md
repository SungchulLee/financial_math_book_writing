# One-Period Market Model

This page sets up the **environment** in which all of one-period asset pricing
takes place: states, probabilities, traded assets, the payoff matrix, and the
risk-free bond. The economic content — arbitrage, the linear pricing rule,
state prices, and risk-neutral expectation — is developed in the three pages
that follow, each of which depends on the notation fixed here.

The chapter has a single destination: the **First Fundamental Theorem of Asset
Pricing**, which states that a finite market admits no arbitrage if and only
if its price vector $\mathbf{P}$ and payoff matrix $\mathbf{X}$ satisfy a
linear pricing rule $\mathbf{P} = \mathbf{X}\boldsymbol{\phi}$ with
$\boldsymbol{\phi} \gg 0$. The theorem is stated and proved in
[§ Arbitrage and dominance](arbitrage_and_dominance.md); its interpretation as
Arrow–Debreu pricing and risk-neutral expectation is the subject of
[§ State prices](state_prices_arrow_debreu.md). The roadmap:

| Section | Role | Concept |
|---|---|---|
| **One-period model** (this page) | Environment | States, assets, payoff matrix, bond |
| [Portfolios and payoffs](portfolios_and_payoffs.md) | Mechanics | Trading, linearity, attainable set |
| [Arbitrage and dominance](arbitrage_and_dominance.md) | Core theory | No-arbitrage, LOP, FTAP |
| [State prices](state_prices_arrow_debreu.md) | Interpretation | Arrow–Debreu, $\mathbb{Q}$, SDF |

Every continuous-time result later in the book — Black–Scholes, HJM, and
beyond — has a one-period ancestor built on the same logic:
**no-arbitrage $\Leftrightarrow$ linear pricing**.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Define the mathematical components of a one-period market: finite state space, probability measure, asset prices, and payoff matrix
    - Express the pricing problem in vector and matrix form
    - Distinguish between the initial price vector and the terminal payoff matrix
    - Understand the role of the risk-free bond in normalizing prices and defining the discount factor
    - Connect this framework to the concepts of [portfolios](portfolios_and_payoffs.md), [arbitrage](arbitrage_and_dominance.md), and [state prices](state_prices_arrow_debreu.md) developed in the subsequent sections

---

## Uncertainty and the State Space

### Intuition

In a deterministic world, pricing is trivial: every asset's future value is known, and its price today is simply the discounted future value. The interesting problem arises when the future is uncertain. We model uncertainty by specifying a finite list of possible scenarios --- called **states of the world** --- exactly one of which will be realized at the future date. Each state determines the payoff of every asset in the economy.

The finiteness assumption is a deliberate simplification. It makes the mathematics concrete --- linear algebra replaces measure theory --- while preserving the economic content. The general case with infinitely many states requires the machinery of probability spaces and sigma-algebras, but every key insight already appears in the finite setting.

### Formal Setup

!!! info "Definition: State Space and Probability Measure"
    The **state space** is a finite set

    $$
    \Omega = \{\omega_1, \omega_2, \ldots, \omega_S\}
    $$

    where $S \geq 2$ is the number of possible future states. Each state $\omega_s$ represents a complete description of the world at the future date.

    A **probability measure** $\mathbb{P}$ assigns to each state a strictly positive probability:

    $$
    p_s = \mathbb{P}(\omega_s) > 0, \quad s = 1, 2, \ldots, S
    $$

    with the normalization

    $$
    \sum_{s=1}^{S} p_s = 1
    $$

The strict positivity requirement $p_s > 0$ means that every state is genuinely possible. If some state had zero probability, it could be removed from $\Omega$ without changing the model. The probabilities $p_s$ represent the **physical** (or **real-world**) probabilities --- the actual likelihoods an observer would assign to each scenario.

!!! tip "Why Strict Positivity Matters"
    If a state $\omega_s$ were assigned probability zero, it would be economically irrelevant: no agent would pay to insure against it, and no pricing constraint would arise from it. The condition $p_s > 0$ for all $s$ ensures that the probability measure $\mathbb{P}$ and any risk-neutral measure $\mathbb{Q}$ (introduced in the [state prices](state_prices_arrow_debreu.md) section) are **equivalent** --- they agree on which events are possible, even if they disagree on the numerical probabilities.

---

## Time Structure

The one-period model has exactly two dates:

- **$t = 0$** (today): Prices are observed, investment decisions are made, and portfolios are formed.
- **$t = 1$** (future): Uncertainty is resolved --- one state $\omega_s \in \Omega$ is realized --- and assets deliver their payoffs.

There is no trading at $t = 1$. All portfolio decisions are made at $t = 0$ and held until $t = 1$. This "buy and hold" structure means there are no intermediate rebalancing opportunities, no transaction costs from dynamic trading, and no issues of information arrival between dates.

!!! note "One Period Does Not Mean One Day"
    The interval from $t = 0$ to $t = 1$ can represent any horizon: one day, one month, one year, or even ten years. What matters is that there are exactly two decision points and exactly one resolution of uncertainty.

---

## Traded Assets and Prices

### Asset Prices at Time Zero

The economy contains $N \geq 1$ traded assets, indexed by $j = 1, 2, \ldots, N$. At $t = 0$, each asset $j$ has a known, observable market price $P_j \in \mathbb{R}$. We collect these into the **price vector**:

$$
\mathbf{P} = \begin{pmatrix} P_1 \\ P_2 \\ \vdots \\ P_N \end{pmatrix} \in \mathbb{R}^N
$$

Prices may be positive (stocks, bonds), zero (forward contracts at initiation), or negative (short positions reflected in certain structured products), so we allow $P_j \in \mathbb{R}$ in general.

### Terminal Payoffs

At $t = 1$, once the state $\omega_s$ is realized, asset $j$ delivers a payoff $X_{js} = X_j(\omega_s)$. This payoff represents the total cash flow received by the holder --- it includes both the terminal asset value and any dividends or coupons paid at $t = 1$.

!!! info "Definition: Payoff Matrix"
    The **payoff matrix** $\mathbf{X} \in \mathbb{R}^{N \times S}$ collects all terminal payoffs:

    $$
    \mathbf{X} = \begin{pmatrix} X_{11} & X_{12} & \cdots & X_{1S} \\ X_{21} & X_{22} & \cdots & X_{2S} \\ \vdots & \vdots & \ddots & \vdots \\ X_{N1} & X_{N2} & \cdots & X_{NS} \end{pmatrix}
    $$

    - **Row $j$**: the payoff profile of asset $j$ across all states, i.e., the row vector $(X_{j1}, X_{j2}, \ldots, X_{jS})$.
    - **Column $s$**: the payoffs of all assets in state $\omega_s$, i.e., the column vector $(X_{1s}, X_{2s}, \ldots, X_{Ns})^\top$.

The payoff matrix is the central object of the one-period model. Its rank determines whether the market is complete or incomplete, and its column space determines which contingent claims can be replicated. These connections are developed in the sections on [portfolios and payoffs](portfolios_and_payoffs.md) and [arbitrage and dominance](arbitrage_and_dominance.md).

---

## The Risk-Free Bond

### Motivation

Among the $N$ traded assets, one plays a distinguished role: the **risk-free bond** (or **riskless asset**). This is an asset whose payoff is the same in every state of the world, so it carries no uncertainty. Its existence is not a theorem --- it is an assumption we impose on the model, reflecting the empirical observation that short-term government securities are approximately riskless over short horizons.

### Definition

!!! info "Definition: Risk-Free Bond"
    The **risk-free bond** is an asset (conventionally labeled $j = 0$ or $j = 1$) with:

    - **Price at $t = 0$**: $B_0 = 1$ (normalized to one unit of currency).
    - **Payoff at $t = 1$**: $B_1 = 1 + r_f$ in every state $\omega_s$, where $r_f > -1$ is the **risk-free interest rate** (also called the **risk-free rate**).

The normalization $B_0 = 1$ is a convention that simplifies notation --- any riskless asset with price $B_0 \neq 0$ can be rescaled to satisfy it. The condition $r_f > -1$ ensures the bond has a strictly positive terminal value.

### The Discount Factor

The **discount factor** is defined as:

$$
\beta = \frac{1}{1 + r_f}
$$

It converts future (time-$1$) cash flows into present (time-$0$) values. A dollar received at $t = 1$ is worth $\beta$ dollars today. Since $r_f > -1$, we have $\beta > 0$, and when $r_f > 0$ (the typical case), $\beta < 1$, reflecting the time value of money: a dollar today is worth more than a dollar tomorrow.

!!! tip "Discount Factor vs Risk-Free Rate"
    The two quantities $r_f$ and $\beta = 1/(1 + r_f)$ encode the same information in different forms. Use whichever is more convenient:

    - The risk-free rate $r_f$ is natural when discussing returns: the bond earns a gross return of $1 + r_f$.
    - The discount factor $\beta$ is natural when pricing: the bond's time-$0$ price satisfies $B_0 = \beta \cdot B_1 = \beta(1 + r_f) = 1$.

### Including the Bond in the Payoff Matrix

When the risk-free bond is one of the $N$ assets (say, asset $j = 1$), its row in the payoff matrix is:

$$
(X_{11}, X_{12}, \ldots, X_{1S}) = (1 + r_f, \; 1 + r_f, \; \ldots, \; 1 + r_f)
$$

and its entry in the price vector is $P_1 = 1$. Equivalently, if we prefer to separate the bond from the risky assets, we can index risky assets $j = 1, \ldots, N$ and treat the bond as an additional "zeroth" asset with its own notation. Both conventions appear in the literature; we will use whichever is clearer in context.

---

## Putting It All Together

### The Complete Model Specification

!!! info "Definition: One-Period Market Model"
    A **one-period market model** is specified by the tuple $(\Omega, \mathbb{P}, N, \mathbf{P}, \mathbf{X}, r_f)$ where:

    1. $\Omega = \{\omega_1, \ldots, \omega_S\}$ is the finite state space with $S \geq 2$ states.
    2. $\mathbb{P}$ is a probability measure with $p_s = \mathbb{P}(\omega_s) > 0$ for all $s$.
    3. $N \geq 1$ is the number of traded assets.
    4. $\mathbf{P} \in \mathbb{R}^N$ is the vector of time-$0$ asset prices.
    5. $\mathbf{X} \in \mathbb{R}^{N \times S}$ is the payoff matrix of terminal payoffs.
    6. $r_f > -1$ is the risk-free interest rate, with corresponding discount factor $\beta = 1/(1 + r_f)$.

    One of the $N$ assets is assumed to be the risk-free bond with price $1$ and constant payoff $1 + r_f$.

### The Pricing Problem

The central question of asset pricing is: **Given the model $(\Omega, \mathbb{P}, N, \mathbf{P}, \mathbf{X}, r_f)$, which price vectors $\mathbf{P}$ are consistent with the absence of arbitrage?**

Equivalently: is there a way to assign values to future uncertain cash flows that is internally consistent --- meaning no investor can construct a portfolio that generates something from nothing? This question leads directly to the theory of [arbitrage and dominance](arbitrage_and_dominance.md), and its answer involves the existence of [state prices](state_prices_arrow_debreu.md).

---

## Worked Example: A Two-State, Two-Asset Economy

We now construct a concrete one-period model to illustrate all the definitions above.

!!! example "Example: Boom-Recession Economy"
    **Setup.** Consider an economy with two states and two assets:

    - **States**: $\Omega = \{\text{Boom}, \text{Recession}\}$, so $S = 2$.
    - **Probabilities**: $p_{\text{Boom}} = 0.6$, $p_{\text{Recession}} = 0.4$.
    - **Risk-free rate**: $r_f = 0.05$ (5% per period), so $\beta = 1/1.05 \approx 0.9524$.
    - **Assets**: a risk-free bond and a stock, so $N = 2$.

    **Prices at $t = 0$:**

    | Asset | Price $P_j$ |
    |:------|:---:|
    | Bond ($j = 1$) | \$1.00 |
    | Stock ($j = 2$) | \$50.00 |

    **Payoffs at $t = 1$:**

    | Asset | Boom | Recession |
    |:------|:---:|:---:|
    | Bond ($j = 1$) | \$1.05 | \$1.05 |
    | Stock ($j = 2$) | \$65.00 | \$40.00 |

    **Price vector and payoff matrix:**

    $$
    \mathbf{P} = \begin{pmatrix} 1.00 \\ 50.00 \end{pmatrix}, \quad \mathbf{X} = \begin{pmatrix} 1.05 & 1.05 \\ 65.00 & 40.00 \end{pmatrix}
    $$

    **Interpretation.** The bond pays \$1.05 regardless of which state occurs --- it is riskless. The stock pays \$65 in the boom (a 30% return) and \$40 in a recession (a $-$20% return). The expected stock payoff under the physical measure is:

    $$
    \mathbb{E}^{\mathbb{P}}[X_2] = 0.6 \times 65 + 0.4 \times 40 = 39 + 16 = 55
    $$

    The expected gross return on the stock is $55/50 = 1.10$, or 10%, which exceeds the risk-free rate of 5%. This **risk premium** compensates investors for bearing the uncertainty of the stock payoff.

---

## Matrix Formulation and Notation Summary

The one-period model has a clean linear-algebraic structure that makes it amenable to systematic analysis. We summarize the key notation here for reference.

| Symbol | Object | Dimension | Description |
|:---|:---|:---:|:---|
| $\Omega$ | State space | $S$ elements | $\{\omega_1, \ldots, \omega_S\}$ |
| $\mathbb{P}$ | Physical measure | --- | $p_s = \mathbb{P}(\omega_s) > 0$, $\sum p_s = 1$ |
| $\mathbf{P}$ | Price vector | $\mathbb{R}^N$ | Time-$0$ asset prices |
| $\mathbf{X}$ | Payoff matrix | $\mathbb{R}^{N \times S}$ | $X_{js}$ = payoff of asset $j$ in state $s$ |
| $r_f$ | Risk-free rate | $\mathbb{R}$ | Bond return: $B_1 = 1 + r_f$ |
| $\beta$ | Discount factor | $\mathbb{R}$ | $\beta = 1/(1 + r_f)$ |

The matrix $\mathbf{X}$ encodes the entire future of the economy. Its rows are asset payoff profiles; its columns are state-contingent payoff vectors. The relationship between $\mathbf{P}$ and $\mathbf{X}$ --- which price vectors are "consistent" with a given payoff matrix --- is the subject of the next three sections.

---

## Remarks on Generality

Several modeling choices deserve brief comment.

**Frictionless markets.** We assume that all assets can be bought and sold at the same price (no bid-ask spread), in any quantity (no position limits), and without transaction costs. These assumptions are relaxed in later chapters but are essential for the clean algebraic structure of the one-period model.

**No consumption or endowments.** The model specifies prices and payoffs but says nothing about where they come from. In a general equilibrium model, prices would be determined by agents' preferences and endowments. Here, we take prices as given and ask only whether they are arbitrage-free --- a weaker but more robust question.

**Finite states.** The restriction to finitely many states is not as severe as it first appears. Any continuous distribution can be approximated by a fine discrete grid, and the fundamental theorems of asset pricing hold in both settings. The finite case has the advantage that all proofs use only linear algebra, making the economic content transparent.

---

## What Comes Next

With the environment in place, the chapter continues as previewed in the roadmap above:

- [§ Portfolios and Payoffs](portfolios_and_payoffs.md) introduces the trading mechanics and the linearity of cost and payoff.
- [§ Arbitrage and Dominance](arbitrage_and_dominance.md) imposes the no-arbitrage condition and proves the FTAP.
- [§ State Prices](state_prices_arrow_debreu.md) interprets the resulting $\boldsymbol{\phi}$ as Arrow–Debreu prices and rescales it into a risk-neutral measure.

---

## Summary

| Component | Symbol | Role in the Model |
|:---|:---|:---|
| State space | $\Omega = \{\omega_1, \ldots, \omega_S\}$ | Enumerates all possible future scenarios |
| Probability measure | $\mathbb{P}$ with $p_s > 0$ | Assigns real-world likelihoods to states |
| Price vector | $\mathbf{P} \in \mathbb{R}^N$ | Known asset prices at $t = 0$ |
| Payoff matrix | $\mathbf{X} \in \mathbb{R}^{N \times S}$ | State-contingent asset payoffs at $t = 1$ |
| Risk-free bond | $B_0 = 1$, $B_1 = 1 + r_f$ | Anchors the time value of money |
| Discount factor | $\beta = 1/(1 + r_f)$ | Converts future values to present values |

The one-period market model provides the minimal mathematical setting in which the fundamental questions of asset pricing --- fair valuation, replication, and arbitrage --- can be posed and answered with full rigor.

---

## Exercises

**Exercise 1.** Consider a one-period market with $S = 3$ states $\Omega = \{\omega_1, \omega_2, \omega_3\}$ and $N = 2$ assets: a risk-free bond with $r_f = 0.03$ and a stock with price $P_2 = 40$. The stock payoffs are $X_{21} = 55$, $X_{22} = 42$, $X_{23} = 30$. Write down the price vector $\mathbf{P}$, the payoff matrix $\mathbf{X}$, and the discount factor $\beta$.

??? success "Solution to Exercise 1"
    The risk-free bond has price $P_1 = 1$ (by convention) and pays $1 + r_f = 1.03$ in every state. The stock has price $P_2 = 40$.

    **Price vector:**

    $$
    \mathbf{P} = \begin{pmatrix} 1 \\ 40 \end{pmatrix}
    $$

    **Payoff matrix** (rows = assets, columns = states):

    $$
    \mathbf{X} = \begin{pmatrix} 1.03 & 1.03 & 1.03 \\ 55 & 42 & 30 \end{pmatrix}
    $$

    **Discount factor:**

    $$
    \beta = \frac{1}{1 + r_f} = \frac{1}{1.03} \approx 0.9709
    $$

---

**Exercise 2.** In the Boom-Recession example from this section, suppose the stock payoff in the Boom state changes to $\$70$ while everything else remains the same. Compute the new expected stock payoff under $\mathbb{P}$ and the new expected gross return. Is the risk premium larger or smaller than in the original example?

??? success "Solution to Exercise 2"
    With the new stock payoff of \$70 in the Boom state and \$40 in the Recession state (unchanged), the expected stock payoff under $\mathbb{P}$ is:

    $$
    \mathbb{E}^{\mathbb{P}}[X_2] = 0.6 \times 70 + 0.4 \times 40 = 42 + 16 = 58
    $$

    The expected gross return on the stock is:

    $$
    \frac{\mathbb{E}^{\mathbb{P}}[X_2]}{P_2} = \frac{58}{50} = 1.16
    $$

    so the expected net return is $16\%$. The risk-free rate is $5\%$, so the risk premium is:

    $$
    16\% - 5\% = 11\%
    $$

    In the original example, the expected net return was $10\%$ and the risk premium was $5\%$. The new risk premium of $11\%$ is **larger** than the original $5\%$. This makes sense: the upside payoff increased (from \$65 to \$70) while the downside remained unchanged (\$40), increasing the spread between boom and recession payoffs, and thus the expected return.

---

**Exercise 3.** Prove that if the risk-free rate satisfies $r_f > 0$, then the discount factor satisfies $0 < \beta < 1$. What happens when $r_f = 0$? What happens when $-1 < r_f < 0$?

??? success "Solution to Exercise 3"
    Suppose $r_f > 0$. Then $1 + r_f > 1 > 0$, so the discount factor is:

    $$
    \beta = \frac{1}{1 + r_f}
    $$

    Since $1 + r_f > 0$, we have $\beta > 0$. Since $1 + r_f > 1$, we have $\beta = 1/(1 + r_f) < 1$. Thus $0 < \beta < 1$.

    **When $r_f = 0$:** We get $\beta = 1/(1 + 0) = 1$. There is no time value of money; a dollar today is worth exactly the same as a dollar tomorrow.

    **When $-1 < r_f < 0$:** We have $0 < 1 + r_f < 1$, so $\beta = 1/(1 + r_f) > 1$. A dollar tomorrow is worth more than a dollar today. This corresponds to a negative interest rate environment, where holding cash is penalized or deflation is expected.

---

**Exercise 4.** Consider a one-period model with $S = 4$ states and $N = 3$ assets (one risk-free bond and two risky stocks). Determine the maximum possible rank of the payoff matrix $\mathbf{X} \in \mathbb{R}^{3 \times 4}$. Under what condition on the rank is the market complete?

??? success "Solution to Exercise 4"
    The payoff matrix $\mathbf{X} \in \mathbb{R}^{3 \times 4}$ has 3 rows and 4 columns. By the rank inequality:

    $$
    \operatorname{rank}(\mathbf{X}) \leq \min(3, 4) = 3
    $$

    so the maximum possible rank is $3$.

    The market is complete when every contingent claim in $\mathbb{R}^S = \mathbb{R}^4$ can be replicated. This requires $\operatorname{rank}(\mathbf{X}) = S = 4$. However, since the maximum rank is $3 < 4$, **the market cannot be complete with only 3 assets and 4 states**, regardless of the specific payoff values. At least one more linearly independent asset is needed.

---

**Exercise 5.** In a one-period model with $S$ states and $N$ assets, suppose one of the risky assets has a payoff that is identical in every state: $X_{j1} = X_{j2} = \cdots = X_{jS} = c$ for some constant $c > 0$. Show that if $c \neq (1 + r_f) P_j$, then an arbitrage opportunity exists.

??? success "Solution to Exercise 5"
    Suppose asset $j$ has constant payoff $X_{js} = c > 0$ for all $s = 1, \ldots, S$, and $c \neq (1 + r_f)P_j$.

    The risk-free bond pays $1 + r_f$ in every state and has price $1$. Asset $j$ pays $c$ in every state, so it is also riskless. Consider the portfolio that buys $\alpha$ units of the bond and $\beta$ units of asset $j$, chosen to exploit the mispricing.

    **Case 1: $c > (1 + r_f)P_j$.** Asset $j$ offers a higher return than the risk-free rate. Form a portfolio: buy $1$ unit of asset $j$ and sell $c/(1 + r_f)$ units of the bond. The cost is:

    $$
    P_j - \frac{c}{1 + r_f} \cdot 1 = P_j - \frac{c}{1 + r_f} < 0
    $$

    since $c > (1 + r_f)P_j$ implies $P_j < c/(1 + r_f)$. The payoff in every state is:

    $$
    c - \frac{c}{1 + r_f} \cdot (1 + r_f) = c - c = 0
    $$

    This is a Type 2 arbitrage: the portfolio generates cash at $t = 0$ (negative cost) with zero payoff in every state.

    **Case 2: $c < (1 + r_f)P_j$.** Reverse the strategy: sell $1$ unit of asset $j$ and buy $c/(1 + r_f)$ units of the bond. The cost is $c/(1 + r_f) - P_j < 0$ and the payoff is $0$ in every state. Again a Type 2 arbitrage.

    In both cases, an arbitrage opportunity exists.

---

**Exercise 6.** A one-period market has $\Omega = \{\omega_1, \omega_2\}$ with $p_1 = 0.7$, $p_2 = 0.3$, and $r_f = 0.10$. The market contains a bond and a stock with $P_2 = 20$, $X_{21} = 28$, $X_{22} = 16$. Write the complete model specification $(\Omega, \mathbb{P}, N, \mathbf{P}, \mathbf{X}, r_f)$. Compute the expected return on the stock and the risk premium over the risk-free rate.

??? success "Solution to Exercise 6"
    **Complete model specification:**

    - $\Omega = \{\omega_1, \omega_2\}$ with $S = 2$
    - $\mathbb{P}$: $p_1 = 0.7$, $p_2 = 0.3$
    - $N = 2$ (bond and stock)
    - $r_f = 0.10$, so $\beta = 1/1.10 \approx 0.9091$

    **Price vector:**

    $$
    \mathbf{P} = \begin{pmatrix} 1 \\ 20 \end{pmatrix}
    $$

    **Payoff matrix:**

    $$
    \mathbf{X} = \begin{pmatrix} 1.10 & 1.10 \\ 28 & 16 \end{pmatrix}
    $$

    **Expected stock payoff:**

    $$
    \mathbb{E}^{\mathbb{P}}[X_2] = 0.7 \times 28 + 0.3 \times 16 = 19.6 + 4.8 = 24.4
    $$

    **Expected gross return on the stock:**

    $$
    \frac{\mathbb{E}^{\mathbb{P}}[X_2]}{P_2} = \frac{24.4}{20} = 1.22
    $$

    so the expected net return is $22\%$.

    **Risk premium:**

    $$
    22\% - 10\% = 12\%
    $$

    The stock's expected return of $22\%$ exceeds the risk-free rate of $10\%$ by a risk premium of $12\%$, compensating investors for bearing the uncertainty between the \$28 and \$16 payoffs.
