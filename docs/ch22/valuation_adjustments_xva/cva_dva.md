# CVA and DVA

**Credit Valuation Adjustment (CVA)** and **Debit Valuation Adjustment (DVA)** account for counterparty and own default risk in derivative pricing. They represent the market price of counterparty credit risk.

---

## Credit Valuation Adjustment (CVA)

### Definition

CVA is the expected loss due to counterparty default:

$$
\text{CVA} = \mathbb{E}^{\mathbb{Q}}\left[\text{LGD} \cdot D(\tau) \cdot E_\tau \cdot \mathbf{1}_{\tau \le T}\right]
$$

where:
- $\tau$ = counterparty default time
- $\text{LGD}$ = Loss Given Default (typically 60%)
- $D(\tau)$ = discount factor to default time
- $E_\tau = V_\tau^+$ = exposure at default
- $T$ = portfolio maturity

**Interpretation:** CVA is the risk-neutral expected present value of losses from counterparty default.

---

### CVA Formula (Independence Assumption)

Assuming independence between exposure and default:

$$
\text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot dPD(t) \cdot D(0, t)
$$

where:
- $\text{EE}(t) = \mathbb{E}^{\mathbb{Q}}[V_t^+]$ = Expected Exposure
- $PD(t) = \mathbb{Q}(\tau \le t)$ = cumulative default probability
- $D(0,t)$ = discount factor

**Discrete approximation:**
$$
\text{CVA} \approx \text{LGD} \sum_{i=1}^{n} \text{EE}(t_i) \cdot [PD(t_i) - PD(t_{i-1})] \cdot D(0, t_i)
$$

---

### CVA with Hazard Rate

If the default intensity (hazard rate) is $\lambda(t)$:

$$
PD(t) = 1 - e^{-\int_0^t \lambda(s) \, ds}
$$

$$
dPD(t) = \lambda(t) \cdot e^{-\int_0^t \lambda(s) \, ds} \, dt = \lambda(t) \cdot S(t) \, dt
$$

where $S(t) = 1 - PD(t)$ is the survival probability.

**CVA formula:**
$$
\text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot \lambda(t) \cdot S(t) \cdot D(0,t) \, dt
$$

---

### Unilateral vs Bilateral CVA

**Unilateral CVA:** Only considers counterparty default risk

$$
\text{CVA}^{\text{unilateral}} = \text{LGD}_C \int_0^T \mathbb{E}[V_t^+] \cdot dPD_C(t) \cdot D(0,t)
$$

**Bilateral CVA:** Considers both counterparty AND own default

$$
\text{CVA}^{\text{bilateral}} = \text{CVA}^{\text{unilateral}} \text{ (counterparty defaults first)}
$$

The bilateral framework requires joint modeling of both default times.

---

## Debit Valuation Adjustment (DVA)

### Definition

DVA reflects the benefit from the bank's own default risk:

$$
\text{DVA} = \mathbb{E}^{\mathbb{Q}}\left[\text{LGD}_B \cdot D(\tau_B) \cdot E_{\tau_B}^- \cdot \mathbf{1}_{\tau_B \le T}\right]
$$

where:
- $\tau_B$ = bank's own default time
- $\text{LGD}_B$ = bank's Loss Given Default
- $E_t^- = V_t^- = \max(-V_t, 0)$ = negative exposure (what bank owes)

**Interpretation:** DVA is the expected gain to the bank from not having to pay in full upon its own default.

---

### DVA Formula

$$
\text{DVA} = \text{LGD}_B \int_0^T \text{NEE}(t) \cdot dPD_B(t) \cdot D(0,t)
$$

where $\text{NEE}(t) = \mathbb{E}[V_t^-]$ is the Negative Expected Exposure.

---

### DVA Controversy

DVA is economically controversial:

**Arguments for DVA:**
- Symmetric treatment of default risk
- Required by accounting standards (IFRS 13, ASC 820)
- Reflects true market price of derivatives

**Arguments against DVA:**
- Counterintuitive: profit increases as credit worsens
- Cannot be hedged (can't sell protection on yourself)
- "Gains" cannot be monetized
- Creates P&L volatility from own credit spread moves

**Regulatory treatment:** Basel III excludes DVA from regulatory capital calculations.

---

## Net Valuation with CVA and DVA

### Adjusted Derivative Value

$$
V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA}
$$

where $V^{\text{risk-free}}$ is the classical risk-neutral value ignoring default.

**Alternative formulation:**

$$
V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA} = V^{\text{risk-free}} - \text{BCVA}
$$

where $\text{BCVA} = \text{CVA} - \text{DVA}$ is the **Bilateral CVA**.

---

### First-to-Default Framework

In the bilateral setting, only the first default matters:

$$
V^{\text{bilateral}} = \mathbb{E}\left[D(\tau_1) \cdot V_{\tau_1}^* \cdot \mathbf{1}_{\tau_1 \le T}\right] + \mathbb{E}\left[D(T) \cdot V_T \cdot \mathbf{1}_{\tau_1 > T}\right]
$$

where $\tau_1 = \min(\tau_C, \tau_B)$ is the first-to-default time and $V^*$ is the close-out value.

---

## CVA Calculation Methods

### 1. Semi-Analytical (Simple Portfolios)

For portfolios with analytical exposure profiles:

$$
\text{CVA} = \text{LGD} \sum_{i=1}^n \text{EE}(t_i) \cdot \Delta PD_i \cdot D(0, t_i)
$$

with $\text{EE}(t)$ computed analytically (e.g., for single swap).

### 2. Monte Carlo Simulation

**Algorithm:**
1. Simulate $M$ paths of market factors
2. For each path and time point, compute portfolio value $V_t^{(m)}$
3. Compute exposure $E_t^{(m)} = V_t^{(m)+}$
4. Average: $\text{EE}(t) = \frac{1}{M} \sum_{m=1}^M E_t^{(m)}$
5. Apply CVA formula

### 3. American Monte Carlo (Longstaff-Schwartz)

For path-dependent exposures or early exercise features, use regression-based methods.

---

## CVA Sensitivities (CVA Greeks)

### Credit Spread Sensitivity

$$
\frac{\partial \text{CVA}}{\partial s} = -\text{LGD} \int_0^T \text{EE}(t) \cdot t \cdot e^{-st} \cdot D(0,t) \, dt
$$

where $s$ is the credit spread (constant hazard rate approximation).

### Market Factor Sensitivities

$$
\frac{\partial \text{CVA}}{\partial S} = \text{LGD} \int_0^T \frac{\partial \text{EE}(t)}{\partial S} \cdot dPD(t) \cdot D(0,t)
$$

These are **contingent credit sensitivities**—market Greeks conditional on default.

---

## CVA Hedging

### Credit Hedge

Buy CDS protection on counterparty:
- Notional based on expected exposure
- Roll protection as exposure profile evolves
- Imperfect hedge due to exposure uncertainty

### Market Hedge

Hedge market sensitivities of CVA:
- Delta hedge the underlying exposure
- Vega hedge if volatility affects exposure
- Creates a "CVA desk" function

### Challenges

- CVA is path-dependent (dynamic hedging needed)
- Exposure uncertainty makes hedge sizing difficult
- Credit-market correlation (wrong-way risk)
- Liquidity of CDS market

---

## Accounting and Regulatory Treatment

### Accounting (IFRS 13 / ASC 820)

- CVA and DVA required for fair value measurement
- DVA included despite controversy
- P&L impact from credit spread movements

### Regulatory Capital (Basel III)

- **CVA capital charge:** Additional capital for CVA risk
- **DVA excluded:** Cannot reduce capital requirements
- **SA-CVA and BA-CVA:** Standardized and basic approaches

---

## Example Calculation

**Setup:**
- 5-year interest rate swap, notional \$100M
- Counterparty credit spread: 200 bps
- LGD: 60%
- Risk-free rate: 3%

**Exposure profile (simplified):**

| Year | EE (\$M) |
|------|----------|
| 1 | 2.0 |
| 2 | 3.5 |
| 3 | 4.0 |
| 4 | 3.0 |
| 5 | 1.5 |

**Survival probabilities:** $S(t) = e^{-0.02t}$

**CVA calculation:**
$$
\text{CVA} = 0.60 \times \sum_{i=1}^{5} \text{EE}(t_i) \times [S(t_{i-1}) - S(t_i)] \times D(0, t_i)
$$

$$
\approx 0.60 \times (2.0 \times 0.0198 \times 0.97 + 3.5 \times 0.0194 \times 0.94 + \cdots)
$$

$$
\approx \$0.25\text{M} \text{ (approximately)}
$$

---

## Key Takeaways

- CVA is the expected loss from counterparty default
- DVA is the symmetric adjustment for own default (controversial)
- $V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA}$
- CVA depends on exposure profile, default probability, and LGD
- Monte Carlo simulation is standard for complex portfolios
- CVA hedging requires both credit and market hedges
- Accounting includes DVA; regulatory capital excludes it

---

## Further Reading

- Gregory, J., *Counterparty Credit Risk and Credit Value Adjustment*
- Brigo, D., Morini, M., & Pallavicini, A., *Counterparty Credit Risk, Collateral and Funding*
- Cesari, G. et al., *Modelling, Pricing, and Hedging Counterparty Credit Exposure*
- Pykhtin, M. & Zhu, S. (2007), "A Guide to Modelling Counterparty Credit Risk"
- ISDA, "ISDA Margin Survey" (market practice)
