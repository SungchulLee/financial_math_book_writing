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
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[\text{PV of Payoff} \mid \mathcal{G}_t\right].
$$

### Decomposition into Components

$$
P^d(t,T) = \underbrace{\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} F \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right]}_{\text{Survival Component}} + \underbrace{\mathbb{E}^{\mathbb{Q}}\left[\text{Recovery Payment} \mid \mathcal{F}_t\right]}_{\text{Default Component}}.
$$

The exact form of the second term depends on the recovery assumption.

---

## Recovery Conventions

### Recovery of Face Value (RFV)

At default, bondholders receive a fraction $R$ of **face value**:

$$
\text{Recovery Payment} = R \cdot F \quad \text{paid at } \tau.
$$

**Price formula:**

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} F \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] + \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{\tau} r_s ds} RF \cdot \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right].
$$

### Recovery of Treasury (RT)

At default, bondholders receive a fraction $R$ of the **risk-free bond value**:

$$
\text{Recovery Payment} = R \cdot P(\tau, T) \cdot F \quad \text{paid at } \tau,
$$

where $P(\tau, T)$ is the risk-free discount factor from $\tau$ to $T$.

This is equivalent to receiving $R \cdot F$ at maturity $T$.

**Price formula:**

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} F \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] + R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right].
$$

### Recovery of Market Value (RMV)

At default, bondholders recover a fraction $R$ of the **pre-default market value** of the bond:

$$
\text{Recovery Payment} = R \cdot P^d(\tau-, T) \quad \text{paid at } \tau.
$$

This leads to a recursive relationship in pricing.

**Simplified formula (Duffie-Singleton):**

Under RMV, the defaultable bond price satisfies:

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + (1-R)\lambda_s) ds} F \mid \mathcal{F}_t\right].
$$

The intensity-adjusted discount rate is $r + (1-R)\lambda$, where $(1-R)\lambda$ is the **loss-adjusted intensity**.

---

## Pricing Under Intensity Models

### Survival Component

Using the fundamental credit pricing formula:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} F \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] = F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} \mid \mathcal{F}_t\right].
$$

### Default Component (RFV)

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{\tau} r_s ds} RF \cdot \mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right] = RF \cdot \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s) ds} \lambda_u \, du \mid \mathcal{F}_t\right].
$$

### Combined Formula (RFV)

$$
P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} \mid \mathcal{F}_t\right] + RF \cdot \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s) ds} \lambda_u \, du \mid \mathcal{F}_t\right].
$$

---

## Special Cases

### Deterministic Rates and Intensity

If $r(t)$ and $\lambda(t)$ are deterministic:

**RFV:**
$$
P^d(t,T) = F \cdot e^{-\int_t^T (r(s) + \lambda(s)) ds} + RF \cdot \int_t^T e^{-\int_t^u (r(s) + \lambda(s)) ds} \lambda(u) \, du.
$$

**RMV/Duffie-Singleton:**
$$
P^d(t,T) = F \cdot e^{-\int_t^T (r(s) + (1-R)\lambda(s)) ds}.
$$

### Constant Rates and Intensity

With constant $r$ and $\lambda$:

**RFV:**
$$
P^d(t,T) = F \cdot e^{-(r+\lambda)(T-t)} + RF \cdot \lambda \cdot \frac{1 - e^{-(r+\lambda)(T-t)}}{r + \lambda}.
$$

**RMV:**
$$
P^d(t,T) = F \cdot e^{-(r + (1-R)\lambda)(T-t)}.
$$

### Zero Recovery

If $R = 0$:
$$
P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} \mid \mathcal{F}_t\right] = P(t,T) \cdot S(t,T),
$$

under independence of $r$ and $\lambda$.

---

## Credit Spread Analysis

### Definition of Yield

The yield on a defaultable zero-coupon bond is:

$$
y^d(t,T) = -\frac{1}{T-t} \ln\left(\frac{P^d(t,T)}{F}\right).
$$

### Credit Spread

The **credit spread** (or **yield spread**) is:

$$
s(t,T) = y^d(t,T) - y(t,T),
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
s \approx (1 - R) \cdot \bar{\lambda},
$$

where $\bar{\lambda}$ is the average intensity over the period.

**Derivation:** Under RMV with constant parameters:
$$
P^d = P \cdot e^{-(1-R)\lambda T} \approx P \cdot (1 - (1-R)\lambda T).
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
P^d_{\text{coupon}}(t,T) = \sum_{i: t_i > t} c \cdot P^d(t, t_i) + F \cdot P^d(t, T),
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
