# Recovery Schemes

Recovery assumptions specify what investors receive upon default. They are crucial modeling choices that significantly affect prices, credit spreads, and the interpretation of calibrated parameters. Different conventions lead to different pricing formulas and have distinct economic interpretations.

---

## Overview of Recovery Conventions

Three standard recovery schemes dominate credit modeling:

1. **Recovery of Face Value (RFV):** Fixed fraction of par paid at default
2. **Recovery of Treasury (RT):** Fraction of risk-free bond value paid at default
3. **Recovery of Market Value (RMV):** Fraction of pre-default market value recovered

Each has advantages in terms of tractability, realism, and market convention.

---

## Recovery of Face Value (RFV)

### Definition

At default time $\tau$, bondholders receive:

$$
\text{Recovery Payment} = R \cdot F
$$

where $R$ is the recovery rate and $F$ is the face value (par).

### Timing

Payment occurs at default time $\tau$, not at maturity.

### Pricing Formula

For a zero-coupon bond with face value $F$ and maturity $T$:

$$
P^d(0,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s ds} \mathbf{1}_{\{\tau > T\}}\right] + R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^{\tau} r_s ds} \mathbf{1}_{\{\tau \le T\}}\right]
$$

Using intensity-based valuation:

$$
P^d(0,T) = F \cdot \mathbb{E}\left[e^{-\int_0^T (r_s + \lambda_s) ds}\right] + R \cdot F \cdot \mathbb{E}\left[\int_0^T e^{-\int_0^u (r_s + \lambda_s) ds} \lambda_u \, du\right]
$$

### Deterministic Rates and Intensity

With constant $r$ and $\lambda$:

$$
P^d(0,T) = F \cdot e^{-(r+\lambda)T} + R \cdot F \cdot \frac{\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)T}\right)
$$

### Advantages and Disadvantages

**Advantages:**
- Intuitive: recovery is a fixed fraction of principal
- Matches bankruptcy practice: recovery rates are quoted as percentage of par
- Standard in bond market analysis

**Disadvantages:**
- More complex pricing formulas (two-term structure)
- Recovery payment timing affects present value

---

## Recovery of Treasury (RT)

### Definition

At default time $\tau$, bondholders receive the equivalent of $R \cdot F$ at maturity $T$:

$$
\text{Recovery Payment at } \tau = R \cdot F \cdot P(\tau, T)
$$

where $P(\tau, T)$ is the risk-free discount factor from $\tau$ to $T$.

### Pricing Formula

$$
P^d(0,T) = F \cdot P(0,T) \cdot \left[R + (1-R) S(0,T)\right]
$$

### Advantages and Disadvantages

**Advantages:**
- Clean separation of credit and interest rate risk
- Analytical simplicity

**Disadvantages:**
- Economically odd: recovery depends on time remaining
- Not how actual bankruptcy works

---

## Recovery of Market Value (RMV)

### Definition (Duffie-Singleton)

At default, bondholders recover a fraction $R$ of the **pre-default market value**:

$$
\text{Recovery Payment} = R \cdot P^d(\tau-, T)
$$

### Key Result

The Duffie-Singleton formula:

$$
P^d(0,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T (r_s + (1-R)\lambda_s) ds}\right]
$$

Default risk enters through the **loss-adjusted intensity** $(1-R)\lambda$.

### Advantages and Disadvantages

**Advantages:**
- Simplest pricing formula
- Closed-form in affine models
- Consistent with CDS conventions

**Disadvantages:**
- Recursive definition less intuitive
- May not match bankruptcy outcomes

---

## Comparison Summary

| Convention | Recovery Payment | Pricing Complexity | Market Use |
|------------|-----------------|-------------------|------------|
| RFV | $R \cdot F$ at $\tau$ | Moderate | Bonds |
| RT | $R \cdot F$ at $T$ | Simple | Academic |
| RMV | $R \cdot P^d(\tau-,T)$ | Simplest | CDS |

---

## Empirical Recovery Rates

Typical recovery rates by seniority:

| Seniority | Average Recovery |
|-----------|-----------------|
| Senior Secured | 50-70% |
| Senior Unsecured | 35-45% |
| Subordinated | 20-35% |
| Junior/Equity | 0-10% |

Standard assumption for CDS: $R = 40\%$ (senior unsecured).

---

## Key Takeaways

- Recovery assumptions materially affect prices and calibrated parameters
- RMV (Duffie-Singleton) gives simplest formulas: discount at $r + (1-R)\lambda$
- RFV is most intuitive and matches bond market practice
- Standard CDS recovery assumption is 40%
- Recovery-intensity trade-off creates identifiability issues in calibration

---

## Further Reading

- Duffie, D., & Singleton, K. J. (1999). Modeling term structures of defaultable bonds. *Review of Financial Studies*.
- O'Kane, D. (2008). *Modelling Single-name and Multi-name Credit Derivatives*. Wiley.

---

## Exercises

**Exercise 1.** Under the RFV convention with constant $r = 4\%$ and $\lambda = 2\%$, compute the price of a 5-year defaultable zero-coupon bond with $F = 100$ and $R = 40\%$. Decompose the price into the survival component and the default (recovery) component.

---

**Exercise 2.** Repeat Exercise 1 using the RMV (Duffie-Singleton) convention. Compare the total prices under RFV and RMV. Explain intuitively why the two conventions give different prices and under what conditions the difference is small.

---

**Exercise 3.** Under recovery of treasury (RT), the bond price simplifies to

$$
P^d(0,T) = F \cdot P(0,T)\left[R + (1-R)\,S(0,T)\right]
$$

Derive this formula from the general pricing expression. For $r = 3\%$, $\lambda = 2\%$, $R = 40\%$, and $T = 5$, compute the price.

---

**Exercise 4.** The recovery-intensity trade-off means that pairs $(R, \lambda)$ can produce the same CDS spread since $s \approx (1-R)\lambda$. Find two pairs $(R_1, \lambda_1)$ and $(R_2, \lambda_2)$ that both give a spread of 90 bp. Then compute the defaultable bond prices under RFV for each pair with $r = 3\%$ and $T = 5$. Are the bond prices also equal? Why or why not?

---

**Exercise 5.** Using the empirical recovery data in the table (Senior Secured: 50--70%, Senior Unsecured: 35--45%, Subordinated: 20--35%), a firm has both senior unsecured and subordinated bonds with the same maturity $T = 5$ and the same default intensity $\lambda = 3\%$. Compute the credit spread for each seniority class under the approximation $s \approx (1-R)\lambda$. How does the seniority structure affect the spread?

---

**Exercise 6.** Explain why the RMV convention leads to the simplest pricing formulas. Specifically, show that the recursive definition (recovery equals $R$ times the pre-default market value) converts the two-component pricing formula into a single exponential discount. Why is this analytically convenient for affine intensity models?
