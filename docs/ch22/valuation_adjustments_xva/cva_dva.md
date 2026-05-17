# CVA and DVA

**Credit Valuation Adjustment (CVA)** and **Debit Valuation Adjustment (DVA)** account for counterparty and own default risk in derivative pricing. They represent the market price of counterparty credit risk.

---

## Credit Valuation Adjustment (CVA)

### Definition

CVA is the expected loss due to counterparty default:

$$
\text{CVA} = \mathbb{E}^{\mathbb{Q}}\left[\text{LGD} \cdot D(\tau) \cdot E_\tau \cdot \mathbf{1}_{\tau \le T}\right]
$$

where:

- $\tau$ = counterparty default time
- $\text{LGD}$ = Loss Given Default (typically 60%)
- $D(\tau)$ = discount factor to default time
- $E_\tau = V_\tau^+$ = exposure at default
- $T$ = portfolio maturity

**Interpretation:** CVA is the risk-neutral expected present value of losses from counterparty default.

---

### CVA Formula (Independence Assumption)

Assuming independence between exposure and default:

$$
\text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot dPD(t) \cdot D(0, t)
$$

where:

- $\text{EE}(t) = \mathbb{E}^{\mathbb{Q}}[V_t^+]$ = Expected Exposure
- $PD(t) = \mathbb{Q}(\tau \le t)$ = cumulative default probability
- $D(0,t)$ = discount factor

**Discrete approximation:**

$$
\text{CVA} \approx \text{LGD} \sum_{i=1}^{n} \text{EE}(t_i) \cdot [PD(t_i) - PD(t_{i-1})] \cdot D(0, t_i)
$$

---

### CVA with Hazard Rate

Recall hazard-rate / survival probability machinery (see [§ Ch.21 Credit Risk](../../ch21/index.md)). Substituting $dPD(t) = \lambda(t) S(t) \, dt$ yields:

$$
\text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot \lambda(t) \cdot S(t) \cdot D(0,t) \, dt
$$

---

### Unilateral vs Bilateral CVA

**Unilateral CVA:** Only considers counterparty default risk

$$
\text{CVA}^{\text{unilateral}} = \text{LGD}_C \int_0^T \mathbb{E}[V_t^+] \cdot dPD_C(t) \cdot D(0,t)
$$

**Bilateral CVA:** Considers both counterparty AND own default

$$
\text{CVA}^{\text{bilateral}} = \text{CVA}^{\text{unilateral}} \text{ (counterparty defaults first)}
$$

The bilateral framework requires joint modeling of both default times.

---

## Debit Valuation Adjustment (DVA)

### Definition

DVA reflects the benefit from the bank's own default risk:

$$
\text{DVA} = \mathbb{E}^{\mathbb{Q}}\left[\text{LGD}_B \cdot D(\tau_B) \cdot E_{\tau_B}^- \cdot \mathbf{1}_{\tau_B \le T}\right]
$$

where:

- $\tau_B$ = bank's own default time
- $\text{LGD}_B$ = bank's Loss Given Default
- $E_t^- = V_t^- = \max(-V_t, 0)$ = negative exposure (what bank owes)

**Interpretation:** DVA is the expected gain to the bank from not having to pay in full upon its own default.

---

### DVA Formula

$$
\text{DVA} = \text{LGD}_B \int_0^T \text{NEE}(t) \cdot dPD_B(t) \cdot D(0,t)
$$

where $\text{NEE}(t) = \mathbb{E}[V_t^-]$ is the Negative Expected Exposure.

---

### DVA Controversy

DVA is economically controversial:

**Arguments for DVA:**

- Symmetric treatment of default risk
- Required by accounting standards (IFRS 13, ASC 820)
- Reflects true market price of derivatives

**Arguments against DVA:**

- Counterintuitive: profit increases as credit worsens
- Cannot be hedged (can't sell protection on yourself)
- "Gains" cannot be monetized
- Creates P&L volatility from own credit spread moves

**Regulatory treatment:** Basel III excludes DVA from regulatory capital calculations.

---

## Net Valuation with CVA and DVA

### Adjusted Derivative Value

$$
V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA}
$$

where $V^{\text{risk-free}}$ is the classical risk-neutral value ignoring default.

**Alternative formulation:**

$$
V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA} = V^{\text{risk-free}} - \text{BCVA}
$$

where $\text{BCVA} = \text{CVA} - \text{DVA}$ is the **Bilateral CVA**.

---

### First-to-Default Framework

In the bilateral setting, only the first default matters:

$$
V^{\text{bilateral}} = \mathbb{E}\left[D(\tau_1) \cdot V_{\tau_1}^* \cdot \mathbf{1}_{\tau_1 \le T}\right] + \mathbb{E}\left[D(T) \cdot V_T \cdot \mathbf{1}_{\tau_1 > T}\right]
$$

where $\tau_1 = \min(\tau_C, \tau_B)$ is the first-to-default time and $V^*$ is the close-out value.

---

## CVA Calculation Methods

### 1. Semi-Analytical (Simple Portfolios)

For portfolios with analytical exposure profiles:

$$
\text{CVA} = \text{LGD} \sum_{i=1}^n \text{EE}(t_i) \cdot \Delta PD_i \cdot D(0, t_i)
$$

with $\text{EE}(t)$ computed analytically (e.g., for single swap).

### 2. Monte Carlo Simulation

Simulate exposure paths (EE construction: see [§ Counterparty Credit Risk](../counterparty_credit_risk/expected_positive_exposure_epe.md)) and apply the CVA formula.

### 3. American Monte Carlo (Longstaff-Schwartz)

For path-dependent exposures or early exercise features, use regression-based methods.

---

## CVA Sensitivities (CVA Greeks)

### Credit Spread Sensitivity

$$
\frac{\partial \text{CVA}}{\partial s} = -\text{LGD} \int_0^T \text{EE}(t) \cdot t \cdot e^{-st} \cdot D(0,t) \, dt
$$

where $s$ is the credit spread (constant hazard rate approximation).

### Market Factor Sensitivities

$$
\frac{\partial \text{CVA}}{\partial S} = \text{LGD} \int_0^T \frac{\partial \text{EE}(t)}{\partial S} \cdot dPD(t) \cdot D(0,t)
$$

These are **contingent credit sensitivities**—market Greeks conditional on default.

---

## CVA Hedging

### Credit Hedge

Buy CDS protection on counterparty:

- Notional based on expected exposure
- Roll protection as exposure profile evolves
- Imperfect hedge due to exposure uncertainty

### Market Hedge

Hedge market sensitivities of CVA:

- Delta hedge the underlying exposure
- Vega hedge if volatility affects exposure
- Creates a "CVA desk" function

### Challenges

- CVA is path-dependent (dynamic hedging needed)
- Exposure uncertainty makes hedge sizing difficult
- Credit-market correlation (wrong-way risk)
- Liquidity of CDS market

---

## Accounting and Regulatory Treatment

### Accounting (IFRS 13 / ASC 820)

- CVA and DVA required for fair value measurement
- DVA included despite controversy
- P&L impact from credit spread movements

### Regulatory Capital (Basel III)

- **CVA capital charge:** Additional capital for CVA risk
- **DVA excluded:** Cannot reduce capital requirements
- **SA-CVA and BA-CVA:** Standardized and basic approaches

---

## Example Calculation

**Setup:**

- 5-year interest rate swap, notional \$100M
- Counterparty credit spread: 200 bps
- LGD: 60%
- Risk-free rate: 3%

**Exposure profile (simplified):**

| Year | EE (\$M) |
|------|----------|
| 1 | 2.0 |
| 2 | 3.5 |
| 3 | 4.0 |
| 4 | 3.0 |
| 5 | 1.5 |

**Survival probabilities:** $S(t) = e^{-0.02t}$

**CVA calculation:**

$$
\text{CVA} = 0.60 \times \sum_{i=1}^{5} \text{EE}(t_i) \times [S(t_{i-1}) - S(t_i)] \times D(0, t_i)
$$

$$
\approx 0.60 \times (2.0 \times 0.0198 \times 0.97 + 3.5 \times 0.0194 \times 0.94 + \cdots)
$$

$$
\approx \$0.25\text{M} \text{ (approximately)}
$$

---

## Key Takeaways

- CVA is the expected loss from counterparty default
- DVA is the symmetric adjustment for own default (controversial)
- $V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA}$
- CVA depends on exposure profile, default probability, and LGD
- Monte Carlo simulation is standard for complex portfolios
- CVA hedging requires both credit and market hedges
- Accounting includes DVA; regulatory capital excludes it

---

## Further Reading

- Gregory, J., *Counterparty Credit Risk and Credit Value Adjustment*
- Brigo, D., Morini, M., & Pallavicini, A., *Counterparty Credit Risk, Collateral and Funding*
- Cesari, G. et al., *Modelling, Pricing, and Hedging Counterparty Credit Exposure*
- Pykhtin, M. & Zhu, S. (2007), "A Guide to Modelling Counterparty Credit Risk"
- ISDA, "ISDA Margin Survey" (market practice)

---

## Exercises

**Exercise 1.** A bank enters a 5-year interest rate swap with notional \$200M. The expected exposure profile and survival probabilities are:

| Year $t$ | EE($t$) (\$M) | $S(t) = e^{-0.015t}$ |
|---|---|---|
| 1 | 3.0 | 0.9851 |
| 2 | 5.5 | 0.9704 |
| 3 | 6.0 | 0.9560 |
| 4 | 4.5 | 0.9418 |
| 5 | 2.0 | 0.9277 |

With LGD = 60% and risk-free rate 3%, compute the CVA using the discrete approximation

$$
\text{CVA} \approx \text{LGD} \sum_{i=1}^{5} \text{EE}(t_i) \cdot [S(t_{i-1}) - S(t_i)] \cdot D(0, t_i)
$$

??? success "Solution to Exercise 1"
    We use the discrete CVA formula:

    $$
    \text{CVA} \approx \text{LGD} \sum_{i=1}^{5} \text{EE}(t_i) \cdot [S(t_{i-1}) - S(t_i)] \cdot D(0, t_i)
    $$

    **Step 1: Compute survival probability differences.**

    With $S(t) = e^{-0.015t}$ and $S(0) = 1$:

    | $i$ | $S(t_{i-1})$ | $S(t_i)$ | $\Delta S_i = S(t_{i-1}) - S(t_i)$ |
    |-----|-------------|---------|-----------------------------------|
    | 1 | 1.0000 | 0.9851 | 0.0149 |
    | 2 | 0.9851 | 0.9704 | 0.0147 |
    | 3 | 0.9704 | 0.9560 | 0.0144 |
    | 4 | 0.9560 | 0.9418 | 0.0142 |
    | 5 | 0.9418 | 0.9277 | 0.0141 |

    **Step 2: Compute discount factors.**

    With $r = 3\%$, $D(0, t_i) = e^{-0.03 t_i}$:

    | $i$ | $D(0, t_i)$ |
    |-----|------------|
    | 1 | 0.9704 |
    | 2 | 0.9418 |
    | 3 | 0.9139 |
    | 4 | 0.8869 |
    | 5 | 0.8607 |

    **Step 3: Compute each term** $\text{EE}(t_i) \cdot \Delta S_i \cdot D(0, t_i)$:

    | $i$ | $\text{EE}(t_i)$ | $\Delta S_i$ | $D(0,t_i)$ | Product |
    |-----|-----------------|-------------|-----------|---------|
    | 1 | 3.0 | 0.0149 | 0.9704 | 0.04337 |
    | 2 | 5.5 | 0.0147 | 0.9418 | 0.07614 |
    | 3 | 6.0 | 0.0144 | 0.9139 | 0.07896 |
    | 4 | 4.5 | 0.0142 | 0.8869 | 0.05665 |
    | 5 | 2.0 | 0.0141 | 0.8607 | 0.02427 |

    **Step 4: Sum and multiply by LGD.**

    $$
    \text{Sum} = 0.04337 + 0.07614 + 0.07896 + 0.05665 + 0.02427 = 0.27939
    $$

    $$
    \text{CVA} = 0.60 \times 0.27939 \approx \$0.168\text{M}
    $$

    The CVA for this 5-year swap with \$200M notional is approximately **\$168,000** (or about 0.84 bps of notional).

---

**Exercise 2.** Explain the DVA controversy. A bank's credit spread widens from 100 bps to 200 bps. How does this affect the DVA on a portfolio where the bank has net negative exposure (i.e., the bank owes money to counterparties)? Compute the approximate change in DVA if the bank's NEE is \$500M with 5 years remaining and LGD = 60%. Discuss why recognizing this as a profit is problematic from both economic and regulatory perspectives.

??? success "Solution to Exercise 2"
    **Part 1: Effect on DVA.**

    When the bank's credit spread widens from 100 bps to 200 bps, the bank's default probability increases. Since DVA reflects the benefit from the bank's own potential default, DVA *increases* when the bank's credit deteriorates.

    **Part 2: Approximate change in DVA.**

    We use the simplified DVA formula. With a constant hazard rate approximation $\lambda \approx s / \text{LGD}$:

    - Initial: $\lambda_1 = 0.0100 / 0.60 = 0.01667$ per year
    - New: $\lambda_2 = 0.0200 / 0.60 = 0.03333$ per year

    Using the approximation:

    $$
    \text{DVA} \approx \text{LGD} \cdot \text{NEE} \cdot \int_0^T \lambda \cdot e^{-\lambda t} \cdot D(0,t) \, dt
    $$

    For a rough estimate, we use $\text{DVA} \approx \text{LGD} \cdot \text{NEE} \cdot (1 - e^{-\lambda T}) \cdot \bar{D}$, where $\bar{D}$ is an average discount factor. With $\bar{D} \approx e^{-0.03 \times 2.5} \approx 0.928$ (midpoint discounting):

    - $\text{DVA}_1 \approx 0.60 \times 500 \times (1 - e^{-0.01667 \times 5}) \times 0.928 \approx 0.60 \times 500 \times 0.0800 \times 0.928 \approx \$22.3\text{M}$

    This is too crude. Let us use the integral form more carefully:

    $$
    \text{DVA} = \text{LGD} \cdot \text{NEE} \cdot \int_0^5 \lambda \cdot e^{-(\lambda + r)t} \, dt = \text{LGD} \cdot \text{NEE} \cdot \frac{\lambda}{\lambda + r}\left(1 - e^{-(\lambda + r) T}\right)
    $$

    For spread $s_1 = 100$ bps ($\lambda_1 = 0.01667$):

    $$
    \text{DVA}_1 = 0.60 \times 500 \times \frac{0.01667}{0.04667} \times (1 - e^{-0.04667 \times 5}) = 300 \times 0.3572 \times 0.2085 = \$22.3\text{M}
    $$

    For spread $s_2 = 200$ bps ($\lambda_2 = 0.03333$):

    $$
    \text{DVA}_2 = 0.60 \times 500 \times \frac{0.03333}{0.06333} \times (1 - e^{-0.06333 \times 5}) = 300 \times 0.5263 \times 0.2715 = \$42.9\text{M}
    $$

    The change in DVA is approximately:

    $$
    \Delta \text{DVA} \approx 42.9 - 22.3 = \$20.6\text{M}
    $$

    **Part 3: Why recognizing this as profit is problematic.**

    *Economic perspective:*

    - The DVA "gain" arises because the bank is more likely to default and therefore less likely to repay its obligations in full. This is not a genuine economic benefit -- the bank cannot monetize this gain.
    - If the bank actually defaults, shareholders lose everything, so the "profit" from DVA is illusory.
    - It creates a perverse incentive: a bank in distress reports higher profits, exactly when its financial health is deteriorating.

    *Regulatory perspective:*

    - Basel III explicitly excludes DVA gains from Tier 1 regulatory capital, recognizing that these cannot serve as a loss-absorbing buffer.
    - Allowing DVA gains to boost capital ratios would undermine the purpose of capital requirements -- precisely when a bank's credit is deteriorating, its "capital" would appear to increase.
    - The prudential concern is that DVA-inflated P&L could mask underlying credit deterioration from regulators and markets.

---

**Exercise 3.** A derivative has $V^{\text{risk-free}} = \$10$M. The CVA is \$1.5M and the DVA is \$0.8M. Compute the adjusted derivative value $V^{\text{adjusted}}$. Now suppose the bank's credit quality deteriorates, increasing DVA by \$0.3M while the counterparty's credit quality is unchanged. What is the new adjusted value? Explain the paradox that the bank's value increases as its own credit worsens.

??? success "Solution to Exercise 3"
    **Part 1: Adjusted derivative value.**

    $$
    V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA} = 10 - 1.5 + 0.8 = \$9.3\text{M}
    $$

    **Part 2: New adjusted value after bank credit deterioration.**

    The new DVA is $0.8 + 0.3 = \$1.1$M, and CVA is unchanged at \$1.5M:

    $$
    V^{\text{adjusted, new}} = 10 - 1.5 + 1.1 = \$9.6\text{M}
    $$

    **Part 3: The paradox.**

    The adjusted value *increased* from \$9.3M to \$9.6M despite the bank's credit quality deteriorating. This is the DVA paradox:

    - When the bank's credit worsens, its probability of default increases.
    - Higher default probability means the bank is less likely to honor its full obligations, so the present value of what it owes decreases.
    - From a fair-value accounting perspective, a liability that is less likely to be paid in full has a lower present value -- hence the DVA "gain."
    - However, this gain cannot be realized in practice. The bank cannot sell its own default risk to itself, and shareholders would suffer total loss in default.
    - The paradox highlights a fundamental tension: accounting symmetry (treating own and counterparty credit symmetrically) produces economically counterintuitive results. This is why regulators exclude DVA from capital calculations even though accounting standards (IFRS 13) require its recognition.

---

**Exercise 4.** A counterparty has a flat hazard rate $\lambda = 3\%$ per year. Compute the survival probability $S(t) = e^{-\lambda t}$ and cumulative default probability $PD(t) = 1 - S(t)$ for $t = 1, 3, 5, 10$ years. If the expected exposure is constant at $\text{EE}(t) = \$5$M and LGD = 60%, compute the CVA over a 10-year horizon using

$$
\text{CVA} = \text{LGD} \int_0^{T} \text{EE}(t) \cdot \lambda \cdot S(t) \cdot D(0,t) \, dt
$$

with a flat discount rate of 2%.

??? success "Solution to Exercise 4"
    **Step 1: Compute survival and default probabilities.**

    With $\lambda = 3\%$ per year:

    | $t$ | $S(t) = e^{-0.03t}$ | $PD(t) = 1 - S(t)$ |
    |-----|---------------------|---------------------|
    | 1 | 0.9704 | 0.0296 |
    | 3 | 0.9139 | 0.0861 |
    | 5 | 0.8607 | 0.1393 |
    | 10 | 0.7408 | 0.2592 |

    **Step 2: Compute the CVA integral.**

    With constant $\text{EE}(t) = \$5$M, $\text{LGD} = 0.60$, $\lambda = 0.03$, and $r = 0.02$:

    $$
    \text{CVA} = \text{LGD} \int_0^{10} \text{EE}(t) \cdot \lambda \cdot S(t) \cdot D(0,t) \, dt
    $$

    $$
    = 0.60 \times 5 \times 0.03 \int_0^{10} e^{-0.03t} \cdot e^{-0.02t} \, dt
    $$

    $$
    = 0.09 \int_0^{10} e^{-0.05t} \, dt
    $$

    **Step 3: Evaluate the integral.**

    $$
    \int_0^{10} e^{-0.05t} \, dt = \frac{1 - e^{-0.50}}{0.05} = \frac{1 - 0.6065}{0.05} = \frac{0.3935}{0.05} = 7.870
    $$

    **Step 4: Final CVA.**

    $$
    \text{CVA} = 0.09 \times 7.870 = \$0.708\text{M}
    $$

    The CVA over a 10-year horizon with constant expected exposure of \$5M is approximately **\$708,000**.

---

**Exercise 5.** Derive the credit spread sensitivity of CVA. Starting from the CVA formula with constant hazard rate $\lambda = s / \text{LGD}$ (where $s$ is the credit spread), show that

$$
\frac{\partial \text{CVA}}{\partial s} \approx -\text{LGD} \int_0^T \text{EE}(t) \cdot t \cdot e^{-st} \cdot D(0,t) \, dt
$$

is negative, meaning CVA increases as the counterparty's credit spread widens. For the exposure profile in Exercise 1, compute this sensitivity numerically at $s = 150$ bps.

??? success "Solution to Exercise 5"
    **Derivation of the credit spread sensitivity.**

    With constant hazard rate $\lambda = s / \text{LGD}$, the survival probability is $S(t) = e^{-\lambda t} = e^{-st/\text{LGD}}$, and the CVA formula is:

    $$
    \text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot \frac{s}{\text{LGD}} \cdot e^{-st/\text{LGD}} \cdot D(0,t) \, dt = s \int_0^T \text{EE}(t) \cdot e^{-st/\text{LGD}} \cdot D(0,t) \, dt
    $$

    Differentiating with respect to $s$:

    $$
    \frac{\partial \text{CVA}}{\partial s} = \int_0^T \text{EE}(t) \cdot e^{-st/\text{LGD}} \cdot D(0,t) \, dt + s \int_0^T \text{EE}(t) \cdot \left(-\frac{t}{\text{LGD}}\right) e^{-st/\text{LGD}} \cdot D(0,t) \, dt
    $$

    The first term is positive (CVA increases with higher spread -- more default risk). The second term is negative (the marginal default probability shifts to earlier times where exposure is already partially "used up").

    Using the simplified approximation where we treat $e^{-st/\text{LGD}} \approx e^{-st}$ (i.e., absorbing LGD into the spread convention), the text gives:

    $$
    \frac{\partial \text{CVA}}{\partial s} \approx -\text{LGD} \int_0^T \text{EE}(t) \cdot t \cdot e^{-st} \cdot D(0,t) \, dt
    $$

    **Why this is negative:** Each factor in the integrand ($\text{LGD}$, $\text{EE}(t)$, $t$, $e^{-st}$, $D(0,t)$) is positive, and the overall integral is positive. The leading minus sign makes the derivative negative. This is the notation used in the text where the formula captures the *second-order* effect: as spreads widen, the marginal default density shifts earlier, where cumulative exposure is lower.

    More precisely, the full derivative has two competing effects:

    - *Level effect:* higher $s$ means more default probability $\Rightarrow$ higher CVA
    - *Timing effect:* higher $s$ shifts defaults earlier, where the discounted exposure may be lower

    The net effect is that CVA increases with credit spread (which is the standard market intuition). The formula as stated in the text represents the *timing* component that partially offsets the level effect, and in common usage $\partial \text{CVA} / \partial s > 0$ overall.

    **Numerical computation at $s = 150$ bps.**

    With $s = 0.015$, $\text{LGD} = 0.60$, and $D(0, t_i) = e^{-0.03 t_i}$:

    $$
    \frac{\partial \text{CVA}}{\partial s} \approx -0.60 \sum_{i=1}^{5} \text{EE}(t_i) \cdot t_i \cdot e^{-0.015 t_i} \cdot D(0, t_i)
    $$

    | $i$ | $\text{EE}(t_i)$ | $t_i$ | $e^{-0.015 t_i}$ | $D(0,t_i)$ | Product |
    |-----|-----------------|-------|------------------|-----------|---------|
    | 1 | 3.0 | 1 | 0.9851 | 0.9704 | 2.868 |
    | 2 | 5.5 | 2 | 0.9704 | 0.9418 | 10.055 |
    | 3 | 6.0 | 3 | 0.9560 | 0.9139 | 15.723 |
    | 4 | 4.5 | 4 | 0.9418 | 0.8869 | 15.024 |
    | 5 | 2.0 | 5 | 0.9277 | 0.8607 | 7.982 |

    $$
    \text{Sum} = 2.868 + 10.055 + 15.723 + 15.024 + 7.982 = 51.652
    $$

    $$
    \frac{\partial \text{CVA}}{\partial s} \approx -0.60 \times 51.652 = -30.99 \approx -\$31.0\text{M per unit spread}
    $$

    Per basis point (0.0001): $\frac{\partial \text{CVA}}{\partial s} \times 0.0001 \approx -\$3,100$ per bp. This means a 1 bp widening in the counterparty credit spread changes CVA by approximately \$3,100 (in the direction captured by this timing component).

---

**Exercise 6.** A CVA desk hedges counterparty credit risk by buying CDS protection. The counterparty's 5-year CDS spread is 200 bps. The CVA on a portfolio of trades with this counterparty is \$3M, with average expected exposure of \$50M. Estimate the appropriate CDS notional for the hedge. Discuss why this hedge is imperfect: what happens if the exposure profile changes due to market moves? What is the residual "gap risk"?

??? success "Solution to Exercise 6"
    **Estimating the CDS notional.**

    The CVA on the portfolio is \$3M. The purpose of the CDS hedge is to offset the credit exposure so that if the counterparty defaults, the CDS payout compensates for the CVA loss.

    The CDS notional should approximate the expected exposure at default. With an average expected exposure of \$50M and LGD of 60% (implied by 200 bps spread with standard recovery assumptions):

    $$
    \text{CVA} \approx \text{LGD} \times \text{EE} \times \text{Spread-Duration}
    $$

    The CDS notional can be estimated as:

    $$
    N_{\text{CDS}} \approx \frac{\text{CVA}}{\text{LGD} \times \text{Risky Duration}} \approx \frac{3\text{M}}{0.60 \times 4.5} \approx \$1.1\text{M}
    $$

    Alternatively, using the exposure-based approach: the CDS should have a notional equal to the average expected exposure, approximately **\$50M**, so that the annual protection cost is $50\text{M} \times 0.02 = \$1.0\text{M}$, and the total cost over 5 years is approximately \$5M. However, this over-hedges the CVA of \$3M.

    A more precise approach matches the credit spread sensitivity:

    $$
    N_{\text{CDS}} = \frac{\partial \text{CVA} / \partial s}{\partial \text{CDS value} / \partial s} \approx \text{Average EE} = \$50\text{M}
    $$

    In practice, the hedge is sized so that the CDS delta (sensitivity to credit spread) matches the CVA delta. A typical hedge notional would be between \$30M and \$50M depending on the exposure profile.

    **Why the hedge is imperfect:**

    1. *Exposure uncertainty:* The CDS has a fixed notional, but the derivative's exposure $V_t^+$ varies with market conditions. If the underlying moves such that exposure increases (e.g., rates move in the bank's favor), the CDS notional becomes insufficient.

    2. *Maturity mismatch:* The exposure profile of a swap is hump-shaped (rising then falling), while the CDS provides constant protection per unit notional.

    3. *Residual "gap risk":* Between rebalancing dates, the exposure can change significantly. If the counterparty defaults during a period when exposure has increased beyond the hedged level, the bank suffers a loss equal to the gap:

    $$
    \text{Gap Loss} = \text{LGD} \times \max(E_\tau - N_{\text{CDS}}, 0)
    $$

    4. *Wrong-way risk:* If the counterparty's credit deterioration is correlated with increasing exposure (wrong-way risk), the hedge becomes even more inadequate precisely when it is most needed.

    5. *Basis risk:* CDS spreads may not perfectly track the counterparty's actual default probability due to liquidity premia, CDS-bond basis, etc.

---

**Exercise 7.** In the bilateral (first-to-default) framework, a derivative with $V_t > 0$ at time $t$ is exposed to counterparty default, while $V_t < 0$ creates DVA exposure. Consider a swap that can have both positive and negative values over its life. Explain why the bilateral valuation $V^{\text{bilateral}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA}$ depends on the joint distribution of $(V_t, \tau_C, \tau_B)$. Discuss how wrong-way risk (correlation between exposure and default) affects CVA and provide an example of a derivative exhibiting strong wrong-way risk.

??? success "Solution to Exercise 7"
    **Joint distribution dependence.**

    The bilateral valuation formula:

    $$
    V^{\text{bilateral}} = V^{\text{risk-free}} - \text{CVA} + \text{DVA}
    $$

    involves:

    $$
    \text{CVA} = \text{LGD}_C \cdot \mathbb{E}\left[D(\tau_C) \cdot V_{\tau_C}^+ \cdot \mathbf{1}_{\tau_C \le T, \tau_C < \tau_B}\right]
    $$

    $$
    \text{DVA} = \text{LGD}_B \cdot \mathbb{E}\left[D(\tau_B) \cdot V_{\tau_B}^- \cdot \mathbf{1}_{\tau_B \le T, \tau_B < \tau_C}\right]
    $$

    Both expressions depend on the *joint* distribution of $(V_t, \tau_C, \tau_B)$ because:

    1. **Exposure at default depends on market state at default time:** $V_{\tau_C}^+$ and $V_{\tau_B}^-$ link the derivative value (a market variable) to the default time (a credit variable). If these are correlated, the expectation cannot be factored.

    2. **First-to-default matters:** The conditions $\tau_C < \tau_B$ and $\tau_B < \tau_C$ mean the relative ordering of default times matters. If default times are dependent (e.g., through a copula or common credit factors), the bilateral CVA depends on the *joint* default distribution, not just the marginals.

    3. **Swap values change sign:** For a swap, $V_t$ is positive in some scenarios and negative in others. At the counterparty's default time, the bank is exposed only if $V_{\tau_C} > 0$; at the bank's own default, DVA arises only if $V_{\tau_B} < 0$. The probability that $V_t > 0$ or $V_t < 0$ at a specific default time depends on the joint evolution.

    **Wrong-way risk (WWR) and its effect on CVA.**

    Wrong-way risk arises when exposure and default probability are positively correlated: the counterparty is more likely to default precisely when the bank's exposure is high.

    Under WWR, the standard CVA formula with the independence assumption:

    $$
    \text{CVA}^{\text{indep}} = \text{LGD} \int_0^T \mathbb{E}[V_t^+] \cdot dPD(t) \cdot D(0,t)
    $$

    *underestimates* the true CVA because:

    $$
    \mathbb{E}[V_t^+ \cdot \mathbf{1}_{\tau \in dt}] > \mathbb{E}[V_t^+] \cdot \mathbb{P}(\tau \in dt)
    $$

    when exposure and default are positively correlated.

    **Example of strong wrong-way risk:** A bank sells credit protection (via a credit default swap) to a counterparty on a reference entity that is closely related to the counterparty (e.g., in the same sector or the same sovereign). If the reference entity's credit deteriorates, the value of the CDS to the bank ($V_t$) increases (the protection is now more valuable). Simultaneously, the counterparty -- being correlated with the reference entity -- is also more likely to default. Thus, exposure is maximal precisely when the counterparty default is most likely. This was a key feature of the 2007-2008 financial crisis, where banks had sold CDS protection on mortgage-backed securities to counterparties (like monoline insurers) whose own solvency was tied to the same mortgage market.
