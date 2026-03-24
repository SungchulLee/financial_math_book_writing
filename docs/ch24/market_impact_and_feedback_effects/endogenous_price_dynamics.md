# Endogenous Price Dynamics


In modern financial markets, prices are not purely exogenous processes. **Endogenous price dynamics** arise when trading activity itself influences prices.

---

## Exogenous vs endogenous views


Traditional models assume:
- prices driven by external information,
- agents as price takers.

In reality:
- large trades move prices,
- strategies interact through markets,
- feedback loops emerge.

---

## Market impact as endogeneity


Trading generates:
- temporary impact through order-book pressure,
- permanent impact through information revelation.

As a result, price dynamics depend on market participants’ actions.

---

## Implications for modeling


Endogenous dynamics imply:
- violations of martingale assumptions,
- strategy-dependent returns,
- path dependence of prices.

Models must incorporate impact and feedback.

---

## Financial applications


Endogeneity matters for:
- optimal execution,
- high-frequency trading,
- systemic risk analysis.

Ignoring it leads to underestimated risk.

---

## Key takeaways


- Prices are shaped by trading behavior.
- Market impact creates feedback loops.
- Endogeneity challenges classical assumptions.

---

## Further reading


- Bouchaud et al., market impact.
- Farmer et al., endogenous markets.

---

## Exercises

**Exercise 1.** Consider a stock with fundamental value $V_t = V_0 + \sigma_V W_t$ and market price $S_t = V_t + I_t$, where $I_t$ is the aggregate market impact from trading. A large trader liquidates $Q$ shares using a constant rate $v = Q/T$ over $[0,T]$. Temporary impact is $\eta v$ and permanent impact accumulates as $g \int_0^t v \, ds = g v t$. (a) Compute $S_T - V_T$ at the end of liquidation. (b) Explain why the price path is no longer a martingale under the physical measure when impact is present. (c) If a second trader observes the price trend caused by the liquidation and sells (front-runs), describe the feedback loop that amplifies the price decline.

---

**Exercise 2.** In the Kyle (1985) model, an informed trader, noise traders, and a market maker interact. The price is set as $S_t = \lambda (X_t + U_t)$ where $X_t$ is the informed order flow and $U_t$ is noise flow. (a) Explain how the market maker's pricing rule makes the price endogenous: it depends on the order flow, which in turn depends on the price. (b) In equilibrium, $\lambda = \sigma_V / (2\sigma_U)$. Show that higher noise trading ($\sigma_U$) reduces price impact, providing more camouflage for the informed trader. (c) Discuss how this model captures information revelation as a form of permanent impact.

---

**Exercise 3.** Volatility targeting strategies adjust exposure to maintain a constant portfolio volatility: $w_t = \sigma_{\text{target}} / \hat{\sigma}_t$, where $\hat{\sigma}_t$ is the estimated volatility. (a) When the market drops and $\hat{\sigma}_t$ increases, what happens to $w_t$? Show that this forces selling. (b) If many funds use this strategy simultaneously, explain how the selling pressure further depresses prices and increases volatility, creating a feedback loop: drop $\to$ higher $\hat{\sigma}$ $\to$ selling $\to$ further drop. (c) Model this as a fixed-point problem: the equilibrium volatility $\sigma^*$ must be consistent with the aggregate selling pressure. Under what conditions does a stable equilibrium exist?

---

**Exercise 4.** A fire sale occurs when a distressed institution sells assets at below-fundamental-value prices, causing mark-to-market losses at other institutions. (a) Let bank $i$ hold a portfolio with asset $j$ in quantity $a_{ij}$. If bank 1 sells $\Delta$ units of asset $j$, the price drops by $\delta_j = f(\Delta)$. Compute the mark-to-market loss at bank 2 holding $a_{2j}$ units. (b) If this loss forces bank 2 to sell assets (e.g., due to leverage constraints), describe the contagion cascade. (c) Explain why this endogenous feedback is absent in models that treat prices as exogenous, and how it leads to underestimation of systemic risk.

---

**Exercise 5.** The Almgren-Chriss framework treats permanent impact as exogenous: $dS_t = \sigma dW_t - g v_t dt$. In the mean field game framework, permanent impact is endogenous: $dS_t = \sigma dW_t - g N \bar{v}_t dt$. (a) Explain the conceptual difference: in the exogenous model, the trader takes $g$ as given; in the endogenous model, the effective impact depends on what all traders do in equilibrium. (b) In the endogenous model, if all traders accelerate their execution, how does this change $\bar{v}_t$ and hence the price dynamics? (c) Discuss why regulators should prefer endogenous models for assessing market stability: they capture the amplification effects that exogenous models miss.

---

**Exercise 6.** Consider a market with $N$ momentum traders who buy when prices rise and sell when prices fall: $v_t^i = \alpha (S_t - S_{t-1})$ for each trader $i$. The price is $S_t = V_t + \eta \sum_i v_t^i$ where $V_t$ is the fundamental value. (a) Substitute the trading rule into the price equation and show that the resulting price dynamics exhibit positive feedback: $S_t - V_t = \frac{N \alpha \eta}{1 - N \alpha \eta}(V_t - V_{t-1})$ (assuming $N\alpha\eta < 1$). (b) Explain what happens when $N\alpha\eta \ge 1$: the system becomes unstable. (c) Relate this to the flash crash of 2010, where algorithmic trading contributed to a rapid price decline and recovery.
