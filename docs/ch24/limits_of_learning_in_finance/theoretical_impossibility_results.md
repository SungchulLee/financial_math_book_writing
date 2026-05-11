# Theoretical Impossibility Results


Beyond practical challenges, there are **theoretical limits** to what learning algorithms can achieve in financial markets.

---

## No-free-lunch principles


No-free-lunch theorems state that:

- averaged over all data-generating processes,
- no learning algorithm outperforms others.

Assumptions drive performance, not algorithms alone.

---

## Market efficiency arguments


Under strong forms of market efficiency:

- predictable excess returns cannot persist,
- learning algorithms cannot systematically outperform.

Any discovered pattern may vanish once exploited.

---

## Adversarial and adaptive markets


In adaptive markets:

- strategies change the environment,
- learning induces feedback effects,
- convergence guarantees may fail.

This limits long-term learnability.

---

## Implications for practice


Impossibility results imply:

- performance guarantees are fragile,
- humility is required in model claims,
- robustness matters more than optimality.

Learning must be combined with judgment.

---

## Key takeaways


- There are fundamental limits to learning.
- Efficiency and adaptivity constrain predictability.
- Robust risk management dominates pure optimization.

---

## Further reading


- Wolpert & Macready, no-free-lunch theorems.
- Farmer, markets as adaptive systems.

---

## Exercises

**Exercise 1.** State the No-Free-Lunch theorem for optimization: averaged over all possible objective functions, no optimization algorithm outperforms random search. Explain why this theorem does not make optimization useless in practice---what role do problem-specific assumptions (structure, smoothness, convexity) play in making certain algorithms effective for financial applications?

??? success "Solution to Exercise 1"
    **No-Free-Lunch theorem and the role of structure.**

    **Statement.** The No-Free-Lunch (NFL) theorem for optimization (Wolpert and Macready, 1997) states: for any pair of optimization algorithms $A_1$ and $A_2$, when performance is averaged uniformly over *all* possible objective functions $f: \mathcal{X} \to \mathbb{R}$:

    $$
    \sum_f P(d_m^{(1)} \mid f, m, A_1) = \sum_f P(d_m^{(2)} \mid f, m, A_2)
    $$

    where $d_m^{(i)}$ is the sequence of $m$ distinct sample points and their evaluations produced by algorithm $A_i$. In other words, no optimization algorithm is universally superior: for every problem where $A_1$ outperforms $A_2$, there exists another problem where $A_2$ outperforms $A_1$.

    **Why NFL does not make optimization useless.** The theorem averages over *all* possible objective functions, including pathological ones that bear no resemblance to real-world problems. In practice, financial optimization problems have considerable **structure**:

    - **Smoothness:** Portfolio objective functions (e.g., mean-variance, Sharpe ratio) are smooth and often differentiable, allowing gradient-based methods to be highly efficient. Random search cannot exploit this smoothness.

    - **Convexity:** Mean-variance optimization with linear constraints is a quadratic program --- a convex problem with a unique global optimum. Convex optimization algorithms (interior point methods, quadratic programming) solve this in polynomial time, far outperforming random search.

    - **Low effective dimensionality:** Although a portfolio may have hundreds of assets, factor models reduce the effective dimension to a handful of principal components. Algorithms that exploit low-rank structure (e.g., factor-based optimization) dramatically outperform generic methods.

    - **Regularity in financial data:** Return distributions, while heavy-tailed, have well-characterized statistical properties (e.g., volatility clustering, mean-reversion in certain assets). Algorithms designed to exploit these patterns (GARCH, regime-switching models) outperform agnostic approaches.

    The NFL theorem tells us that algorithm selection *matters* --- we must match the algorithm to the problem structure. It does not say that all algorithms are equally useless; it says that no algorithm is universally best. For financial applications, the relevant question is: does the problem have exploitable structure? In most cases, the answer is yes.

---

**Exercise 2.** Under the strong form of the Efficient Market Hypothesis, all information (public and private) is reflected in prices. If true, show that the best predictor of tomorrow's return is zero (a martingale). What does this imply for any learning algorithm attempting to forecast returns? Under what weaker form of efficiency can learning algorithms still add value?

??? success "Solution to Exercise 2"
    **Efficient Market Hypothesis and implications for learning.**

    **Strong-form EMH.** Under the strong form of the EMH, all information --- public, private, and insider --- is instantaneously reflected in prices. Formally, the price process $\{S_t\}$ satisfies the **martingale property** with respect to the universal information filtration $\mathcal{F}_t$:

    $$
    \mathbb{E}[S_{t+1} \mid \mathcal{F}_t] = S_t
    $$

    or equivalently, for returns:

    $$
    \mathbb{E}[r_{t+1} \mid \mathcal{F}_t] = 0
    $$

    **Proof that the best predictor is zero.** If $\hat{r}_{t+1} = g(\mathcal{F}_t)$ is any $\mathcal{F}_t$-measurable predictor, the mean squared prediction error is:

    $$
    \mathbb{E}[(r_{t+1} - g(\mathcal{F}_t))^2] = \mathbb{E}[r_{t+1}^2] - 2\mathbb{E}[r_{t+1}\,g(\mathcal{F}_t)] + \mathbb{E}[g(\mathcal{F}_t)^2]
    $$

    By the tower property and the martingale condition:

    $$
    \mathbb{E}[r_{t+1}\,g(\mathcal{F}_t)] = \mathbb{E}[\mathbb{E}[r_{t+1} \mid \mathcal{F}_t]\,g(\mathcal{F}_t)] = \mathbb{E}[0 \cdot g(\mathcal{F}_t)] = 0
    $$

    Therefore:

    $$
    \mathbb{E}[(r_{t+1} - g(\mathcal{F}_t))^2] = \mathbb{E}[r_{t+1}^2] + \mathbb{E}[g(\mathcal{F}_t)^2] \geq \mathbb{E}[r_{t+1}^2]
    $$

    with equality if and only if $g(\mathcal{F}_t) = 0$ a.s. The minimum MSE predictor is $\hat{r}_{t+1} = 0$.

    **Implications for learning algorithms.** Under strong-form EMH, any learning algorithm that produces a nonzero forecast $\hat{r}_{t+1} \neq 0$ is *adding noise* to the optimal prediction. No amount of data, computational power, or algorithmic sophistication can improve upon the trivial forecast of zero. All apparent patterns in historical data are either noise or already priced in.

    **Weaker forms.** Under the **semi-strong form**, prices reflect all *public* information but not private information. Agents with superior private information (or faster processing of public information) can earn excess returns. Under the **weak form**, prices reflect past price and volume data, but publicly available fundamental information (earnings, macroeconomic data) may not be fully priced in.

    Learning algorithms can add value under weak-form efficiency by exploiting fundamental information, and under semi-strong efficiency by processing information faster than the market (a competitive advantage, not a violation of efficiency). The relevant question for practitioners is which form of efficiency approximately holds in their market --- highly liquid large-cap equities are approximately semi-strong efficient, while less liquid or less studied markets may exhibit weak-form inefficiencies.

---

**Exercise 3.** In an adaptive market (Lo, 2004), strategies that exploit inefficiencies attract capital, which erodes the inefficiency. Model this as a simple game: strategy $i$ earns return $\alpha_i(1 - c_i/C)$ where $c_i$ is capital allocated and $C$ is a capacity parameter. Show that in equilibrium, all strategies earn zero excess return. How does this limit the long-run profitability of any learned strategy?

??? success "Solution to Exercise 3"
    **Adaptive market equilibrium and the erosion of alpha.**

    **Model.** Strategy $i$ earns a return that depends on allocated capital:

    $$
    R_i = \alpha_i\!\left(1 - \frac{c_i}{C}\right)
    $$

    where $\alpha_i > 0$ is the inherent alpha (return from the inefficiency), $c_i$ is the capital allocated to strategy $i$, and $C > 0$ is the capacity parameter (the maximum capital the inefficiency can absorb before it is fully arbitraged away).

    **Equilibrium analysis.** Rational investors allocate capital to maximize returns. If strategy $i$ earns $R_i > 0$, it attracts additional capital. If $R_i < 0$, capital withdraws. In equilibrium, capital flows until no reallocation can improve returns.

    **Nash equilibrium.** In a competitive market with many investors, capital flows to each strategy until marginal returns equalize. For an interior equilibrium where all strategies are used ($c_i > 0$ for all $i$), returns must be equal:

    $$
    R_i = R_j \quad \forall\, i, j
    $$

    Setting $R_i = R_j$:

    $$
    \alpha_i\!\left(1 - \frac{c_i}{C}\right) = \alpha_j\!\left(1 - \frac{c_j}{C}\right)
    $$

    Additionally, if there is free entry and no barriers to investment, the equilibrium return must equal the opportunity cost. If the risk-free rate is the outside option ($R_f = 0$ for excess returns), then in equilibrium:

    $$
    R_i = \alpha_i\!\left(1 - \frac{c_i}{C}\right) = 0 \quad \Longrightarrow \quad c_i = C
    $$

    Wait --- this implies each strategy absorbs capital $C$, which cannot be correct for finite total capital. The equilibrium depends on the total capital $K$ available across all strategies.

    If total capital $K$ is unconstrained (free entry), for each strategy in equilibrium:

    $$
    c_i^* = C \quad \Longrightarrow \quad R_i^* = \alpha_i(1 - 1) = 0
    $$

    **All strategies earn zero excess return in equilibrium.** This is because capital flows into each profitable strategy until the capacity is fully utilized and the inefficiency is completely arbitraged away.

    If total capital is constrained ($\sum_i c_i = K < nC$ where $n$ is the number of strategies), the equilibrium has positive returns but still features diminished alpha relative to the zero-capital case.

    **Implications for learned strategies.** A machine learning algorithm that discovers a profitable inefficiency (positive $\alpha_i$) faces a self-defeating dynamic:

    1. The algorithm identifies the pattern and begins trading.
    2. Profits attract attention --- other funds develop similar algorithms.
    3. Increased capital erodes the alpha: $R_i$ decreases as $c_i$ increases.
    4. In the long run, $R_i \to 0$ as the inefficiency is fully exploited.

    This is the fundamental insight of Lo's Adaptive Markets Hypothesis: strategies have life cycles. The long-run profitability of any learned strategy is bounded by the rate at which the market adapts. Persistent profitability requires *continuous innovation* --- discovering new inefficiencies faster than old ones are arbitraged away.

---

**Exercise 4.** The bias-variance decomposition states that expected prediction error = bias$^2$ + variance + irreducible noise. In a financial time series with signal-to-noise ratio $\text{SNR} = 0.01$ (typical for daily returns), compute the minimum number of observations needed to detect the signal at the 5% significance level using $n \geq (z_{0.025}/\text{SNR})^2$. What does this imply about the feasibility of learning from short samples?

??? success "Solution to Exercise 4"
    **Minimum sample size for signal detection.**

    **Setup.** Consider detecting a signal of size $\mu$ (expected return per period) in noise of standard deviation $\sigma$. The signal-to-noise ratio is:

    $$
    \text{SNR} = \frac{\mu}{\sigma} = 0.01
    $$

    The sample mean estimator is $\hat{\mu} = \frac{1}{n}\sum_{t=1}^n r_t$ with standard error $\sigma/\sqrt{n}$.

    **Hypothesis test.** To detect $\mu > 0$ at the 5% significance level (one-sided) with the $z$-test:

    $$
    z = \frac{\hat{\mu}}{\sigma/\sqrt{n}} = \frac{\mu}{\sigma/\sqrt{n}} = \text{SNR} \cdot \sqrt{n}
    $$

    For significance at the 5% level, we need $z \geq z_{0.05} = 1.645$ (one-sided) or $z \geq z_{0.025} = 1.96$ (two-sided). Using the two-sided threshold:

    $$
    \text{SNR} \cdot \sqrt{n} \geq z_{0.025} = 1.96
    $$

    $$
    \sqrt{n} \geq \frac{z_{0.025}}{\text{SNR}} = \frac{1.96}{0.01} = 196
    $$

    $$
    n \geq 196^2 = 38{,}416
    $$

    **Interpretation.** At an SNR of 0.01, we need approximately **38,416 daily observations** --- roughly **153 years** of daily trading data (assuming 252 trading days per year) --- just to detect that the signal is nonzero at the 5% level.

    Note: this computation gives only the sample size needed for *detection* (rejecting the null), not for *useful prediction* (having enough precision to be economically meaningful). For practical trading, we would also want high power (e.g., 80%), which requires:

    $$
    n \geq \left(\frac{z_{0.025} + z_{0.20}}{\text{SNR}}\right)^2 = \left(\frac{1.96 + 0.84}{0.01}\right)^2 = 280^2 = 78{,}400
    $$

    This is over **311 years** of daily data.

    **Implications for learning from short samples:**

    - With typical financial datasets of 10--20 years ($n \approx 2{,}500$--$5{,}000$), we have $z = 0.01 \times \sqrt{5000} \approx 0.71$, which is far below the significance threshold. The signal is **undetectable** in realistic samples.
    - This is a fundamental impossibility: the signal-to-noise ratio in financial returns is so low that statistical learning requires far more data than exists.
    - Machine learning algorithms, despite their flexibility, cannot overcome this fundamental statistical limitation. They may achieve better *efficiency* (higher power for a given sample size) by exploiting structure, but they cannot create information that is not in the data.
    - This explains why most return prediction models have very low $R^2$ values ($< 1\%$) and why even genuinely profitable strategies have modest Sharpe ratios.

---

**Exercise 5.** A fundamental impossibility in adversarial settings is that if an agent's strategy is predictable, a counterparty can exploit it. Formalize this: if a trading algorithm $\mathcal{A}$ produces trades $\{a_t\}$ that are $\mathcal{F}_{t-1}$-measurable, an adversary with knowledge of $\mathcal{A}$ can construct prices $\{S_t\}$ such that $\mathcal{A}$ loses money. How does this relate to the game-theoretic foundations of market microstructure?

??? success "Solution to Exercise 5"
    **Adversarial exploitation of predictable strategies.**

    **Formalization.** Consider a trading algorithm $\mathcal{A}$ that at each time $t$ produces a trade $a_t$ (number of shares to buy/sell) based on past information:

    $$
    a_t \in \mathcal{F}_{t-1} \quad \text{($a_t$ is $\mathcal{F}_{t-1}$-measurable)}
    $$

    The P&L of the algorithm over $T$ periods is:

    $$
    \text{PnL}_{\mathcal{A}} = \sum_{t=1}^T a_t (S_t - S_{t-1}) = \sum_{t=1}^T a_t \Delta S_t
    $$

    **Adversarial construction.** An adversary who knows the algorithm $\mathcal{A}$ (including its internal state and decision rule) can observe $a_t$ before setting $S_t$. The adversary constructs:

    $$
    \Delta S_t = S_t - S_{t-1} = -\text{sign}(a_t) \cdot \epsilon_t
    $$

    where $\epsilon_t > 0$ is an arbitrary positive increment. Then:

    $$
    a_t \Delta S_t = a_t \cdot (-\text{sign}(a_t) \cdot \epsilon_t) = -|a_t| \cdot \epsilon_t \leq 0
    $$

    with strict inequality whenever $a_t \neq 0$. The total P&L is:

    $$
    \text{PnL}_{\mathcal{A}} = -\sum_{t=1}^T |a_t| \epsilon_t < 0
    $$

    The algorithm loses money on every trade.

    **Key insight.** The adversary's power comes from two properties:

    1. **Predictability:** $a_t$ is $\mathcal{F}_{t-1}$-measurable, so the adversary can compute $a_t$ before the market moves.
    2. **Market-making power:** The adversary can influence prices (i.e., the adversary is a market maker or informed trader on the other side).

    **Relation to market microstructure.** This connects directly to the game-theoretic foundations of market microstructure:

    - **Kyle (1985) model:** An informed trader (adversary) trades against a market maker. The informed trader's strategy is designed to maximize profits at the expense of uninformed traders. If a trading algorithm is predictable, the informed trader can effectively "pick off" the algorithm by trading against its anticipated orders.

    - **Glosten-Milgrom (1985):** Market makers set bid-ask spreads to protect against informed traders. A predictable algorithm is equivalent to an uninformed trader whose order flow is known in advance --- the market maker will adjust prices adversely.

    - **Adverse selection:** In equilibrium, the bid-ask spread reflects the market maker's expected loss to informed traders. A predictable algorithm always pays the spread (and more), because its trades are anticipated and the market moves against it before execution.

    **Practical implications:**

    - Trading algorithms must incorporate **randomization** to avoid being fully predictable. This is why execution algorithms use random timing, order splitting, and dark pools.
    - The more *transparent* an algorithm's strategy (e.g., rules-based index rebalancing), the more vulnerable it is to front-running.
    - This impossibility result is strongest in adversarial settings (e.g., market microstructure) and weakest in settings where prices are driven by exogenous forces (e.g., macroeconomic factors).

---

**Exercise 6.** Compare the implications of impossibility results for two contexts: (a) high-frequency trading where the data-generating process is approximately stationary over short horizons, and (b) macro factor investing where regimes span years. In which context are impossibility results more binding, and why? Propose a practical framework for deciding when learning is likely to succeed.

??? success "Solution to Exercise 6"
    **Impossibility results in high-frequency vs. macro factor investing.**

    **(a) High-frequency trading (HFT).**

    **Strengths of learning in HFT:**

    - **Approximate stationarity.** Over short horizons (seconds to minutes), the data-generating process for order flow, bid-ask dynamics, and microstructure patterns is approximately stationary. This means that models trained on recent data are likely to generalize to the immediate future.
    - **Massive sample sizes.** HFT generates thousands to millions of observations per day, far exceeding the sample size requirements from Exercise 4. Even with low SNR per trade, the large $n$ provides statistical power.
    - **Structural regularities.** Microstructure patterns (bid-ask bounce, order imbalance, queue dynamics) have strong economic foundations and are robust features.
    - **Fast feedback.** Strategies can be validated quickly (within days or weeks), enabling rapid iteration and adaptation.

    **Binding impossibility constraints:**

    - **Adversarial competition.** HFT is a zero-sum game among algorithms. The adversarial impossibility result (Exercise 5) is highly relevant: competitors actively seek to detect and exploit predictable patterns in each other's order flow.
    - **Capacity constraints.** Even genuine microstructure alpha has very limited capacity --- profits erode quickly as capital scales (Exercise 3).
    - **Latency arms race.** The advantage is often not in better learning but in faster execution, which is a technological rather than statistical challenge.

    **(b) Macro factor investing.**

    **Challenges for learning in macro investing:**

    - **Severe non-stationarity.** Macroeconomic regimes span years or decades. The data-generating process changes fundamentally across regimes (e.g., interest rate environment, regulatory regime, technological era). Models trained on one regime may be useless in the next.
    - **Tiny sample sizes.** Monthly data over 50 years provides only $n = 600$ observations. With typical SNR $\approx 0.05$ for monthly factor returns, the minimum sample for detection is $n \geq (1.96/0.05)^2 \approx 1{,}537$ months $\approx 128$ years.
    - **No-free-lunch relevance.** With such limited data and regime changes, there is essentially no way to distinguish between genuine factor premia and historical accidents. The NFL theorem is most binding here: with few observations and many potential factors, almost any pattern can be "found" in the data.
    - **Multiple testing burden.** Decades of factor research have tested hundreds of candidate factors (HLZ), making it difficult to identify genuinely new ones.

    **Verdict.** Impossibility results are **more binding for macro factor investing** than for HFT. The combination of small samples, non-stationarity, and massive multiple testing creates a setting where learning is fundamentally limited. In HFT, the approximate stationarity and large sample sizes mitigate the statistical impossibilities, but adversarial dynamics introduce different constraints.

    **Practical framework for deciding when learning is likely to succeed:**

    | Criterion | Favorable for Learning | Unfavorable |
    |-----------|----------------------|-------------|
    | **Sample size** | $n \gg (z_\alpha / \text{SNR})^2$ | $n$ near or below threshold |
    | **Stationarity** | Short-horizon, stable DGP | Regime changes, structural breaks |
    | **Signal-to-noise** | SNR > 0.05 | SNR < 0.01 |
    | **Competition** | Few sophisticated competitors | Adversarial, zero-sum |
    | **Capacity** | Strategy scales with capital | Alpha erodes quickly |
    | **Feedback speed** | Fast validation (days) | Slow validation (years) |
    | **Economic foundation** | Clear mechanism | Pure statistical pattern |

    A proposed decision rule: score each criterion on a 1--5 scale. Learning is likely to succeed if:

    $$
    \text{Total Score} = \sum_{j=1}^{7} w_j \cdot s_j > \theta
    $$

    where $w_j$ are importance weights and $\theta$ is a minimum threshold calibrated to historical successes and failures of learning-based strategies. The weights should emphasize sample size and stationarity most heavily, as these are the most fundamental constraints.
