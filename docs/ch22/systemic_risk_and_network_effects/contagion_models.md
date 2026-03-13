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
