# Connection to Stochastic Control


Reinforcement learning is closely related to **stochastic control**, a classical framework in mathematical finance and economics.

---

## Stochastic control formulation


Stochastic control problems involve:

- controlled stochastic dynamics,
- an objective functional,
- optimization over admissible controls.

The goal is to maximize expected utility or reward.

---

## Hamilton–Jacobi–Bellman equation


In continuous time, optimal control leads to the HJB equation:

$$
0 = \sup_u \left\{ \mathcal{L}^u V + r(x,u) \right\}
$$


where $\mathcal{L}^u$ is the controlled generator.

This is the continuous-time analogue of Bellman equations (Recall (see [§ Bellman equations](markov_decision_processes.md#bellman-equations))).

---

## RL as data-driven control


Reinforcement learning can be viewed as:

- approximating value functions,
- solving control problems without known dynamics,
- replacing model-based control with data-driven learning.

---

## Financial applications


Connections appear in:

- optimal trading and execution (Recall (see [§ RL for Optimal Execution](rl_for_optimal_execution.md))),
- portfolio optimization,
- market making and hedging (Recall (see [§ RL for Option Hedging](rl_for_option_hedging.md))).

RL generalizes stochastic control to unknown environments.

---

## Key takeaways


- RL and stochastic control share the Bellman principle.
- HJB equations connect continuous-time finance to RL.
- RL enables control without full model specification.

---

## Further reading


- Fleming & Soner, *Controlled Markov Processes*.
- Pham, continuous-time RL connections.

---

## Exercises

**Exercise 1.** Consider the Merton portfolio optimization problem: maximize $\mathbb{E}[\int_0^T e^{-\rho t} U(c_t) dt + e^{-\rho T} U(W_T)]$ where $W_t$ is wealth, $c_t$ is consumption, and $U(x) = x^{1-\gamma}/(1-\gamma)$ is CRRA utility. The wealth dynamics are $dW_t = W_t[(\mu - r)\pi_t + r] dt + W_t \pi_t \sigma dB_t - c_t dt$, where $\pi_t$ is the risky asset fraction. (a) Write the HJB equation $0 = \sup_{\pi, c}\{\partial_t V + \mathcal{L}^{\pi,c} V + e^{-\rho t} U(c)\}$. (b) Conjecture $V(t, W) = e^{-\rho t} f(t) W^{1-\gamma}/(1-\gamma)$ and derive the optimal controls $\pi^* = (\mu-r)/(\gamma \sigma^2)$ and $c^* = W / f(t)$. (c) Explain how an RL agent could learn these controls without knowing $\mu$ and $\sigma$.

??? success "Solution to Exercise 1"
    **(a) HJB equation for Merton's problem.**

    The value function $V(t, W)$ satisfies:

    $$
    0 = \sup_{\pi, c} \left\{\partial_t V + W[(\mu - r)\pi + r] \partial_W V - c \, \partial_W V + \frac{1}{2}W^2 \pi^2 \sigma^2 \partial_{WW} V + e^{-\rho t} U(c)\right\}
    $$

    The controlled generator $\mathcal{L}^{\pi,c}$ applied to $V$ gives the drift and diffusion terms from $dW_t = W_t[(\mu-r)\pi_t + r]dt + W_t \pi_t \sigma dB_t - c_t dt$:

    - Drift term: $\{W[(\mu - r)\pi + r] - c\} \partial_W V$
    - Diffusion term: $\frac{1}{2}W^2 \pi^2 \sigma^2 \partial_{WW} V$

    The terminal condition is $V(T, W) = e^{-\rho T} \frac{W^{1-\gamma}}{1-\gamma}$.

    **(b) Derivation of optimal controls.**

    Conjecture $V(t, W) = e^{-\rho t} f(t) \frac{W^{1-\gamma}}{1-\gamma}$ where $f(T) = 1$. Then:

    $$
    \partial_t V = e^{-\rho t}\!\left[f'(t) - \rho f(t)\right]\frac{W^{1-\gamma}}{1-\gamma}
    $$

    $$
    \partial_W V = e^{-\rho t} f(t) W^{-\gamma}, \quad \partial_{WW} V = -\gamma e^{-\rho t} f(t) W^{-\gamma - 1}
    $$

    **Optimal portfolio fraction $\pi^*$:** Maximizing over $\pi$, the first-order condition from the HJB is:

    $$
    (\mu - r) W \partial_W V + W^2 \pi \sigma^2 \partial_{WW} V = 0
    $$

    $$
    (\mu - r) e^{-\rho t} f(t) W^{-\gamma+1} - \gamma \pi \sigma^2 e^{-\rho t} f(t) W^{-\gamma+1} = 0
    $$

    $$
    \pi^* = \frac{\mu - r}{\gamma \sigma^2}
    $$

    This is the classical Merton fraction, independent of wealth and time.

    **Optimal consumption $c^*$:** The first-order condition over $c$ is:

    $$
    -\partial_W V + e^{-\rho t} U'(c) = 0 \implies -e^{-\rho t} f(t) W^{-\gamma} + e^{-\rho t} c^{-\gamma} = 0
    $$

    $$
    c^* = f(t)^{-1/\gamma} W
    $$

    The function $f(t)$ is determined by substituting back into the HJB and solving the resulting ODE with $f(T) = 1$. For the infinite-horizon case ($T \to \infty$), $f$ is a constant and $c^* = W/f$, giving a constant consumption-to-wealth ratio.

    **(c) RL approach without knowing $\mu$ and $\sigma$.**

    An RL agent can learn $\pi^*$ and $c^*$ without knowing the parameters:

    1. **State:** $s_t = (W_t, t)$ (or features such as recent returns for estimating $\mu, \sigma$).
    2. **Action:** $a_t = (\pi_t, c_t)$ (portfolio fraction and consumption rate).
    3. **Reward:** $r_t = e^{-\rho t} U(c_t) \Delta t$ (instantaneous utility).
    4. **Learning:** The agent simulates (or experiences live) wealth trajectories and uses policy gradient or actor-critic methods to maximize $\mathbb{E}[\sum_t r_t]$.

    The agent implicitly estimates $\mu$ and $\sigma$ through its experience: trajectories with high returns lead to gradient updates that increase the portfolio fraction, while high-volatility episodes lead to updates that reduce it. After sufficient training, the learned policy converges to $\pi \approx (\mu-r)/(\gamma\sigma^2)$. The key advantage is that the agent adapts if $\mu$ or $\sigma$ change over time, without requiring re-estimation and re-solving the HJB.

---

**Exercise 2.** The Bellman equation in discrete time is $V^*(s) = \max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')\}$. The HJB equation in continuous time is $0 = \sup_u \{\mathcal{L}^u V + r(x,u)\}$ where $\mathcal{L}^u V = \partial_t V + b(x,u) \partial_x V + \frac{1}{2}\sigma^2(x,u) \partial_{xx} V$. (a) Show that the discrete-time Bellman equation converges to the continuous-time HJB as the time step $\Delta t \to 0$. (Hint: expand $V(t + \Delta t, x')$ in a Taylor series.) (b) Identify the discount factor $\gamma$ with $e^{-\rho \Delta t}$. (c) Explain why the HJB is a PDE while the Bellman equation is a functional equation, and why numerical methods differ.

??? success "Solution to Exercise 2"
    **(a) Discrete Bellman converges to HJB.**

    The discrete-time Bellman equation at state $(t, x)$ with time step $\Delta t$ is:

    $$
    V(t, x) = \max_u \left\{r(x, u) \Delta t + e^{-\rho \Delta t} \mathbb{E}[V(t + \Delta t, x + \Delta x)]\right\}
    $$

    where $\Delta x = b(x, u)\Delta t + \sigma(x, u)\sqrt{\Delta t} \, Z$, $Z \sim \mathcal{N}(0,1)$.

    Taylor-expand $V(t + \Delta t, x + \Delta x)$ around $(t, x)$:

    $$
    V(t+\Delta t, x+\Delta x) \approx V + \partial_t V \Delta t + \partial_x V \Delta x + \frac{1}{2}\partial_{xx} V (\Delta x)^2
    $$

    Taking the expectation (noting $\mathbb{E}[\Delta x] = b \Delta t$, $\mathbb{E}[(\Delta x)^2] = \sigma^2 \Delta t + O(\Delta t^2)$):

    $$
    \mathbb{E}[V(t+\Delta t, x+\Delta x)] \approx V + \partial_t V \Delta t + b \partial_x V \Delta t + \frac{1}{2}\sigma^2 \partial_{xx} V \Delta t
    $$

    Also $e^{-\rho \Delta t} \approx 1 - \rho \Delta t$. Substituting into the Bellman equation:

    $$
    V = \max_u \left\{r \Delta t + (1 - \rho \Delta t)\left[V + \partial_t V \Delta t + b \partial_x V \Delta t + \frac{1}{2}\sigma^2 \partial_{xx} V \Delta t\right]\right\}
    $$

    Expanding and canceling $V$ from both sides, then dividing by $\Delta t$ and taking $\Delta t \to 0$:

    $$
    0 = \max_u \left\{r(x,u) - \rho V + \partial_t V + b(x,u)\partial_x V + \frac{1}{2}\sigma^2(x,u)\partial_{xx} V\right\}
    $$

    This is exactly the HJB equation: $0 = \sup_u \{\mathcal{L}^u V + r - \rho V\}$ where $\mathcal{L}^u V = \partial_t V + b \partial_x V + \frac{1}{2}\sigma^2 \partial_{xx} V$. $\square$

    **(b) Discount factor identification.**

    In the discrete-time Bellman equation, the discount factor between steps is $\gamma = e^{-\rho \Delta t}$. As $\Delta t \to 0$:

    $$
    \gamma = e^{-\rho \Delta t} \approx 1 - \rho \Delta t
    $$

    The continuous-time discount rate $\rho$ and the discrete discount factor are related by $\rho = -\ln \gamma / \Delta t$. For $\gamma = 0.99$ and $\Delta t = 1/252$ (daily): $\rho = -\ln(0.99) \times 252 \approx 0.01005 \times 252 \approx 2.53$ (253% annual), which shows that $\gamma = 0.99$ per day corresponds to very aggressive discounting in continuous time.

    **(c) PDE vs. functional equation.**

    The HJB equation is a **partial differential equation** (PDE) in $(t, x)$: it involves derivatives $\partial_t V$, $\partial_x V$, $\partial_{xx} V$ and is solved over a continuous domain. Numerical methods include finite difference schemes (explicit, implicit, Crank-Nicolson), finite element methods, and spectral methods, all operating on a grid in $(t, x)$ space.

    The discrete-time Bellman equation is a **functional equation** on a (possibly finite) set of states. It does not involve derivatives. Numerical methods include value iteration, policy iteration, and Q-learning, which operate on a state-action table or use function approximation.

    The key numerical difference is that the HJB requires discretizing continuous space into a grid and approximating derivatives, while the Bellman equation operates directly on discrete states. For low-dimensional problems (1--3 state variables), PDE methods can be very efficient. For high-dimensional problems, RL methods that solve the Bellman equation with function approximation scale better.

---

**Exercise 3.** In model-based stochastic control, the dynamics $dx_t = b(x_t, u_t)dt + \sigma(x_t, u_t)dW_t$ are known. In RL, they are unknown. (a) List the advantages of model-based control: exact solutions for LQ problems, convergence guarantees, interpretability. (b) List the advantages of RL: no model needed, handles nonlinear dynamics, adapts to real data. (c) For optimal execution with linear impact (Almgren-Chriss), the model-based solution is a known closed-form. Why might an RL agent still be preferable in practice? (Hint: consider nonlinear impact, stochastic liquidity, and intraday patterns.)

??? success "Solution to Exercise 3"
    **(a) Advantages of model-based control.**

    - **Exact solutions for LQ problems:** Linear-quadratic (LQ) control problems (linear dynamics, quadratic costs) have closed-form solutions via the Riccati equation. No training or sampling is needed.
    - **Convergence guarantees:** The HJB equation has a unique viscosity solution under standard conditions; verification theorems certify optimality. Sample complexity is zero---the solution is computed analytically or numerically.
    - **Interpretability:** The optimal policy is expressed in terms of model parameters (e.g., $\pi^* = (\mu-r)/(\gamma\sigma^2)$), making it easy to understand, audit, and explain to stakeholders.
    - **Computational efficiency:** Solving a PDE or Riccati equation once is far faster than training an RL agent for millions of episodes.

    **(b) Advantages of RL.**

    - **No model needed:** RL learns from data (simulated or real) without specifying the dynamics $b(x,u)$ or $\sigma(x,u)$. If the model is unknown or misspecified, RL can still learn a good policy.
    - **Handles nonlinear dynamics:** RL with neural network function approximation can handle arbitrary nonlinear dynamics and cost functions, whereas analytical solutions exist only for special cases (LQ, certain affine models).
    - **Adapts to real data:** RL can be trained on historical data or live market data, capturing features (regime changes, volatility clustering, microstructure effects) that parametric models may miss.
    - **Scalability to high dimensions:** RL with function approximation scales to high-dimensional problems (many assets, many state variables) where PDE methods suffer from the curse of dimensionality.

    **(c) RL for optimal execution beyond Almgren-Chriss.**

    The Almgren-Chriss solution assumes linear, time-invariant impact and arithmetic Brownian motion. In practice:

    - **Nonlinear impact:** Real market impact is concave (square-root law: $\text{impact} \propto \sqrt{n}$), not linear. The LQ framework breaks down.
    - **Stochastic liquidity:** Bid-ask spreads, depth, and volume vary throughout the day and across days. A static strategy cannot adapt.
    - **Intraday patterns:** Volume and volatility have strong intraday patterns (U-shaped volume, opening/closing effects) that a model-free RL agent can exploit.
    - **Information arrival:** News events, earnings announcements, and order-flow signals create opportunities for adaptive execution that a static schedule misses.

    An RL agent trained on realistic market simulations or historical data can learn to exploit all these features, producing execution strategies that outperform Almgren-Chriss in practice.

---

**Exercise 4.** Consider a simple stochastic control problem: $dx_t = u_t dt + \sigma dW_t$ with cost $J = \mathbb{E}[\int_0^T (x_t^2 + u_t^2)dt + x_T^2]$. (a) Write the HJB equation and conjecture $V(t,x) = a(t)x^2 + b(t)$. Derive the Riccati equation for $a(t)$. (b) The optimal control is $u^* = -a(t)x$. A Q-learning agent learns the Q-function $Q(x, u) \approx x^2 + u^2 + \gamma V(x')$ from sampled transitions. Compare the sample efficiency of Q-learning with the analytical Riccati solution. (c) For this LQ problem, how many training episodes would Q-learning need to achieve 1% error in the optimal policy?

??? success "Solution to Exercise 4"
    **(a) HJB equation and Riccati conjecture.**

    The dynamics are $dx_t = u_t dt + \sigma dW_t$ with cost $J = \mathbb{E}[\int_0^T (x_t^2 + u_t^2)dt + x_T^2]$. The HJB equation is:

    $$
    0 = \min_u \left\{\partial_t V + u \, \partial_x V + \frac{1}{2}\sigma^2 \partial_{xx} V + x^2 + u^2\right\}
    $$

    with terminal condition $V(T, x) = x^2$.

    Conjecture $V(t, x) = a(t)x^2 + b(t)$. Then $\partial_t V = a'(t)x^2 + b'(t)$, $\partial_x V = 2a(t)x$, $\partial_{xx} V = 2a(t)$.

    First-order condition for $u$: $\partial_x V + 2u = 0 \implies u^* = -a(t)x$.

    Substituting $u^* = -a(t)x$ into the HJB:

    $$
    0 = a'x^2 + b' + (-ax)(2ax) + \frac{1}{2}\sigma^2 (2a) + x^2 + a^2 x^2
    $$

    $$
    0 = (a' - 2a^2 + 1 + a^2)x^2 + (b' + \sigma^2 a)
    $$

    $$
    0 = (a' - a^2 + 1)x^2 + (b' + \sigma^2 a)
    $$

    Since this must hold for all $x$, both coefficients must be zero:

    $$
    a'(t) = a(t)^2 - 1, \quad a(T) = 1 \quad \text{(Riccati equation)}
    $$

    $$
    b'(t) = -\sigma^2 a(t), \quad b(T) = 0
    $$

    The Riccati equation has the solution $a(t) = \frac{e^{2(T-t)} + 1}{e^{2(T-t)} - 1} = \coth(T - t)$ for $t < T$.

    **(b) Comparison of Q-learning and analytical solution.**

    The analytical solution requires:

    - Solving the Riccati ODE (a single 1D ODE, computed in milliseconds).
    - The optimal control is $u^*(t, x) = -\coth(T-t) \cdot x$, available in closed form.

    Q-learning requires:

    - Discretizing the state $(x, t)$ and action $u$ spaces.
    - Sampling transitions $(x, u, \text{cost}, x')$ by simulating the dynamics.
    - Updating Q-values iteratively until convergence.
    - Typical sample complexity: $O(|\mathcal{S}||\mathcal{A}|/\epsilon^2)$ transitions for $\epsilon$-optimal Q-values.

    For this LQ problem, Q-learning is vastly less sample-efficient than the analytical solution. The analytical approach exploits the known structure (linearity, quadratic cost) perfectly, while Q-learning must discover this structure from data. Q-learning's advantage is that it works even when the dynamics or cost are unknown or non-standard.

    **(c) Training episodes for 1% error.**

    For a simple LQ problem with one state variable discretized into $M = 100$ levels, one action variable discretized into $A = 50$ levels, and $N = 20$ time steps, the state-action space has $100 \times 20 \times 50 = 100{,}000$ entries. To estimate each Q-value to within 1% accuracy, each state-action pair needs to be visited $O(1/\epsilon^2) = O(10{,}000)$ times (for $\epsilon = 0.01$ relative error with order-1 noise). Total transitions needed: approximately $100{,}000 \times 10{,}000 = 10^9$.

    With $N = 20$ transitions per episode, this requires approximately $5 \times 10^7$ episodes. With function approximation (e.g., a neural network exploiting the quadratic structure), the sample requirement can be reduced significantly, but is still orders of magnitude more than the analytical solution.

---

**Exercise 5.** Risk-sensitive stochastic control minimizes $J_\lambda = -\frac{1}{\lambda} \ln \mathbb{E}[e^{-\lambda \sum_t r_t}]$ where $\lambda > 0$ controls risk aversion. (a) Show that as $\lambda \to 0$, $J_\lambda \to \mathbb{E}[\sum_t r_t]$ (risk-neutral). (b) Show that as $\lambda \to \infty$, $J_\lambda \to \min_\omega \sum_t r_t(\omega)$ (worst-case). (c) Write the risk-sensitive Bellman equation: $V(s) = \sup_a \{r(s,a) - \frac{1}{\lambda}\ln \mathbb{E}_s[e^{-\lambda V(s')}]\}$. (d) Explain why this formulation is natural for financial applications where tail risk matters.

??? success "Solution to Exercise 5"
    **(a) Risk-neutral limit ($\lambda \to 0$).**

    By Taylor expansion of the exponential:

    $$
    J_\lambda = -\frac{1}{\lambda}\ln \mathbb{E}\!\left[e^{-\lambda \sum_t r_t}\right]
    $$

    Let $R = \sum_t r_t$. For small $\lambda$:

    $$
    e^{-\lambda R} \approx 1 - \lambda R + \frac{\lambda^2 R^2}{2}
    $$

    $$
    \mathbb{E}[e^{-\lambda R}] \approx 1 - \lambda \mathbb{E}[R] + \frac{\lambda^2}{2}\mathbb{E}[R^2]
    $$

    $$
    \ln \mathbb{E}[e^{-\lambda R}] \approx -\lambda \mathbb{E}[R] + \frac{\lambda^2}{2}(\mathbb{E}[R^2] - \mathbb{E}[R]^2) = -\lambda \mathbb{E}[R] + \frac{\lambda^2}{2}\text{Var}[R]
    $$

    Therefore:

    $$
    J_\lambda \approx \mathbb{E}[R] - \frac{\lambda}{2}\text{Var}[R] \xrightarrow{\lambda \to 0} \mathbb{E}[R]
    $$

    In the limit, the agent maximizes expected total reward (risk-neutral). $\square$

    **(b) Worst-case limit ($\lambda \to \infty$).**

    For large $\lambda$, $e^{-\lambda R}$ is dominated by the scenario with the smallest $R$ (worst case):

    $$
    \mathbb{E}[e^{-\lambda R}] \approx e^{-\lambda \min_\omega R(\omega)} \cdot P(\text{worst case}) + \ldots
    $$

    More precisely, by Varadhan's lemma or the Laplace principle:

    $$
    -\frac{1}{\lambda}\ln \mathbb{E}[e^{-\lambda R}] \xrightarrow{\lambda \to \infty} \min_\omega R(\omega) = \text{ess inf } R
    $$

    The agent optimizes worst-case total reward. This is the most conservative (maximin) objective. $\square$

    **(c) Risk-sensitive Bellman equation.**

    The risk-sensitive objective satisfies the recursion:

    $$
    V(s) = \sup_a \left\{r(s,a) - \frac{1}{\lambda}\ln \mathbb{E}_{s'|s,a}\!\left[e^{-\lambda V(s')}\right]\right\}
    $$

    This replaces the standard expectation $\mathbb{E}[V(s')]$ with the **certainty equivalent** $-\frac{1}{\lambda}\ln \mathbb{E}[e^{-\lambda V(s')}]$, which penalizes variability in future values. When $V(s')$ is random:

    $$
    -\frac{1}{\lambda}\ln \mathbb{E}[e^{-\lambda V(s')}] \le \mathbb{E}[V(s')]
    $$

    by Jensen's inequality (since $x \mapsto e^{-\lambda x}$ is convex). The risk-sensitive operator discounts uncertain future values more than certain ones.

    **(d) Financial relevance.**

    This formulation is natural for finance because:

    - It connects to exponential utility: $U(x) = -e^{-\lambda x}$, the most common utility in risk management.
    - It penalizes tail risk: scenarios with very low $R$ contribute exponentially more to the objective as $\lambda$ increases.
    - It provides a single tuning parameter $\lambda$ that interpolates between risk-neutral ($\lambda \to 0$) and worst-case ($\lambda \to \infty$) objectives.
    - It is time-consistent (unlike mean-variance): the Bellman recursion holds exactly, ensuring that the optimal policy at time $t$ remains optimal at time $t+1$.

---

**Exercise 6.** A market maker must continuously quote bid and ask prices. This is a stochastic control problem where the state is $(q_t, S_t, t)$ (inventory, mid-price, time), the controls are the bid-ask spread $(d_a, d_b)$, and the objective trades off P&L against inventory risk. (a) Write the HJB equation for the Avellaneda-Stoikov market-making model. (b) The optimal spread is $d^* = \frac{1}{\gamma}\ln(1 + \gamma/\kappa) + \frac{\gamma}{2}\sigma^2(T-t)$ where $\gamma$ is risk aversion and $\kappa$ is order arrival intensity. Interpret each term. (c) An RL agent trained on historical LOB data learns a market-making policy. What advantages does it have over the Avellaneda-Stoikov solution?

??? success "Solution to Exercise 6"
    **(a) HJB for Avellaneda-Stoikov market making.**

    The state is $(q_t, S_t, t)$ where $q$ is inventory, $S$ is mid-price, and the market maker quotes bid/ask at $S - d_b$ and $S + d_a$. The value function $V(t, q, S)$ satisfies:

    $$
    0 = \partial_t V + \frac{1}{2}\sigma^2 \partial_{SS} V + \sup_{d_a, d_b} \left\{\Lambda_a(d_a)\left[V(t, q-1, S) - V(t, q, S) + d_a\right] + \Lambda_b(d_b)\left[V(t, q+1, S) - V(t, q, S) + d_b\right]\right\}
    $$

    where $\Lambda_a(d_a) = \kappa e^{-\kappa d_a}$ and $\Lambda_b(d_b) = \kappa e^{-\kappa d_b}$ are the order arrival intensities (higher spread $\to$ fewer fills). The terminal condition penalizes final inventory: $V(T, q, S) = q S - \gamma q^2$ (liquidate at mid-price with inventory penalty).

    **(b) Interpretation of optimal spread.**

    The optimal half-spread is:

    $$
    d^* = \underbrace{\frac{1}{\gamma}\ln\!\left(1 + \frac{\gamma}{\kappa}\right)}_{\text{profit margin}} + \underbrace{\frac{\gamma}{2}\sigma^2(T-t)}_{\text{inventory risk compensation}}
    $$

    - **First term** $\frac{1}{\gamma}\ln(1 + \gamma/\kappa)$: This is the base profit margin, independent of time. It balances the desire for profit (wide spread) against fill probability (narrow spread). When $\kappa$ is large (many orders), the market maker can afford tighter spreads. When $\gamma$ is large (high risk aversion), spreads widen.
    - **Second term** $\frac{\gamma}{2}\sigma^2(T-t)$: This compensates for inventory risk over the remaining time horizon. It increases with volatility $\sigma$ (more price risk), risk aversion $\gamma$, and time remaining $T-t$ (longer exposure). Near expiry ($T-t \to 0$), this term vanishes and the spread tightens.

    **(c) Advantages of RL for market making.**

    An RL agent trained on historical limit order book (LOB) data can learn to:

    - **Adapt to intraday patterns:** Market dynamics vary throughout the day (opening auction, lunch lull, closing rush). The RL agent can learn time-dependent strategies without an explicit model.
    - **Respond to order-book imbalance:** The Avellaneda-Stoikov model uses only mid-price and inventory; RL can incorporate queue position, order-book depth, and trade flow signals.
    - **Handle non-Poisson order arrival:** Real order arrivals are clustered and self-exciting (Hawkes process), not Poisson. RL adapts without needing to specify the arrival model.
    - **Manage multi-asset portfolios:** The analytical solution is for a single asset. RL scales to market making across correlated instruments, exploiting cross-asset hedging.
    - **Learn from adverse selection:** RL can detect and adapt to informed order flow (toxic flow), which is absent from the basic Avellaneda-Stoikov model.

---

**Exercise 7.** The verification theorem states that if a smooth function $V$ satisfies the HJB equation with appropriate boundary conditions, then $V$ is the optimal value function. (a) Explain why this is important: it confirms that a candidate solution is truly optimal. (b) When might the verification theorem fail? (Hint: viscosity solutions are needed when $V$ is not smooth.) (c) In RL, there is no verification theorem---the agent converges to a local optimum at best. Discuss the implications for deploying RL-based trading strategies: how do you validate that the learned policy is actually good? Propose validation methods (backtesting, comparison to known benchmarks, stress testing).

??? success "Solution to Exercise 7"
    **(a) Importance of the verification theorem.**

    The verification theorem provides a **sufficiency condition** for optimality. In stochastic control, we typically:

    1. Derive the HJB equation (necessary condition via dynamic programming principle).
    2. Conjecture a candidate solution $V$ (often by guessing the functional form).
    3. Verify that $V$ satisfies the HJB and the appropriate boundary/terminal conditions.
    4. Invoke the verification theorem to conclude that $V$ is the true optimal value function and the associated control is optimal.

    Without the verification theorem, solving the HJB only gives a candidate---it could be a saddle point, or the conjectured form might not be the true solution. The verification theorem provides mathematical certainty that the candidate is genuinely optimal.

    **(b) When the verification theorem fails.**

    The classical verification theorem requires $V \in C^{1,2}$ (once differentiable in $t$, twice in $x$). It fails when:

    - **Non-smooth value functions:** In problems with state constraints, free boundaries (e.g., American options, singular control), the value function has kinks or corners where $\partial_{xx} V$ does not exist.
    - **Degenerate diffusion:** When $\sigma(x, u) = 0$ for some $(x, u)$, the PDE is degenerate and classical solutions may not exist.
    - **Unbounded controls or state space:** The supremum in the HJB may not be attained, or $V$ may grow too fast for the It\^o formula to apply.

    In these cases, the theory of **viscosity solutions** provides the correct framework: the value function is characterized as the unique viscosity solution of the HJB, even when it is not classically differentiable. Verification-type results for viscosity solutions (comparison principles) replace the classical verification theorem.

    **(c) Validation without a verification theorem in RL.**

    RL provides no mathematical guarantee that the learned policy is optimal (or even close to optimal). Validation must rely on empirical methods:

    - **Backtesting:** Apply the learned policy to historical data not used in training (out-of-sample). Compare performance metrics (Sharpe ratio, maximum drawdown, P&L) against baselines.
    - **Comparison to known benchmarks:** When analytical solutions exist for simplified versions of the problem (e.g., Merton, Almgren-Chriss), verify that the RL agent matches or beats these solutions in the appropriate limits.
    - **Stress testing:** Evaluate the policy under extreme scenarios (market crashes, liquidity droughts, correlation breakdowns). A good policy should degrade gracefully, not catastrophically.
    - **Sensitivity analysis:** Perturb the state inputs and verify that the policy's actions change smoothly and sensibly (e.g., higher volatility $\to$ smaller positions).
    - **Cross-validation:** Train multiple agents with different random seeds and architectures. If they converge to similar policies, this increases confidence that the solution is robust.
    - **Paper trading:** Deploy the policy in a live market environment without real capital to assess performance and detect discrepancies between simulation and reality.
    - **Gradual deployment:** Start with very small allocations and increase gradually as confidence builds, monitoring for any deviation from expected behavior.

    The absence of a verification theorem means that RL-based strategies require more extensive empirical validation and should always be deployed with appropriate risk controls (position limits, stop-losses, kill switches).
