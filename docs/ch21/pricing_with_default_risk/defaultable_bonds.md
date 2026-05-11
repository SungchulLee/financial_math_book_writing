# Defaultable Bonds

Defaultable bonds are bonds subject to issuer default risk. Their pricing reflects both interest-rate discounting and the possibility of default with partial recovery. Understanding defaultable bond pricing is fundamental to credit markets, as it forms the basis for credit spread analysis and relative value.

---

## Payoff Structure

### Zero-Coupon Defaultable Bond

A defaultable zero-coupon bond with face value $F$, maturity $T$, and recovery rate $R$ pays:

$$
\text{Payoff} = \begin{cases}
F & \text{if } \tau > T \text{ (no default)} \\
R \cdot F \cdot \delta(\tau) & \text{if } \tau \le T \text{ (default)}
\end{cases}
$$

where:

- $\tau$ is the default time
- $R$ is the recovery rate (fraction of face value recovered)
- $\delta(\tau)$ is a timing factor depending on the recovery convention

### Cash Flows Depend on Default

The key distinction from default-free bonds:

- **Uncertain principal:** Recovery payment if default
- **Timing uncertainty:** When and how much is received
- **Credit risk premium:** Compensation for bearing default risk

---

## General Pricing Framework

### Risk-Neutral Valuation

Under the risk-neutral measure $\mathbb{Q}$, the price at time $t$ (on $\{\tau > t\}$) is:

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[\text{PV of Payoff} \mid \mathcal{G}_t\right]
$$

### Decomposition into Components

$$
P^d(t,T) = \underbrace{\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} F \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right]}_{\text{Survival Component}} + \underbrace{\mathbb{E}^{\mathbb{Q}}\left[\text{Recovery Payment} \mid \mathcal{F}_t\right]}_{\text{Default Component}}
$$

The exact form of the second term depends on the recovery assumption.

---

## Recovery Conventions

### Recovery of Face Value (RFV)

At default, bondholders receive a fraction $R$ of **face value**:

$$
\text{Recovery Payment} = R \cdot F \quad \text{paid at } \tau
$$

**Price formula:**

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} F \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] + \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{\tau} r_s ds} RF \cdot \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right]
$$

### Recovery of Treasury (RT)

At default, bondholders receive a fraction $R$ of the **risk-free bond value**:

$$
\text{Recovery Payment} = R \cdot P(\tau, T) \cdot F \quad \text{paid at } \tau
$$

where $P(\tau, T)$ is the risk-free discount factor from $\tau$ to $T$.

This is equivalent to receiving $R \cdot F$ at maturity $T$.

**Price formula:**

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} F \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] + R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right]
$$

### Recovery of Market Value (RMV)

At default, bondholders recover a fraction $R$ of the **pre-default market value** of the bond:

$$
\text{Recovery Payment} = R \cdot P^d(\tau-, T) \quad \text{paid at } \tau
$$

This leads to a recursive relationship in pricing.

**Simplified formula (Duffie-Singleton):**

Under RMV, the defaultable bond price satisfies:

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + (1-R)\lambda_s) ds} F \mid \mathcal{F}_t\right]
$$

The intensity-adjusted discount rate is $r + (1-R)\lambda$, where $(1-R)\lambda$ is the **loss-adjusted intensity**.

---

## Pricing Under Intensity Models

### Survival Component

Using the fundamental credit pricing formula:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} F \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] = F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} \mid \mathcal{F}_t\right]
$$

### Default Component (RFV)

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{\tau} r_s ds} RF \cdot \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right] = RF \cdot \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s) ds} \lambda_u \, du \mid \mathcal{F}_t\right]
$$

### Combined Formula (RFV)

$$
P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} \mid \mathcal{F}_t\right] + RF \cdot \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s) ds} \lambda_u \, du \mid \mathcal{F}_t\right]
$$

---

## Special Cases

### Deterministic Rates and Intensity

If $r(t)$ and $\lambda(t)$ are deterministic:

**RFV:**

$$
P^d(t,T) = F \cdot e^{-\int_t^T (r(s) + \lambda(s)) ds} + RF \cdot \int_t^T e^{-\int_t^u (r(s) + \lambda(s)) ds} \lambda(u) \, du
$$

**RMV/Duffie-Singleton:**

$$
P^d(t,T) = F \cdot e^{-\int_t^T (r(s) + (1-R)\lambda(s)) ds}
$$

### Constant Rates and Intensity

With constant $r$ and $\lambda$:

**RFV:**

$$
P^d(t,T) = F \cdot e^{-(r+\lambda)(T-t)} + RF \cdot \lambda \cdot \frac{1 - e^{-(r+\lambda)(T-t)}}{r + \lambda}
$$

**RMV:**

$$
P^d(t,T) = F \cdot e^{-(r + (1-R)\lambda)(T-t)}
$$

### Zero Recovery

If $R = 0$:

$$
P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} \mid \mathcal{F}_t\right] = P(t,T) \cdot S(t,T)
$$

under independence of $r$ and $\lambda$.

---

## Credit Spread Analysis

### Definition of Yield

The yield on a defaultable zero-coupon bond is:

$$
y^d(t,T) = -\frac{1}{T-t} \ln\left(\frac{P^d(t,T)}{F}\right)
$$

### Credit Spread

The **credit spread** (or **yield spread**) is:

$$
s(t,T) = y^d(t,T) - y(t,T)
$$

where $y(t,T)$ is the yield on a comparable risk-free bond.

### Spread Components

The credit spread compensates for:

1. **Expected loss:** Probability of default × Loss given default
2. **Unexpected loss:** Uncertainty around default
3. **Risk premium:** Compensation for systematic credit risk
4. **Liquidity premium:** Compensation for illiquidity

### Approximate Spread Formula

For small spreads and short horizons:

$$
s \approx (1 - R) \cdot \bar{\lambda}
$$

where $\bar{\lambda}$ is the average intensity over the period.

**Derivation:** Under RMV with constant parameters:

$$
P^d = P \cdot e^{-(1-R)\lambda T} \approx P \cdot (1 - (1-R)\lambda T)
$$

Taking logs: $y^d - y \approx (1-R)\lambda$.

---

## Coupon-Bearing Defaultable Bonds

### Structure

A defaultable coupon bond pays:

- Coupons $c$ at times $t_1, t_2, \ldots, t_n = T$ (if no default)
- Principal $F$ at maturity $T$ (if no default)
- Recovery payment upon default

### Pricing as Sum of Components

$$
P^d_{\text{coupon}}(t,T) = \sum_{i: t_i > t} c \cdot P^d(t, t_i) + F \cdot P^d(t, T)
$$

where each $P^d(t, t_i)$ is a defaultable discount factor.

### Accrued Interest at Default

Upon default, accrued interest from the last coupon date may or may not be paid:

- **With accrued:** Standard market convention
- **Without accrued:** Simplifies modeling

---

## Numerical Example

**Parameters:**

- Face value: $F = 100$
- Recovery rate: $R = 40\%$
- Risk-free rate: $r = 4\%$ (constant)
- Intensity: $\lambda = 2\%$ (constant)
- Maturity: $T = 5$ years
- Recovery convention: RFV

**Calculations:**

**Survival component:**

$$
100 \cdot e^{-(0.04 + 0.02) \times 5} = 100 \cdot e^{-0.30} = 74.08
$$

**Default component:**

$$
40 \cdot 0.02 \cdot \frac{1 - e^{-0.06 \times 5}}{0.06} = 0.8 \cdot \frac{1 - 0.7408}{0.06} = 0.8 \cdot 4.32 = 3.46
$$

**Total price:**

$$
P^d = 74.08 + 3.46 = 77.54
$$

**Yield:**

$$
y^d = -\frac{1}{5} \ln(77.54/100) = \frac{0.2545}{5} = 5.09\%
$$

**Credit spread:**

$$
s = 5.09\% - 4\% = 1.09\% = 109 \text{ bp}
$$

**Check:** Approximate formula gives $s \approx (1-0.4) \times 2\% = 1.2\%$, close to exact.

---

## Comparison of Recovery Conventions

| Convention | Recovery at Default | Analytical Simplicity | Market Use |
|------------|--------------------|-----------------------|------------|
| RFV | $R \cdot F$ | Moderate | Common |
| RT | $R \cdot P(\tau,T) \cdot F$ | Good | Academic |
| RMV | $R \cdot P^d(\tau-,T)$ | Best (Duffie-Singleton) | CDS market |

**RMV advantages:**

- Simple multiplicative adjustment to discount rate
- Closed-form pricing in affine models
- Consistent with CDS market quoting conventions

**RFV advantages:**

- Intuitive: recover fraction of par
- Directly observable in bankruptcy proceedings
- Standard in bond market analysis

---

## Key Takeaways

- Defaultable bonds combine interest rate and credit risk
- Pricing requires specifying recovery convention (RFV, RT, or RMV)
- Under intensity models, prices have semi-closed forms
- RMV (Duffie-Singleton) gives simplest formulas: discount at $r + (1-R)\lambda$
- Credit spreads reflect expected loss plus risk/liquidity premiums
- Coupon bonds price as portfolios of defaultable zero-coupon bonds

---

## Further Reading

- Duffie, D., & Singleton, K. J. (1999). Modeling term structures of defaultable bonds. *Review of Financial Studies*, 12(4), 687–720.
- Jarrow, R. A., & Turnbull, S. M. (1995). Pricing derivatives on financial securities subject to credit risk. *Journal of Finance*, 50(1), 53–85.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 9.
- O'Kane, D. (2008). *Modelling Single-name and Multi-name Credit Derivatives*. Wiley.

---

## Exercises

**Exercise 1.** A defaultable zero-coupon bond has face value $F = 100$, maturity $T = 3$ years, recovery rate $R = 40\%$ under the RFV convention, constant risk-free rate $r = 5\%$, and constant intensity $\lambda = 3\%$. Compute the price using the formula

$$
P^d = F \cdot e^{-(r+\lambda)T} + RF \cdot \frac{\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)T}\right)
$$

Then compute the yield and credit spread.

??? success "Solution to Exercise 1"

    **Given:** $F = 100$, $T = 3$, $R = 0.40$, $r = 0.05$, $\lambda = 0.03$, RFV convention.

    The RFV pricing formula with constant parameters is:

    $$
    P^d = F \cdot e^{-(r+\lambda)T} + RF \cdot \frac{\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)T}\right)
    $$

    **Step 1: Compute the survival component.**

    $$
    F \cdot e^{-(r+\lambda)T} = 100 \cdot e^{-(0.05+0.03)\times 3} = 100 \cdot e^{-0.24}
    $$

    We have $e^{-0.24} = 0.78663$, so the survival component is:

    $$
    100 \times 0.78663 = 78.663
    $$

    **Step 2: Compute the default (recovery) component.**

    $$
    RF \cdot \frac{\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)T}\right) = 40 \cdot \frac{0.03}{0.08}\left(1 - 0.78663\right)
    $$

    $$
    = 40 \times 0.375 \times 0.21337 = 15 \times 0.21337 = 3.201
    $$

    **Step 3: Total price.**

    $$
    P^d = 78.663 + 3.201 = 81.864
    $$

    **Step 4: Compute the yield.**

    $$
    y^d = -\frac{1}{T}\ln\!\left(\frac{P^d}{F}\right) = -\frac{1}{3}\ln\!\left(\frac{81.864}{100}\right) = -\frac{1}{3}\ln(0.81864)
    $$

    Since $\ln(0.81864) = -0.20003$:

    $$
    y^d = \frac{0.20003}{3} = 0.06668 = 6.668\%
    $$

    **Step 5: Compute the credit spread.**

    $$
    s = y^d - r = 6.668\% - 5\% = 1.668\% = 166.8 \text{ bp}
    $$

    The credit spread of approximately 167 bp exceeds the approximate formula $(1-R)\lambda = 0.6 \times 3\% = 1.8\% = 180$ bp because the RFV formula differs from the RMV formula, and the approximation $s \approx (1-R)\lambda$ is exact only under RMV.

---

**Exercise 2.** For the same bond parameters as Exercise 1, compute the price under the RMV (Duffie-Singleton) convention using

$$
P^d = F \cdot e^{-(r+(1-R)\lambda)T}
$$

Compare the two prices and explain why they differ.

??? success "Solution to Exercise 2"

    **Given:** Same parameters as Exercise 1: $F = 100$, $T = 3$, $R = 0.40$, $r = 0.05$, $\lambda = 0.03$.

    The RMV (Duffie-Singleton) formula with constant parameters is:

    $$
    P^d = F \cdot e^{-(r+(1-R)\lambda)T}
    $$

    **Step 1: Compute the effective discount rate.**

    $$
    r + (1-R)\lambda = 0.05 + (1-0.40) \times 0.03 = 0.05 + 0.018 = 0.068
    $$

    **Step 2: Compute the price.**

    $$
    P^d = 100 \cdot e^{-0.068 \times 3} = 100 \cdot e^{-0.204}
    $$

    Since $e^{-0.204} = 0.81546$:

    $$
    P^d = 81.546
    $$

    **Step 3: Compare with the RFV price from Exercise 1.**

    | Convention | Price |
    |---|---|
    | RFV | 81.864 |
    | RMV | 81.546 |

    The RMV price is slightly lower than the RFV price.

    **Explanation of the difference:** Under RFV, the recovery payment is $R \cdot F = 40$ paid at default time $\tau$. Under RMV, the recovery payment is $R \cdot P^d(\tau-, T)$, which is $R$ times the pre-default market value. Since the pre-default market value is less than par ($P^d < F$ for a credit-risky bond), the RMV recovery payment is smaller than $R \cdot F$. This lower recovery leads to a lower bond price under RMV.

    For the RMV convention, the yield is:

    $$
    y^d = -\frac{1}{3}\ln(0.81546) = \frac{0.204}{3} = 0.068 = 6.8\%
    $$

    and the credit spread is exactly:

    $$
    s = 6.8\% - 5\% = 1.8\% = 180 \text{ bp} = (1-R)\lambda
    $$

    This confirms that under RMV, the credit spread equals $(1-R)\lambda$ exactly.

---

**Exercise 3.** Derive the approximate credit spread formula $s \approx (1-R)\lambda$ starting from the RMV pricing formula. Clearly state the assumptions needed and show the steps. For $R = 40\%$ and $\lambda = 200$ bp, compute the approximate spread and compare with the exact yield spread from Exercise 2.

??? success "Solution to Exercise 3"

    **Goal:** Derive $s \approx (1-R)\lambda$ from the RMV pricing formula.

    **Step 1: Start from the Duffie-Singleton formula.**

    Under RMV with constant parameters:

    $$
    P^d(t,T) = F \cdot e^{-(r + (1-R)\lambda)(T-t)}
    $$

    **Step 2: Compute the yield on the defaultable bond.**

    $$
    y^d = -\frac{1}{T-t}\ln\!\left(\frac{P^d(t,T)}{F}\right) = -\frac{1}{T-t}\ln\!\left(e^{-(r+(1-R)\lambda)(T-t)}\right) = r + (1-R)\lambda
    $$

    **Step 3: Compute the risk-free yield.**

    For a risk-free zero-coupon bond with constant rate $r$:

    $$
    y = r
    $$

    **Step 4: Compute the credit spread.**

    $$
    s = y^d - y = \left[r + (1-R)\lambda\right] - r = (1-R)\lambda
    $$

    This derivation is exact under RMV with constant parameters. No approximation is needed.

    **Assumptions required:**

    1. Recovery of Market Value (RMV/Duffie-Singleton) convention
    2. Constant risk-free rate $r$
    3. Constant default intensity $\lambda$
    4. Independence between interest rates and default intensity (automatically satisfied when both are constant)

    For the general (non-constant) case, $s \approx (1-R)\bar{\lambda}$ where $\bar{\lambda}$ is the average intensity, and the formula becomes an approximation rather than exact.

    **Numerical check with $R = 40\%$ and $\lambda = 200$ bp $= 0.02$:**

    $$
    s_{\text{approx}} = (1-0.40) \times 0.02 = 0.012 = 120 \text{ bp}
    $$

    From Exercise 2 with $r = 0.05$, $\lambda = 0.03$, the exact spread was $180$ bp $= (1-0.40) \times 0.03$. For $\lambda = 0.02$, under RMV the exact spread is:

    $$
    s_{\text{exact}} = (1-R)\lambda = 0.6 \times 0.02 = 0.012 = 120 \text{ bp}
    $$

    The approximate and exact values agree perfectly under RMV with constant parameters.

---

**Exercise 4.** A defaultable coupon bond pays semi-annual coupons of 3% per annum on a face value of 100, with maturity $T = 5$ years, $r = 4\%$ constant, $\lambda = 1.5\%$ constant, and $R = 40\%$ under RMV. Compute the bond price as the sum of defaultable discount factors applied to each cash flow. What is the credit spread?

??? success "Solution to Exercise 4"

    **Given:** Semi-annual coupons of 3% per annum on $F = 100$, so coupon rate $= 3\%/2 = 1.5\%$ per period. Maturity $T = 5$ years, $r = 4\%$, $\lambda = 1.5\%$, $R = 40\%$, RMV convention.

    **Step 1: Identify cash flows.**

    Semi-annual coupon payment: $c = 100 \times 0.03/2 = 1.50$ at times $t_i = 0.5, 1.0, 1.5, \ldots, 5.0$ (10 payments). Principal $F = 100$ at $T = 5$.

    **Step 2: Compute defaultable discount factors under RMV.**

    Under Duffie-Singleton with constant parameters, the defaultable discount factor to time $t_i$ is:

    $$
    D^d(0, t_i) = e^{-(r + (1-R)\lambda)t_i} = e^{-(0.04 + 0.6 \times 0.015)t_i} = e^{-0.049 \, t_i}
    $$

    **Step 3: Compute each discount factor.**

    | $t_i$ | $0.049 \times t_i$ | $D^d(0, t_i)$ |
    |---|---|---|
    | 0.5 | 0.0245 | 0.97580 |
    | 1.0 | 0.0490 | 0.95218 |
    | 1.5 | 0.0735 | 0.92912 |
    | 2.0 | 0.0980 | 0.90660 |
    | 2.5 | 0.1225 | 0.88461 |
    | 3.0 | 0.1470 | 0.86312 |
    | 3.5 | 0.1715 | 0.84213 |
    | 4.0 | 0.1960 | 0.82162 |
    | 4.5 | 0.2205 | 0.80157 |
    | 5.0 | 0.2450 | 0.78197 |

    **Step 4: Price the coupon bond.**

    $$
    P^d_{\text{coupon}} = \sum_{i=1}^{10} c \cdot D^d(0, t_i) + F \cdot D^d(0, 5)
    $$

    Sum of coupon discount factors:

    $$
    \sum_{i=1}^{10} D^d(0, t_i) = 0.97580 + 0.95218 + 0.92912 + 0.90660 + 0.88461 + 0.86312 + 0.84213 + 0.82162 + 0.80157 + 0.78197 = 8.95872
    $$

    $$
    P^d_{\text{coupon}} = 1.50 \times 8.95872 + 100 \times 0.78197 = 13.438 + 78.197 = 91.635
    $$

    **Step 5: Compute the credit spread.**

    First, compute the risk-free coupon bond price:

    $$
    D(0, t_i) = e^{-0.04 \, t_i}
    $$

    $$
    \sum_{i=1}^{10} D(0, t_i) = 0.98020 + 0.96079 + 0.94176 + 0.92312 + 0.90484 + 0.88692 + 0.86936 + 0.85214 + 0.83527 + 0.81873 = 8.97313
    $$

    $$
    P_{\text{rf}} = 1.50 \times 8.97313 + 100 \times 0.81873 = 13.460 + 81.873 = 95.333
    $$

    The credit spread can be approximated as:

    $$
    s \approx (1-R)\lambda = 0.6 \times 1.5\% = 0.90\% = 90 \text{ bp}
    $$

    To verify more precisely, we solve for the spread $s$ such that:

    $$
    \sum_{i=1}^{10} 1.50 \cdot e^{-(0.04 + s) t_i} + 100 \cdot e^{-(0.04+s) \times 5} = 91.635
    $$

    Since under RMV the defaultable discount factor is $e^{-(r+(1-R)\lambda)t}$, the spread is exactly $(1-R)\lambda = 0.009 = 90$ bp.

---

**Exercise 5.** Explain the economic differences among the three recovery conventions (RFV, RT, RMV). For a bond with 10 years to maturity that defaults after 2 years, compute the recovery payment under each convention given $R = 40\%$, $F = 100$, $r = 3\%$, and a pre-default bond price of $P^d = 85$.

??? success "Solution to Exercise 5"

    **Part 1: Economic differences among RFV, RT, and RMV.**

    **Recovery of Face Value (RFV):**

    - At default, bondholders receive $R \cdot F$, a fixed fraction of par value.
    - The recovery amount does not depend on when default occurs or on interest rates.
    - This matches bankruptcy practice where recovery is quoted as cents per dollar of par.
    - Pricing requires two separate terms (survival + recovery), making formulas more complex.

    **Recovery of Treasury (RT):**

    - At default at time $\tau$, bondholders receive $R \cdot F \cdot P(\tau, T)$, equivalent to receiving $R \cdot F$ at maturity $T$.
    - The recovery depends on the risk-free discount factor at the time of default, so earlier defaults yield smaller recovery payments (in present value terms at $\tau$).
    - Economically, this is less intuitive: the bondholder receives a risk-free bond paying $R \cdot F$ at maturity.
    - Provides clean separation of credit and interest rate components.

    **Recovery of Market Value (RMV / Duffie-Singleton):**

    - At default, bondholders recover $R \cdot P^d(\tau-, T)$, a fraction of the pre-default market value.
    - This creates a recursive definition: the recovery depends on the bond price just before default, which itself depends on the recovery assumption.
    - Analytically the simplest: default risk is absorbed into the discount rate as $r + (1-R)\lambda$.
    - Standard in CDS markets and affine model frameworks.

    **Part 2: Compute recovery payments for a bond defaulting after 2 years.**

    **Given:** $R = 40\%$, $F = 100$, $r = 3\%$, $T = 10$, $\tau = 2$, $P^d(\tau-, T) = 85$.

    **RFV:**

    $$
    \text{Recovery} = R \cdot F = 0.40 \times 100 = 40
    $$

    This is $\$40$ paid at $\tau = 2$.

    **RT:**

    The risk-free discount factor from $\tau = 2$ to $T = 10$ is:

    $$
    P(\tau, T) = e^{-r(T-\tau)} = e^{-0.03 \times 8} = e^{-0.24} = 0.78663
    $$

    $$
    \text{Recovery} = R \cdot F \cdot P(\tau, T) = 0.40 \times 100 \times 0.78663 = 31.465
    $$

    This is $\$31.47$ paid at $\tau = 2$ (or equivalently, $\$40$ paid at $T = 10$).

    **RMV:**

    $$
    \text{Recovery} = R \cdot P^d(\tau-, T) = 0.40 \times 85 = 34
    $$

    This is $\$34$ paid at $\tau = 2$.

    **Summary:**

    | Convention | Recovery Payment at $\tau = 2$ |
    |---|---|
    | RFV | $\$40.00$ |
    | RT | $\$31.47$ |
    | RMV | $\$34.00$ |

    RFV gives the largest recovery because it is based on par value. RT gives the smallest because it discounts the par recovery to the remaining 8 years at the risk-free rate. RMV is intermediate, reflecting the pre-default market value which is below par but above the present value of par received at maturity.

---

**Exercise 6.** A zero-recovery ($R = 0$) defaultable bond has price $P^d(0,T) = P(0,T) \cdot S(0,T)$ under independence of rates and intensity. If $r = 3\%$, $\lambda = 2\%$, and $T = 5$, compute the survival probability $S(0,5)$, the risk-free bond price $P(0,5)$, and the defaultable bond price. Verify that the credit spread equals $\lambda = 200$ bp exactly in this case.

??? success "Solution to Exercise 6"

    **Given:** $R = 0$, $r = 3\% = 0.03$, $\lambda = 2\% = 0.02$, $T = 5$, $F = 100$, constant rates, independence of $r$ and $\lambda$.

    **Step 1: Compute the survival probability.**

    With constant intensity:

    $$
    S(0,5) = e^{-\lambda T} = e^{-0.02 \times 5} = e^{-0.10} = 0.90484
    $$

    The probability of surviving to year 5 is approximately 90.48%.

    **Step 2: Compute the risk-free bond price.**

    $$
    P(0,5) = e^{-rT} = e^{-0.03 \times 5} = e^{-0.15} = 0.86071
    $$

    **Step 3: Compute the defaultable bond price.**

    With $R = 0$, there is no recovery payment, so:

    $$
    P^d(0,5) = F \cdot P(0,5) \cdot S(0,5) = 100 \times 0.86071 \times 0.90484 = 77.880
    $$

    Equivalently:

    $$
    P^d(0,5) = F \cdot e^{-(r+\lambda)T} = 100 \cdot e^{-(0.03+0.02) \times 5} = 100 \cdot e^{-0.25} = 77.880
    $$

    **Step 4: Verify the credit spread equals $\lambda$.**

    Yield on the defaultable bond:

    $$
    y^d = -\frac{1}{T}\ln\!\left(\frac{P^d}{F}\right) = -\frac{1}{5}\ln(0.77880) = -\frac{1}{5}(-0.25) = 0.05 = 5\%
    $$

    Risk-free yield:

    $$
    y = -\frac{1}{T}\ln P(0,T) = -\frac{1}{5}\ln(0.86071) = -\frac{1}{5}(-0.15) = 0.03 = 3\%
    $$

    Credit spread:

    $$
    s = y^d - y = 5\% - 3\% = 2\% = 200 \text{ bp} = \lambda
    $$

    **Verification:** With $R = 0$, the defaultable bond price is $P^d = F \cdot e^{-(r+\lambda)T}$. The yield is $y^d = r + \lambda$, and the spread is $s = \lambda$ exactly. This is because with zero recovery:

    - Under RMV: $s = (1-R)\lambda = 1 \times \lambda = \lambda$.
    - Under RFV: the recovery component vanishes (since $R = 0$), so $P^d = F \cdot e^{-(r+\lambda)T}$, giving the same result.

    All three recovery conventions coincide when $R = 0$, and the credit spread equals the default intensity exactly.
