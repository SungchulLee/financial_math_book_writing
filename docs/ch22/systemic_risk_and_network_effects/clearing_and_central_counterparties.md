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

??? success "Solution to Exercise 1"
    **Step 1: Compute net bilateral exposures.**

    For each pair $(i,j)$ with $i < j$, the net bilateral exposure is $|E_{ij} - E_{ji}|$:

    - Banks 1--2: $|E_{12} - E_{21}| = |50 - 40| = 10$
    - Banks 1--3: $|E_{13} - E_{31}| = |30 - 20| = 10$
    - Banks 1--4: $|E_{14} - E_{41}| = |25 - 35| = 10$
    - Banks 2--3: $|E_{23} - E_{32}| = |60 - 45| = 15$
    - Banks 2--4: $|E_{24} - E_{42}| = |15 - 10| = 5$
    - Banks 3--4: $|E_{34} - E_{43}| = |55 - 30| = 25$

    $$
    \text{Total net bilateral exposure} = 10 + 10 + 10 + 15 + 5 + 25 = 75
    $$

    **Step 2: Compute each bank's net CCP exposure.**

    Each bank's net position: $E_i^{\text{CCP}} = \sum_j (E_{ij} - E_{ji})$ (positive = net creditor, negative = net debtor).

    Bank 1:

    $$
    E_1^{\text{CCP}} = (E_{12} - E_{21}) + (E_{13} - E_{31}) + (E_{14} - E_{41})
    $$

    $$
    = (50 - 40) + (30 - 20) + (25 - 35) = 10 + 10 - 10 = 10
    $$

    Bank 2:

    $$
    E_2^{\text{CCP}} = (E_{21} - E_{12}) + (E_{23} - E_{32}) + (E_{24} - E_{42})
    $$

    $$
    = (40 - 50) + (60 - 45) + (15 - 10) = -10 + 15 + 5 = 10
    $$

    Bank 3:

    $$
    E_3^{\text{CCP}} = (E_{31} - E_{13}) + (E_{32} - E_{23}) + (E_{34} - E_{43})
    $$

    $$
    = (20 - 30) + (45 - 60) + (55 - 30) = -10 - 15 + 25 = 0
    $$

    Bank 4:

    $$
    E_4^{\text{CCP}} = (E_{41} - E_{14}) + (E_{42} - E_{24}) + (E_{43} - E_{34})
    $$

    $$
    = (35 - 25) + (10 - 15) + (30 - 55) = 10 - 5 - 25 = -20
    $$

    **Verification:** Net positions should sum to zero: $10 + 10 + 0 + (-20) = 0$ ✓

    **Step 3: Total CCP exposure.**

    $$
    \text{Total CCP exposure} = \sum_i |E_i^{\text{CCP}}| = |10| + |10| + |0| + |-20| = 40
    $$

    **Step 4: Comparison.**

    | Metric | Bilateral | CCP |
    |--------|-----------|-----|
    | Total exposure | 75 | 40 |
    | Reduction | --- | 46.7% |

    The CCP reduces total exposure from 75 to 40, a netting benefit of 46.7%. This occurs because multilateral netting allows offsetting exposures across multiple counterparties simultaneously. For example, Bank 3's net CCP exposure is zero---its claims and obligations across all counterparties cancel completely, which is impossible to achieve with purely bilateral netting.

---

**Exercise 2.** A CCP uses a default waterfall with the following layers: defaulter's IM (\$500M), defaulter's DF contribution (\$100M), CCP skin-in-the-game (\$50M), non-defaulting members' DF (\$800M), and assessment powers (up to \$400M). If a member defaults causing total losses of \$1.2 billion, trace the loss through the waterfall. How much of the non-defaulting members' DF is consumed? If losses were instead \$1.8 billion, would the CCP survive without resolution?

??? success "Solution to Exercise 2"
    **Default waterfall layers:**

    | Layer | Amount | Cumulative |
    |-------|--------|------------|
    | 1. Defaulter's IM | \$500M | \$500M |
    | 2. Defaulter's DF | \$100M | \$600M |
    | 3. CCP SITG | \$50M | \$650M |
    | 4. Non-defaulting members' DF | \$800M | \$1,450M |
    | 5. Assessment powers | \$400M | \$1,850M |

    **Scenario 1: Total losses = \$1.2 billion.**

    Trace through the waterfall:

    - Layer 1: Defaulter's IM absorbs \$500M. Remaining loss: $\$1,200\text{M} - \$500\text{M} = \$700\text{M}$
    - Layer 2: Defaulter's DF absorbs \$100M. Remaining: $\$700\text{M} - \$100\text{M} = \$600\text{M}$
    - Layer 3: CCP SITG absorbs \$50M. Remaining: $\$600\text{M} - \$50\text{M} = \$550\text{M}$
    - Layer 4: Non-defaulting members' DF absorbs \$550M of the available \$800M.

    **Answer:** \$550M of the non-defaulting members' DF is consumed (68.75% of the \$800M pool). The assessment powers (Layer 5) are not needed. The CCP survives.

    **Scenario 2: Total losses = \$1.8 billion.**

    - Layer 1: IM absorbs \$500M. Remaining: \$1,300M
    - Layer 2: DF (defaulter) absorbs \$100M. Remaining: \$1,200M
    - Layer 3: SITG absorbs \$50M. Remaining: \$1,150M
    - Layer 4: Non-defaulting DF absorbs \$800M. Remaining: \$350M
    - Layer 5: Assessment powers absorb \$350M of the available \$400M.

    Total absorption capacity = \$500M + \$100M + \$50M + \$800M + \$400M = \$1,850M.

    Since \$1,800M < \$1,850M, the CCP **survives without resolution**. However, the assessment powers are nearly exhausted (\$350M of \$400M used), leaving only \$50M of headroom. The CCP would need to replenish its default fund and potentially reassess margin requirements to restore resilience.

    If losses exceeded \$1,850M, the CCP would enter recovery (e.g., variation margin haircutting, partial tear-up of contracts) or resolution (orderly wind-down by authorities).

---

**Exercise 3.** Explain the procyclicality problem in CCP margining. During a crisis, volatility doubles from $\sigma = 1.5\%$ to $\sigma = 3.0\%$ daily. If the CCP computes IM as $\text{IM} = z_{0.99} \cdot \sigma \cdot \sqrt{\text{MPOR}} \cdot \text{Notional}$ with MPOR = 5 days and $z_{0.99} = 2.326$, compute the IM for a \$1 billion position under both normal and stressed volatility. What is the increase in margin calls? Describe two anti-procyclicality measures and their tradeoffs.

??? success "Solution to Exercise 3"
    **IM formula:** $\text{IM} = z_{0.99} \cdot \sigma \cdot \sqrt{\text{MPOR}} \cdot \text{Notional}$ with $z_{0.99} = 2.326$ and MPOR = 5 days.

    **Normal volatility ($\sigma = 1.5\%$ daily):**

    $$
    \text{IM}_{\text{normal}} = 2.326 \times 0.015 \times \sqrt{5} \times \$1\text{B}
    $$

    $$
    = 2.326 \times 0.015 \times 2.236 \times \$1\text{B}
    $$

    $$
    = 2.326 \times 0.03354 \times \$1\text{B} = 0.07802 \times \$1\text{B} = \$78.0\text{M}
    $$

    **Stressed volatility ($\sigma = 3.0\%$ daily):**

    $$
    \text{IM}_{\text{stressed}} = 2.326 \times 0.030 \times \sqrt{5} \times \$1\text{B}
    $$

    $$
    = 2.326 \times 0.030 \times 2.236 \times \$1\text{B}
    $$

    $$
    = 2.326 \times 0.06708 \times \$1\text{B} = 0.15604 \times \$1\text{B} = \$156.0\text{M}
    $$

    **Increase in margin calls:**

    $$
    \Delta\text{IM} = \$156.0\text{M} - \$78.0\text{M} = \$78.0\text{M}
    $$

    The margin requirement doubles (increases by 100%), since IM is proportional to $\sigma$ and volatility doubled.

    **Procyclicality problem:** During a crisis, precisely when institutions are most stressed and liquidity is scarce:

    1. Volatility spikes → IM requirements surge
    2. Members must post additional collateral (here, an extra \$78M per \$1B position)
    3. To raise cash for margin, members may be forced to liquidate other positions
    4. Forced liquidation depresses prices further → volatility increases more
    5. Higher volatility → even higher IM requirements → more forced selling

    **Anti-procyclicality measures:**

    *Measure 1: IM floor based on stressed periods.*

    Set IM using a lookback window that always includes a stress period (e.g., 10-year window including 2008). This means IM never drops to the "calm period" level, reducing the size of the jump during a crisis.

    - **Tradeoff:** Members pay higher margin during calm periods (opportunity cost of posting collateral), but face smaller margin calls during stress.

    *Measure 2: Cap on IM increases.*

    Limit the maximum increase in IM over any given period (e.g., IM cannot increase by more than 25% in a single quarter). The EMIR indicative guideline is $\text{IM}_{\text{stressed}} \leq 1.25 \times \text{IM}_{\text{normal}}$.

    - **Tradeoff:** Protects members from sudden large margin calls, but means the CCP is under-margined during extreme stress, potentially relying more heavily on the default fund and increasing mutualized losses.

---

**Exercise 4.** Under the Basel treatment, trade exposures to a qualifying CCP receive a 2% risk weight, while exposures to a non-qualifying CCP receive a 1250% risk weight. A bank has \$10 billion in trade exposures cleared through a qualifying CCP and \$500 million through a non-qualifying CCP. Compute the RWA for each and the total capital charge (assuming 8% capital ratio). Discuss why the regulatory treatment creates strong incentives to clear through qualifying CCPs.

??? success "Solution to Exercise 4"
    **Setup:** Bank has \$10B cleared through qualifying CCP and \$500M through non-qualifying CCP.

    **RWA computation:**

    *Qualifying CCP (2% risk weight):*

    $$
    \text{RWA}_{\text{qualifying}} = 0.02 \times \$10\text{B} = \$200\text{M}
    $$

    *Non-qualifying CCP (1250% risk weight):*

    $$
    \text{RWA}_{\text{non-qualifying}} = 12.50 \times \$500\text{M} = \$6,250\text{M}
    $$

    **Capital charge (at 8% capital ratio):**

    $$
    \text{Capital}_{\text{qualifying}} = 0.08 \times \$200\text{M} = \$16\text{M}
    $$

    $$
    \text{Capital}_{\text{non-qualifying}} = 0.08 \times \$6,250\text{M} = \$500\text{M}
    $$

    $$
    \text{Total capital charge} = \$16\text{M} + \$500\text{M} = \$516\text{M}
    $$

    **Summary:**

    | | Exposure | Risk Weight | RWA | Capital Charge |
    |---|---------|-------------|-----|----------------|
    | Qualifying CCP | \$10,000M | 2% | \$200M | \$16M |
    | Non-qualifying CCP | \$500M | 1250% | \$6,250M | \$500M |

    The \$500M exposure to the non-qualifying CCP generates a capital charge of \$500M---equal to 100% of the exposure (since $12.50 \times 0.08 = 1.00$). This is effectively a full deduction from capital.

    **Incentive effects:** The 625:1 ratio of risk weights (1250% vs. 2%) creates an extremely powerful incentive to clear through qualifying CCPs. For the same capital charge of \$500M, a bank could support \$312.5 billion in qualifying CCP exposures versus only \$500M in non-qualifying CCP exposures. This regulatory design achieves two objectives:

    1. It pushes OTC derivatives clearing toward well-regulated CCPs that meet PFMI standards
    2. It effectively penalizes clearing through CCPs in jurisdictions with weaker regulatory frameworks

    The result is concentration of clearing at a few qualifying CCPs, which reduces counterparty risk but increases the systemic importance of those CCPs.

---

**Exercise 5.** The Cover-2 standard requires CCP resources to cover the simultaneous default of the two largest members under extreme conditions. Suppose the two largest members have stressed exposures of \$3 billion and \$2.5 billion respectively. The CCP has total IM of \$4 billion, total DF of \$1.5 billion, and own capital of \$200 million. Does the CCP meet the Cover-2 standard? If not, what is the shortfall, and how might the CCP close the gap?

??? success "Solution to Exercise 5"
    **Cover-2 requirement:** Total resources $\geq$ Exposure of largest + Exposure of 2nd largest under stressed conditions.

    $$
    \text{Cover-2 requirement} = \$3.0\text{B} + \$2.5\text{B} = \$5.5\text{B}
    $$

    **Available resources:**

    $$
    \text{Total resources} = \text{IM} + \text{DF} + \text{Own capital} = \$4.0\text{B} + \$1.5\text{B} + \$0.2\text{B} = \$5.7\text{B}
    $$

    **Does the CCP meet Cover-2?**

    $$
    \$5.7\text{B} \geq \$5.5\text{B} \quad \checkmark
    $$

    Yes, the CCP meets the Cover-2 standard, but with only \$200M of headroom ($5.7 - 5.5 = 0.2$B), which is very thin.

    **Concerns about the thin buffer:**

    The \$200M margin represents only 3.6% excess over the requirement. This is precarious because:

    - Stressed exposures may be underestimated (model risk)
    - Multiple defaults could occur simultaneously with correlation
    - Market conditions during a double default could be worse than the "extreme but plausible" scenario assumed

    **If the CCP did not meet Cover-2 (or to increase the buffer), it could:**

    1. **Increase initial margin requirements:** Raise IM models to capture more tail risk. Tradeoff: higher costs for members, procyclicality.
    2. **Increase default fund contributions:** Require members to post more to the DF. Tradeoff: higher capital costs, may reduce market participation.
    3. **Increase CCP own capital (SITG):** CCP shareholders invest more equity. Tradeoff: lower return on equity for CCP owners.
    4. **Reduce concentration:** Impose position limits on the largest members so that their stressed exposures decrease.
    5. **Secure committed credit lines:** Arrange standby liquidity facilities with central banks or commercial banks to supplement resources in a crisis.

---

**Exercise 6.** Describe the CCP-bank nexus and the two-way risk it creates. A bank posts \$5 billion in cash as margin to a CCP, and the CCP invests this cash in short-term deposits at banks (including the posting bank itself). Explain the circular risk: what happens if the CCP defaults (bank loses margin), and what happens if a major bank defaults (CCP loses investments)? Propose risk mitigation measures for each direction.

??? success "Solution to Exercise 6"
    **CCP-bank nexus and two-way risk:**

    A bank posts \$5B in cash margin to the CCP. The CCP invests this cash in short-term deposits at banks, potentially including the posting bank itself.

    **Direction 1: CCP defaults → Bank loses margin.**

    If the CCP defaults (fails to return margin), the bank loses its \$5B cash posting. This is a direct credit exposure of the bank to the CCP. The loss could occur if:

    - Multiple member defaults exhaust the CCP's waterfall
    - The CCP has operational or governance failures
    - The CCP invests margin in risky or illiquid assets that lose value

    The bank's \$5B margin posting is effectively an unsecured loan to the CCP (although in practice, regulations require margin to be held in segregated accounts, reducing but not eliminating this risk).

    **Direction 2: Major bank defaults → CCP loses investments.**

    The CCP holds margin cash in bank deposits. If a major bank fails:

    - CCP loses the deposits held at the defaulting bank
    - This coincides with the CCP potentially facing the same bank's default as a clearing member
    - The CCP faces a "double hit": losing invested margin *and* bearing the defaulting member's clearing losses
    - This is **wrong-way risk**: the CCP's investment losses are correlated with its clearing losses

    **Circular risk:** The circularity is especially dangerous:

    1. Bank posts cash margin to CCP
    2. CCP deposits cash back at the same bank
    3. If the bank defaults, CCP loses its investment
    4. CCP may not have sufficient resources to return margin to other members
    5. Other members face losses, potentially triggering further defaults

    **Risk mitigation measures:**

    *For Direction 1 (bank exposed to CCP):*

    - **Segregation requirements:** Margin held in legally segregated accounts, protected in CCP bankruptcy
    - **Diversification of CCPs:** Banks should clear across multiple CCPs to avoid concentration
    - **Qualifying CCP standards:** PFMI principles ensure robust risk management
    - **Recovery and resolution frameworks:** Ensure orderly wind-down if CCP fails, with tools like variation margin haircutting and partial tear-ups to protect margin

    *For Direction 2 (CCP exposed to banks):*

    - **Investment policy limits:** CCP should diversify cash investments across many banks, with concentration limits per bank
    - **High-quality liquid assets:** Invest margin in government securities rather than bank deposits
    - **Reverse repo with central bank:** Place cash in central bank facilities (where available)
    - **Avoid investing at clearing member banks:** Eliminate the circular exposure by not depositing margin at the banks that posted it
    - **Stress testing:** Include wrong-way investment risk in CCP stress tests (test scenarios where the defaulting member is also the bank where margin is invested)

---

**Exercise 7.** Compare bilateral clearing and central clearing for a market with 10 dealers, each with an average of 20 bilateral trades. Under bilateral clearing, each pair must manage counterparty risk independently, resulting in $\binom{10}{2} = 45$ bilateral relationships. Under central clearing, all trades novate to the CCP. Discuss the tradeoffs: multilateral netting benefits, risk concentration, moral hazard, and the impact on market liquidity. Under what conditions might bilateral clearing be preferred for certain asset classes?

??? success "Solution to Exercise 7"
    **Market setup:** 10 dealers, each with an average of 20 bilateral trades.

    **Bilateral clearing:**

    - $\binom{10}{2} = 45$ bilateral relationships to manage
    - Each pair must independently: assess counterparty credit risk, negotiate CSAs (Credit Support Annexes), exchange margin, manage disputes
    - Netting is bilateral only: offsets within each pair, but not across counterparties
    - Total gross exposure can be large because netting is limited

    **Central clearing:**

    - All 10 dealers face a single counterparty (the CCP)
    - 10 clearing relationships instead of 45
    - Multilateral netting: all trades offset against each other through the CCP
    - Standardized margining and default management

    **Tradeoffs:**

    *Multilateral netting benefits:*

    Central clearing provides significant netting benefits. With bilateral clearing, a dealer's exposure to each counterparty is netted separately. With CCP clearing, all trades are netted against each other. For 10 dealers, the netting efficiency can be substantial---theoretical models suggest reductions of 50--90% in total exposure, depending on the correlation structure of trades. As shown in Exercise 1, even a simple 4-bank example achieved a 47% reduction.

    *Risk concentration:*

    Central clearing concentrates counterparty risk at the CCP. If the CCP fails, all 10 dealers are simultaneously affected---a single point of failure for the entire market. Under bilateral clearing, the failure of one dealer affects only its counterparties. This is the "too-big-to-fail" problem applied to market infrastructure: the CCP becomes systemically important precisely because it mitigates bilateral counterparty risk.

    *Moral hazard:*

    - CCP clearing may reduce members' incentives to monitor counterparty credit quality, since losses are mutualized through the default fund
    - Members may take larger positions knowing that the CCP's risk management and default waterfall provide a safety net
    - The implicit government backstop of systemically important CCPs creates additional moral hazard

    *Market liquidity impact:*

    - Central clearing can *improve* liquidity by reducing counterparty risk concerns that might otherwise discourage trading
    - However, margin requirements *reduce* available capital for trading, potentially decreasing market-making capacity
    - Procyclical margin calls during stress can *worsen* liquidity precisely when it is most needed

    **When bilateral clearing may be preferred:**

    1. **Bespoke/illiquid products:** Highly customized derivatives (structured notes, exotic options) that cannot be standardized for CCP clearing. The CCP requires standardization for risk management and auction processes.

    2. **Low counterparty concentration:** When there are many diverse participants and the netting benefit of central clearing is small (e.g., end-users who trade infrequently).

    3. **Cross-product netting:** Bilateral netting across different asset classes (rates, credit, equity, FX) may be more efficient than clearing at separate CCPs that each handle only one product type.

    4. **Markets with few participants:** When there are too few dealers to support a viable CCP (insufficient default fund diversification, auction liquidity concerns).

    5. **Emerging or frontier markets:** Where the regulatory and legal infrastructure for CCP operation is not yet mature, bilateral clearing with strong CSA agreements may be more reliable.

    6. **Wrong-way risk products:** Products where the exposure increases when the counterparty's credit quality deteriorates (e.g., CDS on the counterparty's own debt) may be better managed bilaterally with tailored risk mitigation.
