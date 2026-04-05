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

---

## Exercises

**Exercise 1.** A bank has a funding spread of 80 bps over the risk-free rate. It enters a 7-year uncollateralized swap with expected positive exposure $\mathbb{E}[V_t^+]$ averaging \$15M and expected negative exposure $\mathbb{E}[V_t^-]$ averaging \$10M over the life. Compute the symmetric FVA using

$$
\text{FVA} = s_F \int_0^T \mathbb{E}[V_t] \cdot D(0,t) \, dt
$$

assuming a flat discount rate of 3%. Also compute the asymmetric FVA if the lending spread is $s_F^- = 40$ bps and the borrowing spread is $s_F^+ = 80$ bps.

??? success "Solution to Exercise 1"
    **Symmetric FVA.**

    The net expected exposure is $\mathbb{E}[V_t] = \mathbb{E}[V_t^+] - \mathbb{E}[V_t^-] = 15 - 10 = \$5$M (constant average over 7 years). With $s_F = 80$ bps $= 0.0080$ and $r = 3\%$:

    $$
    \text{FVA}_{\text{sym}} = s_F \int_0^7 \mathbb{E}[V_t] \cdot D(0,t) \, dt = 0.0080 \times 5 \int_0^7 e^{-0.03t} \, dt
    $$

    Computing the integral:

    $$
    \int_0^7 e^{-0.03t} \, dt = \frac{1 - e^{-0.21}}{0.03} = \frac{1 - 0.8106}{0.03} = \frac{0.1894}{0.03} = 6.313
    $$

    $$
    \text{FVA}_{\text{sym}} = 0.0080 \times 5 \times 6.313 = 0.04 \times 6.313 = \$0.253\text{M}
    $$

    **Asymmetric FVA.**

    With $s_F^+ = 80$ bps (borrowing) and $s_F^- = 40$ bps (lending):

    $$
    \text{FVA}_{\text{asym}} = \int_0^7 \left[s_F^+ \cdot \mathbb{E}[V_t^+] - s_F^- \cdot \mathbb{E}[V_t^-]\right] D(0,t) \, dt
    $$

    $$
    = \left[0.0080 \times 15 - 0.0040 \times 10\right] \int_0^7 e^{-0.03t} \, dt
    $$

    $$
    = (0.12 - 0.04) \times 6.313 = 0.08 \times 6.313 = \$0.505\text{M}
    $$

    The asymmetric FVA (\$0.505M) is roughly double the symmetric FVA (\$0.253M) because the asymmetric version applies the higher borrowing spread to the larger positive exposure, while the symmetric version nets the exposures first.

---

**Exercise 2.** A derivative portfolio requires average regulatory capital of \$8M over 10 years. The bank's hurdle rate (cost of capital) is 12%. Compute the KVA using the simplified formula

$$
\text{KVA} \approx h \int_0^T K(t) \cdot D(0,t) \, dt
$$

with a flat discount rate of 3%. If the bank's survival probability is $S_B(t) = e^{-0.01t}$, how does incorporating the survival probability change the KVA?

??? success "Solution to Exercise 2"
    **KVA without survival probability.**

    With $h = 12\%$, $K(t) = \$8$M (constant), and $r = 3\%$:

    $$
    \text{KVA} = h \int_0^{10} K(t) \cdot D(0,t) \, dt = 0.12 \times 8 \int_0^{10} e^{-0.03t} \, dt
    $$

    $$
    \int_0^{10} e^{-0.03t} \, dt = \frac{1 - e^{-0.30}}{0.03} = \frac{1 - 0.7408}{0.03} = \frac{0.2592}{0.03} = 8.640
    $$

    $$
    \text{KVA} = 0.12 \times 8 \times 8.640 = 0.96 \times 8.640 = \$8.294\text{M}
    $$

    **KVA with survival probability.**

    Incorporating $S_B(t) = e^{-0.01t}$:

    $$
    \text{KVA}' = h \int_0^{10} K(t) \cdot S_B(t) \cdot D(0,t) \, dt = 0.12 \times 8 \int_0^{10} e^{-0.01t} \cdot e^{-0.03t} \, dt
    $$

    $$
    = 0.96 \int_0^{10} e^{-0.04t} \, dt = 0.96 \times \frac{1 - e^{-0.40}}{0.04} = 0.96 \times \frac{1 - 0.6703}{0.04} = 0.96 \times 8.242 = \$7.912\text{M}
    $$

    **Effect of survival probability:**

    The KVA decreases from \$8.294M to \$7.912M, a reduction of about \$0.382M (4.6%). This reduction reflects the fact that the bank only needs to hold capital while it is alive -- if it defaults, no further capital is required. The survival probability effectively discounts future capital costs by the probability that they will actually be incurred.

---

**Exercise 3.** Explain why XVAs are not additive across trades: $\text{XVA}(A + B) \neq \text{XVA}(A) + \text{XVA}(B)$. Provide a concrete example involving netting: two swaps with the same counterparty where Swap A has positive value and Swap B has negative value. Show that the CVA of the netted portfolio is less than the sum of individual CVAs. What implications does this non-additivity have for trade pricing and the allocation of XVA charges to individual business units?

??? success "Solution to Exercise 3"
    **Why XVAs are not additive.**

    XVAs depend on portfolio-level quantities such as *netted exposure*, *netted capital requirements*, and *netted funding needs*, which are nonlinear functions of individual trade values.

    **Concrete netting example.**

    Consider two swaps with the same counterparty:

    - Swap A: $V_A = +\$10$M (bank receives from counterparty)
    - Swap B: $V_B = -\$8$M (bank owes counterparty)

    **Standalone CVAs** (using simplified formula with flat hazard rate $\lambda$, LGD, and duration $T$):

    $$
    \text{CVA}(A) = \text{LGD} \cdot \mathbb{E}[V_A^+] \cdot \lambda T \cdot \bar{D} = \text{LGD} \cdot 10 \cdot \lambda T \cdot \bar{D}
    $$

    $$
    \text{CVA}(B) = \text{LGD} \cdot \mathbb{E}[V_B^+] \cdot \lambda T \cdot \bar{D} = \text{LGD} \cdot 0 \cdot \lambda T \cdot \bar{D} = 0
    $$

    (Swap B has no positive exposure, so standalone CVA is zero.)

    $$
    \text{CVA}(A) + \text{CVA}(B) = \text{LGD} \cdot 10 \cdot \lambda T \cdot \bar{D}
    $$

    **Netted portfolio CVA:**

    Under a netting agreement, the exposure is:

    $$
    (V_A + V_B)^+ = (10 - 8)^+ = 2^+ = \$2\text{M}
    $$

    $$
    \text{CVA}(\text{Netted}) = \text{LGD} \cdot 2 \cdot \lambda T \cdot \bar{D}
    $$

    **Verification:**

    $$
    \text{CVA}(\text{Netted}) = \text{LGD} \cdot 2 \cdot \lambda T \cdot \bar{D} < \text{LGD} \cdot 10 \cdot \lambda T \cdot \bar{D} = \text{CVA}(A) + \text{CVA}(B)
    $$

    The netting benefit is $\text{LGD} \cdot 8 \cdot \lambda T \cdot \bar{D}$, an 80% reduction.

    **Implications for trade pricing and XVA allocation:**

    1. *Incremental pricing:* When pricing a new trade, the relevant quantity is the *incremental* XVA (change in portfolio-level XVA), not the standalone XVA. A trade that offsets existing exposure may have *negative* incremental XVA (it benefits the portfolio).

    2. *Allocation challenge:* Since $\sum_i \text{XVA}_i^{\text{standalone}} \ne \text{XVA}(\text{Portfolio})$, allocating portfolio-level XVA to individual trades requires methods like Euler allocation or Shapley values. Different allocation methods give different results, creating internal disputes between business units.

    3. *Order dependence:* The incremental XVA of a trade depends on the existing portfolio, so the "price" of a trade depends on what is already in the book, breaking the law of one price.

---

**Exercise 4.** Consider the complete XVA calculation for a 10-year uncollateralized swap with \$100M notional. The inputs are: CVA = \$2.5M, DVA = \$1.0M, FVA = \$0.6M, KVA = \$2.0M, MVA = \$0 (uncollateralized, no IM). The clean price is \$5M. Compute the total XVA-adjusted price. If a competitor bank with a lower funding spread quotes the trade at a tighter XVA charge, explain how this creates competitive distortions and why different banks may quote different prices for the same derivative.

??? success "Solution to Exercise 4"
    **Total XVA-adjusted price:**

    $$
    V^{\text{total}} = V^{\text{clean}} - \text{CVA} + \text{DVA} - \text{FVA} - \text{KVA} - \text{MVA}
    $$

    $$
    = 5.0 - 2.5 + 1.0 - 0.6 - 2.0 - 0 = \$0.9\text{M}
    $$

    The clean price of \$5M is reduced to \$0.9M after XVA adjustments, an 82% reduction due to the costs of credit risk, funding, and capital.

    **Competitive distortions.**

    A competitor bank with a lower funding spread (e.g., 40 bps vs. 100 bps) would compute:

    - Lower FVA: perhaps \$0.3M instead of \$0.6M
    - Lower KVA: better credit may mean lower capital requirements, say \$1.5M instead of \$2.0M

    Their total XVA might be: $2.5 - 1.0 + 0.3 + 1.5 = \$3.3\text{M}$ vs. our bank's $2.5 - 1.0 + 0.6 + 2.0 = \$4.1\text{M}$.

    **Why different banks quote different prices:**

    1. *Funding spread differs:* Banks with higher credit quality borrow at lower rates, giving them a structural FVA advantage.
    2. *Capital efficiency varies:* Banks with better internal models or more diversified portfolios face lower capital charges.
    3. *Netting sets differ:* A bank with offsetting trades already in its portfolio computes lower incremental CVA.
    4. *DVA depends on own credit:* A riskier bank has higher DVA, which reduces its XVA charge -- paradoxically, the riskier bank can quote a more competitive price.

    This violates the classical law of one price and is one of the most significant consequences of XVA-inclusive pricing: derivative prices become *entity-specific* rather than universal.

---

**Exercise 5.** Post-crisis regulations require bilateral initial margin for uncleared derivatives. A 10-year swap requires IM averaging \$12M over its life, funded at a spread of 90 bps. Compute the MVA. If the same trade is novated to a CCP with IM of \$8M but at a lower funding spread of 60 bps (because CCP margin is more efficiently funded), compute the CCP MVA. Which clearing arrangement has lower total margin-related costs?

??? success "Solution to Exercise 5"
    **Bilateral (uncleared) MVA.**

    With IM averaging \$12M, funding spread $s_F = 90$ bps $= 0.009$, and $r = 3\%$ (assuming constant IM for simplicity):

    $$
    \text{MVA}_{\text{bilateral}} = s_F \int_0^{10} \mathbb{E}[\text{IM}(t)] \cdot D(0,t) \, dt = 0.009 \times 12 \int_0^{10} e^{-0.03t} \, dt
    $$

    $$
    = 0.108 \times 8.640 = \$0.933\text{M}
    $$

    **CCP (cleared) MVA.**

    With IM $= \$8$M and $s_F = 60$ bps $= 0.006$:

    $$
    \text{MVA}_{\text{CCP}} = 0.006 \times 8 \int_0^{10} e^{-0.03t} \, dt = 0.048 \times 8.640 = \$0.415\text{M}
    $$

    **Comparison:**

    | | Bilateral | CCP |
    |---|---|---|
    | IM (\$M) | 12 | 8 |
    | Funding spread (bps) | 90 | 60 |
    | MVA (\$M) | 0.933 | 0.415 |

    The CCP arrangement has lower total margin-related costs (\$0.415M vs. \$0.933M), a reduction of **55%**. This is driven by two factors:

    1. Lower IM requirement at the CCP (due to multilateral netting and standardized risk management), reducing the IM from \$12M to \$8M.
    2. Lower effective funding spread for CCP margin, reflecting that CCP margin is more efficiently funded (high-quality liquid assets can often be posted, and the CCP context provides better financing terms).

    This MVA advantage is one of the economic drivers of central clearing mandates, as it incentivizes market participants to move to centrally cleared platforms.

---

**Exercise 6.** In the BSDE framework for XVA pricing, the driver function is

$$
g(t, V, Z) = -r V + s_F V^+ - s_L V^- + \lambda_C(V^+ - C)
$$

where $r$ is the risk-free rate, $s_F$ is the funding spread, $s_L$ is the lending rate, $\lambda_C$ is the counterparty hazard rate, and $C$ is collateral. Explain each term economically. Why does the BSDE framework naturally avoid the double-counting problem between DVA and FVA? What makes the equation nonlinear, and what are the computational implications?

??? success "Solution to Exercise 6"
    **Economic interpretation of each term in the BSDE driver:**

    $$
    g(t, V, Z) = -r V + s_F V^+ - s_L V^- + \lambda_C(V^+ - C)
    $$

    1. **$-rV$: Risk-free discounting.** This is the standard cost of carrying the position at the risk-free rate. If the bank held a riskless asset worth $V$, it would earn $rV$ per unit time. This term appears with a minus sign because it represents the opportunity cost.

    2. **$s_F V^+$: Funding cost.** When $V > 0$ (the derivative is an asset), the bank must fund this position. It borrows at rate $r + s_F$, so the excess cost above risk-free is $s_F V^+$ per unit time. This is the FVA contribution.

    3. **$-s_L V^-$: Funding benefit (lending rate).** When $V < 0$ (the derivative is a liability), the bank has received cash that it can invest. It earns rate $r + s_L$ on this cash, so the benefit above risk-free is $s_L V^-$. The minus sign reflects that this is a benefit (reduces cost).

    4. **$\lambda_C(V^+ - C)$: CVA (uncollateralized exposure).** If the counterparty defaults (with intensity $\lambda_C$), the bank loses the uncollateralized positive exposure $V^+ - C$ (exposure minus collateral). The term $\lambda_C(V^+ - C)$ is the expected instantaneous loss rate from counterparty default. Note that with full collateralization ($C = V^+$), this term vanishes.

    **Why the BSDE framework avoids double-counting between DVA and FVA.**

    In the additive approach, DVA and FVA are computed separately, and both involve the bank's own credit/funding. DVA captures the benefit from the bank's default on negative exposure, while FVA captures the funding benefit on negative positions. These overlap because both reflect the bank's creditworthiness.

    The BSDE framework avoids this by deriving the full pricing equation from first principles (no-arbitrage replication with realistic funding). The terms $s_F V^+$, $-s_L V^-$, and any DVA component emerge simultaneously from a single consistent derivation. The funding spread $s_F$ already incorporates the bank's credit risk (it borrows at $r + s_F$ precisely because of its default risk), so there is no separate DVA term -- the DVA effect is implicitly embedded in the funding terms. This is why the driver shown has no explicit $\lambda_B \cdot V^-$ DVA term; the DVA-like effect is captured through the lending rate $s_L$.

    **What makes the equation nonlinear.**

    The terms $V^+ = \max(V, 0)$, $V^- = \max(-V, 0)$, and $(V^+ - C)$ are nonlinear functions of $V$. Specifically, the positive-part function $V^+$ has a kink at $V = 0$:

    $$
    g(t, V, Z) = \begin{cases} -rV + s_F V + \lambda_C(V - C), & V > 0 \\ -rV + s_L V, & V < 0 \end{cases}
    $$

    This piecewise structure means the equation cannot be written in the form $g = a(t) V + b(t)$ (which would be linear). The discount rate effectively switches between two regimes depending on the sign of $V$.

    **Computational implications:**

    - Standard linear PDE/BSDE solvers cannot be applied directly.
    - Picard iteration or policy iteration is needed: solve a sequence of linear problems, updating the regime classification at each step.
    - Convergence may be slow near the free boundary $V = 0$.
    - In high dimensions, Monte Carlo with regression or deep learning methods are required.

---

**Exercise 7.** An XVA desk charges a total of \$4M in XVA at trade inception on a new swap. Over the next year, the counterparty's credit spread widens by 50 bps and the bank's funding spread widens by 20 bps. Qualitatively describe the direction of change for each XVA component (CVA, DVA, FVA, KVA). If the XVA desk hedged the credit spread component with CDS but did not hedge the funding component, estimate the P&L impact on the desk. Discuss the organizational challenges of managing a centralized XVA desk.

??? success "Solution to Exercise 7"
    **Direction of change for each XVA component:**

    | Component | Direction | Reason |
    |-----------|-----------|--------|
    | CVA | Increases | Counterparty spread widens $\Rightarrow$ higher default probability $\Rightarrow$ higher expected loss |
    | DVA | Increases | Bank's funding spread widens, implying worsening bank credit $\Rightarrow$ higher DVA (benefit from own default) |
    | FVA | Increases | Funding spread widens $\Rightarrow$ higher cost of funding uncollateralized positions |
    | KVA | Increases | Higher counterparty spread $\Rightarrow$ higher CCR capital $\Rightarrow$ higher CVA capital; wider bank spread may also increase cost of capital |

    **P&L impact on the XVA desk.**

    *Credit component (hedged with CDS):*

    The counterparty spread widened by 50 bps. If the CDS hedge is properly sized, the mark-to-market gain on the CDS position approximately offsets the CVA increase. The P&L impact from credit should be approximately zero (assuming good hedge calibration).

    However, the CDS hedge may not perfectly offset because:

    - The CDS notional is based on expected exposure, which has changed with market moves
    - Basis risk between CDS spread and counterparty's actual default probability

    *Funding component (unhedged):*

    The bank's funding spread widened by 20 bps. This increases FVA. With an average net funding exposure of, say, \$50M over 10 years:

    $$
    \Delta \text{FVA} \approx \Delta s_F \times \text{Net Exposure} \times \text{Duration} \approx 0.002 \times 50 \times 7 \approx \$0.7\text{M}
    $$

    Since this was unhedged, the XVA desk incurs a loss of approximately **\$0.7M** from the funding spread widening.

    Additionally, DVA increases (a gain under accounting), but since the XVA desk typically cannot hedge DVA, this creates P&L volatility that is difficult to manage.

    **Organizational challenges of a centralized XVA desk:**

    1. *P&L attribution:* XVA P&L comes from multiple sources (credit, funding, capital), and attributing gains/losses to specific factors is complex and can be contentious.

    2. *Conflict with trading desks:* Trading desks view XVA charges as a "tax" that reduces their profitability. Disputes arise over the magnitude of charges and whether incremental or standalone XVA should be used.

    3. *Hedging authority:* The XVA desk must decide which risks to hedge (credit spread risk, funding risk) and which to leave open. This requires sophisticated risk management and clear mandates.

    4. *Model risk:* The XVA desk is exposed to significant model risk in exposure simulation, credit curves, and funding models. Model changes can cause large P&L swings.

    5. *DVA management:* Accounting requires DVA recognition, but the XVA desk cannot hedge DVA effectively, creating unavoidable P&L volatility.

    6. *Internal transfer pricing:* Setting fair XVA charges for business units requires balancing accuracy (incremental pricing is theoretically correct but complex) against simplicity (standalone pricing is easier to explain but overcharges).
