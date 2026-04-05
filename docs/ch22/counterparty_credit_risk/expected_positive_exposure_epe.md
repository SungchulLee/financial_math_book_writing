# Expected Positive Exposure (EPE)

**Expected Positive Exposure (EPE)** distills the entire time-varying exposure profile of a derivative portfolio into a single summary statistic. It serves as the primary input to CVA calculations and, through the regulatory alpha multiplier, determines the **Exposure at Default (EAD)** for counterparty credit risk capital.

---

## Exposure Fundamentals

Recall that for a derivative portfolio with value process $V_t$, the **exposure** at time $t$ is the one-sided quantity:

$$
E_t = V_t^+ = \max(V_t, 0)
$$

Only positive values create credit risk: if the counterparty defaults when $V_t > 0$, the surviving party loses the positive mark-to-market.

---

## Expected Exposure

The **Expected Exposure** at time $t$ is:

$$
\text{EE}(t) = \mathbb{E}^{\mathbb{Q}}[E_t] = \mathbb{E}^{\mathbb{Q}}[V_t^+]
$$

where the expectation is under the risk-neutral measure $\mathbb{Q}$. EE is a deterministic function of time that summarizes the average exposure at each point in the portfolio's life.

**Properties of EE:**

- $\text{EE}(t) \ge 0$ for all $t$ (exposures are non-negative)
- $\text{EE}(0) = V_0^+$ (known initial exposure)
- The shape of $\text{EE}(t)$ depends on product type, market dynamics, and portfolio composition

---

## EPE Definition

!!! info "Definition"
    The **Expected Positive Exposure** is the time-weighted average of expected exposure over the portfolio horizon $[0, T]$:

    $$
    \text{EPE} = \frac{1}{T} \int_0^T \text{EE}(t) \, dt
    $$

In practice, with discrete time points $0 = t_0 < t_1 < \cdots < t_n = T$:

$$
\text{EPE} \approx \frac{1}{T} \sum_{i=1}^{n} \text{EE}(t_i) \cdot (t_i - t_{i-1})
$$

or, for equally spaced points with $\Delta t = T/n$:

$$
\text{EPE} \approx \frac{1}{n} \sum_{i=1}^{n} \text{EE}(t_i)
$$

**Interpretation:** EPE reduces the full time profile $\text{EE}(\cdot)$ to a single number representing the average level of expected credit exposure over the trade's lifetime.

---

## Effective EE and Effective EPE

### Motivation

The standard EE profile can be manipulated by structuring trades with artificially low exposure at measurement dates while maintaining high exposure in between. To prevent this gaming, regulators require **non-decreasing** versions.

### Effective Expected Exposure

$$
\text{Effective EE}(t) = \max_{s \le t} \text{EE}(s)
$$

This is the running maximum of EE, ensuring that exposure cannot decrease. If a trade amortizes and then new risk emerges, Effective EE captures the earlier peak.

### Effective EPE

$$
\text{Effective EPE} = \frac{1}{\min(1 \text{ year}, T)} \int_0^{\min(1 \text{ year}, T)} \text{Effective EE}(t) \, dt
$$

**Key regulatory features:**

- The averaging horizon is capped at one year (even for longer-dated trades)
- The non-decreasing EE function prevents manipulation
- Effective EPE $\ge$ EPE always, providing a conservative measure

---

## Potential Future Exposure (PFE)

While EPE captures the average exposure, **Potential Future Exposure** captures the tail:

$$
\text{PFE}_\alpha(t) = \inf\{x : \mathbb{P}(E_t \le x) \ge \alpha\} = F_{E_t}^{-1}(\alpha)
$$

typically at $\alpha = 0.95$ or $0.99$.

**Relationship between EE and PFE:**

- $\text{PFE}_\alpha(t) \ge \text{EE}(t)$ for all $\alpha > 0.5$
- The ratio $\text{PFE}_\alpha(t) / \text{EE}(t)$ is typically 2--4$\times$, depending on the distributional shape
- PFE is used for **credit limit setting** (peak PFE $= \max_t \text{PFE}_\alpha(t)$)
- EE is used for **CVA and capital** calculations

**Non-additivity of PFE:** Unlike EE, PFE is generally not additive across portfolios:

$$
\text{PFE}_\alpha(A + B) \le \text{PFE}_\alpha(A) + \text{PFE}_\alpha(B)
$$

This subadditivity reflects the diversification benefit from netting.

---

## Product-Specific Exposure Profiles

### Interest Rate Swap

For a receiver swap (receive fixed, pay floating) with notional $N$ and maturity $T$:

$$
\text{EE}(t) \approx N \cdot \sigma_{\text{swap}} \cdot \sqrt{t} \cdot (T - t) / T
$$

The profile exhibits a **hump shape**, peaking near $t \approx T/2$:

- Early in life: small diffusion $(\sqrt{t}$ small)
- Late in life: pull-to-par ($T - t$ small)
- Peak: the trade-off between growing uncertainty and shrinking remaining cash flows

### FX Forward

For an FX forward with maturity $T$:

$$
\text{EE}(t) \approx N \cdot \sigma_{\text{FX}} \cdot \sqrt{t}
$$

Exposure grows monotonically, reaching its maximum at maturity. There are no intermediate payments to reset exposure.

### Cross-Currency Swap

Combines IRS and FX profiles, with a large exposure spike at maturity due to notional exchange. The profile resembles the IRS hump shape with an added notional exchange jump.

### Options

- **Option buyer:** Exposure equals option value (always non-negative after premium paid)
- **Option seller:** Zero exposure (negative value to seller)
- Exposure decays with time as option loses time value

---

## EPE and CVA

The **Credit Valuation Adjustment** depends directly on the exposure profile:

$$
\text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot \lambda(t) \cdot S(t) \cdot D(0, t) \, dt
$$

where $\lambda(t)$ is the default intensity, $S(t) = e^{-\int_0^t \lambda(s) \, ds}$ is the survival probability, and $D(0, t)$ is the discount factor.

Under the approximation of constant default intensity $\lambda$ and flat term structure with rate $r$:

$$
\text{CVA} \approx \text{LGD} \cdot \lambda \cdot \int_0^T \text{EE}(t) \cdot e^{-(\lambda + r)t} \, dt
$$

For short-maturity trades where the discount and survival factors are approximately 1:

$$
\text{CVA} \approx \text{LGD} \cdot \lambda \cdot T \cdot \text{EPE}
$$

This shows the direct connection: **CVA is approximately proportional to EPE**.

---

## EAD and the Alpha Multiplier

### Regulatory Exposure at Default

Under the Basel Internal Model Method (IMM), the **Exposure at Default** is:

$$
\text{EAD} = \alpha \cdot \text{Effective EPE}
$$

where $\alpha \ge 1.4$ is the **alpha multiplier** (with a regulatory floor of 1.4).

### Derivation of the Alpha Multiplier

The alpha multiplier accounts for the difference between expected exposure (used in EPE) and the exposure conditional on default. Define:

$$
\alpha = \frac{\text{CVA}_{\text{full}}}{\text{CVA}_{\text{indep}}}
$$

where $\text{CVA}_{\text{full}}$ uses the true joint distribution of exposure and default, while $\text{CVA}_{\text{indep}}$ assumes independence. In the presence of wrong-way risk, $\alpha > 1$.

**Typical values:**

- Regulatory floor: $\alpha = 1.4$
- Empirical estimates: $\alpha \in [1.1, 1.5]$ for typical portfolios
- Wrong-way risk portfolios: $\alpha$ can exceed 2.0

---

## Monte Carlo Computation

### Algorithm

1. Simulate $M$ paths of risk factors $\{\mathbf{x}_t^{(m)}\}_{m=1}^M$ at discrete times $t_1, \ldots, t_n$
2. At each time $t_i$ and path $m$, price the portfolio: $V_{t_i}^{(m)} = P(\mathbf{x}_{t_i}^{(m)})$
3. Compute exposure: $E_{t_i}^{(m)} = \max(V_{t_i}^{(m)}, 0)$
4. Estimate EE: $\widehat{\text{EE}}(t_i) = \frac{1}{M} \sum_{m=1}^M E_{t_i}^{(m)}$
5. Estimate EPE: $\widehat{\text{EPE}} = \frac{1}{n} \sum_{i=1}^n \widehat{\text{EE}}(t_i)$

### Standard Error

The Monte Carlo standard error for EE at time $t$ is:

$$
\text{SE}(\widehat{\text{EE}}(t)) = \frac{1}{\sqrt{M}} \sqrt{\frac{1}{M-1} \sum_{m=1}^M \left(E_t^{(m)} - \widehat{\text{EE}}(t)\right)^2}
$$

Typical implementations use $M = 2{,}000$ to $10{,}000$ paths with 50--100 time steps.

---

## Example Calculation

**Setup:** 5-year interest rate swap, notional \$100M, quarterly payment dates.

**Simulated EE profile (simplified):**

| Year $t$ | EE (\$M) | Effective EE (\$M) | PFE$_{95\%}$ (\$M) |
|-----------|----------|---------------------|---------------------|
| 0.5 | 1.5 | 1.5 | 4.2 |
| 1.0 | 2.8 | 2.8 | 7.1 |
| 1.5 | 3.5 | 3.5 | 8.8 |
| 2.0 | 3.9 | 3.9 | 9.5 |
| 2.5 | 4.0 | 4.0 | 9.7 |
| 3.0 | 3.7 | 4.0 | 8.9 |
| 3.5 | 3.1 | 4.0 | 7.4 |
| 4.0 | 2.2 | 4.0 | 5.3 |
| 4.5 | 1.1 | 4.0 | 2.7 |
| 5.0 | 0.0 | 4.0 | 0.0 |

**EPE computation:**

$$
\text{EPE} = \frac{1}{10} (1.5 + 2.8 + 3.5 + 3.9 + 4.0 + 3.7 + 3.1 + 2.2 + 1.1 + 0.0) = \frac{25.8}{10} = \$2.58\text{M}
$$

**Effective EPE (over 1 year, using first two points):**

$$
\text{Effective EPE} = \frac{1}{2}(1.5 + 2.8) = \$2.15\text{M}
$$

**EAD:**

$$
\text{EAD} = 1.4 \times \$2.15\text{M} = \$3.01\text{M}
$$

---

## Key Takeaways

- EPE is the time-averaged expected exposure, reducing the full EE profile to a single number
- Effective EE (running maximum) and Effective EPE prevent regulatory gaming
- PFE captures tail exposure and is used for credit limits; EE/EPE are used for CVA and capital
- Product-specific profiles vary: IRS shows a hump shape, FX forwards grow monotonically
- CVA is approximately proportional to EPE under simplifying assumptions
- The regulatory alpha multiplier ($\ge 1.4$) converts Effective EPE to EAD, accounting for wrong-way risk

---

## Further Reading

- Gregory, J., *Counterparty Credit Risk and Credit Value Adjustment*
- Pykhtin, M. & Zhu, S. (2007), "A Guide to Modelling Counterparty Credit Risk"
- Basel Committee on Banking Supervision, "The Standardised Approach for Measuring Counterparty Credit Risk Exposures (SA-CCR)"
- Brigo, D., Morini, M., & Pallavicini, A., *Counterparty Credit Risk, Collateral and Funding*
- Canabarro, E. & Duffie, D. (2003), "Measuring and Marking Counterparty Risk"

---

## Exercises

**Exercise 1.** Define Expected Exposure (EE) and Expected Positive Exposure (EPE). A 5-year interest rate swap has expected exposure profile $\text{EE}(t) = 0.5\,t\,(5-t)$ (in millions). Compute the EPE as $\text{EPE} = \frac{1}{T}\int_0^T \text{EE}(t)\,dt$.

??? success "Solution to Exercise 1"
    **Expected Exposure (EE)** at time $t$ is the expected value of the positive part of the portfolio value under the risk-neutral measure:

    $$
    \text{EE}(t) = \mathbb{E}^{\mathbb{Q}}[V_t^+] = \mathbb{E}^{\mathbb{Q}}[\max(V_t, 0)]
    $$

    EE is a deterministic function of time that gives the average credit exposure at each future date.

    **Expected Positive Exposure (EPE)** is the time-weighted average of EE over the portfolio horizon:

    $$
    \text{EPE} = \frac{1}{T}\int_0^T \text{EE}(t)\,dt
    $$

    EPE reduces the entire exposure profile to a single summary number.

    **Computation for $\text{EE}(t) = 0.5\,t\,(5-t)$, $T = 5$:**

    $$
    \text{EPE} = \frac{1}{5}\int_0^5 0.5\,t\,(5-t)\,dt = \frac{1}{10}\int_0^5 (5t - t^2)\,dt
    $$

    Evaluate the integral:

    $$
    \int_0^5 (5t - t^2)\,dt = \left[\frac{5t^2}{2} - \frac{t^3}{3}\right]_0^5 = \frac{5 \cdot 25}{2} - \frac{125}{3} = \frac{125}{2} - \frac{125}{3}
    $$

    $$
    = 125\left(\frac{1}{2} - \frac{1}{3}\right) = 125 \cdot \frac{1}{6} = \frac{125}{6}
    $$

    Therefore:

    $$
    \text{EPE} = \frac{1}{10} \cdot \frac{125}{6} = \frac{125}{60} = \frac{25}{12} \approx 2.083 \text{ million}
    $$

    **Verification:** The EE profile $0.5\,t(5-t)$ is a downward-opening parabola with peak $\text{EE}(2.5) = 0.5 \times 2.5 \times 2.5 = 3.125$M at mid-life. The average of a parabolic hump over $[0,5]$ being about 2.08M (roughly two-thirds of the peak) is consistent with $\int_0^T t(T-t)\,dt = T^3/6$.

---

**Exercise 2.** The regulatory Exposure at Default under the Internal Model Method is $\text{EAD} = \alpha \times \text{Effective EPE}$ where $\alpha \ge 1.4$. If the effective EPE is \$12 million, compute the EAD with $\alpha = 1.4$. Explain the economic purpose of the alpha multiplier.

??? success "Solution to Exercise 2"
    **Computation:**

    With Effective EPE $= \$12$M and $\alpha = 1.4$:

    $$
    \text{EAD} = \alpha \times \text{Effective EPE} = 1.4 \times \$12\text{M} = \$16.8 \text{ million}
    $$

    **Economic purpose of the alpha multiplier:**

    The alpha multiplier bridges the gap between the **expected exposure** (used in EPE) and the **exposure conditional on default**. The standard EPE calculation assumes independence between exposure and default:

    $$
    \text{EPE} = \frac{1}{T}\int_0^T \mathbb{E}[V_t^+]\,dt
    $$

    However, in reality, exposure and default may be correlated (wrong-way risk). Formally, the alpha multiplier is defined as:

    $$
    \alpha = \frac{\text{CVA}_{\text{full}}}{\text{CVA}_{\text{indep}}}
    $$

    where $\text{CVA}_{\text{full}}$ uses the true joint distribution of exposure and default, while $\text{CVA}_{\text{indep}}$ assumes independence. The multiplier captures several effects:

    1. **Wrong-way risk:** Exposure may be higher precisely when the counterparty is more likely to default ($\alpha > 1$).
    2. **Granularity of the portfolio:** Concentrated portfolios have more volatile exposure, so the conditional exposure at default exceeds the unconditional EE.
    3. **Stochastic nature of EAD:** Unlike loans with fixed exposure, derivative exposures are stochastic, and the distribution matters beyond the mean.

    The regulatory floor of $\alpha = 1.4$ is conservative: empirical studies estimate $\alpha \in [1.1, 1.5]$ for typical portfolios, but $\alpha$ can exceed 2.0 for portfolios with significant wrong-way risk.

---

**Exercise 3.** Explain why EPE is the appropriate exposure measure for unilateral CVA calculations. How does EPE differ from Potential Future Exposure (PFE) in terms of the aspect of risk it captures (average vs tail)?

??? success "Solution to Exercise 3"
    **Why EPE is appropriate for unilateral CVA:**

    The unilateral CVA formula is:

    $$
    \text{CVA} = \text{LGD}\int_0^T \mathbb{E}[E_t]\cdot dPD(t) = \text{LGD}\int_0^T \text{EE}(t) \cdot \lambda(t) \cdot S(t)\,dt
    $$

    CVA represents the **expected loss** due to counterparty default, which requires the **expected** (i.e., average) exposure at each potential default time. Since default can occur at any time $t \in [0,T]$, we integrate EE over the full horizon, weighted by the probability of default at each instant. The time-averaged EE is precisely the EPE:

    $$
    \text{CVA} \approx \text{LGD} \cdot \lambda \cdot T \cdot \text{EPE}
    $$

    under simplifying assumptions (constant hazard rate, flat discounting). Thus EPE is the natural single-number summary for pricing purposes because CVA is a **risk-neutral expectation** — an average over all scenarios.

    **Difference between EPE and PFE:**

    | Aspect | EPE (via EE) | PFE |
    |--------|-------------|-----|
    | **Statistical measure** | Mean (average) | Quantile (tail) |
    | **Risk captured** | Average credit loss | Worst-case credit exposure |
    | **Use case** | CVA pricing, regulatory capital (EAD) | Credit limit setting, risk appetite |
    | **Formula** | $\text{EE}(t) = \mathbb{E}[V_t^+]$ | $\text{PFE}_\alpha(t) = F_{E_t}^{-1}(\alpha)$ |
    | **Additivity** | Additive across independent portfolios | Sub-additive (not additive) |
    | **Conservatism** | Reflects average outcome | Reflects tail outcome |

    EPE answers: "On average, how much are we exposed?" This is what matters for pricing the credit risk (CVA is a fair-value adjustment). PFE answers: "How bad could the exposure get?" This is what matters for **risk management** — ensuring the bank has enough capital/limits to withstand adverse scenarios.

    Using PFE for CVA would overstate the adjustment (pricing at tail rather than mean), while using EPE for credit limits would understate the risk (average exposure may be small even when tail exposure is large).

---

**Exercise 4.** The Effective EPE is defined as the running maximum of EE: $\text{Effective EE}(t) = \max_{s \le t}\text{EE}(s)$. Explain why this adjustment is conservative. Give an example of a portfolio where EE decreases over time but effective EE does not.

??? success "Solution to Exercise 4"
    **Why Effective EE is conservative:**

    Effective EE is defined as the running maximum of EE:

    $$
    \text{Effective EE}(t) = \max_{s \le t} \text{EE}(s)
    $$

    This means Effective EE can never decrease over time, even if the actual EE decreases. Since $\text{Effective EE}(t) \ge \text{EE}(t)$ for all $t$, it follows that:

    $$
    \text{Effective EPE} = \frac{1}{\min(1\text{yr}, T)}\int_0^{\min(1\text{yr}, T)} \text{Effective EE}(t)\,dt \ge \frac{1}{\min(1\text{yr}, T)}\int_0^{\min(1\text{yr}, T)} \text{EE}(t)\,dt
    $$

    The adjustment is conservative because it prevents the EE profile from "benefiting" from a decline in exposure. The regulatory rationale is to prevent **gaming**: a bank could structure trades so that exposure is low at standard measurement dates but high in between, or could add short-dated trades that mature early (reducing EE in later periods) while the remaining portfolio still carries risk.

    **Example: Portfolio where EE decreases but Effective EE does not.**

    Consider a portfolio consisting of a single 2-year interest rate swap. Its EE profile (in \$M) might be:

    | Time (years) | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 | 1.50 | 1.75 | 2.00 |
    |-------------|------|------|------|------|------|------|------|------|
    | EE          | 1.0  | 1.8  | 2.2  | 2.0  | 1.5  | 1.0  | 0.4  | 0.0  |
    | Effective EE| 1.0  | 1.8  | 2.2  | 2.2  | 2.2  | 2.2  | 2.2  | 2.2  |

    After the peak at $t = 0.75$ years, EE declines due to the amortization effect (pull-to-par). However, Effective EE remains locked at the peak value of 2.2 for all subsequent dates.

    The Effective EPE (computed over 1 year) would be:

    $$
    \text{Effective EPE} = \frac{1}{4}(1.0 + 1.8 + 2.2 + 2.2) = \frac{7.2}{4} = 1.8
    $$

    compared to the standard EPE over 1 year:

    $$
    \text{EPE}_{1\text{yr}} = \frac{1}{4}(1.0 + 1.8 + 2.2 + 2.0) = \frac{7.0}{4} = 1.75
    $$

    The difference is small here but can be much larger for portfolios with sharply declining EE profiles (e.g., portfolios dominated by short-dated trades or those with early amortization features).

---

**Exercise 5.** A netting set contains two interest rate swaps with opposite directions. Swap A has positive expected exposure, Swap B has negative expected exposure. Explain why the EPE of the netting set is less than the EPE of Swap A alone. Under what conditions does netting provide the greatest benefit?

??? success "Solution to Exercise 5"
    **Setup:** A netting set contains two interest rate swaps:

    - **Swap A:** Receive fixed, pay floating — has positive expected exposure $\text{EE}_A(t) > 0$
    - **Swap B:** Pay fixed, receive floating — the opposite direction, so it tends to have negative value when Swap A has positive value. Its stand-alone $\text{EE}_B(t) > 0$ as well, but the key is that $V_B(t)$ and $V_A(t)$ are negatively correlated.

    **Why netted EPE $<$ EPE of Swap A alone:**

    Under netting, the portfolio exposure is:

    $$
    E_t^{\text{net}} = (V_{A,t} + V_{B,t})^+
    $$

    Since Swap B is in the opposite direction, when rates move so that $V_{A,t} > 0$ (Swap A is in-the-money), typically $V_{B,t} < 0$ (Swap B is out-of-the-money). The net value $V_{A,t} + V_{B,t}$ is smaller in magnitude than $V_{A,t}$ alone. Therefore:

    $$
    \text{EE}^{\text{net}}(t) = \mathbb{E}[(V_{A,t} + V_{B,t})^+] < \mathbb{E}[V_{A,t}^+] = \text{EE}_A(t)
    $$

    This inequality follows because netting with a negatively valued position reduces the positive part. Taking the time average:

    $$
    \text{EPE}^{\text{net}} = \frac{1}{T}\int_0^T \text{EE}^{\text{net}}(t)\,dt < \frac{1}{T}\int_0^T \text{EE}_A(t)\,dt = \text{EPE}_A
    $$

    In the extreme case where the swaps are perfectly offsetting (same terms, opposite directions), $V_{A,t} + V_{B,t} = 0$ for all $t$, so $\text{EPE}^{\text{net}} = 0$.

    **When does netting provide the greatest benefit?**

    Netting benefit is maximized when:

    1. **Opposite directions:** The portfolio contains swaps in both directions (receive-fixed and pay-fixed), so their values offset.
    2. **High negative correlation:** The trade values move in opposite directions. For IRS with the same reference rate but opposite directions, correlation is close to $-1$.
    3. **Similar magnitudes:** The offsetting trades have comparable notionals and maturities, so the positive and negative values nearly cancel.
    4. **Diverse maturities:** Trades with different maturities spread exposure over time, reducing the peak net exposure.
    5. **Multiple asset classes:** Including FX, equity, and commodity derivatives with low cross-correlation provides diversification.

    The netting factor is approximately $\text{NF} \approx \bar{\rho} + (1-\bar{\rho})/n$ for large portfolios with pairwise correlation $\bar{\rho}$. When $\bar{\rho}$ is small or negative, NF can be very small, indicating large netting benefits.

---

**Exercise 6.** Describe how Monte Carlo simulation is used to estimate EPE. Outline the key steps: (a) simulate risk factor paths, (b) revalue the portfolio on each path and date, (c) take the positive part, (d) average across paths. What are the main computational challenges for large portfolios?

??? success "Solution to Exercise 6"
    **Monte Carlo estimation of EPE — step by step:**

    **(a) Simulate risk factor paths.** Generate $M$ independent paths of the relevant market risk factors (interest rates, FX rates, equity prices, etc.) at discrete time points $t_1, t_2, \ldots, t_n$ over the portfolio horizon $[0, T]$. For each path $m = 1, \ldots, M$:

    $$
    \{\mathbf{x}_{t_1}^{(m)}, \mathbf{x}_{t_2}^{(m)}, \ldots, \mathbf{x}_{t_n}^{(m)}\}
    $$

    The simulation uses the risk-neutral measure $\mathbb{Q}$ (for pricing/CVA purposes) with calibrated dynamics (e.g., Hull-White for rates, GBM for FX).

    **(b) Revalue the portfolio on each path and date.** For each scenario $(m, t_i)$, reprice every trade in the portfolio using the simulated market state $\mathbf{x}_{t_i}^{(m)}$:

    $$
    V_{t_i}^{(m)} = \sum_{k=1}^{K} V_k(t_i, \mathbf{x}_{t_i}^{(m)})
    $$

    where $K$ is the number of trades. This is the most computationally intensive step — it requires pricing each trade (possibly using analytical formulas, lattice methods, or even nested Monte Carlo) under each scenario.

    **(c) Take the positive part.** Compute exposure on each path:

    $$
    E_{t_i}^{(m)} = \max(V_{t_i}^{(m)}, 0) = (V_{t_i}^{(m)})^+
    $$

    If netting applies, this positive part is taken at the netting set level (after summing trade values), not at the individual trade level.

    **(d) Average across paths.** Estimate EE at each time point:

    $$
    \widehat{\text{EE}}(t_i) = \frac{1}{M}\sum_{m=1}^{M} E_{t_i}^{(m)}
    $$

    Then estimate EPE:

    $$
    \widehat{\text{EPE}} = \frac{1}{n}\sum_{i=1}^{n} \widehat{\text{EE}}(t_i)
    $$

    (for equally spaced time points) or using the trapezoidal rule for unequal spacing.

    **Main computational challenges for large portfolios:**

    1. **Portfolio revaluation cost:** The dominant cost is step (b). For a portfolio of $K$ trades, $M$ paths, and $n$ time steps, the total number of pricings is $K \times M \times n$. For $K = 10{,}000$ trades, $M = 5{,}000$ paths, and $n = 60$ monthly steps, this is 3 billion pricing calls.

    2. **Nested simulation problem:** Some trades (e.g., Bermudan swaptions, callable structures) require their own Monte Carlo for pricing, creating a "simulation within simulation" problem that is computationally prohibitive without approximation techniques (e.g., regression-based methods like Longstaff-Schwartz).

    3. **Memory requirements:** Storing the full cube of portfolio values ($M \times n$ matrix, plus possibly trade-level detail) requires substantial memory, especially for risk-factor-level storage needed for Greeks and sensitivities.

    4. **Time grid selection:** Too few time points miss exposure peaks (especially for trades with discrete cash flows); too many increase computation. Adaptive grids that cluster points around payment dates help.

    5. **Convergence and variance:** EE estimates converge as $1/\sqrt{M}$, so halving the standard error requires quadrupling the number of paths. Variance reduction techniques (antithetic variates, control variates, importance sampling) are essential for efficiency.

    6. **Model calibration and consistency:** The risk factor simulation must be jointly calibrated across all asset classes (rates, FX, equity, credit), maintaining consistent correlations and no-arbitrage conditions.
