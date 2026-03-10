# Chapter 1: Discrete Models and the Fundamental Theorem of Asset Pricing

!!! warning "Incomplete page"
    This is a chapter index page and does not follow the five-section structure.

This chapter builds the theory of arbitrage-free pricing in discrete-time, finite-state markets. Starting from simple one-period models and Arrow-Debreu securities, we develop the binomial option pricing framework through replication, delta hedging, and risk-neutral expectation. The chapter culminates in the Fundamental Theorem of Asset Pricing, which establishes the deep equivalence between no-arbitrage and the existence of an equivalent martingale measure.

## Key Concepts

### Discrete-Time Foundations

A single-period economy consists of $N$ traded assets across $S$ possible future states, organized into a payoff matrix $\mathbf{X} \in \mathbb{R}^{N \times S}$. A portfolio $\theta$ generates payoff $\theta^\top \mathbf{X}$ across states. An **arbitrage** is a portfolio with zero or negative cost and non-negative payoff in all states, with strict positivity in at least one. **Arrow-Debreu securities** pay one unit in exactly one state and zero otherwise; their prices $\psi_s > 0$ form **state prices** that encode the market's valuation of contingent claims:

$$
V_0 = \sum_{s=1}^{S} \psi_s \, X(\omega_s)
$$

State prices exist if and only if the market is arbitrage-free, and they are unique if and only if the market is complete. The **stochastic discount factor** (pricing kernel) $m_s = \psi_s / p_s$ connects state prices to physical probabilities, enabling the pricing formula $P_j = \mathbb{E}^{\mathbb{P}}[m \cdot X_j]$.

### The Binomial Model

The Cox-Ross-Rubinstein (1979) model assumes the stock price moves by multiplicative factors $u$ (up) or $d$ (down) at each step. The no-arbitrage condition requires

$$
d < e^{r\Delta t} < u
$$

Three equivalent approaches yield the same derivative price:

- **Replicating portfolio**: find $(\Delta, B)$ in stock and bond matching the payoff in both states
- **Delta hedging**: combine the option with $\Delta$ shares to eliminate risk; the risk-free portfolio must earn rate $r$
- **Risk-neutral pricing**: compute the discounted expectation under the risk-neutral probability $q = (e^{r\Delta t} - d)/(u - d)$

$$
V_0 = e^{-r\Delta t}\bigl[q\,V_u + (1-q)\,V_d\bigr]
$$

Under the risk-neutral measure, the discounted stock price is a martingale: $S_0 = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_1]$.

### Multi-Period Extension and American Options

The multi-period binomial tree prices options via **backward induction**, applying the one-period formula recursively from terminal nodes to time zero. American options introduce **optimal stopping**: at each node, the holder compares the continuation value with the immediate exercise payoff:

$$
V_i = \max\bigl(\Phi(S_i),\; e^{-r\Delta t}[q\,V_{i+1}^u + (1-q)\,V_{i+1}^d]\bigr)
$$

For American calls on non-dividend-paying stocks, early exercise is never optimal.

### Binomial to Black-Scholes Limit

As the number of time steps $n \to \infty$ with $\Delta t = T/n \to 0$, the binomial model converges to the Black-Scholes framework. Taylor expansion of the backward recursion yields the **Black-Scholes PDE**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

### The Fundamental Theorem of Asset Pricing

The FTAP establishes two fundamental equivalences:

- **First FTAP**: The market is arbitrage-free if and only if there exists an equivalent martingale measure $\mathbb{Q} \sim \mathbb{P}$ under which discounted prices are martingales
- **Second FTAP**: The market is complete if and only if the equivalent martingale measure is unique

### Numeraire and Change of Measure

A numeraire is any strictly positive traded asset $N_t$. The master pricing formula

$$
V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}[\Phi_T / N_T \mid \mathcal{F}_t]
$$

unifies all standard pricing expressions. Prices are invariant under numeraire changes.

!!! note "From Discrete to Continuous"
    The discrete-time framework developed here provides the conceptual foundation for continuous-time models. Chapter 2 introduces Brownian motion and martingale theory, Chapter 3 develops stochastic calculus, and Chapter 6 derives the Black-Scholes model as the continuous-time limit of the binomial framework.
