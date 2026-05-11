# Funding Constraints

**Funding constraints** arise when institutions face limits or costs in raising capital to finance positions. These constraints materially affect pricing, hedging, and trading strategies, particularly during periods of market stress.

---

## Nature of Funding Constraints

### Sources of Constraints

**1. Unsecured Funding Limits**

- Banks have finite capacity to issue unsecured debt
- Credit quality affects borrowing costs
- Market conditions affect availability

**2. Collateral Requirements**

- Variation margin for derivatives
- Initial margin (post-crisis regulations)
- Repo haircuts

**3. Balance Sheet Limits**

- Leverage ratio constraints
- Risk-weighted asset limits
- Internal risk limits

**4. Regulatory Requirements**

- Liquidity Coverage Ratio (LCR)
- Net Stable Funding Ratio (NSFR)
- Large exposure limits

---

## Funding Spreads

### Definition

The **funding spread** is the cost of borrowing above the risk-free rate:

$$
s_F(t) = r_B(t) - r(t)
$$

where:

- $r_B(t)$ = bank's borrowing rate
- $r(t)$ = risk-free rate (OIS)

### Decomposition

$$
s_F = s_{\text{credit}} + s_{\text{liquidity}} + s_{\text{term premium}}
$$

- **Credit spread:** Compensation for default risk
- **Liquidity spread:** Cost of less liquid funding
- **Term premium:** Cost of longer-term funding

### Asymmetric Rates

In practice, borrowing and lending rates differ:

$$
r^{\text{borrow}} > r^{\text{OIS}} > r^{\text{lend}}
$$

This asymmetry creates nonlinearities in pricing.

---

## Impact on Derivative Pricing

### Classical Assumption

Risk-neutral pricing assumes borrowing/lending at the risk-free rate:

$$
V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT} \cdot \text{Payoff}]
$$

### With Funding Constraints

When funding at rate $r + s_F$:

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T (r + s_F \cdot \mathbf{1}_{V_t > 0}) dt} \cdot \text{Payoff}\right]
$$

This creates path-dependence and nonlinearity.

---

## Funding Valuation Adjustment (FVA)

### Basic Formula

$$
\text{FVA} = \int_0^T s_F(t) \cdot \mathbb{E}[(V_t - C_t)^+] \cdot D(0,t) \, dt
$$

where $C_t$ is collateral held.

### Interpretation

- Positive exposure ($V_t > C_t$): Bank must fund the gap at $s_F$
- Negative exposure ($V_t < C_t$): Bank may earn funding benefit

See [FVA, KVA, and MVA](../valuation_adjustments_xva/fva_kva.md) for details.

---

## Impact on Trading Strategies

### Leveraged Positions

When funding is constrained:

$$
\text{Cost of Position} = \text{Financing Cost} + \text{Expected Return}
$$

High funding costs make leveraged strategies expensive:

- Basis trades
- Carry trades
- Arbitrage strategies

### Arbitrage Persistence

Classical theory: Arbitrage opportunities are eliminated instantly.

**With funding constraints:** Arbitrage can persist if:

$$
\text{Arbitrage Profit} < \text{Funding Cost} + \text{Capital Cost}
$$

**Example:** Corporate bond basis (CDS vs bond) persisted during 2008 crisis due to funding constraints.

---

## Collateral and Margin

### Variation Margin (VM)

Daily exchange of collateral based on mark-to-market:

$$
\text{VM}_t = V_t - V_{t-1}
$$

**Effect on funding:**

- Reduces counterparty credit risk
- Increases funding/liquidity needs
- Procyclical: Margin calls increase during stress

### Initial Margin (IM)

Upfront collateral posted against potential future exposure:

$$
\text{IM} \approx \text{SIMM}(\text{Portfolio Sensitivities})
$$

**Effect:**

- Significant funding drag on trades
- Creates MVA (Margin Valuation Adjustment)
- Incentive to reduce bilateral exposures

### Margin Period of Risk (MPOR)

Time between last margin call and closeout:

- Typically 10 days bilateral, 5 days cleared
- Exposure during MPOR still exists

---

## Liquidity Coverage Ratio (LCR)

### Definition

$$
\text{LCR} = \frac{\text{High Quality Liquid Assets (HQLA)}}{\text{Net Cash Outflows over 30 days}} \ge 100\%
$$

### Impact on Derivatives

Derivatives affect LCR through:

- Collateral outflows (margin calls under stress)
- Contractual outflows (option exercises, etc.)
- Contingent funding commitments

### Constraint Effect

Banks must hold HQLA against derivative exposures, increasing effective funding costs.

---

## Net Stable Funding Ratio (NSFR)

### Definition

$$
\text{NSFR} = \frac{\text{Available Stable Funding (ASF)}}{\text{Required Stable Funding (RSF)}} \ge 100\%
$$

### Impact on Derivatives

- Derivatives require stable funding based on maturity and type
- Collateral received may not count fully as ASF
- Long-dated derivatives have higher RSF

---

## Balance Sheet Constraints

### Leverage Ratio

$$
\text{Leverage Ratio} = \frac{\text{Tier 1 Capital}}{\text{Exposure Measure}} \ge 3\%
$$

Derivatives contribute to exposure via:

- Current exposure
- Potential future exposure (PFE add-on)
- Cash collateral

### RWA Constraints

Risk-weighted assets limit total derivative exposure:

$$
\text{Capital} \ge 8\% \times \text{RWA}
$$

Derivative RWA depends on counterparty credit quality and exposure.

---

## Procyclicality

### Margin Procyclicality

During stress:

1. Market moves cause losses
2. Margin calls increase
3. Liquidity demand spikes
4. Fire sales depress prices further
5. More margin calls...

**Feedback loop amplifies stress.**

### Funding Spread Procyclicality

Bank funding spreads widen during stress:

- Just when funding is most needed
- Amplifies balance sheet pressure
- Can force deleveraging

---

## Funding Cost Models

### Single Funding Rate

Assume uniform funding cost $s_F$:

$$
\text{Funding Cost} = s_F \cdot \int_0^T \mathbb{E}[V_t^+] \, dt
$$

### Term Structure of Funding

Funding cost varies by tenor $\tau$:

$$
\text{Funding Cost} = \int_0^T s_F(t, T-t) \cdot \mathbb{E}[V_t^+] \, dt
$$

### Stochastic Funding Spread

Model $s_F(t)$ as a stochastic process:

$$
ds_F = \kappa(\theta - s_F) dt + \eta dZ
$$

Captures funding spread volatility during stress.

---

## Optimal Funding Strategy

### Objective

Minimize total funding cost subject to liquidity constraints:

$$
\min \int_0^T c(t, \mathbf{F}_t) \, dt \quad \text{s.t. } \text{LCR}_t \ge 100\%, \text{NSFR}_t \ge 100\%
$$

where $\mathbf{F}_t$ is the funding mix.

### Instruments

- Repo/reverse repo
- Commercial paper
- Medium-term notes
- Deposits
- Central bank facilities

### Trade-offs

- Short-term funding: Cheaper but rollover risk
- Long-term funding: Stable but expensive
- Secured funding: Cheaper but uses collateral

---

## Practical Implications

### Pricing

- Include funding costs in derivative prices
- FVA charges to trading desks
- Competitive impact: Banks with better funding have advantage

### Hedging

- Funding-adjusted hedge ratios
- Consider collateral impact of hedges
- Balance margin efficiency vs hedge effectiveness

### Trade Selection

- Prefer trades that reduce funding needs
- Netting benefits more valuable
- Collateralized trades vs uncollateralized

---

## Key Takeaways

- Funding constraints arise from capital, liquidity, and balance sheet limits
- Funding spreads create real costs above risk-free rates
- Constraints affect pricing through FVA and related adjustments
- Margin requirements increase funding needs, especially during stress
- Regulatory ratios (LCR, NSFR) impose additional constraints
- Procyclicality amplifies funding stress during market dislocations
- Optimal funding strategy balances cost, stability, and regulatory compliance

---

## Further Reading

- Gârleanu, N. & Pedersen, L.H. (2011), "Margin-Based Asset Pricing and Deviations from the Law of One Price"
- Brunnermeier, M.K. & Pedersen, L.H. (2009), "Market Liquidity and Funding Liquidity"
- Duffie, D. (2010), "Asset Price Dynamics with Slow-Moving Capital"
- Basel Committee, "Basel III: The Liquidity Coverage Ratio and Liquidity Risk Monitoring Tools"
- Andersen, L., Duffie, D., & Song, Y. (2019), "Funding Value Adjustments"

---

## Exercises

**Exercise 1.** A bank can borrow at SOFR + 80 bp while its client can borrow at SOFR + 200 bp. The bank enters an uncollateralized derivative with positive expected value \$10M over 5 years. Estimate the bank's funding benefit and the client's funding cost. Should the bank charge an FVA?

??? success "Solution to Exercise 1"
    **Bank's funding benefit and client's funding cost.**

    The bank borrows at SOFR + 80 bp and the client borrows at SOFR + 200 bp. The derivative has positive expected value \$10M to the bank over 5 years. Since the trade is uncollateralized and has positive value to the bank, the bank must fund this exposure on its balance sheet.

    **Bank's funding cost on the derivative:**

    The bank finances the positive exposure at its own borrowing spread of 80 bp above risk-free. Over 5 years on an average exposure of \$10M:

    $$
    \text{Bank's Funding Cost} \approx \$10\text{M} \times 0.0080 \times 5 = \$400{,}000
    $$

    However, the bank also has a **funding benefit** relative to the client. Because the bank can borrow 120 bp cheaper than the client (200 bp - 80 bp), the bank effectively provides cheaper funding to the client through the derivative structure.

    **Client's funding cost:**

    The client, if it had to fund a \$10M exposure externally, would pay:

    $$
    \text{Client's Funding Cost} \approx \$10\text{M} \times 0.0200 \times 5 = \$1{,}000{,}000
    $$

    **Should the bank charge FVA?**

    Yes. The bank should charge an FVA to reflect the real cost of funding the positive exposure. The FVA is:

    $$
    \text{FVA} = \int_0^T s_F(t) \cdot \mathbb{E}[(V_t - C_t)^+] \cdot D(0,t) \, dt
    $$

    With $C_t = 0$ (uncollateralized) and $s_F = 80$ bp:

    $$
    \text{FVA} \approx 0.0080 \times \$10\text{M} \times 5 \times \bar{D} \approx \$400{,}000 \times \bar{D}
    $$

    where $\bar{D}$ is an average discount factor. If $\bar{D} \approx 0.95$ (approximate), FVA $\approx \$380{,}000$.

    The bank should charge this FVA because it represents a real economic cost: the bank must raise funds in the market at a spread above the risk-free rate. Without the FVA charge, the trading desk would be subsidized by the bank's treasury, and the derivative would be mispriced from the bank's perspective.

---

**Exercise 2.** Explain the Liquidity Coverage Ratio (LCR) requirement under Basel III. How do funding constraints imposed by LCR affect a bank's willingness to hold illiquid derivative positions?

??? success "Solution to Exercise 2"
    **Liquidity Coverage Ratio (LCR) under Basel III.**

    The LCR is defined as:

    $$
    \text{LCR} = \frac{\text{High Quality Liquid Assets (HQLA)}}{\text{Total Net Cash Outflows over 30 days}} \ge 100\%
    $$

    **Components:**

    - **HQLA (numerator):** Cash, central bank reserves, and high-quality government bonds that can be easily liquidated in stress. These are categorized into Level 1 (no haircut), Level 2A (15% haircut), and Level 2B (25-50% haircut).
    - **Net cash outflows (denominator):** Expected outflows minus inflows over a 30-day stress scenario. Includes deposit run-offs, contractual obligations, contingent funding commitments, and derivative margin calls.

    **Impact on willingness to hold illiquid derivatives:**

    1. **HQLA buffer requirement:** Illiquid derivative positions generate potential cash outflows (margin calls, exercise obligations). The bank must hold HQLA against these projected outflows, which is costly because HQLA assets typically yield less than the bank's funding cost.

    2. **Higher effective cost:** If holding an illiquid derivative position requires the bank to maintain an additional \$X of HQLA, the effective cost includes the carry cost:

        $$
        \text{LCR Cost} = \Delta\text{HQLA} \times (r_{\text{funding}} - r_{\text{HQLA}})
        $$

        This spread is typically 50-150 bp, making illiquid positions expensive to maintain.

    3. **Stress scenario sensitivity:** Illiquid derivatives are harder to close out, meaning projected outflows during stress are higher and more uncertain. This increases the denominator of the LCR, requiring even more HQLA.

    4. **Reduced appetite:** Banks respond by pricing in the LCR cost (effectively an additional funding charge), widening bid-ask spreads on illiquid derivatives, reducing warehouse capacity for exotic products, and preferring cleared or collateralized structures that have lower LCR impact.

    In summary, the LCR constraint acts as a tax on illiquidity, making banks less willing to hold positions that cannot be easily unwound within the 30-day stress horizon.

---

**Exercise 3.** During a credit crisis, a bank's funding cost rises from SOFR + 50 bp to SOFR + 300 bp. Explain how this funding shock affects the mark-to-market of its uncollateralized derivative portfolio through FVA. Why can funding constraints create a feedback loop during stress periods?

??? success "Solution to Exercise 3"
    **Impact of funding shock on FVA and the feedback loop.**

    **FVA impact of funding spread widening:**

    The FVA on an uncollateralized portfolio is:

    $$
    \text{FVA} = \int_0^T s_F(t) \cdot \mathbb{E}[(V_t - C_t)^+] \cdot D(0,t) \, dt
    $$

    When the funding spread rises from 50 bp to 300 bp (a 250 bp increase), the FVA increases proportionally on the positive exposure:

    $$
    \Delta\text{FVA} = \int_0^T \Delta s_F(t) \cdot \mathbb{E}[V_t^+] \cdot D(0,t) \, dt
    $$

    For a portfolio with average positive exposure $\bar{E}$ and average duration $\bar{T}$:

    $$
    \Delta\text{FVA} \approx 0.0250 \times \bar{E} \times \bar{T}
    $$

    For example, if $\bar{E} = \$1\text{B}$ and $\bar{T} = 5$ years:

    $$
    \Delta\text{FVA} \approx 0.0250 \times \$1\text{B} \times 5 = \$125\text{M}
    $$

    This is a massive mark-to-market loss on the derivative portfolio, driven entirely by the bank's own funding costs.

    **Feedback loop mechanism:**

    The feedback loop operates as follows:

    1. **Initial stress:** Market disruption causes losses and increases volatility.
    2. **Funding spread widens:** The bank's credit quality perception deteriorates, raising its borrowing costs from $s_F = 50$ bp to $s_F = 300$ bp.
    3. **FVA losses materialize:** Higher funding costs create FVA-driven mark-to-market losses on the uncollateralized portfolio, as computed above.
    4. **Capital erosion:** These losses reduce the bank's capital, further impairing its creditworthiness.
    5. **Further funding deterioration:** Reduced capital and perceived weakness cause the bank's funding spread to widen even further.
    6. **Margin calls and collateral demands:** Counterparties may demand additional collateral or refuse to roll over funding, creating acute liquidity needs.
    7. **Forced deleveraging:** The bank may be forced to sell assets (including liquid derivatives) at distressed prices to meet funding needs.
    8. **Market-wide contagion:** Multiple banks experiencing the same feedback loop sell simultaneously, depressing prices and increasing volatility, amplifying step 1.

    This procyclical feedback is why funding constraints are particularly dangerous during crises: the cost of funding rises precisely when the bank most needs funding, creating a self-reinforcing spiral that can lead to systemic stress.

---

**Exercise 4.** Compare the pricing of a fully collateralized derivative versus an uncollateralized one. How do funding constraints manifest in the pricing difference? Derive the relationship between the collateralized price and the uncollateralized price through the funding spread.

??? success "Solution to Exercise 4"
    **Collateralized versus uncollateralized derivative pricing.**

    **Fully collateralized derivative:**

    When a derivative is fully collateralized (with daily variation margin at the risk-free rate), the standard risk-neutral pricing formula applies:

    $$
    V_0^{\text{coll}} = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r(s)\,ds} \cdot \text{Payoff}\right]
    $$

    The collateral earns the OIS rate $r(t)$, and the derivative is discounted at OIS. There is no funding cost because any positive exposure is offset by collateral received, and any negative exposure is offset by collateral posted (which is remunerated at OIS).

    **Uncollateralized derivative:**

    Without collateral, the bank must fund positive exposures at its borrowing rate $r(t) + s_F(t)$. The price becomes:

    $$
    V_0^{\text{uncoll}} = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T (r(s) + s_F(s) \cdot \mathbf{1}_{V_s > 0})\,ds} \cdot \text{Payoff}\right]
    $$

    **Relationship through the funding spread:**

    The difference between the two prices is the FVA:

    $$
    V_0^{\text{uncoll}} = V_0^{\text{coll}} - \text{FVA}
    $$

    **Derivation:** Consider the self-financing equation for the hedging portfolio. Under collateralization, the portfolio value $V_t$ satisfies:

    $$
    dV_t = r(t) V_t \, dt + \text{hedge terms}
    $$

    Without collateral, the bank funds positive exposure at $r + s_F$ and invests negative exposure at $r$:

    $$
    dV_t = \left[r(t) + s_F(t) \cdot \mathbf{1}_{V_t > 0}\right] V_t \, dt + \text{hedge terms}
    $$

    The FVA is obtained by taking the difference. Using a first-order approximation (treating $V_t$ as known from the collateralized valuation):

    $$
    \text{FVA} = V_0^{\text{coll}} - V_0^{\text{uncoll}} = \int_0^T s_F(t) \cdot \mathbb{E}^{\mathbb{Q}}[V_t^+ ] \cdot D(0,t) \, dt
    $$

    where $D(0,t) = e^{-\int_0^t r(s)\,ds}$ is the OIS discount factor and $V_t^+ = \max(V_t, 0)$.

    **Key observations:**

    - The uncollateralized price is always lower than the collateralized price (from the bank's perspective for a positive-value trade) because of the funding cost.
    - The difference is linear in the funding spread $s_F$ to first order.
    - The FVA makes the uncollateralized price path-dependent and nonlinear, since $\mathbf{1}_{V_t > 0}$ depends on whether the exposure is positive or negative at each point.

---

**Exercise 5.** A hedge fund faces margin constraints: it can post at most \$100M in collateral. Explain how this limit constrains the fund's derivative trading strategy. What is the cost of the constraint in terms of foregone trading opportunities?

??? success "Solution to Exercise 5"
    **Margin constraints on a hedge fund's derivative strategy.**

    **How the collateral limit constrains trading:**

    A hedge fund with a \$100M collateral limit faces constraints on both initial margin (IM) and variation margin (VM):

    1. **Position sizing:** Each derivative position requires initial margin, typically computed via SIMM (Standard Initial Margin Model) based on portfolio sensitivities. If a single interest rate swap requires \$5M IM, the fund can hold at most approximately 20 such swaps before exhausting its collateral capacity.

    2. **Portfolio composition:** The constraint forces the fund to allocate collateral across positions:

        $$
        \sum_{i=1}^{N} \text{IM}_i + \text{VM buffer} \le \$100\text{M}
        $$

        The fund must reserve a buffer for variation margin calls, since adverse market moves will increase VM requirements. A prudent buffer might be 20-30% of total capacity.

    3. **Strategy limitations:**
        - Cannot take large directional bets that consume significant margin.
        - Basis trades and relative value strategies are constrained by the total margin requirement of both legs.
        - Tail hedges (e.g., deep OTM options) may be expensive in margin terms relative to their premium.
        - Netting benefits become critical: offsetting positions reduce total margin.

    **Cost of the constraint in foregone opportunities:**

    The shadow price of the margin constraint represents the marginal value of an additional dollar of collateral capacity. If the fund identifies a trade with expected Sharpe ratio $S$ but cannot execute due to margin constraints, the opportunity cost is:

    $$
    \text{Opportunity Cost} = \sum_{\text{forgone trades}} \text{Expected P\&L}_i - r_f \times \text{IM}_i
    $$

    More formally, the fund solves a constrained optimization:

    $$
    \max_{\mathbf{w}} \mathbb{E}[R_p] - \frac{\lambda}{2} \text{Var}[R_p] \quad \text{s.t.} \quad \sum_i \text{IM}_i(w_i) \le \$100\text{M}
    $$

    The Lagrange multiplier on the margin constraint gives the shadow price: the marginal improvement in risk-adjusted return per additional dollar of collateral. In practice, this shadow price can be significant during volatile markets when margin requirements increase (due to higher SIMM sensitivities), further constraining the fund precisely when opportunities may be most attractive.

    **Procyclical amplification:** During stress, margin requirements increase (wider spreads, higher volatility), VM calls increase, and the effective available collateral shrinks, potentially forcing the fund to reduce positions at the worst possible time.

---

**Exercise 6.** Discuss whether FVA should be considered a "real" valuation adjustment or an internal cost allocation. Summarize the arguments for and against including FVA in derivative prices from the perspectives of (a) the bank's trading desk, (b) the bank's treasury, and (c) economic theory.

??? success "Solution to Exercise 6"
    **FVA: real valuation adjustment versus internal cost allocation.**

    This is one of the most debated topics in quantitative finance. The arguments depend on the perspective:

    **(a) The bank's trading desk perspective -- FVA is a real cost:**

    - The trading desk must fund any positive exposure at the bank's borrowing rate, which is above the risk-free rate. This is a cash cost that directly affects the desk's P&L.
    - If the desk does not charge FVA, it will show a systematic loss equal to the funding cost over the life of the trade. The desk's treasury charges the desk for funding, so the cost is real and unavoidable.
    - Competitive pricing requires FVA: if bank A charges FVA and bank B does not, bank B systematically underprices and loses money on positive-exposure trades while "winning" trades that destroy value.
    - From a desk management perspective, FVA is as real as the cost of office rent or technology infrastructure -- it must be reflected in trade economics.

    **(b) The bank's treasury perspective -- FVA is a funding allocation:**

    - Treasury raises funding for the bank as a whole and allocates costs to business lines. FVA is the derivative desk's share of the bank's aggregate funding cost.
    - Treasury argues FVA should reflect the marginal funding cost, not the average cost. The marginal cost depends on the bank's overall funding position and may differ from the desk-level allocation.
    - Treasury recognizes that FVA creates an incentive for desks to prefer collateralized trades (which have zero FVA) over uncollateralized ones, which is generally desirable behavior.
    - However, treasury also notes that the funding spread includes a credit component (DVA) and double-counting with CVA/DVA must be avoided.

    **(c) Economic theory perspective -- FVA should not exist in prices:**

    - Hull and White (2012) argue that FVA should not be included in derivative prices because it violates the law of one price. Two banks with different funding costs would assign different values to the same derivative, which is inconsistent with no-arbitrage pricing.
    - In the Modigliani-Miller framework, a firm's cost of capital does not depend on its financing decisions. If FVA changes the derivative's price, the bank's shareholders bear the cost regardless, and the derivative's fair value should be independent of who funds it.
    - The risk-neutral pricing framework derives prices from replication arguments that are independent of the hedger's funding costs. The replicating portfolio's cost is determined by the market, not by the bank's credit quality.
    - Counterargument: Modigliani-Miller assumes perfect markets. In reality, there are taxes, bankruptcy costs, and funding frictions. When markets are incomplete and funding is costly, the classical replication argument breaks down, and FVA reflects a genuine market imperfection.

    **Synthesis:** In practice, most major banks now include FVA in their derivative pricing, reflecting the pragmatic view that funding costs are real and must be recovered. The theoretical objections are acknowledged but are viewed as idealized. The practical consensus is that FVA is a real cost in imperfect markets, but it must be carefully computed to avoid double-counting with CVA and DVA.
