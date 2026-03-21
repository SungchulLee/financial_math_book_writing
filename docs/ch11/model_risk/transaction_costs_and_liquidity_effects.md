# Transaction Costs and Liquidity Effects


With proportional cost \(\lambda\) (bid-ask spread), rebalancing \(\delta \theta\) shares costs about

\[
\text{Cost} = \lambda S |\delta\theta|
\]


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

\[
\Delta^{\text{BS}} - h \leq \Delta^{\text{actual}} \leq \Delta^{\text{BS}} + h
\]

where the **bandwidth** is:

\[
\boxed{h = \left(\frac{3\lambda e^{-r\tau}}{2\Gamma}\right)^{1/3}}
\]

**Intuition:**
- High \(\Gamma\) (convexity benefit): narrow band (hedge frequently)
- High \(\lambda\) (expensive trading): wide band (hedge infrequently)
- The \(1/3\) exponent comes from balancing \(\mathcal{O}(h^2)\) hedging error against \(\mathcal{O}(1/h)\) transaction costs

**Derivation sketch.** The hedging error from a delta deviation of \(h\) is \(\sim \Gamma h^2 \sigma^2 S^2 \Delta t\). The frequency of hitting the band is \(\sim 1/(h^2 \Delta t)\). Transaction cost per hit is \(\sim \lambda S h\). Optimal \(h\) minimizes total cost.

---

## Leland's modified volatility


**Leland (1985)** proposed hedging at Black–Scholes delta but with adjusted volatility:

\[
\sigma_{\text{Leland}}^2 = \sigma^2 + \text{sign}(\Gamma) \cdot \sigma \sqrt{\frac{8\lambda}{\pi \Delta t}}
\]

**For long positions** (\(\Gamma > 0\)): Use higher volatility (wider smile)
**For short positions** (\(\Gamma < 0\)): Use lower volatility

This approach maintains continuous hedging but accounts for transaction costs through the pricing model.

---

## Utility-based analysis


With exponential utility \(U(x) = -e^{-\gamma x}\), the utility loss from transaction costs scales as:

\[
\text{Utility Loss} \sim (\lambda \Gamma S^2 \sigma^2)^{2/3} T^{1/3}
\]

Key features:
- Sublinear in time horizon \(T\)
- Fractional power of costs \(\lambda\)
- Dominated by gamma exposure

---

## Gamma-weighted turnover


Expected hedge turnover over \([0,T]\) is approximately:

\[
\text{Turnover} = \int_0^T |\text{d}\Delta| \approx \int_0^T |\Gamma| \sigma S \, dt
\]

**Near expiry blow-up.** Since \(\Gamma \sim \tau^{-1/2}\):

\[
\text{Turnover} \sim \int_0^T \frac{\sigma S}{\sqrt{T-t}} \, dt \sim \sqrt{T}
\]

The integral diverges as \(t \to T\), reflecting infinite turnover needed for perfect hedging.

**Total transaction cost:**
\[
\text{Total Cost} = \lambda \times \text{Turnover} \sim \lambda \sigma S \sqrt{T}
\]

---

## Liquidity effects


Beyond bid-ask spreads, liquidity impacts hedging through:

**1. Market impact.** Large trades move prices:
\[
\text{Execution Price} = S + \eta \cdot |\delta\theta|^\alpha
\]

where \(\eta\) is impact coefficient and \(\alpha \approx 0.5\) empirically.

**2. Slippage.** Execution prices differ from model prices during rapid moves.

**3. Position limits.** Constraints on delta/gamma exposure from risk limits.

**4. Funding costs.** Borrowing costs for leveraged positions.

---

## Numerical example


ATM call with \(S = K = 100\), \(\sigma = 20\%\), \(\tau = 30\) days, bid-ask spread \(\lambda = 0.1\%\):

- \(\Gamma = 0.055\)
- Optimal bandwidth: \(h = (3 \times 0.001/(2 \times 0.055))^{1/3} = 0.030\) (3 delta points)
- Expected turnover: \(\sim 0.055 \times 0.20 \times 100 \times \sqrt{30/252} \approx 0.38\) shares
- Transaction cost: \(\sim 0.001 \times 100 \times 0.38 = \$0.038\)

For comparison, the option value is \(\sim \$3.20\), so costs are \(\sim 1\%\) of value.

---

## Implications for practice


1. **Widen bands near expiry**: As \(\Gamma\) grows, bandwidth grows slower (\(h \sim \Gamma^{-1/3}\))
2. **Hedge less frequently for expensive assets**: Higher \(\lambda\) means wider bands
3. **Account for costs in pricing**: Add \(\sim \lambda^{2/3}\) to option prices for cost reservation
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
- Optimal no-trade bandwidth scales as \((\lambda/\Gamma)^{1/3}\)
- Costs scale with hedge turnover, hence with gamma
- Leland's approach adjusts volatility to account for costs
- Near-expiry positions face particularly high transaction costs
- Utility loss from costs scales as \(\lambda^{2/3}\), not linearly
