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
