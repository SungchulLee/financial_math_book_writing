# Algorithmic Trading and Mean Field Games

In modern electronic markets, thousands of algorithmic traders execute orders simultaneously, each optimizing their own execution strategy while collectively shaping the price dynamics that all participants face. Analyzing this many-agent interaction directly is intractable for large populations. **Mean field game (MFG) theory** resolves this by replacing the $N$-player game with a representative agent who interacts with the statistical distribution of all agents. This section develops the framework from finite-player trading games through the mean field limit, derives the equilibrium conditions for optimal execution, and examines the interplay between individual optimization and aggregate price impact.

---

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - The formulation of $N$-player optimal execution games with price impact
    - The mean field limit as $N \to \infty$ and the resulting McKean-Vlasov dynamics
    - The MFG fixed-point problem: forward Fokker-Planck and backward Hamilton-Jacobi-Bellman equations
    - Nash equilibrium characterization for optimal execution in continuous time
    - How aggregate trading behavior feeds back into price dynamics

---

## Optimal Execution: Single Agent

### The Almgren-Chriss Framework

Before introducing strategic interaction, recall the single-agent optimal execution problem. A trader must liquidate $Q$ shares over the interval $[0, T]$. Let $q_t$ denote the remaining inventory at time $t$ and $\dot{q}_t = -v_t$ the (negative of the) trading rate.

The asset price is affected by both permanent and temporary impact:

$$
S_t = S_0 + \sigma W_t - g\!\int_0^t v_s\,ds
$$

$$
\tilde{S}_t = S_t - \eta\, v_t
$$

where $g$ is the permanent impact parameter, $\eta$ is the temporary impact parameter, $\sigma$ is volatility, and $W_t$ is a Brownian motion.

The trader minimizes expected cost plus a risk penalty:

$$
\min_{v} \;\mathbb{E}\!\left[\int_0^T (\eta\, v_t^2 + g\, v_t\, q_t)\,dt + \lambda \int_0^T \sigma^2 q_t^2\,dt\right]
$$

subject to $q_0 = Q$ and $q_T = 0$.

The first integral captures execution cost (temporary and permanent impact); the second captures inventory risk (penalized by risk aversion $\lambda$).

### Single-Agent Optimal Strategy

The Euler-Lagrange equation yields the optimal trading rate:

$$
v_t^* = \frac{\kappa\, Q}{\sinh(\kappa T)} \cosh\!\big(\kappa(T-t)\big)
$$

where $\kappa = \sqrt{\lambda \sigma^2 / \eta}$. This is the well-known **Almgren-Chriss TWAP-to-VWAP** solution: for low risk aversion ($\kappa T$ small), the strategy approaches uniform execution (TWAP); for high risk aversion, execution is front-loaded.

---

## N-Player Trading Game

### Setup

Consider $N$ traders, each liquidating an initial inventory $Q^i$. Trader $i$ chooses a trading rate $v_t^i$ to minimize their own cost, but the price is now affected by *all* traders:

$$
S_t = S_0 + \sigma W_t - g \sum_{j=1}^N \int_0^t v_s^j\,ds
$$

The execution price for trader $i$ includes temporary impact:

$$
\tilde{S}_t^i = S_t - \eta\, v_t^i
$$

### Individual Optimization

Each trader $i$ minimizes:

$$
J^i(v^i; v^{-i}) = \mathbb{E}\!\left[\int_0^T \left(\eta\,(v_t^i)^2 + g\, v_t^i\, q_t^i + g\, v_t^i \sum_{j \neq i} q_t^j\right)dt + \lambda \int_0^T \sigma^2 (q_t^i)^2\,dt\right]
$$

subject to $q_0^i = Q^i$, $q_T^i = 0$, where $v^{-i}$ denotes the strategies of all other traders.

The key difficulty is that trader $i$'s optimal strategy depends on the strategies of all other traders through the permanent impact term. This creates a **game-theoretic coupling**.

### Nash Equilibrium

A strategy profile $(v^{1,*}, \ldots, v^{N,*})$ is a **Nash equilibrium** if no trader can reduce their cost by unilaterally deviating:

$$
J^i(v^{i,*}; v^{-i,*}) \leq J^i(v^i; v^{-i,*}) \quad \text{for all admissible } v^i, \; i = 1, \ldots, N
$$

For the linear-quadratic structure above, the Nash equilibrium can be characterized by a system of coupled ODEs.

??? example "Two-Player Game"
    With $N = 2$ symmetric traders ($Q^1 = Q^2 = Q$, same $\lambda$), the Nash equilibrium trading rates satisfy a coupled system. By symmetry, both traders use the same strategy. The equilibrium rate is:

    $$
    v_t^{*} = \frac{\tilde{\kappa}\, Q}{\sinh(\tilde{\kappa} T)} \cosh\!\big(\tilde{\kappa}(T-t)\big)
    $$

    where $\tilde{\kappa}$ depends on $(g, \eta, \lambda, \sigma)$ and the number of players. Compared to the single-agent solution, each trader trades *faster* because of the additional permanent impact from the other trader---a **predatory trading** incentive.

---

## The Mean Field Limit

### Motivation

For large $N$, tracking each player's strategy individually is intractable. The **mean field approximation** replaces the influence of the other $N-1$ players with their aggregate statistical distribution.

### Empirical Distribution

Define the empirical measure of inventories:

$$
\mu_t^N = \frac{1}{N}\sum_{i=1}^N \delta_{q_t^i}
$$

As $N \to \infty$, under appropriate conditions, $\mu_t^N$ converges to a deterministic measure $\mu_t$, the **mean field**.

### Mean Field Interaction

In the mean field limit, the permanent impact from all traders is:

$$
g \sum_{j=1}^N v_t^j \;\to\; g\, N \int v_t(q)\,\mu_t(dq) = g\, N\, \bar{v}_t
$$

where $\bar{v}_t = \int v_t(q)\,\mu_t(dq)$ is the average trading rate across the population.

A representative trader faces the price dynamics:

$$
dS_t = \sigma\, dW_t - g\, N\, \bar{v}_t\, dt
$$

and optimizes against this aggregate, taking $\bar{v}_t$ as given.

---

## Mean Field Game Formulation

### The MFG System

The mean field game equilibrium is characterized by a coupled system of two PDEs:

**1. Hamilton-Jacobi-Bellman (backward):** The value function $u(t, q)$ of the representative trader satisfies:

$$
-\partial_t u - \frac{\sigma_q^2}{2}\,\partial_{qq} u + H(q, \partial_q u, \mu_t) = 0
$$

with terminal condition $u(T, q) = \Phi(q)$ (penalty for residual inventory).

The Hamiltonian for the optimal execution problem is:

$$
H(q, p, \mu) = \inf_{v}\!\left\{\eta\, v^2 + g\, v\, q + g\, v\!\int q'\,\mu(dq') + \lambda\sigma^2 q^2 - v\, p\right\}
$$

The infimum is attained at:

$$
v^*(q, p, \mu) = \frac{p - g\,q - g\!\int q'\,\mu(dq')}{2\eta}
$$

**2. Fokker-Planck (forward):** The distribution $\mu_t$ of inventories evolves according to:

$$
\partial_t \mu + \partial_q\!\big(v^*(q, \partial_q u, \mu_t)\,\mu\big) = \frac{\sigma_q^2}{2}\,\partial_{qq}\mu
$$

with initial condition $\mu_0$ = initial distribution of inventories across traders.

### Fixed-Point Structure

The MFG system has a **fixed-point structure**:

1. Given $\mu_t$, solve the HJB equation backward to get $u$ and the optimal control $v^*$
2. Given $v^*$, solve the Fokker-Planck equation forward to get the resulting distribution $\mu_t$
3. At equilibrium, the two must be consistent: the distribution generated by $v^*$ equals the distribution assumed when computing $v^*$

!!! note "Existence and Uniqueness"
    For the linear-quadratic optimal execution problem, the MFG system admits a unique solution under standard regularity conditions. This follows from the **monotonicity condition** of Lasry and Lions: the cost functional is displacement monotone when the permanent impact $g > 0$, which ensures uniqueness of the mean field equilibrium.

---

## Linear-Quadratic MFG for Optimal Execution

### Closed-Form Solution

When the cost functional is quadratic and the dynamics are linear, the MFG admits a closed-form solution. Assume all traders start with the same inventory $Q$ and face the problem:

$$
\min_{v} \;\mathbb{E}\!\left[\int_0^T \left(\eta\, v_t^2 + g\, v_t\,(q_t + \bar{q}_t) + \lambda\sigma^2 q_t^2\right)dt + c\, q_T^2\right]
$$

where $\bar{q}_t = \mathbb{E}[q_t]$ under the mean field distribution.

The optimal trading rate is:

$$
v_t^* = A(t)\, q_t + B(t)\,\bar{q}_t
$$

where $A(t)$ and $B(t)$ satisfy a system of Riccati equations:

$$
\dot{A} = \frac{(A+g)^2}{4\eta} + \frac{(A+g)B}{2\eta} - \lambda\sigma^2, \quad A(T) = -\frac{c}{\eta}
$$

$$
\dot{B} = \frac{B^2}{4\eta} + \frac{(A+g)B}{2\eta} + \frac{g\,A}{2\eta}, \quad B(T) = 0
$$

### Mean Field Equilibrium Inventory

The average inventory evolves as:

$$
\frac{d\bar{q}_t}{dt} = -\big(A(t) + B(t)\big)\,\bar{q}_t
$$

At equilibrium, the aggregate liquidation schedule is smoother than the individual one, because the mean field feedback tempers aggressive trading.

### Comparison with $N$-Player Equilibrium

**Theorem (Cardaliaguet-Lehalle, 2018).** The MFG equilibrium approximates the $N$-player Nash equilibrium with error:

$$
\left|J^{i,N}_{\text{Nash}} - J^{\text{MFG}}\right| = O\!\left(\frac{1}{\sqrt{N}}\right)
$$

This convergence justifies the mean field approximation for markets with many participants. $\square$

---

## Price Impact in the MFG Framework

### Endogenous Price Formation

In the MFG equilibrium, the price process becomes:

$$
S_t = S_0 + \sigma W_t - g\, N \int_0^t \big(A(s) + B(s)\big)\,\bar{q}_s\,ds
$$

The price impact is **endogenous**: it arises from the equilibrium strategies of all traders rather than being exogenously specified. This is a key advantage of the MFG approach over reduced-form impact models.

### Permanent vs Temporary Impact

- **Temporary impact** ($\eta v_t$) arises from individual order flow and vanishes immediately
- **Permanent impact** ($g \int v_t\,dt$) arises from aggregate order flow and persists

In the MFG framework, the permanent impact is determined by the equilibrium distribution of trading rates, creating a feedback loop between individual strategies and aggregate price dynamics.

!!! info "Connection to Market Microstructure"
    The MFG framework bridges two traditionally separate literatures:

    - **Market microstructure:** Studies price formation at the order-book level
    - **Optimal execution:** Studies the trader's optimization problem taking impact as given

    Mean field games unify these by endogenizing price impact through the equilibrium of many optimizing agents. This connects to the endogenous price dynamics discussed in the sibling section.

---

## Extensions

### Heterogeneous Agents

In practice, traders differ in:

- Initial inventories $Q^i$
- Risk aversion parameters $\lambda^i$
- Urgency (terminal penalties $c^i$)
- Information sets

The MFG framework accommodates heterogeneity by allowing the mean field distribution to represent a mixture of agent types. The fixed-point problem becomes higher-dimensional but retains the same structure.

### Major-Minor Player Models

When some players (e.g., large institutional investors) are too large to be treated as part of the mean field, the framework extends to **major-minor** MFGs:

- **Minor players:** A continuum of small traders described by the mean field
- **Major player:** A single large trader who influences and is influenced by the mean field

The equilibrium is characterized by a coupled system of HJB equations for both the major player and the representative minor player.

### High-Frequency Limit Order Book Models

At higher frequencies, the MFG framework can model the dynamics of the limit order book itself:

- Agents choose to place limit or market orders
- The state variable includes queue position
- The mean field captures the aggregate order flow distribution

---

## Key Takeaways

- In $N$-player trading games, each trader's optimal strategy depends on all others through aggregate price impact, creating a Nash equilibrium problem
- The mean field limit replaces the $N$-player interaction with a representative agent facing the statistical distribution of the population
- The MFG equilibrium is characterized by a coupled HJB (backward) and Fokker-Planck (forward) system
- For linear-quadratic optimal execution, closed-form solutions exist via Riccati equations
- The MFG equilibrium approximates the $N$-player Nash equilibrium with $O(1/\sqrt{N})$ error
- Price impact in the MFG framework is endogenous, arising from the equilibrium strategies of all participants
- Extensions include heterogeneous agents, major-minor models, and limit order book dynamics

---

## Further Reading

- Lasry, J.M. & Lions, P.L. (2007), "Mean Field Games," *Japanese Journal of Mathematics*, 2, 229--260
- Huang, M., Malhame, R. & Caines, P. (2006), "Large Population Stochastic Dynamic Games: Closed-Loop McKean-Vlasov Systems and the Nash Certainty Equivalence Principle," *Communications in Information and Systems*, 6(3), 221--252
- Cardaliaguet, P. & Lehalle, C.A. (2018), "Mean Field Game of Controls and an Application to Trade Crowding," *Mathematics and Financial Economics*, 12(3), 335--363
- Carmona, R. & Delarue, F. (2018), *Probabilistic Theory of Mean Field Games with Applications*, Volumes I--II, Springer
- Almgren, R. & Chriss, N. (2001), "Optimal Execution of Portfolio Transactions," *Journal of Risk*, 3(2), 5--39
- Lacker, D. (2015), "Mean Field Games via Controlled McKean-Vlasov Dynamics," *SIAM Journal on Control and Optimization*, 55(3), 1403--1422
- Casgrain, P. & Jaimungal, S. (2020), "Mean-Field Games with Differing Beliefs for Algorithmic Trading," *Mathematical Finance*, 30(3), 995--1034
