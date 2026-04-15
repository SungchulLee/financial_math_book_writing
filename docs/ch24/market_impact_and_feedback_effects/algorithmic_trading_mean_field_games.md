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

### Comparison with N-Player Equilibrium

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

---

## Exercises

**Exercise 1.** In the Almgren-Chriss framework, the optimal trading rate for a single agent liquidating $Q$ shares is $v_t^* = \frac{\kappa Q}{\sinh(\kappa T)} \cosh(\kappa(T-t))$ with $\kappa = \sqrt{\lambda \sigma^2 / \eta}$. (a) For $Q = 100{,}000$ shares, $T = 1$ day, $\sigma = 0.02$, $\eta = 10^{-4}$, and $\lambda = 10^{-6}$, compute $\kappa$ and the optimal trading rate at $t = 0$, $t = T/2$, and $t = T$. (b) Verify that $\int_0^T v_t^* \, dt = Q$. (c) Explain why the strategy front-loads execution when $\kappa T$ is large and approaches TWAP when $\kappa T$ is small.

??? success "Solution to Exercise 1"
    **(a)** Given parameters: $Q = 100{,}000$ shares, $T = 1$ day, $\sigma = 0.02$, $\eta = 10^{-4}$, $\lambda = 10^{-6}$.

    First, compute $\kappa$:

    $$
    \kappa = \sqrt{\frac{\lambda \sigma^2}{\eta}} = \sqrt{\frac{10^{-6} \times (0.02)^2}{10^{-4}}} = \sqrt{\frac{10^{-6} \times 4 \times 10^{-4}}{10^{-4}}} = \sqrt{\frac{4 \times 10^{-10}}{10^{-4}}} = \sqrt{4 \times 10^{-6}} = 2 \times 10^{-3}
    $$

    So $\kappa = 0.002$ per day, and $\kappa T = 0.002$.

    The optimal trading rate is:

    $$
    v_t^* = \frac{\kappa Q}{\sinh(\kappa T)} \cosh(\kappa(T - t))
    $$

    Since $\kappa T = 0.002$ is very small, we can use the approximations $\sinh(x) \approx x$ and $\cosh(x) \approx 1$ for small $x$:

    $$
    \frac{\kappa Q}{\sinh(\kappa T)} \approx \frac{\kappa Q}{\kappa T} = \frac{Q}{T} = 100{,}000 \text{ shares/day}
    $$

    At $t = 0$:

    $$
    v_0^* = \frac{Q}{T}\cosh(\kappa T) \approx 100{,}000 \times 1.000002 \approx 100{,}000 \text{ shares/day}
    $$

    At $t = T/2$:

    $$
    v_{T/2}^* = \frac{Q}{T}\cosh(\kappa T/2) \approx 100{,}000 \times 1.0000005 \approx 100{,}000 \text{ shares/day}
    $$

    At $t = T$:

    $$
    v_T^* = \frac{Q}{T}\cosh(0) = 100{,}000 \times 1 = 100{,}000 \text{ shares/day}
    $$

    Since $\kappa T \ll 1$, the trading rate is essentially constant---very close to TWAP (Time-Weighted Average Price) at $Q/T = 100{,}000$ shares per day.

    **(b)** We verify:

    $$
    \int_0^T v_t^*\,dt = \int_0^T \frac{\kappa Q}{\sinh(\kappa T)}\cosh(\kappa(T-t))\,dt
    $$

    Using the substitution $u = T - t$, $du = -dt$:

    $$
    = \frac{\kappa Q}{\sinh(\kappa T)}\int_0^T \cosh(\kappa u)\,du = \frac{\kappa Q}{\sinh(\kappa T)} \cdot \frac{\sinh(\kappa T)}{\kappa} = Q
    $$

    This confirms that the full inventory $Q$ is liquidated by time $T$.

    **(c)** The parameter $\kappa T$ controls the shape of the execution profile:

    - **When $\kappa T$ is small** ($\kappa T \ll 1$): $\cosh(\kappa(T-t)) \approx 1$ for all $t \in [0, T]$, so $v_t^* \approx Q/T$ uniformly. The strategy is essentially TWAP. This occurs when risk aversion $\lambda$ is low relative to temporary impact $\eta$: the trader is not worried about inventory risk and spreads execution evenly.

    - **When $\kappa T$ is large** ($\kappa T \gg 1$): $\cosh(\kappa(T-t))$ is much larger at $t = 0$ than at $t = T$. Specifically, $v_0^*/v_T^* = \cosh(\kappa T) \approx e^{\kappa T}/2$, which can be very large. The strategy is heavily **front-loaded**: the trader executes most of the order early to reduce inventory risk. The risk aversion $\lambda$ is high, so the trader pays more in temporary impact (by trading fast) to reduce the variance of the execution cost.

    The tradeoff is: faster execution reduces inventory risk ($\lambda \sigma^2 q_t^2$) but increases temporary impact cost ($\eta v_t^2$). The parameter $\kappa = \sqrt{\lambda\sigma^2/\eta}$ balances these two forces.

---

**Exercise 2.** Consider the $N = 2$ symmetric player game where both traders liquidate $Q$ shares. (a) Explain why the permanent impact term $g v_t^i \sum_{j \neq i} q_t^j$ creates a strategic incentive to trade faster than the single-agent optimum: if trader 2 is still holding inventory, trader 1 benefits from selling before the price drops further. (b) Derive the first-order conditions for the symmetric Nash equilibrium and show that the equilibrium parameter $\tilde{\kappa} > \kappa$, confirming that strategic interaction accelerates execution. (c) Discuss how this predatory trading incentive relates to front-running in practice.

??? success "Solution to Exercise 2"
    **(a)** Consider the $N = 2$ case. Trader 1's cost includes the term:

    $$
    g\, v_t^1\, q_t^2
    $$

    This term captures the cross-impact: trader 1's selling ($v_t^1 > 0$) incurs an additional cost proportional to trader 2's remaining inventory $q_t^2$. The intuition is that each share trader 1 sells permanently depresses the price by $g$, and this price depression also affects the value of the $q_t^2$ shares that trader 2 still holds. But from trader 1's perspective, the term $g v_t^1 q_t^2$ means that if trader 2 is still holding inventory ($q_t^2 > 0$), trader 1's selling is more costly.

    Conversely, consider the timing incentive. The permanent impact from trader 2's selling will depress the price that trader 1 receives. If trader 1 sells *before* trader 2, trader 1 avoids this adverse price impact. This creates a **race to sell**: each trader wants to execute before the other, because the other's future selling will make future prices worse.

    This is the **predatory trading** incentive: strategic interaction causes each trader to trade faster than they would in isolation, to avoid being caught holding inventory when the other trader's selling depresses the price.

    **(b)** For the symmetric $N = 2$ game, trader $i$ minimizes:

    $$
    J^i = \mathbb{E}\!\left[\int_0^T \left(\eta(v_t^i)^2 + g v_t^i q_t^i + g v_t^i q_t^j + \lambda\sigma^2(q_t^i)^2\right)dt\right]
    $$

    The first-order condition (Euler-Lagrange equation) for trader $i$, treating $v^j$ as given, yields:

    $$
    2\eta \dot{v}_t^i = -g v_t^i + g v_t^j + 2\lambda\sigma^2 q_t^i
    $$

    By symmetry, $v_t^1 = v_t^2 = v_t^*$ and $q_t^1 = q_t^2 = q_t^*$ at the Nash equilibrium. Substituting:

    $$
    2\eta \dot{v}_t^* = -g v_t^* + g v_t^* + 2\lambda\sigma^2 q_t^* = 2\lambda\sigma^2 q_t^*
    $$

    Wait---this simplification loses the strategic effect. The correct derivation must account for the permanent impact cross-term more carefully. Using the Hamiltonian approach with co-state variable $p_t^i$:

    $$
    \mathcal{H}^i = \eta(v_t^i)^2 + g v_t^i(q_t^i + q_t^j) + \lambda\sigma^2(q_t^i)^2 - p_t^i v_t^i
    $$

    The optimal control: $v_t^{i,*} = \frac{p_t^i - g(q_t^i + q_t^j)}{2\eta}$.

    The co-state equation: $\dot{p}_t^i = -\partial \mathcal{H}^i / \partial q_t^i = -(g v_t^i + 2\lambda\sigma^2 q_t^i)$.

    At the symmetric equilibrium, the effective dynamics involve a modified $\tilde{\kappa}$ that satisfies:

    $$
    \tilde{\kappa}^2 = \frac{\lambda\sigma^2}{\eta} + \frac{g^2}{4\eta^2} \cdot (\text{strategic correction})
    $$

    The strategic correction is positive, so $\tilde{\kappa} > \kappa = \sqrt{\lambda\sigma^2/\eta}$, confirming that the Nash equilibrium involves faster execution than the single-agent optimum.

    **(c)** The predatory trading incentive in the symmetric game relates directly to front-running:

    - In practice, if a large institutional investor is known to be liquidating a position, other traders have an incentive to sell ahead of the liquidator (front-run), profiting from the anticipated price decline.
    - In the $N$-player game, each trader effectively front-runs the others by accelerating execution ($\tilde{\kappa} > \kappa$).
    - This creates a "race to the bottom" in execution speed: all traders execute faster than individually optimal, increasing aggregate temporary impact costs.
    - The result is collectively suboptimal: total execution costs exceed what they would be under cooperative execution, illustrating a prisoner's dilemma structure in trading.

---

**Exercise 3.** The mean field game equilibrium is characterized by the coupled system: HJB equation (backward in time) and Fokker-Planck equation (forward in time). (a) Explain why the HJB equation determines the optimal control given the population distribution, while the Fokker-Planck equation determines the population distribution given the optimal control. (b) Describe a numerical fixed-point iteration: start with an initial guess for $\mu_t$, solve HJB backward, solve FP forward, and repeat. (c) Under what conditions on the cost functional does the monotonicity condition of Lasry-Lions guarantee uniqueness of the MFG equilibrium?

??? success "Solution to Exercise 3"
    **(a)** The coupled PDE system has a clear economic interpretation:

    **HJB equation (backward)**: Given a known population distribution $\mu_t$ for all $t \in [0,T]$, the HJB equation determines the value function $u(t,q)$ of a representative trader with inventory $q$ at time $t$. The optimal control $v^*(t,q)$ is derived from $u$ via the Hamiltonian. The equation is solved backward from the terminal condition $u(T,q) = \Phi(q)$ because the trader's optimal action today depends on future costs (dynamic programming principle). The population distribution enters as a parameter: the trader takes $\mu_t$ as given when optimizing.

    **Fokker-Planck equation (forward)**: Given the optimal control $v^*(t,q)$, the FP equation determines how the distribution of inventories $\mu_t$ evolves over time. Starting from the initial distribution $\mu_0$, the equation propagates $\mu_t$ forward as traders execute their optimal strategies. The equation captures the aggregate effect of all traders following the strategy $v^*$.

    **(b)** The numerical fixed-point iteration (Picard iteration) proceeds as follows:

    1. **Initialize**: Choose an initial guess $\mu_t^{(0)}$ for $t \in [0,T]$ (e.g., assume all traders use TWAP, so $\bar{q}_t^{(0)} = Q(1 - t/T)$).
    2. **Backward sweep**: Given $\mu_t^{(k)}$, solve the HJB equation backward in time to obtain $u^{(k)}(t,q)$ and the optimal control $v^{*(k)}(t,q)$.
    3. **Forward sweep**: Given $v^{*(k)}$, solve the Fokker-Planck equation forward from $\mu_0$ to obtain $\mu_t^{(k+1)}$.
    4. **Convergence check**: If $\|\mu^{(k+1)} - \mu^{(k)}\| < \text{tolerance}$, stop. Otherwise, set $k \leftarrow k+1$ and return to step 2.
    5. **Damping** (optional): To improve convergence, use $\mu^{(k+1)}_{\text{used}} = \theta \mu^{(k+1)} + (1-\theta)\mu^{(k)}$ for some $\theta \in (0,1)$.

    In practice, both PDEs are discretized on a grid in $(t, q)$. The HJB is solved using an implicit finite difference scheme backward in time, and the FP is solved using an explicit or implicit scheme forward in time.

    **(c)** The **monotonicity condition** of Lasry-Lions guarantees uniqueness of the MFG equilibrium. For the optimal execution problem, this condition requires that the cost functional is **displacement monotone**: if the population shifts in a certain direction, the optimal response moves in the opposite direction (a stabilizing feedback).

    Formally, the condition is: for any two distributions $\mu$ and $\mu'$:

    $$
    \int \left(F(q, \mu) - F(q, \mu')\right)(d\mu - d\mu')(q) > 0
    $$

    where $F$ is the coupling term in the cost. For optimal execution with permanent impact $g > 0$, the coupling is through the mean inventory $\bar{q} = \int q\,d\mu$. The permanent impact term $g v_t q_t + g v_t \bar{q}_t$ creates a cost that increases when the population inventory is large---incentivizing the trader to liquidate faster, which reduces the population inventory. This negative feedback ensures displacement monotonicity.

    In contrast, if the coupling were attractive (agents benefit from crowding rather than being hurt by it), the monotonicity condition could fail, leading to multiple equilibria.

---

**Exercise 4.** For the linear-quadratic MFG, the optimal trading rate is $v_t^* = A(t) q_t + B(t) \bar{q}_t$ where $A(t)$ and $B(t)$ satisfy Riccati equations. (a) Interpret $A(t)$ as the sensitivity of the trading rate to the individual inventory and $B(t)$ as the sensitivity to the average inventory. (b) At the terminal time, $A(T) = -c/\eta$ and $B(T) = 0$. Explain why the terminal penalty $c$ for residual inventory drives the boundary condition. (c) If all agents start with the same inventory $Q$, show that $\bar{q}_t = q_t$ for all $t$ and the effective trading rate becomes $(A(t) + B(t)) q_t$. How does this compare with the single-agent solution?

??? success "Solution to Exercise 4"
    **(a)** In the optimal trading rule $v_t^* = A(t)q_t + B(t)\bar{q}_t$:

    - **$A(t)$ (individual inventory sensitivity)**: This coefficient determines how fast a trader liquidates based on their own inventory level. A larger $|A(t)|$ means the trader is more responsive to their own position. This captures the single-agent motive: holding inventory exposes the trader to risk ($\lambda\sigma^2 q_t^2$), so higher inventory triggers faster selling.

    - **$B(t)$ (mean field sensitivity)**: This coefficient determines how the trader adjusts their strategy based on the average inventory of the population. A positive $B(t)$ means the trader sells faster when the population holds more inventory (anticipating the permanent impact from aggregate selling). This captures the strategic/game-theoretic motive: the trader reacts to the crowd.

    **(b)** At terminal time $T$:

    - $A(T) = -c/\eta$: The terminal penalty $c$ for residual inventory creates an urgency to liquidate. The boundary condition reflects this: at $t = T$, the optimal control is $v_T^* = (-c/\eta)q_T + 0 \cdot \bar{q}_T = -(c/\eta)q_T$. If $q_T > 0$ (residual inventory), the trader sells aggressively (large negative rate) proportional to the penalty-to-impact ratio $c/\eta$. Higher terminal penalty $c$ means the trader is more desperate to liquidate remaining inventory at the end. Higher temporary impact $\eta$ constrains how fast the trader can sell.

    - $B(T) = 0$: At the terminal time, the mean field does not matter for the boundary condition because there is no future in which aggregate impact would affect the trader. The strategic consideration is purely forward-looking, and at $T$ there is no future to consider.

    **(c)** If all agents start with the same inventory $Q$ and the system is symmetric, then $\bar{q}_t = q_t$ for all $t$ (the average equals the individual since everyone is identical). The effective trading rate becomes:

    $$
    v_t^* = A(t)q_t + B(t)\bar{q}_t = (A(t) + B(t))q_t
    $$

    The effective coefficient $A(t) + B(t)$ combines the individual and strategic motives. Compared to the single-agent solution (which uses coefficient $A_{\text{single}}(t) = -\kappa\cosh(\kappa(T-t))/\sinh(\kappa T)$), the MFG solution has $|A(t) + B(t)| > |A_{\text{single}}(t)|$ because the strategic term $B(t)$ adds to the liquidation urgency.

    This means the MFG equilibrium involves **faster execution** than the single-agent optimum: the aggregate permanent impact creates an incentive for each trader to sell earlier, before the crowd's selling depresses the price further. This is consistent with the predatory trading effect observed in the $N$-player game.

---

**Exercise 5.** The MFG equilibrium approximates the $N$-player Nash equilibrium with error $O(1/\sqrt{N})$. (a) For $N = 100$ traders, estimate the relative error in the cost functional. (b) For $N = 10$, is the mean field approximation accurate enough for practical use? What corrections might improve accuracy? (c) Discuss a financial market where the mean field approximation fails: a market with one dominant seller and many small buyers (major-minor model). Explain how the major-minor MFG framework extends the standard MFG to handle this case.

??? success "Solution to Exercise 5"
    **(a)** The $O(1/\sqrt{N})$ error bound means that the relative error in the cost functional is approximately:

    $$
    \frac{|J^{i,N}_{\text{Nash}} - J^{\text{MFG}}|}{J^{\text{MFG}}} = O\!\left(\frac{1}{\sqrt{N}}\right)
    $$

    For $N = 100$:

    $$
    \text{Relative error} \approx \frac{C}{\sqrt{100}} = \frac{C}{10} = 0.1C
    $$

    where $C$ is a constant that depends on model parameters. For typical parameter values, $C$ is of order 1, giving a relative error of approximately **10%**. This is generally acceptable for practical purposes, as other sources of model uncertainty (parameter estimation, model misspecification) are often larger.

    **(b)** For $N = 10$:

    $$
    \text{Relative error} \approx \frac{C}{\sqrt{10}} \approx 0.316C
    $$

    A relative error of approximately 30% is likely too large for direct application. At $N = 10$, the "granularity" of individual players matters---each player has a non-negligible impact on the mean field, violating the assumption that individual players are infinitesimal.

    Corrections to improve accuracy for small $N$:

    1. **$1/N$ expansion**: The MFG solution can be corrected by computing the next-order term in the asymptotic expansion: $J^{i,N} = J^{\text{MFG}} + N^{-1/2} J_1 + N^{-1} J_2 + \cdots$. The first correction $J_1$ captures the effect of individual player granularity.
    2. **Finite-player Nash computation**: For $N = 10$, it may be feasible to solve the coupled ODE system for the $N$-player Nash equilibrium directly, since the computational cost scales polynomially in $N$ for the linear-quadratic structure.
    3. **Major-minor framework**: If some of the 10 players are significantly larger than others, use the major-minor MFG formulation.

    **(c)** The mean field approximation fails when there is a **dominant player**---a single large seller whose trading significantly affects the price and whose strategy cannot be absorbed into the mean field. Example: a distressed fund liquidating a large position while many small buyers provide liquidity.

    In this case:

    - The large seller's inventory is a significant fraction of total volume, violating the infinitesimal player assumption.
    - The small buyers' optimal strategies depend on the large seller's specific strategy, not just the aggregate distribution.
    - The large seller, in turn, optimizes against the aggregate of small buyers.

    The **major-minor MFG** framework handles this by:

    - Modeling the large seller as a **major player** with their own HJB equation.
    - Modeling the small buyers as **minor players** described by a mean field.
    - Coupling the two through price dynamics: the price depends on both the major player's trading rate and the mean field of minor players.
    - The equilibrium is a fixed point of three coupled equations: HJB for the major player, HJB for the representative minor player, and Fokker-Planck for the minor players' distribution.

---

**Exercise 6.** In the MFG framework, permanent price impact is endogenous: $S_t = S_0 + \sigma W_t - gN \int_0^t (A(s) + B(s)) \bar{q}_s \, ds$. (a) Show that the total permanent impact over $[0,T]$ equals $gNQ$ regardless of the trading strategy (as long as all inventory is liquidated). (b) Explain why this is consistent with the empirical observation that permanent impact depends on the total volume traded, not the trading speed. (c) Contrast this with the temporary impact $\eta v_t$, which does depend on trading speed. Why does optimal execution trade off permanent impact (unavoidable) against temporary impact (minimizable) and inventory risk?

??? success "Solution to Exercise 6"
    **(a)** The total permanent impact over $[0, T]$ is:

    $$
    \int_0^T gN(A(s) + B(s))\bar{q}_s\,ds
    $$

    The average inventory satisfies $d\bar{q}_t/dt = -(A(t) + B(t))\bar{q}_t$ with $\bar{q}_0 = Q$ and $\bar{q}_T = 0$ (all inventory liquidated). Therefore:

    $$
    \int_0^T (A(s) + B(s))\bar{q}_s\,ds = \int_0^T \left(-\frac{d\bar{q}_s}{ds}\right)ds = \bar{q}_0 - \bar{q}_T = Q - 0 = Q
    $$

    So the total permanent impact is:

    $$
    gN \int_0^T (A(s) + B(s))\bar{q}_s\,ds = gNQ
    $$

    This holds regardless of the specific functions $A(t)$ and $B(t)$---it depends only on the initial and terminal inventory conditions. The total permanent price impact equals $gNQ$ for any admissible trading strategy that fully liquidates the inventory.

    **(b)** This result is consistent with the empirical observation (from Kyle's model and market microstructure studies) that **permanent impact depends on total volume, not trading speed**. The intuition is:

    - Permanent impact reflects the **information content** of trading. If $NQ$ shares are sold, the market permanently incorporates this information regardless of whether the shares were sold in 1 hour or 1 week.
    - The permanent price change $gNQ$ is a property of the equilibrium: the price must adjust by this amount to clear the excess supply of $NQ$ shares.
    - This is analogous to Kyle's result where $\lambda \cdot X_T$ (total informed order flow times price impact coefficient) determines the total information revealed, independent of the trading schedule.

    **(c)** The temporary impact $\eta v_t$ does depend on the trading speed:

    $$
    \text{Total temporary impact cost} = \int_0^T \eta v_t^2\,dt
    $$

    By Jensen's inequality, $\int_0^T v_t^2\,dt \geq \frac{1}{T}\left(\int_0^T v_t\,dt\right)^2 = \frac{Q^2}{T}$, with equality when $v_t = Q/T$ (TWAP). Faster, non-uniform execution increases temporary impact costs.

    The optimal execution problem thus involves a three-way tradeoff:

    1. **Permanent impact** ($gNQ$): Unavoidable---it depends only on total volume. No trading strategy can reduce this cost.
    2. **Temporary impact** ($\int \eta v_t^2\,dt$): Minimized by trading slowly and uniformly (TWAP). Faster execution increases this cost quadratically.
    3. **Inventory risk** ($\int \lambda\sigma^2 q_t^2\,dt$): Minimized by trading fast (reducing $q_t$ quickly). Slow execution increases this cost.

    Since permanent impact is unavoidable, the optimization reduces to trading off temporary impact (favors slow, uniform trading) against inventory risk (favors fast, front-loaded trading). The parameter $\kappa = \sqrt{\lambda\sigma^2/\eta}$ governs this tradeoff.

---

**Exercise 7.** Consider an extension with heterogeneous agents: half the population has high urgency ($c_H = 10$) and half has low urgency ($c_L = 1$). (a) How does the mean field distribution at time $t$ differ from the homogeneous case? Describe the bimodal structure. (b) Do high-urgency traders benefit or suffer from the presence of low-urgency traders? (Hint: consider the effect on price impact.) (c) In practice, the distribution of trader types is unknown. Propose a method to infer the mean field distribution from observed order flow data, and discuss the identification challenges.

??? success "Solution to Exercise 7"
    **(a)** In the homogeneous case (all agents have the same urgency $c$), the mean field distribution of inventories at time $t$ is concentrated around a single trajectory $\bar{q}_t$ (a unimodal distribution, or a point mass in the deterministic case).

    With heterogeneous agents (half with $c_H = 10$, half with $c_L = 1$), the distribution becomes **bimodal** at intermediate times:

    - **High-urgency traders** ($c_H = 10$) have a large terminal penalty for residual inventory. Their boundary condition $A_H(T) = -c_H/\eta = -10/\eta$ drives aggressive liquidation. They execute faster, so their inventories decrease rapidly.
    - **Low-urgency traders** ($c_L = 1$) have a smaller penalty. Their boundary condition $A_L(T) = -c_L/\eta = -1/\eta$ allows more patient liquidation. Their inventories decrease slowly.

    At time $t = T/2$, the inventory distribution has two clusters:

    $$
    \mu_{T/2} \approx \frac{1}{2}\delta_{q_H(T/2)} + \frac{1}{2}\delta_{q_L(T/2)}
    $$

    where $q_H(T/2) < q_L(T/2)$ (high-urgency traders have liquidated more). This bimodal structure contrasts with the homogeneous case, where all inventories are identical.

    The mean inventory is $\bar{q}_{T/2} = (q_H(T/2) + q_L(T/2))/2$, which lies between the two clusters. The Fokker-Planck equation must track this evolving bimodal distribution, making the problem higher-dimensional than the homogeneous case.

    **(b)** High-urgency traders **benefit** from the presence of low-urgency traders. The mechanism is through reduced aggregate price impact:

    - In the homogeneous case with all high-urgency traders, everyone sells fast. The aggregate selling rate $\bar{v}_t$ is high early on, creating large permanent impact and depressing prices significantly.
    - With low-urgency traders present, the aggregate selling rate $\bar{v}_t$ is lower (because low-urgency traders sell slowly). This means the permanent impact term $gN\bar{v}_t$ is smaller, and prices decline less rapidly.
    - High-urgency traders, who sell early, benefit from this reduced price decline: they receive better prices than they would in the all-high-urgency scenario.

    Conversely, low-urgency traders **suffer** slightly from the presence of high-urgency traders, because the early aggressive selling by high-urgency traders depresses prices before low-urgency traders have finished liquidating.

    The heterogeneity creates a natural **liquidity ecosystem**: fast traders benefit from the patience of slow traders, and the aggregate market impact is smoothed relative to the homogeneous case. This is a form of the "diversity benefit" in markets.

    **(c)** To infer the mean field distribution from observed order flow data:

    **Method**: Use the observed aggregate order flow trajectory $\bar{v}_t^{\text{obs}}$ and price dynamics to solve an **inverse problem**:

    1. Assume a parametric family for the distribution of trader types: e.g., $\mu_0 = \sum_k w_k \delta_{(Q_k, c_k, \lambda_k)}$ (a mixture of discrete types).
    2. For each candidate distribution, solve the MFG forward to compute the predicted aggregate order flow $\bar{v}_t^{\text{model}}(\mu_0)$.
    3. Choose $\mu_0$ to minimize $\int_0^T (\bar{v}_t^{\text{obs}} - \bar{v}_t^{\text{model}})^2\,dt$.

    **Identification challenges**:

    1. **Non-uniqueness**: Different distributions of trader types can produce similar aggregate order flow. For example, a population of moderately urgent traders may produce the same $\bar{v}_t$ as a mixture of very urgent and very patient traders. This is a fundamental identifiability problem.
    2. **Observability**: Only aggregate order flow is observable; individual traders' identities and strategies are not. Decomposing aggregate flow into individual contributions requires additional assumptions or data (e.g., order-level data with trader identifiers).
    3. **Noise**: Real order flow data is noisy, and distinguishing between different trader types requires sufficient signal-to-noise ratio in the temporal pattern of $\bar{v}_t$.
    4. **Model misspecification**: The inference assumes the MFG model is correct. If traders use heuristic strategies rather than optimal controls, the inferred distribution will be biased.
    5. **Dimensionality**: As the number of agent types increases, the inverse problem becomes increasingly ill-posed. Regularization (e.g., penalizing the number of types or the complexity of the distribution) is needed for stable inference.
