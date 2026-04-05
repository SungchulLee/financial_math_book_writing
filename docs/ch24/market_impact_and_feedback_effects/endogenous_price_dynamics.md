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

??? success "Solution to Exercise 1"
    **(a)** The market price is $S_t = V_t + I_t$ where $I_t$ has a temporary component $\eta v$ and a permanent component $g v t$. At $t = T$, the temporary impact vanishes (trading has stopped), so:

    $$
    S_T - V_T = g v T = g \cdot \frac{Q}{T} \cdot T = gQ
    $$

    The permanent impact at the end of liquidation is $gQ$, which depends only on the total quantity traded, not on the rate.

    **(b)** Under the physical measure with no trading, the fundamental value $V_t = V_0 + \sigma_V W_t$ is a martingale. However, the market price satisfies:

    $$
    S_t = V_t + \eta v + g v t = V_0 + \sigma_V W_t + \eta v + g v t
    $$

    The term $gvt = g(Q/T)t$ is a deterministic, linearly increasing function of time (in magnitude, it represents a downward drift since the trader is selling). Therefore:

    $$
    \mathbb{E}[S_{t+s} \mid \mathcal{F}_t] = S_t + gv \cdot s \neq S_t
    $$

    The conditional expectation has a non-zero drift, violating the martingale property. The impact-induced drift makes the price predictable, which is incompatible with the martingale assumption.

    **(c)** The feedback loop operates as follows:

    1. **Initial liquidation**: The large trader sells at rate $v = Q/T$, causing a price decline due to both temporary ($\eta v$) and permanent ($gvt$) impact.
    2. **Signal detection**: The second trader observes the downward price trend and interprets it as information (or simply follows the momentum). This trader begins to sell as well.
    3. **Amplified selling pressure**: The combined selling rate is now $v_{\text{total}} = v + v_{\text{front-runner}}$, which increases both the temporary and permanent impact components.
    4. **Accelerated price decline**: The steeper price decline reinforces the second trader's signal, encouraging even more aggressive selling.
    5. **Cascade**: The feedback loop between selling $\to$ price decline $\to$ more selling continues, potentially causing the price to overshoot below the fundamental value by a margin far exceeding the original impact $gQ$.

    This is a positive feedback loop: the endogenous price movement caused by trading generates additional trading, which amplifies the price movement beyond what the original liquidation alone would produce.

---

**Exercise 2.** In the Kyle (1985) model, an informed trader, noise traders, and a market maker interact. The price is set as $S_t = \lambda (X_t + U_t)$ where $X_t$ is the informed order flow and $U_t$ is noise flow. (a) Explain how the market maker's pricing rule makes the price endogenous: it depends on the order flow, which in turn depends on the price. (b) In equilibrium, $\lambda = \sigma_V / (2\sigma_U)$. Show that higher noise trading ($\sigma_U$) reduces price impact, providing more camouflage for the informed trader. (c) Discuss how this model captures information revelation as a form of permanent impact.

??? success "Solution to Exercise 2"
    **(a)** In the Kyle model, the market maker sets the price as a function of the total order flow $Y_t = X_t + U_t$:

    $$
    S_t = \lambda Y_t = \lambda(X_t + U_t)
    $$

    The informed trader's order flow $X_t$ depends on the pricing rule: the informed trader chooses how aggressively to trade based on the price impact parameter $\lambda$. Specifically, the informed trader maximizes:

    $$
    \mathbb{E}\left[(V - S_t) X_t\right] = \mathbb{E}\left[(V - \lambda(X_t + U_t)) X_t\right]
    $$

    The first-order condition gives $X_t = (V - \lambda U_t)/(2\lambda)$, which depends on $\lambda$. Simultaneously, $\lambda$ is chosen by the market maker to ensure $S_t = \mathbb{E}[V \mid Y_t]$, which depends on $X_t$. This circular dependence---the price depends on order flow, and order flow depends on the price---makes the price endogenous.

    **(b)** In equilibrium, the Kyle lambda is:

    $$
    \lambda = \frac{\sigma_V}{2\sigma_U}
    $$

    When noise trading volatility $\sigma_U$ increases:

    $$
    \frac{\partial \lambda}{\partial \sigma_U} = -\frac{\sigma_V}{2\sigma_U^2} < 0
    $$

    Higher $\sigma_U$ reduces $\lambda$, meaning each unit of order flow moves the price less. The economic intuition is that more noise trading provides **camouflage** for the informed trader: the market maker cannot easily distinguish informed trades from noise, so they set a lower price impact. This allows the informed trader to trade more aggressively while revealing less information per unit traded.

    **(c)** In the Kyle model, permanent impact arises through information revelation. The market maker observes the total order flow $Y_t$ and updates the price to reflect the inferred fundamental value:

    $$
    S_t = \mathbb{E}[V \mid Y_t] = \lambda Y_t
    $$

    As the informed trader submits orders over time, information is gradually incorporated into the price. The cumulative permanent impact is the total information revealed:

    $$
    S_T = \lambda(X_T + U_T)
    $$

    In expectation, $\mathbb{E}[U_T] = 0$, so $\mathbb{E}[S_T] = \lambda \mathbb{E}[X_T]$, and the permanent price change reflects the information content of the informed trader's cumulative order flow. Unlike mechanical impact (which might decay), information-based impact is permanent because the price update reflects a genuine update in the market's assessment of fundamental value.

---

**Exercise 3.** Volatility targeting strategies adjust exposure to maintain a constant portfolio volatility: $w_t = \sigma_{\text{target}} / \hat{\sigma}_t$, where $\hat{\sigma}_t$ is the estimated volatility. (a) When the market drops and $\hat{\sigma}_t$ increases, what happens to $w_t$? Show that this forces selling. (b) If many funds use this strategy simultaneously, explain how the selling pressure further depresses prices and increases volatility, creating a feedback loop: drop $\to$ higher $\hat{\sigma}$ $\to$ selling $\to$ further drop. (c) Model this as a fixed-point problem: the equilibrium volatility $\sigma^*$ must be consistent with the aggregate selling pressure. Under what conditions does a stable equilibrium exist?

??? success "Solution to Exercise 3"
    **(a)** Each fund maintains exposure $w_t = \sigma_{\text{target}} / \hat{\sigma}_t$. When the market drops:

    - Realized volatility increases, so $\hat{\sigma}_t$ rises.
    - The weight decreases: $w_{t+\Delta t} = \sigma_{\text{target}} / \hat{\sigma}_{t+\Delta t} < w_t$.
    - The fund must reduce its equity position from $w_t$ to $w_{t+\Delta t}$, which requires selling.

    The change in weight is:

    $$
    \Delta w = w_{t+\Delta t} - w_t = \sigma_{\text{target}}\left(\frac{1}{\hat{\sigma}_{t+\Delta t}} - \frac{1}{\hat{\sigma}_t}\right) < 0
    $$

    Since the fund's equity position is $w_t \times \text{AUM}$, the dollar amount sold is $|\Delta w| \times \text{AUM}$. This demonstrates that volatility-targeting strategies are inherently **procyclical**: they sell after price drops and buy after price rises.

    **(b)** With many funds using the same strategy simultaneously:

    1. **Market drop** $\to$ $\hat{\sigma}$ increases for all funds.
    2. **All funds sell** $\to$ aggregate selling pressure $= N \times |\Delta w| \times \text{AUM}$.
    3. **Selling pressure depresses prices further** $\to$ larger realized losses.
    4. **Larger losses increase** $\hat{\sigma}$ **further** $\to$ more selling required.
    5. **Repeat**: the cycle amplifies until either the strategy limits are reached, or the selling is absorbed by contrarian buyers.

    This is a positive feedback loop: drop $\to$ higher $\hat{\sigma}$ $\to$ selling $\to$ further drop $\to$ even higher $\hat{\sigma}$ $\to$ more selling $\to \cdots$

    **(c)** Let $\sigma^*$ denote the equilibrium volatility. The total selling pressure at volatility level $\sigma$ is:

    $$
    S(\sigma) = N \cdot \text{AUM} \cdot \sigma_{\text{target}} \cdot \left(\frac{1}{\sigma} - \frac{1}{\sigma_0}\right)
    $$

    where $\sigma_0$ is the pre-shock volatility. This selling pressure causes additional price impact, which raises volatility by an amount $\Delta\sigma(\sigma) = h(S(\sigma))$ for some increasing function $h$. The equilibrium condition is:

    $$
    \sigma^* = \sigma_{\text{shock}} + h\!\left(N \cdot \text{AUM} \cdot \sigma_{\text{target}} \cdot \left(\frac{1}{\sigma^*} - \frac{1}{\sigma_0}\right)\right)
    $$

    where $\sigma_{\text{shock}}$ is the volatility from the initial shock alone (without feedback). This is a fixed-point equation $\sigma^* = F(\sigma^*)$.

    A stable equilibrium exists when the derivative $F'(\sigma^*) < 1$. Since selling pressure $S(\sigma)$ is decreasing in $\sigma$ (at higher volatility, less additional selling is needed), and $h$ is increasing, $F'(\sigma^*)$ involves competing effects. The equilibrium is stable when the feedback sensitivity (proportional to $N \cdot \text{AUM} \cdot h'$) is not too large. If the total AUM in volatility-targeting strategies is too large relative to market liquidity, $F'(\sigma^*) \ge 1$ and no stable equilibrium exists, implying a volatility spiral.

---

**Exercise 4.** A fire sale occurs when a distressed institution sells assets at below-fundamental-value prices, causing mark-to-market losses at other institutions. (a) Let bank $i$ hold a portfolio with asset $j$ in quantity $a_{ij}$. If bank 1 sells $\Delta$ units of asset $j$, the price drops by $\delta_j = f(\Delta)$. Compute the mark-to-market loss at bank 2 holding $a_{2j}$ units. (b) If this loss forces bank 2 to sell assets (e.g., due to leverage constraints), describe the contagion cascade. (c) Explain why this endogenous feedback is absent in models that treat prices as exogenous, and how it leads to underestimation of systemic risk.

??? success "Solution to Exercise 4"
    **(a)** Bank 2 holds $a_{2j}$ units of asset $j$. When bank 1's fire sale reduces the price of asset $j$ by $\delta_j = f(\Delta)$, bank 2's mark-to-market loss is:

    $$
    L_2 = a_{2j} \cdot \delta_j = a_{2j} \cdot f(\Delta)
    $$

    If bank 2 holds multiple assets also sold by bank 1, the total loss is $L_2 = \sum_j a_{2j} \cdot f(\Delta_j)$, where $\Delta_j$ is the quantity of asset $j$ sold by bank 1 and $f$ is the price impact function.

    **(b)** The contagion cascade proceeds as follows:

    1. **Round 1**: Bank 1 (distressed) sells $\Delta$ units of asset $j$. Price drops by $\delta_j = f(\Delta)$.
    2. **Mark-to-market**: Bank 2 suffers loss $L_2 = a_{2j} \delta_j$. If bank 2 has leverage $\ell_2$, its equity is reduced by $L_2$, and its leverage ratio increases.
    3. **Leverage constraint**: If the new leverage exceeds the regulatory or risk limit, bank 2 must sell assets to delever. The required asset sale is approximately $\ell_2 \cdot L_2$.
    4. **Round 2**: Bank 2's selling causes price drops in other assets, say $\delta_k$ for asset $k$. Now bank 3, holding asset $k$, suffers mark-to-market losses $L_3 = a_{3k} \delta_k$.
    5. **Cascade continues**: Each round of forced selling triggers further mark-to-market losses at other institutions, which may trigger further forced selling.

    The cascade is amplified by: (i) high leverage ($\ell$ large), (ii) concentrated holdings (large $a_{ij}$), and (iii) illiquid markets (large $f$). The total loss to the system can be a large multiple of the initial distress at bank 1.

    **(c)** In models with exogenous prices, asset prices follow prescribed stochastic processes (e.g., GBM) regardless of market participants' actions. In such models:

    - Bank 1's fire sale has no effect on prices.
    - Bank 2 experiences no mark-to-market loss from bank 1's selling.
    - There is no contagion cascade.

    This leads to a fundamental underestimation of systemic risk. The total loss in the exogenous model is just bank 1's loss, while in the endogenous model it is bank 1's loss multiplied by a cascade amplification factor that depends on network structure, leverage, and illiquidity. The 2008 financial crisis demonstrated this dramatically: models that treated asset prices as exogenous failed to predict that mortgage losses at a few institutions could cascade into a system-wide crisis through precisely this fire-sale feedback mechanism.

---

**Exercise 5.** The Almgren-Chriss framework treats permanent impact as exogenous: $dS_t = \sigma dW_t - g v_t dt$. In the mean field game framework, permanent impact is endogenous: $dS_t = \sigma dW_t - g N \bar{v}_t dt$. (a) Explain the conceptual difference: in the exogenous model, the trader takes $g$ as given; in the endogenous model, the effective impact depends on what all traders do in equilibrium. (b) In the endogenous model, if all traders accelerate their execution, how does this change $\bar{v}_t$ and hence the price dynamics? (c) Discuss why regulators should prefer endogenous models for assessing market stability: they capture the amplification effects that exogenous models miss.

??? success "Solution to Exercise 5"
    **(a)** In the **exogenous** Almgren-Chriss model:

    $$
    dS_t = \sigma\, dW_t - g\, v_t\, dt
    $$

    Here, $g$ is a fixed parameter. The trader takes $g$ as given and optimizes $v_t$ without considering how other traders affect the price. The price impact is a **unilateral** effect of one trader's actions.

    In the **endogenous** mean field game model:

    $$
    dS_t = \sigma\, dW_t - g\, N\, \bar{v}_t\, dt
    $$

    The drift term $gN\bar{v}_t$ depends on the average trading rate $\bar{v}_t$ of all $N$ traders. Each trader's optimal strategy contributes to $\bar{v}_t$, which in turn affects every trader's price dynamics. The price impact is a **collective, equilibrium** outcome: it is determined by what all traders do, and what all traders do depends on the price dynamics they face.

    **(b)** If all traders accelerate their execution (increase $v_t^i$ uniformly), the average trading rate $\bar{v}_t$ increases. The price dynamics become:

    $$
    dS_t = \sigma\, dW_t - g\, N\, \bar{v}_t^{\text{fast}}\, dt
    $$

    The larger drift term $gN\bar{v}_t^{\text{fast}}$ means prices decline faster. This creates a **self-reinforcing** feedback: if each trader believes others are trading faster, they have an incentive to trade faster themselves (to avoid the anticipated price decline), which validates the initial belief. This is the predatory trading effect---strategic interaction leads to accelerated execution compared to the single-agent optimum.

    In equilibrium, $\bar{v}_t$ is determined by the fixed-point condition: each trader's optimal response to $\bar{v}_t$ generates precisely $\bar{v}_t$ when averaged across all traders.

    **(c)** Regulators should prefer endogenous models because:

    1. **Amplification effects**: Exogenous models treat price impact as fixed and independent of other market participants. They miss the amplification that occurs when many traders execute similar strategies simultaneously. The endogenous model captures how $\bar{v}_t$ can spike when strategies are correlated.

    2. **Systemic risk**: In the exogenous model, adding more traders to the market has no effect on price dynamics (each trader sees the same $g$). In the endogenous model, the effective impact $gN\bar{v}_t$ scales with the number of traders. Crowded strategies become more dangerous as more participants adopt them.

    3. **Procyclicality**: Endogenous models reveal procyclical feedback loops (e.g., selling $\to$ price decline $\to$ more selling) that exogenous models are structurally unable to capture.

    4. **Stress testing**: For market stability assessment, regulators need to understand worst-case scenarios where feedback effects dominate. Exogenous models systematically underestimate tail risks because they assume away the very feedback mechanisms that generate extreme market events.

---

**Exercise 6.** Consider a market with $N$ momentum traders who buy when prices rise and sell when prices fall: $v_t^i = \alpha (S_t - S_{t-1})$ for each trader $i$. The price is $S_t = V_t + \eta \sum_i v_t^i$ where $V_t$ is the fundamental value. (a) Substitute the trading rule into the price equation and show that the resulting price dynamics exhibit positive feedback: $S_t - V_t = \frac{N \alpha \eta}{1 - N \alpha \eta}(V_t - V_{t-1})$ (assuming $N\alpha\eta < 1$). (b) Explain what happens when $N\alpha\eta \ge 1$: the system becomes unstable. (c) Relate this to the flash crash of 2010, where algorithmic trading contributed to a rapid price decline and recovery.

??? success "Solution to Exercise 6"
    **(a)** Each trader uses the rule $v_t^i = \alpha(S_t - S_{t-1})$, and the price equation is:

    $$
    S_t = V_t + \eta \sum_{i=1}^N v_t^i = V_t + N\alpha\eta(S_t - S_{t-1})
    $$

    Solving for $S_t$:

    $$
    S_t - N\alpha\eta\, S_t = V_t - N\alpha\eta\, S_{t-1}
    $$

    $$
    S_t(1 - N\alpha\eta) = V_t - N\alpha\eta\, S_{t-1}
    $$

    $$
    S_t = \frac{V_t - N\alpha\eta\, S_{t-1}}{1 - N\alpha\eta}
    $$

    Now compute the deviation $S_t - V_t$:

    $$
    S_t - V_t = \frac{V_t - N\alpha\eta\, S_{t-1}}{1 - N\alpha\eta} - V_t = \frac{V_t - N\alpha\eta\, S_{t-1} - V_t(1 - N\alpha\eta)}{1 - N\alpha\eta}
    $$

    $$
    = \frac{N\alpha\eta(V_t - S_{t-1})}{1 - N\alpha\eta}
    $$

    Using $S_{t-1} = V_{t-1} + (S_{t-1} - V_{t-1})$ and assuming the deviation at $t-1$ is small (first-order approximation), we approximate $S_{t-1} \approx V_{t-1}$:

    $$
    S_t - V_t \approx \frac{N\alpha\eta}{1 - N\alpha\eta}(V_t - V_{t-1})
    $$

    This confirms positive feedback: a change in fundamental value $V_t - V_{t-1}$ is amplified by the factor $\frac{N\alpha\eta}{1 - N\alpha\eta}$. A positive fundamental change leads to a price increase that overshoots the fundamental, and vice versa.

    **(b)** When $N\alpha\eta \geq 1$, the denominator $1 - N\alpha\eta \leq 0$, and the system becomes unstable:

    - At $N\alpha\eta = 1$: the denominator is zero, implying infinite amplification---any non-zero fundamental change causes a price divergence.
    - At $N\alpha\eta > 1$: the amplification factor $\frac{N\alpha\eta}{1 - N\alpha\eta}$ is negative and large in magnitude. This means the system has an **explosive feedback loop**: a small positive fundamental change triggers selling (through the destabilized dynamics), which triggers more selling, leading to divergence.

    Formally, the price equation $S_t = \frac{V_t - N\alpha\eta S_{t-1}}{1-N\alpha\eta}$ becomes an unstable difference equation. Small perturbations are amplified rather than dampened, and the price path diverges from fundamentals.

    The critical threshold $N\alpha\eta = 1$ can be understood as: $N$ (number of momentum traders) $\times$ $\alpha$ (aggressiveness of momentum strategy) $\times$ $\eta$ (price impact per unit traded) $= 1$. Instability arises from too many traders, trading too aggressively, in an illiquid market.

    **(c)** The Flash Crash of May 6, 2010, provides a real-world illustration:

    1. **Initial shock**: A large sell order (reportedly from a mutual fund) began executing in the E-mini S&P 500 futures market.
    2. **Momentum feedback**: Algorithmic traders detected the price decline and followed their momentum signals, selling into the falling market. This is exactly the $v_t^i = \alpha(S_t - S_{t-1})$ rule with $S_t - S_{t-1} < 0$ triggering sell orders.
    3. **Amplification**: The selling by momentum algorithms pushed prices down further, triggering more sell signals. The feedback parameter $N\alpha\eta$ effectively exceeded the stability threshold, creating an explosive downward spiral.
    4. **Speed**: The entire crash unfolded in approximately 20 minutes, with the Dow Jones dropping nearly 1,000 points, because algorithmic trading operates on millisecond timescales.
    5. **Recovery**: Once prices deviated sufficiently from fundamentals, contrarian buyers stepped in (acting as negative feedback), and circuit breakers were triggered, restoring stability. The recovery was nearly as rapid as the crash.

    The key lesson is that the stability condition $N\alpha\eta < 1$ can be violated transiently when algorithmic trading activity spikes, even if the market is stable under normal conditions. The endogenous nature of the price dynamics---where algorithmic strategies interact through the price---created a cascade that no individual algorithm intended.
