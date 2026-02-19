# Chapter 1: Discrete Models and the Fundamental Theorem of Asset Pricing

This chapter builds the theory of arbitrage-free pricing in discrete-time, finite-state markets. Starting from simple one-period models and Arrow-Debreu securities, we develop the binomial option pricing framework through replication, delta hedging, and risk-neutral expectation. The chapter culminates in the Fundamental Theorem of Asset Pricing, which establishes the deep equivalence between no-arbitrage and the existence of an equivalent martingale measure.

## Key Concepts

**Discrete-Time Foundations**
A single-period economy consists of $N$ traded assets across $S$ possible future states, organized into a payoff matrix $\mathbf{X} \in \mathbb{R}^{N \times S}$. A portfolio $\theta$ generates payoff $\theta^\top \mathbf{X}$ across states. An **arbitrage** is a portfolio with zero or negative cost and non-negative payoff in all states, with strict positivity in at least one. **Arrow-Debreu securities** pay one unit in exactly one state and zero otherwise; their prices $\psi_s > 0$ form **state prices** that encode the market's valuation of contingent claims:

$$V_0 = \sum_{s=1}^{S} \psi_s \, X(\omega_s)$$

State prices exist if and only if the market is arbitrage-free, and they are unique if and only if the market is complete.

**The Binomial Model**
The Cox-Ross-Rubinstein (1979) model assumes the stock price moves by multiplicative factors $u$ (up) or $d$ (down) at each step. The no-arbitrage condition requires 

$$d < e^{r\Delta t} < u$$ 

Three equivalent approaches yield the same derivative price:

- *Replicating portfolio*: find $(\Delta, B)$ in stock and bond matching the payoff in both states
- *Delta hedging*: combine the option with $\Delta$ shares of stock to eliminate risk; the risk-free portfolio must earn rate $r$
- *Risk-neutral pricing*: compute the discounted expectation under the risk-neutral probability $q = \frac{e^{r\Delta t} - d}{u - d}$  

$$V_0 = e^{-r\Delta t}\bigl[q\,V_u + (1-q)\,V_d\bigr]$$


Under the risk-neutral measure, the discounted stock price is a martingale: 

$$S_0 = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_1]$$

**Multi-Period Extension**
The multi-period binomial tree prices options via **backward induction**, applying the one-period formula recursively from terminal nodes to time zero. Dynamic delta hedging rebalances the hedge ratio at each node. American options introduce **optimal stopping**: at each node, the holder compares the continuation value with the immediate exercise payoff, leading to the recursion 

$$V_i = \max\bigl(\Phi(S_i),\; e^{-r\Delta t}[q\,V_{i+1}^u + (1-q)\,V_{i+1}^d]\bigr)$$ 

The trinomial model, with three possible moves per step, illustrates **incomplete markets** where the risk-neutral measure is no longer unique.

**Binomial to Black-Scholes Limit**
As the number of time steps $n \to \infty$ with $\Delta t = T/n \to 0$, the binomial model converges to the Black-Scholes framework. The scaled random walk converges to Brownian motion via **Donsker's theorem**, log-prices become normally distributed by the central limit theorem, and the discrete pricing recursion converges to the Black-Scholes PDE. The Ito correction term $-\frac{1}{2}\sigma^2$ emerges naturally from the discrete-to-continuous passage.

**The Fundamental Theorem of Asset Pricing**
The FTAP establishes two fundamental equivalences:

- *First FTAP*: The market is arbitrage-free if and only if there exists an equivalent martingale measure $\mathbb{Q} \sim \mathbb{P}$ under which discounted prices $\tilde{S}^i_t = S^i_t / S^0_t$ are martingales
- *Second FTAP*: The market is complete if and only if the equivalent martingale measure is unique

The proof in the finite-state case relies on the **separating hyperplane theorem**: if no arbitrage exists, the set of attainable portfolio gains and the positive orthant are disjoint convex sets, and the separating functional defines the state prices (or equivalently, the Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$).

**Numeraire and Change of Measure**
A numeraire is any strictly positive traded asset $N_t$. The FTAP generalizes: for each numeraire there exists an associated martingale measure $\mathbb{Q}^N$ under which prices normalized by $N_t$ are martingales. The **change of numeraire theorem** relates these measures via the Radon-Nikodym derivative. Prices are invariant under numeraire changes—different numeraires yield different measures but identical arbitrage-free prices. This invariance is one of the most powerful computational tools in quantitative finance.

!!! note "From Discrete to Continuous"
    The discrete-time framework developed here provides the conceptual foundation for continuous-time models. Chapter 2 introduces Brownian motion and martingale theory, Chapter 3 develops stochastic calculus, and Chapter 6 derives the Black-Scholes model as the continuous-time limit of the binomial framework.

---
