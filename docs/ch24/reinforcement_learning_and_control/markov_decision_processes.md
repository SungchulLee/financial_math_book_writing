# Markov Decision Processes


Reinforcement learning is built on the framework of **Markov Decision Processes (MDPs)**, which formalize sequential decision-making under uncertainty.

---

## Definition of an MDP


An MDP consists of:
- a state space $\mathcal{S}$,
- an action space $\mathcal{A}$,
- transition probabilities $P(s' \mid s,a)$,
- a reward function $r(s,a)$,
- a discount factor $\gamma \in (0,1]$.

The system evolves according to the Markov property.

---

## Policies and value functions


A **policy** $\pi(a\mid s)$ specifies how actions are chosen.
The value function is

$$
V^{\pi}(s) = \mathbb{E}^{\pi}\left[ \sum_{t=0}^\infty \gamma^t r(s_t,a_t) \mid s_0=s \right]
$$



Optimal policies maximize expected cumulative reward.

---

## Bellman equations


Optimal value functions satisfy the Bellman equation:

$$
V^*(s) = \max_a \left\{ r(s,a) + \gamma \sum_{s'} P(s'\mid s,a) V^*(s') \right\}
$$



This recursion underlies dynamic programming and RL algorithms.

---

## Financial interpretation


In finance:
- states represent market and portfolio conditions,
- actions represent trading or control decisions,
- rewards represent profits, utilities, or risk-adjusted returns.

---

## Key takeaways


- MDPs formalize sequential decisions under uncertainty.
- Value functions encode long-term objectives.
- Bellman equations are central to optimal control.

---

## Further reading


- Puterman, *Markov Decision Processes*.
- Sutton & Barto, *Reinforcement Learning*.

---

## Exercises

**Exercise 1.** Consider a simple portfolio MDP with states $\mathcal{S} = \{\text{bull}, \text{bear}\}$, actions $\mathcal{A} = \{\text{stocks}, \text{bonds}\}$, discount factor $\gamma = 0.95$, and the following transition probabilities and rewards:

| $(s, a)$ | $P(\text{bull} \mid s, a)$ | $P(\text{bear} \mid s, a)$ | $r(s, a)$ |
|---|---|---|---|
| (bull, stocks) | 0.8 | 0.2 | 0.10 |
| (bull, bonds) | 0.7 | 0.3 | 0.03 |
| (bear, stocks) | 0.4 | 0.6 | $-$0.15 |
| (bear, bonds) | 0.5 | 0.5 | 0.02 |

(a) Compute the value function $V^\pi$ for the policy "always stocks" by solving the Bellman equation $V^\pi(s) = r(s, \pi(s)) + \gamma \sum_{s'} P(s'|s, \pi(s)) V^\pi(s')$. (b) Compute $V^\pi$ for the policy "always bonds." (c) Find the optimal policy using value iteration.

??? success "Solution to Exercise 1"
    **(a) Value function for "always stocks."**

    Under the policy $\pi(s) = \text{stocks}$ for all $s$, the Bellman evaluation equation is:

    $$
    V^\pi(s) = r(s, \text{stocks}) + \gamma \sum_{s'} P(s' \mid s, \text{stocks}) V^\pi(s')
    $$

    Writing this out for both states:

    $$
    V^\pi(\text{bull}) = 0.10 + 0.95[0.8 \, V^\pi(\text{bull}) + 0.2 \, V^\pi(\text{bear})]
    $$

    $$
    V^\pi(\text{bear}) = -0.15 + 0.95[0.4 \, V^\pi(\text{bull}) + 0.6 \, V^\pi(\text{bear})]
    $$

    Let $x = V^\pi(\text{bull})$ and $y = V^\pi(\text{bear})$. Then:

    $$
    x = 0.10 + 0.76x + 0.19y \implies 0.24x - 0.19y = 0.10
    $$

    $$
    y = -0.15 + 0.38x + 0.57y \implies -0.38x + 0.43y = -0.15
    $$

    From the first equation: $x = (0.10 + 0.19y)/0.24$. Substituting into the second:

    $$
    -0.38 \cdot \frac{0.10 + 0.19y}{0.24} + 0.43y = -0.15
    $$

    $$
    -\frac{0.038 + 0.0722y}{0.24} + 0.43y = -0.15
    $$

    $$
    -0.15833 - 0.30083y + 0.43y = -0.15
    $$

    $$
    0.12917y = 0.00833 \implies y \approx 0.0645
    $$

    $$
    x = \frac{0.10 + 0.19 \times 0.0645}{0.24} = \frac{0.11226}{0.24} \approx 0.4677
    $$

    So $V^\pi(\text{bull}) \approx 0.468$ and $V^\pi(\text{bear}) \approx 0.065$.

    **(b) Value function for "always bonds."**

    Under $\pi(s) = \text{bonds}$:

    $$
    V^\pi(\text{bull}) = 0.03 + 0.95[0.7 \, V^\pi(\text{bull}) + 0.3 \, V^\pi(\text{bear})]
    $$

    $$
    V^\pi(\text{bear}) = 0.02 + 0.95[0.5 \, V^\pi(\text{bull}) + 0.5 \, V^\pi(\text{bear})]
    $$

    Let $x = V^\pi(\text{bull})$, $y = V^\pi(\text{bear})$:

    $$
    0.335x - 0.285y = 0.03
    $$

    $$
    -0.475x + 0.525y = 0.02
    $$

    From the first equation: $x = (0.03 + 0.285y)/0.335$. Substituting:

    $$
    -0.475 \cdot \frac{0.03 + 0.285y}{0.335} + 0.525y = 0.02
    $$

    $$
    -0.04254 - 0.40448y + 0.525y = 0.02
    $$

    $$
    0.12052y = 0.06254 \implies y \approx 0.5189
    $$

    $$
    x = \frac{0.03 + 0.285 \times 0.5189}{0.335} \approx \frac{0.1779}{0.335} \approx 0.5310
    $$

    So $V^\pi(\text{bull}) \approx 0.531$ and $V^\pi(\text{bear}) \approx 0.519$.

    **(c) Optimal policy via value iteration.**

    Initialize $V_0(\text{bull}) = V_0(\text{bear}) = 0$. At each iteration, apply the Bellman optimality operator:

    $$
    V_{n+1}(s) = \max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V_n(s')\}
    $$

    **Iteration 1:** $V_1(\text{bull}) = \max(0.10, 0.03) = 0.10$ (stocks), $V_1(\text{bear}) = \max(-0.15, 0.02) = 0.02$ (bonds).

    **Iteration 2:**

    - Bull, stocks: $0.10 + 0.95(0.8 \times 0.10 + 0.2 \times 0.02) = 0.10 + 0.0798 = 0.1798$
    - Bull, bonds: $0.03 + 0.95(0.7 \times 0.10 + 0.3 \times 0.02) = 0.03 + 0.0723 = 0.1023$
    - Bear, stocks: $-0.15 + 0.95(0.4 \times 0.10 + 0.6 \times 0.02) = -0.15 + 0.0494 = -0.1006$
    - Bear, bonds: $0.02 + 0.95(0.5 \times 0.10 + 0.5 \times 0.02) = 0.02 + 0.057 = 0.077$

    So $V_2(\text{bull}) = 0.1798$ (stocks), $V_2(\text{bear}) = 0.077$ (bonds).

    Continuing this process to convergence, the optimal policy is: **stocks in bull, bonds in bear**. This is intuitive---invest in stocks during favorable market conditions and switch to bonds during downturns. The converged values lie between those of the two constant policies, with the optimal policy achieving higher value than either pure policy in both states.

---

**Exercise 2.** The Bellman optimality equation is $V^*(s) = \max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')\}$. (a) Show that the Bellman operator $TV(s) = \max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V(s')\}$ is a contraction mapping with modulus $\gamma$ in the sup-norm: $\|TV - TW\|_\infty \le \gamma \|V - W\|_\infty$. (b) By the Banach fixed-point theorem, value iteration $V_{n+1} = TV_n$ converges to $V^*$. How many iterations are needed to guarantee $\|V_n - V^*\|_\infty \le \epsilon$? (c) For $\gamma = 0.99$ and $\epsilon = 0.01$, compute the required number of iterations.

??? success "Solution to Exercise 2"
    **(a) Contraction mapping proof.**

    Let $V, W : \mathcal{S} \to \mathbb{R}$. For any state $s$:

    $$
    (TV)(s) = \max_a \left\{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V(s')\right\}
    $$

    $$
    (TW)(s) = \max_a \left\{r(s,a) + \gamma \sum_{s'} P(s'|s,a) W(s')\right\}
    $$

    Let $a^*_V = \arg\max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V(s')\}$. Then:

    $$
    (TV)(s) - (TW)(s) = \max_a \{r + \gamma P V\} - \max_a \{r + \gamma P W\}
    $$

    Using the inequality $\max_a f(a) - \max_a g(a) \le \max_a [f(a) - g(a)]$:

    $$
    (TV)(s) - (TW)(s) \le \max_a \left\{\gamma \sum_{s'} P(s'|s,a)[V(s') - W(s')]\right\}
    $$

    $$
    \le \gamma \max_a \sum_{s'} P(s'|s,a) \|V - W\|_\infty = \gamma \|V - W\|_\infty
    $$

    since $\sum_{s'} P(s'|s,a) = 1$. By symmetry (swapping $V$ and $W$), $(TW)(s) - (TV)(s) \le \gamma \|V - W\|_\infty$. Therefore:

    $$
    |(TV)(s) - (TW)(s)| \le \gamma \|V - W\|_\infty \quad \forall s
    $$

    Taking the supremum over $s$ gives $\|TV - TW\|_\infty \le \gamma \|V - W\|_\infty$. $\square$

    **(b) Number of iterations.**

    By the contraction property, after $n$ iterations starting from $V_0$:

    $$
    \|V_n - V^*\|_\infty \le \gamma^n \|V_0 - V^*\|_\infty
    $$

    To ensure $\|V_n - V^*\|_\infty \le \epsilon$, we need $\gamma^n \|V_0 - V^*\|_\infty \le \epsilon$, so:

    $$
    n \ge \frac{\ln(\|V_0 - V^*\|_\infty / \epsilon)}{\ln(1/\gamma)}
    $$

    Using the bound $\|V_0 - V^*\|_\infty \le R_{\max}/(1-\gamma)$ (where $R_{\max} = \max_{s,a} |r(s,a)|$), we get:

    $$
    n \ge \frac{\ln(R_{\max} / ((1-\gamma)\epsilon))}{\ln(1/\gamma)}
    $$

    **(c) For $\gamma = 0.99$, $\epsilon = 0.01$.**

    Assuming $R_{\max} = 1$ (bounded rewards):

    $$
    \|V_0 - V^*\|_\infty \le \frac{1}{1 - 0.99} = 100
    $$

    $$
    n \ge \frac{\ln(100 / 0.01)}{\ln(1/0.99)} = \frac{\ln(10{,}000)}{0.01005} \approx \frac{9.2103}{0.01005} \approx 917
    $$

    Approximately **917 iterations** are needed. This illustrates the slow convergence of value iteration when $\gamma$ is close to 1, which is common in financial applications with long time horizons.

---

**Exercise 3.** In a financial MDP for optimal execution, the state is $s = (q, S, t)$ where $q$ is remaining inventory, $S$ is the stock price, and $t$ is time. The action is the number of shares to sell $n \in \{0, 1, \ldots, q\}$. (a) Define the transition kernel: $q' = q - n$, $S' = S - \gamma n + \sigma \varepsilon$ (permanent impact plus noise). (b) Define the reward: $r = n(S - \eta n)$ (revenue minus temporary impact cost). (c) What is the terminal condition at $t = T$ if unsold inventory is penalized by $-\Lambda q_T^2$? (d) Explain why this MDP has a finite state space if we discretize $S$ and $q$, making exact dynamic programming feasible.

??? success "Solution to Exercise 3"
    **(a) Transition kernel.**

    The state is $s = (q, S, t)$. Given action $n$ (shares to sell):

    - Inventory: $q' = q - n$ (deterministic given $n$)
    - Price: $S' = S - \gamma n + \sigma \varepsilon$ where $\varepsilon \sim \mathcal{N}(0, \Delta t)$ (or $\varepsilon \sim \mathcal{N}(0,1)$ scaled by $\sqrt{\Delta t}$)
    - Time: $t' = t + \Delta t$

    The transition kernel factors as:

    $$
    P(q', S', t' \mid q, S, t, n) = \mathbf{1}_{q' = q-n} \cdot \mathbf{1}_{t'=t+\Delta t} \cdot \frac{1}{\sigma\sqrt{2\pi \Delta t}} \exp\!\left(-\frac{(S' - S + \gamma n)^2}{2\sigma^2 \Delta t}\right)
    $$

    The permanent impact term $-\gamma n$ shifts the price permanently, and $\sigma \varepsilon$ adds random noise reflecting fundamental price uncertainty.

    **(b) Reward function.**

    The per-step reward (revenue minus temporary impact cost) is:

    $$
    r(s, n) = n(S - \eta n)
    $$

    Here $nS$ is the gross revenue from selling $n$ shares at price $S$, and $\eta n^2$ is the temporary impact cost (the cost of moving the execution price by $\eta n$ on $n$ shares). The temporary impact parameter $\eta$ penalizes large trades quadratically, encouraging the agent to spread trades over time.

    **(c) Terminal condition.**

    At $t = T$, the terminal reward is:

    $$
    r_T = -\Lambda q_T^2
    $$

    This quadratic penalty for unsold inventory ensures the agent has a strong incentive to complete the liquidation. The parameter $\Lambda > 0$ controls how severely remaining inventory is penalized. As $\Lambda \to \infty$, the constraint $q_T = 0$ is enforced exactly (hard constraint limit). In the Bellman equation, $V(T, q, S) = -\Lambda q^2$ serves as the terminal condition for backward induction.

    **(d) Finite state space and exact DP.**

    If $q \in \{0, 1, \ldots, Q\}$ (where $Q$ is the initial inventory) and $S$ is discretized into $M$ price levels, and $t \in \{0, \Delta t, 2\Delta t, \ldots, T\}$ has $N+1$ time points, then:

    $$
    |\mathcal{S}| = (Q+1) \times M \times (N+1)
    $$

    For example, $Q = 100$ shares, $M = 200$ price levels, $N = 10$ time steps gives $|\mathcal{S}| = 101 \times 200 \times 11 = 222{,}200$ states. At each state, the action space is $\{0, 1, \ldots, q\}$, which has at most $Q+1$ elements. Since $|\mathcal{S}|$ is moderate, exact dynamic programming (backward induction) is computationally feasible: at each time step, compute the Bellman update for all $(q, S)$ pairs, requiring $O((Q+1) \times M \times (Q+1))$ operations per time step. The total complexity is $O(N \times Q^2 \times M)$, which is polynomial and tractable for reasonable problem sizes.

---

**Exercise 4.** The action-value function $Q^*(s, a) = r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')$ satisfies the Bellman equation $Q^*(s,a) = r(s,a) + \gamma \sum_{s'} P(s'|s,a) \max_{a'} Q^*(s', a')$. (a) Show that $V^*(s) = \max_a Q^*(s,a)$ and $\pi^*(s) = \arg\max_a Q^*(s,a)$. (b) Q-learning updates $Q(s,a)$ using $Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$. Explain why this is a stochastic approximation of the Bellman equation that converges to $Q^*$ without knowing $P$. (c) Why is Q-learning called "model-free"?

??? success "Solution to Exercise 4"
    **(a) Relationship between $V^*$, $Q^*$, and $\pi^*$.**

    By definition, $Q^*(s, a) = r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')$. The optimal value function satisfies:

    $$
    V^*(s) = \max_a \left\{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')\right\} = \max_a Q^*(s, a)
    $$

    This follows directly from substituting the definition of $Q^*$ into the Bellman optimality equation for $V^*$.

    The optimal policy selects the action that achieves this maximum:

    $$
    \pi^*(s) = \arg\max_a Q^*(s, a)
    $$

    This is optimal because for any policy $\pi$:

    $$
    V^{\pi}(s) = Q^{\pi}(s, \pi(s)) \le \max_a Q^{\pi}(s,a) \le \max_a Q^*(s,a) = V^*(s)
    $$

    where the second inequality uses the fact that $Q^* \ge Q^\pi$ for all $\pi$. $\square$

    **(b) Q-learning as stochastic approximation.**

    The Q-learning update is:

    $$
    Q(s,a) \leftarrow Q(s,a) + \alpha\left[r + \gamma \max_{a'} Q(s',a') - Q(s,a)\right]
    $$

    The term in brackets is a stochastic sample of the Bellman error. At the fixed point, $Q = Q^*$, the expected update is zero because:

    $$
    \mathbb{E}_{s' \sim P(\cdot|s,a)}\left[r(s,a) + \gamma \max_{a'} Q^*(s', a') - Q^*(s,a)\right] = 0
    $$

    which is exactly the Bellman equation for $Q^*$. The update can be written in the Robbins-Monro stochastic approximation form:

    $$
    Q_{n+1}(s,a) = Q_n(s,a) + \alpha_n\left[F(Q_n)(s,a) - Q_n(s,a) + \xi_n\right]
    $$

    where $F(Q)(s,a) = r(s,a) + \gamma \sum_{s'} P(s'|s,a) \max_{a'} Q(s',a')$ is the Bellman operator and $\xi_n$ is zero-mean noise. Under standard conditions (every state-action pair visited infinitely often, step sizes satisfying $\sum \alpha_n = \infty$, $\sum \alpha_n^2 < \infty$), the contraction property of $F$ ensures $Q_n \to Q^*$ almost surely.

    **(c) Q-learning is "model-free."**

    Q-learning is called model-free because it never requires knowledge of $P(s'|s,a)$ or $r(s,a)$. The algorithm only uses observed transitions $(s, a, r, s')$ obtained by interacting with the environment. The transition probabilities $P$ are implicitly averaged over through repeated sampling. In contrast, value iteration requires explicit knowledge of $P$ and $r$ to compute the sum $\sum_{s'} P(s'|s,a) V(s')$. For financial applications, this is significant: the agent does not need a model of how the market transitions---it learns directly from market data or simulated trading experience.

---

**Exercise 5.** The discount factor $\gamma$ has different interpretations in RL and finance. (a) In RL, $\gamma < 1$ ensures the infinite-horizon sum converges. Compute $\sum_{t=0}^\infty \gamma^t r$ for constant reward $r = 1$ and $\gamma = 0.99$. (b) In finance, $\gamma = e^{-r \Delta t}$ corresponds to the risk-free rate $r$. For $r = 5\%$ annual and $\Delta t = 1/252$ (daily), compute $\gamma$. (c) In many financial problems (e.g., execution over a fixed horizon $T$), the MDP is finite-horizon and no discounting is needed ($\gamma = 1$ with terminal time $T$). Explain why the Bellman equation still has a unique solution in the finite-horizon case.

??? success "Solution to Exercise 5"
    **(a) Geometric series with $\gamma = 0.99$, $r = 1$.**

    $$
    \sum_{t=0}^{\infty} \gamma^t r = \frac{r}{1 - \gamma} = \frac{1}{1 - 0.99} = \frac{1}{0.01} = 100
    $$

    A constant reward of 1 per period has a present value of 100 when discounted at $\gamma = 0.99$.

    **(b) Financial discount factor.**

    With $r = 5\% = 0.05$ annually and $\Delta t = 1/252$ (one trading day):

    $$
    \gamma = e^{-r \Delta t} = e^{-0.05/252} = e^{-0.000198} \approx 1 - 0.000198 \approx 0.999802
    $$

    This discount factor is very close to 1, reflecting the fact that daily discounting at a 5% annual rate is negligible per step. Over a full year ($252$ steps), the cumulative discount is $\gamma^{252} = e^{-0.05} \approx 0.9512$.

    **(c) Finite-horizon Bellman equation uniqueness.**

    In the finite-horizon case with $T$ periods and $\gamma = 1$, the Bellman equation is solved by backward induction:

    $$
    V_T(s) = r_T(s) \quad \text{(terminal reward)}
    $$

    $$
    V_t(s) = \max_a \left\{r(s,a) + \sum_{s'} P(s'|s,a) V_{t+1}(s')\right\}, \quad t = T-1, T-2, \ldots, 0
    $$

    The solution is unique because each step is a deterministic computation given the solution at the next time step. Starting from the terminal condition $V_T$ (which is given), each $V_t$ is uniquely determined by a single backward pass. There is no fixed-point equation to solve and no contraction argument is needed. The discount factor $\gamma = 1$ causes no convergence issues because the sum $\sum_{t=0}^{T} r_t$ is finite (having only $T+1$ terms). This is precisely the situation in most financial execution and hedging problems, where the horizon is fixed.

---

**Exercise 6.** Policy iteration alternates between policy evaluation (computing $V^\pi$) and policy improvement (setting $\pi'(s) = \arg\max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^\pi(s')\}$). (a) Prove that $V^{\pi'} \ge V^\pi$ for all states (policy improvement theorem). (b) Since there are finitely many deterministic policies, policy iteration terminates in finitely many steps. For $|\mathcal{S}| = 100$ and $|\mathcal{A}| = 10$, how many deterministic policies exist? (c) In practice, policy iteration often converges in very few iterations. Compare the per-iteration cost of policy iteration (requires solving a linear system for $V^\pi$) with value iteration (requires only one Bellman backup per state). Which is faster overall?

??? success "Solution to Exercise 6"
    **(a) Policy improvement theorem.**

    Let $\pi'(s) = \arg\max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^\pi(s')\}$. By construction:

    $$
    r(s, \pi'(s)) + \gamma \sum_{s'} P(s'|s, \pi'(s)) V^\pi(s') \ge r(s, \pi(s)) + \gamma \sum_{s'} P(s'|s, \pi(s)) V^\pi(s') = V^\pi(s)
    $$

    Define $Q^\pi(s, a) = r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^\pi(s')$. Then $Q^\pi(s, \pi'(s)) \ge V^\pi(s)$.

    Now we show $V^{\pi'}(s) \ge V^\pi(s)$ by repeatedly expanding:

    $$
    V^\pi(s) \le Q^\pi(s, \pi'(s)) = r(s, \pi'(s)) + \gamma \sum_{s'} P(s'|s, \pi'(s)) V^\pi(s')
    $$

    $$
    \le r(s, \pi'(s)) + \gamma \sum_{s'} P(s'|s, \pi'(s)) Q^\pi(s', \pi'(s'))
    $$

    $$
    = r(s, \pi'(s)) + \gamma \sum_{s'} P(s'|s, \pi'(s)) \left[r(s', \pi'(s')) + \gamma \sum_{s''} P(s''|s', \pi'(s')) V^\pi(s'')\right]
    $$

    Continuing this unrolling indefinitely:

    $$
    V^\pi(s) \le \mathbb{E}_{\pi'}\left[\sum_{t=0}^\infty \gamma^t r(s_t, \pi'(s_t)) \mid s_0 = s\right] = V^{\pi'}(s)
    $$

    Therefore $V^{\pi'} \ge V^\pi$ for all states. $\square$

    **(b) Number of deterministic policies.**

    A deterministic policy assigns one of $|\mathcal{A}|$ actions to each of $|\mathcal{S}|$ states. The number of deterministic policies is:

    $$
    |\mathcal{A}|^{|\mathcal{S}|} = 10^{100}
    $$

    This is a googol, an astronomically large number. Despite this, policy iteration terminates in finitely many steps because each iteration strictly improves the policy (unless already optimal), and the number of policies is finite.

    **(c) Cost comparison.**

    **Policy iteration** per iteration requires:

    - Policy evaluation: solve the linear system $(I - \gamma P^\pi) V^\pi = r^\pi$, which has size $|\mathcal{S}| \times |\mathcal{S}|$ and costs $O(|\mathcal{S}|^3)$ (or $O(|\mathcal{S}|^2)$ with iterative methods).
    - Policy improvement: for each state, compute $\arg\max_a$ over $|\mathcal{A}|$ actions, costing $O(|\mathcal{S}| \cdot |\mathcal{A}|)$.
    - Total per iteration: $O(|\mathcal{S}|^3 + |\mathcal{S}| \cdot |\mathcal{A}|)$.

    **Value iteration** per iteration requires: one Bellman backup per state, each involving a max over $|\mathcal{A}|$ actions and a sum over $|\mathcal{S}|$ next states. Cost: $O(|\mathcal{S}|^2 \cdot |\mathcal{A}|)$.

    Policy iteration is more expensive per iteration but typically converges in very few iterations (often 5--20 in practice). Value iteration is cheaper per iteration but may require hundreds or thousands of iterations, especially when $\gamma$ is close to 1. For problems with large $\gamma$ (common in finance), policy iteration is often faster overall.

---

**Exercise 7.** The Markov property states that $P(s_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, \ldots) = P(s_{t+1} | s_t, a_t)$. (a) In a portfolio optimization problem, argue that the current stock price alone is not Markov: future returns may depend on past returns through momentum or mean-reversion effects. (b) Propose an augmented state $s_t = (S_t, S_{t-1}, \ldots, S_{t-p}, \hat{\sigma}_t)$ that includes lagged prices and estimated volatility to restore the Markov property. (c) Discuss the curse of dimensionality: as the state space grows (more lagged features, more assets), the number of states grows exponentially. How do function approximation methods (neural networks for $V$ or $Q$) address this challenge?

??? success "Solution to Exercise 7"
    **(a) Non-Markov nature of price alone.**

    If the state is simply $s_t = S_t$, the future return $R_{t+1} = S_{t+1}/S_t - 1$ may depend on past prices:

    - **Momentum effects:** Assets that have risen recently tend to continue rising (positive autocorrelation in returns). This means $P(S_{t+1} | S_t)$ does not capture all relevant information; the recent trend $(S_t - S_{t-p})/S_{t-p}$ is also informative.
    - **Mean-reversion effects:** Some assets exhibit mean-reversion where extreme prices tend to revert, making $P(S_{t+1} | S_t, S_{t-1}, \ldots)$ different from $P(S_{t+1} | S_t)$.
    - **Volatility clustering:** High-volatility periods tend to follow high-volatility periods (GARCH effects). The current price $S_t$ alone does not encode the current volatility regime.

    Since the conditional distribution $P(S_{t+1} | S_t, S_{t-1}, \ldots)$ depends on past prices, the price process alone is not Markov.

    **(b) Augmented state space.**

    The augmented state

    $$
    s_t = (S_t, S_{t-1}, \ldots, S_{t-p}, \hat{\sigma}_t)
    $$

    includes $p$ lagged prices and an estimated volatility $\hat{\sigma}_t$ (e.g., from an exponentially weighted moving average or GARCH filter). This restores the Markov property if the dependence on history is captured by these features:

    - Lagged prices encode momentum/mean-reversion effects up to lag $p$.
    - $\hat{\sigma}_t$ encodes the current volatility regime.

    One could also include: lagged returns $R_{t-1}, \ldots, R_{t-p}$, trading volume, bid-ask spreads, or other microstructure features. The key requirement is that $P(s_{t+1} | s_t, a_t)$ should not depend on $s_{t-1}, s_{t-2}, \ldots$ after conditioning on $s_t$.

    **(c) Curse of dimensionality and function approximation.**

    With $d$ assets, $p$ lags, and additional features, the state dimension is $d(p+1) + d_{\text{extra}}$. If each dimension is discretized into $m$ levels, the number of states is:

    $$
    |\mathcal{S}| = m^{d(p+1) + d_{\text{extra}}}
    $$

    For $d = 10$ assets, $p = 5$ lags, and $m = 100$ levels, this is $100^{60} = 10^{120}$, which is utterly intractable for tabular methods.

    **Function approximation** addresses this by representing $V(s)$ or $Q(s,a)$ as parameterized functions (e.g., neural networks) with far fewer parameters than states. A neural network with a few hundred thousand parameters can generalize across the continuous state space, exploiting structure and smoothness in the value function. Specifically:

    - Neural networks learn shared features across similar states, avoiding the need to visit every state individually.
    - They can extrapolate to unseen states using learned patterns.
    - The number of parameters scales with the complexity of the value function, not the size of the state space.

    This is essential for financial applications where the state space is inherently high-dimensional and continuous.
