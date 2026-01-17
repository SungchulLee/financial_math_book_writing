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
