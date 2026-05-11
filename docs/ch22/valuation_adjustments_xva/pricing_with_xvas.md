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

---

## Exercises

**Exercise 1.** Explain why XVA pricing breaks the law of one price. Two banks, A and B, price the same 5-year swap. Bank A has a funding spread of 50 bps and counterparty credit spread of 150 bps; Bank B has a funding spread of 100 bps and counterparty credit spread of 100 bps. With LGD = 60% and average expected exposure of \$10M, compute CVA and FVA for each bank (use simplified formulas). Which bank offers a more competitive price, and why?

??? success "Solution to Exercise 1"
    **Bank A:** funding spread $s_F^A = 50$ bps, counterparty credit spread $s_C^A = 150$ bps.

    **Bank B:** funding spread $s_F^B = 100$ bps, counterparty credit spread $s_C^B = 100$ bps.

    Both have LGD $= 60\%$ and average expected exposure $\text{EE} = \$10$M over 5 years.

    **CVA computation** (simplified: $\text{CVA} \approx \text{LGD} \times \text{EE} \times s_C \times T \times \bar{D}$, where $\bar{D}$ is an average discount factor).

    For a more careful calculation, using $\text{CVA} \approx \text{LGD} \cdot \text{EE} \cdot (1 - e^{-s_C T / \text{LGD}}) \cdot \bar{D}$. With $r = 3\%$ and a simplified approach:

    $$
    \text{CVA} \approx \text{LGD} \times \text{EE} \times \int_0^5 \frac{s_C}{\text{LGD}} e^{-(s_C/\text{LGD} + r)t} \, dt = s_C \times \text{EE} \times \frac{1 - e^{-(s_C/\text{LGD} + r) \cdot 5}}{s_C/\text{LGD} + r}
    $$

    For **Bank A** ($s_C^A = 0.015$, $\lambda_C^A = 0.015/0.6 = 0.025$):

    $$
    \text{CVA}_A = 0.015 \times 10 \times \frac{1 - e^{-0.055 \times 5}}{0.055} = 0.15 \times \frac{1 - 0.7601}{0.055} = 0.15 \times 4.362 = \$0.654\text{M}
    $$

    For **Bank B** ($s_C^B = 0.010$, $\lambda_C^B = 0.010/0.6 = 0.01667$):

    $$
    \text{CVA}_B = 0.010 \times 10 \times \frac{1 - e^{-0.04667 \times 5}}{0.04667} = 0.10 \times \frac{1 - 0.7917}{0.04667} = 0.10 \times 4.464 = \$0.446\text{M}
    $$

    **FVA computation** (simplified: $\text{FVA} \approx s_F \times \text{EE} \times \int_0^5 e^{-rt} dt$):

    $$
    \int_0^5 e^{-0.03t} \, dt = \frac{1 - e^{-0.15}}{0.03} = \frac{0.1393}{0.03} = 4.643
    $$

    For **Bank A:**

    $$
    \text{FVA}_A = 0.005 \times 10 \times 4.643 = \$0.232\text{M}
    $$

    For **Bank B:**

    $$
    \text{FVA}_B = 0.010 \times 10 \times 4.643 = \$0.464\text{M}
    $$

    **Total XVA comparison:**

    | | Bank A | Bank B |
    |---|---|---|
    | CVA | \$0.654M | \$0.446M |
    | FVA | \$0.232M | \$0.464M |
    | **Total** | **\$0.886M** | **\$0.910M** |

    Bank A offers a slightly more competitive price (lower total XVA: \$0.886M vs. \$0.910M), despite having a riskier counterparty, because its lower funding costs more than compensate. This demonstrates that the "best" price depends on the bank's own characteristics, not just the counterparty's credit quality, breaking the law of one price.

---

**Exercise 2.** A portfolio consists of two trades with the same counterparty: Trade 1 has $V_1 = +\$5$M and Trade 2 has $V_2 = -\$3$M. Under a netting agreement, the netted exposure is $\max(V_1 + V_2, 0) = \$2$M. Compute the standalone CVA for each trade and the netted CVA, using a flat hazard rate $\lambda = 2\%$, LGD = 60%, and 5-year horizon. Verify that $\text{CVA}(\text{Netted}) < \text{CVA}(1) + \text{CVA}(2)$ and compute the netting benefit.

??? success "Solution to Exercise 2"
    **Setup:** Trade 1 has $V_1 = +\$5$M, Trade 2 has $V_2 = -\$3$M. Flat hazard rate $\lambda = 2\%$, LGD $= 60\%$, horizon $T = 5$ years.

    **Standalone CVA for Trade 1:**

    The exposure is $V_1^+ = \$5$M (constant for simplicity).

    $$
    \text{CVA}(1) = \text{LGD} \cdot V_1^+ \cdot \int_0^5 \lambda \cdot e^{-(\lambda + r)t} \, dt
    $$

    Assuming $r = 0$ for simplicity (or absorbing it into the discount):

    $$
    \text{CVA}(1) = 0.60 \times 5 \times 0.02 \times \frac{1 - e^{-0.02 \times 5}}{0.02} = 0.06 \times \frac{0.0952}{0.02} = 0.06 \times 4.758 = \$0.285\text{M}
    $$

    With discounting at $r = 3\%$:

    $$
    \text{CVA}(1) = 0.60 \times 5 \times 0.02 \times \frac{1 - e^{-0.05 \times 5}}{0.05} = 0.06 \times \frac{0.2212}{0.05} = 0.06 \times 4.424 = \$0.265\text{M}
    $$

    **Standalone CVA for Trade 2:**

    Trade 2 has $V_2 = -\$3$M, so $V_2^+ = 0$. The bank has no positive exposure to the counterparty on this trade.

    $$
    \text{CVA}(2) = 0
    $$

    **Sum of standalone CVAs:**

    $$
    \text{CVA}(1) + \text{CVA}(2) = 0.265 + 0 = \$0.265\text{M}
    $$

    **Netted portfolio CVA:**

    Under netting, the exposure is $(V_1 + V_2)^+ = (5 - 3)^+ = \$2$M.

    $$
    \text{CVA}(\text{Netted}) = 0.60 \times 2 \times 0.02 \times \frac{1 - e^{-0.05 \times 5}}{0.05} = 0.024 \times 4.424 = \$0.106\text{M}
    $$

    **Verification:**

    $$
    \text{CVA}(\text{Netted}) = \$0.106\text{M} < \$0.265\text{M} = \text{CVA}(1) + \text{CVA}(2) \quad \checkmark
    $$

    **Netting benefit:**

    $$
    \text{Netting benefit} = 0.265 - 0.106 = \$0.159\text{M}
    $$

    This represents a 60% reduction in CVA due to netting. The benefit arises because Trade 2's negative value partially offsets Trade 1's positive value, reducing the net exposure from \$5M to \$2M.

---

**Exercise 3.** In the BSDE framework, the generic XVA driver is

$$
f(t, V, Z) = -rV + \lambda_C \cdot \text{LGD}_C \cdot V^+ - \lambda_B \cdot \text{LGD}_B \cdot V^- + s_F \cdot (V - C)^+
$$

Explain why the $V^+$ and $V^-$ terms make this equation nonlinear. What would the equation reduce to if there were no default risk and no funding costs? Show that in the linear case, the solution recovers the classical risk-neutral price.

??? success "Solution to Exercise 3"
    **Why $V^+$ and $V^-$ make the equation nonlinear.**

    The functions $V^+ = \max(V, 0)$ and $V^- = \max(-V, 0)$ are piecewise linear but not globally linear:

    $$
    V^+ = \begin{cases} V & \text{if } V > 0 \\ 0 & \text{if } V \le 0 \end{cases}, \quad V^- = \begin{cases} 0 & \text{if } V \ge 0 \\ -V & \text{if } V < 0 \end{cases}
    $$

    If we consider two solutions $V_1$ and $V_2$ and a linear combination $\alpha V_1 + \beta V_2$, in general:

    $$
    (\alpha V_1 + \beta V_2)^+ \ne \alpha V_1^+ + \beta V_2^+
    $$

    For example, if $V_1 = 1$ and $V_2 = -2$, then $(V_1 + V_2)^+ = (-1)^+ = 0$, but $V_1^+ + V_2^+ = 1 + 0 = 1$.

    This violates the superposition principle, making the BSDE/PDE nonlinear. Practically, the effective discount rate changes depending on the sign of $V$: the equation behaves differently in the regions $\{V > 0\}$ and $\{V < 0\}$.

    **Linear case (no default, no funding costs).**

    Setting $\lambda_C = \lambda_B = 0$ and $s_F = 0$:

    $$
    f(t, V, Z) = -rV + 0 - 0 + 0 = -rV
    $$

    The BSDE becomes:

    $$
    V_t = \xi + \int_t^T (-r V_s) \, ds - \int_t^T Z_s \, dW_s
    $$

    This is a linear BSDE whose solution is:

    $$
    V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-r(T-t)} \xi \,|\, \mathcal{F}_t\right]
    $$

    This is precisely the **classical risk-neutral pricing formula**: the discounted expected payoff under the risk-neutral measure. The corresponding PDE is the standard Black-Scholes equation:

    $$
    \partial_t V + \frac{1}{2}\sigma^2 x^2 \partial_{xx} V + rx \partial_x V - rV = 0
    $$

    confirming that the BSDE framework reduces to standard risk-neutral pricing when all XVA effects are removed.

---

**Exercise 4.** Compute the incremental XVA for a new trade added to an existing portfolio. The portfolio's current CVA is \$2.0M. Adding a new trade (standalone CVA = \$0.5M) that partially offsets existing exposures results in a new portfolio CVA of \$2.1M. What is the incremental CVA of the new trade? Compare this to the standalone CVA and explain why incremental pricing is essential for trade decisions. Under what conditions could the incremental CVA be negative?

??? success "Solution to Exercise 4"
    **Incremental CVA:**

    $$
    \text{CVA}^{\text{incremental}} = \text{CVA}(\text{Portfolio} + \text{Trade}) - \text{CVA}(\text{Portfolio}) = 2.1 - 2.0 = \$0.1\text{M}
    $$

    **Comparison to standalone CVA:**

    The standalone CVA of the new trade is \$0.5M, but its incremental impact on the portfolio is only \$0.1M -- a reduction of 80%.

    **Why incremental pricing is essential:**

    The new trade partially offsets existing exposures in the portfolio. Under netting, the positive exposure of the new trade is partially cancelled by negative exposures already in the book. If the bank charged standalone CVA (\$0.5M), it would overcharge the client and potentially lose the trade to a competitor who correctly prices incrementally. Conversely, if a bank ignores netting benefits and charges standalone XVA, it misallocates costs and makes suboptimal trade decisions.

    **When could incremental CVA be negative?**

    Incremental CVA is negative when the new trade *reduces* the portfolio's total CVA. This occurs when the new trade has exposure that is negatively correlated with or offsets the existing portfolio's exposure. For example:

    - If the existing portfolio has $V > 0$ (net positive exposure) and the new trade has $V < 0$ (negative value), the new trade reduces net exposure, lowering CVA.
    - A receive-fixed swap added to a portfolio dominated by pay-fixed swaps would reduce exposure at most future time points.

    In such cases, $\text{CVA}(\text{Portfolio} + \text{Trade}) < \text{CVA}(\text{Portfolio})$, so the incremental CVA is negative. The XVA desk would *credit* the trading desk for the CVA benefit, incentivizing risk-reducing trades.

---

**Exercise 5.** Consider the XVA-adjusted delta hedge. A bank holds a call option with clean delta $\Delta^{\text{clean}} = 0.55$. The CVA delta is $\Delta^{\text{CVA}} = 0.03$ (CVA increases when the underlying rises, because exposure increases). The FVA delta is $\Delta^{\text{FVA}} = 0.01$. Compute the total XVA-adjusted delta $\Delta^{\text{total}} = \Delta^{\text{clean}} - \Delta^{\text{CVA}} - \Delta^{\text{FVA}}$ (note: CVA and FVA deltas reduce the effective hedge ratio). Discuss why ignoring XVA Greeks leads to systematic hedging errors.

??? success "Solution to Exercise 5"
    **Total XVA-adjusted delta:**

    $$
    \Delta^{\text{total}} = \Delta^{\text{clean}} - \Delta^{\text{CVA}} - \Delta^{\text{FVA}} = 0.55 - 0.03 - 0.01 = 0.51
    $$

    **Interpretation:**

    The clean hedge ratio requires buying 0.55 shares per option, but the XVA-adjusted hedge requires only 0.51 shares. The reduction reflects the fact that as the underlying rises:

    - The option value increases, increasing exposure to the counterparty
    - Higher exposure means higher CVA (more to lose if counterparty defaults)
    - Higher exposure also means higher FVA (more to fund)

    The CVA and FVA losses partially offset the gain from the option's delta, so less hedging is needed.

    **Why ignoring XVA Greeks leads to systematic hedging errors.**

    If the bank hedges with $\Delta^{\text{clean}} = 0.55$ instead of $\Delta^{\text{total}} = 0.51$, it is *over-hedged* by 0.04 shares. This creates systematic P&L leakage:

    1. *Directional bias:* The portfolio has unintended exposure equal to $\Delta^{\text{CVA}} + \Delta^{\text{FVA}} = 0.04$. If the underlying moves, the excess hedge generates P&L that does not offset any risk in the total (XVA-inclusive) portfolio.

    2. *Accumulation over time:* For a portfolio of many options, these small mishedges accumulate. Over a hedging horizon, the aggregate P&L from ignoring XVA Greeks can be comparable to the XVA itself.

    3. *Cross-gamma effects:* XVA Greeks also have second-order terms (XVA gamma, XVA cross-gamma) that create additional hedging errors if ignored.

    4. *Wrong risk attribution:* The trading desk believes it is flat on delta when it is actually exposed. This leads to incorrect risk reporting and potential limit breaches.

    In practice, the XVA desk typically manages XVA Greeks separately from the trading desk's clean hedges, creating an organizational split that must be carefully coordinated.

---

**Exercise 6.** A trading desk proposes a 5-year equity swap with \$50M notional. The XVA desk computes: CVA = \$300K, DVA = \$150K, FVA = \$200K, KVA = \$400K. The desk expects to earn a spread of 30 bps per annum (\$150K/year). Using the deal acceptability criterion

$$
\text{Accept if } \text{Expected Profit} > \text{XVA Charge}
$$

where Expected Profit = total spread revenue over 5 years, determine whether the trade should be accepted. What minimum spread (in bps) would make the trade acceptable?

??? success "Solution to Exercise 6"
    **Expected profit over 5 years:**

    The desk earns 30 bps per annum on \$50M notional:

    $$
    \text{Annual revenue} = 0.003 \times 50{,}000{,}000 = \$150{,}000 \text{ per year}
    $$

    $$
    \text{Total expected profit} = 150{,}000 \times 5 = \$750{,}000
    $$

    **XVA charge:**

    $$
    \text{Net XVA} = \text{CVA} - \text{DVA} + \text{FVA} + \text{KVA} = 300 - 150 + 200 + 400 = \$750{,}000
    $$

    **Deal acceptability:**

    $$
    \text{Expected Profit} = \$750{,}000 = \text{XVA Charge} = \$750{,}000
    $$

    The trade is exactly at break-even. Under the strict criterion $\text{Expected Profit} > \text{XVA Charge}$, the trade should be **rejected** (or at best is marginal).

    **Minimum spread for acceptability.**

    Let the required spread be $s$ bps per annum. The total revenue over 5 years must exceed the XVA charge:

    $$
    s \times 50{,}000{,}000 \times 5 / 10{,}000 > 750{,}000
    $$

    $$
    s \times 25{,}000 > 750{,}000
    $$

    $$
    s > 30 \text{ bps}
    $$

    The minimum spread is **strictly greater than 30 bps** -- any amount above 30 bps makes the trade profitable. In practice, the desk would target a spread of at least 35-40 bps to provide a reasonable margin above break-even, accounting for model uncertainty in the XVA estimates.

    Note: A more precise calculation would discount the revenue stream and compare the present value of revenues to the XVA charge:

    $$
    \text{PV(Revenue)} = 150{,}000 \times \frac{1 - e^{-0.03 \times 5}}{0.03} = 150{,}000 \times 4.643 = \$696{,}500
    $$

    Under this more accurate comparison, $696{,}500 < 750{,}000$, so the trade is clearly unprofitable and should be rejected. The minimum spread satisfying $s \times 50{,}000{,}000 \times 4.643 / 10{,}000 > 750{,}000$ is:

    $$
    s > \frac{750{,}000}{23{,}215} = 32.3 \text{ bps}
    $$

---

**Exercise 7.** Discuss the FVA debate between Hull-White (2012) and Burgard-Kjaer (2011). Hull and White argue that FVA should not be included in derivative pricing because it creates arbitrage opportunities relative to the risk-neutral framework. Burgard and Kjaer argue that FVA reflects real costs that banks face. Present both arguments. If two banks disagree on whether to include FVA, what market consequences arise? How does the existence of FVA affect the concept of a "fair" derivative price?

??? success "Solution to Exercise 7"
    **The Hull-White (2012) argument against FVA:**

    Hull and White argue from the perspective of the Modigliani-Miller theorem and classical derivatives pricing theory:

    1. *Arbitrage argument:* In complete markets, the unique no-arbitrage price of a derivative is determined by replication. The cost of replication depends only on the hedging instruments, not on how the replicating portfolio is funded. Including FVA creates prices that deviate from the no-arbitrage price, opening up theoretical arbitrage opportunities.

    2. *Shareholder value:* The bank's funding cost reflects its own credit risk, which is already priced by the market. Passing funding costs to derivative prices double-counts this risk (once in the bank's bond spreads, once in derivative FVA).

    3. *Modigliani-Miller:* The value of an asset should be independent of how it is financed. Just as a house's value doesn't depend on the mortgage rate, a derivative's fair value shouldn't depend on the bank's borrowing rate.

    4. *Competitive implication:* If FVA is included, two banks would assign different "fair values" to the same derivative, undermining the notion of a single fair value.

    **The Burgard-Kjaer (2011) argument for FVA:**

    Burgard and Kjaer take a practitioner's perspective based on realistic market conditions:

    1. *Real costs:* Banks cannot borrow at the risk-free rate. Funding an uncollateralized derivative position at $r + s_F$ creates a real cash cost of $s_F$ per unit of exposure per year. This cost exists regardless of theoretical arguments.

    2. *Incomplete markets:* The Modigliani-Miller theorem assumes perfect capital markets. In reality, markets are incomplete, frictions exist, and funding constraints are binding. In this setting, the replication argument breaks down.

    3. *P&L reality:* A bank's treasury charges business units for funding. If the derivatives desk ignores FVA, it will systematically report profits that exceed actual economic performance (because funding costs are borne by treasury but not reflected in the desk's P&L).

    4. *Consistent framework:* The BSDE/PDE framework naturally produces FVA terms when realistic funding assumptions are used. FVA is not an ad-hoc adjustment but emerges from the mathematics of self-financing portfolios under funding constraints.

    **Market consequences if banks disagree.**

    If Bank A includes FVA and Bank B does not:

    - Bank B will quote tighter prices (lower XVA charges), winning more trades.
    - Bank B accumulates unfunded positions, bearing real funding costs that are not reflected in its P&L.
    - Over time, Bank B's economic returns underperform its reported returns, creating a hidden loss.
    - Bank A loses market share but maintains economic consistency.

    This creates adverse selection: the bank with the "correct" but more expensive pricing loses business to the bank with the cheaper but economically incorrect pricing.

    **Impact on the concept of "fair" price.**

    The existence of FVA fundamentally challenges the concept of a single "fair" derivative price:

    1. *Entity-specific pricing:* Different banks with different funding costs compute different prices, even for identical derivatives. The "fair price" becomes entity-dependent.

    2. *Bid-ask from XVA:* FVA naturally creates bid-ask spreads (the bank charges FVA when buying an asset but benefits when taking on a liability). These spreads vary across banks.

    3. *No unique equilibrium:* Unlike the Black-Scholes world where all agents agree on the price, the FVA world has multiple equilibrium prices depending on the participants.

    4. *Pragmatic resolution:* In practice, the market has largely adopted FVA inclusion. The "fair" price is effectively determined by competitive dynamics among FVA-charging banks, with the equilibrium reflecting the marginal funder's cost. The theoretical debate continues, but market practice has moved decisively toward FVA inclusion.
