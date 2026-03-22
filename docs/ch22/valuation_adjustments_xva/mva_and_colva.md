# MVA and ColVA

Post-crisis regulations mandate initial margin (IM) for both cleared and uncleared derivatives, and collateral posting incurs funding costs that classical risk-neutral pricing ignores. **Margin Valuation Adjustment (MVA)** and **Collateral Valuation Adjustment (ColVA)** quantify these costs, completing the XVA framework alongside CVA, DVA, FVA, and KVA.

---

## Collateral Valuation Adjustment (ColVA)

### Motivation

When a derivative is collateralized, the collateral earns a return (the **collateral rate** $r_C$) that may differ from the risk-free OIS rate $r$. The cost or benefit of this mismatch is ColVA.

### Definition

ColVA captures the funding spread between the collateral rate and the risk-free rate:

$$
\text{ColVA} = \int_0^T (r_C(t) - r(t)) \cdot \mathbb{E}[C_t] \cdot D(0, t) \, dt
$$

where:

- $r_C(t)$ = rate earned on posted collateral
- $r(t)$ = risk-free (OIS) rate
- $C_t$ = collateral balance at time $t$
- $D(0, t)$ = discount factor

### Sign Convention

- If $r_C > r$: ColVA is positive (benefit to collateral poster, who earns excess return)
- If $r_C < r$: ColVA is negative (cost to collateral poster)

### Cash vs Non-Cash Collateral

**Cash collateral:** Typically earns the OIS rate (or a negotiated rate), so ColVA is small. Under standard CSA terms with OIS discounting, ColVA $\approx 0$.

**Non-cash collateral (bonds):** Earns coupons but the collateral receiver may apply a **haircut** $h$:

$$
C_t^{\text{effective}} = (1 - h) \cdot C_t^{\text{posted}}
$$

The poster must over-collateralize by $1/(1 - h)$, creating additional funding costs.

---

## Collateral Choice Option

When the CSA allows multiple types of eligible collateral, the poster holds a **cheapest-to-deliver option**. The value of this option is:

$$
\text{CTO} = \mathbb{E}\left[\int_0^T \left(\max_k r_{C,k}(t) - r(t)\right) C_t \, D(0,t) \, dt\right]
$$

where $r_{C,k}$ is the return on collateral type $k$. The poster optimally switches collateral to maximize the spread $r_{C,k} - r$, and the receiver bears the cost.

---

## Margin Valuation Adjustment (MVA)

### Motivation

Initial margin (IM) must be funded by the posting party but cannot be rehypothecated (reused). This creates a pure funding cost over the trade's lifetime.

### Definition

!!! info "Definition"
    The **Margin Valuation Adjustment** is the present value of the funding cost of initial margin:

    $$
    \text{MVA} = \int_0^T s_F(t) \cdot \mathbb{E}[\text{IM}(t)] \cdot D(0, t) \, dt
    $$

    where $s_F(t) = r_B(t) - r(t)$ is the bank's funding spread.

### Key Properties

- **MVA is always a cost:** IM is always posted (never received net), so MVA $\ge 0$
- **MVA is bilateral:** Both counterparties post IM, so each bears an MVA cost
- **MVA can be substantial:** For long-dated trades, the cumulative funding cost of IM can be material (tens of basis points of notional)
- **MVA is path-dependent:** IM depends on the portfolio's future risk profile, which evolves stochastically

---

## Initial Margin Computation

### ISDA SIMM

The **Standard Initial Margin Model** (SIMM) computes IM from portfolio sensitivities:

$$
\text{IM}_{\text{SIMM}} = \sqrt{\sum_{r} \text{IM}_r^2 + \sum_{r \ne s} \psi_{rs} \cdot \text{IM}_r \cdot \text{IM}_s}
$$

where $\text{IM}_r$ is the margin for risk class $r$ (interest rates, credit, equity, commodity, FX) and $\psi_{rs}$ is the cross-risk-class correlation.

Within each risk class, SIMM aggregates delta, vega, and curvature components:

$$
\text{IM}_r = \sqrt{\text{Delta}_r^2 + \text{Vega}_r^2 + \text{Curvature}_r^2}
$$

where the delta component aggregates across buckets:

$$
\text{Delta}_r = \sqrt{\sum_b K_b^2 + \sum_{b \ne c} \gamma_{bc} \cdot S_b \cdot S_c}
$$

with $K_b$ the within-bucket aggregation and $S_b$ the net sensitivity.

### CCP Initial Margin

CCPs typically compute IM using:

$$
\text{IM} \approx \text{VaR}_{99\%}(\Delta V_\delta) + \text{Add-ons}
$$

where $\delta$ is the MPOR (typically 5 days for liquid products). Common methods include historical VaR, filtered historical simulation, and parametric models.

---

## MVA Computation

### Forward IM Profile

Computing MVA requires the **expected future IM profile** $\mathbb{E}[\text{IM}(t)]$ for all $t \in [0, T]$. This is computationally challenging because:

1. IM at each future time depends on the portfolio's sensitivities at that time
2. Sensitivities depend on the full portfolio composition and market state
3. This creates a **simulation within simulation** problem

### Approaches

**Regression-based (American Monte Carlo):**

1. Simulate market factor paths
2. At each time step, compute portfolio sensitivities
3. Apply SIMM formula to obtain IM on each path
4. Average across paths: $\widehat{\mathbb{E}}[\text{IM}(t)] = \frac{1}{M} \sum_{m=1}^M \text{IM}_t^{(m)}$
5. Compute MVA via numerical integration

**Sensitivity approximation:**

Approximate future IM using current sensitivities scaled by factor dynamics:

$$
\text{IM}(t) \approx \text{IM}(0) \cdot g(t)
$$

where $g(t)$ captures the expected decay of sensitivities over time (e.g., for a swap, sensitivities decay toward zero as the swap amortizes).

### MVA as a Percentage of Notional

For a vanilla interest rate swap, typical MVA ranges are:

| Maturity | MVA (bps of notional) |
|----------|----------------------|
| 5 years | 2--5 bps |
| 10 years | 8--15 bps |
| 20 years | 20--40 bps |
| 30 years | 40--80 bps |

These values depend on the funding spread and whether the trade is cleared or bilateral.

---

## KVA Overview

### Definition

The **Capital Valuation Adjustment** represents the cost of holding regulatory capital over the trade's life:

$$
\text{KVA} = \int_0^T h \cdot K(t) \cdot S_B(t) \cdot D(0, t) \, dt
$$

where:

- $h$ = hurdle rate (return on equity demanded by shareholders, typically 8--15%)
- $K(t)$ = regulatory capital requirement
- $S_B(t)$ = bank's survival probability
- $D(0, t)$ = discount factor

### Capital Components

$$
K(t) = K^{\text{default}}(t) + K^{\text{CVA}}(t) + K^{\text{market}}(t)
$$

- **Default risk capital:** Based on counterparty EAD and credit quality
- **CVA capital:** Capital for CVA variability (SA-CVA or BA-CVA)
- **Market risk capital:** FRTB-based capital for trading book risk

### KVA and the Hurdle Rate

The hurdle rate $h$ reflects the equity cost of capital. If $\text{ROE}_{\text{target}} = 12\%$ and the risk-free rate is 3\%, then $h = 12\% - 3\% = 9\%$ is the excess return demanded on regulatory capital.

**KVA interpretation:** A trade that consumes \$10M of capital for 5 years at $h = 10\%$ has:

$$
\text{KVA} \approx 10\text{M} \times 0.10 \times 5 = \$5\text{M}
$$

(simplified; actual computation accounts for the time profile of $K(t)$.)

---

## Interactions Among MVA, ColVA, and Other XVAs

### MVA vs FVA

- **FVA** funds the uncollateralized portion of derivative exposure
- **MVA** funds the initial margin (which is segregated and cannot offset FVA)
- Under full collateralization, FVA is small but MVA remains

### Double-Counting Prevention

The total XVA must avoid double-counting:

$$
V^{\text{total}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA} - \text{FVA} - \text{ColVA} - \text{MVA} - \text{KVA}
$$

Key overlaps to manage:

- **DVA and FVA:** Both depend on the bank's own credit; must use a consistent funding/credit framework
- **ColVA and FVA:** ColVA handles the collateral rate mismatch; FVA handles the uncollateralized funding cost
- **MVA and KVA:** Both are costs of regulatory requirements but address different constraints (margin vs capital)

### Impact on Trade Economics

For a 10-year uncollateralized interest rate swap with notional \$100M:

| Adjustment | Typical Range |
|------------|--------------|
| CVA | 20--50 bps |
| DVA | 10--30 bps (benefit) |
| FVA | 5--20 bps |
| MVA | 10--30 bps |
| KVA | 10--25 bps |
| ColVA | 0--5 bps |

**Total XVA** can represent 50--100+ bps of notional for long-dated uncollateralized trades, fundamentally affecting trade economics and pricing.

---

## BSDE Formulation Including MVA

The unified BSDE framework extends to include MVA:

$$
V_t = \xi + \int_t^T f(s, V_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$

with an extended driver:

$$
f(t, V, Z) = -rV + \lambda_C \cdot \text{LGD}_C \cdot V^+ - \lambda_B \cdot \text{LGD}_B \cdot V^- + s_F(V - C)^+ + s_F \cdot \text{IM}(t, V, Z)
$$

The last term, $s_F \cdot \text{IM}(t, V, Z)$, represents the MVA contribution. Since IM depends on portfolio sensitivities (which relate to $Z$ in the BSDE), this creates additional nonlinearity in the driver.

**Existence and uniqueness** still hold under standard Lipschitz conditions on $f$, but the IM dependence on $Z$ complicates numerical solution and may require iterative schemes.

---

## Example: MVA Calculation

**Setup:** 10-year cleared interest rate swap, notional \$100M.

**Assumptions:**

- Funding spread: $s_F = 80$ bps
- CCP IM: \$5M initially, decaying linearly to zero at maturity
- IM profile: $\text{IM}(t) = 5 \times (1 - t/10)$ million

**MVA computation:**

$$
\text{MVA} = s_F \int_0^{10} \text{IM}(t) \cdot e^{-rt} \, dt \approx 0.008 \int_0^{10} 5(1 - t/10) \cdot e^{-0.03t} \, dt
$$

$$
= 0.04 \int_0^{10} (1 - t/10) \cdot e^{-0.03t} \, dt
$$

Evaluating the integral:

$$
\int_0^{10} e^{-0.03t} \, dt = \frac{1 - e^{-0.3}}{0.03} \approx 8.64
$$

$$
\int_0^{10} \frac{t}{10} e^{-0.03t} \, dt \approx 3.86
$$

$$
\text{MVA} \approx 0.04 \times (8.64 - 3.86) = 0.04 \times 4.78 \approx \$0.19\text{M}
$$

This represents approximately 1.9 bps of notional per annum.

---

## Key Takeaways

- ColVA captures the cost of collateral rate mismatches; it is small for cash-collateralized trades with OIS discounting
- MVA is the present value of funding costs for initial margin, which cannot be rehypothecated
- MVA is always a cost and can be substantial for long-dated trades (tens of basis points)
- ISDA SIMM provides a standardized sensitivity-based approach to IM computation
- KVA represents the cost of regulatory capital at the bank's hurdle rate
- The BSDE framework unifies all XVAs, with MVA adding nonlinearity through IM dependence on portfolio sensitivities
- Total XVA (CVA + DVA + FVA + ColVA + MVA + KVA) can materially affect trade pricing and profitability

---

## Further Reading

- Green, A. & Kenyon, C. (2015), "MVA: Initial Margin Valuation Adjustment by Replication and Regression"
- Andersen, L., Duffie, D., & Song, Y. (2019), "Funding Value Adjustments"
- Albanese, C., Caenazzo, S., & Crepey, S. (2017), "Capital Valuation Adjustment and Funding Valuation Adjustment"
- ISDA (2022), "ISDA SIMM Methodology"
- Crépey, S., Bielecki, T., & Brigo, D. (2014), *Counterparty Risk and Funding: A Tale of Two Puzzles*
- Anfuso, F., Aziz, D., Giltinan, P., & Loukopoulos, K. (2017), "A Sound Modelling and Backtesting Framework for Forecasting Initial Margin Requirements"
