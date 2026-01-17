# Market Impact Theory: Derivation of the Square Root Law


This appendix provides the theoretical foundation for the market impact models used in Chapter 26, addressing the square root relationship between order size and price impact that governs execution costs in cryptocurrency markets.

---

## Theoretical Foundations


### The Kyle (1985) Model


**Setup:**

Kyle's seminal model establishes the linear price impact relationship through strategic informed trading:

**Market participants:**
- Informed trader: Knows true value $V$
- Noise traders: Trade randomly with volume $U \sim N(0, \sigma_u^2)$
- Market maker: Sets prices, observes total order flow

**Information structure:**
- True value: $V \sim N(P_0, \Sigma_0)$ (initial uncertainty)
- Informed trader submits order $X$
- Market maker observes total flow: $Y = X + U$

**Market maker pricing:**

The market maker sets price equal to expected value given order flow:

$$
P = E[V | Y] = P_0 + \lambda Y
$$

Where $\lambda$ is the **Kyle's lambda** (price impact coefficient):

$$
\lambda = \frac{\Sigma_0}{2\sigma_u}
$$

**Interpretation:**
- Higher uncertainty ($\Sigma_0$) → Higher impact (more information in each trade)
- Higher noise volume ($\sigma_u$) → Lower impact (trades hidden in noise)

**Linear impact:**

$$
\Delta P = \lambda \cdot Q
$$

This predicts linear relationship between order size $Q$ and price impact.


### Why Square Root Empirically?


**Empirical observation contradicts linear:**

Actual data shows:

$$
\text{Impact} \propto Q^{0.5}
$$

Not $Q^{1.0}$ as Kyle predicts.

**Resolution: Market microstructure dynamics**

The square root emerges from:
1. Order splitting over time
2. Liquidity replenishment
3. Multi-period optimization

---

## The Almgren-Chriss (2001) Framework


### Optimal Execution Problem


**Setup:**

Trader must execute $X$ shares over time horizon $T$, minimizing:

$$
\min_{x(t)} \quad E[\text{Cost}] + \gamma \cdot \text{Var}[\text{Cost}]
$$

Where:
- $x(t)$ = trading rate (shares per unit time)
- $\gamma$ = risk aversion parameter
- Cost includes permanent and temporary impact

**Position dynamics:**

$$
\frac{dQ}{dt} = -x(t), \quad Q(0) = X, \quad Q(T) = 0
$$

**Price dynamics:**

$$
dP_t = \sigma dW_t + g(x_t) dt + h(x_t)
$$

Where:
- $\sigma dW_t$ = Random price movement (volatility)
- $g(x_t)$ = **Permanent impact** (persists after trade)
- $h(x_t)$ = **Temporary impact** (reverts after trade)


### Impact Function Specifications


**Linear temporary impact:**

$$
h(x) = \eta \cdot x
$$

Cost of immediacy—higher trading rate, higher slippage.

**Linear permanent impact:**

$$
g(x) = \gamma \cdot x
$$

Information revealed moves price permanently.

**Total impact cost:**

$$
\text{Impact Cost} = \int_0^T \left[ g(x_t) \cdot Q_t + h(x_t) \cdot x_t \right] dt
$$


### Optimal Trading Trajectory


**Solution (risk-neutral case, $\gamma = 0$):**

$$
x^*(t) = \frac{X}{T}
$$

Constant trading rate (TWAP)—when no risk aversion, spread evenly.

**Solution (with risk aversion):**

$$
x^*(t) = \frac{\kappa X}{\sinh(\kappa T)} \cosh(\kappa(T-t))
$$

Where $\kappa = \sqrt{\gamma \sigma^2 / \eta}$.

**Interpretation:**
- Trade more at beginning when uncertainty highest
- Reduce rate as position decreases
- Higher volatility ($\sigma$) → Trade faster

---

## Derivation of Square Root Law


### The Dimensional Analysis Argument


**Key insight:** Impact depends on three quantities:

1. Order size: $Q$ (shares)
2. Daily volume: $V$ (shares/day)
3. Daily volatility: $\sigma$ (dimensionless, e.g., 3%)

**Dimensional analysis:**

Impact is a fraction (dimensionless), so:

$$
\text{Impact} = f\left(\frac{Q}{V}\right) \cdot \sigma
$$

The function $f$ must be dimensionless.

**Market microstructure constraint:**

Consider limit: Large $Q$ relative to $V$ should not imply infinite impact (market would attract liquidity).

This suggests:

$$
f(x) \sim x^\alpha, \quad 0 < \alpha < 1
$$

**Empirical finding:** $\alpha \approx 0.5$ (square root)


### The Random Walk Argument


**Price as random walk:**

$$
P_t = P_0 + \sigma \sqrt{t} \cdot Z, \quad Z \sim N(0,1)
$$

**Trading over time $T$:**

If we trade $Q$ over time $T$, participation rate:

$$
\rho = \frac{Q}{V \cdot T}
$$

**Impact accumulated:**

Impact builds as our trades consistently push price:

$$
\text{Impact} \approx \sigma \sqrt{T} \cdot \rho
$$

Substituting $T = Q / (\rho V)$:

$$
\text{Impact} \approx \sigma \sqrt{\frac{Q}{\rho V}} \cdot \rho = \sigma \sqrt{\frac{Q \cdot \rho}{V}}
$$

**For constant participation rate $\rho$:**

$$
\text{Impact} = \sigma \sqrt{\rho} \cdot \sqrt{\frac{Q}{V}}
$$

**Collecting constants:**

$$
\boxed{\text{Impact} = \sigma \cdot \sqrt{\frac{Q}{V}}}
$$

This is the **Square Root Law**.


### The Information Revelation Argument


**Kyle extension to continuous trading:**

As trade reveals information, price adjusts:

$$
dP = \lambda \cdot dQ
$$

**But $\lambda$ is not constant:**

As we trade, remaining information in our order decreases:

$$
\lambda(t) \propto \sqrt{\text{Remaining Position}}
$$

**Integrating:**

Total impact from trading $Q$:

$$
\text{Impact} = \int_0^Q \lambda(q) dq \propto \int_0^Q \sqrt{Q - q} dq
$$

This yields:

$$
\text{Impact} \propto Q^{1/2}
$$

---

## Empirical Calibration for Crypto


### Data Sources


**Historical studies (traditional markets):**
- Almgren et al. (2005): $\alpha = 0.6$ for equities
- Tóth et al. (2011): $\alpha = 0.5$ confirmed across markets

**Crypto studies:**
- Crypto markets show similar square root behavior
- Higher volatility increases coefficient
- Lower liquidity increases coefficient


### Calibrated Model for Crypto


**Standard form:**

$$
\text{Impact} = A \cdot \sigma \cdot \left(\frac{Q}{V}\right)^\alpha + \frac{s}{2}
$$

Where:
- $A$ = Market-specific constant (1.0-2.0 for crypto)
- $\sigma$ = Daily volatility
- $Q/V$ = Participation rate
- $\alpha$ = Exponent (typically 0.5)
- $s/2$ = Half spread (bid-ask cost)

**Example calibration (BTC):**

| Parameter | Value | Source |
|-----------|-------|--------|
| $A$ | 1.5 | Fitted to execution data |
| $\sigma$ | 3% | 30-day realized vol |
| $V$ | 50,000 BTC | Daily volume |
| $\alpha$ | 0.5 | Empirical |
| $s$ | 0.02% | Typical spread |


### Example Calculations


**Order: 100 BTC ($4.3M at $43,000)**

$$
\text{Impact} = 1.5 \times 0.03 \times \sqrt{\frac{100}{50000}} + \frac{0.0002}{2}
$$

$$
\text{Impact} = 1.5 \times 0.03 \times \sqrt{0.002} + 0.0001
$$

$$
\text{Impact} = 0.045 \times 0.0447 + 0.0001 = 0.00201 + 0.0001 = 0.211\%
$$

**Cost:** 0.211% × $4.3M = **$9,100**


**Order: 500 BTC ($21.5M)**

$$
\text{Impact} = 1.5 \times 0.03 \times \sqrt{\frac{500}{50000}} + 0.0001 = 0.00448 + 0.0001 = 0.458\%
$$

**Cost:** 0.458% × $21.5M = **$98,500**

**Note:** 5× order size → 2.17× impact (square root scaling).

---

## Extensions and Refinements


### Time-Varying Impact


**Intraday volume pattern:**

Crypto volume varies by hour (US/EU overlap highest):

$$
V(t) = V_{\text{avg}} \cdot f(t)
$$

Where $f(t)$ is hourly volume factor.

**Adjusted impact:**

$$
\text{Impact}(t) = A \cdot \sigma \cdot \sqrt{\frac{Q}{V(t)}}
$$

Trading during high-volume hours reduces impact.


### Volatility-Adjusted Impact


**During high volatility:**

$$
A_{\text{high vol}} = A_{\text{base}} \times \left(\frac{\sigma_{\text{current}}}{\sigma_{\text{avg}}}\right)^{0.5}
$$

Impact increases with volatility (liquidity providers widen quotes).

**Example:**

Normal vol: 60%, current vol: 120%

$$
A_{\text{adjusted}} = 1.5 \times \left(\frac{1.2}{0.6}\right)^{0.5} = 1.5 \times 1.41 = 2.12
$$

Impact ~40% higher during vol spikes.


### Cross-Venue Execution


**Liquidity aggregation:**

If trading across $n$ venues with volumes $V_1, ..., V_n$:

**Optimal allocation (minimize total impact):**

$$
Q_i^* = Q \times \frac{\sqrt{V_i}}{\sum_j \sqrt{V_j}}
$$

Allocate proportional to square root of volume (not linearly).

**Example:**

$Q = 100$ BTC across Binance ($V_1 = 20K$), Coinbase ($V_2 = 8K$), Kraken ($V_3 = 5K$)

$$
Q_1^* = 100 \times \frac{\sqrt{20000}}{\sqrt{20000} + \sqrt{8000} + \sqrt{5000}} = 100 \times \frac{141}{141 + 89 + 71} = 47 \text{ BTC}
$$

$$
Q_2^* = 100 \times \frac{89}{301} = 30 \text{ BTC}
$$

$$
Q_3^* = 100 \times \frac{71}{301} = 23 \text{ BTC}
$$

---

## Practical Implications


### Position Sizing Based on Impact


**Maximum position without excessive impact:**

Setting impact threshold (e.g., 0.5% max):

$$
Q_{\max} = V \times \left(\frac{\text{Impact}_{\max}}{A \cdot \sigma}\right)^2
$$

**Example:**

Max 0.5% impact, $V = 50000$, $A = 1.5$, $\sigma = 3\%$:

$$
Q_{\max} = 50000 \times \left(\frac{0.005}{1.5 \times 0.03}\right)^2 = 50000 \times (0.111)^2 = 617 \text{ BTC}
$$


### Execution Time Optimization


**Trade-off:** Slower execution reduces impact but increases timing risk.

**Optimal time:**

$$
T^* = \sqrt{\frac{Q \cdot \eta}{V \cdot \gamma \cdot \sigma^2}}
$$

Where $\eta$ = temporary impact, $\gamma$ = risk aversion.

Higher volatility → Trade faster (accept impact to reduce timing risk).


### VWAP vs TWAP Selection


**Use TWAP when:**
- Volume profile flat
- Information leakage concern low
- Simple execution preferred

**Use VWAP when:**
- Volume profile variable (crypto: EU/US overlap higher)
- Tracking benchmark matters
- Lower impact preferred (follow liquidity)

---

## Summary of Key Formulas


**Square Root Law:**

$$
\text{Impact} = \sigma \cdot \sqrt{\frac{Q}{V}}
$$

**Calibrated Crypto Model:**

$$
\text{Impact} = A \cdot \sigma \cdot \left(\frac{Q}{V}\right)^{0.5} + \frac{s}{2}
$$

**Multi-Venue Allocation:**

$$
Q_i^* \propto \sqrt{V_i}
$$

**Maximum Position (impact threshold):**

$$
Q_{\max} = V \times \left(\frac{\text{Impact}_{\max}}{A \cdot \sigma}\right)^2
$$

---

## References


1. Kyle, A. S. (1985). "Continuous Auctions and Insider Trading." *Econometrica*, 53(6), 1315-1335.

2. Almgren, R., & Chriss, N. (2001). "Optimal Execution of Portfolio Transactions." *Journal of Risk*, 3(2), 5-39.

3. Almgren, R., Thum, C., Hauptmann, E., & Li, H. (2005). "Direct Estimation of Equity Market Impact." *Risk*, 18(7), 58-62.

4. Tóth, B., Lemperiere, Y., Deremble, C., De Lataillade, J., Kockelkoren, J., & Bouchaud, J. P. (2011). "Anomalous Price Impact and the Critical Nature of Liquidity in Financial Markets." *Physical Review X*, 1(2), 021006.

5. Gatheral, J. (2010). "No-Dynamic-Arbitrage and Market Impact." *Quantitative Finance*, 10(7), 749-759.

---

*Appendix to Chapter 26: Digital Assets*
*Theoretical Foundations for Market Impact Analysis*
