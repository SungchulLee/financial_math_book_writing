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

Recall (see [§ CVA and DVA](../valuation_adjustments_xva/cva_dva.md)): the standard unilateral CVA formula $\text{CVA} = \text{LGD}\int_0^T \text{EE}(t)\,dPD(t)$ treats $\text{EE}(t)=\mathbb{E}[E_t]$ as independent of the default time $\tau$. **This understates CVA when WWR is present.**

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

Recall (see [§ Default intensity and hazard rates](../../ch21/reduced_form_intensity_based_models/default_intensity_and_hazard_rates.md)): let the default intensity $\lambda_t = \lambda_0 e^{\beta\cdot X_t}$ depend on a market factor $X_t$ that also drives exposure. Positive $\beta$ with positive exposure sensitivity gives WWR; negative $\beta$ gives RWR. For FX exposure with an EM counterparty, $\lambda_t = \lambda_0 e^{\beta(S_t-S_0)/S_0}$: depreciation ($S_t$ up) raises default intensity.

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

---

## Exercises

**Exercise 1.** Define wrong-way risk (WWR) and right-way risk (RWR). For each of the following trades, classify the risk as WWR or RWR from the bank's perspective: (a) a put option purchased from a counterparty on the counterparty's own stock, (b) a commodity swap where the counterparty is a commodity producer receiving a fixed price, (c) a CDS where the bank buys protection on a sovereign from a domestic bank in that country.

??? success "Solution to Exercise 1"
    **Definitions:**

    **Wrong-way risk (WWR):** The adverse situation where exposure to a counterparty increases as the counterparty's credit quality deteriorates (i.e., as default becomes more likely):

    $$
    \text{Corr}(E_\tau, \mathbf{1}_{\tau \le T}) > 0
    $$

    High exposure coincides with high default probability — the worst timing for the surviving party.

    **Right-way risk (RWR):** The beneficial situation where exposure decreases as the counterparty's credit quality deteriorates:

    $$
    \text{Corr}(E_\tau, \mathbf{1}_{\tau \le T}) < 0
    $$

    Low exposure coincides with default — favorable timing for the surviving party.

    **Classification of each trade:**

    **(a) Put option purchased from a counterparty on the counterparty's own stock: WWR (Specific)**

    The bank has purchased a put option on Bank B's stock from Bank B. The exposure is:

    $$
    E_t = \max(K - S_t^B, 0)
    $$

    When Bank B's stock price $S_t^B$ falls:

    - The put option goes deeper in-the-money, so $E_t$ increases
    - Bank B's equity decline signals financial distress, so $PD_t$ increases

    Both exposure and default probability move in the same direction — this is **specific wrong-way risk** because the link is directly through the counterparty's own equity.

    **(b) Commodity swap where the counterparty is a commodity producer receiving a fixed price: RWR**

    The counterparty (commodity producer) receives a fixed price and pays the floating (market) commodity price. From the bank's perspective:

    $$
    V_t \propto \text{Floating Price}_t - \text{Fixed Price}
    $$

    When commodity prices fall:

    - The swap value to the bank becomes negative (bank pays fixed, receives lower floating), so $E_t$ decreases
    - The commodity producer faces revenue stress (lower commodity prices), so $PD_t$ increases

    Exposure decreases while default probability increases — this is **right-way risk**. The bank's exposure is low precisely when the counterparty is most likely to default.

    **(c) CDS where the bank buys protection on a sovereign from a domestic bank in that country: WWR (Specific)**

    The bank buys credit protection on Sovereign X from Bank Y, which is domiciled in country X. The exposure is:

    $$
    E_t = \text{MtM of CDS protection} \approx \text{CDS Spread}_t \times \text{Duration}
    $$

    When Sovereign X's credit deteriorates:

    - The CDS protection becomes more valuable (spread widens), so $E_t$ increases
    - Bank Y, heavily exposed to Sovereign X (through government bond holdings, local economic conditions, and potential bailout obligations), faces increased default risk, so $PD_t^Y$ increases

    Exposure to Bank Y increases when Bank Y is more likely to default — this is **specific wrong-way risk** driven by the direct link between the reference entity (sovereign) and the counterparty (domestic bank).

---

**Exercise 2.** In standard CVA, exposure and default probability are assumed independent. Write the unilateral CVA formula and explain how wrong-way risk violates this independence assumption. Propose a modification that accounts for positive correlation between exposure and default.

??? success "Solution to Exercise 2"
    **Standard unilateral CVA formula (independence assumption):**

    Under the assumption that exposure and default are independent:

    $$
    \text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot dPD(t)
    $$

    where:

    - $\text{LGD} = 1 - R$ is the loss given default
    - $\text{EE}(t) = \mathbb{E}[V_t^+]$ is the expected exposure, computed independently of the default event
    - $dPD(t) = \lambda(t) S(t) dt$ is the marginal default probability, with $\lambda(t)$ the hazard rate and $S(t) = e^{-\int_0^t \lambda(s)ds}$ the survival probability

    In discrete form:

    $$
    \text{CVA} = \text{LGD} \sum_{i=1}^{n} \text{EE}(t_i) \cdot [PD(t_i) - PD(t_{i-1})] \cdot D(0, t_i)
    $$

    The independence assumption means $\text{EE}(t)$ is computed without conditioning on default occurring at time $t$.

    **How WWR violates independence:**

    Wrong-way risk means that exposure and default are positively correlated. The true loss at default is:

    $$
    \text{Loss} = \text{LGD} \cdot E_\tau = \text{LGD} \cdot V_\tau^+
    $$

    The true CVA should use the **conditional** expectation of exposure given default:

    $$
    \text{CVA}^{\text{true}} = \text{LGD} \int_0^T \mathbb{E}[E_t | \tau = t] \cdot dPD(t)
    $$

    Under WWR, $\mathbb{E}[E_t | \tau = t] > \mathbb{E}[E_t] = \text{EE}(t)$ because conditioning on default selects scenarios where exposure tends to be high. Therefore:

    $$
    \text{CVA}^{\text{WWR}} > \text{CVA}^{\text{indep}}
    $$

    The standard CVA understates the true credit risk.

    **Modified CVA formula accounting for WWR:**

    Replace the unconditional EE with the conditional expectation:

    $$
    \text{CVA}^{\text{WWR}} = \text{LGD} \int_0^T \mathbb{E}[E_t | \tau = t] \cdot dPD(t)
    $$

    Computing $\mathbb{E}[E_t | \tau = t]$ requires a joint model of exposure and default. Several approaches:

    **Approach 1: Correlation multiplier.** Use a simple scaling:

    $$
    \mathbb{E}[E_t | \tau = t] = \text{EE}(t) \cdot (1 + w)
    $$

    where $w > 0$ is a WWR multiplier calibrated to data or stress scenarios. Then:

    $$
    \text{CVA}^{\text{WWR}} = (1 + w) \cdot \text{CVA}^{\text{indep}}
    $$

    **Approach 2: Joint simulation.** Model the default intensity as a function of the same market factors that drive exposure:

    $$
    \lambda_t = \lambda_0 \cdot e^{\beta X_t}
    $$

    where $X_t$ is a market factor (e.g., FX rate). Simulate $(X_t, \lambda_t)$ jointly, and compute:

    $$
    \text{CVA}^{\text{WWR}} = \text{LGD} \cdot \mathbb{E}\left[\int_0^T E_t \cdot \lambda_t \cdot e^{-\int_0^t \lambda_s ds} dt\right]
    $$

    This integrates over the joint dynamics, automatically capturing the positive correlation.

    **Approach 3: Copula-based.** Model the joint distribution of exposure $E_t$ and default time $\tau$ using a copula $C(F_{E_t}(x), F_\tau(t); \rho)$ with correlation parameter $\rho > 0$ for WWR.

---

**Exercise 3.** An FX derivative with an emerging-market counterparty has exposure that increases when the local currency depreciates. Explain why this is wrong-way risk. If the counterparty's default probability doubles when the currency depreciates by 30%, estimate the impact on CVA relative to the independence assumption.

??? success "Solution to Exercise 3"
    **Why this is wrong-way risk:**

    The bank holds an FX derivative with an emerging-market (EM) counterparty where the bank's exposure increases when the local currency depreciates. For example, the bank receives USD and pays local currency (LC) in a forward or swap.

    The exposure at time $t$ is approximately:

    $$
    E_t \propto (S_t - K)^+ \quad \text{where } S_t = \text{USD/LC exchange rate}
    $$

    When the LC depreciates ($S_t$ increases):

    - **Exposure increases:** The bank is owed more in USD terms
    - **Counterparty credit deteriorates:** The EM counterparty faces stress because:
        - Revenue is in LC (worth less in USD)
        - USD-denominated debt becomes harder to service
        - Local economic conditions worsen (inflation, capital flight)
        - Sovereign risk increases, affecting all domestic entities

    This positive correlation between exposure and default probability is **general wrong-way risk** (GWWR) — it arises from the systemic relationship between FX and EM credit, not from the specific structure of the trade.

    **Estimating the CVA impact:**

    Under the standard (independence) assumption:

    $$
    \text{CVA}^{\text{indep}} = \text{LGD} \int_0^T \text{EE}(t) \cdot \lambda(t) \cdot S(t) \, dt
    $$

    Under WWR, we need $\mathbb{E}[E_t | \tau = t]$ instead of $\text{EE}(t)$.

    Given that a 30% currency depreciation doubles the default probability, we can construct a simple model. Suppose:

    - The default intensity depends on the FX rate: $\lambda(S) = \lambda_0 \cdot (S/S_0)^\beta$
    - A 30% depreciation ($S = 1.3 S_0$) doubles the intensity: $\lambda_0 \cdot 1.3^\beta = 2\lambda_0$

    Solving for $\beta$:

    $$
    1.3^\beta = 2 \implies \beta = \frac{\ln 2}{\ln 1.3} = \frac{0.693}{0.263} \approx 2.64
    $$

    Under this model, conditioning on default selects scenarios where $S_t$ is high (LC has depreciated). The conditional exposure $\mathbb{E}[E_t | \tau = t]$ exceeds the unconditional $\text{EE}(t)$ because the default-weighted scenarios have higher FX rates and thus higher exposure.

    **Rough estimate of CVA impact:**

    Using a simplified approach, the WWR multiplier is approximately:

    $$
    \frac{\text{CVA}^{\text{WWR}}}{\text{CVA}^{\text{indep}}} \approx 1 + \rho \cdot \frac{\sigma_E}{\text{EE}} \cdot \frac{\sigma_\lambda}{\lambda}
    $$

    where $\rho$ is the correlation between log-exposure and log-intensity. For a moderate scenario:

    - Exposure volatility relative to mean: $\sigma_E / \text{EE} \approx 1.0$ (FX derivatives have high relative volatility)
    - Default intensity volatility: with $\beta \approx 2.64$ and FX volatility $\sigma_{\text{FX}} \approx 15\%$, $\sigma_\lambda / \lambda \approx \beta \cdot \sigma_{\text{FX}} \approx 0.40$
    - Correlation: $\rho \approx 0.6$--$0.8$ (strong FX-credit link for EM)

    This gives a WWR multiplier of approximately:

    $$
    \frac{\text{CVA}^{\text{WWR}}}{\text{CVA}^{\text{indep}}} \approx 1 + 0.7 \times 1.0 \times 0.40 \approx 1.28
    $$

    So CVA could be **28% higher** than under the independence assumption, with a plausible range of 20--50% depending on the specific calibration. For strongly correlated EM FX-credit dynamics, the multiplier can exceed 1.5.

---

**Exercise 4.** Describe two modeling approaches for wrong-way risk: (a) stochastic correlation between exposure and default intensity, and (b) conditional exposure given default. Discuss the advantages and limitations of each approach.

??? success "Solution to Exercise 4"
    **(a) Stochastic correlation between exposure and default intensity:**

    In this approach, both the exposure-driving market factor $X_t$ and the default intensity $\lambda_t$ are modeled as correlated stochastic processes:

    $$
    dX_t = \mu_X(X_t) dt + \sigma_X(X_t) dW_t^X
    $$

    $$
    d\lambda_t = \mu_\lambda(\lambda_t) dt + \sigma_\lambda(\lambda_t) dW_t^\lambda
    $$

    with $\text{Corr}(dW_t^X, dW_t^\lambda) = \rho$. The correlation $\rho$ may itself be stochastic or regime-dependent.

    The portfolio exposure $E_t = V_t(X_t)^+$ and the default intensity $\lambda_t$ are jointly simulated. CVA is then:

    $$
    \text{CVA} = \text{LGD} \cdot \mathbb{E}\left[\int_0^T E_t \cdot \lambda_t \cdot e^{-\int_0^t \lambda_s ds} dt\right]
    $$

    **Advantages:**

    - Captures dynamic, time-varying dependence between exposure and credit
    - Naturally produces the correct conditional expectations $\mathbb{E}[E_t | \tau = t]$
    - Can model both WWR ($\rho > 0$) and RWR ($\rho < 0$)
    - Flexible: can accommodate complex dependence structures (copulas, regime switching)

    **Limitations:**

    - Calibration difficulty: the correlation $\rho$ between market factors and default intensity is hard to estimate from data (few defaults, short time series)
    - Computational cost: joint simulation of exposure and default processes requires many paths
    - Model risk: results are sensitive to the assumed correlation structure, which may not be stable over time
    - Parameter uncertainty: small changes in $\rho$ can produce large changes in CVA

    **(b) Conditional exposure given default:**

    This approach directly models $\mathbb{E}[E_t | \tau = t]$ without explicitly specifying the joint dynamics:

    $$
    \text{CVA}^{\text{WWR}} = \text{LGD} \int_0^T \mathbb{E}[E_t | \tau = t] \cdot dPD(t)
    $$

    The conditional exposure can be estimated via:

    - **Stressed EE:** Compute $\text{EE}(t)$ under a stress scenario consistent with counterparty default (e.g., 2-sigma adverse market move)
    - **Hull-White multiplier:** $\mathbb{E}[E_t | \tau = t] = \text{EE}(t) \cdot (1 + w)$ with calibrated $w$
    - **Regression-based:** Use Monte Carlo simulation, then regress exposure on variables correlated with default

    **Advantages:**

    - Simpler to implement than full joint modeling
    - Directly addresses the quantity of interest ($\mathbb{E}[E_t | \tau = t]$)
    - Can use expert judgment or stress scenarios when data is scarce
    - Easier to explain to senior management and regulators

    **Limitations:**

    - Does not capture the full dependence structure — only the conditional mean
    - The multiplier $w$ or stressed scenarios may be ad hoc
    - Assumes a static relationship between default and exposure (no dynamic evolution)
    - May underestimate or overestimate WWR if the conditioning is too crude
    - Does not naturally produce a distribution of loss (only a point estimate of CVA)

    **Comparison:** Approach (a) is more theoretically complete but harder to calibrate and compute. Approach (b) is more practical and widely used in industry, but involves more approximation. Many banks use a hybrid: approach (a) for portfolios with identified WWR, and approach (b) as a regulatory add-on for general WWR.

---

**Exercise 5.** Regulators require banks to identify and stress-test for wrong-way risk. Describe a stress scenario for a portfolio of interest rate swaps with financial institution counterparties where wrong-way risk materializes. How should the stress test affect the bank's capital requirements?

??? success "Solution to Exercise 5"
    **Stress scenario for IRS portfolio with financial institution counterparties:**

    Consider a bank holding a portfolio of receive-fixed interest rate swaps with multiple financial institution (FI) counterparties. The stress scenario involves a **systemic financial crisis** with the following dynamics:

    **Market scenario:**

    1. **Interest rates fall sharply** (e.g., central bank cuts rates by 200bp in response to economic crisis)
    2. **Credit spreads widen dramatically** (e.g., FI CDS spreads widen from 50bp to 300bp)
    3. **Equity markets crash** (e.g., bank stocks fall 40--60%)
    4. **Interbank funding markets seize** (e.g., LIBOR-OIS spread blows out)

    **Why WWR materializes:**

    - **Exposure increases:** The receive-fixed swaps gain value as rates fall (the bank receives above-market fixed rates). The mark-to-market of the portfolio increases significantly:

    $$
    \Delta V \approx \text{DV01} \times \Delta r = \text{DV01} \times 200\text{bp}
    $$

    For a portfolio with DV01 of \$5M/bp, the gain is approximately \$1 billion.

    - **Counterparty credit deteriorates simultaneously:** The financial institution counterparties face:
        - Losses on their own portfolios (they are paying fixed on offsetting swaps, or have other rate-sensitive positions)
        - Wider funding spreads increasing borrowing costs
        - Potential margin calls they cannot meet
        - Systemic stress affecting all FIs (correlation of defaults increases)

    The exposure is highest precisely when the FI counterparties are most likely to default — classic wrong-way risk.

    **Historical precedent:** This scenario played out during the 2008 financial crisis. Banks with large receive-fixed IRS portfolios faced significant gains that were at risk due to counterparty defaults (Lehman Brothers being the most prominent example).

    **How the stress test should affect capital requirements:**

    1. **Higher CVA capital charge:** The stressed CVA under the WWR scenario is:

    $$
    \text{CVA}^{\text{stressed}} = \text{LGD} \sum_{i} \mathbb{E}[E_{t_i} | \text{stress}] \cdot PD^{\text{stressed}}(t_i)
    $$

    Both the conditional exposure and the default probability are elevated under stress, so $\text{CVA}^{\text{stressed}} \gg \text{CVA}^{\text{base}}$.

    2. **Capital add-on for WWR:** Regulators may require:
        - A multiplicative add-on: $\text{EAD}^{\text{WWR}} = \text{EAD} \times (1 + \alpha_{\text{WWR}})$ with $\alpha_{\text{WWR}} \approx 0.4$
        - Specific identification of WWR-prone counterparties with elevated alpha multipliers
        - Stress testing requirements demonstrating capital adequacy under the WWR scenario

    3. **Increased Effective EPE:** Under the IMM, the alpha multiplier ($\alpha \ge 1.4$) partially captures WWR. Banks with significant WWR exposure may be required to use $\alpha > 1.4$ or to compute a bank-specific alpha.

    4. **Pillar 2 considerations:** Supervisors may impose additional capital buffers under Pillar 2 if the bank's internal WWR assessment reveals material risk not fully captured by Pillar 1 formulas.

    5. **Risk mitigation actions:** The stress test results should also trigger:
        - Exposure limits on FI counterparties
        - Increased collateral requirements (lower CSA thresholds)
        - Portfolio diversification (moving trades to CCP clearing)
        - Credit hedging via CDS on key FI counterparties

---

**Exercise 6.** The opposite of wrong-way risk is right-way risk, where exposure decreases as the counterparty's credit deteriorates. Give two examples of trades exhibiting right-way risk. Should a bank reduce its CVA for trades with right-way risk? Discuss the regulatory and economic considerations.

??? success "Solution to Exercise 6"
    **Two examples of right-way risk (RWR):**

    **Example 1: Call option on counterparty's stock, purchased from a third party, with counterparty as guarantor.**

    More directly: A bank enters into a **commodity swap with a commodity consumer** (e.g., an airline receiving floating oil prices and paying fixed). The bank's exposure is:

    $$
    E_t = (V_t)^+ \propto (\text{Oil Price}_t - \text{Fixed Price})^+
    $$

    When oil prices rise:

    - Exposure increases (swap is in-the-money for the bank, as the airline pays more in floating)
    - But the airline's credit **improves**: lower fuel costs relative to fixed-price hedged level, better profitability

    When oil prices fall:

    - Exposure decreases (swap moves out-of-the-money for the bank)
    - The airline's credit **deteriorates**: higher relative fuel costs, potential financial distress

    Default is most likely when exposure is low — this is right-way risk.

    **Example 2: A bank sells a put option on gold to a gold mining company.**

    The bank's exposure is:

    $$
    E_t = \max(K - S_t^{\text{gold}}, 0)
    $$

    Wait — the bank *sold* the put, so the bank has no exposure (negative value position). Let us reconsider.

    **Corrected Example 2: A bank enters a receive-floating, pay-fixed interest rate swap with a corporate borrower.**

    The bank receives the floating rate and pays fixed. The bank's exposure is:

    $$
    E_t \propto (\text{Swap Rate}_t - \text{Fixed Rate})^+
    $$

    When interest rates rise:

    - Exposure increases (swap is in-the-money for the bank as floating receipts exceed fixed payments)
    - The corporate borrower's credit **may improve** if rising rates reflect a strong economy (higher revenues, better business conditions), or if the borrower has floating-rate assets that benefit

    When interest rates fall:

    - Exposure decreases
    - The borrower may face stress (economic downturn, deflation)

    Under this scenario, high exposure coincides with good economic conditions and strong counterparty credit — right-way risk.

    **Should a bank reduce its CVA for RWR trades?**

    **Economic argument for reduction:**

    If exposure and default are negatively correlated, the conditional exposure at default is lower than unconditional EE:

    $$
    \mathbb{E}[E_t | \tau = t] < \mathbb{E}[E_t] = \text{EE}(t)
    $$

    Therefore:

    $$
    \text{CVA}^{\text{RWR}} = \text{LGD}\int_0^T \mathbb{E}[E_t | \tau = t] \cdot dPD(t) < \text{CVA}^{\text{indep}}
    $$

    Economically, the bank's expected loss is lower because default tends to occur when exposure is low. A fair-value CVA should reflect this benefit.

    **Arguments for caution / against reduction:**

    1. **Model risk:** The negative correlation may not be stable. In a crisis, correlations can shift — what appears to be RWR under normal conditions may become WWR under stress (e.g., systemic events affect all correlations).

    2. **Regulatory conservatism:** Basel regulations generally do not allow banks to reduce capital for RWR. The rationale is asymmetric treatment: underestimating WWR is dangerous, while overestimating RWR is merely costly. Regulators prefer conservative approaches.

    3. **Prudential principle:** If the RWR benefit is uncertain, applying it to reduce CVA creates risk of underprovisioning. The downside of underestimating CVA (unexpected losses) outweighs the cost of overestimating it (slightly higher pricing).

    4. **Correlation instability:** Historical correlations used to justify RWR may break down precisely during the stress events that matter most for counterparty risk.

    5. **Accounting standards:** Under IFRS 13 / ASC 820, CVA should reflect fair value, which should incorporate all available information including RWR. However, auditors may challenge RWR reductions that rely on unstable or difficult-to-calibrate correlations.

    **Practical recommendation:**

    - For **accounting/fair-value CVA**, it is appropriate to include a modest RWR benefit if it can be robustly calibrated and documented, with conservative confidence intervals
    - For **regulatory capital**, banks should generally not reduce capital for RWR unless explicitly permitted by the regulator, with strong model validation
    - Banks should apply **asymmetric treatment**: fully recognize WWR (increase CVA) but only partially recognize RWR (reduce CVA by less than the model suggests), as a buffer against model risk
