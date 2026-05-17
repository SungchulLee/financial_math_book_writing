# CDS Spreads and Hazard Rates


CDS spreads encode market-implied default risk and can be mapped to **hazard rates** within reduced-form credit models.

---

## Relationship between spreads and default risk


Recall (see [§ Default Intensity and Hazard Rates](../reduced_form_intensity_based_models/default_intensity_and_hazard_rates.md)): higher hazard rate $\lambda$ implies more frequent defaults; spreads compensate for expected default losses.

Under simplifying assumptions, spreads are approximately:

$$
s \approx (1 - R) \times \text{average hazard rate}
$$



---

## Formal link under intensity models


Recall (see [§ Credit Default Swaps (CDS)](credit_default_swaps_cds.md)): equating protection and premium legs under recovery of face value and deterministic intensity $\lambda$ gives

$$
s
= \frac{(1-R) \int_0^T e^{-\int_0^t (r+\lambda) ds} \lambda \, dt}
{\int_0^T e^{-\int_0^t (r+\lambda) ds} \, dt}.
$$



This equation is inverted to infer $\lambda$ from market spreads.

---

## CDS bootstrapping


In practice:

- CDS spreads across maturities are given,
- piecewise-constant hazard rates are assumed,
- hazard rates are bootstrapped sequentially.

This is analogous to yield curve construction.

---

## Limitations


- Recovery assumptions affect inferred hazard rates.
- Liquidity and counterparty risk affect CDS spreads.
- The hazard-rate interpretation is model-dependent.

---

## Key takeaways


- CDS spreads imply default intensities.
- Bootstrapping extracts hazard rate curves.
- Interpretation depends on recovery and model choices.

---

## Further reading


- Brigo et al., CDS bootstrapping.
- O'Kane, CDS term structures.

---

## Exercises

**Exercise 1.** A 5-year CDS has a par spread of $s = 120$ bp and the assumed recovery rate is $R = 40\%$. Using the approximation $s \approx (1-R)\lambda$, compute the implied constant hazard rate $\lambda$. What is the corresponding 5-year survival probability $S(0,5) = e^{-\lambda \cdot 5}$?

??? success "Solution to Exercise 1"

    Using the approximation $s \approx (1-R)\lambda$, we solve for the implied hazard rate:

    $$
    \lambda = \frac{s}{1-R} = \frac{120 \text{ bp}}{1 - 0.40} = \frac{0.0120}{0.60} = 0.0200 = 200 \text{ bp}
    $$

    The implied constant hazard rate is $\lambda = 2\%$ per annum.

    The 5-year survival probability is:

    $$
    S(0,5) = e^{-\lambda \cdot 5} = e^{-0.02 \times 5} = e^{-0.10} = 0.9048
    $$

    Therefore the implied 5-year default probability is:

    $$
    \mathbb{Q}(\tau \le 5) = 1 - S(0,5) = 1 - 0.9048 = 0.0952 = 9.52\%
    $$

    Under this model, there is approximately a 9.5% risk-neutral probability that the reference entity defaults within 5 years.

---

**Exercise 2.** Under deterministic intensity $\lambda$ and constant risk-free rate $r$, the par CDS spread satisfies

$$
s = \frac{(1-R)\int_0^T e^{-(r+\lambda)t}\,\lambda\,dt}{\int_0^T e^{-(r+\lambda)t}\,dt}
$$

Show that this simplifies to $s = (1-R)\lambda$ regardless of $r$ and $T$. Explain why the risk-free rate cancels in this expression.

??? success "Solution to Exercise 2"

    Starting from the general formula with constant $\lambda$ and $r$:

    $$
    s = \frac{(1-R)\int_0^T e^{-(r+\lambda)t}\,\lambda\,dt}{\int_0^T e^{-(r+\lambda)t}\,dt}
    $$

    Since $\lambda$ is constant, it factors out of the numerator integral:

    $$
    s = \frac{(1-R) \cdot \lambda \cdot \int_0^T e^{-(r+\lambda)t}\,dt}{\int_0^T e^{-(r+\lambda)t}\,dt}
    $$

    The integrals in the numerator and denominator are identical and cancel:

    $$
    s = (1-R)\lambda
    $$

    This holds for any values of $r$ and $T$ (provided $T > 0$), not just specific ones.

    **Why the risk-free rate cancels:** The factor $e^{-(r+\lambda)t}$ appears in both the protection leg (numerator) and the premium leg (denominator) because both legs involve:

    - Time-value discounting at rate $r$, and
    - Survival weighting at rate $\lambda$.

    The protection leg pays $(1-R)$ at the random default time $\tau$, weighted by $\lambda e^{-(r+\lambda)t}$ (the density of default at $t$, discounted). The premium leg pays at rate $s$ continuously, weighted by $e^{-(r+\lambda)t}$ (survival and discounting). Since the discount factor $e^{-rt}$ multiplies both the default density and the survival probability in the same way, the ratio depends only on $\lambda$, not on $r$. Economically, the risk-free rate determines how much we discount future cash flows, but since both the protection payment and premium payments are discounted by the same rate, the par spread---which equates the two legs---is insensitive to the level of rates.

---

**Exercise 3.** Suppose CDS spreads for maturities 1Y, 3Y, and 5Y are 50 bp, 80 bp, and 120 bp, respectively. Assuming $R = 40\%$ and piecewise-constant hazard rates, bootstrap the hazard rates $\lambda_1$ (for $[0,1]$), $\lambda_2$ (for $(1,3]$), and $\lambda_3$ (for $(3,5]$). Use a flat risk-free rate $r = 3\%$ and the simplified formula for each maturity.

??? success "Solution to Exercise 3"

    We are given CDS spreads: $s_1 = 50$ bp (1Y), $s_2 = 80$ bp (3Y), $s_3 = 120$ bp (5Y), with $R = 40\%$ and $r = 3\%$.

    We assume piecewise-constant hazard rates: $\lambda_1$ on $[0,1]$, $\lambda_2$ on $(1,3]$, $\lambda_3$ on $(3,5]$.

    **Step 1: Bootstrap $\lambda_1$ from the 1-year CDS.**

    For the 1-year CDS with constant hazard rate $\lambda_1$, using the simplified formula:

    $$
    s_1 = (1-R)\lambda_1 \implies \lambda_1 = \frac{s_1}{1-R} = \frac{0.0050}{0.60} = 0.00833 = 83.3 \text{ bp}
    $$

    The survival probability to year 1 is:

    $$
    S(0,1) = e^{-\lambda_1 \cdot 1} = e^{-0.00833} = 0.9917
    $$

    **Step 2: Bootstrap $\lambda_2$ from the 3-year CDS.**

    For the 3-year CDS, we need to solve for $\lambda_2$ such that the par spread equals 80 bp. Using the general pricing formula with annual payments at $t = 1, 2, 3$:

    **Protection leg:**

    $$
    \text{PV}_{\text{prot}} = (1-R) \left[\int_0^1 e^{-(r+\lambda_1)t} \lambda_1 \, dt + \int_1^3 e^{-rt} \lambda_2 S(0,1) e^{-\lambda_2(t-1)} \, dt\right]
    $$

    Using the simplified approach, the par spread formula gives:

    $$
    s_2 = \frac{(1-R) \left[\lambda_1 \int_0^1 e^{-(r+\lambda_1)t}\,dt + \lambda_2 S(0,1)\int_1^3 e^{-rt} e^{-\lambda_2(t-1)}\,dt\right]}{\int_0^1 e^{-(r+\lambda_1)t}\,dt + S(0,1)\int_1^3 e^{-rt} e^{-\lambda_2(t-1)}\,dt}
    $$

    For a practical approximation, note that if the flat hazard rate for the full 3-year period were $\bar{\lambda}_2$, we would have $s_2 = (1-R)\bar{\lambda}_2$, giving:

    $$
    \bar{\lambda}_2 = \frac{0.0080}{0.60} = 0.01333 = 133.3 \text{ bp}
    $$

    The average hazard rate over $[0,3]$ satisfies $\bar{\lambda}_2 \times 3 = \lambda_1 \times 1 + \lambda_2 \times 2$, so:

    $$
    \lambda_2 = \frac{3 \bar{\lambda}_2 - \lambda_1}{2} = \frac{3 \times 0.01333 - 0.00833}{2} = \frac{0.04000 - 0.00833}{2} = \frac{0.03167}{2} = 0.01583 = 158.3 \text{ bp}
    $$

    **Step 3: Bootstrap $\lambda_3$ from the 5-year CDS.**

    Similarly, $s_3 = (1-R)\bar{\lambda}_3$ gives the average hazard rate over $[0,5]$:

    $$
    \bar{\lambda}_3 = \frac{0.0120}{0.60} = 0.0200 = 200 \text{ bp}
    $$

    Using $\bar{\lambda}_3 \times 5 = \lambda_1 \times 1 + \lambda_2 \times 2 + \lambda_3 \times 2$:

    $$
    \lambda_3 = \frac{5 \times 0.0200 - 0.00833 - 2 \times 0.01583}{2} = \frac{0.1000 - 0.00833 - 0.03167}{2} = \frac{0.0600}{2} = 0.0300 = 300 \text{ bp}
    $$

    **Summary of bootstrapped hazard rates:**

    | Period | Hazard Rate |
    |--------|------------|
    | $[0, 1]$ | $\lambda_1 = 83.3$ bp |
    | $(1, 3]$ | $\lambda_2 = 158.3$ bp |
    | $(3, 5]$ | $\lambda_3 = 300.0$ bp |

    The increasing hazard rate curve reflects the upward-sloping CDS spread term structure, indicating that the market prices in increasing default risk over time.

---

**Exercise 4.** A trader observes that the 5-year CDS spread for a reference entity is 200 bp. With $R = 40\%$, the implied hazard rate is $\lambda = 333$ bp. If the recovery assumption is changed to $R = 30\%$, what is the new implied hazard rate? Discuss why the assumed recovery rate materially affects the calibrated hazard rate curve.

??? success "Solution to Exercise 4"

    **With $R = 40\%$:**

    $$
    \lambda = \frac{s}{1-R} = \frac{200 \text{ bp}}{1 - 0.40} = \frac{0.0200}{0.60} = 0.03333 = 333.3 \text{ bp}
    $$

    **With $R = 30\%$:**

    $$
    \lambda = \frac{s}{1-R} = \frac{200 \text{ bp}}{1 - 0.30} = \frac{0.0200}{0.70} = 0.02857 = 285.7 \text{ bp}
    $$

    The implied hazard rate drops from 333.3 bp to 285.7 bp---a decrease of about 14%---when the recovery assumption changes from 40% to 30%.

    **Why recovery materially affects calibrated hazard rates:** The CDS spread compensates for the expected loss rate, which is the product of the hazard rate and the loss given default:

    $$
    s \approx (1-R)\lambda
    $$

    This means $\lambda$ and $(1-R)$ are inversely related for a given spread. A higher recovery assumption means a smaller loss per default event, so the model needs a higher default frequency to justify the observed spread. Conversely, a lower recovery assumption implies larger losses per default, requiring fewer defaults (lower $\lambda$) to explain the same spread.

    This has practical implications: since recovery rates are difficult to estimate in advance, the calibrated hazard rate curve inherits significant uncertainty from the recovery assumption. Two analysts using different recovery rates will produce materially different survival probability curves and, consequently, different prices for non-standard credit products (e.g., digital CDS, CDO tranches).

---

**Exercise 5.** Explain why CDS bootstrapping is analogous to yield curve construction from swap rates. In particular, identify the analogues of: (a) the discount factors, (b) the forward rates, and (c) the par instruments used for calibration.

??? success "Solution to Exercise 5"

    **CDS bootstrapping** extracts a hazard rate term structure from CDS spreads of different maturities, much as **yield curve construction** extracts a forward rate curve from swap rates of different maturities. The analogy is:

    **(a) Discount factors $\leftrightarrow$ Survival probabilities:**

    In interest rate bootstrapping, we extract discount factors $D(0,t) = e^{-\int_0^t r_u \, du}$ that price risk-free cash flows. In CDS bootstrapping, we extract survival probabilities $S(0,t) = e^{-\int_0^t \lambda_u \, du}$ that describe the probability of no default by time $t$. Both are decreasing functions of maturity starting from 1.

    **(b) Forward rates $\leftrightarrow$ Forward (or piecewise) hazard rates:**

    In yield curve construction, the forward rate $f(t)$ is the instantaneous borrowing rate for the future period $[t, t+dt]$. In CDS bootstrapping, the hazard rate $\lambda(t)$ is the instantaneous conditional default rate for period $[t, t+dt]$ given survival to $t$. Both are recovered as derivatives of the cumulative curves: $f(t) = -\frac{d}{dt} \ln D(0,t)$ and $\lambda(t) = -\frac{d}{dt} \ln S(0,t)$.

    **(c) Par instruments used for calibration $\leftrightarrow$ Par CDS spreads:**

    In yield curve construction, par swap rates for standard maturities (2Y, 5Y, 10Y, etc.) serve as the calibration instruments. Each par swap rate embeds information about all discount factors up to its maturity. Similarly, par CDS spreads for standard maturities (1Y, 3Y, 5Y, 7Y, 10Y) are used to calibrate hazard rates. Each par CDS spread depends on all survival probabilities up to its maturity.

    In both cases, the bootstrap proceeds sequentially from short to long maturities: use the shortest-maturity instrument to determine the first segment of the curve, then use the next maturity instrument together with already-determined values to solve for the next segment, and so on.

---

**Exercise 6.** A corporate bond with 5-year maturity has a yield spread of 150 bp over the risk-free rate. The 5-year CDS spread for the same reference entity is 130 bp. Compute the CDS-bond basis. List three market frictions that could explain a persistent negative basis.

??? success "Solution to Exercise 6"

    **CDS-bond basis:**

    $$
    \text{Basis} = s_{\text{CDS}} - s_{\text{bond}} = 130 \text{ bp} - 150 \text{ bp} = -20 \text{ bp}
    $$

    The basis is **negative** at $-20$ bp, meaning CDS protection is cheaper than what the bond spread implies.

    **Three market frictions explaining a persistent negative basis:**

    1. **Funding costs:** Purchasing the corporate bond requires the investor to fund the position. If the investor's borrowing rate exceeds the risk-free rate, the effective cost of holding the bond increases, and the bond yield spread must compensate for this funding cost in addition to pure credit risk. CDS, being unfunded instruments (only margin or collateral is required), do not carry this additional funding cost. This drives bond spreads above CDS spreads.

    2. **Liquidity premium in bonds:** Corporate bonds, particularly off-the-run or smaller issues, may be illiquid. Investors demand a liquidity premium that widens bond spreads beyond pure default compensation. CDS on the same reference entity may be more liquid (especially for actively traded names), so CDS spreads reflect primarily default risk without a large liquidity component.

    3. **Balance sheet and regulatory constraints:** Banks and institutional investors holding corporate bonds must allocate regulatory capital against the credit exposure. This capital charge raises the effective cost of holding bonds, requiring wider bond spreads to attract buyers. CDS have different capital treatment and do not require full balance sheet funding, allowing them to trade at tighter spreads relative to bonds.
