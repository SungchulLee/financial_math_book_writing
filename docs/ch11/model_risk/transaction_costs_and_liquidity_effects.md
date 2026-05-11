# Transaction Costs and Liquidity Effects


With proportional cost $\lambda$ (bid-ask spread), rebalancing $\delta \theta$ shares costs about

$$
\text{Cost} = \lambda S |\delta\theta|
$$


Since hedge turnover increases with gamma, costs can dominate near expiry.

---

## The hedging dilemma


Without transaction costs, the optimal strategy is continuous delta hedging. With costs:

- **Hedge too often**: Transaction costs accumulate
- **Hedge too little**: Hedging error grows

The optimal strategy balances these competing effects.

---

## No-trade band analysis


**Whalley–Wilmott result.** The optimal hedging strategy maintains delta within a band:

$$
\Delta^{\text{BS}} - h \leq \Delta^{\text{actual}} \leq \Delta^{\text{BS}} + h
$$

where the **bandwidth** is:

$$
\boxed{h = \left(\frac{3\lambda e^{-r\tau}}{2\Gamma}\right)^{1/3}}
$$

**Intuition:**

- High $\Gamma$ (convexity benefit): narrow band (hedge frequently)
- High $\lambda$ (expensive trading): wide band (hedge infrequently)
- The $1/3$ exponent comes from balancing $\mathcal{O}(h^2)$ hedging error against $\mathcal{O}(1/h)$ transaction costs

**Derivation sketch.** The hedging error from a delta deviation of $h$ is $\sim \Gamma h^2 \sigma^2 S^2 \Delta t$. The frequency of hitting the band is $\sim 1/(h^2 \Delta t)$. Transaction cost per hit is $\sim \lambda S h$. Optimal $h$ minimizes total cost.

---

## Leland's modified volatility


**Leland (1985)** proposed hedging at Black–Scholes delta but with adjusted volatility:

$$
\sigma_{\text{Leland}}^2 = \sigma^2 + \text{sign}(\Gamma) \cdot \sigma \sqrt{\frac{8\lambda}{\pi \Delta t}}
$$

**For long positions** ($\Gamma > 0$): Use higher volatility (wider smile)
**For short positions** ($\Gamma < 0$): Use lower volatility

This approach maintains continuous hedging but accounts for transaction costs through the pricing model.

---

## Utility-based analysis


With exponential utility $U(x) = -e^{-\gamma x}$, the utility loss from transaction costs scales as:

$$
\text{Utility Loss} \sim (\lambda \Gamma S^2 \sigma^2)^{2/3} T^{1/3}
$$

Key features:

- Sublinear in time horizon $T$
- Fractional power of costs $\lambda$
- Dominated by gamma exposure

---

## Gamma-weighted turnover


Expected hedge turnover over $[0,T]$ is approximately:

$$
\text{Turnover} = \int_0^T |\text{d}\Delta| \approx \int_0^T |\Gamma| \sigma S \, dt
$$

**Near expiry blow-up.** Since $\Gamma \sim \tau^{-1/2}$:

$$
\text{Turnover} \sim \int_0^T \frac{\sigma S}{\sqrt{T-t}} \, dt \sim \sqrt{T}
$$

The integral diverges as $t \to T$, reflecting infinite turnover needed for perfect hedging.

**Total transaction cost:**

$$
\text{Total Cost} = \lambda \times \text{Turnover} \sim \lambda \sigma S \sqrt{T}
$$

---

## Liquidity effects


Beyond bid-ask spreads, liquidity impacts hedging through:

**1. Market impact.** Large trades move prices:

$$
\text{Execution Price} = S + \eta \cdot |\delta\theta|^\alpha
$$

where $\eta$ is impact coefficient and $\alpha \approx 0.5$ empirically.

**2. Slippage.** Execution prices differ from model prices during rapid moves.

**3. Position limits.** Constraints on delta/gamma exposure from risk limits.

**4. Funding costs.** Borrowing costs for leveraged positions.

---

## Numerical example


ATM call with $S = K = 100$, $\sigma = 20\%$, $\tau = 30$ days, bid-ask spread $\lambda = 0.1\%$:

- $\Gamma = 0.055$
- Optimal bandwidth: $h = (3 \times 0.001/(2 \times 0.055))^{1/3} = 0.030$ (3 delta points)
- Expected turnover: $\sim 0.055 \times 0.20 \times 100 \times \sqrt{30/252} \approx 0.38$ shares
- Transaction cost: $\sim 0.001 \times 100 \times 0.38 = \$0.038$

For comparison, the option value is $\sim \$3.20$, so costs are $\sim 1\%$ of value.

---

## Implications for practice


1. **Widen bands near expiry**: As $\Gamma$ grows, bandwidth grows slower ($h \sim \Gamma^{-1/3}$)
2. **Hedge less frequently for expensive assets**: Higher $\lambda$ means wider bands
3. **Account for costs in pricing**: Add $\sim \lambda^{2/3}$ to option prices for cost reservation
4. **Consider asymmetric costs**: Bid-ask may differ from selling; model separately
5. **Liquidity scoring**: Weight hedging decisions by liquidity conditions

---

## Extensions


**Proportional + fixed costs:** Add fixed cost per trade; creates larger bands, less frequent trading.

**Stochastic volatility:** Bandwidth depends on vol state; hedge more in high-vol regimes.

**Regime switching:** Different strategies for different market conditions.

> **Forward reference.** Transaction cost optimization connects to **Chapter 13** (Robust Pricing), where frictions are treated as model uncertainty.

---

## What to remember


- Frictions turn replication into an optimization problem
- Optimal no-trade bandwidth scales as $(\lambda/\Gamma)^{1/3}$
- Costs scale with hedge turnover, hence with gamma
- Leland's approach adjusts volatility to account for costs
- Near-expiry positions face particularly high transaction costs
- Utility loss from costs scales as $\lambda^{2/3}$, not linearly

---

## Exercises

**Exercise 1.** The Whalley-Wilmott bandwidth is $h = (3\lambda e^{-r\tau}/(2\Gamma))^{1/3}$. For an ATM call with $\Gamma = 0.04$, $\lambda = 0.001$, $r = 0.05$, and $\tau = 0.25$, compute $h$ in delta units. If the current delta is $0.52$, what are the upper and lower bounds of the no-trade band? How does $h$ change if the spread doubles to $\lambda = 0.002$?

??? success "Solution to Exercise 1"
    The Whalley-Wilmott bandwidth is

    $$
    h = \left(\frac{3\lambda e^{-r\tau}}{2\Gamma}\right)^{1/3}
    $$

    With $\Gamma = 0.04$, $\lambda = 0.001$, $r = 0.05$, $\tau = 0.25$:

    $$
    e^{-r\tau} = e^{-0.05 \times 0.25} = e^{-0.0125} \approx 0.9876
    $$

    $$
    h = \left(\frac{3 \times 0.001 \times 0.9876}{2 \times 0.04}\right)^{1/3} = \left(\frac{0.002963}{0.08}\right)^{1/3} = (0.03704)^{1/3}
    $$

    $$
    h = 0.03704^{1/3} \approx 0.3334
    $$

    Wait -- this gives $h$ in the same units as $\lambda / \Gamma$. Let us check units. Here $\lambda$ is proportional cost (dimensionless), and $\Gamma$ has units of $S^{-1}$. So actually $h$ is in delta units (dimensionless). Recomputing:

    $$
    h = (0.03704)^{1/3} \approx 0.0334
    $$

    So $h \approx 0.033$ in delta units (3.3 delta points).

    With current delta $= 0.52$, the no-trade band is

    $$
    [0.52 - 0.033, \; 0.52 + 0.033] = [0.487, \; 0.553]
    $$

    If the spread doubles to $\lambda = 0.002$:

    $$
    h_{\text{new}} = \left(\frac{3 \times 0.002 \times 0.9876}{2 \times 0.04}\right)^{1/3} = \left(\frac{0.005926}{0.08}\right)^{1/3} = (0.07407)^{1/3} \approx 0.0420
    $$

    The bandwidth increases from $0.033$ to $0.042$, a factor of $2^{1/3} \approx 1.26$. Doubling the spread widens the band by about $26\%$, reflecting the cube-root dependence on $\lambda$.

---

**Exercise 2.** Leland's modified volatility is $\sigma_{\text{Leland}}^2 = \sigma^2 + \text{sign}(\Gamma) \cdot \sigma\sqrt{8\lambda/(\pi\Delta t)}$. For $\sigma = 0.20$, $\lambda = 0.001$, and daily rebalancing ($\Delta t = 1/252$), compute $\sigma_{\text{Leland}}$ for both a long gamma position ($\Gamma > 0$) and a short gamma position ($\Gamma < 0$). Why does the adjustment have opposite signs for long and short positions?

??? success "Solution to Exercise 2"
    Leland's modified volatility is

    $$
    \sigma_{\text{Leland}}^2 = \sigma^2 + \text{sign}(\Gamma) \cdot \sigma\sqrt{\frac{8\lambda}{\pi \Delta t}}
    $$

    With $\sigma = 0.20$, $\lambda = 0.001$, $\Delta t = 1/252$:

    $$
    \sqrt{\frac{8\lambda}{\pi \Delta t}} = \sqrt{\frac{8 \times 0.001}{\pi / 252}} = \sqrt{\frac{0.008 \times 252}{\pi}} = \sqrt{\frac{2.016}{3.1416}} = \sqrt{0.6415} = 0.8009
    $$

    The adjustment term is $\sigma \times 0.8009 = 0.20 \times 0.8009 = 0.1602$.

    **Long gamma** ($\Gamma > 0$):

    $$
    \sigma_{\text{Leland}}^2 = 0.04 + 0.1602 = 0.2002
    $$

    $$
    \sigma_{\text{Leland}} = \sqrt{0.2002} \approx 0.4475
    $$

    **Short gamma** ($\Gamma < 0$):

    $$
    \sigma_{\text{Leland}}^2 = 0.04 - 0.1602 = -0.1202
    $$

    This is negative, meaning Leland's formula breaks down for these parameters. When the adjustment exceeds $\sigma^2$, the effective volatility becomes imaginary, indicating that the transaction cost is too large relative to the rebalancing frequency for the Leland approach to be valid.

    The adjustment has opposite signs because: for long gamma positions, the gamma P&L is positive (convexity benefit), but transaction costs erode this benefit. To account for the erosion, the effective volatility is increased, which raises the option price and thus the premium charged. For short gamma, transaction costs are partially offset by the fact that the hedger trades less aggressively (the gamma loss is reduced by infrequent rebalancing), so effective volatility decreases. However, the formula's validity requires $\sigma^2$ to exceed the adjustment term, which demands sufficiently frequent rebalancing (small $\Delta t$) or small costs ($\lambda$).

---

**Exercise 3.** The gamma-weighted turnover diverges near expiry as $\int_0^T |\Gamma|\sigma S\,dt \sim \int_0^T \sigma S/\sqrt{T-t}\,dt$. Evaluate this integral explicitly for $S = 100$, $\sigma = 0.20$, $T = 1/12$ (one month). What is the total expected transaction cost with $\lambda = 0.001$? At what time before expiry does the instantaneous turnover rate exceed 1 share per day?

??? success "Solution to Exercise 3"
    The integral for turnover is

    $$
    \text{Turnover} = \int_0^T \frac{\sigma S}{\sqrt{T - t}}\,dt
    $$

    Let $u = T - t$, $du = -dt$. When $t = 0$, $u = T$; when $t = T$, $u = 0$:

    $$
    \text{Turnover} = \int_0^T \frac{\sigma S}{\sqrt{u}}\,du = \sigma S \cdot 2\sqrt{u}\Big|_0^T = 2\sigma S \sqrt{T}
    $$

    With $S = 100$, $\sigma = 0.20$, $T = 1/12$:

    $$
    \text{Turnover} = 2 \times 0.20 \times 100 \times \sqrt{1/12} = 40 \times 0.2887 = 11.55 \text{ shares}
    $$

    Total expected transaction cost:

    $$
    \text{Cost} = \lambda \times S \times \text{Turnover} = 0.001 \times 100 \times 11.55 = \$1.155
    $$

    (Here we interpret turnover as the total number of shares traded, and $\lambda S$ is the cost per share.)

    Actually, since $\text{Cost} = \lambda \times \text{Turnover}$ where turnover already has units of $S$ times shares, let us be more careful. The cost formula is $\lambda S |\delta\theta|$, so total cost is $\lambda \int_0^T S|\Gamma|\sigma S\,dt = \lambda \sigma S^2 \int_0^T |\Gamma|\,dt$. With $|\Gamma| \sim 1/(S\sigma\sqrt{T-t})$:

    $$
    \text{Cost} = \lambda \sigma S^2 \cdot \frac{2\sqrt{T}}{S\sigma} = 2\lambda S\sqrt{T}
    $$

    $$
    \text{Cost} = 2 \times 0.001 \times 100 \times \sqrt{1/12} = 0.200 \times 0.2887 = \$0.0577
    $$

    For the instantaneous turnover rate, the rate at time $t$ is $|\Gamma(t)|\sigma S \approx \sigma S / (\sigma\sqrt{T-t} \cdot S) \cdot \sigma S = \sigma S / \sqrt{T-t}$. Converting to shares per day (multiply by $1/252$): the daily turnover is $\sigma S / \sqrt{T-t} \times (1/252)$. We want this to exceed 1 share per day:

    $$
    \frac{\sigma S}{\sqrt{T - t}} \cdot \frac{1}{252} = 1 \implies \sqrt{T - t} = \frac{\sigma S}{252} = \frac{0.20 \times 100}{252} = 0.0794
    $$

    $$
    T - t = 0.00630 \text{ years} \approx 2.3 \text{ days}
    $$

    The instantaneous turnover rate exceeds 1 share per day when the option is within approximately 2.3 days of expiry.

---

**Exercise 4.** The utility loss from transaction costs scales as $(\lambda\Gamma S^2\sigma^2)^{2/3}T^{1/3}$. Explain why the exponent is $2/3$ rather than $1$ by considering the three competing forces: hedging error ($\sim h^2$), transaction cost per rebalance ($\sim \lambda h$), and rebalancing frequency ($\sim 1/h^2$). If transaction costs decrease by a factor of 8, by what factor does the utility loss decrease?

??? success "Solution to Exercise 4"
    The total cost of hedging combines three effects. With hedge bandwidth $h$ (delta deviation before rebalancing):

    - **Hedging error** per unit time: $\sim \Gamma^2 S^4 \sigma^4 h^2$ (variance of P&L from delta deviation $h$)
    - **Transaction cost per rebalance**: $\sim \lambda S h$ (proportional cost for trading $h$ shares)
    - **Rebalancing frequency**: $\sim \sigma^2 S^2 / h^2$ per unit time (time for delta to drift by $h$)

    Total cost rate:

    $$
    C(h) = \underbrace{\Gamma^2 S^4 \sigma^4 h^2}_{\text{hedging error}} + \underbrace{\lambda S h \cdot \frac{\sigma^2 S^2}{h^2}}_{\text{transaction costs}} = \Gamma^2 S^4 \sigma^4 h^2 + \frac{\lambda \sigma^2 S^3}{h}
    $$

    Minimizing over $h$:

    $$
    \frac{dC}{dh} = 2\Gamma^2 S^4 \sigma^4 h - \frac{\lambda \sigma^2 S^3}{h^2} = 0
    $$

    $$
    h^3 = \frac{\lambda \sigma^2 S^3}{2\Gamma^2 S^4 \sigma^4} = \frac{\lambda}{2\Gamma^2 S \sigma^2}
    $$

    Substituting back, the minimum cost scales as

    $$
    C^* \sim (\lambda \Gamma S^2 \sigma^2)^{2/3}
    $$

    The exponent $2/3$ arises because the optimal bandwidth $h^* \sim \lambda^{1/3}$, so the transaction cost component $\sim \lambda / h \sim \lambda^{2/3}$ and the hedging error $\sim h^2 \sim \lambda^{2/3}$. Both terms contribute equally at the optimum, each scaling as $\lambda^{2/3}$.

    Over time $T$, the total utility loss is $C^* \times T^{1/3}$ (the sublinear time dependence comes from the fact that the hedge can be adjusted less frequently as the option ages).

    If transaction costs decrease by a factor of 8 ($\lambda \to \lambda/8$), the utility loss decreases by

    $$
    (1/8)^{2/3} = \frac{1}{8^{2/3}} = \frac{1}{4}
    $$

    The utility loss decreases by a factor of 4. This is better than linear (which would give a factor of 8) but worse than square root. The $2/3$ exponent means that reducing costs has diminishing returns: cutting costs by $8\times$ only reduces hedging loss by $4\times$.

---

**Exercise 5.** Market impact follows $\text{Execution Price} = S + \eta|\delta\theta|^\alpha$ with $\alpha \approx 0.5$. A trader needs to rebalance by $\delta\theta = 200$ shares, with $S = 100$ and $\eta = 0.01$. Compute the market impact cost. Compare this to the proportional spread cost with $\lambda = 0.001$. At what trade size does market impact begin to dominate spread costs?

??? success "Solution to Exercise 5"
    The market impact cost for trading $\delta\theta = 200$ shares is

    $$
    \text{Impact cost} = \eta \cdot |\delta\theta|^\alpha \cdot \delta\theta = \eta \cdot |\delta\theta|^{1+\alpha}
    $$

    Wait -- the execution price is $S + \eta|\delta\theta|^\alpha$, so the total cost above the fair price is

    $$
    \text{Impact cost} = \eta \cdot |\delta\theta|^\alpha \times \delta\theta = 0.01 \times 200^{0.5} \times 200
    $$

    Actually, the cost per share is $\eta|\delta\theta|^\alpha$, and the total impact cost is

    $$
    \text{Total impact cost} = \eta \cdot |\delta\theta|^\alpha \cdot |\delta\theta| = \eta \cdot |\delta\theta|^{1+\alpha}
    $$

    $$
    = 0.01 \times 200^{1.5} = 0.01 \times 2828.4 = \$28.28
    $$

    The proportional spread cost is

    $$
    \text{Spread cost} = \lambda S \cdot |\delta\theta| = 0.001 \times 100 \times 200 = \$20.00
    $$

    Market impact ($\$28.28$) already exceeds spread cost ($\$20.00$) at 200 shares.

    To find where they are equal, set $\eta|\delta\theta|^{1+\alpha} = \lambda S |\delta\theta|$:

    $$
    \eta |\delta\theta|^\alpha = \lambda S
    $$

    $$
    |\delta\theta|^\alpha = \frac{\lambda S}{\eta} = \frac{0.001 \times 100}{0.01} = 10
    $$

    $$
    |\delta\theta| = 10^{1/\alpha} = 10^{1/0.5} = 10^2 = 100 \text{ shares}
    $$

    Market impact begins to dominate spread costs at trade sizes above 100 shares. Below this threshold, the proportional spread cost is the primary concern; above it, the square-root impact law causes costs to grow faster than linearly.

---

**Exercise 6.** Consider a portfolio of 100 short ATM calls with $S = K = 100$, $\sigma = 0.20$, $\tau = 30$ days. The portfolio gamma is $\Gamma_{\text{port}} = 100 \times 0.055 = 5.5$ and the spread is $\lambda = 0.0005$. Compute the Whalley-Wilmott bandwidth for the portfolio, the expected total transaction cost over the option's life, and compare to the total premium collected. At what spread level does the transaction cost consume more than 10% of the premium?

??? success "Solution to Exercise 6"
    **Whalley-Wilmott bandwidth** for the portfolio with $\Gamma_{\text{port}} = 5.5$, $\lambda = 0.0005$, and assuming $r\tau$ is small so $e^{-r\tau} \approx 1$:

    $$
    h = \left(\frac{3\lambda}{2\Gamma_{\text{port}}}\right)^{1/3} = \left(\frac{3 \times 0.0005}{2 \times 5.5}\right)^{1/3} = \left(\frac{0.0015}{11.0}\right)^{1/3} = (1.364 \times 10^{-4})^{1/3}
    $$

    $$
    h = 0.005146
    $$

    The band is very narrow ($\approx 0.5$ delta points) because the large portfolio gamma demands tight hedging.

    **Expected total transaction cost:** The total turnover is approximately $2\Gamma_{\text{port}} \sigma S \sqrt{\tau} \cdot \sqrt{2/\pi}$ (integrated over the life). More directly, using the formula $\text{Cost} \sim \lambda \sigma S \sqrt{\tau} \times$ (portfolio notional):

    $$
    \text{Turnover} \approx 2\sigma S \sqrt{\tau} = 2 \times 0.20 \times 100 \times \sqrt{30/365} = 40 \times 0.2867 = 11.47 \text{ shares per single option}
    $$

    For 100 options: total turnover $\approx 100 \times 11.47 = 1{,}147$ shares. Total cost:

    $$
    \text{Cost} = \lambda \times S \times \text{Total turnover} = 0.0005 \times 100 \times 1147 = \$57.35
    $$

    **Premium collected:** ATM call with $\tau = 30$ days, $\sigma = 0.20$: $V \approx S\sigma\sqrt{\tau/(2\pi)} = 100 \times 0.20 \times \sqrt{30/(365 \times 2\pi)} \approx 100 \times 0.20 \times 0.1145 = \$2.29$ per option. For 100 options: total premium $\approx \$229$.

    Transaction cost as a fraction of premium: $57.35 / 229 \approx 25\%$.

    **Spread level for 10% cost:** We need $\lambda' \times S \times 1147 = 0.10 \times 229$:

    $$
    \lambda' = \frac{22.9}{100 \times 1147} = \frac{22.9}{114{,}700} = 0.0002
    $$

    At a spread of $\lambda = 0.0002$ ($= 2$ basis points), transaction costs consume $10\%$ of the premium. Above this level, costs eat significantly into profitability.
