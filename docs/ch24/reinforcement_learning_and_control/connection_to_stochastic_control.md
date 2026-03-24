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

---

## Exercises

**Exercise 1.** Consider the Merton portfolio optimization problem: maximize $\mathbb{E}[\int_0^T e^{-\rho t} U(c_t) dt + e^{-\rho T} U(W_T)]$ where $W_t$ is wealth, $c_t$ is consumption, and $U(x) = x^{1-\gamma}/(1-\gamma)$ is CRRA utility. The wealth dynamics are $dW_t = W_t[(\mu - r)\pi_t + r] dt + W_t \pi_t \sigma dB_t - c_t dt$, where $\pi_t$ is the risky asset fraction. (a) Write the HJB equation $0 = \sup_{\pi, c}\{\partial_t V + \mathcal{L}^{\pi,c} V + e^{-\rho t} U(c)\}$. (b) Conjecture $V(t, W) = e^{-\rho t} f(t) W^{1-\gamma}/(1-\gamma)$ and derive the optimal controls $\pi^* = (\mu-r)/(\gamma \sigma^2)$ and $c^* = W / f(t)$. (c) Explain how an RL agent could learn these controls without knowing $\mu$ and $\sigma$.

---

**Exercise 2.** The Bellman equation in discrete time is $V^*(s) = \max_a \{r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')\}$. The HJB equation in continuous time is $0 = \sup_u \{\mathcal{L}^u V + r(x,u)\}$ where $\mathcal{L}^u V = \partial_t V + b(x,u) \partial_x V + \frac{1}{2}\sigma^2(x,u) \partial_{xx} V$. (a) Show that the discrete-time Bellman equation converges to the continuous-time HJB as the time step $\Delta t \to 0$. (Hint: expand $V(t + \Delta t, x')$ in a Taylor series.) (b) Identify the discount factor $\gamma$ with $e^{-\rho \Delta t}$. (c) Explain why the HJB is a PDE while the Bellman equation is a functional equation, and why numerical methods differ.

---

**Exercise 3.** In model-based stochastic control, the dynamics $dx_t = b(x_t, u_t)dt + \sigma(x_t, u_t)dW_t$ are known. In RL, they are unknown. (a) List the advantages of model-based control: exact solutions for LQ problems, convergence guarantees, interpretability. (b) List the advantages of RL: no model needed, handles nonlinear dynamics, adapts to real data. (c) For optimal execution with linear impact (Almgren-Chriss), the model-based solution is a known closed-form. Why might an RL agent still be preferable in practice? (Hint: consider nonlinear impact, stochastic liquidity, and intraday patterns.)

---

**Exercise 4.** Consider a simple stochastic control problem: $dx_t = u_t dt + \sigma dW_t$ with cost $J = \mathbb{E}[\int_0^T (x_t^2 + u_t^2)dt + x_T^2]$. (a) Write the HJB equation and conjecture $V(t,x) = a(t)x^2 + b(t)$. Derive the Riccati equation for $a(t)$. (b) The optimal control is $u^* = -a(t)x$. A Q-learning agent learns the Q-function $Q(x, u) \approx x^2 + u^2 + \gamma V(x')$ from sampled transitions. Compare the sample efficiency of Q-learning with the analytical Riccati solution. (c) For this LQ problem, how many training episodes would Q-learning need to achieve 1% error in the optimal policy?

---

**Exercise 5.** Risk-sensitive stochastic control minimizes $J_\lambda = -\frac{1}{\lambda} \ln \mathbb{E}[e^{-\lambda \sum_t r_t}]$ where $\lambda > 0$ controls risk aversion. (a) Show that as $\lambda \to 0$, $J_\lambda \to \mathbb{E}[\sum_t r_t]$ (risk-neutral). (b) Show that as $\lambda \to \infty$, $J_\lambda \to \min_\omega \sum_t r_t(\omega)$ (worst-case). (c) Write the risk-sensitive Bellman equation: $V(s) = \sup_a \{r(s,a) - \frac{1}{\lambda}\ln \mathbb{E}_s[e^{-\lambda V(s')}]\}$. (d) Explain why this formulation is natural for financial applications where tail risk matters.

---

**Exercise 6.** A market maker must continuously quote bid and ask prices. This is a stochastic control problem where the state is $(q_t, S_t, t)$ (inventory, mid-price, time), the controls are the bid-ask spread $(d_a, d_b)$, and the objective trades off P&L against inventory risk. (a) Write the HJB equation for the Avellaneda-Stoikov market-making model. (b) The optimal spread is $d^* = \frac{1}{\gamma}\ln(1 + \gamma/\kappa) + \frac{\gamma}{2}\sigma^2(T-t)$ where $\gamma$ is risk aversion and $\kappa$ is order arrival intensity. Interpret each term. (c) An RL agent trained on historical LOB data learns a market-making policy. What advantages does it have over the Avellaneda-Stoikov solution?

---

**Exercise 7.** The verification theorem states that if a smooth function $V$ satisfies the HJB equation with appropriate boundary conditions, then $V$ is the optimal value function. (a) Explain why this is important: it confirms that a candidate solution is truly optimal. (b) When might the verification theorem fail? (Hint: viscosity solutions are needed when $V$ is not smooth.) (c) In RL, there is no verification theorem---the agent converges to a local optimum at best. Discuss the implications for deploying RL-based trading strategies: how do you validate that the learned policy is actually good? Propose validation methods (backtesting, comparison to known benchmarks, stress testing).
