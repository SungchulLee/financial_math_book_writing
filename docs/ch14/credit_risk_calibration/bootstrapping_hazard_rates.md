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
\lambda(t) = \lambda_i \quad \text{for } t \in (T_{i-1}, T_i], \quad i = 1, \ldots, n,
$$

where $T_0 = 0$.

### Survival Probability

$$
S(0, T_i) = \exp\left(-\sum_{j=1}^{i} \lambda_j (T_j - T_{j-1})\right) = \prod_{j=1}^{i} e^{-\lambda_j \Delta T_j},
$$

where $\Delta T_j = T_j - T_{j-1}$.

### Recursive Structure

Given $\lambda_1, \ldots, \lambda_{i-1}$:

$$
S(0, T_i) = S(0, T_{i-1}) \cdot e^{-\lambda_i \Delta T_i}.
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
s_i \times \text{RPV01}_i = (1-R) \times \text{PV}_{\text{prot}, i},
$$

where both sides depend on survival probabilities up to $T_i$.

---

## Detailed Formulas

### Protection Leg Present Value

$$
\text{PV}_{\text{prot}}(T_i) = (1-R) \sum_{j=1}^{i} \int_{T_{j-1}}^{T_j} D(0,t) \lambda_j S(0,t) \, dt.
$$

With piecewise-constant intensity and assuming continuous compounding:

$$
\text{PV}_{\text{prot}}(T_i) = (1-R) \sum_{j=1}^{i} \lambda_j \int_{T_{j-1}}^{T_j} D(0,t) S(0, T_{j-1}) e^{-\lambda_j (t - T_{j-1})} \, dt.
$$

### Premium Leg Present Value (Risky Annuity)

$$
\text{RPV01}(T_i) = \sum_{k=1}^{m_i} \Delta_k D(0, t_k) S(0, t_k),
$$

where $t_1, \ldots, t_{m_i}$ are premium payment dates up to $T_i$.

### Par Spread Equation

$$
s_i = \frac{(1-R) \sum_{j=1}^{i} \lambda_j \cdot I_j}{\sum_{k=1}^{m_i} \Delta_k D(0, t_k) S(0, t_k)},
$$

where $I_j$ is the integral contribution from period $j$.

---

## Numerical Solution

### Root Finding

For each step $i$, solve for $\lambda_i$ in the nonlinear equation:

$$
f(\lambda_i) = s_i \times \text{RPV01}(T_i; \lambda_1, \ldots, \lambda_i) - (1-R) \times \text{PV}_{\text{prot}}(T_i; \lambda_1, \ldots, \lambda_i) = 0.
$$

Methods:
- **Bisection:** Robust but slow
- **Newton-Raphson:** Fast with good initial guess
- **Brent's method:** Combines reliability and speed

### Initial Guess

Use the constant-intensity approximation:

$$
\lambda_i^{(0)} \approx \frac{s_i}{1 - R}.
$$

### Convergence Criteria

$$
|f(\lambda_i)| < \epsilon, \quad \text{with } \epsilon \sim 10^{-8}.
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

### Step 1: Bootstrap $\lambda_1$ (1Y CDS)

**Approximate:** $\lambda_1 \approx s_1 / (1-R) = 80 / 60 = 133$ bp

**Exact calculation (simplified):**

RPV01(1Y) $\approx 1 \times e^{-0.03} \times e^{-\lambda_1 \times 0.5} \approx 0.97 \times e^{-0.5\lambda_1}$

PV\_prot(1Y) $\approx 0.6 \times \lambda_1 \times \int_0^1 e^{-(0.03 + \lambda_1)t} dt = 0.6 \lambda_1 \times \frac{1 - e^{-(0.03 + \lambda_1)}}{0.03 + \lambda_1}$

Solving $0.008 \times \text{RPV01} = 0.6 \times \text{PV\_prot}$ numerically:

$$
\lambda_1 \approx 1.35\% = 135 \text{ bp}
$$

$S(0,1) = e^{-0.0135} = 0.9866$

### Step 2: Bootstrap $\lambda_2$ (3Y CDS)

Given $\lambda_1 = 135$ bp and $S(0,1) = 0.9866$:

- Need $\lambda_2$ for period (1Y, 3Y)
- Spread $s_2 = 120$ bp applies to full 3Y CDS

Solving (details omitted):

$$
\lambda_2 \approx 1.15\% = 115 \text{ bp}
$$

$S(0,3) = 0.9866 \times e^{-0.0115 \times 2} = 0.9866 \times 0.9772 = 0.9641$

### Step 3: Bootstrap $\lambda_3$ (5Y CDS)

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
\lambda \propto \frac{s}{1-R}.
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
\sum_{i=1}^n \left(s_i^{\text{model}}(\lambda_1, \ldots, \lambda_n) - s_i^{\text{market}}\right)^2.
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
