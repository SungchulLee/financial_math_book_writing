# Markov Decision Processes


Reinforcement learning is built on the framework of **Markov Decision Processes (MDPs)**, which formalize sequential decision-making under uncertainty.

---

## Definition of an MDP


An MDP consists of:
- a state space \(\mathcal{S}\),
- an action space \(\mathcal{A}\),
- transition probabilities \(P(s' \mid s,a)\),
- a reward function \(r(s,a)\),
- a discount factor \(\gamma \in (0,1]\).

The system evolves according to the Markov property.

---

## Policies and value functions


A **policy** \(\pi(a\mid s)\) specifies how actions are chosen.
The value function is

\[
V^{\pi}(s) = \mathbb{E}^{\pi}\left[ \sum_{t=0}^\infty \gamma^t r(s_t,a_t) \mid s_0=s \right].
\]



Optimal policies maximize expected cumulative reward.

---

## Bellman equations


Optimal value functions satisfy the Bellman equation:

\[
V^*(s) = \max_a \left\{ r(s,a) + \gamma \sum_{s'} P(s'\mid s,a) V^*(s') \right\}.
\]



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

---

**Exercise 2.** The Bellman optimality equation is $V^*(s) = \max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')\}$. (a) Show that the Bellman operator $TV(s) = \max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V(s')\}$ is a contraction mapping with modulus $\gamma$ in the sup-norm: $\|TV - TW\|_\infty \le \gamma \|V - W\|_\infty$. (b) By the Banach fixed-point theorem, value iteration $V_{n+1} = TV_n$ converges to $V^*$. How many iterations are needed to guarantee $\|V_n - V^*\|_\infty \le \epsilon$? (c) For $\gamma = 0.99$ and $\epsilon = 0.01$, compute the required number of iterations.

---

**Exercise 3.** In a financial MDP for optimal execution, the state is $s = (q, S, t)$ where $q$ is remaining inventory, $S$ is the stock price, and $t$ is time. The action is the number of shares to sell $n \in \{0, 1, \ldots, q\}$. (a) Define the transition kernel: $q' = q - n$, $S' = S - \gamma n + \sigma \varepsilon$ (permanent impact plus noise). (b) Define the reward: $r = n(S - \eta n)$ (revenue minus temporary impact cost). (c) What is the terminal condition at $t = T$ if unsold inventory is penalized by $-\Lambda q_T^2$? (d) Explain why this MDP has a finite state space if we discretize $S$ and $q$, making exact dynamic programming feasible.

---

**Exercise 4.** The action-value function $Q^*(s, a) = r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')$ satisfies the Bellman equation $Q^*(s,a) = r(s,a) + \gamma \sum_{s'} P(s'|s,a) \max_{a'} Q^*(s', a')$. (a) Show that $V^*(s) = \max_a Q^*(s,a)$ and $\pi^*(s) = \arg\max_a Q^*(s,a)$. (b) Q-learning updates $Q(s,a)$ using $Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{a'} Q(s',a') - Q(s,a)]$. Explain why this is a stochastic approximation of the Bellman equation that converges to $Q^*$ without knowing $P$. (c) Why is Q-learning called "model-free"?

---

**Exercise 5.** The discount factor $\gamma$ has different interpretations in RL and finance. (a) In RL, $\gamma < 1$ ensures the infinite-horizon sum converges. Compute $\sum_{t=0}^\infty \gamma^t r$ for constant reward $r = 1$ and $\gamma = 0.99$. (b) In finance, $\gamma = e^{-r \Delta t}$ corresponds to the risk-free rate $r$. For $r = 5\%$ annual and $\Delta t = 1/252$ (daily), compute $\gamma$. (c) In many financial problems (e.g., execution over a fixed horizon $T$), the MDP is finite-horizon and no discounting is needed ($\gamma = 1$ with terminal time $T$). Explain why the Bellman equation still has a unique solution in the finite-horizon case.

---

**Exercise 6.** Policy iteration alternates between policy evaluation (computing $V^\pi$) and policy improvement (setting $\pi'(s) = \arg\max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^\pi(s')\}$). (a) Prove that $V^{\pi'} \ge V^\pi$ for all states (policy improvement theorem). (b) Since there are finitely many deterministic policies, policy iteration terminates in finitely many steps. For $|\mathcal{S}| = 100$ and $|\mathcal{A}| = 10$, how many deterministic policies exist? (c) In practice, policy iteration often converges in very few iterations. Compare the per-iteration cost of policy iteration (requires solving a linear system for $V^\pi$) with value iteration (requires only one Bellman backup per state). Which is faster overall?

---

**Exercise 7.** The Markov property states that $P(s_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, \ldots) = P(s_{t+1} | s_t, a_t)$. (a) In a portfolio optimization problem, argue that the current stock price alone is not Markov: future returns may depend on past returns through momentum or mean-reversion effects. (b) Propose an augmented state $s_t = (S_t, S_{t-1}, \ldots, S_{t-p}, \hat{\sigma}_t)$ that includes lagged prices and estimated volatility to restore the Markov property. (c) Discuss the curse of dimensionality: as the state space grows (more lagged features, more assets), the number of states grows exponentially. How do function approximation methods (neural networks for $V$ or $Q$) address this challenge?
