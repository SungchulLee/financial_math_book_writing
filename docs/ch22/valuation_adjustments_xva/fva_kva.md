# FVA, KVA, and MVA

Beyond credit risk, derivative valuation must account for **funding costs**, **capital costs**, and **margin costs**. These adjustments—FVA, KVA, and MVA—extend pricing beyond the classical risk-neutral framework.

---

## Funding Valuation Adjustment (FVA)

### Motivation

Classical derivative pricing assumes:
- Borrowing and lending at the risk-free rate
- No funding constraints
- Perfect market access

**Reality:** Banks fund uncollateralized positions at rates above risk-free, creating funding costs that must be priced.

### Definition

FVA reflects the cost (or benefit) of funding uncollateralized derivative positions:

$$
\text{FVA} = \int_0^T s_F(t) \cdot \mathbb{E}[\text{Funding Exposure}(t)] \cdot D(0,t) \, dt
$$

where $s_F(t)$ is the funding spread (bank's borrowing rate minus risk-free rate).

### Funding Exposure

**Positive derivative value:** Bank must fund the asset
$$
\text{Funding Cost} = s_F \cdot V^+ \cdot dt
$$

**Negative derivative value:** Bank receives funding benefit
$$
\text{Funding Benefit} = s_F \cdot V^- \cdot dt
$$

### Symmetric vs Asymmetric FVA

**Symmetric FVA:**
$$
\text{FVA} = \int_0^T s_F(t) \cdot \mathbb{E}[V_t] \cdot D(0,t) \, dt
$$

**Asymmetric FVA:** Different rates for borrowing ($s_F^+$) and lending ($s_F^-$):
$$
\text{FVA} = \int_0^T \left[s_F^+(t) \cdot \mathbb{E}[V_t^+] - s_F^-(t) \cdot \mathbb{E}[V_t^-]\right] D(0,t) \, dt
$$

---

## Capital Valuation Adjustment (KVA)

### Motivation

Banks must hold regulatory capital against derivative positions. This capital has an opportunity cost—it could be deployed elsewhere for return.

### Definition

KVA reflects the cost of holding regulatory capital over the life of the trade:

$$
\text{KVA} = \int_0^T h \cdot K(t) \cdot S_B(t) \cdot D(0,t) \, dt
$$

where:
- $h$ = hurdle rate (cost of capital, typically 8-15%)
- $K(t)$ = regulatory capital requirement at time $t$
- $S_B(t)$ = bank's survival probability (capital only needed if bank survives)
- $D(0,t)$ = discount factor

### Capital Requirement

For CCR, capital typically includes:
- **Default risk capital:** Based on EAD and counterparty credit quality
- **CVA capital:** Capital for CVA variability
- **Market risk capital:** If derivatives are in trading book

$$
K(t) = K^{\text{default}}(t) + K^{\text{CVA}}(t) + K^{\text{market}}(t)
$$

### KVA Formula

With constant hurdle rate $h$:

$$
\text{KVA} \approx h \cdot \int_0^T K(t) \cdot D(0,t) \, dt
$$

**Example:** If average capital is \$10M over 5 years and $h = 10\%$:
$$
\text{KVA} \approx 0.10 \times 10\text{M} \times 5 \approx \$5\text{M}
$$

(simplified; actual calculation accounts for time profile)

---

## Margin Valuation Adjustment (MVA)

### Motivation

Post-crisis regulations require initial margin (IM) for both cleared and uncleared derivatives. This margin must be funded, creating costs.

### Definition

MVA is the cost of funding initial margin over the life of the trade:

$$
\text{MVA} = \int_0^T s_F(t) \cdot \mathbb{E}[\text{IM}(t)] \cdot D(0,t) \, dt
$$

where $\text{IM}(t)$ is the initial margin requirement at time $t$.

### Initial Margin Calculation

**ISDA SIMM (Standard Initial Margin Model):**
- Risk-sensitive margin based on sensitivities
- Aggregates across risk classes with diversification

**Regulatory IM:**
- Schedule-based or grid approaches
- Less risk-sensitive but simpler

### MVA Characteristics

- MVA is always a cost (IM must be posted, not received net)
- MVA can be substantial for long-dated trades
- IM profile depends on trade structure and model

---

## Interactions Between XVAs

### Double Counting Concerns

**DVA and FVA overlap:**
- DVA reflects benefit from own default
- FVA funding benefit also reduces when bank defaults
- Must avoid counting the same effect twice

**Resolution:** Use consistent framework (typically BSDE-based) that accounts for interactions.

### Hierarchy

Common ordering by materiality:
1. **CVA:** Usually largest for uncollateralized trades
2. **FVA:** Significant for funding-intensive positions
3. **MVA:** Growing importance post-IM rules
4. **KVA:** Often smaller but can be material

### Non-Additivity

XVAs are **not additive** across trades:
$$
\text{XVA}(A + B) \ne \text{XVA}(A) + \text{XVA}(B)
$$

due to netting, collateral, and capital effects.

---

## Total Valuation Adjustment

### XVA-Inclusive Price

$$
V^{\text{total}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA} - \text{FVA} - \text{KVA} - \text{MVA}
$$

**Note:** Signs may vary by convention; FVA and MVA are typically costs (negative adjustments).

### Simplified Notation

$$
V^{\text{total}} = V^{\text{clean}} - \text{XVA}
$$

where XVA is the total adjustment.

---

## BSDE Framework for XVA

XVA pricing can be formulated as a **backward stochastic differential equation**:

$$
V_t = \text{Payoff}_T + \int_t^T g(s, V_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$

where the driver $g$ incorporates:
- Credit risk (CVA/DVA)
- Funding costs (FVA)
- Collateral effects

**Example driver:**
$$
g(t, V, Z) = -r V + s_F V^+ - s_L V^- + \lambda_C (V^+ - \text{collateral}) + \cdots
$$

### Advantages of BSDE Approach

- Unified framework for all XVAs
- Handles interactions consistently
- Connects to hedging strategies

---

## XVA Desk Organization

### Centralized XVA Management

Modern banks typically have a dedicated **XVA desk** that:
- Calculates XVA for all trades
- Manages XVA hedging
- Charges/credits business units
- Reports XVA P&L

### Transfer Pricing

Business units charged for XVA at trade inception:
$$
\text{Trade Price} = V^{\text{clean}} - \text{XVA charge}
$$

XVA desk then owns and manages the XVA risk.

---

## Practical Considerations

### Model Dependence

XVA calculations require:
- Exposure simulation models
- Credit spread curves
- Funding curves
- Capital models

Each introduces model risk.

### Hedgeability

| XVA | Hedgeable? | Instruments |
|-----|------------|-------------|
| CVA | Partially | CDS, contingent CDS |
| DVA | No | Cannot sell protection on self |
| FVA | Partially | Funding instruments |
| KVA | No | Capital cannot be hedged |
| MVA | Partially | IM-reducing trades |

### Accounting vs Economic

- **Accounting:** CVA and DVA required; FVA debated
- **Economic:** All XVAs affect trade profitability
- **Regulatory:** CVA capital required; DVA excluded

---

## Example: Complete XVA Calculation

**Trade:** 10-year uncollateralized interest rate swap, \$100M notional

**Inputs:**
- EE profile: peaks at \$8M (year 5)
- NEE profile: peaks at \$7M
- Counterparty spread: 150 bps, LGD: 60%
- Bank spread: 100 bps, LGD: 60%
- Funding spread: 80 bps
- Hurdle rate: 12%
- Average capital: \$2M

**Calculations:**

| Adjustment | Formula | Value |
|------------|---------|-------|
| CVA | LGD × ∫ EE × dPD | \$2.1M |
| DVA | LGD × ∫ NEE × dPD_B | \$1.2M |
| FVA | s_F × ∫ (EE - NEE) × D | \$0.4M |
| KVA | h × ∫ K × D | \$1.8M |

**Total adjustment:**
$$
\text{XVA} = 2.1 - 1.2 + 0.4 + 1.8 = \$3.1\text{M}
$$

---

## Key Takeaways

- FVA captures funding costs for uncollateralized positions
- KVA reflects the opportunity cost of regulatory capital
- MVA accounts for initial margin funding costs
- XVAs interact and are not simply additive
- BSDE framework provides consistent treatment
- XVA desk centralizes management and hedging
- Model risk is significant across all XVA calculations

---

## Further Reading

- Burgard, C. & Kjaer, M. (2011), "Partial Differential Equation Representations of Derivatives with Bilateral Counterparty Risk and Funding Costs"
- Green, A., Kenyon, C., & Dennis, C.R. (2014), "KVA: Capital Valuation Adjustment by Replication"
- Albanese, C. et al. (2015), "Coherent Global Market Simulations and Securitization Measures for Counterparty Credit Risk"
- Crépey, S., Bielecki, T., & Brigo, D. (2014), *Counterparty Risk and Funding: A Tale of Two Puzzles*
- Andersen, L., Duffie, D., & Song, Y. (2019), "Funding Value Adjustments"
