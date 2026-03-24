# Regret Bounds


**Regret** measures the performance loss of a learning algorithm relative to the best fixed strategy in hindsight.

---

## Definition of regret


For a sequence of losses \(\ell_t\),

\[
\text{Regret}_T
= \sum_{t=1}^T \ell_t(a_t)
- \min_{a} \sum_{t=1}^T \ell_t(a).
\]



Low regret means the algorithm learns effectively.

---

## Types of regret


Common notions include:
- static regret (vs best fixed action),
- dynamic regret (vs time-varying benchmark),
- policy regret (in control settings).

Each reflects different learning goals.

---

## Regret bounds


Typical guarantees are:
- \(O(\sqrt{T})\) regret for convex losses,
- logarithmic regret for strongly convex problems.

Bounds are often worst-case.

---

## Financial interpretation


In finance:
- regret corresponds to opportunity cost,
- low regret ensures competitive long-run performance,
- regret bounds provide model-free guarantees.

---

## Key takeaways


- Regret quantifies learning performance.
- Sublinear regret implies convergence.
- Guarantees are conservative but robust.

---

## Further reading


- Shalev-Shwartz, online learning.
- Bubeck & Cesa-Bianchi, regret analysis.

---

## Exercises

**Exercise 1.** A portfolio manager selects among $K = 5$ assets each day using the Hedge algorithm. After $T = 252$ trading days, the cumulative returns of the five assets are $\{12\%, 8\%, -3\%, 5\%, 15\%\}$. The Hedge algorithm achieved a cumulative return of $10\%$. (a) Compute the static regret relative to the best asset in hindsight. (b) The theoretical regret bound for Hedge is $R_T \le \sqrt{T \ln K / 2}$ (in units of per-period loss bounded in $[0,1]$). If daily returns are in $[-3\%, 3\%]$, rescale the bound appropriately and compare with the actual regret. (c) Explain why $O(\sqrt{T})$ regret implies that the average per-period regret $R_T / T \to 0$ as $T \to \infty$.

---

**Exercise 2.** Define static and dynamic regret precisely. Static regret compares to the best fixed action: $R_T^{\text{static}} = \sum_{t=1}^T \ell_t(a_t) - \min_a \sum_{t=1}^T \ell_t(a)$. Dynamic regret compares to a time-varying benchmark: $R_T^{\text{dynamic}} = \sum_{t=1}^T \ell_t(a_t) - \sum_{t=1}^T \ell_t(a_t^*)$ where $a_t^* = \arg\min_a \ell_t(a)$. (a) Show that dynamic regret is always at least as large as static regret. (b) Why is $O(\sqrt{T})$ dynamic regret generally impossible without assumptions on the variation of $a_t^*$? (c) In a financial context, argue that dynamic regret is the more relevant measure for portfolio management in regime-switching markets, but static regret is more achievable.

---

**Exercise 3.** For online gradient descent with convex losses and step size $\eta_t = 1/\sqrt{t}$, the regret bound is

$$
R_T \le \frac{D^2}{2\eta_T} + \frac{1}{2}\sum_{t=1}^T \eta_t \|\nabla \ell_t(a_t)\|^2
$$

where $D$ is the diameter of the decision set. (a) Show that with $\eta_t = D/(G\sqrt{T})$ (constant step size, $G$ is the gradient bound), this gives $R_T \le DG\sqrt{T}$. (b) For strongly convex losses with parameter $\mu > 0$, the regret improves to $O(\frac{G^2}{\mu}\ln T)$. Explain intuitively why strong convexity helps: the loss landscape has more curvature, making it easier to identify the optimum. (c) In portfolio optimization, when is the loss function strongly convex (hint: consider variance-penalized returns)?

---

**Exercise 4.** A trading firm uses an online learning algorithm to allocate among three momentum strategies. The losses (negative returns) over 5 periods are:

| Period | Strategy A | Strategy B | Strategy C |
|--------|-----------|-----------|-----------|
| 1 | 0.2 | 0.5 | 0.3 |
| 2 | 0.6 | 0.1 | 0.4 |
| 3 | 0.3 | 0.3 | 0.7 |
| 4 | 0.8 | 0.2 | 0.1 |
| 5 | 0.1 | 0.4 | 0.5 |

(a) Compute the cumulative loss of the best fixed strategy in hindsight. (b) Run the Hedge algorithm with learning rate $\eta = \sqrt{2 \ln 3 / 5}$ starting with equal weights, and compute the cumulative loss of the algorithm. (c) Compute the actual regret and compare it with the theoretical bound $\sqrt{T \ln K / 2}$.

---

**Exercise 5.** Explain the financial interpretation of sublinear regret. If $R_T = O(\sqrt{T})$, then the average per-period regret is $R_T / T = O(1/\sqrt{T})$. (a) For a daily trading strategy over 10 years ($T \approx 2520$), compute the per-period regret bound for $K = 20$ assets. (b) Argue that sublinear regret means the algorithm is "almost as good" as the best fixed strategy in the long run. (c) Discuss the limitation: the benchmark is the best *fixed* strategy, but in practice, managers change strategies over time. How does this relate to the distinction between static and dynamic regret? (d) If transaction costs of $c$ per trade are included, how does this modify the regret analysis?

---

**Exercise 6.** Policy regret arises in control settings where the learner's action at time $t$ affects future states. In optimal execution, the trader's order at time $t$ impacts the price at time $t+1$ through market impact. (a) Explain why standard (external) regret is insufficient for this setting: the comparison to the best fixed action ignores that a different sequence of actions would have produced different price paths. (b) Define policy regret as $R_T^{\text{policy}} = \sum_{t=1}^T \ell_t(a_1, \ldots, a_T) - \min_\pi \sum_{t=1}^T \ell_t(\pi)$ where $\pi$ is a policy. (c) Discuss why policy regret bounds are generally harder to obtain and require additional structural assumptions (e.g., bounded memory, Markov dynamics).

---

**Exercise 7.** Lower bounds establish that certain regret rates are optimal. For the experts problem with $K$ experts and adversarial losses in $[0,1]$, the minimax regret is $\Theta(\sqrt{T \ln K})$. (a) Explain what "minimax" means here: it is the best achievable worst-case regret over all possible algorithms. (b) Verify that the Hedge algorithm is minimax optimal (up to constants). (c) For strongly convex losses, the minimax regret drops to $\Theta(\ln T)$. Provide a financial example where the loss function is naturally strongly convex. (d) Discuss the practical gap between worst-case bounds and typical-case performance: in most financial applications, actual regret is much smaller than the worst-case bound. Why?
