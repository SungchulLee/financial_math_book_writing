# Chapter 1: Discrete Models and the Fundamental Theorem of Asset Pricing

This chapter builds the theory of arbitrage-free pricing in discrete-time, finite-state markets. Starting from simple one-period models and Arrow-Debreu securities, we develop the binomial option pricing framework through replication, delta hedging, and risk-neutral expectation. The chapter culminates in the Fundamental Theorem of Asset Pricing, which establishes the deep equivalence between no-arbitrage and the existence of an equivalent martingale measure.

## Key Concepts

**Discrete-Time Foundations**
A single-period economy consists of $N$ traded assets across $S$ possible future states, organized into a payoff matrix $\mathbf{X} \in \mathbb{R}^{N \times S}$. A portfolio $\theta$ generates payoff $\theta^\top \mathbf{X}$ across states. An **arbitrage** is a portfolio with zero or negative cost and non-negative payoff in all states, with strict positivity in at least one. **Arrow-Debreu securities** pay one unit in exactly one state and zero otherwise; their prices $\psi_s > 0$ form **state prices** that encode the market's valuation of contingent claims:

$$V_0 = \sum_{s=1}^{S} \psi_s \, X(\omega_s)$$

State prices exist if and only if the market is arbitrage-free, and they are unique if and only if the market is complete. The **stochastic discount factor** (pricing kernel) $m_s = \psi_s / p_s$ connects state prices to physical probabilities, enabling the pricing formula $P_j = \mathbb{E}^{\mathbb{P}}[m \cdot X_j]$. The **Breeden-Litzenberger result** shows how state price densities can be extracted from European option prices via $\phi(K) = e^{r_f T} \partial^2 C / \partial K^2$, providing a bridge between theory and market observables.

**The Binomial Model**
The Cox-Ross-Rubinstein (1979) model assumes the stock price moves by multiplicative factors $u$ (up) or $d$ (down) at each step. The no-arbitrage condition requires

$$d < e^{r\Delta t} < u$$

Three equivalent approaches yield the same derivative price:

- *Replicating portfolio*: find $(\Delta, B)$ in stock and bond matching the payoff in both states, with the hedge ratio $\Delta = \frac{H_u - H_d}{(u-d)S_0}$ and the state price formula $V_0 = \psi_u H_u + \psi_d H_d$ where $\psi_u = e^{-r\Delta t} q$ and $\psi_d = e^{-r\Delta t}(1-q)$
- *Delta hedging*: combine the option with $\Delta$ shares of stock to eliminate risk; the risk-free portfolio must earn rate $r$, and the risk-neutral probability emerges from the hedging argument without being assumed a priori
- *Risk-neutral pricing*: compute the discounted expectation under the risk-neutral probability $q = \frac{e^{r\Delta t} - d}{u - d}$

$$V_0 = e^{-r\Delta t}\bigl[q\,V_u + (1-q)\,V_d\bigr]$$


Under the risk-neutral measure, the discounted stock price is a martingale:

$$S_0 = e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[S_1]$$

Risk-neutral pricing is linear in payoffs, enabling decomposition of complex structures (e.g., bull spreads, put-call parity $C_0 - P_0 = S_0 - Ke^{-r\Delta t}$) into simpler components.

**Multi-Period Extension and American Options**
The multi-period binomial tree prices options via **backward induction**, applying the one-period formula recursively from terminal nodes to time zero. At node $(n,j)$, the stock price is $S_{n,j} = S_0 u^j d^{n-j}$, and the recombining property $ud = 1$ ensures only $n+1$ nodes at time $n$ (yielding $O(N^2)$ computational complexity). Dynamic delta hedging rebalances the hedge ratio $\Delta_{n,j} = \frac{V_{n+1,j+1} - V_{n+1,j}}{S_{n,j}(u-d)}$ at each node, with the **self-financing property** ensuring no external cash is injected during rebalancing. American options introduce **optimal stopping**: at each node, the holder compares the continuation value with the immediate exercise payoff, leading to the recursion

$$V_i = \max\bigl(\Phi(S_i),\; e^{-r\Delta t}[q\,V_{i+1}^u + (1-q)\,V_{i+1}^d]\bigr)$$

The **early exercise boundary** identifies critical stock prices where immediate exercise becomes optimal. For American calls on non-dividend-paying stocks, early exercise is never optimal. The **trinomial model**, with three possible moves per step, illustrates **incomplete markets** where the risk-neutral measure is no longer unique.

**Binomial to Black-Scholes Limit**
As the number of time steps $n \to \infty$ with $\Delta t = T/n \to 0$, the binomial model converges to the Black-Scholes framework. With the CRR parameterization $u = e^{\sigma\sqrt{\Delta t}}$ and $d = e^{-\sigma\sqrt{\Delta t}}$, the scaled random walk converges to Brownian motion via **Donsker's theorem**, log-prices become normally distributed by the central limit theorem, and the risk-neutral probability approaches $q \to 1/2$. The **Ito correction term** $-\frac{1}{2}\sigma^2$ emerges from Jensen's inequality applied to the concave logarithm: the martingale condition constrains the arithmetic return $\mathbb{E}^{\mathbb{Q}}[S_{i+1}|S_i] = S_i e^{r\Delta t}$, but $\mathbb{E}[\ln R_i] \approx (r - \sigma^2/2)\Delta t$ due to the gap between $\mathbb{E}[\ln X]$ and $\ln \mathbb{E}[X]$. Taylor expansion of the backward recursion yields the **Black-Scholes PDE**:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

The discrete delta converges to $\partial V / \partial S = \Phi(d_1)$, and binomial option prices converge at rate $O(1/n)$ with oscillations between odd and even steps that can be smoothed by Richardson extrapolation.

**The Fundamental Theorem of Asset Pricing**
The FTAP establishes two fundamental equivalences:

- *First FTAP*: The market is arbitrage-free if and only if there exists an equivalent martingale measure $\mathbb{Q} \sim \mathbb{P}$ under which discounted prices $\tilde{S}^i_t = S^i_t / S^0_t$ are martingales
- *Second FTAP*: The market is complete if and only if the equivalent martingale measure is unique

The proof in the finite-state case relies on the **separating hyperplane theorem**: if no arbitrage exists, the set of attainable portfolio gains $\mathcal{V} = \operatorname{Im}(X)$ and the positive orthant $\mathbb{R}^n_{++}$ are disjoint convex sets, and the separating functional defines the state prices (or equivalently, the Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$). The key geometric insight is that the separating vector $q$ satisfies $X^T q = 0$ with $q_i > 0$ for all states, which after normalization becomes the EMM. Related results include **Farkas' lemma** (the linear programming incarnation) and **Minkowski's separation theorem** for relative interiors. In continuous time, the condition strengthens to **No Free Lunch with Vanishing Risk (NFLVR)**, and the Delbaen-Schachermayer theorem (1994) establishes the equivalence via the **Kreps-Yan theorem** (a functional-analytic extension of separating hyperplanes to $L^\infty$ spaces). The connection to Girsanov theory provides the explicit measure change $d\mathbb{Q}/d\mathbb{P} = \mathcal{E}(-\int_0^T \lambda_s\, dW_s)$ where $\lambda_t = (\mu_t - r)/\sigma_t$ is the market price of risk.

**Numeraire and Change of Measure**
A numeraire is any strictly positive traded asset $N_t$. The FTAP generalizes: for each numeraire there exists an associated martingale measure $\mathbb{Q}^N$ under which prices normalized by $N_t$ are martingales. The **change of numeraire theorem** relates these measures via the Radon-Nikodym derivative $\frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}\big|_{\mathcal{F}_t} = \frac{M_t/M_0}{N_t/N_0}$, and the master pricing formula $V_t = N_t \cdot \mathbb{E}^{\mathbb{Q}^N}[\Phi_T / N_T \mid \mathcal{F}_t]$ unifies all standard pricing expressions. Prices are invariant under numeraire changes---different numeraires yield different measures but identical arbitrage-free prices. Key applications include the **forward measure** $\mathbb{Q}^T$ (using zero-coupon bond $P(t,T)$ as numeraire, which eliminates discounting from interest-rate derivative pricing) and **Margrabe's formula** for exchange options (using one asset as numeraire to reduce a two-dimensional problem to a one-dimensional Black-Scholes integral): $V_0 = S^1_0 \Phi(d_1) - S^2_0 \Phi(d_2)$ with $\sigma_R = \sqrt{\sigma_1^2 - 2\rho\sigma_1\sigma_2 + \sigma_2^2}$.

!!! note "From Discrete to Continuous"
    The discrete-time framework developed here provides the conceptual foundation for continuous-time models. Chapter 2 introduces Brownian motion and martingale theory, Chapter 3 develops stochastic calculus, and Chapter 6 derives the Black-Scholes model as the continuous-time limit of the binomial framework.

---
