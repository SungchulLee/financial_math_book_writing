# CDS Index and Tranches

**CDS indices** aggregate single-name credit default swaps into standardized, tradable portfolios, providing liquid exposure to broad credit markets. **Tranches** further slice the portfolio loss distribution into layers with different risk profiles, enabling investors to take targeted positions on default correlation. The interplay between index and tranche pricing reveals the market's view on systematic default risk and has profound implications for portfolio credit risk modeling.

---

## CDS Indices

### Major Index Families

The two principal CDS index families are:

- **CDX** (Credit Default Swap Index): North American reference entities
    - CDX.NA.IG: 125 investment-grade North American names
    - CDX.NA.HY: 100 high-yield North American names
- **iTraxx** (International Traxx): European and Asian reference entities
    - iTraxx Europe: 125 investment-grade European names
    - iTraxx Crossover: 50--75 sub-investment-grade European names

### Index Mechanics

A CDS index is a portfolio of equally weighted single-name CDS contracts:

- **Notional per name:** $N/n$ where $N$ is the total notional and $n$ is the number of names
- **Fixed coupon:** Standardized (e.g., 100 bp for IG, 500 bp for HY)
- **Upfront payment:** Compensates for the difference between par spread and fixed coupon
- **Maturity:** Standard 5-year (also 3, 7, 10 available)
- **Roll:** New series every 6 months (March and September for CDX)

### Index Spread

The **index spread** is the premium that equates the present value of premium and protection legs for the entire portfolio:

$$
s_{\text{index}} = \frac{\sum_{k=1}^n \text{PV}_{\text{prot}}^{(k)}}{\text{Risky Annuity}} = \frac{\sum_{k=1}^n (1-R_k) \int_0^T D(0,u) S_k(0,u) \lambda_k(u) \, du}{\sum_{i=1}^m \Delta_i D(0,t_i) \frac{1}{n}\sum_{k=1}^n S_k(0,t_i)}
$$

Under the simplifying assumption of homogeneous names:

$$
s_{\text{index}} \approx (1-R)\bar{\lambda}
$$

where $\bar{\lambda}$ is the average intensity.

!!! note "Index vs Average Single-Name Spread"
    The index spread is approximately equal to the **arithmetic average** of the constituent single-name CDS spreads, with small convexity adjustments.

---

## Portfolio Loss Distribution

### Loss Variable

For a portfolio of $n$ names, each with notional $1/n$ and recovery $R_k$, the **portfolio loss** at time $T$ is:

$$
L_T = \frac{1}{n}\sum_{k=1}^n (1 - R_k) \mathbf{1}_{\{\tau_k \le T\}}
$$

where $\tau_k$ is the default time of name $k$.

### Expected Loss

$$
\mathbb{E}[L_T] = \frac{1}{n}\sum_{k=1}^n (1-R_k) \mathbb{Q}(\tau_k \le T)
$$

For homogeneous portfolios with common recovery $R$ and default probability $p$:

$$
\mathbb{E}[L_T] = (1-R) p
$$

### The Role of Correlation

The **shape** of the loss distribution depends critically on default correlation:

- **Zero correlation:** Defaults are independent. By the law of large numbers, portfolio loss concentrates around its mean. Thin tails.
- **Perfect correlation:** All names default together or survive together. The distribution is bimodal (either zero loss or total loss).
- **Moderate correlation:** Intermediate behavior. Heavier tails than the independent case, reflecting systematic risk.

Default correlation is the key parameter that drives tranche pricing.

---

## Tranche Structure

### Definition

A **tranche** on a credit portfolio is defined by an attachment point $a$ and a detachment point $d$ (with $0 \le a < d \le 1$):

$$
L_T^{[a,d]} = \frac{[\min(L_T, d) - \min(L_T, a)]^+}{d - a} = \frac{(L_T - a)^+ - (L_T - d)^+}{d - a}
$$

This is the loss absorbed by the tranche as a fraction of its notional $(d-a)$.

### Standard CDX Tranches (Investment Grade)

| Tranche | Attachment | Detachment | Risk Profile |
|---------|-----------|------------|-------------|
| Equity | 0% | 3% | First loss, highest risk |
| Mezzanine Junior | 3% | 7% | Second loss |
| Mezzanine Senior | 7% | 10% | |
| Senior | 10% | 15% | |
| Super Senior | 15% | 30% (or 100%) | Last loss, lowest risk |

### Tranche Loss

For a tranche $[a,d]$, the tranche loss fraction is:

$$
L^{[a,d]}_T = \frac{1}{d-a}\left[\min(L_T, d) - a\right]^+
$$

- If $L_T \le a$: No tranche loss (losses absorbed by subordinate tranches)
- If $a < L_T < d$: Partial tranche loss $(L_T - a)/(d-a)$
- If $L_T \ge d$: Total tranche wipeout ($L^{[a,d]}_T = 1$)

---

## Tranche Pricing

### Expected Tranche Loss

The key quantity for tranche pricing is the **expected tranche loss**:

$$
\text{ETL}(T) = \mathbb{E}^{\mathbb{Q}}[L^{[a,d]}_T] = \frac{\mathbb{E}[(L_T - a)^+] - \mathbb{E}[(L_T - d)^+]}{d - a}
$$

This can be expressed using the **call spread** on portfolio loss:

$$
\text{ETL}(T) = \frac{C(a, T) - C(d, T)}{d - a}
$$

where $C(K, T) = \mathbb{E}[(L_T - K)^+]$ is the portfolio loss call function.

### Tranche Premium Leg

$$
\text{PV}_{\text{prem}}^{[a,d]} = s^{[a,d]} \sum_{i=1}^m \Delta_i D(0, t_i)\left[1 - \text{ETL}(t_i)\right](d-a)
$$

The factor $[1 - \text{ETL}(t_i)]$ is the surviving tranche notional at each payment date.

### Tranche Protection Leg

$$
\text{PV}_{\text{prot}}^{[a,d]} = \int_0^T D(0,u) \, d\mathbb{E}[\text{Tranche Loss}_u] \cdot (d-a)
$$

Discretizing:

$$
\text{PV}_{\text{prot}}^{[a,d]} \approx (d-a)\sum_{i=1}^m D(0, t_i)\left[\text{ETL}(t_i) - \text{ETL}(t_{i-1})\right]
$$

### Par Tranche Spread

$$
s^{[a,d]} = \frac{\text{PV}_{\text{prot}}^{[a,d]}}{\text{PV}_{\text{prem}}^{[a,d]} / s^{[a,d]}} = \frac{\sum_i D(0,t_i)[\text{ETL}(t_i) - \text{ETL}(t_{i-1})]}{\sum_i \Delta_i D(0,t_i)[1 - \text{ETL}(t_i)]}
$$

!!! note "Equity Tranche Convention"
    The equity tranche (0--3%) trades with a fixed running spread of 500 bp plus an upfront payment. The upfront reflects the high expected loss of the first-loss piece.

---

## The Gaussian Copula Model

### One-Factor Model

The standard market model for tranche pricing is the **one-factor Gaussian copula** (Li, 2000):

For each name $k = 1, \ldots, n$, define:

$$
X_k = \sqrt{\rho} \, M + \sqrt{1-\rho} \, Z_k
$$

where:

- $M \sim \mathcal{N}(0,1)$: **systematic factor** (common to all names)
- $Z_k \sim \mathcal{N}(0,1)$: **idiosyncratic factor** (specific to name $k$)
- $M, Z_1, \ldots, Z_n$: mutually independent
- $\rho \in [0,1]$: **asset correlation** parameter

Name $k$ defaults by time $T$ if and only if:

$$
X_k \le C_k := N^{-1}(p_k)
$$

where $p_k = \mathbb{Q}(\tau_k \le T)$ is the marginal default probability.

### Conditional Independence

Given $M = m$, defaults are **conditionally independent**:

$$
\mathbb{Q}(\tau_k \le T \mid M = m) = N\left(\frac{C_k - \sqrt{\rho} \, m}{\sqrt{1-\rho}}\right) =: p_k(m)
$$

### Conditional Loss Distribution

Given $M = m$, the number of defaults follows a (conditionally) binomial distribution for homogeneous portfolios:

$$
\mathbb{Q}(L_T \le x \mid M = m) = \sum_{j=0}^{\lfloor nx/(1-R) \rfloor} \binom{n}{j} p(m)^j (1-p(m))^{n-j}
$$

For large $n$, by the law of large numbers: $L_T \mid M = m \approx (1-R) p(m)$.

### Unconditional Loss Distribution

Integrating over $M$:

$$
\mathbb{Q}(L_T \le x) = \int_{-\infty}^{\infty} \mathbb{Q}(L_T \le x \mid M = m) \, \phi(m) \, dm
$$

For the large-pool approximation:

$$
\mathbb{Q}(L_T \le x) = N\left(\frac{\sqrt{1-\rho} \, N^{-1}\left(\frac{x}{1-R}\right) - N^{-1}(p)}{\sqrt{\rho}}\right)
$$

This is the **Vasicek large-pool formula**, widely used for tranche pricing.

---

## Correlation and Tranche Sensitivity

### Effect of Correlation on Tranches

Correlation has opposite effects on different tranches:

**Higher correlation ($\rho \uparrow$):**

- Equity tranche (0--3%): **Spread decreases.** More probability mass moves to the tails, but the equity tranche is already likely to be hit. Higher correlation means more scenarios with zero loss (all survive), benefiting equity.
- Senior tranche (15--30%): **Spread increases.** Higher correlation pushes more probability into the extreme loss tail, increasing the chance of large losses reaching senior tranches.

**Lower correlation ($\rho \downarrow$):**

- Equity tranche: **Spread increases.** More idiosyncratic defaults accumulate predictably.
- Senior tranche: **Spread decreases.** Less chance of many simultaneous defaults.

### The Correlation Smile

When one calibrates the Gaussian copula model to each tranche separately, one obtains a different **implied correlation** for each tranche:

| Tranche | Implied Correlation |
|---------|-------------------|
| Equity (0--3%) | Low (10--20%) |
| Mezzanine (3--7%) | Higher (20--35%) |
| Senior (7--10%) | Even higher |
| Super Senior (10%+) | Highest (50--70%) |

This **correlation smile** (or skew) indicates that the single-parameter Gaussian copula model is misspecified. The market prices in heavier tails than the Gaussian copula generates.

---

## Base Correlation

### Motivation

The implied correlation smile makes quoting and interpolation difficult because compound correlations are not monotone and can be multi-valued. **Base correlation** resolves this by re-parametrizing the smile.

### Definition

The **base correlation** $\rho_b(K)$ for a given detachment point $K$ is the single correlation parameter that, when used in the Gaussian copula model applied to the equity tranche $[0, K]$, reproduces the market price:

$$
\text{ETL}_{\text{model}}^{[0,K]}(\rho_b(K)) = \text{ETL}_{\text{market}}^{[0,K]}
$$

### Properties

- Base correlation is a **monotonically increasing** function of $K$
- It is well-defined and unique for each detachment point
- It provides a convenient quoting convention and interpolation scheme
- Non-standard tranches are priced by interpolating the base correlation curve

### Construction from Tranche Quotes

1. From the equity tranche (0--3%) quote, find $\rho_b(3\%)$ directly
2. From the 3--7% tranche quote, compute the expected loss of the 0--7% tranche:

$$
\text{ETL}^{[0,7\%]} = \frac{3\%}{7\%}\text{ETL}^{[0,3\%]} + \frac{4\%}{7\%}\text{ETL}^{[3\%,7\%]}
$$

3. Find $\rho_b(7\%)$ such that the Gaussian copula model with correlation $\rho_b(7\%)$ matches $\text{ETL}^{[0,7\%]}$
4. Continue for each successive detachment point

---

## Index-Tranche Arbitrage Constraint

### Consistency

The sum of all tranche losses must equal the index loss:

$$
\sum_j (d_j - a_j) L_T^{[a_j, d_j]} = L_T
$$

This implies:

$$
\sum_j (d_j - a_j) \text{ETL}^{[a_j, d_j]}(T) = \mathbb{E}[L_T]
$$

The index spread pins down $\mathbb{E}[L_T]$, constraining the tranche pricing.

### No-Arbitrage Conditions

For any loss distribution $F_L$:

1. $\text{ETL}^{[0,K]}$ must be non-negative and non-decreasing in $K$
2. $d/dK \, \text{ETL}^{[0,K]} = [1 - F_L(K)]/(K)$ must be non-negative
3. Tranche expected losses must be consistent with the total expected loss

Violations of these conditions indicate arbitrage opportunities or model misspecification.

---

## Numerical Example

**Setup:** Homogeneous portfolio with $n = 125$ names, $p = 2\%$ (5Y default probability), $R = 40\%$, flat correlation $\rho = 20\%$, $r = 3\%$.

**Step 1: Expected portfolio loss**

$$
\mathbb{E}[L_5] = (1-R) p = 0.6 \times 0.02 = 1.2\%
$$

**Step 2: Large-pool loss distribution (Vasicek)**

$$
\mathbb{Q}(L_5 \le x) = N\left(\frac{\sqrt{0.8} \, N^{-1}(x/0.6) - N^{-1}(0.02)}{\sqrt{0.2}}\right)
$$

For $x = 3\%$: $N^{-1}(0.05) = -1.645$, $N^{-1}(0.02) = -2.054$

$$
\mathbb{Q}(L_5 \le 0.03) = N\left(\frac{0.894 \times (-1.645) - (-2.054)}{0.447}\right) = N\left(\frac{-1.471 + 2.054}{0.447}\right) = N(1.304) = 0.904
$$

**Step 3: Expected tranche losses**

Equity (0--3%):

$$
\text{ETL}^{[0,3\%]} = \frac{\mathbb{E}[\min(L_5, 3\%)]}{3\%} \approx \frac{1.15\%}{3\%} = 38.3\%
$$

(Almost all expected loss is absorbed by the equity tranche.)

Senior (15--30%):

$$
\text{ETL}^{[15\%,30\%]} \approx \frac{0.01\%}{15\%} = 0.07\%
$$

**Step 4: Approximate tranche spreads**

Equity: $s^{[0,3\%]} \approx 38.3\% / 4.5 \approx 2130$ bp (pays 500 bp running + large upfront)

Senior: $s^{[15\%,30\%]} \approx 0.07\% / 4.5 \approx 2$ bp

This demonstrates the extreme dispersion of credit risk across the capital structure.

---

## Key Takeaways

- CDS indices (CDX, iTraxx) provide liquid, standardized exposure to portfolio credit risk
- Tranches slice the loss distribution by attachment/detachment points, creating different risk-return profiles
- The Gaussian copula model prices tranches via conditionally independent defaults driven by a common factor
- Correlation has opposite effects on equity vs senior tranches
- The implied correlation smile reveals model misspecification; base correlation provides a monotone quoting convention
- Equity tranches are short correlation; senior tranches are long correlation
- Index-tranche consistency constrains the loss distribution and prevents arbitrage

---

## Further Reading

- Li, D. X. (2000). On default correlation: A copula function approach. *Journal of Fixed Income*, 9(4), 43--54.
- O'Kane, D. (2008). *Modelling Single-name and Multi-name Credit Derivatives*. Wiley, Chapters 14--18.
- McGinty, L., et al. (2004). Credit correlation: A guide. *JP Morgan Credit Derivatives Research*.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 14.

---

## Exercises

**Exercise 1.** Consider a homogeneous portfolio of $n = 125$ equally weighted names, each with 5-year default probability $p = 3\%$ and recovery rate $R = 40\%$. Compute the expected portfolio loss $\mathbb{E}[L_5]$. Determine the fraction of this expected loss that is absorbed by the equity tranche $[0\%, 3\%]$, assuming the entire expected loss falls below the equity detachment point.

??? success "Solution to Exercise 1"

    **Expected portfolio loss:**

    $$
    \mathbb{E}[L_5] = (1-R) \cdot p = (1 - 0.40) \times 0.03 = 0.60 \times 0.03 = 0.018 = 1.8\%
    $$

    **Fraction absorbed by the equity tranche $[0\%, 3\%]$:**

    The equity tranche absorbs all losses up to 3% of the portfolio notional. Since the expected loss of 1.8% is entirely below the equity detachment point of 3%, the equity tranche absorbs virtually all of the expected loss (under the assumption stated in the problem).

    More precisely, the expected tranche loss for the equity piece is:

    $$
    \text{ETL}^{[0,3\%]} = \frac{\mathbb{E}[\min(L_5, 3\%)]}{3\%}
    $$

    If the entire expected loss falls below the 3% detachment point---meaning that $\mathbb{E}[\min(L_5, 3\%)] \approx \mathbb{E}[L_5] = 1.8\%$---then:

    $$
    \text{ETL}^{[0,3\%]} \approx \frac{1.8\%}{3\%} = 60\%
    $$

    The equity tranche absorbs:

    $$
    3\% \times 60\% = 1.8\% = \mathbb{E}[L_5]
    $$

    That is, **100%** of the expected portfolio loss is absorbed by the equity tranche. The fraction absorbed by equity is $1.8\% / 1.8\% = 1$, confirming that all expected loss falls on the first-loss piece.

    Note: In reality, some probability mass of $L_5$ exceeds 3%, so $\mathbb{E}[\min(L_5, 3\%)]$ is slightly less than $\mathbb{E}[L_5]$, and a tiny fraction of expected loss leaks into the mezzanine tranche. However, for the typical parameters here, this effect is negligible.

---

**Exercise 2.** In the one-factor Gaussian copula model with correlation $\rho$, the conditional default probability given the systematic factor $M = m$ is

$$
p(m) = N\!\left(\frac{N^{-1}(p) - \sqrt{\rho}\, m}{\sqrt{1-\rho}}\right)
$$

For $p = 2\%$ and $\rho = 0.3$, compute $p(m)$ for $m \in \{-2, -1, 0, 1, 2\}$. Plot or describe how the conditional default probability varies with the systematic factor and explain the economic interpretation.

??? success "Solution to Exercise 2"

    The conditional default probability is:

    $$
    p(m) = N\!\left(\frac{N^{-1}(p) - \sqrt{\rho}\, m}{\sqrt{1-\rho}}\right)
    $$

    With $p = 2\%$ and $\rho = 0.3$:

    - $N^{-1}(0.02) = -2.054$
    - $\sqrt{\rho} = \sqrt{0.3} = 0.5477$
    - $\sqrt{1-\rho} = \sqrt{0.7} = 0.8367$

    So:

    $$
    p(m) = N\!\left(\frac{-2.054 - 0.5477 \, m}{0.8367}\right)
    $$

    Computing for each value of $m$:

    **$m = -2$:**

    $$
    p(-2) = N\!\left(\frac{-2.054 + 1.095}{0.8367}\right) = N\!\left(\frac{-0.959}{0.8367}\right) = N(-1.146) = 0.1259 = 12.6\%
    $$

    **$m = -1$:**

    $$
    p(-1) = N\!\left(\frac{-2.054 + 0.5477}{0.8367}\right) = N\!\left(\frac{-1.506}{0.8367}\right) = N(-1.800) = 0.0359 = 3.6\%
    $$

    **$m = 0$:**

    $$
    p(0) = N\!\left(\frac{-2.054}{0.8367}\right) = N(-2.455) = 0.0071 = 0.71\%
    $$

    **$m = 1$:**

    $$
    p(1) = N\!\left(\frac{-2.054 - 0.5477}{0.8367}\right) = N\!\left(\frac{-2.602}{0.8367}\right) = N(-3.110) = 0.0009 = 0.09\%
    $$

    **$m = 2$:**

    $$
    p(2) = N\!\left(\frac{-2.054 - 1.095}{0.8367}\right) = N\!\left(\frac{-3.149}{0.8367}\right) = N(-3.764) \approx 0.00008 = 0.008\%
    $$

    **Summary:**

    | $m$ | $p(m)$ |
    |-----|--------|
    | $-2$ | 12.6% |
    | $-1$ | 3.6% |
    | $0$ | 0.71% |
    | $1$ | 0.09% |
    | $2$ | 0.008% |

    **Economic interpretation:** The systematic factor $M$ represents the state of the economy. A negative $m$ (bad economic state) dramatically increases conditional default probabilities: at $m = -2$ (a 2-standard-deviation adverse shock), the default probability jumps to 12.6%---more than 6 times the unconditional $p = 2\%$. Conversely, a positive $m$ (good economic state) makes defaults very unlikely: at $m = 2$, the conditional default probability is nearly zero.

    This captures the key feature of credit risk: defaults are rare in good times but cluster during recessions, driven by the common factor. The correlation parameter $\rho = 0.3$ determines how sensitive individual defaults are to the common factor.

---

**Exercise 3.** Using the Vasicek large-pool approximation

$$
\mathbb{Q}(L_T \le x) = N\!\left(\frac{\sqrt{1-\rho}\, N^{-1}\!\left(\frac{x}{1-R}\right) - N^{-1}(p)}{\sqrt{\rho}}\right)
$$

with $p = 2\%$, $R = 40\%$, and $\rho = 20\%$, compute $\mathbb{Q}(L_5 \le 7\%)$ and $\mathbb{Q}(L_5 \le 15\%)$. Use these to estimate the probability that losses reach the mezzanine and senior tranches.

??? success "Solution to Exercise 3"

    Using the Vasicek large-pool formula:

    $$
    \mathbb{Q}(L_T \le x) = N\!\left(\frac{\sqrt{1-\rho}\, N^{-1}\!\left(\frac{x}{1-R}\right) - N^{-1}(p)}{\sqrt{\rho}}\right)
    $$

    with $p = 0.02$, $R = 0.40$, $\rho = 0.20$.

    Key quantities: $\sqrt{1-\rho} = \sqrt{0.8} = 0.8944$, $\sqrt{\rho} = \sqrt{0.2} = 0.4472$, $N^{-1}(0.02) = -2.054$.

    **Computing $\mathbb{Q}(L_5 \le 7\%)$:**

    $$
    \frac{x}{1-R} = \frac{0.07}{0.60} = 0.11667
    $$

    $$
    N^{-1}(0.11667) = -1.191
    $$

    $$
    \mathbb{Q}(L_5 \le 0.07) = N\!\left(\frac{0.8944 \times (-1.191) - (-2.054)}{0.4472}\right) = N\!\left(\frac{-1.065 + 2.054}{0.4472}\right) = N\!\left(\frac{0.989}{0.4472}\right) = N(2.211)
    $$

    $$
    \mathbb{Q}(L_5 \le 7\%) = N(2.211) = 0.9865 = 98.65\%
    $$

    **Computing $\mathbb{Q}(L_5 \le 15\%)$:**

    $$
    \frac{x}{1-R} = \frac{0.15}{0.60} = 0.25
    $$

    $$
    N^{-1}(0.25) = -0.6745
    $$

    $$
    \mathbb{Q}(L_5 \le 0.15) = N\!\left(\frac{0.8944 \times (-0.6745) - (-2.054)}{0.4472}\right) = N\!\left(\frac{-0.6032 + 2.054}{0.4472}\right) = N\!\left(\frac{1.451}{0.4472}\right) = N(3.244)
    $$

    $$
    \mathbb{Q}(L_5 \le 15\%) = N(3.244) = 0.9994 = 99.94\%
    $$

    **Probabilities that losses reach higher tranches:**

    - Probability that losses exceed 7% (reach the mezzanine senior tranche): $1 - 0.9865 = 1.35\%$
    - Probability that losses exceed 15% (reach the super senior tranche): $1 - 0.9994 = 0.06\%$

    These very small tail probabilities explain why senior and super senior tranches trade at very tight spreads---the probability of losses reaching them is extremely low under this model. However, the 2008 financial crisis demonstrated that these tail probabilities can be dramatically underestimated by the Gaussian copula.

---

**Exercise 4.** A standard CDX tranche has attachment $a = 3\%$ and detachment $d = 7\%$. The expected portfolio losses at the detachment points are $\mathbb{E}[(L_T - 0.03)^+] = 0.45\%$ and $\mathbb{E}[(L_T - 0.07)^+] = 0.10\%$. Compute the expected tranche loss

$$
\text{ETL}^{[3\%,7\%]} = \frac{\mathbb{E}[(L_T - 0.03)^+] - \mathbb{E}[(L_T - 0.07)^+]}{d - a}
$$

and the approximate par tranche spread assuming a risky annuity of 4.3 years.

??? success "Solution to Exercise 4"

    **Expected tranche loss for $[3\%, 7\%]$:**

    $$
    \text{ETL}^{[3\%,7\%]} = \frac{\mathbb{E}[(L_T - 0.03)^+] - \mathbb{E}[(L_T - 0.07)^+]}{d - a} = \frac{0.0045 - 0.0010}{0.07 - 0.03} = \frac{0.0035}{0.04} = 0.0875 = 8.75\%
    $$

    **Approximate par tranche spread:**

    The par tranche spread equates the protection and premium legs. Using the approximation:

    $$
    s^{[3\%,7\%]} \approx \frac{\text{ETL}^{[3\%,7\%]}}{\text{Risky Annuity}} = \frac{0.0875}{4.3} = 0.02035 = 203.5 \text{ bp}
    $$

    More precisely, the risky annuity for the tranche should account for the surviving tranche notional $[1 - \text{ETL}(t_i)]$ at each payment date, but the simple ratio gives a reasonable first approximation.

    This 203.5 bp spread is significantly higher than a typical index spread (which reflects the average credit risk of the portfolio), because the mezzanine tranche concentrates credit risk: it absorbs losses only after the equity tranche is exhausted but before the senior tranches are touched, making it sensitive to scenarios with moderate numbers of defaults.

---

**Exercise 5.** Explain qualitatively why increasing the default correlation $\rho$ decreases the equity tranche spread but increases the super senior tranche spread. Illustrate your argument by describing the shape of the portfolio loss distribution for $\rho = 0$, $\rho = 0.3$, and $\rho = 1$.

??? success "Solution to Exercise 5"

    **Effect of correlation on the portfolio loss distribution:**

    **$\rho = 0$ (independent defaults):** Each name defaults independently with probability $p$. By the law of large numbers (with $n = 125$ names), the portfolio loss is tightly concentrated around its mean $(1-R)p$. The distribution has a sharp peak near the expected loss with very thin tails. Almost all probability mass is near the mean; extreme losses are virtually impossible.

    **$\rho = 0.3$ (moderate correlation):** Defaults are linked through the common factor $M$. When $M$ takes adverse values, many names have elevated default probabilities simultaneously. This spreads out the loss distribution: the peak near the mean is lower and flatter, and the tails become heavier. There is meaningful probability of both very low losses (good scenarios where few names default) and very high losses (bad scenarios where many default together).

    **$\rho = 1$ (perfect correlation):** All names are driven entirely by the common factor, so either all default together or none do. The loss distribution is bimodal: with probability $(1-p)$ the loss is zero, and with probability $p$ the loss is $(1-R) = 60\%$. There is no probability mass at intermediate loss levels.

    **Impact on equity tranche ($[0, 3\%]$):**

    As $\rho$ increases from 0 to 1, the probability of zero or near-zero losses increases (more scenarios where the economy is good and no one defaults). Since the equity tranche is the first loss piece, it benefits from the increased probability of zero loss. The expected equity tranche loss decreases, so the equity spread decreases.

    At $\rho = 0$, the loss distribution is tightly concentrated around the mean (1.8%), which is within the equity tranche. The equity tranche is almost certain to suffer some loss. At $\rho = 1$, either there are no losses (probability 98%) or total loss (probability 2%), so the equity tranche has a 98% chance of zero loss.

    **Impact on super senior tranche ($[15\%, 30\%]$):**

    As $\rho$ increases, the tail of the loss distribution becomes heavier---there is more probability of extreme losses. The super senior tranche is only hit when portfolio losses exceed 15%, which requires a large number of simultaneous defaults. Higher correlation makes such clustered defaults more likely, increasing the expected loss of the super senior tranche and hence its spread.

    At $\rho = 0$, losses above 15% are essentially impossible (the loss concentrates near 1.8%). At $\rho = 1$, losses of 60% occur with probability 2%, which easily wipes out the super senior tranche.

    In summary: **equity tranches are short correlation** (they benefit from diversification) while **senior tranches are long correlation** (they are exposed to systematic risk).

---

**Exercise 6.** Suppose the market quotes the following base correlations: $\rho_b(3\%) = 15\%$, $\rho_b(7\%) = 25\%$, $\rho_b(10\%) = 35\%$. You wish to price a non-standard tranche with detachment point $K = 5\%$. Describe the interpolation procedure using the base correlation curve. What assumption about the loss distribution does this procedure implicitly make, and what is the main weakness?

??? success "Solution to Exercise 6"

    **Interpolation procedure:**

    To price a non-standard tranche with detachment point $K = 5\%$, we need the base correlation $\rho_b(5\%)$, which is not directly quoted. The steps are:

    1. **Build the base correlation curve** from the quoted points: $\rho_b(3\%) = 15\%$, $\rho_b(7\%) = 25\%$, $\rho_b(10\%) = 35\%$.

    2. **Interpolate** $\rho_b(5\%)$ between the known points $\rho_b(3\%) = 15\%$ and $\rho_b(7\%) = 25\%$. Using linear interpolation:

        $$
        \rho_b(5\%) = \rho_b(3\%) + \frac{5\% - 3\%}{7\% - 3\%} \times (\rho_b(7\%) - \rho_b(3\%))
        $$

        $$
        = 15\% + \frac{2\%}{4\%} \times (25\% - 15\%) = 15\% + 0.5 \times 10\% = 20\%
        $$

    3. **Price the equity tranche $[0, 5\%]$** using the Gaussian copula model with correlation $\rho_b(5\%) = 20\%$. This gives $\text{ETL}^{[0,5\%]}$.

    4. **Price a non-standard mezzanine tranche $[5\%, K_2]$** by computing:

        $$
        \text{ETL}^{[5\%, K_2]} = \frac{K_2 \cdot \text{ETL}^{[0,K_2]}(\rho_b(K_2)) - 5\% \cdot \text{ETL}^{[0,5\%]}(\rho_b(5\%))}{K_2 - 5\%}
        $$

    **Implicit assumption:** The base correlation framework assumes that a single Gaussian copula model (with a single correlation parameter) correctly prices each equity tranche $[0, K]$. Different detachment points use different correlations, which means the model is not internally consistent---there is no single loss distribution that simultaneously reproduces all base correlations.

    **Main weakness:** Because each equity tranche $[0, K]$ is priced with a different correlation, the implied loss distributions for overlapping equity tranches are inconsistent. When computing the loss for a mezzanine tranche $[a, d]$ as the difference of two equity tranches $[0, d]$ and $[0, a]$, each uses a different loss distribution. This can produce:

    - Negative tranche expected losses (arbitrage violation) in some cases
    - Inconsistency in hedging: the Greeks computed from the base correlation approach may not aggregate correctly
    - Interpolation sensitivity: the choice of interpolation method (linear, cubic spline, etc.) can materially affect non-standard tranche prices

---

**Exercise 7.** Prove the index-tranche arbitrage constraint: if the portfolio loss $L_T$ is partitioned into tranches $[a_j, d_j]$ for $j = 1, \ldots, J$ with $a_1 = 0$, $d_J = 1$, and $a_{j+1} = d_j$, then

$$
\sum_{j=1}^{J} (d_j - a_j)\, \text{ETL}^{[a_j, d_j]}(T) = \mathbb{E}[L_T]
$$

Starting from the definition $L_T^{[a,d]} = \frac{(L_T - a)^+ - (L_T - d)^+}{d - a}$, show that the tranche losses telescope to recover $L_T$.

??? success "Solution to Exercise 7"

    **Setup:** We have tranches $[a_j, d_j]$ for $j = 1, \ldots, J$ with $a_1 = 0$, $d_J = 1$, and $a_{j+1} = d_j$. The tranche loss is:

    $$
    L_T^{[a_j, d_j]} = \frac{(L_T - a_j)^+ - (L_T - d_j)^+}{d_j - a_j}
    $$

    **Proof:** We compute the weighted sum of tranche losses:

    $$
    \sum_{j=1}^{J} (d_j - a_j) \, L_T^{[a_j, d_j]} = \sum_{j=1}^{J} (d_j - a_j) \cdot \frac{(L_T - a_j)^+ - (L_T - d_j)^+}{d_j - a_j}
    $$

    The $(d_j - a_j)$ factors cancel:

    $$
    = \sum_{j=1}^{J} \left[(L_T - a_j)^+ - (L_T - d_j)^+\right]
    $$

    Writing out the sum explicitly and using $a_{j+1} = d_j$:

    $$
    = \left[(L_T - a_1)^+ - (L_T - d_1)^+\right] + \left[(L_T - a_2)^+ - (L_T - d_2)^+\right] + \cdots + \left[(L_T - a_J)^+ - (L_T - d_J)^+\right]
    $$

    Since $d_j = a_{j+1}$, the terms telescope:

    $$
    = (L_T - a_1)^+ - (L_T - d_J)^+
    $$

    Now use the boundary conditions $a_1 = 0$ and $d_J = 1$:

    - $(L_T - a_1)^+ = (L_T - 0)^+ = L_T^+ = L_T$ since $L_T \ge 0$
    - $(L_T - d_J)^+ = (L_T - 1)^+ = 0$ since $L_T \le 1$ (portfolio loss cannot exceed 100%)

    Therefore:

    $$
    \sum_{j=1}^{J} (d_j - a_j) \, L_T^{[a_j, d_j]} = L_T
    $$

    Taking expectations on both sides:

    $$
    \sum_{j=1}^{J} (d_j - a_j) \, \text{ETL}^{[a_j, d_j]}(T) = \mathbb{E}[L_T]
    $$

    This is the **index-tranche arbitrage constraint**: the notional-weighted sum of tranche expected losses must equal the total expected portfolio loss. This constraint ensures that tranche prices are consistent with the index spread, and any violation indicates an arbitrage opportunity or model misspecification. $\blacksquare$
