# Risk-Neutral vs Physical Intensities


In credit risk modeling, default intensities differ under the **risk-neutral measure** $\mathbb{Q}$ and the **physical measure** $\mathbb{P}$. Understanding this distinction is essential for interpreting calibrated parameters.

---

## Two measures, two roles


- **Physical measure $\mathbb{P}$:**
  governs real-world default frequencies and risk management.
- **Risk-neutral measure $\mathbb{Q}$:**
  governs pricing and is inferred from market instruments (e.g. CDS).

The two intensities generally differ due to risk premia.

---

## Intensity decomposition


A common representation is

$$
\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \text{credit risk premium}
$$



The premium compensates investors for bearing default risk.

---

## Empirical implications


Empirically:
- $\lambda^{\mathbb{Q}}$ implied from CDS is typically higher,
- historical default frequencies underestimate market-implied risk,
- stress periods amplify the gap.

Thus, CDS-implied intensities should not be interpreted as real default probabilities.

---

## Modeling approaches


Common approaches include:
- specifying $\lambda^{\mathbb{P}}$ and adding a market price of risk,
- directly modeling $\lambda^{\mathbb{Q}}$ for pricing,
- joint estimation using market and historical data.

---

## Key takeaways


- Risk-neutral and physical intensities differ.
- The gap reflects default risk premia.
- Measure consistency is crucial for interpretation.

---

## Further reading


- Duffie & Singleton, risk premia in credit.
- Bielecki & Rutkowski, measure changes in credit models.

---

## Exercises

**Exercise 1.** A firm has a physical default intensity of $\lambda^{\mathbb{P}} = 1.5\%$ per year. The 5-year CDS spread implies a risk-neutral intensity of $\lambda^{\mathbb{Q}} = 4.0\%$ (assuming 40% recovery). Compute the credit risk premium $\theta = \lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}}$ and interpret its economic meaning. Calculate the ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ and discuss what it reveals about investor risk aversion.

??? success "Solution to Exercise 1"
    **Credit risk premium:**

    $$
    \theta = \lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}} = 4.0\% - 1.5\% = 2.5\% \text{ per year}
    $$

    **Economic interpretation:** The credit risk premium of 2.5% per year represents the additional intensity that the market demands beyond the actuarial (physical) default rate. It compensates investors for:

    - **Systematic risk:** Default events are correlated with market downturns, when marginal utility of wealth is high
    - **Illiquidity:** Credit instruments are less liquid than risk-free bonds
    - **Model uncertainty:** Investors demand a buffer for estimation error in default probabilities
    - **Tail risk:** Extreme loss scenarios receive disproportionate weight

    **Risk premium ratio:**

    $$
    \frac{\lambda^{\mathbb{Q}}}{\lambda^{\mathbb{P}}} = \frac{4.0\%}{1.5\%} \approx 2.67
    $$

    This means the market prices default risk at approximately 2.67 times the actuarial rate. This ratio is consistent with empirical findings in the literature, where risk-neutral intensities are typically 2 to 4 times physical intensities for investment-grade firms. The ratio reveals substantial risk aversion: investors behave as if defaults are 2.67 times more likely than historical experience suggests.

    A high ratio indicates either elevated systematic risk (defaults correlated with market factors) or high market risk aversion. During crises, this ratio can spike to 5--10x, reflecting a flight to quality.

---

**Exercise 2.** Suppose the physical survival probability over $[0, T]$ is $S^{\mathbb{P}}(T) = e^{-\lambda^{\mathbb{P}} T}$ and the risk-neutral survival probability is $S^{\mathbb{Q}}(T) = e^{-\lambda^{\mathbb{Q}} T}$. For $\lambda^{\mathbb{P}} = 2\%$ and $\lambda^{\mathbb{Q}} = 5\%$, compute both survival probabilities at $T = 1, 3, 5, 10$ years. Plot or tabulate the results and discuss how the gap widens with maturity.

??? success "Solution to Exercise 2"
    **Survival probabilities:** With constant intensities $\lambda^{\mathbb{P}} = 0.02$ and $\lambda^{\mathbb{Q}} = 0.05$:

    | $T$ (years) | $S^{\mathbb{P}}(T) = e^{-0.02T}$ | $S^{\mathbb{Q}}(T) = e^{-0.05T}$ | Gap |
    |:-----------:|:---------------------------------:|:---------------------------------:|:---:|
    | 1 | 0.9802 | 0.9512 | 0.0290 |
    | 3 | 0.9418 | 0.8607 | 0.0811 |
    | 5 | 0.9048 | 0.7788 | 0.1260 |
    | 10 | 0.8187 | 0.6065 | 0.2122 |

    **The gap widens with maturity because:**

    The survival probabilities are exponential functions of the intensity times maturity. The difference is:

    $$
    S^{\mathbb{P}}(T) - S^{\mathbb{Q}}(T) = e^{-\lambda^{\mathbb{P}} T} - e^{-\lambda^{\mathbb{Q}} T}
    $$

    Taking the derivative with respect to $T$:

    $$
    \frac{d}{dT}\left[S^{\mathbb{P}}(T) - S^{\mathbb{Q}}(T)\right] = -\lambda^{\mathbb{P}} e^{-\lambda^{\mathbb{P}} T} + \lambda^{\mathbb{Q}} e^{-\lambda^{\mathbb{Q}} T}
    $$

    At $T = 0$, this equals $\lambda^{\mathbb{Q}} - \lambda^{\mathbb{P}} = 0.03 > 0$, so the gap is initially increasing. It continues to grow for moderate maturities before eventually shrinking as both probabilities converge to zero. For typical credit parameters, the gap is widening throughout the practically relevant maturity range (1--10 years).

    The widening gap has practical consequences: the discrepancy between market-implied and actuarial default assessments is most pronounced for long-dated credit exposures, making the choice of measure particularly important for long-term credit risk management.

---

**Exercise 3.** Consider a time-varying market price of default risk $\theta_t = a + b e^{-ct}$ with $a = 0.01$, $b = 0.04$, and $c = 0.5$. If $\lambda_t^{\mathbb{P}} = 0.02$ is constant, compute $\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \theta_t$ at $t = 0, 1, 2, 5$. Discuss the term structure of the credit risk premium.

??? success "Solution to Exercise 3"
    **Computing $\lambda_t^{\mathbb{Q}}$:** With $\lambda_t^{\mathbb{P}} = 0.02$ and $\theta_t = 0.01 + 0.04 e^{-0.5t}$:

    $$
    \lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \theta_t = 0.02 + 0.01 + 0.04 e^{-0.5t} = 0.03 + 0.04 e^{-0.5t}
    $$

    **Values at specific times:**

    | $t$ | $e^{-0.5t}$ | $\theta_t$ | $\lambda_t^{\mathbb{Q}}$ | Risk premium ratio |
    |:---:|:-----------:|:----------:|:------------------------:|:------------------:|
    | 0 | 1.0000 | 0.0500 | 0.0700 | 3.50 |
    | 1 | 0.6065 | 0.0343 | 0.0543 | 2.71 |
    | 2 | 0.3679 | 0.0247 | 0.0447 | 2.24 |
    | 5 | 0.0821 | 0.0133 | 0.0333 | 1.66 |

    **Discussion of the term structure:**

    The credit risk premium $\theta_t$ is front-loaded: it starts at 5% per year and decays exponentially to the asymptotic level $a = 1\%$.

    - **Short-term premium is highest ($\theta_0 = 5\%$):** This reflects elevated near-term uncertainty, perhaps due to current market stress or impending events (earnings, restructuring)
    - **Long-term premium converges to $a = 1\%$:** The residual premium reflects persistent systematic risk that does not diminish with time
    - **Decay rate $c = 0.5$:** The half-life is $\ln 2 / 0.5 \approx 1.39$ years, so the excess premium halves roughly every 1.4 years

    This term structure is empirically realistic: short-term CDS-implied intensities tend to be significantly higher than long-term intensities relative to physical default rates, especially for distressed or volatile names. The ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ decreases from 3.50 at $t=0$ to 1.66 at $t=5$, showing that the market's relative risk aversion for default risk diminishes at longer horizons.

---

**Exercise 4.** A rating agency reports a 5-year cumulative default probability of 3.2% for BBB-rated firms (physical measure). The market-implied 5-year cumulative default probability from CDS spreads is 11.5%. Compute the implied constant intensities under each measure and the multiplicative risk premium ratio. Explain why investors demand this premium.

??? success "Solution to Exercise 4"
    **Computing constant intensities from cumulative default probabilities:**

    The cumulative default probability over $[0, T]$ is $1 - e^{-\lambda T}$, so:

    $$
    \lambda = -\frac{\ln(1 - p)}{T}
    $$

    **Physical measure:** $p^{\mathbb{P}} = 0.032$, $T = 5$:

    $$
    \lambda^{\mathbb{P}} = -\frac{\ln(1 - 0.032)}{5} = -\frac{\ln(0.968)}{5} = \frac{0.03252}{5} = 0.650\% \text{ per year}
    $$

    **Risk-neutral measure:** $p^{\mathbb{Q}} = 0.115$, $T = 5$:

    $$
    \lambda^{\mathbb{Q}} = -\frac{\ln(1 - 0.115)}{5} = -\frac{\ln(0.885)}{5} = \frac{0.12222}{5} = 2.444\% \text{ per year}
    $$

    **Multiplicative risk premium ratio:**

    $$
    \frac{\lambda^{\mathbb{Q}}}{\lambda^{\mathbb{P}}} = \frac{2.444}{0.650} \approx 3.76
    $$

    **Why investors demand this premium:**

    The market-implied intensity is nearly 4 times the historical default rate. This premium exists because:

    1. **Systematic risk:** Defaults cluster during recessions when investor wealth is low and risk aversion is high. The marginal utility of a dollar lost to default is highest precisely during economic downturns.

    2. **Jump-to-default risk is non-diversifiable:** While individual defaults can be diversified, systematic default risk (correlated defaults) cannot. The 2008 crisis demonstrated that "rare" correlated defaults can impose massive losses.

    3. **Liquidity premium:** Corporate bonds and credit derivatives are less liquid than government bonds. Investors require additional compensation for bearing illiquidity, which is embedded in the credit spread and hence in $\lambda^{\mathbb{Q}}$.

    4. **Estimation risk:** Rating agencies use limited historical data. Investors may perceive true default rates as uncertain and demand compensation for this model uncertainty.

    A ratio of $\approx 3.76$ is consistent with empirical studies (e.g., Berndt et al., 2005; Driessen, 2005) that find ratios of 2--5 for investment-grade corporates.

---

**Exercise 5.** Derive the relationship between the CDS spread $s$ and the risk-neutral intensity $\lambda^{\mathbb{Q}}$ under the simplifying assumptions of constant intensity, constant risk-free rate $r$, continuous premium payments, and recovery of market value with rate $R$. Show that $s \approx (1-R)\lambda^{\mathbb{Q}}$.

??? success "Solution to Exercise 5"
    **Setup:** Constant $\lambda^{\mathbb{Q}}$, constant $r$, continuous premium payments at rate $s$, recovery $R$ of market value.

    **CDS premium leg (annuity):** The present value of continuous premium payments at rate $s$ until default or maturity $T$:

    $$
    \text{PV}_{\text{premium}} = s \int_0^T e^{-rt} \mathbb{Q}(\tau > t) \, dt = s \int_0^T e^{-rt} e^{-\lambda^{\mathbb{Q}} t} dt = s \int_0^T e^{-(r + \lambda^{\mathbb{Q}})t} dt
    $$

    $$
    = s \cdot \frac{1 - e^{-(r + \lambda^{\mathbb{Q}})T}}{r + \lambda^{\mathbb{Q}}}
    $$

    **CDS protection leg:** The present value of the protection payment $(1-R)$ at default:

    $$
    \text{PV}_{\text{protection}} = (1-R) \int_0^T e^{-rt} \lambda^{\mathbb{Q}} e^{-\lambda^{\mathbb{Q}} t} dt = (1-R)\lambda^{\mathbb{Q}} \int_0^T e^{-(r + \lambda^{\mathbb{Q}})t} dt
    $$

    $$
    = (1-R)\lambda^{\mathbb{Q}} \cdot \frac{1 - e^{-(r + \lambda^{\mathbb{Q}})T}}{r + \lambda^{\mathbb{Q}}}
    $$

    **Par CDS spread:** Setting $\text{PV}_{\text{premium}} = \text{PV}_{\text{protection}}$:

    $$
    s \cdot \frac{1 - e^{-(r+\lambda^{\mathbb{Q}})T}}{r + \lambda^{\mathbb{Q}}} = (1-R)\lambda^{\mathbb{Q}} \cdot \frac{1 - e^{-(r+\lambda^{\mathbb{Q}})T}}{r + \lambda^{\mathbb{Q}}}
    $$

    The common factors cancel exactly:

    $$
    s = (1-R)\lambda^{\mathbb{Q}}
    $$

    This is an **exact** result under these simplifying assumptions, not merely an approximation. However, we write $s \approx (1-R)\lambda^{\mathbb{Q}}$ in practice because the exact equality holds only under the idealized assumptions (constant intensity, constant rate, continuous premiums, RMV recovery). With discrete premium payments or stochastic intensity, the relationship becomes approximate.

    **Interpretation:** The CDS spread equals the expected loss rate, which is the product of the loss given default $(1-R)$ and the risk-neutral default intensity $\lambda^{\mathbb{Q}}$. For example, with $R = 40\%$ and $\lambda^{\mathbb{Q}} = 3\%$: $s = 0.6 \times 0.03 = 1.8\%$ = 180 bps.

---

**Exercise 6.** During a financial crisis, the CDS spread of a firm jumps from 100 bps to 500 bps while rating agencies maintain the same rating. Discuss whether this increase reflects a change in $\lambda^{\mathbb{P}}$, a change in the risk premium $\theta$, or both. What empirical evidence would help distinguish the two effects?

??? success "Solution to Exercise 6"
    **Decomposing the CDS spread increase:**

    The CDS spread jumps from 100 bps to 500 bps. Using $s \approx (1-R)\lambda^{\mathbb{Q}}$ with $R = 40\%$:

    - Before: $\lambda^{\mathbb{Q}}_{\text{before}} \approx 100/(10000 \times 0.6) \approx 1.67\%$
    - After: $\lambda^{\mathbb{Q}}_{\text{after}} \approx 500/(10000 \times 0.6) \approx 8.33\%$

    Since $\lambda^{\mathbb{Q}} = \lambda^{\mathbb{P}} + \theta$ (or multiplicatively $\lambda^{\mathbb{Q}} = \eta \cdot \lambda^{\mathbb{P}}$), the increase could reflect:

    **Change in $\lambda^{\mathbb{P}}$ (physical intensity):**

    - Actual credit deterioration: declining revenues, rising leverage, covenant breaches
    - If the rating agency maintains the rating, they may be slow to react (rating agencies are known for through-the-cycle rating methodology)

    **Change in $\theta$ (risk premium):**

    - During financial crises, risk aversion spikes and investors demand higher compensation
    - Liquidity dries up, increasing the liquidity premium embedded in spreads
    - Correlation fears increase (systemic risk), amplifying the systematic risk premium
    - Even if fundamental default risk is unchanged, the market price of bearing that risk rises

    **Most likely: both effects simultaneously.**

    During crises, both $\lambda^{\mathbb{P}}$ and $\theta$ increase, but empirical evidence suggests the **risk premium** accounts for the larger share:

    **Empirical evidence to distinguish the effects:**

    1. **Compare with rating migrations:** If the rating is unchanged and fundamentals are stable, the increase is predominantly risk premium
    2. **Equity volatility and leverage:** If equity price drops and volatility rises, $\lambda^{\mathbb{P}}$ likely increased (structural models link these)
    3. **Cross-sectional comparison:** If all CDS spreads widen (even for strong firms), the systematic risk premium component dominates
    4. **CDS-bond basis:** During crises, CDS spreads can widen more than bond spreads, suggesting a liquidity/risk premium channel
    5. **Historical default rates:** If realized default rates for the same rating cohort remain stable over subsequent years, the widening was mostly risk premium
    6. **KMV/Merton model implied $\lambda^{\mathbb{P}}$:** Compare the market-based estimate of physical default probability with the CDS-implied one; the gap measures $\theta$

---

**Exercise 7.** Suppose you estimate $\lambda^{\mathbb{P}}$ from historical default data and $\lambda^{\mathbb{Q}}$ from CDS markets. If you mistakenly use $\lambda^{\mathbb{Q}}$ for risk management (e.g., computing expected losses), would you overestimate or underestimate the true expected loss? Quantify the error for a portfolio with \$100 million notional, $\lambda^{\mathbb{P}} = 1\%$, $\lambda^{\mathbb{Q}} = 3\%$, and $R = 40\%$.

??? success "Solution to Exercise 7"
    Using $\lambda^{\mathbb{Q}}$ instead of $\lambda^{\mathbb{P}}$ for risk management would **overestimate** the true expected loss.

    **Correct expected loss (using $\lambda^{\mathbb{P}}$):**

    The one-year expected loss is:

    $$
    \text{EL}^{\mathbb{P}} = \text{Notional} \times (1 - R) \times \lambda^{\mathbb{P}} = \$100\text{M} \times 0.60 \times 0.01 = \$600{,}000
    $$

    More precisely, using the exact formula with cumulative default probability:

    $$
    \text{EL}^{\mathbb{P}} = \$100\text{M} \times (1-R) \times (1 - e^{-\lambda^{\mathbb{P}} \cdot 1}) = \$100\text{M} \times 0.60 \times 0.00995 = \$597{,}010
    $$

    **Incorrect expected loss (using $\lambda^{\mathbb{Q}}$):**

    $$
    \text{EL}^{\mathbb{Q}} = \$100\text{M} \times (1-R) \times \lambda^{\mathbb{Q}} = \$100\text{M} \times 0.60 \times 0.03 = \$1{,}800{,}000
    $$

    **Quantifying the error:**

    $$
    \text{Error} = \text{EL}^{\mathbb{Q}} - \text{EL}^{\mathbb{P}} = \$1{,}800{,}000 - \$600{,}000 = \$1{,}200{,}000
    $$

    $$
    \text{Relative error} = \frac{\text{EL}^{\mathbb{Q}} - \text{EL}^{\mathbb{P}}}{\text{EL}^{\mathbb{P}}} = \frac{1{,}200{,}000}{600{,}000} = 200\%
    $$

    The expected loss is **overstated by a factor of 3** (= $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$).

    **Practical consequences of this error:**

    - **Loan loss provisioning:** Over-reserving by \$1.2M per year per \$100M of exposure. For a large bank with \$100B of credit exposure, this error scales to \$1.2B annually.
    - **Capital allocation:** Overstating expected losses leads to excessive capital buffers under internal models, reducing return on equity and making the bank less competitive.
    - **Credit decisions:** The bank may reject profitable lending opportunities because the (incorrectly inflated) expected loss makes the risk-adjusted return appear negative.
    - **Performance evaluation:** Portfolio managers evaluated against risk-neutral expected losses will appear to systematically outperform, creating misleading track records.

    The key lesson is that $\lambda^{\mathbb{Q}}$ is the correct input for **pricing** (marking CDS, computing CVA), while $\lambda^{\mathbb{P}}$ is the correct input for **risk management** (expected loss, provisioning, stress testing). Conflating the two measures is one of the most common errors in credit risk practice.
