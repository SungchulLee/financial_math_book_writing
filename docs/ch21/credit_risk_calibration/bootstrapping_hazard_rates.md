# Bootstrapping Hazard Rates

Calibration of reduced-form credit models typically starts by **bootstrapping hazard rates** from market instruments, most commonly CDS spreads. This process is analogous to yield curve bootstrapping in interest rate markets and produces a term structure of default risk.

---

## Overview

### Goal

Extract a **survival probability curve** $S(0,T)$ or equivalently a **hazard rate curve** $\lambda(t)$ from observed market prices, primarily CDS spreads.

### Inputs

1. **CDS spreads:** $s_1, s_2, \ldots, s_n$ for maturities $T_1, T_2, \ldots, T_n$
2. **Risk-free discount curve:** $D(0,T)$ (from OIS or government bonds)
3. **Recovery rate assumption:** $R$ (typically 40%)

### Output

Piecewise-constant hazard rates $\lambda_1, \lambda_2, \ldots, \lambda_n$ such that each CDS is priced exactly.

---

## The Bootstrapping Framework

### Piecewise-Constant Intensity

Assume:

$$
\lambda(t) = \lambda_i \quad \text{for } t \in (T_{i-1}, T_i], \quad i = 1, \ldots, n
$$

where $T_0 = 0$.

### Survival Probability

$$
S(0, T_i) = \exp\left(-\sum_{j=1}^{i} \lambda_j (T_j - T_{j-1})\right) = \prod_{j=1}^{i} e^{-\lambda_j \Delta T_j}
$$

where $\Delta T_j = T_j - T_{j-1}$.

### Recursive Structure

Given $\lambda_1, \ldots, \lambda_{i-1}$:

$$
S(0, T_i) = S(0, T_{i-1}) \cdot e^{-\lambda_i \Delta T_i}
$$

This recursive structure enables sequential bootstrapping.

---

## The Bootstrapping Algorithm

### Step-by-Step Procedure

**Step 0: Initialize**
- Set $S(0, 0) = 1$
- Input: CDS spreads $(s_1, \ldots, s_n)$, maturities $(T_1, \ldots, T_n)$, recovery $R$, discount curve $D$

**Step 1: Bootstrap $\lambda_1$**
- Solve for $\lambda_1$ such that CDS with spread $s_1$ and maturity $T_1$ prices to zero
- This involves only $\lambda_1$ since $T_1$ is the first maturity

**Step $i$ ($i = 2, \ldots, n$): Bootstrap $\lambda_i$**
- Given $\lambda_1, \ldots, \lambda_{i-1}$ (hence $S(0, T_{i-1})$ is known)
- Solve for $\lambda_i$ such that CDS with spread $s_i$ and maturity $T_i$ prices to zero

### Mathematical Formulation

For each CDS, the par spread condition is:

$$
s_i \times \text{RPV01}_i = (1-R) \times \text{PV}_{\text{prot}, i}
$$

where both sides depend on survival probabilities up to $T_i$.

---

## Detailed Formulas

### Protection Leg Present Value

$$
\text{PV}_{\text{prot}}(T_i) = (1-R) \sum_{j=1}^{i} \int_{T_{j-1}}^{T_j} D(0,t) \lambda_j S(0,t) \, dt
$$

With piecewise-constant intensity and assuming continuous compounding:

$$
\text{PV}_{\text{prot}}(T_i) = (1-R) \sum_{j=1}^{i} \lambda_j \int_{T_{j-1}}^{T_j} D(0,t) S(0, T_{j-1}) e^{-\lambda_j (t - T_{j-1})} \, dt
$$

### Premium Leg Present Value (Risky Annuity)

$$
\text{RPV01}(T_i) = \sum_{k=1}^{m_i} \Delta_k D(0, t_k) S(0, t_k)
$$

where $t_1, \ldots, t_{m_i}$ are premium payment dates up to $T_i$.

### Par Spread Equation

$$
s_i = \frac{(1-R) \sum_{j=1}^{i} \lambda_j \cdot I_j}{\sum_{k=1}^{m_i} \Delta_k D(0, t_k) S(0, t_k)}
$$

where $I_j$ is the integral contribution from period $j$.

---

## Numerical Solution

### Root Finding

For each step $i$, solve for $\lambda_i$ in the nonlinear equation:

$$
f(\lambda_i) = s_i \times \text{RPV01}(T_i; \lambda_1, \ldots, \lambda_i) - (1-R) \times \text{PV}_{\text{prot}}(T_i; \lambda_1, \ldots, \lambda_i) = 0
$$

Methods:
- **Bisection:** Robust but slow
- **Newton-Raphson:** Fast with good initial guess
- **Brent's method:** Combines reliability and speed

### Initial Guess

Use the constant-intensity approximation:

$$
\lambda_i^{(0)} \approx \frac{s_i}{1 - R}
$$

### Convergence Criteria

$$
|f(\lambda_i)| < \epsilon, \quad \text{with } \epsilon \sim 10^{-8}
$$

---

## Pseudocode

```
function BootstrapHazardRates(spreads[], maturities[], R, discountCurve):
    n = length(spreads)
    lambda[] = array of size n
    S_prev = 1.0  # Survival probability at previous node
    
    for i = 1 to n:
        T_prev = maturities[i-1] if i > 1 else 0
        T_curr = maturities[i]
        s = spreads[i]
        
        # Define function to solve
        function f(lambda_i):
            S_curr = S_prev * exp(-lambda_i * (T_curr - T_prev))
            PV_prot = ComputeProtectionLeg(lambda[], lambda_i, i, R, discountCurve)
            RPV01 = ComputeRiskyAnnuity(lambda[], lambda_i, i, discountCurve)
            return s * RPV01 - (1 - R) * PV_prot
        
        # Solve for lambda_i
        lambda[i] = BrentSolve(f, lower=0.0001, upper=1.0)
        S_prev = S_prev * exp(-lambda[i] * (T_curr - T_prev))
    
    return lambda[]
```

---

## Worked Example

### Market Data

| Maturity | CDS Spread (bp) |
|----------|-----------------|
| 1Y | 80 |
| 3Y | 120 |
| 5Y | 150 |

Assume: $R = 40\%$, flat risk-free rate $r = 3\%$, annual premium payments.

### Step 1: Bootstrap λ_1 (1Y CDS)

**Approximate:** $\lambda_1 \approx s_1 / (1-R) = 80 / 60 = 133$ bp

**Exact calculation (simplified):**

RPV01(1Y) $\approx 1 \times e^{-0.03} \times e^{-\lambda_1 \times 0.5} \approx 0.97 \times e^{-0.5\lambda_1}$

PV\_prot(1Y) $\approx 0.6 \times \lambda_1 \times \int_0^1 e^{-(0.03 + \lambda_1)t} dt = 0.6 \lambda_1 \times \frac{1 - e^{-(0.03 + \lambda_1)}}{0.03 + \lambda_1}$

Solving $0.008 \times \text{RPV01} = 0.6 \times \text{PV\_prot}$ numerically:

$$
\lambda_1 \approx 1.35\% = 135 \text{ bp}
$$

$S(0,1) = e^{-0.0135} = 0.9866$

### Step 2: Bootstrap λ_2 (3Y CDS)

Given $\lambda_1 = 135$ bp and $S(0,1) = 0.9866$:

- Need $\lambda_2$ for period (1Y, 3Y)
- Spread $s_2 = 120$ bp applies to full 3Y CDS

Solving (details omitted):

$$
\lambda_2 \approx 1.15\% = 115 \text{ bp}
$$

$S(0,3) = 0.9866 \times e^{-0.0115 \times 2} = 0.9866 \times 0.9772 = 0.9641$

### Step 3: Bootstrap λ_3 (5Y CDS)

Given $\lambda_1, \lambda_2$ and $S(0,3) = 0.9641$:

Solving for $\lambda_3$:

$$
\lambda_3 \approx 2.05\% = 205 \text{ bp}
$$

$S(0,5) = 0.9641 \times e^{-0.0205 \times 2} = 0.9641 \times 0.9599 = 0.9254$

### Summary

| Period | $\lambda$ (bp) | $S(0,T)$ |
|--------|----------------|----------|
| 0–1Y | 135 | 0.9866 |
| 1Y–3Y | 115 | 0.9641 |
| 3Y–5Y | 205 | 0.9254 |

**Observation:** The term structure shows lower mid-term intensity but higher long-term intensity, consistent with the spread curve shape.

---

## Practical Considerations

### Standard CDS Maturities

Typical liquid maturities: 6M, 1Y, 2Y, 3Y, 4Y, 5Y, 7Y, 10Y

For illiquid maturities, interpolation or extrapolation is needed.

### Recovery Rate Sensitivity

Bootstrapped hazard rates depend heavily on assumed recovery:

$$
\lambda \propto \frac{s}{1-R}
$$

A change from $R = 40\%$ to $R = 30\%$ increases implied hazard rates by $\frac{0.60}{0.70} \approx 14\%$.

### Negative Hazard Rates

If spreads are inverted (short-term > long-term) significantly, bootstrapping may produce negative $\lambda_i$, which is economically impossible.

**Solutions:**
- Constrain $\lambda_i \ge 0$ and accept pricing errors
- Use global optimization instead of sequential bootstrap
- Question data quality

### Extrapolation Beyond Last Maturity

For $T > T_n$, common approaches:
- Assume constant intensity: $\lambda(t) = \lambda_n$ for $t > T_n$
- Gradual decay toward long-run average
- Regulatory-specified ultimate hazard rates

---

## Connection to Yield Curve Bootstrapping

| Interest Rates | Credit Risk |
|----------------|-------------|
| Swap rates | CDS spreads |
| Discount factors $D(0,T)$ | Survival probabilities $S(0,T)$ |
| Zero rates | Hazard rates |
| Bootstrap from swaps | Bootstrap from CDS |
| OIS discounting | Risk-free discounting |

The mathematical machinery is nearly identical, with survival replacing discounting.

---

## Alternative Approaches

### Global Fitting

Instead of sequential bootstrapping, fit all hazard rates simultaneously by minimizing:

$$
\sum_{i=1}^n \left(s_i^{\text{model}}(\lambda_1, \ldots, \lambda_n) - s_i^{\text{market}}\right)^2
$$

**Advantages:** More stable, can impose smoothness
**Disadvantages:** Non-unique solution, slower

### Parametric Models

Specify $\lambda(t)$ parametrically (e.g., piecewise linear, Nelson-Siegel form) and calibrate parameters.

### Continuous Hazard Rate Curves

Use spline interpolation to create smooth $\lambda(t)$ from bootstrapped nodes.

---

## Key Takeaways

- Hazard rates are bootstrapped sequentially from CDS spreads
- Piecewise-constant intensity is the standard assumption
- Each CDS maturity adds one equation for one unknown
- The process is analogous to yield curve bootstrapping
- Recovery assumptions critically affect results
- Negative hazard rates signal data or model problems
- Smoothing and regularization improve stability

---

## Further Reading

- O'Kane, D. (2008). *Modelling Single-name and Multi-name Credit Derivatives*. Wiley, Chapter 5.
- Brigo, D., & Mercurio, F. (2006). *Interest Rate Models: Theory and Practice*. Springer, Chapter 21.
- Hull, J. C., & White, A. (2000). Valuing credit default swaps I. *Journal of Derivatives*, 8(1), 29–40.
- ISDA (2009). *ISDA Standard CDS Converter Specification*.

---

## Exercises

**Exercise 1.** Given CDS spreads of 60 bp (1Y) and 100 bp (3Y) with $R = 40\%$ and a flat risk-free rate $r = 2\%$, bootstrap the piecewise-constant hazard rates $\lambda_1$ (for $[0,1]$) and $\lambda_2$ (for $(1,3]$). Use the approximation $\lambda \approx s/(1-R)$ as an initial guess and verify by computing the survival probabilities $S(0,1)$ and $S(0,3)$.

??? success "Solution to Exercise 1"
    **Given:** $s_1 = 60$ bp (1Y), $s_2 = 100$ bp (3Y), $R = 40\%$, flat $r = 2\%$.

    **Initial guesses** from the approximation $\lambda \approx s/(1-R)$:

    $$
    \lambda_1^{(0)} \approx \frac{60}{60} = 100 \text{ bp} = 1.00\%
    $$

    $$
    \lambda_2^{(0)} \approx \frac{100}{60} \approx 167 \text{ bp} = 1.67\%
    $$

    **Bootstrapping $\lambda_1$:** For the 1Y CDS with continuous premium payment, the par spread condition is:

    $$
    s_1 \times \text{RPV01}(1) = (1-R) \times \text{PV}_{\text{prot}}(1)
    $$

    Under continuous premium payment and piecewise-constant intensity:

    $$
    \text{RPV01}(1) = \int_0^1 e^{-rt} e^{-\lambda_1 t}\, dt = \frac{1 - e^{-(r+\lambda_1)}}{r + \lambda_1}
    $$

    $$
    \text{PV}_{\text{prot}}(1) = (1-R)\lambda_1 \int_0^1 e^{-rt} e^{-\lambda_1 t}\, dt = (1-R)\lambda_1 \cdot \frac{1 - e^{-(r+\lambda_1)}}{r + \lambda_1}
    $$

    Substituting into the par spread condition:

    $$
    s_1 \cdot \frac{1 - e^{-(r+\lambda_1)}}{r+\lambda_1} = (1-R)\lambda_1 \cdot \frac{1 - e^{-(r+\lambda_1)}}{r+\lambda_1}
    $$

    The integral factors cancel, giving $s_1 = (1-R)\lambda_1$, so:

    $$
    \lambda_1 = \frac{s_1}{1-R} = \frac{0.0060}{0.60} = 1.00\%
    $$

    The survival probability at $T_1 = 1$:

    $$
    S(0,1) = e^{-\lambda_1 \cdot 1} = e^{-0.01} = 0.9900
    $$

    **Bootstrapping $\lambda_2$:** For the 3Y CDS, the par spread equation involves the full survival curve from $0$ to $3$. With $T_0 = 0$, $T_1 = 1$, $T_2 = 3$, the protection leg is:

    $$
    \text{PV}_{\text{prot}}(3) = (1-R)\left[\lambda_1 \int_0^1 e^{-(r+\lambda_1)t}\,dt + \lambda_2 S(0,1)\int_0^2 e^{-(r+\lambda_2)u}\,du\right]
    $$

    where $u = t - 1$. Evaluating:

    - First integral: $\lambda_1 \cdot \frac{1 - e^{-(r+\lambda_1)}}{r+\lambda_1} = 0.01 \cdot \frac{1-e^{-0.03}}{0.03} = 0.01 \times 0.9851 = 0.009851$

    - Second integral: $\lambda_2 \cdot S(0,1) \cdot \frac{1-e^{-2(r+\lambda_2)}}{r+\lambda_2}$

    Similarly for the RPV01, with discrete annual payments at $t = 1, 2, 3$:

    $$
    \text{RPV01}(3) = e^{-r}S(0,1) + e^{-2r}S(0,2) + e^{-3r}S(0,3)
    $$

    where $S(0,2) = S(0,1)e^{-\lambda_2}$ and $S(0,3) = S(0,1)e^{-2\lambda_2}$.

    Setting $s_2 \times \text{RPV01}(3) = (1-R) \times \text{PV}_{\text{prot}}(3)$ and solving numerically for $\lambda_2$ yields a value near the initial guess. Using Newton-Raphson with $\lambda_2^{(0)} = 1.67\%$:

    $$
    \lambda_2 \approx 1.21\%
    $$

    Note that $\lambda_2 > \lambda_1$ is consistent with the upward-sloping spread curve. The marginal hazard rate for the (1Y, 3Y] period is lower than the initial guess because the 3Y CDS spread reflects the average intensity over the entire 3-year period, not just the marginal period.

    The survival probability at $T_2 = 3$:

    $$
    S(0,3) = S(0,1) \cdot e^{-\lambda_2 \times 2} = 0.9900 \times e^{-0.0121 \times 2} = 0.9900 \times 0.9761 = 0.9663
    $$

    **Summary:**

    | Period | $\lambda$ (bp) | $S(0,T)$ |
    |--------|----------------|----------|
    | 0--1Y | 100 | 0.9900 |
    | 1Y--3Y | 121 | 0.9663 |

---

**Exercise 2.** Suppose a bootstrapping procedure yields a negative hazard rate $\lambda_3 < 0$ for the period $(3\text{Y}, 5\text{Y}]$. Explain the economic interpretation of this result. Under what CDS spread term structure would this occur? Propose two remedies to handle this in practice.

??? success "Solution to Exercise 2"
    **Economic interpretation of $\lambda_3 < 0$:**

    A negative hazard rate for the period $(3\text{Y}, 5\text{Y}]$ would imply that the conditional probability of default in that period, given survival to 3Y, is negative. This is economically nonsensical---a firm that has survived to year 3 cannot have a negative probability of defaulting between years 3 and 5.

    Mathematically, $\lambda_3 < 0$ means $S(0,5) > S(0,3)$, i.e., the survival probability *increases* with time, which violates monotonicity.

    **CDS spread term structure producing this:** This occurs when the CDS spread curve is **sharply inverted**, i.e., the 5Y spread is significantly lower than the 3Y spread. In sequential bootstrapping, the 5Y CDS reprices the entire 0-to-5Y period. If $s_5 \ll s_3$, then the average intensity over $[0,5]$ implied by $s_5$ is much lower than the average over $[0,3]$ implied by $s_3$. To reconcile these, the bootstrapping algorithm forces $\lambda_3$ to be negative to bring the average down.

    For example, if $s_3 = 200$ bp and $s_5 = 80$ bp with $R = 40\%$, the implied average intensity over $[0,3]$ is roughly $200/60 \approx 333$ bp, while over $[0,5]$ it is $80/60 \approx 133$ bp. The dramatic drop requires an extremely low (or negative) marginal intensity in the $(3,5]$ period.

    **Two remedies:**

    1. **Constrain $\lambda_i \ge 0$:** Impose a non-negativity constraint during root finding, e.g., $\lambda_3 = \max(\hat{\lambda}_3, 0)$. This means the 5Y CDS will not be priced exactly---there will be a residual pricing error---but the hazard rate curve remains economically meaningful. The mispricing can be reported as a diagnostic.

    2. **Global fitting with regularization:** Instead of sequential bootstrapping, solve for all hazard rates simultaneously by minimizing a weighted sum of pricing errors plus a regularization penalty:

        $$
        \min_{\lambda_1,\ldots,\lambda_n \ge 0} \sum_i w_i \left(s_i^{\text{model}} - s_i^{\text{market}}\right)^2 + \alpha \sum_i (\lambda_{i+1} - \lambda_i)^2
        $$

        The non-negativity constraint and smoothness penalty prevent negative and wildly oscillating hazard rates, at the cost of imperfect market fit.

---

**Exercise 3.** Starting from the par spread condition

$$
s_i \times \text{RPV01}(T_i) = (1 - R) \times \text{PV}_{\text{prot}}(T_i)
$$

show that under a single-period CDS with maturity $T_1$ and continuous premium payment, the hazard rate satisfies $\lambda_1 = s_1 / (1 - R)$ exactly, regardless of the risk-free rate $r$.

??? success "Solution to Exercise 3"
    **Goal:** Show that for a single-period CDS with maturity $T_1$ and continuous premium payment, $\lambda_1 = s_1/(1-R)$ exactly.

    **Setup:** Consider a CDS with maturity $T_1$, continuous spread payment at rate $s_1$, recovery rate $R$, constant hazard rate $\lambda_1$, and risk-free rate $r$.

    **Premium (fee) leg:** The present value of continuous spread payments is:

    $$
    \text{RPV01}(T_1) = \int_0^{T_1} e^{-rt} S(0,t)\, dt = \int_0^{T_1} e^{-rt} e^{-\lambda_1 t}\, dt = \int_0^{T_1} e^{-(r+\lambda_1)t}\, dt
    $$

    $$
    = \frac{1 - e^{-(r+\lambda_1)T_1}}{r + \lambda_1}
    $$

    **Protection leg:** The present value of the default payment is:

    $$
    \text{PV}_{\text{prot}}(T_1) = (1-R)\int_0^{T_1} e^{-rt} \lambda_1 S(0,t)\, dt = (1-R)\lambda_1 \int_0^{T_1} e^{-(r+\lambda_1)t}\, dt
    $$

    $$
    = (1-R)\lambda_1 \cdot \frac{1 - e^{-(r+\lambda_1)T_1}}{r + \lambda_1}
    $$

    **Par spread condition:** Setting $s_1 \times \text{RPV01} = \text{PV}_{\text{prot}}$:

    $$
    s_1 \cdot \frac{1 - e^{-(r+\lambda_1)T_1}}{r + \lambda_1} = (1-R)\lambda_1 \cdot \frac{1 - e^{-(r+\lambda_1)T_1}}{r + \lambda_1}
    $$

    The factor $\frac{1 - e^{-(r+\lambda_1)T_1}}{r + \lambda_1}$ is strictly positive (for $r + \lambda_1 > 0$ and $T_1 > 0$), so it cancels from both sides:

    $$
    s_1 = (1-R)\lambda_1
    $$

    Therefore:

    $$
    \lambda_1 = \frac{s_1}{1-R}
    $$

    This holds **exactly** and is **independent of the risk-free rate $r$**. The key insight is that with continuous premium payment and constant intensity, both the premium and protection legs share the identical integral factor, so $r$ drops out of the ratio. This is why $\lambda \approx s/(1-R)$ is such a good approximation even for multi-period CDS---it becomes exact in the single-period continuous case. $\blacksquare$

---

**Exercise 4.** A hazard rate curve bootstrapped from CDS spreads with $R = 40\%$ produces $\lambda(0\text{--}5\text{Y}) = 150$ bp. If the recovery assumption is revised to $R = 30\%$, estimate the new hazard rate. Compute the percentage change and explain why recovery rate uncertainty is a major source of calibration risk.

??? success "Solution to Exercise 4"
    **Given:** $\lambda = 150$ bp with $R = 40\%$, revised to $R = 30\%$.

    The approximate relationship is $s \approx (1-R)\lambda$, which gives a fixed spread:

    $$
    s = (1-R)\lambda = 0.60 \times 0.0150 = 0.0090 = 90 \text{ bp}
    $$

    Since the CDS spread $s$ is a market observable (it does not change when we change assumptions), we hold $s = 90$ bp fixed and solve for the new hazard rate under $R = 30\%$:

    $$
    \lambda_{\text{new}} = \frac{s}{1 - R_{\text{new}}} = \frac{0.0090}{0.70} = 1.286\% \approx 129 \text{ bp}
    $$

    **Percentage change:**

    $$
    \frac{\lambda_{\text{new}} - \lambda_{\text{old}}}{\lambda_{\text{old}}} = \frac{129 - 150}{150} = -14.3\%
    $$

    Alternatively, the ratio of hazard rates is:

    $$
    \frac{\lambda_{\text{new}}}{\lambda_{\text{old}}} = \frac{1-R_{\text{old}}}{1-R_{\text{new}}} = \frac{0.60}{0.70} = 0.857
    $$

    so the hazard rate decreases by approximately 14.3%.

    **Why recovery rate uncertainty is a major source of calibration risk:**

    1. **Non-observability:** Recovery rates are not directly observable from CDS spreads. The market quotes a spread, but the split into $\lambda$ and $R$ is inherently ambiguous.

    2. **Proportional impact:** Since $\lambda = s/(1-R)$, the hazard rate is inversely proportional to $(1-R)$. A 10 percentage point change in $R$ (e.g., from 40% to 30%) produces a 14% change in $\lambda$, which propagates into survival probabilities, CVA calculations, and hedging ratios.

    3. **Compounding over time:** The survival probability $S(0,T) = e^{-\lambda T}$, so recovery uncertainty compounds exponentially. For long horizons, the impact on survival probabilities and expected losses is amplified.

    4. **Downstream effects:** Many risk metrics (CVA, economic capital, expected loss provisions) depend on both $\lambda$ and $R$. The product $(1-R) \times \text{default probability}$ may be stable, but the individual components are not, leading to misleading parameter interpretations.

---

**Exercise 5.** Describe the analogy between CDS bootstrapping and interest rate yield curve construction. For each of the following concepts in the interest rate world, identify its credit risk counterpart: (a) swap rate, (b) discount factor, (c) forward rate, (d) par instrument.

??? success "Solution to Exercise 5"
    The analogy between CDS bootstrapping and interest rate yield curve construction is systematic:

    **(a) Swap rate $\longleftrightarrow$ CDS spread**

    A swap rate is the par coupon that makes the swap value zero at inception. Analogously, a CDS spread is the par premium that sets the CDS value to zero at inception. Both are par instrument rates that encode the term structure.

    **(b) Discount factor $D(0,T)$ $\longleftrightarrow$ Survival probability $S(0,T)$**

    The discount factor gives the present value of \$1 received at time $T$ if there is no default concern. The survival probability gives the probability-weighted factor for receiving \$1 conditional on survival to $T$. Both are decreasing functions of $T$ starting from 1 at $T=0$, and both are the fundamental quantities bootstrapped from market data.

    **(c) Forward rate $f(T_1, T_2)$ $\longleftrightarrow$ Forward hazard rate $\lambda(T_1, T_2)$**

    The forward rate is the rate implied for a future period by today's term structure:

    $$
    f(T_1, T_2) = -\frac{\ln D(0,T_2) - \ln D(0,T_1)}{T_2 - T_1}
    $$

    The forward hazard rate is the default intensity for a future period:

    $$
    \lambda(T_1, T_2) = -\frac{\ln S(0,T_2) - \ln S(0,T_1)}{T_2 - T_1}
    $$

    Both represent marginal rates for future intervals, and both are the "local" building blocks of their respective term structures.

    **(d) Par instrument (par swap or par bond) $\longleftrightarrow$ Par CDS**

    A par bond or par swap is one that prices at par given the current term structure. A par CDS is one whose spread is set so that the contract has zero value at inception. In bootstrapping, each par instrument provides one equation to determine one unknown in the term structure.

    The mathematical machinery is identical: sequential root-finding where each new maturity adds one equation and one unknown, building the term structure from short to long maturities.

---

**Exercise 6.** Consider the global fitting alternative where all hazard rates are determined simultaneously by minimizing

$$
\sum_{i=1}^{n}\left(s_i^{\text{model}}(\lambda_1, \ldots, \lambda_n) - s_i^{\text{market}}\right)^2
$$

Discuss the advantages and disadvantages of global fitting compared to sequential bootstrapping. Under what conditions would you prefer one method over the other?

??? success "Solution to Exercise 6"
    **Global fitting** determines all hazard rates $\lambda_1, \ldots, \lambda_n$ simultaneously by minimizing:

    $$
    \sum_{i=1}^{n}\left(s_i^{\text{model}}(\lambda_1, \ldots, \lambda_n) - s_i^{\text{market}}\right)^2
    $$

    **Advantages of global fitting over sequential bootstrapping:**

    1. **Stability:** Small perturbations in a single CDS spread affect all hazard rates smoothly, rather than causing large jumps in one interval. The error is distributed across all parameters.

    2. **Smoothness constraints:** The objective function can be augmented with a regularization term such as $\alpha \sum_i (\lambda_{i+1} - \lambda_i)^2$, which penalizes abrupt changes and produces smoother hazard rate curves.

    3. **Non-negativity enforcement:** Constraints $\lambda_i \ge 0$ for all $i$ are naturally incorporated, preventing the economically meaningless negative hazard rates that sequential bootstrapping can produce.

    4. **Robustness to noisy data:** In illiquid markets with wide bid-ask spreads, global fitting produces more reliable estimates because no single instrument dominates the calibration of any parameter.

    **Disadvantages of global fitting:**

    1. **Non-uniqueness:** The optimization problem may have multiple local minima, especially with many parameters. Different starting points can yield different solutions.

    2. **Computational cost:** Each evaluation of the objective function requires computing all CDS prices, and gradient-based methods need sensitivities of each price to all hazard rates. This is significantly slower than the one-dimensional root-finding in sequential bootstrapping.

    3. **No exact fit:** Unlike bootstrapping (which prices each CDS exactly), global fitting typically produces residual pricing errors for all instruments. Whether this is acceptable depends on the application.

    4. **Choice of regularization:** The penalty parameter $\alpha$ must be chosen, introducing a subjective element. Too little regularization gives an unstable fit; too much smooths away genuine term structure features.

    **When to prefer each method:**

    - **Sequential bootstrapping** is preferred when CDS data is clean, liquid, and available at standard maturities, and exact repricing is required (e.g., for marking to market or CDS trading desks).

    - **Global fitting** is preferred when data is noisy, maturities are non-standard or sparse, negative hazard rates arise from bootstrapping, or the hazard rate curve needs to be smooth for downstream applications (e.g., CVA computation, risk management).

---

**Exercise 7.** A firm's CDS curve has liquid quotes at 1Y, 3Y, 5Y, 7Y, and 10Y. You need to price a 6Y CDS but do not have a direct 6Y quote. Describe how you would interpolate the hazard rate curve between the 5Y and 7Y nodes. Compare piecewise-constant and piecewise-linear interpolation in terms of smoothness and ease of implementation.

??? success "Solution to Exercise 7"
    **Problem:** Interpolate the hazard rate curve at $T = 6\text{Y}$ between the 5Y and 7Y bootstrapped nodes.

    Let $\lambda_5$ and $\lambda_7$ denote the piecewise-constant hazard rates for the periods ending at 5Y and 7Y, respectively. The survival probabilities at the bootstrapped nodes are known: $S(0,5)$ and $S(0,7)$.

    **Piecewise-constant interpolation:**

    Under this approach, $\lambda(t) = \lambda_7$ for all $t \in (5, 7]$. The survival probability at $T = 6$ is:

    $$
    S(0,6) = S(0,5) \cdot e^{-\lambda_7 \times 1}
    $$

    This is the simplest approach and is the default in standard bootstrapping. The hazard rate jumps at each node but is flat between nodes.

    - **Advantages:** Trivially simple to implement; the survival curve is continuous (though its derivative is not); exactly consistent with bootstrapped values at nodes.
    - **Disadvantages:** The hazard rate has discontinuities at node points, which creates jumps in forward default probabilities. The interpolated 6Y value depends only on $\lambda_7$ and ignores the transition from $\lambda_5$.

    **Piecewise-linear interpolation:**

    Here, the hazard rate varies linearly between nodes:

    $$
    \lambda(t) = \lambda_5 + \frac{\lambda_7 - \lambda_5}{T_7 - T_5}(t - T_5) \quad \text{for } t \in (5, 7]
    $$

    At $t = 6$ (the midpoint):

    $$
    \lambda(6) = \frac{\lambda_5 + \lambda_7}{2}
    $$

    The survival probability requires integrating the time-varying intensity:

    $$
    S(0,6) = S(0,5) \cdot \exp\left(-\int_5^6 \lambda(t)\, dt\right)
    $$

    where:

    $$
    \int_5^6 \lambda(t)\, dt = \int_5^6 \left[\lambda_5 + \frac{\lambda_7 - \lambda_5}{2}(t-5)\right] dt = \lambda_5 + \frac{\lambda_7 - \lambda_5}{4} = \frac{3\lambda_5 + \lambda_7}{4}
    $$

    - **Advantages:** The hazard rate curve is continuous (no jumps at nodes), which is more physically realistic. Forward default probabilities transition smoothly between maturities.
    - **Disadvantages:** More complex to implement because the protection and premium leg integrals must account for a linearly varying intensity within each period. Requires recalibrating node values since changing the interpolation method changes the relationship between node hazard rates and CDS prices.

    **Comparison summary:**

    | Feature | Piecewise-constant | Piecewise-linear |
    |---------|-------------------|------------------|
    | Hazard rate continuity | Discontinuous at nodes | Continuous |
    | Survival curve smoothness | $C^0$ (continuous) | $C^1$ (smooth) |
    | Implementation | Simple | Moderate |
    | Integral evaluation | Closed-form | Closed-form (but more terms) |
    | Calibration consistency | Exact at nodes | Requires re-bootstrapping |

    In practice, piecewise-constant is the industry standard for its simplicity, but piecewise-linear (or cubic spline) interpolation is used when smooth hazard rate curves are needed for sensitivity analysis or exotic pricing.
