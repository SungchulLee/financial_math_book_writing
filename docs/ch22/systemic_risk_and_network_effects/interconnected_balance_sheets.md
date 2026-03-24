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

### Setup

**$n$ institutions** with:
- External assets $e_i$ (assets outside the network)
- Interbank liabilities $\bar{p}_i$ (nominal obligations to other banks)
- Liability matrix $\Pi$ where $\Pi_{ij}$ = share of $i$'s liabilities owed to $j$

### Clearing Payments

A **clearing payment vector** $p = (p_1, \ldots, p_n)$ satisfies:

$$
p_i = \min\left(\bar{p}_i, \, e_i + \sum_{j=1}^n \Pi_{ji} p_j\right)
$$

**Interpretation:**
- Institution $i$ pays the minimum of:
  - What it owes ($\bar{p}_i$)
  - What it has: external assets plus what it receives from others

### Fixed-Point Characterization

The clearing vector is a fixed point:

$$
p = \min(\bar{p}, \, e + \Pi^\top p)
$$

**Theorem (Eisenberg-Noe, 2001):** Under mild conditions, there exists a unique clearing vector that can be computed iteratively.

### Default and Contagion

Institution $i$ **defaults** if $p_i < \bar{p}_i$.

**Contagion mechanism:**
1. Institution $A$ receives shock, reduces payments
2. $A$'s creditors receive less, may default themselves
3. Cascade propagates through network

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

When institution $i$ sells assets:
1. Price drops by amount proportional to sale
2. Other holders suffer mark-to-market losses
3. May trigger further sales

**Price impact:**

$$
P' = P \cdot \left(1 - \alpha \cdot \frac{\text{Sales}}{\text{Market Cap}}\right)
$$

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

### CoVaR (Adrian-Brunnermeier)

$$
\text{CoVaR}_\alpha^{i|j} = \text{VaR}_\alpha(\text{System} \mid \text{Institution } j \text{ at VaR})
$$

**$\Delta$CoVaR:** Contribution of institution $j$ to system risk:

$$
\Delta\text{CoVaR}^j = \text{CoVaR}^{i|j=\text{VaR}} - \text{CoVaR}^{i|j=\text{median}}
$$

### Marginal Expected Shortfall (MES)

$$
\text{MES}_i = \mathbb{E}[R_i \mid R_{\text{market}} < \text{VaR}_\alpha^{\text{market}}]
$$

Expected loss of institution $i$ when the market is in distress.

### SRISK

$$
\text{SRISK}_i = k \cdot D_i - (1-k) \cdot W_i \cdot (1 - \text{LRMES}_i)
$$

Capital shortfall in a crisis, where:
- $k$ = prudential capital ratio
- $D_i$ = debt
- $W_i$ = market cap
- $\text{LRMES}$ = long-run MES

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

---

**Exercise 2.** A bank has assets of \$500 billion and equity of \$50 billion (leverage ratio of 10x). If assets decline by 2%, compute the percentage decline in equity. Now suppose the bank operates at 25x leverage. Repeat the calculation. Explain why leverage amplifies balance sheet shocks and connect this to the fire sale externality: if many banks at high leverage simultaneously face a 2% asset decline, what feedback loop can emerge?

---

**Exercise 3.** Define CoVaR, MES, and SRISK. For a large bank with daily MES$_{5\%}$ = 4.0%, market equity $W = \$80$ billion, and book debt $D = \$720$ billion, compute LRMES using the approximation $\text{LRMES} \approx 1 - \exp(-18 \cdot \text{MES})$ and then compute SRISK with prudential ratio $k = 8\%$. Interpret the result: is this institution a net contributor to or absorber of systemic risk?

---

**Exercise 4.** Explain the core-periphery structure commonly observed in financial networks. A network has 3 core banks each connected to all other core banks and 7 peripheral banks, each connected to exactly 1 core bank. Compute the degree centrality of a core bank and a peripheral bank. If one core bank fails with LGD = 60%, describe qualitatively how losses would propagate differently compared to the failure of a peripheral bank. What does this imply for capital surcharges?

---

**Exercise 5.** The fire sale price impact model states $P' = P \cdot (1 - \alpha \cdot \text{Sales}/\text{Market Cap})$. Two banks each hold \$10 billion of a security with market cap \$50 billion and $\alpha = 0.5$. Bank 1 is forced to sell \$5 billion. Compute the new price as a fraction of the original. What is Bank 2's mark-to-market loss on its remaining \$10 billion holding? If Bank 2's equity is \$8 billion and a margin covenant triggers at a 40% equity loss, will Bank 2 be forced to sell? Trace the feedback loop.

---

**Exercise 6.** In the DebtRank model, the distress propagation rule is

$$
h_i(t+1) = \min\left(1, h_i(t) + \sum_{j \in \mathcal{N}(i)} W_{ij} h_j(t)\right)
$$

For a network of 3 banks with $W_{12} = 0.3$, $W_{13} = 0.2$, $W_{21} = 0.4$, $W_{23} = 0.1$, $W_{31} = 0.5$, $W_{32} = 0.15$, and initial distress $h(0) = (1, 0, 0)$ (Bank 1 has fully defaulted), compute $h(1)$ and $h(2)$. What is the total DebtRank of the initial shock?

---

**Exercise 7.** Discuss why no single systemic risk metric is sufficient. A regulator monitors both CoVaR and SRISK for a set of banks. Bank A has a very high $|\Delta\text{CoVaR}|$ but low SRISK, while Bank B has moderate $|\Delta\text{CoVaR}|$ but very high SRISK. Explain what each metric is capturing about these two banks. Under what circumstances would each bank be the greater systemic concern? What additional information (e.g., from network models) might help resolve the discrepancy?
