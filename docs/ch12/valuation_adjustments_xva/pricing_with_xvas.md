# Pricing with XVAs

Modern derivative pricing integrates **XVAs** directly into valuation, fundamentally changing the classical risk-neutral pricing paradigm. This section explores the theoretical and practical implications.

---

## The Classical Framework

### Risk-Neutral Pricing (Pre-XVA)

Classical derivative pricing assumes:

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\left[D(0,T) \cdot \text{Payoff}_T\right]
$$

with key assumptions:
- Borrowing/lending at risk-free rate
- No default risk
- No funding constraints
- Complete markets

**Properties:**
- **Linear:** $V(A + B) = V(A) + V(B)$
- **Law of one price:** Unique price
- **Counterparty-independent:** Price doesn't depend on who trades

---

## XVA-Inclusive Pricing

### The Adjusted Value

$$
V^{\text{total}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA} - \text{FVA} - \text{KVA} - \text{MVA}
$$

This breaks the classical framework:
- **Nonlinear:** $V^{\text{total}}(A+B) \ne V^{\text{total}}(A) + V^{\text{total}}(B)$
- **Multiple prices:** Different banks compute different XVAs
- **Counterparty-dependent:** Price depends on trading relationship

---

## Nonlinearity of XVA Pricing

### Sources of Nonlinearity

**1. Netting:**
$$
\text{CVA}(\text{Netted Portfolio}) \ne \sum_i \text{CVA}(\text{Trade}_i)
$$

**2. Collateral:**
Collateral threshold effects create discontinuities.

**3. Capital:**
Capital requirements have nonlinear dependence on portfolio composition.

**4. Funding:**
Asymmetric borrowing/lending rates.

### Implications

- Trade-level pricing requires incremental XVA calculation
- Portfolio optimization is complex
- No simple aggregation rules

---

## BSDE Formulation

XVA pricing naturally fits the **backward stochastic differential equation** framework:

$$
V_t = \xi + \int_t^T f(s, V_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$

where:
- $\xi$ = terminal payoff
- $f$ = driver incorporating XVA effects
- $Z$ = hedging process

### Generic XVA Driver

$$
f(t, V, Z) = -rV + \underbrace{\lambda_C \cdot \text{LGD}_C \cdot V^+}_{\text{CVA}} - \underbrace{\lambda_B \cdot \text{LGD}_B \cdot V^-}_{\text{DVA}} + \underbrace{s_F \cdot (V - C)^+}_{\text{FVA}} + \cdots
$$

where:
- $\lambda_C, \lambda_B$ = default intensities
- $C$ = collateral
- $s_F$ = funding spread

### Recursive Structure

The BSDE approach captures the **recursive nature** of XVA:
- Today's value depends on future exposures
- Future exposures depend on future values
- Creates feedback loops

---

## PDE Formulation

For Markovian models, XVA pricing satisfies a **nonlinear PDE**:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V + f(t, x, V, \sigma^\top \nabla V) = 0
$$

with terminal condition $V(T, x) = \text{Payoff}(x)$.

**Example (simplified CVA):**
$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r - q)S\frac{\partial V}{\partial S} - rV + \lambda \cdot \text{LGD} \cdot V^+ = 0
$$

### Numerical Methods

- Finite difference schemes (explicit, implicit, Crank-Nicolson)
- Tree methods with XVA adjustments
- Monte Carlo with regression (LSM-style)

---

## Marginal vs Standalone XVA

### Standalone XVA

XVA of a trade considered in isolation:
$$
\text{XVA}^{\text{standalone}}(\text{Trade})
$$

### Incremental (Marginal) XVA

XVA impact of adding a trade to an existing portfolio:
$$
\text{XVA}^{\text{incremental}} = \text{XVA}(\text{Portfolio} + \text{Trade}) - \text{XVA}(\text{Portfolio})
$$

### Allocated XVA

Distribute portfolio XVA to individual trades:
$$
\sum_i \text{XVA}^{\text{allocated}}_i = \text{XVA}(\text{Portfolio})
$$

**Euler allocation:** For homogeneous risk measures:
$$
\text{XVA}^{\text{allocated}}_i = \frac{\partial \text{XVA}}{\partial w_i} \cdot w_i
$$

---

## Pricing Asymmetry

### Two Prices for One Trade

**Bank's price:** $V^{\text{bank}} = V^{\text{clean}} - \text{XVA}^{\text{bank}}$

**Counterparty's price:** $V^{\text{cpty}} = V^{\text{clean}} - \text{XVA}^{\text{cpty}}$

In general: $V^{\text{bank}} \ne -V^{\text{cpty}}$

**The "price" is no longer unique!**

### Bid-Ask from XVA

This asymmetry creates natural bid-ask spreads:
$$
\text{Bid} = V^{\text{clean}} - \text{XVA}^{\text{bid}}
$$
$$
\text{Ask} = V^{\text{clean}} - \text{XVA}^{\text{ask}}
$$

where XVA^{bid} and XVA^{ask} reflect different counterparties or directions.

---

## Impact on Hedging

### XVA-Adjusted Hedging

Classical delta hedge:
$$
\Delta^{\text{clean}} = \frac{\partial V^{\text{clean}}}{\partial S}
$$

XVA-adjusted delta:
$$
\Delta^{\text{total}} = \frac{\partial V^{\text{total}}}{\partial S} = \Delta^{\text{clean}} + \Delta^{\text{XVA}}
$$

### XVA Greeks

**CVA delta:**
$$
\Delta^{\text{CVA}} = \text{LGD} \int_0^T \frac{\partial \text{EE}(t)}{\partial S} \cdot dPD(t) \cdot D(0,t)
$$

**FVA delta:**
$$
\Delta^{\text{FVA}} = s_F \int_0^T \frac{\partial \mathbb{E}[V_t]}{\partial S} \cdot D(0,t) \, dt
$$

### Hedging Challenges

- XVA Greeks can be large and volatile
- Credit hedging (CDS) needed for CVA
- Funding hedges (repo, bonds) for FVA
- XVA hedges may conflict with clean hedges

---

## Organizational Implications

### XVA Desk

Centralized desk responsible for:
- Calculating XVA across all trades
- Charging/crediting trading desks
- Managing and hedging XVA risk
- XVA P&L reporting

### Transfer Pricing

**At trade inception:**
$$
\text{Desk P&L} = \text{Trade Price} - V^{\text{clean}} + \text{XVA Charge}
$$

Trading desks see XVA as a cost; XVA desk manages the risk.

### P&L Attribution

XVA P&L decomposes into:
- New trade impact
- Market movements (rates, spreads, etc.)
- Credit spread movements
- Funding rate movements
- Model changes

---

## Deal Acceptability

### XVA Threshold

A trade may be rejected if XVA is too large:
$$
\text{Accept if } \text{Expected Profit} > \text{XVA Charge}
$$

### Hurdle Rates

Include return on capital:
$$
\text{Accept if } \text{Spread} > \frac{\text{XVA} + \text{KVA}}{\text{Notional} \times \text{Duration}}
$$

### Competitive Implications

Banks with better credit (lower CVA) or funding (lower FVA) have pricing advantages.

---

## Regulatory Perspective

### CVA Capital

Basel III requires capital for CVA risk:
- **SA-CVA:** Standardized approach
- **BA-CVA:** Basic approach (simpler)
- **IMA-CVA:** Internal model approach (advanced)

### Prudent Valuation

Additional reserves for:
- Model uncertainty in XVA
- Market data uncertainty
- Close-out uncertainty

### Accounting

- CVA and DVA in fair value (IFRS 13, ASC 820)
- FVA treatment debated
- KVA and MVA typically not in fair value

---

## Challenges and Debates

### Theoretical Issues

**FVA debate:**
- Does FVA create arbitrage opportunities?
- Should banks price their own funding into derivatives?
- Hull-White (2012) vs Burgard-Kjaer (2011) debate

**DVA inclusion:**
- Controversial "profit from own default"
- Accounting requires it; regulatory capital excludes it

### Practical Issues

- Model risk in XVA calculations
- Computational intensity
- Data quality (credit spreads, funding curves)
- Consistency across XVAs

---

## Example: XVA Impact on Trade Decision

**Proposed trade:** 5-year equity swap, \$50M notional

**Clean value:** \$0 (at-market swap)

**XVA analysis:**

| Component | Value | Notes |
|-----------|-------|-------|
| CVA | -\$300K | Counterparty BB-rated |
| DVA | +\$150K | Bank's own credit |
| FVA | -\$200K | Uncollateralized |
| KVA | -\$400K | Capital requirement |
| **Net XVA** | **-\$750K** | |

**Decision:**
- Trade needs \$750K compensation to break even
- Negotiate higher spread or upfront fee
- Or decline if counterparty won't pay

---

## Key Takeaways

- XVA pricing breaks linearity and creates multiple prices
- BSDE and nonlinear PDE frameworks capture XVA dynamics
- Incremental XVA is key for trade-level decisions
- Hedging requires both market and credit/funding hedges
- XVA desk centralizes calculation and risk management
- Regulatory, accounting, and economic treatments differ
- Competitive advantage accrues to banks with better credit/funding

---

## Further Reading

- Brigo, D., Morini, M., & Pallavicini, A. (2013), *Counterparty Credit Risk, Collateral and Funding*
- Crépey, S. (2015), "Bilateral Counterparty Risk under Funding Constraints"
- Hull, J. & White, A. (2012), "The FVA Debate"
- Burgard, C. & Kjaer, M. (2013), "Funding Costs, Funding Strategies"
- Andersen, L. & Piterbarg, V. (2010), *Interest Rate Modeling* (Vol. III on products and risk)
- Green, A. (2015), *XVA: Credit, Funding and Capital Valuation Adjustments*
