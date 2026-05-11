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

??? success "Solution to Exercise 1"

    **Given:** RFV convention, $r = 0.04$, $\lambda = 0.02$, $T = 5$, $F = 100$, $R = 0.40$, constant parameters.

    The RFV formula with constant rates and intensity is:

    $$
    P^d(0,T) = F \cdot e^{-(r+\lambda)T} + R \cdot F \cdot \frac{\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)T}\right)
    $$

    **Survival component:**

    $$
    F \cdot e^{-(r+\lambda)T} = 100 \cdot e^{-(0.04+0.02) \times 5} = 100 \cdot e^{-0.30}
    $$

    Since $e^{-0.30} = 0.74082$:

    $$
    \text{Survival component} = 100 \times 0.74082 = 74.082
    $$

    This represents the present value of receiving the full face value at maturity, conditional on no default, discounted at the combined rate $r + \lambda$.

    **Default (recovery) component:**

    $$
    R \cdot F \cdot \frac{\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)T}\right) = 40 \times \frac{0.02}{0.06}\left(1 - 0.74082\right)
    $$

    $$
    = 40 \times 0.33333 \times 0.25918 = 13.333 \times 0.25918 = 3.456
    $$

    This represents the expected present value of recovery payments, accounting for the probability and timing of default.

    **Total price:**

    $$
    P^d(0,5) = 74.082 + 3.456 = 77.538
    $$

    **Decomposition summary:**

    | Component | Value | Percentage of Total |
    |---|---|---|
    | Survival | 74.082 | 95.5% |
    | Default (recovery) | 3.456 | 4.5% |
    | **Total** | **77.538** | **100%** |

    The survival component dominates because the default intensity is relatively low ($\lambda = 2\%$), so the probability of survival over 5 years is $e^{-0.10} = 90.5\%$, and most of the bond's value comes from the scenario where the issuer does not default.

---

**Exercise 2.** Repeat Exercise 1 using the RMV (Duffie-Singleton) convention. Compare the total prices under RFV and RMV. Explain intuitively why the two conventions give different prices and under what conditions the difference is small.

??? success "Solution to Exercise 2"

    **Given:** Same parameters: $r = 0.04$, $\lambda = 0.02$, $T = 5$, $F = 100$, $R = 0.40$, now under RMV (Duffie-Singleton).

    The RMV formula is:

    $$
    P^d(0,T) = F \cdot e^{-(r + (1-R)\lambda)T}
    $$

    **Computation:**

    $$
    r + (1-R)\lambda = 0.04 + 0.6 \times 0.02 = 0.04 + 0.012 = 0.052
    $$

    $$
    P^d(0,5) = 100 \cdot e^{-0.052 \times 5} = 100 \cdot e^{-0.26} = 100 \times 0.77105 = 77.105
    $$

    **Comparison:**

    | Convention | Price |
    |---|---|
    | RFV | 77.538 |
    | RMV | 77.105 |
    | Difference | 0.433 |

    The RFV price is higher than the RMV price by about 43 cents per $\$100$ face value.

    **Intuitive explanation:**

    Under RFV, the recovery payment is $R \cdot F = 40$ regardless of when default occurs. Under RMV, the recovery is $R \cdot P^d(\tau-, T)$, which is $R$ times the pre-default market value. Since the pre-default market value satisfies $P^d(\tau-, T) < F$ (the defaultable bond trades below par due to credit risk), the RMV recovery is less than $R \cdot F$. This lower expected recovery translates to a lower bond price under RMV.

    **When the difference is small:**

    The difference between RFV and RMV prices is small when:

    - The default intensity $\lambda$ is small (low probability of default means the recovery term matters less)
    - The recovery rate $R$ is small (smaller recovery means the difference in recovery conventions has less impact)
    - The maturity $T$ is short (less time for default to occur)
    - The risk-free rate $r$ is low (the pre-default market value is closer to par)

    In the limit $\lambda \to 0$, both conventions give $P^d \to F \cdot e^{-rT}$, and the difference vanishes.

---

**Exercise 3.** Under recovery of treasury (RT), the bond price simplifies to

$$
P^d(0,T) = F \cdot P(0,T)\left[R + (1-R)\,S(0,T)\right]
$$

Derive this formula from the general pricing expression. For $r = 3\%$, $\lambda = 2\%$, $R = 40\%$, and $T = 5$, compute the price.

??? success "Solution to Exercise 3"

    **Goal:** Derive the RT formula and compute the price.

    **Derivation:**

    Under RT, at default time $\tau$, the bondholder receives $R \cdot F \cdot P(\tau, T)$, which is equivalent to receiving $R \cdot F$ at maturity $T$. The general pricing formula is:

    $$
    P^d(0,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}}\right] + R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{\tau} r_s\,ds}\,P(\tau,T)\,\mathbf{1}_{\{\tau \le T\}}\right]
    $$

    Since $P(\tau, T) = e^{-\int_{\tau}^T r_s\,ds}$, the recovery term becomes:

    $$
    R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^{\tau} r_s\,ds}\,e^{-\int_{\tau}^T r_s\,ds}\,\mathbf{1}_{\{\tau \le T\}}\right] = R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{\tau \le T\}}\right]
    $$

    The key simplification is that discounting from 0 to $\tau$ and then from $\tau$ to $T$ equals discounting from 0 to $T$. Adding the two terms:

    $$
    P^d(0,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}}\right] + R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{\tau \le T\}}\right]
    $$

    Using $\mathbf{1}_{\{\tau \le T\}} = 1 - \mathbf{1}_{\{\tau > T\}}$:

    $$
    P^d(0,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}}\right] + R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\right] - R \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}}\right]
    $$

    $$
    = (1-R) \cdot F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,\mathbf{1}_{\{\tau > T\}}\right] + R \cdot F \cdot P(0,T)
    $$

    Under independence of $r$ and $\lambda$, using $\mathbb{E}[\mathbf{1}_{\{\tau > T\}}] = S(0,T)$:

    $$
    P^d(0,T) = (1-R) \cdot F \cdot P(0,T) \cdot S(0,T) + R \cdot F \cdot P(0,T)
    $$

    $$
    = F \cdot P(0,T)\left[(1-R)\,S(0,T) + R\right] = F \cdot P(0,T)\left[R + (1-R)\,S(0,T)\right]
    $$

    **Numerical computation:** $r = 0.03$, $\lambda = 0.02$, $R = 0.40$, $T = 5$, $F = 100$.

    $$
    P(0,5) = e^{-0.03 \times 5} = e^{-0.15} = 0.86071
    $$

    $$
    S(0,5) = e^{-0.02 \times 5} = e^{-0.10} = 0.90484
    $$

    $$
    P^d(0,5) = 100 \times 0.86071 \times [0.40 + 0.60 \times 0.90484]
    $$

    $$
    = 86.071 \times [0.40 + 0.54290] = 86.071 \times 0.94290 = 81.157
    $$

    The RT defaultable bond price is $\$81.16$.

---

**Exercise 4.** The recovery-intensity trade-off means that pairs $(R, \lambda)$ can produce the same CDS spread since $s \approx (1-R)\lambda$. Find two pairs $(R_1, \lambda_1)$ and $(R_2, \lambda_2)$ that both give a spread of 90 bp. Then compute the defaultable bond prices under RFV for each pair with $r = 3\%$ and $T = 5$. Are the bond prices also equal? Why or why not?

??? success "Solution to Exercise 4"

    **Goal:** Find two $(R, \lambda)$ pairs giving the same spread of 90 bp, then compare RFV bond prices.

    **Step 1: Find two pairs with $s = (1-R)\lambda = 0.0090$.**

    **Pair 1:** $R_1 = 40\%$, then $\lambda_1 = \frac{0.009}{1-0.40} = \frac{0.009}{0.60} = 0.015 = 1.5\%$.

    **Pair 2:** $R_2 = 25\%$, then $\lambda_2 = \frac{0.009}{1-0.25} = \frac{0.009}{0.75} = 0.012 = 1.2\%$.

    Verify: $(1-0.40) \times 0.015 = 0.009$ and $(1-0.25) \times 0.012 = 0.009$. Both give 90 bp.

    **Step 2: Compute RFV bond prices with $r = 0.03$, $T = 5$, $F = 100$.**

    The RFV formula is:

    $$
    P^d = F \cdot e^{-(r+\lambda)T} + RF \cdot \frac{\lambda}{r+\lambda}\left(1 - e^{-(r+\lambda)T}\right)
    $$

    **Pair 1** ($R_1 = 0.40$, $\lambda_1 = 0.015$):

    $$
    r + \lambda_1 = 0.045, \quad e^{-0.045 \times 5} = e^{-0.225} = 0.79852
    $$

    $$
    P^d_1 = 100 \times 0.79852 + 40 \times \frac{0.015}{0.045}(1 - 0.79852)
    $$

    $$
    = 79.852 + 40 \times 0.33333 \times 0.20148 = 79.852 + 2.686 = 82.538
    $$

    **Pair 2** ($R_2 = 0.25$, $\lambda_2 = 0.012$):

    $$
    r + \lambda_2 = 0.042, \quad e^{-0.042 \times 5} = e^{-0.210} = 0.81058
    $$

    $$
    P^d_2 = 100 \times 0.81058 + 25 \times \frac{0.012}{0.042}(1 - 0.81058)
    $$

    $$
    = 81.058 + 25 \times 0.28571 \times 0.18942 = 81.058 + 1.355 = 82.413
    $$

    **Step 3: Compare.**

    | Pair | $R$ | $\lambda$ | $(1-R)\lambda$ | RFV Price |
    |---|---|---|---|---|
    | 1 | 40% | 1.5% | 90 bp | 82.538 |
    | 2 | 25% | 1.2% | 90 bp | 82.413 |

    The bond prices are **not** equal. They differ by 12.5 cents per $\$100$ face value.

    **Why the bond prices differ despite equal CDS spreads:**

    Under RMV, the bond price depends only on $(1-R)\lambda$, so equal loss-adjusted intensities would give equal RMV prices. However, under RFV, the price depends on $R$ and $\lambda$ **separately**, not just through their product $(1-R)\lambda$. Specifically:

    - The survival component $F \cdot e^{-(r+\lambda)T}$ depends on $\lambda$ alone (not on $R$).
    - The recovery component depends on both $R$ and $\lambda$.

    Pair 1 has higher $\lambda$ (1.5% vs 1.2%), which reduces the survival component more, but higher $R$ (40% vs 25%), which increases the recovery component more. These effects do not perfectly offset under RFV. This illustrates the **recovery-intensity identification problem**: CDS spreads alone cannot separately identify $R$ and $\lambda$, and different $(R, \lambda)$ pairs produce different bond prices under RFV even when they produce identical CDS spreads.

---

**Exercise 5.** Using the empirical recovery data in the table (Senior Secured: 50--70%, Senior Unsecured: 35--45%, Subordinated: 20--35%), a firm has both senior unsecured and subordinated bonds with the same maturity $T = 5$ and the same default intensity $\lambda = 3\%$. Compute the credit spread for each seniority class under the approximation $s \approx (1-R)\lambda$. How does the seniority structure affect the spread?

??? success "Solution to Exercise 5"

    **Given:** $\lambda = 3\% = 0.03$, $T = 5$. Recovery rates by seniority class (using midpoints): Senior Secured $R_{\text{SS}} = 60\%$, Senior Unsecured $R_{\text{SU}} = 40\%$, Subordinated $R_{\text{Sub}} = 27.5\%$.

    **Credit spread approximation:** $s \approx (1-R)\lambda$.

    **Senior Unsecured** ($R = 40\%$):

    $$
    s_{\text{SU}} \approx (1 - 0.40) \times 0.03 = 0.60 \times 0.03 = 0.018 = 180 \text{ bp}
    $$

    **Subordinated** ($R = 27.5\%$):

    $$
    s_{\text{Sub}} \approx (1 - 0.275) \times 0.03 = 0.725 \times 0.03 = 0.02175 = 217.5 \text{ bp}
    $$

    **Summary:**

    | Seniority | Recovery Rate $R$ | Loss Given Default $(1-R)$ | Credit Spread |
    |---|---|---|---|
    | Senior Unsecured | 40% | 60% | 180 bp |
    | Subordinated | 27.5% | 72.5% | 217.5 bp |

    **Impact of seniority on spreads:**

    The seniority structure directly affects credit spreads through the loss given default $(1-R)$:

    1. **Same default intensity:** Both bond classes share the same $\lambda = 3\%$ because they are issued by the same firm. Default is a firm-level event that affects all bonds simultaneously.

    2. **Different recovery:** Senior bonds have priority in bankruptcy, so they recover more. Higher recovery means lower loss given default, which translates directly to lower credit spreads.

    3. **Spread differential:** The subordinated bond spread exceeds the senior unsecured spread by:

        $$
        \Delta s = (R_{\text{SU}} - R_{\text{Sub}}) \times \lambda = (0.40 - 0.275) \times 0.03 = 37.5 \text{ bp}
        $$

    4. **Economic intuition:** Subordinated bondholders bear a higher loss in default and are compensated with a wider credit spread. The spread differential between seniority classes is proportional to the difference in recovery rates.

---

**Exercise 6.** Explain why the RMV convention leads to the simplest pricing formulas. Specifically, show that the recursive definition (recovery equals $R$ times the pre-default market value) converts the two-component pricing formula into a single exponential discount. Why is this analytically convenient for affine intensity models?

??? success "Solution to Exercise 6"

    **Why RMV gives the simplest pricing formulas:**

    **Step 1: The two-component pricing formula.**

    Under any recovery convention, the defaultable bond price has two components:

    $$
    P^d(t,T) = \underbrace{\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,F\,\mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right]}_{\text{Survival component}} + \underbrace{\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^{\tau} r_s\,ds}\,\text{Recovery}\,\mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right]}_{\text{Default component}}
    $$

    Under RFV or RT, the recovery term involves different quantities ($R \cdot F$ or $R \cdot F \cdot P(\tau,T)$), leading to a two-term formula that must be evaluated separately.

    **Step 2: The RMV recursive structure.**

    Under RMV, the recovery is $R \cdot P^d(\tau-, T)$, the pre-default market value. This creates a self-referential equation:

    $$
    P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\,F\,\mathbf{1}_{\{\tau > T\}} \mid \mathcal{F}_t\right] + \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^{\tau} r_s\,ds}\,R\,P^d(\tau-,T)\,\mathbf{1}_{\{t < \tau \le T\}} \mid \mathcal{F}_t\right]
    $$

    **Step 3: Resolution via infinitesimal analysis.**

    Consider the instantaneous return over $[t, t+dt]$:

    - With probability $1 - \lambda_t\,dt$: the bond survives and earns the usual return.
    - With probability $\lambda_t\,dt$: default occurs, and the holder receives $R \cdot P^d(t,T)$ instead of $P^d(t,T)$, a loss of $(1-R) \cdot P^d(t,T)$.

    The expected instantaneous loss rate from default is:

    $$
    \lambda_t \cdot (1-R) \cdot P^d(t,T)\,dt
    $$

    No-arbitrage requires this loss to be compensated by additional return, so the effective discount rate becomes:

    $$
    \tilde{r}_t = r_t + (1-R)\lambda_t
    $$

    This converts the two-component formula into a single exponential:

    $$
    P^d(t,T) = F \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (r_s + (1-R)\lambda_s)\,ds} \mid \mathcal{F}_t\right]
    $$

    **Step 4: Why this is analytically convenient for affine models.**

    In an affine framework, the state vector $X_t = (r_t, \lambda_t)$ follows an affine diffusion:

    $$
    dX_t = (\mu_0 + \mu_1 X_t)\,dt + \Sigma(X_t)\,dW_t
    $$

    The key property of affine models is that expectations of the form:

    $$
    \mathbb{E}\!\left[e^{-\int_t^T (\alpha_0 + \alpha_1' X_s)\,ds} \mid X_t\right] = e^{-A(T-t) - B(T-t)' X_t}
    $$

    have exponential-affine solutions, where $A$ and $B$ satisfy Riccati ODEs.

    Under RMV, the effective discount rate is:

    $$
    \tilde{r}_t = r_t + (1-R)\lambda_t = \alpha_0 + \alpha_1' X_t
    $$

    which is affine in $X_t$. Therefore, the defaultable bond price has the closed-form exponential-affine structure:

    $$
    P^d(t,T) = F \cdot e^{-A(T-t) - B(T-t)' X_t}
    $$

    Under RFV or RT, the recovery term involves integrals of the form $\int_t^T e^{-\int_t^u (\cdot)\,ds}\,\lambda_u\,du$, which require an additional integration step and do not reduce to a single exponential. While still computable in affine models, these formulas are more involved and less elegant. The RMV convention uniquely preserves the one-term exponential-affine structure, making it the preferred choice for analytical tractability.
