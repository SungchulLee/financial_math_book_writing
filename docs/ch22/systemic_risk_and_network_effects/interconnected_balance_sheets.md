# Interconnected Balance Sheets

Systemic risk arises when financial institutions are **interconnected** through balance sheets, contracts, and markets. Distress at one entity can propagate to others, potentially causing system-wide failures.

---

## Sources of Interconnectedness

### Direct Exposures

**Interbank lending:** Banks lend to each other in money markets

- Unsecured lending (Fed funds, LIBOR)
- Secured lending (repo)

**Derivative exposures:** OTC derivatives create bilateral credit risk

- Notional exposures can be massive
- Netting reduces but doesn't eliminate risk

**Payment and settlement:** Intraday credit extensions

### Indirect Exposures

**Common asset holdings:** Fire sales affect all holders

- Forced selling by one institution depresses prices
- Affects mark-to-market of others holding same assets

**Funding markets:** Shared reliance on short-term funding

- Money market stress affects all participants
- Confidence effects spread quickly

---

## Network Representation

### Nodes and Edges

Model the financial system as a directed graph:

- **Nodes:** Financial institutions
- **Edges:** Exposures (claims between institutions)
- **Edge weight:** Size of exposure

$$
\Pi_{ij} = \text{Exposure of } i \text{ to } j
$$

### Liability Matrix

Define the **relative liability matrix**:

$$
\bar{\Pi}_{ij} = \frac{\Pi_{ij}}{\sum_k \Pi_{ik}} = \frac{\text{Claim of } i \text{ on } j}{\text{Total liabilities of } i}
$$

This captures the fraction of each institution's liabilities owed to others.

---

## Eisenberg-Noe Clearing Model

Recall (see [§ Network Models: Eisenberg-Noe Clearing](systemic_risk_metrics.md#network-models-eisenberg-noe-clearing)) for the clearing-payment fixed point $p = \min(\bar{p},\, e + \Pi^\top p)$ and the contagion set $\mathcal{D} = \{i : p_i^* < \bar{p}_i\}$ that captures cascading defaults through reduced payments.

---

## Balance Sheet Amplification

### Leverage Effect

For a leveraged institution:

$$
\text{Equity} = \text{Assets} - \text{Liabilities}
$$

A 1% decline in assets causes $\frac{1}{\text{Equity/Assets}}$ % decline in equity.

**Example:** With 10× leverage, 1% asset loss = 10% equity loss.

### Fire Sale Externality

Recall (see [§ Fire Sale Models](contagion_models.md#fire-sale-models)) for the Greenwood-Landier-Thesmar price-impact model $\Delta P_a = -\lambda_a \cdot \text{Sales}_{ia}/D_a$ and the indirect-exposure / vulnerability index that quantify mark-to-market spillovers across overlapping portfolios.

### Margin Spirals

1. Asset prices fall
2. Margin calls issued
3. Forced liquidation
4. Further price decline
5. More margin calls...

**Procyclical feedback loop.**

---

## Network Topology and Stability

### Concentration vs Diversification

**Highly concentrated:** Few large, interconnected institutions

- Resilient to small shocks (diversification)
- Vulnerable to failure of large node (too-big-to-fail)

**Highly diversified:** Many small connections

- Resilient to individual failures
- Potentially vulnerable to system-wide shocks

### Core-Periphery Structure

Many financial networks exhibit core-periphery structure:

- **Core:** Highly interconnected major banks
- **Periphery:** Smaller institutions connected mainly to core

**Implication:** Core failures are systemically dangerous; peripheral failures less so.

### Metrics

**Degree centrality:** Number of connections

**Eigenvector centrality:** Importance based on connections to important nodes

**Betweenness centrality:** Role in connecting others

---

## Measurement Challenges

### Data Opacity

- Bilateral OTC exposures not publicly reported
- Aggregated data may hide concentration
- Real-time exposure data unavailable

### Dynamic Rebalancing

- Positions change rapidly
- Static network snapshots misleading
- Need to model dynamic evolution

### Feedback Effects

- Exposures depend on prices
- Prices depend on exposures
- Equilibrium analysis required

---

## Systemic Risk Measures

Recall (see [§ CoVaR](systemic_risk_metrics.md#covar-adrian-brunnermeier), [§ MES](systemic_risk_metrics.md#marginal-expected-shortfall-mes), [§ SRISK](systemic_risk_metrics.md#srisk-brownlees-engle)) for the formal definitions, estimation procedures, and capital-shortfall interpretation of the three primary market-based systemic risk metrics.

---

## Regulatory Implications

### G-SIB Framework

**Globally Systemically Important Banks** identified using:

- Size
- Interconnectedness
- Substitutability
- Cross-jurisdictional activity
- Complexity

**Higher capital requirements** for G-SIBs.

### Macroprudential Policy

- Capital buffers for systemic risk
- Countercyclical capital requirements
- Leverage ratio limits
- Large exposure limits

---

## Key Takeaways

- Financial institutions are interconnected through direct and indirect channels
- Network models (Eisenberg-Noe) capture payment cascades
- Leverage amplifies shocks; fire sales create externalities
- Network topology affects system resilience
- CoVaR, MES, SRISK measure systemic importance
- Regulation targets systemically important institutions

---

## Further Reading

- Eisenberg, L. & Noe, T. (2001), "Systemic Risk in Financial Systems"
- Allen, F. & Gale, D. (2000), "Financial Contagion"
- Adrian, T. & Brunnermeier, M. (2016), "CoVaR"
- Acharya, V. et al. (2017), "Measuring Systemic Risk"
- Greenwood, R., Landier, A., & Thesmar, D. (2015), "Vulnerable Banks"

---

## Exercises

**Exercise 1.** Consider a 3-bank Eisenberg-Noe network with external assets $e = (80, 60, 40)$, nominal liabilities $\bar{p} = (100, 80, 50)$, and relative liability matrix

$$
\Pi = \begin{pmatrix} 0 & 0.6 & 0.4 \\ 0.5 & 0 & 0.5 \\ 0.7 & 0.3 & 0 \end{pmatrix}
$$

Starting from $p^{(0)} = \bar{p}$, perform two iterations of the clearing algorithm $p^{(k+1)} = \min(\bar{p}, e + \Pi^\top p^{(k)})$. Identify which banks default. Explain why the algorithm converges.

??? success "Solution to Exercise 1"
    We have 3 banks with $e = (80, 60, 40)$, $\bar{p} = (100, 80, 50)$, and:

    $$
    \Pi = \begin{pmatrix} 0 & 0.6 & 0.4 \\ 0.5 & 0 & 0.5 \\ 0.7 & 0.3 & 0 \end{pmatrix}
    $$

    First compute $\Pi^\top$:

    $$
    \Pi^\top = \begin{pmatrix} 0 & 0.5 & 0.7 \\ 0.6 & 0 & 0.3 \\ 0.4 & 0.5 & 0 \end{pmatrix}
    $$

    **Iteration 0:** $p^{(0)} = \bar{p} = (100, 80, 50)$.

    Compute $\Pi^\top p^{(0)}$:

    $$
    (\Pi^\top p^{(0)})_1 = 0 \times 100 + 0.5 \times 80 + 0.7 \times 50 = 0 + 40 + 35 = 75
    $$

    $$
    (\Pi^\top p^{(0)})_2 = 0.6 \times 100 + 0 \times 80 + 0.3 \times 50 = 60 + 0 + 15 = 75
    $$

    $$
    (\Pi^\top p^{(0)})_3 = 0.4 \times 100 + 0.5 \times 80 + 0 \times 50 = 40 + 40 + 0 = 80
    $$

    Now $e + \Pi^\top p^{(0)} = (80 + 75,\; 60 + 75,\; 40 + 80) = (155, 135, 120)$.

    $$
    p^{(1)} = \min\!\big((100, 80, 50),\; (155, 135, 120)\big) = (100, 80, 50)
    $$

    Since every component of $e + \Pi^\top p^{(0)}$ exceeds $\bar{p}$, all banks can fully pay. We have $p^{(1)} = p^{(0)}$.

    **Iteration 1:** $p^{(1)} = (100, 80, 50)$.

    Since $p^{(1)} = p^{(0)}$, the algorithm has already converged:

    $$
    p^{(2)} = p^{(1)} = (100, 80, 50)
    $$

    **Result:** The clearing vector is $p^* = \bar{p} = (100, 80, 50)$. **No bank defaults.** Each bank's available resources (external assets plus incoming payments) exceed its nominal liabilities.

    To verify, each bank's total resources:

    - Bank 1: $80 + 75 = 155 \geq 100$ ✓
    - Bank 2: $60 + 75 = 135 \geq 80$ ✓
    - Bank 3: $40 + 80 = 120 \geq 50$ ✓

    **Why the algorithm converges:** The Eisenberg-Noe algorithm starts at $p^{(0)} = \bar{p}$ (the maximum possible payments) and produces a monotonically decreasing sequence $p^{(0)} \geq p^{(1)} \geq p^{(2)} \geq \cdots$, bounded below by $0$. Since payments are bounded and the mapping is monotone, the sequence converges by the monotone convergence theorem. Moreover, since payments take values in a finite set (each bank either pays fully or pays its available resources), convergence occurs in finitely many steps.

---

**Exercise 2.** A bank has assets of \$500 billion and equity of \$50 billion (leverage ratio of 10x). If assets decline by 2%, compute the percentage decline in equity. Now suppose the bank operates at 25x leverage. Repeat the calculation. Explain why leverage amplifies balance sheet shocks and connect this to the fire sale externality: if many banks at high leverage simultaneously face a 2% asset decline, what feedback loop can emerge?

??? success "Solution to Exercise 2"
    **Setup:** Assets = \$500B, Equity = \$50B, so Leverage = Assets/Equity = 10x.

    **Case 1: 10x leverage, 2% asset decline.**

    $$
    \Delta\text{Assets} = -2\% \times \$500\text{B} = -\$10\text{B}
    $$

    Since liabilities are fixed (debt doesn't change), the entire asset loss hits equity:

    $$
    \Delta\text{Equity} = -\$10\text{B}
    $$

    $$
    \%\text{ Equity decline} = \frac{\$10\text{B}}{\$50\text{B}} = 20\%
    $$

    A 2% asset decline causes a 20% equity decline. The amplification factor equals the leverage ratio: $10 \times 2\% = 20\%$.

    **Case 2: 25x leverage, 2% asset decline.**

    With 25x leverage: Assets = \$500B, Equity = \$500B/25 = \$20B.

    $$
    \Delta\text{Assets} = -2\% \times \$500\text{B} = -\$10\text{B}
    $$

    $$
    \%\text{ Equity decline} = \frac{\$10\text{B}}{\$20\text{B}} = 50\%
    $$

    A 2% asset decline causes a 50% equity decline at 25x leverage. The amplification factor is again leverage: $25 \times 2\% = 50\%$.

    In general, for leverage ratio $L = \text{Assets}/\text{Equity}$:

    $$
    \%\Delta\text{Equity} = L \times \%\Delta\text{Assets}
    $$

    **Fire sale feedback loop:** When many banks at high leverage simultaneously face a 2% asset decline:

    1. **Mark-to-market losses** deplete equity. At 25x leverage, a 2% decline wipes out 50% of equity.
    2. **Leverage constraints tighten.** Regulatory or internal leverage limits may be breached, forcing banks to reduce assets to restore target leverage.
    3. **Forced asset sales** to deleverage. If a bank needs to restore 25x leverage after losing half its equity, it must sell approximately half its assets.
    4. **Price impact** of selling pushes asset prices down further, since many banks are selling the same assets simultaneously.
    5. **Additional mark-to-market losses** from the depressed prices, which further deplete equity.
    6. **Cycle repeats**, creating a procyclical feedback spiral.

    This is the leverage-fire sale externality: each bank's individually rational deleveraging imposes costs on all other banks through price impact, potentially turning a small initial shock into a systemic crisis.

---

**Exercise 3.** Define CoVaR, MES, and SRISK. For a large bank with daily MES$_{5\%}$ = 4.0%, market equity $W = \$80$ billion, and book debt $D = \$720$ billion, compute LRMES using the approximation $\text{LRMES} \approx 1 - \exp(-18 \cdot \text{MES})$ and then compute SRISK with prudential ratio $k = 8\%$. Interpret the result: is this institution a net contributor to or absorber of systemic risk?

??? success "Solution to Exercise 3"
    **Definitions:**

    - **CoVaR:** The VaR of the system conditional on a specific institution being at its VaR level. $\Delta$CoVaR measures the difference in system VaR when the institution moves from its median to its stress state.
    - **MES:** The expected loss of an institution conditional on the system being in its tail ($R_{\text{sys}} \leq \text{VaR}_\alpha^{\text{sys}}$). It measures the institution's exposure to systemic stress.
    - **SRISK:** The expected capital shortfall in a crisis, combining market data (MES) with balance sheet data (debt, equity).

    **Computation:**

    Given: daily $\text{MES}_{5\%} = 4.0\%$, $W = \$80$B, $D = \$720$B, $k = 8\%$.

    **Step 1: LRMES.**

    $$
    \text{LRMES} = 1 - \exp(-18 \times 0.04) = 1 - e^{-0.72} = 1 - 0.4868 = 0.5132
    $$

    **Step 2: SRISK.**

    $$
    \text{SRISK} = k \cdot D - (1-k) \cdot W \cdot (1 - \text{LRMES})
    $$

    $$
    = 0.08 \times 720 - 0.92 \times 80 \times (1 - 0.5132)
    $$

    $$
    = 57.6 - 0.92 \times 80 \times 0.4868
    $$

    $$
    = 57.6 - 35.83 = \$21.77\text{B}
    $$

    **Interpretation:** SRISK = \$21.77 billion > 0, so this institution is a **net contributor** to systemic risk. In a severe crisis (approximately 40% market decline over 6 months), this bank would need \$21.77 billion in additional capital to meet the 8% prudential ratio. The large positive SRISK is driven by the high leverage ($D/W = 720/80 = 9$) and high tail sensitivity ($\text{MES} = 4\%$, implying over 51% equity loss in a crisis).

---

**Exercise 4.** Explain the core-periphery structure commonly observed in financial networks. A network has 3 core banks each connected to all other core banks and 7 peripheral banks, each connected to exactly 1 core bank. Compute the degree centrality of a core bank and a peripheral bank. If one core bank fails with LGD = 60%, describe qualitatively how losses would propagate differently compared to the failure of a peripheral bank. What does this imply for capital surcharges?

??? success "Solution to Exercise 4"
    **Core-periphery structure:**

    A core-periphery network consists of a small set of highly interconnected "core" banks and a larger set of "peripheral" banks that connect mainly to core banks. This structure is empirically observed in interbank lending networks (e.g., the Fed funds market, the UK interbank network).

    **Degree centrality computation:**

    The network has 3 core banks and 7 peripheral banks (10 total).

    *Core bank:* Each core bank is connected to:

    - 2 other core banks (all core banks interconnected)
    - Some number of peripheral banks. With 7 peripheral banks each connected to exactly 1 core bank, on average each core bank connects to $7/3 \approx 2.33$ peripheral banks.

    However, since each peripheral bank connects to exactly 1 core bank, the total peripheral connections to core = 7. If distributed as evenly as possible: two core banks connect to 2 peripheral banks each, and one connects to 3 (or some similar split). For simplicity, assume approximately equal distribution.

    Core bank degree: $2 + 7/3 \approx 4.33$ (on average). With integer assignments, degrees could be 4, 4, or 5 depending on the specific assignment.

    For a clean calculation: each core bank connects to 2 other core banks + roughly 2--3 peripheral banks.

    **Degree centrality** = degree / (n-1):

    - Core bank: degree $\approx 4$ to $5$, so centrality $= 4/9 \approx 0.44$ to $5/9 \approx 0.56$
    - Peripheral bank: degree $= 1$ (connected to exactly 1 core bank), so centrality $= 1/9 \approx 0.11$

    **Loss propagation:**

    *Core bank failure (LGD = 60%):*

    - The 2 other core banks each lose 60% of their exposure to the failing core bank. Since core banks are highly interconnected, these exposures may be large.
    - The 2--3 connected peripheral banks also lose 60% of their exposure.
    - If either of the remaining core banks defaults as a result, their own connections propagate losses further---potentially to the entire network.
    - The cascade can reach all peripheral banks through the remaining core banks.

    *Peripheral bank failure (LGD = 60%):*

    - Only the 1 connected core bank suffers direct losses.
    - The loss is typically small relative to the core bank's capital (since peripheral exposures are usually small).
    - Cascade is unlikely to propagate beyond the immediate core bank connection.

    **Implications for capital surcharges:** Core banks should face significantly higher capital surcharges because:

    - Their failure propagates to the entire network through the dense core connections
    - They are the conduit through which all peripheral shocks could potentially cascade
    - Their degree centrality is 4--5 times higher than peripheral banks
    - The systemic loss multiplier from a core failure is much larger than from a peripheral failure

    This justifies the G-SIB framework's higher capital requirements for systemically important institutions.

---

**Exercise 5.** The fire sale price impact model states $P' = P \cdot (1 - \alpha \cdot \text{Sales}/\text{Market Cap})$. Two banks each hold \$10 billion of a security with market cap \$50 billion and $\alpha = 0.5$. Bank 1 is forced to sell \$5 billion. Compute the new price as a fraction of the original. What is Bank 2's mark-to-market loss on its remaining \$10 billion holding? If Bank 2's equity is \$8 billion and a margin covenant triggers at a 40% equity loss, will Bank 2 be forced to sell? Trace the feedback loop.

??? success "Solution to Exercise 5"
    **Given:** Two banks each hold \$10B of a security with market cap \$50B, $\alpha = 0.5$. Bank 1 forced to sell \$5B.

    **Step 1: New price after Bank 1's sale.**

    $$
    P' = P \cdot \left(1 - \alpha \cdot \frac{\text{Sales}}{\text{Market Cap}}\right) = P \cdot \left(1 - 0.5 \times \frac{5}{50}\right)
    $$

    $$
    = P \cdot (1 - 0.05) = 0.95P
    $$

    The price drops to 95% of the original.

    **Step 2: Bank 2's mark-to-market loss.**

    Bank 2 holds \$10B at the original price. At the new price:

    $$
    \text{New value} = \$10\text{B} \times 0.95 = \$9.5\text{B}
    $$

    $$
    \text{Mark-to-market loss} = \$10\text{B} - \$9.5\text{B} = \$0.5\text{B}
    $$

    **Step 3: Check Bank 2's margin covenant.**

    Bank 2's equity = \$8B. A 40% equity loss threshold = $0.4 \times \$8\text{B} = \$3.2\text{B}$.

    Bank 2's loss is \$0.5B, which is $0.5/8 = 6.25\%$ of equity. This is well below the 40% threshold.

    **Bank 2 is NOT forced to sell** in the first round.

    **Step 4: Trace the feedback loop if the shock were larger.**

    However, consider what would happen if Bank 1 were forced to sell its entire \$10B holding:

    $$
    P' = P \cdot \left(1 - 0.5 \times \frac{10}{50}\right) = P \cdot 0.9 = 0.90P
    $$

    Bank 2's loss: $\$10\text{B} \times 0.10 = \$1.0\text{B}$, still only 12.5% of equity---below threshold.

    For the margin covenant to trigger, Bank 2 would need losses exceeding \$3.2B, requiring a price drop of more than 32%. This would need:

    $$
    \alpha \cdot \frac{\text{Sales}}{\text{Market Cap}} > 0.32 \implies \text{Sales} > \frac{0.32 \times 50}{0.5} = \$32\text{B}
    $$

    If the margin covenant *did* trigger, the feedback loop would unfold as:

    1. Bank 1 sells → price drops
    2. Bank 2's loss triggers margin covenant → Bank 2 forced to sell
    3. Bank 2's selling pushes price down further
    4. Other holders face losses, potential margin calls
    5. More selling → more price decline → more margin calls...

    This is the **margin spiral** or **fire sale spiral**---a procyclical feedback loop where each round of selling causes price declines that trigger further selling.

---

**Exercise 6.** In the DebtRank model, the distress propagation rule is

$$
h_i(t+1) = \min\left(1, h_i(t) + \sum_{j \in \mathcal{N}(i)} W_{ij} h_j(t)\right)
$$

For a network of 3 banks with $W_{12} = 0.3$, $W_{13} = 0.2$, $W_{21} = 0.4$, $W_{23} = 0.1$, $W_{31} = 0.5$, $W_{32} = 0.15$, and initial distress $h(0) = (1, 0, 0)$ (Bank 1 has fully defaulted), compute $h(1)$ and $h(2)$. What is the total DebtRank of the initial shock?

??? success "Solution to Exercise 6"
    **Given:** $W_{12} = 0.3$, $W_{13} = 0.2$, $W_{21} = 0.4$, $W_{23} = 0.1$, $W_{31} = 0.5$, $W_{32} = 0.15$. Initial distress: $h(0) = (1, 0, 0)$.

    The update rule is:

    $$
    h_i(t+1) = \min\!\left(1,\; h_i(t) + \sum_{j \in \mathcal{N}(i)} W_{ij}\, h_j(t)\right)
    $$

    **Compute $h(1)$:**

    Bank 1 (already fully distressed):

    $$
    h_1(1) = \min\!\left(1,\; 1 + W_{12} \cdot h_2(0) + W_{13} \cdot h_3(0)\right) = \min(1,\; 1 + 0.3 \times 0 + 0.2 \times 0) = 1
    $$

    Bank 2 (exposed to Bank 1):

    $$
    h_2(1) = \min\!\left(1,\; 0 + W_{21} \cdot h_1(0) + W_{23} \cdot h_3(0)\right) = \min(1,\; 0 + 0.4 \times 1 + 0.1 \times 0) = 0.4
    $$

    Bank 3 (exposed to Bank 1):

    $$
    h_3(1) = \min\!\left(1,\; 0 + W_{31} \cdot h_1(0) + W_{32} \cdot h_2(0)\right) = \min(1,\; 0 + 0.5 \times 1 + 0.15 \times 0) = 0.5
    $$

    So $h(1) = (1, 0.4, 0.5)$.

    **Compute $h(2)$:**

    Bank 1:

    $$
    h_1(2) = \min\!\left(1,\; 1 + 0.3 \times 0.4 + 0.2 \times 0.5\right) = \min(1,\; 1 + 0.12 + 0.10) = \min(1, 1.22) = 1
    $$

    Bank 2:

    $$
    h_2(2) = \min\!\left(1,\; 0.4 + 0.4 \times 1 + 0.1 \times 0.5\right) = \min(1,\; 0.4 + 0.4 + 0.05) = \min(1, 0.85) = 0.85
    $$

    Bank 3:

    $$
    h_3(2) = \min\!\left(1,\; 0.5 + 0.5 \times 1 + 0.15 \times 0.4\right) = \min(1,\; 0.5 + 0.5 + 0.06) = \min(1, 1.06) = 1
    $$

    So $h(2) = (1, 0.85, 1)$.

    **Total DebtRank:**

    The DebtRank of the initial shock (Bank 1's default) measures the total relative equity loss caused across the system, excluding the initially shocked bank. After convergence (or at the final step):

    $$
    \text{DebtRank} = \sum_{i \neq \text{shocked}} h_i(\text{final})
    $$

    At $t = 2$: $\text{DebtRank} = h_2(2) + h_3(2) = 0.85 + 1 = 1.85$.

    If we normalize by the number of banks (excluding the initial default), the average distress is $1.85/2 = 0.925$, meaning the initial shock caused nearly complete distress throughout the system. Bank 3 reached full distress ($h_3 = 1$) by round 2 due to its high exposure to Bank 1 ($W_{31} = 0.5$), and Bank 2 is at 85% distress. If we continued to $t = 3$, Bank 2 would likely reach $h_2 = 1$ as well, giving a maximum DebtRank of 2.

---

**Exercise 7.** Discuss why no single systemic risk metric is sufficient. A regulator monitors both CoVaR and SRISK for a set of banks. Bank A has a very high $|\Delta\text{CoVaR}|$ but low SRISK, while Bank B has moderate $|\Delta\text{CoVaR}|$ but very high SRISK. Explain what each metric is capturing about these two banks. Under what circumstances would each bank be the greater systemic concern? What additional information (e.g., from network models) might help resolve the discrepancy?

??? success "Solution to Exercise 7"
    **Why no single metric is sufficient:**

    Each systemic risk metric captures a different dimension of systemic importance. CoVaR measures *statistical tail dependence* between an institution and the system; SRISK measures *capital adequacy under stress*. These can diverge because they rely on different data and different definitions of "systemic."

    **Bank A: High $|\Delta\text{CoVaR}|$, low SRISK.**

    This profile suggests:

    - Bank A's distress is highly *correlated* with system-wide stress (high $\beta_1$ in the quantile regression), meaning when Bank A is in trouble, the system tends to be in trouble too.
    - However, Bank A has a **strong balance sheet**: either low leverage ($D/W$ is small) or high equity, so even in a severe crisis, Bank A does not face a capital shortfall.
    - Bank A might be a well-capitalized institution that is nevertheless a "bellwether" for the system---its distress signals systemic problems even though it itself is unlikely to need a bailout.
    - Example: A large, well-capitalized investment bank with diversified activities that is heavily correlated with the financial sector.

    **Bank B: Moderate $|\Delta\text{CoVaR}|$, high SRISK.**

    This profile suggests:

    - Bank B's statistical co-movement with the system during stress is moderate---its distress doesn't dramatically worsen the system's tail quantile.
    - However, Bank B is **highly leveraged** with a large balance sheet ($D$ is very large relative to $W$), so even moderate tail losses create a massive capital shortfall.
    - Bank B might be a traditional commercial bank with large but stable liabilities and moderate market risk, whose sheer size makes it a systemic risk.
    - Example: A very large, highly leveraged bank with mainly domestic loan exposures that are less correlated with the equity market index.

    **When each is the greater concern:**

    - **Bank A is more concerning** when the regulator cares about *contagion and feedback effects*. High $|\Delta\text{CoVaR}|$ means Bank A's distress *amplifies* system-wide stress. If the regulator's goal is to prevent cascading failures, Bank A is the priority because its distress has outsized impact on the system.
    - **Bank B is more concerning** when the regulator cares about *recapitalization costs* and fiscal exposure. High SRISK means Bank B will need a large government injection during a crisis. If the regulator's goal is to minimize taxpayer-funded bailouts, Bank B is the priority.

    **Additional information to resolve the discrepancy:**

    - **Network models (Eisenberg-Noe, DebtRank):** Would reveal whether Bank A or Bank B is more centrally positioned in the interbank network. A bank with high network centrality can propagate distress even if its balance sheet is strong.
    - **Common asset holdings data:** Would show whether Bank A or Bank B's portfolio overlaps with many other institutions, creating fire sale contagion risk.
    - **Funding structure:** Short-term wholesale funding dependence creates run risk that neither CoVaR nor SRISK directly captures.
    - **Substitutability:** If Bank A provides critical market-making or payment services, its failure would be disruptive regardless of its capital position.
    - **Deposit insurance exposure:** If Bank B has large insured deposits, taxpayer exposure is even larger than SRISK suggests.

    The fundamental lesson is that systemic risk is multidimensional: statistical co-movement (CoVaR), capital adequacy (SRISK), network position (DebtRank), and market function (substitutability) all matter. Effective macroprudential regulation requires monitoring all dimensions simultaneously.
