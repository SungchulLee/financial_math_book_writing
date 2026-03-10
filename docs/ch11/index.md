# Chapter 11: Hedging


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

This chapter develops the theory and practice of hedging derivative positions, progressing from the idealized continuous-time delta hedge through the reality of discrete rebalancing, transaction costs, and model misspecification, to optimal hedging in incomplete markets. The central tension -- between the theoretical perfection of continuous hedging and the practical constraints of real trading -- motivates a hierarchy of hedging strategies with quantifiable error bounds and explicit trade-offs between cost, risk, and model dependence.

## Key Concepts

### **Basic Trading and Hedging Strategies**
Options trading strategies are built on Greek exposures, with each strategy expressing a specific view on direction, volatility, or time decay. The **gamma-theta tradeoff** is the central organizing principle: long gamma positions ($\Gamma > 0$, $\Theta < 0$) profit when the underlying makes large moves (realized volatility exceeds implied), while short gamma positions ($\Gamma < 0$, $\Theta > 0$) earn daily theta when markets remain calm. **Straddles** (long call and put at the same strike) provide symmetric exposure to large moves with breakeven at $S_T > K + \text{premium}$ or $S_T < K - \text{premium}$, while **strangles** use OTM options for cheaper but wider breakeven structures. **Risk reversals** (long OTM call, short OTM put) express simultaneous directional and volatility views, exploiting skew where puts are typically richer than equidistant calls. **Vega trades** position for changes in implied volatility itself, with long vega benefiting from vol increases and short vega profiting from post-spike mean reversion.

### **Delta Hedging and the Replication Argument**
Delta hedging is the most fundamental risk management technique: maintain a portfolio whose net delta is zero, $\Delta_{\text{portfolio}} = 0$, by holding $-\Delta$ shares per option. In the Black--Scholes framework, a European option is perfectly replicated by continuously holding $\Delta_t = \partial V / \partial S$ shares and financing at the risk-free rate. The delta-hedged P&L over a rebalancing period decomposes as

$$P\&L \approx \underbrace{\Theta\,\Delta t}_{\text{time decay}} + \underbrace{\frac{1}{2}\Gamma(\Delta S)^2}_{\text{gamma P\&L}} + \underbrace{\nu\,\Delta\sigma}_{\text{vega P\&L}}$$

This reveals that the hedger profits when realized volatility exceeds implied volatility (for a long gamma position). Delta hedging breaks down near expiry where gamma blows up as $\Gamma \sim 1/(S\sigma\sqrt{\tau})$, under jumps in the underlying, and in illiquid markets where bid-ask spreads make frequent rebalancing prohibitively expensive.

### **Gamma and Vega Hedging**
Delta hedging alone leaves the portfolio exposed to second-order effects. **Gamma hedging** neutralizes $\Gamma_{\text{portfolio}} = 0$ using additional options (since the underlying has zero gamma), followed by re-delta-hedging with shares. **Vega hedging** neutralizes $\nu_{\text{portfolio}} = 0$ to protect against implied volatility shifts, where $\delta V \approx \nu \cdot \delta\sigma_{\text{implied}}$. In Black--Scholes, vega and gamma are proportional via $\nu = \sigma S^2 \tau\,\Gamma$, but in practice (stochastic volatility, term structure effects) they decouple, requiring separate hedging. Joint gamma-vega neutralization requires at least two option instruments, solving the system

$$\begin{cases} n_1 \Gamma_1 + n_2 \Gamma_2 = -\Gamma_{\text{existing}} \\ n_1 \nu_1 + n_2 \nu_2 = -\nu_{\text{existing}} \end{cases}$$

followed by delta adjustment with shares. The gamma-theta link through the Black--Scholes PDE, $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)$, ensures one cannot simultaneously hold positive gamma and positive theta. **Short gamma strategies** sell options to earn theta while delta-hedging dynamically, profiting when $\sigma_{\text{realized}} < \sigma_{\text{implied}}$ but exposing the portfolio to adverse "buy high, sell low" rebalancing during large moves.

### **Theta Management and Time Decay**
Theta measures the rate of decline in an option's value with the passage of time. For ATM options, the extrinsic value decays as $V_{\text{extrinsic}} \propto \sigma S \sqrt{\tau}$, yielding the theta scaling $\Theta_{\text{ATM}} \propto -\sigma S / (2\sqrt{\tau})$ which diverges as $\tau \to 0$ -- reflecting the well-known acceleration of time decay in the final days before expiry. **Calendar spreads** exploit differential time decay by buying a long-dated option and selling a short-dated option at the same strike, earning positive net theta when the short leg decays faster. The daily P&L of a short ATM delta-hedged position decomposes as $\text{Daily P\&L} \approx |\Theta|\,\Delta t - \frac{1}{2}|\Gamma|(\Delta S)^2$, profitable when realized volatility remains below implied volatility, but exposed to large-move gamma losses and volatility spikes.

### **Portfolio Hedging and Cross-Greeks**
Portfolio-level hedging extends individual option hedging to multi-instrument books, where cross-Greeks -- Charm ($\partial\Delta/\partial t$), Vanna ($\partial^2 V/\partial S\partial\sigma$), and Volga ($\partial^2 V/\partial\sigma^2$) -- capture second-order interactions between state variables and model parameters. These sensitivities are critical for managing smile risk and for understanding how hedges evolve over time and across volatility regimes.

### **Discrete-Time Hedging Error**
Continuous-time delta hedging is an idealization; in practice, hedging at discrete times $t_0 < t_1 < \cdots < t_N = T$ introduces a random hedging error. The per-step error is

$$\epsilon_k \approx \frac{1}{2}\Gamma_k\left[(\Delta S_k)^2 - \sigma^2 S_k^2 \Delta t\right]$$

which has zero conditional mean but variance $\text{Var}(\epsilon_k) \approx \frac{1}{2}\Gamma_k^2 S_k^4 \sigma^4 (\Delta t)^2$. The cumulative hedging error variance scales linearly with the rebalancing interval, $\text{Var}(\text{HE}) \approx \frac{1}{2}\bar{\Gamma}^2 S^4 \sigma^4 T \cdot \Delta t$, with standard deviation $\text{Std}(\text{HE}) \sim \sqrt{\Delta t}$. By the central limit theorem, for small $\Delta t$ the cumulative error is approximately Gaussian: $\text{HE} \xrightarrow{d} \mathcal{N}(0,\, \frac{1}{2}\int_0^T \Gamma^2 S^4 \sigma^4\,dt \cdot \Delta t)$. The error is path-dependent through gamma, with volatile paths and paths crossing the strike amplifying the error significantly.

### **Gamma Risk and Convexity Effects**
After delta-hedging, residual P&L is driven by the convexity term $\delta V_{\text{hedged}} \approx \frac{1}{2}\Gamma(\delta S)^2$, linking delta-hedged P&L directly to realized variance. The cumulative P&L from delta-hedging over $[0,T]$ is $P\&L = \frac{1}{2}\int_0^T \Gamma(t,S_t) S_t^2 (\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)\,dt$, providing the theoretical foundation for volatility trading. Practitioners use **dollar gamma** $\Gamma_\$ = \frac{1}{2}\Gamma S^2$ to measure the dollar P&L from a 1% move. Long gamma positions profit from volatility (large squared moves) through favorable "buy low, sell high" rebalancing, while short gamma earns carry but is exposed to adverse rebalancing during large moves.

### **Asymptotic Hedging Error Expansions**
For small rebalancing intervals, the hedging error admits the asymptotic expansion $\text{HE} = c_1\sqrt{\Delta t} + c_2\Delta t + \cdots$, where the leading coefficient is

$$c_1 = \sqrt{\frac{1}{2}\int_0^T \Gamma(t,S_t)^2 S_t^4 \sigma^4\,dt}$$

This coefficient is path-dependent through gamma. With proportional transaction cost $\lambda$, the **Leland--Whalley--Wilmott** result shows the optimal no-trade bandwidth scales as $h \sim (3\lambda / (2\Gamma S^2 \sigma^2))^{1/3}$ and the expected utility loss scales as $\lambda^{2/3}(\Gamma S^2 \sigma^2)^{1/3} T$. Leland's effective volatility adjustment $\sigma_{\text{eff}}^2 = \sigma^2(1 + \sqrt{8\lambda/(\pi\sigma\sqrt{\Delta t})}\,\text{sign}(\Gamma))$ accounts for transaction costs through the pricing model. For jump risk with intensity $\lambda_J$ and size $J$, hedging error is dominated by jump contributions $\text{HE}_{\text{jump}} \sim \sum_{\text{jumps}} \frac{1}{2}\Gamma S^2 J^2$, not diffusive terms.

### **Impact of Volatility Misspecification**
When the hedger uses volatility $\hat{\sigma}$ while the true volatility is $\sigma$, the cumulative hedging error is given by the **El Karoui--Jeanblanc--Shreve** identity:

$$\varepsilon = \frac{1}{2}\int_0^T \Gamma(t,S_t)\left(\sigma^2 - \hat{\sigma}^2\right)S_t^2\,dt$$

For long option positions ($\Gamma > 0$), underestimating volatility ($\hat{\sigma} < \sigma$) produces a gain, while overestimating produces a loss. The error is path-dependent through the gamma weighting: misspecification during high-gamma periods (near strike, near expiry) has outsized impact. Even if average variance matches ($\frac{1}{T}\int_0^T \sigma(t)^2\,dt = \hat{\sigma}^2$), the hedging error need not vanish due to the $\Gamma$-weighting. This identity connects naturally to **variance swaps** via $\varepsilon = T(\sigma_R^2 - \hat{\sigma}^2) \cdot \overline{\Gamma_\$}$ and provides the theoretical basis for the **variance risk premium** when systematically exploited.

### **Rebalancing Frequency Analysis**
The trade-off between hedging error and transaction costs is governed by rebalancing frequency. More frequent rebalancing reduces the hedging error variance (which scales as $\Delta t$) but increases cumulative transaction costs (which scale inversely with $\Delta t$). The optimal rebalancing interval $\Delta t^*$ minimizes total cost by balancing these competing effects, with higher gamma requiring more frequent rebalancing and higher transaction costs favoring less frequent adjustment.

### **Instability of Higher-Order Greeks**
Higher-order Greeks suffer from numerical instability, especially near expiry and near payoff discontinuities. Finite-difference gamma estimation has error $\mathcal{O}(\epsilon/h^2) + \mathcal{O}(h^2)$, with optimal step size $h_{\text{opt}} \sim \epsilon^{1/4}$. Third-order Greeks (speed $\partial\Gamma/\partial S$) amplify noise as $\mathcal{O}(\epsilon/h^3)$, making them extremely sensitive. Near expiry, the gamma profile has width $\sim \sigma\sqrt{\tau}$ and magnitude $\sim \tau^{-1/2}$, so spatial derivatives of gamma diverge as $\sim 1/(\sigma^2\tau)$. Practical stabilization approaches include **bucketing** (averaging over strike/maturity ranges), **polynomial fitting** followed by analytic differentiation, **likelihood ratio / Malliavin estimators** that avoid finite differencing, and **automatic differentiation** that computes exact derivatives through the pricing algorithm.

### **Transaction Costs and Liquidity Effects**
With proportional cost $\lambda$ per dollar traded, rebalancing $\delta\theta$ shares costs $\lambda S|\delta\theta|$, and since hedge turnover increases with gamma, costs dominate near expiry. The **Whalley--Wilmott** optimal hedging strategy maintains delta within a no-trade band $\Delta^{\text{BS}} \pm h$ with bandwidth $h = (3\lambda e^{-r\tau}/(2\Gamma))^{1/3}$, where the $1/3$ exponent balances $\mathcal{O}(h^2)$ hedging error against $\mathcal{O}(1/h)$ costs. **Leland's modified volatility** $\sigma_{\text{Leland}}^2 = \sigma^2 + \text{sign}(\Gamma) \cdot \sigma\sqrt{8\lambda/(\pi\Delta t)}$ adjusts the pricing model to account for costs. Gamma-weighted turnover $\int_0^T |\Gamma|\sigma S\,dt$ diverges near expiry since $\Gamma \sim \tau^{-1/2}$, reflecting the infinite turnover needed for perfect hedging. Beyond bid-ask spreads, **market impact** ($\text{Execution Price} = S + \eta|\delta\theta|^\alpha$ with $\alpha \approx 0.5$), slippage, position limits, and funding costs further constrain practical hedging.

### **Bid-Ask Spread Effects**
The bid-ask spread $S = A - B$ includes inventory cost, information asymmetry protection, and order processing costs, with wider spreads for higher volatility and lower volume. Each rebalance incurs approximately $2S$ per unit in round-trip costs, making continuous rehedging infinitely expensive. Spreads create a pricing band around the model price ($\pm S/2$), and dynamic hedging becomes an optimal control problem rather than a pure replication strategy. Perfect replication assumed in Black--Scholes is impossible under realistic spreads, requiring markup that exceeds the model price by a spread-dependent premium.

### **Breakdown of Continuous-Time Hedging**
The Black--Scholes hedging argument requires continuous trading, zero costs, continuous paths, known volatility, and no arbitrage -- violation of any assumption breaks perfect replication. **Jump risk** from a jump-diffusion $dS/S = \mu\,dt + \sigma\,dW + J\,dN$ produces hedging error $\epsilon_{\text{jump}} \approx \frac{1}{2}\Gamma S^2 J^2$, quadratic in jump size and occurring discretely and unpredictably. Unlike diffusive error (mean-zero), jump error has **systematic bias** when gamma is signed: $\mathbb{E}[\text{Jump HE}] \approx \frac{1}{2}\lambda_J \int_0^T \Gamma S^2 \sigma_J^2\,dt$. The minimum hedging error variance achievable with continuous delta hedging in a jump-diffusion sets a **floor** on unhedgeable risk: $\text{Var}_{\min}(\text{HE}) = \lambda_J\,\mathbb{E}[(\frac{1}{2}\Gamma S^2 J^2)^2]$. In models such as Merton jump-diffusion and variance gamma, perfect replication is impossible and markets are fundamentally incomplete.

### **Robustness vs. Optimality**
Optimal strategies are model-dependent and potentially fragile, while robust strategies trade some optimality for stability under model uncertainty. **Robust pricing bounds** compute $\underline{V} \leq V_{\text{true}} \leq \overline{V}$ across an uncertainty set of models, with width $\overline{V} - \underline{V} \approx \nu \cdot (\sigma_{\max} - \sigma_{\min})$ indicating model sensitivity. **Worst-case hedging** chooses $\Delta^* = \arg\min_\Delta \max_\sigma \text{HedgingError}(\Delta, \sigma)$, often yielding the average delta $\frac{1}{2}(\Delta(\sigma_{\min}) + \Delta(\sigma_{\max}))$. Stress testing across models (Black--Scholes, local vol, Heston, jump-diffusion, SABR) ensures bounded losses, while **robust Greeks** reported as ranges ($\Delta \in [\Delta_{\min}, \Delta_{\max}]$) reflect calibration and model-choice ambiguity. Model risk capital $\alpha \times (\overline{V} - \underline{V})$ quantifies regulatory reserves for model uncertainty.

### **Hedging in Incomplete Markets**
When markets are incomplete -- due to stochastic volatility, jumps, or illiquid hedging instruments -- perfect replication is impossible and the choice of hedge involves a risk-return trade-off. The theoretical framework addresses this through multiple complementary approaches including the Follmer--Schweizer decomposition, which provides the canonical decomposition of any contingent claim into a hedgeable martingale component and an orthogonal residual risk.

### **Mean-Variance Hedging**
Mean-variance hedging minimizes the expected squared replication error $\mathbb{E}[(V_T - \Pi_T)^2]$ over all self-financing strategies, yielding a modified delta that accounts for the correlation between the option and available hedging instruments. The variance-optimal hedge in stochastic volatility models such as Heston reduces to the Black--Scholes delta plus a correction proportional to the vol-of-vol and the correlation $\rho$.

### **Quadratic Hedging**
Quadratic hedging under the minimal martingale measure preserves the martingale property of hedging gains while minimizing tracking error, providing a mathematically rigorous framework for systematic risk decomposition in incomplete markets.

### **Utility-Based Hedging**
Utility-based hedging maximizes $\mathbb{E}[U(\Pi_T)]$ for a given utility function $U$, with the **indifference price** emerging as the certainty-equivalent valuation. In the limit of zero risk aversion, utility-based hedging recovers superreplication; in the limit of infinite risk aversion, it reduces to mean-variance hedging. This approach provides a coherent framework for incorporating risk preferences into hedging decisions when perfect replication is unattainable.

!!! note "Role in the Book"
    Hedging theory connects the Greeks (Chapter 10) to practical risk management (Chapter 22). The delta hedging argument underpins the Black--Scholes derivation (Chapter 6), discrete hedging error analysis motivates the study of transaction costs and volatility uncertainty, and incomplete market hedging provides the practical framework for models with stochastic volatility (Chapter 14) and jumps (Chapter 7). Robust hedging and pricing bounds developed here lead naturally to the superhedging and duality theory in Chapter 13.

---
