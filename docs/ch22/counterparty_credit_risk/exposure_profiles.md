# Exposure Profiles

Counterparty credit risk (CCR) arises from the possibility that a counterparty defaults while a derivative position has positive value. **Exposure profiles** describe how this potential loss evolves over the life of the trade.

---

## Definition of Exposure

For a derivative portfolio with value process $V_t$, the **exposure** at time $t$ is:

$$
E_t = \max(V_t, 0) = V_t^+
$$

**Interpretation:** 
- If $V_t > 0$: We are owed money; default causes loss
- If $V_t < 0$: We owe money; default causes no direct loss (ignoring replacement cost)

Exposure is **one-sided**—only positive values matter for CCR.

---

## Expected Exposure (EE)

The **Expected Exposure** at time $t$ is:

$$
\text{EE}(t) = \mathbb{E}^{\mathbb{Q}}[E_t] = \mathbb{E}^{\mathbb{Q}}[V_t^+]
$$

where the expectation is typically under the risk-neutral measure $\mathbb{Q}$.

**Properties:**
- EE is deterministic (a function of time only)
- EE depends on portfolio composition and market dynamics
- EE is always non-negative

---

## Expected Positive Exposure (EPE)

The **Expected Positive Exposure** is the time-averaged EE:

$$
\text{EPE} = \frac{1}{T} \int_0^T \text{EE}(t) \, dt
$$

**Discrete approximation:**
$$
\text{EPE} \approx \frac{1}{n} \sum_{i=1}^n \text{EE}(t_i)
$$

EPE is a single number summarizing average exposure over the portfolio's life.

---

## Effective EPE and Effective EE

Regulatory capital calculations use **non-decreasing** versions:

**Effective EE:**
$$
\text{Effective EE}(t) = \max_{s \le t} \text{EE}(s)
$$

**Effective EPE:**
$$
\text{Effective EPE} = \frac{1}{\min(1\text{ year}, T)} \int_0^{\min(1\text{ year}, T)} \text{Effective EE}(t) \, dt
$$

**Rationale:** Prevents gaming by structuring trades to have low EE at measurement dates but high EE in between.

---

## Potential Future Exposure (PFE)

**PFE** is a high-quantile measure of future exposure:

$$
\text{PFE}_\alpha(t) = \inf\{x : \mathbb{P}(E_t \le x) \ge \alpha\}
$$

Typically $\alpha = 0.95$ or $0.99$.

**Interpretation:** With probability $\alpha$, exposure at time $t$ will not exceed $\text{PFE}_\alpha(t)$.

**Relation to EE:**
- EE measures average exposure
- PFE measures tail exposure
- $\text{PFE}_\alpha(t) \ge \text{EE}(t)$ always

---

## Exposure Profile Shapes

Different products have characteristic exposure profiles:

### Interest Rate Swap

**Receiver swap (receive fixed, pay floating):**
- Exposure peaks mid-life
- "Hump-shaped" profile
- Pull-to-par effect near maturity

$$
\text{EE}(t) \text{ peaks at } t \approx T/2
$$

### FX Forward

- Exposure grows approximately linearly with time
- Maximum at maturity
- No intermediate payments to reset exposure

### Cross-Currency Swap

- Combines features of IRS and FX
- Notional exchange at maturity creates jump
- Complex profile shape

### Options

- Buyer has exposure; seller does not (after premium paid)
- Exposure depends on moneyness evolution

---

## Drivers of Exposure Profiles

### 1. Product Structure
- Payment schedules
- Optionality
- Notional exchange

### 2. Market Factors
- Interest rate volatility
- FX volatility
- Correlation structure

### 3. Portfolio Effects
- Netting benefits
- Collateral agreements
- Trade maturity mix

### 4. Time Effects
- Diffusion of market factors
- Pull-to-par for swaps
- Time decay for options

---

## Netting and Exposure

Under a **netting agreement**, exposure is calculated at the portfolio level:

$$
E_t^{\text{netted}} = \left(\sum_{i=1}^n V_{i,t}\right)^+ \le \sum_{i=1}^n V_{i,t}^+ = \sum_{i=1}^n E_{i,t}
$$

**Netting benefit:**
$$
\text{Netting Benefit} = \frac{\sum_i \text{EE}_i - \text{EE}_{\text{netted}}}{\sum_i \text{EE}_i}
$$

Netting is most valuable when trades have:
- Opposite signs (long and short)
- Different maturities
- Low correlation of values

---

## Collateralization and Exposure

**Collateral (margin)** reduces exposure:

$$
E_t^{\text{collateralized}} = \max(V_t - C_t, 0)
$$

where $C_t$ is the collateral held.

### Margin Period of Risk (MPOR)

Collateral is not instantaneously available. The **MPOR** is the time to:
- Call for additional margin
- Receive and process collateral
- Close out the position if counterparty defaults

Typical MPOR: 10 business days (bilateral), 5 days (CCP).

**Effective exposure under collateral:**
$$
\text{EE}^{\text{coll}}(t) = \mathbb{E}[\max(V_t - C_{t-\text{MPOR}}, 0)]
$$

---

## CVA and Exposure

**Credit Valuation Adjustment (CVA)** depends directly on exposure profiles:

$$
\text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot \lambda(t) \cdot e^{-\int_0^t (r(s) + \lambda(s)) ds} \, dt
$$

where:
- LGD = Loss Given Default (typically 60%)
- $\lambda(t)$ = default intensity (hazard rate)
- $r(t)$ = risk-free rate

**Discrete approximation:**
$$
\text{CVA} \approx \text{LGD} \sum_{i=1}^n \text{EE}(t_i) \cdot [\mathbb{Q}(\tau \le t_i) - \mathbb{Q}(\tau \le t_{i-1})] \cdot D(t_i)
$$

where $D(t)$ is the discount factor and $\mathbb{Q}(\tau \le t)$ is the default probability.

---

## Monte Carlo Simulation of Exposure

### Algorithm

1. **Simulate market scenarios:** Generate $N$ paths of risk factors $(S_t^{(j)})_{j=1}^N$
2. **Revalue portfolio:** For each path and time point, compute $V_t^{(j)}$
3. **Compute exposure:** $E_t^{(j)} = \max(V_t^{(j)}, 0)$
4. **Aggregate statistics:**
   - $\widehat{\text{EE}}(t) = \frac{1}{N} \sum_{j=1}^N E_t^{(j)}$
   - $\widehat{\text{PFE}}_\alpha(t) = $ empirical $\alpha$-quantile of $(E_t^{(j)})$

### Implementation Considerations

- **Time grid:** Balance accuracy vs. computation
- **Path count:** Typically $N = 1000$ to $10000$
- **Variance reduction:** Antithetic variates, control variates
- **Netting:** Apply at portfolio level, not trade level

---

## Peak Exposure

**Peak Exposure** is the maximum exposure over the portfolio's life:

$$
\text{Peak EE} = \max_{t \in [0,T]} \text{EE}(t)
$$

$$
\text{Peak PFE}_\alpha = \max_{t \in [0,T]} \text{PFE}_\alpha(t)
$$

Peak exposure is used for:
- Credit limit setting
- Counterparty approval
- Stress testing

---

## Key Takeaways

- Exposure is the positive part of portfolio value: $E_t = V_t^+$
- EE is expected exposure; PFE is tail exposure
- EPE (time-averaged EE) summarizes lifetime exposure
- Netting significantly reduces exposure for diversified portfolios
- Collateral reduces exposure but introduces MPOR considerations
- Exposure profiles are essential inputs to CVA calculations
- Monte Carlo simulation is the standard computation method

---

## Further Reading

- Gregory, J., *Counterparty Credit Risk and Credit Value Adjustment*
- Brigo, D., Morini, M., & Pallavicini, A., *Counterparty Credit Risk, Collateral and Funding*
- Pykhtin, M. & Zhu, S. (2007), "A Guide to Modeling Counterparty Credit Risk"
- Basel Committee, "The Standardised Approach for Measuring Counterparty Credit Risk Exposures"
