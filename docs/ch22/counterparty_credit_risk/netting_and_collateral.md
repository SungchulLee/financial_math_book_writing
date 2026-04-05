# Netting and Collateral

**Netting** and **collateral (margin)** are the two primary mechanisms for reducing counterparty credit exposure in derivative portfolios. Netting exploits the offsetting nature of positions within a portfolio, while collateral requires counterparties to post assets against mark-to-market exposure. Together, they transform gross notional exposures of trillions of dollars into manageable net credit risk.

---

## Close-Out Netting

### Concept

Under a **close-out netting agreement** (typically an ISDA Master Agreement), if a counterparty defaults, all trades under the agreement are terminated simultaneously and their values are netted to a single amount.

### Mathematical Framework

For a portfolio of $n$ trades with values $V_1, V_2, \ldots, V_n$ at the time of default:

**Without netting (gross exposure):**

$$
E^{\text{gross}} = \sum_{i=1}^n V_i^+ = \sum_{i=1}^n \max(V_i, 0)
$$

**With netting (net exposure):**

$$
E^{\text{net}} = \left(\sum_{i=1}^n V_i\right)^+ = \max\left(\sum_{i=1}^n V_i, \, 0\right)
$$

### Netting Inequality

!!! info "Proposition (Netting Reduces Exposure)"
    For any portfolio of $n$ trades:

    $$
    E^{\text{net}} \le E^{\text{gross}}
    $$

    with equality if and only if all trades with positive value have the same sign as the portfolio sum.

**Proof.** For any collection of real numbers $v_1, \ldots, v_n$:

$$
\left(\sum_{i=1}^n v_i\right)^+ \le \sum_{i=1}^n v_i^+
$$

This follows because $(\cdot)^+$ is a convex function and $\sum_i v_i \le \sum_i v_i^+$ (since $v_i \le v_i^+$ for all $i$). Applying the non-decreasing property of $(\cdot)^+$:

$$
\left(\sum_i v_i\right)^+ \le \left(\sum_i v_i^+\right)^+ = \sum_i v_i^+
$$

where the last equality uses $v_i^+ \ge 0$. $\square$

### Netting at the Expected Exposure Level

Taking expectations:

$$
\text{EE}^{\text{net}}(t) = \mathbb{E}\left[\left(\sum_{i=1}^n V_{i,t}\right)^+\right] \le \sum_{i=1}^n \mathbb{E}[V_{i,t}^+] = \sum_{i=1}^n \text{EE}_i(t)
$$

The netting benefit for EE is generally less than for instantaneous exposure because the expectation operator smooths out offsetting effects.

---

## Netting Factor

The **netting factor** quantifies the exposure reduction from netting:

$$
\text{NF} = \frac{\text{EE}^{\text{net}}}{\sum_i \text{EE}_i} = \frac{\text{EE}^{\text{net}}}{\text{EE}^{\text{gross}}} \in [0, 1]
$$

### Analytical Approximation

Under simplifying assumptions (equal notionals, pairwise correlation $\bar{\rho}$ between trade values), a useful approximation is:

$$
\text{NF} \approx \frac{\bar{\rho} + (1 - \bar{\rho}) / n}{\bar{\rho} + (1 - \bar{\rho})}
$$

which for large $n$ converges to:

$$
\text{NF} \xrightarrow{n \to \infty} \bar{\rho}
$$

**Interpretation:** When trades are highly correlated ($\bar{\rho} \to 1$), netting provides little benefit (all trades move together). When trades are uncorrelated ($\bar{\rho} \to 0$), the netting factor decreases as $1/n$.

### Drivers of Netting Benefit

Netting is most valuable when the portfolio contains:

- **Opposite-sign positions** (long and short) in the same risk factor
- **Diverse maturities** that spread exposure over time
- **Low correlation** across trade values
- **Multiple asset classes** with different risk drivers

---

## Payment Netting vs Close-Out Netting

| Feature | Payment Netting | Close-Out Netting |
|---------|----------------|-------------------|
| When applied | Ongoing (each payment date) | At default only |
| What is netted | Cash flows due on same date | Mark-to-market of all trades |
| Risk reduction | Settlement risk | Pre-settlement risk |
| Legal basis | Bilateral agreement | ISDA Master Agreement |

Payment netting reduces **settlement risk** by exchanging only the net cash flow on each payment date. Close-out netting reduces **pre-settlement (credit) risk** by computing a single net obligation upon default.

---

## Collateral (Margin) Agreements

### Credit Support Annex (CSA)

The **ISDA Credit Support Annex** governs collateral exchange between counterparties. Key parameters:

- **Threshold ($H$):** Exposure below which no collateral is required
- **Minimum Transfer Amount (MTA):** Smallest collateral transfer executed
- **Independent Amount (IA):** Initial margin posted regardless of mark-to-market
- **Eligible collateral:** Cash, government bonds, corporate bonds (with haircuts)
- **Rehypothecation rights:** Whether the collateral holder can reuse posted collateral

### Collateral Balance

The **required collateral** at time $t$ under a symmetric two-way CSA is:

$$
C_t = \max(V_t - H, 0) \cdot \mathbf{1}_{\{|V_t - H| \ge \text{MTA}\}}
$$

In practice, the collateral balance adjusts with a lag due to the margin call process.

### Collateralized Exposure

With collateral $C_t$, the exposure is:

$$
E_t^{\text{coll}} = (V_t - C_t)^+
$$

Under a zero-threshold, zero-MTA CSA with continuous margining, $C_t = V_t^+$ and $E_t^{\text{coll}} = 0$. In reality, the collateral lags the exposure due to the **margin period of risk**.

---

## Margin Period of Risk (MPOR)

### Definition

The **Margin Period of Risk** is the time interval between:

1. The last successful margin call, and
2. The close-out of the defaulted counterparty's positions

During the MPOR, the portfolio value can move adversely while collateral remains at its previous level.

### Regulatory Standards

| Setting | MPOR |
|---------|------|
| Bilateral (daily margining) | 10 business days |
| CCP (daily margining) | 5 business days |
| Illiquid portfolios | 20 business days |
| Disputed margin calls | 20 business days |

### Collateralized EE

The expected exposure under collateral with MPOR $\delta$ is:

$$
\text{EE}^{\text{coll}}(t) = \mathbb{E}\left[\left(V_t - C_{t-\delta}\right)^+\right]
$$

where $C_{t-\delta}$ is the collateral balance at the time of the last margin call (lagged by MPOR).

**Key insight:** Even with daily margining and zero thresholds, the MPOR creates a **residual exposure** that depends on the volatility of the portfolio over the MPOR interval. For a portfolio with volatility $\sigma$:

$$
\text{EE}^{\text{coll}}(t) \approx \sigma \sqrt{\delta} \cdot \phi(0) \cdot N_{\text{effective}}
$$

where $\phi(0) = 1/\sqrt{2\pi}$ is the standard normal density at zero and $N_{\text{effective}}$ reflects the effective portfolio notional.

---

## Modeling Collateral in Exposure Simulation

### Algorithm

1. Simulate market factor paths at time steps $t_1, t_2, \ldots$
2. At each $t_i$, compute portfolio value $V_{t_i}$
3. Determine collateral call based on CSA terms:

$$
\text{Call}_{t_i} = \max(V_{t_i} - C_{t_i - 1} - H, 0) \cdot \mathbf{1}_{\{\cdot \ge \text{MTA}\}}
$$

4. Collateral arrives after the MPOR lag:

$$
C_{t_i} = C_{t_{i-1}} + \text{Call}_{t_i - \delta}
$$

5. Compute collateralized exposure: $E_{t_i}^{\text{coll}} = (V_{t_i} - C_{t_i})^+$

### Impact of CSA Parameters on Exposure

| Parameter | Effect on Exposure |
|-----------|--------------------|
| Lower threshold $H$ | Reduces exposure |
| Lower MTA | More frequent margin calls, lower exposure |
| Shorter MPOR | Reduces residual exposure |
| Higher independent amount | Reduces exposure (acts as initial margin) |
| Wider eligible collateral | Easier to post, but haircut risk |

---

## Variation Margin vs Initial Margin

### Variation Margin (VM)

Variation margin covers the **current mark-to-market** exposure:

$$
\text{VM}_t = V_t - V_{t-1}
$$

VM is exchanged daily (or more frequently) and reduces exposure to the MPOR-driven residual.

### Initial Margin (IM)

Initial margin covers **potential future changes** in value during the close-out period:

$$
\text{IM} \approx \text{VaR}_\alpha(\Delta V_{\delta})
$$

where $\Delta V_\delta$ is the change in portfolio value over the MPOR $\delta$, typically at the 99% confidence level.

**Post-crisis regulations** (BCBS-IOSCO Uncleared Margin Rules) require bilateral IM for uncleared derivatives, computed via:

- **ISDA SIMM:** Sensitivity-based, risk-factor-level margin
- **Schedule-based:** Simpler, percentage-of-notional approach

### Combined Effect

With both VM and IM:

$$
E_t^{\text{full}} = \max(V_t - C_t^{\text{VM}} - C_t^{\text{IM}}, 0)
$$

The IM provides a buffer that absorbs adverse moves during the MPOR, substantially reducing residual exposure.

---

## Example: Netting and Collateral Impact

**Setup:** Three interest rate swaps with a single counterparty:

| Trade | Notional | Direction | 5-Year EE (stand-alone) |
|-------|----------|-----------|------------------------|
| IRS 1 | \$50M | Receive fixed | \$2.0M |
| IRS 2 | \$30M | Pay fixed | \$1.2M |
| IRS 3 | \$40M | Receive fixed | \$1.6M |

**Gross EE:** $\$2.0\text{M} + \$1.2\text{M} + \$1.6\text{M} = \$4.8\text{M}$

**Netted EE** (accounting for offsetting): Suppose Monte Carlo simulation yields $\text{EE}^{\text{net}} = \$2.1\text{M}$

**Netting factor:** $\text{NF} = 2.1 / 4.8 = 0.44$

**Collateralized EE** (zero threshold, 10-day MPOR): Suppose $\text{EE}^{\text{coll}} = \$0.8\text{M}$

**Total reduction:** From \$4.8M gross to \$0.8M collateralized, a reduction of 83%.

---

## Multilateral Netting and CCPs

**Central Counterparties (CCPs)** provide multilateral netting by interposing themselves between all counterparties:

$$
E^{\text{CCP}} = \left|\sum_{j} V_j^{\text{CCP}}\right|^+ \le \sum_{j} |V_j|^+
$$

The netting benefit of CCPs can be substantial: if institution $i$ has bilateral netting sets with $K$ counterparties, the total bilateral exposure is:

$$
E^{\text{bilateral}} = \sum_{k=1}^K \left(\sum_{j \in \text{NS}_k} V_j\right)^+
$$

while the CCP exposure is:

$$
E^{\text{CCP}} = \left(\sum_{k=1}^K \sum_{j \in \text{NS}_k} V_j\right)^+
$$

The CCP pools all trades into a single netting set, reducing exposure through broader offsetting.

---

## Key Takeaways

- Close-out netting reduces exposure from gross $\sum_i V_i^+$ to net $(\sum_i V_i)^+$, with the netting factor depending on portfolio composition and correlation
- The ISDA CSA governs collateral exchange via thresholds, MTAs, and eligible collateral
- The margin period of risk creates residual exposure even under daily margining, with MPOR of 10 days (bilateral) or 5 days (CCP)
- Variation margin covers current mark-to-market; initial margin covers potential future exposure over the MPOR
- Combined netting and collateral can reduce gross exposure by 80--90% for well-diversified, collateralized portfolios
- CCPs provide multilateral netting, pooling all trades into a single netting set

---

## Further Reading

- Gregory, J., *Counterparty Credit Risk and Credit Value Adjustment*
- Brigo, D., Morini, M., & Pallavicini, A., *Counterparty Credit Risk, Collateral and Funding*
- Duffie, D. & Zhu, H. (2011), "Does a Central Clearing Counterparty Reduce Counterparty Risk?"
- ISDA, *ISDA Master Agreement* and *Credit Support Annex*
- BCBS-IOSCO (2020), "Margin Requirements for Non-Centrally Cleared Derivatives"
- Pykhtin, M. (2009), "Modeling Credit Exposure for Collateralized Counterparties"

---

## Exercises

**Exercise 1.** A bank has three derivatives with the same counterparty: values of +\$10M, -\$7M, and +\$3M. Compute the gross positive exposure and the net exposure under a bilateral netting agreement. By what percentage does netting reduce exposure?

??? success "Solution to Exercise 1"
    **Gross positive exposure:**

    The gross positive exposure sums the positive mark-to-market values of each trade individually:

    $$
    E^{\text{gross}} = \sum_{i=1}^{3} V_i^+ = (+\$10\text{M})^+ + (-\$7\text{M})^+ + (+\$3\text{M})^+
    $$

    $$
    = \$10\text{M} + \$0 + \$3\text{M} = \$13 \text{ million}
    $$

    **Net exposure under bilateral netting:**

    Under a netting agreement, all trade values are summed before taking the positive part:

    $$
    E^{\text{net}} = \left(\sum_{i=1}^{3} V_i\right)^+ = (+\$10\text{M} - \$7\text{M} + \$3\text{M})^+ = (\$6\text{M})^+ = \$6 \text{ million}
    $$

    **Percentage reduction from netting:**

    $$
    \text{Reduction} = \frac{E^{\text{gross}} - E^{\text{net}}}{E^{\text{gross}}} = \frac{\$13\text{M} - \$6\text{M}}{\$13\text{M}} = \frac{\$7\text{M}}{\$13\text{M}} \approx 53.8\%
    $$

    The netting factor is:

    $$
    \text{NF} = \frac{E^{\text{net}}}{E^{\text{gross}}} = \frac{6}{13} \approx 0.462
    $$

    **Interpretation:** Netting reduces the credit exposure by approximately 54%. The key mechanism is that the negative-value trade ($-\$7$M) offsets part of the positive-value trades. Without netting, the counterparty's estate could "cherry-pick" — claiming the \$7M owed to them while defaulting on the \$13M they owe. With netting, only the net \$6M obligation is at risk.

---

**Exercise 2.** Explain the difference between close-out netting and payment netting. Why is close-out netting critical for reducing counterparty credit exposure in the event of default? What legal documentation governs netting (e.g., ISDA Master Agreement)?

??? success "Solution to Exercise 2"
    **Close-out netting** and **payment netting** serve different purposes and operate at different times:

    **Payment netting** applies during the **normal life** of the trades, on each payment date. When multiple cash flows between the same counterparties fall on the same date, only the net cash flow is exchanged. For example, if the bank owes \$5M on Swap A and is owed \$3M on Swap B on the same date, only a net payment of \$2M (bank pays) is made. Payment netting reduces **settlement risk** — the risk that one party pays but the other does not, during the settlement window.

    **Close-out netting** applies only **upon default**. When a counterparty defaults, all trades under the netting agreement are terminated simultaneously, their values are computed (using a prescribed valuation methodology), and a single net amount is determined. Only this net amount is a claim in the bankruptcy.

    **Why close-out netting is critical for counterparty credit exposure:**

    Without close-out netting, the defaulting counterparty's estate can engage in **cherry-picking**: enforcing trades that are profitable to the defaulter (where the surviving party owes money) while repudiating trades that are unprofitable (where the surviving party is owed money). In bankruptcy:

    - The surviving party must pay in full on negative-value trades (obligations to the estate)
    - The surviving party recovers only a fraction (recovery rate) on positive-value trades (claims against the estate)

    This asymmetry means the loss is based on gross positive exposure. With close-out netting, all trades collapse to a single net number, and the loss is based on the (much smaller) net exposure.

    Mathematically:

    $$
    \text{Loss}_{\text{no netting}} = \sum_i V_i^+ - R \cdot \sum_i V_i^+ = (1-R)\sum_i V_i^+
    $$

    $$
    \text{Loss}_{\text{netting}} = (1-R)\left(\sum_i V_i\right)^+ \le (1-R)\sum_i V_i^+
    $$

    **Legal documentation:** Close-out netting is governed by the **ISDA Master Agreement**, the standard bilateral framework for OTC derivatives. The Master Agreement specifies:

    - Events of Default and Termination Events that trigger close-out
    - The close-out valuation methodology (market quotation or loss)
    - The netting of termination values to a single settlement amount
    - The legal enforceability of netting across jurisdictions (supported by ISDA netting opinions)

    The ISDA Master Agreement must be in place **before** trades are executed for netting to be legally enforceable. Jurisdictional analysis (ISDA netting opinions) confirms enforceability in each relevant legal system.

---

**Exercise 3.** A Credit Support Annex (CSA) specifies: threshold = \$5M, minimum transfer amount = \$500K, independent amount = \$2M. If the bank's net exposure to a counterparty is \$8M, compute the collateral call. What exposure remains after collateral is posted?

??? success "Solution to Exercise 3"
    **CSA parameters:**

    - Threshold $H = \$5$M
    - Minimum Transfer Amount (MTA) $= \$500$K
    - Independent Amount (IA) $= \$2$M
    - Net exposure (mark-to-market) $= \$8$M

    **Step 1: Determine the collateral requirement.**

    The collateral call is based on the exposure exceeding the threshold, adjusted for the independent amount. The required collateral is:

    $$
    C_{\text{required}} = \max(V - H + \text{IA}, 0) = \max(\$8\text{M} - \$5\text{M} + \$2\text{M}, 0) = \max(\$5\text{M}, 0) = \$5\text{M}
    $$

    Note: The independent amount effectively lowers the threshold. The bank requires collateral when exposure exceeds $H - \text{IA} = \$5\text{M} - \$2\text{M} = \$3\text{M}$.

    **Step 2: Apply the Minimum Transfer Amount.**

    The collateral call is only executed if it exceeds the MTA. Since the required collateral of \$5M far exceeds the MTA of \$500K, the full \$5M collateral call is made.

    If no prior collateral had been posted, the **collateral call** is \$5M.

    **Step 3: Compute remaining exposure after collateral.**

    $$
    E^{\text{coll}} = (V - C)^+ = (\$8\text{M} - \$5\text{M})^+ = \$3\text{M}
    $$

    **Breakdown of the remaining \$3M exposure:**

    - \$5M is covered by the threshold: The CSA allows up to \$5M of uncollateralized exposure. After subtracting the IA of \$2M, the effective uncollateralized threshold is \$3M.
    - The \$2M independent amount is already included in the \$5M collateral call, providing additional protection.

    Alternatively, without the independent amount, the collateral would be $\max(\$8\text{M} - \$5\text{M}, 0) = \$3\text{M}$, and the remaining exposure would be $\$8\text{M} - \$3\text{M} = \$5\text{M}$ (equal to the threshold). The IA reduces this by \$2M.

---

**Exercise 4.** The Margin Period of Risk (MPR) is the time between the last collateral exchange and the closeout of positions after default. Explain why even fully collateralized portfolios have residual exposure. If the MPR is 10 business days and the portfolio's daily volatility of mark-to-market changes is \$2M, estimate the residual exposure at the 99% confidence level.

??? success "Solution to Exercise 4"
    **Why fully collateralized portfolios have residual exposure:**

    Even with daily variation margin and a zero threshold, collateral is not instantaneous. The **Margin Period of Risk (MPOR)** represents the time gap between:

    1. **Last successful margin call:** The most recent date when collateral was exchanged and reflects an accurate mark-to-market
    2. **Closeout of the defaulted position:** When the surviving party has fully hedged or liquidated the portfolio after the counterparty's default

    During this window of $\delta$ days, the portfolio value changes but the collateral remains at its previous level. The sequence of events in the MPOR:

    - Day 0: Last successful margin exchange
    - Day 1--2: Counterparty misses margin call; bank identifies potential default
    - Day 3--5: Dispute resolution, legal notification, confirm default
    - Day 5--10: Portfolio valuation, hedge/liquidate positions, complete closeout

    The **residual exposure** is the adverse portfolio value change during this window:

    $$
    E_{\text{residual}} = (V_t - C_{t-\delta})^+ = (V_t - V_{t-\delta})^+ = (\Delta V_\delta)^+
    $$

    **Estimation at the 99% confidence level:**

    Given:

    - MPOR $= 10$ business days
    - Daily volatility of mark-to-market changes $= \$2$M

    Assuming daily P&L changes are independent and normally distributed, the volatility over the MPOR is:

    $$
    \sigma_{\delta} = \sigma_{\text{daily}} \cdot \sqrt{\delta} = \$2\text{M} \times \sqrt{10} = \$2\text{M} \times 3.162 = \$6.32\text{M}
    $$

    The 99% PFE of the residual exposure (positive part of a normal variable with mean zero and standard deviation $\sigma_\delta$) is:

    $$
    \text{PFE}_{99\%} \approx \sigma_\delta \cdot \Phi^{-1}(0.99) = \$6.32\text{M} \times 2.326 = \$14.7\text{M}
    $$

    More precisely, the expected positive exposure of a half-normal distribution would be $\sigma_\delta \cdot \phi(0) = \$6.32\text{M} \times 0.399 = \$2.52\text{M}$, but for the 99% quantile, we use the full quantile:

    $$
    \text{Residual Exposure}_{99\%} \approx \$14.7 \text{ million}
    $$

    **Interpretation:** Despite daily collateral exchange, the bank faces a potential exposure of approximately \$14.7M at the 99% confidence level due to the 10-day MPOR. This is why regulators mandate minimum MPORs and why reducing the MPOR (e.g., to 5 days for CCP-cleared trades) significantly reduces residual exposure: $\sqrt{5}/\sqrt{10} \approx 0.707$, a 29% reduction.

---

**Exercise 5.** Bilateral margin requirements for non-centrally cleared derivatives require both initial margin (IM) and variation margin (VM). Explain the economic purpose of each. Why does initial margin provide protection beyond variation margin?

??? success "Solution to Exercise 5"
    **Variation Margin (VM):**

    VM covers the **current mark-to-market exposure**. It is exchanged (typically daily) to reflect changes in portfolio value:

    $$
    \text{VM}_t = V_t - V_{t-1}
    $$

    **Economic purpose:** VM ensures that the collateral balance tracks the portfolio value over time. If the portfolio value increases by \$5M today (increasing the bank's exposure), the counterparty must post \$5M in collateral. This prevents exposure from accumulating over the life of the trade.

    Without VM, exposure would grow with market factor diffusion (e.g., $\sigma\sqrt{T}$ for an FX forward), potentially reaching very large levels for long-dated trades. With daily VM, exposure is reset each day, limiting it to the one-day change in portfolio value.

    **Initial Margin (IM):**

    IM covers the **potential future change** in portfolio value during the closeout period (MPOR):

    $$
    \text{IM} \approx \text{VaR}_\alpha(\Delta V_\delta) \quad \text{or} \quad \text{IM} \approx \text{ES}_\alpha(\Delta V_\delta)
    $$

    where $\Delta V_\delta$ is the change in portfolio value over the MPOR $\delta$.

    **Economic purpose:** IM provides a buffer against adverse value changes during the period when the counterparty has defaulted but the portfolio has not yet been closed out. Even with daily VM, the MPOR creates residual exposure because collateral cannot be adjusted during this window.

    **Why IM provides protection beyond VM:**

    VM alone reduces exposure to the MPOR residual:

    $$
    E_t^{\text{VM only}} = (V_t - C_{t-\delta}^{\text{VM}})^+ \approx (\Delta V_\delta)^+
    $$

    This residual can still be substantial (as shown in Exercise 4, approximately \$14.7M at 99% for a 10-day MPOR). IM pre-positions collateral to absorb this residual:

    $$
    E_t^{\text{VM+IM}} = (V_t - C_{t-\delta}^{\text{VM}} - \text{IM})^+ = (\Delta V_\delta - \text{IM})^+
    $$

    If IM is calibrated at the 99% confidence level, then $\text{IM} \approx \text{VaR}_{99\%}(\Delta V_\delta)$, and the probability that the residual exposure exceeds zero is only 1%. The remaining exposure after both VM and IM is:

    $$
    E^{\text{residual}} = (\Delta V_\delta - \text{IM})^+
    $$

    which is nonzero only in extreme tail events beyond the IM confidence level.

    **Regulatory framework (BCBS-IOSCO):**

    Post-2008 regulations require bilateral IM for uncleared OTC derivatives. IM is computed via:

    - **ISDA SIMM (Standard Initial Margin Model):** A sensitivity-based approach that computes IM from delta, vega, and curvature risk across asset classes, using prescribed risk weights and correlations
    - **Schedule-based approach:** A simpler percentage-of-notional method as a fallback

    Both parties post IM to segregated accounts (no rehypothecation), ensuring the collateral is available even if the collecting party also defaults.

---

**Exercise 6.** Compare the exposure reduction benefits of netting versus collateral for a portfolio of 100 interest rate swaps. Under what portfolio composition (e.g., highly correlated vs diversified trades) does netting provide the greatest benefit? When is collateral more effective?

??? success "Solution to Exercise 6"
    **Netting benefit for a portfolio of 100 IRS:**

    The netting factor depends on portfolio composition and correlation structure:

    $$
    \text{NF} \approx \frac{\bar{\rho} + (1-\bar{\rho})/n}{\bar{\rho} + (1-\bar{\rho})} = \bar{\rho} + \frac{1-\bar{\rho}}{n}
    $$

    For $n = 100$ trades:

    | Avg. correlation $\bar{\rho}$ | Netting Factor | Exposure Reduction |
    |------|------|------|
    | 0.0 (uncorrelated) | $0 + 1/100 = 0.01$ | 99% |
    | 0.2 (low) | $0.2 + 0.8/100 = 0.208$ | 79% |
    | 0.5 (moderate) | $0.5 + 0.5/100 = 0.505$ | 50% |
    | 0.8 (high) | $0.8 + 0.2/100 = 0.802$ | 20% |
    | 1.0 (perfect) | $1.0$ | 0% |

    **Collateral benefit:**

    Collateral reduces exposure independently of portfolio composition by covering the mark-to-market value. Under a zero-threshold CSA with daily margining (MPOR $= \delta$):

    $$
    \text{Collateral Reduction} \approx 1 - \frac{\sigma\sqrt{\delta}}{\text{Peak EE}^{\text{net}}}
    $$

    For typical portfolios, collateral reduces the (already netted) exposure by 70--90%, leaving only the MPOR residual.

    **When netting provides the greatest benefit:**

    Netting is most effective for **diversified portfolios** with:

    - **Low average correlation** ($\bar{\rho}$ close to 0): Trades move independently, so positive and negative values tend to offset
    - **Mix of directions:** Both receive-fixed and pay-fixed swaps (or different asset classes) with roughly balanced notionals
    - **Different maturities:** Staggered maturities reduce the chance that all trades are in-the-money simultaneously
    - **Multiple currencies/asset classes:** Cross-asset diversification provides additional offsetting

    For example, a portfolio of 50 receive-fixed and 50 pay-fixed IRS with various tenors and reference rates would have near-zero average correlation, achieving a netting factor close to 0.01 — a 99% reduction.

    Netting provides **little benefit** when all trades are in the same direction (e.g., all receive-fixed) on the same reference rate with similar tenors. In this case $\bar{\rho} \approx 1$ and $\text{NF} \approx 1$.

    **When collateral is more effective:**

    Collateral is more effective than netting (or provides incremental benefit beyond netting) when:

    - **Highly directional portfolio:** All trades move together ($\bar{\rho}$ close to 1), so netting provides little offset. Collateral directly addresses the remaining exposure regardless of directionality.
    - **Large absolute exposure but low netting opportunity:** A portfolio of long-dated receive-fixed swaps all in the same currency. Netting factor $\approx 1$, but collateral with daily margining reduces exposure to the MPOR residual.
    - **After netting is exhausted:** For a well-diversified portfolio, netting may already reduce exposure by 80%. Collateral then reduces the remaining 20% by another 70--90%, achieving an overall reduction of 94--98%.

    **Combined effect:**

    The two mechanisms are complementary. The optimal strategy applies both:

    1. First, netting reduces gross exposure to net exposure (effective for diversified portfolios)
    2. Then, collateral reduces net exposure to the MPOR residual (effective regardless of portfolio composition)

    For a portfolio of 100 IRS with moderate diversification ($\text{NF} = 0.3$) and daily collateral (residual $= 15\%$ of netted exposure):

    $$
    E^{\text{final}} = E^{\text{gross}} \times \text{NF} \times \text{Collateral Residual} = E^{\text{gross}} \times 0.3 \times 0.15 = 0.045 \times E^{\text{gross}}
    $$

    A combined reduction of approximately 95.5%.
