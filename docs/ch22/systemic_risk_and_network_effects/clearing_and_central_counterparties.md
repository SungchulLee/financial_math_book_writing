# Clearing and Central Counterparties

**Central Counterparties (CCPs)** play a key role in mitigating counterparty risk by interposing themselves between trading parties. However, they also concentrate risk, creating new systemic considerations.

---

## Role of CCPs

### Novation and Interposition

When trades are cleared:
1. Original bilateral trade: A ↔ B
2. After novation: A ↔ CCP ↔ B

The CCP becomes:
- **Buyer to every seller**
- **Seller to every buyer**

### Risk Mitigation Benefits

**Multilateral netting:** Reduces total exposures

$$
\text{Bilateral Exposure} = \sum_{i<j} |E_{ij}|
$$

$$
\text{CCP Exposure} = \sum_i |E_i^{\text{CCP}}| < \sum_{i<j} |E_{ij}|
$$

**Standardized margin:** Consistent risk management

**Default management:** Orderly close-out procedures

---

## CCP Risk Framework

### Margining

**Variation Margin (VM):** Daily mark-to-market settlement

$$
\text{VM}_t = V_t - V_{t-1}
$$

**Initial Margin (IM):** Covers potential future exposure during MPOR

$$
\text{IM} \approx \text{VaR}_{99\%}(\text{Portfolio change over MPOR})
$$

### Default Fund (DF)

Pre-funded contributions from all members:

$$
\text{DF Total} = \sum_i \text{DF}_i
$$

Absorbs losses beyond defaulter's IM.

### Skin in the Game

CCP's own capital at risk:
- First loss after defaulter's margin
- Aligns incentives

---

## CCP Default Waterfall

**Sequential loss absorption:**

1. **Defaulting member's IM** → First buffer
2. **Defaulting member's DF contribution** → Second buffer
3. **CCP's skin-in-the-game** → CCP's own capital
4. **Non-defaulting members' DF** → Mutualized losses
5. **Assessment powers** → Additional member contributions
6. **CCP equity** → Final buffer before resolution

$$
\text{Loss Absorption Capacity} = \text{IM}_{\text{defaulter}} + \text{DF}_{\text{defaulter}} + \text{SITG} + \text{DF}_{\text{others}} + \text{Assessments}
$$

---

## Risk Concentration

### Too Big to Fail

CCPs concentrate risk:
- Single point of failure for cleared markets
- Failure would be catastrophic
- Implicitly backed by public sector

### Winner's Curse

Post-crisis mandates push trading to CCPs:
- More risk concentrated
- Higher systemic importance
- Regulatory paradox

### Interoperability Risk

CCPs may have exposures to each other:
- Link arrangements
- Cross-margining
- Default of one affects others

---

## Margin and Procyclicality

### Problem

During stress:
1. Volatility increases
2. IM requirements increase
3. Members face margin calls
4. Forced liquidation
5. Further volatility...

**Procyclical feedback loop.**

### Mitigants

**Anti-procyclicality measures:**
- Floor on IM (minimum even in calm periods)
- Lookback periods include stressed periods
- Caps on IM increases

**Regulatory guidance (EMIR, PFMI):**

$$
\text{IM}_{\text{stressed}} \le 1.25 \times \text{IM}_{\text{normal}} \quad \text{(indicative cap)}
$$

---

## Default Management

### Close-Out Process

When member defaults:

1. **Declaration:** CCP declares default
2. **Hedging:** CCP hedges portfolio to reduce risk
3. **Auction:** Surviving members bid on portfolio
4. **Allocation:** Losses absorbed via waterfall

### Auction Mechanism

Incentivize bidding:
- "Juniorization" of non-bidders (higher DF exposure)
- Split of auction profits

### Recovery and Resolution

If waterfall exhausted:
- **Recovery:** CCP attempts to continue
- **Resolution:** Orderly wind-down by authorities

---

## Stress Testing CCPs

### Cover-2 Standard

CCPs must hold resources to cover default of two largest members:

$$
\text{Total Resources} \ge \text{Exposure}_{\text{largest}} + \text{Exposure}_{\text{2nd largest}}
$$

under extreme but plausible conditions.

### Stress Scenarios

Test against:
- Historical stress (2008, 2020)
- Hypothetical extremes
- Multiple member defaults
- Wrong-way risk scenarios

### Supervisory Stress Tests

Coordinated across CCPs:
- Common scenarios
- Assess systemic implications
- Identify gaps

---

## CCP-Bank Nexus

### Member Exposures to CCP

Banks face CCP risk through:
- Margin posted (credit exposure to CCP)
- Default fund contributions (mutualized risk)
- Assessment powers (contingent liability)

### CCP Exposures to Banks

CCPs hold bank risk:
- Cash margin invested with banks
- IM in bank securities
- Bank guarantees

**Interconnection creates two-way risk.**

---

## Regulatory Framework

### PFMI (CPSS-IOSCO)

**Principles for Financial Market Infrastructures:**
- Governance
- Credit risk management
- Margin requirements
- Default management
- Liquidity risk

### Basel Treatment

**Exposure to CCPs:**
- Qualifying CCPs: 2% risk weight for trade exposures
- DF contributions: Higher risk weights
- Non-qualifying CCPs: 1250% risk weight

---

## Key Takeaways

- CCPs reduce bilateral counterparty risk through novation and netting
- The default waterfall provides layered loss absorption
- CCPs concentrate risk, creating systemic importance
- Margin procyclicality is a concern; mitigants exist
- Cover-2 standard sizes resources against extreme member defaults
- CCP-bank interconnections create two-way systemic risk
- Robust governance and stress testing are essential

---

## Further Reading

- BIS-IOSCO (2012), "Principles for Financial Market Infrastructures"
- Duffie, D. & Zhu, H. (2011), "Does a Central Clearing Counterparty Reduce Counterparty Risk?"
- Cont, R. (2017), "The End of the Waterfall: Default Resources of Central Counterparties"
- Murphy, D. (2013), *OTC Derivatives: Bilateral Trading and Central Clearing*
- Gregory, J. (2014), *Central Counterparties*
