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

\[
0 = \sup_u \left\{ \mathcal{L}^u V + r(x,u) \right\},
\]


where \(\mathcal{L}^u\) is the controlled generator.

This is the continuous-time analogue of Bellman equations.

---

## RL as data-driven control


Reinforcement learning can be viewed as:
- approximating value functions,
- solving control problems without known dynamics,
- replacing model-based control with data-driven learning.

---

## Financial applications


Connections appear in:
- optimal trading and execution,
- portfolio optimization,
- market making and hedging.

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
