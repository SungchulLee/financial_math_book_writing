# Chapter 11: Hedging

This chapter develops the theory and practice of hedging derivative positions, progressing from the idealized continuous-time delta hedge through the reality of discrete rebalancing, transaction costs, and model misspecification, to optimal hedging in incomplete markets. The central tension—between the theoretical perfection of continuous hedging and the practical constraints of real trading—motivates a hierarchy of hedging strategies with quantifiable error bounds and explicit trade-offs between cost, risk, and model dependence.

## Key Concepts

**Delta Hedging and the Replication Argument**
In the Black-Scholes framework, a European option is perfectly replicated by continuously holding $\Delta_t = \partial V/\partial S$ shares of the underlying and financing the position at the risk-free rate. The self-financing condition ensures that the hedging portfolio $\Pi_t = V_t - \Delta_t S_t$ satisfies $d\Pi_t = r\Pi_t\,dt$, eliminating all stochastic risk. The P&L of a delta-hedged position over an interval $[t, t+dt]$ is $d\text{P\&L} = \frac{1}{2}\Gamma_t S_t^2(\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)\,dt$, revealing that the hedger profits when realized volatility exceeds implied volatility (for a long gamma position) and loses in the opposite case. This **gamma P&L formula** is the fundamental equation connecting hedging to volatility trading.

**Higher-Order Hedging: Gamma and Vega**
Delta hedging alone leaves the portfolio exposed to second-order effects. **Gamma hedging** adds a second instrument (typically another option) to neutralize $\Gamma$, reducing sensitivity to large spot moves and discrete rebalancing error. **Vega hedging** neutralizes $\nu = \partial V/\partial \sigma$, protecting against changes in implied volatility. A portfolio hedged in delta, gamma, and vega solves the linear system

$$\begin{pmatrix} \Delta_1 & \Delta_2 \\ \Gamma_1 & \Gamma_2 \\ \nu_1 & \nu_2 \end{pmatrix} \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = -\begin{pmatrix} \Delta_V \\ \Gamma_V \\ \nu_V \end{pmatrix}$$

requiring at least two hedging instruments beyond the underlying. **Cross-Greeks**—Charm ($\partial\Delta/\partial t$), Vanna ($\partial^2 V/\partial S\partial\sigma$), and Volga ($\partial^2 V/\partial\sigma^2$)—capture second-order interactions between variables and are critical for managing smile risk in portfolios of exotic options. **Theta management** exploits the theta-gamma relation $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV$ to understand time decay as the cost of maintaining convexity.

**Discrete-Time Hedging Error**
In practice, hedging occurs at discrete times $0 = t_0 < t_1 < \cdots < t_N = T$ with interval $\Delta t = T/N$. The cumulative hedging error is

$$\varepsilon_N = \sum_{j=0}^{N-1}\left[\frac{1}{2}\Gamma(t_j, S_{t_j})S_{t_j}^2\bigl((\Delta S_j/S_{t_j})^2 - \sigma^2\Delta t\bigr)\right]$$

For a delta-hedged vanilla option, the variance of the hedging error scales as $\text{Var}(\varepsilon_N) \propto \sigma^4 T/N \cdot \mathbb{E}[\Gamma^2 S^4]$, with the $1/N$ decay reflecting the law of large numbers averaging of independent gamma scalps. Near expiry, the gamma concentration near the strike causes hedging error to spike—the **pin risk** problem. **Asymptotic expansions** (Leland, Wilmott) provide higher-order corrections: the leading hedging error is mean-zero with variance $\mathcal{O}(\Delta t)$, and systematic bias enters at $\mathcal{O}(\Delta t)$ through the discrete gamma-theta imbalance. The **rebalancing frequency** trade-off is explicit: more frequent rebalancing reduces variance but increases transaction costs.

**Model Misspecification and Robustness**
When the true volatility $\sigma_{\text{true}}(t,S)$ differs from the hedging model volatility $\sigma_{\text{model}}$, the hedging error accumulates as $\int_0^T \frac{1}{2}\Gamma_t S_t^2(\sigma_{\text{true}}^2 - \sigma_{\text{model}}^2)\,dt$. The El Karoui-Jeanblanc-Shreve result shows that if $\sigma_{\text{model}} \geq \sigma_{\text{true}}$ everywhere, the seller's delta hedge in the overestimated model **superreplicates** the option—providing a robust, model-free bound. Transaction costs modify the effective hedging equation: the Leland bandwidth $\delta S \propto \sqrt{k\,\Delta t}$ defines the no-trade zone around the delta-neutral position, and the Hoggard-Whalley-Wilmott analysis derives the optimal rebalancing threshold that minimizes the combined cost of hedging error and trading. **Bid-ask spread** effects further widen the no-trade band and introduce a fundamental asymmetry between long and short gamma positions.

**Hedging in Incomplete Markets**
When markets are incomplete—due to stochastic volatility, jumps, or illiquid hedging instruments—perfect replication is impossible and the choice of hedge involves a risk-return trade-off. **Mean-variance hedging** minimizes $\mathbb{E}[(V_T - \Pi_T)^2]$ over all self-financing strategies, yielding a modified delta that accounts for the correlation between the option and the available hedging instruments. The **variance-optimal** hedge in the Heston model reduces to the Black-Scholes delta plus a correction proportional to the vol-of-vol and the correlation $\rho$. **Quadratic hedging** under the minimal martingale measure preserves the martingale property of hedging gains while minimizing tracking error. **Utility-based hedging** maximizes $\mathbb{E}[U(\Pi_T)]$ for a given utility function $U$, with the indifference price emerging as the certainty-equivalent valuation. In the limit of zero risk aversion, utility-based hedging recovers superreplication; in the limit of infinite risk aversion, it reduces to mean-variance hedging. The **Föllmer-Schweizer decomposition** provides the canonical decomposition of any contingent claim into a hedgeable martingale component and an orthogonal residual risk.

!!! note "Role in the Book"
    Hedging theory connects the Greeks (Chapter 10) to practical risk management (Chapter 22). The delta hedging argument underpins the Black-Scholes derivation (Chapter 6), discrete hedging error analysis motivates the study of transaction costs and volatility uncertainty, and incomplete market hedging provides the practical framework for models with stochastic volatility (Chapter 14) and jumps (Chapter 7).

---
