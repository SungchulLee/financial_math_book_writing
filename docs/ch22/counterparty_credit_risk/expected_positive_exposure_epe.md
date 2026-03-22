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
