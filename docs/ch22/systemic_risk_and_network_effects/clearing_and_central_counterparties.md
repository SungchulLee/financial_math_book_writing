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

---

## Exercises

**Exercise 1.** Consider a network of 4 banks with bilateral exposures (in millions): $E_{12} = 50$, $E_{13} = 30$, $E_{21} = 40$, $E_{23} = 60$, $E_{31} = 20$, $E_{32} = 45$, $E_{14} = 25$, $E_{41} = 35$, $E_{24} = 15$, $E_{42} = 10$, $E_{34} = 55$, $E_{43} = 30$. Compute the total bilateral exposure $\sum_{i<j} |E_{ij} - E_{ji}|$ (net bilateral). Under CCP clearing with multilateral netting, each bank's net exposure to the CCP is $E_i^{\text{CCP}} = \sum_j (E_{ij} - E_{ji})$. Compute each bank's CCP exposure and the total CCP exposure. Compare and discuss the netting benefit.

---

**Exercise 2.** A CCP uses a default waterfall with the following layers: defaulter's IM (\$500M), defaulter's DF contribution (\$100M), CCP skin-in-the-game (\$50M), non-defaulting members' DF (\$800M), and assessment powers (up to \$400M). If a member defaults causing total losses of \$1.2 billion, trace the loss through the waterfall. How much of the non-defaulting members' DF is consumed? If losses were instead \$1.8 billion, would the CCP survive without resolution?

---

**Exercise 3.** Explain the procyclicality problem in CCP margining. During a crisis, volatility doubles from $\sigma = 1.5\%$ to $\sigma = 3.0\%$ daily. If the CCP computes IM as $\text{IM} = z_{0.99} \cdot \sigma \cdot \sqrt{\text{MPOR}} \cdot \text{Notional}$ with MPOR = 5 days and $z_{0.99} = 2.326$, compute the IM for a \$1 billion position under both normal and stressed volatility. What is the increase in margin calls? Describe two anti-procyclicality measures and their tradeoffs.

---

**Exercise 4.** Under the Basel treatment, trade exposures to a qualifying CCP receive a 2% risk weight, while exposures to a non-qualifying CCP receive a 1250% risk weight. A bank has \$10 billion in trade exposures cleared through a qualifying CCP and \$500 million through a non-qualifying CCP. Compute the RWA for each and the total capital charge (assuming 8% capital ratio). Discuss why the regulatory treatment creates strong incentives to clear through qualifying CCPs.

---

**Exercise 5.** The Cover-2 standard requires CCP resources to cover the simultaneous default of the two largest members under extreme conditions. Suppose the two largest members have stressed exposures of \$3 billion and \$2.5 billion respectively. The CCP has total IM of \$4 billion, total DF of \$1.5 billion, and own capital of \$200 million. Does the CCP meet the Cover-2 standard? If not, what is the shortfall, and how might the CCP close the gap?

---

**Exercise 6.** Describe the CCP-bank nexus and the two-way risk it creates. A bank posts \$5 billion in cash as margin to a CCP, and the CCP invests this cash in short-term deposits at banks (including the posting bank itself). Explain the circular risk: what happens if the CCP defaults (bank loses margin), and what happens if a major bank defaults (CCP loses investments)? Propose risk mitigation measures for each direction.

---

**Exercise 7.** Compare bilateral clearing and central clearing for a market with 10 dealers, each with an average of 20 bilateral trades. Under bilateral clearing, each pair must manage counterparty risk independently, resulting in $\binom{10}{2} = 45$ bilateral relationships. Under central clearing, all trades novate to the CCP. Discuss the tradeoffs: multilateral netting benefits, risk concentration, moral hazard, and the impact on market liquidity. Under what conditions might bilateral clearing be preferred for certain asset classes?
