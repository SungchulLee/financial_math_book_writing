# Contagion Models

**Contagion models** study how financial distress spreads across institutions through networks, markets, and behavioral channels. Understanding contagion is essential for systemic risk assessment and macroprudential policy.

---

## Types of Contagion

### Credit Contagion

Direct exposure losses:

- Bank A owes Bank B
- Bank A defaults
- Bank B suffers losses, may default
- Cascade continues

### Price Contagion (Fire Sales)

Asset price externalities:

- Institution A forced to sell assets
- Prices drop
- Institution B's portfolio loses value
- B may be forced to sell
- **Fire sale spiral**

### Information Contagion

Confidence and learning effects:

- Bank A's failure signals problems
- Investors reassess similar banks
- Funding withdrawn from "similar" institutions
- **Bank run dynamics**

### Funding Contagion

Liquidity withdrawal:

- Money market stress
- Funding lines cut
- Institutions unable to roll debt
- Forced deleveraging

---

## Default Cascade Models

### Threshold Model

Institution $i$ defaults if:

$$
\text{Losses} > \text{Capital Buffer}
$$

$$
\sum_j \mathbf{1}_{\{j \text{ defaults}\}} \cdot \text{Exposure}_{ij} \cdot \text{LGD} > E_i
$$

### Cascade Algorithm

1. **Initial shock:** Some institutions fail exogenously
2. **Round 1:** Compute losses; identify new defaults
3. **Round 2:** New defaults cause further losses
4. **Iterate** until no new defaults

### Cascade Size

Let $n_k$ = number of defaults after round $k$.

**Cascade terminates** when $n_k = n_{k-1}$.

**Final cascade size:** $n_\infty$

---

## Fire Sale Models

### Greenwood-Landier-Thesmar Model

**Setup:** $n$ institutions hold overlapping portfolios

**Fire sale impact:** When institution $i$ deleverages:

$$
\Delta P_a = -\lambda_a \cdot \frac{\text{Sales}_{ia}}{D_a}
$$

where $\lambda_a$ is illiquidity of asset $a$ and $D_a$ is market depth.

**Indirect exposure:** Institution $j$'s loss from $i$'s deleveraging:

$$
\text{Loss}_j = \sum_a w_{ja} \cdot |\Delta P_a|
$$

**Vulnerability index:**

$$
v_i = \sum_j \text{Impact}_{ij} \cdot \text{Leverage}_j
$$

### Systemic Feedback

Total system losses exceed sum of individual losses:

$$
\text{System Loss} > \sum_i \text{Direct Loss}_i
$$

The multiplier captures fire sale externalities.

---

## Network Contagion Models

### Gai-Kapadia Model

Random network of interbank exposures:

- Average degree: number of connections
- Concentration: distribution of exposure sizes

**Key finding:** Trade-off between:

- **Resilience:** More connections share losses
- **Fragility:** More connections spread contagion

**Robust-yet-fragile:** Normal shocks absorbed; rare large shocks cascade.

### Contagion Threshold

Contagion spreads if the **basic reproduction number** $R_0 > 1$:

$$
R_0 = \bar{d} \cdot p_{\text{default}}
$$

where $\bar{d}$ = average degree and $p_{\text{default}}$ = probability a connection causes default.

### Phase Transitions

As connectivity increases:

- **Low connectivity:** Isolated failures
- **Intermediate:** Maximum contagion risk
- **High connectivity:** Shock absorption

---

## Market-Based Contagion

### Correlation Breakdown

During crises:

- Correlations increase ("all assets down together")
- Diversification benefits disappear
- Risk models underestimate losses

### Flight to Quality

Investors simultaneously:

- Sell risky assets
- Buy safe assets (Treasuries, cash)
- Amplifies price dislocations

### Volatility Contagion

**Volatility clustering across markets:**

- High volatility in one market
- Spreads to related markets
- Increases margin requirements globally

---

## Dynamic Contagion

### Time Evolution

Static models miss dynamics:

- Speed of contagion
- Intervention opportunities
- Recovery processes

**Differential equation models:**

$$
\frac{dI(t)}{dt} = \beta S(t) I(t) - \gamma I(t)
$$

where $I$ = infected (distressed), $S$ = susceptible, $\beta$ = transmission rate, $\gamma$ = recovery rate.

### Tipping Points

System may have:

- **Stable equilibrium:** Small shocks absorbed
- **Tipping point:** Beyond threshold, cascade accelerates
- **Hysteresis:** Recovery path differs from crisis path

---

## Measuring Contagion

### Event Study Approach

During crisis:

1. Identify shock event
2. Measure price changes across institutions
3. Control for common factors
4. Residual = contagion

### Granger Causality

Test whether institution $A$'s distress predicts $B$'s:

$$
R_B(t) = \alpha + \beta R_A(t-1) + \gamma R_M(t-1) + \epsilon_t
$$

Significant $\beta$ suggests contagion channel.

### Network Inference

Infer network from:

- Balance sheet data
- CDS spread co-movements
- Equity return correlations

---

## Policy Implications

### Circuit Breakers

- Trading halts during extreme moves
- Slow cascade propagation
- Allow information processing

### Lender of Last Resort

Central bank provides liquidity:

- Prevents funding contagion
- Stops fire sale spirals
- **Moral hazard concerns**

### Capital Requirements

Higher capital buffers:

- Absorb losses before default
- Reduce probability of cascade
- Cost: lower leverage, lower ROE

### Macroprudential Tools

- Countercyclical capital buffers
- Sectoral concentration limits
- Interconnection limits

---

## Key Takeaways

- Contagion spreads through credit, price, information, and funding channels
- Default cascades follow threshold dynamics
- Fire sales create externalities beyond direct exposures
- Network structure determines resilience vs fragility
- Systems can exhibit phase transitions and tipping points
- Policy tools include circuit breakers, LOLR, and macroprudential regulation

---

## Further Reading

- Gai, P. & Kapadia, S. (2010), "Contagion in Financial Networks"
- Greenwood, R., Landier, A., & Thesmar, D. (2015), "Vulnerable Banks"
- Glasserman, P. & Young, H.P. (2016), "Contagion in Financial Networks"
- Cont, R. et al. (2013), "Network Model of Credit Risk Contagion"
- Acemoglu, D., Ozdaglar, A., & Tahbaz-Salehi, A. (2015), "Systemic Risk and Stability in Financial Networks"

---

## Exercises

**Exercise 1.** Consider a network of 5 banks with the following interbank exposures $E_{ij}$ (bank $i$'s lending to bank $j$) and capital buffers $C_i$: Bank 1 lends 40 to Bank 2, 30 to Bank 3; Bank 2 lends 50 to Bank 3, 20 to Bank 4; Bank 3 lends 35 to Bank 4, 15 to Bank 5; Bank 4 lends 25 to Bank 5; Bank 5 lends 10 to Bank 1. Capital buffers are $C_1 = 60$, $C_2 = 45$, $C_3 = 30$, $C_4 = 20$, $C_5 = 15$, all in millions. Assuming LGD = 100%, if Bank 3 defaults exogenously, trace the default cascade. Which banks fail, and in what round?

??? success "Solution to Exercise 1"
    We trace the default cascade with LGD = 100%.

    **Network structure:** Exposures (bank $i$ lends to bank $j$):

    - Bank 1 → Bank 2: 40, Bank 1 → Bank 3: 30
    - Bank 2 → Bank 3: 50, Bank 2 → Bank 4: 20
    - Bank 3 → Bank 4: 35, Bank 3 → Bank 5: 15
    - Bank 4 → Bank 5: 25
    - Bank 5 → Bank 1: 10

    Capital buffers: $C_1 = 60$, $C_2 = 45$, $C_3 = 30$, $C_4 = 20$, $C_5 = 15$ (all in millions).

    **Initial shock:** Bank 3 defaults exogenously.

    **Round 1:** Identify creditors of Bank 3 (those who lent to Bank 3). With LGD = 100%, they lose their entire exposure:

    - Bank 1 lent 30 to Bank 3 → Loss = 30. Remaining capital: $60 - 30 = 30 > 0$. **Survives.**
    - Bank 2 lent 50 to Bank 3 → Loss = 50. Remaining capital: $45 - 50 = -5 < 0$. **Bank 2 defaults.**

    **Round 2:** Bank 2 has now defaulted. Identify creditors of Bank 2:

    - Bank 1 lent 40 to Bank 2 → Loss = 40. Remaining capital after Round 1: $30$. New remaining capital: $30 - 40 = -10 < 0$. **Bank 1 defaults.**

    **Round 3:** Bank 1 has now defaulted. Identify creditors of Bank 1:

    - Bank 5 lent 10 to Bank 1 → Loss = 10. Remaining capital: $15 - 10 = 5 > 0$. **Survives.**

    **Round 4:** No new defaults. Cascade terminates.

    **Summary:**

    | Round | Defaults | Mechanism |
    |-------|----------|-----------|
    | Initial | Bank 3 | Exogenous shock |
    | Round 1 | Bank 2 | Lost 50 on exposure to Bank 3; exceeded capital of 45 |
    | Round 2 | Bank 1 | Lost 30 (Bank 3) + 40 (Bank 2) = 70; exceeded capital of 60 |
    | Round 3 | None | Bank 5's loss (10) absorbed by capital (15) |

    **Banks that fail:** Banks 3, 2, and 1 (in that order). Banks 4 and 5 survive. Note that Bank 4 had exposures from Banks 2 and 3 (it received lending from them), but as a *borrower* from the defaulted banks, it is not directly harmed---the losses fall on *creditors* (lenders to the defaulted banks). Bank 5 survives because its only exposure to a defaulted bank (10 to Bank 1) is within its capital buffer.

---

**Exercise 2.** In the Gai-Kapadia network model, the basic reproduction number for contagion is

$$
R_0 = \bar{d} \cdot p_{\text{default}}
$$

where $\bar{d}$ is the average degree and $p_{\text{default}}$ is the probability that a connection causes default. For a network with average degree $\bar{d} = 5$ and individual exposure-to-capital ratio of 0.15, if $p_{\text{default}} \approx \text{exposure/capital}$, compute $R_0$. Is this network in the contagion regime ($R_0 > 1$)? How much would the average degree need to decrease to exit the contagion regime?

??? success "Solution to Exercise 2"
    **Given:** $\bar{d} = 5$, exposure-to-capital ratio = 0.15, and $p_{\text{default}} \approx \text{exposure/capital} = 0.15$.

    **Compute $R_0$:**

    $$
    R_0 = \bar{d} \cdot p_{\text{default}} = 5 \times 0.15 = 0.75
    $$

    **Is the network in the contagion regime?** Since $R_0 = 0.75 < 1$, the network is **not** in the contagion regime. On average, each default causes fewer than one additional default, so cascades die out. This is analogous to the sub-critical regime in epidemiology.

    **Critical degree for contagion:** The contagion threshold is $R_0 = 1$, which requires:

    $$
    \bar{d} \cdot p_{\text{default}} = 1 \implies \bar{d}_{\text{crit}} = \frac{1}{p_{\text{default}}} = \frac{1}{0.15} \approx 6.67
    $$

    So the average degree would need to **increase** to about 6.67 to enter the contagion regime (not decrease as the question suggests exploring). Conversely, the current network is safely below the threshold.

    To exit the contagion regime from an already-contagious state, one would need $\bar{d} < 1/p_{\text{default}}$. Equivalently, if the network were in the contagion regime (say $\bar{d} = 8$), reducing the average degree below $6.67$ would exit the regime.

    **Important nuance:** The $R_0$ formula uses the *average* degree, but network heterogeneity matters. In a network with heavy-tailed degree distributions, hubs with very high connectivity can sustain contagion even when $R_0 < 1$ on average. The Gai-Kapadia model shows that the "robust-yet-fragile" property depends not just on average connectivity but on the distribution of exposures.

---

**Exercise 3.** In the Greenwood-Landier-Thesmar fire sale model, the price impact of institution $i$ selling asset $a$ is $\Delta P_a = -\lambda_a \cdot \text{Sales}_{ia} / D_a$. Suppose two banks each hold \$1 billion of asset $a$ (with $\lambda_a = 0.5$, $D_a = \$5$B) and \$0.5 billion of asset $b$ (with $\lambda_b = 1.0$, $D_b = \$2$B). If Bank 1 is forced to sell 50% of its holdings, compute the price impact on each asset and the mark-to-market loss to Bank 2. Compare the contagion through asset $a$ versus asset $b$ and explain why illiquid assets amplify fire sale contagion.

??? success "Solution to Exercise 3"
    **Setup:** Two banks each hold \$1B of asset $a$ and \$0.5B of asset $b$. Parameters: $\lambda_a = 0.5$, $D_a = \$5$B; $\lambda_b = 1.0$, $D_b = \$2$B. Bank 1 sells 50% of its holdings.

    **Step 1: Compute Bank 1's sales.**

    - Sales of asset $a$: $50\% \times \$1\text{B} = \$0.5\text{B}$
    - Sales of asset $b$: $50\% \times \$0.5\text{B} = \$0.25\text{B}$

    **Step 2: Compute price impacts.**

    Using $\Delta P_a = -\lambda_a \cdot \text{Sales}_{1a} / D_a$:

    $$
    \Delta P_a = -0.5 \times \frac{0.5}{5} = -0.5 \times 0.1 = -5\%
    $$

    $$
    \Delta P_b = -1.0 \times \frac{0.25}{2} = -1.0 \times 0.125 = -12.5\%
    $$

    **Step 3: Compute Bank 2's mark-to-market losses.**

    Bank 2 still holds all its positions (\$1B of asset $a$, \$0.5B of asset $b$):

    - Loss on asset $a$: $\$1\text{B} \times 5\% = \$50\text{M}$
    - Loss on asset $b$: $\$0.5\text{B} \times 12.5\% = \$62.5\text{M}$
    - **Total loss to Bank 2: \$112.5M**

    **Step 4: Compare contagion channels.**

    | | Asset $a$ | Asset $b$ |
    |---|---|---|
    | Price impact | $-5\%$ | $-12.5\%$ |
    | Bank 2's loss | \$50M | \$62.5M |
    | Illiquidity $\lambda$ | 0.5 | 1.0 |
    | Market depth $D$ | \$5B | \$2B |

    **Asset $b$ creates more contagion** despite Bank 2 holding less of it (\$0.5B vs. \$1B). The price impact on asset $b$ ($-12.5\%$) is 2.5 times larger than on asset $a$ ($-5\%$), driven by two factors:

    1. **Higher illiquidity** ($\lambda_b = 1.0$ vs. $\lambda_a = 0.5$): Illiquid assets have larger price impacts per unit sold
    2. **Shallower market depth** ($D_b = \$2$B vs. $D_a = \$5$B): Sales represent a larger fraction of the market

    This explains why illiquid assets amplify fire sale contagion: the same selling pressure causes disproportionately larger price declines, which then cause larger mark-to-market losses for all holders. During the 2008 crisis, this mechanism was devastating for structured credit products (CDOs, RMBS) that were highly illiquid and had very shallow markets.

---

**Exercise 4.** The SIR-type differential equation model for financial contagion is

$$
\frac{dI(t)}{dt} = \beta S(t) I(t) - \gamma I(t)
$$

where $S + I + R = N$ (total institutions). Starting with $S(0) = 99$, $I(0) = 1$, $R(0) = 0$, $\beta = 0.005$, and $\gamma = 0.1$, compute $dI/dt$ at $t = 0$. Will the infection grow or shrink initially? Compute the epidemic threshold: what value of $\beta$ is needed for an epidemic ($dI/dt > 0$ at the start)?

??? success "Solution to Exercise 4"
    **Given:** $S(0) = 99$, $I(0) = 1$, $R(0) = 0$, $\beta = 0.005$, $\gamma = 0.1$.

    **Compute $dI/dt$ at $t = 0$:**

    $$
    \frac{dI}{dt}\bigg|_{t=0} = \beta S(0) I(0) - \gamma I(0) = 0.005 \times 99 \times 1 - 0.1 \times 1
    $$

    $$
    = 0.495 - 0.1 = 0.395
    $$

    Since $dI/dt = 0.395 > 0$, **the infection is growing initially**. The number of distressed institutions is increasing.

    **Epidemic threshold:** The infection grows when $dI/dt > 0$:

    $$
    \beta S(0) I(0) - \gamma I(0) > 0
    $$

    $$
    \beta S(0) > \gamma
    $$

    $$
    \beta > \frac{\gamma}{S(0)} = \frac{0.1}{99} \approx 0.00101
    $$

    So the critical transmission rate is $\beta_{\text{crit}} \approx 0.00101$. Any $\beta > 0.00101$ leads to an epidemic.

    Equivalently, the **basic reproduction number** is:

    $$
    \mathcal{R}_0 = \frac{\beta S(0)}{\gamma} = \frac{0.005 \times 99}{0.1} = \frac{0.495}{0.1} = 4.95
    $$

    Since $\mathcal{R}_0 = 4.95 > 1$, the system is well above the epidemic threshold. Each distressed institution "infects" approximately 5 others before recovering, leading to a rapidly growing cascade.

    **Financial interpretation:** $\beta$ captures the rate at which distress spreads through counterparty relationships and market contagion. $\gamma$ represents the recovery rate (e.g., government bailouts, recapitalization). The epidemic threshold condition $\beta S(0) > \gamma$ says that contagion spreads when the rate of new infections exceeds the recovery rate---a financial system with many susceptible institutions ($S$ large), strong transmission channels ($\beta$ large), or slow recovery ($\gamma$ small) is vulnerable to cascading distress.

---

**Exercise 5.** Explain the "robust-yet-fragile" property of financial networks. In a highly connected network, small shocks are absorbed because losses are distributed across many counterparties. However, a sufficiently large shock can cascade through the entire system. Provide a stylized example with a complete network of 4 banks (each bank connected to all others) showing: (a) a shock size that is absorbed without any cascade, and (b) a shock size that causes all banks to fail. What determines the critical shock threshold?

??? success "Solution to Exercise 5"
    **The "robust-yet-fragile" property:**

    In a highly connected network, each bank's exposure to any single counterparty is small (diversified), so small shocks are easily absorbed. However, this same connectivity means that if a shock is large enough to cause even one default, the cascade can reach every institution in the network because there is a path from every node to every other node.

    **Stylized example: Complete network of 4 banks.**

    Consider 4 banks, each with equity $E = 100$. In a complete network, each bank is connected to all 3 others. Suppose each bank has equal bilateral exposures $L$ to each of the other 3 banks.

    **(a) Shock absorbed without cascade:**

    Let each bank's interbank exposure be $L = 30$ to each counterparty (total interbank assets = 90 per bank). Suppose Bank 1 receives an external shock and defaults, with LGD = 100%.

    Each of the 3 surviving banks loses 30 from Bank 1's default:

    - Bank 2: Capital $100 - 30 = 70 > 0$ → Survives
    - Bank 3: Capital $100 - 30 = 70 > 0$ → Survives
    - Bank 4: Capital $100 - 30 = 70 > 0$ → Survives

    The shock of one bank defaulting is absorbed. **No cascade occurs** because the loss from any single counterparty ($30$) is less than each bank's capital ($100$).

    **(b) Shock causes all banks to fail:**

    Now let each bank's interbank exposure be $L = 40$ to each counterparty. Suppose Banks 1 and 2 default simultaneously due to a correlated external shock.

    Each surviving bank loses $40 + 40 = 80$ from the two defaults:

    - Bank 3: Capital $100 - 80 = 20 > 0$ → Survives (barely)

    But now suppose instead the exposures are $L = 60$. With Bank 1 defaulting:

    - Banks 2, 3, 4 each lose 60: Capital $100 - 60 = 40 > 0$ → Survive in Round 1

    Now increase $L = 40$ but the shock hits two banks. Banks 1 and 2 default:

    - Bank 3: loses $40 + 40 = 80$. Capital: $100 - 80 = 20 > 0$. Survives.
    - Bank 4: loses $40 + 40 = 80$. Capital: $100 - 80 = 20 > 0$. Survives.

    For a complete cascade, consider $L = 50$ and Bank 1 defaults:

    - Banks 2, 3, 4 each lose 50: Capital $100 - 50 = 50 > 0$. Survive.

    Now with $L = 40$ and a larger initial shock: suppose Banks 1 *and* 2 default, and LGD = 100%:

    - Bank 3 loses $40 + 40 = 80$, capital $100 - 80 = 20 > 0$. Survives.

    For all banks to fail from a single default, we need $L > E = 100$, i.e., exposure to a single counterparty exceeds capital. Let $L = 110$:

    - Bank 1 defaults → Banks 2, 3, 4 each lose 110. Capital $100 - 110 = -10 < 0$. **All fail in Round 1.**

    **Critical shock threshold:** In a complete network of $n$ banks with equal exposures $L$ and equity $E$, a single default triggers a cascade if and only if:

    $$
    L \cdot \text{LGD} > E
    $$

    More generally, if $k$ banks default simultaneously, the cascade spreads to all remaining banks when:

    $$
    k \cdot L \cdot \text{LGD} > E
    $$

    The critical threshold is $k_{\text{crit}} = \lceil E / (L \cdot \text{LGD}) \rceil$. Below this number of initial defaults, the shock is absorbed; at or above, the entire system collapses. This discontinuity---small shocks absorbed, large shocks catastrophic---is the essence of the "robust-yet-fragile" property.

---

**Exercise 6.** A researcher wants to measure contagion using the Granger causality approach. Describe how the regression

$$
R_B(t) = \alpha + \beta R_A(t-1) + \gamma R_M(t-1) + \epsilon_t
$$

tests for contagion from institution $A$ to $B$, controlling for market-wide factor $R_M$. Discuss the limitations of this approach: can Granger causality distinguish between true contagion and correlated exposures to common factors? What additional data or methodology would be needed to identify causal contagion channels?

??? success "Solution to Exercise 6"
    **Granger causality test for contagion:**

    The regression model is:

    $$
    R_B(t) = \alpha + \beta R_A(t-1) + \gamma R_M(t-1) + \epsilon_t
    $$

    **Testing for contagion:** The null hypothesis is $H_0: \beta = 0$ (institution $A$'s past returns have no predictive power for $B$'s returns after controlling for the market). A statistically significant $\hat{\beta} \neq 0$ suggests that information about $A$'s distress predicts future distress at $B$ beyond what the common market factor explains. This is interpreted as evidence of a contagion channel from $A$ to $B$.

    The market control $\gamma R_M(t-1)$ is crucial: without it, a significant $\beta$ could simply reflect that both $A$ and $B$ respond to common market-wide shocks. By including $R_M(t-1)$, we attempt to isolate the bilateral $A \to B$ channel.

    **Limitations:**

    1. **Correlation vs. causation:** Granger causality tests *temporal precedence*, not true causation. A significant $\beta$ could arise because $A$ reacts faster to common information than $B$ (lead-lag effect) rather than because $A$'s distress causes $B$'s distress.

    2. **Omitted common factors:** The single market return $R_M$ may not capture all common exposures. Both $A$ and $B$ could be exposed to a sector-specific factor (e.g., real estate), a liquidity factor, or a credit factor not captured by $R_M$. This omitted variable would create spurious "contagion" findings.

    3. **Time aggregation:** Daily data may miss within-day contagion. If both $A$ and $B$ react to the same intraday shock, it may appear as if $A$ at $t-1$ predicts $B$ at $t$ when both are actually reacting contemporaneously.

    4. **Nonlinearity:** The linear model may miss contagion that only occurs in extreme tails. Contagion may be regime-dependent---strong during crises but absent during calm periods.

    5. **Network effects:** $A$ may affect $B$ through a third institution $C$ (indirect contagion), which the bivariate test would miss or attribute to the wrong channel.

    **Additional data and methodology needed:**

    - **Balance sheet data** on bilateral exposures to identify direct credit channels
    - **Higher-frequency data** (intraday) to better isolate lead-lag relationships
    - **Multiple factor controls** (VIX, credit spreads, funding spreads) to capture common exposures
    - **Network-based models** (Eisenberg-Noe, DebtRank) that model the full system simultaneously
    - **Event studies** around specific default events to isolate the contagion channel
    - **Quantile regression** or threshold models to detect contagion that is active only in stress periods
    - **Instrumental variable** approaches to address endogeneity if a valid instrument for $A$'s distress can be found

---

**Exercise 7.** Compare credit contagion, fire sale contagion, and information contagion in terms of (a) transmission speed, (b) the type of data needed to model each channel, and (c) policy tools best suited to mitigate each. For the 2008 financial crisis, identify which channel was most significant during the Lehman Brothers default and explain the specific mechanisms through which it operated.

??? success "Solution to Exercise 7"
    **Comparison of contagion channels:**

    | Feature | Credit Contagion | Fire Sale Contagion | Information Contagion |
    |---------|-----------------|--------------------|-----------------------|
    | **(a) Speed** | Slow (days to weeks) | Fast (hours to days) | Very fast (minutes to hours) |
    | **(b) Data needed** | Bilateral exposures, LGD | Portfolio holdings, market depth, illiquidity | Market prices, CDS spreads, news sentiment |
    | **(c) Policy tools** | Capital requirements, large exposure limits, netting | Liquidity requirements, circuit breakers, asset purchase programs | Transparency, communication, deposit insurance |

    **Detailed comparison:**

    **(a) Transmission speed:**

    - **Credit contagion** operates through the settlement of obligations and recognition of losses. It requires the actual default of a counterparty and the subsequent claims process, which takes days to weeks. In the Lehman case, claims took months to fully settle.
    - **Fire sale contagion** operates through market prices and is much faster. When a distressed institution sells assets, prices adjust immediately, causing mark-to-market losses for all holders. This can unfold over hours as forced selling triggers margin calls and further selling.
    - **Information contagion** is the fastest. News of one institution's distress causes immediate reassessment of similar institutions. Equity prices, CDS spreads, and funding costs adjust within minutes. Bank runs can begin within hours of a news event.

    **(b) Data requirements:**

    - **Credit contagion** models (Eisenberg-Noe, default cascade) require detailed bilateral exposure data, which is typically confidential and available only to regulators.
    - **Fire sale models** (Greenwood-Landier-Thesmar) need portfolio holdings data, asset illiquidity measures, and market depth estimates.
    - **Information contagion** can be measured using publicly available market data (equity returns, CDS spreads) but modeling the causal mechanism requires understanding investor beliefs and information asymmetries.

    **(c) Policy tools:**

    - **Credit contagion** is mitigated by capital buffers (absorb losses before default), large exposure limits (cap bilateral exposures), and netting agreements (reduce gross exposures).
    - **Fire sale contagion** is mitigated by liquidity requirements (reduce forced selling), circuit breakers (slow price cascades), and central bank asset purchases (provide market depth).
    - **Information contagion** is mitigated by transparency and disclosure (reduce uncertainty), central bank communication (anchor expectations), and deposit insurance (prevent bank runs).

    **Lehman Brothers (September 2008):**

    The most significant channel was **information/funding contagion**, operating through the following mechanisms:

    1. **Money market freeze:** Lehman's default caused the Reserve Primary Fund (a major money market fund with Lehman exposure) to "break the buck," triggering a run on money market funds. This froze the commercial paper market, cutting funding for institutions system-wide.

    2. **Confidence collapse:** The decision not to bail out Lehman signaled that the government's implicit guarantee was unreliable, causing investors to reassess counterparty risk for all financial institutions. CDS spreads for major banks spiked within hours.

    3. **Funding withdrawal:** Banks hoarded liquidity and refused to lend to each other (LIBOR-OIS spread spiked from 100bp to over 350bp), creating a funding contagion spiral that affected even fundamentally solvent institutions.

    While credit contagion also occurred (direct Lehman counterparties suffered losses) and fire sale contagion played a role (distressed asset sales depressed prices), it was the information and funding contagion that turned a single bankruptcy into a global financial crisis. The speed and breadth of these channels overwhelmed the relatively slower credit loss channel.
