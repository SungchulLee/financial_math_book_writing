# Learning-Induced Instability


When many agents adapt their strategies using similar learning rules, **learning-induced instability** can arise, amplifying volatility and systemic risk.

---

## Adaptive strategies


Learning algorithms:

- update based on past performance,
- respond to observed market patterns,
- often share similar objectives.

Collective adaptation can destabilize markets.

---

## Feedback amplification


Recall (see [Market impact as endogeneity](endogenous_price_dynamics.md#market-impact-as-endogeneity)): trading-induced price moves feed back into strategies. Learning-induced effects include crowded trades, self-reinforcing trends, and sudden regime shifts, so small signals can be amplified through learning feedback.

---

## Examples


Examples include:

- volatility targeting strategies,
- trend-following algorithms,
- risk-parity portfolio adjustments.

These strategies can synchronize behavior.

---

## Risk management implications


Learning-induced instability implies:

- non-linear risk amplification,
- failure of diversification,
- need for macroprudential oversight.

Models assuming independent agents are insufficient.

---

## Key takeaways


- Adaptive learning can destabilize markets.
- Feedback loops amplify shocks.
- Stability requires diversity and constraints.

---

## Further reading


- Hommes, heterogeneous agent models.
- Danielsson et al., endogenous risk.

---

## Exercises

**Exercise 1.** Consider $N = 100$ volatility-targeting funds, each maintaining exposure $w_t = \sigma_{\text{target}} / \hat{\sigma}_t$ where $\hat{\sigma}_t$ is estimated using an exponentially weighted moving average with half-life of 20 days. After a 3% daily market drop, $\hat{\sigma}_t$ jumps from 15% to 20% annualized. (a) Compute the percentage reduction in each fund's equity exposure. (b) If each fund manages \$1 billion and the market has \$500 billion daily volume, estimate the total selling pressure as a fraction of daily volume. (c) Model the feedback: this selling pressure causes an additional price decline $\Delta S$, further increasing $\hat{\sigma}$, leading to more selling. Write the fixed-point equation and discuss whether a stable equilibrium exists.

??? success "Solution to Exercise 1"
    **(a)** Each fund's exposure before the shock is:

    $$
    w_{\text{before}} = \frac{\sigma_{\text{target}}}{\hat{\sigma}_{\text{before}}} = \frac{\sigma_{\text{target}}}{0.15}
    $$

    After the shock, $\hat{\sigma}$ jumps to 20%:

    $$
    w_{\text{after}} = \frac{\sigma_{\text{target}}}{0.20}
    $$

    The percentage reduction in equity exposure is:

    $$
    \frac{w_{\text{before}} - w_{\text{after}}}{w_{\text{before}}} = 1 - \frac{\hat{\sigma}_{\text{before}}}{\hat{\sigma}_{\text{after}}} = 1 - \frac{0.15}{0.20} = 0.25 = 25\%
    $$

    Each fund must reduce its equity exposure by 25%.

    **(b)** Each fund manages \$1 billion. Assuming the equity allocation was approximately $w_{\text{before}}$ fraction of AUM, the dollar selling per fund is:

    $$
    \text{Selling per fund} = 0.25 \times w_{\text{before}} \times \$1\text{B}
    $$

    If $\sigma_{\text{target}} = 10\%$ (a typical value), then $w_{\text{before}} = 10\%/15\% \approx 0.667$, so each fund sells $0.25 \times 0.667 \times \$1\text{B} \approx \$167\text{M}$. With $N = 100$ funds:

    $$
    \text{Total selling} = 100 \times \$167\text{M} = \$16.7\text{B}
    $$

    As a fraction of daily volume (\$500B):

    $$
    \frac{\$16.7\text{B}}{\$500\text{B}} \approx 3.3\%
    $$

    This is a substantial fraction of daily volume concentrated in a short time window (these rebalances typically execute within hours, not over the full day), implying significant price pressure.

    **(c)** Let $\sigma$ denote the post-shock estimated volatility. The selling pressure at volatility level $\sigma$ is:

    $$
    S(\sigma) = N \cdot W \cdot \sigma_{\text{target}} \cdot \left(\frac{1}{\sigma} - \frac{1}{\sigma_0}\right)
    $$

    where $\sigma_0 = 0.15$ is the pre-shock volatility. This selling pressure causes an additional price decline $\Delta p = \eta \cdot S(\sigma)$ (where $\eta$ is the price impact per dollar sold), which further increases estimated volatility by some function $\sigma = \sigma_{\text{shock}} + \phi(\Delta p)$.

    The fixed-point equation is:

    $$
    \sigma^* = \sigma_{\text{shock}} + \phi\!\left(\eta \cdot N \cdot W \cdot \sigma_{\text{target}} \cdot \left(\frac{1}{\sigma^*} - \frac{1}{\sigma_0}\right)\right)
    $$

    Define $F(\sigma) = \sigma_{\text{shock}} + \phi\!\left(\eta N W \sigma_{\text{target}} \left(\frac{1}{\sigma} - \frac{1}{\sigma_0}\right)\right)$. A stable equilibrium requires $F'(\sigma^*) < 1$.

    Since $S(\sigma)$ is decreasing in $\sigma$ (higher volatility means less additional selling needed), $F$ is a decreasing function for reasonable $\phi$. A stable equilibrium exists when the feedback sensitivity $\eta N W \sigma_{\text{target}} \cdot \phi'$ is moderate. If $N \cdot W$ (total AUM in vol-targeting strategies) becomes too large relative to market depth $1/\eta$, the slope $|F'|$ exceeds 1 near any candidate fixed point, and no stable equilibrium exists---implying a volatility spiral where selling and volatility increase without bound until external stabilization (e.g., circuit breakers, contrarian buyers) intervenes.

---

**Exercise 2.** Trend-following algorithms use signals such as $\text{Signal}_t = S_t - \bar{S}_t$ (price minus moving average) to generate buy/sell decisions. (a) If $M$ trend followers all buy when $\text{Signal}_t > 0$, their collective buying pushes the price further above the moving average, reinforcing the signal. Write a discrete-time model: $S_{t+1} = S_t + \epsilon_{t+1} + \alpha M \cdot \mathbf{1}(\text{Signal}_t > 0)$ where $\alpha$ is per-agent impact. (b) Show that this feedback can create artificial trends even when fundamentals are stationary ($\epsilon_t$ are i.i.d. with zero mean). (c) When does the trend reverse? Discuss the mechanism behind the sudden unwinding that occurs when the signal turns negative.

??? success "Solution to Exercise 2"
    **(a)** The discrete-time model with $M$ trend followers is:

    $$
    S_{t+1} = S_t + \epsilon_{t+1} + \alpha M \cdot \mathbf{1}(S_t - \bar{S}_t > 0)
    $$

    where $\bar{S}_t$ is the moving average (e.g., average of $S_{t-k+1}, \ldots, S_t$ over a window of length $k$) and $\alpha$ is the per-agent price impact. When $\text{Signal}_t = S_t - \bar{S}_t > 0$, all $M$ trend followers buy, pushing the price up by $\alpha M$. When the signal is negative, they sell (or abstain), contributing $-\alpha M$ (or 0) to the price change.

    The feedback mechanism is: buying pushes $S_{t+1}$ higher, which makes $S_{t+1} - \bar{S}_{t+1}$ more likely to remain positive (since the moving average adjusts slowly), which triggers more buying at $t+1$.

    **(b)** Even when fundamentals are stationary ($\epsilon_t$ i.i.d. with mean zero), artificial trends emerge through the following mechanism:

    Suppose at some time $t$, a sequence of positive $\epsilon$ shocks pushes $S_t$ above $\bar{S}_t$. Now $\text{Signal}_t > 0$, so the trend followers buy, adding $\alpha M$ to the next price:

    $$
    S_{t+1} = S_t + \epsilon_{t+1} + \alpha M
    $$

    The expected value of $S_{t+1}$ conditional on $\text{Signal}_t > 0$ is $S_t + \alpha M > S_t$, creating an upward bias. The moving average $\bar{S}_{t+1}$ adjusts upward, but slowly (it averages over a window). So $\text{Signal}_{t+1} = S_{t+1} - \bar{S}_{t+1}$ is likely still positive, perpetuating the buying.

    Formally, for the trend to persist, we need $\alpha M$ large enough relative to $\text{Var}(\epsilon)$ that the probability $\Pr(\text{Signal}_{t+1} > 0 \mid \text{Signal}_t > 0) > 1/2$. This creates positive autocorrelation in returns despite i.i.d. fundamentals---an artificial trend generated entirely by feedback trading.

    **(c)** The trend reverses through two mechanisms:

    1. **Moving average catch-up**: As the moving average $\bar{S}_t$ gradually rises toward the inflated price $S_t$, the signal $S_t - \bar{S}_t$ narrows. Eventually, a negative $\epsilon$ shock is sufficient to flip the signal to negative.
    2. **Signal flip cascade**: Once $\text{Signal}_t < 0$, all $M$ trend followers sell (or stop buying). The price drops by approximately $\alpha M$ in addition to any fundamental shock. This makes $\text{Signal}_{t+1}$ even more negative, triggering further selling.

    The unwinding is **sudden** because the transition from positive to negative signal triggers a discrete jump in aggregate demand (from $+\alpha M$ to $-\alpha M$, a swing of $2\alpha M$). The larger $M$ and $\alpha$ are, the more violent the reversal. This creates the characteristic pattern of artificial trends: slow buildup followed by rapid reversal, which resembles mini-bubbles and crashes even in the absence of fundamental news.

---

**Exercise 3.** Risk-parity portfolios allocate inversely to each asset's volatility: $w_i \propto 1/\sigma_i$. During a bond selloff, bond volatility increases, causing risk-parity funds to sell bonds. (a) If there are $N$ risk-parity funds each managing $W$ dollars, and bond volatility doubles, compute the approximate dollar amount of bonds sold. (b) Explain how this selling further increases bond volatility, creating a self-reinforcing cycle. (c) In August 2015, a synchronized unwinding of risk-parity trades contributed to market turbulence. Discuss why diversification across strategies fails when many funds use the same approach.

??? success "Solution to Exercise 3"
    **(a)** In a risk-parity portfolio, the weight on asset $i$ is proportional to the inverse of its volatility:

    $$
    w_i = \frac{1/\sigma_i}{\sum_j 1/\sigma_j}
    $$

    For a simplified two-asset case (equities and bonds), if bond volatility doubles from $\sigma_b$ to $2\sigma_b$, the bond weight changes from:

    $$
    w_b^{\text{before}} = \frac{1/\sigma_b}{1/\sigma_e + 1/\sigma_b} \quad \to \quad w_b^{\text{after}} = \frac{1/(2\sigma_b)}{1/\sigma_e + 1/(2\sigma_b)}
    $$

    The dollar amount of bonds sold per fund is approximately:

    $$
    \Delta_b = (w_b^{\text{before}} - w_b^{\text{after}}) \times W
    $$

    As a rough estimate, if bonds were 60% of the portfolio and the new allocation is 43% (from the doubling of volatility in a simplified two-asset setting), each fund sells $0.17 \times W$. With $N$ funds each managing $W$ dollars:

    $$
    \text{Total bond selling} \approx 0.17 \times N \times W
    $$

    **(b)** The self-reinforcing cycle operates as follows:

    1. **Initial bond selloff**: Some external shock (e.g., unexpected inflation data) causes bond prices to fall and bond volatility to increase.
    2. **Risk-parity rebalancing**: All $N$ funds reduce bond allocations, selling approximately $0.17NW$ in bonds.
    3. **Price impact**: The concentrated selling further depresses bond prices, increasing realized bond volatility beyond the initial shock.
    4. **Second round**: The higher volatility triggers further rebalancing, causing additional selling.
    5. **Amplification**: Each round of selling and volatility increase feeds the next, until either external buyers absorb the flow or the funds reach their minimum bond allocation.

    **(c)** The August 2015 episode illustrates why diversification across assets fails when many funds use the same strategy:

    - **Traditional diversification** assumes that fund behavior is independent: one fund's selling does not cause another fund's losses. Risk-parity allocations across different asset classes should provide diversification.
    - **Strategy crowding** invalidates this assumption. When many funds hold similar positions sized by the same volatility signals, they are effectively acting as a single large agent. An adverse shock triggers synchronized rebalancing, creating correlated selling pressure across all funds.
    - **Correlation breakdown**: During the unwind, assets that were previously uncorrelated become correlated because the same funds are selling all of them simultaneously. The diversification benefit evaporates precisely when it is needed most.
    - **The paradox**: Each individual fund's risk-parity allocation may be well-diversified, but the system of many funds using identical strategies is highly concentrated. Diversification across assets does not provide diversification across strategies.

---

**Exercise 4.** Model learning-induced instability using a simple feedback system. Let $p_t$ be the asset price, $s_t$ the aggregate strategy signal (e.g., momentum), and $\hat{\mu}_t$ the agents' estimated expected return. Agents learn: $\hat{\mu}_t = (1-\alpha)\hat{\mu}_{t-1} + \alpha r_{t-1}$ where $r_t = p_t / p_{t-1} - 1$. They trade proportionally: $v_t = \beta \hat{\mu}_t$. The price responds: $p_t = p_t^{\text{fundamental}} + \gamma v_t$. (a) Combine these equations to find the characteristic equation of the linear system. (b) Show that the system is stable when $\alpha \beta \gamma < 1$ and unstable otherwise. (c) Interpret each parameter: $\alpha$ (learning speed), $\beta$ (aggressiveness), $\gamma$ (market impact). Which parameter is most dangerous to increase?

??? success "Solution to Exercise 4"
    **(a)** We have three equations:

    - Learning: $\hat{\mu}_t = (1-\alpha)\hat{\mu}_{t-1} + \alpha r_{t-1}$
    - Trading: $v_t = \beta \hat{\mu}_t$
    - Price: $p_t = p_t^{\text{fund}} + \gamma v_t = p_t^{\text{fund}} + \gamma \beta \hat{\mu}_t$

    The return is $r_t = p_t / p_{t-1} - 1 \approx (p_t - p_{t-1})/p_{t-1}$. Assuming $p_t^{\text{fund}}$ is approximately constant (or changes slowly) and linearizing around a steady state, the return is approximately:

    $$
    r_t \approx \gamma \beta (\hat{\mu}_t - \hat{\mu}_{t-1}) / p + \text{fundamental return}
    $$

    Substituting into the learning equation and ignoring the fundamental component for stability analysis, we get the homogeneous recursion:

    $$
    \hat{\mu}_t = (1-\alpha)\hat{\mu}_{t-1} + \alpha \cdot \frac{\gamma \beta}{p}(\hat{\mu}_{t-1} - \hat{\mu}_{t-2})
    $$

    Let $\hat{\mu}_t = A z^t$. The characteristic equation is:

    $$
    z^2 - \left(1 - \alpha + \frac{\alpha\beta\gamma}{p}\right)z - \frac{\alpha\beta\gamma}{p} \cdot (-1) = 0
    $$

    Simplifying with the substitution $\phi = \alpha\beta\gamma / p$:

    $$
    z^2 - (1 - \alpha + \phi)z + \phi = 0
    $$

    **(b)** The system is stable when all roots $|z| < 1$. By the Jury stability criterion for second-order systems, the necessary and sufficient conditions are:

    1. $1 - (1-\alpha+\phi) + \phi > 0$, which gives $\alpha > 0$ (always satisfied).
    2. $1 + (1-\alpha+\phi) + \phi > 0$, which gives $2 - \alpha + 2\phi > 0$ (satisfied for reasonable parameters).
    3. $|\phi| < 1$, i.e., $\alpha\beta\gamma / p < 1$.

    The binding constraint is $\alpha\beta\gamma < p$, or equivalently $\alpha\beta\gamma / p < 1$. The system is **stable when** $\alpha\beta\gamma < p$ **and unstable when** $\alpha\beta\gamma \geq p$.

    In normalized form (setting $p = 1$), the stability condition is simply:

    $$
    \alpha \beta \gamma < 1
    $$

    **(c)** Interpretation of each parameter:

    - **$\alpha$ (learning speed)**: How quickly agents update their expected return estimate based on recent performance. High $\alpha$ means agents react strongly to the latest return, incorporating feedback quickly.
    - **$\beta$ (aggressiveness)**: How much agents trade per unit of expected return. High $\beta$ means a small perceived opportunity generates large positions.
    - **$\gamma$ (market impact)**: How much prices move per unit of aggregate trading. High $\gamma$ indicates an illiquid market where trades have large price effects.

    **Which parameter is most dangerous to increase?** All three contribute symmetrically to the product $\alpha\beta\gamma$, but in practice $\gamma$ (market impact) is the most dangerous because:

    1. It is the least controllable: $\alpha$ and $\beta$ are chosen by agents, but $\gamma$ depends on market structure and liquidity, which can change abruptly (e.g., during stress events when liquidity evaporates).
    2. It can spike suddenly: during market crises, bid-ask spreads widen and market depth decreases, causing $\gamma$ to increase rapidly and potentially pushing $\alpha\beta\gamma$ above the stability threshold.
    3. It affects all agents simultaneously: an increase in $\gamma$ destabilizes the system regardless of individual agents' choices of $\alpha$ and $\beta$.

---

**Exercise 5.** Explain why learning-induced instability leads to non-linear risk amplification that is invisible to standard risk models. (a) A VaR model calibrated on normal periods estimates daily VaR at 2%. During a crowded-trade unwind, the actual daily loss is 8%. What went wrong? (b) Describe how the interaction between similar learning algorithms creates endogenous tail events: the probability of extreme losses is higher than predicted by models assuming independent agents. (c) Propose a risk management approach that accounts for learning-induced instability, such as monitoring crowding indicators (e.g., short interest concentration, similar factor exposures across funds).

??? success "Solution to Exercise 5"
    **(a)** The VaR model calibrated on normal periods fails because it assumes **stationary, exogenous risk**. During normal periods, agent strategies are uncorrelated and the feedback loop $\alpha\beta\gamma < 1$ is well within the stable regime. The VaR estimate of 2% is based on the historical distribution of returns under these conditions.

    During a crowded-trade unwind:

    1. Many agents hold similar positions (crowding) built up during the calm period.
    2. A trigger event causes some agents to sell, moving prices against the crowd.
    3. The price movement triggers other agents' stop-losses or risk limits, causing more selling.
    4. The feedback loop amplifies losses far beyond what the historical distribution predicts.

    The actual 8% loss reflects **endogenous risk**---risk created by the interaction of agents' strategies, not by external shocks. The VaR model misses this because it treats returns as drawn from a fixed distribution, ignoring the state-dependent feedback that makes the distribution itself depend on agent behavior.

    **(b)** The interaction between similar learning algorithms creates endogenous tail events through **synchronization**:

    - **Independent agents**: If $N$ agents trade independently, aggregate demand is the sum of $N$ roughly independent random variables. By the CLT, extreme aggregate demand events are exponentially rare (Gaussian tails).
    - **Correlated agents**: When agents use similar learning algorithms, their strategies become correlated. In the extreme case of perfect correlation, aggregate demand is $N$ times a single agent's demand, with the same tail probability but $N$ times the magnitude.

    The probability of a loss exceeding $k\sigma$ under independence is approximately $e^{-k^2/2}$ (Gaussian). Under full correlation, the same probability threshold corresponds to a loss of $Nk\sigma$, which is $N$ times larger. In reality, the correlation is partial and state-dependent (higher during stress), creating a fat-tailed distribution for aggregate losses:

    $$
    \Pr(\text{Loss} > x) \gg \Pr_{\text{independent}}(\text{Loss} > x)
    $$

    for large $x$. The endogenous correlation inflates the tails relative to the independent-agent assumption.

    **(c)** A risk management approach accounting for learning-induced instability should include:

    1. **Crowding indicators**: Monitor concentration of positions across market participants. Metrics include short interest ratios, factor exposure overlap across funds (estimated from 13F filings), and correlation of flows into similar strategies (e.g., ETFs tracking the same factors).
    2. **Feedback stress tests**: Instead of applying historical shocks, simulate scenarios where the feedback loop is active: an initial shock triggers rebalancing, which amplifies the shock. Compute the amplified loss under realistic estimates of $\alpha$, $\beta$, and $\gamma$.
    3. **Liquidity-adjusted risk**: Increase VaR estimates during periods of low liquidity ($\gamma$ high) or high strategy crowding (effective $N\beta$ large). This can be formalized by multiplying the standard VaR by an amplification factor $1/(1 - \alpha\beta\gamma)$ when the system is near the instability threshold.
    4. **Regime-dependent models**: Use models that allow the return distribution to depend on the state (e.g., Markov-switching models where the "crisis" regime has higher volatility and correlation).

---

**Exercise 6.** The "paradox of stability" (Minsky hypothesis) states that stability itself breeds instability: in calm markets, agents take more risk (lower $\hat{\sigma}$ leads to higher leverage), which makes the system fragile to shocks. (a) Formalize this using a leverage cycle model: leverage $L_t = L_{\max} / \hat{\sigma}_t$ and portfolio value $V_{t+1} = V_t(1 + L_t r_{t+1})$. Show that a small negative return $r < 0$ causes a loss proportional to $L_t$, which triggers deleveraging. (b) Compute the required selling if $V_t = \$1$ billion, $L_t = 10$, and $r = -1\%$. (c) Discuss why the learning algorithms that reduce volatility estimates during calm periods are endogenously sowing the seeds of future instability.

??? success "Solution to Exercise 6"
    **(a)** The leverage cycle model is:

    $$
    L_t = \frac{L_{\max}}{\hat{\sigma}_t}, \quad V_{t+1} = V_t(1 + L_t\, r_{t+1})
    $$

    During a calm period, $\hat{\sigma}_t$ is low, so $L_t$ is high. A negative return $r_{t+1} = r < 0$ causes:

    $$
    V_{t+1} - V_t = V_t \cdot L_t \cdot r
    $$

    The loss is:

    $$
    |V_{t+1} - V_t| = V_t \cdot L_t \cdot |r| = V_t \cdot \frac{L_{\max}}{\hat{\sigma}_t} \cdot |r|
    $$

    This loss is proportional to $L_t = L_{\max}/\hat{\sigma}_t$, which is highest precisely when volatility is lowest (the calm period). After the loss, the leverage ratio increases because equity has shrunk while debt remains:

    $$
    L_{t+1} = \frac{\text{Assets}_{t+1}}{\text{Equity}_{t+1}} = \frac{V_t(1+L_t r)}{V_t(1+L_t r) - \text{Debt}} > L_t \quad (\text{for } r < 0)
    $$

    If $L_{t+1}$ exceeds the target $L_{\max}/\hat{\sigma}_{t+1}$, the fund must sell assets to delever, triggering the feedback loop.

    **(b)** With $V_t = \$1$ billion, $L_t = 10$, and $r = -1\%$:

    $$
    \text{Loss} = V_t \cdot L_t \cdot |r| = \$1\text{B} \times 10 \times 0.01 = \$100\text{M}
    $$

    Post-loss equity: $V_{t+1} = \$1\text{B} - \$100\text{M} = \$900\text{M}$.

    Pre-loss assets: $L_t \times V_t = \$10\text{B}$.

    Post-loss assets: $\$10\text{B} \times (1 - 0.01) = \$9.9\text{B}$.

    Post-loss leverage: $\$9.9\text{B} / \$900\text{M} = 11.0$.

    To restore leverage to $L_t = 10$, the fund needs equity of $\text{Assets}_{\text{new}} / 10$, so $\text{Assets}_{\text{new}} = 10 \times \$900\text{M} = \$9.0\text{B}$.

    Required selling:

    $$
    \Delta\text{Assets} = \$9.9\text{B} - \$9.0\text{B} = \$900\text{M}
    $$

    The fund must sell \$900 million in assets to restore its leverage target after a mere 1% market decline. This selling pressure, if it causes further price declines, triggers additional deleveraging---the feedback loop of the Minsky moment.

    **(c)** Learning algorithms that reduce volatility estimates during calm periods are endogenously sowing instability because:

    1. **Low $\hat{\sigma}$ $\Rightarrow$ high leverage**: During extended calm periods, EWMA and similar estimators produce low $\hat{\sigma}_t$, which causes vol-targeting and risk-parity strategies to increase leverage.
    2. **Buildup of fragility**: The aggregate leverage in the system grows, making it increasingly sensitive to shocks. The feedback parameter $\alpha\beta\gamma$ (from Exercise 4) increases as $\beta$ (aggressiveness, via leverage) grows.
    3. **Approaching the instability threshold**: As leverage builds, the system moves closer to $\alpha\beta\gamma = 1$. A small shock that would be absorbed in a low-leverage state is now sufficient to trigger the feedback loop.
    4. **Sudden transition**: The transition from stable ($\alpha\beta\gamma < 1$) to unstable ($\alpha\beta\gamma \geq 1$) can occur suddenly, because the learning algorithms that suppressed $\hat{\sigma}$ have been **accumulating leverage gradually** during the calm period.
    5. **Self-defeating stability**: The very mechanism that produced stability (low volatility estimates leading to efficient allocation) creates the conditions for instability (high leverage leading to fragility). This is precisely Minsky's insight: stability is destabilizing.

    The paradox is resolved by recognizing that low measured volatility is not the same as low risk. The learning algorithms confuse the two because they measure risk using backward-looking volatility estimates, which do not account for the endogenous buildup of systemic fragility through leverage accumulation.

---

**Exercise 7.** Compare three approaches to mitigating learning-induced instability: (a) position limits that cap the maximum exposure of any single algorithm, (b) diversity requirements that mandate different model classes or rebalancing frequencies across funds, and (c) circuit breakers that halt trading when price moves exceed a threshold. For each approach, discuss the mechanism by which it breaks the feedback loop, its practical implementation challenges, and potential unintended consequences. Which approach is most consistent with macroprudential regulation?

??? success "Solution to Exercise 7"
    **(a) Position limits** that cap the maximum exposure of any single algorithm:

    **Mechanism**: By capping exposure at $w_{\max}$, position limits bound each agent's contribution to aggregate demand. If $v_t^i \leq v_{\max}$ for all $i$, then aggregate impact $\gamma \sum_i v_t^i \leq \gamma N v_{\max}$. This prevents any single algorithm from dominating the feedback loop and ensures that the product $\alpha \beta_{\text{eff}} \gamma$ remains bounded.

    **Implementation challenges**: (i) Defining the right limit level---too tight and legitimate strategies are curtailed, too loose and limits are not binding during normal times. (ii) Limits are easy to circumvent by splitting strategies across multiple entities or accounts. (iii) Limits must be set in real-time, requiring robust position reporting infrastructure.

    **Unintended consequences**: (i) Limits may encourage front-running: if a trader is known to be near their limit, others can exploit the predictable behavior. (ii) Limits may reduce liquidity provision during stress, as market makers hit their caps precisely when liquidity is most needed. (iii) Cliff effects: as many agents simultaneously hit their limits, the market may experience a sudden withdrawal of trading activity.

    **(b) Diversity requirements** that mandate different model classes or rebalancing frequencies:

    **Mechanism**: Diversity breaks the synchronization that drives the feedback loop. If agents use different models (some momentum, some mean-reversion, some fundamental) with different rebalancing frequencies (daily, weekly, monthly), their trades are less correlated. The effective feedback parameter $\alpha\beta\gamma$ is reduced because the $\beta$ terms partially cancel across agents with opposing strategies.

    **Implementation challenges**: (i) How to define and enforce "diversity"---regulatory agencies would need to assess the similarity of proprietary algorithms, raising confidentiality concerns. (ii) Measuring strategy overlap is technically difficult (similar inputs can produce different strategies and vice versa). (iii) Innovation may be stifled if firms are forced to use non-standard approaches.

    **Unintended consequences**: (i) Forced diversity may lead to adoption of poorly understood or untested strategies. (ii) Compliance costs may favor large firms that can afford multiple strategy teams. (iii) Diversity requirements may be gamed by making superficial changes to models while retaining the same core signals.

    **(c) Circuit breakers** that halt trading when price moves exceed a threshold:

    **Mechanism**: Circuit breakers interrupt the feedback loop by pausing trading when price moves exceed a threshold (e.g., 5% intraday decline). During the pause, (i) the learning update $\hat{\mu}_t = (1-\alpha)\hat{\mu}_{t-1} + \alpha r_{t-1}$ is frozen because no new returns are observed, and (ii) traders can reassess positions without the pressure of ongoing price moves. This prevents the explosive regime $\alpha\beta\gamma \geq 1$ from persisting indefinitely.

    **Implementation challenges**: (i) Setting the right threshold---too tight and normal volatility triggers halts, too loose and significant damage occurs before the circuit breaker activates. (ii) Cross-market coordination: if equities halt but futures do not, selling pressure migrates to futures. (iii) Post-halt dynamics: the reopening auction may exhibit a large gap, potentially triggering another halt.

    **Unintended consequences**: (i) **Magnet effect**: as prices approach the circuit breaker threshold, traders may rush to sell before the halt, accelerating the decline they are meant to prevent. (ii) Liquidity vacuum: market makers may withdraw orders near the threshold, knowing that a halt will freeze their positions. (iii) The halt does not resolve the underlying imbalance; it merely delays it.

    **Macroprudential assessment**: **Diversity requirements** (option b) are most consistent with macroprudential regulation because:

    1. They address the **root cause** (strategy crowding) rather than the **symptom** (extreme price moves).
    2. They are **preventive** rather than reactive: diversity reduces the probability of instability rather than interrupting it after it begins.
    3. They align with macroprudential principles of monitoring systemic risk from the interaction of institutions, not just individual institution risk.
    4. However, they are the hardest to implement in practice, which is why circuit breakers are more commonly adopted as a pragmatic second-best solution.
