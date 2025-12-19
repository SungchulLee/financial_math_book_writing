# Markov Decision Processes

Reinforcement learning is built on the framework of **Markov Decision Processes (MDPs)**, which formalize sequential decision-making under uncertainty.

---

## 1. Definition of an MDP

An MDP consists of:
- a state space \(\mathcal{S}\),
- an action space \(\mathcal{A}\),
- transition probabilities \(P(s' \mid s,a)\),
- a reward function \(r(s,a)\),
- a discount factor \(\gamma \in (0,1]\).

The system evolves according to the Markov property.

---

## 2. Policies and value functions

A **policy** \(\pi(a\mid s)\) specifies how actions are chosen.
The value function is

\[
V^{\pi}(s) = \mathbb{E}^{\pi}\left[ \sum_{t=0}^\infty \gamma^t r(s_t,a_t) \mid s_0=s \right].
\]



Optimal policies maximize expected cumulative reward.

---

## 3. Bellman equations

Optimal value functions satisfy the Bellman equation:

\[
V^*(s) = \max_a \left\{ r(s,a) + \gamma \sum_{s'} P(s'\mid s,a) V^*(s') \right\}.
\]



This recursion underlies dynamic programming and RL algorithms.

---

## 4. Financial interpretation

In finance:
- states represent market and portfolio conditions,
- actions represent trading or control decisions,
- rewards represent profits, utilities, or risk-adjusted returns.

---

## 5. Key takeaways

- MDPs formalize sequential decisions under uncertainty.
- Value functions encode long-term objectives.
- Bellman equations are central to optimal control.

---

## Further reading

- Puterman, *Markov Decision Processes*.
- Sutton & Barto, *Reinforcement Learning*.
