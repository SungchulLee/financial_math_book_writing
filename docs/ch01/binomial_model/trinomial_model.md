# Trinomial Model

## Introduction

The [binomial model](binomial_model.md) restricts the stock price to two possible outcomes at each time step: up or down. While this yields a clean, complete market in which every contingent claim can be uniquely replicated, real markets offer a richer set of possibilities. The **trinomial model** generalizes the binomial framework by allowing **three** possible price movements per period: up, middle, and down.

This seemingly minor extension has a profound structural consequence. With three possible states but only two traded assets (stock and bond), the payoff space of the market is two-dimensional while the state space is three-dimensional. As a result, **not every contingent claim can be replicated**, and the market becomes **incomplete**. The risk-neutral measure is no longer unique---there is an entire *family* of equivalent martingale measures, each producing a different arbitrage-free price for the same derivative.

The trinomial model thus serves a dual pedagogical purpose:

- **Computational**: the Boyle (1988) trinomial tree is a practical numerical method that often converges faster than the binomial tree
- **Conceptual**: it provides the simplest concrete example of market incompleteness, motivating the [Second Fundamental Theorem of Asset Pricing](../fundamental_theorem_of_asset_pricing/complete_markets_and_uniqueness.md)

!!! info "Prerequisites"
    - [Binomial Model](binomial_model.md): one-period setup, no-arbitrage condition, risk-neutral probability
    - [Replicating Portfolio](replicating_portfolio.md): portfolio construction and the notion of replication
    - [Risk-Neutral Measure](risk_neutral_measure.md): the measure $\mathbb{Q}$ and expectation pricing

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define the one-period trinomial model and identify its three possible stock price outcomes
    2. Derive the no-arbitrage condition for three states
    3. Characterize the set of risk-neutral measures and explain why it is not a singleton
    4. Prove that the trinomial market is incomplete by showing that replication fails for generic claims
    5. Compute the interval of no-arbitrage prices for a European contingent claim
    6. Describe the Boyle (1988) parameterization and its connection to matching moments

---

## One-Period Trinomial Model

### Setup

We work on a single period $t \in \{0, \Delta t\}$ with two traded assets.

**Risk-free asset (bank account).** Starting from $B_0 = 1$, the bank account grows deterministically:

$$
B_{\Delta t} = e^{r \Delta t}
$$

where $r \geq 0$ is the continuously compounded risk-free rate.

**Risky asset (stock).** Starting from $S_0 > 0$, the stock price at time $\Delta t$ takes one of **three** values:

$$
S_{\Delta t} =
\begin{cases}
u \, S_0 & \text{with probability } p_u \quad \text{(up state)} \\[6pt]
m \, S_0 & \text{with probability } p_m \quad \text{(middle state)} \\[6pt]
d \, S_0 & \text{with probability } p_d \quad \text{(down state)}
\end{cases}
$$

where the multiplicative factors satisfy $u > m > d > 0$ and the physical probabilities satisfy $p_u, p_m, p_d > 0$ with $p_u + p_m + p_d = 1$.

!!! note "Notation Convention"
    The middle factor $m$ is often chosen so that $m = 1$ (the stock price stays flat) or $m = e^{r \Delta t}$ (the stock earns the risk-free rate in the middle state). Neither convention is required---the theory works for any $m$ with $d < m < u$.

### The Sample Space

The one-period trinomial model lives on a finite probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with three states:

$$
\Omega = \{\omega_u, \omega_m, \omega_d\}
$$

The filtration is $\mathcal{F}_0 = \{\emptyset, \Omega\}$ (no information at time $0$) and $\mathcal{F}_{\Delta t} = 2^\Omega$ (full information at time $\Delta t$). A **contingent claim** is any $\mathcal{F}_{\Delta t}$-measurable random variable, which in this finite setting is simply a vector $H = (H_u, H_m, H_d)$ specifying the payoff in each state.

---

## No-Arbitrage Condition

### Portfolios

A portfolio $(\Delta, \beta)$ consists of $\Delta$ shares of stock and $\beta$ units of the bank account. Its value at each time is:

$$
V_0 = \Delta \, S_0 + \beta, \qquad V_{\Delta t} = \Delta \, S_{\Delta t} + \beta \, e^{r \Delta t}
$$

An **arbitrage** is a portfolio with $V_0 \leq 0$, $V_{\Delta t} \geq 0$ in all states, and $V_{\Delta t} > 0$ in at least one state.

### Derivation

The same logic as in the [binomial model](binomial_model.md) applies, but now the extreme states are $u$ and $d$.

**If $e^{r \Delta t} \geq u$:** short the stock, invest in the bank. Since $u > m > d$, the payoff $S_0 e^{r \Delta t} - S_{\Delta t}$ is non-negative in all three states and strictly positive in the middle and down states. This is an arbitrage.

**If $e^{r \Delta t} \leq d$:** buy the stock, borrow from the bank. The payoff $S_{\Delta t} - S_0 e^{r \Delta t}$ is non-negative in all three states and strictly positive in the middle and up states. This is an arbitrage.

**Conversely**, if $d < e^{r \Delta t} < u$, one can show that no portfolio $(\Delta, \beta)$ with $V_0 \leq 0$ achieves $V_{\Delta t} \geq 0$ in all three states with strict inequality somewhere (this follows from the First FTAP, or can be verified directly by solving the resulting linear system).

!!! success "No-Arbitrage Condition (Trinomial Model)"
    The one-period trinomial market is arbitrage-free if and only if:

    $$
    \boxed{d < e^{r \Delta t} < u}
    $$

    **Interpretation:** Exactly as in the binomial case, the risk-free return must lie strictly between the worst and best possible stock returns. The middle factor $m$ does not appear in the condition---it is the extreme states that determine whether arbitrage exists.

!!! tip "Why $m$ Does Not Matter"
    The no-arbitrage condition depends only on $d$ and $u$ because a portfolio that exploits a deterministic dominance of one asset over another must do so in *every* state. Only the extremes $d$ and $u$ are relevant for bounding the risk-free rate.

---

## Risk-Neutral Measures

### The Martingale Condition

A probability measure $\mathbb{Q}$ on $\Omega = \{\omega_u, \omega_m, \omega_d\}$ is a **risk-neutral measure** (equivalent martingale measure) if:

1. **Equivalence:** $\mathbb{Q}(\omega) > 0$ for every $\omega \in \Omega$, i.e., $q_u, q_m, q_d > 0$
2. **Normalization:** $q_u + q_m + q_d = 1$
3. **Martingale property:** The discounted stock price is a $\mathbb{Q}$-martingale:

$$
S_0 = e^{-r \Delta t} \, \mathbb{E}^{\mathbb{Q}}[S_{\Delta t}]
$$

Expanding the expectation and dividing by $S_0$:

$$
e^{r \Delta t} = q_u \, u + q_m \, m + q_d \, d
$$

### Characterizing the Set of Risk-Neutral Measures

We now have three unknowns $(q_u, q_m, q_d)$ subject to:

$$
q_u + q_m + q_d = 1
$$

$$
q_u \, u + q_m \, m + q_d \, d = e^{r \Delta t}
$$

$$
q_u > 0, \quad q_m > 0, \quad q_d > 0
$$

This is a system of **two** linear equations in **three** unknowns with positivity constraints. The solution set is a one-parameter family. Using the normalization constraint to eliminate $q_m = 1 - q_u - q_d$ and substituting into the martingale equation:

$$
q_u \, u + (1 - q_u - q_d) \, m + q_d \, d = e^{r \Delta t}
$$

$$
q_u (u - m) + q_d (d - m) = e^{r \Delta t} - m
$$

$$
q_u (u - m) - q_d (m - d) = e^{r \Delta t} - m
$$

We can parameterize the family by a free parameter. Let $q_d = \lambda$ where $\lambda > 0$. Then:

$$
q_u = \frac{e^{r \Delta t} - m + \lambda(m - d)}{u - m}
$$

$$
q_m = 1 - q_u - \lambda
$$

The constraints $q_u > 0$, $q_m > 0$, $q_d = \lambda > 0$ restrict $\lambda$ to an open interval $(\lambda_{\min}, \lambda_{\max})$.

!!! success "Family of Risk-Neutral Measures"
    Under the no-arbitrage condition $d < e^{r \Delta t} < u$, the set of risk-neutral measures for the trinomial model is a **one-parameter family** $\{(q_u(\lambda), q_m(\lambda), q_d(\lambda)) : \lambda \in (\lambda_{\min}, \lambda_{\max})\}$, where each member satisfies the martingale condition and strict positivity.

    In contrast, the [binomial model](binomial_model.md) has a **unique** risk-neutral measure $q = (e^{r\Delta t} - d)/(u - d)$.

### Geometric Interpretation

The martingale condition defines a **plane** (actually a line, after intersecting with the probability simplex) in the simplex $\{(q_u, q_m, q_d) : q_i \geq 0, \sum q_i = 1\}$. In the binomial model, two constraints on two unknowns yield a single point. In the trinomial model, two constraints on three unknowns yield a line segment in the interior of the simplex.

---

## Market Incompleteness

### Replication Failure

In the binomial model, any contingent claim $H = (H_u, H_d)$ can be replicated by choosing $(\Delta, \beta)$ to solve two equations in two unknowns. In the trinomial model, replication requires:

$$
\Delta \, u \, S_0 + \beta \, e^{r \Delta t} = H_u
$$

$$
\Delta \, m \, S_0 + \beta \, e^{r \Delta t} = H_m
$$

$$
\Delta \, d \, S_0 + \beta \, e^{r \Delta t} = H_d
$$

This is a system of **three** equations in **two** unknowns $(\Delta, \beta)$. Generically, such a system has **no** solution.

!!! warning "Incompleteness Theorem"
    **Proposition.** In the one-period trinomial model with two traded assets, a contingent claim $H = (H_u, H_m, H_d)$ is replicable if and only if:

    $$
    \frac{H_u - H_m}{(u - m) \, S_0} = \frac{H_m - H_d}{(m - d) \, S_0}
    $$

    That is, replication is possible only when the payoff differences are proportional to the stock price differences---the claim must be **affine** in $S_{\Delta t}$.

    **Proof sketch.** The first two equations determine $\Delta$ and $\beta$ uniquely. Substituting into the third equation yields the compatibility condition above. $\square$

Claims that fail this condition---such as a generic European call option---cannot be replicated. The market is **incomplete**.

### Connection to the Second Fundamental Theorem

The First FTAP states: *no-arbitrage if and only if there exists at least one risk-neutral measure*. The **Second FTAP** adds:

> The market is complete if and only if the risk-neutral measure is **unique**.

In the trinomial model:

- Risk-neutral measures exist (by no-arbitrage), so the First FTAP is satisfied
- Multiple risk-neutral measures exist, so by the Second FTAP, the market is **incomplete**

This connection is developed rigorously in [Complete Markets and Uniqueness](../fundamental_theorem_of_asset_pricing/complete_markets_and_uniqueness.md).

!!! tip "Completing the Market"
    To make the trinomial market complete, one could introduce a **third** traded asset (e.g., an option on the stock). With three assets and three states, the payoff matrix becomes $3 \times 3$ and generically invertible, restoring uniqueness of the risk-neutral measure. This is a common strategy in practice: liquid options serve as additional hedging instruments.

---

## No-Arbitrage Price Bounds

### The Pricing Interval

Since the risk-neutral measure is not unique, the risk-neutral pricing formula $V_0 = e^{-r \Delta t} \, \mathbb{E}^{\mathbb{Q}}[H]$ gives a **different** price for each choice of $\mathbb{Q}$. Every such price is consistent with no-arbitrage. The set of all no-arbitrage prices forms an **interval**:

$$
\boxed{V_0 \in \left( \inf_{\mathbb{Q} \in \mathcal{Q}} e^{-r \Delta t} \, \mathbb{E}^{\mathbb{Q}}[H], \; \sup_{\mathbb{Q} \in \mathcal{Q}} e^{-r \Delta t} \, \mathbb{E}^{\mathbb{Q}}[H] \right)}
$$

where $\mathcal{Q}$ is the set of all risk-neutral measures. The infimum and supremum are taken over the one-parameter family derived above.

!!! note "Open vs Closed Interval"
    For a non-replicable claim, the interval is **open**: the extreme prices correspond to degenerate measures where one of $q_u, q_m, q_d$ equals zero, violating the equivalence requirement. For a replicable claim, all measures agree and the interval collapses to a single point.

### Super-Replication Interpretation

The upper bound $\sup_{\mathbb{Q}} e^{-r \Delta t} \, \mathbb{E}^{\mathbb{Q}}[H]$ equals the cost of the cheapest portfolio that **super-replicates** $H$ (i.e., $V_{\Delta t} \geq H$ in every state). Similarly, the lower bound equals the negative of the super-replication cost of $-H$. These bounds have direct financial meaning:

- A **seller** of the claim needs at most the upper bound to hedge
- A **buyer** would pay at most the lower bound to avoid being overcharged relative to the market

Any price within the open interval is consistent with no-arbitrage, but the market does not determine a unique fair value. Additional criteria---such as utility maximization, model calibration, or risk preferences---are needed to select a specific price.

---

## The Boyle Parameterization

### Motivation

For computational purposes, we need a specific choice of $u$, $m$, $d$ (and often a specific risk-neutral measure) for the trinomial tree. **Boyle (1988)** proposed choosing parameters to match the **first two moments** (mean and variance) of the stock's log-return under the risk-neutral measure, plus an additional symmetry condition.

### Construction

Fix the time step $\Delta t$ and the volatility $\sigma > 0$. Boyle's parameterization sets:

$$
u = e^{\sigma \sqrt{2 \Delta t}}, \qquad m = 1, \qquad d = e^{-\sigma \sqrt{2 \Delta t}}
$$

Note that $u \, d = 1$ and $m = 1$ (the stock is unchanged in the middle state). The risk-neutral probabilities are chosen to match the mean and variance of $\ln(S_{\Delta t}/S_0)$:

$$
q_u = \left( \frac{e^{r \Delta t / 2} - e^{-\sigma \sqrt{\Delta t / 2}}}{e^{\sigma \sqrt{\Delta t / 2}} - e^{-\sigma \sqrt{\Delta t / 2}}} \right)^2
$$

$$
q_d = \left( \frac{e^{\sigma \sqrt{\Delta t / 2}} - e^{r \Delta t / 2}}{e^{\sigma \sqrt{\Delta t / 2}} - e^{-\sigma \sqrt{\Delta t / 2}}} \right)^2
$$

$$
q_m = 1 - q_u - q_d
$$

!!! note "Moment-Matching Property"
    By construction, $\mathbb{E}^{\mathbb{Q}}[S_{\Delta t}] = S_0 \, e^{r \Delta t}$ (martingale condition) and $\text{Var}^{\mathbb{Q}}[\ln(S_{\Delta t}/S_0)] = \sigma^2 \Delta t + O((\Delta t)^2)$. The two free parameters in the risk-neutral family are pinned down by matching the variance and imposing the symmetry $u \, d = 1$.

### Advantages of the Trinomial Tree

Compared to the Cox-Ross-Rubinstein binomial tree:

- **Three branches per node** produce a more refined lattice, often giving **faster convergence** to the continuous-time (Black-Scholes) price
- The lattice naturally **recombines**: an up-then-down path, a middle-then-middle path, and a down-then-up path can all reach the same node
- The extra degree of freedom allows **better moment matching** and more flexibility in fitting dividend yields or time-varying parameters
- Trinomial trees are especially natural for **interest rate models** (e.g., the Hull-White trinomial tree in [Chapter 20](../../ch20/codes/hull_white_trinomial_tree.py))

---

## Worked Example: European Call in the Trinomial Model

We now compute the interval of no-arbitrage prices for a European call option in a concrete one-period trinomial model.

### Parameters

$$
S_0 = 100, \quad u = 1.2, \quad m = 1.0, \quad d = 0.8, \quad r = 0.05, \quad \Delta t = 1 \text{ year}
$$

The risk-free growth factor is $e^{r \Delta t} = e^{0.05} \approx 1.05127$.

**Verify no-arbitrage:** $d = 0.8 < 1.05127 < 1.2 = u$. The condition holds.

### Stock and Call Payoffs

Consider a European call with strike $K = 100$:

| State | $S_{\Delta t}$ | Call payoff $H = (S_{\Delta t} - K)^+$ |
|-------|:----:|:----:|
| Up | $120$ | $20$ |
| Middle | $100$ | $0$ |
| Down | $80$ | $0$ |

### Is the Call Replicable?

Check the replication condition:

$$
\frac{H_u - H_m}{(u - m) \, S_0} = \frac{20 - 0}{(1.2 - 1.0)(100)} = \frac{20}{20} = 1
$$

$$
\frac{H_m - H_d}{(m - d) \, S_0} = \frac{0 - 0}{(1.0 - 0.8)(100)} = 0
$$

Since $1 \neq 0$, the call is **not replicable**. The market is incomplete for this claim.

### Computing the Price Interval

The risk-neutral probabilities must satisfy:

$$
q_u + q_m + q_d = 1
$$

$$
1.2 \, q_u + 1.0 \, q_m + 0.8 \, q_d = 1.05127
$$

Parameterize by $q_d = \lambda > 0$. From the two equations:

$$
q_u = \frac{1.05127 - 1.0 + \lambda(1.0 - 0.8)}{1.2 - 1.0} = \frac{0.05127 + 0.2\lambda}{0.2} = 0.25634 + \lambda
$$

$$
q_m = 1 - q_u - \lambda = 1 - 0.25634 - 2\lambda = 0.74366 - 2\lambda
$$

**Positivity constraints:**

- $q_d = \lambda > 0$: requires $\lambda > 0$
- $q_u = 0.25634 + \lambda > 0$: automatically satisfied for $\lambda > 0$
- $q_m = 0.74366 - 2\lambda > 0$: requires $\lambda < 0.37183$

So $\lambda \in (0, \, 0.37183)$.

**Call price as a function of $\lambda$:**

$$
V_0(\lambda) = e^{-0.05} \bigl( q_u \cdot 20 + q_m \cdot 0 + q_d \cdot 0 \bigr) = e^{-0.05} \cdot 20 \, q_u
$$

$$
V_0(\lambda) = e^{-0.05} \cdot 20 \, (0.25634 + \lambda) = 19.0246 \cdot (0.25634 + \lambda)
$$

**Bounds:**

- As $\lambda \to 0^+$: $V_0 \to 19.0246 \times 0.25634 \approx 4.877$
- As $\lambda \to 0.37183^-$: $V_0 \to 19.0246 \times (0.25634 + 0.37183) \approx 19.0246 \times 0.62817 \approx 11.949$

!!! example "Pricing Interval for the European Call"
    The no-arbitrage price interval for the European call with $K = 100$ is:

    $$
    V_0 \in (4.88, \; 11.95)
    $$

    Any price in this open interval is consistent with no-arbitrage. The market alone does not determine a unique fair value.

    For comparison, the **binomial model** with the same $u = 1.2$, $d = 0.8$ gives the unique price:

    $$
    V_0^{\text{bin}} = e^{-0.05} \cdot \frac{e^{0.05} - 0.8}{1.2 - 0.8} \cdot 20 = e^{-0.05} \cdot 0.62817 \cdot 20 \approx 11.95
    $$

    The binomial price coincides with the **upper bound** of the trinomial interval. This is because the binomial model is a special case where the middle state is absent, collapsing the family of measures to a single point at the upper end.

### Interpretation

The wide interval $(4.88, \, 11.95)$ reflects the fundamental pricing ambiguity in incomplete markets. In practice, a trader would narrow this interval by:

1. **Adding traded instruments**: if a second option is liquidly traded, its market price pins down additional constraints on $\mathbb{Q}$, shrinking the interval (or eliminating it entirely if the market becomes complete)
2. **Imposing a model**: choosing a specific parameterization (e.g., Boyle's) selects one $\mathbb{Q}$ from the family
3. **Utility-based pricing**: an agent's risk preferences select a unique price within the interval

---

## Summary

| Concept | Binomial Model | Trinomial Model |
|---------|:-:|:-:|
| States per period | 2 | 3 |
| Traded assets | 2 (stock + bond) | 2 (stock + bond) |
| No-arbitrage condition | $d < e^{r\Delta t} < u$ | $d < e^{r\Delta t} < u$ |
| Risk-neutral measures | Unique | One-parameter family |
| Market completeness | Complete | Incomplete |
| Derivative pricing | Unique price | Price interval |

!!! abstract "Key Takeaways"
    1. The trinomial model extends the binomial framework by adding a **middle state** $m$ with $d < m < u$, yielding three possible stock outcomes per period.

    2. The **no-arbitrage condition** $d < e^{r\Delta t} < u$ is identical in form to the binomial case---only the extreme factors matter.

    3. With two assets and three states, the system of martingale equations is **underdetermined**, producing a one-parameter family of risk-neutral measures. By the Second FTAP, this means the market is **incomplete**.

    4. For non-replicable claims, no-arbitrage determines only a **price interval** $(\inf_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-r\Delta t} H], \; \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-r\Delta t} H])$, not a unique price.

    5. The **Boyle (1988) parameterization** pins down specific values of $u$, $m$, $d$ and selects a risk-neutral measure by matching the mean and variance of log-returns, producing a practical trinomial tree for numerical pricing.

    6. The trinomial model provides the simplest concrete example of incomplete markets, motivating the general theory in the [FTAP section](../fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md).

---

## What's Next

| Section | Topic |
|---------|-------|
| [Binomial to Black-Scholes](binomial_to_black_scholes_limit.md) | Continuous-time limit of the binomial tree |
| [Complete Markets and Uniqueness](../fundamental_theorem_of_asset_pricing/complete_markets_and_uniqueness.md) | Second FTAP: uniqueness of $\mathbb{Q}$ and completeness |

---

## Exercises

**Exercise 1.** Consider the trinomial model with $S_0 = 100$, $u = 1.3$, $m = 1.05$, $d = 0.7$, $r = 5\%$, and $\Delta t = 1$. Verify the no-arbitrage condition. Then parameterize the family of risk-neutral measures by $q_d = \lambda$ and determine the admissible range of $\lambda$.

---

**Exercise 2.** Using the trinomial model from Exercise 1, compute the no-arbitrage price interval for a European put with strike $K = 100$. Express $V_0(\lambda)$ as a function of $\lambda$ and find the supremum and infimum over the admissible range. Compare the width of the interval to that of a call with the same strike.

---

**Exercise 3.** Prove that a contingent claim $H = (H_u, H_m, H_d)$ in the one-period trinomial model is replicable if and only if the payoff is **affine** in $S_{\Delta t}$, i.e., $H = a \cdot S_{\Delta t} + b$ for some constants $a, b$. Show that this is equivalent to the condition:

$$
\frac{H_u - H_m}{u - m} = \frac{H_m - H_d}{m - d}
$$

---

**Exercise 4.** In the worked example from the text ($S_0 = 100$, $u = 1.2$, $m = 1.0$, $d = 0.8$, $r = 5\%$), the binomial price of the call equals the upper bound of the trinomial interval. Prove this is not a coincidence: show that for any claim with $H_m = H_d$ (the middle and down payoffs coincide), the binomial price always equals the upper bound of the trinomial price interval.

---

**Exercise 5.** Suppose the trinomial market is "completed" by adding a traded European call option with strike $K = 100$ and observed market price $C_0 = 8.50$ (using the same parameters as the worked example in the text). With three assets (stock, bond, call) and three states, the risk-neutral measure becomes unique. Find the unique risk-neutral measure $(q_u, q_m, q_d)$ and use it to price a European put with strike $K = 110$.

---

**Exercise 6.** For the Boyle (1988) parameterization with $\sigma = 0.20$, $r = 0.05$, and $\Delta t = 0.25$, compute $u$, $m$, $d$, $q_u$, $q_d$, and $q_m$. Verify that (a) $q_u + q_m + q_d = 1$, (b) the martingale condition $q_u u + q_m m + q_d d = e^{r\Delta t}$ holds, and (c) $\text{Var}^{\mathbb{Q}}[\ln(S_{\Delta t}/S_0)] \approx \sigma^2 \Delta t$.
