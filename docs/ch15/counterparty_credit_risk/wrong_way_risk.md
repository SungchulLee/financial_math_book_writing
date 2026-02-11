# Wrong-Way Risk

In counterparty credit risk, **wrong-way risk (WWR)** occurs when exposure to a counterparty increases as the counterparty's credit quality deteriorates. This adverse correlation amplifies potential losses.

---

## Definition

Wrong-way risk arises when:

$$
\text{Corr}(E_\tau, \mathbf{1}_{\tau \le T}) > 0
$$

where $E_\tau$ is exposure at default time $\tau$.

**In words:** High exposure tends to coincide with default—the worst possible timing.

**Opposite:** **Right-way risk** occurs when exposure decreases as default becomes more likely (beneficial correlation).

---

## Types of Wrong-Way Risk

### Specific Wrong-Way Risk (SWWR)

Arises from the **specific nature of the transaction** with the counterparty.

**Examples:**
- **Equity derivatives on counterparty's stock:** Put options on a bank's own equity—if the bank's stock falls, the bank is more likely to default AND the put is more valuable (higher exposure)
- **Credit protection sold by related entity:** CDS protection on a sovereign sold by a bank heavily exposed to that sovereign
- **Commodity trades with producers:** Derivatives with an oil company that worsen as oil prices fall

**Characteristic:** Direct, identifiable link between trade structure and counterparty credit.

### General Wrong-Way Risk (GWWR)

Arises from **correlation between market factors and credit quality** not specific to the transaction.

**Examples:**
- **FX derivatives with EM counterparty:** Currency depreciation often coincides with sovereign/corporate stress
- **Interest rate derivatives during crisis:** Rate movements correlate with credit spreads
- **Equity derivatives in systemic crisis:** Market-wide equity decline correlates with increased default rates

**Characteristic:** Indirect, systemic correlation through market conditions.

---

## Mathematical Framework

### Standard CCR Model (Independence Assumption)

The standard CVA formula assumes independence:

$$
\text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot dPD(t)
$$

where:
- $\text{EE}(t) = \mathbb{E}[E_t]$ is computed independently of default
- $PD(t) = \mathbb{Q}(\tau \le t)$ is the cumulative default probability

**This understates CVA when WWR is present.**

### WWR-Adjusted CVA

With wrong-way risk:

$$
\text{CVA}^{\text{WWR}} = \text{LGD} \int_0^T \mathbb{E}[E_t | \tau = t] \cdot dPD(t)
$$

The key difference: **conditional expectation** $\mathbb{E}[E_t | \tau = t]$ replaces the unconditional $\text{EE}(t)$.

**Relation:**
$$
\text{CVA}^{\text{WWR}} > \text{CVA} \quad \text{under positive correlation}
$$

---

## Modeling Approaches

### 1. Stressed Exposure Approach

Simple but conservative:

$$
\text{CVA}^{\text{WWR}} = \text{LGD} \int_0^T \text{EE}^{\text{stressed}}(t) \cdot dPD(t)
$$

where $\text{EE}^{\text{stressed}}(t)$ is computed under a stressed scenario consistent with default.

**Advantage:** Simple to implement
**Disadvantage:** May be overly conservative; no probability calibration

### 2. Correlation Approach

Model joint distribution of exposure and default:

$$
(V_t, \tau) \sim F(v, t; \rho)
$$

where $\rho$ captures the correlation structure.

**Implementation:**
- Copula models for dependence
- Stochastic intensity models with correlated factors
- Structural models linking asset value to default

### 3. Intensity-Based Models

Let default intensity $\lambda_t$ depend on market factors $X_t$:

$$
\lambda_t = \lambda_0 \cdot e^{\beta \cdot X_t}
$$

If $X_t$ also drives exposure:
- Positive $\beta$ with positive exposure sensitivity → WWR
- Negative $\beta$ with positive exposure sensitivity → RWR

**Example:** For FX exposure with EM counterparty:
$$
\lambda_t = \lambda_0 \cdot e^{\beta \cdot (S_t - S_0)/S_0}
$$

where $S_t$ is the FX rate (domestic per foreign). Depreciation ($S_t$ increases) raises default intensity.

### 4. Hull-White WWR Model

Assume exposure at default follows:

$$
\mathbb{E}[E_\tau | \tau = t] = \text{EE}(t) \cdot (1 + w)
$$

where $w$ is the WWR multiplier.

**Calibration:** Estimate $w$ from:
- Historical data on exposure-default correlation
- Stress scenarios
- Expert judgment

---

## Regulatory Treatment

### Basel III/IV

Regulators require explicit WWR consideration:

**Specific WWR:**
- Transactions with SWWR must be identified
- May require separate treatment or exclusion from netting
- Conservative exposure assumptions

**General WWR:**
- Correlation between exposure and default must be assessed
- Stress testing required
- Capital add-ons may apply

### Supervisory Formula

Some regulators prescribe:

$$
\text{EAD}^{\text{WWR}} = \text{EAD} \times (1 + \alpha_{\text{WWR}})
$$

where $\alpha_{\text{WWR}}$ is a supervisory add-on (e.g., 40%).

---

## Examples in Detail

### Example 1: Put Option on Counterparty Stock

**Setup:**
- Bank A sells a put option on Bank B's stock to Bank B
- If Bank B's stock falls, put becomes ITM
- Bank B's default probability increases when stock falls

**Analysis:**
$$
E_t = \max(K - S_t^B, 0)
$$

As $S_t^B \downarrow$:
- Exposure $E_t \uparrow$
- Default probability $PD_t \uparrow$

**Strong SWWR:** This combination is particularly dangerous.

### Example 2: FX Forward with EM Corporate

**Setup:**
- Trade: Receive USD, pay BRL forward
- Counterparty: Brazilian corporate
- Risk: BRL depreciation

**Analysis:**
$$
V_t = N \cdot (F_t - K) \cdot D(t,T)
$$

If BRL depreciates (USD/BRL increases):
- Forward value increases (exposure rises)
- Brazilian corporate likely under stress (credit deteriorates)

**GWWR through FX-credit correlation.**

### Example 3: CDS Protection from Correlated Entity

**Setup:**
- Buy CDS protection on Reference Entity A from Counterparty B
- A and B are in the same sector/region

**Analysis:**
- If A defaults, CDS has high value (exposure to B is high)
- B's credit likely impaired if A defaults (sector stress)

**SWWR due to sectoral/regional correlation.**

---

## Quantifying WWR Impact

### CVA Multiplier

Define the WWR multiplier:

$$
\text{WWR Multiplier} = \frac{\text{CVA}^{\text{WWR}}}{\text{CVA}}
$$

**Typical ranges:**
- Low WWR: 1.0-1.2×
- Moderate WWR: 1.2-1.5×
- High WWR (SWWR): 1.5-3.0× or higher

### Sensitivity Analysis

Compute CVA under varying correlation assumptions:

$$
\text{CVA}(\rho) \text{ for } \rho \in [-1, 1]
$$

Plot to understand WWR sensitivity.

---

## Mitigation Strategies

### 1. Trade Structuring
- Avoid trades with obvious SWWR
- Include break clauses
- Limit exposure to correlated counterparties

### 2. Collateralization
- Daily margin calls reduce exposure at default
- But MPOR still creates WWR window

### 3. Credit Support Annex (CSA) Design
- Lower thresholds
- Shorter MPOR
- Rating triggers

### 4. Portfolio Diversification
- Diversify counterparty exposure across sectors/regions
- Avoid concentration in WWR-prone relationships

### 5. Hedging
- Credit hedges on counterparties
- But watch for hedge-exposure correlation

---

## Backtesting WWR Models

### Methodology

1. Identify historical defaults
2. Compare actual exposure at default to model predictions
3. Assess whether WWR correlation captured

### Challenges

- Few default observations
- Exposure data may be unavailable
- Market conditions change

### Stress Testing Alternative

Use stressed scenarios to assess WWR impact:
- Simulate counterparty default under stress
- Compute exposure under same stress
- Compare to base case

---

## Key Takeaways

- WWR occurs when exposure increases as counterparty credit deteriorates
- Specific WWR: Direct transaction-counterparty link
- General WWR: Systemic correlation through market factors
- Standard CVA understates risk when WWR present
- Modeling requires joint exposure-default dynamics
- Regulators require explicit WWR assessment and capital treatment
- Mitigation through structuring, collateral, and diversification

---

## Further Reading

- Gregory, J., *Counterparty Credit Risk* (Chapter on Wrong-Way Risk)
- Basel Committee, "Guidelines for Computing Capital for Incremental Risk in the Trading Book"
- Hull, J. & White, A. (2012), "CVA and Wrong-Way Risk"
- Rosen, D. & Saunders, D. (2012), "CVA the Wrong Way"
- Pykhtin, M. & Rosen, D. (2010), "Pricing Counterparty Risk at the Trade Level and CVA Allocations"
