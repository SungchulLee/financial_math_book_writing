# Regret Bounds


**Regret** measures the performance loss of a learning algorithm relative to the best fixed strategy in hindsight.

---

## Definition of regret


For a sequence of losses $\ell_t$,

$$
\text{Regret}_T
= \sum_{t=1}^T \ell_t(a_t)

- \min_{a} \sum_{t=1}^T \ell_t(a)
$$



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

- $O(\sqrt{T})$ regret for convex losses,
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

??? success "Solution to Exercise 1"
    **(a)** The best asset in hindsight achieved a cumulative return of $\max\{12\%, 8\%, -3\%, 5\%, 15\%\} = 15\%$ (Asset 5). The Hedge algorithm achieved 10%. The static regret is:

    $$
    R_T = 15\% - 10\% = 5\%
    $$

    In absolute terms, the algorithm underperformed the best single asset by 5 percentage points over the year.

    **(b)** The theoretical bound is $R_T \le \sqrt{T \ln K / 2}$ where $T = 252$ and $K = 5$, but this is in units where per-period losses lie in $[0,1]$. Daily returns are in $[-3\%, 3\%]$, so we rescale to $[0,1]$ by the transformation $\tilde{\ell}_t = (\ell_t + 0.03)/0.06$, which maps $[-3\%, 3\%]$ to $[0,1]$. The range of the rescaled loss is 1, and the regret bound in rescaled units is:

    $$
    \tilde{R}_T \le \sqrt{\frac{252 \times \ln 5}{2}} = \sqrt{\frac{252 \times 1.6094}{2}} = \sqrt{202.8} \approx 14.24
    $$

    Converting back to return units by multiplying by the range $0.06$:

    $$
    R_T^{\text{bound}} \le 14.24 \times 0.06 \approx 0.855 = 85.5\%
    $$

    The actual regret of 5% is far below the theoretical worst-case bound of 85.5%. This is typical: the worst-case bound is achieved only by an adversary specifically designed to maximize regret, while real market returns are far more benign.

    **(c)** The average per-period regret is $R_T / T$. If $R_T = O(\sqrt{T})$, then:

    $$
    \frac{R_T}{T} = O\!\left(\frac{\sqrt{T}}{T}\right) = O\!\left(\frac{1}{\sqrt{T}}\right) \to 0 \text{ as } T \to \infty
    $$

    This means the algorithm's **average performance converges** to that of the best fixed strategy. Over long horizons, the cost of not knowing the best strategy in advance becomes negligible on a per-period basis. After 252 days, $1/\sqrt{252} \approx 0.063$; after 2520 days (10 years), $1/\sqrt{2520} \approx 0.020$. The algorithm becomes increasingly competitive over time.

---

**Exercise 2.** Define static and dynamic regret precisely. Static regret compares to the best fixed action: $R_T^{\text{static}} = \sum_{t=1}^T \ell_t(a_t) - \min_a \sum_{t=1}^T \ell_t(a)$. Dynamic regret compares to a time-varying benchmark: $R_T^{\text{dynamic}} = \sum_{t=1}^T \ell_t(a_t) - \sum_{t=1}^T \ell_t(a_t^*)$ where $a_t^* = \arg\min_a \ell_t(a)$. (a) Show that dynamic regret is always at least as large as static regret. (b) Why is $O(\sqrt{T})$ dynamic regret generally impossible without assumptions on the variation of $a_t^*$? (c) In a financial context, argue that dynamic regret is the more relevant measure for portfolio management in regime-switching markets, but static regret is more achievable.

??? success "Solution to Exercise 2"
    **(a)** Dynamic regret is at least as large as static regret because the dynamic benchmark is always at least as good as the static one. Formally:

    $$
    \sum_{t=1}^T \ell_t(a_t^*) \le \min_a \sum_{t=1}^T \ell_t(a)
    $$

    Wait -- this inequality goes the wrong way. Let us be precise. We have $a_t^* = \arg\min_a \ell_t(a)$, so $\ell_t(a_t^*) \le \ell_t(a)$ for all $a$ and all $t$. Summing over $t$:

    $$
    \sum_{t=1}^T \ell_t(a_t^*) \le \sum_{t=1}^T \ell_t(a) \quad \text{for all } a
    $$

    In particular, for $a^* = \arg\min_a \sum_{t=1}^T \ell_t(a)$:

    $$
    \sum_{t=1}^T \ell_t(a_t^*) \le \sum_{t=1}^T \ell_t(a^*)
    $$

    Therefore:

    $$
    R_T^{\text{dynamic}} = \sum_{t=1}^T \ell_t(a_t) - \sum_{t=1}^T \ell_t(a_t^*) \ge \sum_{t=1}^T \ell_t(a_t) - \sum_{t=1}^T \ell_t(a^*) = R_T^{\text{static}}
    $$

    **(b)** $O(\sqrt{T})$ dynamic regret is generally impossible without assumptions on the variation of $a_t^*$ because the dynamic benchmark can be arbitrarily hard to track. Consider losses $\ell_t(a) = (a - a_t^*)^2$ where $a_t^*$ alternates between 0 and 1 every period. The dynamic benchmark achieves zero loss, but any algorithm must pay a switching cost. If $a_t^*$ changes $T$ times, the total tracking error is at least $\Omega(T)$, giving linear regret.

    More formally, the dynamic regret generally satisfies:

    $$
    R_T^{\text{dynamic}} = \Omega\!\left(\sqrt{T(1 + P_T)}\right)
    $$

    where $P_T = \sum_{t=1}^{T-1} \|a_{t+1}^* - a_t^*\|$ is the **path length** of the comparator sequence. Without bounding $P_T$, the regret can be $\Omega(T)$.

    **(c)** In financial contexts:

    - **Dynamic regret** is more relevant for portfolio management in regime-switching markets because the best strategy changes over time (e.g., momentum works in trends, mean-reversion works in range-bound markets). A manager should be compared to the best strategy at each point in time, not the best fixed strategy over the whole period.
    - **Static regret** is more achievable because it sets a weaker benchmark. The $O(\sqrt{T})$ guarantee is attainable by standard algorithms without additional assumptions.
    - In practice, dynamic regret bounds require assumptions such as bounded path length $P_T$ or bounded total variation $V_T$, which may or may not hold. The practical approach is to target static regret guarantees while using adaptive methods (e.g., restarting, variable learning rates) that empirically track changing environments.

---

**Exercise 3.** For online gradient descent with convex losses and step size $\eta_t = 1/\sqrt{t}$, the regret bound is

$$
R_T \le \frac{D^2}{2\eta_T} + \frac{1}{2}\sum_{t=1}^T \eta_t \|\nabla \ell_t(a_t)\|^2
$$

where $D$ is the diameter of the decision set. (a) Show that with $\eta_t = D/(G\sqrt{T})$ (constant step size, $G$ is the gradient bound), this gives $R_T \le DG\sqrt{T}$. (b) For strongly convex losses with parameter $\mu > 0$, the regret improves to $O(\frac{G^2}{\mu}\ln T)$. Explain intuitively why strong convexity helps: the loss landscape has more curvature, making it easier to identify the optimum. (c) In portfolio optimization, when is the loss function strongly convex (hint: consider variance-penalized returns)?

??? success "Solution to Exercise 3"
    **(a)** With constant step size $\eta_t = \eta = D/(G\sqrt{T})$ where $D$ is the diameter and $G = \max_t \|\nabla \ell_t(a_t)\|$:

    $$
    R_T \le \frac{D^2}{2\eta} + \frac{\eta}{2}\sum_{t=1}^T G^2 = \frac{D^2}{2 \cdot D/(G\sqrt{T})} + \frac{D}{2G\sqrt{T}} \cdot T G^2
    $$

    $$
    = \frac{DG\sqrt{T}}{2} + \frac{DG\sqrt{T}}{2} = DG\sqrt{T}
    $$

    **(b)** For strongly convex losses with parameter $\mu > 0$ (meaning $\ell_t(a) \ge \ell_t(a_t) + \nabla \ell_t(a_t)^\top(a - a_t) + \frac{\mu}{2}\|a - a_t\|^2$), using step size $\eta_t = 1/(\mu t)$:

    $$
    R_T \le \frac{G^2}{2\mu}\sum_{t=1}^T \frac{1}{t} = \frac{G^2}{2\mu}(1 + \ln T) = O\!\left(\frac{G^2}{\mu}\ln T\right)
    $$

    **Intuition**: Strong convexity means the loss function curves sharply around its minimum. Each gradient step provides more information about the location of $a^*$ than in the merely convex case. Specifically:

    - The loss grows quadratically away from the optimum, so being "close" in function value means being close in parameter space.
    - The gradient $\nabla \ell_t(a_t)$ is more informative: it not only points toward the optimum but its magnitude is proportional to the distance from the optimum.
    - This allows the step size to decrease as $1/t$ (faster than $1/\sqrt{t}$), since each observation is more informative, leading to $O(\ln T)$ instead of $O(\sqrt{T})$ regret.

    **(c)** In portfolio optimization, the loss function is strongly convex when variance penalization is included. Consider the mean-variance loss:

    $$
    \ell_t(w) = -r_t^\top w + \frac{\gamma}{2} w^\top \Sigma w
    $$

    The Hessian is $\nabla^2 \ell_t(w) = \gamma \Sigma$. If $\Sigma \succ 0$ (positive definite covariance matrix), then $\ell_t$ is $\gamma \lambda_{\min}(\Sigma)$-strongly convex, where $\lambda_{\min}(\Sigma)$ is the smallest eigenvalue of $\Sigma$. In this case:

    $$
    \mu = \gamma \lambda_{\min}(\Sigma) > 0
    $$

    This gives $O(\ln T)$ regret for online mean-variance portfolio optimization, a dramatic improvement over the $O(\sqrt{T})$ rate for general convex losses. The financial intuition is that the variance penalty prevents the optimizer from making extreme bets, making the learning problem easier.

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

??? success "Solution to Exercise 4"
    **(a)** The cumulative loss of each strategy:

    - Strategy A: $0.2 + 0.6 + 0.3 + 0.8 + 0.1 = 2.0$
    - Strategy B: $0.5 + 0.1 + 0.3 + 0.2 + 0.4 = 1.5$
    - Strategy C: $0.3 + 0.4 + 0.7 + 0.1 + 0.5 = 2.0$

    The best fixed strategy in hindsight is **Strategy B** with cumulative loss $1.5$.

    **(b)** Initialize with equal weights $w_i^{(0)} = 1/3$ for $i = A, B, C$. The learning rate is $\eta = \sqrt{2\ln 3 / 5} = \sqrt{2 \times 1.0986 / 5} = \sqrt{0.4394} \approx 0.6629$.

    **Period 1**: Losses: $\ell_A = 0.2, \ell_B = 0.5, \ell_C = 0.3$. Play $p^{(1)} = (1/3, 1/3, 1/3)$. Algorithm's loss: $\hat{\ell}_1 = (0.2 + 0.5 + 0.3)/3 = 0.3333$.

    Update weights: $w_A^{(1)} \propto \frac{1}{3}e^{-0.6629 \times 0.2} = \frac{1}{3} \times 0.8762 = 0.2921$, $w_B^{(1)} \propto \frac{1}{3}e^{-0.6629 \times 0.5} = \frac{1}{3} \times 0.7165 = 0.2388$, $w_C^{(1)} \propto \frac{1}{3}e^{-0.6629 \times 0.3} = \frac{1}{3} \times 0.8196 = 0.2732$.

    Normalizing: $Z = 0.2921 + 0.2388 + 0.2732 = 0.8041$. So $p^{(2)} = (0.3633, 0.2970, 0.3398)$.

    **Period 2**: Losses: $\ell_A = 0.6, \ell_B = 0.1, \ell_C = 0.4$. Algorithm's loss: $\hat{\ell}_2 = 0.3633 \times 0.6 + 0.2970 \times 0.1 + 0.3398 \times 0.4 = 0.2180 + 0.0297 + 0.1359 = 0.3836$.

    Update: $w_A^{(2)} \propto 0.3633 \times e^{-0.6629 \times 0.6} = 0.3633 \times 0.6721 = 0.2442$, $w_B^{(2)} \propto 0.2970 \times e^{-0.6629 \times 0.1} = 0.2970 \times 0.9358 = 0.2779$, $w_C^{(2)} \propto 0.3398 \times e^{-0.6629 \times 0.4} = 0.3398 \times 0.7672 = 0.2607$.

    Normalizing: $Z = 0.2442 + 0.2779 + 0.2607 = 0.7828$. So $p^{(3)} = (0.3120, 0.3550, 0.3330)$.

    **Period 3**: Losses: $\ell_A = 0.3, \ell_B = 0.3, \ell_C = 0.7$. Algorithm's loss: $\hat{\ell}_3 = 0.3120 \times 0.3 + 0.3550 \times 0.3 + 0.3330 \times 0.7 = 0.0936 + 0.1065 + 0.2331 = 0.4332$.

    Update: $w_A^{(3)} \propto 0.3120 \times e^{-0.6629 \times 0.3} = 0.3120 \times 0.8196 = 0.2557$, $w_B^{(3)} \propto 0.3550 \times e^{-0.6629 \times 0.3} = 0.3550 \times 0.8196 = 0.2910$, $w_C^{(3)} \propto 0.3330 \times e^{-0.6629 \times 0.7} = 0.3330 \times 0.6300 = 0.2098$.

    Normalizing: $Z = 0.2557 + 0.2910 + 0.2098 = 0.7565$. So $p^{(4)} = (0.3381, 0.3847, 0.2773)$.

    **Period 4**: Losses: $\ell_A = 0.8, \ell_B = 0.2, \ell_C = 0.1$. Algorithm's loss: $\hat{\ell}_4 = 0.3381 \times 0.8 + 0.3847 \times 0.2 + 0.2773 \times 0.1 = 0.2705 + 0.0769 + 0.0277 = 0.3751$.

    Update: $w_A^{(4)} \propto 0.3381 \times e^{-0.6629 \times 0.8} = 0.3381 \times 0.5892 = 0.1992$, $w_B^{(4)} \propto 0.3847 \times e^{-0.6629 \times 0.2} = 0.3847 \times 0.8762 = 0.3371$, $w_C^{(4)} \propto 0.2773 \times e^{-0.6629 \times 0.1} = 0.2773 \times 0.9358 = 0.2595$.

    Normalizing: $Z = 0.1992 + 0.3371 + 0.2595 = 0.7958$. So $p^{(5)} = (0.2503, 0.4236, 0.3261)$.

    **Period 5**: Losses: $\ell_A = 0.1, \ell_B = 0.4, \ell_C = 0.5$. Algorithm's loss: $\hat{\ell}_5 = 0.2503 \times 0.1 + 0.4236 \times 0.4 + 0.3261 \times 0.5 = 0.0250 + 0.1694 + 0.1631 = 0.3575$.

    **Cumulative algorithm loss**: $0.3333 + 0.3836 + 0.4332 + 0.3751 + 0.3575 = 1.8827$.

    **(c)** Actual regret: $1.8827 - 1.5 = 0.3827$.

    Theoretical bound: $\sqrt{T \ln K / 2} = \sqrt{5 \times \ln 3 / 2} = \sqrt{5 \times 1.0986 / 2} = \sqrt{2.7466} \approx 1.657$.

    The actual regret ($0.38$) is well below the theoretical bound ($1.66$), which is expected since the bound is a worst-case guarantee. The algorithm successfully tracked the best strategy (B) by shifting weight toward it over time.

---

**Exercise 5.** Explain the financial interpretation of sublinear regret. If $R_T = O(\sqrt{T})$, then the average per-period regret is $R_T / T = O(1/\sqrt{T})$. (a) For a daily trading strategy over 10 years ($T \approx 2520$), compute the per-period regret bound for $K = 20$ assets. (b) Argue that sublinear regret means the algorithm is "almost as good" as the best fixed strategy in the long run. (c) Discuss the limitation: the benchmark is the best *fixed* strategy, but in practice, managers change strategies over time. How does this relate to the distinction between static and dynamic regret? (d) If transaction costs of $c$ per trade are included, how does this modify the regret analysis?

??? success "Solution to Exercise 5"
    **(a)** For $T = 2520$ trading days and $K = 20$ assets, the regret bound is:

    $$
    R_T \le \sqrt{\frac{T \ln K}{2}} = \sqrt{\frac{2520 \times \ln 20}{2}} = \sqrt{\frac{2520 \times 2.9957}{2}} = \sqrt{3774.6} \approx 61.44
    $$

    In normalized loss units (losses in $[0,1]$), the per-period regret bound is:

    $$
    \frac{R_T}{T} \le \frac{61.44}{2520} \approx 0.0244
    $$

    If daily returns range over $[-5\%, 5\%]$ (range = 0.10), the per-period regret in return units is approximately $0.0244 \times 0.10 = 0.00244 = 0.244\%$ per day, or roughly $0.244\% \times 252 \approx 61.5\%$ annualized. This is a loose bound; actual regret is typically much smaller.

    **(b)** Sublinear regret $R_T = O(\sqrt{T})$ means:

    $$
    \frac{1}{T}\sum_{t=1}^T \ell_t(a_t) - \frac{1}{T}\min_a \sum_{t=1}^T \ell_t(a) = \frac{R_T}{T} = O\!\left(\frac{1}{\sqrt{T}}\right) \to 0
    $$

    The average per-period loss of the algorithm converges to the average per-period loss of the best fixed strategy. In the long run, the algorithm is "almost as good" as the best asset: no fixed asset can significantly outperform the algorithm in terms of average returns over long horizons. This is a strong guarantee obtained without any distributional assumptions.

    **(c)** The limitation is that the benchmark is the best **fixed** strategy -- the single asset that performed best over the entire horizon. In practice:

    - Managers change strategies over time (e.g., switching from momentum to value).
    - The best fixed strategy may not correspond to any realistic investment approach.
    - In regime-switching markets, no fixed strategy performs well throughout.

    This is the distinction between static regret (vs. best fixed action) and dynamic regret (vs. best time-varying action). Dynamic regret bounds require additional assumptions (bounded path length or variation) and are generally larger: $O(\sqrt{T(1 + P_T)})$ where $P_T$ is the path length of the comparator.

    **(d)** With transaction costs $c$ per trade, the regret analysis is modified:

    - The algorithm's total cost includes trading costs: $\sum_{t=1}^T \ell_t(a_t) + c \sum_{t=1}^T \|a_t - a_{t-1}\|_1$.
    - The benchmark's cost also includes the cost of the initial trade (but no ongoing costs for a fixed strategy): $\min_a \sum_{t=1}^T \ell_t(a) + c\|a - a_0\|_1$.
    - The effective regret bound increases because the algorithm's frequent rebalancing incurs more transaction costs than the fixed benchmark. If the algorithm changes weights by $O(1)$ each period, the total transaction cost is $O(cT)$, which is **linear** in $T$, potentially overwhelming the $O(\sqrt{T})$ regret from suboptimal decisions.
    - To control transaction costs, the learning rate $\eta$ must be reduced (fewer/smaller updates) or a penalty on turnover must be added to the objective, at the expense of slower learning and higher regret from the loss term.

---

**Exercise 6.** Policy regret arises in control settings where the learner's action at time $t$ affects future states. In optimal execution, the trader's order at time $t$ impacts the price at time $t+1$ through market impact. (a) Explain why standard (external) regret is insufficient for this setting: the comparison to the best fixed action ignores that a different sequence of actions would have produced different price paths. (b) Define policy regret as $R_T^{\text{policy}} = \sum_{t=1}^T \ell_t(a_1, \ldots, a_T) - \min_\pi \sum_{t=1}^T \ell_t(\pi)$ where $\pi$ is a policy. (c) Discuss why policy regret bounds are generally harder to obtain and require additional structural assumptions (e.g., bounded memory, Markov dynamics).

??? success "Solution to Exercise 6"
    **(a)** Standard (external) regret compares the algorithm's cumulative loss to the best fixed action: $R_T = \sum_{t=1}^T \ell_t(a_t) - \min_a \sum_{t=1}^T \ell_t(a)$. This comparison is **counterfactual but assumes the loss sequence is fixed**. In optimal execution with market impact:

    - If the trader had chosen a different action sequence $a_1', \ldots, a_T'$, the prices would have been different (because each order impacts future prices).
    - The loss $\ell_t$ at time $t$ is not a fixed function of $a_t$ alone but depends on the entire history of actions $a_1, \ldots, a_{t-1}$ through price impact.
    - Comparing to the "best fixed action" $a^*$ is meaningless because if the trader had actually played $a^*$ every period, the price sequence would have been completely different.

    For example, if a trader submits large buy orders, prices rise. Comparing against a benchmark that buys the same amount at the (now-inflated) prices is not the same as what would have happened if the benchmark strategy had been used from the start.

    **(b)** Policy regret accounts for this by comparing against the best **policy** (a mapping from states to actions):

    $$
    R_T^{\text{policy}} = \sum_{t=1}^T \ell_t(s_1, a_1, \ldots, s_T, a_T) - \min_\pi \sum_{t=1}^T \ell_t(s_1^\pi, \pi(s_1^\pi), \ldots, s_T^\pi, \pi(s_T^\pi))
    $$

    where $s_t^\pi$ is the state at time $t$ if policy $\pi$ had been followed from the beginning. The key difference is that the counterfactual loss accounts for the different state trajectories that would have resulted from the alternative policy.

    In optimal execution: a policy might be "sell $X/T$ shares per period" (TWAP) or "sell more when liquidity is high." The policy regret compares the actual execution against the best such policy, accounting for the fact that different execution schedules generate different price paths.

    **(c)** Policy regret bounds are harder to obtain because:

    - **Exponential blowup**: The space of policies is exponentially larger than the action space. A policy maps states to actions, and with $|\mathcal{S}|$ states and $|\mathcal{A}|$ actions, there are $|\mathcal{A}|^{|\mathcal{S}|}$ deterministic policies.
    - **Dependence on dynamics**: The state evolution depends on the actions (the system is controlled), so the loss function is no longer decomposable across time steps. Standard online learning analyses rely on the loss being a function of the current action only.
    - **Structural assumptions needed**: To obtain tractable bounds, one typically assumes:
        - *Bounded memory*: The state at time $t$ depends only on the last $m$ actions (not the full history).
        - *Markov dynamics*: The state transition $s_{t+1} = f(s_t, a_t, \omega_t)$ depends only on the current state and action.
        - *Mixing conditions*: The system's dependence on initial conditions decays geometrically, so past actions have diminishing influence.
    - Under these assumptions, bounds of the form $R_T^{\text{policy}} = \tilde{O}(\sqrt{T})$ can be obtained, but with larger constants and additional problem-dependent terms compared to standard regret.

---

**Exercise 7.** Lower bounds establish that certain regret rates are optimal. For the experts problem with $K$ experts and adversarial losses in $[0,1]$, the minimax regret is $\Theta(\sqrt{T \ln K})$. (a) Explain what "minimax" means here: it is the best achievable worst-case regret over all possible algorithms. (b) Verify that the Hedge algorithm is minimax optimal (up to constants). (c) For strongly convex losses, the minimax regret drops to $\Theta(\ln T)$. Provide a financial example where the loss function is naturally strongly convex. (d) Discuss the practical gap between worst-case bounds and typical-case performance: in most financial applications, actual regret is much smaller than the worst-case bound. Why?

??? success "Solution to Exercise 7"
    **(a)** "Minimax regret" is defined as:

    $$
    \inf_{\text{algorithm } \mathcal{A}} \sup_{\text{loss sequence } \ell_1, \ldots, \ell_T} R_T(\mathcal{A}, \ell_1, \ldots, \ell_T)
    $$

    - The **inner sup** (over loss sequences) computes the worst-case regret for a given algorithm: the adversary chooses the hardest possible loss sequence.
    - The **outer inf** (over algorithms) finds the algorithm with the smallest worst-case regret: the learner chooses the best possible strategy.
    - The minimax regret $\Theta(\sqrt{T \ln K})$ means that no algorithm can guarantee regret better than $c_1\sqrt{T \ln K}$ against all adversaries, and there exists an algorithm achieving regret at most $c_2\sqrt{T \ln K}$.

    **(b)** The Hedge algorithm achieves:

    $$
    R_T^{\text{Hedge}} \le \sqrt{\frac{T \ln K}{2}}
    $$

    The lower bound (proved via probabilistic arguments or information-theoretic methods) is:

    $$
    \inf_{\mathcal{A}} \sup_{\ell} R_T(\mathcal{A}) \ge c\sqrt{T \ln K}
    $$

    for a universal constant $c > 0$. Since Hedge's upper bound matches the lower bound up to a constant factor ($1/\sqrt{2}$ vs. $c$), Hedge is **minimax optimal** up to constants. This means no algorithm can significantly outperform Hedge in the worst case.

    **(c)** For strongly convex losses (strong convexity parameter $\mu > 0$), the minimax regret drops to $\Theta\!\left(\frac{G^2}{\mu}\ln T\right)$.

    **Financial example**: Mean-variance portfolio optimization with the loss:

    $$
    \ell_t(w) = -r_t^\top w + \frac{\gamma}{2}w^\top \Sigma w
    $$

    This has Hessian $\gamma \Sigma \succ 0$, giving strong convexity parameter $\mu = \gamma \lambda_{\min}(\Sigma) > 0$. The $O(\ln T)$ regret means that over $T = 2520$ days (10 years):

    $$
    R_T = O(\ln 2520) \approx O(7.8)
    $$

    This is a dramatic improvement over $O(\sqrt{2520}) \approx O(50)$ from the general convex case. The variance penalty makes the problem much easier to learn.

    Another example: risk-penalized optimal execution where the loss includes a quadratic penalty on inventory position.

    **(d)** The practical gap between worst-case bounds and typical-case performance arises because:

    - **Markets are not fully adversarial**: Returns have statistical structure (mean-reversion, momentum, factor structure) that a good algorithm can exploit. The worst case assumes an omniscient adversary, which is unrealistic.
    - **Smooth loss sequences**: In practice, successive losses are correlated (today's returns are related to yesterday's), which makes tracking easier. The worst case requires rapidly changing, adversarially chosen losses.
    - **Bounded variation**: Real markets have bounded total variation in return distributions (except during crises), which places them in the "easy" part of the adversarial spectrum.
    - **Effective dimension**: Even with many assets, the effective dimensionality (number of independent risk factors) is small, reducing the complexity of the learning problem below what $K$ or $d$ suggests.
    - **Hedging against the worst case is expensive**: The $\sqrt{T \ln K}$ bound is tight for the worst-case loss sequence, but this sequence rarely resembles anything seen in markets. Algorithms that are slightly suboptimal in the worst case but exploit statistical structure can perform much better in practice.
