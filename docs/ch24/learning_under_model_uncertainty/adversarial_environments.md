# Adversarial Environments


In **adversarial environments**, data-generating processes may react strategically to the learner’s actions, invalidating classical statistical assumptions.

---

## From stochastic to adversarial settings


Traditional learning assumes:

- i.i.d. or stationary data.

Adversarial learning assumes:

- worst-case or adaptive opponents,
- no probabilistic structure.

This provides strong performance guarantees.

---

## Online adversarial learning


Algorithms are designed to minimize regret (Hedge / multiplicative weights, online gradient descent, mirror descent) and perform well against any adversarial sequence. Recall (see [§ Regret Bounds](regret_bounds.md)) for the definition of regret and the $O(\sqrt{T \ln K})$ guarantee of Hedge.

---

## Financial relevance


Markets can behave adversarially:

- crowding effects,
- feedback from strategies,
- strategic counterparties.

Adversarial models capture these phenomena.

---

## Costs and conservatism


Adversarial guarantees are:

- pessimistic,
- often overly conservative,
- data-inefficient in benign environments.

Hybrid stochastic–adversarial models are often preferred.

---

## Key takeaways


- Adversarial models assume worst-case data.
- They provide strong guarantees.
- Conservatism is the price of robustness.

---

## Further reading


- Cesa-Bianchi & Lugosi, adversarial bandits.
- Hazan, online convex optimization.

---

## Exercises

**Exercise 1.** Consider the Hedge (multiplicative weights) algorithm for choosing among $K$ trading strategies. At each round $t$, the learner assigns weight $w_i^{(t)} = w_i^{(t-1)} \exp(-\eta \ell_i^{(t-1)})$ to strategy $i$, where $\ell_i^{(t)}$ is the loss of strategy $i$ at round $t$ and $\eta > 0$ is the learning rate. (a) Show that the regret after $T$ rounds satisfies $R_T \le \frac{\ln K}{\eta} + \frac{\eta T}{8}$ when losses are in $[0,1]$. (b) Optimize over $\eta$ to find that the optimal regret bound is $R_T \le \sqrt{\frac{T \ln K}{2}}$. (c) For $K = 10$ strategies over $T = 252$ trading days, compute the per-round average regret. Is this practically meaningful?

??? success "Solution to Exercise 1"
    **(a)** We analyze the Hedge algorithm's regret. Define $W_t = \sum_{i=1}^K w_i^{(t)}$ as the total weight at round $t$, with $W_0 = K$ (starting from uniform weights $w_i^{(0)} = 1$). The update $w_i^{(t)} = w_i^{(t-1)} e^{-\eta \ell_i^{(t-1)}}$ gives:

    $$
    W_t = \sum_{i=1}^K w_i^{(t-1)} e^{-\eta \ell_i^{(t-1)}}
    $$

    **Upper bound on $\ln W_T$:** The algorithm plays the mixed strategy $p_i^{(t)} = w_i^{(t)} / W_t$, incurring expected loss $\hat{\ell}_t = \sum_i p_i^{(t)} \ell_i^{(t)}$. Then:

    $$
    \frac{W_{t+1}}{W_t} = \sum_i p_i^{(t)} e^{-\eta \ell_i^{(t)}}
    $$

    Using the inequality $e^{-\eta x} \le 1 - \eta x + \frac{\eta^2 x^2}{2} \le 1 - \eta x + \frac{\eta^2}{8}$ for $x \in [0,1]$ (since $x^2 \le x \le 1$ and the tighter Hoeffding-type bound gives the $1/8$ constant):

    $$
    \frac{W_{t+1}}{W_t} \le 1 - \eta \hat{\ell}_t + \frac{\eta^2}{8} \le \exp\!\left(-\eta \hat{\ell}_t + \frac{\eta^2}{8}\right)
    $$

    Telescoping over $t = 0, \ldots, T-1$:

    $$
    \ln W_T \le \ln K - \eta \sum_{t=1}^T \hat{\ell}_t + \frac{\eta^2 T}{8}
    $$

    **Lower bound on $\ln W_T$:** For any expert $j$: $W_T \ge w_j^{(T)} = e^{-\eta \sum_{t=1}^T \ell_j^{(t)}}$, so $\ln W_T \ge -\eta \sum_{t=1}^T \ell_j^{(t)}$.

    Combining and rearranging:

    $$
    \sum_{t=1}^T \hat{\ell}_t - \sum_{t=1}^T \ell_j^{(t)} \le \frac{\ln K}{\eta} + \frac{\eta T}{8}
    $$

    Since this holds for all $j$, including the best expert in hindsight:

    $$
    R_T \le \frac{\ln K}{\eta} + \frac{\eta T}{8}
    $$

    **(b)** To optimize over $\eta$, set $\frac{d}{d\eta}\left(\frac{\ln K}{\eta} + \frac{\eta T}{8}\right) = 0$:

    $$
    -\frac{\ln K}{\eta^2} + \frac{T}{8} = 0 \implies \eta^* = \sqrt{\frac{8 \ln K}{T}}
    $$

    Substituting back:

    $$
    R_T \le \frac{\ln K}{\sqrt{8\ln K / T}} + \frac{T}{8}\sqrt{\frac{8\ln K}{T}} = \sqrt{\frac{T \ln K}{8}} \cdot 2 = \sqrt{\frac{T \ln K}{2}}
    $$

    **(c)** For $K = 10$ and $T = 252$:

    $$
    R_T \le \sqrt{\frac{252 \times \ln 10}{2}} = \sqrt{\frac{252 \times 2.3026}{2}} = \sqrt{290.1} \approx 17.03
    $$

    The per-round average regret is:

    $$
    \frac{R_T}{T} \le \frac{17.03}{252} \approx 0.0676
    $$

    Since losses are in $[0,1]$, this means the algorithm's average daily loss is at most about 6.8% worse than the best strategy's average daily loss (in the normalized loss scale). If daily returns are on the order of a few percent, the actual dollar regret per day is quite small. Moreover, this is a **worst-case** bound; typical-case regret is much smaller. With 252 trading days, the guarantee is practically meaningful: the algorithm is competitive with the best of 10 strategies, paying only a modest cost for not knowing in advance which strategy would be best.

---

**Exercise 2.** In online gradient descent, a portfolio manager selects weights $w_t \in \Delta_n$ (the simplex) at each step, then suffers loss $\ell_t(w_t)$. The update rule is $w_{t+1} = \Pi_{\Delta_n}(w_t - \eta \nabla \ell_t(w_t))$, where $\Pi_{\Delta_n}$ is the projection onto the simplex. (a) Explain why the projection step is necessary for portfolio optimization. (b) If $\ell_t(w) = -r_t^\top w$ (negative portfolio return), what is the gradient $\nabla \ell_t$? (c) Derive the regret bound $R_T \le \frac{\|w_1 - w^*\|^2}{2\eta} + \frac{\eta}{2}\sum_{t=1}^T \|\nabla \ell_t\|^2$ and discuss how the choice of $\eta$ trades off tracking the best fixed portfolio against stability.

??? success "Solution to Exercise 2"
    **(a)** The projection $\Pi_{\Delta_n}$ onto the simplex $\Delta_n = \{w \in \mathbb{R}^n : w_i \ge 0, \sum_i w_i = 1\}$ is necessary because:

    - Portfolio weights must be non-negative (no short selling in the constrained case) and sum to 1 (fully invested).
    - The gradient step $w_t - \eta \nabla \ell_t(w_t)$ generally violates these constraints: weights may become negative or fail to sum to 1.
    - The projection finds the closest feasible point: $\Pi_{\Delta_n}(z) = \arg\min_{w \in \Delta_n} \|w - z\|^2$, ensuring the portfolio remains valid.

    **(b)** For the loss $\ell_t(w) = -r_t^\top w$ (negative of portfolio return, since we minimize loss which corresponds to maximizing return):

    $$
    \nabla \ell_t(w) = -r_t
    $$

    The gradient is simply the negative return vector, which does not depend on $w$. The update becomes:

    $$
    w_{t+1} = \Pi_{\Delta_n}(w_t + \eta r_t)
    $$

    This is intuitive: assets with high returns $r_{t,i}$ get their weights increased, and the projection then renormalizes to maintain a valid portfolio.

    **(c)** The standard OGD regret analysis proceeds via a telescoping argument. For any comparator $w^* \in \Delta_n$:

    $$
    \|w_{t+1} - w^*\|^2 = \|\Pi_{\Delta_n}(w_t - \eta \nabla \ell_t) - w^*\|^2 \le \|w_t - \eta \nabla \ell_t - w^*\|^2
    $$

    where the inequality uses the non-expansiveness of projection. Expanding:

    $$
    \|w_t - \eta \nabla \ell_t - w^*\|^2 = \|w_t - w^*\|^2 - 2\eta \nabla \ell_t^\top (w_t - w^*) + \eta^2 \|\nabla \ell_t\|^2
    $$

    By convexity, $\ell_t(w_t) - \ell_t(w^*) \le \nabla \ell_t^\top (w_t - w^*)$. Rearranging and summing over $t$:

    $$
    \sum_{t=1}^T [\ell_t(w_t) - \ell_t(w^*)] \le \frac{\|w_1 - w^*\|^2}{2\eta} + \frac{\eta}{2}\sum_{t=1}^T \|\nabla \ell_t\|^2
    $$

    This is the regret bound $R_T \le \frac{D^2}{2\eta} + \frac{\eta}{2}\sum_{t=1}^T G_t^2$ where $D = \|w_1 - w^*\|$ and $G_t = \|\nabla \ell_t\|$.

    **Tradeoff in choosing $\eta$:**

    - **Small $\eta$** (conservative): The first term $D^2/(2\eta)$ is large (slow convergence to the best portfolio) but the second term $\frac{\eta}{2}\sum G_t^2$ is small (stable updates, less sensitivity to noisy gradients).
    - **Large $\eta$** (aggressive): Fast convergence toward good portfolios but large variance from noisy gradient updates.
    - **Optimal $\eta = D / (G\sqrt{T})$** (where $G = \max_t \|r_t\|$): Balances both terms to give $R_T \le DG\sqrt{T}$.

---

**Exercise 3.** Explain how crowding effects in financial markets create an adversarial environment. Suppose $N$ momentum traders simultaneously buy assets with positive recent returns. As more traders adopt the strategy, the returns from momentum diminish. (a) Model this as a game where each trader's loss depends on the aggregate strategy of all other traders. (b) Explain why i.i.d. assumptions about returns are violated when a large fraction of the market uses the same strategy. (c) Discuss how adversarial regret bounds provide guarantees even when other market participants react to the learner's trades.

??? success "Solution to Exercise 3"
    **(a)** Consider $N$ momentum traders, each choosing position size $q_i$ in assets with positive recent returns. The aggregate demand is $Q = \sum_{i=1}^N q_i$. The price impact model gives the execution price:

    $$
    P_{\text{exec}} = P_0 + \lambda Q
    $$

    where $\lambda > 0$ is the price impact parameter. Each trader's realized return depends on the total demand:

    $$
    r_i(q_i, Q_{-i}) = \frac{P_{\text{future}} - P_0 - \lambda(q_i + Q_{-i})}{P_0 + \lambda(q_i + Q_{-i})} \cdot q_i
    $$

    where $Q_{-i} = \sum_{j \ne i} q_j$. This is a **congestion game**: each trader's payoff depends on the aggregate action of all others. As more traders crowd into momentum, the entry price is pushed up and the expected profit per trader shrinks:

    $$
    \frac{\partial r_i}{\partial Q_{-i}} < 0
    $$

    **(b)** The i.i.d. assumption on returns fails because:

    - Past returns attract momentum capital, which pushes prices up, generating further momentum (positive feedback loop), followed by eventual reversal when the strategy becomes too crowded.
    - The return distribution at time $t+1$ depends on the aggregate strategy at time $t$: $P_{t+1} = f(P_t, Q_t, \ldots)$. Returns are not drawn from a fixed distribution but from one that is endogenously determined by market participants.
    - Correlation structures change: during crowding episodes, momentum assets become correlated not because of fundamentals but because of common ownership. This is the opposite of the i.i.d. assumption.

    **(c)** Adversarial regret bounds (such as the $O(\sqrt{T \ln K})$ bound for Hedge) provide guarantees against **any** sequence of losses, including sequences generated by strategic opponents. This means:

    - Even if other traders observe and react to the learner's strategy, the learner's regret is bounded.
    - The guarantees hold without any distributional assumptions on returns.
    - The learner can compete with the best fixed strategy in hindsight, regardless of how other market participants behave.

    This is particularly valuable in crowded trades where the "environment" (other traders) is genuinely adversarial: they exploit the same signals, creating feedback effects that are not captured by stochastic models.

---

**Exercise 4.** Compare the performance of an adversarial algorithm (Hedge) with a stochastic algorithm (sample mean estimator) in two scenarios: (a) returns are genuinely i.i.d. Gaussian, and (b) returns are generated by an adversary who observes the learner's past actions. Show that the stochastic algorithm achieves $O(1/\sqrt{T})$ convergence in scenario (a) but can suffer linear regret in scenario (b), while the adversarial algorithm achieves $O(\sqrt{T/\ln K})$ regret in both. Under what market conditions (liquid vs illiquid, small vs large trader) is the adversarial guarantee worth its conservatism cost?

??? success "Solution to Exercise 4"
    **(a) Scenario: i.i.d. Gaussian returns.** Let returns be $r_t \sim \mathcal{N}(\mu, \sigma^2)$ i.i.d. The sample mean estimator $\hat{\mu}_T = \frac{1}{T}\sum_{t=1}^T r_t$ converges to $\mu$ at rate $O(1/\sqrt{T})$:

    $$
    |\hat{\mu}_T - \mu| = O_p\left(\frac{\sigma}{\sqrt{T}}\right)
    $$

    The cumulative regret of using $\hat{\mu}_t$ to select strategies is $O(\sqrt{T})$ (since the per-period suboptimality is $O(1/\sqrt{t})$ and $\sum_{t=1}^T 1/\sqrt{t} = O(\sqrt{T})$).

    The Hedge algorithm achieves regret $O(\sqrt{T \ln K})$, which is slightly worse by the $\sqrt{\ln K}$ factor. Both are sublinear, so both work.

    **(b) Scenario: adversarial returns.** An adversary who observes the learner's past actions can exploit the sample mean estimator. For example, if the learner computes $\hat{\mu}_t$ and invests in the asset with highest estimated mean, the adversary can:

    - Make that asset perform poorly in the next period.
    - Systematically mislead the learner by alternating which asset has the highest sample mean.

    This can produce **linear regret** $R_T = \Omega(T)$ for the sample mean estimator, because the estimator's predictions are predictably wrong from the adversary's perspective.

    The Hedge algorithm, by contrast, still achieves $R_T = O(\sqrt{T \ln K})$ because its guarantee holds for **any** loss sequence, including adversarially chosen ones.

    **When is the adversarial guarantee worth the conservatism cost?**

    - **Worth it**: Illiquid markets where the trader's actions move prices (adversarial feedback); markets with informed counterparties; crowded strategy environments; regime-switching markets.
    - **Not worth it**: Highly liquid markets where the trader is small (no price impact, no adversarial feedback); stable statistical environments where returns are approximately i.i.d.; when the $\sqrt{\ln K}$ cost is large relative to available alpha.

---

**Exercise 5.** A market maker must set bid-ask spreads in a market where some counterparties may be informed traders (adversaries). The market maker uses an online learning algorithm to adaptively adjust spreads. (a) Formulate this as an adversarial online learning problem where the loss at time $t$ depends on whether the counterparty is informed. (b) Explain why the Glosten-Milgrom adverse selection model can be viewed as a special case of adversarial learning. (c) Discuss the tradeoff: wider spreads protect against adversarial counterparties but lose flow from uninformed traders. How does this relate to the conservatism of worst-case bounds?

??? success "Solution to Exercise 5"
    **(a)** Formulate the market maker's problem as adversarial online learning:

    - **Actions**: At each time $t$, the market maker chooses a bid-ask spread $s_t \in [s_{\min}, s_{\max}]$ (or more generally, bid and ask prices $(b_t, a_t)$).
    - **Adversary**: Nature selects whether the counterparty is informed (probability $\alpha$) or uninformed. An informed trader trades in the direction of the true value, causing the market maker to lose money. An uninformed trader trades randomly, allowing the market maker to earn the spread.
    - **Loss function**: At time $t$, if the spread is $s_t$ and the counterparty is informed with true value $V_t$:

    $$
    \ell_t(s_t) = \begin{cases} \alpha(V_t - a_t) + (1-\alpha) s_t / 2 & \text{(buy order)} \\ \alpha(b_t - V_t) + (1-\alpha) s_t / 2 & \text{(sell order)} \end{cases}
    $$

    The loss depends on the (unknown) type of counterparty, making this adversarial.

    **(b)** The **Glosten-Milgrom model** can be viewed as a Bayesian version of this adversarial learning problem:

    - The market maker maintains a belief $\mu_t$ about the asset value.
    - Bid and ask prices are set as conditional expectations: $a_t = \mathbb{E}[V \mid \text{buy}]$ and $b_t = \mathbb{E}[V \mid \text{sell}]$.
    - Each trade updates the belief (learning from order flow).
    - The spread compensates for adverse selection: $a_t - b_t > 0$ because the market maker expects to lose on average to informed traders and needs the spread revenue from uninformed traders.

    In the adversarial learning framework, Glosten-Milgrom is a special case where the adversary's strategy (the proportion of informed traders and their information) is modeled parametrically, and the market maker uses Bayesian updating instead of a worst-case algorithm.

    **(c)** The tradeoff is:

    - **Wider spreads**: Protect against informed (adversarial) counterparties. The market maker loses less per informed trade. However, wider spreads repel uninformed flow, reducing trading volume and revenue from the spread.
    - **Narrower spreads**: Attract more uninformed flow and earn more per uninformed trade. But the market maker is more exposed to adverse selection losses.

    This mirrors the conservatism of worst-case bounds: the adversarial algorithm (wide spreads) guarantees bounded losses against any counterparty mix, but underperforms when most counterparties are uninformed. The stochastic algorithm (narrow spreads calibrated to the estimated $\alpha$) performs well when $\alpha$ is correctly estimated but fails badly if informed trading surges unexpectedly.

    In practice, market makers use adaptive algorithms that widen spreads when adverse selection signals are detected (large orders, unusual timing, order flow imbalance) and narrow spreads in calm conditions.

---

**Exercise 6.** Mirror descent generalizes online gradient descent by using a Bregman divergence $D_\psi(w, w_t)$ instead of the Euclidean distance. With the negative entropy $\psi(w) = \sum_i w_i \ln w_i$, mirror descent on the simplex reduces to the Hedge algorithm. (a) Write the mirror descent update explicitly for this choice of $\psi$. (b) Explain why the KL divergence is more natural than Euclidean distance for portfolio weights on the simplex. (c) For a portfolio of 100 assets over $T = 1000$ days, compare the regret bounds of Euclidean online gradient descent ($O(\sqrt{n T})$) with entropic mirror descent ($O(\sqrt{T \ln n})$). Which is dramatically better for large $n$?

??? success "Solution to Exercise 6"
    **(a)** Mirror descent with Bregman divergence $D_\psi$ performs the update:

    $$
    w_{t+1} = \arg\min_{w \in \Delta_n} \left\{\eta \langle \nabla \ell_t(w_t), w \rangle + D_\psi(w, w_t)\right\}
    $$

    For $\psi(w) = \sum_i w_i \ln w_i$ (negative entropy), the Bregman divergence is the KL divergence:

    $$
    D_\psi(w, w_t) = \sum_i w_i \ln\frac{w_i}{w_{t,i}}
    $$

    The KKT conditions for the constrained minimization over the simplex yield:

    $$
    w_{t+1,i} = \frac{w_{t,i} \exp(-\eta \nabla_i \ell_t(w_t))}{\sum_j w_{t,j} \exp(-\eta \nabla_j \ell_t(w_t))}
    $$

    This is precisely the **Hedge (multiplicative weights) update**: multiply each weight by $\exp(-\eta \nabla_i \ell_t)$ and renormalize.

    **(b)** The KL divergence is more natural than Euclidean distance for portfolio weights on the simplex because:

    - **Scale invariance**: KL divergence measures relative changes in weights, which is appropriate since portfolio performance depends on ratios of allocations, not absolute differences.
    - **Boundary behavior**: The KL divergence $D_\psi(w, w_t) \to \infty$ as any $w_i \to 0$ while $w_{t,i} > 0$, which naturally keeps weights positive without explicit constraints. Euclidean distance does not penalize approaching the boundary.
    - **Dimension dependence**: The "diameter" of the simplex under KL divergence is $\ln n$ (the maximum KL divergence between any two distributions on $n$ points), whereas the Euclidean diameter is $\sqrt{2}$. This $\ln n$ dependence leads to better regret bounds in high dimensions.
    - **Multiplicative updates**: KL-based mirror descent produces multiplicative weight updates, which are natural for proportional allocations.

    **(c)** For $n = 100$ assets and $T = 1000$ days:

    - **Euclidean OGD regret**: $O(\sqrt{nT}) = O(\sqrt{100 \times 1000}) = O(\sqrt{100000}) \approx O(316)$
    - **Entropic mirror descent regret**: $O(\sqrt{T \ln n}) = O(\sqrt{1000 \times \ln 100}) = O(\sqrt{1000 \times 4.605}) = O(\sqrt{4605}) \approx O(68)$

    The entropic mirror descent bound is roughly **4.7 times better**. The ratio $\sqrt{n / \ln n} = \sqrt{100 / 4.605} \approx 4.66$ grows with $n$:

    | $n$ | $\sqrt{n}$ | $\sqrt{\ln n}$ | Ratio |
    |-----|-----------|----------------|-------|
    | 10 | 3.16 | 1.52 | 2.1 |
    | 100 | 10 | 2.15 | 4.7 |
    | 1000 | 31.6 | 2.63 | 12.0 |

    For large $n$ (many assets), entropic mirror descent is **dramatically better** because its regret depends only logarithmically on the number of assets, whereas Euclidean OGD depends polynomially.

---

**Exercise 7.** A hybrid stochastic-adversarial model assumes that returns are drawn from a distribution $P_t$ that can change at each step, but the total variation $\sum_{t=1}^{T-1} \|P_{t+1} - P_t\|$ is bounded by some $V_T$. (a) Explain how this interpolates between the purely stochastic case ($V_T = 0$) and the fully adversarial case ($V_T$ unrestricted). (b) State how the optimal regret scales with both $T$ and $V_T$. (c) In financial markets, argue that $V_T$ is small during calm periods and large during crises. How would an adaptive algorithm (that does not know $V_T$ in advance) adjust its learning rate?

??? success "Solution to Exercise 7"
    **(a)** The total variation budget $V_T = \sum_{t=1}^{T-1} \|P_{t+1} - P_t\|$ controls the degree of non-stationarity:

    - **$V_T = 0$**: All distributions are identical, $P_1 = P_2 = \cdots = P_T$. This is the classical i.i.d. (purely stochastic) setting. Standard stochastic algorithms achieve optimal rates.
    - **$V_T$ unrestricted** (no bound on variation): The distributions can change arbitrarily from one step to the next. This is the fully adversarial setting where no distributional assumptions hold. Only adversarial algorithms with worst-case guarantees are valid.
    - **$0 < V_T < \infty$**: An intermediate regime. The environment is non-stationary but not fully adversarial. The total amount of distributional change is bounded, allowing algorithms to exploit some statistical structure while remaining robust to drift.

    **(b)** The optimal dynamic regret for this setting scales as:

    $$
    R_T^{\text{dynamic}} = O\!\left(T^{1/3} V_T^{1/3} + \sqrt{T \ln K}\right)
    $$

    For the specific case of tracking the best expert with variation $V_T$:

    - When $V_T = 0$: the bound reduces to $O(\sqrt{T \ln K})$, matching the static stochastic rate.
    - When $V_T = \Theta(T)$ (fully adversarial): the bound becomes $O(T^{2/3} (\ln K)^{1/3})$ or $O(\sqrt{T \ln K})$, whichever dominates, consistent with standard adversarial bounds.
    - The $T^{1/3} V_T^{1/3}$ term reflects the cost of non-stationarity: the algorithm must balance responsiveness (small learning rate suffers from staleness) against stability (large learning rate suffers from noise).

    **(c)** In financial markets:

    - **Calm periods** (bull markets, low VIX): Return distributions change slowly. $V_T$ over a quarter might be small (e.g., means and volatilities shift by small amounts). Algorithms can use longer lookback windows and smaller learning rates.
    - **Crisis periods** (2008, COVID crash, etc.): Return distributions shift dramatically -- volatility spikes, correlations go to 1, mean returns change sign. $V_T$ over the same horizon is very large.

    An **adaptive algorithm** that does not know $V_T$ in advance can adjust its learning rate by:

    - **Monitoring realized variation**: Track $\hat{V}_t = \sum_{s=1}^{t-1} \|\hat{P}_{s+1} - \hat{P}_s\|$ using empirical distribution estimates. When $\hat{V}_t$ increases rapidly, increase the learning rate $\eta_t$.
    - **Adaptive learning rates**: Use algorithms like AdaGrad or parameter-free methods that automatically adjust $\eta_t$ based on observed gradient magnitudes. Large gradients (indicative of distribution shifts) trigger larger steps.
    - **Restarting strategies**: Maintain a meta-algorithm that runs multiple copies of a base algorithm with different start times. When a distribution shift is detected (via changepoint detection), the algorithm effectively "restarts" by upweighting recent copies.
    - **Discounted weights**: Instead of uniform averaging, use exponentially decaying weights $w_t \propto e^{-\beta(T-t)}$ that forget old observations. The decay rate $\beta$ can be adapted to the observed level of non-stationarity.

    The key principle is that the algorithm should be **more responsive** (higher effective learning rate, shorter memory) during volatile periods and **more stable** (lower learning rate, longer memory) during calm periods, without requiring advance knowledge of the regime.
