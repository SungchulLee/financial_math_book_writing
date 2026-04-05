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

---

## Exercises

**Exercise 1.** A 10-year cleared interest rate swap with notional \$200M has an initial margin profile $\text{IM}(t) = 8(1 - t/10)$ million (linearly decaying). The bank's funding spread is 70 bps. Compute the MVA using

$$
\text{MVA} = s_F \int_0^{10} \text{IM}(t) \cdot e^{-rt} \, dt
$$

with $r = 3\%$. Express the result in basis points of notional per annum.

??? success "Solution to Exercise 1"
    With $\text{IM}(t) = 8(1 - t/10)$ million, $s_F = 70$ bps $= 0.007$, and $r = 3\%$:

    $$
    \text{MVA} = s_F \int_0^{10} \text{IM}(t) \cdot e^{-rt} \, dt = 0.007 \int_0^{10} 8\left(1 - \frac{t}{10}\right) e^{-0.03t} \, dt
    $$

    $$
    = 0.056 \int_0^{10} \left(1 - \frac{t}{10}\right) e^{-0.03t} \, dt
    $$

    We need two integrals:

    $$
    I_1 = \int_0^{10} e^{-0.03t} \, dt = \frac{1 - e^{-0.3}}{0.03} = \frac{1 - 0.7408}{0.03} = \frac{0.2592}{0.03} = 8.640
    $$

    $$
    I_2 = \int_0^{10} \frac{t}{10} e^{-0.03t} \, dt = \frac{1}{10} \int_0^{10} t \, e^{-0.03t} \, dt
    $$

    Using integration by parts for $\int_0^{10} t \, e^{-0.03t} \, dt$:

    $$
    \int_0^{10} t \, e^{-0.03t} \, dt = \left[-\frac{t}{0.03} e^{-0.03t}\right]_0^{10} + \frac{1}{0.03}\int_0^{10} e^{-0.03t} \, dt
    $$

    $$
    = -\frac{10}{0.03} e^{-0.3} + \frac{1}{0.03} \times 8.640 = -333.33 \times 0.7408 + 288.0 = -246.93 + 288.0 = 41.07
    $$

    Therefore:

    $$
    I_2 = \frac{41.07}{10} = 4.107
    $$

    **MVA computation:**

    $$
    \text{MVA} = 0.056 \times (8.640 - 4.107) = 0.056 \times 4.533 = \$0.254\text{M}
    $$

    **Expressing in basis points of notional per annum.**

    The notional is \$200M, and the trade has a 10-year life:

    $$
    \text{MVA per annum} = \frac{0.254}{10} = \$0.0254\text{M/year}
    $$

    $$
    \text{In bps of notional} = \frac{0.0254}{200} \times 10{,}000 = 1.27 \text{ bps per annum}
    $$

    The MVA is approximately **\$254,000** or **1.27 bps of notional per annum**.

---

**Exercise 2.** A CSA allows the poster to choose between cash (earning OIS rate $r = 2.5\%$) and government bonds (earning coupon rate $r_C = 3.0\%$, subject to haircut $h = 5\%$). The collateral amount is \$50M. Compute the ColVA for each collateral type over 1 year. Which is the cheapest-to-deliver? Explain the collateral choice option and who benefits from it.

??? success "Solution to Exercise 2"
    **Cash collateral ColVA.**

    With cash earning the OIS rate $r_C = r = 2.5\%$, the spread is zero:

    $$
    \text{ColVA}_{\text{cash}} = (r_C - r) \cdot C \cdot 1 = (0.025 - 0.025) \times 50 \times 1 = \$0
    $$

    **Government bond collateral ColVA.**

    The bond earns coupon rate $r_C = 3.0\%$, but the haircut $h = 5\%$ means the poster must deliver $C^{\text{posted}} = 50 / (1 - 0.05) = \$52.63$M to cover the \$50M requirement. The excess collateral $\$2.63$M must be funded but earns no return to the poster.

    The ColVA from the rate mismatch on the effective collateral:

    $$
    \text{ColVA}_{\text{bond}} = (r_C - r) \cdot C \cdot 1 - s_F \cdot h \cdot C^{\text{posted}} \cdot 1
    $$

    The first term is the rate benefit:

    $$
    (0.030 - 0.025) \times 50 \times 1 = 0.005 \times 50 = \$0.25\text{M}
    $$

    However, the poster must fund the haircut amount. If the poster's funding cost is, say, the OIS rate (minimum), the over-collateralization cost is approximately:

    $$
    \text{Haircut cost} \approx r \cdot h \cdot C^{\text{posted}} = 0.025 \times 0.05 \times 52.63 = \$0.066\text{M}
    $$

    Net ColVA for bonds:

    $$
    \text{ColVA}_{\text{bond}} \approx 0.25 - 0.066 = \$0.184\text{M}
    $$

    **Cheapest-to-deliver analysis.**

    The bond collateral has ColVA of \$0.184M (benefit), while cash has ColVA of \$0. Therefore, government bonds are the cheapest-to-deliver from the poster's perspective, as the coupon excess over OIS more than compensates for the haircut cost.

    **The collateral choice option.**

    The CSA gives the poster the right to choose which collateral to deliver at any point. This is a cheapest-to-deliver option. The poster will optimally switch between cash and bonds depending on market conditions:

    - When bond yields are high relative to OIS: post bonds (earn excess coupon)
    - When bond yields fall below OIS: post cash (avoid negative spread)

    The option benefits the **poster** (who can optimize) and costs the **receiver** (who accepts whichever collateral is cheapest for the poster). The value of this option increases with the volatility of the spread $r_C - r$ and the number of eligible collateral types.

---

**Exercise 3.** A trade requires average regulatory capital of \$5M over 7 years, with the bank's hurdle rate $h = 11\%$, survival probability $S_B(t) = e^{-0.01t}$, and discount rate $r = 3\%$. Compute the KVA using

$$
\text{KVA} = h \int_0^T K(t) \cdot S_B(t) \cdot D(0,t) \, dt
$$

Why does the bank's survival probability appear in the formula? What happens to KVA if the bank's credit quality deteriorates significantly?

??? success "Solution to Exercise 3"
    **KVA computation.**

    With $h = 11\%$, $K(t) = \$5$M (constant), $S_B(t) = e^{-0.01t}$, and $r = 3\%$:

    $$
    \text{KVA} = h \int_0^7 K(t) \cdot S_B(t) \cdot D(0,t) \, dt = 0.11 \times 5 \int_0^7 e^{-0.01t} \cdot e^{-0.03t} \, dt
    $$

    $$
    = 0.55 \int_0^7 e^{-0.04t} \, dt = 0.55 \times \frac{1 - e^{-0.28}}{0.04}
    $$

    $$
    = 0.55 \times \frac{1 - 0.7558}{0.04} = 0.55 \times \frac{0.2442}{0.04} = 0.55 \times 6.105 = \$3.358\text{M}
    $$

    **Why does the bank's survival probability appear?**

    The bank only needs to hold regulatory capital while it is alive and operating. If the bank defaults at time $\tau_B$, it no longer holds capital beyond $\tau_B$. Therefore, the cost of capital at future time $t$ should be weighted by the probability that the bank survives to time $t$:

    $$
    \text{KVA} = \int_0^T h \cdot K(t) \cdot \underbrace{S_B(t)}_{\text{probability capital is needed}} \cdot D(0,t) \, dt
    $$

    This is analogous to a life annuity: the bank "pays" $h \cdot K(t)$ per year in capital opportunity cost, but only while it survives.

    **Effect of significant credit deterioration.**

    If the bank's credit quality deteriorates significantly, $S_B(t)$ decreases faster (the hazard rate increases). For example, if the hazard rate doubles to 2%:

    $$
    \text{KVA}' = 0.55 \int_0^7 e^{-0.05t} \, dt = 0.55 \times \frac{1 - e^{-0.35}}{0.05} = 0.55 \times \frac{0.2953}{0.05} = 0.55 \times 5.906 = \$3.248\text{M}
    $$

    Paradoxically, KVA *decreases* as the bank's credit worsens (from \$3.358M to \$3.248M). This parallels the DVA paradox: a bank that is more likely to default faces lower expected future capital costs because it is less likely to survive to bear them. This creates a perverse incentive and is one reason regulators may question the inclusion of $S_B(t)$ in KVA calculations for pricing purposes.

---

**Exercise 4.** Explain why MVA is always a cost (never a benefit) to the posting institution, while FVA can be either a cost or a benefit depending on the sign of the derivative's value. For a fully collateralized trade where FVA is approximately zero, the MVA may still be substantial. Provide a numerical example: a 20-year swap with IM averaging \$15M and funding spread of 90 bps. Compare this MVA to a typical bid-ask spread for the same swap.

??? success "Solution to Exercise 4"
    **Why MVA is always a cost.**

    Initial margin is *bilateral*: both parties post IM to protect against the other's default. The key features are:

    1. IM is always *posted* (never received net for the purpose of IM). Each party posts IM based on the risk the other party faces.
    2. Posted IM cannot be rehypothecated -- it is held in a segregated account and cannot be used by the receiver to offset funding needs.
    3. The poster must fund the IM at their borrowing rate, but the IM earns at most the risk-free rate (or a contractually specified rate, usually lower than the funding rate).

    Therefore, $\text{MVA} = s_F \cdot \mathbb{E}[\text{IM}] \cdot \text{Duration} \ge 0$ always, since $s_F > 0$ and $\text{IM} \ge 0$.

    In contrast, FVA can be negative (a benefit) because derivative values can be negative, in which case the bank receives cash that it can invest at a rate above risk-free.

    **Numerical example: 20-year swap.**

    With IM averaging \$15M, funding spread $s_F = 90$ bps $= 0.009$, and $r = 3\%$:

    $$
    \text{MVA} = 0.009 \times 15 \int_0^{20} e^{-0.03t} \, dt = 0.135 \times \frac{1 - e^{-0.6}}{0.03}
    $$

    $$
    = 0.135 \times \frac{1 - 0.5488}{0.03} = 0.135 \times 15.04 = \$2.030\text{M}
    $$

    As a percentage of notional (assuming \$100M notional):

    $$
    \text{MVA in bps} = \frac{2.030}{100} \times 10{,}000 = 203 \text{ bps total, or } \frac{203}{20} \approx 10.2 \text{ bps per annum}
    $$

    **Comparison to bid-ask spread.**

    A typical bid-ask spread for a 20-year plain vanilla interest rate swap is approximately 0.5-2 bps of running spread (annualized). The MVA of 10.2 bps per annum is **5-20 times larger** than the typical bid-ask spread. This means MVA alone exceeds the trading profit margin, making the trade economically unattractive unless the counterparty compensates for the MVA cost through a wider spread.

---

**Exercise 5.** The ISDA SIMM aggregation formula is

$$
\text{IM}_{\text{SIMM}} = \sqrt{\sum_{r} \text{IM}_r^2 + \sum_{r \ne s} \psi_{rs} \cdot \text{IM}_r \cdot \text{IM}_s}
$$

Consider a portfolio with exposures to interest rates ($\text{IM}_{\text{IR}} = \$8$M), credit ($\text{IM}_{\text{CR}} = \$5$M), and equity ($\text{IM}_{\text{EQ}} = \$3$M), with cross-correlations $\psi_{\text{IR,CR}} = 0.25$, $\psi_{\text{IR,EQ}} = 0.15$, $\psi_{\text{CR,EQ}} = 0.20$. Compute the total SIMM IM. Compare this to the sum of individual IMs and discuss the diversification benefit.

??? success "Solution to Exercise 5"
    **SIMM IM computation.**

    With $\text{IM}_{\text{IR}} = 8$, $\text{IM}_{\text{CR}} = 5$, $\text{IM}_{\text{EQ}} = 3$ (all in \$M):

    $$
    \text{IM}_{\text{SIMM}} = \sqrt{\sum_r \text{IM}_r^2 + \sum_{r \ne s} \psi_{rs} \cdot \text{IM}_r \cdot \text{IM}_s}
    $$

    **Sum of squared terms:**

    $$
    \sum_r \text{IM}_r^2 = 8^2 + 5^2 + 3^2 = 64 + 25 + 9 = 98
    $$

    **Cross terms** (each pair appears twice: $r \ne s$ and $s \ne r$):

    $$
    \sum_{r \ne s} \psi_{rs} \cdot \text{IM}_r \cdot \text{IM}_s = 2 \times (0.25 \times 8 \times 5 + 0.15 \times 8 \times 3 + 0.20 \times 5 \times 3)
    $$

    $$
    = 2 \times (10.0 + 3.6 + 3.0) = 2 \times 16.6 = 33.2
    $$

    **Total SIMM IM:**

    $$
    \text{IM}_{\text{SIMM}} = \sqrt{98 + 33.2} = \sqrt{131.2} = \$11.45\text{M}
    $$

    **Comparison to sum of individual IMs:**

    $$
    \text{IM}_{\text{sum}} = 8 + 5 + 3 = \$16.0\text{M}
    $$

    **Diversification benefit:**

    $$
    \text{Diversification benefit} = 16.0 - 11.45 = \$4.55\text{M}
    $$

    $$
    \text{As a percentage} = \frac{4.55}{16.0} \times 100\% = 28.4\%
    $$

    The SIMM aggregation recognizes that losses across risk classes are imperfectly correlated. The relatively low cross-correlations ($\psi \le 0.25$) produce substantial diversification, reducing the total IM by 28.4% compared to the simple sum. This directly reduces MVA by the same proportion, providing a significant cost saving for diversified portfolios.

---

**Exercise 6.** In the BSDE formulation including MVA, the driver is

$$
f(t, V, Z) = -rV + \lambda_C \cdot \text{LGD}_C \cdot V^+ - \lambda_B \cdot \text{LGD}_B \cdot V^- + s_F(V - C)^+ + s_F \cdot \text{IM}(t, V, Z)
$$

Explain why the IM term depends on $Z$ (the hedging process / sensitivity) through the SIMM formula. What computational challenge does this create for solving the BSDE numerically? Describe the "simulation within simulation" problem and one approach to overcome it.

??? success "Solution to Exercise 6"
    **Why the IM term depends on $Z$.**

    In the BSDE framework, $Z_t = \sigma(t, X_t) \cdot \partial_x V(t, X_t)$ represents the portfolio's sensitivity (delta) to the underlying risk factors. The ISDA SIMM formula computes initial margin based on portfolio *sensitivities* (deltas, vegas, curvatures):

    $$
    \text{IM}(t) = \text{SIMM}(\text{sensitivities at time } t) = \text{SIMM}\left(\frac{\partial V}{\partial x_1}, \frac{\partial V}{\partial x_2}, \ldots\right)
    $$

    Since the BSDE control $Z$ is proportional to these sensitivities, IM is effectively a function of $Z$:

    $$
    \text{IM}(t, V, Z) = \text{SIMM}(Z / \sigma)
    $$

    This makes the BSDE driver $f(t, V, Z)$ depend on $Z$ through the MVA term $s_F \cdot \text{IM}(t, V, Z)$, unlike the standard XVA BSDE where $f$ depends only on $V$.

    **Computational challenge: "simulation within simulation."**

    To compute MVA, we need the expected future IM profile $\mathbb{E}[\text{IM}(t)]$ for all $t \in [0, T]$. This requires:

    1. **Outer simulation:** Simulate market factor paths $\{X_t^{(m)}\}$ forward in time.
    2. **Inner computation:** At each future time $t$ on each path $m$, compute the portfolio's sensitivities at that state. This requires either:
        - Repricing the entire portfolio with bumped risk factors (finite difference Greeks), or
        - Solving an inner pricing problem conditional on $X_t^{(m)}$

    This creates a nested simulation problem with computational cost $O(M \times N \times P)$, where $M$ is the number of outer paths, $N$ is the number of time steps, and $P$ is the cost of computing sensitivities at each node.

    **Approaches to overcome this:**

    1. **Regression-based (American Monte Carlo):** Instead of repricing at each node, use regression (Longstaff-Schwartz style) to approximate sensitivities as functions of state variables. At each time step, regress portfolio value (or Greeks) on basis functions of the current state, then evaluate SIMM on the regressed sensitivities. This reduces the problem from $O(M \times N \times P)$ to $O(M \times N \times B)$, where $B$ is the cost of regression evaluation (much cheaper than full repricing).

    2. **Sensitivity scaling:** Approximate future sensitivities by scaling current sensitivities with a deterministic decay function: $\text{IM}(t) \approx \text{IM}(0) \cdot g(t)$, where $g(t)$ captures the expected evolution of sensitivities (e.g., for a swap, sensitivities decay as the swap amortizes). This avoids inner simulation entirely but sacrifices accuracy.

    3. **Deep learning:** Train neural networks to approximate the map from state variables to portfolio sensitivities, then evaluate SIMM on the neural network output. This provides fast evaluation once trained.

---

**Exercise 7.** For a 10-year uncollateralized interest rate swap with \$100M notional, the typical XVA ranges are: CVA 20-50 bps, DVA 10-30 bps (benefit), FVA 5-20 bps, MVA 10-30 bps, KVA 10-25 bps, ColVA 0-5 bps. Taking midpoint values, compute the total XVA in dollar terms and as a percentage of notional. If the swap's clean mid-market value is \$0 (at-market), what upfront fee or running spread would the bank need to charge to break even on XVA? Discuss how this affects the bank's competitiveness.

??? success "Solution to Exercise 7"
    **Midpoint XVA values** (in bps of \$100M notional):

    | Component | Midpoint (bps) | Dollar Value (\$) |
    |-----------|---------------|-------------------|
    | CVA | 35 | 350,000 |
    | DVA (benefit) | -20 | -200,000 |
    | FVA | 12.5 | 125,000 |
    | MVA | 20 | 200,000 |
    | KVA | 17.5 | 175,000 |
    | ColVA | 2.5 | 25,000 |

    **Total XVA:**

    $$
    \text{XVA} = 35 - 20 + 12.5 + 20 + 17.5 + 2.5 = 67.5 \text{ bps}
    $$

    In dollar terms:

    $$
    \text{XVA} = 67.5 \times \frac{100{,}000{,}000}{10{,}000} = \$675{,}000
    $$

    As a percentage of notional: $67.5 / 10{,}000 = 0.675\%$.

    **Upfront fee or running spread to break even.**

    *Upfront fee:* The bank would need to charge approximately **\$675,000** upfront.

    *Running spread:* To convert to a running spread over 10 years, divide by the present value of a 10-year annuity. With $r = 3\%$:

    $$
    \text{PV01 (annuity)} = \frac{1 - e^{-0.03 \times 10}}{0.03} = \frac{0.2592}{0.03} = 8.64 \text{ years}
    $$

    $$
    \text{Running spread} = \frac{675{,}000}{100{,}000{,}000 \times 8.64} = \frac{675{,}000}{864{,}000{,}000} = 0.000781 = 7.81 \text{ bps per annum}
    $$

    The bank would need to charge approximately **7.8 bps per annum** above mid-market to break even on XVA.

    **Impact on competitiveness.**

    A charge of 7.8 bps per annum is significant in interest rate swap markets, where typical bid-ask spreads are 0.5-2 bps. This means:

    1. The XVA charge is 4-15 times the normal trading margin, fundamentally altering the economics.
    2. Banks with better credit quality (lower CVA, FVA) or more efficient capital management (lower KVA) can offer tighter spreads.
    3. Banks with large offsetting portfolios benefit from netting, reducing incremental XVA below the standalone level.
    4. This creates strong incentives for central clearing (which reduces CVA and KVA) and collateralization (which reduces FVA), even though these increase MVA.
    5. End-users may shift to standardized, clearable products to avoid the XVA surcharge on bespoke uncollateralized trades.
